# Flat Director starter 3 — preserved records, fewer compulsory actors

One Project Director stays in conversation, delegates useful bounded work and
retains whole delivery. No mandatory manager, Recorder, identity-pool, setup-check
or learning actor. Flat orchestration does not remove exact source/record/lifecycle,
verification, update, supervision or project-authority obligations.

**Starter 3 is the current source correction candidate**, not a release tag or an
installation in other projects. Its `director-request-bundles` backend is incompatible
with starter-2 state.json; read the [unsupported-2 recovery notice](unsupported-v2.md)
before recovering that format. Existing mature trackers remain canonical and need
reviewed instruction/adapter integration, not a fresh installer or second ledger.
The [design-obligation matrix](https://github.com/bladnman/director_pattern/blob/main/development/BEHAVIOR_PARITY.md) explains the
old reasons, revised routes, evidence and remaining verification limits.

The manifest's `starter_revision` (now 3.3) is a readable revision number bumped with
each published payload change; `starter_version` stays the install-format number.

Revision 3.3 changes where the Director's rules live. The installer writes a marked
Director block of about 7.5 KB into the project's AGENTS.md, followed by a
project-owned settings section. The block holds the role gate, the ten standing
duties, the first-reply check, the recovery steps and the reading rule, because hosts
restore AGENTS.md after a compaction and do not restore files an agent read. Detail
sits on seven cards in `.director/cards/`, each read before the action the block's
table names. START.md and DIRECTOR.md remain only as redirect stubs. The block's
source is [agents/block.md](agents/block.md) and the section's is
[agents/project-section.md](agents/project-section.md); neither is payload.
An installation at revision 3.2 or earlier moves through its own reviewed update:
[UPDATES](payload/UPDATES.md), "Move to the AGENTS.md block". Static checks and the
installer do not show that an agent follows the block after a compaction.

## Install beside ordinary notes and assets

Python3.10+ on POSIX with stdlib `fcntl` (macOS/Linux); current executed checks are
macOS. Windows runtime/locking is unsupported and refuses with an actionable error.
No package manager, network, service, daemon or scheduler is installed. Source and
installer guides are not startup; only the selected manifest payload is installed.

```sh
python3 pattern/starter/install.py plan --target /path/to/project
python3 pattern/starter/install.py install --target /path/to/project
```

Ordinary files survive. Existing `.director`, `.producer`, `.program`, `.team`,
`requests`, AGENTS or CLAUDE conflict causes a no-write refusal. Repeat identical
install is a no-op preserving records, optional roles, policy, the project section
and the project's own AGENTS.md text; changed package, an edited Director block
or local instruction drift refuses. No starter-2/legacy-store migration is supplied.
The installer stages/verifies all selected bytes, creates config schema1/store2
`director-request-bundles`, validates its empty state and writes `.director/install.json`.
That exact technical receipt records managed hashes/source evidence and unrun native
startup/acceptance separately. A fresh UUID project identity is allocated once at actual install, independently of
the target path. A deterministic plan leaves it unallocated (config hash null).
Cloning/moving initialized work preserves its identity; never copy it as a template
for a different project. UUID event IDs support distinct cross-machine operations.

The manifest includes the worker foundation, the seven action cards, deferred
operational/record/learning guides, the established backend, thin CLI, canonical-note
learning and daily discovery. Code on disk is not startup model context. `plan`
reports exact per-file and total bytes, the standing block and project-section bytes
with their caps (7,600 and 3,000), each card's bytes (cap 6,000) and the worker
foundation (cap 4,500); an over-cap block, section, card or worker file refuses. Existing privacy choices are preserved. Fresh
config/request records/exact sources/receipts are Git-eligible by default so a clone
can recover the same work. The owner warns once for a public/unknown remote and
records actual delivery; exact pushed messages remain readable after deletion.
Existing privacy opt-outs/parent ignore rules remain unchanged; Git eligibility
is not an automatic commit or push.

Local Git provenance records full checkout/published-base SHA, pattern-tree identity
and dirty/candidate delta separately when the canonical origin/main evidence exists.
This is offline evidence, not a latest-network check or adoption. A transported
package may supply `--source-receipt FILE` with `source` (canonical url/fullsha,
publication evidence) and `payload_sha256` for every exact manifest payload name;
all hashes must match. Caller attestation is not authentication. Unknown provenance
stays explicit and the active owner resolves/reviews it under UPDATES before safe
replacement; a copied folder is not silently called published/accepted.

```sh
python3 pattern/starter/install.py rollback --receipt /path/to/project/.director/install.json
```

Rollback takes the native writer lock and removes only unchanged owned bytes. It
preserves ordinary files and refuses new records/roles/cache/policy, changed config,
active writer or instruction drift. It stops no actor and refreshes no existing chat.
Preserve/reconcile changed work before a separately reviewed removal.

## Use and maintenance

Before the Project Director's first ordinary reply, including hello/identity, the
standing block has it run the project section's check command, by default
`python3 .director/startup_check.py`.
This bounded read-only evidence plus the actor's actual role/guard/backend evaluation
permits 🎬; missing facts give a specific gap and normal answer without a badge.
🎬 no longer claims that a chain of startup files was read.
Workers and scoped child Directors skip this check. It reads no tracker history,
uses no network/checker actor, writes no startup checkpoint and initializes no store.
A later badge question performs the currently possible check, not just an explanation.
This local check does not prove native-host behavior or broader acceptance.
Mature projects state their exact receipt/config/selected-guard command in the
project section, with the structures in OPERATIONS;
lean/manual routes use their authoritative known contract, not invented JSON state.
The check also reports whether daily update discovery is due, whether the block still
matches its recorded baseline, and what to do next.

The block tells every role to repeat its startup after every compaction or session
resume (a summary is not a re-read): the Project Director's check, a Director's
recovery steps, a worker's WORKER.md and role file, and the card or manual the next
action needs. Recovery (find held work, reconcile it with current evidence, resume
ownership, report) is written in the block itself and also runs at the first project
action of every new conversation. Selected project guards and task/action
instructions remain binding before action.
The marker `director-starter:2` is the retained block interface, not a state version;
block wording can change between revisions under the same marker. The checker accepts
a block that names `.director/WORKER.md` and has the `director-project` section beside
it; a block that still names `.director/START.md` passes only with its earlier full
startup files.
Actors have fitting **emoji Name** labels plus actual handles, without identityfiles.
While delegated work is held, proactive **📋 SitRep** runs about five minutes from
actual dispatch, independently of short host progress updates; no offline wakeup.

The Director chooses current capability/effort/verification for risk, preserves
specialist discovery/authority and independent testing, records exact originals and
addenda before dependent work, plans every finishable obligation and supervises
actual handles through evaluation/rework. Parent/requirement/evidence traces stay
compact and recoverable. Canonical source/history and local assets survive folder
moves/recovery. State does not prove liveness, human approval or true evidence.

```sh
python3 .director/requests.py status --limit 5 --max-bytes 12000
python3 .director/requests.py current REQ-... --max-bytes 12000
python3 .director/requests.py --help
```

Read deferred [API](payload/API.md), [TOOLING](payload/TOOLING.md) and
[RECORDS](payload/RECORDS.md) before state actions. Bounded current views omit history
but validate underlying original sources internally; follow snapshot continuations.
The direct backend API is unchanged; the thin launcher supplies its actual root.
No human/OS authentication or cross-host atomicity is claimed.

[LEARNING](payload/LEARNING.md) uses typed canonical notes, not another store. At
meaningful evaluation, three pending incidents make one bounded review due under
the default owner/closure policy; actual dispatch or durable real deferral required.
Review output+proposals save atomically before explicit incident IDs are consumed.
The owner evaluates scoped decisions and next matching work loads accepted knowledge.
Explicit source-backed user rules apply immediately without threshold/review. No
incident/review count creates authority or a department. Existing project policy
wins; install flags `--review-initiator`, `--review-when`, `--review-min-incidents`
set only the initial receipt's policy. Touched current role/runbook/artifact upkeep
is a separate closure duty even when no learning review is due.

[OPERATIONS](payload/OPERATIONS.md) owns the check's structures and the context-budget
preflight; the cards own staffing, requests, supervision, knowledge, update
discovery, privacy and the badge.
[UPDATES](payload/UPDATES.md) restores rolling24h active-session metadata discovery
including failures; notify(default), explicit automatic, and off choices; exact
published pins, backups, baseline/current/incoming adaptation comparison, schema/
privacy preservation, rollback and receipt. The deterministic helper only checks
metadata/saves preferences; automatic application is actual scoped owner/worker work,
not unattended code execution. Missing transport/capability stays visibly pending.
A file check or CLI fixture is not fresh-host compliance, periodic cadence, human
acceptance, release, or proof the method is universally cheaper.

Starter3's executable installer provisions tracked mode only. An explicit lean
choice remains available through the [legacy v1 guide](../INSTALL-v1.md#select-and-copy-only-the-payload)/real existing-tracker
route, with its actual smaller retention promise and no automatic new store. Do
not call this installer lean-compatible or drop open commitments to change mode.
