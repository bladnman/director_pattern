# Update the flat foundation without replacing the project

Only the manifest-selected foundation/helper files and the marked Director block in
AGENTS.md are managed. Project authority, the `director-project` section, roles,
adapters, state, exact sources and discovery pointers stay project-owned.
The fresh installer refuses existing installations; a compatible update is an actual
reviewed operation below, never rerunning it as an overwrite. A version/schema
change is not permission to migrate an older canonical store.

Published [GitHub main](https://github.com/bladnman/director_pattern) is the upstream
source of truth. This project's Director, or an agent it authorizes within this
project, performs an update in this project's own conversation on an explicit
request or recorded project-scoped standing authorization; when no working Director
exists here, an agent the user directs in this project's own conversation performs
it. Read this whole guide before planning an update. The project Director arranges
a tiny metadata check at its first/next active project-work opportunity, at most once per rolling
24 hours, and defaults to notifying the user. No worker, optional outcome Director, bootstrap,
or global skill starts these checks. This adds no daemon, scheduler, runtime
installation, dependency, or wakeup. Existing project and host permissions still apply.

## Daily discovery and project preference

Keep the first-reply check local and answer greeting-only requests without network.
Arrange due discovery through a supported background route or the next active
project-work step. Until it actually runs, retain the due check in context and at
the next ordinary checkpoint; do not invent execution or a new greeting write.

Use the project's authoritative receipt pointer (fresh default `.director/install.json`) to reconcile acceptance, separately from
the current-conversation installation check and pending behavioral trials under
[OPERATIONS](OPERATIONS.md#installation-evidence).
An accepted baseline with a successful current setup check permits daily discovery
despite an unrelated pending trial. A real unaccepted baseline or required unrun
check keeps its applicable gate; discovery grants no update authorization.

The absent `update-policy.json` means **notify**. With a package change available,
say exactly: **A new Director Pattern is available. Say “update director pattern”
to install it.** Emit it once for that daily result; do not repeat cached notices
on each turn. A failed check is a quiet best-effort result, not a reason to delay
the user's work or retry on every reply. Return errors once to the Director;
explain an actionable persistent gap when relevant without repeating user alerts on
each turn. No check runs while the project is inactive; "daily" means the next active
interaction after 24 hours, not midnight or a background appointment.

When the user says **“always update director pattern”**, preserve that source and
use the existing authorized owner/execution route to save **automatic** for
this project. That utterance is standing update authorization, with no extra
confirmation. "Notify me instead" saves **notify**; "stop checking for updates"
saves **off**. These choices affect only this installation. Neither ordinary
installation nor this feature's adoption enables automatic mode. A later explicit
manual update remains possible with checks off.

The installed base helper [update_check.py](update_check.py) uses an
already available Python 3.10+ on macOS/Linux and its standard library. Run it
through an existing authorized tool-execution route; a separate checking model
is unnecessary. The project Director decides when it is due and can execute the deterministic
command directly. Do not create another checking model or actor.
If the runtime/tool is unavailable, report that gap; do not install software or
promise checks occurred. Lean and custom trackers need no bundled request store.

Supply the project's **exact authoritative receipt pointer**, relative to the project
root (or an absolute path inside `.director/`); never select the newest receipt by
filename, timestamp, or directory order:

```sh
python3 /project/.director/update_check.py --root /project/.director check --receipt .director/receipts/<accepted-receipt>.json
python3 /project/.director/update_check.py --root /project/.director set-policy automatic --authorization 'sources/<user-source>/input.txt: explicit always-update request'
```

Always supply `--root /project/.director` before the command. For notify/off use the same
`set-policy` command and the actual source of that choice. The generated project-scoped `update-policy.json` has schema 1, `mode` (`notify`, `automatic`, or `off`),
`authorization` (user-source reference), and `changed_at` (UTC Unix seconds).
Preserve unknown project fields; reject an unknown schema or malformed policy
for review rather than resetting it. It is project configuration, not a new
request-ledger schema, and is never a completed template seed.

The ignored `.update-check.json` caches schema 1, UTC `last_attempt` (including
failure/interruption), last success/result, and a published-baseline tree identity.
A nonblocking `.update-check.lock` serializes cooperating local chats and preference
writes; atomic replacement prevents partial JSON. Busy callers return quietly. Retain `next_check_at` in the active conversation
so same-day turns skip the helper too; do not spawn a model merely to read the
cache. A new conversation reuses the existing owner/tool route to read it.
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
The Director entrusts that update through its existing bounded execution
route, retaining the same SHA for staging and review. The helper only changes
policy/cache, never contracts, source pointers, receipts, or project state. Cached
results are diagnostic and never reissued as actions within the 24-hour window.

**Automatic** authorizes the safe update protocol below, not arbitrary incoming
instructions or destructive conflict resolution, and not the one-time move to the
AGENTS.md block, which needs the owner's explicit go-ahead. No repeated routine permission
is needed for compatible reversible updates. Preserve every local adaptation,
back up and compare first, validate schema/state, and record only successful
adoption. Unresolved conflicts, unknown provenance, missing capabilities, migration,
new dependencies, or expanded authority retain the prior revision and require the
appropriate explicit decision. Do not repeatedly attempt the failed update on
every turn; the daily discovery reservation already limits retries. Never run
incoming downloaded helper code as an unattended installer.

The current accountable owner retains scope, compatibility decisions and acceptance.
This project's Director, or an agent it authorizes within this project, performs
the update, following its actual host/assignment rules; when no working Director
exists here, an agent the user directs in this project's own conversation performs
it. The Director handles bounded validated records/receipts and delegates
substantial update execution to a bounded worker. Each assignment names role,
outcome, scope and authority. Report unavailable capabilities.

Update each installation from its own project, through that project's Director. Only
that Director knows the project's layout, roles, adaptations, tracker, records and
acceptance gates. To update another project's installation, ask that project's
Director (or the agent the user directs there) to update its Director Pattern in its
own conversation, for example by
starting a session there with "update director pattern", then follow its reports.
Start a session in another project only when the user asked for that update, and
carry the user's request with it. If you cannot start a session in that project,
give the user the 🖐️ action to open it and say "update director pattern", then
follow its reports. Never patch another installation's files from outside, even by
following this protocol. A template or stencil without its own Director is updated
only through its maintainer's reviewed staging route. If no documented staging
route exists, report the gap; do not edit the template.

An ordinary compatible update is bounded, well specified and checked by the
required independent review. It is a case where the
[lighter-tier choice](cards/staffing.md) fits: for its
execution, choose a lighter capability tier at high effort, or the strong tier at
medium effort, and record the choice. Keep the required independent review; by
default it uses the strong tier at high effort. Use the strong tier at high effort or above, with a
recorded reason, for unresolved conflicts, migrations, unknown provenance or
ambiguous project adaptations.

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
then write backups. Receipts live under `.director/receipts/` and follow the project's existing privacy/version-control choice.

Preserve the project's version-control choices. An installation whose files are
ignored, under the earlier private default or by deliberate choice, stays ignored:
keep that privacy choice; a user may separately choose to track reviewed nonprivate files.
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

Preserve enduring project context/overlays, authorized budget/authority policy,
conditional custom adapters, additions to `.director/.gitignore`, state mode,
stable project/request IDs, sources and attachments, request history, activity,
decisions, and actual handles. Preserve the project-owned role index, definitions,
applicable overrides and guardrails, identity roster/cursor, and current activity.
These are project-owned; an initialized roster or cursor never overwrites current
state. A replacement identity pool is an adaptation, merged like any other.

Preservation does not promote old environment mappings into current authority.
When PROJECT or another loaded instruction contains model/provider/version IDs,
agent/team rosters, slot counts, tool/permission/context/inheritance/return-route
observations, or setup results, preserve the original in verified backup/history
and recovery-relevant evidence in the actual receipt/activity record. Remove that
observational category from PROJECT and the loaded operating instructions, rather
than changing the number, dating it, or moving it to a new loaded environment
cache. Keep durable user-authorized constraints, stable responsibility IDs, product
requirements, and canonical locators; do not weaken permission or spending policy.
If a purported restriction's authority is unclear, resolve its provenance with the
owner before weakening it. Record the cleanup and preserved evidence locator in
the update receipt. Retained host-specific adapters must have explicit applicability
and current capability validation before use; historical mappings do not configure
the next host. Resolve runtime controls at their relevant use under [the staffing card](cards/staffing.md).

Policy adoption does not reassign work. Existing open director-owned requests keep
their owner, handles, and obligations until an explicit acknowledged assignment or
handoff changes responsibility. Do not bulk-rewrite owners, spawn managers, or
create a role index full of placeholder entries merely because the package changed.
Select verification from the relevant upstream delta and local drift as described
below. An upstream revision change alone is no reason to refactor working startup
instructions. When startup integration is required, follow [OPERATIONS](OPERATIONS.md#installation-evidence):
preserve exact specialized instructions at maintained destinations and register
them in the same canonical index before removing global copies. Leave one small
loaded hook and bootstrap with the existing canonical-index pointer, without stale
abstracts, duplicate role tables, or competing role defaults. This includes an
upgrade that needs to repair earlier oversized AGENTS or equivalent files.
A template update changes only generic seeds;
never copy a configured store, project identity, runtime state, or a completed setup
receipt into a seed. Generated projects perform their own first-use initialization.

When the incoming startup hook changes, integrate its applicable change into the
existing host-loaded entrypoint as a reviewed project-owned adaptation; replacing
the engine alone cannot update that hook.
Keep the role default, the explicit request for bounded subagents and the marked
block in AGENTS.md, or in the hook source the project's check selects, even when
other rules live in a shared file. When the host loads CLAUDE.md and expands its
imports into loaded text, make CLAUDE.md only import AGENTS.md (for example
`@AGENTS.md`) and move its other content into AGENTS.md; never keep a second copy
of the Director paragraph in CLAUDE.md. Where the host does not expand imports,
keep the role default and the bounded-subagent request in CLAUDE.md and report
that gap.
Back up and verify each startup file the update changes, both AGENTS.md and
CLAUDE.md, compare the identifiable marked block and local adaptations with the
prior and incoming hook, and merge only the needed change. Report, rather than
move, content whose ownership is unclear or that applies to only one host.
Preserve all unrelated bytes and project-specific instructions, including
customizations inside the block. Do not append a duplicate hook. For the standing
Director block, follow "Move to the AGENTS.md block" below: its text is managed, and
a project's own wording moves to the project section instead of being lost. If the block or
applicable authority is ambiguous, retain the original and report the incomplete
integration for review. Verify the actual loaded route and select affected startup
checks below; record the resulting hook and backup in the receipt rather than
treating engine replacement as adoption.

### Move to the AGENTS.md block

From starter revision 3.3 the Director's standing rules are the marked block in
AGENTS.md itself, with a project-owned section directly below it. START.md and
DIRECTOR.md are redirect stubs, detail lives on the cards in `.director/cards/`, and
the check requires the block to name `.director/WORKER.md`. An installation whose
block still says to read `.director/START.md` makes this move once, as part of its
ordinary reviewed update, in this order:

1. Back up and verify AGENTS.md, CLAUDE.md if present, every managed file to be
   changed and the current receipt, as above.
2. Compare and replace the managed payload as above. New managed files:
   `.director/cards/` with `staffing.md`, `requests.md`, `supervision.md`,
   `knowledge.md`, `update-check.md`, `privacy.md` and `badge.md`. START.md and
   DIRECTOR.md become the incoming stubs, and OPERATIONS.md loses its staffing and
   privacy sections to the cards, only after any local addition to those files or
   sections is moved to a project-owned file the project section lists; never drop it.
3. In the hook source (AGENTS.md unless the check selects another file), replace
   everything from the `<!-- director-starter:2 -->` line through the
   `<!-- /director-starter:2 -->` line with the incoming block, byte for byte, from
   the pinned revision's `pattern/starter/agents/block.md`. Keep the block first in
   the file where the project's own layout allows. The block's text is managed: do
   not edit it. Move a project's own wording from inside the old block into the
   project section or the surrounding project text, and report anything whose place
   is unclear. A project using the `director-pattern:start` / `director-pattern:end`
   markers keeps its marker lines around the same incoming text.
4. Directly below the block, add the project section once, starting from
   `pattern/starter/agents/project-section.md`. Fill it from this project's reviewed
   state, not from defaults: its exact check command (existing `--receipt`,
   `--config`, `--backend-contract`, `--guard` and `--hook-source` arguments), the
   guard files to read before the work they govern, the request store's manuals if
   they are not the bundled ones, the role-file locator, and the roster. Where the project already has a
   role index, name that index in the section instead of copying it; never keep two
   role tables. Otherwise write one row per maintained role. Each row's Limits (or the
   index entry) must carry every assignment-affecting guard, because the staffer
   chooses from it; the staffer still reads the selected role file's selection and
   authority part before dispatch. List guard files in two groups: read before the
   first reply, and read before named work. A generated project that still awaits first use also lists
   FIRST_USE.md and its required reads before the first check. When a section already
   exists, never replace it; merge only what the update needs.
5. Measure the result with `context_check.py` against the host's instruction cap
   ([OPERATIONS.md](OPERATIONS.md#optional-context-budget-preflight)). The block must
   stay within 8,000 bytes and the project section within 3,000; a roster that does
   not fit moves to `.director/ROSTER.md`, named in the section. If the whole
   instruction file would pass 24 KiB or the host's cap, report what would be cut and
   let the owner choose; never trim project text silently.
6. Once the file checks above pass, write the update receipt with the new managed baselines (WORKER.md,
   OPERATIONS.md, startup_check.py, each card, the stubs and the other payload files)
   and `director_block_sha256`, the SHA-256 of the block from its opening marker line
   through its closing marker line and newline. Point the project section's check
   command at that receipt with `--receipt`, and use the same receipt for
   `update_check.py`. The check needs this receipt, so it is written before the fresh
   host trials of step 7: record each of those trials in it as pending, and record
   their results when they run. This is the one case where a receipt precedes a
   required check; it must not report the move as adopted until they pass.
7. Run the check command exactly as the project section states it. It must report
   `evidence_matched`, `startup_hook.target` ending in `WORKER.md` and
   `director_block: unchanged`. An edited block, an empty or over-cap project section and
   a changed stub each block the check. This is a structural change to the loaded startup
   chain: the fresh host trials in the table below apply, including a first reply, a
   reply after a forced compaction, and a worker start.

This move is strong-tier work at high effort, with the required independent review;
it is not a lighter-tier case. Automatic update mode never starts it unattended: when
an automatic result would bring this move, tell the owner what it changes and wait
for an explicit go-ahead.

Interrupted between steps 2 and 3, the old block points at a stub and the check
blocks with that gap: finish the move or restore the backup; do not leave it mixed.
An installation that keeps its earlier START.md route by a deliberate reviewed
decision keeps its earlier START.md, DIRECTOR.md and OPERATIONS.md too, and records
that choice in its receipt.

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
| Structural changes to the loaded startup chain, bootstrap routing, role selection/defaults, or inherited instruction placement; or a detected startup defect that requires integration | Trace the actual host-loaded hook through complete selected role/project guards, check missing/truncated reads and applicable authority, then run relevant fresh unassigned/assigned host trials before claiming their behavior. A change affecting all routes can require the whole trial set. |
| Missing baseline or uncertain provenance | Reconstruct from the prior pinned upstream revision and review local differences, or obtain explicit review before replacement; expand startup/behavior checks only if those findings trigger them. |
| Already-current installation | Confirm the pinned revision and inspect local drift and preservation. Report no upstream change; do not rewrite files or rerun startup/role trials without a relevant finding. |

Changing required-reference phases or capability triggers is a startup/behavior
change: audit every reachable affected path, preserve project-owned unphased
requirements, and run the relevant progressive-loading and incomplete-result trials.
Changing a flat foundation does not shorten existing custom definitions' required-reference chains. A reviewed
local rephase must preserve exact authority, applicability, transitive dependencies
and before-use triggers, with old/new mapping in the receipt. Retain prior
acceptance until newly required checks pass.
Separating staffer selection knowledge from executor manuals likewise records the
responsible actor and timing under the staffing card. Keep every assignment-affecting guard in
the selection package; unresolved authority cannot hide in a deferred manual.
Existing unqualified actor and explicit staffer requirements survive engine
replacement until that reviewed mapping is integrated and checked.

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
owner route, preserved identity history, and the version-control check in
[RECORDS](RECORDS.md#persistence-and-interruption-recovery) where changed or needed to establish their
preservation. Verify a template remains generic and generated identities separate
when templates are affected. Use read-only actual-state validation where supported
and disposable fixtures for necessary helper behavior checks, never dummy requests
in the real backlog.

When triggered above, use the relevant subset of
[affected fresh host checks](OPERATIONS.md#installation-evidence).
Do not claim a cold-session behavioral trial unless one actually ran. Carry forward
known prior verification gaps with their limits; an unrelated pending trial does
not fail a routine update or become passed through evidence reuse. A newly required
check that is blocked or unrun leaves that part incomplete, never passed.

Only after all checks required for this update succeed, write the update receipt
(the one exception is the move to the AGENTS.md block, whose receipt is written before
its fresh host trials and records them as pending) under `.director/receipts/`: source URL/full SHA, prior revision, selected managed
paths and resulting SHA-256 baseline hashes, startup wiring/hash, preserved
adaptations, backup location/hashes, scope and reason, performed checks, reused
evidence and limits, and carried-forward gaps. Update the project's source pointer
to that successful receipt. A no-op report must distinguish reviewed local
adaptations from unreviewed drift; it does not accept unreviewed edits. A partial
or failed update retains the old accepted revision and records the actual mixed
state and next action; it must not advertise complete adoption. Restore only owned
edits from verified backups when safe, preserving intervening changes.

Record the incoming manifest's `starter_revision` in the update receipt, and name
the previous and new `starter_revision` when reporting the update to the user. When
the installed receipt has none, report the previous one as "unrecorded".
Report what changed, what remained locally adapted, verification and limitations.
Refresh the director's current-conversation installation check after relevant setup
changes; a successful file update alone grants no badge, role, or live supervision
claim.

## Provenance and operational check result

Fresh `install.json` records exact managed hashes and a technical file-check result,
not human/host acceptance. Installation from a canonical Git checkout records its
full HEAD, pattern tree, tracked local delta and known published base when locally
verifiable; it needs no install-time network. A transported source can carry a
verified receipt with exact payload hashes. Never label unknown/unpublished input
as accepted publication. The exact published base and adapted/candidate payload
are separate, even if their trees later become equal.

If no known published base exists, retain the provenance gap. At the next authorized
update or active project-work opportunity, resolve an exact canonical upstream pin,
compare installed payload/provenance to that revision, and record the reviewed
published baseline through the normal recording route, separately from local deltas.
Then run discovery subject to its existing daily window. Do not reinstall, reset
the cache or promote acceptance to satisfy the checker. If transport
or comparison is unavailable, retain a visible pending provenance/check gap with
the actual failure and next opportunity. Do not retry each turn or hide a permanent
no-check state. Explicit notify/automatic/off preferences remain honored, including
offline handling and manual update requests while checks are off.

An `available` automatic result is a real pending safe-update operation, not proof
of application. Execute only when the current host can perform the scoped protocol;
otherwise retain the pinned pending operation/reason and inform the user of the
meaningful limitation. No invented backend, daemon or unattended downloaded code.

END UPDATES.md
