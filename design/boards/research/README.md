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
| 2026-11-07 | Why the Director ran everything at full strength, and stopped being a steward | `2026-11-07-staffing-and-stewardship/` |
| 2026-11-07 | Where the Director Pattern should live after compaction: scale, surfaces, architecture. 2026-11-09: proposed Director slug and layout (brief.md, slug-draft.md); independent second pass (second-pass.md). 2026-11-10: route, card triggers and trial clarification (`clarity-20261110/`). | `2026-11-07-startup-architecture/` |
| 2026-11-08 | How the Director Pattern installs into a video project (draft, corrected after independent review) | `2026-11-08-installation/` |
| 2026-11-10 | Making the system feel alive: original diagnosis, five reviewed chapter revisions and separate category ratings. Final delivery QA and owner creative acceptance remain open. | `2026-11-10-living-system-art/` |
| 2026-11-13 | Why a Director never proposes a role for recurring work, lets a specialist's call drift to itself, and treats every recorded step as fixed. Diagnosis accepted; implemented as starter 3.4 (static tests only); independent review accepted after findings were applied; maintainer acceptance, publication and installation pending. | `2026-11-13-recurring-work-and-roles/` |
| 2026-11-13 | Should personal and exploratory work live apart from the open-source repo, as Tinka's dev and public pair does? Decision: a sibling workspace. Migration plan in preparation; nothing has moved yet; four choices open. | `2026-11-13-dev-public-split/` |

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

Then open `http://127.0.0.1:8878/2026-11-07-staffing-and-stewardship/slides.html`.
Stop that server when you are finished.
