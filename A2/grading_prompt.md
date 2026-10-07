# Assignment 2 Grading Criteria

This rubric is for an LLM grading agent that reviews ITPD Assignment 2 team submissions.
ITPD assigns no points: each segment gets one status, `met`, `partial`, `missing`, or `unverified`, and an `Evidence gaps: yes|no` flag, per `docs/grading-feedback-format.md`.
The instructor assigns the grade from the statuses and the evidence, so this rubric never proposes a grade, a score, or a late penalty.
The shared rules live in `docs/grader-policy.md`: evidence states, verified absence, blocked and conflicting artifacts, snapshot resolution, live GitHub evidence through `gh api`, the single access check for consumer-hosted media, privacy, undeclared deviations, and rule applicability by `Since:` marker.
This file states only what is specific to Assignment 2 and does not repeat those rules.

## Authoritative sources

All paths are in the course-materials submodule, pinned at itpd commit `a949e8d7ff7f677ed3b97fa1b9bd9291b4a05bc1`.
If the checked-out submodule differs from that commit, read each file with `git -C A2/itpd show a949e8d7ff7f677ed3b97fa1b9bd9291b4a05bc1:<path>`.

- `A2/itpd/assignments/assignment-2.md` — the student-facing brief: Parts 1–11, What Good Looks Like, the repository report contents, the Moodle PDF contents, the submission procedure, and the checklist.
- `A2/itpd/requirements/general-requirements.md` — formatting-only changes, identifier rules (bare-identifier headings, bulleted fields, `**Status:**` first, dropped items), and traceability into later weeks.
- `A2/itpd/requirements/repository-requirements.md` — issue tracking, branch naming, the pull request template, link checking, action pinning, permalinks and snapshots, the Markdown check, and the course materials as an agent skill.
- `A2/itpd/requirements/user-stories-requirements.md` — story issues, the story issue form and its labels, the story, acceptance criteria, and MoSCoW priorities.
- `A2/itpd/requirements/task-issues-requirements.md` — task issues, the task issue form, task acceptance criteria, and closing a task.
- `A2/itpd/requirements/local-task-tracking-requirements.md` — an in-repository tracker, `TODO.md`, and the Done-task workflow, all Recommended only.
- `A2/itpd/requirements/decisions-requirements.md` — the decision entry, its fields, what cites it, and reversing it.
- `A2/itpd/requirements/assumptions-requirements.md` — the assumption entry, what rests on it, and checking and settling it.
- `A2/itpd/requirements/research-requirements.md` — the Week 2 field orders of `ALT-nn`, `GAP-nn`, and `VP-nn` sections, their statuses, and the research honesty rules.
- `A2/itpd/requirements/product-vision-requirements.md` — the goal, stakeholders, `CON-nn` constraints, `BND-nn` boundary items, and the system context diagram.
- `A2/itpd/requirements/minimum-usable-product-requirements.md` — where the candidate lives, what it contains, and the customer's verdict on it.
- `A2/itpd/requirements/prototypes-requirements.md` — the prototype record, keeping prototype code off `main`, and the four places a customer-driven change is recorded.
- `A2/itpd/requirements/customer-meetings-requirements.md` — every meeting, permission questions, the meeting script, report, and transcript, and the Week 2 report example.
- `A2/itpd/requirements/weekly-report-requirements.md` — the weekly public report, the AI usage report, declaring deviations, and the Moodle PDF.
- `A2/itpd/requirements/visibility-requirements.md` — what is public, what is Moodle only, and screenshot sanitization.
- `A2/itpd/course/rules.md` — the course contract, the AI policy, the generic deadline pair, and the submission channel.
- `A2/itpd/course/syllabus.md` — the Week 2 deliverables and minima, and the Week 2 hard-deadline exception.
- `A2/itpd/guides/user-stories-and-prototyping.md` and `A2/itpd/guides/validating-with-the-customer.md` — the method, used to judge quality and never as extra requirements.
- `A2/itpd/AGENTS.md` — course terminology and the `docs/` destination map for Week 2.

Apply only rules marked `**Since: W1**` or `**Since: W2**`.
These `**Since: W3**` rules do not apply: root `README.md` setup instructions, Showing Working Software, Contributing, Changelog, Releases And Versioning, continuous integration rules 6–8 for product code, and the `CONTRIBUTING.md` statement about `TODO.md`.

## Assignment parameters

- Report title: `# Assignment 2 Feedback Report`
- Week: `W2`
- Course materials: `A2/itpd` at `a949e8d7ff7f677ed3b97fa1b9bd9291b4a05bc1`
- Primary index artifact: `reports/week-02/README.md` at the snapshot, as named in Assignment Report In The Repository and in Moodle item 3 of `assignment-2.md`.
- Soft deadline: Thursday 8 October 2026, 23:59.
- Hard deadline: Saturday 10 October 2026, 23:59, the Week 2 exception that `course/syllabus.md` states.
- The time zone is not stated; read both deadlines as Innopolis time (UTC+3).
- Submission inputs: the Moodle PDF under `itpd-assignments-feedback/A2/submissions/<team_dir>/`; there is no ZIP.
  The snapshot is fetched from GitHub at the permalink SHA into `itpd-assignments-feedback/A2/work/<team_dir>/`.
- Live artifact families: story and task issues with their comments, timelines, and edit history; repository labels; pull requests with their reviews, files, and closing references; Actions runs of the Markdown check and the link check; external prototype views; and the meeting recording link.
- Story and task issues are not in the snapshot, so they are read live and judged as of the snapshot commit time, per [procedure step 6](#assignment-specific-procedure-deltas).

The segments, in order:

- S1: Issue forms, labels, and task workflow
- S2: Decisions and assumptions in the Week 2 format
- S3: Markdown CI and research entry format
- S4: Product vision and context diagram
- S5: User stories and acceptance criteria
- S6: Minimum usable product candidate
- S7: Prototypes and customer-driven change
- S8: Customer validation meeting
- S9: Week report and submission
- S10: AI usage and research honesty

### Segment overview

Every checklist item and every coverage-table row of `assignment-2.md` maps to exactly one segment, and a shortfall is reported only in the segment that owns it.

| Segment | Covers |
|---------|--------|
| S1: Issue forms, labels, and task workflow | Part 1; checklist items "`.github/ISSUE_TEMPLATE/user-story.yml`, `task.yml`, `config.yml`, and the labels, in one pull request started from a blank issue", "`Story` and `Acceptance criteria` fields in `task.yml`, and every pull request closing one task issue", "A `Rests on` field in `user-story.yml`, and every story's `ASM-nn` in its `Rests on` list", and "`.github/pull_request_template.md` links the task issue"; coverage rows Issue forms, Labels, and Pull request template |
| S2: Decisions and assumptions in the Week 2 format | Parts 2 and 3; checklist items "`docs/decisions.md` with a `DEC-nnn` section for each Week 1 decision" and "`docs/assumptions.md` with an `ASM-nn` section for each Week 1 assumption, and no table left in `value-proposition.md`"; coverage rows Assumptions and Decisions; the entry format of every decision and assumption |
| S3: Markdown CI and research entry format | Part 4; checklist items "Earlier weeks' Markdown fixed in a formatting-only pull request", "`ALT-nn`, `GAP-nn`, and `VP-nn` headings cut down to their identifiers", and "Markdown check and link check green on `main`"; every Week 2 edit to `reports/week-01/` |
| S4: Product vision and context diagram | Part 5; checklist item "`docs/product-vision.md`, with its constraints as `CON-nn` sections, at least 3 `BND-nn` boundary items, and the system context diagram"; coverage rows Product vision and System context diagram |
| S5: User stories and acceptance criteria | Part 6; checklist item "The story issues"; coverage row Story issues |
| S6: Minimum usable product candidate | Part 7; checklist item "`## Minimum Usable Product Candidate` in `reports/week-02/README.md`"; repository report item 3 |
| S7: Prototypes and customer-driven change | Part 8, and the Part 10 rules "Change something because of what the customer said about the prototype" and "Add a comment to each story issue the meeting changed"; checklist items "`reports/week-02/prototypes.md` with at least one prototype, and no prototype code on `main`" and "At least one artifact changed because of what the customer said about the prototype, citing its `DEC-nnn`"; coverage row Prototypes; repository report item 4 |
| S8: Customer validation meeting | Part 9, and Part 10 apart from the two rules S7 owns; checklist items "Each kickoff action point's outcome in `## Previous action points`", "Each kickoff open question answered or carried forward", "`reports/week-02/meeting-script.md`", "`reports/week-02/meeting-report.md`", and "`reports/week-02/meeting-transcript.md`, if the meeting was recorded or held in writing"; coverage rows Kickoff action points, Kickoff open questions, Meeting script, and Customer validation; Moodle items 4 and 5 |
| S9: Week report and submission | Assignment Report In The Repository items 1, 2, 5, and 6 and the base Weekly Public Report rules; Moodle items 1, 2, 3, and 6; the Submission Procedure; checklist items "`reports/week-02/README.md`", "Everything merged into `main`, with the permalink and the snapshot taken from that commit", and "PDF ready, and the permalink opened in a browser at the full commit hash" |
| S10: AI usage and research honesty | Part 11; checklist item "`reports/week-02/ai-usage.md`"; coverage row AI usage; Research Honesty Rules and AI Usage Report rule 5 for text added or changed in Week 2 |

The coverage-table rows map to the segment that judges the artifact in the row.
Whether the table has the row and links it is judged in S9.

## Status guide

Use the status vocabulary of `docs/grading-feedback-format.md` and the evidence states of `docs/grader-policy.md`.
A segment is `met` only when every `met` criterion below holds on verified evidence.
A segment is `partial` when its core artifact exists and at least one verified shortfall remains.
A segment is `missing` when the `missing` criterion below holds.
A segment is `unverified` when its core evidence could not be read, such as S1 or S5 when `gh` cannot read the repository's issues or pull requests at all.
Recommended items and the What Good Looks Like points are quality notes for the instructor, and they never cause a shortfall unless they coincide with a Required rule.

### S1 — Issue forms, labels, and task workflow

**Check:**

- `.github/ISSUE_TEMPLATE/user-story.yml`, `.github/ISSUE_TEMPLATE/task.yml`, `.github/ISSUE_TEMPLATE/config.yml`, and `.github/pull_request_template.md` in the snapshot.
- The repository's labels, from `gh label list`.
- Every pull request and every `task` issue, from the `gh pr list` and `gh issue list` calls in [procedure step 5](#assignment-specific-procedure-deltas).
- The commits and pull requests that added or changed the issue forms, from the path history in procedure step 5.
- The `### Traces to` and `### Rests on` sections of every story issue.

**met:**

- `user-story.yml` is an Issue Form, a `body:` list of fields, that applies `user-story` through `labels:` or applies the issue type or field that User Story Requirements rule 6 allows instead.
- `user-story.yml` has a field for the statement, `Value proposition`, `Traces to`, `Rests on`, the acceptance criteria, and `Priority reason`.
- In `user-story.yml`, the statement, `Value proposition`, and `Priority reason` are `required: true`, `Value proposition` is a single-line `input`, and `Traces to`, `Rests on`, and the acceptance criteria are optional.
- `task.yml` is an Issue Form that applies `task`, with a required description field, an optional `Story` field, and a required `Acceptance criteria` field.
- `config.yml` sets `blank_issues_enabled: false`.
- The labels `user-story`, `task`, `moscow:must`, `moscow:should`, `moscow:could`, and `moscow:won't` exist, or the issue type or field that replaces a label exists.
- One pull request, the forms pull request, added all three files and was merged before every other Week 2 pull request.
- The forms pull request closes the blank issue it started from, its branch is named `<that issue's number>-<short-description>`, and that issue now carries the `task` label.
- A `Rests on` field added after the forms pull request came in a pull request of its own, and so did a `Story` or `Acceptance criteria` field added to `task.yml`.
- No story issue lists an `ASM-nn` under `### Traces to`; each one sits under `### Rests on`.
- `.github/pull_request_template.md` prompts for what changed and why, what was checked and how, and what the reviewer should look at, and it asks for the task issue the pull request closes, for example with a `Closes #` line.
- Every in-scope pull request closes exactly one issue, that issue carries `task`, and it is never a story issue.
- Every in-scope pull request's head branch is `<closed task number>-<short lowercase hyphenated description>`.
- Every merged in-scope pull request has an approving review from a member other than its author, its task's acceptance-criteria boxes are all ticked, and its task closed as completed.
- Every pull request closed without merging, and every abandoned task, left its task closed as not planned with a comment that gives the reason and links the pull request when there is one.
- Every task issue opened after the forms pull request carries `task`, has at least one criterion written as a checklist item `- [ ] AC-nn:` numbered within the issue, and has a `Story` field that is empty or lists story issues as `- #<n>`, optionally followed by `(AC-nn, ...)`.

**partial:**

- The three files and the labels exist, and at least one other `met` criterion fails.
- Typical shortfalls: a pull request that closes no issue, two issues, or a story issue; a branch without the task number; a merged pull request with no non-author approval or with unticked criteria; the blank issue without `task`; an `ASM-nn` left in `Traces to`; a catch-up field added inside an unrelated pull request; a template that does not ask for the task issue.

**missing:**

- `user-story.yml` or `task.yml` is absent at the snapshot, or no in-scope pull request closes a task issue.

**Guardrails:**

- In scope are the pull requests created on or after the forms pull request and merged or closed at or before the snapshot commit time.
  Earlier pull requests follow the Week 1 rules and were graded in Assignment 1.
- Dependabot pull requests and the pull requests a Done-task workflow opens are exempt from the closing and branch-name rules.
- A pull request merged before the `task.yml` catch-up that referenced a story needs no change.
- A team that disabled blank issues before it had a task form may have opened the forms pull request's issue with `gh issue create`; that is allowed.
- Labels are not part of a pull request, so check only that they exist.
- An in-repository tracker, `TODO.md`, and a Done-task workflow are Recommended, and their absence is never a shortfall.
- Branch protection settings are a Week 1 rule; do not query or re-grade them, and report an unapproved merged Week 2 pull request here as a workflow shortfall.
- A story issue that a pull request closed is reported here only, not again in S5.
- With more than 40 in-scope pull requests, check every closing reference and branch name from the JSON, check reviews and ticked criteria on at least 10 merged pull requests including the forms pull request and the one the README cites, and name the sample in `**Evidence:**`.

### S2 — Decisions and assumptions in the Week 2 format

**Check:**

- `docs/decisions.md`, `docs/assumptions.md`, and `docs/research/value-proposition.md` in the snapshot.
- The Week 1 sources: the `## Decisions` table of `reports/week-01/meeting-report.md`, with the columns `Decision`, `Made by`, and `Traces to`, and the team's `## Decisions` table in `reports/week-01/README.md` when it has one.
- The Week 1 assumptions table, read from the base of the pull request that moved it, with `gh pr diff <n> --repo "$REPO"`.
- The path history of `docs/decisions.md` and `docs/assumptions.md`, and the creation and edit times of the first story issue that links a `DEC-nnn` or an `ASM-nn`.
- Every artifact named in a Week 1 decision row's `Traces to`.

**met:**

- `docs/decisions.md` has one `## DEC-nnn` section per Week 1 decision row, the kickoff rows first and then the README rows, numbered in that order with three digits, and every section is in identifier order.
- Every entry, migrated or new, has a first line that states the decision in one sentence, followed by its fields as a bulleted list, one `- **Label:** value` bullet each, in the order `**Status:**`, `**Reverses:**` only on a reversal, `**Date:**`, `**Made by:**`, `**Source:**`, `**Why:**`.
- `**Status:**` is `Active` or `Reversed by DEC-nnn` with the reversing entry linked, and `**Made by:**` is `Customer`, `Team`, or `Team, not contested`.
- A kickoff row's entry has the kickoff date, the row's `Made by` mapped to one of the three values, and a `**Source:**` that links `reports/week-01/meeting-report.md`.
- A README row's entry has the date the team decided and `**Made by:** Team`.
- No entry lists what it changed, so there is no `Changes`, `TBD`, or `None` field.
- Each Week 1 decision whose `Traces to` names an artifact it changed is cited, linked, from that artifact: a dropped item's `**Dropped:**` reason, a `**Changed:**` bullet of a `GAP-nn` or `VP-nn`, or an assumption's `**Outcome:**`.
- `docs/assumptions.md` has one `## ASM-nn` section per row of the Week 1 assumptions table, numbered in the table's order, each first line a one-sentence belief that can turn out false.
- Every assumption's fields are bulleted, with `**Status:**` first and set to `Open`, `Confirmed`, `Refuted`, or `Dropped`, and a `**How to check:**` that says how and in which week.
- Every `Confirmed` or `Refuted` assumption has an `**Outcome:**` that says what was found and links the evidence, citing the `DEC-nnn` when a decision settled it, and every `Dropped` one ends with `**Dropped:**`.
- No assumption entry lists what rests on it.
- `docs/research/value-proposition.md` keeps no assumptions table.
- The decisions were migrated in one pull request and the assumptions in one pull request, and both were merged into `main` before the first story issue that links them was opened or edited to add the link.

**partial:**

- Both files exist with identifier sections, and at least one other `met` criterion fails.
- Typical shortfalls: a Week 1 row with no entry; numbering out of the required order; fields as plain lines or a table; a field out of order or under another label; an assumptions table left in `value-proposition.md`; a settled assumption with no `**Outcome:**`; a changed artifact that does not cite its decision; a migration merged after a story linked it.

**missing:**

- `docs/decisions.md` or `docs/assumptions.md` is absent at the snapshot, or either one still holds only the Week 1 table with no `## DEC-nnn` or `## ASM-nn` sections.

**Guardrails:**

- A team that already kept `docs/decisions.md` or `docs/assumptions.md` in sections in Week 1 is judged on the end state; the catch-up pull request is not required.
- A Week 1 with no decision rows or no assumption rows needs no migrated entries.
- Accept any reasonable mapping of a free-text Week 1 `Made by` value to one of the three allowed values.
- Do not grade the quality of the Week 1 decisions or assumptions themselves; a thin `**Why:**` carried over from Week 1 is a quality note.
- Edits to `reports/week-01/` belong to S3.
- Whether the Week 2 meeting made and listed its decisions belongs to S8; this segment judges only the format of their entries.
- Citations of the decision behind the customer-driven change belong to S7.

### S3 — Markdown CI and research entry format

**Check:**

- `.github/workflows/*.yml`, every Markdown tool configuration and ignore file (`.markdownlint-cli2.*`, `.markdownlint.*`, `.markdownlintignore`, `.prettierrc*`, `.prettierignore`, `.remarkrc*`), `package.json` and its lockfile when the workflow installs the tool, and `lychee.toml`.
- `docs/research/alternatives.md`, `docs/research/gap-analysis.md`, `docs/research/value-proposition.md`, and every Markdown file that links them, including `reports/week-01/`.
- The Actions runs of the Markdown check and the link check on `main`, and the runs on the snapshot SHA.
- The pull requests in the Week 2 window that touch `reports/week-01/`, `docs/research/`, or `.github/workflows/`, with their diffs.
- Old anchors, with `grep -rnE '#(alt|gap|vp)-[0-9]{2}-' --include='*.md' .` in the work directory and the same pattern in story issue bodies.

**met:**

- A Markdown workflow runs on `pull_request` and on `push` to `main`, runs `markdownlint-cli2`, `prettier --check`, `remark-lint`, or a declared equivalent, and fails the job on a finding, with no `continue-on-error: true`, `|| true`, or report-only flag.
- Every third-party `uses:` in the Markdown workflow is pinned to a full 40-character SHA with the version in a trailing comment, and the tool's version is pinned by the action or by a committed lockfile.
- Nothing is excluded from the Markdown check except a task tracker's directory, such as `backlog/**`, and the course-materials submodule's directory, such as `.agents/skills/itpd/**`.
- The latest Markdown check run and the latest link-check run on `main` at or before the snapshot commit time both concluded `success`.
- A formatting-only pull request that fixed earlier weeks' Markdown was merged before the pull request that added the Markdown workflow, and the first Markdown check run on `main` was green.
- A pull request of its own cut every `ALT-nn`, `GAP-nn`, and `VP-nn` heading in `docs/research/` down to the bare identifier, such as `## GAP-01`, with the title on the line under it, and it was merged before the first story issue that links a `VP-nn` was opened.
- No link in the snapshot or in a story issue body still targets a pre-cut anchor such as `#gap-01-<title>`.
- Every `ALT-nn` section has its bulleted fields in the order `**Status:**`, `**Kind:**`, `**Link:**`, `**Version looked at:**`, `**Depth of evaluation:**`, `**Problem it solves:**`, then `**Dropped:**` only when dropped, followed by the `**Observations by property**` table with the columns `Property` and `Observation`, and the `**Strengths**` and `**Weaknesses**` lists.
- Every `GAP-nn` section has its bulleted fields in the order `**Status:**`, `**Who needs it and what they cannot do:**`, `**Evidence:**`, `**What closing it looks like:**`, `**Buildable by us in this course:**`, `**Confidence:**`, then `**Rests on:**`, `**Changed:**`, and `**Dropped:**` only when they apply, and every gap has a `**Confidence:**`.
- Every `VP-nn` section has its bulleted fields in the order `**Status:**`, `**User:**`, `**Problem:**`, `**What we do that the alternatives do not:**`, `**Closes:**`, `**Rests on:**` when it applies, `**What it costs:**`, `**How a competitor would respond:**`, then `**Changed:**` and `**Dropped:**` only when they apply.
- Every `**Status:**` is `Active` or `Dropped`, and every dropped item ends with a `**Dropped:**` that gives the date and the reason, citing the linked `DEC-nnn` when a decision dropped it.
- A dropped gap lists no value propositions it affected, every value proposition that closes it keeps it under `**Closes:**` and records the drop under `**Changed:**`, and a value proposition that closes no `Active` gap is `Dropped`.
- Every Week 2 change to `reports/week-01/` is formatting-only, such as whitespace, list markers, heading levels, table alignment, or a link repointed at the same section, and it sits in a pull request with no other kind of change.

**partial:**

- A Markdown workflow exists or the research entries were converted, and at least one other `met` criterion fails.
- Typical shortfalls: the latest `main` run red; an action pinned to a tag; an extra exclusion; a titled research heading left; fields not bulleted or out of order; a gap with no `**Confidence:**`; an old anchor left; a reworded Week 1 report; the formatting fix merged after the workflow.

**missing:**

- There is no Markdown check workflow at the snapshot, and the research entries are still in their Week 1 form.

**Guardrails:**

- The link-check configuration and Dependabot are Week 1 artifacts; judge here only that the latest link-check run on `main` is green and that any exclusion added in Week 2 carries its reason in the file that excludes it.
- A team whose Markdown had nothing to fix needs no formatting pull request, provided the first Markdown check run on `main` was green.
- Files that `.gitignore` lists are not in the repository, so skipping them is not an exclusion.
- A field label must match the requirement's wording; a case-only difference is a quality note, and a label in other words is a shortfall.
- Do not re-grade the Week 1 research content, such as the number of alternatives, the properties, or the gap tests.
- When the Actions runs cannot be read, use the `statusCheckRollup` of the pull requests; if neither can be read, mark the CI criterion unverified with `Evidence gaps: yes` and judge the rest.

### S4 — Product vision and context diagram

**Check:**

- `docs/product-vision.md` and `docs/architecture/` in the snapshot.
- The rendered permalink `https://github.com/<org>/<repo>/blob/<SHA>/docs/product-vision.md`, and the diagram image opened directly.
- `docs/research/value-proposition.md`, for the status of each `VP-nn` the goal links.

**met:**

- `docs/product-vision.md` is the only file that carries the vision; no report or other file restates the goal, constraints, or boundary.
- The goal states in one sentence what the product must achieve, and it links at least one `Active` `VP-nn` section in `docs/research/value-proposition.md` rather than restating it.
- The stakeholders name who the product is for, who operates it, who pays for it, and who is affected without using it, and they include the customer.
- `## Constraints` holds at least one `### CON-nn` section whose first line states the condition.
- Every constraint's bulleted fields are in the order `**Status:**` (`Active` or `Dropped`), `**Source:**` (`Customer-given`, `Team-given`, `Environmental`, or `Derived`), `**What it costs:**`, `**Decision:**` with the `DEC-nnn` linked only when a decision imposed it, then `**Changed:**` and `**Dropped:**` only when they apply.
- No constraint is an assumption or a technology choice the team made, and every customer mandate's `**Decision:**` cites its `DEC-nnn`.
- `## Boundary` holds at least 3 `### BND-nn` sections, each first line one job somebody could expect the product to do rather than a quality.
- Every boundary item's bulleted fields are in the order `**Status:**` (`Active` or `Dropped`), `**Handled by:**` (an external system or actor, the user by hand, or `Nobody`), `**Why:**` (a linked `CON-nn`, a linked `DEC-nnn`, or the team's reasoning), then `**Changed:**` and `**Dropped:**` only when they apply.
- The diagram is committed at `docs/architecture/context.<ext>` as an image GitHub renders, such as SVG or PNG, and `docs/product-vision.md` embeds it with an image link.
- When the drawing tool saves a source file, such as `.mmd`, `.puml`, `.d2`, `.drawio`, or `.excalidraw`, it is committed beside the image with the same base name.
- The diagram shows the product as one box with the external actors and systems around it, and it is not a use case diagram or a drawing of components, containers, or internal structure.
- The diagram has an opaque background or otherwise stays legible in both the light and the dark GitHub theme.
- Prose next to the diagram describes the external actors without restating the diagram.
- Every external system or actor named in a `**Handled by:**` appears on the diagram, and nothing on the diagram does a job the product claims or a job the boundary leaves to `Nobody`.
- The vision links the story list, filtered by the `user-story` label or the team's marker, and the current week's report.

**partial:**

- `docs/product-vision.md` exists, and at least one other `met` criterion fails.
- Typical shortfalls: a goal with no `VP-nn` link; fewer than 3 `BND-nn` items; constraints or boundary items as a table or paragraph; a constraint that is an assumption or a team technology choice; a missing stakeholder role; a diagram given only as a Mermaid block or a view-only link; a transparent diagram that disappears on the dark theme; a `**Handled by:**` system missing from the diagram.

**missing:**

- `docs/product-vision.md` is absent at the snapshot.

**Guardrails:**

- "A goal that could fail" and "a boundary somebody argued with" are quality notes; record a goal that names a feature rather than an outcome in `**Evidence:**` for the instructor.
- Assumption–constraint confusion is a shortfall only when the item states an unverified belief rather than a condition the team cannot change.
- Judge dark-theme legibility from the file: an SVG with a filled background element, or a PNG without transparency, passes; when it cannot be determined, say so in `**Evidence:**` without raising an evidence gap.
- Whether stories and priorities respect the boundary, and whether each story's `VP-nn` is one the goal cites, belong to S5.
- The record of a boundary or constraint change caused by the meeting belongs to S7; this segment judges only the format of the fields.

### S5 — User stories and acceptance criteria

**Check:**

- Every story issue, from `gh issue list --repo "$REPO" --label user-story --state all --limit 1000 --json number,title,labels,state,stateReason,createdAt,closedAt,body,url`, or the team's own marker.
- The comments, timeline, and edit history of every story issue, per procedure step 5, to read each story as of the snapshot commit time.
- `docs/product-vision.md`, `docs/research/value-proposition.md`, and `docs/research/gap-analysis.md`, for the chain checks.

**met:**

- At the snapshot commit time there are at least 8 story issues, titled `US-nn: <title>` with unique two-digit identifiers, each carrying `user-story` or the team's marker and exactly one `moscow:*` label or priority field value.
- At least 5 stories are not `moscow:won't`.
- Every story body has the sections the form renders, such as `### Story`, `### Value proposition`, `### Traces to`, `### Rests on`, `### Priority reason`, and `### Acceptance criteria`, showing that it was opened from the form.
- Every statement is a user's need that names the user, the need, and the value, and it carries no design only the team decides, such as a screen, button, component, or library, unless that specific thing is itself the need.
- Every `Value proposition` names exactly one `VP-nn`, linked on `main`, such as `https://github.com/<org>/<repo>/blob/main/docs/research/value-proposition.md#vp-01`.
- The `VP-nn` of every story that is not `Won't Have` is one the vision's goal links.
- Every `Traces to` entry is a linked `GAP-nn` that the story's `VP-nn` lists under `**Closes:**`, a linked `DEC-nnn`, or an action point cited by `reports/week-01/meeting-report.md#action-points` with the action quoted, and every link points at `main`.
- Every `Rests on` entry is a linked `ASM-nn` on `main`.
- Every story that is not `Won't Have` has at least two acceptance criteria, each starting with its `AC-nn`, numbered from `AC-01`, unique within the issue, and observable with a pass or fail answer that somebody else would reproduce.
- Every story has a `Priority reason` that says why it has this priority and not the neighbouring one, that cites the linked `CON-nn` when a constraint drives it, and that does not merely restate the label's definition.
- At least one story the team intends to build is `moscow:should` or `moscow:could`.
- Every `moscow:won't` story is closed as not planned with a comment naming the reason, and a `Won't Have` reason that rests on the boundary cites the linked `BND-nn`.
- No story the team intends to build does a job that an `Active` `BND-nn` excludes.
- Every story the team intends to build is small enough to build and verify in one week, and none is closed as completed.
- The repository keeps no second list of the stories or their criteria.

**partial:**

- At least one story issue existed at the snapshot commit time, and at least one other `met` criterion fails.
- Typical shortfalls: fewer than 8 stories or fewer than 5 intended ones; a story with one criterion; a criterion such as "works well" or "is fast"; a statement that names a screen or a library; a missing or second `moscow:*` label; every intended story `Must Have`; a `Won't Have` story left open; a `GAP-nn` the story's `VP-nn` does not close; a relative link or a link at a commit hash.

**missing:**

- No story issue existed at the snapshot commit time, or none was opened from the form with a `US-nn` title.

**Guardrails:**

- A team may mark stories and priorities with a GitHub issue type or field instead of the labels; filter and read by that marker.
- When two issues were opened with the same `US-nn`, the later one must have taken the next free `US-nn` before any artifact cited it.
- An `ASM-nn` under `Traces to` and a story closed by a pull request are reported in S1 only.
- Comments recording a story change after the meeting belong to S7.
- "Three or four `Must Have` stories, not eight" is a quality note; it is a shortfall only when every intended story is `Must Have`.
- Flag a story as too big for one week only when it plainly bundles several needs.
- A candidate that lists only some of the minimum usable product stories is judged in S6, not here.

### S6 — Minimum usable product candidate

**Check:**

- `## Minimum Usable Product Candidate` in `reports/week-02/README.md` at the snapshot.
- The labels of each listed story as of the snapshot commit time.
- The verdict's entry in `docs/decisions.md`, and `## Decisions` in `reports/week-02/meeting-report.md`.

**met:**

- `reports/week-02/README.md` has a section headed exactly `## Minimum Usable Product Candidate`.
- The section names the core task in one line: one thing a user does from start to finish.
- The section lists the `US-nn` of each story with its issue linked, the list is not empty, and every listed story carries `moscow:must` at the snapshot commit time.
- The listed stories together let a user complete the core task end to end, and removing any one of them breaks the task.
- The section cites the customer's verdict as a `DEC-nnn` linked to `docs/decisions.md#dec-nnn`, whose entry exists, has `**Made by:** Customer`, and has a `**Source:**` that links `reports/week-02/meeting-report.md`.
- The section shows the candidate as it stands after the verdict: a story the verdict dropped is not listed, and it kept its `moscow:*` label unless the customer changed the priority.
- No other file restates the candidate, apart from the meeting script's candidate part written before the meeting.

**partial:**

- The section exists, and at least one other `met` criterion fails.
- Typical shortfalls: no core task; a listed story that is not `Must Have`; stories that cover only part of the core task; a story the task does not need; no verdict `DEC-nnn`; the pre-meeting candidate submitted unchanged after a verdict that changed it.

**missing:**

- `reports/week-02/README.md` has no candidate section, or the candidate it records lists no story.

**Guardrails:**

- Two or three stories is Recommended; a long candidate is a quality note.
- A candidate recorded under a slightly different heading is a shortfall here, not in S9.
- When the verdict entry says `Team, not contested`, record it in `**Evidence:**` and leave it to the instructor rather than counting it as a shortfall.
- The comment that records a priority change on a dropped story belongs to S7.
- The script's candidate part belongs to S8.

### S7 — Prototypes and customer-driven change

**Check:**

- `reports/week-02/prototypes.md` and `reports/week-02/images/` in the snapshot.
- Each `**View:**` link, with one access check per external link, and each linked pull request with `gh pr view <n> --repo "$REPO" --json state,mergedAt,headRefName`.
- The snapshot tree and the merged pull requests, for prototype code on `main`, per procedure step 9.
- The customer-driven change chain, per procedure step 10.
- The comments and edit history of every story issue changed on or after the meeting date.

**met:**

- `reports/week-02/prototypes.md` has at least one section headed by a name for the prototype.
- Every prototype's fields are bulleted in the order `**What it is:**`, `**View:**`, `**Tested:**`, `**Question:**`, `**What the customer said:**`, `**What changed:**`.
- `**View:**` is a screenshot in `reports/week-02/images/` that renders, or a view-only external link that opens, and a code spike is shown by a screenshot and, optionally, a pull request closed without merging rather than a branch link.
- `**Tested:**` names the linked `US-nn` issue or the `GAP-nn` it tested and any `AC-nn` it exercised, and the `ASM-nn` when the risky part is an assumption.
- `**Question:**` is one question whose answer the team could not predict, aimed at the story or assumption the team was least sure of, such as an `Open` assumption.
- `**What the customer said:**` records the customer's reaction, and it agrees with the meeting report.
- No prototype code is on `main` at the snapshot, no spike pull request was merged, and nothing prototype-related is under `docs/`.
- Every published screenshot is sanitized and cropped, showing no personal data, credentials, or unrelated windows.
- One `DEC-nnn` records a change caused by what the customer said about the prototype, its entry's `**Source:**` links `reports/week-02/meeting-report.md`, and the meeting report lists it under `## Decisions`.
- The prototype's `**What changed:**` cites that `DEC-nnn` and says where the change is recorded.
- The changed artifact says something different and cites that `DEC-nnn`: a story issue comment, a `**Changed:**`, `**Why:**`, or `**Dropped:**` field of a `CON-nn` or `BND-nn`, or the `**Outcome:**` of an assumption whose status became `Confirmed` or `Refuted`.
- `reports/week-02/README.md` has one line that names the changed `US-nn`, boundary item, constraint, or `ASM-nn` and what changed in it, linking it and the `DEC-nnn`.
- Every story issue the meeting changed has a comment dated on or after the meeting that says what changed, names each changed `AC-nn`, gives the reason, and links the `DEC-nnn` on `main`, and so does every other change to a story part after the meeting.

**partial:**

- `reports/week-02/prototypes.md` records at least one prototype, and at least one other `met` criterion fails.
- Typical shortfalls: a field missing or out of order; a branch link as the only view; prototype code merged into `main`; a prototype of the part the team was sure about; a decision with no story comment; no README line; a "change" that only confirms the current direction; a change that came from the boundary or candidate discussion rather than from the prototype.

**missing:**

- `reports/week-02/prototypes.md` is absent, or it records no prototype that was shown to the customer.

**Guardrails:**

- A decision that confirms the current direction settles the meeting's target, but it is not the change this segment requires.
- When nothing changed and the team declared it as a deviation, the status is `partial` and the honesty is recorded as a strength; an undeclared absence of change is handled per `docs/grader-policy.md`.
- A change invented only to satisfy the rule, such as a reworded criterion with no link to the customer's reaction, is a shortfall.
- An inaccessible external view is an evidence gap for that view only; the rest of the record is still judged.
- Application code on `main` that is not tied to a prototype is reported here and listed as an ambiguity for the instructor, because Week 2 has no product code.
- Repository tooling is not prototype code: `.github/`, Markdown tool configuration, `package.json` and its lockfile for that tooling, `flake.nix`, a task tracker's directory, and the course-materials submodule.

### S8 — Customer validation meeting

**Check:**

- `reports/week-02/meeting-script.md`, `reports/week-02/meeting-report.md`, and `reports/week-02/meeting-transcript.md` when it exists, in the snapshot.
- `reports/week-01/meeting-report.md`, for the kickoff's `## Action points` and `## Open questions`.
- The path history of the script, to confirm that it was committed before the meeting and not rewritten afterwards.
- Every artifact and task issue an `Outcome` or `Answer` cell links.
- The Moodle PDF's recording line and any transcript appendix, with one access check on the recording link.

**met:**

- The script has exactly the sections `## Context`, `## Agenda`, `## Questions`, `## Roles`, and `## Key improvements`, in that order, with `## Roles` left out only for a meeting held in writing, and an empty section says `None`.
- `## Context` gives the problem-space sentence, what the team believes, and a one-sentence target that covers whether the prototype, the boundary, and the minimum usable product candidate are right.
- `## Agenda` is a numbered list whose first part asks the three permission questions and whose last part reads back the decisions and action points.
- Every agenda part has a timebox, the timeboxes add up to the planned length, every part names what is shown or says that nothing is shown, and every question appears in exactly one part.
- The prototype, the boundary, and the candidate each have their own part, after the previous meeting's open questions and due action points, with the part the team is least sure of first.
- The candidate's part names the core task, lists only the candidate's `US-nn`, each linking its issue, and links the issue list filtered by the `user-story` label.
- `## Questions` is numbered, every question is tagged open or closed, and every question serves the target.
- `## Roles` names a moderator, a note taker, and an observer by GitHub username.
- `## Key improvements` records at least one rewritten question with the before, the after, and the principle.
- The script reached the repository before the meeting date and changed afterwards only by formatting-only changes.
- The report has exactly the sections `## Metadata`, `## Previous action points`, `## Previous open questions`, `## Summary`, `## Decisions`, `## Action points`, `## Open questions`, and `## Disagreements`, in that order, and an empty section says `None`.
- `## Metadata` is a bulleted list, one `- **Label:** value` bullet each, giving the date, the duration, the attendees by GitHub username with the customer as `Customer`, what was presented, the answer to each of the three permission questions, the transcript link or `None` with the reason, and the script link.
- `## Previous action points` has the columns `Action`, `Outcome`, and `Decision`, and one row per kickoff action point due in Week 2 or carried out early.
- Every `Action` cell cites `reports/week-01/meeting-report.md#action-points` with the action quoted, every `Outcome` says whether it was carried out and what was found or why not and links each changed artifact and task issue, and every `Decision` links a `DEC-nnn` or says `None`.
- Every outcome that changes an artifact is visible in that artifact, and every action point not carried out reappears in `## Action points` with a new due week unless the `Outcome` says it was dropped.
- `## Previous open questions` has the columns `Question`, `Answer`, and `Decision`, one row per kickoff open question not yet closed, each citing `reports/week-01/meeting-report.md#open-questions` with the question quoted, and every unanswered question reappears in `## Open questions`.
- `## Summary` has 3 to 5 bullets on what the meeting settled or changed.
- `## Decisions` has at least two bullets of the form `[DEC-nnn: <the entry's first line>](../../docs/decisions.md#dec-nnn)`, one of them the customer's verdict on the candidate, and every linked entry exists with a `**Source:**` that links this report.
- `## Action points` has the columns `Action`, `Owner`, and `Due`, at least two rows, an owner given by GitHub username, and every due date inside Week 3, such as `End of Week 3` or a date from 9 to 15 October 2026.
- `## Open questions` has the columns `Question`, `What it would change`, and `Follow-up`.
- `## Disagreements` has the columns `Your position`, `Customer's position`, and `What you changed`, and every row that changed nothing says why the team kept its position.
- The report is written in English in the team's own words, not a line-by-line restatement of the transcript.
- When the meeting was recorded or held in writing and publication was permitted, `reports/week-02/meeting-transcript.md` exists, opens with `- **Date:**` and `- **Participants:**` bullets, and then has one sentence per line in the form `[hh:mm:ss] <label>: <sentence>`.
- The transcript labels speakers by GitHub username and `Customer`, marks gaps with `[inaudible]` or `[redacted]`, and carries no personal data.
- When publication was refused, no transcript is committed and the Moodle PDF carries it in an appendix.
- The Moodle PDF links a recording that instructors can open, or gives one line saying why there is none, and it agrees with the permission answers in `## Metadata`.
- The meeting took place in Week 2, between 2 October 2026 and the snapshot, the attendees in `## Metadata` include every team member from the PDF's member table, and a meeting held in writing is declared as a deviation.
- Every meeting artifact names the customer `Customer` and identifies people only by GitHub username.

**partial:**

- `reports/week-02/meeting-report.md` exists, and at least one other `met` criterion fails.
- Typical shortfalls: a missing or extra section; no permission part in the agenda; a candidate part that lists every story; fewer than two decisions; no candidate verdict; action points due outside Week 3; a kickoff action point with no row; an outcome recorded only in the table; a script committed after the meeting; a published transcript without permission.

**missing:**

- `reports/week-02/meeting-report.md` is absent at the snapshot, or no Week 2 meeting with the customer took place.

**Guardrails:**

- When the kickoff had no action points due in Week 2 or no open questions, `None` in the matching section is correct.
- Do not re-grade the kickoff script, report, or transcript.
- A later meeting has no per-area question floor, and the planned length is the team's choice.
- An inaccessible recording is an evidence gap for that check only, after the single access check `docs/grader-policy.md` allows.
- Personal data in a meeting artifact is reported here; personal data anywhere else is reported in S9.
- The format of the decision entries belongs to S2, the candidate section to S6, and the customer-driven change chain to S7.

### S9 — Week report and submission

**Check:**

- `reports/week-02/README.md` at the snapshot, and every repository file it links.
- The Moodle PDF, its page count, and its contents.
- The snapshot SHA's position on `main`, and the snapshot commit time, per procedure step 4.
- A privacy scan of the snapshot, per procedure step 12.

**met:**

- `reports/week-02/README.md` is in the snapshot, and every repository file it links is in the same snapshot.
- The report identifies the week, the project, the team, and the covered scope.
- The summary says what the team found, decided, and left open, including what the team found out it was wrong about.
- The coverage table has the 14 rows of `assignment-2.md` (Kickoff action points, Kickoff open questions, Product vision, System context diagram, Assumptions, Decisions, Story issues, Issue forms, Labels, Pull request template, Prototypes, Meeting script, Customer validation, AI usage).
- Every coverage cell links its artifact: a repository file with its path from the repository root as the link text, with the heading anchor when the row names a section, and anything else, such as the filtered story list or the labels page, with descriptive link text.
- When the customer refused publication of the transcript, the Customer validation row says so and points at the Moodle submission.
- No second list of the same links follows the coverage table.
- A contribution table maps each member's GitHub username to the work done, with links to commits, pull requests, or reviews.
- The repository evidence links one merged pull request that closed its task issue, the latest green link-check run, and the latest green Markdown check run on `main`.
- Every link the link check excludes is justified in prose.
- `## Deviations` declares every deviation observed in the other segments, or says `None` when there is none.
- One line states that no private-only material was committed to the repository.
- The privacy scan finds no private-only material in the snapshot outside the meeting artifacts.
- The snapshot SHA is on `main`, and the PDF permalink points at `reports/week-02/README.md` at that full 40-character SHA.
- The PDF is at most two pages, not counting a transcript appendix, and holds only the six items of `assignment-2.md`: the project name and team number, the member table, the permalink, the recording line, the transcript when publication was refused, and the privacy confirmation line.

**partial:**

- `reports/week-02/README.md` exists at the snapshot, and at least one other `met` criterion fails.
- Typical shortfalls: a coverage row missing or not linked; no statement of what the team was wrong about; no contribution table; repository evidence missing a run or the pull request; no `## Deviations`; an undeclared deviation; a seven-character permalink; a snapshot that is not on `main`; a PDF over two pages or with extra content.

**missing:**

- `reports/week-02/README.md` is absent at the snapshot.

**Guardrails:**

- A coverage row whose artifact is absent is a shortfall in the segment that owns the artifact; here the shortfall is only a missing row or a row that does not link.
- The candidate section is judged in S6 and the one-line change statement in S7, so neither needs a coverage row.
- Record the snapshot commit date against the deadlines in `**Evidence:**`, and never change a status for lateness.
- Report a privacy finding by path and kind, such as "a personal email address in `docs/product-vision.md`", never by value, and match real names from the PDF without copying them.
- The root `README.md` link to the current week's report is a Week 1 artifact and is only noted.

### S10 — AI usage and research honesty

**Check:**

- `reports/week-02/ai-usage.md` in the snapshot.
- Traces of AI tools: `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.agents/`, `.opencode/`, `opencode.json`, `.github/copilot-instructions.md`, `.cursor/`, and the `Co-Authored-By:` trailers and "Generated with" lines in Week 2 commit messages and pull request bodies.
- The prose added or changed in Week 2: the vision, the story issues, `prototypes.md`, the README, and the `**Changed:**`, `**Dropped:**`, and `**Confidence:**` fields added to `docs/research/`.

**met:**

- `reports/week-02/ai-usage.md` names each tool and what it was used for, and says what the team did with the output: what it accepted, changed, and rejected, and why.
- Alternatively, the file states in one line that no AI tools were used, and nothing in the repository or its history contradicts it.
- The disclosure agrees with the traces of AI tools in the repository, the commit messages, and the pull request bodies.
- The Week 2 prose has no filler, meaning no template sentence without a product name, an identifier, or a date, and no unchecked generated text, such as leftover `<org>` or `<repo>` placeholders, identifiers that point nowhere, or claims that contradict the team's own artifacts.
- Research text added or changed in Week 2 separates what was observed from what was inferred, states its confidence when the evidence is thin, and traces each claim to something the team looked at.

**partial:**

- `reports/week-02/ai-usage.md` exists, and at least one other `met` criterion fails.
- Typical shortfalls: tools named without saying what happened to their output; agent traces or co-author trailers with no disclosure; template sentences or placeholders in a Week 2 artifact; a new `**Changed:**` bullet with no evidence behind it.

**missing:**

- `reports/week-02/ai-usage.md` is absent at the snapshot.

**Guardrails:**

- Using AI tools is allowed and is never a shortfall by itself.
- The course-materials submodule alone does not prove agent use; count it as undisclosed use only when other traces show agent output.
- The meeting report's own-words rule belongs to S8.
- Week 1 text left unchanged is not re-judged.

## Assignment-specific procedure deltas

1. Take the team set from the directory names under `itpd-assignments-feedback/A2/submissions/`.
2. Read the Moodle PDF, preferring the one that carries the commit-hash permalink when there are several, and extract:

   - the project name and the team number;
   - the GitHub usernames of the member table, keeping real names and emails only in working memory for the privacy match;
   - the permalink to `reports/week-02/README.md`, with its organization, repository, and full SHA;
   - the recording link or the line saying why there is none;
   - whether a transcript appendix is present;
   - the privacy confirmation line;
   - the page count, for example from `pdfinfo`, and anything outside the six allowed items.

3. Resolve the snapshot per `docs/grader-policy.md`, and fetch it from GitHub into `itpd-assignments-feedback/A2/work/<team_dir>/` when that directory is empty.
4. Set `REPO=<org>/<repo>` and `SHA=<full SHA>`, then read the snapshot commit time and check that the commit is on `main`:

   ```sh
   gh api "repos/$REPO/commits/$SHA" --jq '.commit.committer.date'
   gh api "repos/$REPO/compare/$SHA...main" --jq '.status'
   ```

   A status of `identical` or `ahead` puts the commit on `main`; `behind` or `diverged` does not, which is an S9 shortfall.
   Call the first value `SNAPSHOT_TIME`.

5. Collect the live evidence once and keep it beside, not inside, the fetched snapshot:

   ```sh
   gh label list --repo "$REPO" --limit 200 --json name,description
   gh issue list --repo "$REPO" --state all --limit 1000 \
     --json number,title,labels,state,stateReason,createdAt,closedAt,body,url,author,closedByPullRequestsReferences
   gh pr list --repo "$REPO" --state all --limit 500 \
     --json number,title,author,headRefName,baseRefName,state,createdAt,mergedAt,closedAt,body,closingIssuesReferences,reviews,files,url
   gh run list --repo "$REPO" --branch main --limit 100 \
     --json databaseId,workflowName,headSha,event,status,conclusion,createdAt,url
   gh api "repos/$REPO/actions/runs?head_sha=$SHA" \
     --jq '.workflow_runs[] | [.name, .event, .conclusion, .html_url] | @tsv'
   ```

   For each story issue and each task issue a check needs, read its comments, its timeline of label, rename, and close events, and its body edit history:

   ```sh
   gh api "repos/$REPO/issues/<n>/comments" --paginate
   gh api "repos/$REPO/issues/<n>/timeline" --paginate
   gh api graphql -F owner='<org>' -F name='<repo>' -F n=<n> -f query='
     query($owner: String!, $name: String!, $n: Int!) {
       repository(owner: $owner, name: $name) {
         issue(number: $n) { lastEditedAt userContentEdits(first: 100) { nodes { editedAt diff } } }
       }
     }'
   ```

   For the history of a repository path and the pull request behind each commit:

   ```sh
   gh api "repos/$REPO/commits?sha=$SHA&path=<path>&per_page=100" \
     --jq '.[] | [.sha, .commit.committer.date, (.commit.message | split("\n")[0])] | @tsv'
   gh api "repos/$REPO/commits/<commit>/pulls" --jq '.[] | [.number, .title, .merged_at] | @tsv'
   gh pr diff <n> --repo "$REPO"
   ```

6. Judge every issue as of `SNAPSHOT_TIME`:

   - Count only issues whose `createdAt` is at or before `SNAPSHOT_TIME`, and note any story opened later as a caveat in S5 `**Evidence:**`.
   - Take an issue's labels at `SNAPSHOT_TIME` from its timeline's `labeled` and `unlabeled` events, its title from `renamed` events, and its open or closed state and close reason from `closed` and `reopened` events.
   - Take its body from the last edit at or before `SNAPSHOT_TIME` when the edit history allows it; otherwise judge the current body and say so in `**Evidence:**`.
   - A comment or edit made after `SNAPSHOT_TIME` is a caveat, never a shortfall.
   - Set `Evidence gaps: yes` only when the state at `SNAPSHOT_TIME` cannot be read and the difference could change the status.

7. Identify the forms pull request as the pull request behind the earliest commit that added `.github/ISSUE_TEMPLATE/user-story.yml`.
   The in-scope pull requests for S1 run from its creation to `SNAPSHOT_TIME`, without Dependabot pull requests and pull requests a workflow opened.
   Check that no pull request touching a Week 2 artifact was merged before it.
8. For each in-scope pull request, check the task workflow:

   ```sh
   gh pr list --repo "$REPO" --state all --limit 500 \
     --json number,headRefName,author,state,mergedAt,closingIssuesReferences,reviews \
     --jq '.[] | {n: .number, branch: .headRefName, author: .author.login, state, merged: .mergedAt,
                  closes: [.closingIssuesReferences[].number],
                  approvers: [.reviews[] | select(.state == "APPROVED") | .author.login] | unique}'
   ```

   - `closes` has exactly one number, and that issue carries `task` and not `user-story`.
   - `branch` matches `^<that number>-[a-z0-9]+(-[a-z0-9]+)*$`.
   - A merged pull request has an approver other than its author, its task's body has every criterion as `- [x] AC-nn:`, and the task's `stateReason` is `COMPLETED`.
   - A pull request closed without merging left its task `NOT_PLANNED` with a comment that gives the reason and links the pull request.

9. Check that no prototype code is on `main`:

   - List application source in the snapshot, for example with `find . -type f \( -name '*.py' -o -name '*.js' -o -name '*.ts' -o -name '*.tsx' -o -name '*.jsx' -o -name '*.go' -o -name '*.java' -o -name '*.kt' -o -name '*.dart' -o -name '*.swift' -o -name '*.vue' \) -not -path './.github/*' -not -path './.agents/*' -not -path './node_modules/*'`, and look for directories such as `src/`, `app/`, `prototype/`, or `spike/`.
   - Search the merged pull requests for a spike by title, branch, or files, using the `files` field from step 5.
   - Confirm that every pull request a `**View:**` field links is `CLOSED` with an empty `mergedAt`.

10. Check the customer-driven change chain, starting from the README's one-line change statement:

    - Find the `DEC-nnn` it links in `docs/decisions.md`, and confirm that its `**Source:**` links `reports/week-02/meeting-report.md` and its date is the meeting date.
    - Confirm that `## Decisions` of the meeting report lists it, and that a `## Disagreements` row or the prototype's `**What the customer said:**` shows the customer's reaction behind it.
    - Confirm that the prototype's `**What changed:**` cites it.
    - Confirm that the changed artifact cites it and now says something different: for a story, a comment dated on or after the meeting plus a body or label change in the edit history or timeline; for a `BND-nn` or `CON-nn`, the `**Changed:**`, `**Why:**`, or `**Dropped:**` field; for an `ASM-nn`, the `**Outcome:**` with a `Confirmed` or `Refuted` status.
    - Search the snapshot and the story issues for the `DEC-nnn`, so that a decision nothing cites is visible.

11. Check the ordering rules from the merge times and creation times collected in step 5:

    - The forms pull request was merged before every other Week 2 pull request.
    - The formatting-only pull request was merged before the pull request that added the Markdown workflow.
    - The research-heading pull request was merged before the first story issue that links a `VP-nn` was opened.
    - The decisions and assumptions migrations were merged before the first story issue that links a `DEC-nnn` or an `ASM-nn` was opened.
    - The script's first commit predates the meeting date in `## Metadata`, and no later commit changed its words.

12. Scan the snapshot for private-only material: email addresses with `grep -rnE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'`, phone numbers, the real names from the PDF member table, recording links in meeting files, and `.env` files.
    Report each finding by path and kind only.
13. Make one access check per external prototype view and on the recording link, per `docs/grader-policy.md`.
14. Grade each of the 10 segments independently, and report each shortfall only in the segment that owns it in the [segment overview](#segment-overview).

## Assignment-specific constraints

- The `Primary index reviewed` metadata bullet points to `reports/week-02/README.md` at the snapshot whenever the snapshot is inspectable.
- Moodle-only items are judged from the PDF, and their absence from the repository is correct: the member table with real names and university emails, the recording link, and a transcript the customer refused to publish.
- Never copy a real name or an email from the PDF into feedback; refer to people by GitHub username.
- A recording or external view that fails its single access check is an evidence gap for that check only, and the surrounding evidence is still judged.
- A transcript appendix does not count toward the PDF's two pages.
- Week 1 artifacts are not re-graded: repository setup, `LICENSE`, the root `README.md`, branch protection settings, the Week 1 pull request evidence, the link-check configuration, Dependabot, the Week 1 research content, and the kickoff script, report, and transcript.
- Week 1 artifacts are checked only where Assignment 2 requires it: the link check green on `main` (S3), the Week 1 decisions and assumptions migrated (S2), the research entries in the Week 2 format and Week 1 reports changed only by formatting-only changes (S3), the kickoff action points and open questions closed (S8), and the pull request template linking the task issue (S1).
- When a Week 1 artifact that Assignment 2 builds on is absent, such as a kickoff report with no action points, judge the Assignment 2 item against what exists and do not report the Week 1 absence again.
- The one-time catch-ups in Parts 1–4 are judged by their end state when a team already met the newer rule in Week 1.
- Week 2 has no product code and no product CI, so neither is expected.
- The course-materials submodule is Recommended; excluding its directory from both checks is allowed, and its absence is never a shortfall.
- Use the course's terminology in feedback: `Customer` for the person the team answers to, story issue, task issue, meeting report, meeting script, and minimum usable product candidate.
