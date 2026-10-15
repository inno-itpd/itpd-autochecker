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
├── .agents/skills/commit-itpd/ # commit skill for this repo's Git conventions
├── .opencode/command/commit.md # /commit command → commit-itpd skill
├── docs/
│   ├── grader-policy.md            # General grading policy
│   └── grading-feedback-format.md  # Canonical feedback report format
├── A<N>/
│   ├── grading_prompt.md      # Segments and status guide for the assignment
│   ├── extract_feedback.py    # Feedback → dev.md + feedback_release.csv
│   └── itpd/                  # Course repo submodule pinned to the reviewed commit
├── tools/grader_tools/        # Report parsing, rendering, validation, extraction, PDF/evidence/privacy/link logic
├── scripts/                   # Per-team fetch, evidence, check, privacy, link, render, and regrade CLIs
├── tests/                     # pytest suite
├── backlog/                   # Backlog.md tasks for this repo
├── tmp/A<N>/<team_dir>/       # (gitignored) per-team grader scratch, so parallel workers never collide
└── itpd-assignments-feedback/ # Submodule: assignment data and feedback
    └── A<N>/
        ├── submissions/       # Moodle export, committed: <team_dir>/*.pdf
        ├── work/              # (gitignored, disposable) snapshots fetched from GitHub at the permalink SHA
        ├── feedback/<team_dir>/agent-feedback.md
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
2. Run `uv run python scripts/preflight.py` before a grader batch; it checks `gh` auth, `pdftotext`, and `markdownlint-cli2`.
3. Review teams with the grader agent (see below).
4. Validate changed reports with `uv run python scripts/check_feedback_report.py A<N> <agent-feedback.md>`, then run `markdownlint-cli2 --fix "itpd-assignments-feedback/A<N>/feedback/**/*.md"`.
5. Run `uv run python A<N>/extract_feedback.py` to regenerate `dev.md` and `feedback_release.csv`.
6. Review the extractor warnings and fix malformed reports.

## Reviewing teams with the grader agent

`agents/grader.md` is the executable prompt for one team.
It uses `{ASSIGNMENT_DIR}` (for example `A1`) and `{TEAM_DIR}` (the submission directory name) as placeholders.

When the user asks to review or re-review teams:

1. Read `agents/grader.md`.
2. Read `grading.json` and use `team_batch_size` as the batch size.
   Default to `8` if the file or value is missing or invalid.
3. Pick the teams: the ones the user names, or every directory in `itpd-assignments-feedback/A<N>/submissions/` that has no `feedback/<team_dir>/agent-feedback.md` yet.
4. For each batch, launch one subagent per team in parallel:
   - Claude Code: the `grader` agent (`.claude/agents/grader.md`).
   - opencode: the `grader` subagent (`.opencode/agents/grader.md`) via the `task` tool.
   - Pass the assignment directory, the team directory, and the mode in the prompt.
   - Workers write disjoint paths (feedback, `work/`, and `tmp/` per team), so they need no coordination.
5. If subagents are unavailable, review sequentially without asking.
6. After all batches, run the lint and extraction steps from the workflow above.

## Grader helper scripts

All run from the repository root and print counts and paths only.
`agents/grader.md` uses them in steps 7 to 13 and keeps the raw `gh` and `jq` commands as fallback.

- `uv run python scripts/preflight.py` — checks `gh` auth, `pdftotext`, and `markdownlint-cli2` before a batch.
- `uv run python scripts/fetch_team_snapshot.py A<N> <team_dir>` — PDF permalink, recording, page-count, and member-token extraction; commit and `main` check; snapshot refetch; writes `tmp/A<N>/<team_dir>/pdf-info.json`.
- `uv run python scripts/collect_github_evidence.py A<N> <team_dir> [--issues <n> ...] [--paths <path> ...]` — paginated dumps (`labels.json`, `issues.json`, `prs.json`, `runs_main.json`, `runs_sha.json`, `commits.json`, plus `issues/<n>.comments.json`, `issues/<n>.timeline.json`, `issues/<n>.edits.json`, and `paths/<path>.json`) in the same scratch directory.
- `uv run python scripts/check_snapshot_links.py <work_dir> [--issue-bodies <issues.json>]` — broken relative links, missing anchors, and pre-cut research anchors.
- `uv run python scripts/scan_privacy.py A<N> <team_dir> [--feedback <agent-feedback.md>]` — privacy findings by path and kind only.
- `uv run python scripts/check_feedback_report.py A<N> <agent-feedback.md>` — report validation plus `markdownlint-cli2` in one command.
- `uv run python scripts/render_feedback_report.py A<N> <payload.json>` — renders a complete report from one structured payload.
- `uv run python scripts/image_info.py <files>` — PNG and JPEG dimensions, byte size, and PNG transparency.

The `pdf-info.json` keys and the dump file names are documented under Paths in `agents/grader.md`.

## Segment inspection and targeted regrades

- Inspect the saved state: `uv run python scripts/inspect_feedback_segments.py A<N> <agent-feedback.md> S<n> ... [--fresh-payload <payload.json>] [--format text|json]`
- Preview a regrade: `uv run python scripts/regrade_feedback_segments.py A<N> <agent-feedback.md> <payload.json> S<n> ... --dry-run`
- Apply a regrade (patches, validates, lints, and re-extracts): the same command without `--dry-run`.
- Low-level patch: `uv run python scripts/patch_feedback_report.py A<N> <agent-feedback.md> <payload.json>`
- Validate one report: `uv run python scripts/validate_feedback_report.py A<N> <agent-feedback.md>`

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
3. Add `A<N>` to `tools/grader_tools/assignment_config.py`: segment names identical to the prompt, plus `primary_index`, `week_window_start`, and `issue_cutoff` as ISO 8601 Innopolis (UTC+3) strings.
   `scripts/fetch_team_snapshot.py`, `collect_github_evidence.py`, `scan_privacy.py`, `check_feedback_report.py`, and `render_feedback_report.py` all read this config.
4. Copy `A1/extract_feedback.py` to `A<N>/` and change `ASSIGNMENT`.
5. Create `itpd-assignments-feedback/A<N>/feedback/` (with a `.gitkeep`).
6. Smoke-check the helpers against one submission: `uv run python scripts/preflight.py`, then `uv run python scripts/fetch_team_snapshot.py A<N> <team_dir>` and `uv run python scripts/collect_github_evidence.py A<N> <team_dir>`.

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

- Use Conventional Commits with a path scope, for example `feat(A1/prompt): ...`, `fix(tools): ...`, `docs(agents): ...`, `chore(deps): ...`.
- Every commit has a body of 2-4 short bullets explaining what changed and why.
- Commits made by an AI agent end with `Harness:` and `Model:` metadata lines instead of a `Co-Authored-By` trailer, with `Model:` holding the exact `<provider>/<model>` identifier.
- Commit feedback in the `itpd-assignments-feedback` submodule first, then bump the submodule here.
- The `commit-itpd` skill (`.agents/skills/commit-itpd/SKILL.md`, also `/commit` in opencode) owns the message format, the staged-changes-only rule, and the model-identity rules.
