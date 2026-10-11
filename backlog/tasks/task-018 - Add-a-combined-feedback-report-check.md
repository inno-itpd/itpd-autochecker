---
id: TASK-018
title: Add a combined feedback report check
status: To Do
assignee: []
created_date: '2026-10-11 14:23'
labels: []
dependencies: []
ordinal: 18000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Sessions ran scripts/validate_feedback_report.py and markdownlint-cli2 pairwise and sometimes fell back to npx when the binary was missing.
Add scripts/check_feedback_report.py with signature check_feedback_report.py <assignment> <feedback.md> that runs both checks in one command and exits non-zero when either fails.
It wraps the existing validator instead of duplicating report parsing and prints a clear actionable message when markdownlint-cli2 is not on PATH.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 One invocation runs report validation and markdownlint-cli2 and exits non-zero if either fails
- [ ] #2 A missing markdownlint-cli2 produces a clear error without a traceback
- [ ] #3 Tests cover pass, fail, and absent-linter cases and uv run pytest passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
