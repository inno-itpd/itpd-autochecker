---
id: TASK-013
title: Add a gh helper for repeated process checks
status: To Do
assignee: []
created_date: '2026-10-07 10:16'
labels: []
dependencies: []
ordinal: 13000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Optional. Script the GitHub checks every assignment repeats (branch protection, PR reviews per member, Actions run status at the snapshot) so graders spend fewer tokens.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 scripts/ has a helper that prints a JSON summary for <org>/<repo> at <sha>
- [ ] #2 agents/grader.md tells the grader to use it
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
