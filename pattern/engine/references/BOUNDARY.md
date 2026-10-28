# Replaceable engine and project-owned integration

The installation has two owners. `engine/` contains upstream generic contracts,
references, and helper implementations. Everything outside it belongs to the
project, except the two explicitly managed compatibility launchers listed by the
manifest. Project context, roles, specialist responsibilities, policy, adapters,
tracker/config, exact sources, current activity, identities, receipts, and privacy
choices never belong in the engine. A customized project can replace the engine
without replacing those files.

## Interface 1

The manifest declares `engine_api_version: 1`, `engine_files`,
`project_seed_files`, and `entrypoint_files`. The existing `base_files` and
`tracked_files` remain the copy allowlists; the ownership lists partition them.
Engine files all live under `engine/`. Seeds are created only when absent and are
never update targets. Launchers are the only managed files outside the engine;
verify their baseline before replacing them. Unknown files or local edits inside
an installed engine block wholesale replacement until their owner reviews them.
Do not infer that every file under `.director/` is managed payload.

The explicit coupling points are:

- The host's one marked hook reads project-owned `.director/PATTERN.md` first.
  That small bridge names the one canonical role index, relative to the bridge,
  and points to `engine/PATTERN.md`. Its returned result precedes the engine read;
  the engine result precedes the index read. There is no circular bridge reread.
- The canonical project index selects generic definitions under `engine/` and
  project-owned standalone definitions wherever the project maintains them.
  Its project-wide guardrails and selected references carry local policy and
  overrides. Generic Director definitions load project-owned `PROJECT.md` one
  level above the engine. PROJECT records the same index locator as the bridge.
- Generic MODELS policy stays in the engine. User-authorized capability, budget,
  authority, and specialist constraints are project-owned required references,
  reached through PROJECT/index/definitions. An engine update cannot weaken them.
- The static identity pool is project-owned `IDENTITY_POOL.txt` beside the bridge.
  The roster/cursor stays in the project's canonical activity location.
- `tools/requests.py` and `tools/update_check.py` are thin interface-1 launchers.
  They pass the actual `.director/` root to implementations in `engine/tools/`.
  Direct engine CLI use derives that same root; explicit `--team`/`--root` retains
  its existing meaning. Python Store APIs still require their explicit root.
  No state/cache/config is written under `engine/`. Existing trackers need no
  bundled request helper or store.

Interface 1 does not change the request/config schemas, store format, policy or
receipt schema, role values, authority, or predecessor-store refusal. A future
incompatible interface requires explicit reviewed integration; never assume a
directory rename is a data migration or silently reset a store to make it fit.

## New setup and reusable stencils

Copy only selected manifest files, preserving their paths. Fill the project-owned
bridge/index/PROJECT and map real responsibilities. The root `.gitignore` and
identity pool are initial seeds; later project choices win. Never customize the
engine to record local roles, host snapshots, or tracker adapters.

A reusable stencil contains generic contracts plus placeholder project context
and its generic or domain role definitions. No initialized identity/config,
request/source records, activity, live roster, update policy, or completed receipt
is copied. Domain template configuration for an existing tracker is distinct from
an initialized bundled Director store; preserve its actual contract. Each copied
project performs first-use setup with its own identity where its backend needs
one. Record stencil provenance externally; generated-project acceptance is a
separate receipt. Preserve each stencil's specialized project-owned content.

## Reviewed transition from the flat installation

This is a one-time layout integration, not a tracker migration. Back up and verify
the actual installation and loaded startup chain before edits. Use its pinned
source/baselines to classify old files. Compare unknown drift rather than deleting
it. Preserve exact prior bytes externally or in ignored backups.

1. Place the reviewed generic payload under `engine/`. Move exact meaningful
   local adaptations into project-owned definitions, policy, or adapters; register
   their applicability and precedence in the existing canonical index before
   removing their globally loaded copies. Do not summarize away constraints.
2. Keep PROJECT, canonical index, definitions, privacy rules, pool/roster, trackers,
   config, state, sources, receipts, unfinished work, and actual handles intact.
   Remove historical host observations from loaded instructions only under the
   existing preservation rules, retaining exact originals and recovery evidence.
3. Replace the old bootstrap with the project bridge and update its existing
   canonical index entries/references to generic definitions under `engine/`.
   Repair actual stale callers. Preserve unrelated AGENTS bytes; keep one small
   marked hook. Remove obsolete flat generic files only after their exact origins,
   adaptations, references, and new destinations are accounted for.
4. Add reviewed compatibility launchers where selected. Validate both old CLI
   entrypoints and direct engine invocations against the real root in disposable
   fixtures. No helper/config/store schema or identity changes follow from layout.
5. Run [STARTUP](STARTUP.md)'s affected structural-route checks and fresh trials.
   Record performed and unrun checks, preservation mapping, hashes, and actual
   local-candidate/published provenance in the authoritative external evidence.
   Never call an unpublished candidate an official published revision.

## Subsequent engine replacement

Pin/review source and interface compatibility under [UPDATES](UPDATES.md). Verify
the installed engine against its receipt and inspect any drift. Back up, stage
exact selected engine bytes, check their links and affected interfaces, then
replace only `engine/` and reviewed launchers. Prune stale engine payload there;
do not prune project-owned neighbors. Preserve outside bytes and the bridge's
index pointer. No project-wide role rewrite, schema migration, new ledger, or
unconditional startup audit is part of a compatible engine replacement.

Verification stays incremental: helper changes test affected behavior and root
compatibility; behavior changes check relevant roles; bridge/index/interface
changes trigger the relevant startup trials. Static preservation and idempotence
checks do not establish fresh-host compliance or universal compatibility.
