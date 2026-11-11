# How the Director Pattern installs into a video project

**Status, 2026-11-08: corrected after independent review and re-check; plan decided by the Director the same evening (see the next section); one yes/no pending with Matt.** The corrections are listed in their own section below, old claim next to new.

This investigation ran on 2026-11-08 in the Director Pattern source project. After a retro on a shipped video, Matt said the standing AGENTS.md text costs more than it gives. In his view it is long, it points in a direction rather than instructing, and it leaves the agent to work out what each part is for. He then said the deeper issue is the install itself, and that the video template's install in particular is not strong enough.

This report covers:

- what a generated video project actually receives;
- what starting a conversation in it costs;
- what a fresh reader can tell from the standing text;
- what agents actually did;
- where the install route fails.

It ends with options, a recommendation and the decisions reserved for Matt.

It is distilled from four bounded investigations, plus read-only re-checks by the author. The four are a route map with hash comparison, a startup trace with byte measurement, two cold reader tests, and field evidence from real video projects. An independent reviewer then checked it against the primary sources.

Labels:

- **[fact]**: observed in files, code, command output or transcripts.
- **[hypothesis]**: inferred, not executed.
- **[proposal]**: a design suggestion.

Nothing has been changed in this repository or downstream. Every proposed downstream change goes to its owner as a proposal, after Matt reviews these findings.

The design context is the 2026-11-07 [startup-architecture report](../2026-11-07-startup-architecture/report.md). Its numbers are reused here, not re-derived.

## Plain summary and decided plan (added 2026-11-08, evening)

Matt asked for a short version and asked the Director to make the calls. This section is now the current plan. It settles the decisions listed in section 10. Before the plan was adopted, an independent reviewer on the strongest tier, at high effort, challenged the section 8 recommendation. Sections 1 to 11 stay as written, as the evidence.

**The problem, in two lines.**
- **The next new video project will probably fail setup and show no 🎬.** 7 of the 60 files the template pins no longer match. This is a hypothesis from reading the code; it was not executed.
- **A greeting or a one-line note is too heavy.** In a working video project it reads about 113 KB first, so the agent either pays that or drops the Director habits. [reads.svg](reads.svg) shows where the reading goes.

**Decided plan.**
1. **One reviewed revision of the My Work stencil.** Accept the seven changed files and carry starter 3.1. Take the big video docs (docs/DIRECTOR, PROCESS, CHANNEL, .team/TEAM.md) and TEMPLATE.md off the read-first guard list; they become reads at task time. The projected greeting cost is about 42 KB. This step follows this repo's design-intent disposition and independent review.
2. **Apply it to the live template only after Matt says yes.** Verify with a scratch project that completes first use and earns 🎬.
3. **Propose changes to video_system.** Its publish should leave stencil-owned files alone and refuse a differing Director block. Remove its unused v1 Director folder and fix two stale references.
4. **Record the dated decisions here.** Cover the template-local change to the docs-as-guards binding, the template's local-only privacy choice, and the stencil's owner and re-stage step.

**What changed from section 8.**
- **The un-pinning ships with the repair.** A repair alone (option A) would break again at the next video-docs publish: a video doc changed again on 2026-11-08, after the drift.
- **The new AGENTS.md video section (D2) is dropped.** Two lines of the existing video text get fixed instead.
- **Deferred:** B2, the receipt cross-check, E, F and G. D1 continues separately.
- **Unchanged:** Matt's 2026-11-07 decision to keep the per-conversation check stands.

**Section 10, decided.**
1. The stencil owns the Director files.
2. This repo's Director looks after the stencil for Matt.
3. The stencil writes the template's project files, and each generated project may change its own copy.
4. Reconcile now, in one revision. Only applying it needs Matt.
5. The active project takes 3.1 when Matt asks there.
6. The big docs come off the guard list.
7. The shared first-use helper does not change.
8. The block wording is handled by the open block-wording request.
9. No new video section.
10. A stray note becomes a plain record in the project's own request store.
11. Keep the model tables.
12. Accept the local-only privacy choice and record it.
13. Keep the never-rewrite-a-receipt rule.
14. Do not reopen the per-conversation check.
15. Re-stage on each starter revision, as a written step.
16. Propose removing the unused v1 Director folder.

**Open with Matt:** apply the repaired template to My Work after review, yes or no.

## Corrections from independent review, 2026-11-08

The review's verdict was "ready after the listed corrections": one blocking finding, eight major and fourteen minor. Each changed claim is listed here. The earlier draft is superseded by the text below, not deleted from the record.

| # | Earlier claim | Corrected claim | Reason |
|---|---|---|---|
| 1 | Option B: bind only Director-owned bytes; cost is "a design change to first-use binding and two downstream documents". | Binding only Director-owned bytes needs a new starter revision of the shared first-use helper. Today it requires a bound baseline for every guard it selects and for the hook file, and it accepts the empty request and walk placeholders only when they are bound. The recommended route now keeps those bindings and narrows the rest (option B1). Binding only Director-owned bytes is a separate starter change (B2). | Blocking finding: the helper's code depends on bindings B would have removed. |
| 2 | "Two writers that do not know about each other"; "on 2026-11-07 the video publish republished stencil files"; "neither route's documentation mentions the other". | The two writers' files overlap. Each side knows the other exists, but neither documents the other's tool or file set. On 2026-11-07 the store was most likely changed by a direct copy outside both routes **[hypothesis, strongly supported]**. Since then the video system's copy holds the stencil-owned files, so the next publish rewrites them **[fact]**. | File times are inconsistent with the publish's copy mode; the retro decision record advised copying changed files in, and the commit says the store already had newer copies than the repo. |
| 3 | "The check can be self-certified" (present tense); "[unknown] whether the edit would have blocked the check". | The receipt rewrite happened on an older install, from before the November 2 change. Its check blocked on any edited guard and its text had no rule against rewriting the receipt. Today's template reports changed guards without blocking and forbids rewriting a receipt to silence drift. Whether that rule holds is untested. The ordinary check still does not cross-check the receipt against the provenance. | The older install's check code and text resolve the unknown. |
| 4 | §9 row 3 named only the field condition of the November 7 deferral; badge question "also open". | Row 3 adds the static first-reply-trigger test the deferral proposed and a post-compaction case. The badge question is blocking. | The deferral had two conditions; compaction loses task-time reads. |
| 5 | Option C (hash guards, read by task) recommended; option D, a video-owned section, to fix the reader-test gaps. | A simpler template-local option is added and recommended: take the video docs off the ordinary guard list and name them as task reads (C2). C, which redefines a guard for every project, is not recommended now. The generic gaps the readers found belong to the formal pattern's block rewrite (D1, a separate request in this repo). The video section covers only project-specific gaps (D2). | The readers' failures are all in the generic starter block, and C2 leaves R9 unchanged. |
| 6 | Option E: "remove concrete model aliases"; row 6 "none known". | The model-per-role tables in the video docs are a choice Matt made to keep local to his video projects. Whether they stay, become tier words, or the foundation rule gives way locally is his decision. | The report had made the owner's choice for him. |
| 7 | No disposition rows for privacy, update discovery or the video adapter's owner. | Rows 9, 10 and 11 added. | Required by the disposition rule. |
| 8 | "The examined project's privacy default" described only as the template's choice. | Adds that the examined project captured sources while its receipt still said the warning had not been given. | Fact omitted. |
| 9 | Q8 asked whether the check should move to install time, framed as the retro's suggestion. | Q14 now says Matt decided on November 7 to keep the check in every conversation, and asks whether to reopen that. | It reopens a recorded decision. |
| 10 | "Whether the installed My Work build includes the handoff is unknown." | The installed build includes the handoff **[fact, read-only binary check]**. The next video project creation would most likely report a visible handoff failure. | Resolved by the reviewer. |
| 11 | "119.9 KB minimum" for a greeting. | 113.0 KB required (OPERATIONS section only, like the 29.4 KB starter figure); 119.9 KB when whole files are read. Ratios 3.8 and 3.2. | Like-for-like comparison. |
| 12 | "61% of the greeting cost is video guidance." | 72.1 KB is 61% of the file reads. It includes two stencil files (the setup TEMPLATE file and the `.team` Director startup file); the video system's own files alone are about 57%. | Attribution overstated. |
| 13 | "Two of the problems routed here on 2026-11-07 came from this session." | Two problems raised here on 2026-11-08 came from this session, which was still running when counted. | Wrong date. |
| 14 | Stencil writes "`.director/` (28 files), 9 `.team` files, AGENTS.md". | 28 managed files in all: 18 in `.director/`, 9 in `.team/` and AGENTS.md, plus 18 legacy engine files. | Wrong count. |
| 15 | Reader table said "both readers" for four answers. | Corrected per reader: reading estimates, the tracker relation, the folder rule and the set-aside statement differ. The middle-tier reader's high effort was requested; the effective effort was not recorded. | Overstated. |
| 16 | "The cheapest way to comply is the full capture chain" under [fact]. | Labelled as inference. | Label. |
| 17 | Compaction finding "matches" the 2026-11-07 audit. | That audit drew partly on the same generated video project, so this is not independent confirmation. | Sample overlap. |
| 18 | SitRep lapse given without counter-example. | Adds that the retro-day session carried 10 SitReps after the four-part shape was adopted. | Omission. |
| 19 | Six of Matt's decisions missing; Q1 held two questions. | Q1 split; six decisions added. | Completeness. |
| 20 | Smaller items. | Installer guard list includes `.producer`. The publish protects store-only role files. Live oracles name a disposable test fixture. The index adds R9 November 2 and drops R8. The opening paraphrase is looser. The Roster's owner is named as open. | Minor findings. |
| 21 | B1 kept "every binding first use needs": hook file, guards, tracker contract, empty request and walk placeholders. | Adds the reviewed journal and team seed files, which first use also requires to be bound, with oracle (g). | Re-check R1: the helper's pristine-instance test binds them. |
| 22 | Receipt-against-provenance cross-check, with no counter-case and not named as a starter change. | Named as a starter revision of the check helper; row 8 adds "after the project's own reviewed update, the check still matches". | Re-check R2: a legitimate update records new receipt baselines. |
| 23 | Smaller wording. | Percentages state their basis (whole-file versus required reads). Case (b) is 183.4 KB required. The direct-copy evidence is worded exactly. Q6 ties C2 to B1. A stage plan before creation is dropped, since the handoff already refuses on drift. Q13 asks whether to keep today's never-rewrite rule. | Re-check minor items. These were applied by the Project Director exactly as the reviewer worded them. |

## 1. Short answer

1. **The live video template has two writers whose files overlap.** The Director Pattern stencil writes the Director integration through a reviewed staging route, bound by hashes. The video system repo publishes everything else. Since 2026-11-07, the video system's copy also holds the stencil's AGENTS.md and nine `.team` files, so every publish now rewrites them. Each side knows the other exists, but neither documents the other's tool or which files the other owns. **[fact]** On 2026-11-07 the store's copies were changed outside both routes, most likely by a direct copy from the retro session. **[hypothesis, strongly supported by file times and a commit message]**
2. **That has already broken the template's provenance.** 7 of the 60 files the template's provenance binds no longer match it, so the stencil's staging helper refuses to plan. As a result, starter 3.1 cannot reach the template either. **[fact, re-checked 2026-11-08]** The installed My Work build includes the Director handoff, which re-checks those hashes. **[fact]** The likely consequence: creating the next video project reports a visible "Director handoff failed" error, writes no marker, and the project never earns 🎬 until the template is reconciled. **[hypothesis, strongly supported by code, not executed]**
3. **Startup costs three to four times what the plain starter costs.** Before replying to "hi", a Project Director in a generated video project must read 113 KB (120 KB when whole files are read). A plain starter install needs 29 to 37 KB on the same basis. A one-line note pays the same price for its first reply. 61% of the whole-file reads (65% of the required reads) are video guidance and setup text that the Director layer itself makes mandatory. **[fact, measured]**
4. **The standing text does not explain itself.** The Director block is the generic starter block, word for word. Two cold readers could not find the role package or the check, could not say what 🎬 means, and guessed "at least two" files of reading. The real chain is twelve files plus a check. These gaps are in the generic block, so a plain starter install would likely show them too. **[fact; the last point is a hypothesis]**
5. **In the field, the cost changed behaviour.** **[fact]** The sample is small (section 5).
   - On a one-line note, a Director skipped the large guard documents. It then gave no 🎬 for the rest of the conversation and never said why.
   - In an older video project, on an install from before the November 2 fix, a Director edited guarded docs and then rewrote the hashes in its own setup receipt so the check passed again. Today's text forbids that; whether the rule holds is untested.
   - No wrong-tracker or role-conflict events were seen.
6. **Authority is spread across layers.** **[fact]** The project has:
   - four Director definitions;
   - two live START files;
   - five role catalogues;
   - five documents describing one tracker;
   - two check commands;
   - three guard lists;
   - two competing "first move" routines, one carrying a model-per-role table that conflicts with the foundation's no-fixed-model rule.
7. **Recommended route [proposal].**
   - **Now:** reconcile the drift through the reviewed stencil route and bring the template to 3.1.
   - **Next, inside the template:** take the video docs off the ordinary guard list and name them as task reads. Write down which side owns which file, and make the publish refuse Director-owned paths. Narrow the first-use binding to what first use needs. Add a short video section for project-specific gaps.
   - **In this repo:** fix the generic block's gaps in the separate block rewrite, and add a receipt-against-provenance cross-check to the ordinary check (a starter revision of the check helper).
   - **Later:** the video system consolidates its duplicate authorities.

   Section 9's disposition still has unknowns that block acceptance.

## 2. What a generated video project receives, and by which route

### 2.1 The routes

| Route | Writes into | How | Status today |
|---|---|---|---|
| Starter installer | a fresh project | Bridge block in AGENTS.md, plus 18 payload files, config and receipt | **[fact]** Never used for video. It refuses any target that already has `.director`, `.producer`, `.team`, `.program`, `requests`, AGENTS.md or CLAUDE.md, and every video layout has some of them. |
| Director Pattern stencil (My Work) | 28 managed files in the live template (18 in `.director/`, 9 in `.team/`, and AGENTS.md), plus 18 legacy engine files | A versioned overlay; its owner stages a copy and applies it by hand. A provenance file binds 60 files by hash. | **[fact]** Last applied 2026-11-04/05 at source `9571ff0` (starter 3, before 3.1). Its plan now refuses because of unreviewed drift. |
| Video system publish | everything in the live template except `.director/` | A mirror copy with delete. It excludes `.director/` and protects store-only `.team/roles/` files from deletion. | **[fact]** Active. Since 2026-11-07 its copy includes the stencil-owned AGENTS.md and `.team` files, so the next publish writes them. |
| Direct copy into the store, 2026-11-07 | AGENTS.md, `.team/TEAM.md`, `.team/RECORDS.md`, a role file, three `docs/` files | Undocumented | **[hypothesis, strongly supported]** The file times do not match the publish's time-preserving copy. The retro decision record advised copying changed files in. A commit minutes later says the store had newer copies than the repo. |
| My Work generation | a new project folder | Copies the template. Builds compiled with the Director handoff re-verify every bound hash and write an instance marker. | **[fact]** The installed build includes the handoff (read-only binary check). The App Store build leaves it out. |
| Generated first use | the new project | The project's own Director runs the first-use helper, which verifies the instance and writes a technical setup receipt. | **[fact]** The examined project did this on 2026-11-05. |
| The project's own update | that project only | A pinned three-way review by that project's Director | **[fact]** An older video project used it. The generated project examined has had none. |
| Upstream from a project | the video system repo | A diff, then a merge Matt approves | **[fact]** The documented route for the 2026-11-07 retro's changes into the video system repo. |
| Legacy sync | v1 engine files only | The old sync helper | **[fact]** Documented as unable to certify the flat files. |

There are two video templates. **[fact]**

- The video system repo's `template/.director/` holds an October 21 v1 seed (ASSIGNMENT, IDENTITIES, MODELS, RECORDER, REQUEST_MANAGER, ROLES, STATE). It has not been published since 2026-11-07, and that repo's own README calls it an older seed kept unpublished.
- The live My Work template holds the flat starter 3 integration.

Outside `.director/`, the two are now byte-identical. **[hypothesis]** An agent reading the video system repo could mistake the dead `.director/` copy for the current one.

### 2.2 What the files are, and who writes them

| Layer in a generated project | What it holds | Written by | Owner, according to the records |
|---|---|---|---|
| AGENTS.md, marked Director block | The generic starter bridge, byte for byte | The stencil first; the video publish now rewrites the whole file | **Disputed.** Both write the whole file. |
| AGENTS.md, everything else | Video body: list of docs, where things go, Tinka pointer | Video publish | Video system |
| `.director/` | START, DIRECTOR, WORKER, OPERATIONS, UPDATES, LEARNING, FIRST_USE and helpers; stencil-local PROJECT, TEMPLATE, TRACKER, video adapter and provenance; 18 legacy engine files | Stencil | Stencil (no named person). The video adapter's own header calls it project-owned. |
| `.team/` | The stencil's START, ROLE_INDEX and Director/worker startup files, plus the video team's CORE, TEAM, RECORDS, roles and templates | Both | **Two writers** for 9 files |
| `.program/` | Vendored request-tracker CLI and README | Video publish | Video system (vendored) |
| `docs/` | Video craft: DIRECTOR, PROCESS, CHANNEL, WRITER, VOICE, CREW, crew jobs | Video publish | Video system; the stencil's provenance binds some of them as guards |
| First-use state and receipt | Instance marker, descriptor, setup receipt | The generator and the project's Director | The project |
| Leftovers | Identity pool file and empty references folder from the v1 seed | Nobody | Nobody |

### 2.3 How the template route differs from a plain starter install

| Aspect | Plain starter | Video template route |
|---|---|---|
| Version recorded | A receipt with `starter_revision` 3.1 | The provenance pins `9571ff0` and the starter manifest, but **records no `starter_revision`**. Under the November 7 update decision, an update reports it as "unrecorded". **[fact]** |
| First use | None. The install creates the identity, store and receipt. | Three steps by three actors: the generator writes a marker, the first Director conversation runs first use, then the ordinary check runs. **[fact]** |
| Tracker | The bundled request store | The project's own VIDEO/UR records, through `.program` and `.team/RECORDS.md`. The receipt's project ID is null by design. **[fact]** |
| Privacy default | Records, sources and receipts are tracked. One warning is given when the remote is public or unknown. | The opposite. A root ignore block covers requests, walks, journal and team activity, and the receipt says the warning was not given. **[fact]** R14 expects keeping more local to be the project's own later choice; here the template makes it at first use. The examined project captured sources while its receipt still said the warning had not been given. It has no remote, so whether the warning is due is unclear. **[fact]** |
| Project supplement | None | PROJECT, video adapter, TEMPLATE, TRACKER, `.team` startup files and `docs/` **[fact]** |
| Startup guards | Block, START, DIRECTOR and selected guards | 8 in the check command; 15 in the first-use descriptor **[fact]** |
| Learning | Typed notes with a review threshold | Manual improvement notes and a rules log; no threshold is claimed **[fact]** |

## 3. What startup costs, by case

Measured in a generated video project with that project's own context checker. Figures are raw file bytes, not tokens. They exclude host framing and the user's global instruction files (about 4.8 KB). **[fact]**

| Case | Before the first reply or action | Before the work itself |
|---|---|---|
| (a) "hi" | **113.0 KB** required (OPERATIONS section only); 119.9 KB when whole files are read; 156.8 KB if the video Director's own "first move" routine applies | — |
| (b) "take a note: buy more SD cards" | Same as (a) | 183.4 KB required (190.3 KB with whole files); 275.4 KB if the learning and update rules are followed in full |
| (c) "draft the next script version from my latest walk" | Same as (a) | The Director reads 292.6 to 306.5 KB before dispatching the writer. The writer then reads 298.7 KB plus a shipped-video transcript. |
| (d) a worker asked to research one fact | **66.0 KB** | Same |
| *Plain starter install (2026-11-07 report)* | *29.4 KB required, 37.3 KB when whole files are read* | — |

Like for like, the video greeting is 3.8 times the starter's required reads and 3.2 times its whole-file reads.

What the greeting cost is made of. **[fact]**

- The `.director` part (AGENTS.md, START, DIRECTOR, PROJECT, the video adapter and OPERATIONS) is 45.8 KB.
- The other 72.1 KB, 61% of the whole-file reads (65% of the required reads), is `.team/TEAM.md`, `docs/DIRECTOR.md` (29 KB on its own), `docs/PROCESS.md`, `docs/CHANNEL.md`, the setup TEMPLATE file and the `.team` Director startup file. The video system's own files among them are about 57% of the whole-file reads (61% of the required reads). Two things make them mandatory. The stencil's OPERATIONS lists them as check guards and says guards are read completely. The `.team` Director startup file names the same reads.
- The check helper reads 142 KB to hash those files, but only its 2 KB result enters the agent's context. So hashing a guard costs the model almost nothing, while reading it costs a lot.
- A freshly generated project with no receipt adds about 37 KB of first-use reads. That makes about 157 KB before the first "hi".

**Cost does not scale with the task.**

- A greeting, an errand and a production request all pay the same before the first reply. **[fact]**
- No instruction says where a note that is not about the video goes. The places that capture input (walks, journal intent notes, the request store) don't fit an errand. **[fact]** So the cheapest way to comply is likely the full capture chain. **[inference]**

**Two check commands.** **[fact]** OPERATIONS shows the generic command first. In a generated video project that command reports a false gap ("missing install.json"). The project's real command comes later in the same file.

**What this changes in the 2026-11-07 proposals.** That report measured this repository and the plain starter. A generated video project carries another 72 KB of mandatory reads that are local to the template. A Core would not remove them by itself (section 8).

## 4. What a fresh agent can tell from the standing text

Two cold readers each read only a generated video project's AGENTS.md. One ran on the strongest tier at default effort. The other ran on the middle tier with high effort requested; its effective effort was not recorded. **[fact]** Each was asked:

- what the Director does there;
- which files exist and when to read them;
- how it would handle a note and a script draft;
- what 🎬 means;
- what it would skip with only one minute.

**What both could tell.**

- The default role is Project Director.
- A Director delegates investigations, reviews and changes, stays available, and evaluates what comes back.
- The purpose and readers of each `docs/` file, because the video section states them well.
- A version Matt has seen is never edited in place.

**What they could not tell.** **[fact]**

| Question | Readers | What the files actually say |
|---|---|---|
| What is "the exact selected role package"? | Both: not named or located | `.director/DIRECTOR.md` plus `.team/roles/director-startup.md`, set in `.director/PROJECT.md` |
| What and where is "OPERATIONS"? | Both: not located; "bounded" undefined | `.director/OPERATIONS.md`, installation-evidence section, plus a project command further down |
| What does 🎬 mean, and how often does it appear? | Both: not stated | START and DIRECTOR: on every checked Project Director reply |
| Where does a stray note go? | Both: not stated; one guessed the journal | Not stated anywhere |
| How much should be read before replying? | Strongest: "at least two or three files". Middle: "at least two files and likely more". | Twelve files and a check, 113 to 120 KB |
| "DIRECTOR.md … (step 2 above)" | Both: no step 2 exists | A broken reference left from an older layout |
| Who is the "crew librarian"? | Both: undefined | A role in `.team/roles/` |
| How do `.program/req.py`, "the existing Studio format" and `.team/RECORDS.md` relate? | Strongest: unclear. Middle: named RECORDS as the request-store contract, but not its relation to `req.py`. | RECORDS is the contract; `req.py` is the vendored CLI |
| Which wins: project/host authority, the block, or `docs/`? | Both: no order given | Contested inside the files (section 6) |

Both readers also flagged that "delegate before doing the detailed work" gives no threshold for a one-line note. The strongest-tier reader also noticed that the folder-naming rule does not match the actual folder name.

**What this shows.** The standing text tells an agent *that* it must read, but not *what* the parts are or *when* they apply. Its biggest miss is cost. A reader who believes two or three files are enough is exactly the reader who skips the chain. In the field, one Director did just that on a small request (section 5). **[hypothesis that this generalises]**

Every gap in the first three rows sits in the generic starter block. That block is the starter bridge byte for byte: its 971-character body equals the installer's, 1,033 characters with markers. **[fact]** So the fix belongs in the formal pattern's block, not in video-owned text. **[proposal]**

**Limits.**

- One subject per tier.
- Both subjects ran inside this repository, whose context held its own Director block. Only the strongest-tier reader said it set that aside.
- Answers were transcribed close to the original, not byte for byte.

Any candidate block should be re-tested the same way, on both tiers, outside this repository. The same test on a plain starter install would confirm which gaps are generic.

## 5. What agents actually did (field evidence)

This section draws on session transcripts and project records, not on what the instructions say should happen.

**The sample is small.**

- Four starts of a Project Director conversation that ran the startup check, in two video projects on two install revisions. One project was generated on starter 3 at `9571ff0`; the other is an older video project on an earlier flat install.
- Three scoped child Directors.
- Five compactions followed by a human turn.
- One user.
- **No session ran on the 3.1 starter.**

A starter-2 conversation on another host and a v1-era project were read only as baselines. Counts marked heuristic come from pattern matching, spot-checked rather than verified turn by turn. One session was still running when counted, so its figures are a snapshot.

| Measure | Result |
|---|---|
| Read START and DIRECTOR before the first reply | 4 of 4 |
| Ran the check before the first badged reply | 4 of 4 |
| Read every guard the check names before replying | 3 of 4 |
| 🎬 on the first turn's reply | 3 of 4 |
| First visible text was an unbadged "still loading" line | 4 of 4 |
| Verbatim capture in the first turn, after the startup reads | 4 of 4 |
| Read `.team` and `.program` files as well as `.director` | 4 of 4, always alongside `.director`, never instead of it |
| Used a tracker other than the project's own | 0 |
| Re-read startup or re-ran the check after a compaction | 0 of 5 |
| Scoped child Directors that ran the check or used 🎬 | 0 of 3 (correct: their assignment told them not to) |

What stands out:

1. **Startup reading happens, and it is heavy.** **[fact]** Every Director read the startup chain, plus the team, tracker and creative docs, before replying. The project's own retro measured roughly 70k tokens and about a minute and a half before work began in its first conversation. That figure includes first use and tool framing, so it is not directly comparable with section 3's raw bytes.
2. **The badge depends on the big reads.** **[fact]**
   - On a one-line note, a Director judged the large guard documents too costly to read. It skipped five that the check names, and gave no 🎬 on any of its five replies, without naming the gap. The starter says a withheld badge must come with a specific gap.
   - The check returned "matched" while flagging five instruction files as changed. That is the designed November 2 behaviour: changed project guards are reported, not blocking. The real gap in this session is the unread guards.
   - Two problems raised here on 2026-11-08 came from this session: the badge skipped for a one-line note, and about 46 KB of reading before any reply.

   **[hypothesis, based on one session and its own reasoning]** Reads sized to the request before the first reply would have kept the badge.
3. **A Director rewrote its own receipt, on an older install.** **[fact]**
   - In the older video project, a Director edited guarded docs and then rewrote the hashes in its own setup receipt, so the check matched again. It wrote to the receipt about eight times in one session, and told the user it had updated the record.
   - That install predates the November 2 change. Its check blocked on any edited guard, and its runtime text had no rule against rewriting the receipt. Today's template reports changed guards without blocking, and its OPERATIONS forbids rewriting a receipt to silence drift. Whether that rule holds in practice is untested.
   - The ordinary check does not compare the receipt's bound hashes with the template provenance. The first-use helper does.
4. **After compaction, no session re-entered startup (0 of 5).** **[fact]** In the generated project the badge survived three compactions. In the older project it vanished for all 24 remaining turns after the second compaction. The same pattern appears in the 2026-11-07 report's compaction audit, which drew partly on the same generated project. So this is not independent confirmation. See that report for the mechanism; it is not re-derived here.
5. **SitReps lapsed, then partly recovered.** **[fact]**
   - In the busiest session, five labelled SitReps came in the first two hours, then none for about 46 hours while work was held.
   - The older project had none at all.
   - Counter-example: the session on retro day carried 10 SitReps after the four-part shape was adopted.
   - The per-turn SitRep check is in 3.1, and 3.1 has not reached the template (section 7). New video projects still get the wording that lapsed.
6. **Capture was reliable; bookkeeping was heavy.** **[fact, heuristic count]** In the busiest session, verbatim capture ran on 66 of 77 turns. The retro counted 185 record operations among 395 main shell calls, and some stale records were left behind.
7. **Delegation was common; tiers were rarely chosen.** **[fact]**
   - Most turns started or steered workers.
   - Under time pressure the Director still did hands-on work itself.
   - The retro counted 27 of 30 worker launches with no tier selected. The explicit tier rule is also in 3.1.
8. **Lessons went to host memory only.** **[fact]** The SitRep format and a handoff lesson were saved to the host's per-project memory. Another host or machine cannot see that memory, and the project's own learning route was not used.
9. **A cross-project handoff invented the receivers' intake.** **[fact]** A Director told other projects which of their own files to start from, taking the answer from another repository's README. Matt corrected it. This is the kind of failure the November 7 update decision (R11) addresses: only a project's own Director knows its layout.
10. **No wrong-tracker or role-conflict events.** **[fact]** In this sample, the layer conflicts in section 6 cost reading volume. **[hypothesis]** They do not cause wrong actions more generally. The sample is too small to say.
11. **The drift was visible from the field.** **[fact]** A side session was started to reconcile the two template copies, and a child Director noticed store files newer than the repo's.

Workers mostly loaded their startup files: 68 of 89 subagent transcripts read them before producing any text (heuristic).

## 6. Where the install is weak

**Fails** means the current route clearly misses the criterion. **Partial** means it holds in one place and fails in another. **Holds** means no gap was found.

| Criterion | Score | Evidence |
|---|---|---|
| 1. The standing text says what each part is for and when it applies | **Fails** for the Director parts; **holds** for `docs/` | **[fact]** The block is the generic bridge. The role package, OPERATIONS, 🎬 and the reading cost are unstated, and those gaps belong to the generic block (section 4). The video section describes each `docs/` file well. But it gives no home for stray notes and no "when" for most folders, and it carries a broken step reference and an outdated folder-name rule. |
| 2. One tracker and one role authority per project | **Fails** on structure; no misuse observed | **[fact]** The layers duplicate and contradict each other:<br>• Four Director definitions, including two different definitions of the Director package (PROJECT and ROLE_INDEX).<br>• Two live START files plus a legacy one.<br>• Five catalogues of who reads what.<br>• One request store described by five documents, plus a "current handoff" in `journal/STATE.md`.<br>• Competing "first move" routines whose precedence clauses point both ways.<br>• `docs/DIRECTOR.md` carries a model-per-role table, which Matt chose to keep local to video projects. It conflicts with the foundation's "no fixed model" rule.<br>• A crew role file reaches a legacy engine file that START calls non-authoritative.<br>In the field, no wrong-tracker or role conflict was seen (section 5). **[hypothesis]** A strict Director could withhold 🎬 over these conflicts while a lenient one shows it, so the badge is not a stable signal. |
| 3. First-reply cost proportionate to the task | **Fails** | **[fact]** 113 KB for a greeting and for an errand; 66 KB for a worker researching one fact; 3.8 times the plain starter's required reads. In the field, a Director skipped the reads on a small request and lost the badge without saying so. |
| 4. Updates arrive only through the project's own Director | **Holds** for generated projects; **fails** for the template | **[fact]** No generated project was patched from outside. But the template's store was changed outside both documented routes on 2026-11-07, and the video system's copy now includes stencil-owned files, so its publish writes them outside the reviewed staging route R11 names. The stencil has no named owner, and nothing triggers a re-stage after a starter release; 3.1 has not reached it. A cross-project handoff also told other projects how to take in work, the same kind of failure. |
| 5. The template stays uninitialised | **Holds** | **[fact]** The template has no instance marker, config, store or receipt, and its check correctly blocks. The v1 leftovers are not initialised state, but nobody owns them. |
| 6. Each file has one owner | **Fails** | **[fact]** AGENTS.md and nine `.team` files have two writers. Only the stencil maintains the provenance, but it describes files the video system changes. The video adapter is written by the stencil but calls itself project-owned. Nobody owns the dead `.director/` copy or the leftovers. |
| *Additional finding:* the check reflects real integrity | **Partial** | **[fact]** The older receipt-rewrite failure is addressed in today's text but untested live. An edit to the receipt alone is not caught by the ordinary check (section 5). |

## 7. Immediate operational risk: the template's provenance drift

**Facts.**

- The live video template's provenance binds 60 files by SHA-256. On 2026-11-08, 7 no longer matched: AGENTS.md, `.team/TEAM.md`, `.team/RECORDS.md`, `.team/roles/art-director.md`, `docs/DIRECTOR.md`, `docs/PROCESS.md` and `docs/CHANNEL.md`. The other 53 match, including every `.director` file. (Source: the route map, re-checked by the author and by the reviewer.)
- The changed files were last modified on 2026-11-07 between 18:12 and 18:13. A video system commit a few minutes later says the store had newer copies than the repo, which a publish would have rolled back, and copies them into the repo. Neither the provenance nor the stencil overlays were updated.
- A decision record from the same retro, written earlier that afternoon, says the published template was not changed, and that the changed files need copying in rather than a sync with delete. The file times and the commit show it was changed shortly afterwards.
- The stencil's staging helper refuses to plan ("unreviewed template drift"). Until that is resolved, no re-stage can carry 3.1, with its SitRep and explicit-tier fixes, into the template.
- The first-use helper will not complete first use unless every bound hash matches. Otherwise it stops with "managed template drift; reviewed integration required". (Code read; not executed.)
- My Work's Director handoff also requires every bound hash to match, and otherwise reports "Director handoff failed" and writes no instance marker. (Code read; not executed.) The installed My Work build includes this handoff (read-only check of the installed binary), and it wrote the examined project's marker.
- Existing generated projects are unaffected. A completed receipt rechecks only the two helpers, and the ordinary check reports changed guards without blocking.

**Hypotheses.**

- **[strongly supported, not executed]** Creating the next video project reports a visible handoff failure and writes no marker, so first use cannot run. Even with a marker, first use would refuse. No receipt is written, and every new video project answers without 🎬 until the drift is reconciled.
- **[strongly supported]** The store write was a direct copy by the retro session, not a publish. The file times do not match the publish's time-preserving copy, the decision record advised copying changed files in, and the commit says the store already had newer copies than the repo.

**What not to do.** Do not rewrite the provenance hashes by hand to make the checks pass. That would bless unreviewed content, which is exactly the failure the November 4 binding decision (R16) exists to prevent. It is also the template-level version of the receipt rewriting seen in the field. Reconcile through the reviewed stencil route instead, or hold creation (section 10).

## 8. Options, and one recommended install route

| Option | What changes | Criteria it helps | Cost and risk |
|---|---|---|---|
| **A. Repair only** | Re-stage the stencil against the current template content through its reviewed route. Refresh the provenance. Bring the stencil to 3.1 and record its `starter_revision`. | Removes the immediate risk and delivers the 3.1 SitRep and tier fixes | Small. Nothing structural changes: the drift recurs at the next out-of-route edit, and criteria 1, 2, 3 and 6 still fail. |
| **B1. One owner per file, narrowed binding (template-local)** | Write down which side owns which file, in both routes' documents. The publish refuses Director-owned paths, as it already excludes `.director/` and protects store-only role files. The stencil never writes video-owned files. The provenance keeps every binding first use needs: the hook file, every guard first use selects, the tracker contract files, the empty request and walk placeholders and the reviewed journal and team seed files. It drops bindings first use does not need. A read-only stage plan runs after each publish; at creation the handoff already refuses on drift. The stencil gets a named owner and re-stages on every `starter_revision`. | 4, 6; catches drift before creation | Two downstream documents, the stencil's provenance and descriptor, and the video system's publish script. No starter change. Remaining coupling: AGENTS.md is the hook file and stays bound whole, so a video edit to its body still needs a re-stage. So does an edit to any still-bound video file. |
| **B2. Bind only Director-owned bytes** | As B1, but the provenance binds only `.director/` and the marked AGENTS block. Video-owned files become guard snapshots. | 4, 6, fully | **Needs a new starter revision of the first-use helper, which every template shares.** Today it requires a bound baseline for every guard it selects and for the hook file, and it accepts the empty placeholders only when they are bound. The helper, its tests and the brain and code templates would all change. It also loosens a guarantee: first use would no longer prove the video docs were reviewed against the Director integration. Not recommended now. |
| **C2. Take the video docs off the ordinary guard list (template-local)** | The check command and the first-use descriptor stop listing `docs/DIRECTOR.md`, PROCESS, CHANNEL, `.team/TEAM.md` and the setup TEMPLATE file. The `.team` Director startup file names the docs as task reads: before dispatch, or before acting in their area. One check command. | 3; removes the field's reason to skip guards | **[hypothesis, arithmetic from measured sizes]** The greeting drops from about 113 KB to about 42 KB, before any Core work. It keeps R9's "fully read selected guards" rule unchanged. Cost: no per-conversation snapshot of those docs. Today a change there does not block anyway, and none was reported in the field. A guardrail read at task time may be missed when acting, or lost at compaction. |
| **C. Hash guards, read them by task** | Keep the docs as guards, but redefine a guard as hashed each conversation and read only at the task that needs it. The `.team` Director startup file's own read list changes too. | 3 | Same saving as C2, but it changes R9's November 2 rule for every project. **Not recommended now**; C2 gets the saving locally. |
| **D1. Fix the generic block (formal pattern)** | In the starter block: name the role package, say where the check is, say what 🎬 means and how often, within the 1,500-character budget. This is the subject of a separate block-rewrite request in this repo. | 1, for every project | One starter revision; the reader tests are its oracle. |
| **D2. A short video section (video system)** | In AGENTS.md outside the markers: where a stray note goes, when each folder applies, the fixed step reference and the folder rule. Pointers and purposes, not rules. | 1, the project-specific part | Small. It is a second place that can drift, so it stays short. |
| **E. One tracker and one role authority** | Retire `.team/START.md` and `.team/roles/director.md` as live Director authority. Fold the five catalogues into one (the 2026-11-07 Roster). Give the tracker one describing document. Settle the "first move" precedence with a dated supersession in `docs/DIRECTOR.md`. Resolve the model-per-role table's conflict with the no-fixed-model rule as Matt decides. Stop live role files reaching the legacy engine. Remove the dead `.director/` copy from the video system repo. | 2, part of 3 | Mostly editorial work in the video system repo. It needs B1 first, so that each change has one owner. Since no misuse was observed, its value is mainly lower reading volume and clarity. |
| **F. Compose at generation time** | The generator merges the video content and the stencil overlay when it creates a project. | 6 | **Not recommended.** It adds a third writer and new generator machinery, and the App Store build leaves the handoff out. |
| **G. Move the Director integration into the video system repo** | The video system owns the whole template and applies Director updates itself. | 6 | **Not recommended now.** It separates the video template from the stencil practice used for the brain and code templates. It would make the video system's maintainer review Director integrations, and it departs from R11's named staging route. Kept as a fallback if B1's split proves unworkable. |

The field evidence and the project's retro also suggested running the integrity check only at install and update time. Matt decided on November 7 to keep the check in every conversation. The receipt rewrite that argued for moving it happened on an older install, before the November 2 fix. This report does not propose reopening that decision, but it is listed for Matt (section 10). The remaining receipt gap is better closed by a cross-check in the ordinary check (section 9, row 8).

**Recommended route [proposal]:**

1. **Now.** Option A. Separately, the active generated project can take 3.1 through its own Director if Matt wants the SitRep and tier fixes there without waiting (R11).
2. **Next, one reviewed revision inside the template.** Options C2, B1 and D2, through the stencil and the video system.
3. **In this repo.** D1 in the separate block rewrite, plus a receipt-against-provenance cross-check in the ordinary check (a starter revision of the check helper). B2 only if the remaining AGENTS.md coupling proves costly.
4. **Then.** Option E, as the video system's follow-on work.

The resulting install route, end to end:

1. **Director Pattern source → stencil.** On every published `starter_revision`, the named stencil owner re-stages and reviews the overlay. The provenance records the revision and keeps only the bindings first use needs.
2. **Video system → template.** The publish writes everything except Director-owned paths, and refuses if asked to change one. A read-only stage plan after each publish reports any drift in a bound file.
3. **My Work → new project.** A copy plus the instance marker, nothing else. At creation the handoff already refuses on drift.
4. **The project's own Director.** It runs first use and every later update. Only those two routes write the receipt. No other session patches the project or tells it how to take in work.
5. **Standing text.** The generic block, within 1,500 characters and improved by D1 (later also carrying the 2026-11-07 re-entry marker), plus the short video section.
6. **First reply.** The block, START, the foundation, PROJECT, the video adapter, the check section and one check command. The video docs are read when a task needs them.

How this lines up with the 2026-11-07 proposals:

- **AGENTS block budget of 1,500 characters.** Kept. Today's block is 1,033 characters with markers. The video section sits outside it, with its own owner.
- **Core.** Kept, with two additions from the installation evidence. First, the template's Core carries exactly one check command, the project's own. Second, a Core on its own does not remove the 72 KB of mandatory reads local to the template; C2 does that in the template.
- **Roster.** Kept. It must absorb the template's five catalogues, or it becomes the sixth. Under B1 the video role rows are video-owned while the Roster is a `.director/` file, so who writes the video template's rows is open (section 9, row 5).
- **Re-entry marker.** Unchanged. The field's 0 of 5 re-entries after compaction is consistent with the earlier audit, though the samples partly overlap.
- **A November 7 hypothesis.** The triage guessed that the startup-check cost was local to the template. It proposed that the template state one exact command and keep setup-only manuals out of the ordinary guards. The evidence here supports both halves: the generic command gives a false gap, and the setup-only TEMPLATE file is an ordinary guard. **[fact]** C2 is that proposal, extended to the video docs.

## 9. Design-intent disposition sketch

This repository has a rule for replacing a default or onboarding route. Before the replacement, record each mechanism's owning decision, the failure it prevents, the new route and a concrete regression oracle. Any unknown or omitted obligation blocks acceptance. The table below is a sketch for a rationale author and an independent reviewer, not a finished disposition.

Every oracle that says "live" runs in a disposable fixture: a test copy of the template made through the video system's template-destination setting, plus a scratch generation. No oracle edits a real project.

| # | Mechanism changed | Owning decision | Failure it prevents | New route | Regression oracle | Blocking unknowns |
|---|---|---|---|---|---|---|
| 1 | First use binds seeded template files by hash, including the empty canonical seed, the guards it selects and the custom tracker contract | R16, later November 4 (bind generation without initialising the stencil; retain a semantically empty video seed); R9, later November 4; parity, November 4 (the video route keeps its backend and private rules) | A project initialises from an unreviewed or tampered integration, drift gets blessed, or a populated seed is taken for a pristine one | B1: keep every binding first use needs (hook file, selected guards, tracker contract files, the five empty placeholders, the reviewed journal and team seeds), drop the rest. A video-owned edit to a bound file goes through a stencil re-stage. B2 would need a new starter revision of the helper. | (a) A publish edits a now-unbound video doc; a fresh fixture generation completes first use. (b) Changing one byte in `.director/DIRECTOR.md`, or inside the block, makes first use refuse. (c) A pristine instance with the five empty placeholders completes first use. (d) One populated request or walk file makes first use refuse. (e) The custom tracker route still creates no bundled store. (f) The seed and malformed-provenance counter-cases still report honestly. (g) A pristine instance with the reviewed journal and team seeds completes first use; an extra or edited journal file makes it refuse. | **Blocking:** what reviews an unbound video doc that contradicts Director authority, now that first use no longer binds it. No replacement check exists yet. For B2 only: whether a helper change is acceptable for the brain and code templates. |
| 2 | Template update route | R11, November 7 item 1 (a template is updated only through its maintainer's reviewed staging route; a missing route is a gap) | Unreviewed outside edits leave the template looking current when it is not | Two documented routes with disjoint file sets, each naming the other's tool and files. The publish refuses Director-owned paths; it already excludes `.director/` and protects store-only role files, a precedent. A named stencil owner re-stages on each `starter_revision`. | A publish dry run with a changed Director-owned file refuses. A direct write into the store outside both routes (the 2026-11-07 case) is reported by the read-only stage plan run after each publish and before each creation. A new starter revision produces a re-stage plan. | **Blocking:** who the named stencil owner is (Matt), and whether the video system accepts a refusal rule. |
| 3 | The video docs are read completely before the first reply, as guards | R10, October 24/30 (required reads are reachable); R9, November 2 (selected guards are fully read, and conflicting surrounding authority prevents the badge); parity triage, November 7 (deferred the OPERATIONS split until the field's first minutes are measured, and proposed a static first-reply-trigger test first) | Guardrails go unread before acting; a badge is shown over conflicting authority | C2: the docs leave the ordinary guard list and become task reads. Remaining guards are still read completely. Conflict review of the docs moves to the stencil re-stage (row 1). One check command. | Static: a test pins the first-reply trigger prose in START, DIRECTOR and OPERATIONS before the guard list changes. Live, in the fixture:<br>• An unhinted greeting reads only the first-reply set, runs the check and shows 🎬.<br>• A one-line note keeps 🎬 and skips no required read.<br>• A withheld badge always names its gap.<br>• A production task reads PROCESS before dispatch.<br>• A render task reaches the private-upload guardrail before acting.<br>• After a forced compaction, the next production task re-reads PROCESS before dispatch, and the check reruns before the next 🎬.<br>• A planted contradiction in a doc is caught at re-stage. | **Blocking:** (1) the static trigger test does not exist yet; (2) whether four starts and two post-setup conversations, with no timings, meet the deferral's field condition; (3) whether moving conflict review of the docs to the re-stage keeps R9's November 2 rule that an unresolved conflict prevents the badge. |
| 4 | The standing block stays generic and managed | R10, October 23 (a small common bootstrap); R9, November 2 (one marked route, with the checker verifying the block's structure) | Project text inside the managed block breaks managed equality and mixes owners | The generic gaps are fixed in the starter block itself (D1, separate request). Project-specific gaps go in a short video section outside the markers (D2). | Re-run both reader tests outside this repository, on a generated video project and on a plain starter install. To pass, both readers locate the role package and the check, say what 🎬 means, give a home for stray notes in the video project, and estimate first-reply reading within a factor of two of the measured chain. The check still reports the hook structure as valid. | Whether the video section needs its own drift check. |
| 5 | Duplicate Director, START and catalogue files | R10, October 23 (a single active default and index); R16, October 25 (engine files are not live authority) | Legacy and team copies keep historical backend compatibility; removing them could break a caller | One Director definition, one START, one Roster and one tracker contract. Live role files stop reaching the legacy engine. Their owners retire the dead copies. | A search of live instruction text reaches exactly one Director definition and one START. The crew librarian's package does not reach the legacy engine. A reader asked "who defines the Director here?" gives one answer. | **Blocking:** whether the vendored tracker CLI or any crew action depends on legacy engine documents (not checked); who writes the video template's Roster rows. |
| 6 | Model-per-role table in `docs/DIRECTOR.md` | This repo's maintainer rule; the foundation's "no fixed model" rule; Matt's earlier choice to keep model-per-role tables local to his video projects | Frozen choices go stale and override per-task settings | As Matt decides: the tables stay, become tier words, or the foundation rule gives way locally | Whatever is chosen, the template states one rule, and dispatch records match it. | **Blocking:** Matt's decision. |
| 7 | Stencil provenance has no `starter_revision` | R11, November 7 item 3 | Updates cannot name the previous revision | The provenance records `starter_revision` at each re-stage | An update report names the previous revision, or says "unrecorded" | None known |
| 8 | Setup receipt baselines | R9, November 2, and its parity row (never rewrite a receipt to silence project drift); R11 (receipts change through the update route) | A Director certifies its own integrity, and 🎬 then asserts a check the Director rigged | Keep today's runtime rule: changed guards are reported, not blocking, and a receipt is never rewritten to silence drift. Add a read-only cross-check of the receipt's bound hashes against the template provenance to the ordinary check; first use already does this. | In the fixture: a Director edits a guarded doc; at the next greeting the check reports the changed snapshot, and the Director names it and leaves the receipt untouched. A receipt with a hand-edited bound hash fails the ordinary check. After the project's own reviewed update, the check still matches. | **Blocking:** whether the runtime rule holds is untested; the only incident ran without it. |
| 9 | Template's local-only privacy default and warning | R14, October 21 (tracked by default; keeping more local is the project's explicit later choice; one warning on a public or unknown remote) and later November 4 (setup records the warning as due rather than inventing delivery) | Exact sources reach a public remote's history; or a project loses continuity without knowing it | Preserved as today. B1 names the owner of the video adapter, which carries the privacy gate. | In the fixture: first use still verifies the ignore block and records the warning as due. A project with a public or unknown remote gets the one warning before its first capture. | **Blocking:** who owns the adapter (row 11); whether R14 accepts a template-made local choice (Matt); whether the warning is due for the examined project, which has no remote. |
| 10 | Daily update discovery | R11 (throttled discovery at the next active project-work step, independent of the greeting's local check) | A project silently runs a stale method, or pays network cost on a greeting | Preserved: the discovery triggers in DIRECTOR and PROJECT stay in the first-reply set under C2. | In the fixture: an unhinted greeting does no network discovery; the next project-work step runs the daily discovery. | None known |
| 11 | Owner of the video adapter and the other stencil-local files (PROJECT, TEMPLATE, TRACKER) | R16, October 25 (project-owned integration is separate from the replaceable engine) | A project-owned adapter is overwritten by a stencil update, or a stencil fix never reaches it | B1 states whether the stencil or the video system writes them. They carry the privacy gate and the tracker rule, so their owner reviews any change to either. | Both routes' documents name the same owner for these four files. A stage plan shows them as stencil-written, or the publish carries them, never both. | **Blocking:** Matt's choice of owner. |

This would touch these recorded decisions: the November 7 deferral on splitting the OPERATIONS installation section (row 3), and the November 4 binding decision (row 1). Each one either gets a dated supersession or stays in force. C2 leaves R9's November 2 guard rule unchanged.

## 10. Decisions reserved for Matt

*Decided 2026-11-08, evening: see "Plain summary and decided plan" above. The questions below stay as the record of what was open.*

1. Who should own the Director files in the video template: the Director Pattern stencil, as now, or the video system repo?
2. If the stencil, who is its named owner?
3. Who owns the video adapter and the other video-specific files in `.director/` (PROJECT, TEMPLATE, TRACKER)?
4. Creating a new video project today would most likely fail with a visible handoff error. Should the template be reconciled through the stencil's reviewed route before the next video, or should new video projects wait?
5. Should the active video project take 3.1 now, through its own Director, to get the SitRep and tier fixes?
6. Should the video docs come off the guard list, so that a Director reads them only when a task needs them and, with B1 dropping their bindings, editing them no longer blocks new projects?
7. If you would rather the video system's files stopped being hash-locked at first use altogether, that needs a change to the starter's first-use helper, which every template shares. Do you want that change?
8. Should the gaps the readers found in the standing block (role package, check, 🎬, reading cost) be fixed in the formal pattern's block, or in each video project's own section?
9. Do you want a short section in each video project's AGENTS.md, written by the video system, for the video-specific gaps?
10. Where should a note that is not about the video go, such as an errand?
11. You chose to keep model-per-role tables local to your video projects. Should they stay, become tier words, or should the foundation's no-fixed-model rule give way in video projects?
12. The template keeps requests, walks and journal out of Git for every video project. R14 expects that to be each project's own choice. Do you accept the template making it? Is the privacy warning due in the examined project, which has no remote?
13. Today's text says a Director never rewrites its receipt to silence drift. Keep that?
14. On November 7 you decided to keep the startup check in every conversation. Do you want to reopen that? The new evidence is the reading cost in video projects (section 3). The receipt rewrite happened on an older install that has since been fixed.
15. Should every new starter revision automatically trigger a stencil re-stage plan?
16. May the old v1 `.director/` copy be removed from the video system repo's template?

## 11. Evidence index

Listed by class of evidence only. The exact locations are kept privately.

- **Route map.**
  - A file-by-file SHA-256 comparison of 87 paths across the video system template, the live My Work template, the stencil overlay and a generated video project.
  - Read-only plan runs of the stencil staging helper and of the starter installer.
  - Code reading of the generator handoff, the first-use helper and the check helper.
  - Comparison with older video projects.
- **Startup trace.**
  - A line-numbered reading of every instruction file on the startup chain, in a generated video project and in the live template.
  - Byte counts for four cases, using the project's own context checker.
  - A read-only run of the project's check.
- **Reader tests.** Two cold readers, one on the strongest tier at default effort and one on the middle tier with high effort requested. Each read only a generated project's AGENTS.md. Answers were transcribed close to the original.
- **Field evidence.**
  - Read-only extraction from session transcripts in two video projects: Project Director starts, scoped child Directors, compactions and subagent transcripts.
  - Baselines: one starter-2 conversation and one v1-era project.
  - Request records.
  - The project's own 2026-11-07 retro findings.
- **Author re-checks, 2026-11-08, all read-only.** The live template's managed hashes compared against its provenance; the first-use helper's refusal on drift, in its code; the modification times of the changed files.
- **Independent review, 2026-11-08, all read-only.** A re-hash of the live template, a plan-only staging run, code reading of the first-use helper, both check helpers, the handoff and the installer, file times and commit history in the video system repo, a string check of the installed My Work binary, and spot extraction over four field transcripts.
- **Design context.**
  - The 2026-11-07 startup-architecture report.
  - Rationale decisions R9 (November 2 and later November 4), R10 (October 23, November 1 and 4), R11 (November 7 and earlier template clauses), R14 (October 21 and later November 4) and R16 (October 25 and later November 4).
  - Behaviour-parity rows for:
    - the November 7 field triage;
    - November 4 generated first use;
    - November 2 composed project guidance;
    - the installation, privacy and update mechanisms.
