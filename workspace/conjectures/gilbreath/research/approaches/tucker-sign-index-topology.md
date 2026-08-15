```approach
idea: Read the SIGNED forward-difference triangle (without absolute values) as a discrete height function on the half-line and use the Morse/Poincaré–Hopf index theorem for sign changes — a discrete combinatorial-topology constraint (in the spirit of Tucker's lemma and Sperner's lemma on the sign pattern) to certify that the left edge A_k(1) cannot leave {0,2}.
mechanism: |
  Split the Gilbreath cell map at its nonlinearity:
      A_{k+1}(i) = |A_k(i) - A_k(i+1)| = sigma_{k,i} * (A_k(i) - A_k(i+1)),
  where sigma_{k,i} = +1 or -1 records which of the two parents is larger
  (the "min branch" when the sign flips). The SIGNED difference sequence
  D_k(i) = sum_j (-1)^{k-j} C(k,j) A_0(i+j) satisfies D_{k+1} = D_k(i) - D_k(i+1)
  exactly (d^2 = 0), and A_k(i) = |D_k(i)| differs from |D_k(i)|... no:
  A_k(i) equals |D_k(i)| exactly when the sign pattern of D is coherent
  (all min-branch choices line up). The sign word sigma_k = (sigma_{k,0}, sigma_{k,1}, ...)
  is the object that carries ALL of the nonlinearity.

  A classical fact: for a sequence x_0, x_1, ..., the number of sign changes
  of its forward difference is the number of local extrema of x, and the
  "index" sum_{i} [sign change of D_k at i] is constrained by the endpoints.
  In the smooth world this is Poincaré–Hopf: the Morse index of the height
  function x equals the Euler characteristic of the domain (here: the ray,
  chi = 1). The discrete analogue is a Sperner/Tucker-type parity lemma: a
  sign word on a 1-complex whose boundary values are fixed must contain a
  certain number of "labelled" adjacent pairs. The conjecture A_k(1) in {0,2}
  is, in this language, a statement about the sign word sigma_k AT the left
  boundary — and the topological constraint may force exactly the boundary
  sign that keeps A_{k+1}(1) in {0,2} whenever the interior sign pattern is
  non-degenerate (a "no flat all-same-sign tail" hypothesis, i.e. a
  prime-free non-periodicity condition).

  Named mathematics: the discrete Morse theory of Forman (1998), the
  Poincaré–Hopf index theorem for discrete height functions, Tucker's lemma
  and the octahedral Tucker lemma (Matoušek, "Using the Borsuk–Ulam
  theorem"), and the sign-change index of one-dimensional maps. This is a
  genuinely different axis from everything on disk: none of the refuted
  approaches used the SIGN WORD of the nonlinearity as a topological
  object — comparison-order-CA was refuted for scale-invariance (it threw
  away magnitude), but this keeps magnitude via the signed difference and
  keeps only the sign of the COMPARISON between consecutive signed entries,
  which is scale-covariant in a controlled way.
status: refuted
killed-by: |
  Two independent groundings. (1) The load-bearing dictionary is FALSE and
  held already by the run: claim fwd-diff-identity-refuted — the Gilbreath
  entry A_k(i) is NOT |Delta_k(i)| (the absolute value of the signed forward
  difference), first violation at (k,i)=(3,2), inside the leading {0,2}
  block; first violation at position 1 is k=4 (|Delta_4(1)|=6, A_4(1)=2);
  17 of the first 20 rows fail. So the sign word of the SIGNED triangle
  Delta_k does not determine A_k(1)'s value at all: the sign of Sigma_k at
  the boundary has no fixed correspondence to whether A_{k+1}(1) is in
  {0,2}. The candidate's own mechanism admits this ("A_k(i) equals |D_k(i)|
  exactly when the sign pattern is coherent"), and the run has shown that
  coherence fails immediately — so the topological object whose boundary
  sign is to be forced (the sign of Delta_k) is not the object that governs
  A_k(1). (2) Even where the dictionary held, the index theorems named do
  not give a boundary constraint. Forman's discrete Morse theorem, the
  Poincaré–Hopf index theorem, and Tucker's lemma (incl. the combinatorial
  Zp-Tucker of Mukherjee–Pramanik 2025, arXiv:2511.10319) all constrain the
  TOTAL number of critical cells / sign changes — a global Euler-
  characteristic / degree / parity count — never the VALUE at a single
  specified cell. The index theorem fixes the total number of sign changes,
  not their location, which is precisely the "boundary sign free"
  obstruction the candidate flagged as its first-step falsifier.
precedent: |
  Discrete Morse theory: Forman 1998/2002 (Trans. AMS, doi 10.1090/S0002-9947-02-03041-6), Kozlov "Organized Collapse"; combinatorial degree/Tucker: Mukherjee–Pramanik 2025 (arXiv:2511.10319, combinatorial Zp-Tucker via discrete Morse). None applies any of this to Gilbreath or to iterated absolute differences. The run's own held claim fwd-diff-identity-refuted (research/notes/check_fwd_diff_identity.notes.md) and the prior approach gantmacher-krein-oscillatory-matrix-sign-regularity (refuted: the alternating Pascal matrix is not sign-regular, and the identity A_k=|Delta_k| fails at (3,2)) document the death of the signed-forward-difference line before any topology is invoked.
```

**Grounding note (research, this cycle).** Refuted on the run's own proved falsifier, which is decisive. The inventor's first-step falsifier ("if the boundary sign is free, this dies") is satisfied: the signed-forward-difference linearization is dead at (3,2) — claimed `fwd-diff-identity-refuted` — so the sign word of Δ_k is already disconnected from A_k(1) before the topological index is ever applied. And the index theorems themselves (Forman discrete Morse, Poincaré–Hopf, Tucker/octahedral-Tucker, Zp-Tucker) are global counting statements; none returns a boundary value. This closes the topological sign-index line: it is not a missing-application gap but a false premise plus a wrong type of conclusion.
