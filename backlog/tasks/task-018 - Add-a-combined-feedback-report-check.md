---
id: TASK-018
title: Add a combined feedback report check
status: Done
assignee: []
created_date: '2026-10-11 14:23'
updated_date: '2026-10-11 15:15'
labels: []
dependencies: []
modified_files:
  - scripts/check_feedback_report.py
  - tests/test_check_feedback_report.py
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
- [x] #1 One invocation runs report validation and markdownlint-cli2 and exits non-zero if either fails
- [x] #2 A missing markdownlint-cli2 produces a clear error without a traceback
- [x] #3 Tests cover pass, fail, and absent-linter cases and uv run pytest passes
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Added scripts/check_feedback_report.py (<assignment> <feedback.md>): it calls tools.grader_tools.validate.validate_feedback_file in-process, then runs markdownlint-cli2 from the repo root. Decisions: the linter is resolved with shutil.which and a missing binary fails with an actionable dev-shell message instead of an npx fallback; both checks always run so one invocation reports validation and lint findings together; the exit status is 1 when either check fails; a missing report file is reported without a traceback. Validation: uv run pytest -> 77 passed, including 5 new tests in tests/test_check_feedback_report.py covering pass, invalid report, lint findings, absent linter, and missing report; a manual run against the A1 Team 1 report exits 0; markdownlint-cli2 over the repo Markdown reports only the pre-existing untracked TODO.md findings, and no Markdown files changed.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
