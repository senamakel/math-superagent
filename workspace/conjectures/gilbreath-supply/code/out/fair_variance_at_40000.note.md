# Ratio B (prefix-variance null) across N: excess persists, limit undetermined

Directive-18/19 result. The operator confirmed `code/out/fair_variance_at_40000.txt`
is correct and a real result (data path fixed: `ν₂(40000)=20081 ≈ 0.5020` is the
primes, not a control), then directive 19 corrected the over-claim I (and the
earlier note) had made about where Ratio B is going. This note is the corrected,
honest statement.

## The null model (one line of algebra — established, not fitted)

Per-index fair-model variance of `ν₂(n)/n` is `Var(ν₂(n)/n) = (n−2)/(4n²) ≈ 1/(4n)`
(from `wt(Φ_n h) ~ Binomial(n−2, 1/2)`, claim `fair-model-exact-binomial`, PROVED).
The PREFIX empirical variance `s2_N` of the sequence `{ν₂(n)/n : n=2..N}` is the
average of the per-index variances:

    E[s2_N] = (1/N) Σ_{n=2..N} 1/(4n) ≈ log(N)/(4N),

NOT `1/(4N)`. Ratio A = `s2_N·4N` therefore tests the wrong (constant) null and
grows ~ log N. Ratio B = `s2_N·4N/log N` is the correct null-corrected statistic;
it is ~1 when the primes track the fair model.

- The NAIVE constant null `1/(4N)` fails badly (Ratio A = 13.94 at N=40000 vs 1).
- The `log(N)/(4N)` null is the right one (Ratio B ≈ 1.3).

## Ratio B across N with per-doubling decrements (directive 19 table)

From `code/out/fair_variance_at_40000.txt` (exact Fractions, floored oracle
nu2(53)=18, nu2(64)=27). The decrement between consecutive rows, normalised per
doubling of N, is what decides whether the limit is 1 or a constant above it:

| N     | s2_N      | Ratio B = s2_N·4N/log N | per-doubling decrement |
|-------|-----------|--------------------------|------------------------|
| 1000  | 2.4916e-3 | 1.4428                   | —      |
| 4000  | 7.2163e-4 | 1.3921                   | −0.0507 |
| 10000 | 3.1327e-4 | 1.3605                   | —      |
| 20000 | 1.6549e-4 | 1.3368                   | −0.0237 |
| 40000 | 8.7121e-5 | 1.3155                   | −0.0213 |

The strictly-equally-spaced doublings are 1000→4000 (−0.0507) and
20000→40000 (−0.0213). Directive 19's arithmetic: between the last two doublings
the decrement barely shrank, from 0.0237 to 0.0213 (ratio ≈ 0.90). If the
per-doubling decrement continued to decay geometrically at 0.9, the limiting
Ratio B would be about 1.13; if it decays much more slowly the sum diverges and
Ratio B reaches 1. **Four points over one decade cannot separate those two
hypotheses.**

## What is actually established (honest statement)

- The excess **PERSISTS** across N = 1000 to 40000: Ratio B falls 1.443 → 1.316,
  a ~32% excess at N=40000 over the `log(N)/(4N)` uniform null.
- The decrements decay SLOWLY and are still ~90% of their predecessor at the
  last step — the measured range does NOT determine whether the limit is 1
  (primes asymptotically indistinguishable from uniform) or a constant above 1
  (permanent structural excess).
- **Do not settle the limit by extrapolation.** Directive 19's honest move is to
  extend one more decade (task `extend-ratio-b-decade`); see the addition below.

## Deep-tail dip result (the density-1 signal, c=None)

Deep-tail window `[0.9N,N] = [36000,40000]`: for the PRIMES the dip density
`#{n : ν₂(n)/n < c} / |window|` never exceeds 0.01 at ANY threshold
`c = 0.40..0.49` — it is 0.0000 at every c, so the "sparsity break" is `c=None`.
ALL-ONES and THUE-MORSE both break at `c=0.40` (density already > 0.01 at 0.40).
That is the density-1 signal with the negative controls failing exactly where
they must.

```claim
id: fair-variance-log-null-tail-clean-40000
statement: (corrected per directive 19) At N=40000 the prefix empirical variance
  s2_N of nu2(n)/n tracks the log null log(N)/(4N), not the constant null
  1/(4N): Ratio A = s2_N*4N = 13.94 (fails against 1), Ratio B = s2_N*4N/log N =
  1.3155 (tracks the log null with a ~32% excess). Ratio B across N:
  1.4428@1000 → 1.3921@4000 → 1.3605@10000 → 1.3368@20000 → 1.3155@40000 →
  1.297@80000. The
  excess PERSISTS across the whole measured range but the per-doubling decrements
  (−0.0507, −0.0316, −0.0237, −0.0213, −0.019) decay only slowly — the last two are in ratio
  ~0.90 — so the measured range alone does NOT determine whether the limit of
  Ratio B is 1 (primes asymptotically indistinguishable from uniform) or a
  constant above 1 (permanent structural excess). It is NOT settled by
  extrapolation. In the deep tail [0.9N,N]=[36000,40000] the primes' dip density
  #{n : nu2(n)/n < c} is 0 at every c=0.40..0.49, so the first c with density
  > 0.01 is c=None; ALL-ONES and THUE-MORSE both break at c=0.40.
hypotheses: floored oracle (nu2(53)=18, nu2(64)=27), exact Fractions, N=40000,
  deep-tail window [0.9N,N]; sequence {nu2(n)/n : n=2..N}; fair per-index
  variance 1/(4n) from Binomial(n−2,1/2).
holds-here: yes — measured to N=40000 (capture code/out/fair_variance_at_40000.txt).
status: measured
bearing: the correct prefix-variance null is log(N)/(4N); the primes sit ~32%
  above it and the excess persists with slowly-decaying per-doubling decrements
  (0.051, 0.032, 0.024, 0.021, 0.019; consecutive RATIOS 0.63, 0.75, 0.875,
  0.905 drift up toward 1 — the discriminator per directive 21, using the
  ROUNDED decrements; the EXACT decrement ratios are ≈0.623/0.752/0.899/0.878
  and the last step falls, so directive 24 withdraws the lean — NEITHER limit
  is favoured).
  Whether the limit is 1 or a constant above 1 is UNDETERMINED by N≤80000 —
  two extrapolations stated, neither declared: geometric tail ≈1.126 vs
  divergent tail →1; settling it requires more doublings (160000, 320000…)
  each ~4× the runtime (task extend-ratio-b-decade).
  Supersedes prefix-variance-fair-model-law's 'ratio drifting toward 1' reading
  (that was N≤4000 and conflated the analytic null with the Monte Carlo
  like-for-like).
anchor: code/out/fair_variance_at_40000.txt ; code/averaged/fair_variance_at_40000.py
```

## Addition: N=80000 extension (landed, attempt 2)

Extended the PRIMES-only Ratio B to N=80000 (one doubling past 40000) via the
exact s_sos oracle (`code/ratio_b/measure_ratio_b.py`; capture
`code/out/ratio_b_extension.txt`). Results:

| N     | Ratio B | per-doubling decrement | decrement ratio (this / prev) |
|-------|---------|------------------------|-------------------------------|
| 1000  | 1.443   | —      | —      |
| 4000  | 1.392   | 0.051  | —      |
| 10000 | 1.361   | 0.032  | 0.63   |
| 20000 | 1.337   | 0.024  | 0.75   |
| 40000 | 1.315   | 0.021  | 0.875  |
| 80000 | **1.297**| 0.019  | 0.905  |

The reported discriminating statistic is now the **decrement ratio**, not
"decrements are shrinking" (directive 21). At full precision the ratios are
≈0.623 → 0.752 → 0.899 → **0.878**: the last step FALLS, so the rounded
0.63 → 0.75 → 0.875 → 0.905 "drifting up toward 1" lean does not survive
exact arithmetic (directive 24) — NEITHER limit is favoured. Two
extrapolations side by side, neither declared: ratio settling below 1 ⇒
geometric tail ≈0.171 more, limit ≈1.126; ratio → 1 ⇒ tail diverges, Ratio
B → 1. (The 0.63/0.75/0.875/0.905 set was the operator's approximation from
a rounded table, not data; the exact values are the record.)

DIRECTIVE 24: the exact decrement ratios are ≈0.623/0.752/0.899/0.878 and the
last step falls, so the direction of the lean depends on that one number and
neither limit is favoured. Two extrapolations side by side:
geometric tail (ratio settles below 1) ⇒ ≈0.171 more, limit ≈1.126; ratio → 1
⇒ tail diverges, Ratio B → 1. Neither is declared. A single extra
point cannot separate "limit exactly 1 approached from above" from "limit > 1".
That would require several more doublings (160000, 320000, …), each ~4× the
runtime (~22 min for 160000, over the per-command budget), so 160000 was NOT
run. The excess PERSISTS and the limit is still UNDETERMINED — do not settle by
extrapolation. Guards (asserted on the PRODUCED array): nu2[53]=18, nu2[64]=27,
nu2[4000]=1975, mu_4000(prod)=0.497259; baseline 1000..40000 reproduced exactly
(confirms reduce convention denominator N−1). Within this run there is no
failing negative control (all-ones vacuous / Thue-Morse failing were verified
with the same oracle in the parent chebyshev capture) — stated as a limitation.
