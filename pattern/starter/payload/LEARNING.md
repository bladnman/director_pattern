# Bounded learning over the canonical tracker

This is deferred action guidance, not every worker's startup. No second ledger,
state.json, learning actor or background service is installed. The actual owner
captures meaningful evidence alongside ordinary result/checkpoint recording.
The helper validates the existing bundle sources/histories internally; bounded
returned context does not imply constant I/O or free model/time cost.

## Initiation and recovery

At meaningful outcome evaluation/closure the Director queries the bounded `pending`
view. Use the installed `install.json` review_policy (or the mature project's explicit
canonical policy) if not already retained; no hidden helper scheduling is implied.
Default policy: three pending incidents make one review due, with the owner
as initiator and a maximum batch of five incidents/12000 returned bytes. This
threshold batches spending, never proves a shared cause or authorizes a rule.
A direct user review request may bypass it. A project's explicit documented policy
may choose another budget/checkpoint or user initiation; preserve it during updates.
No survey/reviewer is needed when no evidence is pending.

If due and permitted capacity exists, actually dispatch one bounded worker with
WORKER, this guide, the selected complete incident IDs/digests and scoped sources.
Product work may continue independently through supported host controls. If no
execution route/capacity is available, retain a canonical ordinary note of pending
IDs, reason and next active opportunity, then accurately report the deferral.
No daemon, scheduler, sleep loop, notification file or queue causes execution.
Offline review needs separately authorized real host scheduling and evaluation.

The reviewer returns one durable review output, uncertainty/settings/spend (unknown
where unobserved), and all bounded proposals together. The owner saves the complete
review note atomically before any incident is considered consumed. A crash before
save leaves incidents pending; identical UUID retry replays, changed payload/stale
revision/conflicting consumption rejects. Consumed IDs/digests in immutable review
notes are the recovery cursor, not a mutable sidecar. Fresh owners retrieve pending,
reviews and undecided proposals without a full-history model read. New appended
incidents remain pending; an interrupted reviewer never loses their evidence.

## Exact action route

```sh
python3 .director/canonical_learning.py pending --data-file query.json
python3 .director/canonical_learning.py proposals --data-file query.json
python3 .director/canonical_learning.py selectors --data-file query.json
python3 .director/canonical_learning.py select --data-file matching.json
python3 .director/canonical_learning.py append --data-file event.json
```

Defaults resolve the installed `.director/` and exact `request_store.py`; mature
adapters must supply their own verified `--store`/`--helper`, not reuse this format
on a predecessor. Queries are objects with optional `request_id`, `offset`, `limit`
(default5,max20), `max_bytes` (default12000,max32000) and `at_snapshot`. Read `total`,
`next_offset` and snapshot, continue all relevant pages; changed snapshots reject.
`selectors` returns current IDs/scopes only; optional path discovers overlapping
ancestor/descendant scopes. Map natural work to existing canonical task/audience
vocabulary, then `select` with exact `task`, actual affected `path`, and `audience`.
A guessed zero exact-tag match is not proof no semantically relevant rule exists.
Queries `reviews` and `decisions` recover durable output; `proposals` defaults to
undecided plus quarantined legacy proposals needing classification (optional
`include_decided`). No history is startup. Internal scans grow.

Every append is `{request_id, expected_revision, entry}`. Generate the entry `id`
with `requests.py event-id learning`; it is also the native note event ID. Common
entry fields: `schema:1`, `id`, `kind`, canonical `source_id`, exact `source_sha256`,
`request_revision` when that source already belonged to the request, `scope` with
nonempty `tasks/paths/audiences` arrays, `owner`, bounded `text`. A source from the
future, corrupt source, unknown field or unsupported scope shape rejects. Paths
are project-relative; `*` is explicit universal scope, never inferred from repetition.
The helper serializes cooperating learning writers and uses canonical tracker CAS;
role strings/locks are not authentication or cross-host transactions.

Kinds and additional fields:

| Kind | Additional fields and meaning |
|---|---|
| incident | `hypothesis` boolean; evidence/correction separate from inferred cause. |
| review | `incidents:[{id,digest}]`, `proposals:[{id,kind,text,scope,hypothesis}]`, `spend` object with actual settings/cost or unknowns. Nested `kind` must be `knowledge`, `routing` or `structure`; proposal IDs use `review-id/suffix`; one atomic note contains complete output. |
| decision | `proposal_id`, `decision:accept/reject/retire`; exact proposal scope, owner evaluation in text. Hypotheses cannot become rules; accepted/rejected history is terminal except explicit retirement. |
| rule | Already explicit source-backed user instruction; no reviewer/count/extra approval gate. |
| retire | `knowledge_id`, exact old scope and reason; retires a current rule or accepted proposal, preserving history. |

A review can consume incidents from several requests by explicit ID/digest; proposals
and decisions remain anchored in the review's request. Entry total is at most8000
encoded bytes, review at most20 IDs/10 proposals; use the smaller policy batch above.
Do not truncate source evidence to make it fit; reduce the batch or retain a pointer
with exact available evidence for an authorized focused investigation.

## Acceptance and later use

The existing authorized owner evaluates proposals before scoped acceptance. Only
accepted `knowledge` proposals and explicit `rule` entries reach `select`/`selectors`.
Accepted `routing`/`structure` decisions return `implementation_required:true` and
never become task knowledge merely by acceptance; use the owning maintainer for an
authorized implementation and update the actual discovery pointer. Returned
proposal/decision fields are `proposal_kind`, `classification_required` and
`implementation_required`. Acceptance cannot expand authority, create a department
or implement a file change.

Stored older proposals lacking a nested kind remain byte-for-byte history, returned
as `proposal_kind:unclassified`, `classification_required:true`. They remain visible
for owner classification even if an older decision accepted them, but never reach
knowledge selection; a new acceptance requires an explicit supported kind. Legacy
identical replay is preserved. This helper does not migrate/edit old notes or infer
their type from wording; classification support or a new explicitly typed evidence
review needs a separate scoped owner disposition. Until resolved, retain the visible
classification gap rather than inventing a knowledge rule or completed change.
An explicit user rule applies now; record `rule` for its already authorized durable
scope without waiting for review. On later matching work load all applicable
accepted entries and their provenance before acting, then check actual uptake.
Retire stale knowledge explicitly; never erase evidence or broaden audience/tasks.

Incremental reviews do not connect every past batch into global trends. Targeted
historical research/optional Architect may be justified by real evidence; it costs
execution and context. Pending capture, saved proposal, owner acceptance, updated
routing and demonstrated later use are distinct states, never automatic learning.
