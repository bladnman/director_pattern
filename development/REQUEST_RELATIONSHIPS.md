# Request relationships and cross-project ownership

**Candidate semantics · October 16, 2026.** The user authorized implementing request
folders and these flexible links. The bundled helper now represents supported
local relationships/handoff receipts; it is not a transport or real-store migration. Tracked
remains the accepted default. One project and one director remain the normal case;
an external handoff is optional. No graph database or central registry is required.

## Distinct relationships, without a required tree

Keep these meanings separate; a directed link states which meaning applies:

| Relationship | Meaning | Completion effect |
|---|---|---|
| Source/provenance | Outcomes refer to one exact original user message or later addendum. | None by itself. |
| Grouping/decomposition | Deliberately collect related scope or split an outcome into parts. | None unless required dependencies are explicitly declared. |
| Required completion dependency | This outcome cannot be accepted successfully until the agreed prerequisite is met or removed with authority. | Explicitly gates acceptance. |
| Handoff/ownership | Another project acknowledges responsibility for an agreed deliverable. | Source commitment remains open when that deliverable is required. |
| Information/reference | Context, related research, or a result worth linking. | None by itself. |

“Parent/child” can describe deliberate decomposition; it is not the universal
relationship model. Common source, a parent label, or a folder location never
silently creates a required dependency. Ownership is independent of these links.
Flat physical bundles can express them without nesting or a fixed team structure.

Preserve the complete original message as one immutable canonical source, with
attachments and later exact addenda. Give each independently finishable outcome
its own ID and status immediately. Link all to the source; keep director-authored
scope/instructions separate from the user's words. An optional umbrella request
is useful only when there is a whole-scope commitment to accept. The source message
itself is provenance, not an executing parent. Completed siblings remain complete.

## Four outcomes survive tomorrow's restart

One message asks for a folder, research, a new repository, and a complex app. The
first three finish locally; another project's director acknowledges the app work.
The following is illustrative state, not a claim these tasks were executed:

| Local outcome | Owner of canonical record | Restart answer |
|---|---|---|
| REQ-1: create folder | Source project A | Complete; retain acceptance/evidence. |
| REQ-2: research | Source project A | Complete; retain accepted research/result. |
| REQ-3: new repository | Source project A | Complete; retain accepted repository result. |
| REQ-4: obtain complex app | Source project A | Waiting on project B's acknowledged deliverable; last verified observation/time retained. |
| App execution and its local requests | Receiving project B | B owns all its requests/children; A has an agreed outcome reference, not B's task tree. |

A new director can report “three complete; the app is waiting on B,” without
untying, reopening, or rebundling anything. A recorder retrieves local source links,
outcomes, handoff receipts, and observations. A director authorized to read A can
answer from that evidence; it need not gain access to B. Any optional umbrella
stays open while its explicitly required app outcome is pending.

A's REQ-4 is its own commitment to the user, not a second canonical copy of B's
request. B may create one or many local requests with source correlation. B owns
execution and internal decomposition; A remains accountable for the promised
outcome and its own acceptance. A does not control or mirror B's internal work.
REQ-4 is illustrative: retain the commitment/waiting link in an appropriate local
record or optional aggregate, without requiring a synthetic umbrella or fixed proxy
shape. The restart answer must remain recoverable whichever representation is used.

## Stable identity, acknowledged ownership

Use project/installation identity plus request ID. Store current root/path as a
locator hint, not permanent identity. Resolve IDs when paths move; unresolved or
unknown locations stay explicit. Each request has one owning project. Changing
an assignee does not silently move its record authority between projects. An
explicit ownership transfer could retain an acknowledged owner change/forwarding
reference and one current authority; ordinary handoff does not perform that transfer.
Derived summaries and remote observations never become remote canonical state.

Before handoff, identify an authorized, capable destination and permitted return
route. The proposed portable envelope carries source identity and locator, the
requested outcome, relevant exact user-source/attachment references, constraints,
acceptance, and action authority. Transfer available content if references are
inaccessible; acknowledge missing material. Record receiver identity/request IDs
only after an actual acknowledgment. A link grants no access or messaging rights.

An illustrative handoff record, **not a parser schema**:

```yaml
source: {project: project-A, request: REQ-4}
source_locator: /current/project-A
return_route: authorized host channel or reachable result location
outcome: Deliver the agreed complex app
source_refs: [UR-1, UR-1/attachments/specification.pdf]
content_transfer: available content delivered; missing material explicitly listed
constraints_and_authority: agreed scope, action boundaries, and required gates
acceptance: agreed deliverable and evidence; source director evaluates return
relationship: required outcome dependency and acknowledged external ownership
receiver: {project: project-B, outcome_ref: APP-17} # after acknowledgment
handoff_receipt: actual acknowledgment reference and timestamp
last_observation: dated verified status; current liveness unknown unless checked
source_disposition: waiting for external deliverable; acceptance pending
```

Attempted send, acknowledged handoff, actual execution, returned evidence, and
accepted outcome are distinct observations. An unacknowledged send leaves routing
and follow-up with A. Acknowledgment transfers the agreed execution responsibility,
not ownership of A's user commitment or acceptance authority. B supervises that
external execution after acknowledgment; A can durably wait without staying online
or managing B's descendants, once A accounts for its other held work. A proposed
or merely sent handoff does not satisfy this condition. Neither project can edit the other's records
or direct its internals merely because a link exists.

The director records required dependencies when decomposing work to satisfy
acceptance; each link needs no separate user permission within authorized scope.
Declare real blocking edges explicitly. Before successful closure, check required
edges for cycles, dangling references, and unresolved outcomes; expose ambiguity
instead of inventing success. The bundled helper enforces supported local required
cycles/closure; cross-project meaning and evidence still need director judgment. Independent and informational links never gate closure; informational
backreferences may be reciprocal. Check cycles only on actual blocking completion
edges, without requiring a global graph crawler.

## Recovery, return, change, and cancellation

On restart, the recorder retrieves local open outcomes, saved acknowledgments,
last dated observations, evidence, and next actions. Report completed siblings as
complete and REQ-4 as waiting on its named external owner. If no fresh query is
available, state the last verified status/time and unknown current liveness.
Refresh only through an authorized host route; do not force foreign filesystem
access. Preserve partial artifacts and do not duplicate execution because data is old.

Recover the local waiting commitment, then evaluate the remote deliverable when
it returns. B's completion is a submitted result for A's agreed acceptance; it
does not close A automatically. Successful acceptance of REQ-4 requires the agreed
deliverable to be met. Authorized removal/cancellation gets an explicit non-success
or revised-scope disposition with history preserved; removing a required edge may
unblock an aggregate but cannot make the original REQ-4 successful. Re-evaluate
the aggregate against its explicitly revised scope. Failure is not success.
Source acceptance resumes on return or in the next authorized session; retaining
a waiting commitment promises no automatic wakeup or continuous source supervision.

Changes and cancellation require explicit permitted communication and acknowledgment
where the receiver is affected. Updating A's state cannot stop B's execution or
revoke its writes. Preserve actual message/decision receipts and disclose uncertainty.
This design authorizes no foreign messages, new chats, or background monitoring.

## Implementation and remaining limits

The [bundled record contract](../pattern/engine/references/RECORDS.md) and
[CLI reference](../pattern/engine/references/TOOLING.md) define the implemented schema/API.
Request folders move with their assets/evidence; immutable source bundles preserve
shared originals. Typed links separate group/decomposition/information from required
dependencies. Local required targets must exist and be done; required cycles fail.
External dependencies require explicit director-reviewed evidence. Observations do
not satisfy closure or establish present liveness.

The helper records proposed/requested/acknowledged/returned/accepted handoffs. A
proposal may know only the receiving project; acknowledgment binds its actual
request identity. Required acknowledgment retains the source in blocked/waiting;
source acceptance of the return and its normal completion lifecycle remain distinct.
On return, the source can resume, bind the actual remote execution/return receipt
through dispatch, submit evidence for review, then accept; this records existing
execution and does not pretend the source launched a new worker.
A required waiver records changed acceptance and returns to queued; it cannot
mark an unmet original deliverable successful. This document's YAML is illustrative
context, not literal CLI payload; use the actual event definitions.

No foreign resolver/reads, transport, automatic refresh, global cycle crawler,
authenticated remote proof, or real-store migration is implemented. Verification
evidence belongs in DESIGN_NOTES; code availability is not project adoption.
Simple projects need no external-owner setup.
