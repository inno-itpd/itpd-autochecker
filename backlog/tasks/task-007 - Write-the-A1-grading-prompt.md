---
id: TASK-007
title: Write the A1 grading prompt
status: Done
assignee: []
created_date: '2026-10-07 10:15'
updated_date: '2026-10-07 10:17'
labels: []
dependencies: []
ordinal: 7000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A1/grading_prompt.md: segments and status guide derived from the A1 checklist and requirements at fe58ba7.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Every A1 checklist item maps to exactly one segment
- [x] #2 Segment names match tools/grader_tools/assignment_config.py
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Written by a subagent from A1 at fe58ba7; 24 checklist items mapped to S1-S9. Open instructor questions (deadline timezone, unmerged-PR commits, branch naming strictness, board mandatory?, 2-3 VPs required vs recommended, DEC traces) are listed in the session summary; resolve before the A1 review run.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
