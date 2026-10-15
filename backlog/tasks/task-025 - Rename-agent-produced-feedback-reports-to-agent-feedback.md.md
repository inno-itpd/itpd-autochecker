---
id: TASK-025
title: Rename agent-produced feedback reports to agent-feedback.md
status: Done
assignee: []
created_date: '2026-10-15 19:22'
updated_date: '2026-10-15 19:22'
labels: []
dependencies: []
ordinal: 25000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agent-written feedback reports currently live at itpd-assignments-feedback/A<N>/feedback/markdown/<team_dir>/feedback.md, which is too easy to confuse with human or instructor-produced feedback. Rename the convention to agent-feedback.md everywhere: grader prompt and wrappers, scripts, extractor, docs, and tests, and rename the 16 existing reports with their dev.md links.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Grader prompt, wrappers, scripts, extractor, AGENTS.md, and submodule README refer to agent-feedback.md.
- [ ] #2 Existing A1 and A2 reports are renamed and dev.md regenerated; real names/emails still never leave the reports.
- [ ] #3 uv run pytest passes and the renamed reports pass scripts/check_feedback_report.py.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Renamed the agent report contract from feedback.md to agent-feedback.md: agents/grader.md, both harness wrappers, AGENTS.md, seven scripts (docstrings and help text), tools/grader_tools/extract_reports.py, five test modules, and the submodule README. Renamed all 16 committed reports under itpd-assignments-feedback/A{1,2}/feedback/markdown/ with git mv and regenerated both dev.md files; both feedback_release.csv files came out byte-identical, so only links changed. Decisions: script file names (check_feedback_report.py etc.) keep the general 'feedback report' concept and stay unchanged; backlog tasks 010/015/018/021 keep their historical wording. Validation: uv run pytest -> 180 passed; check_feedback_report.py passes on a renamed A1 and A2 report (validation plus markdownlint); markdownlint-cli2 on the changed Markdown reports no new findings.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
