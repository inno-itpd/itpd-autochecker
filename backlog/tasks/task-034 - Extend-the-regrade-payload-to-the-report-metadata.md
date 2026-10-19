---
id: TASK-034
title: Extend the regrade payload to the report metadata
status: To Do
assignee: []
created_date: '2026-10-19 11:15'
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
- [ ] #1 The regrade payload accepts an optional top-level report object with snapshot, repository, primary_index, and notes
- [ ] #2 A snapshot and repository pair renders the canonical Primary index reviewed link and removes Notes about the snapshot
- [ ] #3 A payload that leaves the snapshot unresolved keeps Primary index reviewed: none and requires the notes bullet
- [ ] #4 An optional sections object replaces the summary, strengths, and main issues lists
- [ ] #5 The patched report is validated exactly as a full review, and an invalid payload fails closed without writing
- [ ] #6 inspect_feedback_segments.py reports the metadata and section changes a regrade would make
- [ ] #7 Tests cover the metadata patch, the notes removal, the unresolved case, and the fail-closed path
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
