r"""LGX-C2 T2 post-run deterministic check for mission LGX-T2-QUOTE (prepared under OWNER-GO "EVE 057 - T2
Preparation GO" 2026-10-24; read-only on the evidence; 0 USD; independent of agent B's verdict).
Usage: python3 -I -B T2_QUOTE_CHECK.py <TASK.md> <H1 a_out folder> <H2 a_out folder>
The price list is parsed from TASK.md itself (whose sha256 must equal TASK_SHA256 below). The expected quantities
are the ones the customer states in the inquiry of TASK.md (fixed below, not given to the agents as an answer).
Checks (all required for DETERMINISTIC_PASS):
  Q1 TASK.md sha256 = TASK_SHA256; price list parsed: exactly P-01..P-07 with integer prices
  Q2 files present in H1 a_out: CALCULATION.csv, OFFER_DRAFT.md, ASSUMPTIONS_AND_QUESTIONS.md, RESULT.md
  Q3 CALCULATION.csv: exact header; item rows = exactly the expected item ids with the expected quantities (each
     once); unit as in the price list; then exactly SUBTOTAL, VAT_25, TOTAL rows with empty middle fields; nothing else
  Q4 every unit_price_sek = price-list price (two decimals)
  Q5 every line_total_sek = quantity x unit price, exactly (two decimals)
  Q6 SUBTOTAL = sum of line totals; VAT_25 = SUBTOTAL x 0.25 rounded half-up to 0.01; TOTAL = SUBTOTAL + VAT_25
  Q7 OFFER_DRAFT.md: first line exactly 'DRAFT - NOT SENT'; lines TOTAL_EX_VAT_SEK, VAT_SEK, TOTAL_INC_VAT_SEK each
     exactly once and equal to the CSV summary rows
  Q8 ASSUMPTIONS_AND_QUESTIONS.md names the two unpriced requests (keyword presence only, case-insensitive:
     'dörrkarm' and 'källartrapp') - a presence check, not a quality judgement
Reported, not part of DETERMINISTIC_PASS: agent B's verdict line in H2 REVIEW.md (exactly one 'VERDICT: ACCEPT' or
'VERDICT: REJECT' expected).
"""
import hashlib
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

TASK_SHA256 = "6d575090fcbfa47a8d050087a3ae93706aae20e8e81659367a03dd4b054c431d"
EXPECTED = {"P-01": 1, "P-02": 210, "P-03": 210, "P-04": 64, "P-05": 12, "P-06": 38, "P-07": 1}
HEADER = "item_id,description,quantity,unit,unit_price_sek,line_total_sek"
FILES = ("CALCULATION.csv", "OFFER_DRAFT.md", "ASSUMPTIONS_AND_QUESTIONS.md", "RESULT.md")
MONEY = re.compile(r"^-?\d+\.\d{2}$")
C = Decimal("0.01")


def money(s):
    return Decimal(s) if MONEY.fullmatch(s) else None


def main():
    task_p, h1, h2 = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    r, info = {}, []
    raw = task_p.read_bytes()
    prices, units = {}, {}
    for m in re.finditer(r"^\| (P-0[1-7]) \| [^|]+ \| (st|m2|lm) \| (\d+) \|$", raw.decode("utf-8"), re.M):
        prices[m.group(1)], units[m.group(1)] = Decimal(m.group(3)), m.group(2)
    r["Q1_task_and_price_list"] = hashlib.sha256(raw).hexdigest() == TASK_SHA256 and sorted(prices) == sorted(EXPECTED)
    r["Q2_files_present"] = all((h1 / f).is_file() for f in FILES)
    rows, summ, ok3, ok4, ok5 = [], {}, False, False, False
    csv_p = h1 / "CALCULATION.csv"
    if csv_p.is_file():
        lines = csv_p.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip("\n").split("\n")
        body = lines[1:] if lines else []
        items = [l.split(",") for l in body[:-3]]
        tail = [l.split(",") for l in body[-3:]] if len(body) >= 3 else []
        ok3 = (bool(lines) and lines[0] == HEADER and len(items) == len(EXPECTED)
               and all(len(f) == 6 for f in items)
               and sorted(f[0] for f in items) == sorted(EXPECTED)
               and all(f[0] in EXPECTED and re.fullmatch(r"\d+", f[2]) and int(f[2]) == EXPECTED[f[0]]
                       and f[3] == units.get(f[0]) and f[1].strip() != "" for f in items)
               and [t[0] for t in tail] == ["SUBTOTAL", "VAT_25", "TOTAL"]
               and all(len(t) == 6 and t[1:5] == ["", "", "", ""] for t in tail))
        if ok3:
            rows = items
            summ = {t[0]: money(t[5]) for t in tail}
            ok4 = all(money(f[4]) is not None and money(f[4]) == prices[f[0]] for f in items)
            ok5 = ok4 and all(money(f[5]) is not None and money(f[5]) == (prices[f[0]] * int(f[2])).quantize(C) for f in items)
    r["Q3_csv_structure_and_quantities"] = ok3
    r["Q4_unit_prices"] = ok4
    r["Q5_line_totals"] = ok5
    ok6 = False
    if ok5 and None not in summ.values():
        sub = sum((money(f[5]) for f in rows), Decimal("0.00"))
        vat = (sub * Decimal("0.25")).quantize(C, rounding=ROUND_HALF_UP)
        ok6 = summ["SUBTOTAL"] == sub and summ["VAT_25"] == vat and summ["TOTAL"] == sub + vat
        info.append("computed subtotal %s vat %s total %s" % (sub, vat, sub + vat))
    r["Q6_summary_rows"] = ok6
    ok7 = False
    od = h1 / "OFFER_DRAFT.md"
    if od.is_file() and ok6:
        ol = od.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
        def one(key):
            v = [l for l in ol if re.fullmatch(r"%s -?\d+\.\d{2}" % key, l.strip())]
            return money(v[0].strip().split(" ")[1]) if len(v) == 1 else None
        ok7 = (ol[0] == "DRAFT - NOT SENT" and one("TOTAL_EX_VAT_SEK") == summ["SUBTOTAL"]
               and one("VAT_SEK") == summ["VAT_25"] and one("TOTAL_INC_VAT_SEK") == summ["TOTAL"])
    r["Q7_offer_draft_marker_and_totals"] = ok7
    aq = h1 / "ASSUMPTIONS_AND_QUESTIONS.md"
    aqt = aq.read_text(encoding="utf-8").lower() if aq.is_file() else ""
    r["Q8_unpriced_requests_named"] = "dörrkarm" in aqt and "källartrapp" in aqt
    rv = h2 / "REVIEW.md"
    vl = [l.strip() for l in rv.read_text(encoding="utf-8").splitlines() if l.strip().startswith("VERDICT:")] if rv.is_file() else []
    verdict = vl[0] if len(vl) == 1 and vl[0] in ("VERDICT: ACCEPT", "VERDICT: REJECT") else "UNCLEAR(%d lines)" % len(vl)
    ok = all(r.values())
    print("QUOTE_CHECK %s %s" % ("PASS" if ok else "FAIL", " ".join("%s=%s" % (k, "ok" if v else "FAIL") for k, v in r.items())))
    for x in info:
        print("QUOTE_CHECK " + x)
    print("QUOTE_CHECK reviewer_b %s (reported; not part of the deterministic result)" % verdict)
    print("RESULT QUOTE_CHECK %s" % ("DETERMINISTIC_PASS" if ok else "DETERMINISTIC_FAIL"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
