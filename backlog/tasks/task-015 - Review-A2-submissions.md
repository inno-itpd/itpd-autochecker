---
id: TASK-015
title: Review A2 submissions
status: To Do
assignee: []
created_date: '2026-10-07 21:04'
labels: []
dependencies: []
ordinal: 15000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
After the A2 hard deadline (Saturday 10 October 2026, 23:59 UTC+3), unpack the A2 Moodle export into itpd-assignments-feedback/A2/submissions/ and run the grader for all teams against A2/itpd at a949e8d. Before the batch, check on the first team's task issue that userContentEdits gives the times the acceptance-criteria boxes were ticked, as the S1 rule in A2/grading_prompt.md assumes.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The S1 tick-order check is confirmed on a real task issue, or the rubric is adjusted
- [ ] #2 Every team has a valid feedback.md
- [ ] #3 dev.md and feedback_release.csv are regenerated
- [ ] #4 Pending-review teams are checked by the instructor
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
