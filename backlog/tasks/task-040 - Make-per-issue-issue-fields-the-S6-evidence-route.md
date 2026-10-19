---
id: TASK-040
title: Make per-issue issue fields the S6 evidence route
status: To Do
assignee: []
created_date: '2026-10-19 14:57'
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
- [ ] #1 The S6 check and procedure step 12 make per-issue `issueFieldValues` or REST `issue_field_values` the primary route, and remove or demote the `organization { issueFields }` example.
- [ ] #2 The rubric states that an empty organization field list or `totalCount: 0` is not evidence that a field is absent, and that S6 is never `missing` on that list alone; public issues are readable without organization membership, so per-issue values and the project settle the segment.
- [ ] #3 The `unverified` definition for S6 names the per-issue route instead of the organization field list.
- [ ] #4 The fallback `gh api repos/<repo>/issues/<n>` projection includes `issue_field_values` beside `type` and `milestone`.
- [ ] #5 `scripts/collect_github_evidence.py` implements and documents an issue-fields mode that dumps the field values for each issue into the team work directory, so graders do not hand-write the query.
- [ ] #6 Verification: the documented recipe returns `Responsible` and `Accountable` for `WellMadeTeam`; a team whose issues carry no values is judged from the project criterion; the documented query parses against the live schema without `selectionMismatch`.
- [ ] #7 `uv run pytest` and `markdownlint-cli2` pass.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->
