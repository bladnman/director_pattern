# Tinka in this project

This project's boards are in `design/boards`. Their manifests, experiments, assets,
handoffs and disk notes are durable project material. Keep them in version control,
including each board's `.state/notes.json`. Check your project's ignore rules.
The boards can be read and edited without installing a skill or running Tinka.

## Director Pattern field guide

The durable explainer is the **How the Director Pattern grows** board (stable ID
`director-pattern-explainer`). It contains seven topics: overview, moving parts,
growth, instruction ownership, learning and limits, practical examples, and evidence.
Pages and rendered SVG diagrams live in
[design/boards/director-pattern-explainer/](design/boards/director-pattern-explainer/README.md).
They are explanatory reference material, not installation payload or operating policy.

After starting this project, append `/boards/director-pattern-explainer/` to the
printed URL's origin to open the board directly, or select it from Home.
For the full-page guide, append `/resources/explainer/overview.html` to the printed
URL's origin. Start at [overview.html](design/boards/director-pattern-explainer/overview.html)
when serving the resource folder independently. All diagrams and styles are local.

The reference is grounded in public Director Pattern source `8db49cb`; its evidence
page distinguishes observed assigned-agent behavior, remaining overhead, startup
deviations and unproved native cold startup. Project-specific conversion receipts
and private conversations are not part of this public board.

This project pins Tinka **0.6.1** and includes its public ZIP/checksum in
`tinka/packages/` for offline restoration. The ZIP SHA-256 is
`4337123b10e177a13b2c73c9ef9bb98a2d76ba40e738b0d2dc36544137223042`,
matching the [official v0.6.1 release](https://github.com/bladnman/tinka/releases/tag/v0.6.1).
The replaceable app and machine-local config/process state remain ignored.

The initialized schema-2 metadata is `design/boards/.tinka/`. Change its canonical
organization, build states and review through supported CLI operations; do not
hand-edit transaction metadata. Preserve the complete durable store and resource
folder. Read this board's [AGENTS.md](design/boards/director-pattern-explainer/AGENTS.md)
and the installed [app instructions](tinka/app/AGENTS.md) before affected work.

## Restore on a new machine

With Node.js 22 or newer, run from the project root:

```sh
node tinka/setup.mjs
node tinka/app/cli.mjs start --config tinka/local/config.json
```

Setup installs the version pinned in [tinka/project.json](tinka/project.json),
verifies its archive checksum, and rebuilds this machine's config using relative
project paths. Open the URL printed by start. No global skill or registry is needed.
Setup first uses a matching committed `tinka/packages/tinka-vVERSION.zip` and
its `.sha256` sidecar when present. Otherwise it needs network access, or a
local ZIP and checksum passed with `--zip PATH --checksum PATH`.

Before editing boards, read their `AGENTS.md` and the installed app's
[agent guide](tinka/app/docs/AGENT.md) and [protocol](tinka/app/docs/PROTOCOL.md).
If the app is absent, restore it or use the board's portable instructions.
Preserve earlier rounds, stable IDs, assets and notes. Record actual project
requirements, such as which board is the accepted style guide, in project guidance.

## What travels with Git

Commit `TINKA.md`, the project's `AGENTS.md` pointer, `tinka/project.json`,
`tinka/setup.mjs`, `tinka/.gitignore`, and all of `design/boards/`, including disk
notes. Browser-only view preferences are local. `tinka/app/` and `tinka/local/`
are ignored: setup restores the app and recreates config, logs and process state.
A dot folder is not automatically ignored by Git; verify the actual staged files.
An app can also be vendored deliberately if offline restoration is required.

Run the normal start command whenever returning to boards, including when the server
is already running. Installed apps check for updates at most once daily and return
the verified URL. Default notify announces each new release once. Use
`node tinka/app/cli.mjs update now --config tinka/local/config.json`,
`update later` (24h), or `update policy notify|auto|off` with the same config.
Choose auto only with the owner's explicit personal consent; it installs eligible
compatible releases before a stopped start and never interrupts a running board.
Preferences stay in ignored `tinka/local/updates.json`. Read the installed agent
guide for compatibility, older-receipt bootstrap and recovery details.

Upgrade deliberately with `node tinka/setup.mjs --version X.Y.Z`, then review
and commit the changed version pin. Setup preserves existing boards and notes;
it never silently upgrades a checkout to the latest release.
