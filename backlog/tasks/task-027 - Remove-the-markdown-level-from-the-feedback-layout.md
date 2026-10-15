---
id: TASK-027
title: Remove the markdown level from the feedback layout
status: Done
assignee: []
created_date: '2026-10-15 20:55'
updated_date: '2026-10-15 20:56'
labels: []
dependencies: []
ordinal: 27000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agent feedback reports now live at itpd-assignments-feedback/A<N>/feedback/<team_dir>/agent-feedback.md, one level shorter than the old feedback/markdown/ layout, because every feedback file is Markdown. Align tools/grader_tools/assignment_config.py, scripts/regrade_feedback_segments.py, scripts/render_feedback_report.py, agents/grader.md, AGENTS.md, and the tests, and finish the submodule migration whose A1 half was already renamed by hand.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The feedback_dir default, the grader prompt, AGENTS.md, and the tests all use feedback/<team_dir>/agent-feedback.md with no markdown level.
- [ ] #2 A1 and A2 feedback directories live directly under feedback/ in the submodule, and its README documents the new layout.
- [ ] #3 Re-extraction leaves both feedback_release.csv files byte-identical and changes dev.md only in its link paths.
- [ ] #4 uv run pytest passes and markdownlint-cli2 reports no issues on the changed Markdown.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Removed the redundant level in one pass: feedback_dir in assignment_config drives the extractor default, the regrade script derives the assignment root as feedback_dir.parent, and the grader prompt, AGENTS.md, the render docstring, and three test modules use the shorter path. Decisions: backlog tasks 009/025 keep their historical wording; the feedback/**/*.md lint glob now also covers the instructor *-feedback.md notes, which is intended; the submodule half was finished with git mv for A2 (A1 was already renamed in 74480aa) and its README documents the layout. Validation: uv run pytest 180 passed; markdownlint-cli2 (dev shell) reports 0 issues on the changed Markdown; check_feedback_report.py passes on A1 Team 1; inspect_feedback_segments.py reads A2 Team 9 from the new path; both release CSVs are byte-identical and dev.md differs only in link paths.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
