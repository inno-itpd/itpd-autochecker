---
id: TASK-047
title: Re-verify the committed A3 regrade output after the fixes
status: Done
assignee: []
created_date: '2026-10-19 14:58'
updated_date: '2026-10-19 16:30'
labels: []
dependencies:
  - TASK-039
  - TASK-040
  - TASK-041
  - TASK-042
  - TASK-043
  - TASK-044
  - TASK-045
  - TASK-046
ordinal: 47000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Sequencing step 4 from plan-1.md, adjusted to the state on disk. The regrade output is already committed: `itpd-assignments-feedback` is at `ff7faad` (`fix(a3): update feedback`) with seven regenerated reports, `A3/dev.md`, and `A3/feedback_release.csv`, and this repository bumped the pointer in `6775432` (`chore(feedback): update`). That commit landed before the fixes, contrary to the "fix the prompt and scripts before committing the regrade output" decision, so this task re-verifies the committed reports against the fixed rubric and tooling and commits any correction. Team 5's S12 `Evidence gaps: yes` still needs instructor review before the output is treated as final.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The instructor has reviewed Team 5's S12 and decided whether it keeps `Evidence gaps: yes`; the report content changes only for that decision.
- [x] #2 TASK-039 through TASK-046 are done, so the rubric, tooling, and guidance used for the next batch are fixed and committed before this verification.
- [x] #3 All seven reports are re-checked against the fixed rubric and tooling, including the S2 hard deadlines, per-issue S6 fields, privacy findings, and permalink week; any status change is recorded in the submodule and the pointer is bumped here.
- [x] #4 `A3/dev.md` and `A3/feedback_release.csv` are re-extracted with no warnings, and every report passes `scripts/check_feedback_report.py` and `scripts/scan_privacy.py --feedback`; if nothing changes, the notes record that `ff7faad` stands.
- [x] #5 No unrelated submodule or working-tree changes are included.
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
Instructor decision on Team 5's S12: the submitted PDF is the Week 2 map while A3 asks for the Week 3 report, so S12 stays `missing` but becomes a verified shortfall and its `Evidence gaps: yes` is cleared. The later Week 3 report (`reports/week-03/README.md`, first committed 2026-10-18T19:32:08Z in `92310fa`, PR #101 merged as `233e19a`) was found, but the full re-grade against that snapshot is deferred to another session and no other Team 5 segment was changed. The S12 evidence now records that later snapshot, its verified shortfalls name the wrong-week submission, and the unverified bullet is gone. The regrade also regenerated `A3/dev.md` and `A3/feedback_release.csv`; Team 5's manual-review flag changed from `yes` to `no`, its per-segment statuses are unchanged (`partial 1 · missing 12`), and the other six rows are byte-identical.

Re-check of all seven reports: the S2 hard deadlines in the reports match the syllabus dates, and no report carries a stale soft deadline as a hard one; the three live mismatches (Team 1's milestones one day late, Team 4's `SPRINT-04` on `2026-10-22`, Team 6's `SPRINT-03` on `2026-10-18`) are already judged as S2 shortfalls. Fresh `--issue-fields` dumps were collected for all seven teams and queried through `evidence.sqlite`: Team 1 and Team 4 still carry no `Responsible` or `Accountable` value on any issue, so their S6 `missing` statuses stand; Teams 2, 3, 6, and 9 carry values and keep their S6 statuses; Team 5 has no values at the submitted Week 2 snapshot. The reports' S6 evidence for Teams 1 and 4 still quotes the empty organization list, but the per-issue data confirms the same statuses and the fixed prompt no longer relies on that list. Permalink weeks: Teams 2, 3, 4, 6, and 9 resolve to `reports/week-03/README.md`; Team 1's PDF carried a bare SHA resolved by `gh search commits` and its report names the Week 3 index; Team 5 is the wrong-week stop, which the patched S12 records. Privacy scans with `--feedback` report no findings for all seven reports.

Validation: `uv run python A3/extract_feedback.py` wrote 7 rows to `dev.md` and the release CSV with no warnings; `scripts/check_batch_ready.py A3` reports ready for all seven teams; every report passes `scripts/check_feedback_report.py` and `scripts/scan_privacy.py --feedback`; `uv run pytest -q` -> 319 passed; `markdownlint-cli2` on the changed Markdown -> 0 issues. The submodule commit is `043e694` (`fix(a3): mark Team 5's Week 2 submission as a verified shortfall`) with only the Team 5 report, `dev.md`, and `feedback_release.csv`; this repository bumped the pointer in `b5158e8` (`chore(feedback): update`). `TODO.md` and `plan-1.md` remain untracked and untouched, and no unrelated submodule change is included. Follow-up for another session: re-grade all Team 5 segments against the right Week 3 snapshot (deferred by the instructor).
<!-- SECTION:NOTES:END -->
