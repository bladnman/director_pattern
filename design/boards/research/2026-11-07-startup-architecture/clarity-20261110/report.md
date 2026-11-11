# Startup route clarification

**Dated supplement · November 10, 2026**

Most detailed guidance in the proposal moves into eight separate files. A short AGENTS block carries reminders and tells the agent which file to open before each action. The older startup files would remain on disk but stop being the normal reading path. In both observed candidate runs, the agent did not open the recovery card after compaction.

This note clarifies that proposal against the current route and recorded test evidence. The candidate is a proposal and scratch prototype. It is not an adopted route, published starter, or accepted behavior replacement.

## The terms

- **AGENTS block**: a marked group of instructions in the project's root `AGENTS.md`, which the host is expected to load as standing project context.
- **Card**: a separate instruction file the agent is told to open completely before a named action. A card is not automatically loaded just because the block names it.
- **Current setup** below describes this source checkout's active local adaptation. A new project's public starter route is shown separately because it is a different installation state.
- **Proposed setup** describes the candidate block and cards in this investigation. The scratch test did not install them as a supported payload.

## 1. Current setup: where the work enters

In this checkout, root `AGENTS.md` selects the local route: `.director/START.md` → `.director/DIRECTOR.md` plus the selected `.director/OPERATIONS.md` section and `.director/PROJECT.md` / `.director/CAPABILITY_POLICY.md` guards → `.director/startup_check.py`. The Project Director completes that route before the first ordinary reply. The public new-project starter has a separate route: its bridge points to `START.md`, then the selected Director package and Operations section feed the initial check. These paths share a purpose, but they are not the same installation.

Today the Director's responsibilities are introduced through the startup package, then carried into task work. The proposal changes **when and how those responsibilities are retrieved**: a short always-loaded block carries turn-level duties, while separate cards are opened before relevant actions.

| Responsibility | Current route | Proposed route and trigger |
|---|---|---|
| Role and owner | Startup resolves the Project Director, worker, or scoped child Director before the first reply. | The block sorts roles. It assigns Directors the standing duties; workers and scoped child Directors follow their role-specific lines. This changes how a spawned report-back worker is classified; that disposition remains open. |
| Check and 🎬 | Project Director reads the installation-evidence instructions, checks guards/backend/loaded route, runs the check, then uses 🎬 only after a pass. | The block requires the Project Director's check before the first reply, including a greeting, and repeats startup after a compaction or resume. Within an uninterrupted context, unchanged check evidence remains current; 🎬 applies until the next break, so the check is not rerun before every reply. `badge.md` is read after a failed check or when installation/instruction loading changes; it explains check meaning and recovery. The candidate no longer binds 🎬 to checked startup-file hashes. |
| Requests and state | Director startup rules establish partner judgment, capture/splitting, request lifecycle, and narrow state work. | `requests.md` opens before capturing, splitting, steering a request, or any store command. It owns those detailed steps. |
| Staffing and evaluation | Director startup plus Operations staffing guidance govern delegation; the Director evaluates the full result. | `staffing.md` opens before staffing/briefing or setting tier and effort. `supervision.md` opens while supervising, evaluating a return, or ending a turn with work out. |
| Recovery and continuity | Startup says to repeat startup after compaction/resume; the Director's continuation rules restore held work. | `recovery.md` opens at the Director's first project action after a break. `knowledge.md` opens for task knowledge, recording a correction, or outcome closure. |
| Updates and privacy | Operations/Director guidance defines daily update discovery, update authority, and source privacy. | `update-check.md` opens when no daily check is due in 24 hours or update planning is discussed; `privacy.md` opens before first exact-source capture or changing Git tracking. |

The candidate does not put all eight cards into `AGENTS.md`. The block's role is to tell the agent which route to take and when to read each file. See the [candidate block](../slug-draft.md), [card trigger map](../layout.md#ii-cards), and the slide's [route diagram](route-map.svg).

## 2. Proposed setup: one trigger, then the relevant card

The block is the standing entry point. Its table names action triggers; each trigger points to a card. The card supplies the action's instructions. The candidate also names project-specific instructions, the role roster, and the startup-check command in a project-owned section beneath the block.

| Card | Open it before… | It carries… |
|---|---|---|
| `badge.md` | Handling a failed check, or integrating/changing instruction loading | What the check establishes, failure gaps, retry conditions, surrounding-instruction conflicts |
| `recovery.md` | A Director's first project action after compaction or resume | Finding held work, reconciling current evidence, resuming ownership, and recovery reporting |
| `requests.md` | Capturing, splitting, steering, or running any store command | Partner judgment, exact capture, request lifecycle, checkpoints, narrow state operations |
| `staffing.md` | Staffing or briefing work, or choosing tier/effort | Routing, roles, dispatch details, settings evidence, authority, independent work |
| `supervision.md` | Supervising, evaluating returns, or ending a turn while work is out | SitReps, result-level review, waits, completion, real exits |
| `knowledge.md` | Looking up task knowledge, recording a correction, or closing an outcome | Selectors, durable rules, learning review, role and fact upkeep |
| `update-check.md` | Project work when the last daily check is older than 24 hours (or none is recorded), or discussing an update | Daily metadata discovery, preferences, and who may update a project |
| `privacy.md` | Capturing an exact source for the first time, or changing Git tracking | Remote visibility, source warning, ignore choices, privacy boundaries |

The triggers are part of the proposal, not evidence that each path is reliable. For example, the knowledge card's trigger can fail to fire when the duty to maintain a role alias arises during staffing. The table is a map to test, not a claim of parity. The eight card files and their trigger prose are in [`cards/`](../cards/); seven were copied from current guidance with link changes, while staffing was rewritten. That content distinction does not make either route behaviorally proven.

## 3. Reachability and obligations left outside the route

The scratch installation kept `START.md`, `DIRECTOR.md`, and `OPERATIONS.md` on disk because the shipped checker hashes them. **Kept on disk is not the same as reached by the candidate route.** The candidate block does not route a Director to START or DIRECTOR. Operations is named only as optional detail in some cases, so its check failure, first-use, and context-preflight rules may not be reached at the time they matter.

The review map identifies these unresolved consequences:

- The candidate's recovery trigger misses a **new conversation that begins with work already outstanding**; this is not a compaction or resume event, so the recovery card is not necessarily opened.
- The draft shortens or relocates clauses about assignment resolution, read ordering and bounds, child/worker duties, cross-project update authority, mid-flight partner judgment, role aliases, guard timing, and update discovery. Their replacement route or trigger must be checked one by one.
- The proposed badge meaning no longer proves that the checked Director rules match the installed files. The badge card also contains old file pointers and a claim about complete startup reads, which conflict with the proposed route.
- Generated-project first-use ordering, the project-owned check command and guard reads, the role roster, and a proposed checker's new `WORKER.md` route all need coordinated implementation. The scratch recipe did not make those payload changes.
- A block's audience labels tell agents who should act; they do not hide its text from workers or other readers who receive the root file.

The full disposition list and disagreements remain in the [swap audit](../swap-audit.md), [slug review](../slug-review.md), and [layout map](../layout.md#iii-where-each-obligation-group-lands). The [duty diagram](duty-map.svg) shows both the proposed card trigger and known reachability questions.

## 4. What the existing evidence shows

There are three different evidence layers. They answer different questions.

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| Existing static repository tests | `test_flat_bridge_repeats_startup_after_compaction_or_resume` and `test_flat_reuse_rules_do_not_survive_compaction_or_resume` pin selected text, route hooks, and stale-evidence clauses. They were not run for this candidate, which changes some pinned text/placement. | That this candidate passes the suite, or that an agent actually re-reads a card after compaction and restores the intended work. |
| Scratch install recipe | A file-copy recipe from a disposable starter 3.2 install, plus the observed checker gap: the shipped checker expects `.director/START.md`; the candidate points at `.director/WORKER.md`. A throwaway checker copy was patched for the candidate trial. This control is not this checkout's local `.director` route or a published release. | A shipped checker change, supported install/update, source publication, or acceptance. |
| Four recorded live session trials | Each arm had two sessions and one manually forced compaction per session. After compaction, both scratch-control and both candidate sessions reran their own check and displayed 🎬. The scratch control used the shipped checker; the candidate used the throwaway patched copy. Initially, one control greeting was permission-blocked and unbadged, the other control passed, and both candidate greetings passed only with the patched checker. | Four initial passes, a common checker across arms, or proof that the badge's underlying instructions remained present. |

The observed post-compaction reads differ directly. In each control session, the agent freshly read `DIRECTOR.md` completely. `START.md` was re-attached by the host but not freshly read through a tool. `OPERATIONS.md` was partial in one control (lines 1–119 of 234) and complete in the other. In both candidate sessions, the agent opened **zero cards**; the recovery card was missed before the first project action. The host did not re-attach any cards. The post-break prompts were a status question and a small code lookup; no post-break staffing occurred. Delegation was seen in one of four candidate opportunities and three of four control opportunities, but the follow-up task was small enough that both setups permitted direct handling. The difference does not demonstrate a delegation failure. Writes were denied. The trial did not measure request capture, return evaluation, SitRep cadence, or actual state I/O.

A passing check and surviving badge are narrow evidence about the check command and display rule; they do not prove card re-entry, held-work recovery, delegation, or full-method continuity. This was one host, two sessions per arm, one manually forced compact per session. It does not test resume, repeated compaction, work already held at a new conversation, a worker's recovery, other hosts, the real installer/checker route, or a broad case requiring delegation. Do not infer a rate or general reliability from these four trials. See the [evidence diagram](evidence-boundary.svg), [test recipe](../test-install.md), and the existing investigation's [compaction evidence](../report.md#23-what-happens-at-compaction-sibling-evidence-not-re-derived-here).

**Dated recovery update · November 10, 2026:** Offline hook plumbing passed on synthetic input only. In the native headless attempt, PreCompact fired, but a provider quota response stopped the task before output; `/compact` produced no boundary, so no post-compact recovery behavior was observed and native recovery remains unverified.

The earlier study reports 21 compactions across nine sessions with no complete startup re-read. Those observations are a small sample; the proposed causal interpretation and transfer to other hosts remain hypotheses. **Correction to the earlier summary:** hosts do not uniformly discard every tool-read file; some may re-attach recently used files, and the behavior varies by host and session. The four-session table above records one host's attachments separately from fresh tool reads. Host documentation claims in the older report are dated research, not current verification. See [the original evidence limits](../report.md#23-what-happens-at-compaction-sibling-evidence-not-re-derived-here) and [host-by-host documentation limits](../report.md#3-what-survives-compaction-by-host).

## 5. The open decision

**Should the startup route be changed at all, and if so, which behavior-preserving route is acceptable?** The candidate has a smaller first-read path and readable action cards, but its check, reachability and recovery gaps still require disposition. No owner acceptance or payload publication is recorded.

The proposal leaves specific owner calls open: whether the role gate should treat a spawned report-back agent as a worker; whether 🎬 should stop certifying read/hash-managed startup parity; whether a project-owned roster should replace global role discovery and selected-definition reads; whether Directors should lose the package acknowledgment; which omitted clauses keep a reliable trigger; whether project guards and generated first-use precede 🎬; how project-owned settings survive updates; how to trigger full `UPDATES.md` reads and cross-project update authority; how to recover work already held when a new conversation starts; and whether the block/card size caps and existing card contradictions are acceptable.

The layout marks N1/N2/N4/N5/N6 as adopted design choices, but the scratch recipe does not implement them. N3 remains proposed and was not feasibility-checked; related block wording was withdrawn pending that check. These labels distinguish a design decision from an implemented or verified behavior.

Before implementation, the owning design rules require an obligation-by-obligation comparison against the previous route, explicit treatment of each changed or unreachable trigger, and a concrete regression oracle. The next useful gate is a reviewed parity map that includes the newly observed no-card recovery case and the initial-permission failure. Any live trial must use the intended checker and actual post-break card reads; a passing badge alone cannot close it. The repository's `development/BEHAVIOR_PARITY.md` describes that review requirement.

**Status labels:** the block and cards are drafted; their route was exercised in a scratch trial with a patched checker copy; implementation in the starter and source checkout is not demonstrated; human acceptance and publication are open.

## Source map

Public source files referenced above (repo-relative):

- `AGENTS.md`
- `pattern/starter/payload/START.md`
- `pattern/starter/payload/DIRECTOR.md`
- `pattern/starter/payload/WORKER.md`
- `pattern/starter/payload/OPERATIONS.md`
- [Candidate block and route](../slug-draft.md)
- [Candidate file layout and action triggers](../layout.md)
- [Scratch installation recipe and checker gap](../test-install.md)
- [Independent swap audit](../swap-audit.md)
- [Detailed prior investigation](../report.md)
