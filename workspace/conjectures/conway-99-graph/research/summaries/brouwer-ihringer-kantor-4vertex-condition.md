# Bourwer–Ihringer–Kantor, "Strongly regular graphs satisfying the 4-vertex condition" — summary

<!-- source: https://arxiv.org/pdf/2107.00076 | arXiv:2107.00076 -->
Survey of SRGs satisfying the t-vertex condition (t=4 focus), with new families
obtained by switching on collinearity graphs of polar spaces (symplectic polar
spaces give 4-vertex-condition graphs).

## Why it belongs in this library

GOAL.md's main attack surface for srg(99,14,1,2) is a *counting identity* over
induced C₅/C₆/K₄−e and *forced local configurations*. The 4-vertex condition is
precisely such a counting identity: it fixes the number of induced
configurations straddling a pair of vertices, and is computable from
common-neighbour substructures. This paper is the standard reference for it.

## The statement that matters for (99,14,1,2)

**Proposition 2.1 (Sims).** An SRG with parameters (v,k,λ,µ) satisfies the
4-vertex condition, with parameters (α,β), iff the number of edges in the
induced common-neighbour subgraph Γ(x)∩Γ(y) equals α when x~y and β when
x≁y. In that case

```
k · (C(λ,2) − α) = β · (v − k − 1).
```

**Consequence for the family srg(v,k,1,2).** Here λ=1, so C(λ,2)=C(1,2)=0 and
the relation reads `−kα = β(v−k−1)`. Since k, v−k−1 > 0 and α, β are
nonnegative edge-counts, this forces **α = β = 0**. So *if* it satisfies the
4-vertex condition at all, a graph in this family must have α=β=0: for *every*
pair of vertices x,y (adjacent or not), the common-neighbour set Γ(x)∩Γ(y)
induces an independent set (no edges among the common neighbours).

The adjacent case (λ=1) is automatic: two adjacent vertices have exactly one
common neighbour, trivially independent. The content is in the nonadjacent case
(µ=2): the two common neighbours of a nonadjacent pair must be nonadjacent to
each other. **This is a checkable structural fact, and it is NOT an eigenvalue
argument** — so it is a candidate that survives the GOAL.md v=9 / v=243 test
(one must verify it holds for the rook's graph and BvLS, as it must for any
argument not already spectral).

> This deduction is arithmetic on the source's stated formula; treat the
> formula as sourced and the λ=1 ⟹ α=β=0 step as verified-by-hand arithmetic.
> Whether the 4-vertex condition actually *holds* for a hypothetical
> srg(99,14,1,2) (i.e. whether α,β are well-defined) is exactly the open
> structural question this raises — it is a lead for the research role, not a
> settled fact.

## The t-vertex hierarchy, and the 5-vertex condition for partial quadrangles

The source defines the t-vertex condition (lines 24-36): for every t-vertex
graph T with distinguished pair (x0,y0) and every pair of distinct vertices
(x,y), the number of copies of T mapping x0→x, y0→y depends only on whether
x,y are adjacent. Key ladder facts (lines 34-36, 84-86, 177-185):

- A graph satisfies the **3-vertex condition iff it is strongly regular**.
- A graph satisfies the **v-vertex condition iff it is rank 3**; the t-vertex
  conditions are a strictly increasing hierarchy between srg and rank 3.
- **4-vertex condition**: the collinearity graph of a generalized quadrangle
  or partial quadrangle satisfies it, with α = C(λ,2), β = 0 (lines 85-86,
  177). For a λ≤1 graph it likewise holds with α=β=0.
- **5-vertex condition**: "Reichard [31] showed that the collinearity graphs
  of generalized quadrangles satisfy the 5-vertex condition, and that ... GQ(s,s²)
  satisfy the 7-vertex condition. **More generally the 5-vertex condition holds
  for partial quadrangles**" (lines 181-185). The PQ part is asserted in the
  survey without a named proof (status asserted, not proved here).

**Consequence for (99,14,1,2).** A srg(99,14,1,2) has λ=1, hence is
diamond-free, hence is the collinearity graph of PQ(2,6,2) (Mohammadian-
Tayfeh-Rezaie, named in the adopted pq approach). Since a PQ collinearity
graph satisfies the 5-vertex condition (BIK, asserted), a hypothetical 99-graph
**must satisfy the 5-vertex condition** — a NECESSARY condition, and the first
rung of the hierarchy not automatic from regularity that the non-rank-3 99-graph
does not inherit for free. Both controls (rook(3)=PQ(2,1,2), BvLS=PQ(2,10,2))
are rank 3 and also PQs, so satisfy it trivially — the "step that breaks on 9
and 243" is absent by construction, making this programme admissible under
GOAL.md. What still must be checked is whether the 5-vertex-condition equations
at (99,14,1,2) are consistent (approach step (3)); consistency is automatic for
the controls, so an inconsistency at t=6 would be a 99-only win.

## Other content

- Theorem 1.1: for v≥4 there are at least ⌊v^(1/6)⌋! SRGs on ≤v vertices
  satisfying the 4-vertex condition (abundance).
- Polar-space switching constructions: new 4-vertex-condition families from
  symplectic polar spaces; cospectral partners.
- 4-vertex condition sits strictly between SRG and rank-3; first non-rank-3
  SRGs satisfying it start at v=36 (36,14,4,6), α=0, β=4.
- Kaski–Khatirinejad–Östergård 2011 (DST, arXiv trail) resolved STS(25) 4-vertex
  condition negatively (computer-assisted; via Klin/Kaski). Block graphs of STS
  are the triple-system analogue of this run's triangle geometry.

## Relation to the run's geometry

The triangle geometry of a putative srg(99,14,1,2) is a partial Steiner triple
system; its "blocks" are the graph triangles. The Sims criterion phrased on
common neighbours is directly the local geometry: it says the two distance-1
or distance-2 vertices sharing a pair impose independence among common
neighbours. This is the cleanest counting-identity lead currently in the
library.

## Source details
arXiv:2107.00076. A. E. Brouwer, Ferdinand Ihringer, William M. Kantor.
Full text at research/sources/brouwer-ihringer-kantor-4vertex-condition.full.md.

```claim
id: bik-5vertex-holds-for-pq
statement: The collinearity graph of a partial quadrangle satisfies the 5-vertex
  condition (BIK, extending Reichard's result that GQ collinearity graphs do).
  In particular 4-vertex holds for PQ/GQ collinearity graphs with alpha=C(lambda,2),
  beta=0; 5-vertex holds for PQ collinearity graphs; GQ(s,s^2) collinearity
  graphs satisfy the 7-vertex condition. A graph satisfying the 3-vertex
  condition iff strongly regular; the v-vertex condition iff rank 3.
hypotheses: Gamma is the collinearity graph of a partial quadrangle / generalized
  quadrangle. For the (99,14,1,2) application: lambda=1 implies diamond-free
  implies Gamma = PQ(2,6,2) collinearity graph.
holds-here: yes (99 is diamond-free, so it is a PQ collinearity graph, so it
  must satisfy the 5-vertex condition)
status: asserted (the PQ 5-vertex part is asserted in the survey, no proof named;
  the GQ part is cited to Reichard [31])
bearing: Makes the 5-vertex condition a NECESSARY condition on a hypothetical
  srg(99,14,1,2) -- the first hierarchy rung the non-rank-3 99-graph does not get
  for free. Both controls (rook, BvLS) are rank-3 PQs, so pass trivially: the
  admissibility step (must break on 9 and 243) is absent by construction.
anchor: research/sources/brouwer-ihringer-kantor-4vertex-condition.full.md
answers: pq-5vertex-condition-requirement
```
