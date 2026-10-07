---
id: TASK-011
title: Re-pin A2 course materials after the A2 deadline
status: To Do
assignee: []
created_date: '2026-10-07 10:16'
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

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
