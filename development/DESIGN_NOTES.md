# First candidate design notes

The candidate supports outcome ownership, recursive worker delegation, active
supervision, evaluated closure, exact intent capture, interruption recovery, and
evidence-backed improvement. The installed contract stays small and project-local.
These public notes describe validation scope; source conversations and internal
references are retained privately and are not installation dependencies.

## Where the reasons live

[RATIONALE.md](RATIONALE.md) is the canonical evolving explanation of WHY: current
directions, status, alternatives, tradeoffs, and revisit triggers. These notes
retain validation scope rather than a second decision history.

The [storage comparison](REQUEST_STORAGE_COMPARISON.md) explains generic design
alternatives, and the [relationship design](REQUEST_RELATIONSHIPS.md) describes
independent outcomes and peer-owned execution without imposing a universal tree.
Request folders and typed links are implemented. Verification evidence remains
separate from that selection; documentation does not authorize real-store migration
or external communication.

## Manual scenarios before adoption claims

| Case | Required observation |
|---|---|
| Inherited director history | Child and grandchild stay workers unless explicitly scoped directors; each parent evaluates descendants. |
| Raw multiline message and correction | Recorder receives exact source, preserves bytes once, links distinct outcomes, appends tiny steering without rewriting originals. |
| Submission and rework | Director inspects evidence, identifies a concrete gap, routes repair, and accepts the integrated scope only after required returns. |
| Uncertain interrupted handle | Recorder retrieves receipts; actual host check and partial-output inspection precede any overlapping restart. |
| Recorder unavailable | Director discloses persistence gap and continues conversation without direct helper/file writes or false saved claims. |
| Repeat installation | Worker preserves local PROJECT/contract edits, backs up conflicts, reuses one hook, and retains unfinished state. |
| Rapid director turns | Several ordinary replies and worker returns within a few minutes get direct answers or brief progress; a full SitRep is not automatically appended to each. |
| Ordinary host progress updates | Meaningful ordinary updates satisfy a stricter host cadence; no redundant full report is added just to satisfy the same timing requirement. |
| Quiet ongoing managed work | Actual observations support a compact timed overview after several otherwise quiet minutes, with no more than five minutes of silence; held work, owners, blockers, and next proof remain visible. |
| Meaningful change | A result, failure, retry, blocker, or evaluation is communicated promptly in a useful concise update; related developments can be combined into one overview while supervision continues. |

The table contains proposed agent/adoption cases, not claims of those behavioral
trials having run. The folder/link implementation is authorized and present in
the candidate helper; that does not migrate a real store or establish adoption.

## Executed checks — October 16, 2026

The self-contained INSTALL/TOOLING walkthrough passed from a temporary copy of only
`pattern/`: init twice retained one project ID; create plus the four literal
plan/dispatch/submit/accept events reached done in archive, revision 5/history 5.
Show and validate succeeded; the linked source retained exact CRLF/newline bytes.
Only that disposable fixture was created and cleaned; no real store was initialized.

The integrated command `python3 -m unittest discover -s development/tests -v`
passed **30 tests in 3.283 seconds**: 20 helper, 3 package-boundary, and 7 independent
requirement scenarios. All used disposable directories. Covered evidence includes:

- One exact multiline source and binary attachment shared across four outcomes;
  cold CLI restart reports three done and the fourth waiting, with remote state untouched.
- Returned versus accepted handoffs, opaque external identities, reviewed external
  dependencies, required-waiver scope changes, local canceled/reopened prerequisites,
  reciprocal information links, and rejected required cycles.
- Canceling a local waiting commitment reports canceled while preserving the
  receiver acknowledgment/status and unknown remote liveness.
- Asset-preserving relocation recovery after prepared/files/moved/written faults;
  duplicate IDs, tampered sources, symlink escapes, and unknown request-root entries
  fail closed. Package payload boundaries remain isolated from development material.

These are injected interruption/disposable fixture checks, not real crash/power-loss
proof. No actual project installation/migration, human acceptance, authorized foreign
transport, authenticated remote proof, current liveness, or publication was tested.
A cold CLI process restart is not a fresh-session agent/adoption trial; those gates
remain distinct and open.
