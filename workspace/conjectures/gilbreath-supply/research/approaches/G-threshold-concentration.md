```approach
idea: Prove Var(ν₂(n)) = o(n²) at fixed θ = w/n, the concentration companion to the asymptotic-zero limit: not only does the weight-w mean of ν₂ vanish at fixed positive density, its variance is subquadratic so the threshold is sharp. Pure F₂/hypergeometric, no primes.
mechanism: Under the uniform distribution on weight-w strings, the second moment of ν₂ is a double sum of Krawtchouk pair overlaps over row pairs (d,d'), with the weight constraint imposed through K_w; the second-moment route's distance enumerator F_n(z) over |M_d △ M_d'| is the natural object to carry this. Proposed route, not established.
status: grounded
precedent: >
  Engine named and applicable: the same HKS normalized-Krawtchouk exponential
  decay (Harrow–Kolla–Schulman, DOI 10.4086/toc.2014.v010a003, Lemma 2.2:
  |κ_k^n(x)| ≤ e^{-c·kx/n} for 0≤k≤x≤n/2) bounds the large-|M_d △ M_{d'}|
  off-diagonal terms of E[S²] = Σ_{d,d'} K_w(|M_d△M_{d'}|;n)/C(n,w); the
  hypergeometric log-concavity mode bound (Greene–Wellner Bernoulli 2017,
  DOI 10.3150/15-bej800; Lahiri–Chatterjee Proc AMS 2007) bounds the rest.
  In-workspace: downset-row-intersection-meet-formula (proved — the
  symmetric-difference multiset |M_d△M_{d'}| feeding the second moment);
  sphere-mean-krawtchouk-exact (proved); excess-is-negative-character-sum.
  Residual open step: the pair-COUNT over the symmetric-difference multiset
  giving o(n²) is not yet on paper (fold-distance-enumerator-On does NOT
  discharge it — see supply-threshold-limit.md header correction).
first-step: Express the exact second moment E_w[ν₂(n)²] as a double Krawtchouk sum and compute it exactly for small n at fixed θ to confirm the o(n²) scaling before attacking the asymptotics; then bound the pair-count over the symmetric-difference multiset (the open step) with HKS + the mode bound.
```

