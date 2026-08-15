# Re-capture note: reduction_audit.py wording (Directive 51)

The capture `code/out/reduction_audit.captured.txt` still holds the defective
VERDICT line ("MACHINE-CONFIRMED as a theorem on real rows") and the
"a theorem by construction" line — both the Directive 42/44/51 category
error (a 281-column / 45150-cell check is not a theorem).

Review of the CURRENT source `code/gap_analysis/reduction_audit.py`:
it no longer prints any "theorem", "proved", "proves", or "VERDICT" wording.
Its output is (A) cross-check, (B) model-match, (C) fixedness, (D) the
constant-1 erosion law (REPORTED not asserted, correct), and an aggregate
"ALL AUDIT CHECKS PASSED" / "AUDIT RESULT: ... REFUTED here" line that carries
the count over the stated range. The captured file is therefore STALE — it
came from an older version of the program.

Per the do-not-overwrite rule, re-capture to a NEW file
`code/out/reduction_audit.captured2.txt` rather than clobbering the record of
the defective line.

## Directive 51 final (this session)

The current source now ends with a final factual VERDICT line plus an
aggregate TOTALS line and a (D)-distinction line, and it was re-captured to a
NEW file `code/out/reduction_audit.recapture2.txt` (EXIT_CODE=0). The VERDICT
reads: "the passage from real right-diagonal column dynamics to the
(pattern,v) descent model is CONFIRMED over the cross-check and 10001 real
columns with 0 violations; the pattern eps is read off the previous diagonal
delta(q_{n-1}), so it is prefix-determined (check C) and does not depend on
the trajectory's own value." It uses only CONFIRMED/REFUTED over the stated
range — no theorem/proved/proves in the captured output (grep confirms NONE).
The (D)-distinction line keeps the refuted diagonal-coordinate constant-1 law
separate from the CONFIRMED row-direction block lemma b_{k+1} >= b_k - 1 (0
violations). `reduction_audit.captured.txt` (defective) and
`reduction_audit.captured2.txt` (prior corrected) are both untouched.
