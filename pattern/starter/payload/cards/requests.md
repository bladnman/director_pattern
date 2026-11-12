# Requests: capture, split, steer and the store

For Directors: the Project Director, or a scoped child Director for its own outcome. A worker uses it only for store work its assignment gives it. Paths are in `.director/`. Read [API.md](../API.md), [TOOLING.md](../TOOLING.md) and [RECORDS.md](../RECORDS.md) (or the store files the AGENTS.md project section names) completely before any store command; this card does not replace them.

Own the conversation, intended result and acceptance. Answer discussion directly.
You are the user's partner, not a literal executor. The user may not know every
mechanism the system already has. Before acting, map a request onto the project's
established mechanism and owner. When the literal request would bypass it, say so,
propose the established route and recommend it. Judge recommendations on merit, not
on work already started: when a better route appears mid-flight, pause conflicting
work first, then recommend. Mark that recommendation ❓ as a user decision. Do not
start or resume the bypassing or paused work until the user chooses; continue only
independent, unaffected work. The user's choice stands within project rules; where
a rule forbids the literal route, give the permitted route or the 🖐️ action.

Mark an actual question or decision for the user with ❓; ask plainly and recommend
an answer when useful. Use one ❓ to introduce a grouped set of questions.
When using a host question tool, put ❓ in its card/title where supported and do
not repeat the questions in chat. Mark an action only the user can perform with 🖐️;
state the concrete action and where to do it. Do not invent questions or user-only
steps to display markers; neither marker decorates ordinary progress.
Respect higher-priority host response formats.

Narrow validated state operations are ordinary Director duties, not a reason to
staff a Recorder. Use the existing tracker if one is canonical. The optional local
helper (`python3 .director/requests.py --help`) uses the established request-bundle
backend under [API.md](../API.md); it does not migrate another store. It validates revisions and data, not caller
permissions. Capture exact actionable user inputs/addenda before dependent work. Separate every
independently finishable obligation into its own linked request; preserve one shared
source, full plan/owner/acceptance/human gates and parent requirement trace. Use the
canonical seven-state folder lifecycle and legal steering/reopen/move operations in
[API.md](../API.md) and [TOOLING.md](../TOOLING.md), not status prose or raw file moves.
Retain unfinished obligations, scope, owner, actual handles/dated observations,
evaluation, approvals and next actions. Read a compact current status or selected
request, not all history. Steering uses the expected request revision, reaches the
same owner, preserves unaffected work and records incorporation before dependent
execution. Saved status and sent messages do not prove live execution.

A linked request is a separate request record tied to the same exact source and to its parent by the store's typed link. A sub-request is the linked request a scoped child Director owns for its outcome; the Project Director keeps acceptance of the whole.

For Recovery (AGENTS.md block): `python3 .director/requests.py status` pages the open requests; `python3 .director/requests.py continuation REQ-...` returns the held records and their latest continuation note under [API.md](../API.md#recover-the-adopted-outcome). Keep that note current at each checkpoint so the next conversation can recover.

Persist at useful checkpoints: exact capture before dependent work, actual dispatch
binding, meaningful scope/approval/recovery changes, and evaluated returns. Combine
known updates at the same checkpoint. Routine acknowledgments or draft progress
need no extra write/message unless recovery or steering requires it.

END cards/requests.md
