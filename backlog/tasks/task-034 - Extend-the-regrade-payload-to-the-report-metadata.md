---
id: TASK-034
title: Extend the regrade payload to the report metadata
status: Done
assignee: []
created_date: '2026-10-19 11:15'
updated_date: '2026-10-19 12:04'
labels: []
dependencies: []
ordinal: 34000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
regrade_feedback_segments.py cannot patch the metadata preamble, so moving Snapshot reviewed: none to a SHA required hand-editing during the Team 5 regrade. A regrade that changes the picture must also be able to rewrite the summary, strengths, and main issues.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The regrade payload accepts an optional top-level report object with snapshot, repository, primary_index, and notes
- [x] #2 A snapshot and repository pair renders the canonical Primary index reviewed link and removes Notes about the snapshot
- [x] #3 A payload that leaves the snapshot unresolved keeps Primary index reviewed: none and requires the notes bullet
- [x] #4 An optional sections object replaces the summary, strengths, and main issues lists
- [x] #5 The patched report is validated exactly as a full review, and an invalid payload fails closed without writing
- [x] #6 inspect_feedback_segments.py reports the metadata and section changes a regrade would make
- [x] #7 Tests cover the metadata patch, the notes removal, the unresolved case, and the fail-closed path
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
Implemented the extended regrade/patch payload through one shared preamble path.

Payload contract: optional `report` object (`snapshot`, `repository`, `primary_index`, `notes`) and optional `sections` object (`summary` 3-5 bullets, `strengths` and `main_issues_to_fix` at least one bullet, `main_issues` alias). Each report field is optional: absent keeps the saved value, null marks that side unresolved. `repository` accepts `org/repo` or `https://github.com/org/repo` and normalizes to the URL. `primary_index` defaults to the assignment config and rejects any other path. `notes` is required while the pair is unresolved, rejected once it is resolved, and resolving the pair removes the saved notes. Title and team are parsed from the saved preamble and preserved. Omitting `report` leaves the metadata bytes untouched; omitting `sections` keeps the saved bodies. The existing top-level string `summary`/`strengths`/`main_issues_to_fix` support remains, and supplying a section both ways is rejected.

Refactor: extracted `ReportMetadata`, `parse_preamble`, `render_preamble`, `normalize_repository`, `single_line_text`, and `bullet_list` into `tools/grader_tools/feedback_report.py`. `render_feedback_report.py` now uses the same renderer, so full-render output stays byte-identical. `patch_report` re-parses the rendered text and runs `validate_report` before returning, so both patch and regrade fail closed; both CLIs print `ERROR:` and exit 2 and leave the file untouched. `inspect_feedback_segments.py` predicts metadata and section changes and emits them as separate `predicted_report_metadata`/`predicted_report_sections` JSON keys and text blocks, read-only.

Tests added in `tests/test_segment_workflows.py` for metadata resolution, repository normalization, notes removal/requirement/rejection, unresolved pairs, section replacement, inspect text+JSON, regrade passthrough, and fail-closed file preservation; `tests/test_feedback_report.py` covers the parser/renderer round trip. Validation: `.venv/bin/python -m pytest -q` -> 233 passed; `markdownlint-cli2 docs/grading-feedback-format.md` -> 0 issues (linted only the changed Markdown because the repo-wide run has pre-existing failures in the feedback submodule and untracked TODO.md).
<!-- SECTION:NOTES:END -->
