---
id: TASK-015
title: Review A2 submissions
status: In Progress
assignee: []
created_date: '2026-10-07 21:04'
updated_date: '2026-10-11 19:36'
labels: []
dependencies: []
ordinal: 15000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
After the A2 hard deadline (Saturday 10 October 2026, 23:59 UTC+3), unpack the A2 Moodle export into itpd-assignments-feedback/A2/submissions/ and run the grader for all teams against A2/itpd at a949e8d. Before the batch, check on the first team's task issue that userContentEdits gives the times the acceptance-criteria boxes were ticked, as the S1 rule in A2/grading_prompt.md assumes.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The S1 tick-order check is confirmed on a real task issue, or the rubric is adjusted
- [x] #2 Every team has a valid feedback.md
- [x] #3 dev.md and feedback_release.csv are regenerated
- [ ] #4 Pending-review teams are checked by the instructor
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-11: Full re-grade of all 7 teams in one parallel batch with the new grader helper scripts (fetch_team_snapshot, collect_github_evidence, check_snapshot_links, scan_privacy, check_feedback_report). Every segment re-verified from the snapshot and live GitHub evidence with permalinks; no observations reused from the first pass.
All 7 reports pass check_feedback_report.py (validator + markdownlint-cli2); A2/extract_feedback.py regenerated dev.md and feedback_release.csv with no warnings; uv run pytest 180 passed.
Status changes vs the first pass: T1 S4 partial->met and the S7 evidence gap cleared (the transcript shows the prototype was shown; the recorded 'Not bad' reaction is unsupported and stays a shortfall); T2 S4 met->partial, S7 missing->partial, S9 partial->met; T4 S10 partial->met; T5 S2 partial->met, S5 met->partial (US-13 Won't Have cites no BND-nn), S10 partial->met; T9 S3 met->partial (ALT-03 field order), S10 partial->met; T6 and T7 unchanged.
Manual review: Team 7 only (Zoom recording link passcode-gated on the single access check).
S1 tick-order check confirmed on real task issues via userContentEdits vs review submittedAt (e.g. Team 6 #10/#16 ticked after approval; Team 5 has no post-fill edits), so AC #1 needs no rubric change.
Grader judgement calls for the instructor: T1 S7 reaction-unsupported ruling; T5 S5 BND citation; T9 S3 ALT-03 'License' bullet; T7 S8 recording access.
Changed files sit uncommitted in the itpd-assignments-feedback submodule.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
