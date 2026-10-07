# Grading Feedback Format

This document defines the canonical feedback report structure for this repository.

General grading policy lives in `docs/grader-policy.md`.

ITPD assignments are not scored with points.
Each segment gets a status, and the instructor decides the grade.

Assignment-specific prompts remain responsible for:

- segment names
- segment count
- the primary index path
- the status criteria for each segment

## Status vocabulary

| Status | Meaning |
|--------|---------|
| `met` | Every requirement of the segment is satisfied by verified evidence. |
| `partial` | Some requirements are satisfied, and at least one verified shortfall remains. |
| `missing` | The segment's required artifacts are absent, or none of its requirements are satisfied. |
| `unverified` | The grader could not check the segment because its evidence was inaccessible or conflicting. |

Rules:

- `unverified` always comes with `Evidence gaps: yes`.
- Any other status may come with `Evidence gaps: yes` when a blocked or conflicting check could still change it.
- Choose the status from the currently verified evidence.
  Do not upgrade a status on the strength of an artifact that could not be checked.

## Required report sections

Every feedback report must contain these sections in this order:

1. `# Assignment <N> Feedback Report`
2. repository metadata bullets
3. `## Overall assessment`
4. `## Segments`
5. `## Unresolved evidence gaps`
6. `## Summary`
7. `## Strengths`
8. `## Main issues to fix`
9. `## Segment details`

Do not add extra top-level sections.

## Repository metadata

Immediately below the title, include these bullets in this order:

- `- Team: <number>`
- ``- Repository reviewed: `https://github.com/<org>/<repo>` ``
- ``- Snapshot reviewed: `<full 40-character SHA>` `` or `- Snapshot reviewed: none`
- `` - Primary index reviewed: [`reports/week-NN/README.md`](<permalink at the snapshot>) `` or `- Primary index reviewed: none`

If the primary index is `none`, add one more bullet immediately below:

- `- Notes about the snapshot: <prose explanation>`

The `Notes about the snapshot` bullet is not allowed when a primary index was reviewed.
Problems resolving the PDF permalink belong in `## Unresolved evidence gaps`, not in the metadata.

## Overall assessment

The section body must be exactly:

```markdown
- Met: `<count>/<total>`
- Partial: `<count>/<total>`
- Missing: `<count>/<total>`
- Unverified: `<count>/<total>`
- Automatic review status: `complete` or `pending review`

This assessment reflects currently checked evidence and may change after instructor review of unresolved evidence gaps.
```

Rules:

- `<total>` is the number of assignment-defined segments.
- The four counts must add up to `<total>`.
- The status is `pending review` when any segment has `Evidence gaps: yes`, and `complete` otherwise.

## Segments table

The `## Segments` section must contain a three-column Markdown table:

```markdown
| Segment | Status | Evidence gaps |
|---------|--------|---------------|
| [S1: <segment name>](#s1-segment-name) | met | no |
| [S2: <segment name>](#s2-segment-name) | partial | yes |
| Manual review required | yes | |
```

Rules:

- One row per assignment-defined segment, in assignment-defined order.
- Each label must use the exact `S<N>: <segment name>` text from the assignment prompt, linked to the matching `### S<N>: ...` heading.
- `Manual review required` is `yes` if any segment has `Evidence gaps: yes`, and `no` otherwise.

## Unresolved evidence gaps

When `Manual review required` is `no`, the section body must be exactly:

`No manual review required. All evidence was accessible`

When `Manual review required` is `yes`:

- use one top-level bullet per affected segment, linking to its `### S<N>: ...` heading
- use nested bullets, indented by two spaces, for each blocked, conflicting, or otherwise unresolved check from the current run
- each nested bullet should name the artifact, the exact URL or path, the observed result, what could not be verified, and the surrounding evidence that was still verified
- do not include stale observations from earlier runs

```markdown
- [S2](#s2-ci-checks-and-supply-chain-hygiene)
  - `gh api repos/<org>/<repo>/actions/runs` returned 404 on 2026-10-07; the link-check run on `main` could not be verified, while `.github/workflows/links.yml` exists in the snapshot.
```

## Summary

- 3-5 short bullets.
- Only verified shortfalls and the most important student-actionable issues.
- Do not mention blocked or unresolved checks here.
- This is the only section exported into the release CSV.

## Strengths

- One sentence per bullet.
- Verified positives only, linked to artifacts where possible.

## Main issues to fix

- One sentence per bullet.
- Actionable issues that students can confidently fix from verified evidence.

## Segment details

For each assignment-defined segment, in order:

```markdown
### S<N>: <segment name>

Status: met | partial | missing | unverified

Evidence gaps: yes | no

**Evidence:**

- concrete verified evidence, with permalinks to the snapshot

**Why not met (verified):**

- verified shortfalls

**Why not met (unverified):**

- blocked, conflicting, or unresolved checks from the current run
```

Rules:

- Keep the heading, the `Status:` line, and the `Evidence gaps:` line separate.
- `**Evidence:**` is always present and has at least one bullet.
  For a segment with no positive evidence, state what was checked and found absent.
- `**Why not met (verified):**` is present with at least one bullet exactly when the status is `partial` or `missing`.
  It may also be present for `unverified` when some shortfalls were verified.
- `**Why not met (unverified):**` is present with at least one bullet exactly when `Evidence gaps: yes`.
- Instructor-provided evidence used in a regrade goes into `**Evidence:**` and is labelled as instructor-reviewed.

## Evidence and permalink rules

- Every repository file reference must link to the snapshot commit, for example `https://github.com/<org>/<repo>/blob/<sha>/docs/decisions.md`.
- Live GitHub evidence (pull requests, issues, Actions runs, branch protection) cites the exact URL or `gh api` endpoint checked.
- Moodle PDF references use a clear label such as `Moodle PDF, contribution table`.
- Never copy real names or university emails from the PDF into the report.
  Refer to people by GitHub username.

## Formatting rules

- One sentence per line.
- No hard wrapping.
- All fenced code blocks have a language tag.
- Keep headings and table labels exactly as specified, because the extractor depends on them.
