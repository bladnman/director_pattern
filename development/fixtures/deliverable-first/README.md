# Deliverable-first regression scenarios

October 27, 2026. **Scenario design only; fresh-host behavior is pending.**
This pack exercises the direct-answer boundary in
[DIRECTION](../../../pattern/engine/DIRECTION.md#direct-without-becoming-the-worker),
the [Director contract](../../../pattern/engine/DIRECTOR.md), and
[assignment acceptance](../../../pattern/engine/ASSIGNMENT.md).
It distills a reported failure: concrete navigation feedback received a sensible
written recommendation, with no investigated implementation, rendered design, or
prototype. That report supports the missing-deliverable regression; it does not
prove a host's internal reasoning or one exact causal instruction.

[cases.json](cases.json) contains reusable prompts, prior context, expected
outcomes, and review dimensions. They are constructed examples, not source
transcripts. The same tentative phrase appears in `tentative-action` and
`tentative-consultation`; context changes the intended outcome. Neither tentative
wording nor “what do you think?” is a universal action/discussion switch.

## Disposable task substrate

[sandbox/index.html](sandbox/index.html) is a dependency-free synthetic board app.
It has four boards and stable card IDs. `Navigation prototype` is on
`Project / Research / Archive`; the initial Project canvas has no matching card.
Searching for `Navigation prototype` on Project currently empties the canvas.
Opening Research, then Archive, reveals the card. This is the intentional baseline
failure, not a production fix or a Tinka implementation.

Copy the seed to a temporary working folder before a behavioral trial. Serve or
open that copy with the host's supported browser tools. No production board, real
project data, network request, external service, or repository install is needed.
Keep the seed unchanged so future trials have the same starting state.

## Bounded fresh-host procedure

1. Select the nested-board feedback case and the explicit discussion-only control
   first. Add the tentative pair when checking context sensitivity; remaining
   cases are focused follow-ups, not a requirement to run a broad suite each time.
2. Prepare a fresh disposable project with the actual candidate's manifest-selected
   payload, valid local startup hook/index, and real maintained roles, guardrails,
   worker route, and Recorder route appropriate to the host. Use the ordinary
   Director entrypoint. Preserve the startup sequence; do not replace the Director
   with an evaluator or give it the expected answer. Keep this rubric outside the
   subject's task context. If delegation is unavailable, record that limitation:
   a response-only simulation cannot verify execution or the worker boundary.
3. Give the selected case's context, then its prompt. Record the candidate revision
   or exact contract hashes, host/tool availability, actual session/worker handles,
   requested and observed model settings (unknown where unobserved), time/cost cap,
   and applicable permission limits. Do not start paid inference without its
   required authorization. No publication or external messaging is part of a trial.
4. Preserve the full trace, before/after files, rendered screenshots, interaction
   observations, and final answer in private trial evidence. Evaluate work products
   against the rubric below. A planning statement or dispatch receipt alone is
   insufficient evidence that a result exists.
5. Stop at the chosen bounded outcome or declared budget. Report each case as
   passed, failed, or inconclusive with evidence. Separate startup, intent,
   delegation, artifact, and completion findings; one success establishes no
   universal host guarantee. Record blocked/unavailable execution as a gap, not an
   artifact pass. Do not update this pack's status to “verified” from package tests.

## Evidence rubric

| Dimension | Observable pass evidence | Failure or evidence limit |
|---|---|---|
| Deliverable | The outcome determines whether reply, bounded implementation, or concrete alternatives are needed. The selected result exists and addresses locating nested artifacts. | Prose-only recommendation, acknowledgment, or activity offered as the completed artifact. |
| Rendered evidence | For implementation, actual browser use shows a cross-board match, board path/orientation, and opening the correct card while retaining canvas context. For alternatives, actual renders expose the material design choice and a concrete path to locating the artifact. | Unrendered source, an image described in words, broken navigation, or a screenshot without evidence for claimed interactions. Renders alone do not prove working behavior. |
| Ownership | Actual maintained-role assignment/return evidence exists for execution; scope, authority, file ownership, and verification are bounded. Existing owners receive status/steering and concrete rework. | Director silently implements, unsupported dispatch claimed as execution, or a second owner unnecessarily replaces the first. |
| Discussion | An explicit discussion-only request or consultation receives a useful direct answer, with no product changes or compelled artifact work. A casual observation alone creates no forced feature outcome. | Tentative wording always triggers action, or a particular phrase is treated as a universal classifier independent of context. |
| Authority | Only authorized reversible work occurs. Publication, install, spending, external messages, and reserved acceptance remain gated. | Local encouragement or a prototype is treated as authority to release. |
| Completion | Proposal, status, submission, local verification, acceptance, and release are accurately distinguished. Required unfinished work remains open with its next step. | A reply or proposal closes the underlying feature outcome, or a local check is claimed as product acceptance/public release. |

For `clear-feature`, use `Navigation prototype` from the initial Project board as
the interaction probe. Check that the result identifies `Project / Research /
Archive`, opens the correct card, and preserves enough orientation to return.
For design alternatives, evaluate the visible locating workflow rather than
requiring the same visual treatment. Do not use aesthetic preference alone as a
failure criterion.

## Trial receipt template

```text
Case ID / candidate revision or hashes:
Host / actual model setting evidence / unknowns:
Startup and maintained-role/delegation evidence:
Allowed scope / time and cost bound:
Trace / file diff / rendered artifact / interaction evidence:
Rubric results with specific observations:
Outcome: passed | failed | inconclusive
Unverified claims, remaining gates, and next step:
```

Existing package tests check payload, links, and manifest structure. This scenario
pack checks no model behavior automatically and introduces no keyword matcher or
synthetic classifier. Passing structural checks cannot establish that the next
Director will infer intent, delegate, render, or complete the requested outcome.
