# DSH patch overlay

`.dsh/cordis.patch.yml` is a `dsh` overlay that registers the Backlog and codebase-memory MCP servers as `mcp__backlog__*` and `mcp__codebase-memory-mcp__*`.
`dsh` does not discover this file on its own, so pass it explicitly when launching from the checkout root:

```sh
dsh --patch .dsh/cordis.patch.yml --profile web --port 0 --no-open
```

`--patch` is a launcher flag, so it must come before any app argument.
`dsh web` is shorthand for `dsh --profile web`, and the launcher accepts launcher flags after the profile name.
Use the same form for another app, for example `dsh headless --patch .dsh/cordis.patch.yml "run the tests"`.
Launching `dsh` without the flag boots the profile without these MCP servers.

Overlays are read at launch, so restart `dsh` after editing `.dsh/cordis.patch.yml`; configuration HMR does not watch them.
`dsh plugin` and `--dump-default-config` reject launcher overlays, so omit `--patch` for those invocations.
Check the composition without booting a session with `dsh --patch .dsh/cordis.patch.yml --profile web --dump-config`.

The `backlog` and `codebase-memory-mcp` binaries come from the flake devShell.
`.envrc` pins `BACKLOG_CWD` to this checkout and `CBM_CACHE_DIR` under `.local/`, so `backlog` resolves this project and graph-cache writes stay inside the sandboxed checkout.
Run `direnv allow` after changing `.envrc`.
The index skips the vendored `A*/itpd/` checkouts and the submission data under `itpd-assignments-feedback/` as `.cbmignore` lists.

To add another MCP server, append a row to the `insert` list in `.dsh/cordis.patch.yml` with a unique `serverName`, then relaunch with the flag.
