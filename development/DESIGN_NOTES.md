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
