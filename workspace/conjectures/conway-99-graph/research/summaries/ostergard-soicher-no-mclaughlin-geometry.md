# There is no McLaughlin geometry — Östergård & Soicher (2018)

<!-- source: https://arxiv.org/pdf/1607.03372 (published J. Combin. Theory Ser. A 155 (2018) 27–41, doi 10.1016/j.jcta.2017.10.004) -->

> **A mis-download was corrected here.** The first fetch of this file used the
> guessed arXiv id `1705.06821`, which is actually a machine-learning paper on
> spatial variational auto-encoders. That wrong paper must NOT be cited for the
> Conway 99-graph problem. The correct arXiv id is **1607.03372**. This file now
> holds the correct paper.

## What it establishes

**Theorem.** There is no partial geometry `pg(s, t, α)` with parameters
`(s, t, α) = (4, 27, 2)`. Such a geometry would have the **McLaughlin graph**
(275, 112, 30, 56) as its point graph.

**Two consequences the run must hold:**
1. The **McLaughlin graph is not the point graph of any partial geometry**
   `pg(4, 27, 2)`.
2. More generally, a **pseudogeometric strongly regular graph that achieves
   equality in the Krein bound need not be geometric** — need not come from a
   partial geometry — when `α > 1`. The `α = 1` case (where point graphs of
   partial geometries are the pseudo-geometric graphs) does not extend.

**Method.** Symmetry reduction combined with high-performance distributed
backtracking search (256-core cluster). Uses explicit permutation generators
for the automorphism group of the McLaughlin graph and detailed computational
checks. Proves nonexistence by exhausting symmetry-reduced cases.

## Why this matters for the Conway 99-graph

The run reasons about a putative srg(99,14,1,2) as the **collinearity graph of
a partial linear space** on 99 points with 231 lines of size 3 and 7 lines per
point. Because λ=1, this geometry is actually a **linear space structure** (any
two adjacent vertices lie on a unique triangle → a unique line). But the
McLaughlin-geometry result is a cautionary precedent: **an SRG with feasible
parameters that would be the point graph of a partial geometry may still fail
to be geometric**, even when it is pseudogeometric and satisfies strong bounds.
So any argument that reasons from the geometry of (99,14,1,2) must be careful:
the graph, if it exists, is the point graph of a *partial linear space* (which
is automatic here from λ=1, triangles = lines), but the *partial-geometry*
status of the collinearity structure is not automatic. The relevant contrast:
for λ=1, μ=2 with k=14, `k < 12λ(λ+3)` fails, so this is NOT near the Krein
bound-achieving regime the McLaughlin case lives in. Still, the run should not
assume the triangle geometry "nicely" realizes anything without checking.
