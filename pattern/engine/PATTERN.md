# Shared startup bootstrap

Startup interface: 1. The project-owned bridge just read names the single canonical
role index. Use that exact locator, relative to the bridge, without rewriting this
engine file. Project-owned context is [PROJECT.md](../PROJECT.md).

## Complete startup before task work

This is an instruction-guided loading sequence, not automatic file injection or
host enforcement. At each conversation start, including a plain question with no
role specified, complete these dependencies before task work:

1. The first invocation reads only the project-owned `.director/PATTERN.md`
   bridge. Its returned result precedes a separate invocation reading only this
   engine bootstrap. Read this result before issuing the next invocation. Do not
   batch either stage with task files, searches, commands, or other reads.
2. In a later startup-only invocation, read the canonical role index named by the
   bridge, resolving its locator relative to that bridge. Wait
   for and read its result to resolve your assignment and applicable guardrails.
3. Read the selected standalone definition(s). Read their results to discover
   required references; then load those references and applicable project-wide
   guardrails, including further mandatory references they require. Workers also
   load WORKER below. Known independent startup reads may be batched once their
   need is established; dependent discovery requires a returned, read result.
4. After the last required result has returned and been read, send a brief
   startup-completion acknowledgment in assistant text before your first task
   tool invocation or substantive answer. Identify the resolved assignment role,
   maintained responsibility, loaded definition(s) and required references, and
   any gaps; honor any acknowledgment required by those references. An earlier
   role label or promise to load them is not this completion acknowledgment.
   Then address the original request in the same turn, without requiring a
   greeting or extra confirmation.

Until this package is loaded and acknowledged, do no task I/O (including read-only
inspection), substantive task investigation, planning, delegation, changes, or
substantive answer. A brief acknowledgment of the request may precede startup.
Do not batch or parallelize startup with task work: ordered reads in one shell
command, parallel calls in one assistant tool group, or a role self-label without
reading its package do not satisfy the dependency barrier. Even an answer that
fits directly in a reply must follow role loading; background setup and identity
checks are separate duties governed by the selected role.

## Resolve the assignment role

Use the index and applicable project-wide guardrails loaded through that sequence.
Use the explicit assignment's `Role: worker` or `Role: director` and maintained
responsibility ID to select its standalone definition and required references.
Read and acknowledge those before acting; supplied locators must agree with the
index. Load only selected responsibilities, not every role's instructions.

With no assignment, a new project conversation defaults to the indexed `director`
responsibility (`Role: director`), regardless of who opened it. A bounded delegated
assignment must name role, responsibility, outcome, scope, and authority. Missing,
unknown, conflicting, or incomplete delegated roles require clarification with the
assigner through a permitted return route before affected action; they never
trigger the Director default. Ancestry, tool type, inherited history, and a label
such as “manager” confer no role or extra authority.

Workers also follow [WORKER.md](WORKER.md). Directors load the references in their
selected definition; Director-specific policies are not common startup duties.
All actors preserve existing project authority, shared guardrails, other authors'
edits, and host restrictions. No role grants access, publication, spending,
thread creation, messaging, or release authority beyond its actual assignment.
A source checkout is not adoption. Missing installation/index/definition is a
visible gap; stop affected action and report it, without inventing a fallback.
