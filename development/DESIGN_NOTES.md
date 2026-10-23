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
