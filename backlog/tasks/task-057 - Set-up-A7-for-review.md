---
id: TASK-057
title: Set up A7 for review
status: Done
assignee: []
created_date: '2026-11-16 16:26'
updated_date: '2026-11-16 16:27'
labels: []
dependencies: []
ordinal: 57000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Week 7 needs the same scaffolding as A5 and A6: the course submodule pinned at the week-7 merge, a 19-segment grading prompt with 5 semantic dimensions, the config entry, the extractor wrapper, updated tests and docs, and a validated batch of submissions. The operator chose setup only, to launch the review later.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A7/itpd is a submodule pinned at d7bcb1b24c142df8377da11ac5a1b4854e317fba
- [ ] #2 A7/grading_prompt.md defines the 19 configured segments and the 5 semantic dimensions in order
- [ ] #3 assignment_config.py carries A7 with the week-7 window, cutoff, primary index, and semantic dimensions
- [ ] #4 A7/extract_feedback.py carries ASSIGNMENT = "A7"
- [ ] #5 Tests and docs name A7 and the full suite passes
- [ ] #6 Every A7 submission resolves to a week-07 snapshot on main, and Team 8 is reported as a non-submission
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
A7 scaffolding is complete and validated. The course submodule is pinned at d7bcb1b (week-7 merge, 2026-11-12); the 19-segment prompt matches the config and carries the five semantic dimensions (Design, Evidence, Plan, Customer loop, Publication); the extractor wrapper and docs/tests name A7. Validation: uv run pytest 471 passed; markdownlint-cli2 clean on changed files; preflight healthy; all 8 PDF submissions resolve to a week-07 snapshot on main (Team 8 is a non-submission). Watch-outs for the batch: Team 1's PDF permalinks the repo root rather than reports/week-07/README.md; Team 4's PDF is 7 pages; Teams 1, 2, and 7 have no recording link; Team 2's member table yields no usernames. No review agents launched: the operator asked for setup only.
<!-- SECTION:NOTES:END -->
