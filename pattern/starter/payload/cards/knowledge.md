# Knowledge: lookup, corrections and closure

Looking up knowledge for a task is for every role; recording corrections and closing outcomes are Director work. Paths are in `.director/`.

Load the project's required canonical I/O instructions before querying knowledge.
At task time, if canonical task/audience vocabulary is not already known from the
assignment/context, page `canonical_learning.py selectors` (optionally path-filtered). It returns
only current IDs/scopes, not claims/history. Map the natural task to relevant
existing selectors and pass exact tags to workers. Discovery includes overlapping
ancestor/descendant scopes; then select for the actual affected file(s), not merely
the broad discovery directory. A guessed exact-string miss
does not prove no semantically applicable rule. Then query matching knowledge with
`python3 .director/canonical_learning.py select --data-file -` (JSON task/path/audience), unless
the unchanged complete matching set is already retained. Read all matching pages,
preserving their scope and provenance. An empty/simple reply needs no request/history or learning query.

Record a meaningful incident/correction inline with ordinary result/observation
recording when supported by evidence; hypotheses remain hypotheses. At meaningful
outcome evaluation query bounded pending learning under the installed policy and
[LEARNING.md](../LEARNING.md). By default three pending incidents
make one bounded review due at closure; this only batches spend, never proves a
rule. Actually dispatch at most one bounded worker with the pending batch when due
and permitted capacity exists; product work may continue through supported
independent routes. Otherwise record the real deferral reason/IDs and next active opportunity in an
ordinary canonical note, leaving evidence pending. An explicit user rule applies now in its scope (`rule` canonical note
for durable selection), without a reviewer/count gate. A direct review request
can bypass the threshold. No implicit scheduler,
wakeup or free learning is promised. The owner evaluates proposals; accepted scoped
knowledge is queried on the next matching task. Release, access, spending and
structural changes still require their actual authority.

At meaningful closure refresh the touched role/knowledge selector, roster rows, artifact pointers
and accepted facts through their owning maintainer; preserve sources and dated history and move
stale runtime claims to evidence, not another loaded cache. Keep unaccepted proposals pending without adding
a delivery gate; check uptake on next relevant use. Preserve established caller/role IDs and optional aliases during refactors so cold
recovery can resolve older assignments without restoring mandatory actors; removing
mandatory staffing does not delete the callable responsibility. Register
new/renamed/retired responsibilities in the project roster
before use (`cards/staffing.md`); preserve applicable authority and evaluate the next selected use.
This is bounded affected-use upkeep, not a role census or automatic department creation.

END cards/knowledge.md
