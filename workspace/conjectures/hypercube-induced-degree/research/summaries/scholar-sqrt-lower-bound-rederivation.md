# Scholar note — the sqrt(n) lower bound is re-derivable by elementary linear algebra

**Result: for every n >= 1, f(n) >= sqrt(n).** This is the missing lower bound
that closes problem.md's `log n`–`sqrt(n)` gap from below. It was re-derived
here by hand (elementary block-matrix algebra + Cauchy interlacing + a
quadratic-form spectral bound), independent of the withheld primary source.
It agrees with the recalled Huang theorem and with the exact small-n oracle
values f(1..4) = 1,2,2,2 = ceil(sqrt(n)).

## The mechanism (all three steps verified by hand below)

The quantity that produces a *maximum* — answering problem.md's challenge — is
the largest eigenvalue of a signed adjacency matrix of the cube. The `sqrt(n)`
comes from the quadratic relation `A_n^2 = n·I`.

```claim
id: huang-signed-adjacency
statement: For each n >= 1 there is a symmetric 2^n x 2^n matrix A_n over {0,±1}
  whose support is exactly the edges of Q_n and which satisfies A_n^2 = n·I.
  Hence its spectrum is +sqrt(n) and -sqrt(n), each with multiplicity 2^{n-1}.
hypotheses: none beyond the recursion A_1=[[0,1],[1,0]], A_{n+1}=[[A_n,I],[I,-A_n]].
holds-here: yes
status: verified (hand derivation; elementary block-matrix algebra)
bearing: the entire max-degree lower bound rests on this identity; it is where
  the sqrt(n) comes from (quadratic relation), exactly as problem.md predicted.
falsifies: a machine check of A_n^2 = n·I failing at any n would refute it;
  that check is queued in code/out/scholar_verify_huang.py.
anchor: research/backward/spectral-interlacing-sqrt-lower-bound.md
```

Hand verification: block-multiply
```
A_{n+1}^2 = [[A_n, I],[I,-A_n]]^2
         = [[A_n^2+I^2, A_n I + I(-A_n)], [I A_n + (-A_n)I, I^2 + A_n^2]]
         = [[A_n^2+I, 0],[0, A_n^2+I]]
```
With A_n^2 = n·I this is (n+1)·I, so by induction A_n^2 = n·I. Diagonal zero
(A_n and I have zero diagonal), symmetric. Support: A_n on within-copy edges,
±I on cross-coordinate edges = all edges of Q_{n+1}. Since tr A_n = 0 and
A_n^2 = n·I, the 2^n eigenvalues are ±sqrt(n) in equal number. Verified.

```claim
id: interlacing-sqrt
statement: Let B be a principal submatrix of A_n on k = 2^{n-1}+1 rows. Then
  lambda_max(B) >= sqrt(n).
hypotheses: A_n is symmetric with eigenvalues ±sqrt(n) each of multiplicity 2^{n-1};
  Cauchy interlacing for principal submatrices.
holds-here: yes
status: verified (Cauchy interlacing)
bearing: forces a large eigenvalue (a maximum quantity) out of a mere >half-size
  set; this is the step that makes the max-degree bound independent of how S is
  chosen.
falsifies: interlacing instantiation wrong (m-k+1 = 2^{n-1} is the eigenvalue
  sqrt(n)); machine check in scholar_verify_huang.py.
anchor: research/backward/spectral-interlacing-sqrt-lower-bound.md
```

Hand verification: interlacing gives mu_1 >= lambda_{m-k+1} with m=2^n,
m-k+1 = 2^n - 2^{n-1} = 2^{n-1}, whose eigenvalue of A_n is sqrt(n). Verified.

```claim
id: lambda-max-bounded-by-degree
statement: Let H be a finite graph, B a real symmetric matrix with zero diagonal,
  entries in {0,±1} supported on edges of H. Then lambda_max(B) <= Delta(H),
  the maximum degree of H.
hypotheses: B[uv]!=0 only when uv in E(H).
holds-here: yes
status: verified (quadratic-form bound, shown below)
bearing: once lambda_max(B) >= sqrt(n), this is what turns it into
  Delta(Q_n[S]) >= sqrt(n), i.e. a bound on D(S) itself.
falsifies: none found; small machine check in scholar_verify_huang.py.
anchor: research/backward/spectral-interlacing-sqrt-lower-bound.md
```

Hand verification: x^T B x = 2 Σ_uv B_uv x_u x_v <= 2 Σ_uv |x_u x_v|
<= Σ_uv (x_u^2 + x_v^2) = Σ_v deg_H(v) x_v^2 <= Delta(H) ||x||^2. Since
lambda_max(B) = max_{||x||=1} x^T B x, done. Verified.

```claim
id: f-lower-bound-sqrt-n
answers: exact-statement-huang-932b
statement: f(n) = min{ D(S) : S ⊆ Q_n, |S|=2^{n-1}+1 } >= sqrt(n) for all n.
hypotheses: the three lemmas above.
holds-here: yes
status: derived (re-derivation of Huang's lower bound by hand); machine
  confirmation and the matching upper-bound construction remain open.
bearing: closes problem.md from below. f(n) is an integer, so in fact
  f(n) >= ceil(sqrt(n)); consistent with f(1..4)=1,2,2,2.
falsifies: an S of size 2^{n-1}+1 with D(S) < sqrt(n) would refute it; the
  machine interlacing check in scholar_verify_huang.py is the first line of attack.
anchor: research/backward/spectral-interlacing-sqrt-lower-bound.md
```

## What this does and does not settle

- **Settled (by hand, re-derived):** the missing `sqrt(n)` LOWER bound. This is
  a genuine partial result stated exactly: `f(n) >= sqrt(n)` for every n, with
  a fully checkable mechanism.
- **Not settled:** the matching UPPER bound construction `f(n) <= sqrt(n)`
  (problem.md cites it; the source is withheld; the construction must be rebuilt
  to certify exact equality). Until then the exact statement is
  `sqrt(n) <= f(n) <= (upper construction)`.
- **Contradiction / resolution:** the recalled memory held Huang's theorem as
  "recalled, not verified." My hand-derivation of the lower-bound mechanism
  independently confirms it from first principles. This is the most valuable
  find: the "thirty-year gap" is closed from below by an elementary argument.

## Note for coder

`code/out/scholar_verify_huang.py` (written by this scholar) independently
machine-checks all three lemmas exactly (integer `A_n^2 = n·I`, exact spectra,
interlacing on random submatrices, edge-support) for n=1..7. This scholar has
no execution tool; that check is queued for the school that can run it. The
hand derivation above does not depend on it, but running it is cheap insurance
against a hand-algebra slip.
