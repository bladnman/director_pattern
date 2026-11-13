# Why a Director never proposes a role, and lets specialist calls drift to itself

Investigation · November 13, 2026

**Status**

| Item | State |
|---|---|
| Diagnosis | Accepted |
| Change | Implemented in the starter source as revision 3.4 |
| Independent review | Accepted. The first pass returned "accept with changes"; all 13 findings were applied, and the focused re-review accepted. |
| Static tests | Pass: 269, as reported by the implementation |
| Maintainer acceptance, publication, installation | Pending (nothing published) |
| Live trials | None |

The wording and byte counts below are taken from the implemented source. Where this
report and the November 13 entries in `development/RATIONALE.md` (R1, R2, R10, R11,
R17, R18) or the tests differ, the rationale and the tests win.

**Labels.** **Fact:** seen in a file or record. **Hypothesis:** an inferred cause.
**Implemented:** present in the starter source and checked by static tests.
**Pending:** not yet done.

## The short answer

An adopting video project shipped a video, then held a retro. It raised three problems
with how the Director worked, plus a few smaller ones:

1. **A role is never proposed.** Work that recurred went to general workers with a
   fresh brief each time. That work was after-actions, analysis of the owner's own hand
   edits, and overnight render and upload chains. No Director said that the work kept
   recurring and should have a role.
2. **A specialist's call drifted to the generalist.** The project had a maintained
   packaging role with an explicit rule for titles and thumbnails. The Director judged
   the owner's own title and thumbnail itself anyway. It wrote title rounds in chat and
   set a limit the role does not have. The owner corrected it twice.
3. **Every recorded step is treated as fixed.** The Director never proposed cutting or
   merging a step.

**All three are one kind of mistake.** The Director treats the project's maintained
structure as a fixed lookup table. That structure is its roster and its recorded
procedures. The Director neither routes through it nor maintains it.

Before 3.4, the pattern questioned structure only after a failure:
- A correction became an incident, incidents fed a bounded review, and the review
  might propose a `structure` change.
- A repeated failure called for reassessment.

Work that recurred without being corrected never became an incident. Neither did a
step that cost more than it returned. So nothing ever asked about them. In the other
direction, the Director's direct-answer exception had no carve-out for a judgment
that a roster role owns. That exception is "discussion, simple lookups and
acceptance judgments yourself".

**Implemented as 3.4**

- **The block (7,997 of 8,000 bytes):**
  - Duty 2 gains a role-domain clause.
  - The knowledge-card row of the read table now names a retro.
  - Six phrases are tightened, with their meaning kept, so that no rule is dropped.
  - The Roster rule stays, narrowed to a limit.
- **The cards:**
  - Knowledge gains a "Look back on the work" paragraph.
  - Staffing and requests carry the role-domain clause.
  - Requests lets a step be raised as a cut once.
  - Supervision covers quiet stretches.
- **Installation:**
  - The update guide gains an "Update an installed block" step.
  - The 3.3 move's custom-marker step is corrected.
  - New installs get a one-line project-section hint.
- **Not added:** a role value, a store kind, a threshold, a census, or automatic
  creation of anything.

## What happened (distilled)

- **Fact.** The run used the starter 3.2 Director file. The project moved to the 3.3
  AGENTS.md block after the ship. The rules at issue read the same in both revisions:
  - closure upkeep is "not a role census";
  - departments are not created from a correction count;
  - ordinary discussion, simple lookups and acceptance judgments are answered directly.

  So the gap carried forward.
- **Fact.** The installed 3.3 block and cards matched the source byte for byte. The
  only difference was the project's own marker lines around the block.
- **Fact.** Recurring jobs were briefed each time to the roster's general analysis
  row. The project has since drafted its own retro role. That role asks every time
  which work recurred without a role, and which steps could be dropped or merged.
  This is the project's change.
- **Fact.** The project's own packaging guidance did not send the packaging check to
  the packaging role, and that contributed. The project is changing that guidance on
  its own authority. The pattern-level part is what the Director did:
  - It wrote eighteen titles in chat. That is detailed work on a deliverable, done
    directly.
  - It added a length cap that contradicts the role's own rule. By design, the
    Director does not read that rule.
- **Fact.** SitReps lapsed during a quiet stretch with no worker return and no user
  message. The project's Director fixed this itself with a five-minute timer.
- **Fact.** A process question was answered once in chat. The answer could not be
  found again.
- **Fact.** The project's dated guidance maps tiers to specific models. The strongest
  model ran out of capacity twice mid-run.

## Diagnosis

### Problem 1: recurring work never becomes a role

The mechanism existed, but nothing triggered it.

| Where | What it says | Why it did not fire |
|---|---|---|
| `development/RATIONALE.md`, R18 | "Departments follow recurring responsibility and coordination needs observed in real work." | The intent was recorded, but no runtime text acted on it. |
| R1, consequence and revisit | Revisit when recurring ownership friction shows a missing responsibility. | This is a revisit trigger for the maintainer, not a step for the Director. |
| `pattern/starter/payload/LEARNING.md` | A bounded review may return `structure` or `routing` proposals. | A review reads only incidents, which are recorded corrections. Work nobody corrected produces none. |
| `cards/knowledge.md`, closure | Refresh the touched roles and roster rows. This is "not a role census or automatic department creation". | A role that does not exist is never touched. |
| `cards/staffing.md` | "Register a new, renamed or retired role in the project roster before using it." | It applies only after someone decides to create a role. |
| `cards/staffing.md` | "A general worker never silently replaces a maintained role." | With no maintained role, a general worker is always correct. |
| `development/BEHAVIOR_PARITY.md` | The closure trigger is unproven. | Already known. No trial had reached a closure. |

**Finding.** The trigger was missing. The only route to a structure proposal was
driven by corrections. Closure looked only at what had been touched.

### Problem 2: a specialist's call drifts to the generalist

No rule covered the Director, and an existing rule did not fire.

| Where | What it said | Why it did not fire |
|---|---|---|
| Block, duty 2 | "Answer discussion, simple lookups and acceptance judgments yourself." | A passing remark about a title counts as discussion. There was no carve-out for a domain a role owns. |
| Block, duty 1 | Map each **request** onto the established mechanism and owner. | A remark is not a request, so the mapping never ran. |
| `cards/staffing.md`; R10, October 21 | No generic actor substitutes for a matching maintained role. | It governs whom the Director staffs, not what it answers itself. |
| `cards/staffing.md`, `cards/supervision.md` | Specialists keep their own authority. | This applies only once a specialist has been selected. |
| R10, October 30 | The Director reads a role's selection and authority part, not its craft. | By design, the Director lacks the craft rule, so routing the call is the only safe move. |
| R2, later November 1 | A review was done directly. The likely cause was misclassification as discussion. | **The same mistake had happened before.** That fix named reviews; this time a domain judgment slipped through. |

**Finding.** The hole is narrow and sits in the block. A card-only fix would not fire,
because answering a remark does not feel like staffing.

### Problem 3: recorded steps are treated as fixed

| Where | What it said | Gap |
|---|---|---|
| Block, duty 1; `cards/requests.md` | Map onto the established mechanism. A better route found mid-flight is raised as a ❓. | Nothing said a step of that route could itself be questioned. |
| `cards/supervision.md` | Reassess after a mismatch or repeated failure. | It fires only on failure. |
| `cards/knowledge.md`, closure | Move stale runtime claims to evidence. | It covers claims, not steps. |

**Finding.** Missing. It has the same root as problem 1.

### The smaller findings

- **SitReps in a quiet stretch.** The rule existed but was incomplete. The per-turn due
  check needs a turn, and a quiet stretch brings none. The supervision card already
  said that waits must leave both cadences usable. 3.4 says how.
- **Findings lost in chat.** This is mostly the project's choice. The pattern-level
  part is one clause: the look-back keeps its answers where the project keeps findings
  the user reads back.
- **A named model ran out of capacity.** This is also the project's choice. The
  starter names no model, and recording the effective settings is already required.
  There is no pattern change.

**Hypothesis.** The diagnosis is the Director's own. That the missing trigger caused
the behavior is inferred from the records, not observed. The same goes for the
Director treating the title remark as discussion.

## What 3.4 implements

### The block (`pattern/starter/agents/block.md`): 7,993 → 7,997 bytes, cap 8,000

**Duty 2** now reads:
> You route; workers execute. Answer discussion, simple lookups and acceptance judgments yourself; a judgment, draft or rule in a roster role's domain goes to that role, even in chat. Delegate project investigations, reviews and changes to bounded subagents before doing the detailed work. Scope assignments, stay available to the user and evaluate returns.

**The knowledge-card row of the read table:** "look up knowledge, record a correction,
close an outcome, or hold or brief a retro".

**Six phrases are tightened to fit the cap.** No rule is dropped and the meaning is
kept:

| Where | Before | After |
|---|---|---|
| The gate | "project/host authority, the user's authority" | "project, host and user authority" |
| Duty 2 | "Directors, delegate" | the "Directors," vocative is dropped |
| Duty 2 | "evaluate the returned results" | "evaluate returns" |
| The read rule | "Cards in cards/," | "Cards," |
| The knowledge row | "look up knowledge for a task" | "look up knowledge" |
| The update row | "update, here or elsewhere" | "update anywhere" |

The cap is unchanged.

**The Roster rule is kept, and narrowed.**
- Before: "Before dispatch read the selection and authority part of any role file the
  row or section names; the rest is for its executor."
- Now: "Before dispatch read only the selection and authority part of the role file
  its row names."

Two things change:
- A permission becomes a limit. This follows the accepted rule that the Director
  routes from roster summaries and does not read the executor's craft.
- The sentence now names the file in the role's row. A file named only through the
  project section's locator is still covered by that section's own role-file line.

The October 30 behavior is kept: the staffer reads the selection and authority part
before dispatch.

### Cards

- **`cards/staffing.md`, 6,303 → 6,491 bytes (cap 6,500).** The first rung gains:
  > A judgment, draft or rule in a roster role's domain goes to that role, even in chat. Accepting a return against the whole request stays yours.

  The brief's "Applicable knowledge" field now says that a retro or look-back brief
  carries the knowledge card's two questions. A few phrases are tightened to stay
  within the cap, with their meaning kept.
- **`cards/requests.md`, 5,121 → 5,475 bytes.** It opens with:
  > Answer discussion directly, except a call in a roster role's domain, which goes to that role, even in chat.

  The card already says the Director owns the conversation, the intended result and
  acceptance. After the partner rule it adds:
  > An established mechanism is the default route, not a fixed law: when one of its steps is not earning its cost on this request, say so and recommend the cut or merge as a ❓ once; until the user chooses, keep the step. A repeat goes to the look-back (`cards/knowledge.md`).
- **`cards/knowledge.md`, 3,103 → 4,280 bytes.** The opening line adds looking back on
  the work as Director work. A new paragraph follows:
  > **Look back on the work.** At meaningful closure, and whenever you or the user look back on how work went (a retro or after-action), ask two questions of the work this conversation held, not of all history: what did we brief more than once, or rebuild from scratch, that no roster role holds; and which recorded steps, records or rules cost more than they returned, or could merge? Bring each supported answer to the user as one ❓ proposal: a role (what its file would hold, its roster row) or a cut or merge (the step's source, its cost, what would break). Keep a step whose source is a user rule, an authority gate or required independent review unless the user changes it. A proposal changes nothing until the user decides; an accepted one becomes a request for the owning maintainer, and a new role is registered before use (`cards/staffing.md`). One repeat is a candidate, not a department: say how thin the evidence is, and propose nothing when nothing recurred and every step earned its cost. A delegated look-back carries both questions in its brief. Keep the answers where the project keeps findings the user reads back, not only in chat.
- **`cards/supervision.md`, 5,147 → 5,457 bytes.** It adds:
  > When no worker return or user message may arrive before the next SitRep is due, arm a supported background timer or wait that leaves you available to the user and brings you back by then; a quiet stretch does not pause the cadence. If the host has none, say so once and send each due SitRep at your next turn.

### The project section template: 1,120 → 1,189 bytes, cap 3,000

For new installs, `pattern/starter/agents/project-section.md` adds: "If the roster
moves to a file, keep one line per role's domain here." This keeps a role's domain
visible when the roster grows. Existing sections are project-owned and do not get
this sentence from an update.

### How installed projects receive it

**Revision.** The manifest's `starter_revision` moves from 3.3 to 3.4. 3.4 is the
first change to the block since the move to the AGENTS.md block. A 3.3 project's check
reports that the block differs from its recorded baseline until the project takes
its own reviewed update.

**New step in the payload `UPDATES.md`, "Update an installed block":**
1. Back up and verify the hook source, every managed file to be changed and the
   current receipt.
2. In the file the check selects, replace everything from the opening marker line
   through the closing marker line with the incoming block, byte for byte.
   - Leave all other text untouched, including the project section. Only the
     `--receipt` paths in its check and update-check commands change.
   - If the installed block was edited, first move that wording into the project
     section, then measure as in the move.
3. Once the file checks pass, write the update receipt. It holds the new baselines of
   each changed card and payload file, and the new block hash: the block as it now
   stands, marker lines included. Point the check commands at it.
4. Run the check exactly as the project section states it. It must report
   `evidence_matched` and `director_block: unchanged`.

**Corrected during review: custom markers.** Some projects use their own marker pair
around the block. Such a project puts its two marker lines *in place of* the incoming
block's first and last lines. The 3.3 move's step said to keep them *around* the
incoming text, which would have left two marker pairs, and the check accepts exactly
one. That step is corrected the same way.

**Superseded in part: receipt order.** On November 11, a receipt could precede
required checks "for this move only". The check reads the receipt, so every block
update now has the same order. The receipt records the selected fresh host trials as
pending, and the update is not reported as adopted until they pass.

**New scripted test.** A 3.3 installation, with and without custom markers, is
updated to 3.4. The project section and a project role file are unchanged apart from
the receipt paths. Exactly one marker pair remains. The check, run as the section
states it, reports `evidence_matched` and `director_block: unchanged`.

### What did not change, and why

- **`LEARNING.md` and the store schema.** There is no new learning kind, no
  recurrence field, and no survey of work patterns by the reviewer. A census would
  contradict the bounded learning loop and its startup cost.
- **No count threshold and no automatic role creation.** A count already "never
  creates a department", and one repeat can be worth naming.
- **No upstream retro role.** A retro role, its reading list, its board and any model
  ledger belong to a project.
- **No craft reads for the Director.** The new clause routes the call. It gives the
  Director no new knowledge.
- **The project's own guidance stays the project's.** That covers its packaging text,
  its model mapping and its board habits.
- **This repository's own installation still holds the 3.3 block.** It changes only
  through its own reviewed update.

## How the change keeps the earlier design intent

| Earlier decision, and the failure it prevents | Disposition |
|---|---|
| R18: a correction count never creates a department, and a task count alone does not create a layer. Prevents ceremony and premature organization. | **Preserved.** A repeat is a candidate. The user decides through a ❓. An accepted proposal becomes a request for the maintainer. Nothing is created automatically, and nothing is proposed when nothing recurred. |
| R17, October 30: closure upkeep is "not a role census". Prevents unbounded review cost. | **Preserved, with a dated refinement under R18.** Two questions, limited to the work this conversation held. |
| R18's learning correction: do not read all history. | **Preserved.** The questions use context already loaded at closure. Learning and the store are unchanged. |
| R10, October 30: selection is separate from execution knowledge. | **Preserved, relied on, and made a limit.** The Director reads *only* the selection and authority part. |
| R10, October 21: no generic substitute for a matching maintained role. | **Extended to the Director.** Accepting a return against the whole request stays the Director's. |
| R2, later November 1: discussion and acceptance stay direct. | **Narrowed by domain.** This is the second instance of the same misclassification. |
| R1, November 7: the partner rule. | **Refined.** A step can be the better route. It is raised once as a ❓ and kept until the user chooses. A repeat goes to the look-back. |
| R17, November 7: SitRep cadence, with no daemon. | **Completed.** The Director uses the host's own background timer or wait. No tool is named and the interval is unchanged. |
| R11, November 11: the receipt precedes checks for this move only. | **Superseded in part.** This now applies to every block update, with trials pending until they pass. |
| R10, November 11: the block stays within 8,000 bytes. | **Preserved by tightening.** No rule is dropped. |

The design-obligation matrix updates the affected standing-block rows. It adds a
section, "Field report triage — November 13, 2026", in the November 7 format.

## Regression oracle

**Static tests** (all pass, 269 in total, as reported):

| Test | What it covers |
|---|---|
| `test_a_call_in_a_roster_roles_domain_goes_to_that_role_even_in_chat` | The role-domain clause in the block and on the cards; acceptance stays the Director's |
| `test_knowledge_card_looks_back_with_two_bounded_questions` | The look-back paragraph's limits, its trigger, and the retro brief |
| `test_a_step_not_earning_its_cost_is_asked_once_and_kept_until_the_user_chooses` | The step-cut sentence on the requests card |
| `test_a_quiet_stretch_does_not_pause_the_sitrep_cadence` | The quiet-stretch sentence on the supervision card |
| `test_update_guide_updates_an_installed_block_without_touching_the_section` | The new update step in the guide |
| `test_a_3_3_installation_updates_its_block_and_keeps_the_section_and_markers` | The scripted 3.3 → 3.4 update, with and without custom markers |

The updated block, card and section pins also pass, as do the 8,000-byte block cap,
the card and section caps, and `test_standing_text_and_cards_name_no_model`.

**Live cases.** None have run. Each needs a fresh session.

1. **Recurrence.** The same analysis is briefed from scratch three times.
   - Pass: a retro brings one ❓ proposing a role, with what its file would hold and
     its roster row. Nothing is registered before the user accepts. A delegated retro
     brief carries both questions.
   - Known bad: the field run, where no role was proposed at all.
2. **Domain.** The owner asks in chat what the Director thinks of a title, and the
   roster has a packaging role.
   - Pass: the Director captures the question and briefs that role. With no matching
     role it answers directly. Its acceptance of a returned whole result stays its own.
   - Known bad: the two corrections.
3. **Cut.** A recorded step cannot change a small request's result.
   - Pass: the step is named with its source and cost, and the cut is raised as one
     ❓. The step still runs until the user chooses.
   - Fail: a Director that skips the step silently, or asks again on every request.
4. **Quiet stretch.** Two long-running workers and a silent user.
   - Pass: a labeled SitRep arrives about every five minutes. On a host with no timer
     or wait, one statement says so.
   - Known bad: SitReps lapsing in silence.
5. **No ceremony.** Nothing recurred and every step earned its cost.
   - Pass: no proposal.
   - Fail: a Director that adds a role, cuts a step or edits a role file on its own.

## Remaining risk and uncertainties

- **Accepted risk.** The look-back lives on a card, and a card is read only if the
  Director opens it at its trigger. That trigger was already unproven for this card,
  and one earlier session skipped the card after a compaction. Two things narrow the
  gap without closing it: naming a retro in the table row, and putting the two
  questions in every retro brief. Moving the paragraph into the block was not
  possible within the cap without dropping a rule. A live retro is the test.
- **Thin evidence.** It comes from one project and one run, on 3.2 text that reads
  the same as 3.3 here. It is not an observation of 3.3 or 3.4.
- **Roster rows.** "A roster role's domain" is judged from roster rows, and a row can
  be vague or stale. A remark that needed no specialist may still be routed, at the
  cost of an ordinary capture and brief.
- **Pending:**
  - the maintainer's acceptance;
  - commit and publication;
  - every installed project's own reviewed update;
  - fresh-session trials.
