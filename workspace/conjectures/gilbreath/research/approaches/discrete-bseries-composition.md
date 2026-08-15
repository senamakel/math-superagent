```approach
idea: Treat the row map T: row -> |partial row| as a discrete nonlinear flow and expand its k-th iterate in the canonical B-series / rooted-tree (Butcher group) basis, so that the second column A_k(1) becomes an explicit rooted-tree sum over the initial gap word; the conjecture is then a boundedness theorem about a distinguished B-series coefficient, attacked with the Butcher group's Hopf-algebra structure.
mechanism: |
  The map T acts on a row h = (h_0, h_1, ...) of non-negative integers by
  (Th)_i = |h_i - h_{i+1}|. Write the nonlinearity as
      |a - b| = (a + b) - 2*min(a,b),
  i.e. a LINEAR difference operator minus a "min" nonlinearity. The iterate
  T^k applied to the initial halved gap word is therefore a composition of k
  layers, each a linear map plus a min-nonlinearity. In the theory of
  discrete B-series (Calvo–Chartier–Murua; Chartier–Hairer–Vilmart's
  "algebraic structures of B-series" and the Butcher group), an arbitrary
  composition of a linear part and a nonlinear part has a CANONICAL
  expansion as a formal sum over rooted trees (or coloured trees for the
  min-branch): each tree contributes a product of the nonlinearity's
  derivatives (here: discrete min, whose "elementary differentials" are
  extremely sparse) times the linear part's coefficients (the Pascal/binomial
  weights, i.e. the Sierpinski pattern).

  Concretely, A_k(1)/2 should equal a finite signed sum over rooted trees of
  degree <= k, each tree weighted by (a) a number of leaves equal to a
  window of the gap word and (b) a combinatorial coefficient that is the
  composition law in the Butcher group. The {0,2} block is the region where
  all min-branches are trivial (h_i - h_{i+1} in {-1,0,1} after halving),
  so the tree expansion has a "tropical zero" structure there. The
  conjecture A_k(1) in {0,2} becomes: a distinguished tree-sum does not
  exceed 1 in absolute value. This is a purely algebraic statement in the
  incidence Hopf algebra of rooted trees (Connes–Kreimer), independent of
  primality, and the supply/regeneration content is the growth of the number
  of trees of given degree that survive the min-branch cancellation.

  Named mathematics: the Butcher group and B-series, the Connes–Kreimer
  Hopf algebra of rooted trees, discrete B-series for difference operators
  (Chartier–Hairer–Vilmart 2010; Calvo–Chartier–Murua), and the composition
  of diffeomorphisms as a pre-Lie / Novikov-algebra product. This is a
  genuinely different axis: it is NOT a scalar potential (refuted class),
  NOT a mod-2^t linearization, NOT a finite-state/automaticity claim, and
  NOT the Riordan/Sheffer array (which is the *linear* part only). It keeps
  the full nonlinearity, organised algebraically.
status: refuted
killed-by: |
  Two independent groundings. (1) SMOOTHNESS. The elementary differentials
  of a B-series are F[tau] = f^(n)(...)(F[t_1],...,F[t_n]) — they require
  DERIVATIVES f^(n) of the map. |a-b| and min(a,b) are not differentiable at
  the switch hyperplane a=b, and the run has established (rule90-interior-xor,
  proved) that inside the {0,2} block the map reduces to XOR/Rule 90, while
  the absolute value keeps a genuine non-smooth kink at the boundary. The
  nearest non-smooth extension in the literature is Bruned–Ebrahimi–Fard–Hou
  2024 multi-indice B-series (arXiv:2402.13971, JLMS 2024), but it is still
  a Taylor-type expansion of 1-dimensional affine-local maps — no Hopf-
  algebraic "bounded-coefficient" theorem, and nothing that hands back a
  bound on a single coefficient. Thus the "canonical rooted-tree expansion
  of the iterate of |partial|" the mechanism asserts is not the Butcher-
  group/B-series object (which is smooth), and the non-smooth generalisation
  that exists is a different formalism without the Hopf structure the idea
  needs. (2) SIZE. Even granting a rooted-tree expansion, writing A_k(1) as
  a sum over rooted trees of degree <= k produces at least |T_k| terms, where
  |T_k| (the number of rooted trees of order <= k) grows like rho^k with
  rho = 2.95576... — the same exponential leaf growth as the already-proposed
  lattice-path-weighted-enumeration-left-column, which the run has not closed
  for that reason. A boundedness theorem on a single B-series coefficient of
  an exponentially large tree-sum is no easier than the original A_k(1) in
  {0,2} statement — it just re-writes the recursion the run already had. Where
  the min-branch is trivial (the {0,2} block), the expansion collapses to the
  linear Pascal/Rule-90 part, which the run has already handled and proven
  (rule90-interior-xor); the content lives exactly where B-series has no
  footing.
precedent: |
  B-series/Butcher group: Butcher 2021 "B-Series"; Sanz-Serna–Murua 2015 (arXiv:1503.06976); Butcher–Mitsui–Miyatake–Sato 2024 (arXiv:2409.08533, B-series composition theorem); Calaque–Ebrahimi-Fard–Manchon 2010 (doi 10.1016/j.aam.2009.08.003); Connes–Kreimer Hopf algebra of rooted trees. Non-smooth/multi-index extension: Bruned–Ebrahimi-Fard–Hou 2024, "Multi-indice B-series", arXiv:2402.13971 / J. Lond. Math. Soc. (doi 10.1112/jlms.70049). Rooted-tree count: Otter 1948 (|T_k| ~ C·(2.95576)^k k^{-5/2}). NONE applies B-series or the Hopf algebra of rooted trees to Gilbreath or to iterated absolute differences (searched "B-series absolute value min branch", "piecewise linear nonsmooth iteration rooted tree B-series", "rooted trees Gilbreath"). The run's own held claims: rule90-interior-xor (proved), fwd-diff-identity-refuted (signed-forward-difference linearization dead at (3,2)).
```

**Grounding note (research, this cycle).** Refuted on the most speculative of the three — and exactly at the point the inventor flagged as the cheap first-step falsifier ("does the min-branch cause cancellation or exponential tree growth before any Hopf work"). The B-series machinery is a smooth-ODE formalism whose elementary differentials need derivatives the map does not have; the non-smooth multi-indice extension exists but lacks the Hopf structure the proposal's boundedness theorem would need; and even in the best case the number of degree-<=k rooted trees grows like 2.9557^k, so the coefficient-sum is not a handle on A_k(1) — it is an exponential re-writing of the recursion, no better than the lattice-path enumeration already on disk. The linear contribution inside the {0,2} block is the already-proved Pascal/Rule-90 part; the genuinely nonlinear content is precisely where no rooted-tree/Hopf theorem applies.
