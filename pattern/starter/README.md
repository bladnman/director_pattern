# Flat Director starter 2 — new projects

This candidate starts with one Director foundation and bounded workers. There is
no default manager, Recorder, identity pool, setup actor or review actor. It is a
separate format from the legacy v1 engine (the full repository keeps `pattern/README-v1.md`); installing it never
overwrites or migrates that engine, its tracker, project policy or mature stencils.
This subtree is self-contained for transport; none of its source guides is startup.

Use Python 3.10+ on a POSIX host with standard-library `fcntl` (macOS/Linux).
The current checks run on macOS; Windows locking is not implemented and unsupported
hosts receive an actionable error. Role instructions remain host-neutral. No network, dependency manager,
service or scheduler is used:

```sh
python3 pattern/starter/install.py plan --target /path/to/new-project
python3 pattern/starter/install.py install --target /path/to/new-project
```

The project may already have ordinary meeting notes/assets; these are preserved.
Existing `.director`, `.producer`, `.team`, `.program`, `requests`, AGENTS or CLAUDE
startup need reviewed integration and cause a no-write refusal. This is deliberate
preservation, not automatic migration. Existing unrelated files are never copied
into the payload. Identical reinstall is a no-op preserving state and optional
role files; changed instructions/package cause a visible refusal, not overwrite.

The manifest selects seven static files under `.director/`: START, DIRECTOR,
WORKER, LEARNING, deferred API, the stdlib state helper and privacy ignore rules.
Installer adds a thin explicit-delegation AGENTS bridge, empty state and a technical
install receipt. Plan reports exact per-file hashes/bytes and Director/worker
startup bytes. The initial project identity is deterministically derived from the
installation root; copied installed state retains that identity, so a new project
uses a fresh install rather than cloning initialized state. Runtime sources/state/
receipt stay ignored by default; decide privacy before publishing exact inputs.

Rollback only removes unchanged owned installation bytes:

```sh
python3 pattern/starter/install.py rollback --receipt /path/to/new-project/.director/install.json
```

It preserves ordinary notes/assets and refuses after changed state, instructions or
new files in the managed area. Preserve/reconcile those before any removal. It
does not stop actors or refresh already running chats. This is a reversible file
operation, not a host-enforced sandbox, adoption guarantee or background runtime.

## Ordinary use

The bridge asks for START and the exact selected role package in complete bounded
reads, without a bridge/index/engine dependency ceremony. An unassigned conversation
loads the small Director foundation; assigned workers load only their package and
applicable guards. New task instructions and matching accepted knowledge load
before action, with unchanged retained instructions reused. Discussion stays direct.
Existing independent review, release, spending and access gates remain binding.

An explicitly assigned Director uses the same foundation plus a bounded overlay
only when meaningful outcome coordination needs it. Role/department knowledge is
project-defined; instruction composition never merges required independent actors.
The owner retains whole delivery, steering, evaluation and pending approvals.
Direct narrow validated state operations are Director duties. An existing tracker
remains canonical; the helper is not a second-ledger or migration license.

Discover the deferred exact runtime JSON API without reading implementation:

```sh
python3 .director/state.py --help
python3 .director/state.py help
python3 .director/state.py status --data-file /path/to/query.json
```

Empty stdin or `{}` is a default compact query. Mutations carry unique `op_id`,
expected global revision and, for request changes, expected request revision.
They preserve exact UTF-8 source/addenda and attachment hashes, current obligations,
owners/handles/dated observations, evaluations and approval gates. Original sources
and history remain separate from compact status. Helpers validate supplied data,
not whether the caller is authorized or its observations true.

## Learning has a queue, an initiator and a cost

Default installed policy: outcome owner initiates one bounded review at meaningful
closure when three incidents are pending and permitted worker capacity exists.
Ordinary observe/evaluate receipts expose `review_pending`, count and `review_due`.
The number only batches spend; it proves no rule and creates no department. Options:
`--review-initiator user --review-when explicit` leaves review for direct requests;
`--review-min-incidents N` changes the initial spend gate. Reinstall does not silently
change an existing policy. A direct review request can override the count gate.

Capture meaningful incidents inline with ordinary results, preserving scope/source/
revision and hypotheses. When due, the initiator actually dispatches one bounded
existing worker with WORKER + LEARNING and a `review-batch` (default five incidents,
12000 bytes). Product work may continue independently on supported tools. If that
route/capacity is absent, `review-defer` records the real reason and evidence stays
pending. No actor is needed for an empty/simple task or a batch with no incidents.
Scheduled/offline review requires explicit authorization and a real host scheduler;
nothing here installs one or promises automatic wakeup.

`review-save` commits durable output/proposals and cursor together. Crashes/replay,
stale revisions, skipped/changed batch evidence and competing decisions fail
visibly or return an idempotent saved result. The existing owner evaluates; `decide`
accepts the exact proposed scope. Only accepted knowledge appears in matching task/
path/audience `select` results, with provenance. Routing/structural proposals need
separate authorized implementation. Hypotheses are not rules. Full history and
pending evidence never become user startup.

An already explicit user rule applies now within scope; `accept-rule` records it
with its exact source and owner decision, without waiting for incidents/reviewer.
Retire or supersede any current rule with a source-aware `retire-knowledge`, keeping
old decisions/evidence. No automatic authority growth occurs.

Review workers report actual spend/settings or unknowns separately. The helper
reports local state bytes and precommit preparation time (excluding atomic write); it parses this small state file
internally, so I/O cost grows with it. No model cost, latency or learning-success
claim follows from bytes or a cursor. Actual-agent trials establish only their
observed route; host compliance and caller permission are not enforced by roles.
