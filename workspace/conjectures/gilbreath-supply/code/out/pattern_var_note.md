# pattern_var.py — first captured run

Settles: **the empirical variance of `ν₂(n)/n` over the primes decays to 0**,
so the averaged-form target (GOAL priority 1: `ν₂(n) ≥ c·n` on a density-1
set) is numerically supported. This is the first executed capture for a script
that existed on disk with no output beside it.

## What it computes

`ν₂(n)` is read two independent ways and the run cross-checks them at
`n ∈ {100, 500, 1000, 2000, 4000}` — from the stored endpoint sum `S(n)`
(`supply_endpoint_density.txt`) via `ν₂ = (n−2−S)/2`, and from the gap-parity
string `h` via the submask-product SOS transform (`lib.supply_fold.s_sos`).
**Every cross-check agreed exactly (diff = 0).** Then

```
σ²_N = (1/N) Σ_{n≤N} (ν₂(n)/n − μ_N)² ,   μ_N = mean of ν₂(n)/n .
```

## Result (exact integer arithmetic; only ratios float)

| N | mean μ_N | σ²_N | σ_N | min_tail |
| --- | --- | --- | --- | --- |
| 100 | 0.4439 | 1.64e-02 | 0.1282 | 0.0000 |
| 500 | 0.4842 | 4.54e-03 | 0.0674 | 0.0000 |
| 1000 | 0.4911 | 2.49e-03 | 0.0499 | 0.0000 |
| 2000 | 0.4954 | 1.34e-03 | 0.0367 | 0.0000 |
| 4000 | 0.4973 | 7.21e-04 | 0.0269 | 0.0000 |

Tail-only σ² over the last half (removes the small-n bias):

| N | window | σ² |
| --- | --- | --- |
| 500 | [250,500) | 7.78e-04 |
| 1000 | [500,1000) | 3.44e-04 |
| 2000 | [1000,2000) | 1.62e-04 |
| 4000 | [2000,4000) | 9.11e-05 |

- The mean μ_N is **rising toward ≈ 0.497** and the variance σ²_N is **decaying**
  (`1.64e-02 → 7.21e-04` full; tail-only `7.78e-04 → 9.11e-05`, about `1/N`).
- `min_tail = 0.0000` everywhere is the known pointwise dip (`ν₂` is 0 at tiny
  `n`, and `ν₂/n` dips at `n≈53`); it is not a failure of the averaged form.

## Claim

```md
id: g-var-empirical-vanishing
statement: Over n ≤ 4000 the primes' ν₂(n)/n has mean μ_N → 0.497 and variance
  σ²_N decaying to 0 (tail-only ~ 9.1e-05 at N=4000, ~ 1/N), consistent with
  ν₂(n)/n having a limit and averaged SUPPLY holding on a density-1 set.
hypotheses: ν₂ computed exactly by two independent routes (endpoint-sum and
  gap-parity SOS), agreeing at 5 sample n; primes only; n ≤ 4000.
holds-here: true at n ≤ 4000 (measured); not a proof of any infinite statement.
status: checked (numeric, n ≤ 4000)
bearing: supports the averaged-form attack (goal priority 1); the variance
  decay is the mechanism the pointwise parity barrier is blind to.
anchor: code/out/pattern_var_captured.txt
```

## Status

Measured, not proved. The positive control (SOS ⇌ endpoint-sum agreement) passed
at all 5 cross-check points; there is no negative control in this particular
script (it is a measurement, not a theorem check). The capture is in
`code/out/pattern_var_captured.txt`.
