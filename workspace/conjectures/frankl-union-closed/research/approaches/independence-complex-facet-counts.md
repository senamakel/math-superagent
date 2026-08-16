# Independence complex: facet counts, links, and the Euler characteristic

```approach
idea: Attack the graph formulation through the independence complex I(G). The
  maximal stable sets of a graph G are the facets of I(G); the number of facets
  containing a vertex v is the number of facets of the link lk(v). UC
  (Bruhn–Charbit–Schaudt–Telle) is equivalent to: every bipartite graph with an
  edge has, in each bipartition class, a vertex lying in at most half of I(G)'s
  facets. So the object is a simplicial-complex statement: facet counts of a
  complex and of its vertex links, with bipartiteness as the operative hypothesis.
mechanism: Facet counts of a complex and its links are tied by the reduced Euler
  characteristic χ̃(I(G)) = Σ_{F ∈ I(G)} (−1)^{|F|} and by the delete/contract
  (Alexander-duality) identities that for independence complexes of bipartite
  graphs relate facet counts to the f-vector and to the topology of the complex
  (Engström-type results on independence complexes of bipartite graphs). If some
  part had every vertex in > half the facets, the sum of link facet counts over
  that part would exceed the bound that the Euler characteristic / f-vector
  identity permits — a parity-and-topology contradiction instead of a counting or
  entropy one. This is the same graph object as the settled-class results, but
  driven by facet/link algebraic identities rather than by maximal-stable-set
  counting.
status: refuted
killed-by: independence-complex-nonpure — independence complexes of bipartite graphs are generally NON-PURE (maximal stable sets of differing cardinality), so the reduced Euler characteristic χ̃(I(G)) = Σ_{F∈I(G)}(−1)^|F| is an alternating signed sum over ALL faces and does NOT reduce to signed facet counts; no f-vector/Euler identity is established (or found) that forces a half-density vertex via link-facet counts. Engström-type / edge-ideal results (Dochtermann–Engström arXiv:0810.4120; Van Tuyl arXiv:0906.0273; Cook–Nagel SIDMA 2012) concern (co)homology, regularity, and Cohen–Macaulayness — not facet-count forcing. The one direct topology application to union-closed (Bhasin, cubical set of a simply-rooted family, arXiv:2409.17050) proves acyclicity + Euler–Poincaré identity but gives no abundance forcing.
precedent: graph-formulation (Bruhn–Charbit–Schaudt–Telle, https://arxiv.org/abs/1409.1814 — maximal stable sets ARE the I(G) facets, and the settled bipartite classes were obtained by explicit counting of maximal stable sets, which is the sound facet-count route); topological-union-closed-acyclicity (Bhasin 2024).
first-step: (refuted as stated — no topological identity was found; do not re-derive the Euler hinge. The sound route stays explicit maximal-stable-set counting as in the settled-class papers.)
```

**Refuted on evidence, not absence.** The facet-count *perspective* is exactly
the graph formulation and is the proven workhorse (the settled classes were
counted explicitly). But the specific proposed mechanism — an
Euler-characteristic/f-vector identity forcing a half-density vertex — has no
precedent and is structurally obstructed: I(G) is generally non-pure, so χ̃ is a
signed alternating sum over all faces, not a signed facet count, and no such
forcing identity is known. The closest topological result (Bhasin) gives
acyclicity without abundance forcing. The specific topological hinge is not
grounded; the explicit counting route already found in the literature is.
