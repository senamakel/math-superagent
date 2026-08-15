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
the defective line. No source edit was needed: the wording rule already lives
in the code; the fix is that the on-disk capture match the source.
