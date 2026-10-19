---
id: TASK-036
title: Rewrite the grader instructions for context budget and crash safety
status: Done
assignee: []
created_date: '2026-10-19 11:15'
updated_date: '2026-10-19 12:20'
labels: []
dependencies: []
ordinal: 36000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
All 14 crashed runs read oversized input. The agent prompt needs a documented interpreter rule, a context budget, a crash-safe loop, and a return line that survives partial success.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The environment preamble documents both working invocations, uv run python and .venv/bin/python, with a one-line probe that picks one
- [x] #2 The two uv failure causes are documented separately, with their distinct remedies
- [x] #3 A Context budget section states the observed dump sizes, the bounded-output rule, and prefer four small projections over one large read
- [x] #4 A crash-safe rule says to stop, narrow, and continue on unexpectedly large output, and never to re-read a summarized file
- [x] #5 The return value must be emitted on partial success and name the exact path written
- [x] #6 The prompt reads as one coherent instruction set with no duplicated step numbering, and markdownlint passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Rewrote agents/grader.md as one instruction set. Decisions: added a `## Environment` section before Modes with the one-line probe (`.venv/bin/python -c "import sys" ... || echo "uv run python"`), named both `.venv/bin/python` and `uv run python`, showed `.venv/bin/python` in the command examples, and noted that `uv run python` is the substitute when the probe picks it. Documented the two independent uv failures separately: the read-only cache (`Could not acquire lock` / `Read-only file system (os error 30)` at `~/.cache/uv`; run from the checkout so uv.toml uses `.local/uv-cache`, or set `UV_CACHE_DIR`) and the broken Nix-Python platform probe (`Unknown operating system: ""`; use `.venv/bin/python` or repair `_PYTHON_HOST_PLATFORM`/`_PYTHON_SYSCONFIGDATA_NAME`, with a note that a cache override cannot fix it). Consolidated the dump-size and bounded-projection guidance from Paths and step 11 into a new `## Context budget` section: read `summary.md` first (at most 60 lines), observed `commits.json` at 1.35 MB and `prs.json` at 284 KB, projections capped at about 40 lines, "prefer four small projections over one large read", and a crash-safe rule to stop, narrow, and continue and never re-read a summarized file. Step 11 now references `## Context budget` instead of repeating sizes and examples. Preserved all three modes, the write-early rendered report, the incremental payload groups, the regrade and inspect commands, the bounded `summary.md` digest, and the 1..14 step numbering, so the internal "After step 11" reference and A3 procedure-delta step mapping still point at the same steps. The return value now names the exact report path, is emitted for a written report even when a later check fails (with a `— <check> failed` suffix), and `FAIL` is reserved for the case where no report was written. Validation: `.venv/bin/python -m pytest -q` -> 239 passed in 1.93s; `markdownlint-cli2 agents/grader.md` -> 0 issues in 1 file (v0.23.2); `git diff --check` clean. Only `agents/grader.md` and this task file changed.
<!-- SECTION:NOTES:END -->
