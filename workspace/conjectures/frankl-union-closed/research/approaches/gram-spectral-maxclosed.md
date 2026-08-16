# Gram matrix / spectral-copositive attack on max-closed column sets

```approach
idea: Encode a family F ⊆ 2^[n] by its 0/1 incidence matrix M (n × m) and its
  co-occurrence Gram matrix G = M·Mᵀ. Then G_{xy} = |{A ∈ F : x,y ∈ A}| and the
  diagonal G_{xx} is exactly the abundance of x; UC is equivalent to
  max_x G_{xx} ≥ m/2. Union-closure of F says precisely that the m columns of M
  form a subset of {0,1}^n closed under coordinatewise max — a "max-closed set"
  in the sense of Jeavons–Cohen (the feasible sets of a max-closed CSP). So the
  whole conjecture becomes an optimization over max-closed 0/1 point sets of
  the largest diagonal of their Gram matrix, relaxable by the moment/SOS
  (Lasserre) hierarchy over the convex hull of a max-closed set.
mechanism: The iid-entropy argument (Gilmer/AHS) uses only the marginal
  densities p_x — the *diagonal* moment G_{xx}/m — and its OR-closure
  constraint collapses to a one-variable inequality h(2p−p²) ≤ h(p), capping at
  (3−√5)/2. The Gram matrix keeps the *off-diagonal* moments G_{xy}, and
  union-closure constrains them hard: max-closure forces the convex hull to be
  a max-closed polytope, which has an explicit linear description (Jeavons–Cohen
  binary max-closed hulls), so G must lie in a completely-positive cone
  intersected with that polytope's moment constraints. Perron–Frobenius on
  G ≥ 0 gives spectral information (ρ(G) dominates tr(G)/n), and the hierarchy
  of moment matrices is strictly richer than the first-moment entropy bound.
  This is a *named* and *certifiable* hierarchy (copositive / moment-SOS), and
  its level-1 certificate should reproduce exactly the (3−√5)/2 barrier while
  higher levels can only increase it — giving either a new constant or a proved
  certificate that the hierarchy itself stalls, which is a barrier theorem.
status: refuted
killed-by: boolean-max-closed-is-union-closed — Jeavons–Cohen's "max-closed" objects (Jeavons–Cohen–Gyssens, J.ACM 1997, doi:10.1145/263867.263489; Rossi–Walsh et al. Handbook 2006, doi:10.1016/s1574-6526(06)80012-x) are relations closed under componentwise max over a *totally ordered domain*. Over the Boolean domain {0,1}, coordinatewise max is exactly set union, so a "max-closed set of columns" is EXACTLY a union-closed family: the reformulation is a restatement of the conjecture, not a new convex description. The claim that "the max-closed hull has an explicit linear description" is unsupported for the Boolean/union-closed case (the tractable max-closed *linear* structure, Cohen–Jeavons–Jönsson–Koubarakis doi:10.1145/355483.355485, is over ordered numerical domains, not {0,1}); the convex hull of a union-closed family has no standard polyhedral description beyond itself, and "level-1 of the SOS/copositive hierarchy reproduces exactly the (3−√5)/2 entropy barrier" is unchecked speculation (Boppana's h(x²)≥φ·x·h(x) is an entropy inequality, not a moment-SOS level-1 result). No application of a moment/SOS/copositive hierarchy to the union-closed conjecture was found (searched: "Gram matrix union-closed moment SOS copositive"; the closest optimization literature, Poonen's weight system and Pulaj's cutting planes doi:10.14279/depositonce-6534, is LP/CP over abuse weights, not a max-closed-polytope hierarchy).
precedent: jeavons-cohen-max-closed (Jeavons–Cohen–Gyssens, J.ACM 1997, https://doi.org/10.1145/263867.263489; Rossi–Walsh–et-al., Handbook of Constraint Programming 2006, https://doi.org/10.1016/s1574-6526(06)80012-x; Cohen–Jeavons–Jönsson–Koubarakis 2000, https://doi.org/10.1145/355483.355485); poonen-weights (Poonen, JCTA 1992, https://doi.org/10.1016/0097-3165(92)90068-6); pulaj-cutting-planes (Pulaj, 2017, https://doi.org/10.14279/depositonce-6534).
first-step: Build M and G from the canonical oracle (code/lib/uc.py) for the
  guard families (2^[n], singleton-containing, an EIL small-set family) and for
  tight-at-1/2 examples; compute eigenvalues/trace of G and the linear
  description of the max-closed hull; then formulate and solve the level-1
  moment/SOS relaxation over a 2- or 3-element ground set and check that its
  optimum is (3−√5)/2, not 1/2. Confirm the three negative controls on G.
```

## Speculation, marked

The claim that the moment/SOS hierarchy over max-closed hulls is *strictly
stronger* than the iid-entropy bound, and that it either certifies a constant
above (3−√5)/2 or admits a clean barrier certificate, is my speculation — it has
not been checked against the literature and the hierarchy may collapse to the
first moment. The safe, non-speculative content is: (i) the exact equivalence
UC ⟺ max_x G_{xx} ≥ m/2 for the Gram matrix of a max-closed column set, and
(ii) the fact that max-closed sets/polytopes have an explicit linear theory
(Jeavons–Cohen), which together give a finite, moment-relaxable convex
reformulation. The iid-entropy barrier being "the first-moment relaxation" is a
clean hypothesis to test, not an established fact.
