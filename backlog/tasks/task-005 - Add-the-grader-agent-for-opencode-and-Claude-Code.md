---
id: TASK-005
title: Add the grader agent for opencode and Claude Code
status: Done
assignee: []
created_date: '2026-10-07 10:15'
updated_date: '2026-10-07 10:17'
labels: []
dependencies: []
ordinal: 5000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
One canonical prompt in agents/grader.md with thin harness wrappers.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 agents/grader.md covers full review, partial regrade and segment inspect modes
- [x] #2 .opencode/agents/grader.md and .claude/agents/grader.md point to it
- [x] #3 AGENTS.md documents batched parallel reviews via grading.json
<!-- AC:END -->





## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
