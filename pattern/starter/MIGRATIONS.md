# Starter 3 upgrade notes

Read this from the pinned incoming source when updating an existing starter 3
installation. Apply each matching entry in revision order, even when skipping
releases. Compare numbered revision components numerically. If the installed
receipt has no `starter_revision`, look for the manifest at its verified prior
source pin. If the revision still cannot be established, use the entry's local
evidence to assess relevance and preserve uncertain changes for review. Report an
unrecorded receipt revision as unrecorded. Use the same comparison, backup,
independent review and receipt as the rest of the update. Retain or consolidate
entries while any supported direct upgrade still needs them. For another package
family or an incompatible store, follow its own compatibility or recovery route.

## From before 3.12, or when this issue remains outstanding

- **Check workflow visibility.** In a Git worktree, inspect the effective ignore
  rules for this installation's workflow and configuration files with
  `git check-ignore -v --no-index` and inspect tracked paths separately with
  `git ls-files`. Identify the governing rule, including any excluded parent.
  Look at the actual startup route and recorded local privacy choices. If the
  intended files are already eligible, or the project has no Git, leave the files
  alone and report the finding.
- **Establish ownership.** Reconcile a blocking rule only when verified prior
  installer or template material, or reliable setup history, ties it to an
  obsolete setup default without a later local override. A version number,
  a literal `/.director/` rule, or an unchanged installed hash alone is insufficient.
  A current privacy instruction signals local authority. Check whether it came
  from the same obsolete default or records a project decision. If its authority
  is unclear, preserve it and report what the owner would need to resolve. Keep a
  deliberate choice unless the project owner expressly authorized a change to
  that policy and its scope. Keeping a local choice is a valid update outcome.
- **Narrow only the proven default.** Review an explicit list of shareable
  workflow/configuration files, including relevant files referenced by the startup
  hook. Check their content for private data. In a manual update, change only the
  proven default or the expressly authorized rule in a file this project owns and
  has authority to edit. Reconcile verified stale setup wording that would reapply
  the rule under that same authority. If an old rule hides the entire directory,
  keep explicit exclusions for everything outside that reviewed list, reopening
  ancestors only as needed to reach those files. Keep
  existing exclusions for requests, linked sources and attachments, receipts,
  activity, state, secrets and runtime scratch. Keep scratch and backups local.
  If an ancestor, global or other retained rule still blocks a file, report the
  source of that rule and leave it in place. Preserve the Git index and history.
  Automatic mode can inspect and record results, but needs an explicit update
  instruction before applying a migration edit.
- **Check and record.** Back up and verify affected ignore and instruction files
  before editing. Recheck effective Git eligibility for intended and protected
  paths, the unchanged index, and continued access to the existing tracker and
  startup files. If an edit fails its checks, restore only the update's own edits
  from verified backups when safe. Record in the existing update record what was
  changed, already eligible, deliberately kept local, inapplicable or still
  pending, with the rule source, origin evidence, checks and next action. Report
  any uncertain rule that needs the owner's decision as unresolved. Keep an
  incomplete change under the normal partial-update rules. A same-revision retry
  uses the existing record and current evidence, leaving a completed or
  deliberately retained choice alone.
