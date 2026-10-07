---
id: TASK-010
title: Review A1 submissions
status: In Progress
assignee: []
created_date: '2026-10-07 10:15'
updated_date: '2026-10-07 21:21'
labels: []
dependencies: []
ordinal: 10000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Unpack the A1 Moodle export into itpd-assignments-feedback/A1/submissions/ and run the grader for all teams.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Every team has a valid feedback.md
- [x] #2 dev.md and feedback_release.csv are regenerated
- [ ] #3 Pending-review teams are checked by the instructor
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-08: Teams 2-9 reviewed in one parallel batch of 8 after 02ae36b (naming check dropped, Team 9 roster note). Team 1 S1 regraded (naming shortfall removed, stays partial). All 9 reports validate; extractor has no warnings; committed in feedback 9d88d68, bumped in 0d1fb95. Manual review: Teams 1, 3, 5, 6, 8, 9 (mostly board access: Miro/Figma). Waiting on AC #3 (instructor check). Grader judgement calls to review: T9 S8 permalink commit reached main only after a later merge; T9 S4 Miro board; T7 joint kickoff with another Modular LLM Gateway team (likely explains T1 S7 gap); T6 S7 member absent through connection problems; T5 S4 met-with-gap (Figma 403); T4 timestamps in meeting artifacts. Late snapshots (after hard deadline): T3, T7, T8, T9. Parallel graders shared one scratchpad; T3's commits.tsv was overwritten by T4 and redone in a subdirectory; reports cross-checked to cite only their own org.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
