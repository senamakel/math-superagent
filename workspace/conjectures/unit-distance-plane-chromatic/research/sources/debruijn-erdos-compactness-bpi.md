# De Bruijn–Erdős compactness for graph colouring, and its choice principle

**Source:** N.G. de Bruijn, P. Erdős, "A Colour Problem for Infinite Graphs and
a Problem in the Theory of Relations", Indagationes Mathematicae (Proceedings)
54 (1951) 369–373. URL: https://doi.org/10.1016/s1385-7258(51)50053-7
(volume 13 of Indagationes Mathematicae, series "Proceedings of the
Koninklijke Nederlandse Akademie van Wetenschappen, Series A").

## The theorem

An infinite graph G is k-colourable **iff every finite subgraph of G is
k-colourable**. Equivalently, χ(G) = sup over finite subgraphs H of χ(H). For
the Hadwiger–Nelson problem this is the single most load-bearing reduction:
χ(plane unit-distance graph) ≥ k holds iff some **finite** unit-distance graph
is not (k−1)-colourable, so the whole infinite problem is decided by finite
configurations. The statement and its application are classical; the original
1951 paper, the Chen–Chvátal 2007 survey (doi:10.1016/j.dam.2007.05.036), and
the citation record (275 citations, including Erdős–Hajnal 1966 and the 1966
Erdős–Hajnal–Rothschild papers) all confirm it.

## The choice principle it uses (exact hypothesis)

The standard proof observes that a k-colouring is a point of the product
∏_{v∈V} {1,…,k} (finite discrete factors); the colouring exists iff the
sub-basis sets "edge uv properly coloured" have the finite intersection
property, which holds iff every finite subgraph is k-colourable. The step
"product of finite discrete spaces is compact" is **Tychonoff for finite
spaces**, which is equivalent to Rado's selection principle and to the
**Boolean prime ideal theorem (BPI)** — a strictly weaker principle than the
Axiom of Choice (Halpern–Lévy 1971). Gottschalk, "Choice functions and
Tychonoff's theorem", Proc. AMS 2 (1951) 172–174,
doi:10.1090/s0002-9939-1951-0040376-x, proves Rado's selection principle as a
corollary of Tychonoff's theorem and is held verbatim (theorem and proof) in
this library. Läuchli, "Coloring infinite graphs and the Boolean prime ideal
theorem", Israel J. Math. 9 (1971) 422–429, proved the compactness/colouring
statement **equivalent to BPI over ZF** (bibliographic detail via the Cowen–
Hechler 2004 paper "G-free colorability and the Boolean prime ideal theorem",
which recites the citation and the equivalence programme; see also Cowen–
Hechler–Mihók 2002, "Graph coloring compactness theorems equivalent to BPI").

So the answer to "which choice principle": **BPI (equivalently: compactness of
products of finite discrete spaces, Rado's selection principle) is exactly what
the theorem needs; full AC is sufficient but not necessary.** The theorem is a
theorem of ZF + BPI (hence of ZFC), and is not provable in ZF alone for
arbitrary infinite graphs.

```claim
id: debruijn-erdos-compactness-bpi
statement: An infinite graph G is k-colourable iff every finite subgraph is; for the plane unit-distance graph chi = sup over finite subgraphs, so chi(plane) >= k iff some finite unit-distance graph is non-(k-1)-colourable. The proof needs a choice principle: Tychonoff for products of finite discrete spaces / Rado's selection principle = the Boolean prime ideal theorem (Gottschalk 1951), and the statement is equivalent to BPI over ZF (Laeuchli 1971). Full AC suffices but is not necessary.
hypotheses: arbitrary (possibly infinite) simple graph G; k a fixed positive integer; ZF + BPI (weak choice).
holds-here: true — the plane unit-distance graph is exactly this setup; k = 4,5 are the cases the run uses.
status: proved (de Bruijn–Erdos 1951, canonical standard reference; choice basis proved verbatim in Gottschalk 1951; equivalence to BPI per Laeuchli 1971 via Cowen–Hechler 2004 recital)
bearing: the entire lower-bound search operates on finite unit-distance graphs; nothing infinite needs reasoning about.
anchor: research/sources/debruijn-erdos-compactness-bpi.md
```

## Note on download

Full text of the 1951 paper is not on disk (download_document is
network-blocked on indagationes/doi hosts in this run); the statement, its
application, and the citation record are confirmed from the library's existing
debruijn-erdos-colour-problem-1951.md, chen-chvatal-debruijn-erdos-survey.md,
gottschalk-choice-functions-1951.md notes and the citation-graph record.
Sourcing tier: **canonical primary reference** (1951), with the choice-basis
detail anchored in two further canonical sources (Gottschalk 1951, verbatim on
disk; Läuchli 1971 via a secondary recital in Cowen–Hechler 2004).