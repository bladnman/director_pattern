# Supervision and recovery regression scenarios

October 27, 2026. These are bounded behavioral scenarios, not an automatic intent
or liveness classifier. The owning contracts are
[DIRECTION](../../../pattern/engine/DIRECTION.md#recover-and-supervise-held-work),
[STATE](../../../pattern/engine/STATE.md#parent-commitment-and-requirement-traceability),
and [ASSIGNMENT](../../../pattern/engine/ASSIGNMENT.md).

| Scenario | Observable result |
|---|---|
| Subordinate worker or director is running | Its parent retains the user commitment, observes real handles, uses bounded waits and stays supervising. Calling the child a director does not create an external handoff. |
| Status question while work runs | The parent gives an evidence-based status answer and continues the existing assignment. A reply does not close the outcome or classify slow work as stuck. |
| Proactive labeled SitRep becomes due | About five minutes after actual dispatch, or the user's interval, the parent sends a labeled **📋 SitRep** without waiting to be asked. It accounts for all held streams, owners, actual status and next action. Ordinary progress/status messages do not reset or substitute for this report. |
| Resume with overdue or unknown SitRep time | Recover the reporting cursor alongside held work. If the last labeled report is overdue or unknown, provide a labeled overview promptly; do not start a fresh full waiting interval merely because this conversation resumed. |
| Incomplete first submission | The parent inspects the actual artifact, names the missing requirement and sends concrete rework to the existing owner using a supported continuation route. It evaluates the repaired return before acceptance. |
| Queued message to an idle/completed owner | Delivery is distinguished from execution. The parent checks actual recipient state and uses a supported resume/start action when needed; it does not silently wait for a message to launch work. |
| Active-project conversation restarts | Recover stable request/owner IDs, last observations, handles, partial results and next actions, then check actual host state. Evaluate returned work; do not blindly respawn old tasks or treat an old active record as live execution. |
| Required child reworked or relocated | The original parent commitment and per-owner requirement/status evidence survive. Assignment and return reference parent project/request IDs and child record IDs or locators when present. Small assignments need no duplicate request tree. |
| Genuine external owner, explicit pause, or host interruption | Respect the precise exit condition and retain the waiting commitment or checkpoint. An external acknowledgment does not prove liveness, grant access, or transfer source acceptance. No daemon or automatic wakeup is promised. |
| Explicit discussion-only request with no held work | Answer conversationally without compelled dispatch. Existing authorized work is not canceled by an unrelated discussion/status reply. |

## Finite runtime trial

Use a disposable project with the actual candidate engine, its startup bridge,
real maintained role definitions/reference chain, and a permitted worker route.
Do not replace the manager with an evaluator who only repeats the expected answer.
Keep raw traces, actual handles, artifacts and receipts private. Declare the exact
candidate hashes, host limits, model/effort evidence and bounded authority.

One small trial can exercise several transitions: a fresh bounded manager obtains
a JSON report from a real child, a status question arrives while the child runs,
a controlled first submission omits a required field, and the manager requests
rework from that same child. Inspect the final artifact independently. A fresh
recovery reader then compares dated trial evidence with actual host status before
recommending any continuation. Deliberate fault injection must be disclosed; it
is not an unbiased production reliability observation.

Report startup loading, dispatch, active observation, status answer, artifact
inspection, rework, final evaluation and recovery separately. A helper fixture
proves only record behavior; a prompt or saved status proves no live supervision.
A bounded successful trial establishes no universal future-host guarantee, actual
user acceptance, release, five-minute cadence, or behavior during host exhaustion.
A separate cadence observation must record actual dispatch and labeled-report
times, intervening ordinary updates, and the resume cursor. Keep user-observed
missed proactive reports as failures; later wording or a shorter successful trial
does not erase them or establish that the revised cadence was followed.

## Deterministic record checks

[test_supervision_records.py](../../tests/test_supervision_records.py) uses only
disposable stores. It checks that explicit required child dependencies gate parent
acceptance through rework, stable informational backreferences and requirement
notes survive relocation, and a status note/restart does not change active work
to done or turn its recorded dispatch into verified liveness. Existing external
handoff fixtures cover independently owned waiting outcomes. None implements or
claims a model-behavior classifier.
