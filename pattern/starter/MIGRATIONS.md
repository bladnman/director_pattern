# Starter 3 upgrade notes

During an upgrade, use the notes at the incoming pin. Work through applicable
entries in revision order, including skipped releases. Compare version components
as numbers (`3.9 < 3.12`). If the installed revision is missing, check the manifest
at the verified prior pin. If it is still unknown, use local evidence to assess
applicability. Keep entries while supported upgrades need them. Follow
[UPDATES](payload/UPDATES.md) for same-pin retries, backups, review, rollback and
receipts.

## From before 3.12, or when this issue remains outstanding

- **Find the rule.** If there is no Git worktree, record that finding and skip the
  edit. Use `git check-ignore -v --no-index` to locate effective rules, including
  excluded parents, and `git ls-files` to check the index. Leave already eligible
  files alone.
- **Narrow the rule.** Edit only a project-owned rule that verified prior installer,
  template, or setup history identifies as an obsolete default, or one the project
  owner expressly authorizes changing.
  Preserve deliberate and ambiguous rules without that authority. Review an
  explicit list of shareable workflow and configuration files for private content.
  Make only those files newly eligible, reopening parents as needed. Under the same
  authority, reconcile proven stale setup instructions that would restore the old
  rule. Automatic mode may inspect and record findings. An edit requires an explicit
  update instruction.
- **Verify the result.** Check that intended files are eligible and existing
  exclusions still protect requests, sources and attachments, receipts, state,
  activity, secrets, backups and scratch. Leave the Git index and history untouched.
  Record the disposition, rule and evidence in the update receipt as applicable.
  Report any remaining blocking rule and any unresolved privacy decision.
