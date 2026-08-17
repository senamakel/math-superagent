# Approach: exact general-k pair-correlation matrix, depart-from-Toeplitz boundary term

```approach
idea: Ψ(k) = Σ_{i,j} C(i,j) 10^{2k-2-i-j} with C(i,j) = #{length-k factors w
      with w_i = w_j = 1} (the factor pair-correlation matrix). This
      quadratic-form identity is known, but the run's directive-1 route used it
      only at k = F_n − 1, where C is translation-invariant (a function of
      i−j) and collapses. At general k the invariance FAILS (verified by the
      pattern hunt). The genuinely different idea is to make that failure the
      object: by Sturmian balance, C(i,j) differs from a Toeplitz profile by
      at most a small explicitly-computable boundary/rank perturbation, so
      Ψ(k) = (Toeplitz part, a few geometric sums) + (exact low-rank
      correction). Attack the matrix itself rather than the floor-sum.

mechanism: A Sturmian word is "balanced": the number of 1s in any two windows
      of equal length differs by at most 1. This forces C(i,j) to be a
      2-Lipschitz, level-set-bounded function of (i,j); its deviation from
      translation invariance lives on the boundary of the k×k window and can
      be parametrised by the Bezout/three-distance pattern of the rational
      slope a = F(n−2)/F(n). If the correction term is rank-≤2 of closed form,
      Ψ(k) becomes a sum of a Toeplitz second moment plus a handful of
      geometric double-sums — O(log k) with no universal-Euclidean monoid.

status: refuted

killed-by: Not independent and its decisive payoff is unsupported. The
      general-k residual R(i,j)=C(i,j)-T(|i-j|) is NOT a low-rank boundary
      term the literature backs — the thread's own general-k account
      (dir1-domain-autocorrelation) gives C(j,j+d) as a lattice-point count in
      an arc whose length depends on d alone, i.e. exactly the floor-sum
      primitive the committed universal-Euclidean route already evaluates. So
      the approach closes to the same OCTA floor-sum rather than bypassing it,
      and its one distinct claim (low-rank Toeplitz correction with no
      Euclidean machinery) has no source and is the same hard gap the run
      already measured. Rejected as the primary route; its Toeplitz profile is
      valid only at k=F_n-1, where the run's directive-1 collapse already
      handles it.

mechanism-checked: The three ingredients are established.
      (i) The quadratic-form identity Ψ(k)=Σ_{i,j}C(i,j)10^{2k-2-i-j} is exact
      and the run's brute oracle confirms it.
      (ii) At k=F_n−1 the k+1 factors are the F_n rotations of the standard
      word q_n truncated to k letters, so C is translation-invariant and
      collapses to the cyclic autocorrelation A(d)=max(0,m−t)+max(0,m−(N−t)),
      N=F_n, m=#ones in q_n, t=(d·m) mod N — the run's directive-1 claim,
      verified for n=3..12. So at exactly those k the Toeplitz profile is
      explicit and exact.
      (iii) Sturmian = balanced (Perrin-Restivo, TCS 2011) forces C(i,j) to
      be 2-Lipschitz: two equal-length windows differ by ≤1 in ones, so the
      pairwise-correlation counts differ by O(1). This is what caps the
      departure from Toeplitz.

residual-open: What the literature does NOT give is a published closed form for
      the general-k residual R(i,j)=C(i,j)−T(|i−j|) as an explicit boundary
      term in (i,j) from the three-distance structure. That formula is the
      missing piece the run would have to establish itself; it is the same
      hard gap the run already measured (translation invariance failing away
      from k=F_n−1). The three-distance theorem (below) gives the exact gap
      lengths/counts of the representative set, which is the natural ingredient
      for such a boundary parametrisation, but the transfer from "at most 3 gap
      lengths" to "rank-≤2 deviation of C from Toeplitz" is NOT in any source
      found and should be treated as conjecture until the run computes R for
      k=1..60 and matches brute Ψ.

precedent:
      - Perrin & Restivo, "A note on Sturmian words", TCS 2011,
        doi:10.1016/j.tcs.2011.12.047 — Sturmian = balanced; factor structure.
      - Three Distance / Gap Theorem (Sós): van Ravenstein, "The Three Gap
        Theorem (Steinhaus Conjecture)", J. Austral. Math. Soc. A 45 (1988);
        Weiß, "Deducing Three Gap Theorem from Rauzy-Veech induction",
        arXiv:1807.11273 (exact gap lengths L1,L2,L3 and counts N1,N2,N3 in
        terms of Ostrowski data of α).
      - The Toeplitz-collapse at k=F_n−1 is the run's own verified directive-1
        claim (A(d) listed above), cross-checked against brute for n=3..12.

first-step: For k = 1..60 compute C(i,j) exactly (three independent ways:
      direct factor enumeration, mechanical/residue model, and the cyclic-
      autocorrelation formula restricted to k=F_n−1). Subtract the best
      Toeplitz fit (cyclic-autocorrelation at the nearest F_n−1 or the
      empirical function of i−j) and study the residual R(i,j)
      = C(i,j) − T(|i−j|): measure its rank/bandwidth and whether it takes
      the closed form of a boundary term in (i,j) from the three-distance
      structure. Reproduce every brute Ψ(k) from the decomposition before
      going to 10^18. The open question is exactly whether R is low-rank /
      boundary-local — that is what would make the approach pay off.
```

## Assessment for the run

The mechanism is fully **grounded** in the literature and the run's own
verified work, but the decisive new claim — that the general-`k` residual
`R = C − Toeplitz` is low-rank/closed-form — is **not** in any source found.
This is the honest state: the approach is a well-founded conjecture whose payoff
hinges on a formula the run itself must establish (or fail to establish). It is
worth an experiment, and it is the only one of the three that directly targets
the translation-invariance failure the run already measured.
