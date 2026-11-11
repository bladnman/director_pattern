# Research and diagnosis

This board is the starting point for every research and diagnosis investigation
in this project. Start here, then open the investigation you need.

## The rule

Research and diagnosis work gets a durable, progressive Tinka report.

- **One investigation per child board.** Each investigation is one item on this board, and its own board holds the work.
- **Update it as findings land.** Corrections are part of the record. A finding that independent review revised stays visible next to its correction. It is not silently rewritten.
- **Two ways to read it.** A markdown report (`report.md`) you can clip through, and a paged telling (`slides.html`) you can step through section by section. Add rendered diagrams as separate items when they help.
- **Label what is known.** Separate facts, hypotheses, proposals, published changes and verified behaviour.

## Investigations

| Date | Investigation | Folder |
|---|---|---|
| 2026-11-10 | Making the system feel alive: original diagnosis, five reviewed chapter revisions and separate category ratings. Final delivery QA and owner creative acceptance remain open. | `2026-11-10-living-system-art/` |

## Public boundary

This folder is committed to a public repository. Distil findings into public
narrative. Keep raw conversations, session identifiers, transcript locations,
private store locators and personal paths in private evidence, outside this
folder. Paraphrase the owner rather than quoting him. Refer to repository files
by their public repo-relative paths. Describe capability tiers as strongest,
middle and lightest, never by model name.

## Opening it

Use the project Tinka service (see `../../../TINKA.md`), and open
`/boards/research/` on the printed URL's origin. Every page here is a local,
self-contained resource with no network dependency. To serve the folder without
Tinka, from the repository root:

```sh
python3 -m http.server 8878 --bind 127.0.0.1 --directory design/boards/research
```

Then open `http://127.0.0.1:8878/2026-11-10-living-system-art/slides.html`.
Stop that server when you are finished.
