# Reimbayev, "The Subgraphs of Order Six of the Family of SRGs with λ=1 and μ=2" (arXiv:2508.03377) — FULL TEXT

<!-- source: https://arxiv.org/html/2508.03377v2 | full text at research/sources/reimbayev-subgraphs-order-six-body.full.md -->

## What the paper establishes (body now in library)

For the whole family srg(v,k,1,2), derives **exact counts of every induced
subgraph of order ≤ 6** in terms of n, k and a single further parameter n_3.

**Subgraphs of order ≤ 5: exact, depending only on (n,k).** Complete lists for
the nine order-4 subgraphs (l_1..l_9) and the order-5 subgraphs (m_1..m_21) are
given with closed forms, e.g.
- l_4 (order-4: P₂ ∪ P₃-type / "tail") = (1/2) n k (k−2)(n−3k+4)
- l_6, l_7, l_8, l_9 = (1/6) n k (k−2)(k−4), (1/12)nk(k−2)(k−4),
  (1/8) n k (k−2), (1/2) n k (k−2)
- m_13 (number of P₅) = (1/2) n k (k−2)(k²−8k+17)

Since the (n,k) are themselves tied (five-member family), these counts depend
effectively on k alone.

**Subgraphs of order 6: all 62 (n_1..n_62) given in closed form as a term in
(n,k) plus a multiple of n_3.** Where n_3 is the number of subgraphs of type 3
(Figure 1 / "graph 3"): two triangles sharing exactly one edge — equivalently
two triangles joined by two edges. Examples (n_12 = hexagon count):
```
n_12 = (1/12) n k (k−2)(2k²−21k+53) + n_3     <- hexagons
n_2  = (1/2) n k (k−2)
n_9  = (1/4) n k (k−2)(k−4) − n_3
n_3  = free parameter (unknown multiple)
```

## The key structural observation

Every order-6 subgraph count depends on n_3 and n_3 alone as the undetermined
parameter; order ≤5 counts have none. The paper states (Section 4): "All the
arguments of symmetry tell that n_3 must be equal zero. But that would
immediately mean, as shown by Makhnev [7], that an srg(99,14,1,2) doesn't
exist" — [7] = Makhnev 1988, Mat. Zametki 44(5) 667-672. And if the conjecture
that n_3 = 0 holds for the whole family, all graphs are built from Paley-9
building blocks.

## What the run should take from it

1. The **entire subgraph-count structure through order 6 is now in the
   library** with explicit formulas. This is a ready-made, checkable oracle
   target: the run can verify these counts exactly on the two existing graphs
   (Paley 9 and BvLS) using its own adjacency matrices, independent of the
   paper — a direct application of the oracle task.
2. **n_3 = 0 is the crux.** The run's counting-identity attack should aim at
   proving or refuting n_3 = 0 (pairs of triangles sharing an edge / joined by
   two edges). If n_3 = 0 is forced in any srg(99,14,1,2), then via the
   Makhnev conditional the graph cannot exist.
3. **Caution / status**: the formulas are asserted-by-source from an arXiv
   preprint (2025, not peer-reviewed); the Makhnev 1988 nonexistence conditional
   is no longer merely on Reimbayev's word — the primary Russian full text is
   in the library and its Thm 2 confirms the conditional (claim
   `makhnev1988-condstar-theorems`). The formulas, being explicit closed forms
   in (n,k,n_3), are independently checkable by the run on the two existing
   graphs — and the hexagon identity n12 = formula + n3 with n3=0 has been
   checked exactly on both controls (code/out/hexagon_identity_verified.captured.txt).

## Lou–Murin forbidden order-9 lead (from the paper's introduction)

The paper's introduction (lines 25-33) records a concrete, separate structural
lead that GOAL.md's "forced local configuration" surface names:

> "Using Wilbrink and Brouwer's lemma, Lou and Murin were able to establish a
> forbidden subgraph of order 9 in case when k = 14. This fact should hold true
> for any k, which needs a strict proof of course."

So Lou & Murin (the unpublished [9] reference) proved, via Wilbrink–Brouwer's
lemma, that a putative (99,14,1,2) contains a **forbidden subgraph on 9
vertices**. If this were independently verifiable, it would be exactly a
"forced local configuration that does not extend" — one of GOAL.md's named
attack surfaces. Status: **asserted-by-source on Reimbayev's word**; the
Lou–Murin work is not found in any indexed source (a working note / course
project), and the forbidden 9-vertex subgraph itself is not described in
Reimbayev's paper. This is a lead to hunt, not an established fact.

The Wilbrink–Brouwer lemma is from [8] = H. Wilbrink & A.E. Brouwer, "A (57,14,1)
strongly regular graph does not exist", Indag. Math. (Proc.) 86(1) 117-121 (1983).
That is the closely adjacent λ=1 nonexistence precedent (k=14, but μ=1 not 2);
Brouwer's table row `57 14 1 4 | 2^38 –5^18` confirms (57,14,1,4) noted as ruled
out. This (57,14,1) proof is the closest λ=1, k=14 nonexistence argument in the
literature and is a model for how a small-μ+λ=1 case gets killed.

## n_3 meaning (from the derivation)

n_3 (type 3 in the order-6 figure) is one specific order-6 subgraph, defined by
the relation `2 p_4 = 3 n_1 + n_3` (recover triangles on the opposite sides of a
quadrilateral). The interpretive content "n_3 = pairs of triangles joined by
two edges" and the "n_3=0 ⟹ nonexistence via Makhnev" rely on Reimbayev's own
reading of Makhnev 1988 (paywalled). Keep the two apart: the closed-form
formulas (order ≤5 exact; order-6 = (n,k)-term + multiple of n_3) are checkable
arithmetic; the nonexistence conditional is asserted-by-source.
Using code/lib oracle on BvLS (243,22,1,2) and Paley 9: count induced subgraphs
of each of the 21 order-5 types and 62 order-6 types and compare against the
paper's formulas with the appropriate n,k and n_3 (for these two graphs n_3
should match the observed count of pairs of triangles sharing an edge). This
both verifies the paper and pins down n_3 for the existing graphs.

```claim
id: reimbayev-order-six-subgraph-counts
statement: In any srg(v,k,1,2), all induced-subgraph counts of order <= 5 are
  determined by (n,k) alone (closed forms given), and all 62 order-6 induced
  subgraph counts are determined by (n,k) plus a single parameter n_3 (number
  of pairs of triangles sharing an edge = two triangles joined by two edges).
  If n_3 = 0 then a putative srg(99,14,1,2) would not exist (Makhnev 1988
  Thm 2, primary Russian full text now in library; conditional on n_3=0,
  which is itself a conjecture).
hypotheses: srg(v,k,1,2); the counting derivations in the paper.
holds-here: yes — the full subgraph-count structure of the family. The hexagon
  identity n12 = formula + n3 (with n3=0) is checked exactly on both control
  graphs; the order-6 counting alone does not force n3>=1 at (99,14,1,2)
  (claim order6-n3-not-forced).
status: asserted-by-source for the full formula list (arXiv preprint, not
  peer-reviewed); the hexagon identity and n3=0 on the controls are checked;
  the Makhnev conditional is sourced.
bearing: gives the run its most concrete counting-identity target: n_3, the
  count of edge-sharing triangle pairs. Attacking n_3=0 (or computing n_3 for
  the existing graphs to calibrate) is the natural next step.
anchor: research/sources/reimbayev-subgraphs-order-six-body.full.md
follows-from: makhnev1988-condstar-theorems, order6-n3-not-forced
```
