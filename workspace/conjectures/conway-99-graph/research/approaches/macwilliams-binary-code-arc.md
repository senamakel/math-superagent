# Approach: MacWilliams identities over a binary code from the adjacency matrix

```approach
idea: Lift a putative srg(99,14,1,2) to a binary linear code C over F_2 (span of rows of A+I or of a related matrix), and use the MacWilliams identities / Delsarte bounds to force the full weight enumerator from the parameters.
mechanism: Every srg(v,k,1,2) has A+I of full rank over Q in one eigenspace; the row span over F_2 is a binary code. Delsarte (1973) shows a two-weight projective code's weights are determined by the SRG parameters; for lambda=1,mu=2 the two weights are 8 and 11. The MacWilliams identities pin the complete weight distribution, and — the new object — the *binary* (char-2) self-orthogonality conditions differ from the spectral conditions, so this attacks a quantity the spectral route does not. The catch (must fail on controls): 9 and 243 satisfy the same equations, so the argument must exploit a *char-2* feature (e.g. rank of A over F_2) that distinguishes the three.
precedent:
  - Delsarte, "Weights of linear codes and strongly regular normed spaces", Discrete Math. 3 (1972) 47-64: the equivalence (i) two-weight projective codes (ii) SRGs from difference sets (iii) subsets of projective space with two-valued hyperplane intersections. THIS is the named theorem the reformulation rests on.
  - Haemers, Peeters, van Rijckevorsel, "Binary Codes of Strongly Regular Graphs" (1998): the dimension (p-rank) is often but not always determined by parameters; two-graph codes unify SRG codes under Seidel switching; a two-graph code is 2-weight.
  - Makhnev 1988 (in library, research/sources/makhnev-1988-lambda1.full.md) is the mu=2 context but does not go through the code.
  - The run's own claim c4 (9 and 243 exist) and c1 (family list) are the controls any such argument must fail on.
status: refuted
killed-by: The two-weight/MacWilliams set-up is parameter-driven, and there is no published or derivable fraction that separates (99,14,1,2) from (9,4,1,2) and (243,22,1,2). The row span over F_2 of A+I is a binary two-weight code whose weight enumerator is fixed by the parameters alone (Delsarte 1972/Haemers-Peeters-van Rijckevorsel 1998), so the MacWilliams identities cannot carry an invariant that distinguishes 99 from 9 and 243. Moreover the proposed char-2 feature (rank_2 of A or A+I) is not a "new quantity the spectral route never sees" for an existence purpose: p-ranks (Peeters 2002) are "relevant" — i.e. not spectrum-determined — only as a way to tell apart graphswhen a cospectral family exists, and here there is no cospectral pair to distinguish, so a p-rank gives no existence obstruction. No source applies this route to (99,14,1,2), and the honest reason is that the controls satisfy every equation, so it does not even offer a search boundary.
first-step: (Still worth doing cheaply for the record, not as the argument.) Compute rank_2(A+I) and the weight enumerator for rook(3) and bvls_graph() over F_2 in sympy, and confirm both are two-weight codes with the Delsarte-pinned weights; record that the same then holds a fortiori for any 99. This is the check that makes the refutation evidence-based rather than by absence.
```

Refuted on evidence: the Delsarte two-weight equivalence means the weight
enumerator/self-orthogonality is fixed by the parameters, so it cannot split 99
from the two existing members of the family. The proposed char-2 lever (p-rank) is
a distinguishing tool for cospectral pairs, and no cospectral pair is at issue
here — the run is deciding existence, not distinguishing isomorphs.
