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

The reference was first authored for starter 2 at public source `8db49cb`.
**October 31, 2026 correction:** confirmed plan/history, terminal-steering and
earlier-source-integrity defects required replacing that prototype's record helper.
The guide now explains the starter 3 correction candidate: established canonical
request bundles, typed learning notes and restored operational duties. Earlier
trial evidence stays dated and separate.

The evidence page includes a rendered [seven-case overview](design/boards/director-pattern-explainer/evidence.html#case-overview) and a separate [source-readiness checklist](design/boards/director-pattern-explainer/evidence.html#release-readiness). The forensic findings stay version-bound history; later confidence/target/publication gates are recorded separately. The bounded source patch and selected published baselines are accepted. Core source `b237023cfb2f23fadb70d5d4ec7d7ce063bd8b43` and all three selected target commits were normally pushed and remote-verified; the readiness page records those exact commits. Starter 3 is a published source candidate, not a new formal release tag or a perfect-parity claim.

The [design-obligation parity matrix](development/BEHAVIOR_PARITY.md) and
[validation notes](development/DESIGN_NOTES.md#behavior-preservation-correction--october31-2026)
separate current source contracts, backend tests, actual actor observations and
remaining adoption limits. Candidate evaluation is not perfect parity or native
cold-start proof. Existing mature trackers, adaptations and privacy choices remain
authoritative; no silent starter-2 data migration is supplied. Private conversion
receipts and conversations are not part of this public board.

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


## Local hover-fix candidate - 2026-11-02

The current pinned app is **0.6.5**, an unpublished local candidate. Its exact
ZIP, SHA-256 sidecar and compatibility metadata are retained in `tinka/packages/`
for offline restore with `node tinka/setup.mjs`. ZIP SHA-256:
`8a298b32fe2085a635a3e9f46b486d4f56216f66c5781c77b15e9b5f674411d7`.
Earlier package versions and guidance above remain historical recovery material.

Preview hover retains the visible artwork in light and dark appearances. This
app replacement preserves existing board data, stable IDs, saved geometry,
notes, resource files and update preferences; it performs no workspace migration.
Keep prior packages and app backups. Never restore data over subsequent live work.
Technical installation and browser checks do not establish owner acceptance or
public publication.


## Local cover-layer candidate - 2026-11-02

The current pin is **0.6.6**, superseding the local 0.6.5 candidate above.
It preserves translucent hover and hides fallback labels behind available cover
previews while keeping unavailable/title-only fallbacks. The exact ZIP, checksum
and compatibility metadata are in `tinka/packages/` for offline pinned restore.
ZIP SHA-256: `d7ac7a901f0227319878baa7331be19503f364f1a1482c31dea2c8428004958f`.
Boards, geometry, notes, resource files and prior packages remain preserved; no
workspace conversion was performed. This remains an unpublished local candidate.


## Research and diagnosis boards - 2026-11-08

Research and diagnosis work gets a durable, progressive Tinka report. The root
board is **Research and diagnosis** (stable ID `research`), on Home. It is the
starting point for every investigation. It holds a short intro card stating that
rule, and one item per investigation. Each item opens a child board containing a
markdown `report.md` and a self-contained, paged `slides.html`, with optional SVG
diagrams. Update an investigation as findings land, keeping corrections visible.

Resources live in [design/boards/research/](design/boards/research/README.md),
registered as the `research` resource root. Read that folder's
[AGENTS.md](design/boards/research/AGENTS.md) before adding an investigation. The
first investigation (child board `research-2026-11-07-staffing-stewardship`)
diagnoses why a Director inherited full-strength worker settings and stopped acting
as the project's steward. It includes the corrections from independent review and
from the owner. The board is public: distil the evidence, and keep raw
conversations and private locators out.

After starting this project, append `/boards/research/` to the printed URL's
origin, or select it from Home. To open the first investigation's slides directly,
append `/resources/research/2026-11-07-staffing-and-stewardship/slides.html`.


## Inside agentic systems — November 10, 2026

The **Inside agentic systems** board (stable ID `agentic-systems-20261110`)
contains five connected animated diagrams: Agentic systems, The Director Pattern,
Learning and growth, Across systems, and People in the loop. It is a visual
prototype suite, with current method and proposed mechanisms distinguished.
It does not change the operating pattern.

Open `/boards/agentic-systems-20261110/` on this project's printed Tinka origin.
The full presenter is `/resources/agentic-systems/presenter.html`; its five chapter
links are `#systems`, `#director`, `#learning`, `#communication`, and `#human`.
Source and standalone run instructions live in
[the suite README](design/boards/agentic-systems-20261110/README.md).

The reviewed revision now includes a [native chapter gallery](design/boards/agentic-systems-20261110/gallery.html), [progressive art report](design/boards/research/2026-11-10-living-system-art/report.md), [five-page telling](design/boards/research/2026-11-10-living-system-art/slides.html) and [separate review scores](design/boards/research/2026-11-10-living-system-art/score-matrix.md). All five chapter reviews meet the seven-category bar; final delivery QA and owner creative acceptance remain separate. The first version and frozen iterations are preserved.


## Agentic systems executive briefing — November 11, 2026

The **Agentic systems — executive briefing (Claude Fable 5.2)** board (stable ID
`agentic-systems-briefing-20261111`) is a separate, simpler 24-step telling of the
same five topics plus a closing zoom-out to many systems for a ten-minute briefing, authored by Claude Fable 5.2. It shares
no files with the Inside agentic systems suite, which is unchanged. Open
`/resources/agentic-briefing/presenter.html`; source and notes are in
[its README](design/boards/agentic-systems-briefing-20261111/README.md).
First draft; owner review open.
