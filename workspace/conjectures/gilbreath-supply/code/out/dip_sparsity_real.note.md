# Real dip sparsity at the N=40000 ceiling after de-vacuousing the oracle

The tool_builder's `dip_sparsity_monotonic.py` computed nu2 by the UNFLOORED
literal suffix (identically 0), so `code/out/dip_sparsity_monotonic.txt` was a
vacuous capture (density 1.000 at every threshold, min nu2/n = 0). Per
directive 11 this run: rewrote the script to the canonical floored oracle
(lib.supply_fold.s_sos/s_direct, d∈[2,n−1]), added top-of-file assertions
nu2(53)==18 and |mu_4000 − 0.4977| ≤ 0.01 so a zeroed oracle aborts, fixed the
float trap (n=145 is exactly 0.4, must not be counted < 0.40 — uses exact
Fraction(hundredths,100)), DELETED the vacuous file, and re-ran at N=40000.

## Real dip density {n : nu2(n)/n < c} at N=40000 (prime h), measured

| c | full [50,N] | half [N/2,N] | tail [0.9N,N] |
|---|---|---|---|
| 0.40 | 0.000075 | 0.000000 | 0 |
| 0.43 | 0.000375 | 0.000000 | 0 |
| 0.45 | 0.001277 | 0.000000 | 0 |
| 0.47 | 0.003880 | 0.000000 | 0 |
| 0.48 | 0.008861 | 0.000000 | 0 |
| 0.49 | 0.033917 | 0.000500 | 0 |

Window minima nu2/n: full 0.339623, half 0.487947, tail 0.490344 (tail argmin
n=36972, verified independently from scratch; matches capture).

**The tail window [0.9N,N] has ZERO dips at every c in 0.40..0.49.** At the
40000 ceiling sparsity does NOT break in the tail through 0.49 (the refuter's
c=0.48 breaking was full-range density at N=3000, dominated by small-n dips
n≤274).

Negative controls (both fail, so the prime bound is discriminating):
ALL-ONES nu2/n≡0, tail dip density 1.0 at every c (vacuous); THUE-MORSE tail
nu2/n ~ 0.003, tail dip density 1.0 at every c (fails sparsity).

```claim
id: dip-sparsity-tail-clean-through-0.49-at-40000
statement: At the N=40000 ceiling (fixed floored oracle, asserts
  nu2(53)==18 and mu_4000 within 0.01 of 0.4977), the tail window [0.9N,N] of
  {n : nu2(n)/n < c} is EMPTY for every c in 0.40..0.49. The full-window
  density {n:nu2/n<c} rises 0.000075(c=0.40) -> 0.0339(c=0.49); the half-window
  [N/2,N] has one dip (density 0.0005) at c=0.49 and none below. Tail min
  nu2/n = 0.49034 (argmin n=36972). So sparsity does NOT break in the tail
  through c=0.49 at N=40000. Negative controls ALL-ONES (tail density 1.0,
  vacuous) and THUE-MORSE (tail density 1.0, fails) discriminate. This
  replaces/strengthens the earlier c=0.48 breaking reported from full-range
  N=3000, which was dominated by small-n dips.
hypotheses: fold convention d∈[2,n−1]; canonical s_sos oracle, exact Fraction
  comparisons (n=145 exactly 0.4 not counted); N=40000; measured.
holds-here: yes, measured at N=40000 (tail) and N=4000..40000 (windows).
status: measured-not-proved
bearing: measured density-1 shape for GOAL priority 1 is far stronger than the
  earlier c=0.40 pin: the tail (last 10%) is clean of dips through 0.49. Any
  counterexample would have to be at very large n with nu2/n < 0.49.
anchor: code/out/dip_sparsity_monotonic.txt (regenerated, floored);
  code/averaged/dip_sparsity_monotonic.py (fixed)
```
