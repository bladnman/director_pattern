# Install the candidate

On an adoption request, perform reversible local setup without another routine
confirmation. Reading alone is not adoption. Preserve existing authority, edits,
canonical trackers, and unfinished work. No publication, request migration, app
launch, scheduler, or executable installer is part of this setup. The installing
agent need not already be a Director; follow its actual assignment and host rules.
For an existing installation, go directly to [Repeat, upgrade, remove](#repeat-upgrade-remove)
and the pinned current update protocol; the first-install audit and trials below
are not an update fallback.

Install the separation of responsibilities, not a homemade summary in AGENTS.md.
Use [STARTUP.md](references/STARTUP.md) to audit the entire loaded instruction
chain and preserve specialized rules in reachable standalone definitions.

## Select and copy only the payload

[manifest.json](manifest.json) is the single authoritative copy allowlist. Its paths
are relative to this package; preserve each selected path under the target project's
`.director/`. Copy `base_files` in every mode. Add `tracked_files` only when selecting
a new bundled tracked store. Everything else is excluded; do not recursively copy
the repository or package directory. README, INSTALL, and manifest are guidance,
not payload. A temporary staging clone is optional transport only.

1. Inspect the target's actual startup instruction entrypoint and referenced rules.
   Follow STARTUP’s whole-chain audit, including oversized inherited startup
   files and misplaced role duties. Identify root, existing owners/tracker, and
   real delegation, model, effort, context, observation, and return capabilities. A tier label proves no selection.
   Find the project's existing maintained role definitions, runbooks, and
   project-wide guardrails, and whether managers can reach a recorder directly.
   The installation is committed with the project by default: contracts, filled
   PROJECT, config, requests, sources, current activity, and receipts, so another
   machine or a cloud checkout continues the same work. The payload's
   `.director/.gitignore` keeps only the helper lock, in-progress write scratch,
   pre-update backups, and daily update-check cache local. If the project is not
   under version control, report that as a parallelism and recovery limitation:
   parallel actors share one working tree that cannot be reviewed or rolled back
   by change, and the installation cannot continue elsewhere. Recommend
   initializing Git in place in the existing root, with no new checkout, and with
   the payload `.director/.gitignore` and the project's own ignore rules for
   private material in place before the first commit; initialize only at the
   user's request. Otherwise, check whether the repository has a remote and
   whether it is public. If it is public, or its visibility cannot be checked,
   warn the user once: `sources/` keeps their exact messages and attachments, and
   pushed history stays readable after a later deletion. Record the warning in
   PROJECT so later conversations and machines do not repeat it. Keeping more
   local is the project's choice, never a setup default; see
   [STATE](STATE.md#version-control). A template repository commits only the
   contracts and a placeholder PROJECT, never initialized config, requests,
   sources, activity, or a completed receipt; each generated project runs its
   own init.
2. Resolve published GitHub `main` to one exact commit SHA and inspect the selected
   revision before copying; retain its URL/SHA as the installation source. A local
   unpublished candidate must be labeled as such. An authorized installation agent
   copies the selected manifest files. Fill installed PROJECT context from actual facts,
   leaving unknowns visible. The adoption request and current host/assignment
   establish setup authority;
   apply default tracked mode and observed mappings within that authority, leaving
   ungranted policy decisions to the accountable owner. Tracked is default; lean optional.
   An existing canonical tracker uses the contract without creating a second store.
   Map PROJECT's role index, project-wide guardrails, durable capability policy and
   scoped host observations under [MODELS](MODELS.md#projecthost-mapping), Recorder
   route and state policy, and identity roster location. Reuse existing maintained
   definitions; generate a project-owned role index only when none exists,
   registering package definitions and actual project roles under STARTUP. Fill
   PATTERN’s canonical-index locator and record that same path in PROJECT. Never
   present illustrative entries as real roles. The roster lives in current activity, never in a seed.
3. For a new bundled tracked store, use an authorized setup actor to run
   `python3 <target>/.director/tools/requests.py init`. It creates/preserves config
   schema 1 and initializes request-store schema 2 with a stable project ID.
   Record the actual init receipt in PROJECT; do not hand-invent identity or
   convert legacy stores. Config is generated setup, not an extra copied file.
   Commit it: its project ID is the root of every request and source ID, so a
   clone that ran its own init would no longer match the committed records.
   Lean needs no helper; optional new lean config uses `"record_mode":"lean"`.
   Preserve existing config keys. Switching tracked to lean first requires
   reconciling commitments, live assignments, and pending evaluation; preserve the
   ledger and recovery pointers before a deliberate change. Mode cancels no work.
4. Complete the [startup audit and integration](references/STARTUP.md), then use
   one small marked hook in the actual loaded entrypoint, adapting the path:

   ```markdown
   <!-- director-pattern:start -->
   At the start of each conversation, your first tool invocation must only read
   `.director/PATTERN.md`; wait for and read its result. Complete its startup sequence
   and acknowledge the resolved role package before any task I/O, planning,
   delegation, changes, or substantive answer. A brief acknowledgment may come first;
   then address the original request in the same turn, without requiring a greeting
   or extra confirmation.
   <!-- director-pattern:end -->
   ```

   This routes to PATTERN's mandatory read/result dependencies and brief
   role-package acknowledgment, including for read-only questions and direct
   answers. The selected Director's background setup/identity check is separate.
   Verify that the host loads this actual entrypoint; file presence alone does
   not establish loading, automatic injection, or enforced ordering.

   Reuse an existing hook on upgrades. Preserve common project authority; move
   exact specialized instructions to maintained definitions/contracts and register
   them before removing their globally loaded copies. A tiny appended block alone
   does not repair an oversized startup chain. No duplicate role table belongs in
   the hook. Preserve a predecessor’s records and remove competing startup defaults
   through reviewed reversible integration, separately from any store migration.

For every mode, keep the daily discovery default **notify** unless the user has
explicitly chosen another mode. Record the exact accepted receipt pointer in
PROJECT's Source updates section. Only the checked project Director arranges
active-project checks under [UPDATES](references/UPDATES.md#daily-discovery-and-project-preference);
the shared bootstrap and worker startup do not run them. `update-policy.json` is
project-owned generated configuration, preserved on upgrades and absent from seeds.
The base helper uses an already available Python standard library; do not install
a runtime or dependency for checking, and disclose unavailable capability.

For every mode, record the source URL/SHA, selected managed-file paths and SHA-256
baselines, startup wiring, adaptations, and verification in a setup receipt under
`.director/receipts/`. It is committed so an update from any checkout can compare
baselines. Baselines describe installed bytes after adaptation, not successful
behavior. Committed files use project-relative paths. Never seed a completed
receipt into a template.

## Verify without polluting the backlog

Run [STARTUP’s static checks and fresh host trials](references/STARTUP.md#static-checks-then-fresh-host-trials).
Verify that the host actually loads the entrypoint and selected role/context
files. Check canonical state, requested versus actual model controls, and truthful
behavior when delegation/persistence is unavailable. Confirm the role index and its
listed definitions resolve, the Recorder route is one the host actually supports,
and the identity roster location is recorded; record unmapped roles as gaps. In a
Git repository, run the `git check-ignore` check in [STATE](STATE.md#version-control)
and report a parent or global rule that ignores `.director/`; without version
control, record the limitation and recommendation from step 1. For an existing
tracker, verify its actual mapped workflow and persistence receipts without installing a
new helper or second store. For lean, verify core wiring and current activity/
decision persistence; honestly retain its lack of a complete-ledger promise.

**Only for a new bundled tracked store**, perform the helper checks below. It
needs Python 3.10+ on macOS/Linux for `fcntl` advisory locks. Missing dependencies
or failed checks leave that tracked setup incomplete; report the limitation.
Have an authorized setup actor run `validate` on its actual store without modifying
it; an empty store is valid. Separately, have an authorized setup actor test the helper lifecycle
in a newly created disposable directory, never by adding dummy actual requests:

1. Copy the selected package helper to `<fixture>/tools/requests.py` and run its
   `init` command. Write a tiny UTF-8 `<fixture>/raw.txt` artificial request. The
   fixture must be separate from the actual project and have its own project ID.
2. Save the four literal minimal-lifecycle plan, dispatch, submit, and accept JSON
   examples from [TOOLING.md](references/TOOLING.md) as separate event files in the fixture.
   Its dispatch handle is synthetic fixture input, not an actual execution claim.
3. Substitute the fixture path and returned ID, then run:

   ```sh
   python3 <fixture>/tools/requests.py init
   python3 <fixture>/tools/requests.py create --raw-file <fixture>/raw.txt --title "Fixture only" --event-id "$(python3 <fixture>/tools/requests.py event-id create)"
   python3 <fixture>/tools/requests.py apply <returned-ID> --event-file <fixture>/plan.json --expect-revision 1
   python3 <fixture>/tools/requests.py apply <returned-ID> --event-file <fixture>/dispatch.json --expect-revision 2
   python3 <fixture>/tools/requests.py apply <returned-ID> --event-file <fixture>/submit.json --expect-revision 3
   python3 <fixture>/tools/requests.py apply <returned-ID> --event-file <fixture>/accept.json --expect-revision 4
   python3 <fixture>/tools/requests.py show <returned-ID>
   python3 <fixture>/tools/requests.py validate
   ```

4. Confirm done under archive/<REQ-ID>/request.md, the linked immutable source
   preserves exact raw text, expected history/revisions, and successful validation. Remove only the disposable fixture afterward. No external test suite
   or maintainer document is required for this check.

Obtain a factual setup receipt with the actual startup wiring, required files,
project configuration/mode, and canonical state checked. Align PROJECT's startup
fields with that evidence. The installing agent can prepare this receipt within
its adoption authority; use existing authorized recording/staffing capabilities
where available. No Director title or newly spawned Recorder is required to
perform setup. After adoption, the installed role-specific staffing/state rules
apply, including the separate Director identity check below. Resolve each
conversation's assignment role first. For the project Director conversation, the recorder checks the current facts before the director
judges whether to show `🎬`; refresh after relevant changes. Other roles omit the
badge without this check. Installation never overrides an explicit worker assignment.
Missing wiring/files, unknown mode, or an unavailable recorder leave
the check incomplete; explain that plainly without a badge. Lean and existing
trackers use their applicable setup without requiring a bundled helper or config.
Report installation separately from author approval or a successful fresh-session
behavioral trial. Payload links are relative; fill PROJECT locally. Files do not
start workers, and the identity marker does not claim live supervision.

## Repeat, upgrade, remove

For an existing installation, resolve published GitHub `main` to an exact reviewed
SHA on an explicit or standing-authorized update, then use that revision's
[update protocol](references/UPDATES.md), even if the installed version has no
protocol or requires a full audit on every upgrade. Read installed guidance for
local adaptations and preserve project-owned rules and host restrictions; resolve
any conflict with the accountable owner. Select checks from the upstream delta and
local drift. Routine changes use focused checks and still-applicable evidence;
full startup audits and fresh host trials run only when their changes require them.
Do not restart the first-install procedure just to update an older installation.
Active-project discovery defaults to daily notification; recorded project-scoped
“always update director pattern” authorizes the same safe update protocol. Reuse
the existing hook and preserve local
context, adaptations, identities, role index and definitions, model mapping, identity
roster, canonical state, and unfinished work. Missing
baselines require comparison to the prior pinned upstream revision or explicit
review, never blind replacement. Record a new source revision only after checks
succeed; no tracker migration is an update side effect.

For removal, have the recorder identify unfinished requests, actual handles,
pending evaluation, and decisions. Reconcile execution and retain records at an
agreed reachable location. Remove the marked hook and unused contract files only;
preserve unfinished state and recovery pointers. Removing files stops no agents.
