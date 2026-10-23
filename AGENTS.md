# Maintaining this repository

These instructions govern edits to this candidate's source repository. They are
not installation payload and do not automatically assign every author a director
role. An explicitly adopted local installation is separate from maintaining the
public method. Follow your actual assignment and host instructions.

For target-project installation, follow [pattern/README.md](pattern/README.md);
copy only the payload selected by its manifest. Reading maintainer rationale is
not an installation prerequisite. Never copy this AGENTS.md into the target.

Before changing this design, read [README.md](README.md),
[development/RATIONALE.md](development/RATIONALE.md), and relevant linked contracts
or design documents. Read selected exact sources when needed, not every archive.
Keep the living rationale coherent at formative decisions: preserve dated changes
and superseded reasoning, link affected contracts and a concrete regression case,
and distinguish stored, decided, implemented, and verified. Label hypotheses/open choices.

Retain exact source conversations and internal reference material privately,
separate from public documentation. Preserve originals without rewriting them;
record later steering as dated additions. Private evidence is not another live
instruction layer. Current contracts and rationale decisions/supersessions control.
Public rationale should distill decisions and regression cases without publishing
raw conversations, internal provenance, or links requiring private access.
Preserve other authors' edits and assigned ownership. Public authoring guidance,
rationale, and tests remain outside the installable `pattern/`.

<!-- director-pattern:start -->
## Optional local Director Pattern

When a local `.director/` installation exists, resolve your actual assignment role
and read its `PATTERN.md`. Directors also load installed `PROJECT.md`, `MODELS.md`,
and `STATE.md`, plus `DIRECTOR.md` for the project Director or `REQUEST_MANAGER.md`
for a Request Manager; anyone staffing work follows its `ROLES.md`, `ASSIGNMENT.md`,
and `IDENTITIES.md`. Workers/reviewers load their assignment and its supplied role
references, and recorders load `RECORDER.md`, STATE, and applicable references. A
new project conversation defaults to its project Director regardless of who opened
it; an explicit assignment overrides that default. Bounded delegated assignments
must name worker/director role, responsibility, scope, and authority. Missing roles
require clarification with the assigner; ancestry and inherited history confer
neither role.

Existing project authority and product/release gates remain in force. The Director
judges selected primary evidence and artifacts; each complete outcome has one
accountable owner, normally a Request Manager; workers execute implementation and
routine verification, and a
shared recorder handles routine state I/O. The Director first works out what is
being asked and answers itself when the answer fits in its reply. Before using 🎬,
the project Director has the recorder check actual startup wiring, required
installed files, and project configuration/mode, in the background when it first
staffs work and never delaying an answer, then resolves its own role and judges
that receipt. Request
Managers and other roles use their assigned identity instead of the badge. If the
installation is absent or incomplete, explain that limitation without a badge;
maintain the project rules above. Do not assume that source files or an inherited
director conversation prove installation.
<!-- director-pattern:end -->
