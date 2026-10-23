# Update an installed pattern

Published [GitHub main](https://github.com/bladnman/director_pattern) is the upstream
source of truth. An agent performs an update on an explicit request or recorded
project-scoped standing authorization. The checked project Director arranges a tiny
metadata check at its first/next active project interaction, at most once per rolling
24 hours, and defaults to notifying the user. No worker, Request Manager, bootstrap,
or global skill starts these checks. This adds no daemon, scheduler, runtime
installation, dependency, or wakeup. Existing project and host permissions still apply.

## Daily discovery and project preference

The absent `update-policy.json` means **notify**. With a package change available,
say exactly: **A new Director Pattern is available. Say “update director pattern”
to install it.** Emit it once for that daily result; do not repeat cached notices
on each turn. A failed check is a quiet best-effort result, not a reason to delay
the user's work or retry on every reply. Return errors once to the Director/Recorder;
explain an actionable persistent gap when relevant without repeating user alerts on
each turn. No check runs while the project is inactive; "daily" means the next active
interaction after 24 hours, not midnight or a background appointment.

When the user says **“always update director pattern”**, preserve that source and
use the existing authorized execution/Recorder route to save **automatic** for
this project. That utterance is standing update authorization, with no extra
confirmation. "Notify me instead" saves **notify**; "stop checking for updates"
saves **off**. These choices affect only this installation. Neither ordinary
installation nor this feature's adoption enables automatic mode. A later explicit
manual update remains possible with checks off.

The installed base helper [update_check.py](../tools/update_check.py) uses an
already available Python 3.10+ on macOS/Linux and its standard library. Run it
through an existing authorized tool-execution route; a separate checking model
is unnecessary. The project Director alone decides when it is due; the Recorder
can execute the deterministic command without creating another checker agent.
If the runtime/tool is unavailable, report that gap; do not install software or
promise checks occurred. Lean and custom trackers need no bundled request store.

Supply PROJECT's **exact authoritative receipt pointer**, relative to the project
root (or an absolute path inside `.director/`); never select the newest receipt by
filename, timestamp, or directory order:

```sh
python3 /project/.director/tools/update_check.py check --receipt .director/receipts/<accepted-receipt>.json
python3 /project/.director/tools/update_check.py set-policy automatic --authorization 'sources/<user-source>/input.txt: explicit always-update request'
```

The root defaults to the helper's installed `.director/`; `--root /project/.director`
before the command supports an explicit root. For notify/off use the same
`set-policy` command and the actual source of that choice. The generated,
committed `update-policy.json` has schema 1, `mode` (`notify`, `automatic`, or `off`),
`authorization` (user-source reference), and `changed_at` (UTC Unix seconds).
Preserve unknown project fields; reject an unknown schema or malformed policy
for review rather than resetting it. It is project configuration, not a new
request-ledger schema, and is never a completed template seed.

The ignored `.update-check.json` caches schema 1, UTC `last_attempt` (including
failure/interruption), last success/result, and a published-baseline tree identity.
A nonblocking `.update-check.lock` serializes cooperating local chats and preference
writes; atomic replacement prevents partial JSON. Busy callers return quietly. Retain `next_check_at` in the active conversation
so same-day turns skip the helper too; do not spawn a model merely to read the
cache. A new conversation reuses the existing setup/Recorder/tool route to read it.
A policy change retains the daily attempt window. Clock rollback stays throttled
until that timestamp plus 24 hours. Corrupt/unknown caches fail closed without
network or automatic reset; preserve them for review. Do not delete/reset a cache
to force another routine check. The cache/lock are local to one machine; separate
checkouts can each check once a day. This is no cross-machine scheduler or lock.

### Concrete metadata source and response

The helper performs bounded HTTPS JSON reads against the existing public repository:

1. `https://api.github.com/repos/bladnman/director_pattern/git/ref/heads/main` → full `object.sha`.
2. `/repos/bladnman/director_pattern/git/trees/<that-sha>` on the same API → the
   entry with `path: "pattern"`, `type: "tree"`, and its Git tree `sha`.
3. On first use, the same root-tree endpoint at the **installed published base SHA**
   supplies its `pattern` identity, unless already recorded in the receipt or cache.

Use an 8-second timeout per read, no retries, and bounded response sizes. Ordinarily
this is two metadata reads, at most three on baseline bootstrap. No source code is
fetched or executed. Compare package-tree identity, not whole-repository commit
inequality: a website-only main commit must not alert, even when the installed
receipt postdates the last package-changing commit. Any change within the
self-contained `pattern/` package, including installation guidance/manifest, is
relevant. Tree changes indicate a different published package, not semantic version
ordering or proof of compatibility; a rollback also needs normal review.

The receipt format is `source: {url: "https://github.com/bladnman/director_pattern",
sha: "<full published commit>", published: true, pattern_tree_sha: "<optional tree>"}`
plus installed `managed_files` baselines. Existing receipts with `source.sha` and
`published: true` bootstrap their tree from GitHub. Other older formats require
review and a normalized receipt through the existing recording route; never guess
or promote an unpublished SHA. Keep a local candidate delta labeled separately
from its authoritative published base. A candidate later publishing still needs
normal comparison/review and a new accepted receipt; tree equality alone never
promotes source authority.

The helper returns JSON: `current`, `available`, `throttled`, `off`, `busy`, or
`error`. An available notify result has `action: "notify"` and the exact message;
an automatic result has `action: "request_safe_update"` and pinned `upstream_sha`.
The checked Director entrusts that update through its existing bounded execution
route, retaining the same SHA for staging and review. The helper only changes
policy/cache, never contracts, source pointers, receipts, or project state. Cached
results are diagnostic and never reissued as actions within the 24-hour window.

**Automatic** authorizes the safe update protocol below, not arbitrary incoming
instructions or destructive conflict resolution. No repeated routine permission
is needed for compatible reversible updates. Preserve every local adaptation,
back up and compare first, validate schema/state, and record only successful
adoption. Unresolved conflicts, unknown provenance, missing capabilities, migration,
new dependencies, or expanded authority retain the prior revision and require the
appropriate explicit decision. Do not repeatedly attempt the failed update on
every turn; the daily discovery reservation already limits retries. Never run
incoming downloaded helper code as an unattended installer.

The current accountable owner retains scope, compatibility decisions, and
acceptance. The authorized installation agent need not already be a Director;
follow actual host/assignment rules. In an adopted Director installation, an
explicit worker performs the update and the shared Recorder handles routine
state/receipts. Every delegated assignment names worker/director role,
outcome, scope, and authority. Unavailable capabilities remain visible.

## Pin and inspect the incoming revision

Resolve the published repository's `main` to one full commit SHA using the available
Git/API transport. Fetch that exact revision into temporary staging and inspect its
manifest and relevant contract/helper changes before applying them. Recheck the
staged revision matches the pinned SHA; never combine files from changing `main`
URLs. Fetching is not permission to execute downloaded code, migrate data, publish,
or copy repository history into the target. Only the manifest-selected payload
belongs under `.director/`; maintainer docs, tests, and private material do not.

Use this pinned revision's reviewed update guidance to plan the operation, even
when the installed protocol requires an audit on every upgrade or has no update
procedure. Read that installed protocol for local adaptations; adopting revised
upstream guidance never waives project-owned rules or host restrictions. If such
rules conflict, resolve that boundary with the accountable owner.

Identify the actual project root and loaded startup wiring. Read the existing
setup receipt, PROJECT (and any local overlay an older installation uses), configured mode,
canonical tracker, local adapters, and current installed files. Do not infer actual
role, model support, or current worker liveness from a saved receipt.

## Compare before replacing

Before edits, create a unique dated backup under `.director/backups/` of every
managed file and startup file to be changed, with original paths and SHA-256
hashes. Verify backup bytes. Backups stay local through `.director/.gitignore`;
committed history already keeps prior versions. If the installation has no
`.director/.gitignore` yet, add the incoming one first (it is a new managed file),
then write backups. Receipts are committed under `.director/receipts/`.

Preserve the project's version-control choices. An installation whose files are
ignored, under the earlier private default or by deliberate choice, stays ignored:
report that the current default commits them and leave the decision to the user.
Never silently start tracking, untrack, or rewrite history.

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
provenance is a review requirement, never evidence that replacement is safe. Missing
baselines alone do not require a full startup audit or fresh-agent trial.

Preserve project context/overlays, host mappings, custom adapters, additions to
`.director/.gitignore`, state mode, stable
project/request IDs, source bundles and attachments, request history, activity,
decisions, and actual handles. Also preserve the project-owned role index, its role
definitions and overrides, project-wide guardrails, model/host mapping, and the
identity roster, cursor, and current activity. These are project-owned, not
upstream payload; an initialized roster or cursor never overwrites current state.
A project's replacement identity pool is an adaptation, merged like any other.

Policy adoption does not reassign work. Existing open director-owned requests keep
their owner, handles, and obligations until an explicit acknowledged assignment or
handoff changes responsibility. Do not bulk-rewrite owners, spawn managers, or
create a role index full of placeholder entries merely because the package changed.
Select verification from the relevant upstream delta and local drift as described
below. An upstream revision change alone is no reason to refactor working startup
instructions. When startup integration is required, follow [STARTUP](STARTUP.md):
preserve exact specialized instructions at maintained destinations and register
them in the same canonical index before removing global copies. Leave one small
loaded hook and bootstrap with the existing canonical-index pointer, without stale
abstracts, duplicate role tables, or competing role defaults. This includes an
upgrade that needs to repair earlier oversized AGENTS or equivalent files.
A template update changes only generic seeds;
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
decision, never an update; do not edit its config or records to make it open.
Reviewed reversible startup-policy adoption can replace its old role default
without migrating that store; preserve predecessor records and shared authority. Lean and existing trackers retain their
applicable workflow and do not acquire a bundled backend as an update side effect.

## Select the smallest sufficient verification

Routine updates are incremental. Review what changed upstream since the prior
pinned revision, what differs locally, and which behavior or startup route those
changes can affect. State the resulting scope and reason briefly in the existing
receipt; no separate plan, schema, or test matrix is required. Use these triggers:

| Change or finding | Required scope |
|---|---|
| Prose correction or contract clarification with no behavior or startup effect | Check changed files and links, resulting merged bytes, and preservation of adaptations. Reuse still-applicable startup evidence. |
| Helper-only change | Check helper/config/store compatibility and affected behavior in disposable fixtures; use read-only actual-state validation where supported. No fresh startup trial follows solely from a helper change. |
| Changed role behavior without startup restructuring | Check affected definitions, references, index reachability, and preservation; run only the fresh host trials relevant to that behavior. |
| Structural changes to the loaded startup chain, bootstrap routing, role selection/defaults, or inherited instruction placement; or a detected startup defect that requires integration | Run STARTUP's whole-chain audit and integration, then the relevant fresh host trials for affected routes. A change affecting all routes can require the whole trial set. |
| Missing baseline or uncertain provenance | Reconstruct from the prior pinned upstream revision and review local differences, or obtain explicit review before replacement; expand startup/behavior checks only if those findings trigger them. |
| Already-current installation | Confirm the pinned revision and inspect local drift and preservation. Report no upstream change; do not rewrite files or rerun startup/role trials without a relevant finding. |

A tiny prose change that affects a routing rule is a behavior change regardless of
its size. Conversely, unchanged startup instructions need no fresh audit merely
because another file changed. Reuse evidence only where its checked files, local
adaptations, host configuration, and relevant behavior remain applicable; name that
evidence and its limits. Inspect affected callers and links when a path changes.
If a previously unknown startup defect is found, repair/verify it within authorized
scope or report the blocked boundary; do not hide it behind the routine path.

## Validate and record the result

Check selected payload presence and affected local links, resulting merged bytes,
and preserved project-owned context, index pointer, adapters, state, and identities.
Confirm the actual startup path still resolves; focused reachability/preservation
checks suffice when routing is unchanged. Recheck configured mode/canonical state,
Recorder route, roster location, and the version-control check in
[STATE](../STATE.md#version-control) where changed or needed to establish their
preservation. Verify a template remains generic and generated identities separate
when templates are affected. Use read-only actual-state validation where supported
and disposable fixtures for necessary helper behavior checks, never dummy requests
in the real backlog.

When triggered above, use the relevant subset of
[STARTUP's concrete fresh host trials](STARTUP.md#static-checks-then-fresh-host-trials).
Do not claim a cold-session behavioral trial unless one actually ran. Carry forward
known prior verification gaps with their limits; an unrelated pending trial does
not fail a routine update or become passed through evidence reuse. A newly required
check that is blocked or unrun leaves that part incomplete, never passed.

Only after all checks required for this update succeed, write the update receipt
under `.director/receipts/`: source URL/full SHA, prior revision, selected managed
paths and resulting SHA-256 baseline hashes, startup wiring/hash, preserved
adaptations, backup location/hashes, scope and reason, performed checks, reused
evidence and limits, and carried-forward gaps. Update the project's source pointer
to that successful receipt. A no-op report must distinguish reviewed local
adaptations from unreviewed drift; it does not accept unreviewed edits. A partial
or failed update retains the old accepted revision and records the actual mixed
state and next action; it must not advertise complete adoption. Restore only owned
edits from verified backups when safe, preserving intervening changes.

Report what changed, what remained locally adapted, verification and limitations.
Refresh the director's current-conversation installation check after relevant setup
changes; a successful file update alone grants no badge, role, or live supervision
claim.
