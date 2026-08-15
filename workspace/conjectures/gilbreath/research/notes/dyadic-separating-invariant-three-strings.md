# Measure the 2-adic separating invariant — three strings, one code path

Status: `checked` (exact integers, single code path, capture
`code/out/measure_separating_invariant.captured.txt`, EXIT 0).

```claim
id: dyadic-separating-invariant-three-strings
statement: The 2-adic separating invariant (measured as the true supply
  density nu2(n)/n from the actual right-diagonal dynamics) separates the
  three strings: Thue-Morse (h[j]=wt(j) mod 2) is rigid, nu2/n collapsing
  0.270->0.011 and exponent log nu2/log n decaying 0.72->0.46 over n=100..4000;
  odd-factor P=3 (h=[0,0,1] periodic) is non-rigid/linear, nu2/n holding at
  ~2/3 (0.660->0.667), exponent 0.91->0.95; the REAL prime right diagonal
  (ground truth, gaps incl. 6,10,...) sits with the non-rigid family at
  nu2/n ~ 0.49-0.50, exponent 0.82->0.92, nu2(primes)/nu2(P3) ~ 0.74 at
  n>=1000. The 2/4 reconstruction from the primes' mod-4 switch bits is a
  faithful shadow of the true prime diagonal (nu2 values within 0-3 at every
  sampled n), so the mod-4 switch bit string captures essentially all the
  supply content of the primes at these scales.
hypotheses: exact integer right-diagonal recurrence (lib.rightdiag), canonical
  cycle_and_nu2 = maximal {0,2} suffix of the right diagonal; 2-then-odds
  construction; n <= 4000, sieve 4e5 for the primes (~33860 primes).
holds-here: yes
status: checked
bearing: resolves Directive 66 item 2 as a measurement — the invariant
  genuinely separates the collapse class (Thue-Morse: rigid, density->0) from
  the linear families (P=3 and the real primes: positive density 2/3 and 1/2).
  For the primes this is numerical evidence to n<=4000, NOT a proof, and does
  NOT close G-supply (nu2 >= c*n stays named-open); it quantifies that the
  primes sit on the non-rigid side with positive density ~1/2, consistent with
  the two-point switch model.
anchor: code/out/measure_separating_invariant_THISRUN.captured.txt (executed this attempt, EXIT 0, code/dyadic/measure_separating_invariant.py + _final.py, independent double-route; reproduced the table exactly under the on-disk C1 convention h[j]->gap q_{j+2}->q_{j+3})
```

Directive 66 item 2, task `measure-2adic-separating-invariant-three-strings`.
The corrected open question: which finer invariant separates Thue–Morse
(nu2 = O(log n), sublinear) from the odd-factor families (nu2 ~ c·n, linear),
and where do the real primes sit on it. We measure the ground-truth shadow of
the named invariant (2-adic spectral non-rigidity, the mass of the halved-gap
bit string h in the non-nilpotent part of sigma = I+S) as the TRUE supply
density nu2(n)/n, computed by the actual right-diagonal dynamics
(`lib.rightdiag.incremental_diagonals` + `cycle_and_nu2`, canonical),
NOT the subset-zeta parity statistic (which mis-identifies nu2 —
thue-morse-subset-zeta-confirmed-identification-refuted).

One code path builds a 2-then-odds sequence from a bit string
(gap q_{j+2}->q_{j+3} = 2 if h[j]==1 else 4), then runs the same diagonal
recurrence. Four strings measured: Thue–Morse (h=wt(j) mod 2), odd-factor P=3
(h=[0,0,1] periodic), the REAL primes' actual right diagonal (ground truth,
gaps incl. 6,10,...), and the real primes' mod-4 switch bits re-fed through the
same 2/4 reconstruction.

## Result — density nu2(n)/n and exponent log nu2/log n

| n | TM nu2/n | P=3 nu2/n | TRUE primes nu2/n | 2/4-recon primes nu2/n |
|---|---|---|---|---|
| 100   | 0.270 | 0.660 | 0.430 | 0.430 |
| 200   | 0.145 | 0.660 | 0.490 | 0.495 |
| 500   | 0.078 | 0.664 | 0.498 | 0.502 |
| 1000  | 0.041 | 0.666 | 0.496 | 0.499 |
| 2000  | 0.022 | 0.666 | 0.497 | 0.498 |
| 4000  | 0.011 | 0.667 | 0.493 | 0.494 |

Exponent log nu2/log n at n=4000: TM 0.459 (decaying upward from 0.459? no —
decaying toward 0), P=3 0.951, TRUE primes 0.915.

## What separates

- **Thue–Morse is 2-adically RIGID:** nu2/n collapses 0.270 → 0.011 over
  n=100..4000, exponent decaying 0.72 → 0.46. Sublinear, the O(log n) witness.
  Confirms thue-morse-sublinear-supply-witness: aperiodicity does NOT force
  linear supply, and TM sits at the rigid (nilpotent) end of the invariant.
- **Odd-factor P=3 is NON-RIGID/linear:** nu2/n holds at ~2/3 (0.660 → 0.667),
  exponent 0.91 → 0.95. Matches the held dyadic-oddfactor-infimum-bounded
  (0.647@102, inf ~0.5) — regression passed (nu2(200)/200 = 0.660 in [0.4,0.8]).
- **Real primes sit with the LINEAR (non-rigid) family:** TRUE ground-truth
  density ~0.49–0.50, exponent 0.82 → 0.916, i.e. nu2(primes)/nu2(P3) ≈ 0.74
  at n≥1000. The primes are NOT at the rigid end nor near the TM end; they
  carry positive density ~1/2 exactly as the two-point switch model predicts.

## The 2/4 reconstruction is a faithful shadow of the true primes

TRUE prime diagonal vs 2/4-reconstructed-from-switch-bits at the same n:
(43,98,249,496,993,1973) vs (43,99,251,499,995,1975). Nearly identical —
real gaps > 4 (6,10,14,...) contribute negligibly to nu2(n) at these scales.
So the mod-4 switch bit string captures essentially all the supply content of
the primes, and the dyadic-2/4 model is a valid lens on the true dynamics.

## Bearing

This is the most informative measurement left on the dyadic route (Directive
66 item 2): the invariant genuinely separates — TM (rigid, density→0) vs
P=3 and the primes (non-rigid, positive density 2/3 and 1/2). For the primes
it is numerical evidence up to n≤4000 (sieve 4e5, ~33860 primes), NOT a proof;
it does NOT close G-supply. It says: the primes sit on the non-rigid side with
positive density ~1/2, so the supply bound nu2 ≥ c·n is quantitatively
supported at these scales by the same split that separates the collapse class.
