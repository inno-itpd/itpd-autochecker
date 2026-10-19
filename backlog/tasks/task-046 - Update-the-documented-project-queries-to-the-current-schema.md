---
id: TASK-046
title: Update the documented project queries to the current schema
status: To Do
assignee: []
created_date: '2026-10-19 14:58'
labels: []
dependencies: []
ordinal: 46000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
F9 from plan-1.md. `ProjectV2.description` is now an undefined field, and `projectV2.fields` and `repository.issues(orderBy:)` selections raised `selectionMismatch` in the A3 batch. Agents adapted without losing findings, but the documented route must match the live schema before the next run.

Decision: prefer the `gh project` commands where they cover the need, replace the stale selections with `shortDescription` or the README and project-page route, and keep one GraphQL example that has been verified against a live A3 project.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A search of `A3/grading_prompt.md`, `agents/grader.md`, and the helper scripts finds no `ProjectV2.description`, `projectV2.fields`, or `repository.issues(orderBy:)` selection; any stale selection found is replaced with a current field or the README and project-page route.
- [ ] #2 The S6 check and procedure step 12 prefer `gh project list`, `gh project field-list`, and `gh project view`, and keep one GraphQL example for the project items and views.
- [ ] #3 The documented GraphQL example uses current fields such as `shortDescription`, `items`, and `fieldValues`, and runs against one A3 project without `selectionMismatch` or an undefined-field error.
- [ ] #4 The fallback that reads the project description uses `shortDescription` or the project page and README, and the instructions say which route answered.
- [ ] #5 `markdownlint-cli2` passes.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
