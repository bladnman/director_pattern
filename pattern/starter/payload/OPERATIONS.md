# Check, hook and budget reference — deferred action reference

Read this before changing the check command, the hook source or how this project's
instructions load, and when a failed check names a hook, receipt, source or backend
gap. What 🎬 claims and how to handle a failed check are in
[cards/badge.md](cards/badge.md); staffing is in [cards/staffing.md](cards/staffing.md);
privacy is in [cards/privacy.md](cards/privacy.md).

## Installation evidence

If this project's reviewed integration selects generated-project
first use, its generator instance evidence is present and its expected setup receipt
is absent, completely load [FIRST_USE](FIRST_USE.md) and its full selected native
canonical I/O/privacy prerequisites before any setup writes. Follow its guarded
`ensure` route before the ordinary check: it requires actual generator INSTANCE
evidence bound to selected transport provenance, not merely a missing receipt.
Generic seeds and arbitrary missing/damaged setup evidence grant no initialization
authority; existing configured projects retain their backend/identity and ordinary
read-only route. A first-use failure gives its specific gap, not a fabricated receipt
or repeated initialization. Successful setup earns no badge by itself.
Then run the concrete local command (fresh starter installation):

```sh
python3 .director/startup_check.py
```

It reads only the exact `.director/install.json` provenance, the installed
WORKER/OPERATIONS/card/checker baselines, current AGENTS and explicit selected
project guards, a bounded config header and the local update-check cache. It imports
no tracker, scans no requests/sources/history, makes no
network request and writes nothing. Read-only technical config/receipt/hash
inspection is distinct from canonical request/source/history I/O; it does not
activate TOOLING/RECORDS, learning or a new persistence step. Those protocols remain
mandatory before their actual operations. Hold this check's output in active
context; record it later only at an ordinary authorized checkpoint. Reuse unchanged
current-conversation facts; relevant changed startup bytes require recheck, and so do
facts from before a compaction or session resume.

Its output adds `next` (what to do and read next), `update_check` (`due`, `not_due`,
`off` or `unknown`, from the local cache only), `director_block` (`unchanged`
against the receipt's `director_block_sha256`) and
`project_section` (its bytes and the 3,000-byte cap). A block that differs from its
recorded baseline blocks the check, because the block is managed text, and so does a
receipt with no recorded baseline: the installer, first use and the UPDATES move each record it.

A mature project supplies its exact reviewed command in the AGENTS.md project
section, for example:

```sh
python3 .director/startup_check.py --root .director --receipt .director/SOURCE.json --config .producer/config.json --guard .director/PROJECT.md --guard .director/CAPABILITY_POLICY.md
```

Receipt `managed`, `managed_files` or `installed_files` baselines may be maps of
project-relative paths to SHA256 (or `{sha256:...}`), or a managed_files list of
`{path,installed_sha256}`. The managed startup artifacts require known, matching
hashes: WORKER.md, OPERATIONS.md, startup_check.py, the START.md and DIRECTOR.md
redirect stubs and the seven cards
(`cards/staffing.md`, `requests.md`, `supervision.md`, `knowledge.md`,
`update-check.md`, `privacy.md`, `badge.md`). AGENTS and explicitly selected
project-owned guards are composed
current instructions: fully read them and evaluate their authority and compatibility.
Their saved hashes describe historical snapshots. The helper reports each snapshot
as `unchanged`, `changed` or `not_recorded`; changed or absent project snapshots alone
do not block the check. Malformed or conflicting recorded baselines still block.
Never rewrite a receipt merely to silence drift or select it by filename recency.
The source needs canonical
URL/full SHA and truthful published boolean; an unpublished verified candidate can
be checked without being promoted to published. Missing/unsafe/symlink/oversized
files, unreadable project text or unknown provenance block the check. Generated template transport provenance is not
a configured installation receipt.

The helper supports one standalone marked block: `director-starter:2` with
`/director-starter:2`, or `director-pattern:start` with `director-pattern:end`.
It requires exactly one ordered pair outside Markdown code blocks and, inside it, a
reference to the selected installation's WORKER.md. The same file must also hold
exactly one ordered `director-project` / `/director-project` pair, the project-owned
section; without it the gap is `project section missing`. The section must hold a
`- Check command:` line and stay within 3,000 bytes, or the check blocks. Missing, duplicate,
malformed or unsupported structure gives a specific route gap. This checks structure
only; it does not prove which entrypoint the host loaded or what the prose means.

A block that instead references the installation's START.md is the earlier route.
It still passes while START.md, DIRECTOR.md, OPERATIONS.md and the checker match
their recorded baselines and START.md is the earlier full startup file. Once
START.md is the redirect stub, that block routes nowhere: the check blocks and names
the unfinished update ([UPDATES.md](UPDATES.md), "Move to the AGENTS.md block").

The marked block defaults to AGENTS.md. When an actual project entrypoint imports a
shared file containing it, explicitly select that project-relative file:

```sh
python3 .director/startup_check.py --hook-source docs/assistant_instructions.md --guard CLAUDE.md
```

Use the project's actual receipt/backend arguments too. The helper always reads
outer AGENTS and additionally reads the exact selected hook source; it does not
search for a passing hook elsewhere. Include other actual host entrypoints and
shared/role authority as selected project guards. Fully read and evaluate the real
host import chain: unused matching files cannot substitute for the active route.
A different hook structure needs a reviewed supported integration, not a fabricated
pass. All selected files retain the same safety and total read bounds.

Lean/custom backends need no generic JSON store. An explicitly already-read
project declaration can instead bind `--backend-contract <maintained-project-path>`;
the helper safely reads its current text and reports its snapshot. The actor must
resolve its actual route/constraints. Unknown backend or absent required provenance is still
a gap. Do not use this option to bypass required configuration, initialize a
backend or certify an unconfigured template. Add any actual
selected backend/authority files as bounded `--guard` paths when required.

## Optional context-budget preflight

At installation, update or a changed host instruction route, use the optional
read-only calculator when a byte-budget check is useful:

```sh
python3 .director/context_check.py --root /path/to/project --spec /path/to/selected-chain.json --max-output-bytes 12000
```

Supply a schema-1 spec with `chain` (ordered unique project-relative paths and
`required_through_bytes` boundaries), `cap` (`bytes` and `provenance`), and `evidence`
(the actual host-route/cap evidence locator). Resolve the host's real discovery,
overrides and counted inputs first; the helper does not discover the chain.
Use provenance `effective`, `default` or `unknown`: effective is caller-declared
evidence, default gives only a conditional prediction, and unknown ignores any
numeric cap. A boundary is a raw-byte prefix length, or null when none is asserted.
The report counts/hashes the selected raw files without printing their bodies.
Inspect both total fit and required-boundary fit; a later required pointer can be
cut or omitted even when an earlier one fits. Aggregate boundary fit covers only
positive caller assertions; null/zero boundaries establish no required coverage.
Missing/unsafe inputs fail visibly.
Every report keeps `actual_admission:unqualified`; it proves neither received text,
consumption nor compaction restoration. This action reference adds no first-reply
check, new configuration registry or host-setting change. Preserve the existing
complete-read and truncation-recovery duties.

For the AGENTS.md route, list AGENTS.md first with `required_through_bytes` at the
end of the `/director-starter:2` marker line, so a cut that would reach the Director
block is visible. Keep the block first in its file.

END OPERATIONS.md
