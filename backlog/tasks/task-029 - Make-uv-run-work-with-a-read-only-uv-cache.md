---
id: TASK-029
title: Make uv run work with a read-only uv cache
status: Done
assignee: []
created_date: '2026-10-19 10:44'
updated_date: '2026-10-19 10:44'
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
Diagnosis, measured in-session: (1) ~/.cache/uv is on a read-only mount, so uv fails at 'Could not acquire lock -> Could not create temporary file -> Read-only file system (os error 30)'; uv run --no-cache and uv run --python /usr/bin/python3 fail the same way, so the cache is always touched first. (2) The 'Unknown operating system: Empty module name' error is the Nix Python's sysconfig with an empty _PYTHON_SYSCONFIGDATA_NAME; with the variables the dev shell exports, uv run works, and uv itself reads pyvenv.cfg rather than importing sysconfig. Changes: scripts/uv.sh probes the default cache by writing a file and reruns uv with UV_CACHE_DIR=<repo>/.local/uv-cache (fallback .uv-cache) when it is unwritable; it works from any directory, leaves an existing UV_CACHE_DIR alone, and --migrate copies the default cache, skipping copies above 2 GiB unless ITPD_UV_MIGRATE_ALLOW_LARGE=1 (the default cache here is 7.9 GiB). .envrc exports UV_CACHE_DIR to the in-checkout cache only when no usable cache exists, so it refreshes the environment once instead of on every reload; the shim lives in .envrc because shellHook runs from the flake store and a cached dev shell does not refresh it. flake.nix drops the UV_CACHE_DIR shellHook fallback and guards the _PYTHON_* exports with ${VAR:-} under set -u. Validation: ./scripts/uv.sh run pytest 187 passed; scripts/preflight.py ready; scripts/uv.sh sync up to date; wrapper works from /tmp and with direnv variables cleared; nix develop with XDG_CACHE_HOME in /tmp runs a wrapped uv; markdownlint-cli2 clean on AGENTS.md and README.md. Not committed: waiting for the model identity to fill the Model: line.
<!-- SECTION:NOTES:END -->
