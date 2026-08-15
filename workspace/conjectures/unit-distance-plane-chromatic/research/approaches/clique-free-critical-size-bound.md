# Clique-free critical graphs — a sharper edge lower bound for the size-bound theorem

```approach
idea: Prove a lower bound on the number of vertices of any 5-chromatic unit-distance graph by combining the plane's clique bound omega ≤ 3 with sharpened edge lower bounds for clique-free critical graphs — a theorem route whose key ingredient (the K4-free restriction) the earlier discharging line never used.
mechanism: A minimal 5-chromatic UDG is 5-critical, so min degree ≥ 4, and it contains no K4, because the unit-distance clique number of the plane is 3 (the only maximal clique is the equilateral triangle; four pairwise-unit points would be a regular tetrahedron, impossible in R^2). The killed size-bound line crossed the general Kostochka–Yancey bound f_5(n) ≥ (9n−5)/4 against SST's ceiling u_2(n) ≤ C n^{4/3}, and that first stopped forcing a contradiction at n = 10 even with the impossible C = 1, so its provable N was ≤ 9, below the census's n = 11. The new ingredient attacks the other side: the edge-minimal 5-critical graphs are K5-based (they contain large cliques), so K4-free 5-critical graphs are forced to have strictly more edges — a sharper lower bound f_5^{K4-free}(n) > f_5(n) on the number of unit edges. Crossing that sharper lower bound against SST can only push the contradiction to larger N.
status: refuted
killed-by: capped-below-census-and-epsilon-unattainable — the asymptotic SST crossing gives N ≈ 11 even with the K4-free (triangle-free) ε-refinement, because the crossing exponent (linear vs n^{4/3}) puts the contradiction at a fixed small n that the ε-sharpening changes only by a constant. The run's census has ALREADY proved N=11 by exact enumeration, so the asymptotic form cannot beat it; and the known ε in "|E| ≥ (9/4+ε)n − 5/4 − δ·T(G)" for triangle-free 5-critical graphs is an asymptotic existence constant, not explicit, so it cannot be asserted to reach the N=12 threshold ε > 5/48. The salvageable core — crossing the critical-graph bound against the *exact* ceiling u(n)=A186705 rather than the asymptotic SST — is adopted as exact-ceiling-size-bound.
first-step: Pin the sharpest known lower bound on |E| for K4-free 5-critical graphs on n vertices (the critical-graphs-with-forbidden-subgraph literature: Ore graphs, Gallai forests, Kostochka–Yancey refinements for H-free critical graphs); then solve the exact inequality f_5^{K4-free}(n) > C n^{4/3} for the largest N, and contrast it with the killed line's N = 9 and the run's census n = 11.
precedent: unchecked
speculation: Whether the K4-free refinement of Kostochka–Yancey is strong enough to beat N = 9 (and the census's n = 11). If the known K4-free bound is asymptotically equal to (9n−5)/4, the line retires with that precise datum — a result in itself.
```

## Why this is not the closed discharging line

- `discharging-minimal-counterexample` was killed by the pair (Kostochka–Yancey **general** 5-critical bound) × (SST ceiling), giving N ≤ 9. This proposal changes the *lower-bound* ingredient to a **K4-free** 5-critical edge bound, exploiting the plane's clique number ω ≤ 3, which the killed analysis did not include.
- It is a theorem route (an inequality), not a search and not a certificate.

Named mathematics: critical graphs with a forbidden clique, Gallai forests, Ore's theorem and its refinements, Kostochka–Yancey for H-free critical graphs, the plane's unit-distance clique number ω = 3.

## What would falsify it

If the sharpest known K4-free 5-critical edge bound is not strictly stronger than (9n−5)/4 for the relevant n, the new N does not exceed the killed line's N = 9 and the line retires. If SST's constant C in the relevant range is so large that even the sharper lower bound does not cross it below the census, the size bound stays out of reach by this route.
