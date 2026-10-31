# Bounded review, paid for when it runs

This is an action guide. Empty/simple tasks need no learning actor. Incidents are
evidence, not rules. Capture meaningful friction/corrections inline with `observe`
or `evaluate` using `incident`, or explicitly with the `incident` action. Preserve
source/request revision, task/path/audience scope, evidence, hypothesis and owner.
Exact user corrections are captured as sources/addenda first, not reconstructed.

`pending` exposes the queue and the installation's explicit initiator/opportunity
policy. Default: the outcome owner initiates one review at meaningful closure when
three incidents are pending (`min_incidents: 3`) and capacity exists. This number
only batches review spend; it establishes no truth or department. Ordinary
observation/evaluation receipts and compact status expose `review_due` and the
pending count. `user`/`explicit` instead leaves review for a direct request; an
explicit review query (`explicit_review: true`) bypasses the count gate.
At a due opportunity the initiator actually assigns one bounded existing worker
the reviewer task: WORKER, this guide and one `review-batch` result. It need not
load a Director/Architect or full history. Default batch is at most five incidents
and 12,000 encoded bytes; caller budgets may be smaller/larger within host limits.
Record the actual reviewer handle/settings or `unknown`, and review spend/time
separately from product execution. If dispatch or background execution is not
available, use `review-defer` with the real reason, preserve `review_pending` and
report that no review ran. A file does not
wake an actor. Scheduled/offline review requires separate user authorization and
an actual host scheduler; none is installed here.

`review-batch` is read-only: it returns contiguous pending evidence, source/scope/
revision and a digest/token. The reviewer proposes a supported correction or says
why none is warranted, separates hypotheses, and may propose knowledge, routing
or structural changes. Return a durable bounded review output through
`review-save`, with the batch and expected state revision. That single atomic
commit stores the output/proposals before advancing the cursor. A crash before
commit leaves evidence pending; after commit a replayed `op_id` returns its receipt.
Concurrent/stale/conflicting output fails visibly. No cursor-only acknowledge or
silent discard operation exists. New incidents remain pending for another batch.

The existing owner evaluates each proposal with `decide`; acceptance is an explicit
scoped decision, not an automatic promotion. Only accepted `knowledge` proposals
enter the current selector. `routing`/`structure` proposals need separately
authorized implementation; accepting a proposal does not edit roles or grant
permissions. No department is created from a number of corrections. Hypotheses
cannot be accepted as rules. Retire/supersede knowledge with another explicit
decision, retaining prior review/source evidence. On the next matching task,
`select` returns only accepted current knowledge for the requested task/path/audience,
with provenance and paging; consume every applicable page before affected work.
An explicit user rule is different from incident accumulation: apply it now in
the authorized scope. `accept-rule` can record that supplied decision directly
with exact source, request revision, scope and owner reason, without waiting for
three incidents or staffing a reviewer. This trusted-caller path authenticates no
speaker and grants no new authority.

The helper uses a local cooperating-writer lock and atomic state-file replacement.
Callers are trusted to hold authority: the schema does not authenticate owners or
sandbox files. It reads the state file internally; state I/O cost grows with this
small store. Receipts expose state bytes and operation time, not model cost/token
estimates. Larger review/routing architecture is a later explicit decision.
