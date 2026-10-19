---
id: TASK-044
title: Add a SQLite evidence projection for issue and PR queries
status: Done
assignee: []
created_date: '2026-10-19 14:58'
updated_date: '2026-10-19 15:59'
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
- [x] #1 `scripts/collect_github_evidence.py` writes `evidence.sqlite` in the team work directory with tables for issues, labels, milestones, assignees, closing references, issue field values, pull requests, reviews, and pull-request files; absent or null arrays become NULL or zero rows instead of errors, and `--summary` rebuilds the database from saved dumps without calling `gh`.
- [x] #2 The issue projection includes number, state, title, type, milestone, assignees, and closing references, and documented SQL answers the S6 and S7 questions about field values, milestones, assignees, closing pull requests, and reviews without a `jq` error.
- [x] #3 `agents/grader.md` adds null-safe `jq` examples beside the context-budget examples: `(.closingIssuesReferences // [])[]`, `(.assignees // [])[]`, and `(.fieldValues.nodes // [])[]`.
- [x] #4 A pytest fixture builds the database from dumps containing null arrays and asserts the projection query returns the expected rows.
- [x] #5 The helper reference documents `evidence.sqlite`; `uv run python -m sqlite3` opens it with no new runtime dependency or dev-shell package.
- [x] #6 `uv run pytest` and `markdownlint-cli2` pass.
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
Added tools/grader_tools/evidence_sqlite.py (standard-library sqlite3 only) and wired it into scripts/collect_github_evidence.py and tools/grader_tools/live_evidence.py. Normal collection and --issue-fields rebuild evidence.sqlite from the saved dumps; --summary rebuilds summary.md and evidence.sqlite from the saved dumps and issue-fields.json when present, without calling gh, and the CLI prints the database line. Schema: tables issues, labels, issue_labels, milestones, issue_assignees, issue_closing_references, issue_field_values, pull_requests, pr_reviews, pr_files, and pr_closing_references (added beyond the suggested names so a pull request's own closingIssuesReferences is queryable instead of inferred from the issue side). The issue_projection view exposes number, state, title, type, milestone, milestone_due_on, labels, assignees, and closing_pull_requests; multi-valued columns are comma-separated ('' for a null array), states are lowercase, and issue-fields.json supplies type, milestone, and assignees. Decisions: explicit INSERT statements with None for absent values; a missing dump is an empty table, so issue-fields.json stays optional; malformed JSON raises EvidenceDatabaseError; foreign keys are declared for readability but not enforced so partial dumps still build; the database is written atomically through a 0600 temp file and rebuilt from scratch every time; live_evidence.ISSUE_FIELDS, PR_FIELDS, and the issue-fields projection are mirrored in ISSUE_DUMP_KEYS, PR_DUMP_KEYS, and ISSUE_FIELDS_DUMP_KEYS, and a test keeps them equal. Docs: AGENTS.md helper reference and a new Evidence database section; agents/grader.md Paths, step 11, a new Evidence database section with SQL for field values, milestones, assignees, closing pull requests, and reviews, and the three null-safe jq examples in Context budget. Tests: new tests/test_evidence_sqlite.py (null-array fixture projection, S7 queries, missing issue-fields, issue-fields-only, null top-level dumps, malformed dump, --summary rebuild without gh including a second rebuild proving freshness, stdlib sqlite3 CLI, dump-key drift) plus updates to tests/test_live_evidence.py (database write, issue-fields CLI output, summary output, unchanged dumps). Validation: uv run pytest -q -> 296 passed; markdownlint-cli2 AGENTS.md agents/grader.md -> 0 issues; repo-wide markdownlint-cli2 "**/*.md" -> 31 issues in 11 files, all pre-existing itpd-assignments-feedback/A1|A2/feedback/.../denis-feedback.md plus untracked TODO.md, left untouched. Live check: building from the real A3 Team 3 dumps produced 62 issues, 64 pull requests, 110 reviews, 216 files, and 44 pr_closing_references; the documented queries returned rows, and uv run python -m sqlite3 <db> "PRAGMA table_list;" listed every table plus issue_projection. Deviation: the pytest CLI check runs sys.executable -m sqlite3 (the same interpreter uv run uses) rather than spawning uv; the literal uv run python -m sqlite3 form was verified by hand. No files staged or committed.
<!-- SECTION:NOTES:END -->
