# Starter 2 local API — action reference

Use `python3 .director/state.py ACTION --data-file FILE` or `--data-file -` for JSON
stdin. `python3 .director/state.py help` prints this reference without reading state.
No dependency install, shell wrapper, Recorder or role catalog is needed.
Success prints JSON; failure prints `error` and exits 2. Mutations require a unique
`op_id` and current global `expected_revision`. Retry the identical payload after
an uncertain outcome: the same op returns its saved receipt; changed payload with
that op conflicts. Capture pins source/attachment bytes once and includes their
digests in retry identity: changed external file bytes conflict even with the same
JSON paths, and the bytes fingerprinted are the bytes persisted. Read `status` if another operation won, then deliberately replan.
There is one nonblocking local writer lock; `store busy` is retryable. Roles/owners
are supplied facts from trusted callers, not authenticated permissions.

All read actions accept `limit` (default 5), `max_bytes` (default 12000), `offset`
and optional `at_revision` from the prior page. Complete all relevant pages using
`next_offset`; `omitted` never claims an unread page was loaded. Too-small budgets
fail visibly instead of truncating an instruction. `review-batch` starts at the
review cursor and forbids nonzero offsets: save one contiguous batch, then fetch
the next. Readonly calls do not advance revisions/cursors. Internal store parsing
is proportional to state-file size; no model-history loading is implied.

`proposals {}` pages undecided proposals with full claim/scope/basis and review IDs;
`proposal_id` selects one, `include_decided:true` includes retained decisions.
`reviews {}` pages saved summary/reviewer/spend/batch/proposal IDs; `review_id` selects
one. `incidents {"review_id":"V-returned-id"}` pages its exact supporting evidence,
including already-reviewed incidents. `deferrals {}` pages saved deferral reasons.
These task/recovery queries let a fresh owner discover durable outputs without
reading state.json or loading full history.

`selectors {}` pages only current knowledge IDs and exact task/path/audience scopes,
never claims/history; optional `path` discovers overlapping ancestor OR descendant
paths by segments (`.` means projectwide discovery). Siblings do not overlap.
Use it at task time when canonical vocabulary is not retained or supplied. Map
natural requests (for example presentations) to relevant existing tags (for example
customer-deck), then `select` those exact tags and pass them to workers. A guessed
exact-string miss is not proof that no semantically applicable rule exists. After
discovery query `select` for actual affected file(s); discovery does not broaden a
rule's execution applicability.

`status {}` returns bounded current unfinished requests and counts, review policy,
pending and due. `pending {}` returns bounded incident identities/scopes, not their
full history. `request {"request_id":"deck"}` explicitly pages that request's
history for task/recovery work. Neither startup nor simple discussion needs it.
`select {"task":"customer-deck","path":"slides/demo","audience":"customer"}`
returns only current accepted knowledge matching all three dimensions, with exact
scope/provenance. `*` is an explicitly approved wildcard; path prefixes match
segments. Training does not match customer-deck/customer unless explicitly scoped.

Create a request and preserve exact UTF-8 source (no newline rewriting):

```json
{"op_id":"capture-1","expected_revision":0,"text":"Make the customer deck.\n","request":{"id":"deck","summary":"Customer deck","scope":{"tasks":["customer-deck"],"paths":["slides"],"audiences":["customer"]},"acceptance":"Owner evaluates usable slides","owner":"Director"}}
```

`capture` accepts exactly `text` OR `source_file` (UTF-8 bytes), optional
`attachments:[{"path":"...","name":"..."}]`, and either a new `request` above or
`request_id` + `expected_request_revision` to add immutable steering. Receipt gives
`source_id`, request/global revisions. Attachments are copied and hashed. Capture validates all fields/revisions before file writes. It
creates durable source files before committing state: an interrupted valid attempt
can leave an unreferenced immutable source directory; an identical retry reuses it.
It never silently rewrites referenced sources. Retain orphan evidence for inspection.

Update with source/revision awareness (`changes` is optional for observations):

```json
{"op_id":"observe-1","expected_revision":1,"request_id":"deck","expected_request_revision":1,"source_id":"S-from-capture","changes":{"handles":["actual-host-handle"],"next_action":"Evaluate return"},"observation":{"handle":"actual-host-handle","status":"returned","observed_at":"2026-10-30T12:00:00Z","evidence":"slides/demo rendered"}}
```

`update`, `observe`, `evaluate` share this shape. Changes allow scope, acceptance,
owner, status (`active`, `review`, `blocked`, `accepted`, `canceled`), next_action,
handles and pending_approvals. `evaluation` may add a bounded judgment string.
Each operation retains its source/changes/evaluation in request history and bumps
the request revision. An observation needs all four shown fields. Actual receipt
data is not liveness or authenticated proof; the caller owns evaluation/approval.
Setting `status:accepted` requires the `evaluate` action, a nonempty evaluation
and no unresolved pending_approvals; ordinary update cannot bypass these checks.

Attach a meaningful `incident` object to the ordinary observation/evaluation above,
or call `incident` with `{op_id,expected_revision,incident:...}`:

```json
{"source_id":"S-from-capture","request_id":"deck","request_revision":1,"scope":{"tasks":["customer-deck"],"paths":["slides"],"audiences":["customer"]},"evidence":"Customer review found dense slides","correction":"Consider sparse participant-facing slides","hypothesis":true}
```

Incident records are immutable, sequenced, capped at 6000 encoded bytes; evidence/
correction strings at 2000 each. Link larger evidence rather than loading it all.
Sources must belong to the request; recorded request revisions must exist.
Receipts expose review_pending/count/due and the policy. Default threshold three
is a spend-batching policy, not a rule detector. At meaningful closure the owner
dispatches at most one bounded existing worker if due and capacity permits.
`review-defer {op_id,expected_revision,owner,reason}` records real inability without
consuming evidence. `explicit_review:true` on status/pending bypasses the count gate
for a direct request; no incidents still means no review. Nothing schedules a run.

`review-batch {}` returns bounded incident text and `batch:{cursor,ids,digest}`.
Give that exact batch to a bounded reviewer (WORKER + LEARNING), not full history.
Save its actual output and separately observed overhead:

```json
{"op_id":"review-1","expected_revision":4,"batch":{"cursor":0,"ids":[1,2,3],"digest":"exact returned digest"},"review":{"summary":"Three customer-slide incidents support a scoped proposal","reviewer":"actual-host-handle-or-unknown","spend":{"seconds":"unknown","tokens":"unknown","cost":"unknown"},"proposals":[{"kind":"knowledge","claim":"Keep customer deck slides sparse","scope":{"tasks":["customer-deck"],"paths":["slides"],"audiences":["customer"]},"basis":[1,2,3],"hypothesis":false}]}}
```

`review-save` durably stores output/proposals and advances the cursor in the SAME
atomic commit. A no-proposal output still needs a reason in summary. Batch mismatch,
skipped evidence or stale cursor fails without advancement. Later incidents stay
pending. Limits: at most 100 incidents per selected batch, 20 proposals, 32000 bytes
review output. Defaults are smaller. Output retention is not implementation.

`decide {op_id,expected_revision,proposal_id,decision:"accept"|"reject"|"retire",owner,reason}`
retains an explicit owner decision. Accept copies the proposal's exact scope; no
claim/scope override is accepted. Hypotheses cannot become rules. Accepted routing/
structure proposals require separate authorized implementation and create no role.
Retire applies to current accepted proposal knowledge and retains its prior history.

For an already explicit user instruction, apply it now within authority. Durable
selection needs no reviewer or threshold:
`accept-rule {op_id,expected_revision,request_id,expected_request_revision,source_id,claim,scope,owner,reason}`.
The source/revision and explicit supplied-decision reason remain provenance. This
path trusts the caller; it does not prove a user spoke or grant permissions.
`retire-knowledge {op_id,expected_revision,knowledge_id,request_id,expected_request_revision,source_id,owner,reason}`
retires either an explicit K-* rule or proposal-backed knowledge with a retained
source-aware decision. Supersede by retiring the old rule and accepting the new
explicit scoped rule/proposal; query matches exclude retired entries. Revisions
make concurrent changes fail visibly; old rules and decisions remain evidence.

Mutating receipts expose prepare_seconds (precommit, excluding atomic write) and state_bytes; these are local helper
overhead, not model cost. Review workers report their actual spend or unknowns.
