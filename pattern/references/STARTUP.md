# Establish and verify the startup route

Use this procedure for installation and every upgrade. An installing agent need
not already be a Director: follow the user's installation authority and actual
host/assignment rules. The result should give every fresh actor a small common
bootstrap and the selected maintained role's instructions before action.
Do not invent an abstract of the method in AGENTS.md.

## Audit and integrate the loaded instructions

1. Identify the host's actual loaded entrypoint and all always-loaded or
   transitively required instructions, including parent/global files and existing
   AGENTS, CLAUDE, or equivalent files. Record what is actually loaded versus
   merely present. Review the whole startup chain for size, duplicated policy,
   competing defaults, and specialized duties applied to everyone. Merely adding
   a small hook to an enormous file does not complete this audit. There is no
   arbitrary word limit: judge what every actor needs before role selection.
2. Keep applicable project authority, safety, collaboration, and release/send
   gates common. Preserve exact existing specialized instructions by moving them
   to standalone maintained definitions or referenced contracts with the same
   applicability and authority; record old section → new canonical locator in
   the receipt and check no instruction was lost. Preserve originals in verified
   backups/history. Do not summarize away constraints. If ownership or scope is
   ambiguous, retain the original until resolved and report the incomplete audit;
   do not advertise the startup refactor as complete. Changes to parent/global
   rules outside authorized scope remain an explicit gap.
3. Reuse the project's canonical maintained role index. If none exists, generate
   a project-owned `.director/ROLE_INDEX.md`; it is not upstream managed payload.
   An existing index also needs this audit: an entry pointing only to a giant
   AGENTS section or loose runbook prose is not yet a standalone role definition.
   Create its maintained definition, preserve/reference the exact applicable
   instructions, update that existing entry, and verify the new route; do not
   create a competing index or discard project entries.
   Register actual `director` → `DIRECTOR.md`, `request-manager` →
   `REQUEST_MANAGER.md`, and `recorder` → `RECORDER.md` entries with selection cues,
   role, references, authority constraints, and maintainer under
   [ROLES.md](../ROLES.md). Add actual project specialist entries and moved
   instructions; optional `bounded-analysis` selects `ANALYSIS.md`. Resolve
   locators relative to the index. Definitions include required shared contracts:
   director definitions load DIRECTION, PROJECT, MODELS, STATE, ROLES, ASSIGNMENT,
   and IDENTITIES; workers load WORKER plus their selected definition/references.
   A role may compose existing references without duplicating them. Do not seed
   illustrative specialists as real definitions.
4. Fill PATTERN's canonical-index locator with the one real path (a relative
   Markdown link is suitable); record the same path in PROJECT. This pointer is a
   local adaptation preserved across updates. Keep one live role table in that
   index; the hook and bootstrap route there instead of copying it. Verify each
   selected definition and required reference exists and agrees with its entry.
5. Replace the old identifiable pattern startup block with INSTALL's small hook.
   Remove relocated specialized duties from always-loaded files only after the
   maintained destination and index are reachable. Recheck the entire chain:
   no stale abstract, repeated role table, or competing default remains active.
   Record loaded paths, moved sections, index pointer, remaining gaps, and hashes.

A predecessor adoption may replace its old startup role-default instruction as
part of reviewed reversible instruction integration. Preserve shared authority
and predecessor records, and leave one active default. This instruction change
neither authorizes a `.producer/` store migration nor makes that store compatible
with the Director helper. If it stays canonical, map its existing authorized
workflow as an existing tracker; otherwise obtain a separate migration decision.

## Static checks, then fresh host trials

First inspect file/link reachability, actual host startup configuration, role-index
entries, and preserved-instruction mapping. Disposable fixtures can check that
selected manifest files are self-contained and project-owned files survive a
merge. These establish wiring and preservation, not fresh-agent behavior.

Then use the host's supported fresh-session mechanism, subject to its conversation
creation and delegation restrictions. A fresh context must start through the real
project entrypoint; do not simulate success by pasting all role instructions into
an already running conversation. Use harmless read-only or disposable tasks and
retain observed file reads/acknowledgments and first role-specific actions:

| Trial | Required observation |
|---|---|
| Fresh unassigned project conversation | Receives common bootstrap, follows the canonical index, loads the Director definition/references, and resolves `Role: director`. An answer that fits in its reply remains direct; no setup ritual delays it. |
| Fresh explicitly assigned reader, writer, reviewer, or test responsibility | Receives bootstrap, resolves its indexed worker definition and required references, acknowledges them before action, and retains bounded worker authority even with inherited Director history. Use actual maintained definitions; disposable definitions may be clearly labeled fixtures. |
| Missing role, unknown responsibility, conflicting definition, or incomplete delegated assignment | Stops affected action and seeks clarification through a permitted route, without becoming Director or inventing a generic specialist. |
| Newly registered recurring role | Discovers the new standalone definition through the same canonical index and reads its references before action. |
| Upgrade from oversized startup instructions | Common startup excludes relocated specialist duties and stale pattern defaults; the selected responsibility still reaches every preserved instruction at its maintained destination. |

Record each trial separately with host/session, startup route, assignment,
observed reads or acknowledgment, first action, result, and limits. An unread
file's existence, a role's self-description, a fixture, or a setup badge is not
proof of the real read sequence. Where the host cannot expose reads, say which
acknowledgment/behavior was observed and what remains unverified. If a fresh trial
cannot be run, mark it pending; do not fabricate a successful behavioral check.
Refreshing files does not refresh already loaded conversations.
