---
id: TASK-010
title: Review A1 submissions
status: In Progress
assignee: []
created_date: '2026-10-07 10:15'
updated_date: '2026-10-07 21:08'
labels: []
dependencies: []
ordinal: 10000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Unpack the A1 Moodle export into itpd-assignments-feedback/A1/submissions/ and run the grader for all teams.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Every team has a valid feedback.md
- [ ] #2 dev.md and feedback_release.csv are regenerated
- [ ] #3 Pending-review teams are checked by the instructor
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
