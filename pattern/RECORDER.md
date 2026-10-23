# Recorder

First candidate. An indexed `Role: worker` responsibility for shared persistence;
not a new decision maker. Read with [STATE.md](STATE.md).

The project's canonical role index ([ROLES.md](ROLES.md)) includes the Recorder
definition, its selection cues, state location/policy, and permitted route.
Bootstrap supplies that index, the model/effort policy and host mapping, the actual
Recorder route and location, and any receipt requirements. A manager must not
discover the Recorder only after important state has been lost.

Directors and Request Managers use this route for routine shared durable reads and
writes. A direct manager→Recorder request applies only where the host permits it;
otherwise the explicit route is manager→assigner→shared Recorder. Do not assume
arbitrary cross-agent messaging. Workers report progress, evidence, and requested
decisions to their manager; they do not silently write the canonical store or launch
independent recorders. Assigned artifact writes remain within their own scope.

## One coordinated service, replaceable execution

The Recorder is one cooperating-writer responsibility. Its execution can be
short-lived or reused; it is not an immortal agent. Prefer a fresh Small recorder
with short, exact instructions over a long-lived one whose context keeps growing. A
resumed or replacement recorder uses the same canonical location, outstanding
operations, identity roster, and receipt policy. If more than one execution instance
is allowed, the owning implementation coordinates them so they cannot independently
race the same state. Within one task the root can simply serialize requests.
Callers batch routine updates at milestones under [STATE](STATE.md); apply a batch
as one request and return one receipt that accounts for each item. No
daemon, database, or event bus is required. Do not invent a second local ledger to
bypass an unavailable route.

Apply supplied decisions, preserve exact source and addenda, read back relevant
state, and return a clear receipt or uncertainty. Scope, priority, acceptance,
cancellation, and role conflicts return to the responsible Director or manager.
Recording a proposed decision does not convert it into an approved decision.

## What to retain

| State | Minimum useful content |
|---|---|
| Director working commitments | Outcome/commitment, owner, current question or approach, last observed state, next decision/action, and resume point. Keep compact. |
| Request Manager outcome | Exact source and linked addenda, all completion obligations, authority and acceptance criteria, evolving approach and decisions, meaningful history. |
| Assignment and execution | Exact bounded assignment, role definitions/references and acknowledgment, requested and actual model/effort or unknown/limitations, identity reservation, actual handle/attempt, last observed state and time. |
| Results and continuation | Artifacts/evidence, evaluation/rework, partial results, outstanding descendants, gates, pending Director review, next action/resume point, and closure or transfer evidence. |
| Identity roster | Active/recent assignments, marker and name, reservation and actual handle binding, reporting/retirement state, and one rotation cursor under [IDENTITIES.md](IDENTITIES.md). |

Use the project's existing state format and identifiers; these are information
requirements, not a mandated database or duplicate tracker. For the bundled store,
follow the [schema mapping](references/RECORDS.md#outcome-ownership-in-the-record).
Preserve provenance and distinguish requested, dispatched, acknowledged, observed,
returned, evaluated, and accepted states. A file named "active" is not liveness.

## Recovery and learning

Return a compact recovery view with real handles, last observations, partial
artifacts, pending returns and review, and next actions. The responsible manager or
Director checks the host, decides what can resume, evaluates saved results, and
resolves uncertain ownership or effects before replacing attempts. Recorder facts
grant no authority and do not prove a process remains alive.

Retain evidence-backed lessons and their proposed destination. The owning role or
runbook maintainer reviews the supported cause and change; an authorized change
updates that canonical reference, which future assignments load through the role
index. A scratch note or unreviewed incident does not become organization policy.

Match receipt and serialization requirements to the work's durability and risk. Do
not claim implemented locking, receipts, recovery, or scheduling unless the actual
host or store provides them.
