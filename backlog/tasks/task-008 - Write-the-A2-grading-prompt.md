---
id: TASK-008
title: Write the A2 grading prompt
status: Done
assignee: []
created_date: '2026-10-07 10:15'
updated_date: '2026-10-07 10:21'
labels: []
dependencies: []
ordinal: 8000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A2/grading_prompt.md: segments and status guide derived from the A2 checklist, coverage table and W1-W2 requirements.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Every A2 checklist item and coverage-table row maps to exactly one segment
- [x] #2 Segment names match tools/grader_tools/assignment_config.py
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Written by a subagent from A2 at a949e8d; 23 checklist items and 14 coverage rows mapped to S1-S10. Issues are judged as of the snapshot commit time (createdAt, timeline events, userContentEdits). Open instructor questions (timezone, rules.md Friday vs A2 Saturday hard deadline, issues created after snapshot, CON minimum, Team-not-contested MUP verdict) are listed in the session summary. tests/test_assignment_prompts.py guards prompt/config segment drift.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
