---
id: TASK-048
title: Keep dev-shell state inside the checkout under the DSH sandbox
status: Done
assignee: []
created_date: '2026-10-24 07:40'
updated_date: '2026-10-24 07:41'
labels: []
dependencies: []
ordinal: 48000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
DSH's workspace-write sandbox has one writable root (the session workspace) and no extra writable paths, so entering the dev shell failed: `nix develop` could not open `~/.cache/nix/fetcher-locks/*.lock`, `direnv allow` could not write `~/.local/share/direnv/allow`, and the Bun-backed `backlog` binary re-extracted its module cache to the ephemeral /tmp or to `./node_modules/.cache`. Relocate that state into the checkout the way `uv.toml` already keeps uv's cache in `.local/uv-cache`.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 `nix develop` and `backlog` work from a workspace-write sandboxed shell without writing outside the checkout.
- [x] #2 The shellHook no longer exports an invocation-dependent `BACKLOG_CWD`, and a stale value inherited from the launching shell is cleared.
- [x] #3 No probe artifacts or unintended untracked files remain, and `uv run` still works.
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
Verified inside a workspace-write sandbox: `nix develop --command bash -c 'backlog task list --plain'` lists this repository's tasks with `BACKLOG_CWD` unset, both from the repository root and from `scripts/`, and a stale ambient `BACKLOG_CWD=~/Desktop/gh/timeful` is cleared. Nix state landed in `.local/cache` (4.4 MB) and Bun's cache in `.local/bun-cache` (372 KB); `uv run python -c ...` still passes and no `node_modules/` was created. `direnv allow` remains a manual step outside the sandbox because the allow file lives under `~/.local/share/direnv`.

`uv run pytest` passed (319 tests); `markdownlint-cli2` lints 0 files because the only changed Markdown is under the ignored `backlog/**`.
<!-- SECTION:NOTES:END -->
