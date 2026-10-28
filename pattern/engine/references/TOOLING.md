# Recorder CLI

The bundled helper uses Python 3.10+ and the standard library on macOS/Linux
(`fcntl` advisory locks are required). All routine state reads/writes below belong
to the Small recorder. It applies director decisions and returns IDs, revisions,
paths/update receipts. It launches no workers, sends no messages, and authenticates
neither supplied evidence nor remote status. Use one canonical store.

## Initialize and capture

The stable `.director/tools/requests.py` launcher explicitly passes `.director/`
as the store root to `engine/tools/requests.py`. Direct engine invocation derives
the same root, never `engine/`. The historical `--team ROOT` option overrides that root and must
precede the subcommand; it creates no team. Commands below use an illustrative
`/project/.director`; substitute the actual root. Files containing text use UTF-8.

Every `--event-id` and event-file `event_id` ends in `-<32 lowercase hex>`. Run
`event-id <kind>` once per new operation; it prints a fresh ID such as
`capture-<32 hex>`. Keep that ID for any retry of the same operation. The CLI
rejects counter-style IDs such as `request-1`: a counter restarts on every machine,
and when the store travels through Git, two machines would give two different
outcomes one ID.

```sh
python3 /project/.director/tools/requests.py init
python3 /project/.director/tools/requests.py event-id capture
python3 /project/.director/tools/requests.py capture --raw-file /path/to/exact-message.txt --event-id <capture-ID> --attachment /path/to/original.png
python3 /project/.director/tools/requests.py create --source-id <returned-UR-ID> --title "Director-written outcome" --event-id <request-ID>
python3 /project/.director/tools/requests.py create --source-id <same-UR-ID> --title "Independent second outcome" --event-id <another-request-ID>
python3 /project/.director/tools/requests.py show <returned-REQ-ID>
python3 /project/.director/tools/requests.py list --open
python3 /project/.director/tools/requests.py validate
```

`init` preserves config extras and adds `request_store` with schema version 2,
format `director-request-bundles`, and a stable `PROJ-<32 lowercase hex>` project ID. Config's
own schema remains 1 and mode is tracked. Repeat init retains the identity; optional
`--project-id PROJ-…` explicitly selects an identity for an empty new store. Legacy
flat JSON or an unrecognized populated store is rejected without conversion.

`capture` returns a stable `UR-<32 hex>` ID. It saves exact text as
`sources/<UR>/input.txt`, metadata/hashes as source.json, and supplied original bytes
under attachments/. Repeat `--attachment FILE` for several files; duplicate original
filenames in one source fail rather than overwrite. Missing attachment bytes need
an explicit director/recorder note; the helper cannot fetch a chat attachment.
`source <UR-ID>` verifies/returns metadata; inspect the canonical input.txt for exact
words. Do not edit either raw source or metadata in place.

`create` returns a stable `REQ-<32 hex>` ID, revision 1, inbox. Use the same source
ID for several independent outcomes. Alternatively `create --raw-file FILE` instead
of `--source-id` captures a source as a convenience; use explicit capture to share
one source or include attachments. Capture/create IDs derive from project identity
and event ID, so retries do not create extra outcomes. Reuse an event ID only for
the same operation/payload; every new operation gets a new ID from `event-id`.
Record each returned receipt before dependent updates.

## Files, revisions, and lifecycle events

Folders are `requests/{pending,working,archive}/<REQ-ID>/request.md`. Source/project
IDs stay stable when requests move. `show` resolves an ID and returns its record;
the Python API `Store(ROOT).path(REQ_ID)` returns its current request.md path.
Do not cache old paths as identity. Never hand-edit the JSON block or derived body.

To snapshot request-local material, use the command rather than a hand-built event:

```sh
python3 /project/.director/tools/requests.py attach <REQ-ID> --file /path/to/research.txt --kind assets --event-id <asset-ID> --expect-revision <current-revision>
python3 /project/.director/tools/requests.py attach <REQ-ID> --file /path/to/checks.txt --kind evidence --event-id <evidence-ID> --expect-revision <current-revision>
```

The copied file gets an event-derived filename, original-name/byte-count/SHA-256
receipt, and new record revision; it travels with the request. Use references for
large canonical outputs. Original user attachments belong to immutable sources;
later originals require a new captured source, not mutation of an old one.

Write director-supplied events as JSON files, then:

```sh
python3 /project/.director/tools/requests.py apply <REQ-ID> --event-file /path/to/event.json --expect-revision <current-revision>
```

Every event has `event_id` (from `event-id`) and `type`. Additional literal keys are below. Unknown
keys fail. Strings must be nonempty; evidence/acceptance lists must be nonempty
where required. All supplied facts/evidence still require director judgment.

| Type | Allowed source state → new state | Other payload |
|---|---|---|
| plan | inbox/queued → queued | owner, acceptance: string list, human_gate: {"required":true/false} |
| dispatch | queued → active | receipt: object with kind agent/direct and id; optional host details |
| submit | active → review | evidence: string list; optional artifacts: string list |
| accept | review → done | director, evidence; required human-gate proof below |
| block | queued/active/review → blocked | reason |
| resume | blocked → queued | reason |
| requeue | active/blocked → queued | reason |
| revise | review → queued | reason |
| reopen | done/canceled → queued | reason |
| cancel | any open → canceled | reason |
| amend | inbox/queued/blocked → unchanged | source_id of newly captured steering; raw_text convenience also captures a new source |
| note | any → unchanged | text; optional evidence/artifacts string lists |

Dispatch only records factual worker execution; it never starts execution. A
source resuming evaluation can bind an already-real external execution/return
receipt as described below, without pretending to launch a new worker. `direct`
is a schema option for worker execution, not permission for a director role switch.
Amend appends source provenance and clears acceptance/execution; replan before new
dispatch. Capture active/review steering first, reconcile workers, then requeue/revise
before amend ([steering flow](#steer-an-active-or-reviewed-outcome)). Done/canceled
needs reopen; blocked needs resume before planning.

For a minimal no-human-gate lifecycle, save these as four separate event files.
They are synthetic fixture inputs in a disposable test, never real execution proof;
their fixed event IDs are fixture literals, and real events take fresh IDs:

```json
{"event_id":"plan-203fd3c1415f401d851bc6ee9575cdcb","type":"plan","owner":"worker-1","acceptance":["Agreed outcome met"],"human_gate":{"required":false}}
```
```json
{"event_id":"dispatch-2d3a0a4113b04b04b0ea518d24ee64ac","type":"dispatch","receipt":{"kind":"agent","id":"fixture-worker-1"}}
```
```json
{"event_id":"submit-e1780413fbb242fd817585d34a9d1bae","type":"submit","evidence":["Fixture result"]}
```
```json
{"event_id":"accept-a001b19efcce4f73a843eb60c32b23ec","type":"accept","director":"director","evidence":["Fixture result evaluated against scope"]}
```

For real work replace fixture inputs with actual receipts/evidence. A planned human
gate needs `"human_gate":{"status":"passed","evidence":["Actual acceptance reference"]}`
on accept; omit human_gate when not planned. It cannot be waived at completion.

A real dispatch receipt may carry extra host-detail keys, which are preserved. Use
them for facts actually observed at dispatch, for example:

```json
{"event_id":"dispatch-e6f9261d35334496834f7c4537539053","type":"dispatch","receipt":{"kind":"agent","id":"<actual handle>","responsibility":"request-manager","identity":"🐙 Contract","requested":"Large/high","selected":"<actual model/effort or unknown>"}}
```

Record a later acknowledgment, specialist assignment, or evaluation as a `note`.
The helper has no role, model, identity, or activity command; those stay in
receipts, notes, and recorder-maintained current activity.

### Steer an active or reviewed outcome

`amend` is limited to inbox/queued/blocked, and `requeue`/`revise`/`resume` clear
the current execution receipt; event history keeps the old one. Active/review
in-place amendment is not supported. Steer through the existing legal flow:

1. Capture the exact addendum as a new source and reconcile it with the existing
   manager and affected work at a supported boundary.
2. Retain the stable manager identity, actual existing handle, last live observation,
   partial results, and incorporation state in activity/evidence before changing
   the record. Message delivery alone is not incorporation.
3. Apply `requeue` for an active request or `revise` for a review request. These
   are replanning transitions, not host process stop/restart commands.
4. While queued, apply `amend` with the new source_id, then `plan` the **same
   manager owner** with the full revised acceptance obligations and human_gate.
5. Apply `dispatch` binding the **same actually observed manager handle**. This
   records existing execution; it does not spawn another manager or worker.

When waiting on incorporation is genuinely the outcome's state, `block` → `amend` →
`resume` → `plan` → factual `dispatch` of that same handle also works. If the handle
is uncertain, inspect, wait, or settle ownership first. A returned manager that
needs resumption uses an actually supported host continuation; record its observed
attempt and handle. Durable responsibility does not prove an active attempt.

## Typed links and external outcome records

`target` is `{project_id,request_id,locator?}`; locator is a path/route hint.
Local bundled IDs keep their strict format. External project/request identities
are opaque tokens up to 256 characters, without control characters or slashes. The source project owns its record; a link grants no foreign
access or ownership. All mutations below use apply and current revision.

| Type | Additional payload and meaning |
|---|---|
| link | link_id, kind: group/decomposes/related/depends_on, target |
| unlink | link_id, director, reason; retains removal decision/history |
| review_dependency | link_id, director, evidence; only external depends_on |
| observe | exactly one link_id or handoff_id, status, evidence, observed_at |

Link/unlink/review_dependency require open records; observe can record history in
any state. Local link targets must exist. Only depends_on blocks acceptance; local
required cycles fail and required local targets must be done, not canceled.
External depends_on requires explicit director-reviewed evidence, not a status
observation. Informational/grouping links do not gate closure. Observations retain
the supplied time and always leave current liveness unknown. Unlink is an explicit
scope decision; it does not make the removed outcome successful.

Handoffs record an external outcome contract without copying the receiver's tree:

| Type | Additional payload |
|---|---|
| handoff_propose | handoff_id, target, outcome, required: boolean, return_route, constraints, content, acceptance: string list |
| handoff_request | handoff_id, receipt of actual permitted send/request |
| handoff_acknowledge | handoff_id, receipt, owner; target required when proposal omitted request_id |
| handoff_return | handoff_id, receipt, evidence |
| handoff_accept | handoff_id, director, evidence |
| handoff_waive | handoff_id, director, reason; revised_acceptance string list required for required handoff |

A handoff proposal may name only the receiving project in target; acknowledgment
must bind its actual request_id if not already known. It cannot change a known
project/request identity. Ordinary links always require complete target identity.
Propose is allowed in queued/active/blocked; other handoff events require open
records. Proposed → requested → acknowledged → returned → accepted are distinct.
A required acknowledgment puts the local request in blocked/waiting. Return alone
does not satisfy acceptance. After evaluating/accepting the external result, resume
and perform the appropriate local dispatch/submit/accept lifecycle to finish the
source commitment. Waiving a required handoff requires revised_acceptance different
from current criteria, records old/new scope, and resets to queued with execution
and human proof cleared. It never claims the original deliverable succeeded;
complete the revised lifecycle or cancel the unmet original scope explicitly.
Optional waivers omit revised_acceptance.
The helper does not send the request, authenticate acknowledgments, query foreign
stores, or transfer authority. Real authorization and evidence remain host/director duties.

### Finish a waiting source commitment

Record `handoff_return` with the actual remote return receipt/evidence; it stays
a submission, not source acceptance. After evaluating it, record `handoff_accept`
with the source director's decision. This does not itself mark the local request done.
For a source still blocked, apply `resume` with the return/evaluation reason, then
`dispatch` binding the **already-real external execution/return receipt** (kind agent,
its actual ID), then `submit` with returned/integrated evidence to enter review.
The dispatch event records that execution; it neither launches a source worker
nor claims the remote work restarted. Never invent a new run to satisfy the schema.
If factual execution/return evidence is missing, retain the gap instead.
Finally apply local `accept` only after the agreed scope, required links/handoffs,
and human gates are satisfied. Use each returned revision for the next event.

## Recover and verify honestly

Read-only source/show/list/validate refuse a pending `.request-txn` instead of
silently repairing it. Have the recorder run `recover`; a subsequent mutation also
resolves pending intent under its lock before proceeding. Recovery validates expected
content and preserves conflicting/uncertain copies by failing rather than overwriting.
Unpublished staging and retired cleanup leftovers are not a promise of automatic cleanup.

Identical event retries with identical normalized payloads are no-ops even with a
stale revision; conflicting reuse or new events against stale revisions fail.
Mutations serialize cooperating writers with `.requests.lock`. Atomic per-file
replacement plus a journal makes relocation recoverable, not a multi-file or
cross-machine transaction. Never raw-move a bundle to simulate a lifecycle event.
The lock and journal are machine-local and ignored by Git. When the store travels
through Git, one machine writes at a time; see
[RECORDS](RECORDS.md#persistence-and-interruption-recovery).

Validate checks source/file hashes, record/body consistency, history replay,
directory/state/identity, and supported local links/cycles. It cannot prove evidence
truth, human identity, live execution, or remote outcome completeness. Inspect actual
host handles and partial artifacts before replacement work; state changes stop no
agent. Neither files nor this helper provide continuous supervision or a wakeup.


## Daily update discovery is separate from request storage

The base-payload [update_check.py](../tools/update_check.py) implements the
[UPDATES daily check](UPDATES.md#daily-discovery-and-project-preference). It needs
no request store/config, so lean and existing trackers use the same discovery.
Only the checked project Director arranges checks through the existing authorized
execution route; no worker/Recorder startup invokes it automatically. It returns
data and never updates contracts or request records. Runtime availability,
metadata endpoints, policy commands, receipt schema, daily failure throttle,
concurrency limits, and safe automatic-update handling are specified in UPDATES.
