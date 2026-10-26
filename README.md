# EVE Verified - T2 governed agent handoff - public evidence view

Static site. No build step. Serve the folder as is.

- index.html - the evidence view
- T2_EVIDENCE_PACKAGE_2026-10-25_final.zip - the full package (46 files), byte-identical to package/
- package/public_evidence_T2_2026-10-25_final/ - the package unpacked; originals byte-identical to the frozen manifest
- SHA256SUMS.txt - SHA-256 of every file in this site except itself

Check: `python3 package/public_evidence_T2_2026-10-25_final/VERIFY_PACKAGE.py` -> `RESULT PACKAGE_INTEGRITY_OK`
and `sha256sum -c SHA256SUMS.txt`.
