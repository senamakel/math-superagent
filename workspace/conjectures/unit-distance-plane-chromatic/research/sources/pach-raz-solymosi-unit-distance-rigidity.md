# Erdős's Unit Distance Problem and Rigidity

**Source:** arxiv.org/abs/2507.15679
**Authors:** János Pach, Orit E. Raz, József Solymosi
**Full text:** research/sources/pach-raz-solymosi-unit-distance-rigidity.full.md (download blocked; see note)

## What this paper establishes (technique relevance to Hadwiger–Nelson)

- **Recasts unit-distance problem as point–circle incidences.** A set P of n
  points determines u(P) unit-distance pairs iff those pairs are incidences
  between points of P and unit circles centred in P. This lets incidence
  geometry bear on the question.
- **Spencer–Szemerédi–Trotter (1984) theorem:** the maximum number of unit
  distances among n points in the plane is O(n^{4/3}). This is the classical
  upper bound the problem.md leads cite (`O(n^{4/3})` bound). Erdős's
  conjectured truth is near n^{1+1/log log n}, attained by a sqrt(n) × sqrt(n)
  grid.
- **Structure Theorem (their Theorem 6):** if u(P) ≥ n^{4/3} h(n) with
  h(n) → ∞, then P decomposes into a large subset P′ (size ≈ n^{1/3} h(n)^4)
  and a family of bipartite graphs G_i with small parts (size ≲ h(n)^6) and
  many edges (|E_i| ≳ h(n)^7), each admitting unit-distance embeddings. This is
  the "rigidity forces structure" phenomenon.
- **Rigidity Conjecture (their Conjecture 7):** if a graph G has enough
  unit-embeddings and its vertex-neighbourhoods avoid collinear embeddings,
  then a substantial subgraph G′ on ≥ 4 vertices admits a rigid realisation in
  the plane. If this conjecture holds (even in a weaker form proven by Raz and
  Solymosi), it improves the O(n^{4/3}) barrier.

## Why it matters here

The unit-distance graph that Hadwiger–Nelson attacks has rigidity at its core:
a graph forcing high chromatic number has to be algebraically rigid, with many
coincidental unit distances. This paper gives the structural vocabulary — how
near-extremal unit-distance sets must decompose, and why rigidity is the source
of density.

## Note on download

Full text download (arxiv.org/html/2507.15679 and doi:10.4230/...) failed at
the network layer in this run. The read_sources summary is the basis for the
content above. Status: **sourced via read_sources; full text not on disk**.
