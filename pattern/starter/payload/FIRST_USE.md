# Generated-project first use

Use this route only when the current integration selects it for a real generated
instance. Fresh starter installations already have `install.json` and use their
normal check. Existing projects retain their own backend, receipt and recovery
route. A missing receipt, current folder, Git repository or copied template does
not authorize initialization.

Before `ensure`, completely read the selected project, template, tracker and
canonical I/O instructions. For the native request-bundle route, retain its STATE,
RECORDS and TOOLING requirements and current ownership adaptations. For a custom
video route, read TRACKER, `.team/RECORDS.md`, `.program/README.md` and the video
adapter. Complete its actual privacy/index prerequisites before private writes.
The helper verifies exclusions read-only; it does not change ignore rules or the
index. Resolve missing instructions or conflicting authority before proceeding.

Run the exact selected command once before the ordinary first-reply check:

```sh
python3 .director/first_use.py ensure --root .director --instance .director/INSTANCE.json --provenance .director/PROVENANCE.json
```

Only a successful opted-in generator creates `INSTANCE.json`, with schema 1,
kind `generated-template-instance`, UUID `generation_id`, actual `template_id`,
canonical new destination `root_path` and SHA-256 of the copied PROVENANCE bytes.
`template_id` is the actual selected folder ID; PROVENANCE's `template` is the
content profile. They may differ for a renamed template. Both must be nonempty;
the exact provenance digest and managed hashes bind the selected backend and bytes.
Generic seeds contain no `INSTANCE.json`. The root binding applies before setup; an initialized
project may move or clone while retaining its existing identity and receipt.
This marker is creation evidence, not authenticated identity or setup acceptance.

The transport's exact `first_use` descriptor selects schema 1, `instance_path`,
`receipt`, `backend`, `hook_source`, `guards` and `optional_guards`. The supported
paths are `.director/INSTANCE.json` and `.director/receipts/RECEIPT_setup.json`.
The native backend is `director-request-bundles` through the preserved
`.director/tools/requests.py` and `.director/config.json`; `project-contract`
instead names its actual contract `path` and creates no bundled store. An optional
guard becomes required when present and needs its reviewed transport baseline.
Unknown routes, drift and unreviewed customization require owner integration.
Custom canonical `requests/` and `walks/` must contain no user data. They may contain
only regular zero-byte `.gitkeep` files at exact reviewed managed paths, plus
structural directories leading to those placeholders. Unreviewed directories or
files, nonempty placeholders and unsafe paths block setup. Only expressly reviewed
generic journal and `.team` seed files may otherwise match transport baselines;
a hash-listed user request or walk is already populated state.

`ensure` verifies strict bounded JSON, regular safe paths, source pin/tree,
generation binding, exact managed hashes and selected guards. It refuses generic
seeds, existing data without its own intent, and conflicting state. It preserves
the transport provenance and its unconfigured/not-accepted flags. Published source
evidence and an unpublished candidate delta remain distinct in the technical
receipt; a known published base does not publish new helper bytes.

For an eligible empty native instance, it saves one chosen project ID in
`.director/.first-use.json`, calls the preserved native initialization API, validates
the empty backend and creates the technical receipt exclusively. Its first-use
lock and the native writer lock serialize cooperating local writers. Do not delete
locks or intent. A retry resumes only that exact unchanged owned intent and chosen
ID. Existing user changes, native transactions and mature data require their owner
recovery route; no implicit rollback, migration or new identity follows. Keep these
machine-local intent/lock files and the absolute-path instance marker excluded
under the selected template's privacy policy.

A completed receipt is reused without initialization or rewriting. A missing
receipt with existing state must be restored or reconciled; never allocate another
ID. The exact owned intent may restore a missing receipt only with its matching
instance/root/provenance, unchanged empty config and no populated user state or
managed drift. That recovery reuses the chosen identity without initialization and
records the recovery in the receipt and result. Other receipt loss remains a gap.
After a failed attempt, inspect the actual gap and owned intent. At most one
demonstrated safe recovery attempt in the conversation is appropriate; otherwise
return the gap and next owner/action while continuing independent authorized work.

After successful preparation or reuse, run the integration's normal explicit
`startup_check.py` command separately. Evaluate its returned evidence, complete
current role/guard/backend instructions and actual authority before using 🎬.
Bootstrap success alone grants no badge. Workers and scoped child Directors skip
this Project Director route. Technical receipts retain native startup and human
acceptance as unrun; setup captures no user source, configures no remote or update
policy, initializes no Git repository and claims no delivered privacy warning.

The helper requires Python 3.10+ and POSIX `fcntl`. It bounds JSON at 128000 bytes,
individual selected files at 1000000 bytes, an input pass at 4000000 bytes, managed
entries at 256 and output at 4096 bytes. Local advisory locks do not provide a
multi-machine transaction or authenticate source evidence.
The selected native init CLI has a 15-second timeout. Managed code is rechecked
immediately before execution; the local cooperating-writer contract does not protect
against a hostile process replacing code between verification and execution.

END FIRST_USE.md
