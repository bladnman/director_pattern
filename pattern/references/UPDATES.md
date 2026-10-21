# Update an installed pattern

Published [GitHub main](https://github.com/bladnman/director_pattern) is the upstream
source of truth. An agent performs an update only on an explicit authorized request;
normal project startup checks its installed setup and never silently fetches or
replaces it. This is a bounded installation operation, not a daemon or a new state
engine. Existing project and host permissions still apply.

The director owns scope, compatibility decisions, and acceptance. An explicitly
assigned worker performs the update; a Small recorder handles routine inspection,
backups, and receipts. Every delegated assignment names worker/director role,
outcome, scope, and authority. Unavailable capabilities remain visible.

## Pin and inspect the incoming revision

Resolve the published repository's `main` to one full commit SHA using the available
Git/API transport. Fetch that exact revision into temporary staging and inspect its
manifest and relevant contract/helper changes before applying them. Recheck the
staged revision matches the pinned SHA; never combine files from changing `main`
URLs. Fetching is not permission to execute downloaded code, migrate data, publish,
or copy repository history into the target. Only the manifest-selected payload
belongs under `.director/`; maintainer docs, tests, and private material do not.

Identify the actual project root and loaded startup wiring. Read the existing
private setup receipt, PROJECT (and local overlay if used), configured mode,
canonical tracker, local adapters, and current installed files. Do not infer actual
role, model support, or current worker liveness from a saved receipt.

## Compare before replacing

Before edits, create a unique dated private backup of every managed file and
startup file to be changed, with original paths and SHA-256 hashes. Verify backup
bytes. Keep backups and receipts outside Git/public payload. Verify effective ignore
rules and the index for all private destinations before any writes; an ignore rule
does not remove indexed history. Preserve existing user material and report privacy
conflicts rather than silently untracking or rewriting it.

Compare three versions for each selected managed path:

- **Baseline:** bytes/hash installed after the last successful setup or update.
- **Current:** actual local bytes, including intentional project adaptations.
- **Incoming:** the selected file from the exact reviewed upstream revision.

A current/baseline match means no new edits since the last setup; it does not
mean the file has no persistent local adaptation. Also compare the prior upstream
file to the installed baseline and review recorded adaptations. Whole-file
replacement is safe only when that baseline matches prior upstream and no required
adaptation is lost, or an explicit reviewed result preserves those adaptations.
Otherwise merge the upstream delta into adapted current bytes, even when current
matches baseline. Any new current/baseline differences also need preservation and
review. Never choose the newer file wholesale merely because its hash is unchanged
since installation. PROJECT/context and project-owned adapters are never wholesale
replaced by upstream. Retain the prior upstream SHA and adaptation notes so that
this comparison remains possible.
If a previous receipt lacks baselines, reconstruct a safe comparison from its pinned
upstream revision and inspect local differences, or require explicit review. Unknown
provenance is a review requirement, never evidence that replacement is safe.

Preserve project context/overlays, host mappings, custom adapters, state mode, stable
project/request IDs, source bundles and attachments, request history, activity,
decisions, and actual handles. Also preserve the project-owned role index, its role
definitions and overrides, project-wide guardrails, model/host mapping, and the
private identity roster, cursor, and current activity. These are project-owned, not
upstream payload; an initialized roster or cursor never overwrites current state.
A project's replacement identity pool is an adaptation, merged like any other.

Policy adoption does not reassign work. Existing open director-owned requests keep
their owner, handles, and obligations until an explicit acknowledged assignment or
handoff changes responsibility. Do not bulk-rewrite owners, spawn managers, or
create a role index full of placeholder entries merely because the package changed.
Keep one loaded startup hook and merge its role/privacy rules without erasing
specialized project instructions. A template update changes only generic seeds;
never copy a configured store, shared identity, runtime state, or a completed setup
receipt into a seed. Generated projects perform their own first-use initialization.

Inspect helper/config/store schema compatibility before replacing a bundled helper.
An incompatible or uncertain schema blocks that part of the update; preserve the
old helper and state, report the boundary, and obtain a separate migration decision.
Do not auto-migrate a tracker, initialize a second ledger, switch modes, or assign a
new project identity to make an update pass. A Producer Pattern installation is a
separate predecessor package, not an earlier revision of this one: its `.producer/`
store uses the `request-bundles` format with `producer` fields, and this helper
refuses it before reading or writing. Moving from it is an explicit migration
decision, never an update; do not edit its config or records to make it open. Lean and existing trackers retain their
applicable workflow and do not acquire a bundled backend as an update side effect.

## Validate and record the result

Check selected payload presence and local links, the single actual startup path,
role resolution (including missing-role clarification and explicit bounded child
directors), configured mode/canonical state, preserved adapters, role index and
Recorder route, private roster location, and privacy/index boundaries. Verify a template remains generic and generated identities are separate.
Use read-only validation of actual state where supported; use disposable fixtures
for necessary helper behavior checks, never dummy requests in the real backlog.
Do not claim a cold-session behavioral trial unless one actually ran.

Only after all required checks succeed, write the private update receipt: source
URL/full SHA, prior revision, selected managed paths and resulting SHA-256 baseline
hashes, startup wiring/hash, preserved adaptations, backup location/hashes, checks
and limits. Update the project's source pointer to that successful receipt. A
partial/failed update retains the old accepted revision and records the actual
mixed state and next action; it must not advertise complete adoption. Restore only
owned edits from verified backups when safe, preserving intervening changes.

Report what changed, what remained locally adapted, verification and limitations.
Refresh the director's current-conversation installation check after setup changes;
a successful file update alone grants no badge, role, or live supervision claim.
