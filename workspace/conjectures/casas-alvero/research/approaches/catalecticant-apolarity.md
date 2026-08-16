# Approach: catalecticant apolarity (refuted)

Proposed: translate CA into the language of binary-form apolarity / catalecticant
matrices, where pure powers are exactly the rank-1 catalecticant locus (the
rational normal curve). Refuted at convergence.

```approach
idea: Apolarity/catalecticant reformulation: f = Σ a_i x^i is a pure power iff
      every catalecticant Catal_k(f) has rank 1 (Macaulay / Iarrobino–Kanev).
      CA ⟺ the derivative-sharing resultants cut out this rank-1 locus, so the
      n−1 conditions Res(f, H_i f) = 0 should be determinantal identities on the
      catalecticant.
mechanism: The Hasse derivative H_i(f) is obtained from f by apolarity with x^i,
      so the derivative tower is a slice of the same dual-pairing data as the
      catalecticants; the resultants were conjectured to be combinations of
      catalecticant/Hankel minors, turning CA into "n−1 slice-determinants cut
      the rational normal curve out of their common zero locus".
status: refuted
killed-by: The load-bearing bridge is unsupported and contradicted by the known
      structure of apolar ideals. The rank-1-catalecticant ⟺ pure-power
      equivalence is classical and true, but it does NOT factor the n−1
      resultant conditions: for a generic binary form the apolar ideal f^⊥ is
      generated in two degrees g, g′ with g + g′ = n + 2 and gcd(g,g′) = 1
      (Brambilla–Staglianò 2018, "On the algebraic boundaries among typical
      ranks for real binary forms", held in search; the genericity pattern is
      the standard apolarity fact), so the derivative resultants are not minors
      of a single catalecticant. The claimed identity
      Res(f, H_i f) = "combination of catalecticant minors" was the proposal's
      own conjecture (marked _unchecked_) and no source or computation supports
      it. The true reformulation that does factor the derivative conditions per
      root is the elementary-symmetric root-difference identity, adopted as
      root-difference-coloring — which makes Ghosh's σ_i explicit — so this
      representation change buys the target ideal only through that identity,
      not through the null cone.
first-step: superseded — see research/approaches/root-difference-coloring.md.
precedent: none found (apolarity appears in Polstra 2012 only as a hint for
      future work; Lu 2017 uses regular sequences, not catalecticants).
speculative: the "resultants = catalecticant minors" bridge, now refuted.
```
