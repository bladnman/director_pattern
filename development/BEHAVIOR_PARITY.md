# Preserving the design obligations in the flat foundation

Correction review · October31,2026 · **scoped source and target gates accepted, with declared limits**.
Flat orchestration removes compulsory actors, not the reasons the previous design
existed. Reusing code proves neither good assignments nor actual host behavior.
This matrix accounts for every legacy manifest capability and its documented
reason; it is not a declaration that every old CLI branch or host passed.

The earlier starter2 single-JSON backend was a design regression. Reproduced cases
lost the initial plan owner/acceptance after update, left accepted work accepted
after a new addendum, and missed corruption of an earlier source when a later source
was valid. It also lacked equivalent relationship/handoff/attachment/recovery
semantics. Those defects were not authorized consequences of fewer actors. The
current starter3 default restores the established request-bundle backend; existing
experimental2 data and trial evidence remain unchanged, with no silent migration.

## Field report triage — November 13, 2026

An adopting video project, after shipping a video and holding a retro, reported (the
run used starter 3.2 text; the project moved to 3.3 after the ship, and the rules at
issue read the same in both) that its Director never proposed a role for recurring
work, made a call that belonged to an existing specialist role, never proposed
cutting a step, lost a process answer in chat, and let SitReps lapse in quiet
stretches. This repository's Project Director triaged it into one class of mistake
(the roster and recorded steps treated as a fixed lookup table, questioned only after
a failure) and decided the dispositions below on November 13. **Implemented in the
starter source as revision 3.4. Independent review accepted, with its findings
applied; maintainer acceptance and publication pending. Static tests only; no live
run.** The active route is the 3.3 one: the host-loaded block, then a card read
before its named action.

| Owning purpose and failure prevented | Disposition and active route | Concrete oracle and claim boundary |
|---|---|---|
| R18 Oct 30, "departments follow recurring responsibility observed in real work"; R17 Oct 30, closure upkeep is "not a role census". Field: retros, cut-diff analysis and render chains briefed from scratch each time; no role ever proposed. | **Accept (R18 Nov 13): bounded look-back.** Block table row "close an outcome, or hold or brief a retro" → knowledge card, "Look back on the work": at closure or a retro, two questions of this conversation's work (recurring role-less work; steps not earning their cost), one ❓ proposal each, the user decides, a new role registered before use, one repeat a candidate, nothing when nothing recurred and every step earned its cost; a delegated look-back carries both questions, and the staffing card's brief puts them in every retro or look-back brief. No threshold, no automatic role, no LEARNING or store change. | `test_knowledge_card_looks_back_with_two_bounded_questions`. **Trigger unproven, risk knowingly accepted (R18 Nov 13):** a card read, already unproven for this card (November 11 unknown 3); the block has no room for the paragraph. A retro proposing a role, or proposing nothing when nothing recurred: not run. |
| R10 Oct 21, no generic substitute for a matching maintained role; staffing card, a general worker never silently replaces one. These govern staffing only. Field: a packaging role's rule was written; the Director judged the owner's title and thumbnail itself and was corrected twice. | **Accept (R10 Nov 13): extend no-substitution to the Director.** Duty 2, the staffing card and the requests card: a judgment, draft or rule in a roster role's domain goes to that role, even in chat; accepting a return against the whole request stays the Director's. Routing costs a normal capture and brief, by design. The Director routes from the roster row and the role file's selection and authority part, not the role's craft. The installer's project section keeps one line per role's domain if the roster moves to a file; existing sections do not get that line from an update. A project-owned cause (the project's own packaging-check guidance) is the project's to change. | `test_a_call_in_a_roster_roles_domain_goes_to_that_role_even_in_chat`, `test_flat_roles_preserve_delegation_fallback_and_bounded_worker_default`. A conversational question in a role's domain routed to it: not run. |
| R2 Nov 1, delegate before detailed review; misclassification as discussion is the hypothesis. | **Narrowed by domain (R2 Nov 13 cross-reference):** acceptance judgments of returned whole results stay direct; a role's call does not. | Same oracle as the row above. |
| R1 Nov 7 partner rule: map a request onto the established mechanism; recommend a better route as ❓ and hold affected work. Field: every recorded step applied as fixed procedure. | **Accept (R1 Nov 13):** requests card, inside the partner rule: the established mechanism is the default route, not a fixed law; a step not earning its cost on this request is named and its cut or merge recommended as a ❓ once; the step is kept until the user chooses, and a repeat goes to the look-back. The look-back row above covers steps across a whole outcome. | `test_a_step_not_earning_its_cost_is_asked_once_and_kept_until_the_user_chooses` (wording and order). Not run. |
| R17 Nov 7, check each turn whether a SitRep is due. Field: no turn arrives in a quiet stretch, so the check never runs; the Director fixed it with its own five-minute timer. | **Accept (R17 Nov 13):** supervision card: with no return or user message expected before the next SitRep is due, arm a supported background timer or wait that leaves the Director available to the user; a quiet stretch does not pause the cadence; with none, say so once and send each due SitRep at the next turn. Interval unchanged; no host tool named. | `test_a_quiet_stretch_does_not_pause_the_sitrep_cadence`. Cadence over a quiet stretch: not run. |
| Findings lost in chat (field). | **Mostly project-owned.** One pattern clause: the look-back keeps its answers where the project keeps findings the user reads back, not only in chat. Where that is (a board, a journal) stays the project's. | Covered by the look-back test. |
| Model capacity ran out mid-run; the project's guidance names a model (field). | **No pattern change.** The starter names no model (`test_standing_text_and_cards_name_no_model` stays green); the project's mapping is its own. | Existing test. |
| R11 Nov 11: a block reaches an installation only through a reviewed update; the receipt precedes required checks "for this move only". 3.4 is the first block change after the move. | **Accept (R11 Nov 13):** UPDATES "Update an installed block": replace the bytes between the markers the check selects, byte for byte, with a project's own marker pair in place of the block's first and last lines; leave the project section untouched apart from the `--receipt` paths; new receipt with card and block baselines, the block hash covering the marker lines as they stand (what the checker hashes); the receipt-before-trials ordering now also covers a block update. | `test_update_guide_updates_an_installed_block_without_touching_the_section`; `test_a_3_3_installation_updates_its_block_and_keeps_the_section_and_markers` scripts the steps against an exact 3.3 fixture, with and without custom markers. **No installed update: unknown.** |
| Block within 8,000 bytes (R10 Nov 11). | **Preserved by tightening, no rule dropped:** six phrases shortened with their meaning kept, listed in R10 Nov 13. The Roster rule is **narrowed** (row below). 7,997 bytes. | `test_block_is_one_marked_region_within_its_byte_cap` and the updated pins. |

**Acceptance-blocking unknowns for 3.4:** none of the four new rules has a live run;
the look-back and quiet-stretch rules sit on cards behind triggers already unproven;
no installation has taken the block update, and this checkout's own root AGENTS.md
keeps the 3.3 block until its own reviewed update; the owner's decision on these
dispositions is not recorded.

*November 14 addition:* this checkout's installation and its 3.3 block moved to a
private sibling workspace, and this repository's AGENTS.md no longer carries a block
([R14](RATIONALE.md#r14--commit-the-installation-with-the-project)). The block-update unknown above now concerns the installation in
that workspace.

## Standing block and cards — November 11, 2026

Starter revision 3.3 replaces the default startup route. It is implemented on a
branch and is **not merged, not published and not accepted**. This section is the
design-intent disposition against the previous recommended path, the 3.2 route:
bridge in AGENTS.md → START.md → DIRECTOR.md or WORKER.md → OPERATIONS'
installation-evidence section → `startup_check.py`, with OPERATIONS' staffing and
privacy sections and the manuals read before their actions.

**Active route in 3.3.** The host loads AGENTS.md. Its marked block
(`director-starter:2`, from `pattern/starter/agents/block.md`) holds the role gate,
the Directors' ten every-turn duties, the Project Director's check paragraph, the
Recovery steps, the read rules, the "Before you / Read" table, the Summaries rule and
the Roster rule. The project-owned section below it holds the check command, the two
guard lists, the store line, the role-file locator and the roster. Seven cards in
`.director/cards/` are read before the actions the table names. Workers read
WORKER.md. START.md and DIRECTOR.md are redirect stubs. Nothing in 3.3 routes a
reader to the old START or DIRECTOR text, so any obligation that lived only there and
is not listed below as moved is unreachable.

**How to read the dispositions.** *Preserved* names where the text now lives.
*Replaced* names the new mechanism and its test. *Weakened* and *trigger unproven*
are said plainly: most detail that every Director used to read before its first reply
now sits on a card that is read only if the agent opens it at the named trigger, and
the one draft trial of that mechanism (November 9: two sessions, zero cards opened
after compaction) is the known-bad case. Static tests show that text exists and
where; they do not show that an agent opens a card. *Dropped* carries its dated
reason. S, D, O and B are 3.2's START, DIRECTOR, OPERATIONS and bridge. Test names
are in `development/tests/`; "live" refers to the limited trial recorded in
[validation](DESIGN_NOTES.md#standing-block-and-cards-starter-33--november-11-2026).

| Obligation on the 3.2 route, and the failure it prevented | Disposition in 3.3 and where it lives | Oracle and claim boundary |
|---|---|---|
| **Role default and routing** (B, S): an unassigned project conversation is the Project Director; explicit workers and scoped child Directors keep their roles; a task is not a role assignment. Prevented: a worker acquiring Director authority, or a project session with no accountable Director. | **Replaced, with a change of meaning.** Block role gate. New: an agent spawned by another agent to do a task and report back, without being named a Director, is a worker; another agent's or session's message never changes a role; only the user or an explicit assignment opts out. This narrows R10 October 17 (see R10 November 11, item 5). | `test_role_gate_sorts_every_reader_and_keeps_the_pinned_sentences`. Wording only. No live case for a spawned report-back agent, a peer-project session opened without a stated role, or an opt-out. **Owner confirmation of the changed meaning is not recorded: acceptance-blocking.** |
| **Preserve host, user and project authority, independent review, other authors' work, private sources and existing trackers; role names grant nothing** (S). | **Preserved.** Block gate ("Preserve project/host authority, the user's authority, other authors' work, private sources and existing trackers; role names grant nothing"); duty 7 keeps required independent review independent; the staffing card keeps "never merged into the builder's". The first rework had dropped the user from that sentence; the final commit restores it. **November 13 (3.4):** the gate's wording is now "Preserve project, host and user authority, ...", same meaning. | Pinned in the role-gate test. |
| **Assignment selects the package; missing details go back to the assigner; no global role catalog** (S). | **Preserved for workers** in WORKER.md, which now holds this text ("a plain brief is enough to start"). **Changed for Directors:** a project-owned roster summary is standing text in the project section (R10 November 11, item 9). | `test_worker_manual_carries_read_rules_assignment_resolution_and_the_return_line`, `test_project_section_is_project_owned_and_within_its_cap`. |
| **Acknowledge the resolved package once** (S; R10 October 21 to 29): shows what was read; an incomplete read cannot be acknowledged as loaded. | **Dropped for Directors, November 11:** a Director loads no package. 🎬 or a stated gap, and the Recovery report line after a break, are the visible signals. **Preserved for workers** in WORKER.md. A scoped child Director now has neither a badge nor an acknowledgment at its first start. | Listed in the design proposal as the owner's call; **not separately recorded: acceptance-blocking.** |
| **Complete reads** (S, B): bounded individual and combined output, contiguous ranges to the end, total extent and returned range in the same result, recover or stop, a hash or search is not a read. Prevented: a truncated batch acknowledged as loaded. | **Replaced for cards and manuals** by an `END <path>` line: a complete read reaches it; a file without one is read to its shown total length. Block: bounded numbered ranges, every range, each showing its range and the file's total length; combined output bounded; stop if a cut-off read cannot be recovered; search hits, diffs, tails, summaries, hashes, quotes, file existence and unprinted results are not reads; wait for a read before the command it governs. The first rework had left the range-and-length, combined-output and existence/unprinted rules in WORKER.md only; the final commit restores them to the block. WORKER.md keeps the longer text. **Dropped, November 11** (cost limits, not safety): "Read known independent files together when their combined output fits", "Coverage shown in the read needs no separate verification call", "with room for tool framing", and "Installer/source documentation is not startup". | `test_reading_rule_keeps_the_reentry_sentence_first_and_defines_a_fresh_read`, `test_cards_ship_in_the_manifest_and_end_with_their_end_line`, `test_manuals_and_stubs_end_with_their_end_line`, `test_flat_complete_reads_keep_combined_bounds_and_recovery`. Live: both sessions read the staffing and requests cards fresh before acting. No test or trial covers a truncated card read. The last two dropped clauses were not in the list given to the author of this entry; they are reported for the owner. |
| **Task instructions before their action; read again after compaction or resume** (B, S, D; R10 November 9). | **Preserved and tightened in text.** The November 9 sentence is word for word at the top of the block's read rules. "This startup", "a break", "fresh" and "repeated" are defined there. | `test_flat_bridge_repeats_startup_after_compaction_or_resume`, `test_flat_reuse_rules_do_not_survive_compaction_or_resume`. Live: check rerun after compaction in both sessions; card re-reads partial (below). |
| **First-reply check, even for a greeting; 🎬 on every reply after a pass; a failed check gives its gap and an ordinary answer; a badge question reruns the check; workers and scoped children skip it** (B, S, D, O; R9 October 31, November 1, November 4). | **Preserved** in the block's check paragraph and gate; detail on `cards/badge.md`. The command now comes from the project section. | `test_check_and_badge_paragraph_is_for_the_project_director_only`, `test_flat_root_check_and_final_acceptance_match_the_flat_roles`. Live: one new conversation and two post-compaction replies ran the check and showed the badge. A failed check has not been observed live on 3.3. |
| **What 🎬 claims** (O; R9 October 31; R18 October 31): a passed check plus the actor's confirmation of complete selected reads, role and guard authority and backend binding. | **Replaced, narrower** (R9 November 11): the check passed since the last break and the actor confirmed the check's listed items. No claim about startup-file reads. | Tests as above. **Owner confirmation of the changed meaning is not recorded: acceptance-blocking.** |
| **Actor evaluation before the badge** (O 101–118; R9 November 2): read surrounding instructions; an intact hook cannot excuse a conflicting role default, disabled checks or a competing tracker; an unrelated receipt-listed file is not a backend declaration; an omitted guard is not checked. Prevented: a badge over a conflicting installation. | **Weakened.** The text is on `cards/badge.md` ("Confirm before the badge"), which the table names only for a failed check or a change to the check or loading route. On a passing check the actor sees only the four short `actor_must_confirm` strings in the check's output. | `test_intact_hook_with_surrounding_override_still_requires_actor_judgment` shows the checker still passes such a file and leaves the judgment to the actor. Nothing shows the actor makes it without the card. **Acceptance-blocking until dispositioned.** |
| **Managed integrity of the Director's rules** (R9 November 2): START, DIRECTOR, OPERATIONS and the checker must match recorded hashes. | **Replaced.** The block's bytes must match the receipt's `director_block_sha256`; WORKER.md, OPERATIONS.md, the checker, the two stubs and the seven cards must match recorded hashes; the project section must exist once, hold a check command and stay within 3,000 bytes. A receipt with no recorded block baseline blocks the check (the first rework let it pass with an added `actor_must_confirm` item; the final commit closes that), and the installer, generated first use and the move each record the baseline. Text inside the block is no longer a place for project adaptation. | `test_gutted_or_negated_director_block_blocks_the_check`, `test_redirect_stubs_are_hash_checked_on_the_block_route`, `test_project_section_is_required_once_beside_the_block`, `test_managed_foundation_still_requires_known_installed_integrity`. |
| **Earlier route keeps working until a project moves** (R10 November 9: the checker accepts earlier wording under the retained marker). | **Preserved, bounded.** A block that names START.md passes only while START.md, DIRECTOR.md, OPERATIONS.md and the checker match their baselines and START.md is the full earlier file. Pointing at the stub blocks with a named gap. | `test_earlier_start_route_passes_only_with_its_own_full_startup_files`, `test_old_bridge_pointing_at_the_redirect_stub_is_an_unfinished_update`. |
| **Host-required progress note before the check** (S, O; R9 November 4). | **Preserved.** Block: "A host-required progress note first stays unbadged and claims nothing"; badge card. | Pinned in the check-paragraph test. |
| **Generated-project first use before the check** (S, D, O; R9 November 4). | **Replaced; trigger unproven.** The block says to run the check "after any first-use step" the project section lists; a generated project's section must list FIRST_USE.md and its required reads. `first_use.py` follows the route the block names. The installer's default section lists nothing, so the order depends on each template's section. | `test_generated_project_route_follows_the_marked_block`. The generated receipt now records the block baseline the check requires. No generated template has been restaged on 3.3 and no generated first reply has run. **Unknown: acceptance-blocking for generated projects.** |
| **What the check reads, that it writes nothing and needs no store manuals, hold its output in context** (S, D, O). | **Preserved in text, off the passing path:** badge card and OPERATIONS. | Checker behaviour is unchanged and tested (`test_fresh_check_is_readonly_and_does_not_claim_consumption_role_or_ledger`). |
| **Receipt formats, hook structure, `--hook-source`, `--backend-contract`, context-budget preflight** (O). | **Preserved** in OPERATIONS, reached through the table's last row. The preflight is also a step of the move. | Existing checker and context-check tests. |
| **Partner rule** (D; R1 November 7). | **Preserved.** Short form in duty 1; full paragraph on the requests card, whose trigger is capturing, splitting or steering a request. **November 13 (3.4):** the requests card adds that a step not earning its cost is recommended for a cut as a ❓ once and kept until the user chooses. | `test_ten_standing_duties_keep_the_delegation_request_and_fallback`, `test_card_audiences_and_moved_obligations`. Live behaviour unobserved, as before. |
| **Read all of UPDATES before planning any update; another installation is updated only from its own project** (D; R11 November 7). | **Preserved.** Table row and `cards/update-check.md`. New: a session started in another project for an update is told its role in its first message. | `test_card_audiences_and_moved_obligations`. No live rollout. |
| **❓ and 🖐️** (D; R9 November 4). | **Preserved.** Duty 9. The longer paragraph (one ❓ for a grouped set, recommend an answer, do not invent questions) is on the requests card, behind a trigger unrelated to asking a question. | Pinned wording. Uptake unobserved, as before. |
| **Delegate investigations, reviews and changes before the detailed work; answer discussion directly; if subagents are unavailable, report the gap and stop** (B, D; R2 and R10 November 1). | **Preserved.** Duty 2, with the pinned sentences. **November 13 (3.4):** duty 2 adds that a judgment, draft or rule in a roster role's domain goes to that role, even in chat; the delegation sentence drops its "Directors," vocative ([triage](#field-report-triage--november-13-2026)). | `test_ten_standing_duties_keep_the_delegation_request_and_fallback`, `test_flat_roles_preserve_delegation_fallback_and_bounded_worker_default`. Live: both sessions delegated before and after compaction. |
| **Before dispatch, read the staffing instructions and select the maintained role and its guards; give the worker its instructions and knowledge** (D, O; R10 later November 1). | **Replaced.** Table row → `cards/staffing.md`; duty 5 lists the brief's ten fields; the Roster rule and the project section point to the roster and role files. | `test_brief_fields_match_the_staffing_card_in_order`, `test_table_names_only_shipped_files_and_every_card_has_a_trigger`. Live: both pre-rework sessions read the staffing card fresh before staffing, before and after compaction; in the in-flight trial the Director read it fresh before two follow-on dispatches. |
| **The staffer reads the selected definition's selection and authority part; the executor reads the rest** (O; R10 October 30). | **Preserved; no supersession.** Block Roster rule, staffing card, project section's role-file line, WORKER.md. The staffing card's list of what the staffer reads names the assignment role and the exact task/action trigger map again (restored in the final commit). **November 13 (3.4), narrowed:** the Roster rule now says "Before dispatch read only the selection and authority part of the role file its row names." The permission "the rest is for its executor" becomes the limit "only", and the file is the one the role's row names, no longer any file "the row or section names"; the section's own role-file line still asks for the same read. The read before dispatch is kept. | `test_card_audiences_and_moved_obligations`. Not observed live with a real role file. |
| **Tier and effort set explicitly on every dispatch; strong tier at high effort by default; the lighter option; record requested, selected and effective settings with a reason** (D, O; R2 November 5 and 7). | **Preserved.** Duty 3; staffing card. | Pinned wording. Live: on the pre-rework build the worker tier choice was confounded by a visible budget figure. In the in-flight trial, with no budget figure shown, the Director chose the strong tier at high effort for all four dispatches; observed once. |
| **Local judgments, bounded rework authority, return contents, no self-review; same contract across sessions and external routes; source subset only** (D, O). | **Preserved** on the staffing card ("Authority", "Return route", "Routes and ownership") and the supervision card. | Pinned wording only. |
| **Stay available; no mandatory manager or Recorder; another Director only for real coordination; no departments from a correction count** (D). | **Preserved.** Duty 2; supervision and staffing cards. **New in the payload:** the routing ladder (do it yourself; a worker; a scoped child Director). **November 13 (3.4):** the ladder's first rung adds the role-domain sentence; still no department from a count. | Pinned wording only. |
| **Verification tiers; emoji Names** (O, S). | **Preserved.** Staffing card; duty 5; WORKER.md. | Pinned wording only. |
| **Capture exact inputs before dependent work; split each finishable obligation; legal lifecycle and steering; narrow state operations are the Director's; discussion needs no capture** (D). | **Preserved.** Duty 4; requests card; the manuals before any store write. | `test_card_audiences_and_moved_obligations`. Live: both sessions read the requests card fresh before acting. No capture, split or steering was measured. |
| **Checkpoints** (D). | **Preserved** on the requests card. | Pinned wording only. |
| **Store manuals (API, TOOLING, RECORDS) completely before any store operation** (R10 October 30; R9 October 31). | **Preserved for every write and for `recover`. Replaced for three read-only views** (`status`, `continuation`, `current`) on the bundled store, which need the requests card alone (R17 November 11). | `test_card_audiences_and_moved_obligations` ties the card's gap names to the helper. The card can drift from the manuals; no parity test covers its field descriptions. Live, in-flight trial, once: the Director ran the status and continuation views having read 0 bytes of the store manuals, and read the requests card immediately **after** the views, not before; it reread the manuals before its store writes. **Open: the block routes the views through the card and the observed order did not follow it.** |
| **Judge returns against the whole intended result; reassess after repeated failure; smallest proof** (D; R17 November 4). | **Preserved.** Duty 7; supervision card. Every worker return now ends with a line telling the owner to read the supervision card before accepting. | `test_worker_manual_carries_read_rules_assignment_resolution_and_the_return_line`. Live: on the pre-rework build one of two sessions skipped the supervision card after compaction; in the in-flight trial the Director read it fresh before evaluating returns. Three sessions in all; no rate implied. |
| **Keep the outcome open; on recovery retrieve all task-bound request IDs, including terminal ones; correct a false "done"** (D; R17 November 2). | **Replaced.** Block Recovery steps and duty 8; also run in a new conversation before the first reply that acts on the project (R17 November 11). | `test_recovery_steps_live_in_the_block_not_on_a_card`. Live: Recovery performed through the store and re-entry reported after compaction in both sessions, on the build before the Recovery-timing and store-view changes. Work was already finished at each compaction. In-flight trial, reworked build, one session, two workers still running at a real compaction: check rerun; read-only views run on both held requests; re-entry reported with the correct count and both workers named; no re-dispatch, and both original workers completed with no duplicate. Closing the requests through the store was not reached. **Observed once; no rate implied; resume, repeated compaction and other hosts still unverified.** |
| **📋 SitRep about every five minutes while work is out; check each turn; cover every stream; shape and example; after a break only if overdue or unknown; no-time-source fallback** (D; R17 November 7). | **Preserved** as duty 6 (cadence and per-turn check) and, verbatim, on the supervision card (coverage, shape, example, unchanged-turn line, fallback). **Weakened:** everything but the cadence sentence is behind the card. Recovery step 4 now carries the November 7 condition (send one after a break only if overdue or its last time is unknown), matching the card; the first rework's unconditional "now" was corrected in the final commit, so that inconsistency is closed. **November 13 (3.4):** the supervision card adds arming a supported background timer or wait for quiet stretches; still behind the card. | `test_ten_standing_duties_keep_the_delegation_request_and_fallback`. Live: on the pre-rework build one of two sessions skipped the supervision card after compaction and sent no SitRep in that reply. In the in-flight trial the Director sent none in the re-entry reply, deferring to the next due time, and sent SitReps on schedule later; observed once. |
| **Continue to completion; real exits; submitted, verified, accepted and published differ; waits instead of polling** (D). | **Preserved.** Duties 8 and 10; supervision card. "Waits, not polling" is on the card only. | Pinned wording only. |
| **Incidents, the three-incident review or a recorded deferral, explicit user rules; closure upkeep of roles, pointers and facts** (D, O; R18). | **Preserved** on the knowledge card and in LEARNING. **Trigger unproven:** the trigger is "record a correction, or close an outcome". **November 13 (3.4):** the trigger becomes "close an outcome, or hold or brief a retro", and the card adds the bounded look-back; still unproven. | `test_card_audiences_and_moved_obligations`. Live: one of two pre-rework sessions skipped the knowledge card after compaction; the in-flight trial did not reach a correction or a closure. **Still unproven.** |
| **Keep caller and role IDs and aliases resolving through refactors; register a role before use** (S, O). | **Preserved** on the staffing card (trigger: change a role) and the knowledge card (closure). | Pinned wording only. |
| **Task-time knowledge selectors** (S): every role read this at startup. | **Preserved for workers** (WORKER.md links the knowledge card). **Trigger unproven for Directors:** the procedure is on the knowledge card behind "look up knowledge for a task"; the standing prompts are the brief's "applicable knowledge" field and that table row. | Selector-order pin in `test_card_audiences_and_moved_obligations`. No live knowledge lookup observed. |
| **Daily update discovery during active sessions** (D; R11). | **Replaced.** The check's output carries `update_check` (`due`, `not_due`, `off`, `unknown`) from the local cache; the table sends the Project Director to the update-check card when it is due or unknown and project work begins. A greeting still triggers nothing. **Narrowed:** the hint is produced only when the check runs, so a conversation that crosses the 24-hour mark without a break gets no new prompt. | `test_update_discovery_hint_reads_only_the_local_cache`, `test_update_card_repeats_the_exact_notify_sentence`. Not observed live. |
| **Continuity and privacy** (O; R14). | **Preserved verbatim** on the privacy card, now with an explicit trigger (first exact source capture; changing what Git tracks). 3.2's START and DIRECTOR had no pointer to that section. | `test_no_payload_text_routes_to_the_removed_sections`. Not observed live. |
| **A mature project's guards and exact check command** (project files; R9 November 2). | **Replaced.** The project section states the command and lists guards in two groups: read before the first reply, and read before named work. Which group each existing guard joins is decided in each project's reviewed move. | `test_mature_receipt_list_and_external_config_preserve_local_guard_composition`, the scripted move. **No mature project has moved: unknown, acceptance-blocking for existing installations.** |
| **A scoped child Director gets the Director foundation plus its overlay** (S, D). | **Replaced; trigger unproven.** The child follows the block's Directors-only sections for its outcome, and its overlay. That reaches the child only where the host passes AGENTS.md to subagents; the staffing card tells the staffer to include the block's text otherwise. | Role-gate test. **Not verified: a host that does not pass AGENTS.md to subagents; no child Director has run on 3.3.** |
| **A worker's startup** (B → START → WORKER). | **Replaced.** The gate sends a worker to WORKER.md, which now carries the read rules and assignment resolution; the staffing card says to tell every worker to read it. | `test_worker_manual_carries_read_rules_assignment_resolution_and_the_return_line`. A worker's re-read after its own compaction has not been observed. |
| **Safe compatible updates** (R11). | **Extended** with the one-time move (R11 November 11): reviewed manual steps; never started by automatic mode; strong tier; receipt written before its fresh-session trials and recording them as pending. **November 13 (3.4):** "Update an installed block" added, with a scripted 3.3-to-3.4 test. | `test_a_3_2_installation_moves_to_the_block_and_keeps_project_content`, `test_a_move_interrupted_before_the_block_is_merged_blocks_with_a_named_gap`, `test_update_guide_documents_the_move`. Scripted file operations only. |
| **New in 3.3, with no earlier counterpart:** what a summary must carry across a break; the visible "Re-entered:" line; the worker's fixed last return line; the check's `next` line. | Block Summaries and Recovery; WORKER.md; `startup_check.py`. | `test_summaries_carry_role_work_and_the_reentry_next_step` and the tests above. Whether a host's summarizer follows the Summaries rule is unobserved. |

**Acceptance-blocking unknowns.** These are open, not smoothed over:

1. Recovery of work still running at a compaction has been observed once, on one
   host, on the reworked build before the final commit's wording changes. No rate is
   implied. Closing the held requests through the store after recovery was not
   reached. The final wording itself has no live run.
2. In that trial the Director ran the read-only store views before reading the
   requests card. The block routes those views through the card; the route's order
   was not followed.
3. Card-read triggers for knowledge and learning remain unproven: one earlier session
   skipped the knowledge card after compaction, and no trial reached a correction or
   a closure.
4. Not verified at all: session resume; repeated compaction; a new conversation with
   work out from an earlier one; another host; a host that does not pass AGENTS.md to
   subagents; a scoped child Director; a worker after its own compaction; a failed
   check followed by a badge-card read; a generated project's first use.
5. No installed project has made the move: not a mature project with its own guards,
   store and role index, and not this source checkout, whose root AGENTS.md still
   selects the 3.2 route by the presence of `.director/START.md` and needs a new
   locator when it moves.
6. Owner confirmation is not recorded for: what 🎬 certifies; the worker
   classification; the roster as standing text; dropping the Director's package
   acknowledgment.
7. The actor-evaluation detail is off the passing path (row above).
8. The legacy v1 engine is unchanged; none of this applies to it.

*November 14 additions to item 5:* this checkout's installation took the move on
November 13 and left this repository for a private sibling workspace on November 14,
where its block route still awaits fresh host trials; this repository's AGENTS.md
has no route left to select ([R14](RATIONALE.md#r14--commit-the-installation-with-the-project)).
"No installed project has made the move" no longer holds: the maintainer's other
local installations took the 3.3 move on November 13, and their fresh-session trials
are pending.

Closed by the final commit of November 11 and removed from this list: a receipt
without a block baseline no longer passes; the SitRep-after-break wording in the
block matches the supervision card and the November 7 rule.

[R10](RATIONALE.md#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)
owns the route decision; [R9](RATIONALE.md#r9--make-attention-and-active-supervision-visible-without-decoration),
[R11](RATIONALE.md#r11--update-from-a-pinned-public-source-without-replacing-project-state),
[R17](RATIONALE.md#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request)
and [R18](RATIONALE.md#r18--start-flat-and-make-learning-an-explicit-bounded-loop)
carry the parts they own. The dated sections below describe the 3.2 route and stay
as history; where they say "starter DIRECTOR", "START" or "OPERATIONS' staffing
section", 3.3 moves that text as this table says.

## Compaction re-entry — November 9, 2026

| Owning purpose and failure prevented | Disposition and active route | Concrete oracle and claim boundary |
|---|---|---|
| R10 Oct 24/Oct 31 and R9 Oct 31: the host-loaded block must reach START and the complete selected package before the first ordinary reply, and 🎬 means a check in this conversation. v1 PATTERN reloaded no-longer-retained instructions; the flat starter dropped that clause without a recorded decision. Observed by the maintainer: after compaction the host reloads AGENTS.md, the agent does not re-read START or the role package, and the startup check, 🎬, delegation and SitReps stop. | **Accept (maintainer request) as the first piece of the larger stopgap a November 7 investigation proposed for the block** (an end-marker re-entry paragraph, summary steering, and explicit-settings and capture-and-split sentences). The installer's bridge and this checkout's guarded AGENTS branch add, after the role and check routing: "After every compaction or session resume, repeat this startup before your next reply. Read the files again; a summary that mentions them is not a substitute." After independent review, four foundation reuse rules stop excusing a skipped re-read or re-check: DIRECTOR treats evidence from before a compaction or session resume as stale, START and WORKER say a compaction summary does not retain instructions and they are read again, and OPERATIONS rechecks facts from before a compaction or session resume. Marker `director-starter:2` retained; starter revision 3.2. Projects already installed get these only when each runs its own update through its own Director. Not included: an end marker or mechanical re-entry test, summary steering, the settings and capture sentences, a host hook, or any checker change. | Live: in a Director session, force a compaction; the next reply follows a fresh read of START and the selected role package, visible in the transcript after the summary, and any 🎬 follows a fresh check. A reply relying on the summary's "read" fails. A compacted worker or scoped child Director re-reads its own package, keeps its role, runs no Project Director check and shows no 🎬. A session resume behaves the same way as compaction in each case. Static: tests pin the sentence, its placement, source/installed parity, the four foundation clauses and the checker's acceptance of the previous and current block. Nothing proves an agent re-reads. Pending ([validation](DESIGN_NOTES.md#compaction-re-entry--november-9-2026)). |

[R10](RATIONALE.md#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)
owns the decision; the **Operational installation truth** row below is the affected
obligation.

## Field report triage — November 7, 2026

An adopting multi-day video project on Director starter 3 (source 9571ff0) hit three
problems; the maintainer routed them here as a problem report, not a change order.
The dispositions were first stored as proposals. **November 7 decision:** the
maintainer approved the four SitRep rows, now implemented in starter DIRECTOR with a
static wording test; live cadence is unverified. The maintainer kept the startup-check
and write-refusal dispositions (decided: no pattern change); the startup trigger-prose
test remains proposed only.

| Owning purpose and failure prevented | Disposition and active route | Concrete oracle and claim boundary |
|---|---|---|
| R9 Oct 17, R17 Oct 27, R18 Oct 31: a labeled 📋 SitRep keeps held work and attention needs visible and shows supervision has not stopped, without the user asking. Field: no labeled report for ~46 hours of notification-driven held work. | **Accept (approved November 7): per-turn due check.** Keep "about every five minutes from actual dispatch (or the agreed interval)". Host hook → START → starter DIRECTOR checks on every turn, including worker returns and notifications, whether one is due, using host timestamps or a clock check, and notes each SitRep's time. After compaction or session resume, report once promptly only if one is overdue or the last time is unknown, then time the next from it; a notification wake-up is not a resume. Tradeoff: when turns arrive further apart than the interval (field: ~220 wake-ups over the ~2-day session), every notification turn is due; that is acceptable only because each then carries at most a brief labeled report. Maintainer's call, approved: the no-time-source fallback (say so once, then report at each user message or held-stream change); rare, since hosts that delegate usually expose a clock. Known risk: under the fallback, reporting at each user message could add a report to rapid exchanges; only the one-line-when-unchanged rule limits that. Reject reporting only at meaningful changes or on request (reintroduces the Oct 27 failure). Defer changing the number: nothing shows it caused the lapse, and the agreed interval already lets a project tune it. | Live: three or more intervals of notification-driven held work with one deliberately stalled stream; the first turn after each interval carries a labeled SitRep naming the stalled stream and what waits on the user. A run of "nothing new" turns spanning a due interval without a SitRep fails. Sparse unchanged turns: notification turns more than an interval apart with nothing changed each carry at most a labeled one-line-per-stream SitRep; a full block on consecutive unchanged turns fails. Compaction/resume: after a compaction or session resume with a SitRep overdue or its time unknown, one prompt report, then the next timed from it — not one per turn; a notification wake-up is not a resume. A user returning after hours without turns gets a prompt report that claims none in between. Pending. |
| R9 Oct 19, R17 Oct 27: a quiet, stalled or unevaluated stream must not vanish, and full blocks must not become noise. The flat starter's compression of legacy DIRECTION dropped those clauses. | **Accept (approved November 7) as restoration:** cover every held stream, including quiet, stalled or returned-but-unevaluated work; one line per held stream, not the full shape, when nothing changed since the last SitRep; between due reports, ordinary prose rather than another full block; and noting each SitRep's time, carrying over DIRECTION's kept due time. Legacy DIRECTION already states these; no new duty. | Oct 19 no-noise: several exchanges and returns inside one interval get direct answers and at most one full SitRep. No held work, no SitRep. No time source: one statement that timing is unavailable, then a SitRep only at a user message or held-stream change; a SitRep on an unchanged notification turn fails. Pending. |
| R9 Oct 17: the exact heading makes reports scannable; R9 Oct 19 keeps them from becoming decoration. Nothing gives a report a consistent shape. | **Accept (approved November 7) as a suggestion, not a requirement:** **Done** · **In progress** (who, what, actual status, next step) · **Waiting on you** (❓ questions, 🖐️ user-only actions, or "nothing") · **Next**, followed (later November 7) by an example table for a full SitRep with Who, Doing, Status and Next step columns; the same columns as lines also work. It presents the existing required coverage: results and evaluated returns → Done; who holds each stream, what it is doing, its actual status and next step → In progress; blockers needing the user → Waiting on you, whose wording now keeps ❓ and 🖐️ visible; next action/proof → Next. Heading unchanged. | A differently ordered report with full coverage passes, as do the example's columns given as lines; a four-part report that omits a held stream, drops who, status or next step for one, or hides a ❓ question or 🖐️ user-only action, fails. Copying the example's names or content instead of the actual actors and work fails. Pending. |
| R17 Oct 27: ordinary progress neither resets nor replaces the report. Field: ~26 one-line "still waiting" notification replies in one window. | **Approved November 7. Reject a silence rule:** the owner did not endorse silence, hosts may render a reply on every turn, and routine acknowledgments already need no extra message. **Add only** that notification replies do not reset or replace a due SitRep; a notification turn is where an overdue one is sent. | Oct 27 case: an informative ordinary update or a notification reply does not reset the clock, and the report arrives unasked. Pending. |
| R9 Oct 17 and Oct 31, R10 Oct 31: 🎬 means a check in this conversation, before the first ordinary reply. R9 Nov 2/Nov 4: strict managed hashes; after setup the ordinary checker alone validates a generated receipt. Hand edits, partial updates, reverts, template syncs, a removed or repointed hook, or a copied project's wrong ID arise between install and use. | **Reject** install/update-time-only checking: installer staging, generated first use, UPDATES and the optional context preflight already check then, and checking only then would make 🎬 the role-only marker R18 declined. **Reject** a separate file-change trigger: knowing a file changed takes the same hash check. Keep host hook → START → DIRECTOR/OPERATIONS → `startup_check.py` per conversation. R10 Oct 30's "repeated checks recreate startup overhead" trigger legitimately fired; triage measured ≈2.4k tokens and under half a second of command time per conversation. START loads only OPERATIONS' installation-evidence section; an agent reading all of OPERATIONS (~14.8 KB here; the field reported 16 KB) spends ≈4k tokens instead, still small. | Existing static tests cover drifted managed files, hook faults, template provenance refused as a receipt, changed project guards not blocking, null-ID generated receipts, the source-checkout branch and worker/scoped-child exclusion. Live: unhinted greeting → reads → check → 🎬, timed; one edited DIRECTOR byte → specific gap, no 🎬; source checkout or worker → no check or badge. One host, first conversation only. Pending. |
| R10 Oct 24/Oct 30: required reads stay reachable; advisory links alone did not finish a read chain in earlier loading trials. | **Defer** splitting OPERATIONS' installation-evidence section into a short per-conversation route (trigger, exact command, pass/block handling, actor evaluation) plus an explicitly triggered install/update/integration/diagnosis part, until the field's first-minutes tool sequence and one post-setup conversation are measured. **Propose** (not applied) a static test pinning the START/DIRECTOR/OPERATIONS first-reply trigger prose before any split. Likely template-local, routed to the adopting template owner: state the exact ordinary check command; keep setup-only manuals out of ordinary guards (hypothesis). | Test oracle: the check precedes the first ordinary reply, including a greeting, without waiting for staffing; failure gives the gap and an answer without 🎬; every checked reply carries 🎬. After any split, a blocked check still reaches the diagnosis text. Neither the test nor a split proves agents still run the check or materially cuts first-conversation time. |
| R2 Oct 24/Nov 3: host observations never become loaded instructions; adapters stay project-owned and conditional. R15: workers write within assigned ownership. R17: a host observation was corrected without prescribing host tools. R18: an unsupported route is a specific gap. | **No payload change.** Workers write files within their assigned ownership (R15) as normal; the field issue is one host's narrow built-in refusal of Markdown files whose names start with four specific prefixes. Starter DIRECTOR resolves return routes from current host controls, OPERATIONS confirms the actual return route and WORKER returns the requested result with check evidence; the v1 assignment template lists text as one deliverable form. Nothing in the pattern names worker outputs with these prefixes; `pattern/engine/ANALYSIS.md` is a v1 role definition agents read and keeps its name. A build-specific list would burden other hosts and go stale; a project on that host can keep the fact in its own conditional host adapter. Held in reserve, not proposed: starter WORKER could add "if the host refuses an assigned write, return the full content and the refusal as text, without working around it." That fallback applies only when a host actually refuses an assigned write. | Live, on that host: a brief naming a `FINDINGS_` file gets the full content plus the refusal, with no rename or shell workaround; the owner saves it verbatim and reads back; a `NOTES_` name writes normally. On another host nothing makes the Director avoid these names. Optional static: pin the return-route sentences; no starter/engine contract carries a prefix list or host product name (README-v1's optional global-skill passage excepted). Revisit if a refused worker routes around the host, returns a summary instead of the content, or content is lost or saved without readback. Pending. |

**Starter SitRep wording — proposed at triage, applied November 7.** Previous
paragraph text in `pattern/starter/payload/DIRECTOR.md` (lines 114–120 at 9571ff0),
kept as history:

```text
While delegated work is outstanding, proactively
send a labeled **📋 SitRep** about every five minutes from actual dispatch (or the
agreed interval), covering actual handles/observations, results, blockers, steering
and next proof. Reserve 📋 for that report heading, not every progress sentence.
Ordinary progress/status answers do not reset or replace it. On
resume, report promptly if overdue or timing is unknown. Stricter host progress
updates stay concise and separate; supported waits must leave both cadences usable.
```

Applied text, now verbatim in starter DIRECTOR. On November 7, after independent
review, the maintainer approved tightening two triage sentences, "When nothing
changed, one line per held stream is enough" and "On resume, or when you cannot tell
when the last one was sent, report once promptly and time the next from it", to the
unchanged-turn and resume sentences below; the earlier paragraph above stays as
history. Later November 7, the maintainer chose to add an example: **In progress**
(owner, actual status) became (who, what, actual status, next step), followed by an
example table. Independent review then added blank lines so a copied example renders
as a table, filled every Next step cell and began the intro "For a full SitRep, for
example". The current paragraph and example:

````text
While delegated work is outstanding, proactively send a labeled **📋 SitRep**
about every five minutes from actual dispatch (or the agreed interval). On every
turn, including worker returns and notifications, check whether one is due, using
host timestamps or a clock check, and note each SitRep's time. Cover every held
stream, including quiet, stalled or returned-but-unevaluated work, with actual
handles/observations, results, blockers, steering and next proof. A suggested
shape: **Done** · **In progress** (who, what, actual status, next step) ·
**Waiting on you** (❓ questions, 🖐️ user-only actions, or "nothing") · **Next**.
When nothing changed since the last SitRep, give one line per held stream, not the
full shape. Reserve 📋 for that report heading; between due reports use ordinary
prose, not another full block. Ordinary progress/status answers and notification
replies do not reset or replace it. After compaction or session resume, if one is
overdue or you cannot tell when the last one was sent, report once promptly and
time the next from it. Without any time source, say so once and report at each
user message or held-stream change instead. Stricter host progress updates stay
concise and separate; supported waits must leave both cadences usable.

For a full SitRep, for example (a table where it renders well; the same columns as
lines also work):

```text
**📋 SitRep** · 14:05

**Done:** outline approved; checks pass.

| Who | Doing | Status | Next step |
|---|---|---|---|
| 🐝 Hive | Draft the setup guide | Returned, checked | Revise after review |
| 🦅 Kestrel | Review the draft | Running, 6 min | Verdict |

**Waiting on you:** ❓ publish now or hold?

**Next:** revise once the review returns.
```
````

**Optional legacy mirror and interaction:** not applied; still the maintainer's call,
recommended because DIRECTION owns the R17 loop and already keeps the due time and the
no-full-block line. `pattern/engine/DIRECTION.md` would add the per-turn check including notifications
with a clock check, noting each SitRep's time, notification replies among what does
not reset the due time, and "A suggested order is done, in progress, waiting on you
(❓ questions, 🖐️ user-only actions or nothing), next."; `pattern/engine/DIRECTOR.md` would
get the per-turn/notification phrase. Starter README, README-v1, site copy and install
docs stay unchanged (same cadence meaning; site publication is a separate gate). The
starter change and the November 5 lighter-tier staffing change both alter starter
DIRECTOR's pinned hash and ship together so installations refresh once. The decision
is recorded by a separate static package test, a dated R17 entry with an R9 note and
the updated **Readable identities and cadence** row below.

[R2](RATIONALE.md#r2--protect-judgment-and-conversation-from-executionbookkeeping), [R9](RATIONALE.md#r9--make-attention-and-active-supervision-visible-without-decoration),
[R10](RATIONALE.md#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes), [R17](RATIONALE.md#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request)
and [R18](RATIONALE.md#r18--start-flat-and-make-learning-an-explicit-bounded-loop)
own the decisions these dispositions refine. [Validation](DESIGN_NOTES.md#field-report-triage--november-7-2026)
keeps evidence, measurements, host fact, hypotheses and pending scenarios. Unknown
affected obligations stay acceptance-blocking.

## Generated-project first use — November 4, 2026

The prior route correctly kept templates uninitialized and checks read-only, but
omitted the executable handoff between actual generation and first-reply checking.
An actual generated code project's greeting/identity startup reproduced that gap.
This later refinement adds one generated-instance setup operation; it preserves
the normal configured-project path and all earlier failed observations.

| Owning purpose and failure prevented | Disposition and active route | Concrete oracle and claim boundary |
|---|---|---|
| R9/R10: a promised future setup cannot satisfy an immediate missing-receipt check. | Opted-in actual generator → fresh INSTANCE bound to copied provenance/root → host hook/START/selected Director and guards → FIRST_USE plus full native I/O/privacy prerequisites → guarded ensure/technical receipt → ordinary read-only checker → actor role/backend evaluation → first reply. | Actual pristine generated project, unhinted native greeting/identity, complete returned reads before ensure, real receipt/check and checked reply. Source wording/fixture setup and later user-prompted repair are not automatic proof. Marker or ensure return alone never earns 🎬. |
| R9/R10: a silent-start metric can conflict with a receiving host's required tool-progress message. | START/DIRECTOR/OPERATIONS permit only an honest unbadged checking preamble required by a higher-priority host; no ordinary greeting/identity answer or setup/completion claim before the check. Ordinary answer/check/authority requirements remain. | Actual Code candidate returned all 13 selected bodies before ensure and gave its first ordinary greeting with 🎬 after a separate matched check. The zero-visible-message metric failed; commentary came after initial reads, and a wrong extra STATE guard was corrected in the same turn. These qualifications remain, without a universal silence or full-procedure claim. |
| R9/R16: completed startup skips ensure, so helper-only receipt validation can be unreachable. | Preserve the receipt-present read-only caller; startup_check conditionally validates generated receipt format/backend/claims and actual native ID/format. Existing receipt formats retain their route; no new writes or caller change. | Direct ordinary checker rejects null/missing native ID, contradictory custom contract/identity and unsupported acceptance/warning claims without writes. Independent source/CLI checks passed; actual Code candidate first-use proof is qualified, while final installed Release/default-path proof remains open. Candidate observations do not prove uptake of every final wording change. |
| R10/R16: generic seeds, arbitrary missing receipts or existing stores can be mistaken for pristine generated projects. | Require reviewed first-use integration plus actual generated-instance evidence. Generic seeds contain no INSTANCE/config/state/receipt. Missing/damaged provenance, existing state without verified owned intent and unknown integrations remain gaps; no fresh installer over copied integration. | Seed ensure refuses without writes; missing receipt alone allocates no identity; existing/moved/configured project reuses its real identity/receipt. Worker/scoped child neither initializes nor badges. Preserve unknown/mature data. |
| R3–R6/R14/R16: first setup can duplicate identity, bypass canonical/privacy gates or replace a custom backend. | Native bundled init/validate only for verified pristine instances; custom contract route creates no bundled store. Full selected manual/index/privacy gates remain. Narrow locked owned-attempt recovery preserves intended identity and exact bytes; no stale-lock deletion or whole-directory replacement. | Two generated projects get distinct IDs; repeated/concurrent/interrupted ensure retains one identity. Conflicting state fails rather than rebaselining. Custom/video route retains its backend/private rules; canonical requests/walks contain no user records, permitting only exact reviewed empty .gitkeep placeholders and structural directories. Reviewed noncanonical journal/team seeds may match baselines. Existing assets, guards and opt-outs survive. November 9: that video template's three large docs become unbound managed files (60 to 57); the hook, remaining-guard, tracker-contract, empty-seed and journal/team-seed bindings stay, and the shared helper is unchanged. Decided and staged, not applied or verified live ([R16](RATIONALE.md#r16--separate-replaceable-engine-from-project-owned-integration)). |
| R9/R14/R18: transport or technical metadata can falsely imply acceptance, warning delivery or a successful native first reply. | Keep original transport provenance separate; write technical setup evidence only after actual checks, with native/human acceptance unrun. Normal later conversations use the ordinary read-only command. No setup actor, source capture, Git init/push, policy seed or Stop activation. | Actual second conversation has no reinitialization; checker failure or authority conflict gives a specific gap/no badge. No copied completed receipt, marker-as-badge or fabricated privacy-warning delivery. Native first-use proof and downstream publication/adoption remain separate. |

[R9/R10/R14/R16/R18 rationale](RATIONALE.md#r9--make-attention-and-active-supervision-visible-without-decoration)
owns the dated scope refinement; [validation](DESIGN_NOTES.md#generated-project-first-use--november-4-2026)
must retain deterministic and actual native outcomes separately. Unknown affected
obligations remain acceptance-blocking. Bounded candidate results are recorded; final
installed Release/default-path proof remains required for whole acceptance. A qualified
source release can precede that separate installed-route gate.

## Bounded context and Stop prototype — November 4, 2026

The selected repair preserves the previous recommended flat and legacy routes.
It restores positive attention instructions, adds one optional byte calculator,
and keeps the stopping experiment in development outside installation manifests.
The existing continuation API is deliberately unchanged. Implementation, independent
review/checks and native qualification remain separate acceptance questions.

| Owning purpose and failure prevented | Disposition and actual route | Concrete oracle and claim boundary |
|---|---|---|
| R9: reserved names alone can leave actionable questions and user-only steps unmarked. | Preserve existing semantics. Host hook → START → flat DIRECTOR now positively commands ❓ questions/decisions and 🖐️ user-only actions; legacy DIRECTION already supplies that route. Grouped/tool-card handling, checked 🎬 and heading-only 📋 SitRep survive. | Actual question, grouped/tool question and physical/authentication step use the appropriate marker without chat duplication; ordinary progress gains none. Source wording is implemented; this delta has no observed marker-uptake trial. |
| R10/R18: complete-read prose cannot restore an automatically omitted entrypoint. | Preserve complete selected/manual reads and recovery. Optional installation/update/route-change OPERATIONS → `.director/context_check.py` uses explicit caller-resolved counted chain, raw bytes, required prefix boundaries and cap evidence; no new first-reply call. | Exact cap vs one-byte overflow; later pointer cut/omitted; early required boundary fits despite total over; multibyte counts and unsafe/mutated inputs. Unknown cap ignores a number, default is conditional, effective is caller-declared. All reports retain actual admission unqualified; host discovery/overhead/injection/consumption/compaction are not verified. |
| R3–R6/R17: compact recovery can lose exact intent, accepted partials or terminal parents. | Preserve the existing native Store/API `continuation` with explicitly bound terminal IDs, immutable source reads and legal lifecycle/recovery. Defer another recovery/source-locator API, packet registry or backend replacement. | Done parent + completed children + recorded remaining work stays recoverable. Latest malformed/stale checkpoint and native journal/source errors stay gaps. A clean checkpoint still cannot establish semantic completion or cause execution. Earlier recorded-data checks remain scoped evidence, not a new native result. |
| R17/R18: a falsely all-complete checkpoint can hide an unfinished adopted outcome at voluntary Stop. | Optional `development/prototypes/stop_guard.py`, outside manifests, takes explicit session/root-owner/task/source binding and a trusted bounded snapshot command; optional evaluator sees source/task facts and attempted final, including terminal/all-complete cases. No cwd/backlog task inference or enabled host config. | Injected snapshot/evaluator commands must carry unfinished final + false-done state to evaluation, block a supported continue verdict once, and distinguish full pause from an experiment hold with independent work. Stubs prove protocol plumbing only; structural-only checks miss false-complete intent. Real backend bridge, semantic accuracy and native continued action remain unqualified. |
| R5/R9/R17: corrective prompting must respect genuine exits and avoid looping or canceling a child return. | One atomically persisted correction per session/stable binding; no turn/checkpoint/source/final rewrite reset, automatic replenishment, task writes or wakeup. Stop-only root scope; fail open for missing/corrupt established state, source/command unknowns and exhaustion. | New turn IDs and repeated Stops stay exhausted; true pause, sufficient completion and correct child return allow. Missing state never creates fresh budget. Stop alone establishes neither interrupt latch nor genuine-user authenticity; native interruption/synthetic-prompt handling require receiving-host proof. |
| R7/R10/R11/R14/R18: new packaging must not make existing duties transitively unreachable. | Keep hook/START/selected guards, staffing/manual-read triggers, native canonical I/O, recovery/SitRep loop, UPDATES, LEARNING and touched-role upkeep at their current triggers. No new global skill/config/role framework, tracker, manifest-installed Stop guard or default activation. | Existing startup/checker compatibility and manifest boundaries stay intact; downstream adaptation, backend, source/privacy, caller aliases and independent/human gates survive separately reviewed adoption. Unknown affected obligations block the claim; source publication alone cannot establish installation or prevention. |

[R9](RATIONALE.md#r9--make-attention-and-active-supervision-visible-without-decoration),
[R17](RATIONALE.md#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request)
and [R18](RATIONALE.md#r18--start-flat-and-make-learning-an-explicit-bounded-loop)
record the dated intent dispositions; [validation](DESIGN_NOTES.md#bounded-context-and-stop-prototype--november-4-2026)
records returned evidence. No exact future published pin, local adoption, hook
activation or release acceptance is inferred from this plan.

## Whole-result evidence and checked display — November 4, 2026

The previous route already retained Director accountability for the whole result
and a checked reply prefix. This candidate makes evidence reconciliation and display
operational while giving qualified local judgment useful bounded consequences.
It changes instructions, not the checker, backend, role values or host controls.

| Owning purpose and failure prevented | Disposition and active route | Concrete oracle and claim boundary |
|---|---|---|
| R1/R2/R17: green component returns can leave the requested complete behavior failing. | Preserve whole-result accountability. Flat DIRECTOR and legacy DIRECTION compare intended result, combined evidence, user reports and unresolved failures at planning/meaningful returns; runtime claims identify user entry, observable result and substituted/bypassed parts. | With green harness results and contrary user reports, identify the missing journey, retain valid partials and keep whole-result acceptance open until the conflict is resolved or accurately qualified. The reported harness bypass is screenshot evidence, not independently established product code behavior. |
| R2/R15/R17: repeating narrow repairs can conceal an inadequate strategy or proof. | A mismatch/repeated unresolved failure triggers reassessment before another narrow fix. Choose the smallest suitable proof, including known-bad/regression comparison when useful; existing tiers and real project gates remain. | A test that bypasses the failing path cannot establish that path's repair. A suitable regression distinguishes known-bad/repaired behavior; a small task does not automatically gain a full end-to-end suite. Source text is not observed uptake. |
| R1/R2/R10/R18: retained final accountability must not make the Project Director a serial approval router or restore compulsory managers. | Flat DIRECTOR/OPERATIONS, legacy DIRECTION/ASSIGNMENT and flat RECORDS entrust local decisions, permitted next actions, bounded rework, real escalation and actual return routes. Evaluate reasons, coverage and exceptions without repeating every check. Keep optional scoped Director/Request Manager and required review independence. | Multiple independently cleared branches advance through already-authorized phases without new per-file tokens. Backend/privacy changes escalate; substantive authors do not self-review. A small coupled task remains flat. Final canonical/user-facing acceptance stays with Project Director; no new `accept` authority/schema. |
| R9/R10: prerequisites that merely permit 🎬 can leave checked replies unmarked. | Existing emitted hook reaches START/DIRECTOR; those and OPERATIONS positively require every checked Project Director user-facing reply prefix, including discussion/status. Legacy Director/DIRECTION/IDENTITIES display callers agree after their actual selected setup route. | A real initial check and role/guard/backend evaluation pass, then ordinary status/discussion replies retain 🎬. Missing/stale evidence uses the currently possible check; actual failure/semantic conflict gives specific gap/no badge. Worker/scoped-role exclusions and higher-priority host formats remain. Badge is not product acceptance. |
| R3–R7/R11/R14/R16/R17/R18: new default guidance must not erase custody, recovery, privacy or continuing obligations. | Keep selected-read barriers, native canonical I/O, exact sources, seven-state lifecycle/terminal recovery, human gates, real updater/learning/upkeep triggers and managed/project boundaries unchanged. Existing hooks already reach the affected contracts; no extra hook, checker or startup actor is required. | Completed children/falsely done parent still require actual source/obligation reconciliation and useful authorized continuation. Partial holds stay scoped; actual pause/sufficient bounded result remains a valid exit. Old receipts, private evidence, caller aliases and target adaptations survive later reviewed adoption. |

Actual flat route: host hook → START → selected DIRECTOR/WORKER and project guards;
OPERATIONS before staffing and native I/O manuals before canonical operations.
Legacy selected Director/Request Manager → DIRECTION/ASSIGNMENT retains the v1
Recorder/setup route; this change does not silently replace it with a flat checker.
The new local-decision contract uses existing assignments, receipts and notes.
No new universal reviewer, manager, end-to-end suite, model exemplar or tracker is
introduced. Independent review must examine the actual callers and purposes, not
just a green test count. Unknown affected obligations still block the claimed scope.

[Owning rationale](RATIONALE.md#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request)
and [validation](DESIGN_NOTES.md) distinguish implemented candidate instructions,
source checks, actual behavioral observations and later publication/adoption.
The original reported failures and prior partial/native evidence remain intact;
no source wording pass establishes a runtime cure.
The [constructed scenario set](fixtures/whole-result/README.md) supplies concrete
counterexamples; its proposed sequences are not executed application evidence.

## Portable reconciliation and composed project guidance — November 2, 2026

The prior recommended route already supplied role selection, executor loading,
validated records and supervised return evaluation. This repair preserves them and
addresses two narrower gaps: treating a composed project file as immutable managed
payload, and recovering an unfinished parent after all children finish or its record
is falsely terminal. The original purposes remain the acceptance unit.

| Owning purpose and failure prevented | Disposition and active route | Concrete oracle and claim boundary |
|---|---|---|
| R9/R10/R16: a meaningful checked identity must distinguish installed method integrity from evolving project authority. | Strict hashes remain for managed START/DIRECTOR/OPERATIONS/checker. Current AGENTS/selected project guards are read safely and historical drift disclosed; one supported marked route must reach selected START. The explicit project-relative `--hook-source` defaults to AGENTS; outer AGENTS and actual selected host/shared guards remain required, with no automatic search. OPERATIONS requires complete current actor authority/compatibility evaluation. | Appended unrelated build guidance reports changed snapshot without false managed-integrity failure. Managed tampering, malformed/misdirected hook and unsafe paths still fail. An intact hook with conflicting surrounding authority still prevents the actor's badge. Structure/hash tests do not prove consumption or semantic compatibility. November 9: a template-local narrowing for the My Work video template takes its large video docs, TEAM and TEMPLATE off the selected guards as task-time reads; this rule is unchanged for the remaining guards. Decided and staged, not applied or verified live ([R9](RATIONALE.md#r9--make-attention-and-active-supervision-visible-without-decoration), [R16](RATIONALE.md#r16--separate-replaceable-engine-from-project-owned-integration)). |
| R11: preservation must survive an update even when current equals an old snapshot or legitimate project guidance has changed. | The R9 distinction does not waive UPDATES' pinned baseline/current/incoming and prior-upstream adaptation review, backups, actual backend/authority or affected route gates. | Preserve legitimate project guidance and selected hook through update; unknown managed drift or incompatible routing remains unresolved. Never rewrite a receipt to silence project drift. |
| R2/R17/R18: whole delivery must survive worker/milestone completion and status answers. | DIRECTOR/DIRECTION retain adopted obligations and next action/wait at meaningful source/return reconciliation. The implemented bounded continuation view/checkpoint uses the existing native store, including explicitly selected terminal IDs. | Completed children + falsely done parent + recorded remaining authorized work must remain recoverable and cause actual continuation before voluntary yield. Status reply, launch count or done flag alone fails. Pause, genuine wait, correct child return and sufficient bounded completion remain legal. Fifteen independent installed-CLI cases verify recorded-data behavior below; actual-host uptake remains unqualified. |
| R3–R6/R17: exact intent, accepted partials and native recovery must survive a new compact view. | API's existing capture/source, requirement trace, legal lifecycle, native I/O prerequisites and sole canonical backend remain; ordinary checkpoint notes add no schema or mutation authority. | Source-frontier mismatch/newer malformed checkpoint/missing note/pending transaction yields its actual gap; terminal inclusion never auto-reopens, accepts or declares intent complete. Corrupted sources retain native refusal. |
| R10/R15/R18: atomic maintained responsibilities need a small caller interface and complete executor instructions across authorized transports. | Keep ROLES/ASSIGNMENT and flat OPERATIONS' existing selection/authority versus task-manual split. Concise flat DIRECTOR and legacy ASSIGNMENT additions make transport-independent responsibility, authorized source subset/access and actual return explicit. Existing canonical recording/handoff authority remains; no four executed integrations are claimed. Explicit role/scope/access/return apply independently of ancestry. | A nested route restriction still reaches selection; the caller avoids unrelated craft manuals; a separate-session worker stays bounded. Unsupported cross-harness access is a transport gap, not simulated dispatch. No new mandatory registry/resolver/actor. |

Transitive obligations remain on the active route: host hook → START → exact
DIRECTOR/WORKER and project authority; OPERATIONS before staffing; actual canonical
I/O protocols before state/knowledge queries; DIRECTOR/DIRECTION recovery and labeled
SitReps for held execution; UPDATES for due active-session discovery and safe changes;
LEARNING for bounded review/deferral and matching uptake. Existing source/relationship/
revision/journal semantics, explicit lean/v1 choice, privacy opt-outs, stable caller
aliases, managed/project ownership and independent/human gates remain. No new
universal startup history scan, global skill, Stop guard, scheduler, migration or
host-liveness guarantee replaces them. Unknown affected obligations remain acceptance
blocking; unrelated unrun host claims do not become new deterministic source gates.

The [owning rationale](RATIONALE.md#r17--keep-delegated-work-supervised-and-recover-the-users-whole-request)
and [validation record](DESIGN_NOTES.md#portable-reconciliation-and-composed-project-guidance--november-2-2026)
separate accepted repair direction, implemented code, focused checks and unqualified
native behavior. Independent review must compare source intent with claimed closure,
including a terminal parent; it cannot accept only current open-count fields.

Context-delivery qualification remains separately open. For the actual affected route,
retain automatic discovery/override chain, raw bytes/required entry boundary and cap
provenance as known, default-only or unknown, plus required query/access controls and
actual returned read coverage. A disk inventory can flag a known oversized chain;
it does not establish effective Desktop admission or consumption. Existing bounded
progressive reads and aggregate-output/truncation recovery remain mandatory. The
continuation/checker repair supplies no native injection or compaction guarantee.

## Delegation exception correction — November 1, 2026

**Later execution-order correction, under evaluation:** A fresh installed review
loaded the intended role/operational route and still did the work without a child
call. The candidate now requires bounded dispatch before detailed investigation,
review or changes; scoping, ordinary discussion/simple lookups and acceptance stay
direct. This preserves R2's protected attention and R10's role boundary. A real
child must execute and return before parent acceptance; after-the-fact staffing is
not the oracle. Internal misclassification remains a hypothesis, not a proved cause.
The earlier failed observation remains negative evidence even if a retry passes.
Follow-up actual dispatches did not satisfy the full package oracle: required
staffing/role reads and child startup/knowledge access were incomplete. The next
candidate moves the existing staffing step before dispatch, supplies required
instructions/knowledge or retrieval access, and returns read-scope conflicts before
affected worker action. The complete guarded sequence, not a launch count, is the
acceptance unit; restrictive earlier harnesses remain distinct from normal host
capability and from the newly clarified instruction route.
The subsequent bootstrap clarification distinguishes a role assignment from an
ordinary task, states the default role in the actual adopted hook, and explicitly
orders returned instruction reads before dependent commands and canonical I/O
instructions before knowledge selectors. This preserves R10's selected-role route
and R6's native wire/record guards; it adds no read-only exemption. Actual final
integration cases must observe those steps, with required source material genuinely
accessible; a changed harness is not an unchanged-settings causal comparison.
For shared instruction files, the update route also requires the explicit role
default/delegation request in the actual AGENTS/CLAUDE entrypoint. Literal target
entrypoint inspection is the oracle; preserving only a referenced request is not
equivalent under a host rule that names AGENTS.md. Detailed role/authority files
remain canonical and target-specific adaptations remain preserved.

**November 9 (starter 3.2):** the starter update route now keeps the role default,
bounded-subagent request and marked block in AGENTS.md (or the hook source the
project's check selects); a CLAUDE.md the host loads, on a host that expands its
imports, becomes only an import of AGENTS.md, with its other content moved into
AGENTS.md and no second Director paragraph. An import is loaded text, so the
literal-entrypoint oracle above still holds. Where the host does not expand imports,
the request stays in CLAUDE.md and the gap is reported. The update backs up and
verifies each startup file it changes and reports, rather than moves, content of
unclear ownership or for only one host. Oracle: in an updated project CLAUDE.md is
exactly `@AGENTS.md`, AGENTS.md holds one marked block and the startup check passes.
**Open gap, next to the v1 update gap in the Safe compatible updates row:** the v1
engine guide is unchanged legacy, so a v1 update route can still recreate the
duplicate Director paragraph in CLAUDE.md. Wording and checker fixture only; no
project updated ([R10](RATIONALE.md#r10--assign-roles-explicitly-preserve-project-ownership-across-entry-routes)).

The prior recommended flat route already requested useful delegation, but its
"when permitted" wording and opt-in WORKER sentence left a failed interpretation
unresolved. An installed actor subsequently acknowledged that its loaded AGENTS.md
already satisfied the host's exception; it had wrongly required another user request.
This is distinct from an actual higher-priority prohibition or missing capability.

| Owning purpose | Current disposition and active route | Concrete acceptance oracle |
|---|---|---|
| R2/R15: keep substantial execution in bounded workers while the owner remains available. | Preserve the mechanism: emitted AGENTS hook positively requests subagents, DIRECTOR requires substantial analysis/project changes to use them, WORKER uses useful independent subsets within scope. No new actor layer. | A fresh affected-model project-change request without a delegation hint actually launches a bounded worker and evaluates its returned evidence; an applicable project-instruction exception is not rewritten as user-only permission. |
| R10: obey actual host authority and report unavailable routes without silently changing roles. | Preserve: the loaded hook directly requests subagents; the foundation retains a short specific blocked-route/stop boundary. Debugging/host-exception explanations stay in maintainer rationale. | A real user-only prohibition or unavailable tool produces a truthful gap and no substantial Director implementation. A tool listed on disk alone is insufficient. |
| R1/R18: keep ordinary conversation direct and avoid compulsory organization. | Preserve: direct discussion, critical judgment and narrow validated recording remain Director duties; optional specialized actors stay in the detailed foundation rather than the delegation hook. No new startup file or manager. | An ordinary discussion answer stays direct; a project change does not get implemented by the Director merely because no department exists. |
| R1/R18: one accountable flat owner can accept a worker result without inventing a manager. | Correct RECORDS' contradictory no-owner-acceptance sentence: Project Director evaluates and accepts the whole submission; workers/scoped children submit. Human and required independent gates remain. | One Project Director + worker reaches review→acceptance; a pending human gate still blocks; a child cannot self-grant project acceptance. |
| R9/R10: checked Project Director identity and complete reads must not depend on implicit role selection. | Clarify hook/START for default and explicitly selected Project Directors; worker/scoped-child exemption stays. Shorter START retains individual/aggregate output bounds, contiguous EOF reads, recovery/stop and no hash-as-read substitution. | Default/explicit root check, worker/child skip; truncated combined output is recovered completely before dependent work. |
| R9/R17/R18: recognize live actors without mandatory roster bookkeeping. | RECORDS keeps assignment identities, actual handles and project-required existing roster; it does not create a flat roster/cursor. | Stable worker name/handle without roster allocation; an existing required roster remains intact. |
| R11: discovery is real, throttled and independent of the greeting's local check. | Keep due discovery for supported background execution or the next active project-work step; retain 24-hour failure window/policies, exact updater root and reviewed-pin recovery for unknown provenance. | Greeting has no network; an observed due check respects the window; unknown provenance cannot be promoted or fixed by resetting cache. |
| R6/R7/R18: short action instructions must retain compatibility/recovery guards. | Remove migration/implementation anecdotes while retaining incompatible-format refusal, reopen-after-stale-instance rejection including init, and untyped-note quarantine/replay. Knowledge query matching and wire/protocol phases remain unchanged. | Existing store/fence, unclassified-note and daily-discovery fixtures remain applicable; no backend/state/schema/wire change. A guessed selector miss still grants no exemption. |
| R8/R10/R16: explicit package selection must survive renamed guides and distinct formats. | V1 adoption/lean links explicitly select README-v1/INSTALL-v1/manifest; legacy pre-engine transition excludes starter 2/3. PROJECT keeps ownership at startup and phases the complete boundary manual before layout/install/update action. | Literal v1/lean links retain their package; starter 3 stays on its own route; unknown formats stop. Required boundary text is read before later engine changes. |
| R15: shared ownership and recoverability should support useful delegation, not require implicit Git setup. | Dated narrow supersession removes Git as a delegation prerequisite; retain one shared tree, bounded file/resource ownership, verified pre-write backups and truthful recovery limits. | A useful disposable non-Git implementation uses actual subagents and evaluated output without Git init/worktrees; recovery limitations stay explicit. |
| R8/R12: the agent front door must reach the selected canonical method without imposing another package's organization. | Replace duplicated v1 instructions with actual package/manifest/protocol selection, preserve exact install/verify/update requests and correct the dead discovery link. Release/source/deployment claims remain separate. | All canonical agent pointers resolve to real files; copied requests stay exact; selected flat work does not acquire compulsory v1 roles; public build remains allowlisted/private-state-free. |

The [validation record](DESIGN_NOTES.md#delegation-exception-correction--november-1-2026)
separates source-route checks, actual emitted tool calls/returned results, and
independent review. Static wording checks and earlier greeting/badge passes do not
establish this worker-execution behavior. No change to request custody, native
backends, status folders, update discovery or learning protocols is implied.

## Why each mechanism existed, and the new route

| Obligation and original reason | Flat route / deliberate difference | Evidence and remaining proof |
|---|---|---|
| **Complete exact sources** (R3/R6): interpretation can omit independent obligations or corrupt tiny steering; original attachment custody matters. | Capture one immutable UTF-8/source+attachment bundle, link each finishable outcome to it, append new sources for corrections. Director/API require capture before dependent work and reconcile all source obligations. | Exact established backend, installed CLI regressions for binary/CRLF/shared outcomes/earlier-source corruption. Actual new-package decomposition and meaningful scope/owner/evidence still need observed actor/recovery checks. |
| **Request-local folders** (R6, [storage comparison](REQUEST_STORAGE_COMPARISON.md)): assets/evidence must travel with lifecycle; large outputs/shared originals remain canonical. Seven states map to three containers; paths are locators, IDs are identity. | Same request.md bundles, assets/evidence hashes, seven-state transitions and ID resolver. No flat state.json replacement or raw folder moves. | Established backend with the reviewed stale-lock/configuration fence plus installed attach/move/replay tests. Physical folders alone do not prove useful requirements or real delivery; no power-loss/OS durability guarantee. |
| **Graph and independent ownership** (R4/R5): grouping/shared source is not a required dependency; 3 completed siblings must stay done while a fourth waits externally. | Same typed links, cycle/required-success enforcement, proposed/requested/acknowledged/returned/accepted handoffs. Parent retains source acceptance; no mirrored foreign tree. | Installed dependency/handoff regressions and separate source/foreign identities; actual permitted transport/acknowledgment and current remote liveness remain host-supplied facts. |
| **Plan, human gate and acceptance** (R2/R3/R5): a title/status is not a complete brief; submission and trusted evidence differ from accepted outcome. | Director records substantive per-outcome owner, acceptance/human gate and execution binding, then submit→review→owner acceptance; active accept rejects. Legal requeue/revise/reopen/amend/replan preserves initial history and unaffected work. | Permanent regressions check retained old plan and latest truth, terminal addendum refusal, earlier-source verification and required human proof. Backend validates declarations, never authenticates human identity, authority or evidence truth. |
| **Retention modes** (R3): short/creative work still contains commitments; lean is an explicit reduced-retention choice, not inferred from project type. | Starter3 installer provisions tracked only. Explicit lean remains available through the retained legacy installation/existing-tracker route; no automatic mode switch or new backend on a mature tracker. Preserve/reconcile unfinished commitments before a separately authorized mode change. | This is a declared installer boundary, not parity of lean installer options. No unsupported lean helper operation or full-backlog promise is claimed. |
| **Parent/requirement trace** (R17): decomposition must not lose parts of the user's request on restart or child return. | Compact assignment/note artifact carries stable parent/local project/request IDs, requirement IDs, owner, actual handle/dated observation, evidence/pending reason and return backreferences. Update at meaningful steering/evaluation; no mandatory new schema or task tree. | API/Director/Worker before-dispatch/return obligations; actor trace and fresh recovery must inspect substantive trace, not just presence of fields. Static prose is not uptake proof. |
| **Crash/retry/serialization** (R6/R14): relocating a folder and replacing its record is not atomic; two writers must not guess a failed result. | Same expected revisions, UUID event IDs, journal and explicit recovery; read-only commands refuse pending intent. Requests wrapper supplies the correct actual root. | Installed fault/replay/CAS tests; collisions/uncertainty preserved. Locks are cooperating same-machine controls, not authentication, cross-host atomicity or uninterrupted supervision. |
| **Cross-machine continuity** (R14): clones need the same identity, originals, backlog, roles and receipts; counters collide across machines. | Fresh durable config/requests/sources/receipts are Git-eligible; only scratch/locks/cache/backups local. UUID suffixes stay. One machine writer, commit/push/pull under actual authority; same-record divergent edits require preservation/reconciliation. | Clone/unique-ID/conflict fixtures required, not a claim that an installation commits or pushes automatically. Templates omit initialized identities/state. Existing private stores/ignore choices remain untouched. November 14: this repository's own ignored installation, which reached no clone, other machine or backup, moved to a private sibling workspace. There it is tracked and pushed to a private remote, with backups, scratch, locks and the update cache local; the move is hash-verified. The public cleanup's push and the live trials are pending ([R14](RATIONALE.md#r14--commit-the-installation-with-the-project), [validation](DESIGN_NOTES.md#maintainer-installation-moves-to-a-private-sibling-workspace--november-14-2026)). |
| **Privacy awareness** (R14): deletion cannot undo public exact-source history. | Once-only public/unknown-remote warning at setup/first capture, recorded only after actual delivery; private verified remote needs none. Unknown visibility is not private. Installer reports pending awareness, not fake delivery. No-Git continuity limit visible. | Git eligibility/opt-out/awareness fixtures; actual host visibility and user notification separately observed. Restores R14: starter2's private default was not an authorized supersession. Never force-add/unignore mature records. November 9: the My Work video template's local-only choice (requests, walks, journal and team activity kept out of Git) is recorded as the template's dated choice; the warning becomes due when a remote that is not verified private is added ([R14](RATIONALE.md#r14--commit-the-installation-with-the-project)). November 14: the maintainer's installation now lives in a private sibling workspace whose remote was confirmed private before its first push, so no warning is due. This public repository holds no installation, and its ignore lines for `/.director/` and `.reference/` stay as a guard ([R14](RATIONALE.md#r14--commit-the-installation-with-the-project), [validation](DESIGN_NOTES.md#maintainer-installation-moves-to-a-private-sibling-workspace--november-14-2026)). |
| **One conversational owner / protected judgment** (R1/R2/R17): implementation/clerical coordination must not monopolize conversation or leave work unsupervised. | Flat Director + useful bounded workers; validated owner state operations replace compulsory Recorder. Optional same-base outcome Director when real coordination warrants it. A child acknowledgment does not end parent supervision; only real authorized independent transfer/exit does. | Earlier assigned-host utility evidence remains historical; new-package steering/recovery and return evaluation need observed checks. No universal cost/latency win, perpetual actor or wakeup. November 7 partner rule: starter DIRECTOR tells the Director to map a request onto the project's established mechanism and owner, say so and recommend that route when a literal reading would bypass it, and pause conflicting in-flight work before recommending a better route; it adds no actor, hierarchy or approval step. After independent review the recommendation is marked ❓ as a user decision, the bypassing or paused work is held until the user chooses while independent, unaffected work continues, the user's choice stands within project rules (a forbidden literal route gets the permitted route or the 🖐️ action), and DIRECTOR points to reading the whole UPDATES guide before planning any update. Oracle: a rollout request becomes a session per project with no outside writes; a mid-flight better route pauses conflicting work first, then is recommended on merit as a ❓ with unaffected work continuing; a buried recommendation or resumed conflicting work fails; a request that already fits proceeds without a detour. Wording only, independently reviewed; live behavior unverified ([R1](RATIONALE.md#r1--one-accountable-conversation-without-a-forced-organization), [validation](DESIGN_NOTES.md#partner-rule-and-explicit-dispatch-settings--november-7-2026)). |
| **Readable identities and cadence** (R9/R17): user must recognize who holds work, actual attention needs and overdue supervision. | 🎬 operationally checked Project Director; fitting **emoji Name** actors, stable through continuation/parent summary, no identity roster. **📋 SitRep** about five minutes from dispatch independently of short host updates; from November 7 the starter checks on every turn, including notifications, whether one is due, covers every held stream and suggests Done · In progress (who, what, status, next step) · Waiting on you · Next, with an example table for a full SitRep. ❓ actual decision/question; 🖐️ actual user-only action. | Contract restoration; actual five-minute cadence unproved until an observed held-work interval. The November 7 per-turn check, coverage and shape are implemented in starter wording and still unproved live. 🎬 retains its checked-installation meaning via a light direct current-conversation owner check; an unverified role acknowledgment has no badge. A role-only marker was considered and not accepted as the default. It never proves live work or accepted delivery. November 11 (starter 3.3, on a branch, not accepted): 🎬 means the check passed since the last break and the actor confirmed the check's listed items; it no longer claims startup-file reads. The cadence sentence is duty 6 of the AGENTS.md block and the rest of the SitRep text is on the supervision card ([dated section](#standing-block-and-cards--november-11-2026)). |
| **Capability/effort and proportional verification** (R2/R10/R15): avoid blindly inherited strongest settings or underpowered cheapest execution; independent review cannot merge into builder. | The Director staffing route resolves current host controls, reliability/budget/context/permission/capacity at use; requested/tool-selected/effective-or-unknown evidence. Smoke/Focused/Full by risk/reversibility/audience, specialized authority and independent actors preserved. November 5: a strong tier stays the default; occasionally a lighter tier at high or extra-high effort, or the strong tier at medium, fits small, well-specified, easily checked work; evaluation and required independent review are unchanged at every tier. | OPERATIONS + explicit assignment contract; real host choice/incomplete-read/settings observations needed. The initially partial WORKER-descendant route was repaired in validation-v4 with an explicit OPERATIONS/selected-guard trigger; a real bounded worker then loaded that package completely before dispatching its child. Role labels are neither model IDs nor sandboxes; no fixed vendor/pricing or invisible control support. The November 5 posture is starter wording only, pending live observation. November 7 (supersedes the inherited-by-omission gap): the flat rewrite had dropped v1 MODELS' explicit-instruction and no-silent-inheritance sentences, and an audit saw 9 of 12 early workers inherit the strongest tier at top effort (~74% of subagent output tokens). Starter OPERATIONS and DIRECTOR now require both capability and effort on every dispatch wherever the host allows, including hosts that reserve them for explicit instructions (the guidance is that instruction); the strong default is the strong tier at high effort chosen at dispatch; top levels only for hard diagnosis, conflicting evidence or consequential review; each choice recorded with a one-line reason, and "inherited/not set" only with the forcing host constraint. Oracle: a lookup-only dispatch sets an explicit lighter tier and effort with a reason; a receipt "inherit; not set" without a host constraint fails review. Wording only, independently reviewed; live dispatch behavior unverified ([R2](RATIONALE.md#r2--protect-judgment-and-conversation-from-executionbookkeeping), [validation](DESIGN_NOTES.md#partner-rule-and-explicit-dispatch-settings--november-7-2026)). |
| **Role discovery and touched knowledge upkeep** (R7/R10/R17): existing specialties/accepted facts must reach the next task; stale selectors cannot describe shipped artifacts as pending. | Project-owned canonical discovery; staffer reads complete selection/authority guards, executor reads task manuals before action. At meaningful closure refresh touched role/runbook/current guide/artifact pointers independently of learning threshold, preserve dated reasons, verify next relevant use. Keep old caller aliases reachable on reviewed update. | Affected-use/next-use checks and preservation mappings required; no global startup catalog, role census, arbitrary cap or automatic department creation. Unqualified local requirements remain until reviewed rephase. November 11 (starter 3.3, on a branch, not accepted): a project-owned roster summary, or a pointer to the project's existing role index, is standing text in the AGENTS.md project section; the staffer still reads the selected role file's selection and authority part before dispatch ([dated section](#standing-block-and-cards--november-11-2026)). |
| **Operational installation truth** (R9/R10/R16): a hook/receipt can falsely imply loaded instructions or supported capabilities. | Direct owner checks/evaluates selected complete route, relevant payload/links/drift/config/receipt and states actual gaps separately. No setup actor; unchanged checks reused. Foundations/deferred guides replace bridge/index/engine read ceremony; authority survives. | File checks do not establish native unassigned cold startup. Missing/truncated instructions must stop affected action, with recovery. Assigned trials may retain ambient source-host contamination; no blanket startup pass. November 9: the bridge asks for the full startup again after every compaction or session resume, since a summary that mentions the files is not a re-read, and the foundations' reuse rules treat evidence from before a compaction or resume as stale ([dated entry](#compaction-re-entry--november-9-2026)); live re-entry pending. November 11 (starter 3.3, on a branch, not accepted): the Director's rules are the marked block in AGENTS.md, checked against a recorded block baseline; START and DIRECTOR are redirect stubs; the actor-evaluation detail is on the badge card, off the passing path ([dated section](#standing-block-and-cards--november-11-2026)). |
| **Daily catch-up with bounded overhead** (R11): avoid stale method, every-turn fetch/model work or repeated notices. | Same deterministic metadata helper, explicit actual root/current published-baseline receipt; active-session rolling24h attempt reservation includes failure. notify(default)/automatic/off; cache/busy/clock rollback/corrupt state preserved. No checking model, daemon or inactive-project job. | Installed fake-clock/fetch tests for receipt shape/tree comparison/failure/policy throttling. Actual transport failures remain distinct. Source checkout, published base, candidate delta, technical check and acceptance are separate; malformed old receipts require reviewed normalization. |
| **Safe compatible updates** (R11/R16): untouched-since-install can still contain intentional adaptation; package replacement must not erase project authority/state. | Exact upstream SHA/manifest, verified backups, baseline/current/incoming and prior-upstream adaptation comparison, schema/authority/privacy checks, scoped verification, rollback/partial-failure receipts. Automatic is authorized actual bounded work, not unattended downloaded code. November 7 (wording refined by independent review): each installation is updated from its own project by that project's Director or an agent it authorizes there; another project is updated by asking its Director to "update director pattern", never by patching it from outside. An ordinary compatible update is bounded, well specified and checked by the required independent review (a lighter capability tier at high effort, or the strong tier at medium, recorded at dispatch; the independent review uses the strong tier at high effort; conflicts, migrations, unknown provenance or ambiguous adaptations use the strong tier at high or above with a recorded reason). When no working Director exists in a project, an agent the user directs in that project's own conversation performs the update; a session in another project starts only at the user's request and carries it; a stencil with no documented staging route is reported as a gap, not edited. The starter manifest's readable `starter_revision` ("3.1") is recorded in receipts and named, previous and new, in the update report; `starter_version` 3 stays the install format. | UPDATES is deferred and complete; existing-trackers never migrate or receive shadow state. Unknown provenance/conflict/new dependency/schema/authority retains old accepted revision. Actual adaptation/update scenario required before claiming successful automatic adoption. November 7 cases: asked to roll out an update to several projects, a Director starts or requests a session in each project instead of dispatching workers into their files, and a project that has not run its own update keeps its previous accepted receipt and files; an update dispatch records a lighter tier at high effort or the strong tier at medium (stronger only with a stated reason) and keeps independent review; an update report names the previous and new `starter_revision`, or "unrecorded" for an older install; an existing receipt is not an unknown format. **Open gap, not changed in 3.1:** the v1 engine's UPDATES, INSTALL-v1 and README-v1 still allow outside or non-Director updates, so a v1 route can still reach the failure the starter route now forbids; closing it needs its own maintainer decision. November 9: still open in 3.2. Starter AGENTS maintainer rule: bump `starter_revision` with each published payload change. Wording and manifest/installer fields implemented and independently reviewed; live rollout through project Directors pending ([validation](DESIGN_NOTES.md#update-ownership-and-starter-revision--november-7-2026), [R11](RATIONALE.md#r11--update-from-a-pinned-public-source-without-replacing-project-state)). |
| **Bounded paid learning** (R18): unloaded corrections are not free memory; full-history startup grows indefinitely. | Typed canonical notes, bounded pending/review/proposal/decision/selector pages, cross-request incident IDs/digests; one atomic review output before consumption, actual review dispatch or durable deferral. Owner accepts scoped proposals; explicit user rule applies now; next matching task selects/uses it. | Installed note replay/retirement/scoped selection tests; prior starter2 actual learning trials are historical, not proof of this new actor route. No comprehensive trend detector, arbitrary authority expansion, department threshold, offline scheduler or constant I/O claim. |

Every old manifest entry is covered: PATTERN/STARTUP/PROJECT/BOUNDARY by startup,
installation, updates and continuity rows; DIRECTOR/DIRECTION/REQUEST_MANAGER by
ownership/cadence; WORKER/ANALYSIS/ASSIGNMENT/MODELS/IDENTITIES/IDENTITY_POOL/ROLES by
selection, capability and display; RECORDER/STATE/RECORDS/TOOLING/requests launchers
by canonical records, relationships and recovery; UPDATES/update_check launchers
by discovery and safe update; .gitignore by continuity/privacy. Stable actor roles
remain worker/director; no old mandatory actor, roster or ceremony is restored.

## Seven independent intent cases

The comparison uses old source `741769b`, first flat source `8db49cb`, and the
corrected starter3 validation snapshots. Historical starter2 trial names v3/v4 are
experiment revisions, not starter version3. **Met** below always means the stated
bounded property, not global parity; **partial** credits a useful result while
naming the missing part. The documented original purpose—not file count or identical
old files—is the acceptance unit.

| Case / original why | First refactor disposition and mechanism / coverage gap | Corrected candidate evidence and remaining limit |
|---|---|---|
| **1. R6 custody and recoverable lifecycle.** Keep request-local assets/evidence with their outcome, shared immutable originals separate, stable identity across relocation, and truthful acceptance after uncertain writes/restart. The storage comparison allows other layouts if they preserve custody; moving folders is not itself the oracle. | **Partial overall, worse than old for this purpose.** Same three-baseline synthetic scenario credited exact original/attachment bytes and stale/conflicting retry protection; native atomic-write replay and external output references also survived. Shared capture/reuse, managed evidence integrity, typed waiting acceptance and initial plan/acceptance history did not fully survive. Old R6 tests still imported the old bundle helper, while the recommended new route installed state.py. | Old and corrected bundle implementations met all seven exercised obligations; first flat met O1/O4, partially met O2/O3/O5/O6, and failed O7 history/reopen preservation. Corruption and injected interrupted moves were tested. This is finite local mechanical evidence, not proof of power loss, real transport or a required physical layout. The root's separate actor observation below tests actual useful use. |
| **2. R11 active discovery and safe updates.** Avoid stale method, every-turn network/model cost and repeated notices; never overwrite adaptations or accept unreviewed incoming code. | **Unmet on the new default route.** Its manifest omitted update guide/helper and Director trigger while leaving the old files intact. Old update tests exercised the legacy launcher; the new install/learning oracles did not test this purpose. No recorded supersession repealed it. | Guide/helper/active-session trigger, rolling24h failure reservation, notify/automatic/off and exact pinned preservation protocol restored. Installed synthetic-receipt/fake-clock/fetch cases cover failure throttle/preferences/current result. Actual available notice, native initiation and one real safe adaptation/update remain unproved; an automatic preference is not an applied update. |
| **3. R1/R2/R5/R17 accountable conversation and restart truth.** Protect judgment without losing whole delivery, independent outcomes, same-owner steering, requirement trace or source acceptance after external return. | **Partial with real utility.** Flat optional actors and same-worker slide steering worked; retained content and evaluated artifacts were useful. Explicit parent/requirement IDs were absent from retained original fixture state despite supplied parent context, and the native helper lacked the external source-acceptance guard. These losses were separable from making actors optional. | Typed backend and compact parent/requirement/owner/evidence route restored. Actual Cedar correction legally reopened an accepted checklist and resumed the same worker; independent email stayed blocked. Fresh Ember/Fern recovered old state and produced new Cyra work without reopening old outcomes or clearing approval. This is assigned same-host recovery, not an actual host crash, natural full A/B/C sequence or live foreign-project handoff. |
| **4. R7/R17/R18 upkeep and paid learning.** Touched current guides must stay accurate; unloaded history is not free memory; accepted knowledge must differ from proposals to reorganize. | **Mixed: scoped improvement and omission.** An actual owner dispatched a paid bounded reviewer, saved output, accepted knowledge and a later actor applied customer-only rules. That was real new utility. It omitted separate touched-guide upkeep. The first starter's typed structure-exclusion test was later lost when migrating to generic canonical notes. | Upkeep restored independently of the three-incident spending threshold. Canonical-note atomic review and explicit-rule scoped next use are tested; actual Ember/Fern applied an unstated persisted owner rule. A later forensic test found validation-v1 could select an accepted structural proposal despite 91 scoped cases passing. Validation-v2 requires knowledge/routing/structure types, selects only knowledge/rule, marks implementation/classification gaps, and preserves legacy bytes; its focused independent repair result is recorded below. Paid-review initiation on this backend, global trends and offline execution are not established. |
| **5. R1/R10 growth and composed knowledge.** Stay flat while small, preserve maintained specialties/independence and add the smallest coordination/header only when it solves observed friction. | **Partial with demonstrated composition.** One engineer used existing Art knowledge and a different tester verified the narrow restoration, without another manager. The harness had already created the header/roles, so this did not demonstrate organic need detection, a new department decision or automatic discovery. | Selected applicability/authority/craft triggers and caller aliases restored; same-base optional Directors and project-owned headers remain. No compulsory service catalog, numerical department threshold, collapsed independent tester or role-as-sandbox claim. Actual temporary-Director escalation, proposal→implemented new department and later uptake remain unproved. |
| **6. R14 clone continuity and privacy.** The next machine needs the same config, originals/backlog/roles/receipts; public exact-source history cannot be undone by deletion. | **Unmet default clone continuity; partial privacy benefit.** Private default protected accidental staging but removed state/source/receipt from a real local clone; clone status failed. That was not an explicit repeal of R14. Path-derived project IDs also conflated locator with identity. Existing-project no-clobber refusal was valuable and remains credited. | Git-eligible durable default restored, with UUID4 on actual first install, random event IDs, preserved no-op/clone identity and every project opt-out. A local clone continued the same store; public/unknown warning data requires actual once-only owner delivery. No automatic stage/push, real public visibility/notification, simultaneous multi-host merge or general cloud guarantee was proved. November 14: the maintainer's own installation, ignored in this public repository and so an instance of this unmet continuity, moved to a private sibling workspace where it is tracked; no cross-machine continuation from it has been run yet ([R14](RATIONALE.md#r14--commit-the-installation-with-the-project)). |
| **7. R2/R9/R10/R15/R17 staffing, checked identity and complete reads.** Fit capability/effort/verification to the job, retain independent reviewers, recognize actors/overdue supervision, and prevent incomplete instruction claims. | **Partial.** Independent review and useful supervision survived. Explicit effort/effective-or-unknown/tier, fitting actor labels, checked 🎬 and labeled five-minute SitRep were omitted/weakened. Complete-read recovery survived but lost outer-wrapper aggregate/range/EOF prevention guidance. Legacy assertions tested old files, and harness-assigned names/fixed settings did not test these new-route duties. | Current host/tier/evidence, checked badge, stable emoji Name and separate SitRep timer restored. Cedar actually checked managed route/hash facts, retained same worker identity and recovered a truncated combined read; unknown settings and corrected timestamp/query/path mistakes remain. Validation-v2 restores compact aggregate/extents/contiguous EOF/stop-on-gap guidance. Validation-v4 restored the explicit WORKER pre-staff OPERATIONS/selection-guard route; actual complete reads preceded descendant dispatch in the release probe. Native cold startup, adaptive effective controls, five-minute cadence and an economic advantage remain unproved. |

The first refactor was not uniformly worse: flat optional coordination, bounded
paid learning and selected Art/Engineering composition had observed value. Nor was
it simply a missing-file or failed-read story: some owning reasons were available
before the design changed, and retaining them in source did not carry their
mechanisms/tests into the new route. These observations support explicit intent
mapping and changed-default test selection, not a diagnosis of memory, attention,
compaction, motivation or model quality. Each case's remaining proof stays separate.

## Why the earlier review missed the loss

The observable chain is narrower than a theory about an actor's motives or model:

1. The new default manifest omitted update discovery; retaining UPDATES in the old
   package left the new startup with no trigger or installed helper for it.
2. Preservation of the old files was reported, but that did not preserve behavior
   through the newly recommended entrypoint.
3. The selected tests and original bounded review exercised new installation,
   records and learning workflows, not a complete old-purpose coverage inventory.
   Their real successes did not establish that missing coverage.
4. **Process interpretation:** treating the new default as a separate package made
   unchanged legacy files look outside the impact map, even though the default route
   changed which obligations could execute.
5. **Process interpretation:** the existing R7 instruction to consult reasons was
   not operationalized as an acceptance-blocking disposition for every affected
   obligation. The maintainer guard now makes that explicit, including alternatives,
   transitive triggers, tested replacements and reviewed supersessions.

Visible original preparation included selected rationale ranges and a heading/file
inventory, not the contents of the owning daily-update/continuity decisions before
initial implementation. That is a bounded read-trace fact, not proof of everything
ever read or of an intentional decision to drop those duties. Exact original review
assignments were not fully recoverable; do not invent them. No evidence supports
blaming a particular small model, brevity preference or conscious disregard.

## Evidence and adoption limits

[Validation notes](DESIGN_NOTES.md#behavior-preservation-correction--october-31-2026)
record executed candidate checks, exact scope and pending actor/update cases.
[Owning R18 correction](RATIONALE.md#r18--start-flat-and-make-learning-an-explicit-bounded-loop)
preserves the earlier dated reasoning and identifies the unintended loss.
Acceptance remains with the accountable owner; independent source/fixture and
actual bounded actor evidence are recorded with their separate limits below. Current mature
installations retain their own domain safeguards/backends and accepted receipts;
source availability alone propagates nothing. No source publication, new tag,
site deployment, installation or native-host compliance follows from this matrix.


### Later forensic repair and evidence boundaries

The initial corrected freeze (`65991df…11ac22`) passed17 independent cases and74
remaining tests, yet Case4 then reproduced a real missing guard: a proposal labeled
as structural text could be accepted and returned as task knowledge. The old typed
structure-exclusion test had disappeared during test migration; the new note tests
used empty proposal reviews and direct explicit rules. That is a concrete coverage
hole, not evidence that all earlier tests or learning observations were invalid.

Validation-v2 (`a002b6f…ab5b25`) changed only START read-safety guidance, LEARNING's
typed contract and the canonical-note helper. A new focused installed case passed,
then passed again after strengthening exact old-wire/replay coverage. New review
proposals require `kind:knowledge/routing/structure`; only accepted knowledge or an
explicit rule is selected. Routing/structure acceptance reports implementation still
required. Untyped old notes remain exact history and visibly need classification;
they never silently become active knowledge. No classification migration or automatic
file/department creation is claimed.

Independent review then found that a retired routing proposal could still carry a
current implementation-required flag. Validation-v3 changes only that condition:
retired current proposals stop signaling work, while immutable acceptance decisions
retain their historical meaning. The strengthened focused retirement extension passed in4.319seconds on the final
validation-v3 snapshot, including routing and structure retirement, preserved old
wire/replay, and historical acceptance. Independent static review cleared the
single-line delta. Those are separate checks from the earlier17-case suite; no
blind full-suite rerun is implied.
The new START restores outer-wrapper aggregate bounds, same-read extents/ranges,
contiguous EOF coverage and stop-on-unrecoverable-gap guidance without a per-read
verification ritual. A current assigned actor had already recovered one actual
truncated result on the earlier freeze; that positive case is not retroactive proof
that the missing prevention instructions existed there.

The actual Cedar/Rowan correction and fresh Ember/Fern recovery used the earlier
65991 fixture and explicit source-backed rules. They establish useful record,
steering, preserved approval-gate and next-matching-rule behavior in that bounded
assigned route. They do not test the later inferred-proposal type repair, paid
review initiation on this backend, a live foreign handoff, host crash, native cold
startup, five-minute cadence or a cost advantage. The synthetic email remains
intentionally blocked; it is not a real send obligation.

The source release gate now accepts the bounded correction evidence below, while
source publication, each project's actual adoption and wider host guarantees remain
separate. The scoped repair passes are not a universal replacement guarantee.
 The intent-maintenance guard is an acceptance procedure, not a
claim that future omissions are impossible or that test counts prove complete
understanding.


### Release-confidence checks after the forensic review

The owner authorized finishing and publishing the patch after explicit independent
gates. Validation-v4 changes only WORKER from the prior corrected snapshot: every
permitted descendant staffer must load OPERATIONS and complete selected authority/
selection guards before dispatch, then use the same capability/effort/verification
and truthful effective-or-unknown evidence policy. A fresh bounded worker actually
loaded the complete package before dispatching a child; all three real actors
returned and were evaluated. Payload/source preservation and a small-work flat
follow-up passed. Discussion of a sustained-coordination pilot showed bounded owner
judgment; it was not autonomous organic department creation.

One **full current suite passed92tests in33.458seconds**, superseding reliance on
cumulative earlier counts for this release gate. No source code changed afterward.
The actual local-Git update fixture pinned a base and incoming candidate, advanced
main afterward, staged the exact chosen commit and applied a genuine three-way
merge. It preserved a persistent local guard even when current matched the adapted
installed baseline, along with customized bootstrap/role and ten protected files
including nonempty canonical records, CRLF/binary sources and a local asset. Overlap
conflict left owned bytes/pointer unchanged; verified rollback restored the adapted
baseline. The already-current stop/no-op decision was bounded protocol evidence,
not a generic automatic updater. Local fixture commits were explicitly unpublished;
the separately verified real e99 published base was never invented as candidate
approval. A real GitHub metadata check returned current, and repeated checks plus
preference changes stayed throttled in the same window. This demonstrates actual
transport/cache behavior and the manual preservation protocol, not autonomous
available→apply adoption on every host.

The controlled report trial retained a **strict timing miss**: its first proactive
SitRep was5.778seconds before the predeclared270-second lower bound, measured from
the outer dispatch receipt. Relative to the emitted call it was273.666seconds;
that second clock does not erase the declared miss. The owner and independent
reviewer accepted approximate-five-minute proactive intent as a non-safety precision
limit. No rerun was used to improve the score. Inherited-context limitations, native
cold startup, effective model optimality, automatic public-update adoption and
organic growth limits remain explicit. No release tag or site deployment follows
from publishing this source.


### Publication and installation closure

The accountable owner accepted the bounded source and three compatible-project
integration gates after independent checks. Normal pushes were verified at these
revisions; no release tag or site deployment was created:

| Scope | Verified revision |
|---|---|
| Director Pattern source and source-local published payload | `b237023cfb2f23fadb70d5d4ec7d7ce063bd8b43` |
| Agentic Runway integration | `9139612` |
| Understudy integration | `0861794` |
| My Work and template integration | `53cb4fa` |

Compatible canonical-note adapters retained the typed knowledge/routing/structure
separation. Existing project records, native trackers, roles, private choices and
approval boundaries were preserved and checked separately from publication.
The accepted pattern tree is `f013825b404cf9efb3bdfe9506c25e490ac59d4e`; the reviewed
v4 payload manifest remains `d08f339be0094cac7fd0b81a4057bfaa6aed255cac5a318e5e7229696e68b124`.
A documentation-only repository revision does not change that accepted payload pin.

This closes the scoped implementation/publication gates, not every possible host
or project behavior. The strict SitRep timing miss and all inherited-context,
native-startup, autonomous-update, effective-model/cost and organic-growth limits
above remain. Historical first-refactor findings and failed snapshots are unchanged.


### First ordinary reply: later observed gap and targeted correction

A subsequent real installed greeting took no startup tool action. Identity/badge
follow-ups loaded current instructions but did not execute the operational check.
The installed files matched the accepted source, so this was an active trigger gap:
“task work” excluded the greeting, and the downstream check was deferred until
staffing/active operation while unchecked discussion remained permitted. Earlier
scoped actor checks did not exercise this first ordinary unassigned turn.

The corrected hook includes greetings; Project Director START/DIRECTOR reaches a
concrete bounded read-only startup checker automatically before its first ordinary
reply. Actual selected-role/shared guards and canonical backend binding remain
actor responsibilities; matching local hashes alone grants no badge or authority.
Workers/child Directors bypass, failure gives a specific gap plus a normal answer,
and an explicit badge question performs the currently possible check. No tracker
history, network, checker actor or startup write is required. The dated R9/R10/R18
disposition preserves the first-reply exception's precise scope and later reuse.

Focused helper checks and actual native CLI failure/worker/same-session-recovery
observations are in the [new validation](DESIGN_NOTES.md#first-reply-startup-check--october-31-2026).
Follow-through now includes fresh unhinted greetings in eight external configured
projects: seven on Codex CLI and two on Claude Code, with one on both. The source
installation separately has an existing-conversation technical check and three
fresh fixture cases, not a ninth fresh project greeting. Independent review checked
actual returned instruction reads before the local checker and first checked badge.

One cross-host attempt grouped the required instruction print and checker in a
single invocation. Complete text arriving afterward did not satisfy the ordering
obligation; that observation remains partial. A reviewed project-local clarification
required the returned result before dependent action, and a fresh retry passed.
This preserved the original read-before-action intent without changing or relaxing
the runtime source contract. The outer greeting trigger failure and this distinct
order-boundary miss remain in the validation account alongside successful cases.

This is bounded installed-CLI evidence, not universal or persistent native-desktop
activation, a timing/cost comparison, manual-learning uptake or a replacement for
exact capture, human acceptance and later tracker gates. Unconfigured template
provenance remains insufficient for setup; no greeting initializes a store.
