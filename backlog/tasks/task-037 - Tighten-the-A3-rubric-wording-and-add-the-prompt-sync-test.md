---
id: TASK-037
title: Tighten the A3 rubric wording and add the prompt sync test
status: To Do
assignee: []
created_date: '2026-10-19 11:15'
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
- [ ] #1 S1 states beside its met bullets that the failure statement's wording is never judged, only the table's shape and tracing
- [ ] #2 S3 says in both the met bullet and the partial shortfall list that the summary table sits above the first RISK-nn section, matching the course requirement
- [ ] #3 Procedure step 6 states that post-cutoff file state is a caveat and never a status change, except in a segment that judges the snapshot
- [ ] #4 tests/test_assignment_prompts.py asserts the - S<n>: <name> lines, the status-guide headings, and the segment count against assignment_config.py
- [ ] #5 uv run pytest and markdownlint-cli2 pass
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
