#!/usr/bin/env python3
"""gate_receipt.py — validate a gate receipt's evidence contract (Sol G1 / Council D1).

A gate marked `ran` is usable only when its artifact exists in the
receiving workspace, identifies the candidate actually read, and covers
its stated scope. This validator checks a gate-receipt markdown file for:

  1. Every `ran` gate row names a candidate path + 64-hex SHA.
  2. Every named artifact path exists on disk.
  3. Every artifact's actual SHA-256 matches the SHA in the row
     (when the row gives one).
  4. Every `ran` gate row names a reviewer+role OR a command+exit code.
  5. No row claims `ran` with an input-error exit (e.g. "exit 1",
     "input error") unless a bounded inheritance row is present.
  6. The receipt names the final candidate SHA it clears.

Usage: python3 tools/gate_receipt.py <gate-receipt.md> [--root DIR]
Exit 0: contract holds. Exit 1: violations listed.
This validates evidence presence and identity — not literary quality.
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

SHA_RE = re.compile(r"\b([0-9a-f]{64})\b")
# table rows: | gate | ran/not run/deferred | ... |
ROW_RE = re.compile(r"^\|([^|]*)\|([^|]*)\|.*\|?\s*$")
STATUS_WORDS = ("ran", "not run", "deferred")


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("receipt")
    ap.add_argument("--root", default=".")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    receipt = Path(args.receipt)
    if not receipt.exists():
        print(f"ERROR: receipt not found: {args.receipt}")
        return 1
    text = receipt.read_text(encoding="utf-8")
    errors = []

    # final candidate SHA declared?
    final_shas = SHA_RE.findall(text)
    if not final_shas:
        errors.append("no 64-hex candidate SHA anywhere in the receipt — "
                      "the receipt does not identify what it clears")

    ran_rows = 0
    for i, line in enumerate(text.splitlines(), 1):
        m = ROW_RE.match(line.strip())
        if not m:
            continue
        gate, status = m.group(1).strip().lower(), m.group(2).strip().lower()
        if not any(w in status for w in STATUS_WORDS):
            continue
        if "not run" in status or "deferred" in status:
            continue
        if "ran" not in status:
            continue
        ran_rows += 1
        row_shas = SHA_RE.findall(line)
        if not row_shas:
            errors.append(f"L{i} gate '{gate}': marked ran but names no "
                          "candidate/artifact SHA")
        # artifact paths: backticked .md paths in the row
        for pm in re.finditer(r"`([^`]*\.md)`", line):
            apath = root / pm.group(1)
            # also try relative to receipt's chapter dir
            if not apath.exists():
                alt = receipt.parent / pm.group(1)
                if alt.exists():
                    apath = alt
            if not apath.exists():
                errors.append(f"L{i} gate '{gate}': artifact "
                              f"'{pm.group(1)}' does not exist on disk")
                continue
            actual = sha256_of(apath)
            if row_shas and actual not in row_shas:
                errors.append(
                    f"L{i} gate '{gate}': artifact '{pm.group(1)}' "
                    f"SHA {actual[:12]}… matches no SHA in the row — "
                    "stale or wrong-candidate report")
        # reviewer/command evidence
        low = line.lower()
        has_reviewer = any(k in low for k in
                           ("reviewer", "dsh", "sol", "critic", "reader"))
        has_command = any(k in low for k in
                          ("python", "exit code", "exit 0", "command"))
        if not (has_reviewer or has_command):
            errors.append(f"L{i} gate '{gate}': marked ran but names "
                          "neither reviewer+role nor command+exit code")
        # input-error masquerading as ran
        if re.search(r"exit [1-9]|input error|traceback", low) and \
                "inheritance" not in low:
            errors.append(f"L{i} gate '{gate}': ran with an error exit and "
                          "no bounded inheritance row — a tool input error "
                          "is not zero findings")

    if ran_rows == 0:
        errors.append("no gate rows marked 'ran' found — nothing to validate")

    print("=" * 70)
    print("GATE RECEIPT EVIDENCE CHECK")
    print("=" * 70)
    for e in errors:
        print(f"ERROR: {e}")
    print("-" * 70)
    print(f"ran gates checked: {ran_rows}  errors: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
