#!/usr/bin/env bash
# Run uv with a cache that works in this checkout, wherever it is invoked from.
#
# `uv` needs a writable cache directory. Here the default `~/.cache/uv` is on a
# read-only mount, so `uv run`, `uv sync`, and `uv lock` fail with
#
#     error: Could not acquire lock
#       cause: Could not create temporary file
#       cause: Read-only file system (os error 30) at ... ~/.cache/uv/.tmpXXXX
#
# before they ever look at the interpreter. This wrapper probes the default
# cache once and, when it is not writable, points UV_CACHE_DIR at
# `.local/uv-cache` inside this checkout (gitignored), falling back to
# `.uv-cache` when `.local` cannot be created (that happens when the sandbox
# only grants this repository root).
#
# The local cache starts empty: `uv run` re-syncs the dev environment into the
# existing `.venv` on first use, which is fast for this project because `.venv`
# already holds the packages. Use `--migrate` to copy the default cache into
# the local one; that only pays off for projects with heavy wheels.
#
# Only one of the two reported ways in which `uv run` fails: the other one, uv
# reporting "Unknown operating system: ''", is a Python calling sysconfig
# without its build data, not a cache problem. `uv run` itself does not need
# the fix (it reads the venv's pyvenv.cfg instead of importing sysconfig); set
# _PYTHON_HOST_PLATFORM/_PYTHON_SYSCONFIGDATA_NAME for code that calls
# sysconfig directly. See Troubleshooting in AGENTS.md.
#
# Usage: scripts/uv.sh run python -m pytest
#        scripts/uv.sh sync
#        scripts/uv.sh --migrate
#
# Optional environment:
#   UV_CACHE_DIR                     already set: used as is, nothing is probed
#   ITPD_UV_WRAPPER_CACHE            local cache path (default: <repo>/.local/uv-cache)
#   ITPD_UV_MIGRATE_ALLOW_LARGE=1    let --migrate copy a default cache over 2 GiB

set -euo pipefail

root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

if ! command -v uv >/dev/null 2>&1; then
  echo "scripts/uv.sh: uv is not on PATH; run this from the Nix dev shell (nix develop or direnv allow)" >&2
  exit 127
fi

migrate=0
if [ "${1:-}" = "--migrate" ]; then
  migrate=1
  shift
fi
if [ "$#" -eq 0 ] && [ "$migrate" -eq 0 ]; then
  echo "usage: scripts/uv.sh [--migrate] <uv arguments...>" >&2
  exit 2
fi

if [ -n "${UV_CACHE_DIR:-}" ]; then
  exec uv "$@"
fi

default_cache=$(uv cache dir 2>/dev/null || true)
default_cache=${default_cache:-${XDG_CACHE_HOME:-$HOME/.cache}/uv}

# Probe by writing a file: on a read-only mount mkdir fails even for an
# existing directory, and a failed mkdir may still leave the directory created.
cache_usable() {
  local target=$1 probe
  probe="$target/.probe.$$"
  ( mkdir -p "$target" && : >"$probe" ) >/dev/null 2>&1 || {
    rm -f "$probe" 2>/dev/null
    return 1
  }
  rm -f "$probe"
}

if [ "$migrate" -eq 1 ]; then
  # Run first so uv creates the target cache with its own markers.
  if ! cache_usable "$default_cache"; then
    echo "scripts/uv.sh: $default_cache is not writable, setting UV_CACHE_DIR=$root/.local/uv-cache" >&2
    export UV_CACHE_DIR="$root/.local/uv-cache"
    if ! mkdir -p "$UV_CACHE_DIR" 2>/dev/null; then
      UV_CACHE_DIR="$root/.uv-cache"
      mkdir -p "$UV_CACHE_DIR"
    fi
  fi
  uv sync "$@"
  destination=${UV_CACHE_DIR:-$default_cache}
  # The default cache can be tens of gigabytes: never copy it by default.
  set -o pipefail
  size=$(du -sk "$default_cache" 2>/dev/null | cut -f1 || true)
  size=${size:-0}
  if [ "$size" -gt 2097152 ] && [ "${ITPD_UV_MIGRATE_ALLOW_LARGE:-0}" != 1 ]; then
    echo "scripts/uv.sh: not copying $default_cache ($((size / 1024)) MiB) into $destination;" \
      "set ITPD_UV_MIGRATE_ALLOW_LARGE=1 to override, or let uv fill the cache on demand" >&2
    exit 0
  fi
  # Clear first so uv never reads a half-copied entry; ignore the read-only
  # source and keep uv's own markers (CACHEDIR.TAG) out of the copy.
  find "$destination" -mindepth 1 -maxdepth 1 \
    ! -name CACHEDIR.TAG ! -name .gitignore ! -name .lock -exec rm -rf {} +
  tar -C "$default_cache" -cf - --exclude=./CACHEDIR.TAG --exclude=./.lock . 2>/dev/null \
    | tar -C "$destination" -xf -
  echo "scripts/uv.sh: copied $default_cache into $destination" >&2
  exit 0
fi

if cache_usable "$default_cache"; then
  exec uv "$@"
fi

local_cache=${ITPD_UV_WRAPPER_CACHE:-$root/.local/uv-cache}
export UV_CACHE_DIR="$local_cache"
if ! mkdir -p "$UV_CACHE_DIR" 2>/dev/null; then
  UV_CACHE_DIR="$root/.uv-cache"
  mkdir -p "$UV_CACHE_DIR"
fi
echo "scripts/uv.sh: $default_cache is not writable, using $UV_CACHE_DIR" >&2

exec uv "$@"
