---
id: TASK-014
title: Add CI for tests and Markdown lint
status: To Do
assignee: []
created_date: '2026-10-07 10:16'
labels: []
dependencies: []
ordinal: 14000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Optional. Run uv run pytest and markdownlint-cli2 on pushes and PRs, with actions pinned to full SHAs.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A workflow runs pytest and markdownlint-cli2
- [ ] #2 Actions are pinned to full commit SHAs
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
