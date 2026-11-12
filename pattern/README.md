# Director Pattern packages

**New projects: [flat starter 3](starter/README.md).** This source candidate uses one
Project Director and bounded workers, with a small install and explicit bounded
learning review. It is a new format, not an automatic v1 upgrade or a published
release claim. Ordinary notes/assets may already exist; conflicting startup or
tracker installations require reviewed integration.

From starter revision 3.3 the installer writes two things into the project's
AGENTS.md: a managed Director block (the role gate, the Director's every-turn duties,
the first-reply check, the recovery steps and the read rules) and, below it, a
project-owned settings section (check command, guard files, roster). Detail sits on
seven cards in `.director/cards/`, each read before the action the block names;
workers read `.director/WORKER.md`. `.director/START.md` and `.director/DIRECTOR.md`
remain only as redirect stubs. The block's source is
[starter/agents/block.md](starter/agents/block.md); it is installer input, not
payload. An installation at revision 3.2 or earlier does not get this by reinstalling:
it moves through its own reviewed update, under
[UPDATES](starter/payload/UPDATES.md), "Move to the AGENTS.md block".

```sh
python3 pattern/starter/install.py plan --target /path/to/project
python3 pattern/starter/install.py install --target /path/to/project
```

Only the starter manifest, the Director block and the project section are selected
for that operation. Its source guides and installer are not startup payload. Its portable role guidance and POSIX local
helper have separate limits; see its guide for exact runtime prerequisites,
reversal, privacy, pending review and actual-host verification boundaries.

**Existing v1 projects: [legacy v1 guide](README-v1.md), [installation guide](INSTALL-v1.md)
and [compatible update protocol](engine/references/UPDATES.md).** The existing
[manifest](manifest.json), engine, launchers and project seed layout remain the
legacy interface-1 package. Published v1.1.0 and current source candidate starter 3
are distinct. Read actual installed policy, preserve project-owned rules, requests,
trackers and identities, and use pinned source/baseline comparison for compatible
v1 updates. Do not copy starter 3 over an existing v1 installation or mature stencil.
A new format requires an explicit reviewed migration; none is implemented here.

Use [INSTALL.md](INSTALL.md) to select the appropriate lifecycle route. No repository
history, tests, private conversations or authoring instructions belong in either
runtime payload. No source guide itself confers installation or release authority.
