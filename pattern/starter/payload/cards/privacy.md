# Privacy and continuity

For a Director or a worker assigned to capture sources or decide what to track in `.director/`.

In a Git project, `.director/` configuration and workflow files belong in project
history by default so a fresh clone can run the same workflow. The leading dot
only hides the directory from ordinary file listings. Follow the project's privacy
choices and keep secrets and machine-local scratch out of commits.

At installation/first source capture, inspect actual Git/remote availability and
existing ignore choices. Fresh config, source/request bundles and receipts are
Git-eligible, not automatically committed or pushed. With a public remote or
unknown visibility, tell the user once that sources retain exact messages and
attachments and pushed history stays readable after deletion; record actual
delivery in the installation receipt/current project context so later machines
do not repeat it. The installer reports a due warning, not proof of user delivery.
A verified private remote needs no warning. Determine visibility with current
authorized tools or keep unknown; never infer private from a URL. If no Git exists,
report the review/rollback/cross-machine continuity limit; initialize only on user
request. Honor every existing privacy rule. Never unignore a mature store, force-add
data or silently change what is tracked. Ignore requests and linked sources
together when opting out; already pushed history is not removed by ignoring it.
Use git check-ignore to verify scratch/backups local and intended durable files
eligible; report a parent/global ignore rule rather than replacing it.

END cards/privacy.md
