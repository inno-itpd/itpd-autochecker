---
id: TASK-032
title: Add a bounded evidence digest for the grader's live checks
status: To Do
assignee: []
created_date: '2026-10-19 11:15'
labels: []
dependencies: []
ordinal: 32000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Graders died after reading multi-megabyte dumps whole: commits.json reached 1.35 MB and prs.json 284 KB. Step 11 needs a compact digest to read first, dumps bounded to projections, and an explicit rule never to cat a full dump.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The collector writes summary.md into the team work directory with the issue count, PR ranges, failing runs, tags, and per-milestone due dates with open and closed counts, capped at about 60 lines
- [ ] #2 collect_github_evidence.py --summary regenerates and prints the digest from existing dumps without calling gh
- [ ] #3 The collector records milestones.json, releases.json, and tags.json, so the digest needs no raw gh call
- [ ] #4 agents/grader.md step 11 and the Paths section say to read summary.md first and to open a dump only through a bounded projection of about 40 lines
- [ ] #5 A3 grading prompt procedure step 5 carries the same rule
- [ ] #6 Tests cover the digest content, the line cap, and the no-gh rerun
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
