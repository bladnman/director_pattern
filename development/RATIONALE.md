# Why the Director Pattern has this shape

Living design rationale · updated November 16, 2026. This repository authors a
candidate pattern; it has not automatically adopted or installed that pattern.
This document explains the current reasoning, tradeoffs, and revisit triggers.
It is not an activity log or a claim that every design direction is approved.

Keep four claims distinct: **stored** means preserved in a file; **decided** means
an explicit choice has been made; **implemented** means the behavior exists;
**verified** means relevant evidence demonstrates it. A requirement can be accepted
while its implementation remains open. Tracked-by-default is accepted; the entire
package is not thereby approved. The request-folder/link implementation is now
authorized separately; implementation and verification still need their own evidence.

The v1 compatibility contracts are [PATTERN.md](../pattern/PATTERN.md),
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

The latest [flat-starter decision](#r18--start-flat-and-make-learning-an-explicit-bounded-loop)
supersedes the earlier normal Request Manager/Recorder route for new starter
installations. Earlier dated decisions remain below as history; existing
installations retain their authority until explicitly integrated.

A November 11, 2026 candidate, starter revision 3.3, moves the Director's standing
rules into a marked block in AGENTS.md and the detail onto cards read before named
actions. It is implemented on a branch and is not merged, published or accepted; its
supersessions are listed under
[R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes).
Until it is accepted, the 3.2 route described in the earlier dated entries remains
the source candidate's current route.
*November 14 addition:* 3.3 and 3.4 are now published on `main`; acceptance still
waits on fresh host trials.

A November 13, 2026 source change, starter revision 3.4, keeps that route and adds
four rules from a field report: a call in a roster role's domain goes to that role;
the Director looks back at closure or a retro for recurring role-less work and steps
that do not earn their cost; such a step can be the better route it recommends; and a
quiet stretch with work out does not pause the SitRep cadence. It is recorded under
[R18](#r18--start-flat-and-make-learning-an-explicit-bounded-loop) and cross-referenced
from R1, R2, R10, R11 and R17; it is reviewed with findings applied, and not yet
accepted by the maintainer or published.

On November 14, 2026, the maintainer's own installation moved out of this repository
into a private sibling workspace. Before, it sat here, ignored, so Git never carried it off this machine.
This repository now holds no installation. The entry under
[R14](#r14--commit-the-installation-with-the-project) supersedes the ignored-installation
choice and the public half of the November 13 move of that installation to the 3.3
block, with cross-references in R8, R10 and R11. The move is implemented and
hash-verified; the public cleanup's merge and push and the live fresh-session trials
are pending.

Also on November 14, 2026, the maintainer decided that a project's AGENTS.md belongs
to the project: the pattern states and enforces no byte limit on it, its installed
block or its project section. The 8,000, 6,500, 4,500 and 3,000 byte budgets stay only
as authoring rules for the text this repository ships. The entry under
[R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes) supersedes the November 11
caps as limits on projects. It is decided, and implemented in the working tree as
starter revision 3.5 and tested; it is not committed or published.
*Later November 14 addition:* 3.5 is now published on `main`.

Later on November 14, 2026, the maintainer stated a base intent: several Project
Directors and other actors working in one folder at the same time is expected, not a
hazard. They may not know about each other; they notice overlap and manage it as a
team would, and the Director that accepts an outcome checks the combined result. The
entry under [R1](#r1--one-accountable-conversation-without-a-forced-organization) records it, rewords phrasing
that counted sessions or writers, and turns the shipped block's 8,000-byte budget into
a target with an alarm at 10,000. It is implemented in the working tree as starter
revision 3.6 and tested statically; it is not committed or published.

Also on November 14, 2026, after a Director asked a sibling project's Director a
question only when the user told it to, and then told it to change nothing, the
maintainer decided that a Director knows other projects may have their own Director
and takes a question or task that belongs there to it as a peer, which owns its
project and decides how to work there. The entry under
[R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)
records it, with the block lines and other additions the Director made in review. It
is implemented in the working tree as starter revision 3.7, with the new wording
pinned by `PeerDirectorsNovember14Tests`; it is not committed or published.
*November 15 addition:* 3.6 and 3.7 are now published on `main`.

On November 15, 2026, after fresh host trials in which one of three sessions started
from a Director session arrived as a worker because the host told it its report goes
back, the maintainer decided that a worker is a session a Director names as one, and
that any other session is its project's Director, whoever or whatever started it.
Directors will be started by agents more often than by people. The shipped worker
line also names the user and an explicit assignment; that keeps the block's existing
assignment and opt-out wording and is not part of the maintainer's decision. The
entry under
[R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)
records it; it supersedes the November 11 narrowing of who counts as a worker and
restores the October 17 default. It is implemented as wording in starter revision
3.8, pinned by `RoleDefaultNovember15Tests`, and published on `main` with this
change; its live trials are pending.

Later on November 15, 2026, after a trial in which a subagent given a brief with no
role was nominally a Director but ran no startup, the maintainer decided that this
risk is handled by the agent that starts the session: a subagent should not be
created without being defined as a worker. The entry under
[R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)
records it, with the host fact that subagents receive the parent session's
start-time instructions. It is implemented as wording in starter revision 3.9, pinned
by `HelpersAreDirectorsNovember15Tests`, and published on `main` with this change;
its live trial is pending.

Also on November 15, 2026, after two outside projects' Directors each held a routine
update open for four fresh-session trials and asked whether to run them, the
maintainer decided that a user's update is finished when its quick checks show things
still work; a deeper check may be offered but is never required. The entry under
[R11](#r11--update-from-a-pinned-public-source-without-replacing-project-state)
records it: fresh host trials become the maintainers' work on published revisions in
their own installation, and the receipt-before-trials rule of November 11 and 13 is
superseded. It is implemented as wording in starter revision 3.10, pinned by
`UserUpdatesFinishOnChecksNovember15Tests`, and published on `main` with this change.

## R1 — One accountable conversation, without a forced organization

**November 14 — several Directors in one folder are expected, and they cooperate
(clarifies "One folder normally has one project director"; starter revision 3.6):** A
Director in an adopting project warned the maintainer that a second Project Director
session in the same folder would collide. The maintainer's position is that several
Project Directors, and other actors, working in one folder at once is a core
expectation of the design, not a hazard to prevent. Each may not know about the
others; they notice where their work meets and manage it the way a team does, and the
Director that accepts an outcome checks that the combined result still holds. No live
rule forbade this, and the block already assumed it: Recovery leaves other open
requests with their owners, a second conversation does not adopt another's requests
([R17](#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request)),
and the store serializes cooperating writers and rejects stale revisions. But several
sentences counted sessions or writers, among them the "Current direction" line below,
and nothing said positively that parallel Directors are normal. That the counting
wording primed the warning is a hypothesis; the model's own prior may explain it.

The line below keeps its original wording as history. It meant that accountability
sits with one owner per outcome and that no manager tree is required, not a limit on
how many Director conversations run in one folder. Likewise, "another Director only
for sustained coordination" ([R18](#r18--start-flat-and-make-learning-an-explicit-bounded-loop))
is about a Director staffing a scoped child, not about how many sessions the user
starts.

**Implemented.** The block's role paragraph, which every role reads, gains two
sentences after "role names grant nothing": "Other Directors and actors may be working
here at the same time, often unaware of you; that is expected. Notice where your work
meets theirs and work it out together." The supervision card's reconcile paragraph
gains the acceptance check and the recovery route: others may have changed the same
files or records meanwhile, so before accepting, check that the combined result still
holds, and where work was stepped on, use its request to restore what it was for. Its
"One owner keeps the whole usable result" becomes "Each outcome's owner keeps". The
store guide's "One cooperating writer owns shared state" becomes "Cooperating writers
share this state; the helper takes their changes one at a time", and its Git paragraph
now says one machine writes at a time "when it moves between machines through Git",
which is what it always meant. The source guides' counting phrases ("One Project
Director stays", "uses one Project Director", "another Director", "no mandatory second
Director", and "One project and one director remain the normal case" in
[REQUEST_RELATIONSHIPS](REQUEST_RELATIONSHIPS.md)) are reworded to their meaning: one
accountable owner per outcome, a flat shape, a scoped child Director when coordination
warrants it.

**Why/tradeoff:** The pattern states intent, not mechanics. Rules that would forbid
changing another actor's work, require a single session, or require Git were
considered and rejected. They create edges agents trip over later without knowing
why, and overlap happens anyway. Requests are the durable record of what each actor
was trying to do, so stepped-on work can be found and redone from its request;
uncommitted work is common and is not a fault in itself. Git composes with this and
helps, but the starter does not require it, as
[R15](#r15--allow-subagents-at-every-level-with-named-checks-and-batched-records)'s
November 1 supersession already holds. The risk is a Director that under-reacts to a
real conflict; the acceptance check is the guard. The card sentence is read only at the
card's trigger, so the always-loaded block carries the intent and the card carries the
check.

**The block's size is a target, not a cap.** The two sentences cost 167 bytes and take
the shipped block from 7,997 to 8,164 bytes, past the 8,000 budget that
[R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)'s
November 14 entry kept as an authoring rule. The maintainer decided the same day that
8,000 is not a magic number: the block should be as small as it can be and stay near
8,000 bytes, with an alarm as it approaches 10,000. This repository's AGENTS.md now says
"keep the shipped `agents/block.md` as small as it can be, near 8,000 bytes; past 10,000
is the alarm to cut it back", and the budget test fails only past 10,000. Staying near
8,000 is an authoring judgment a test cannot make; the purpose, small standing text
every agent pays for on every turn, is unchanged. The card, WORKER.md and
section-template budgets are unchanged.

**Regression cases:** A Director that finds another session's open requests or edits in
the folder says so plainly, leaves those requests with their owner and goes on with its
own work, coordinating where they meet. A Director that declares parallel Directors
will collide, asks as a rule that one be stopped, or adopts the other's requests fails.
A Director whose outcome touched files another actor changed checks the combined result
before accepting, and uses the other request to restore work it stepped on. Known-bad
case: the field warning above. A shipped block past 10,000 bytes fails the pre-publish
budget check; one at 8,164 passes.

**Status:** Decided by the maintainer on November 14, 2026, and implemented in the
working tree as starter revision 3.6: the block, supervision card and RECORDS.md
wording above, the source-guide rewordings, the AGENTS.md budget sentence, and
`BLOCK_BUDGET` raised to the 10,000 alarm in `development/tests/test_authoring_budgets.py`
with its drift guard and the shipped-number scan updated. New oracle:
`test_parallel_directors_and_actors_are_expected_and_cooperate` (in
`development/tests/test_block_route.py`), which pins the sentences and keeps the counting
phrases out of shipped text; the role-gate pins carry the two new sentences. Static
tests only. No live run shows a Director noticing overlap or checking the combined
result; that needs a trial with two Directors in one folder. Not committed or
published; installed copies keep their adopted text until updated.

**November 13 — a step that does not earn its cost can be the better route
(cross-reference):** The November 7 partner rule below maps a request onto the
project's established mechanism. The November 13 field report (recorded under
[R18](#r18--start-flat-and-make-learning-an-explicit-bounded-loop)) found that rule
read as "every recorded step is fixed": no step was ever proposed for a cut. The
requests card now says the established mechanism is the default route, not a fixed
law: when one of its steps is not earning its cost on this request, the Director says
so and recommends the cut or merge as a ❓ once; until the user chooses, the step is
kept, and a step that keeps not earning its cost goes to the look-back
([R18](#r18--start-flat-and-make-learning-an-explicit-bounded-loop)) rather than
being asked again on every request. The user still decides, and where a project rule
forbids the cut the Director gives the permitted route. **Regression case:** a
recorded step that cannot change the result of a small request is named with its
source and cost, and the cut is one ❓; the step still runs until the user chooses. A
Director that skips it silently, asks again on every later request, or keeps applying
it without ever saying so, fails.
**Status:** Decided by this repository's Project Director on November 13, 2026, from
the maintainer's field report, and implemented in the starter source as revision 3.4.
An independent review the same day, with its findings applied, accepted it; the
maintainer's acceptance and publication are pending. Static tests only; no live run
yet, and installed copies keep their adopted text until updated. Oracle:
`test_a_step_not_earning_its_cost_is_asked_once_and_kept_until_the_user_chooses`.

**November 7 — act as the user's partner, map the request onto the project's own
route, and judge a better route on merit:** An independent audit of a session that
rolled out a starter update found the Director treating a literal request as an
order. Asked to roll an update out, it dispatched outside workers to patch other
projects instead of using each project's own Director and
[update route](#r11--update-from-a-pinned-public-source-without-replacing-project-state);
it read only part of the update guide before planning; and when the user proposed the
right route, it recommended finishing its own in-flight workers first. The guidance
that should have prevented this was scattered preservation and ownership constraints
that could be satisfied by their letter, while momentum rules (finish what is
started) pulled the other way. The audit account is the maintainer's; the causes
beyond what the session did are hypotheses.

The maintainer decided on a partner rule at the top of starter
[DIRECTOR](../pattern/starter/payload/DIRECTOR.md), the one file every conversation
reads. The Director is the user's partner, not a literal executor: the user may not
know every mechanism the system already has, so before acting the Director maps a
request onto the project's established mechanism and owner. When the literal request
would bypass it, the Director says so, proposes the established route and recommends
it. Recommendations are judged on merit, not on work already started: when a better
route appears mid-flight, conflicting work pauses first, then the Director
recommends. The user still decides; this adds no new role, hierarchy or approval
step.

**Review refinement (independent review, same day):** the review found the first
wording left the recommendation easy to bury and the in-flight work free to continue.
The runtime text now marks the recommendation ❓ as a user decision and holds the
bypassing or paused work, neither started nor resumed until the user chooses, while
independent, unaffected work continues. The user's choice stands within project
rules: where a rule forbids the literal route, the Director gives the permitted route
or the 🖐️ action. DIRECTOR also now points to reading the whole
[UPDATES](../pattern/starter/payload/UPDATES.md) guide before planning any update, in
this or another project, and says another installation is updated only by its own
project's Director (or, without one, an agent the user directs there) in its own
conversation; this is a reachability fix, since the field Director had read only part
of the guide.

**Why/tradeoff:** One short rule that names the failure (a literal reading that
bypasses an established owner) is easier to follow than constraints that each look
satisfied in isolation, and it sits where it is read in every conversation. Pausing
before recommending removes the pull of sunk work from the recommendation; the cost
is that a pause can briefly idle work that turns out to be fine, and pausing is
reversible where a patch outside the owner is not. Holding only the affected work
keeps independent work moving; the cost is that the user is asked at a decision point
and an unanswered ❓ leaves that work held. The rule may add a short exchange
when a request bypasses an established route. The risk is a Director second-guessing
requests that do not bypass anything; the rule applies only when a literal reading
would bypass an established mechanism or owner, and the user's choice stands. That
the top-of-file position raises uptake is a hypothesis. Reading the complete
selected guide before planning is an existing requirement and is unchanged.

**Regression cases:** Asked to roll an update out to several projects, the Director
maps it onto each project's own Director, starts or requests a session in each, and
writes nothing in those projects from outside. When the user proposes a better route
while workers are in flight, the Director first pauses conflicting work, then
recommends on merit, not on finishing what is started. A request that already fits
the established route proceeds without a detour or lecture. A Director that explains
the established route but still dispatches the outside patch fails. A better route
mid-flight yields a ❓ recommendation with the affected work held and unaffected work
continuing; a recommendation buried in prose, or conflicting work resumed before the
user chooses, fails. Where a project rule forbids the user's literal choice, the
Director offers the permitted route or the 🖐️ action rather than silently complying
or refusing. Planning an update begins with the complete UPDATES guide.

**Status:** Decided by the maintainer on November 7, 2026, with wording refined by the
independent review that day, and implemented in starter DIRECTOR wording. Live
behavior is unverified; installed copies keep their adopted text until updated, and
the v1 engine is unchanged. See the
[validation cases](DESIGN_NOTES.md#partner-rule-and-explicit-dispatch-settings--november-7-2026).

**November 4 — entrust local judgment, retain whole-result acceptance:** Qualified
owners and required independent reviewers receive the local decisions they may
make, what their findings permit next, bounded repairs and real escalation conditions.
The Project Director evaluates their reasons, evidence coverage and exceptions
against the whole intended result without repeating every delegated check. This
implements the useful per-outcome judgment of the earlier Manager design while
preserving R18's flat default and optional scoped coordination. It adds no new role
value or mandatory reviewer/manager. [R17](#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request)
owns the concrete evidence-reconciliation trigger and limits.

**Latest supersession, October 30:** [R18](#r18--start-flat-and-make-learning-an-explicit-bounded-loop)
restores the flat default for new starter installations; the earlier manager route
below remains the history and v1 compatibility design.

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

**November 13 — the direct-answer category is narrowed by domain (cross-reference):**
The later November 1 entry below kept acceptance judgments among the Director's
direct work and named misclassifying a review as discussion as the hypothesis for an
undelegated review. The November 13 field case is a second instance of the same
shape: a call that belonged to a roster role was handled as discussion. Duty 2 now
excludes a judgment, draft or rule in a roster role's domain from what the Director
answers itself, even in chat
([R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes),
November 13). Discussion, simple lookups and the Director's acceptance of a returned
whole result stay direct.

**November 7 — set capability and effort explicitly on every dispatch; the strong
default is the strong tier at high effort:** An independent audit of a session that
rolled out a starter update found that 9 of its first 12 workers were dispatched with
no model and no effort, inheriting the strongest tier at the session's top effort;
these accounted for about 74% of the subagent output tokens. The audit identified
three contributing causes. The flat starter's rewrite had dropped the v1 [MODELS](../pattern/engine/MODELS.md)
sentences that make the policy the explicit instruction and forbid silent inheritance
by omission. The host's delegation tool reserves effort for explicit instructions, so
an unset effort fell back to the parent's. And an earlier review had stated the
"explicit choice at dispatch, not inherited parent settings" principle only in the
November 5 entry below, which is not loaded at runtime, so the runtime text never
carried it. The figures are the audit's, not re-run here.

The maintainer decided the rule now in starter
[OPERATIONS](../pattern/starter/payload/OPERATIONS.md#staffing-and-maintained-roles),
with one sentence in starter [DIRECTOR](../pattern/starter/payload/DIRECTOR.md).
The guidance is itself the explicit instruction to set capability and reasoning
effort for each delegated task wherever the host allows, including hosts that reserve
those controls for explicit instructions. Both are set on every dispatch; omission is
not a choice. **Extending and tightening the November 5 entry:** the strong default
means the strong tier at high effort, chosen at dispatch rather than inherited; the
lighter-tier path (a lighter tier at high or extra-high effort, or the strong tier at
medium, for small, well-specified, easily checked work) stands as that entry
describes. The strong tier's top effort levels are reserved for hard diagnosis,
conflicting evidence or a consequential independent review. Each choice is recorded
with a one-line reason (size, how easily the result is checked, consequence of
error); "inherited" or "not set" is acceptable only with the host constraint that
forced it. This restores in runtime text the v1 intent to select both for each job and
never inherit by omission; it does not restore the v1 "smallest suitable capability"
sentence, which the November 5 entry already departs from.

**Why/tradeoff:** An explicit rule closes the gap the audit found: omission was
silently the most expensive choice. High effort was chosen over medium or matching
the parent: medium would under-serve routine strong-tier work, and matching the
parent is exactly how the session's top effort reached most of the output. The cost
is that routine strong-tier work now runs at high, not medium, and each dispatch
carries a recorded reason. Where a host cannot set one control, the honest record is
the constraint, not a claimed choice. The no-frozen-model, no-vendor and
no-universal-strongest/cheapest rules stand; effort names map to the nearest supported
controls. A reason line can become boilerplate; review of dispatch records is the
check, and its quality is unproven.

**Regression cases:** A lookup-only dispatch sets an explicit lighter tier and effort
with a one-line reason, not the parent's settings. A normal build or review dispatch
sets the strong tier at high effort unless the work meets the lighter-tier conditions
or genuinely needs the top levels, and says why. A dispatch record "inherit; not set"
without a forcing host constraint fails review. A host that reserves effort for
explicit instructions still receives a value, because the guidance is the explicit
instruction. A host that cannot set effort records that constraint and the settings
observed or unknown. Guidance names no vendor or model.

**Status:** Decided by the maintainer on November 7, 2026, with the independent
review's wording changes included (DIRECTOR also says to record a one-line reason, and
OPERATIONS lets a guide name a case that meets the lighter-tier conditions, as
[R11](#r11--update-from-a-pinned-public-source-without-replacing-project-state) does
for ordinary updates), and implemented in starter OPERATIONS and DIRECTOR wording.
Live dispatch behavior is unverified; installed
copies keep their adopted text until updated, and the v1 engine and its MODELS
contract are unchanged. See the
[validation cases](DESIGN_NOTES.md#partner-rule-and-explicit-dispatch-settings--november-7-2026).

**Later November 1 — dispatch before detailed investigation/review:** A fresh
installed review request loaded the current Director/operational instructions but
completed the review itself, without a subagent call. No failed subagent launch was
observed. Misclassification as discussion or acceptance is a hypothesis; the trace
does not establish the model's internal cause. The existing positive delegation
rule did not establish this case's behavior.

The loaded hook now names project investigations/reviews/changes and requires
delegation before detailed work. The foundation says scope → dispatch → evaluate;
ordinary discussion, simple lookups, startup/scoping reads, narrow recording and
acceptance judgments remain direct. A distant broad reply-only sentence is removed
so a review deliverable cannot become direct work merely because its report fits
in a reply. The oracle requires an actual bounded dispatch before detailed review,
then returned evidence and owner evaluation. A child launched after the parent has
finished the review does not satisfy it. This is a focused candidate correction,
not a new organization or a claim of reliable behavior until the affected trial
and independent review pass.

**Latest supersession, October 30:** [R18](#r18--start-flat-and-make-learning-an-explicit-bounded-loop)
removes mandatory Manager/Recorder actors from the starter while retaining bounded
execution, explicit authority and complete-outcome evaluation.

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

**Clarified, November 3 — author for unknown future environments:** The repository's
[maintainer instructions](../AGENTS.md) apply the portability policy to examples and
comparisons too: no concrete model name or alias stands for capability or size.
A future reader cannot recover that meaning from an obsolete catalog. Describe the
required reasoning and capability, resolve current controls at use, and retain
actual selections only as dated execution evidence. The regression is guidance
that uses a retired model as its capability exemplar: a new environment must be
able to choose from the stated task needs without interpreting that old name.
This clarification is implemented in maintainer guidance outside the installation
payload; it changes no runtime route and establishes no fresh-host behavior.

**November 5 — strong default, occasional lighter tier for small confident work:**
The user asked staffing to fit capability to bounded work: a strong capability
tier stays the default, but occasionally, with very high confidence that a lighter
tier can do small, well-specified and easily checked work, choose that tier at high
reasoning effort, or extra-high when a little less confident; the strong tier at
medium effort is equally acceptable. The user asked for this as a host-neutral
suggestion, because the same pattern runs under different hosts, never as model
names. Starter [OPERATIONS](../pattern/starter/payload/OPERATIONS.md#staffing-and-maintained-roles)
and [DIRECTOR](../pattern/starter/payload/DIRECTOR.md) now state it.

**Why/tradeoff:** A blanket strong tier spends capacity on work a lighter tier at
higher effort can do reliably; a lighter default would under-serve ambiguous work
and invite cost-driven choices. Gating on size, specification, easy checking and
confidence bounds the risk, and the unchanged verification tier, required
independent review and staffer evaluation catch a wrong call. "Occasional" is
deliberate: no quota, ratio or cost target. Effort names map to the nearest
supported controls. The no-frozen-model/vendor and no-universal-strongest/cheapest
rules stand. This states a stronger default posture for the flat starter than the
v1 [MODELS](../pattern/engine/MODELS.md) "smallest suitable capability" sentence;
that compatibility contract is unchanged, and existing installations keep their
adopted guidance until explicitly updated.
The strong default is an explicit choice made at dispatch, not inherited parent
settings, so task-fit selection, the lighter-tier path and the settings evidence keep
R2 October 23's purpose that a clerk does not silently inherit its parent's strongest
model/effort.

**Regression cases:** A small help-text cleanup with an exact diff check may go to
a lighter tier at high effort; its dispatch records requested and effective
settings or unknowns, and the staffer still evaluates the return. A small fix with
slightly less certainty uses a lighter tier at extra-high effort or the strong tier
at medium. An ambiguous diagnosis, a consequential release step or work without a
cheap check stays on the strong tier regardless of cost. A lighter builder never
waives or absorbs required independent review. Guidance names no vendor or model;
a host with different effort labels maps to its nearest supported levels.
The dispatch records a deliberate tier choice; a child never takes its parent's
settings merely by inheritance.
**Status:** decided and implemented in starter guidance only. Installed copies, the
v1 engine and actual host staffing behavior are unchanged and unverified.
Independently reviewed on November 7 alongside the SitRep change; the
[validation cases](DESIGN_NOTES.md#occasional-lighter-tier-staffing--november-5-2026)
remain pending.
**Extended, November 7:** An ordinary compatible update is named as a case that fits
the lighter tier at high effort, or the strong tier at medium (OPERATIONS now says a
guide may name such a case; its independent review uses the strong tier at high
effort); see
[R11](#r11--update-from-a-pinned-public-source-without-replacing-project-state).
**Extended, later November 7:** Settings are now set explicitly on every dispatch and
the strong default is the strong tier at high effort; see the entry at the top of this
decision.

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

**Clarified, October 30 — stewardship does not add an outcome owner:** Useful
specialist responsibilities remain selectable knowledge. Their existence alone
does not require another manager, approval or handoff for a small coupled task.
A small assignment may use a matching worker directly, with evaluation and rework
retained by its accountable owner. Consequential work spanning implementation,
verification and delivery still needs one owner for that complete result, rather
than an owner per specialty. [DIRECTOR](../pattern/engine/DIRECTOR.md),
[REQUEST_MANAGER](../pattern/engine/REQUEST_MANAGER.md) and
[DIRECTION](../pattern/engine/DIRECTION.md#assign-bounded-work) preserve existing
review, release and user authority. The regression is a tiny source-map report
that can finish through one maintained clerk, compared with an engine/UI/package
outcome that needs coordinated specialties through usable delivery. Actual bounded
observations and their limits are recorded in
[validation notes](DESIGN_NOTES.md#role-knowledge-and-actual-host-trials--october-30-2026).

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

**November 7 — fix runtime failures in runtime text:** The audit behind the
[dispatch-settings rule](#r2--protect-judgment-and-conversation-from-executionbookkeeping)
found that an earlier review had recorded the correct principle (explicit choice at
dispatch, no inheritance by omission) only in this rationale, which receiving agents
do not load, so the observed failure recurred. The maintainer added a rule to the
repository's [maintainer instructions](../AGENTS.md): when an observed failure is
runtime behavior, fix it in runtime text, not only in the rationale or design notes.
This adds no startup read for target actors. **Why/tradeoff:** a design note records
the reason but cannot change what a loaded instruction says; the cost is that each
runtime fix also needs the existing regression oracle and a payload change that
installations must update to receive. **Regression case:** a review of a runtime
failure that edits only RATIONALE or DESIGN_NOTES, with no runtime text change or
stated reason none is needed, is incomplete. **Status:** decided by the maintainer and
written in the maintainer instructions; whether authors follow it is unverified.

**October31 maintainer guard:** Before accepting a refactor, replacement default/
onboarding route or recommended alternative package, read each affected
owning decision from the prior recommended path, even if its files remain unchanged.
Account for transitively unreachable behavior/triggers and document each purpose/
failure prevented, the actual active
instruction/runtime route, and a concrete regression oracle. Preserve the mechanism,
verify a replacement, or explicitly review a dated supersession/tradeoff; unknown
or omitted obligations block acceptance. Independent review examines this
[design-obligation disposition](BEHAVIOR_PARITY.md), not merely source diffs or a
green test total. This follows the observed failure to carry forward documented
update/continuity/record obligations during the first flat implementation. It adds
no universal startup read for target actors; the maintainer loads it at the actual
refactor trigger. Do not invent a historical reason that the owning source never
stated. The matrix's dated review-accounting separates observable coverage loss
from the process interpretation explaining why a new recommended path escaped it. Preserve failed work and dated corrections as evidence.

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

**November 16 — visual workshop leaves the shipping checkout:** The maintainer
decided that the Tinka application, restoration packages, board metadata and visual
experiments belong in the separate development workspace. This supersedes the
November 14 statement that this repository retains the entire public workshop.
Generic rationale, contracts and tests remain here; the installable method is
unchanged. Preservation replaces deletion: move the complete visual workspace,
including ignored local state, retain a recovery copy, and rebind its current app
configuration and authoring pointers. Historic evidence stays unchanged.

**Intent disposition:** R8's self-contained installation and separation of method
from authoring tools are preserved. The former repository-local TINKA.md route is
removed; development-workspace guidance now routes to its local TINKA.md and app.
This intentionally removes public checkout access to the visual experiments; no
public contract or installation step may depend on those private materials.
Regression oracles: every moved file matches its preserved bytes before explicit
locator edits; board IDs, metadata and resource files survive; the relocated app
serves the same boards from its new root; the shipping checkout has no app/board
files; pattern payload bytes remain unchanged. Independent review and the executed
checks are required before accepting the move. This is a local relocation, not a
release, history rewrite or claim that older commits contain no visual material.

**Local verification:** all 778 moved files matched their preservation inventory;
independent review rechecked the archive and move with no missing files or blocking
findings. The relocated workspace validates (64 items, 11 boards), all 71 resource
paths load, and pattern payload bytes are unchanged. Current guidance and local
identity settings are the explicit post-move edits. The shipping boundary is pinned
by `test_shipping_checkout_excludes_visual_workshop`; publishing this cleanup does
not rewrite earlier published trees.

**November 14 — the maintainer's installation leaves the workshop (cross-reference):**
The maintainer's own Director installation, exact sources and preserved originals
now live in a private sibling workspace, not ignored inside this repository
([R14](#r14--commit-the-installation-with-the-project), November 14). This
repository still holds the method and its public workshop together, as chosen below.
The Consequence below, that raw conversations and internal references remain
private, now holds structurally rather than by an ignore rule. Its Revisit trigger,
unintended publication of private evidence, is the case the move guards against.

**November 1 route correction:** Supported v1 adoption examples now name
README-v1/INSTALL-v1 and their manifest explicitly; an explicit lean choice links
to that route. The current starter remains tracked-only. Reusing renamed generic
guide links had sent a deliberate v1/lean choice back to the starter selector.
The oracle follows the literal consumer link/prompt and preserves the selected
package; no new installer mode or store migration is introduced. Trial-label history
stays in development records rather than the current consumer guide.

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

**November 11 — what 🎬 certifies, how the Director's rules are checked, and the end
of the OPERATIONS-split deferral (starter revision 3.3; implemented on a branch, not
merged, published or accepted):** These three changes belong to the move of the
Director's rules into the AGENTS.md block, recorded under
[R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes).

*What 🎬 certifies.* Before (October 31 below, and R18's "preserved checked-marker
meaning"): the badge followed a passed check plus the actor's confirmation of
"complete selected reads", role and guard authority and backend binding. The
read claim existed because a hook or receipt can imply instructions were loaded when
they were not. Now: 🎬 means that the Project Director's own run of the project
section's check command, after the latest compaction or resume, reported
`evidence_matched`, and that the actor confirmed the items the check lists in
`actor_must_confirm`. The first of those items changed from "resolved Project Director
role and complete startup reads" to "resolved Project Director role". The badge no
longer claims that a chain of startup files was read, because there is no such chain:
the rules are in the host-loaded block. The project section's "read before your first
reply" files are still read completely before the check, and the badge card says they
are the instructions the actor confirms as complete and free of conflict. Cost: a
badge now says nothing about whether any card or manual was read, and whether the
host actually loaded the block is, as before, not proved by the check. The detail of
what to confirm (an intact block cannot excuse a conflicting role default or a
competing tracker elsewhere; an unrelated receipt-listed file is not a backend
declaration; an omitted guard is not checked) used to be read before every first
reply as part of OPERATIONS' installation-evidence section. It is now on
[cards/badge.md](../pattern/starter/payload/cards/badge.md), which the block's table
names only for a failed check or a change to the check or the loading route. On a
passing check the actor confirms from the four short item strings alone. That is a
weakening, recorded as such in the
[matrix](BEHAVIOR_PARITY.md#standing-block-and-cards--november-11-2026). Oracle:
`test_check_and_badge_paragraph_is_for_the_project_director_only`,
`test_card_audiences_and_moved_obligations` (the badge card holds no startup-read
claim), `test_fresh_check_is_readonly_and_does_not_claim_consumption_role_or_ledger`.
The design proposal listed the badge's meaning as the owner's call; that call is not
separately recorded here.

*How the Director's rules are checked.* Before (November 2 below): the checker
required known matching hashes for START, DIRECTOR, OPERATIONS and itself, so an
edited foundation could not sit under a badge, while AGENTS.md was project
composition whose snapshot was only reported. The update guide preserved
customizations inside the marked block. Now: on the block route the checker requires
matching hashes for WORKER.md, OPERATIONS.md, itself, the two redirect stubs and the
seven cards, and it compares the block's own bytes, marker line to marker line, with
the receipt's `director_block_sha256`. A block that differs blocks the check; the
block is managed text, and a project's own wording belongs in the project section or
the surrounding file. The rest of AGENTS.md stays project composition under the
November 2 rule. A missing, duplicated, empty or over-cap project section blocks
*(November 14: the over-cap failure is superseded; see [R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes), November 14)*. A
block that still points at START.md is the earlier route: it passes only while
START.md, DIRECTOR.md, OPERATIONS.md and the checker match their recorded baselines
and START.md is the earlier full file; once START.md is the stub, the check blocks
and names the unfinished update. The first rework let a receipt with no recorded
block baseline pass, adding only an `actor_must_confirm` item; any block that kept
the markers and named WORKER.md would then have passed. The final commit of the same
day closes that: on the block route a receipt without `director_block_sha256` blocks
the check, and the installer, generated first use and the move each record it. Cost:
a block-route project whose receipt predates the baseline is blocked until a reviewed
update records it. This narrows the October 29
and November 2 regression case "an update preserves customized text inside and
outside the hook": text inside the block is now moved out, not kept in place.
Oracle: `test_gutted_or_negated_director_block_blocks_the_check` (the review's
known-bad cases: rules gutted, negated, or one sentence reversed with the markers
intact), `test_redirect_stubs_are_hash_checked_on_the_block_route`,
`test_project_section_is_required_once_beside_the_block`,
`test_earlier_start_route_passes_only_with_its_own_full_startup_files`,
`test_old_bridge_pointing_at_the_redirect_stub_is_an_unfinished_update`.

*The November 7 deferral.* The November 7 triage deferred splitting OPERATIONS'
installation-evidence section into a short per-conversation route and an explicitly
triggered diagnosis part until the field's first-minutes tool sequence and one
post-setup conversation were measured, and proposed a static test pinning the
first-reply trigger prose before any split. The November 9 entry at the top of this
section said that deferral stayed in force. 3.3 makes the split: the per-conversation
route is the block's check paragraph, pass and fail handling is on the badge card,
and structures stay in OPERATIONS. **The deferral is superseded without its
measurement condition being met**; neither measurement was taken. The static pin now
exists in a different form (the block's check paragraph, above). The triage's own
oracle, "after any split, a blocked check still reaches the diagnosis text", is met
in text: a blocked check's `next` field names the badge card
(`test_gutted_or_negated_director_block_blocks_the_check` asserts it). Whether an
agent then opens it is not observed.

**Status:** implemented on a branch and statically tested; independently reviewed
November 11. Live: in two sessions on one host the Director reran the check after a
forced compaction and kept the badge; see
[validation](DESIGN_NOTES.md#standing-block-and-cards-starter-33--november-11-2026)
for what that does and does not show. A failed check followed by a badge-card read
has not been observed.

**November 9 — the video template reads its large docs at task time, not as startup
guards (template-local; decided and staged):** For the My Work video template only,
the three large video docs (`docs/DIRECTOR.md`, `docs/PROCESS.md`,
`docs/CHANNEL.md`), `.team/TEAM.md` and the setup `TEMPLATE.md` leave the ordinary
check's selected guards and the first-use guards. The template's Director startup
supplement, `.team/roles/director-startup.md`, makes TEAM, docs/DIRECTOR and PROCESS
complete reads before capture, intake, staffing, dispatch or any delivery step,
including render and upload; CHANNEL before intake, briefing or judging creative
work; and TEMPLATE at first use. It requires them again after compaction. A reply
may come before those reads; acting may not. In the field, a working video
project's greeting needed about 113 KB of required reads, and on a one-line note a
Director skipped the large guard docs and gave no 🎬 for the rest of the
conversation without naming the gap. The staged greeting reads about 47 KB, against
117.5 KB for the same bytes under the old route.

The November 2 rule above is unchanged for the guards that remain (the video
adapter, the startup supplement and PROJECT): they are read completely, their
snapshots are reported rather than blocking, and an unresolved conflict still
prevents the badge. The tradeoff is that the moved docs get no per-conversation
snapshot or badge-time conflict evaluation; their conflict review moves to the
template's re-stage and the video system's own approved merge. The November 7
deferral of splitting the starter OPERATIONS section stays in force; this changes
one template's guard selection, not the starter. The binding change, the full
oracle and the unknowns are recorded under
[R16](#r16--separate-replaceable-engine-from-project-owned-integration). Concrete
cases for this decision: an unhinted greeting reads only the first-reply set, runs
the check and shows 🎬; a render task reads PROCESS and docs/DIRECTOR before acting;
after compaction, a production task re-reads them before dispatch. The last case
has not been tested live. **Open, acceptance-blocking:** nothing yet checks an
unbound doc that contradicts Director authority.

**November 7 — SitRep due check and suggested shape:** recorded under
[R17](#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request); its
suggested **Waiting on you** part keeps ❓ questions and 🖐️ user-only actions visible,
and the exact **📋 SitRep** heading is unchanged. Under the no-time-source fallback,
each held-stream change, such as a worker return, gets a SitRep: a narrow refinement
of R9 October 19 that applies only without a time source.

**Later November 4 — distinguish required checking progress from the ordinary answer:**
The candidate's first Code greeting followed complete selected reads, actual setup
and a separate successful check, but an honest unbadged checking preamble appeared
before setup. The recorded higher-priority host requires commentary for tool work.
START/DIRECTOR/OPERATIONS now permit only that required pending-progress message:
no greeting/identity answer, setup/completion claim or 🎬 before the actual check.
The first ordinary answer still follows full reads, required setup, separate check
and role/guard/backend evaluation; failure retains the specific-gap/no-badge route.
This is no promise of silent startup or permission for an early checked identity.
The literal zero-visible-message metric remains unmet, and the preamble arrived
after initial reads, so blanket host-procedure compliance is not established.
The same turn's rejected extra STATE guard and subsequent correction also remain
qualifications. [Validation](DESIGN_NOTES.md#generated-project-first-use--november-4-2026)
separates the observed ordinary answer, recoveries and still-pending installed route.

**Later November 4 — validate generated receipts on the completed route:** A
receipt-present conversation correctly skips first-use setup and reaches the normal
read-only checker directly. Independent review showed that this checker accepted
a generated receipt whose native project ID was null; stricter validation inside
`ensure` alone was unreachable on that real path. The
[checker](../pattern/starter/payload/startup_check.py) now conditionally validates
the generated technical format, backend/claims and actual native identity/format,
including when an expected-ID override is supplied. Existing receipt formats retain
their supported route. No caller change, new write or setup retry is added.
The oracle is direct ordinary-checker refusal of incomplete/contradictory generated
evidence without writes, alongside preserved legacy/fresh-installer cases. Those
source/CLI cases passed independent review. Qualified candidate observations and
pending final installed-app proof are separated in [validation](DESIGN_NOTES.md#generated-project-first-use--november-4-2026).

**Later November 4 — complete verified generated first use before checking:** An
actual generated code project reproduced missing setup receipt, no badge and no
writes on ordinary greeting/identity startup. Its selected rules promised later
setup but correctly forbade initialization merely to make the first-reply checker
pass. The actual generator copied transport provenance without a durable creation
handoff. This was a missing executable lifecycle edge; more badge wording could not
create the receipt. Later explicitly prompted setup is recovery, not automatic proof.

The accepted repair inserts a distinct generated-instance operation before the
ordinary read-only check: opted-in generation emits fresh instance metadata; the
Project Director loads complete selected authority, [FIRST_USE](../pattern/starter/payload/FIRST_USE.md)
and applicable native I/O/privacy prerequisites; guarded `first_use.py ensure`
verifies that instance and selected provenance, performs only eligible setup and
writes an honest technical receipt; then the ordinary read-only checker and actor evaluation
earn 🎬. [START](../pattern/starter/payload/START.md),
[DIRECTOR](../pattern/starter/payload/DIRECTOR.md) and
[OPERATIONS](../pattern/starter/payload/OPERATIONS.md#installation-evidence) route
that order. A marker/ensure return alone earns no badge. Missing receipt alone grants
no initialization authority, and existing configured/mature projects retain their
read-only route. Workers/scoped children do neither root setup nor the check.

This narrowly refines the October 31 no-startup-write assumption for recognized
unconfigured generated instances; it adds no writes inside `startup_check.py`, setup
actor or blanket greeting initialization. Generic templates remain uninitialized;
existing identity/backend/privacy choices survive. The acceptance oracle is an actual
generator-produced pristine project and unhinted first native reply: complete reads
→ ensure → real receipt → checker/evaluation → badge, followed by a new conversation
that reuses the same identity without initialization. Seed/malformed provenance and
worker countercases must remain honest. Source components and bounded candidate
routes are checked; final installed-route proof remains pending in
[validation](DESIGN_NOTES.md#generated-project-first-use--november-4-2026);
the previous failed observations remain intact.

**November 4 — restore positive attention instructions:** The flat Director named
reserved ❓/🖐️ markers without directly requiring their use. Existing R9 intent and
legacy DIRECTION already supplied that behavior. Flat
[DIRECTOR](../pattern/starter/payload/DIRECTOR.md) now positively marks real user
questions/decisions and user-only actions, retaining grouped/tool-card handling and
no duplicated chat questions. Ordinary progress needs neither marker; 📋 remains
reserved for **📋 SitRep**, and checked 🎬 retains its separate check. This preserves
the previous recommended semantics. Source review can establish the reachable
instructions; actual questions, grouped/tool questions and user-only actions with
ordinary-progress controls are the uptake oracle. No such observation ran for this
delta; earlier badge observations do not prove these markers.

**November 4 — make checked display an explicit action:** The flat START and
DIRECTOR described when a badge was permitted, while the earlier accepted purpose
already required the checked Director to keep its reply prefix. Reports of missing
prefixes expose a display problem; they do not alone establish that the check was
skipped or why the actor omitted it. The flat START/DIRECTOR/OPERATIONS now directly
require a 🎬 prefix on every Project Director user-facing reply after its actual
current check and role/guard/backend evaluation pass, including discussion, progress
and status. Legacy Director/DIRECTION/IDENTITIES callers state the same display
rule after their selected setup route passes; the separate v1 setup route is not
silently replaced with the flat checker.

The automatic first ordinary-reply check needs no preliminary greeting. Unchanged
current-conversation evidence is reused; missing/stale evidence is checked when
currently possible. Failure or unresolved role/authority/backend gives the specific
gap and ordinary answer without a badge. Workers and scoped child Directors retain
their own identities. Higher-priority host formats still apply. No new checking
actor, tracker operation, startup history scan or badge-as-product-acceptance claim
is introduced. The oracle is successful initial check followed by ordinary status
and discussion prefixes, missing/stale recovery, failed technical or semantic
authority check without a badge, and worker/scoped-role exclusion. These instruction
changes are implemented as a source candidate; source checks, observed display and
target adoption remain separate in [validation](DESIGN_NOTES.md).

**November 2 — distinguish managed integrity from current project guidance:**
An unchanged valid installation could fail its local check after unrelated project
build guidance was appended to AGENTS. The checker had compared a historical hash
of the whole composed file as though every project-owned paragraph were immutable
Pattern payload. This was an inspectable integrity-boundary defect; it did not
establish an instruction-consumption or native-host failure.

The corrected [checker](../pattern/starter/payload/startup_check.py) keeps strict
known matching hashes for START, DIRECTOR, OPERATIONS and itself, plus the existing
safe-path, bounded-read, provenance and actual backend/config checks. Current
AGENTS and explicitly selected project-owned guards are safely read; their historical
snapshots are reported as unchanged, changed or not recorded. Malformed/conflicting
recorded baselines still fail. Exactly one supported ordered marked hook, outside
Markdown code examples, must point to the selected START route. It defaults to
AGENTS; an explicit project-relative `--hook-source` selects a shared marked file.
Outer AGENTS is always read, along with the exact selected source and explicit actual
host/shared/role guards. No search for a convenient passing hook occurs. Missing,
duplicate, unsupported or misdirected selected hooks fail specifically. A marked reference establishes
structure, not that a host loaded it or that its surrounding prose is compatible.

This narrowly supersedes R9/R10's requirement that every selected project-owned
instruction match an installation-time hash. It does not relax managed-file
integrity, full current reads, selected Project Director authority or actual backend
binding. Under [OPERATIONS](../pattern/starter/payload/OPERATIONS.md#installation-evidence),
the actor must read and evaluate the complete current instructions, including
conflicting role defaults, disabled checks or competing authority outside the hook;
an unresolved actual conflict still prevents the badge. Legitimate project guidance
remains binding. Receipt rewriting cannot replace that evaluation.

**Tradeoff and oracle:** Project composition no longer produces a false broken-install
result merely because its snapshot changed; semantic compatibility remains an explicit
actor judgment, not a helper guarantee. Append unrelated build guidance and require
managed integrity plus supported route structure to match, with changed project
snapshot disclosed. Change a managed foundation, remove/misdirect the hook, supply an
unsafe guard, or introduce a real authority conflict: the applicable technical or
actor check must still fail. Workers/scoped child Directors retain their exemption.
[Validation](DESIGN_NOTES.md#portable-reconciliation-and-composed-project-guidance--november-2-2026)
separates deterministic source checks from native behavior and adoption. R11's
[preservation protocol](#r11--update-from-a-pinned-public-source-without-replacing-project-state)
continues to govern actual instruction changes and receipt updates.

**November 1 scope clarification:** The first-reply check belongs to the actual
Project Director, whether defaulted or explicitly selected. An assignment is not
an exemption for that role. Workers and scoped child Directors still skip it;
complete selected reads, known guard/backend evidence, checked-only 🎬 and a normal
same-turn answer on failure remain. The concrete oracle exercises all four role
selections, not just an unassigned greeting.

**October 31, 2026 — automatic first-reply check:** A later ordinary native greeting
exposed an active-route gap after the earlier scoped release: the host hook said
before task work, START only conditioned the badge, DIRECTOR permitted unchecked
discussion, and OPERATIONS waited for staffing/active work. An identity follow-up
loaded the role but treated the check as optional; a badge question read more prose
without performing the described check. This is an observed trigger/execution gap,
not evidence of stale files, a deliberate policy choice or a model-level cause.

The Project Director now loads its package even for the first greeting and directly
runs one concrete bounded read-only local evidence check before the first ordinary
reply. A badge question retries currently available evidence rather than only
explaining omission. The helper checks exact receipt/source, selected route/guard
hashes and applicable config header or explicit lean/custom contract; it returns
evidence, not role authority or complete installation approval. The actor must
confirm complete selected reads, role/shared authority and actual backend binding.
If a required fact is unavailable, answer normally with the specific gap and no
badge. Workers and scoped child Directors skip this Project Director check.

No checker actor, network, tracker import, request/source/history read, store init
or startup write is added. Keep the evidence in active context; persist later at
an ordinary authorized checkpoint. This minimal technical inspection does not
activate full tracker manuals or weaken their later capture/mutation/recovery gates.
Correct lean/manual backends need no generic JSON store; transport-only template
provenance does not become a configured setup receipt. Relevant changed files are
[hook/installer](../pattern/starter/install.py), [START](../pattern/starter/payload/START.md),
[DIRECTOR](../pattern/starter/payload/DIRECTOR.md),
[OPERATIONS](../pattern/starter/payload/OPERATIONS.md) and
[startup_check.py](../pattern/starter/payload/startup_check.py).
The focused [validation](DESIGN_NOTES.md#first-reply-startup-check--october-31-2026)
separates observed native CLI turns from desktop/other-host guarantees.

**October31 starter correction:** R18 restores checked identity, sparse attention
markers and periodic labeled SitReps; a direct owner check replaces the compulsory
setup actor without changing the 🎬 operational-check meaning. Earlier checked-badge reasoning remains below.

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

**November 15 — the agent that starts a session names a worker one (starter revision
3.9; handles the cost recorded for 3.8 in the entry below):** Starter 3.8 made any
session that nobody names a worker its project's Director, and recorded the cost: a
Director that briefs a subagent without naming it a worker gets a Director. Three
observations that day, on the desktop host, bear on that cost.

**Observed, November 15.**
1. *Subagents carry the parent's start-time instructions.* A probe ran from a session
   that started before its block was updated to 3.8 in that same session. Its
   subagent received the AGENTS.md the parent had loaded at its start, not the
   current file, so it ran the old 3.7 block and called itself a worker under the
   report-back test. Host fact, as observed: subagents get the parent session's loaded
   instructions, so after an in-session block update, that session's subagents keep
   the old block until a new session starts. This probe therefore says nothing about
   3.8's wording.
2. *A host-defined search helper did no startup reads at all.* Whether it received
   AGENTS.md and ignored it, or never received it, is not established.
3. *A valid trial on 3.8.* From a Director session started after the 3.8 install, a
   general-purpose subagent given a brief with no role had the 3.8 Worker line. It did
   the lookup itself, with no check, no 🎬 and no read of WORKER.md. Asked its role, it
   said it had not chosen one; it agreed that by the text it was the Project Director
   and called skipping startup a gap. So a roleless subagent is nominally a Director
   but does not behave as one consistently: here it acted as neither.

**Decided by the maintainer, November 15:** the 3.8 risk is handled on the creator's
side. A subagent should not be created without being defined as a worker.

**Implemented, as wording (starter revision 3.9).** Duty 5's role
item now reads "role (tell each worker it is one: any agent you start unnamed, even a
host helper, counts as a Director)", so the rule sits in the always-loaded text the
starting Director has in hand when it writes the brief. In review, "tell each worker
it is one" replaced a first draft's "name each worker one", which could be read as
"give each worker a name", and "counts as a Director" replaced "is a Director". The
starter README's 3.9 paragraph says such an agent "counts as a Director under the
block, though it may not act as one". The staffing card's Role line now says
"Tell every worker, helpers and lookups too, it is one and to read
`.director/WORKER.md`". The role paragraph drops "Default to Project Director unless
explicitly assigned a worker or scoped child Director role." (below). The manifest is
3.9 and the starter README has a 3.9 paragraph. The block is 8,396 bytes (8,391 at
3.8); the staffing card is 6,499 (6,473), one byte inside its
6,500 budget.

**Design-intent disposition of the removed Default sentence.** *Affected:* the
sentence in the role paragraph, which descends from the November 1 decision below
("role assignment is not a user task") that the host-loaded hook state the Project
Director default unless a worker or scoped child Director role is explicitly
assigned. *Purpose and failure prevented:* an ordinary assigned task must not read as
excluding the Director default, and a session without a role assignment must reach
its Director. *Disposition:* the meaning is kept by the three role bullets directly
below it, which since 3.8 say the same thing in more detail: "Worker: only if this
project's Director, the user or an explicit assignment names you one", the scoped
child Director bullet, and "Otherwise you are the Project Director, whoever or
whatever started you". A task that names no role is not a naming, so it falls to
"Otherwise". The sentence repeated the bullets, and after 3.8 its "explicitly
assigned" was a looser wording of the worker bullet's "names you one". Dropping it
saves 95 bytes, which pays for most of duty 5's addition. The regression oracle moves
to the bullets' pins.

**Why/tradeoff.** The rule now lives with the actor who can keep it: a Director
writing a brief can always name the role, while a started session cannot reliably
tell from its own context what it was meant to be (observations 1 and 3). The text
still says what an unnamed session is, so the receiving side keeps a defined answer.
*Cost:* nothing on the receiving side changes. A Director that forgets still starts a
nominal Director that may not act as one (observation 3), and a host helper whose
prompt the host writes may read no startup at all (observation 2), which no brief
fixes. Saying in duty 5 that an unnamed host helper "counts as a Director" states
what the text makes it, not how it was seen to behave. The staffing card now has one byte of
budget left.

**Regression cases:** A Director that starts a lookup or a host helper names it a
worker in the brief, and the helper reads WORKER.md if it does any startup. A
subagent started with a brief that names no role and no worker is the stated failure
of the starting Director, not of the subagent. After a Director updates its block
inside a running session, its subagents are tested only from a new session, because
they keep the parent's start-time instructions. A task brief that names no role still
leaves the reader under "Otherwise", with the Default sentence gone.

**Status.** Decided by the maintainer on November 15, 2026. Implemented as wording in
starter revision 3.9 and published on `main` with this change; no installed project
has it. Verified statically: the full suite passes, 298 tests, and the new wording is
pinned by the four tests in `HelpersAreDirectorsNovember15Tests` in
`test_block_route.py`, with the existing pins updated to 3.9; the pins of the Default
sentence now assert its absence from the block. These are wording pins only
([validation notes](DESIGN_NOTES.md#whoever-starts-a-session-names-a-worker-one-starter-39--november-15-2026)).
Not verified: a live trial of a named against an unnamed subagent on 3.9, from a
session started after the 3.9 install, is pending.

**November 15 — a worker is a session a Director names as one; an unnamed session is
the Director, whoever started it (starter revision 3.8; supersedes the November 11
narrowing, item 5 below, and restores the October 17 default and its regression
case):** In fresh host trials on November 15, sessions that the desktop app started
from a Director session resolved their role inconsistently: twice as that project's
Director, once as a worker. The worker case cited the block's worker line, "spawned
by another agent to do a task and report back without being named a Director". The
host's session-start text tells every session it starts that its report goes back
to the session that started it, so every agent-started session matched "report
back", whether or not anyone meant it to be a worker. The November 11 rule sorted
readers by the shape of the start, and on this host that shape is the same for every
session an agent starts.

**Decided by the maintainer, November 15:** Directors will be started by other
agents more often than by people, for example a Director opening a session in
another project. A worker is a session a Director names as one; a Director opening a
worker knows it is doing so. A session nobody names defaults to Director. The
maintainer noted that this was the rule's first definition (October 17, below) and
called the finding critical for scaling, as systems come to talk to systems.

**Implemented, as wording (starter revision 3.8).** The block's worker line now
begins "Worker: only if this project's Director, the user or an explicit assignment
names you one", and its default line reads "Otherwise you are the Project Director,
whoever or whatever started you, even if it expects a report back"; the rest of each
line is unchanged except as listed below. "The user or an explicit assignment" keeps
the block's existing assignment and opt-out wording; it is not part of the
maintainer's decision, which names only a Director. The requests card keeps its role-naming sentence and
replaces its reason: unnamed, the session "is still that project's Director". The
update-check card keeps its example first message and says the same: "Unnamed, that
session is still the project's Director; naming the role makes that plain." The
staffing card's Role field now says "Tell every worker it is one and to read
`.director/WORKER.md`". The manifest is 3.8 and the starter README has a 3.8
paragraph. The block is 8,391 bytes (8,355 at 3.7); the requests card is 6,475 (6,497), the staffing card 6,473
(6,459) and the update-check card 3,179 (3,166).

**Added by the Director after the independent review, November 15; open to the
maintainer's review.** Three more block edits, each with its reason:
- The worker line says "this project's Director", not "a Director". This is the
  Director's decision, in line with the maintainer's 3.7 decision that another
  project's Director is a peer: a brief from another project's Director does not by
  itself make a session here its worker, so its ask still lands in this project's
  records. "An explicit assignment" could still be read to cover such a brief; the
  role paragraph's peer sentence points the other way.
- The role paragraph's first sentence reads "**Your role**, once set, never changes on
  another agent's or session's message", because a Director's brief is now the only
  way to make a worker, and that brief is itself another agent's message; the role
  is set at the start and not changed later.
- The default line ends "General host instructions name no role and are no opt-out",
  so a host's session-start text, such as the report-back wording seen in the trials,
  sets no role.

**Design-intent disposition.** *Affected:* item 5 of the November 11 entry below,
kept as written with a dated note, and the passages that relied on it (the 3.7
reading of the role gate and the reason for its role-naming sentence, the November
11 regression case for a spawned report-back agent, and the R11 note on an update
session's first message), each now carrying a November 15 addition. *Purpose and
failure prevented:* item 5 kept a spawned helper whose brief left out its role from
taking Director authority on hosts that pass AGENTS.md to subagents. That failure was
a reading of the text, not an observation. Item 5 stated its own cost: the role is
inferred from the shape of the spawn, which October 17 forbade, and a peer-project
session opened without a role arrives as a worker with no Director in that project.
That cost is what the November 15 trial then showed, in one case of three.
*Disposition:* restore October 17's default, a project session is that project's
Director whoever opened it and roles are not inferred from ancestry or tool type,
with its regression case "a session opened in a peer project by another director
serves as that project's director by default". Keep item 5's purpose through the
brief instead of the shape of the start: duty 5 has every brief state the role, and
the staffing card now has every brief tell a worker it is one. *What stays from November 11:*
another agent's or session's message never changes a role once a session has one;
only the user or an explicit assignment opts a session out of acting as Director;
workers and scoped child Directors skip the check and 🎬.

**Also superseded, November 15: "clarify, never default" on the block route.**
October 17 below said a delegated assignment with no role "seeks clarification before
role-specific action"; October 23 says "malformed bounded assignments clarify, never
default", with the regression case that "an incomplete delegated assignment cannot
become Director"; and October 24 says malformed delegated assignments "still clarify
without falling into the Director default". Their text stays below as history. The
maintainer's November 15 decision settles these cases too: a session that is not told
it is a worker defaults to Director, and a worker must be named as one by a Director.
So on the block route a brief with no role makes a Director; it does not seek
clarification. November 11 had already dropped the clarification step there; 3.8
records the replacement as decided. What stays: WORKER.md's "Missing or conflicting
assignment details return to the assigner" still applies to a session already named
a worker that is missing other details, such as its scope, authority or return route;
those details never make it a Director.

**Cost, stated honestly.** A Director that briefs a subagent without naming it a
worker now gets a Project Director on hosts that pass AGENTS.md to subagents: it
runs the check, shows 🎬 and holds Director duties for whatever it was sent to do.
The expected case, not yet observed, is a one-line lookup sent to a built-in search
helper. *Observed, November 15:* on the desktop host, a subagent that a Director
started with a written brief did receive the workspace's AGENTS.md, so on that host a
brief without a role makes a Director. The mitigation is duty 5 (every brief states
the role) and the staffing card's "Tell every worker it is one"; neither guards a
brief the Director did not write. Whether built-in helpers whose prompts the host
writes receive AGENTS.md is still unknown.
*Later November 15 addition:* three more observations that day (R10, November 15,
3.9) refine this. A valid 3.8 trial of a roleless general-purpose subagent found it
nominally a Director but running no startup, and a host-defined search helper did no
startup reads at all; an earlier probe that ran the old block reflected the host
giving subagents the parent's start-time instructions. The maintainer decided the
risk is handled on the creator's side, and starter 3.9 puts the naming duty in duty 5.

**Regression cases:** A Director opens a session in another project without naming
its role; that session is the project's Director, runs its check and captures the
ask under its own rules. A session the desktop app starts from a Director session,
whose start text says its report goes back, is a Director unless its brief names it a
worker. A subagent whose brief names it a worker reads WORKER.md and shows no check
and no 🎬. A running Director that a later agent message calls a worker keeps its
role. A subagent briefed without a role on a host that passes AGENTS.md acts as a
Project Director: that is the stated cost, not a pass.
*Later November 15 addition:* observed once on 3.8, such a subagent was nominally a
Director but ran no startup (R10, November 15, 3.9).

**Status.** Decided by the maintainer on November 15, 2026; the three later block
edits above are the Director's, open to the maintainer's review. Implemented as
wording in starter revision 3.8 and published on `main` with this change; no
installed project has it. Verified statically: the full suite passes, 294 tests,
and the new wording, including the three later block edits and the starter README
paragraph, is pinned by the six tests in `RoleDefaultNovember15Tests` in
`test_block_route.py`, with the existing role-gate and peer pins updated to 3.8
([validation notes](DESIGN_NOTES.md#a-worker-is-named-as-one-starter-38--november-15-2026)).
These are wording pins only. Not verified: the live trial of an unnamed
agent-started session and a trial of an unnamed subagent are pending.

**November 14 — another project's Director is a peer, not your worker (starter
revision 3.7; carries onto the cards and block the October 17 peer-project decision
below, as narrowed November 11 (item 5), and
[R5](#r5--preserve-the-four-outcome-restart-truth-across-ownership-boundaries)'s
"receiver owns its requests"):** A Director's work needed an answer that belonged to
a sibling project with its own Director. It did not go and ask on its own; the user
had to tell it to. When it did start a session there, its brief told the receiver to
change nothing and only report back. The receiver acted as that project's Director,
but it followed the brief over its own duty to capture the request, so the ask never
entered that project's records and the receiver did not work the way its project
works.

**Contributing causes.** Nothing in the shipped text said that another project may
have its own Director, or that a question belonging there should go to it. The
staffing card's routes paragraph said the same responsibility, authority, owner and
return contract "carry across" separate sessions and external routes, which reads as
the sender's contract binding the receiver. The asking project had its own rule to
treat other projects read-only, which began as a product rule for an app and was
applied to its Director's conduct. The host's session-start wording describes some
sessions as read-only pieces, which supplied that label. *Reading of the text,
not observed:* under the block's role gate, an agent started to do a task and report
back without being named a Director counts as a worker, so a session opened without
its role could arrive as one. In this case the receiver did not; it acted as a
Director and still deferred to the brief. *November 15 addition:* that reading was
then observed. In one of three fresh host trials, a session the desktop app started
from a Director session arrived as a worker and cited that line; starter 3.8 removes
it (R10, November 15).

**Decided by the maintainer, November 14 (the approved draft):** a Director knows other projects may have
their own Director, who owns that project and how it works, and takes a question or
task that belongs there to that Director as a peer, without the user having to say
so. The consulted Director decides how to work, including capturing the request and
writing in its own project. The asker limits only what it sends and what it asks for.
Disclosure limits, and the host's, the user's and each project's gates, are
unchanged. The maintainer approved this draft of the requests-card paragraph and the
staffing card's rewrite of its routes paragraph; "what it asks for" is that draft's
wording.

**Added by the Director in review, not separately approved by the maintainer:** the
requests card's role-naming sentence ("You are this project's Project Director"),
because of the role-gate reading above; the staffing card's cut of its duplicate
ownership sentences, to fit the card budget; the review rewording of the requests
paragraph, which ties it to the work in hand ("When your work needs a question
answered or a task done"), places the host's, user's and each project's limits on
sessions and messages next to "need not wait", adds the sentence that what you send
may land in that project's records, so send only what may go there, and drops "what
you ask for" from what the asker limits; and two block lines, because most
Directors make this routing choice before they open any card. Duty 1 maps a request
onto its established mechanism and owner "including another project's own Director,
as a peer, for work that belongs there"; the role gate adds "Another project's
Director asking you something is a peer making a request here, under this project's
rules."
*November 15 addition:* the role-naming sentence stays in 3.8, but its reason
changes. An unnamed session there is now still that project's Director, so naming
the role makes it plain rather than keeping the session from arriving as a worker
(R10, November 15).

**Implemented.** The requests card gains a paragraph after the partner paragraph:
other projects may have their own Director; take a question or task that belongs
there to that Director as a peer, without waiting for the user, within the host's,
user's and each project's limits on sessions and messages, and propose the session
where only the user can start it; name its role when opening a session there; say
who asks and why, the question, and what is needed back and where; what you send may
land in that project's records, so send only what may go there; that Director decides
how to work; neither side's message or link gives authority over the other's records;
and a Director asked by another treats it as a request to its own project, under its
own rules. The staffing card's routes paragraph now says "Work you staff keeps" its
contract across routes and that another project's Director is a peer, not your
worker, pointing to the requests card; its disclosure, unavailable-route and
recording sentences are unchanged, and "Specialists and project departments keep
their own authority" joins it. To stay within the card budget, the card drops its
copy of "You keep the whole usable result through evaluation and rework. A
sub-director's acknowledgment does not release you." Both rules still ship in the
supervision card, which a Director reads before evaluating a return ("Each outcome's
owner keeps the whole usable result"; "a subordinate Director's acknowledgment does
not release the parent"), and the requests card keeps the Project Director's
acceptance of the whole. A first draft instead cut the record bullet's "(size, how
easily it is checked, consequence of error)" and the route qualifiers "configured"
and "acknowledged"; that was reverted, because those words carry the November 7
dispatch-settings decision under [R1](#r1--one-accountable-conversation-without-a-forced-organization)
and the route contract, and decided wording is not cut just to fit a budget. The
[design-obligation matrix](BEHAVIOR_PARITY.md) records the narrowed same-contract row.

**Why/tradeoff:** The fix states intent and awareness rather than a protocol: no
message format, handshake or read-only mode is added. The block carries the intent
because the choice to ask another project comes before any card is read; the cards
carry how. The block grows by 191 bytes to 8,355, under the 10,000 alarm. The risk
is a Director that routes to another project too readily, or a receiver that writes
in its project when the asker wanted only an answer; the asker says what it needs
back, and the receiver's own rules and gates govern what it does. The update rule on
the update-check card is unchanged and more specific: a session in another project
for a Director Pattern update still starts only when the user asked for that update.

**Regression cases:** A Director whose work needs an answer from a sibling project
with its own Director takes it there without being told, opens a session naming it
that project's Project Director, says who asks and why, the question and what it
needs back, and does not tell it to change nothing; the receiver captures the request
in its own store and answers under its own rules. On a host that lets only the user
start sessions, the Director proposes the session instead of claiming it ran. A
Director asked by another Director treats the ask as a request to its own project.
A brief to another project carries only what may land in that project's records.

**Status.** Decided as above on November 14, 2026. Implemented in the working tree as
starter revision 3.7; the full suite passes, and the new wording is pinned by the five
tests in `PeerDirectorsNovember14Tests` in `test_block_route.py` ([validation notes](DESIGN_NOTES.md#other-projects-directors-are-peers-starter-37--november-14-2026)).
Not committed or published. No live session between two projects' Directors has
been run.
*November 15 addition:* 3.7 is now published on `main`.

**November 14 — a project's AGENTS.md belongs to the project; the pattern states no
byte limit on it (supersedes the November 11 byte caps as limits on projects):** The
November 11 entry below gave the standing text three caps that the starter enforced
on the project: the installer refused a Director block over 8,000 bytes and a project
section over 3,000, the update guide told an updater the block and section "stay
within" those sizes, and the startup check blocked an over-cap section. The reason
was sound: that text is paid for on every turn by every agent the host gives the file
to, so it should stay small. The failure was in the placement. A caps rule written
for the text we ship was applied to the project's own file.

**Failure case.** A project kept its own longer `director-pattern:start` and
`director-pattern:end` marker lines, which is what the guide's own correction
(November 13, under [R11](#r11--update-from-a-pinned-public-source-without-replacing-project-state))
tells it to do. The shipped block was 7,997 bytes, so three bytes of room; the
project's markers took the installed block to 2 bytes over 8,000, and the starter 3.4
update stopped to ask the user. The project did nothing wrong: it followed the guide.
Its AGENTS.md was one chunk of text it owns.

**Decided by the maintainer, November 14:** a project's AGENTS.md belongs to the
project. The Director block is one chunk inside it, a managed chunk the project keeps
byte for byte but does not have to fit into a size we picked. The shipped pattern no
longer states or enforces a byte limit on that file, on the installed block or on the
`director-project` section: the installer's refusal, the update guide's "stay within
8,000 and 3,000" and the check's over-cap section failure are removed. A project
decides how much standing text it carries. A host's own instruction limit, which
varies by host and version, is the host's. The update guide still measures the
result against that host cap and, if the file would pass it, reports what would be
cut and lets the owner choose, never trimming project text silently. It restates no
number of its own.

**What stays, as a maintainer rule.** The budgets for the text this repository ships
(block about 8,000 bytes, each card 6,500, WORKER.md 4,500, the section template
3,000) *(later November 14: the block's figure is now a target near 8,000 with an alarm
past 10,000; see [R1](#r1--one-accountable-conversation-without-a-forced-organization), November 14)* become authoring rules in this repository's AGENTS.md, in a sentence after
the `starter_revision` rule, checked before publishing a starter revision. A test
that checks the shipped files against those budgets replaces the tests that pinned
the project-side limits
(`development/tests/test_authoring_budgets.py`). Their purpose is unchanged: keep the standing per-turn
text small, because a larger block costs every project that adopts it. That is a
design goal for what we ship. It is no longer a condition a project must meet to
install or update.

**Design-intent disposition.** *Affected:* November 11's cap statements (item 9, the
installer sentence, the over-cap check) and the November 13 byte-fit tightening it
sits beside. *Purpose and failure prevented:* standing text that grows unnoticed until
every turn is expensive. *Disposition:* preserve the purpose as an authoring
discipline on the shipped text; supersede the limit on the project's text. *Also
dropped:* update-guide step 5's 24 KiB whole-file threshold, which reported what
would be cut once the whole instruction file passed it. Its purpose was to leave room
for nested instruction files under a host's combined cap; its disposition is that
only the host's own cap is measured now, and the guide restates no number. Nothing
else in the route changes: the block must still match its recorded hash, and the
project section must still exist once and hold a check command.

**Tradeoff.** A project can now grow its AGENTS.md without the
pattern warning it, and the pattern's only guard on the shipped text is a maintainer
check run before publishing, which a skipped check would miss. That is accepted,
because the cost of an over-long file lands on the project that owns it, and a
stop-and-ask on a text the project did not write is a worse failure.

**Regression cases:** A project with its own longer marker lines, whose installed
block therefore measures over 8,000 bytes, takes an update without stopping to ask,
and its check reports `evidence_matched` and `director_block: unchanged`. A project
section over 3,000 bytes no longer blocks the check or the installer, while an empty
or missing section, or one without a check command, still does. A published starter
revision whose shipped block, a card, WORKER.md or the section template exceeds its
budget fails the maintainer's pre-publish check.

**Status.** Decided by the maintainer on November 14, 2026. Implemented in the
working tree as starter revision 3.5: the installer refusal and the check's
cap fields and over-3,000 failure are removed, update-guide step 5 says the project
owns AGENTS.md and no size limit applies or blocks the update, step 7 blocks only on
an empty project section or one without a check command, and the budget sentence is
in this repository's AGENTS.md. The tests that pinned the old limits are replaced.
`development/tests/test_authoring_budgets.py` holds
`test_shipped_block_cards_worker_and_section_template_fit_their_budgets` and
`test_budgets_are_not_shipped_as_limits_on_a_project`. The field regression is
`test_project_marker_lines_take_the_block_over_8000_bytes_and_the_update_and_check_pass`,
with `test_installer_and_check_set_no_size_limit_on_the_block_or_section` and
`test_a_project_section_over_3000_bytes_passes_and_reports_its_size`. Implemented and
tested in the working tree (the full suite passes, 278 tests, as the Director
reported); not committed or published, and no installed copy has taken 3.5 *(later
November 14: published on `main`)*. An
independent review passed with low-severity wording fixes, which were applied. Until it
ships, the earlier passages that state the caps as limits on a project describe the
published 3.4 behavior, and each now points here.

**November 13 — a call in a roster role's domain goes to that role, from the Director
too (starter revision 3.4):** October 21 below decided that "no generic engineer
substitutes for a matching maintained role", and the staffing card keeps "a general
worker never silently replaces a maintained role". Both govern whom the Director
staffs, not what it answers itself. In the field report recorded under
[R18](#r18--start-flat-and-make-learning-an-explicit-bounded-loop) (November 13), the
project had a packaging role whose file held an explicit rule about how large a claim
a title or thumbnail may make. When the owner raised his own title and thumbnail in
conversation, the Director judged them itself, raised a worry that the role's rule
already answered, and was corrected twice. Duty 2 let it answer "discussion, simple
lookups and acceptance judgments" with no exception for a call a role owns, so its
place in the route let it bypass the role that reads the rule. A project-owned cause
contributed: the project's own packaging-check guidance did not send that check to
the packaging role. That guidance is the project's, and the project is changing it
on its own authority; this entry changes only the pattern.

Duty 2, the staffing card's first rung and the requests card's "answer discussion
directly" now add: a judgment, draft or rule in a roster role's domain goes to that
role, even in chat. The staffing card adds that accepting a return against the whole
request stays the Director's. This extends October 21's no-substitution to the
Director. The Director still routes from the roster row and the role file's selection
and authority part, never from the role's craft knowledge. So that a domain stays
visible when a roster grows, the installer's project section now says to keep one
line per role's domain in the section if the roster moves to a file; existing
sections are project-owned and do not get that sentence from an update.
**Cost:** a routed remark costs a normal capture and brief like any other dispatch.
That is intended: the call then reaches the role whose file holds its rules. A
Director may also route a remark that needed no specialist, and the domain is judged
from a roster row that can be stale. **Regression cases:** the owner asks in chat
what the Director thinks of a title, and the project has a packaging role: the
Director captures the question and briefs that role instead of judging the title; a
project with no matching role gets a direct answer; the Director's acceptance of a
returned result against the whole request stays its own.

*November 14 addition:* the 8,000-byte cap named in the next paragraph is now an
authoring budget for the shipped block only, no longer a limit on a project's installed block
([R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes), November 14).

To fit the 8,000-byte cap without dropping a rule, the same revision tightens six
block phrases and keeps their meaning: the gate's "project/host authority, the user's
authority" becomes "project, host and user authority"; duty 2 drops the "Directors,"
vocative inside the Directors-only duties and says "evaluate returns"; the Reading
rule says "Cards, WORKER.md and the table's manuals"; the knowledge row says "look up
knowledge" and the update row "a Director Pattern update anywhere". The knowledge
row's trigger also becomes "close an outcome, or hold or brief a retro".

**Narrowed, not only tightened: the Roster rule.** Before: "Before dispatch read the
selection and authority part of any role file the row or section names; the rest is
for its executor." Now: "Before dispatch read only the selection and authority part
of the role file its row names." Two things change. A permission ("the rest is for
its executor", which left the rest unread but allowed) becomes a limit ("only"), in
line with the accepted rule that the Director routes from roster summaries and does
not read the executor's craft. And the file is the one the role's row names; a role
file reached only through the project section's locator is no longer named by this
sentence, though the section's own role-file line still says to read its selection and
authority part. The October 30 behavior (the staffer reads the selection and
authority part before dispatch) is kept. The block is 7,997 bytes. The staffing card
is tightened the same way to stay within 6,500 bytes ("that owns its sub-request and
staffs its workers", "host controls", "as chosen above, and set in the host's
controls", and "at every depth" moved into the opening line), with meaning kept. This checkout's own root
AGENTS.md keeps the 3.3 block until its own reviewed update; the package test now
accepts there either the current block or the published 3.3 block, byte for byte, by
hash.
*November 14 addition:* that package test is superseded. This repository's AGENTS.md
carries no block; `test_public_checkout_claims_no_local_installation` and
`test_public_clone_tracks_no_installation_and_still_ignores_one` assert it. The block
now sits in the private sibling workspace, under that workspace's own check
([R14](#r14--commit-the-installation-with-the-project), November 14).

**Status:** Decided by this repository's Project Director on November 13, 2026, from
the maintainer's field report, and implemented in the starter source as revision 3.4.
An independent review the same day, with its findings applied, accepted it; the
maintainer's acceptance and publication are pending. Static tests only; no live run
yet, and installed copies keep their adopted text until updated. Oracle: `test_a_call_in_a_roster_roles_domain_goes_to_that_role_even_in_chat`
and the updated pins in `test_block_route.py` and `test_package.py`.

**November 11 — the Director's standing rules move into the AGENTS.md block; detail
moves to cards read before named actions (starter revision 3.3):** The November 9
sentence below asks an agent to read START and its role package again after a
compaction. Two things were then seen. A November 9 draft of a short block plus
separate cards was tried on one host in two sessions with one forced compaction each:
after the compaction neither session opened any card, and the card that held the
recovery steps was missed before the first project action. In the matching control
sessions on the 3.2 route the agent did re-read DIRECTOR completely, but OPERATIONS
only partly in one of two. The November 7 investigation quoted below had found no
complete startup re-read after any of 21 compactions. The working inference, still a
hypothesis, is that a rule which must hold after a break has to sit in the text the
host restores by itself, and that a file behind a trigger is not reliably opened.

**Decided, November 11:** the owner decided to build the refactor with recovery moved
into the always-loaded block. That decision is the only one recorded here as the
owner's. The individual changes of meaning listed below are implemented on a branch;
where one needed its own owner call in the design proposal, that call is not recorded
in this entry and stays acceptance-blocking.

**Implemented on a branch as starter revision 3.3 (not merged, not published, not
accepted):** the [installer](../pattern/starter/install.py) writes a marked Director
block from [agents/block.md](../pattern/starter/agents/block.md) into the project's
root AGENTS.md (7,993 bytes; the installer refuses above 8,000), followed by a
project-owned section from
[agents/project-section.md](../pattern/starter/agents/project-section.md) (cap 3,000
bytes). *(November 14: the installer's refusal and the section cap are superseded as limits on a project; see [R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes), November 14.)* The block holds the role gate, ten every-turn duties for Directors, the
Project Director's check and 🎬 paragraph, four Recovery steps, the read rules, a
"Before you / Read" table, a rule for what summaries carry, and a roster rule. The
project section holds the check command, two guard lists ("read before your first
reply" and "read before named work"), the request-store line, the role-file locator
and a roster, or the name of the project's existing role index. Seven cards in
`.director/cards/` (staffing, requests, supervision, knowledge, update-check, privacy,
badge) carry the detail and are read before the action the table names. START.md and
DIRECTOR.md remain only as hash-checked redirect stubs with no rules.
[OPERATIONS](../pattern/starter/payload/OPERATIONS.md) keeps the check's structures
and the context-budget preflight. The cards, WORKER.md and the manuals end with an
`END <path>` line, and a complete read is one that reaches it. The marker stays
`director-starter:2`.

**What this supersedes.** Earlier text stays below as history. Each item names the
previous decision and the failure it prevented, what replaces it, the cost, and the
regression case. Test names are in `development/tests/`.

1. **Where the Director's rules are loaded from** (this section, October 24, October
   31 and November 9; [R18](#r18--start-flat-and-make-learning-an-explicit-bounded-loop)
   November 4, "host hook → START → selected DIRECTOR/WORKER/guards"). Before: a
   short bridge in AGENTS.md pointed to START, the selected role package and
   OPERATIONS' installation-evidence section, all read completely before the first
   ordinary reply, so that a greeting reached the real package and not only correct
   files on disk. Now: the Director's rules are the block itself, so no file has to
   be opened for them to be in context; only the project section's first-reply files
   and the check precede the first reply. The November 9 sentence is kept word for
   word at the top of the block's read rules, and "this startup" is now defined there:
   the Project Director's first-reply reads and check, a Director's Recovery, a
   worker's WORKER.md and role file, a child's overlay or role file, and the file the
   next action needs. Cost: about 8 KB of standing text for every agent the host
   gives AGENTS.md to, workers included; audience labels say who acts on a section but
   do not hide it; and every rule that left the standing text now depends on a card
   being opened at its trigger, which is the mechanism the draft trial saw fail.
   Oracle: `test_block_route.py` (`BlockTextTests`), `test_flat_bridge_repeats_startup_after_compaction_or_resume`,
   and the live cases in [validation](DESIGN_NOTES.md#standing-block-and-cards-starter-33--november-11-2026).
2. **What 🎬 certifies** ([R9](#r9--make-attention-and-active-supervision-visible-without-decoration);
   recorded there).
3. **How the Director's rules are integrity-checked** (R9; recorded there).
4. **Where Recovery lives and when it runs**
   ([R17](#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request);
   recorded there).
5. **Who counts as a worker** (this section, October 17). Before: a new project
   conversation defaulted to that project's Director regardless of who opened it, a
   missing delegated role went back to the assigner, and roles were never inferred
   from ancestry or tool type. That replaced an earlier rule that every agent launched
   by an agent was a worker, which had kept a peer project's session from reaching its
   accountable Director. Now: an agent "spawned by another agent to do a task and
   report back without being named a Director" is a worker; otherwise the reader is
   the Project Director "even if a tool started the session"; another agent's or
   session's message never changes a role; and only the user or an explicit
   assignment opts a session out of acting as Director. A session started in another
   project to update the pattern must be told its role in its first message, because
   without it an agent started to report back counts as a worker there. This
   narrows the October 17 regression case "a session opened in a peer project by
   another director serves as that project's director by default": that now holds
   only when the opener names the role or the session is not a report-back task. Why:
   on hosts that pass AGENTS.md to subagents, every spawned worker reads the block,
   and on a literal reading of the old default a brief that omitted the role made it
   a Director (a reading of the text, not an observed failure). Cost:
   the role is inferred from the shape of the spawn, which October 17 forbade, and a
   peer-project session opened without a stated role is now a worker with no Director
   in that project. Oracle: `test_role_gate_sorts_every_reader_and_keeps_the_pinned_sentences`
   and `test_card_audiences_and_moved_obligations` pin the wording; no live case has
   run for a spawned report-back agent or a peer-project session. The design proposal
   listed this as a Director's decision for the owner to confirm; that confirmation
   is not recorded here.
   *November 15 addition: superseded.* No owner confirmation of this narrowing was
   recorded, and on November 15 the maintainer decided the opposite. A worker is a
   session a Director names as one (the shipped line also keeps the user and an
   explicit assignment), and any other session is its
   project's Director whoever or whatever started it, even one expected to report
   back. In fresh host trials that day, one of three sessions started from a Director
   session arrived as a worker by the "report back" line, because the host tells
   every session it starts that its report goes back. Starter 3.8 restores the
   October 17 default and its peer-project regression case; this item's text and
   reasoning stay above as history (R10, November 15).
6. **Read-only store views after the requests card alone** (R17; recorded there).
7. **The November 7 deferral of splitting OPERATIONS' installation-evidence section**
   (R9; recorded there).
8. **The November 9 "Not done here" list** (the entry below). Of the pieces that entry
   left out, 3.3 implements an end marker with a stated test for a complete read, a
   rule for what summaries carry, the explicit-settings sentence (duty 3), the
   capture-and-split sentence (duty 4) and a checker change. Still not done: a host
   hook or adapter, and anything that proves a read happened. The transcript scanner
   the proposal adopted as a field oracle is not built.
9. **"No startup catalog"** (R18, October 31; the matrix's "no global startup
   catalog"). Before: roles were found at use through the project's discovery
   pointer, and nothing role-shaped was standing text, to keep startup small and
   avoid a role census. Now: a roster summary sits in the project section, which is
   standing text. It is project-owned, holds one row per role (what it does, when to
   use it, a suggested start, limits), is capped with the rest of the section at
   3,000 bytes with overflow to a named file, and may be replaced by a pointer to an
   index the project already has. A fresh install has two generic rows. Role
   definitions are still not standing text. Cost: every agent given AGENTS.md sees
   the rows; a row can go stale against its role file. Oracle:
   `test_project_section_is_project_owned`; the checker blocks a
   section over its cap (`test_project_section_is_required_once_beside_the_block`).
   Listed in the proposal as the owner's call; not separately recorded.
   *November 14 addition:* the 3,000-byte cap and the check's over-cap failure are
   superseded as limits on a project (R10, November 14); the budget stays an authoring
   rule for the shipped section template.
10. **Package acknowledgment, for Directors only** (this section, October 21, October
    24 and October 29: the actor reads and acknowledges its package before acting,
    and an incomplete read cannot be acknowledged as loaded). A Director no longer
    loads a package, so it gives no acknowledgment; the visible signal is 🎬 or a
    stated gap, and after a break the Recovery report line. WORKER.md keeps "Briefly
    acknowledge the resolved package once" for workers. Cost: a scoped child Director,
    which shows no 🎬, now has no acknowledgment at its first start; its Recovery
    report line appears only after a break or at its first reply that acts. Listed in
    the proposal as the owner's call; not separately recorded.
11. **Two read-efficiency sentences are dropped** (this section, October 30: "no
    separate verification round trip is needed after each successful read"). START's
    "Read known independent files together when their combined output fits" and
    "Coverage shown in the read needs no separate verification call" have no
    successor text. They limited cost, not safety. WORKER.md keeps "Batch independent
    reads only". Two smaller clauses of START also have no successor: "with room for
    tool framing", and "Installer/source documentation is not startup". Three safety
    rules that the first rework had left only in WORKER.md are back in the block's
    read rules in the final commit: each range shows its range and the file's total
    length, combined output stays bounded, and file existence and unprinted results
    are not reads.
12. **The update receipt may precede its fresh-session trials, for this move only**
    ([R11](#r11--update-from-a-pinned-public-source-without-replacing-project-state);
    recorded there).
    *November 15 addition:* superseded by starter 3.10: the move finishes on its
    check and review, and fresh host trials are the maintainers' work (R11, November
    15).

**What stays, with no supersession.** Staffing keeps the October 30 decision in this
section ("separate selection from execution knowledge"): the staffer chooses from the
roster row and then, before dispatch, reads the selection and authority part of the
role file the row or the project section names; the executor reads the rest. The
design proposal had suggested routing from roster rows alone; the independent review
kept the recorded behaviour, and no supersession is written. The pinned delegation
sentence, the gap-and-stop fallback, explicit tier and effort on every dispatch, the
partner rule, the SitRep paragraph and example, the first-reply check before a
greeting, generated-project first use before the check, and the worker and scoped
child exclusions from the check and 🎬 are carried over; the
[matrix](BEHAVIOR_PARITY.md#standing-block-and-cards--november-11-2026) says where
each lives and which triggers are unproven. New in the payload, from an owner rule
previously held only as project knowledge: the staffing card's routing ladder (do it
yourself; a worker; a scoped child Director for long, multi-round or multi-worker
work).

**Tradeoff.** The block trades a smaller, cheaper first reply and rules that survive
a compaction for two risks. The detail on the cards is reached only if the agent
opens the card at its trigger, and the block alone produces plausible behaviour, so a
skipped card is hard to see. And about 8 KB is now paid on every turn by every
agent the host gives the file to. The block is managed text: a project can no longer
adapt wording inside it, only beside it.

**Regression cases.** The November 9 draft trial is the known-bad case: after a
forced compaction, zero cards opened and no recovery. A passing run shows, after each
compaction, a fresh check before the first 🎬, the Recovery steps performed through
the store with the "Re-entered:" line in that reply, and the agent's own complete
read of each card, through its END line, before the action it governs. A search hit,
a diff or a worker's quote of an END line does not count as a read. A spawned
report-back agent shows no check and no 🎬. An edited block, a changed stub and an
empty or over-cap project section each block the check.
*November 14 addition:* an over-cap section no longer blocks (R10, November 14); an empty section or one without a check command still does.
*November 15 addition:* with starter 3.8, "a spawned report-back agent" in this case
means an agent its brief names a worker. An agent-started session that nobody names
is a Director and runs the check (R10, November 15).

**Status.** Decided: build the refactor with recovery in the always-loaded block
(owner, November 11). Implemented: on a branch as starter revision 3.3, with an
independent review on November 11 whose nine findings were applied and a final
commit the same day that closed five further items (a missing block baseline now
blocks; the SitRep after a break is conditional; three read rules are back in the
block; the staffing card names the assignment role and the exact task/action trigger
map again; the gate names the user's authority). Verified statically and in three
limited live trials on one host, with the limits recorded in
[validation](DESIGN_NOTES.md#standing-block-and-cards-starter-33--november-11-2026).
Not merged, not published, not accepted. This source checkout's own installation and
its guarded AGENTS branch still use the 3.2 route, and no installed project has made
the move. The unknowns listed in the matrix are acceptance-blocking.
*November 14 addition:* 3.3 and 3.4 are now published on `main`; acceptance still
waits on fresh host trials.

**Later status, November 13 and 14 (dated addition; the paragraph above is kept as
written):** On November 13, after 3.3 was published, this checkout's own installation
moved to the block route. Its root AGENTS.md then carried the managed block, the
project section and a paragraph applying them only when the ignored installation was
present. On November 14 the installation left this repository for a private sibling
workspace, and that public half of the move is superseded
([R14](#r14--commit-the-installation-with-the-project), November 14). This
repository's AGENTS.md now holds the maintainer rules only and has no guarded
branch. The installation keeps the same block, byte for byte, in the private
workspace's AGENTS.md, where its fresh host trials are still pending. The 3.4
entry's statement that this checkout's root AGENTS.md keeps the 3.3 block until its
own reviewed update now applies to the private workspace's AGENTS.md instead.

**November 9 — repeat startup after every compaction or session resume:** The
maintainer observed that after compaction the host reloads AGENTS.md, but the agent
does not re-read the files its block points to, `.director/START.md` and the
selected role package. The Director habits those files carry then stop: the startup
check, 🎬, delegation and SitReps. A November 7 investigation of Director sessions
across compactions found the same shape: in 21 compactions across 9 Director
sessions in 7 projects, none was followed by a complete re-read of START, the role
package and OPERATIONS (its figures, not re-run here). The host re-injected the
standing instruction file but not the files read through it, and the summary said
those files had been read while carrying none of their rules. The block's only
trigger was "before the first ordinary reply in each conversation", and a compacted
session is still the same conversation, so no standing text asked for a re-read. The
flat starter had also dropped v1's reload of no-longer-retained instructions without
a recorded decision. Why each host restores what it restores is a hypothesis.

**Decided and implemented:** At the maintainer's request for one simple sentence in
the instruction file, the [installer's bridge](../pattern/starter/install.py) and
this checkout's guarded AGENTS branch now say, right after the role and check
routing: "After every compaction or session resume, repeat this startup before your
next reply. Read the files again; a summary that mentions them is not a substitute."
"This startup" is the block's own: complete reads of START and the selected package,
and for the Project Director the bounded local check before 🎬. Workers and scoped
child Directors re-read their own package and still skip that check. The November 7
investigation proposed a larger stopgap for the block: an end-marker re-entry
paragraph, summary steering, and explicit-settings and capture-and-split sentences.
This sentence is its first piece only.

After independent review, the same decision removes four readings of the
foundations' reuse rules that could excuse skipping the re-read or the re-check:
[DIRECTOR](../pattern/starter/payload/DIRECTOR.md) now says current-conversation
evidence from before a compaction or session resume is stale;
[START](../pattern/starter/payload/START.md) and [WORKER](../pattern/starter/payload/WORKER.md)
say a compaction summary does not retain instructions, so after compaction or session
resume they are read again; and [OPERATIONS](../pattern/starter/payload/OPERATIONS.md)
says facts from before a compaction or session resume require recheck, like changed
startup bytes. The marker
stays `director-starter:2`, the retained bridge interface that the checker and update
merges recognize; earlier wording changes kept it, and the checker accepts the
previous and the new wording under it. The starter revision is now 3.2. Projects
already installed get the sentence and the clauses only when each one runs its own
update through its own Director ([R11](#r11--update-from-a-pinned-public-source-without-replacing-project-state)).

**Not done here:** no end-of-file marker or mechanical re-entry test, no summary-steering,
explicit-settings or capture-and-split sentence, no host hook or adapter, and no change
to the checker. Nothing proves that a re-read happened; the text asks for one, and an
agent can still carry on from the summary.

**Why/tradeoff:** Standing text is what survives compaction, so the trigger has to
live there. One sentence keeps the block small and leaves the pinned delegation
sentence verbatim; the foundation clauses stop a re-read file from undoing it. The
cost is a full startup re-read after each compaction or resume (and one bounded check
for the Project Director), including a resume whose transcript still holds the files.

**Regression cases:** In a Director session, force a compaction. The next reply comes
after a fresh read of START and the selected role package, visible in the transcript
as returned reads after the summary, and any 🎬 follows a fresh check. A reply that
relies on the summary's statement that the files were read fails. A compacted worker
or scoped child Director re-reads its own package, keeps its role, runs no Project
Director check and shows no 🎬. A session resume behaves the same way as compaction
in each case. **Status:** static tests pin the sentence, its placement,
source/installed parity, the four foundation clauses and the checker's acceptance of
the previous and current block; the live cases are pending
([matrix](BEHAVIOR_PARITY.md#compaction-re-entry--november-9-2026),
[validation](DESIGN_NOTES.md#compaction-re-entry--november-9-2026)).

**Later November 4 — selected first-use writes retain their full prerequisites:**
[R9's generated-instance operation](#r9--make-attention-and-active-supervision-visible-without-decoration)
is a real setup action before the first check, so it loads FIRST_USE plus complete
applicable canonical I/O/privacy protocols before writing. It has no thin-read
exemption. Every selected host/shared entrypoint must reach that same distinction;
an ordinary task is still not a bounded-worker assignment. Existing configured
startup stays read-only; worker/scoped-child exclusions and returned-read barriers
are unchanged. An actual cold trace, not source links alone, must prove that order.

**Later November 1 — classify requested work before applying the direct-answer
exception:** The order correction in R2 preserves startup and role authority while
separating a requested investigation/review from acceptance of a worker's return.
The hook and selected foundation carry the short work sequence; no extra capability
essay, role, prerequisite read or permission ceremony is added. Genuine host/user
restrictions retain precedence and the existing specific-gap fallback. The source
candidate and any installed trial must retain truthful local-delta evidence until
publication/acceptance; failed earlier observations are not replaced by retries.

**Later November 1 — complete the assignment before dispatch:** Follow-up native
cases did dispatch children, but the predeclared package/guard oracle still failed:
staffing instructions and maintained role selection were omitted, and assignment
read restrictions prevented required startup/knowledge access. Some tool restrictions
came from the test harness; they are not evidence of a missing project capability.
Dispatch alone is not complete Director behavior. The foundation now places the
existing staffing/role/guard read before dispatch and requires exact startup/task
instructions plus applicable accepted knowledge or access to retrieve it. Scope must
permit those required reads. The Worker returns a conflicting assignment before
affected work instead of skipping required knowledge. The earlier buried staffing
pointer moves rather than duplicates; capability/effort/tier, source/ownership,
requirement trace and independent-review duties remain. The oracle is a complete
guarded assignment → real dispatch → complete child reads/knowledge → work → return
evaluation, or an honest blocked-read return. No universal helper or new actor is
introduced; genuine project adapters and privacy constraints still control.

**Later November 1 — role assignment is not a user task:** The bootstrap's
"Without an assignment" wording could treat an ordinary assigned task as excluding
the default Director route. That is a real static ambiguity, not a proved internal
cause of an observed actor's omitted role reads. The adopted host-loaded hook now
states the Project Director default unless a worker or scoped child Director role
is explicitly assigned, and START distinguishes an explicit role assignment from
the task itself. *November 15 addition:* starter 3.9 drops the block's sentence that
carried this default ("Default to Project Director unless explicitly assigned..."); its
meaning stays in the three role bullets (R10, November 15, 3.9). The public checkout's absent-installation branch still grants no
Director role. The owning regression checks both adopted/absent routes and explicit
workers, not a promise that every host loads or follows the files.
*November 14 addition:* this repository no longer has an adopted or absent branch.
The maintainer's installation moved to a private sibling workspace, and this
checkout's AGENTS.md holds only the maintainer rules, which assign no Director role
([R14](#r14--commit-the-installation-with-the-project), November 14).

START also directly requires instructions to return and be read before dependent
commands, and the project's required canonical I/O instructions before knowledge
queries, including selector discovery. These clarify existing order without new
roles, files, thin-read exemptions or wire/phase changes. Same-read total extent and
returned range, combined-output bounds, contiguous EOF coverage and recovery/stop
remain. Native schema, privacy, recording and transitive manual guards still apply;
test access limitations require honest blocked results rather than waived purposes.

**Later November 1 — shared rules do not replace the host entrypoint:** A reviewed
installation kept the delegation request only in a shared instruction file while
its actual AGENTS/CLAUDE entrypoints merely pointed there. That reintroduced the
original reference-only ambiguity for a host whose exception names an applicable
AGENTS.md request. The update guides now require the role default and explicit
bounded-subagent request in the actual host entrypoint as well as shared rules.
Preserve all other shared instructions and one canonical detailed package; do not
copy the whole role foundation into each router. The oracle inspects the literal
host-loaded entrypoint in every affected target, not just its referenced document.
This repairs an integration route; it does not prove native behavior or resolve
unrelated models' observed instruction-following failures.

**November 9 — one Director paragraph, in AGENTS.md; CLAUDE.md only imports it:**
The maintainer asked that projects use AGENTS.md rather than CLAUDE.md for Director
text: move everything in CLAUDE.md into AGENTS.md and reconcile it there. Several
installations carried the Director paragraph in both files. The likely cause, an
inference from the wording rather than a traced update, was the starter update
guide's wording of the decision above, which told updaters to keep the role default
in "the actual host entrypoint (AGENTS.md or CLAUDE.md) as well". Two copies can
drift apart, and an update merges only the one marked block it finds. Starter
[UPDATES](../pattern/starter/payload/UPDATES.md) now keeps the role default, the
explicit bounded-subagent request and the marked block in AGENTS.md, or in the hook
source the project's check selects, even when other rules live in a shared file.
When the host loads CLAUDE.md and expands its imports into loaded text, CLAUDE.md
only imports AGENTS.md (for example `@AGENTS.md`), its other content moves into
AGENTS.md, and no second copy of the Director paragraph stays in CLAUDE.md. After
independent review, two guards were added: where the host does not expand imports,
the role default and bounded-subagent request stay in CLAUDE.md and the gap is
reported; and the update backs up and verifies each startup file it changes, both
AGENTS.md and CLAUDE.md, reporting rather than moving content whose ownership is
unclear or that applies to only one host.

This keeps the November 1 mechanism. An import is literally loaded: the host
inserts the imported text into the loaded instructions, so AGENTS.md imported by
CLAUDE.md is still host-loaded entrypoint text, not a reference the agent must
choose to follow. The November 1 failure was a pointer to another file; its oracle,
that the literal loaded entrypoint carries the role default and request, still holds
without the duplicate. The route relies on the host expanding the import, which is
why a non-expanding host keeps the request in CLAUDE.md. The checker's default hook
source is already AGENTS.md, so no checker change follows. The legacy v1 engine's
update guide keeps the old wording, so a v1 update can still recreate the duplicate;
it is not part of this starter revision. Projects already installed reconcile only when each runs its own
update. **Regression case:** in an updated project, CLAUDE.md is exactly
`@AGENTS.md`, AGENTS.md holds one marked block, CLAUDE.md's earlier non-Director
content is in AGENTS.md, and the startup check passes. **Status:** starter 3.2
wording; static tests pin the sentence and the checker's pass on that layout. No
project has been updated, and host import expansion was not observed here.

**October 31, 2026 — partial supersession for the first Project Director reply:**
The earlier plain-factual-question regression below excluded hash checks before an
answer. R9's new first-reply rule deliberately supersedes only that exclusion for
the Project Director's first ordinary reply, including hello/identity. One bounded
local route/receipt/applicable-config check is now required; later unchanged replies
reuse it. Assigned workers and child Directors still skip it, and discussion does
not activate Recorder, request/history, learning or metadata-network protocols.
The tradeoff is finite first-reply I/O for a meaningful automatic checked identity;
it is not permission to pull every manual or validate all history before greeting.
Actual CLI timings/commands are recorded in the focused validation, not estimated
as universal startup speed. All other action references retain their progressive
before-use triggers and authority.

**October 31 — returned reads and installed-host validation:** The outer host
hook is part of the behavior: a greeting must reach the selected package, not
merely find correct files on disk. The read barrier is equally material. Printing
required instructions and executing the dependent checker in one tool invocation
does not let the actor consume the returned instructions before acting. One actual
cross-host trial did exactly that; complete text later in its result did not turn
it into a pass. A reviewed project-local clarification made the returned-result
barrier explicit, and a meaningful fresh retry observed it before the checker and
first badge. This clarified the existing complete-read-before-action obligation;
it did not relax the source contract or expand the check into ledger operations.

The [validation record](DESIGN_NOTES.md#first-reply-startup-check--october-31-2026)
now distinguishes eight external configured-project greeting observations across
two CLI hosts from the source installation's existing-conversation technical check
and fresh fixture failure/worker/recovery cases. These observations support this
bounded entry route, not universal desktop activation, identical host behavior,
comparative startup cost or automatic learning. Failed observations remain evidence
rather than being replaced by the successful retry.

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
*November 15 addition:* the November 11 narrowing of this default (item 5 there) is
superseded, and starter 3.8 restores the default and the peer-project regression
case. The case of a delegated assignment with no role seeking clarification is
superseded on the block route: a brief with no role makes a Director (R10, November
15).

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
*November 15 addition:* on the block route, "malformed bounded assignments clarify,
never default" and the regression case below that an incomplete delegated assignment
cannot become Director are superseded: a brief with no role makes a Director. A
session already named a worker that is missing other details still returns them to
the assigner (R10, November 15).

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
*November 15 addition:* superseded on the block route for an assignment with no role,
which now makes a Director (R10, November 15).

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

**Refined, November 1 — apply the exception already granted:** An installed
Director again described an applicable host rule as requiring a separate user
delegation request. On correction it acknowledged that its loaded AGENTS.md already
qualified under the rule's explicit project-instruction exception. This supports a
misclassification of the exception, not a finding that permission was absent or a
particular model cannot delegate. Earlier greeting checks did not exercise this
decision or actual worker execution.

The [flat installer's loaded hook](../pattern/starter/install.py) and legacy
[hook](../pattern/INSTALL-v1.md) now simply say: use subagents for substantial
analysis and project changes, assign bounded work, stay available and evaluate
results. This is the explicit project request. "When permitted," optional-actor
lists and host-rule interpretation prose do not belong beside it: they obscure the
action and make each executor solve the original debugging problem again. That
reasoning stays here. The [Director foundation](../pattern/starter/payload/DIRECTOR.md)
briefly requires a specific gap and stop, rather than self-implementation, if the
actual tool is unavailable or delegation prohibited. Existing host authority holds;
no project directive overrides a true user-only prohibition or creates a tool.

**Preserved intent and regression oracle:** R2's protected conversation requires an
actual bounded worker invocation and evaluated return on a project-change request
that does not separately ask for delegation. R10's authority boundary requires a
real user-only prohibition or unavailable tool to produce a specific limitation,
without Director implementation; merely seeing the word "only" before an applicable
exception is insufficient. R1/R18 discussion stays direct, with no compulsory
second Director or specialist. Static route checks cover the recommended emitted
hook, both role foundations and source-hook parity. Actual affected-model execution
and independent review remain separate acceptance gates; successful source wording
or an actor's promise to delegate is not evidence of launch or return evaluation.

**Refined and superseded in part, October 30 — conversational startup and
mandatory progressive loading:** The October 24 returned-result barrier remains
for the actual startup package, with interface 1 and role resolution preserved.
It no longer makes every generic Director operational protocol a prerequisite for
a simple reply. The [bootstrap](../pattern/engine/PATTERN.md) now owns the small
conversational package and explicit capability triggers. Selected
[Director](../pattern/engine/DIRECTOR.md),
[Request Manager](../pattern/engine/REQUEST_MANAGER.md) and
[worker](../pattern/engine/WORKER.md) definitions retain role/authority, intended
deliverable, non-worker/delegation boundaries and commitment ownership. Task
references load before affected inspection/execution. Staffing, state, identity,
setup, updates and other protocols load completely before their action, once per
retained context. Deferred means mandatory at the trigger, never optional.

Project authority and shared gates remain in startup. Unqualified requirements
load transitively with their requiring document: at startup when it is startup-
required, or before the requiring deferred action. Engine replacement cannot
silently rephase project definitions or an older PROJECT reference chain. Reviewed
integration must preserve exact requirements, applicability, locators and triggers;
[STARTUP](../pattern/engine/references/STARTUP.md) and
[UPDATES](../pattern/engine/references/UPDATES.md) record that boundary. The public
maintainer guide now selects the rationale overview, owning decisions and relevant
validation sections rather than making unrelated dated history a universal read;
history remains intact and discoverable. Existing explicit full-file role
requirements still apply until separately reviewed.

**Why/tradeoff:** Unconditionally reading the staffing/state/supervision chain
makes reply-only discussion pay for actions it never takes. A reported startup
truncation also involved a wrapper aggregate, not missing source files. Increasing
each inner tool's output allowance does not bound the outer response. Required
reads now bound each model-visible result, including wrappers, with extents/ranges
in the read and contiguous chunks for unknown/oversized text. Inspect results and
recover omissions before a loaded claim; no separate verification round trip is
needed after each successful read. This remains instruction-guided and cannot
prove understanding or detect every possible host omission.

**Concrete regressions:** A plain factual question loads role and authority, then
answers without Recorder activation, hash checks or metadata discovery. A later
staffing action first loads model/role/identity/assignment/state protocols and the
matching local guards. A nested mandatory prohibition cannot vanish behind a
deferred runbook. Outer-wrapper truncation or a missing middle chunk prevents a
completed-package claim until recovered. Discussion remains prompt while held
commitments continue through the existing recovery/supervision loop; deferred
loading creates neither an exit exception nor a silent worker role switch.

**Status and limits:** Authorized direction, implemented source candidate.
[Review and measurements](STARTUP_LOADING.md) separate shared bytes/tokens/read
stages from project references and preserve the obligation map. Generic Director
startup text shrinks substantially; worker discovery/safe-read text grows modestly
without an extra dependency stage. These are file/token inventories, not measured
latency. Static/fixture checks and their scope are recorded in
[validation notes](DESIGN_NOTES.md#progressive-loading--october-30-2026).
Fresh-host behavior, the current live installation and downstream adoption remain
separate and unverified for this change. Revisit if before-use loading skips a
project guard, deferred protocols are treated as optional, repeated checks recreate
startup overhead, or actual timing fails to improve.

**Refined later October 30 — separate selection from execution knowledge:**
[ROLES](../pattern/engine/ROLES.md#selection-knowledge-and-execution-knowledge)
requires the staffer to read the selected standalone definition and its complete
selection/authority package: applicability, ownership, scope, guards, reserved
decisions, route and exact reference/trigger map. The executor loads its full
startup and affected manuals before their triggers. A staffer need not perform
the executor's startup or eagerly read unrelated craft manuals just to assign it.
An ambiguous reference that may hide a selection or authority constraint must
still be read or resolved before staffing; old explicit staffer requirements and
unqualified actor dependencies remain binding until reviewed separation.

**Why/tradeoff:** Having every ancestor read every executor manual duplicates
specialist context. Deferring hidden guards would instead weaken assignment
safety. A complete selector exposes the decisions the staffer must make while
preserving the executor's full knowledge. The concrete regression is a maintained
role whose route prohibition lives in a nested reference: that prohibition must
reach selection even when its task manual is deferred. Existing project phases
require an exact preservation map before integration; a generic engine update
cannot silently rewrite them.

**Observed correction, later October 30:** A fresh assigned Director safely
answered a reply-only question but first read the full direction protocol. Its
later explanation identified the capability table's general “exit” trigger as
inviting an interpretation that every final answer needs exit accounting. That
explanation is self-report; the extra read itself is visible in the actual trace.
The [bootstrap](../pattern/engine/PATTERN.md#required-capability-protocols) and
[Director](../pattern/engine/DIRECTOR.md#keep-commitments-through-acceptance) now
clarify that a reply-only answer with no held commitments is not a claim of outcome
completion or an end to held-execution supervision. Actual held work retains its
recovery, supervision and exit duties. The original extra-read observation remains
separate from the fresh affected retry; neither successful startup nor this narrow
correction establishes universal host compliance.

## R11 — Update from a pinned public source without replacing project state

**November 15 — a user's update is finished when its quick checks pass; fresh host
trials are the maintainers' work (starter revision 3.10; supersedes November 11's
receipt-before-trials rule, item 12 of the R10 November 11 entry, the November 13
"pending until they pass" wording, and, for the starter route, part of the October 23
trigger table and its pending-trial regression case):** The maintainer updated two
outside projects from 3.3 to 3.9. Each project's Director reported the update as
staying open until four fresh-session trials had run, and then asked whether to run
them. The guide told them to: the move and every block update recorded the selected
fresh host trials as pending in the receipt and did not report the update adopted
until they passed, and the trigger table required fresh trials for any change to
startup, role routing or role behavior.

**Decided by the maintainer, November 15:** people outside are trying to update to
the latest version, not to run test software. Whatever quick validation shows that
things still work has to be enough for a user. A deeper check may be offered, but it
is never required.

**The argument.** A fresh host trial watches the pattern's own text at work: a first
reply, a reply after a forced compaction, a worker start. Every installation receives
that text byte for byte from the published revision, and `director_block: unchanged`
proves the installed block is that text. `startup_hook.target` shows the block sits,
unchanged, in the hook source the project's check names; the table's trace of the
host-loaded hook covers whether the host loads that file. What is the project's own (its section, guards, store,
roles and adaptations) is covered by the three-way comparison, the preservation
checks and the independent review. So a trial run in a user's project mostly
re-tests the published text, which is the same in every installation; that test
belongs to the people who publish it, once per revision, in their own installation.

**Implemented, as wording (starter revision 3.10).** In the
starter [UPDATES](../pattern/starter/payload/UPDATES.md):
- "Move to the AGENTS.md block" steps 6 and 7, and "Update an installed block" steps
  3 and 4, finish on the check, with the independent review for the move. The receipt
  is still written just before the check, because the check reads it; if the check
  then fails, the cause is fixed or the backup restored, and the move or update is not
  reported finished. No trial is recorded as pending, and nothing waits on one.
- The verification table's rows for changed role behavior and for structural startup
  changes now trace the route and run the check, repairing or reporting a detected
  defect, with no fresh host trial required; the progressive-loading sentence no
  longer requires its trials.
- A new subsection, "Fresh host trials", says they are the maintainers' work on
  published revisions in their own installation. A user's update must not record them
  as pending, hold the update open for them, or end its report on a question about
  them. A receipt from an earlier update that lists such trials as pending is left as
  written and its entries are not carried forward. A deeper check may be mentioned
  once, as a plain statement, and run only when the user asks. An unpublished or
  local candidate revision is said to be one. A startup defect the update finds is
  still handled; a fresh session is one way to show a repair, not a requirement.
- "Validate and record" calls fresh host trials optional for an update, no longer
  links OPERATIONS' installation-evidence checks from there, and keeps "Do not claim
  a cold-session behavioral trial unless one actually ran".
- Move step 7 now ends: "The block is the published text byte for byte, and the
  check shows it is in place, unchanged, in the file this project's check reads; the
  table's trace covers how the host loads that file." A conversation already running,
  and the subagents it starts, may keep the instructions it loaded at its start, so
  the new block applies from the next new conversation (R10, November 15, 3.9,
  observation 1).
- The daily-discovery paragraph now says a fresh host trial, pending or not, never
  holds daily discovery; a real unaccepted baseline or a required unrun check keeps
  its gate. This narrows the later October 23 clarification below ("An unrelated
  pending trial cannot invent a new gate or block daily metadata discovery") to every
  fresh host trial.
- The manifest is 3.10 and the starter README has a 3.10 paragraph.

**What this supersedes.** Earlier text stays as history, each with a dated note.
1. *November 11, "A receipt may precede required checks, for this move only"*, with
   R10 November 11 item 12: the receipt was written before the fresh host trials and
   the move was not adopted until they passed. Its purpose was that a project never
   looks adopted when it is not. Disposition: the purpose is kept by the check, which
   reads the receipt and must pass, by the review, and by "do not report the move
   finished" when the check fails; the trials leave the gate.
2. *November 13 (3.4), "the update is not reported adopted until they pass"*, which
   carried the same ordering to every block update. Same disposition.
3. *October 23, part of the trigger table and one regression case, on the starter
   route.* The table's "run only the fresh host trials relevant to that behavior" and
   "relevant fresh unassigned/assigned host trials" are replaced by tracing the route
   and running the check, and "A structural role-routing upgrade performs the full
   audit and affected fresh trials" now ends at the audit and the check. The regression
   case "A previously unrun default-Director trial remains explicitly pending through
   an unrelated prose update" no longer applies to fresh host trials: such entries are
   left as written and not carried forward. Other known gaps still carry forward with
   their limits. The legacy v1 engine guide (`pattern/engine/references/UPDATES.md`)
   is out of scope: it is unchanged and keeps its trial triggers.

**What does not change.** Verified backups before change; the pinned three-way
comparison and preservation of adaptations; separate migration decisions and their
authorization; conflicts resolved, never silently waived; project, host and user
authority, and each installation updated only from its own project; the required
independent review; strong tier at high effort for the move; automatic mode never
starting the move; and the rule that no cold-session trial is claimed unless one ran.

**Out of scope for 3.10.** The public site still describes fresh-agent trials as part
of updates. Changing it needs site work and its own deployment authorization. The
legacy v1 engine guide is also unchanged (item 3 above).

**Tradeoff.** A published revision whose maintainer trials have not run can reach
users without anyone watching it work in a fresh session, and a user's update no
longer catches that. Closing the gap is the maintainers' job: run the trials on each
published revision in their own installation, and fix and republish when one fails.
A defect that only shows with one project's own adaptations is caught only if the
comparison, review or check sees it, or if the user asks for the deeper check.
Whether the host actually loads the project's hook file (for example, a CLAUDE.md
import the host does not expand) is now shown only by that static trace.

**Regression cases:** A project updates from 3.3 to the latest revision; its files
compare cleanly, its adaptations are preserved, the check reports `evidence_matched`
with `director_block: unchanged`, and the Director reports the update finished,
without recording trials as pending and without ending on a question about them. The
report may say once, as a statement, that a fresh session can be opened to watch a
first reply and a worker start; the Director runs one only when the user asks. An
earlier receipt's pending trials stay as written and do not appear in the new
receipt. A move whose check fails is not reported finished, and the backup is
restored or the cause fixed. An update that finds a startup defect still repairs it or
reports it. An update to an unpublished candidate says so.

**Status.** Decided by the maintainer on November 15, 2026. Implemented as wording in
starter revision 3.10 and published on `main` with this change; no installed project
has it. Verified statically: the full suite passes, 305 tests, and the new wording is
pinned by the seven tests in `UserUpdatesFinishOnChecksNovember15Tests` in
`test_block_route.py`, with the existing pins updated to the new UPDATES wording and
to 3.10 ([validation notes](DESIGN_NOTES.md#a-users-update-ends-on-its-quick-checks-starter-310--november-15-2026)).
These are wording pins only. Not verified: no project has updated under 3.10, and the
maintainers' own trials of 3.10 in their installation have not run. The legacy v1
engine guide is out of scope and unchanged.

**November 13 — update an installed block (starter revision 3.4):** 3.4 is the first
block change after the move, and the guide had no step for an installation already
on the block. Starter [UPDATES](../pattern/starter/payload/UPDATES.md) gains "Update
an installed block": back up; in the file the check selects, replace everything
between the marker lines with the incoming block byte for byte; leave the project
section and all other text untouched, first moving any project wording from an edited
block into the section and measuring as in the move's step 5; write the receipt with the changed cards' and payload files'
baselines and the new `director_block_sha256`; point the check and `update_check.py`
at it; and run the check, which must report `evidence_matched` and `director_block:
unchanged`. Only the `--receipt` paths in the section's check and update-check
commands change. A project with its own `director-pattern:start` / `director-pattern:end`
pair puts those lines in place of the incoming block's first and last lines, and
`director_block_sha256` hashes the block as it stands, from its opening marker line
through its closing marker line and newline, which is what the checker hashes.
**Correction to the published 3.3 guidance:** the move's step 3 said such a project
"keeps its marker lines around the same incoming text". Read literally, that nests two
marker pairs, and the checker, which accepts exactly one pair, then blocks. Step 3 now
says the project's lines replace the block's own first and last lines. No known
installation followed the literal reading; the field project's block carries only its
own pair.
**Superseded in part:** November 11's "a receipt may precede required
checks, for this move only". The check reads the receipt, so every block update has
the same ordering; the receipt records the selected fresh host trials as pending and
the update is not reported adopted until they pass. The "Validate and record" and
move steps now say so. *November 15 addition:* superseded by starter 3.10. A block
update now finishes on its check; fresh host trials are the maintainers' work and are
not recorded as pending (R11, November 15). **Regression case:** a 3.3 installation with an edited project
section takes 3.4; the section's bytes are unchanged apart from the `--receipt`
paths, custom markers stay in place, and the check reports `evidence_matched` and
`director_block: unchanged`. **Status:** Decided by this repository's Project Director on November 13, 2026, from
the maintainer's field report, and implemented in the starter source as revision 3.4.
An independent review the same day, with its findings applied, accepted it; the
maintainer's acceptance and publication are pending. Static tests only; no live run
yet, and installed copies keep their adopted text until updated. Oracle:
`test_update_guide_updates_an_installed_block_without_touching_the_section` and
`test_a_3_3_installation_updates_its_block_and_keeps_the_section_and_markers`, which
scripts steps 1 to 4 against a fixture of the exact 3.3 files 3.4 changes, with and
without custom markers. No installation, including this checkout, has taken it.
*November 14 addition:* that installation has since left this repository for a private
sibling workspace ([R14](#r14--commit-the-installation-with-the-project), November 14);
it still has not taken 3.4.

**November 11 — the move from revision 3.2 to the AGENTS.md block is a reviewed
manual operation (starter revision 3.3; implemented on a branch, not merged,
published or accepted):** The route change recorded under
[R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)
cannot reach an installed project by replacing managed files: the block in AGENTS.md
must be replaced, a project section written from the project's own reviewed state,
and START.md and DIRECTOR.md turned into stubs. Starter
[UPDATES](../pattern/starter/payload/UPDATES.md), "Move to the AGENTS.md block",
gives seven ordered steps: back up; replace the managed payload, moving any local
addition to the removed files or sections into a project-owned file first; replace
the block byte for byte from the pinned revision; add the project section once and
fill it from the project's check command, guards, store files, role-file locator and
roster or existing role index; measure against the block, section and host caps
*(November 14: the block and section numbers are superseded as limits, and the
measuring now reports against the host's own cap only; see [R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes), November 14)*;
write the receipt with the new baselines and `director_block_sha256`; run the check
exactly as the section states it.

Three rules are new and narrow earlier ones:

- **A receipt may precede required checks, for this move only.** The November 7 and
  earlier rule is that an update receipt is written only after every required check
  succeeds, so a project never looks adopted when it is not. The block-route check
  needs the new receipt to run, so here the receipt is written before the fresh host
  trials, records each of them as pending, and must not report the move as adopted
  until they pass. Cost: a receipt exists while trials are open, and only its own
  pending entries say so.
  *November 15 addition:* superseded by starter 3.10. The receipt still comes before
  the check, which reads it, but the move finishes when the check passes with the
  independent review; fresh host trials are not recorded as pending (R11, November
  15).
- **Automatic mode never starts the move.** The standing "automatic" preference
  authorizes compatible reversible updates without repeated permission. The move
  changes the loaded startup chain, so an automatic result that would bring it waits
  for the owner's explicit go-ahead.
- **The move is not a lighter-tier case.** November 7 named an ordinary compatible
  update as bounded, checked work that fits a lighter tier. The move is strong-tier
  work at high effort with the required independent review.

The block's text is managed; the update guide's earlier promise to preserve
customizations inside the marked block now means moving them to the project section
or the surrounding file and reporting anything whose place is unclear (see
[R9](#r9--make-attention-and-active-supervision-visible-without-decoration)). An
installation interrupted after the payload is replaced and before the block is
merged has an old block pointing at a stub; the check blocks and names the unfinished
update. A project may keep its earlier START.md route by a deliberate reviewed
decision, keeping its earlier START.md, DIRECTOR.md and OPERATIONS.md and recording
the choice. The November 7 rule that each installation is updated from its own
project is unchanged; a session started in another project for an update now must be
told its role in its first message (R10, item 5).
*November 15 addition:* the first message still names the role in 3.8, but item 5 is
superseded: unnamed, that session is still the project's Director, and naming the
role makes that plain (R10, November 15).

**Regression cases:** A 3.2 installation with project text around its bridge, a
project role, an update policy and a captured request makes the move and keeps all
of them; its check then reports `evidence_matched`, a hook target ending in
`WORKER.md` and `director_block: unchanged`. A move stopped before the block is
merged blocks with the named gap. An automatic result that would bring the move does
not start it.

**Status:** implemented on a branch.
`test_a_3_2_installation_moves_to_the_block_and_keeps_project_content` scripts the
file operations of steps 1 to 6 against a fixture of the exact 3.2 startup files and
reaches `evidence_matched`;
`test_a_move_interrupted_before_the_block_is_merged_blocks_with_a_named_gap` and
`test_update_guide_documents_the_move` cover the rest. The scripted move measures
the byte caps only, not a host's instruction cap, and runs no agent. *(November 14:
the caps it measures are superseded as limits on a project; see [R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes), November 14.)* No installed
project has made the move: not a mature project with its own guards, store or role
index, and not this source checkout. The fresh host trials the guide requires
(a first reply, a reply after a forced compaction, a worker start) have not run on
any moved project.
*November 15 addition:* since starter 3.10 the guide no longer requires them of a
project; they are the maintainers' work on published revisions (R11, November 15).

**November 7 — each installation is updated from its own project, an ordinary
update is bounded and checked, and the starter gets a readable revision:** In a field
case, a Director in this source repository was asked to roll out a new starter
revision. It dispatched outside workers that merged the new
[DIRECTOR](../pattern/starter/payload/DIRECTOR.md)/[OPERATIONS](../pattern/starter/payload/OPERATIONS.md)
text into seven downstream projects directly, bypassing each project's own Director,
tracker records and acceptance. Each project ended with new files but its previous
accepted receipt, a half-updated state. The workers wrote backups and stopped short
of acceptance; the projects' own Directors were then asked to review or redo. The
same session dispatched nearly every worker on the inherited strongest tier with no
effort chosen. The maintainer made three decisions; an independent review then
changed the wording of each, recorded here as the current text.

1. **Update from inside the project.** This project's Director, or an agent it
   authorizes within that project, performs the update in that project's own
   conversation; when no working Director exists here, an agent the user directs in
   this project's own conversation performs it. To update other projects, ask each
   project's Director to "update director pattern". A session in another project
   starts only when the user asked for that update, and carries the user's request;
   if no session can be started there, the user gets the 🖐️ action to open one and
   say it. Never patch another installation from outside, even by following the
   protocol. Only that Director knows the project's layout, roles, adaptations,
   tracker, records and acceptance gates. A template or stencil without its own
   Director is updated only through its maintainer's reviewed staging route; if none
   is documented, the gap is reported and the template is not edited. This narrows the
   earlier UPDATES wording that let any authorized installation agent perform an
   update and said it "need not already be a Director"; the performer's scope,
   compatibility decisions and acceptance remain the accountable owner's. The
   starter DIRECTOR also now points to reading the whole UPDATES guide before
   planning any update, a reachability fix because the field Director had read only
   part of it.
2. **An ordinary compatible update is bounded, well specified and checked by the
   required independent review.** It therefore fits the
   [lighter-tier choice](#r2--protect-judgment-and-conversation-from-executionbookkeeping)
   (November 5): a lighter capability tier at high effort, or the strong tier at
   medium, recorded at dispatch. Starter OPERATIONS now says a guide may name such a
   case, and UPDATES does. The independent review stays and uses the strong tier at
   high effort. Harder cases (unresolved conflicts, migrations, unknown provenance or
   ambiguous project adaptations) use the strong tier at high effort or above, with a
   recorded reason. The update case is no longer described as "small": the
   lighter-tier conditions are bounded, well-specified, easily checked work, and an
   update meets them through its specification and the independent review that checks
   it, not through size. [R17](#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request)
   carries the cross-reference.
3. **A readable `starter_revision` ("3.1")** is added to the starter
   [manifest](../pattern/starter/manifest.json) and recorded in the receipt on
   install and update. `starter_version` stays 3 as the install format: bumping it
   would make every existing receipt an unknown format and imply a migration. The
   maintainer instructions in [AGENTS](../AGENTS.md) now require bumping the revision
   with each published starter payload change. An update names the previous and new
   revision when reporting; an install with none is reported as "unrecorded".

**Why/tradeoff:** Only the project's own Director can judge adaptations, tracker
records and acceptance, and an outside patch cannot see them. Merging into a project
while its receipt stays unchanged leaves it looking accepted and current when it is
neither. The cost is one session per project instead of one script across all of
them: slower, but each project's owner reviews its own result. Starting another
project's session only on the user's request and carrying it keeps the user in
control of which projects change; the fallback to an agent the user directs covers a
project with no working Director without reopening outside patching. Naming ordinary
updates as bounded, checked work avoids spending the strongest tier on routine merges;
a wrong call is caught by the independent review, now at the strong tier and high
effort, and the Director's acceptance. A separate readable revision gives people and
agents something to say and compare ("3.1") without changing the install format; the
cost is one more number to bump with each payload change (now a maintainer rule), and
an install from before it has an unknown previous revision, reported as "unrecorded"
rather than guessed. Reporting a template with no staging route as a gap leaves it
stale instead of risking an unreviewed edit.

**Regression cases:** Asked to roll out an update to several projects, a Director
starts a session in each project at the user's request, carries the request, asks its
Director to "update director pattern", and follows its reports; where it cannot start
one it gives the 🖐️ action. It does not dispatch workers into those projects' files,
and a project that has not run its own update keeps its previous accepted receipt
with no new files. A stencil with no documented staging route is reported as a gap,
not edited. A project with no working Director is updated by an agent the user directs
in that project's own conversation, not from outside. An update dispatch records a
lighter tier at high effort, or the strong tier at medium, with requested and
effective settings or unknowns; its independent review records the strong tier at
high effort; an unresolved conflict, migration, unknown provenance or ambiguous
adaptation records the strong tier at high or above with the reason. An update report
names the previous and new `starter_revision`; for an install with no recorded
revision it says "unrecorded". A fresh install's receipt records the revision;
`starter_version` remains 3 and an existing receipt is not treated as an unknown
format. A starter payload change merged without a revision bump violates the
maintainer instruction.

**Status:** Decided by the maintainer on November 7, 2026; the independent review's
wording changes are included. Implemented in starter
[UPDATES](../pattern/starter/payload/UPDATES.md) and DIRECTOR/OPERATIONS wording, the
manifest's `starter_revision`, the installer's report and receipt, and the maintainer
instructions, with the starter README noting the revision. Static package checks
establish wording and reachability only. Live rollout through each project's own
Director is pending, and no downstream update has been verified. Installed copies keep
their adopted text until updated. **Open gap:** the v1 engine's UPDATES, INSTALL-v1
and README-v1 still allow outside or non-Director updates; they are not changed in
3.1 (see the [matrix](BEHAVIOR_PARITY.md#why-each-mechanism-existed-and-the-new-route)
and [validation](DESIGN_NOTES.md#update-ownership-and-starter-revision--november-7-2026)).

**November 2 — project composition and update baselines:** R9's
[composed-guidance correction](#r9--make-attention-and-active-supervision-visible-without-decoration)
separates strict managed startup integrity from historical snapshots of current
project-owned instructions. A changed project snapshot alone is not a broken
installation or permission to rewrite its receipt. Actual updates still pin source,
back up changed files and compare baseline/current/incoming plus prior upstream to
preserve adaptations, project authority and the canonical store. Structural route
changes retain their affected whole-chain audit and behavioral gates. The regression
is an update preserving legitimate build guidance and an intact selected hook,
while an incompatible route or managed drift remains an explicit unresolved gap.

**November 1 narrow timing refinement:** Keep greeting-only first replies local;
arrange due metadata discovery through a supported background route or the next
active project-work step. Until observed, it remains due in context and at an
ordinary checkpoint, not a new greeting write or invented actor. Preserve rolling
24-hour failure throttling and notify/automatic/off. Unknown publication requires
an exact upstream pin and reviewed installed comparison through the authorized
update/normal recording route; do not reset a cache or promote acceptance to pass.
This narrowly supersedes discovery at the first active interaction when it is only
a greeting and the host has no supported background route: discovery waits for the
next active project-work step. The tradeoff favors a bounded prompt reply over
immediate refresh; the check remains due, not silently waived. The oracle is a
greeting with no network followed by observed due discovery on the next work step,
plus unchanged failure throttle and preference behavior.

**October31 starter correction:** These preservation/discovery obligations apply to
the flat foundation too, through its deferred UPDATES guide and reused deterministic
checker. Fewer compulsory actors do not waive active-session checks or preferences.

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
passed nor a reason to block that update. *November 15 addition:* on the starter
route, starter 3.10 supersedes part of this entry: the structural and role-behavior
rows no longer require fresh host trials, the structural case ends at the audit and
the check, and a fresh host trial left pending by an earlier update is left as
written and not carried forward. The legacy v1 engine guide is unchanged (R11,
November 15). An already-current check reports local
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

**November 1 agent-guide correction:** The website's agent guide linked current
`main` while repeating mandatory v1 manager/Recorder/roster and badge procedures.
Those instructions conflicted with the newly selected flat source candidate.
The guide now selects the actual package/manifest, preserves the three copyable
requests and points to the applicable canonical protocols instead of restating
their runtime organization. Verification treats inapplicable fields as inapplicable,
not missing prerequisites. `llms.txt` uses a valid selector link. Published v1.1.0,
unreleased source, installation and deployment remain distinct. The oracle resolves
all canonical agent links to real files and keeps selected-package scope, exact
requests, preservation and public-build boundaries. Source changes are not website
deployment; the existing human narrative is unchanged.

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

**November 14 — the maintainer's installation moves to a private sibling workspace
(supersedes this repository's ignored installation):** The October 21 decision below
records a deliberate local choice: "This source repository still ignores its own
`/.director/`", because the repository is public and an installation here holds the
maintainer's exact conversations. The choice kept that material off the public
remote, at the cost this decision exists to prevent. Ignored files reach no clone,
no remote and no other machine, so the request history, exact sources and receipts
lived on one disk. On November 13 that installation also moved to the 3.3 block route
([R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)).
The move put the managed block, its project section and a paragraph applying them
only when the ignored installation was present into this repository's root
AGENTS.md. For every public reader that text was inert, and every agent that loaded
the file paid for it ([R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)
November 11 on the per-turn cost).

**Decided:** the maintainer chose a private sibling workspace on November 13 and
approved the migration plan on November 14. The installation, its canonical store
and the preserved originals live in a private workspace beside this checkout.
Sessions that maintain the method start there and edit this repository in place.
The workspace holds no copy of the method, and no private material moves into this
repository. Cleanup here moves forward only: public history is not rewritten.
Finished work in either repository is committed and pushed unless the maintainer
says not to.
**Considered alternative:** a private copy of this repository with a rule to push
changes to the public one. It was rejected because two copies of the source drift
whenever an agent forgets the rule.

**Design-intent disposition.** *Affected:* the October 21 sentence quoted above; the
privacy consequence of [R8](#r8--separate-the-installed-method-from-its-workshop)
(raw conversations and internal references remain private); and R10's statements
about this checkout's own installation and its guarded AGENTS branch (November 1,
the November 11 status, November 13). *Purpose and failure prevented:* keep exact
sources, request history and receipts off a public remote, since deletion does not
remove them from public history; and keep a public clone from presenting or
activating a Director installation. *Disposition:* preserve the purpose and
supersede the location.
- *Preserved, now by construction.* The private store is no longer inside the public
  working tree, so neither a removed ignore line nor a forced add can publish it.
  This repository's ignore file keeps `/.director/` and `.reference/` as a second
  guard. "A source checkout alone is not installation" now holds because the checkout
  has no installation in it.
- *Restored for the maintainer's own installation: this decision's default.* The
  store is tracked in the private workspace and pushed to a remote that was confirmed
  private before its first push, so the public-remote warning is not due. Backups,
  scratch, locks and the update cache stay local. The preserved originals stay
  local-only because of their size, so their single-disk risk is unchanged.
- *Superseded, November 14.* The October 21 sentence that this repository ignores its
  own `/.director/`. Also the public half of the November 13 move: the applicability
  paragraph, managed block and project section in this repository's AGENTS.md, and
  the package tests that pinned them there. The private half, the installation's own
  block route, moved with its block byte for byte; its project section was re-bound
  to a new technical record written for the move.
- *Active route now.* This repository's AGENTS.md holds the maintainer rules, one
  sentence that the maintainer's installation lives outside this repository, and
  the Tinka pointer. The private workspace's AGENTS.md holds its own header, the
  managed block byte for byte and its project section. Its startup authority lists
  this repository's "Maintaining this repository" as an explicit read, because a
  check there cannot hash a file outside its workspace.
- *Kept reachable.* The maintainer rules stay startup authority for every role, now
  through that explicit read instead of a shared file. The privacy card's "change
  what Git tracks" trigger now applies to the private workspace's repository. The
  role gate's "a source checkout alone assigns no Director role" still holds here,
  with no installation branch left to choose.

**Tradeoff.** There are now two repositories to keep committed and pushed. A
project-owned sync check in the private workspace reports, for both repositories,
uncommitted changes, unpushed commits and branches without an upstream. It makes a
held push visible but does not prevent one. A change to the method and its private
record are separate commits in separate repositories. Public readers lose the
in-repository example of a mature installation; the fixtures in `test_block_route.py`
still cover the block route.

**Regression cases.** (1) This repository claims no installation. The checkout
holds no `.director/`; neither a `git archive HEAD` export nor the index holds
`.director/` or `.reference/`.
AGENTS.md carries no block, project-section or starter marker and no private request,
source or project ID, and `/.director/` and `.reference/` still match the ignore file.
The rewritten checks in `test_package.py` cover this. A fresh session opened here
gets the maintainer rules only, with no check and no 🎬. (2) The private workspace's
project-section check returns `evidence_matched` with `director_block: unchanged`
against a new technical record written for the move. A fresh session there shows the
check and 🎬 in its first reply, runs the check again and Recovery after a forced
compaction, and gives a spawned worker no check and no 🎬. (3) The move leaves the
store's identity and history unchanged. A hash manifest of every installation file,
ignored files included, and the request-status snapshot are identical before and
after. (4) Both repositories are committed and pushed: the sync check reports clean
for each.

**Status.** *Decided:* as above. *Implemented:* the move, the re-binding, the private
remote and the sync check in the private workspace. The public cleanup (AGENTS.md and
the package tests) is on a branch here, not merged or pushed. *Verified:* the move was
hash-verified, with identical manifests and request-status snapshots. The private
workspace's check returns `evidence_matched`. The private remote was confirmed
private before its first push. 24 fixture tests of the sync check pass. *Pending:* the
public branch's merge and push, and with them oracle (4) for this repository; the live
fresh-session trials for oracles (1) and (2), which are the 3.3 trials that the
November 13 record still lists as pending, now to run in the private workspace; and
independent review of this entry. Acceptance of the maintainer's 3.3 installation
stays pending those trials, as before the move.
**Revisit:** the sync check reports the same held push across many turns; store
conflicts appear between machines; or private material appears in a public diff.

**November 9 — the video template's local-only privacy choice:** The My Work video
template keeps requests, walks, journal and team activity out of Git for every
generated video project, through a root ignore block that first use verifies. The
October 21 decision below makes keeping more local a project's explicit later choice;
here the template makes it at first use. The November 8 installation plan accepted
that, and it is recorded as the template's dated choice, not a change to the
starter's tracked default. The tradeoff is the continuity this decision protects:
those records do not reach a clone or another machine. A generated project that wants
them tracked changes its own recorded choice, and updates preserve whichever choice
is recorded. With no remote, nothing is pushed, so the one-time warning is not yet
due. When a remote is added, the warning becomes due unless the remote is verified
private, and it is recorded as due rather than delivered until it is actually given
(later November 4). The examined project captured sources while its receipt said the
warning had not been given; it has no remote. **Oracle:** first use verifies the
ignore block and records no delivered warning; after a public or unknown remote is
added, the warning is given once before the next capture. **Status:** decided and
recorded; the template already carries the ignore block, so no runtime text changes.
The remote case has not been observed.

**Later November 4 — generation evidence is local handoff, not shared identity:**
The opt-in generator's fresh instance marker records creation/provenance only;
generic seeds contain neither that marker nor initialized config, records or receipt.
First-use control scratch and instance evidence follow the integration's effective
ignore policy before writes. Existing privacy choices remain; setup records warning
due rather than inventing public/unknown-remote warning delivery. No Git init,
commit/push, source capture or update policy is added merely for setup. Generated
native stores receive distinct IDs; moved/configured projects preserve theirs.

**October31 restoration:** Starter2 changed the fresh default to ignored durable
state without superseding this continuity decision. Starter3 restores Git-eligible
config/requests/sources/receipts and once-only public/unknown-remote awareness;
existing privacy opt-outs remain untouched. No automatic commit/push is implied.

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

**November 14 — parallel Directors share the tree too (cross-reference):** The
actors this section lets work in one shared project tree include several Project
Directors that the user starts, often unaware of each other. They notice overlap and
work it out together, and the accepting Director checks the combined result; no
partition, lock or Git rule is added ([R1](#r1--one-accountable-conversation-without-a-forced-organization),
November 14). The revisit trigger below is not met: the field warning there predicted a
collision, it did not observe one.

**November 1 narrow supersession — Git is recovery support, not agent permission:**
The October 23 "under Git" condition could prohibit even useful read-only subagents
in a legitimately non-Git project. The owner now explicitly permits useful bounded
delegation there. Keep all actors in one shared project tree with file/resource
ownership, report the review/rollback/cross-machine limits and preserve verified
backups before writes. Git is recommended; initialize it only at the user's request,
never create a worktree/checkout to satisfy the pattern. This trades Git's change
history for explicitly limited local recovery, not for overlapping uncontrolled
writes. The concrete oracle delegates a useful disposable implementation outside
Git, evaluates its artifact, preserves owned preimages and creates no Git repository.
An unavailable tool or actual higher-priority prohibition remains a separate gap.

**November 1 flat-route correction:** The starter WORKER's "only when authorized by
the assignment" wording had reintroduced an opt-in interpretation after R15 made
bounded descendants the useful-work default. Its loaded AGENTS.md now explicitly
requests useful independent worker subsets, and [WORKER](../pattern/starter/payload/WORKER.md)
requests them unless the assignment's explicit limits prohibit it.
Existing scope, shared capacity, selection guards, supervision and return evaluation
remain. This is not a demand to split small/coupled work or permission to exceed a
parent's scope; a genuine higher-priority restriction still controls. The oracle is
an actual assigned worker using a useful bounded child without a second permission
request, plus a scope/prohibition negative case, not a count of mentioned agents.

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

**Refined, October 30 — batch dependent phases without losing receipts:**
[STATE](../pattern/engine/STATE.md), [RECORDER](../pattern/engine/RECORDER.md),
[IDENTITIES](../pattern/engine/IDENTITIES.md), and
[DIRECTION](../pattern/engine/DIRECTION.md#assign-bounded-work) combine known
capture/setup/reservation requests when timing and authority permit, then batch
actual dispatch bindings and received acknowledgments at the shared checkpoint.
Each item retains its own success or gap. Scope-setting capture still returns
before dependent dispatch, reservation before identity use, and real handles
before execution claims. This removes repeated round trips without substituting
one successful stream's receipt for another. No state schema or new service is
introduced. The regression is a wave with one confirmed dispatch and one failed
attempt: a batched response must retain that difference and cannot claim both live.
Actual host routing and absence of false saved-state claims remain behavioral
checks, separate from fixture/schema guarantees.

## R16 — Separate replaceable engine from project-owned integration

**November 9 — template-local narrowing of the video template's binding (decided
and staged, not yet applied or verified live):** For the My Work video template only,
the three large video docs (`docs/DIRECTOR.md`, `docs/PROCESS.md`,
`docs/CHANNEL.md`) become unbound managed files: its provenance binds 57 files
instead of 60. They, `.team/TEAM.md` and `TEMPLATE.md` also leave the startup and
first-use guards, becoming complete task-time reads named in
`.team/roles/director-startup.md`, as recorded under
[R9](#r9--make-attention-and-active-supervision-visible-without-decoration). A reply
may come first; capture, dispatch and every delivery step, including render and
upload, wait for those reads, and compaction requires them again.

**Why:** In the field the greeting cost about 113 KB of required reads, and a
Director skipped the guard docs and the badge on a one-line note. The template's
bindings had also drifted: 7 of its 60 bound files no longer matched, so the next
generated project would probably fail setup, and a stand-in handoff on a scratch
copy of the current template did refuse. A repair that kept the docs bound would
break again at the next docs publish, since a video doc changed again on November 8,
after the drift.
The un-pinning therefore ships with the repair.

**What stays:** R16's later November 4 bindings that first use needs: the AGENTS hook
file, the remaining guards, the tracker contract (`.team/RECORDS.md`,
`.program/README.md`), the five exact empty placeholders (the empty-seed rule) and
the reviewed journal and team seeds. Generation is still bound by the reviewed
managed hashes, not by current drift. The shared first-use helper and the checker
are unchanged; this narrows one template's binding, not the starter or the helper.
R9's November 2 rule is unchanged for the remaining guards.

**Regression oracle:** On scratch copies of the template, the stage plan is clean; a
generated project completes first use and its check passes, and a second run reports
existing setup; one changed byte in `.director/DIRECTOR.md`, or inside the AGENTS
block, refuses at the handoff, at first use and in the stage plan; an edited video
doc no longer blocks first use or the stage plan; a filled request file or an extra
journal file still refuses, and no bundled store is created; and the greeting's
required reads fall to about 47 KB from 117.5 KB for the same bytes under the old
route. One cold read reached the private-upload rule through PROCESS and
docs/DIRECTOR before acting on "render and upload". These checks first ran against
a provisional pin; after the pin moved to the published 3.2 starter they were
repeated with real exit codes and passed, and an independent reviewer confirmed
the re-pin. The cold read was not repeated: its files are byte-identical.

**Unknowns, acceptance-blocking:** nothing yet checks an unbound doc that contradicts
Director authority; re-reading after compaction is not tested live; the real
generator handoff was not run (a stand-in mirrored it); and the greeting and render
reads were observed in one cold read only. The video system's publish also still
carries two bound stencil-owned files (AGENTS.md and the startup supplement) and
would restore older bytes until its publish route changes.

**Status:** decided in the November 8 installation plan and staged through the
template's staging route; not yet applied to the live template or verified live.
The independent review of the staged revision requires this entry before the
template is applied, and applying it needs the maintainer's yes.

**Later November 4 — retain a semantically empty video seed:** The real generic
video template has five zero-byte `.gitkeep` placeholders in canonical requests/
walks. The initial literal-empty-directory rule below rejected that preserved seed.
The reviewed refinement permits only exact managed empty regular `.gitkeep` files
and their structural directories. Real records, even hash-listed ones, nonempty or
unreviewed placeholders/directories and unsafe paths still block setup. This narrowly
supersedes literal directory emptiness, not the ban on copied user/runtime state;
earlier candidate tests did not establish that the real video scaffold worked.

**Later November 4 — bind generation without initializing the stencil:** The
reviewed template provenance selects first-use helper/backend/receipt/guards; actual
generation adds instance metadata bound to its copied provenance and new root.
The actual selected folder ID may differ from the content profile; both must be
valid, with the provenance digest and managed hashes binding the copied backend/bytes.
The helper verifies the managed baselines instead of blessing current drift.
Completed projects reuse real setup evidence; partial owned attempts recover only
their verified identity/bytes. Existing unknown/configured/custom state is preserved,
and custom contracts acquire no bundled store. This supplies R9's missing creation
handoff while preserving stencil/engine ownership; real generator/cold-first-use and
custom-backend countercases remain required acceptance evidence.
Custom canonical requests/walks must be empty; only expressly reviewed noncanonical
journal and team seed files may match their transport baselines.

**November 1 route and phase clarification:** "Flat layout" in this decision meant
the legacy pre-engine v1 layout, not starter 2/3. The supported transition and its
callers now name that format and exclude incompatible stores. PROJECT retains the
ownership rule at startup while requiring the full BOUNDARY manual before
installation, layout work or engine updates. Other unqualified/transitive authority
guards remain mandatory. The oracle resolves a known pre-engine v1 installation to
that reviewed transition, leaves starter 3 on its own route, and stops unknown
formats before changes. A greeting need not load layout procedures; a later engine
replacement must load them before edits. Existing backup/interface/state protections
are preserved, not summarized away.

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

**November 13 — a quiet stretch does not pause the SitRep cadence:** The November 7
rule below checks on every turn whether a SitRep is due, but a turn comes only when a
worker returns or the user writes. In the November 13 field report (recorded under
[R18](#r18--start-flat-and-make-learning-an-explicit-bounded-loop)) SitReps lapsed
during such stretches until the Director set a five-minute background timer itself.
The supervision card now says: when no worker return or user message may arrive
before the next SitRep is due, arm a supported background timer or wait that leaves
you available to the user and brings you back by then; a quiet stretch does not pause
the cadence; if the host has none, say so once and send each due SitRep at your next
turn. This completes the card's "supported waits must leave both cadences
usable". The interval is unchanged and no host tool is named. **Regression case:**
two long-running workers and a silent user: a labeled SitRep arrives about every five
minutes without any return or message to prompt it; on a host with no timer or wait,
one statement says so and the November 7 fallback applies. **Status:** Decided by this repository's Project Director on November 13, 2026, from
the maintainer's field report, and implemented in the starter source as revision 3.4.
An independent review the same day, with its findings applied, accepted it; the
maintainer's acceptance and publication are pending. Static tests only; no live run
yet, and installed copies keep their adopted text until updated.
Oracle: `test_a_quiet_stretch_does_not_pause_the_sitrep_cadence`.

**November 11 — Recovery steps live in the standing block and also run in a new
conversation; read-only store views need the requests card alone (starter revision
3.3; implemented on a branch, not merged, published or accepted):** Part of the move
recorded under
[R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes).

*Where Recovery lives and when it runs.* Before (November 2 below, and R10 November
9): the recovery rule was a passage of the Director foundation ("On recovery,
retrieve all task-bound request IDs, including terminal ones, through the
continuation view ... correct a false terminal claim ... A completed milestone does
not finish the whole ask"), reached only by re-reading that file after a break. It
existed because a parent marked done with finished children had been treated as a
finished request. In the November 9 draft trial the same steps sat on a card, and
after a forced compaction neither of two sessions opened it. Now: four numbered
steps (find held work, reconcile it with current evidence, resume ownership, report)
are written in the block, so no file must be opened to learn them. They are part of
startup after a compaction or session resume, before the next reply, and in a new
conversation they run before the first reply that acts on the project, which closes
the proposal's known gap of work still out from an earlier conversation. The check's
output also carries a `next` line pointing to them on every run. Step 3 is
task-bound: the Director resumes the outcomes this conversation holds or the user
names, and other open requests stay with their owners. Step 4 asks for a visible
line in that reply, "Re-entered: N requests held; N others open; N workers out",
with "check run" added by the Project Director. Cost: about 1.1 KB of standing text
for every reader, and a store read at the first acting reply of every new
conversation even when nothing is held.

*The SitRep after a break keeps the November 7 rule.* The November 7 entry below
restored "after compaction or session resume, report once promptly only if one is
overdue or timing is unknown", and the supervision card keeps that sentence. The
first rework's step 4 said to send a SitRep "now" whenever work was out, without
that condition. The final commit of the same day makes step 4 conditional: "With
work out, if a 📋 SitRep is overdue or its last time unknown, send one now and time
the next from it." The block, the card and November 7 now agree; nothing is
superseded.

*Read-only store views.* Before (R10 October 30, R9 October 31): the store manuals
(API, TOOLING, RECORDS) are read completely before any store operation, so that a
revision, journal or recovery rule cannot be skipped; the first-reply check was
deliberately kept from activating them. Recovery after every break would otherwise
cost about 36 KB of manual reads before the first reply. Now, with the bundled store
only: three views that change no record (`status`, `continuation`, `current`) may be
run after reading [cards/requests.md](../pattern/starter/payload/cards/requests.md)
alone. The card explains each field and every gap value the helper can return. Any
store write, and `recover`, which is a write, still require the three manuals first;
a project with its own store reads the files its project section names. This is the
narrow form of a wider proposal (routine write commands on the card), which is not
built and not decided. Cost: an agent reads store output without the manuals'
context, and the card repeats part of the manuals and can drift from them. **Open:**
in the one in-flight trial the Director ran the status and continuation views before
it read the requests card, having read none of the manuals; it read the card
immediately afterwards. The block routes the views through the card, and that order
was not followed. Oracle:
`test_card_audiences_and_moved_obligations` ties every gap name on the card to the
helper's source; `test_table_names_only_shipped_files_and_every_card_has_a_trigger`.

**Regression cases:** After a forced compaction with requests held and a worker out,
the next reply follows a fresh check, performs the four steps through the store,
carries the "Re-entered:" line and continues the existing worker by handle rather
than starting a duplicate. A terminal parent with unfinished obligations is found
through the continuation view's `terminal_with_unfinished_obligations` gap and
corrected by the store's legal route. A second conversation does not adopt another
conversation's open requests. A new conversation with work out from an earlier one
runs the steps before its first acting reply. The known-bad case is the November 9
draft trial: zero cards opened, no recovery.

**Status:** implemented on a branch;
`test_recovery_steps_live_in_the_block_not_on_a_card` pins the steps and their
timing. Live, one host, on the build before the Recovery-timing and store-view
changes: in two sessions, each with one real forced compaction, the Director reran
the check, performed Recovery through the store and reported re-entry. Work was
already finished at each compaction. Live, one host, one session, on the reworked
build before the final commit's wording changes, with a real compaction while two
delegated workers were still running: the Director reran the check, ran the
read-only views on both held requests, reported re-entry with the correct count and
both workers named, and did not re-dispatch; both original workers completed with no
duplicate. It sent no SitRep in the re-entry reply and sent them on schedule later.
Closing the requests through the store was not reached. **Observed once; no rate
implied; resume, repeated compaction and other hosts still unverified.** A new
conversation with work out is also not verified, and the final commit's wording has
no live run
([validation](DESIGN_NOTES.md#standing-block-and-cards-starter-33--november-11-2026)).

**November 7 — update staffing (cross-reference):** An ordinary compatible update
is bounded, well specified and checked by the required independent review: a lighter
capability tier at high effort, or the strong tier at medium, with that review kept
at the strong tier and high effort, and harder cases (conflicts, migrations, unknown
provenance, ambiguous adaptations) at the strong tier at high effort or above with a
recorded reason; a field session had dispatched nearly
every update worker on the inherited strongest tier with no effort chosen. Owned by
[R11](#r11--update-from-a-pinned-public-source-without-replacing-project-state);
the rule it applies is [R2's November 5 entry](#r2--protect-judgment-and-conversation-from-executionbookkeeping).

**Later November 7 — an example of the suggested shape:** The maintainer found some
SitReps easier to follow than others, chiefly ones that make it easy to see who is
doing what, its status and its next step, and asked for an example rather than a
required format. Starter [DIRECTOR](../pattern/starter/payload/DIRECTOR.md) now lists
**In progress** as (who, what, actual status, next step) and follows the SitRep
paragraph with a short example: a table with Who, Doing, Status and Next step columns,
framed as a table where it renders well, with the same columns as lines also fine.
Independent review then added blank lines so the example renders as a table when
copied, filled every Next step cell and changed the intro to "For a full SitRep, for
example"; the [SitRep example](DESIGN_NOTES.md#pending-scenarios) scenario stays
pending.

**Why/tradeoff:** An example shows the intended content faster than more rules, and the
shape stays a suggestion: any layout with full coverage still satisfies the duty. The
maintainer chose a table over lines or both; lines stay acceptable because rendering
varies by host. The cost is about 12 more lines in a file every conversation reads,
and an example's names or content could be copied literally.

**Regression cases:** A SitRep that gives the same columns as lines passes. One that
drops who, status or next step for a held stream, or hides a ❓ question or 🖐️
user-only action, fails. Copying the example's names or content instead of the actual
actors and work is wrong.

**Status:** Decided by maintainer choice on November 7, 2026 and implemented in starter
DIRECTOR wording with a static package test; live uptake is unverified. The v1 engine
is unchanged.

**November 7 — check each turn whether a SitRep is due, restore coverage and suggest
a shape:** An adopting multi-day video project on the flat starter reported about 46
hours without a labeled 📋 SitRep while notification-driven delegated work stayed
held; one-line "still waiting" notification replies took the report's place, and the
owner had to ask about state. The October 27 rule was present, but nothing made each
notification turn a place to check it, and the starter's compression of legacy
DIRECTION had dropped coverage of quiet, stalled and unevaluated streams, brief
unchanged reports and the no-full-block line. Invisible elapsed time, notification
turns read as acknowledgments and a hard-to-find rule remain hypotheses.

The maintainer approved the triaged change. Starter
[DIRECTOR](../pattern/starter/payload/DIRECTOR.md) now checks on every turn,
including worker returns and notifications, whether a SitRep is due, using host
timestamps or a clock check, and notes each SitRep's time. It covers every held
stream, gives one line per held stream, not the full shape, when nothing changed
since the last SitRep, uses ordinary prose between due reports and suggests **Done**
· **In progress** · **Waiting on you** (❓ questions, 🖐️ user-only actions, or
"nothing") · **Next**. Notification replies, like ordinary progress, neither reset
nor replace a due report. After compaction or session resume it reports once promptly
only if one is overdue or timing is unknown, restoring the October 27 "if overdue or
timing is unknown" condition, and times the next from that report; a notification
wake-up is not a resume. Without any time source it says so once and reports at each
user message or held-stream change.

**Why/tradeoff:** The interval stays about five minutes or the agreed interval:
nothing showed the number caused the lapse, and projects can already tune it. On
hosts that give no timestamps, the per-turn check costs one extra small clock call
each turn; the field session had ~220 wake-ups. A silence rule for notification
replies was rejected; the owner did not ask for silence, hosts may render a reply
every turn, and routine acknowledgments already need no extra message. Reporting only
at meaningful changes or on request was rejected because it restores the October 27
failure where the user had to ask. The shape is a suggestion, not a requirement: any
order with full coverage satisfies the
duty. When turns arrive further apart than the interval, each notification turn is
due; the one-line unchanged report keeps that brief. The no-time-source fallback is
the maintainer's call by approval. It should be rare, since delegating hosts usually
expose a clock, but reporting at each user message could add reports to rapid
exchanges; only the one-line rule limits that.

**Regression cases:** Over three or more intervals of notification-driven held work
with one stalled stream, the first turn after each interval carries a labeled SitRep
naming that stream and what waits on the user; "nothing new" turns spanning a due
interval without one fail. Sparse unchanged notification turns each carry at most a
one-line-per-stream SitRep; full blocks on consecutive unchanged turns fail. Several
exchanges inside one interval get direct answers and at most one full SitRep (R9
October 19). An informative update or notification reply does not reset the clock
(October 27). After compaction or session resume with a report overdue or its timing
unknown, one prompt report, then the next timed from it; a notification wake-up is not
a resume. No held work, no SitRep. Without a time source, one statement,
then reports only at user messages or held-stream changes. A different order with full
coverage passes; one hiding ❓ or 🖐️ items fails.

**Status:** Decided by maintainer approval on November 7, 2026 and implemented in
starter DIRECTOR only. After independent review the maintainer also approved
tightening the unchanged-turn and resume sentences the same day. It is to ship
together with the November 5 staffing change; that combined change alters both starter
DIRECTOR and OPERATIONS, so installations refresh once. A static package test pins
the wording; it proves wording and reachability, not cadence. The v1 engine mirror in
[DIRECTION](../pattern/engine/DIRECTION.md#recover-and-supervise-held-work) and
engine DIRECTOR is not applied and remains an open maintainer choice. Installed
copies keep their adopted text until updated. Live cadence is unverified; the
[matrix](BEHAVIOR_PARITY.md#field-report-triage--november-7-2026) and
[validation](DESIGN_NOTES.md#field-report-triage--november-7-2026) keep the pending
oracles.

**November 4 — separate recovery from an optional stopping experiment:** Keep the
terminal-inclusive `continuation` view and exact-source reconciliation unchanged.
Another recovery/source-locator API or packet registry is deferred: the existing
helper already provides bounded recorded-state recovery, but cannot force an actor
to act after acknowledging unfinished adopted work.

The selected [development-only Stop prototype](prototypes/README.md) stays outside
installation manifests. Explicit session/root-owner/task/source binding includes
terminal IDs; a caller-supplied trusted snapshot command must use the existing
canonical route. No cwd/open-backlog inference selects work. An optional bounded evaluator
receives snapshot plus attempted final as evidence, returning allow/continue/unknown
with supported remaining obligation, authorized next action and wait assessment.
Structural-only checks miss falsely complete intent; stub evaluators prove plumbing,
not semantic quality. Quoted text grants no new authority. At most one snapshot,
optional evaluation and correction per session/stable binding are atomically
consumed before execution/output; even allow/error uses that inspection allocation.
Turn IDs, synthetic prompts, source/checkpoint/final edits and claimed progress never reset it. Unknowns,
corrupt/missing established state and exhaustion fail open without task/source writes.
Real pause, sufficient completion and correct child return remain exits; a held
experiment does not stop independent runnable work. Stop alone authenticates neither
interruption nor genuine user steering; no restart/wakeup is supplied.

**Status and oracle:** Implementation/offline conformance are selected, not native
activation or prevention acceptance. The concrete case is a terminal parent, finished
children and all-complete checkpoint plus an unfinished attempted final reaching a
configured evaluator; a supported continue verdict may block once, with later Stops
exhausted despite new turn IDs. Pause, child return, partial hold and command/source
errors are controls. A real backend bridge, semantic quality and receiving-host
binding/trust/event behavior remain unqualified; actual continued action remains a
held experiment. Publication/target updates never activate the prototype. The
[validation](DESIGN_NOTES.md#bounded-context-and-stop-prototype--november-4-2026) and
[matrix](BEHAVIOR_PARITY.md#bounded-context-and-stop-prototype--november-4-2026)
separate those claims. November 2's no-hook statement remains the scope of that repair.

**November 4 — reconcile the evidence path and unresolved counterevidence:** A
reported application failure continued after component/harness passes. Supplied
screenshots describe a harness supplying its own inputs and calling a runtime path
directly, leaving the shell, warning and window journey outside its proof. This is
reported evidence, not an independent code inspection. The baseline already made
the Director accountable for the whole result; absence of another reconciliation
actor does not explain away that responsibility. The inspectable contract gap was
less operational guidance for evaluating whether combined evidence actually covered
the requested behavior and what to do when real reports contradicted narrow passes.

The flat [DIRECTOR](../pattern/starter/payload/DIRECTOR.md) and legacy
[DIRECTION](../pattern/engine/DIRECTION.md#stay-with-execution-and-evaluate-returns)
now require that comparison at planning and meaningful returns. For runtime claims,
identify the relevant user entry through observable result, substituted inputs and
bypassed parts. Retain supported component milestones, but resolve contrary reports
or keep the whole-result gap open. A mismatch or repeated unresolved failure triggers
reassessment of approach and proof before another narrow repair. Use a known-bad or
regression comparison when it distinguishes a repair; select the smallest adequate
proof rather than requiring a full end-to-end suite universally.

Useful investigation, integration and review can be entrusted to qualified actors
with bounded judgment, repair and next-action authority. The
[staffing guide](../pattern/starter/payload/OPERATIONS.md#staffing-and-maintained-roles),
[assignment caller](../pattern/engine/ASSIGNMENT.md) and
[record mapping](../pattern/starter/payload/RECORDS.md#outcome-ownership-in-the-record)
carry that authority without another mandatory actor or canonical acceptance
operation. Positive findings can activate an already-authorized phase; actual
reserved gates and Project Director final integrated acceptance remain. A substantive
author cannot supply its required independent review. Per-file approval
queues are not the replacement for thoughtful evaluation of returned judgments.

**Tradeoff and oracle:** This adds judgment about evidence sufficiency and possible
strategy change; it cannot guarantee that an actor will make that judgment well.
Give an owner green component returns plus repeated unresolved user failure and a
harness bypassing the affected production journey. It must preserve useful partials,
identify the proof gap, reassess and take the next suitable authorized action rather
than declare the whole result complete or default to another narrow patch. Qualified
independent branches should progress under bounded authority; scope/privacy/backend
changes still escalate. A small coupled task stays flat, and a sufficient bounded
result or real pause remains a valid exit. The existing terminal-parent recovery,
source custody, native recording, human gates and supervision triggers are unchanged.
This is an implemented instruction candidate; [validation](DESIGN_NOTES.md) must
separate source/fixture checks from actual uptake and any later native adoption.
The [constructed scenarios](fixtures/whole-result/README.md) preserve the proof-path,
delegated-authority, false-done and small-flat-task countercases without publishing
private source material or claiming a product reproduction.

**November 2 — retain parent obligations after all children finish:** A reviewed
continuation failure had completed children and a parent marked done, followed by
an explicit acknowledgment that adopted work remained unfinished. The owner answered
the status question and ended its turn without taking an available authorized next action.
The existing instructions already required continuation; this is not evidence that
an instruction was simply absent. An exit check concerned only with running or
unevaluated descendants, or only open records, misses this case.

The accepted portable repair direction retains the flat owner and existing canonical
backend. At meaningful steering and return evaluation, reconcile the adopted outcome
with its latest sources, preserve accepted partial results and retain remaining
obligations plus the next authorized action or concrete wait. Answering a status
question, accepting a milestone and finishing a worker do not close remaining parent
work. A hold applies to its affected activity; continue independent authorized work.
Before completion, compare the whole result and evidence with the sources even when
the record already says done. Keep sufficient bounded completion, explicit user
pause/cancellation/replacement, real dependency/authority/host limits and acknowledged
independent transfer as genuine exits. A bounded worker may correctly return while
its parent still owes work; optional inquiry is not an endless adopted obligation.

The source candidate adds a bounded `continuation` view to the existing
[owner wrapper](../pattern/starter/payload/requests.py), with the exact command and
versioned ordinary-note checkpoint documented in
[API](../pattern/starter/payload/API.md). Explicit caller-supplied request IDs include
terminal records; the view exposes current sources, latest checkpoint/event locators
and missing, stale or contradictory recorded facts through validated native replay.
It creates no new tracker, schema, owner, lifecycle operation or automatic binding
from the current directory/open backlog. Current `status` excludes terminal requests
and `current` omits historical note text; those commands alone cannot supply this
checkpoint recovery view. The wrapper, API and Director/DIRECTION changes are
implemented, with 15 independent installed-CLI cases passing; acceptance and actual
host behavior remain separate.
The [validation record](DESIGN_NOTES.md#portable-reconciliation-and-composed-project-guidance--november-2-2026)
will distinguish their actual scope.

**Tradeoff and regression:** The checkpoint/view makes recorded unfinished work and
false terminal contradictions easier to recover. It cannot infer omitted user
obligations, authenticate declarations or force continuation. Independent source/scope
evaluation and the owner's actual next action remain required. Replay a done parent,
completed children and a checkpoint with remaining authorized work: retrieve it by
explicit ID, preserve accepted partial results, reconcile sources and actually resume
or dispatch before voluntary yield. Include a held experiment with still-authorized
research, a real pause, correct child return and sufficient completed bounded work as
countercases. An old source frontier, newer malformed checkpoint or pending native
transaction must give its actual gap, never silently certify an older state.

No Stop hook, scheduler, native role replacement or cross-harness launcher is supplied
by this repair. Optional enforcement would need separately qualified host binding,
source access and finite correction controls; source tests cannot establish it or
claim that advisory instructions now prevent the previously observed behavior.

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

**Refined, October 30 — close the touched knowledge path:** At meaningful
closure the accountable owner reviews the affected selector, canonical artifact
pointers and accepted facts under
[ROLES](../pattern/engine/ROLES.md#improve-the-systems-knowledge). Correct supported
stale claims through the existing owning maintainer/worker route; preserve dated
exploration, superseded reasons and exact history. Runtime observations belong in
scoped evidence, not present-tense operating defaults. Evaluate the correction at
its next relevant use. An unresolved proposal is retained without inventing a new
approval gate for delivery. This is local upkeep, not a role census, recurring
service or arbitrary size limit. The regression is a completed canonical guide
whose selector still says the guide may not exist, or a shipped feature still
listed as pending: refresh the current pointer/status while retaining its earlier
history and unrun acceptance gates. Static edits can establish preservation and
reachability; the next actual selected use must establish uptake.

## R18 — Start flat and make learning an explicit bounded loop

**November 14 — "one Project Director" means one accountable owner per outcome
(cross-reference):** This section's "a new starter has one Project Director" and "the
rest stands: one Project Director" describe the flat shape, one accountable owner per
outcome with bounded workers and no manager layer. They do not limit how many Director
conversations run in one folder; several are expected and cooperate
([R1](#r1--one-accountable-conversation-without-a-forced-organization), November 14).
"Use one for sustained coordination, not each branch" is about staffing a scoped child.

**November 13 — look back on the work: propose a role for recurring work and a cut for
a step that does not earn its cost (starter revision 3.4):** A field report from an
adopting video project, written after it shipped a video and held a retro (the run
used starter 3.2 text; the project moved to 3.3 after the ship, and the rules at
issue read the same in both),
named one kind of mistake in several places: the Director treated the roster and the
recorded steps as a fixed lookup table, not as something it routes through and
maintains. Recurring work (after-action reviews, analysis of the owner's own edits,
overnight render and upload chains) was briefed from scratch to general workers each
time, and no role was ever proposed. Every recorded step was applied as fixed
procedure, and none was ever proposed for a cut or merge. A process answer given once
in chat was never found again. The existing loop questions structure only after a
failure: incidents feed a bounded review and perhaps a `structure` proposal, and a
repeated failure calls for reassessment. Work that recurs without a correction, and a
step that costs more than it returns, trigger nothing, and closure upkeep covers only
the touched path, "not a role census"
([R17](#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request),
October 30). The diagnosis is the Director's; that the missing trigger caused the
behavior is a hypothesis.

The knowledge card gains a "Look back on the work" paragraph; the block's table
sends "close an outcome, or hold or brief a retro" to that card, and the staffing
card's brief says a retro or look-back brief carries the card's two questions. At meaningful closure, and at any
retro or after-action, the Director asks two questions of the work this conversation
held, not of all history: what was briefed more than once, or rebuilt from scratch,
that no roster role holds; and which recorded steps, records or rules cost more than
they returned, or could merge. Each supported answer goes to the user as one ❓
proposal: a role (what its file would hold, its roster row) or a cut or merge (the
step's source, its cost, what would break). A step whose source is a user rule, an
authority gate or required independent review stays unless the user changes it. A
proposal changes nothing until the user decides; an accepted one becomes a request
for the owning maintainer, and a new role is registered before use. One repeat is a
candidate, not a department; nothing is proposed when nothing recurred and every
step earned its cost. A delegated look-back carries both questions, and the answers are kept where
the project keeps findings the user reads back, not only in chat.

**Why/tradeoff:** This keeps "departments follow recurring responsibility and
coordination needs observed in real work" (below) and gives the observation a place
where the work is still in view. It stays bounded: two questions about one
conversation's work, no count threshold, no automatic role creation, no upstream
retro role, and no change to LEARNING or the store. A count threshold was rejected
because a count already "never creates a department" and one repeat can be worth
naming. The cost is a short step at closure and a ❓ per proposal; the risk is
proposals on thin evidence, which "say how thin the evidence is" limits.

**Residual risk, knowingly accepted:** the look-back lives on a card, and the card is
read only if the Director opens it at the table's trigger; the November 11 matrix
already lists that trigger as unproven for this card, and one earlier session skipped
it after a compaction. Moving the paragraph into the block was not possible within
its 8,000-byte cap without dropping a rule *(November 14: that cap is now an authoring
budget for the shipped block, not a limit on a project; see [R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes), November 14)*. The table row now names a retro, and the
staffing card puts the questions in every retro brief, which narrows the gap but
does not close it. The Director accepted this risk on November 13; a live retro is
the oracle.

**Regression cases:** In a retro after the same analysis was briefed from scratch
three times, the Director proposes one role as a ❓, naming what its file would hold
and its roster row, and registers it only after the user accepts. A closure where
nothing recurred and every step earned its cost proposes nothing. A step whose cost
exceeds its return is named with its source and what would break; a step from a user
rule, an authority gate or required independent review is not cut without the user.
A delegated retro brief carries both questions. The answers end up where the project
keeps findings, not only in a chat reply. A Director that adds a role, cuts a step or
edits a role file on its own fails.

**Status:** Decided by this repository's Project Director on November 13, 2026, from
the maintainer's field report, and implemented in the starter source as revision 3.4.
An independent review the same day, with its findings applied, accepted it; the
maintainer's acceptance and publication are pending. Static tests only; no live run
yet, and installed copies keep their adopted text until updated. The [matrix](BEHAVIOR_PARITY.md#field-report-triage--november-13-2026) holds the dispositions and [validation](DESIGN_NOTES.md#field-report-triage-starter-34--november-13-2026) the checks.

**November 11 — the starter's route changes; its shape does not (cross-reference):**
Starter revision 3.3, implemented on a branch and recorded under
[R10](#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes),
supersedes two statements in this section. The November 4 plan below preserved "host
hook → START → selected DIRECTOR/WORKER/guards"; the active route is now the
host-loaded block in AGENTS.md, with cards read before named actions, and START and
DIRECTOR are redirect stubs. The October 31 correction below said no "startup
catalog returns"; a project-owned roster summary now sits in the standing project
section (R10, item 9). The rest stands: one Project Director, bounded workers, no
mandatory Recorder, manager, setup actor or identity pool, the established
request-bundle backend, and the bounded learning loop, which now lives on the
knowledge card and in LEARNING. The checked-marker meaning preserved on October 31
is narrowed as
[R9](#r9--make-attention-and-active-supervision-visible-without-decoration) records.
The [matrix](BEHAVIOR_PARITY.md#standing-block-and-cards--november-11-2026) carries
the obligation-by-obligation disposition against the previous route.

**Later November 4 — one deterministic generated setup, then the normal route:**
[R9](#r9--make-attention-and-active-supervision-visible-without-decoration) adds a
guarded first-use helper and real generation handoff, not another actor, tracker or
startup framework. The ordinary checker remains read-only. Existing native backend,
privacy, full instruction loading, staffing, recovery, updates and learning triggers
remain reachable. Generic templates and arbitrary markerless/mature projects never
gain initialization authority from an absent receipt. Source/fixture checks alone
cannot close the observed first-reply defect; actual generated cold use is required.

**November 4 — bounded implementation plan, no packaging replacement:** Preserve
host hook → START → selected DIRECTOR/WORKER/guards, native canonical I/O,
terminal-inclusive continuation and existing staffing/upkeep/learning/update triggers.
Restore R9 attention instructions; add one optional model-free
[context calculator](../pattern/starter/payload/context_check.py) through a small
[OPERATIONS action reference](../pattern/starter/payload/OPERATIONS.md#optional-context-budget-preflight),
plus R17's development prototype. Independent review and focused checks precede
acceptance. No new global config, skill, role framework, tracker or migration follows.
Existing default/legacy packages and project adaptations retain their selected routes.

The calculator's explicit input is the caller-resolved counted file chain, raw-byte
required boundaries and cap/evidence. It is not another configuration registry.
`effective` is caller-declared evidence, `default` a conditional prediction, and
`unknown` ignores any number. It reports total and required-boundary fit separately,
with hashes/predicted prefixes and no bodies; every result retains
`actual_admission:unqualified`. Host discovery/overhead, received text, consumption
and compaction are not measured. Aggregate fit covers only positive asserted
boundaries; null/zero boundaries certify no required coverage. It cannot restore a
cut pointer or raise a host limit, and adds no first-reply duty to the unchanged checker.

**Disposition and oracle:** Preserve progressive loading and exact read/recovery;
add diagnostics rather than substitute shorter prose or native repackaging. Check
exact-cap/overflow, early boundary fitting with total over, later omitted pointer,
multibyte bytes, provenance, unsafe/changing inputs, bounded body-free output and
startup-checker compatibility. Recovery API expansion and automatic packet/role
frameworks are deferred. Unknown route/cap/native proof blocks the corresponding
claim, without a universal startup gate. [Validation](DESIGN_NOTES.md#bounded-context-and-stop-prototype--november-4-2026)
separates implementation from publication, adoption and behavior; no future published
pin is selected here.

**November 2 — finish the portable reconciliation within the existing core:**
[R17's continuation repair](#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request)
keeps adopted parent work recoverable after child completion and even a false terminal
record. It preserves accepted partial results without treating their milestone as
the whole outcome. A versioned checkpoint is an ordinary canonical note, not accepted
learning, a second store or a new backend schema. Existing legal steering/reopen,
source custody, revision/recovery, independent verification and human gates remain.

The existing [ROLES selection/execution split](../pattern/engine/ROLES.md#selection-knowledge-and-execution-knowledge),
[assignment contract](../pattern/engine/ASSIGNMENT.md) and flat
[staffing route](../pattern/starter/payload/OPERATIONS.md#staffing-and-maintained-roles)
already provide the small caller interface and full executor context route. Preserve
these rather than install another registry, resolver or mandatory specialist layer.
A responsibility's purpose, authority and return contract survive authorized subagent,
separate-session or cross-harness delivery; an unsupported transport is a specific gap,
not execution. Accessible authorized source/context and actual return evidence are
still required. A concise contract clarification now carries these same responsibility,
source-access and return boundaries in flat DIRECTOR and legacy ASSIGNMENT; legacy
canonical recording still uses its configured Recorder. This is contract portability,
not four executed integrations. No new global skill, native adapter or universal host
support follows.

This is a bounded source repair with separate implementation, deterministic checks,
independent review and actual-host adoption claims. The full affected-purpose matrix
retains update discovery, project privacy/continuity, role upkeep and scoped learning
at their existing triggers. A shorter route must not make those unchanged mechanisms
unreachable. Source availability and a recorded checkpoint prove neither later uptake
nor autonomous supervision after the host stops.

**Retained delivery qualification:** Complete selected-read instructions cannot
raise a host's automatic project-instruction budget or restore an omitted entrypoint.
At an affected installation/update qualification, retain the actual selected override/
root-to-working-directory chain, raw file bytes and required entry boundary, known
versus default-only versus unknown effective cap, required access/query controls and
observed returned-read coverage. A model-free file inventory can expose a known
oversize chain; it cannot establish the Desktop's effective admission, actual prompt
consumption or compaction restoration. Automatic delivery, available manual references,
returned complete reads and applied behavior are separate claims. Preserve progressive
loading, individual/aggregate output headroom and contiguous truncation recovery;
unknown actual-host admission remains pending qualification. No new universal startup
file, larger user setting or native delivery guarantee is supplied by this repair.

**November 1 delegation clarification:** Flat removes compulsory coordination and
specialist layers, not workers for substantial analysis or project changes. The
host-loaded request is now a direct action instruction. Optional named actor choices
remain in the detailed foundation; they no longer dilute the startup hook. Direct
discussion and narrow validated recording stay with the owner. No new startup
file, manager, permission ritual or permanent actor is introduced. See R10/R15 and
the [affected-purpose disposition](BEHAVIOR_PARITY.md#delegation-exception-correction--november-1-2026).

**November 1 instruction audit:** The live record guide still said the outcome owner
could not accept its own outcome, contradicting one Project Director owning and
accepting a flat worker result. It now states that the Project Director evaluates
the whole submission and accepts; workers/scoped child Directors cannot self-accept
for it. Required independent verification and human gates remain. Notes keep actual
identities/handles and any project-required roster, without creating a flat roster.
The action guides now state current guards directly: no backend initialization to
pass a check, exact updater root, re-open after stale-instance rejection (including
init), and untyped-note quarantine. Their code, schemas and wire/lifecycle order are
unchanged. Runtime implementation anecdotes are removed; the reasons remain here.
The shorter startup text retains complete selected reads, individual/aggregate
output bounds, contiguous EOF coverage, recovery/stop and no hash-as-read claim.
Knowledge matching and transitive action-reference phases were deliberately not
loosened: an unknown scope or guessed miss cannot justify skipping required rules.

**October 31 first-reply refinement:** Removing a setup actor did not make the
Project Director's operational check optional. R9/R10 now require a concrete bounded
local check automatically before the first ordinary response, including greetings,
and actual retry on a missing-badge question. The flat/default role and exact worker
packages remain; workers/child Directors bypass this check. Technical evidence
stays in context without backend/history operations or a new startup receipt write.
This targeted correction does not claim native startup on every host, full ledger
validation, permission authentication or broader behavior from a badge.

**Correction, October31 — preserve the reasons as well as fewer actors:** The first
starter2 implementation incorrectly treated record mechanics and operational duties
as replaceable overhead. Reproduced regressions erased original owner/acceptance
on update, retained accepted state after new work and missed corruption of earlier
source. Its five-state JSON store omitted established dependency/handoff/local-file
and journal semantics. This was not an authorized change to R3–R6/R14/R17.
Starter3 restores the established request-bundle backend behind flat roles, plus
direct validated owner I/O and canonical-note learning; experimental2 remains
unsupported history with no automatic migration. More deferred code on disk is an
acceptable cost for preserving request-local custody, exact source/UUID identities,
seven-state folder lifecycle and recoverable evidence. Code bytes are not startup
model reads. New actor instructions must actually trigger meaningful decomposition,
full acceptance/owner/human gates, legal steering and parent/requirement tracing;
identical backend bytes alone do not establish those results.

Restore R9/R17 visible identity and labeled periodic reports, R10/R15 current
capability/effort/verification and role discovery/upkeep, R11 real active-session
24h failure-throttled discovery/preferences/pinned safe update, and R14 Git-eligible
durable state with once-only public/unknown-remote awareness. Preserve every
existing project's explicit privacy choice; eligibility is not a commit/push.
No pool, mandatory Recorder/manager/setup actor or startup catalog returns.
**Preserved checked-marker meaning:** 🎬 is used only after the Project Director
evaluates a light direct current-conversation installation/role check. Before that
it acknowledges the unverified role without a badge. A role-only marker was
considered, not accepted as the default. No mandatory checker/Recorder returns;
unknown native-host behavior/effective settings remain distinct. Sparse question/
user-action meaning remains.
Touched current guide/role upkeep is independent of the learning review threshold.

A later intent-by-intent review also caught a regression in the first corrected
canonical-note layer: removing proposal types let accepted routing/structure text
enter task knowledge. The earlier prototype distinguished those kinds, but its
specific exclusion test was lost during test migration. The repaired layer requires
typed proposals, selects only accepted knowledge/explicit rules, preserves unknown
legacy notes as unclassified history, and reports structural implementation as
pending work rather than completed knowledge. Retirement clears current work flags
without rewriting the original decision. A large green test count had not proved
this untested obligation; independent purpose-case review supplied the missing oracle.

The [design-obligation matrix](BEHAVIOR_PARITY.md) maps documented original reasons,
flat routes, intentional differences, regression oracles and remaining limits for
the whole legacy manifest. This is implemented correction work under evaluation,
not full parity or adoption proved by CLI tests. Exact sources, failed experiments
and earlier reasoning remain; [validation](DESIGN_NOTES.md#behavior-preservation-correction--october-31-2026)
separates code fixtures, assigned actor traces and unproved native cold behavior.


**Decided October 30, 2026:** A new starter has one Project Director that stays in
conversation and retains the complete outcome, with bounded workers for execution
and independent review. An additional Director is a choice for sustained detailed
coordination, using the same base role with scoped/domain overlays. It is not the
normal wrapper around each outcome. This supersedes R1's October 21 default Request
Manager route and R2's October 23 mandatory child-coordination route for the starter.
Complete-outcome ownership, delegated substantial execution, supervision, authority
and acceptance boundaries remain. Specialist stewardship alone never creates
another owner.

The active Director owns validated supported recording operations. The starter
requires no separate Recorder, Manager, Architect, identity pool or setup-check
actor. This supersedes the mandatory Recorder/identity staffing prerequisites of
R2/R10 for that new path; it does not permit concurrent arbitrary writers or turn
workers into canonical-state owners. Existing installations and custom trackers
use a separate explicit preservation/integration path. They are not silently
migrated or flattened. Replaceable engine/project-owned integration remains an
ownership boundary, independent of the project's organizational shape (R16).

**Why and tradeoff:** The earlier design required coordinating and bookkeeping
actors before a particular outcome had demonstrated that need. Reducing actors and compulsory setup can reduce
that overhead, but file counts do not measure startup latency, model usage or
installation duration. A reported slow installation motivates investigation;
it is not a measured causal explanation. Small startup and a narrow fresh-folder
entrypoint must coexist with preservation of existing authority, adaptations,
unfinished work, original sources and independent testing.

**Observed tradeoff:** The bounded v3 trial demonstrated utility with substantial
overhead: 59 slide-phase calls versus seven for a plain worker, or 37 versus six
when clear harness waits are excluded. A narrow two-instruction-file v4 retry
batches meaningful persistence checkpoints, supplies exact paths and uses supported
message waits; it observed 30 calls, or 26 excluding waits. Guidance and harness
changed together, so the result is not a clean causal comparison or an economic
win over plain execution. [Validation notes](DESIGN_NOTES.md#narrow-efficiency-retry--frozen-v4)
retain token accounting, cached-input limits, startup misses and the unchanged
helper/API/installer boundary. The value of richer recovery and scoped learning
must be weighed against that remaining overhead.

Departments follow recurring responsibility and coordination needs observed in
real work. A narrow published entrypoint exposes applicability, input, result and
authority; internal organization can evolve behind it. Shared base roles and domain
knowledge compose rather than duplicate a generic Director for every specialty.
No full department service catalog is required at installation. A task count
alone does not create a layer. Accepted craft knowledge, a maintained named role
and a department caller header are distinct project-owned knowledge paths. An
authorized maintainer implements new routing and adds a project-owned startup
pointer to the header without editing the managed foundation. Accepting a structure
proposal supplies neither that implementation nor automatic discovery of arbitrary
files. Composition must not collapse independent verification, explicit approval
or other authority gates.

**Learning correction:** The Director does not automatically remember every past
assignment, result and correction. Repeated problems cannot be reliably noticed
from context that was never loaded. Reading all project history at each startup
would instead make conversation pay an ever-growing cost. R17's touched-knowledge
upkeep remains useful, but is not evidence that historical pattern detection
happens for free.

Use durable, scoped incident/correction evidence and a compact current summary
of commitments, pending review and knowledge selectors. The Director applies an explicit user instruction immediately within its
scope, and retains the relevant evidence; `accept-rule` durably records an already
explicit rule without review or a count threshold. During active supported execution
the default owner initiates a bounded independent reviewer at meaningful closure
when three incidents are pending and capacity exists. That count batches spend;
a direct review request can bypass it. An explicit-request installation policy is
also available. That reviewer
reads only queued evidence after a retained successful-review cursor, identifies
supported patterns and uncertainty, and returns proposals. The accountable owner
evaluates them before accepted rules reach the owning maintained knowledge.
Startup reads compact commitments and a knowledge count/pointer, not the
historical evidence queue or all accepted lesson text. Task-time paginated scope
discovery exposes canonical task/audience/path selectors before matching; guessed
category names must not silently miss retained lessons. Discovery includes
overlapping path scopes, while execution selects for actual affected files;
discovery never broadens a rule. This is scoped lookup,
not a semantic history-search engine. The matching task then loads its complete
applicable accepted rules, and its result must be checked;
storage, acceptance and actual uptake are separate claims. Incremental batches do
not guarantee global or cross-batch trend detection: an issue split across already
reviewed batches may need targeted historical investigation. Durable evidence is
not a reviewer's retained memory. Three pending incidents need not share a cause;
this scoped loop is not comprehensive self-healing.

Review initiation is an active Director duty, not an implied daemon or scheduler.
If the host cannot run the review now, it remains pending for the next active
opportunity. Bounded review preserves a retryable cursor and unfinished evidence;
failed/interrupted review must not consume unseen corrections. Reviewer work has
model, time and context costs, which must be measured when available and otherwise
reported as unknown. Bounded returned context does not imply constant storage cost:
the starter helper reads its state file internally, so its I/O grows with the store.
An optional Architect may own recurring review when justified; one is not required
merely to install the starter. Periodic off-session review
requires separately configured actual host execution, authorized scheduling and a
return/evaluation route; the starter does not implement that service. Three
corrections are evidence to evaluate, never an automatic department-creation
threshold or universal policy.

**Concrete regressions:** A fresh slides request creates one accountable Director
and a bounded author, without mandatory Manager/Recorder/Architect staffing. A
midstream request to keep participant instructions concise reaches the current
owner and survives recovery. A subsequent Director reads its compact scope and
pending review summary rather than every prior deck. A separate bounded reviewer
can propose a course-slide rule from retained incidents; interruption leaves the
unreviewed tail available. An owner rejects an overbroad rule but accepts a narrow
supported one. A later matching slide assignment loads that lesson; an unrelated
technical report does not inherit it. Temporary multi-artifact coordination can
justify another Director, and recurring coordination can justify a department
without changing independent testing or publication authority. An existing project
with a custom tracker and local release policy preserves both until reviewed
integration, even though the fresh-folder starter is smaller.

**Contracts and status:** The [package entrypoint](../pattern/README.md) owns the
new-install versus existing-project routes. The [starter foundation](../pattern/starter/payload/DIRECTOR.md),
[learning contract](../pattern/starter/payload/LEARNING.md), and
[current request-bundle backend](../pattern/starter/payload/request_store.py) own the new path.
The [plain-language guide](FLAT_STARTER.md) explains the progression. This is an
implemented unreleased source candidate. Publishing its source on main is separate
from a release tag or target adoption. Observed behavior, inventories, timing
limits and remaining gates are separated in
[validation notes](DESIGN_NOTES.md#flat-starter-and-bounded-learning--october-30-2026). This decision does not publish a
release, update the current live installation or adopt another project. Revisit if
compact recovery omits accepted scope, review fails to resume without lost evidence,
new lessons never reach matching work, coordination still monopolizes conversation,
or the smaller entrypoint weakens preservation or authority.

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
