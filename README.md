# Director Pattern

**[v1.0.0](https://github.com/bladnman/director_pattern/releases/tag/v1.0.0) · October 23, 2026.** The project Director stays in conversation,
keeps its unfinished commitments, and accepts each outcome. Each complete outcome has
one accountable owner, normally a Request Manager; specialists execute; a shared
recorder preserves state.
Tracked is default; lean is optional.

"Director Pattern" names the package. Assignment roles stay `worker` and `director`:
the project Director and a Request Manager bounded to one outcome both carry
`Role: director`, and Request Manager and Recorder are maintained responsibilities,
not new role values. A specialty such as engineering, testing, or release is a task
inside an outcome, not a reason for another manager. The Director can optionally
dispatch substantial independent analysis that returns a proposal. Before staffing,
an installation records enduring context, the canonical role index, capability and
authority policy, Recorder routing policy, and the identity roster locator. Runtime
controls are resolved when used; model/team/host observations stay in assignment or
receipt evidence, outside PROJECT and startup instructions. It adds no runtime or
live-agent guarantee. Updates preserve project policy and historical evidence
without treating past environment mappings as current configuration.

**New here? [Start with the website](https://director.metal-sole.com/)** for the
overview and copyable requests to install, check, or update it through your
project's existing agent. Website source and hosting notes live in [site/](site/).

**For an agent:** [read the website's guide](https://director.metal-sole.com/install.md)
to continue to the canonical GitHub installation or update protocol.

**Here to install? Start with [pattern/README.md](pattern/README.md).** That subtree
stands alone. Install only its manifest-listed payload into the target project's
`.director/`; the rest of this repository is not part of the installation.
A temporary clone may transport files, but copying the checkout is not adoption.

**Here to develop the pattern? Read [development/RATIONALE.md](development/RATIONALE.md)**
for the reasons, tradeoffs, and open decisions, then follow this
repository's [authoring guidance](AGENTS.md). Maintainer material is not required
for installation. Local adoption is separate: when configured, the optional local
startup hook activates an installation. A source checkout alone does not install
the pattern or confer director authority.

Candidate authorship, target installation, fresh-session verification, and public
publication are separate steps. The source repository is
[bladnman/director_pattern](https://github.com/bladnman/director_pattern);
the agent installation entrypoint is [pattern/README.md](pattern/README.md).

For an existing installation, pin published GitHub `main` to an exact reviewed
commit and use that revision's [update protocol](pattern/references/UPDATES.md),
even when installed guidance predates incremental updates. Preserve project-owned
rules and adaptations. Routine updates use focused checks and applicable prior
evidence; full startup audits and fresh-agent trials run only for affected changes.
While active, only the checked project Director arranges a tiny metadata check
at most once per rolling 24 hours and defaults to a short notification. Say
“always update director pattern” to enable project-scoped automatic updates through
the same safe update protocol. No scheduler or new software is installed.

## Optional global skill

This optional lifecycle pointer requires explicit user invocation. Ordinary task
relevance must not select or run it. On request, copy the complete selected host
skill below to its per-user `director-pattern/` skill directory, preserving an
existing copy before replacement. Do not install a project-local skill by default.

| Host | Canonical source and required native control | Per-user destination | Explicit invocation |
|---|---|---|---|
| Codex | [skill/director-pattern/](skill/director-pattern/SKILL.md), including [agents/openai.yaml](skill/director-pattern/agents/openai.yaml) with `policy.allow_implicit_invocation: false` | `$CODEX_HOME/skills/director-pattern/` when set, otherwise `~/.codex/skills/director-pattern/` | `$director-pattern` |
| Claude Code | [skill/claude-code/director-pattern/](skill/claude-code/director-pattern/SKILL.md), with `disable-model-invocation: true` and `user-invocable: true` in `SKILL.md` | `$CLAUDE_CONFIG_DIR/skills/director-pattern/` when set, otherwise `~/.claude/skills/director-pattern/` | `/director-pattern` |

A clear user request to use the Director Pattern skill also meets its invocation
gate. Use the host command above or direct the agent to the selected skill file
for a reliable loading route; a bare name may not load a skill hidden from model
context. Native controls are required: description wording alone does not disable
automatic selection. Preserve these controls during every global-skill update; do
not copy
only Codex's `SKILL.md` and omit its policy file. For another host, establish its
supported explicit-only policy before installing this optional skill.

The pointer routes the requested operation to the current canonical guide;
installing or invoking it does not install the pattern in any project. Adopted
project startup hooks remain a separate instruction route. Already running chats
may retain previously loaded instructions; these file changes do not establish a
fresh-session behavior check.

On a request to remove the global skill, remove only the selected host's managed
files: `SKILL.md` and, for Codex, `agents/openai.yaml`. Remove managed `agents/` and
`director-pattern/` directories only if empty. Preserve unrelated files, other
skills, and every project installation.
