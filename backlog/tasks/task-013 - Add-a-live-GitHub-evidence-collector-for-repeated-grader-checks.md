---
id: TASK-013
title: Add a live GitHub evidence collector for repeated grader checks
status: To Do
assignee: []
created_date: '2026-10-07 10:16'
updated_date: '2026-10-11 14:24'
labels: []
dependencies:
  - TASK-017
ordinal: 13000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
From the A2 batch study: every grader session hand-rolled the same gh pipelines and hit stdout truncation, field-name mismatches, and inconsistent pagination.
Add scripts/collect_github_evidence.py with signature collect_github_evidence.py <assignment> <team_dir> that reads tmp/<A>/<team_dir>/pdf-info.json, dumps paginated labels, issues, pull requests, runs, and commits as JSON into the team scratch dir, and prints only a compact summary with file paths.
Support --issues for comments, timeline, and userContentEdits drilldowns and --paths for repository path histories.
Encode the field lists from the A2 grading prompt procedure step 5 so they cannot drift.
Logic lives in tools/grader_tools/live_evidence.py.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The command writes labels, issues, pull requests, runs, and commits dumps into tmp/<A>/<team_dir>/ and prints a compact summary
- [ ] #2 --issues fetches comments, timelines, and edit history and --paths fetches per-path commit history
- [ ] #3 Pagination is handled for commits, comments, and timelines and raw JSON dumps never go to stdout
- [ ] #4 Tests cover dump shaping with fixtures and uv run pytest passes
<!-- AC:END -->





## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
