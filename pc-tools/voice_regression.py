#!/usr/bin/env python3
"""voice_regression.py — exact rejected-wording regression for Ghost Weights.

Checks a candidate draft for exact occurrences of wording the author
rejected (from voice-rejected-anchors.json), broad review cues from the
JSON's review_patterns, and the spec-register lexicon (insurance, want,
turn, beat, arc) as contextual review cues — not automatic rejects.

Accepts both administrative-header and headerless candidates; the
first-dateline locator preserves source line offsets, and the raw-byte
SHA is hashed from the original bytes.

Usage: python3 voice_regression.py <candidate.md> --anchors <anchors.json>
Exit 0 always (this is a screen, not a gate); non-zero only on usage/file errors.
Zero hits do NOT certify voice.
"""
import argparse
import hashlib
import json
import re
import sys

BS = chr(92)

# first dateline: *Weekday, Month Day[, Year], H:MM a.m./p.m.*
FIRST_DATELINE_RE = re.compile(
    r"\*([A-Z][a-z]+day),\s+([A-Z][a-z]+)\s+(\d{1,2})(?:,\s*(\d{4}))?,\s*"
    r"(\d{1,2}):(\d{2})\s*([ap])\.m\.\*"
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate")
    ap.add_argument("--anchors", required=True)
    args = ap.parse_args()

    raw = open(args.candidate, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    text = raw.decode("utf-8")
    anchors = json.load(open(args.anchors, encoding="utf-8"))
    lines = text.splitlines()

    print(f"candidate: {args.candidate}")
    print(f"sha256: {sha}")
    m = FIRST_DATELINE_RE.search(text)
    if m:
        print(f"first dateline at line "
              f"{text[:m.start()].count(chr(10)) + 1}: {m.group(0)[:60]}")
    else:
        print("first dateline: NOT FOUND (headerless or malformed)")

    exact_hits = []
    for entry in anchors.get("reject", []):
        phrase = entry.get("phrase", "")
        notes = entry.get("notes", [])
        if not phrase:
            continue
        pat = re.compile(re.escape(phrase), re.IGNORECASE)
        for i, line in enumerate(lines, 1):
            if pat.search(line):
                exact_hits.append((i, notes, phrase))

    print(f"rejected wording: {len(exact_hits)} hits", end="")
    if exact_hits:
        print()
        for i, notes, phrase in exact_hits:
            print(f"  {i} [EXACT] notes {notes}: {phrase[:70]}")
    else:
        print()

    cues = []
    for pat_entry in anchors.get("review_patterns", []):
        name = pat_entry.get("name", "?")
        try:
            pat = re.compile(pat_entry.get("regex", ""), re.IGNORECASE)
        except re.error:
            print(f"  [warn] bad review_pattern regex for {name}; skipped")
            continue
        for i, line in enumerate(lines, 1):
            if pat.search(line):
                cues.append((i, name))

    print(f"review cues: {len(cues)} hits")
    for i, cue in cues:
        print(f"  {i} [review] {cue}")

    spec_hits = []
    for entry in anchors.get("spec_lexicon", []):
        term = entry.get("term", "?")
        try:
            pat = re.compile(entry.get("regex", ""), re.IGNORECASE)
        except re.error:
            print(f"  [warn] bad spec_lexicon regex for {term}; skipped")
            continue
        for i, line in enumerate(lines, 1):
            if pat.search(line):
                spec_hits.append((i, term))

    print(f"spec-register cues: {len(spec_hits)} hits "
          f"(contextual review, not rejects)")
    for i, term in spec_hits:
        print(f"  {i} [spec] {term} — check narration vs dialogue/artifact; "
              f"needs payload/POV disposition")

    print("Exact rejected-wording recurrence and broad search cues only; "
          "zero hits do not certify voice.")

if __name__ == "__main__":
    sys.exit(main())
