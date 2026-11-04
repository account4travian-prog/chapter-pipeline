#!/usr/bin/env python3
"""Ghost Weights deterministic audit — process facts only.

Checks:
  1. Record presence per chapter dir (packet, freeze-record, run-manifest,
     at least one draft candidate).
  2. STATUS.md consistency: every current-proposed/accepted file exists
     and its SHA-256 matches the recorded hash.
  3. Freeze-record SHA match: every SHA-256 named in a freeze record
     matches its file byte-for-byte.
  4. Dateline shape and order: the chapter's first dateline is the full
     form (weekday, month day, year, time); every scene opens with a
     dateline; scene dates are non-decreasing.
  5. Quantity/date-interval sweep: every "<number> <days|hours|minutes|
     weeks|seconds>" (numeral AND spelled-out) in the current candidate
     is reported with its passage; any value not in the chapter's
     expected-quantities.md is flagged as a WARNING with the offending
     passage and the expected basis.

  6. Prose register (WARNINGS only): narration dates take ordinals,
     1-12 clocks need an a.m./p.m. datum (00/13-23 pass as 24-hour);
     datelines and fenced code/log blocks are exempt.
  7. Packet gate (ch.9+): REQUIRED blocks present; consumer-UI rows
     when call/share/video language appears.
  8. Location tree: node files carry type/parent/established; parent
     and home references resolve to real nodes.
  9. Repo hygiene: no leading/trailing-whitespace filenames; WORKFLOW.md
     carries the Council A1-A6 markers; defect-log.md carries S24-S29.

Severity: errors block the gate they guard (exit 1). Warnings need human
inspection and a recorded disposition (exit 0).

Passing this audit does NOT certify voice, pace, technical truth, or
reader enjoyment. It never rewrites prose.

Usage: python3 tools/audit.py [--root DIR] [--status PATH] [--chapter NN-slug]
                              [--candidate PATH] [--phase prehandoff|freeze]
"""

import argparse
import hashlib
import re
import sys
from datetime import datetime
from pathlib import Path

NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90,
}
UNITS = ["day", "days", "hour", "hours", "minute", "minutes", "week",
         "weeks", "second", "seconds", "min", "mins", "hr", "hrs",
         "month", "months", "year", "years", "gpu-hour", "gpu-hours"]

QTY_RE = re.compile(
    r"\b(\d+|[a-z]+(?:-[a-z]+)?)[-\s](" + "|".join(UNITS) + r")\b",
    re.IGNORECASE,
)
# "four hundred GPU-hours" — multiplier form the single-token regex misses
HUNDRED_RE = re.compile(
    r"\b(one|two|three|four|five|six|seven|eight|nine)\s+hundred[-\s]("
    + "|".join(UNITS) + r")\b",
    re.IGNORECASE,
)
DATELINE_RE = re.compile(
    r"\*([A-Z][a-z]+day),\s+([A-Z][a-z]+)\s+(\d{1,2})(?:,\s*(\d{4}))?,\s*"
    r"(\d{1,2}):(\d{2})\s*([ap])\.m\.\*"
)
SHA_RE = re.compile(r"\b([0-9a-f]{64})\b")
MD_RE = re.compile(r"`?([\w.\-/]+\.md)`?")
STATUS_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|.*?\|\s*\*\*(accepted|current proposed|proposed|published)\*\*\s*\|"
    r"\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`"
)
# any table row that starts like a chapter row but didn't parse
CHAPTER_ROW_LIKE_RE = re.compile(r"^\|\s*\d+\s*\|")

# --- Register check (Sol G4 / Council D6) ---
MONTHS = ("January|February|March|April|May|June|July|August|September|"
          "October|November|December")
CARDINAL_DATE_RE = re.compile(
    rf"\b({MONTHS})\s+(\d{{1,2}})(?!\d)\b(?!\s*(?:st|nd|rd|th)\b)")
# 1-12 clock without leading zero and without a.m./p.m. datum;
# 00-09/13-23 and zero-padded 01-12 pass as 24-hour forms
BARE_CLOCK_RE = re.compile(
    r"(?<![\d:])([1-9]|1[0-2]):([0-5]\d)(?!\s*[ap]\.m\.)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)

# --- Packet gate (DSH 6 / Council D7) ---
PACKET_REQUIRED_CH9 = ["## Operational invariants row",
                       "## Prop-origin registry",
                       "## Spec-register note",
                       "Location-tree checklist"]

# --- Control presence (DSH 1 / Council D7) ---
REQUIRED_WORKFLOW_MARKERS = ["Council A1", "Council A2", "Council A3",
                             "Council A4", "Council A5", "Council A6"]
REQUIRED_DEFECT_SECTIONS = ["## S24", "## S25", "## S26",
                            "## S27", "## S28", "## S29"]


def word_to_num(token: str):
    token = token.lower()
    if token.isdigit():
        return int(token)
    if token in NUMBER_WORDS:
        return NUMBER_WORDS[token]
    if "-" in token:
        parts = token.split("-")
        if len(parts) == 2 and parts[0] in NUMBER_WORDS and parts[1] in NUMBER_WORDS:
            return NUMBER_WORDS[parts[0]] + NUMBER_WORDS[parts[1]]
    if token.endswith("hundred") or "hundred" in token:
        # "four hundred" arrives as two tokens; handle "four-hundred"
        parts = token.replace("-", " ").split()
        if len(parts) == 2 and parts[0] in NUMBER_WORDS and parts[1] == "hundred":
            return NUMBER_WORDS[parts[0]] * 100
    return None


def norm_unit(unit: str) -> str:
    u = unit.lower()
    if u in ("min", "mins"):
        return "minutes"
    if u in ("hr", "hrs"):
        return "hours"
    if u.endswith("s"):
        return u
    return u + "s"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, msg):
        self.errors.append(msg)

    def warning(self, msg):
        self.warnings.append(msg)

    def ok(self):
        return not self.errors


def parse_expected_quantities(chapter_dir: Path):
    """Read expected-quantities.md -> set of (value, unit)."""
    p = chapter_dir / "expected-quantities.md"
    expected = set()
    if not p.exists():
        return None
    for line in p.read_text().splitlines():
        m = re.match(r"\s*-\s*(\d+)\s+([a-z-]+)\b", line.strip(), re.IGNORECASE)
        if m:
            expected.add((int(m.group(1)), norm_unit(m.group(2))))
    return expected


def check_quantity_sweep(chapter_dir: Path, candidate: Path, rep: Report):
    expected = parse_expected_quantities(chapter_dir)
    if expected is None:
        rep.warning(f"{chapter_dir.name}: no expected-quantities.md — "
                    "quantity sweep skipped (add the file to enable it)")
        return
    text = candidate.read_text()
    # 1:1 offset-preserving flatten so quantities split across line
    # breaks ("four hundred\nGPU-hours") are still caught
    flat = re.sub(r"\s", " ", text)
    line_starts = [0]
    for m in re.finditer(r"\n", text):
        line_starts.append(m.start() + 1)

    def lineno(off: int) -> int:
        import bisect
        return bisect.bisect_right(line_starts, off)

    for i, m in enumerate(QTY_RE.finditer(flat)):
        val = word_to_num(m.group(1))
        if val is None:
            continue
        unit = norm_unit(m.group(2))
        report_match(candidate, m, val, unit, text, lineno, expected, rep)
    for m in HUNDRED_RE.finditer(flat):
        if any(m.start() < h.end() and m.end() > h.start()
               for h in QTY_RE.finditer(flat)):
            continue
        val = word_to_num(m.group(1)) * 100
        unit = norm_unit(m.group(2))
        report_match(candidate, m, val, unit, text, lineno, expected, rep)


def report_match(candidate, m, val, unit, text, lineno, expected, rep):
    if (val, unit) in expected:
        return
    ln = lineno(m.start())
    start = max(0, m.start() - 60)
    snippet = re.sub(r"\s+", " ", text[start:m.end() + 60]).strip()[:120]
    rep.warning(
        f"{candidate.name} L{ln}: unexpected quantity "
        f"'{m.group(0).strip()}' ({val} {unit}) — not in "
        f"expected-quantities.md. Passage: \"{snippet}\". "
        f"Expected basis: {sorted(expected)}"
    )


def check_datelines(chapter_dir: Path, candidate: Path, rep: Report):
    text = candidate.read_text()
    found = list(DATELINE_RE.finditer(text))
    if not found:
        rep.error(f"{candidate.name}: no datelines found at all")
        return
    first = found[0]
    if not first.group(4):
        rep.error(f"{candidate.name}: first dateline lacks the year "
                  "(chapter must open with weekday, month day, year, time)")
    prev = None
    for m in found:
        wd, mon, day, year, hh, mm, ap = m.groups()
        dt = datetime.strptime(
            f"{mon} {day} {year or '2027'} {hh}:{mm} {ap.upper()}M",
            "%B %d %Y %I:%M %p",
        )
        if prev and dt < prev[0]:
            rep.error(
                f"{candidate.name}: scene dateline out of order — "
                f"'{m.group(0)[:60]}' precedes '{prev[1][:60]}'")
        prev = (dt, m.group(0))


def check_freeze_shas(chapter_dir: Path, rep: Report):
    fr = chapter_dir / "freeze-record.md"
    if not fr.exists():
        return
    lines = fr.read_text().splitlines()
    checklist = chapter_dir / "release-checklist.md"
    checklist_text = checklist.read_text() if checklist.exists() else ""
    for i, line in enumerate(lines):
        for hm in SHA_RE.finditer(line):
            sha = hm.group(1)
            # nearest PRECEDING .md filename: same line first, then up
            # to 4 lines back ("candidate `draft-r2.md` ... SHA-256: `…`"
            # puts the name before the hash)
            best, best_dist = None, 99
            for j in range(min(len(lines) - 1, i), max(-1, i - 5), -1):
                fms = list(MD_RE.finditer(lines[j]))
                if not fms:
                    continue
                if j == i:
                    # same line: filename must precede the hash
                    fms = [f for f in fms if f.start() < hm.start()]
                    if not fms:
                        continue
                cand = fms[-1].group(1)
                best, best_dist = cand, i - j
                break
            if not best:
                rep.warning(f"{fr.name} L{i+1}: SHA {sha[:12]}… has no "
                            "preceding filename — cannot verify")
                continue
            target = (chapter_dir / Path(best).name)
            if not target.exists():
                rep.error(f"{fr.name}: named file '{best}' does not exist "
                          f"(SHA {sha[:12]}…)")
                continue
            actual = sha256_of(target)
            if actual != sha:
                if actual in checklist_text:
                    rep.warning(
                        f"{fr.name}: '{best}' no longer matches the SHA "
                        f"recorded here ({sha[:12]}…); its current hash "
                        f"{actual[:12]}… is recorded in "
                        f"release-checklist.md — documented supersession "
                        f"(pre-acceptance freeze revised per author "
                        f"feedback). Freeze record kept as the historical "
                        f"document; do not retro-edit.")
                else:
                    rep.error(f"{fr.name}: SHA mismatch for '{best}': "
                              f"recorded {sha[:12]}…, file is "
                              f"{actual[:12]}…")


def check_status_file(root: Path, status_path: Path, rep: Report):
    if not status_path.exists():
        rep.error(f"STATUS file missing: {status_path}")
        return []
    current = []
    unparsed = 0
    for line in status_path.read_text(encoding="utf-8").splitlines():
        m = STATUS_ROW_RE.match(line)
        if m:
            _num, _state, rel, sha = m.groups()
            current.append((rel, sha))
        elif CHAPTER_ROW_LIKE_RE.match(line):
            unparsed += 1
    if unparsed:
        rep.error(f"STATUS.md: {unparsed} chapter row(s) not parsed — "
                  "state word outside accepted|current proposed|proposed|"
                  "published, or malformed row")
    if not current:
        rep.warning("STATUS.md: no accepted/proposed chapter rows parsed")
    for rel, sha in current:
        target = root / rel
        if not target.exists():
            rep.error(f"STATUS.md: current file '{rel}' does not exist")
            continue
        actual = sha256_of(target)
        if actual != sha:
            rep.error(f"STATUS.md: hash mismatch for '{rel}': recorded "
                      f"{sha[:12]}…, file is {actual[:12]}… "
                      "(stale STATUS entry or wrong candidate)")
    return current


def check_records(chapter_dir: Path, rep: Report, pre_freeze: bool):
    if not (chapter_dir / "packet.md").exists():
        rep.error(f"{chapter_dir.name}: missing required file packet.md")
    for req in ("freeze-record.md", "run-manifest.md"):
        if not (chapter_dir / req).exists():
            msg = f"{chapter_dir.name}: missing {req}"
            if pre_freeze:
                rep.warning(msg + " (pre-freeze: required at freeze)")
            else:
                rep.error(f"missing required file {req}")
    drafts = (sorted(chapter_dir.glob("draft*.md")) +
              sorted(chapter_dir.glob("candidate-*.md")))
    if not drafts:
        rep.error(f"{chapter_dir.name}: no draft/candidate file found")


def check_register(candidate: Path, rep: Report):
    """Prose register: narration dates take ordinals; 1-12 clocks need a
    datum; 24-hour forms pass. Datelines and fenced code/log blocks are
    exempt. Warnings only — a legitimate form must not block."""
    text = candidate.read_bytes().decode("utf-8")
    exempt = [(m.start(), m.end()) for m in DATELINE_RE.finditer(text)]
    exempt += [(m.start(), m.end()) for m in FENCE_RE.finditer(text)]

    def is_exempt(pos):
        return any(s <= pos < e for s, e in exempt)

    line_starts = [0]
    for m in re.finditer(r"\n", text):
        line_starts.append(m.start() + 1)

    def lineno(off: int) -> int:
        import bisect
        return bisect.bisect_right(line_starts, off)

    for m in CARDINAL_DATE_RE.finditer(text):
        if is_exempt(m.start()):
            continue
        rep.warning(
            f"{candidate.name} L{lineno(m.start())}: cardinal date "
            f"'{m.group(0)}' in narration — prose dates take ordinals "
            "(datelines and code blocks exempt)")
    for m in BARE_CLOCK_RE.finditer(text):
        if is_exempt(m.start()):
            continue
        rep.warning(
            f"{candidate.name} L{lineno(m.start())}: bare clock "
            f"'{m.group(0)}' without a.m./p.m. datum — 1-12 forms need "
            "a datum; zero-padded 00-12 and 13-23 pass as 24-hour")


def check_packet_fields(chapter_dir: Path, rep: Report):
    p = chapter_dir / "packet.md"
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    m = re.search(r"[Cc]hapter\s+(\d+)", text)
    if not m or int(m.group(1)) < 9:
        return  # pre-tree chapters audited separately
    for block in PACKET_REQUIRED_CH9:
        if block.lower() not in text.lower():
            rep.error(f"{p.name}: missing REQUIRED block '{block}'")
    if ("Consumer-UI" not in text and
            re.search(r"(call|share|screen[- ]?share|video)", text, re.I)):
        rep.error(f"{p.name}: consumer-UI interaction present but no "
                  "Consumer-UI rows block")


def check_location_tree(root: Path, rep: Report):
    loc = root / "locations"
    if not loc.exists():
        return
    slugs = {p.stem: p for p in loc.glob("*.md")
             if p.stem.lower() != "readme"}
    for slug, p in slugs.items():
        text = p.read_text(encoding="utf-8")
        for field in ("type", "parent", "established"):
            if not re.search(rf"(?m)^{field}:", text):
                rep.error(f"locations/{p.name}: missing '{field}:'")
        for field in ("parent", "home"):
            fm = re.search(rf"(?m)^{field}:\s*(\S+)", text)
            if (fm and fm.group(1) not in ("none", "null") and
                    fm.group(1) not in slugs):
                rep.error(f"locations/{p.name}: {field} "
                          f"'{fm.group(1)}' has no node")


def check_filename_hygiene(root: Path, rep: Report):
    for p in root.rglob("*"):
        if p.name != p.name.strip():
            rep.error("filename has leading/trailing whitespace: "
                      f"{p.relative_to(root)}")


def check_workflow_markers(root: Path, rep: Report):
    wf = root / "WORKFLOW.md"
    if not wf.exists():
        rep.error("WORKFLOW.md missing")
        return
    text = wf.read_text(encoding="utf-8")
    for marker in REQUIRED_WORKFLOW_MARKERS:
        if marker not in text:
            rep.error(f"WORKFLOW.md is missing standing control {marker}")
    dl = root / "defect-log.md"
    if dl.exists():
        dtext = dl.read_text(encoding="utf-8")
        for sec in REQUIRED_DEFECT_SECTIONS:
            if sec not in dtext:
                rep.error(f"defect-log.md is missing {sec}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--status", default=None)
    ap.add_argument("--chapter", default=None,
                    help="only audit one chapter dir, e.g. 02-wont-fix")
    ap.add_argument("--candidate", default=None,
                    help="exact candidate file to inspect, e.g. "
                    "chapters/08-static/candidate-r6.md")
    ap.add_argument("--phase", default="freeze",
                    choices=["prehandoff", "freeze"],
                    help="prehandoff: freeze-only record requirements "
                    "become warnings")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    status_path = Path(args.status) if args.status else root / "STATUS.md"
    rep = Report()
    pre_freeze = args.phase == "prehandoff"

    check_filename_hygiene(root, rep)
    check_workflow_markers(root, rep)
    check_location_tree(root, rep)

    chapters = sorted((root / "chapters").glob("*"))
    if args.chapter:
        chapters = [c for c in chapters if c.name == args.chapter]
    if not chapters:
        rep.error("no chapter directories found")
    else:
        for ch in chapters:
            check_records(ch, rep, pre_freeze)
            check_freeze_shas(ch, rep)
            check_packet_fields(ch, rep)

    current = check_status_file(root, status_path, rep)

    # dateline + quantity + register sweeps run on the STATUS-named
    # current files, or on --candidate when given
    sweep_targets = []
    if args.candidate:
        sweep_targets.append(root / args.candidate)
    else:
        sweep_targets = [root / rel for rel, _sha in current]

    for target in sweep_targets:
        if not target.exists():
            rep.error(f"sweep target does not exist: {target}")
            continue
        # find the chapter dir this file belongs to (Windows-safe)
        chdir = None
        tres = target.resolve()
        for ch in chapters:
            try:
                if tres.is_relative_to(ch.resolve()):
                    chdir = ch
                    break
            except (OSError, ValueError):
                continue
        if chdir is None:
            rep.warning(f"sweep target {target.name} is not inside a "
                        "chapter dir — dateline/quantity/register sweeps "
                        "skipped")
            continue
        check_datelines(chdir, target, rep)
        check_quantity_sweep(chdir, target, rep)
        check_register(target, rep)

    print("=" * 70)
    print("GHOST WEIGHTS DETERMINISTIC AUDIT — process facts only")
    print("=" * 70)
    for e in rep.errors:
        print(f"ERROR: {e}")
    for w in rep.warnings:
        print(f"WARN:  {w}")
    print("-" * 70)
    print(f"errors: {len(rep.errors)}  warnings: {len(rep.warnings)}")
    print("NOTE: passing does not certify voice, pace, technical truth, "
          "or reader enjoyment.")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
