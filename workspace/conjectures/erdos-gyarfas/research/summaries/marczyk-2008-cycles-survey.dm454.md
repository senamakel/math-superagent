> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/marczyk-2008-cycles-survey.dm454.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://web.archive.org/web/2024/https://www.impan.pl/shop/publication/transaction/download/product/88171 | converted from PDF -->

## What it claims

Our aim is to survey results in graph theory centered around four themes: hamiltonian graphs,
pancyclic graphs, cycles through vertices and the cycle structure in a graph. We focus on problems
related to the closure result of Bondy and Chv´atal, which is a common generalization of two
fundamental theorems due to Dirac and Ore. We also describe a number of proof techniques in
this domain. Aside from the closure operation we give some applications of Ramsey theory in
the research of cycle structure of graphs and present several methods used in the study of the
structure of the set of cycle lengths in a hamiltonian graph.

2000 Mathematics Subject Classiﬁcation: 05C45, 05C38, 05C35.
Key words and phrases: cycles, paths, hamiltonian graphs, traceable graphs, pancyclic graphs,
toughness, claw-free graphs, closure, cyclability, pancyclability, arbitrarily vertex decompos-
able graphs, maximal common subgraph.
Received 12.10.2007; revised version 10.12.2007.

[4]

1. Introduction

The purpose of this paper is twofold: to survey the progress in results that deal with
cycle structures of…

[5…

## Statements it makes

Theorem 3.1 (Dirac [101]). Let G = (V, E) be a graph on n vertices, where n ≥ 3. If
δ(G) ≥ n/2, then G is hamiltonian.

Corollary 3.2. If δ(G) ≥ (n − 1)/2, where n is the order of G, then G contains a
hamiltonian path.

Theorem 3.3. Let G be a 2-connected graph on n ≥ 3 vertices. Then G contains either
a cycle of length at least 2δ(G) or a hamiltonian cycle.

Theorem 3.4. Let r ≥ 3 be an integer and let G be a 2-connected nonbipartite graph on
n ≥ 2r vertices such that δ(G) ≥ r. Then G contains both an odd cycle of length at least
2r − 1 and an even cycle of length at least 2r.

Theorem 3.5. Let k ≥ 431 and G be a 2-connected graph of order n with at least n
2 + k
vertices of degree at least k. Then G contains either a cycle of length at least 2k or a
hamiltonian cycle.

Theorem 3.6. Let G be a graph of order n and minimum degree δ = δ(G) < n/2. If
|{v ∈ V (G) | d(v) < n/2}| ≤ δ − 1, then G is hamiltonian.

Theorem 3.7. Let s be a positive integer and G a simple graph of order n ≥ 3 and
minimum degree δ, where δ ≥ n/(s + 1). Then G contains a cycle of length at least n/s.

Theorem 3.8 (Ore [227]). If a graph G on n ≥ 3 vertices is such that d(x) + d(y) ≥ n
for every pair x, y of nonadjacent vertices, then G is hamiltonian.

Corollary 3.9. Let G be a graph of order n ≥ 3 and x1, . . . , xn a hamiltonian path in
G such that d(x1) + d(xn) ≥ n and x1xn /∈ E(G). Then G is hamiltonian.

Corollary 3.10. If G is a graph of order n such that d(x) + d(y) ≥ n − 1 for any pair
of nonadjacent vertices x and y, then G contains a hamiltonian path.

Theorem 3.11. If dk > k for 1 ≤ k < (n − 1)/2 and d(n−1)/2 > (n − 1)/2, if n is odd,
then G is hamiltonian.

Theorem 3.12. If dj + dk ≥ n ≥ 3 for all pairs j, k with j < k, dj ≤ j, dk ≤ k − 1, then
G is hamiltonian.

Theorem 3.13. If n ≥ 3 and dn−k ≥ n − k for all k with dk ≤ k < n/2, then G is
hamiltonian.

Theorem 3.14. If there exists a labeling v1, . . . , vn of the vertices such that j < k,
k ≥ n − j, vkvj /∈ E(G), d(vj) ≤ j and d(vk−1) ≤ k − 1 implies d(vj) + d(vk) ≥ n, then
G is hamiltonian.

Theorem 3.15. If a graph G of order n ≥ 3 is such that d(x) + d(y) ≥ n + 1 for every
pair x, y of nonadjacent vertices, then G is hamiltonian-connected.

Corollary 3.16. If G is a graph of order n ≥ 3 with δ(G) ≥ (n + 1)/2, then G is
hamiltonian-connected.

Theorem 3.17. Let G be a connected graph of order n ≥ 3 such that d(x) + d(y) ≥ d for
any pair x, y of nonadjacent vertices. If d < n then G contains a path of length at least
d and if d ≥ n, then G is hamiltonian.

Theorem 3.18. Let G be a 2-connected graph such that d(x) + d(y) ≥ d for any pair
x, y of nonadjacent vertices. Then G contains either a cycle of length at least d or a
hamiltonian cycle.

Theorem 3.19. Let G be a graph of order n with minimum degree δ. If n2(G) < g(n, δ),
then G is hamiltonian.

Theorem 3.20. Let G be a 2-connected graph of order n such…

P…


*[further statements in the full text]*

*[digest of a 271889 character source; every section, statement, and proof in full at `research/sources/marczyk-2008-cycles-survey.dm454.full.md`]*
