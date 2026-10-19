---
id: TASK-031
title: Resolve a bare-SHA submission PDF through the fetcher
status: To Do
assignee: []
created_date: '2026-10-19 11:15'
updated_date: '2026-10-19 11:16'
labels: []
dependencies: []
ordinal: 31000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A submission PDF may carry only `Submission commit: <sha40>` and no GitHub URL, as Team 1's A3 PDF did. `_permalink_from_bare_sha` returns None without a URL, and `collect_github_evidence.py` then hard-fails, so the grader must run `gh search commits` by hand.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 find_permalink records an unresolved bare-SHA candidate when exactly one 40-character SHA appears and no GitHub URL does, and returns None on zero or several SHAs
- [ ] #2 PdfPermalink models a missing repository as None and repo_full returns None instead of an empty string
- [ ] #3 fetch_team_snapshot resolves the repository with gh search commits, adopts exactly one result, and records permalink_source gh-search-commits
- [ ] #4 An ambiguous or failed gh search keeps the stop path, and the summary names the candidates and the command tried
- [ ] #5 fetch_team_snapshot.py --repo org/repo pairs an explicit repository with the PDF's bare SHA and records permalink_source operator
- [ ] #6 collect_github_evidence.py prints result: skipped (no snapshot) and exits 0 when repo and sha are null
- [ ] #7 Tests cover resolution, ambiguity, the override, and the skip path, and the suite passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
