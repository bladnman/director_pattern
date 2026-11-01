# Runtime API — canonical request bundles, starter 3

Load this action guide before relevant state I/O, not at empty startup. One canonical
store, no Recorder prerequisite. The owner supplies decisions; helpers validate
structure, revisions and recorded evidence, not caller permissions, human identity,
real execution or truth. Existing trackers keep their actual verified adapter.
Never initialize another store or migrate one merely to use these commands.

The bundled helper accepts config schema 1, request-store schema 2 and exact format
`director-request-bundles`. It rejects other formats without writing; preserve them
for separately authorized recovery. Existing trackers use their own verified adapter.

## Current views and exact operations

```sh
python3 .director/requests.py --help
python3 .director/requests.py status --limit 5 --max-bytes 12000
python3 .director/requests.py current REQ-... --max-bytes 12000
```

`status` pages open id/title/state/revision/owner; `current` omits historical events.
Both return snapshot/total/next_offset/scan disclosure; continue with `--offset`
and the same `--at-snapshot`. A changed snapshot rejects; restart the page set.
An item too large for the bound fails visibly; raise within 32000 bytes or use the
selected full record through the deferred tool route. These are bounded returned
views, not constant disk work: source integrity and full histories validate inside.
Actual handles, latest steering, unresolved gates and source words must be read for
the selected task, not inferred from an open-count summary. State is not liveness.

[TOOLING.md](TOOLING.md) is the complete CLI/event schema; [RECORDS.md](RECORDS.md)
owns seven-state lifecycle, sources, typed relationships, handoffs and recovery.
Use exact sources before interpretation and retain immutable UTF-8/attachment bytes.
One source can serve independent outcomes. Capture each addendum before dependent
work; reconcile the same actual worker, requeue/revise/reopen as required, amend,
replan the full scope/human gate, then bind the same actually observed handle.
An accepted outcome cannot silently absorb new work and remain done. Initial and
revised plans/owners/acceptance remain in replayable history.

Generate each operation's fresh UUID event ID once, reuse it only for identical
retry, and use returned expected request revisions. Unknown outcomes, changed
payload reuse, stale writes, corrupted original sources and unfinished transaction
intent fail visibly. Inspect actual receipt/revision and explicit `recover` before
retrying uncertain writes; never raw-move folders or hand-merge record JSON.
Original assets/evidence attachments relocate with the bundle and keep hashes.

Only review can become done, after actual submit/evaluation and required human,
local dependency and acknowledged external-result gates. A canceled dependency is
not success; grouping/shared source is not a blocking dependency. The helper checks
declared human evidence, not who said it. User approval cannot be forged by filling
a field. Required independent testing and actual release authority still apply.

## Parent and requirement traceability

Before decomposition retain a compact requirement trace in the existing assignment
artifact/request note: source project/request IDs (or exact source for a new local
outcome), stable requirement IDs, each obligation/acceptance condition, current
owner, actual handle/observation, evidence or unresolved reason, and return route.
Each delegated assignment and return carries the relevant parent project/request
and requirement IDs plus its own local IDs. Update this touched trace at meaningful
steering/evaluation checkpoints so restart can reconstruct obligation → owner →
result/evidence and remaining approval, without loading all historical text.

Use the canonical record's owner/acceptance, actual dispatch receipt, notes and
artifact locators; no new top-level schema or mirrored task tree. Shared source or
parent/grouping links do not impose required-success edges. Record a real required
dependency only when acceptance needs it; detect cycles. An external handoff needs
actual acknowledgment and return evidence, while the source keeps its own final
acceptance/unfinished commitment. A sent message never proves transfer or liveness.

## Learning and operations

[LEARNING.md](LEARNING.md) specifies bounded typed canonical notes and real review
initiation/recovery. [OPERATIONS.md](OPERATIONS.md) separates role/display identity,
installation evidence, staffing/effort/verification and role upkeep.
[UPDATES.md](UPDATES.md) restores active-session daily discovery, project preferences
and actual pinned safe updates. These action documents add no startup actors.

After a store-replacement or configuration-fence rejection, reopen the current
store; never retry through an old loaded instance. This also applies to init.
