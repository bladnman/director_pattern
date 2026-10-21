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
and `STATE.md`; workers/reviewers load their assignment and applicable project
rules, and recorders load STATE and its applicable references. A new project
conversation defaults to its project director regardless of who opened it; an
explicit assignment overrides that default. Bounded delegated assignments must
name worker/director role, scope, and authority. Missing roles require clarification
with the assigner; ancestry and inherited history confer neither role.

Existing project authority and product/release gates remain in force. The director
judges selected primary evidence and artifacts; workers execute implementation and
routine verification, and a recorder handles routine state I/O. Before using 🎬,
a director has the recorder check actual startup wiring, required installed files,
and project configuration/mode, then resolves its own role and judges that receipt.
Other roles omit the badge. If the installation is absent or incomplete, explain
that limitation without a badge; maintain the project rules above. Do not assume
that source files or an inherited director conversation prove installation.
<!-- director-pattern:end -->
