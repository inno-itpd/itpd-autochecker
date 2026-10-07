# ITPD autochecker

AI-agent tooling that reviews team submissions for the ITPD course ([`inno-itpd/itpd`](https://github.com/inno-itpd/itpd)).
The agent writes structured feedback for each segment, and the instructor decides the grade.

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
- `agents/grader.md`: the one-team grader prompt, used through `.claude/agents/` and `.opencode/agents/`.
- `docs/`: the grading policy and the feedback report format.
- `scripts/`: validate, inspect, patch, and regrade feedback reports.
- `itpd-assignments-feedback/`: the submodule holding submissions (gitignored), feedback, and exports.
- `backlog/`: Backlog.md tasks for this repo.

See `AGENTS.md` for the full workflow.
