---
id: TASK-040
title: Make per-issue issue fields the S6 evidence route
status: Done
assignee: []
created_date: '2026-10-19 14:57'
updated_date: '2026-10-19 15:24'
labels: []
dependencies: []
ordinal: 40000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
F2 from plan-1.md. The documented `organization(login:) { issueFields { nodes { name, dataType, options } } }` query is invalid because `IssueFields` is a union, and even the valid `totalCount` form is not evidence of absence: it returned 0 for repositories whose issues demonstrably carry `Responsible` and `Accountable` values. The route that works is per issue: GraphQL `Issue.issueFieldValues`, or REST `repos/<repo>/issues/<n>` and the `issue_field_values` array. Teams 3 and 9 used it and documented it; Teams 1 and 4 read the empty organization list as "no fields". Their `missing` S6 statuses stand because no project held the repository's issues at the cutoff, but the trap must be removed before the next batch.

Decision: public issues are visible to everyone, not only to organization members. S6 reads per-issue values and corroborates with the project; an empty organization list never decides the segment.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The S6 check and procedure step 12 make per-issue `issueFieldValues` or REST `issue_field_values` the primary route, and remove or demote the `organization { issueFields }` example.
- [x] #2 The rubric states that an empty organization field list or `totalCount: 0` is not evidence that a field is absent, and that S6 is never `missing` on that list alone; public issues are readable without organization membership, so per-issue values and the project settle the segment.
- [x] #3 The `unverified` definition for S6 names the per-issue route instead of the organization field list.
- [x] #4 The fallback `gh api repos/<repo>/issues/<n>` projection includes `issue_field_values` beside `type` and `milestone`.
- [x] #5 `scripts/collect_github_evidence.py` implements and documents an issue-fields mode that dumps the field values for each issue into the team work directory, so graders do not hand-write the query.
- [x] #6 Verification: the documented recipe returns `Responsible` and `Accountable` for `WellMadeTeam`; a team whose issues carry no values is judged from the project criterion; the documented query parses against the live schema without `selectionMismatch`.
- [x] #7 `uv run pytest` and `markdownlint-cli2` pass.
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
Made the per-issue route primary: S6 reads Responsible/Accountable from the new issue-fields.json dump, the REST issue_field_values projection, or GraphQL issueFieldValues, with field names/options/pinning/visibility from the issue sidebar and project fields. Removed the organization issueFields query from the prompt, demoted the org list to non-evidence, stated that an empty list or totalCount 0 is not evidence of absence and that S6 is never missing on it alone, and named the per-issue route in the unverified definition. Added the collector --issue-fields mode (one paginated REST issue-list call, pull requests skipped, null-safe rows with type, milestone, assignees, field_values, written 0600) and documented it in the prompt, agents/grader.md, and AGENTS.md; --issue-fields is its own mode and is rejected with --summary, --issues, and --paths. Validation: uv run pytest -q -> 252 passed; markdownlint-cli2 on the three changed Markdown files -> 0 issues. Live checks: the documented REST projection and the GraphQL query both return Responsible=danmaninc and Accountable=Kamil116 for WellMadeTeam/workspace-ai-03 issue 126 with no selectionMismatch; a scratch-root collector run wrote 62 non-PR issues without touching the real A3 work directories. Deviation: repo-wide markdownlint-cli2 still reports the pre-existing A1/A2 denis-feedback.md issues and untracked TODO.md; those were left untouched.
<!-- SECTION:NOTES:END -->
