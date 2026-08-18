# Second independent validation of the Lean L8∉⟨L4,L6⟩ tables

**Status: verified-computationally (executed capture, exact integer arithmetic).**

`code/bautin/verify_lean_tables.py` is a SECOND route to the statement
"L8 not in ⟨L4,L6⟩". Unlike `cofactor_certificate.py` / `lyapunov_quadratic.py`,
it does NOT re-run the sympy focal-value recurrence. It validates the emitted
data tables themselves — the exact text the Lean kernel elaborates in
`code/lean/Lib/Bautin.lean`.

## What it does
A small stdlib-only parser (no sympy) reads the file text of Bautin.lean and
extracts:
- `V1num`: the six explicit terms `C (c : ℚ) * X i * X j`
- `v2coeffs` / `v2ms`: 56 integer coefficients + 56 exponent vectors
- `v3coeffs` / `v3ms`: 220 integer coefficients + 220 exponent vectors
- `certPt` = `[-2, -2, 1, -1, -1, 1]`

It reconstructs V1num, V2num, V3num as exact integer polynomials over the six
coefficient variables (a1,a2,a3,b1,b2,b3), evaluates each at certPt, and
asserts:
- monomial counts 6 / 56 / 220
- eval V1num = 0, eval V2num = 0, eval V3num = 7200

## Result (PASS)
- eval V1num = 0 (must be 0)
- eval V2num = 0 (must be 0)
- eval V3num = 7200 (must be 7200)
- all table-shape, distinctness, and monomial-count checks PASS
- CERTIFICATE VALID: PASS, exit 0
- capture: `code/out/lean_tables.captured.txt`

## Independent structural audit (second route to correctness)
- V1num monomial degrees = {2}, V2num = {4}, V3num = {6} — matches the
  homogeneity of L4 / L6 / L8 (degree-2, -4, -6 focal values), so the parse
  cannot have misassigned a table.
- all exponent vectors within each table distinct; no zero coefficients
  (a zero entry would be a silent table corruption).
- Hand spot-check: V1num = 8·L4 agrees with the capture's L4 formula; and
  V3num value 7200 at certPt ↔ L8 = 25/64 (since 7200/18432 = 25/64), matching
  cofactor_certificate.captured.txt.

## Tamper test (attacking the method)
A copy of Bautin.lean with one v3 coefficient changed (89450→89449) is caught:
eval V3num = 7232 ≠ 7200, CERTIFICATE VALID: FAIL, exit 1. So the checker is
not vacuous — it genuinely detects corrupted emitted tables.

## Bearing
These are exactly the three evaluations the Lean kernel uses as the premises
of `theorem V3_not_mem_span_V1_V2` in Bautin.lean (the proof that Bautin's
generating set genuinely needs three generators). It never claims M(2)=3,
which stays Cited (Bautin 1952). Task: `cofactor-certificate-L8-not-in-L4-L6`.
