# Swap audit: what the candidate block trades away

**Independent audit, 2026-11-09.** Read-only, Focused verification. Compares today's installed startup route (starter revision 3.2) with the candidate block in [slug-draft.md](slug-draft.md) as it stood at the end of this audit: round 7, 6,190 bytes, with the November 9 re-entry sentence restored at the top of "Reading (every role)". The first pass (parts 1 to 3) was formed from primary files only: `pattern/starter/install.py` (`BRIDGE`), `pattern/starter/payload/` START, DIRECTOR, WORKER and OPERATIONS, `startup_check.py`'s output, the bridge and startup tests in `development/tests/`, and the owning entries in `development/RATIONALE.md` and `development/BEHAVIOR_PARITY.md`. Only after that were [layout.md](layout.md)'s obligation map, its dated supersessions list and slug-draft.md's notes read (part 4). The earlier reviews (slug-review.md, second-pass.md, report.md) were not read.

Terms. **Today** means what an installed agent actually receives now: the bridge, then START and the selected role package before the first reply, and, for the Project Director, OPERATIONS' installation-evidence section and the check. **Pinned** means a test in `development/tests/` asserts the sentence or behaviour. **Recorded** means a dated RATIONALE or BEHAVIOR_PARITY entry names the failure it prevents. **Untested** means no static test or live trial exercises it. All cards except staffing are unwritten, so a card is untested by definition. Where this audit says "safe", it means the card's trigger is the action itself and the old text is an action reference anyway.

## 1. Today's route, behaviour by behaviour

In the order an agent meets them. B = bridge, S = START, D = DIRECTOR, O = OPERATIONS, W = WORKER (line numbers are those of the published payload). Classes: **K** kept word for word · **R** reworded, same trigger and audience · **M** mechanism replaced · **X** dropped.

| # | Today: who, what, when | Candidate | Class |
|---|---|---|---|
| 1 | B, every reader: "Default to Project Director unless explicitly assigned a worker or scoped child Director role." | Same sentence in "Your role" | K |
| 2 | S 15–23, every reader: with no explicit role assignment, load DIRECTOR and serve as Director; missing or conflicting details go back to the assigner and never create Director authority | A spawned agent with a report-back task is a worker without being named one; "never changes on another agent's or session's message"; opt-out for the Project Director | M (different reader) |
| 3 | S 17–18: missing or conflicting assignment details return to the assigner | WORKER keeps the clause (W 23–25 today) | R |
| 4 | B + S, every role, before the first ordinary reply in each conversation, greeting not exempt: read START and the selected package completely | Project Director: no package; the duties are standing text, cards are read before their actions. Worker: "Read `.director/WORKER.md` and any role file" with no stated time. Child: its overlay | M (startup read becomes standing text plus on-demand reads) |
| 5 | S 3–13, every role: complete reads, contiguous ranges to EOF, total extent in the same result, hashes/summaries/searches are not reads | "Reading": END line or shown total length, bounded numbered ranges, non-reads listed; full rules move to WORKER | R (END line is new) |
| 6 | S 6–7, every role: "Batch independent reads only; wait for required instructions to return and read them before running dependent commands." | Not in the block. WORKER gets the full read rules, but Directors no longer read WORKER | X (for Directors) |
| 7 | S 9–11 + B: recover truncated reads; stop affected work if recovery fails | "If a cut-off read cannot be recovered, stop that work and say so." | R |
| 8 | B, S 25–33, D 17–30, O 8–13, Project Director: run the check before the first ordinary reply, even a greeting, proactively, not waiting for staffing | "Before your first reply, even to a greeting, run the project section's check command." | R |
| 9 | S 34–37, O 6–8, Project Director: 🎬 on every reply after a pass; on failure the specific gap and an ordinary answer | Same in the 🎬 paragraph | R |
| 10 | O 101–118, Project Director, read before the first reply: confirm complete reads, role, every guard, backend binding, the host-loaded route and conflicts in surrounding instructions before 🎬 | "you confirm its actor_must_confirm items": the list comes from the checker's output; the explanatory text moves to the badge card, read only after a failed check | M (standing read becomes a pointer in tool output) |
| 11 | O 59–62 and R9 (Nov 2), Project Director: selected project guards are read completely and their conflicts evaluated before 🎬 | Project section: guards are read "before task work" (layout marks this open), while 🎬 still asks the agent to confirm "complete current project instructions, including conflicts outside the hook" | M (read moved after the badge) |
| 12 | O 57–64: START, DIRECTOR, OPERATIONS and the checker are managed files with strict hashes; one edited DIRECTOR byte gives a gap and no 🎬 | The Director's rules move into AGENTS.md, which the checker treats as composed project text whose changed snapshot never blocks; layout v.3 only "optionally" hashes the slug and reports it `changed` | X (integrity over the Director's rules) |
| 13 | S 31–32, O 15–21: an honest unbadged progress preamble the host requires; no greeting or identity answer, no claim, no 🎬 before the check | "A host-required progress note first stays unbadged and claims nothing." | R |
| 14 | S 28–30, O 23–33, Project Director: in an unconfigured generated instance, complete the guarded first use **before** the check | Block row: FIRST_USE under "handle a failed check". Order is meant to be restored by a line in a generated template's project section (layout v.6) | M (order now carried by project-owned text; the block's own route puts first use after the failure) |
| 15 | B, S 38–39, D 28–29: workers and scoped child Directors skip the check and never inherit 🎬 | "No check, no 🎬" and "never the check or 🎬" | R |
| 16 | B: "Preserve project/host authority." | Same words, plus other authors' work, private sources and trackers | K |
| 17 | B, every role, after a compaction or resume: "repeat this startup", where "this startup" is the complete read of START and the package plus the Project Director's check | Same two sentences, moved to the top of "Reading". "This startup" is redefined: the Project Director's check; a worker's WORKER and role file; a child's overlay; "the file your next action needs" | M (same words, new referent for the Project Director) |
| 18 | D 26–27, S 63–65, O 48–49, W 21–23 (pinned): evidence and instructions from before a compaction or resume are stale and are read or checked again | DIRECTOR and START go; the "fresh" test (your own run or complete read after the latest break) replaces their clauses; the OPERATIONS and WORKER clauses stay | M (direct clauses become the break test) |
| 19 | B, Directors: the three delegation sentences | Same words, duty 2 | K |
| 20 | B, workers: "Workers, delegate useful independent subsets within your assigned scope." | Same words, worker bullet | K |
| 21 | B, every role: "Load selected task instructions before action" (any selected instruction) | Only cards, table manuals and files the project section names need a fresh read before their action | M (narrower set) |
| 22 | S 26–28: the Project Director checks whether defaulted or explicitly selected | "Otherwise you are the Project Director" covers both | R |
| 23 | D 3: own the conversation, result and acceptance; answer discussion directly | Duties 1–2 | R |
| 24 | D 4–7 (pinned): partner, not literal executor; map the request to the established mechanism; say so; recommend as ❓; hold | Duty 1 | R |
| 25 | D 7–12 (pinned, and a test requires it to load before the check paragraph): judge on merit, not on work started; pause conflicting mid-flight work, then recommend; continue only independent work; a forbidden route gets the permitted route or a 🖐️ action | Requests card, read before "capture, split or steer a request" | M (startup read becomes an on-demand card with an indirect trigger) |
| 26 | D 13–16 (pinned): before planning any update, here or elsewhere, read all of UPDATES; another installation is updated only by its own Director | Table row "as Project Director, ... or discuss updating" leads to the update-check card; UPDATES "before planning an update" | M (startup read becomes on-demand) |
| 27 | D 38–44: ❓ and 🖐️, grouped questions, question tools, host formats | Duty 9 | R |
| 28 | D 45–50 (pinned), O 148–157: before dispatch read the staffing section and the selected role's definition | Staffing card; Directors route from roster rows instead of reading the definition | M |
| 29 | D 48–50 (pinned): give the worker its startup and task instructions and knowledge; its scope must permit those reads | Staffing card (written; carries both, plus the block's text when the host does not pass AGENTS.md) | M (card, matching trigger) |
| 30 | D 52–53 (pinned): no subagents means report the gap and stop | Duty 2 | R |
| 31 | D 65–67 (pinned): set tier and effort explicitly on every dispatch; strong tier at high effort; one-line reason | Duties 3 and 5 | R |
| 32 | D 62–65, O 159–188: lighter-tier option; record requested and effective settings | Staffing card | M (card, matching trigger) |
| 33 | D 69–75, O 190–195: local decisions, rework authority, return contents | Staffing and supervision cards | M (card, matching trigger) |
| 34 | D 77–84: same contract across sessions and routes; only the authorized source subset | Staffing card | M (card, matching trigger) |
| 35 | D 94–95 (pinned): narrow state operations are the Director's own duty, not a reason to staff a Recorder | Requests card; duty 2 says "You route; workers execute" | M (card, matching trigger) |
| 36 | D 98–100: capture exactly before dependent work; split obligations | Duty 4, with the simple-reply exemption from S 58 | R |
| 37 | D 100–112: lifecycle operations, steering by revision, checkpoints | Requests card and store manuals | M (card, matching trigger) |
| 38 | D 114–125: judge evidence against the whole result; reassess after repeated failure | Duty 7; supervision card | R |
| 39 | D 126–133: keep the outcome open; on recovery retrieve all task-bound IDs | Duty 8; recovery card "as a Director, take your first project action after any break" | M (on-demand; known gap for a new conversation with work out) |
| 40 | D 134–138 (pinned): SitRep about every five minutes; check every turn whether one is due; one report covering every held stream | Duty 6: "send a 📋 SitRep on every stream ... check each turn" | R (but see part 2) |
| 41 | D 136–149 (pinned): clock check, note each time, quiet and stalled streams, shape and example, one line when unchanged, replies do not reset it, prompt report after a break, no-clock fallback | Supervision and recovery cards | M (card, matching trigger) |
| 42 | D 169–179: next useful action before ending a turn; real exits; submitted vs accepted | Duties 8 and 10 | R |
| 43 | D 181–183: supported waits, not polling | Supervision card | M (card, matching trigger) |
| 44 | D 185–198 (R18): record incidents inline; pending learning at evaluation; three-incident review | Knowledge card, read before "record a correction, or close an outcome" | M (the duty to record now sits behind the trigger "record a correction") |
| 45 | D 200–204, O 209–215, S 19–21: closure upkeep; keep caller IDs and aliases through refactors | Knowledge card | M |
| 46 | D 204–206: during active sessions arrange due daily update discovery (the helper's cache decides) | Row "as Project Director, begin work with no update check in 24 hours" | M (the agent must judge a condition it cannot see) |
| 47 | S 24–25: briefly acknowledge the resolved package once | Dropped for Directors; WORKER keeps it for workers | X |
| 48 | S 48–58: task-time knowledge selectors and select | Knowledge card; WORKER keeps "matching accepted knowledge before action"; duty 5 names "applicable knowledge" | M (card, matching trigger) |
| 49 | O 217–233: continuity and privacy (already an action reference) | Privacy card | M (card, matching trigger) |
| 50 | O 197–202: verification tiers | Staffing card | M (card, matching trigger) |
| 51 | S 16–17, ROLE_INDEX: no global startup catalog; discovery route | Roster in the standing project section | M |
| 52 | D 32–34, S 58–62: no checker actor; the check makes no network request or write | Badge card; "your own run" | M (card) |
| 53 | S 44–46: composition cannot merge people or waive independent testing; staff for work, not ceremony | Staffing card | M (card, matching trigger) |
| 54 | O 10–12: a later badge or identity question retries a missing or stale check | Not in the block; the badge card only after a failure | X |
| 55 | O 47–49: relevant changed startup bytes require a recheck | Badge card, "change how this project installs or loads" | M (card, matching trigger) |

**Counts:** kept word for word 4 · reworded with the same trigger and audience 17 · mechanism replaced 30 · dropped 4 (55 behaviours).

## 2. Evidence for each replaced or dropped behaviour

| # | Old mechanism: evidence | New mechanism: evidence | Verdict |
|---|---|---|---|
| 12 | Pinned: the checker's drifted-managed-file tests. Recorded: BEHAVIOR_PARITY field triage keeps "one edited DIRECTOR byte gives a specific gap and no 🎬" as the live oracle | None. The slug is project text; a changed snapshot does not block, and hashing it is optional | **Loss.** 🎬 would no longer certify the rules the Director actually follows |
| 14 | Recorded: R9 later November 4. A generated project gave a missing receipt and no 🎬 on its greeting; the fix put first use before the check. Pinned: the helper only (test_first_use); the order lives in START, DIRECTOR and OPERATIONS prose | Untested. The block's own row puts FIRST_USE after a failed check, which is the November 4 failure shape. The restoring line lives in a project section that "updates never replace", so a template fix cannot reach it | **Risky** |
| 11 | Recorded: R9 November 2 (guards read completely; an unresolved conflict prevents 🎬); O 59–62 | Untested. The guards are read before task work, but 🎬 is given at the first reply and claims a conflict check that has not happened | **Risky** |
| 10 | Recorded: R10 October 31 (the actor confirms reads, authority and backend). The checker's `actor_must_confirm` list exists today | Partly real: the list is emitted. Confirming it without OPERATIONS' explanation is untested; layout flags the meaning change | **Risky** |
| 17 | Pinned: test_flat_bridge_repeats_startup_after_compaction_or_resume (text and placement). Recorded: R10 November 9. Reported live: Director sessions re-read startup after a compaction under this sentence | The words are kept, but for the Project Director "this startup" is now the check plus "the file your next action needs": the untested fresh-read test. The live reports concern the old referent (re-reading START and DIRECTOR); they do not transfer | **Risky.** Restoring the words did not restore the mechanism that was observed |
| 18 | Pinned: test_flat_reuse_rules_do_not_survive_compaction_or_resume (four clauses). Recorded: R10 November 9 | Fresh-read test; no live evidence (layout says so) | **Risky** |
| 2 | Pinned: "Without an explicit role assignment, load [DIRECTOR.md]" (test_flat_complete_reads…). Recorded: R10 October 17 and November 1 | Untested. It needs an agent to infer that it was spawned. It does not settle a session another agent starts with a report-back task ("spawned" or "a tool started the session"?). "Never changes on another agent's message" can also block a parent re-scoping a worker into a child Director | **Risky** (flagged ⚠) |
| 6 | Pinned: test_flat_complete_reads_keep_combined_bounds_and_recovery. Recorded: R10 October 31; a cross-host trial printed instructions and ran the dependent checker in one call | None for Directors. The check command is now standing text, so that exact case cannot recur, but "read card, then store command" in one call can | **Loss** (narrow) |
| 25 | Pinned: test_director_is_a_partner_and_sets_dispatch_settings, including the assertion that the partner rule loads before the first-reply paragraph | Untested card. A better route appearing mid-flight is not "capture, split or steer a request", so the trigger can miss it | **Risky** |
| 26 | Pinned: the same test (phrase count). Recorded: the starter 3.1 decision that each project updates itself | Untested card. "Copy the new starter into project X" need not read as "discuss updating" or "planning an update" | **Risky** |
| 46 | Recorded: R11 daily discovery; UPDATES pinned for "at most once per rolling 24 hours" | Untested. After a break the agent cannot tell whether a check ran in 24 hours; today it just runs the helper, whose cache decides | **Risky** |
| 21 | Implicitly pinned: test_source_hook… requires the source and installed bridges to match. Recorded: R10 October 24/30 (required reads must stay reachable) | Untested narrowing. A runbook named in a brief or in a role file's trigger map, and not in the project section, loses the before-action rule for Directors | **Risky** |
| 44 | Recorded: R18 | Untested. The read is triggered by "record a correction", but the instruction to record one is inside that card | **Risky** |
| 28 | Pinned: test_flat_roles_preserve_delegation…. Recorded: R10 November 1 (staffing and role selection were omitted before dispatch) | Untested. Roster rows replace the definition read; an owner rule | **Risky** (flagged ⚠, owner's decision) |
| 39 | Recorded: R17 | Untested card; layout already records the new-conversation gap | **Risky** (flagged ⚠) |
| 45 | Recorded: S 19–21, O 211–214 | Untested; behind the closure trigger | **Risky** (flagged ⚠) |
| 4 | Recorded: R10 October 31 (eight greeting observations on two hosts); BEHAVIOR_PARITY: advisory links alone did not finish read chains in earlier trials | Untested for every card. Layout proposes the live smoke test and the N6 scanner | **Risky** (the proposal's own change) |
| 29, 32–35, 37, 41, 43, 48–50, 53, 55 | Pinned in places (SitRep detail, staffing tiers, narrow state operations), mostly action-time references | The card is read before the very action it governs | **Safe**, if the card carries the pinned text and the pins follow it |
| 51 | Recorded: the no-global-catalog rule | Standing roster; an owner rule | **Safe** (needs its supersession) |
| 52 | Recorded: R9 October 31 | "Your own run" | **Safe** |
| 47 | Recorded: R10 October 29 (the acknowledgment reports reads, not capability) | 🎬 and the N5 re-entry line | **Safe** |
| 54 | O 10–12 | Covered by the check before the first reply and after every break | **Safe** |

Also, behaviour 40 is classed R but its wording changes meaning. The pinned text says one report that covers every held stream; "a 📋 SitRep on every stream" can be read as one report per stream. The cut saved 10 bytes and was recorded as no change in meaning. **Risky** (minor).

## 3. Additions that change who is addressed, or add a duty

1. **Opt-out skips "Reading".** "Skip all but Summaries" also drops the complete-read and stop-on-truncation rules, and the re-entry sentence, for a user-facing session that is told not to act as Director. Today no such exemption exists. New, untested.
2. **Summaries (every role).** Every reader, workers included, must state its role, opt-out and parent, and copy the open request IDs, worker handles, ❓ and 🖐️ items and the last SitRep time. Workers have no such duty today. On many hosts the summary is written by a summarizer, not the agent. Untested (slug-draft note 7 says so).
3. **Workers read the whole Director block.** Each worker now receives 6 KB of Directors-only duties and has to sort itself out by section labels. Layout says a label is "a reading instruction, not a filter". Today a worker never sees DIRECTOR text.
4. **Spawned means worker.** This is a new rule for classifying readers (row 2). It is also the reverse of the second known defect: an agent can now be classed as a worker without anyone assigning it.
5. **New duties on every worker return** (N2's fixed last line) and on the Director's first reply after a break (N5's visible re-entry line).
6. **"General host instructions are no opt-out."** A new judgment sits next to "Preserve project/host authority". It is harmless only if "general" is read narrowly.
7. **Narrowed audience.** The update row says "as Project Director", so a scoped child Director, which today reads DIRECTOR's update rule, no longer meets it.
8. **Custody moves to the project section.** The check command, the guard list and the first-use order move into text that is written once and "updates never replace". A starter fix to any of them can no longer reach installed projects.

## 4. Comparison with layout.md's map and supersessions list

**Found here, not flagged ⚠ by the map:**
- Row 12: the integrity loss. The map lands the check in "Slug; badge card"; layout v.3 makes the slug hash optional and non-blocking. No supersession is listed.
- Row 6: the returned-read barrier. The map lands the read rules in "Slug (…); WORKER (full text)", but Directors no longer read WORKER.
- Row 21: the narrower before-action read rule. The map row has no ⚠.
- Row 25: the mid-flight partner pause moves to the requests card. No ⚠, and the pinned load-before-check assertion is not among the listed test changes.
- Row 26: the cross-project update rule. The map calls it an "unchanged rule"; the text is unchanged, but its trigger is not.
- Row 44: the trigger for incident recording presupposes the duty.
- Row 40: "on every stream". Recorded as a cut with no change in meaning.
- Part 3, items 1, 2, 3, 7 and 8. The map flags Summaries only for the K1 reversal.

**Flagged by the map, judged differently here:**
- **Re-entry sentence (row 17): riskier.** Supersession 1 is withdrawn as "no supersession needed". The words are back, but the definition that follows them turns the Project Director's half into the break test the withdrawal meant to avoid. The test's text pin still passes. The mechanism behind the live reports does not carry over.
- **First use (row 14): riskier.** The map says "order kept". The block's own table routes FIRST_USE after a failure, and the restoring instruction is project-owned text that no update can correct.
- **Guards (row 11): riskier.** The map leaves "before the first reply or before task work" open. The second option contradicts the 🎬 claim in supersession 3, so this cannot stay open while supersession 3 is decided.
- **Daily update (row 46): riskier.** The map's ⚠ is about drift from UPDATES. The larger problem is a trigger the agent cannot evaluate.
- **Package acknowledgment (⚠, supersession 7): safer.** Dropping it loses no recorded protection.
- **Roster in the project section (⚠, supersession 6): about as safe as claimed.**
- **Role resolution (supersession 4): agree it is risky.** It adds the "spawned or tool-started" ambiguity and the re-scoping problem above.

## 5. Classes of gap

1. **Works today, replaced by something untested.** Rows 4, 10, 17, 18, 28, and every card.
2. **Addressed to the wrong reader.** Part 3, items 1 to 4 and 7. Workers get Summaries duties and the whole Director block; the opt-out exempts a user-facing session from the reading rules; the worker definition widens by inference; child Directors lose the update rule.
3. **Same words, new referent.** A sentence kept word for word, so its test pin passes, while what it refers to has changed. Row 17 ("this startup", "the files"); 🎬 (same mark, different claim); "Load selected task instructions" turned into a closed list (row 21). Word-for-word restoration does not show that behaviour is preserved.
4. **Trigger presupposes the duty.** A standing duty moves behind a pointer whose trigger is doing the duty, or depends on state the agent cannot see. Rows 44 (record a correction), 46 (no update check in 24 hours), 25 (mid-flight pause filed under "steer"), 26 (the rule that stops cross-project edits filed under "discuss updating").
5. **Order inversions.** A step that came before something now comes after it. Rows 14 (first use after the failed check), 11 (guards after the badge), 6 (no wait between returned reads and dependent commands).
6. **Custody moves from verified, managed text to unverified or project-owned text.** Row 12 (the Director's rules leave the hash-checked set), part 3 item 8 (check command, guards and first-use order move into a section updates never touch). The check stays green while the governing text drifts.

## Limits

Not checked: the seven unwritten cards (only the staffing card sample was searched, for two rules); UPDATES, FIRST_USE, LEARNING, API, TOOLING and RECORDS in full; DESIGN_NOTES; whether any host passes AGENTS.md to subagents or lets the agent write its own compaction summary; any live behaviour. No tests were run. The earlier reviews were deliberately not read, so overlap with their findings is not assessed. Line numbers refer to the published starter 3.2 payload.
