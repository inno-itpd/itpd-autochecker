---
id: TASK-016
title: Re-check rubrics after itpd drops the team-number naming rule
status: To Do
assignee: []
created_date: '2026-10-07 21:10'
labels: []
dependencies: []
ordinal: 16000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The instructor withdrew the rule that organization and repository names carry the team number, but itpd requirements/repository-requirements.md (Repository Setup item 1) still states it. A1/grading_prompt.md has an S1 guardrail overriding it. Once itpd removes the rule, check that no rubric (A1, A2, later) requires it and drop the guardrail if it is no longer needed.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 itpd repository-requirements.md no longer requires the team number in names
- [ ] #2 No A<N>/grading_prompt.md requires it, and the A1 S1 guardrail is reviewed
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
