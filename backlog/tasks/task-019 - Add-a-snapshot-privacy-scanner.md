---
id: TASK-019
title: Add a snapshot privacy scanner
status: To Do
assignee: []
created_date: '2026-10-11 14:23'
labels: []
dependencies:
  - TASK-017
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
- [ ] #1 Findings are grouped by rule and printed as path plus kind with no matched value
- [ ] #2 The exit code reflects whether findings exist
- [ ] #3 --feedback scans a report file with the same rules
- [ ] #4 Unit tests cover each rule against fixtures and uv run pytest passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
