# Bautin focal-value clearing denominators — provisional structure

## Data (exact, from code/out/focal_denoms.captured.txt)

D_d = gcd-clearing denominator of L_d (5-param chart family), d = 4..14:

    d    D_d                    v2   v3   v5   v7
    4            8                3    0    0    0
    6          192                6    1    0    0
    8        18432               11    2    0    0
   10      1105920               13    3    1    0
   12  22295347200               19    5    2    1
   14 37456183296000             23    6    3    2

Factorizations (this pass, exact):
    8   = 2^3
    192 = 2^6 * 3
    18432 = 2^11 * 3^2
    1105920 = 2^13 * 3^3 * 5
    22295347200 = 2^19 * 3^5 * 5^2 * 7
    37456183296000 = 2^23 * 3^6 * 5^3 * 7^2

## Provisional observations (6 computed terms only — NOT laws)

- v3 = d/2 - 2 for d = 4,6,8,10; then v3(12)=5, v3(14)=6 (i.e. +1 above d/2-2).
- v5 = d/2 - 4 for d = 8,10,12,14 (v5=0 for d=4,6 trivially).
- v7 = d/2 - 5 for d >= 12.
- v2 is IRREGULAR: residuals from ceil(3d/2): -3,-3,-1,-2,1,2 — no simple
  affine law over the 6 terms. The 2-adic valuation is where any clean
  structure breaks.

Ratios D_{d+2}/D_d: 24, 96, 60, 20160, 1680 — no simple pattern.

## What would test these

The pending d18 run (delegated) was steered to report D_16 and D_18 with their
(v2,v3,v5,v7). The threshold-affine laws predict, IF the observed shifts
continue: v3(16)=? (needs the continuation of the +1 step), v5(16)=4, v7(16)=3
— but with the v2 irregularity no clean prediction for D_16/D_18 should be
trusted before the exact computation. Do NOT record any of this as a finding
until d=16,18 rows are computed.