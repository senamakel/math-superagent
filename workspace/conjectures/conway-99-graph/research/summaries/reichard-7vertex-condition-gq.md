# Reichard, "Strongly regular graphs with the 7-vertex condition" — summary

**Source**: Sven Reichard, arXiv:1401.6816 [math.CO], 2014; published J. Algebraic
Combin. 40 (2014) 857-865, doi 10.1007/s10801-014-0554-1. Full text:
`research/sources/reichard-7vertex-condition-gq.full.md`.

## What it establishes

- **Theorem 1.** The point graph of a generalized quadrangle satisfies the
  5-vertex condition. (Primary proof behind the GQ case of the PQ 5-vertex claim;
  Pech 2021 extends this from GQ to all PQ point graphs.)
- **Theorem 2.** For any integer s, the point graph of a GQ of order (s,s²)
  satisfies the 7-vertex condition. This yields the first infinite family of
  non-rank-3 strongly regular graphs satisfying the 7-vertex condition.
- **Corollary 1.1.** Klin's parameter t₀ (the threshold where the t-vertex
  condition characterizes rank-3 graphs) is at least 8. Sharpness: a GQ(5,3)
  does not satisfy the 6-vertex condition; a GQ(5,25) does not satisfy the
  8-vertex condition.

## Proof structure (t-vertex-condition machinery)

- Theorem 3 (Hestenes–Higman criterion): Γ is k-isoregular and satisfies the
  (t−1)-vertex condition; to test the t-vertex condition it suffices to test
  graph types whose additional vertices have valency at least k+1.
- Theorem 4: for fixed t, the t-vertex condition is checkable in time polynomial
  in n.
- Theorem 8: if Γ satisfies the 4-vertex condition, checking the 5-vertex
  condition reduces to 8 graph types (Table 1).
- Lemmas 6.1-6.4 give counts of the forbidden/observed types in a GQ, showing
  the counts are constant — whence Thm 1.

## Relevance to srg(99,14,1,2)

The 99-graph is a PROPER partial quadrangle, not a generalized quadrangle
(μ=2 ≠ t+1=7), so Reichard's Thm 1 (GQ 5-vertex) does NOT by itself apply; the
PQ extension is Pech Thm 5.7. This source is the primary second proof of the
5-vertex-condition programme and provides the 6-vertex/7-vertex machinery (8-type
reduction) that Pech's Prop 5.8 builds on. It confirms the t-vertex hierarchy is
the right weakening-of-rank-3 instrument: rank-3 graphs satisfy every t-vertex
condition, and a hypothetical 99-graph is provably non-rank-3, so the vertex
conditions are exactly where it could differ from the rank-3 controls.
