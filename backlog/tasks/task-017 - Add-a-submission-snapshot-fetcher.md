---
id: TASK-017
title: Add a submission snapshot fetcher
status: Done
assignee: []
created_date: '2026-10-11 14:23'
updated_date: '2026-10-11 14:37'
labels: []
dependencies: []
ordinal: 17000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Grader sessions parse the Moodle PDF for the permalink with ad-hoc pdftotext, pdftohtml, and strings pipelines, then validate and fetch the snapshot by hand.
Add scripts/fetch_team_snapshot.py with signature fetch_team_snapshot.py <assignment> <team_dir>.
It extracts the permalink (org, repo, full 40-character SHA), the recording link, and the page count from the PDF; checks that the commit exists and is on main; fetches the tarball into a freshly emptied itpd-assignments-feedback/<A>/work/<team_dir>/; and writes tmp/<A>/<team_dir>/pdf-info.json with repo, sha, snapshot_time, page_count, recording_link, and member name/email tokens for the privacy scanner without echoing them.
When no full SHA exists it stops repository-dependent checks cleanly per docs/grader-policy.md.
Logic lives in tools/grader_tools/submission_pdf.py.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Extracts the permalink and metadata from PDFs where pdftotext alone fails, including link annotations, and picks the PDF that carries a full SHA
- [x] #2 The fetch empties and repopulates work/<team_dir>/ and the summary reports the commit-exists and on-main results
- [x] #3 Writes pdf-info.json to the gitignored scratch dir without printing real names or emails
- [x] #4 Unit tests cover link extraction and metadata parsing with a fixture PDF and uv run pytest passes
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-11: added tools/grader_tools/submission_pdf.py and scripts/fetch_team_snapshot.py.

Extraction: text comes from `pdftotext -raw` (fallback `-layout`); URLs wrapped across lines are rejoined without dropping characters, so a hyphen the renderer kept stays in the URL (A1 T5, A2 T5/T6). Link annotations come from `pdftohtml -q -xml -stdout -i`; because pdftohtml only emits `<a href>` around text covered by an annotation rect, the raw PDF is also scanned for `/URI (...)` and `/URI <hex>` when it finds none. Permalink candidates are scored by path against the assignment primary index (exact path, then its directory, then other paths, then repo root), which picks `reports/week-NN/README.md` over a meeting-notes or folder link at the same SHA. If no URL carries a full SHA, a repo URL plus exactly one bare 40-hex SHA (or `<org>/<repo> at <sha>`) is combined. Page count comes from pdfinfo with a pdftohtml page-number fallback.

Fetch: `gh api repos/<org>/<repo>/commits/<sha> --jq .commit.committer.date` then `compare/<sha>...main --jq .status`; `identical`/`ahead` is on main, a 404 on compare records `not-found` as not on main, other gh failures raise. The tool always empties `itpd-assignments-feedback/<A>/work/<team_dir>/` first, then fetches `gh api tarball/<sha>` and untars with `--strip-components=1`. No full SHA or a missing commit stops repository-dependent checks cleanly per docs/grader-policy.md#submission-and-snapshot-rules: the work dir stays empty and pdf-info.json is still written with nulls; the script exits 0 then and 1 on PDF/transport errors.

pdf-info.json contract (tmp/<A>/<team_dir>/, mode 0600): assignment, team_dir, pdf, pdf_path, page_count, recording_link, org, repo (org/repo), sha, permalink, permalink_path, snapshot_time, commit_exists, on_main, on_main_status, snapshot_fetched, work_dir, github_usernames, privacy_tokens{name_tokens,email_tokens}. Member rows are parsed by header column order (GitHub-first and Name-first both seen), stop at the first non-row, and yield casefolded name words (>=3 chars) and lowercased emails; GitHub usernames stay out of the tokens. stdout prints counts and paths only, never names or emails. TASK-013 and TASK-019 consume this file.

Validation: `uv run pytest` -> 57 passed, with fixture PDFs covering annotation links, wrapped text-only URLs, and a short-SHA PDF, plus selection of the PDF that carries a full SHA. Dry-run extraction over all 16 A1/A2 submissions matched every reviewed permalink/SHA/recording/page count (spot checks: A1 T2 a38cb12, A1 T5 84f011b, A2 T5 ec5016f, A2 T9 b8decdc). End-to-end runs for A1 T2 and A2 T5 fetched snapshots; A2 T5 snapshot_time 2026-10-10T20:39:35Z matches the saved feedback. Markdownlint is unaffected: backlog/** is ignored by .markdownlint-cli2.jsonc and no other Markdown changed.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
