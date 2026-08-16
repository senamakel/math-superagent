# Correlation decay ⇒ linear fold weight: the weakest-input theorem via the distance enumerator

```approach
idea: >
  Promote the adopted meet-join Parseval identity from PRODUCT measures to
  MIXING measures. The run proved (meet-join-parseval-self-duality) that for
  every product measure μ_p = p^{wt}(1−p)^{n−wt} on the cube,

      E_{μ_p}[S(n)²] = F_n(1−2p) = O(n),

  with F_n(z) = Σ_{d,d'} z^{|M_d △ M_{d'}|} the (geometry-only) distance
  enumerator, already proved O(n) for |z|<1. The primes are NOT a product
  measure — but the surviving open statement is exactly E[S(n)²] = O(n) for
  the prime gap-parity string. The theorem to prove: the same O(n) bound
  holds for EVERY measure under which the ±1 process ε_j = (−1)^{h_j} has
  sufficiently decaying correlations (ψ-mixing with summable coefficients, or
  a finite-number-of-gaps decorrelation bound). Concretely, for a measure μ
  on the cube,

      E_μ[S(n)²] = Σ_{d,d'} E_μ[ ∏_{j ∈ M_d △ M_{d'}} ε_j ],

  and each symmetric difference M_d △ M_{d'} is a union of intervals (their
  number controlled by popcount(d)+popcount(d') via the meet formula). For a
  ψ-mixing process, the correlation of a product over a set that is a union
  of k intervals is bounded by a function of the gap lengths and the mixing
  coefficients, uniformly in the set's size. The result is a transfer
  theorem: correlation decay of ε ⇒ E_μ[S(n)²] = O(n), hence by Chebyshev
  ν₂/n → 1/2 on a density-1 set — GOAL priority 2 with the weakest input
  priced exactly.
mechanism: >
  (1) The interval structure is load-bearing but must be priced exactly, not
  asserted: M_d is a reflected digital downset, hence (claim
  g-run-telescope-verified) a union of 2^{pc(d)−ν₂(d+1)} maximal intervals,
  NOT O(pc(d)) intervals — the interval count can be exponential in popcount.
  This is a two-edged fact: many intervals mean many gaps, which is GOOD for
  a mixing bound (each gap buys a factor ψ(g)), but the n² pairs must still
  sum to O(n), so the transfer needs the distance-enumerator concentration
  (popcount split at K = c·log log n, the mechanism of
  downset-row-code-distance-closed-form) and NOT a naive per-pair count.
  (2) The decorrelation estimate is the named theory of ψ-mixing / weak
  Bernoulli processes (Bradley's survey): for a set B that is a union of
  maximal intervals with k gaps, |E[∏_{j∈B} ε_j] − ∏ over components|
  is bounded by a function of the gap lengths and the mixing coefficients, so
  a summable ψ makes Σ_{d,d'} E[∏_{M_d △ M_{d'}} ε] = O(n) provided the
  low-popcount stratum (few gaps, long intervals) is small enough — which is
  exactly what the distance enumerator controls. (3) The collapse witnesses
  are exactly the NON-mixing inputs, so the hypothesis is doing real work and
  is not a closed door: all-ones has ε ≡ 1 (perfect correlation), Thue-Morse
  has persistent nonzero autocorrelation at infinitely many lags, anti-dyadic
  balanced strings are periodic — none is ψ-mixing with summable
  coefficients. The primes' ε has measured lag-1 correlation → 0 (fold-inert
  LOS bias, deliverable 5), so the hypothesis is at least approximately
  satisfied; the exact decay rate is the falsifier.
  (4) This is strictly stronger than the adopted product-measure result and
  names the actual arithmetic input the run has been pricing: a provable
  correlation-decay bound on ε_j = χ₄(q_j)χ₄(q_{j+1}). The product-measure
  case is the z^{|M_d △ M_{d'}|} specialization of the same sum.
status: grounded
precedent: >
  The correlation-decay transfer engine is the named theory of strong mixing —
  Bradley, *Basic Properties of Strong Mixing Conditions, a Survey and Some Open
  Questions*, Probab. Surveys 2 (2005) 107–144, DOI 10.1214/154957805100000104
  (defines ψ,ψ′,ρ,φ,β and their interrelations; the objective of the needed
  product-over-separated-blocks estimate), supplemented by the ψ-mixing /
  interlaced-ρ literature (lower ψ-mixing ⇒ exponential interlaced-ρ; copula
  Markov chains). The Parseval/distance-enumerator leg is already proved
  in-workspace: meet-join-parseval-self-duality, fold-second-moment-krawtchouk,
  downset-row-intersection-meet-formula (|M_d △ M_{d'}| =
  2^{pc(d)}+2^{pc(d')}−2^{pc(d∧d')+1}), anticorrelation-margin-of-the-fold. The
  INPUT hypothesis — the prime switch string ε_j=χ₄(q_j)χ₄(q_{j+1}) is ψ-mixing
  with summable coefficients — is NOT established and is the gate: its g=0
  term is the mod-4 switch-pair, the named parity barrier (abgs-p1-wide-open,
  lau-nonconstant-pattern-open), and LOS slow-decay
  (los-scale-bias-slowdecay: bias at loglog/log scale, non-summable) warns full
  ψ-mixing may be too strong. Grounding: research/grounding_three_current_candidates.md §2.
first-step: >
  tool_builder, exact arithmetic: (1) establish the interval-structure lemma
  — for every d,d' ≤ 2^14 compute M_d △ M_{d'} and count its maximal intervals
  and gaps, assert the count is 2^{pc(d)+pc(d')} or below and that the
  distance-enumerator popcount split controls the high-popcount stratum
  (brute downsets, no primes). (2) For the 2-state Markov ε-process with the
  primes' measured parameters (switch prob a ≈ 0.52, lag-1 corr −0.04..−0.15)
  compute E[S(n)²]/(n−2) exactly (matrix-product transfer) over n up to 2^15
  and confirm it stays O(1); negative control: a NON-mixing process (periodic
  ε, or ε ≡ 1) must give Ω(n) or fail the O(1) plateau. (3) State the precise
  ψ-mixing theorem (Bradley, the "summable coefficients" form) and price the
  single remaining input: the ψ-coefficient decay of ε_j along the primes.
  FALSIFIER: if a ψ-mixing process is found with E[S²] = ω(n) (a mixing
  collapse witness), the transfer theorem is false and correlation decay is
  not sufficient; if the primes' ε decay rate is shown non-summable, the
  hypothesis does not hold here and the route dies with that reason.
falsifies: >
  (a) the interval-structure lemma fails (then the geometry transfer is wrong);
  (b) a ψ-mixing input with E[S²]/n → ∞ exists (correlation decay is not the
  right weakest input); (c) the prime ε-process provably has non-summable
  correlations (the hypothesis fails here — this is the live risk, since the
  LOS switch bias decays only at loglog x / log x scale, which is NOT summable,
  and the theorem would then need the weaker second-moment-only input, not
  full mixing).
