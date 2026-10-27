# Grader Policy

This document is the authoritative source for general grading policy in this repository.
It applies to every assignment unless the assignment's `A<N>/grading_prompt.md` explicitly overrides it.

## Purpose and scope

- The primary goal is student-facing feedback that is accurate, specific, and actionable.
- The autochecker does not assign grades.
  It assigns a status to each segment, and the instructor decides the grade.
- Review only the current assignment.
  Apply a course rule only when its `**Since: WN**` marker is at or before the assignment's week.
- Do not mark a segment down for a later-week requirement.

## Authority and document boundaries

- `docs/grader-policy.md` (this file) is the authority for general policy.
- `docs/grading-feedback-format.md` is the authority for the exact report format.
- `A<N>/grading_prompt.md` is the authority for the segments, their status criteria, and the assignment-specific procedure.
- `A<N>/itpd/` is the course repository pinned at the commit the assignment is reviewed against.
  It overrides the current course repository.

## Status policy

- Use the status vocabulary from `docs/grading-feedback-format.md`: `met`, `partial`, `missing`, `unverified`.
- Be conservative.
  `met` requires verified evidence for every requirement of the segment.
- Use `unverified` only when the segment could not be judged at all.
  When some requirements were verified, pick `partial` or `missing` from the verified evidence and set `Evidence gaps: yes`.
- `Manual review required` is `yes` exactly when any segment has `Evidence gaps: yes`.

## Evidence gaps policy

- `Evidence gaps: yes` is reserved for a blocked, conflicting, or otherwise unresolved check that could still change the segment's status.
  The test is the status-changing one: if a later review of the blocked artifact could not change the status, there is no evidence gap.
- A criterion the grader could not check that cannot change the status is an `**Evidence:**` caveat, never an evidence gap and never a `**Why not met (unverified):**` bullet.
  State what was checked, what could not be read, and why the verified evidence already settles the status.
- This policy takes precedence over an assignment prompt that says "an evidence gap for that criterion".
  Apply the status-changing test there too, and record the blocker as a caveat when the verified evidence is enough for the status.
- A blocked artifact URL does not count as positive evidence by itself.
  Only independently verified surrounding evidence counts.
- Verified absence may still come with `Evidence gaps: yes` when an inaccessible location could change the result.
- When a gap clears because new evidence confirms the earlier shortfall, the status may stay the same; clear the gap rather than silently upgrading the status.

## Evidence-state definitions

- `missing`: the required artifact or information is absent.
- `inaccessible`: the artifact may exist, but the grader cannot verify it through the snapshot, the public GitHub repository, the GitHub API with `GITHUB_TOKEN`, or the Moodle PDF where the assignment allows PDF evidence.
- `conflicting`: the PDF, the repository, GitHub metadata, or the linked artifacts disagree materially.

## Submission and snapshot rules

ITPD submissions are uploaded to Moodle as a PDF report that carries a permalink to the week report.
There is no ZIP.

- The PDF must carry a permalink to `reports/week-NN/README.md` at a full 40-character commit SHA.
  A 7-character abbreviation is not a permalink.
- The permalink must name the assignment's week.
  A wrong-week permalink stops the fetch instead of grading a wrong-week target: `scripts/fetch_team_snapshot.py` prints a `warn:` line, repeats it in `work/<team_dir>/summary.md`, records `permalink_week_mismatch`, skips the commit check and the snapshot fetch, and exits 1.
  Judge the mismatch as a submission shortfall in the week-report-and-submission segment (S15 in A4, S12 in A3, S9 in A2, S8 in A1), and request the right permalink with `scripts/fetch_team_snapshot.py A<N> "<team_dir>" --permalink <url>`; the snapshot fetched from that permalink still governs every file check.
- The authoritative snapshot is that full SHA.
- Fetch the snapshot from GitHub at that SHA (`gh api repos/<org>/<repo>/tarball/<sha>`) and use it as the offline evidence.
- Do not require or report on a ZIP.
- If no full SHA can be found, or the commit does not exist in the repository, stop repository-dependent checks.
  Write `Snapshot reviewed: none` and `Primary index reviewed: none` with a `Notes about the snapshot` bullet, and mark the repository-dependent segments `unverified` with `Evidence gaps: yes`.
- Use only the snapshot for file evidence.
  Do not review files from the moving default branch.

## Live GitHub evidence

Process evidence lives on GitHub, not in the snapshot files: branch protection, pull requests, reviews, issues, labels, and Actions runs.

- Use the `gh` CLI (`gh api`, `gh pr list`, `gh issue list`, `gh run list`) with `--repo <org>/<repo>`.
- Judge live state as of the snapshot where possible.
  Compare `createdAt`, `mergedAt`, `closedAt`, and run timestamps with the snapshot commit date.
  An assignment prompt may set a later cut-off for an artifact family, such as issues judged as of the hard deadline.
- Changes made after the hard deadline do not repair the submission.
  Note them in the evidence, but do not credit them.
- The grader usually lacks admin rights, so admin-only endpoints such as `repos/<org>/<repo>/branches/main/protection` are expected to return 403 or 404.
  That alone is not an evidence gap.
  Use the readable routes instead: `repos/<org>/<repo>/branches/main` (`.protected`), `repos/<org>/<repo>/rules/branches/main` (rulesets), and the evidence the assignment asks for, such as the branch-protection screenshot.
  Set `Evidence gaps: yes` only when those readable routes disagree or cannot settle the requirement.

## Consumer-hosted media

- Recordings, videos, and shared drives (YouTube, Google Drive, Yandex Disk, and similar) get one access check.
- If the artifact is sign-in gated, permission gated, or otherwise not directly inspectable, stop there.
  Record it as an evidence gap for instructor review.
- Never try to watch or transcribe recordings.

## Visibility and privacy

- The course requires that real names, university emails, and recordings stay out of the public repository and appear only in the Moodle PDF.
- Never copy real names or emails from the PDF into feedback.
  Refer to people by GitHub username, and to the customer as `Customer`.
- Before quoting a branch name, tag name, URL, or path in a report, check it against the member name and email tokens in `work/<team_dir>/pdf-info.json`.
  A branch or URL that embeds a member's name is a privacy leak even when it looks like a harmless identifier: rewrite the reference, do not only add a note.
  For example, describe the branch by its number and purpose rather than repeating `week4-<name>-...`.
- Re-run the report privacy scan after the rewrite; the scan is what catches a name token the prose reviewer missed.
- There are two scans, and a batch needs both:
  - `scripts/scan_privacy.py A<N> "<team_dir>" --feedback <agent-feedback.md>` scans the finished report against the PDF tokens.
  - `scripts/scan_privacy.py A<N> "<team_dir>"` scans the fetched snapshot before extraction.
  After `work/<team_dir>/` is cleaned, the first scan still works with `--no-snapshot`, because it derives the tokens from the submission PDF.
- Do not mark down a team for keeping private material out of the repository when the course requires or allows that.
- Do mark down a team for committing private material that the course forbids in the repository.
  Describe the problem without repeating the private data.
- A feedback report never presents advice as a third party's note.
  The checker writes the optional `## Suggested next steps` section itself, so the section is the checker's own suggestion rather than someone else's note.

## Deviations

- The week report may declare deviations from the assignment with a justification.
- A declared deviation is judged on whether what the team did instead satisfies the intent of the rule, and on whether the justification is reasonable.
  When it does, it is not a shortfall.
- Declaring a deviation does not excuse a broken Required rule whose intent the alternative cannot satisfy, such as a meeting that changed nothing when a change is required.
  That stays a shortfall, and the honest declaration is recorded as a strength.
- An undeclared deviation is treated as a missing requirement.

## Quality and honesty

- Disclosed AI use is never penalised by itself.
- Filler counts as a verified shortfall: template sentences with no product name, no ID, and no date, generic claims, or analysis that does not refer to the evidence.
  Quote a short fragment as evidence.
- Do not penalise style or wording when the content is specific and checkable.

## Evidence citation policy

- Cite concrete evidence for every status: snapshot permalinks, file headings, stable IDs (`ALT-01`, `DEC-003`, `US-04`), issue and PR numbers, run URLs, or PDF statements.
- Repository file evidence links to the snapshot: `https://github.com/<org>/<repo>/blob/<sha>/<path>`.
- Live GitHub evidence cites the exact URL or `gh api` endpoint checked.

## General grading procedure

1. Read the PDF first.
   Extract the team number, the repository URL, the permalink and its SHA, and the declared links.
2. Resolve the authoritative snapshot under the rules above.
3. Fetch the snapshot from GitHub at the permalink SHA.
4. Review the files offline from the fetched snapshot.
5. Collect the live GitHub evidence the assignment requires.
6. Judge each segment independently with the assignment's status guide.
7. Write the report in the canonical format and validate it with `scripts/validate_feedback_report.py`.

## Report content policy

- `## Unresolved evidence gaps` is the only place for blocked-access and conflict diagnostics.
- `## Summary` holds only verified shortfalls and the most important student-actionable issues.
- `## Strengths` holds only verified positives.
- `## Main issues to fix` holds only issues that students can confidently fix from verified evidence.

## Regrading policy

- A `full regrade` re-audits every segment of an existing report against freshly checked evidence.
  It preserves the team work directory, rebuilds the payload, and re-renders the report; it does not re-fetch or re-review from zero.
- Treat the existing report as an unverified draft, not as evidence.
  A claim survives only when the saved dumps or a fresh lookup still support it.
- Regrades do not depend on when a grader reruns them.
  Re-read the artifact instead of trusting the previous wording, and give every changed claim a new `**Evidence:**` bullet.
- Regrades re-check previously blocked artifacts instead of reusing old observations.
- Segment-targeted regrades refresh the requested segments plus any segment whose status depends on the same newly checked artifact.
  Choose related segments by shared artifact, not by adjacent segment numbers.
- Untouched segment blocks stay verbatim.
- Instructor-provided evidence may be used directly, and is cited in `**Evidence:**` as instructor-reviewed.
- A regrade may clear `Evidence gaps` without changing the status, when newly visible evidence confirms the earlier shortfall.
- A regrade never changes a status on prose alone; the change needs verified evidence.

## Segment inspection policy

- Segment inspection is read-only.
- Separate the saved report state from fresh current-run checks.
- Say whether the fresh observations would justify a regrade.

## Authenticated access and token handling

<!-- TODO can we get it from gh? -->
<!-- TODO which scopes should it have? -->
- `GITHUB_TOKEN` is loaded into the shell environment by direnv; `gh` picks it up automatically.
- Do not read `.env`, echo token values, or include them in reports.
  Reference tokens only by variable name.
- Retry with the token before marking a GitHub artifact as inaccessible.

## Implementation consistency

- If the validator or extractor disagrees with this policy or the format document, fix the implementation to match the documents.
