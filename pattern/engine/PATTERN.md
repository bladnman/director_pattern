# Shared startup bootstrap

Startup interface: 1. The project-owned bridge names the single canonical role
index; resolve that locator relative to the bridge. Context is
[PROJECT.md](../PROJECT.md). This is instruction-guided loading, not automatic
injection, a runtime, or host enforcement.

## Complete startup before task work

1. First invocation: read only the project-owned `.director/PATTERN.md` bridge.
   Read its result, then read only this engine bootstrap in a separate invocation.
2. Read the bridge's canonical index in a startup-only invocation; read its result
   to resolve role and project-wide guardrails before selecting definitions.
3. Read selected definitions, startup-required references and applicable guardrails.
   Directors also read PROJECT; workers read [WORKER.md](WORKER.md), and PROJECT
   when required by their index/definition/assignment. Follow mandatory dependencies
   transitively: an unqualified reference loads with its requiring document
   (at startup if that document is startup-required). Deferral needs an explicit
   task/action trigger in the owning instruction. Batch known
   independent reads within response limits; discovered dependencies wait for their
   parent result to be read.
4. After the complete results, briefly acknowledge role, maintained responsibility,
   loaded startup package and gaps in assistant text. Honor project acknowledgments,
   then address the original request in the same turn without a greeting/confirmation.

Before that acknowledgment, do no task I/O (including read-only inspection),
substantive investigation, planning, delegation, changes or substantive answer.
A brief request acknowledgment may precede startup. Neither the bridge nor engine
stage shares a tool group with other reads; no startup stage shares one with task
work. Ordered shell commands, parallel calls from one assistant generation or a
result streamed between them do not establish consumption. A role label or promise
to read is not completion. The acknowledgment reports reads, not permission to
delegate, Recorder availability, or checked setup.
One sufficient startup acknowledgment completes this conversational duty. Loading
later task/action references needs complete reads before use, not another startup
ceremony or a separate acknowledgment for each file, unless a project rule or the
assignment explicitly requires it. Report material gaps when found.

### Read completely without a verification round trip

Bound each model-visible response, **including an outer wrapper's aggregate**.
Use known extents or conservative bounded reads reporting total extent and returned
range in the same response. Chunk unknown/oversized files with explicit ranges;
retain contiguous coverage through EOF. Allow ample space for framing, escaping
and aggregated results; a token/output limit alone cannot make a batch safe.
Return separate bounded responses when needed. Unprinted results, summaries,
searches, hashes and file existence do not supply required instruction text.

Inspect returned results for errors, truncation/elision and missing coverage.
A failed, missing, or truncated result is not a complete read: recover and read
every missing portion before claiming that reference or package was loaded.
If it cannot be recovered, disclose the specific gap and stop affected action.
Coverage belongs in the read itself; do not add a separate verification tool call
after every read. This cannot guarantee understanding or detect every host omission.

## Resolve the assignment role

Select indexed definitions by explicit `Role: worker` or `Role: director` and
maintained responsibility; supplied locators must agree with the index. Only an
unassigned project conversation defaults to indexed `director`, regardless of
opener. Delegated assignments must name role, responsibility, outcome, scope and
authority. Missing, unknown, conflicting or incomplete delegated roles clarify
with the assigner through a permitted route before affected action, never default
to Director. Ancestry, history, tool type or a “manager” label grants no role.

Preserve project authority, shared guardrails, others' edits and host restrictions.
Roles grant no access, publication, spending, thread creation, messaging or release
beyond the assignment. A source checkout is not adoption. Missing installation,
index or definition stops affected action with a visible gap, no invented fallback.
Load selected responsibilities, not every role's history; Director policies are
not common worker startup duties.

## Required capability protocols

Understand intended work next; load task-required project references before
affected inspection/execution. Before each triggered action below, completely read
its protocols and applicable mandatory dependencies. Deferral is never optional.
Keep loaded unchanged protocols for this context; reload only changed, unavailable
or no-longer-retained instructions, not before every tool call. Project triggers
and stricter gates add to this map; generic guidance or a “read-only” label cannot
bypass them.

| Capability | Before | Required protocols |
|---|---|---|
| direction | Director analysis/coordination, delegation, evaluation, held-work recovery/supervision, or claiming outcome completion/ending held-execution supervision; a reply-only answer with no held commitments is not this exit trigger | [DIRECTION.md](DIRECTION.md) |
| staffing | Any actor selects/dispatches staff, including Recorder/descendants | [ROLES.md](ROLES.md), [MODELS.md](MODELS.md), [IDENTITIES.md](IDENTITIES.md), [ASSIGNMENT.md](ASSIGNMENT.md), [STATE.md](STATE.md) plus selected indexed definitions and their selection/authority package under ROLES; the executor loads its full references before their triggers |
| persistence | Capture, canonical state I/O/recovery, or recordable ownership/acceptance decisions | [STATE.md](STATE.md), indexed [Recorder](RECORDER.md) route and project tracker adapter; bundled-store operators also read [RECORDS.md](references/RECORDS.md) and [TOOLING.md](references/TOOLING.md) |
| identity | Identity reservation/binding/change/release | [IDENTITIES.md](IDENTITIES.md) and persistence above |
| setup | Installation check or project Director badge use/refresh | [DIRECTION.md](DIRECTION.md#check-installation-before-using-director-identity) and persistence above |
| updates | Metadata discovery/preferences or update inspection/application | [UPDATES.md](references/UPDATES.md); structural integration also requires [STARTUP.md](references/STARTUP.md) and [BOUNDARY.md](references/BOUNDARY.md) |
| maintenance | Recurring responsibility/learned-rule creation/change/registration/retirement | [ROLES.md](ROLES.md#maintain-standalone-definitions-and-one-index) and its owning project rules |
| external action | Cross-project access, messaging, publication/release, spending or installation/migration/removal | Applicable project authority and maintained runbook first; lifecycle work uses [canonical lifecycle guide](https://github.com/bladnman/director_pattern/blob/main/pattern/README.md). A protocol grants no authorization. |

Reply-only discussion needs no staffing, capture, Recorder activation, operational
setup/hash check, or update discovery before the answer. It does not close held
commitments; directors retain their recovery/supervision duties without making
state reconciliation a prerequisite for discussion.
