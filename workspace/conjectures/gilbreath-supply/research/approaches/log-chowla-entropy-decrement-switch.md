# Entropy decrement / log-averaged Chowla for the switch-sign product correlations

```approach
idea: >
  The squared-excess route (`squared-excess-higher-order-dyadic-correlations`,
  adopted) reduces density-1 SUPPLY to E[S(n)²] = O(n), equivalently to bounds on
  the products ∏_R χ(q_{a_R}) χ(q_{b_R}) of the switch signs u_j = χ(q_j)χ(q_{j+1})
  at the fold's classified separations. These are higher-order (order ≥ 4 in χ)
  correlations of a sequence built from CONSECUTIVE primes. Attack them with Tao's
  entropy-decrement machine and the logarithmically-averaged Chowla–Elliott
  conjecture (Tao 2016; Matomäki–Radziwill–Tao averaged Chowla) — the named
  machinery purpose-built to show higher-order correlations of "prime-like"
  sequences vanish without any multiplicativity in the index.
mechanism: >
  (1) Entropy decrement does not require the target sequence to be multiplicative
  in its own index; it requires the sequence to FACTOR through a multiplicative
  source. The switch sign u_j = χ(q_j)χ(q_{j+1}) is a 2-point function of the
  multiplicative character χ at consecutive primes, so its higher-order
  correlations are exactly correlations of χ sampled at a structured set of prime
  indices. (2) The standard Möbius inversion on the prime indicator (the same
  device as Mauduit–Rivat's solution of the Gelfond digit-sum problem, in the
  library) expresses Σ_{n≤N} S(n)² — after the squared-excess run telescope — as
  log-averaged correlations of the bounded multiplicative function χ over INTEGER
  arguments at the fold's separations. (3) This is index-domain in n (the averaging
  is over the window length), so it does NOT encounter the value-shift obstruction
  that killed `dispersion-bilinear-large-sieve` and
  `matomaki-radziwill-index-autocorrelation`; and it does NOT claim Walsh/U²
  structure, so it avoids the basis mismatch that killed `gowers-u2-nilsequence-
  uniformity`. The arithmetic content is isolated as a log-averaged Chowla-type
  statement for χ, strictly weaker than positive mod-4 switch density (GOAL
  priority 2), and the second moment closes by Chebyshev (GOAL priority 1).
status: refuted
killed-by: >
  THE ENGINE'S HYPOTHESES DO NOT HOLD — entropy decrement needs the correlation
  to be a correlation of a bounded multiplicative function at AFFINE-INTEGER
  shifts in its own index. Tao's logarithmically averaged Chowla / Elliott
  theorems (Tao, "The logarithmically averaged Chowla and Elliott conjectures
  for two-point correlations", Forum Math. Pi 2016, arXiv:1509.05422; Tao–
  Teräväinen, Ant. 2019; Tao–Teräväinen, Forum Math. Sigma 2019) control sums
  Σ_n λ(a₁n+b₁)…λ(aₖn+bₖ)/n — correlations of the Liouville (or any bounded
  multiplicative) function over INTEGER arguments n + fixed shifts. The engine's
  structural input is MULTIPLICATIVITY at small primes (decompose λ(an+b) at the
  small primes dividing a, n, b). The Möbius inversion on the prime indicator
  converts the fold's second moment Σ_{n≤N} S(n)² into a sum over prime values
  q_j, q_{j'} of χ(q_j)χ(q_{j'}) at prime-INDEX separations — a BILINEAR sum in
  the index-domain string j ↦ χ(q_j), and j ↦ χ(q_j) is NOT multiplicative in j
  (the primes are not multiplicative in their index). There is no single bounded
  multiplicative function f with the fold's switch products expressible as
  Σ f(a n+b)-style one-point affine correlations; so entropy decrement's
  entire machinery (short-prime-factor reduction, entropy inequalities on
  independent random draws) never engages. This is the SAME index-vs-value
  obstruction that refuted dispersion-bilinear-large-sieve, matomaki-radziwill-
  index-autocorrelation, level-set explicit formula, and the transfer leg of
  every model route. Falsifier (b) of the candidate's own first-step fires: the
  product correlations cannot be expressed as correlations of a single bounded
  multiplicative function. AND falsifier (c) is corroborated by directive 32
  (per-scale-refinement-collapses-to-switch-density): the second-moment
  correlations collapse to the g=0 switch-density scale. So the arithmetic
  content is not strictly weaker than switch density (priority 4 is not reached);
  the honest position is priority 5 (SUPPLY's second moment is equivalent to a
  switch-density-family statement), matching every killed route.
first-step: >
  tool_builder + research, exact arithmetic, real residue string r_j = q_j mod 4.
  (1) MACHINE-VERIFY the squared run-telescope identity (SQ) for n ≤ 60 and every
      ordered pair (d,d') ∈ [2,n−1]²: ε_d ε_{d'} = ∏_{R∈runs(M_d△M_{d'})}
      (−1)^{[r_{a_R}≠r_{b_R}]}, checked against the literal ε_d ε_{d'} =
      (−1)^{T(n,d)⊕T(n,d')} (raw [r_a≠r_b] form at the position-0 boundary).
      NEGATIVE CONTROL: an r mod 3 boundary must break (SQ) on a positive count,
      else the check is vacuous. This closes the one gap the squared-excess route
      left hand-only.
  (2) STRATIFY the off-diagonal Σ_{d≠d'} ε_d ε_{d'} for the real primes at
      n = 400/1000/4000 by symmetric-difference size k = |M_d△M_{d'}| and by
      run-count, printing per-stratum partial sums. THE GATE (attacks the method
      before trusting it): (i) machine-confirm no stratum equals the standalone
      adjacent switch density Σ_a u_a (even-symmetric-difference theorem); (ii)
      compare the fold-weighted off-diagonal against the unweighted switch-product
      sum to decide whether the fold's A_k weights are load-bearing for the O(n)
      cancellation — if the unweighted sum is already O(n) the fold does no work
      (priority-5 flavour), if only the weighted sum is O(n) the priced object is
      the fold-weighted bilinear form (priority-4 flavour).
  (3) HAND research the precise statement: after Möbius-inverting the prime
      indicator, is Σ_{n≤N} S(n)² a sum of correlations of the bounded
      multiplicative χ at the fold's classified separations to which Tao's
      entropy-decrement / log-averaged Chowla hypotheses apply? FALSIFIER: the
      conversion reproduces the adjacent switch density (⇒ priority 5) instead of
      a strictly weaker weighted statement (⇒ priority 4).
precedent: >
  (verdict: refuted) — The engine is real, named, and correctly stated, but its
  HYPOTHESES fail at this object. Tao, "The logarithmically averaged Chowla and
  Elliott conjectures for two-point correlations", Forum of Mathematics, Pi
  (2016), DOI 10.1017/fmp.2016.6, arXiv:1509.05422: proves for any bounded
  multiplicative g and any fixed a₁,a₂,b₁,b₂ with a₁b₂−a₂b₁≠0,
  Σ_{x/ω<x<n≤x} g(a₁n+b₁)g(a₂n+b₂)/n = o(log ω), via the entropy-decrement
  argument + MRT short-interval averages + multiplicativity at small primes.
  Tao–Teräväinen, "The structure of correlations of multiplicative functions at
  almost all scales" (Algebra & Number Theory 13 (2019) 2103), DOI
  10.2140/ant.2019.13.2103, and "The structure of logarithmically averaged
  correlations" (Duke 2019), DOI 10.1215/00127094-2019-0002, extend to k-point
  correlations at almost-all scales and to the unweighted case. Teräväinen,
  "On binary correlations of multiplicative functions" (Forum Math. Sigma),
  DOI 10.1017/fms.2020.30. All require a bounded MULTIPLICATIVE function at
  INTEGER-argument affine shifts. The fold's second moment after Möbius
  inversion is a bilinear sum of χ(q_j)χ(q_{j'}) over PRIME indices at prime-
  INDEX separations; j↦χ(q_j) is not multiplicative in j, so the hypotheses
  fail and the machinery never engages. In-workspace: the same index-vs-value
  obstruction refuted dispersion-bilinear-large-sieve, matomaki-radziwill-
  index-autocorrelation, level-set-explicit-formula; directive 32 (claim
  per-scale-refinement-collapses-to-switch-density) shows the correlations
  collapse to the switch-density scale. Adopted route that prices the real
  object: squared-excess-higher-order-dyadic-correlations.
```
