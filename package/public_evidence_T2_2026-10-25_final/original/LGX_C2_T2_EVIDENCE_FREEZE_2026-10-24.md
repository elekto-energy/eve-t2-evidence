# LGX-C2 T2 EVIDENCE FREEZE - LGX-T2-QUOTE session LGX-T2-QUOTE-20261024T130334Z - 2026-10-24

```text
CLASS      EVIDENCE FREEZE MANIFEST (producer: Claude; create-only; immutable). Copy and verify only: no original changed,
           no agent run, no new approval
AUTHORITY  the D: pointer D:\EVE11\Projects\057_agent_platform\_HANDOVER_CURRENT.md (Atlas); this manifest is declared there with
           every file below (sha256 + bytes). Drive (EVE Shared Atlas, 01_AUTO_SYNC versions/<utc>/) is the shared review copy
           written by the scheduled sync, never a source of truth
BASIS      result record LGX_C2_T2_RESULT_2026-10-24.md (Atlas v101, pointer 34aa9e1c07b57d0cecb38537671b68311324fd2f2026437aee4d0f44b9027bad)
LAYERS     L-1 chain PASS (ALL_PASS + CHAIN_VERIFIED); L-2 DETERMINISTIC_PASS; L-3 agent B VERDICT: ACCEPT; L-4 2/2 server
           receipts (client-reported, server-checked); L-5 independent verification NOT_ESTABLISHED
LABEL      TESTED_LOCAL, one owner-approved run, fictional data; same producer built and verified (not E-3); no T7 anchor;
           no claim of network isolation, production safety or complete agent isolation
PATHS      relative to D:\EVE11\Projects\057_agent_platform\; 0-byte lock files of the session are not listed
```

## result

```text
0df6fa4a6570a7fbebfa293cdaa3da9944f8fb9ff3035bf29f795ab65db131e2     5834  LGX_C2_T2_RESULT_2026-10-24.md
```

## work product (agent A)

```text
14215d27c8bc6e77d23d19f647c3bcb21a5393b1ceb9b4e818eeb06c4b679af4     1241  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\out\H1\a_out\OFFER_DRAFT.md
d9cab3dbcdc46d9c5cdec06f309687f0c719f41a31a2073c4de918df278108ea      548  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\out\H1\a_out\CALCULATION.csv
19745abb6f7cea32365763c3e26a15233af38e444b2cd0d595447a241298ae66     1274  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\out\H1\a_out\ASSUMPTIONS_AND_QUESTIONS.md
b1eaa62787f9537bfd14f60c8840eb11b3ef92472fefd8f27bb2802e7bced935      480  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\out\H1\a_out\RESULT.md
aa7a7e47f2f94bab1debba3a0c0e715a703c7d754e4c022965fde0dc1f7ee4e9      334  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\out\H1\A_OUT_MANIFEST.sha256
ae09e4040f52846890e8ed44190172b76255a0ce0f2369bf99950354152ffae5    10240  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\out\H1\a_out.tar
```

## review (agent B)

```text
16537de90f879dc8c8fde34e7bfb1a2051a1b590bbfa2b99e71104e065afbcb6     1420  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\out\H2\a_out\REVIEW.md
c0042cc960159fd1b217c6a13aba76c1199f20ad7f7c023c1969f39f0feb3dfa       76  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\out\H2\A_OUT_MANIFEST.sha256
9145faa2828d8899be1fe1cc34fd5e9a01d70ca7f375f74f7f5f47d5333daae8    10240  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\out\H2\a_out.tar
```

## mandate and owner approval

```text
4494612f489fb858780906075880900e51181a564d2648be277bca68f942eaab      816  chain02\r2\missions\LGX-T2-QUOTE\MANDATE_LGX-T2-QUOTE-20261024T130334Z.txt
633bee9a64969a0bb72fb83b76227884d4aa6265a68dd23287efda9baea13338      310  chain02\r2\missions\LGX-T2-QUOTE\MANDATE_LGX-T2-QUOTE-20261024T130334Z.txt.sig
88e70d0fe04cad9b1ebc8fa04e79ce97f6b9c932972a614eb2648a6bbfb64b43     1765  chain02\r2\lgx_c2\T2\T2_OWNER_GO_RECORD.md
654226842f988bd162a0fcc5add09b152360aac446f77a8ad39e65b47614bc77     1119  chain02\r2\lgx_c2\activations\N3R3_ACT_654226842f988bd162a0fcc5add09b152360aac446f77a8ad39e65b47614bc77.md
43e2d5a159aa1080909a7fcff1c3af62b7392bd9e173deb84ec154621c9d1e27      164  chain02\r2\lgx_c2\activations\consumed\654226842f988bd162a0fcc5add09b152360aac446f77a8ad39e65b47614bc77\CONSUMED.txt
1c945f698397984cb8619eb662160cfdbf6f4dbfc7f84f6de2bd457e7f3ee510    40199  chain02\r2\lgx_c2\RUN_TASK_LGX_WSL_r4_T2.sh
```

## mission inputs

```text
6d575090fcbfa47a8d050087a3ae93706aae20e8e81659367a03dd4b054c431d     4121  chain02\r2\missions\LGX-T2-QUOTE\TASK.md
456652d461549fe1c59e64ea56ec3371bf3d0bf585899f285e363326973338a7     2525  chain02\r2\missions\LGX-T2-QUOTE\MISSION_HOLD_LIFT.md
8965d91e25e36deb26272ab2d9d4b39b9c8a933f73200b8c5a6ae0b5e3cbd00d     9503  chain02\r2\lgx_c2\T2\T2_SPEC.md
```

## run trace

```text
22d43e5cd4e797ffd4dd2e38dd66e1b7117aa6042a81950841319dfb9ea2b627    12364  chain02\r2\missions\LGX-T2-QUOTE\RUN_LGX-T2-QUOTE-20261024T130334Z.txt
02df91531127341c145c04ed2d2821d2337552fb5c86dda981b5ab0120d021f8    16566  chain02\runs\C2-live-LGX-T2-QUOTE-20261024T130334Z.json
3615753028856a239db86badf96dd9fa98f19c4f97d0cab59362d772e7d826b5      748  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\link\LINK.json
0f2d3024edf8d7d24594af3c8cb27617b68183553b57a2dc1f42466f088daa4e     4820  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\server_io.log
d90a7154f85f33c936b44f8ed4d4de375c603d0488ab9317cb547ca4645a06a1      159  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\pkg\H1\MANIFEST.sha256
7dafc199d898d01b0af7b4f39888c12f230a07c23deac15966446968f3e5dd60    10240  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\pkg\H1\package.tar
1213a9dd1b2264806154b6c5d7253a89dec97d6113ca0b84c882f45a2b405e77      597  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\pkg\H2\MANIFEST.sha256
78c783cc91735d800fca7c100e06cc10f4ee96662424c7a627222bc82c26472b    20480  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\pkg\H2\package.tar
5e1cabb02689f79c2719f830edde1efa2a1ffb7c86931f3f1556623bf09f523d      254  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\consumed\79abb1472f4dd56ef9e97decaa11dac7e63df41a62e173db9e447ff1b168408d.json
ac53b4fffd6d467b86c75ec03f20be947fa57b344c07fe1bf382d9b4c174cc17      254  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\consumed\9d9b85ef0e27f94727e78fb39dd0f120c667673c9c4db89d5effc4256330de65.json
```

## EVE / VHR records

```text
119e89d64e7a50e0abe5e96a42d18dad5a43a27e0fd780d74594cf3f746938eb    11499  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\eve\determination_records.json
4860f171e6e2081d8da9008d00c71fc240611e3c789f32ed6c37b796b50b942f     8407  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\eve\verified_handoff_v11_records.json
8fee17d4a5d70aba3490ca50af31014da8c55e6234c21539c82a6ce189b51f04     1217  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\executor\intents\EVE-VHR11-LOCAL-000001.json
c118560d2f90f395a548c1755b9727306601361eacbad929ca6a3107e0270877     1219  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\executor\intents\EVE-VHR11-LOCAL-000002.json
9dae2b0e3f61c821b26ea26944000d795c491cb47e3b44ac57f51f9b907541a3     1116  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\executor\journals\EVE-VHR11-LOCAL-000001.jsonl
d352fbfb6ec8bed57d066df158ab66061f07b294c2546626eadfdc9a5a3d0083     1116  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\executor\journals\EVE-VHR11-LOCAL-000002.jsonl
61e49717c5fe1e0d8960be2a5e448a776d6e7019d11d4db381e1ac42faedc6a7      340  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\executor\outcomes\EVE-VHR11-LOCAL-000001.json
abd8b98053dd7cad67cba9ce3e65c97abf0cfa457fe0b867f973500dd97f71c0      340  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\executor\outcomes\EVE-VHR11-LOCAL-000002.json
c7c1735eaa2028266316eb3221ab997d7278aeaa403ba24abc73bb4878b16cea      131  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\executor\reservations\EVE-VHR11-LOCAL-000001.json
2ca91bacb29d33093e155cc45a86d410cdf7bc07c674d2c8bfd681e862ade18d      131  chain02\runs\LGX-T2-QUOTE-20261024T130334Z\executor\reservations\EVE-VHR11-LOCAL-000002.json
```

## verification and server receipts

```text
7d13984cad9a9ce0230a59b0295de5dba0a34e71ef6d31ca83fb2bac27bf21ed      937  chain02\r2\missions\LGX-T2-QUOTE\C2X_RESULT_LGX-T2-QUOTE-20261024T130334Z.txt
798eee2de416d831ef48b5e03b0f16bd51aa5ca9aaba893cd65282612d80af35     3880  chain02\r2\missions\LGX-T2-QUOTE\RESULT_SUMMARY_LGX-T2-QUOTE-20261024T130334Z.md
57fd0ff294624ee075c03a74c54c55a498f4df27ab799469fb851ddaf27615b5      417  lgx_c2_results\2026-10-24\T2_RESULT_LGX-T2-QUOTE-20261024T130334Z\T2_QUOTE_CHECK_OUTPUT.txt
67d8184ceaf8f49843869f0ad11c0de339a504c66e474f532a37bf47b1243deb     6153  chain02\r2\lgx_c2\T2\T2_QUOTE_CHECK.py
```

## isolation window

```text
7dc8b691cf4792977f612478ec1e89cc3e1a599084489aedaac0c379bd1da732     6189  chain02\r2\h2\H2_CHANGE_20261024T125556Z.txt
42f341a14853e69da81945999df3ea3c9840b30ce34ea5d742c834e7d8295f90     1379  chain02\r2\h2\H2K_CHECK_20261024T125801Z.txt
994426b386f342d887f5908a5c3fb4cf36917d853a7d42fd137682827438a0b0      747  chain02\r2\h2\H2_CANARY_T2_20261024T130725Z.txt
71d820e15cfd6dcd2bec12735a49fdb06921af5f21e5a3aaf28d410e21f108f0     3796  chain02\r2\h2\H2_ROLLBACK_20261024T130828Z.txt
ebc9a629d0fd17c577efb28406da7447410a51618e789233a6959cd380a070a0     3193  lgx_c2_results\2026-10-24\T2_PRECHECK_20261024T125552Z\T2_PRECHECK_LOG.txt
```

## Use

```text
baseline   reference for later agent runs (compare sha256 of the same roles)
material   demonstration film and eveverified.com: quote only these files, with their sha256 and the layer labels above
```
