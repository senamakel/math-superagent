# Fair model is exact: wt(Φ_n h) is Binomial(n−2, 1/2) for uniform h

Directive 10. The capture `code/out/fair_model_exact.txt` is stronger than it
was labelled. It is not an empirical fit — it is a consequence of the rank fact
already on disk (claim `fold-rank-is-n-2-nullity-2-alternating`).

## The argument

The operative fold matrix `Φ_n` is `(n−2) × n` with rows `d = 2..n−1`, and
`rank Φ_n = n−2` (full row rank), nullity 2. A full-row-rank linear map over
`F₂` is **surjective**: every point of `F₂^{n−2}` is attained. The fibres of a
linear map are cosets of the kernel, and the kernel has `2^{nullity} = 2^2 = 4`
elements, so **every image point is attained by exactly 4 preimages**.

Now take `h` uniform on `F₂^n` (the cube). Its image `wt(Φ_n h)` is uniform on
`F₂^{n−2}` pulled back through the weight map, so the number of preimages of a
weight `k` is `4 · C(n−2, k)`. Hence

    Pr[wt(Φ_n h) = k] = 4·C(n−2,k) / 2^n = C(n−2,k) / 2^{n−2}.

That is exactly **Binomial(n−2, 1/2)**. The table in `fair_model_exact.txt`
(n=12 row `4, 40, 180, 480, 840, 1008, 840, …` = `4·C(10,k)`) is the
**confirming check**, not the evidence. The evidence is surjectivity + nullity
2, which is a statement about `Φ_n` alone and holds for every `n` (all-n via
the unit-lower-triangular submask-XOR argument; machine-checked n = 2..20).

Consequences:

- `E[wt(Φ_n h)] = (n−2)/2`; `Var(ν₂/n) = (n−2)/(4n²) ≈ 1/(4n)`.
- **Chernoff:** for any fixed `c < 1/2`, `Pr[wt(Φ_n h) < c·n] ≤ exp(−Ω_c(n))`,
  so `wt(Φ_n h) ≥ c·n` holds with probability `1 − exp(−cn)`.
- The measured prime Cesàro mean `μ_N = 0.4977` (N=4000) sits on the random
  prediction `1/2` — see claim `avg-supply-empirical`.

## Position (directive 10): the difficulty is non-adversariality

SUPPLY is therefore **true with overwhelming probability for a uniformly random
input** to `Φ_n`. This is a statement about the fold, not about the primes, and
it is orthogonal to — touches none of — the five closed doors in `problem.md`
§4, which refute hypotheses of the form "h is complicated enough" (all-ones
stays in the kernel with `ν₂ = O(1)`, Thue-Morse stays sublinear, anti-dyadic
inputs stay bounded). The whole remaining difficulty is that the primes are not
known to be non-adversarial for this fold: the arithmetic input to prove is
some correlation/variance statement on the prime gap-parity string `h`, or the
negative theorem that SUPPLY ⇔ switch density. This is GOAL priorities 2 and 3.

Author: director (filing directive 10; the arithmetic is the rank claim's).
Anchor: `code/out/fair_model_exact.txt` (confirming check),
`code/fold_rank/rank_of_fold.py`, claim `fold-rank-is-n-2-nullity-2-alternating`.

```claim
id: fair-model-exact-binomial
statement: For h uniform on F2^n, wt(Phi_n h) is EXACTLY Binomial(n-2, 1/2):
  Pr[wt(Phi_n h) = k] = C(n-2, k) / 2^{n-2}. Equivalently the weight-k fibre
  of the operative (n-2) x n fold matrix Phi_n has 4·C(n-2, k) inputs. This
  follows from rank Phi_n = n-2 (full row rank) with nullity 2: Phi_n is
  surjective onto F2^{n-2}, and every image point has exactly 2^2 = 4
  preimages. Mean (n-2)/2; Var(nu2/n) = (n-2)/(4 n^2) ~ 1/(4n). The exact
  counts in code/out/fair_model_exact.txt (e.g. n=12: 4,40,180,480,840,1008,
  840,... = 4·C(10,k)) are the CONFIRMING check, not the evidence.
hypotheses: rank Phi_n = n-2 (full row rank), nullity 2, for the operative
  (n-2) x n matrix with rows d = 2..n-1 (claim
  fold-rank-is-n-2-nullity-2-alternating; machine-checked n=2..20, all-n via
  the unit-lower-triangular submask-XOR argument, task prove-fold-rank-all-n);
  h uniform on F2^n.
holds-here: yes — this is the actual fold whose weight the run measures, and
  the rank fact is on disk.
status: proved (from surjectivity + nullity 2; NOT a measured fit)
bearing: kills the misreading that the decaying empirical variance is
  prime-specific. Var(nu2/n) ~ 1/(4n) is the fair-model null for ANY uniform
  input, so the *sample* variance s2_N has fair-model expectation
  E[s2_N] = (1/N)sum_{n<=N} Var(nu2(n)/n) ~ log(N)/(4N) (NOT 1/(4N): the small
  values X_n = nu2(n)/n are mutually independent under the fair model and
  mu_N is their average, so E[s2_N] ~ (1/N)sum 1/(4n), and the log is what
  resists the lowering of the mean correction). The decisive statistic is the
  ratio s2_N / (log(N)/(4N)) = 4N·s2_N/log(N), which is ~ 1 under the null and
  deviates from 1 when the primes are non-adversarial/adversarial for this
  statistic. (CORRECTED: an earlier version of this claim, and the operator's
  directive, guessed the null as 1/(4N); the exact-sequence computation above
  shows log(N)/(4N).)
falsifies: would be false only if rank Phi_n < n-2 (surjectivity fails), which
  contradicts the rank claim.
anchor: code/out/fair_model_exact.txt (check), code/fold_rank/rank_of_fold.py,
  claim fold-rank-is-n-2-nullity-2-alternating
```

```claim
id: uniform-random-h-supply-whp
statement: For h uniform on F2^n, wt(Phi_n h) >= c·n with probability at least
  1 - exp(-Omega_c(n)) for every fixed c < 1/2, by Chernoff on the exact
  Binomial(n-2, 1/2) of claim fair-model-exact-binomial. Thus SUPPLY
  (nu2(n) >= c·n for all large n) holds for a uniformly random h with
  probability 1 - exp(-c n), and a single uniform draw fails only with
  exponentially small probability.
hypotheses: claim fair-model-exact-binomial (exact Binomial(n-2,1/2) for
  uniform h); standard Chernoff bound.
holds-here: yes — the exact binomial is established for the actual fold.
status: proved (Chernoff on an exact binomial)
bearing: the fold imposes no generic obstruction: a random input satisfies
  SUPPLY w.h.p. The only open content is whether the PRIME gap-parity string is
  non-adversarial, i.e. an arithmetic/correlation input on h (GOAL priority 2)
  or SUPPLY <=> switch density (GOAL priority 3).
falsifies: would be false if the exact binomial failed (it does not) or if
  Chernoff were misapplied (c fixed strictly below the mean (n-2)/2n).
anchor: claim fair-model-exact-binomial
```

```claim
id: supply-difficulty-non-adversarial-reframing
statement: SUPPLY holds with probability 1 - exp(-c n) for a uniformly random
  input (claim uniform-random-h-supply-whp), and the measured prime Cesaro
  mean 0.4977 sits on the random prediction 1/2 (claim avg-supply-empirical).
  Therefore the entire remaining difficulty is that the prime gap-parity string
  h is not known to be non-adversarial for the fold Phi — an arithmetic input
  on h must be proved (GOAL priority 2), or SUPPLY shown equivalent to switch
  density (GOAL priority 3). This reframing touches NONE of the five closed
  doors in problem.md §4: those refute 'h is complicated enough' hypotheses,
  while this is a statement about the fold on uniform input.
hypotheses: uniform-random-h-supply-whp (proved), avg-supply-empirical
  (measured prime mean = 0.4977 at N=4000).
holds-here: yes, for the framing it states.
status: asserted (a reframing of what is left, derived from two proved/checked
  facts; not itself a new theorem)
bearing: re-prices the whole problem: the variance decay s2_N ~ 1/N is the
  fair-model null, not prime-specific evidence, so the live question is the
  ratio s2_N/(1/(4N)) and the weakest arithmetic input on h.
falsifies: would be wrong if a theorem showed the prime h is adversarial
  (sublinear fold weight), or if the primes were known non-adversarial and
  SUPPLY thereby solved.
anchor: claims uniform-random-h-supply-whp, avg-supply-empirical;
  thread fair-model-non-adversarial-reframing
```
