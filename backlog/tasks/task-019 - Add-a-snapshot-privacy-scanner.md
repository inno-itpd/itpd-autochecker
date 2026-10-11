---
id: TASK-019
title: Add a snapshot privacy scanner
status: Done
assignee: []
created_date: '2026-10-11 14:23'
updated_date: '2026-10-11 15:39'
labels: []
dependencies:
  - TASK-017
modified_files:
  - tools/grader_tools/privacy_scan.py
  - scripts/scan_privacy.py
  - tests/test_privacy_scan.py
ordinal: 19000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Every grader session hand-rolled privacy greps with different regexes and false positives.
Add scripts/scan_privacy.py with signature scan_privacy.py <assignment> <team_dir> that consumes tmp/<A>/<team_dir>/pdf-info.json and scans the snapshot for emails, phone numbers, .env and key files, recording links outside meeting artifacts, and member name tokens.
Add --feedback <path> to scan a finished report file with the same rules.
Findings are reported by path and kind only; matched values never reach stdout.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Findings are grouped by rule and printed as path plus kind with no matched value
- [x] #2 The exit code reflects whether findings exist
- [x] #3 --feedback scans a report file with the same rules
- [x] #4 Unit tests cover each rule against fixtures and uv run pytest passes
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-11: added tools/grader_tools/privacy_scan.py and scripts/scan_privacy.py.

Rules (all value-free): personal email addresses (the A2 grep regex, minus RFC 2606 placeholder domains, the .example TLD, github.com, and GitHub noreply addresses; PDF email tokens override the ignore list); phone numbers (+international, parenthesized-area formats, and bare 7/8-prefixed 11-digit, with a 10-15 digit guard that rejects dates, versions, and long IDs); .env and key files by name (env files allow the sanitized .env.example/.sample/.template/.dist the repository requirements ask for; pem/key/p12/pfx/jks/keystore/ppk/p8 and id_* names are key files); recording links by host (Zoom, Telemost, Google Drive, Yandex Disk incl. yadi.sk, YouTube, VK Video) or exact match to the PDF recording link; and member name tokens from pdf-info.json matched case-insensitively as whole words. Recording links are only reported outside meeting artifacts (meeting/kickoff path components), per the task; personal data inside those files stays with the meeting segment (A2 S8 reports it there).

Mechanics: findings are deduped per rule/path/line and grouped by rule as path:line: kind; matched values never reach stdout. Binary files (NUL in the first 8192 bytes), files over 5 MiB, symlinks, and unreadable files are skipped and counted; .git is skipped. --feedback scans only the given report file with the same tokens and rules. Exit codes: 0 clean, 1 findings, 2 cannot scan (missing pdf-info.json, missing work dir, snapshot_fetched=false, missing report); errors print one line, no traceback. The scanner reads work_dir, recording_link, snapshot_fetched, and privacy_tokens from tmp/<A>/<team_dir>/pdf-info.json.

Validation: uv run pytest -> 96 passed, with 19 new tests in tests/test_privacy_scan.py covering each rule against fixtures, placeholder/date/ID false positives, binary/oversized/symlink skips, feedback mode, and exit codes 0/1/2. Real runs: scripts/scan_privacy.py on the A1 Team 2 and A2 Team 5 snapshots scans clean (exit 0), matching the saved reviews; --feedback on the saved A1 Team 2 report exits 1 with two member-name-token findings at lines 42 and 123 (branch names quoting a person), reported by path and line only. markdownlint-cli2 over the repo reports only the pre-existing untracked TODO.md findings; no Markdown changed (backlog/** is ignored).
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
