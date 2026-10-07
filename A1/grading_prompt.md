# Assignment 1 Grading Criteria

This rubric is for an LLM grading agent that reviews ITPD Assignment 1 (Initial Project Research) team submissions.
There are no points: the agent assigns each segment a status (`met`, `partial`, `missing`, or `unverified`) and an `Evidence gaps` flag, and the instructor assigns the grade.
General rules live in `docs/grader-policy.md`, and the report contract lives in `docs/grading-feedback-format.md`; this file adds only what is specific to Assignment 1.

## Authoritative sources

All course materials are read from `A1/itpd/`, the course repository pinned at commit `fe58ba70bbd90b92ffd6942d340f1e8b35b4bbb1`.
That is the version of Assignment 1 published at the deadline.
Files under `A1/itpd/` override the current course repository, even where the current version differs.

- `A1/itpd/assignments/assignment-1.md`: the student-facing brief, the Week 1 minima, the week report and Moodle PDF contents, "What Good Looks Like", and the checklist.
- `A1/itpd/requirements/repository-requirements.md`: repository setup, licensing, root README, branch protection and pull requests, link checking, action pinning, permalinks and snapshots, and sensitive information.
- `A1/itpd/requirements/artifact-requirements.md`: the `reports/week-NN/` versus `docs/` split, visibility, the weekly public report, the meeting report, transcript, notes and script structures, screenshot evidence, the AI usage report, the private submission wrapper, and deviations.
- `A1/itpd/requirements/process-requirements.md`: what counts as an alternative, a property, a comparison cell, a gap, a value proposition and an assumption, the identifier rules, the quality rules, and the kickoff meeting rules.
- `A1/itpd/course/rules.md`: public versus private material, AI tools policy, and the soft and hard deadline pair.
- `A1/itpd/course/syllabus.md`: the Week 1 and Week 2 date ranges and the late-submission policy, which the instructor applies, not the agent.
- `A1/itpd/course/teams-and-projects.md`: the team number to project mapping for the autumn 2026 term.
- `A1/itpd/guides/alternatives-research.md`, `A1/itpd/guides/comparison-and-synthesis.md`, `A1/itpd/guides/customer-interview.md`: method only.
  Use them to interpret a requirement, never as an extra requirement.
- `A1/itpd/AGENTS.md`: course terminology, identifier conventions, and the `docs/` destination map.

## Assignment parameters

- Report title: `# Assignment 1 Feedback Report`
- Week: `W1`
- Apply only requirements marked `**Since: W1**` in the requirements files, plus the assignment text.
- Primary index: `reports/week-01/README.md` at the authoritative snapshot.
- Soft deadline: Thursday 1 October 2026, 23:59.
- Hard deadline: Friday 2 October 2026, 23:59.
- Week 1 runs 25 September to 1 October 2026, and Week 2 runs 2 to 8 October 2026 (`A1/itpd/course/syllabus.md`).
- Submissions: `itpd-assignments-feedback/A1/submissions/<team_dir>/` holds the Moodle PDF; there is no ZIP.
- Working copy: fetch the snapshot from GitHub at the permalink SHA into `itpd-assignments-feedback/A1/work/<team_dir>/`.

Segments, in report order:

- S1: Repository setup and branch protection
- S2: CI checks and supply-chain hygiene
- S3: Collaboration through pull requests
- S4: Alternatives research
- S5: Comparison and gap analysis
- S6: Value proposition and assumptions
- S7: Customer kickoff meeting
- S8: Week report and submission
- S9: AI usage and research honesty

### Segment overview

Every item of the Assignment 1 checklist maps to exactly one segment.

| Segment | Covers (assignment parts / checklist items) |
|---------|---------------------------------------------|
| S1 — Repository setup and branch protection | Part 1 items 4–6, Part 2 items 1–4; checklist: public repository in the team's own organization with all members as collaborators and `main` as default; `LICENSE`, `.gitignore`, root `README.md`; `main` protected with the screenshot in `reports/week-01/images/` |
| S2 — CI checks and supply-chain hygiene | Part 2 items 6–7; checklist: Lychee link check on pull requests and `main`, green, with justified exclusions in `.lycheeignore`; actions pinned to commit SHAs with `.github/dependabot.yml` |
| S3 — Collaboration through pull requests | Part 2 items 5 and 8; checklist: pull request template at `.github/pull_request_template.md`; at least one merged pull request approved by another member; every member with at least one commit and at least one review |
| S4 — Alternatives research | Part 3; checklist: `docs/research/alternatives.md` with 3–4 alternatives and `ALT-nn` IDs; `reports/week-01/candidate-list.md` with the full search; board linked, view-only, two screenshots per alternative |
| S5 — Comparison and gap analysis | Parts 4–5; checklist: `docs/research/comparison.md` with at least 6 properties and traceable cells; `docs/research/gap-analysis.md` with `GAP-nn` entries and the rejected list |
| S6 — Value proposition and assumptions | Part 6; checklist: `docs/research/value-proposition.md` with `VP-nn` entries and assumptions |
| S7 — Customer kickoff meeting | Part 7; checklist: meeting script with five areas and tagged questions; `## Key improvements` with two real rewrites; three roles and whole team attending; meeting held with all three permissions asked; meeting report with all six sections and the minima; transcript or notes, sanitized |
| S8 — Week report and submission | Part 1 items 1–3, "Assignment Report In The Repository", "Assignment Report On Moodle"; checklist: team of 3 or 4 with project and team number; `reports/week-01/README.md` complete; PDF and snapshot ready with the permalink at the full commit hash |
| S9 — AI usage and research honesty | Part 8, "What Good Looks Like", Quality Rules in `process-requirements.md`; checklist: `reports/week-01/ai-usage.md` written |

## Status guide

Use the status vocabulary and evidence-state rules from `docs/grader-policy.md` and `docs/grading-feedback-format.md`.
The headings below use an em dash; in the feedback report, write each segment heading as `### S<n>: <name>`, exactly as the format requires.
Each shortfall belongs to exactly one segment, the one named as its owner below.
Do not record the same shortfall in a second segment.
A declared deviation is judged in the segment that owns the requirement it replaces.

### S1 — Repository setup and branch protection

Check:

- `gh api repos/<org>/<repo>`: `.owner.type`, `.visibility`, `.default_branch`, `.owner.login`, `.name`.
- `gh api repos/<org>/<repo>/collaborators` (needs push access, so 403 is expected) and, as fallback, `author_association` on the pull requests and reviews collected for S3.
- Snapshot files: `LICENSE`, `.gitignore`, `README.md`.
- `gh api repos/<org>/<repo>/branches/main` (`.protected`), `gh api repos/<org>/<repo>/branches/main/protection` (admin only), and `gh api repos/<org>/<repo>/rules/branches/main` (rulesets, readable with read access).
- The branch protection screenshot under `reports/week-01/images/`: open the image and read the settings it shows.
- PDF: the member table, for the list of GitHub usernames.

`met`:

- The repository is owned by an organization account, is public, and has `main` as its default branch.
- The organization name and the repository name both carry the team number (`repository-requirements.md`, Repository Setup item 1).
- Every GitHub username in the PDF member table is a collaborator with write access.
  When the collaborators endpoint returns 403, accept an `author_association` of `OWNER`, `MEMBER`, or `COLLABORATOR` on that member's pull request or review as evidence.
- `LICENSE` contains the MIT License text with a copyright line naming the team and the year.
- `.gitignore` covers all four categories: editor state, OS files, `.env` and other secret files, and build output.
- Root `README.md` contains all five Week 1 items: project name from the catalog and team number; a one-line description; a link to `reports/week-01/README.md`; a link to the maintained documentation in `docs/`; a note that the project is a work in progress for the ITPD course.
- `main` requires a pull request before merging and at least one approval, shown by the API (classic protection or a ruleset `pull_request` rule with `required_approving_review_count` of 1 or more) or by a legible screenshot.
- A screenshot of the `main` protection settings is committed under `reports/week-01/images/`, and it shows the pull request requirement and the approval count.

`partial`:

- The repository is public and reachable, but at least one `met` item is a verified shortfall.
  Typical cases: a missing `.gitignore` category, a `LICENSE` without the team or year, a root README missing one of the five items, a repository under a personal account, names without the team number, or protection that is verified but has no screenshot in `reports/week-01/images/`.

`missing`:

- `LICENSE`, `.gitignore`, and root `README.md` are all absent from the snapshot, and `main` is verified unprotected (`.protected` is `false` and `rules/branches/main` returns no `pull_request` rule).

Guardrails:

- GitHub never lets a pull request author approve their own pull request, so do not require a separate visible "no self-approval" setting when a pull request and an approval are required.
- Rulesets and classic branch protection are equivalent.
- Do not require the file name `branch-protection.png`; any clearly named image in `reports/week-01/images/` counts.
- When the admin-only protection endpoint returns 403 or 404, follow `docs/grader-policy.md`; the screenshot together with `.protected: true` is the evidence for the settings.
- `.protected: false` with no applicable ruleset is verified absence, whatever the screenshot shows.
- Do not mark down for extra collaborators, for example instructors.
- Do not require setup or run instructions in the root README; they are `Since: W2`.
- Direct pushes and unapproved merges belong to S3, not here.
- Do not mark down a team-size problem here; S8 owns it.

### S2 — CI checks and supply-chain hygiene

Check:

- Snapshot files: every file in `.github/workflows/`, any composite action under `.github/actions/`, `.lycheeignore`, any `lychee.toml`, and `.github/dependabot.yml`.
- `gh api "repos/<org>/<repo>/actions/runs?branch=main&event=push&per_page=30"`, filtered to the Lychee workflow, and in particular the run whose `head_sha` is the snapshot SHA.
- `gh api "repos/<org>/<repo>/actions/runs?event=pull_request&per_page=30"`, filtered to the Lychee workflow.
- For each pinned action, `gh api repos/<action-owner>/<action-repo>/commits/<version-in-comment> --jq .sha`, to compare with the pinned SHA.
- The link-exclusion justification and the browser-check confirmation in `reports/week-01/README.md`.

`met`:

- A GitHub Actions workflow runs Lychee on `pull_request` and on `push` to `main`.
- It checks every Markdown file in the repository (for example `'./**/*.md'` or `.`), not a subset of directories and not only the changed files.
- It fails on a broken link: no `fail: false`, no `continue-on-error: true`, no `--offline`, no blanket exclusion of external links, and no accepted status codes that hide broken links (for example `404`).
- The latest `main` run of the Lychee workflow at or before the snapshot commit date concluded `success`, preferably the run on the snapshot SHA.
- Every excluded link or pattern (in `.lycheeignore`, `lychee.toml`, or `--exclude` arguments) carries a comment justifying why it cannot be checked mechanically.
- The week report repeats the justification in prose and confirms each excluded link was opened in a browser.
- Every `uses:` reference to a third-party action or reusable workflow is pinned to a full 40-character commit SHA with a trailing version comment on the same line, and spot-checked comments match their SHAs.
- `.github/dependabot.yml` exists with a `package-ecosystem: github-actions` update entry.

`partial`:

- A Lychee workflow exists, but at least one `met` item is a verified shortfall.
  Typical cases: no `pull_request` trigger, a narrowed glob, a red or missing latest `main` run, an unjustified exclusion, one action pinned to a tag or branch, a version comment that names a different version than the SHA, or no `dependabot.yml`.

`missing`:

- No Lychee workflow exists in the snapshot.

Guardrails:

- Do not require the workflow file name `lychee.yml`.
- In `lycheeverse/lychee-action` v2 and later, `fail` defaults to `true`, so an omitted `fail` input is not a shortfall there.
- Accepting `429` is fine, because the course example does it; accepting `403` needs a justification like any exclusion.
- An absent or empty `.lycheeignore` is not a shortfall when nothing is excluded.
- Local actions (`uses: ./...`) need no SHA pin.
- A red `main` run that happened only after the hard deadline does not change the status; judge the run current at the snapshot under `docs/grader-policy.md`.
- If Actions runs are inaccessible, judge configuration from the snapshot, and set `Evidence gaps: yes` for the run status.
- Do not require stack-specific CI (linting, tests, build); it is `Since: W5`.

### S3 — Collaboration through pull requests

Check:

- Snapshot file: `.github/pull_request_template.md`.
- `gh api --paginate "repos/<org>/<repo>/pulls?state=all&per_page=100"`, then for each pull request `gh api repos/<org>/<repo>/pulls/<n>/reviews` and `gh api --paginate repos/<org>/<repo>/pulls/<n>/commits`.
- `gh api --paginate "repos/<org>/<repo>/commits?sha=<snapshot-sha>&per_page=100"`, then `gh api repos/<org>/<repo>/commits/<sha>/pulls` for each commit, to find commits that reached `main` without a pull request.
- PDF: the member table, for the list of GitHub usernames.

`met`:

- `.github/pull_request_template.md` exists and prompts for all three items: what changed and why; what was checked and how; for the reviewer, what to look at and whether the linked requirements or acceptance criteria are satisfied.
- At least one pull request was merged into `main` at or before the snapshot commit date with an `APPROVED` review from a team member other than its author, submitted before the merge.
- Every member in the PDF member table authored at least one commit that is part of a pull request.
- Every member submitted at least one `APPROVED` review on a pull request authored by another team member.
- Apart from the first commit, every commit on the snapshot's first-parent history reached `main` through a pull request.
- No pull request was merged into `main` without an approving review from another member.
- Branch names are short, lowercase, hyphenated descriptions of the change.

`partial`:

- At least one approved and merged pull request exists, but at least one `met` item is a verified shortfall.
  Typical cases: one member with no commit or no approval, a template missing one of the three prompts, a direct push to `main` after the first commit, a merge with no approval, or branch names such as `patch-1` or a person's name.

`missing`:

- No pull request was merged into `main` with an approval from another member, and no pull request template exists.

Guardrails:

- Count only events at or before the snapshot commit date, per `docs/grader-policy.md`.
- A review whose state is `COMMENTED` or `CHANGES_REQUESTED` is not an approval.
- When a commit's `author.login` is `null` because the commit email is not linked to an account, attribute it to the pull request author and say so in the evidence.
- A commit in a pull request that was still open at the snapshot counts for the member, but say so in the evidence.
- Dependabot pull requests and their `dependabot/...` branches are exempt from the branch-naming rule, but they still need an approving review if merged.
- Do not mark down an initial setup pull request for bundling `LICENSE`, `.gitignore`, and `README.md`; flag "one change per pull request" only for plainly unrelated changes in one pull request.
- Do not require issues, issue links, or `<issue-number>-<description>` branch names; they are `Since: W2`.
- Whether the week report links the approved pull request belongs to S8.

### S4 — Alternatives research

Check:

- Snapshot files: `docs/research/alternatives.md` and `reports/week-01/candidate-list.md`.
- The board link in `docs/research/alternatives.md`, with one access check under `docs/grader-policy.md`.
- Any screenshots under `reports/week-01/images/` used as alternative evidence.

`met`:

- `docs/research/alternatives.md` opens with one problem-space sentence naming whose problem it is and what they are trying to do.
- It has 3–4 alternatives, each in its own section with the ID in the heading (`## ALT-01: <name>`), zero-padded, in research order, and with any removed alternative kept and marked removed with a reason and a date.
- The set includes at least one direct competitor, at least one adjacent substitute, and at least one open-source or self-hosted option.
- Each `ALT-nn` section records: name, product link, and the version or date looked at; the problem it solves and for whom; an observation for each of the chosen properties (at least 6, the same set for every alternative); the sources used (documentation, public repository, pricing page, hands-on use); the depth of evaluation; strengths; and at least two weaknesses, each tied to an observation.
- `reports/week-01/candidate-list.md` lists 10 or more candidates, each with a URL and one line on why it might be relevant, and keeps the cut candidates.
- A research board is linked from `docs/research/alternatives.md`, opens without signing in, and is shared view-only.
- There are at least two described screenshots per alternative, of screens or flows that matter for the properties, on the board or under `reports/week-01/images/`.

`partial`:

- `docs/research/alternatives.md` exists with at least one `ALT-nn` section, but at least one `met` item is a verified shortfall.
  Typical cases: 2 or 5 alternatives, no open-source option, an alternative with one weakness, no version or date, no depth statement, fewer than 10 candidates, a list of survivors only, no board link, or fewer than two relevant screenshots for an alternative.

`missing`:

- `docs/research/alternatives.md` is absent or has no `ALT-nn` section.

Guardrails:

- Do not require a `**Kind:**` field; infer the kind from the entry when it is not labelled.
- Do not require a specific board tool; Figma, Miro, Excalidraw, and similar are all acceptable.
- A pricing-page screenshot does not count toward the two per alternative.
- If the board cannot be opened after one access check, set `Evidence gaps: yes`, and judge the screenshot requirement from repository screenshots only.
- Treat an accessible board as view-only unless the grader is offered editing without signing in.
- Do not mark down because the order "properties before evaluation" cannot be proven from the files.
- The comparison table and the property quality belong to S5; reference accuracy and depth honesty belong to S9.

### S5 — Comparison and gap analysis

Check:

- Snapshot files: `docs/research/comparison.md` and `docs/research/gap-analysis.md`, cross-checked against the `ALT-nn` sections in `docs/research/alternatives.md`.

`met`:

- `docs/research/comparison.md` contains a qualitative analysis table whose rows are properties (at least 6) and whose columns are all non-removed `ALT-nn` alternatives.
- Each property is relevant to the problem space, observable from use, documentation, or source, and independent of the others, not a feature name, pricing tier, or marketing adjective.
- Every cell is analysis rather than a bare "good", "yes", or rating, and references its evidence by `ALT-nn` or by link.
- Cells separate observation from conclusion, and strengths and weaknesses state the condition that makes them matter.
- The file, or `docs/research/gap-analysis.md`, records 3–5 candidates read from the table as a whole, each a disputable claim about the shape of the evidence.
- Each candidate either became a gap that quotes the shape in its `**Evidence:**` field or appears in the rejected list.
- `docs/research/gap-analysis.md` has at least one gap with the ID in the heading (`## GAP-01: <title>`), zero-padded and never renumbered.
- Each gap passes all four tests explicitly: who needs it and what they cannot do; evidence that the alternatives do not serve it; what closing it looks like in one sentence; and why a team of 3–4 can build it in this course.
- Each gap references the `ALT-nn` IDs and the property names that established it.
- The file records at least one gap the team chose not to pursue, with a reason.

`partial`:

- Both files exist, but at least one `met` item is a verified shortfall.
  Typical cases: fewer than 6 properties, a column missing for an alternative, adjective-only cells, cells with no `ALT-nn` or link, no recorded candidates, a gap missing one of the four tests, a gap with no `ALT-nn` reference, or no rejected list.

`missing`:

- Both files are absent, or neither contains a property table or a `GAP-nn` entry.

Guardrails:

- Do not require the guide's exact field labels for gaps; require that each of the four tests is answered in a findable way.
- Do not require the candidates to be under a specific heading.
- Do not mark down a small number of gaps; "A week with two solid gaps is a good week".
- A gap list that is padded with gaps failing the four tests is a verified shortfall here.
- Filler in a required cell or gap field is a shortfall here; filler in free prose belongs to S9.

### S6 — Value proposition and assumptions

Check:

- Snapshot file: `docs/research/value-proposition.md`, cross-checked against `docs/research/gap-analysis.md`.

`met`:

- The file has 2–3 value propositions, each with the ID in the heading (`## VP-01: <title>`), zero-padded.
- Each is a short positioning statement naming the target user, their problem, and what the product does that the alternatives do not.
- Each closes at least one `GAP-nn` that exists in `docs/research/gap-analysis.md` and is not in the rejected list.
- Each names what the advantage costs (more setup, a narrower feature set, a worse default, a higher price, or similar).
- Each says how a competitor would respond.
- No value proposition claims "better", "more modern", "more user-friendly", or "more powerful" without saying better at what, measured how.
- The file ends with an assumptions table of at least one row, in which every assumption traces to a `GAP-nn` or `VP-nn` and states how and when it will be checked.

`partial`:

- At least one `VP-nn` exists, but at least one `met` item is a verified shortfall.
  Typical cases: one or four or more value propositions, a value proposition with no `GAP-nn`, a dangling `GAP-nn` reference, no cost, no competitor response, an unmeasured "better" claim, no assumptions table, or assumptions without a check.

`missing`:

- The file is absent or has no `VP-nn` entry.

Guardrails:

- Assumptions phrased as questions to the Customer are a shortfall, because the requirements say assumptions are not questions for the Customer.
- Do not require the exact `**User:**` field layout from the guide.
- Whether the value proposition reflects the kickoff disagreements belongs to S7.

### S7 — Customer kickoff meeting

Check:

- Snapshot files: `reports/week-01/meeting-script.md`, `reports/week-01/meeting-report.md`, and `reports/week-01/meeting-transcript.md` or `reports/week-01/meeting-notes.md`.
- PDF: the recording link (one access check only), the transcript if publication was refused, and the member table.
- The deviations section of `reports/week-01/README.md`, for an asynchronous meeting.

`met`:

- The meeting script contains `## Context`, `## Questions`, `## Roles`, and `## Key improvements`, in that order, and nothing else.
- `## Context` states the problem-space sentence, what the team believes, and what the meeting has to settle.
- `## Questions` is a numbered list covering the five areas (business goals, end users, current workflow, pain points and constraints, scope) with at least two questions per area, every question tagged open or closed.
- `## Roles` names an interviewer, a note taker, and an observer, each a team member's GitHub username.
- `## Key improvements` shows at least two rewritten questions, each with the before, the after, and the principle named.
- The meeting report contains exactly `## Metadata`, `## Summary`, `## Decisions`, `## Action points`, `## Open questions`, and `## Disagreements`, in that order, and nothing else.
- `## Metadata` gives the date (in Week 1, no later than the snapshot), the duration, the attendees by GitHub username with `Customer`, what was presented, the answer to each of the three permission questions (record, publish a sanitized transcript, share it privately), and a link to the transcript or notes and to the script.
- The attendees include every member in the PDF member table.
- `## Summary` has 3–5 bullets on what the meeting settled or changed.
- `## Decisions` has the columns `Decision`, `Made by`, `Traces to`, and at least 2 rows that trace to an existing `GAP-nn` or `VP-nn`.
- `## Action points` has the columns `Action`, `Owner`, `Due`, and at least 2 rows, each with a team member's GitHub username as owner and a due date inside Week 2 (2–8 October 2026, or "Week 2").
- `## Open questions` has the columns `Question`, `What it would change`, `Follow-up`, or says `None`.
- `## Disagreements` has the columns `Your position`, `Customer's position`, `What you changed`, or says `None`.
- Every change named in `What you changed` is visible in the research files at the snapshot.
- Exactly one of `meeting-transcript.md` and `meeting-notes.md` is committed, unless publication was refused, in which case the transcript is in the PDF and the week report says so.
- A transcript is in English, one sentence per line, each line starting with `[hh:mm:ss]` and a speaker label, using GitHub usernames and `Customer`, with `[inaudible]` and `[redacted]` where needed.
- Notes are chronological prose covering what was presented, what the Customer said, what was decided, and what was left open.
- The meeting artifacts call the Customer `Customer`, never a real name and never "the instructor".
- The recording link is in the PDF when recording was permitted.

`partial`:

- A meeting report exists, but at least one `met` item is a verified shortfall.
  Typical cases: one script area with a single question, untagged questions, a `## Key improvements` section with claims but no before and after, an extra or missing report section, fewer than 2 traced decisions, an action point without an owner or with a due date outside Week 2, both transcript and notes committed, a `Disagreements` change that the research files do not reflect, or no recording link in the PDF although recording was permitted.

`missing`:

- `reports/week-01/meeting-report.md` is absent, or the evidence shows no kickoff meeting took place and no asynchronous substitution was declared.

Guardrails:

- An explicit `None` in `## Disagreements` meets the requirement; do not downgrade on it alone.
- Do not mark down the meeting duration; 30 minutes is a plan, not a minimum.
- A declared asynchronous meeting is acceptable: the script has no `## Roles`, the notes are a timestamped written exchange, and the role and length rules do not apply.
- Do not mark down the absence of a recording link when the meeting report says recording was refused.
- Never watch or transcribe the recording; one access check decides whether it is reachable, and an unreachable link is an evidence gap for this segment only.
- A transcript or notes that the Customer refused to publish must not be in the repository; finding it there is a shortfall here.
- Recording links, emails, and other private-only material committed anywhere belong to S8; the naming of the Customer and of members inside the meeting artifacts belongs here.
- Do not judge the content of the recording or the transcript beyond these structural and consistency checks.

### S8 — Week report and submission

Check:

- PDF: page count, project name, team number, member table, permalink, recording link, refused transcript if any, privacy line, and anything else it contains.
- `gh api repos/<org>/<repo>/compare/<snapshot-sha>...main --jq .status`, to confirm the snapshot is on `main`.
- `gh api repos/<org>/<repo>/commits/<snapshot-sha> --jq .commit.committer.date`, for the snapshot commit date.
- Snapshot file: `reports/week-01/README.md`, and every link in it.
- `A1/itpd/course/teams-and-projects.md`, for the team number and project pair.
- A search of the whole snapshot for private-only material (see the procedure deltas).

`met`:

- The PDF is at most two pages and contains only the six required items: project name and team number; a table of members with GitHub username, real name, and university email; a permalink to `reports/week-01/README.md` at a full 40-character SHA; the recording link; the transcript, only if the Customer refused publication; and one line confirming no private-only material was committed.
- The member table lists 3 or 4 members, and the team number and project match `A1/itpd/course/teams-and-projects.md`.
- The permalink commit is on `main`.
- `reports/week-01/README.md` opens with the project name, the team number, and the problem-space sentence, which matches the one in `docs/research/alternatives.md`.
- It contains a short summary of what the team found and what it proposes.
- It contains a coverage table with one row per deliverable (candidate list, alternatives search, comparison, gap analysis, value proposition, research board, meeting script, Customer kickoff, AI usage), each linking the artifact that satisfies it, and no second list of the same links after it.
- When the Customer refused publication of the transcript or the notes, the kickoff row says so and points at the Moodle submission.
- It contains the three pieces of repository evidence: the branch protection screenshot, a link to a merged pull request approved by another member (verified as such through `gh api`), and a link to the latest green link-check run on `main`.
- It contains a contribution table mapping every member's GitHub username to their commits, issues, pull requests, and reviews, with links where possible, and the linked items match the GitHub data.
- It links the root `LICENSE`.
- It has a deviations section, with each deviation and its reason, or `None`.
- It has one line confirming that no private-only material was committed.
- It does not repeat the kickoff open questions, which live in `meeting-report.md`.
- The snapshot contains no private-only material: no university or personal email addresses, no real names of members, no recording links or timecodes into recordings, no `.env` files, and no credentials.

`partial`:

- `reports/week-01/README.md` exists and the PDF carries a usable permalink, but at least one `met` item is a verified shortfall.
  Typical cases: a missing coverage row, a missing evidence link, a linked pull request that was not approved by another member, a contribution table missing a member, no `LICENSE` link, no deviations section, no privacy line, a PDF over two pages or carrying copied report content, or committed private-only material.

`missing`:

- `reports/week-01/README.md` is absent from the snapshot, or no PDF was submitted.

Guardrails:

- An empty issues column in the contribution table is fine; issues are `Since: W2`.
- Do not apply late penalties; record the snapshot commit date in the evidence when it is after the hard deadline, and leave lateness to the instructor.
- A team number and project pair that disagrees with `A1/itpd/course/teams-and-projects.md` is conflicting evidence, not a verified shortfall, because the instructor may have approved a swap.
- A team of 2 or 5 is a verified shortfall here; say so without naming anyone.
- Never copy a real name, email address, or recording link into the feedback, including when reporting that one was committed; give the path and line number instead.
- The `.lycheeignore` justification and the browser-check confirmation belong to S2, even though they sit in the week report.
- The snapshot-resolution rules are in `docs/grader-policy.md`; record the effect on this segment here.
- Teams submit no ZIP; do not require or report on one.

### S9 — AI usage and research honesty

Check:

- Snapshot file: `reports/week-01/ai-usage.md`.
- Free prose across the week: `reports/week-01/README.md` summary, the problem statements and depth statements in `docs/research/alternatives.md`, and the prose of the gaps and value propositions.
- At least three references cited for product claims in `docs/research/alternatives.md` or `docs/research/comparison.md`, opened and compared with the claim they support.
- Mentions of transcription or drafting tools in the meeting artifacts.

`met`:

- `reports/week-01/ai-usage.md` names the tools used and what they were used for, and says what was accepted, changed, and rejected and why, or states in one line that no AI tools were used.
- Any tool used to transcribe or draft the meeting report is declared there.
- The spot-checked references exist and support the claims that cite them.
- Inferences are labelled as inferences, and confidence is stated where the evidence is thin.
- The research does not make claims about a product's roadmap, funding, or business.
- The free prose contains no filler under `docs/grader-policy.md`, and no leftover generated output such as chat preambles, placeholder brackets, or "as an AI" phrasing.

`partial`:

- `reports/week-01/ai-usage.md` exists, but at least one `met` item is a verified shortfall.
  Typical cases: tools named without what was accepted, changed, or rejected; an undeclared transcription tool named in the meeting artifacts; a reference that does not support its claim; unlabelled inferences; claims about funding; or quoted filler fragments.

`missing`:

- `reports/week-01/ai-usage.md` is absent, or it contains neither a disclosure nor a no-AI line.

Guardrails:

- Never penalise disclosed AI use.
- Never infer undisclosed AI use from writing style alone; cite a concrete artifact (a leftover prompt, a placeholder, a fabricated reference).
- A reference that is rate-limited, paywalled, or sign-in gated is not fabricated; pick another reference, and set `Evidence gaps: yes` only when no checkable reference remains.
- Quote at most a short fragment when citing filler.
- Structural shortfalls in required fields belong to S4–S7; this segment owns disclosure, reference accuracy, and free-prose quality.

## Assignment-specific procedure deltas

1. Determine the team set from the directory names under `itpd-assignments-feedback/A1/submissions/`.
2. Read the Moodle PDF first.
   If a team directory holds more than one PDF, use the one that carries the permalink.
3. From the PDF, extract: the project name, the team number, the member table as GitHub usernames only, the permalink and its SHA, the recording link, whether a transcript is included, the privacy confirmation line, and the page count.
   Keep real names and emails out of notes and feedback.
4. Resolve the snapshot under `docs/grader-policy.md`, and fetch it from GitHub into `itpd-assignments-feedback/A1/work/<team_dir>/`.
5. Record the snapshot commit date and confirm the snapshot is on `main`:

   ```bash
   gh api repos/<org>/<repo>/commits/<sha> --jq .commit.committer.date
   gh api repos/<org>/<repo>/compare/<sha>...main --jq .status
   ```

   A status of `identical` or `ahead` means the snapshot is on `main`.
6. Collect the repository and protection evidence for S1:

   ```bash
   gh api repos/<org>/<repo>
   gh api repos/<org>/<repo>/collaborators
   gh api repos/<org>/<repo>/branches/main
   gh api repos/<org>/<repo>/branches/main/protection
   gh api repos/<org>/<repo>/rules/branches/main
   ```

7. Collect the pull request evidence for S3 and build a member matrix of commits through pull requests and approvals of other members' pull requests, counting only events at or before the snapshot commit date:

   ```bash
   gh api --paginate "repos/<org>/<repo>/pulls?state=all&per_page=100"
   gh api repos/<org>/<repo>/pulls/<n>/reviews
   gh api --paginate repos/<org>/<repo>/pulls/<n>/commits
   gh api --paginate "repos/<org>/<repo>/commits?sha=<sha>&per_page=100"
   gh api repos/<org>/<repo>/commits/<commit-sha>/pulls
   ```

8. Collect the Actions evidence for S2:

   ```bash
   gh api "repos/<org>/<repo>/actions/runs?branch=main&event=push&per_page=30"
   gh api "repos/<org>/<repo>/actions/runs?event=pull_request&per_page=30"
   ```

9. Verify the three repository-evidence links in the week report against the data from steps 7 and 8.
10. Make one access check each for the research board and the recording link.
11. Search the unpacked snapshot for private-only material: email addresses, recording links (for example Zoom, Telemost, Google Drive, Yandex Disk, or YouTube links in meeting artifacts), timecodes into recordings, `.env` files, and token-shaped strings.
    Report matches by path and line only.
12. Spot-check at least three product references for S9.
13. Judge each of the nine segments independently with the status guide above.

## Assignment-specific constraints

- The member table with real names and university emails, the recording link, and a transcript the Customer refused to publish are Moodle-only; never penalise their absence from the repository.
- Alternative screenshots are expected on the external board; their absence from the repository is not a shortfall when the board shows them.
- The branch protection screenshot is the one screenshot that must be committed, under `reports/week-01/images/`.
- Recordings and boards get one access check each, and an inaccessible one is an evidence gap for the segment that needs it, never verified absence.
- Week 1 has no code, prototype, or deployment; never mark down their absence.
- Do not apply `Since: W2` or later requirements: issue templates, issue-linked branch names, `docs/work-plan.md`, setup instructions in the root README, `CHANGELOG.md`, tags, or stack CI.
- Grade against the Assignment 1 text at `fe58ba7` even when the current course repository says something else.
- The `Primary index reviewed` bullet points at `reports/week-01/README.md` whenever the snapshot is inspectable.
- In feedback, call the instructor `Customer` when referring to the meeting role, and refer to members by GitHub username only.
