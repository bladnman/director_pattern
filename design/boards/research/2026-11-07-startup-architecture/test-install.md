# Test install: from today's starter to the candidate

**Recipe for a throwaway live test, 2026-11-09.** Not a release, update or migration route. Every step below is a file operation inside the test folder; nothing in this repository changes. Steps 1 to 7 and the variant in step 8 were dry-run in a scratch folder on 2026-11-09, and the expected outputs quoted below are the ones observed.

**Inputs from this folder:**
- `slug-draft.md`: its first four-backtick `markdown` fence holds the candidate block (6,303 bytes) and its second fence holds the project section (905 bytes).
- `cards/`: eight files, each ending with its END line.

**Control run:** steps 0 to 2 only. **Candidate run:** steps 0 to 9, in a fresh folder.

## Steps

**0. Folder.** Create an empty folder `T` outside any Git repository.

**1. Install today's starter.** From this repository's root:

```sh
python3 pattern/starter/install.py install --target T
```

This writes `T/AGENTS.md` (today's 1,190-byte bridge only) and `T/.director/` (the starter payload, `config.json` and `install.json`).

**2. Check the control.**

```sh
cd T && python3 .director/startup_check.py
```

Expected: `"status":"evidence_matched"`. The control run stops here.

**3. Replace `T/AGENTS.md` completely** with exactly the following, in order:
1. the candidate block, copied byte for byte from `slug-draft.md`'s first fence, from `<!-- director-starter:2 -->` through `<!-- /director-starter:2 -->` and its newline;
2. one empty line;
3. the project section, copied byte for byte from the second fence, from `<!-- director-project -->` through `<!-- /director-project -->` and its newline.

Nothing else goes in the file. Expected size: 7,209 bytes.

**4. Cards.** Create `T/.director/cards/` and copy these eight files into it, unchanged, from this folder's `cards/`:
- `badge.md`
- `knowledge.md`
- `privacy.md`
- `recovery.md`
- `requests.md`
- `staffing.md`
- `supervision.md`
- `update-check.md`

**5. END lines on seven manuals.** For each `M` in `WORKER.md`, `API.md`, `TOOLING.md`, `RECORDS.md`, `LEARNING.md`, `UPDATES.md` and `FIRST_USE.md` in `T/.director/`:
1. remove trailing newlines;
2. append a newline, an empty line, `END M` and a newline.

For example, the last line of `T/.director/WORKER.md` becomes `END WORKER.md`. Make no other change to these files.

**6. Leave these unchanged:** `T/.director/START.md`, `DIRECTOR.md`, `OPERATIONS.md` and `startup_check.py`. They are the checker's managed files, and a single changed byte blocks the check.
- The candidate's route never sends anyone to START.md or DIRECTOR.md.
- OPERATIONS.md is named only as "detail" and keeps no END line, so the block's whole-file rule applies to it.
- In a real implementation START.md and DIRECTOR.md would become redirect stubs and OPERATIONS.md would be trimmed. The test does not need that.

**7. No other files.** Do not create `CLAUDE.md`, host settings or hook files. The control has none either.

**8. The check needs a script change to pass.** With the shipped checker, the candidate's check blocks. Observed:

```text
{"status":"blocked","scope":"bounded local operational evidence only","gap":"marked startup hook does not reference selected route: .director/START.md"}
```

- **Cause:** the candidate block names `.director/WORKER.md`, not `.director/START.md`, and the block may not change. `startup_check.py` line 224 builds the required target from `root / 'START.md'`; for the candidate it must be `root / 'WORKER.md'`.
- **That is a change to the check script, and it is not made here.** It is for the Project Director to approve.
- **Without approval, skip 8a and 8b.** The Project Director then gets this gap on every check and answers without 🎬. Whether it reruns the check after a compaction is still observable; whether the badge lapses and renews is not.
- **With approval, do exactly this and nothing else:**
  - **8a.** Copy `T/.director/startup_check.py` to `T/.director/startup_check_candidate.py`. In the copy only, replace the one occurrence of `(root / 'START.md').relative_to(project)` with `(root / 'WORKER.md').relative_to(project)`.
  - **8b.** In `T/AGENTS.md`, replace the project section's line `` - Check command: `python3 .director/startup_check.py` `` with `` - Check command: `python3 .director/startup_check_candidate.py` ``. Expected `T/AGENTS.md` size: 7,219 bytes.

  Expected from `python3 .director/startup_check_candidate.py` (observed): `"status":"evidence_matched"`, `startup_hook.target` `.director/WORKER.md`, and `AGENTS.md` snapshot `changed`, which does not block. The shipped `startup_check.py` stays byte-identical, so its managed hash still matches `install.json`.

**9. Verify before the session starts.**
- `wc -c T/AGENTS.md` gives 7,209, or 7,219 after step 8b.
- `tail -n 1` on each card, and on the seven manuals from step 5, prints its `END …` line.
- The check command named in `T/AGENTS.md`'s project section gives the status expected in step 8.

## What the candidate's route uses

| Reader | Reads at start | Re-reads after a compaction or resume |
|---|---|---|
| Project Director | `AGENTS.md` (standing); runs the check | The check, and the card or file its next action needs |
| Worker (a subagent with a report-back task) | `AGENTS.md` (on hosts that pass it), `.director/WORKER.md`, any role file in its brief | The same, when no longer shown |
| Scoped child Director | `AGENTS.md`, its overlay or role file | The same |

`START.md`, `DIRECTOR.md` and the unchanged `OPERATIONS.md` stay installed and are reachable by name. The candidate's block does not send anyone to START or DIRECTOR. If a transcript shows them being read, record that as an observation.
