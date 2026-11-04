# Chapter audit runner (Linux)

Runs the WriteProject project's own deterministic audit scripts on this
Linux VM via PowerShell 7 (installed 2026-09-25 from Microsoft's Ubuntu
24.04 package feed).

## Source

- `run/scripts/chapter-control-audit.ps1` — copied from the project's
  `scripts/chapter-control-audit.ps1` @ `origin/main`, 2026-09-25.
- `run/scripts/originality-gate.ps1` — copied from the project's
  `scripts/originality-gate.ps1` @ `origin/main`, 2026-09-25.

## The only changes (documented, check with diff)

The project's scripts assume Windows path separators, which breaks their
path-prefix guards on Linux. The shim changes ONLY path handling:

1. `$rootPrefix = ... .TrimEnd('\') + '\'`
   → `.TrimEnd(DirectorySeparatorChar, AltDirectorySeparatorChar) + DirectorySeparatorChar`
   (works on both platforms).
2. `'continuity\*.md'` join-paths → `'continuity/*.md'`
   (forward slashes work on both platforms in .NET).

Every check — regexes, required fields, receipt decisions, error/warning
levels — is byte-identical to the project scripts. Verify any time with:
`diff <(gh-file.py scripts/chapter-control-audit.ps1 main) run/scripts/chapter-control-audit.ps1`
(modulo the documented lines above).

## Layout

`run/` acts as the project root (`$PSScriptRoot/..`):
- `run/scripts/` — the two scripts
- `run/continuity/` — repo-fetched project records (originality register,
  feedback catalog, review state, experience ledger) used by draft/release
  checks
- chapter + movement files are copied in per run

## Usage

```bash
cd ~/workspace/tools/chapter-audit/run
pwsh -NoProfile -File scripts/chapter-control-audit.ps1 \
  -ChapterPath chapter-08.md -ChapterNumber 8 \
  -MovementPath movement-08.md -Stage draft
```

Exit 1 = errors present. Warnings require inspection + recorded judgement.

## Ghost Weights naming (2026-10-01)

The `--chapter` argument accepts any path — pass the actual candidate
file (`chapters/08-static/candidate-r3.md` etc.); there is no `draft*.md`
glob to satisfy. `--stage draft` (the default) runs pre-freeze; the
release stage additionally requires the continuity records. Do not
fabricate a freeze record merely to satisfy a stage requirement.

## Limits

- Release-stage checks run against repo-fetched copies of the continuity
  files — same check logic as the project's machine, but the canonical
  release audit for the shared repo still runs on the project's side.
- The audit checks format, records, and structure. It does not certify
  voice or literary quality: on 2026-09-25 it passed the ch.8 Atlas draft
  with 0 errors / 0 warnings while a blind reader found seven real
  defects. The gate is necessary, not sufficient.
