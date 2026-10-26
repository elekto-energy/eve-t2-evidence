#!/usr/bin/env python3
"""VERIFY_PACKAGE.py - integrity check of this distribution package. Python 3 standard library only.

Run from anywhere:  python3 VERIFY_PACKAGE.py
Three kinds of file are kept apart:
  ORIGINAL       evidence/<path>: unchanged copy of a frozen file; must equal the sha256 + bytes of its line in
                 original/LGX_C2_T2_EVIDENCE_FREEZE_2026-10-24.md                      -> MATCH / MISMATCH / MISSING
  WITHHELD       listed in the original manifest but not distributed; must NOT be present -> NOT_IN_PACKAGE (<status>)
  READING COPY   reading_copies/*: derived, redacted, NOT evidence; checked only against its OWN sha256 in
                 PUBLICATION_MANIFEST.json, never against the original                  -> READING_COPY_OWN_HASH_OK / _BAD
Every other file in the package must be listed in PUBLICATION_MANIFEST.json            -> UNLISTED_FILE otherwise
Exit 0 only if every check passes.
Limits: proves file identity against the manifest text; it does not prove that the manifest is authentic, who
produced it, or that any statement inside a file is true.
"""
import hashlib, json, os, re, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
PUB = json.load(open(os.path.join(ROOT, "PUBLICATION_MANIFEST.json"), encoding="ascii"))
MAN = os.path.join(ROOT, *PUB["original_manifest"]["path"].split("/"))
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(65536), b""): h.update(b)
    return h.hexdigest()
bad = 0; counts = {}
def out(st, what):
    global bad
    counts[st] = counts.get(st, 0) + 1
    if st in ("MISMATCH", "MISSING", "UNEXPECTED_PRESENT", "UNLISTED_ORIGINAL", "READING_COPY_OWN_HASH_BAD",
              "READING_COPY_MISSING", "SUPPORT_FILE_BAD", "UNLISTED_FILE", "ORIGINAL_MANIFEST_BAD"):
        bad += 1
    print(st.ljust(34), what)
om = PUB["original_manifest"]
out("ORIGINAL_MANIFEST_OK" if sha(MAN) == om["sha256"] and os.path.getsize(MAN) == om["bytes"] else "ORIGINAL_MANIFEST_BAD",
    om["path"] + " " + sha(MAN))
status = {e["original_path"]: e for e in PUB["files"]}
listed = {om["path"]}
for line in open(MAN, encoding="utf-8"):
    m = re.match(r"^([0-9a-f]{64})\s+(\d+)\s+(\S.*)$", line.rstrip("\n"))
    if not m: continue
    want, size, rel = m.group(1), int(m.group(2)), m.group(3)
    e = status.get(rel)
    if e is None: out("UNLISTED_ORIGINAL", rel); continue
    p = os.path.join(ROOT, "evidence", *rel.split("\\"))
    if e["package_status"] == "ORIGINAL_UNCHANGED":
        listed.add(e["package_path"])
        if not os.path.isfile(p): out("MISSING", rel)
        else: out("MATCH" if sha(p) == want and os.path.getsize(p) == size else "MISMATCH", rel)
    else:
        out("UNEXPECTED_PRESENT" if os.path.exists(p) else "NOT_IN_PACKAGE (" + e["package_status"] + ")", rel)
for r in PUB["reading_copies"]:
    listed.add(r["path"]); p = os.path.join(ROOT, *r["path"].split("/"))
    if not os.path.isfile(p): out("READING_COPY_MISSING", r["path"]); continue
    first = open(p, "rb").readline()
    ok = sha(p) == r["own_sha256"] and first.startswith(b"READING COPY - NOT EVIDENCE")
    out("READING_COPY_OWN_HASH_OK" if ok else "READING_COPY_OWN_HASH_BAD",
        r["path"] + " (NOT evidence; derived from " + r["derived_from"] + ", not comparable with its sha256)")
for s in PUB["support_files"]:
    listed.add(s["path"]); p = os.path.join(ROOT, *s["path"].split("/"))
    out("SUPPORT_FILE_OK" if os.path.isfile(p) and sha(p) == s["sha256"] else "SUPPORT_FILE_BAD", s["path"])
listed.add("PUBLICATION_MANIFEST.json")
for d, _, fs in os.walk(ROOT):
    for f in fs:
        rel = os.path.relpath(os.path.join(d, f), ROOT).replace(os.sep, "/")
        if rel not in listed: out("UNLISTED_FILE", rel)
print("summary", json.dumps(counts, sort_keys=True))
print("RESULT", "PACKAGE_INTEGRITY_OK" if bad == 0 else "PACKAGE_INTEGRITY_FAIL")
sys.exit(1 if bad else 0)
