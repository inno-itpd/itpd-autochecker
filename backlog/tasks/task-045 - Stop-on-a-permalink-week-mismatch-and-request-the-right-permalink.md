---
id: TASK-045
title: Stop on a permalink week mismatch and request the right permalink
status: Done
assignee: []
created_date: '2026-10-19 14:58'
updated_date: '2026-10-19 16:10'
labels: []
dependencies: []
ordinal: 45000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
F8 from plan-1.md. Team 5's PDF permalinks `reports/week-02/README.md` at `ec5016f`, while the assignment expects `reports/week-03/README.md`. `scripts/fetch_team_snapshot.py` records `permalink_path` faithfully, but neither the script nor `summary.md` warns that the week is wrong; the operator had to notice and supply the right permalink by hand because the submission report provided a wrong one.

Decision: derive and record the permalink week, warn on a mismatch, and stop to request the correct permalink instead of silently grading a wrong-week target. The mismatch remains a submission shortfall in S12, and once the right permalink is supplied the snapshot still governs every file check.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 `scripts/fetch_team_snapshot.py` derives `permalink_week` from the permalink path and writes it, together with the assignment's expected week, to `pdf-info.json`.
- [x] #2 A mismatch prints a `warn:` line, repeats it in `summary.md`, exits non-zero instead of fetching or grading a wrong-week target, and prints the rerun command that requests the correct permalink.
- [x] #3 A `--permalink <url>` override replaces the PDF permalink, records `permalink_source=operator`, and lets the run continue; the override is documented in `agents/grader.md` and `AGENTS.md`.
- [x] #4 `agents/grader.md` step 8 states that a wrong-week PDF permalink is a submission shortfall in S12, that the snapshot still governs every file check, and that the grader requests the right permalink when the fetcher stops.
- [x] #5 Tests: a fixture PDF with a week-02 permalink produces the warning and the stop and records `permalink_week`; a correct-week PDF proceeds; the operator override proceeds.
- [x] #6 `uv run pytest` and `markdownlint-cli2` pass.
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
Implemented in tools/grader_tools/submission_pdf.py, scripts/fetch_team_snapshot.py, and tools/grader_tools/live_evidence.py, with docs and tests. Decisions: permalink_week(path) extracts the first week-NN segment (/reports/week-02/README.md and /reports/week-02 -> 2; no segment -> None), and a mismatch is raised only when a week was found and differs from ASSIGNMENT_CONFIG[assignment]["week"] as expected_week, so the existing bare-SHA and no-week stop paths stay non-mismatch. pdf-info.json gains permalink_week, expected_week, and permalink_week_mismatch next to permalink_path and the previously undocumented permalink_source; SnapshotFetchResult gains week_mismatch and snapshot_fetched (both default False). On a mismatch the fetcher prints a warn: line and a rerun command in the documented --permalink form, writes both to work/<team_dir>/summary.md (mode 0600), skips check_commit and fetch_snapshot, still writes pdf-info.json, and returns week_mismatch=True with snapshot_fetched=False. scripts/fetch_team_snapshot.py run exits 0 on success, 1 on mismatch, and 2 on SubmissionPdfError or SnapshotFetchError; a malformed --permalink raises SubmissionPdfError. The --permalink override requires a full GitHub blob/tree URL with a 40-character SHA, replaces the PDF permalink, records permalink_source=operator, prints the --repo ignored note when both are given, and a wrong-week override still stops. live_evidence rebuilds the same warning from pdf-info.json for both collect_github_evidence and regenerate_evidence_summary, inserts it near the header before the capped evidence lines, and keeps the 60-line cap, so --summary repeats it after a later digest. The shared warning text stays assignment-generic; the explicit S12 claim lives in agents/grader.md step 8 (with S8/S9 for A1/A2). Docs: agents/grader.md Paths key list plus steps 7-8, AGENTS.md helper reference and observed failure mode, docs/grader-policy.md submission/snapshot rules. Tests: week parser including no week, mismatch stop plus summary.md duplicate, CLI exit 1, A2 correct-week fetch (updated the existing A1 tests), override proceed, override plus --repo note, wrong-week override stop, malformed override raise and CLI exit 2, and the --summary digest warning. Validation: uv run pytest -q -> 315 passed; markdownlint-cli2 AGENTS.md agents/grader.md docs/grader-policy.md -> 0 issues; repo-wide markdownlint-cli2 "**/*.md" -> 31 issues in 11 files, all pre-existing itpd-assignments-feedback/A1|A2/feedback/.../denis-feedback.md plus untracked TODO.md, left untouched. Manual checks: A1 + week-02 fixture -> exit 1 with warn: week 2 / expects week 1 and pdf-info permalink_week=2, expected_week=1, permalink_week_mismatch=true, snapshot_fetched=false; --permalink week-01 -> exit 0, permalink_source=operator, snapshot_fetched=true; malformed --permalink -> exit 2; wrong-week --permalink -> exit 1. No files staged or committed; itpd-assignments-feedback/, TODO.md, and plan-1.md untouched.
<!-- SECTION:NOTES:END -->
