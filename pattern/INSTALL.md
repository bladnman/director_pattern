# Install the candidate

On an adoption request, perform reversible local setup without another routine
confirmation. Reading alone is not adoption. Preserve existing authority, edits,
canonical trackers, and unfinished work. No publication, request migration, app
launch, scheduler, or executable installer is part of this setup.

## Select and copy only the payload

[manifest.json](manifest.json) is the single authoritative copy allowlist. Its paths
are relative to this package; preserve each selected path under the target project's
`.director/`. Copy `base_files` in every mode. Add `tracked_files` only when selecting
a new bundled tracked store. Everything else is excluded; do not recursively copy
the repository or package directory. README, INSTALL, and manifest are guidance,
not payload. A temporary staging clone is optional transport only.

1. Inspect the target's actual startup instruction entrypoint and referenced rules.
   Identify root, existing owners/tracker, and real delegation, model, effort,
   context, observation, and return capabilities. A tier label proves no selection.
   Find the project's existing maintained role definitions, runbooks, and
   project-wide guardrails, and whether managers can reach a recorder directly.
   Before writing private context, config, state, sources, or receipts, verify
   effective exclusions and that none of those destinations are Git-indexed.
   Preserve already tracked user history and report a reconciliation need; ignore
   rules alone do not protect indexed files. Keep generic contracts versionable
   where desired; customized context and setup facts stay private. Template seeds
   carry placeholders, never shared initialized IDs or copied runtime state.
   A generated project initializes its own identity only after this privacy gate.
2. Resolve published GitHub `main` to one exact commit SHA and inspect the selected
   revision before copying; retain its URL/SHA as the installation source. A local
   unpublished candidate must be labeled as such. Have an installation worker copy
   the selected manifest files. Fill installed PROJECT context from actual facts,
   leaving unknowns visible. The director decides mode/mappings; the worker records
   them. Tracked is default; lean optional.
   An existing canonical tracker uses the contract without creating a second store.
   Map PROJECT's role index, project-wide guardrails, model/host mapping, Recorder
   route and state policy, and identity roster location. Reuse existing maintained
   definitions; seed or link a local role index (the generic ROLES entries plus
   actual project roles) only when none exists. Never present illustrative entries
   as real roles. The roster lives in private current activity, never in a seed.
3. For a new bundled tracked store, have the recorder run
   `python3 <target>/.director/tools/requests.py init`. It creates/preserves config
   schema 1 and initializes request-store schema 2 with a stable project ID.
   Record the actual init receipt in PROJECT; do not hand-invent identity or
   convert legacy stores. Config is generated setup, not an extra copied file.
   Lean needs no helper; optional new lean config uses `"record_mode":"lean"`.
   Preserve existing config keys. Switching tracked to lean first requires
   reconciling commitments, live assignments, and pending evaluation; preserve the
   ledger and recovery pointers before a deliberate change. Mode cancels no work.
4. Add one small marked hook to the actual loaded instruction entrypoint, adapting
   relative paths to its location. Preserve the rest of that file:

   ```markdown
   <!-- director-pattern:start -->
   Read `.director/PATTERN.md` and resolve your assignment role first. New project
   conversations default to their project Director regardless of who opened them;
   explicit assignments override that default. Bounded delegated assignments must
   name Role: worker/director, responsibility, scope, and authority. Clarify missing
   delegated roles with the assigner; ancestry or inherited history grants neither.
   Directors also read PROJECT.md, MODELS.md, and STATE.md inside `.director/`: the
   project Director reads DIRECTOR.md, a Request Manager reads REQUEST_MANAGER.md,
   and anyone staffing work follows ROLES.md, ASSIGNMENT.md, and IDENTITIES.md.
   Workers/reviewers load their assignment and its supplied role references;
   recorders load RECORDER.md, STATE, and tracked references when applicable.
   Director-only authority stays with directors. Before the project Director uses
   the 🎬 identity, have a Small recorder check this conversation's installed
   wiring, required files, and project configuration/mode; the Director judges the
   receipt under PATTERN's startup check. Request Managers and other roles use
   their assigned identity, never the badge.
   <!-- director-pattern:end -->
   ```

For every mode, record the source URL/SHA, selected managed-file paths and SHA-256
baselines, startup wiring, adaptations, and verification in an ignored setup receipt.
Baselines describe installed bytes after adaptation, not successful behavior. A
generic template PROJECT remains versionable; actual generated-project context
belongs in an ignored local overlay loaded by its startup hook. Never seed a
completed receipt.

## Verify without polluting the backlog

Verify that the host actually loads the entrypoint and referenced role/context
files. Check canonical state, requested versus actual model controls, and truthful
behavior when delegation/persistence is unavailable. Confirm the role index and its
listed definitions resolve, the Recorder route is one the host actually supports,
and the identity roster location is private; record unmapped roles as gaps. For an existing tracker,
verify its actual mapped workflow and persistence receipts without installing a
new helper or second store. For lean, verify core wiring and current activity/
decision persistence; honestly retain its lack of a complete-ledger promise.

**Only for a new bundled tracked store**, perform the helper checks below. It
needs Python 3.10+ on macOS/Linux for `fcntl` advisory locks. Missing dependencies
or failed checks leave that tracked setup incomplete; report the limitation.
Have the recorder run `validate` on its actual store without modifying it; an
empty store is valid. Separately, have a worker/recorder test the helper lifecycle
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
   python3 <fixture>/tools/requests.py create --raw-file <fixture>/raw.txt --title "Fixture only" --event-id fixture-capture-1
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

Obtain a recorder setup receipt with the actual startup wiring, required files,
project configuration/mode, and canonical state checked. Align PROJECT's startup
fields with that evidence. Resolve each conversation's assignment role first. For
a director conversation, the recorder checks the current facts before the director
judges whether to show `🎬`; refresh after relevant changes. Other roles omit the
badge without this check. Installation never overrides an explicit worker assignment.
Missing wiring/files, unknown mode, or an unavailable recorder leave
the check incomplete; explain that plainly without a badge. Lean and existing
trackers use their applicable setup without requiring a bundled helper or config.
Report installation separately from author approval or a successful fresh-session
behavioral trial. Payload links are relative; fill PROJECT locally. Files do not
start workers, and the identity marker does not claim live supervision.

## Repeat, upgrade, remove

For an existing installation, follow the installed
[update protocol](references/UPDATES.md). Published GitHub `main` is the upstream
source of truth; resolve it to an exact reviewed SHA for each explicit update.
Normal startup never silently updates. Reuse the existing hook and preserve local
context, adaptations, identities, role index and definitions, model mapping, identity
roster, canonical state, and unfinished work. Missing
baselines require comparison to the prior pinned upstream revision or explicit
review, never blind replacement. Record a new source revision only after checks
succeed; no tracker migration is an update side effect.

For removal, have the recorder identify unfinished requests, actual handles,
pending evaluation, and decisions. Reconcile execution and retain records at an
agreed reachable location. Remove the marked hook and unused contract files only;
preserve unfinished state and recovery pointers. Removing files stops no agents.
