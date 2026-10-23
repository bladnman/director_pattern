# Capability, effort, and actual selection

First candidate. Directors and Request Managers **read this policy before selecting
staff**, and choose capability, effort, and a [verification tier](#verification-tiers)
per assignment. Capability tiers describe needed capability, not vendor names,
prices, guaranteed controls, or model aliases.

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

During installation, map these tiers to the host's actually exposed models and
effort settings in PROJECT.md, with constraints on selection, inheritance, and
context, and the shared capacity/budget. Maintain that mapping centrally when the
host changes; generic roles do not embed vendor names or assumed prices.

For each assignment retain requested tier/model/effort and the **actual
tool-selected** model/effort, or mark either unknown. Preserve selection receipts
and constraints such as unavailable effort levels, inherited-only full-history forks,
or unsupported overrides. Passing "Small" or "high effort" in a prompt does not
select it. Check actual tool controls and receipts; do not report a selection the
tool did not make, or infer costs from tier names.

Avoid inheriting a director's model and full history into a clerk or recorder when
the host supports explicit model selection and short assignment context. Supply only
the exact source or path, mechanical operation, permitted writes, and return format.
If the desired selection is unsupported, choose an allowed suitable alternative and
record it, or return a consequential limitation to the assigner; never describe an
inherited model as Small without evidence. Actual supported controls and user or
project instructions take precedence over generic preferences.

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
