# Update check and updates

For the Project Director (daily discovery), and for any Director before discussing or planning a Director Pattern update. No worker, scoped child Director or global skill starts these checks. Paths are in `.director/`.

## Who may update what

Before planning any Director Pattern update, in this or another project, read
[UPDATES](../UPDATES.md) completely; another installation is updated only by its own
project's Director (or, without a working one, an agent the user directs there) in its own
conversation. Never patch another installation's files from outside. To get another project updated, start a session there with "update director pattern" only when the user asked for that update, or give the user the 🖐️ action to do so, then follow its reports.

## Daily discovery

During active sessions arrange due daily metadata discovery and
honor notify/automatic/off preferences under [UPDATES.md](../UPDATES.md); do not add a
checking actor, daemon or claim an unexecuted check/update.

- When: the startup check's `update_check` value is `due` (no attempt recorded in the last 24 hours) and you begin project work. A greeting or discussion never triggers it, and it never delays the first reply. `not_due` and `off` need no action; on `unknown`, run the command once in the conversation.
- Run it yourself or through a supported background route, with this project's exact accepted receipt (a fresh install uses `.director/install.json`); never pick the newest receipt by name or date:

```sh
python3 .director/update_check.py --root .director check --receipt .director/install.json
```

- It makes at most three bounded metadata reads, fetches and runs no code, and throttles itself: `throttled`, `current`, `off` and `busy` need no action. Keep its `next_check_at` in view so later turns skip it.
- `available` with `action: "notify"`: tell the user once, exactly: **A new Director Pattern is available. Say “update director pattern” to install it.** Do not repeat it on later turns.
- `available` with `action: "request_safe_update"`: the user chose automatic. That is a pending safe update, not an applied one: read all of UPDATES.md, then run its protocol at the pinned `upstream_sha`.
- `error`: note it once; do not retry each turn or delay the user's work. If the runtime or network is unavailable, say so; never claim a check that did not run.
- Preferences, saved with the same helper's `set-policy` and the user's source reference: “always update director pattern” saves **automatic** (standing authorization, no extra confirmation); “notify me instead” saves **notify**; “stop checking for updates” saves **off**. A later explicit update request still works with checks off.

For anything else here (the cache, the receipt format, provenance gaps), read UPDATES.md.

END cards/update-check.md
