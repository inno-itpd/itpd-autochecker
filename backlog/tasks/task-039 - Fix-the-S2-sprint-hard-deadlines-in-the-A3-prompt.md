---
id: TASK-039
title: Fix the S2 sprint hard deadlines in the A3 prompt
status: To Do
assignee: []
created_date: '2026-10-19 14:57'
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
- [ ] #1 The S2 guardrail lists `2026-10-17`, `2026-10-23`, `2026-10-30`, `2026-11-06`, `2026-11-13`, `2026-11-20`, and `2026-11-27` for `SPRINT-03` to `SPRINT-09`, and states that `course/syllabus.md` is authoritative.
- [ ] #2 The Week 4 deadline bullet describes `2026-10-23` as a hard deadline, or is removed when `REL-04` does not need it.
- [ ] #3 A regression test parses the Week 4 to Week 9 hard deadlines from `A3/itpd/course/syllabus.md` and asserts the prompt has them for `SPRINT-04` to `SPRINT-09`, plus the Week 3 Saturday exception `2026-10-17` for `SPRINT-03`; the expected dates stay in the test so it runs when the submodule is absent.
- [ ] #4 The test fails when any of `2026-10-29`, `2026-11-05`, `2026-11-12`, `2026-11-19`, or `2026-11-26` is restored, and passes after the edit; no `2026-10-29` remains under `A3/`.
- [ ] #5 `uv run pytest` and `markdownlint-cli2` pass.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
