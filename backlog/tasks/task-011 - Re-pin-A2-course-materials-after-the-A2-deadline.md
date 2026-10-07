---
id: TASK-011
title: Re-pin A2 course materials after the A2 deadline
status: Done
assignee: []
created_date: '2026-10-07 10:16'
updated_date: '2026-10-07 21:10'
labels: []
dependencies: []
ordinal: 11000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A2 may change before the hard deadline (Sat 10 Oct 23:59). Re-pin A2/itpd to the commit published at the deadline and re-check A2/grading_prompt.md against it.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A2/itpd points at the commit published at the A2 hard deadline
- [ ] #2 A2/grading_prompt.md and assignment_config.py match that version
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Superseded by decision: A2 is graded against a949e8d, frozen, and is not re-pinned after the deadline. AC #1/#2 intentionally not applied; A2/grading_prompt.md and assignment_config.py already match a949e8d (tests pass).
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
