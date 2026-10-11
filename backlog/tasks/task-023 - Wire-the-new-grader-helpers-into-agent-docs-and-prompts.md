---
id: TASK-023
title: Wire the new grader helpers into agent docs and prompts
status: To Do
assignee: []
created_date: '2026-10-11 14:24'
labels: []
dependencies:
  - TASK-013
  - TASK-017
  - TASK-018
  - TASK-019
  - TASK-020
  - TASK-021
  - TASK-022
ordinal: 23000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Point the grader at the new helpers instead of the hand-rolled gh and jq pipelines while keeping the raw commands as fallback.
Update agents/grader.md steps 7 to 13, the A2 grading prompt procedure deltas, and the AGENTS.md workflow and new-assignment checklist.
Document the tmp scratch contracts: pdf-info.json keys and the dump file names each helper writes.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 agents/grader.md references the fetch, evidence, check, privacy, and link helpers with manual commands kept as fallback
- [ ] #2 A2/grading_prompt.md procedure deltas reference the helpers for PDF extraction, evidence collection, and privacy scanning
- [ ] #3 AGENTS.md lists the new scripts in the workflow and the adding-a-new-assignment checklist
- [ ] #4 markdownlint-cli2 passes on the changed Markdown files
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
