# Should personal work live apart from the open-source repo?

Investigation · November 13, 2026

**Status** (updated November 14, 2026)

| Item | State |
|---|---|
| Question | Answered: use a sibling workspace |
| Decision | Made by the maintainer, November 13, 2026 |
| Migration plan | Accepted, and approved by the maintainer on November 14, 2026 |
| Migration | In progress, starting with the workspace move |
| Open choices | One left: host settings for the dev workspace |

**Labels.** **Fact:** seen in a file, layout or record. **Decision:** chosen by the
maintainer. **Proposal:** a plan not yet carried out. **Open:** not yet decided.

## The question

Director Pattern is an open-source method, published from one public repository. The
same checkout also holds the maintainer's personal and exploratory work: a private
local Director installation, preserved snapshots, research boards and a local Tinka
setup. Should that personal work live in a separate place, the way Tinka keeps a
private dev workspace beside its public repository?

## How Tinka does it

- **Fact.** Tinka has two folders. A private dev workspace holds coordination: the
  producer store, redesign plans, design studies and boards.
- **Fact.** All app code lives only in the public `tinka` repository. Agents edit it in
  place, from the dev workspace.
- **Fact.** There is no second copy of the code and no "push changes to public" sync
  step. With one copy, nothing can drift.
- **Fact.** A planning tool created the dev workspace.

The private folder holds the thinking about the code. It never holds the code.

## Director Pattern today

- **Fact.** The private local installation and the preserved snapshots are git-ignored
  inside the public checkout. Because they are ignored, they are backed up nowhere. A
  fresh clone does not restore them, and a lost disk loses them.
- **Fact.** Some personal material is tracked in the public repository: the research
  boards, the local Tinka setup, and this checkout's own Director block in the root
  `AGENTS.md`.
- So the boundary runs through one folder, with ignore rules marking the private
  side. That keeps the private side out of Git, and it also keeps it out of every
  backup.

## Options considered

| | (A) Private dev copy | (B) Sibling workspace |
|---|---|---|
| Shape | Duplicate the folder into a private dev repo, add a rule: "push changes to public" | A private workspace beside the public repo, as Tinka does |
| Copies of the source | Two | One |
| Sync | A rule agents must remember | None needed |
| Drift risk | High: the copies diverge whenever the rule is forgotten | None for source: there is one copy |
| Private material | In the dev repo | In the sibling workspace, which can be backed up |

**Why (A) fails.** It creates two copies of the source and relies on a rule that agents
have to remember. Agents forget rules, especially after a compaction. When they do,
the copies drift and someone must reconcile them by hand.

**Why (B) holds.** There is one copy of the source, so there is nothing to sync. The
private coordination sits beside it in its own workspace, where it can have a real
backup.

## Decision

**Decision (maintainer, November 13, 2026).** Use the sibling model.

**Proposal (November 13).** An exact migration plan is being prepared. Nothing has moved yet.

**Update (November 14, 2026).** The plan was accepted, and the maintainer approved it.
The migration has started. It is summarised below.

## The accepted plan

**Decision (maintainer, November 14, 2026).** The migration plan is approved. Work is
in progress. This is a short summary of it.

### Target layout

- **The public repository** keeps the method: `pattern/`, `development/`, `site/`,
  `skill/` and the README. Its root `AGENTS.md` keeps only the maintainer rules and
  the Tinka pointer. The research boards and the local Tinka setup stay here. It
  holds no local Director installation. Its ignore rules stay as a guard against
  adding one back by accident.
- **A private sibling workspace** sits beside it. It holds the local Director
  installation and its request store, now tracked in a private repository. It holds
  the preserved originals, kept local-only. It has its own `AGENTS.md` with the
  Director block, and a check that both repositories are committed and pushed.
- **Every session starts in the sibling workspace.** Edits to the public method are
  made in place, in the public checkout. There is still one copy of the source.

### Steps

| Step | What happens |
|---|---|
| S0 | Preconditions: plan approved, no other session working in the public checkout, public `main` clean and equal to its remote. |
| S1 | Create the private sibling workspace. |
| S2 | Freeze and back up the local installation, with a checksum manifest. |
| S3 | Move the local installation and the originals into the sibling workspace. |
| S4 | Re-bind the installation there: its own startup entry, updated project settings, a new technical record, and the both-repositories check. |
| S5 | An independent worker verifies the sibling workspace before any push. |
| S6 | Create the private remote, confirm it is private, and push. |
| S7 | Clean the public checkout on a branch: remove this checkout's Director block, update the tests, remove merged leftovers. |
| S8 | Record a dated supersession in the rationale, with independent review. |
| S9 | Merge and push the public cleanup. |
| S10 | Run live trials in fresh sessions in both places, and record the results. |

### Decisions now made

| Decision | Date |
|---|---|
| Use a sibling workspace, not a private copy | November 13, 2026 |
| Exploratory boards stay public | November 14, 2026 |
| Originals stay local-only | November 14, 2026 |
| No rewrite of public Git history | November 14, 2026 |
| Finished work is committed and pushed, unless the maintainer says not to | November 14, 2026 |

**Open.** Host settings for the dev workspace.

## Open choices (as of November 13), now decided

The four choices below were open on November 13. Each original note is kept, with
its decision beside it.

1. **Was open.** Which tracked items stay public. The research boards are meant to be
   public distillations, so they may stay where they are.
   **Decided (November 14, 2026).** The exploratory boards stay public.
2. **Was open.** Where the large snapshot archive is backed up.
   **Decided (November 14, 2026).** The originals stay local-only. They move into the
   sibling workspace but are not committed to either repository.
3. **Was open.** When to migrate, relative to the 3.3 rollout that is still in flight.
   **Decided (November 14, 2026).** Migrate now. The plan was approved and work has
   started with the workspace move.
4. **Was open.** Whether to scrub public Git history. The default is no.
   **Decided (November 14, 2026).** No history rewrite. Cleanup moves forward only.

## Next

The migration is in progress, starting with the workspace move. Results will be
added to this board as steps finish. Earlier findings stay visible next to any
correction.

**Earlier text (November 13).** "The accepted migration plan will be added to this
board when it is ready." It was added on November 14, above.
