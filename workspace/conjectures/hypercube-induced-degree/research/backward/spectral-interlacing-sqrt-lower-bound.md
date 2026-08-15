# Skeleton — sqrt(n) lower bound via the signed adjacency matrix and spectral interlacing

This decomposition attacks the *strong* target `f(n) >= sqrt(n)`, which closes
the `log n`–`sqrt(n)` gap from below and subsumes the run's primary target
`f(n) = omega(log n)`. It answers the obstruction in `problem.md` directly: the
quantity that produces the maximum is the largest eigenvalue of a signed
adjacency matrix — a *maximum over unit vectors by construction*, not an
average, and it carries a `sqrt` because the matrix satisfies `A_n^2 = n·I`.

```skeleton
goal: For every n >= 1, f(n) >= sqrt(n), where f(n) = min{ D(S) : S ⊆ V(Q_n), |S| = 2^{n-1}+1 } and D(S) is the maximum internal degree of the induced subgraph Q_n[S].
implies: Fix any n and any S with |S| = 2^{n-1}+1, and let H = Q_n[S]. By G-signed-adjacency-matrix there is a symmetric matrix A_n indexed by V(Q_n) with entries in {0,±1}, support exactly the edges of Q_n, and A_n^2 = n·I_{2^n}; its diagonal is zero, so its spectrum is +sqrt(n) and −sqrt(n), each with multiplicity 2^{n-1}. Let B = A_n[S,S] be the principal submatrix on S; it has 2^{n-1}+1 rows. By G-interlacing-sqrt, λ_max(B) >= sqrt(n). The support of B is exactly the edge set of H and its nonzero entries are ±1, so by G-eigenvalue-bounds-degree, Δ(H) >= λ_max(B) >= sqrt(n). Since D(S) = Δ(H) and S was arbitrary, every admissible S has D(S) >= sqrt(n); taking the minimum over S gives f(n) >= sqrt(n), hence in particular f(n) = omega(log n).
status: sketched
rests-on: none — research/CLAIMS.md records no claims yet; all three lemmas below are open gaps
```

```gap
id: G-signed-adjacency-matrix
lemma: For each n >= 1 there is a symmetric 2^n × 2^n matrix A_n over {0,±1} whose support is the edge set of Q_n (A_n[u,v] = 0 unless u and v differ in exactly one coordinate) and which satisfies A_n^2 = n·I_{2^n}. Equivalently, A_n is a signed adjacency matrix of Q_n whose eigenvalues are ±sqrt(n), each with multiplicity 2^{n-1}.
status: open
next: Define A_1 = [[0,1],[1,0]] and recursively A_n = [[A_{n-1}, I_{2^{n-1}}], [I_{2^{n-1}}, −A_{n-1}]]. Verify A_n^2 = n·I with exact sympy arithmetic for n = 1..8, and hand-check n = 2 against the cube's actual edges. Then prove the square identity and the zero diagonal algebraically from the recursion (theorem_prover / lean_prover).
```

```gap
id: G-interlacing-sqrt
lemma: Let B be any principal submatrix of A_n on 2^{n-1}+1 rows. Then λ_max(B) >= sqrt(n). This is the instance of Cauchy's interlacing theorem for A_n: its spectrum is ±sqrt(n), each with multiplicity 2^{n-1}, so its (2^{n-1})-th largest eigenvalue equals sqrt(n), and interlacing forces the top eigenvalue of B to be at least that.
status: open
next: State and prove Cauchy's interlacing theorem for principal submatrices of real symmetric matrices (theorem_prover; or lean_prover against Mathlib's interlacing statement if one exists). Instantiate at m = 2^n, k = 2^{n-1}+1, where the (m−k+1)-th largest eigenvalue of A_n is exactly the (2^{n-1})-th, i.e. sqrt(n). Sanity-check numerically: for n = 2..10 compute λ_max of random principal (2^{n-1}+1)-submatrices of A_n and confirm each is >= sqrt(n).
```

```gap
id: G-eigenvalue-bounds-degree
lemma: Let H be a finite simple graph on vertex set S with maximum degree Δ(H), and let B be a real symmetric matrix with B[u,v] ∈ {0,±1} and B[u,v] ≠ 0 only when uv is an edge of H (so B has zero diagonal). Then λ_max(B) <= Δ(H).
status: open
next: Prove by the quadratic-form bound: for any unit vector x, x^T B x = Σ_{uv∈E(H)} 2·B[u,v]·x_u·x_v <= Σ_{uv∈E(H)} (x_u² + x_v²) = Σ_v deg_H(v)·x_v² <= Δ(H)·||x||², then conclude via the Rayleigh–Ritz characterisation λ_max(B) = max_{||x||=1} x^T B x. Hand this to theorem_prover / lean_prover today; it is the only lemma of the three that is standard graph-spectral folklore rather than bespoke.
```
