---
id: TASK-031
title: Resolve a bare-SHA submission PDF through the fetcher
status: Done
assignee: []
created_date: '2026-10-19 11:15'
updated_date: '2026-10-19 11:20'
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
- [x] #1 find_permalink records an unresolved bare-SHA candidate when exactly one 40-character SHA appears and no GitHub URL does, and returns None on zero or several SHAs
- [x] #2 PdfPermalink models a missing repository as None and repo_full returns None instead of an empty string
- [x] #3 fetch_team_snapshot resolves the repository with gh search commits, adopts exactly one result, and records permalink_source gh-search-commits
- [x] #4 An ambiguous or failed gh search keeps the stop path, and the summary names the candidates and the command tried
- [x] #5 fetch_team_snapshot.py --repo org/repo pairs an explicit repository with the PDF's bare SHA and records permalink_source operator
- [x] #6 collect_github_evidence.py prints result: skipped (no snapshot) and exits 0 when repo and sha are null
- [x] #7 Tests cover resolution, ambiguity, the override, and the skip path, and the suite passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
PdfPermalink.org/repo are optional; repo_full returns None for an unresolved candidate. find_permalink ranks blob URLs first, then a repo URL with one bare SHA, then '<org>/<repo> at <sha>', then a lone SHA (source=bare-sha). fetch_team_snapshot resolves an unresolved repo with gh search commits via the injectable resolve_repo_fn, records permalink_source gh-search-commits or operator, and keeps the stop path with the candidates and command named. --repo only fills a missing repository and notes an ignored override. pdf-info gains permalink_source. collect_github_evidence returns skipped=True with 'result: skipped (no snapshot)' and the CLI exits 0. Validated: .venv/bin/python -m pytest -> 200 passed; end-to-end Team 1 A3 PDF resolved to itpd-absolute-cinema/llm-module-gateway via gh search commits and the snapshot fetched.
<!-- SECTION:NOTES:END -->
