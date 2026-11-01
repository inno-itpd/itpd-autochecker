---
id: TASK-051
title: Register the Backlog and codebase-memory MCP servers through a .dsh overlay
status: Done
assignee: []
created_date: '2026-11-01 13:25'
updated_date: '2026-11-01 13:25'
labels: []
dependencies: []
ordinal: 51000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
dsh has no project-local configuration discovery: it composes bundle, profile, home-level, and explicit --patch layers only, so a repository cannot ship MCP servers that a plain `dsh web` picks up. Register the Backlog and codebase-memory MCP servers in a repository overlay that the launcher receives with --patch, mirroring the sibling timeful checkout, so sessions started from this checkout can use mcp__backlog__* and mcp__codebase-memory-mcp__* tools. Scope: local development harness only; no Python, grading, or feedback change.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 .dsh/cordis.patch.yml inserts the backlog and codebase-memory mcp-client rows, and `dsh --dump-config --patch .dsh/cordis.patch.yml` composes both while the same dump without --patch composes neither.
- [x] #2 .dsh/README.md states the launcher form, the flag-before-app-arguments ordering, the restart-after-edit rule, and the dsh plugin and --dump-default-config exceptions.
- [x] #3 The devShell provides the codebase-memory-mcp binary and .envrc pins CBM_CACHE_DIR under .local/, so indexing succeeds inside the workspace-write sandbox.
- [x] #4 .cbmignore keeps the vendored A*/itpd checkouts, the itpd-assignments-feedback data, and the tool state out of the graph.
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
Verified the overlay with a writable scratch DSH_HOME (`.local/dsh-verify`, because `--dump-config` rewrites the profile's `cordis.yml` and `~/.dsh` is read-only under the workspace-write sandbox): `dsh --patch .dsh/cordis.patch.yml --profile web --dump-config` composes the `mcp-backlog` and `mcp-codebase-memory` rows, the same dump without `--patch` composes none, and `dsh web --patch ... --dump-config` and `--profile headless` parse the same way. `dsh plugin --patch ...` hands the overlay path to pnpm, so launcher overlays are not a plugin-manager input, as documented.

The devShell resolves backlog 1.52.0 and codebase-memory-mcp 0.11.0 from the pinned nixpkgs (the same nixpkgs revision as the sibling timeful checkout, and the store path was already built). `CBM_CACHE_DIR="$PWD/.local/cache/codebase-memory-mcp" codebase-memory-mcp cli index_repository --repo-path .` indexed 1,408 nodes and 6,835 edges with the cache inside the checkout, and reported the `.cbmignore` directories and the PDF fixtures as excluded.

`uv run pytest` passed (388 tests); `markdownlint-cli2` reported 0 issues on `.dsh/README.md`, `README.md`, and `AGENTS.md`. The running web GUI keeps the profile it booted with, so the MCP tools appear only after relaunching `dsh` with `--patch`; the `.envrc` and `flake.nix` changes need `direnv reload` (or `nix develop`) to reach an existing shell.
<!-- SECTION:NOTES:END -->
