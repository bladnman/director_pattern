# Project orientation

Startup audit: [loaded chain, misplaced duties moved with exact preservation map, remaining gaps; STARTUP procedure]
Fresh host trials: [per-trial evidence or pending; distinct from static wiring]
Candidate installation state: [prepared / installed]
Installation acceptance: [owner; decision; authoritative receipt; distinct from Fresh host trials above]
Candidate source/version: [published repository URL + exact reviewed commit SHA; label unpublished candidates]
Setup/update receipt: [committed path under .director/receipts/; selected managed-file SHA-256 baselines, startup wiring, adaptations, verification scope/reason, performed checks, reused evidence and limits]
Version control: [committed by default; paths the project chose to keep local in .director/.gitignore; public-remote warning given on date / not needed / no Git: parallelism and recovery limitation reported, in-place init recommended]
Project root and outcome owner: [actual root; project Director]
Scope and desired outcomes: [one project; constraints; explicit exclusions]
Existing instruction authority and runbooks: [paths; preserve their authority]
State mode: [tracked by default / explicit optional lean choice; reason]
Canonical state: [existing tracker, or initialized .director request-bundle store; no second ledger]
Stable project identity/store schema: [actual init receipt, or existing tracker identity; paths are locators]
Current activity/recovery pointer: [path; recorder-maintained; holds Director commitments]
Important decisions: [path or canonical existing document]
Required human acceptance/publication gates: [actual policy; unknown if unresolved]

## Roles, guardrails, and routes

Canonical role index: [actual project-owned index path; same locator as PATTERN; real entries linking standalone definitions]
Project-wide applicable guardrails: [paths that apply to every actor]
Unmapped or conflicting roles: [known gaps that stop affected staffing until resolved]
Recorder definition and route: [indexed Recorder entry; direct manager→Recorder only if supported, otherwise manager→assigner→Recorder]
Recorder state policy/location: [canonical store and current activity; serialization and receipt requirements]
Identity roster and cursor: [current-activity location; never seeded or packaged]
Identity pool: [IDENTITY_POOL.txt, a project replacement, or text labels]

Fill these from the project's actual maintained definitions; illustrative entries in
ROLES are not real roles. A missing index or route is a visible gap to resolve before
affected staffing, not a reason to improvise generic specialists. Project tuning
belongs in the role index, its references, and this mapping, not in edited copies of
the generic Director or Request Manager contracts.

## Conversation startup check

Recorder setup facts: [loaded startup entrypoint and installed pattern path;
required files checked; configuration, mode, canonical state, role index, Recorder
route, and identity roster location; evidence or gaps]
Resolved current role: [new project conversation default, or explicit worker/director assignment and responsibility; scope and authority]
Current-conversation identity result: [checked project Director + tracked/lean, or incomplete/unknown; reason]

Resolve the assignment role first; only the project Director runs this check.
Request Managers receive its facts in their bootstrap. Use a Small recorder for
routine inspection, then the Director judges the receipt before using `🎬`; refresh
when role or setup changes. The check runs in the background when the Director
first staffs work and never delays an answer. The setup receipt may be compact and
conversation-local; this is not a new registry or a requirement to rewrite PROJECT
on every reply. Lean needs no bundled helper/config; an existing tracker stays
canonical. Checked setup is not a successful behavioral trial or proof that any
worker is alive.

## Capability policy and host observations

Durable capability/effort policy: [per-role/task reasoning and reliability needs;
existing valid user/project preferences; no permanent role→model table]
Resolve current selections and refresh observations under [MODELS](MODELS.md#projecthost-mapping).
Concrete selections belong in dispatch evidence, not future assignment defaults.

Observed host and time: [host identity; observation time; scope and uncertainty]
Host and execution mechanisms: [actual available tools; restrictions]
Status/observation and permitted return routes: [actual tools; limits]
Recorder availability and exact-source transfer: [mechanism; known limits]
Context isolation: [short explicit context supported / unsupported / unknown]
Shared budget/capacity and reserved review capacity: [actual limits or unknown]
Continuation after a final reply: [what the host keeps running or resumes; limits]

Model/effort/context controls and inheritance constraints: [actually exposed
controls; supported selection route; limitations or unknowns]
Per-dispatch selection evidence: [canonical record/receipt location; requested and
effective model/effort, context mode, host/time, unknowns and differences]

Observations are scoped evidence/cache. Refresh them at relevant staffing under
MODELS; a different host or changed option is routine maintenance when a supported
suitable route exists. Unsupported delegation or persistence remains a disclosed
limitation, with no silent execution-role switch.

## Source updates

Use [UPDATES.md](references/UPDATES.md) for requested or standing-authorized updates
from published GitHub `main`. The checked project Director arranges at most one
metadata check per 24 hours while active; absent policy defaults to notify.
Update preference: [notify by default / automatic only on explicit “always update director pattern” / off; update-policy.json and user-source reference]
Daily check receipt pointer: [exact accepted .director/receipts/...json; source.url, source.sha, published:true, optional pattern_tree_sha; never newest-by-date]
Local candidate delta: [none / explicitly unpublished files and evidence relative to the retained published base; no automatic source promotion]
Record source URL and exact SHA plus installed managed-file baselines in the
committed receipt. Keep the machine-local check cache ignored. Automatic mode uses
the same backup/comparison/compatibility protocol and never bypasses conflicts.
Preserve this project's context, canonical tracker, state mode, stable IDs, raw
sources, role index and definitions, model mapping, identity roster, local
adapters, and version-control choices. A template seed carries no completed
receipt or initialized identity; each generated project fills its own PROJECT
and runs its own init.

## Working references

Every actor starts with [PATTERN.md](PATTERN.md) and its canonical index, then
loads the selected standalone definition and required references. Directors read
[DIRECTION.md](DIRECTION.md), [MODELS.md](MODELS.md), and [STATE.md](STATE.md)
with [DIRECTOR.md](DIRECTOR.md) or [REQUEST_MANAGER.md](REQUEST_MANAGER.md).
Existing owners and active assignments: [canonical pointers; verify actual handles]
Local adaptations and installation history: [changes, backup paths, setup receipt]
Open decisions and next validation: [target-specific unresolved choices; relevant fresh-session trial]
