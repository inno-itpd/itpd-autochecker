---
id: TASK-029
title: Make uv run work with a read-only uv cache
status: Done
assignee: []
created_date: '2026-10-19 10:44'
updated_date: '2026-10-19 11:06'
labels: []
dependencies: []
ordinal: 29000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
In some environments (and inside the dev shell of this repo, as of 2026-10-19) the default uv cache ~/.cache/uv is mounted read-only, so every uv run, uv sync, and uv lock fails with 'Could not acquire lock ... Read-only file system (os error 30)' before uv ever reaches the interpreter. --no-cache and an explicit --python do not help, because uv creates its lock and temp files in the cache directory first. Provide a wrapper that probes the default cache and points UV_CACHE_DIR at a cache inside the checkout when it is not writable, make plain uv run work for direnv users, and document this cache cause separately from the sysconfig/'Unknown operating system' interpreter cause so neither is misdiagnosed as the other.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 scripts/uv.sh runs uv with a writable cache from any directory and honours an existing UV_CACHE_DIR
- [x] #2 .envrc exports UV_CACHE_DIR to the in-checkout cache only when no usable cache exists, so plain uv run works after a direnv reload
- [x] #3 flake.nix no longer picks UV_CACHE_DIR in the shellHook and keeps the sysconfig exports guarded under set -u
- [x] #4 AGENTS.md and README.md document the wrapper and keep the two uv failure causes apart
- [x] #5 ./scripts/uv.sh run pytest passes and markdownlint-cli2 is clean on the changed Markdown
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Superseded by TASK-030: the uv.toml cache-dir replaces the wrapper and the .envrc shim. scripts/uv.sh was removed; uv run now works without any wrapper, and an exported UV_CACHE_DIR still overrides the file. Kept in Done history because the diagnosis of the two distinct uv failure causes (read-only cache vs sysconfig) still holds in AGENTS.md.
<!-- SECTION:NOTES:END -->
