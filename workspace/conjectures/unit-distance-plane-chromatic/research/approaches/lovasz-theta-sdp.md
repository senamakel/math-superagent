# Lovasz theta / vector chromatic number as an exact lower-bound certificate

```approach
idea: Use the Lovasz theta SDP hierarchy as a polynomial-time lower-bound
oracle for finite unit-distance graphs. theta(G) >= alpha(G), hence
chi(G) >= n/theta(G); Schrijver's theta' and theta-bar sharpen this, and for a
vertex-transitive graph all of these collapse to closed-form character/eigenvalue
expressions. A finite unit-distance graph with theta-bar(G) <= n/5 is a
certificate that chi(G) >= 5, obtained by an SDP (not by SAT), and theta-bar
also gives the vector chromatic number chi_v(G) which interpolates
chi_f(G) <= chi_v(G) <= chi(G). For Cayley graphs — exactly the dense,
vertex-transitive unit-distance families — theta is a function of the connection
set's Fourier transform, computable symbolically over the coordinate field, with
no floating point. This turns "is there a 5-chromatic unit-distance graph" into
"is there a finite point set whose exact theta-bar drops to n/5", screened in
polynomial time before the complete SAT oracle is invoked on survivors.
mechanism: Colouring is reformulated as an orthogonal-representation / PSD
constraint: a k-colouring is equivalent to assigning each vertex a vector with
pairwise inner products avoiding a forbidden value, and the Lovasz theta of the
complement captures the best such representation. For a Cayley graph of a finite
abelian group the adjacency matrix is diagonalised by characters, so theta and
the Hoffman bound alpha(G) <= n*(-lambda_min)/(lambda_max - lambda_min) are
exact algebraic expressions in character sums of the connection set. These sums
can be evaluated exactly over Q(sqrt d, sqrt 11, ...) or cyclotomic fields. A
graph passing the theta-bar >= ... threshold is handed to the complete colouring
test, so the SDP is a cheap necessary-condition filter, never a substitute for
the witness.
status: proposed
first-step: Implement an exact eigenvalue/Hoffman bound for the calibrated
7-vertex spindle and the Minkowski-power family already computed by the run, and
check it reproduces chi >= 4 on the spindle and stays strictly below 5 on the
known 4-chromatic dense family (confirming it does not hallucinate 5). Then apply
the same exact character-theoretic bound to finite root-of-unity Cayley graphs,
and pass only the theta-promising ones to the SAT oracle.
```

## Established vs speculation

- **Established (standard):** `theta(G) >= alpha(G)` so `chi(G) >= n/theta(G)`;
  for regular/vertex-transitive graphs the Hoffman eigenvalue bound and the
  theta number have exact character-theoretic form; Schrijver's refinement
  `theta-bar <= theta` is a sharper independence bound. These are classical
  (Lovasz 1979, Schrijver 1979) — research should pin the exact statements and
  which variant gives the tightest `n/· >= 5` threshold.
- **Speculation:** that some structured unit-distance family attains
  `theta-bar <= n/5`. The theta bound is *weaker* than chi, so it can only
  prove `chi >= 5` when it actually reaches 5; if the dense families stay below
  5 in theta, the tool still serves as a screening filter and as a new invariant
  to classify the constructions, not as the final proof.
- **Not the measurable variant:** theta/chi_v lower-bounds plain chi, so this is
  not importing the measurable-chromatic lower bound; it is an exact finite-graph
  certificate route.
