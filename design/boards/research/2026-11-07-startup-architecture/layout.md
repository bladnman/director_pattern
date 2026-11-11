# Layout: the Director slug and action cards

**Proposal, 2026-11-09, revised the same day after an independent review and its re-checks ([slug-review.md](slug-review.md)) and a second, independent pass ([second-pass.md](second-pass.md)).** Not decided, not implemented. Companion to [slug-draft.md](slug-draft.md) and [card-sample-staffing.md](card-sample-staffing.md). Figures marked "measured" come from `wc -c` on this checkout; card sizes other than staffing are estimates from the source text they absorb.

## (i) Before and after

Before: starter revision 3.2 payload, as installed in a new project.

```text
AGENTS.md                bridge block                     1,190  standing (re-sent by the host)
.director/
  START.md               read rules, role routing, check   4,767  read before first reply
  DIRECTOR.md            Director foundation              14,415  read before first reply
  OPERATIONS.md          check section 7,862 (before first reply), context preflight 1,524,
                         staffing 5,093, privacy 1,217    15,696
  WORKER.md              worker foundation                 2,711
  API.md 8,438 · TOOLING.md 16,090 · RECORDS.md 11,815     request-store manuals (36,343)
  LEARNING.md 7,554 · UPDATES.md 28,109 · FIRST_USE.md 6,005
  *.py helpers, config.json, install.json
```

After (proposal):

```text
AGENTS.md
  <!-- director-starter:2 -->  Director slug, managed      6,303  standing; first in the file
  <!-- director-project -->    project settings + roster     905  standing; project-owned, cap 3,000
  (the project's own text)
.director/
  cards/                       each ends "END cards/<name>.md"
    staffing.md                                    5,998 (reviewed rewrite)
    requests.md                                    3,122
    supervision.md                                 5,021
    recovery.md                                    1,265
    knowledge.md                                   3,433
    update-check.md                                  671
    privacy.md                                     1,410
    badge.md                                       6,440 (over the 6,000 card cap)
                   all measured; written in round 8 from today's text, word for word
                   (link targets aside), except staffing; total 27,360
  WORKER.md        worker foundation + full read rules  ~4,300  ends "END WORKER.md"
  OPERATIONS.md    check internals + preflight     ~6,500  ends "END OPERATIONS.md"
  API.md TOOLING.md RECORDS.md LEARNING.md UPDATES.md FIRST_USE.md
                   text unchanged; each gains an END line
  START.md, DIRECTOR.md   ~400 each: redirect stubs so older assignments still resolve
  ROSTER.md        only if a roster outgrows the project section
  *.py helpers     checker output gains a "next" key; one actor_must_confirm item changes (part v)
```

Every file the slug names exists above: `WORKER.md`, the eight cards, `API.md`, `TOOLING.md`, `RECORDS.md`, `LEARNING.md`, `UPDATES.md`, `OPERATIONS.md`, `FIRST_USE.md`, the check command's `startup_check.py`, and the optional `ROSTER.md` named by the project section.

## Budgets

| Part | Hard cap | This draft | Why |
|---|---|---|---|
| Slug | 6,300 bytes (6,000, raised to 6,200 in round 7 and to 6,300 in round 8) | 6,303 (measured): **3 bytes over**; a −4-byte meaning-neutral cut is proposed, not applied | Always in context for Directors and, on hosts that pass AGENTS.md to subagents, for every worker too. Raised only to restore the November 9 re-entry sentence word for word: live Director sessions have been reported re-reading startup after a compaction under it (reported to this work, not re-checked here), while the break test has no live evidence. Standing total with the generic project section: 7,208 bytes. Round 8 raised it again for five accepted fixes that restore working mechanisms (re-check 4) |
| Project section | 3,000 bytes | 905 generic; 1,950 for this checkout's nine roles (measured) | Overflow moves the roster to ROSTER.md, named in the section |
| Each card | 6,000 bytes | all measured; badge 6,440 is over, because it carries today's check text from three files word for word | About 1,500 tokens: under one host's 5,000-token cap for files it re-attaches after compaction |
| WORKER.md | 4,500 bytes | ~4,300 | Every worker reads it |
| Whole AGENTS.md | 24 KiB guidance | — | One host caps combined project instruction files at 32 KiB by default; leave room for nested files. Keep the slug first so a cut never reaches it |

The installer's `plan` should report these and refuse an install whose slug or section is over cap.

## Audience of each section

**Correction, 2026-11-09 (from the owner).** The duties were written to "you" under a heading ("On every turn:") that named no audience, so every agent that loads the root file, workers and sub-agents included, was addressed by them. The worker bullet's "these parts apply to you" clause was the only exclusion, which is too weak. Each section now names its audience, and the role bullets say which labels apply to which role:

| Section | Audience | Label in the block |
|---|---|---|
| Your role (the gate) | Every reader | none; it sorts readers into roles. An opted-out Project Director session skips all but Summaries |
| Every turn (duties 1 to 10) | Directors only: the Project Director, and a scoped child Director for its assigned outcome | "(Directors only)" |
| 🎬 and the check | Project Director only | "(Project Director only)" |
| Reading and the table | Every role; a worker uses the rows for its own actions | "(every role)"; the update row adds "as Project Director", the recovery row "as a Director" |
| Summaries | Every role, including an opted-out session, because it carries the opt-out across a break (its quoted next step limits the check to the Project Director) | "(every role)" |
| Roster | Directors only | "(Directors only)" |

The break definition moved from the check section into Reading, because workers apply the re-read test too.

**Limit.** A label controls who should act on a section, not who receives it. Every agent the host gives the root file to still loads the whole block, labels and all, and pays its bytes. Labels are a reading instruction, not a filter.

**Settled on the cards, not in the block:** the supervision and knowledge rows sit under "Reading (every role)" and are legitimately used by some workers. When written, the supervision card opens by saying status reports (📋 SitReps) are Director work, and that a delegating worker evaluates its sub-workers' returns and accounts for them in its own return. The knowledge card opens by saying lookup is for every role, while recording corrections and closing outcomes are Director work. The recovery row is labelled "as a Director" in the block (re-check 3).

**Known, unpaid:** the child bullet does not say the parent keeps acceptance (the project section's `sub-director` row does; +22 bytes, so it goes on the requests or supervision card); and with the "## Director" heading removed, a block that is not first in its file has no visible name (+10 bytes for "**Director: your role**…").

## (ii) Cards

| Card | Purpose | Read before | Budget |
|---|---|---|---|
| `staffing.md` | Routing ladder (do it, worker, scoped child Director); tier and effort including the lighter option; the brief's ten fields in duty 5's order, with the requirement trace; names; verification tiers; other routes; registering roles | Staffing or briefing any work, or setting tier and effort; workers before delegating | 6,000 |
| `requests.md` | Partner rule in full; defines "linked request" and "sub-request"; exact capture and its exemption; splitting; checkpoints; steering by revision; the four store commands (the routine command lines only with a verified N3); ❓ in question tools; the Director owns narrow state writes | Capturing, splitting or steering a request, or any store command | 4,500 |
| `supervision.md` | SitRep coverage, shape, example, no-clock fallback; waits instead of polling; evaluating returns against the whole result; continuing to completion; true exits; ❓ and 🖐️ detail | Supervising delegated work, evaluating a return, ending a turn with work out | 6,000 |
| `recovery.md` | After a break: find held work (summary, continuation notes, owner's records), run the continuation view, reconcile, correct false "done" records, one prompt SitRep, resume existing owners; asks for a visible re-entry line in the first reply (N5); a full-replay resume as a known limit | First project action after any break | 2,500 |
| `knowledge.md` | Task-time knowledge selectors and tags for workers; recording corrections; the three-incident review or recorded deferral; explicit user rules; closure upkeep of roles, pointers and facts; keeping caller and role IDs and aliases working through refactors (moved from the staffing card) | Looking up knowledge for a task, recording a correction, closing an outcome | 4,500 |
| `update-check.md` | Daily discovery (once per rolling 24 hours of activity), the exact notify sentence, notify / automatic / off phrases, who may update a project | Project work with no check in 24 hours; any talk of updating | 3,000 |
| `privacy.md` | Git and remote visibility, the once-only public-history warning, ignore rules | First exact source capture; changing what Git tracks | 2,000 |
| `badge.md` | What 🎬 claims; pass and fail handling; conflicts in surrounding instructions; when a failed check is retried; recheck after changed startup bytes | A failed check; installing, integrating or changing how instructions load | 4,500 |

## (iii) Where each obligation group lands

S = START.md, D = DIRECTOR.md, O = OPERATIONS.md (starter 3.2), B = today's bridge. "Slug" means the short form is in the slug and any detail is in the named card. ⚠ marks a change in meaning that needs a dated supersession (listed in part v) or an owner decision.

| Group | From | Lands in |
|---|---|---|
| Role default; workers and scoped child Directors; workers and child skip the check | B, S 15–24, 38–39 | Slug role gate (worker bullet: Directors-only sections are not for it, "no check, no 🎬"; child bullet: Directors-only sections for its outcome, "never the check or 🎬") ⚠ worker status from a spawn-and-report-back task |
| Preserve host/user/project authority, other authors' work, private sources and existing trackers; role names grant nothing | B, S 40–44 | Slug role gate; WORKER |
| Explicit assignment selects package; missing details go back to the assigner; load only that package, no global catalog | S 15–18 | WORKER (a plain brief is enough to start); the slug's Reading rule makes a worker re-read WORKER.md and its role file, and a child Director its overlay, after each break |
| Complete reads, bounded output, ranges to the end, total extent, truncation recovery, "a hash is not a read" | S 3–13, B | Slug (bounded numbered ranges, every range, shown total length, stop if unrecoverable, non-reads listed); WORKER (full text) |
| Task instructions before their action; re-read after compaction or resume (3.2), for Directors, workers and child Directors; helper guides are action references, installer docs are not startup | B, S 63–67, D 26–27 | Slug Reading: the November 9 sentence kept word for word, at the top of "Reading (every role)". "This startup" is listed right after it: the Project Director's check; a worker's WORKER.md and role file; a child Director's overlay; the file the next action needs. "Repeated" means each step is fresh (your own run or complete read after the latest break). Cards, table manuals and project-listed files need a fresh complete read before their action |
| First-reply check, even a greeting; the default command; 🎬 on every reply; failure gives the gap and an answer; recheck when stale; what the check does not prove | B, S 25–37, D 17–37, O 5–13, 34–38 | Slug (own check run after the latest break, before each reply; the project section's command); badge card |
| Host-required progress note before the check | S 31–32, O 15–21 | Slug 🎬 paragraph |
| Generated-project first use, before the check | S 28–30, O 23–33 | A generated template's project section lists FIRST_USE.md and its required reads before the first check; FIRST_USE.md unchanged; order kept |
| What the check reads, no network or writes, hold output in context | S 58–62, O 40–49 | badge card |
| Receipt formats, hook structure, `--hook-source`, `--backend-contract`, mature command example | O 51–99 | OPERATIONS (unchanged manual, named in slug) |
| What 🎬 claims; guards, backend binding, loaded route and conflicts confirmed | O 101–118 | Slug (the check's `actor_must_confirm` items); badge card ⚠ no longer claims startup reads |
| Context-budget preflight | O 120–144 | OPERATIONS (named in slug); also used by the update merge (part v) |
| Acknowledge the resolved package once | S 24–25 | ⚠ dropped for Directors (no package; 🎬 serves); WORKER keeps it for workers |
| Partner rule | D 3–12 | Slug duty 1; requests card (pause mid-flight, independent work continues, forbidden routes) |
| Read all of UPDATES before planning any update; other projects update themselves | D 13–16 | Slug table row; update-check card (open owner decision, unchanged rule) |
| ❓, 🖐️, grouped questions, question tools, host formats | D 38–44 | Slug duty 9 (question tool included; "Higher-priority host formats win" restored by re-check 3 after a round-5 cut); requests and supervision cards |
| Delegate before detailed work; answer discussion directly; gap and stop when no subagents | D 45–53, B | Slug duty 2 (pinned sentences); staffing card |
| Routing ladder: do it, worker, scoped child Director | accepted owner rule, Nov 8 | staffing card; project section's `sub-director` row ⚠ not yet in the payload |
| Brief contents and requirement trace | D 54–58, API trace section | Slug duty 5 (ten fields: emoji Name; role; tier, effort and reason; scope; file ownership; authority; expected result and checks; request IDs; applicable knowledge; return route); staffing card in the same order (trace rule on the card, recorded through the requests row) |
| Tier and effort: explicit every dispatch, strong default, lighter option, record reasons | D 58–68, O 159–188 | Slug duty 3 (the host's controls explicitly on every dispatch, strong default; "inheriting is not a choice" now only on the staffing card) and duty 5 (tier, effort and a one-line reason as brief fields); staffing card (lighter option, recording) |
| Local decisions, rework authority, return contents, no self-review | D 69–75, O 190–195 | staffing card; supervision card (evaluation side), prompted by the fixed last line on every worker return (N2, WORKER.md) |
| Same contract across sessions and external routes; source subset only; child Director text where AGENTS.md is not passed | D 77–84 | staffing card |
| Stay available; no mandatory manager; another Director only for real coordination | D 86–92 | Slug duty 2 (pinned "stay available"); staffing card |
| Role discovery; prefer maintained roles; executor loads its own manuals | O 148–157 | staffing card + project section roster and its "Role files" locator line (N4) ⚠ Directors route from roster rows instead of reading the selected definition |
| Verification tiers | O 197–202 | staffing card |
| Emoji Names | O 204–207, S 39–40 | Slug duty 5; staffing card |
| Capture exact inputs, split obligations, lifecycle, steering, state ops by the Director; simple replies need no capture | D 94–107, S 58 | Slug duty 4 (with the exemption); requests card |
| Checkpoints | D 109–112 | requests card |
| Whole-result evidence, reassess after repeated failure, smallest proof | D 114–125 | Slug duty 7; supervision card |
| Keep the outcome open; recover all task IDs including terminal ones | D 126–133 | Slug duty 8; recovery card, prompted by the check's "next" key (N1) ⚠ a new conversation with work still out from an earlier one is not a break, so the recovery row does not fire; closed only once N1 is built |
| SitRep cadence, coverage of every stream, shape, example, after-break rule, no-clock fallback | D 134–167 | Slug duty 6; supervision card; recovery card |
| Continue to completion; real exits; submitted vs accepted | D 169–179 | Slug duties 8, 10; supervision card |
| Waits, not polling | D 181–183 | supervision card |
| Incidents, pending learning, three-incident review, explicit user rules | D 185–198 | knowledge card; LEARNING (named) |
| Closure upkeep of roles, pointers, facts; caller IDs and aliases | D 200–204, O 209–215, S 19–21 | knowledge card (now including caller IDs and aliases); staffing card (registering a role before use) ⚠ open: the alias rule now sits behind the closure and knowledge-lookup trigger, so a Director renaming a role at staffing time does not meet it (re-check 2, item 6); settle when the knowledge card is written |
| Daily update discovery | D 204–206 | update-check card; UPDATES (named) ⚠ the card repeats part of UPDATES' first section: drift risk, needs a parity test |
| Task-time knowledge selectors | S 48–58 | knowledge card |
| Continuity and privacy | O 217–233 | privacy card |
| Composition cannot merge people or waive independent testing; staff for work, not ceremony | S 44–46 | staffing card |
| Request-store manuals before state I/O | README, API intro | Slug table row: manuals "before the command" (unchanged rule). C4 ("for a command it lacks") is withdrawn until N3 is feasibility-checked and returns only in the same change ⚠ 36,343 bytes, the next bulk target |
| Project startup guards and exact check command (mature projects) | project PROJECT files | Project section; read under the slug's rule before the work they govern (open: before the first reply or before task work) |
| Roster | project ROLE_INDEX | Project section ⚠ needs a dated supersession of "no global startup catalog" |
| Summary contents across a break (new) | second pass C1; review finding 3; re-check 2 | Slug Summaries: role, any opt-out and whom you report to, exact IDs, names, handles, pending ❓ and 🖐️, last SitRep time, and next steps beginning with the fixed re-entry sentence ⚠ K1 removed "Never copy END lines…", reversing part of a reviewed fix |
| Re-entry made visible and countable (new) | second pass N5, N6 | recovery card asks for a re-entry line; maintainer transcript scanner outside the payload |

Nothing in START, DIRECTOR or OPERATIONS is dropped without a flagged decision; every ⚠ row is listed in part v.

## (iv) Read cost, before and after

Tool-read bytes (files read plus check output); standing AGENTS.md text is noted separately. Check output is this checkout's measured 1,717 bytes; a new project's was not measured. Card figures are measured on the round-8 card files.

| Case | Before (3.2) | After (proposal) |
|---|---|---|
| New project, first reply | START 4,767 + DIRECTOR 14,415 + OPERATIONS section 7,862 + check ≈ **29.9 KB** with the 1,190-byte bridge standing (37.8 KB if OPERATIONS is read whole) | Check only, ≈ **1.7 KB**, with 7,208 bytes standing: **≈ 8.9 KB** in all |
| A break, no work held | Re-read 27,044 + check ≈ **28.8 KB** | Check ≈ 1.7 KB, plus the recovery card (1,265) at the first project action: **≈ 3.0 KB** |
| A break, work held | 27,044 + check + store manuals 36,343 for the continuation view ≈ **65 KB** | Check + recovery 1,265 + requests 3,122 + store manuals 36,343 + supervision 5,021 ≈ **47.5 KB** (about 27% less) |
| First delegated change, new project | 27,044 + check + store manuals + LEARNING 7,554 + OPERATIONS staffing 5,093 ≈ **77.8 KB** | Check + requests + store manuals + knowledge 3,433 + LEARNING + staffing 5,998 + supervision ≈ **63.2 KB** (about 19% less) |
| This checkout, first reply (greeting) | **42.9 KB measured** (AGENTS 5,490, START 5,123, DIRECTOR 13,162, PROJECT 8,646, CAPABILITY_POLICY 1,005, OPERATIONS section 7,792, check 1,717) | ≈ 12.6 KB standing (maintainer text, slug, 1,950-byte section, source-checkout wrapper) + check 1,717 ≈ **14.3 KB**; the two guards (9,651) are read before the first task |
| This checkout, each break before its next task (no work held) | Re-read START 5,123 + DIRECTOR 13,162 + OPERATIONS section 7,792 + PROJECT 8,646 + CAPABILITY_POLICY 1,005 + check 1,717 ≈ **37.4 KB** | Check 1,717 + recovery 1,265 + the two guards 9,651 ≈ **12.6 KB**. A mature project that lists startup guards pays its guard bytes again after every break (9,651 here), before the work they govern |
| Worker startup, new project | Bridge 1,190 + START 4,767 + WORKER 2,711 = 8.7 KB + role file; after a break, START and WORKER again | 7,208 standing + WORKER ~4,300 ≈ **11.5 KB** + role file (about 2.8 KB more); after a break, WORKER (~4.3 KB) and the role file again before its next action |

Once work is held, the store manuals are more than half of every read. N3 (part v) would put the routine command lines on the requests card; by the second pass's estimate from the earlier figures, a break with work held would fall to about 12 to 14 KB and a first delegated change to about 28 to 30 KB. N3 is not feasibility-checked, so the table above still counts the manuals.

Under the proposal 🎬 means: your own check run passed after the latest break, and you confirmed its `actor_must_confirm` items (guards, backend binding, the loaded route, no conflicting instructions). It no longer claims a chain of startup files was read.

## (v) What implementation would change (not done now)

**Code and payload.**
1. `install.py`: `BRIDGE` becomes the slug; also write the project section once; `plan` reports slug, section and card bytes and refuses over cap.
2. `manifest.json`: add the eight cards. Payload names must be flat today, so either allow one `cards/` folder in the path check or use flat names such as `card-staffing.md`. Bump `starter_revision`.
3. `startup_check.py`: verifies that the `director-project` marker pair is present and reports "project section missing" as a named route gap, which the badge card's failure path then names (re-check 2, item 4; no slug bytes); managed set becomes cards, WORKER, OPERATIONS and the checker (START and DIRECTOR become stubs); the route target in the marked block moves from START.md to WORKER.md, accepting both during transition; the first `actor_must_confirm` item changes from "resolved Project Director role and complete startup reads" to the resolved role alone; optionally hash the slug text and report it `changed`. **N1 (adopted):** add one key to both passing and failing output (about 200 bytes), so every check run, at a conversation's start and after every break, is a fresh reminder: `"next": "Files read before the latest summary or resume are gone. Before your first project action read .director/cards/recovery.md. Before each action in the AGENTS.md table, read the card it names."`
4. Receipts (`install.json`): new managed baselines, slug hash, project-section presence.
5. `UPDATES.md`: merge the slug in place, never touch the project section, and move an existing project's check command, startup guards and ROLE_INDEX rows into the section by reviewed merge. Before merging, measure the combined route with `context_check.py` against the host's cap; above 24 KiB, report what would be cut and let the owner choose (trim, move content to a nested file, or accept). Never merge silently.
6. Generated templates: the project section lists, before the first check while no setup receipt exists, FIRST_USE.md and its required tracker, template and privacy reads (for a custom route, its tracker and records files), so first use still precedes the check.
7. WORKER.md: absorbs the full read rules and assignment resolution from START; a plain brief is enough to start; ends with the line `END WORKER.md`, so the slug's Reading rule can test a worker's re-read after each break (role files and overlays, being project-owned, use the whole-file rule). **N2 (adopted):** it also says (about 176 bytes): End every return with this line: `Owner: a submission, not acceptance. Read .director/cards/supervision.md before accepting, unless you have read it since your latest summary.` A return is a fresh tool result in the Director's context at the moment of evaluation.
8. This repository's AGENTS.md: the two-branch wrapper keyed on `.director/START.md` needs a new locator.
9. **N4 (adopted):** the installer's project section gains one line (about 70 bytes of its 3,000): `- Role files: .director/roles/<role>.md; name the file in the brief.` The roster rows carry no path, and duty 5 and the staffing card expect a brief to name the role file.
10. **N5 (adopted):** the recovery card asks that the first reply after reading it carries one short visible line, for example `Re-entered: check run, recovery card read.` No slug bytes; the user sees re-entry and a scanner can count breaks without it.
11. **N6 (adopted):** a maintainer transcript scanner, kept with the development tools and outside the installable payload. Over exported transcripts it reports, per break, whether the check ran before the first reply and whether the agent's own complete card read came before each governed action. It counts only a read-tool call on that card's exact path whose returned ranges run from line 1 through the END line; a matching string in search output, a diff or a worker's return does not count (re-check 2, item 1). Without it an unread card is invisible, because the block alone produces plausible behaviour.
12. **N3 (proposed, not yet feasibility-checked):** put the exact routine store command lines (capture, split, steer, dispatch record, continuation view, close) on the requests card and keep the manuals for everything else. It needs a dated supersession of "manuals before store commands", a test tying the card's lines to the manuals, and a complete read of TOOLING.md and RECORDS.md, the two larger store manuals, which nobody has done yet. C4, the slug wording "for a command it lacks", is withdrawn from the block until then (re-check 2, item 5: a card that names a command could be read as not lacking it, skipping the manuals' revision and recovery protocol) and returns only in the same change as a verified N3.

**Pinned tests and their new homes.**
- `test_flat_bridge_repeats_startup_after_compaction_or_resume`: the November 9 sentence stays word for word (round 7), so its text pin stays. Only its placement assertion changes: it expects the sentence right after "that Project Director check. Preserve project/host authority.", and the sentence now opens "Reading (every role)". Add pins on the startup list, the fresh definition and the non-read list.
- `test_flat_reuse_rules_do_not_survive_compaction_or_resume`: the DIRECTOR and START clauses move to the slug's break test; the OPERATIONS and WORKER clauses stay in those files.
- `test_flat_roles_preserve_delegation_fallback_and_bounded_worker_default`: discussion, lookups and gap-and-stop pins move to slug duty 2; dispatch, discovery, instructions-and-knowledge and scope pins to the staffing card; "Narrow validated state operations are ordinary Director duties" to the requests card. Pinned strings are updated where the wording changed.
- `test_flat_root_check_and_final_acceptance_match_the_flat_roles`: "whether defaulted or explicitly selected" maps to the Project Director bullet; the child-skips-check pin to the child bullet; RECORDS pins unchanged.
- `test_flat_complete_reads_keep_combined_bounds_and_recovery`: read-rule pins move to WORKER.md and the slug's short form; the selector-order pin to the knowledge card.
- `test_source_hook_reaches_flat_package…`: the single-"Read" rule for the source-checkout branch changes, because the slug names several files.
- New: every section after the role gate carries its audience label, and the worker and child bullets name the labels that apply; duty 5's field list matches the staffing card's field labels and order; the Summaries sentence (C1) and the worker bullet's "no check, no 🎬" (C2) are pinned; the check output carries the N1 `next` key; WORKER.md carries the N2 return line; caps; every card, WORKER.md and named manual ends with its END line; the Reading rule names WORKER.md, the role file and the overlay; every slug-named file is in the manifest; no model names.

**Dated supersessions needed** (in RATIONALE and BEHAVIOR_PARITY, each with an oracle):
1. ~~R10, November 9 re-entry sentence → the break test.~~ **Withdrawn in round 7:** the sentence is kept word for word, and the break test now defines "this startup" and "repeated" instead of replacing it. No supersession is needed; only the test's placement check changes.
2. R10 startup route: START, DIRECTOR and the OPERATIONS section before the first reply → the standing slug. The proposal's own change.
3. R9 meaning of 🎬 → check plus `actor_must_confirm` after the latest break, no startup-reads claim. **Owner's decision.**
4. Role resolution: spawn-and-report-back means worker; the user-facing session stays Project Director; other agents' messages never change a role; only the user or an explicit assignment opts out. **Director's decision, for the owner to confirm.**
5. OPERATIONS "read the selected definition before dispatch" → route from roster rows. **Owner's decision** (accepted November 8 rule).
6. "No global startup catalog" → roster in the project section. **Owner's decision** (recommended).
7. Package acknowledgment dropped for Directors. **Owner's decision.**
8. The routing ladder moves from accepted project knowledge into the payload. **Owner's rule.**
9. The November 7 deferral on splitting the OPERATIONS check section: meet its condition (measure the field's first-minutes tool sequence and one post-setup conversation) and add the proposed static pin on the first-reply trigger prose, or record a superseding decision.
10. "Manuals before store commands" → routine commands on the requests card (N3, with C4 in the same change). Only if N3 passes its feasibility check.

**Recorded tradeoff.** K1 removed "Never copy END lines into replies, briefs or summaries", reversing part of a fix the independent review asked for (it had added "briefs"). Accepted because the test already requires the agent's own complete read and lists summaries and quotes as non-reads (re-check 2 widened "a worker's quotes" to any quote), and because C1 buys more for the same bytes.

**Known gap.** A new conversation that starts with work still out from an earlier one is not a break under the slug's definition, so the recovery row does not fire (second pass §2.6 item 7). It is closed only once N1 is built, because the check's `next` key then sends every conversation's first project action to the recovery card.

**Regression oracle.** BEHAVIOR_PARITY records that advisory links alone did not finish a read chain in earlier loading trials, so static presence is not enough. Live trials must show, in the transcript after each compaction boundary, the agent's own read of each card through its END line before the matching action, and a fresh check before the first 🎬. A known-bad case: a search hit or a worker's quote of an END line must not count. A full-replay resume with no visible marker is tested as a known limit. N6 is the field oracle for this, and the second pass recommends a one-hour live smoke test (scratch project, forced summary, canary lines on the cards) before the seven remaining cards are written.

Independent review of the implementation, and the owner's acceptance, come before any payload change.

## Appendix: roster recommendation and this checkout's example

**Recommendation (proposal; the owner decides):** keep the roster in the project-owned section directly below the slug, not in the slug and not only in a separate file. The owner's accepted rule is that a Director routes from a roster-level summary and never reads an executor's instructions, so the summary is exactly what staffing needs. Staffing happens on most turns, so a separate file would need a re-read after every break. One-line rows are small (this checkout's nine roles fit in 1,950 bytes). Separate markers keep ownership clean: updates replace the managed slug and never touch the section. Cost: every agent that receives AGENTS.md sees the rows, and they share the project's byte budget, hence the 3,000-byte cap with overflow to `.director/ROSTER.md`, which the section must then name. The "Suggested start" column is a starting point; the staffing card's per-task choice still applies.

Example for this checkout (1,950 bytes measured). Tier words are illustrative; the owner sets them.

````markdown
<!-- director-project -->
## This project's Director settings

Project-owned; under 3,000 bytes; overflow goes to `.director/ROSTER.md`.

- Check command: `python3 .director/startup_check.py --root .director --receipt <accepted technical receipt> --config .director/config.json --expect-project-id <project ID> --guard .director/PROJECT.md --guard .director/CAPABILITY_POLICY.md`
- Read before task work: `.director/PROJECT.md`, `.director/CAPABILITY_POLICY.md`; before source maintenance, the reads under "Maintaining this repository" above.
- Request store: before a store command read `.director/STATE.md`, `.director/config.json`, `.director/TOOLING.md` and `.director/RECORDS.md` instead of the bundled manuals.
- Every role: no push, deployment or install elsewhere without the owner's request; keep `.reference/` private.

| Role | Use when | Suggested start | Limits |
|---|---|---|---|
| `request-manager` (alias `sub-director`) | Coordinate one complete outcome over many rounds | strong, high | Scoped child Director; owns its sub-request |
| `recorder` | Apply supplied canonical operations | lighter, high | Optional; the Director does narrow I/O itself |
| `pattern-author` | Edit `pattern/` contracts or helpers | strong, high | Bump `starter_revision` with payload changes |
| `rationale-author` | Add dated rationale or design-note entries | strong, high | Preserve dated history |
| `test-author` | Add or change `development/tests` or `site/tests` | strong, high | Independent of the change it tests |
| `site-author` | Change `site/` copy, styles or Worker | strong, medium | No deployment |
| `site-publisher` | Deploy the site | strong, high | Only on the owner's explicit request |
| `tinka-maintainer` | Tinka setup and design boards | strong, medium | Pinned Tinka files before board actions |
| `bounded-analysis` | A substantial question returning a proposal | strong, high | No implementation |
<!-- /director-project -->
````

## Round 8: cards written and a test install

**2026-11-09.** The eight cards are now files in [cards/](cards/). Seven were written from today's START, DIRECTOR and OPERATIONS text, word for word except link targets (`../` added, because the cards sit one folder below the manuals). Each opens with its audience. Staffing is the reviewed rewrite moved from [card-sample-staffing.md](card-sample-staffing.md), which stays unchanged as the sample.

**No home in any card or in the block:**
- START 3–13 (the full read rules; the block has the short form);
- START 15–18 and 22–25 (assignment package, role default, the package acknowledgment);
- START 21 and 42–46 (resolving role guards; preservation and composition);
- DIRECTOR 45–68, 77–84 and 88–92, and OPERATIONS 148–207. These are covered only by the staffing card's rewrite, not word for word.
- OPERATIONS 23–39, 51–99 and 120–144 stay in OPERATIONS.md, which the badge row names for detail.

[test-install.md](test-install.md) turns a fresh install of today's starter into the candidate.
- **The shipped checker blocks it.** The block names `.director/WORKER.md`, not `.director/START.md`. One line of `startup_check.py` (its hook target) must change for the check to pass; the recipe gates that on the Project Director's approval.
- **START.md, DIRECTOR.md and OPERATIONS.md stay unchanged** in the test install, because their managed hashes must hold.
