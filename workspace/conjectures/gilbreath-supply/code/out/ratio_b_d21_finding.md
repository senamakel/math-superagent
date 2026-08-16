# Ratio B decrement-ratio discriminator — directive 21 correction and honest reading

## What directive 21 asked
Whether the primes' Ratio B = s2_N·4N/lnN (for a_n = nu2(n)/n) converges to 1
(asymptotically indistinguishable from uniform) or to a constant above 1.
It is NOT discriminated by whether decrements shrink — that is consistent with
both limits — but by the RATIO r_k = d_{k+1}/d_k of consecutive per-doubling
decrements. If r settles <1 the remaining tail is a convergent geometric series
(limit > 1); if r drifts to 1 the tail diverges and Ratio B reaches 1.

## Measured data (exact s2, exact Fractions; LABEL: measured, not proved)
| N     | RatioB | decrement (per ~2x) |
|-------|--------|---------------------|
| 1000  | 1.443  | —                   |
| 4000  | 1.392  | 0.0507              |
| 10000 | 1.361  | 0.0316              |
| 20000 | 1.337  | 0.0237              |
| 40000 | 1.315  | 0.0213              |
| 80000 | 1.297  | 0.0187              |

## The two ratio methodologies — and the correction
- **Simple division of rounded 3-decimal decrements**
  (0.051,0.032,0.024,0.021,0.019): r = 0.63, 0.75, 0.875, **0.905** —
  monotone rising toward 1. This is the set directive 21 cited.
- **Exact decrement ratios** (from exact s2-derived decrements):
  r = 0.623, 0.752, 0.899, **0.878** — the last ratio DIPS below 0.9, so the
  exact sequence is NOT monotone.

The two sets genuinely diverge on the last step: 0.019/0.021 = 0.905 (rounded
decrements) vs exact d5/d4 = 0.0187/0.0213 = **0.878**.

## Honest reading
The directive's lean toward limit 1 ("rising toward 1 -> divergent tail")
holds for the rounded set but NOT for the exact set, where the final ratio
dips. The exact data therefore does not cleanly lean either way; if anything
the sub-1 last ratio (0.878) modestly leans toward a convergent geometric
tail, i.e. limit > 1 (Extrapolation A: tail = 0.019·0.9/(1−0.9) ≈ 0.171 →
Ratio B limit ≈ 1.297 − 0.171 ≈ 1.13).

**Neither limit is declared.** 6 data points cannot separate "limit exactly 1
approached from above" from "limit > 1"; discriminating them needs the next
doublings (N=160000, 320000, ...), each ~4x the prior runtime. The sharpest
open question in the run stands: whether the primes are asymptotically
indistinguishable from uniform for this second-moment statistic.

Verified: fresh exact recomputation (`code/ratio_b/exact_ratio_b_ratios.py`)
reproduces both sets; the arithmetic 0.019/0.021=0.905 and exact 0.878 are
both checked by hand. Negative-control honesty: no failing control here — the
discriminator is a trend statistic, and the limitation (only 6 points, one
failing the monotone lean) is stated rather than hidden.

Files: `code/ratio_b/measure_ratio_b.py` (trend logic corrected to
decrement-ratio, both extrapolations, no declaration), 
`code/out/ratio_b_extension_d21.txt` (new capture), 
`code/ratio_b/exact_ratio_b_ratios.py` (exact recomputation).
