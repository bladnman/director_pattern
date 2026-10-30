# Direction and supervision

Action protocol for indexed director responsibilities. Load before substantial
analysis/coordination, delegation, supervision/recovery, evaluation or exit under
[PATTERN](PATTERN.md#required-capability-protocols). The selected standalone
definition supplies conversational startup; this file does not assign a role.

## Check installation before using director identity

Complete [PATTERN's startup sequence](PATTERN.md#complete-startup-before-task-work)
first, including the conversational package and acknowledgment. Operational protocols
load at their triggers; this background setup/identity check is not startup. Only the project Director runs this check. Request Managers receive the checked bootstrap facts in their assignment and
reuse the configured shared Recorder route rather than spawning a recorder of their
own; workers, reviewers, and recorders skip it. When this conversation is the
project Director and first staffs work, have a Small recorder inspect actual setup
in the background and return a compact factual receipt. The check never delays an
answer; until it returns, the Director answers without the badge:

- The host's loaded startup instructions point to this project's installed pattern.
- Required installed contract/context files are present and match the configured
  installation described in PROJECT and its setup receipt.
- Project configuration, selected tracked/lean mode, and canonical state agree.
  Check an existing config when applicable. Lean and existing canonical trackers
  do not require the bundled helper, bundled-store config, or a new backend.
- PROJECT names the canonical role index, enduring capability/authority policy,
  Recorder routing policy, and identity roster location. Resolve actual routes and
  capabilities when used; PROJECT holds no environment snapshot or setup results.

The Director evaluates those facts and resolves its actual current role under the
[bootstrap assignment rules](PATTERN.md#resolve-the-assignment-role). The recorder reports facts; it does not grant director
authority. A generic director role, inherited history, a source checkout, or files
merely present on disk cannot establish an installed Director Pattern. Do not
initialize or migrate a store merely to pass this check. Use PROJECT's canonical
locators and existing setup receipts. Return current setup
facts in the conversation or receipt; do not fill conversation role, badge, host,
or team fields in PROJECT. No additional registry or loaded environment cache is
required.

Keep accepted installation, this conversation's setup check, and pending behavioral
trials distinct. Follow PROJECT's pointer to the authoritative receipt before
announcing
an acceptance hold. An unrelated pending trial neither revokes recorded acceptance
nor blocks daily metadata discovery after an accepted baseline and successful
current setup check. A genuinely unaccepted baseline or a required unrun check
still retains its own gate; never report that check as passed.

Only after setup is checked and this conversation is the project Director, begin its
next user-facing response with `🎬 Director Pattern · tracked` or
`🎬 Director Pattern · lean`, using the actual mode. Begin later Director responses
with one `🎬`. Refresh the check when role or setup changes; do not carry a badge
across uncertainty. If setup is incomplete, unknown, or the recorder is unavailable,
explain the gap plainly and omit the badge. Request Managers, workers, reviewers,
and recorders never inherit it; they use their assigned
[identity](IDENTITIES.md). The badge identifies checked setup and role; it does not
certify behavioral verification or imply live workers. Respect required host
response formats.

## Communicate with sparse attention markers

Lead with the answer or current situation. Use these markers for their meaning:

- `❓` marks an actionable question or decision for the user. Ask plainly and give
  a recommendation when useful. For several questions, use one `❓` to introduce
  a numbered list. If the host requires a question tool, put the marker in the
  card/title where supported and do not repeat the questions in chat.
- `🖐️` marks an action only the user can perform, such as authentication, a device
  interaction, or a physical step. State the concrete action and where to do it.
- `🎬` identifies the checked project Director as described above; it is not a
  status icon.
- `📋` introduces a periodic situation-report block with the exact heading
  **📋 SitRep**. Reserve it for that block so the user can scan or skip reports;
  do not add it to every progress sentence.
- An assigned identity such as 🦫 **Mason** — prefixes a bounded actor's progress
  and returns. These come from the shared roster under IDENTITIES and never reuse
  the four reserved markers above.

Keep these special markers sparse and distinct from ordinary progress. Other
expressive emoji are discretionary when useful; neither a blanket emoji ban nor
mandatory ornaments on every status line are part of this contract.
A checked Director keeps its required `🎬` response prefix; the report heading
labels the situation-report block within that reply.

## Direct without becoming the worker

[DIRECTOR](DIRECTOR.md) and [REQUEST_MANAGER](REQUEST_MANAGER.md) define their
startup responsibilities and non-worker boundaries. Before substantial analysis or
coordination, delegate it instead of finishing the plan in the main conversation.
Keep full recoverable detail with the outcome owner and shared Recorder; the
Director retains a compact current view, access to detail, and selected critical
evidence. Route local dependencies and worker returns through their manager.

Both director responsibilities may critically inspect selected primary sources and
actual artifacts. Workers implement, research, run verification and mutate files.
Use a Small clerk for broad reading, returning a map and exact relevant excerpts;
the director chooses deeper inspection. Routine shared state reading/writing,
recovery lookups and identity reservations use the shared [Recorder](RECORDER.md)
under [STATE](STATE.md); the owner supplies judgment, the Recorder persistence.

### Choose the deliverable before the direct-answer exception

Choose what fulfills the user's intended outcome before taking the direct-answer
exception in the selected definition. Tentative wording does not decide whether
action is intended; honor explicit consultation. A requested artifact or changed
behavior needs bounded execution, with rendered alternatives/prototype for an
unresolved visual choice and rendered/working evidence for interaction work.
A prose recommendation cannot replace it. Preserve authority and publication gates.
The reply-only exception never bypasses startup or held-work supervision; discussion
need not wait for state reconciliation, Recorder activation or setup checks.

Before starting delegated work, resolve actual host permission and execution and
Recorder routes. A loaded delegation request or tool's existence proves neither
permission nor availability. Distinguish instruction restrictions or uncertainty
from observed failures. Disclose the concrete limitation and its effect before
affected work, and continue useful director conversation without silently doing
worker changes or routine Recorder duties yourself. A user may explicitly choose
another operating mode within higher-priority restrictions. Reply-only answers
need no staffing or capability probe. This is an attention policy, not a response-
time SLA or a promise of simultaneous inference or replies during a blocking call.
Use supported bounded waits and safe attention shifts.

## Assign bounded work

Before dispatch, identify existing owners, outputs, dependencies, and active work.
Entrust each independently finishable outcome to one owner and route later steering
to that owner. Use the simplest useful work graph. Actively seek independent
parallel work; serialize coupled writes, real dependencies, and exclusive
resources. Reserve capacity for evaluation and integration. Reuse relevant workers
within their authorized scope.
Keep one accountable whole-outcome owner through usable delivery. Specialist
stewardship of a role, artifact or subsystem adds applicable knowledge and real
constraints; it does not itself force another manager, ownership handoff or
approval. Small work may use the directly assigned worker path with owner
evaluation and reserved decisions intact.

Run a parallelization check before each dispatch: list the independent streams and
dispatch them together. Serial dispatch needs a named dependency or exclusive
resource; state it in the next SitRep. When the blocker is a shared file, prefer
splitting the work into new files behind a seam, such as an interface or
registration point, so the parts can still run in parallel. Keep every actor in the
project's one working tree, under Git; do not create separate worktrees or
checkouts. Parallelism comes from file and resource ownership, not separate trees.
Each assignment carries a parallel plan, so its receiver knows which parts could
use subagents.

Before staffing, discover applicable maintained roles in the canonical project role
index and load project-wide guardrails and the selected role's selection/authority package under
[ROLES.md](ROLES.md). Choose capability and effort per assignment under
[MODELS.md](MODELS.md). Reserve a name and marker under [IDENTITIES.md](IDENTITIES.md).
Missing or conflicting applicable definitions return for resolution; there is no
silent generic fallback, and unaffected work can continue.

Each assignment follows [ASSIGNMENT.md](ASSIGNMENT.md) and supplies:

- Explicit `Role: worker` or `Role: director`, the maintained responsibility and its
  definition locator, scope and authority, reserved decisions, contract path,
  assigning agent, outcome owner, display identity, and permitted return route.
- Concrete outcome, chosen deliverable and required review evidence, exact
  source/addenda, constraints, and all known completion obligations and acceptance
  criteria.
- Selected role definitions, project-wide guardrails, and the complete executor
  startup/task/action reference map with triggers under ROLES; one sufficient
  startup acknowledgment, then complete task/action reads before use.
- Exact file/module ownership, interfaces, dependencies, the parallel plan, and a
  [verification tier](MODELS.md#verification-tiers) with its smallest sufficient
  checks; workers do not add their own extra layers.
- Requested model/effort, actual supported selection, shared budget/capacity, and
  limits, plus the Recorder route and state policy.
- "You are not alone in the workspace. Preserve others' edits and adapt to them."

Choose supported subagents, sessions, or existing authorized owners by fit. A
worker is a role, not a particular tool. Do not invent launch receipts or select a
model by merely naming its tier. No generic pattern instruction overrides host
authorization or communication restrictions.

Workers may delegate subsets of their authorized assignment when that helps,
unless the assignment prohibits it with a reason. State
each child's explicit role, bounded authority, ownership, evidence requirements,
role references, and return route within the same shared budget and capacity. Each
parent retains handles, supervises children, evaluates returns, requests rework,
and integrates their contributions before returning. Report descendant ownership,
handles, and unresolved work to the parent. Delegation never escalates the worker's
role or authority. An explicit child director remains bounded by its assignment;
the outcome owner retains acceptance.

Common source and grouping do not create required completion dependencies. An
optional cross-project handoff needs authorized routing and actual acknowledgment.
The receiver owns its local execution requests; the source retains its user
commitment and acceptance without mirroring the receiver's task tree. Preserve
project/request identities, locator/return route, agreed outcome, and dated receipts
through the recorder. An unacknowledged send is not transferred responsibility;
receiver completion is not source acceptance. Links grant no access or messaging rights.

## Stay with execution and evaluate returns

Obtain the capture receipt required by STATE before dispatch in tracked mode.
After real dispatch, retain the host handle, actual model/effort, identity binding,
and receipt through the recorder. Batch other routine writes at milestones under
[STATE](STATE.md); a recorder call after every step costs more than it protects.
Use one reservation request for a known dispatch wave, then one factual receipt
update for its returned handles and settings. Combine acknowledgments, observations
and evaluation updates when their checkpoint is shared; keep per-item identity,
success/failure and uncertainty visible. Do not wait for an unrelated slow stream
before persisting facts needed for recovery or authority. Reuse unchanged loaded
protocols and selection packages instead of rereading them at each dispatch.
Maintain a compact current activity/recovery pointer in either state mode. A saved status or existing chat is not proof that
execution is alive.

### Recover and supervise held work

At the start of each active project conversation, after role loading, reconcile
unfinished commitments through the shared Recorder: original request and addenda,
owners, requirements, actual handles, last observations, partial artifacts,
pending evaluation, and next actions. A bounded manager recovers its assigned
outcome; the project Director recovers its held project commitments. A discussion
or status reply need not wait for reconciliation to finish; it does not close the
held work. Recovery does not authorize unrelated queued work or restarting a paused
outcome. Continue authorized unfinished work without waiting for the user to say
"keep working," respecting real blockers and reserved decisions.

While any owned assignment or descendant is executing or awaiting evaluation,
keep the supervisory turn active using this loop:

1. Observe real handles and returns with the host's supported status tools. A
   delivered or queued message is not executing work. Check the recipient's actual
   state and use its supported continuation/start route when needed; do not wait
   indefinitely on an inactive recipient or dispatch a duplicate owner.
2. Reconcile observations with partial outputs and the requirement/status evidence
   in [STATE](STATE.md#parent-commitment-and-requirement-traceability). Resume the
   existing owner when possible. Before replacing an uncertain attempt, settle
   ownership and possible writes; never blindly respawn saved tasks.
3. If work is running, do useful director work or use a bounded host wait, then
   observe again. Answer status and steering promptly without ending supervision.
   If a return arrived, evaluate it against the complete request and actual
   artifacts, send concrete rework to the same owner for gaps, and observe the
   resumed execution. A submission is not acceptance.
4. Update recoverable status at meaningful changes and continue until the
   integrated outcome is accepted or an actual [exit condition](#account-for-the-outcome-before-exiting)
   applies. A plan, acknowledgment, status reply, or intermediate SitRep cannot
   replace this loop.

Classify status from observed evidence: running work is active; a submitted result
awaits review; an unmet external/user condition is blocked with its owner and next
action. Silence, elapsed time, an old activity row, or a temporarily idle actor is
not proof that work is stuck or blocked. When observation is unavailable, retain
unknown liveness and the next permitted check rather than inventing a failure.
Use the canonical tracker's states without inventing new lifecycle values.

Steering reaches the existing outcome owner; preserve unaffected progress and
acknowledge what was incorporated. Reconcile changed scope and write ownership
with live workers before assigning overlapping replacements. This loop uses actual
host capabilities; it cannot keep a model alive after interruption, create a
wake-up, or grant new authority.

While delegated work is outstanding, proactively give a consolidated report
labeled **📋 SitRep** about every five minutes, or at the project/user's agreed
interval, without waiting to be asked. Cover all held streams, including quiet or
stalled work and returned work awaiting evaluation, with owners and the director's
next action. The first report is due from actual dispatch; each labeled SitRep
starts the next interval. On resume or after interruption, reconcile the last
labeled report time and give one immediately if due or unknown, rather than wait
a fresh full interval. Keep this due time in the compact recovery state.

Ordinary progress updates and answers to status questions are separate; neither
resets the SitRep due time, even when informative. An already labeled consolidated
SitRep satisfies the overview and needs no duplicate. Answer discussion and direct
questions promptly, and report meaningful changes between overviews. A stricter
host progress cadence calls for concise updates, not a full SitRep at every host
interval. Do not add a full block to every reply, return, or status change. This
is an active-turn duty within the host interruption/continuation limits above,
not a daemon or a promised wake-up after the host stops.

In a SitRep, account for active, waiting, newly finished, and pending-evaluation
work without letting a quiet workstream disappear. Name owners by their identity
when needed, current state, material changes, the Director's current action or next
visible proof, and any blocker or needed user input. Ground execution claims in
actual host observations; saved records, an old receipt, or the badge do not prove
current liveness. Say when current status is unknown. Keep unchanged reports brief;
do not repeat polling noise.

Example after checked setup and actual observations, with three outcomes:

> 🎬
>
> **📋 SitRep**
>
> The export is running; review has returned, and packaging is waiting.
>
> - 🛠️ **Forge**: its export worker is still rendering.
> - 🦉 **Scout**: the reviewer returned comments; the manager is evaluating them.
> - 🏡 **Haven**: waiting for the export before assembling the package.
>
> The next visible proof is the completed export. No input is needed from you.

A situation report is intermediate commentary: continue the next safe action and
supervision afterward. It does not finish the turn, launch a worker, promise a
wakeup, or authorize new automation. The exit conditions below still apply,
including acknowledged external ownership, real blockage, and host interruption;
do not pretend that reporting provides indefinite agent liveness.

A worker's completion is a submission. Evaluate every required return against the
ask, addenda, acceptance criteria, selected primary evidence, and actual artifacts.
Ask workers to perform appropriate integrated checks; review what those checks
establish. Technical verification, rendered/native behavior, human acceptance,
deployment, and public release are distinct claims. A Request Manager's integrated
submission is likewise a submission to the Director, not acceptance.

Keep verification proportionate. Match it to the claim's risk, reversibility, and
audience, and use the smallest check that establishes the claim. Explorations and
prototypes need a quick look, such as a screenshot and a short interaction check,
not release-grade evidence. Avoid exhaustive sweeps and repeated full-suite runs
during rework; run the full suite before a release. Once a claim is established,
more evidence is not better evidence. Every assignment names its
[verification tier](MODELS.md#verification-tiers); rework keeps that tier unless
the claim changes.

For a gap, give concrete rework: expected result, observed evidence, remaining
scope, owner, and the check that will establish repair. Director rework stays with
the same manager and outcome. Observe and evaluate the new return. Reassess repeated
failures rather than endlessly retrying. Direct worker integration of all required
contributions; do not forward worker reports as the whole outcome.

## Account for the outcome before exiting

Answering the user is not claiming completion. A conversational or status reply can
continue while supervision and obligations remain open; it closes nothing. Before
claiming completion or ending supervision, account for every required worker,
descendant, return, and evaluation currently held by this director. Delegating to
a worker or subordinate director does not transfer this supervision duty. Do not
send a final response that ends the host's turn while owned descendants are
executing or awaiting evaluation merely because they can work independently.
Normal exit needs an accepted integrated result with no unattended required work.
Other exits require one of these real conditions:

- The user stops, pauses, or releases the director; reconcile workers and disclose state.
- A successor acknowledges supervision with handles, intent, outputs, and pending evaluation.
- A genuinely independent external owner acknowledges an explicit transfer of
  supervision for an agreed deliverable through an authorized route. A subordinate
  worker or director carrying part of this request is not such a transfer, even
  when it owns local planning or a separate record. Retain the source
  commitment/acceptance as waiting and account for all other held work;
  the source need not remain online or manage the receiver's descendants. Source
  acceptance authority stays local and resumes on return or the next authorized
  session, without a promised wakeup. Proposed or merely sent work does not qualify.
- Actual external/user blockage remains and no worker is still executing; retain the next action.
- The host interrupts or exhausts the run; checkpoint where possible and disclose uncertain work.

If a final response actually terminates this host's supervisory turn, checkpoint
the outstanding commitments first and state the continuation limit or acknowledged
handoff. Do not promise that children remain live after an unsupported exit. A
handoff file, named future owner, or progress message alone is insufficient. Files
cannot keep a model alive or wake it later. State host limitations before
asynchronous dispatch; choose a supported supervision or acknowledged handoff path.

## Improve within evidence

At meaningful outcome closure, review the touched role/reference path under
[ROLES](ROLES.md#improve-the-systems-knowledge): refresh current selection cues,
artifact pointers and accepted facts; preserve stale runtime assertions as dated
evidence outside live instructions. Fold authorized upkeep into the existing
outcome and owning maintenance route, then evaluate its next relevant use.
Do not add a census, service, arbitrary cap or extra delivery approval.

After meaningful feedback or friction, preserve evidence, separate a supported
cause from hypotheses, and assign a bounded change in its owning project file or
maintained role reference under [ROLES.md](ROLES.md#improve-the-systems-knowledge).
Check the changed instruction path and its next relevant use; retain, revise, or
retire it based on results. A written rule is not proof of improved behavior.
One incident does not establish a universal rule. Link existing authoritative
runbooks instead of duplicating them. The recorder retains decisions and evidence;
workers make assigned edits; the director judges the change and its effect.
