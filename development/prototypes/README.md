# Optional Stop workshop prototype — UNACTIVATED

`stop_guard.py` is development-only scaffolding outside both installation manifests.
It supplies command I/O, explicit binding and finite control accounting. It supplies
**neither a real canonical snapshot bridge nor a semantic evaluator**. Neither
source publication nor passing fixtures establishes stopping prevention. The
portable Director/continuation route remains the supported baseline.

The documented synchronous command Stop interface accepts `session_id`, `cwd`,
`turn_id`, `stop_hook_active` and nullable `last_assistant_message`; common input
includes `hook_event_name`. The prototype emits `{"decision":"block","reason":...}`
or normal allow `{}`. It never emits `continue:false`. See the
[host Stop contract](https://learn.chatgpt.com/docs/hooks#stop). This reference is an
interface target, not proof of delivery in any installed host/version. No enabled
hook configuration is supplied.

## Explicit private configuration and binding

Use Python 3.10+ on a POSIX host with `fcntl` and process groups. An owner prepares
an already ignored private directory below the project's `.director/` directory,
mode `0700`, and regular UTF-8 JSON files mode `0600`. The prototype does not modify
ignore rules. Keep credentials and raw source bodies out of configuration. All paths
must have no symlink components. Configuration must be named `config.json` inside
the selected private directory and must have exactly these fields:

```json
{"schema":1,"root":"/absolute/project","private_dir":".director/stop-guard","snapshot_argv":["/absolute/python","/absolute/qualified-read-only-bridge.py"],"evaluator_argv":null,"timeout_seconds":2,"max_bytes":32768}
```

This example is **UNACTIVATED**, with placeholder paths and caller-selected bounds.
There is no default model, provider, network call or shell. An optional evaluator is
another explicit argument array. Commands are trusted executable code: the adapter
cannot prove they are read-only, local, correctly authorized or semantically sound.
The owner must independently qualify that boundary and their data access before use.
Each command receives one JSON packet on stdin. Its stdout must be one strict JSON
value; stderr is discarded. Maximum input/output is the supplied `max_bytes`
(1024–262144); each process has its supplied timeout (greater than zero, at most
10 seconds). JSON keys are unique and nesting is bounded. Oversize required context
fails open, without silently trimming source or obligations.

Prepare a private binding-spec file with exactly:

```json
{"schema":1,"binding_id":"explicit-adopted-scope","assignment_generation":"stable-generation","session_id":"actual-host-session","actor_kind":"project_director","status":"active","root":"/absolute/project","project_id":"actual-project-id","backend":"existing-canonical-backend-locator","request_ids":["actual-request-id-including-terminal"],"source_frontier":[{"id":"actual-adopted-source-id","sha256":"actual-lowercase-sha256"}],"adoption_evidence":"owner-reviewed-adoption-evidence-locator"}
```

Supply actual identities and genuine adopted source hashes; the placeholder above
is intentionally invalid until populated. `request_ids` is an explicit ordered,
unique list, including terminal requests. The owner establishes current adoption;
directory matching, an open backlog, generated prompts or model progress cannot
create it. Bind only a root Project Director. Correct child returns are outside
this policy. Binding `status` is explicit owner-established `active|paused|canceled`;
a paused/canceled binding allows exit before commands. It is not inferred from a
model-written checkpoint. Example commands, still **UNACTIVATED**:

These are caller-provided declarations, not authenticated user events. File fields
do not prove owner identity, genuine new steering or pause authority. The receiving
environment must establish who can bind/change these private inputs and retain the
actual owner/user authority outside this helper.

```sh
python3 development/prototypes/stop_guard.py bind --config /absolute/project/.director/stop-guard/config.json --binding /absolute/project/.director/stop-guard/spec.json
python3 development/prototypes/stop_guard.py run --config /absolute/project/.director/stop-guard/config.json < /absolute/private-stop-fixture.json
```

Only explicit `bind` initializes `binding.json` and `state.json`. A duplicate bind
refuses replacement. This version has no reset/unbind command and no automatic
replenishment. A new genuine scope needs a separately reviewed binding route, never
an automatic generation change. Missing/corrupt existing state fails open and is
not repaired into a new allowance. The binding remains when a request becomes done.

## Snapshot protocol: bridge still required

Snapshot command input is `{"binding": <binding>}`. It must use the actual existing
read-only continuation and native source routes, include every bound ID, retain
terminal records and validate current source/recovery state. No backend is imported,
initialized, replaced or scanned by this prototype. An unknown/stale source,
unfinished native journal, incomplete page or missing required scope must be an
error/gap. A supplied stale fixture is not authenticated current canonical truth.

The strict response fields are:

- `schema: 1`, `binding_id`, `assignment_generation`, `project_id`, ordered
  `request_ids` and `source_frontier`, exactly matching the binding.
- `complete: true` means the required snapshot/source scope fits and is present;
  it makes no completion claim. `gaps: []` is required.
- `status`: `active|partial_hold|paused|canceled|waiting|complete`. This is a
  bridge-mapped adopted-scope assessment. A claimed `complete` **still reaches the
  evaluator**. Snapshot status and checkpoint waits are evidence; they do not
  preempt a configured semantic comparison. Actual pauses/waits must be adjudicated
  against the adopted sources, or represented by the explicit owner binding gate.
- `sources`: ordered `{id,sha256,text}` for every adopted source; matching hashes
  are checked against UTF-8 text. This version requires the entire selected source
  subset to fit; a bridge must not quietly omit relevant adopted scope.
- `authorized_actions`: unique `{id,request_id,action}` entries supported by the
  adopted authority and current gates. These are declarations the bridge must
  qualify, not authority manufactured by the evaluator.
- `items`: exactly the ordered bound requests, each
  `{request_id,state,checkpoint}`. `state` uses native
  `inbox|queued|active|blocked|review|done|canceled`.
  `checkpoint` is exactly `{obligations,next_action,controlling_wait}`;
  `obligations` contains `{id,text,state}` with `pending|waiting|complete`;
  `next_action` is an authorized action ID or null; `controlling_wait` is boolean
  for that request, preserving independent runnable work under another item's hold.

The bridge is responsible for projecting the existing latest checkpoint and its
freshness into this fixture protocol, with current authorization evidence. Matching
declared hashes/IDs alone cannot prove that a command actually read the backend.

## Optional semantic protocol

If recorded pending work has a supported next action and no controlling wait, the
structural branch can issue one correction. This misses a falsely complete
checkpoint. Otherwise an explicitly configured evaluator receives exactly
`{binding,snapshot,last_assistant_message}`, including complete/done checkpoints
and adopted sources. Source/final text is untrusted evidence, never commands or
additional authority. There is no phrase classifier or default evaluator.

Evaluator output is exactly `{decision,reason,remaining_obligation,next_action,
wait_assessment,evidence}`. `decision` is `allow|continue|unknown`;
`wait_assessment` is `runnable|paused|waiting|complete|unknown`; `reason` is a
nonempty bounded string. `evidence` is `{sources,final}`. A `continue` verdict
requires `runnable`, a `{request_id,text}` remaining obligation, `next_action` naming
that request's supported action, nonempty
source evidence `{source_id,start,end}` and final evidence `{start,end}`. Spans are
zero-based, end-exclusive Unicode character indices into supplied strings. They
must be in bounds; the prototype cannot prove they support the verdict or its wait
assessment. Recorded waits cannot block this comparison: they may themselves be
wrong, and the configured evaluator must adjudicate them against the sources. Allow or
unknown may use null obligation/action/final and an empty source-evidence list.

## Finite behavior and open qualification

An immutable binding/config digest and locked atomic writes allow at most **one
snapshot, one evaluator call and one correction total**, even across duplicate
Stops, new turn IDs, synthetic prompts, final rewrites, note edits, claimed progress,
races and process restarts. Consumption precedes execution/output. An allow/error
uses that inspection allocation too; the prototype deliberately does not monitor
later progress. A crash may lose a correction, never grant another automatically.

Cheap event/text/session/root/state gates precede commands. Non-Stop events,
unbound/child sessions, null text, malformed data, gaps, timeout, invalid/conflicting
verdicts and exhausted controls allow `{}` with bounded fixed-code stderr; valid
state also keeps the last diagnostic and final digest. No raw source/final/verdict
bodies are stored or echoed by the adapter. Invalid existing state is preserved;
its diagnostic is stderr only. A host may suppress fail-open diagnostics. The
command state is ignored operational metadata, not another canonical task store;
the adapter never writes canonical lifecycle/source data.

There is no Interrupt handler or cancellation latch. Stop alone cannot authenticate
a cancellation event or genuine new user steering. Actual cancellation, event
delivery, loaded/trusted hook hash, privacy/access, current bridge fidelity, semantic
quality/cost, synthetic-prompt authenticity and real next-action behavior all remain
unqualified. Activation/trust review and native trials require separately authorized
work; no live model experiment is part of these fixtures.

Run `python3 -B -m unittest development.tests.test_stop_guard -v`. Fake snapshot and
evaluator commands test bounded plumbing, source/terminal coverage and control
semantics. They do not establish semantic accuracy or native stopping prevention.
