# Director Pattern

A Project Director stays in conversation, retains the whole outcome, assigns
bounded execution to workers, and evaluates the result through usable delivery.
Start flat. Add another Director when sustained coordination warrants it; develop
a department when recurring ownership and maintained knowledge earn their place.
The same base role can compose scoped and domain knowledge without duplicating an
organization at installation.

**Current source candidate:** the [flat starter](pattern/starter/README.md) is the
new-install entrypoint for a project without conflicting startup or tracker.
It has no mandatory second Director,
Recorder, Architect, identity pool or setup-check actor. The Director performs
validated recording operations and supervises workers. Durable corrections feed a
separate bounded learning review; the Director does not reread all history at
startup or remember lessons without recorded evidence and later matching use.
[See the concrete growth and learning walkthrough](development/FLAT_STARTER.md).

**Published release:** [v1.1.0](https://github.com/bladnman/director_pattern/releases/tag/v1.1.0),
October 27, 2026, uses the earlier Request Manager/shared Recorder design. The flat
starter is an unpublished source candidate. This checkout, the website, the live
local installation and existing projects can therefore describe different revisions;
source changes do not update them automatically.

**Installing or updating:** begin with [pattern/README.md](pattern/README.md).
It separates the fresh-project path from the explicit preservation path for
existing projects with startup instructions or trackers. Ordinary notes and assets
are preserved on the fresh path. Preserve canonical trackers, local authority, adaptations,
unfinished work and exact sources; an existing installation is never silently
migrated to the starter. Copy only the selected manifest payload, not this entire
checkout or its maintainer instructions.

**Using the published method:** [the website](https://director.metal-sole.com/) has
the public overview and lifecycle requests; its [agent guide](https://director.metal-sole.com/install.md)
routes to canonical published installation/update guidance. Website source and
hosting notes live in [site/](site/). Publication is separate from this candidate.

**Maintaining the method:** read the overview, owning decisions and applicable
dated supersessions in [development/RATIONALE.md](development/RATIONALE.md), then
follow [AGENTS.md](AGENTS.md). [Development validation notes](development/DESIGN_NOTES.md)
distinguish source/fixture checks from actual agent observations and remaining
adoption gates. These documents and tests are not installation payload. A source
checkout alone does not install the pattern or confer Director authority.

Assignment roles remain `worker` and `director`. A scoped coordinating Director,
reviewer or domain specialist is a maintained responsibility, not a new role value,
permission grant or promise of a live agent. Independent testing and existing
approval boundaries remain explicit as knowledge packages compose. No daemon,
scheduler, background wakeup or offline learning service is implied.

The source repository is [bladnman/director_pattern](https://github.com/bladnman/director_pattern).
Candidate authorship, target installation, fresh-session verification, user
acceptance and public publication are separate steps.

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
