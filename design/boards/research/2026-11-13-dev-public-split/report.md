# Should personal work live apart from the open-source repo?

Investigation · November 13, 2026

**Status**

| Item | State |
|---|---|
| Question | Answered: use a sibling workspace |
| Decision | Made by the maintainer, November 13, 2026 |
| Migration plan | Being prepared. Nothing has moved yet. |
| Open choices | Four, listed below |

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

**Proposal.** An exact migration plan is being prepared. Nothing has moved yet.

## Open choices

1. **Open.** Which tracked items stay public. The research boards are meant to be
   public distillations, so they may stay where they are.
2. **Open.** Where the large snapshot archive is backed up.
3. **Open.** When to migrate, relative to the 3.3 rollout that is still in flight.
4. **Open.** Whether to scrub public Git history. The default is no.

## Next

The accepted migration plan will be added to this board when it is ready. Earlier
findings stay visible next to any correction.
