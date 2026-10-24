# Bootstrap and assignment template

First candidate. Fill canonical project locators and real authority; omit irrelevant
detail. Staffing actors follow [ROLES.md](ROLES.md), [MODELS.md](MODELS.md),
and [IDENTITIES.md](IDENTITIES.md); directors also follow
[DIRECTION.md](DIRECTION.md#assign-bounded-work).

## Project bootstrap

```text
Project/domain and installed operating contract:
Canonical role index, project-wide applicable guardrails, selected specialist references:
Durable capability/effort, budget, and authority policy locators:
Recorder indexed role, routing policy, canonical state location/policy:
  Direct only if supported; otherwise manager -> assigner -> shared Recorder
Identity roster, shared cursor, optional pool, reservation/return route:
Relevant current execution/delegation/messaging controls, capacity and limits:
Authorization and acceptance/release/send gates:
```

The project Director reads durable project policy and locators from PROJECT and
resolves current host controls at the relevant use, then supplies the applicable
facts with every manager assignment. Runtime names, handles, model selections,
capacity, permissions, context, and return-route observations belong in the actual
assignment/receipt/activity evidence, never in PROJECT or another loaded environment
cache. Observation is not authority; preserve host/user restrictions and unknowns.
The Recorder's own bootstrap includes its selected indexed
definition, supplied-decision boundary, state location/format, cooperating-writer
route, receipt requirements, and identity policy. Bootstrap is required wiring;
mentioning a service name is not a working route.

## Bounded assignment

```text
Role: worker | director, as permitted by the installed contract
Maintained responsibility: selected canonical role ID + definition locator
Assigning actor and accountable outcome owner:
Display identity: reserved marker + short Capitalized name; bold name in report prefix per IDENTITIES.md
Stable outcome/assignment identity; permitted return route:
Outcome, exact source/addenda, full completion obligations and acceptance:
Scope, file/resource ownership, authority, reserved decisions, exclusions, dependencies:
Required selected role definitions + shared guardrails/runbooks/learnings:
Required model/effort policy; requested capability/effort; current supported controls:
Actual selection/known limits: record from tool receipt after dispatch
Shared capacity/budget; subagent limits (allowed by default; any prohibition states its reason):
Parallel plan: parts that could run in parallel or suit a subagent, or none:
Recorder route/state policy; what evidence/status/decisions to return:
Verification tier (MODELS.md) and its checks; review/rework/closure conditions:
You are not alone in the workspace. Preserve others' edits and adapt to them.
Before action, read and acknowledge the supplied role and required references.
Return missing/conflicting applicable definitions; no silent generic fallback.
Use this same reference-loading/identity/authority rule for any descendants.
```

Every assignment fills the parallel-plan and verification-tier lines; see the
[parallelization check](DIRECTION.md#assign-bounded-work) and
[verification tiers](MODELS.md#verification-tiers). Parallel actors share the
project's one working tree and divide it by file and resource ownership.

Use only supported assignment role values: `worker` or `director`. Name a Request
Manager, Recorder, reviewer, or analyst as the maintained responsibility, not as a
new role value. The receiver acknowledges the role/reference package and material
gaps before acting; the manager records that acknowledgment through the shared
Recorder when it is actually received. After dispatch, bind the actual handle and
model/effort evidence; never fill those with a guess. Routine artifact writes stay in
the assigned scope; shared canonical-state writes use the configured Recorder route.

An assignment transfers only its explicit bounded authority. A marker, model tier,
inherited conversation, role name, or permission to create descendants cannot
enlarge it.
