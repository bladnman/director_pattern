# State, capture, and recovery

Tracked is the default for new installations; lean is an explicit option without
a complete-backlog promise. Keep an existing tracker canonical. State mode does
not depend on project type, organization size, or staffing. An existing tracker
must map the same intent/ownership/acceptance contract with its actual guarantees.

A Small recorder owns **all routine state reading and writing** in either mode,
through one coordinated [Recorder](RECORDER.md) route named in PROJECT. Harder
reconciliation may warrant more capability under [MODELS.md](MODELS.md). Judgment is
owner-relative: a Request Manager plans, evaluates, and reworks its bounded outcome;
the project Director decides cross-outcome scope and priority, authorization, and
final acceptance. The recorder applies supplied facts and returns exact IDs, paths,
revisions, and applied-update receipts. Ambiguous scope, authorization, priority,
acceptance, and cancellation return to the responsible owner. Workers report to
their manager rather than writing canonical state or launching competing recorders.
If unavailable, disclose unsupported persistence and continue director conversation;
do not silently turn a director into a direct-helper worker.

Keep two depths of state. The Director's working commitments stay compact: each
unfinished outcome or thought, its owner, current question or approach, next
decision, and resume point. Each Request Manager's outcome record carries the full
source and obligations, approach and decisions, assignments and handles, evidence,
gates and review, and next actions. Full recoverable detail stays available to the
Director; a compact view is an attention boundary, not permission to discard it.
The manager owns active detailed coordination. Durable owner identity and a
replaceable execution attempt are different things. The shared identity roster and cursor
([IDENTITIES.md](IDENTITIES.md)) live in current activity, serialized through the
same Recorder route. Not every passing thought needs a durable write.

For the project Director's conversation, the recorder checks installed wiring,
required files, and project mode/configuration under the [identity check](DIRECTION.md#check-installation-before-using-director-identity).
It returns factual evidence through the existing setup receipt/PROJECT context;
the Director resolves its role and judges whether the `🎬` identity is warranted.
Lean and existing trackers need no bundled backend for this check. If evidence or
the recorder is unavailable, report that limitation without claiming verification.
The receipt is setup evidence, not behavioral acceptance or worker liveness.

## Bundled tracked store

For a new store, initialize the bundled request-folder format through the helper.
It assigns a stable project identity and distinguishes the new store/record schema
from legacy JSON files. Never silently convert an existing store. See the
[record contract](references/RECORDS.md) and [recorder CLI](references/TOOLING.md).

Each independently finishable outcome has a stable request ID and one canonical
request folder. Its request.md carries machine metadata and a readable record;
request-local assets/evidence travel with it. Seven states map to three containers:
inbox/queued in pending, active/review/blocked in working, done/canceled in archive.
IDs resolve current paths; old paths are locator hints, not permanent identity.
Shared originals and large product/media outputs remain canonical elsewhere through
stable references. Request bundles are physically flat, regardless of their links.

Capture applies to requests that start work; one the Director answers in its reply
needs none. Capture the complete exact user message once as an immutable source
bundle, keeping
source metadata/derived mappings separate from raw UTF-8 text. Snapshot available
attachment bytes and hashes; record unavailable material explicitly. Give the
recorder exact text or a source path, never a reconstructed summary. Link separate
outcomes to the shared source. Later steering, including tiny corrections, is a
new immutable source linked as an addendum; preserve original scope/history.
Capture scope-setting or decision-making messages, and acknowledge their receipts,
before dispatching work that depends on them; then reconcile live assignments and
use the lifecycle's amendment/replanning rules. Routine steering, receipts, and
outcomes may be recorded together in one short batch at a natural checkpoint, such
as the end of a task. Keep records small and fast. Prefer a fresh Small recorder
with short, exact instructions over resuming a long-lived recorder whose context
keeps growing. Only timing and size relax; capture stays exact and immutable.
A captured idea is not execution authority.

## Relationships and acceptance

Source/provenance, grouping, information, required dependencies, and ownership
handoffs have different meanings. Common source and grouping never imply a blocking
edge. Director-derived required edges need no separate permission within authorized
scope. The helper checks supported local required dependencies and cycles; the
director still judges substantive success, human gates, and required integration.
Failure/cancellation is not successful fulfillment. Removing a requirement needs
an explicit scoped decision, retained history, and re-evaluation of affected scope.

An acknowledged external owner owns its own requests and execution. Retain the
source's waiting commitment, agreed outcome/acceptance, acknowledgment, and dated
observations without mirroring remote internals. Identity is project ID + request ID;
a root/path and return route help resolution. Supplied remote evidence is not an
authenticated status feed. No automatic foreign reads, transport, or refresh occurs.
Source state cannot stop remote execution. Receiver completion awaits source
acceptance; independent completed outcomes remain complete while another waits.

## Recovery is explicit

Recorder-maintained activity/decision pointers in both modes retain actual handles,
write owners, identity bindings, last observations, results, pending evaluation,
review/rework ownership, and next actions.
They are not a second lifecycle authority or proof of liveness. The helper never
starts workers, sends messages, schedules a wakeup, or authenticates supplied proof.

The helper uses one cooperating writer, revisions, event identities, and a recovery
journal for record replacement and relocation. Multi-file work is not atomic.
Read-only inspection reports pending recovery instead of silently mutating it; the
recorder runs recover or a subsequent mutation resolves intent before continuing. Query actual host handles and assign
worker inspection of partial outputs before overlapping restarts. Preserve old
attempts and uncertainty; do not infer termination from age. Claim saved state only
after a receipt. Files preserve continuity but cannot keep an agent running.

## Version control

The installation is committed with the project by default: contracts, PROJECT,
config, requests, sources, current activity, decisions, and receipts. Another
machine or a cloud checkout then continues the same work. `.director/.gitignore`
keeps only the helper lock, in-progress write scratch, and pre-update backups
local. One machine writes state at a time: commit and push before continuing
elsewhere, and pull before the next write
([RECORDS](references/RECORDS.md#persistence-and-interruption-recovery)).
Committed files use project-relative paths.

A project may keep more local by adding paths to `.director/.gitignore`; updates
preserve that choice. Ignore `requests/` and `sources/` together: reading a
request verifies its linked sources, so committed requests with ignored sources
cannot be read on another machine. A local store cannot be continued from another
machine or a cloud checkout. Ignoring a path does not remove what is already
committed or pushed; report that history to the user rather than rewriting it.

In a Git repository, `git check-ignore` should show the lock and `backups/` as
ignored and the rest of the installation as not ignored, apart from paths the
project chose to keep local. Report a parent or global rule that ignores
`.director/` instead of editing it; it may be deliberate.
