# Deterministic van der Corput differencing on the excess sequence

```approach
idea: >
  Apply the deterministic van der Corput (Weyl) differencing lemma to the excess
  sequence S(n) = Σ_{d=2}^{n−1} (−1)^{T(n,d)} — NOT to any random object. van der
  Corput's inequality is a pure identity, no probability measure:

      |Σ_{n≤N} z_n|²  ≤  ((N+M−1)/M²) · Σ_{|m|<M} (M−|m|) Σ_n z_n z̄_{n+m}.

  Taking z_n = S(n)/n (or the ±1 fold sign), the RHS is a weighted sum of the
  index-shifted autocorrelations Σ_n S(n)S(n+m) of the excess, each of which the
  squared-excess run telescope (`squared-excess-higher-order-dyadic-correlations`)
  writes in CLOSED FORM as products of switch signs at fold-controlled separations.
  This is the deterministic analogue that the refuted probabilistic routes lacked.
mechanism: >
  (1) Every refuted concentration route (`dyadic-martingale-azuma`,
  `haar-chaos-hypercontractive`) died because Azuma/Burkholder/Bonami–Beckner are
  statements over a probability space, while S(n) is one fixed deterministic
  sequence. van der Corput is a DETERMINISTIC differencing identity: it converts a
  bound on a single sum into bounds on autocorrelations, with no measure and no
  "random h" assumption. (2) The autocorrelation Σ_n S(n)S(n+m) is, by the
  squared-excess identity, Σ_{n} Σ_{d,d'} ∏_R χ(q_{a_R−m-ish})χ(q_{b_R−m-ish}) —
  the SAME classified products of switch signs, only shifted in the window index by
  m. The meet formula and run telescope give the exact combinatorial weights, so
  the differencing step is a THEOREM (identity + geometry), not a heuristic.
  (3) The remaining arithmetic input is a bound on the SHIFTED switch-product
  correlations, strictly weaker than the standalone switch density (which the
  even-symmetric-difference theorem shows never appears as a summand). Density-1
  SUPPLY then follows by Chebyshev (GOAL priority 1); the pointwise form follows if
  the differencing closes at the L² level with a summability tail.
status: refuted
killed-by: >
  Tool/target mismatch (the on-disk original): van der Corput is a FIRST-moment
  cancellation identity — it bounds |Σ_{n≤N} S(n)| via shifted autocorrelations,
  but (A) is the SECOND moment E[S(n)²]=O(n). The shifted autocorrelations it
  produces are the same fold-weighted switch-product correlations the
  squared-excess route already prices, reached through a strictly weaker (mean,
  not second-moment) lens, so it is dominated by log-chowla + squared-excess and
  adds no new arithmetic input. Bounding Σ_n S(n) does not even imply S(n)=o(n)
  on a density-1 set. Added by the research grounding pass: for SHIFTED
  autocorrelations the two S(n) factors read OVERLAPPING windows, so the single
  symmetric-difference structure (whose evenness excludes a standalone switch
  sign) does NOT transpose — a standalone switch-density term CAN appear, and
  criterion (c) is corroborated by directive 32 (per-scale-refinement-collapses-
  to-switch-density): the shifted correlations are no weaker than switch density.
precedent: >
  (verdict: refuted) — The van der Corput differencing lemma is real,
  deterministic, and correctly stated, and it is a pure identity with no
  probability measure — this halves the mechanism is sound. Standard references:
  the classical van der Corput / Weyl differencing inequality
  |Σ_{n≤N} z_n|² ≤ (N+M)/M² · Σ_{|m|<M}(M−|m|) Σ_n z_n z̄_{n+m}
  is the engine behind van der Corput's Difference Theorem and Weyl
  equidistribution (Bergelson–Moreira, "Van der Corput's difference theorem:
  some modern developments", Indag. Math. 2015, DOI 10.1016/j.indag.2015.10.014,
  with the exact theorem and its complexity-reduction core; the modern general
  inequality is in van der Corput–Kemperman, "Eine Ungleichung von van der
  Corput und Kemperman", Monatsh. Math. 92 (1981) 139–152, DOI
  10.1007/BF01295144; the mean-square/averaged form used in analytic number
  theory is in Bernert arXiv:2310.02039 and Browning–Prendiville, Crelle 2015,
  DOI 10.1515/crelle-2014-0122). So the differencing identity is a theorem.
  But it converts a first-moment (mean) bound into bounds on the SHIFTED
  autocorrelations Σ_n S(n)S(n+m), which are the SAME fold-weighted switch-
  product correlations the squared-excess route already prices. For shifted
  autocorrelations the two S(n) factors read OVERLAPPING windows, so the
  even-symmetric-difference evasion (no standalone switch-sign summand) is NOT
  established: the shifted autocorrelation is not a single symmetric difference
  M_d △ M_{d'}, so a standalone switch-density term CAN appear, collapsing to
  the parity barrier (the candidate's own falsifier (b)). And criterion (c) is
  corroborated by in-workspace directive 32: the per-scale correlation
  decomposition collapses to the g=0 switch-density scale (claim
  per-scale-refinement-collapses-to-switch-density), so the shifted
  correlations are no weaker than switch density. In-workspace claims:
  excess-is-negative-character-sum, g-run-telescope-verified,
  per-scale-refinement-collapses-to-switch-density; the adopted
  squared-excess-higher-order-dyadic-correlations and log-chowla-entropy-
  decrement-switch both dominate this route.
first-step: >
  tool_builder, exact integer/F₂ arithmetic, real prime residue string r_j = q_j mod 4:
  (1) VERIFY the van der Corput identity as an exact-integer equality for the real
  prime string at N ≤ 2000, M = ⌊√N⌋, printing left and right sides (negative
  control: a WRONG exponent M = ⌊N/2⌋ must fail the equality). (2) COMPUTE the
  autocorrelation A_m = Σ_{n≤N} S(n)S(n+m) for m = 1..64 and confirm it equals the
  closed-form classified switch-product expression from the squared-excess identity
  (independent route). FALSIFIER: if the decomposition of A_m contains a stratum
  that is exactly the standalone switch density (contradicting the even-
  symmetric-difference theorem), the reduction collapses to the parity barrier and
  the route is dead; if the shifted correlations are as hard as switch density,
  priority 5 is the truth and is recorded.
falsifies: >
  (a) the van der Corput identity fails to hold exactly (arithmetic bug); (b) the
  shifted autocorrelation decomposes with a standalone switch-density stratum (then
  even symmetric differences is false and the route hits the parity barrier);
  (c) research shows the shifted switch-product correlations are no weaker than
  switch density (then SUPPLY ⇔ switch density, priority 5, recorded as such).
```
