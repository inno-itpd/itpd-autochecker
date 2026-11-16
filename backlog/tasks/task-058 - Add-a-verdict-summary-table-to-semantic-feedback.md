---
id: TASK-058
title: Add a verdict summary table to semantic feedback
status: Done
assignee: []
created_date: '2026-11-16 20:51'
updated_date: '2026-11-16 20:53'
labels: []
dependencies: []
priority: medium
type: feature
ordinal: 58000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The semantic companion file records one verdict per dimension in separate sections, so a reader must scan the whole file to see its overall shape; the compliance report already gives that at-a-glance view with its segments table. Add a summary table to the semantic format so instructors can read every dimension's verdict in one place without changing the prose assessment.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The semantic feedback format documents a required `## Verdicts` table between `## How to read this` and the dimension sections.
- [x] #2 The semantic feedback validator rejects a missing table, mismatched dimension rows, a table verdict that differs from its section, duplicate or missing rows, out-of-order rows, and a bad heading anchor.
- [x] #3 The semantic agent prompt instructs the agent to write the table and keep its verdicts identical to the dimension sections.
- [x] #4 All existing A5, A6, and A7 semantic feedback files carry the table and pass `scripts/check_semantic_feedback.py`.
- [x] #5 The semantic validator tests cover the valid table and each failure mode, and the full pytest suite passes.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Add the required `## Verdicts` table to `docs/semantic-feedback-format.md` and the semantic agent prompt.
2. Parse and validate the table in `tools/autochecker/semantic_feedback.py`: one row per dimension section, same order, heading anchors, and verdicts equal to the sections.
3. Extend `tests/test_semantic_feedback.py` with the valid table and each failure mode.
4. Backfill the 25 existing A5/A6/A7 semantic files and validate each with `scripts/check_semantic_feedback.py`.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
The table sits between `## How to read this` and the dimension sections, mirroring the compliance segments table with `Dimension` and `Verdict` columns.

The validator compares the table against the file's own dimension sections, so an omitted dimension has no row and the check needs no cross-reference to the assignment config.

Anchors use `github_slug` from `snapshot_links`, the same slug rule the snapshot anchor checker applies.

Backfilled all 25 existing A5/A6/A7 semantic files. Validation: checker 25 checked, 0 failures; `uv run pytest` 480 passed (28 semantic tests); markdownlint on the changed Markdown 0 issues. A repo-wide markdownlint run still reports pre-existing MD009 in `A5/feedback/Team 4_10940_assignsubmission_file/denis-feedback.md` and MD034 in the separately modified `A6/feedback/Team 2 - OK_10938_assignsubmission_file/danila-feedback.md`.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Add a required `## Verdicts` summary table to the semantic companion file, mirroring the compliance report's segments table. The format doc and semantic agent prompt define the two-column table; the validator requires one linked row per dimension section and rejects missing, duplicate, out-of-order, unknown, anchor-mismatched, or verdict-mismatched rows. The 25 existing A5/A6/A7 semantic files were backfilled and all pass `scripts/check_semantic_feedback.py`. Tests cover the valid table and each failure mode; `uv run pytest` passes 480 tests and markdownlint is clean on the changed Markdown.
<!-- SECTION:FINAL_SUMMARY:END -->
