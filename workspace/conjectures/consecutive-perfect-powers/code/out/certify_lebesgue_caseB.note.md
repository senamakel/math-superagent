# Case B certification: x^p - y^2 = 1, p odd prime — machine-certified

Runs `code/caseB/certify_lebesgue_caseB.py`; captured output
`code/out/certify_lebesgue_caseB.captured.txt`, EXIT 0.

## What it settles

Every step of the Lebesgue-style reduction of the exponent-2 "y-squared" case
of Catalan (`x^p - y^2 = 1`, p odd prime, x,y > 0) is machine-certified in
exact integer + symbolic sympy arithmetic (no floats):

- **Step 1 (parity):** y odd forces x^p = y^2+1 = 2 (mod 4), impossible for an
  odd p-th power; so y even and x odd. PASS.
- **Step 2 (Z[i] factorisation):** x^p = (y+i)(y-i) with gcd a unit for even y
  (1+i does not divide y+i); Z[i] a UFD, so y+i = u·(a+bi)^p. PASS (norm,
  gcd-unit, 1+i nondivisibility all checked on y in [0,2000)).
- **Step 3 (unit absorption):** for every unit u in {1,-1,i,-i} and every odd
  prime p, a unit w has w^p = u, so y+i = (c+di)^p. Checked symbolically and on
  concrete Gaussian integers for p in {3..59,17,19,23}. PASS.
- **Step 4:** 1 = Im(y+i) = d·(integer poly), so d = ±1. PASS.
- **Step 5:** c | y, and N gives x = c^2+1, with m^2 = T(c,p) =
  sum_{k=0}^{p-1}(c^2+1)^k = (x^p-1)/(x-1). PASS (Re-divisibility by c,
  N((c+di)^p) = (c^2+d^2)^p, geometric-sum and concrete T identities).
- **Step 6(a):** numerically T(c,p) is never a perfect square for c in
  [1,2000] and every odd prime p in [3,101] — 50000 pairs, 0 squares found.
  PASS.
- **Step 6(b):** the general statement is the classical Ljunggren-type theorem
  (x^n-1)/(x-1) = y^2 has only solutions (4,7,20) and (5,3,11). Here n = p an
  odd prime, only (5,3,11) could apply; its x=3 forces c^2+1=3, impossible.
  This is ASSERTED-CLASSICAL, NOT proved in-workspace. So the full theorem
  "x^p - y^2 = 1 (p odd prime) has no positive solution" is certified
  **CONDITIONALLY** on that classical lemma; the reduction is proved.

**Falsifier check:** the known solution (3,2,2,3) has p=2, q=3, so it is
correctly OUTSIDE Case B's hypothesis (q=2, p odd prime). The claim does not
over-eliminate: no solution with y-exponent 2 and p odd prime is asserted to
exist or not exist by this reduction — the certification closes the reduction,
not the whole conjecture.

## Status ledger

- Reduction steps 1-5: machine-certified (proved modulo the Z[i] UFD and
  unit-absorption which are classical, each structurally argued and
  numerically/symbolically checked here).
- Step 6(a) numeric box: verified-numerically, 0 squares over 50000 (c,p)
  pairs (c<=2000, p<=101).
- Step 6(b) key lemma: verified-numerically in the box + asserted by the
  classical Ljunggren-type theorem (not re-derived in-workspace). This is the
  honest boundary of the certification.
- The `(x^p-1)/(x-1) = sum x^k` symbolic FAIL seen in an earlier run was a
  sympy artifact: with symbolic p the summation returns a Piecewise whose
  x=1 branch is nan under simplify. The identity is true for every concrete p
  (confirmed separately) and is now checked as the polynomial identity
  (x-1)·sum = x^p - 1, which PASSES for all tested p.

## Claim

```claim
id: caseb-lebesgue-reduction-certified
statement: x^p - y^2 = 1 (p odd prime >= 3, x,y > 0) reduces to x = c^2+1 and
  m^2 = T(c,p) = (x^p-1)/(x-1) = sum_{k=0}^{p-1}(c^2+1)^k for integers c, m;
  and T(c,p) is not a square for c in [1,2000], odd prime p in [3,101].
hypotheses: p odd prime >= 3; x,y,c,m positive integers; Z[i] is a UFD.
holds-here: known solution (3,2,2,3) has q=3 (not 2), outside hypothesis —
  no over-elimination.
status: reduction machine-certified (steps 1-5 PASS); T(c,p) non-square
  verified-numerically in the box, general case asserted by the classical
  Ljunggren-type theorem (not re-derived here).
bearing: closes the reduction of GOAL's exponent-2 "y-squared" case; the lone
  open lemma (T(c,p) never a square) is classical, not re-derived.
anchor: code/out/certify_lebesgue_caseB.captured.txt (EXIT 0)
```
