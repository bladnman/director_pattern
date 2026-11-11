# The Director slug: a second pass

## Summary

**Verdict: keep with changes.** **[fact]** Before reading the draft, this pass reached nearly the same design: rules in the root block, role routing, an action-to-file table, small cards read on need, a badge that lapses at every summary.

The weak point is the trigger. **[hypothesis]** The END-line test soundly defines what is in context and suits an offline check. But nothing fresh makes a compacted agent ask it.

Three changes matter most:

1. **Give the question a fresh asker.** The summary states the role and begins its next steps with "earlier reads are gone: rerun the check". The check's output and every worker return repeat it at no slug cost.
2. **Make dispatch settings a field of every brief,** and tell workers "no check, no 🎬".
3. **Put routine store commands on the requests card,** so 36 KB of manuals are not due after each summary.

**[fact]** With matching cuts the block is 5,998 bytes of 6,000.

**Test:** one scratch project, seven short sessions. Force a real summary, then request a tempting small change. Look for a fresh check, a card read before the first dispatch, no edit by the Director. Pass: two of three runs.

---

*Assessment and proposal, 2026-11-09, by a second, independent strongest-tier pass. Nothing was changed, decided or implemented. No live session was run. Statements are labelled **[fact]**, **[hypothesis]** or **[proposal]**. The rest of this file is: Phase 1 (my own design, frozen before reading the draft), Phase 2 (the candidate judged), the live test, the risks, and what was not checked.*

## Phase 1: my own design

Written before opening the brief, the draft slug, the layout, the sample card or the review. Nothing in this section was changed after reading them.

### 1.1 How a compacted model behaves (the model I reason from)

**[fact, from the report]** After a summary the host gives back the root instruction file and a summary. In 21 measured compactions there was no complete re-read. Dispatching came back within minutes. Settings, status reports and capture discipline slipped.

**[hypothesis]** A compacted agent re-reads a file for only four reasons. Strongest first:

1. **A fresh message tells it to.** A user message or a tool result that arrives after the summary. This is live instruction.
2. **The summary's own "next step" says so.** The host tells the agent to carry on with the last task. The summary defines that task.
3. **It needs a concrete thing it does not have.** A path, a command line, a template, a table row. Agents look these up without being told. They do not feel that they lack a *rule*; they do feel that they lack a *path*.
4. **A standing rule, tied to the action it is about to take, states a condition it can check by looking.**

Today's block uses none of these. It gives a one-time order ("read this before your first reply", "after compaction repeat startup"). A one-time order can be marked done. The summary marks it done ("the files were read"). The agent believes the summary, because the summary also carries the gist of the rules, and gist feels like knowledge.

**[hypothesis]** This is why a state-conditional line works better than an order. An order is discharged once. A precondition about the present ("you hold this file only while its text is in front of you") cannot be discharged by history. It is evaluated again each time the action comes up.

**[fact, from the report]** Form-shaped duties held after compaction and judgment-shaped duties slipped. Settings were ignored on the first five dispatches even with the staffing text fully in context. So some failures are not about re-reading at all. They need the duty turned into a form field.

### 1.2 What must be in the root block

**[proposal]** Design the block so that an agent which never re-reads anything is still a Director. A missed re-read should cost precision, not the role. That means the block carries rules, not only pointers:

- **Role routing first, default last.** Worker, child Director and opt-out branches come before the Director default, so a worker leaves early and does not absorb the Director identity.
- **The every-turn rules, in full, one line each.** Own the conversation and the result. Delegate before doing detail work; if there are no sub-agents, stop that work. The badge and what it depends on. The dispatch form. Independent review. The status report and its interval. Capture and split user inputs. The two user markers. Map a request onto the project's existing mechanism. Evaluate returns against the whole result and keep going until done.
- **The dispatch form as a field list.** Name, role, tier, effort, reason, scope, owned files, checks, owner, return route. A form gets filled in. A paragraph about choosing settings gets skipped.
- **The need table.** One line per action: the action, then the file it needs. Every secondary file is reachable from the block in one hop.
- **A statement of fact about summaries.** What a summary deletes, and the rule that a file is held only while its text is visible below the latest summary. Default is "not held".
- **Summary steering.** Three lines addressed to whoever writes the summary.
- **One line of read discipline.** Read completely, through the last line; a note, a search hit or a hash is not a read.

### 1.3 What must not be in the root block

- One-time orders ("read X now", "before your first reply read Y"). They cost bytes and are the part that fails.
- Anything that claims a state ("you have read", "startup is complete").
- Reasons, history, disclaimers, "does not prove" clauses.
- Receipt formats, hook variants, backend options, update procedure, privacy procedure. One trigger line each, no more.
- Install-specific values that change, such as a receipt file name. The block is one constant for every install.
- The project's roster rows (see 1.6).
- Model names. Tier words only.
- The long status-report example. It belongs in a card.
- Director identity text placed above the role branch.

### 1.4 The re-read mechanism

**[proposal]** Use all four routes from 1.1, not only the weakest one. In order of value for cost:

**A. Steer the summary.** The summary is what defeats the re-read today. Turn it into what triggers it. The block tells the summary writer to: record the role; write "instruction files held: none, badge lapsed"; never write that files were read; copy request IDs, live worker names, handles, tiers and the last report time exactly; and make the first next step "run the check, then read what the next action needs". **[hypothesis]** At least one host documents that summary instructions in the root file are honoured. Others may ignore them. So this is one layer, not the method.

**B. Default-deny by possession, not by memory.** The test is not "did you read it". The test is "can you see its text now, below the latest summary". If unsure, the answer is no. This needs no extra bytes, only different wording.

**C. Bait.** Put in each card something the action cannot be done without: the role's file path, the command line, the form. Put the rules above it in the same card. The agent goes for the data and passes through the rules. This is why the rules for staffing and the roster belong together, and why the block should not carry enough data to dispatch a maintained role without opening anything.

**D. Fresh carriers that need no host hook.** Three exist on every host:
   - *The check.* The badge already depends on it. Make the badge lapse at every summary, so the one command a Director has a reason to run is also the re-entry step. Let its output name what to do on failure, so the pass path needs no manual.
   - *Worker returns.* A return arrives as a fresh tool result at the exact moment the Director must evaluate. Have every worker end its return with one fixed line that names the evaluation card. Sub-agents become the reminder. Workers started before the summary still send it.
   - *Helper output.* A short footer on every request-store command (the report already adopted this).

**E. A visible receipt.** After a summary, the first reply says in one line what was re-run and re-read. The user can see re-entry happen or not happen. A scanner can check it. Writing the line without doing the work would be a false statement, which an agent avoids.

**F. An end line on each card.** Useful as proof that a read was complete, and for an offline scanner. **[hypothesis]** Weak as a trigger: an agent that never asks itself the question never looks for the line. And a predictable line can be "remembered" without being present, because the block itself must describe it. I would keep it for completeness and for the oracle, and not lean on it.

Read lazily, not eagerly. An eager "re-read everything after a summary" is the bloat again, and it was never done in the measured sessions. Re-read only what the next action needs: one to four kilobytes at a time.

### 1.5 Roles and opt-out

**[proposal]** Four branches, tested top down:

1. An assignment names a worker or a role: worker. Needs the worker file and the role file the assignment names. The block carries the worker's hard rules inline (do only the assignment, return to the assigner, never take the badge or the default), so a small search sub-agent that reads nothing still behaves.
2. An assignment creates a Director for one outcome: Director rules inside that scope, no badge, no check.
3. The user said not to direct in this conversation: an ordinary assistant under the project's other rules. The rest of the block is skipped until the user says otherwise.
4. None of these: Project Director.

Role is conversation state, so it is lost at a summary unless the summary carries it. The steering in A makes the summary carry it. Without that, a compacted worker can wake up as a Director, and a session the user opted out of can come back as one.

### 1.6 The roster

**[proposal]** One short project-owned file under the installation folder, named from the block. Not in the block. Reasons:

- The block is one managed constant for all installs. Roster rows are project-specific and grow.
- A roster is lookup data. Agents fetch lookup data when they need it. It is the best bait for the staffing rules.
- Every worker and sub-agent pays for the block. They do not need the roster.

What the block does carry: that maintained roles exist, that a generic worker never replaces a fitting one, and the settings default. A small project may add one project-owned line of role IDs below the block. That is an option, not the default.

### 1.7 Cutting what is read up front

**[fact, from the report]** Today: 43 to 50 KB before a first reply in the live install, 29 to 37 KB in the payload, and about 28 KB more once the request-store manuals are needed.

**[proposal]**

| Moment | Today | Proposed |
|---|---|---|
| First reply | 43 to 50 KB in five files plus a section | The block (4 to 6 KB, already loaded by the host) plus the check's output. No file reads on the pass path |
| First dispatch | already paid | Staffing card, roster, project guards: about 6 to 10 KB |
| First request-store action | plus about 28 KB of manuals | Store card: about 3 KB. The full manuals only for unusual operations |
| After each summary | nothing was re-read | The check, then one card per action: 1 to 4 KB each |

That is roughly 85% less before the first reply. A full working session ends near 15 to 22 KB, loaded in small pieces that can each be loaded again.

Two costs to state plainly:

- The badge must be redefined. Today it asserts that the startup files and guards were read. Under this design it means: role resolved, the check passed below the latest summary. That overrides a recorded deferral and needs a dated decision.
- Nothing is dropped, but about 100 obligations move. Each needs a row saying where it went: a block line, a card, or a manual with a trigger line in the block. Until that table exists and is reviewed, this is a proposal.

### 1.8 My own sketch of the block

About 3,800 bytes with markers. It is a sketch to compare against, not a tested text.

```text
Your context, as fact. Hosts summarize long conversations. A summary deletes the
text of every file you read and keeps only a note that you read it. This block
comes back; the files do not. You hold a file only while its text is visible below
the latest summary, in a tool result or attachment. A note that it was read is not
the file. When unsure, you do not hold it.

Who you are. Decide first; a summary's record of your role stands.
- An assignment names you a worker or gives you a role: you are a worker. You need
  WORKER.md and the role file the assignment names. Do only the assignment. Return
  to whoever assigned you. Never take the badge or the Director default. End each
  return with the line "Owner: evaluate before accepting (cards/evaluate.md)."
- An assignment makes you Director of one outcome: the Director rules below apply
  inside that scope, without the badge or the check.
- The user said not to direct here: you are an ordinary assistant under the
  project's other rules. Skip the rest of this block until the user says otherwise.
- None of these: you are the Project Director.

Project Director, every turn. These hold with no file held.
1. You own the conversation, the result and acceptance. Answer discussion and simple
   lookups yourself. Hand each investigation, review and change to a sub-agent before
   doing detailed work. No sub-agents: say so and stop that work.
2. The badge starts every reply only while the check has passed below the latest
   summary. If it has not, run it before replying. If it fails, name the gap and
   answer without the badge.
3. Every dispatch states: emoji Name, role, tier, effort, a one-line reason, scope,
   files owned, checks, owner, return route. Set the host's tier and effort controls
   to match; inheriting is not a choice. Default: strongest tier, high effort. Go
   lighter only for small, well-specified, easily checked work.
4. The author of a change never supplies its required independent review.
5. While work is out, send a status report about every five minutes: Done, In
   progress (who, what, status), Waiting on you, Next. Check every turn if one is due.
6. Capture each actionable user input exactly, and split independent asks, before
   dependent work.
7. One marker for a real question to the user, with a recommendation. One marker
   for a step only the user can take.
8. Map each request onto the project's existing mechanism. If the literal ask
   bypasses it, say so and recommend the established route.
9. Evaluate each return against the whole intended result before accepting.
   Continue until the whole outcome is done or truly blocked.

What each action needs. If you do not hold it, read it completely, through its last
line, before the action.
- dispatch; choose role, tier or effort: staffing card, roster
- change, dispatch or accept anything in the project: project guards
- record or read requests: store card
- a worker returns: evaluation card
- a full status report: report card
- call an outcome done, or stop with work open: closing card
- the check fails, or first use: operations manual
- plan a pattern update: updates manual
- a learning review is due: learning manual

When you write a summary of this conversation: state the role. Write "instruction
files held: none; badge lapsed". Never write that files were read. Copy open request
IDs, live worker names, handles, tiers and the last report time exactly. Make the
first next step "run the check, then read what the next action needs".
After a summary, your first reply says in one line what you re-ran and re-read.
```

## Phase 2: the candidate, judged against Phase 1

Read after Phase 1 was frozen: the brief, the draft block, the layout, the sample staffing card and the review. Byte figures marked "measured" come from applying each replacement to the exact 5,994-byte block with a script and counting UTF-8 bytes.

### 2.1 Where the candidate is right

- Rules live in the block, not only pointers. An agent that re-reads nothing still routes, delegates and reports.
- The worker branch comes first. The Director default is the last branch.
- Only the user or an explicit assignment can switch the Director off. Another agent's message cannot change a role.
- 🎬 lapses at every break, so the one command a Director has a reason to run is also the re-entry step.
- 🎬 claims a passed check, not a chain of reads. An agent can keep that claim true.
- The table is keyed to actions. Every secondary file is one hop from the root file.
- Cards stay under 6 KB and are read on need. **[fact]** The eager 27 KB re-read happened in none of 21 measured compactions.
- "Break" covers a summary and a resume, and the case with no break is defined.
- The test asks what is in context after the break, not what the agent remembers reading.
- Tier and effort are explicit on every dispatch, strong and high by default, with no model names.
- The managed block and the project's section sit under separate markers. Updates never touch the project's part.
- Greetings and discussion need no capture, so "hi" does not cost 36 KB of manuals.
- The block is first in the file, with a 24 KiB guide and a measured merge. A capped host cuts other text first.
- The review response is honest. Every finding has a row. Every changed meaning is flagged for a dated decision.

### 2.2 Where reading it changed my Phase 1 view

- **The roster belongs in the root file.** Phase 1 put it in its own file, as bait for the staffing rules. The candidate puts it in a project-owned section under the block. The candidate is right. **[hypothesis]** Staffing happens on most working turns, the rows survive a summary there, and the separate markers keep the managed block constant.
- **The price of that choice.** The block plus the roster are now enough to dispatch. The staffing card has lost its bait. **[hypothesis]** After a summary it will often stay unopened. So anything that must happen on every dispatch has to be a form in the block, not a rule on the card. Change C3 follows from this.
- **One steering sentence is enough,** if it is the right one. Phase 1 used three lines. See C1.
- **Workers can be sent to their own file** instead of carrying hard rules inline, now that the Reading rule covers that file after a break.

### 2.3 Changes inside the block

**[proposal]** Five wording changes and three cuts. Net +4 bytes: 5,994 to 5,998, measured, markers and final newline included.

**C1. The summary carries the role and the next step (+129).**

Old:

```text
**Summaries** copy exactly the open request IDs, each live worker's emoji Name, handle and task, pending ❓ and 🖐️ items and the last SitRep time; they never claim cards were read or 🎬.
```

New:

```text
**Summaries** state your role and whom you report to; copy exactly the open request IDs, each live worker's emoji Name, handle and task, pending ❓ and 🖐️ items and the last SitRep time; and begin next steps with "Earlier reads are gone: rerun the check (Project Director only), then read what the next action needs."
```

Why. **[hypothesis]** After a summary the strongest standing carrier is the summary's own next step. The host tells the agent to carry on, and the summary says with what. The draft's sentence says what to copy and what not to claim. It does not say what to do next, and it does not carry the role. A prohibition also fights host summary templates that ask for a list of files read (**[fact]**, seen on one host during this pass). A sentence to copy fits the template's next-step slot. Only two facts have to survive a chain of summaries: the role, and "rerun the check". The check and the table supply the rest. The words "earlier reads are gone" are chosen so they cannot be misread as "no work is out".

**C2. Workers: no check, no 🎬 (+19).**

Old (end of the Worker bullet):

```text
"Reading" and the rows for your actions apply to you.
```

New:

```text
"Reading" and the rows for your actions apply to you; no check, no 🎬.
```

Why. **[fact]** Today's block says workers and child Directors skip the Project Director check. The draft says so for the child only. Its check paragraph begins "Before each reply, even to a greeting" and names no role. On hosts that pass the root file to sub-agents, every worker reads that paragraph.

**C3. Dispatch settings become a field of the brief (duty 3: −55; duty 5: +22).**

Old duty 3:

```text
3. Set tier and reasoning effort explicitly on every dispatch; inheriting is not a choice. Default: the strong tier at high effort; the staffing card says when a lighter tier fits. Record a one-line reason.
```

New duty 3:

```text
3. Set the host's tier and reasoning-effort controls explicitly on every dispatch; inheriting is not a choice. Default: the strong tier at high effort.
```

Old duty 5:

```text
5. Brief each worker with its role, scope, file ownership, authority, expected result and checks, request IDs, applicable knowledge and return route, and a fitting emoji Name.
```

New duty 5:

```text
5. Every brief states: a fitting emoji Name; role; tier, effort and a one-line reason; scope; file ownership; authority; expected result and checks; request IDs; applicable knowledge; return route.
```

Why. **[fact]** In the measured sessions, settings were ignored on the first five dispatches with the staffing text fully in context. Duties shaped like a form held; duties shaped like a judgment slipped. The draft's duty 3 is a rule, and its "Record a one-line reason" names no place to record it. The draft's duty 5 lists what a brief holds, and the settings are not on the list. With tier, effort and reason on the list, the Director writes the setting on every dispatch. "The host's … controls" points at the real parameter, not at a sentence in the brief. The dropped pointer to the staffing card is already table row 1. An agent that never opens the card stays on strong and high, which is the safe side. **[fact, from the report]** The report also proposes that the store helper refuse a dispatch record without these fields. This change makes the block agree with that.

**C4. Store manuals only for what the card lacks (+4).** It goes with N3 below.

Old (Requests row, right cell):

```text
`cards/requests.md`; before the command, `API.md`, `TOOLING.md`, `RECORDS.md` (or the project section's store files)
```

New:

```text
`cards/requests.md`; for a command it lacks, `API.md`, `TOOLING.md`, `RECORDS.md` (or the project section's store files)
```

**The cuts that pay for it.**

K1 (−56). Remove this sentence from the Reading paragraph:

```text
Never copy END lines into replies, briefs or summaries.
```

Why this one. It is a second guard on a hole the test already closes: the test asks for "your own complete read", and summaries and a worker's quotes are listed as non-reads. The sentence also plants the exact string it warns about. The review added "briefs" to it, so this cut reverses part of a reviewed fix. The new argument is that C1 does more for the same bytes.

K2 (−47). In the check paragraph:

```text
run the project section's check command (default `python3 .director/startup_check.py`).
```

becomes

```text
run the project section's check command.
```

Why. The project section always carries the command. **[fact, from the review]** The default was wrong for at least one install. If the section is missing, the paragraph's own rule applies: state the gap and answer without 🎬.

K3 (−12). The Roster paragraph:

```text
**Roster.** Choose workers from the project section's roster, or the file it names. Read a role's own instructions only to execute it.
```

becomes

```text
**Roster.** Staff from the project section's roster, or the file it names; a role's own instructions are for its executor.
```

| Change | Bytes (measured) |
|---|---|
| C1 summary sentence | +129 |
| C2 worker bullet | +19 |
| C3 duty 3 | −55 |
| C3 duty 5 | +22 |
| C4 requests row | +4 |
| K1 | −56 |
| K2 | −47 |
| K3 | −12 |
| **Net** | **+4, giving 5,998** |

If only part can be afforded, the order is C1, then C2, then C3.

Measured but not proposed now:

- Widening the recovery row to "take your first project action in a conversation or after any break": +21. N1 covers it at no cost.
- A visible re-entry line in the block: +96. N5 covers it at no cost.
- The role paragraph's default sentence is 95 bytes, and the third bullet restates it. It is pinned by a test, so cutting it needs a test change and a recorded decision. It is the first place to look if room is ever needed.

### 2.4 Changes outside the block (no slug bytes)

**N1. The check's output says what to do next. [proposal]** Add one key to the check's passing and failing output (200 bytes):

```text
"next": "Files read before the latest summary or resume are gone. Before your first project action read .director/cards/recovery.md. Before each action in the AGENTS.md table, read the card it names."
```

Why. The check's output is a fresh tool result. It arrives at the start of every conversation and after every break, which is when the reminder is needed. It is not a hook and needs no host setting. It is the output of a command the Director already runs, and the layout already plans an edit to this output.

**N2. Every worker return ends with one fixed line. [proposal]** Add to the worker file (176 bytes):

```text
End every return with this line: `Owner: a submission, not acceptance. Read .director/cards/supervision.md before accepting, unless you have read it since your latest summary.`
```

Why. Workers start with a fresh context and read their file. Their return lands in the Director's context as a fresh tool result, at the moment of evaluation. Workers started before a summary still send it afterwards. **[hypothesis]** This raises the supervision card's read rate more than any wording in the block can.

**N3. Routine store commands go on the requests card. [proposal]** **[fact, from the layout]** With work out, a break costs about 48.7 KB, and 36,343 bytes of that are the three store manuals. The layout names this as the next target and defers it. Do it in the same change. Put the exact command lines for capture, split, steer, dispatch record, continuation view and close on the card. Keep the manuals for everything else (C4). From the layout's own figures: a break with work out falls from about 48.7 KB to about 12 to 14 KB, and a first delegated change from about 64.4 KB to about 28 to 30 KB. Why now. **[hypothesis]** A 36 KB read after a summary is the read most likely to be skipped, and it stands in front of the continuation view, the step that finds work still out. It needs a dated supersession of "manuals before store commands" and a test that the card's lines match the manuals. Feasibility is not verified: the two larger manuals were only skimmed.

**N4. The project section says where role files are. [proposal]** One line (70 bytes of the section's 3,000):

```text
- Role files: `.director/roles/<role>.md`; name the file in the brief.
```

Why. **[fact]** The draft's roster table has four columns, and none is a path. The block and the staffing card both expect a brief to name the role file. Today's staffing text sends the staffer to the project's role discovery pointer. Without a locator the Director has to search, or the worker gets no role file.

**N5. The recovery card asks for a visible re-entry line. [proposal]** The first reply after the card is read carries one short line, for example `Re-entered: check run, recovery card read.` It costs no slug bytes. The user sees re-entry happen. A scanner can count the breaks that lack it.

**N6. A transcript scanner is the real oracle. [proposal]** A maintainer script over exported transcripts. For each break it reports: was the check run before the first reply, and did an own complete read of the card come before each governed action. Without it an unread card is invisible, because the block alone produces plausible behaviour.

Low priority: the staffing card is at 5,996 of 6,000 bytes. Keep the brief fields and the tier rule first, and let the last section move out if the card grows.

### 2.5 Will the END-line re-read test work?

**As a test of what is in context: yes. [hypothesis]** It tests what is in front of the agent, not what is remembered. It catches a cut-off read. It survives a host that clears old tool results. It gives the right answer for restored files. **[fact, one host, this pass]** After a summary the host re-attached five recently read files, the sample card among them, complete through its END line, and kept the latest exchange word for word. In both cases the text really is in context.

**As an offline oracle: yes.** A scanner can find an END line in the agent's own tool result after a break marker.

**As a trigger: not on its own. [hypothesis]** Where it can fail:

1. **Nobody asks.** The test is a condition inside standing text. The block is good enough to act on, so nothing forces the question. **[fact]** After the measured summaries the badge carried on in about 13 segments and dispatching resumed within minutes, with no re-read.
2. **The check rule has the same shape.** "Unless your own run of the check appears after the latest break" is also a silent self-test. If it is skipped, the one fresh carrier goes with it.
3. **The summary speaks first.** Host templates ask for files read and for a next step. A summary that says "read the staffing card; continue the dispatch" reads as "already read". The draft forbids that claim and supplies nothing in its place.
4. **The line is predictable.** The block describes it, so an agent can believe it saw it. "Your own complete read" limits this. It cannot remove it.
5. **The recovery row is tied to an event,** "first project action after any break", not to an action the agent can see itself about to take. Rows tied to events are the weakest kind.
6. **Cost.** With work out, the next step is a 36 KB read. Expensive reads get skipped (N3).
7. **A resume that replays the whole transcript with no marker.** The draft records this as a known limit. Agreed.

**What would be stronger.** Keep the test. Add askers that arrive fresh: the summary's next step (C1), the check's output (N1), worker returns (N2). Turn duties that apply to every dispatch into a form (C3). Make the costly read cheap (N3). Make re-entry visible and countable (N5, N6). None of this needs a hook, a compiler, a host-specific file or a skill.

### 2.6 What neither the draft nor its review saw

1. **Role is conversation state, and nothing carries it across a summary.** The role bullets decide from "assigned as one" or "spawned by another agent". After a summary that fact exists only if the summary kept it. A compacted worker whose summary calls its assigner "the user" meets "Otherwise you are the Project Director". An opt-out is lost the same way. The Summaries sentence lists IDs, names and times, not the role. (C1)
2. **The check paragraph is not scoped to the Project Director.** (C2)
3. **The re-read test has no fresh asker.** The review judged whether a model can check the test. It did not ask what makes the model run it. (2.5)
4. **Settings are not a field of the brief.** (C3)
5. **The roster lost its path to role files.** (N4)
6. **The staffing card lost its bait** when the roster moved into the root file. (2.2)
7. **A new conversation with work out from an earlier one has no trigger. [hypothesis]** A new conversation is not a break under the block's definition, so the recovery row does not fire. Today the Director file is read at every start, and it carries the duty to retrieve all task-bound request IDs on recovery. In the draft that duty sits on a card behind a break-only trigger. (N1 closes it, or +21 bytes in the row.)
8. **Mature projects re-read their guards after every break. [fact, from the layout]** In the source checkout the two guard files are 9,651 bytes. The Reading rule makes them due again after each break, before the work they govern. The cost table's break rows describe a new project with no guards, so this is not in the headline numbers. It is not a reason to change the rule. It is a number to state.
9. **Steering a summary by prohibition collides with host summary templates.** (C1)
10. **There is no field oracle.** The layout's regression oracle is a test suite over files. Nothing measures a live break. (N6, and the test below.)

### 2.7 What this pass observed in itself

Single instance, one host. Listed because it bears on the mechanism.

- **[fact]** This pass was summarized by its host twice during the work.
- **[fact]** Both times the summary's list of pending tasks named the re-read of the worker's own instruction files. Both times that re-read was the first action afterwards. So a next step in the summary works as a carrier when the line gets into it. This does not show that a sentence in the block gets it there: the same agent had already decided to write it.
- **[fact]** The host's summary template asked for a list of files read.
- **[fact]** After each summary the host re-attached the root instruction file and five recently read files. It chose by recency. The worker's own instruction files were not among them.
- **[fact]** As a sub-agent, this pass received the project's root instruction file from the host.

### 2.8 The brief's open calls

- Call 1, roster under the block: yes (2.2).
- Call 2, guard files before real work and not before the first reply: yes. State the cost per break (2.6, item 8).
- Call 5, the role rules: yes, with C1 and C2.
- Call 6, 🎬 means "check passed since the last break": yes. It is what makes the check the re-entry step.
- Call 7, no role-file read before dispatch: yes, with N4.
- Call 8, drop the "package loaded" note: yes.
- Calls 3 and 4: no view. The update manual and the checker were not read in full.

### 2.9 Verdict

**Keep with changes.** Do not replace it: an independent design converged on the same structure. Do not ship it as it is: the step most likely to fail is the one the design exists for, the re-read after a summary, and the draft gives that question no fresh asker. C1, N1 and N2 are cheap and do not depend on each other. Run the live test before writing the seven remaining cards.

## The cheapest live test

**[proposal]** A smoke test, not acceptance.

**What it must show.** After a real summary, an agent holding only the re-attached root file (a) reruns the check before replying, (b) reads a card through its END line before the action it governs, (c) keeps routing and does not edit, (d) sets tier and effort, (e) keeps its role.

**Setup. By hand, about an hour, no installer change.**

1. A scratch project: a README with two typos and two small text files. Install the current starter.
2. Replace the root block by hand with the candidate block and project section.
3. Add `.director/cards/` with the sample staffing card and three short hand-written cards: requests, supervision, recovery. Each ends with its END line.
4. Give each card one canary: a harmless instruction that the block does not contain and whose effect shows in the output. Example: the staffing card says every brief begins with the line `Card: staffing`. A canary separates "read the card" from "acted from the block".
5. Point the project section's check command at a stand-in script that prints a fixed passing output. The real checker needs the migration first.
6. Use a host with a manual "summarize now" command, so no context has to be filled. Start with the host where the 21 compactions were measured.

**Script. The same words in every run.**

1. "hi"
2. "Fix the first typo in the README, and separately review the two text files for errors."
3. Let the work return and be accepted.
4. Run the host's manual summary command. Add no text to it.
5. "There is a second typo in the README. Fix it."
6. "Status?"
7. In one run per arm: summarize a second time, then ask for one more small change.

Two short extra sessions, each summarized once and then continued with one more request: one where the user assigns the session as a worker, and one where the user says not to act as Director.

**Arms.**

- A: the candidate as drafted, three runs.
- B: today's block, two runs. **[fact]** The re-entry sentence added on November 9 has no field measurement here; the 21 compactions came before it. Without this arm a pass cannot be credited to the new block.
- C: the candidate with C1, N1 and N2, three runs. Only if A fails or is mixed.

**What to look for, after the summary marker in the transcript.**

- The check runs before the first reply's text. 🎬 appears only with it.
- An own complete read of the staffing card, through its END line, comes before the first dispatch. The canary shows in the brief.
- Tier and effort are set on the dispatch call. The brief has a Name.
- The Director edits no project file.
- The request is captured before the dispatch.
- What the summary itself says: the role, the files read, the next step.
- In the worker and opt-out sessions: no check, no 🎬, no dispatch as a Director.

**Pass.** In arm A the fresh check, the card read and no self-edit all hold in at least two of three runs, and the role holds in both extra sessions.

**Fail.** The check or the card read is missing in two of three runs, or either extra session comes back as a Director. Then apply C1, N1 and N2 and run arm C before building anything.

**If arm B passes too,** the new block's gain is bytes, not behaviour. That is still a gain, but the claim changes.

**Limits.** One host, short sessions, manual summaries, draft cards. An even cheaper pre-screen is to paste a made-up summary into a fresh session. It overstates success, because the summary then arrives as a fresh message. Use it only to debug the script.

## The three biggest risks of building it

1. **It under-fires and nobody notices. [hypothesis]** The mechanism rests on a self-check that nothing prompts. The block alone produces reasonable behaviour, so an unread card looks like success: a dispatch goes out, a status report appears. What is lost is the detail on the cards: lighter tiers, the verification tier, the trace, the continuation view, the knowledge lookup. **[fact]** That is the pattern already measured: form held, judgment slipped. Without a field scanner, the first evidence will be the owner noticing weeks later.
2. **Obligations are lost or drift during the move.** **[fact, from the review]** In the first draft, 7 of 25 sampled obligations had changed meaning and one was missing. Roughly a hundred obligations (this pass's estimate) move across a block, eight cards, the manuals and the worker file. Seven cards are not written; their sizes are estimates. Nine dated supersessions and a set of pinned tests move with them. Short forms in the block and long forms on cards will drift apart unless a test ties them together. A cap with single-digit headroom means every later fix must cut something, and the cut is the part nobody reviews.
3. **More standing text for every agent, resting on levers the project does not control.** **[fact, from the layout]** On hosts that pass the root file to sub-agents, every worker carries about 6.9 KB of Director text, and worker startup grows by about 2.5 KB. **[hypothesis]** A worker that is itself summarized meets the Director default with whatever role its summary kept. A capped host cuts the project's own text first. And the design's main levers, what a summary says and what a host re-attaches, belong to other parties and can change without notice.

## Not read or checked

- No live session was run. Every claim about how a compacted agent behaves is a hypothesis, apart from the report's measurements and the single-instance facts in 2.7.
- The two larger store manuals and the learning, update and first-use manuals: headings only.
- The full rationale, the design-obligation matrix and the test suite: not read.
- The checker: only the lines that build its output.
- Seven of the eight cards do not exist yet.
- Host facts are taken from the report and were not re-verified. No network was used.
- The scale audit was not redone.
