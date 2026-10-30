# Names and scannable identities

First candidate. Identity is not status, model tier, role, or authority.

The assigner supplies a short, memorable, Capitalized name and a unique marker.
Bold the name in human-facing output, for example 🦫 **Cutter** —. The actor prefixes
progress and returns with that identity. All parent, Director, and manager summaries,
including SitReps, retain the assigned emoji and **bold name** as well. Keep the
identity stable across a resumed assignment even when its runtime attempt changes.
This is a text convention, not a
claim that the host can set native chat icons.

The checked project [Director](DIRECTOR.md) keeps the `🎬` installation and role
badge under [DIRECTION.md](DIRECTION.md). Request Managers and other bounded actors,
including child directors, use their assigned identity instead. A marker never
grants role or authority.

The optional package pool is [IDENTITY_POOL.txt](../IDENTITY_POOL.txt). It is a
candidate list, **not a live roster**. An adopting project may replace it or use
distinct text labels. Never allocate these reserved symbols, including equivalent
rendered variants: `🎬`, `📋`, `❓`, `🖐️`. Their existing meanings stay intact.

## Choose a character that fits the work

Use playful semantic fit rather than an arbitrary next glyph. Animals, plants,
tools, buildings, and other characters can suggest the assignment without encoding
a fixed role, model tier, status, or authority. Affinities are soft and overlapping:
a beaver might build as **Mason** or edit as **Cutter**; a crab could also be
**Cutter**. A tree or flower might suit design as **Willow** or **Bloom**; an owl
could read files or email as **Scout**; a parrot might notify as **Piper**; a raccoon
or broom might clean up as **Tidy** or **Sweep**; a feather might record as **Quill**.
A tool might build as **Forge**. These are suggestions, not required pairings or an
allocation table. Choose naturally for generalized work too; do not force every
assignment into a category.

Semantic fit guides the choice; availability and rotation resolve suitable options.
Use one pool, one active/recent roster, and one cursor, never independent pools or
cursors per affinity. Preserve project-owned pool customization on update. Identity
guidance adds no runtime service or record schema.

## One shared allocation route

Directors and managers use the **same Recorder-maintained active/recent roster and
rotation cursor**. It can be a small table in current activity, with the root
serializing requests within one task. Do not copy the list into local histories and
rotate independently. Managers request reservations through the permitted
[Recorder](RECORDER.md) route: directly only where supported, otherwise through
their assigner. This is coordinated responsibility, not a new identity service.
Reserve several known assignments in one request and bind a dispatch wave's
returned handles in one update when practical. Serialize allocation against the
same roster/cursor and return each reservation before its dispatch; batching
never relaxes collision, authority or late-return protection.

1. Identify suitable candidates for the assignment, then ask the Recorder to reserve
   an available marker and name before dispatch. Skip reserved symbols and any marker
   or name held by an unreleased reservation or live, reviewing, or still-reporting
   actor; account for
   equivalent rendered glyph variants and names differing only in capitalization.
   Starting at the shared cursor, rotate among suitable available candidates in the
   single pool; advance that cursor past the chosen marker with the reservation
   receipt. Do not take an ill-fitting glyph just because it is next in the list.
2. Dispatch with that identity and the normal bounded assignment. Bind the actual
   returned handle or attempt to the reservation through the Recorder. A reservation
   alone is not proof of dispatch or liveness.
3. Retain the identity while the actor is executing, waiting on required work or
   review, resumed, or likely to send pending reports. Retries and parent summaries
   do not silently rename it.
4. Release only after the assignment is accepted or retired and no competing live or
   reporting actor, or likely pending return, can be confused with a new one. Keep
   recent retirement history where it avoids late-message ambiguity.

If no preferred candidate is available, broaden the affinity to a sensible available
character. If the pool is exhausted or has no sensible fit, reserve a distinct
additional glyph or an explicit unique text label such as `Scout 17`. Do not reuse
a marker or name for competing live or reporting actors. If allocation is
unavailable, resolve it through the shared route
or choose an explicitly unique text reservation under the same authority; do not
start another independent identity service.

The roster needs assignment identity, display name and marker, reservation state,
actual handle/attempt binding, pending-report/review state, retirement or release
evidence, and one rotation cursor. It is project state: never package a live
roster, and never let an initialized roster or cursor overwrite current state.
