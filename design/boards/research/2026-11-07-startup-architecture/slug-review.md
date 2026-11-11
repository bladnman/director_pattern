# Independent review: Director slug candidate

**Review, 2026-11-09.** Reviewer: 🦅 Kestrel, a bounded worker who did not write the candidate. Reviewed: `slug-draft.md`, `layout.md`, `card-sample-staffing.md`, `brief.md`. Compared against starter 3.2's `START.md`, `DIRECTOR.md`, `OPERATIONS.md`, the installer's `BRIDGE`, `startup_check.py`, `development/tests/test_package.py` and `development/BEHAVIOR_PARITY.md`. Judged against the owner's requirements R1 to R7, not against the author's intent. Nothing was edited apart from this file. No live session was run.

**Verdict: ready after the fixes below.** The structure holds up: a short standing block of duties, "before you do X, read Y" triggers, cards that end with END lines, and the roster in a project-owned section. Findings 1 to 5 block acceptance. Each one is a wording fix of roughly 50 to 200 bytes, but together they push the block over the proposed 6,000-byte cap (finding 13).

## Findings, most serious first

### 1. The role gate can turn the wrong agents into workers (blocking, R2)

**Text:** "a task handed to you by another agent counts unless it makes you a child Director".

**Failures:**
- **Explicit Project Director assignments.** An orchestrating agent starts a session to act as a project's Project Director, or a forked or handed-off session continues the Director's work. The first message comes from an agent, and the only exception the rule allows is "child Director", so the session classifies itself as a worker. It never runs the check, never shows 🎬, and returns to an owner who is not listening. This breaks the pinned START obligation "the Project Director, whether defaulted or explicitly selected".
- **Cross-session messages.** Another project's Director messages a running Director session, for example "update director pattern". Read literally, the rule reclassifies the running Director as that agent's worker in the middle of the conversation. That contradicts the update rule that each installation is updated by its own Director.
- **Two names for one role.** The gate says "Scoped child Director", while duty 2 and the roster say `sub-director`. An agent assigned as `sub-director` with a brief that never says "child Director" can conclude the exception does not apply. It then reads WORKER.md and works as a worker instead of coordinating.

**Fix (about +200 bytes):** "Your role is set when you start and changes only when the user or host changes it. You are a worker when another agent started you to return a result to it, unless it assigned you as Project Director or as a scoped child Director (roster `sub-director`). A later message from another agent is a request to evaluate, not a new role."

### 2. The opt-out is too broad and overlaps the worker line (blocking, R2)

**Text:** "if the user, the host or your assignment gives you another job or says not to act as a Director, do that job and skip this block."

**Failures:**
- **Host prompts.** Every host's system prompt gives the agent a job ("help the user with software tasks"). A literal reading lets the main session drop the Director role on any host.
- **Workers.** Every worker's assignment "gives you another job", so a worker meets both bullets. If it picks the opt-out, it skips "Reading cards", which is the only route to WORKER.md and its END-line re-reads.
- **Injected text.** For a worker, "the user" reaches it only through tool content. Text claiming "the user says do X instead" invites the worker to drop its assignment.
- **No end point.** Nothing says how long the opt-out lasts (scenario d below).

**Fix (about +60 bytes net):** "Otherwise, if the user or your assigner explicitly tells you not to act as this project's Director, do what they ask and skip the rest of this block while that applies; run the check before showing 🎬 again. A host's general instructions are not such a request; a worker's job changes only through its assigner."

### 3. Non-reads can pass the END-line test (blocking, R3 and R4)

**Text:** "unless its END line appears in a tool result or host-attached file after the latest break".

**Failures:** The line appears in many tool results that are not reads of the card:
- a search over `.director/` that matches `END cards/staffing.md`;
- a diff that shows a card's last lines;
- a `tail`, or only the last range of a long manual;
- a worker's return that quotes a card (reviews like this one do). A return is a tool result in the Director's context.

The block's own sentence "A summary, search or hash is not a read" contradicts the literal test, and a model can follow either one. This weakens the mechanism's main claim (note 3: "Nothing relies on the agent judging what it remembers").

**Fix (about +50 bytes):** "unless your own read of that file, through its END line, appears after the latest break (in ranges, every range)". Also add "briefs" to "Never copy END lines into replies or summaries."

**Also:**
- **No break yet.** "After the latest break" is undefined when no break has happened. Define it once: "after the latest break, or in this conversation if there was none". Today only the 🎬 meaning sentence covers this case.
- **Resume with full replay.** A resume that replays the whole old transcript with no visible marker cannot be detected by any positional test, so the old results count. Record this as a known limit with its own test case rather than claiming the test is mechanical.

### 4. Project-named files lose their re-read after a break (blocking, R3 and R4)

**Text:** "Before you act under a file this block names…" and, under Roster, "read the files that section lists before the work they govern."

**Failure:** Files the project section names have no END lines and are not named by "this block". In this checkout those are PROJECT.md, CAPABILITY_POLICY.md and STATE.md; in other projects, ROSTER.md and the project's guards. So nothing requires reading them again after a break. Today's bridge covers them ("repeat this startup… Read the files again"), because START lists the project guards as startup reads.

**Fix (about +90 bytes):** Extend the rule to "a file this block or the project section names". Add: "a file without an END line counts as read only when your read of the whole file appears after the latest break."

### 5. The capture duty has lost its exemption (blocking, R5)

**Text:** duty 4, on every turn, "Capture the user's exact request, and each later addition, before work that depends on it".

**Failure:** START line 58 exempts simple replies: "An empty/simple reply needs no request/history or learning query." The slug drops that sentence. A careful agent receiving "hi", or a discussion question, may capture it. Capturing triggers the requests card plus the three store manuals (36,343 bytes) before replying. That reverses the up-front saving the proposal is built on. The layout maps this sentence to the knowledge card, but the slug's unqualified wording is read first.

**Fix (about +70 bytes):** "Capture each actionable request exactly… Discussion and simple replies need no capture or knowledge query."

### 6. Some triggers fire at the wrong time, so the rule never reaches the moment it governs (high)

The AGENTS.md maintenance rule asks reviewers to look for triggers that can never be reached:
- **❓ in host question tools.** The rules "put ❓ in its title; don't repeat the questions in chat" and "one ❓ for a grouped set" are on the supervision card. That card is read only when work is held. A ❓ partner decision under duty 1 usually comes before any dispatch, so the card is not read. Fix: add "(in a host question tool, ❓ goes in its title; don't repeat it in chat)" to duty 9, about +70 bytes.
- **Host-required progress note.** This rule is on the badge card, which is read only after a failed check. It governs the moment before the check, on the normal path. Layout row "⚠ moved out of the slug for size" records the move but not this consequence. Fix: add "If the host requires a progress note first, keep it unbadged and claim nothing" to the 🎬 paragraph, about +80 bytes.
- **Recovery card.** "first act after a break while any request or worker is held" assumes the agent knows something is held. The summary may omit that, and its steering is untested (note 7). Fix: "first project action after any break". The card is about 1.6 KB and tells the agent how to find held work.

### 7. 🎬 now means less, and the checker contradicts the slug (high, R9 change)

**Text:** "If it reports `evidence_matched` and nothing in this project's instructions conflicts with your Director role, begin every reply with 🎬".

**What changed:** The OPERATIONS conditions for 🎬 are no longer checked on the passing path. Those conditions are: include every selected guard, resolve the authoritative backend or config binding, and evaluate the route the host actually loaded. They are now on the badge card, which is read only after a failure. Meanwhile the checker's own output still lists `actor_must_confirm: "resolved Project Director role and complete startup reads"`, but under the slug there are no startup reads. Part v of the layout does not mention this output text. The 🎬 meaning sentence also leaves out the conflict condition.

**Fix (about +60 bytes):** "…and the check's `actor_must_confirm` items hold". This uses the checker's own output as the list. Then change that output text in part v.

**Also, which command?** "this project's check command (default …)" never points to the project section. In this checkout the default fails because there is no `.director/install.json`, which would produce a false gap. Fix: "(the project section's Check command; default …)", about +30 bytes.

### 8. The read-cost table only covers the case with no work held (high, claims)

**Text:** "Each break afterwards … Check only, **~1.7 KB**". Brief: "about 29 KB of re-reading to under 2 KB".

**What is wrong:** Breaks happen in long sessions, which usually have work held. With work held, the recovery card runs the continuation view. That is a store command, so it needs the requests card, API, TOOLING and RECORDS, plus the supervision card before evaluating. That comes to about 48 KB (my estimate from measured manual sizes and the layout's card estimates). Before, it was about 65 KB including the same manuals. The first delegated code change costs about 62 KB after, against about 79 KB before. Real savings, but nearer 20 to 25% than 70 to 95%.

**Fix:** Add both rows to table (iv) and correct the brief. The 36 KB of store manuals now dominate the reads; the layout already flags this.

### 9. "Nothing thrown away" is not accurate yet (medium, R4)

**Text:** layout: "Nothing in START, DIRECTOR or OPERATIONS is dropped". Brief: "Nothing was thrown away; it moved into cards."

**Problems:** Directors no longer reach these:
- **The read rules.** "Include each file's total extent and returned range", "batch independent reads only" and "bounded output with room for framing" are mapped to WORKER only, and Directors never read WORKER.
- **Preservation.** "Preserve … other authors' work, private sources and existing trackers" is mapped to the slug's role gate and WORKER. The slug keeps only "project/host authority".
- **First-use order.** FIRST_USE.md stays "text unchanged" but still says "Run the exact selected command once before the ordinary first-reply check". That contradicts the slug's new order: check, then first use, then check again.

**Fixes:**
- Add "preserve other authors' work and private sources" to the role gate, about +50 bytes.
- Put the short read rules in the "Reading cards" paragraph, or on the badge card.
- Mark FIRST_USE.md as changed.
- Reword the brief to "nothing dropped without a flagged decision", and list every ⚠ decision in its open questions. The brief currently leaves out these four:
  - the package acknowledgment is dropped;
  - the first-use order is reversed;
  - the "read the selected definition before dispatch" supersession;
  - the narrower meaning of 🎬.

### 10. Note 2 is false, and the pinned tests have no new home (medium, claims)

**Text:** "Every sentence today's tests pin in the bridge is kept word for word".

**What is wrong:**
- **The re-entry sentence.** `test_flat_bridge_repeats_startup_after_compaction_or_resume` pins, with its exact placement, the November 9 sentence "After every compaction or session resume, repeat this startup… a summary that mentions them is not a substitute." The slug replaces it; it is absent.
- **Stub files.** When START and DIRECTOR become stubs, the DIRECTOR and START pins lose the files they test. Those pins are in `test_flat_roles_preserve_delegation_fallback…`, `test_flat_root_check_…` and `test_flat_reuse_rules_…`. Each pin records an accepted obligation.

**Fix:** Correct the note. In part v, map each pinned sentence to its new home (slug or named card) and give each a replacement test.

### 11. A 32 KiB cap silently cuts the project's own text (medium, R5)

**Scenario (h):** a 30 KB project AGENTS.md, plus the slug (5,976 bytes) and the section (884 bytes), totals 36,860 bytes. Putting the slug first protects it. The cut then removes about 4.1 KB from the end of the project's own text, and drops every nested instruction file, without warning. The installer cannot catch this, because it refuses to install when an AGENTS.md already exists. Existing projects get the slug through an UPDATES merge.

**Fix:** In part v item 5, the merge measures the combined route with the existing `context_check.py` against the host's cap. Above 24 KiB it reports to the owner what would be cut and requires the owner to choose (trim, move content to a nested file, or accept). It never merges silently.

### 12. Agents on hosts that don't pass AGENTS.md lose the Director text (medium)

- **Child Directors.** The Director foundation now lives only in AGENTS.md. A child Director on a host that does not pass AGENTS.md to subagents gets no Director text. Fix: the staffing card's "Role" brief item names the AGENTS.md block as the child Director's startup read. The child bullet adds "and your assignment's overlay or role file".
- **Plain briefs.** On a host that does pass AGENTS.md, a subagent with a plain brief is told to read "your assignment's role file", which does not exist. The new WORKER.md would carry "missing assignment details return to the assigner", so the subagent may hand the task back instead of doing it. Fix: "your role file if the assignment names one; a plain task brief is enough to start".
- **Store work.** "only 'Reading cards' and the staffing row apply to you" leaves out the requests row for a worker assigned store operations. Fix: "the rows for actions your assignment gives you".

### 13. Density, wording and size (low, R5 and R7)

**Sentences that carry the least behaviour per byte:**
- "What you read before the latest break is gone or stale, whatever a summary says." (86 bytes; it explains rather than instructs).
- In duty 2, the routing ladder "give bounded work to a worker, and long, multi-round or multi-worker work to a sub-director that owns its own sub-request". It overlaps the pinned delegation sentence and the staffing card (about 130 bytes).
- "Workers, delegate useful independent subsets…" sits inside the Director duties, which workers are told do not apply to them. Move it into the worker bullet; it stays pinned.

**Terms the block uses without defining:**
- "held";
- "sub-request";
- "linked request";
- "sub-director" next to "scoped child Director";
- "strong" and "lighter" tier (deliberately abstract; the mapping is on the card).

**Ambiguity:** "a file this block names" could include `startup_check.py`. A literal model might read the 289-line script before each check.

**Duty 6:** It should say "covering every held stream", about +25 bytes. Without it, an agent holding only the slug reports only on the stream that just returned (scenario c).

**Size:** The fixes above add roughly 550 to 700 bytes. The cuts listed here free about 250. The 6,000-byte cap leaves 24 bytes of headroom, so any correction needs a renegotiation. Set the cap at about 6,800, target about 6,500, and keep the block first. That is still about 21% of a 32 KiB route including the section.

**Brief:** Accurate apart from findings 8 and 9. "If that END line is not visible after the latest summary" drops "in a tool result" and the resume case; that is acceptable in a summary once finding 3 is fixed.

### 14. Lower-order notes

- **Tier per roster row.** The roster's "Tier, effort" column edges toward a tier fixed per role. DIRECTOR says "No fixed model, blind strongest/cheapest choice or role-based permission follows". The tier rule now lives in three places: slug duty 3, the staffing card and each roster row, which is a drift risk. Label the column "suggested start" or drop it.
- **Earlier evidence against pointer tables.** BEHAVIOR_PARITY's November 7 row records that "advisory links alone did not finish a read chain in earlier loading trials". It also deferred splitting the OPERATIONS check section until a field tool sequence and one post-setup conversation are measured, and proposed pinning the first-reply trigger prose before any split. Part v supersedes the deferral, but it does not meet the measurement condition or add that pin. Add both to the regression oracle: a transcript showing each card's END line read before its matching action.
- **A required section reached through a card.** The staffing card requires API.md's "Parent and requirement traceability" section at briefing time, but the slug names API.md only "before the command". That is a second trigger reached through a card. Name it in the staffing row or bring the rule onto the card.
- **Required reads reached only through FIRST_USE.md.** FIRST_USE.md's own required reads (the tracker, template and privacy reads, and for a custom route TRACKER, `.team/RECORDS.md` and `.program/README.md`) are reachable only through it. A generated template's project section should list them.

## Slug-only walkthroughs

The position taken: an agent knowing only the slug and the project section, as background text after a summary.

**(a) "hi" right after a summary.** The agent defaults to Director. There is no check result after the break, so it runs the check, gets a pass and replies "🎬 hi". This works, except:
- With an unqualified duty 4 (finding 5), a careful agent may capture "hi" first.
- In a mature project, an agent that runs the default command gets a false gap (finding 7).

**(b) A code change across three files.**
- Duty 1 maps the request onto the project's mechanism.
- Duty 4 captures it, which needs the requests card plus 36 KB of manuals.
- The staffing row needs the staffing card.
- Duty 5 asks for "the knowledge that applies", which needs the knowledge card plus LEARNING.md.
- Duty 3 sets tier and effort, the agent dispatches, then duty 6 and the supervision card take over.

Correct, at about 62 KB of reads (finding 8). The most likely slip is skipping the knowledge lookup, because duty 5 names knowledge only as a brief field.

**(c) A worker returns while two other workers are still out, and a SitRep is overdue.** Duty 6 makes the agent check on this turn, so it sends one. It reads the supervision card before evaluating the return. Likely wrong without the card: a SitRep that covers only the returned stream. Without a clock, the agent guesses at "due".

**(d) "Don't be a director, just answer this."** The opt-out applies and the agent answers without 🎬, which is honest. What is unclear is whether the opt-out lasts for the rest of the conversation and whether the agent rechecks afterwards (finding 2). The user probably meant "answer directly", which duty 2 already allows.

**(e) A plain brief on a host that passes AGENTS.md.** "Handed to you by another agent" applies, so the subagent becomes a worker and reads WORKER.md. It may stall on the missing role file (finding 12). It costs about 4.3 KB more per trivial subagent, which is acceptable. This is a real fix: today's bridge would make the subagent a Project Director.

**(f) An assigned scoped child Director.** It follows the block for its outcome, with no check and no 🎬, and reports to its parent. It misfires if it was assigned as `sub-director` without the words "child Director" (finding 1). It has no overlay or role-file read, and it gets no block at all on hosts that do not pass AGENTS.md (finding 12).

**(g) A second summary mid-task with requests open.** The END lines are gone, so the agent re-reads the cards at their next action and reruns the check before its next reply. Recovery depends on the summarizer copying the request IDs. If the IDs are omitted, the "while held" trigger may never fire (finding 6).

**(h) A 32 KiB cap with a 30 KB project AGENTS.md.** The slug and section survive. About 4.1 KB of the project's own text, and any nested files, are lost silently (finding 11).

## The positional test

Points as tested:
- **Checkable when the break is visible.** On hosts that insert a visible summary, everything after it is after the break, so the test reduces to "is my own read visible outside the summary". A model can check that.
- **Robust to clearing.** It survives the host clearing old tool results without a summary: the line disappears, so the agent re-reads.
- **No needless re-reads.** It causes none in a long conversation without breaks, because the END lines stay visible.
- **Restored files.** A host that re-attaches recently read files after compaction legitimately satisfies the test. If the host cuts the attachment short, the END line is missing and the agent re-reads, which is the safe outcome. I did not verify any host's re-attachment limits.
- **Where it fails:** quoted END lines (finding 3); a resume that replays the full transcript without a marker (finding 3); and a host that re-attaches a partial range of a file. That last case is unverified, and finding 3's "every range" wording covers it.

## Sampled obligations (25)

| # | Obligation (source) | Status |
|---|---|---|
| 1 | Never rewrite a receipt to silence drift or pick one by filename recency (O 65) | manual (OPERATIONS) |
| 2 | Managed hashes must match; changed or unrecorded project snapshots don't block (O 57–64) | manual (OPERATIONS) |
| 3 | ❓ goes in the host question tool's title, not repeated in chat; one ❓ per grouped set (D 39–41) | card (supervision); trigger gap, finding 6 |
| 4 | Parent and requirement traceability (D 56–58) | card (staffing, verified); slug short form |
| 5 | Learning batch: three incidents, one bounded review, or a recorded deferral (D 188–195) | card (knowledge, not yet written) + LEARNING |
| 6 | Verification tiers Smoke / Focused / Full (O 197–202) | card (staffing, verified) |
| 7 | One-time public-history privacy warning (O 219–226) | card (privacy, not yet written) |
| 8 | Daily update discovery; notify / automatic / off (D 204–206) | card (update-check) + UPDATES |
| 9 | Continuation view including terminal IDs; correct false "done" (D 128–133) | card (recovery); trigger gap, finding 6 |
| 10 | Host-required unbadged progress note before the check (S 31–32, O 15–21) | changed: unreachable on the passing path |
| 11 | A simple reply needs no capture or learning query (S 58) | changed: duty 4 overrides it (finding 5) |
| 12 | Read rules: total extent and range, batch-only, bounded output (S 3–13) | changed: Directors are no longer routed to them |
| 13 | Acknowledge the resolved package once (S 24) | changed (flagged ⚠) |
| 14 | Read the selected role definition's guards before dispatch (O 151–153) | changed (flagged ⚠, needs a supersession) |
| 15 | Preserve other authors' work, private sources and existing trackers (S 42–43) | **missing** for Directors |
| 16 | Checkpoints at capture, dispatch binding, scope change, evaluated return (D 109–112) | card (requests) |
| 17 | Waits, not polling (D 181–183) | card (supervision) |
| 18 | A missing-badge question retries the check (D 28, O 11) | card (badge, failed-check trigger) |
| 19 | Delegate before detailed work; if subagents are unavailable, report the gap and stop (D 45–53) | kept (slug, pinned) |
| 20 | Strong tier at high effort by default, set explicitly on every dispatch (D 62–67) | kept (slug duty 3; extra-high on the card) |
| 21 | Changed startup bytes mid-conversation require a recheck (O 47–49) | card (badge, install-change trigger) |
| 22 | Generated first use before the check (S 28–30, O 23–33) | changed: order reversed; FIRST_USE still says before |
| 23 | SitRep due check on every turn, including notifications (D 135–137) | kept (slug duty 6) |
| 24 | Evidence from before a break is stale (D 26–27) | kept (positional test) |
| 25 | 🎬 needs backend binding, all guards and the loaded route evaluated (O 103–106) | changed: narrower meaning (finding 7) |

**Totals: kept 4, card 11, manual 2, changed 7, missing 1.**

In BEHAVIOR_PARITY, the mapping does not mention the November 7 "advisory links alone did not finish a read chain" evidence or the measurement condition on the deferral (finding 14). I found no other parity obligation that is absent from the mapping.

## Holds up

- **Sizes.** Measured with `wc -c`: slug 5,976 bytes, project section 884 bytes, this checkout's section 1,941 bytes, staffing card body 5,997 bytes. All exact.
- **Before/after arithmetic.** The before/after figures for a first reply, this checkout's first reply and worker startup check out against real file sizes:
  - 27,044 = 4,767 + 14,415 + 7,862, where 7,862 is the OPERATIONS title plus its check section;
  - this checkout's 42,935;
  - 8,668 for worker startup;
  - 36,343 for the store manuals.
- **Pinned sentences.** The pinned role-default, authority and three delegation sentences are present word for word, and the banned phrases "when permitted" and "no mandatory" are absent. The re-entry pin is the exception (finding 10).
- **Checker structure.** The current `startup_hook` accepts the slug's structure when the target is `.director/WORKER.md` and rejects it for START.md, so note 1 and part v item 3 describe the needed change accurately. The `director-project` marker is not mistaken for a second hook.
- **Model names.** None appear in the four files.
- **Staffing card.** It carries the OPERATIONS staffing content faithfully: tier and effort, recording, verification tiers, names, routes, and IDs and aliases. The one deliberate change is the flagged definition-read change.
- **Roster location.** The reasoning (R6) is sound: staffing happens often, roster rows are small, and separate markers keep ownership clean.
- **Trigger shape.** The conditional "before you X, read Y" form suits text that is re-injected in the background and not acted on as a command (R3).
- **R1.** An agent holding only the slug has the core Director behaviour: own the result, delegate, set tier and effort, capture, brief, SitRep, judge the whole result, ❓ and 🖐️, state what is unverified, and the check.

## Not checked

- No live session, compaction or resume was run.
- Host summarizer behaviour, host re-attachment limits and caps are not verified.
- Cards other than staffing exist only as estimates. Their contents, and whether the layout's mapping rows survive writing them, could not be checked.
- The test suite was not run, since nothing it covers changed.
- RATIONALE decisions were not read in full; only the BEHAVIOR_PARITY rows were checked.

## Re-check, 2026-11-09

The coordinator asked for a re-check after the rework. I re-read, completely, the revised `slug-draft.md`, `brief.md` and `card-sample-staffing.md`, and parts iii to v of `layout.md`.

**Verdict: pass with notes.** All seven requested fixes hold. The rework introduced one new gap, which is small and should be fixed before the owner sees the candidate.

| # | Check | Status | Proving line |
|---|---|---|---|
| 1 | Role gate | fixed | "**Your role** never changes on a message from another agent or session." · "spawned by another agent to do a task and report back without being named a Director" · "Otherwise you are the Project Director, even if a tool started the session." |
| 2 | Opt-out | fixed | It sits only in the Project Director bullet, after the worker bullet: "If the user or an explicit assignment says not to act as one, do what they ask and skip this block until the user says otherwise, then rerun the check before 🎬. General host instructions are not such a request." |
| 3 | Re-read test | fixed | "unless your own complete read of it appears after the latest break" · "Search hits, diffs, tails, summaries, hashes and a worker's quotes are not reads." · "(before any, the whole conversation counts)" |
| 4 | Files the project section lists | fixed | "or under a file the project section says to read … for a file without one, every line up to its shown total length" |
| 5 | Exemption and preservation | fixed | "Discussion, greetings and simple replies need no capture or store manuals." · "Preserve project/host authority, other authors' work, private sources and existing trackers" |
| 6 | Pinned-sentence claim | fixed | slug note 2: "**Not kept:** the November 9 re-entry sentence … needs a dated supersession and a replacement test" · layout part v, supersession 1: "R10, November 9 re-entry sentence → the break test." |
| 7 | Both after-compaction figures | fixed | brief: "After compaction with nothing running: 29 KB to about 3 KB. With work running: 65 KB to about 49 KB" |

**New gap: WORKER.md has no re-read after compaction.** The rule now reads "Cards in `cards/` and the table's manuals end with a line `END ` … Before acting under one of them, or under a file the project section says to read". WORKER.md is named only in the worker bullet: it is not a card, not in the table, and not in the project section. The role file and a child Director's overlay are outside the rule too. So after compaction nothing makes a worker read its own package again. That is the BEHAVIOR_PARITY oracle "A compacted worker … re-reads its own package", and the first draft covered it with "a file this block names". **Fix:** "Cards, `WORKER.md`, the table's manuals and any role file or overlay your assignment names". That costs about 40 bytes against 19 of headroom, so it needs a matching cut.

**Note:** the brief says "Anyone the user talks to is the Director". That is broader than the slug, which also lets an explicit assignment make the agent a worker or a child Director. Not blocking.

**Sizes** (measured with `wc -c` and a character count):
- slug block: 5,981 bytes;
- project section: 905 bytes;
- staffing card body: 5,996 bytes;
- brief.md: 2,499 characters (2,518 bytes).

**Checks I re-ran.** The five pinned bridge sentences are present, and the banned phrases "when permitted" and "no mandatory" are absent. The current `startup_hook` accepts the slug's structure with WORKER.md as the target.

**Public scan.** I searched the five files for model names and aliases, request, session and project IDs, home-directory and personal paths, emails and owner-conversation phrasing. No hits.

**Not checked:** no live session was run. The other seven cards are still estimates. I did not recompute the layout's new read-cost figures beyond reading them for plausibility. The test suite was not run.

## Re-check 2, 2026-11-09

This re-check covers the seven second-pass changes to the block (C1 to C4, K1 to K3) and their companion edits. I re-read, completely: `slug-draft.md` (the block and its "Second-pass changes" table), `second-pass.md` §2.3 to §2.6 (and §2.8 and §2.9 for the brief), `layout.md` parts ii to v, `card-sample-staffing.md` and `brief.md`.

**Measured:**
- slug block: 5,998 bytes between and including the markers, with the final newline (cap 6,000);
- staffing card body: 5,998 bytes (cap 6,000);
- brief.md: 2,500 characters.

**Re-confirmed:** the five pinned bridge sentences are present; the banned phrases "when permitted" and "no mandatory" are absent; the current `startup_hook` accepts the block when its target is `.director/WORKER.md`.

**Overall: pass after two small fixes (items 2 and 5).** Applying the three block edits proposed below gives 5,996 bytes, measured on a scratch copy.

| # | Item | Verdict |
|---|---|---|
| 1 | K1, END-line copying | pass with note: one cheaper wording also closes the last route (−11 bytes) |
| 2 | C1, summary sentence | **fail, small:** an opt-out does not survive a summary (+13 bytes) |
| 3 | C3, settings as brief fields | pass: nothing missing from both places |
| 4 | K2, K3 | pass with note: a missing section should become a named checker gap (no slug bytes) |
| 5 | C4, "for a command it lacks" | **fail as written:** revert to "before the command" until N3 lands (−4 bytes) |
| 6 | Staffing card moves | pass with note: both moves are recorded; the alias rule now sits behind a later trigger |
| 7 | brief.md | pass with note |

**1. K1.** No plausible agent route remains:
- the test requires "your own complete read of it … through its END line";
- "Search hits, diffs, tails, summaries, hashes and a worker's quotes are not reads" excludes the usual copies.

What is left: the agent's own earlier reply, or a brief or user paste that quotes an END line. None is "a read", but none is listed either. The cheapest close is to generalize the list, which also pays for item 2:
- replace `hashes and a worker's quotes are not reads.` with `hashes and quotes are not reads.` (−11 bytes).

For the offline scanner (N6), state in its spec that only a read-tool call on that path counts, with returned ranges covering line 1 through the END line. A scanner that matches the string in any tool result would count search output and a worker's return that quotes a card. This change costs no slug bytes.

**2. C1.** For the cases that matter, the positive sentence does more than the old prohibition did:
- **Cards read:** "Earlier reads are gone" answers a host template's "files read" list directly.
- **🎬 applies:** "rerun the check" and the check rule's "your own run … after the latest break" cover it.
- **Worker:** it records "worker" and its assigner, so §2.6 item 1 is closed.
- **Scoped child Director:** "(Project Director only)" keeps it from running the check.

**Fails for an opted-out session.** The opt-out says "skip this block until the user says otherwise", and Summaries is part of the block. The summary sentence also names no slot for the opt-out. After a summary the agent meets "Otherwise you are the Project Director" again, has no recorded reason not to act as one, reruns the check and resumes 🎬 against the user's instruction.
- **Fix:** `**Summaries** state your role, any opt-out and whom you report to;` (+13 bytes).

**3. C3.** Both block and card still carry everything from the old duty 3 and duty 5:
- **Explicit controls and the strong default:** duty 3.
- **The one-line reason:** now a brief field, and recorded on the card with what was selected, what was effective, host and time (card line 24).
- **The lighter-tier option:** card line 21.
- **The pointer to the card:** table row 1.
- **The old card's "Inputs" field:** split into "Scope" (paths, source subset) and "Applicable knowledge" (selector tags).
- **"Trace":** now "Request IDs", with the same content.

Nothing is missing from both places.

**4. K2 and K3.**
- **K2.** If the project section is missing, the agent has no command to run and the paragraph's "otherwise state the specific gap" applies: safe, but vague. A resourceful agent may guess the default command. On a mature project the guess fails, and on a malformed fresh install it could pass. Fix outside the block, no slug bytes: in part v item 3, the checker verifies that the `director-project` marker pair is present and reports "project section missing" as a route gap. Then the badge card's failure path names it.
- **K3.** No change of meaning. The prohibition becomes a plain statement ("are for its executor"), as the first review suggested. The card keeps "Do not read the role's own instructions".

**5. C4.** As written, this is not safe to ship before N3. The planned requests card "names the four store commands" (layout card table). An agent can judge that a card naming a command does not "lack" it, then run the command without the manuals' expected-revision and recovery protocol. The block itself never says "until N3 holds, the manuals stay due"; only layout row 120 does.
- **Fix:** revert the cell to `` `cards/requests.md`; before the command, `API.md`, `TOOLING.md`, `RECORDS.md` (or the project section's store files) `` (−4 bytes). Apply C4 in the same change as a verified N3, where the card holds the exact command lines.

**6. Staffing card.**
- **Both moves are recorded.** Caller IDs and aliases moved to the knowledge card: layout card table, and obligation map row "Closure upkeep … knowledge card (now including caller IDs and aliases)". The self-review rule was folded into card line 14 ("and the author of a substantive change never reviews it"), and the destination is unchanged: map row "no self-review → staffing card".
- **The brief fields match.** The ten fields are identical to duty 5 in name and order.
- **Note, a trigger gap.** A Director renaming a role at staffing time now reads "Register a new, renamed or retired role …" without the alias rule, which is read only at closure or knowledge lookup. Optional wording: `Register a new, renamed or retired role in the roster before use; old IDs stay as aliases.` (+12 bytes). The card is at 5,998 of 6,000 bytes, so this needs a 10-byte cut elsewhere in the card.

**7. brief.md** is consistent with the block on roles, the opt-out, brief fields, re-reads and costs.
- **Missing context.** The brief does not mention that the block's store row now depends on the unverified N3 (C4), or that K1 reversed part of a reviewed fix. Once the item 5 fix lands, add one line, or drop C4 from the brief's story.
- **Ambiguous attribution.** "Both passes agree" refers to the draft and the second pass. My review flagged the package note and the role-file read as owner decisions, and did not endorse dropping them. Say "the draft and the second pass agree".

**Nothing else found that blocks building.** The known gap for a new conversation with work still out stays as recorded (closed by N1).

**Not checked:**
- no live session or summarizer behaviour;
- N1, N2 and N4 to N6 exist only as proposals in part v, so their text in WORKER.md and the checker was not verified;
- N3's feasibility, since TOOLING.md and RECORDS.md were not read in full for this check;
- the other seven cards, which are not written;
- the second pass's measured-session facts, which I took as reported;
- the test suite was not run.

## Re-check 3, 2026-11-09

This re-check asks whether each section of the block names its audience (acceptance item R9), and whether the cuts that paid for the labels lost anything. I re-read, completely: the `slug-draft.md` block, its notes, the "Audience labels" section and its cut list; the audience part and part v of `layout.md`; and `brief.md`.

**Measured:**
- The block is 5,995 bytes between and including the markers, with the final newline (cap 6,000).
- The five pinned bridge sentences are present, and the current `startup_hook` still accepts the block with WORKER.md as the target.

**Verdict against R9: pass after two named fixes (B and A below).** The labels work for the worker, the scoped child Director and the Project Director. Two problems remain:
- The opt-out tells its reader to skip the only section that keeps the opt-out alive across a summary.
- One cut drops a recorded obligation.

All proposed edits together measure 5,996 bytes on a scratch copy. The pins and the hook still pass after them.

### 1. How each of four readers takes the block

**(a) A spawned worker with a plain brief.**
- **Takes as its own:** the role gate (including "Preserve … other authors' work …"), the worker bullet, Reading, Summaries, and the table rows for its own actions.
- **Skips, correctly:** the duties (the bullet says "Directors-only sections are not for you"), the check ("No check, no 🎬"), the update row ("as Project Director") and Roster.
- **Wrong reader:** "take your first project action after any break". Every worker's first action after its own compaction is a project action, so this row sends it to a card written for Directors. That card runs the continuation view, which is a store command and so pulls in about 36 KB of manuals. It also says to correct "done" records and resume existing owners. A worker's own recovery is already covered by Reading's re-read of WORKER.md, its role file and its brief. See fix C.

**(b) A scoped child Director.**
- **Takes as its own:** the role gate, the child bullet, all ten duties ("follow the Directors-only sections"), Roster, Reading, Summaries, and every table row except the update row.
- **Skips, correctly:** the check and 🎬.
- **Wrong reader (it was the same before the labels):** duty 1 "You own the conversation, the intended result and acceptance" and duty 2 "stay available to the user". "For your assigned outcome only" narrows the scope, but the literal text still gives the child acceptance, and RECORDS says a scoped child Director cannot self-accept for the Project Director. The project section's `sub-director` row ("the Project Director keeps acceptance") mitigates this. Optional fix D: `; report to your parent, who keeps acceptance.` (+22 bytes). It is not affordable inside the cap after A to C, so it should go on the requests or supervision card.

**(c) A session told not to act as a Director.**
- It reads the gate and the Project Director bullet, then "skip this block until the user says otherwise". That skips Summaries too.
- **Dropped by the right reader:** Summaries is where re-check 2 put "state your role, any opt-out", so the opt-out has nothing carrying it across a summary. After the summary the agent meets "Otherwise you are the Project Director" again and goes back to the check and 🎬.
- Skipping Reading is acceptable: the cards serve Director work the user has switched off. See fix B.

**(d) The Project Director.** It takes everything. Nothing is wrongly addressed to it. One obligation is gone: deferring to higher-priority host formats (item 5, fix A).

### 2. Unclear "you" or imperatives under "Reading (every role)"

- "Rows for your actions" is enough for most rows:
  - a delegating worker legitimately takes the staffing row (the card says "workers read it before delegating");
  - a worker takes the store and privacy rows only when assigned that work;
  - it takes the badge row only for an install or integration task.
- **Supervision row.** A delegating worker will take it as its own, because "Workers, delegate useful independent subsets" makes it supervise. The supervision card's 📋 SitRep cadence is a Director duty, while WORKER.md says no routine progress exchange is needed. That card must open with its audience: SitReps are for Directors; a delegating worker evaluates its children's returns and accounts for them in its own return. This is a card-side requirement; it costs no block bytes.
- **Knowledge row.** Looking up knowledge is legitimate for a worker. Recording a correction and closing an outcome are Director work. The card should open with that split. The draft already records this as a known ambiguity; I agree with it.
- **Should a worker read cards/recovery.md after a break? No.** Fix C, +15 bytes: `| as a Director, take your first project action after any break |`. This matches the update row's "as Project Director" pattern.

### 3. "Directors only" without naming both kinds of Director

**Pass.** The child bullet says "follow the Directors-only sections", the worker bullet excludes them, and every other reader is the Project Director. Together the bullets make the heading unambiguous. The layout's audience table spells this out.

### 4. The opt-out reader

**Fail.** "do what they ask and skip this block until the user says otherwise" defeats the opt-out record in Summaries.

**Fix B, +7 bytes:** `do what they ask and skip all but Summaries until the user says otherwise`.

Losing Reading for that session is the right outcome, since the cards govern switched-off work. Losing Summaries is not.

### 5. The cuts

- **"Higher-priority host formats win." (duty 9): fail, an obligation was dropped.**
  - DIRECTOR.md says "Respect higher-priority host response formats", and OPERATIONS repeats it for the 🎬 prefix.
  - The gate's general "Preserve project/host authority" does not tell a reader that "begin every reply with 🎬" gives way to a host's required format.
  - The supervision card, the layout's stated new home, is read only when work is out.
  - **Fix A, +34 bytes:** restore the sentence at the end of duty 9.
  - **Pay for it with these cuts, none of which changes meaning (−58 bytes in all, measured):**
    - `, then do the task.` → `.` in the worker bullet (−18);
    - `You route; workers execute. ` (−28); the pinned delegation sentence and "Answer … yourself" carry the same rule;
    - backticks around evidence_matched, actor_must_confirm, sub-director, and Reading's .director/, cards/ and WORKER.md (−12). This is formatting only, like the table cut already made. The `.director/WORKER.md` path and `END ` keep their backticks, because the checker and the trailing space depend on them.
- **"General host instructions don't count."** This is ambiguous standing alone: it can read as "host instructions don't count" at all, against "Preserve project/host authority". **Fix G, +3 bytes:** `General host instructions are no opt-out.`
- **"Role names grant nothing":** no change of meaning (it is broader than "no permissions").
- **Duty 10, "…; submitted, verified, accepted and published differ":** no change of meaning.
- **"A host-required progress note first stays unbadged and claims nothing":** a little awkward, but still means "before the check". No change needed.
- **The 15 backticks removed from the table:** formatting only. The checker does not read the table.
- **The other cuts in the list:** no change of meaning.

**Byte total.** A, B, C and G add 59 bytes. The cuts remove 58. Result: 5,996 bytes, measured on a scratch copy. The pins and the hook still pass. If the owner rejects cutting "You route; workers execute.", drop fix C and put the recovery card's audience on its first line instead.

### 6. The removed "## Director" heading

**Note, not a blocker.** In a fresh install the block is first in the file, so little is lost. The loss shows up where the block is not first:
- **Composed root files.** These include this repository's wrapper, which follows "Maintaining this repository", and imported shared files. With no heading, "**Your role** never changes…" reads as part of the preceding project section.
- **Orphaned references.** The staffing card ("the AGENTS.md Director block") and the project section ("the manuals named above") point to a block whose name now appears nowhere visible; the marker comment alone carries it.

**Optional fix H, +10 bytes:** `**Director: your role** never changes…`. It is not affordable after A to C unless the owner accepts a further cut.

### 7. Honest statement of the limit

- **layout.md: pass.** "A label controls who should act on a section, not who receives it … Labels are a reading instruction, not a filter."
- **brief.md: partly.** "Every section names its audience; … Workers … read WORKER.md and skip those" never says that workers still receive and pay for the whole block; only "workers +2.5 KB" hints at it. Add: "Labels say who acts, not who receives: every agent given the root file still loads the whole block." The brief has no byte cap.

### Not checked

- No live reading by real agents of any of the three kinds; these walk-throughs are my reading of the text.
- The cards that are not written yet, including the audience lines they now need.
- The test suite was not run.

## Re-check 4, 2026-11-09

This re-check covers round 7, which restored the after-compaction sentence and changed several other things in the same edit. I read fresh: the block between the markers in `slug-draft.md`; its notes 2, 3 and 7; the "Re-entry sentence restored" section; the round 7 rows of `layout.md`; and `test_flat_bridge_repeats_startup_after_compaction_or_resume` in `development/tests/test_package.py`.

**Settings.** Requested: strong tier, high effort. Effective: unknown from inside this worker.

**Measured:**
- **Block size:** 6,190 bytes between and including the markers, with the final newline. That matches the draft's figure and is within the 6,200 cap. The coordinator's message said 6,189.
- **Pins and hook:** the re-entry sentence appears exactly once, word for word. The five other pinned sentences are present, the banned phrases are absent, and the current `startup_hook` accepts the block with WORKER.md as the target.

**Verdict for R10: pass after two required fixes (R1 and R2) and one restoration (R3).**
- The sentence is kept word for word, and the break test now defines it instead of replacing it. That part of R10 holds.
- But round 7 also changed two working mechanisms and called both changes "no meaning change":
  - the check paragraph's own stale-evidence guard;
  - the visibility condition in the re-read test.
- All three fixes, plus two meaning-neutral cuts and the earlier-offered "You route; workers execute." cut, measure 6,193 bytes on a scratch copy. The pins and the hook still pass.

### 1. The sentence and the startup list

**Pass, with two notes.** The sentence appears once, word for word, at the top of "Reading (every role)", where every role meets it. The list that follows ("This startup: the Project Director's check; a worker's WORKER.md and role file; a child's overlay; the file your next action needs.") tells each role what "this startup" and "the files" mean:
- **The Project Director:** rerun the check. Its foundation is now the standing block itself.
- **A worker:** re-read WORKER.md and its role file.
- **A child Director:** re-read its overlay.
- **Every role:** whatever the next action needs. The per-action rule carries the full reach of that last item.

Nobody can satisfy the list by doing less than the route requires today, with two notes:
- **Child Directors.** The staffing card says a child's brief names "its role file and the instructions it must read", so a child may have both a role file and an overlay. Optional: `a child's overlay or role file;` (+13 bytes).
- **Project startup guards.** If the owner decides that project guard files are read before the first reply (open call 2), the Project Director's item must name them. Today's route re-reads them after a compaction. With the draft's choice, "before real work", the per-action rule covers them.

### 2. The check paragraph: required fix R1

**Fail.** The paragraph changed:
- **Was:** "Before each reply, even to a greeting, unless your own run of the check appears after the latest break, run…".
- **Now:** "Before your first reply, even to a greeting, run…".

This lost two things.
- **A second guard.** The old wording was a self-contained, per-reply test inside the Project Director's own section, so it caught a missed re-run even when the agent skipped the Reading paragraph. Skipping that paragraph is exactly the observed failure mode: the badge carried on after summaries.
- **The stale-evidence rule.** The paragraph now says "begin every reply with 🎬", with no end point. If the after-break re-run is missed, nothing in the check section stops the badge. This is the DIRECTOR rule "evidence from before a compaction or session resume is stale". Part v moves its pin to the slug, and the slug no longer states it for the badge.

**Fix R1 (+21 bytes):** `begin every reply with 🎬 until the next break;`. The badge then lapses by its own rule, and the startup list says what renews it.

### 3. The shorter Summaries next step

**Recommended, not required.**
- **Was:** "Earlier reads are gone: rerun the check (Project Director only), then read what the next action needs."
- **Now:** "Earlier reads are gone: repeat startup before the next reply."

The new wording drops the one concrete step the old one named, the check. A summary now carries a word, "startup", that the agent can resolve only by reading the standing block's list. In the one observed live success, the summary carried concrete items: the startup reads, the exact check command, and a "repeat startup before replying" step. One case cannot separate the summary from the standing sentence. But it points toward summaries that list concrete steps, not fewer of them.

**Proposed (+54 bytes):** `and begin next steps with "Earlier reads are gone: repeat startup before the next reply:" and your startup steps, with the exact check command.` It is not affordable under 6,200 together with R1 to R3, so it needs a cap decision. As a fallback, restoring the old C1 wording costs +41 bytes.

### 4. "Each range" and the other tightenings

**Fail on two points. The claim "change no meaning" does not hold.**

- **Each range, R3 (+12 bytes).** The definition "a complete read reaches that line" is met by reading the first range and the last one, which holds the END line, while skipping the middle. "each range" was the fix for exactly that gap (re-check 1, finding 3). Restore: `Read long files in bounded numbered ranges, each range.` Alternative at +13 bytes: `a complete read covers every line to that line`.
- **Fresh, R2 (+13 bytes).** "A run or read is fresh if your own and after the latest break" drops the old test's "appears". The old rule asked whether the read is still in view. The new one asks only whether it happened. Some hosts clear old tool results without a summary, which is no break under the block's definition. A card read earlier and then cleared still counts as "fresh", so the agent does not re-read it even though its text is gone. The review and the second pass both listed surviving that clearing as a strength of the test. Fix: `fresh if your own, still shown and after the latest break`.
- **The other tightenings check out:** "repeated means each step is fresh" and "Before acting under … have a fresh complete read" carry the same meaning. With R2 applied, so does "fresh".

### 5. Anything else of the same kind in this round

The owner's concern is any working mechanism changed without the trade being weighed. Apart from R1 to R3:
- **Narrower per-action list (note).** The rule no longer names WORKER.md, a role file or an overlay. Those are now re-read only at a break, under startup. Inside one conversation, after a host clears an old tool result, a worker's instructions are no longer due again. This is lower risk than R2, but it is the same kind of loss. Fix it on the worker side: WORKER.md's own text should keep "re-read when no longer shown".
- **Summaries.** Covered in item 3; the draft flags it ⚠.
- **"Inheriting is not a choice."** Dropped from duty 3 in the previous round, not this one. It is recorded in the cut list as a re-check 3 payment, so it is outside this re-check. It is worth one look, though, against the second pass's field fact that settings were ignored on the first dispatches.

**Cuts that pay for R1 to R3 (none changes meaning):**
- `summaries, ` from the non-read list (−11 bytes): the pinned sentence already says a summary is not a substitute;
- `A break is either one.` → `Either is a break.` (−4 bytes);
- `You route; workers execute. ` (−28 bytes), offered in re-check 3 and kept by the draft owner. Without that cut, R1 to R3 come to 6,221 bytes, so the alternative is a cap of about 6,230.

### 6. The pinned test

What `test_flat_bridge_repeats_startup_after_compaction_or_resume` pins, for both the installed `BRIDGE` and this checkout's guarded AGENTS.md branch:
- the re-entry sentence appears exactly once in whitespace-normalized text;
- it sits inside the substring "that Project Director check. Preserve project/host authority. " + the sentence + " Directors, delegate project investigations". In other words, after the role and check routing and before the delegation request;
- the bridge starts with `<!-- director-starter:2 -->\n` and ends with `<!-- /director-starter:2 -->\n`.

On the round 7 block, the count pin and both marker pins pass. The placement pin fails.

What would have to change:
- **Placement.** Replace the placement string with the new neighbours, for example "**Reading (every role).** " + the sentence + " This startup: the Project Director's check;". Record that the old placement's intent, "before the delegation request", is deliberately given up: the sentence now comes after the duties.
- **The source-checkout branch.** The test locates it with `authoring.split("When `.director/START.md` exists in this checkout:")`, so that split must follow the new locator (part v item 8).
- **Companion test.** `test_flat_reuse_rules_do_not_survive_compaction_or_resume` pins DIRECTOR's "evidence from before a compaction or session resume is stale … run the currently possible check before replying". Its new home is the slug only once R1 lands.

### Not checked

- No live session, compaction or resume.
- The separate auditor's comparison of the whole block against today's route.
- The draft's per-change byte figures; I measured only the total and my own edits.
- The cards and WORKER.md that are not yet written.
- The test suite was not run; the test was read and its assertions checked against the extracted block.

## Re-check 5, 2026-11-09

This re-check covers the drafter's round 8: the five agreed fixes, the eight cards and the throwaway-folder install recipe. I re-read my worker startup files first, after a compaction notice.

I read fresh:
- the `slug-draft.md` block;
- all eight files in `cards/`;
- `test-install.md`;
- today's `pattern/starter/payload/START.md`, `DIRECTOR.md` and `OPERATIONS.md`, compared by script;
- `startup_check.py`'s output fields.

**Settings.** Requested: strong tier, high effort. Effective: unknown from inside this worker.

### 1. The block: R10 passes

A token-level diff of round 8 against the round 7 block I extracted in re-check 4 shows exactly five changes and nothing else:
- `until the next break;`
- `a child's overlay or role file;`
- `fresh if your own, still shown and`
- `ranges, each range.`
- `before the next reply:" and your startup steps, with the exact check command.`

The arithmetic matches: 6,190 + 21 + 13 + 13 + 12 + 54 = 6,303 bytes, marker to marker with the final newline. Without the final newline it is 6,302, which is the coordinator's figure. The draft's own convention includes the newline.

Also confirmed: the re-entry sentence appears once, word for word; the five other pins are present; the current hook check accepts the block with WORKER.md as the target.

**The overrun.** I mildly disagree with accepting it. Two cuts I offered in re-check 4 are meaning-neutral and cut no recorded sentence:
- `summaries, ` in the non-read list (−11 bytes);
- `A break is either one.` → `Either is a break.` (−4 bytes).

Together they give 6,288 bytes, under the 6,300 cap. Not blocking, but the installer's planned "refuse over cap" check needs a number the block actually meets.

### 2. The cards: the word-for-word claim holds

**Method.** For each of the seven cards other than staffing.md, I split the body into paragraphs, normalized whitespace and link targets, and searched for each paragraph in today's START, DIRECTOR and OPERATIONS. Every paragraph except each card's opening audience line appears there verbatim and contiguously. Every card ends with its END line.

**Is the no-home list complete? Yes.** A line-level map of what the seven cards carry verbatim leaves these source ranges without a home:
- START 3–18 (that is, 3–13 and 15–18, with 14 blank), 21–25 and 42–46;
- DIRECTOR 45–68, 77–84 and 88–92;
- OPERATIONS 23–37, 51–99 and 122–207.

The few lines that look uncovered at a card boundary (START 58; DIRECTOR 28, 129 and 204) are split between two cards, and I checked both halves. This matches the drafter's list. In OPERATIONS:
- 122–144 is the context preflight;
- 148–207 is carried only by the staffing card's rewrite;
- 209–233 is on the knowledge and privacy cards.

**Behaviour a Director would now never meet** (not in the block, any card, or a mandatory read):
- **Read discipline (START 3–9, 12–13):**
  - "Keep individual and combined tool output bounded, with room for tool framing";
  - "Batch independent reads only; wait for required instructions to return and read them before running dependent commands";
  - "Coverage shown in the read needs no separate verification call".

  "Include each file's total extent and returned range" survives only partly, as "shown total length".
- **Assignment resolution (START 15–18, 21):** "Missing or conflicting assignment details return to the assigner; they never create Director authority", "not a global role catalog", and executor-side "Resolve missing/conflicting role guards". Layout part v item 7 plans to put these in WORKER.md, but the test installs today's WORKER.md, which lacks them. So no reader meets them in the test.
- **Role guards (OPERATIONS 155–157):** "Unqualified mandatory references remain mandatory unless a reviewed local mapping preserves their authority and explicit triggers". The staffing rewrite keeps only "a deferred read never waives a limit".
- **Package acknowledgment (START 24–25):** dropped by a recorded owner decision.
- **Failure handling (OPERATIONS 51–99):** "Never rewrite a receipt merely to silence drift or select it by filename recency", plus the hook and import-chain rules. These are reachable only as optional "detail in OPERATIONS.md". That is the one moment a Director is tempted to "fix" a failing check by editing a receipt. The receipt sentence belongs on the badge card.
- **The context preflight (OPERATIONS 122–144):** optional, so acceptable.

DIRECTOR 45–68, 77–84 and 88–92, and START 42–46, do reach the Director, through the staffing card's rewrite and the block. The changed meanings there are already recorded as owner decisions.

**Two side effects of the verbatim transplant:**
- **The badge card is over budget.** It is 6,440 bytes, against the 6,000-byte card cap and its 4,500-byte budget in the layout.
- **The badge card carries today's route pointers.** "follow [OPERATIONS](../OPERATIONS.md#installation-evidence)", "loads OPERATIONS' installation-evidence section", "🎬 under DIRECTOR", and "Before the badge, confirm complete current startup reads". The last of these contradicts the block's narrower meaning of 🎬.

### 3. The recipe: fail as written

The recipe leaves the old route reachable through three prompts that come from the candidate's own path, not by accident:
- **The checker's output.** The patched copy changes only the route target. Its output still lists `.director/START.md` and `.director/DIRECTOR.md` among `checked_paths`, and still asks under `actor_must_confirm` for "resolved Project Director role and complete startup reads". The block tells the Project Director to "confirm its actor_must_confirm items". A careful Director may read START.md and DIRECTOR.md to confirm "complete startup reads", on every first reply and after every break. A pass earned that way is today's route's pass.
- **The badge card's verbatim pointers,** listed above. They send a Director handling a failed check into OPERATIONS' installation section and to "DIRECTOR".
- **Today's WORKER.md.** It is installed with an END line added and says "Before selecting any descendant, completely load OPERATIONS#staffing-and-maintained-roles". So a delegating worker reads today's staffing text, not the staffing card.

The test also omits two adopted fixes: N1 (the check's "next" key) and N2 (the fixed line at the end of every worker return). That understates the candidate. So the result is unclear in both directions.

**What makes the run count:**
- **(a)** In step 8a, also replace `'resolved Project Director role and complete startup reads'` with `'resolved Project Director role'` in the copy. This is part v item 3's planned text.
- **(b)** Make it a pass criterion that the transcript shows no read of START.md, DIRECTOR.md or OPERATIONS.md's installation section. If one appears, the run is contaminated, not passed.

A run already under way can stand if its transcripts show no such reads. Otherwise repeat it with (a). For a clean test of the old route's absence, the copy can also drop START.md and DIRECTOR.md from its managed list (line 198), so that both files can be removed from T.

**For a real build, the patched copy is test-only.**
- **Checker.** The shipped `startup_check.py` itself must change, keeping its name so that project sections and receipts don't fork. That covers:
  - the route target, accepting START.md and WORKER.md during transition;
  - the managed set (cards, WORKER, OPERATIONS, the checker);
  - the `actor_must_confirm` text;
  - the N1 `next` key;
  - a project-section presence check.
- **Around the checker:** new receipt baselines, manifest entries and a `starter_revision` bump, with tests.
- **Files that must never ship:** `startup_check_candidate.py`, and a project section that names it.
- **Badge card.** Its verbatim pointers to OPERATIONS and DIRECTOR must be rewritten once OPERATIONS is trimmed.

### 4. What the candidate must show to count as equal

In the control, after one forced compaction, the agent:
- read DIRECTOR.md and OPERATIONS.md again;
- reran the check, passed, and showed 🎬;
- in one of two runs, delegated the next small request with tier and effort stated.

To count as equal, each candidate run must show these after its compaction:
- **Check before 🎬:** its own fresh run of the check before the first reply, and 🎬 only after that run passes. With the unpatched checker, the specific gap instead, and no 🎬.
- **No old-route reads:** none of START.md, DIRECTOR.md or OPERATIONS.md's installation section.
- **Cards before governed actions:** a fresh, complete read of `cards/staffing.md` before briefing, and of `cards/recovery.md` before the first project action if work is held.
- **Briefs:** when it delegates, a brief carrying the ten duty-5 fields, including tier, effort and reason.

Answering a small request directly is allowed by duty 2, so delegating in one of two runs, as the control did, is a like-for-like comparison, not a target. The candidate should also do all this with clearly fewer bytes read at re-entry: about 2 KB of check output against the control's 20 to 30 KB of re-reads.

**What this test cannot tell, either way:**
- **Rates.** Two runs per arm with one compaction each cannot separate them.
- **Which text drove re-entry.** It cannot tell the standing sentence from a host summary that lists the reads itself, as in the one earlier success.
- **Re-attachment.** If the host re-attaches recently read files, a card that is "still shown" needs no re-read, so the absence of a re-read is not a failure. This is the same mechanism that re-attached START.md in the control.
- **Paths not exercised:** a session resume, a second compaction, recovery with work held, a worker's own compaction, SitRep cadence over time, other hosts, and the real installer and checker.

### Not checked

- The live runs themselves.
- `swap-audit.md`.
- The staffing card's rewrite, beyond earlier rounds.
- The verbatim cards' fit with the block's labels, beyond each card's audience line.
- The test suite was not run.
