---
id: TASK-035
title: Make the privacy scan tolerate cleaned work directories
status: To Do
assignee: []
created_date: '2026-10-19 11:15'
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
- [ ] #1 Name-token matches that fall entirely inside a known GitHub username from pdf-info.json are not reported, and the skipped count appears as a note line
- [ ] #2 Tokens shorter than four characters do not match prose, and the summary says how many were ignored
- [ ] #3 scan_privacy.py --feedback <path> --no-snapshot scans the report with tokens derived from the submission PDF, so a missing work/<team>/ does not block the gate
- [ ] #4 --no-snapshot without --feedback fails with a clear error
- [ ] #5 A real name in prose is still reported
- [ ] #6 Tests cover the false positive, the short token, --no-snapshot, and a real finding
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
