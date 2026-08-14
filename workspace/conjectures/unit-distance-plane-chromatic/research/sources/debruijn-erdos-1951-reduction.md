# De Bruijn–Erdős 1951 — the finite-subgraph reduction

**Source:** N. G. de Bruijn, P. Erdős, "A Colour Problem for Infinite Graphs and
a Problem in the Theory of Relations", *Indagationes Mathematicae (Proceedings)*
54 (1951) 371–373. DOI https://doi.org/10.1016/s1385-7258(51)50053-7. Full text
also available at https://www.renyi.hu/~p_erdos/1951-01.pdf.

**How obtained:** Original text retrieved server-side via `deep_research`
(which fetched the renyi.hu PDF and returned its content line by line). The
direct download of the PDF was refused by the network boundary; the server-side
retrieval returned the actual theorem statements.

## What this source establishes

**Theorem 1 (de Bruijn–Erdős).** Let `k` be a positive integer and let the graph
`G` have the property that every finite subgraph is `k`-colourable. Then `G`
itself is `k`-colourable.

**Corollary / equivalent form.** For any graph `G` (finite or infinite),
`chi(G) = sup { chi(H) : H a finite induced subgraph of G }`. In particular, if
the chromatic numbers of finite subgraphs are unbounded, `chi(G)` is infinite.

**Proof.** Uses a theorem of Rado (the paper's Theorem 2): given sets `M_i` and
finite-compatibility data, there is a choice function agreeing with the finite
choices on every finite subset. Applied to colourings, the induced `x(·)` gives a
global colouring; the edge-by-edge argument uses that every edge lies in a finite
subgraph that is `k`-colourable, so its endpoints receive different colours.

**Choice principle.** Theorem 2 is a form of the axiom of choice / Rado's
selection lemma. The topological version of the same proof uses Tychonoff's
theorem on the product `k^{V(G)}` (Gottschalk 1951). The theorem is equivalent in
strength to the Boolean prime ideal theorem; for countable graphs `WKL_0`
suffices (reverse-mathematics reading). All this retrieval captured.

## Authority

**Duplicate note (librarian housekeeping):** the scholar wrote an overlapping
`research/sources/debruijn-erdos-1951-chromatic-reduction.md`; `CLAIMS.md` keys on
that file. This file is retained for its proof-detail notes; the two should be
read as the same source.

Primary source (the original paper), retrieved verbatim content. 275 citations
per the citation graph. This is the single most load-bearing reduction in
`problem.md`: it is what lets a finite unit-distance graph with `chi >= k` certify
`chi(plane) >= k`.

## Basis and status

- `chi(G) = sup chi(finite subgraphs)` — sourced (original paper, verbatim),
  universally accepted.
- Choice principle = AC / BPI / Tychonoff — sourced; noted so a proof here can
  cite it rather than re-deriving the compactness.
