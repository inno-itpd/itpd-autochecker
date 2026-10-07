# ITPD Autochecker — Agent Guide

## Repo structure

```text
/
├── flake.nix, flake.lock      # Nix dev shell (python, uv, gh, pdftotext, markdownlint-cli2, backlog)
├── pyproject.toml, uv.lock    # Python project, managed with uv
├── AGENTS.md, CLAUDE.md       # This file (CLAUDE.md imports it)
├── opencode.json              # opencode config (loads AGENTS.md)
├── grading.json               # {"team_batch_size": N} for parallel reviews
├── agents/grader.md           # Canonical one-team grader prompt
├── .opencode/agents/grader.md # opencode wrapper → agents/grader.md
├── .claude/agents/grader.md   # Claude Code wrapper → agents/grader.md
├── docs/
│   ├── grader-policy.md            # General grading policy
│   └── grading-feedback-format.md  # Canonical feedback report format
├── A<N>/
│   ├── grading_prompt.md      # Segments and status guide for the assignment
│   ├── extract_feedback.py    # Feedback → dev.md + feedback_release.csv
│   └── itpd/                  # Course repo submodule pinned to the reviewed commit
├── tools/grader_tools/        # Report parsing, rendering, validation, extraction
├── scripts/                   # validate / inspect / patch / regrade CLIs
├── tests/                     # pytest suite
├── backlog/                   # Backlog.md tasks for this repo
└── itpd-assignments-feedback/ # Submodule: assignment data and feedback
    └── A<N>/
        ├── submissions/       # Moodle export, committed: <team_dir>/*.pdf
        ├── work/              # (gitignored, disposable) snapshots fetched from GitHub at the permalink SHA
        ├── feedback/markdown/<team_dir>/feedback.md
        ├── dev.md             # Instructor triage table
        └── feedback_release.csv
```

## Stack

- Nix flake dev shell: run `nix develop`, or `direnv allow` once and let `.envrc` load it.
  It provides Python 3.13, uv, gh, pdftotext, unzip, jq, ripgrep, markdownlint-cli2, lychee, and backlog.
- Python with no runtime dependencies; `pytest` as the dev dependency, managed with `uv`.
- `GITHUB_TOKEN` in `.env` (see `.env.example`), loaded by direnv.
  Agents never read `.env`.

## Course specifics

- ITPD assignments are not scored with points.
  Each segment gets a status: `met`, `partial`, `missing`, or `unverified`.
  The instructor decides the grade.
- The grader gets only the Moodle PDF; there is no ZIP.
  The PDF carries a permalink to `reports/week-NN/README.md` at the full SHA, and the grader fetches the snapshot from GitHub at that SHA.
- `A<N>/itpd` pins the course repository (`inno-itpd/itpd`) at the commit the assignment is reviewed against.
  A1 is pinned to `fe58ba7`, the version published at the Week 1 deadline.

## Workflow

1. Unpack the Moodle export into `itpd-assignments-feedback/A<N>/submissions/`, one directory per team.
2. Review teams with the grader agent (see below).
3. Run `markdownlint-cli2 --fix "itpd-assignments-feedback/A<N>/feedback/markdown/**/*.md"`.
4. Run `uv run python A<N>/extract_feedback.py` to regenerate `dev.md` and `feedback_release.csv`.
5. Review the extractor warnings and fix malformed reports.

## Reviewing teams with the grader agent

`agents/grader.md` is the executable prompt for one team.
It uses `{ASSIGNMENT_DIR}` (for example `A1`) and `{TEAM_DIR}` (the submission directory name) as placeholders.

When the user asks to review or re-review teams:

1. Read `agents/grader.md`.
2. Read `grading.json` and use `team_batch_size` as the batch size.
   Default to `8` if the file or value is missing or invalid.
3. Pick the teams: the ones the user names, or every directory in `itpd-assignments-feedback/A<N>/submissions/` that has no `feedback/markdown/<team_dir>/feedback.md` yet.
4. For each batch, launch one subagent per team in parallel:
   - Claude Code: the `grader` agent (`.claude/agents/grader.md`).
   - opencode: the `grader` subagent (`.opencode/agents/grader.md`) via the `task` tool.
   - Pass the assignment directory, the team directory, and the mode in the prompt.
   - Workers write disjoint paths, so they need no coordination.
5. If subagents are unavailable, review sequentially without asking.
6. After all batches, run the lint and extraction steps from the workflow above.

## Segment inspection and targeted regrades

- Inspect the saved state: `uv run python scripts/inspect_feedback_segments.py A<N> <feedback.md> S<n> ... [--fresh-payload <payload.json>] [--format text|json]`
- Preview a regrade: `uv run python scripts/regrade_feedback_segments.py A<N> <feedback.md> <payload.json> S<n> ... --dry-run`
- Apply a regrade (patches, validates, lints, and re-extracts): the same command without `--dry-run`.
- Low-level patch: `uv run python scripts/patch_feedback_report.py A<N> <feedback.md> <payload.json>`
- Validate one report: `uv run python scripts/validate_feedback_report.py A<N> <feedback.md>`

Payload shape:

```json
{
  "segment_updates": {
    "S4": {
      "status": "met",
      "evidence_gaps": false,
      "evidence": ["Instructor-reviewed: the board is public and has two screenshots per ALT."],
      "verified_shortfalls": [],
      "unverified_checks": []
    }
  },
  "unresolved_evidence_gaps": {}
}
```

Decision rules:

- Newly available evidence satisfies the requirement: raise the status and clear the gap.
- Access is restored but the artifact is still weak: keep the status and clear the gap.
- New evidence confirms a failure: turn the blocker into a verified shortfall and clear the gap.
- Keep `Evidence gaps: yes` only while a later review could still change the status.

## Exports

- `dev.md` columns: `team | gaps | gaps section | statuses | feedback`.
- `feedback_release.csv` uses `|` as the delimiter: `group|s1..sN|manual_review|feedback`.
- Only the `## Summary` section goes into the release feedback column.

## Adding a new assignment

1. `git submodule add https://github.com/inno-itpd/itpd A<N>/itpd`, then check out the commit the assignment is reviewed against.
2. Write `A<N>/grading_prompt.md` with `## Authoritative sources`, `## Assignment parameters` (with the `- S<n>: <name>` lines), and `## Status guide`.
3. Add `A<N>` to `tools/grader_tools/assignment_config.py`, with segment names identical to the prompt.
4. Copy `A1/extract_feedback.py` to `A<N>/` and change `ASSIGNMENT`.
5. Create `itpd-assignments-feedback/A<N>/feedback/markdown/` (with a `.gitkeep`).

## Task tracking

Tasks for this repo are tracked with Backlog.md in `backlog/`.

- `backlog task list --plain`
- `backlog task create "Title" -d "Description" --ac "Criterion"`
- `backlog task edit <id> -s "In Progress"`, then `-s Done` with `--notes` recording decisions and validation

Run `backlog` inside the dev shell so `BACKLOG_CWD` points at this repo.

## Checks

- `uv run pytest`
- `markdownlint-cli2 "**/*.md"`

## Git conventions

<!-- TODO use commit-itpd skill from the itpd repo -->

- Use Conventional Commits with a path scope, for example `feat(A1/prompt): ...`, `fix(tools): ...`, `docs(agents): ...`, `chore(deps): ...`.
- Every commit has a body of 2-4 short bullets explaining what changed and why.
- Commits made by an AI agent end with a `Co-Authored-By` trailer naming the model.
- Commit feedback in the `itpd-assignments-feedback` submodule first, then bump the submodule here.
