# ν₂ supply as a minimum-distance statement of a linear code over F₂

```approach
idea: The ν₂ supply transfer Φ_n (the F₂ Pascal/Rule-90 fold of the halved-gap mod-2 bit) is a linear map, so its image is a linear code C_n = im(Φ_n). The open supply bound ν₂ ≥ c·w is exactly a minimum-distance statement d_min(C_n) ≥ c·w, attackable with algebraic coding theory: the MacWilliams identity, the dual code, and the Delsarte linear-programming (Krawtchouk) bound.
mechanism: |
  ν₂(q_n) = wt(Φ_n h) with h the mod-4 switch bit over [2,n−1], w = wt(h),
  Φ_n the fixed F₂ Pascal/Rule-90 fold (claims `supply-nu2-factorization`,
  `G-supply-linearization`). The universal bound wt(Φ_n h) ≤ (2/3)wt(h) is
  machine-refuted (consecutive-odds h in ker Φ_n gives ν₂=0). The proposal
  reads the supply as d_min(im Φ_n) ≥ c·w and attacks it with MacWilliams
  duality + the Delsarte LP bound.
status: refuted
killed-by: transfer-matrix-kernel-allones (rank Φ_n = n−3, kernel = span(all-ones)) — the image code is trivial
  STRUCTURAL: Φ_n is an (n−3)×(n−2) F₂ matrix of rank n−3 (run's checked claim
  `transfer-matrix-kernel-allones`: rank n−3, nullity 1, kernel = span(111..1)).
  Because rank = #rows = n−3, im(Φ_n) = F₂^{n−3} — the ENTIRE output space.
  Hence the image code C_n = im(Φ_n) has minimum distance d_min = 1 (could not
  be lower), the dual code is trivial (0-dimensional), and the Delsarte LP /
  MacWilliams / Krawtchouk machinery has nothing to certify: a full-space code
  carries no minimum-distance constraint. Hand-check n=5: rows (0,1,1),(1,0,1)
  span F₂², d_min=1. So candidate 1's central premise — that ν₂ ≥ c·w is a
  minimum-distance statement of a nontrivial code — is FALSE. The supply is NOT
  a code distance; it is the weight of the image of a SINGLE vector h under a
  surjective fold, and that weight can only be small if h is near the kernel,
  which for a rank-(n−3) map in an (n−2)-dim domain is a SINGLE direction
  (the all-ones vector), not a high-codimension subspace.
  Also: the kernel is span(111..1), NOT the "dyadic-periodic subspace" the
  candidate files assume; the refined target min_{h∉ker} wt(Φ_n h)/wt(h) is a
  genuinely thinner statement than d_min(C_n) and even if it held uniformly the
  all-ones counterexample (h in ker, nu2=0, w=n−2) shows the relative expansion
  is 0 for the collapse direction — so no uniform c>0 survives even over h∉ker
  in the asymptotic family. The empirically meaningful object (prime h only,
  nu2/w ∈ [0.515, 0.87]) is case (b) prime-specific per `g-supply-transfer-refuted`;
  no universal coding-theoretic constant exists.
precedent: |
  Delsarte LP / MacWilliams / Krawtchouk bounds (textbook; e.g. "On Delsarte's
  Linear Programming Bounds for Binary Codes", FOCS 2005 doi:10.1109/SFCS.2005.55;
  J. MacWilliams & N. J. A. Sloane, The Theory of Error-Correcting Codes, 1977;
  "New Solutions to Delsarte's Dual Linear Programs", IEEE-IT 2024
  doi:10.1109/TIT.2024.3476974). None applies this to Gilbreath — consistent
  with claim `block-growth-literature-not-covered`. Run-internal precedent:
  claims `transfer-matrix-kernel-allones`, `g-supply-transfer-universal-refuted`,
  `g-supply-transfer-measured`, `supply-nu2-factorization`.
first-step: (was) compute d_min(im Φ_n) for n=3..40 — THIS STEP IS NOW MOOT: d_min=1 identically.
side: regeneration (supply side)
named-mathematics: linear codes over F₂, MacWilliams identity, dual codes, Delsarte LP bound, Krawtchouk polynomials
speculative: (moot) uniformity and LP tightness of d_min(im Φ_n) ≥ c·w
falsifier: an n with true d_min(im Φ_n) < c·w — (vacuous: d_min=1 always).
```
