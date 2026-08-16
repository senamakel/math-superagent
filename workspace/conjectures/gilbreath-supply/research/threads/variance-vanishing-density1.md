# Variance-vanishing: the second-moment route to density-1

Directive 9 connected the Chebyshev negative (a bounded mean does not give
density-1) to the second moment. **Directive 14 supersedes directive 10 and 13:
the `s2_N/(1/(4N))` ratio is dropped as the null test** (s2_N is a prefix
statistic and 1/(4n) a per-index variance — different objects). The operative
statement is the measured tail density-1 signal, and sharper: the pointwise
tail-min signal.

```thread
id: variance-vanishing-density1
question: Is s2_N = Var(ν₂(n)/n over n≤N) → 0 provable for the prime h — and
  from what arithmetic input? The measured s2_N decays 0.000783@4000 →
  0.0000934@40000 (~1/N), the input Chebyshev needs to turn into density-1
  ν₂ ≥ c·n (GOAL priority 1). Sharper than density-1 (directive 14): the tail
  min of ν₂/n over [X,N] is RISING — 0.3396@50 → 0.4599@1000 → 0.4850@10000 →
  0.4901@30000 — evidence for ν₂/n → 1/2 POINTWISE with no exceptional set in
  the computed tail. The sharpest open problem is therefore: prove s2_N → 0,
  or prove the exceptional set is finite. s2_N → 0 is the WEAKER sufficient
  input for SUPPLY (it yields the density-1/averaged form via Chebyshev);
  finiteness of the exceptional set is the stronger pointwise statement. The
  two are not equivalent — mean + vanishing variance give density-1, not
  finiteness.
status: dead  (terminus — directive 33: hypothesis refuted by deliverable_3, run closes negative; see research/CONCLUSION.md)
rests-on: mean-bounded-not-density1 (bounded mean alone gives only positive
  density, directive 3(c) answered), fair-model-exact-binomial (uniform h ⇒
  exact Binomial(n−2,1/2)), excess-is-negative-character-sum
  (S(n)=n−2−2·ν₂(n)), n40000-second-moment-density1-measured (directive 14),
  prime-E-S2-On-sharp-conjecture (directive 31: E[S²]=O(n) ⇒ density-1 only;
  subgaussian tail ⇒ finite exceptional sets)
blocked-by:
next: Prove s2_N → 0 (or the exceptional set is finite) for the prime h, from
  the weakest arithmetic input. **Directive 18 settles the prefix-variance
  null:** the correct null is log(N)/(4N) (each ν₂(n)/n has fair variance
  ≈1/(4n), and the prefix variance is their average), not 1/(4N) — Ratio A
  = s2_N·4N = 13.94 fails the constant null, Ratio B = s2_N·4N/log N = 1.3155
  tracks the log null with a ~32% excess at N=40000 (claim
  fair-variance-log-null-tail-clean-40000). Ratio B across N (1.443@1000 →
  1.392@4000 → 1.361@10000 → 1.337@20000 → 1.315@40000) shows a PERSISTENT
  excess falling with slowly-decaying decrements (−0.0507, −0.0316, −0.0237,
  −0.0213; the last two steps are each ~a doubling and the decrement only shrank
  to ≈0.9 of its predecessor). **Directive 19: this does not separate a limit
  of 1 from a constant above 1** — but DIRECTIVE 21 corrects this reading: shrinking decrements do not
  discriminate (the harmonic series shrinks strictly yet diverges); the
  discriminator is the RATIO of consecutive decrements. **Directive 24
  corrects the lean:** the 0.63, 0.75, 0.875, 0.905 ratios were the
  operator's approximations from a rounded table, NOT data. The EXACT
  decrement ratios are ≈0.623, 0.752, 0.899, 0.878 and the last step FALLS
  (0.899 → 0.878), so the "rising toward 1" lean does not survive exact
  arithmetic and NEITHER limit is favoured.** Both extrapolations stated,
  neither declared: geometric tail
  ≈1.126 vs divergent tail →1. The sharpest open question is whether the
  primes are asymptotically indistinguishable from uniform for this statistic;
  the settlement is the ratio drift, not a one-decade extension (head is task
  correct-ratio-b-overclaim). The deep tail
  [0.9N,N] is dip-free at every c=0.40..0.49 (first break c=None) while
  all-ones and Thue-Morse break at c=0.40. What remains after the extension is
  the Monte Carlo
  like-for-like primes/fair at N=40000 (task push-prefix-variance-null-40000).
  Keep the two negative controls in any further
  capture — all-ones vacuous, Thue-Morse fails (~99.3% of n below 0.30) — so
  the pipeline is shown discriminating. Label everything measured, not proved.
```

## Directive 14 — the capture is vindicated, the ratio test is dropped

`code/out/chebyshev_second_moment_N40000.txt` is populated and correct for the
primes (`mu_N=0.499658` at N=40000). The `mu=0.064146` read beside the primes
is the **Thue-Morse negative-control** value at its own N=4000 ceiling, not
contamination of the primes table. The `4N·s2_N` ratio against `1/(4N)` is
**dropped as a test**: s2_N is a prefix statistic and 1/(4n) a per-index
variance, different objects, so the ratio is not the decisive null test.
The operative statement is the measured tail density-1 signal and the rising
tail min (claim `n40000-second-moment-density1-measured`).

## Directive 15 → 18 — the prefix-variance null, settled

The flawed comparison was `s2_N` vs the analytic per-index `1/(4N)`. Directive 15
reinstated the correct like-for-like test (primes' prefix variance vs Monte
Carlo fair-model prefix variance); directive 18 then settled the analytic side:
the correct null is `log(N)/(4N)` — each `ν₂(n)/n` has fair variance ≈ `1/(4n)`,
and the prefix variance is their average `(1/N)Σ 1/(4n) ≈ log(N)/(4N)` — so
Ratio A `= s2_N·4N = 13.94` fails the constant null while Ratio B
`= s2_N·4N/log N = 1.3155` tracks the log null with a ~32% excess at N=40000
(claim `fair-variance-log-null-tail-clean-40000`). Ratio B across N
(1.443@1000 → 1.315@40000) shows a persistent excess falling with
slowly-decaying decrements (last two steps ~doubling, decrement ratio ≈0.9).
**Directive 19: this does not separate a limit of 1 from a constant above 1**
— geometric decay at 0.9 gives ≈1.13, slower decay diverges to 1. Settle by a
one-decade extension (task `extend-ratio-b-decade`), not extrapolation. The
Monte Carlo like-for-like (primes/fair = 1.283@4000) is requeued behind the
extension (task `push-prefix-variance-null-40000`).
Measured, not proved.

## The measured numbers (this run's capture, not a proof)

From `code/out/chebyshev_second_moment_N40000.txt` (primes, floored oracle):
`μ_N = 0.499658` at N=40000; `s2_N` decays `0.000783@4000 → 0.0000934@40000`
(~1/N, std 0.0097). Over `[30000,40000]` every n has `ν₂/n ≥ 0.49` (min
0.490114, zero dips below 0.45); over `[50,40000]` only 1 n below 0.35, 3 below
0.40, 10 below 0.42, 51 below 0.45, all densities < 0.0013. Tail min of `ν₂/n`
over `[X,N]` rising: 0.3396@50 → 0.4599@1000 → 0.4850@10000 → 0.4901@30000.
Negative controls: all-ones (M=0, vacuous), Thue-Morse (fails, ~99.3% of n
below 0.30). All measured, not proved.

## Why this is the sharp question (corrected by directive 14)

The decay `s2_N ~ 1/N` is what the fair model predicts (uniform h ⇒
`Var(ν₂/n) = (n−2)/(4n²) ≈ 1/(4n)`), so the decay alone is not
prime-specific evidence — and the `s2_N/(1/(4N))` ratio conflates a prefix
statistic with a per-index variance, so it is not the null test to run. What
*is* prime-specific and measured is the **sparsity of the dip set** (the
density-1 tail) and the **rising tail min** (the pointwise signal): a random
string has the same variance decay but not the empty tail. The Chebyshev glue
(variance → 0 ⇒ density-1 `ν₂ ≥ c·n`) remains pure and Lean-formalisable; the
open arithmetic content is proving `s2_N → 0` for the primes, or the stronger
finiteness of the exceptional set.
