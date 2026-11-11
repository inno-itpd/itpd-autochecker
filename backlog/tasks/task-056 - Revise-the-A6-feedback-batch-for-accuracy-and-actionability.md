---
id: TASK-056
title: Revise the A6 feedback batch for accuracy and actionability
status: Done
assignee: []
created_date: '2026-11-11 07:11'
updated_date: '2026-11-11 07:29'
labels: []
dependencies: []
priority: high
type: task
ordinal: 56000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The eight published A6 compliance reports (all teams except the non-submitting Team 8) were generated in one batch and are valid, lint-clean, and privacy-clean, but they have not had a second evidence-backed pass. Re-audit every segment against the saved snapshot and evidence, correct any wrong status, target, or claim, and tighten the student-facing prose and grounded next steps so the batch can be released with confidence. Keep the semantic companions in step because each report hash changes.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 All eight A6 compliance reports are re-audited in full regrade mode against the saved SHA and saved evidence, with every status change backed by a verified artifact
- [x] #2 Every report still passes scripts/check_compliance_feedback.py and markdownlint-cli2, and the privacy scan reports no findings
- [x] #3 Each report hash is refreshed in the semantic companion via semantic regrade, and every companion passes scripts/check_semantic_feedback.py with its ledger
- [x] #4 The pre-extraction gate passes for all eight teams, and A6/extract_feedback.py regenerates dev.md and feedback_release.csv without warnings
- [x] #5 The batch diff is reviewed for unexplained status churn, and the final status counts per team are recorded
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
Run one full-regrade compliance agent per A6 team, then one semantic regrade per team, validate, gate, and extract. Review the aggregate diff before reporting.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
All eight submitted A6 teams were regraded in full, then their semantic companions were regraded against the new report hashes.

Status changes (each verified against the rubric and the snapshot):
- Team 4: S11 met -> partial (threshold table header is `Can the new data settle it?`, TOS-03 answers `Partly.`, Proposal is `None`).
- Team 5: S6 met -> partial (docs/observability.md omits the university-network/private-only access statement).
- Team 6: S9 met -> partial (features observability entry added in PR #231 after ADR-008 in PR #217).
- Team 7: S18 met -> partial (reports/week-06/ai-usage.md leaves the team assessment as TODO).
- Team 9: S1 met -> partial (Planned Velocity 24 counts US-11/US-12 points that are absent from the field; field sum 18) and S7 partial -> met (two-series staging chart with the 345 ms timeout P95; literal legend is a caveat).
- Teams 1, 2, 3: no status changes, but their reports were corrected and their Summaries reduced to shortfalls only.

Final counts (met/partial/missing): 1: 0/15/3, 2: 4/13/1, 3: 7/10/1, 4: 3/13/2, 5: 11/6/1, 6: 11/7/0, 7: 5/9/4, 9: 12/6/0. All eight reports now carry `## Suggested next steps`.

Validation: all 8 compliance reports and all 8 semantic companions pass their checkers; every semantic ledger hash matches its report; report and semantic privacy scans are clean; `check_batch_ready.py A6` is ready with 8 teams; `markdownlint-cli2 --fix` reports 0 issues; `A6/extract_feedback.py` wrote 8 rows to dev.md and feedback_release.csv with no warnings; `uv run pytest` 465 passed.

The revisions are uncommitted in the feedback submodule (8 compliance reports, 8 semantic companions, dev.md, feedback_release.csv).
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Revised the A6 feedback batch with one full-regrade compliance pass and one semantic regrade per team. Five status corrections were made, all evidence-backed; the other three teams kept their statuses but had claims corrected. All 16 feedback files validate, semantic ledger hashes match, privacy scans are clean, the batch gate is ready, and the exports were regenerated.
<!-- SECTION:FINAL_SUMMARY:END -->
