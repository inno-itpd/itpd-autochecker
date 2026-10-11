---
id: TASK-023
title: Wire the new grader helpers into agent docs and prompts
status: Done
assignee: []
created_date: '2026-10-11 14:24'
updated_date: '2026-10-11 16:58'
labels: []
dependencies:
  - TASK-013
  - TASK-017
  - TASK-018
  - TASK-019
  - TASK-020
  - TASK-021
  - TASK-022
ordinal: 23000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Point the grader at the new helpers instead of the hand-rolled gh and jq pipelines while keeping the raw commands as fallback.
Update agents/grader.md steps 7 to 13, the A2 grading prompt procedure deltas, and the AGENTS.md workflow and new-assignment checklist.
Document the tmp scratch contracts: pdf-info.json keys and the dump file names each helper writes.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 agents/grader.md references the fetch, evidence, check, privacy, and link helpers with manual commands kept as fallback
- [x] #2 A2/grading_prompt.md procedure deltas reference the helpers for PDF extraction, evidence collection, and privacy scanning
- [x] #3 AGENTS.md lists the new scripts in the workflow and the adding-a-new-assignment checklist
- [x] #4 markdownlint-cli2 passes on the changed Markdown files
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Wired the helper scripts into the docs, keeping the raw commands as fallback.

agents/grader.md: step 7 now runs scripts/fetch_team_snapshot.py (PDF metadata, commit and main check, snapshot refetch) with the pdftotext and tarball commands as fallback; step 8 reads the pdf-info.json resolution fields; step 10 runs scripts/check_snapshot_links.py (plus --issue-bodies after step 11); step 11 runs scripts/collect_github_evidence.py (labels/issues/prs/runs/commits dumps and issues/<n>.*, paths/<path>.json) with the grading-prompt gh/jq commands as fallback; step 12 runs scripts/scan_privacy.py with the grep fallback; step 13 points at image_info.py for screenshot/diagram checks. The Output section now uses scripts/check_feedback_report.py for validation, documents scripts/render_feedback_report.py for a payload-rendered report, and scans the finished report with scan_privacy.py --feedback. The scratch contracts (all pdf-info.json keys plus the collector dump names) are documented under Paths.

A2/grading_prompt.md procedure deltas: step 2 uses fetch_team_snapshot.py for PDF extraction (fallback list kept), step 3 uses its fetch, step 4 reads snapshot_time/on_main/on_main_status from pdf-info.json (raw gh fallback kept), step 5 prefers collect_github_evidence.py with the raw gh/jq pipelines kept as fallback, and step 12 prefers scan_privacy.py with the grep fallback.

AGENTS.md: workflow step 2 runs preflight.py and step 4 runs check_feedback_report.py; a new Grader helper scripts section lists preflight, fetch, evidence, links, privacy, check, render, and image_info; the adding-a-new-assignment checklist adds week_window_start/issue_cutoff and names the config-consuming helpers.

Validation: markdownlint-cli2 on AGENTS.md, agents/grader.md, and A2/grading_prompt.md reports 0 errors; uv run pytest -> 180 passed. The only repo-wide markdownlint findings are pre-existing (.claude/.opencode MD041 and the untracked TODO.md).
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
