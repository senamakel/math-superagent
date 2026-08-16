# Scholar — third pass: the mean half of the threshold is exactly solvable (and predicts tends-to-0)

For the pass's one computation (does the linear-supply weight threshold tend to 0
or plateau near 1/8), the **mean** half of the "typical" test can be computed
exactly, with zero sampling error, over the whole weight-w layer — decided the
mean half analytically rather than by the sampled method.

## The identity (proved by parity-counting)

For a fixed depth `d`, the fold cell `T(n,d)` is the XOR of the
`k = 2^popcount(d)` positions in row `M_d`. Over all weight-w strings, the
probability that the cell is odd is

```
P_d(w) = ( C(n,w) − [z^w](1−z)^k(1+z)^{n−k} ) / ( 2 C(n,w) )
```

(the alternating sum `c_w = [z^w](1−z)^k(1+z)^{n−k} = #even − #odd`). Hence the
exact mean of `ν₂/n` over the weight-w layer is `mean_n(w) = (1/n) Σ_{d=2}^{n−1} P_d(w)`.
Hand-checked at n=3,4; exact integer/Fraction, arbitrary n.

## What it predicts (heuristic, to be confirmed by the exact computation)

For weight ratio `r = w/n`, a depth with `k = 2^pc(d)` is odd with prob
`≈ (1 − e^{−2rk})/2`, so `≈1/2` when `2^pc(d) ≫ 1/(2r)`. Since
`popcount(d) ~ Bin(log₂n, ½)`, `mean ≥ 0.4` (i.e. ≥80% of depths odd-capable)
needs `pc ≥ −log₂r − 1` for ~80% of depths, giving

```
r_min(mean)  ≳  n^{−1/2} · 2^{0.42√(log₂n) − 1}  →  0
```

Predicted ratios: ~0.29@8, 0.22@16, 0.17@32, 0.13@64, 0.095@128, 0.067@256.
**If confirmed, the measured 0.125 plateau at n=64,128 was sampling resolution** —
the 300/weight sampler only visited w=8,16,32 at n=128, so w=16/0.125 was the
first sampled weight above the true mean-crossing ~0.09, and the column is still
falling toward 0, not levelling at a constant. That would mean the mean demand is
satisfiable at any positive density — a first affirmative weakening in this
workspace.

## Caveat, stated plainly

This resolves the **mean** half only. "Typical" also needs the **frac** half
(fraction of weight-w strings with `ν₂/n ≥ 0.4` is `≥ 0.5`), which is a
concentration question and is exactly where the operator's raise-the-sample-count
directive bites. The pass data shows the mean is the binding constraint at
n=8..128 (frac was already ≥0.5 at the mean-crossing w), but that must be
confirmed at larger n.

## Handoff

Exact computation `code/scholar/threshold_exact_mean.py` handed to tool_builder:
cross-check the closed-form mean vs brute `s_sos` on (n,w)∈{(6,1),(6,2),(8,1),
(8,3),(10,2),(12,3)}, then print exact first-w/n-with-mean≥0.40 for
n=8..2048. Capture `code/out/scholar_threshold_exact_mean.captured.txt`.
Claim block `threshold-mean-exact-parity-formula` filed in CLAIMS.md.
