# Request bundles and their writer

This is the bundled tracked-store contract. Existing canonical trackers remain
valid adapters, with their own verified guarantees; do not create a second ledger
or claim this helper's safeguards for another backend. Routine state I/O belongs
to the Small recorder. The director supplies interpretation and explicit decisions.
Use [TOOLING.md](TOOLING.md) for the actual CLI and event payloads.

## Identity, source, and local material

Initialize a new store before writing. The config separates its configuration
schema from request-store schema/format and stable project identity. Legacy stable
JSON stores are a different format; the helper does not silently convert them.
Project ID + request ID identifies an outcome. A current path is a locator hint;
use the helper's resolver after relocation rather than preserving stale paths.

Every independently finishable outcome has its own request folder with canonical
`request.md`, request-local `assets/`, and generated `evidence/` as needed. Its
machine-readable metadata and readable body must agree; use the recorder/helper,
not hand-edits to competing metadata. A location change moves the whole request
folder, preserving its local material. Shared originals and large product/media
outputs remain at canonical locations through references, not silent duplication.

Capture one complete exact user message as a source bundle, with immutable raw
UTF-8 text distinct from its metadata. Save available original attachment bytes
with identities/hashes; retain missing-file conditions explicitly. A caption or
chat reference is not saved attachment bytes. The recorder receives exact text
or a source file; it never reconstructs verbatim wording from an interpretation.

Create separate actionable requests linked to that source. Do not turn the source
message into an executing parent. Compare the extracted outcomes with the whole
source so no independent instruction vanishes. Director-authored scope, constraints,
acceptance, and worker instructions are visibly separate from the user's words.
Use an optional umbrella only for a useful whole-scope commitment, not every message.

Later steering is a new immutable source linked as an addendum, including tiny
corrections. Preserve originals and old decisions. Capture scope-setting steering
first, reconcile live assignments, then amend/replan through allowed lifecycle
operations. Obtain and acknowledge the receipts that dependent work needs before
dispatch; routine records may batch at a checkpoint ([STATE](../STATE.md)). Captured or
queued work is not itself execution authority.

## Seven states, three locations

| State | Container | Meaning/evidence |
|---|---|---|
| inbox | pending | Source captured; interpretation/authorization may remain open. |
| queued | pending | Director planned bounded scope, owner, acceptance, and human gate. |
| active | working | Factual local/external execution receipt recorded; current liveness remains separate. |
| review | working | A worker submitted result/evidence; director evaluation is owed. |
| blocked | working | Named unmet condition; retain owner and exact next action. |
| done | archive | Director accepted scope and required human gates/dependencies. |
| canceled | archive | Explicit non-success ending decision and reason; preserve history. |

Lifecycle and container must agree. Rework returns review to queued. Recovery can
requeue remaining scope with a fresh execution attempt; reopening preserves earlier
acceptance/history and needs new evaluation. Changing state cannot stop a worker
or revoke writes. Never archive unfinished work as done to tidy the queue.

Required human acceptance is decided before execution. The helper checks supplied
event declarations; it cannot authenticate the person or truth behind them.
Technical verification, rendered/native behavior, user/creator acceptance, deployment,
and public release are distinct claims. Worker completion is a submission.

## Outcome ownership in the record

Config schema 1 and request-store schema 2 already carry complete-outcome
management; no helper command, status, or schema change exists for named roles,
models, identities, or manager phases. Map them onto existing validated fields:

| Existing field or event | Use for a managed outcome |
|---|---|
| `owner` set by `plan` | Stable accountable Request Manager identity for the whole outcome, not each specialty or transient attempt. |
| `acceptance` list | All known completion obligations and criteria, including release verification and follow-up. The evolving detailed approach belongs in manager artifacts/activity. |
| `dispatch` and `execution_receipt` | The manager's actual execution handle and host receipt. Extra receipt keys carry selected role/reference package, requested and actual model/effort, and identity; acknowledgment only when actually received. |
| `note` events and current activity | Specialist assignments and handles, read acknowledgments, evaluations and rework, partial results, observed status, obligations/resume pointers, and the identity roster/cursor. |
| `submit` → review | Integrated manager submission to the Director. Worker-level evaluation does not submit the whole outcome; manager responsibility persists while its attempt waits. |
| `accept` event `director`; stored `director_acceptance.director` | The project Director's final decision and identity. A manager does not close its own outcome; Director rework stays with the same manager and outcome. |

Unknown top-level event keys are rejected, and canonical fields are reconstructed
by replay with exact equality. Do not bolt manager metadata into request.md or
invent JSON keys. Keep one outcome identity: distinguish its owner, its execution
attempts, and its internal assignments without duplicating the request tree.
Steering an active or reviewed outcome uses the existing replanning transitions in
[TOOLING](TOOLING.md#steer-an-active-or-reviewed-outcome).

## Typed relationships, independent ownership

Source provenance, grouping/decomposition, information links, required dependencies,
and ownership handoffs have different meanings. Grouping/shared source does not
imply a blocking edge. Parent/child is optional decomposition language, not a fixed
topology. Physically flat bundles can be linked in several arrangements.

A director records required edges as needed within authorized scope, without asking
permission for every link. Supported local required dependencies must resolve and
must not introduce blocking cycles. Informational backreferences may be reciprocal.
Successful acceptance requires required outcomes, not merely terminal child states;
a canceled/failed prerequisite is not success. Director judgment still decides
substantive fulfillment, acceptance evidence, and required integration/human gates.
Removing a requirement is an explicit scope decision with history and re-evaluation,
not fabricated successful completion of the removed work.

External links identify project/request and locator/return route. An attempted
send is not an acknowledged handoff, and acknowledgment is not proof of execution.
After real acknowledgment, the receiver owns supervision of its execution and
local requests. The source keeps its commitment/acceptance and agreed outcome
reference, not a copy of the receiver's task tree. Each request has one canonical
owning project; a link alone grants no authority or record ownership transfer.

Retain exact relevant source/attachment references and agreed constraints/acceptance.
Transfer accessible content through an authorized route when pointers cannot be
used, recording missing material. The helper records supplied receipts/observations;
it performs no foreign reads, network transport, refresh, or authenticated proof.
The first three independent outcomes can remain done while a fourth waits on an
external owner. Dated observations survive restart; current liveness can be unknown.
Source acceptance resumes on return or the next authorized session, without a wakeup
promise. Source cancellation alone cannot stop receiver execution.

## Persistence and interruption recovery

One cooperating writer owns shared state. Mutations use event identities, expected
revisions, preserved history, and canonical record replacement. Identical retries
are safe under the documented event rules; stale or conflicting updates fail.
Do not guess whether a failed call wrote: inspect its receipt, current revision,
and pending recovery before retrying. Preserve conflicting copies for reconciliation.

Moving a request plus updating related files is not a multi-file atomic operation.
A journal retains pending intent so an interrupted relocation/write can be resolved
explicitly. Read-only commands report recovery required instead of silently writing.
The recorder runs recover (or the next mutation resolves intent), inspects resulting
paths/records, and obtains receipts
before further mutations. Do not use raw `mv` as a substitute for that process.

Same-machine advisory locks and atomic per-file replacement do not provide safe
multi-machine/cloud transactions, authentication, or tamper-proof audit. Keep one
canonical store across worktrees. Validation checks stored invariants and supported
relationship consistency; it does not prove that real-world evidence is true.

On restart, the recorder retrieves relevant open outcomes, sources, actual dispatch
and handoff receipts, latest dated observations, results, and pending decisions.
The director queries real host handles through authorized tools and assigns worker
inspection of partial outputs. Unknown/old status is not termination; settle write
ownership before overlapping replacement work. A file/status change starts no agent.

Both tracked and lean retain compact activity and important decisions through the
recorder. These are recovery pointers, not another lifecycle authority or a live
watcher. The helper launches no agents, sends no messages, and schedules no wakeup.
