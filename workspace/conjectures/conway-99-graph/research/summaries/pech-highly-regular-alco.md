# Pech, "On highly regular strongly regular graphs" — summary

**Source**: Christian Pech, *Algebraic Combinatorics* 4 (2021) no. 5, pp. 843-878,
doi 10.5802/alco.183. Open access (CC-BY 4.0). Full text held:
`research/sources/pech-highly-regular-alco.full.md` (front matter + references;
NNB — arXiv:2107.05747 is a DIFFERENT, unrelated ML paper, do not confuse; see
the correction note in that file).

## What it establishes

The paper unifies strong regularity, k-isoregularity, and the t-vertex condition
(§2-3) and builds an algebraic composition/decomposition theory of these
regularity conditions. Its headline results:

1. A family of non-rank-3 graphs already known to satisfy the 7-vertex
   condition (the point graphs of GQ(q, q²)) in fact satisfy the stronger
   (3,7)-regularity. This strengthens Reichard's 7-vertex-condition result.
2. From that family a new infinite family of non-rank-3 strongly regular graphs
   satisfying the 6-vertex condition is obtained.
3. **Central to this run's adopted approach:** the point graphs of partial
   quadrangles satisfy the 5-vertex condition (Pech, extending Reichard). This
   is the primary-source proof behind claim `bik-5vertex-holds-for-pq`, which
   the BIK survey had asserted.

## Relevance to srg(99,14,1,2)

The adopted approach `pq-2-6-2-classification` reformulates (99,14,1,2) as the
collinearity graph of PQ(2,6,2) and attacks it through the t-vertex-condition
hierarchy. Pech's theorem makes the **5-vertex condition a NECESSARY condition**
on a hypothetical srg(99,14,1,2) — the first hierarchy rung beyond strong
regularity. Per `bik-5vertex-holds-for-pq`: both controls (rook(3), BvLS) are
rank-3 PQs and pass trivially, so the 5-vertex condition does not by itself
separate 99 (it is necessary, not sufficient); the step would need a 99-specific
constraint one rung higher that the rank-3 controls do not satisfy for free.

## References spine (from the paper's bibliography)
Bamberg–De Clerck–Durante (intriguing sets in PQs, JCD 2011); Bose 1963
(strongly regular graphs / partial geometries); Bose–Shrikhande 1972; Brouwer's
SRG parameter table; Reichard (7-vertex condition); Hestenes–Higman (t-vertex
condition framework); the srg/partial-quadrangle literature. These reinforce the
PQ/5-vertex-condition literature the run relies on.
