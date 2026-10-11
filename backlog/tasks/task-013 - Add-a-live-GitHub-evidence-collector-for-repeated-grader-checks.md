---
id: TASK-013
title: Add a live GitHub evidence collector for repeated grader checks
status: Done
assignee: []
created_date: '2026-10-07 10:16'
updated_date: '2026-10-11 15:04'
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
- [x] #1 The command writes labels, issues, pull requests, runs, and commits dumps into tmp/<A>/<team_dir>/ and prints a compact summary
- [x] #2 --issues fetches comments, timelines, and edit history and --paths fetches per-path commit history
- [x] #3 Pagination is handled for commits, comments, and timelines and raw JSON dumps never go to stdout
- [x] #4 Tests cover dump shaping with fixtures and uv run pytest passes
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-11: added tools/grader_tools/live_evidence.py, scripts/collect_github_evidence.py, and tests/test_live_evidence.py.

Entry point: collect_github_evidence.py <assignment> <team_dir> [--issues N ...] [--paths PATH ...]. It reads tmp/<A>/<team_dir>/pdf-info.json and stops with an ERROR when the file is missing or repo/sha are null, pointing at scripts/fetch_team_snapshot.py and the policy stop rule.

Base dumps, written 0600 and pretty-printed: labels.json, issues.json, prs.json, runs_main.json (gh --json field lists and limits are constants copied from A2 procedure step 5), runs_sha.json (actions/runs?head_sha=<sha>, pages merged, projected to name/event/conclusion/html_url), commits.json (repos/<repo>/commits?sha=<sha>&per_page=100 raw commit objects, so Co-Authored-By trailers stay readable for S10). --issues <n> writes issues/<n>.comments.json and <n>.timeline.json plus <n>.edits.json from the userContentEdits GraphQL query; --paths <path> writes paths/<path>.json projected to sha/date/first message line. Repo-relative paths are validated (no absolute paths, no ..) and quoted in the API URL.

Pagination: gh --paginate prints one JSON value per page; parse_json_stream decodes them all, merge_list_pages flattens arrays, merge_run_pages concatenates workflow_runs. stdout prints only counts and file paths, never raw JSON. gh failures raise LiveEvidenceError with the command label (gh label list / gh api <endpoint>) and stderr, never stdout.

Anti-drift: test_a2_step5_field_lists_match_the_collector parses A2/grading_prompt.md's procedure step 5 and asserts the label/issue/pr/run --json lists, the --limit values, the runs-sha jq fields, the path-history jq fields, and the userContentEdits node fields match the collector constants.

Validation: uv run pytest -> 72 passed (14 new). Live smoke test against itpd-2026-team-5/team-5-sentence-card-generator @ ec5016f with --issues 11 50 --paths reports/week-02/README.md: 26 issues, 27 PRs, 16 labels, 37 main runs, 2 runs at the SHA, 89 commits, 4 commits on the report path, matching the saved grader scratch counts. markdownlint reports 0 errors on the changed Markdown (backlog/** is ignored). Note: the pre-existing untracked TODO.md in the repo root fails markdownlint (hard tabs) and was left untouched.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
