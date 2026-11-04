# First candidate design notes

The candidate supports outcome ownership, recursive worker delegation, active
supervision, evaluated closure, exact intent capture, interruption recovery, and
evidence-backed improvement. The installed contract stays small and project-local.
These public notes describe validation scope; source conversations and internal
references are retained privately and are not installation dependencies.

## Where the reasons live

[RATIONALE.md](RATIONALE.md) is the canonical evolving explanation of WHY: current
directions, status, alternatives, tradeoffs, and revisit triggers. These notes
retain validation scope rather than a second decision history.

The [storage comparison](REQUEST_STORAGE_COMPARISON.md) explains generic design
alternatives, and the [relationship design](REQUEST_RELATIONSHIPS.md) describes
independent outcomes and peer-owned execution without imposing a universal tree.
Request folders and typed links are implemented. Verification evidence remains
separate from that selection; documentation does not authorize real-store migration
or external communication.

## Manual scenarios before adoption claims

| Case | Required observation |
|---|---|
| Inherited director history | Child and grandchild stay workers unless explicitly scoped directors; each parent evaluates descendants. |
| Raw multiline message and correction | Recorder receives exact source, preserves bytes once, links distinct outcomes, appends tiny steering without rewriting originals. |
| Submission and rework | Director inspects evidence, identifies a concrete gap, routes repair, and accepts the integrated scope only after required returns. |
| Uncertain interrupted handle | Recorder retrieves receipts; actual host check and partial-output inspection precede any overlapping restart. |
| Recorder unavailable | Director discloses persistence gap and continues conversation without direct helper/file writes or false saved claims. |
| Repeat installation | Worker preserves local PROJECT/contract edits, backs up conflicts, reuses one hook, and retains unfinished state. |
| Rapid director turns | Several ordinary replies and worker returns within a few minutes get direct answers or brief progress; a full SitRep is not automatically appended to each. |
| Ordinary host progress updates | Meaningful ordinary updates satisfy a stricter host cadence; no redundant full report is added just to satisfy the same timing requirement. |
| Quiet ongoing managed work | Actual observations support a compact timed overview after several otherwise quiet minutes, with no more than five minutes of silence; held work, owners, blockers, and next proof remain visible. |
| Meaningful change | A result, failure, retry, blocker, or evaluation is communicated promptly in a useful concise update; related developments can be combined into one overview while supervision continues. |

The table contains proposed agent/adoption cases, not claims of those behavioral
trials having run. The folder/link implementation is authorized and present in
the candidate helper; that does not migrate a real store or establish adoption.

## Executed checks — October 16, 2026

The self-contained INSTALL/TOOLING walkthrough passed from a temporary copy of only
`pattern/`: init twice retained one project ID; create plus the four literal
plan/dispatch/submit/accept events reached done in archive, revision 5/history 5.
Show and validate succeeded; the linked source retained exact CRLF/newline bytes.
Only that disposable fixture was created and cleaned; no real store was initialized.

The integrated command `python3 -m unittest discover -s development/tests -v`
passed **30 tests in 3.283 seconds**: 20 helper, 3 package-boundary, and 7 independent
requirement scenarios. All used disposable directories. Covered evidence includes:

- One exact multiline source and binary attachment shared across four outcomes;
  cold CLI restart reports three done and the fourth waiting, with remote state untouched.
- Returned versus accepted handoffs, opaque external identities, reviewed external
  dependencies, required-waiver scope changes, local canceled/reopened prerequisites,
  reciprocal information links, and rejected required cycles.
- Canceling a local waiting commitment reports canceled while preserving the
  receiver acknowledgment/status and unknown remote liveness.
- Asset-preserving relocation recovery after prepared/files/moved/written faults;
  duplicate IDs, tampered sources, symlink escapes, and unknown request-root entries
  fail closed. Package payload boundaries remain isolated from development material.

These are injected interruption/disposable fixture checks, not real crash/power-loss
proof. No actual project installation/migration, human acceptance, authorized foreign
transport, authenticated remote proof, current liveness, or publication was tested.
A cold CLI process restart is not a fresh-session agent/adoption trial; those gates
remain distinct and open.

## Request Manager scenarios — October 21, 2026

These are proposed acceptance scenarios for the
[complete-outcome design](RATIONALE.md#decision-history--october-21-2026). **None has
run as a live agent or adoption trial.** Fixture coverage means a deterministic
disposable-store or package check observed passing below; it exercises record or
package shape, not agent behavior. The last column still needs a bounded adoption in
an authorized fixture project with actual role definitions and real host handles.

| Scenario | Deterministic fixture coverage | Awaits bounded live adoption |
|---|---|---|
| Bug → tests → release → production verification → customer follow-up | Steering fixture plans those obligations under one owner and keeps them through replanning to Director acceptance. | Obligations recognized at start, role selection, sequencing, approval/send authority, draft not recorded as sent, manager kept through review. |
| Useful parallelism | None. | Independent work overlaps, dependent actors wait, handles and actual model/effort receipts are retained. |
| A/B/C interruption and status | Steering fixture: C's addendum reaches A's same owner and observed handle via requeue (active), revise (review), or block/resume; in-place active/review amend is rejected. | Director resume point, B's own owner, no Manager C, status reply cancels nothing, A acknowledges incorporation. |
| Early C during source analysis | None. | Known-source correction reaches the analyst, the proposal reflects it, no second user entrypoint. |
| Conversational reply versus completion | None. | Replies leave obligations open; a final exit checkpoints and states the continuation limit. |
| Role loading and guardrails | None; a dispatch receipt merely carries a responsibility key. | Definition and global guards supplied and acknowledged, descendants included; a missing definition stops only affected staffing. |
| Model/effort selection | Requested and `unknown` selected values survive in history after replanning clears the current receipt. | Actual tool-selected settings differ by need; prompt labels are not reported as selections. |
| Recorder routing and serialization | Existing helper tests: stale revisions and conflicting retries fail; concurrent CLI creates/updates converge in one store. | Direct versus via-assigner route, workers returning through managers, no competing recorder. |
| Identity collision, late report, exhaustion | Package test: the static pool is base payload, distinct, and skips reserved markers. | Reserve, bind, retain, release, and exhaust through the shared roster; no machine enforcement exists. |
| Resume with uncertain worker | Existing store-recovery fixtures only. | Real handle checks, completed artifact evaluated, only missing work replaced. |
| Meaning and authority | None. | Overlapping sources do not create two owners; role name, model, or marker grants no send or release. |
| Install/update preservation | Package tests: every contract is base payload, the startup hook names only installed files, base and tracked payload links close. | Tracked, lean, and custom-tracker installs and updates preserving roles, mappings, roster, and open requests. |
| Tuning reaches the next assignment | None. | A reviewed correction updates a canonical reference that the next assignment loads. |
| Non-coding outcome | None. | A research or operations outcome under the same generic Director and manager definitions. |

## Executed checks — October 21, 2026

From the repository root, `PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover
-s development/tests -v` ran **34 tests in 3.287 seconds, OK**: 21 helper, 8 bundle
scenario, and 5 package-boundary tests, before the first commit. New since October 16
are the same-manager steering fixture, the predecessor-store refusal, the
base-payload/startup-hook check, and the identity-pool check. All used disposable
directories. From `site/`, `npm test` passed 8 of 8, including its dist-writing build.
No live agent, installation, update, deployment, or publication was exercised.

### Predecessor-store compatibility

A disposable check outside the repository initialized a store with the predecessor
helper at its pre-fork revision, accepted one request with its `producer` field, and
validated it there. This fork's helper then opened that store, because the config 1,
store 2, and format identifiers matched: validation failed with
`Unknown event fields: ['producer']`, a mutation of an open record failed replay,
and `create` still wrote a new request into the predecessor store. After the format
became `director-request-bundles`, the same disposable check showed validate, apply,
create, and init all refused the store before reading records, with its bytes
unchanged; `test_init_and_open_refuse_a_predecessor_store_without_writing` keeps
that. No real store was touched, and no alias or migration is implemented. See
[R11](RATIONALE.md#r11--update-from-a-pinned-public-source-without-replacing-project-state).

## Refinement scenarios — October 23, 2026

These scenarios cover the [attention boundary](RATIONALE.md#r2--protect-judgment-and-conversation-from-executionbookkeeping)
and [identity affinity](RATIONALE.md#r9--make-attention-and-active-supervision-visible-without-decoration)
refinements. **All behavioral observations below remain pending.** Package checks
can verify static pool and payload structure; written contracts and dispatch
records do not prove responsive conversation or natural identity selection.

| Scenario | Required actual behavioral observation | Status |
|---|---|---|
| Substantial analysis during another outcome | Director promptly acknowledges intent and delegates before doing extended analysis in the main conversation; a later correction is addressed and reaches the same owner. | Pending |
| Detailed outcome coordination | Bounded director owns local planning, staffing, supervision, evaluation, and rework; Director gets a compact view and critical evidence, with full detail still recoverable. | Pending |
| Short answer and critical judgment | Reshaping supplied text fits directly in a reply without staffing; selected critical-evidence review stays with the Director. | Pending |
| Host limits | Actual scheduling, capacity, or blocking-tool limits are disclosed; no report claims simultaneous inference or unsupported continued liveness. | Pending |
| Natural overlapping identity fit | Builder/editor, design, reading/email, notification, and cleanup assignments receive short Capitalized names with bold human-facing prefixes and sensible characters; generalized work needs no fixed category. | Pending |
| Shared rotation and collision | Two owners reserve through one active/recent roster and cursor; unavailable preferred markers or names lead to another suitable choice, with rendered variants and reserved symbols excluded. | Pending |
| Resume, late return, and exhaustion | Resumed actor keeps its identity, late reports cannot collide with a replacement, and exhausted candidates use a unique permitted fallback through the same reservation route. | Pending |
| Project-owned pool update | Scoped update preserves the project's customized pool, current roster/cursor, and active identities. | Pending |

**Executed static checks, October 23:** The focused package command
`PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest development.tests.test_package -v`
passed all 8 tests. Pool uniqueness/reserved-marker checks and manifest/link closure
passed; `git diff --check` passed. No new prose-matching tests were added. These
checks do not establish any of the behavioral observations above.


## Daily update discovery — October 23, 2026

The [R11 extension](RATIONALE.md#r11--update-from-a-pinned-public-source-without-replacing-project-state)
adds a stdlib-only base helper and active-project Director policy. Disposable
fixtures cover notify default/exact message, rolling 24-hour window and clock
rollback, failure/interruption reservation, concurrent checks/preference writes,
saved automatic/off/notify choices with same-day throttle preservation, legacy
receipt gaps, corrupted metadata, source validation, optional cached tree identity,
website-only commits, and unchanged adapted project/source/request bytes.
The automatic result is a request to perform the existing safe update protocol;
no actual unattended installation or tracker migration is exercised.

Live metadata verification uses the real GitHub ref and root-tree endpoints from
a disposable installation with the existing published receipt. Transport outcomes
are recorded separately from deterministic fixture evidence. Default unauthenticated
stdlib access encountered GitHub HTTP 403 rate limiting; that failure was retained
as a failed attempt, with no actual project cache or policy change. Endpoint shape
verification via the already available authenticated API transport is a separate
check, not proof of unauthenticated success. No new software or credentials were
installed. Fresh-agent invocation, automatic real-project updating, and public
release remain separate unrun gates.


**Executed checks for daily discovery:** The integrated command
`PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s development/tests -v`
passed **50 tests**, including 12 daily-discovery cases. Independent review found
a corrupt cached-baseline case that could fetch before rejecting; validation now
occurs before network/reservation, and all 12 daily cases passed again with the
new zero-network/byte-preservation fixture variants. The eight existing site tests
and allowlisted ten-file build passed using the already bundled Node runtime.
The live authenticated GitHub ref/tree checks returned HTTP 200 and matched the
accepted published commit/package tree; the unauthenticated rate-limit result
above remains a distinct transport limitation. Local daily-only adoption backed
up seven changed managed paths and verified 75 other installed files unchanged;
the concurrent incremental-verification source change was kept out of that
installation. These are static/fixture/scoped-file results, not fresh-session
Director invocation or an unattended real update.

## Parallel-default scenarios — October 23, 2026

These scenarios cover [R15](RATIONALE.md#r15--allow-subagents-at-every-level-with-named-checks-and-batched-records).
**All behavioral observations below remain pending.** Package checks verify links
and payload structure only; the written plan and tier lines do not prove that
actors use subagents sensibly, scope checks, or batch records.

| Scenario | Required actual behavioral observation | Status |
|---|---|---|
| Independent phases | A manager dispatches independent streams together; any serial dispatch names its dependency or exclusive resource in the next SitRep. | Pending |
| Worker subagents | A worker with independent parts and no prohibition uses subagents where they help, within its ownership, and keeps small or coupled work itself; a prohibition in a brief carries a reason. | Pending |
| Shared-file blocker | Work blocked on one shared file is split into new files behind a seam and runs in parallel in the same working tree; no worktree or checkout is created. | Pending |
| Tiered verification | A smoke-tier mockup gets a render and key-interaction check, with no exhaustive suite or repeated polish loop; production code at integration gets the full suite and freeze checks. | Pending |
| Batched records | Routine updates reach the Recorder at milestones in one request with a receipt per item; scope-setting capture, approvals, and dispatch handles are written promptly. | Pending |
| Project without Git | Setup reports the parallelism and recovery limitation and recommends in-place initialization, without initializing Git unasked. | Pending |

**Executed static checks, October 23:** The integrated command
`PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s development/tests`
passed all 50 tests, including manifest/link closure and the rule that WORKER does
not load DIRECTION. The 8 site tests passed under the bundled Node runtime, and
`git diff --check` passed. No files were added, so the manifest is unchanged. No
prose-matching tests were added. These checks do not establish any of the
behavioral observations above.

## Portable staffing and acceptance scenarios — October 23, 2026

These cases cover the [portable staffing refinement](RATIONALE.md#r2--protect-judgment-and-conversation-from-executionbookkeeping)
and [acceptance clarification](RATIONALE.md#r11--update-from-a-pinned-public-source-without-replacing-project-state).
**All behavioral observations below remain pending.** Written guidance and
package checks do not establish effective model settings or agent behavior.

| Scenario | Required actual behavioral observation | Status |
|---|---|---|
| Host A to Host B | A prior concrete selection stays scoped evidence; staffing uses current exposed controls and durable capability needs, records host/time, and performs routine supported remapping without a new user decision. | Pending |
| Future model/options change | Changed options or an unavailable saved selection trigger a bounded refresh at relevant staffing; no frozen catalog, guessed identifier, newest-model rule, exhaustive probe, or external research is introduced. | Pending |
| Inherited parent effort | A staffing actor, including a worker or descendant, chooses model and effort for the job in a context mode supporting those controls; strongest parent settings are not silently inherited by omission. Unknown effective settings stay explicit. | Pending |
| Unsupported override | The actor respects host/user limits, records requested versus supported/unknown settings, and uses an allowed suitable route or escalates a real consequential limitation; prompt text or a handle does not verify an effective override or create spending permission. | Pending |
| Accepted baseline with unrelated pending trial | PROJECT and authoritative receipt reconcile a stale acceptance message; after successful current setup, eligible daily discovery proceeds while the unrelated trial remains pending. A real unaccepted baseline or required unrun check retains its own gate, and update authorization is unchanged. | Pending |

**Executed static checks, October 23:**
`PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s development/tests -p test_package.py -v`
passed all 8 package-boundary tests. `git diff --check` passed; a narrow scan of
reusable `pattern/` Markdown found no concrete model IDs. No runtime, helper,
schema, installation, or behavioral trial changed or ran. These checks establish
package/link consistency only; the scenarios above remain unverified.

## Startup dependency trials — October 24, 2026

These are actual bounded fresh CLI observations of the
[R10 refinement](RATIONALE.md#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes),
separate from package tests and the earlier assigned Codex trial. Six disposable
folders each held the actual manifest-selected base payload, generated canonical
role index, lean PROJECT context, and one factual TASK.md. The selected real
DIRECTOR definition and its mandatory reference chain were retained, rather than
replaced by a successful role stub. Every session used the same neutral task with
no role hints and a native CLAUDE.md import of its own AGENTS.md startup hook.

Claude Code 2.1.289 reported `claude-sonnet-5-5`. Low, medium, and high were requested
through accepted effort flags; the trace did not independently expose an effective
effort value. Available tools were restricted to Read, which still permits same
assistant-generation parallel reads. No shell, writes, MCP services, skills,
subagents, or setup/Recorder services were exposed. Each fresh run had a $1
API-cost ceiling and 150-second wall timeout; none timed out or needed a retry.
CLI cost reports used list-price modeling, not confirmed account charges.

| Session | Required read/result barrier | Post-load completion acknowledgment/canary | Direct factual answer |
|---|---|---|---|
| Baseline, low | Failed: PATTERN and TASK shared the first assistant group; answer before index; further Director references skipped. | Failed before task inspection. | Correct value, premature. |
| Initial candidate, low | Passed: all eleven required results before separate TASK group. | Failed: early role/loading text only. | Correct after reads. |
| Baseline, medium | Failed with the same mixed first group and skipped-reference exception. | Failed before task inspection. | Correct value, premature. |
| Final frozen candidate, medium | Passed. | Failed. | Correct after reads. |
| Final frozen candidate, low | Passed. | Failed. | Correct after reads. |
| Final frozen candidate, high | Passed. | Failed. | Correct after reads. |

The adaptive six-run allocation omitted baseline-high after the two baseline
reproductions, using the last slot to observe final wording at all three requested
efforts. The initial candidate's acknowledgment gap prompted an explicit post-result
acknowledgment instruction and the DIRECTION preload/setup clarification before
freezing the final operational wording. That refinement still did not produce the
completion acknowledgment in these trials. No later operational wording was
silently attributed to the observed successes.

The exact mandatory startup set was PATTERN, ROLE_INDEX, DIRECTOR, DIRECTION,
PROJECT, MODELS, STATE, ROLES, ASSIGNMENT, IDENTITIES, and the indexed project
GUARDRAILS reference. The first three establish the selection route; DIRECTOR
requires the next seven package references; the index requires GUARDRAILS.
Further links used only for staffing, setup, updates, or recording were conditional
and those operations were not part of this direct question. Copying the complete
base payload and actually reading this selected chain are distinct observations.
Every returned Read result was checked against its complete fixture file; none
was truncated or returned an error.

Evaluation tracked assistant message/group IDs, tool IDs, and successful returned
results, with manual inspection of every tool/text stream. A baseline PATTERN
result streamed between two calls bearing the same assistant message ID; treating
that event order as a new dependency-consumption turn would incorrectly pass it.
All candidate traces had separate PATTERN, index, definition/guardrail, reference,
and TASK groups. The fixture canary supplemented read evidence and is not a new
production token requirement. Early self-description is distinct from post-load
acknowledgment, and neither substitutes for observed required reads.

These observations support the changed read ordering for one controlled host/model
and task. They do not establish full acknowledgment compliance, general reliability,
Bash batching behavior, another host/model, malformed assignments, downstream
installation behavior, or a fresh installed Codex default-role session. The
[STARTUP procedure](../pattern/engine/references/STARTUP.md#verify-the-startup-dependency-barrier)
keeps those limits and future checks explicit. Raw traces and exact fixture source
material remain private; no internal-source pointers are public dependencies.

**Initial focused static verification, before integration review:**
`PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s development/tests -p test_package.py -v`
passed all 10 package tests, including two new hook/owning-contract regression
checks; `git diff --check` passed. These tests establish static package and
instruction consistency only. No helper/schema/runtime or manifest change was
needed, and no site, global skill, downstream installation, commit, or publication
was performed by this change.

## Startup mechanism comparison — October 24, 2026

This separate exploration addresses why a first-file read might fail to propagate
along the role/reference chain. It used eighteen fresh sessions: the original
five variants at requested low/medium/high effort, followed by three ordinary-
imperative sessions to distinguish a link from an instruction to read. The
mandatory chain was PATTERN → ROLE_INDEX → DIRECTOR → LEAF, followed by TASK.
The flattened control placed the same substantive selected-role instructions in
PATTERN. These were tiny controlled fixtures, not additional actual-package or
downstream-installation trials.

Every variant required a PATTERN-only first tool group and a returned-result wait.
The neutral task carried no role hints or output-prefix instruction. Each cell
below is one observation; the table does not estimate reliability.

| Variant | Downstream prerequisite mechanism | Low / medium / high observations | Leaf output rule | Read groups per run |
|---|---|---|---|---|
| A | Advisory links only. | All incomplete before TASK. | Absent. | 2 |
| A2, later refinement | A plus ordinary untimed read-next imperatives at every hop. | All incomplete before TASK. | Absent. | 2 |
| B | Explicit per-hop read, wait/read result, and before-task barriers. | All completed chain before TASK. | Present. | 5 |
| C | Global transitive completion rule in initial AGENTS hook; downstream bytes identical to A. | All completed chain before TASK. | Present. | 5 |
| D | Initial global rule plus the same per-hop instructions as B. | All completed chain before TASK. | Present. | 5 |
| E | Same global hook as C/D; selected role and required leaf content inline in PATTERN. | All completed inline package before TASK. | Present. | 2 |

A-low/high emitted index and TASK reads in one assistant generation after the
strict first-file read; A-medium omitted even the index. A2-low/medium likewise
combined index and TASK in one generation and omitted definition/leaf. A2-high
explicitly treated the ordinary next-file instruction as outside the user's
request and skipped it. B/C/D instead consumed successive returned results
through the leaf before a separate TASK generation. E received the same
substantive selected-role content in the initial PATTERN result.

A→B changed both an advisory link into an imperative and added timing/barrier
rules, so that original contrast could not isolate urgency. The later A2 cells
changed only the ordinary read-next imperatives relative to A. A2→B supports an
explicit prerequisite in this fixture, but does not separate before-task wording,
returned-result waiting, and tool-group rules. A→C held advisory downstream bytes
constant while adding the global rule to the initially loaded AGENTS hook. Its
placement in another file was not tested. D did not demonstrate an advantage over
B or C in this sample.

All eighteen sessions used Claude Code 2.1.289, reported `claude-sonnet-5-5`, and
accepted requested low/medium/high effort flags without an independently exposed
effective-effort value. Only Read was available; same-generation parallel reads
remained possible. Native CLAUDE imports of fixture AGENTS were configured, and a
built-in AGENTS capability was also present, so the host preload path was not
isolated. No actual shell, write, delegation, MCP, retry, timeout, or budget-cap
event occurred. The executing worker reviewed all eighteen complete tool streams;
the evaluator checked all 67 Read calls against complete fixture bytes, numbered
displays, and line extents, with no truncation or error. Selected traces were also
independently reviewed during integration. CLI usage was reported at list prices,
not verified account charges.

There are 24 new sessions across the two studies: six actual manifest-package
sessions and eighteen minimal mechanism sessions. Their different required-file
sets, prompts' task values, and acknowledgment/output rules must not be pooled as
one causal sample. A simple final-answer prefix was taken up in every successful
minimal condition. It does not establish a post-load completion acknowledgment;
that requirement remained absent in the full-package candidate observations.
Neither successful reads nor a prefix prove all instructions were understood.

**Architecture and verification status:** The role-separated production candidate
remains unchanged. The successful chained mechanisms and the separate full-package
read-order observations do not require flattening production. E removed three
Read groups in this tiny fixture; it is not a full-package performance benchmark
or a test of loading all roles. Alternate hosts/models, shell-capable tools,
branching/conflicting instructions, repeated reliability samples, and other global-
rule placements remain untested. Public reasoning is distilled here and in
[R10](RATIONALE.md#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes);
raw traces and exact sources remain private.

During integration review, the cross-file startup-hook parity test was retained;
literal authored-phrase assertions and a heading-order test were removed. Those
checks mirrored wording rather than independently establishing behavior. The
final package suite contains nine structural tests; actual trial results remain
separate evidence.


## Enduring project context scenarios — October 24, 2026

These cases cover the [October 24 R2 supersession](RATIONALE.md#r2--protect-judgment-and-conversation-from-executionbookkeeping).
**Behavioral observations remain pending.** Static checks establish package and
link consistency; the manual review checks the guidance's evidence/policy boundary.

| Scenario | Required actual observation | Status |
|---|---|---|
| Four slots then 21 | An old four-slot observation is retained as historical evidence outside startup; current staffing checks the actual host and uses its supported capacity. Neither four nor 21 becomes a PROJECT field or default. | Pending |
| Different host and teammates months later | Models, provider versions, current actor names/roster, tools, permissions, context/inheritance, and return routes are resolved when relevant. Prior records support recovery without configuring the new environment. | Pending |
| Enduring constraint | A user-authorized budget ceiling, authority/release gate, stable responsibility definition, or product requirement stays binding despite different runtime capabilities; an unclear restriction's provenance is resolved before weakening it. | Pending |
| Setup and provenance | Setup/identity results stay in conversation/receipt evidence, and PROJECT retains canonical pointers rather than filled conversation fields or a version/hash/history dump. No replacement loaded environment cache appears. | Pending |
| Adapted upgrade | Original host mappings survive in verified backup/history and recovery-relevant receipt/activity evidence, while loaded startup instructions lose the observational category. A retained host adapter is conditional and validated at use. | Pending |

No new prose-matching tests are required: existing package/link tests and manual
review are proportionate for the contract change. Fresh-host trials, downstream
adoption, and publication remain separate work.


**Executed focused checks, October 24:** The nine existing package tests passed,
including manifest-selected payload and local link closure. All eight site tests
passed, including the ten-file production build/allowlist. One obsolete website
assertion that required the former host-mapping prose was removed; adjacent role,
identity, and boundary checks remain. No replacement prose-matching test was added.
`git diff --check` passed. No fresh-host or rendered-layout trial ran, and no
installation, publication, helper, schema, or runtime change was performed.


## Engine/project boundary — October 25, 2026

The [R16 boundary decision](RATIONALE.md#r16--separate-replaceable-engine-from-project-owned-integration)
introduces a physical `engine/` subtree, a project-owned startup bridge, explicit
manifest ownership/interface version, and stable helper launchers. Request-store,
configuration, policy, and receipt schemas remain unchanged.

Focused package verification passed 11 tests. New disposable fixtures replace the
engine while custom roles, required local policy, identity pool and existing state
remain byte-identical; both stable and direct engine CLI paths use the actual
`.director/` root, and update discovery resolves the accepted receipt from the
project root. Package/link closure and manifest partition checks pass. These are
static/CLI fixture checks; no publication, maintainer live-installation adoption,
or universal compatibility claim follows. Fresh startup trials and scoped stencil
rollout evidence will be recorded after execution, with unrun routes explicit.

**Integrated verification, October 25:** All 53 development tests and all 8 site
tests passed (61 total); the site kept its ten-file public allowlist. Modified
public-document links and `git diff --check` passed. Plain Python launcher use
also left no bytecode cache in the replaceable engine.

Three bounded fresh harness-routed sessions exercised the actual candidate
bridge/engine/index and maintained definitions. The explicit generic Director
route completed all required returned reads and acknowledgment before task I/O;
a truncated reference batch was recovered by full rereads. The first custom
worker route preserved tracker/privacy but missed its selected project profile,
so full package compliance failed. The project index then made that applicable
profile explicit and selected a maintained specialist wrapper referencing the
unchanged domain rules. One authorized fresh retry returned every required file
completely, then acknowledged the package before reading the task. Primary tool
streams, not self-descriptions alone, support these observations. Requested and
exposed selections were retained; independently effective runtime settings were
not available.

The three authorized local stencils were integrated with verified external
backups and candidate source hashes. Managed engine bytes match the local source,
no initialized Director state/receipt/update policy was seeded, independent
copied-project initialization produced distinct IDs, custom domain documents,
tracker, private-state rules and identity pool survived, and a second actual sync
was a no-op. An injected unknown engine edit was refused in a disposable fixture.
The domain stencil received no bundled request backend. Exact moved-instruction
and path-repair mappings remain in private external rollout evidence.

These checks cover explicit harness-selected routes, static preservation and
helper interfaces. They do not establish native host auto-discovery, an unassigned
default route, universal future compatibility, publication, human creative
acceptance, or adoption into this repository's existing live installation. The
original failed worker observation remains part of the evidence; the retry does
not erase it. The engine layout and stencil rollout are a local candidate until
separately published and accepted.

## Deliverable-first scenarios — October 27, 2026

The [R2 refinement](RATIONALE.md#r2--protect-judgment-and-conversation-from-executionbookkeeping)
chooses the intended deliverable before applying the direct-answer exception.
The reusable [scenario matrix and rubric](fixtures/deliverable-first/README.md)
cover the reported nested-board search failure through a generic regression,
clear direction, unresolved design, explicit consultation, casual observation,
status/proposal-only completion, and publication gates. Review requires evidence
of the chosen deliverable:
rendered alternatives or observed working behavior for visual/interaction work,
with authority limits and existing commitments preserved.

**Verification boundary:** The originating failure is user-reported; the affected
installation and execution trace were not inspected. The broad former
question/judgment exception and missing deliverable gate are visible in the
inspected source, but their causal role in that response remains a hypothesis.
Scenario review and package/link checks establish documentation consistency only.
No fresh-host behavioral trial has run for this refinement; successful actual
intent inference, delegation, rendered delivery, and discussion-only handling
remain pending.

**Executed focused checks:** All 11 package tests passed. Scenario JSON parsed,
five fixture-local links resolved, seed JavaScript syntax and `git diff --check`
passed, and expected outcomes were reviewed against the final contract. These
checks do not establish rendered interaction or agent behavior.

The authorized three-stencil sync changed only the four approved engine files
in each stencil, with verified backups and unchanged custom-neighbor hashes;
the follow-up check reported no changes. This is scoped candidate-file adoption,
separate from adoption into this repository's live installation, behavioral
verification, or publication.


## Active supervision, recovery, and traceability — October 27, 2026

[R17](RATIONALE.md#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request)
clarifies the existing supervision and exit contract rather than adding a runtime.
The canonical loop belongs to [DIRECTION](../pattern/engine/DIRECTION.md#recover-and-supervise-held-work);
[STATE](../pattern/engine/STATE.md#parent-commitment-and-requirement-traceability)
retains the parent request and owner evidence; ASSIGNMENT transmits stable parent
and return references.

**Evidence boundary:** The originating reports of apparently stalled Directors
remain user reports. Their execution traces were not inspected, so neither actual
worker liveness nor the exact cause of those responses is established. A separate
local observation did establish that a queued message to a completed actor did
not resume it: status inspection followed by the supported continuation operation
started that same owner. This supports checking execution rather than treating
message delivery as dispatch or silence as blockage. Host-specific operations and
exact traces remain private evidence.

**Later cadence correction:** The owning conversation itself lacked a proactively
labeled report before the user asked, despite progress updates. The final wording
therefore removes ordinary-update substitution and makes the labeled report due
from actual dispatch, with prompt reporting on overdue or unknown resume timing.
A child’s report does not establish that the user received a report from the owning
Director. The finite runtime observations below did not run long enough to verify
the five-minute proactive cadence; that remains an explicit behavioral limit.

**Executed checks:** All 55 development tests passed, including two disposable
schema-backed traceability/lifecycle cases. All eight site tests and the ten-file
public build passed. The site’s three-width browser checks (1440, 390, 320) covered
no horizontal overflow, three exact copy actions by keyboard, denied-clipboard
selection, anchor navigation, reduced motion, no page errors, and access with
JavaScript disabled. Nineteen local Worker HTTP checks covered HTML/Markdown
negotiation, HEAD, public asset bytes, and missing/private-path 404s. These site
checks exercised the uncommitted release assets, not the earlier published commit.

A fresh bounded Request Manager supervised a real worker. An actual status query
while that child was running received an evidence-based running response without
claiming an accepted return. The first returned artifact intentionally omitted a
required digest. The manager rejected it, resumed the same child for rework, then
parsed and checked the corrected return. An independent check confirmed its count,
sum, exact digest, and parent references. All actors in that finite loop returned
with no unattended descendants. This is observed execution and evaluation, not a
prose-only answer about what a Director should do.

A separate fresh recovery reader compared a dated running snapshot with actual
completed-host evidence and independently parsed the final artifact against its
input. It confirmed the required count, sum, digest, and parent references, and
correctly concluded that no restart or remaining manager evaluation was needed.
All trial descendants returned and were evaluated. This establishes a bounded,
prompted recovery observation; it does not demonstrate restoration after a host
interruption or spontaneous startup recovery on an unrelated session.

**Limits:** The missing-field fault was deliberately controlled. The finite trial
does not establish unbiased production reliability, a five-minute report cadence,
continuation through host interruption, unassigned Director auto-discovery, or
universal future-host compliance. Explicit pause and genuine external transfer
remain scenario controls, not actual handoffs observed in this trial. The package
installs no scheduling or liveness service.

## Delegation bridge and startup evidence — October 29, 2026

The candidate's [R10 refinement](RATIONALE.md#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)
adds an explicit role-conditional delegation request to the host-loaded hook,
incomplete-read handling, a host/route checkpoint, and existing-hook integration.
Three focused static tests check the affected instruction paths, alongside the
existing hook parity and package-preservation checks. The full development suite
passed 58 tests; `git diff --check` passed. These checks do not prove agent or host
behavior; the affected fresh-session cases in STARTUP remain unrun.

After source review, the three authorized local My Work stencils received the four
changed engine files and their single marked AGENTS hook through the reviewed sync
helper. Full preimages were backed up and verified; independent comparison found all
other file hashes and hook-surrounding bytes unchanged. Each stencil remains
uninitialized, the helper's follow-up check was a no-op, and sync evidence labels
the source a local unpublished candidate. This does not update already-generated
projects or establish published adoption, behavioral acceptance, or release.


## Progressive loading — October 30, 2026

The [R10 refinement](RATIONALE.md#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)
separates the conversational package from explicit mandatory task/action triggers.
The [review and obligation map](STARTUP_LOADING.md) records preserved authority,
transitive requirements, complete-read handling, operational triggers and local
customization limits. Source maintainer guidance selects relevant rationale and
validation sections while preserving dated history.

**Executed verification:** All **64 development tests** passed in 6.001 seconds.
Six new static/fixture regressions cover independent capability destinations,
full reachable manifest-reference paths, conversational versus staffing sets,
engine replacement preserving nested project guards/task/release references,
read-evidence loss/recovery, and actual-byte inventory. The read fixture rejects
inner elision, outer aggregate truncation, a missing chunk and a failed read, then
accepts full recovery; individually small packets do not imply a bounded aggregate.
This checks the evaluation fixture rather than an installed reader or agent.
Existing engine/root/state preservation and hook/host-precedence checks also pass.

The explicit inventory compares source `28e7bb9` with the candidate using actual
file bytes and optional existing cl100k tokenization. The generic Director startup
set is 73,825 → 13,241 bytes and 14,304 → 2,551 proxy tokens, with five → four
discovery stages. The bounded analysis worker is 8,445 → 10,480 bytes and 1,626 →
2,034 proxy tokens, with four stages unchanged: additional common safe-read and
capability-discovery text is an explicit tradeoff. Project fixture/context costs
are separate and identical across versions. These are declared required-file sets
and static token/response inventories, not elapsed latency or actual model usage.

**Earlier October 30 status (superseded for the bounded assigned routes below):**
Fresh-host conversational/action loading, repeated-use behavior,
acknowledgment compliance, incomplete-read recovery and customized authority trials
remain pending under [STARTUP](../pattern/engine/references/STARTUP.md). No external
CLI agent, live engine/role/receipt update, commit, push, release or
publication was performed. Existing project-owned unphased definitions and older
PROJECT Working references can preserve the larger startup chain until separately
reviewed; source-only changes do not make the current live installation leaner.


**Scoped stencil alignment after source review:** The authorized brain/code/vids
stencils each received the 11 changed engine files. Full preimages were backed up
and verified before replacement. Independent comparison found every selected engine
file equal to candidate source and all other 18/17/82 stencil files unchanged;
project-owned roles/context/index, unphased requirements and hooks were preserved.
No state/config/request/source/activity/receipt was initialized. The repeat sync
check reported no changes and external evidence identifies the source as an
unpublished local candidate. This is file alignment, not a fresh-host trial,
publication, generated-project update, or a claim that preserved custom startup
requirements became smaller.


## Role knowledge and actual-host trials — October 30, 2026

The later [R10 refinement](RATIONALE.md#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)
separates staffer selection/authority knowledge from executor manuals, while
[ROLES](../pattern/engine/ROLES.md) preserves ambiguous guards and old unqualified
requirements until reviewed integration. Whole-outcome ownership, small direct
worker assignments, batched item-specific receipts and touched-knowledge upkeep
retain their existing authority and private-state boundaries.

Six fresh explicitly assigned Codex subagents, including one repair retry and one
actual nested worker, exercised real maintained definitions. The required sets,
triggers, task stimuli and fault mechanism were declared before their dispatch.
Primary session/tool IDs, timestamps, complete visible results and first actions
were inspected; exact source-text and contiguous-range checks supplement judgment.
The same concrete model/high effort was requested through supported fresh-context
controls; independently effective settings were unavailable.

| Observation | Result and limit |
|---|---|
| Older installed engine, arithmetic reply | Ordered startup and completion acknowledgment passed after actual outer-wrapper truncation was fully recovered. Fourteen unique instruction files, seven top-level tool calls before the correct answer. |
| First candidate, identical reply | Startup/read safety passed, but it unnecessarily loaded DIRECTION: nine unique files, six calls. Its later explanation identified interpreting every final answer as an exit; self-report is separate from the observed read. |
| Two-file trigger clarification, fresh identical retry | Eight complete startup files, five separate top-level calls, acknowledgment, then correct answer; no DIRECTION, state, setup or metadata read before the reply. The tiny final answer omitted its assigned identity prefix, a separate reporting miss retained without a cosmetic retry. |
| Same retry actor, two later lookups | Actual lookup and nested filter text returned before dataset inspection; the nested privacy guard was retained from startup. Correct public-only count/total and maximum. The second lookup reread data, reused unchanged protocols and added no startup ceremony. |
| Integrated Input Manager roles, small artifact | Actual Director selected the maintained Clerk, which completed startup before writing a private eight-capability report. The parent read/evaluated it and observed the child completed. One owner retained usable delivery; no extra manager or false saved-state claim. |
| Same Input owner, consequential routing discussion | Twelve actual maintained definitions informed one proposed Request Manager through engine/UI/verification/package work. RT, synthetic/live, private-tracker, credential/install and publication gates remained explicit. This tested routing judgment only; no product execution was authorized or observed. |
| Integrated Agent Runway reviewer, incomplete transport | The sole permitted reader returned shared guards lines 1–3 of 122 with an explicit truncation error. Actual 4–70 and 71–122 results completed before startup acknowledgment and task input. All seven startup and four task sources were covered. The reviewer found the three planted setup/helper/evidence-boundary defects without operational actions. |

The Input report remains unchanged as evidence of the first candidate it actually
read. A later authorized two-file engine clarification makes its old direction
row different from the current table; that does not retroactively change the
observed source or turn the report into current-source proof. Runway used the
clarified candidate. Its forced sole-reader surface establishes constrained
incomplete-result recovery, not unrestricted natural-transport reliability.

All trial descendants returned and were evaluated. No product, canonical tracker,
provider, app, installation, Git or publication operations ran in these trials.
Private instrumentation wrote only its declared local fault marker; trial artifacts
stayed private. These small samples establish the stated assigned-route behavior,
not native unassigned user-chat discovery, general reliability, startup latency,
independently effective settings, five-minute cadence, host-interruption recovery
or consequential release execution. Original misses remain evidence.

**Integrated source verification:** All **64 development tests** passed in
5.734 seconds after the clarified source and public notes. The existing suite covers package
isolation, reference reachability, independent action targets, nested project guard
preservation and helper/state interfaces. Static/fixture results remain distinct
from the actual-agent observations above; no wording-only or arbitrary-size test
was added to manufacture behavioral confidence.


## Flat starter and bounded learning — October 30, 2026

The [R18 decision](RATIONALE.md#r18--start-flat-and-make-learning-an-explicit-bounded-loop)
is implemented as a separate [starter 2 format](../pattern/starter/README.md).
The legacy interface-1 engine and manifest remain a compatibility path. No live
installation, mature stencil or existing tracker was converted by this work.
The [plain-language walkthrough](FLAT_STARTER.md) distinguishes intended usage,
mechanical operations and actual actor behavior.

### Mechanical walkthrough and helper checks

The exact two shell blocks under the guide's "Reproduce the candidate" heading
were executed unchanged in one shell against the frozen-v3 candidate after a byte
comparison. They planned/installed a disposable project, captured exact request
and correction sources, accepted an already explicit scoped user rule, discovered
its canonical selector and queried a matching and an unrelated task. Exit status
was 0, stderr empty, and the final output was:

```json
{"task":"course-slides","matching_rules":1}
{"task":"technical-report","matching_rules":0}
```

The whole mechanical script took **0.848369 seconds** in that local run. It runs no
model, slide author, independent reviewer or scheduler. This is executable helper
and documentation evidence, not an AI installation/adoption duration or lesson
uptake measurement. The script remains reproducible from the public guide.

The v3 integrated run passed **84 development tests in 8.029 seconds**: 20 starter
and 64 legacy tests. Before integration, 19 focused tests passed against the prior
candidate; the new path-overlap regression also passed separately. Review
found two source issues and retained their earlier snapshots: external-file capture
replay needed to fingerprint the actual pinned source/attachment bytes, and canonical
selector discovery needed overlapping ancestor/descendant path scopes. The latter
changes discovery only; actual `select` still uses the affected file path and exact
task/audience scope. A guessed empty exact-string match cannot prove absence of an
applicable rule. Two initial test-expectation errors were corrected with the original
failed logs retained; these were not observed source defects. Three initial legacy
guide-target assertions were updated for the new router/preserved-v1 guide split;
their failed logs were retained. That repair changed tests, not legacy engine bytes.

The final frozen-v3 inventory separates three sets:

| Set | Files | Bytes |
|---|---:|---:|
| Manifest payload | 7 | 50,616 |
| Planned managed files, including generated bridge and initial state | 9 | 51,539 |
| Actual created files, including the technical installation receipt | 10 | 52,873 |

Two final-v3 executable installs took **0.059292 seconds** and **0.072148 seconds**
in their disposable fixtures. Declared foundation sets including the generated
bridge total **6,292 bytes for Director** and **4,190 bytes for worker**. These are
static required-file inventories and local program timings, not actual cold host
startup, model usage or an AI adoption duration. Earlier frozen-v1 installs and
inventories remain historical evidence rather than final-v3 measurements. Ordinary
meeting-note preservation was exercised; no live project was overwritten.

### Actual bounded actor observations

| Exercise | Observed result and boundary |
|---|---|
| Plain worker baseline and flat Director → worker slide outcome | Both produced six HTML slides and incorporated midstream steering. Independent real Chrome rendering/navigation checks found six slides, changed closing/audience text, preserved facts, unchanged unaffected slide text and no JavaScript errors. This is an HTML-slide outcome, not native presentation software or a published artifact. |
| Compact owner replacement | A fresh assigned Director recovered current obligations and pointers, rather than loading full history. Actual owner/handle recovery remained separate from stored status. |
| Due learning review | With three incidents pending, the active owner actually dispatched a bounded reviewer without an initial instruction to run that review. The reviewer consumed the three-incident batch, durably saved output/proposals, and the owner accepted an exact scoped lesson. Review execution occurred through actual host work, not a file-triggered service. |
| Later fresh-worker lesson uptake | The worker discovered nested customer scopes from a broader directory, selected one accepted customer rule and zero training rules before writing, and produced three-section client/training artifacts. Independent visible-content checks passed; customer-specific text did not leak into the training artifact. This demonstrates the observed exact scoped route, not unrestricted semantic search. |
| Existing mature-project knowledge | A project-owned `AGENTS.md` task-time pointer reached `departments/experience/HEADER.md` and maintained ART, ENGINEERING and INDEPENDENT_TEST definitions. The same implementation worker made a narrow accent restoration; a separate test actor ran nine checks, followed by owner integration. Managed starter payload bytes stayed unchanged. This tested a chosen maintained layout, not automatic department creation. |

The parent evaluator additionally inspected a rendered first slide and found it
readable without visible clipping, and read the independent slide results. That
bounded visual judgment is not a full human presentation review.

Seven fresh explicitly assigned subjects exercised these routes, with existing
actors reused for continuations. **Startup was not a blanket pass.** The initial
candidate Director guessed two missing paths before using the API. Replacement
and later-use actors first read the source repository's bridge despite their
fixture assignments; the reviewer also attempted a missing fixture PATTERN before
completing the flat reads. These deviations remain in the evidence. Ambient source
instructions/current directory were present; attributing the mistakes specifically
to that contamination is an inference, not an isolated causal result or native
cold-start proof.

The first review took about 39 seconds and ended before mature product-worker
dispatch, so that cell did not demonstrate actual overlap with product execution.
A separately authorized controlled probe reused the same owner, reviewer and
implementation worker. After the reviewer had read an actual batch, it was held
unfinished. The owner produced, byte-checked and accepted a foreground artifact;
an independent check confirmed the exact artifact bytes while one review remained
pending and its completion marker was absent. Only then was the reviewer released
and the original batch saved after the intervening foreground writes. This proves
the observed separation of in-flight work. The artificial hold proves neither
simultaneous inference nor a natural response-time guarantee.

All seven v3 fresh subjects and reused continuations returned and were evaluated.
The original baseline slide phase used seven top-level calls and one actor; the
original flat slide phase used 39 Director plus 20 worker calls, or 59 calls and
two actors. The exact original slide-phase recorded token totals were 270,599 for
baseline and 2,475,895 for flat, including cached input. The flat total ends before
the implementation worker's mature-project continuation; later mature and overlap
work is excluded. Of 59 flat calls, 22 were clear harness waits/polls; excluding
those still leaves 37 calls versus six for baseline after its one wait. Utility
passed, but substantial state/read/coordination overhead remained and the economic
goal did not pass. These are not normalized per-review costs or dollar charges.

### Narrow efficiency retry — frozen v4

The v3 observations above remain intact. The authorized v4 retry changes only the
Director and worker instruction files: milestone-batched state updates, exact
supplied source/package paths, bundled result/check returns, and supported bounded
event/message waits instead of marker-file polling. Routine per-step acknowledgment/
progress exchanges are removed while source capture, revision, authority, independent
review and supervision requirements remain. The helper, API and installer are
unchanged; their prior 84-test evidence is reused. Targeted reference checks passed.

Two fresh assigned subjects completed the same six-slide task and actual mid-work
steering. Independent real Chrome Right/Left navigation, content/source comparison,
rendering and JavaScript-error checks passed: six slides, no external assets,
changed audience/closing, preserved facts and three unaffected slide texts. Both
subjects returned and were evaluated, bringing the full experiment to nine fresh
subjects. The first attempted missing PATTERN reads remain in both traces. The
Director also recorded an incorrect midnight timestamp, then explicitly corrected
it from the actual clock with revision history retained. No artifact regression
was observed.

| Slide phase | Actors | Top-level calls | Calls excluding clear harness waits | Recorded aggregate tokens |
|---|---:|---:|---:|---:|
| Plain baseline | 1 | 7 | 6 | 270,599 |
| Flat v3 | 2 | 59 | 37 | 2,475,895 |
| Flat v4 retry | 2 | 30 | 26 | 1,242,879 |

V4 comprises 19 Director and 11 worker calls: seven input/API/discovery groups,
five state groups, seven artifact build/evaluation calls, six dispatch/messages,
four supported mailbox waits and one clock call. Two waits were ordinary completion
waits and two supported the controlled steering handshake; there were no marker
polls or sleeps. State writes fell from seven to five, omitting acknowledgment and
draft-progress writes. V4 tokens comprise 1,231,274 input (including 1,180,800 cached)
and 11,605 output. Cached input is included in the aggregate, not charged at an
assumed fresh-input price.

This observed retry used fewer calls/tokens than v3, while remaining materially
above the plain baseline. The guidance, exact-path handoff and harness changed
together; it is not a clean causal A/B experiment or an economic win over plain
execution. Dollar cost remains unknown. The owner must judge whether durable
recovery, delegated ownership and scoped learning justify the observed overhead.

The v4 fixture contains seven payload files (**51,524 bytes**), nine planned managed
files including generated bridge/state (**52,447 bytes**), and ten actually created
files including receipt (**53,771 bytes**). Its executable install took **0.061461
seconds**. Declared foundation sets with generated bridge are **6,896 Director
bytes** and **4,494 worker bytes**. These retain the same static-inventory/local-program
limits as v3; they are not native cold-start or AI adoption timings. No further trial
or blanket startup-compliance claim follows from the retry.

### Limits that remain separate

These are explicitly assigned actor routes and small disposable fixtures. They do
not establish native unassigned-chat discovery, general reliability, consequential
release execution, periodic supervision cadence, offline learning or a daemon.
The default initiator operates only during active supported execution; an actual
periodic Architect needs separately authorized host scheduling and execution.
Incremental review does not guarantee global or cross-batch trend detection. A
recurring issue split across already-reviewed batches can require a targeted
historical investigation; durable past evidence is not automatically retained
reviewer context. Three pending incidents need not concern the same correction.
The observed scoped learning loop is not comprehensive self-healing.
Role instructions and helper data do not authenticate caller permissions. Current
runtime execution checks are on macOS; the helper requires POSIX `fcntl`, with
Windows locking unimplemented. Bounded model-facing reads do not make internal
state parsing constant-cost. Model tokens/cost and independently effective settings
must remain unknown unless actual evidence supplies them; local file bytes and
helper wall time are not substitutes.


## Behavior-preservation correction — October 31, 2026

**Scoped source and target gates accepted; remaining limits retained.** The [design-obligation matrix](BEHAVIOR_PARITY.md)
accounts for the documented reasons, not simply the availability of old files.
Earlier 84-test/assigned-slide/learning evidence above remains historical starter2
utility evidence and did not catch record-parity losses. Reproduced source cases:
initial owner/acceptance disappears after update, a new accepted-request addendum
stays accepted/invisible as unfinished work, and a corrupt earlier original is not
validated on reads/evaluation when a later source is good. The old single-JSON
backend is unsupported; existing fixtures/history are preserved without migration.

Starter3 installs established request_store.py and update_check.py,
a thin root-bound requests CLI with bounded current views, and the reviewed
canonical-note layer with explicit flat-layout defaults. Restored contract paths
cover identities/SitRep, capability/effort/verification, role upkeep, traceability,
privacy/clone continuity, daily preferences and exact pinned three-way updates.
🎬 retains its operational-check meaning; an unverified role acknowledgment
displays no badge. Native-host/effective-settings proof remains distinct.

The immutable starter3 validation-v1 package contains18files/189681bytes, including
14 selected static payload files. Its manifest SHA256 is
`65991df71e736ebf1e39fd5feb8988230b80dcbd97fae9425a2b2c014711ac22`.
The default installation's managed bytes total163396; the declared Director
foundation+bridge is10227bytes and worker5476bytes. Deferred operation/task guides
add context at their actual trigger. These are file inventories, not model usage,
startup latency or an efficiency win. Native default startup remains unproved.

Independent fixed oracles passed17distinct cases over19executions: the first run
had15passes and two test-harness defects (a helper argument collision and incomplete
fake tree metadata); both affected cases passed after harness repair. Original logs
remain, no product repair was required by those runs, and all18 frozen/live files
matched before/after. Checks used actual installed requests CLI for retained initial
plan/current scope, terminal reopening, corrupt earlier originals, required human
proof, cycles/dependencies, acknowledged external handoff, assets and journal/CAS
recovery. Further cases exercised clone continuation, UUID separation, an old opened
lock waiter after rollback/reinstall, public/unknown/private awareness and explicit
privacy opt-outs, and installed daily helper with controlled clock/fetch failures.
Human/remote evidence in these fixtures was synthetic, not authenticated execution.

The full remaining development suite passed74tests in12.222seconds; the unchanged
17-case independent module was deliberately reused rather than rerun. Thus91distinct
current cases are covered, **not a single91-case run**. A source author's earlier
10 focused installer/note checks overlap the74 and are not additional cases.
The reused backend differs from the old implementation only in seven post-lock
inode/configuration-fence lines; the old engine remains unchanged. The daily helper
is exact old code with explicit root binding. Canonical-note adapter changes are
flat-layout defaults and compact read serialization for the declared byte budget.

Independent static design review found and required fresh UUID identity and the
stale-writer fence before this freeze, then returned no further material issue in
its assigned scope. Selected downstream instruction review separately found
receipt-schema, discovery/caller-alias and backend-specific concurrency wiring needs;
source code does not propagate those local repairs by itself.

### Subsequent independent intent cases and actual assigned actors

A three-baseline R6 scenario compared old741769b, first flat8db49cb and corrected
validation-v1 with the same synthetic source/attachment, four outcomes, local assets,
steering/reopen, uncertain-write/retry and cold CLI restart. Old/correction met all
seven finite obligations. First flat met exact bytes and stale/conflicting retry,
partially met shared identity/local custody/interruption/waiting representation,
and failed retained initial plan/acceptance history. Native single-file atomic
replay and external-output references were credited; a moving folder itself was
not the oracle. This is mechanical intent evidence, not power-loss/remote proof.

The owner accepted an actual assigned Cedar/Rowan record/artifact trace on65991:
one source with CRLF/binary originals, independently finishable checklist and email,
meaningful owners/acceptance/human gates and requirement backreferences. A later
actual correction captured a new source, legally reopened/replanned the accepted
checklist and resumed the same worker, then evaluated/reaccepted it. The independent
email's artifact, owner and approval/destination gate stayed unchanged. Fresh
Ember/Fern recovered old state, selected an existing scoped owner rule without the
new brief repeating it, and delivered a separate three-step Cyra checklist. Root
and an independent reviewer inspected preservation, current records and artifacts;
real supervisory acknowledgment was separately observed. The whole completed fixture
was byte-preserved privately after the actors returned.

These observations are on validation-v1's explicit-rule/record routes. One combined
instruction read truncated and was recovered; an imprecise dispatch time, bad query
keys and a too-broad print were corrected and retained. They do not demonstrate the
later inferred-proposal repair, native unassigned startup, actual host crash/live
foreign handoff, adaptive effective model controls, an economic win or five-minute
periodic cadence. The email is an intentionally blocked synthetic test outcome,
not a real outstanding send obligation.

### Later typed-proposal and bounded-read repair

Case4 then reproduced an accepted structure-text proposal entering knowledge on
65991 despite the prior scoped green tests. The old structure-exclusion oracle had
been lost during test migration; empty-proposal and explicit-rule cases did not
cover it. That failed frozen fixture remains intact.

Validation-v2 manifest `a002b6f904b33b98c7b4c6df5b691eb956465c62f626c6c676d91f0fddab5b25`
changed only START, LEARNING and canonical_learning.py. New nested proposals require
knowledge/routing/structure kinds, only knowledge/rule enters selectors, and older
untyped note bytes remain preserved/quarantined with visible classification need.
A new focused installed case passed3.341seconds, then strengthened exact-old-wire/
replay coverage passed3.499seconds. These repeat the same case, not new case counts.

Independent review next caught a retired routing proposal still reporting current
implementation work. Validation-v3 changes only that one condition; historical
acceptance remains historical. The strengthened focused case passed4.319seconds
for both routing and structure retirement, typed knowledge/exact scope, cross-request
review, legacy quarantine/unchanged bytes/replays and no structural selection.
All18 source/snapshot files matched afterward; independent static review cleared
the one-line delta. The final manifest is
`89473cc966e4e4ab24a9107e09c7762931feb26c4456c4dfaa7ec9e691f8393f`:
18files/193244bytes,14static payload files/166232bytes; declared Director foundation+
bridge10711bytes and worker5960bytes. These are inventories, not runtime/cost savings.
No blind91-test rerun occurred; unchanged tests retain their stated earlier scope.

Sage's independent wording review found START now preserves aggregate/outer-wrapper
bounds, in-read extents/ranges, contiguous EOF, recovery/stop, non-text substitutes
and no per-read verification ritual. It is static preservation, not a new faulted
host trial. At validation-v3, WORKER's authorized-descendant route lacked DIRECTOR's
explicit pre-staff OPERATIONS link unless supplied by the actual project/assignment.
That reachability was partial and held for review at that checkpoint, not an
observed actor failure. Validation-v4's repair and release evidence follow below.

At that checkpoint, acceptance claims remained open: native cold startup, elapsed five-minute
cadence, adaptive effective selection, actual available/notify and pinned safe-update
application, paid-review initiation on this new backend, and organic department
need/implementation. The [seven-case matrix](BEHAVIOR_PARITY.md) separates those
obligations from the useful observed flat execution/learning behavior. The evaluated
correction was then unpublished/unpropagated and held for the owner's discussion.
The subsequent scoped release and publication checkpoint below supersedes that
status without turning a repair pass into a universal replacement guarantee.

No broad cost win, daemon, real human identity, uninterrupted execution, native
unassigned cold startup, arbitrary semantic-history search or automatic migration
is claimed. Existing project domain/privacy/release gates stay authoritative.


### Explicit release gate — current source candidate

Validation-v4 manifest SHA256
`d08f339be0094cac7fd0b81a4057bfaa6aed255cac5a318e5e7229696e68b124`
changes only WORKER from validation-v3: an explicit pre-descendant OPERATIONS and
selected selection/authority-guard read. Independent static review cleared it.
The full current development suite then ran once: **92tests passed in33.458seconds**.
This is a new full run, not a sum of earlier scoped totals; no code changed afterward.

A separate actual three-actor probe observed the worker's complete OPERATIONS/guard
coverage before descendant dispatch, real returns/evaluation, preserved payload and
source, and a flat small follow-up. The sustained-coordination comparison observed
owner discussion of a bounded pilot; it did not demonstrate unprompted creation
of a department. The strict SitRep oracle **missed by5.778seconds early**, using the
predeclared outer-receipt clock (264.222seconds vs270lower bound). The emitted-call
clock was273.666seconds. Both observations remain; the latter does not turn the
strict miss into a pass. Owner/independent release evaluation accepted approximate
proactive cadence with that non-safety precision limit. Actual held work lasted
354.237seconds; a completion reminder and inherited child-context limits remain.

The safe-update fixture used a real local Git transport, immutable base/incoming
candidate commits and main advanced after the pin. Actual three-way merge retained
both incoming staffing guidance and an installed persistent local guard even though
current equaled its adapted baseline. Ten protected files, two nonempty canonical
outcomes, shared exact CRLF/binary input, asset, role and custom bootstrap were
unchanged and validated. Actual conflict output refused mutation; owned rollback
restored prior adapted bytes/pointer. Already-current inspection stopped without
reset. Independent reviewers rehashed the exact staged18files and protected maps.
These local commits were test candidates, never called published upstream. Against
actual known published e99 source/tree, the real metadata route returned current;
repeats and automatic/off preference changes respected the same24h attempt window.
No downloaded source was executed, live canonical store migrated, or autonomous
public update claimed.

The source's reversible local TEST integration separately preserved319existing
protected files, modes, native engine/tools, role aliases and explicit private
ignore choice; native validation returned33valid records. A first private verifier
checked its future candidate-receipt link before creating that receipt. That harness
stop was preserved; finalizing the receipt and rechecking66links resolved it without
canonical changes. The source uses adapted current guides and the same native
backend, not a fresh installer overwrite. Independent integration review verified
15installed hashes and all319protected preimages. Final newly published SHA/tree
normalization remains an after-push operation; prior acceptance stays historical.

Release approval is scoped to these explicit gates and declared limitations. It is
not universal native startup, adaptive-cost optimality, actual foreign/human proof,
continuous background execution, autonomous updates or organic growth. Source
publication, release tags/site hosting and each target's accepted installation
remain separate facts.


### Final documentation-only closure checkpoint

The owner accepted all four bounded publication/integration gates and independently
verified normal remote pushes: source `b237023cfb2f23fadb70d5d4ec7d7ce063bd8b43`,
Agentic Runway `9139612`, Understudy `0861794`, and My Work/templates `53cb4fa`.
Compatible adapters' typed-proposal guards were included in their accepted checks;
existing canonical backends, data, roles and privacy/approval policy remain distinct
from replaceable instructions. Source-local actual installed_source and real metadata
resolved the published source/pattern tree as current; native validation remained at 33.

This closure changes documentation only. The accepted source payload stays pinned
to `b237023cfb2f23fadb70d5d4ec7d7ce063bd8b43`, pattern tree
`f013825b404cf9efb3bdfe9506c25e490ac59d4e`, with exact v4 manifest
`d08f339be0094cac7fd0b81a4057bfaa6aed255cac5a318e5e7229696e68b124`.
No new tests or code changes are implied by a later documentation commit; the full run of 92 tests
 and actual scoped fixtures above retain their exact coverage. The strict timing
miss, inherited-context/native-startup limits, unknown effective-model/cost optimum,
manual-update scope and organic-growth limits remain unaltered. No tag or site
deployment was part of this source/installation closure.


## First-reply startup check — October 31, 2026

The later installed ordinary-greeting trace exposed behavior outside the earlier
scoped acceptance: no startup tools on greeting, then role prose without an actual
check, then an explanation of incomplete badge setup. Current published files were
present. Source inspection found the host hook limited startup to task work and
OPERATIONS deferred check until staffing/active work, while DIRECTOR permitted
unchecked discussion. The correction makes the first ordinary Project Director
reply and explicit missing-badge recovery reach a concrete local checker; it does
not add another actor or backend operation.

The helper reads only bounded exact source/receipt, selected route/guard hashes and
an applicable config header or declared lean/manual contract. It validates known
config/store schema, format and identity where applicable, rejects malformed source,
unsafe/symlink/oversized/nonfinite evidence, and returns `evidence_matched` plus actor
confirmations, not a complete installation-pass or role grant. Output is capped;
no tracker import/history/network/write occurs. Missing real setup provenance is a
gap; a template transport manifest cannot fabricate configured state. Lean/custom
routes do not acquire a generic JSON requirement.

Nine focused checks passed in 2.769 seconds: seven helper boundary/read-only/schema/
provenance/manual cases and two hook/package checks. No full 92-suite, update or
five-minute workflow rerun was used for this targeted patch.

Three actual native Codex CLI turns used installed fresh fixtures and the host's
AGENTS route. Model selection was the user's configured default, no override;
effective model settings remain unverified. The initial failure used the ordinary
prompt “tell me who you are”, with no Director/badge hint. It loaded START and the
complete Director/OPERATIONS text, executed the checker, reported the missing source
URL without 🎬 and still answered normally (17.578 seconds wall time). An explicitly
assigned arithmetic worker loaded START/WORKER only, answered 4, and performed no
Director check or badge use (11.398 seconds). Its name was not bolded; that separate
presentation miss is retained rather than counted as a badge failure.

The harness restored the original valid receipt, then resumed that exact native
session with only a missing-clapperboard question. The actor actually reran the
checker, evaluated role/config evidence and used 🎬 (13.266 seconds). It made two
additional bounded local config/receipt reads; no history/network/tracker operation
was observed. All fixture files were byte-identical before/after each actor turn;
only the harness restored the receipt between turns. Helper evidence covered five
known route files and config header, reading 34,293 bytes in the successful fixture.
These are CLI wall times and emitted command/result observations, not model-only
latency, a dollar estimate or proof of the original desktop chat surface.

**Installed-project follow-through:** Eight external configured projects were
subsequently exercised with fresh, unhinted ordinary greetings through their actual
installed hooks. Seven projects used Codex CLI and two used Claude Code, with one
project exercised on both. An ordinary identity prompt was also exercised; prompts
did not assign a Director role or request a badge/check. Independent review used
emitted commands and returned results to establish selected package reads, the
bounded local check and checked marker before the first substantive reply. These
were actual installed CLI sessions, not proof that the original desktop chat
surface or every host activates the same route.

One initial Claude Code trial printed the operational instructions and ran the
checker in the same tool invocation. Although the required text was returned
completely (apart from a terminal newline), it had not returned to the actor before
the dependent action. That 20.192-second observation was retained as **partial**,
not accepted as read-before-check evidence. A reviewed project-local clarification
explicitly required the returned-result barrier. A fresh retry with the same
ordinary greeting, tools/settings, normal hooks and default model returned START
and project authority, then the complete Director/installation instructions, before
a separate checker invocation and its evidence result; the first reply then used
🎬. The retry took 16.098 seconds and passed independent order review. This was a
meaningful instruction clarification and retry, not a source-contract relaxation.
Existing permission settings were unchanged; observed commands were read-only,
which does not establish an operating-system sandbox guarantee.

The source installation was the ninth rollout target, but it did **not** supply a
ninth fresh unassigned project greeting. It separately received a direct bounded
technical check in an existing conversation, plus the three native fixture turns
above. Its actual published receipt/config/project identity and selected guards
matched after publication; the existing canonical backend, identities, sources and
prior receipts were preserved. Legitimate concurrent bookkeeping is distinct from
the installation's zero canonical write scope. Generic unconfigured templates
still require real applicable setup provenance; transport metadata is not a badge
pass and no tracker is initialized merely for a greeting.

The nine focused source checks and earlier failed observations remain unchanged.
Host defaults, tools and harness settings differed across projects; timings are
individual wall-time observations, not causal host comparisons, model-only latency
or financial/economy claims. The observed routes do not establish persistent native
desktop activation, every project's manual-backend behavior, effective settings,
full ledger integrity, live supervision, autonomous updates or learning uptake.
Learning/manual procedures remain action-time contracts; these greeting checks did
not exercise them. No runtime payload, installer or manifest change was needed for
this documentation closure; installed runtime provenance remains the published
first-reply correction at `04dd95d`.

## Delegation exception correction — November 1, 2026

The reported installed refusal was followed by the same actor's acknowledgment
that its loaded AGENTS.md already met the actual host exception. That observation
does not establish an absent tool, a genuine user-only prohibition or a model-wide
inability. The recommended flat hook is now an unqualified positive delegation
request with bounded assignment and return evaluation. Its short production rule
contains neither the old qualifier nor host-exception debugging prose. The Director
has a separate short unavailable/prohibited-route stop boundary; the Worker keeps
useful descendants within assigned scope. The legacy hook has the same directive,
with its existing staffing/state route unchanged.

At the initial minimal delegation checkpoint, all 16 package-boundary/source-route
tests passed in 2.319 seconds; `git diff --check` passed. They inspect the actual
recommended installer's emitted hook, source-hook parity and both selected roles,
and check the direct request,
worker scope and no-silent-implementation fallback while
retaining direct discussion/narrow recording. These are instruction-route checks,
not proof that a model dispatched. The acceptance oracle requires an actual fresh
affected-model work request without an added delegation hint, a real bounded worker
handle, returned artifact/checks and owner evaluation. Genuine prohibition/tool-gap
and direct-discussion cases stay distinct. At authoring, those actor trials and
independent review remain pending; do not relabel earlier greeting checks as them.

A subsequent bounded instruction audit found a contradictory final-owner acceptance
sentence, an unnecessary implicit-role qualifier on the root check and a surviving
default roster reference. These were clarified without changing state code/schema,
human/independent gates or wire/lifecycle order. Direct discussion/judgment now sits
beside the execution delegation rule. Startup read wording was shortened while
retaining combined-output bounds, EOF coverage and recovery before action. Action
guides keep exact updater root, stale-instance rejection recovery and legacy-note
quarantine without debugging chronology. Daily discovery is arranged independently
of the greeting through a supported route/next project-work opportunity, with its
existing failure window and provenance review. Knowledge matching and transitive
action-reference requirements were intentionally not relaxed. Final source checks
and affected native-role observations must use this later candidate explicitly;
earlier frozen trials remain separate evidence.

The supported-v1/lifecycle audit separately repaired literal v1/lean guide routes,
qualified the pre-engine layout transition and phased its full boundary manual
before layout/install/update work while retaining startup ownership. Positive
legacy delegation rules replace the negative permission-search caveats. A dated R15
owner decision permits useful delegation without Git while retaining shared-tree
ownership, verified pre-write backups, honest recovery limits and user-only Git
initialization. Consumer-only duplicated badge/experimental trial chronology was
removed without changing runtime triggers. Targeted source route/guard tests and
independent review apply; a real disposable non-Git actor observation remains a
separate acceptance oracle. These edits change no helper or store schema.

After the final role-scoped hook and audit corrections, all 22 package/source-route
tests passed in 1.024 seconds and `git diff --check` passed. An earlier frozen
candidate also passed 36 package, starter-store/learning and startup-checker tests
in 10.366 seconds; later changes affected instruction specificity and consumer
routes, not helper code. Neither count establishes native delegation or acceptance.

Three clean native Codex CLI cases subsequently ran in temporary folders outside
the source checkout's instruction hierarchy, configured for `gpt-6.1-terra` with
`xhigh` reasoning. Actual tool traces showed: the root Director dispatched three
bounded workers; an assigned worker dispatched one useful child; and a substantive
implementation request dispatched two workers before their code changes, returned
eight passing tests and received parent evaluation without parent code writes.
These observations used the following near-final snapshot, not the later final
role-addressed hook or restored extent/adapter wording:

| Instruction source | SHA-256 |
|---|---|
| Installer/hook | `98093b706a5a694231608d3ef11622ce2b58143b5d67318f97b2f0be673e0d1c` |
| START | `fbbc5220248baf564ff10019822a9049266fa3eebe83053ae4e3222389ff7c8a` |
| DIRECTOR | `4635687d67fdfe6de6ffe0a48b9ac748e154479f066c6404841f7dcc94ef6c7f` |
| WORKER | `e68bd41968c4b20b84dac064dc9342aaf3b13e65a1ed22b2c7f80e25ef84b9e8` |

Earlier fixtures inside the source checkout inherited its ancestor AGENTS.md and
were confounded. They remain evidence, but are not a valid old-control comparison
or clean isolated trial. The actual desktop failure and these finite successful
cases do not establish deterministic model improvement, universal compliance or
an effective-cost comparison. Final installed-target Terra and two Claude Code
observations remain separate pending gates; publication of this source candidate
does not accept every target installation.

The source-only public agent front door now selects the actual package and resolves
its manifest/update links instead of imposing v1 staffing on the flat candidate.
All nine site contract tests passed, including actual canonical-path resolution,
the three unchanged copied requests and the ten-file public/private build boundary.
An initial run exposed a stale inherited exact-phrase assertion for the legacy
specialty rule; the replacement checks its current whole-owner/no-forced-manager
meaning. No HTML/style/runtime-helper change, rendered-site QA or deployment ran.

### Later installed review failure and ordered-work candidate

After source `0a5c1b0` was published, an actual installed Claude Code review request
read DIRECTOR and OPERATIONS but performed the review itself with no subagent call.
Observed Bash denials were not subagent launch attempts or subagent denials. This
negative observation is retained; successful earlier Terra cases do not make it
pass. Classification as direct discussion/acceptance is a hypothesis, not an
established internal cause or a model-wide diagnosis.

The next unpublished candidate names project investigations/reviews/changes in the
hook and requires delegation before detailed work. DIRECTOR says scope, dispatch,
then evaluate, while preserving ordinary discussion, simple lookups and acceptance
judgments directly. The broad distant reply-only sentence is removed; the legacy
hook mirrors the directive and its Director clarifies that a review reported in a
reply still delegates. No helper, state, schema or new role/reference is added.
All 22 focused source-route tests passed in 1.881 seconds; diff checking passed.
These tests do not prove execution. An affected fresh same-request installed retry
and independent review remain required before publication or target acceptance.

Subsequent native Terra and Claude cases using the ordered-work candidate did
dispatch actual children. Their predeclared complete-package checks still failed:
the parent omitted required staffing/maintained-role reads, or the brief prevented
the child from loading START and applicable knowledge before work. These are
**dispatch passes and package/guard failures**, not accepted end-to-end outcomes.
One earlier Claude case also exceeded the SitRep interval without a report while
the harness limited lifecycle tools; no new instruction's causal effect or repaired
periodic cadence is inferred from that observation.

The next candidate places the existing OPERATIONS staffing/role/guard step before
dispatch, requires exact worker startup/task instructions and applicable accepted
knowledge or access to retrieve it, and keeps those reads within scope. WORKER
returns a scope conflict before affected work. The old later staffing pointer is
moved, and all capability/effort/tier/source/identity/requirement/ownership fields
remain. All 22 focused source-route tests passed in 1.073 seconds; diff checking
passed. No helper, adapter, role catalog or state change is introduced. A fresh
predeclared end-to-end package case with genuinely available required read/query
and lifecycle tools, plus independent review, remains required before acceptance.
Old failed/partial primaries and their narrower harness limits remain preserved.

A later case again read START and issued a helper command without loading its
Director/project guard package or dispatching a child. Another parent selected its
staffing route but queried knowledge before the required native state/wire
instructions had returned; the child also lacked accessible pinned source material.
These remained failures of the predeclared integration oracle. Missing source/tool
access in a harness is not repaired by waiving the original verification purpose.

The next candidate makes the default role explicit in the adopted host hook and
distinguishes role assignment from an ordinary user task in START. It states the
existing return-and-read-before-dependent-action barrier and required canonical
I/O reads before knowledge selectors. Combined bounds, same-read extent/range,
EOF/recovery and all native wire/transitive guards remain. Director and Worker
staffing/package bodies retain their previous candidate hashes. Focused tests check
these instruction routes only; the last targeted native integration cases must
actually follow them with required read/query/lifecycle tools and pinned source
material accessible. Earlier narrower settings and failures remain separately
labeled, not an unchanged-settings causal comparison or a successful final package.

An actual shared-file integration review found AGENTS/CLAUDE routers that pointed
to shared instructions without carrying their own explicit delegation request.
Both update guides now require the role default and bounded-subagent request in
the actual host entrypoint too. The existing hook-merge regression covers both
guides and retains adaptation/backup/no-duplicate/ambiguous-integration guards.
Literal inspection of affected target entrypoints remains separate from source
guidance tests and native actor behavior. The frozen START/Director/Worker bodies
are unchanged by this updater-action clarification; no new controller, adapter,
host profile, helper or default execution mechanism is published by it.


## Portable reconciliation and composed project guidance — November 2, 2026

R9/R11 distinguish managed startup integrity from composed current project guidance.
R17/R18 preserve the adopted parent outcome when scoped children finish, a milestone
is accepted or a parent record is falsely terminal. The
[affected-purpose disposition](BEHAVIOR_PARITY.md#portable-reconciliation-and-composed-project-guidance--november-2-2026)
includes unchanged transitive authority, storage, discovery, privacy and learning
triggers. This work changes no canonical backend, request/source identity, lifecycle
or schema, and introduces no host enforcement framework.

### Composed project instruction check

The source checker now requires matching known baselines for managed
START/DIRECTOR/OPERATIONS/checker, while safely reading current AGENTS and selected
project-owned guards. It reports their historical snapshots as unchanged, changed or
not recorded. Malformed/conflicting baselines remain errors. One supported ordered
marked hook outside Markdown code examples must reference the selected START route.
The marked source defaults to AGENTS; explicit project-relative `--hook-source`
supports a selected shared instruction file. Outer AGENTS is always read, plus the
exact selected marked source and explicit actual host/shared/role guards. No
automatic search selects a passing file. The helper checks selected structure;
OPERATIONS separately requires the actor to read and evaluate the actual import
chain and all current instructions and resolve actual authority conflicts, including
ones outside an intact hook. No changed snapshot is silently promoted into a receipt.

The independent checker worker reported **19 CLI tests passing**, with syntax and
diff checks passing. They exercise composed-guidance drift, strict managed evidence,
marked-route recognition and failure boundaries. This is deterministic source/CLI
evidence reported to the owner, not a new installed-project or native-model trial.
The later shared-hook compatibility extension passed **23 focused CLI cases** in
7.495 seconds, reported by the checker worker; this supersedes the 19-case source
scope above without adding repeated runs into a total. The additional cases exercise
an explicit shared marked source, required outer AGENTS and safe selection/refusal
boundaries. There is no semantic compatibility or host-import proof from a selected
file's structure. An independent final reviewer also passed the 23 checker cases in 8.069 seconds
and the 15 continuation cases in 16.103 seconds after reviewing the selected shared
hook and transport clauses. These are repeated confirmation of the same distinct
cases, not additional cases. Combined source review and actual adoption remain separate.

The concise transport clarification in flat DIRECTOR and legacy ASSIGNMENT preserves
the same responsibility, purpose, authority, context, owner and return contract across
permitted routes. It requires an authorized source subset/usable locator and a real
route/access observation. Legacy Recorder and actual handoff gates remain. These
source clauses do not establish four host integrations or authorize a new transport.

### Adopted outcome continuation

The source candidate implements `continuation REQ_ID [REQ_ID ...]` over the
existing validated backend and a versioned ordinary-note checkpoint. Explicit caller
request IDs include terminal records. The view must expose actual sources, latest
checkpoint/event metadata and honest missing/stale/contradictory facts without
mutating lifecycle or certifying semantic completeness. It reuses `--team`,
`--offset`, `--limit`, `--max-bytes` and `--at-snapshot`; paging retains the same
ordered request-ID binding. The exact API is documented in
[API](../pattern/starter/payload/API.md#recover-the-adopted-outcome).

`DIRECTOR_CONTINUATION_V1 ` prefixes strict JSON in an ordinary native note with
schema, request ID, ordered source IDs, outcome, obligations, next action and wait.
A complete obligation needs declared evidence; unfinished obligations need a next
action or wait. Action and wait may coexist for independent work under a partial
hold. The latest note in the continuation family wins even when invalid or
unsupported. Unknown requests/absent notes are explicit gaps. Source-list differences,
later non-note events and terminal records with unfinished obligations are exposed;
ordinary later notes alone do not mark a checkpoint stale. No gap-free result proves
semantic completion, true evidence, actual execution or authority.

The author reported AST/help/diff checks passing and the existing bounded
current/status snapshot/wire/no-history fixture passing **1/1**. Independent focused
continuation fixtures then passed **15 distinct cases** in 15.457 seconds through
disposable installed CLI stores, using
[test_continuation_view.py](tests/test_continuation_view.py). Independent source
review first found uncaught deeply nested malformed JSON; the repair returns an
explicit invalid gap with null validated data and no older-note fallback. The final
15-case run includes that regression. Repeated runs are not added to the distinct
case count, and no author check is reported as independent acceptance.

Predetermined meaningful oracles:

- A done parent with completed children and remaining authorized obligations is
  retrieved by explicit ID; no open-only scan silently drops its binding.
- A useful accepted partial result remains accepted while remaining parent work
  and its next action/wait stay visible. The owner compares the whole adopted result
  with exact current sources and actually continues before voluntary yield.
- Held experiments do not block independent authorized research/synthesis. Explicit
  pause, real required user/external wait, correct bounded child return and sufficient
  completed bounded work remain truthful exits.
- A changed source frontier, newer malformed/unsupported checkpoint or absent note
  produces an explicit gap. Old useful evidence may remain visible but cannot silently
  become a current clean checkpoint.
- Bounds/snapshot changes, corrupted source or unfinished native journal retain
  honest refusal/recovery behavior. The inspection command writes no files and keeps
  existing current/status/mutation routes compatible.

A deterministic view can expose only recorded facts. It cannot infer user obligations
omitted by the writer, authenticate next-action declarations or cause a model to act.
Instruction-route tests do not prove actual delegation, continuation, complete context
consumption, five-minute SitRep cadence or compaction recovery. No new live model
experiments, Stop hook, native profile, scheduler, global skill, publication or broad
downstream adoption were performed for this documentation checkpoint. Those claims
remain separate, and the old failed/partial observations remain preserved.

### Retained context-delivery qualification

Automatic project instruction admission, later manual tool reads and model behavior
remain distinct. A model-free inventory at an affected route change should retain
actual selected override/root-to-working-directory chain, raw file bytes and required
entry boundary, with cap provenance labeled effective/known, default-only or unknown.
It should retain required query/access controls and actual returned-read coverage.
A known oversized chain can then fail its specific admission claim. A small disk
inventory alone cannot prove the effective Desktop cap, received context, consumption
or compaction restoration. Complete-read prose cannot cure an omitted startup pointer
or a denied operation. Individual and aggregate result bounds, contiguous read ranges
and recovery-before-action remain the portable manual-read route. Actual automatic
host admission and behavioral uptake remain pending qualification; this repair adds
no universal startup report, host configuration increase or delivery guarantee.

## Whole-result evaluation and consistent checked identity — November 4, 2026

The new regression concerns evidence adequacy after delegated component work.
All returned component checks can pass while the user's requested behavior still
fails. A harness that supplies its own device list and invokes refresh directly
does not establish the application shell, event handling, warning presentation or
window presenter. Repeated user reports of failure require the accountable Director
to reconcile that counterevidence and reconsider the proof path, rather than accept
another narrow pass. Another test owner can execute the proof; the Director still
judges whether it supports the whole claimed result.

The [whole-result scenario pack](fixtures/whole-result/README.md) and
[constructed inputs](fixtures/whole-result/cases.json) retain a concrete
component-green/user-failure case, authorized branch review and rework, a real
authority conflict with unrelated work continuing, a small flat task and completed
children with an unfinished parent. These are case definitions with observable
oracles, not automated model judgments or private production evidence. No new test
merely checks that runtime prose contains the expected reconciliation words.

The positive branch oracle requires actual progression: a qualified independent
reviewer rejects inadequate evidence, the owner repairs within existing authority,
the exact corrected version receives independent clearance and proceeds without a
fresh Root APPLY token. Root evaluates the reasons, evidence path, integrated
coverage and exceptions while retaining final acceptance. Proposed progression
alone does not pass. New backend/privacy/release authority escalates only the
affected action; a simple coupled task does not acquire a mandatory new manager.

For the whole-result case, require evidence that reaches the actual entry point
and claimed visible result, with substitutions and omitted stages disclosed. A
suitable known-bad/regression control should expose the failure when practical.
A synthetic substitute can demonstrate its own path only; it cannot establish
production recovery. Reject or narrow the completion claim until adequate proof
exists. The earlier zero-child/falsely-done-parent and partial-hold controls remain
under the [existing continuation cases](tests/test_continuation_view.py); recorded
facts and CLI behavior do not establish the owner's actual next action.

R9 already required the checked Director's reply prefix. The affected route must
preserve automatic first ordinary-reply checking, then consistent checked identity
on later discussion/status/acceptance replies while evidence remains current.
Relevant changed startup bytes require recheck; missing/stale-check questions cause
the possible check. A failed check or unresolved authority conflict gives its
specific gap and a normal answer without the badge. Workers and scoped child
Directors retain their own identities and skip that check. Neither a badge nor
the helper's `evidence_matched` certifies product success or full method uptake.

Focused package/link, startup-helper and continuation checks can establish
structural delivery, technical refusal/read-only behavior and recorded-obligation
preservation. Actual startup order, first and followup badge, whole-claim judgment,
path adequacy and the next suitable proof must be scored separately in an actual
bounded observation. Branch application, production behavior, broad reliability,
compaction and five-minute cadence require their own relevant evidence. New checks
and any observation results for this candidate are recorded below when executed;
the older failed/partial observations remain unchanged.

### Focused preservation checks and one bounded observation

The frozen runtime candidate passed **48 existing focused checks in 9.185 seconds**:
22 package/installation-boundary cases, 23 startup-helper cases, two transitive
load-path cases and the terminal-parent/idle-children continuation case. The helper,
checker, schema and emitted hook were unchanged by this source delta. These results
establish the exercised structural and recorded-data preservation, including genuine
negative inputs; they do not score the new judgment prose as agent behavior.

One explicitly authorized native CLI observation then used a fresh manifest-installed
candidate in a temporary project outside the source repository's instruction ancestry.
It used the configured host selection with no model override or global setting
changes, read-only execution and a 120-second limit per turn. The first prompt was
an ordinary greeting; the followup resumed the same actual session with the first
constructed case's supplied reports and acceptance question. The scoring rubric
was not supplied to the subject. No retry or further case ran.

| Dimension | Actual observation | Qualification |
|---|---|---|
| Startup and evidence check | The exact installed host hook was received. START, the complete Director/operations text and current local receipt/configuration returned before a separate successful checker call and greeting. | Checks the fresh CLI route; no original desktop or other-host claim. |
| First checked display | The greeting used 🎬 after the local evidence check. | Local role/check identity only. |
| Followup checked display | The same actual session's acceptance reply retained 🎬 with unchanged startup files. | No new failed/stale-check or worker-role native case ran. Existing helper negatives do not establish actor behavior in those controls. |
| Whole-result judgment | The Director rejected recovery completion despite passing components and retained valid partial results and the open whole outcome. | Judgment of supplied evidence, not autonomous discovery of the real harness gap. |
| Evidence path | It identified the substituted device list/direct-refresh harness as bypassing the visible application path. | No application or device operation occurred. |
| Next suitable proof | It named the real reconnect-to-window path and a regression/known-bad control where practical, then explicitly said investigation, fixes and installation had not been executed. | A proposed test is not an executed proof or actual branch progression. |

The greeting took 37.626 seconds and the followup 30.060 seconds; both exited
successfully and left every fixture file byte-identical. These are individual
wall times, not model-only latency or economic comparisons. Required local reads,
checker execution and actual session resumption worked. The retained native primary
does not serialize a full offered-tool inventory; uncalled capabilities remain
unknown. Two nonblocking managed-feature diagnostics were retained. The normal
host memory/skills were present, so this was a fresh chat without a parent-chat
fork, not a memory-free or instruction-only causal comparison.

This single observation supports the two delivered badge replies and the supplied
acceptance judgment at this exact candidate. It does not establish a general cure,
production recovery, actual test execution, delegated branch application, continued
action after a status interruption, failed-check recovery, role countercases,
compaction or cadence. Those behavioral scenarios remain defined and unrun here.
Independent source/evidence review and accountable-owner acceptance remain separate
from these observations.

## Bounded context and Stop prototype — November 4, 2026

This delta restores positive R9 attention instructions, adds an optional model-free
context calculator and develops an unactivated Stop prototype outside manifests.
The existing terminal-inclusive continuation API/backend stays unchanged; recovery
API expansion and packet/native-role frameworks are deferred. The
[intent matrix](BEHAVIOR_PARITY.md#bounded-context-and-stop-prototype--november-4-2026)
and R9/R17/R18 record the reasons and actual routes.

### Required focused evidence

The manifest destination `.director/context_check.py` requires caller `--root`, `--spec` and
`--max-output-bytes`. Check total versus required-boundary fit: exact-cap/overflow,
early boundary fitting with total over, later cut/omitted pointer, multibyte bytes,
unknown/default/effective provenance, no asserted boundary, unsafe/missing/changing
inputs and deterministic bounded body-free JSON. Unknown ignores any numeric cap,
default is conditional and effective is caller-declared; even full declared fit
must retain `actual_admission:unqualified`. Aggregate fit covers only positive
assertions, with asserted/unasserted counts; null/zero asserts no required coverage.
Preserve startup-checker compatibility
and installation boundaries without adding an automatic startup call.

The Stop prototype needs explicit session/root-owner/task/source-frontier binding
and a trusted snapshot command over the existing canonical route. Conformance must
send terminal/all-complete facts plus unfinished attempted final to an injected
evaluator and show one supported corrective block. Full pause, correct child,
sufficient completion and experiment hold with independent work are controls.
One snapshot, optional evaluation and correction total are allowed; an allow/error
also consumes the inspection allocation rather than monitoring later progress.
Repeated Stops/new turn IDs/source or checkpoint edits/final rewrites/process
restart must not reset allowance. Missing/corrupt established state, null text,
stale/source errors, invalid verdict, timeout and exhaustion must fail open. Check
process/output bounds, privacy diagnostics and no canonical lifecycle/source writes.
Injected evaluator decisions prove protocol/control only, not semantic quality.

Positive marker source review checks the reachable ❓/🖐️ instructions and grouped/
tool-card handling while preserving ordinary progress, checked 🎬 and heading-only
📋 SitRep. Prose matches are not observed uptake; actual questions and user-only
actions with negative controls need a separate observation.

### Current evidence and remaining gates

The context author's `python3 -B -m unittest development.tests.test_context_check`
final run passed **19 cases in 2.435 seconds**.
The author's existing `development.tests.test_flat_starter` and
`development.tests.test_startup_check` suites passed **33 cases in 13.153 seconds**.
Independent review replayed the same **19 cases in 2.054 seconds** and separately
checked small-cap/multibyte arithmetic, unknown provenance, cap overflow and asserted
versus unasserted coverage. These are deterministic calculator results, not native
admission evidence; reruns are not additional distinct cases.

The Stop author's `python3 -B -m unittest development.tests.test_stop_guard -v`
run passed **32 cases in 6.146 seconds**. Independent recheck passed the same
**32 cases in 5.887 seconds**, plus discriminating complete/partial-hold and persisted
control-state cases. These verify injected-command protocol and finite controls,
not actual bridge fidelity, evaluator quality or native prevention; reruns add no
distinct cases. Independent source review also confirmed the restored R9 marker
semantics; observed uptake remains unrun.
Earlier continuation and badge/judgment observations retain their original scope
and cannot substitute for these checks.

Actual host discovery/counting, effective admission, received text, consumption
and compaction remain unqualified. Stop delivery, trusted binding, real backend
snapshot bridge, evaluator quality, correction followed by authorized action,
interruption and genuine-user versus synthetic-prompt handling also remain
unqualified. No new marker-uptake trial ran. The live-model/native experiment hold
continues; publication would not activate the prototype. Source publication, target
installation, template updates and behavioral acceptance require separate evidence.
No future published pin is invented; prior failed/partial observations remain intact.
