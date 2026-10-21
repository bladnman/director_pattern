# Capability, effort, and actual selection

First candidate. Directors and Request Managers **read this policy before selecting
staff**, and choose capability and effort per assignment. Tiers describe needed
capability, not vendor names, prices, guaranteed controls, or model aliases.

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

Actively seek useful independent subagents within the shared capacity and authority.
Give each a concrete responsibility, applicable role references, bounded writes,
and proportionate verification. Sequence dependencies and exclusive resources.
Reserve capacity for evaluation and integration; more concurrent actors are not
automatically faster.

Role, maintained responsibility, runtime actor, capability/effort, and authority are
separate choices. A Max worker remains a worker; a Small recorder applies supplied
decisions and returns ambiguity to its owner. A cheap model does not make an
irreversible action safe. Host restrictions on model selection, context, threads,
and delegation always apply. This policy promises no vendor pricing, throughput,
continuous availability, or simultaneous thought in one model stream.
