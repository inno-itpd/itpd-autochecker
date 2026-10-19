# Assignment 3 Grading Criteria

This rubric is for an LLM grading agent that reviews ITPD Assignment 3 team submissions.
ITPD assigns no points: each segment gets one status, `met`, `partial`, `missing`, or `unverified`, and an `Evidence gaps: yes|no` flag, per `docs/grading-feedback-format.md`.
The instructor assigns the grade from the statuses and the evidence, so this rubric never proposes a grade, a score, or a late penalty.
The shared rules live in `docs/grader-policy.md`: evidence states, verified absence, blocked and conflicting artifacts, snapshot resolution, live GitHub evidence through `gh api`, the single access check for consumer-hosted media, privacy, undeclared deviations, and rule applicability by `Since:` marker.
This file states only what is specific to Assignment 3 and does not repeat those rules.

## Authoritative sources

All paths are in the course-materials submodule, pinned at itpd commit `23b22a6d637c0ac9c6a3350b377ae333cb42a082`.
If the checked-out submodule differs from that commit, read each file with `git -C A3/itpd show 23b22a6d637c0ac9c6a3350b377ae333cb42a082:<path>`.

- `A3/itpd/assignments/assignment-3.md` — the student-facing brief: Parts 1–10, What Good Looks Like, the repository report contents, the Moodle PDF contents, the submission procedure, and the checklist.
- `A3/itpd/requirements/general-requirements.md` — where artifacts live, the identifier rules for `TOS-nn`, `RISK-nn`, `SPRINT-nn`, `MLS-nn`, and `REL-nn`, and traceability into later weeks.
- `A3/itpd/requirements/planning-requirements.md` — the plan and the threshold: where each lives, `docs/project-plan.md` with `## Milestones`, `## Sprints`, and `## Progress Monitoring`, the seven sprints and their `REL-nn`, `docs/threshold-of-success.md` with its `TOS-nn` sections and the statements table.
- `A3/itpd/requirements/risks-requirements.md` — the register, the summary table, the risk sentence, its fields, the ratings, the response, and checking and settling.
- `A3/itpd/requirements/definition-of-done-requirements.md` — `docs/definition-of-done.md` and its three sections.
- `A3/itpd/requirements/issue-tracking-requirements.md` — opening issues, linking a file from an issue, the `Responsible` and `Accountable` issue fields, scheduling with the sprint's GitHub milestone, the assignees, and the public GitHub project.
- `A3/itpd/requirements/pull-requests-requirements.md` — how a change gets in, the reviewer, the checks before a merge, and the pull request template.
- `A3/itpd/requirements/task-issues-requirements.md` — task issues, the `Story` field, task acceptance criteria, and closing a task.
- `A3/itpd/requirements/user-stories-requirements.md` — stories, acceptance criteria, MoSCoW priorities, where stories live, and the `Responsible` and `Accountable` values on a story.
- `A3/itpd/requirements/minimum-usable-product-requirements.md` — where the candidate lives, the candidate, and building, delivering, and releasing it.
- `A3/itpd/requirements/customer-meetings-requirements.md` — every meeting, showing working software, the permission questions, the script, the report, and the transcript.
- `A3/itpd/requirements/decisions-requirements.md` — the decision entry, its fields, what cites it, and reversing it.
- `A3/itpd/requirements/assumptions-requirements.md` — the assumption entry, so that an action point's outcome carried into an `ASM-nn` can be read.
- `A3/itpd/requirements/releases-requirements.md` — where the changelog lives, its format, versioning and tags, and cutting a release.
- `A3/itpd/requirements/repository-requirements.md` — the root README, setup and run instructions, the documentation site, contributing, continuous integration, action pinning, permalinks and snapshots, and configuration.
- `A3/itpd/requirements/visibility-requirements.md` — what is public, what is Moodle only, and screenshot sanitization.
- `A3/itpd/requirements/weekly-report-requirements.md` — the weekly public report, the AI usage report, declaring deviations, and the Moodle PDF.
- `A3/itpd/course/rules.md` — the course contract, the AI policy, the deadline pair, and the submission channel.
- `A3/itpd/course/syllabus.md` — the Week 3 deliverables and minima, and the Week 3 hard deadline.
- `A3/itpd/guides/planning-and-tracking.md`, `A3/itpd/guides/validating-with-the-customer.md`, and `A3/itpd/guides/user-stories-and-prototyping.md` — the method, used to judge quality and never as extra requirements.
- `A3/itpd/AGENTS.md` — course terminology and the `docs/` destination map for Week 3.

Apply every rule marked `**Since: W1**`, `**Since: W2**`, or `**Since: W3**`.
These `**Since: W4**` rules do not apply: product-code CI, the Definition of Done item that names it, the in-repository tracker's Week 4 rules, and the Week 4 architecture, quality, and testing items.

## Assignment parameters

- Report title: `# Assignment 3 Feedback Report`
- Week: `W3`
- Course materials: `A3/itpd` at `23b22a6d637c0ac9c6a3350b377ae333cb42a082`
- Primary index artifact: `reports/week-03/README.md` at the snapshot, as named in Assignment Report In The Repository and in Moodle item 3 of `assignment-3.md`.
- Soft deadline: Thursday 15 October 2026, 23:59.
- Hard deadline: Saturday 17 October 2026, 23:59, as `course/syllabus.md` and `assignments/assignment-3.md` state it.
- Hard deadline of the following week: Friday 23 October 2026, 23:59, the date the Week 4 syllabus block gives `REL-04`, and the date a plan milestone due in Week 4 is judged against.
- The time zone is not stated; read every deadline as Innopolis time (UTC+3).
- Submission inputs: the Moodle PDF under `itpd-assignments-feedback/A3/submissions/<team_dir>/`; there is no ZIP.
  The snapshot is fetched from GitHub at the permalink SHA into `itpd-assignments-feedback/A3/work/<team_dir>/snapshot/`.
- Live artifact families: story and task issues with their comments, timelines, and edit history; repository labels; the organization's issue fields; pull requests with their reviews, files, and closing references; Actions runs of the Markdown check, the link check, and the Pages deployment; the repository's tags and releases; the seven sprint GitHub milestones; the organization's GitHub project; the published documentation site; and the meeting recording link.
- Story and task issues, their milestones, and their issue-field values are not in the snapshot, so they are read live and judged as of the hard deadline, `2026-10-17T23:59:59+03:00` (`ISSUE_CUTOFF`), per [procedure step 6](#assignment-specific-procedure-deltas).
  An issue opened after the snapshot commit but by the hard deadline counts.
- Tags, releases, milestones, the GitHub project, and the documentation site are read live and judged as of the hard deadline too.
  An issue-field value has no history in the API: read the current value and read the issue's timeline for what changed after the hard deadline, and say so in `**Evidence:**` when the timeline cannot settle it.

The segments, in order:

- S1: Threshold of success
- S2: Project plan and sprint milestones
- S3: Risk register
- S4: Stack decision and dependencies
- S5: Definition of Done and contributing guide
- S6: Issue fields and GitHub project
- S7: Minimum usable product on main
- S8: Documentation site and setup page
- S9: Week 2 action points and open questions
- S10: Customer validation of the working software
- S11: Changelog and first release
- S12: Week report and submission
- S13: AI usage and honesty

### Segment overview

Every checklist item and every coverage-table row of `assignment-3.md` maps to exactly one segment, and a shortfall is reported only in the segment that owns it.

| Segment | Covers |
|---------|--------|
| S1: Threshold of success | Part 1; checklist items "`docs/threshold-of-success.md` with 3+ goals, each with its fields, and the failure and success statements below them" and "The vision's goal links the threshold"; coverage row Threshold of success |
| S2: Project plan and sprint milestones | Part 2; checklist items "`docs/project-plan.md` with `## Milestones`, `## Sprints`, and `## Progress Monitoring`" and "The seven `SPRINT-nn` GitHub milestones created, each with its focus and due date, and the plan's `**Sprints:**` runs disjoint and consecutive"; coverage rows Project plan and Sprint milestones and issue fields (the milestone part) |
| S3: Risk register | Part 2's risk rules; checklist item "`docs/risks.md` with 3+ risks and the summary table"; coverage row Risk register |
| S4: Stack decision and dependencies | Part 3; checklist item "The stack recorded as a `DEC-nnn`, `.gitignore` extended, and the stack's ecosystem added to `.github/dependabot.yml`"; coverage row Stack decision |
| S5: Definition of Done and contributing guide | Part 4's first two items; checklist item "`docs/definition-of-done.md` and `CONTRIBUTING.md`"; coverage rows Definition of Done and Contributing guide |
| S6: Issue fields and GitHub project | Part 4's last three items; checklist items "The `Responsible` and `Accountable` fields created and `Public`", "The public GitHub project with its table view", and "Every issue the plan schedules is in its sprint's GitHub milestone, carries the two values, and has both members as assignees"; coverage rows Sprint milestones and issue fields (the fields and values part) and GitHub project |
| S7: Minimum usable product on main | Part 5; checklist item "Every candidate story built into `main` through task issues and pull requests, and shown at the meeting or moved out by the customer's decision"; coverage row Minimum usable product |
| S8: Documentation site and setup page | Part 6; checklist items "The docs site published and linked, and `docs/setup.md` linked from the root README" and "`docs/setup.md`"; coverage rows Documentation site and Setup and run instructions |
| S9: Week 2 action points and open questions | Part 7; checklist items "Each Week 2 action point's outcome in `## Previous action points`, and in the artifact it changed" and "Each Week 2 open question answered or carried forward in `## Previous open questions`"; coverage rows Week 2 action points and Week 2 open questions |
| S10: Customer validation of the working software | Part 8, apart from the action points and open questions S9 owns; checklist items "`reports/week-03/meeting-script.md`", "`reports/week-03/meeting-report.md`, with a `DEC-nnn` for each story shown and each story that moved out, and 2+ action points due in Week 4", and "`reports/week-03/meeting-transcript.md`, if the meeting was recorded or held in writing"; coverage rows Meeting script and Customer validation; Moodle items 4 and 5 |
| S11: Changelog and first release | Part 9; checklist item "The first release tagged, and the changelog's released section, the plan's `REL-03` line, and `reports/week-03/README.md` merged after the tag"; coverage row Changelog and first release |
| S12: Week report and submission | Assignment Report In The Repository items 1, 2, 4, and 5 and the Weekly Public Report rules, apart from the release and the meeting outcome S10 and S11 own; Moodle items 1, 2, 3, and 6; the Submission Procedure; checklist items "`reports/week-03/README.md`", "Everything merged into `main`, with the permalink and the snapshot taken from that commit", and "PDF ready, and the permalink opened in a browser at the full commit hash"; coverage table as an index |
| S13: AI usage and honesty | Part 10; checklist item "`reports/week-03/ai-usage.md`"; coverage row AI usage; the AI Usage Report rules for Week 3 text |

The coverage-table rows map to the segment that judges the artifact in the row.
Whether the table has each row, and whether each row links, is judged in S12.

## Status guide

Use the status vocabulary of `docs/grading-feedback-format.md` and the evidence states of `docs/grader-policy.md`.
A segment is `met` only when every `met` criterion below holds on verified evidence.
A segment is `partial` when its core artifact exists and at least one verified shortfall remains.
A segment is `missing` when the `missing` criterion below holds.
A segment is `unverified` when its core evidence could not be read, such as S7 when the repository's pull requests cannot be read at all, or S6 when neither the per-issue field values nor the project can be read and nothing else settles them.
Recommended items and the What Good Looks Like points are quality notes for the instructor, and they never cause a shortfall unless they coincide with a Required rule.

### S1 — Threshold of success

**Check:**

- `docs/threshold-of-success.md` and `docs/product-vision.md` in the snapshot.
- Every `DEC-nnn` a goal's `**Changed:**` or `**Dropped:**` cites, in `docs/decisions.md` and in `reports/week-03/meeting-report.md`.
- The rendered permalink `https://github.com/<org>/<repo>/blob/<sha>/docs/threshold-of-success.md`, for the statements table's rendering.

**met:**

- `docs/threshold-of-success.md` holds at least 3 `## TOS-nn` sections, in identifier order, with three digits or two as the team numbered them, and every identifier unique.
- Each `## TOS-nn` heading is the bare identifier, and the goal's first line states it in one sentence as a result its `**Measure:**` can settle.
- Each goal's fields are a bulleted list in the order `**Status:**`, `**Measure:**`, then `**Outcome:**` only on `Achieved` or `Missed`, `**Changed:**` only while `Open`, and `**Dropped:**` only on a dropped goal.
- Every `**Status:**` is `Open`, `Achieved`, `Missed`, or `Dropped`; every `**Measure:**` names the evidence or the number and the week it lands in.
- Every `Achieved` or `Missed` goal carries an `**Outcome:**` that says what was found and links the evidence and any `DEC-nnn`.
- Every change to an `Open` goal's text, including a date, sits as one bullet under `**Changed:**` and cites the customer's `DEC-nnn`, and that entry in `docs/decisions.md` exists with `**Made by:** Customer` or `Team, not contested`.
- A goal added later has a first `**Changed:**` bullet saying it was added and citing the customer's `DEC-nnn`; a `Dropped` goal's `**Dropped:**` gives the date, the reason, and the customer's `DEC-nnn`.
- Below the goals, `## Failure And Success Statements` holds one table with the columns `Goal`, `Success statement`, and `Failure statement`, in that order, rows grouped by their first goal in `TOS-nn` order with the rows no goal covers last.
- Every `Goal` cell links its goal as `[TOS-nn](#tos-nn)` or `—`, every row is one failure statement with its conversion, and every `TOS-nn` is linked from at least one row.
- The failure statement's wording is the session's and is never judged; only the table's shape and its tracing are.
- `docs/product-vision.md` states its goal in one sentence in `## Goal` and links `docs/threshold-of-success.md` from that section.
- The goal's link to the threshold is one-way: a threshold that links the vision's goal in prose is a quality note, and a milestone reaches the threshold through `**Advances:**`, per [Milestones](../A3/itpd/requirements/planning-requirements.md#milestones).

**partial:**

- `docs/threshold-of-success.md` exists with `TOS-nn` sections, and at least one other `met` criterion fails.
- Typical shortfalls: fewer than 3 goals; a titled heading; fields as a table or a paragraph; a `**Changed:**` bullet with no `DEC-nnn`; a bar moved without the customer; a statements table with the columns out of order, fewer columns, or rows rewritten; a goal no row traces to; a vision goal that does not link the threshold.

**missing:**

- `docs/threshold-of-success.md` is absent at the snapshot, or it holds no `## TOS-nn` section.

**Guardrails:**

- "A threshold that could fail" is a quality note: record a goal nobody could miss in `**Evidence:**` for the instructor, and name the goal.
- 3 to 5 goals is Recommended; more than 5 is a quality note, and fewer than 3 is the shortfall.
- Do not re-grade the Week 2 product vision content; judge only the goal's one sentence and its link to the threshold.

### S2 — Project plan and sprint milestones

**Check:**

- `docs/project-plan.md` and `docs/threshold-of-success.md` in the snapshot.
- The repository's GitHub milestones, from `gh api "repos/$REPO/milestones?state=all&per_page=100"`.
- The path history of `docs/project-plan.md`, for when each sprint's section was written.
- The pull requests in the Week 3 window that touch `docs/project-plan.md`.

**met:**

- `docs/project-plan.md` has the parts `## Milestones`, then `## Sprints`, then `## Progress Monitoring`, in that order, and those three only, plus the title and any prose between them.
- `## Milestones` holds `### MLS-03` with its focus delivering the MUP, and any further milestone is numbered by its due week with a gap where no week has one.
- Each `### MLS-nn` section is headed by the bare identifier, its fields are bulleted in the order `**Due:**`, `**Sprints:**`, `**Advances:**`, and a description follows them.
- `**Due:**` is the hard deadline of the due week as `course/syllabus.md` gives it, such as `2026-10-17` for `MLS-03`; `**Sprints:**` links a consecutive run of `SPRINT-nn` sections, one or more; `**Advances:**` links at least one `TOS-nn` that exists in `docs/threshold-of-success.md`.
- The description's first sentence states what the increment delivers, and it does not restate `**Sprints:**` or `**Advances:**`; `MLS-03`'s first sentence states the Week 2 candidate's core task.
- The `**Sprints:**` runs of all milestones are disjoint, and each run ends in the week its milestone is due.
- `## Sprints` holds `### SPRINT-03` to `### SPRINT-09`, in order, each a bare heading.
- Each `### SPRINT-nn` section opens with the sprint's goal in one sentence, stated as a result and not as a list of tasks; a sprint not yet planned states a provisional goal.
- Under the goal, each `### SPRINT-nn` carries `**Due:**` with the hard deadline of its week, and `**Sprint Backlog:**` linking the sprint's GitHub milestone once the sprint has issues.
- `SPRINT-03` and `SPRINT-04` have concrete goals, and every later sprint has a goal.
- Each `### SPRINT-nn` nests exactly one `#### REL-nn` heading, `REL-03` to `REL-09` in order, and a release section stays empty until the release is published.
- Every one of the seven `SPRINT-nn` GitHub milestones exists, titled `SPRINT-nn: <focus>` with the sprint's number, open or closed as its week requires, and its due date equal to the hard deadline of its week, `2026-10-17` for `SPRINT-03` up to the Week 9 hard deadline for `SPRINT-09`.
- The plan's milestones are not GitHub milestones, and no GitHub milestone stands for a plan milestone.
- `## Progress Monitoring` is last, is a bulleted list of `- **Label:** value` bullets, and names when the team's weekly review is held, who checks, and where progress is visible: the GitHub project's table view and the sprints' GitHub milestones.
- `## Progress Monitoring` links `docs/risks.md` exactly once, and `docs/project-plan.md` carries no contingency section.
- The plan copies no issue list into the file.

**partial:**

- `docs/project-plan.md` exists with `## Milestones` and `## Sprints`, and at least one other `met` criterion fails.
- Typical shortfalls: the three parts out of order or a fourth part added; no `MLS-03`; a milestone numbered by its week when its due week differs; `**Sprints:**` runs that overlap or do not end in the milestone's week; a sprint whose goal reads as a task list; a missing `REL-nn` or two releases on one sprint; a missing sprint milestone; a milestone due date that is not the week's hard deadline; `## Progress Monitoring` without the three items; `risks.md` linked twice or not at all.

**missing:**

- `docs/project-plan.md` is absent at the snapshot, or it has no `## Sprints` section with `SPRINT-nn` sections.

**Guardrails:**

- A milestone due date is judged against `course/syllabus.md`, which is authoritative: its table dates are the Thursday soft deadlines, each hard deadline is the following Friday at 23:59, and Weeks 2 and 3 are the Saturday exceptions.
- The hard deadlines for `SPRINT-03` to `SPRINT-09` are `2026-10-17`, `2026-10-23`, `2026-10-30`, `2026-11-06`, `2026-11-13`, `2026-11-20`, and `2026-11-27`, the same dates applying to a plan milestone due in that week.
- A closed GitHub milestone is a strength when its release was cut and its leftover issues moved on, and never a shortfall.
- Further plan milestones are the team's choice; their absence beyond `MLS-03` is never a shortfall, and "plan milestones as increments, not weeks" is a quality note.
- Whether an issue carries its milestone and the two values belongs to S6, and whether `**Sprint Backlog:**` resolves belongs to [procedure step 13](#assignment-specific-procedure-deltas), reported here.
- A sprint section written after the sprint started is a caveat in `**Evidence:**`, never a shortfall, unless the goal was plainly written from what happened; say what the evidence shows.

### S3 — Risk register

**Check:**

- `docs/risks.md` and `docs/project-plan.md` in the snapshot.
- Every `TOS-nn`, `DEC-nnn`, and `SPRINT-nn` a risk cites.
- The pull requests in the Week 3 window that touch `docs/risks.md`, for a settled risk's date.

**met:**

- `docs/risks.md` holds at least 3 `## RISK-nn` sections in identifier order, each headed by the bare identifier.
- The register opens with a summary table above the first `## RISK-nn` section, with the columns `ID`, `Status`, `Impact`, `Likelihood`, and `Risk`, in that order, each `ID` linked to its section such as `[RISK-02](#risk-02)`, each `Status` and rating matching the section, and each `Risk` quoting the section's first line.
- The table lists the `Open` risks first, sorted by `Impact` then `Likelihood`, both `High` to `Low`, then the settled risks in identifier order, with ties in identifier order.
- Each risk's first line is one sentence stating the cause that sets it off, the event it may trigger, and the impact of that event.
- Each risk's fields are bulleted in the order `**Status:**`, `**Impact:**`, `**Likelihood:**`, `**Trigger:**`, `**Window:**`, `**Mitigation:**`, `**Contingency:**`, then `**Outcome:**` only on `Mitigated` or `Realized` and `**Dropped:**` only on `Dropped`.
- Every `**Status:**` is `Open`, `Mitigated`, `Realized`, or `Dropped`.
- `**Impact:**` and `**Likelihood:**` each carry `High`, `Medium`, or `Low` directly after the field name, with one colon, and the reason follows on a nested bullet under the rating.
- `**Trigger:**` names something the review can observe rather than infer, and `**Window:**` names a date, a week, a sprint, or a plan milestone.
- `**Mitigation:**` says what the team does before the risk happens, and `**Contingency:**` is one alternative solution with no choice left open in it.
- Each risk threatens the plan or the threshold, so a reader can see what it costs the team if it happens.
- A `Mitigated` or `Realized` risk's `**Outcome:**` says what was done or what happened and links the evidence and any `DEC-nnn`; a `Dropped` risk's `**Dropped:**` gives the date and the reason.
- When a mitigation or a contingency passes a point of no return, it cites the `DEC-nnn` that records it.

**partial:**

- `docs/risks.md` exists with `RISK-nn` sections, and at least one other `met` criterion fails.
- Typical shortfalls: a missing summary table, a column out of order, or a summary table that sits below the first `## RISK-nn` section or after the risk sections; open risks not sorted by rating; a first line that states only a worry, with no cause, event, or impact; a rating word spelled into the reason so the bullet has two colons; a `**Trigger:**` nobody could watch; a contingency that offers two options; a settled risk with no `**Outcome:**`.

**missing:**

- `docs/risks.md` is absent at the snapshot, or it holds no `## RISK-nn` section.

**Guardrails:**

- "Risks you would act on", with a trigger the review can watch and a fallback decided beforehand, is the quality bar: note a risk whose rating contradicts its reason, or whose trigger is a feeling, in `**Evidence:**`.
- Week 3 is early, so every risk is usually `Open`; a register that settles a risk is not judged on the settlement's timing.
- An assumption mistaken for a risk, or the reverse, is reported here when the entry states a belief to check rather than an event to watch.
- The plan's Progress Monitoring links the register, and that link belongs to S2.

### S4 — Stack decision and dependencies

**Check:**

- `docs/decisions.md`, `.gitignore`, `.github/dependabot.yml`, and the product's dependency manifest and lockfile in the snapshot.
- The path history of `.gitignore`, `.github/dependabot.yml`, and the manifest, and the pull requests behind each change.
- The Actions runs on `main` at or before the snapshot commit time.

**met:**

- `docs/decisions.md` holds one `DEC-nnn` entry that records the stack the MUP is built with, with the stack named in its first line, and the entry carries `**Why:**`.
- The entry's fields are bulleted in the order `**Status:**`, `**Date:**`, `**Made by:**`, `**Source:**`, `**Why:**`, and `**Made by:**` is `Customer`, `Team`, or `Team, not contested`.
- The stack the entry names is the stack the product code uses in the snapshot: a manifest and a lockfile for that stack exist, or the stack needs neither and the code shows it.
- `.gitignore` covers the chosen stack's usual local artifacts, such as `node_modules/`, `.venv/`, `__pycache__/`, `target/`, `build/`, or `dist/`.
- `.github/dependabot.yml` keeps the `github-actions` ecosystem and adds the stack's package ecosystem with its directory and schedule.
- A stack with no versioned Dependabot ecosystem, such as one with no package registry, may say so in the entry instead, and that is not a shortfall.
- The product code's CI is not required this week, and no shortfall arises from its absence.

**partial:**

- A stack decision entry exists, and at least one other `met` criterion fails.
- Typical shortfalls: an entry with no `**Why:**`; the entry naming a stack that the code does not use; `.gitignore` extended for one stack while the code uses another; `.github/dependabot.yml` unchanged; the `github-actions` ecosystem dropped from `dependabot.yml`.

**missing:**

- `docs/decisions.md` holds no decision recording the stack at the snapshot, or `.github/dependabot.yml` is absent.

**Guardrails:**

- The stack's quality, popularity, or fit is never a shortfall; record an entry whose `**Why:**` restates the choice rather than justifying it as a quality note.
- A choice explained in a task issue, or in `CONTRIBUTING.md`, without a `DEC-nnn` entry is the shortfall; a second record of the same choice is not judged.
- A Dependabot pull request's absence is never a shortfall.
- Week 4 may revise the stack, and a later revision is not judged here.

### S5 — Definition of Done and contributing guide

**Check:**

- `docs/definition-of-done.md` and `CONTRIBUTING.md` in the snapshot.
- The root `README.md`, for what it links.
- The team's GitHub project, for the views `CONTRIBUTING.md` names.

**met:**

- `docs/definition-of-done.md` carries exactly the sections `## Story`, `## Task`, and `## Pull Request`, in that order, each a list of plain bullets.
- `## Story` lists at least every acceptance criterion passing on `main`, the story's task issues closed with their pull requests merged, the story issue linking the evidence for each criterion, and the accountable member's check that each criterion is runnable and every link resolves.
- `## Task` lists at least every acceptance criterion of the task satisfied, and the task closing as completed when its pull request merges.
- `## Pull Request` lists at least one task issue closed and linked, the accountable reviewer ticking every task acceptance criterion before approving, the approval from a member other than the author, the link check and the Markdown check green, an `[Unreleased]` entry in `CHANGELOG.md` for a user-visible change, the acceptance criteria passing on the branch and on `main` after the merge, no secret, recording, or private-only material committed, and implementation notes in the pull request description.
- The three lists are disjoint: an item sits under the smallest unit it applies to, and the story list cites the task and pull request lists instead of repeating them.
- The Definition of Done does not restate `CONTRIBUTING.md`'s content, and `CONTRIBUTING.md` links `docs/definition-of-done.md` rather than copying it.
- `CONTRIBUTING.md` sits in the repository root and states the commit message format the team uses.
- `CONTRIBUTING.md` states how a change gets in: the branch naming rule, what a pull request must contain, and what the reviewer checks.
- `CONTRIBUTING.md` names the views the team uses in its GitHub project and why, and links the project.

**partial:**

- Both files exist with their sections, and at least one other `met` criterion fails.
- Typical shortfalls: a section missing, out of order, or renamed; checkboxes instead of bullets; an item of the minimum list absent; the pull request list restating the story list; `CONTRIBUTING.md` restating the Definition of Done; no commit message format; no statement of what the reviewer checks; no statement of the project's views.

**missing:**

- `docs/definition-of-done.md` or `CONTRIBUTING.md` is absent at the snapshot, or the Definition of Done has none of the three sections.

**Guardrails:**

- The commit message format is the team's; judge only that it is stated.
- The definition of done list is a standard, not a per-pull-request state: a bullet nobody ticked on a given pull request is never a shortfall here.
- Whether a merged pull request followed the list belongs to S7, and the Week 4 product-code CI item does not apply.
- An item in other but equivalent words is judgeable: report a differently worded item as a quality note unless it drops what the rule asks.

### S6 — Issue fields and GitHub project

**Check:**

- The per-issue field values first: from `issue-fields.json` (the collector's `--issue-fields` mode), from the REST `issue_field_values` in `gh api "repos/$REPO/issues/<n>"`, or from the GraphQL `issueFieldValues` query, per [procedure step 12](#assignment-specific-procedure-deltas).
- The fields' names, data types, options, issue-type pinning, and visibility from each issue's sidebar and from the project's fields, with `gh project field-list <number> --owner <org> --format json`, per [procedure step 12](#assignment-specific-procedure-deltas).
- The organization's GitHub projects, from `gh project list --owner <org> --format json`, `gh project field-list <number> --owner <org> --format json`, and `gh project view <number> --owner <org> --format json`, plus the project's page and the GraphQL `items` and `views` query in [procedure step 12](#assignment-specific-procedure-deltas) for its items and views.
- The project's description from `gh project view`'s `shortDescription`, or from the project page and its README; say in `**Evidence:**` which route answered.
- Every open issue and every issue the plan schedules, from `issue-fields.json` or `issues.json`, with its `milestone`, `assignees`, and field values.
- The repository's GitHub milestones, from the milestone list in S2.

**met:**

- The two issue fields `Responsible` and `Accountable` exist, each single-select, as every scheduled issue's `field_values` and the issue sidebar name them.
- Each field's options are one per team member, named by the member's GitHub username, and every member from the PDF's member table has an option, from the issue sidebar's option list or the project's fields.
- Each field is pinned to the issue types the team uses for story and task issues, or to `Issues without a type` when the team uses none, from the fields the sidebar offers on an issue of each type.
- Each field's visibility is `Public`, from the issue sidebar or the project's fields, or the team declares a deviation and carries the two roles as the labels `responsible:<username>` and `accountable:<username>`.
- One GitHub project exists per team, in the organization, titled after the product or the repository, and its description links the repository, from `gh project view`'s `shortDescription` or the project page and README.
- The project's visibility is `Public`.
- The project holds every open issue of the repository at or before `ISSUE_CUTOFF`.
- The project carries at least one table view whose columns include the `Responsible` and `Accountable` fields, the built-in `Assignees`, and the built-in `Milestone`, grouped or sorted by `Milestone`.
- Every issue the plan schedules at or before `ISSUE_CUTOFF`, and at least the `SPRINT-03` set, is in its sprint's GitHub milestone, from `issue-fields.json` or `issues.json` beside the milestone list.
- Every such issue's `Responsible` and `Accountable` values, from its `field_values` or its sidebar, name two different members, and its assignees are exactly those two members.
- On the label fallback, every such issue carries both role labels and the same two assignees.

**partial:**

- The fields exist or the project exists, and at least one other `met` criterion fails.
- Typical shortfalls: a field pinned to nothing, or with `Organization` visibility while the project is public; an option missing for a member; a private project; no table view, or a view without the two fields, the assignees, or the milestone; an open issue absent from the project; a scheduled issue in no milestone, or in the wrong sprint's milestone; values naming one member twice; assignees that differ from the values.

**missing:**

- Neither `Responsible` nor `Accountable` is readable from any issue's `field_values` or its sidebar, or no organization project holds the repository's issues, at `ISSUE_CUTOFF`.

**guardrails:**

- Public issues and their field values are readable by everyone, including non-organization-members, so read each issue's `issue_field_values` from REST or `issueFieldValues` from GraphQL, or the values in its sidebar.
- An empty `organization { issueFields }` result or a `totalCount` of `0` is never evidence that a field is absent, because that list needs organization membership the review token may not have.
- The project type has no plain description field: read the description from `shortDescription`, the project page, or the README, and read fields and options with `gh project field-list`, because a direct `fields` selection on the project type is a union and raises `selectionMismatch`.
- S6 is never `missing` on the organization field list alone: the per-issue values and the project settle the segment.
- A team that cannot create issue fields and declares the label fallback is judged on the fallback, and its absence of fields is never a shortfall.
- The project's auto-add workflow and adding items by hand both count.
- An issue the team has not scheduled is not a shortfall: only issues the plan schedules carry the two values and a milestone, and the `SPRINT-03` set is the floor.
- An already closed issue needs no values or milestone, and the values stay on it after it closes; do not require values on issues closed before Week 3.
- When the project cannot be queried with the token, say which endpoint failed, judge the rest from the issues, and set `Evidence gaps: yes` only when the answer could change the status.
- `**Evidence:**` names the route that answered: `issue-fields.json`, the REST `issue_field_values`, the GraphQL `issueFieldValues`, the issue sidebar, `gh project view`, `gh project field-list`, the project page, or the GraphQL project query.
- Whether a work item closed by a pull request followed the workflow belongs to S7; this segment judges only that the work item is scheduled.

### S7 — Minimum usable product on main

**Check:**

- `## Minimum Usable Product Candidate` in `reports/week-02/README.md` at the snapshot, for the candidate's stories.
- The task issues, their pull requests, reviews, and acceptance criteria, from `issues.json` and `prs.json`, with `issues/<n>.edits.json` for each task.
- The snapshot tree, for product code and for what runs.
- `docs/setup.md` and `.github/workflows/`, for what the slice needs and for the Pages deployment.
- The merged pull requests in the Week 3 window, for the order of the merge and the customer meeting.

**met:**

- At `ISSUE_CUTOFF` every candidate story's `US-nn` has at least one task issue that names it in the task's `Story` field.
- Every such task is closed as completed by the merge of the pull request that closes it, and every one of those pull requests is merged into `main`.
- Every such pull request closes exactly one task issue, and its head branch is `<closed task number>-<short lowercase hyphenated description>`.
- Every such task's acceptance criteria were ticked before the approving review, and every merged pull request has an approving review from a member other than its author.
- Every user-visible change a merged pull request made has an entry in the `[Unreleased]` section of `CHANGELOG.md`, or the pull request says it made no user-visible change.
- The snapshot contains product code for the slice, and the code is not a prototype committed to `main` under a `prototype/` or `spike/` directory.
- `docs/setup.md` at the snapshot covers the prerequisites, the install, the configuration pointing at a `.env.example` or similar, how to run the product, and how to run the checks and the tests.
- The prerequisites, the install command, the configuration, and the run command `docs/setup.md` gives are the ones the snapshot's files and lockfile use, so a reader following the page on a clean checkout reaches the core task.
- Every command `docs/setup.md` names exists in the snapshot: a script named by `npm run`, an entry point named by the page, and a lockfile that the install the page states consumes.
- Every pull request of the slice was merged before the Week 3 customer meeting that showed the stories, so nothing of the slice was left on a branch at the meeting.

**partial:**

- Product code for the slice is on `main`, and at least one other `met` criterion fails.
- Typical shortfalls: a candidate story with no task issue; a task still open at the deadline; a pull request that closes no issue or two; a branch without the task number; a merged pull request with no non-author approval, or with criteria ticked after it; a `docs/setup.md` with a section missing or a command that does not exist in the snapshot; a stated prerequisite the lockfile contradicts; a part of the slice merged after the meeting.

**missing:**

- The snapshot contains no product code that the candidate's stories need, or no candidate story has a merged pull request, at the snapshot.

**guardrails:**

- "Working" is judged from the page and the snapshot, never by running the product: a page whose steps and names match the snapshot satisfies the criterion, and a page whose steps cannot be followed as written does not.
- A command that would download something from the network is not a shortfall; a command that names a file, a script, or a version the snapshot does not contain is.
- A `docs/setup.md` that covers the minimum but leaves the directory it names unstated is a quality note when the reader could find it, and a shortfall when the reader could not.
- The slice's completeness against the stories belongs here, and the customer's verdict on each story belongs to S10.
- A Week 3 task outside the candidate is not owed and its absence is never a shortfall.
- Deployment is not required in Week 3, so a missing live instance is never a shortfall.

### S8 — Documentation site and setup page

**Check:**

- `docs/setup.md`, the root `README.md`, `.github/workflows/*.yml`, and the Pages configuration file, in the snapshot.
- The Actions runs of the Pages workflow, from `runs_main.json` and `runs_sha.json`, and the published site's URL from the PDF, the README, and the repository's Pages settings.
- One access check on the site's default page, per `docs/grader-policy.md#consumer-hosted-media`.
- Every third-party `uses:` in the deployment workflow.

**met:**

- `docs/setup.md` is in the snapshot and covers the prerequisites, the install, the configuration pointing at a `.env.example` or similar, how to run the product, and how to run the checks and the tests.
- The root `README.md` links `docs/setup.md`, and its text says the link is the setup and run instructions or equivalent.
- The root `README.md` links the site's URL, and the site serves the repository's documentation.
- A workflow under `.github/workflows/` publishes `docs/` to GitHub Pages, and it is the repository's Pages source, so the `github-pages` environment or the Pages settings name it.
- Every third-party `uses:` in that workflow is pinned to a full 40-character SHA with the version in a trailing comment on the same line.
- The Pages run on `main` at or before the snapshot commit time concluded `success`, or the run for the snapshot SHA did.
- The site's default page responds and is a landing page: it says what the product is and navigates to the other pages, rather than listing files.
- The site's default page and its navigation are served from the snapshot's `docs/` at or after the snapshot's content, so the site a reader reaches matches what was submitted.
- The site does not link the weekly reports, and a page that links a file outside `docs/` uses that file's GitHub URL.

**partial:**

- `docs/setup.md` exists and is linked from the root `README.md`, and at least one other `met` criterion fails.
- Typical shortfalls: a site workflow that exists but was never deployed, or whose latest run failed; an action pinned to a tag or a branch; a site linked from nothing; a default page that is a file listing; a setup page missing the configuration item or the checks-and-tests item; a setup page the README does not link.

**missing:**

- `docs/setup.md` is absent at the snapshot, or the repository publishes no site from `docs/` at all.

**guardrails:**

- The generator is the team's choice, and a site built with any of mdBook, Zensical, MkDocs, Jekyll, or a plain HTML page is judged the same.
- When the site's URL cannot be opened because Pages is gated, or the deployment run cannot be read, use the snapshot's workflow and the README as far as they settle it, and set `Evidence gaps: yes` only for the criterion the access leaves open.
- The site's design, navigation depth, and quantity of pages are quality notes.
- The setup page's content is judged here and in S7: a section it lacks is reported once, here, and a step that would not run is reported in S7.
- A Pages workflow the team added but whose URL differs from the one in the README is a shortfall when neither resolves.

### S9 — Week 2 action points and open questions

**Check:**

- `reports/week-03/meeting-report.md`, its `## Previous action points` and `## Previous open questions`.
- `reports/week-02/meeting-report.md` at the snapshot, for its `## Action points` rows due in Week 3 and every row of its `## Open questions`.
- Every artifact and task issue an `Outcome` or `Answer` cell links, and the `DEC-nnn` entries a `Decision` cell names.

**met:**

- `reports/week-02/meeting-report.md` exists in the snapshot and its `## Action points` and `## Open questions` can be read, or the report says there are none.
- `## Previous action points` in the Week 3 report has the columns `Action`, `Outcome`, and `Decision`, with one row per Week 2 action point due in Week 3 or carried out early.
- Every `Action` cell cites `reports/week-02/meeting-report.md#action-points` with the action quoted.
- Every `Outcome` says whether the action point was carried out and what was found, or why it was not, and links each artifact and task issue it changed.
- Every artifact an `Outcome` says changed holds that change: the artifact says what the outcome says, and the change is dated no later than `ISSUE_CUTOFF`.
- An action point not carried out reappears in the Week 3 `## Action points` with a new due week, unless its `Outcome` says the team or the customer dropped it.
- Every `Decision` cell links the `DEC-nnn` the outcome produced, or says `None`, and every linked entry exists, and its `**Source:**` points at where the decision was made.
- `## Previous open questions` has the columns `Question`, `Answer`, and `Decision`, with one row per Week 2 open question not yet closed and every Week 2 open question either answered there or carried into the Week 3 `## Open questions`.
- Every `Question` cell cites `reports/week-02/meeting-report.md#open-questions` with the question quoted, and every `Answer` says what the work or the meeting found and links each artifact the answer changed.

**partial:**

- The Week 3 `meeting-report.md` has both `## Previous` sections, and at least one other `met` criterion fails.
- Typical shortfalls: an action point due in Week 3 with no row; an outcome that exists only in the table, with the artifact unchanged; an action point not carried out that does not reappear; a Week 2 open question with no row and no carry-forward; a citation without the quoted action; an `Outcome` naming a task issue that does not exist.

**missing:**

- `reports/week-03/meeting-report.md` is absent at the snapshot, or neither `## Previous action points` nor `## Previous open questions` is present when the Week 2 report has rows for it.

**guardrails:**

- When the Week 2 report has no action point due in Week 3 or no open question, `None` in the matching section is correct.
- Do not re-grade the Week 2 report; judge only what Week 3 did with its rows.
- An outcome carried into an artifact is judged by whether the artifact changed, not by whether the change is large.
- An action point the customer dropped stays closed, and the customer's decision is cited.
- The report is a record of one meeting, so an action point closed in a later meeting of the same week still needs its row here only when the report covers that meeting.

### S10 — Customer validation of the working software

**Check:**

- `reports/week-03/meeting-script.md`, `reports/week-03/meeting-report.md`, and `reports/week-03/meeting-transcript.md` when it exists, in the snapshot.
- The path history of the script, for whether it was committed before the meeting.
- Every `DEC-nnn` the report lists, in `docs/decisions.md`, and every story issue the meeting showed or moved out, with its comments, timeline, and edit history.
- The Moodle PDF's recording line and any transcript appendix, with one access check on the recording link.

**met:**

- The script has exactly the sections `## Context`, `## Agenda`, `## Questions`, `## Roles`, and `## Key improvements`, in that order, with `## Roles` left out only for a meeting held in writing, and every empty section says `None`.
- `## Context` gives the problem-space sentence, what the team believes, and a one-sentence target that covers whether the finished stories do what the customer needs and what comes next.
- `## Agenda` is a numbered list whose first part asks the three permission questions, whose last part reads back the decisions and action points, and whose parts each have a timebox that add up to the planned length.
- The agenda runs each finished story in its own part and asks for its verdict there, then each candidate story the team will not finish, then the next stories, with the part the team is least sure of first among the parts after the previous follow-ups.
- Every agenda part names what is shown, with a link or a statement that nothing is shown, and every question appears in exactly one part.
- `## Questions` is numbered, every question is tagged open or closed, and every question serves the target.
- `## Roles` names a moderator, a note taker, and an observer by GitHub username.
- `## Key improvements` records at least one rewritten question with the before, the after, and the principle.
- The script's first commit predates the meeting date in `## Metadata`, and its later commits are formatting-only changes.
- The report has exactly the sections `## Metadata`, `## Previous action points`, `## Previous open questions`, `## Summary`, `## Decisions`, `## Action points`, `## Open questions`, and `## Disagreements`, in that order, and every empty section says `None`.
- `## Metadata` is a bulleted list of `- **Label:** value` bullets giving the date, the duration, the attendees by GitHub username with the customer as `Customer`, what was presented, the answer to each of the three permission questions, the transcript link or `None` with the reason, and the script link.
- `## Summary` has 3 to 5 bullets on what the meeting settled or changed.
- `## Decisions` lists at least one `DEC-nnn` entry of the form `[DEC-nnn: <the entry's first line>](../../docs/decisions.md#dec-nnn)`, and every story shown against its acceptance criteria has a verdict `DEC-nnn` in `docs/decisions.md` naming its `US-nn`, made by `Customer` or `Team, not contested`, with a `**Source:**` linking this report.
- Each rejected story's verdict names the `AC-nn` it failed, and each story moved out of the candidate has a `DEC-nnn` naming that story.
- A story moved out of the candidate whose departure leaves the remaining stories unable to complete the core task is accompanied by the same decision re-scoping the core task, and `MLS-03`'s description in `docs/project-plan.md` now opens with the new core task.
- Every `DEC-nnn` the report lists exists in `docs/decisions.md` with a `**Source:**` that links `reports/week-03/meeting-report.md`, and every linked entry's first line matches the report's link text.
- `## Action points` has the columns `Action`, `Owner`, and `Due`, at least two rows, an owner given by GitHub username, and every due date inside Week 4, such as `End of Week 4` or a date from 16 to 22 October 2026.
- `## Open questions` has the columns `Question`, `What it would change`, and `Follow-up`; `## Disagreements` has the columns `Your position`, `Customer's position`, and `What you changed`, and every row that changed nothing says why the team kept its position.
- Every story issue the meeting showed, accepted, rejected, or changed has a comment dated on or after the meeting that names the verdict or the change, names each `AC-nn` affected, and links the `DEC-nnn` on `main`.
- An accepted story is closed, a rejected one stays open, and each rejected story's failed `AC-nn` has an open rework task issue.
- When the meeting was recorded or held in writing and publication was permitted, `reports/week-03/meeting-transcript.md` exists, opens with `- **Date:**` and `- **Participants:**` bullets, and then has one sentence per line in the form `[hh:mm:ss] <label>: <sentence>`, labels speakers by GitHub username and `Customer`, marks gaps with `[inaudible]` or `[redacted]`, and carries no personal data.
- When publication was refused, no transcript is committed and the Moodle PDF carries it in an appendix.
- The Moodle PDF links a recording that instructors can open, or gives one line saying why there is none, and it agrees with the permission answers in `## Metadata`.
- The meeting was held in Week 3, between 9 October 2026 and `ISSUE_CUTOFF`, and a meeting held in writing is declared as a deviation.
- Every meeting artifact names the customer `Customer` and identifies people only by GitHub username.

**partial:**

- `reports/week-03/meeting-report.md` exists, and at least one other `met` criterion fails.
- Typical shortfalls: a missing or extra section; no permission part in the agenda; a story shown without its own part, or shown with no `AC-nn` verdict; a verdict decision that does not name its `US-nn`; an action point due outside Week 4; a script committed after the meeting; a published transcript without permission; a report that restates the transcript line by line.

**missing:**

- `reports/week-03/meeting-report.md` is absent at the snapshot, or no Week 3 meeting with the customer took place.

**guardrails:**

- When the Week 2 report has no previous action points or open questions, `None` in the matching section is correct.
- Do not re-grade the Week 2 script, report, or transcript.
- A later meeting has no per-area question floor, and the planned length is the team's choice.
- An inaccessible recording, or a recording gated to a sign-in, is an evidence gap for that check only, after the single access check `docs/grader-policy.md` allows.
- A transcript the customer refused to publish is Moodle-only, per `docs/grader-policy.md`; a recording link outside the meeting artifacts belongs to S12.
- The outcome of the action points the Week 3 report closes belongs to S9; this segment judges only the report's own sections and the verdicts.
- Week 3 has exactly one meeting per team; a second meeting is a quality note, and its artifacts may be read when they exist.

### S11 — Changelog and first release

**Check:**

- `CHANGELOG.md` and `docs/project-plan.md` in the snapshot.
- The repository's tags and releases, from `gh api "repos/$REPO/releases?per_page=100"` and `gh api "repos/$REPO/git/refs/tags"`.
- The tag protections, from `gh api "repos/$REPO/rulesets"` and `gh api "repos/$REPO/rulesets/<id>"`, by hand.
- The path histories of `CHANGELOG.md` and `docs/project-plan.md`, and the run and merge times they sit at.
- The rendered release page and the rendered tag permalink.

**met:**

- `CHANGELOG.md` sits in the repository root and follows Keep a Changelog, with an `[Unreleased]` section during development.
- Every user-visible change merged before `ISSUE_CUTOFF` has an entry in `[Unreleased]` or in a released section, unless its pull request says it made no user-visible change.
- At least one tag exists whose version follows Semantic Versioning with the `v` prefix, such as `v0.1.0`, and it is the first release this week cut.
- The first release tag points at a commit that is on `main`, and that commit is not after `ISSUE_CUTOFF`.
- A GitHub release exists for that tag, titled with the tag so the title and the tag match.
- The changelog has a dated section headed `[x.y.z](https://github.com/<org>/<repo>/releases/tag/vX.Y.Z) - YYYY-MM-DD` that links the release, its entries are the entries released, and a new empty `[Unreleased]` sits above it.
- A `#### REL-03` section in `docs/project-plan.md` carries the line `Released as [vx.y.z](https://github.com/<org>/<repo>/releases/tag/vx.y.z) on YYYY-MM-DD`, with the tag the release used.
- The tag's commit merge the state after the customer meeting's rework: every pull request the changelog's released entries describe is merged at or before the tag's commit, and the meeting is at or before it.
- The release tag is protected against being moved or deleted, by a ruleset that covers tag pushes.
- The tag predates the commit that added the changelog's released section, the commit that added the plan's `REL-03` line, and the commit that added `reports/week-03/README.md`, so every link to the release resolves against a tag that already existed.
- `SPRINT-03`'s GitHub milestone is closed once the release is cut, or still open with a reason in the week report.

**partial:**

- `CHANGELOG.md` exists, or a release was cut, and at least one other `met` criterion fails.
- Typical shortfalls: no `[Unreleased]` section; a tag without the `v` prefix, or not SemVer; a tag on a branch commit; a release titled differently from its tag; a dated section that does not link the release; no `REL-03` line; a document that links the release in a commit that predates the tag; an unprotected tag.

**missing:**

- `CHANGELOG.md` is absent at the snapshot, and no tag or release exists at `ISSUE_CUTOFF`.

**guardrails:**

- The version number is the team's choice under SemVer; a first release other than `v0.1.0` is never a shortfall.
- The Recommended shape, linking the changelog from the plan or `REL-nn` from the changelog, is a quality note.
- The tag's date decides whether the release was cut in Week 3; a late tag is a caveat in `**Evidence:**` and never a status change.
- When the tag rulesets cannot be read with the token, say which endpoint returned what, judge the rest, and set `Evidence gaps: yes` only when the answer could change the status.
- An `[Unreleased]` section, an empty `REL-04` to `REL-09`, and a later release are not judged here.

### S12 — Week report and submission

**Check:**

- `reports/week-03/README.md` at the snapshot, and every repository file it links.
- The Moodle PDF, its page count, and its contents.
- The snapshot SHA's position on `main`, and the snapshot commit time, per procedure step 4.
- The link and Markdown check runs on `main`, and the rendered links of the report.
- A privacy scan of the snapshot, per procedure step 14.

**met:**

- `reports/week-03/README.md` is in the snapshot, and every repository file it links is in the same snapshot.
- The report identifies the week, the project, the team, and the covered scope.
- The summary names `REL-03` and its tag, and what moved out of the candidate.
- The summary says what the team found, built, or decided, and what it left open.
- The report states the customer-meeting outcome: each story shown with whether the customer accepted or rejected it, and each candidate story that moved out, each citing its `DEC-nnn`.
- The coverage table has the 17 rows of `assignment-3.md`, in its order: Threshold of success, Project plan, Risk register, Stack decision, Definition of Done, Contributing guide, Sprint milestones and issue fields, GitHub project, Minimum usable product, Changelog and first release, Documentation site, Setup and run instructions, Week 2 action points, Week 2 open questions, Meeting script, Customer validation, and AI usage.
- Every coverage cell links its artifact, a repository file with its path from the repository root as the link text and the heading anchor when the row names a section, and anything else with descriptive link text.
- When the customer refused publication of the transcript, the Customer validation row says so and points at the Moodle submission.
- No second list of the same links follows the coverage table.
- A contribution table maps each member's GitHub username to the work done, with links to commits, pull requests, or reviews.
- The repository evidence links one merged pull request that closed its task issue, the latest green link-check run on `main`, and the latest green Markdown check run on `main`, and each link resolves.
- Every link in the report resolves, and every link the link check excludes is justified in prose.
- `## Deviations` declares every deviation observed in the other segments, or says `None` when there is none.
- One line states that no private-only material was committed to the repository.
- The privacy scan finds no private-only material in the snapshot outside the meeting artifacts.
- The snapshot SHA is on `main`, and the PDF permalink points at `reports/week-03/README.md` at that full 40-character SHA.
- The PDF is at most two pages, not counting a transcript appendix, and holds only the six items of `assignment-3.md`: the project name and team number, the member table, the permalink, the recording line, the transcript when publication was refused, and the privacy confirmation line.
- The root `README.md` links the current week's report, `reports/week-03/README.md`; this repeats the Week 1 rule, so a root README that still links an earlier week's report is recorded in `**Evidence:**` and never changes a status.

**partial:**

- `reports/week-03/README.md` exists at the snapshot, and at least one other `met` criterion fails.
- Typical shortfalls: a coverage row missing, out of order, or not linked; no release line in the summary; no meeting outcome; no contribution table; repository evidence missing a run or the pull request, or linking a red run; no `## Deviations`; an undeclared deviation; a privacy finding; a seven-character permalink; a snapshot that is not on `main`; a PDF over two pages or with extra content.

**missing:**

- `reports/week-03/README.md` is absent at the snapshot.

**guardrails:**

- A coverage row whose artifact is absent is a shortfall in the segment that owns the artifact; here the shortfall is only a missing row or a row that does not link.
- The candidate section, the verdicts, and the release's linkage are judged in S7, S10, and S11, so neither needs a coverage row of its own.
- Record the snapshot commit date against the deadlines in `**Evidence:**`, and never change a status for lateness.
- Report a privacy finding by path and kind, such as "a personal email address in `docs/setup.md`", never by value.
- A report that links a file at a commit other than the snapshot is judged on whether the target exists, not on the hash.
- The report's length, its prose, and the contribution table's wording are quality notes.

### S13 — AI usage and honesty

**Check:**

- `reports/week-03/ai-usage.md` in the snapshot.
- Traces of AI tools: `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.agents/`, `.opencode/`, `opencode.json`, `.github/copilot-instructions.md`, `.cursor/`, the `Co-Authored-By:` trailers, a `Harness:` or `Model:` trailer, and a "Generated with" line in Week 3 commit messages and pull request bodies.
- The Week 3 prose: `docs/threshold-of-success.md`, `docs/project-plan.md`, `docs/risks.md`, `docs/definition-of-done.md`, `CONTRIBUTING.md`, `docs/setup.md`, the meeting artifacts, and the report.

**met:**

- `reports/week-03/ai-usage.md` names each tool and what it was used for, and says what the team did with the output: what it accepted, changed, and rejected, and why.
- Alternatively, the file states in one line that no AI tools were used, and nothing in the repository or its history contradicts it.
- The disclosure agrees with the traces of AI tools in the repository, the commit messages, and the pull request bodies, including an agent installed as the course-materials skill.
- The Week 3 prose has no filler, meaning no template sentence without a product name, an identifier, or a date, and no unchecked generated text, such as leftover `<org>` or `<repo>` placeholders, identifiers that point nowhere, or claims that contradict the team's own artifacts.
- Every identifier a Week 3 artifact states resolves to an artifact that carries it, and every count it states matches the artifact it counts.
- Where the statement of a goal, a risk, or a milestone's first sentence separates what was observed from what was inferred, it says which; a claim with no evidence behind it is a shortfall here only when it contradicts the team's artifacts.

**partial:**

- `reports/week-03/ai-usage.md` exists, and at least one other `met` criterion fails.
- Typical shortfalls: tools named without saying what happened to their output; agent traces or co-author trailers with no disclosure; a placeholder or a template sentence left in a Week 3 artifact; a `TOS-nn`, `RISK-nn`, or `REL-nn` cited that does not exist; a statement of how many sprints or goals that the artifact contradicts.

**missing:**

- `reports/week-03/ai-usage.md` is absent at the snapshot.

**guardrails:**

- Using AI tools is allowed and is never a shortfall by itself.
- The course-materials submodule alone does not prove agent use; count it as undisclosed use only when other traces show agent output.
- The meeting report's own-words rule belongs to S10.
- Week 1 and Week 2 text left unchanged is not re-judged.
- The filler test is anchored to the artifact's own evidence: quote a short fragment, and name the artifact and the heading.

## Assignment-specific procedure deltas

1. Take the team set from the directory names under `itpd-assignments-feedback/A3/submissions/`.
2. Read the Moodle PDF with the submission fetcher, which prefers the PDF that carries the full-SHA permalink to `reports/week-03/README.md` when there are several:

   ```console
   uv run python scripts/fetch_team_snapshot.py A3 "<team_dir>"
   ```

   It records the extracted metadata in `itpd-assignments-feedback/A3/work/<team_dir>/pdf-info.json`: the team number, repository, permalink, full SHA, recording link, page count, GitHub usernames, and the member name/email tokens for the step 12 privacy scan.
   The fallback is to read the PDF directly and extract:

   - the project name and the team number;
   - the GitHub usernames of the member table, keeping real names and emails only in working memory for the privacy match;
   - the permalink to `reports/week-03/README.md`, with its organization, repository, and full SHA;
   - the recording link or the line saying why there is none;
   - whether a transcript appendix is present;
   - the privacy confirmation line;
   - the page count, for example from `pdfinfo`, and anything outside the six allowed items.

3. The fetcher in step 2 resolves the snapshot per `docs/grader-policy.md` and refetches it into a freshly emptied `itpd-assignments-feedback/A3/work/<team_dir>/snapshot/`.
   When it cannot, resolve and fetch by hand as in `agents/grader.md`.
4. Read the snapshot commit time and the on-`main` result from `pdf-info.json` (`snapshot_time`, `on_main`, `on_main_status`), or re-check them with `REPO=<org>/<repo>` and `SHA=<full SHA>`:

   ```sh
   gh api "repos/$REPO/commits/$SHA" --jq '.commit.committer.date'
   gh api "repos/$REPO/compare/$SHA...main" --jq '.status'
   ```

   A status of `identical` or `ahead` puts the commit on `main`; `behind` or `diverged` does not, which is an S12 shortfall.
   Call the first value `SNAPSHOT_TIME`.

5. Collect the live evidence once and keep it beside, not inside, the fetched snapshot.
   Preferred: `uv run python scripts/collect_github_evidence.py A3 "<team_dir>" [--issues <n> ...] [--paths <path> ...]`, which reads `itpd-assignments-feedback/A3/work/<team_dir>/pdf-info.json` and writes `labels.json`, `issues.json`, `prs.json`, `runs_main.json`, `runs_sha.json`, `commits.json`, `milestones.json`, `releases.json`, `tags.json`, plus `issues/<n>.comments.json`, `issues/<n>.timeline.json`, `issues/<n>.edits.json`, `paths/<path>.json`, and a bounded `summary.md` there, printing counts and paths only.
   Read `summary.md` first: it carries the issue counts, the pull-request numbers, the failing runs, the tags, and each milestone's due date with its open and closed issue counts, in at most 60 lines.
   Open a dump only through a bounded projection that prints at most about 40 lines (`head -n 40`, a `jq` projection, or an `rg` match); never `cat` a full dump, because `commits.json` reached 1.35 MB and `prs.json` 284 KB.
   `--summary` rebuilds the digest from the saved dumps without calling `gh`.
   The issue fields are their own mode: `uv run python scripts/collect_github_evidence.py A3 "<team_dir>" --issue-fields` writes `issue-fields.json` there with every issue's `type`, `milestone`, `assignees`, and `field_values`, from one paginated REST list call and without its pull requests.
   It is not combined with `--summary`, `--issues`, or `--paths`.
   The raw fallback commands are:

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

   For each story issue and each task issue a check needs, read its comments, its timeline of label, rename, milestone, and close events, and its body edit history:

   ```sh
   gh api "repos/$REPO/issues/<n>/comments" --paginate
   gh api "repos/$REPO/issues/<n>/timeline" --paginate
   gh api graphql -F owner='<org>' -F name='<repo>' -F n=<n> -f query='
     query($owner: String!, $name: String!, $n: Int!) {
       repository(owner: $owner, name: $name) {
         issue(number: $n) {
           milestone { title dueOn }
           assignees(first: 10) { nodes { login } }
           lastEditedAt
           userContentEdits(first: 100) { nodes { editedAt diff } }
         }
       }
     }'
   ```

   The REST `body` stays in `issues.json`, and the GraphQL fields add the milestone, the assignees, and the edit history beside it.

   For the history of a repository path and the pull request behind each commit:

   ```sh
   gh api "repos/$REPO/commits?sha=$SHA&path=<path>&per_page=100" \
     --jq '.[] | [.sha, .commit.committer.date, (.commit.message | split("\n")[0])] | @tsv'
   gh api "repos/$REPO/commits/<commit>/pulls" --jq '.[] | [.number, .title, .merged_at] | @tsv'
   gh pr diff <n> --repo "$REPO"
   ```

6. Judge every issue as of `ISSUE_CUTOFF`, the hard deadline `2026-10-17T23:59:59+03:00`:

   - Count only issues whose `createdAt` is at or before `ISSUE_CUTOFF`.
     An issue opened after `SNAPSHOT_TIME` but by `ISSUE_CUTOFF` counts like any other.
   - Take an issue's labels at `ISSUE_CUTOFF` from its timeline's `labeled` and `unlabeled` events, its title from `renamed` events, and its open or closed state and close reason from `closed` and `reopened` events.
   - Take its body from the last edit at or before `ISSUE_CUTOFF` when the edit history allows it; otherwise judge the current body and say so in `**Evidence:**`.
   - Take its milestone from the `milestoned` and `demilestoned` events when the issue has them, and its current milestone otherwise, noting in `**Evidence:**` which was read.
   - A comment or edit made after `ISSUE_CUTOFF` is a caveat, never a shortfall.
   - Post-cutoff file state is a caveat and never a status change, except in a segment that judges the snapshot, which reads the file at `SNAPSHOT_TIME`.
   - Set `Evidence gaps: yes` only when the state at `ISSUE_CUTOFF` cannot be read and the difference could change the status.
   - Pull requests, Actions runs, repository files, tags, and releases stay judged as of `ISSUE_CUTOFF`, and the snapshot stays the evidence for files.

7. Identify the Week 3 pull requests: every pull request created on or after Friday 9 October 2026, 00:00 Innopolis time, the start of Week 3 in `course/syllabus.md`.
   A pull request merged at or before the team's Assignment 2 snapshot commit is part of the Week 2 submission, not a Week 3 pull request; check the Week 2 report's permalink when `reports/week-03/README.md` does not say it.
   The in-scope pull requests for S7 run from the first one that closes a task issue on a candidate story to `ISSUE_CUTOFF`, without Dependabot pull requests and pull requests a workflow opened.

8. For each in-scope pull request, check the workflow:

   ```sh
   gh pr list --repo "$REPO" --state all --limit 500 \
     --json number,headRefName,author,state,mergedAt,closingIssuesReferences,reviews,milestone \
     --jq '.[] | {n: .number, branch: .headRefName, author: .author.login, state, merged: .mergedAt,
                  closes: [.closingIssuesReferences[].number],
                  approvers: [.reviews[] | select(.state == "APPROVED") | .author.login] | unique,
                  milestone: .milestone.title}'
   ```

   - `closes` has exactly one number, and that issue carries `task` or the team's task marker.
   - `branch` matches `^<that number>-[a-z0-9]+(-[a-z0-9]+)*$`.
   - A merged pull request has an approver other than its author, its task's body has every criterion ticked as `- [x] AC-nn:`, and the task's `stateReason` is `COMPLETED`.
   - Compare the task's body edit history (`userContentEdits` `editedAt`, from step 5) with each approving review's `submittedAt`.
     A shortfall needs the history to show a box ticked after the approval.
     When the task has no edit history, check only that every box is ticked by merge and say so in `**Evidence:**`.
   - A pull request closed without merging left its task `NOT_PLANNED` with a comment that gives the reason and links the pull request.

9. Confirm that the slice runs, from the snapshot and the page, without running the product:

   - List the product's source files in the snapshot, with `find . -type f \( -name '*.py' -o -name '*.js' -o -name '*.ts' -o -name '*.tsx' -o -name '*.jsx' -o -name '*.go' -o -name '*.java' -o -name '*.kt' -o -name '*.dart' -o -name '*.rb' -o -name '*.rs' -o -name '*.php' -o -name '*.cs' \) -not -path './.github/*' -not -path './.agents/*' -not -path './node_modules/*' -not -path './.venv/*'`, and note `src/`, `app/`, `backend/`, or `frontend/`.
   - Read `docs/setup.md` and confirm that every command it names exists: each `npm run <script>` has that key in `package.json`; each Python entry point, module, or `pyproject.toml` script exists; each `make <target>` has that target; each container command has its compose or Dockerfile.
   - Confirm that the lockfile the page's install step consumes is present, and that the runtime version the page states is not contradicted by `package.json`'s `engines`, `.nvmrc`, `pyproject.toml`'s `requires-python`, or the tool-version file.
   - Confirm that the configuration the page states through a `.env.example` or similar file exists, and that the variables the code reads are the ones the file shows.
   - Confirm that nothing in a `prototype/` or `spike/` directory is product code the slice needs.

10. Check the customer-driven chain from the working software to the candidate:

    - Start from each candidate `US-nn` in `reports/week-02/README.md`, and find its task issues and pull requests.
    - Find the story issue's verdict comment inside Week 3, and confirm that it links a `DEC-nnn` whose entry names that `US-nn`.
    - Confirm that each `DEC-nnn` the verdict cites is listed in `## Decisions` of the Week 3 meeting report, and that its `**Source:**` links that report.
    - For a story moved out, confirm that its `DEC-nnn` names the story, that the story issue records the move, and that `MLS-03` in `docs/project-plan.md` was re-scoped when the remaining stories no longer complete the core task.
    - Search the snapshot and the issues for the verdict `DEC-nnn`, so that a decision nothing cites is visible.

11. Check the release against the tag:

    - Read `gh api "repos/$REPO/releases?per_page=100"` for the tag names, titles, and dates, and `gh api "repos/$REPO/git/refs/tags/<tag>"` for the commit the tag names.
    - Confirm that the tag's commit is an ancestor of `main`, with `gh api "repos/$REPO/compare/<tag>...main" --jq '.status'`, which is `ahead` or `identical` when it is.
    - Read the changelog's dated section, the plan's `REL-03` line, and `reports/week-03/README.md` at the snapshot, and find, for each, the pull request that first added it, with the commits API over the file's path.
    - Compare the merge time of those three pull requests with the release's `published_at` and the tag's commit date; each must be later than, or at, the tag.

12. Check the milestones, the issue fields, and the project from the issue dumps and the organization's endpoints:

    ```sh
    gh api "repos/$REPO/milestones?state=all&per_page=100" \
      --jq '.[] | [.title, .due_on, .state, .open_issues, .closed_issues] | @tsv'
    gh api "repos/$REPO/issues/<n>" \
      --jq '{number, type: (.type.name // null), milestone: (.milestone.title // null),
             assignees: [(.assignees // [])[].login],
             field_values: [(.issue_field_values // [])[] | {field: .issue_field_name, data_type, value: (.single_select_option.name // .value)}]}'
    gh project list --owner <org> --format json
    gh project field-list <number> --owner <org> --format json
    gh project view <number> --owner <org> --format json
    ```

    Read the per-issue values first, from `issue-fields.json` or the REST projection above, and the field names, options, issue-type pinning, and visibility from the issue sidebar and the project's fields.
    The same values are available from GraphQL when REST cannot answer:

    ```sh
    gh api graphql -F owner='<org>' -F name='<repo>' -F n=<n> -f query='
      query($owner: String!, $name: String!, $n: Int!) {
        repository(owner: $owner, name: $name) {
          issue(number: $n) {
            number
            milestone { title }
            assignees(first: 10) { nodes { login } }
            issueFieldValues(first: 20) {
              nodes {
                ... on IssueFieldSingleSelectValue { field { ... on IssueFieldSingleSelect { name } } value }
                ... on IssueFieldMultiSelectValue { field { ... on IssueFieldMultiSelect { name } } value }
                ... on IssueFieldTextValue { field { ... on IssueFieldText { name } } value }
              }
            }
          }
        }
      }'
    ```

    The organization `issueFields` list is not evidence: it needs organization membership the token may not have, and an empty list or `totalCount: 0` never means a field is absent.
    When the project page or `gh project view` cannot answer, read the project's items and views from one GraphQL query:

    ```sh
    gh api graphql -F owner='<org>' -F number=<n> -f query='
      query($owner: String!, $number: Int!) {
        organization(login: $owner) {
          projectV2(number: $number) {
            number
            title
            shortDescription
            public
            readme
            items(first: 100) {
              totalCount
              nodes {
                content {
                  ... on Issue { number title state }
                  ... on PullRequest { number title state }
                }
                fieldValues(first: 20) {
                  nodes {
                    ... on ProjectV2ItemFieldSingleSelectValue {
                      name
                      field { ... on ProjectV2SingleSelectField { name } }
                    }
                    ... on ProjectV2ItemFieldTextValue {
                      text
                      field { ... on ProjectV2FieldCommon { name } }
                    }
                  }
                }
              }
            }
            views(first: 20) {
              nodes { name layout }
            }
          }
        }
      }'
    ```

    The project type has no plain description field: read the description from `shortDescription` in the query or `gh project view`, or from the project page and README, and say in `**Evidence:**` which route answered.
    A direct `fields` selection on the project type is a union and raises `selectionMismatch`, so read the field names, options, and data types from `gh project field-list` instead.
    The `fieldValues` connection returns one node per value type, so filter the nodes that carry a field name.
    Read each project's visibility from `gh project view` or the query above, and the table views and their columns from the project's page, `gh project field-list`, or the `views` connection.
    Say in `**Evidence:**` which route answered.

13. Check that every `**Sprint Backlog:**` link in `docs/project-plan.md` resolves, and that the milestone it names is the sprint's own milestone and lists the issues scheduled into that sprint:

    ```sh
    gh api "repos/$REPO/milestones/<number>" --jq '[.title, .due_on, .open_issues, .closed_issues] | @tsv'
    gh api "repos/$REPO/issues?milestone=<number>&state=all&per_page=100" \
      --jq '.[] | [.number, .title, .state] | @tsv'
    ```

14. Scan the snapshot for private-only material:

    ```console
    uv run python scripts/scan_privacy.py A3 "<team_dir>"
    ```

    It reads `itpd-assignments-feedback/A3/work/<team_dir>/pdf-info.json`, strips inline `data:...;base64,` payloads, and checks email addresses, phone numbers, `.env` and key files, recording links outside meeting artifacts, and the real names from the PDF member table, including hits in meeting artifacts.
    It reports one line per file with a count, such as `docs/setup.md: email address (x2)`, plus per-rule hit and file totals; the exit code is 1 when it finds any.
    The raw fallback is email addresses with `grep -rnE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'`, phone numbers, the real names from the PDF member table, recording links in meeting files, and `.env` files.
    Report each finding by path and kind only, with the number of hits per file.

15. Open the documentation site's default page and the recording link once each, per `docs/grader-policy.md#consumer-hosted-media`.

16. Grade each of the 13 segments independently, and report each shortfall only in the segment that owns it in the [segment overview](#segment-overview).

## Assignment-specific constraints

- The `Primary index reviewed` metadata bullet points to `reports/week-03/README.md` at the snapshot whenever the snapshot is inspectable.
- Moodle-only items are judged from the PDF, and their absence from the repository is correct: the member table with real names and university emails, the recording link, and a transcript the customer refused to publish.
- Never copy a real name or an email from the PDF into feedback; refer to people by GitHub username.
- A recording or external view that fails its single access check is an evidence gap for that check only, and the surrounding evidence is still judged.
- A transcript appendix does not count toward the PDF's two pages.
- Week 1 and Week 2 artifacts are not re-graded on their own requirements: repository setup, branch protection, the link-check configuration, Dependabot, the GitHub project's absence before Week 3, the research content, the Week 1 and Week 2 reports, and the kickoff artifacts.
- Week 1 and Week 2 artifacts are checked only where Assignment 3 requires it: the vision's goal linking the threshold (S1), the Week 2 candidate's stories (S7), the Week 2 action points and open questions (S9), the link check and the Markdown check green on `main` (S12), and the story and task issues the slice closes (S7).
- When a Week 2 artifact that Assignment 3 builds on is absent, such as a Week 2 report with no candidate, judge the Assignment 3 item against what exists, report the absence in the segment that owns the artifact it should contain, and do not report the Week 2 absence again.
- The one-time catch-ups in Parts 1–4 are judged by their end state when a team already met the newer rule before Week 3.
- Week 3 has no product-code CI and no deployment, so neither is expected.
- The course-materials submodule is Recommended; excluding its directory from both checks is allowed, and its absence is never a shortfall.
- Use the course's terminology in feedback: `Customer` for the person the team answers to, story issue, task issue, meeting report, meeting script, minimum usable product candidate, threshold of success, plan milestone, sprint milestone, and release.
