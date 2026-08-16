# Directive 21 — exact decrement-ratio arithmetic: which way the final ratio moves

## The bug it fixes
`code/out/ratio_b_extension_d21.txt` printed equations like
`r_3 = 0.021/0.024 = 0.899` and `r_4 = 0.019/0.021 = 0.878` whose operands
were the **3-decimal-rounded** decrements but whose quotients were computed
from the **unrounded** ones. Those printed equations are false:
`0.021/0.024 = 0.875` (not 0.899) and `0.019/0.021 = 0.905` (not 0.878).
Because the two readings lean opposite ways (the rounded-operand set
`0.63,0.75,0.875,0.905` rises monotonically toward 1; the exact set
`0.623,0.752,0.899,0.878` dips on the last step), the round-then-divide vs
exact-divide distinction is not cosmetic — it flips the direction of the
final step.

## Exact computation (all operands from the same full-precision s2_N)
`RatioB(N) = s2_N * 4N / ln N`, exact per the given s2_N values. Every ratio
below is the quotient of two ratios computed to full precision.

| k | d_k = RatioB[k] − RatioB[k+1] | r_k = d_{k+1}/d_k |
|---|-------------------------------|-------------------|
| 1 | 1000→4000 : 0.0507056445 | — |
| 2 | 4000→10000 : 0.0315724664 | r_1 = 0.622661771 |
| 3 | 10000→20000 : 0.0237280573 | r_2 = 0.751542721 |
| 4 | 20000→40000 : 0.0213411201 | r_3 = 0.899404441 |
| 5 | 40000→80000 : 0.0187328094 | **r_4 = 0.877780046** |

**r_4 = 0.877780046 < r_3 = 0.899404441 → the final exact ratio FALLS.**

(The two routes agree: the exact-float capture and an independent
50-digit-decimal recomputation both give r_4 = 0.877780046 vs r_3 = 0.899404441.)

## Why this decides nothing on its own
The direction of any "lean" depends on this single number r_4. Here r_4 falls
below r_3, and because the final ratio is sub-1 it modestly leans toward a
convergent geometric tail (Limit B above 1, extrapolation A) rather than
toward the divergent-tail limit-of-1 reading of the rounded monotone set.

But the evidence is thin: 6 data points cannot separate "limit exactly 1
approached from above" from "limit a constant above 1". The sign of one
decrement ratio — a quantity whose value depends on the s2 values to several
significant figures — is not a proof in either direction.

**Neither limit (Ratio B limit = 1, uniform; vs constant above 1) is
favoured or declared.** A discriminator needs several more doublings
(N = 160000, 320000, …), each ~4× the prior runtime.

The operator's screen approximations (0.63, 0.75, 0.875, 0.905) are **not**
data and are not quoted as such; the exact values above are the record.

- LABEL: measured, not proved.
- Verified: exact float route and independent 50-digit decimal route agree on
  all four ratios and on the FALL.

Files: `code/ratio_b/directive21_exact_ratios.py` (exact arithmetic, atomic
capture), `code/out/directive21_exact_ratios.captured.txt` (the capture).
