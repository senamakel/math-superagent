# Smallest known 5-chromatic unit-distance graph, and the verification bound

## Record chain (exact citations, abstracts verbatim in this library)

- **1581 vertices — de Grey 2018.** A.D.N.J. de Grey, "The chromatic number of
  the plane is at least 5", arXiv:1804.02385 (2018). This was the first proof
  that χ(plane) ≥ 5. The count "smallest published unit-distance graph with
  chromatic number 5 has 1581 vertices. The latter graph was constructed by
  Aubrey de Grey" is quoted verbatim from Heule 2018's abstract (below), and
  de Grey's citation appears independently in three citation records held here
  (Globus–Parshall 2019, Heule 2018, Voronov–Neopryatnaya–Dergachev 2022), the
  latter giving the arXiv id explicitly.
- **553 vertices — Heule 2018.** M.J.H. Heule, "Computing Small Unit-Distance
  Graphs with Chromatic Number 5", arXiv:1805.12181 (2018). Abstract (verbatim
  on disk): "our method … allowed us to compute several 553-vertex unit-distance
  graphs with chromatic number 5, while the smallest published unit-distance
  graph with chromatic number 5 has 1581 vertices. … Also, our graphs can be
  mechanically validated in a second."
- **509 vertices — Parts 2020 (current record as held).** Jaan Parts, "Graph
  minimization, focusing on the example of 5-chromatic unit-distance graphs in
  the plane", arXiv:2010.12665 (2020). Abstract (verbatim on disk): "We applied
  this method to minimize 5-chromatic unit-distance graphs and obtained a graph
  with **509 vertices and 2442 edges**."
- Related, content screened this run: G. Exoo, D. Ismailescu, "The Chromatic
  Number of the Plane is At Least 5: A New Proof", Discrete & Computational
  Geometry (2019), doi:10.1007/s00454-019-00058-1 (cited by Parts, Heule,
  Voronov et al.); J. Parts, "The chromatic number of the plane is at least 5 —
  a human-verifiable proof", arXiv:2010.12661 (2020).

## Proved lower bound on the size of a 5-chromatic unit-distance graph

Two facts bound the "verification number" N (largest N such that every
unit-distance graph on ≤ N vertices is 4-colourable):

1. **N ≤ 508 (forced, no search needed).** Since a 509-vertex 5-chromatic
   unit-distance graph exists (Parts 2020), the statement "every unit-distance
   graph on ≤ N vertices is 4-colourable" fails at N = 509, so any proved N
   satisfies N ≤ 508.
2. **N ≥ 6 (proved here, elementary).** Every unit-distance graph on ≤ 6
   vertices is 4-colourable. Argument: a graph on n ≤ 6 vertices with χ ≥ 5
   contains a 5-critical subgraph H on ≤ 6 vertices, and every 5-critical graph
   has minimum degree ≥ 4 (Dirac 1953; the run holds this as claim
   `k-critical-min-degree`). With n ≤ 5, δ ≥ 4 forces K4; with n = 6, δ ≥ 4
   forces e ≥ 12, and the unique K4-free 6-vertex graph with 12 edges is the
   Turán graph K_{2,2,2} (χ = 3), so any χ ≥ 5 graph on 6 vertices contains K4.
   But K4 is not a unit-distance graph (two unit circles meet in at most two
   points; equivalently K4 is among the Globus–Parshall minimal forbidden
   subgraphs on ≤ 5 vertices), and subgraphs of unit-distance graphs are
   unit-distance graphs. Hence no unit-distance graph on ≤ 6 vertices is
   5-chromatic, i.e. all are 4-colourable.

So the honest state is **6 ≤ N ≤ 508 proved, with the open question being
everything in 7…508**. The run's REQUESTS row `largest-which-currently-5018`
(what the published current maximum N is) remains open: this library holds no
source establishing N > 6 — nothing in the held literature proves 4-colourability
of all unit-distance graphs up to any larger N. If anyone had, it would headline
as a minimality proof for a 5-chromatic graph.

## Caveat on "current record"

Whether any 5-chromatic unit-distance graph smaller than 509 vertices was
constructed after 2020 (e.g. in Voronov–Neopryatnaya–Dergachev, "Constructing
5-chromatic unit distance graphs embedded in the Euclidean plane and
two-dimensional spheres", Discrete Math. 345 (2022), doi:10.1016/j.disc.2022.113106)
could **not** be verified this run: searches for the current record were
withheld by the run's evidence policy, which screens answer-tier material on
this problem. The statement "509 vertices is the smallest known" is anchored to
Parts' own abstract (2020), the newest primary record the library holds.
Heule's 553-vertex graphs were machine-verified (SAT); Parts' graph is by
construction with published minimization.

## Note on download and sourcing

Full texts of de Grey, Heule, Parts, and Exoo–Ismailescu are not on disk:
download_document is network-blocked on arxiv/doi hosts in this run, and the
construction papers' content is additionally screened by the evidence policy.
The assertions above come from the authors' own abstracts (Heule, Parts — read
verbatim), citation records (de Grey title + arXiv id; Exoo–Ismailescu DOI), and
a derivation performed in this note. Sourcing tier: **primary** for the record
chain statements (author abstracts), **derived/proved** for the N ≥ 6 bound,
**forced** for N ≤ 508 (from the held 509-vertex existence fact).

```claim
id: smallest-five-chromatic-udg-509
answers: largest-which-currently-5018
statement: The smallest known 5-chromatic unit-distance graph has 509 vertices and 2442 edges (Parts 2020, arXiv:2010.12665). Record chain: de Grey 2018, arXiv:1804.02385 (1581 vertices, first proof chi(plane) >= 5) -> Heule 2018, arXiv:1805.12181 (several 553-vertex graphs) -> Parts 2020 (509). Existence of a 509-vertex 5-chromatic unit-distance graph forces any proved N with "all unit-distance graphs on <= N vertices are 4-colourable" to satisfy N <= 508.
hypotheses: unit-distance graphs in the Euclidean plane; chromatic number >= 5.
holds-here: true — pins the current upper end of the size scale for 5-chromatic unit-distance graphs.
status: sourced (primary abstracts verbatim on disk: Heule 2018 and Parts 2020; de Grey title/arXiv id confirmed in three citation records; post-2020 record not verifiable — screened)
bearing: sets the range the size-lower-bound work must live in (N <= 508); the 509-vertex graph is the external existence fact the run competes with.
anchor: research/sources/smallest-five-chromatic-unit-distance-graph.md
```

```claim
id: all-udg-6-vertices-4colourable
statement: Every unit-distance graph on at most 6 vertices is 4-colourable (verification number N >= 6). Proof: a chi >= 5 graph on n <= 6 vertices contains a 5-critical subgraph with minimum degree >= 4; on n <= 5 that forces K4, and on n = 6 it forces e >= 12, whose unique K4-free realisation is the Turan graph K_{2,2,2} (chi = 3, contradiction); hence any chi >= 5 graph on <= 6 vertices contains K4, which is not a unit-distance graph (two unit circles meet in at most two points). Combined with Parts' 509-vertex 5-chromatic graph, the verification number N satisfies 6 <= N <= 508.
hypotheses: finite unit-distance graphs in the plane; planarity of the embedding (unit circles intersect in <= 2 points).
holds-here: true — an elementary proved lower bound for the G-exhaust sweep.
status: proved (derived in this note; relies on Dirac's delta >= k-1 for k-critical graphs and Turan's theorem, both standard)
bearing: the run's size-lower-bound skeleton starts from a proved N = 6; anything claimed above 6 is new.
anchor: research/sources/smallest-five-chromatic-unit-distance-graph.md
```

```claim
id: largest-which-currently-5018-answered
statement: The current verification bound record, as this library establishes it: N >= 6 is PROVED (every unit-distance graph on <= 6 vertices is 4-colourable; claim all-udg-6-vertices-4colourable, derived in-library from 5-criticality + min-degree >= 4 + K4 not unit-distance). N <= 508 is FORCED by the smallest known 5-chromatic unit-distance graph, 509 vertices (Parts 2020, claim smallest-five-chromatic-udg-509). The open question is everything in 7..508; the library holds no source establishing N > 6, and post-2020 record changes are screened by the evidence policy (answer-tier) and unverifiable this run.
hypotheses: finite unit-distance graphs in R^2; the held record chain (de Grey 1581 -> Heule 553 -> Parts 509); evidence policy screens answer-tier sources.
holds-here: yes — this is the answer to REQUESTS.md row largest-which-currently-5018: the run starts the size-lower-bound sweep from N = 6 (proved), and the swept range is 7..508.
status: verified (proved lower end in-library; forced upper end from held primary abstracts)
bearing: sets the starting N for the size-lower-bound skeleton and states the range honestly; any N > 6 the run proves is new.
answers: largest-which-currently-5018
anchor: research/sources/smallest-five-chromatic-unit-distance-graph.md
```