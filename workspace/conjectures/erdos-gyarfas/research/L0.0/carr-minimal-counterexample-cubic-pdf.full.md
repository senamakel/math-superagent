<!-- source: https://arxiv.org/pdf/2605.22844 | converted from PDF -->

Every Minimal Counterexample to the Erd˝os–Gy´arf´as Conjecture is
Predominantly Cubic

Avery Carr
Independent Researcher
avery.carr@ymail.com

Updated: May 13, 2026

Abstract

A minimal counterexample to the Erd˝os–Gy´arf´as conjecture is a graph of minimum possible
order and size with minimum degree at least 3 that contains no cycle whose length is a power
of 2. Markstr¨om observed that any such graph must contain an independent set of vertices of
degree at least 4 together with a nonempty set of vertices of degree exactly 3. As an immediate
consequence, every regular minimal counterexample must be cubic. Building on this structure,
two additional consequences are derived. First, every vertex of a minimal counterexample is
adjacent to a vertex of degree exactly 3. Second, at least 4/7 of the vertices of any minimal
counterexample must have degree exactly 3.

Keywords: Erd˝os–Gy´arf´as conjecture, cycles of power-of-two length, cubic graphs, minimal coun-
terexamples, graph structure, extremal graph theory

Mathematics Subject Classification: 05C38, 05C35, 05C75

Notation

All graphs considered in this note are finite, simple, and undirected. Let G = (V (G), E(G)) be a
graph with vertex set V (G) and edge set E(G). For a vertex v ∈ V (G), the neighborhood of v is

N (v) = {u ∈ V (G) : uv ∈ E(G)},

and the degree of v is d(v) = |N (v)|.

The minimum degree of G is denoted by

δ(G) = min{d(v) : v ∈ V (G)}.

A graph H is a proper subgraph of G if H ⊊ G. A graph G is called k-regular if every vertex
of G has degree k. A cubic graph is a 3-regular graph.
In this note, a minimal counterexample to the Erd˝os–Gy´arf´as conjecture means a graph G with
δ(G) ≥ 3 that contains no cycle whose length is a power of 2, chosen with minimum possible order
and, subject to that, minimum possible size.
 1arXiv:2605.22844v1  [math.CO]  13 May 2026
Introduction

The Erd˝os–Gy´arf´as conjecture asks whether every graph G with minimum degree δ(G) ≥ 3 contains
a cycle whose length is a power of two [1]. Despite its simple formulation, the conjecture remains
open in general and has only been verified for restricted graph classes, including planar graphs, cubic
claw-free graphs, 3-connected cubic planar graphs, P8-free graphs, and P10-free graphs [2, 3, 4, 5, 6].
Computational work of Royle and Markstr¨om further suggests that any counterexample must
be highly constrained. In particular, their investigations imply that any cubic counterexample must
contain at least 30 vertices, while extremal constructions show that the smallest power-of-two cycle
lengths can first occur at comparatively large values such as 16 [7].
Recent work of the author establishes the conjecture for graphs of diameter 2, proving that
every graph G with diam(G) = 2 and δ(G) ≥ 3 contains a cycle of length 4 or 8 [8]. Motivated by
the increasingly rigid structure expected of minimal counterexamples, this note studies structural
restrictions on such graphs.

Main Result

Lemma 0.1. Let G be a minimal counterexample to the Erd˝os–Gy´arf´as conjecture. Then δ(H) ≤ 2
for every proper subgraph H ⊊ G.

Proof. Let G be a minimal counterexample with respect to order and size, and suppose H ⊊ G is
a proper subgraph with δ(H) ≥ 3. By minimality of G, the graph H cannot be a counterexample.
Hence, H contains a cycle whose length is a power of 2. Since H is a subgraph of G, the same
cycle occurs in G, contradicting that G is a counterexample. Therefore, δ(H) ≤ 2 for every proper
subgraph H ⊊ G.

The following corollaries and theorem strengthen the structural picture first described by Mark-
str¨om [7]. In particular, Corollary 0.1(1) shows that the cubic vertices form a dominating set in
every minimal counterexample. Corollary 0.1(2), originally observed by Markstr¨om [7], states that
the vertices of degree at least 4 form an independent set. Theorem 0.1 then uses this structural
restriction to establish an explicit lower bound on the proportion of cubic vertices.

Corollary 0.1. Let G be a minimal counterexample to the Erd˝os–Gy´arf´as conjecture.

1. Every vertex of G is adjacent to a vertex of degree exactly 3.

2. The set of vertices of degree at least 4 forms an independent set.

Proof. (1) Let v ∈ V (G). Since G − v is a proper subgraph of G, Lemma 0.1 gives δ(G − v) ≤ 2.
Since every vertex of G has degree at least 3, the only way a vertex in G − v can have degree at
most 2 after deleting v is if it was adjacent to v and had degree exactly 3 in G. Therefore, v is
adjacent to a vertex of degree exactly 3.

(2) Suppose u, v ∈ V (G) are adjacent vertices with d(u) ≥ 4 and d(v) ≥ 4. Deleting the edge
uv decreases both degrees by exactly 1, so both vertices retain degree at least 3, while all other
vertex degrees remain unchanged. Hence δ(G − uv) ≥ 3, contradicting Lemma 0.1. Therefore, no
two vertices of degree at least 4 can be adjacent.

2

v w

v1 v2 vk−1 w1 w2 wk−1
· · · · · ·

Figure 1: An edge vw in a k-regular graph, where k ≥ 4. Each endpoint has k − 1 ≥ 3 other
incident edges.
 v w

v1 v2 vk−1 w1 w2 wk−1
· · · · · ·

dG−vw(v) = dG−vw(w) = k − 1 ≥ 3

Figure 2: After deleting the edge vw, the vertices v and w still have degree at least 3, while all
other vertices retain their original degrees. Hence δ(G − vw) ≥ 3.

Corollary 0.2. If G is a regular minimal counterexample to the Erd˝os–Gy´arf´as conjecture, then
G is cubic.

Proof. Suppose G is k-regular. Since δ(G) ≥ 3, one has k ≥ 3. If k ≥ 4, then every vertex has
degree at least 4, contradicting Corollary 0.1(2). Therefore k = 3, and hence G is cubic.

Theorem 0.1. Let G be a minimal counterexample to the Erd˝os–Gy´arf´as conjecture. Then at least
4/7 of the vertices of G have degree exactly 3.

Proof. Let V3 = {v ∈ V (G) : d(v) = 3}

and V≥4 = {v ∈ V (G) : d(v) ≥ 4}.

By Corollary 0.1(2), the set V≥4 is independent. Hence every edge incident to a vertex of V≥4
joins it to a vertex of V3.
Let e(V3, V≥4) denote the number of edges between the two sets. Since every vertex in V≥4 has
degree at least 4, one has e(V3, V≥4) ≥ 4|V≥4|.

On the other hand, every vertex in V3 has degree exactly 3, so

e(V3, V≥4) ≤ 3|V3|.

Therefore, 4|V≥4| ≤ 3|V3|.

Since V (G) = V3 ∪ V≥4, it follows that

|V (G)| = |V3| + |V≥4| ≤ |V3| + 3
4 |V3| = 7
4 |V3|.

3

Hence,
 |V3| ≥ 4
7 |V (G)|.

Thus at least 4/7 of the vertices of G have degree exactly 3.

Acknowledgments

The author would like to thank Klas Markstr¨om for prior structural observations related to min-
imal counterexamples to the Erd˝os–Gy´arf´as conjecture, as well as the editors for their time and
consideration.

References

[1] P. Erd˝os, Some old and new problems in various branches of combinatorics, Discrete Math.
165/166 (1997), 227–231.

[2] D. Daniel and S. E. Shauger, A result on the Erd˝os–Gy´arf´as conjecture in planar graphs,
Congressus Numerantium 153 (2001), 129–139.

[3] P. Salehi Nowbandegani, H. Esfandiari, M. H. Shirdareh Haghighi, and K. Bibak, On the
Erd˝os–Gy´arf´as conjecture in claw-free graphs, Discuss. Math. Graph Theory 34 (2014), 635–
640.

[4] C. C. Heckman and R. Krakovski, Erd˝os–Gy´arf´as conjecture for cubic planar graphs, Electronic
J. Combin. 20(2) (2013), #P7.

[5] Y. Gao and S. Shan, Erd˝os–Gy´arf´as conjecture for P8-free graphs, Graphs and Combinatorics
38 (2022), Article 168.

[6] Z. Hu and C. Shen, The Erd˝os–Gy´arf´as conjecture holds for P10-free graphs, Discrete Mathe-
matics 347 (2024), 114175.

[7] K. Markstr¨om, Extremal graphs for some problems on cycles in graphs, Congressus Numeran-
tium 171 (2004), 177–188.

[8] A. Carr, Cycles of Length 4 or 8 in Graphs with Diameter 2 and Minimum Degree
at Least 3, Bull. Inst. Combin. Appl. 109 (February 2027), to appear. Available at:
https://arxiv.org/abs/2508.19302.
 4
