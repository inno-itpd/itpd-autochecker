---
id: TASK-032
title: Add a bounded evidence digest for the grader's live checks
status: Done
assignee: []
created_date: '2026-10-19 11:15'
updated_date: '2026-10-19 11:30'
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
- [x] #1 The collector writes summary.md into the team work directory with the issue count, PR ranges, failing runs, tags, and per-milestone due dates with open and closed counts, capped at about 60 lines
- [x] #2 collect_github_evidence.py --summary regenerates and prints the digest from existing dumps without calling gh
- [x] #3 The collector records milestones.json, releases.json, and tags.json, so the digest needs no raw gh call
- [x] #4 agents/grader.md step 11 and the Paths section say to read summary.md first and to open a dump only through a bounded projection of about 40 lines
- [x] #5 A3 grading prompt procedure step 5 carries the same rule
- [x] #6 Tests cover the digest content, the line cap, and the no-gh rerun
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
Implemented the bounded digest in tools/grader_tools/live_evidence.py. Layout: issues total/open/closed; PR count and number range; failing runs per source (conclusion in failure/cancelled/timed_out, up to 3 shown with URL then a visible +N line); tags (up to 12 sorted, +N more); releases (count and latest published); milestones (up to 40 sorted by due date, each with due date and open/closed counts, +N more). Hard cap SUMMARY_LINE_CAP=60 enforced with a visible truncation line, and the file states the cap. The collector now records paginated milestones.json (title, due_on, open_issues, closed_issues), releases.json (tag_name, draft, prerelease, published_at), and tags.json (name), writes summary.md atomically with mode 0600, and prints its path. --summary rebuilds and prints the digest from the saved dumps, exits 2 with an ERROR line when dumps are missing, and never calls gh; the no-snapshot skip path is unchanged. agents/grader.md Paths and step 11 and A3/grading_prompt.md step 5 now say to read summary.md first, open a dump only through a projection capped at about 40 lines, never cat a full dump, and cite the observed 1.35 MB commits.json and 284 KB prs.json. Tests extend tests/test_live_evidence.py with digest content, the 60-line cap with visible truncation, and the no-gh --summary rerun plus its missing-dumps error. Validation: .venv/bin/python -m pytest -q -> 204 passed; markdownlint-cli2 agents/grader.md A3/grading_prompt.md -> 0 issues.
<!-- SECTION:NOTES:END -->
