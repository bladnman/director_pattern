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

<!-- director-starter:2 -->
When `.director/START.md` exists in this checkout:
  Read `.director/START.md` and the exact selected role package completely before
  task work; preserve this project's and host's authority. Use an explicit bounded
  worker assignment when supplied; otherwise serve as the project Director.
  Delegate useful substantial execution/coordination to bounded subagents when
  permitted. No mandatory manager, Recorder, learning or setup actor is required.
  Load selected task instructions before action; recover incomplete reads.

Otherwise:
  This public source checkout has no adopted local Director installation. Follow
  the repository maintainer rules above and the actual host/explicit assignment.
  Do not create or install a private role/state package merely to satisfy a hook;
  a source checkout alone assigns no Director role.
<!-- /director-starter:2 -->

## Tinka

Read [TINKA.md](TINKA.md) before working with this project's Tinka boards. It identifies the boards and explains how to restore the pinned app on a new machine without a skill.
