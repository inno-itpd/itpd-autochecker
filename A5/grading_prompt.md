# Assignment 5 Grading Criteria

This rubric is for the compliance agent that reviews ITPD Assignment 5 team submissions.
ITPD assigns no points: each segment gets one status, `met`, `partial`, `missing`, or `unverified`, and an `Evidence gaps: yes|no` flag, per `docs/compliance-feedback-format.md`.
The instructor assigns the grade from the statuses and the evidence, so this rubric never proposes a grade, a score, or a late penalty.
The shared rules live in `docs/grading-policy.md`: evidence states, verified absence, blocked and conflicting artifacts, snapshot resolution, live GitHub evidence through `gh api`, the single access check for consumer-hosted media, privacy, undeclared deviations, and rule applicability by `Since:` marker.
This file states only what is specific to Assignment 5 and does not repeat those rules.

## Authoritative sources

All paths are in the course-materials submodule, pinned at itpd commit `0173b82dfb82e515457a1074970c116760490c79`.
If the checked-out submodule differs from that commit, read each file with `git -C A5/itpd show 0173b82dfb82e515457a1074970c116760490c79:<path>`.

- `A5/itpd/assignments/assignment-5.md` — the student-facing brief: Parts 1–12, What Good Looks Like, the repository report contents, the Moodle report contents, the submission procedure, and the checklist.
- `A5/itpd/requirements/general-requirements.md` — artifact terms, the `reports/week-NN/` vs `docs/` split, the identifier rules including `QRT-nn` and the pair `QR-01 QRT-02`, and how a later week cites an earlier action point.
- `A5/itpd/requirements/planning-requirements.md` — `docs/project-plan.md` with `## Milestones`, `## Sprints`, `## Releases`, and `## Quality Requirement Testing Plan`; the `**Due:**`, `**Sprints:**`, `**Advances:**`, `**Planned Velocity:**`, and `**Actual Velocity:**` fields; and the `REL-nn` block with `**Released:**` and `**Checked QRs:**`.
- `A5/itpd/requirements/sprint-ceremonies-requirements.md` — sprint planning, product backlog refinement, estimation, the Sprint Review, and the retrospective with its four sections, row counts, and columns.
- `A5/itpd/requirements/issue-tracking-requirements.md` — scheduling as the sprint's GitHub milestone, the `Responsible` and `Accountable` fields, the matching assignees, and the public GitHub project.
- `A5/itpd/requirements/user-stories-requirements.md` — the story issue's `User Story` type, its `MoSCoW` value, its checkbox `AC-nn` criteria, and `### Specified by`.
- `A5/itpd/requirements/task-issues-requirements.md` — the `Task` issue type, its `### Requirements`, and the pull request that closes it.
- `A5/itpd/requirements/quality-requirements-requirements.md` — the `QR-nn` file, the six-part scenario, the `## QRT-nn` section and its fields, the four levels and the environment each runs in, the index, and the Week 5 index rules.
- `A5/itpd/requirements/functional-requirements-requirements.md` — the `FR-nnn` file that owns a capability's behavior, which a feature entry links as `**Behavior:**`.
- `A5/itpd/requirements/architecture-requirements.md` — `docs/architecture/README.md`, its drivers, and its ADR index, which the Sprint Review and a feature entry reach.
- `A5/itpd/requirements/adr-requirements.md` — the `ADR-nnn` record a feature entry links as `**Decisions:**`, and its `**Addresses:**` list.
- `A5/itpd/requirements/product-vision-requirements.md` — the vision's boundary and system context, which make a deployment claim a claim about the product.
- `A5/itpd/requirements/customer-meetings-requirements.md` — the weekly meeting as the Sprint Review, showing the deployed production instance and each implemented test's result at its level, the script, the report's `## Previous action points` and `## Previous open questions`, and the transcript.
- `A5/itpd/requirements/decisions-requirements.md` — the `DEC-nnn` entry, its `**Source:**`, and what cites it.
- `A5/itpd/requirements/releases-requirements.md` — `CHANGELOG.md`, Semantic Versioning, tags and their protection, the release title, and the user-facing body that ends with the `Full changelog` line.
- `A5/itpd/requirements/weekly-report-requirements.md` — the weekly public report and its coverage table, the AI usage report, declaring deviations, and the Moodle PDF.
- `A5/itpd/requirements/visibility-requirements.md` — what is public, what is Moodle only including the VM's addresses, and screenshot sanitization.
- `A5/itpd/requirements/glossary-requirements.md` — `docs/glossary.md` and the terms a feature entry links at first use.
- `A5/itpd/requirements/agent-instructions-requirements.md` — the team's root `AGENTS.md`, read for what it states and as an AI trace.
- `A5/itpd/requirements/pull-requests-requirements.md` — every change through a pull request, one change per pull request, review and approval, and closing a task issue.
- `A5/itpd/requirements/repository-requirements.md` — the link check, the Markdown check, `actionlint`, the five product-code checks, pinning third-party actions, and the four environments with the manual deployment on the university VM.
- `A5/itpd/requirements/definition-of-done-requirements.md` — `docs/definition-of-done.md` and the `## Pull Request` list the Week 5 checks join.
- `A5/itpd/requirements/minimum-usable-product-requirements.md` — the core task a production deploy verifies.
- `A5/itpd/requirements/features-requirements.md` — `docs/features.md`: where the page lives, its flat capability entries, the `**Stories:**`, `**Behavior:**`, and `**Decisions:**` links, the same-pull-request rule, and the Week 5 minimum.
- `A5/itpd/guides/quality-requirement-tests.md` — the method for turning a response measure into a test, choosing its level, running it in the right environment, and recording its row.
- `A5/itpd/guides/deployment-and-environments.md` — the method for the environment map, the VM, the configuration, the staging and production deploys, the verification, the rollback, and the runbook.
- `A5/itpd/guides/quality-and-architecture.md` — the method for the quality requirements and, in Step 8, the feature page.
- `A5/itpd/guides/planning-and-tracking.md` — the method for the milestones, the sprints, the release order, the release body, and the retrospective.
- `A5/itpd/guides/validating-with-the-customer.md` — the method for the meeting's target, questions, agenda, roles, and tracing what changed.
- `A5/itpd/course/rules.md` — the course contract, the AI policy, the submission channel, and the Saturday-at-23:59 deadline policy.
- `A5/itpd/course/syllabus.md` — the Week 5 objectives and deliverables, the hard deadline, and the following week's hard deadline.
- `A5/itpd/AGENTS.md` — course terminology and the `docs/` destination map, which puts `docs/deployment.md` and `docs/features.md` in Week 5.

Apply every rule marked `**Since: W1**`, `**Since: W2**`, `**Since: W3**`, `**Since: W4**`, or `**Since: W5**`.
No rule in the pinned materials carries a `**Since: W6**` or later marker, so nothing is excluded by a later marker; the analytics, usability testing, and configuration management the syllabus schedules from Week 6 on are not Assignment 5 deliverables, and their absence is never a shortfall.

## Assignment parameters

- Report title: `# Assignment 5 Feedback Report`
- Week: `W5`
- Course materials: `A5/itpd` at `0173b82dfb82e515457a1074970c116760490c79`
- Primary index artifact: `reports/week-05/README.md` at the snapshot, as named in Assignment Report In The Repository and in Moodle item 3 of `assignment-5.md`.
- Week window: from Friday 23 October 2026, 00:00 Innopolis time, `2026-10-23T00:00:00+03:00`.
  The syllabus gives the Week 5 class week as 23 to 29 October 2026; the submission is due on the Saturday after it, and the window runs from that Friday to `ISSUE_CUTOFF`.
- Soft deadline: none; `course/rules.md` gives every group submission from Week 4 to Week 9 a single hard deadline, and `course/syllabus.md` and `assignments/assignment-5.md` state the same date.
- Hard deadline: Saturday 31 October 2026, 23:59, as the pinned `course/syllabus.md` and `assignments/assignment-5.md` state it.
- No per-team deadline override exists for Week 5: every team's deadline is Saturday 31 October 2026, 23:59.
- `ISSUE_CUTOFF`: `2026-10-31T23:59:59+03:00` for every team.
  Every later reference to `ISSUE_CUTOFF` means that cutoff, and `**Evidence:**` states the cutoff used.
- Hard deadline of the following week: Saturday 7 November 2026, 23:59, the deadline the Week 6 syllabus block gives and the due date `SPRINT-06`'s GitHub milestone carries.
  A Week 5 action point due in Week 6 carries a due date inside the Week 6 class week, 30 October to 5 November 2026, as `course/syllabus.md` gives Week 6; 7 November is the Week 6 submission deadline, and a due date from 6 November on falls in Week 7 and is outside the meeting's Week 6 window.
- The time zone is not stated in the materials; read every deadline as Innopolis time (UTC+3).
- Submission inputs: the Moodle PDF under `itpd-assignments-feedback/A5/submissions/<team_dir>/`; there is no ZIP, so the snapshot upload to Moodle is not judged.
  The snapshot is fetched from GitHub at the permalink SHA into `itpd-assignments-feedback/A5/work/<team_dir>/snapshot/`.
- Live artifact families: the story and task issues with their types, field values, comments, timelines, and edit history; repository labels; pull requests with their reviews, files, and closing references; Actions runs of the link check, the Markdown check, `actionlint`, and the product code; the repository's tags and releases; the seven sprint GitHub milestones; the organization's GitHub project with its fields and table view; the published documentation site, read only where a Week 5 criterion names it; and the Moodle recording link.
- Story and task issues, their types, their field values, their milestones, and the labels are not in the snapshot, so they are read live and judged as of `ISSUE_CUTOFF`, per [procedure step 6](#assignment-specific-procedure-deltas).
  An issue opened after the snapshot commit but by `ISSUE_CUTOFF` counts.
- Tags, releases, milestones, the GitHub project, and the documentation site are read live and judged as of `ISSUE_CUTOFF` too.
  An issue-field value has no history in the API: read the current value and read the issue's timeline for what changed after `ISSUE_CUTOFF`, and say so in `**Evidence:**` when the timeline cannot settle it.

The segments, in order:

- S1: Sprint plan and milestones
- S2: New stories and backlog refinement
- S3: Automated tests and CI checks
- S4: Deployment and environments
- S5: Quality requirement tests
- S6: Testing plan and results
- S7: Feature documentation
- S8: Week 4 action points and open questions
- S9: Customer validation of the deployed product
- S10: Redeploy and retest after same-week rework
- S11: REL-05 release
- S12: Sprint close and retrospective
- S13: Week report and submission
- S14: AI usage and honesty

### Segment overview

Every checklist item and every coverage-table row, or named part of a row, of `assignment-5.md` maps to exactly one segment, and a shortfall is reported only in the segment that owns it.

| Segment | Covers |
|---------|--------|
| S1: Sprint plan and milestones | Part 1 items 1–3; the goal, planned-velocity, and milestone part of coverage row Sprint plan and milestones; the plan milestones due in `SPRINT-05` to `SPRINT-09`; checklist items "`SPRINT-05` planned with its goal, its `**Due:**` field, its `**Sprint Backlog:**` link, and its `**Planned Velocity:**`" and "2 or more plan milestones due in `SPRINT-05` through `SPRINT-09` in total, with only the shortfall added, the two due in different sprints, and each with its fields and its increment" |
| S2: New stories and backlog refinement | Part 1 items 4–7; coverage row New stories; checklist items "2 or more new `US-nn` in the Week 4 shape, at least one scheduled in `SPRINT-05` and one refined for `SPRINT-06` with no milestone" and "The next two sprints' worth of the product backlog refined, with the `Story Points` on each and no sprint milestone" |
| S3: Automated tests and CI checks | Part 2; coverage row Automated tests and CI; checklist items "`actionlint` over `.github/workflows/` and a named step for each applicable product-code check, on pull requests and `main`, every action pinned", "The checks that do not apply recorded with their reason, and the automated test suite covering the testability requirement's critical modules", and "The Definition of Done's pull request list carries `actionlint` and the product-code checks, the latest `main` runs are green, and the workflow deploys nothing" |
| S4: Deployment and environments | Part 3 items 1–6; coverage row Deployment; checklist items "`docs/deployment.md` with the four environments, the campus access, the configuration, the deploy, the verification, and the rollback, and no real address" and "The release candidate deployed to staging and production, the core task verified from a campus machine, and the real addresses in the Moodle submission". The VM-unavailable fallback (Part 3 item 7) is accepted here as a declared deviation; its test-level consequence belongs to S5 and S6, and the PDF's own shape to S13 |
| S5: Quality requirement tests | Part 4; coverage row Quality requirement tests; checklist items "A `QRT-nn` inside every active High business-importance requirement's file, with its fields, its procedure, and its pass criterion" and "The testability requirement's `CI` test and one other active requirement's test at `CI`, `scripted`, or `deployed`, with the High-requirement and next-active-row rule applied, and no `manual` test standing in for the second" |
| S6: Testing plan and results | Part 5 items 1–3 and 5–6; coverage rows Testing plan and the index-link part of Quality requirement tests; checklist items "The testing plan with one row per test, the testability and other implemented rows `Passes` and `Checked` in `SPRINT-05`, and every other row keeping its result" and "The quality requirements index links the testing plan once". The report's pointer at the plan and its no-copied-rows rule are S13's (Part 5 item 4) |
| S7: Feature documentation | Part 6; coverage row Feature documentation; checklist item "Feature documentation in `docs/features.md`, with at least three features or every feature, one sentence per capability with its glossary term linked, the page's glossary line, and the story, requirement, and record links". The report's coverage row that links the page is S13's (Part 6 item 6) |
| S8: Week 4 action points and open questions | Part 7; coverage rows Week 4 action points and Week 4 open questions; checklist items "Each Week 4 action point's outcome in `## Previous action points`, and in the artifact it changed" and "Each Week 4 open question answered or carried forward in `## Previous open questions`" |
| S9: Customer validation of the deployed product | Part 8; coverage rows Meeting script, Meeting transcript, and Customer validation; checklist items "`reports/week-05/meeting-script.md`", "`reports/week-05/meeting-report.md`, with the deployed product and the implemented tests shown, a `DEC-nnn` for each story shown, and 2 or more action points due in Week 6", and "`reports/week-05/meeting-transcript.md`, if the meeting was recorded or held in writing" |
| S10: Redeploy and retest after same-week rework | Part 9; checklist item "Any same-week rework merged, redeployed to staging, retested, redeployed to production, and verified, or deferred to `SPRINT-06` with the reviewed commit released"; whether the released commit is the one the staging test ran and production served after the rework |
| S11: REL-05 release | Part 10 items 2–7; coverage row `REL-05`; checklist items "`REL-05` tagged on the final production commit, with its user-facing release body, the changelog's released section, the plan's `REL-05` block, and the sprint milestone closed" and "`Checked QRs` lists every `QR-nn` with at least one test checked in `SPRINT-05`, and the testing plan shows each test's result". The plan's rows are S6's; the changelog's `[Unreleased]` upkeep through the week (Part 10 item 1) is judged here as part of the released section |
| S12: Sprint close and retrospective | Part 11; the actual-velocity part of coverage row Sprint plan and milestones; coverage row Sprint retrospective; checklist item "`**Actual Velocity:**` set in `### SPRINT-05`, and `reports/week-05/sprint-retrospective.md` with its four sections and its carried actions" |
| S13: Week report and submission | Assignment Report In The Repository items 1–5; Assignment Report On Moodle items 1–7; the Submission Procedure; the 15 coverage rows, judged only as rows that exist and link; checklist items "`reports/week-05/README.md`", "Everything merged into `main`, with the permalink and the snapshot taken from that commit", and "PDF ready, the permalink opened in a browser at the full commit hash, and the production and staging addresses in it"; plus the report's summary, contribution table, repository evidence, `## Deviations`, and privacy line. The underlying artifacts are judged in S1 to S12 and S14 |
| S14: AI usage and honesty | Part 12; coverage row AI usage; checklist item "`reports/week-05/ai-usage.md`"; the AI Usage Report rules for Week 5 text |

The coverage-table rows map to the segment that judges the artifact in the row.
Whether the table has each row, and whether each row links, is judged in S13.
S10 owns the deploy-and-retest sequence and the identity of the released commit; S11 owns the tag, its protection, the release body, the changelog, the plan's block, and the milestone close, so a tag placed on a commit the sequence does not produce is reported in S10 and its own record in S11 is judged there.

## Status guide

Use the status vocabulary of `docs/compliance-feedback-format.md` and the evidence states of `docs/grading-policy.md`.
A segment is `met` only when every `met` criterion below holds on verified evidence.
A segment is `partial` when its core artifact exists and at least one verified shortfall remains.
A segment is `missing` when the `missing` criterion below holds.
A segment is `unverified` when its core evidence could not be read, such as S11 when the tags and releases cannot be read at all, or S4 when neither the runbook nor any evidence route settles which commit production ran.
Recommended items and the What Good Looks Like points are quality notes for the instructor, and they never cause a shortfall unless they coincide with a Required rule.

### S1 — Sprint plan and milestones

**Check:**

- `docs/project-plan.md` in the snapshot, its `## Milestones` and `### SPRINT-05` sections, and the path history of the file for when each field was written.
- The repository's GitHub milestones: `milestones.json` for the titles and due dates, and the raw `gh api "repos/$REPO/milestones?state=all&per_page=100"` call at procedure step 12 for each milestone's state.
- The `User Story` issues in `SPRINT-05`'s milestone and their `Story Points`, from `issue-fields.json` or the REST `issue_field_values`.
- Each `User Story`'s `milestoned` and `demilestoned` events, from `issues/<n>.timeline.json` or the `issue_events` table filtered to the planning time, for the stories the milestone held when the sprint was planned.
- The pull requests in the Week 5 window that touch `docs/project-plan.md`, for when `**Planned Velocity:**` and the milestone fields were written.

**met:**

- `### SPRINT-05` opens with the sprint's goal in one sentence, stated as a result rather than as a list of tasks, and it replaces the provisional goal the section carried before planning.
- Under the goal, `### SPRINT-05` carries `**Due:**`, `**Sprint Backlog:**`, and `**Planned Velocity:**`, in that order, as a bulleted list.
- `**Due:**` is `2026-10-31`.
- `**Sprint Backlog:**` links the `SPRINT-05` GitHub milestone, and the link resolves to the milestone whose title begins `SPRINT-05:`.
- `**Planned Velocity:**` is a whole number, and it equals the sum of the `Story Points` of the stories the milestone held when the sprint was planned, from its `milestoned` and `demilestoned` events where they exist and from its current stories otherwise; a story added mid-sprint does not change the planned figure.
- `## Milestones` holds at least two `### MLS-nn` sections whose `**Due:**` is one of `2026-10-31`, `2026-11-07`, `2026-11-14`, `2026-11-21`, or `2026-11-28`, and at least two of those due dates differ, so the two milestones are due in different sprints.
  A milestone already in that range before Week 5 counts, and the segment never requires two newly written ones.
- Each of those `### MLS-nn` headings carries the identifier alone, and the number is the milestone's due week: a milestone due `2026-10-31` is `MLS-05`, one due `2026-11-07` is `MLS-06`, and a week with no milestone leaves a gap in the sequence.
- Each milestone due in that range opens with `**Due:**`, `**Sprints:**`, and `**Advances:**`, in that order, as a bulleted list, and a description follows the fields.
- Each `**Due:**` is the hard deadline of its due week, exactly the Saturday `course/syllabus.md` gives that week, so a due week of Week 5 is `2026-10-31` and never the class week's last class day.
- Each `**Sprints:**` is a consecutive run of one or two `SPRINT-nn` sections, each linked to its section anchor, and the run ends in the sprint of the milestone's due week.
  A run may begin at `SPRINT-04` and end at `SPRINT-05`.
- The `**Sprints:**` runs of the milestones due in that range are disjoint, so no two milestones cover the same sprint.
- Each `**Advances:**` links at least one `TOS-nn` that exists in `docs/threshold-of-success.md`.
- The description's first sentence states what the increment delivers, so a reader who stops there has the milestone; a later sentence may add scope, sequencing, or the problem the increment beats, and none restates `**Sprints:**` or `**Advances:**`.
- The GitHub milestones `SPRINT-05`, `SPRINT-06`, `SPRINT-07`, `SPRINT-08`, and `SPRINT-09` exist, each titled `SPRINT-nn: <focus>` with its own number, and due `2026-10-31`, `2026-11-07`, `2026-11-14`, `2026-11-21`, and `2026-11-28`.
- `SPRINT-06` to `SPRINT-09` are open at `ISSUE_CUTOFF`. `SPRINT-05`'s state belongs to S11.
- The plan copies no issue list into the file, and no `## Milestones` entry stands for a GitHub milestone.

**What does not count:**

- A prose sentence such as "we planned about 20 points", or a rounded total, as `**Planned Velocity:**`.
- The current story set when the milestone gained or lost a story after planning: the sum must use the stories the milestone held at planning, from `milestoned`/`demilestoned` events.
- A figure copied from `SPRINT-04` or from the week report instead of the sum of the planned stories' `Story Points`.
- A plan milestone due `2026-10-29` or `2026-10-24`: the class week ends on 29 October and the previous submission's date is 24 October, while the milestone's `**Due:**` is the syllabus's hard deadline, Saturday `2026-10-31`.
- A `**Sprints:**` run written as bare `SPRINT-05` with no link, or a run of three sprints.
- A milestone description that leads with the team's task list, such as "build the deployment, write the tests, and cut the release".
- Two milestones whose `**Sprints:**` runs both name `SPRINT-05`, even when their due weeks differ.

**partial:**

- `docs/project-plan.md` has `### SPRINT-05` and a `## Milestones` section, and at least one other `met` criterion fails.
- Typical shortfalls: a provisional goal left in `SPRINT-05`; `**Planned Velocity:**` absent, not a whole number, or not the planning-time sum; a due date other than `2026-10-31`; a `**Sprint Backlog:**` link that does not resolve or points at another sprint's milestone; fewer than two plan milestones in range; both plan milestones due at one date; a milestone numbered by a week other than its due week; a field missing or out of order; `**Advances:**` that links no goal or a goal that does not exist; a description that opens with tasks; a missing sprint milestone; a `SPRINT-nn` milestone titled without its number; a sprint milestone due on a date other than its Saturday; a future sprint's milestone closed early.

**missing:**

- `docs/project-plan.md` is absent at the snapshot, or it has no `### SPRINT-05` section with a goal.

**Guardrails:**

- A sprint's due date is judged against `course/syllabus.md`, and Week 5's is Saturday 31 October 2026 with no extension and no per-team override.
- The `## Milestones` entries are **plan milestones**, which live only in the plan and carry no exit check of their own; the `SPRINT-nn` GitHub milestones are the **sprint milestones**, and the two are never the same artifact.
  A plan milestone due in `SPRINT-05` through `SPRINT-09` means a plan milestone whose `**Due:**` is the hard deadline of one of those five weeks.
- The earlier milestones' own shape is Week 3's and Week 4's and is not re-graded; this segment judges the milestones due in the five weeks and any milestone written this week.
- `SPRINT-04`'s goal, fields, and sprint milestone were Week 4's and are not re-graded; a `SPRINT-04` milestone still open at the cutoff is Week 4's release question, not this segment's.
- `**Actual Velocity:**` belongs to S12, the `#### REL-05` block to S11, and the stories' `Story Points` and assignees to S2.
- A milestone section written after the sprint started is a caveat in `**Evidence:**`, never a shortfall, unless the goal or the increment was plainly written from what happened.
- Whether `**Planned Velocity:**` was set at planning is a caveat in `**Evidence:**`, read from the plan's path history against the sprint's first story close; it is a shortfall only when the history plainly shows the number was written after the sprint's stories had closed.
- When the milestone's timeline is unavailable and the current story set differs from the planning-time set, compare the number with the stories the report or the issues place at planning, and say in `**Evidence:**` which set was used.
- A milestone due in range that is re-dated this week is accepted when its increment and its `**Sprints:**` run still match the new due week; a re-dated milestone whose run ends in a different sprint is the mismatch the rule names.
- The focus phrase in a sprint milestone's title and the milestones' content are the team's choice and are not judged.

### S2 — New stories and backlog refinement

**Check:**

- `issues.json`, `issue-fields.json`, and each new story's body, comments, timeline, and edit history, at `ISSUE_CUTOFF`.
- The `User Story` type and the `MoSCoW` and `Story Points` values, from `issue-fields.json` or the REST `issue_field_values`.
- The `milestoned` and `demilestoned` events and the `Responsible`/`Accountable` field values of every story the segment judges.
- The assignees, from the issue's `assignees` or `issue-fields.json`.
- Every `FR-nnn` and `ADR-nnn` a `### Specified by` links, for existence at the snapshot.
- The `SPRINT-05` and `SPRINT-06` GitHub milestones and the open stories in no milestone.

**met:**

- At least two `US-nn` issues were opened on or after `2026-10-23T00:00:00+03:00` and by `ISSUE_CUTOFF`, and each carries the `User Story` issue type.
- Each carries one `MoSCoW` value, one of `Must Have`, `Should Have`, `Could Have`, or `Won't Have`.
- Each carries one `Story Points` value, and no story's scope is larger than the `13` points the scale tops out at.
- Each story's acceptance criteria are checklist items of the form `- [ ] AC-nn: <criterion>` or `- [x] AC-nn: <criterion>`, numbered from `AC-01` within the story.
- Each story other than a `Won't Have` story carries `### Specified by`, and the section names each `FR-nnn` and `ADR-nnn` that specifies the story, each linked on `main`.
- Every `FR-nnn` and `ADR-nnn` a new story's `### Specified by` links exists at the snapshot, and each entry is one of those two families.
- At least one new story sits in `SPRINT-05`'s GitHub milestone and carries a `Responsible` value, an `Accountable` value naming a different member, and exactly the two assignees those values name.
- At least one other new story is refined for `SPRINT-06` and stays in the product backlog: it carries no milestone, no `Responsible` value, no `Accountable` value, and no assignees, while keeping its `Story Points`.
  When the team adds more than two new stories, at least one of them still has to be the unscheduled, refined one; a team that schedules every new story fails this criterion.
- Every open `User Story` the team places in the next two sprints' worth of the product backlog carries a `Story Points` value, has runnable acceptance criteria, and sits in no milestone.
- The stories the team places in the next two sprints' worth are unscheduled: no milestone, no `Responsible`, no `Accountable`, and no assignees.
- No story larger than `13` points is scheduled: every story in `SPRINT-05`'s milestone carries a `Story Points` value, and no scheduled story is a story the team records as needing a split.
- The `SPRINT-05` milestone holds the scheduled story and the sprint's other issues.

**What does not count:**

- A story added by the issue form without its type or its `MoSCoW` value, because the form does not apply either: the type and the field are set on the issue after it is created.
- A label such as `user-story` or `moscow:must` as a substitute for the `User Story` type or the `MoSCoW` value.
- A story scheduled in `SPRINT-06`'s milestone as the item "refined for `SPRINT-06`": refinement schedules nothing.
- An estimate on a backlog story as the whole of refinement: a story whose criteria are not runnable is not ready to schedule.
- A `Story Points` value of `0`, `20`, or `14`: the field's options stop at `13`, so a larger story is split rather than estimated.
- The `Story Points` on a story counted from a project column or from a `gh project field-list` result: the per-issue field value is the evidence.

**partial:**

- At least one new story with its `User Story` type and a `Story Points` value is readable, and at least one other `met` criterion fails.
- Typical shortfalls: fewer than two new stories; a new story missing its type, its `MoSCoW` value, its `Story Points`, or a criterion; a story with no `### Specified by`; a `### Specified by` that does not resolve or that names a `US-nn`; the new story scheduled in `SPRINT-05` without one of the two roles or with an assignee the roles do not name; a new story left in the backlog that sits in a milestone or carries a role or an assignee, or every new story scheduled and none left in the backlog; a backlog story the team places in the next two sprints without an estimate; a story over `13` points scheduled.

**missing:**

- At `ISSUE_CUTOFF` no `US-nn` issue opened on or after `2026-10-23T00:00:00+03:00` exists, or the stories that exist carry neither a type nor a `Story Points` value and no issue field can be read.

**Guardrails:**

- Every new story is judged in the Week 4 shape, and the shape itself was Week 4's rule; a defect in an older story's criteria or `### Specified by` is not re-graded here.
  The older stories are judged only for their `Story Points` and their unscheduled state where they belong to the next two sprints' worth.
- "New" means opened on or after the Week 5 window start and by `ISSUE_CUTOFF`; a story opened after the snapshot but by the cutoff counts like any other, and one opened after the cutoff is not judged.
- Refinement's quantity is the team's judgement: judge the stories the team has placed in the next two sprints' worth of the product backlog, name them, and do not require an estimate on every open backlog story.
  The assignment's "next two sprints' worth" is the planning horizon, not a numeric floor.
- The `Responsible` and `Accountable` fields, the assignees, and the milestones are read live at `ISSUE_CUTOFF`; a field value changed after the cutoff is drift and never repairs the state at the cutoff.
- A `Won't Have` story is not estimated or scheduled, so its lack of `Story Points` is not a shortfall; it still carries no roles and no assignees while it is open and unscheduled.
- An already closed issue needs no values and no assignees, and its values stay on it after it closes.
- `SPRINT-05`'s `**Sprint Backlog:**` link and its planning-time contents are S1's; this segment judges the story that is scheduled and the items left unscheduled.
- Whether the issue forms and the issue fields exist at all was Week 2's and Week 3's rule; a team whose organization cannot create them declares a deviation, and that declaration is judged in S13.
- A story added to `SPRINT-05` mid-sprint is a shortfall here only when it was neither refined nor estimated.

### S3 — Automated tests and CI checks

**Check:**

- Every workflow file under `.github/workflows/` and the composite actions under `.github/actions/` in the snapshot, read as YAML.
- `docs/definition-of-done.md`'s `## Pull Request` list in the snapshot.
- `runs_main.json` for the latest run of each required workflow on `main`, and `runs_sha.json` for the runs on the snapshot SHA.
- The testability quality requirement's named critical modules, the test files that cover them under the product's test directories, and the workflow step that runs the suite.
- `paths/.github/workflows/<file>.json` and the pull requests that added or changed each workflow, when the workflow's history matters.

**met:**

- At least one workflow runs `actionlint` over `.github/workflows/` on `pull_request` and on every push to `main`.
- `actionlint` is pinned: the action that runs it is pinned to a full 40-character commit SHA with its version in a trailing comment, or, when a workflow installs `actionlint` itself, the installed version is pinned in the command or the lockfile.
- A product-code workflow exists with continuous integration for the product, on `pull_request` and on `main`, and every third-party action it uses is pinned to a full 40-character SHA with its version in a trailing comment.
- For each of the five checks that applies to the stack, the workflow carries a named step that runs that check: linting, formatting, type checking, build, and automated tests.
  A step named after two checks counts only for the check its command actually runs.
- Each of the five checks that does not apply is recorded as not applicable with its reason in the same workflow, beside the checks that do, so the omission is readable beside the steps rather than only in the report.
- The automated tests include at least one test for each critical module the testability `QR-nn` names by repository path, so a broken module fails the suite.
- The tests run from a clean checkout: the job checks the repository out fresh and runs the suite in that job, with no restored workspace, no cached build output, and no step that skips the suite.
- The workflow stops at the build and the tests: no job checks out and then reaches the university network, no job runs a deploy, and no job runs `ssh`, `scp`, or a remote command on the VM.
- `docs/definition-of-done.md`'s `## Pull Request` list names `actionlint` and the applicable product-code checks among the checks that must be green, beside the link check and the Markdown check.
- The latest completed run of every required check on `main` at `ISSUE_CUTOFF` is `success`: the link check, the Markdown check, `actionlint`, and the product-code workflow.
- Every required check's workflow runs on `pull_request` and on a push to `main`, and no required check runs only on `workflow_dispatch` or a schedule.

**What does not count:**

- One job or step that runs a linter, cited as the whole product-code CI when formatting, type checking, the build, or the tests also apply to the stack.
- A step named "Run tests" whose command is `npm test --if-present`, `pytest || true`, or a placeholder assertion that passes with no test.
- `continue-on-error: true`, `if: false`, or a shell `|| true` on a required step.
- An action pinned to `@v2`, `@main`, or a branch, instead of a commit SHA.
- A job named `actionlint` with no `actionlint` invocation, or a `markdownlint` run cited as `actionlint`.
- A green run on a branch other than `main`, a run on a pull request, or a queued or in-progress run at the cutoff, as the latest green `main` run.
- The workflow's run list page or a job URL as the evidence for a run: the segment needs the run itself, or the report's link to it in S13.
- A `docs/definition-of-done.md` that names "the product code checks" in prose without naming `actionlint` and the applicable checks.

**partial:**

- `actionlint` or a product-code workflow exists on pull requests and `main`, and at least one other `met` criterion fails.
- Typical shortfalls: `actionlint` only on pull requests or only on `main`; an unpinned action; a missing named step for an applicable check; a non-applicable check silently absent; no test for a critical module; a suite that runs against a restored workspace; a deployment job; a Definition of Done list without `actionlint` or without the product-code checks; a red or missing `main` run of a required check; a required check that no event triggers.

**missing:**

- At the snapshot no workflow runs `actionlint`, and no workflow runs the product's checks, so the product CI is absent.

**Guardrails:**

- The five checks are the ones that apply to the stack: a documentation-only or frontend-only product legitimately marks type checking or the build not applicable, and the reason is what the rule requires, not a particular set of five steps.
  A step that runs is a check that applies; a check the workflow records as not applicable is judged by its recorded reason, and a reason that names the stack is enough.
- `actionlint` is read from the workflow that runs it, not from a local `pnpm run lint:actions` or a Git hook; the required evidence is the workflow and its `main` run.
- The product-code workflow's name, its job names, its cache use, and its runner are the team's choice; only the trigger, the pinned actions, the named steps, the clean checkout, and the absence of a deploy are judged.
- The clean-checkout criterion is about the job that runs the suite: a job that restores a prebuilt workspace or skips the tests does not satisfy it, and a cache of package dependencies is not a restored workspace.
- "No test for a critical module" is judged against the paths the testability `QR-nn` names at the snapshot; when that requirement names no repository path, the criterion cannot hold, and the shortfall is S5's requirement shape, with S3 judging the suite it can see.
- The latest `main` runs are judged at `ISSUE_CUTOFF` for their conclusion, and the report's links to those runs belong to S13; a workflow whose latest `main` run is green but whose earlier run was red is correct.
- The link check and the Markdown check were Week 1's and Week 2's; here only their continued existence, their green `main` state, and their place in the Definition of Done are judged.
- A workflow change made after `ISSUE_CUTOFF` is drift and never repairs the state at the cutoff.

### S4 — Deployment and environments

**Check:**

- `docs/deployment.md`, `.env.example`, and `docs/setup.md` in the snapshot.
- `reports/week-05/README.md` and every week-local file it links, for the deployment record and the core-task verification.
- The testing plan's `deployed` or fallback row and its evidence, for the commit staging ran.
- The meeting report and the meeting script, for what was shown and from where.
- Issue, pull-request, and commit messages in the Week 5 window that record a deploy, a rollback, or a verification.
- Screenshots under `reports/week-05/images/`, with `scripts/image_info.py` when a file's size or transparency matters.
- The Moodle PDF's staging and production addresses and its note about the university network, read once.

**met:**

- `docs/deployment.md` exists and names the four environments, with what runs in each: development on the team's machines, integration in the product CI, staging on the university VM, and production on the university VM.
- It describes the VM and its access: the machine from the university portal, recreated from the portal's image, its password set by the team, and a connection over SSH from a machine on the university network.
- It says there is no domain name and that the customer reaches production from the university network at the VM's IPv4 address.
- It makes staging and production separate deployments on separate ports, with separate configuration, separate secrets, and separate data, so a command aimed at one fails against the other.
- It carries the configuration's shape, with `.env.example` holding placeholders, and says the real values are installed on the VM outside the repository.
- It gives the manual deploy from a campus machine: the release candidate to staging first, then the same commit to production, with the commands a teammate runs.
- It records the core-task verification after a production deploy: what was checked, on production, from a campus machine, and on which commit.
- It gives the rollback: how a deploy that fails its verification returns to the previous release, with the command, and where the previous release comes from.
- It links `docs/setup.md` for the build and the run and repeats none of its install, build, or run steps.
- `docs/deployment.md`, `.env.example`, and the other files this segment reads carry no real IPv4 address, host name, domain name, password, token, or secret; every command that needs one reads a placeholder such as `<university-vm-ipv4>` or an environment variable such as `$STAGING_URL`.
- The runbook names where to get the address rather than giving it, so a teammate substitutes the value from the Moodle submission; the report's pointer and a leak in the report's own text are S13's, and a leak in a test's `**Runs at:**` or procedure is S5's.
- The week's deployment is recorded: staging and production ran the same commit in the Week 5 window, the production deploy was verified on the core task, and the record names the commit or the release.
  A runbook section, the week report, a deployed test's evidence, an issue or pull-request comment, a dated screenshot, and the meeting report are each acceptable evidence for this criterion.
- The real staging and production addresses are in the Moodle PDF.
- When the VM was not available, the postponement and the date the group chat announced are recorded, `## Deviations` declares the deviation, and the rest of the week's deployment evidence is judged against that declaration.
  That path satisfies this segment, and its consequence for the second test's level is S5's and S6's.

**What does not count:**

- A `docs/deployment.md` that copies the install and run steps of `docs/setup.md`, as a second copy that drifts from the first.
- A deployment document that stops at the first successful deploy and carries no rollback.
- A runbook that names the VM's address, host name, or password, or a `.env` committed as the configuration.
- An invented domain name, such as `https://booking.example.com`, in the runbook or the report.
- A claim that the product is deployed, with no record of a staging or production run, no verification, and no declared deviation.
- The CI workflow as the deployment: the product CI cannot reach the university network, and the deploy is manual from a campus machine.
- A staging deploy of one commit and a production deploy of another, presented as the same commit; the rework sequence that moves both is S10's.
- A screenshot of a page with no explanation, as the evidence for the core-task verification.

**partial:**

- `docs/deployment.md` exists with the four environments, and at least one other `met` criterion fails.
- Typical shortfalls: an environment missing or misnamed; no campus-network access described; one deployment on one port; a shared configuration or secret between staging and production; no rollback; a verification record that names no commit; the runbook copying `docs/setup.md`; an address, host name, or secret in a public file; a deployment claim with no record; the addresses absent from the PDF.

**missing:**

- `docs/deployment.md` is absent at the snapshot, or it does not describe the deployment at all.

**Guardrails:**

- The deployment is judged from the runbook plus the evidence routes this segment lists, not from one screenshot: a runbook that a teammate could follow and a record that the deploy happened are two criteria, and either may fail alone.
- The real addresses are Moodle-only, so the runbook's job is to name where to get them; the PDF's own shape, page count, and item list belong to S13, and this segment reads the PDF only for the addresses and the network note.
- An address that does not respond, or a staging instance that is not reachable from the agent's network, is an evidence gap for that check only, after the single access check `docs/grading-policy.md` allows.
  The runbook, the deploy record, and the verification are still judged, and an unreachable external view is never by itself a shortfall.
- A VM that was unavailable with a declared deviation and a recorded postponement is the assignment's own fallback and is not a shortfall; a VM claimed but never reached, with no deviation, is.
- A deployment claim that cannot be reached and that no other evidence route supports is a shortfall here; the same claim repeated in the week report is judged once, in this segment.
- The integration environment is the product CI and not a third deployment; a team that runs only staging and production still names integration as the CI.
- `docs/setup.md` was Week 3's artifact and is not re-graded; this segment judges only the runbook's link to it and the absence of a second copy.
- The staging deployment's use by a `deployed` test is S5's and S6's; this segment judges that staging exists, is separate, and is reachable.
- A deploy, rollback, or fix made after `ISSUE_CUTOFF` is drift and never repairs the state at the cutoff.

### S5 — Quality requirement tests

**Check:**

- Every `docs/quality-requirements/qr/QR-nn.md` in the snapshot, for its `## QRT-nn` sections and its fields.
- `docs/quality-requirements/README.md` for the matrix's active rows, their `Business importance` values, and their sort order.
- The workflow and step a test's `**Runs at:**` names, in the snapshot's `.github/workflows/`.
- The scripts, commands, and tools a `scripted` or `deployed` test names, in the snapshot.
- The testability requirement's named critical modules and the suite's tests for them, in the snapshot.
- `reports/week-05/README.md`'s `## Deviations` and the plan's deviations, for a `manual` test and for the next-active-row case.

**met:**

- Every active `QR-nn` whose `**Business importance:**` is `High` carries at least one `## QRT-nn` section.
- A `## QRT-nn` section sits inside its requirement's file, after the requirement's `## Scenario`, and its heading is the bare identifier `## QRT-nn`, numbered from `QRT-01` within that requirement.
- The first line below the heading is the test in one sentence, stating what must hold about the product rather than how it is checked.
- Each test carries its fields in the order `**Status:**`, `**Level:**`, `**Runs at:**`, then `**Why Manual:**` only on a `manual` test and `**Dropped:**` only on a dropped test.
- Every `**Status:**` is `Active` or `Dropped`, and no `**Status:**` holds a result such as `Passes` or `Fails`.
- Every `**Level:**` is one of `CI`, `scripted`, `deployed`, or `manual`, and it matches the environment the level names: integration for `CI`, development for `scripted`, staging for `deployed`, and no environment for `manual`.
- Every `**Runs at:**` names what runs the test in one line: the workflow and its step for a `CI` test, the script path or command for a `scripted` test, the staging deployment with the command or tool for a `deployed` test, and the inspection step for a `manual` test.
- A `deployed` test's `**Runs at:**` names the staging deployment and never production, and every address in its command or procedure is a placeholder or an environment variable such as `$STAGING_URL`.
- The testability requirement's test is a `CI` test whose `**Runs at:**` names the workflow step that runs the product's suite from a clean checkout.
- A second implemented test exists, on one other active requirement, at `CI`, `scripted`, or `deployed`, and it is not a `manual` test.
  It sits on a `High` business-importance requirement other than the testability one whenever the matrix has another such requirement.
- When the matrix has no other active `High` requirement, the second test sits on the next active row by the matrix's sort, and the week report's `## Deviations` names that requirement and says the matrix has no other `High` row.
- Every `manual` test carries `**Why Manual:**` in one sentence saying why no command can check the requirement, and the week report's `## Deviations` declares it and names the requirement.
- The two implemented tests are at least two distinct `QR-nn QRT-nn` pairs, and the testability requirement's test counts as one of them.
- Every test carries a `### Procedure` whose numbered list is the steps a stranger runs, names where the runner stands, and ends with the output the reader reads.
- Every test carries exactly one `**Pass when:**` line after the procedure, and it is one comparison against the threshold the requirement's `Response Measure` states, in the requirement's units and interval.
- No test carries a result, a checked sprint, an evidence link, or a last-check field: the test is the definition, and the plan's row is the result.
- A dropped test keeps its section with `**Status:** Dropped` and a `**Dropped:**` field giving the date and the reason, and its pair is never reused.
- Every test is cited as the pair `QR-nn QRT-nn`, and a link to it uses its requirement's path and its `#qrt-nn` anchor.

**What does not count:**

- A `**Status:** Passes` or `**Result:** Passes` on the test, or an `**Evidence:**` bullet holding the run's URL: the result and the evidence belong to the testing plan's row.
- A test that restates the requirement, such as "the booking page is fast enough", instead of naming what is done, against what, and which output settles the verdict.
- A `manual` test offered as the second implemented test, or a `deployed` test that is a person looking at a page and deciding it works.
- A `deployed` test run against production, or one whose command carries the real staging address.
- A `**Runs at:**` of `CI` alone, of "the tests", or of a workflow name with no step.
- A `**Pass when:**` with two checks and one verdict, such as "it loads fast and shows no errors", or one that changes the requirement's units.
- A test on a `Medium` or `Low` requirement as the second implemented test when the matrix has another active `High` requirement.
- A `QRT-01` heading in a file whose requirement has no `## Scenario`, or a test placed above the scenario.

**partial:**

- At least one active `High` requirement carries a `## QRT-nn` section, and at least one other `met` criterion fails.
- Typical shortfalls: one `High` requirement with no test; a test above the scenario or with a named heading; a field missing or out of order; a level outside the four; a `**Runs at:**` that names no step; the testability test not `CI` or not from a clean checkout; no second implemented test; the second test `manual` or on the wrong requirement without a declared deviation; a `manual` test without `**Why Manual:**` or without the deviation; no `### Procedure`; no `**Pass when:**` or more than one; a result or evidence kept on the test; the pair cited as a bare `QRT-nn`.

**missing:**

- `docs/quality-requirements/qr/` is absent at the snapshot, or no active `High` business-importance requirement carries a `## QRT-nn` section.

**Guardrails:**

- The matrix's `Business importance` decides which requirements need a test: a `High` `Technical risk` does not make a requirement high-priority for this rule, and a `Medium` or `Low` requirement may carry a test without being required to.
- A requirement whose `**Status:**` is `Dropped` needs no test, and a dropped test's section stays in its file so the pair is never reused.
- The second implemented test may sit on the testability requirement only when the matrix has no other active `High` row, and the deviation is what makes that correct; without the deviation the criterion fails.
- The fallback the assignment allows when staging is not available is written at the level that can run, `CI` or `scripted`, with that run recorded; a test left `deployed` with no run keeps its row `Not verified` and the sprint the VM is now expected in, and that row never becomes a `Passes`.
  Both forms declare the deviation, and the level, `**Runs at:**`, and row change together.
- The assignment prefers `deployed` for the second test when staging is available; a `CI` or `scripted` second test is correct when the VM's staging is not there and the deviation is declared, and the preference alone is never a shortfall.
- A `deployed` test is automated: a person deciding from a page that looks right is a `manual` test without its `**Why Manual:**`, and it cannot be the second implemented test.
- The test's numbering restarts at `QRT-01` inside each requirement, so two requirements both carrying a `QRT-01` is correct; the pair is what identifies one.
- The procedure's wording, the test's title, and the tool it names are the team's choice; only the fields, the level, the procedure's runnability, and the one comparison are judged.
- Whether a test that passes is a strong test is a quality note; whether the `**Pass when:**` copies the response measure is the check.
- `docs/quality-requirements/README.md`'s own columns and sort were Week 4's and are not re-graded here; this segment reads the matrix for the active rows and their priorities, and its link to the plan is S6's.

### S6 — Testing plan and results

**Check:**

- `## Quality Requirement Testing Plan` in `docs/project-plan.md` at the snapshot, its columns, its rows, and their order.
- Every `## QRT-nn` section in `docs/quality-requirements/qr/`, for the rows the plan must carry.
- `docs/quality-requirements/README.md`, for its sort order and its one link to the plan.
- The evidence each row's `Evidence` cell links, in the snapshot or in the live runs.
- The `SPRINT-05` section of the plan, for the `#sprint-05` anchor the `Checked` cells use.
- The report's summary line that points at the plan, for S13's criterion rather than this segment's.

**met:**

- `docs/project-plan.md` carries a `## Quality Requirement Testing Plan` section with one row per `QRT-nn` in the repository, and no test without a row and no row without a test.
- The table's columns are `QR`, `QRT`, `Status`, `Checked`, `Planned for sprint`, and `Evidence`, in that order.
- The rows follow the order of the quality requirements index, and a test's number breaks a tie within one requirement.
- Each `QR` cell is the identifier as link text, linked to its file under `qr/`, and each `QRT` cell is the pair as link text, linked to its section's `#qrt-nn` anchor.
- Every `Status` is `Passes`, `Fails`, `Not verified`, or `Dropped`.
- Every `Checked` is the `SPRINT-nn` of the run, linked through the plan such as `[SPRINT-05](#sprint-05)`, and `None` on a `Not verified` or `Dropped` row.
- Every `Planned for sprint` is exactly one `SPRINT-nn`, linked through the plan, and `None` on a `Dropped` row.
- Every `Evidence` cell on a `Passes` or `Fails` row links the proof its level requires, and holds no output, number, or command text of its own.
- The testability requirement's `CI` row is `Passes` with `Checked` in `SPRINT-05`, and its `Evidence` links the run on `main` the level requires.
- The second implemented test's row is `Passes` with `Checked` in `SPRINT-05`, and its `Evidence` links the proof its level requires: a CI run, a scripted command with its output in the week's evidence, or a staging run with its measured value and commit.
- Every other row keeps its result: a `Fails` row keeps its `Checked` and its evidence, a `Not verified` row keeps its planned sprint, and a `Dropped` row has `None` for `Checked`, `Planned for sprint`, and `Evidence`.
- `docs/quality-requirements/README.md` links `docs/project-plan.md#quality-requirement-testing-plan` once.
- A `scripted` or `deployed` row's `Evidence` points at a dated section of `reports/week-05/README.md` or at a week-local file the report links, and that section or file holds the command or tool, the output, the measured value, and the commit when the level is `deployed`.
- The plan carries no priority column and no copied test procedure, and the `Checked` sprint of each row is the sprint the test last ran.

**What does not count:**

- Output pasted into an `Evidence` cell: the cell is a link, and a pasted table is a second copy that cannot be checked against its run.
- A row with `Checked: SPRINT-04` whose test the team did not rerun this sprint, presented as a `SPRINT-05` result.
- A `Passes` row with no evidence, or one whose evidence is a screenshot of a page with no measured value on a `deployed` row.
- A plan table with the columns in another order, an extra priority column, or rows grouped by status instead of by the index's order.
- A `QRT` cell that names only `QRT-01`, without its requirement, so two rows cannot be told apart.
- A `Checked` cell holding a bare `SPRINT-05` with no link, or a `Planned for sprint` holding two sprints.
- The quality requirements index linking the plan twice, or linking it from a weekly report instead: the index's one link is the criterion.

**partial:**

- The plan table exists with its rows, and at least one other `met` criterion fails.
- Typical shortfalls: a missing column or a column out of order; a test with no row or a row with no test; rows out of index order; an unlinked `QR` or `QRT` cell; an invalid `Status`; a `Checked` value that is not the run's sprint; a `Passes` row of the testability or other implemented test with `Checked` in an earlier sprint; missing evidence or pasted output; a `Dropped` row that keeps a planned sprint; a `Fails` or `Not verified` row whose result was cleared; no index link or two of them.

**missing:**

- `docs/project-plan.md` is absent at the snapshot, or it carries no `## Quality Requirement Testing Plan` section at all.

**Guardrails:**

- The plan is the one place a test's result lives: the test's section carries the definition, and this table carries the run, so a result on both is the drift the rule names.
- "Checked in `SPRINT-05`" means the `Checked` cell names `SPRINT-05`; a requirement whose only test last ran in an earlier sprint is not a checked requirement for this sprint, and that distinction is also what S11's `Checked QRs` list reads.
- The evidence's form follows the level: a `CI` run on `main`, a `scripted` command and its output, a `deployed` run with the staging environment, the measured value, and the commit, or a `manual` inspection with who looked and what was seen.
  A screenshot that carries a measured value may support a `deployed` row, and a screenshot alone is an inspection.
- An address in a `deployed` row's evidence is a placeholder or an environment variable, and a real address there is a visibility shortfall in this segment.
- The report's pointer at the plan, its summary's reference to the rows that are not `Passes`, and its rule against copying rows are S13's, which owns the report; a row that the report copies is reported there.
- The index's own columns, sort, and status column were Week 4's and are not re-graded; this segment judges only the one link to the plan.
- A row whose test is planned for a later sprint is correct with `Not verified`; do not require every row to be `Passes`.
- A `Fails` row is a correct record and is not a shortfall by itself; the week's review reads it, and only its missing result or cleared evidence is the shortfall.
- A test that a team dropped this week keeps its row with `Dropped` and three `None` values, and the row is not deleted.

### S7 — Feature documentation

**Check:**

- `docs/features.md` in the snapshot, its intro, each `##` entry, and its bullets.
- `docs/glossary.md`, for the terms an entry's opening sentence links and the anchor each link uses.
- Every `US-nn`, `FR-nnn`, and `ADR-nnn` an entry links, for existence and for the record's own facts.
- `prs.json`'s `files` and the `pr_files` table, for the pull request that changed a linked record and whether it also touched `docs/features.md`.
- The path history of `docs/features.md`, for when each entry arrived.

**met:**

- `docs/features.md` exists and carries at least three `##` entries, or every capability the product has when it has fewer than three.
- The intro carries one line that links `docs/glossary.md` as the route to the words the project uses in its own sense.
- Each entry is one `##` section headed with the capability's name in sentence case, so its anchor is `#<capability>`, and the heading carries no link.
- The entries form one flat list in the order a reader should meet the product, with no role grouping, no sub-headings per role, and no `**Users:**` field.
- The first line under each heading is one sentence in the user's language saying what a user can do, and it describes a capability rather than a screen, a table, or a service.
- That sentence names no `US-nn`, `FR-nnn`, or `ADR-nnn`.
- Every word `docs/glossary.md` defines links to its term at its first use in that sentence, and each link resolves to an existing anchor.
- Below the sentence, each entry carries a `- **Stories:**` bullet whose links reach the stories that carry the need, and a `- **Behavior:**` bullet whose links reach the `FR-nnn` files that own the capability, in that order.
- An entry carries `- **Decisions:**` when the capability has an `ADR-nnn` that shapes it, each linked, and omits the field when it has none rather than writing `None` or `TBD`.
- Every link in every bullet resolves at the snapshot, and the page restates no behavior an `FR-nnn` owns and no acceptance criterion a story or requirement carries.
- The page was updated in the same pull request as the change it reflects: a Week 5 pull request that adds an `FR-nnn`, changes an `ADR-nnn`, renames a glossary term an entry uses, or adds a capability also changes `docs/features.md` in that pull request.
- Every capability the product gained in Week 5 has its entry, and an entry whose record was superseded links the new record rather than the old one.

**What does not count:**

- A page that lists artifacts rather than capabilities, such as "the booking service" or "the deployment", as its entries.
- An entry whose opening sentence describes a screen or a data model, such as "the booking page validates the slot form".
- An entry that copies its `FR-nnn`'s `shall` statements or its story's `AC-nn` criteria into the page.
- A `**Users:**` field, a `## For coaches` grouping, or a second list of entries by role.
- A glossary line that defines the project's terms on the page instead of linking `docs/glossary.md`.
- A term whose first use in the sentence is unlinked, with its link added later in the same sentence or in the bullets.
- An `FR-nnn` or `ADR-nnn` that the entry links but that does not exist, or a story link that points at an issue number that is not that `US-nn`'s issue.
- A `docs/features.md` written once and never touched while its linked records changed in Week 5's pull requests.

**partial:**

- `docs/features.md` exists with at least one capability entry, and at least one other `met` criterion fails.
- Typical shortfalls: fewer than three entries when the product has more; no glossary line; a heading that is a sentence, a title in Title Case, or linked; a role grouping; an opening sentence that names an identifier or describes a screen; a missing first-use term link; a missing `**Stories:**` or `**Behavior:**` bullet; a linked record that does not exist; a restated behavior or criterion; a `None` under `**Decisions:**`; an entry that missed the pull request that changed its record.

**missing:**

- `docs/features.md` is absent at the snapshot.

**Guardrails:**

- A feature is a capability, not an artifact: the team's set of capabilities is its own judgement, and the count is a minimum, so a page with four entries and three capabilities is not short by one.
  A capability with no story or no functional requirement is not ready to be documented, and the missing record is S2's or the requirement's own segment, not this one's.
- The sentence-case rule is broken by Title Case in a heading and by a heading that is a sentence; the anchor is the citation form, so a heading that reads well is enough.
- The `**Stories:**` link reaches an issue, and the issue's number is the link's target; an entry may name several stories, and an entry with one is correct.
- The same-pull-request rule is judged from the pull request's files and merge time against the record it changed; a formatting-only touch of `docs/features.md` in an unrelated pull request is a quality note, and a record changed in Week 5 with the page untouched is the shortfall.
- A record changed before Week 5 with the page written in Week 5 is correct: the page is created this week, and the same-pull-request rule binds from the page's first commit on.
- The glossary's own shape was Week 4's and is not re-graded; this segment judges the term links the page uses and that the anchor exists.
- The report's coverage row that links this page is S13's, and its absence is a shortfall there, not here.
- The page's length, its prose, and the order of its entries beyond "one flat list" are quality notes.

### S8 — Week 4 action points and open questions

**Check:**

- `reports/week-05/meeting-report.md`, its `## Previous action points` and `## Previous open questions`.
- `reports/week-04/meeting-report.md` at the snapshot, for its `## Action points` rows due in Week 5 and every row of its `## Open questions`.
- Every artifact and task issue an `Outcome` or `Answer` cell links, and every `DEC-nnn` entry a `Decision` cell names.
- `docs/decisions.md`, for the entries a `Decision` cell links and their `**Source:**`.

**met:**

- `reports/week-04/meeting-report.md` exists in the snapshot and its `## Action points` and `## Open questions` can be read, or the Week 5 report says there were none.
- `## Previous action points` has the columns `Action`, `Outcome`, and `Decision`, with one row per Week 4 action point due in Week 5 or carried out early.
- Every `Action` cell cites `reports/week-04/meeting-report.md#action-points` with the action quoted.
- Every `Outcome` says whether the action point was carried out and what was found, or why it was not, and links each artifact and task issue it changed.
- Every artifact an `Outcome` says changed holds that change, and the change is dated no later than `ISSUE_CUTOFF`.
- An action point not carried out reappears in the Week 5 `## Action points` with a new due week, unless its `Outcome` says the team or the customer dropped it. The due week's window is S9's, so a reappearance outside Week 6 is not a second shortfall here.
- Every `Decision` cell links the `DEC-nnn` the outcome produced, or says `None`, and every linked entry exists with a `**Source:**` that points at where the decision was made.
- `## Previous open questions` has the columns `Question`, `Answer`, and `Decision`, with one row per Week 4 open question not yet closed, and every Week 4 open question is either answered there or carried into the Week 5 `## Open questions`.
- Every `Question` cell cites `reports/week-04/meeting-report.md#open-questions` with the question quoted.
- Every `Answer` says what the work or the meeting found and links each artifact the answer changed.
- No Week 4 action point or open question is silently dropped: one that the team no longer intends to do is `Dropped` in its `Outcome` or carried forward, and one the meeting answered is answered with its `DEC-nnn`.

**What does not count:**

- An `Outcome` that says "done" with no artifact and no task issue linked, while the artifact it should have changed is unchanged.
- A citation by number alone, such as "action 2", without the report's path, the `#action-points` anchor, and the quoted action.
- A Week 4 open question that is neither answered in `## Previous open questions` nor carried into `## Open questions`.
- A `Decision` cell naming a `DEC-nnn` that does not exist, or one whose `**Source:**` points at another meeting.
- A Week 5 report that edits the Week 4 report to close its rows there.

**partial:**

- The Week 5 report has both `## Previous` sections, and at least one other `met` criterion fails.
- Typical shortfalls: an action point due in Week 5 with no row; an outcome that exists only in the table, with the artifact unchanged; an action point not carried out that does not reappear; a Week 4 open question with no row and no carry-forward; a citation without the quoted action; an `Outcome` naming a task issue that does not exist; a `Decision` cell that links nothing and does not say `None`.

**missing:**

- `reports/week-05/meeting-report.md` is absent at the snapshot, or neither `## Previous action points` nor `## Previous open questions` is present when the Week 4 report has rows for it.

**Guardrails:**

- When the Week 4 report has no action point due in Week 5 or no open question, `None` in the matching section is correct.
- Do not re-grade the Week 4 report; judge only what Week 5 did with its rows.
- An outcome carried into an artifact is judged by whether the artifact changed, not by whether the change is large.
- An action point the customer dropped stays closed, and the customer's decision is cited.
- A Week 4 report edited in Week 5 is a quality note unless its content was rewritten; a formatting-only change is allowed.
- A Week 4 open question the work has not answered belongs in the Week 5 meeting's questions; when the report carries it forward without an answer and the script does not ask it, report it here as a shortfall.
- The Week 5 `## Action points` table's shape and due dates belong to S9; this segment judges the reappearance of an open action point, not the table.
- An action point due in Week 6 but carried out this week may close here, and the row is correct.

### S9 — Customer validation of the deployed product

**Check:**

- `reports/week-05/meeting-script.md`, `reports/week-05/meeting-report.md`, and `reports/week-05/meeting-transcript.md` when it exists, in the snapshot.
- The path history of the script, for whether it was committed before the meeting.
- Every `DEC-nnn` in `## Decisions`, in `docs/decisions.md`, and every story issue the meeting showed or changed, with its comments, timeline, and edit history.
- The meeting artifacts for a recording link or timecode, and the Moodle PDF's transcript appendix when the customer refused publication; the recording link's access check is S13's, and the transcript appendix is read here only to see that no transcript leaked into the repository.
- The quality requirements index, the architecture document, the testing plan, and the other implemented test's evidence, for what the meeting showed.
- The deployed production instance, after the single access check `docs/grading-policy.md` allows.

**met:**

- The script has exactly the sections `## Context`, `## Agenda`, `## Questions`, `## Roles`, and `## Key improvements`, in that order, with `## Roles` left out only for a meeting held in writing, and every empty section says `None`.
- `## Context` gives the problem-space sentence, what the team believes, and a one-sentence target that covers whether the deployed product does what the stories say, which quality requirements hold at the levels their tests run, and what comes next.
- `## Agenda` is a numbered list whose first part asks the three permission questions, whose last part reads back the decisions and action points, and whose parts each have a timebox that adds up to the planned length, or, for a meeting held in writing, the order of the exchange and what is sent with each part instead of timeboxes.
- The agenda shows the production deployment reached from the university network, then the testing plan's rows and the other implemented test at its level, and asks for the customer's verdict on each story.
- Every agenda part names what is shown, with a link or a statement that nothing is shown, and every question appears in exactly one part.
- `## Questions` is numbered, every question is tagged open or closed, and every question serves the target.
- `## Roles` names a moderator, a note taker, and an observer by GitHub username, and a written meeting omits the section.
- `## Key improvements` records at least one rewritten question with the before, the after, and the principle.
- The script was written before the meeting it prepares: its first commit is on or before the meeting date in `## Metadata`, and a same-day commit is accepted when the history shows it came before the meeting; its later commits are formatting-only changes.
- The report has exactly the sections `## Metadata`, `## Previous action points`, `## Previous open questions`, `## Summary`, `## Decisions`, `## Action points`, `## Open questions`, and `## Disagreements`, in that order, and every empty section says `None`.
- `## Metadata` is a bulleted list of `- **Label:** value` bullets giving the date, the duration, the attendees by GitHub username with the customer as `Customer`, what was presented, the answer to each of the three permission questions, the transcript link or `None` with the reason, and the script link.
- The report's `## Metadata` or `## Summary` says the meeting showed the deployed production instance on the university VM, reached from the university network, and names what was shown.
  When the VM was unavailable, it says the team showed the local product and the deployment plan and declares the deviation.
- The meeting shows each implemented test's result at its level: the testability requirement's `CI` run and the other implemented test's result against staging, or its fallback level's result, with the commit and the measured value.
- `## Summary` has 3 to 5 bullets on what the meeting settled or changed.
- `## Decisions` lists at least one `DEC-nnn` entry of the form `[DEC-nnn: <the entry's first line>](../../docs/decisions.md#dec-nnn)`, and every change the customer made has a `DEC-nnn` entry in `docs/decisions.md` naming what it changed, made by `Customer` or `Team, not contested`, with a `**Source:**` linking this report.
- Every story the meeting showed has a verdict recorded as a decision naming its `US-nn`, and an accepted story has closed with a comment that cites its verdict's `DEC-nnn` and names the `AC-nn` it was accepted against.
- A rejected story's verdict names each `AC-nn` it failed, the story stays open, and its rework task names the story and the failed `AC-nn`.
- Every story issue the meeting showed, accepted, rejected, or changed has a comment dated on or after the meeting that names the verdict or the change, names each `AC-nn` affected, and links the `DEC-nnn` on `main`.
- `## Action points` has the columns `Action`, `Owner`, and `Due`, at least two rows, an owner given by GitHub username, and every due date inside the Week 6 class week, such as `End of Week 6` or a date from 30 October to 5 November 2026; the 7 November submission deadline is not that window.
- `## Open questions` has the columns `Question`, `What it would change`, and `Follow-up`; `## Disagreements` has the columns `Your position`, `Customer's position`, and `What you changed`, and every row that changed nothing says why the team kept its position.
- The meeting was held in the Week 5 window, between Friday 23 October 2026 and `ISSUE_CUTOFF`, and a meeting held in writing says so and carries no `## Roles` section.
- Every meeting artifact names the customer `Customer` and identifies people only by GitHub username.
- When the meeting was recorded or held in writing, and publication was permitted, `reports/week-05/meeting-transcript.md` exists, opens with the date and the participants as `- **Label:** value` bullets above the first timestamped line, with a `#` title allowed above them, and then has one sentence per line in the form `[hh:mm:ss] <label>: <sentence>`, labels speakers by GitHub username and `Customer`, marks gaps with `[inaudible]` or `[redacted]`, and carries no personal data.
- When publication was refused, no transcript is committed, and the report's `## Metadata` says the transcript is Moodle-only; the PDF's appendix is S13's item.
- No meeting artifact carries a recording link or a recording timecode: the recording link and the timecodes are Moodle-only, per the visibility rule.

**What does not count:**

- An agenda that shows only the local product without the VM's production instance, when the VM was available, and without a declared deviation.
- A test's result reported as "the tests pass", with no level, no commit, and no measured value.
- A verdict recorded only in the report's table, with no `DEC-nnn` entry and no story comment.
- A transcript written one speaker turn per line when a turn carries several sentences: that is not the one sentence per line the rule requires.
- A script whose first commit is after the meeting date, or a same-day commit the history cannot place before the meeting.
- A script or transcript rewritten after the meeting, or edited after `ISSUE_CUTOFF`, as the pre-meeting form.
- A transcript that says the customer refused publication but sits in the repository.
- A test result shown against production as a `deployed` test's run.

**partial:**

- `reports/week-05/meeting-report.md` exists, and at least one other `met` criterion fails.
- Typical shortfalls: a missing or extra section; no permission part in the agenda; the agenda showing neither the deployment nor the implemented tests; a story shown with no `AC-nn` verdict; a verdict decision that does not name its `US-nn`; a change with no `DEC-nnn`; an action point due outside Week 6; a script committed after the meeting; a published transcript without permission; a recording link or timecode in a meeting artifact; personal data in a meeting artifact; a report that restates the transcript line by line; the VM fallback claim without the deviation.

**missing:**

- `reports/week-05/meeting-report.md` is absent at the snapshot, or no Week 5 meeting with the customer took place.

**Guardrails:**

- When the Week 4 report has no previous action points or open questions, `None` in the matching section is correct.
- Do not re-grade the Week 4 script, report, or transcript.
- The weekly meeting is the Sprint Review, so no second review meeting is expected; a second meeting in the same week is a quality note, and its artifacts may be read when they exist.
- A meeting held on or after Friday 23 October 2026 and by `ISSUE_CUTOFF` was held in Week 5; the syllabus's class week ends on 29 October, and the submission's date is 31 October, so a meeting on 30 or 31 October is in the window and is a caveat in `**Evidence:**` rather than a shortfall.
- The deployed product is shown from the university network, and the production instance is judged in S4; here the criterion is that the meeting showed it and that each implemented test's result was shown at its level.
- A VM that was unavailable, with the local product shown and the deviation declared, satisfies the showing criterion; the deployment itself is judged in S4, and the test's fallback level in S5 and S6.
- The Moodle PDF's recording link and the permission answers it must agree with are S13's PDF items; this segment judges the permission answers in `## Metadata`, the transcript's existence and form, and the report's statement about publication.
- A transcript the customer refused to publish is Moodle-only; a recording link outside the meeting artifacts belongs to S13, and a recording link or timecode inside a meeting artifact is a visibility shortfall here.
- The outcome of the action points the Week 4 report closes belongs to S8; this segment judges only the report's own sections and the verdicts.
- The report's `## Action points` shape is judged here; whether an open action point reappears from S8 is judged there.
- A story the customer accepted in a shared verdict is still judged by its own `AC-nn` comments, and a shared verdict is one decision.
- The script's plan for the tests and the deployment is judged, not whether the customer liked them; the verdict's content is the customer's.
- The PDF's own shape, page count, item list, recording link, and transcript appendix are S13's; this segment reads the report and the script, and reads the PDF only when the report's own statement about publication is unclear.

### S10 — Redeploy and retest after same-week rework

**Check:**

- The pull requests in the Week 5 window that carry the meeting's rework, with their merge times and their files.
- The run of the other implemented test after the rework: its `head_sha`, its created time, and its evidence in the report.
- The tag's target commit, from `gh api "repos/$REPO/git/refs/tags/<tag>"` or `gh api "repos/$REPO/commits/<tag>"`.
- The production deploy record after the rework: its commit, its date, and its core-task verification.
- `reports/week-05/README.md` and the testing plan's evidence, for the commit each names.
- `## Deviations`, for rework deferred to `SPRINT-06`.

**met:**

- When the review asked for same-week rework, the rework is merged in the Week 5 window, on or before `ISSUE_CUTOFF`.
- The reworked commit was deployed to staging after the merge, and the other implemented test ran again at its level against that deployment, or in the CI on the reworked commit.
- The staging test's result is recorded, and it is the result the testing plan's `Checked` sprint and evidence describe.
- The same final commit was then deployed to production, and the core task was verified on it again.
- The released tag names that final commit: the commit the staging test ran, the commit the evidence links, and the commit production serves are the same commit.
- When the rework could not finish before the deadline, it was deferred to `SPRINT-06`, `## Deviations` declares the deferral, and the released commit is the reviewed and tested commit rather than an untested later one.
- When the review asked for no rework, the released commit is the commit staging tested and production served, and nothing in the record claims a rework that did not happen.
- When the VM was unavailable and `## Deviations` declares it, no staging or production deploy takes place: the fallback path satisfies this segment when the tag names the commit the reviewed checks ran on, the record states the fallback, and no artifact claims a deploy or a rework that did not happen; the absent deployment is S4's shortfall.
- The release order the week records is the one the merges, the run SHAs, and the tag show: rework merged, staging deploy and test, production deploy and verification, tag, then the documents that link the tag.

**What does not count:**

- A tag on a commit that no staging test ran, with the evidence pointing at an earlier commit's run.
- Rework merged after the tag, so the release names a state the customer never saw.
- A production deploy of a different commit from the one staging tested, described as "the same commit".
- A rework that was retested only locally while the row claims a `deployed` check.
- A deferral with no `## Deviations` entry, or one that releases an untested later commit.
- The release's date as the deploy's date: the deploy and the test are the evidence, and the tag's date is not one of them.

**partial:**

- A rework exists and its merge or its retest is visible, and at least one other `met` criterion fails.
- Typical shortfalls: rework merged but not redeployed to staging; a staging deploy with no retest; a retest on the old commit; production served a different commit; no core-task verification after the redeploy; the tag on a commit the evidence does not name; a deferral without a deviation.

**missing:**

- The meeting's rework merged in Week 5, but no deploy and no retest after it can be found, and no deferral is declared.

**Guardrails:**

- The sequence is judged from the pull requests' merge times, the runs' `head_sha` and created times, the tag's target, and the evidence links, and any one of those can settle it when the others are silent.
- A same-week rework that the customer's verdict did not require is a quality note: the segment's criteria bind only when the review changed something, and a week with no rework is judged by the released commit's identity alone.
- A rework whose retest failed and whose release was cut anyway is a shortfall here; the failed result itself belongs to S6, and the release on the failing commit is this segment's.
- A deploy after `ISSUE_CUTOFF` is drift and never repairs the sequence at the cutoff.
- The tag's SemVer number, its protection, the release body, the changelog, and the plan's block are S11's; this segment judges only the commit the tag names and the deploy-and-retest sequence that produced it.
- "Deployed to production" is judged from the record in this segment and from the runbook's evidence in S4; a deploy that only an issue comment claims, with no verification, is not a deploy that moved the released commit.
- When the review asked for no rework, no deploy record can be found, and no VM-unavailable deviation is declared, the segment is `partial` against the release-order criterion rather than `missing`; S4 carries the deployment shortfall, and this segment still judges whether the tag names the commit the record supports.

### S11 — REL-05 release

**Check:**

- `CHANGELOG.md` and `docs/project-plan.md` in the snapshot.
- The repository's tags and releases, from `tags.json`, `releases.json`, and `gh api "repos/$REPO/git/refs/tags"`.
- The tag's own date and the date of the commit it names, from `gh api "repos/$REPO/git/refs/tags/<tag>"` for an annotated tag or `gh api "repos/$REPO/commits/<tag>"` for a lightweight one; `releases.json`'s `published_at` is the release page's date and not the tag's.
- The tag protections, from `gh api "repos/$REPO/rulesets"` and `gh api "repos/$REPO/rulesets/<id>"`.
- The release title and body, from the rendered release page or `gh api "repos/$REPO/releases?per_page=100"`, because the collector's dump omits the body.
- The path histories of `CHANGELOG.md`, `docs/project-plan.md`, and `reports/week-05/README.md`, and the merge times they sit at.
- `SPRINT-05`'s GitHub milestone state and its open issues, from the raw `gh api "repos/$REPO/milestones?state=all&per_page=100"` call and its issue list.
- The testing plan's `Checked` cells, for the requirements `**Checked QRs:**` lists.

**met:**

- `CHANGELOG.md` sits in the repository root and follows Keep a Changelog, and its entries are user-visible changes only: a test, a workflow, or a deployment is not an entry.
- Every user-visible change merged before `ISSUE_CUTOFF` has an entry in `[Unreleased]` or in a released section, unless its pull request says it made no user-visible change.
- One tag is this week's release: its version follows Semantic Versioning with the `v` prefix, such as `v0.5.0`, and it is the tag the plan's `#### REL-05` block and the changelog's latest dated section name; when those disagree, both fail.
- The release tag points at a commit on `main`, the commit is not after `ISSUE_CUTOFF`, and its own date is not after `ISSUE_CUTOFF` either.
- The tag names the final production commit of S10: the commit the staging test ran, the evidence links, and production served; on S10's VM-unavailable fallback, it names the reviewed commit the checks ran on.
- A GitHub release exists for that tag, titled with the tag, so the title and the tag match.
- The release body is the customer-facing note in the team's shape, and its last line is `[Full changelog](<absolute url>)` linking the changelog's released section, with nothing after it.
- The changelog has a dated section headed `[x.y.z](https://github.com/<org>/<repo>/releases/tag/vx.y.z) - YYYY-MM-DD` that links the release, its entries are the entries released, and a new empty `[Unreleased]` sits above it.
- The `#### REL-05` section nested under `### SPRINT-05` carries a bulleted block with `**Released:**` first and `**Checked QRs:**` second.
  `**Released:**` gives the tag as link text and the day it was cut, so the bullet reads `- **Released:** [v0.5.0](https://github.com/<org>/<repo>/releases/tag/v0.5.0) on 2026-10-29.`
- `**Checked QRs:**` follows its label with one bullet per `QR-nn` that has at least one test checked in `SPRINT-05`, each linked to its requirement file, and then one sentence linking the testing plan's `#quality-requirement-testing-plan` anchor.
- Every requirement in `**Checked QRs:**` has a test whose `Checked` cell names `SPRINT-05`, and no requirement whose only tests were last checked in an earlier sprint appears.
- A requirement whose test is checked in `SPRINT-05` appears even when its row is `Fails` or `Not verified` for another test: the list indexes what was checked, not what passed.
- `#### REL-05` is the sprint's last release and carries the block; an earlier release cut in the same sprint carries no `#### REL-nn` section and no block, and a hotfix after `REL-05` carries none.
- `SPRINT-05`'s GitHub milestone is closed after the release, and every issue that was still open was moved into a later sprint's milestone before the close.
- The tag predates the commit that added the changelog's released section, the commit that added the plan's `REL-05` block, and the commit that added `reports/week-05/README.md`, so every link to the release resolves against a tag that already existed.
- The tag is protected against being moved or deleted, by a repository ruleset that covers tag pushes or an equivalent tag-protection rule that blocks moving and deleting the tag.

**What does not count:**

- A release body that is the changelog's entries pasted in, a list of pull requests, or a copy of the week report: the body is the customer-facing note.
- A `Full changelog` line with content after it, a relative link, or a link to `CHANGELOG.md` with no released-section anchor.
- The release page's `published_at` or the changelog's date as the tag's time when the tag object or its commit is later.
- A commit date before the cutoff with a tag created or pushed after it.
- A `tags.json` entry on its own, because it carries only the tag name and not the date the tag was created.
- A tag that was force-moved or re-pushed to an older commit to appear on time.
- A `**Checked QRs:**` list built from the matrix's `High` rows rather than from the tests whose `Checked` cell names `SPRINT-05`.
- A `**Checked QRs:**` list that includes a requirement whose test last ran in `SPRINT-04` and was not rerun.
- The testing plan's own test results as the list's content: the list links the plan once and repeats no result.
- A still-open `SPRINT-05` milestone with no declared deviation.

**partial:**

- `CHANGELOG.md` exists, or a release was cut, and at least one other `met` criterion fails.
- Typical shortfalls: no `[Unreleased]` section; a tag without the `v` prefix or not SemVer; a tag on a branch commit or cut after `ISSUE_CUTOFF`; a release titled differently from its tag; a body that is a changelog dump; no `Full changelog` line or one that does not resolve; a dated section that does not link the release; no `REL-05` block; `**Released:**` without the tag link or the day; a `Checked QRs` list missing a checked requirement, adding an unchecked one, or linking the plan twice; a document that links the release in a commit that predates the tag; an unprotected tag; `SPRINT-05`'s milestone still open without a declared deviation; two releases in the sprint both carrying a block.

**missing:**

- `CHANGELOG.md` is absent at the snapshot, and no tag or release exists at `ISSUE_CUTOFF`.

**Guardrails:**

- The version number is the team's choice under SemVer; a `REL-05` other than `v0.5.0` is never a shortfall, and the course's `v0.5.0` is an example rather than a scheme.
- `**Checked QRs:**` is an index of what was checked in the sprint and not a quality claim: a requirement with one passing test and one `Not verified` test belongs in the list, and the plan's rows say which is which.
- The release body's recommended shape, such as the opening capability and the limitation, is a quality note; the required facts are the customer-facing note, the team's own shape, and the `Full changelog` line last.
- The changelog's groups, `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security`, are judged by the entries' placement, not by whether every group is used.
- When the tag rulesets cannot be read with the token, say which endpoint returned what, judge the rest, and set `Evidence gaps: yes` only when the answer could change the status.
- `REL-04` and Week 4's release are not re-graded; this segment judges the release this week cut.
- A tag created after `ISSUE_CUTOFF` is a shortfall under the cutoff criterion, and a tag made on the cutoff day is judged by its timestamp in UTC.
- The commit the tag names is S10's final production commit, or the reviewed commit on S10's VM-unavailable fallback; a disagreement between this segment and S10's sequence is reported in S10, which owns the sequence, and this segment judges only that the tag names that commit.
- The changelog's `[Unreleased]` upkeep through the week is judged by the released section's completeness, not by an entry-by-entry audit of every intermediate commit.
- A changelog line that a pull request's own body marks as not user-visible is judged by the entry, not by the marker alone.

### S12 — Sprint close and retrospective

**Check:**

- `### SPRINT-05` in `docs/project-plan.md` at the snapshot, its `**Actual Velocity:**`, and the path history of the plan.
- The story issues in `SPRINT-05`'s milestone, their closed state and reason from `issues.json`, and their `Story Points` from `issue-fields.json`.
- The issues rescheduled out of `SPRINT-05`'s milestone, from their `milestoned` and `demilestoned` events.
- `reports/week-05/sprint-retrospective.md` in the snapshot.
- `reports/week-04/sprint-retrospective.md` at the snapshot, for its `## Actions` rows marked `Carried: Yes`.
- The artifacts the retrospective's actions and outcomes link.

**met:**

- `### SPRINT-05` carries `**Actual Velocity:**` after `**Planned Velocity:**`, as the next field in the bulleted list.
- `**Actual Velocity:**` is a whole number equal to the sum of the `Story Points` of the stories in `SPRINT-05`'s milestone that are closed as completed at `ISSUE_CUTOFF`, and a story closed as not planned does not enter the sum.
- The `**Actual Velocity:**` line continues with one sentence saying what moved out of the sprint and to which sprint, or saying that nothing moved out, and the sentence agrees with the milestone events.
- `reports/week-05/sprint-retrospective.md` exists and carries the sections `## What Went Well`, `## What Did Not`, `## Actions`, and `## Carried Actions`, in that order.
- `## What Went Well` has the column `What went well` and 3 or more rows, each one sentence naming what happened.
- `## What Did Not` has the columns `Problem` and `Root cause` and 2 or 3 rows, each with the problem and its root cause.
- `## Actions` has the columns `Action`, `Owner`, `Impact`, `Reason`, and `Carried`, in that order, and 3 or 4 rows; every `Owner` is a GitHub username, every `Impact` is `High`, `Medium`, or `Low`, every `Reason` names the problem or root cause it answers, and every `Carried` is `Yes` or `No`.
- `## Carried Actions` has the columns `Action` and `Outcome`, with one row for each action `reports/week-04/sprint-retrospective.md` marks `Carried: Yes`.
- Every `Action` cell in `## Carried Actions` cites `reports/week-04/sprint-retrospective.md#actions` with the action quoted.
- Every `Outcome` is `Done`, `Not done`, or `Dropped`, and it says what was found or why not.
- Every action with `Outcome: Not done` is re-listed in this file's `## Actions` with `Carried: Yes`, and an action `Done` or `Dropped` is not re-listed.
- The retrospective adds no section beyond the four, and it is the record of `SPRINT-05` rather than a rewrite of an earlier file.

**What does not count:**

- `**Actual Velocity:**` as a sentence without a number, or as a number that is the planned figure rather than the completed stories' sum.
- A sum that includes a story closed as not planned, or a task's `Priority` value.
- A `## Carried Actions` table of the team's new actions rather than the previous file's `Carried: Yes` rows.
- An `Action` cell that cites `reports/week-04/sprint-retrospective.md` with no `#actions` anchor or no quoted action.
- An `Outcome` of `Done` with no artifact or comment behind it.
- A `Not done` action that disappears from `## Actions` instead of being re-listed with `Carried: Yes`.
- A retrospective section renamed, reordered, or merged, such as `## What Went Well And What Did Not`.
- Four actions with no `Reason`, or an `Owner` given as a real name.

**partial:**

- `### SPRINT-05` carries `**Actual Velocity:**`, or the retrospective exists, and at least one other `met` criterion fails.
- Typical shortfalls: `**Actual Velocity:**` absent, out of order, or not the completed stories' sum; no sentence on what moved out; a retrospective section missing, renamed, or out of order; fewer than 3 things that went well; a `## What Did Not` without a root cause; 2 or 5 actions; an owner who is not a GitHub username; an `Impact` or `Carried` value outside its options; a missing `Reason` cell; a `## Carried Actions` that carries the wrong actions or cites nothing; a `Not done` action not re-listed.

**missing:**

- `reports/week-05/sprint-retrospective.md` is absent at the snapshot, and `### SPRINT-05` carries no `**Actual Velocity:**`.

**Guardrails:**

- The retrospective's content and the "what went well" facts are the team's judgement; judge the sections, the row counts, the columns, the citations, and the outcomes, not whether the sprint was good.
- The carried actions are exactly the previous file's `Carried: Yes` rows: an action the previous file marked `Carried: No` is not carried, and one the team had already finished may be `Done`.
- When the Week 4 retrospective says there is no previous retrospective, that file's `## Carried Actions` is a sentence and the Week 5 file still carries a table, because it now has a previous file to carry from.
- A story that moved out and was rescheduled into a later sprint's milestone is the sentence's subject, and its later milestone is the sprint it names.
- A story closed as completed after `ISSUE_CUTOFF` does not enter the sum, and the `**Evidence:**` states which stories were counted and at which cutoff.
- A mismatch between the sentence and the report's moved-out line is reported here, because this segment owns the plan's velocity sentence, and the report's own line is judged in S13 against the same events.
- Whether the file's first commit followed `**Actual Velocity:**` is a caveat in `**Evidence:**`, never a status change.
- A later formatting-only change to the file is allowed; a rewrite of its content after the week is a caveat and a quality note.
- `SPRINT-06`'s retrospective and any later one are not judged here.

### S13 — Week report and submission

**Check:**

- `reports/week-05/README.md` at the snapshot, and every repository file it links.
- The Moodle PDF, its page count, and its contents; a submission directory that holds a Markdown wrapper and no PDF is a submission-format problem judged here.
- The snapshot SHA's position on `main` and the snapshot commit time, per procedure step 4.
- The runs whose `head_sha` is the snapshot SHA or an ancestor on `main`, from `runs_sha.json` and `runs_main.json`, for the repository evidence.
- The merged pull requests in the Week 5 window, for the one that closed its task issue.
- A privacy scan of the snapshot, per procedure step 16.
- The tags and releases, for the summary's claims.

**met:**

- `reports/week-05/README.md` is in the snapshot, and every repository file it links resolves.
- The report identifies the week, the project, the team, and the covered scope.
- The summary names the deployment and where it runs, so a reader knows the product is on the university VM and that the customer reaches it from the university network, and it points at the Moodle submission for the address rather than naming it.
- The summary names each plan milestone whose `**Due:**` falls in `SPRINT-05` to `SPRINT-09` and says what each delivers, or says that the plan carries none in that range.
- The summary names `REL-05` and its tag.
- The summary names the CI checks that do not apply to the stack and why, or says that every check applies, and names what moved out of the sprint.
- The summary points at `docs/project-plan.md#quality-requirement-testing-plan` for the rows that are not `Passes`, and copies none of the rows.
- The summary says what the team found, built, or decided, and what it left open.
- The report states the customer-meeting outcome: each story shown with whether the customer accepted or rejected it, each citing its `DEC-nnn`, and each implemented test's result at its level.
- The report says whether the meeting's transcript was published, shared privately, or not made, and why.
- The coverage table has the 15 rows of `assignment-5.md`, in its order: Sprint plan and milestones, New stories, Quality requirement tests, Testing plan, Automated tests and CI, Deployment, Feature documentation, Week 4 action points, Week 4 open questions, Meeting script, Meeting transcript, Customer validation, `REL-05`, Sprint retrospective, and AI usage.
- Every coverage cell links its artifact: a repository file with its path from the repository root as the link text and the heading anchor when the row names a section, and anything else with descriptive link text; a row whose artifact is not public says so instead of linking it.
- When the customer refused publication of the transcript, the Meeting transcript row says so and points at the Moodle submission.
- No second list of the same links follows the coverage table.
- The report carries no sprint planning, refinement, or retrospective section, because the plan, the issues, and the retrospective file own them.
- A contribution table maps each member's GitHub username to the work done, using links to their commits, pull requests, or reviews where possible.
- The report does not assess an individual: no section rates or explains a member's contribution.
- The repository evidence links one merged pull request that closed its task issue, and the latest green link-check, Markdown-check, `actionlint`, and product-code CI runs on `main`, each by its run URL, and each link resolves.
  Each run's `conclusion` is `success`, and a run whose branch is not `main`, or whose `head_sha` is not an ancestor of the snapshot, is not the run this item asks for.
- Every link in the report resolves, and every link the link check excludes is justified in prose.
- `## Deviations` declares every deviation observed in the other segments, including a VM that was not available, a `scripted` or `CI` fallback, a `manual` test with its `**Why Manual:**`, a second test on the next active row, and rework deferred to `SPRINT-06`, or says `None` when there is none.
- One line states that no private-only material was committed to the repository.
- The privacy scan finds no email address, phone number, member-name token, or `.env`/key file outside the Week 5 meeting artifacts, and no recording link outside them; a personal-data hit or a recording link inside a Week 5 meeting artifact is reported in S9, not here.
- The report and the week-local files it links carry no real VM address, host name, password, token, or secret, and the report points at the Moodle submission for the address; an address in `docs/deployment.md` is S4's and one in a test's `**Runs at:**` is S5's.
- The snapshot SHA is on `main`, and the PDF permalink points at `reports/week-05/README.md` at that full 40-character SHA.
- The report and every repository file it links are merged into `main` at the snapshot; nothing the assignment requires is left on an unmerged pull-request branch.
- The PDF is at most two pages, not counting a transcript appendix, and holds only the seven items of `assignment-5.md`: the project name and team number, the member table, the permalink, the staging and production addresses with the network note, the recording link or the line saying why there is none, the transcript when publication was refused, and the privacy confirmation line.
- The submission is a PDF: a directory that holds only a Markdown wrapper is a submission-format shortfall in this segment, even when the wrapper carries a valid permalink.

**What does not count:**

- The workflow's run list page, a branch's run history, or a job URL as the run link: the report needs the individual green run's URL.
- A green run on a branch other than `main`, a pull-request run, or a run on a commit that is not an ancestor of the snapshot.
- A red, cancelled, or in-progress run cited as green; read `conclusion`, not the run's existence.
- A Markdown wrapper, or a link to one, as the two-page Moodle PDF.
- A coverage table with the weekly-report example's 12 rows in place of the assignment's 15, or one that omits a row and folds it into another.
- A report that pastes the testing plan's rows, or that repeats the plan's table as its own.
- A PDF that carries the repository report pasted in, or a page over the two allowed.
- A summary that says the product "is deployed" with no place and no network.
- A `## Deviations` line that declares one deviation and leaves another observed one out.

**partial:**

- `reports/week-05/README.md` exists at the snapshot, and at least one other `met` criterion fails.
- Typical shortfalls: a coverage row missing, out of order, or not linked; no deployment line, no milestone lines, no release line, no non-applicable-check note, or no moved-out note in the summary; no meeting outcome or no test result; a sprint-planning, refinement, or retrospective section in the report; no contribution table; an individual assessment; repository evidence missing a run or the pull request, linking a red run, a run list, or a run off `main`; a Markdown wrapper instead of the PDF; no `## Deviations`; an undeclared deviation; a privacy finding outside the meeting artifacts; a seven-character permalink; a snapshot that is not on `main`; a PDF over two pages or with extra content; the addresses missing from the PDF.

**missing:**

- `reports/week-05/README.md` is absent at the snapshot.

**Guardrails:**

- A coverage row whose artifact is absent is a shortfall in the segment that owns the artifact; here the shortfall is only a missing row or a row that does not link.
- The underlying tests, deployment, features, release, retrospective, and AI usage are judged in S5 to S12 and S14; here only the week report's summary lines, the coverage rows, their links, the report's own evidence, and the submission are judged.
- The Deployment row links `docs/deployment.md` and the report's deployment line; whether the deployment happened is S4's.
- The Testing plan row and the summary's pointer are judged here as a pointer and a link, while the plan's columns, rows, and results are S6's.
- The Submission Procedure's snapshot upload to Moodle is not judged: the autochecker receives only the PDF and rebuilds the snapshot from the permalink SHA, per `docs/grading-policy.md`.
- The PDF's recording link gets one access check per `docs/grading-policy.md#consumer-hosted-media`; an inaccessible or sign-in-gated recording is an evidence gap for that item only, and the PDF's other items are still judged.
- Record the snapshot commit date against the deadline in `**Evidence:**`, and never change a status for lateness.
- Report a privacy finding by path and kind, such as "the VM's IPv4 address in `docs/deployment.md`", never by value.
- The privacy line is a repository-wide claim: the scan covers the whole snapshot, so a member-name, email, phone, `.env`, or key-file hit in a Week 1 to Week 4 file, including an earlier week's meeting artifact, is a shortfall here even though that week's own artifacts are not re-graded; a hit inside a Week 5 meeting artifact is reported in S9.
- A report that links a file at a commit other than the snapshot is accepted when the target exists; record the hash in `**Evidence:**`.
- The report's length, its prose, and the contribution table's wording are quality notes.
- The `## Deviations` section declares what the other segments observed; an undeclared deviation is a shortfall here, while the deviation itself is judged in its own segment.
- The root `README.md` linking the current week's report is a Week 1 rule: a current-week or previous-week link is recorded in `**Evidence:**` as a quality note and never changes an S13 status.
- The member table, the addresses, the recording link, and a refused transcript are Moodle-only, and their absence from the repository is correct; the API-key, token, or password that a deploy needs is never judged as missing from the PDF unless the assignment's own item list asks for it, which Week 5 does not.

### S14 — AI usage and honesty

**Check:**

- `reports/week-05/ai-usage.md` in the snapshot.
- Traces of AI tools: the team's `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.agents/`, `.opencode/`, `opencode.json`, `.github/copilot-instructions.md`, `.cursor/`, a `Co-Authored-By:` trailer that names an AI tool, a `Harness:` or `Model:` trailer, and a "Generated with" line in Week 5 commit messages and pull request bodies.
- The Week 5 prose: `docs/deployment.md`, `docs/features.md`, the quality requirement tests, the testing plan, the week report, the meeting artifacts, the retrospective, and the README summary lines.
- The claims the Week 5 artifacts make about the deployment, the tests, the counts, and the identifiers they cite.

**met:**

- `reports/week-05/ai-usage.md` names each tool and what it was used for, and says what the team did with the output: what it accepted, changed, and rejected, and why.
- Alternatively, the file states in one line that no AI tools were used, and nothing in the repository or its history contradicts it.
- The disclosure agrees with the traces of AI tools in the repository, the commit messages, and the pull request bodies, including the course-materials skill when other traces show agent output.
- The Week 5 prose has no filler, meaning no template sentence with no product name, no identifier, and no date, and no unchecked generated text, such as leftover `<org>` or `<repo>` placeholders, identifiers that point nowhere, or claims that contradict the team's own artifacts.
- Every identifier a Week 5 artifact states resolves to an artifact that carries it, and every count it states matches the artifact it counts, including the number of tests, the number of features, and the `Checked QRs` count.
- The deployment and test claims agree with the evidence: a report that says production runs a commit the evidence never names, or that a test is `deployed` when its only run is `CI`, is the contradiction this criterion names.
- Where the statement of a test's level, a deployment's date, or a sprint's velocity separates what was observed from what was inferred, it says which; a claim with no evidence behind it is a shortfall here only when it contradicts the team's artifacts.

**What does not count:**

- Tools named with no statement of what happened to their output.
- An agent trace or an AI-tool `Co-Authored-By:` trailer with no disclosure, while the file says no AI was used.
- A placeholder or a template sentence left in a Week 5 artifact, such as `TBD` in a table or `<your-deployment>` in the runbook.
- A `QR-nn`, `QRT-nn`, `FR-nnn`, `ADR-nnn`, or `US-nn` cited that does not exist.
- A statement of how many requirements are checked that the plan's `Checked QRs` count contradicts.
- A one-line "no AI tools were used" beside a commit trailer that names an AI tool.

**partial:**

- `reports/week-05/ai-usage.md` exists, and at least one other `met` criterion fails.
- Typical shortfalls: tools named without saying what happened to their output; agent traces or an AI-tool `Co-Authored-By:` trailer with no disclosure; a placeholder or a template sentence left in a Week 5 artifact; an identifier cited that does not exist; a count that the artifact contradicts; a deployment or test claim that contradicts the evidence.

**missing:**

- `reports/week-05/ai-usage.md` is absent at the snapshot.

**Guardrails:**

- Using AI tools is allowed and is never a shortfall by itself.
- The course-materials submodule alone does not prove agent use; count it as undisclosed use only when other traces show agent output.
- The meeting report's own-words rule belongs to S9, and the deployment's truthfulness to S4; here the criterion is the disclosure and a contradiction between a claim and the team's own artifacts, reported once, in the segment that owns the artifact.
- Week 1 to Week 4 text left unchanged is not re-judged.
- The filler test is anchored to the artifact's own evidence: quote a short fragment, and name the artifact and the heading.
- A generated diagram or table is not a shortfall when the team checked it and the disclosure says so; the artifact's correctness is judged in its own segment.
- The AI usage report's file is the disclosure; a one-line "no AI" answer is valid when the traces agree.
- The report's honesty about a fallback, such as a VM that was not available, is judged in S4 and S13; this segment judges only that the Week 5 prose does not claim what the artifacts contradict.

## Semantic feedback

`agent-semantic-feedback.md` is the optional companion file defined in `docs/semantic-feedback-format.md`.
The semantic agent writes it after the compliance report is final, when the operator runs the semantic pass.
The compliance agent does not write the companion file.
The semantic agent starts from the report as a map, verifies each claim its verdict rests on against the snapshot at the saved SHA or the saved evidence, and never edits `agent-compliance-feedback.md`.
It never changes a status, an `Evidence gaps` flag, `Manual review required`, the overall assessment, or the grade; a segment may be `met` while its dimension is `thin`.

The five dimensions, in this order:

| Dimension | Segments | The question |
|-----------|----------|--------------|
| Setup | S3, S4 | Could a teammate who was not in the room redeploy, verify, and roll back on Monday, and would CI stop a broken critical module? |
| Tests | S5, S6 | Does each QRT measure the requirement, and would the suite fail if the requirement's failure mode happened? |
| Plan | S1, S2, S12 | Is the plan a forecast the team could steer by, written before the work? |
| Customer loop | S8, S9, S10 | Did the review change what the team will build, and did the change reach production? |
| Publication | S7, S11, S13, S14 | Can a reader who trusts the public record reproduce what production runs? |

### Setup

Ask whether a teammate who was not in the room could redeploy, verify, and roll back, and whether CI would fail on a broken critical module.
Read the four environments, the staging and production separation by construction, the deploy and rollback commands, the verification record, the critical modules the testability requirement names, and the workflows' triggers, pins, named steps, clean checkout, and absence of a deploy.

`thin` when the runbook defers the two steps a teammate cannot improvise, when staging and production share configuration or data, when the verification stops at a health endpoint, or when a critical module is compiled but never exercised.
`not yet adequate` when the deploy cannot be followed from the runbook, or the released commit and the deployed commit disagree.

### Tests

Ask whether each test measures the requirement and whether the suite would fail when the requirement's failure mode happens.
Read the `**Pass when:**` line against the response measure, the procedure, the level and `**Runs at:**`, the critical modules, the manual exception, and the testing plan's statuses and evidence.

`thin` when a test exists but exercises the easy path, when the pass criterion drops the threshold, when the critical modules are compiled rather than tested, or when the plan marks a row `Passes` without level-appropriate evidence.
`not yet adequate` when the tests do not measure the requirement at all, or the plan's result and the test's definition disagree.

### Plan

Ask whether the plan is a forecast the team could steer by, written before the work.
Read the sprint goal, the plan and sprint milestones, the planning-time and closed-story velocity, the refinement state, the retrospective's causes, and the path history of `docs/project-plan.md`.

`thin` when the plan was written after the sprint started, when the planned and actual figures are the same while the stories are still open, when the milestones are task bundles, or when the retrospective records no cause and carries nothing.
`not yet adequate` when the plan carries no goal or no computed figure, or the sprint close contradicts the plan's own numbers.

### Customer loop

Ask whether the review changed what the team will build, and whether the change reached production.
Read the script, the report, the transcript, the per-story verdicts, the decisions and the artifacts they changed, the action points and their due dates, the rework, and the released commit.

`thin` when the decisions are shared rather than per-story, when no decision changes an acceptance criterion or the next sprint's scope, when the script was written after the meeting, or when the rework is recorded but not redeployed.
`not yet adequate` when the meeting did not show the deployed product or its implemented tests, or the recorded decisions cannot be traced to any change.

### Publication

Ask whether a reader who trusts the public record can reproduce what production runs.
Read the tag and its target, the release body, the changelog, the plan's `Checked QRs`, the week report's claims against the issues, pull requests, and runs, the features page, and the AI usage report.

`thin` when the release record is complete but the evidence links stop at index pages, when the report's claims run ahead of the artifacts, or when the features page lists artifacts rather than capabilities.
`not yet adequate` when the release does not name the production commit, or the public record contradicts the repository.

### Guardrails

- Ground every claim in an artifact you verified at the saved SHA or a live URL; the compliance report is a map, not evidence.
- Verify the claims your judgement depends on, not every report claim, and do not re-audit the segments.
- Prefer `evidence.sqlite` and the saved dumps; at most three live `gh` lookups for this file, and record each one.
- Write `work/<team_dir>/semantic-claims.json` and mark each claim `supported`, `contradicted`, or `unverifiable`; only supported claims feed the semantic file.
- Do not use status vocabulary (`met`, `partial`, `missing`, `unverified`), a grade, a score, a rank, or a cross-team comparison.
- Do not repeat the `## Main issues to fix` list; say what the artifact can and cannot do yet, and what breaks first.
- A `partial` or `missing` segment does not make its dimension `not yet adequate` by itself; judge the artifact, not the count.
- If a judgement contradicts a status, record the conflict in the ledger and return it; the status wins until the operator regrades the report.
  Never edit the report to fit the judgement, and never soften the judgement to fit the status.
- Omit a dimension only when all of its segments are `unverified`; keep at least three.
  If fewer than three dimensions remain, do not write the file.

## Assignment-specific procedure deltas

1. Take the team set from the directory names under `itpd-assignments-feedback/A5/submissions/`.
2. Read the Moodle PDF with the submission fetcher, which prefers the PDF that carries the full-SHA permalink to `reports/week-05/README.md` when there are several:

   ```console
   uv run python scripts/fetch_team_snapshot.py A5 "<team_dir>"
   ```

   It records the extracted metadata in `itpd-assignments-feedback/A5/work/<team_dir>/pdf-info.json`: the team number, repository, permalink, full SHA, recording link, page count, GitHub usernames, the member name/email tokens for the step 16 privacy scan, and the permalink week it derives from the path.
   The fallback is to read the PDF directly and extract:

   - the project name and the team number;
   - the GitHub usernames of the member table, keeping real names and emails only in working memory for the privacy match;
   - the permalink to `reports/week-05/README.md`, with its organization, repository, and full SHA;
   - the staging and production addresses and the network note, for the S4 check and the S13 item;
   - the recording link or the line saying why there is none;
   - whether a transcript appendix is present;
   - the privacy confirmation line;
   - the page count, for example from `pdfinfo`, and anything outside the seven allowed items.

   When the submission directory holds no PDF and one Markdown file instead, run `uv run python scripts/fetch_markdown_snapshot.py A5 "<team_dir>"`: it reads the Markdown, writes `pdf-info.json` with `permalink_source=operator` and the member name/email tokens, and fetches the snapshot.
   Treat the missing PDF as an S13 shortfall, and say in `**Evidence:**` that the wrapper was Markdown rather than a PDF.
   Fall back to reading the Markdown by hand and writing `pdf-info.json` only when the helper cannot parse it.
3. The fetcher in step 2 resolves the snapshot per `docs/grading-policy.md` and refetches it into a freshly emptied `itpd-assignments-feedback/A5/work/<team_dir>/snapshot/`.
   When it cannot, resolve and fetch by hand as in `agents/compliance-agent.md`.
   A permalink that points at `reports/week-04/README.md` is a wrong-week permalink: the fetcher prints a `warn:` line, records `permalink_week_mismatch`, skips the commit check and the snapshot fetch, and exits 1 with a rerun command.
   Do not grade the wrong-week target; the wrong week is the S13 shortfall, and the operator supplies the right permalink with `uv run python scripts/fetch_team_snapshot.py A5 "<team_dir>" --permalink <url>`, recorded as `permalink_source=operator`, so the snapshot fetched from that permalink governs every file check.
4. Read the snapshot commit time and the on-`main` result from `pdf-info.json` (`snapshot_time`, `on_main`, `on_main_status`), or re-check them with `REPO=<org>/<repo>` and `SHA=<full SHA>`:

   ```sh
   gh api "repos/$REPO/commits/$SHA" --jq '.commit.committer.date'
   gh api "repos/$REPO/compare/$SHA...main" --jq '.status'
   ```

   A status of `identical` or `ahead` puts the commit on `main`; `behind` or `diverged` does not, which is an S13 shortfall.
   Call the first value `SNAPSHOT_TIME`, and record the snapshot commit time against the deadline in `**Evidence:**`; it never changes a status.
5. Collect the live evidence once and keep it beside, not inside, the fetched snapshot.
   Preferred: `uv run python scripts/collect_github_evidence.py A5 "<team_dir>" [--issues <n> ...] [--paths <path> ...] [--timelines [<n> ...]]`, which reads `itpd-assignments-feedback/A5/work/<team_dir>/pdf-info.json` and writes `labels.json`, `issues.json`, `prs.json`, `runs_main.json`, `runs_sha.json`, `commits.json`, `milestones.json`, `releases.json`, `tags.json`, plus `issues/<n>.comments.json`, `issues/<n>.timeline.json`, `issues/<n>.edits.json`, `paths/<path>.json`, and a bounded `summary.md` there, printing counts and paths only.
   A bare `--timelines` collects every issue's timeline at one paginated request per issue; name the issues when only a few need it, and let `--issues` cover the rest.
   Read `summary.md` first: it carries the issue counts, the pull-request numbers, the failing runs, the tags, and each milestone's due date with its open and closed issue counts, in at most 60 lines.
   Open a dump only through a bounded projection that prints at most about 40 lines (`head -n 40`, a `jq` projection, or an `rg` match); never `cat` a full dump, because `commits.json` reached 1.35 MB and `prs.json` 284 KB.
   `--summary` rebuilds the digest from the saved dumps without calling `gh`.
   The issue fields are their own mode: `uv run python scripts/collect_github_evidence.py A5 "<team_dir>" --issue-fields` writes `issue-fields.json` there with every issue's `type`, `milestone`, `assignees`, and `field_values`, from one paginated REST list call and without its pull requests.
   It is not combined with `--summary`, `--issues`, or `--paths`.
   The raw fallback commands are:

   ```sh
   gh label list --repo "$REPO" --limit 200 --json name,description
   gh issue list --repo "$REPO" --state all --limit 1000 \
     --json number,title,labels,state,stateReason,createdAt,closedAt,body,url,author,type,closedByPullRequestsReferences
   gh pr list --repo "$REPO" --state all --limit 500 \
     --json number,title,author,headRefName,baseRefName,state,createdAt,mergedAt,closedAt,body,closingIssuesReferences,reviews,files,url
   gh run list --repo "$REPO" --branch main --limit 100 \
     --json databaseId,workflowName,headSha,event,status,conclusion,createdAt,url
   gh api "repos/$REPO/actions/runs?head_sha=$SHA" \
     --jq '.workflow_runs[] | [.name, .event, .conclusion, .html_url] | @tsv'
   ```

   The issue's `type` may need the REST call rather than `gh issue list`; the `--issue-fields` mode is the reliable route.
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

6. Judge every issue as of `ISSUE_CUTOFF`, `2026-10-31T23:59:59+03:00`, for every team:

   - Count only issues whose `createdAt` is at or before `ISSUE_CUTOFF`.
     An issue opened after `SNAPSHOT_TIME` but by `ISSUE_CUTOFF` counts like any other, and an issue opened after the cutoff is not judged.
   - Take an issue's labels at `ISSUE_CUTOFF` from its timeline's `labeled` and `unlabeled` events, its title from `renamed` events, and its open or closed state and close reason from `closed` and `reopened` events.
   - Take its body from the last edit at or before `ISSUE_CUTOFF` when the edit history allows it; otherwise judge the current body and say so in `**Evidence:**`.
   - Take its milestone from the `milestoned` and `demilestoned` events when the issue has them, and its current milestone otherwise, noting in `**Evidence:**` which was read.
   - The `issue_state_at_cutoff` view in `evidence.sqlite` answers the label set, milestone, and close or reopen state at the cutoff for every collected timeline in one query; `issue_events` answers when the question needs the events themselves or a time other than the cutoff, such as the planning time for S1 and the reschedule for S12.
   - A comment or edit made after `ISSUE_CUTOFF` is a caveat, never a shortfall.
   - Post-cutoff file state is a caveat and never a status change, except in a segment that judges the snapshot, which reads the file at `SNAPSHOT_TIME`.
   - Set `Evidence gaps: yes` only when the state at `ISSUE_CUTOFF` cannot be read and the difference could change the status.
   - Pull requests, Actions runs, repository files, tags, and releases stay judged as of `ISSUE_CUTOFF`, and the snapshot stays the evidence for files.
7. Identify the Week 5 pull requests: every pull request created on or after Friday 23 October 2026, 00:00 Innopolis time, the start of Week 5 in `course/syllabus.md`, and by `ISSUE_CUTOFF`.
   A pull request merged at or before the team's Assignment 4 snapshot commit is part of the Week 4 submission, not a Week 5 pull request.
   Read that SHA from the saved A4 feedback report's `Primary index reviewed` link at `itpd-assignments-feedback/A4/feedback/<team_dir>/agent-compliance-feedback.md`, or from the A4 submission PDF.
   When neither is available, use the team's A4 cutoff as the boundary: `2026-10-25T23:59:59+03:00` for every team, and `2026-10-26T23:59:59+03:00` for `Team 2 - OK_10938_assignsubmission_file`, whose Week 4 deadline was extended; say in `**Evidence:**` which boundary was used.
   The in-scope pull requests for the release, the rework sequence, and the report's evidence run from the start of Week 5 to `ISSUE_CUTOFF`, without Dependabot pull requests and pull requests a workflow opened.
8. Gather the pull-request facts below as evidence. These are Week 1 and Week 2 mechanics and are not re-graded in Assignment 5, except where a criterion names them: S10's rework sequence, S11's merge order, and S13's repository-evidence pull request. Record an anomaly in `**Evidence:**` only; never make it a shortfall in S13 or S2.

   ```sh
   gh pr list --repo "$REPO" --state all --limit 500 \
     --json number,headRefName,author,state,mergedAt,closingIssuesReferences,reviews,milestone \
     --jq '.[] | {n: .number, branch: .headRefName, author: .author.login, state, merged: .mergedAt,
                  closes: [.closingIssuesReferences[].number],
                  approvers: [.reviews[] | select(.state == "APPROVED") | .author.login] | unique,
                  milestone: .milestone.title}'
   ```

   - `closes` has exactly one number, and that issue carries the `Task` issue type.
   - `branch` matches `^<that number>-[a-z0-9]+(-[a-z0-9]+)*$`.
   - A merged pull request has an approver other than its author, its task's body has every criterion ticked as `- [x] AC-nn:`, and the task's `stateReason` is `COMPLETED`.
   - Compare the task's body edit history (`userContentEdits` `editedAt`, from step 5) with each approving review's `submittedAt`.
     A shortfall needs the history to show a box ticked after the approval.
     When the task has no edit history, check only that every box is ticked by merge and say so in `**Evidence:**`.
   - A pull request closed without merging left its task `NOT_PLANNED` with a comment that gives the reason and links the pull request.
9. Read the new stories and the backlog from the issue dumps at `ISSUE_CUTOFF`:

   ```sh
   jq -r '.[] | [.number, (.type // "-"), (.milestone // "-"),
                   ((.field_values // []) | map(select(.name == "MoSCoW") | .value) | join(",")),
                   ((.field_values // []) | map(select(.name == "Story Points") | .value) | join(",")),
                   ((.field_values // []) | map(select(.name == "Responsible") | .value) | join(",")),
                   ((.field_values // []) | map(select(.name == "Accountable") | .value) | join(",")),
                   ((.assignees // []) | join(","))]
                  | @tsv' "{TEAM_WORK}/issue-fields.json" | head -n 60
   jq -r '.[] | select(.number == <n>) | .body' "{TEAM_WORK}/issues.json" | head -n 40
   ```

   - The first projection answers the type, the milestone, the four field values, and the assignees for the issues in the page it prints; narrow it with `select(...)` when the list is long.
   - The body projection answers the criteria and `### Specified by`; read it for each new story, and use `issues/<n>.edits.json` when the body changed at the cutoff.
   - Every `FR-nnn` and `ADR-nnn` a new story's `### Specified by` names must resolve in the snapshot.
   - The stories opened on or after `2026-10-23T00:00:00+03:00` are the new ones; the open stories in no milestone are the product backlog, and the ones the team places in the next two sprints' worth are the ones refinement must have estimated.
10. Check the deployment from the runbook and the record:

    - Read `docs/deployment.md`, `.env.example`, and `docs/setup.md` at the snapshot, and check the four environments, the VM access, the two ports, the separate configuration and secrets, the manual deploy, the verification, and the rollback.
    - Search every snapshot file for a real IPv4 address, host name, password, token, or secret, and compare the hits with the addresses in the PDF; report a hit by path and kind, never by value.
    - Find the deployment record: the report's deployment line, the testing plan's `deployed` row, an issue or pull-request comment, a dated screenshot under `reports/week-05/images/`, or the meeting report.
    - Open the production and staging addresses once, from the university network if the agent can reach it, per `docs/grading-policy.md#consumer-hosted-media`; a view that cannot be reached is an evidence gap for that check only.
    - A VM that was not available is judged by its recorded postponement, its announced date, and its `## Deviations` entry, not by a deploy that could not happen.
    - The Moodle PDF's addresses are read once in step 2 and never copied into feedback.

11. Check the quality requirement tests and the testing plan together:

    ```sh
    rg -n "^## QR-|^\*\*Business importance:\*\*|^## QRT-|^\*\*Level:\*\*|^\*\*Status:\*\*|^\*\*Runs at:\*\*|^\*\*Pass when:\*\*|^### Procedure" "{TEAM_WORK}/snapshot/docs/quality-requirements" | head -n 80
    rg -n "^## Quality Requirement Testing Plan|^\| .*QRT-" "{TEAM_WORK}/snapshot/docs/project-plan.md" | head -n 40
    ```

    - The first projection answers which requirements are active and `High`, which of them carry a test, and each test's status, level, what runs it, and pass criterion, for the lines it prints; read each active `High` requirement's file in full when the projection is not enough.
    - The second projection answers the plan's columns and rows, in the page it prints; read the table in full when a row's evidence or linkage matters.
    - The rows are in `docs/project-plan.md`, and the `Checked` cells are the link between a test and `SPRINT-05`; the `**Checked QRs:**` list in S11 is built from those cells and from nothing else.
    - A `deployed` row's evidence must name the staging deployment, the measured value, and the commit; a `CI` row's evidence must be a green run on `main`.

12. Check the sprint milestones and the plan:

    ```sh
    gh api "repos/$REPO/milestones?state=all&per_page=100" \
      --jq '.[] | [.title, .due_on, .state, .open_issues, .closed_issues] | @tsv'
    gh api "repos/$REPO/issues?milestone=<number>&state=all&per_page=100" \
      --jq '.[] | [.number, .title, .state] | @tsv'
    ```

    - Find `SPRINT-05` to `SPRINT-09` in `milestones.json` and confirm the five Saturdays with the raw call.
    - Read `### SPRINT-05`'s fields and `## Milestones` from the snapshot, and add the planned stories' `Story Points` by hand from `issue-fields.json` for the planning-time set.
    - Read `SPRINT-05`'s milestone state and its open issues for S11, and the rescheduled issues' events for S12.
    - Read the GitHub project only to confirm the scheduled story is in it; the project's fields and table view were Week 3's and are not re-graded.
13. Check the features page against the records it links:
    - Read `docs/features.md` and each `US-nn`, `FR-nnn`, and `ADR-nnn` it links, and confirm every link and every first-use glossary anchor resolves.
    - Read `prs.json`'s `files` for each Week 5 pull request that changed an `FR-nnn`, an `ADR-nnn`, a glossary term an entry uses, or added a capability, and confirm `docs/features.md` is among its files.
14. Check the release against the tag:
    - Read `releases.json` for the tag names and dates; read the release title and body from the rendered release page or the raw `gh api "repos/$REPO/releases?per_page=100"` response, because the collector's dump omits them; read `gh api "repos/$REPO/git/refs/tags/<tag>"` for the commit the tag names.
    - Confirm that the tag's commit is an ancestor of `main`, with `gh api "repos/$REPO/compare/<tag>...main" --jq '.status'`, which is `ahead` or `identical` when it is.
    - Read the changelog's dated section, the plan's `REL-05` block, and `reports/week-05/README.md` at the snapshot, and find, for each, the pull request that first added it, with the commits API over the file's path.
    - Compare the merge time of those three pull requests with the tag's commit date; each must be later than, or at, the tag, and the changelog's dated section, the plan's block, and the report must be merged in that order.
    - Read `gh api "repos/$REPO/rulesets"` and each tag ruleset for the protection that covers tag pushes.
    - Build `**Checked QRs:**` from the testing plan's `Checked` cells: a requirement belongs when at least one of its tests has `SPRINT-05` there, whatever the row's `Status`.
15. Check the sprint close from the issue dumps and the plan:
    - From `issues.json`, take the stories closed as completed at `ISSUE_CUTOFF` in `SPRINT-05`'s milestone and their `Story Points` from `issue-fields.json`; add them by hand and compare the total with `**Actual Velocity:**`.
    - Read `reports/week-05/sprint-retrospective.md`'s four sections, their columns, and their row counts, and check each `## Carried Actions` row against `reports/week-04/sprint-retrospective.md`'s `Carried: Yes` actions.
    - Confirm every `Not done` action is re-listed in `## Actions` with `Carried: Yes`.
16. Scan the snapshot for private-only material:

    ```console
    uv run python scripts/scan_privacy.py A5 "<team_dir>"
    ```

    It reads `itpd-assignments-feedback/A5/work/<team_dir>/pdf-info.json`, strips inline `data:...;base64,` payloads, and checks email addresses, phone numbers, `.env` and key files, recording links outside meeting artifacts, and the real names from the PDF member table, including hits in meeting artifacts.
    It reports one line per file with a count, such as `docs/deployment.md: email address (x2)`, plus per-rule hit and file totals; the exit code is 1 when it finds any.
    Its rules do not include IPv4 addresses, so check the VM's address separately against the PDF's two addresses, and report a hit by path and kind.
    The raw fallback is email addresses with `grep -rnE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'`, phone numbers, the real names from the PDF member table, recording links in the submission and outside the meeting artifacts, `.env` files, and the two addresses from the PDF searched over the snapshot.
    Report each finding by path and kind only, with the number of hits per file.
17. Grade each of the 14 segments independently, and report each shortfall only in the segment that owns it in the [segment overview](#segment-overview).

## Assignment-specific constraints

- The `Primary index reviewed` metadata bullet points to `reports/week-05/README.md` at the snapshot whenever the snapshot is inspectable.
- Moodle-only items are judged from the PDF, and their absence from the repository is correct: the member table with real names and university emails, the staging and production addresses with the network note, the recording link, and a transcript the customer refused to publish.
- Never copy a real name, an email address, or the VM's address from the PDF into feedback; refer to people by GitHub username, to the customer as `Customer`, and to an address by the placeholder or by the kind of finding.
- A recording or external view that fails its single access check is an evidence gap for that check only, and the surrounding evidence is still judged.
- A transcript appendix does not count toward the PDF's two pages.
- Week 1 to Week 4 artifacts are not re-graded on their own requirements: repository setup, branch protection, the link-check configuration, Dependabot, the research content, the vision, the assumptions, the issue forms and fields, the project's table view, the risk register, the threshold of success, the plan's Week 3 and Week 4 parts, the Definition of Done's other sections, `CONTRIBUTING.md`, `docs/setup.md`, the documentation site, the functional requirements, the architecture document, the ADR records, the glossary, the team's `AGENTS.md`, `REL-04`, and the Week 1 to Week 4 meeting artifacts, reports, and retrospectives.
- Week 1 to Week 4 artifacts are checked only where Assignment 5 requires it: the plan's `### SPRINT-05` and `## Milestones` (S1), the testability requirement's critical modules (S3 and S5), the quality requirements index's active rows and its one link to the plan (S5 and S6), `docs/definition-of-done.md`'s `## Pull Request` list (S3), `docs/setup.md`'s link from the runbook (S4), the glossary's terms and anchors (S7), the Week 4 meeting report's action points and open questions (S8), the Week 4 retrospective's `Carried: Yes` actions (S12), `CHANGELOG.md`'s released section and `[Unreleased]` (S11), the link check and the Markdown check green on `main` (S3 and S13), and the `SPRINT-05` milestone and the issues in it (S2, S11, and S12).
- When a Week 4 artifact Assignment 5 builds on is absent, such as a quality requirements directory with no active `High` requirement, a Week 4 report with no action points, or a Week 4 retrospective with no file, judge the Assignment 5 item against what exists, report the absence in the segment that owns the artifact it should contain, and do not report the Week 4 absence again.
- A Week 4 report with no action point due in Week 5 or no open question makes `None` in the matching `## Previous` section correct, and it is never a shortfall.
- The Week 4 deadline extension does not move Week 5: the A4 cutoffs `2026-10-25T23:59:59+03:00` and, for `Team 2 - OK_10938_assignsubmission_file`, `2026-10-26T23:59:59+03:00` bound the Week 4 submission only, and the Week 5 cutoff stays `2026-10-31T23:59:59+03:00` for every team.
- A deployment claim that cannot be reached, with no other evidence route behind it, is a shortfall in S4; the unreachable external view alone is an evidence gap for that check only, and the deployment claim's repetition in the week report is judged once, in S4.
- Sanitize every screenshot before judging it as published evidence: a screenshot that shows the VM's address, a personal email, a real name, or a recording link is a visibility shortfall in the segment that owns the artifact it supports, reported by path and kind.
- A commit, comment, tag, deploy, or edit after `ISSUE_CUTOFF` is a caveat and never repairs the state at the cutoff; it is a shortfall only where a criterion names the cutoff, such as S11's tag date.
- The product code, its tests, its deployment, and its configuration are Week 5 deliverables: their absence is never excused as "not this week's".
- Week 6's analytics integration and telemetry, Week 7's usability testing, and Week 8's configuration management are not Assignment 5 deliverables, and their absence is never a shortfall.
- The course-materials submodule is Recommended; excluding its directory from both checks is allowed, and its absence is never a shortfall.
- Use the course's terminology in feedback: `Customer` for the person the team answers to, story issue, task issue, product backlog, product backlog refinement, sprint, sprint planning, sprint backlog, sprint review, sprint milestone, plan milestone, story points, velocity, retrospective, quality requirement, quality requirements index, quality requirement test, quality requirement testing plan, evidence, development environment, integration environment, staging environment, production environment, university VM, deployed test, deployment runbook, feature, feature documentation, glossary, functional requirement, architectural decision record, release, changelog, weekly report, weekly public report, private-only artifact, and deviation.
