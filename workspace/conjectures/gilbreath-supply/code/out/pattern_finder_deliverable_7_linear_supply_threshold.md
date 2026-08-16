# Pattern-finder deliverable — third pass: the linear-supply threshold tail

## The one owed computation, answered

The pass-two column `w/n` at which "linear supply becomes typical"
(`mean nu2/n >= 0.40` `AND frac(nu2/n>=0.40) >= 0.5`) was
`0.375, 0.300, 0.250, 0.286, 0.188, 0.156, 0.125, 0.125` for
`n = 8..128`, holding at 0.125 twice. The run was stopped before resolving
tends-to-0 vs plateaus-at-1/8.

I pushed it to n=8192 with a vectorized int8 submask-fold (verified equal to
`lib.supply_fold.s_sos` and `s_direct`; guard `nu2(53)==18, nu2(64)==27`
passed), sampling 2000–3000 weight-`w` strings per point with a **fresh
independent RNG per (n,w)** — the sequential-RNG contamination in the first
draft produced a spurious "none" at n=256, which the fresh-RNG rewrite fixed.

## The column (measurement, S=2000–3000)

```
   n   first_w   w/n
   8      3     0.3750   (exhaustive)
  10      3     0.3000   (exhaustive)
  12      3     0.2500   (exhaustive)
  14      4     0.2857   (exhaustive)
  16      3     0.1875   (exhaustive)
  32      5     0.1562
  64      8     0.1250
 128     16     0.1250
 256     17     0.0664
 512     25     0.0488
1024     38     0.0371
2048     55     0.0269
4096     87     0.0212
8192    127     0.0155
```

## Verdict the data supports (inference, not proof)

The **n=64/128 plateau at 1/8 is decisively broken**: the ratio keeps falling
through n=8192. Log-log slope of `w/n` vs `n` over the `n>=64` tail ≈ −0.46,
i.e. `w/n ~ n^{-0.46}`, equivalently `first_w ~ n^{0.54}` (sublinear in n).

The data therefore **supports "tends to 0," not "plateaus at 1/8"**: linear
supply becomes typical at any positive density in the measured range, so the
arithmetic input the primes need would (for this statistic) reduce to positive
density plus non-adversariality — materially weaker than pointwise mod-4
switch density.

## Honest limit

Monte Carlo, not a proof. Exponent −0.46 is a fit to a finite column, not an
established law; n ≤ 8192 cannot prove the limit is 0, nor rule out an
eventual plateau at positive `c`. What it **removes** is the concrete
pass-two hypothesis "plateaus at 1/8." The gap to an affirmative theorem:
prove `w/n -> 0` (or bound the decay).

## Sequence notes

`first_w = 3,3,3,4,3,5,8,16,17,25,38,55,87,127` (n=8..8192): **not in OEIS**
(no catalogued match), no constant-coefficient linear recurrence of order ≤ 6,
not a low-degree polynomial. This is expected — it is a statistical threshold
from Monte Carlo sampling, so a clean closed form is not the right target; the
structural fact is the monotone decay, i.e. `first_w ~ n^{0.54}` (`w/n ~ n^{-0.46}`).

## Controls

- All-ones string (max weight n) is a kernel vector, `nu2/n -> 0` for every n
  — the metric reads position structure, not weight.
- `h = e_{n-2}` is weight-1 yet `nu2 ~ n/2`: weight alone is not supply;
  typicality is a property of random strings of a given weight, which is what
  this column measures.
