---
id: TASK-033
title: Make the report write-early and crash-safe
status: To Do
assignee: []
created_date: '2026-10-19 11:15'
labels: []
dependencies: []
ordinal: 33000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A crash mid-review leaves no validated report. Team 4's half-written report failed validation, and Team 9 crashed while correcting its own report. The validated report must reach disk as soon as the statuses are decided, and a missing segment must render as an explicit placeholder rather than an invalid file.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 render_feedback_report.py accepts an incomplete segment_updates and renders each missing segment as unverified with Evidence gaps: yes and an explicit placeholder bullet, so the file validates
- [ ] #2 Placeholders never render as met, and the rendered file passes validate_feedback_report.py
- [ ] #3 validate_feedback_report.py quotes the computed status counts beside the declared ones when the overall assessment does not match
- [ ] #4 agents/grader.md Output tells the grader to write the validated report as soon as the 13 statuses are decided, then run the gates
- [ ] #5 Output describes building the payload per segment group and writing work/<team>/payload.json after each group
- [ ] #6 Tests cover the partial render, the placeholder status, and the count-bearing error
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
