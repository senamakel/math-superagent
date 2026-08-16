# Thread: the k=14, λ=1 local-structure route — what three settled cases share with 99

```thread
id: thread-k14-l1-local
question: The Conway graph srg(99,14,1,2) has k=14 and λ=1, so its local
  structure (neighbourhood = perfect matching 7K2, i.e. the closed
  neighbourhood is a windmill W14) is forced. Three nearby cases have been
  settled by local extension arguments at the SAME k=14 and λ=1. Can their
  shared machinery — fixed vertex, group-divisible design on the
  neighbourhood, counting inequality, coclique-design branch — be brought to
  bear on 99, whose only difference is μ=2 vs their μ=4 (57-graph) and the
  λ=3 (85-graph)?
status: open
rests-on: wilbrink-brouwer-5714ceedings, milosevic-starcomplement-5714-template,
  shpectorov-zhao-85-nonexists-template, c5 (7K2 local structure),
  derived-design-at-a-vertex (G-reduce)
blocked-by: none in the library; the next step is a concrete structural claim.
next: fix a vertex v0 of a putative srg(99,14,1,2); verify on rook(3) and BvLS
  that the verbatim analogue of the Wilbrink-Brouwer GD structure holds
  (7 groups of size 2; 84 exterior points as blocks of size 2 = the 84
  non-edges of the 7K2; this is exactly G-reduce). Then seek the analogue of
  the mu=4 contradiction: a counting inequality (Wilbrink-Brouwer Lemma 1) or
  a coclique-design branch (@ a 22-coclique, since coclique bound for 99 is
  n(-s)/(k-s) = 99*4/18 = 22) that gives a contradiction which rook(3) and
  BvLS escape by parameter.
```

## The three settled k=14 precedents

| Case | parameters | λ | μ | local structure | method | settled by |
|---|---|---|---|---|---|---|
| Wilbrink–Brouwer | (57,14,1,4) | 1 | 4 | windmill 7K2 | counting inequality + 2-(15,5,4) coclique design + GD block overlap | 1978 |
| Milošević | (57,14,1,4) | 1 | 4 | windmill 7K2 | star complements, 3720 segments | 2008 |
| Shpectorov–Zhao | (85,14,3,2) | 3 | 2 | cubic (µ=2 but λ=3) | 478 segments, Euclidean rep | 2025 |
| **99 (open)** | (99,14,1,2) | 1 | **2** | windmill 7K2 | ? | open |

The (57,14,1,4) pair share with 99 both k=14 AND λ=1 — the exact same forced
local structure (neighbourhood = perfect matching, closed neighbourhood =
windmill W14, exterior points = blocks of a group divisible design on the
neighbourhood). Only μ differs (4 vs 2). The 85-graph shares k=14 and μ=2 but
NOT λ=1 (λ=3), so its local graph is cubic rather than a matching — a DIFFERENT
and harder local space (39 good cubic graphs) than 99's (one graph: 7K2).

So (99,14,1,2) sits exactly between two settled templates:
- its λ=1, k=14 local geometry is the (57,14,1,4) one, but with μ=2 (blocks of
  size 2 instead of 4 → the GD on the neighbourhood degenerates to the 7K2
  itself + 84 size-2 exterior blocks);
- its μ=2 is the (85,14,3,2) one, but with a FAR simpler local graph (7K2 vs 39
  cubic graphs) so the analogous segment space would be far smaller than 478.

## The transferable machinery (from the full texts)

From Wilbrink–Brouwer (primary, CWI 1978, in library):
1. **Counting inequality (Lemma 1).** For an induced subgraph H with N points,
   M edges, degrees d_i:
   `(kN−2M) − (λM + μ(C(N,2)−M) − Σ C(d_i,2)) ≥ n−N`, equality iff the
   exterior points adjacent to 2 points of H number exactly `(kN−2M)−(n−N)`.
   Applies verbatim to any (99,14,1,2) — a fully general weapon.
2. **Coclique bound (Lemma 2).** Coclique size ≤ n(−s)/(k−s); equality gives a
   2-design. For 99: s=−4, bound = 99·4/18 = 22. A 22-coclique in a putative
   99-graph would force a 2-(22,K,2) design structure — the direct analogue of
   the 2-(15,5,4) branch that kills the 57-graph.
3. **Group-divisible design structure.** Fix ∞: Γ(∞) = 7 groups of size 2
   (the perfect matching); exterior vertices ↔ blocks of size μ on Γ(∞). For
   μ=2 the blocks are the 84 non-edges of the 7K2 — exactly the G-reduce
   bijection already in the library (research/backward/derived-design-at-a-vertex.md).

From Shpectorov–Zhao: the local-template + Euclidean-eigenspace enumeration
closed a μ=2 k=14 case by complete finite search; for 99 the local graph 7K2
makes the analogue search smaller (one local graph, far fewer segments than
478), which is why attempting it at 99 is worth considering — with the
exhaustiveness argument that made their search a theorem.

## What this thread implies that the library has not yet stated

1. The **57-graph, not the 85-graph, is the closest local structural analogue
   of 99** (same k=14 AND λ=1, same windmill). GOAL.md's guidance named the
   (85,14,3,2) local-enumeration template; the library now also holds a λ=1
   template with the IDENTICAL local seed for a μ=2 case (99).
2. The **coclique design branch is a concrete unexploited route**: a 22-coclique
   (or its absence) in a putative (99,14,1,2) gives a 2-design structure, and
   the (57,14,1,4) proof shows exactly how such a design-theoretic contradiction
   runs. This is structural, non-spectral, and the coclique bound is the one
   part that differs between 99 and the controls (verified exact in
   code/out/coclique-bound-verified.md): rook(3) bound = 3, 99 bound = 22,
   BvLS bound = 45. Whether a 99-graph can have a 22-coclique (or must) is
   open and un-attacked in the library.
3. The counting inequality (Lemma 1) has never been applied in this run to
   99 — it applies verbatim and is a candidate structural tool.

## Negative-control discipline
Any use of the counting inequality or coclique-design branch must be tested so
it does NOT also rule out rook(3) and BvLS. The coclique bounds for the two
controls (3 and 45) differ from 99's (22), so a contradiction that uses the
specific value 22 is the promising direction; one that holds for all three is
refuted on arrival. This thread records the test before the search starts.
