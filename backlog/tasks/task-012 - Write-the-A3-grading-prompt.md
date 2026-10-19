---
id: TASK-012
title: Write the A3 grading prompt
status: Done
assignee: []
created_date: '2026-10-07 10:16'
updated_date: '2026-10-19 10:50'
labels: []
dependencies: []
ordinal: 12000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Add A3/ once Assignment 3 is published: pin A3/itpd, write grading_prompt.md, register segments, add extract_feedback.py.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 A3 is registered in assignment_config.py
- [x] #2 A3/grading_prompt.md passes markdownlint
- [x] #3 Every A3 checklist item and coverage-table row maps to exactly one segment
- [x] #4 A3/itpd is pinned at 23b22a6d637c0ac9c6a3350b377ae333cb42a082
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
A3/itpd is pinned at 23b22a6, the merge of `week-3` on 2026-10-14 and the last Week 3 course change before the Week 4 lecture and requirements landed. The later `week-3` commit 16005be only adds maintainer documentation (`course/decisions/a3.md`) and leaves `assignment-3.md` byte-identical.
Segments S1-S13 map the 22 checklist items and 17 coverage rows: threshold, plan and sprint milestones, risks, stack, DoD and contributing, issue fields and project, the MUP on `main`, docs site and setup, Week 2 follow-ups, the customer meeting, the release, the report and submission, and AI usage. Work items scheduled in a sprint, their `Responsible`/`Accountable` values, tags, releases, milestones, and the project are read live at `ISSUE_CUTOFF` = 2026-10-17T23:59:59+03:00; issue-field values have no API history, so procedure step 6 reads the timeline and says when it cannot settle the value at the cutoff.
Week 4 is not graded: product-code CI, the DoD's Week 4 CI item, and deployment are excluded. "Working" is judged from `docs/setup.md` and the snapshot, never by running the product.
Validation: `pytest` 187 passed (new A3 window and course-commit guards in tests/test_assignment_prompts.py); `markdownlint-cli2 A3/grading_prompt.md` clean; smoke run on Team 4 fetched the snapshot at 2aaa2ce, collected the evidence dumps, found no privacy or link findings, and rendered and validated a 13-segment report. `uv run python scripts/preflight.py` could not run in this sandbox because uv and the Nix cache are read-only, so the helpers were run directly from `.venv/bin/python`.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
