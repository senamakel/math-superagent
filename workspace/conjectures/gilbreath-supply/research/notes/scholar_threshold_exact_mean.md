# Exact mean of ν₂/n over the weight-w layer — the threshold's mean half

**Author:** scholar (third pass). **Status:** derived; exact computation handed
to tool_builder; this note is the statement and the derivation.

The pass's one question (`GOAL.md`): does the minimum weight ratio `w/n` at which
linear supply becomes *typical* tend to **0**, or plateau near **1/8**? The
measured column is `0.375, 0.300, 0.250, 0.286, 0.188, 0.156, 0.125, 0.125` for
`n = 8, 10, 12, 14, 16, 32, 64, 128`.

"Typical" is defined (directive 38/39, task `linear-supply-threshold-limit`) as
**two conditions**: mean `ν₂/n ≥ 0.40` AND fraction of weight-w strings with
`ν₂/n ≥ 0.40` is `≥ 0.5`. The first (mean) half admits an **exact closed form**
over the entire weight-w layer, with zero sampling.

## The parity identity (proved by hand, checked on n=3,4)

For a fixed depth `d`, the fold cell `T(n,d)` is the XOR of the
`k = 2^popcount(d)` positions in row `M_d`. Over **all** weight-`w` strings, count
those with an odd number of ones in `M_d` (the ones that make `T(n,d)=1`):

```
#odd = Σ_{r odd} C(k,r) C(n−k, w−r) = ( C(n,w) − c_w ) / 2
c_w = [z^w] (1−z)^k (1+z)^{n−k}
```

because `c_w = Σ_r (−1)^r C(k,r)C(n−k,w−r) = #even − #odd`, and `#even+#odd=C(n,w)`. Hence

```
P_d(w) := P( over weight-w strings, T(n,d)=1 )
        = ( C(n,w) − [z^w] (1−z)^{2^pc(d)} (1+z)^{n−2^pc(d)} ) / ( 2 C(n,w) )
```

and the exact mean over the weight-w layer is

```
mean_n(w) = (1/n) Σ_{d=2}^{n−1} P_d(w).        (floored d-range [2, n−1])
```

**Hand checks.** n=3, w=1, d=2 (k=2): `c_w=[z^1](1-z)^2(1+z)=-1`,
`P=(3−(−1))/6=2/3`; brute over {100,010,001}: T=h[0]⊕h[2]=1 for 2 of 3 ✓.
n=4, w=1: d=2 (k=2): c=0, P=1/2; d=3 (k=4): c=−4, P=1; mean=(1/4)(1/2+1)=0.375 ✓.

## Asymptotic reading (heuristic, to be confirmed by the exact computation)

For a depth with `k=2^pc(d)` and weight ratio `r=w/n`, the odd-probability is
`P_d ≈ (1 − e^{−2 r k})/2` (the k positions are ~independent Bernoulli(r) when
`k≪n` and the count concentrates otherwise). So `P_d ≈ 1/2` iff
`r·2^pc(d) ≫ 1`, i.e. `2^pc(d) ≫ 1/(2r)`. The mean is then `≈ (1/2)·F(1/(2r))`
where `F(K)` is the fraction of depths with `2^pc(d) ≥ K`. Since `popcount(d)`
over `d∈[0,2^m)`, `m=log₂n`, is `Bin(m,½)`, the condition `mean≥0.4` (i.e.
`F≥0.8`) needs `pc(d) ≥ −log₂r−1` for `≥80%` of depths. Normal approximation:
`−log₂r − 1 ≤ m/2 − 0.42√m`, so

```
r_min(mean)  ≳  n^{−1/2} · 2^{0.42√(log₂n) − 1}  →  0.
```

Predicted mean-threshold ratios: ~0.29@8, 0.22@16, 0.17@32, 0.13@64, 0.095@128,
0.067@256, …, declining like `n^{-1/2}`. **If this holds, the measured 0.125
plateau at n=64,128 was sampling resolution** (the 300/weight sampler only
visited w = 8, 16, 32 at n=128, so w=16/0.125 was the first sampled weight above
the true mean-crossing ~0.09) — the ratio tends to 0, and the "typical" demand is
satisfiable at any positive density, not a fixed constant.

## What still needs the sampled computation (frac half)

The fraction-`≥0.5` half is a *concentration* question: even if the mean crosses
0.4 at ratio `r(n)→0`, the distribution of `ν₂/n` over weight-w strings at that
ratio must put `≥½` of strings above 0.4. The pass's data shows the mean is the
binding constraint at n=8..128 (frac was already ≥0.5 at the mean-crossing w), but
that must be confirmed at larger n. This is where raising the 300/weight sample
count matters (the operator's directive). My exact mean removes the sampling
error from the *mean* half of the test entirely; the frac half is tool_builder's
sampled job.

## The computation confirmed the trend (third pass, exact)

tool_builder ran the exact closed form grouped by popcount to **n=4096**
(`code/scholar/threshold_limit_run.py`, capture
`code/out/threshold_limit_exact.txt`). The exact mean-threshold column:

```
n     8  10  12  14  16   32   64    128   256    512    1024    2048    4096
theta 0.375 0.300 0.250 0.286 0.188 0.156 0.109 0.086 0.0625 0.0469 0.0342 0.0254 0.0188
```

**Eventually decreasing across the listed range, no plateau.** The exact column
is *not* globally monotone — `0.2857`@14 rises above `0.2500`@12 — but from n=14
onward it declines monotonically and keeps falling through 0.125
(`0.109@64, 0.086@128`). The heuristic's
predictions were close (0.095@128 predicted vs 0.086 actual; 0.067@256 vs
0.0625), and the ratio keeps falling through 0.125. The pass-2 "0.125 held
twice at n=64,128" was a 300-sample + stricter (mean AND frac≥0.5) sampling
artifact; the exact mean gives 0.109@64 and 0.086@128. At every fixed
`alpha ∈ {0.05..0.15}` the exact mean rises toward 1/2 with `n`
(e.g. alpha=0.05: 0.375@8 → 0.4675@4096), i.e. at ANY fixed positive density
the mean eventually crosses 0.40.

**The frac half agrees.** Sampled with ≥2000 strings per weight at n=256,512
(PART B of the same script), the first weight with `frac(nu2/n≥0.40) ≥ 0.5`
sits near `w/n=0.05` at n=512 (matching the mean crossing), so the true
(mean AND frac) "typical" threshold tracks the mean threshold downward.

```claim
id: threshold-mean-exact-parity-formula
statement: Over all weight-w binary strings of length n, for a fixed depth d the fold cell T(n,d) (XOR of the k=2^popcount(d) positions in row M_d) is odd with probability P_d(w) = ( C(n,w) − [z^w](1−z)^k(1+z)^{n−k} ) / ( 2 C(n,w) ); hence the exact mean of nu2/n over the weight-w layer is mean_n(w) = (1/n) Σ_{d=2}^{n−1} P_d(w).
hypotheses: floored d-range [2,n−1]; the submask-XOR cell T(n,d) (problem.md facts 1–2); weight exactly w.
holds-here: yes (the formula is exact integer/Fraction arithmetic over C(n,w) and a coefficient; no approximation)
status: verified-numerically (identity proved by parity-counting; hand-checked n=3,4; exact grouped computation to n=4096 matches exhaustive s_sos on n=6..14 and the prior independent exhaustive capture)
bearing: Decides the MEAN half of the 'typical' test with zero sampling error. The exact mean-threshold ratio declines from n=14 onward 0.375@8 → 0.0188@4096 — no plateau. Directive 45 reframes what this buys: 'positive density suffices' is NOT weaker than switch density (it is that statement, so it wins nothing); the deliverable is the absolute threshold weight w*(n)=θ(n)·n ~ n^0.55, sublinear (fitted 0.546±0.011 over large-n rows) — 'about n^0.55 switches suffice' is strictly weaker than switch density. The limit itself is not proven (exact over the n-list, not an asymptotic theorem); and 'typical is not this string' — the genericity gap to the primes' own h — remains.
anchor: code/scholar/threshold_limit_run.py; code/out/threshold_limit_exact.txt
```
