> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/L0.0/sudakov-verstraete-sparse-pdf.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/0707.2117 | converted from PDF -->

## What it claims

Let C(G) denote the set of lengths of cycles in a graph G. In the ﬁrst part of this paper,
we study the minimum possible value of |C(G)| over all graphs G of average degree d and girth
g. Erd˝os [8] conjectured that |C(G)| = Ω(
d
⌊(g−1)/2⌋) for all such graphs, and we prove this
conjecture. In particular, the longest cycle in a graph of average degree d and girth g has length
Ω(
d
⌊(g−1)/2⌋)
. The study of this problem was initiated by Ore in 1967 and our result improves
all previously known lower bounds on the length of the longest cycle [7, 11, 21, 24, 25].
Moreover, our bound cannot be improved in general, since known constructions of d-regular
Moore Graphs of girth g have roughly that many vertices. We also show that Ω
(
d
⌊(g−1)/2⌋) is
a lower bound for the number of odd cycle lengths in a graph of chromatic number d and girth
g. Further results are obtained for the number of cycle lengths in H-free graphs of average
degree d.

In the second part of the paper, motivated by the conjecture of Erd˝os and Gy´arf´as [9] (see
also Erd˝os [10]) that every graph of minimum degree at…

o…

## Statements it makes

Theorem 1.1 Let G be a graph of average degree d and girth g. Then C(G) contains Ω(
d⌊(g−1)/2⌋)

Theorem 1.2 Let H be a ﬁxed bipartite graph containing a cycle and let G be an H-free graph
of average degree d. Then there exists a constant t > 1 depending on H such that C(G) contains
Ω(
dt/(t−1)) consecutive even integers. Furthermore, we can take t = r if H is r-half-bounded, and
t = 1 + 1
k−1 if H is a 2k-cycle.

Theorem 1.3 For any inﬁnite increasing sequence σ of positive even integers and for any n-
vertex graph G, if G contains no σ-cycle, then G has average degree at most

Corollary 1.4 Let σ denote an inﬁnite increasing exponentially bounded sequence of positive even
integers. Then any n-vertex graph with no σ-cycles has average degree exp(O(log*n)).

Lemma 2.1 Let G be a graph of girth g and minimum degree at least 6(d + 1). Then, for every
X ⊂ V (G) of size at most 1
3 d⌊(g−1)/2⌋,
 |∂X| > 2|X|.

Theorem 2.2 For any graph G of girth g and average degree 48(d + 1), |C(G)| ≥ 1
8 d⌊(g−1)/2⌋.

Lemma 2.3 Let G be a graph of average degree 48(d + 1) and girth g, where d⌊(g−1)/2⌋ ≥ 6. Then
G contains a θ-graph containing a cycle of length at least d⌊(g−1)/2⌋ + 2.

Lemma 2.4 Let Γ be a θ-graph and let (A, B) be a nontrivial partition of V (Γ). Then Γ contains
AB-paths of all lengths less than |V (Γ)| unless Γ is bipartite with bipartition (A, B).

Lemma 2.5 Let H be a minimal d-chromatic graph, where d ≥ 3. Then for any distinct vertices
u, v ∈ V (H), there is a uv-path of odd length in H and a uv-path of even length in H.

Lemma 2.6 Let H be a minimal d-chromatic graph, where d ≥ 3. Then for any even cycle
C ⊂ H, there is an odd θ-graph in H containing C.

Theorem 2.7 Let G be a graph of chromatic number d and girth g. Then C(G) contains
Ω(
d⌊(g−1)/2⌋) consecutive integers.

Lemma 3.1 Let P be a monotone property of graphs, and suppose that for every graph G ∈ P
with minimum degree d, and every set X ⊂ V (G) of size at most f (d),

Lemma 3.2 Let a > 0, 1
2 < b < 1 be reals such that for any positive integer n, ex(n, H) ≤ an2b.
Then, for any H-free graph G of minimum degree at least 18ad, and any subset X of vertices of
G of size at most d1/(2b−1), |∂X| > 2|X|.
 8

Claim 4.1 Let (ai)i≥1 be positive real numbers such that a1 = 4π(1) and, for all i ≥ 2,

*[digest of a 33153 character source; every section, statement, and proof in full at `research/L0.0/sudakov-verstraete-sparse-pdf.full.md`]*
