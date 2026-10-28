# Request storage alternatives

Design decision · October 16, 2026. The candidate uses one folder per actionable
request, with separately preserved exact user-source bundles. This comparison
explains the general alternatives and the reasons for that choice. The current
[record contract](../pattern/engine/references/RECORDS.md) and
[CLI reference](../pattern/engine/references/TOOLING.md) define actual behavior.

## Alternatives

| Concern | Stable flat records | Moving task files | Moving request folders |
|---|---|---|---|
| Canonical request | One file at a stable path; lifecycle is metadata. | One file moves between lifecycle locations. | One directory moves between lifecycle locations, with one canonical request record inside. |
| Local assets/evidence | Usually separate paths linked from the record. | Usually separate paths that do not travel with the task file. | Local assets/evidence travel with the request directory. |
| Exact user source | Can be embedded or linked; shared source needs an explicit identity. | Can link a separate shared source bundle. | Links a separate shared source bundle without duplicating the original. |
| Path stability | Simple stable record paths. | Resolve IDs after each move. | Resolve IDs after each move; request-local relative paths remain useful. |
| Consistency burden | Protect record updates and referenced material. | Protect file moves, state metadata, and separate material. | Protect directory moves, record updates, and newly captured local material. |
| Large outputs | Reference established canonical locations. | Reference established canonical locations. | Reference established canonical locations; avoid copying large outputs into every request. |
| Relationships | Typed links can represent dependencies and grouping. | Typed links can represent dependencies and grouping. | Typed links can represent dependencies and grouping without physical nesting. |

No layout alone supplies revision protection, idempotency, truthful acceptance,
agent supervision, or transport. Those need explicit contracts and implementation.
A stable-file design is reasonable when linked material has independent custody.
A moving task file is useful when location communicates lifecycle and local assets
are rare. Request folders are useful when request-specific research and evidence
should stay together through state changes and restart.

## Selected design

Use separate source and request identities. Capture a complete exact original
once, preserve original attachments with byte hashes, and link independently
finishable outcomes to it. Later steering is another immutable source linked in
order; it does not replace the original words.

Each request has one canonical `request.md` inside an ID-named folder. Seven states
map to pending, working, and archive containers. Assets and evidence appear only
as needed. Folder location and metadata must agree; resolve the ID each time
rather than treating a previous path as permanent identity.

The physical layout stays flat. Common source, grouping, decomposition, required
completion dependencies, and external ownership carry different meanings. Only
explicit required dependencies gate acceptance. Peer projects own their own
execution records; a source retains its commitment and acceptance authority.
See the [relationship design](REQUEST_RELATIONSHIPS.md).

## Safeguards and tradeoffs

A move plus record replacement is not a multi-file atomic operation. The helper
uses a cooperating writer lock, expected revisions, retry identities, replayable
history, and a write-ahead intent. Recovery finishes validated local mutations;
collisions or uncertain content are preserved and rejected. Read-only commands
report pending recovery without silently repairing it.

Separately stored shared originals mean a request folder is not a standalone
export. Stable source IDs and file receipts preserve provenance; large outputs
still rely on their referenced canonical locations. Supplied observations and
receipts do not establish current liveness or authenticated remote status.

The selected implementation does not silently migrate legacy flat JSON stores.
Validation evidence lives in [DESIGN_NOTES.md](DESIGN_NOTES.md). Revisit this choice
if concrete preservation, recovery, dependency, or ownership cases cannot be
represented safely; retain the independent-outcome and exact-source requirements.
