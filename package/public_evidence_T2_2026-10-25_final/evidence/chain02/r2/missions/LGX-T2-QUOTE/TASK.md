# TASK LGX-T2-QUOTE - quote draft from a customer inquiry (synthetic test data)

Owner mission for the 057 EVE work chain (agent A = worker, agent B = reviewer). Agent A receives ONLY this file.
ALL company names, people and figures below are FICTIONAL TEST DATA. Nothing is sent to anyone: the result is a
draft that stays in the work folder.

## Role

You work for the fictional painting company "EXEMPEL Maleri AB (FICTIONAL)". A fictional housing cooperative has
sent the inquiry below. Prepare a quote DRAFT in Swedish, using ONLY the price list and terms in this file.

## Customer inquiry (verbatim, fictional)

```text
Från: Styrelsen, Bostadsrättsföreningen Testgården (FIKTIV)
Ämne: Offertförfrågan målning av trapphus

Hej!

Vi vill ha en offert på målning av vårt trapphus. Det gäller:

1. Väggarna i trapphuset, totalt 210 kvadratmeter. Väggarna har sprickor och behöver spacklas och slipas innan
   de målas.
2. Taket i trapphuset, totalt 64 kvadratmeter.
3. Våra 12 lägenhetsdörrar mot trapphuset. Bara utsidan mot trapphuset ska målas.
4. Trappräcket, totalt 38 löpmeter.
5. Dörrkarmen vid entrédörren är trasig och behöver bytas.
6. Vi vill gärna också få källartrappan målad, men vi vet inte hur många kvadratmeter den är.

Vi vill att ni tar hand om skydd och städning efteråt.

Med vänliga hälsningar
Styrelsen, Brf Testgården (FIKTIV)
```

## Price list (the ONLY allowed prices; SEK excluding VAT; materials included)

| item_id | description | unit | unit_price_sek |
|---|---|---|---|
| P-01 | Etablering och skydd (per uppdrag) | st | 2500 |
| P-02 | Spackling och slipning av vägg | m2 | 95 |
| P-03 | Målning vägg, två strykningar | m2 | 120 |
| P-04 | Målning tak, två strykningar | m2 | 140 |
| P-05 | Målning dörr inklusive karm, en sida | st | 650 |
| P-06 | Målning trappräcke | lm | 310 |
| P-07 | Bortforsling och slutstädning (per uppdrag) | st | 900 |

## Terms

- VAT (moms) is 25 % of the subtotal excluding VAT.
- P-01 and P-07 appear exactly once in every quote.
- Prices are fixed. No discounts, no surcharges, no other items.
- Work that is not in the price list, or whose quantity is not stated by the customer, is NOT priced. It is listed as
  an open question for the customer instead. Never invent a price or a quantity.
- The quote is valid 30 days.

## Output (write all files in your work folder)

1. `CALCULATION.csv` - UTF-8, comma separated, dot as decimal separator, no thousands separator, exactly this header:
   `item_id,description,quantity,unit,unit_price_sek,line_total_sek`
   then one row per priced item (item_id from the price list, quantity as an integer, unit as in the price list,
   unit_price_sek and line_total_sek with exactly two decimals, line_total_sek = quantity x unit_price_sek), then
   exactly three summary rows with empty middle fields:
   `SUBTOTAL,,,,,<amount>` and `VAT_25,,,,,<amount>` and `TOTAL,,,,,<amount>` (two decimals each).
   Do not put commas inside the description.
2. `OFFER_DRAFT.md` - the quote draft in Swedish to the cooperative. Its first line is exactly `DRAFT - NOT SENT`.
   It contains, each on its own line and exactly once, the machine-readable totals
   `TOTAL_EX_VAT_SEK <amount>`, `VAT_SEK <amount>`, `TOTAL_INC_VAT_SEK <amount>` (two decimals, equal to the CSV).
3. `ASSUMPTIONS_AND_QUESTIONS.md` - every assumption you made and every open question to the customer, including
   each requested item you did not price and why.
4. `RESULT.md` - what you did and the list of every file you produced.

## Reviewer acceptance (agent B)

Agent B accepts only if: every priced row uses an item_id and the exact unit price from the price list; every
quantity is stated by the customer; every line total, the subtotal, the VAT and the total are arithmetically
correct; P-01 and P-07 appear exactly once; nothing outside the price list is priced; every requested item that is
not priced appears as an open question; `OFFER_DRAFT.md` starts with `DRAFT - NOT SENT` and its totals equal the CSV.
Agent B lists every deviation it finds. Agent B does not correct the files.
