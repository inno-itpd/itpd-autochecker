---
id: TASK-028
title: Store per-team grader work under the feedback repo's work directories
status: Done
assignee: []
created_date: '2026-10-15 21:04'
updated_date: '2026-10-15 21:05'
labels: []
dependencies: []
modified_files:
  - tools/grader_tools/submission_pdf.py
  - tools/grader_tools/live_evidence.py
  - tools/grader_tools/privacy_scan.py
  - tools/grader_tools/snapshot_links.py
  - scripts/fetch_team_snapshot.py
  - scripts/collect_github_evidence.py
  - scripts/check_snapshot_links.py
  - agents/grader.md
  - AGENTS.md
  - A1/grading_prompt.md
  - A2/grading_prompt.md
  - .gitignore
  - tests/test_submission_pdf.py
  - tests/test_live_evidence.py
  - tests/test_privacy_scan.py
  - >-
    itpd-assignments-feedback/A2/feedback/Team 3 -
    WellMadeTeam_10939_assignsubmission_file/agent-feedback.md
  - >-
    itpd-assignments-feedback/A2/feedback/Team
    4_10940_assignsubmission_file/agent-feedback.md
ordinal: 28000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Per-team grader scratch lived in tmp/<A>/<team_dir>/ while the fetched snapshot lived in itpd-assignments-feedback/<A>/work/<team_dir>/, so repository data was split across two trees.
Move all per-team grader data into itpd-assignments-feedback/<A>/work/<team_dir>/: pdf-info.json, the GitHub evidence dumps, payloads, and the snapshot, which moves down into <team_dir>/snapshot/ so the fetcher can rebuild it without wiping its siblings (and so the privacy scan never scans the dumps).
Rename the pdf-info.json key work_dir to snapshot_dir and update the helpers, agent prompt, assignment prompts, tests, and existing data.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The fetcher writes itpd-assignments-feedback/<A>/work/<team_dir>/pdf-info.json and downloads the snapshot into <team_dir>/snapshot/
- [x] #2 collect_github_evidence.py and scan_privacy.py read and write the work directory; pdf-info.json exposes snapshot_dir
- [x] #3 AGENTS.md, agents/grader.md, and the A1/A2 grading prompts describe the new layout and uv run pytest passes
- [x] #4 Existing scratch and snapshot data is migrated and the repository tmp/ directory and its .gitignore rule are removed
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Layout: itpd-assignments-feedback/<A>/work/<team_dir>/ holds pdf-info.json, the evidence dumps, and payloads; the fetched snapshot moved down into <team_dir>/snapshot/, so a refetch wipes only snapshot/ and the privacy scan never scans the dumps. Renamed the pdf-info.json key work_dir -> snapshot_dir, the SnapshotFetchResult field, and the check_snapshot_links.py positional argument. Migration: moved 16 snapshots into snapshot/ and 10 scratch dirs from tmp/A1 and tmp/A2 into the work dirs (no name conflicts), patched 9 pdf-info.json files to the new key, rewrote 10 tmp/A2 citations in the two saved A2 reports and their payloads, then removed tmp/ and its .gitignore rule (the feedback submodule already ignores work/). Validation: uv run pytest 180 passed; check_feedback_report.py clean for both edited reports; markdownlint-cli2 clean except the pre-existing TODO.md and denis-feedback.md findings; A1/A2 extract_feedback.py regenerate dev.md and feedback_release.csv unchanged; live smoke test on A1 Team 2 ran fetch_team_snapshot, collect_github_evidence, scan_privacy, and check_snapshot_links green.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
