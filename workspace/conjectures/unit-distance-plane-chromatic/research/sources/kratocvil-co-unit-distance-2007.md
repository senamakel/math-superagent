# Planar unit-distance graphs having planar unit-distance complement — the 69-graph census

**Source:** sciencedirect.com/science/article/pii/S0012365X07002841
(Discrete Mathematics 2007); seen in search results as
"Planar unit-distance graphs having planar unit-distance complement"
**Authors:** (Kratochvíl and co-authors; the 1-planar follow-up at GD 2025 is
Červenková & Kratochvíl)
**Full text:** NOT on disk — sciencedirect host is network-blocked for
download_document; content from server-side search-result excerpts.

## What this establishes — the co-unit-distance graph census

- **Definition.** A graph is a *co-unit-distance graph* if both it and its
  complement are unit-distance graphs in the plane; *strict* versions require
  non-edges to be at distance ≠ 1.
- **Census (exhaustive enumeration, Theorem/Table 1):** there are exactly
  **69 co-unit-distance graphs** in total, **65 strict**, of which **55
  connected** (51 strict connected), and **7 self-complementary**.
- **Classification method.** Connected co-unit-distance graphs are classified
  by the length λ of the largest induced cycle; it is shown λ ≤ 6 for
  connected co-unit-distance graphs. Enumeration per class: 8 (λ=6) + 5 (λ=5)
  + 16 (λ=4) + 19 (λ=3) + 7 (remaining) = 55 connected; the 14 disconnected
  ones come from complementation (a disconnected graph corresponds to a
  connected complement and conversely).

## Why it matters here

The small-graph classification tier: Globus–Parshall classify unit-distance
graphs on ≤ 9 vertices by forbidden subgraphs; this census classifies the
much rarer graphs whose *complements* are also unit-distance. For the run's
construction search, a candidate "almost unit-distance" graph (dense, with
many near-missing edges) that is a co-unit-distance graph is a place where
chromatic structure can be probed — and the census gives an exact list to test
against for small n. Also: 5-chromatic unit-distance graphs must be extremely
dense (5-critical ⇒ e ≥ 2n), so complement structure (how many non-edges a
dense unit-distance graph must have) is exactly the relevant growth question.

```claim
id: co-udg-census-69
statement: There are exactly 69 co-unit-distance graphs in the plane (graphs G with both G and its complement unit-distance embeddable), of which 65 are strict; 55 are connected (51 strict) and 7 are self-complementary.
hypotheses: plane unit-distance embeddings of both G and complement; strict = non-edges at distance != 1.
holds-here: yes for the small-graph census tier - an exact list against which the run's dense candidates can be checked for n small.
status: sourced (Discrete Mathematics 2007, via search-result excerpts; full text not on disk)
bearing: pins how many non-edges a small unit-distance graph can have while its complement stays unit-distance - a density/complement boundary for the construction search.
anchor: research/sources/kratocvil-co-unit-distance-2007.md
```

```claim
id: co-udg-induced-cycle-bound
statement: Every connected co-unit-distance graph has largest induced cycle length at most 6, and the connected census is 8 (lambda=6) + 5 (lambda=5) + 16 (lambda=4) + 19 (lambda=3) + 7 (remaining) = 55 graphs.
hypotheses: connected co-unit-distance graphs; lambda = largest induced cycle length.
holds-here: yes - a structural restriction on small co-unit-distance graphs usable as a filter.
status: sourced (Discrete Mathematics 2007, via search-result excerpts)
bearing: classification machinery for the small-graph layer; a non-edge-complement viewpoint on dense unit-distance candidates.
anchor: research/sources/kratocvil-co-unit-distance-2007.md
```

## Note on download

Full text blocked at the network layer (as with all publisher hosts in this
run). Status: **sourced via search excerpts; full text not on disk**.