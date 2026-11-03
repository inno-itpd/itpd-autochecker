# ITPD autochecker

AI-agent tooling that reviews team submissions for the ITPD course ([`inno-itpd/itpd`](https://github.com/inno-itpd/itpd)).
A compliance agent produces the per-segment report, a separate semantic agent assesses whether the artifacts do their job, and the instructor decides the grade.

<!-- TODO how to ask an agent to grade? Maybe need a skill and need to document it somewhere here -->
<!-- TODO where to store submissions -->

## Setup

```console
git clone --recurse-submodules https://github.com/inno-itpd/itpd-autochecker
cd itpd-autochecker
cp .env.example .env   # add GITHUB_TOKEN
direnv allow           # or: nix develop
uv run pytest
```

## Layout

- `A<N>/grading_prompt.md`: segments and status guide for assignment N.
- `A<N>/itpd`: the course repository pinned at the commit assignment N is reviewed against.
- `A<N>/extract_feedback.py`: turns feedback reports into `dev.md` and `feedback_release.csv`.
- `agents/compliance-agent.md`: the one-team compliance prompt, used through `.claude/agents/` and `.opencode/agents/`.
- `agents/semantic-agent.md`: the one-team semantic feedback prompt, run after the compliance report is final.
- `agents/README.md`: the two-role pipeline and handoff contract.
- `docs/`: the grading policy and the feedback report format.
- `scripts/`: validate, inspect, patch, and regrade feedback reports.
- `uv.toml`: keeps uv's cache inside the checkout (`.local/uv-cache`), so `uv run` also works where `~/.cache/uv` is read-only.
- `itpd-assignments-feedback/`: the submodule holding submission PDFs, feedback, and exports.
- `backlog/`: Backlog.md tasks for this repo.
- `.dsh/`: the DSH overlay that registers the Backlog and codebase-memory MCP servers.

See `AGENTS.md` for the full workflow.
