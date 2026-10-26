# MISSION_HOLD_LIFT - LGX-T2-QUOTE (owner text; T2 = first live LangGraph/Hermes run under EVE control)

```text
MISSION_ID LGX-T2-QUOTE
TASK_SHA256 6d575090fcbfa47a8d050087a3ae93706aae20e8e81659367a03dd4b054c431d
VALID_UNTIL_UTC 2026-10-31T23:59:59Z
MAX_COST_CAP_USD 2.00
LGX_ORCHESTRATOR_SHA256 865f20a983dbbfeb9a6949d1f6f0510e9bec3c364b44b94266ee0f07885b5393
```

## Scope

- Covers only runs of THIS mission: TASK.md with exactly the sha256 above, through an activated copy of N3 r4
  (RUN_TASK_LGX_WSL_r4.sh 3552fdca..., only line 81 changed) -> N1 r3 (LangGraph orchestration, the sha256 above) ->
  F5 dc006243... -> C2 server r3k3 916021e9... -> agent A (worker) then agent B (reviewer), each started at most once,
  no retry.
- Every run needs (1) a separate OWNER-GO with an activation record bound to this mission, (2) the owner's typed
  approval of the MISSION_ID after the preview and (3) the owner's signature of a NEW mandate naming the sha256 of
  TASK.md and of exactly this text. Without all three, nothing runs.
- Roles: LangGraph orchestrates the hand-offs (fixed control flow, no model of its own); the Hermes agents do the
  work; EVE controls admission, mandate, binding and traceability.
- Data: all names and figures in TASK.md are fictional test data. The result is a draft file; nothing is sent to
  anyone and no business system (FlowWink or other) is written.
- Cost: cost_cap_usd of the signed mandate (at most MAX_COST_CAP_USD 2.00) is an ESTIMATE-BASED stop rule checked
  before each agent turn on after-the-fact Hermes estimates. It is NOT a hard spend limit: a single agent turn can
  exceed it. Actual cost is read from the server ledger after the run. The operational STOP of 15 USD on the shared
  ledger is separate and unchanged.
- Agent permissions: the agents' runtime-enabled tools and their containers' network egress are NOT_ESTABLISHED; the
  server prompt "do not contact anyone, do not publish" is an instruction, not a technical barrier.
- Ends at VALID_UNTIL_UTC; each run ends at its mandate's hard_end_utc. Changes no agent config, toolset, EVE Core,
  VHR, LGX or run-path file.

## Not established

E-3 (independent verification), T7 anchor, exclusive EVE control of the agents, the agents' runtime tools and network
egress, a hard cost limit, quote quality beyond the deterministic check and the reviewer's acceptance criteria.

Approved by: Joakim Eklund, by a separate OWNER-GO, typing the MISSION_ID and signing a mandate that names the
sha256 of exactly this text.
