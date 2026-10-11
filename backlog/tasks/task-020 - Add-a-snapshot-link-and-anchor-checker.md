---
id: TASK-020
title: Add a snapshot link and anchor checker
status: To Do
assignee: []
created_date: '2026-10-11 14:23'
labels: []
dependencies: []
ordinal: 20000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Sessions grepped for pre-cut anchors and one grader hand-wrote a relative-link checker for the snapshot.
Add scripts/check_snapshot_links.py with signature check_snapshot_links.py <work_dir> that walks Markdown in the snapshot and verifies relative links and heading anchors using GitHub slug rules.
Support --issue-bodies <issues.json> to check anchors referenced from dumped issue bodies and report pre-cut anchors such as #gap-01-<title> separately.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Broken relative links and missing anchors are reported with the file, the line, and the target
- [ ] #2 Pre-cut anchor occurrences matching #(alt|gap|vp)-NN- are listed separately
- [ ] #3 --issue-bodies checks anchors from dumped issue bodies against snapshot headings
- [ ] #4 Unit tests cover slug rules, relative paths, and the old-anchor pattern and uv run pytest passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
