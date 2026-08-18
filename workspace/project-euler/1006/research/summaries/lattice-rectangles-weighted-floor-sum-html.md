# Babichev & Babichev — weighted floor-sum closure

**Source:** https://arxiv.org/html/2604.22456v2  [[lattice-rectangles-weighted-floor-sum-html.full]]

The source proves closure of a fixed six-state family of polynomially weighted floor moments under affine normalization and the reciprocal Euclidean staircase step, hence O(log) evaluation for those moments. It also discusses larger weighted families. This is a theorem-level independent anchor for constant-state Euclidean floor arithmetic.

For PE1006, it supports the inner floor-moment primitive only. The paper does not discuss Sturmian words, Fibonacci factors, Ψ, or the joint sum over all rotation intercepts. Its weights are polynomial in the index, not the exact geometric powers of 10; the latter remain supported by the fhq/LOJ138/OI-Wiki sources. No direct target computation follows.

```claim
id: babichev-six-moment-floor-kernel-closure
statement: The six-moment family H_{p,q}(n;m,a,b) = Σ_{x=0}^{n-1} x^p ⌊(ax+b)/m⌋^q, q≥1, p+q≤3 (i.e. (H_{0,1},H_{1,1},H_{2,1},H_{0,2},H_{1,2},H_{0,3})) is closed under the Euclidean recursion: the affine step (a=Am+a', b=Bm+b' reduces the moments at (m,a,b) to explicit linear combinations of the moments at (m,a',b') plus power sums P_r(n) — Lemma 4 / App. B.3) and the reciprocal step (Y=⌊(a(n−1)+b)/m⌋, g(t)=⌊(mt+m−b−1)/a⌋, expresses the moments at (n;m,a,b) through those at (Y;a,m,m−b−1) plus power sums — Lemma 5 / App. B.4). Hence the six moments are evaluable in O(log m) arithmetic operations (Corollary 6, Lemma 23): each cycle strictly decreases the larger Euclidean parameter and does O(1) work per step.
hypotheses: n≥0, m≥1, a,b≥0 integers; floor over the integer quotient; the six states as defined in App. B.1.
holds-here: yes — the O(log) floor-moment closure is exactly the arithmetic the run's universal-Euclidean monoid implements; but the weights here are polynomial in x (x^p), not the geometric 10^j weights Ψ needs.
status: asserted — proofs read in full text (App. B, Lemmas 4-5, Cor 6, Lemma 23); not mechanically verified by this run.
bearing: Journal-grade independent anchor for the O(log) floor-moment recursion behind G4's inner primitive (corroborates universal-euclidean-geometric-floor-sum on the polynomial-weight side). Does NOT supply the geometric-weight monoid (fhq/OI-wiki/LOJ138 do) nor the joint-intercept aggregation Ψ(k) requires. Boundary identical to Binner (binner-reciprocity-floor-square-functions).
anchor: research/sources/lattice-rectangles-weighted-floor-sum-html.full.md (App. B lines 960-1089; Lemmas 4-5, Cor 6 lines 252-310)
follows-from: none
```

Full text: `research/sources/lattice-rectangles-weighted-floor-sum-html.full.md` (arXiv:2604.22456, v2; also `research/sources/lattice-rectangles-weighted-floor-sum-ar5iv.full.md` = landing page only).