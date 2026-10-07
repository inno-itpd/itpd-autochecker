---
id: TASK-004
title: Port the report tooling to statuses
status: Done
assignee: []
created_date: '2026-10-07 10:15'
updated_date: '2026-10-07 10:17'
labels: []
dependencies: []
ordinal: 4000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Port tools/grader_tools and scripts/ from swp-autochecker with statuses instead of points, and a single shared validator.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 feedback_report.py parses and renders status-based reports
- [x] #2 validate.py is shared by the validator CLI and the extractor
- [x] #3 extract_reports.py writes dev.md and a |-delimited feedback_release.csv
- [x] #4 validate, inspect, patch and regrade scripts work end to end
- [x] #5 uv run pytest passes
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Validation is in tools/grader_tools/validate.py and shared by scripts/validate_feedback_report.py and the extractor (SWP had two diverging copies). Regrade calls patch_report in-process, validates before writing, and derives dev.md/CSV paths from the feedback path. Validation: uv run pytest -> 26 passed.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
