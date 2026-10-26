VERDICT: ACCEPT

Findings (all acceptance criteria checked against TASK.md):
- CSV header is exact. Rows P-01..P-07 use the correct item_ids, units and unit prices.
- All quantities come from the customer: 210 m2 walls (P-02 and P-03), 64 m2 ceiling, 12 doors, 38 lm railing. P-01 and P-07 appear once each.
- Arithmetic checked: 2500 + 19950 + 25200 + 8960 + 7800 + 11780 + 900 = 77090.00. VAT 25 % = 19272.50. Total = 96362.50. Every line total equals quantity x unit price.
- Nothing outside the price list is priced. The door frame replacement and the cellar stairs are unpriced and listed as open questions in ASSUMPTIONS_AND_QUESTIONS.md. The cellar stairs have no stated area and no price-list item.
- OFFER_DRAFT.md line 1 is exactly "DRAFT - NOT SENT". TOTAL_EX_VAT_SEK, VAT_SEK and TOTAL_INC_VAT_SEK each appear once and match the CSV. The draft is in Swedish and states 30 days validity.

Minor deviations (not blocking):
- CSV descriptions for P-03, P-04 and P-05 use " - " where the price list has ", ". This was needed to avoid commas in the CSV, as the task requires.
- OFFER_DRAFT.md says "(se frågor)" but contains no actual question text. The questions are only in ASSUMPTIONS_AND_QUESTIONS.md. Those questions are written in English.
- RESULT.md lists the file path as the ...-H1 work folder, not H2. This looks like a path label from the earlier run. The files themselves were delivered in result/.
