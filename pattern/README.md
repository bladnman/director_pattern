# Install the Director Pattern

**First candidate · October 16, 2026.** This subtree is a self-contained package
for agents installing the method in a target project. It is not a proven adoption.

Give one project a director who discusses, decides, coordinates workers, evaluates
evidence, requests rework, and accepts the integrated outcome. The director is a
non-worker: workers execute; Small clerks map broad material; a Small recorder
handles routine state reading/writing. Selective critical reading and ordinary
discussion stay with the director. No department tree is required.

Tracked is the default for new installations; lean is an explicit optional choice.
Keep an existing tracker canonical. New bundled stores use request folders with
shared immutable user sources and typed relationship/ownership records. Files
preserve continuity, not agent liveness
or an automatic wakeup. No service, scheduler, or new chat is installed.

Periodic supervision overviews use **📋 SitRep** so they are easy to scan or skip.
Use one after a quiet stretch of ongoing work or when several developments benefit
from a combined view; ordinary replies and brief progress updates do not need a
full report. Meaningful ordinary updates satisfy the progress cadence without a
redundant SitRep. The checked director's `🎬` identity, `❓` questions, and `🖐️`
user-only actions keep their meanings. See [PATTERN.md](PATTERN.md) for the sparse
marker rules, timing, and continuing supervision requirements.

## Adopt in a target project

Ask the agent working in that project:

```text
Read this package's README.md and follow its INSTALL.md to install the candidate
Director Pattern in the target project. Preserve existing instructions, local
adaptations, unfinished work, and the canonical tracker. Copy only the selected
manifest payload, fill PROJECT.md from real context, and verify supported host
capabilities. Do not publish, migrate requests, or copy the whole source repository.
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

Read [PATTERN.md](PATTERN.md), [MODELS.md](MODELS.md), [STATE.md](STATE.md), and the
fillable [PROJECT.md](PROJECT.md) as needed for setup. The package depends on no
files outside this subtree. Reading alone is not adoption; an adoption request
authorizes the reversible setup. Host restrictions and existing authority remain.

## Update an existing installation

Ask the project agent to follow its installed [update protocol](references/UPDATES.md),
or this package's [INSTALL.md](INSTALL.md) when the older installation has none.
Use published GitHub `main` resolved to an exact reviewed commit, preserve local
adaptations and private state, and verify before recording the new revision.
An update request is distinct from reading the repository; startup does not silently
update an installation.

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

A separate optional skill routes lifecycle requests to this guide. For its
installation or removal, see the repository's
[global skill guidance](https://github.com/bladnman/director_pattern/blob/main/README.md#optional-global-skill).
Removing that global skill removes discovery through the skill; it does not remove
any project's pattern installation. Project removal likewise leaves the global
skill installed unless its removal is requested too.
