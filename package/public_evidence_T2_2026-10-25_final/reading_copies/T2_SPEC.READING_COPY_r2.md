READING COPY - NOT EVIDENCE - NOT PART OF THE FROZEN CHAIN
derived from  chain02/r2/lgx_c2/T2/T2_SPEC.md
original      sha256 8965d91e25e36deb26272ab2d9d4b39b9c8a933f73200b8c5a6ae0b5e3cbd00d  bytes 9503  (listed in original/LGX_C2_T2_EVIDENCE_FREEZE_2026-10-24.md)
this file     has its OWN sha256; it cannot be checked against the frozen manifest and never replaces the original
redactions    marked [REDACTED: ...]; line N of the original = line N+7 of this file; see PUBLICATION_MANIFEST.md
original      WITHHELD (owner decision 2026-10-25); only this reading copy (revision r2) is distributed
==========================================================================================================
# LGX-C2 T2 - RUN SPECIFICATION (prepared; nothing activated, nothing run)

```text
CLASS     SPECIFICATION (OWNER-GO "EVE 057 - T2 Preparation GO" 2026-10-24; T2_EXECUTION_HOLD)
BASIS     LGX_C2_T2_DECISION_BASIS_2026-10-24.md fb7daa5a... (Atlas v78); owner decisions D-1..D-5 2026-10-24
MISSION   LGX-T2-QUOTE - quote draft from a fictional customer inquiry (D-1)
          chain02\r2\missions\LGX-T2-QUOTE\TASK.md              6d575090fcbfa47a8d050087a3ae93706aae20e8e81659367a03dd4b054c431d
          chain02\r2\missions\LGX-T2-QUOTE\MISSION_HOLD_LIFT.md 456652d461549fe1c59e64ea56ec3371bf3d0bf585899f285e363326973338a7
WRAPPER   N3 r4 RUN_TASK_LGX_WSL_r4.sh 3552fdca... only (LOCKED, never edited); activated copy
          RUN_TASK_LGX_WSL_r4_T2.sh = N3 r4 with only line 81 set to R = sha256 of the final activation record
DRAFT     chain02\r2\lgx_c2\T2\T2_ACTIVATION_RECORD_DRAFT.md     efd1c6f4311e7406c6632afb53286950c1959e32cd4ba8c663f20630c684db77
ROLES     LangGraph (N1 r3) orchestrates the hand-offs in a fixed line of 9 nodes and has no model of its own; the
          Hermes agents A (worker) and B (reviewer) do the work; EVE controls admission, mandate, binding and
          traceability. LangGraph is never presented as an autonomous agent.
```

## 1 Decisions applied

```text
D-1  mission LGX-T2-QUOTE, fictional data only
D-2  cost: MAX_COST_CAP_USD 2.00 in the mission text; the run is started with COST_CAP 2.00. Estimate-based stop rule
     before each agent turn (after-the-fact Hermes estimates), NOT a hard limit: a single agent turn can exceed it;
     RUN_TIMEOUT 600 s per agent; ledger STOP 15 USD; actual cost = ledger after the run. Observed comparable cost:
     057G1 0.275440 USD (estimate). No hard cost guarantee is claimed anywhere.
D-3  activation window 60 minutes (VALID_UNTIL_UTC = ACTIVATED_UTC + 60 min); one activation record, consumed once,
     one session; the wrapper is started with WINDOW_MIN 60 (mandate hard end <= 60 min after start)
D-4  any STOP after the activation is consumed (including a wrong passphrase at step 3) ends T2 for this activation;
     a new attempt needs a new OWNER-GO and a new activation record; no automatic retry
D-5  O-C: reference measurement of the venv interpreter by T2_PRECHECK_WSL.sh (K3); W1d unchanged; not a gate
```

## 2 Run procedure (only after a separate T2 OWNER-GO)

```text
P-0  owner: T2_PRECHECK_WSL.sh result T2_PRECHECK_OK registered (K1 pins, K2 RF-9, K4 W1d, K5 project state; K3 O-C
     reference recorded)
P-1  producer: OWNER-GO record (create-only) binding N3 r4 3552fdca, N1 r3 865f20a9, mission LGX-T2-QUOTE, TASK and
     mission-text sha256, draft efd1c6f4, cost 2.00 (soft), window 60 min, D-4
P-2  producer, immediately before the owner starts: final record = draft with exactly 3 substitutions (STATUS ACTIVE,
     ACTIVATED_UTC, VALID_UNTIL_UTC = +60 min); R = its sha256; created create-only as
     chain02\r2\lgx_c2\activations\N3R3_ACT_<R>.md together with the empty folder activations\consumed\ (needed by
     the wrapper's atomic mkdir); activated copy chain02\r2\lgx_c2\RUN_TASK_LGX_WSL_r4_T2.sh = N3 r4 with only line
     81 set to R; checks V-1..V-5 (as T1-1b): record = draft + 3 substitutions, sha = R, diff = line 81 only,
     normalised copy sha = 3552fdca, record names the copy, N3 r4 and LGX-T2-QUOTE; all measured on D: and
     registered (handover + pointer CAS) before the owner starts
P-3  owner, within the 60-minute window, in PowerShell (one run):
       wsl -d Ubuntu-22.04 bash <PROJECT>/chain02/r2/lgx_c2/RUN_TASK_LGX_WSL_r4_T2.sh LGX-T2-QUOTE 2.00 60
     expected owner inputs, and only these:
       step 2  check the preview (mission LGX-T2-QUOTE, task sha 6d575090..., mission-text sha 456652d4..., agents A
               then B, cost cap 2.00, window), then type LGX-T2-QUOTE
       step 3  owner GO key passphrase (up to 3 attempts; a failed signing = STOP, D-4)
       step 4  eve-c2 key passphrase
     anything else, or a preview that differs from the OWNER-GO record -> Ctrl-C, nothing typed
P-4  producer after the run: evidence (section 3) measured and registered; T2_QUOTE_CHECK.py run read-only; ledger
     before/after read from the run evidence; result record; Atlas
```

## 3 Evidence required (all registered by sha256 + bytes)

```text
E-1  chain02\r2\missions\LGX-T2-QUOTE\RUN_<session>.txt (wrapper output incl. step 0 env gate lines, RESULT line)
E-2  MANDATE_<session>.txt and .sig; C2X_RESULT_<session>.txt; RESULT_SUMMARY_<session>.md; OUTCOME_UNKNOWN_<session>.json
     if written (R-B)
E-3  chain02\runs\C2-live-<session>.json (client record) and chain02\runs\<session>\ (link\LINK.json, out\H1\a_out\*,
     out\H2\a_out\REVIEW.md, manifests)
E-4  activation record, CONSUMED.txt in activations\consumed\<R>\, activated copy (derived sha recorded)
E-5  server evidence receipts / evidence-status as reported in E-1 (client-reported, server-checked; not E-3)
E-6  T2_QUOTE_CHECK.py output over TASK.md, out\H1\a_out and out\H2\a_out
E-7  ledger before/after and the Hermes cost estimates per agent as reported in E-1 / RESULT_SUMMARY
```

## 4 Result classification (layers kept separate)

```text
L-1 chain        wrapper 'RESULT status=PASS step=5 verdict=ALL_PASS chain=CHAIN_VERIFIED' (client ALL_PASS and C2-X
                 CHAIN_VERIFIED) - otherwise the chain result is FAIL or STOP as printed
L-2 work         T2_QUOTE_CHECK.py DETERMINISTIC_PASS (Q1-Q8; independent of both agents)
L-3 reviewer     agent B 'VERDICT: ACCEPT' or 'VERDICT: REJECT' (same vendor, separate context; not E-3)
L-4 server       evidence receipts (client-reported, server-checked)
L-5 independent  NOT_ESTABLISHED
T2 demonstration result = L-1 PASS and L-2 DETERMINISTIC_PASS; L-3 and L-4 reported beside it. An R-B
OUTCOME_UNKNOWN receipt means the outcome is unknown, never PASS. No layer is upgraded by another.
```

## 5 Stop conditions

```text
before P-2   precheck not OK; any pin differs; RF-9 differs; W1d differs; project activations folder or activated copy
             already present; ledger margin (15 - ledger) below 2.00 as last measured -> no activation
in the run   every wrapper STOP is final (D-4); no retry; no re-activation without a new OWNER-GO
prompts      section 2 P-3; anything else -> Ctrl-C
after        evidence registered before interpretation; agent output never corrected; a DETERMINISTIC_FAIL or a B
             REJECT is reported as such
```

## 6 Agent permissions (owner requirement: established, or an open T2 decision)

```text
status   NOT_ESTABLISHED - cannot be established inside this preparation GO (it forbids server contact)
evidence (existing read-only records, static reads, Hermes never executed):
  [REDACTED: agent container network / toolset configuration detail]
  [REDACTED: agent container network / toolset configuration detail]
  [REDACTED: agent container network / toolset configuration detail]
  [REDACTED: agent container network / toolset configuration detail]
  [REDACTED: agent container network / toolset configuration detail]
  [REDACTED: agent container network / toolset configuration detail]
  run path   the agent needs outbound access to its model provider to work at all, so 'no network' is not available
             without a new egress design (not in scope: no new architecture without separate approval)
  prompt     'Do not use [REDACTED: service name], do not contact anyone, do not publish anything' (server r3k3 receive prompt) -
             an instruction, not a technical barrier
  evidence after a run: the client receives the agent stdout (base64) and the output files; the agents' internal
             tool-call logs inside the containers are not collected by the run path
D-6 (open, for the T2 OWNER-GO):
  (a) run T2 with permissions NOT_ESTABLISHED, stated in the GO; risk reduced by fictional data only, no credentials
      in TASK.md, file-only output, post-run review of the agent stdout in E-1
  (b) first a separate read-only server inventory GO (no agent start, 0 USD agent cost): container network and
      firewall rules, effective toolset list from the installed Hermes code, [REDACTED: service name] MCP reachability; result
      registered; then the T2 GO
  (c) a technical restriction (egress allow-list to the model provider only, toolset reduction) - new configuration /
      architecture, needs its own approval and design; not proposed here
```

## 7 Boundaries

```text
RV-7     the activation record is unsigned (procedural gate); the owner-signed mandate and the server's single
         consumption are the authoritative controls
RV-5     only the N3 r4 copy is activated; r2/r3 are never activated (they still accept --upload)
O-B      chain02\runs is written legitimately by the run; changes are detected, not prevented
O-C      interpreter binary referenced (K3), not pinned by W1d
L-C1     EVE admission is enforced on the owner PC; the server cannot see it
L-PAR    first live execution of N1 r3 (only stub-tested before); parity limited by R3-F1, R3-F2, R3-F4, R-DNE
P-3      the wrapper exit code is tee's; the RESULT line decides
claims   same-vendor producer; B same vendor separate context; no E-3; not legal or tax advice; fictional data
```
