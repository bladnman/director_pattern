# Install the Director Pattern

**[v1.0.0](https://github.com/bladnman/director_pattern/releases/tag/v1.0.0) · October 23, 2026.** This subtree is a self-contained package
for agents installing the method in a target project. It is not a proven adoption.

Give one project a **Director** who stays in the conversation, keeps its unfinished
commitments, sets cross-outcome scope and priority, and accepts each outcome. The
Director entrusts every independently finishable outcome to one **Request Manager**,
who owns its understanding, all completion obligations, planning, specialist tasks,
evaluation, rework, and follow-up until the Director accepts it. A specialty such as
engineering, testing, release, or customer communication is a task inside the
outcome, not a reason for another manager. Specialists execute; Small clerks map
broad material; one shared [Recorder](RECORDER.md) handles routine state reading and
writing. The Director delegates substantial analysis and detailed coordination
before that active work occupies the main conversation. Independent analysis
returns a proposal; no intake layer is mandatory. Selective critical reading and
ordinary discussion stay with the Director. No department tree is required.

"Director Pattern" names this package. Assignment roles stay `worker` and `director`:
`Role: director` carries the project Director and a Request Manager bounded to one
outcome, and `Role: worker` carries specialists, reviewers, the Recorder, and
optional bounded analysis. Request Manager and Recorder are maintained
responsibilities, not new role values. Only the checked project Director uses `🎬`;
managers and other actors use an assigned identity from a shared pool, such as
🦫 **Mason** —, chosen for a playful fit with the assignment under
[IDENTITIES.md](IDENTITIES.md). See [DIRECTOR.md](DIRECTOR.md) and
[REQUEST_MANAGER.md](REQUEST_MANAGER.md).

Tracked is the default for new installations; lean is an explicit optional choice.
Keep an existing tracker canonical. New bundled stores use request folders with
shared immutable user sources and typed relationship/ownership records. Files
preserve continuity, not agent liveness or an automatic wakeup. No service,
scheduler, runtime, or new chat is installed.

The installed `.director/` is committed with the project, including its requests
and exact user sources, so work continues from another machine or a cloud
checkout. Its own `.gitignore` keeps only the helper lock, in-progress write
scratch, pre-update backups, and daily update-check cache local. A project may
choose to keep more local;
see [STATE.md](STATE.md#version-control).

Before the Director can staff work, the installation maps four project facts in
PROJECT.md: a canonical role index ([ROLES.md](ROLES.md)), durable capability policy
and scoped host observations ([MODELS.md](MODELS.md)), the Recorder route and state
location, and the identity roster location ([IDENTITIES.md](IDENTITIES.md)). Reuse the project's
existing maintained roles and guardrails. Missing roles/routes stay visible;
routine supported model remapping follows MODELS within existing authority.

Periodic supervision overviews use **📋 SitRep** so they are easy to scan or skip.
Use one after a quiet stretch of ongoing work or when several developments benefit
from a combined view; ordinary replies and brief progress updates do not need a
full report. Meaningful ordinary updates satisfy the progress cadence without a
redundant SitRep. The checked project Director's `🎬` identity, `❓` questions, and
`🖐️` user-only actions keep their meanings. See [DIRECTION.md](DIRECTION.md) for the
sparse marker rules, timing, and continuing supervision requirements.

Every actor receives a small common [bootstrap](PATTERN.md), follows its one
project-owned role index, and loads the selected standalone definition/references
before acting. The first tool invocation reads only the bootstrap; returned
results establish each later startup dependency before any task I/O or substantive
answer. A brief completed-package acknowledgment precedes task work. This
instruction route is not automatic injection or host enforcement. Direct answers
still follow role loading; the Director's setup/identity check stays background.
Explicit assignments route first; only an unassigned project
conversation defaults Director. Malformed delegated assignments seek clarification.
Director/manager policies live in [DIRECTION.md](DIRECTION.md), outside worker
startup. Recurring specialist rules live in maintained files registered in the
same index, never an abstract appended to AGENTS.md.

An installing agent need not already be a Director. First installation audits the
entire loaded startup chain, preserves shared authority, and moves exact misplaced
specialist duties to reachable maintained definitions. Follow the
[startup integration and verification procedure](references/STARTUP.md); an
appended hook alone is insufficient. Updates use the
[incremental procedure](references/UPDATES.md#select-the-smallest-sufficient-verification):
a full startup audit or fresh-agent trial is required only by affected structure,
behavior, or detected defects. Static wiring and real fresh-agent trials remain
separate evidence.

## Adopt in a target project

Ask the agent working in that project:

```text
Read this package's README.md and follow its INSTALL.md to install the candidate
Director Pattern in the target project. Preserve existing instructions, local
adaptations, unfinished work, and the canonical tracker. Copy only the selected
manifest payload, fill PROJECT.md from real context (role index, capability policy
and scoped host observations, Recorder route, identity roster), and verify supported
host capabilities.
Do not publish, migrate requests, or copy the whole source repository.
```

Use this [package entrypoint](https://github.com/bladnman/director_pattern/blob/main/pattern/README.md)
when pointing an agent at the published repository. A staging clone is optional
transport, not a request to adopt everything in the checkout.

Follow [INSTALL.md](INSTALL.md). [manifest.json](manifest.json) is the authoritative
copy list: base files are always payload; tracked files are added only for a new
bundled tracked store. Preserve their relative paths under the target `.director/`.
README, INSTALL, and manifest guide the operation; they are not installed payload.
No maintainer rationale, user-source history, tests, private archive, repository
metadata, or authoring instructions belong in the target installation.

Read [PATTERN.md](PATTERN.md), [ROLES.md](ROLES.md), [MODELS.md](MODELS.md),
[STATE.md](STATE.md), and the fillable [PROJECT.md](PROJECT.md) as needed for setup.
The package depends on no files outside this subtree. Reading alone is not adoption; an adoption request
authorizes the reversible setup. Host restrictions and existing authority remain.

## Update an existing installation

Ask the project agent to resolve published GitHub `main` to an exact reviewed
commit and use that revision's [update protocol](references/UPDATES.md), including
when installed guidance requires an audit on every update or has no protocol.
Read installed guidance for local adaptations; preserve project-owned rules,
adaptations, and state. Routine changes use focused checks and still-applicable
evidence. Full startup audits and fresh-agent trials are triggered by affected
structure, behavior, or defects; only required checks gate the new revision. The
project's role index and definitions, model mapping, and identity roster belong to
the project; an update does not replace them. An update request is distinct from
reading the repository. While a project is active, only its checked Director
arranges a tiny metadata check at most once per 24 hours, including failures.
Default to: **A new Director Pattern is available. Say “update director pattern”
to install it.** The user can say **“always update director pattern”** to save
project-scoped automatic updates; notify/off remain durable choices. Automatic
mode follows the same safe backup, merge, compatibility and verification protocol.
No scheduler, checking model, dependency installation, or inactive-project wakeup
is added. See the [daily check contract](references/UPDATES.md#daily-discovery-and-project-preference).

## Remove a project installation

On an explicit removal request, identify unfinished requests, actual execution
handles, pending evaluation, and decisions with the recorder, then reconcile their
ownership and recovery pointers. Disable only the identifiable Director startup
hook, preserving unrelated instructions. Retain owned `.director/` state, context,
requests, and backups in place or archive them securely at an agreed reachable
location; do not delete state unless separately requested. Leave shared canonical
trackers untouched. Remove unused contract files only after preserving those records.
Removing files does not stop live agents or change their roles; refresh affected
conversations before claiming their instructions or roles have changed.

## Optional global skill

A separate optional skill routes explicitly requested lifecycle operations to this
guide. It requires explicit user invocation: `$director-pattern` in Codex,
`/director-pattern` in Claude Code, or a user direction to its skill file. Ordinary
task relevance must not select or run it. For the complete host-specific payload,
required native invocation controls, updates, and removal, see the repository's
[global skill guidance](https://github.com/bladnman/director_pattern/blob/main/README.md#optional-global-skill).
Preserve those controls on updates. Global skill invocation and an adopted
project's startup hook are separate instruction routes. Removing the global skill
does not remove any project's pattern installation. Project removal likewise
leaves the global skill installed unless its removal is requested too.
