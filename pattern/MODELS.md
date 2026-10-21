# Capability and actual selection

First candidate. These tiers describe needed capability, not vendor names,
prices, guaranteed controls, or model aliases. Use the smallest suitable capability
for the assignment while preserving reliability.

| Tier | Meaning | Typical assignment |
|---|---|---|
| Small | Reliable mechanical I/O with minimum reasoning | Recorder; bounded file mapping and exact excerpt retrieval |
| Medium | Clear bounded execution with moderate reasoning | Routine implementation or verification |
| Large | Strongest suitable everyday, non-Max model with high/very high reasoning | Complex execution; independent review |
| Max | Most capable available judgment model with high reasoning | Director; consequential or ambiguous review |

Default director: Max. Default recorder/clerk: Small. Implementation normally
starts at Medium and uses Large when complexity requires it. Review normally uses
Large and uses Max for consequential ambiguous judgment. “Small” means capable
of reliable I/O, not automatically the weakest or smallest available model.

During installation, map these tiers to the host's exposed models and effort
settings in PROJECT.md. Record requested and actual model/effort for assignments,
or explicitly mark either unknown. Passing “Small” in a prompt does not select a
model. Check actual tool controls and receipts; do not claim controls the host
lacks or infer costs from tier names.

Avoid inheriting the director's Max model and full history into a clerk when the
host supports explicit model selection and short assignment context. Supply only
the exact source or path, mechanical operation, permitted writes, and return format.
If selection is unsupported, report the actual limitation and agree a supported
mapping; never describe an inherited model as Small without evidence.

Capability does not change role or authority. A Max worker remains a worker;
a Small recorder applies supplied decisions and returns ambiguity to the director.
Host restrictions on model selection, context, threads, and delegation always apply.
