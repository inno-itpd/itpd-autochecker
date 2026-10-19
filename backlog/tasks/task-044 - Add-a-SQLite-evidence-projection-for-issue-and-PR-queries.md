---
id: TASK-044
title: Add a SQLite evidence projection for issue and PR queries
status: To Do
assignee: []
created_date: '2026-10-19 14:58'
labels: []
dependencies: []
ordinal: 44000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
F7 from plan-1.md. Ad-hoc `jq` over the evidence dumps fails on nulls where graders expect arrays: `closingIssuesReferences`, `assignees`, and project field values produced `Cannot iterate over null (null)` and `string ("") and array (["Closes",null]) cannot be added` in several sessions. Agents recovered, but each failure costs steps.

Decision: use SQLite instead of the flat `issues-projection.tsv` proposed in the plan. The collector writes a queryable `evidence.sqlite` beside the JSON dumps, and the grader instructions keep null-safe examples for the dumps the database does not cover. SQLite is in the Python standard library, so this adds no runtime dependency.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 `scripts/collect_github_evidence.py` writes `evidence.sqlite` in the team work directory with tables for issues, labels, milestones, assignees, closing references, issue field values, pull requests, reviews, and pull-request files; absent or null arrays become NULL or zero rows instead of errors, and `--summary` rebuilds the database from saved dumps without calling `gh`.
- [ ] #2 The issue projection includes number, state, title, type, milestone, assignees, and closing references, and documented SQL answers the S6 and S7 questions about field values, milestones, assignees, closing pull requests, and reviews without a `jq` error.
- [ ] #3 `agents/grader.md` adds null-safe `jq` examples beside the context-budget examples: `(.closingIssuesReferences // [])[]`, `(.assignees // [])[]`, and `(.fieldValues.nodes // [])[]`.
- [ ] #4 A pytest fixture builds the database from dumps containing null arrays and asserts the projection query returns the expected rows.
- [ ] #5 The helper reference documents `evidence.sqlite`; `uv run python -m sqlite3` opens it with no new runtime dependency or dev-shell package.
- [ ] #6 `uv run pytest` and `markdownlint-cli2` pass.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
