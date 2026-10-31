# Select a Director Pattern installation

For a **new project**, including one with ordinary meeting notes/assets but no
conflicting startup/tracker, follow [starter 2](starter/README.md). Its stdlib
installer plans, measures, installs and safely rolls back the separately manifested
flat starter. It performs no network/dependency-manager operation. Current local
helper requires POSIX `fcntl`; unsupported hosts fail with guidance.

For an **existing v1 engine installation**, use the preserved
[v1 guide](INSTALL-v1.md) and [compatible update protocol](engine/references/UPDATES.md).
The legacy [manifest](manifest.json) and interface-1 engine remain unchanged.
Resolve the exact installed format before choosing payload. Existing trackers,
project policy, private data and local roles stay authoritative; no automatic
format migration, starter overwrite or mature-stencil synchronization is authorized.

For an existing conflicting startup or another tracker, stop automatic installation
and prepare reviewed integration with backups and exact authority preservation.
The starter installer deliberately refuses these cases. Removal/update authority
is separate from reading a guide; preserve unfinished work and exact history.
