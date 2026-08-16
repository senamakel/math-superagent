# Carr 2026 — Every Minimal Counterexample is Predominantly Cubic (FULL TEXT)

Source: arXiv:2605.22844 (Avery Carr), "Every Minimal Counterexample to the
Erdős–Gyárfás Conjecture is Predominantly Cubic", 13 May 2026, 4 pp.
Full text: [[carr-predominantly-cubic-fulltext.html.full]] (this library now
holds the complete proof, previously only the abstract).
URL recorded in the full text.

## What it establishes (verified against full proof text)

A **minimal counterexample** = graph of minimum order and, subject to that,
minimum size, δ≥3, no cycle of length 2^k.

- **Lemma 0.1**: every proper subgraph H ⊊ G has δ(H) ≤ 2. (Proof: if some
  proper subgraph had δ≥3, by minimality it would contain a 2^k-cycle, which
  is also in G. Contradiction.)
- **Corollary 0.1(1)**: every vertex is adjacent to a vertex of degree exactly
  3. (From Lemma 0.1 applied to G−v: δ(G−v) ≤ 2, so deleting v must drop some
  neighbour to degree ≤2, i.e. that neighbour had degree exactly 3 in G.)
- **Corollary 0.1(2)** (Markström): the degree-≥4 vertices form an independent
  set. (Deleting an edge between two degree-≥4 vertices would leave δ ≥ 3,
  contradicting Lemma 0.1.)
- **Corollary 0.2**: every regular minimal counterexample is cubic.
- **Theorem 0.1**: at least **4/7** of the vertices have degree exactly 3.
  Proof: V≥₄ independent ⟹ every V≥₄ vertex's neighbours are in V₃ ⟹
  e(V₃,V≥₄) ≥ 4|V≥₄|; each V₃ vertex has degree 3 ⟹ e(V₃,V≥₄) ≤ 3|V₃|.
  Hence 4|V≥₄| ≤ 3|V₃| ⟹ |V| = |V₃|+|V≥₄| ≤ 7/4|V₃| ⟹ |V₃| ≥ 4/7|V|.

## What it implies here

These are the load-bearing structural facts of the near-cubic thread
(`research/threads/near-cubic-degree-spine.md`). The independent-set +
dominating-degree-3 facts force a minimal counterexample to be *nearly cubic*:
cubics dominate (≥4/7), degree-≥4 vertices form an independent set touching only
degree-3 vertices.

## Not settled / sharpness

The 4/7 lower bound is what Carr proves. A stronger bound |V₃| ≥ 2|V≥₄|+1
(>2/3 of vertices cubic) is derivable from Corollary 0.1(1) — each V₃ vertex
has a distinct V₃ neighbour, so at most 2 V≥₄ neighbours — and is verified in
`librarian` this cycle (see holdings note and the erdosproblems-64-discussion
summary). That improvement is NOT in Carr's paper.

```claim
id: ce-predominantly-cubic
statement: Every vertex of a minimal counterexample is adjacent to a degree-3 vertex, and at least 4/7 of its vertices have degree exactly 3.
hypotheses: G a minimal counterexample (vertex- and edge-minimal, δ≥3, no 2^k-cycle)
holds-here: yes (exactly the counterexample class under attack)
status: proved (full proof text now held and read)
anchor: research/sources/carr-predominantly-cubic-fulltext.html.full.md
```
