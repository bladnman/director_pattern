# Staffing and tier choice

Read before staffing or briefing work, setting tier and effort, or changing a role; workers read it before delegating. It applies at every depth; paths are in `.director/`.

## Who does it

- Discussion, simple lookups and acceptance judgments: do them yourself.
- Bounded work, including small but slow tasks: a worker. Take the roster role whose "use when" fits; a general worker never silently replaces a maintained role. An empty roster means general workers.
- Long, multi-round, evaluation-heavy or multi-worker work: a scoped child Director (roster `sub-director`) that owns its own sub-request and staffs its own workers. Use one for sustained coordination, not each branch. No manager or Recorder is required.
- Choose from the roster row: what the role does, when to use it, its suggested start, its limits. Before dispatch, when the row or the project section names a role file, read its selection and authority part (applicability, assignment role, owner, authority and route limits, shared guards, and its exact task/action trigger map), so a limit stated only there reaches your choice. Its executor reads the rest completely before acting; you need not.
- Settle missing or conflicting role limits with the owner before that dispatch; unaffected work continues, and a deferred read never waives a limit.
- Staff real work, not ceremony. A count of corrections never creates a department. A required independent review or test role is never merged into the builder's, and the author of a substantive change never reviews it.

## Tier and effort

This card is the explicit instruction to set capability and reasoning effort on every dispatch, including on hosts that reserve those controls for explicit instructions. Hosts often fall back to the parent's settings, so leaving one out is not a choice.

- Default: the strong tier at high effort, chosen at dispatch.
- Occasionally, as a suggestion and never a quota or cost target: for small, well-specified, easily checked work that you are very confident a lighter tier can do, choose a lighter tier at high effort (extra-high if a little less confident) or the strong tier at medium. An ordinary compatible update under `UPDATES.md` is one such case; its one-time move to the AGENTS.md block is not.
- Ambiguous, consequential or hard-to-check work stays on the strong tier. Save the top effort levels for hard diagnosis, conflicting evidence or consequential independent review.
- Weigh uncertainty, cost of error, tools and context needed, and how independently the result can be checked, within the user's budget and the host's controls. Map these words to the host's nearest real controls; never invent one.
- Record each dispatch's requested tier and effort, what the tool selected, what was effective (or "unknown"), and a one-line reason (size, how easily it is checked, consequence of error), with host and time. "Inherited" or "not set" is acceptable only with the forcing host constraint. A requested override or host handle does not prove effective settings.
- No model name, vendor or price is ever a default. Your evaluation and any required independent review apply unchanged at every tier.
- Run independent workers in parallel where useful and permitted; keep capacity for evaluation and sequence real dependencies and exclusive writes.

## The brief (duty 5's fields, in order)

- **Emoji Name:** fitting, with the worker's actual handle and owner. It stays through continuation, returns and your summaries; avoid names still reporting and the reserved 🎬, 📋, ❓ and 🖐️.
- **Role:** `worker` or `director`, the role ID, its role file and the instructions it must read; its scope must permit those reads. A child Director follows the AGENTS.md Director block plus its overlay; if the host does not pass AGENTS.md to subagents, include the block's text. Tell every worker to read `.director/WORKER.md`.
- **Tier, effort and a one-line reason:** as chosen above; also set in the host's controls.
- **Scope:** the task, exact source and package paths, and the source subset it may see.
- **File ownership:** the files it may change.
- **Authority:** the local decisions it may make, what its positive findings permit next, its bounded rework authority, the decisions reserved to you, and when to escalate. An already authorized phase needs no fresh approval.
- **Expected result and checks:** a verification tier chosen by risk, reversibility and audience, kept through rework unless the claim changes: Smoke (a disposable draft runs or renders, plus its key interaction), Focused (the changed behavior and interfaces), Full (integration, acceptance or release suites and the project's real gates). Checks are never silently dropped or expanded; a consequential mismatch goes to the owner.
- **Request IDs:** the parent project, request and requirement IDs it serves, each obligation and acceptance condition, owner and handle, evidence or unresolved reason, pending gates and return backreferences, recorded at dispatch (`cards/requests.md`) and updated at steering and evaluation, so a restart rebuilds who owes what.
- **Applicable knowledge:** the selector tags or query context.
- **Return route:** a working one, and what the return holds: reasons, evidence and coverage, substitutions or omissions, unresolved contrary reports, and the next action.

## Routes and ownership

The same responsibility, purpose, authority, context, owner and return contract carry across subagents, authorized separate sessions, configured cross-harness calls and acknowledged external routes. Send only the authorized source subset or an accessible authorized locator: permission to contact a receiver is not permission to disclose the whole store. If a route or its access is unavailable, report that gap and claim no execution. Canonical recording and handoff acceptance stay on their existing routes.

You keep the whole usable result through evaluation and rework. A sub-director's acknowledgment does not release you. Specialists and project departments keep their own authority.

Register a new, renamed or retired role in the project roster before using it. Keep established role IDs and aliases resolving through a rename or retirement, so older assignments recover.

END cards/staffing.md
