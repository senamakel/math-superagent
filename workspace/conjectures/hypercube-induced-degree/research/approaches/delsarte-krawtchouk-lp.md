# Delsarte / Krawtchouk LP on the Hamming scheme

```approach
idea: Attack f(n) in the Hamming association scheme H(n,2): the quantity of
interest is the inner distribution of S under the Hamming metric, so Delsarte's
linear programming bound (Krawtchouk polynomials / MacWilliams transform) is the
native home of the parity codes that make this problem, and it turns the lower
bound into a *linear program* whose dual variable is a machine-checkable witness.

mechanism: The Bose–Mesner algebra of Q_n is spanned by the distance matrices
D_0..D_n with eigenvalues the Krawtchouk matrix K; the adjacency matrix is D_1
and the identity is D_0. For S, define the inner distribution a_i = (1/|S|)·#ordered
pairs (v,u) ∈ S×S with dist(v,u)=i; then a_0 = 1, a_i ≥ 0, Σ a_i = |S|, and the
average internal degree equals a_1 exactly (a_1 = 2e(S)/|S|). Since D(S) ≥ a_1
(max ≥ average), minimising a_1 over the Delsarte polytope { a ≥ 0, K·a ≥ 0,
Σ a_i = 2^{n-1}+1 } gives a lower bound on f(n). The parity classes (even-weight
code, odd-weight code) are exactly the Delsarte-optimal objects at distance 2, so
this is where the +1-vertex excess sits.

This is the *average-degree* route and the record says averaging caps at
Θ(log n); the honest value of this proposal is therefore (i) a machine-checked
quantitative certificate of exactly where the LP stops — an obstruction theorem
(R9) with a number attached, not a slogan — and (ii) a test of whether the
per-vertex "max ≤ d" constraints, added as a (valid but large) family of linear
inequalities, restore tightness at √n. If the LP dual is tight at the parity
codes, it re-derives the √n bound in the coding-theory frame with a certificate
as evidence; if it is not, the integrality gap *is* the obstruction located.

covers: reproduces `huang-f-n-sqrt-n` and `f-exact-1..5` from the
Bose–Mesner/Krawtchouk algebra (the adjacency spectrum is the Krawtchouk
transform), satisfying Scholze's rule.

status: refuted
killed-by: (1) Scholze's rule fails: the signed adjacency A_n that carries the
  sqrt(n) eigenvalue is NOT in the Bose-Mesner algebra of the Hamming scheme —
  its sign depends on the differing coordinate and the prefix parity, not on
  Hamming distance — so the MacWilliams constraint K·a >= 0 (the only
  constraint of the Delsarte LP) cannot see the sqrt(n) eigenvalue. The Delsarte
  LP on the inner distribution therefore cannot reproduce `huang-f-n-sqrt-n`
  in the coding-theory frame, as the covers clause claims. (2) The survival
  claim min a_1 (average internal degree) <= f(n) is average-type, so by the
  problem.md/probabilistic obstruction it caps at Theta(log n) — it cannot
  reach sqrt(n). Verified by construction: even if the LP dual is tight at the
  parity codes it yields only an average bound. Survives only in its modest
  instrument guise (machine-checked certificate locating WHERE the LP stops),
  which is orthogonal to closing the gap.
precedent:
  - Delsarte 1973, "An algebraic approach to the association schemes of coding
    theory" (Hamming scheme, MacWilliams transform, Krawtchouk LP) — the object
    is real and well-studied.
  - https://link.springer.com/article/10.1007/s10623-023-01191-y (Unique optima
    of the Delsarte LP, Des. Codes Cryptogr. 2023) — uniqueness when d<=2;
    optimal "quasicodes" and parity phenomena, exactly the d=2 parity regime of
    this problem.
  - https://dl.acm.org/doi/10.1109/TIT.2024.3476974 (New solutions to Delsarte's
    dual LPs) — dual-witness machinery, MRRW-type solutions, bounds on A(n,d).
  - https://www.sciencedirect.com/science/article/pii/S0024379506004630
    (Delsarte LP as ratio bound / Lovasz theta) — LP value as a bound on the
    independence number of a scheme-aligned graph.
  - MDPI 2021 (Generalized information-theoretic bound, Entropy 23:270) — for
    the independence-number frame of the ratio bound.
  No source found applying the Delsarte LP to the max-internal-degree quantity
  D(S)=f(n); all of it bounds codes/min-distance or independence number, both
  distance-average-type quantities.
verified-at: n=4 exact witness (4 even + 5 odd, not parity+one) bounds nothing
  here, but the two structural arguments above are settled by hand from the
  verified matrices and exact values.

first-step: Build the Hamming-scheme LP with variables a_0..a_n, constraints
a_0 = 1, a_i ≥ 0, Σ a_i = 2^{n-1}+1, and the MacWilliams nonnegativity K·a ≥ 0;
minimise a_1 for n = 1..5 and compare the implied lower bound on max degree to
f(1..5) = (1,2,2,2,3). If the LP value undershoots f(n) at some n ≤ 5, record
the exact gap; if it matches, extract the dual witness and push to larger n.
```
