# Thread: sqrt(n) lower bound via signed adjacency / spectral interlacing

```thread
question: Is f(n) >= sqrt(n) for every n? (closes problem.md's log–sqrt gap from below)
status: PROVED — mechanism hand-derived and machine-verified (exact A_n^2=nI n<=8;
  interlacing + degree-bound proved and spot-checked n<=10; consistent with exact
  f(1..5)=1,2,2,2,3=ceil(sqrt(n))).
rests-on: huang-signature-matrix-square, huang-interlacing-sqrt,
  huang-degree-bounds-lambda, hypercube-adjacency-spectrum-cayley (base spectrum)
blocked-by: none for the LOWER bound. The matching UPPER construction
  (f(n) <= ceil(sqrt(n))) is still open — its source is withheld and the
  construction must be rebuilt to certify exact equality f(n)=ceil(sqrt(n)).
next: rebuild the sqrt(n)/ceil(n^(1/2)) upper construction and measure its D(S)
  directly; then read the exact-value conclusion f(n)=ceil(sqrt(n)) off the
  matched pair. The Clifford/Dirac approach (approaches/clifford-dirac-fermionic.md)
  is the one live route that would overshoot the asymptotic Theta(sqrt(n)) to a
  speculated exact value.
```

The mechanism (hand derivation + captured-output verification):

1. **Signed adjacency:** A_1=[[0,1],[1,0]], A_{n+1}=[[A_n,I],[I,-A_n]].
   Block multiplication gives A_{n+1}^2 = [[A_n^2+I,0],[0,A_n^2+I]], so by
   induction A_n^2 = n·I. Zero diagonal, symmetric, support = edges of Q_n.
   Hence eigenvalues ±sqrt(n) each × 2^{n-1}. **Exact-verified** n=1..8
   (huang_spectral.captured.txt Parts 1–2); spectrum ±√n n<=7 exact, n=8..10
   numeric.
2. **Interlacing:** Cauchy interlacing on the (2^{n-1}+1)-row principal submatrix
   forces λ_max(A_n[S,S]) >= sqrt(n) (the (2^{n-1})-th eigenvalue of A_n).
   Spot-checked worst-case λ_max=√n n=2..10.
3. **Spectral bound:** for a {0,±1} matrix supported on edges,
   λ_max <= Δ(H) (quadratic form <= sum deg·x^2 <= Δ||x||^2). Proved, spot-checked.
4. **Base spectrum** (Liu–Zhou): unsigned adjacency of Q_d has eigenvalues d−2i,
   mult C(d,i); the √n above comes from the signed matrix's A_n²=nI, not from the
   plain adjacency (whose top eigenvalue is d). Confirms the sign-colouring story.

Conclusion: every admissible S has D(S) >= sqrt(n), i.e. f(n) >= sqrt(n) for all
n. This re-derives Huang's theorem from first principles against the withheld
source, closing the "thirty-year gap" from below and making the deliverable the
exact bound stated cleanly plus the upper construction to certify equality.
