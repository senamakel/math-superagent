# Huang spectral lower bound — mechanically verified

```claim
id: huang-signature-matrix-square
statement: The signed adjacency matrix A_n defined by A_1 = [[0,1],[1,0]] and
  A_n = [[A_{n-1}, I_{2^{n-1}}], [I_{2^{n-1}}, -A_{n-1}]] satisfies A_n^2 = n·I_{2^n},
  has zero diagonal, and its support is exactly the edge set of Q_n. Hence its
  spectrum is +sqrt(n) and -sqrt(n), each with multiplicity 2^{n-1}.
hypotheses: n >= 1; recursion as stated.
holds-here: yes
status: checked
evidence: exact sympy Integer arithmetic, n=1..8: A_n^2==n*I, zero diagonal,
  support==edges(Q_n) all True (through 256x256). Exact eigenvals n=2..7 give
  exactly ±sqrt(n) each mult 2^{n-1}; numeric n=8..10 reproduce (n=10: 512 of
  each sign, 0 others). Anchor: code/out/huang_spectral.captured.txt Parts 1-2.
anchor: code/out/huang_spectral.captured.txt
```

```claim
id: huang-interlacing-sqrt
statement: For every S ⊆ V(Q_n) with |S| = 2^{n-1}+1, the principal submatrix
  B = A_n[S,S] has λ_max(B) >= sqrt(n). (Instance of Cauchy interlacing for a
  matrix whose spectrum is ±sqrt(n) each with mult 2^{n-1}.)
hypotheses: A_n as in huang-signature-matrix-square; |S| = 2^{n-1}+1.
holds-here: yes
status: checked
evidence: verified over EVERY admissible S for n=1..4 (1, 4, 56, 11440 sets),
  and 5 random sets per n for n=5..10 — λ_max >= sqrt(n) in every trial, always
  tight at sqrt(n). Anchor: f_exact_verify.captured.txt Part 2, huang_spectral.captured.txt Part 3.
anchor: code/out/f_exact_verify.captured.txt
```

```claim
id: huang-degree-bounds-lambda
statement: Let H be a finite graph on vertex set S with max degree Δ(H), and B
  a real symmetric matrix with entries in {0,±1}, zero diagonal, nonzero only on
  edges of H. Then λ_max(B) <= Δ(H). Proof: for unit x, x^T B x = Σ_{uv} 2B_uv x_u x_v
  <= Σ_{uv}(x_u^2+x_v^2) = Σ_v deg(v)·x_v^2 <= Δ(H)||x||^2, then Rayleigh-Ritz.
hypotheses: H finite simple graph; B zero-diagonal {0,±1} supported on E(H).
holds-here: yes
status: checked
evidence: λ_max(A_n[S,S]) <= Δ(Q_n[S]) in every trial, all admissible S for
  n=1..4 and random S for n=5..10. Anchor: f_exact_verify.captured.txt Part 2,
  huang_spectral.captured.txt Part 4.
anchor: code/out/huang_spectral.captured.txt
```

## Synthesis

```claim
id: huang-f-n-sqrt-n
statement: f(n) = min{ D(S) : S ⊆ V(Q_n), |S| = 2^{n-1}+1 } satisfies
  f(n) >= sqrt(n) for every n >= 1; hence f(n) = Θ(sqrt(n)) against the known
  upper construction f(n) <= sqrt(n), and in particular f(n) = ω(log n).
hypotheses: none beyond huang-signature-matrix-square, huang-interlacing-sqrt,
  huang-degree-bounds-lambda.
holds-here: yes (this is the goal)
status: proved, verified numerically on small cases
evidence: For arbitrary S with |S|=2^{n-1}+1, D(S)=Δ(Q_n[S]) >= λ_max(A_n[S,S])
  >= sqrt(n). Verified against exact f(1..4)=1,2,2,2 (all >= sqrt(n); equality
  at n=1,4). This reproduces Hao Huang (Annals of Math 190 (2019)) — the source
  was withheld here, so the derivation stands on this run's own computation.
anchor: code/out/f_exact_verify.captured.txt, code/out/huang_spectral.captured.txt
```

## Evidence classes
- huang-signature-matrix-square: **exact** (sympy Integer arithmetic).
- huang-interlacing-sqrt: verified numerically over all small cases; rests on
  proved Cauchy interlacing theorem.
- huang-degree-bounds-lambda: proved (quadratic form + Rayleigh-Ritz); verified
  numerically.
- huang-f-n-sqrt-n: follows by the chain given; numerically consistent with all
  exact f(1..4).
