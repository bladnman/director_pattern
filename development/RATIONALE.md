# Why the Director Pattern has this shape

Living design rationale · updated October 27, 2026. This repository authors a
candidate pattern; it has not automatically adopted or installed that pattern.
This document explains the current reasoning, tradeoffs, and revisit triggers.
It is not an activity log or a claim that every design direction is approved.

Keep four claims distinct: **stored** means preserved in a file; **decided** means
an explicit choice has been made; **implemented** means the behavior exists;
**verified** means relevant evidence demonstrates it. A requirement can be accepted
while its implementation remains open. Tracked-by-default is accepted; the entire
package is not thereby approved. The request-folder/link implementation is now
authorized separately; implementation and verification still need their own evidence.

The operational contracts are [PATTERN.md](../pattern/PATTERN.md),
[MODELS.md](../pattern/engine/MODELS.md), and [STATE.md](../pattern/engine/STATE.md), with the
responsibility contracts [DIRECTOR.md](../pattern/engine/DIRECTOR.md),
[REQUEST_MANAGER.md](../pattern/engine/REQUEST_MANAGER.md), [ROLES.md](../pattern/engine/ROLES.md),
[RECORDER.md](../pattern/engine/RECORDER.md), [IDENTITIES.md](../pattern/engine/IDENTITIES.md), and
[ASSIGNMENT.md](../pattern/engine/ASSIGNMENT.md). This public rationale distills design
decisions, alternatives, and regression cases. Source conversations and internal
references remain private. Public contracts must be understandable without access
to those materials or provider memory.

Entries dated before October 21, 2026 were written for the predecessor Producer
Pattern and now read in this fork's renamed vocabulary. That is a terminology change
only; their reasoning and dates are unchanged. Later dated additions record what the
[October 21 design](#decision-history--october-21-2026) actually superseded.

## R1 — One accountable conversation, without a forced organization

**Problem:** Delegation can leave the user assembling worker reports, or turn a
simple project into departments and hierarchy before those solve any real problem.
**Current direction:** One folder normally has one project director. It stays in
conversation, interprets intent, coordinates execution, judges returns, requests
concrete rework, and accepts the integrated outcome. This is the candidate contract,
not a claim of successful adoption. Explicit child director scopes remain possible.
**Why:** Accountability belongs to the outcome; team count, worker count, role,
execution mechanism, model capability, and state mode are separate choices.
**Consequence:** No fixed org tree, department registry, or mandatory network setup.
See [PATTERN.md](../pattern/PATTERN.md). **Revisit:** recurring ownership or integration friction
shows a specific missing responsibility that a bounded additional scope would solve.

**Superseded in part, October 21:** Per-outcome judgment moves to a Request Manager.
One manager, a bounded child `Role: director`, owns each complete entrusted outcome:
understanding, every completion obligation recognized at the start, planning,
specialist tasks, evaluation, rework, Director review, and required follow-up. A
specialty is a task inside the outcome, not a reason for another manager. The project
Director keeps the conversation, a compact list of unfinished commitments and resume
points, cross-outcome scope and priority, authorization, and user-facing acceptance.
The earlier "explicit child director" option becomes this normal route; a small
outcome may still go directly to a bounded worker with decisions reserved. The
no-org-tree consequence stands: managers exist per outcome, not per department.
**Why/tradeoff:** A worked multi-specialty example, not an observed incident, showed
two failures: specialty-sized owners push their dependencies back onto the Director,
and late obligations such as release verification or a customer reply vanish once
engineering reports success. The cost is one coordinating layer per outcome.
**Superseded alternative:** A mandatory shared intake agent ahead of the Director,
with a one-pass limit, was proposed and dropped: it added a second user entrypoint
and a forced hand-off for every message. The Director may instead explicitly
dispatch [bounded analysis](../pattern/engine/ANALYSIS.md) that
returns a proposal; that is a judgment, not a layer.
**Implemented:** [DIRECTOR.md](../pattern/engine/DIRECTOR.md),
[REQUEST_MANAGER.md](../pattern/engine/REQUEST_MANAGER.md), [PATTERN.md](../pattern/PATTERN.md),
and owner-relative state depth in [STATE.md](../pattern/engine/STATE.md) and
[RECORDER.md](../pattern/engine/RECORDER.md). The helper is unchanged;
[RECORDS.md](../pattern/engine/references/RECORDS.md#outcome-ownership-in-the-record) maps
owner, obligations, dispatch, notes, submission, and Director acceptance onto it.
**Regression cases:** "Investigate this bug, fix it, add tests, release it, verify
production, and thank the customer" is one outcome whose manager lists all five
obligations at the start; engineering success or a drafted message cannot close it,
and Director review does not end the manager. In the A/B/C case, A starts,
independent B arrives, and C steers A: B gets its own owner when appropriate, C
reaches A's existing manager without a Manager C, a status reply cancels nothing,
and A keeps unaffected results and acknowledges what it incorporated. Tracked
steering of an active or reviewed outcome uses
[legal replanning](../pattern/engine/references/TOOLING.md#steer-an-active-or-reviewed-outcome)
to the same owner and observed handle. **Verification limit:** Fixtures cover the
record mapping only; no live manager behavior has been observed
([scenarios](DESIGN_NOTES.md#request-manager-scenarios--october-21-2026)).

## R2 — Protect judgment and conversation from execution/bookkeeping

**Problem:** A director doing every small implementation or state update can drift
back into being the worker, consuming its attention and strongest model capacity.
**Current direction:** Director is strictly non-worker. It answers discussion and
critically reads selected primary evidence/artifacts for judgment. Workers execute;
Small clerks map broad material; a Small recorder performs routine state I/O.
**Why/tradeoff:** This preserves focus but requires actual delegation/persistence
support; unavailable capability must be disclosed, not hidden by a silent role switch.
**Consequence:** Capability tiers describe reliability/reasoning needs, not brands,
cost guarantees, or selections made by a prompt label. Host model/effort mappings
must be actual or unknown. See [MODELS.md](../pattern/engine/MODELS.md) and [PATTERN.md](../pattern/PATTERN.md).
**Revisit:** observed host limits or workload evidence justify a consciously chosen
operating-mode change; they do not create a permanent direct-execution exception.

**Extended and superseded in part, October 21:** The non-worker boundary stands and
now covers Request Managers: they delegate implementation and routine work, including
a small task. A small outcome may go directly to a `Role: worker` with decisions
reserved; no implicit director implementation exception is added. The fixed model
defaults are superseded: "Default director: Max," which children could inherit,
becomes a per-assignment policy. Directors and managers read
[MODELS.md](../pattern/engine/MODELS.md) before staffing and choose capability and effort
for each assignment's reasoning need and consequence. The project Director is
typically Max; most managers are Large, and none is Max merely because its parent
is. Neither blanket strongest inheritance nor blanket cheapest selection is policy;
actual tool-selected values, or explicit unknowns, are retained. The Small recorder
becomes one coordinated, indexed [Recorder](../pattern/engine/RECORDER.md) route: direct
from a manager only where the host supports it, otherwise through the assigner.
Workers report to their manager and never write canonical state independently.
**Why/tradeoff:** Inherited strongest models spend judgment capacity where none is
needed, while a fixed cheap default under-serves hard manager work. A recorder per
manager would recreate the competing-ledger problem that STATE forbids. The cost is
a deliberate selection and receipt for every assignment.
**Regression cases:** A manager's clerk or recorder does not inherit the manager's
model and full history when explicit selection exists; a prompt saying "Small" is
not recorded as a selection; a manager on a host without direct agent messaging
reaches the shared Recorder through its assigner instead of starting its own; a small
task goes to a worker rather than to a manager editing files.

**Superseded in part, October 22:** "Strictly non-worker" no longer means every
request is routed. The Director first works out what is being asked and sizes the
response to it. An answer that fits in the reply (reshaping material the user
supplied, a question, a status, a judgment) is given directly in that turn, with no
workers, recorder, capture, or setup check. The absolute "no direct-execution or
direct-helper exception for small tasks" is removed; the non-worker boundary still
governs work that is substantial, parallel, needs a separate context, or changes the
project. The startup setup check now runs in the background when the Director first
staffs work and never delays an answer, and capture applies to requests that start
work.
**Why/tradeoff:** Delegation exists to keep the conversation fast and the Director's
context clean while real work runs; it is never the goal. Hosts tell models to
follow instruction files exactly, so an absolute rule with no stated purpose
outranked the model's own reading of the request. Rules now state their purpose so
the Director can reason from it. The cost is a judgment call at the boundary, which
the Director is there to make.
**Regression case:** A user pasted a director prompt and asked for it back as a few
bullets to read on camera. The Director staffed a writer and a recorder and ran the
startup check: two agents and several minutes for an answer that fit in one reply.
The user's correction: the pattern's goal is not to make everything take ten times
longer, and the Director must be smart enough to see when it can just answer.
**Status:** decided and implemented in [PATTERN.md](../pattern/PATTERN.md),
[DIRECTOR.md](../pattern/engine/DIRECTOR.md), [REQUEST_MANAGER.md](../pattern/engine/REQUEST_MANAGER.md),
[STATE.md](../pattern/engine/STATE.md), [PROJECT.md](../pattern/PROJECT.md), and the
[INSTALL.md](../pattern/INSTALL.md) hook; not yet verified in a fresh installed session.

**Refined, October 23:** The main project Director answers promptly and establishes
enough intent and need to choose a useful next step, then delegates substantial
analysis **and coordination before doing that active work in the main conversation**.
A bounded child director, normally the Request Manager, owns detailed planning,
staffing, supervision, evaluation, and rework. Substantial independent analysis can
use a worker with the optional bounded-analysis responsibility or a matching
maintained role. This makes the earlier attention-protection purpose operational;
it supersedes treating analysis delegation as merely optional when the main
Director is already occupied with substantial analysis or coordination. The
October 22 direct-in-reply exception remains: a useful answer that fits in the
reply needs no compulsory staffing or intake layer.

**Why/tradeoff:** Avoiding implementation alone leaves a Director free to spend an
extended turn doing the manager's analysis and coordination, delaying the user's
next conversation. Keeping detail is valuable; actively doing that work in the
main conversation is the problem. Managers and the shared Recorder retain full
recoverable detail, while the Director keeps a compact view, access to the detail,
selected critical evidence, cross-outcome judgment, authority, and user acceptance.
The cost is an explicit boundary decision before substantial work, with actual
host capacity and scheduling limits disclosed rather than disguised as availability.
No arbitrary response-time SLA, simultaneous-inference promise, new role value,
or mandatory intake actor is introduced.

**Concrete regression:** A user adds an identity-design request while another
outcome is active. The Director acknowledges and determines the needed result,
entrusts detailed design analysis and coordination, and can address a later status
or intent correction without first finishing that analysis itself. The existing
owner receives relevant steering and retains full detail. A short request to
reshape supplied text still gets its answer directly in that reply. A selected
critical-evidence review remains Director judgment, rather than wholesale local
supervision returning to the main conversation.

**Status and verification boundary:** Decided and implemented in
[DIRECTION](../pattern/engine/DIRECTION.md#direct-without-becoming-the-worker),
[DIRECTOR](../pattern/engine/DIRECTOR.md), [REQUEST_MANAGER](../pattern/engine/REQUEST_MANAGER.md),
and [STATE](../pattern/engine/STATE.md). Package/link checks establish structural
consistency only. Prompt replies, effective delegation, steering incorporation,
and recoverable full detail still need the actual host observations in the
[manual scenarios](DESIGN_NOTES.md#refinement-scenarios--october-23-2026).
Revisit if substantial work still occupies the main conversation or delegation
adds friction to answers that fit directly in a reply.

**Refined and superseded in part, later October 23 — portable staffing policy:**
The October 21 per-assignment selection decision stands. This supersedes the
instruction to map concrete tier selections centrally into PROJECT during
installation, and PROJECT's role-to-model table: those invited a prior host's
selections to become permanent defaults. Durable capability/effort needs and valid
user/project preferences belong in PROJECT; host controls and constraints are
observations scoped by host/time. Concrete requested and effective settings belong
in dispatch evidence, with unknowns explicit. Reusable guidance prescribes no
vendor/model IDs, fixed catalog, price claim, or newest-model choice.

**Why/tradeoff:** A project can move from Host A to Host B, or encounter changed
model generations/options on the same host, without a new user policy decision.
At the next relevant staffing, every staffing actor resolves model and effort
from exposed current controls and chooses a context mode supporting them. Supported
remapping is agent-owned maintenance within existing authority, not a user-facing
gap or repeated confirmation. This adds a bounded refresh when needed, not routine
catalog sweeps, comparative jobs, or external research. Unsupported controls,
unknown effective settings, and genuine consequential choices remain visible;
host/user restrictions and spending authority are unchanged.

**Concrete regressions:** A Host A receipt does not prescribe Host B's identifier;
a changed option prompts supported remapping instead of a frozen role default;
a clerk does not silently inherit its parent's strongest model/effort; an
unsupported override is recorded with a suitable allowed route or a real blocker,
never invented settings. See [MODELS](../pattern/engine/MODELS.md#projecthost-mapping),
[PROJECT](../pattern/PROJECT.md#durable-capability-and-authority-policy), and the
[manual cases](DESIGN_NOTES.md#portable-staffing-and-acceptance-scenarios--october-23-2026).
**Status:** Decided and implemented in guidance/templates; behavioral effects
remain unverified. Revisit if stale observations still become assignment policy
or refreshing supported controls still creates avoidable user work.

**Superseded in part, October 24 — PROJECT is enduring project context:**
The October 23 scoped-observation/cache approach did not go far enough. Its
PROJECT template still invited host/time, tools, slots, permissions, context,
inheritance, return routes, and conversation setup results. Dating such a snapshot
could still bias a future actor. PROJECT now holds enduring context, authority,
maintained responsibilities, and canonical policy/state/evidence locators. It has
no environment-observation category, concrete model/provider/version table, current
agent/team roster, or continually filled setup fields. No replacement automatically
loaded environment definition or cache is introduced. The per-assignment selection
and current-control requirements stand.

**Why/tradeoff:** One project can move among coding systems, teammates, and model
generations over months. A prior observed four-slot host must not constrain a host
that now reports 21, and replacing four with 21 would repeat the defect. Resolve
relevant capabilities from the actual host when needed, with uncertainty explicit
and no exhaustive catalog sweep. Retain recovery-relevant observations with the
actual assignment, receipt, or activity evidence; observations never grant
permissions or become operating authority. This keeps useful history while taking
away a tempting startup shortcut.

**Preserved boundaries:** Durable user-authorized budget and authority constraints,
stable project responsibility IDs, and actual product requirements remain binding
and distinct from runtime observations. A retained host-adapter locator is
conditional on applicability and current capability validation. Installation source,
revision, baselines, setup/acceptance results, and verification history live in the
authoritative receipt; PROJECT points there. Upgrade preservation keeps exact old
material in verified backups/history and relevant recovery evidence outside
startup, rather than deleting history or silently promoting it back into policy.
Unclear authority must be resolved before weakening a purported restriction.

**Concrete regressions and status:** Four slots on an old host versus 21 on the
current host, and changed models/agents months later, require current discovery;
an explicit budget ceiling, release gate, or maintained role requirement survives.
Decided and implemented in the [PROJECT template](../pattern/PROJECT.md),
[MODELS](../pattern/engine/MODELS.md#projecthost-mapping), [assignment bootstrap](../pattern/engine/ASSIGNMENT.md),
[setup](../pattern/INSTALL.md), and [update preservation](../pattern/engine/references/UPDATES.md#compare-before-replacing),
with their direct callers and public copy aligned. Static package/link checks and
manual contract review are separate from actual cross-host behavior; the
[regression scenarios](DESIGN_NOTES.md#enduring-project-context-scenarios--october-24-2026)
remain pending. No runtime/schema change is needed. Revisit if another loaded
context file becomes an environment cache or preserved evidence is treated as
current configuration.

**Refined and superseded in part, October 27 — choose the intended deliverable first:**
The October 22/23 fast-answer purpose stands. The direct-answer exception applies
after choosing what would fulfill the user's intended outcome; a shorter reply
must not shrink that result. Concrete product problems and desired improvements
can imply actionable intent in tentative conversation. Context decides: neither
uncertain wording nor a request for judgment forces discussion or action. Explicit
consultation remains conversational, and casual observations do not automatically
start implementation.

When the outcome requires an artifact or changed behavior, delegate bounded,
reversible execution through the maintained roles and existing authority. Clear
direction leads to a reviewable implementation; a material unresolved design
choice calls for rendered alternatives or a prototype before asking for a choice,
when feasible within that authority. Visual/interaction work needs rendered
designs or working behavior. A recommendation, acknowledgment, or status reply
does not complete the underlying work. Genuine limits, publication gates, and
proportionate verification remain binding.

**Why/evidence:** A reported nested-board navigation/search problem ended with a
written recommendation and no investigation, rendered alternatives, or prototype.
The inspected direct-answer wording broadly listed questions and judgments and
omitted an intended-deliverable gate. Treating that gap as the cause of the
reported response remains a hypothesis: the affected installation and execution
trace were not inspected. The tradeoff is contextual judgment at intake rather
than a keyword classifier or automatic implementation of every observation.

**Decided and implemented:** [DIRECTION](../pattern/engine/DIRECTION.md#choose-the-deliverable-before-the-direct-answer-exception)
owns the rule; [DIRECTOR](../pattern/engine/DIRECTOR.md) and
[REQUEST_MANAGER](../pattern/engine/REQUEST_MANAGER.md) point there;
[ASSIGNMENT](../pattern/engine/ASSIGNMENT.md) carries the chosen deliverable and
required review evidence. Exact source evidence is stored privately, separate
from public guidance. The [regression cases](fixtures/deliverable-first/README.md)
cover nested-board search, clear implementation, unresolved design, explicit
discussion, casual observation, completion, and publication gates. Static checks
and case review are recorded in [validation notes](DESIGN_NOTES.md#deliverable-first-scenarios--october-27-2026);
fresh-host behavior remains unverified. **Revisit:** intended artifacts still
become prose-only recommendations, or consultation and casual observations begin
triggering unwanted execution.

## R3 — Retain commitments by default, preserve original intent

**Problem:** Short/creative work can still carry commitments, corrections, and
partial completion that must survive tomorrow; project type is a poor retention test.
**Accepted decision, October 16:** Use tracked state by default, with lean as an
explicit option. This supersedes choosing retention mode by project type. Lean
omits a complete-backlog promise; creative work does not imply lean mode.
Existing trackers stay canonical.
**Why/tradeoff:** Small persistence receipts add overhead, but prevent entrusted work
and tiny steering from disappearing. Whole exact user messages remain separate
from interpreted titles, scope, acceptance, and decisions; attachments matter too.
**Consequence:** Independent outcomes are independently visible, with sources and
history intact. Status is not liveness, completion is not release, and files do not
wake agents. See [STATE.md](../pattern/engine/STATE.md). **Revisit:** evidence that a bounded exploration
needs a different retention promise; do not silently cancel work when changing mode.

## R4 — Relationships must support several orientations

**Requirement:** Projects may coordinate with peer projects. Relationships must
support different ownership and dependency arrangements without mandating a workflow.
**Current design:** Separate source/provenance, optional grouping/decomposition,
explicit required completion dependencies, and ownership handoffs. Directed links
can express these without a universal parent tree, graph database, or central registry.
**Why:** Shared source or a parent label cannot establish every completion rule.
Informational backreferences may be reciprocal; only real blocking edges need
cycle/unresolved-dependency checks. A director can derive required links within scope.
**Consequence:** Flat request bundles can support graph-shaped relationships;
optional umbrellas are useful only for real whole-scope commitments. See
[REQUEST_RELATIONSHIPS.md](REQUEST_RELATIONSHIPS.md). **Revisit:** a concrete
scenario cannot be represented without forcing ownership or completion into a tree.

## R5 — Preserve the four-outcome restart truth across ownership boundaries

**Regression story:** One message asks for a folder, research, a new repository,
and a complex app. The first three finish; another project's director acknowledges
the app deliverable. Tomorrow the answer must remain “three complete; the fourth
waits on that owner,” with original context and last verified status/time intact.
No untying, reopening, or rebundling completed siblings should be necessary.
**Current design:** Receiver owns its requests and execution; source retains its
commitment and judges the agreed returned outcome, without mirroring a remote task
tree. Project/request IDs are identity; current roots/paths are locator hints.
**Why/tradeoff:** Ownership stays clear while source observations may be stale.
Attempted send, acknowledgment, execution, return, and acceptance are distinct.
**Consequence:** Acknowledged external supervision lets the source go offline with
a durable waiting commitment; it need not manage receiver descendants. It retains
acceptance authority, with no promised wakeup. Unacknowledged sends do not qualify.
Cancellation/removal preserves a non-success/revised-scope disposition, not fabricated
success. Details and the restart table are in the [relationship design](REQUEST_RELATIONSHIPS.md).
**Revisit:** lost acknowledgments, inaccessible source content, moved locators, or
contradictory ownership expose a specific resolution/transport requirement.

## R6 — Standardize request folders without losing recovery guarantees

**Problem:** A flat request file can preserve state but leaves request-local assets
and evidence at separate locations. Relocating the request then requires several
references to remain consistent.
**Accepted direction, October 16:** Standardize one folder per actionable request
and implement flexible ownership/dependency links.
Keep seven lifecycle states mapped to pending/working/archive, exact shared source
bundles, stable project/request identities, and distinct relationship meanings.
**Why/tradeoff:** Local assets/evidence should travel with a request, while shared
originals and large outputs remain canonical through references. Moves require
resolution, collisions/stale-write protection, retry identity, journaling, and repair;
no multi-file atomicity or automatic migration is implied.
**Consequence:** A versioned helper now implements this direction; disposable
verification evidence is recorded in [DESIGN_NOTES.md](DESIGN_NOTES.md). Legacy stores remain intact and are never silently converted. Transport, liveness,
authentication of supplied proof, and foreign writes are outside the helper.
The [storage comparison](REQUEST_STORAGE_COMPARISON.md) explains the alternatives.
**Revisit:** preservation, recovery, dependency, or ownership fixtures expose a gap;
revise the bounded implementation, not the accepted independent-outcome requirement.

## R7 — Keep the reasons durable, current, and revisable

**Requirement:** Preserve the reasons behind formative decisions so future work
can evaluate a change without repeatedly rediscovering earlier tradeoffs.
**Current practice:** This is the canonical public explanation of WHY; contracts
define behavior, detailed design docs explain mechanisms, and
[DESIGN_NOTES.md](DESIGN_NOTES.md) records validation scope and open gates.
**Why/tradeoff:** A coherent explanation is more useful than a growing transcript,
but refactoring must not erase the evidence or reasons for changed decisions.
**Consequence:** Repository authors read relevant rationale before changing design;
this is authoring guidance, not automatic installation of director behavior here.
**Revisit:** new formative evidence changes a decision, exposes a contradiction,
or shows that guidance is unreachable or no longer improves behavior.

## R8 — Separate the installed method from its workshop

**Requirement:** Install only the method. Public development documentation and
tests support maintenance but are not target-project installation payload.
**Chosen layout:** Keep one repository to prevent rationale and method drifting,
but isolate a self-contained `pattern/` package from `development/` rationale
and tests. The layout is an implementation choice. Root README routes each
audience explicitly.
**Why/tradeoff:** The workshop remains shareable and refactorable while an agent can
download/install just the method. `pattern/manifest.json` selects copied payload;
guides and authoring AGENTS are not target instructions. Local adoption is a separate,
explicit setup choice; a source checkout alone is not installation.
**Consequence:** Generic rationale and tests remain public and outside the
installation payload. Raw conversations and internal references remain private.
**Revisit:** a boundary check reveals an external package dependency, accidental
copying of authoring material, or unintended publication of private evidence.

## R9 — Make attention and active supervision visible without decoration

**Problem:** A real question or user-only action can disappear among progress
updates. A polished update can also hide that supervision has stopped. A director
label can imply an installation that was never checked.
**Initial decision, October 17:** Use three semantic markers: `❓` for actionable
user questions/decisions, `🖐️` for user-only actions, and `🎬` for director identity
after a current-conversation installation and role check. Other expressive emoji
remain discretionary; special markers are sparse, not routine status decoration.
**Accepted refinement, October 17:** Add `📋` for the periodic situation-report
block, using the exact heading **📋 SitRep**. This supersedes the earlier unmarked
`Sitrep` opener and its capitalization. Four markers now distinguish checked
director identity, user questions, user-only actions, and periodic report blocks.
The checked director retains its `🎬` reply prefix; `📋 SitRep` labels a block
inside that reply. Reserve the heading for periodic reports so readers can scan
or skip them; it is not a prefix for every progress sentence. Cadence, evidence,
continued supervision, and exit requirements are unchanged.
**Reported friction, October 19:** Full reports appear too frequently during ordinary
director exchanges. The frequency is reported; its cause has not been established.
**Hypothesis:** Tying report formatting to meaningful changes and stricter host
timing may encourage a full block on each reply.
**Accepted refinement, October 19:** A SitRep is a useful periodic overview during
ongoing supervision, not a default block on every director reply, worker return,
or status change. Use ordinary prose for discussion, direct answers, and brief
progress; communicate meaningful changes promptly. Meaningful ordinary updates
already satisfy the cadence, so do not append a redundant report. A full overview
helps after several minutes of otherwise quiet work or when multiple developments
or workstreams benefit from one combined view. This supersedes interpreting the
earlier cadence as requiring a full report with each change or host update.
The five-minute silence limit and stricter host timing remain; stricter timing
calls for concise progress, not a full report at each interval.
**Why/tradeoff:** A small vocabulary makes attention needs recognizable. One marker
can introduce several numbered questions. A checked identity exposes startup truth,
while its limited meaning avoids implying tested behavior or live execution.
**Consequence:** [PATTERN.md](../pattern/PATTERN.md) now defines the markers and
separates timely progress updates from periodic overviews while managed work
continues. Reports cover held work and current action/next proof, using actual
observations.
They remain intermediate commentary; existing handoff, blockage, and interruption
boundaries still apply. A Small recorder returns setup facts under
[STATE.md](../pattern/engine/STATE.md); the director resolves its actual role. The existing
[PROJECT](../pattern/PROJECT.md) and [installation](../pattern/INSTALL.md) receipts
supply the context without a new state engine or runtime requirement for lean or
an existing tracker. The cadence refinement is implemented in the contract and
package/site summaries. Link and package checks do not establish fresh-session
behavioral compliance; the [manual scenarios](DESIGN_NOTES.md#manual-scenarios-before-adoption-claims)
remain proposed checks, not executed trials.
**Regression cases:** A source checkout or inherited worker cannot display director
identity. A correctly wired lean installation can pass without the bundled helper.
With three workstreams, an active export, returned review, and waiting packaging
all remain visible; the director evaluates the review and keeps supervising after
its report. User questions stay actionable, and a host question tool is not echoed
as a second question in chat. The heading identifies a periodic report without
turning ordinary progress sentences into reports or suggesting that saved state
proves live workers. Rapid exchanges and worker returns do not each get a full
block; useful ordinary host updates satisfy timing without duplication. Quiet
managed work still gets a timed overview, and meaningful changes are communicated
promptly while supervision continues. **Revisit:** real use shows missed attention
needs, noisy repetition, false setup claims, or supervision ending at a status report.

**Superseded in part, October 21:** `🎬` belongs only to the checked **project**
Director. With Request Managers assigned as `Role: director`, the October 17 wording
would have given every bounded child director the badge. Only the project Director
runs the startup check; managers receive its facts in their bootstrap. Managers and
other bounded actors use an assigned name and unique marker, such as `🐙 Contract —`,
from one Recorder-maintained roster and rotation cursor: reserved before dispatch,
bound to the actual handle, kept through resume and pending reports, and released
only when no late return can collide. `🎬`, `📋`, `❓`, `🖐️`, and equivalent variants
are never allocated; exhaustion uses another glyph or a unique text label. A marker
grants no role or authority. See [IDENTITIES.md](../pattern/engine/IDENTITIES.md).
**Refinement, October 21:** Answering the user is not claiming completion. A
conversational or status reply can continue while obligations stay open, and it
closes nothing. Exit accounting applies before claiming completion or ending
supervision. If a final reply actually ends the host's supervisory turn, outstanding
work is checkpointed and the continuation limit or acknowledged handoff is stated,
without promising that children stay live; see the
[exit rules](../pattern/engine/DIRECTION.md#account-for-the-outcome-before-exiting).
**Regression cases:** A resumed manager and parent summaries keep its marker; no
manager prefixes a reply with `🎬`. Two reservations serialized through the shared
Recorder never receive one marker. A status question mid-outcome is answered while
the bug-to-customer-follow-up outcome stays open. **Verification limit:** Allocation
is instructional and serialized by one Recorder route; no helper command or
machine-enforced reservation exists. A package check covers only the static pool.

**Refined, October 23:** [IDENTITIES](../pattern/engine/IDENTITIES.md) now owns the
canonical choice policy: a short, memorable, Capitalized name, bold in human-facing
output, and a character that naturally suggests the assignment. Soft overlapping
affinities can draw on animals, flora, tools, or buildings; they do not encode a
fixed role, model tier, status, or authority. A beaver can suggest building or
editing, while a tree or flower can suit design. These are illustrative choices,
not a mandatory allocation table. The static pool expands compactly without
separate category pools.

**Why/tradeoff:** A purely sequential glyph can be distinctive yet feel unrelated
to the work. Semantic fit makes actors more memorable and adds character without
requiring a taxonomy for every possible assignment. Fit guides selection first;
availability and rotation resolve suitable options through the same active/recent
roster and **one cursor**. When preferred choices are unavailable, broaden to a
sensible fit, then use a distinct additional glyph or unique text reservation if
needed. Names and equivalent rendered marker variants cannot collide among active
or still-reporting actors. Reserved `🎬`, `📋`, `❓`, and `🖐️` variants keep their
existing attention meanings. Resumed identities stay stable even when another
character would now appear more apt, and project-owned pool customizations survive
updates. No runtime service, new record schema, or machine-enforced allocator is
introduced.

**Regression cases:** A video editor can be 🦫 **Cutter** or 🦀 **Cutter**, but two
live actors cannot share that name. A designer can be 🌳 **Willow** without all
designers becoming plants. Reading/email, notifications, and cleanup each admit a
natural choice without a new category or cursor. Two simultaneous reservations use
the one serialized roster; a preferred glyph in use triggers another suitable
choice. A resumed assignment and a late return retain their original marker/name,
preventing confusion with a new actor. Exhaustion never borrows a reserved symbol.

**Clarified, October 23:** The existing identity-preservation rule explicitly
includes the assigned emoji and bold name in all parent, Director, and manager
summaries and SitReps, as well as actor updates and returns. A summary that keeps
only the name drops required formatting; [IDENTITIES](../pattern/engine/IDENTITIES.md)
now says so directly. This is a wording clarification, not a new allocation rule
or a verified live-behavior claim.

**Status and verification boundary:** Decided and implemented in IDENTITIES and
[IDENTITY_POOL](../pattern/IDENTITY_POOL.txt), with references/examples aligned in
[DIRECTION](../pattern/engine/DIRECTION.md), [ASSIGNMENT](../pattern/engine/ASSIGNMENT.md), and
the [package guide](../pattern/README.md). Static package checks establish pool
uniqueness, reserved-symbol exclusion, and payload/link closure. The
[manual scenarios](DESIGN_NOTES.md#refinement-scenarios--october-23-2026) still await
behavioral observations of fit, reservation, collision handling, and resume. Revisit
if selections feel forced, categories harden into authority signals, or rotation
and late-report protection diverge across owners.

## R10 — Assign roles explicitly; preserve project ownership across entry routes

**Accepted decision, October 17:** A new project conversation defaults to that
project's director regardless of who opened it. Explicit user/assigner roles
supersede the default. Every bounded delegated assignment names worker/director
role, outcome, scope, and authority; reviewers and recorders are bounded worker
specializations. Missing delegated roles require clarification with the assigner,
not inference from ancestry, tool type, or inherited history. This supersedes the
earlier rule that all agents launched by agents defaulted to workers at every depth.
**Why/tradeoff:** Entering another project should reach its accountable director,
while a bounded worker must not acquire director authority merely by inheriting
context. Explicit child directors can coordinate an entrusted scope; worker
subdelegation never expands authority. The installation/badge check is independent.
**Implemented:** [PATTERN.md](../pattern/PATTERN.md) and the
[installation hook](../pattern/INSTALL.md) carry the revised contract.
**Regression cases:** A session opened in a peer project by another director serves
as that project's director by default. An explicit worker inheriting director history
stays a worker. An explicit child director coordinates only its granted outcome.
A delegated assignment with no role seeks clarification before role-specific action.
**Verification limit:** Document/package checks do not establish actual fresh-session
role behavior. Revisit if ambiguous assignment boundaries still cause role drift.

**Refined, October 21:** Role values stay exactly `worker` and `director`; no new
value such as `Role: request-manager` is sent. Responsibilities ride on them: a
Request Manager is `Role: director` bounded to one complete outcome, with local
planning, staffing, evaluation, and rework explicitly delegated; the Recorder,
reviewers, specialists, and bounded analysis are `Role: worker`. Assignments now
also name the maintained responsibility and its definition locator from the
project's canonical role index, and supply project-wide guardrails, selected role
references, model/effort, identity, and Recorder route. The actor, and any
descendant, reads and acknowledges that package before acting. Missing or
conflicting applicable definitions return for resolution, with no silent generic
fallback; unaffected work continues. A manager label, tier, or marker grants no authority.
**Why/tradeoff:** Fresh generic specialists forget an organization's guardrails and
prior learning. Tuning belongs in the maintained index and references, not in a
rewritten generic manager per domain; the cost is adoption mapping before affected
staffing. Two role values avoid inventing a host or store enum; the fork's rename
changed one value's spelling, not the set.
**Implemented:** [ROLES.md](../pattern/engine/ROLES.md), [ASSIGNMENT.md](../pattern/engine/ASSIGNMENT.md),
[role resolution](../pattern/engine/PATTERN.md#resolve-the-assignment-role), and the
role-index mapping in [PROJECT.md](../pattern/PROJECT.md) and
[INSTALL.md](../pattern/INSTALL.md). Specialist entries in ROLES are illustrative.
**Regression cases:** A maintained release role with a material "must not" guard is
supplied and acknowledged before any release step; no generic engineer substitutes
for a matching maintained role; a missing index stops only the affected staffing; an
explicit worker labeled "manager" gains no director powers.

**Refined and superseded in part, October 23:** Installation and upgrade establish
one small common [PATTERN bootstrap](../pattern/PATTERN.md), whose locally adapted
pointer reaches one project-owned canonical role index. Explicit assignment role
and maintained responsibility select standalone definitions/references before
action. Only an unassigned project conversation defaults Director; malformed
bounded assignments clarify, never default. Director/manager policies formerly
in the common PATTERN move to [DIRECTION.md](../pattern/engine/DIRECTION.md), loaded by
[DIRECTOR](../pattern/engine/DIRECTOR.md) and [REQUEST_MANAGER](../pattern/engine/REQUEST_MANAGER.md).
Worker boundaries and optional analysis have their own files. This supersedes
having every worker read the full Director-heavy contract or the hook's abstract.
The October 22 fast-answer decision in R2 remains intact.

**Reported evidence versus hypothesis:** An adoption report described an installer
appending its own abstract to already enormous startup instructions, with poor
role separation. That report does not establish the other host's exact loaded
context or prove a universal cause. Inspection of this candidate did establish
that its hook required every actor to load Director-heavy PATTERN, and that an
existing role-index requirement alone did not require standalone definitions or
an audit of inherited globally loaded duties. The hypothesis is that explicit
installation ethos and a real common/selected-role split prevent that recurrence.
One fresh assigned Codex trial below now supports the selected-role loading route;
broader host behavior and prevention of recurrence remain unproven.

**Decided and implemented:** [INSTALL](../pattern/INSTALL.md),
[UPDATES](../pattern/engine/references/UPDATES.md), and the self-contained
[STARTUP procedure](../pattern/engine/references/STARTUP.md) audit the entire loaded
startup chain, preserve shared authority and exact specialist instructions at
maintained destinations, and leave a single active default and index. An installing
agent need not already be a Director. Existing entries pointing only to startup
sections are repaired in the same index, not discarded. New or revised recurring
roles need standalone definitions, index registration, and checked reachability
before staffing under [ROLES](../pattern/engine/ROLES.md#maintain-standalone-definitions-and-one-index).
The index is generated project-owned context, excluded from upstream payload;
its bootstrap pointer survives updates as an adaptation. No runtime/schema change
or arbitrary word-count gate is introduced.

**Regression cases and verification boundary:** A fresh assigned reader, writer,
reviewer, or tester receives the common bootstrap and selected maintained definition
before acting; an incomplete delegated assignment cannot become Director. A newly
registered role is discoverable through the same index. An upgrade of oversized
startup instructions removes relocated specialist duties from common loading while
preserving their exact rules and shared authority. Package fixtures check manifest
boundaries, selected-file reachability, and common/Director separation; they do not
prove the host loaded those files or that an actor obeyed them. STARTUP specifies
separate real-host trials and requires unrun trials to remain pending. Revisit if
observed reads or actions still bypass role definitions or the audit loses a rule.

**Verified, October 23 (static/fixture scope):** 38 development tests, including the
common/selected-role and generated-index package regressions, and 8 site tests
passed. The site build retained its 10-file public allowlist; a headless 390px
check showed no horizontal overflow. These checks do not establish fresh-session
role selection or real host read order.

**Verified, October 23 (one fresh assigned Codex trial):** A fresh explicitly
assigned test worker received the host-supplied AGENTS hook, then explicitly read
installed PATTERN, followed its canonical role index to the standalone selected
definition and required references, and acknowledged those before its first review
action. This is observed assigned-role startup behavior; PATTERN was read through
the hook, not automatically injected by the host. The trial does not establish
unassigned/default startup, malformed-assignment handling, discovery of a newly
indexed role, another host's behavior, or any future session's compliance. Those
trials remain pending; the result does not turn static checks into behavioral proof.

**Later October 23 scope clarification:** The whole-chain audit and fresh-host
trial requirements above remain the first-install and affected-change procedure.
Routine updates reuse still-applicable evidence and expand checks only when their
upstream delta or local drift requires it; see the dated supersession in
[R11](#r11--update-from-a-pinned-public-source-without-replacing-project-state).
This does not waive actual role loading or preservation of project-owned rules.

**Clarified, later October 23 — conversation-start prerequisite:** The prior hook's
“before role-specific action” wording left room to investigate or plan the user's
task before loading the role. The [installation hook](../pattern/INSTALL.md) and
[repository hook](../AGENTS.md) now require PATTERN and the selected definition and
required references at conversation start, before substantive task investigation,
planning, delegation, or changes. A brief acknowledgment may come first; the actor
then addresses the original request in the same turn, without requiring a greeting
or extra confirmation. **Regression case:** The first message contains a real
multistep task and no hello; role loading still precedes work on that task.
**Status:** Instruction clarification implemented; behavior has not been freshly
verified, and the hook supplies no host-enforced loading guarantee.

**Refined, October 24 — returned-result startup dependencies:** A reported Claude
Code plain-question test read task files in the same step as PATTERN at low,
medium, and high effort, resolving Director only afterward. The October 23
conversation-start clarification above changed the hook, but left PATTERN's
"before role-specific action" wording unchanged and had no fresh behavior trial.
That earlier assigned Codex observation still supports only its stated assigned
route; it does not establish the unassigned default or Claude behavior.

**Decided and implemented:** The [small hook](../pattern/INSTALL.md) now requires
the first invocation to read only PATTERN and wait for its result.
[PATTERN](../pattern/engine/PATTERN.md#complete-startup-before-task-work) owns the remaining
dependencies: canonical-index result, selected-definition results, all required
references/guardrails, then a brief completed-package acknowledgment before task
I/O or a substantive answer. Known independent startup references may batch after
discovery; task work may not share their invocation or assistant tool group.
Read-only inspection and direct answers have no role-loading exception.
[DIRECTION](../pattern/engine/DIRECTION.md#check-installation-before-using-director-identity)
keeps background setup/identity checks separate, preserving R2's direct-answer
purpose after role loading. This is an instruction-guided route, not automatic
file injection, a runtime, or host enforcement. Malformed delegated assignments
still clarify without falling into the Director default.

**Why/tradeoff:** "Before" did not specify the tool boundary. A model can emit
PATTERN and task reads in one generation, even when the host streams a PATTERN
result between their executions; the task call then cannot reflect that result.
Explicit dependencies cost several short startup turns and the actual selected
reference context. They avoid pretending that a file's presence or a role label
means its instructions were loaded. Keep the hook a pointer and load only selected
responsibilities; do not regain speed by skipping mandatory references.

**Concrete regression and observed evidence:** A fresh unassigned question asks
for a value in TASK.md through the host's real startup entrypoint. Both observed
baseline low/medium Claude sessions read PATTERN and TASK in the first assistant
group, answered before index loading, and later skipped required Director
references by treating a direct-answer rule as an exception. An initial candidate
at low effort and the final frozen candidate at low/medium/high instead returned
all eleven required startup-file results before a separate TASK read, then
answered directly. These six bounded sessions copied the actual manifest base
payload and real Director/reference chain with generated project context; they
used Read-only tools, the same native instruction-import route, and one neutral
task. The allocation was adaptive: baseline-high was omitted after reproduction
to test the final candidate at all three requested efforts.

**Verification limit and remaining gap:** Primary read ordering passed in those
four candidate observations. None produced the required post-load completion
acknowledgment or fixture canary before task inspection; early role/loading text
is not that acknowledgment. Thus full startup compliance is not verified. The
canary was a fixture diagnostic, not a production token policy. Effective model
was reported by the CLI; efforts were requested through accepted flags, with no
independent effective-effort field exposed. This is one controlled host/model
sample with restricted tools, not a general reliability result, shell-batching
trial, downstream installation, or fresh Codex test. The
[validation notes](DESIGN_NOTES.md#startup-dependency-trials--october-24-2026) and
[STARTUP procedure](../pattern/engine/references/STARTUP.md#verify-the-startup-dependency-barrier)
retain separate read-order and acknowledgment checks. Revisit if real task reads
still cross a startup dependency or the acknowledgment remains unreliable; do not
report a later wording change as behavior already tested.

**Later October 24 — testing the loading mechanism:** A separate eighteen-session
exploration compared a tiny four-file selected-role chain with a flattened copy
of the same substantive selected-role instructions. Every condition required the
first invocation to read only PATTERN. Advisory links alone failed to finish the
chain before task inspection at all three requested efforts. Three additional
sessions with an ordinary, untimed instruction to read the next file at every
hop also failed. One treated the next-file instruction as unrelated to the user's
task and skipped it. The first-file requirement therefore did not automatically
make downstream references prerequisites in these observations.

Explicit per-hop read/result/before-task barriers, one global transitive
completion rule in the initial AGENTS hook with advisory downstream links, and
their combination each completed the chain in the low/medium/high observations.
The global rule's location was the initially loaded hook; moving it elsewhere was
not tested. Ordinary imperatives were added after recognizing that links alone
were not a fair comparison with an instruction to read. This refinement supports
the value of an explicit prerequisite, while not isolating the separate effects
of before-task wording, returned-result waits, and tool-group separation.

The flattened selected-role control also passed and used two Read groups rather
than the successful chains' five. This is a small routing comparison, not a
production-package cost or latency benchmark. It supplies no need to flatten all
roles or load irrelevant policies. **Architecture decision:** retain the existing
common bootstrap, canonical index, and selected standalone definitions, with the
explicit dependency barrier already implemented in
[PATTERN](../pattern/engine/PATTERN.md#complete-startup-before-task-work). That candidate
also passed the separate actual-package eleven-file read sequence at all three
requested efforts. No production rewrite or further operational wording change
followed from the mechanism study.

**Evidence boundary:** These are eighteen exploratory observations, one per
condition/effort cell, separate from the six actual-package sessions above.
All successful minimal conditions also used a simple output-prefix rule found
only in the loaded leaf or its inline copy. That output uptake does not establish
general instruction compliance or resolve the actual-package completion-
acknowledgment gap. Native instruction imports were configured, and a built-in
AGENTS capability was also present; the preload path was not isolated. All runs
used the same reported Claude model and Read-only surface, with requested rather
than independently exposed effective effort. No shell batching, another model or
host, repeated reliability sample, or alternative global-rule location was
tested. See the separate
[mechanism validation](DESIGN_NOTES.md#startup-mechanism-comparison--october-24-2026).
Revisit on an observed downstream loading failure; retain result/group evidence
rather than interpreting higher effort, a link, or a role self-label as proof.

**Refined, October 29 — explicit delegation bridge and truthful startup evidence:**
An agent reported interpreting a host rule narrowly because the installed
`AGENTS.md` hook required loading the pattern but did not itself request
delegation. It then performed implementation rather than following the existing
unavailable-worker fallback, and acknowledged a package after a truncated batch.
The report supports what the agent said it did; it does not prove the host actually
prohibited a launch or that every such host interprets referenced instructions
the same way. The missing explicit bridge wording and existing fallback are
directly inspectable; whether the bridge changes host behavior is a hypothesis.

The [installation hook](../pattern/INSTALL.md) now explicitly asks the selected
Director to delegate substantial analysis and project changes to bounded
subagents within higher-priority host rules. This small role-conditional request
does not add a role table or impose delegation on a worker or reply-only answer.
[DIRECTION](../pattern/engine/DIRECTION.md#choose-the-deliverable-before-the-direct-answer-exception)
requires a capability/authority checkpoint before affected delegated work and an
accurate disclosure when a required route is prohibited, uncertain, or unavailable;
it retains the no-silent-role-switch boundary. The selected package acknowledgment
reports reads, not operational capability or setup verification. The shared
[startup bootstrap](../pattern/engine/PATTERN.md#complete-startup-before-task-work)
requires incomplete reads to be recovered before a completed-package claim, or a
specific gap and stop if recovery fails. The update contract now explicitly merges
affected hook changes into existing project-owned entrypoints with backup and
adaptation preservation; engine replacement alone cannot perform that merge.

**Regression cases:** A host permits delegation only when the user's or an
applicable `AGENTS.md` instruction explicitly asks: the selected Director can
evaluate the new loaded hook against that actual rule before staffing. An actual
prohibition remains binding and is disclosed without implementation by the
Director. A truncated required reference is fully reread before the completion
acknowledgment; an unrecoverable read stops affected work. A direct-answer-only
request remains direct, and an assigned worker keeps its own role. An update
preserves customized text inside and outside the hook and never silently appends a
second hook. See [STARTUP's affected trials](../pattern/engine/references/STARTUP.md#static-checks-then-fresh-host-trials).

**Status and limits:** The change is implemented as a local candidate; exact source
evidence is retained privately. Static contract and package checks do not establish
that a host permits delegation, that an agent honors the new instructions, or that
an existing installation was updated. Fresh affected-host trials and downstream
adoption remain separate; preserve failed or unrun observations rather than
describing them as passing. Revisit if the loaded bridge still fails a real host's
delegation boundary or if the checkpoint delays ordinary direct answers.

## R11 — Update from a pinned public source without replacing project state

**Accepted decision, October 17:** Published GitHub `main` is the upstream source of
truth. Explicit agent-driven updates resolve one exact reviewed SHA, back up managed
files and startup wiring, and compare installed baseline/current/incoming bytes.
Normal startup does not silently update. Private setup receipts retain source URL/SHA
and managed-file hashes; old receipts without baselines require safe prior-upstream
comparison or review. No updater daemon, new version registry, or state engine is added.
**Why/tradeoff:** A common upstream makes catch-up possible, but installations contain
project context and adapters that upstream must not overwrite. Schema compatibility
is checked; migration requires its own decision. Baselines describe installed bytes,
not proof of behavior. Partial failures must remain visible rather than claim a new
accepted revision.
**Implemented:** The base manifest includes [UPDATES.md](../pattern/engine/references/UPDATES.md);
[INSTALL.md](../pattern/INSTALL.md) and [PROJECT.md](../pattern/PROJECT.md) route setup
and updates through private receipts.
**Regression cases:** An adapted existing-tracker installation merges upstream role
rules while preserving tracker, context, IDs, raw sources, and unfinished work.
Lean stays lean. Missing baselines block blind replacement. An incompatible helper
schema leaves the existing helper/state intact. Template copies receive fresh local
identities at first use, never cloned initialized state or completed receipts.
**Verification limit:** Static/package checks establish reachable self-contained
instructions; actual target catch-up and fresh-session trials need separate receipts.
Revisit when a real update conflict exposes an insufficient preservation check.

**Extended, October 21:** Preservation also covers the project-owned role index,
definitions and overrides, project-wide guardrails, model/host mapping, and the
private identity roster, cursor, and current activity. The new contracts are base
payload, so lean installs stay self-contained; a live roster is never packaged.
Policy adoption reassigns nothing: open director-owned requests keep owner, handles,
and obligations until an acknowledged handoff, and an update spawns no managers and
seeds no placeholder roles. See [UPDATES.md](../pattern/engine/references/UPDATES.md).
**Decided, October 21:** The rename changed the accept event field and stored
acceptance, so a predecessor store is a different format, not an older revision.
Sharing config 1/store 2 and the `request-bundles` name let this helper open such a
store, reject its records, and still create new ones in it
([observation](DESIGN_NOTES.md#predecessor-store-compatibility)). The store format
is now `director-request-bundles`: a predecessor store is refused before any read or
write, schema numbers stay 1 and 2, and moving from it is an explicit migration
decision, never an update. Reading old fields or an automatic migration was rejected
as needless scope for a new package with no installations.

**Superseded in part, October 21:** Setup and update receipts are committed under
`.director/receipts/` rather than kept private, so an update from any checkout can
compare baselines; only pre-update backups stay local. See
[R14](#r14--commit-the-installation-with-the-project).

**Extended, October 23:** Startup cleanup is part of updates as well as first
installation. Preserve the actual canonical-index pointer, project definitions,
and instruction preservation map through the three-way comparison. A reviewed,
reversible predecessor-policy adoption can replace its old startup default while
leaving its records and authorized tracker workflow intact. That instruction
integration is distinct from migrating its store, which still needs its own
authorization and compatibility work. Never leave two competing active defaults.
See [STARTUP](../pattern/engine/references/STARTUP.md).

**Decided and implemented; superseded in part, later October 23:** Routine updates
are incremental. This supersedes the unconditional whole-chain startup audit and
fresh-host trial matrix added earlier today to every upgrade in R10/R11. First
installation retains the full procedure. An update reviews the relevant upstream
delta and local drift, then selects the smallest sufficient checks under
[UPDATES](../pattern/engine/references/UPDATES.md#select-the-smallest-sufficient-verification).
Structural changes to startup, role routing/defaults, or inherited instruction
placement, and detected defects requiring integration, trigger the whole-chain
[STARTUP](../pattern/engine/references/STARTUP.md) audit. Fresh-host tests cover affected
role/runtime behavior with the relevant subset of trials. A helper-only delta
requires compatibility and affected fixture checks, not fresh startup trials.

**Why/tradeoff:** The previous instructions mandated expensive installation work
for any update, even a prose correction. A reported slow-update experience is not
a measured timing baseline or proof of its sole cause; the unconditional wording
was directly inspectable. Reusing applicable evidence avoids repeating unrelated
work while preserving source pins, manifest boundaries, verified backups of changed
files, baseline/current/incoming and prior-upstream comparisons, persistent local
adaptations, project-owned state/context/mappings/roles/identities, compatibility,
and separate migration decisions. Missing baselines call for safe reconstruction
or review, not automatically a startup audit. Unknown drift never becomes accepted
merely because upstream is already current.

**Entry and failure boundary:** On an explicit update, pin/review current upstream
guidance and use its incremental procedure even if installed guidance mandates an
audit on every upgrade or lacks a protocol. Preserve locally adapted guidance,
project-owned authority and host restrictions; a conflict needs resolution rather
than a silent waiver. [INSTALL](../pattern/INSTALL.md#repeat-upgrade-remove), both
READMEs, and the public agent guide route existing installs here without rerunning
first installation. A compact existing receipt records scope/reason, performed
checks, reused evidence/limits, and prior gaps. Unrelated pending behavioral trials
stay pending without failing a routine update. Newly required blocked checks leave
the affected adoption incomplete; partial updates keep the old accepted revision.
No schema, runtime, or separate approval process is introduced.

**Concrete regression cases:** A prose correction merges into a bootstrap with a
persistent canonical-index adaptation even when current equals installed baseline;
focused preservation/link checks suffice. A helper-only change checks schema and
relevant disposable fixtures without spawning startup trials. A structural
role-routing upgrade performs the full audit and affected fresh trials. A missing
baseline is safely reconstructed/reviewed before replacement, expanding tests only
if that review finds affected behavior. A previously unrun default-Director trial
remains explicitly pending through an unrelated prose update; it is neither newly
passed nor a reason to block that update. An already-current check reports local
drift without silently accepting it. Revisit if scoped checks miss a changed
behavior or routine updates still impose unrelated installation work.

**Verified, later October 23 (static scope):** All 8 package tests and all 8 site
tests passed; the build retained its 10-file public allowlist and `git diff --check`
passed. The revised contracts and entrypoints implement this instruction change.
These checks establish static consistency, not an actual
project update, fresh-agent behavior, or measured update-time improvement. Earlier
trial gaps and the single assigned-worker observation in R10 keep their stated
scope; no new fresh-host trial is claimed here.

**Superseded in part, October 23 — active-project daily discovery:** The earlier
no-startup-fetch direction now permits a tiny metadata-only check arranged by the
checked project Director at the first/next active interaction, no more than once
per rolling 24 hours. Default is notification; an explicit “always update director
pattern” choice supplies project-scoped standing authorization. It does not grant
migration, dependency installation, publication, or destructive overwrite authority.
The safe baseline/current/incoming comparison, backups, compatibility checks,
project ownership, and accepted-receipt boundary remain in force for automatic
updates. [UPDATES](../pattern/engine/references/UPDATES.md#daily-discovery-and-project-preference),
[DIRECTOR](../pattern/engine/DIRECTOR.md), and [PROJECT](../pattern/PROJECT.md) carry this
extension. Global skills retain their native explicit-only invocation controls.

**Why/tradeoff:** A deterministic helper makes a version comparison without a
checking model or software installation. Existing GitHub ref/tree metadata gives
a concrete pinned source and excludes website-only changes without maintaining a
second release registry. The first check may need three short requests to bootstrap
a legacy receipt's package tree; later checks need two. A last-attempt reservation
before network work, a local nonblocking lock, and atomic cache replacement bound
failure and concurrency costs. The Director retains the next eligible time so
same-day turns do not invoke another model/helper merely to read a timestamp.
The cache is machine-local, so another checkout can perform its own daily check;
no global timing/liveness or inactive-project wakeup is promised. Missing runtime,
unknown receipts, corrupt metadata, and HTTP rate limits are visible gaps, not
permission to install software, reset state, or fabricate success.

**Decided and implemented:** A generated, committed `update-policy.json` retains
notify/automatic/off with its user authorization source; absent policy means notify.
The ignored local cache includes failures/interruption. Policy changes preserve
an existing cooldown; switching off makes no network request. The helper returns
an update request, never executes an installer or rewrites receipts/contracts.
Local unpublished deltas retain a published base; later publication still needs
normal review and receipt promotion. No candidate-tree auto-promotion is added.

**Regression cases:** Two active chats race and only one reserves the daily check;
an offline failure suppresses retries for 24 hours; enabling automatic in the
same window does not force another check. A website-only main commit produces no
notice even when the receipt's SHA postdates the last package-changing commit.
A local candidate cannot be advertised as newly published, and automatic mode
leaves adapted PROJECT, role/index/pool, tracker, requests, raw sources, and helper
bytes untouched until the existing update protocol is actually performed.
Corrupt/unknown cache and policy schemas fail closed instead of silently resetting.
**Verification:** Deterministic fixture results and live metadata transport limits
are recorded in [DESIGN_NOTES](DESIGN_NOTES.md#daily-update-discovery--october-23-2026).
They establish helper behavior, not fresh-agent adoption, automatic real-tree
updates, publication, or a host-independent scheduler.

**Clarified, later October 23 — acceptance and pending trials:** An accepted
installation, the current conversation's setup check, and a pending behavioral
trial are separate facts. This clarifies the daily-discovery prerequisite without
changing update authorization or weakening first-install/affected-update checks.
Before announcing an acceptance hold, reconcile PROJECT and its authoritative
receipt. An unrelated pending trial cannot invent a new gate or block daily
metadata discovery after an accepted baseline and successful current setup check.
A genuinely unaccepted baseline, or a check required for the claimed adoption,
retains its actual gate and is never reported as passed.
**Why/regression:** A stale message says adoption awaits acceptance while PROJECT
and the source receipt record acceptance; only an unrelated fresh-conversation
trial remains pending. Reconciliation preserves the accepted baseline, performs
eligible discovery, and reports the trial's narrow uncertainty. See
[DIRECTION](../pattern/engine/DIRECTION.md#check-installation-before-using-director-identity)
and [UPDATES](../pattern/engine/references/UPDATES.md#daily-discovery-and-project-preference).
**Status:** Clarification implemented in guidance; the corresponding
[manual scenario](DESIGN_NOTES.md#portable-staffing-and-acceptance-scenarios--october-23-2026)
is unverified. Revisit if genuine acceptance/check gates are skipped or unrelated
trial gaps still cause false holds.

## R12 — Give people a readable front door without another contract layer

**Accepted direction, October 17:** A public site at `director.metal-sole.com`
explains the director/worker/recorder division and gives visitors copyable requests
for their existing project agent to install, check, or explicitly update the pattern.
GitHub's published package remains authoritative; the agent guide links to its
current protocols instead of maintaining another installation implementation.
**Front-door refinement, October 17:** Human-facing install/update requests use
the public `director.metal-sole.com` address. A prominent “For an agent” link opens
the readable guide, which sends authorized work directly to the canonical GitHub
protocol and an exact reviewed revision. This supersedes copying the raw repository
URL in the website's human-facing prompts; it does not change upstream authority.
**Why/tradeoff:** Repository contracts are precise but dense for a first visit.
A short visual introduction makes the next action clear, while a separate summary
can drift. Keep installation/status/update claims bounded and link their source.
**Implemented:** [site/](../site/README.md) contains a static page and agent guide,
a small HTML/Markdown negotiation Worker, and an explicit public build allowlist.
It is outside the manifest-selected payload. Initial publication remains a separate
gate until a deployment receipt verifies the intended domain. Local content and
browser checks are not evidence of public availability or successful adoption.
**Regression cases:** The install button copies an agent request, not an executable
installer. The browser cannot declare the visitor's project installed. A displayed
director marker describes a checked setup/role, not running workers. Updates preserve
adaptations and private state under [UPDATES.md](../pattern/engine/references/UPDATES.md).
The public build excludes project state, private sources, and maintainer archives.
A domain-based request must reach the GitHub installation steps without sending
the agent or user around a loop of copying the same website request again.
**Revisit:** Real visitors cannot find the next step, summary copy contradicts
contracts, or a public build includes files beyond its explicit allowlist.

## R13 — Keep global discovery separate from project installation

**Accepted decision, October 18:** Offer a tiny optional global skill that points
to the current canonical [package guide](../pattern/README.md) for requested
install/add/update/upgrade/remove operations. Its
[source](../skill/director-pattern/SKILL.md) stays outside the manifest payload;
[distribution guidance](../README.md#optional-global-skill) selects the host's
per-user skill directory on request, without a project-local default.
**Why/tradeoff:** Discoverability should not duplicate the protocol or silently
adopt it in every project. Fetching the authoritative guide avoids stale copied
rules; a global pointer does not confer director authority. This adds an optional
entry route without changing the existing project adoption boundary.
**Implemented:** The source skill and global distribution guidance exist; the
package guide now explicitly distinguishes project removal from skill removal and
preserves owned project records and shared trackers. Existing installation and
update contracts remain authoritative for their operations.
**Regression cases:** A global skill discovered in a new project routes to the
canonical guide without declaring an installation. An explicit update reads the
current protocol rather than copied skill rules. Removing a project hook preserves
private context, requests, backups, and shared canonical trackers; removing only
the skill leaves project installations intact.
**Verification limit:** Skill validation and package isolation/link checks verify
structure and boundaries, not fresh-session discovery, target adoption, or removal.
**Revisit:** Real lifecycle requests misroute, pointer copies accumulate protocol,
or discovery is mistaken for project authority.

**Superseded in part, October 22:** The optional global skill is now explicitly
invoked only. Ordinary task relevance, including generic install/update/remove,
delegation, or project work, must not select or run it. The October 18 entry route
and project boundaries remain; automatic discovery is superseded.
**Why/tradeoff:** A globally available pointer could activate an operating method
when the user only asked for ordinary work. A clear request to use the skill, an
explicit command, or direction to its skill file keeps this lifecycle route
available without that ambient trigger.
Description wording alone cannot enforce selection policy.
**Decided and implemented:** The [Codex source](../skill/director-pattern/SKILL.md)
ships [agents/openai.yaml](../skill/director-pattern/agents/openai.yaml) with
`policy.allow_implicit_invocation: false`; the separate
[Claude Code source](../skill/claude-code/director-pattern/SKILL.md) sets
`disable-model-invocation: true` and `user-invocable: true`. Host-specific sources
avoid relying on undocumented cross-host frontmatter support. The
[distribution guide](../README.md#optional-global-skill) requires the complete
selected host skill and preservation of its native controls during updates.
Other hosts need a supported explicit-only policy before installation. Invocation
of a global skill remains distinct from the startup hook of an adopted project.
**Regression cases:** “Fix this bug and update its tests” or “install this package”
must not load the global Director Pattern skill based on relevance. An explicit
`$director-pattern` in Codex, `/director-pattern` in Claude Code, or user direction
to the skill file still reaches the canonical lifecycle guide. An update must not
lose Codex's policy file or Claude Code's invocation flags. Removing only the global
skill leaves project startup wiring and installations intact.
**Verification limit:** Frontmatter/policy parsing, source-to-installed byte checks,
skill validation, and package/link checks establish metadata and distribution
structure only. No live fresh-session selection or explicit-invocation trial is
claimed; running chats can retain earlier loaded instructions.

## R14 — Commit the installation with the project

**Problem:** The installed `.director/` holds the method contracts next to project
context, the request ledger, exact user sources, and receipts. The install guide
told agents to keep everything but the contracts out of Git, without saying what
to write in an ignore file, so the simplest compliant move was to ignore the whole
folder. A committed startup hook then named files that a fresh clone lacked, and
the missing-file check failed quietly. Work could not continue on another machine
or in a cloud checkout, and a collaborator saw none of the project's roles,
guardrails, or backlog.
**Accepted decision, October 21:** Commit the installation with the project by
default: contracts, filled PROJECT, config, requests, sources, current activity,
and receipts. A payload `.director/.gitignore` keeps only the helper lock,
in-progress write scratch, and pre-update backups local. Keeping more local is a
project's explicit later choice, recorded in that file and preserved by updates.
This supersedes the private treatment of project context, state, sources, and
receipts in R11–R13 and the "ignored local overlay" for generated-project context.
**Why/tradeoff:** The ledger is the project's request history and the backlog that
lets work continue anywhere; role mappings and guardrails are definitions a team
shares. Privacy matters in one case that a later opt-out cannot fix: exact messages
and attachments pushed to a public remote stay in history after deletion. Setup
warns once when a remote is public or its visibility cannot be checked, records the
warning in PROJECT, and asks nothing on private repositories. A shared store also
needs IDs that cannot collide. Request and source IDs derive from the project ID and
event ID, and counter-style event IDs restart on every machine, so the CLI now
requires event IDs ending in 32 random hex digits and offers `event-id` to make
them. The lock still covers one machine, so one machine writes at a time. A template
repository commits only contracts and a placeholder PROJECT, so generated projects
never share an initialized identity.
**Considered alternatives:** A committed `.director/` with an ignored `local/`
subfolder for the ledger and receipts kept the backlog off other machines, which is
the main reason to commit it. Renaming to a plain `director/` folder was not needed:
Git tracks dot folders, and the problem was mixing shared and private files with no
explicit ignore contract.
**Implemented:** [.gitignore](../pattern/.gitignore) as base payload; the
committed default, keep-more-local rules, and `git check-ignore` check in
[STATE.md](../pattern/engine/STATE.md#version-control), which installed files can reach;
the setup step and public-remote warning in [INSTALL.md](../pattern/INSTALL.md); local
backups, committed receipts, and existing ignored installations left alone in
[UPDATES.md](../pattern/engine/references/UPDATES.md); a version-control field in
[PROJECT.md](../pattern/PROJECT.md); the one-writer rule in
[RECORDS.md](../pattern/engine/references/RECORDS.md#persistence-and-interruption-recovery);
and the helper's `event-id` command and CLI check in
[TOOLING.md](../pattern/engine/references/TOOLING.md). This source repository still
ignores its own `/.director/`: the repository is public, and a local installation
here would hold the maintainer's exact conversations, which stay private. That is
the deliberate local choice this decision allows, not the default.
**Regression cases:** A fresh clone has every file its startup hook names, plus
config, requests, and sources, and `validate` passes there. A solo user pushes from
a laptop and a cloud checkout continues the open requests. Two machines starting
from one commit each create a request; the IDs differ and both survive the merge.
`create --event-id request-1` fails. The lock and a pre-update backup never appear
in `git status`. A project that ignores `requests/` and `sources/` keeps them
ignored through an update. An older installation ignored by a root rule is
reported, not silently tracked. A public-remote warning appears once, not again on
another machine.
**Verification limit:** Unit tests cover the event-ID check and generator and the
manifest payload. No real installation, cross-machine continuation, or public-remote
warning has been observed.
**Revisit:** committed sources leak sensitive material in real use, Git conflicts
in shared state become common, or teams need per-person ledgers.

## R15 — Allow subagents at every level, with named checks and batched records

**Problem:** Only directors were told to work in parallel. DIRECTION and MODELS said
to seek independent work, but WORKER said to delegate only when explicitly
permitted, and the assignment template offered a neutral "descendants permitted or
prohibited" line. Briefs filled it with a prohibition, so every worker stayed
serial. The October 19 proportionality rule named no level a brief could state, so
builders still defaulted to exhaustive checks. Outside tracked capture, nothing told
callers to batch routine records, so a recorder call followed nearly every step.
**Requested and implemented, October 23:** Any actor that staffs, workers included,
may use subagents where they help. Before each dispatch, a director lists the
independent streams, dispatches them together, and names the dependency or
exclusive resource behind any serial dispatch in the next SitRep. A shared-file
blocker is first split into new files behind a seam. Every assignment carries a
parallel plan; subagents are allowed by default within stated limits, and a
prohibition states its reason. A worker considers subagents for independent parts
of its own assignment and keeps small or coupled work itself. The aim is
permission, not splitting every task. Every actor works in the
project's one working tree under Git; parallelism comes from file and resource
ownership, not separate worktrees or checkouts. Every assignment names a
[verification tier](../pattern/engine/MODELS.md#verification-tiers): smoke for exploration
and mockups, focused for production changes in progress, full for production code
at integration, acceptance, or release. Routine state writes batch at milestones;
scope-setting capture, owner decisions and approvals, and dispatch receipts are
written promptly. Setup reports a project without version control as a parallelism
and recovery limitation and recommends initializing Git in place.
**Why/tradeoff:** A top-level instruction does not reach a worker that reads only
its brief and WORKER. Some hosts keep agents from using subagents unless an
instruction explicitly allows it, so opt-in wording and a neutral template line
read as a prohibition. The permission has to sit where each role reads it, and the
template has to ask for a plan rather than leave the question open. Serial dispatch still
happens, but it now carries a reason the user can see. A named tier gives a brief a
short, checkable verification instruction and keeps a receiver from raising it on
its own. Batching gives up some recovery granularity for speed; the writes that
recovery and authority depend on stay prompt. The cost is two required lines in each
brief and a judgment at each dispatch. Role, authority, and privacy rules are
unchanged: a default to delegate grants no scope a worker did not already have.
**Considered alternatives:** A worktree or checkout per parallel actor isolates
writes, but it adds merges, hides in-progress state from the one tree the owner
inspects, and was explicitly declined. Keeping delegation opt-in and relying on
directors to grant it had already failed: the grant was not given.
**Regression case:** In a native-app project on the predecessor pattern, four
independent implementation phases (diagrams, an add panel, help sheets, an icon) ran
one after another. Every worker brief said not to spawn agents; HTML mockup builders
ran 66 to 469 automated checks and three polish passes each; a recorder call
followed nearly every step; and the project was not under Git. Under this decision
the manager dispatches the four phases together, each brief carries a parallel plan
and a tier (smoke for the mockups), records batch at the dispatch wave and at each
evaluated return, and setup has already reported the missing Git.
**Status and verification boundary:** Implemented at the owner's request in
[WORKER](../pattern/engine/WORKER.md), [ASSIGNMENT](../pattern/engine/ASSIGNMENT.md),
[DIRECTION](../pattern/engine/DIRECTION.md#assign-bounded-work),
[REQUEST_MANAGER](../pattern/engine/REQUEST_MANAGER.md), [MODELS](../pattern/engine/MODELS.md),
[STATE](../pattern/engine/STATE.md), [RECORDER](../pattern/engine/RECORDER.md),
[INSTALL](../pattern/INSTALL.md), and [PROJECT](../pattern/PROJECT.md); awaiting the
owner's review of the wording. Package checks establish structure only; the
[manual scenarios](DESIGN_NOTES.md#parallel-default-scenarios--october-23-2026)
remain unobserved.
**Revisit:** parallel actors in one tree collide often enough to cost more than
serial work, smoke-tier work ships defects a focused check would have caught, or
batched records lose state that recovery needed.

## R16 — Separate replaceable engine from project-owned integration

**Decided October 25:** Install upstream contracts and helper implementations in
`.director/engine/`, separately from project-owned context, roles, policy,
adapters, identity pool/roster, tracker/config/state, sources and receipts.
A small project-owned PATTERN bridge supplies the canonical index locator and
points to the generic engine bootstrap; that engine loads the selected role
through the existing index. Manifest ownership lists and startup interface 1 make
the few coupling points explicit. Stable root helper launchers retain the prior
CLI/API and pass the actual store root; direct engine invocation uses that same
root. No store/config schema or predecessor compatibility changes.

**Problem and why:** The previous flat payload mixed generic files with adapted
PROJECT/bootstrap and project-owned roles/state. A heavily customized project or
domain stencil could not safely replace a directory: whole-folder replacement
lost its context, while comparing every neighboring file made a small update a
project reconstruction. Role preservation prose was necessary but did not create
an independently replaceable engine. The cost now is one explicit bridge read and
a reviewed one-time layout integration. This supersedes treating the whole flat
`.director/` directory as managed payload; it preserves R10's selected-role loading,
R11's incremental checks, and enduring policy rather than runtime caches.

**Affected contracts:** The [boundary](../pattern/engine/references/BOUNDARY.md),
[manifest](../pattern/manifest.json), [bridge](../pattern/PATTERN.md),
[engine startup](../pattern/engine/PATTERN.md), [setup](../pattern/INSTALL.md),
[startup integration](../pattern/engine/references/STARTUP.md), and
[updates](../pattern/engine/references/UPDATES.md). Interface compatibility and
engine baselines gate directory replacement. Unknown local engine edits require
reviewed extraction into project-owned definitions/adapters before replacement;
no blind deletion or mandatory repeated whole-project audit is introduced.

**Concrete regression:** A domain project has many specialist roles in its own
index, a custom identity pool, a release prohibition in local policy, and an
existing tracker. Replacing a compatible verified engine leaves those bytes and
store identity unchanged; the next selected role still reaches that policy.
Both stable and direct-engine helper entrypoints operate on `.director/`, never
create a parallel store under `engine/`, and still refuse predecessor stores.
A reusable stencil has no initialized state; copied projects initialize distinct
identities. An incompatible engine interface or unknown drift stops replacement.

**Status and verification boundary:** Implemented as a local candidate; not
published or adopted into this maintainer repository's live installation. Focused
package fixtures pass ownership, link closure, custom-neighbor preservation and
helper-root/receipt resolution checks. Explicit harness-selected startup trials and authorized stencil rollout are
recorded separately in [validation notes](DESIGN_NOTES.md); static checks do not
establish universal future compatibility or fresh-session compliance.
**Revisit:** frequent interface changes, unavoidable engine edits for local policy,
or project-owned callers require repeated reconstruction after compatible updates.

## R17 — Keep delegated work supervised and recover the user’s whole request

**Decided October 27:** The parent retains the user’s request and completion
obligations while work is delegated. Stable project/request references connect
owners’ requirements, progress, returned records, and evidence. Existing trackers
stay canonical; small assignments do not each need a new request folder.

**Problem and supported cause:** Existing contracts already required observation,
evaluation, rework, and exit accounting. Their external-owner exit did not
explicitly distinguish an independently accountable project from a subordinate
director. Recovery was described as an operation without making reconciliation a
normal duty at an active project conversation. Those are visible wording gaps.
Reports that users had to ask a Director to continue do not establish whether
workers were running, blocked, or misclassified in those incidents; that causal
explanation remains a hypothesis because those execution traces were not inspected.

A separate local observation showed a narrower execution failure: sending a
request to an idle, completed actor did not start a new turn. Actual status
inspection and the host’s supported continuation operation resumed the same owner.
A queued or delivered message is therefore not sufficient evidence of execution.
The durable correction states that distinction without prescribing host-specific
tools or treating silence as a blocker.

**Why and tradeoff:** Delegation protects the Director’s attention only if it
continues to observe and evaluate the entrusted work. A subordinate director does
not become an external ownership transfer by receiving a director role. The
existing genuine external-handoff exception remains for independently owned
projects with actual acknowledgment. This refines the earlier R5/R9 exit language;
it does not promise a daemon, wakeup, uninterrupted inference, or continuation
after the host ends a run. Explicit pauses, real blockers, interruptions, and
reserved authority retain their existing effects.

**Cadence refinement, October 27:** This supersedes the October 19/23 reading that
any ordinary progress update can indefinitely replace a consolidated overview.
While delegated work is outstanding, an overview about every five minutes, or the
user/project interval, accounts for all held streams and owners, including quiet
work and returns awaiting evaluation, with next actions. Ordinary progress can
satisfy that duty only when it provides equivalent coverage. Stricter host progress
updates remain concise; they do not each require another full report.

**Superseded later October 27 — proactively labeled reports:** The same
conversation exposed the remaining gap: the owning Director had sent progress
updates but no proactively labeled situation report before the user asked. That
observed output failure is distinct from hypotheses about the earlier reported
incidents. It also shows why equivalent ordinary coverage is insufficient for the
user’s explicit expectation of a recognizable report.

The later decision requires a proactively labeled **📋 SitRep** while delegated
work is outstanding, about every five minutes or at the user/project interval.
Ordinary progress and status questions neither replace nor reset it. The first
interval starts at actual dispatch; resumed work whose report is overdue or has
unknown timing receives a prompt report. Stricter host progress updates stay
concise and separate. This supersedes the immediately preceding equivalent-update
exception while retaining the earlier reasoning as history. Host interruption
still limits execution; no file supplies a daemon or wakeup.

**Implemented ownership:** [DIRECTION](../pattern/engine/DIRECTION.md#recover-and-supervise-held-work)
owns the supervision/recovery loop and exit distinction.
[STATE](../pattern/engine/STATE.md#parent-commitment-and-requirement-traceability)
owns parent references and evidence retention;
[ASSIGNMENT](../pattern/engine/ASSIGNMENT.md) carries those references into bounded
work. Role definitions point to those contracts rather than repeat the policy.
The scope is entrusted unfinished work within existing authority, not automatic
execution of casual conversation or every queued idea.

**Concrete regressions:** A parent keeps observing a running worker and a bounded
child director after answering a status question; an incomplete submission returns
to its same owner for rework. A later active conversation inspects saved handles,
returns, and artifacts before resuming authorized work, instead of blindly
restarting stale tasks or calling them stuck. Child returns preserve parent and
local record IDs, observed status/time, and evidence locators. A genuine external
owner’s acknowledged transfer keeps the source commitment waiting without
requiring the source to supervise that owner’s descendants. Explicit discussion-only
requests remain conversational.

**Verification boundary:** The instruction changes and public explanation are
implemented. Deterministic fixture results and actual bounded runtime observations
are recorded separately in [validation notes](DESIGN_NOTES.md#active-supervision-recovery-and-traceability--october-27-2026).
No test of prose or stored status alone proves active supervision.
**Revisit:** child director assignments still become accidental exit routes,
restart reconciliation duplicates work, or traceability starts forcing a second
tracker or a new record per tiny task.

## Maintain this explanation

At a material design choice, update the relevant topic rather than append every
conversation. State context, current direction/status, why/tradeoff, affected contract
or design reference, and a concrete scenario that should still work. Label uncertainty
as hypothesis/open. Ordinary status chat or a hunch does not create universal policy.
Refactor for coherence; preserve dated changes and superseded reasoning in a short
history or linked design record rather than silently rewriting the past.

Preserve source evidence privately without rewriting originals. Later steering
gets a dated addition; current contracts and dated decisions/supersessions control.
Publish distilled reasoning rather than verbatim conversations or internal-source
pointers. Public documentation must stand on its own.

## Initial decision history — October 16, 2026

- Accepted tracked-by-default with lean optional, superseding project-type defaults.
- Preserved the user's independent-outcome/peer-ownership restart requirement;
  refined the candidate around flexible links and acknowledged external supervision.
- Separated installable method from workshop material after the explicit boundary
  request; retained one repository with an isolated package and manifest copy list.
- Established a living rationale to retain decisions, alternatives, and revisit triggers.
- Selected and implemented request folders with typed links, superseding the earlier
  flat-file design; host mappings and real adoption remain separate gates.
- Established a public/private authoring boundary: generic rationale and tests are
  public; exact conversations and internal reference material are retained privately.

## Decision history — October 17, 2026

- Added sparse question, user-action, and checked director-identity markers.
- Refined the marker vocabulary with **📋 SitRep** for periodic report blocks,
  superseding the unmarked `Sitrep` opener while retaining director identity and
  the existing supervision/cadence requirements.
- Added a bounded situation-report cadence with continued supervision; preserved
  existing host, handoff, pause, and interruption boundaries.
- Required current setup facts from the recorder and role resolution by the director
  before identity use, without claiming behavioral verification or worker liveness.
- Superseded ancestry-based worker defaults with project-session director defaults
  and explicit role/scope/authority on every bounded delegated assignment.
- Added pinned GitHub-source update instructions and private managed-file baselines;
  preserved project state, adapters, template identity boundaries, and explicit migration gates.
- Added a public introduction outside the installable package, with copyable agent
  requests and GitHub protocols remaining authoritative; publication is a separate gate.

## Decision history — October 18, 2026

- Added an optional global pointer skill outside the project payload, preserving
  one canonical lifecycle guide and explicit project adoption.
- Clarified conservative removal and the independent global-skill/project boundaries.

## Decision history — October 19, 2026

- Refined SitRep frequency around useful periodic overviews, preserving timely
  ordinary progress, the five-minute silence limit, and stricter host timing.
- Kept the reported repetition distinct from its hypothesized cause; documentation
  implements the refinement, while fresh-session behavioral checks remain pending.
- Added proportionality to verification and records. Evidence demands had no
  counterweight and compounded: exhaustive layout sweeps and release-grade QA on a
  throwaway prototype, and a per-message capture round-trip before work could move.
  Verification now matches risk, reversibility, and audience; briefs state the
  smallest sufficient check; routine records batch small and fast at checkpoints.
  Scope-setting capture stays first and exact; the director still does no worker tasks.

## Decision history — October 21, 2026

- Forked the predecessor Producer Pattern as the Director Pattern. By explicit later
  direction, every "producer" term became "director": package name, `Role: director`,
  the `.director/` install directory, the accept event's `director` field, stored
  `director_acceptance.director`, the public site address, and the source repository.
  Earlier entries now use this vocabulary as a terminology change only, not a change
  to their reasoning. The store format became `director-request-bundles` so a
  predecessor store is refused rather than half-read (R11).
- Gave each complete outcome one Request Manager, superseding per-outcome judgment by
  the project Director (R1). Specialties are tasks inside the outcome; the Director
  keeps conversation, compact commitments, cross-outcome scope and priority,
  authorization, and user-facing acceptance; managers keep the full outcome record.
- Mapped the design onto existing vocabulary: a Request Manager is a bounded
  `Role: director`, with no new role value (R10); the non-worker boundary covers
  managers (R2); only the checked project Director shows `🎬` (R9); a conversational
  reply is not completion or the end of supervision (R9).
- Superseded a proposed mandatory shared intake layer with optional, explicitly
  dispatched bounded analysis: no second user entrypoint and no one-pass limit (R1).
- Required role-index discovery and reference acknowledgment before staffing, with no
  silent generic fallback (R10); replaced fixed model defaults with a per-assignment
  capability/effort policy and one coordinated Recorder route (R2); added a shared
  identity roster that skips reserved markers (R9).
- Kept the helper's events and config 1/store 2 schema, changing only its store
  format name to `director-request-bundles`; documented active/review steering
  as requeue or revise, then amend, plan the same owner, and dispatch the same
  observed handle. Added the new contracts to the base manifest and extended update
  preservation to project roles, model mapping, and the private roster (R11).
- Status: decided and implemented in contracts; deterministic fixtures cover the
  record mapping and package boundary. The acceptance scenarios have not run live
  ([design notes](DESIGN_NOTES.md#request-manager-scenarios--october-21-2026)).
- Committed the installation with the project by default, superseding private
  project context, state, sources, and receipts (R14, R11). A payload
  `.director/.gitignore` keeps only the lock, write scratch, and backups local;
  setup warns once on a public remote; CLI event IDs must be unique across machines.
  Status: decided and implemented; unit tests pass, no real installation observed.

## Decision history — October 22, 2026

- Superseded automatic global skill discovery with explicit user invocation (R13).
  Codex and Claude Code receive their supported native invocation controls in
  separate complete host skill sources; updates must preserve those controls.
- Kept optional global invocation, adopted project startup hooks, installation,
  and removal distinct. Metadata/configuration checks do not prove fresh-session
  behavior or change instructions already loaded in a running chat.

## Decision history — October 23, 2026

- Separated durable capability policy from host/time-scoped observations (R2),
  superseding PROJECT's role-to-model table and installation-time concrete mapping
  as a future default. All staffing actors refresh current supported selections at
  relevant use; routine remapping stays within existing authority. Clarified that
  recorded installation acceptance, current setup, and unrelated pending trials
  have separate effects on daily discovery (R11). Guidance is implemented;
  behavioral verification remains pending.
- Refined responsiveness (R2): the main Director delegates substantial analysis and
  detailed coordination before doing that active work in the main conversation.
  Bounded outcome owners retain full recoverable detail; compact Director context
  does not mean losing that detail. Direct-in-reply answers, critical judgment,
  existing authority, and actual host limits remain intact.
- Refined identity choice (R9): short Capitalized names are bold in human-facing
  output; playful semantic fit guides choices through one shared roster and cursor.
  Soft overlapping affinities add no fixed role taxonomy, separate pools, runtime,
  or schema. Collision, resume, late-return, reserved-symbol, and customization
  protections remain explicit.
- Status: decided and implemented in owning contracts, with package checks scoped
  to static structure. Actual responsiveness, delegation, identity choice, and
  reservation behavior await the listed manual observations.

- Made routine updates incremental (R11), superseding the earlier October 23
  unconditional upgrade audit/trial requirements while preserving first-install
  checks and project-specific adaptations. Current pinned update guidance selects
  scope even for older installations; performed checks, reused evidence, and
  unresolved prior gaps remain distinct.
- Named the first release **v1.0.0** using an annotated Git tag and GitHub release.
  Public front doors show the readable version; the pinned commit and package-tree
  comparison in R11 remain authoritative for update discovery. No version registry
  or schema change is introduced. Regression case: a newer main commit with an
  unchanged package tree still produces no update notice, regardless of tags.
  Release naming does not establish pending fresh-host or automatic-update trials.

- Allowed subagents by default at every level (R15), superseding opt-in worker
  delegation and the neutral descendants line in the assignment template. Every
  assignment now carries a parallel plan and a verification tier; serial dispatch
  names its reason; all actors share one working tree under Git; routine records
  batch at milestones; setup reports a project without version control. Extends the
  October 19 proportionality rule with named tiers. Status: implemented in contracts,
  awaiting owner review and release naming; package checks only, behavior unobserved.


## Decision history — October 24, 2026

- Added explicit returned-result startup dependencies from the host-loaded hook
  through PATTERN, canonical index, selected definitions, and mandatory references
  before task I/O or direct answers (R10). Background setup/identity checks stay
  separate. Controlled fresh Claude observations support read ordering for the
  candidate; the required completion acknowledgment remains an observed gap.
- Retained role-selected loading after eighteen separate mechanism observations:
  initial global or per-hop prerequisites completed the small chain, while links
  and ordinary untimed read instructions did not. Flattening reduced Read groups
  in the tiny selected-role control, without establishing a need to flatten the
  production package. Observed behavior and limits are recorded separately from
  the six actual-package sessions; operational wording remains unchanged.
