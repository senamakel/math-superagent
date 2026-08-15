# Elementary ladder rungs settled (R-trivial-bases, R-p-eq-q) and R-fixed-23 verified

Output: `code/out/elementary_rungs.captured.txt` (run of `code/elementary/elementary_rungs.py`,
EXIT 0). All arithmetic exact integer; no floats.

## R-trivial-bases — SETTLED (proved, one-line)

**Statement.** No solution of `x^p - y^q = 1` with x,y>0, p,q>1 has x = 1 or y = 1.

**Proof.** If x = 1 then `1 - y^q = 1`, so `y^q = 0`, `y = 0`, excluded by y > 0.
If y = 1 then `x^p - 1 = 1`, so `x^p = 2`, impossible for integers x>=1, p>=2
(2 has no perfect-power representation) and p=1 is excluded by p > 1.

**Independent check.** The exact oracle `solutions(10^8)` returns exactly
`[(3,2,2,3)]`, whose bases are both >= 2; no output value has a base of 1. (The
oracle itself only iterates bases >= 2, so this is a consistency check, not an
independent proof — the proof above is the argument.)

```claim
id: r-trivial-bases
statement: No solution of x^p - y^q = 1 with x,y>0 and p,q>1 has x = 1 or y = 1.
hypotheses: x,y > 0; p,q > 1; x^p - y^q = 1.
holds-here: yes — the known solution (3,2,2,3) has both bases >= 2, so it is not eliminated.
status: checked (proved by two-line case split; consistency-checked against the exact oracle)
bearing: closes the weakest open rung of the Catalan ladder; all solutions have x,y >= 2.
anchor: code/out/elementary_rungs.captured.txt
```

## R-p-eq-q — SETTLED (proved)

**Statement.** For every odd prime p, `x^p - y^p = 1` has no solution in x,y > 0.

**Proof.** `x^p - y^p = (x-y)(x^{p-1} + x^{p-2}y + ... + y^{p-1})`. Since the
left is 1 and both factors are positive integers, both equal 1. But
`x^{p-1}+...+y^{p-1}` (p terms) is >= p >= 3 for x,y >= 1 (and equals p when
x = y = 1, which is excluded anyway since x>y). Contradiction.

**Independent check.** Exact brute force over odd primes p in {3,5,7,11,13,17,19}
and x < 3000, y < x: zero hits. (Brute force is not the proof — the factorisation
above is — but it is an independent confirmation on the tested box.)

```claim
id: r-p-eq-q
statement: For every odd prime p, x^p - y^p = 1 has no solution in integers x,y > 0.
hypotheses: p odd prime; x,y > 0; x^p - y^p = 1.
holds-here: yes — the known solution (3,2,2,3) has p=2 != 3=q, so it sits outside this rung's symmetric case and is not claimed away.
status: checked (proved by factorisation; brute-force-confirmed over primes<=19, x<3000)
bearing: the symmetric odd-prime case is closed in Z by elementary factorisation.
anchor: code/out/elementary_rungs.captured.txt
```

## R-fixed-23 — PROVED in this workspace; numeric verification retained as cross-check

**Statement.** `x^2 - y^3 = 1` has `(x,y) = (3,2)` as its only solution in
x,y > 0 (with y > 0).

**Proof (this workspace).** The full statement is proved by an explicit descent
plus a complete Thue resolution: `y^3 = (x-1)(x+1)`, gcd(x-1,x+1) | 2; x even
impossible (min cube gap 7 > 2); x = 2k+1 odd forces {k,k+1} = {c^3, 2d^3},
reducing to the two Thue equations `c^3 - 2d^3 = +-1`, resolved completely by
PARI's proven `thue()` (code/refute/thue_descent_full.py, code/refute/thue_nf.gp;
output code/out/thue_descent_full.captured.txt, thue_gp.captured.txt). Final
filtering x,y > 0 selects exactly (x,y) = (3,2). This is the claim
`exp2-fixed23-proved-thue` (status: proved) recorded in the ladder's R-fixed-23
merge and in code/out/thue_descend_fixed23.note.md.

**Independent numeric cross-check of the proof.** The brute force below serves
as a numeric cross-check of that proof, not as the proof itself. Exact brute
force over `1 <= x <= 10^7`
(integer cube-root binary search, exact arithmetic): the only solutions of
`x^2 - y^3 = 1` are `(x,y) = (1,0)` and `(3,2)`. With the hypothesis y > 0, the
only solution is `(3,2)`. This is a numeric verification to a stated bound, a
fact about x <= 10^7, consistent with (and confirming) the proved statement.

```claim
id: r-fixed-23-verified-numerically
statement: Over 1 <= x <= 10^7 the only solution of x^2 - y^3 = 1 with y > 0 is (x,y) = (3,2).
hypotheses: 1 <= x <= 10^7; y > 0; x^2 - y^3 = 1.
holds-here: yes (numerical verification of a sub-range of the full statement).
status: checked (numerically to x = 10^7; a cross-check of the proved full statement, claim exp2-fixed23-proved-thue)
bearing: calibration for the exponent-2 case R-exp2; confirms the known solution is the small one.
anchor: code/out/elementary_rungs.captured.txt
```

## Rungs status after this run

- `R-trivial-bases`: open -> **settled** (proved).
- `R-p-eq-q`: open -> **settled** (proved).
- `R-fixed-23`: open -> **proved** (descent + complete PARI thue(), claim
  exp2-fixed23-proved-thue); numeric verification to x = 10^7 retained as
  independent cross-check.
