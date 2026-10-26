# EVE - T2 governed agent handoff - evidence package (FINAL LOCAL PACKAGE, NOT PUBLISHED)

```text
STATE      final local package 2026-10-25 under owner GO "T2 Public Evidence Final Package". Not published.
           Publication needs a separate owner GO.
RUN        one owner-approved test run, session LGX-T2-QUOTE-20261024T130334Z, 2026-10-24, fictional test data
           (a housing association asks for a stairwell painting quote; all names marked FICTIONAL)
SETUP      LangGraph orchestrates a fixed 9-node line; two Hermes agents (A worker, B reviewer) on model
           anthropic/claude-sonnet-5-5; EVE controls admission, mandate binding, handoff checks and traceability
```

## 1 What the distributed originals show (and where)

```text
mandate        MANDATE_...txt + .sig: task, agents, model, cost cap, time window; OpenSSH signature (see G-1)
chain          C2-live-...json: verdict ALL_PASS, 15 checks PASS (admission of H1/H2, M-3 handoff check before
               agent B, one start per agent, replay of the H2 record -> ALREADY_CLOSED)
               C2X_RESULT_...txt: FAILS [] RESULT CHAIN_VERIFIED
handoffs       eve/verified_handoff_v11_records.json, eve/determination_records.json, executor/*: recipient named,
               scope bound; consumed/*.json and CONSUMED.txt: one-time use markers
work           out/H1 (agent A quote draft), out/H2/REVIEW.md (agent B: VERDICT: ACCEPT - an agent statement)
quote check    T2_QUOTE_CHECK_OUTPUT.txt: Q1..Q8 ok, RESULT QUOTE_CHECK DETERMINISTIC_PASS (independent of the agents)
server         RESULT_SUMMARY_...md: 2/2 evidence items stored with receipts (client-reported, server-checked)
independent    NOT_ESTABLISHED (RESULT_SUMMARY_...md status layer 4)
```

## 2 What is NOT distributed and what that limits

- The main result record LGX_C2_T2_RESULT_2026-10-24.md is withheld for security reasons (server firewall state
  and signing-attempt detail). It stays unchanged in the frozen chain; its name and sha256 are in
  PUBLICATION_MANIFEST.json (WITHHELD_SECURITY_METADATA). Outside reviewers therefore cannot read the producer's
  consolidated result classification; the layers above are shown by the distributed originals listed in section 1.
- RUN (wrapper trace) and T2_SPEC (run specification) are distributed only as redacted READING COPIES. They are NOT
  evidence, carry their own sha256 and cannot be checked against the frozen manifest.
- 6 further files are withheld (run wrapper script, four isolation-window logs, environment precheck): server
  addresses, owner environment, container topology and egress results.

## 3 What this package does NOT establish

- not independently verified; not externally audited; not certified; not fully reproducible
- same producer built and checked the run; no independent reviewer; no external time anchor
- G-1 NOT PERFORMED: the mandate signature has not been checked against an owner-supplied public key; a prepared
  check (g1/G1_CHECK.sh) exists. Even when it passes, it proves only signature/key correspondence, not key control
- G-2 NOT RESOLVED: the run client, server script and chain verifier pinned in the mandate (lines 5-7) are not in
  this package; the chain checks cannot be re-run from it
- L-5 independent verification: NOT_ESTABLISHED
- the agents' runtime tools and network egress were not established; no network isolation, production safety or
  hard cost limit is claimed

## 4 Layout and check

```text
original/LGX_C2_T2_EVIDENCE_FREEZE_2026-10-24.md   frozen manifest, byte-identical (sha256 f9468fd3..., 8833 bytes)
evidence/<path from the manifest>                  39 unchanged originals
reading_copies/                                    2 redacted reading copies (NOT evidence)
PUBLICATION_MANIFEST.json                          status of all 48 originals, reading copies, support files
VERIFY_PACKAGE.py                                  python3 VERIFY_PACKAGE.py  -> RESULT PACKAGE_INTEGRITY_OK
g1/G1_CHECK.sh                                     prepared signature check (not run)
```

VERIFY_PACKAGE.py checks file identity against the manifest text only; it does not prove the manifest's
authenticity or the truth of any statement.

## 5 Known metadata exposure

```text
original manifest  project root D:\EVE11\Projects\057_agent_platform, the name of the owner's shared review folder,
                   and the file names (not contents) of all 48 files including withheld ones
distributed files  server short host name eve-agents-01, agent container names, server-internal paths
                   (/opt/data/work_c2, /var/log/eve-agents, /var/backups/eve-h2), local project paths
                   (/mnt/d/EVE11/Projects/057_agent_platform/...) in C2-live, C2X and RESULT_SUMMARY
```
