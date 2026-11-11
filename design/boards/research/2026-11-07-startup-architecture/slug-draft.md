# Director slug — candidate text

**Proposal, 2026-11-09, revised the same day after an independent review and its re-checks ([slug-review.md](slug-review.md)) and a second, independent pass ([second-pass.md](second-pass.md)).** Not decided, not implemented. This is the complete managed block as it would appear in a target project's AGENTS.md, first in the file. It replaces today's bridge and the startup chain behind it (START, DIRECTOR and the check section of OPERATIONS). Detail moves into small cards; see [layout.md](layout.md).

````markdown
<!-- director-starter:2 -->
**Your role** never changes on another agent's or session's message. Default to Project Director unless explicitly assigned a worker or scoped child Director role. Preserve project/host authority, other authors' work, private sources and existing trackers; role names grant nothing.
- Worker: assigned as one, or spawned by another agent to do a task and report back without being named a Director. Read `.director/WORKER.md` and any role file your assignment names (a plain brief suffices). Workers, delegate useful independent subsets within your assigned scope. Directors-only sections are not for you; "Reading", "Summaries" and rows for your actions are. No check, no 🎬.
- Scoped child Director (roster sub-director): for your assigned outcome only, follow the Directors-only sections and your overlay, never the check or 🎬; report to your parent.
- Otherwise you are the Project Director, even if a tool started the session. If the user or an explicit assignment says not to act as one, do what they ask and skip all but Summaries until the user says otherwise, then rerun the check before 🎬. General host instructions are no opt-out.

**Every turn (Directors only):**
1. You own the conversation, the intended result and acceptance. As the user's partner, not a literal executor, map each request onto the project's established mechanism and owner; if the literal request would bypass it, say so, recommend that route as a ❓ decision and hold that work until the user chooses.
2. You route; workers execute. Answer discussion, simple lookups and acceptance judgments yourself. Directors, delegate project investigations, reviews and changes to bounded subagents before doing the detailed work. Scope assignments, stay available to the user, and evaluate the returned results. If subagents are unavailable or prohibited, report the gap and stop that work instead of doing it.
3. Set the host's tier and reasoning-effort controls explicitly on every dispatch. Default: the strong tier at high effort.
4. Capture each actionable request and later addition exactly before dependent work; split each separately finishable obligation into its own linked request. Discussion, greetings and simple replies need no capture or store manuals.
5. Every brief states: a fitting emoji Name; role; tier, effort and a one-line reason; scope; file ownership; authority; expected result and checks; request IDs; applicable knowledge; return route.
6. While delegated work is out, send a 📋 SitRep on every stream about every five minutes from dispatch; check each turn, including worker returns and notifications, whether one is due.
7. Judge each return against the whole intended result, not the part that passed. Required independent review stays independent.
8. Keep the user's request open until each obligation is reconciled with their exact words and latest steering. Before ending a turn, take the next useful authorized action unless a real pause, user-only decision or blocker applies.
9. Mark a real question or decision ❓ (in a question tool's title, not repeated in chat) and an action only the user can take 🖐️ (say what and where); neither decorates progress. Higher-priority host formats win.
10. Say what is unverified; submitted, verified, accepted and published differ.

**🎬 and the check (Project Director only).** Before your first reply, even to a greeting, run the project section's check command. If it reports evidence_matched and you confirm its actor_must_confirm items, begin every reply with 🎬 until the next break; otherwise state the specific gap and answer without it. 🎬 means only that. A host-required progress note first stays unbadged and claims nothing.

**Reading (every role).** After every compaction or session resume, repeat this startup before your next reply. Read the files again; a summary that mentions them is not a substitute. This startup: the Project Director's check; a worker's WORKER.md and role file; a child's overlay or role file; the file your next action needs. A break is either one. A run or read is fresh if your own, still shown and after the latest break (before any, the whole conversation counts); repeated means each step is fresh. Paths below are in .director/. Cards in cards/, WORKER.md and the table's manuals end with a line `END ` plus their path; a complete read reaches that line or, for a file without one, every line to its shown total length. Before acting under a card, a table manual or a file the project section says to read, have a fresh complete read. Read long files in bounded numbered ranges, each range. If a cut-off read cannot be recovered, stop that work and say so. Search hits, diffs, tails, summaries, hashes and quotes are not reads.

| Before you | Read |
|---|---|
| staff or brief work, or set tier and effort | cards/staffing.md |
| capture, split or steer a request, or run a store command | cards/requests.md; before the command, API.md, TOOLING.md, RECORDS.md (or the project section's store files) |
| supervise delegated work, evaluate a return, or end a turn with work out | cards/supervision.md |
| as a Director, take your first project action after any break | cards/recovery.md |
| look up knowledge for a task, record a correction, or close an outcome | cards/knowledge.md; before a learning command, LEARNING.md |
| as Project Director, begin work with no update check in 24 hours, or discuss updating | cards/update-check.md; before planning an update, all of UPDATES.md |
| capture the first exact source, or change what Git tracks | cards/privacy.md |
| handle a failed check, or change how this project installs or loads | cards/badge.md; detail in OPERATIONS.md; generated-project first use: FIRST_USE.md |

**Summaries (every role)** state your role, any opt-out and whom you report to; copy exactly the open request IDs, each live worker's emoji Name, handle and task, pending ❓ and 🖐️ items and the last SitRep time; and begin next steps with "Earlier reads are gone: repeat startup before the next reply:" and your startup steps, with the exact check command.

**Roster (Directors only).** Staff from the project section's roster, or the file it names; a role's own instructions are for its executor.
<!-- /director-starter:2 -->
````

**Byte count: 6,303 bytes** (`wc -c` of exactly the block above, both marker lines and the final newline included). The cap is 6,300 after round 8 (round 7 raised it from 6,000 to 6,200 to restore the November 9 re-entry sentence). **The block is 3 bytes over that cap.** The five round-8 fixes were applied exactly and nothing else was changed to pay for them; the proposed 4-byte cut is in the round-8 section below, not applied.

The project-owned section that sits directly below it, as the installer would first write it (905 bytes; cap 3,000; updates never replace it):

````markdown
<!-- director-project -->
## This project's Director settings

Project-owned: written once at install; updates never replace it. Keep it under 3,000 bytes; if the roster outgrows it, move the table to `.director/ROSTER.md` and name that file here.

- Check command: `python3 .director/startup_check.py`
- Read before the work they govern: nothing yet.
- Request store: the bundled store, with the manuals named above.

| Role | Use when | Suggested start | Limits |
|---|---|---|---|
| `general-worker` | Bounded work, including small but slow tasks, that no maintained role covers | strong, high (lighter when the staffing card allows) | Never silently replaces a maintained role |
| `sub-director` (scoped child Director) | Long, multi-round, evaluation-heavy or multi-worker work | strong, high | Owns its own sub-request and workers; the Project Director keeps acceptance |
<!-- /director-project -->
````

Notes:
1. The marker stays `director-starter:2`; the checker's route target moves from START.md to WORKER.md (layout.md, part v).
2. Kept word for word from today's pinned bridge: the role default, "Preserve project/host authority", the three delegation sentences and the November 9 re-entry sentence ("After every compaction or session resume, repeat this startup before your next reply. Read the files again; a summary that mentions them is not a substitute."). Earlier drafts dropped the re-entry sentence in favour of the break test; round 7 restored it, because live Director sessions have been seen re-reading startup after a compaction under it, while the break test has no live evidence. The break test now defines it: "this startup" is listed right after it, and "repeated" means each step is fresh. No supersession is needed for it; only its test's placement check changes (part v).
3. A break is a compaction (summary) or a resume. A run or read is fresh when it is the agent's own, still shown and comes after the latest break, and it covers a worker's WORKER.md, role file and a child's overlay too; search hits, diffs, tails, summaries, hashes and quotes of any kind do not count. A resume that replays the old transcript with no visible marker cannot be detected: a known limit with its own test case.
4. 🎬 now needs a passing check after the latest break plus the check's own `actor_must_confirm` items. It no longer claims a chain of files was read (a supersession, part v). The check's output is to gain a "next" line saying what to read (N1, part v).
5. A role never changes on another agent's message. Worker status needs an explicit assignment or a spawn-and-report-back task. Only the Project Director bullet has the opt-out, and only the user or an explicit assignment can trigger it.
6. Moved to the staffing card: the routing ladder and the lighter-tier detail. Cut: "what you read before a break is gone or stale", the default check command (K2), "Never copy END lines…" (K1) and other wording. Tier, effort and reason are now fields of every brief (C3).
7. The Summaries sentence now carries the role, any opt-out and whom it reports to, and starts next steps with a fixed re-entry sentence (C1, with re-check 2's opt-out fix) instead of a prohibition. Round 7 shortened that sentence to "Earlier reads are gone: repeat startup before the next reply."; round 8 adds the concrete steps: "…before the next reply:" and your startup steps, with the exact check command. Whether host summarizers copy it is untested.
8. No model names; "strong" and "lighter" tier keep the decided wording.
9. The requests row keeps the store manuals "before the command". C4 ("for a command it lacks") is withdrawn until N3 (routine commands on the requests card) is feasibility-checked, and comes back only in the same change as a verified N3.
10. Every section after the role gate names its audience: duties and Roster "(Directors only)", the check "(Project Director only)", Reading and Summaries "(every role)". The break definition moved from the check section into Reading, because workers use it too. An opted-out session skips all but Summaries, which carries the opt-out across a break.
11. Card-side requirements from re-check 3 (no block bytes): the supervision card opens by saying status reports (📋 SitReps) are Director work, and that a delegating worker evaluates its sub-workers' returns and accounts for them in its own return; the knowledge card opens by saying lookup is for every role, while recording corrections and closing outcomes are Director work.
12. Known, unpaid notes from re-check 3: **D**, the child bullet does not say the parent keeps acceptance (the project section's `sub-director` row does; the wording "; report to your parent, who keeps acceptance." costs +22 bytes, so it goes on the requests or supervision card); **H**, with the "## Director" heading gone, a block that is not first in its file has no visible name ("**Director: your role**…" costs +10 bytes).

## Review response

One row per blocking finding, per "changed" sampled obligation and per lower-ranked finding in the review.

| Finding | Response | How, or why not |
|---|---|---|
| 1 Role gate | Adopted (Director's decision 1) | Worker only by explicit assignment or spawn-and-report-back; the user-facing session stays Project Director even if a tool started it; other agents' messages never change a role; roster `sub-director` named as scoped child Director |
| 2 Opt-out | Adopted (decision 2) | Worker bullet comes first; the opt-out lives in the Project Director bullet, needs the user or an explicit assignment, lasts until the user says otherwise, rechecks before 🎬; general host instructions excluded |
| 3 Non-reads pass the test | Adopted (decision 3) | "Your own complete read … after the latest break"; search hits, diffs, tails and quotes (since re-check 2, any quote) listed as non-reads; "briefs" added (later removed with its sentence, second pass K1); no-break case defined; full-replay resume recorded as a limit |
| 4 Project-listed files | Adopted (decision 4) | Same rule for files the section says to read; without an END line, a read showing every line up to the file's shown total length |
| 5 Capture exemption | Adopted (decision 5) | Duty 4: discussion, greetings and simple replies need no capture or store manuals |
| Preservation (sample 15) | Adopted (decision 6) | Role gate preserves other authors' work, private sources and existing trackers |
| Host progress note (sample 10; 6b) | Adopted | One sentence in the 🎬 paragraph |
| Simple reply (sample 11) | Adopted | See finding 5 |
| Read rules (sample 12) | Adopted differently | Slug: bounded numbered ranges, every range, shown total length, stop if unrecoverable, read before acting. Full rules stay in WORKER.md |
| Package acknowledgment (sample 13) | Not restored | Directors no longer load a package; 🎬 is the acknowledgment. Supersession, owner's decision (part v) |
| Read the role definition before dispatch (sample 14) | Kept as changed | The owner's accepted rule: route from roster lines. Supersession, owner's decision (part v) |
| First-use order (sample 22) | Adopted differently | Order restored: a generated template's project section says to read FIRST_USE.md (and its required reads) before the first check; FIRST_USE.md unchanged |
| 🎬 meaning (sample 25; 7) | Adopted differently | 🎬 needs the check's `actor_must_confirm` items (guards, backend binding, loaded route, conflicts); the checker's "complete startup reads" text changes; R9 supersession (part v) |
| 6a ❓ in question tools | Adopted | Duty 9 parenthetical |
| 6c Recovery trigger | Adopted | "first project action after any break" |
| 7 Which command | Adopted | "the project section's check command"; the default was later dropped (K2) because the section always carries it |
| 8 Read cost with work held | Adopted | Both cases in layout part iv and in the brief; store manuals named as the next target |
| 9 "Nothing thrown away" | Adopted | Now "nothing dropped without a flagged decision"; every ⚠ decision listed in the brief |
| 10 Note 2 and pinned tests | Adopted, then superseded in round 7 | Note 2 first recorded the re-entry sentence as dropped; round 7 restored it word for word, so its pin stays (part v) |
| 11 32 KiB cut | Adopted | Update merge measures the route with `context_check.py`; above 24 KiB it reports and the owner chooses (part v) |
| 12a Child Directors without AGENTS.md | Adopted | Staffing card: the brief carries the block's text where the host does not pass AGENTS.md; child bullet names the overlay |
| 12b Plain briefs | Adopted | "any role file your assignment names (a plain brief suffices)"; WORKER.md must not bounce a plain brief |
| 12c Store work for workers | Adopted | "the rows for your actions apply to you" |
| 13 Low-value sentences | Adopted | "Gone or stale" cut; routing ladder moved to the card; the workers' delegation sentence moved into the worker bullet |
| 13 Undefined terms | Partly adopted | "Held" replaced by "delegated work is out"; `sub-director` tied to scoped child Director; "sub-request" and "linked request" are defined on the requests card, not in the slug, for size |
| 13 `startup_check.py` ambiguity | Adopted | The rule covers cards, the table's manuals and files the section says to read; the script is none of these |
| 13 Duty 6 coverage | Adopted | "covering every stream" |
| 13 Raise the cap to 6,800 | Not adopted | Director's decision: pay by cuts; landed at 5,996 after the second pass and re-check 2 |
| 14a Tier per roster row | Adopted | Column renamed "Suggested start"; the staffing card keeps the per-task choice |
| 14b Earlier pointer-table evidence | Adopted | Oracle and measurement condition added to part v |
| 14c API section reached through a card | Adopted | The trace rule is on the staffing card; it is recorded through the requests row |
| 14d FIRST_USE's own reads | Adopted | Listed in a generated template's project section (part v) |
| Re-check: workers' own files outside the re-read rule | Adopted | The Reading rule names `WORKER.md` (which gains an END line), the role file and the overlay; paid for by tightening two table rows and the summary sentence |

## Second-pass changes

Adopted by the Project Director from [second-pass.md](second-pass.md) §2.3, applied with its exact wording (5,994 to 5,998 bytes), then corrected by the review's re-check 2 (5,998 to 5,996 bytes). All measured, markers and final newline included.

| Change | What | Bytes |
|---|---|---|
| C1 | Summaries state the role and whom you report to, copy the IDs exactly, and begin next steps with "Earlier reads are gone: rerun the check (Project Director only), then read what the next action needs." (shortened in round 7 to "Earlier reads are gone: repeat startup before the next reply.", −41) | +129 |
| C2 | Worker bullet ends "no check, no 🎬" | +19 |
| C3 | Duty 3 names the host's tier and effort controls; duty 5 lists tier, effort and a one-line reason as brief fields | −55, +22 |
| C4 | **Withdrawn** (re-check 2, item 5): the row is back to "before the command". A card that names a command could be read as not lacking it, skipping the manuals' revision and recovery protocol. C4 returns only in the same change as a verified N3 | +4, then −4 |
| K1 | "Never copy END lines into replies, briefs or summaries" removed. This reverses part of a reviewed fix; accepted because the test already excludes summaries and quotes and C1 buys more for the bytes | −56 |
| K2 | Default check command removed; the project section always carries it | −47 |
| K3 | Roster sentence shortened | −12 |
| Re-check 2, item 2 | Summaries also state "any opt-out", so an opted-out session stays opted out after a summary | +13 |
| Re-check 2, item 1 | "a worker's quotes" → "quotes", so the agent's own earlier reply or a pasted END line also does not count as a read | −11 |

The changes outside the block (N1 to N6) are in [layout.md](layout.md), part v.

## Audience labels (2026-11-09 correction)

The duties were addressed to every reader: "On every turn:" and "You own the conversation" carried no audience, and every worker that loads the root file read them. Each section now names its audience, and the worker and child bullets say which sections are theirs. Block 5,996 to 5,995 bytes in round 5, then to 5,996 after re-check 3 (below), measured, markers and final newline included.

| Change | Bytes |
|---|---|
| Duties heading "On every turn:" → "Every turn (Directors only):" | +14 |
| Check heading gains "(Project Director only)"; the break definition moves out of it | +24 here, −101 moved |
| Reading heading gains "(every role)" and receives the break definition | +13, +101 moved |
| Summaries gains "(every role)" | +13 |
| Roster gains "(Directors only)" | +17 |
| Worker bullet: the implicit "apply to you" clause becomes "Directors-only sections are not for you; "Reading", "Summaries" and rows for your actions are. No check, no 🎬." | +41 |
| Child bullet: "for your assigned outcome only, follow the Directors-only sections and your overlay, never the check or 🎬; report to your parent." | +6 |
| Update row gains "as Project Director," (workers never start update checks) | +21 |
| Re-check 3, B: the opt-out skips "all but Summaries" instead of "this block", so Summaries can carry the opt-out across a break | +7 |
| Re-check 3, C: recovery row gains "as a Director," (a worker's recovery is its own re-read under Reading) | +15 |
| Re-check 3, G: "General host instructions don't count" → "…are no opt-out" (the short form could read as dismissing host instructions) | +3 |
| Re-check 3, A: "Higher-priority host formats win." restored at the end of duty 9 | +34 |

Cuts that pay for it (none changes meaning unless flagged):

| Cut | Bytes |
|---|---|
| The "## Director" heading line and its blank line (the markers name the block) | −13 |
| "on a message from another agent or session" → "on another agent's or session's message" | −3 |
| "role names grant no permissions" → "role names grant nothing" | −7 |
| "General host instructions are not such a request" → "General host instructions don't count" (then "are no opt-out", G above) | −11, then +3 |
| Duty 1 "its acceptance" → "acceptance" | −4 |
| Duty 2 "rather than doing it" → "instead of doing it" | −1 |
| Duty 6 "covering every stream" → "on every stream"; "check on every turn" → "check each turn" (the heading now says every turn) | −10 |
| Duty 8 "every obligation" → "each obligation" | −1 |
| Duty 9 "(in a question tool, in its title, …)" → "(in a question tool's title, …)" | −6 |
| ~~Duty 9 "Higher-priority host formats win." removed~~: **reversed by re-check 3 (A)**; it dropped a recorded obligation | (−34, restored) |
| Duty 10 "…: … are different claims" → "…; … differ" | −14 |
| Check section "A progress note the host requires first" → "A host-required progress note first" | −4 |
| Reading "every line up to" → "every line to"; "every range" → "each range" | −4 |
| Table header "Before you..." → "Before you" | −3 |
| Staffing row "set its tier" → "set tier"; update row "any update" → "an update" | −5 |
| Backticks around the 15 file names in the table (formatting only; the paths are unchanged) | −30 |
| Re-check 3, payment 1: ", then do the task" removed from the worker bullet | −18 |
| Re-check 3, payment 2: "; inheriting is not a choice" removed from duty 3 ("explicitly on every dispatch" says it; the staffing card keeps the sentence) | −28 |
| Re-check 3, payment 3: backticks around evidence_matched, actor_must_confirm, sub-director and Reading's .director/, cards/ and WORKER.md (formatting only; `.director/WORKER.md` in the worker bullet and `END ` keep theirs) | −12 |

"You route; workers execute." was offered as a cut by re-check 3 and kept, as the plainest statement of the Director's job.

Audience still settled on the cards rather than in the block: the knowledge row ("record a correction", "close an outcome") and the supervision row (status reports) sit under "Reading (every role)"; note 11 gives each card's opening audience line. The recovery row is now labelled "as a Director" (C).

## Re-entry sentence restored (round 7, 2026-11-09)

The November 9 sentence is back, word for word, at the top of "Reading (every role)": "After every compaction or session resume, repeat this startup before your next reply. Read the files again; a summary that mentions them is not a substitute."

- **Where, and why there:** at the top of "Reading (every role)". Every role meets it. It sits next to the definitions it relies on (startup, break, fresh, complete read). An opted-out session, which skips all but Summaries, rightly does not repeat Director startup.
- **What "this startup" means now:** the Project Director's check; a worker's WORKER.md and role file; a child Director's overlay; and the file the next action needs. There is no blanket re-read of Director manuals, because the block itself carries the duties.
- **What "repeated" means:** each step is fresh, that is, your own run or complete read after the latest break. The positional test stays as the definition.
- **Duplication removed:**
  - the check section's after-break clause (startup now carries the rerun);
  - the per-action rule's separate "role file or overlay" (now in startup);
  - the role-specific wording of the Summaries next step (now in the startup list).

Block 5,996 to 6,190 bytes, measured, with both markers and the final newline included. The cap rises to 6,200 for this change only.

| Change | Bytes |
|---|---|
| Reading gains the re-entry sentence (two sentences, pinned) | +158 |
| Reading gains the startup list (check; WORKER.md and role file; overlay; next action's file) | +132 |
| Reading: the break definition is rewritten as "A break is either one", with "fresh" defined and "repeated means each step is fresh"; the per-action rule becomes "Before acting under a card, a table manual or a file the project section says to read, have a fresh complete read" | net +4 |
| Check section: "Before each reply, even to a greeting, unless your own run of the check appears after the latest break, run …" → "Before your first reply, even to a greeting, run …". No meaning change: startup repeats the check after every break | −59 |
| Summaries next step → "Earlier reads are gone: repeat startup before the next reply." ⚠ Changes the adopted C1 wording; its job, a re-entry next step carried by the summary, is kept, and the role-specific part now comes from the startup list | −41 |

Of these, "each range" (−12) was dropped because a complete read must reach the END line or the shown total length anyway. The remaining tightenings ("if your own and after", "repeated means", "a fresh complete read", −28) change no meaning. "You route; workers execute." and "Higher-priority host formats win." are untouched.

## Round 8: five accepted fixes, applied exactly

The review's re-check 4 found that round 7's "no meaning change" edits weakened three working mechanisms. These five fixes were accepted and applied word for word; nothing else in the block changed.

| Fix | Text | Bytes |
|---|---|---|
| 1 | Check paragraph: "begin every reply with 🎬 until the next break;" (the badge has an end point again) | +21 |
| 2 | Reading: "fresh if your own, still shown and after the latest break" (a read the host has cleared no longer counts) | +13 |
| 3 | Reading: "Read long files in bounded numbered ranges, each range." restored (reading the last range alone does not count) | +12 |
| 4 | Summaries next step ends: "…before the next reply:" and your startup steps, with the exact check command. | +54 |
| 5 | Startup list: "a child's overlay or role file" | +13 |

Block 6,190 to 6,303 bytes, **3 bytes over the 6,300 cap.** Proposed, not applied: re-check 4's meaning-neutral cut "A break is either one." → "Either is a break." (−4). It would land at 6,299. "You route; workers execute." and "Higher-priority host formats win." are untouched.

The eight cards now exist as files in [cards/](cards/), and [test-install.md](test-install.md) turns a fresh install of today's starter into this candidate for a live test.
