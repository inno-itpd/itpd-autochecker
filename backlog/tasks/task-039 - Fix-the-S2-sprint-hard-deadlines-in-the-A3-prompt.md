---
id: TASK-039
title: Fix the S2 sprint hard deadlines in the A3 prompt
status: Done
assignee: []
created_date: '2026-10-19 14:57'
updated_date: '2026-10-19 15:16'
labels: []
dependencies: []
ordinal: 39000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
F1 from plan-1.md. The S2 guardrail at `A3/grading_prompt.md:182` lists Thursday soft deadlines (`2026-10-29` through `2026-11-26`) as sprint hard deadlines, while `course/syllabus.md` makes each hard deadline the following Friday at 23:59, with Weeks 2 and 3 as Saturday exceptions. Line 47 also calls the Week 4 hard deadline "soft". A grader following the numeric list would fail five sprint milestones and any plan milestone due in those weeks, so this changes how S2 is judged and must land before the next A3 batch.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The S2 guardrail lists `2026-10-17`, `2026-10-23`, `2026-10-30`, `2026-11-06`, `2026-11-13`, `2026-11-20`, and `2026-11-27` for `SPRINT-03` to `SPRINT-09`, and states that `course/syllabus.md` is authoritative.
- [x] #2 The Week 4 deadline bullet describes `2026-10-23` as a hard deadline, or is removed when `REL-04` does not need it.
- [x] #3 A regression test parses the Week 4 to Week 9 hard deadlines from `A3/itpd/course/syllabus.md` and asserts the prompt has them for `SPRINT-04` to `SPRINT-09`, plus the Week 3 Saturday exception `2026-10-17` for `SPRINT-03`; the expected dates stay in the test so it runs when the submodule is absent.
- [x] #4 The test fails when any of `2026-10-29`, `2026-11-05`, `2026-11-12`, `2026-11-19`, or `2026-11-26` is restored, and passes after the edit; no `2026-10-29` remains under `A3/`.
- [x] #5 `uv run pytest` and `markdownlint-cli2` pass.
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
Fixed the S2 guardrail to the syllabus hard deadlines 2026-10-17, 2026-10-23, 2026-10-30, 2026-11-06, 2026-11-13, 2026-11-20, and 2026-11-27 for SPRINT-03..SPRINT-09, and made course/syllabus.md authoritative (table dates are Thursday soft deadlines, hard deadlines are the following Friday at 23:59, Weeks 2-3 are Saturday exceptions). Rewrote the Week 4 bullet to call 2026-10-23 a hard deadline. Added tests/test_assignment_prompts.py coverage: expected dates kept in the test, syllabus Weeks 4-9 parsed and cross-checked when the submodule is present, prompt mappings asserted, each restored soft date rejected, and no stale date under A3/. Validation: uv run pytest -q -> 246 passed; markdownlint-cli2 A3/grading_prompt.md -> 0 issues; no 2026-10-29 under A3/. Deviation: repo-wide markdownlint-cli2 "**/*.md" fails on pre-existing A1/A2 denis-feedback.md files and the untracked TODO.md; those were left untouched.
<!-- SECTION:NOTES:END -->
