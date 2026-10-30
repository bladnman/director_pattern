# Progressive loading review — October 30, 2026

This source candidate changes when instructions load; role authority and
installation acceptance remain unchanged. Interface 1, bridge/index locators, assignment role values, helper
entrypoints, store/config schemas and the manifest remain unchanged. Existing
project-owned bridges, PROJECT and role definitions are preserved; their older
unqualified requirements can retain the earlier, larger startup package.

The [bootstrap](../pattern/engine/PATTERN.md) requires a conversational package,
then explicitly triggered task/action packages. This is instruction guidance,
not an installed runtime, automatic injection or a guarantee of agent compliance.

## Reviewed obligation map

| Obligation | Required at startup | Mandatory later trigger and owner |
|---|---|---|
| Role and authority | Bridge → engine → canonical index → selected definitions; shared authority/gates; explicit bounded role; malformed delegation cannot default Director | Matching task references before affected inspection/execution; no generic specialist substitution under ROLES |
| Transitive requirements | A startup document's unqualified required refs load with it, recursively | A deferred document's unqualified dependencies load with it before its trigger; an explicit later trigger is required to defer further |
| Complete instruction text | Bound every visible response and outer aggregate; extents/ranges in reads; contiguous chunks through EOF; recover omissions before acknowledgment | The same rule covers task/action packages; no extra verification invocation after each successful read and no completeness/understanding guarantee |
| Direct answers and intended deliverable | Distinguish intended discussion from an artifact/change; no compulsory staffing, capture, Recorder activation, hash/setup checks or metadata discovery before a reply | Rendered alternatives/prototype/working behavior when the intended deliverable calls for them; publication authority remains separate |
| Director/manager boundaries | Non-worker; delegate substantial analysis/coordination before doing it; one whole-outcome owner; no silent role switch for unavailable routes | DIRECTION before coordination/delegation/evaluation/recovery/supervision/exit; resolve actual permission and routes before affected work |
| Staffing at any depth | Explicit capability discovery; workers may delegate within assignment/host limits | ROLES + MODELS + IDENTITIES + ASSIGNMENT + STATE before staff selection/dispatch; current controls, supported context, actual selections or unknowns, one working tree, parallel plan, ownership and tier |
| Identity | Use supplied emoji and bold name; only checked project Director may use its badge | IDENTITIES and persistence before reservation/binding/release; one roster/cursor, collision and late-return protection remain unchanged |
| Persistence | Shared Recorder boundary and canonical tracker are binding; no parallel ledger | STATE + indexed Recorder/adapter before canonical I/O/capture/recovery/recordable decisions; actual bundled-store operator also loads RECORDS + TOOLING; exact immutable sources and prompt recovery-critical receipts remain unchanged |
| Held commitments | Discussion/new input cancels nothing; keep resume points, actual observations and owner through acceptance | DIRECTION/STATE recovery loop at active entry without gating discussion; actual handle supervision, same-owner rework, parent traceability and proactive labeled SitReps from dispatch; no unsupported parent exit |
| Setup and badge | Loaded-package acknowledgment reports reads only | DIRECTION + persistence before setup/badge; background check when first staffing; no new runtime or backend requirement |
| Updates and lifecycle | No automatic update from loading instructions | UPDATES before metadata/preferences/update work; rolling 24-hour failure throttle, explicit automatic mode, exact pin/baselines/backups and acceptance preserved; structural changes add STARTUP/BOUNDARY and affected fresh trials |
| External actions and maintenance | Existing access/send/spend/release/install gates remain binding | Actual maintained runbook/authority before action; ROLES before recurring-role/rule changes. A linked protocol grants no permission. |

Protocols already read completely and retained in the context need no repeated
loading ritual. Changed, unavailable or no-longer-retained instructions need
reloading before the affected action. Installation/update integration must record
exact old requirement → new canonical locator + trigger mappings before changing
project-owned phases. Engine replacement alone cannot perform that review.

## File-load comparison

The table below records the earlier October 30 progressive-loading inventory,
before the later selector/coordination refinements. It is retained as a dated
measurement rather than advertised as the final candidate's byte count.
Baseline is source commit `28e7bb9`. Reproduce the current inventory with
`python3 -B development/startup_loading.py --tokens`; `--tokens` uses an already
available optional tiktoken tokenizer. Plain invocation uses only stdlib.
The inventory explicitly declares reviewed required sets; it is not a natural-
language instruction parser. Counts include the project bridge and generic engine
texts, deduplicated per scenario; project-specific fixtures are separate below.
Tokens use `cl100k_base` as a repeatable text-size proxy, not the actual host model's
accounted usage. Dependency stages are returned-result discovery stages; a file
may need several bounded responses within its stage.

| Scenario | Shared bytes before → candidate | Proxy tokens before → candidate | Dependency stages before → candidate |
|---|---:|---:|---:|
| Project Director, reply-only | 73,825 → 13,241 | 14,304 → 2,551 | 5 → 4 |
| Request Manager, reply-only | 73,710 → 12,523 | 14,296 → 2,402 | 5 → 4 |
| Bounded analysis worker | 8,445 → 10,480 | 1,626 → 2,034 | 4 → 4 |

The Director reduction is 82.1% in shared bytes. The worker gains 2,035 bytes
(24.1%) because complete-read handling and explicit common capability discovery
now reach it too; this is a safety/discovery tradeoff, not a worker speedup claim.
No extra worker dependency stage is introduced. The illustrative one-file/chunk
per response inventory at 12 KB text payload is 14 → 6 responses for each director
scenario and 6 → 6 for the worker. That is a conservative reporting policy, not
an optimized batching count, a host limit, or a universal byte-to-token guarantee;
real framing/escaping and outer response limits must still be budgeted.

The identical small project fixture adds 908 bytes / 190 proxy tokens for director
scenarios (index, authority and PROJECT), and 463 bytes / 108 proxy tokens for the
worker (index and authority). Real custom context and mandatory references add
their actual cost and can introduce further discovery stages. PROJECT is loaded
for directors after index-based role resolution, and for workers only when their
index, definition or assignment requires it. Index guardrails remain mandatory
for every role.

A maintained role that unconditionally requires the full public rationale and
design notes adds at least 149,803 bytes at this candidate's pre-addition baseline,
before its other references. Narrowing maintainer AGENTS to the overview, owning
decisions, affected contracts and relevant validation sections helps future source
maintenance; it cannot rewrite an installed role's explicit full-file requirement.
Such local definitions and an older PROJECT Working references section require a
separate reviewed phase mapping. That earlier inventory did not update this repository's installed engine, roles
or accepted receipt/source pointer. Subsequent reviewed local integration has its
own receipts and preservation checks; it does not promote an unpublished candidate
to the accepted published pointer. Stencil alignment is recorded separately below
and preserves project-owned phase requirements.

## Verification and remaining evidence

The focused regression suite checks each capability's independent policy targets,
all reachable package links against the manifest, reply/staffing required sets,
nested project authority/task/release paths after actual engine replacement, and
byte inventories. The read-evidence fixture compares visible contiguous text with
known source text and rejects inner elision, outer aggregate truncation, missing
ranges and failed reads; full recovery passes. This validates the fixture rubric,
not an agent or a production reader. Existing helper-root, project-preservation,
hook parity, host precedence and package-isolation regressions remain active.

The earlier unrun status is superseded for the bounded assigned routes in
[the later actual-host trial notes](DESIGN_NOTES.md#role-knowledge-and-actual-host-trials--october-30-2026).
A same-task older-engine/candidate comparison preserved ordered startup and
acknowledgment. The first candidate unnecessarily read DIRECTION before a plain
reply; a narrow exit-trigger clarification and genuinely fresh retry reduced
observed pre-reply instruction files from fourteen to eight, and top-level calls
from seven to five. The retry then loaded nested lookup rules before data work
and reused unchanged protocols on the next lookup. Its tiny final reply omitted
the assigned identity prefix; that distinct reporting miss remains recorded.

Actual integrated Input roles produced an evaluated private artifact through one
maintained worker and correctly framed a later consequential routing discussion.
An integrated Runway reviewer recovered actual truncated shared text before its
acknowledgment and task input, using a deliberately constrained reader. Exact
required text/ranges and first actions, rather than loaded self-reports, support
these observations. The six fresh assigned actors include the repair retry and
nested worker; they are not native unassigned/default-chat trials. No latency or
reliability claim follows, and effective runtime settings remained independently
unknown. Static tests and byte inventories remain separate evidence.

After source review, the three authorized local My Work stencils received exactly
11 changed engine files each. Complete preimages were backed up and verified; an
independent comparison confirmed all other 18/17/82 files unchanged, every selected
engine file equal to candidate source, all stencils uninitialized and a repeat
sync check a no-op. No hook, project context/index/role or reference phase changed.
External sync evidence labels the source unpublished. This establishes candidate
file alignment, not smaller customized startup, generated-project adoption, fresh-
host behavior or publication.


The later selection/coordination changes preserve a complete staffer authority
package while leaving full executor manuals mandatory at their actual triggers.
Reviewed local integration and actual trials are separate from published
installation acceptance. Touched knowledge upkeep refreshes current selectors and
accepted facts without deleting dated source evidence, introducing another tracker
or adding an approval intermediary. See the owning dated decisions in
[RATIONALE](RATIONALE.md#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes).
