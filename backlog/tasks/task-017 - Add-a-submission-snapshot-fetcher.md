---
id: TASK-017
title: Add a submission snapshot fetcher
status: To Do
assignee: []
created_date: '2026-10-11 14:23'
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
- [ ] #1 Extracts the permalink and metadata from PDFs where pdftotext alone fails, including link annotations, and picks the PDF that carries a full SHA
- [ ] #2 The fetch empties and repopulates work/<team_dir>/ and the summary reports the commit-exists and on-main results
- [ ] #3 Writes pdf-info.json to the gitignored scratch dir without printing real names or emails
- [ ] #4 Unit tests cover link extraction and metadata parsing with a fixture PDF and uv run pytest passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
