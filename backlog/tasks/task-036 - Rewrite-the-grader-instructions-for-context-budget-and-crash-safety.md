---
id: TASK-036
title: Rewrite the grader instructions for context budget and crash safety
status: To Do
assignee: []
created_date: '2026-10-19 11:15'
labels: []
dependencies: []
ordinal: 36000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
All 14 crashed runs read oversized input. The agent prompt needs a documented interpreter rule, a context budget, a crash-safe loop, and a return line that survives partial success.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The environment preamble documents both working invocations, uv run python and .venv/bin/python, with a one-line probe that picks one
- [ ] #2 The two uv failure causes are documented separately, with their distinct remedies
- [ ] #3 A Context budget section states the observed dump sizes, the bounded-output rule, and prefer four small projections over one large read
- [ ] #4 A crash-safe rule says to stop, narrow, and continue on unexpectedly large output, and never to re-read a summarized file
- [ ] #5 The return value must be emitted on partial success and name the exact path written
- [ ] #6 The prompt reads as one coherent instruction set with no duplicated step numbering, and markdownlint passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
