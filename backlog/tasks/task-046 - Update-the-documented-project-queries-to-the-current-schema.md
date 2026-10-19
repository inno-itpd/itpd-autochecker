---
id: TASK-046
title: Update the documented project queries to the current schema
status: Done
assignee: []
created_date: '2026-10-19 14:58'
updated_date: '2026-10-19 16:20'
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
- [x] #1 A search of `A3/grading_prompt.md`, `agents/grader.md`, and the helper scripts finds no `ProjectV2.description`, `projectV2.fields`, or `repository.issues(orderBy:)` selection; any stale selection found is replaced with a current field or the README and project-page route.
- [x] #2 The S6 check and procedure step 12 prefer `gh project list`, `gh project field-list`, and `gh project view`, and keep one GraphQL example for the project items and views.
- [x] #3 The documented GraphQL example uses current fields such as `shortDescription`, `items`, and `fieldValues`, and runs against one A3 project without `selectionMismatch` or an undefined-field error.
- [x] #4 The fallback that reads the project description uses `shortDescription` or the project page and README, and the instructions say which route answered.
- [x] #5 `markdownlint-cli2` passes.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Updated A3's S6 check, guardrails, and procedure step 12. The check now names `gh project list`, `gh project field-list`, and `gh project view` as the preferred field, option, visibility, and description routes, and keeps one GraphQL project query for the items and views. The query uses `shortDescription`, `public`, `readme`, `items(first: 100)` with each item's `fieldValues(first: 20)`, and `views(first: 20)`; it was run against the live A3 project `WellMadeTeam/projects/1` (number 1, 62 items, views Backlog/BOARD_LAYOUT, Team items/TABLE_LAYOUT, My items/TABLE_LAYOUT) and returned data without `selectionMismatch` or an undefined-field error. The project type's plain description field and a direct `fields` selection were confirmed to fail on the live schema; the prompt now names `shortDescription`, the project page, and the README as the description routes, and `gh project field-list` as the fields route, and requires `**Evidence:**` to say which route answered. Removed no stale selection because the search found none, and added tests/test_project_queries.py to keep the prompt, agents/grader.md, and the helper scripts free of the three stale selections and to assert the current routes and query fields stay documented. Validation: uv run pytest -q -> 319 passed; markdownlint-cli2 A3/grading_prompt.md -> 0 issues; repo-wide markdownlint-cli2 "**/*.md" -> 31 issues in 11 files, all pre-existing itpd-assignments-feedback/A1|A2/feedback/.../denis-feedback.md plus untracked TODO.md, left untouched. No files staged or committed.
<!-- SECTION:NOTES:END -->
