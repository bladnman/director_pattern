# Where the Director Pattern should live after compaction

> **2026-11-10 clarification:** [Startup route clarification](clarity-20261110/report.md) separates the current local route, public starter, and scratch candidate; records the action-card triggers and reachability gaps; and adds later compaction observations. It also narrows the older summary's claim about what hosts retain after compaction.

> 2026-11-09 update: a follow-on proposal for a "Director slug" in AGENTS.md is in [brief.md](brief.md) and [slug-draft.md](slug-draft.md). It is a proposal; nothing below was changed by it.

Scale, surfaces, and a proposed architecture. Investigation of 2026-11-07 in the Director Pattern source project. Distilled from four bounded investigations (a scale audit of the startup chain, a Claude Code documentation pass, a cross-host documentation pass, a digest of the two sibling research notes), the sibling session's catch-up brief, and one independent adversarial review whose corrections are folded in and marked. Facts carry their source class. Design claims are **[proposal]** or **[hypothesis]**. Where the reviewer overturned a draft claim, the row says so.

## 1. Short answer

1. **We are not in the wrong surface. We are in the wrong layer.** Plain instruction files plus a root `AGENTS.md` block remain the only portable surface across hosts. The failure is that the pattern treats a one-time tool read (START, DIRECTOR, OPERATIONS) as if it were standing context. Every host keeps a small standing layer across compaction (system prompt, root instruction file, some hook output) and discards everything that arrived through tool reads. The pattern puts about 1 KB in the standing layer and about 43 KB in the layer that is discarded.
2. **Skills do not fix this.** Only Claude Code re-injects an invoked skill's body after compaction, capped at 5,000 tokens per skill. No other host documents it, and a Codex community report says it is lost there. Skills also bring the auto-discovery and distribution problems Matt already objects to. The `.agents/skills/` folder is a plausible future shell for executor craft manuals, not for Director authority.
3. **Plugins are packaging, not persistence.** The only plugin component that helps is a hook, and the Agent Plugins 1.0 standard excludes hooks from portability (per the cross-host researcher's reading of the announcement). A project-local hook file does the same job with no marketplace, no install step and no plugin.
4. **Hooks are the one mechanism that re-injects after compaction, in exactly two hosts** (Claude Code and Codex, both via a session-start hook with a `compact` source). Other hosts inject at session start or per turn but not after compaction. Hooks are a per-host accelerator, never the method, and this public repository cannot carry them in committed settings because `.director/` is ignored in every clone.
5. **The scale is 43 to 50 KB (10.7k to 12.5k tokens), five files plus one section, about 100 distinct obligations, of which about 12 apply on every turn.** Word-for-word duplication is only 1%. The same rules restated in other words are 12 to 13%. A third of all sentences are negations or disclaimers.
6. **Proposed shape: a hand-written Core under a hard budget, a Roster with tier words, Manuals the Director never reads unless they are its own craft, a tiny ignored continuation State, mechanical re-entry (an end marker the model searches for, not a self-assessment), store-enforced dispatch fields, and optional per-host adapters trialled locally first.** Target: about 18 KB across five small files instead of 43 to 50 KB across six places. The reviewer showed a Core of about 7,900 characters is achievable.
7. **Not ready to ship as architecture.** Before any of it lands, the repo's own rule applies: an obligation-by-obligation disposition against the design-obligation matrix, plus dated supersessions for three recorded deferrals this would override. Section 8 lists them. The stopgap in section 10 step 1 does not need the architecture and should go first.

## 2. What we measured

### 2.1 Required reads before a fresh Project Director's first reply

| Layout | Unambiguously required | If the agent reads whole files (it usually does) | Files |
|---|---|---|---|
| Live install in this checkout (revision 3.0) | 42.8 KB, about 10.7k tokens | 50.0 KB, about 12.5k tokens | AGENTS, START, DIRECTOR, PROJECT, CAPABILITY_POLICY, OPERATIONS section, check output |
| Starter payload for a new project (revision 3.1) | 29.4 KB, about 7.4k tokens | 37.3 KB, about 9.3k tokens | bridge block, START, DIRECTOR, OPERATIONS section, check output |
| v1 engine, reply only | 26.9 KB | 97 KB with badge, 125 KB with staffing | 6 files, 4 serial stages |
| Explicit worker (pattern-author) | 24.1 KB | 28.2 KB with ROLE_INDEX | 6 files |

In this repository an ordinary task then adds README plus rationale decisions: 10 to 40 KB more, from a 212 KB RATIONALE whose largest decision is 35 KB. The installer's own `plan` reports 20 KB for the Director chain, omitting the OPERATIONS section START makes mandatory, so it understates by about 38%. **[fact, scale audit]**

### 2.2 What the chain is made of

| Measure | Value |
|---|---|
| Distinct obligations imposed on a Director | about 100 |
| Of those, every-turn invariants | about 12 (badge, ❓, 🖐️, delegate, stay available, SitRep check, continue to completion, emoji names, explicit tier and effort, mechanism mapping, host formats, recheck when stale) |
| Verbatim duplication across files | about 1% |
| Same rule restated in other words | 12 to 13% (badge theme alone: 31 sentences in 5 files) |
| Sentences containing a negation or disclaimer | 34% (23 "does not prove" clauses, 12 of them in OPERATIONS) |
| OPERATIONS installation-evidence section | 7.8 KB, mostly receipt formats and hook variants that are irrelevant once the check passes |
| Runtime rules that mention compaction | one (SitRep timing) |
| Host hook mechanisms used by the pattern | none; "hook" in this repo means the marked prose block in AGENTS.md |

Two regressions surfaced on the way: the flat starter dropped v1's explicit "reload no-longer-retained instructions" clause with no recorded decision, and this checkout's live install lags the 3.1 payload (no explicit tier/effort rule, no partner rule) although its receipt says DIRECTOR equals the payload, which is true only at f4f3ef0. **[fact, scale audit]**

### 2.3 What happens at compaction (sibling evidence, not re-derived here)

- 21 compactions across 9 Director sessions in 7 projects: none followed by a complete re-read of START plus role plus OPERATIONS. Dispatching resumed 1 to 5 minutes later. The 🎬 badge continued in about 13 segments and lapsed in others. **[fact, sibling audit]**
- The host re-injected the instructions attachment (CLAUDE.md files and the AGENTS.md block) plus a few recently used files; in the audited session that was PROJECT.md and two scratch notes, never START, DIRECTOR or OPERATIONS. The 12.9k-character summary said the files were "read" and that "every reply carries 🎬", with zero rule text. **[fact, sibling audit]**
- Why nothing re-reads: the surviving AGENTS.md trigger says "before the first ordinary reply in each conversation", and a compacted session is the same conversation. START and DIRECTOR say "reuse unchanged retained instructions", which after compaction points the wrong way. **[fact]**
- Request capture-before-work fell from about 74% to about 53% after compaction; uncaptured requests went from 3 of 19 to 17 of 59; in one project seven asks were folded into one request. The sibling notes label these approximate, from a small sample, and the recorder comparison comes from a different v1 project. The reading that memory-resident duties degrade at compaction is **the sibling's own hypothesis, not a fact** (reviewer correction). **[hypothesis, sibling §J]**
- Standing host text ("never on your own judgment", "when in doubt, don't spawn", "do exactly that") appears to beat pattern text read once. This is the sibling conflict map's **interpretation**, consistent with transcripts, not a measured fact (reviewer correction). **[hypothesis, sibling §D]**
- Settings were ignored even with the staffing text fully in context (first 5 dispatches). Relocating text does not fix that case; explicit per-dispatch settings plus enforcement do (reviewer correction, sibling §A1). **[fact]**

## 3. What survives compaction, by host

Three layers exist in every host, with different persistence. **[fact, both surface investigations, documentation unless marked]**

| Layer | What lives there | Survives compaction? |
|---|---|---|
| L0 standing | system prompt, root instruction file (CLAUDE.md / AGENTS.md / always-on `.cursor/rules` / GEMINI.md), skill name and description lines, auto-memory, output of compact-source hooks | Yes, by construction; re-sent each turn or re-injected from disk |
| L1 loaded | file contents read with tools, skill bodies, hook output from earlier in the session, subagent instructions | No. Claude Code re-reads up to five recently used files under 5,000 tokens and re-injects invoked skill bodies (5,000 per skill, 25,000 total). Elsewhere: gone, replaced by a summary sentence |
| L2 reference | manuals, rationale, history | Not expected to survive; read on demand |

Per host:

| Host | Root file re-injected | Post-compaction injection hook | Per-turn injection hook | Skill body survives | `.agents/skills` | Reads `.claude/settings.json` hooks |
|---|---|---|---|---|---|---|
| Claude Code | project-root CLAUDE.md; AGENTS.md is read in its place when no CLAUDE.md exists (docs); this session shows both a home CLAUDE.md and the project AGENTS.md loaded, so the exact rule needs a dated check | SessionStart with sources `startup`, `resume`, `clear`, `compact`, `fork`; 10,000 characters per hook string | UserPromptSubmit can add context (reviewer; verify against the hooks reference) | yes, capped | not documented | native |
| Codex | AGENTS.md re-sent as turn context (community, maintainer thread; whether re-read from disk each turn is a different claim) | SessionStart `source: compact`, `additionalContext` | UserPromptSubmit `additionalContext` | no (community) | yes | reads Claude marketplace and plugin formats |
| Cursor | always-on rules and root or nested AGENTS.md (staff: "system prompt plus summary") | none (preCompact shows a message only) | none that injects | undocumented | yes | with third-party hooks enabled |
| Copilot CLI | instruction files and AGENTS.md; custom-agent instructions dropped after compaction (open issue) | none (preCompact is notification only) | none | undocumented | yes | yes (per the cross-host researcher) |
| Gemini CLI / Antigravity | context files "sent with every prompt" | PreCompress exists; injection unclear | BeforeAgent can add context | undocumented | yes | no |
| Amp | AGENTS.md; re-inclusion not stated | none | `agent.start` can append a hidden message each turn | undocumented | yes | no |
| Cline | rules and AGENTS.md; re-application not stated | PreCompact with `contextModification` (extension) | UserPromptSubmit / beforeRun | undocumented | `.claude/skills` only | no |

Standards: the Agent Skills specification has no field to stop auto-invocation; each host adds its own. Agent Plugins 1.0 covers skills and MCP servers only. Several host facts in this table were collected by the two researchers from vendor documentation on 2026-11-07 and were not independently re-verified by the reviewer, who asked for dated primary quotes before any of them carries design weight: SessionStart `fork`, PreCompact stdout as summary instructions, the 1,536-character description limit, Copilot reading `.claude/settings.json`, and the plugin standard's hook exclusion.

## 4. Matt's questions, answered

**Does this need to be a skill? Do skills get reread after compaction for free?** Only in Claude Code, only when the skill was invoked, and capped. The description line is standing context everywhere, which suits a one-line re-entry trigger but not authority. Skills are auto-listed to any actor holding the Skill tool, so workers would see the Director's skill and every role's skill. Verdict: not for the Director core. Possibly later for executor craft manuals, where discovery is harmless and progressive disclosure is wanted.

**Plugins versus skills; do plugins reload after compaction?** A plugin is a bundle. Nothing about being a plugin survives compaction; only a hook inside it would, and plugin hooks are vendor-specific. Verdict: no plugin.

**Would literal hooks help?** Yes, materially, in the two hosts we actually run (Claude Code and Codex). But: this repository is public and `.director/` is ignored, so a committed hook that reads `.director/CORE.md` fails in every clone and worktree; hooks must be trialled in `.claude/settings.local.json` only. Settings files need a structural merge, not a marked block. Whether the host trusted and loaded a hook is unobservable to the installer, so a receipt may record "emitted", never "active". A Director Core injected at session start into a session that turns out to be a worker is pollution in reverse, so injection has to be gated (section 6.7). Per-turn injection of 15 KB on Codex would fill a 200k window in about 50 turns; per-turn text must stay under about 400 characters. All reviewer corrections.

**Are we in the wrong surface area?** No. Files are the only portable surface, and the root `AGENTS.md` block is the only portable standing text. What must change is which obligations live in standing text, which live in a re-enterable Core, and which live in manuals the Director never reads.

**How big are we, and how many files does a new Director read?** Section 2. Five files plus a section, 43 to 50 KB. The proposal brings re-entry to one file under 10,000 characters and startup to about 18 KB across five small files.

**Could a single START be the thing that is reread?** Almost. The reread target should be one file under a hard budget (the Core). The re-entry trigger must live in the AGENTS.md block, because the trigger must survive compaction and the Core cannot carry its own trigger. START today is 5 KB of read discipline and routing that tells the agent to read 12 more things.

**Compile step?** Not now (reviewer, adopted). A fragment compiler creates a second source of truth beside pinned payload text, and an installed project that edited DIRECTOR.md would have no per-file base for the three-way merge UPDATES uses. The Core also carries the install-specific check command and marker, so it is per-install output anyway. Instead: hand-write CORE.md as a managed file, ship a provenance sidecar mapping each Core line to the file and paragraph it replaced so UPDATES can carry old local diffs over, and route project adaptations to PROJECT.md or a budgeted overlay. Revisit a compiler only if the Core proves hard to keep consistent by hand.

## 5. Diagnosis

1. **Authority is allocated to the wrong layer.** About 1 KB standing, about 43 KB loaded. After compaction the loaded layer becomes "a summary says you read it", which is worse than nothing because the badge keeps asserting a state that no longer exists.
2. **The pattern's proof model is "a read happened".** Hashes, complete-read discipline, truncation recovery and the check all establish that a read happened at time T. Nothing establishes that the text is in context at time T plus n. The badge is defined as the former and consumed as the latter.
3. **Reads done through the shell may be invisible to the host's restore.** Claude Code restores "recently used files", and the one restored file in the audited session was one read with the Read tool. Under bypass-permissions mode this host asks for shell reads (`cat`, `sed` ranges), which the restore likely does not see. This would explain why START, DIRECTOR and OPERATIONS were never restored while PROJECT.md was. **[hypothesis, reviewer; cheap to test with `/context` after a forced compaction]**
4. **Host standing text wins ties on delegation; on settings the host condition is satisfiable.** The Agent tool accepts effort "when instructions such as CLAUDE.md or a skill explicitly ask for a specific level". Text read once counts if present at dispatch; 3.1 already names a level. The real problem is that the text is not present after compaction, not its wording (reviewer correction to the draft's diagnosis).
5. **Judgment-shaped duties slip; form-shaped duties hold.** After compaction the request stores stayed valid and the helper's required flags kept records well-formed, while the judgments (capture before work, split independent asks) slipped. Whatever the helper enforces survives; whatever memory enforces does not. **[hypothesis consistent with sibling §J]**
6. **The reread chain is too long to be re-entered under pressure.** Even a Director that notices it should reread faces 43 to 50 KB in six places with ordering rules. Re-entry must be one file, one command, one mechanical test.

## 6. Proposed architecture

**[proposal]** Parts by persistence layer. Everything here is subject to the disposition in section 8.

### 6.1 Budgets

| Artifact | Layer | Hard limit | Target | Why |
|---|---|---|---|---|
| AGENTS.md block (bridge) | L0 standing, portable | 1,500 chars | 1,250 | Small fraction of a root file that hosts advise keeping under 200 lines; the reviewer's full block is 1,243 chars |
| `.director/CORE.md` | L1, re-entered | 10,000 chars | 8,000 | Claude Code hook string cap; under the 5,000-token re-read cap. Reviewer's tight draft: about 7,900 chars including invariants (3,096), recovery list (729), role preamble, check command, dispatch packet, size test, state commands, evaluation, action triggers, end marker |
| `.director/ROSTER.md` | L1, re-entered | 4,000 chars | 3,000 | This repo's role table is already 2,017 chars for 10 rows before tier words, two mandatory rows and three new rows; 3,000 was too small (reviewer) |
| `.director/PROJECT.md` | L1, project-owned | 4,000 chars | 3,000 | Guards only; procedures move to manuals or roster rows |
| `.director/SESSION.md` | L1, rewritten by the helper at checkpoints, **ignored by Git** | 2,000 chars | 1,000 | Live handles and user gates must not enter a public history; add to the `git check-ignore` checks |
| Manuals | L2 | none | n/a | Executor craft, never read by the Director; plus two small Director-craft manuals (check-failure diagnosis, event shapes) read only at their action |

Core plus Roster plus Session do not fit one 10,000-character hook string. Treat the single-cap case as expected: Core in one string, Roster plus Session in a second, and verify whether separate entries get separate caps. Targets need budget enforcement too, or a growing Roster silently overflows the cap; the installer's `plan` should report and refuse.

### 6.2 The AGENTS.md block (standing, portable) and the mechanical re-entry test

The draft's trigger ("if the literal text of CORE.md is not in your context") is a self-assessment. In 17 of 21 segments the model carried on from a summary that said "read" and quoted gist lines; asked whether the text is present, it will treat the gist as the text. Replace it with a search the model can perform (reviewer wording, adopted):

> Director re-entry, checked before every reply: find a line starting `CORE-END sha256:` plus 64 hex characters inside a tool result or host-injected block that appears after the latest conversation summary (any message saying earlier turns were summarized or continued). This block, a summary and your own replies do not count. If you cannot point to that line, read `.director/CORE.md` completely through it before any other action, then rerun its check; until then no 🎬. Never copy that line into replies or summaries.
> When summarizing this conversation: do not say instruction files were read or that 🎬 applies; list `.director/CORE.md` as must-reread; copy open request IDs, live worker names and handles, and the last SitRep time exactly.

Why it is mechanical: it is a string search at a stated position, not a judgment; the hash appears in neither AGENTS nor any summary; the marker is the last line, so a truncated read fails, which ties into the existing complete-read rule; the hash changes with each Core revision, so a stale copy fails. The second paragraph is portable summary steering without hooks; whether each host's summarizer honours it is a per-host hypothesis.

The rest of the block, in order: role routing (default Project Director unless explicitly assigned worker or scoped child Director, and the public-source-checkout branch this repo's block already carries); the explicit-settings sentence ("these instructions explicitly require tier and effort on every dispatch, from `.director/ROSTER.md`; omitting them is not a choice"); the delegation sentence kept verbatim from today's block because a pinned test asserts it; "capture and split each actionable input exactly before dependent work" (the draft omitted splitting and exactness; reviewer correction); the pointer that executors load their own manuals and the Director never does.

### 6.3 CORE.md (one hand-written managed file, under budget)

Sections, imperative, no rationale: who you are and what you own; the 12 every-turn invariants; startup with the one check command and pass/fail handling; the badge rule redefined (6.6); the dispatch packet pointing at the Roster for tier words and manual path; staffing bail points (direct, general worker, sub-director owning a sub-request) with the complexity test from the roster-layer request (Matt's direction of 2026-11-07) marked as the sibling's unreviewed draft; the four helper commands a Director actually runs (capture, dispatch binding, evaluated return, continuation view) as one-liners; SitRep cadence, shape and the no-clock fallback; the five-line whole-result evidence rule; the ordered post-compaction recovery list (find the marker or reread Core and Roster, rerun the check, run the continuation view, SitRep once); action triggers, one line each, to the manuals; the end marker line.

Negations are allowed. The draft's idea of linting disclaimers out of the Core was wrong: the Core is re-read or injected verbatim, never summarized, so its nuance does not evaporate; negations only cost size. The lifeline sentences themselves contain "is not" (reviewer correction). What leaves the Core: receipt format variants, hook-structure variants, backend-contract options, context-budget preflight, continuity and privacy procedure, learning threshold mechanics, update discovery procedure, My Work stencil procedure. Each of those must land on a named owner (section 6.4) or a Director-craft manual with a Core trigger line, never on a bare link. BEHAVIOR_PARITY case 2 already records a guide whose Director trigger was dropped while its files stayed; that is the failure to avoid.

### 6.4 ROSTER.md

One table: role ID, assignment role (worker or director), when to pick it, suggested tier **word** and effort word (never a model name or alias; the host handle is resolved at dispatch, as AGENTS.md and DIRECTOR already require), manual path, owner and route constraints. Per-role words are a starting suggestion; the per-task choice (strong tier at high effort by default, lighter only with very high confidence) stays, so effort is not frozen per role (reviewer correction). Rows: the existing ten; `general-worker` with the caution that it never silently substitutes for a maintained specialty; `sub-director` as an alias of `request-manager` so old assignments resolve (caller-ID rule); and three rows that take over procedures leaving the Core: `privacy-notice` (first-capture notice, R14), `learning-review` (the three-incident review, R18) and `update-owner` (daily discovery and update planning, R11). Selection and authority facts stay in the row; the Director reads rows, not manuals. Workers do not read the Roster, but the every-role guards ROLE_INDEX carries today (no push or deploy without Matt, keep the private reference folder private) move into the assignment packet so they are not lost.

### 6.5 SESSION.md and continuation

The helper already has a continuation view. At every checkpoint write it also emits `.director/SESSION.md`: role, open request IDs with owners, live dispatches with handles and emoji names, last SitRep time, pending user gates. Inject it at SessionStart `compact`, not PreCompact: idle compaction in the audited session wrote the summary at 22:42 and applied it at 00:04, so PreCompact-captured state can be 80 minutes stale (reviewer). The draft's hope that a checkpoint-written file lands in Claude Code's five restored files is weak: a file written by a Python helper through Bash is probably not in the Read tool's restore set. **[hypothesis, test with `/context`]**

### 6.6 Badge redefinition and oracles

🎬 means: the Core end marker is present after the latest summary and the check passed in this context segment. After compaction the badge drops until re-entry.

Primary oracle (reviewer, adopted): a transcript scanner that, after each `compact_boundary`, requires a complete Core read (or injection) plus the check before the first Agent call or the first 🎬. Run it over the 21 audited segments as the baseline, then over every trial. Add the capture and split rate across the boundary. The draft's static canary tests recall, not spontaneous re-entry, and a static value can ride in the summary; if a canary is used at all it is a nonce that changes on every injection or check run.

### 6.7 Host adapters (optional, trialled locally, never required)

| Host | Adapter | Gate | Notes |
|---|---|---|---|
| Claude Code | `settings.local.json` first: SessionStart (`startup`, `resume`, `clear`, `compact`, `fork`) injects Core in one string and Roster plus Session in another; PreCompact prints the summary-steering paragraph | Inject only when the session is a Director: the hook checks a role marker (an assignment file or environment the dispatcher sets for workers) and otherwise prints nothing | Avoids worker pollution and double injection on resume, where the transcript already holds the Core |
| Claude Code, stronger (reviewer mechanism A) | PreToolUse on the Agent tool, plus UserPromptSubmit, reads `transcript_path`, finds the last `compact_boundary`, looks for the Core end marker after it; missing: deny the dispatch with "read CORE.md first", or inject only then | Same | Fixes double injection and cost; the same scanner is the offline oracle; extends `development/prototypes/stop_guard.py`, which already exists unactivated |
| Codex | hooks file with SessionStart `source: compact`; UserPromptSubmit limited to a 400-character pointer, not the Core | Same role gate | Per-turn 15 KB would fill a window in about 50 turns |
| Copilot CLI | reads `.claude/settings.json` hooks; sessionStart injects | Same | Session start only; relies on the re-entry rule afterwards |
| Cursor | always-on rule containing the block text | n/a | A second copy that can drift and that the checker never sees; prefer the AGENTS.md root support Cursor already has |
| Any other | AGENTS.md block only | n/a | The re-entry rule carries the method |

Installer emission of adapters is deferred (reviewer; and a Nov 4 decision records "no enabled host config, no default activation"). Trial by hand first.

### 6.8 Store-enforced duties and the per-call footer (reviewer mechanism B, adopted)

Make the dispatch-binding event require tier word, effort word, one-line reason, independent reviewer (or an explicit "none required" with the rule that permits it), and parent and requirement IDs. The helper refuses otherwise. Have every helper call print a footer of at most 300 characters: SitRep due time, held streams, the current Core marker, and an uncaptured-input hint. Text a tool prints on every call is the one Director-facing text that returns after compaction on every host, with no hook. This is the portable half of the design and may matter more than the hooks.

### 6.9 Clear-and-resume instead of compaction (reviewer mechanism C, adopted as an option)

Near the context limit, at a checkpoint, the Director offers a 🖐️ step: start a new session, then say "resume". The cold-start first-reply route is the one route with tests behind it; the continuation view plus a handoff file carries state across, turning an untested re-entry into a tested startup. Where a host supports it, `idleCompaction: false` removes the idle case only (Matt's call, sibling).

### 6.10 Roles as system-prompt-resident actors

In Claude Code a custom agent's body is the subagent's system prompt and survives the subagent's own compaction; subagents cannot see each other's definitions. The draft proposed emitting `.claude/agents/<role>.md` from manuals. Deferred: it would put a concrete model alias in an enduring payload file, which AGENTS.md forbids, and it brings back the auto-listing that section 4 rejected for skills. If a project wants it, the files stay project-local with tier words resolved at dispatch, outside the payload.

## 7. What this changes in existing text

| Existing text or decision | Change | Reason |
|---|---|---|
| START and WORKER "reuse unchanged retained instructions"; DIRECTOR "reuse unchanged current-conversation evidence" | Replace with the end-marker re-entry rule | Points the wrong way after compaction |
| v1 "reload no-longer-retained instructions" (dropped in the flat starter without a decision) | Restore, strengthened, in the AGENTS block | Undocumented regression |
| AGENTS block trigger "before the first ordinary reply in each conversation" | Trigger becomes the marker search before every reply | A compacted session is the same conversation |
| 🎬 means "check passed earlier" | 🎬 means "marker present after the latest summary and check passed in this segment" | Badge was false evidence in 18 replies |
| 3.1 "read UPDATES completely before planning an update" | **Left undecided.** The sibling's open item says it conflicts with the anti-pollution rule; the draft wrongly settled it. The `update-owner` roster row is one resolution; Matt decides | Owner decision |
| OPERATIONS installation-evidence section (7.8 KB) | Command plus badge rule to Core; formats and variants to a Director-craft manual read when the check fails. **Blocked** until the Nov 7 deferral (measure the field's first-minutes sequence; pin the first-reply trigger in a static test) is superseded or satisfied | Recorded deferral |
| ROLE_INDEX | Becomes ROSTER (6.4) | The roster-layer request (Matt's direction of 2026-11-07) |
| R18 record keeping on the Director | Keep the duty; move persistence to SESSION.md plus store-enforced fields and the capture-and-split line in standing text; the recorder stays optional | Sibling §J hypothesis; the fix does not depend on it being true |
| Model and effort | Roster tier words; standing text requires them per dispatch; helper refuses dispatch records without them | Settings were ignored even with text in context |
| Worker reads ROLE_INDEX? | Workers never read the Roster; every-role guards travel in the assignment | Resolves the contradiction toward less reading |
| `startup_check.py`, receipts, `test_package.py` | Checker must accept a hook that names CORE; managed-artifact set changes; the pinned test that requires exactly one locator and the verbatim delegation sentence must be updated in the same revision; the two-branch block (adopted versus public checkout) must be preserved | The draft would have broken all three silently (reviewer) |

## 8. What blocks acceptance

The repo's AGENTS.md requires a design-intent disposition for any refactor or replaced default route: for each mechanism, its owning decision, the failure it prevented, the new active route and a concrete regression oracle, with unknowns acceptance-blocking. The draft did not supply it. These obligations have no disposition yet:

- The author of a substantive change cannot supply its independent review (OPERATIONS).
- Task-time knowledge selectors paged with `canonical_learning.py` and passed as exact tags to workers (START).
- Generated-project first-use before the check (Nov 4 row).
- Privacy notice at first source capture (R14).
- Daily update discovery (R11).
- Three-incident learning review and touched-knowledge upkeep at closure (R18).
- Steering by expected revision to the same owner (R17).
- Caller-ID and alias preservation (START).
- Source-subset limit for external routes (DIRECTOR).

Recorded deferrals this would override, each needing a dated supersession or staying deferred: splitting the OPERATIONS installation section before the first-minutes measurement (Nov 7); no enabled host config and no default activation (Nov 4); the continuation API left deliberately unchanged, no new recovery API (Nov 4; SESSION.md is one).

The next concrete step is therefore a disposition table with one row per obligation in BEHAVIOR_PARITY's "why each mechanism existed" plus the Nov 4 and Nov 7 rows, each with the new route, its Core trigger line or roster row, and its oracle. That is bounded work for a rationale-author worker, not a Director.

## 9. Hypotheses and open questions

- **[hypothesis]** An 8,000-character Core preserves behavior. Test: the obligation-inventory test plus the transcript oracle.
- **[hypothesis]** Standing text can beat the host's per-turn counter-text on delegation. Needs the live trial with a deliberately tempting small task.
- **[hypothesis]** Shell reads are invisible to the host's file restore (5.3). Test with `/context` after a forced compaction, once with Read-tool reads and once with `cat`.
- **[hypothesis]** Each hook entry gets its own 10,000-character cap. If not, the Core target drops to about 6,000.
- **[open]** Whether UPDATES at update-planning time is Director craft or pollution (Matt).
- **[open]** Whether "Director craft manuals" (check-failure diagnosis, event shapes) are compatible with the anti-pollution rule, or whether those too need roster owners (Matt).
- **[open]** Worker compaction: a worker reading its manual loses it the same way; the portable fallback is the same marker rule in a WORKER core.
- **[open]** Stability of Codex re-sending AGENTS.md each turn (community source).
- **[retracted, stays retracted]** S3 "Director reads every procedure it routes"; the Roster plus manuals design is the replacement.

## 10. Sequence

1. **Stopgap, one revision, no architecture change.** In the AGENTS block generated by `install.py`: the end-marker re-entry paragraph (with a temporary marker line appended to today's DIRECTOR.md), the summary-steering sentence, the explicit-settings sentence and the capture-and-split sentence; keep the pinned delegation sentence verbatim; update `startup_check.py`, the receipt baseline and `test_package.py` in the same change; bring this checkout's own install up to 3.1. Oracle: the transcript scanner over a forced compaction in this repo.
2. **Local hook trial, this machine only, `settings.local.json`.** A hand-written Core under 9,000 characters ending in the marker; SessionStart compact injection; PreCompact steering; the transcript scanner as the pass test. The draft's version (inject DIRECTOR plus START, 18,285 bytes) could not fit the cap and would have tested truncation.
3. **Disposition table** (section 8) by a rationale-author worker, independently reviewed. Nothing in steps 4 to 6 lands before it.
4. **Core, Roster, helper enforcement, footer.** Hand-written Core with provenance sidecar; ROSTER with the new rows; dispatch-binding event requires the fields; per-call footer. Oracles: budget tests, inventory test, transcript scanner, capture and split rate.
5. **Adapters by hand per host we run**, gated on role; installer emission only after a dated supersession of the Nov 4 decision. Oracles: a worker session's transcript shows no Director Core injected; the transcript scanner passes across a forced compaction in a Director session with the adapter on.
6. **Later, optional:** project-local agent files; `.agents/skills/` for executor manuals; a compiler only if the hand-written Core proves hard to keep consistent. Oracles: a worker compaction trial (the worker still follows its manual after its own compaction); for a compiler, byte-identical output against the hand-written Core before it replaces anything.

## 11. Evidence index

- Scale audit: two scratch scripts (duplication and theme restatement), not published; figures in section 2.
- Claude Code documentation (as read by the guide researcher on 2026-11-07): context-window "what survives compaction" table; hooks reference (SessionStart sources, 10,000-character cap, PreCompact stdout as summary instructions); skills (re-injection caps); sub-agents (body is system prompt, independent compaction); memory (200-line guidance).
- Cross-host documentation (as read on 2026-11-07): Codex AGENTS.md, skills, hooks and subagents pages and maintainer thread 21269; Cursor rules, hooks, skills, plugins; Copilot CLI hooks reference and issue 2895; Gemini CLI context and hooks; Antigravity plugins; Amp plugins and news; Cline hooks and skills; Devin rules; agentskills.io specification; Agent Plugins 1.0 announcement.
- Sibling research (private project notes, 2026-11-07): the staffing-settings audit (compaction audit, conflict map, re-load wording, Matt's roster direction) and the single-thread stall triage; the three pending requests of the same day (roster layer, Tinka research reports, rollout); the public distillation on the sibling board `research-2026-11-07-staffing-stewardship`.
- Independent review: a strongest-tier reviewer at extra-high effort read the draft against AGENTS.md, START, DIRECTOR, OPERATIONS, ROLE_INDEX, the installer bridge, the rationale overview and maintenance section, and BEHAVIOR_PARITY headings; 17 findings and 3 proposed mechanisms, all incorporated or recorded above.
- Pattern text cited: `.director/START.md:69`, `.director/DIRECTOR.md:13-14,129`, `.director/OPERATIONS.md:66-85,178,185`, `pattern/engine/PATTERN.md:78-79`, `pattern/starter/install.py` BRIDGE, `development/STARTUP_LOADING.md`, `.director/context_check.py`, `development/prototypes/stop_guard.py`, `.gitignore:58`.
