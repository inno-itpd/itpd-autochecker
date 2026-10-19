---
id: TASK-037
title: Tighten the A3 rubric wording and add the prompt sync test
status: Done
assignee: []
created_date: '2026-10-19 11:15'
updated_date: '2026-10-19 12:22'
labels: []
dependencies: []
ordinal: 37000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Two rubric rules were ambiguous in the batch. S1's statement-wording guardrail sits far from its met bullets, and one agent revisited its own met call; S3's summary-table placement was judged partial by one agent. The cutoff rule also needs one determinism sentence.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 S1 states beside its met bullets that the failure statement's wording is never judged, only the table's shape and tracing
- [x] #2 S3 says in both the met bullet and the partial shortfall list that the summary table sits above the first RISK-nn section, matching the course requirement
- [x] #3 Procedure step 6 states that post-cutoff file state is a caveat and never a status change, except in a segment that judges the snapshot
- [x] #4 tests/test_assignment_prompts.py asserts the - S<n>: <name> lines, the status-guide headings, and the segment count against assignment_config.py
- [x] #5 uv run pytest and markdownlint-cli2 pass
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
Implemented TASK-037.

Decisions:
- S1: moved the statement-wording rule out of `**Guardrails:**` and into the `**met:**` list as a third statements bullet, scoped to the failure statement's wording ("The failure statement's wording is the session's and is never judged; only the table's shape and its tracing are."), so the rule sits beside the table-shape and tracing bullets.
- S3: the `met` bullet now says the summary table sits above the first `## RISK-nn` section, and the `**partial:**` shortfall list adds a table that sits below the first risk section or after the risk sections, matching `A3/itpd/requirements/risks-requirements.md` ("The register opens with a summary table above the sections").
- Procedure step 6: added one determinism bullet, "Post-cutoff file state is a caveat and never a status change, except in a segment that judges the snapshot, which reads the file at `SNAPSHOT_TIME`."; the issue-state, comments/edits, and evidence-gap bullets are unchanged.
- Tests: `tests/test_assignment_prompts.py` now compiles `SEGMENT_LINE` and `STATUS_HEADING` (em dash, re.MULTILINE) patterns; `test_prompt_segments_match_config` asserts the `- S<n>: <name>` lines, asserts the `## Status guide` `### S<n> — <name>` headings, and asserts both counts equal the configured segment count.
- No segments or steps renumbered and no unrelated sections restructured. A1/A2 prompts, `AGENTS.md`, `agents/grader.md`, `plan.md`, `TODO.md`, other backlog tasks, and the feedback submodule are untouched.

Validation:
- `.venv/bin/python -m pytest -q` -> 239 passed in 2.73s.
- `.venv/bin/python -m pytest tests/test_assignment_prompts.py -q` -> 15 passed in 0.03s.
- `markdownlint-cli2 A3/grading_prompt.md` -> exit 0, "Summary: 0 issues in 0 files".
<!-- SECTION:NOTES:END -->
