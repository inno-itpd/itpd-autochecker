---
id: TASK-059
title: Refine the A8 feedback batch for accuracy and actionability
status: Done
assignee: []
created_date: '2026-11-25 13:40'
updated_date: '2026-11-25 14:11'
labels:
  - feedback
  - A8
dependencies: []
priority: high
type: task
ordinal: 59000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The seven A8 compliance reports and their semantic companions were produced in one batch and pass the checkers, but they have not had a second evidence-backed pass. Re-audit every segment in full regrade mode against the saved snapshot and evidence, correct any wrong status, target, or claim, and tighten the student-facing prose and grounded next steps. Then regrade the semantic companions because every report hash changes.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 All seven A8 compliance reports are re-audited in full regrade mode against the saved SHA and saved evidence, with every status change backed by a verified artifact
- [x] #2 Every report still passes scripts/check_compliance_feedback.py and markdownlint-cli2, and the report privacy scan reports no findings
- [x] #3 Each report hash is refreshed in its semantic companion via semantic regrade, and every companion passes scripts/check_semantic_feedback.py with its ledger
- [x] #4 The pre-extraction gate passes for all seven teams, and A8/extract_feedback.py regenerates dev.md and feedback_release.csv without warnings
- [x] #5 The batch diff is reviewed for unexplained status churn, and the final status counts per team are recorded
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
All seven A8 reports were re-audited in full regrade mode against the saved SHA, then all seven semantic companions were regraded against the new report hashes.

Compliance: one status change only, Team 2 S9 `met -> partial` — the rubric requires the configuration-plan link in the root `AGENTS.md` layout section, and the snapshot links it under `## Configuration` (verified in the snapshot). The other six reports kept their statuses after re-verification. Corrections landed in all seven: withdrawn or re-owned shortfalls (Team 1 S18, Team 4 S2, Team 6 S18, Team 9 S12), post-cutoff timing fixed (Team 1 tags/releases, Team 3 S4/S7/S8/S14/S16, Team 9 merge time), counts and targets corrected (Team 4 S17 16 -> 18 PRs and #263, Team 6 S2 issue list, Team 2 milestone 16 -> 15 issues), and one added S17 summary-link shortfall (Team 7) plus Team 9's real-name shortfall restated.

Semantic: 7/7 regraded, 150 supported claims total, zero conflicts, every ledger's `report_sha256` matches its report. Three verdicts moved on re-verified evidence: Team 3 Publication `adequate -> thin` (PDF item 4 omits the recordings-folder link/access), Team 6 Results `thin -> adequate` (declared results shortfall is a result, SUS recomputes, events reconcile), Team 7 Publication `not yet adequate -> thin` (reader-effort gaps, not public-record contradictions). The other verdicts held.

Provider note: the seven original regrade runs died on a 403 key-limit cap; each team was resumed once with `record_resume.py` (1/4), the same sessions, and crash-safe incremental payload/render. All budgets were cleared with `--done`.

Validation: 14 files pass `check_compliance_feedback.py` / `check_semantic_feedback.py --ledger` plus markdownlint (0 issues); report and companion privacy scans `no findings`; `check_batch_ready.py A8` ready; `A8/extract_feedback.py` wrote 7 rows with no warnings; `uv run pytest` 486 passed. Repo-wide markdownlint still reports three pre-existing errors outside A8 (`A5/.../danila-feedback.md`, `TODO.md`), untouched by this pass.

Final counts (met/partial/missing/unverified, manual): T1 0/11/7/0 no · T2 2/8/8/0 no · T3 10/7/1/0 no · T4 2/11/5/0 no · T6 8/8/2/0 no · T7 5/9/4/0 yes · T9 7/7/4/0 no. Changes are uncommitted in the feedback submodule and the parent checkout.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Refined the A8 batch with one full compliance regrade and one semantic regrade per team. One evidence-backed status correction (Team 2 S9), corrections in all seven reports, three semantic verdict movements, 150 supported claims with zero conflicts. All 14 files validate and are privacy-clean, the gate is ready, exports are regenerated, and 486 tests pass.
<!-- SECTION:FINAL_SUMMARY:END -->
