# Start flat, grow when the work needs it

This guide explains the local source candidate. It is not a claim that the published
v1.1.0 release, this repository's live installation, or another project has changed.
Use [the package guide](../pattern/README.md) for installation; this explanation is
maintainer material and is not copied into a target project.

Learning uses recorded evidence, not the current Director's memory: corrections
enter a queue, a cursor bounds what a separate reviewer reads, and an owner decides
which scoped lessons to retain. Later matching work must actually load and use them.
No offline review runs unless an actual execution schedule is separately configured.

## One conversation, one accountable Director

Start with one Project Director. It understands the request, keeps the conversation
moving, assigns bounded execution to workers, evaluates what comes back, and retains
the whole outcome through usable delivery. A worker can research, make slides, code,
or independently test. A role describes the responsibility and required knowledge;
it does not create a continuously running actor or grant extra permission.

The Director performs supported, validated recording operations itself. A separate
Recorder, second Director, Architect, identity pool, department directory, or checking
actor is not a prerequisite for a new project. A short question is answered directly.
After startup, pure conversation needs no helper call or state/learning action
guide. Those load when an actual action needs them. An artifact request gets an
artifact and appropriate checks. Existing project gates, privacy rules, trackers
and independent testing remain applicable.

## A concrete progression

This is a usage example. The evidence section below separately identifies what
actual temporary-folder trials exercised and what remains unverified.

**1. Ask for slides.** In a fresh project, ask: "Make six slides explaining our new
onboarding process. Use the supplied notes, and give me an editable deck."
The Director captures the actionable request and acceptance conditions, assigns a
worker with the supplied notes and slide-authoring responsibility, and retains
conversation and evaluation. It does not create a Slides Department. The worker
returns a deck and rendered evidence; the Director checks the intended result and
requests concrete repair where needed. Technical validity and human approval remain
different claims.

**2. Correct the work midstream.** Say: "Keep the participant instructions sparse;
put facilitator guidance in the notes." The Director applies that instruction now,
preserves the correction with its scope and source, and routes it to the same owner.
An explicit durable user rule can be recorded with `accept-rule` immediately; it
does not wait for three incidents or an independent reviewer. Unaffected work
continues. The record separates what happened, what caused it if known, what was
corrected, and what remains uncertain. The rule takes effect within existing
authority; a reviewer need not rediscover or approve it before it can be followed.

**3. Come back tomorrow.** A new Director loads the small current summary: unfinished
outcomes, owners and observed execution references, next actions, and a knowledge
count/pointer. After startup, task-time scope discovery identifies the canonical
task, audience and path scopes; the Director then selects the complete applicable
lesson text for the actual affected files. Discovery can find nested scopes without
broadening where their rules apply. It does not guess category names or preload
all accepted rules. It checks actual execution before resuming or replacing work.
It does not read every historical slide revision to enter the conversation. The
correction still belongs to the slide outcome; a compact pointer preserves access to its exact
source and evidence. A saved handle does not prove a worker is running.

**4. Review accumulated friction separately.** The active Director initiates a
bounded independent learning review in a separate worker context at meaningful
closure under the default
review policy, when three incidents are pending and permitted capacity exists.
That default count batches review spending; it detects no pattern and creates no
department. A direct review request can bypass it. A project can instead select an
explicit-request policy. The reviewer reads the queued evidence after the last successful review cursor, within its
assigned limit. It may find one correction, repeated corrections, or no reusable
lesson. It returns a scoped proposal with evidence and limits. It does not silently
rewrite policy, create departments, or consume the entire project history.

This is not guaranteed detection of trends across already-reviewed batches. The
same problem can recur in separate batches without the reviewer connecting them.
Past evidence remains available for a targeted historical investigation or an
optional Architect, but no actor magically retains it all. Three pending incidents
need not be three instances of the same issue. This is a scoped learning loop,
not comprehensive self-healing.

The review is real work with model, time and context costs. The helper also reads
its state file internally; a bounded model-facing batch does not make storage work
constant as the project grows. If there is no supported execution opportunity, it stays pending. A file does not launch it while the host is
inactive. The next active checkpoint can retry from retained work; interruption or
failure must not silently skip unreviewed evidence. Current user work continues
under the rules already known, and the Director reports a consequential gap.

**5. Accept a lesson, then test its use.** The accountable owner evaluates the
reviewer's proposal. For example: "For participant-facing course slides, keep visible
instructions concise and put facilitator detail in notes." If authorized and
supported, the owner records that limited rule and routes it into the maintained
slide-authoring knowledge. Rejected and uncertain proposals remain distinguishable
from accepted policy. A future assignment selects that responsibility, discovers
the canonical knowledge scopes at task time, and loads the matching accepted rule before working. Exact
scoped discovery is not a semantic search engine over every old conversation.
Only a later matching task and its checks show that the lesson was actually used. A stored lesson alone proves storage.

Three similar corrections can justify a review. They do not automatically prove a
common cause, a universal rule, or a need for another Director. A one-off preference
for a particular deck stays local unless its evidence and authority support more.

**6. Add temporary coordination when needed.** Suppose the next outcome requires a
series of decks, a web exercise, participant materials and independent review, with
many dependent returns and recurring rework. The Project Director can give one
bounded outcome to another Director using the same base role plus the relevant
scope and domain knowledge. That actor owns detailed coordination; the Project
Director retains conversation, cross-outcome judgment and user-facing acceptance.
An outcome-named Director can describe that responsibility. It uses the same
`director` assignment role and is not an automatic layer for every deliverable.

**7. Let a department earn its place.** If several outcomes repeatedly need the same
coordinated responsibility, maintained knowledge and owner, preserve that capability
as a department. Give callers a narrow entrypoint stating when to use it, what to
supply, what it returns, and its authority limits. Its internal workers and evolving
organization can stay behind that entrypoint. A small project does not need a
complete service catalog in advance. Repeated demand, ownership friction and actual
results guide the decision; the number of files or corrections does not decide it.
Three or thirty-five task requests can stay flat; a count does not require a layer.

Keep the pieces distinct. Accepted craft knowledge lives in the scoped knowledge
store or the project's canonical craft reference, and matching tasks load it.
A named role definition adds selection cues, responsibility, references and authority
for recurring work. A department header adds a narrow caller interface to coordinated
work: when to use it, what to supply, what comes back and the reserved gates. These
are project-owned additions, not more mandatory starter files.

The Project Director learns that such a header exists through an explicitly
maintained project startup pointer. An authorized maintainer adds that pointer to
the project's own instructions, leaving the managed starter foundation intact.
The actor then reads the named header when its trigger applies. Arbitrary files
are not automatically discovered, and accepting a structural proposal does not
write a role, add a pointer or implement routing. That implementation and its
next-use check are separate work within the project's actual authority.

The temporary mature-project fixture uses this concrete layout:

| Project-owned location | Purpose |
|---|---|
| `AGENTS.md` task-time pointer | Routes affected HTML, art, engineering and testing work to the existing header. |
| `departments/experience/HEADER.md` | Small entrypoint exposing shared routing, knowledge and reserved gates. |
| `roles/ART.md` | Maintained art responsibility and its scope. |
| `roles/ENGINEERING.md` | Maintained implementation responsibility. |
| `roles/INDEPENDENT_TEST.md` | Separate independent verification responsibility. |
| Starter's accepted state knowledge | Scoped craft lessons queried through `selectors` and `select`. |

The fixture adds its pointer explicitly and preserves the managed `.director/`
payload. It demonstrates a chosen project layout, not automatic generation of a
department or a mandatory directory convention. The validation notes identify
which actual actors loaded and followed it.

Combining knowledge packages can remove repeated instructions. It does not merge
independent testing into the producer's self-review, remove an approval boundary,
or authorize publishing, spending, installation elsewhere or external messages.

## What happens automatically, and what does not

The installed instructions make bounded capture, compact recovery, delegation,
evaluation and review initiation duties of the active Director. The host still has
to execute those duties. Queued evidence, a role definition and a review cursor are
durable data, not a scheduler, daemon, wakeup or continuously running Architect.
For example, an Architect that reviews incidents every night would need an actual
separately configured host schedule, authorized execution and a return/evaluation
route. That off-session service is not implemented by this starter.

The user need not request a new department for each deliverable or retell an accepted
scoped correction every session. The user still supplies consequential taste and
authority decisions that are reserved to them. The accountable owner evaluates new
learning proposals; authority and existing gates determine whether a change can be
accepted directly or needs the user's decision. No actor gains permission from
calling a change self-healing.

## Reproduce the candidate

From this repository on Python 3.10+ and a POSIX host, make a disposable project.
Current execution checks are on macOS; Windows locking is not implemented.

```sh
trial_project="$(mktemp -d /tmp/director-walkthrough.XXXXXX)"
python3 pattern/starter/install.py plan --target "$trial_project"
python3 pattern/starter/install.py install --target "$trial_project"
python3 "$trial_project/.director/state.py" status </dev/null
```

The plan reports copied paths, hashes, bytes and the declared startup sets. Keep
the temporary folder to inspect it. Ordinary notes/assets are preserved, but an
existing conflicting startup or tracker causes a no-write refusal and needs the
separate [reviewed integration path](../pattern/INSTALL.md). Identical reinstall
preserves state. Rollback uses the printed install receipt and refuses changed
owned content; it does not discard later work.

This mechanical rehearsal captures a request, preserves a later exact correction,
records its already explicit scoped rule, discovers the canonical scope, and
selects it for a matching task.
It runs no model, author, reviewer or scheduler:

```sh
python3 - "$trial_project" <<'PYTHON'
import json
import pathlib
import subprocess
import sys

helper = pathlib.Path(sys.argv[1]) / ".director" / "state.py"
def call(action, data):
    output = subprocess.check_output(
        [sys.executable, str(helper), action, "--data-file", "-"],
        input=json.dumps(data).encode(),
    )
    return json.loads(output)

scope = {"tasks": ["course-slides"], "paths": ["slides"],
         "audiences": ["participant"]}
request = call("capture", {
    "op_id": "walk-request", "expected_revision": 0,
    "text": "Make six editable onboarding slides.\n",
    "request": {"id": "slides", "summary": "Onboarding slides", "scope": scope,
                "acceptance": "Owner evaluates usable slides", "owner": "Director"},
})
correction = call("capture", {
    "op_id": "walk-correction", "expected_revision": request["revision"],
    "request_id": "slides", "expected_request_revision": request["request_revision"],
    "text": "For participant course slides, keep visible instructions concise; "
            "put facilitator guidance in notes.\n",
})
rule = call("accept-rule", {
    "op_id": "walk-rule", "expected_revision": correction["revision"],
    "request_id": "slides", "expected_request_revision": correction["request_revision"],
    "source_id": correction["source_id"], "scope": scope, "owner": "Director",
    "claim": "Keep participant course-slide instructions concise; use notes for facilitator guidance",
    "reason": "Explicit scoped user instruction in the captured correction",
})
catalog = call("selectors", {"path": "slides/example"})
# This fresh rehearsal has one rule; larger catalogs require every relevant page.
canonical = catalog["items"][0]["scope"]
matching = (canonical["tasks"][0], canonical["audiences"][0])
for task, audience in [matching, ("technical-report", "engineer")]:
    selected = call("select", {"task": task, "path": "slides/example", "audience": audience})
    print(json.dumps({"task": task, "matching_rules": len(selected["items"])}))
PYTHON
```

The intended output is one matching rule for course slides and zero for the
technical report. A real worker still needs to read the complete selected rule
before producing slides; this rehearsal proves neither authorship nor learning
uptake. For independent pattern review, use the exact bounded
[`review-batch` → `review-save` → `decide` API](../pattern/starter/payload/API.md),
with a real reviewer's output and an accountable owner's evaluation. That path
remains separate from recording an already explicit user instruction.

## What was actually checked

The exact mechanical walkthrough above passed against the frozen candidate: one
matching course-slide rule and zero unrelated-report rules. Temporary-folder
inventory, helper checks, actual-agent observations and their limits are recorded
in [the validation notes](DESIGN_NOTES.md#flat-starter-and-bounded-learning--october-30-2026).
Actual actors demonstrated bounded review, later scoped lesson use and separate
verification. A narrow instruction/handoff retry reduced observed calls from 59 to
30, while the plain worker used seven. Efficiency over plain execution remains
unproven, and substantial overhead was observed. Startup deviations are retained;
this is not a blanket host-compliance result. The evidence separates recording a
rule, accepting a reviewer proposal and actually using it on a later task.
