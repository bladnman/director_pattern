# Project startup bridge — interface 1

Canonical role index: <installation fills the single project-owned index locator>
Engine bootstrap: [engine/PATTERN.md](engine/PATTERN.md)
Project context: [PROJECT.md](PROJECT.md)

This bridge is project-owned. Preserve its canonical index and required project
references when replacing the engine. Do not put role tables or runtime snapshots
here. The engine and this bridge use startup interface 1; an incompatible interface
requires reviewed integration before replacement.

Your first tool invocation reads only this file. Wait for and read its result.
In the next startup-only invocation read the engine bootstrap above; wait for and
read its result before following the canonical role index named here. Complete the
engine's startup sequence and acknowledge the selected role package before any
task I/O, planning, delegation, changes, or substantive answer. No substantive
answer or read-only task bypasses these returned-result dependencies.
