# Iterated union-entropy operator (entropy-production dynamics)

```approach
idea: Replace the one-shot entropy inequality with the *dynamics* of the
  union operator on the probability simplex. Define T: Δ(2^[n]) → Δ(2^[n]) by
  T(μ)(S) = Σ_{A∪B=S} μ(A)μ(B) — the law of the union of two independent
  draws from μ. Union-closure says supp(Tμ) ⊆ supp(μ) for μ supported on F, so
  H(Tμ) ≤ H(μ). The one-shot barrier that caps the iid method at (3−√5)/2 is a
  statement about a *single* application of T at a fixed μ. The new object is
  the semigroup/iteration: T^k(μ) = law of the union of 2^k iid draws, and the
  *marginal flow* it induces. Coordinate i of the flow obeys
  p_i^{(k+1)} = 2p_i^{(k)} − (p_i^{(k)})², whose fixed points are {0,1} and
  which sends any p_i > 0 to 1 − (1−p_i)^{2^k} → 1 super-exponentially fast.
mechanism: The one-step certificate is capped because it evaluates the pairwise
  entropy gain h(2p−p²)−h(p) once, at the original marginal p. Under iteration
  the marginals escape the (3−√5)/2 barrier region: even a family where every
  element sits below density 1/2 has its k-union marginal pushed toward 1 for
  k ≈ log log(1/(1−p)). So an entropy budget counted *across the trajectory*
  {H(T^k μ)} — each step bounded by the Lagrange/Shearer-style inequalities at
  the *evolved* marginals, telescope-summed — is a strictly stronger certificate
  than the one-shot, exactly the locus the dependent-coupling line (capped at
  t̂_max ≈ 0.38235 in the two-atom class) could not reach. The endgame: on a
  minimal counterexample (every element density < 1/2) the telescoped gain must
  exceed log|F|, contradiction. This is a genuinely different *representation*:
  an operator semigroup and its spectral/contraction analysis, not a single
  two-variable inequality. Speculative and unproved; the fixed-point/escape
  structure is exact and checkable.
status: refuted
killed-by: k-union-closed-generalization — the "iterated union operator / marginal
  flow p^{(k)} = 1−(1−p)^{2^k}" IS the k-fold-union (k-union-closed) object, and
  that generalisation is already a closed route whose constants STRICTLY
  DECREASE in k. The named theorem is the generalised Boppana inequality
  α_k·h(x^k) ≥ x^{k−1}·h(x), where α_k is the positive root of x(1+x)^{k−1}=1
  (Yuster arXiv:2302.12276; Wakhare arXiv:2312.14743; Ho arXiv:2601.19327,
  Lean-verified). The one-shot constant is the k=2 case: c = α_2/(1+α_2) =
  (3−√5)/2 ≈ 0.38197 (α_2=(√5−1)/2 solves α(1+α)=1). For k=3 the same
  machinery gives α_3≈0.4656, c≈0.318 < 0.382, and the constants keep
  decreasing (verified analytically: k=2→0.38197, k=3→~0.318; matches
  `boppana-entropy-inequality` and `ho-generalized-boppana-k`). Hence the
  natural reading of "telescoped entropy across the 2^k-union trajectory" — the
  object the proposed first-step itself computes — is exactly the k-generalisation
  already excluded because it cannot beat the one-shot. The claim that the
  iterated semigroup is a STRICTLY STRONGER certificate is contradicted: the
  uniform k-fold certificate is strictly weaker. (Residual gap, stated plainly:
  a genuinely different telescoping — a non-uniform sum of per-step increments
  each evaluated at evolved marginals — is not literally Yuster's uniform bound,
  and no source in or out of this library establishes or refutes THAT specific
  object; the refutation above covers the claimed mechanism and the object the
  first-step measures, which is the k-fold marginal.)
precedent:
  - k-union-closed-generalization, (Yuster, Almost k-union closed set systems, arXiv:2302.12276)
  - iterated-entropy-derivatives, (Wakhare, Iterated Entropy Derivatives and Binary Entropy Inequalities, arXiv:2312.14743)
  - ho-generalized-boppana-k, (Ho, A generalization of Boppana's entropy inequality, arXiv:2601.19327)
  - boppana-entropy-inequality, (Boppana, the k=2 case, ≤ (3−√5)/2)
  - sawin-above-barrier, (Sawin, arXiv:2211.11504)
first-step: With the canonical oracle, take the near-5-cube family and a few
  small union-closed families, compute the exact marginal trajectory
  p^{(k)} = 1−(1−p)^{2^k} for every element, and the exact entropy H(T^k μ)
  (exact multinomial counts, not floats), and measure the telescoped gain
  Σ_k [h(p^{(k)} repeated)-gain]. Decide whether the trajectory escapes the
  (3−√5)/2 cap on any family and by how much — before any inequality is written
  down. Confirm the three negative controls on the flow (2^[n] gives p=1/2
  fixed; a non-union-closed family shows supp escaping F).
```

**Grounding verdict — REFUTED (on the collision + decreasing-constants evidence).**

What the reformulation is actually called: this is the *k-fold union / k-union-closed* generalization of Gilmer's method, and the named theorem governing it is the *generalized Boppana entropy inequality* `α_k·h(x^k) ≥ x^{k−1}·h(x)`, where `α_k` is the positive root of `x(1+x)^{k−1}=1` and `h` is binary entropy. This is established in Yuster (arXiv:2302.12276, formally the multidimensional extension of Chase–Lovett), Wakhare (arXiv:2312.14743, via iterated derivatives with generalized Stirling numbers), and Ho (arXiv:2601.19327, Lean-verified). The proposed first step — computing the marginal trajectory `p^{(k)} = 1−(1−p)^{2^k}` — is precisely the marginal of a k-fold union of iid draws, i.e. exactly this object.

Hypotheses: the generalised-Boppana inequality holds for all real k > 1, equality at x ∈ {0, 1/(1+α_k), 1}; it is a *scalar* per-coordinate inequality over independent Bernoulli marginals — the same iid class whose barrier is (3−√5)/2. It applies here (the pieces are iid unions), and it is what the telescoped sum would be built from.

Application to this problem: the whole generalization is the existing, closed `k-union-closed-generalization` route. The constants `α_k/(1+α_k)` **strictly decrease** in k: k=2 gives (3−√5)/2 ≈ 0.38197; k=3 gives α_3/(1+α_3) ≈ 0.318 (α_3≈0.4656, verified analytically). So iterating the union operator, under the natural reading this candidate itself specifies, certifies *less*, not more — the direct negation of its claim of a "strictly stronger certificate."

What it would buy: nothing — a route provably weaker than the one-shot, already on the closed list. The one genuinely unexplored sliver (a non-uniform telescoped sum at evolved marginals, distinct from Yuster's uniform bound) has no source either way, and is the only honest remaining question under this heading. Do not re-propose the uniform k-fold form.
