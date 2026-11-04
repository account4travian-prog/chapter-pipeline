#!/usr/bin/env python3
"""chapter_audit.py — Python port of WriteProject's scripts/chapter-control-audit.ps1.

Runs the same draft/release control checks on Linux, where PowerShell is not
installed. This is a faithful port, NOT the project's own script: do not
present its output as the PowerShell audit's output.

Usage:
    python3 chapter_audit.py --chapter <path> --number <N>
        [--movement <path>] [--stage draft|release]
        [--project-root <dir>]

Exit code: 0 when no error-level check fails, 1 otherwise (mirrors the .ps1).
"""

import argparse
import os
import re
import sys

TIMESTAMP_PATTERN = (
    r'^\*(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s+'
    r'\d{1,2}\s+'
    r'(January|February|March|April|May|June|July|August|September|October|November|December)'
    r'\s+188[45]\s+—\s+\d{1,2}:\d{2}\s+(a|p)\.m\.\*$'
)
SCENE_BREAK = r'^---\s*$'

CADENCE_PATTERNS = [
    r'It was better\.\s+It was not enough\.',
    r'\bbuy the day\b',
    r'\bThat was almost a relief\b',
    r'\bThat is not the same thing\b',
    r'\bSomething answered\b',
    r'\bfor reasons? (he|she|they) could not (name|explain|understand)\b',
    r'\bcould not help but\b',
    r'\blet out a breath\b',
]

PACKET_CONCEPTS = [
    ('calendar', r'(?im)^##\s+.*calendar'),
    ('scene spine', r'(?im)^##\s+.*scene spine'),
    ('viewpoint knowledge', r'(?im)^##\s+.*viewpoint'),
    ('physical/resource ledger', r'(?im)^##\s+.*(physical|resource)'),
    ('visual ledger', r'(?im)^##\s+.*visual'),
    ('older dependencies', r'(?im)^##\s+.*(older|dependenc)'),
    ('forbidden shortcuts', r'(?im)^##\s+.*forbidden'),
]


def resolve(project_root, candidate):
    """Mirror the .ps1 Resolve-ProjectPath: confine to the project root."""
    resolved = (os.path.abspath(candidate) if os.path.isabs(candidate)
                else os.path.abspath(os.path.join(project_root, candidate)))
    prefix = os.path.abspath(project_root).rstrip(os.sep) + os.sep
    if not resolved.startswith(prefix):
        raise SystemExit(f'Path is outside the project root: {candidate}\n'
                         f'(pass --project-root to audit files elsewhere)')
    return resolved


def main():
    ap = argparse.ArgumentParser(description='Python port of chapter-control-audit.ps1')
    ap.add_argument('--chapter', required=True, help='chapter markdown file')
    ap.add_argument('--number', required=True, type=int, help='chapter number')
    ap.add_argument('--movement', default=None, help='movement markdown file')
    ap.add_argument('--stage', default='draft', choices=['draft', 'release'])
    ap.add_argument('--project-root', default=os.path.expanduser('~/workspace/projects/WriteProject'))
    args = ap.parse_args()

    project_root = os.path.abspath(os.path.expanduser(args.project_root))
    chapter = resolve(project_root, args.chapter)
    if not os.path.isfile(chapter):
        raise SystemExit(f'Chapter not found: {chapter}')
    with open(chapter, encoding='utf-8') as f:
        content = f.read()

    results = []

    def add(check_id, level, passed, detail):
        results.append((check_id, level, passed, detail))

    add('proposal-status', 'error',
        bool(re.search(r'(?m)^\*\*Status:\*\* PROPOSED EXPERIMENT — not manuscript canon\.$', content)),
        'AI manuscript carries the exact proposal boundary.')
    add('title', 'error',
        bool(re.search(r'(?m)^#\s+\S', content)),
        'Chapter has a Markdown title.')
    add('unfinished-markers', 'error',
        not re.search(r'(?im)\b(TODO|TBD|FIXME)\b|\[\s*insert[^\]]*\]', content),
        'No unfinished drafting marker remains.')

    scene_breaks = len(re.findall(SCENE_BREAK, content, re.M))
    timestamps = len(re.findall(TIMESTAMP_PATTERN, content, re.M))
    add('scene-timestamp-count', 'error', timestamps == scene_breaks + 1,
        f'Found {timestamps} complete timestamps for {scene_breaks + 1} scenes.')
    add('legacy-scene-marker', 'error',
        not re.search(r'(?im)^\s*--scene break--\s*$', content),
        'No legacy scene-break placeholder remains.')

    segments = re.split(SCENE_BREAK, content, flags=re.M)
    with_ts = sum(1 for s in segments if re.search(TIMESTAMP_PATTERN, s, re.M))
    add('timestamp-per-scene', 'error', with_ts == len(segments),
        f'Every scene segment contains a complete timestamp ({with_ts}/{len(segments)}).')

    cadence_hits = []
    for pat in CADENCE_PATTERNS:
        cadence_hits += [m.group(0) for m in re.finditer(pat, content, re.I)]
    add('known-cadence-flags', 'warning', len(cadence_hits) == 0,
        'No known stock cadence pattern found.' if not cadence_hits
        else 'Review: ' + '; '.join(cadence_hits))

    if args.movement:
        m_arg = os.path.expanduser(args.movement)
        if os.path.isfile(m_arg):
            movement = os.path.abspath(m_arg)
        else:
            # fall back to project-root resolution (mirrors the .ps1)
            movement = resolve(project_root, args.movement)
        if not os.path.isfile(movement):
            raise SystemExit(f'Movement not found: {movement}')
        with open(movement, encoding='utf-8') as f:
            movement_content = f.read()
        for name, pat in PACKET_CONCEPTS:
            add(f'packet-{name.replace(" ", "-")}', 'error',
                bool(re.search(pat, movement_content)),
                f'Movement contains {name}.')

    if args.stage == 'release':
        def read(rel):
            p = os.path.join(project_root, *rel.split('/'))
            with open(p, encoding='utf-8') as f:
                return f.read()
        feedback = read('continuity/feedback-catalog.md')
        review_state = read('continuity/review-state.md')
        experience = read('continuity/experience-ledger.md')
        n = args.number
        add('feedback-section', 'error',
            bool(re.search(rf'(?im)^##\s+Chapter\s+{n}\b', feedback)),
            'Feedback catalog contains the chapter section.')
        add('review-state-capsule', 'error',
            bool(re.search(rf'(?im)^###\s+Chapter\s+{n}\b', review_state)),
            'Rolling review state contains the chapter capsule.')
        add('experience-retrospective', 'error',
            bool(re.search(rf'(?im)^###\s+Chapter\s+{n}\b', experience)),
            'Experience ledger contains the chapter retrospective.')

    word_count = len(re.findall(r"[\w][\w'’-]*", content, re.UNICODE))

    print(f'Chapter control audit (python port): {chapter} '
          f'({word_count} words, stage: {args.stage})')
    print(f'{"Id":<28}{"Level":<9}{"Passed":<8}Detail')
    for cid, level, passed, detail in results:
        print(f'{cid:<28}{level:<9}{str(passed):<8}{detail}')

    errors = [r for r in results if r[1] == 'error' and not r[2]]
    warnings = [r for r in results if r[1] == 'warning' and not r[2]]
    print(f'Result: {len(errors)} error(s), {len(warnings)} warning(s). '
          'Automated checks do not certify voice or literary quality.')
    print('NOTE: python port of scripts/chapter-control-audit.ps1 — '
          'not the project\'s PowerShell script.')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
