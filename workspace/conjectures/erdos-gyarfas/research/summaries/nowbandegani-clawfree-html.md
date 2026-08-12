> Summary — replaces the digest. Full text: [[nowbandegani-clawfree-html.full]] (P. Salehi Nowbandegani, H. Esfandiari, M. H. Shirdareh Haghighi, K. Bibak, "On the Erdős-Gyárfás conjecture in claw-free graphs", arXiv:1109.5398v3, 7 Feb 2013; published Discuss. Math. Graph Theory 34(3) (2014) 635–640).

## What the source establishes

**Theorem 2.1.** Let G be claw-free with δ(G) ≥ 3. Then G has a cycle whose length is 2^k or 3·2^k for some k ≥ 1.
- Proof uses **Lemma 2.2**: if δ(G) ≥ 3 and G has no C4, then G has a hole (induced cycle) of length n ≥ 5. (This is the same induced-cycle lemma restated by Gao–Shan as their Lemma 3.1.)

**Theorem 2.7.** Let G be claw-free with δ ≥ 4 and no C4. Then every non-cut vertex of G lies on a cycle whose length is a power of 2. (An aside: this theorem has a "non-cut vertex" hypothesis — the only occurrence of any cut-connectivity idea in the whole EG literature; it is about a different class and does not constrain general minimal counterexamples.)

**§3 — triangle structure in cubic claw-free C4-free graphs (the closest analogue to a triangle-exit lemma).**
> "Suppose that G is a cubic claw-free graph that does not contain C4. Let v be an arbitrary vertex ... Since G is claw-free, so we can assume that xy ∈ E(G). Thus, xz, yz ∉ E(G); otherwise a C4 appears. Let x1 and y1 be respectively the other neighbours of x and y. Easily we see that x1 ≠ y1. Therefore, for every vertex there exists a unique triangle containing it, such that the other neighbours of its vertices are distinct."

**Proposition 2.** The mapping G ↔ Ĝ (contract each triangle to a vertex) is a one-to-one correspondence between simple cubic graphs and simple cubic claw-free graphs without C4. **Corollary 3.** If Ĝ has a cycle of length k, G has cycles of every length 2k, 2k+1, …, 3k.
**Theorem 3.2.** Any counterexample to EG in cubic claw-free graphs has at least 114 vertices (via the 38-vertex bound on Ĝ).

## Implication for this run

- The **"exits of a triangle are distinct"** content is published **only in the cubic claw-free C4-free case** (this paper, §3). The exits are the "other neighbours" x1, y1 of the two triangle vertices x, y (and similarly z1). Independence of the exits and non-adjacency of an exit to the other two triangle vertices are **not** stated. So a general (non-claw-free) triangle-exit lemma would be new.
- The triangle-contraction idea (cycles of length 2k..3k from a cycle of length k in the triangle-contracted graph) is a reusable technique; it is exactly the mechanism that produces the run's Apollonian/K4-triangle-expansion census family.
- 114-vertex bound for cubic claw-free counterexamples: an existing computational/structural bound for that class.

```claim
id: EG-clawfree-triangle-exits-distinct
statement: In a cubic claw-free C4-free graph, every vertex lies in a unique triangle, the other neighbours of the three triangle vertices are distinct, and the graph is vertex-disjoint triangles joined by a perfect matching (equivalently G ↔ Ĝ, contract each triangle to a vertex, is a bijection to simple cubic graphs). The exits' independence and their non-adjacency to the other triangle vertices are not stated.
hypotheses: G cubic, claw-free, C4-free.
holds-here: no — a minimal counterexample is not known to be claw-free, so this structure does not transfer.
status: proved (Nowbandegani–Esfandiari–Shirdareh–Bibak, DMGT 34 (2014) 635–640, §3).
bearing: The published "distinct exits" fact requires claw-freeness; any triangle-exit lemma the run proves without claw-freeness is new.
anchor: research/summaries/nowbandegani-clawfree-html.md
```