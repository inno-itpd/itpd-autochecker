# Assignment 4 Grading Criteria

This rubric is for an LLM grading agent that reviews ITPD Assignment 4 team submissions.
ITPD assigns no points: each segment gets one status, `met`, `partial`, `missing`, or `unverified`, and an `Evidence gaps: yes|no` flag, per `docs/grading-feedback-format.md`.
The instructor assigns the grade from the statuses and the evidence, so this rubric never proposes a grade, a score, or a late penalty.
The shared rules live in `docs/grader-policy.md`: evidence states, verified absence, blocked and conflicting artifacts, snapshot resolution, live GitHub evidence through `gh api`, the single access check for consumer-hosted media, privacy, undeclared deviations, and rule applicability by `Since:` marker.
This file states only what is specific to Assignment 4 and does not repeat those rules.

## Authoritative sources

All paths are in the course-materials submodule, pinned at itpd commit `35c9294415d31c81a8598042b8b7419ea4481a46`.
If the checked-out submodule differs from that commit, read each file with `git -C A4/itpd show 35c9294415d31c81a8598042b8b7419ea4481a46:<path>`.

- `A4/itpd/assignments/assignment-4.md` — the student-facing brief: Parts 1–13, What Good Looks Like, the repository report contents, the Moodle PDF contents, the submission procedure, and the checklist.
- `A4/itpd/requirements/general-requirements.md` — artifact terms, the `reports/week-NN/` vs `docs/` split, the identifier rules including `FR-nnn`, `QR-nn`, and `ADR-nnn`, and traceability into later weeks.
- `A4/itpd/requirements/planning-requirements.md` — `docs/project-plan.md` with `## Milestones`, `## Sprints`, and `## Progress Monitoring`, the sprint's `**Due:**`, `**Sprint Backlog:**`, `**Planned Velocity:**`, and `**Actual Velocity:**` fields, the releases, and the threshold of success.
- `A4/itpd/requirements/sprint-ceremonies-requirements.md` — sprint planning, product backlog refinement, estimation, the Sprint Review, and the retrospective.
- `A4/itpd/requirements/issue-tracking-requirements.md` — the issue fields `MoSCoW`, `Story Points`, and `Priority`, scheduling, the assignees, and the public GitHub project's table view.
- `A4/itpd/requirements/user-stories-requirements.md` — story issues, their `User Story` type and `MoSCoW` value, acceptance criteria as checkboxes, and `### Specified by`.
- `A4/itpd/requirements/task-issues-requirements.md` — the `Task` issue type, the `### Requirements` section, acceptance criteria, and closing a task.
- `A4/itpd/requirements/quality-requirements-requirements.md` — `docs/quality-requirements/` with `qr/`, the ISO/IEC 25010:2023 pair, the six-part quality attribute scenario, and the priority matrix.
- `A4/itpd/requirements/functional-requirements-requirements.md` — `docs/functional-requirements/` with `fr/`, the requirement's fields, behavior, criteria, and the index.
- `A4/itpd/requirements/architecture-requirements.md` — `docs/architecture/README.md`, the drivers, the container view, the responsibilities table, diagrams and legends, and the ADR index.
- `A4/itpd/requirements/adr-requirements.md` — `docs/architecture/adr/`, the record's fields and body, and `**Addresses:**`.
- `A4/itpd/requirements/product-vision-requirements.md` — where the vision lives and the architecture document it links.
- `A4/itpd/requirements/customer-meetings-requirements.md` — the weekly meeting as the Sprint Review, showing working software, the permission questions, the script, report, and transcript.
- `A4/itpd/requirements/decisions-requirements.md` — the `DEC-nnn` entry, its fields, what cites it, and reversing it.
- `A4/itpd/requirements/releases-requirements.md` — `CHANGELOG.md`, Semantic Versioning, tags and their protection, and cutting a release.
- `A4/itpd/requirements/weekly-report-requirements.md` — the weekly public report, the AI usage report, declaring deviations, and the Moodle PDF.
- `A4/itpd/requirements/visibility-requirements.md` — what is public, what is Moodle only, and screenshot sanitization.
- `A4/itpd/requirements/glossary-requirements.md` — `docs/glossary.md` and its terms.
- `A4/itpd/requirements/agent-instructions-requirements.md` — the team's root `AGENTS.md` and what it states.
- `A4/itpd/requirements/pull-requests-requirements.md` — every change through a pull request, branch naming, review and approval, and closing a task issue.
- `A4/itpd/requirements/repository-requirements.md` — the documentation site, the link check and the Markdown check, and permalinks and snapshots.
- `A4/itpd/course/rules.md` — the course contract, the AI policy, the submission channel, and the Saturday-at-23:59 deadline policy.
- `A4/itpd/course/syllabus.md` — the Week 4 deliverables and minima, and the original Saturday hard deadline with no soft deadline; the instructor's Week 4 extension is recorded in [Assignment parameters](#assignment-parameters).
- `A4/itpd/guides/quality-and-architecture.md`, `A4/itpd/guides/planning-and-tracking.md`, and `A4/itpd/guides/validating-with-the-customer.md` — the method, used to judge quality and never as extra requirements.
- `A4/itpd/AGENTS.md` — course terminology and the `docs/` destination map for Week 4.

The pinned materials give Week 4's deadline as the original Saturday 24 October 2026.
The instructor extended Week 4 after the pin; the extension is recorded in [Assignment parameters](#assignment-parameters), supersedes those materials for Week 4 only, and leaves Weeks 5 to 9 on their Saturdays.

Apply every rule marked `**Since: W1**`, `**Since: W2**`, `**Since: W3**`, or `**Since: W4**`.
These `**Since: W5**` rules do not apply: product-code continuous integration, the Definition of Done item that names it, the component and sequence views, the testing plan and its tests, the production instance and deployment automation, analytics, usability testing, and configuration management.

## Assignment parameters

- Report title: `# Assignment 4 Feedback Report`
- Week: `W4`
- Course materials: `A4/itpd` at `35c9294415d31c81a8598042b8b7419ea4481a46`
- Primary index artifact: `reports/week-04/README.md` at the snapshot, as named in Assignment Report In The Repository and in Moodle item 3 of `assignment-4.md`.
- Soft deadline: none; `course/syllabus.md` and `course/rules.md` give Week 4 a single hard deadline.
- Original Week 4 deadline: Saturday 24 October 2026, 23:59, as the pinned `course/syllabus.md` and `assignments/assignment-4.md` state it; `course/rules.md` gives the Saturday-at-23:59 policy, not the date.
- Effective Week 4 deadline: Sunday 25 October 2026, 23:59 for every team except `Team 2 - OK_10938_assignsubmission_file`, whose effective deadline is Monday 26 October 2026, 23:59.
  The instructor extended Week 4 after the course materials were pinned; the extension supersedes the pinned Week 4 deadline and leaves Weeks 5 to 9 on their Saturdays.
- `ISSUE_CUTOFF`: `2026-10-25T23:59:59+03:00` for every team except `Team 2 - OK_10938_assignsubmission_file`, whose cutoff is `2026-10-26T23:59:59+03:00`.
  Read the team's exact `submissions/` directory name and use its cutoff; every later reference to `ISSUE_CUTOFF` means that team's cutoff, and `**Evidence:**` states the cutoff used.
- Before the cutoff of `Team 2 - OK_10938_assignsubmission_file`, a report judges the snapshot-based segments S3, S4, S5, S6, S7, and S9 (S5's live issue links and S9's `SKILL.md` URL are read as they stand), and marks S1, S2, S8, S10, S11, S12, S13, S14, S15, and S16 `unverified` with `Evidence gaps: yes` and the reason that the team's cutoff has not passed.
  This is the one case where `unverified` means the cutoff has not passed rather than that the evidence cannot be read; if the team has not submitted a PDF and snapshot yet, the whole report waits.
- Hard deadline of the following week: Saturday 31 October 2026, 23:59, the deadline the Week 5 syllabus block gives for `REL-05` and the due date `SPRINT-05`'s GitHub milestone carries; the Week 4 extension does not move it.
- The time zone is not stated; read every deadline as Innopolis time (UTC+3).
- Submission inputs: the Moodle PDF under `itpd-assignments-feedback/A4/submissions/<team_dir>/`; there is no ZIP, so the snapshot upload to Moodle is not judged.
  The snapshot is fetched from GitHub at the permalink SHA into `itpd-assignments-feedback/A4/work/<team_dir>/snapshot/`.
- Live artifact families: story and task issues with their types, field values, comments, timelines, and edit history; repository labels; pull requests with their reviews, files, and closing references; Actions runs of the Markdown check, the link check, and the Pages deployment; the repository's tags and releases; the seven sprint GitHub milestones; the organization's GitHub project with its fields and table view; the published documentation site; and the meeting recording link.
- Story and task issues, their types, their field values, their milestones, and the labels are not in the snapshot, so they are read live and judged as of `ISSUE_CUTOFF`, per [procedure step 6](#assignment-specific-procedure-deltas).
  An issue opened after the snapshot commit but by `ISSUE_CUTOFF` counts.
- Tags, releases, milestones, the GitHub project, and the documentation site are read live and judged as of `ISSUE_CUTOFF` too.
  An issue-field value has no history in the API: read the current value and read the issue's timeline for what changed after `ISSUE_CUTOFF`, and say so in `**Evidence:**` when the timeline cannot settle it.

The segments, in order:

- S1: Sprint plan and estimates
- S2: Product backlog refinement and issue fields
- S3: Quality requirements and priority matrix
- S4: Container view and responsibilities
- S5: Functional requirements and index
- S6: Architecture drivers and vision link
- S7: Architectural decision records and index
- S8: Issue catch-up
- S9: Glossary and team AGENTS.md
- S10: Week 3 action points and open questions
- S11: Customer validation of stories and architecture
- S12: REL-04 release
- S13: Sprint close and retrospective
- S14: Documentation site and navigation
- S15: Week report and submission
- S16: AI usage and honesty

### Segment overview

Every checklist item and every coverage-table row, or named part of a row, of `assignment-4.md` maps to exactly one segment, and a shortfall is reported only in the segment that owns it.

| Segment | Covers |
|---------|--------|
| S1: Sprint plan and estimates | Part 1 items 1–3; the planned-velocity part of coverage row Sprint plan and estimates; checklist item "SPRINT-04 planned with its goal, its `**Due:**` field, its `**Sprint Backlog:**` link, and its `**Planned Velocity:**`, and the later sprints' `**Due:**` fields and GitHub milestones moved to the five Saturdays" |
| S2: Product backlog refinement and issue fields | Part 1 items 4–7; coverage rows Product backlog refinement and Issue fields in the project view; checklist items "The next two sprints' worth of stories refined in the product backlog, with the `Story Points` on each and no sprint milestone" and "The three issue fields created, `Public`, pinned, and shown in the project's table view" |
| S3: Quality requirements and priority matrix | Part 2; coverage row Quality requirements; checklist items "3 or more `QR-nn` files under `docs/quality-requirements/qr/`, each with a different characteristic, the six scenario parts, and its row in `docs/quality-requirements/README.md`" and "The `Maintainability` / `Testability` requirement names its critical modules and carries `High` business importance" |
| S4: Container view and responsibilities | Part 3; the container-view part of coverage row Container view; checklist item "The container view: `docs/architecture/README.md` with `## Container View`, its image and source, `### Container Responsibilities`, and `## Diagrams And Legends`" |
| S5: Functional requirements and index | Part 4; coverage row Functional requirements; checklist item "5 or more `FR-nnn` files under `docs/functional-requirements/fr/`, each with its `**Traces to:**`, its `**Containers:**`, its `shall` statements, and its own criteria, and its row in the index" |
| S6: Architecture drivers and vision link | Part 5; the drivers-and-vision part of coverage row Architecture and drivers; checklist items "`docs/architecture/README.md` opens with the vision link, and its `## Drivers` links the four holders and names no requirement of its own" and "`docs/product-vision.md` links `docs/architecture/README.md`, and the vision keeps the goal, stakeholders, constraints, boundary, and system context" |
| S7: Architectural decision records and index | Part 6; coverage row Architectural decisions; checklist items "3 or more `ADR-nnn` files, each `**Addresses:**` at least one requirement, each with its options turned down and its accepted quality attributes covered by a `QR-nn`", "The ADR index with its four columns, active records above inactive ones, and each active record `Accepted`", and "The record that decides the split and the stack names every container in the view" |
| S8: Issue catch-up | Part 7; coverage row Issue catch-up; checklist item "Every issue from Weeks 2 and 3 in the Week 4 shape: the two types and a `MoSCoW` on every story, checkbox criteria, every story other than a `Won't Have` naming its `### Specified by`, every open task's `### Requirements`, and the six labels retired" |
| S9: Glossary and team AGENTS.md | Part 8; coverage rows Glossary and Team `AGENTS.md`; checklist item "`docs/glossary.md` with 3 or more terms, and a root `AGENTS.md` linking the course `SKILL.md` once" |
| S10: Week 3 action points and open questions | Part 9; coverage rows Week 3 action points and Week 3 open questions; checklist items "Each Week 3 action point's outcome in `## Previous action points`, and in the artifact it changed" and "Each Week 3 open question answered or carried forward in `## Previous open questions`" |
| S11: Customer validation of stories and architecture | Part 10; coverage rows Meeting script and Customer validation; checklist items "`reports/week-04/meeting-script.md`", "`reports/week-04/meeting-report.md`, with a `DEC-nnn` for each story shown and 2 or more action points due in Week 5", and "`reports/week-04/meeting-transcript.md`, if the meeting was recorded or held in writing"; Moodle items 4 and 5 |
| S12: REL-04 release | Part 11; coverage row `REL-04`; checklist item "The fourth release tagged, and the changelog's released section, the plan's `REL-04` line, and `reports/week-04/README.md` merged after the tag" |
| S13: Sprint close and retrospective | Part 12; the actual-velocity part of coverage row Sprint plan and estimates; coverage row Sprint retrospective; checklist item "`**Actual Velocity:**` set in `### SPRINT-04`, and `reports/week-04/sprint-retrospective.md` with its four sections and its first-retrospective `## Carried Actions`" |
| S14: Documentation site and navigation | Coverage row Documentation site; the published site's navigation and the links it serves |
| S15: Week report and submission | Assignment Report In The Repository items 1–5 and the Weekly Public Report rules: the report's own summary lines for the release and the customer-meeting outcome, the coverage table and its row links, the contribution table, the repository evidence, `## Deviations`, and the privacy line; Moodle items 1, 2, 3, and 6; the Submission Procedure; checklist items "`reports/week-04/README.md`", "Everything merged into `main`, with the permalink and the snapshot taken from that commit", and "PDF ready, and the permalink opened in a browser at the full commit hash"; the coverage table as an index. The underlying release, verdicts, retrospective, and AI usage are judged in S12, S11, S13, and S16. |
| S16: AI usage and honesty | Part 13; coverage row AI usage; checklist item "`reports/week-04/ai-usage.md`"; the AI Usage Report rules for Week 4 text |

The coverage-table rows map to the segment that judges the artifact in the row.
Whether the table has each row, and whether each row links, is judged in S15.

## Status guide

Use the status vocabulary of `docs/grading-feedback-format.md` and the evidence states of `docs/grader-policy.md`.
A segment is `met` only when every `met` criterion below holds on verified evidence.
A segment is `partial` when its core artifact exists and at least one verified shortfall remains.
A segment is `missing` when the `missing` criterion below holds.
A segment is `unverified` when its core evidence could not be read, such as S7 when the repository's ADR directory cannot be read at all, or S2 when neither the per-issue field values nor the project can be read and nothing else settles them.
Recommended items and the What Good Looks Like points are quality notes for the instructor, and they never cause a shortfall unless they coincide with a Required rule.

### S1 — Sprint plan and estimates

**Check:**

- `docs/project-plan.md` in the snapshot, its `### SPRINT-04` to `### SPRINT-09` sections, and the path history of the file.
- The repository's GitHub milestones: `milestones.json` for the titles and due dates, and the raw `gh api "repos/$REPO/milestones?state=all&per_page=100"` call at procedure step 12 for each milestone's state.
- The `User Story` issues in `SPRINT-04`'s milestone and their `Story Points`, from `issue-fields.json` or the REST `issue_field_values`.
- The pull requests in the team's Week 4 window that touch `docs/project-plan.md`, for when each sprint's fields were written.

**met:**

- `### SPRINT-04` opens with the sprint's goal in one sentence, stated as a result and not as a list of tasks, and the goal is the sprint's own rather than a provisional one.
- Under the goal, `### SPRINT-04` carries `**Due:**`, `**Sprint Backlog:**`, and `**Planned Velocity:**`, in that order, as a bulleted list.
- `**Due:**` is one of `2026-10-24`, `2026-10-25`, or `2026-10-26`, and never later than the team's effective deadline: `2026-10-25` for every team except `Team 2 - OK_10938_assignsubmission_file`, whose effective deadline is `2026-10-26`, so `2026-10-26` is accepted only for that team.
- `**Sprint Backlog:**` links the `SPRINT-04` GitHub milestone, and the link resolves to the milestone whose title begins `SPRINT-04:`.
- `**Planned Velocity:**` is a whole number, and it equals the sum of the `Story Points` of the stories the milestone held when the sprint was planned, from its `milestoned` events where they exist and from its current stories otherwise; a story added mid-sprint does not change the planned figure.
- `SPRINT-05` to `SPRINT-09` each carry `**Due:**` with `2026-10-31`, `2026-11-07`, `2026-11-14`, `2026-11-21`, and `2026-11-28`, in that order.
- The seven `SPRINT-nn` GitHub milestones exist, `SPRINT-03` to `SPRINT-09`, each titled `SPRINT-nn: <focus>` with the sprint's number. `SPRINT-03`'s milestone exists, but its due date and open or closed state are Week 3's and are not re-graded here. `SPRINT-04`'s due date is the same accepted date as its `**Due:**`; its state belongs to S12. `SPRINT-05` to `SPRINT-09` are due on the five Saturdays above and are open.
- Every sprint section from `### SPRINT-04` on nests exactly one `#### REL-nn` heading, `REL-04` to `REL-09` in order; `### SPRINT-03` keeps its `#### REL-03` and is not re-graded here. The plan copies no issue list into the file.

**partial:**

- `docs/project-plan.md` has `### SPRINT-04` and the later sprint sections, and at least one other `met` criterion fails.
- Typical shortfalls: a provisional goal left in `SPRINT-04`; `**Planned Velocity:**` absent, not a whole number, or not the sum of the planned stories; a due date other than one of the accepted Week 4 dates or the five Saturdays; a `SPRINT-04` milestone whose due date disagrees with `**Due:**`; a due date after the team's effective deadline; a sprint milestone missing or titled without the sprint number; a future sprint's milestone closed early; a missing `REL-nn`.

**missing:**

- `docs/project-plan.md` is absent at the snapshot, or it has no `### SPRINT-04` section with a goal.

**Guardrails:**

- A sprint's due date is judged against this prompt and the team's effective deadline, not the pinned course materials' original date.
  Week 4's original date was Saturday 24 October 2026; the instructor extended it to Sunday 25 October 2026 for every team except `Team 2 - OK_10938_assignsubmission_file`, which has Monday 26 October 2026.
- From Week 5 to Week 9 every submission is due on Saturday at 23:59, with no soft deadline, and the five later Saturdays follow one week apart.
- The plan's `## Milestones` and `## Progress Monitoring` parts and the `SPRINT-03` section were Week 3's and are not re-graded here.
- `**Actual Velocity:**` belongs to S13, and its absence from this segment is not a shortfall here.
- A plausible number that is not the exact sum is the shortfall the rule names; do not accept a rounded total.
- A sprint section written after the sprint started is a caveat in `**Evidence:**`, never a shortfall, unless the goal was plainly written from what happened.
- Whether `SPRINT-04`'s goal and `**Planned Velocity:**` were set at planning is a caveat in `**Evidence:**`, read from the plan's path history against the sprint's first story close; it is a shortfall only when the history plainly shows the number was written after the sprint's stories had closed.
- When the milestone's timeline is unavailable and the current story set differs from the planning-time set, compare the number with the stories the report or the issues place at planning, and say in `**Evidence:**` which set was used.
- The focus phrase in a milestone title is the team's choice and is not judged.

### S2 — Product backlog refinement and issue fields

**Check:**

- `issue-fields.json` (the collector's `--issue-fields` mode), the REST `issue_field_values` of each issue, the organization `issueFields` list when the token can read it, and the issue sidebar, for the three new fields, their definitions, and their values.
- The project's fields, its table view, and its columns, from `gh project field-list <number> --owner <org> --format json`, `gh project view <number> --owner <org> --format json`, the project page, and the GraphQL items and views query in [procedure step 12](#assignment-specific-procedure-deltas).
- The `User Story` issues in no sprint milestone and in `SPRINT-04`'s milestone, from `issue-fields.json` and `issues.json`.
- The repository's GitHub milestones, for the milestone each story sits in.

**met:**

- The issue fields `MoSCoW`, `Story Points`, and `Priority` exist, each single-select and `Public`, read from the organization `issueFields` list when the token can read it and otherwise from the issue sidebar; a definition neither route can settle is an evidence gap for that criterion, not a shortfall.
- `MoSCoW`'s options are `Must Have`, `Should Have`, `Could Have`, and `Won't Have`; `Story Points`'s options are `1`, `2`, `3`, `5`, `8`, and `13`; `Priority`'s options are `High`, `Medium`, and `Low`.
- `MoSCoW` and `Story Points` are pinned to the `User Story` issue type, `Priority` is pinned to the `Task` issue type, and no field is pinned to `Issues without a type`.
- The project has at least one table view whose columns include the `Responsible`, `Accountable`, `MoSCoW`, `Story Points`, and `Priority` fields, the built-in `Assignees`, and the built-in `Milestone`, grouped or sorted by `Milestone`.
- The three new fields appear in that table view beside the two role fields, the assignees, and the milestone.
- Every open `User Story` that sits in no sprint's GitHub milestone, is not `Won't Have`, and is among the next two sprints' worth of the product backlog carries its `Story Points`.
- Every open `User Story` that sits in no sprint's GitHub milestone has no `Responsible` value, no `Accountable` value, and no assignees.
- No story carries more than `13` story points, and no story larger than `13` points is scheduled in a milestone.
- Every `User Story` issue scheduled into `SPRINT-04`'s milestone carries a `Story Points` value.
- Every `Task` issue scheduled into `SPRINT-04`'s milestone carries a `Priority` value.

**partial:**

- At least one of the three fields `MoSCoW`, `Story Points`, or `Priority` is readable from an issue's field values or its sidebar, or the project has a table view, and at least one other `met` criterion fails.
- Typical shortfalls: a field pinned to nothing or to `Issues without a type`; an option missing or an extra option; a field with `Organization` visibility while the project is public; no table view, or a view without one of the five fields, the assignees, or the milestone; an open product-backlog story that carries `Responsible`, `Accountable`, or assignees; a scheduled story without `Story Points`; a scheduled task without `Priority`; a story among the next two sprints' worth without `Story Points`; a story over `13` points.

**missing:**

- The three fields are absent: no issue's field values or sidebar names `MoSCoW`, `Story Points`, or `Priority`, and the project has no table view, at `ISSUE_CUTOFF`. When the fields may exist but neither the organization `issueFields` list, the issue sidebar, nor the project can be read, the segment is `unverified` with `Evidence gaps: yes`.

**Guardrails:**

- Read the per-issue values first. The organization `issueFields` list is evidence only when the token can read it; it needs organization membership the token may not have, so an empty list or `totalCount: 0` never means a field is absent. When the token cannot read it, the issue sidebar answers the definitions and values; a definition the sidebar cannot settle is an evidence gap for that criterion, not a shortfall.
- A project's own fields and the organization's issue fields are different: the issue's sidebar and `issue_field_values` name the issue fields, while `gh project field-list` answers for the project's fields. Say in `**Evidence:**` which route answered.
- A direct `fields` selection on the project type is a union and raises `selectionMismatch`, so read field names, options, and data types from `gh project field-list`.
- A `Won't Have` story is not estimated or scheduled, so its lack of `Story Points` is not a shortfall. It still carries no `Responsible`, `Accountable`, or assignees while it is open and unscheduled.
- The refinement's quantity is the team's judgement: judge the stories the team has placed in the next two sprints' worth of the product backlog, name them, and do not require an estimate on every open backlog story. The assignment's "next two sprints' worth" is the planning horizon, not a numeric floor, and a story beyond it need not carry `Story Points` yet; it still carries no milestone, no roles, and no assignees while it stays in the backlog.
- Whether every issue carries its type and its `MoSCoW` value belongs to S8; this segment judges the field definitions, the values on the scheduled and backlog stories, and the project view.
- The `Responsible` and `Accountable` fields and their values were Week 3's; here only their presence in the table view and the unscheduled-story rule are judged.
- An already closed issue needs no values, and a value stays on it after it closes.
- A story added to `SPRINT-04` mid-sprint is a quality note when it was refined and estimated, and a shortfall when it was not.
- The project's auto-add workflow and adding items by hand both count.

### S3 — Quality requirements and priority matrix

**Check:**

- `docs/quality-requirements/README.md` and every `docs/quality-requirements/qr/QR-nn.md` in the snapshot.
- The repository paths the `Maintainability` / `Testability` requirement names, in the snapshot.
- The rendered permalinks of the index and one requirement, for the links and the table.
- Every `ADR-nnn` a quality requirement file names, for the rule that a quality requirement cites no ADR.

**met:**

- `docs/quality-requirements/README.md` and at least 3 files under `docs/quality-requirements/qr/`, each named `QR-nn.md` with a two-digit number.
- The 3 or more requirements carry different `**Characteristic:**` values, so each is a different characteristic.
- Every requirement's heading is `# QR-nn: <short outcome>`, and the first line below it is the outcome in one sentence that a reviewer could fail.
- Every requirement's fields are a bulleted list in the order `**Status:**`, `**Characteristic:**`, `**Sub-characteristic:**`, `**Business importance:**`, `**Technical risk:**`, then `**Changed:**` only when it changed, and `**Dropped:**` only on a dropped requirement.
- Every `**Status:**` is `Active` or `Dropped`; every `**Characteristic:**` and `**Sub-characteristic:**` is one allowed pair from the ISO/IEC 25010:2023 table in its Title Case; every `**Business importance:**` and `**Technical risk:**` is `High`, `Medium`, or `Low`.
- Exactly one pair per requirement, so a requirement that addresses two sub-characteristics is two files.
- At least one requirement carries `**Characteristic:** Maintainability` and `**Sub-characteristic:** Testability`, with `**Business importance:** High`, and names its critical modules by repository path, including the product's frontend entry point and its payment module where the product has them, so each named path exists in the snapshot.
- Not every active requirement carries `**Business importance:** High`, so the matrix's first sort distinguishes rows; a matrix whose every active row is `High` is the shortfall Part 2 item 4 names.
- Every requirement carries `## Scenario` with exactly the six `###` sub-headings `Source`, `Stimulus`, `Environment`, `Artifact`, `Response`, and `Response Measure`, in that order.
- Each of the six parts states its one thing, and the `Response Measure` is a number, a threshold, a conformance outcome, or a state a reviewer can observe, not an adjective.
- The scenario states the behavior rather than the design tactic, so it names no cache, queue, library, or product as the answer.
- A dropped requirement keeps its file, its title, and its six scenario headings, with `**Status:**` `Dropped` and a `**Dropped:**` field giving the date and the reason and citing the `DEC-nnn` when a decision caused the drop.
- A requirement that changed without dropping records each change under `**Changed:**` as a gap records one.
- A requirement cites no `ADR-nnn` and carries no `ASR` field.
- The index has one row per `QR-nn`, with the columns `QR`, `Outcome`, `Business importance`, `Technical risk`, `Characteristic`, `Sub-characteristic`, and `Status`, in that order.
- Each `QR` cell is the identifier as link text, linked to its file under `qr/`; each `Outcome` repeats the requirement's one-sentence outcome; each `Status` matches the requirement file.
- The index rows are sorted active first, then `**Business importance:**` from `High` to `Low`, then `**Technical risk:**` from `High` to `Low`, with `QR-nn` order breaking a tie.
- The index repeats none of the scenario.

**partial:**

- The index and at least 3 `QR-nn` files exist, and at least one other `met` criterion fails.
- Typical shortfalls: fewer than 3 requirements; two requirements with the same characteristic; a field missing or out of order; a characteristic or sub-characteristic outside the table or not in Title Case; a scenario part missing, renamed, or out of order; a `Response Measure` that is an adjective; a scenario that names a cache, a queue, or a library; the testability requirement missing, not `High`, or naming no repository path; every active row `High`; index columns out of order, rows unsorted, cells unlinked, or a status that disagrees with its file.

**missing:**

- `docs/quality-requirements/` is absent at the snapshot, or it holds no `QR-nn` file.

**Guardrails:**

- A scenario that names the design tactic is the shortfall the rule names; the tactic belongs in an ADR, and the requirement states the behavior.
- "Every row High" is judged on the active requirements' `Business importance`; one active `Medium` row makes the matrix sort, and the distribution beyond that is the team's quality judgement.
- A requirement with no `**Changed:**` field has not changed, and that is correct.
- An active requirement that no ADR `**Addresses:**` is not a shortfall here; the ADR side belongs to S7 and the trace is one-directional.
- The requirement's outcome need not be met in the product yet; this segment judges the requirement's shape, not its achievement.
- Whether a response measure could be automated is Week 5's testing plan, not this segment.
- The index is the list; a weekly report that links the index is not a second list.
- A requirement file that carries the pair as an index value only, with no scenario, is not a requirement yet.

### S4 — Container view and responsibilities

**Check:**

- `docs/architecture/README.md`, the image at `docs/architecture/container.<ext>`, and its committed source, in the snapshot.
- The record the view's opening sentence links.
- Every `FR-nnn` `**Containers:**` value under `docs/functional-requirements/fr/`, for the container set.
- The rendered architecture page, for the embedded image and the table.

**met:**

- `docs/architecture/README.md` carries `## Container View` above `### Container Responsibilities`, and its `## Diagrams And Legends` section comes after the views.
- `## Container View` opens with one sentence that links the record deciding the stack and the container split, and that record exists.
- Below the sentence, the container diagram is embedded as an image committed under `docs/architecture/`, with its source committed beside it.
- The diagram shows at least two containers, each an application or a data store the team deploys or rents, and each label names the container and its technology.
- The diagram shows the external systems a container exchanges data with, or says there are none, and no external actor.
- The container names in the diagram match, with the same spelling, the rows of `### Container Responsibilities`, with no container in one and not the other.
- `### Container Responsibilities` holds one table with the columns `Container` and `Responsibilities`, in that order, one row per container in the diagram's order.
- Each `Responsibilities` cell gives two to five responsibilities in one sentence, each clause starting with a verb and separated by a semicolon, and at least one clause says what data or state the container owns.
- A responsibility names no library, framework version, or vendor product.
- Every container is named by at least one functional requirement's `**Containers:**` field or is a store those requirements use.
- A product that genuinely runs as one container says so in the section's opening sentence in place of the count, and the responsibilities table has that one row.
- The view is a view and not a decision: the reason for the split and the stack stays in the linked record, and the section adds no second decision.
- `## Diagrams And Legends` carries one legend naming every shape, colour, and arrow the document's views use, and the tool and the source of each image.
- Every arrow in the diagram says what crosses it, such as a protocol, a request, or an event.
- Every element the document names in prose appears in a view, and the views agree with the document's text and with the vision's boundary.

**partial:**

- `docs/architecture/README.md` carries `## Container View` and `### Container Responsibilities`, and at least one other `met` criterion fails.
- Typical shortfalls: no image, or an image with no committed source; one container without the one-container sentence; a label without its technology; an external actor in the container diagram; a container in the diagram but not the table, or spelled differently; one responsibility or six; a responsibility naming a framework or a vendor; no responsibility that owns data or state; a container no functional requirement names; no legend, no tool, no source, or an unlabelled arrow.

**missing:**

- `docs/architecture/README.md` is absent at the snapshot, or it carries no `## Container View` section.

**Guardrails:**

- Judge the container set against what the product runs as, not against the code's directories: a monolith that genuinely runs as one container is correct with one row and its sentence.
- A container is an application or a data store that has to be running; a library, a module, a JAR, a package, or a database table is not a container.
- Read the committed source, such as Mermaid, PlantUML, D2, or the draw.io XML, and the image itself for the labels, the arrows, and the external systems; an image whose labels cannot be read is an evidence gap for that criterion only.
- The diagram's layout, style, and tool are quality notes.
- Week 5's component and sequence views are not expected; their absence is never a shortfall, and a team that added them early is not judged on them here.
- The record's own content belongs to S7; this segment judges only that the view links it and that the link resolves.
- The architecture document's opening sentence and the order of its top-level parts belong to S6, and the ADR index to S7.
- A product with no external system says so or shows none, and an empty arrow set is correct.

### S5 — Functional requirements and index

**Check:**

- `docs/functional-requirements/README.md` and every `docs/functional-requirements/fr/FR-nnn.md` in the snapshot.
- The container view's names, for each `**Containers:**` value.
- Every `US-nn`, `DEC-nnn`, `CON-nn`, `ADR-nnn`, and meeting report a `**Traces to:**` links, for existence.
- The rendered index, for its links and its order.

**met:**

- `docs/functional-requirements/README.md` and at least 5 files under `docs/functional-requirements/fr/`, each named `FR-nnn.md` with a three-digit number.
- Every file's heading is `# FR-nnn: Title`, and one file carries one requirement.
- Every requirement's fields are a bulleted list in the order `**Status:**`, `**Traces to:**`, `**Containers:**`, then `**Changed:**` only when it changed, and `**Dropped:**` only on a dropped requirement.
- Every `**Status:**` is `Active` or `Dropped`.
- Every `**Traces to:**` holds at least one entry, each linked: an origin, which is a `US-nn`, a `DEC-nnn`, a `CON-nn`, or a meeting report, or the `ADR-nnn` that constrains the requirement.
- The requirement has no `**Stories:**` field, no `ASR` field, does not restate the story, and the repository keeps no second list of stories.
- Every `**Containers:**` value is a container the container view lists, spelled as the view spells it, and it names the containers the behavior runs in rather than every container the behavior touches.
- `## Behavior` holds one or more `shall` statements, each naming its actor, its condition, and its observable outcome, and each naming no task issue, sprint, pull request, or library.
- `## Acceptance Criteria` holds one `### AC-nn` section per criterion, `AC-01` upward, numbered within the requirement and never renumbered or reused there, and every requirement carries at least one.
- Every criterion is a verifiable assertion: a given and an expected result, an example input and output, a configuration table, or a state a reader can observe, and none needs a scenario notation to be checkable.
- A dropped requirement keeps its file, its title, and its `### AC-nn` sections, with `**Status:**` `Dropped` and a `**Dropped:**` field giving the date and the reason and citing the `DEC-nnn` or `ADR-nnn` when one caused the drop.
- A requirement that changed without dropping records each change under `**Changed:**`.
- The index has one row per `FR-nnn`, in `FR-nnn` order, with the columns `FR`, `Title`, `Containers`, and `Status`, in that order.
- Each `FR` cell is the identifier as link text, linked to its file under `fr/`; each `Title` repeats the title after the colon in the file's heading; each `Containers` repeats the requirement's names; each `Status` matches the requirement file.
- The index repeats neither the behavior nor the criteria, and it is the only list of functional requirements in the repository.

**partial:**

- The index and at least 5 `FR-nnn` files exist, and at least one other `met` criterion fails.
- Typical shortfalls: fewer than 5 requirements; a field missing or out of order; a `**Traces to:**` entry that is not an origin or an ADR, or that does not resolve; a requirement that restates its story; a `**Containers:**` value absent from the view or naming a store the behavior does not run in; a `shall` statement with no actor, condition, or outcome; an acceptance criterion that is an adjective; a requirement with no criterion; index rows out of order, unlinked, or a status that disagrees with its file.

**missing:**

- `docs/functional-requirements/` is absent at the snapshot, or it holds no `FR-nnn` file.

**Guardrails:**

- `**Traces to:**` is provenance and constraint, not a reverse index: it names where the requirement came from and what limits it, and it does not list the story that consumes it.
- The ADR link is the requirement's own record of the constraint, and the ADR's `**Addresses:**` is S7's; both facts may be written in either order.
- Judge the behavior and the criteria for verifiability, not for whether the product implements them.
- A requirement's title is not its outcome, and the title's wording is the team's choice.
- The `**Containers:**` values are judged against the container view's rows, not against the code's directories.
- A story that names the requirement in `### Specified by` is S8's; here only the requirement's own side is judged.
- The assignment's "do not keep a second list of stories" is judged by the repository's files, not by the issue list.
- A criterion's notation is free; only a criterion that nobody but its author could run is the shortfall.

### S6 — Architecture drivers and vision link

**Check:**

- `docs/architecture/README.md` and `docs/product-vision.md` in the snapshot, and `docs/threshold-of-success.md` for the vision goal's link.
- The four holders `## Drivers` links: `docs/threshold-of-success.md`, `docs/product-vision.md#constraints`, `docs/functional-requirements/README.md`, and `docs/quality-requirements/README.md`.
- The rendered architecture page and vision page, for the links and the section order.

**met:**

- `docs/architecture/README.md` opens with one sentence that links `docs/product-vision.md` as the scope the document serves.
- After the title and the opening sentence, the document carries the parts `## Drivers`, `## Container View` with `### Container Responsibilities`, `## Diagrams And Legends`, and `## Architectural Decisions`, in that order, and no trace section.
- `## Drivers` carries four entries, in this order, as a bulleted list rather than a table:
  - The business goals entry links `docs/threshold-of-success.md` in full, because a goal is its own `## TOS-nn` section.
  - The constraints entry links `docs/product-vision.md#constraints`.
  - The functional requirements entry links `docs/functional-requirements/README.md`.
  - The quality requirements entry links `docs/quality-requirements/README.md`.
- Each entry says which group it is and links the group; the section names no `TOS-nn`, `CON-nn`, `FR-nnn`, or `QR-nn`, and restates no goal, constraint, or requirement.
- The section links neither the boundary nor the system context.
- Every link in `## Drivers` resolves in the snapshot, and each named anchor exists.
- `docs/product-vision.md` links `docs/architecture/README.md` as a whole.
- The vision's goal links `docs/threshold-of-success.md`, per the Week 3 rule.
- The vision keeps the goal, the stakeholders, the constraints, the boundary, and the system context, and the context diagram stays embedded in the vision.
- No part of the vision moved into the architecture document, and neither file copies the other.

**partial:**

- The architecture document and the vision exist with a `## Drivers` section, and at least one other `met` criterion fails.
- Typical shortfalls: no opening sentence linking the vision; the parts out of order; a drivers table instead of a list; a missing or misordered entry; a drivers entry that names identifiers or restates a goal; the boundary or the system context linked from the drivers; a broken link; a vision that does not link the architecture; a vision section moved into the architecture document or copied there.

**missing:**

- `docs/architecture/README.md` is absent at the snapshot, or it carries no `## Drivers` section, or `docs/product-vision.md` is absent.

**Guardrails:**

- The drivers section is a map, not an argument: an entry that restates a goal or lists a requirement is the shortfall, and one line per entry is a quality note.
- The boundary and the system context are scope; the opening sentence links the vision for both, and a drivers entry that links either is the shortfall.
- The vision's own content was Week 2's and Week 3's; here only its architecture link, its goal's threshold link, and the presence of its five parts are judged.
- The architecture document's `## Container View` internals belong to S4 and its ADR index to S7; this segment judges the document's shell and the drivers.
- A drivers link that points at a section which exists but is empty resolves, and the empty section is a quality note.
- Week 5's component and sequence views are not expected, and the document's order is judged without them.

### S7 — Architectural decision records and index

**Check:**

- `docs/architecture/adr/ADR-nnn.md`, `docs/architecture/adr/TEMPLATE.md`, and `docs/architecture/README.md`, in the snapshot.
- Every `FR-nnn` and `QR-nn` an `**Addresses:**` links, for existence.
- Every `DEC-nnn` a `**Decision:**` links.
- The container view's rows, for the record that names every container.
- The rendered ADR index.

**met:**

- `docs/architecture/adr/TEMPLATE.md` exists as the shape to copy, and at least 3 `ADR-nnn.md` files exist, each with a three-digit number.
- Every record's heading is `# ADR-nnn: Title`.
- Every record's fields are a bulleted list in the order `**Status:**`, then `**Superseded by:**` only on a superseded record, then `**Dropped:**` only on a dropped record, then `**Created:**`, `**Updated:**`, `**Containers:**`, `**Addresses:**`, and `**Decision:**` only when a `DEC-nnn` exists.
- Every `**Status:**` is `Proposed`, `Accepted`, `Superseded`, `Deprecated`, or `Dropped`; a superseded record links its replacement in `**Superseded by:**`; a dropped record gives the date and the reason in `**Dropped:**`.
- Every `**Containers:**` value is a container name from the architecture document's container view.
- Every `**Addresses:**` lists one or more `FR-nnn` and `QR-nn`, each linked, with no relation word such as `satisfies`, `enables`, or `constrains`.
- Every `**Addresses:**` entry resolves to a file that exists at the snapshot.
- The record that decides the stack and the container split names every container the view lists, and the view's opening sentence links it.
- The record's body carries `## Context`, `## Considered Options`, `## Decision Outcome`, and `## Consequences`, in that order.
- `## Considered Options` names each option considered, and for each one turned down, why it lost.
- `## Decision Outcome` names the option chosen and why it beats the others.
- `## Consequences` says what the choice gives and costs, and names each quality attribute it accepts with the `QR-nn` that covers it, linked; a record that accepts a quality attribute with no `QR-nn` is not ready.
- A record's reasoning stays in the record: the `DEC-nnn` it names carries only what the customer decided, and a technology or functional-behavior choice is a record rather than a `DEC-nnn`.
- The three minimum records are `Accepted` before submission, so at least three records carry `**Status:** Accepted`.
- The ADR index is one table under `## Architectural Decisions`, with the columns `ADR`, `Status`, `Addresses`, and `Decision`, in that order.
- Each `ADR` cell is the identifier as link text, linked to its file under `adr/`; each `Status` matches the record's `**Status:**`; each `Addresses` cell names every `FR-nnn` and `QR-nn` the record accounts for, each linked; each `Decision` cell gives the chosen option in one line.
- The active rows come first, in `ADR-nnn` order, and the inactive rows follow, in `ADR-nnn` order.
- Every record is listed in the index once, and no record is missing from it.

**partial:**

- At least 3 records and an index exist, and at least one other `met` criterion fails.
- Typical shortfalls: no template; a heading without the identifier and title; a field missing or out of order; an invalid status; a container not in the view; no `**Addresses:**`, an unlinked one, or one with a relation word; the stack record missing a container; a body section missing, out of order, or an options list with no rejected options; `## Consequences` with no `QR-nn` link; fewer than three `Accepted` records; index columns wrong, rows unordered, a record missing, or a status that disagrees with its file.

**missing:**

- `docs/architecture/adr/` is absent at the snapshot, or it holds no `ADR-nnn` file.

**Guardrails:**

- The stack record is judged by the containers it names, not by whether the stack is good; the quality of the choice is never a shortfall.
- An ADR is not a `DEC-nnn`: a technology or behavior choice recorded only as a `DEC-nnn` leaves the record missing, and a `DEC-nnn` the record names is the customer's mandate, not the record itself.
- A record may name several requirements, and an `**Addresses:**` cell that lists them all is correct; a requirement that no record names is not this segment's shortfall.
- The `Decision` index cell is the chosen option's short name; a longer sentence is a quality note.
- `**Updated:**` records the last edit that left the decision as it was; a changed decision is a new record that supersedes this one, not an edit.
- Week 3's `DEC-nnn` entries and the stack's Week 3 record are not re-graded; this segment judges the record that documents the stack now.
- The index's `Addresses` column is the one map from a requirement to its record; a second driver table is a quality note.
- A record that keeps its file and body after being superseded is correct; do not require it to be rewritten.

### S8 — Issue catch-up

**Check:**

- `issues.json`, `issue-fields.json`, and each story's and task's body, comments, timeline, and edit history, at `ISSUE_CUTOFF`.
- The repository labels, from `labels.json`.
- The issue types, from `issue-fields.json` or the REST `type.name`.
- Every `FR-nnn` and `ADR-nnn` a `### Specified by` or `### Requirements` links, for existence.

**met:**

- Every story issue, open or closed, that was opened on or after `2026-10-02T00:00:00+03:00` carries the `User Story` issue type.
- Every story carries one `MoSCoW` value, one of `Must Have`, `Should Have`, `Could Have`, or `Won't Have`.
- Every task issue carries the `Task` issue type.
- No open issue carries any of the six labels `user-story`, `task`, `moscow:must`, `moscow:should`, `moscow:could`, or `moscow:won't`.
- Every story's acceptance criteria are checklist items of the form `- [ ] AC-nn: <criterion>` or `- [x] AC-nn: <criterion>`, each keeping its `AC-nn`.
- Every story other than a `Won't Have` story carries `### Specified by`, and the section names each `FR-nnn` and `ADR-nnn` that specifies the story, each linked on `main`, including the stories that closed in Weeks 2 and 3.
- Every `FR-nnn` and `ADR-nnn` a `### Specified by` links exists at the snapshot, and each entry is one of those two families.
- Every open task carries `### Requirements`, and the section names each `FR-nnn` and `ADR-nnn` the task works on, each linked on `main`, or the one line saying it serves none, such as `None: repository upkeep`.
- Every `FR-nnn` and `ADR-nnn` a `### Requirements` links exists at the snapshot.
- No issue carries a comment that records the one-time catch-up: no comment in the Week 4 window says that the type, the `MoSCoW` value, the checkboxes, `### Specified by`, or `### Requirements` were added by this pass.

**partial:**

- Some stories and tasks carry their type, and at least one other `met` criterion fails.
- Typical shortfalls: an issue with no type; a story with no `MoSCoW` value; an open issue still carrying one of the six labels; criteria written as plain bullets; a story with no `### Specified by` or an empty one; a task with no `### Requirements`; a `### Specified by` naming a `US-nn` or another family; a catch-up comment; an unlinked specification.

**missing:**

- At `ISSUE_CUTOFF`, none of the catch-up's carriers is present: no story carries the `User Story` type, no story carries a `MoSCoW` value, and no task carries the `Task` type.

**Guardrails:**

- Judge the end state at the cutoff; a one-time catch-up is judged by its end state, not by when each edit landed, and an edit made after the snapshot but by the cutoff counts.
- The catch-up is one change: do not fail because its edits cluster in one day or are spread over the week, and the absence of a per-issue change comment is the criterion.
- A `Won't Have` story keeps its `US-nn` and needs no `### Specified by`, but it still carries the type and a `MoSCoW` value.
- A closed story still carries its type, its `MoSCoW` value, and `### Specified by`; only its criteria ticks are state.
- The type and the fields are the only carriers: there is no label substitute, and a team whose organization cannot create them declares a deviation.
- The six labels retire from the open issues: a label object that still exists but is carried by no open issue is not a shortfall, because the requirement's observable is that no open issue carries one.
- A bot's issue or a workflow's pull request issue is not a task and is not judged.
- The story's `### Specified by` is its conformance, not an origin, and the requirement does not name the story back.
- An issue opened after `ISSUE_CUTOFF` is not judged.
- The `### Requirements` line that says the task serves none is correct for repository upkeep and is never a shortfall.

### S9 — Glossary and team AGENTS.md

**Check:**

- `docs/glossary.md` and the root `AGENTS.md` in the snapshot.
- The artifacts a `**Defined by:**` line links, for existence and for what they define.
- The course `SKILL.md` URL, for its one occurrence and its target.
- The repository layout, checks, and conventions, for what `AGENTS.md` states.

**met:**

- `docs/glossary.md` sits in `docs/` and holds at least three terms.
- Each term is a `### Term` section under the heading of the domain it belongs to, and the term's heading is the term alone, so its anchor is `#<term>`.
- Each term's definition is one sentence stating what the term means in this project, not what it means in general.
- Where an artifact already defines the term, a `**Defined by:**` line under the definition links that artifact, and the link resolves.
- A term no artifact defines stands on its definition alone.
- The terms are words the product's own artifacts and interface use.
- The repository root carries `AGENTS.md`, named exactly that.
- `AGENTS.md` states the repository layout, with what each directory holds and where a new file goes.
- `AGENTS.md` states the checks, with how to run each check the repository has, by the command a member runs locally or the workflow that runs it in CI.
- `AGENTS.md` states the conventions: the commit message format, the branch naming, and the code style.
- `AGENTS.md` states the files an agent must not edit, each by path, with the condition under which a member makes the edit instead.
- `AGENTS.md` links the course repository's `SKILL.md` by its GitHub URL, `https://github.com/inno-itpd/itpd/blob/main/SKILL.md`, once, as the router to the course requirements.
- `AGENTS.md` maps no artifact path to a requirements file, and it does not copy the course requirements.

**partial:**

- The glossary and the team `AGENTS.md` exist, and at least one other `met` criterion fails.
- Typical shortfalls: fewer than 3 terms; a heading that carries the definition or is a sentence; a definition that is general rather than project-specific; a `**Defined by:**` link that does not resolve; no domain heading; `AGENTS.md` missing one of its four sections; the `SKILL.md` link repeated, relative, or missing; an artifact-to-requirements map copied in.

**missing:**

- `docs/glossary.md` is absent at the snapshot, or the root `AGENTS.md` is absent.

**Guardrails:**

- The glossary is the project's ubiquitous language, not a course glossary: a definition that would fit any project is the shortfall, and a term the team invented for its own artifact is a good entry.
- `**Defined by:**` is optional per term and required only when an artifact already defines the term.
- The number of terms is judged at the minimum; a longer glossary is a quality note, and completeness is judged against the project's own artifacts rather than against every noun.
- A word the team uses in its own sense should have an entry; report a missing entry only for a word the artifacts use in a way a reader could misread, and never require an entry for every noun.
- The team's `AGENTS.md` is its own and is different from the course repository's `AGENTS.md`; it links the course requirements rather than copying them.
- The `SKILL.md` link is judged by its URL and its count; a relative path to a skill directory is the shortfall, because the skill's directory depends on the agent.
- Whether the layout, the checks, and the conventions are true is judged against the snapshot; an `AGENTS.md` that describes a repository that no longer exists is the shortfall.
- A file an agent must not edit is judged by its path and condition, not by whether someone edited it.

### S10 — Week 3 action points and open questions

**Check:**

- `reports/week-04/meeting-report.md`, its `## Previous action points` and `## Previous open questions`.
- `reports/week-03/meeting-report.md` at the snapshot, for its `## Action points` rows due in Week 4 and every row of its `## Open questions`.
- Every artifact and task issue an `Outcome` or `Answer` cell links, and every `DEC-nnn` entry a `Decision` cell names.

**met:**

- `reports/week-03/meeting-report.md` exists in the snapshot and its `## Action points` and `## Open questions` can be read, or the report says there are none.
- `## Previous action points` has the columns `Action`, `Outcome`, and `Decision`, with one row per Week 3 action point due in Week 4 or carried out early.
- Every `Action` cell cites `reports/week-03/meeting-report.md#action-points` with the action quoted.
- Every `Outcome` says whether the action point was carried out and what was found, or why it was not, and links each artifact and task issue it changed.
- Every artifact an `Outcome` says changed holds that change, and the change is dated no later than `ISSUE_CUTOFF`.
- An action point not carried out reappears in the Week 4 `## Action points` with a new due week, unless its `Outcome` says the team or the customer dropped it.
- Every `Decision` cell links the `DEC-nnn` the outcome produced, or says `None`, and every linked entry exists, and its `**Source:**` points at where the decision was made.
- `## Previous open questions` has the columns `Question`, `Answer`, and `Decision`, with one row per Week 3 open question not yet closed, and every Week 3 open question is either answered there or carried into the Week 4 `## Open questions`.
- Every `Question` cell cites `reports/week-03/meeting-report.md#open-questions` with the question quoted.
- Every `Answer` says what the work or the meeting found and links each artifact the answer changed.

**partial:**

- The Week 4 report has both `## Previous` sections, and at least one other `met` criterion fails.
- Typical shortfalls: an action point due in Week 4 with no row; an outcome that exists only in the table, with the artifact unchanged; an action point not carried out that does not reappear; a Week 3 open question with no row and no carry-forward; a citation without the quoted action; an `Outcome` naming a task issue that does not exist.

**missing:**

- `reports/week-04/meeting-report.md` is absent at the snapshot, or neither `## Previous action points` nor `## Previous open questions` is present when the Week 3 report has rows for it.

**Guardrails:**

- When the Week 3 report has no action point due in Week 4 or no open question, `None` in the matching section is correct.
- Do not re-grade the Week 3 report; judge only what Week 4 did with its rows.
- An outcome carried into an artifact is judged by whether the artifact changed, not by whether the change is large.
- An action point the customer dropped stays closed, and the customer's decision is cited.
- The report is a record of one meeting, so an action point closed in a later meeting of the same week still needs its row here only when the report covers that meeting.
- A Week 3 report edited in Week 4 is a quality note unless its content was rewritten; a formatting-only change is allowed.
- A Week 3 open question the work has not answered belongs in the Week 4 meeting's questions; when the report carries it forward without an answer and the script does not ask it, report it here as a shortfall.
- The Week 4 `## Action points` table's shape and due dates belong to S11; this segment judges the reappearance of an open action point, not the table.

### S11 — Customer validation of stories and architecture

**Check:**

- `reports/week-04/meeting-script.md`, `reports/week-04/meeting-report.md`, and `reports/week-04/meeting-transcript.md` when it exists, in the snapshot.
- The path history of the script, for whether it was committed before the meeting.
- Every `DEC-nnn` in `## Decisions`, in `docs/decisions.md`, and every story issue the meeting showed or changed, with its comments, timeline, and edit history.
- The meeting artifacts for a recording link or timecode, and the Moodle PDF's recording line and any transcript appendix, with one access check on the recording link.
- The quality requirements index and the architecture document, for what the meeting reviewed.

**met:**

- The script has exactly the sections `## Context`, `## Agenda`, `## Questions`, `## Roles`, and `## Key improvements`, in that order, with `## Roles` left out only for a meeting held in writing, and every empty section says `None`.
- `## Context` gives the problem-space sentence, what the team believes, and a one-sentence target that covers whether the quality requirements and the architecture answer the drivers, and what comes next.
- `## Agenda` is a numbered list whose first part asks the three permission questions, whose last part reads back the decisions and action points, and whose parts each have a timebox that adds up to the planned length, or, for a meeting held in writing, the order of the exchange and what is sent with each part instead of timeboxes.
- The agenda shows the working software, then the quality requirements and the architecture against the drivers, and asks for the customer's verdict on each story.
- Every agenda part names what is shown, with a link or a statement that nothing is shown, and every question appears in exactly one part.
- `## Questions` is numbered, every question is tagged open or closed, and every question serves the target.
- `## Roles` names a moderator, a note taker, and an observer by GitHub username, and a written meeting omits the section.
- `## Key improvements` records at least one rewritten question with the before, the after, and the principle.
- The script was written before the meeting it prepares: its first commit is on or before the meeting date in `## Metadata`, and a same-day commit is accepted when the history shows it came before the meeting; its later commits are formatting-only changes.
- The report has exactly the sections `## Metadata`, `## Previous action points`, `## Previous open questions`, `## Summary`, `## Decisions`, `## Action points`, `## Open questions`, and `## Disagreements`, in that order, and every empty section says `None`.
- `## Metadata` is a bulleted list of `- **Label:** value` bullets giving the date, the duration, the attendees by GitHub username with the customer as `Customer`, what was presented, the answer to each of the three permission questions, the transcript link or `None` with the reason, and the script link.
- `## Summary` has 3 to 5 bullets on what the meeting settled or changed.
- `## Decisions` lists at least one `DEC-nnn` entry of the form `[DEC-nnn: <the entry's first line>](../../docs/decisions.md#dec-nnn)`, and every story shown against its acceptance criteria has a verdict `DEC-nnn` in `docs/decisions.md` naming its `US-nn`, made by `Customer` or `Team, not contested`, with a `**Source:**` linking this report.
- Each rejected story's verdict names each `AC-nn` it failed, and a rejected story stays open with an open rework task whose `Story` field names the story and the failed `AC-nn`.
- An accepted story closes with a comment that cites its verdict's `DEC-nnn`.
- Every `DEC-nnn` in `## Decisions` exists in `docs/decisions.md` with a `**Source:**` that links `reports/week-04/meeting-report.md`, and every linked entry's first line matches the report's link text. A `DEC-nnn` in a `Decision` cell of `## Previous action points` or `## Previous open questions` is judged in S10.
- The report is written in the team's own words: it does not restate the transcript line by line and is not a tool's output pasted in unchecked.
- `## Action points` has the columns `Action`, `Owner`, and `Due`, at least two rows, an owner given by GitHub username, and every due date inside Week 5, such as `End of Week 5` or a date from 23 to 29 October 2026.
- `## Open questions` has the columns `Question`, `What it would change`, and `Follow-up`; `## Disagreements` has the columns `Your position`, `Customer's position`, and `What you changed`, and every row that changed nothing says why the team kept its position.
- Every story issue the meeting showed, accepted, rejected, or changed has a comment dated on or after the meeting that names the verdict or the change, names each `AC-nn` affected, and links the `DEC-nnn` on `main`.
- The meeting was held in the Week 4 window, between Friday 16 October 2026 and `ISSUE_CUTOFF`, and a meeting held in writing says so and carries no `## Roles` section.
- Every meeting artifact names the customer `Customer` and identifies people only by GitHub username.
- When the meeting was recorded or held in writing, and publication was permitted, `reports/week-04/meeting-transcript.md` exists, opens with the date and the participants as `- **Label:** value` bullets above the first timestamped line, with a `#` title allowed above them, and then has one sentence per line in the form `[hh:mm:ss] <label>: <sentence>`, labels speakers by GitHub username and `Customer`, marks gaps with `[inaudible]` or `[redacted]`, and carries no personal data.
- When publication was refused, no transcript is committed and the Moodle PDF carries it in an appendix.
- No meeting artifact carries a recording link or a recording timecode: the recording link and the timecodes are Moodle-only, per the visibility rule.
- The Moodle PDF links a recording that instructors can open, or gives one line saying why there is none, and it agrees with the permission answers in `## Metadata`.

**partial:**

- `reports/week-04/meeting-report.md` exists, and at least one other `met` criterion fails.
- Typical shortfalls: a missing or extra section; no permission part in the agenda; a story shown with no `AC-nn` verdict; a verdict decision that does not name its `US-nn`; no review of the quality requirements and the architecture against the drivers; an action point due outside Week 5; a script committed after the meeting; a published transcript without permission; a recording link or timecode in a meeting artifact; personal data in a meeting artifact; a report that restates the transcript line by line.

**missing:**

- `reports/week-04/meeting-report.md` is absent at the snapshot, or no Week 4 meeting with the customer took place.

**Guardrails:**

- When the Week 3 report has no previous action points or open questions, `None` in the matching section is correct.
- Do not re-grade the Week 3 script, report, or transcript.
- The weekly meeting is the Sprint Review, so no second review meeting is expected; a second meeting in the same week is a quality note, and its artifacts may be read when they exist.
- A meeting held on or after Friday 16 October 2026 and by `ISSUE_CUTOFF` was held in Week 4; the extension allows a meeting on Saturday 24, Sunday 25, or Monday 26 October 2026 when it is by that team's cutoff.
- An inaccessible recording, or a recording gated to a sign-in, is an evidence gap for that check only, after the single access check `docs/grader-policy.md` allows.
- A transcript the customer refused to publish is Moodle-only, per `docs/grader-policy.md`; a recording link outside the meeting artifacts belongs to S15, and a recording link or timecode inside a meeting artifact is a visibility shortfall here.
- The outcome of the action points the Week 3 report closes belongs to S10; this segment judges only the report's own sections and the verdicts.
- The report's `## Action points` shape is judged here; whether an open action point reappears from S10 is judged there.
- The report is not rewritten after the meeting apart from a formatting-only change; a later rewrite is reported in `**Evidence:**` as a quality note.
- A story the customer accepted in a shared verdict is still judged by its own `AC-nn` comments, and a shared verdict is one decision.
- The script's plan for the quality requirements and the architecture is judged, not whether the customer liked them; the verdict's content is the customer's.

### S12 — REL-04 release

**Check:**

- `CHANGELOG.md` and `docs/project-plan.md` in the snapshot.
- The repository's tags and releases, from `tags.json`, `releases.json`, and `gh api "repos/$REPO/git/refs/tags"`.
- The tag protections, from `gh api "repos/$REPO/rulesets"` and `gh api "repos/$REPO/rulesets/<id>"`, by hand.
- The path histories of `CHANGELOG.md`, `docs/project-plan.md`, and `reports/week-04/README.md`, and the merge times they sit at.
- `SPRINT-04`'s GitHub milestone state, from the raw `gh api "repos/$REPO/milestones?state=all&per_page=100"` call, because `milestones.json` omits the state.
- The rendered release page and the rendered tag permalink.

**met:**

- `CHANGELOG.md` sits in the repository root and follows Keep a Changelog, with an `[Unreleased]` section during development.
- Every user-visible change merged before `ISSUE_CUTOFF` has an entry in `[Unreleased]` or in a released section, unless its pull request says it made no user-visible change.
- At least one tag exists whose version follows Semantic Versioning with the `v` prefix, such as `v0.4.0`, and it is the tag this week's release used: the tag the plan's `#### REL-04` line names and the changelog's latest dated section links. When those disagree, both fail.
- The release tag points at a commit that is on `main`, and the tag's commit is not after `ISSUE_CUTOFF`.
- A GitHub release exists for that tag, titled with the tag so the title and the tag match.
- The changelog has a dated section headed `[x.y.z](https://github.com/<org>/<repo>/releases/tag/vX.Y.Z) - YYYY-MM-DD` that links the release, its entries are the entries released, and a new empty `[Unreleased]` sits above it.
- A `#### REL-04` section in `docs/project-plan.md`, nested under `### SPRINT-04`, carries the line `Released as [vx.y.z](https://github.com/<org>/<repo>/releases/tag/vx.y.z) on YYYY-MM-DD`, with the tag the release used.
- The tag's commit merges the state after the Week 4 customer meeting and its rework: every pull request the changelog's released entries describe is merged at or before the tag's commit, and the meeting is at or before it.
- The release tag is protected against being moved or deleted, by a repository ruleset that covers tag pushes or by an equivalent tag-protection rule that blocks moving and deleting the tag.
- The tag predates the commit that added the changelog's released section, the commit that added the plan's `REL-04` line, and the commit that added `reports/week-04/README.md`, so every link to the release resolves against a tag that already existed.
- `SPRINT-04`'s GitHub milestone is closed once the release is cut; a still-open milestone is accepted only when the Week 4 report's `## Deviations` declares it and gives the reason.

**partial:**

- `CHANGELOG.md` exists, or a release was cut, and at least one other `met` criterion fails.
- Typical shortfalls: no `[Unreleased]` section; a tag without the `v` prefix or not SemVer; a tag on a branch commit or cut after `ISSUE_CUTOFF`; a release titled differently from its tag; a dated section that does not link the release; no `REL-04` line; a document that links the release in a commit that predates the tag; an unprotected tag; `SPRINT-04`'s milestone still open without a declared deviation.

**missing:**

- `CHANGELOG.md` is absent at the snapshot, and no tag or release exists at `ISSUE_CUTOFF`.

**Guardrails:**

- The version number is the team's choice under SemVer; a `REL-04` other than `v0.4.0` is never a shortfall.
- The Recommended shape, linking the changelog from the plan or `REL-04` from the changelog, is a quality note.
- The tag's date decides whether the release was cut in Week 4: a tag after `ISSUE_CUTOFF` is a shortfall under the cutoff criterion, and a tag after the sprint's end but by the cutoff is a caveat in `**Evidence:**`.
- When the tag rulesets cannot be read with the token, say which endpoint returned what, judge the rest, and set `Evidence gaps: yes` only when the answer could change the status.
- An empty `REL-05` to `REL-09` and a later release are not judged here.
- `REL-03` and Week 3's release are not re-graded; this segment judges the release this week cut.
- The changelog's groups, `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security`, are judged by the entries' placement, not by whether every group is used.

### S13 — Sprint close and retrospective

**Check:**

- `### SPRINT-04` in `docs/project-plan.md` at the snapshot, its `**Actual Velocity:**`, and the path history of the plan.
- The story issues in `SPRINT-04`'s milestone, their closed state and reason from `issues.json`, and their `Story Points` from `issue-fields.json`.
- `reports/week-04/sprint-retrospective.md` in the snapshot.

**met:**

- `### SPRINT-04` carries `**Actual Velocity:**` after `**Planned Velocity:**`, as the next field in the bulleted list.
- `**Actual Velocity:**` is a whole number equal to the sum of the `Story Points` of the stories in `SPRINT-04`'s milestone that are closed as completed at `ISSUE_CUTOFF`.
- The `**Actual Velocity:**` line continues with one sentence saying what moved out of the sprint and to which sprint, or saying that nothing moved out.
- `reports/week-04/sprint-retrospective.md` exists and carries the sections `## What Went Well`, `## What Did Not`, `## Actions`, and `## Carried Actions`, in that order.
- `## What Went Well` has the column `What went well` and 3 or more rows, each one sentence naming what happened.
- `## What Did Not` has the columns `Problem` and `Root cause` and 2 or 3 rows, each with the problem and its root cause.
- `## Actions` has the columns `Action`, `Owner`, `Impact`, `Reason`, and `Carried`, in that order, and 3 or 4 rows; every `Owner` is a GitHub username, every `Impact` is `High`, `Medium`, or `Low`, and every `Carried` is `Yes` or `No`.
- `## Carried Actions` is, because this is the first retrospective, one sentence saying there is no previous retrospective rather than an empty table; from the second retrospective on it has the columns `Action` and `Outcome`.

**partial:**

- `### SPRINT-04` carries `**Actual Velocity:**`, or the retrospective exists, and at least one other `met` criterion fails.
- Typical shortfalls: `**Actual Velocity:**` absent, out of order, or not the completed stories' sum; no sentence on what moved out; a retrospective section missing, renamed, or out of order; fewer than 3 things that went well; a `## What Did Not` without a root cause; 2 or 5 actions; an owner who is not a GitHub username; an `Impact` or `Carried` value outside its options; an empty `## Carried Actions` table instead of the first-retrospective sentence.

**missing:**

- `reports/week-04/sprint-retrospective.md` is absent at the snapshot, and `### SPRINT-04` carries no `**Actual Velocity:**`.

**Guardrails:**

- The retrospective is the first one with a file, so `## Carried Actions` is a sentence, and a team that writes a sentence rather than a table is correct.
- The actions' content and the "what went well" facts are the team's judgement; do not judge whether the sprint was good, only whether the record has the sections, the counts, and the columns.
- `**Actual Velocity:**` counts stories, not tasks; a task's `Priority` never enters the sum.
- A story closed as not planned is not a completed story and does not enter the sum; say in `**Evidence:**` which stories were counted.
- When the plan's history cannot show whether `**Actual Velocity:**` was set after the retrospective, note it in `**Evidence:**` and never change a status for it.
- A story that moved out and was rescheduled into a later sprint's milestone is the sentence's subject, and its later milestone is the sprint it names.
- `SPRINT-05`'s retrospective and any later one are not judged here.
- Whether the file's first commit followed `**Actual Velocity:**` is a caveat in `**Evidence:**`, never a status change.
- A later formatting-only change to the file is allowed; a rewrite of its content after the week is reported in `**Evidence:**` as a quality note.

### S14 — Documentation site and navigation

**Check:**

- The site URL in `reports/week-04/README.md` and the root `README.md`.
- The Pages workflow under `.github/workflows/` and its Pages settings, in the snapshot.
- The Pages runs, from `runs_main.json` and `runs_sha.json`.
- The site's default page and its navigation, with the single access check `docs/grader-policy.md#consumer-hosted-media` allows.

**met:**

- The root `README.md` links the site's URL, and the site serves the repository's documentation.
- The site's default page responds and is a landing page: it says what the product is and navigates to the other pages, rather than listing files.
- The site's navigation, or its generated documentation index, links the Week 4 pages: `docs/quality-requirements/README.md`, `docs/functional-requirements/README.md`, `docs/architecture/README.md`, and `docs/glossary.md`.
- Each of those four links resolves on the site and opens the page it names.
- The site's navigation or generated documentation index does not list the weekly reports. A page may link a week report by its GitHub URL, and a page that links a file outside `docs/` uses that file's GitHub URL.

**partial:**

- The site is published, and at least one other `met` criterion fails.
- Typical shortfalls: a Week 4 page absent from the navigation or leaking a 404; a default page that is a file listing; a site's navigation that lists a weekly report; a page that links a file outside `docs/` by a site-relative path.

**missing:**

- No site URL resolves, or the repository publishes no site from `docs/` at all.

**Guardrails:**

- The generator is the team's choice, and a site built with any of mdBook, Zensical, MkDocs, Jekyll, or a plain HTML page is judged the same.
- The site is a Week 3 artifact, so its generator, workflow pinning, design, navigation depth, and quantity of pages are not re-graded; this segment judges its current reachability and the Week 4 navigation update.
- A generated navigation that lists the new pages counts, and the four pages need not each have a hand-written menu entry.
- When the site's URL cannot be opened because Pages is gated, or the deployment run cannot be read, use the snapshot's workflow and the README as far as they settle it, and set `Evidence gaps: yes` only for the criterion the access leaves open.
- A site that lags the snapshot by a deployment is a caveat in `**Evidence:**` and never a status change; the four Week 4 pages must still be reachable.
- The coverage row's link to the site is judged in S15; this segment judges the site itself.

### S15 — Week report and submission

**Check:**

- `reports/week-04/README.md` at the snapshot, and every repository file it links.
- `## Minimum Usable Product Candidate` in `reports/week-02/README.md` and `MLS-03`'s description in `docs/project-plan.md`, for a candidate story that moved out.
- The Moodle PDF, its page count, and its contents.
- The snapshot SHA's position on `main`, and the snapshot commit time, per procedure step 4.
- The link and Markdown check runs on `main`, from `runs_main.json` and `runs_sha.json`.
- A privacy scan of the snapshot, per procedure step 15.

**met:**

- `reports/week-04/README.md` is in the snapshot, and every repository file it links resolves.
- The report identifies the week, the project, the team, and the covered scope.
- The summary names `REL-04` and its tag, and says what moved out of the sprint.
- The report links `REL-04` to its plan section, `docs/project-plan.md#rel-04`, per the traceability rule.
- The summary says what the team found, built, or decided, and what it left open.
- The report states the customer-meeting outcome: each story shown with whether the customer accepted or rejected it, and each candidate story that moved out, each citing its `DEC-nnn`.
- The report says whether the meeting's transcript was published, shared privately, or not made, and why.
- The coverage table has the 19 rows of `assignment-4.md`, in its order: Sprint plan and estimates, Product backlog refinement, Issue catch-up, Quality requirements, Functional requirements, Container view, Architecture and drivers, Architectural decisions, Glossary, Team `AGENTS.md`, Issue fields in the project view, Documentation site, Week 3 action points, Week 3 open questions, Meeting script, Customer validation, `REL-04`, Sprint retrospective, and AI usage.
- Every coverage cell links its artifact: a repository file with its path from the repository root as the link text and the heading anchor when the row names a section, and anything else with descriptive link text; a row whose artifact is not public says so instead of linking it.
- When the customer refused publication of the transcript, the Customer validation row says so and points at the Moodle submission.
- No second list of the same links follows the coverage table.
- The report carries no sprint planning, refinement, or retrospective section, because the plan, the issues, and the retrospective file own them.
- A contribution table maps each member's GitHub username to the work done, with links to commits, pull requests, or reviews.
- The report does not assess an individual: no section rates or explains a member's contribution.
- The repository evidence links one merged pull request that closed its task issue, the latest green link-check run on `main`, and the latest green Markdown check run on `main`, and each link resolves.
- Every link in the report resolves, and every link the link check excludes is justified in prose.
- `## Deviations` declares every deviation observed in the other segments, or says `None` when there is none.
- One line states that no private-only material was committed to the repository.
- The privacy scan finds no email address, phone number, member-name token, or `.env`/key file outside the meeting artifacts, and no recording link outside the meeting artifacts. A personal-data hit or a recording link inside a meeting artifact is reported in S11, not here.
- The snapshot SHA is on `main`, and the PDF permalink points at `reports/week-04/README.md` at that full 40-character SHA.
- The PDF is at most two pages, not counting a transcript appendix, and holds only the six items of `assignment-4.md`: the project name and team number, the member table, the permalink, the recording line, the transcript when publication was refused, and the privacy confirmation line.

**partial:**

- `reports/week-04/README.md` exists at the snapshot, and at least one other `met` criterion fails.
- Typical shortfalls: a coverage row missing, out of order, or not linked; no release line or no moved-out note in the summary; no meeting outcome; a sprint-planning, refinement, or retrospective section in the report; no contribution table; an individual assessment; repository evidence missing a run or the pull request, or linking a red run; no `## Deviations`; an undeclared deviation; a privacy finding outside the meeting artifacts; a seven-character permalink; a snapshot that is not on `main`; a PDF over two pages or with extra content.

**missing:**

- `reports/week-04/README.md` is absent at the snapshot.

**Guardrails:**

- A coverage row whose artifact is absent is a shortfall in the segment that owns the artifact; here the shortfall is only a missing row or a row that does not link.
- The release's content, the verdicts, the retrospective, and the AI usage are judged in S12, S11, S13, and S16; here only the week report's summary lines, the coverage rows, and their links are judged.
- The minimum usable product candidate's record was Week 2's, and the plan's `MLS-03` owns its core task after Week 3; the report repeats neither, and this segment judges only a candidate story that moved out this week.
- The Documentation site row links the site's URL; the site's own state is S14's.
- The Submission Procedure's snapshot upload to Moodle is not judged: the autochecker receives only the PDF and rebuilds the snapshot from the permalink SHA, per `docs/grader-policy.md`.
- Record the snapshot commit date against the team's deadline in `**Evidence:**`, and never change a status for lateness.
- Report a privacy finding by path and kind, such as "a personal email address in `docs/glossary.md`", never by value.
- A report that links a file at a commit other than the snapshot is accepted when the target exists; record the hash in `**Evidence:**`.
- The report's length, its prose, and the contribution table's wording are quality notes.
- The `## Deviations` section declares what the other segments observed; an undeclared deviation is a shortfall here, while the deviation itself is judged in its own segment.
- The root `README.md` linking the current week's report is a Week 1 rule: a current-week or previous-week link is recorded in `**Evidence:**` as a quality note and never changes an S15 status.

### S16 — AI usage and honesty

**Check:**

- `reports/week-04/ai-usage.md` in the snapshot.
- Traces of AI tools: the team's `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.agents/`, `.opencode/`, `opencode.json`, `.github/copilot-instructions.md`, `.cursor/`, a `Co-Authored-By:` trailer that names an AI tool, a `Harness:` or `Model:` trailer, and a "Generated with" line in Week 4 commit messages and pull request bodies.
- The Week 4 prose: the quality requirements, the functional requirements, the architecture document, the ADRs, the glossary, the team's `AGENTS.md`, the sprint retrospective, the meeting artifacts, and the week report.

**met:**

- `reports/week-04/ai-usage.md` names each tool and what it was used for, and says what the team did with the output: what it accepted, changed, and rejected, and why.
- Alternatively, the file states in one line that no AI tools were used, and nothing in the repository or its history contradicts it.
- The disclosure agrees with the traces of AI tools in the repository, the commit messages, and the pull request bodies, including the course-materials skill when other traces show agent output.
- The Week 4 prose has no filler, meaning no template sentence with no product name, no identifier, and no date, and no unchecked generated text, such as leftover `<org>` or `<repo>` placeholders, identifiers that point nowhere, or claims that contradict the team's own artifacts.
- Every identifier a Week 4 artifact states resolves to an artifact that carries it, and every count it states matches the artifact it counts.
- Where the statement of a requirement, an ADR's decision, or a sprint's velocity separates what was observed from what was inferred, it says which; a claim with no evidence behind it is a shortfall here only when it contradicts the team's artifacts.

**partial:**

- `reports/week-04/ai-usage.md` exists, and at least one other `met` criterion fails.
- Typical shortfalls: tools named without saying what happened to their output; agent traces or an AI-tool `Co-Authored-By:` trailer with no disclosure; a placeholder or a template sentence left in a Week 4 artifact; a `QR-nn`, `FR-nnn`, or `ADR-nnn` cited that does not exist; a statement of how many requirements or records that the artifact contradicts.

**missing:**

- `reports/week-04/ai-usage.md` is absent at the snapshot.

**Guardrails:**

- Using AI tools is allowed and is never a shortfall by itself.
- The course-materials submodule alone does not prove agent use; count it as undisclosed use only when other traces show agent output.
- The meeting report's own-words rule belongs to S11.
- Week 1 to Week 3 text left unchanged is not re-judged.
- The filler test is anchored to the artifact's own evidence: quote a short fragment, and name the artifact and the heading.
- A generated diagram or table is not a shortfall when the team checked it and the disclosure says so; the artifact's correctness is judged in its own segment.
- The AI usage report's file is the disclosure; a one-line "no AI" answer is valid when the traces agree.

## Assignment-specific procedure deltas

1. Take the team set from the directory names under `itpd-assignments-feedback/A4/submissions/`.
2. Read the Moodle PDF with the submission fetcher, which prefers the PDF that carries the full-SHA permalink to `reports/week-04/README.md` when there are several:

   ```console
   uv run python scripts/fetch_team_snapshot.py A4 "<team_dir>"
   ```

   It records the extracted metadata in `itpd-assignments-feedback/A4/work/<team_dir>/pdf-info.json`: the team number, repository, permalink, full SHA, recording link, page count, GitHub usernames, and the member name/email tokens for the step 15 privacy scan.
   The fallback is to read the PDF directly and extract:

   - the project name and the team number;
   - the GitHub usernames of the member table, keeping real names and emails only in working memory for the privacy match;
   - the permalink to `reports/week-04/README.md`, with its organization, repository, and full SHA;
   - the recording link or the line saying why there is none;
   - whether a transcript appendix is present;
   - the privacy confirmation line;
   - the page count, for example from `pdfinfo`, and anything outside the six allowed items.

   When the submission directory holds no PDF and one Markdown file instead, run `uv run python scripts/fetch_markdown_snapshot.py A4 "<team_dir>"`: it reads the Markdown, writes `pdf-info.json` with `permalink_source=operator` and the member name/email tokens, and fetches the snapshot. Treat the missing PDF as an S15 shortfall, and say in `**Evidence:**` that the wrapper was Markdown rather than a PDF. Fall back to reading the Markdown by hand and writing `pdf-info.json` only when the helper cannot parse it.

3. The fetcher in step 2 resolves the snapshot per `docs/grader-policy.md` and refetches it into a freshly emptied `itpd-assignments-feedback/A4/work/<team_dir>/snapshot/`.
   When it cannot, resolve and fetch by hand as in `agents/grader.md`.
4. Read the snapshot commit time and the on-`main` result from `pdf-info.json` (`snapshot_time`, `on_main`, `on_main_status`), or re-check them with `REPO=<org>/<repo>` and `SHA=<full SHA>`:

   ```sh
   gh api "repos/$REPO/commits/$SHA" --jq '.commit.committer.date'
   gh api "repos/$REPO/compare/$SHA...main" --jq '.status'
   ```

   A status of `identical` or `ahead` puts the commit on `main`; `behind` or `diverged` does not, which is an S15 shortfall.
   Call the first value `SNAPSHOT_TIME`.

5. Collect the live evidence once and keep it beside, not inside, the fetched snapshot.
   Preferred: `uv run python scripts/collect_github_evidence.py A4 "<team_dir>" [--issues <n> ...] [--paths <path> ...]`, which reads `itpd-assignments-feedback/A4/work/<team_dir>/pdf-info.json` and writes `labels.json`, `issues.json`, `prs.json`, `runs_main.json`, `runs_sha.json`, `commits.json`, `milestones.json`, `releases.json`, `tags.json`, plus `issues/<n>.comments.json`, `issues/<n>.timeline.json`, `issues/<n>.edits.json`, `paths/<path>.json`, and a bounded `summary.md` there, printing counts and paths only.
   Read `summary.md` first: it carries the issue counts, the pull-request numbers, the failing runs, the tags, and each milestone's due date with its open and closed issue counts, in at most 60 lines.
   Open a dump only through a bounded projection that prints at most about 40 lines (`head -n 40`, a `jq` projection, or an `rg` match); never `cat` a full dump, because `commits.json` reached 1.35 MB and `prs.json` 284 KB.
   `--summary` rebuilds the digest from the saved dumps without calling `gh`.
   The issue fields are their own mode: `uv run python scripts/collect_github_evidence.py A4 "<team_dir>" --issue-fields` writes `issue-fields.json` there with every issue's `type`, `milestone`, `assignees`, and `field_values`, from one paginated REST list call and without its pull requests.
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

6. Judge every issue as of `ISSUE_CUTOFF`, the team's effective deadline defined in [Assignment parameters](#assignment-parameters):

   Use `2026-10-25T23:59:59+03:00` for every team except `Team 2 - OK_10938_assignsubmission_file`, whose cutoff is `2026-10-26T23:59:59+03:00`; do not use the pinned course materials' original Saturday date.

   - Count only issues whose `createdAt` is at or before `ISSUE_CUTOFF`.
     An issue opened after `SNAPSHOT_TIME` but by `ISSUE_CUTOFF` counts like any other.
   - Take an issue's labels at `ISSUE_CUTOFF` from its timeline's `labeled` and `unlabeled` events, its title from `renamed` events, and its open or closed state and close reason from `closed` and `reopened` events.
   - Take its body from the last edit at or before `ISSUE_CUTOFF` when the edit history allows it; otherwise judge the current body and say so in `**Evidence:**`.
   - Take its milestone from the `milestoned` and `demilestoned` events when the issue has them, and its current milestone otherwise, noting in `**Evidence:**` which was read.
   - A comment or edit made after `ISSUE_CUTOFF` is a caveat, never a shortfall.
   - Post-cutoff file state is a caveat and never a status change, except in a segment that judges the snapshot, which reads the file at `SNAPSHOT_TIME`.
   - Set `Evidence gaps: yes` only when the state at `ISSUE_CUTOFF` cannot be read and the difference could change the status.
   - Pull requests, Actions runs, repository files, tags, and releases stay judged as of `ISSUE_CUTOFF`, and the snapshot stays the evidence for files.

7. Identify the Week 4 pull requests: every pull request created on or after Friday 16 October 2026, 00:00 Innopolis time, the start of Week 4 in `course/syllabus.md`.
   A pull request merged at or before the team's Assignment 3 snapshot commit is part of the Week 3 submission, not a Week 4 pull request. Read that SHA from the saved A3 feedback report's `Primary index reviewed` link at `itpd-assignments-feedback/A3/feedback/<team_dir>/agent-feedback.md`, or from the A3 submission PDF. When neither is available, use the A3 cutoff `2026-10-17T23:59:59+03:00` as the boundary and say so in `**Evidence:**`.
   The in-scope pull requests for the release and the report's evidence run from the start of Week 4 to `ISSUE_CUTOFF`, without Dependabot pull requests and pull requests a workflow opened.

8. Gather the pull-request facts below as evidence. These are Week 1 and Week 2 mechanics and are not re-graded in Assignment 4, except where a criterion names them: S8's catch-up comment and S12's release merge. Record an anomaly in `**Evidence:**` only; never make it a shortfall in S15 or S8.

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

9. Read the one-time catch-up from the issue dumps at `ISSUE_CUTOFF`:

   ```sh
   jq -r '.[] | [.number, (.type // "-"), (.milestone // "-"),
                   ((.field_values // []) | map(select(.name == "MoSCoW") | .value) | join(",")),
                   ((.field_values // []) | map(select(.name == "Story Points") | .value) | join(",")),
                   ((.field_values // []) | map(select(.name == "Priority") | .value) | join(","))]
                  | @tsv' "{TEAM_WORK}/issue-fields.json" | head -n 60
   jq -r '.[].name' "{TEAM_WORK}/labels.json" | sort | head -n 40
   jq -r '.[] | select(.number == <n>) | .body' "{TEAM_WORK}/issues.json" | head -n 40
   ```

   - The first projection answers the type, the milestone, and the three field values for the issues in the page it prints; narrow it with `select(...)` when the list is long.
   - The labels projection answers whether the six retired labels still exist in the repository; the issue's own `labels` from `issues.json` answer whether an open issue still carries one.
   - The body projection answers `### Specified by` and `### Requirements`; read it for each story and each open task, and use `issues/<n>.edits.json` when the body changed at the cutoff.
   - Every `FR-nnn` and `ADR-nnn` a list names must resolve in the snapshot, and every story other than a `Won't Have` must carry `### Specified by`.

10. Check the requirement chain across the snapshot, by file and by link:

    - Every `FR-nnn` `**Containers:**` name is a container in `docs/architecture/README.md`'s `### Container Responsibilities`, spelled the same.
    - Every `ADR-nnn` `**Addresses:**` entry resolves to an `FR-nnn` or `QR-nn` file that exists.
    - Every `QR-nn` the ADR index names resolves to a file, and every ADR the view's opening sentence links exists.
    - Every `US-nn` and `DEC-nnn` a `**Traces to:**` links resolves, and every story's `### Specified by` names an existing requirement or record.
    - The stack record names every container the view lists.

11. Check the release against the tag:

    - Read `releases.json` for the tag names and dates; read the release title from the rendered release page or the raw `gh api "repos/$REPO/releases?per_page=100"` response, because the collector's dump omits `name`; read `gh api "repos/$REPO/git/refs/tags/<tag>"` for the commit the tag names.
    - Confirm that the tag's commit is an ancestor of `main`, with `gh api "repos/$REPO/compare/<tag>...main" --jq '.status'`, which is `ahead` or `identical` when it is.
    - Read the changelog's dated section, the plan's `REL-04` line, and `reports/week-04/README.md` at the snapshot, and find, for each, the pull request that first added it, with the commits API over the file's path. To map a released entry to its pull request, use the pull request template's changelog line or search the pull request bodies for the entry's text.
    - Compare the merge time of those three pull requests with the release's `published_at` and the tag's commit date; each must be later than, or at, the tag.
    - Read `gh api "repos/$REPO/rulesets"` and each tag ruleset for the protection that covers tag pushes.

12. Check the milestones, the issue fields, and the project from the issue dumps and the organization's endpoints:

    ```sh
    gh api "repos/$REPO/milestones?state=all&per_page=100" \
      --jq '.[] | [.title, .due_on, .state, .open_issues, .closed_issues] | @tsv'
    gh api "repos/$REPO/issues/<n>" \
      --jq '{number, type: (.type.name // null), milestone: (.milestone.title // null),
             assignees: [(.assignees // [])[].login],
             field_values: [(.issue_field_values // [])[] | {name: .issue_field_name, data_type, value: (.single_select_option.name // .value)}]}'
    gh project list --owner <org> --format json
    gh project field-list <number> --owner <org> --format json
    gh project view <number> --owner <org> --format json
    ```

    Read the per-issue values first, from `issue-fields.json` or the REST projection above, and the field names, options, issue-type pinning, and visibility from the issue sidebar and the project's fields.
    The raw REST projection keys the name as `issue_field_name`; the collector's `issue-fields.json` keys it as `name`.
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

    The organization `issueFields` list is evidence only when the token can read it: it needs organization membership the token may not have, and an empty list or `totalCount: 0` never means a field is absent. When it cannot be read, the issue sidebar answers the definitions, and a definition neither route can settle is an evidence gap.
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
              nodes {
                name
                layout
                fields(first: 50) {
                  nodes {
                    ... on ProjectV2FieldCommon { name dataType }
                  }
                }
                groupByFields(first: 20) {
                  nodes { ... on ProjectV2FieldCommon { name } }
                }
                sortByFields(first: 20) {
                  nodes {
                    direction
                    field { ... on ProjectV2FieldCommon { name } }
                  }
                }
              }
            }
          }
        }
      }'
    ```

    The project type has no plain description field: read the description from `shortDescription` in the query or `gh project view`, or from the project page and README, and say in `**Evidence:**` which route answered.
    A direct `fields` selection on the project type is a union and raises `selectionMismatch`, so read the field names, options, and data types from `gh project field-list` instead.
    The `fieldValues` connection returns one node per value type, so filter the nodes that carry a field name.
    Read each project's visibility from `gh project view` or the query above, and the table views and their columns from the `views` connection, the project's page, or `gh project field-list`; `gh project field-list` lists the project's fields, not a specific view's columns, so the `views` connection or the project page answers a view's columns.
    On a view, `fields`, `groupByFields`, and `sortByFields` name the columns, the grouping, and the sort; `fields` is a union, so select it with inline fragments, as the query does on `ProjectV2FieldCommon`.
    Say in `**Evidence:**` which route answered.

13. Check that every `**Sprint Backlog:**` link in `docs/project-plan.md` resolves, and that the milestone it names is the sprint's own milestone and lists the issues scheduled into that sprint:

    ```sh
    gh api "repos/$REPO/milestones/<number>" --jq '[.title, .due_on, .open_issues, .closed_issues] | @tsv'
    gh api "repos/$REPO/issues?milestone=<number>&state=all&per_page=100" \
      --jq '.[] | [.number, .title, .state] | @tsv'
    ```

14. Check the sprint close from the issue dumps and the plan:

    - Find `SPRINT-04`'s GitHub milestone in `milestones.json`, and the story issues whose `milestone` is that title in `issue-fields.json`.
    - From `issues.json`, take the stories closed as completed at `ISSUE_CUTOFF` and their `Story Points` from `issue-fields.json`; add them by hand and compare the total with `**Actual Velocity:**`.
    - Read `reports/week-04/sprint-retrospective.md`'s four sections, their columns, and their row counts, and check that `## Carried Actions` is the first-retrospective sentence rather than an empty table.

15. Scan the snapshot for private-only material:

    ```console
    uv run python scripts/scan_privacy.py A4 "<team_dir>"
    ```

    It reads `itpd-assignments-feedback/A4/work/<team_dir>/pdf-info.json`, strips inline `data:...;base64,` payloads, and checks email addresses, phone numbers, `.env` and key files, recording links outside meeting artifacts, and the real names from the PDF member table, including hits in meeting artifacts.
    It reports one line per file with a count, such as `docs/glossary.md: email address (x2)`, plus per-rule hit and file totals; the exit code is 1 when it finds any.
    The raw fallback is email addresses with `grep -rnE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'`, phone numbers, the real names from the PDF member table, recording links in the submission and outside the meeting artifacts, and `.env` files.
    Report each finding by path and kind only, with the number of hits per file.

16. Open the documentation site's default page once, follow its navigation to the four Week 4 pages, and open the recording link once, per `docs/grader-policy.md#consumer-hosted-media`.

17. Grade each of the 16 segments independently, and report each shortfall only in the segment that owns it in the [segment overview](#segment-overview).

## Assignment-specific constraints

- The `Primary index reviewed` metadata bullet points to `reports/week-04/README.md` at the snapshot whenever the snapshot is inspectable.
- Moodle-only items are judged from the PDF, and their absence from the repository is correct: the member table with real names and university emails, the recording link, and a transcript the customer refused to publish.
- Never copy a real name or an email from the PDF into feedback; refer to people by GitHub username.
- A recording or external view that fails its single access check is an evidence gap for that check only, and the surrounding evidence is still judged.
- A transcript appendix does not count toward the PDF's two pages.
- Week 1 to Week 3 artifacts are not re-graded on their own requirements: repository setup, branch protection, the link-check configuration, Dependabot, the research content, the vision's own content, the Week 1 to Week 3 reports, the kickoff artifacts, the minimum usable product candidate, the threshold of success, the plan's Week 3 parts, the risk register, the Definition of Done, `CONTRIBUTING.md`, the setup page, the documentation site's generator and workflow, `REL-03`, and the Week 2 and Week 3 meeting artifacts.
- Week 1 to Week 3 artifacts are checked only where Assignment 4 requires it: the vision's architecture link and its goal's threshold link (S6), the plan's `SPRINT-04` and later sections (S1), the existing issues' catch-up (S8), the project's table view (S2), the Week 3 action points and open questions (S10), the Week 2 report's candidate and `MLS-03` (S15), the link check and the Markdown check green on `main` (S15), the documentation site's navigation (S14), and the sprint milestone and the issues in it (S1, S2, S13).
- When a Week 3 artifact that Assignment 4 builds on is absent, such as a Week 3 report with no action points, judge the Assignment 4 item against what exists, report the absence in the segment that owns the artifact it should contain, and do not report the Week 3 absence again.
- The one-time catch-up in Part 7 is judged by its end state when a team already met the newer shape before Week 4.
- The product code, its tests, its deployment, its analytics, and its configuration management are not Week 4 deliverables, so their absence is never a shortfall.
- Week 4 has no product-code CI and no deployment, so neither is expected; the link check and the Markdown check are the checks that must be green.
- The course-materials submodule is Recommended; excluding its directory from both checks is allowed, and its absence is never a shortfall.
- The architecture document's Week 5 parts, the component and sequence views and the testing plan, are not judged.
- Use the course's terminology in feedback: `Customer` for the person the team answers to, story issue, task issue, meeting report, meeting script, sprint, sprint planning, product backlog, product backlog refinement, story points, velocity, retrospective, threshold of success, quality requirement, quality requirements index, functional requirement, functional requirements index, architectural decision record, ADR index, container view, container responsibilities, architectural driver, plan milestone, sprint milestone, release, weekly report, and deviation.
