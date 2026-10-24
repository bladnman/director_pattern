# Capability, effort, and actual selection

First candidate. Every staffing actor, workers and descendants included, **reads
this policy before selecting staff**, and chooses capability, effort, and a
[verification tier](#verification-tiers) per assignment. Capability tiers describe
needed capability, not vendor names,
prices, guaranteed controls, or model aliases. Reusable contracts, templates, and
examples state capability and reasoning needs; they prescribe no vendor/model IDs,
fixed catalog, price claims, or newest-model default.

Pick capability and effort for the reasoning required, the uncertainty and
consequence of error, the available context and tools, and the need for independent
evaluation. Use the smallest suitable capability that preserves reliability. Neither
automatically inheriting the strongest parent model for every child nor choosing
the cheapest model irrespective of reliability is the policy.

| Tier | Capability need | Typical assignment | Effort choice |
|---|---|---|---|
| Small | Reliable mechanical handling with minimum reasoning | Recorder; exact capture; bounded file mapping and excerpt retrieval; formatting | Low where the host supports it and accuracy stays adequate |
| Medium | Clear bounded execution | Well-specified implementation, focused testing, routine research | Enough for the task's dependencies and verification; raise as ambiguity grows |
| Large | Complex execution or independent review; strongest suitable everyday, non-Max model | Difficult diagnosis, substantial decomposition, conflicting evidence, integrated review, most Request Managers | High or very high reasoning |
| Max | Consequential judgment and conversation; most capable available judgment model | Project Director; ambiguous outcome scoping, cross-outcome tradeoffs, difficult acceptance, a consequential Request Manager | High reasoning |

The project Director is typically Max. A Request Manager is chosen for its outcome:
Large for most, Max when scoping or acceptance is consequential and ambiguous, never
Max merely because its parent is. A role has no universal tier: a routine recorder
operation is Small, while complex state reconciliation may need more, and the
Recorder returns semantic decisions to their owner. A bounded analysis helper may
need reasoning comparable to the Director. "Small" means capable of reliable I/O,
not automatically the weakest available model.

## Project/host mapping

This policy is the project instruction to choose model and effort where the host
allows project-directed selection; it cannot override a stricter host restriction.

PROJECT keeps durable capability/effort policy and existing valid user/project
preferences separate from host observations. Scope observed controls, inheritance,
context, and capacity constraints by host and observation time. A previously
selected concrete model is evidence/cache for that assignment and host, never a
permanent role default or global model policy.

At relevant staffing, resolve concrete model identifiers **and** effort from the
current host's actually exposed controls, within existing authority. Refresh the
observed mapping when the host differs, exposed options change, or a saved selection
is unavailable. This is bounded setup maintenance, not an every-turn catalog,
exhaustive probe, model-comparison job, or external product-research task. If controls
do not expose availability, retain that uncertainty and use a supported suitable
route; do not invent identifiers.

Choose a context mode that supports the intended controls. Do not silently inherit
the strongest parent model/effort by omission. When supported and authorized, select
both for each job; short explicit context is preferable for a clerk or Recorder's
bounded work. Inherited-only forks and unsupported overrides are constraints, not
evidence of the requested selection. Host/user restrictions prevail; this policy
creates no spending permission.

Keep concrete requested and tool-selected model/effort in per-dispatch evidence,
with host, observation time, context mode, receipt, and material limits; mark unknown
effective settings explicitly. A prompt label, dispatch handle, or requested override
alone does not independently verify effective settings. If selection is unsupported,
choose an allowed suitable alternative and record it, or return a consequential
limitation to the assigner. Never describe an inherited model as Small without
evidence or infer costs from tier names.

Routine supported remapping is agent-owned maintenance within existing authority;
it needs no repeated confirmation or user-facing "gap." Escalate a real unresolved
choice or limitation affecting authorization, cost, reliability, or ability to
proceed. Keep genuine blockers and unknown effective settings visible.

## Parallelism and accountability

Any actor that staffs, workers included, may use subagents where they help. Look
for useful independent subagent work within the shared capacity and authority, in
the project's one working tree. Give each a concrete responsibility, applicable
role references, bounded writes, and a verification tier. Sequence dependencies and
exclusive resources. Reserve capacity for evaluation and integration; more
concurrent actors are not automatically faster.

Role, maintained responsibility, runtime actor, capability/effort, and authority are
separate choices. A Max worker remains a worker; a Small recorder applies supplied
decisions and returns ambiguity to its owner. A cheap model does not make an
irreversible action safe. Host restrictions on model selection, context, threads,
and delegation always apply. This policy promises no vendor pricing, throughput,
continuous availability, or simultaneous thought in one model stream.

## Verification tiers

Every assignment names one tier, chosen like capability: by the claim's risk,
reversibility, and audience. The assigner picks it; a receiver does not raise it on
its own and asks when it looks wrong. Rework keeps its tier unless the claim changes.

| Tier | Use for | Checks |
|---|---|---|
| Smoke | Exploration, mockups, prototypes, throwaway drafts | It renders or runs, and the key interactions work, such as a screenshot and a short interaction pass. No exhaustive automated suites, sweeps, or repeated polish loops. |
| Focused | A production change still being built or reworked | Targeted tests for the changed behavior and its interfaces. Leave the full suite for integration. |
| Full | Production code at integration, acceptance, or release | Full suites, freeze checks, and the project's release gates. |

A tier selects checks; it does not turn technical evidence into observed behavior,
human acceptance, or release. Live, soak, and other project gates still apply.
