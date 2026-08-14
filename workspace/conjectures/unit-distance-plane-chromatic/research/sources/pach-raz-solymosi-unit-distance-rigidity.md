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

```claim
id: ud-bound-spencer
statement: The maximum number u(n) of unit distances among n points in the Euclidean plane is O(n^{4/3}). This is the Spencer–Szemerédi–Trotter (1984) bound.
hypotheses: Points in R^2; distance exactly 1.
holds-here: true — this is the density constraint on unit-distance graphs that the Hadwiger–Nelson lower-bound search must respect (rigid graphs are what matter, since density cannot be bought).
status: sourced (surveyed and cited in Pach–Raz–Solymosi, arxiv 2507.15679)
bearing: Bounds what a unit-distance graph on n vertices can look like; rules out random/greedy density.
anchor: research/sources/pach-raz-solymosi-unit-distance-rigidity.md
```

```claim
id: ud-rigidity-structure
statement: If a planar point set P of size n has u(P) >= n^{4/3} h(n) with h(n) -> inf, then P decomposes into a large subset and bipartite subgraphs G_i with small parts and many edges, each admitting unit-distance embeddings. (Structure Theorem)
hypotheses: P subset R^2, |P|=n, near-extremal unit-distance count.
holds-here: conjectural/imposing-structure; marks rigidity as the source of density, which is the regime unit-distance graphs that defeat 4 colours would live in.
status: sourced (Pach–Raz–Solymosi Theorem 6)
bearing: Supports the framing that only algebraically rigid point sets are dense enough to matter for the chromatic-number lower bound.
anchor: research/sources/pach-raz-solymosi-unit-distance-rigidity.md
```

```claim
id: prs-incidence-recasting
statement: A set P of n points determines u(P) unit-distance pairs iff those pairs are incidences between the points of P and the unit circles centred in P; the unit-distance problem is thereby a point–circle incidence problem.
hypotheses: plane geometry; distance exactly 1.
holds-here: yes — definitionally; the recasting is what lets the Szemerédi–Trotter incidence machinery yield O(n^{4/3}).
status: asserted (stated in the excerpt; elementary)
evidence: research/sources/pach-raz-solymosi-unit-distance-rigidity.md (librarian excerpt; primary text not on disk)
bearing: links the chromatic search to incidence geometry: near-maximal unit-distance configurations are near-maximal point–circle incidence configurations, i.e. algebraically rigid ones.
anchor: research/sources/pach-raz-solymosi-unit-distance-rigidity.md
```

```claim
id: prs-rigidity-conjecture
statement: (PRS Conjecture 7) If a graph G has sufficiently many unit-distance embeddings and the neighbourhoods of its vertices avoid collinear embeddings, then a substantial subgraph G' on at least 4 vertices admits a rigid realisation in the plane; if the conjecture holds — even in the weaker form already proved by Raz and Solymosi — the O(n^{4/3}) barrier for u(n) improves.
hypotheses: G has "enough" unit embeddings; vertex neighbourhoods avoid collinear embeddings; rigid realisation in R^2.
holds-here: unchecked — the hypothesis of many embeddings concerns the algebraic side of density; a minimal 5-chromatic graph is only known to have one embedding (itself), so applicability to the chi >= 5 problem is unknown and possibly false.
status: asserted (explicitly a conjecture in the source)
evidence: research/sources/pach-raz-solymosi-unit-distance-rigidity.md
bearing: marks the route from rigidity to improved density bounds; no direct computable consequence for the chromatic search.
anchor: research/sources/pach-raz-solymosi-unit-distance-rigidity.md
```

```claim
id: ud-erdos-grid-lower
statement: Erdős conjectured the true growth of u(n) to be close to n^{1+1/log log n} — far below n^{4/3} — and that order is approached by the sqrt(n) x sqrt(n) square grid.
hypotheses: n points in R^2.
holds-here: n/a — background for interpreting the O(n^{4/3}) bound; not a tool for the chromatic search.
status: sourced (Erdős's conjecture as surveyed in the PRS excerpt)
evidence: research/sources/pach-raz-solymosi-unit-distance-rigidity.md
bearing: none directly; clarifies that the 4/3 exponent is a loose upper bound, so what "dense" can mean for unit-distance graphs is still open territory.
anchor: research/sources/pach-raz-solymosi-unit-distance-rigidity.md
```

## Note on download

Full text download (arxiv.org/html/2507.15679 and doi:10.4230/...) failed at
the network layer in this run. The read_sources summary is the basis for the
content above. Status: **sourced via read_sources; full text not on disk**.
