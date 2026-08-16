# SUPPLY threshold limit — does the "typical" weight ratio tend to 0 or plateau near 1/8?

This is the third-pass goal (GOAL.md "the one computation this pass owes") decomposed
backward. It is **not** SUPPLY for the primes; it is the finite-string question:

> Does the minimum weight ratio `w/n` at which linear supply becomes *typical*
> tend to **0**, or plateau near **1/8**?

The measured column is `0.375, 0.300, 0.250, 0.286, 0.188, 0.156, 0.125, 0.125`
at `n = 8, 10, 12, 14, 16, 32, 64, 128` (sampled, ~300 samples/weight). The
decomposition below replaces the sampling with an **exact closed form** and
reduces the decision to a Krawtchouk/hypergeometric question — no primes, no
number theory.

## The key structural fact (why this is decidable at all)

The fold cell `T(n,d) = ⊕_{o⊆d} h[n−1−d+o]` is a parity over exactly
`m_d = 2^popcount(d)` **distinct** positions (`fold-cell-degree-is-2^popcount`).
For `h` a uniformly random string of weight `w`, the number `X` of ones landing
in the cell's `m_d` positions is Hypergeometric(`n`, `m_d`, `w`), so

```
P[T(n,d) = 1] = P[X odd] = (1/2)·(1 − E[(−1)^X]),
```

where `E[(−1)^X] = K_w(m_d; n)/C(n,w)` and
`K_w(x;n) = Σ_j (−1)^j C(x,j) C(n−x, w−j)` is the Krawtchouk polynomial. This
single fact converts the whole question into a deterministic computation of
Krawtchouk values — no sampling, no primes.

**Correction (adversarial, this pass).** An earlier draft of this file carried
the pointwise bound `|E[(−1)^X]| ≤ (1−2θ)^m` for `X ~ Hypergeometric(n, m, ⌊θn⌋)`,
`θ ∈ (0,1/2)`. That bound is **false**. Counterexample `n=6, m=3, w=2`
(`θ=1/3`): `P[X=j] = (1/5, 3/5, 1/5)`, so `E[(−1)^X] = 1/5 − 3/5 + 1/5 = −1/5`,
yet `(1−2θ)^m = (1/3)^3 = 1/27 ≈ 0.037 < 0.2`. The correct engine is the exact
identity plus the *unimodality* bound in G-threshold-parity-control below. The
false bound was also the sole justification for marking the concentration step
"discharged via fold-distance-enumerator-On" — that step is **not** discharged;
it is the open gap G-threshold-concentration.

```skeleton
goal: Determine whether the minimum weight ratio θ(n) = min{ w/n : linear supply is
      typical at weight w } tends to 0 or plateaus near 1/8, where "typical" means
      E[ν₂(n)/n] ≥ 0.40 and P[ν₂(n)/n ≥ 0.40] ≥ 0.5 over uniformly random weight-w
      strings h ∈ F₂ⁿ. The decomposition's answer: θ(n) → 0, and the measured
      0.125 at n = 64, 128 is a finite-size artifact, not a plateau.
implies: G-threshold-mean-closed-form gives the exact scalar M(n,w) = E[ν₂(n)/n]
      as (1/2n)·Σ_{d=2}^{n−1}(1 − K_w(2^popcount(d); n)/C(n,w)), removing the
      sampling entirely. G-threshold-parity-control supplies the one safe bound
      on the cell parity (exact generating function + unimodality
      |E[(−1)^X]| ≤ C/√(1+θ(1−θ)m(1−m/n)) for X ~ Hyper(n,m,⌊θn⌋)); this is the
      corrected replacement for the refuted pointwise bound. G-threshold-asymptotic-zero
      feeds that bound into the popcount count #{d : pc(d)=k} = C(⌊log₂n⌋,k) to
      prove M(n,⌊θn⌋) → 1/2 for every fixed θ ∈ (0,1/2), hence the mean-crossing
      threshold θ_mean(n) → 0. G-threshold-concentration proves Var(ν₂(n)) = o(n²)
      for fixed θ via the exact second moment E[S²] = Σ_{d,d'} K_w(|M_d △ M_{d'}|;n)/C(n,w)
      (symmetric-difference sizes from downset-row-intersection-meet-formula),
      so ν₂/n concentrates and the fraction criterion follows once the mean
      exceeds 0.40; hence the measured threshold (mean AND frac) also → 0.
      G-data-reconciliation evaluates the exact finite sums at n = 8..128 and
      beyond, providing the explicit column GOAL.md asks for and confirming the
      small-n plateau is an artifact. All four lemmas are pure F₂/hypergeometric
      combinatorics; no prime input is involved.
status: sketched
rests-on: fold-cell-degree-is-2^popcount (proved — m_d = 2^popcount(d) distinct
      positions per cell), downset-row-intersection-meet-formula (proved —
      |M_d △ M_{d'}| = 2^pc(d)+2^pc(d')−2^{pc(d∧d')+1}, the geometry feeding the
      second moment), excess-is-negative-character-sum (checked — the ν₂ ↔ S
      dictionary identifying "linear supply" with ν₂/n), fair-model-exact-binomial
      (proved — the uniform-h special case, the w-mixture of these moments).
killed-by: none
```

```gap
id: G-threshold-mean-closed-form
lemma: For h uniformly distributed on the weight-w slice of F₂ⁿ (w ones, n−w
      zeros, all C(n,w) strings equally likely), the expected fold weight is
      exact: E[ν₂(n)] = (1/2)·Σ_{d=2}^{n−1}(1 − K_w(2^popcount(d); n)/C(n,w)),
      with K_w(x;n) = Σ_{j=0}^{w} (−1)^j C(x,j) C(n−x,w−j). Equivalently
      E[ν₂(n)/n] = (1/2n)·Σ_{d=2}^{n−1}(1 − E[(−1)^{X_d}]) where X_d ~
      Hypergeometric(n, 2^popcount(d), w). Pure F₂ + hypergeometric
      combinatorics, no number theory. It reproduces the measured threshold
      column: at n=16, cells are 3 at m=2, 6 at m=4, 4 at m=8, 1 at m=16; w=3
      gives E[ν₂] = 3834/560 = 6.846 (0.428 ≥ 0.40) and w=2 gives 628/120 = 5.233
      (0.327 < 0.40), so the mean crosses 0.40 at exactly w=3, θ=0.1875, matching
      the measured θ(16)=0.188.
status: discharged
discharged-by: guruswami-macwilliams-lp-from-fourier (proved — the Krawtchouk
      evaluation Σ_{wt h=w} (−1)^{h·1_M} = K_w(|M|;n); with |M| = 2^popcount(d)
      this is exactly the per-cell parity E[(−1)^{X_d}] = K_w(2^pc(d);n)/C(n,w)).
      Only the *computation* (reproduce the measured column and push n) remains;
      that is a task, not a lemma, and is the first move of G-data-reconciliation.
next: tool_builder/symbolic_math: (a) implement M(n,w) = (1/2n)Σ_d (1 −
      K_w(2^pc(d);n)/C(n,w)) over n ∈ {8,10,12,14,16,32,64,128} and assert the
      measured θ column (0.375, 0.300, 0.250, 0.286, 0.188, 0.156, 0.125, 0.125)
      is reproduced from the mean-≥0.40 criterion; (b) verify the parity identity
      P[X odd] = (1 − K_w(m;n)/C(n,w))/2 by brute force over ALL weight-w strings
      at n=8,16 against the canonical fold oracle (s_sos), with a negative control
      (a wrong parity formula) shown failing; (c) then push the closed form — not
      sampling — to n ∈ {256,512,1024,2048,4096} over w/n ∈ {1/32..1/4} and
      report θ*(n) = min{w/n : M(n,w) ≥ 0.40}. This last step IS the computation
      GOAL.md says the pass owes, with the sampling ceiling removed (cost O(n log n)).
thread: research/threads/supply-class-characterisation.md
```

```gap
id: G-threshold-parity-control
lemma: (the one safe cell-parity bound, replacing the refuted pointwise bound)
      For X ~ Hypergeometric(n, m, w) with w = ⌊θn⌋, θ ∈ (0,1) fixed:
      (i) EXACT — E[(−1)^X] = [z^w](1−z)^m (1+z)^{n−m} / C(n,w), the coefficient
      of z^w; equivalently K_w(m;n)/C(n,w). (ii) UNIMODAL — X is log-concave
      (hence unimodal), and |E[(−1)^X]| ≤ max_j P[X=j] ≤ C/√(1 + θ(1−θ)m(1−m/n))
      for an absolute constant C, by splitting the alternating sum at the mode
      (each monotone side is bounded by the mode atom) and the standard
      log-concavity local bound max_j p_j = O(1/√(1+Var X)). This bound is TRUE in
      the corner where the refuted bound failed: n=6, m=3, w=2 has Var = 2·(1/3)(2/3)(3)(1/2)
      = 2/3, C/√(5/3) ≈ C·0.77 ≥ 0.2 for any C ≥ 0.26, consistent with the true |E|=0.2.
status: open
next: theorem_prover: pin the absolute constant C in the log-concavity bound
      max_j P[X=j] ≤ C/√(1+Var X) for hypergeometric X (the library carries
      odonnell-boolean-fourier-degree-k-toolkit and the coding-theory machinery,
      but this specific bound is to be proved, not cited). symbolic_math: verify
      (ii) numerically for all (n,m,w), n ≤ 40, and check the sharp corner n=6,
      m=3, w=2. This one lemma is shared verbatim by G-threshold-asymptotic-zero
      and G-threshold-concentration, so closing it closes half of both.
```

```gap
id: G-threshold-asymptotic-zero
lemma: For every fixed θ ∈ (0,1/2) and w = ⌊θn⌋, the biased-cell sum is
      sublinear: (1/n)·Σ_{d=2}^{n−1} K_w(2^popcount(d); n)/C(n,w) → 0 as n → ∞.
      Consequently E[ν₂(n)/n] → 1/2 for every fixed θ > 0, so the mean-crossing
      threshold θ_mean(n) = min{w/n : M(n,w) ≥ 0.40} → 0. Engine (corrected):
      group cells by popcount k; there are C(⌊log₂n⌋, k) cells with m_d = 2^k,
      and G-threshold-parity-control gives |K_w(2^k;n)/C(n,w)| ≤ C/√(1 + θ(1−θ)2^k(1−2^k/n)).
      The worst-case group k = ⌊log₂n⌋/2 has C(L,k) ~ 2^L/√L ~ n/√log n and
      2^k ~ √n, contributing ~ (n/√log n)/n^{1/4} = n^{3/4}/√log n = o(n); groups
      with 2^k ~ n have C(L,k) = O(1); small-k groups have C(L,k) = O(log^k n)
      and bounded denominator. Summing over k gives o(n), hence E[ν₂/n] → 1/2.
status: open
next: tool_builder: evaluate the exact group sum Σ_k C(L,k)·|K_w(2^k;n)|/C(n,w)
      at θ ∈ {1/32, 1/16, 1/8, 1/4}, n = 2^8..2^20, and print the ratio /n (must
      fall to 0). theorem_prover: assemble the rigorous o(n) proof from
      G-threshold-parity-control + the binomial-coefficient bound on the number
      of popcount-k cells — no primes, no fold geometry beyond popcount(d); the
      claim is elementary and a theorem_prover can carry it end to end.
```

```gap
id: G-threshold-concentration
lemma: For every fixed θ ∈ (0,1/2), w = ⌊θn⌋, Var(ν₂(n)) = o(n²), hence
      ν₂(n)/n → 1/2 in probability; the fraction P[ν₂/n ≥ 0.40] → 1, so the
      measured "typical" condition (mean ≥ 0.40 AND frac ≥ 0.5) holds for every
      fixed θ in the limit and the sampled threshold θ(n) → 0. Engine: with
      ε_d = (−1)^{T(n,d)}, ν₂ = (n−2−S)/2 and E[ε_d ε_{d'}] = K_w(|M_d △ M_{d'}|;n)/C(n,w),
      because ε_d ε_{d'} = (−1)^{T_d ⊕ T_{d'}} is the parity over the symmetric
      difference M_d △ M_{d'} (size given by downset-row-intersection-meet-formula).
      Hence E[S²] = Σ_{d,d'} K_w(|M_d △ M_{d'}|;n)/C(n,w); the diagonal contributes
      n−2. Bound each off-diagonal term by G-threshold-parity-control applied to
      m = |M_d △ M_{d'}|, and count pairs by their symmetric-difference size.
      NOTE (correction): this is NOT discharged by fold-distance-enumerator-On —
      that claim bounded Σ z^{m} for |z|<1 with a pointwise z^m ≤ (1−2θ)^m
      substitution that fails for hypergeometric parity (see header correction).
      The pair-count over the symmetric-difference multiset is the open content.
status: open
next: tool_builder: compute the exact symmetric-difference multiset N(m) =
      #{(d,d') : |M_d △ M_{d'}| = m} for n ≤ 2^12 (exact, via the meet formula,
      not enumeration) and the exact E[S²] = Σ_m N(m)·K_w(m;n)/C(n,w) at
      θ ∈ {1/32, 1/16, 1/8, 1/4}; report E[S²]/n² and whether it decays, with
      negative controls w = 1 (S = Θ(n), E[S²] = Θ(n²)) and w = n (all-ones
      kernel, ν₂ = 0) shown NOT decaying. theorem_prover: bound
      Σ_m N(m)/√(1 + θ(1−θ)m(1−m/n)) = o(n²) from the popcount-pair count —
      the single open step, elementary but not yet on disk. If the pair-count
      does not give o(n²), the mean-only result (G-threshold-asymptotic-zero)
      still stands and the fraction criterion is the honest residual gap.
```

```gap
id: G-data-reconciliation
lemma: The measured threshold column τ(n)/n = 0.375, 0.300, 0.250, 0.286, 0.188,
      0.156, 0.125, 0.125 at n = 8,10,12,14,16,32,64,128 is reproduced by the
      exact finite G-threshold-mean-closed-form sum (and its second-moment
      refinement), and the two consecutive 0.125 values are a slow-decay regime
      at L = ⌊log₂n⌋ = 6,7 — not a limit. At L = 6,7 the cells with popcount ≤ 3
      number C(6,≤3) = 41 of 63 and C(7,≤3) = 64 of 127 respectively, a positive
      fraction that only vanishes as L → ∞; this is exactly why the mean at small
      α dips below 0.4n at n = 64 but the exact formula predicts no such barrier
      for large n.
status: open
next: tool_builder: evaluate the exact G-threshold-mean-closed-form sum (and the
      G-threshold-concentration second moment) at n = 8,10,12,14,16,32,64,128 and
      report the exact τ_mean(n)/n beside the measured column; then evaluate at
      n = 2^6..2^20 and report the decay of τ_mean(n)/n — the deliverable is the
      exact column that shows whether the ratio falls through 1/8, with the
      measured values as the small-n check. No sampling needed; 300-sample
      agreement at n ≤ 128 is the verification, not the evidence.
```
