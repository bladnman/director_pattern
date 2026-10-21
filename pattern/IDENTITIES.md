# Names and scannable identities

First candidate. Identity is not status, model tier, role, or authority.

The assigner supplies a meaningful display name and a unique marker, for example
`🐙 Contract —`. The actor prefixes human-facing progress and returns with that
identity; parent summaries preserve it. Keep the identity stable across a resumed
assignment even when its runtime attempt changes. This is a text convention, not a
claim that the host can set native chat icons.

The checked project [Director](DIRECTOR.md) keeps the `🎬` installation and role
badge under [PATTERN.md](PATTERN.md). Request Managers and other bounded actors,
including child directors, use their assigned identity instead. A marker never
grants role or authority.

The optional package pool is [IDENTITY_POOL.txt](IDENTITY_POOL.txt). It is a
candidate list, **not a live roster**. An adopting project may replace it or use
distinct text labels. Never allocate these reserved symbols, including equivalent
rendered variants: `🎬`, `📋`, `❓`, `🖐️`. Their existing meanings stay intact.

## One shared allocation route

Directors and managers use the **same Recorder-maintained active/recent roster and
rotation cursor**. It can be a small table in current activity, with the root
serializing requests within one task. Do not copy the list into local histories and
rotate independently. Managers request reservations through the permitted
[Recorder](RECORDER.md) route: directly only where supported, otherwise through
their assigner. This is coordinated responsibility, not a new identity service.

1. Ask the Recorder to reserve an available marker and name for a stable assignment
   identity, before dispatch. Skip allocated, reserved, or still-reporting markers.
   Advance the shared cursor with the reservation receipt.
2. Dispatch with that identity and the normal bounded assignment. Bind the actual
   returned handle or attempt to the reservation through the Recorder. A reservation
   alone is not proof of dispatch or liveness.
3. Retain the identity while the actor is executing, waiting on required work or
   review, resumed, or likely to send pending reports. Retries and parent summaries
   do not silently rename it.
4. Release only after the assignment is accepted or retired and no competing live or
   reporting actor, or likely pending return, can be confused with a new one. Keep
   recent retirement history where it avoids late-message ambiguity.

If the pool is exhausted, reserve a distinct additional glyph or an explicit unique
text label such as `Contract 17`. Do not reuse a marker for competing live or
reporting actors. If allocation is unavailable, resolve it through the shared route
or choose an explicitly unique text reservation under the same authority; do not
start another independent identity service.

The roster needs assignment identity, display name and marker, reservation state,
actual handle/attempt binding, pending-report/review state, retirement or release
evidence, and one rotation cursor. It is private project state: never package a live
roster, and never let an initialized roster or cursor overwrite current state.
