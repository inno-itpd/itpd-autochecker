---
id: TASK-035
title: Make the privacy scan tolerate cleaned work directories
status: Done
assignee: []
created_date: '2026-10-19 11:15'
updated_date: '2026-10-19 12:16'
labels: []
dependencies: []
ordinal: 35000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
scan_privacy.py cannot run after a grader cleans work/<team>/, and its name-token matcher reports false positives from real GitHub usernames that contain a short name fragment.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Name-token matches that fall entirely inside a known GitHub username from pdf-info.json are not reported, and the skipped count appears as a note line
- [x] #2 Tokens shorter than four characters do not match prose, and the summary says how many were ignored
- [x] #3 scan_privacy.py --feedback <path> --no-snapshot scans the report with tokens derived from the submission PDF, so a missing work/<team>/ does not block the gate
- [x] #4 --no-snapshot without --feedback fails with a clear error
- [x] #5 A real name in prose is still reported
- [x] #6 Tests cover the false positive, the short token, --no-snapshot, and a real finding
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Implemented in `tools/grader_tools/privacy_scan.py`, `scripts/scan_privacy.py`, `tests/test_privacy_scan.py`, and a two-line discoverability note in `docs/grader-policy.md`.

Decisions:
- Name-token scanning still uses whole-word patterns, but now filters tokens shorter than `MIN_NAME_TOKEN_LENGTH = 4` before compiling them; the ignored token count is reported as a `note:` line and exposed as `PrivacyScanResult.ignored_short_name_tokens`.
- `github_usernames` is read from `pdf-info.json` (same metadata the snapshot fetcher writes). A name-token match is skipped when its character span lies inside a case-insensitive username occurrence; the skipped match count is reported as a second `note:` line and exposed as `PrivacyScanResult.skipped_name_matches`. Values never enter the summary.
- `scan_privacy(..., no_snapshot=True)` requires `feedback_path` and derives `name_tokens`, `email_tokens`, `github_usernames`, and the recording link from `select_submission_pdf(submissions/<team_dir>, ASSIGNMENT_CONFIG[assignment]["primary_index"])`; missing directories and PDF failures become `PrivacyScanError` with exit code 2. `pdf-info.json` and `work/<team_dir>/` are not touched in this mode.
- The CLI rejects `--no-snapshot` without `--feedback` in `run()` with a clear `ERROR:` line and exit code 2, and both `--help` and the module docstring document the flag. The policy note keeps the flag discoverable without editing `agents/grader.md`, which a later task rewrites.
- Added tests for: a surname fragment inside `max-smirnov` skipped with its note, a 3-character token ignored with its count while a longer token still matches, a real name still reported, `--no-snapshot` scanning a report with `work/<team_dir>/` absent, `--no-snapshot` without `--feedback`, and a missing submission PDF error. The PDF test copies `tests/fixtures/submission-text-only.pdf` and is guarded by the same poppler `requires_poppler` marker as `tests/test_submission_pdf.py`.

Validation:
- `.venv/bin/python -m pytest -q` -> 239 passed in 2.68s.
- `.venv/bin/python -m pytest tests/test_privacy_scan.py -q` -> 25 passed in 0.10s.
- `markdownlint-cli2 docs/grader-policy.md` -> 0 issues in 0 files, exit code 0.
- `git diff --check` -> clean.
- `uv run` was not used because it is broken in this sandbox; `.venv/bin/python` is the documented equivalent here.
<!-- SECTION:NOTES:END -->
