# An order-K (>1) functional controllable by an input weaker than switch density

GOAL.md (second pass), priorities 1–2: the single reopened question. The first
pass died believing every functional of the fold collapses to the `K=1` pair
correlation; `REOPENED.md` refuted that with an explicit witness, so the
deliverable is a functional that provably sees past pairs, together with the
arithmetic input that controls it. This skeleton takes the canonical witness
functional — the signed-excess second moment `S²` — and decomposes the claim
that it answers the question.

```skeleton
goal: >
  There is a functional of the fold that (i) is sensitive at correlation order
  K for every 1 < K ≤ K*(n) ≈ ⌈n/2⌉ — concretely S(n)² = (Σ_{d=2}^{n-1}
  (−1)^{T(n,d)})², which is NOT determined by pair correlations and is
  determined only at order ⌈n/2⌉ — and (ii) is controllable by an arithmetic
  input on the prime gap-parity string h that is strictly weaker than pointwise
  mod-4 switch density; the control yields ν₂(n) ≥ c·n on a density-1 set
  (problem.md result 3; GOAL.md priority 1, priced in priority 2).

implies: >
  The functional is F = S(n)², with S(n) = (n−2) − 2ν₂(n) (claim
  excess-is-negative-character-sum), so F is a function of the fold coordinates
  T(n,d) = ⊕_{o⊆d} h[n−1−d+o] and of Φ_n h alone. Three lemmas combine.

  (SENSITIVITY) G-order-sensitivity records the witness that S² is not a K=1
  functional, and G-order-budget records the measured threshold K*(n) ≈ ⌈n/2⌉
  at which it becomes determined. Together they certify clause (i): the
  functional genuinely sees structure past pair correlations, so it is not a
  re-labelling of the switch-density (adjacent-pair) object that the known
  reduction discards.

  (CONTROL) G-second-moment-control is pure algebra + Chebyshev: a second-moment
  bound on S(n) empties the lower tail of ν₂(n)/n, so the fold weight is
  controlled by the single scalar input "S(n) = O(√n)" (equivalently
  S(n)² = O(n), a submask-window second-moment / Walsh bound on h).

  (ARITHMETIC) G-prime-second-moment states that the real prime string h
  satisfies S(n) = O(√n) from an unconditional arithmetic input — the single
  surviving open statement of the first pass — and G-input-strictness states
  that this input is strictly weaker than switch density by exhibiting a
  switch-density-0 string that satisfies it.

  Chain: G-second-moment-control applied to the input granted by
  G-prime-second-moment gives ν₂(n)/n → 1/2 on a density-1 set (in fact
  pointwise under the uniform S = O(√n) reading). G-input-strictness shows the
  input does not imply positive switch density, so clause (ii) holds.
  G-order-sensitivity + G-order-budget show the functional doing the work is at
  correlation order ~n/2, not order 1. The three together discharge the goal.
  Quantifier care: "S = O(√n)" is read uniformly (S(n)² = O(n) for all large n,
  giving pointwise ν₂/n → 1/2); the weaker averaged input
  (1/N)Σ_{n≤N} S(n)²/n² → 0 gives only the density-1 form, and both are stated
  inside G-second-moment-control so the weaker one never gets inflated to the
  stronger.

status: sketched

rests-on: >
  excess-is-negative-character-sum, fold-rank-n-minus-2-binomial-proved,
  downset-row-intersection-meet-formula, fold-distance-enumerator-On,
  g-run-telescope-verified, squared-excess-run-endpoint-product,
  no-standalone-switch-sign-in-squared-excess, lucas-submask-odd
```

```gap
id: G-order-sensitivity
lemma: >
  S(n)² is not determined by pair correlations: there exist two binary strings
  with identical correlation vectors of order 1 but different S(n)². The
  canonical witness is n = 8, h = 00000010 (1 at index 6) and h' = 00000100
  (1 at index 5): both have C₁ = (5, 1, 1, 0) yet S²(h) = 0 and S²(h') = 4.
  Consequently S² is sensitive at correlation order K = 2 — it is not a K=1
  functional, and no collapse theorem forces it through adjacent-pair
  correlations.
status: discharged
discharged-by: >
  research/REOPENED.md (the collapse-hypothesis refutation) with the
  independent hand-check in research/witness-crosscheck-imported.txt.
  Not yet a claim block in the ledger; the witness is stated and re-verified
  on disk, which is enough to mark the lemma discharged for this skeleton.
next: >
  (bookkeeping, not a proof gap) file a claim block carrying the witness so
  later skeletons cite a claim id rather than REOPENED.md.
```

```gap
id: G-order-budget
lemma: >
  The correlation order at which S(n)² becomes determined is K*(n) = ⌈n/2⌉ for
  all n ≥ 6 (and K*(4) = K*(5) = 2, with n = 5 the sole exception to the
  ⌈n/2⌉ formula). Precisely: for every K < K*(n) there exist h, h' with
  identical correlation vectors C₁, …, C_K but different S(n)², and at
  K = K*(n) no such pair exists. Measured n = 2..20 (research/
  witness-hunt-n20-imported.txt): K* = 1,1,2,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10.
  This certifies that the sensitivity of S² reaches order ~n/2, i.e. the whole
  budget GOAL.md claims for the reopened pass, not just order 2.
status: open
next: >
  tool_builder: extend the witness hunt behind research/witness-hunt-n20-imported.txt
  to n = 21..128 (exact F₂, canonical floored oracle, guards ν₂(53)=18,
  ν₂(64)=27). For each n compute the maximal K with a witness pair (identical
  C₁..C_K, different S²) and test the two conjectures: (a) K*(n) = ⌈n/2⌉ for
  all n ≥ 6; (b) the n = 5 exception is isolated (K*(n) = ⌈n/2⌉ − 1 exactly at
  n = 5, nowhere else). Report witness pairs and a negative control
  (witness@K = n−1 is False at every n, since full-order correlations determine
  h up to the kernel and S² is kernel-invariant) so the search is not vacuous.
```

```gap
id: G-second-moment-control
lemma: >
  A second-moment bound on S(n) empties the lower tail of the fold weight.
  (strong) If S(n) = O(√n) uniformly then ν₂(n)/n = 1/2 − 1/n − S(n)/(2n) → 1/2
  pointwise, hence ν₂(n) ≥ c·n for every c < 1/2 and all large n.
  (weak) If (1/N)Σ_{n≤N} S(n)²/n² → 0 then, with μ_N the empirical mean of
  ν₂(n)/n, Chebyshev gives #{n ≤ N : ν₂(n)/n < c₀/2}/N ≤ 4σ²_N/c₀² → 0, so
  ν₂(n) ≥ (c₀/2)·n on a density-1 set. Both are pure algebra (2ν₂ − (n−2) = −S)
  plus Markov/Chebyshev; no number theory and no property of h.
status: discharged
discharged-by: >
  the identity 2ν₂ − (n−2) = −S (claim excess-is-negative-character-sum) and
  elementary Markov/Chebyshev; the density-1 form is written out in the bearing
  of research/notes/pattern_finder_second_moment_plateau.md. This is the glue,
  not the hard part — it is what makes the single arithmetic scalar S = O(√n)
  the whole demand.
next: >
  lean_prover: formalise the two implications (strong and weak) against the
  Mathlib Chebyshev/Markov lemma, with #print axioms and no sorryAx — a pure
  inequality so it closes quickly and removes any doubt that the control step
  is the trivial half of the argument.
```

```gap
id: G-prime-second-moment
lemma: >
  The real prime gap-parity string h (h[j] = ((q_{j+1}−q_j)/2) mod 2) satisfies
  S(n) = O(√n), equivalently S(n)² = O(n), from an unconditional arithmetic
  input (or at worst conditional on Shiu 2000, held abstract in problem.md).
  Priced in the fold's own coordinates (claim
  squared-excess-run-endpoint-product): this is exactly the statement that
  S(n)² = (n−2) + Σ_{d≠d'} ∏_{R ∈ runs(M_d △ M_{d'})} χ(r_{a_R}) χ(r_{b_R})
  is O(n) — a submask-window second-moment / Walsh bound on h at correlation
  order ≥ 2, never a single switch sign (claim
  no-standalone-switch-sign-in-squared-excess). This is the single surviving
  open statement of the first pass (research/CONCLUSION.md §5) and the
  arithmetic heart of the reopened question.
status: open
next: >
  Two concrete first moves, both runnable today. (a) tool_builder: compute the
  exact submask-window Walsh coefficients of the prime h up to n = 10^6 and the
  off-diagonal run-endpoint product sum to the oracle ceiling, recording the
  measured ratio E[S²]/(n−2) and the threshold the O(n) bound demands, with
  Thue-Morse (grows ~n per-index, fails) as the negative control.
  (b) theorem_prover/research: price the index-domain statement
  Σ_{d≠d'} ∏_R χ(r_{a_R})χ(r_{b_R}) = O(n) for the fixed prime boundary r — the
  named open request walsh-spectral-subset-b904. If the only input that implies
  it is positive switch density itself, the honest output is the rival skeleton
  supply-switch-equivalence.md (GOAL priority 4), not a claim of this route.
```

```gap
id: G-input-strictness
lemma: >
  The second-moment input is strictly weaker than pointwise mod-4 switch
  density: there is a binary string h* with switch density 0 (o(n) ones) that
  nevertheless satisfies S(n) = O(√n). Then the input does not imply positive
  switch density, so clause (ii) of the goal holds and the fold contributes
  work the switch-density reduction discards.
status: open
next: >
  tool_builder / sat_solver: for n = 8..64 compute max_{h : wt(h) ≤ k} S(n)²/n
  over a grid k/n → 0 and report whether any sparse h keeps sup_n S(n)²/n
  bounded. This is a finite exact-F₂ computation and is NOT the already-refuted
  G-eq-sparse-fold-is-sublinear (that tested fold weight ν₂; this tests the
  second moment S², the genuinely different object — the e_{2^m} witness has
  S(2^m+1) = Θ(n), so it fails here). Two sharp sub-moves: (a) use the read-cone
  bound ν₂(n) ≤ n·Σ_{j ∈ S} 2^{−popcount(n−1−j)} (research/approaches/
  read-cone-column-equivalence.md) to reduce the search to a dyadic-measure
  question about sparse sets; (b) if the search finds no sparse witness through
  n = 64, that is evidence (not proof) the second-moment input implies switch
  density, which would refute this skeleton's strictness clause and point the
  run at a different order-K functional or at priority 4.
```

## Relation to the other skeletons

This is the positive branch of the reopened question, and it *contains* the
second-moment route but adds the order-K requirement the first pass never wrote
down. `supply-averaged-second-moment.md` is the same Chebyshev engine without
the sensitivity/strictness clauses; `weak-input-fold.md` is the same
strictness clause without naming the functional's correlation order.
`supply-switch-equivalence.md` is the rival: its G-sup-implies-switch is the
contrapositive of this skeleton's hope, and refuting G-sup-implies-switch is
exactly what G-input-strictness (or a weaker witness) would deliver.
