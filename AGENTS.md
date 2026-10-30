# Maintaining this repository

These instructions govern edits to this candidate's source repository. They are
not installation payload and do not automatically assign every author a director
role. An explicitly adopted local installation is separate from maintaining the
public method. Follow your actual assignment and host instructions.

For target-project installation, follow [pattern/README.md](pattern/README.md);
copy only the payload selected by its manifest. Reading maintainer rationale is
not an installation prerequisite. Never copy this AGENTS.md into the target.

Before changing this design, read [README.md](README.md), the overview and owning
decisions in [development/RATIONALE.md](development/RATIONALE.md), and affected
contracts/design documents. Read the rationale's maintenance section when editing
it and relevant validation sections of development/DESIGN_NOTES.md when claiming
checks. Follow dated supersessions for the affected decision; full unrelated
history is discoverable reference, not a universal read requirement. Read selected
exact sources when needed, not every archive.
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
When a local `.director/` installation exists:
At the start of each conversation, your first tool invocation must only read
`.director/PATTERN.md`; wait for and read its result. Complete its startup sequence
and acknowledge the resolved role package before any task I/O, planning,
delegation, changes, or substantive answer. A brief acknowledgment may come first;
then address the original request in the same turn, without requiring a greeting
or extra confirmation.
For the selected Director role, delegate substantial analysis and project changes
to bounded subagents as directed by the selected role package, subject to
higher-priority host instructions.
If absent or incomplete, explain the limitation and maintain the repository rules above.
<!-- director-pattern:end -->
