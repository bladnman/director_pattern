# Role discovery and maintained knowledge

First candidate. Mandatory before staffing, at every permitted depth.

Use one canonical project role index, located in PROJECT, to discover maintained
responsibilities. The index can link generic pattern roles and organization or
project-specific roles across several projects. Generic Director and Request Manager
instructions stay reusable; the mapping selects applicable local knowledge rather
than rewriting those generic roles for every team or domain.

Each index entry needs a stable role ID, responsibility and selection cues,
canonical definition locator, applicability, required shared guardrails, runbooks,
and reviewed learnings, owning maintainer, its assignment role (`worker` or
`director`), and any authority or route constraints. Keep it quick to scan; load
definitions and references for the selected work rather than every role's history.
Project-wide applicable guardrails apply to everyone independently of role
selection; specialist references add to them and cannot bypass them.

## Required discovery sequence

1. Identify the task's work and affected project and resources.
2. Read the canonical index and select all applicable maintained roles and reference
   layers. A role definition may compose shared guardrails with a project runbook.
3. Load the selected definitions and mandatory references before writing the
   assignment. Confirm they exist and are coherent with the explicit authority.
4. Supply their exact canonical locators in the bounded [assignment](ASSIGNMENT.md),
   with source, scope, acceptance evidence, model/effort selection, Recorder route,
   and identity.
5. Require the actor to read and acknowledge the selected definition and references
   before acting. Record acknowledgment through the manager/Recorder route when it is
   actually received. The same rule applies to any descendants.

If a matching maintained role exists, do not substitute a generic engineer, tester,
or customer communicator. If the index is missing, a relevant reference is
unavailable, or applicable roles conflict, return the affected staffing decision for
resolution. Do not quietly infer a generic fallback. Explicit resolution may supply a
missing definition, select the applicable layer, or authorize a bounded temporary
role; retain that decision. Unaffected work can proceed.

## Generic pattern entries

These definitions ship with this package. A project index points to its installed
copies under `.director/` and adds its own maintained roles.

| Role ID | Assignment role | Select when | Definition and required references |
|---|---|---|---|
| `director` | director (project conversation default) | Own the conversation, independent outcomes, and whole-project coordination and acceptance. | [DIRECTOR.md](DIRECTOR.md), project bootstrap, index, shared rules, and mapping. |
| `request-manager` | director, bounded to one outcome | Own one complete entrusted outcome through review and follow-up. | [REQUEST_MANAGER.md](REQUEST_MANAGER.md), project index, and selected applicable rules. |
| `recorder` | worker | Read and write routine shared durable state and identity reservations under supplied decisions. | [RECORDER.md](RECORDER.md), [STATE.md](STATE.md), canonical state location/route, and [IDENTITIES.md](IDENTITIES.md). |
| `bounded-analysis` (optional) | worker | Prepare a substantial source or decision analysis for the Director without owning execution. | [Definition below](#optional-bounded-analysis), project-wide guardrails, and selected domain references. Prefer a matching maintained project analysis role. |

All staffing also requires [MODELS.md](MODELS.md) with the project's host mapping and
[ASSIGNMENT.md](ASSIGNMENT.md). These generic entries supply no project's specialist
rules.

## Optional bounded analysis

Read the Director's bounded question or source, relevant owner/source revisions,
exact addenda, project-wide guardrails, and selected domain role/runbook references
before action. Acknowledge the package. Gather evidence and propose coherent
outcomes, routes, or choices; make uncertainty and examined or incorporated source
revisions explicit. Receive known-source corrections at supported boundaries and
include them in the eventual proposal. Return to the Director for judgment.

Do not independently create Request Managers, execute side-effecting work, expand
authority, or answer a competing user conversation. Preserve a resume point and
relevant evidence through the configured Recorder route. This optional
responsibility can use a short-lived actor; it is not a mandatory intake layer or
permission to bypass a more applicable maintained project role.

## Illustrative project entries — examples only

The locators below are **illustrative placeholders**, not files in this package and
not real organization rules. An adopting project fills its actual canonical locators
and references before using such entries. Several projects can share
`customer-communication` while selecting different engineering and release entries.

| Example ID | Selection cue | Example canonical definition | Required-reference categories to map |
|---|---|---|---|
| `product-a-engineering` | Diagnose or change Product A behavior or code. | `<project-a>/roles/engineering.md` | Shared engineering guardrails, architecture, resource-access policy, reviewed product learnings. |
| `product-a-testing` | Reproduce, design tests, or verify Product A behavior. | `<project-a>/roles/testing.md` | Test strategy, fixture/data rules, supported verification and evidence. |
| `product-a-release` | Prepare, deploy, or verify a Product A release. | `<project-a>/roles/release.md` | Release runbook, authorization/gates, environment/rollback, production verification. |
| `customer-communication` | Draft or send a customer-facing response. | `<organization>/roles/customer-communication.md` | Company voice, factual/review requirements, privacy, permitted send/approval route. |
| `human-coordination` | Seek a teammate's information or decision. | `<organization>/roles/human-coordination.md` | Contact/channel policy, permission/authority, evidence to include. |

## Improve the system's knowledge

Preserve meaningful friction, evidence, and a supported cause separately from
speculation. Propose the smallest correction to the owning role or runbook
maintainer. After review and an authorized update, retain its revision or evidence
link in the index or canonical reference. Future assignments load that corrected
reference; evaluate its next relevant use. Do not make each fresh actor rediscover
the last team's lessons, or turn every anecdote into a universal rule.

A role is a maintained responsibility and knowledge package. It is not a live agent,
a model size, a permission level, a department instance, or a delegation license.
