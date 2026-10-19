---
id: TASK-030
title: Force the uv cache into the checkout with uv.toml
status: Done
assignee: []
created_date: '2026-10-19 11:06'
updated_date: '2026-10-19 11:09'
labels: []
dependencies: []
ordinal: 30000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Plain `uv run` failed with 'Could not acquire lock ... Read-only file system (os error 30)' at ~/.cache/uv. TASK-029 worked around this with scripts/uv.sh and a UV_CACHE_DIR export in .envrc, but made callers opt in and kept a wrapper for one purpose. Replace that with a tracked uv.toml that sets `cache-dir = ".local/uv-cache"`: uv resolves a relative cache-dir against the project root, so a plain `uv run` works from any subdirectory without exporting anything, and no per-machine or per-directory absolute path is involved. Remove the now-redundant wrapper and the .envrc shim, whose exported UV_CACHE_DIR would override the tracked file with a stale path.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 uv.toml sets cache-dir to .local/uv-cache and plain `uv run` succeeds from the repository root and from nested subdirectories while ~/.cache/uv is read-only
- [x] #2 scripts/uv.sh is removed and no tracked file references it
- [x] #3 .envrc no longer exports UV_CACHE_DIR, which would override uv.toml with a stale absolute path
- [x] #4 AGENTS.md, README.md, and flake.nix document uv.toml instead of the wrapper, including that uv does not discover uv.toml from outside the checkout
- [x] #5 `uv run pytest` passes, `uv run python scripts/preflight.py` is ready, and markdownlint-cli2 is clean on the changed Markdown
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
Root cause: uv touches its cache before it does anything else, so on this machine (~/.cache/uv on a read-only mount) even `uv run --no-cache` fails upstream of the interpreter. The fix cannot live in an environment variable exported from a tracked file: a static path breaks when the checkout moves. uv resolves a RELATIVE `cache-dir` against the project root (verified: `uv cache dir` prints the literal value, and `uv run -v` logs 'Found workspace configuration at .../uv.toml'), so uv.toml with `cache-dir = ".local/uv-cache"` gives a plain `uv run` a writable in-repo cache from any subdirectory. `.local/` was already gitignored and uv writes its own CACHEDIR.TAG/.gitignore inside the cache. Removed scripts/uv.sh (119 lines) and the .envrc probe shim: with the tracked file they were redundant, and the shim's exported UV_CACHE_DIR would OVERRIDE uv.toml with a stale absolute path. .envrc is left as just `use flake` with no explanatory comment: the rationale lives in uv.toml (adjacent to the setting), AGENTS.md (policy), and git history, and a comment there had already gone stale within the hour by still naming the deleted wrapper. Outside the checkout uv does not discover uv.toml, so that case is documented as `--config-file <repo>/uv.toml` or UV_CACHE_DIR rather than kept as a wrapper. Also fixed a pre-existing Troubleshooting error found in passing: it said `direnv allow` reloads a stale shell, but only `direnv reload` does. Validation: ~/.cache/uv probed as still read-only in the same command; `uv run` ok from the root, tools/, and tools/grader_tools/; `uv cache dir` = .local/uv-cache; an explicit UV_CACHE_DIR still overrides the file; `uv run pytest` 187 passed; scripts/preflight.py ready (3/3); markdownlint-cli2 clean on AGENTS.md and README.md (pre-existing MD009/MD041/MD047 in the untracked TODO.md and MD025 in an A2 feedback file were already failing and are unrelated); flake.nix parses via nix-instantiate. Committed: no (staged only, awaiting the Model: identity).
<!-- SECTION:NOTES:END -->
