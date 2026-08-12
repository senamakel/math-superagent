<!-- source: https://arxiv.org/pdf/2601.13552 | converted from PDF -->

Dean’s conjecture and cycles modulo k

Yufan Luo
1 Jie Ma1,2 Ziyuan Zhao1

Abstract

Dean conjectured three decades ago that every graph with minimum degree at least k ≥ 3
contains a cycle whose length is divisible by k. While the conjecture has been verified for
k ∈ {3, 4}, it remains open for k ≥ 5. A weaker version, also proposed by Dean, asserting
that every k-connected graph contains a cycle of length divisible by k, was resolved by Gao,
Huo, Liu, and Ma [16] using the notion of admissible cycles.
In this paper, we resolve Dean’s conjecture for all k ≥ 6. In fact, we prove a stronger
result by showing that every graph with minimum degree at least k contains cycles of length
r (mod k) for every even integer r, unless every end-block belongs to a specific family of
exceptional graphs, which fail only to contain cycles of length 2 (mod k). We also estab-
lish a strengthened result on the existence of admissible cycles. Our proof introduces two
sparse graph families, called trigonal graphs and tetragonal graphs, which provide a flexible
framework for studying path and cycle lengths and may be of independent interest.

1 Introduction

The study of cycle lengths in graphs is a central and classical theme in graph theory; see [6, 27]
for comprehensive treatments. A particularly interesting problem in this area concerns the
existence of cycles whose lengths are divisible by a given integer k; see, for example, [1,9,25,26].
The present work is motivated by the following beautiful conjecture of Dean (see Conjecture 7.4
in [6]), which has remained open for three decades.

Conjecture 1.1 (Dean’s conjecture). For every integer k ≥ 3, every graph with minimum degree
at least k contains a cycle of length divisible by k.

The minimum degree condition in Conjecture 1.1 is best possible, as complete bipartite
graphs Kk−1,n for odd k and n ≥ k − 1 show that it cannot be weakened to k − 1. The
conjecture has been verified for k = 3 and k = 4 by Chen and Saito [7] and by Dean, Lesniak,
and Saito [11], respectively, but remains open for all k ≥ 5. A weaker version, also proposed by
Dean [9], asserting that every k-connected graph contains a cycle of length divisible by k, was
resolved by Gao, Huo, Liu, and Ma [16] via a unified approach to related cycle problems.
In this paper, we prove Conjecture 1.1 for all k ≥ 6. To state our main result, let Hk denote
the family of all graphs Hk,n;t, where 2 ≤ t ≤ k < n, obtained from the complete bipartite graph
Kk,n by deleting k − t edges incident to a single vertex in the part of size n.

Theorem 1.2 (Main Theorem). For every integer k ≥ 6, let G be a graph with minimum degree
at least k. Then exactly one of the following holds:

(1) G contains a cycle of length r (mod k) for every even integer r;

(2) k is odd, every end-block of G is isomorphic to a graph in {Kk+1, Kk,k} ∪ Hk, and every
non-end-block contains no cycle of length 2 (mod k);

(3) k is even, every end-block of G is isomorphic to Kk+1, and every non-end-block contains
no cycle of length 2 (mod k).

1School of Mathematical Sciences, University of Science and Technology of China, Hefei 230026, China.
2Yau Mathematical Sciences Center, Tsinghua University, Beijing 100084, China.

1arXiv:2601.13552v1  [math.CO]  20 Jan 2026
Observe that every graph in {Kk+1, Kk,k} ∪ Hk contains cycles of all even lengths modulo k,
with the sole exception of length 2 (mod k). Consequently, we obtain the following immediate
corollary, which resolves Conjecture 1.1 affirmatively for all k ≥ 6.1

Corollary 1.3. Let k ≥ 6 be an integer. Then for every even integer r ̸≡ 2 (mod k), every
graph with minimum degree at least k contains a cycle of length r (mod k).

The general study of cycle lengths modulo k dates back to the 1970s, initiated by the work
of Burr and Erd˝os [14]. For integers ℓ and k with even integers in the residue class ℓ (mod k),
let cℓ,k denote the smallest constant c such that every n-vertex graph with at least cn edges
contains a cycle of length ℓ (mod k). Erd˝os [14] conjectured that cℓ,k exists for all ℓ when k is
odd, and this was later confirmed by Bollob´as [4]. Thomassen [24] further improved the bound
to cℓ,k ≤ 4k(k + 1) for all integers k and even ℓ. In a subsequent work [25], Thomassen provided
a polynomial-time algorithm for finding a cycle of length divisible by k. Resolving a conjecture
of Thomassen [24], Gao, Huo, Liu, and Ma [16] showed that for any k ≥ 3, every graph with
minimum degree at least k + 1 contains cycles of all even lengths modulo k (the case of even
k was previously proved in [22]). From an extremal perspective, Sudakov and Verstra¨ete [23]
established a striking relation that for all 3 ≤ ℓ < k, the constant cℓ,k is upper bounded by the
k-vertex Tur´an number of Cℓ. To date, exact values of cℓ,k are known for very few pairs (ℓ, k);
we refer to [3, 7, 10, 18, 19]. Diwan [13] extended this study to weighted graphs.
An effective approach to obtaining cycles with prescribed residues is to find a collection of
admissible cycles, where the lengths of the cycles (or paths) form an arithmetic progression with
common difference 1 or 2. This notion was first introduced in [16] and has since been applied
in a number of works on cycle length problems; see, for example, [8, 17, 18, 20, 21]. A central
result in this line of research, conjectured by Liu and Ma [22] and proved by Gao et al. [16],
asserts that every graph with minimum degree at least k + 1 contains k admissible cycles. We
generalize this result by relaxing the minimum degree condition for all integers k ≥ 7.

Theorem 1.4. Let k ≥ 7 and let G be a graph with minimum degree at least k. Then G contains
k admissible cycles, unless every end-block of G is isomorphic to a graph in {Kk+1, Kk,k} ∪ Hk.

Our proofs employ several novel techniques, distinct from those in [16,22], as discussed below.

Proof Overview and New Tools. Our proof builds upon the approach of Gao et al. [16],
which refine earlier results of Fan [15] and Liu–Ma [22]. Specifically, the idea is to find a collection
of k admissible paths between any two given vertices x, y in a suitable 2-connected graph G.
The key step is to identify a specified subgraph H (called the core subgraph) such that, for some
positive integer t, the following typically hold:

(a) the core subgraph H satisfies a robust spreading property, namely, H contains t admissible
paths between many pairs of vertices; and

(b) the graph obtained from G by contracting or deleting V (H) satisfies suitable minimum
degree conditions and yields k +1−t admissible paths between prescribed pairs of vertices.

By concatenating these paths appropriately, one obtains the desired k admissible paths in G.
In all previous works, such as Gao et al. [16], the core subgraphs were typically dense struc-
tures: either complete graphs, complete bipartite graphs, or graphs closely resembling them.
The main technical contribution of this work is to go beyond this paradigm by introducing two
new families of core graphs that can be very sparse (with average degree at most four; they
can even be outer-planar) while still satisfying properties (a) and (b). We call these families
trigonal graphs and tetragonal graphs, which handle the non-bipartite and bipartite cases, re-
spectively; a detailed discussion is provided in Section 3. We would like to point out that the
high-connectivity condition was essential in the proof of the weaker version of Dean’s conjecture
in [16]. Owing to their sparsity, these core subgraphs can be found in graphs with lower con-
nectivity, providing the crucial ingredient for our proof. We believe that these two families are
of independent interest and may also find applications in related problems.

1The case k = 5 requires separate arguments and we will address this special case in forthcoming work.

2

A Related Result. During a conference in Xi’an in June 2025, we learned that Bai, Grzesik,
Li, and Prorok [2] independently obtained results related to our Theorems 1.2 and 1.4. More
precisely, among other results, they [2] proved corresponding versions of Theorems 1.2 and 1.4
under the additional assumption that the graph is 2-connected, for every integer k ≥ 4. Their
proofs are mainly based on the approach of Gao et al. [16]. Beyond the difference in proofs, we
would like to emphasize that, in order to derive Conjecture 1.1, it is crucial to establish results
of the type given in our main theorem that remove any connectivity assumption.

Paper Organization. The remainder of this paper is organized as follows. In Section 2, we
present the necessary definitions and preliminary results. Section 3 introduces two key families
of graphs, namely trigonal graphs and tetragonal graphs, and establishes properties of paths
within them. In Section 4, we introduce k-weak graphs, reduce the proof of Theorem 1.2 to this
class (see Theorem 4.2), and establish several structural lemmas. The proof of Theorem 4.2 is
then split between Sections 5 and 6, according to whether the host graph is non-bipartite or
bipartite. At the end of Section 6, we also prove Theorem 1.4.

2 Preliminaries

2.1 Notations

All graphs in this paper are finite, undirected, and simple. We use standard graph theory
notation and terminology; see [12]. The set of neighbors of a vertex v in G is denoted by NG(v),
and the degree of v is denoted by degG(v) = |NG(v)|. For A, B ⊆ V (G) and v ∈ V (G), we
denote by NA(v) = NG(v) ∩ A, NA(B) = ⋃b∈B NA(b) and degA(v) = |NA(v)|, where we omit
the subscript G, as the host graph G will be clear in the context. For a subgraph H ⊆ G, we
simplify NV (H)(v) to NH (v) and degV (H)(v) to degH (v). For a positive integer k, we write δk(G)
for the k-th minimum degree of G, and abbreviate the minimum degree δ1(G) to δ(G). Recall
the collection of graphs Hk = {Hk,n;t : 2 ≤ t ≤ k < n}, we have δ(Hk,n;t) = t, δ2(Hk,n;t) = k,
and Hk,n;k ≃ Kk,n. For U ⊆ V (G), G[U ] denotes the subgraph of G induced by U , and let
G − U := G[V (G) \ U ]. If U = {u}, we write G − u for G − {u}. We say that a graph
G′ is obtained from G by contracting U into a vertex u if V (G′) = (V (G) \ U ) ∪ {u} and
E(G′) = E(G − U ) ∪ {uv : v ∈ NG(U )}.
We say that a vertex v ∈ V (G) is a cut-vertex of G if G − v contains more components than
G. A block in G is a maximal connected subgraph that has no cut-vertex of its own (i.e., it is
a maximal 2-connected subgraph, a bridge, or an isolated vertex). An end-block of G is a block
containing at most one cut-vertex of G. Note that if a connected graph G of order at least three
is not 2-connected, then G contains at least two end-blocks.
For two positive integers k ≤ ℓ, we define [k, ℓ] = {k, k + 1, . . . , ℓ} and [k] = [1, k]. For two
integer sets X and Y , we denote their set addition by X + Y := {x + y : x ∈ X, y ∈ Y }. We also
write k + X := {k + x : x ∈ X}. Given two vertex subsets A, B ⊆ V (G), a path P = x1 · · · xt in
G is called an (A, B)-path if V (P ) ∩ A = {x1} and V (P ) ∩ B = {xt}. If an (A, B)-path consists
of a single edge, we call it an (A, B)-edge; we write E(A, B) for the set of all (A, B)-edges.
We abbreviate ({a}, B)-paths to (a, B)-paths and (V (H), B)-paths to (H, B)-paths if H is a
subgraph of G. For a subgraph H ⊆ G and distinct vertices u, v ∈ V (G), we write P H
u,v for the
set of all (u, v)-paths whose internal vertices belong to H, and LH
u,v for the set of lengths of these
paths. For vertices x, y ∈ V (H), let distH (x, y) denote the length of a shortest (x, y)-path in H.
For distinct vertices u, v ∈ V (G), let G + uv (resp. G − uv) denote the graph with vertex
set V (G) and edge set E(G) ∪ {uv} (resp. E(G) \ {uv}). We refer to the triple (G, u, v) as a
rooted graph to implicitly fix two distinct vertices u, v ∈ V (G). The minimum degree of a rooted
graph (G, u, v), denoted by δ(G, u, v), is the minimum degree in G of vertices in V (G) \ {u, v}.
The second minimum degree, δ2(G, u, v), is defined analogously. We say that the rooted graph
(G, u, v) is 2-connected if G + uv is 2-connected. For a connected graph M and a block B of
M , we write Cut(B) for the set of cut-vertices of M contained in B; we typically omit the
notation for M when it is clear from the context. For brevity, we write a k-AP for an arithmetic

3

progression with common difference k.
We will frequently use the notions of consecutive and admissible sets for integers, paths, and
cycles, which we now define formally.

Definition 2.1. A set of integers is called consecutive (resp. admissible) if its elements form
a 1-AP (resp. 1-AP or 2-AP). A family of paths or cycles in a graph G is called consecutive
(resp. admissible) if the set of their lengths is consecutive (resp. admissible).

Throughout, we use the following basic fact to estimate the size of an admissible or consec-
utive cycle family obtained by concatenating paths from two path families.

Observation 2.2. Let X and Y be admissible integer sets of size s and t, respectively. Then:

(1) X + Y is admissible and has size at least s + t − 1.

(2) If either X or Y is consecutive, then so is X + Y .

(3) If X is a 2-AP, Y is consecutive, and t ≥ 2, then X + Y is of size at least 2s + t − 2.

2.2 Some useful lemmas

We use the following result by Chiba and Yamashita [8], which provides a sufficient condition
for the existence of k admissible paths in a 2-connected rooted graph.

Lemma 2.3. ([8]) Let k be a positive integer. If (G, x, y) is a 2-connected rooted graph with
|G| ≥ 4 and δ2(G, x, y) ≥ k + 1, then there exist k admissible (x, y)-paths in G.

Using this lemma, Chiba and Yamashita proved the following theorem on admissible cycles.

Theorem 2.4. ([8]) For any integer k ≥ 2, every graph G on at least three vertices, having at
most two vertices of degree less than k + 1, contains k admissible cycles.

We then present a technical lemma regarding the distance between neighbors of vertices on
a cycle. This result operates independently in general graphs but is essential for linking paths
to the core subgraphs in the subsequent sections.

Lemma 2.5. Let C be a cycle of length s ≥ 3 in graph G, and let u1, u2 ∈ V (G − C) be two
distinct vertices such that degC(u1) > 0 and degC(u2) > 0. If neither NC(u1) nor NC(u2)
contains two consecutive vertices of C, then the following statements hold.

(1) If NC(u1) ∩ NC(u2) = ∅, then there exist v1 ∈ NC(u1) and v2 ∈ NC(u2) such that 1 ≤
distC(v1, v2) ≤ max{1, ⌊s/2⌋ + 2 − degC(u1) − degC(u2)};

(2) If degC(u1) ≥ 2, then there exist v1 ∈ NC(u1) and v2 ∈ NC(u2) such that 1 ≤
distC(v1, v2) ≤ max{3, s/ degC(u1), ⌊s/2⌋ + 3 − degC(u1) − degC(u2)}.

Proof. Let ℓ := min{distC(v1, v2) : v1 ∈ NC(u1), v2 ∈ NC(u2), v1 ̸= v2}. Since distC(v1, v2) ≤
s/2 for any pair v1, v2, it suffices to prove the result assuming degC(u1)+degC(u2) ≥ 3 and ℓ ≥ 2.
Color the vertices in NC(u1) red and those in NC(u2) blue; vertices in NC(u1) ∩ NC(u2) receive
both colors. These colored vertices divide C into t := |NC(u1) ∪ NC(u2)| subpaths P1, . . . , Pt.
Note that the endpoints of each path are colored, while their internal vertices are uncolored.
Since neither NC(u1) nor NC(u2) contains consecutive vertices, e(Pi) ≥ 2 if the endpoints share
a color; otherwise, e(Pi) ≥ ℓ by the definition of ℓ.
Firstly, consider (1). Suppose NC(u1) ∩ NC(u2) = ∅; then t = degC(u1) + degC(u2) ≥ 2.
Since there are at least two Pi whose endpoints have different colors, it follows that s = |C| =∑
i∈[t] e(Pi) ≥ (t − 2) · 2 + 2 · ℓ (using ℓ ≥ 2). Hence ℓ ≤ s/2 + 2 − t, as desired.
It remains to consider (2). We may assume that NC(u1) ∩ NC(u2) ̸= ∅ and ℓ ≥ 4. Let
r := |NC(u1) ∩ NC(u2)| ≥ 1, i.e., there are r vertices colored both red and blue. Then t + r =
degC(u1) + degC(u2). Let p be the number of subpaths Pi that have at least one endpoint
in NC(u1) ∩ NC(u2). Note that each of such paths is of length at least ℓ. Since each of the

4

T3 T4 T5 T6

a3
 b3
 x3
 a4 b4

x4
 a5

b5

x5

Figure 1: Trigonal graphs

r common neighbors is an endpoint of exactly two such subpaths, and each of such path Pi
contains at most two endpoints in NC(u1) ∩ NC(u2), it follows that p ≥ r. Equality holds if and
only if NC(u1) = NC(u2).
If NC(u1) = NC(u2), then degC(u1) = degC(u2) = r and s = |C| ≥ r · ℓ, implying ℓ ≤ s/r =
s/ degC(u1). Otherwise, we have p ≥ r + 1. Since C is split into subpaths P1, . . . , Pt, where
t ≥ degC(u1) ≥ 2. Note that at least p of such paths have lengths no less than ℓ. Hence,

s = |C| ≥ p · ℓ + (t − p) · 2

= (ℓ − 2)p + 2(degC(u1) + degC(u2) − r)

≥ (ℓ − 2)(r + 1) + 2(degC(u1) + degC(u2) − r)

≥ (ℓ − 4)r + (ℓ − 2) + 2(degC(u1) + degC(u2))

≥ (ℓ − 4) + (ℓ − 2) + 2(degC(u1) + degC(u2)).

Therefore, ℓ ≤ s/2 + 3 − degC(u1) − degC(u2), completing the proof of (2).

3 The core subgraphs: trigonal and tetragonal graphs

In this section, we introduce two graph families: trigonal graphs and tetragonal graphs. These
structures provide the framework for constructing the core subgraphs in our proof. Each graph
in these families is equipped with a specific Hamiltonian cycle, referred to as its boundary cycle.
The defining characteristic of these graphs is the rich structure of path lengths between their
vertices. Specifically, we establish that the set of path lengths between any pair of vertices
forms a long arithmetic progression with common difference 1 or 2 (i.e., an admissible set). This
flexibility is the cornerstone of our main proof, enabling us to construct cycles of desired residues
modulo k when combined with paths from the remainder of the graph.

3.1 Trigonal graphs

Definition 3.1 (Trigonal graph). A trigonal graph T is a non-bipartite outer-planar graph
equipped with a Hamiltonian cycle ∂T , defined as the final graph Tn (with ∂T = ∂Tn) of a finite
sequence of trigonal graphs T3, T4, . . . , Tn that satisfies the following properties:

• T3 ≃ K3 and ∂T3 = T3.

• For every 3 ≤ i ≤ n − 1, Ti+1 is obtained from Ti by adding a new vertex xi and a path
Pi := aixibi where aibi ∈ E(∂Ti); ∂Ti+1 is obtained from ∂Ti by adding the path Pi and
deleting the edge aibi.

By definition, a trigonal graph is exactly an outer-planar graph in which every inner face is a
triangle. We refer to Figures 1 and 2 for examples of trigonal graphs. The black lines represent
the boundary cycle. In each step, Ti+1 is obtained from Ti by replacing the boundary edge aibi
of ∂Ti with the path aixibi. The following proposition ensures the existence of consecutive path
lengths between two vertices at a given distance on ∂T .

5

t = 3 t = 4 t = 5

t = 6, case I t = 6, case II t = 6, case III

w1 w2
 w3

w4w5

w6

Figure 2: All trigonal graphs on at most six vertices

Proposition 3.2. Let T be a trigonal graph with |T | = t, and let u, v be two distinct vertices
of V (T ) with dist∂T (u, v) = d, then [d, t − d] ⊆ LT
u,v. In particular, if uv ∈ E(∂T ), then
[1, t − 1] ⊆ LT
u,v.

Proof. We proceed by induction on t. The base case t = 3 is trivial. Assume that the proposition
holds for every trigonal graph of order at most k for some k ≥ 3. Suppose that |T | = t = k+1 ≥ 4.
It is clear that {d, k + 1 − d} ⊆ LT
u,v.
If degT (u) ≥ 3 or degT (v) ≥ 3, then there exists a vertex w ∈ V (T ) \ {u, v} such that
degT (w) = 2. Let T ′ := T − w. Then T ′ is a trigonal graph of order k and dist∂T ′(u, v) ≤ d. By
the induction hypothesis,

L
T
u,v ⊇ {d, k + 1 − d} ∪ LT ′
u,v ⊇ {d, k + 1 − d} ∪ [d, k − d] = [d, k + 1 − d].

Otherwise, we must have degT (u) = degT (v) = 2. By the recursive construction of trigonal
graphs, every edge on ∂T belongs to a triangle in T . Hence, u and v cannot be adjacent on ∂T , as
otherwise T ≃ K3, contradicting that t = k + 1 ≥ 4. Thus, d = dist∂T (u, v) ≥ 2. Let u′ ∈ V (T )
be a vertex satisfying dist∂T (u, u′) = 1 and dist∂T (v, u′) = d − 1. Note that T ′ = T − {u} is a
trigonal graph on k vertices. The induction hypothesis yields [d − 1, k − (d − 1)] ⊆ LT ′
v,u′. Hence,

L
T
u,v ⊇ (L
T ′
v,u′ + 1) ⊇ [d, k + 1 − d].

This completes the induction proof.

In particular, applying Proposition 3.2 to uv ∈ E(∂T ) in a trigonal graph T of order t, it
follows that T has cycles (containing the edge uv) of all lengths in [3, t].
The following simple observation yields an improved bound for the cases t ≤ 6 in Proposi-
tion 3.2. Its proof follows directly from Figure 2, which we omit.

Observation 3.3. Let T be a trigonal graph with |T | = t ≤ 6, and let u, v be two distinct
vertices of V (T ) with dist∂T (u, v) = d. Then either [d, t − d + 1] ⊆ LT
u,v or [d − 1, t − d] ⊆ LT
u,v
(i.e., P T
u,v contains t − 2d + 2 consecutive paths), unless T is of Case III with {u, v} = {w3, w5}.

3.2 Tetragonal graphs

Definition 3.4 (Tetragonal graph). A tetragonal graph T is a bipartite outer-planar graph
equipped with a Hamiltonian cycle ∂T , defined as the final graph Tn (with ∂T = ∂Tn) of a finite
sequence of tetragonal graphs T2, T3, · · · , Tn satisfying the following properties:

• T2 ≃ C4, ∂T2 = T2.
 6

T2 T3 T4 T5 T6

a2 b2

x2 y2 a3

b3
 x3

y3
 a4 b4
 a5x5

y5 b5

x4 y4

Figure 3: Tetragonal graphs

• For every 2 ≤ i ≤ n − 1, Ti+1 is obtained from Ti by adding two new vertices xi, yi and a
path Pi := aixiyibi with aibi ∈ E(∂Ti); ∂Ti+1 is obtained from ∂Ti by adding the path Pi
and deleting the edge aibi.

By definition, a tetragonal graph is exactly an outer-planar graph in which every inner face
is a 4-cycle. See Figure 3 for a sequence of tetragonal graphs on 4, 6, 8, 10, and 12 vertices. The
black lines represent their boundary cycles, and the vertices ai, bi, xi, yi are marked to indicate
that Ti+1 is obtained from Ti by replacing the edge aibi on ∂Ti with the path aixiyibi.
The following proposition ensures the existence of admissible paths between two vertices at
a given distance on the boundary ∂T .

Proposition 3.5. Let T be a tetragonal graph with |T | = 2m, and let u, v be two distinct vertices
of T with dist∂T (u, v) = d. Then {d, d + 2, . . . , 2m − d} ⊆ LT
u,v.

Proof. We proceed by induction on m. The base case m = 2 (where T ≃ C4) is trivial. Assume
that the proposition holds for every tetragonal graph with fewer than 2m vertices. Let a, x, y, b
be four consecutive vertices on ∂T such that T is obtained from a smaller tetragonal graph T ′

by adding the new path axyb. Then V (T ′) = V (T ) \ {x, y} and |T ′| = 2m − 2.
If {x, y} = {u, v}, then 1 ∈ LT
u,v. Applying the induction hypothesis to T ′ yields LT ′
a,b ⊇
{1, 3, . . . , 2m − 3}. Consequently, LT
u,v ⊇ {1} ∪ (2 + LT ′
a,b) ⊇ {1, 3, . . . , 2m − 1}.
If |{x, y} ∩ {u, v}| = 1, we may assume without loss of generality that u = x and v /∈ {x, y}.
Then dist∂T ′(a, v) = d − 1 and dist∂T ′(b, v) ∈ {d − 2, d}. Since v /∈ {x, y}, we must have v ̸= a
or v ̸= b. If v ̸= a, the induction hypothesis on T ′ implies LT ′
a,v ⊇ {d − 1, d + 1, . . . , 2m − d − 1}.
Thus, LT
u,v ⊇ 1 + LT ′
a,v ⊇ {d, d + 2, . . . , 2m − d}. If v ̸= b, the induction hypothesis implies LT ′
b,v ⊇
{d, d + 2, . . . , 2m − d − 2}. Thus, LT
u,v ⊇ {d} ∪ (2 + LT ′
b,v) ⊇ {d, d + 2, . . . , 2m − d}, as desired.
Finally, if {x, y} ∩ {u, v} = ∅, then dist∂T ′(u, v) ∈ {d − 2, d}. The induction hypothesis
implies LT ′
u,v ⊇ {d, d + 2, . . . , 2m − d − 2}. Hence, LT
u,v ⊇ {2m − d} ∪ LT ′
u,v ⊇ {d, d + 2, . . . , 2m − d}.
In all cases, we have LT
u,v ⊇ {d, d + 2, . . . , 2m − d}, and the result follows by induction.

By applying Proposition 3.5 to uv ∈ E(∂T ) in a tetragonal graph T of order 2m, we see that
T contains cycles (each includes uv) of all lengths in {4, 6, . . . , 2m}.
Before defining the specific core subgraph in bipartite graphs, we motivate the need for a
more robust structure than a simple tetragonal graph. The analysis of the bipartite case is
inherently more challenging in our approach because tetragonal graphs are significantly less
efficient at generating admissible paths compared to trigonal graphs. To illustrate this disparity,
let T1 be a maximum trigonal subgraph of a non-bipartite graph G1, and let T2 be a maximum
tetragonal subgraph of a bipartite graph G2, assuming |T1| = |T2| = 2m and that both G1 and
G2 have sufficiently large minimum degrees. Then the maximality of |T1| and the bipartiteness
of G2 implies that δ(Gi − Ti) ≥ δ(Gi) − m. However, a critical difference arises in the number
of generated path lengths. Comparing Proposition 3.2 and Proposition 3.5, for two vertices
at distance d on the boundary, T1 provides a set of path lengths [d, 2m − d] with cardinality
2m − 2d + 1, whereas T2 yields only {d, d + 2, . . . , 2m − d} with cardinality m − d + 1. This
substantial reduction in available paths necessitates an extension of the tetragonal subgraph to
include vertices with high degrees, thereby forming a stronger core.
We then introduce a specific class of tetragonal subgraphs for the subsequent proofs.

7

Definition 3.6. We say that T is an optimal tetragonal subgraph of a bipartite graph G if the
following conditions hold.

(1) T is a tetragonal subgraph of G with maximum order;

(2) Subject to condition (1), the number of edges in G[V (T )] is maximized.

The following lemma summarizes the key properties of optimal tetragonal subgraphs. In
Section 6 (bipartite case), we employ the subgraph induced by V (T ) ∪ R as the core subgraph.

Lemma 3.7. Let T be an optimal tetragonal subgraph of a bipartite graph G. If |T | = 2m ≥ 6,
then the following hold:

(1) For every v ∈ V (G − T ), degT (v) ≤ m. The equality holds only if G[V (T )] ≃ Km,m.

(2) R := {v ∈ V (G − T ) : degT (v) ≥ m − 1} is an independent set.

(3) If m ≥ 4, then R is contained in one of the two partite sets of G.

(4) For every v ∈ V (G − T − R), exactly one of the following holds:

(4.1) degR(v) = 0 and degT (v) ≤ m − 2;

(4.2) degR(v) = 1 and degT (v) = 0.

Proof. For (1), since G is bipartite, degT (v) ≤ m trivially holds. Suppose degT (v) = m for
some v ∈ V (G − T ). Let (A, B) be the partite sets of G with v ∈ B. Then v is adjacent
to every vertex in V (T ) ∩ A. If G[T ] ̸≃ Km,m, then there exists u ∈ B with degT (u) < m.
The set (V (T ) \ {u}) ∪ {v} spans a tetragonal graph that induces strictly more edges than T ,
contradicting the maximality of e(G[V (T )]). Hence G[T ] ≃ Km,m, which proves (1).
For (2), suppose to the contrary that there are two adjacent vertices u1, u2 ∈ R. By
Lemma 2.5 (1), there exist v1, v2 ∈ V (T ) such that u1v1, u2v2 ∈ E(G) and v1v2 ∈ E(∂T ).
It is routine to verify that V (T ) ∪ {u1, u2} spans a larger tetragonal graph, whose boundary
cycle is obtained from ∂T by replacing the edge v1v2 with the path v1u1u2v2, a contradiction.
Hence R is an independent set, proving (2).
For (3), let (A, B) be the partite sets of G. Suppose to the contrary that both R ∩ A and
R∩B are non-empty; then there exist u1 ∈ R∩A and u2 ∈ R∩B. We claim that V (T )∪{u1, u2}
would span a larger tetragonal graph. Let ∂T = v0 . . . v2m−1v0, where indices are taken modulo
2m. Since degT (u1), degT (u2) ≥ m − 1, we may select vi ∈ V (T ) ∩ B and vj ∈ V (T ) ∩ A such
that u1 is adjacent to every vertex in (V (T ) ∩ B) \ {vi}, and u2 is adjacent to every vertex in
(V (T ) ∩ A) \ {vj}.
If vivj ∈ E(∂T ), we may assume that j = i − 1. Note that the edge vivj is contained in a
unique 4-cycle F = vi−1vivqvp in T . Since G is bipartite, i and p have the same parity, while
q has the opposite parity. See Figure 4a for an illustration, where ∂T is the outer cycle on
2m = 22 vertices. We label the 4-cycles u1vs−1vsvs+1 (for s = i − 3, i − 5, . . . , q + 2), u2vqvpvp+1,
u2vt−1vtvt+1 (for t = q − 1, q − 3, . . . , i + 2), and the 4-cycle F by 1, 2, . . . , m. Recall the iterative
process in Definition 3.4. As visualized in Figure 4a, let the 4-cycle labeled 1 be the initial
tetragonal graph. By sequentially adding the 4-cycles labeled 2, 3, . . . , m, we obtain a tetragonal
graph with vertex set V (T ) ∪ {u1, u2}, contradicting the maximality of m.
Now consider the case where j − i /∈ {−1, 1}. It follows that vi−1, vi+1 ∈ NT (u2). We have
|j − i| ≥ 2 since i and j have different parities. Since m ≥ 4, vi+3 is distinct from vi−3. We
may assume without loss of generality that j ̸= i − 3, so u2vi−3 ∈ E(G). See Figure 4b for
an example with |T | = 22. The 4-cycles u2vi−1vivi+1, u2vi−3vi−2vi−1, and u1vt−1vtvt+1 (for
t = i − 3, i − 5, . . . , i + 3) are labeled 1, 2, . . . , m. It is straightforward to verify that, starting
from the 4-cycle labeled 1 and sequentially adding the cycles labeled 2, 3, . . . , m, we obtain a
tetragonal graph with vertex set V (T ) ∪ {u1, u2}, contradicting the maximality of m. This
completes the proof of (3).
For (4), select an arbitrary vertex w ∈ V (G − T − R). If degR(w) = 0, then degT (w) ≤ m − 2
by the definition of R. Now assume degR(w) > 0. First, we show degT (w) = 0. Let p ∈ NR(w).

8

7
 8

9

10

1

2
 3
 4 5 6

11
 u1

u2

vi−1 vi
 vq

vp

vp+1
 (a) j = i − 1
 1
2

3

4

5
 6 7 8
 9

10

11

u1

u2
vi
 vq

vp

vj
 vi−2 vi−1 vi+1 vi+2
vi−3
 (b) |j − i| > 1

1

3 2

vi−2
 vi−1 vi vi+1
 vi+2

p′ p
w

(c) ∣
∣E({vi−2, vi}, {p, p′})
∣
∣ ≥ 3
 1
 3

2

vi−2
 vi−1 vi vi+1
 vi+2

p′ p

w

(d) ∣
∣E({vi, vi+2}, {p, p′})∣
∣ ≥ 3

Figure 4: Forming larger tetragonal graphs in Lemma 3.7

If there exists v ∈ NT (w), since degT (p) ≥ m − 1, there exists v′ ∈ NT (p) such that vv′ ∈ E(∂T ).
Then V (T ) ∪ {p, w} spans a larger tetragonal graph (with the boundary cycle obtained by
replacing the edge vv′ on ∂T with the path vwpv′). This contradiction implies that degT (w) = 0.
It remains to show that degR(w) = 1. Suppose for the sake of contradiction that there is a
vertex p′ ∈ NR(w) distinct from p. Assume that ∂T = v0 . . . v2m−1v0, with indices taken modulo
2m. We say that an ordered pair of indices (i, j) ∈ [0, 2m − 1]2 is bad if:

(i) j ∈ {i − 1, i + 1};

(ii) T − {vi, vj} is a tetragonal graph;

(iii) max {∣
∣E({vi−2, vi}, {p, p′})
∣
∣, ∣
∣E({vi+2, vi}, {p, p′})
∣
∣
} ≥ 3.

We claim that if (i, j) is bad, then V (T )\{vj}∪{p, p′, w} spans a larger tetragonal graph. Assume
without loss of generality that j = i + 1; then the condition (ii) that T − {vi, vj} is a tetragonal
graph is equivalent to vi−1vi+2 ∈ E(T ). The claim is illustrated in Figures 4c and 4d for the
cases |E({vi−2, vi}, {p, p′})| ≥ 3 and |E({vi+2, vi}, {p, p′})| ≥ 3. The gray region represents the
tetragonal subgraph with vertex set V (T ) \ {vi, vi+1}, whose boundary cycle is derived from
∂T by replacing the path vi−1vivi+1vi+2 with the edge vi−1vi+2. The ‘red’ and ‘blue’ regions
correspond to the 4-cycles pvi−2vi−1vi and wp′vi−2p in Figure 4c, and to pvivi−1vi+2 and wp′vip
in Figure 4d, respectively. By adding the red 4-cycle and then the blue 4-cycle to the gray
tetragonal graph, we obtain a tetragonal graph with vertex set V (T ) \ {vj} ∪ {p, p′, w}, proving
the claim. We remark that these figures depict a representative edge configuration; for another
scenario satisfying condition (iii) (for example, when p′ is adjacent to vi rather than vi−2), the
construction is analogous. Thus, the maximality of m implies that no bad pair (i, j) exists.
We now derive a contradiction by identifying such a bad pair. Note that T is an outer-planar
graph where every inner face is a 4-cycle. Since |T | ≥ 6, T must contain a chord of ∂T , implying
that there are at least two faces that share three edges with ∂T . It follows that there are two

9

distinct indices i and i′ such that vi−1vi+2, vi′−1vi′+2 ∈ E(T ). We will show that one of the pairs
(i, i + 1), (i + 1, i), (i′, i′ + 1), or (i′ + 1, i′) is bad. Indeed, conditions (i) and (ii) hold for all four
pairs. Suppose neither (i, i + 1) nor (i + 1, i) is bad. By symmetry, we may assume that p and vi
belong to different partite sets. Then |E({vi−2, vi}, {p, p′})| ≤ 2 and |E({vi+2, vi}, {p, p′})| ≤ 2.
Recall that each of p′ and p is non-adjacent to at most one vertex in {vi−2, vi, vi+2}. It follows
that vi must be the common non-neighbor for both p and p′. This implies that the vertex in
{vi′, vi′+1} belonging to the partite set distinct from that of p cannot serve as a common non-
neighbor for both p and p′. Consequently, either (i′, i′ + 1) or (i′ + 1, i′) must be bad. Thus,
a bad pair always exists. This contradiction proves that if degT (w) = 0, then degR(w) = 1,
completing the proof of (4).

4 The k-weak graphs and proof of Theorem 1.2

In this section, we introduce a class of graphs called k-weak graphs, which structurally approx-
imate 3-connected graphs with minimum degree at least k, and state the main technical result
on cycle lengths in this class (Theorem 4.2). The section is then divided into two parts: in Sec-
tion 4.1, we prove Theorem 1.2 via a reduction argument assuming Theorem 4.2; in Section 4.2,
we establish key structural lemmas for k-weak graphs, preparing for the proof of Theorem 4.2
in Sections 5 and 6.
We first provide the formal definition.

Definition 4.1. Let k ≥ 3 be an integer. A graph G is k-weak if one of the following holds:

Type I. G is 3-connected with δ2(G) ≥ k.

Type II. There exists exactly one vertex θ ∈ V (G) with degG(θ) = 2, whose neighbors are θ1
and θ2, such that the graph G − θ + θ1θ2 is 3-connected with minimum degree at least k.

In either case, we denote by θ a vertex of minimum degree in G. Note that θ is the unique vertex
with degG(θ) < k whenever δ(G) < k.

It follows from the definition that a k-weak graph is always 2-connected with δ2(G) ≥ k.
While Type I covers the 3-connected case, Type II represents the minimal structural deviation
from 3-connectivity: the graph is 2-connected, but the separating set isolates exactly one vertex.
We now state Theorem 4.2, which constitutes the main technical result of this paper.

Theorem 4.2. Let k ≥ 6 be an integer. If G is a k-weak graph not isomorphic to any graph in
{Kk+1, Kk,k} ∪ Hk, then G contains a cycle of length r (mod k) for every even integer r.

4.1 Proof reduction of Theorem 1.2

In this subsection, we prove Theorem 1.2, under the validity of Theorem 4.2.

Proof of Theorem 1.2 (assuming Theorem 4.2). It suffices to establish the following sta-
bility result for 2-connected graphs: for k ≥ 6, every 2-connected graph G with δ2(G) ≥ k
contains a cycle of length r (mod k) for every even integer r, unless G is isomorphic to a graph
in {Kk+1, Kk,k} ∪ Hk. Observe that every graph in {Kk+1, Kk,k} ∪ Hk contains cycles of all even
lengths modulo k with the only exception of 2 (mod k). Thus, Theorem 1.2 follows directly by
applying this result to each end-block of the graph (since every end-block B of a graph with
δ(G) ≥ k satisfies δ2(B) ≥ k).
We now proceed to prove this statement. Suppose for the sake of contradiction that G is a
2-connected graph with δ2(G) ≥ k that is not isomorphic to any graph in {Kk+1, Kk,k} ∪ Hk,
yet there is no cycle of length r (mod k) in G for some even integer r. Then G cannot be
3-connected; otherwise, G would be a k-weak graph of Type I, and Theorem 4.2 would imply
the existence of such a cycle, a contradiction.
We first claim that there exists a 2-cut S of G such that at least two components of G − S
have order at least 2. Suppose to the contrary that for every 2-cut S = {x, y} of G, there is a

10

component of G − S consisting of a single vertex z, i.e., NG(z) = {x, y}. Then (G − z − xy, x, y)
is a 2-connected rooted graph with δ2(G − z − xy, x, y) ≥ δ2(G) ≥ k. By Lemma 2.3, there are
k − 1 admissible (x, y)-paths in G − z − xy. If xy ∈ E(G), combining these paths with the edge
xy or the path xzy yields at least (k − 1) + 2 − 1 = k consecutive cycles in G, a contradiction.
Hence, we must have xy /∈ E(G). Since δ2(G) ≥ k, z is the unique vertex with degree less than
k in G. Hence, S is the unique 2-cut of G, and G − z + xy is 3-connected. This implies that
G is a k-weak graph of Type II, so Theorem 4.2 guarantees the existence of the desired cycle, a
contradiction. This proves the claim.
Let S = {x, y} be a 2-cut of G satisfying the claim, and let M and N be the vertex sets of
two components of G − S with |M |, |N | ≥ 2. Define GM := G[M ∪ S] and GN := G[N ∪ S].
Then (GM , x, y) and (GN , x, y) are 2-connected rooted graph on at least four vertices with
δ2(GM , x, y) ≥ k and δ2(GN , x, y) ≥ k. By Lemma 2.3, there are k − 1 admissible (x, y)-paths
in both GM and GN . Concatenating these paths produces at least (k − 1) + (k − 1) − 1 = 2k − 3
admissible cycles in G. Since none of these cycles has length r (mod k), we deduce that k must
be even, all these cycles must have odd lengths, and the lengths of admissible paths in GM or
GN form a 2-AP.
If one of GM and GN is non-bipartite, say GM , then there exist two (x, y)-paths L1, L2 in
GM whose lengths have different parities. Consequently, combining one of {L1, L2} with the
k − 1 admissible (x, y)-paths in GN would produce at least k − 1 ≥ k/2 even cycles, whose
lengths form a 2-AP. This collection must contain a cycle of length r (mod k) (since k is even,
any set of k/2 even lengths forming a 2-AP covers all even residues modulo k), a contradiction.
Therefore, we assume that both GM and GN are bipartite. We may assume without loss
of generality that θ /∈ M , so that degGM (v) ≥ k for every vertex v ∈ M . We claim that GM
contains a block B of order at least 4 such that |V (B) ∩ (Cut(B) ∪ S)| ≤ 2. If such a block B
exists, then B is a 2-connected bipartite graph where degB(v) ≥ k holds for all but at most two
vertices v ∈ V (B). According to Theorem 2.4, B contains k − 1 ≥ k/2 even cycles with lengths
forming a 2-AP, which guarantees a cycle of length r (mod k), a contradiction.
It remains to verify the existence of such a block B. If GM is 2-connected, then B := GM
suffices. Suppose GM is not 2-connected. If GM has an end-block B disjoint from S, then any
non-cut-vertex v ∈ V (B) satisfies degB(v) = degG(v) ≥ k, implying |B| ≥ k + 1 > 4, which
suffices. Thus, we may assume that GM has exactly two end-blocks, say Bx and By, containing
x and y respectively. If |Bx| ≥ 3, let B := Bx. Then, similar to the previous case, any non-cut-
vertex v ∈ V (B) \ {x} satisfies degB(v) ≥ k, implying |B| ≥ k + 1 > 4. Finally, assume |Bx| =
|By| = 2, with Bx = {x, z}. Let B be the unique block of GM distinct from Bx that contains z.
Since |M | ≥ 2, the graph GM is not merely the path xzy, which implies y /∈ V (B). Moreover,
since z is adjacent only to x outside of B, we have |B| ≥ degB(z) + 1 = degG(z) ≥ k > 4. Thus,
B satisfies the required conditions. This completes the proof.

4.2 Notation and lemmas for k-weak graphs

We now establish the necessary definitions and structural lemmas for k-weak graphs. Henceforth,
we use G⋆ to represent a k-weak graph.
For technical reasons, we define a specific subgraph G ⊆ G⋆ as follows:

Definition 4.3. Let G⋆ be a k-weak graph and θ be the vertex defined in Definition 4.1. We
define the subgraph G ⊆ G⋆ as follows:

G :=
 {
G⋆, if G⋆ is of Type I,
G⋆ − θ, if G⋆ is of Type II.

Our general strategy is to find two specific path families in a core subgraph H ⊆ G and
in G − H, respectively, and then concatenate these paths yields the required cycles. Let us
summarize the degree and connectivity constraints for G that will be used later.

Proposition 4.4. The graph G satisfies δ(G) ≥ 3, δ2(G) ≥ k − 1, and δ3(G) ≥ k. In particular:

11

• If G⋆ is of Type I, then G is 3-connected with δ(G) ≥ 3 and δ2(G) ≥ k.

• If G⋆ is of Type II, then G is 2-connected with δ(G) ≥ k − 1 and δ3(G) ≥ k. Moreover, if
θ1θ2 ∈ E(G) (i.e., θ1θ2 ∈ E(G⋆)), then δ(G) ≥ k.

In the subsequent proofs, a recurring task is to find admissible paths within specific compo-
nents. To apply Lemma 2.3 effectively, we identify pairs of vertices within a 2-connected rooted
subgraph satisfying the requisite degree conditions. This motivates the following definition.

Definition 4.5. Let x, y be distinct vertices in a connected graph M , and let t ≥ 2 be an integer.
The ordered pair (x, y) is t-valid if there exists an end-block B of M with |B| ≥ t such that one
of the following holds:

(1) x, y ∈ V (B), and degB(v) ≥ t for all but at most one vertex v ∈ V (B) \ {x, y}.

(2) x ∈ V (B) \ {b} and y /∈ V (B), where {b} = Cut(B), and degB(v) ≥ t for all but at most
one vertex v ∈ V (B) \ {x, b}.

The following observation follows immediately from Lemma 2.3 and Definition 4.5.

Observation 4.6. Let x and y be distinct vertices in a connected graph M , and let t ≥ 2 be an
integer. If (x, y) is t-valid, then P M
x,y contains t − 1 admissible paths.

Proof. Suppose (x, y) is t-valid. Let B be the end-block containing x as specified in Definition 4.5.
If |B| ≤ 3, then B ≃ K|B| (as B is a block), and t ≤ |B| ≤ 3. The conclusion holds trivially.
Now assume |B| ≥ 4. Apply Lemma 2.3 to the 2-connected rooted graph (B, x, y) if y ∈ V (B),
or to (B, x, b) if y /∈ V (B) (where {b} = Cut(B)). The conclusion holds in either case.

We introduce BM and uM to identify a specific configuration in M suitable for establishing
valid pairs.

Definition 4.7 (BM , uM ). Let G⋆ be a k-weak graph, and let T be a subgraph of G. For any
component M of G − T of order at least 3, we select an end-block BM of M as follows:

(1) If M is 2-connected, let BM := M .

(2) If M is not 2-connected and G⋆ is of Type I, let BM be an arbitrary end-block such that
θ /∈ V (BM ) \ Cut(BM ).

(3) If M is not 2-connected and G⋆ is of Type II, let BM be an end-block of maximum order
such that V (BM ) \ Cut(BM ) contains at most one of θ1 and θ2.

Based on this selection, we choose a vertex uM ∈ V (BM ) \ Cut(BM ) satisfying:

(1) degT (uM ) = max{degT (v) : v ∈ V (BM ) \ Cut(BM )}.

(2) Subject to (1), degG(uM ) is minimized.

We omit the subscript T from BM and uM , as M being a component of G − T implicitly
fixes T . The following lemma establishes that uM forms a valid pair with any other vertex in
M . We remark that the proof below does not rely on the maximality of the order of BM in
cases (3); however, this property will be useful in Section 6.

Lemma 4.8. Let k ≥ 6 be an integer and G⋆ be a k-weak graph. For every subgraph T ⊆ G
and every component M of G − T with |M | ≥ 3, if degT (uM ) ≤ k − 2, then for every vertex
w ∈ V (M ) \ {uM }, the pair (uM , w) is (k − degT (uM ))-valid.

Proof. Let t := k − degT (uM ). By definition, it suffices to show that |BM | ≥ t and that
degBM (v) ≥ t holds for all but at most one vertex v ∈ V (BM ) \ {uM }.

12

We first consider the case that M is 2-connected. Then BM = M and |BM | ≥ 3. Since
δ2(G) ≥ k − 1, there exists a vertex u ∈ V (M ) with degG(u) ≥ k − 1. By the maximality of
degT (uM ), we have degT (u) ≤ degT (uM ), and thus

|M | ≥ degM (u) + 1 = degG(u) − degT (u) + 1 ≥ (k − 1) − degT (uM ) + 1 = t.

It remains to verify the degree condition. If G⋆ is of Type I, θ is the only vertex that may have
degree less than k in G. The maximality of degT (uM ) implies that for every v ∈ V (M )\{uM , θ},
we have degM (v) = degG(v) − degT (v) ≥ k − degT (uM ) = t. Thus, at most one vertex (namely,
θ) may fail the degree condition.
If G⋆ is of Type II, all vertices other than θ1 and θ2 have degree at least k in G. For every
v ∈ V (M ) \ {uM , θ1, θ2}, we have

degM (v) = degG(v) − degT (v) ≥ k − degT (uM ) = t. (1)

We claim that if both θ1 and θ2 fail the degree condition (i.e., degM (θi) < t for i = 1, 2), then
uM ∈ {θ1, θ2}. Indeed, by revisiting inequality (1), the condition degM (θi) < t implies that
degG(θi) = k − 1. Suppose to the contrary that uM /∈ {θ1, θ2}. By the selection criterion (2) for
uM , we must have degT (θ1) < degT (uM ) (as otherwise uM would not minimize degG). However,
this yields degM (θ1) = degG(θ1) − degT (θ1) ≥ (k − 1) − (degT (uM ) − 1) = t, a contradiction.
Thus, at most one vertex in V (M ) \ {uM } has degree less than t, completing the verification.
We then assume that M is not 2-connected. Then BM is an end-block with |BM | ≥ 2. For
any u ∈ V (BM ) \ Cut(BM ), we have degG(u) ≥ k − 1. (This is ensured by the criterion (2) for
Type I since θ /∈ V (BM ) \ Cut(BM ), and by δ(G) ≥ k − 1 for Type II). By the maximality of
degT (uM ), it follows that

|BM | ≥ degBM (u) + 1 = degG(u) − degT (u) + 1 ≥ (k − 1) − degT (uM ) + 1 = t.

Now we verify the degree condition. If |BM | = 2, the condition holds trivially. Assume
|BM | ≥ 3, then V (BM ) \ (Cut(BM ) ∪ {uM }) is non-empty. If G⋆ is of Type I, for every v ∈
V (BM )\(Cut(BM )∪{uM }), we have v ̸= θ, so degBM (v) = degG(v)−degT (v) ≥ k−degT (uM ) =
t. If G⋆ is of Type II, the verification is analogous to the 2-connected case. Recall that V (BM ) \
Cut(BM ) contains at most one of θ1 and θ2; we may assume without loss of generality that
θ2 /∈ V (BM ) \ Cut(BM ). Consequently, for every v ∈ V (BM ) \ (Cut(BM ) ∪ {uM , θ1}), we have
degBM (v) ≥ t. By repeating the argument based on the selection criterion (2), we deduce that
if θ1 ∈ V (BM ) \ Cut(BM ) and degBM (θ1) < t, then necessarily uM = θ1. Thus, only the vertex
in Cut(BM ) may violate the degree condition. This completes the proof.

Finally, we establish a strengthened form of Menger’s Theorem for 2-connected graphs.

Lemma 4.9. Let G be a 2-connected graph, and let X, Y be a partition of V (G) such that
|X| ≥ 2 and |Y | ≥ 2. Then for every x ∈ NX (Y ), there exist two disjoint (X, Y )-edges, one of
which is incident to x.

Proof. Let y ∈ NY (x). If E(X − x, Y − y) ̸= ∅, then any edge in this set, together with xy, forms
the desired pair of disjoint edges. Suppose otherwise. Since G is 2-connected, E(X − x, Y ) ̸= ∅.
By our assumption, every edge in this set must be incident to y, implying E(X − x, y) ̸= ∅.
Similarly, E(x, Y − y) ̸= ∅. Selecting an arbitrary edge from each of these two sets yields a pair
of disjoint edges, which completes the proof.

5 Proof of Theorem 4.2: the non-bipartite case

Throughout the rest of the paper, let G⋆ be a given k-weak graph and let G ⊆ G⋆ be defined in
Definition 4.3. This section is devoted to the proof of Theorem 4.2 when G is non-bipartite.

Theorem 5.1. Let k ≥ 6 be an integer, and let G⋆ be a k-weak graph not isomorphic to Kk+1.
If G is non-bipartite, then G⋆ contains a cycle of length r (mod k) for every even integer r.

13

Throughout this section, we assume the conditions of Theorem 5.1:

k ≥ 6, G⋆ is a k-weak graph, G⋆ ̸≃ Kk+1, and G is non-bipartite.

The first lemma treats the K3-free case, with a minimal induced odd cycle as the core graph.

Lemma 5.2. If G is K3-free, then G contains a cycle of length r (mod k) for any even r.

Proof. Suppose for a contradiction that for some even r, G⋆ does not contain any cycle of length
r (mod k). Let C = v0v1 . . . v2sv0 ⊆ G (s ≥ 2) be an induced odd cycle of minimum order such
that ∑2s
i=0 degG(vi) is minimized. By the minimality of |C|, every vertex v ∈ V (G − C) satisfies
degC(v) ≤ 2, with equality holding if and only if NC(v) = {vi, vi+2} for some index i (taken
modulo 2s + 1). Moreover, if G⋆ is of Type I, the vertex θ /∈ V (C) and degG(θ) < k, then
the minimality of the degree sum implies degC(θ) ≤ 1. Consequently, for any component M of
G − C, every v ∈ V (M ) satisfies degM (v) ≥ degG(v) − 2 ≥ k − 3, except possibly when G⋆ is
of Type I and v = θ, in which case degM (θ) ≥ degG(θ) − 1 ≥ 2. In summary, it always holds
that δ(M ) ≥ 2 and δ2(M ) ≥ k − 3, which implies that every end-block of M has order at least
k − 2 ≥ 4.

Claim 1. G − C is connected.

Proof. Suppose to the contrary that G − C has components M1, . . . , Mt with t ≥ 2. For each
s ∈ [t], let us := uMs and Bs := BMs as defined in Definition 4.7.
First, consider the case where degC(ui) = 1 for some i ∈ [t], or k ≥ 7 (in which case
let i ∈ [t] be arbitrary). Pick any index j ∈ [t] distinct from i. Since G is 2-connected,
Lemma 4.9 guarantees the existence of vertices wi ∈ V (Mi) \ {ui} and wj ∈ V (Mj) \ {uj}, along
with two disjoint paths connecting {ui, wi} and {uj, wj} whose internal vertices lie in C. By
Observation 4.6 and Lemma 4.8, P Mi
ui,wi contains k − degC(ui) − 1 admissible paths, and P Mj
uj ,wj
contains k − degC(uj) − 1 admissible paths. Concatenating these path collections, together with
the two disjoint connecting paths, yields at least (k −degC(ui)−1)+(k−degC(uj)−1)−1 = 2k−
3 − degC(ui) − degC(uj) ≥ k admissible cycles in G (using the fact that k ≥ 7 or degC(ui) = 1).
Since G contains no cycle of length r (mod k), we deduce that k must be even, and the lengths
of admissible paths in P Mi
ui,wi must form a 2-AP. As C is an odd cycle, P C
ui,wi contains a path L
whose length has the same parity as the admissible paths in P Mi
ui,wi. Combining P Mi
ui,wi with L
produces at least k − degC(ui) − 1 ≥ k − 3 ≥ k/2 cycles of even lengths forming a 2-AP, one of
which must have length r (mod k), a contradiction.
Thus, we may assume k = 6 and degC(us) = 2 for each s ∈ [t]. We claim that for any
s ∈ [t], NC(Ms) is contained in a set of three consecutive vertices on C. Suppose the claim
fails for M1. We may assume NC(u1) = {v0, v2}. Since the claim fails, there exists w ∈
V (M1) − u1 adjacent to some vℓ ∈ V (C) with ℓ /∈ {0, 1, 2}. Then P C
u1,w contains paths of
lengths {ℓ, ℓ + 2, 2s − ℓ + 3, 2s − ℓ + 5} (two odd and two even integers, with differences of 2).
It is straightforward to verify that combining these paths with P M
u1,w (which contains k − 3 = 3
admissible paths) generates cycles of all lengths modulo 6, a contradiction.
We now assert that NC(ui) ∩ NC(Mi \ {ui}) ̸= ∅ for every i ∈ [t]. Suppose for the sake
of contradiction that this intersection is empty for some index, say i = 1. We may assume
NC(M1) ⊆ {v0, v1, v2} and NC(u1) = {v0, v2}, then NC(M1 \ {u1}) ⊆ {v1}. Consequently,
{u1, v1} is a 2-cut of G separating M1 \ {u1} (which is non-empty since |M1| ≥ 3) from the rest
of the graph. This is impossible if G⋆ is of Type I (as G is 3-connected). Thus, G⋆ must be of
Type II, and M1 must contain exactly one of the vertices θ1, θ2 (as G + θ1θ2 is 3-connected). For
every v ∈ V (M1) \ {u1}, since NC(v) ⊆ {v1}, we have degC(v) ≤ 1. Consequently, degM1(v) =
degG(v) − degC(v) ≥ k − 1 for all v ∈ V (M1) \ {u1}, with the possible exception for the single
vertex in V (M1) ∩ {θ1, θ2}. We then select q as follows: if M1 is 2-connected, let q be any
neighbor of v1 in M1 \ {u1}. If M1 is not 2-connected, let q be any neighbor of v1 in M1 − B1
(such a vertex exists because Cut(B1) is not a cut-vertex in G). In either case, a routine check
confirms that (u1, q) is (k − 1)-valid, as the required degree condition holds for all vertices in
M1 \ {u1} except possibly for the single vertex in V (M1) ∩ {θ1, θ2}. By Observation 4.6, P M1
u1,q

14

contains k − 2 admissible paths. Recall that the pair (u2, w2) in M2 yields k − 3 admissible
paths in P M2
u2,w2. Since G is 2-connected, Lemma 4.9 provides two disjoint paths between {u1, q}
and {u2, w2} with all internal vertices in C. Concatenating the paths from P M1
u1,q and P M2
u2,w2
via these connecting paths produces (k − 2) + (k − 3) − 1 = k admissible cycles (given k = 6).
Following the previous parity argument, if these cycles fail to cover some residue r (mod k), the
lengths of admissible paths in P M1
u1,q must form a 2-AP. Combining these with a path in P C
u1,q of
the appropriate parity yields k − 2 > k/2 even admissible cycles, a contradiction. This proves
the assertion.
According to the assertion, for each i ∈ [t], there exists pi ∈ V (Mi) \ {ui} such that NC(pi) ∩
NC(ui) ̸= ∅. Then LC
ui,pi ⊇ {2, 4, 2s + 1}. The proof of Claim 1 is then partitioned into the
cases s ∈ {2, 3} and s ≥ 4. If s ∈ {2, 3}, the set P C
u1,p1 contains two paths whose lengths differ
by 3. Concatenating these with the k − 3 = 3 admissible paths in P M1
u1,p1 yields cycles of all
possible lengths modulo 6, a contradiction. If s ≥ 4, then |C| = 2s + 1 ≥ 9. Recall that each
NC(Mi) is some set of three consecutive vertices on C. Since δ(G) ≥ 3, every vertex in C has
a neighbor outside C, so these sets NC(Mi)’s cover V (C). A routine calculation shows that
there must be three sets that are pairwise disjoint or intersect in at most one vertex. In other
words, there exist distinct i, j, ℓ ∈ [t] and indices a, b, c such that NC(ui) = {va−1, va, va+1},
NC(uj) = {vb−1, vb, vb+1}, and NC(uℓ) = {vc−1, vc, vc+1}, with the distance between any pair of
{va, vb, vc} being at least 2. Since each of P Mi
ui,pi, P Mj
uj ,pj , and P Mℓ
uℓ,pℓ contains k − 3 = 3 admissible
paths, combining them via three disjoint subpaths of C connecting these endpoints, yields at
least 3 + 3 + 3 − 2 > 6 admissible cycles. Again, if these fail to cover some residue r (mod k), we
derive a contradiction by combining P M1
u1,p1 with a path in P C
u1,p1 with a suitable length parity.
This completes the proof of Claim 1.

By Claim 1, M := G − C is connected. Let u := uM . Without loss of generality, assume
NC(u) is either {v0} or {v0, v2}. Since δ(G) ≥ 3, every vertex on C has a neighbor in M . In
particular, some w ∈ V (M ) is adjacent to vs+2. Note u ̸= w as s ≥ 2. If NC(u) = {v0},
then by Observation 4.6 and Lemma 4.8, P M
u,w contains k − 2 admissible paths. Observe that
LC
u,w ⊇ {s + 1, s + 4}. Since k ≥ 6, combining paths in P C
u,w and P M
u,w yields k consecutive cycles,
a contradiction. If NC(u) = {v0, v2}, then P M
u,w contains k − 3 admissible paths, and one can
verify that LC
u,w ⊇ {s + 1, s + 2, s + 3, s + 4}. Combining the paths in P M
u,w and P C
u,w yields
(k − 3) + 4 − 1 = k consecutive cycles, a contradiction. This completes the proof.

In the remainder of this section, following Lemma 5.2, we may assume K3 ⊆ G and

let T ⊆ G be a trigonal subgraph of maximum order.

In what follows, the core graph always refers to this maximum trigonal subgraph T , and the
proofs are divided into Lemmas 5.3, 5.4, and 5.6, according to the order of T .
Denote by K−
n the graph obtained from Kn by removing an edge.

Lemma 5.3. If |T | = 3, then G⋆ contains k consecutive cycles.

Proof. Define a subgraph H ⊆ G⋆ as follows: if G⋆ is of Type II and θ1θ2 /∈ E(G⋆), let H := G⋆;
otherwise, let H := G. By assumption, H contains a triangle, say with vertex set {a, b, c}, but
no K−
4 subgraph. It follows that every v ∈ V (H) − {a, b, c} has at most one neighbor in {a, b, c}.
Let H ′ be the graph obtained from H by contracting the edge bc into a new vertex a′. We
claim that H ′ is 2-connected. If G⋆ is of Type II and θ1θ2 /∈ E(G⋆), then {θ1, θ2} is the unique
2-cut of H = G⋆ (since G + θ1θ2 is 3-connected), which implies that {b, c} is not a 2-cut in H
(as bc ∈ E(G⋆)); thus, a′ is not a cut-vertex in H ′. Clearly, no other vertex can be a cut-vertex
in H ′. Otherwise, we have G⋆ is of Type II and θ1θ2 ∈ E(G⋆), or G⋆ is of Type I. It follows from
the definition that H = G is 3-connected, which immediately ensures that H ′ is 2-connected.
In either case, H ′ is 2-connected, implying that the rooted graph (H ′ − aa′, a, a′) is 2-
connected. Since H contains no K−
4 , every v ∈ V (H) \ {a, b, c} satisfies deg{a,b,c}(v) ≤ 1. This
implies that δ2(H ′ − aa′, a, a′) ≥ δ2(H) ≥ k. Note that |H ′| ≥ |H| − 1 ≥ |G| − 1 ≥ δ2(G) > 4.

15

By Lemma 2.3, P H ′−aa′
a,a′ contains k − 1 admissible paths. Equivalently, P H−{a,b,c}
a,b ∪ P H−{a,b,c}
a,c
contains k − 1 admissible paths. By combining these with the edges ab, ac or the paths acb, abc
(which have length 1 or 2), we obtain (k − 1) + 2 − 1 = k consecutive cycles in H, and thus in
G⋆. This completes the proof of Lemma 5.3.

Lemma 5.4. If |T | = 4, then G⋆ contains k consecutive cycles.

Proof. Let T be a trigonal subgraph with |T | = 4. Since δ(G) ≥ 3 and δ2(G) ≥ k − 1 ≥ 5,
G − T ̸= ∅. By the maximality of T , every v ∈ V (G − T ) has at most two neighbors in T . Thus,
for any component M of G − T , δ(M ) ≥ 1 and δ2(M ) ≥ k − 3, implying that every end-block
of M is an edge or has order at least k − 2 ≥ 4.
If G[V (T )] ≃ K4, then the maximality of T implies that every v ∈ V (G−T ) has degT (v) ≤ 1.
Let M be a component of G − T and let u := uM . By Lemma 4.9, there exists w ∈ V (M ) \ {u}
such that u and w are adjacent to distinct vertices in T . Thus LT
u,w = {3, 4, 5}. By Lemma 4.8
and Observation 4.6, P M
u,w contains at least k − degT (u) − 1 ≥ k − 2 admissible paths. The union
of paths in P M
u,w and P T
u,w yields (k − 2) + 3 − 1 = k consecutive cycles.
If G[V (T )] ≃ K−
4 , define H as in Lemma 5.3: if G⋆ is of Type II and θ1θ2 /∈ E(G⋆), let
H := G⋆; otherwise, let H := G. Then T remains a trigonal subgraph of maximum order in H.
Let V (T ) = {a, b, c, d} with bd /∈ E(H). The maximality of T implies that every v ∈ V (H − T )
satisfies |NH (v) ∩ {b, c}| ≤ 1. Let H ′ be obtained from H by contracting bc into a vertex a′.
Similar to Lemma 5.3, one can verify that (H ′ − aa′, a, a′) is a 2-connected rooted graph with
δ2(H ′ − aa′, a, a′) ≥ k. According to Lemma 2.3, P H ′−aa′
a,a′ contains k − 1 admissible paths, and

equivalently, P H−{a,b,c}
a,b ∪ P H−{a,b,c}
a,c contains k − 1 admissible paths. Concatenating these with
the subpaths in the triangle H[{a, b, c}] produces k consecutive cycles in H, and thus in G⋆.
This completes the proof of Lemma 5.4.

Finally, we consider the remaining case where |T | ≥ 5. To proceed, we need the following
classical pancyclicity criterion due to Bondy [5].

Lemma 5.5 ([5]). Let G be a graph of order n. If dG(u) + dG(v) ≥ n for every pair of non-
adjacent vertices u, v ∈ V (G), then G contains cycles of all lengths in [3, n], unless G ≃ Kn/2,n/2.

Lemma 5.6. If |T | ≥ 5, then G⋆ contains a cycle of length r (mod k) for any even r.

Proof. Suppose G⋆ is a counterexample. Let |T | = t ≥ 5. Recall Proposition 3.2 implies that
every trigonal graph on k + 2 vertices contains cycles of all lengths in [3, k + 2], so we must have
5 ≤ t ≤ k + 1. Let ∂T = v0v1 . . . vt−1v0. By the maximality of T , no vertex v ∈ V (G − T ) can
be adjacent to two consecutive vertices on ∂T ; consequently, degT (v) ≤ ⌊t/2⌋.
We first consider the case where |V (G)| ≤ k + 3. For any pair of non-adjacent vertices in G,
the sum of their degrees is at least δ(G) + δ2(G) ≥ min{3 + k, 2(k − 1)} = k + 3 ≥ |G|. Since
K3 ⊆ T ⊆ G, G cannot be bipartite. It then follows from Lemma 5.5 that G contains cycles
of all lengths in [3, |V (G)|]. Since G⋆ is a counterexample and thus misses a cycle of length in
[3, k + 2], we must have |G| ≤ k + 1. On the other hand, |G| ≥ δ3(G) + 1 ≥ k + 1. This forces
|G| = k + 1, and that all but at most two vertices in G have degree exactly k. Consequently,
G is isomorphic to Kk+1 or K−
k+1. Since G⋆ is not isomorphic to Kk+1 or K−
k+1, G⋆ must be
obtained from G by adding the vertex θ adjacent to exactly two vertices in G. It is clear that
any such G⋆ contains cycles of all lengths in [3, k + 2], a contradiction.
Henceforth, we assume |G| ≥ k + 4. Thus |G − T | ≥ (k + 4) − t ≥ 3. Since δ2(G − T ) ≥
(k − 1) − ⌊t/2⌋ ≥ 2, there exists a component M of G − T with order at least 3. Let u = uM .
By Lemma 4.8, for every v ∈ V (M ) \ {u}, the pair (u, v) is (k − degT (u))-valid.

Claim 1. degT (u) ≤ max{1, ⌊t/2⌋ − 2}.

Proof. Suppose to the contrary that degT (u) = ⌊t/2⌋ − r where r ∈ {0, 1} (with r = 0 if t = 5).
Since G is 2-connected, there exists a vertex w ∈ V (M ) \ {u} with NT (w) ̸= ∅.

16

We first consider the case where NT (u) and NT (w) are disjoint. By Lemma 2.5, there
exist vi ∈ NT (u) and vj ∈ NT (w) such that dist∂T (vi, vj) ≤ max{1, ⌊t/2⌋ + 2 − (⌊t/2⌋ − r) −
1} = r + 1. It follows from Proposition 3.2 that LT
u,w ⊇ 2 + LT
vi,vj ⊇ [r + 3, t − r + 1]. In
addition, Observation 4.6 ensures that P M
u,w contains k − degT (u) − 1 = k − ⌊t/2⌋ + r − 1
admissible paths. If t = 5 or t ≥ 7, concatenating the paths in P T
u,w and P M
u,w produces at least
(t−2r −1)+(k −⌊t/2⌋+r −1)−1 = k +(t−⌊t/2⌋−3)−r ≥ k consecutive cycles, a contradiction.
If t = 6, we observe that degT (u) = 3 − r ≥ 2. By choosing a neighbor in NT (u) that avoids
Case III in Observation 3.3 (possible since degT (u) ≥ 2), we deduce that P T
u,w contains at least
t − 2dist∂T (vi, vj) + 2 ≥ 6 − 2(r + 1) + 2 = 6 − 2r consecutive paths. Combining this with P M
u,w
yields at least (6 − 2r) + (k + r − 4) − 1 = k + 1 − r ≥ k consecutive cycles, a contradiction.
It remains to consider the case where NT (u) and NT (w) intersect. Let vi ∈ NT (u) ∩ NT (w).
Since no two vertices in NT (u) are consecutive on ∂T , it is straightforward to find a vertex
vj ∈ NT (u) \ {vi} such that dist∂T (vi, vj) ≤ r + 2. By Proposition 3.2, LT
u,w ⊇ {2} ∪ (2 + LT
vi,vj ) ⊇
{2} ∪ [4 + r, t − r]. Moreover, LM
u,w contains an admissible subset of size k − ⌊t/2⌋ + r − 1; we
denote this subset by L. Combining these two path collections, it follows that G contains cycles
of all lengths in L + 2 and L + [4 + r, t − r].
If the set L is consecutive, a routine calculation shows that the union of consecutive sets L+2
and L + [4 + r, t − r] is a larger consecutive set (this is equivalent to k ≥ ⌊t/2⌋ + 3). This union
is exactly the set sum L + [2, t − r], which has size at least (k − ⌊t/2⌋ + r − 1) + (t − r − 1) − 1 =
k + t − ⌊t/2⌋ − 3 ≥ k. This implies that G contains k consecutive cycles, a contradiction.
Thus, we may assume that L is a 2-AP. If k ≥ 7 or t is odd, it follows from Observation 2.2 (3)
that the sum L + [4 + r, t − r] yields a consecutive set of size at least 2 (k − ⌊t/2⌋ + r − 1) +
(t − 2r − 3) − 2 = (2k − 7) + (t − 2⌊t/2⌋) ≥ k, a contradiction. Otherwise, we must have
k = 6 and t ∈ [5, k + 1] is even, which implies t = k = 6. Since degT (u) = 3 − r ≥ 2
and Observation 3.3 implies at most one neighbor in NT (u) leads to the configuration in Case
III described there, we can select a neighbor in NT (u) to avoid Case III. Consequently, P T
u,w
contains t − 2dist∂T (vi, vj) + 2 ≥ 6 − 2(r + 2) + 2 = 4 − 2r consecutive paths. Hence, by
Observation 2.2 (3) again, the sum of L and the consecutive subset in LT
u,w yields a consecutive
set of size at least 2 (k − ⌊t/2⌋ + r − 1)+(4−2r)−2 = k, implying that G contains k consecutive
cycles, a contradiction. This completes the proof of Claim 1.

Claim 2. M is the unique component of G − T containing at least 3 vertices.

Proof. Suppose to the contrary that G−T contains another component M ′ of order at least 3. Let
u′ = uM ′. By Lemma 4.8, for any vertex v′ ∈ V (M ′)\{u′}, the pair (u′, v′) is (k−degT (u′))-valid.
By Claim 1, both degT (u) and degT (u′) are at most max{1, ⌊t/2⌋ − 2}. Since G is 2-connected,
Lemma 4.9 guarantees the existence of vertices w ∈ V (M ) \ {u} and w′ ∈ V (M ′) \ {u′}, along
with two disjoint paths connecting {u, w} and {u′, w′} whose internal vertices lie in T . By
Observation 4.6, both P M
u,w and P M ′
u′,w′ contain at least k − max{1, ⌊t/2⌋ − 2} − 1 ≥ ⌈(k + 1)/2⌉
admissible paths. The union of these two path collections, together with the two connecting
paths, yields at least ⌈(k + 1)/2⌉ + ⌈(k + 1)/2⌉ − 1 ≥ k admissible cycles. If these cycles do
not cover r (mod k), the path lengths in P M
u,w must form a 2-AP. Since T is non-bipartite, we
can combine P M
u,w with a path in P T
u,w of a suitable parity to obtain ⌈(k + 1)/2⌉ admissible even
cycles, which must contain one of length r (mod k), a contradiction. This proves Claim 2.

Claim 3. No two consecutive vertices on ∂T have degrees that are both at most k − 1 in
V (T ) ∪ V (M ).

Proof. By Claim 2, each component of G − T − M has order at most two. Hence, every v ∈
V (G − T − M ) satisfies degG(v) ≤ 1 + degT (v) ≤ 1 + ⌊t/2⌋ < k − 1. Thus, |G − T − M | ≤ 1,
with equality only if G⋆ is of Type I and V (G − T − M ) = {θ}.
Recall ∂T = v0v1 . . . vt−1v0. Suppose for the sake of contradiction that there exist consecutive
vertices, say v0 and v1, such that their degrees in V (T ) ∪ V (M ) are at most k − 1.

17

If V (G − T − M ) ̸= ∅, then as noted above, V (G − T − M ) = {θ}. Since degG(v) ≥ k
for all v ̸= θ, the vertices v0 and v1 must be adjacent to θ. It follows that θ is adjacent to
consecutive vertices on ∂T , contradicting the maximality of T . Otherwise, V (G − T − M ) = ∅,
so degG(v0) ≤ k − 1 and degG(v1) ≤ k − 1. This implies G⋆ is of Type II and {v0, v1} = {θ1, θ2}.
Consequently, θ1θ2 ∈ E(G), which implies δ(G) ≥ k, a contradiction. This proves Claim 3.

Returning to the main proof, let u = uM . Choose distinct vertices vi ∈ NT (u) and vj ∈
NT (M − u) to minimize the distance dist∂T (vi, vj). Without loss of generality, we assume
the indices satisfy 0 ≤ i < j and the distance along the boundary is j − i ≤ t/2. By the
minimality of j − i, we have NM (vℓ) = ∅ for all i < ℓ < j. Since vj ∈ NT (M − u), there exists
a vertex w ∈ V (M ) \ {u} adjacent to vj. By Claim 1 and Observation 4.6, P M
u,w contains
k − max{1, ⌊t/2⌋ − 2} − 1 = min{k − 2, k − ⌊t/2⌋ + 1} admissible paths. We proceed by
distinguishing cases based on the order of T .
If t = 5, Observation 3.3 implies that P T
u,w always contains 3 consecutive paths. Conse-
quently, the union of paths in P M
u,w and P T
u,w yields at least (k − 2) + 3 − 1 = k consecutive
cycles, a contradiction.
If 6 ≤ t ≤ k, we must have j −i ∈ {1, 2}. Indeed, if j −i ≥ 3, then NM (vi+1) = NM (vi+2) = ∅.
This implies that both vi+1 and vi+2 have degree at most t − 1 ≤ k − 1 in V (T ) ∪ V (M ), which
contradicts Claim 3. By Proposition 3.2, P T
u,w contains t − 3 consecutive paths. The union of
paths in P M
u,w and P T
u,w thus produces at least (k −⌊t/2⌋+1)+(t−3)−1 = k +(t−⌊t/2⌋−3) ≥ k
consecutive cycles, a contradiction.
Finally, suppose t = k + 1. The case j − i ∈ {1, 2} follows the same reasoning as above. If
j − i ≥ 3, it follows from Claim 3 that at least one of vi+1, vi+2 must have degree k = t − 1 in T .
If degT (vi+1) = k, consider paths of the form vivi−1 . . . vαvi+1vβvβ+1 . . . vj, where α ∈ [j + 1, i]
and β ∈ [i + 2, j] are indices such that α, β have the same parity as i. This construction yields
LT
vi,vj ⊇ [2, t − 1]. If degT (vi+2) = k, the paths of the form vivi−1 . . . vαvi+2vβvβ+1 . . . vj (which
avoids vi+1) establish LT
vi,vj ⊇ [2, t − 2]. In either case, P T
u,w contains at least t − 3 consecutive
paths. The union of paths in P M
u,w and P T
u,w thus produces at least (k −⌊t/2⌋+1)+(t−3)−1 ≥ k
consecutive cycles, a contradiction. This finishes the proof of Lemma 5.6.

Now we are ready to complete the proof of Theorem 5.1.

Proof of Theorem 5.1. Theorem 5.1 follows from Lemma 5.2, which handles the triangle-
free case, and Lemmas 5.3, 5.4, 5.6, which collectively cover all possible cases of the maximum
trigonal subgraph T . This concludes the proof of Theorem 4.2 for the non-bipartite case.

We remark that for k ≥ 7, our proof in fact yields the existence of k admissible cycles; see
the following corollary. This case can be verified directly from the arguments, and is distinct
from the case k = 6, mainly due to differences in the proofs of Claim 1 in Lemmas 5.2 and 5.6.

Corollary 5.7. Let k ≥ 7 be an integer, and let G⋆ be a k-weak graph not isomorphic to Kk+1.
If G is non-bipartite, then G⋆ contains k admissible cycles.

6 Proof of Theorem 4.2: the bipartite case

In this section, we establish Theorem 4.2 for the case where G is bipartite via the following.

Theorem 6.1. Let k ≥ 6 be an integer, and let G⋆ be a k-weak graph not isomorphic to Kk,k
or Hk,n;t for any 2 ≤ t ≤ k < n. If G is bipartite, then G⋆ contains a cycle of length r (mod k)
for every even integer r.

Note that in bipartite graphs, a collection of k admissible cycles contains one of length r
(mod k) for every even r. For k ≥ 7, we obtain a stronger result for admissible cycles as follows.

Theorem 6.2. Let k ≥ 7 be an integer, and let G⋆ be a k-weak graph not isomorphic to Kk,k
or Hk,n;t for any 2 ≤ t ≤ k < n. If G is bipartite, then G⋆ contains k admissible cycles.

18

Throughout this section, we assume the conditions of Theorem 6.2:

k ≥ 7, G⋆ is not isomorphic to Kk,k or Hk,n;t for any 2 ≤ t ≤ k < n, and G is bipartite.

The main bulk of this section is used to prove Theorem 6.2. We conclude this section by
establishing Theorem 6.1 via Theorem 6.2 and outlining the proof of Theorem 1.4.

6.1 No tetragonal subgraph on six vertices

Our first lemma treats the C4-free case, using a minimal induced cycle as the core subgraph.

Lemma 6.3. If G is C4-free, then G⋆ contains k admissible cycles.

Proof. Let C = v0v1 · · · v2s−1v0 (s ≥ 3) be an induced cycle in G with |C| = 2s minimized.
We first show that for any vertex v ∈ V (G − C), degC(v) ≤ 1. Suppose to the contrary that
degC(v) ≥ 2. Without loss of generality, assume that v0, vi ∈ NC(v) for some even index i ∈ [s],
and v1, . . . , vi−1 /∈ NC(v). Then vv0v1 . . . viv is an induced cycle of length i + 2 ≤ s + 2 < 2s,
which contradicts the minimality of |C|. Since δ(G) ≥ 3, every vertex in C must have a
neighbor in G − C, which implies G − C ̸= ∅. Moreover, for any component M of G − C, we
have δ(M ) ≥ δ(G) − 1 ≥ 2, and thus |M | ≥ 3.
Suppose first that G − C is not connected. Let M1 and M2 be two distinct components
of G − C. For i ∈ {1, 2}, let ui = uMi (see Definition 4.7). By Lemma 4.8, for any vertex
v ∈ V (Mi) \ {ui}, the pair (ui, v) is (k − 1)-valid. By Lemma 4.9, there exist vertices wi ∈
V (Mi) \ {ui} and two disjoint paths between {u1, w1} and {u2, w2} in G whose internal vertices
lie in C. By Observation 4.6, P Mi
ui,wi contains k−2 admissible paths. The union of paths in P M1
u1,w1
and P M2
u2,w2, together with the two connecting paths, produces at least (k − 2) + (k − 2) − 1 > k
admissible cycles.
Now assume that M := G − C is connected, so |M | ≥ 3. Let u = uM . Without loss
of generality, we assume NC(u) = {v0}. Since every vertex in C has a neighbor in M , there
exists w ∈ V (M ) adjacent to vs−2. Since s ≥ 3, we have vs−2 ̸= v0, which implies w ̸= u. By
Observation 4.6 and Lemma 4.8, P M
u,w contains k − 2 admissible paths. One can verify that
LC
u,w = {s, s + 4}. Since k ≥ 6, the union of paths in P M
u,w and P C
u,w produces k admissible
cycles. This completes the proof.

Throughout the rest of this section, we assume that C4 ⊆ G, and

let T be an optimal tetragonal subgraph of G (recall Definition 3.6).

The remainder of the proof is divided according to the order of T : Lemmas 6.4 and 6.5 consider
the case |T | = 4, while Lemma 6.6 handles the case |T | > 4.
In the following two lemmas, we utilize a subgraph K2,t with maximum t as the core subgraph.

Lemma 6.4. If G⋆ is of Type I and |T | = 4, then G contains k admissible cycles.

Proof. Recall that G = G⋆ since G⋆ is of Type I. Let K ≃ K2,t (with t ≥ 2) be a subgraph of G
that maximizes t. Let (X, Y ) denote the partite sets of K such that |X| = 2 and |Y | = t. The
maximality of K and T implies that degK(v) ≤ 1 for every vertex v ∈ V (G − K).
Suppose first that there exists a component M of G − Y such that V (M ) ∩ X = ∅. Then
Y separates X from M in G. Since G is 3-connected, we must have |NY (M )| ≥ 3. This
implies |Y | ≥ 3. Moreover, since degY (v) = degK(v) ≤ 1 for every v ∈ V (M ), we also have
|M | ≥ |NY (M )| ≥ 3. Fix a vertex u ∈ NY (M ) and let W := Y \ {u}. Let H be the graph
obtained from G[V (M ) ∪ Y ] by contracting W into a single vertex w. Since both u and W
have neighbors in M , (H, u, w) is a 2-connected rooted graph with δ2(H, u, w) ≥ δ2(G) ≥ k and
|H| ≥ |M | + 2 > 4. By Lemma 2.3, there exist k − 1 admissible (u, w)-paths in H. Lifting
this back to G, this implies that the path collection ⋃v∈W P M
u,v contains k − 1 admissible paths.
Since |Y | ≥ 3, for any v ∈ W , we have LK
u,v = {2, 4}. Consequently, combining the paths in
⋃v∈W P M
u,v with those in P K
u,v yields (k − 1) + 2 − 1 = k admissible cycles, which suffices.

19

Consequently, we may assume that every component of G − Y intersects X. Let G′ be
the graph obtained from G by contracting X into a vertex x and Y into a vertex y. Since
δ2(G) ≥ k, G − K is non-empty. Let L be an arbitrary component of G − K. Similar to the
previous paragraph, we have |L| ≥ |NK(L)| ≥ 3. By our assumption, NX (L) ̸= ∅. Since |X| = 2
and G is 3-connected, X cannot be a 2-cut; thus NY (L) ̸= ∅. It follows that (G′, x, y) is a
2-connected rooted graph with |G′| ≥ |L| + 2 > 4 and δ2(G′, x, y) ≥ k. By Lemma 2.3, there
are k − 1 admissible (x, y)-paths in G′. Equivalently, in terms of G, the union ⋃u∈X,v∈Y P G−K
u,v
contains k − 1 admissible paths. Observe that for any u ∈ X and v ∈ Y , we have LK
u,v = {1, 3}.
Therefore, combining the paths in P G−K
u,v (where u ∈ X, v ∈ Y ) with the paths in P K
u,v produces
(k − 1) + 2 − 1 = k admissible cycles. This proves Lemma 6.4.

Lemma 6.5. If G⋆ is of Type II and |T | = 4, then G⋆ contains k admissible cycles.

Proof. Let K ≃ K2,t be a subgraph of G that maximizes t, and let (X, Y ) be its partite sets
with |X| = 2 and |Y | = t. The maximality of K and T implies that degK(v) ≤ 1 for any
v ∈ V (G − K).
Suppose first that there exists a component M of G − Y such that V (M ) ∩ X = ∅. Then
Y separates X from M in G. For any v ∈ V (M ), we have degM (v) = degG(v) − degK(v) ≥
(k−1)−1 = k−2, which implies |M | ≥ k−1 ≥ 6. Fix a vertex u ∈ NY (M ) and let W := Y \{u}.
Let H be the graph obtained from G[V (M ) ∪ Y ] by contracting W into a vertex w. Since u is
not a cut-vertex in G (as G is 2-connected), both u and W have neighbors in M , so (H, u, w) is
a 2-connected rooted graph.
We distinguish two cases based on the location of θ1 and θ2. If |V (M ) ∩ {θ1, θ2}| ≤ 1, then
clearly δ2(H, u, w) ≥ k. If {θ1, θ2} ⊆ V (M ), let H ′ be the graph obtained from G⋆[V (M ) ∪
Y ∪ {θ}] by contracting W into a vertex w. Observe that H ′ is obtained from H by adding the
vertex θ and the edges θθ1, θθ2. Since (H, u, w) is a 2-connected rooted graph, it follows that
(H ′, u, w) is also 2-connected, and it is clear that δ2(H ′, u, w) ≥ k. Applying Lemma 2.3 to H
(in the first case) or H ′ (in the second case), we always find k − 1 admissible (u, w)-paths in H ′.
In either case, the path collection ⋃v∈W P G⋆[V (M )∪{θ}]
u,v contains k − 1 admissible paths.
Now consider paths whose internal vertices lie in K, based on the size of Y . If t ≥ 3, then
for any v ∈ W , we have LK
u,v = {2, 4}. Combining these with the k − 1 admissible paths in
⋃v∈W P G⋆[V (M )∪{θ}]
u,v yields (k − 1) + 2 − 1 = k admissible cycles in G⋆. If t = 2, since G + θ1θ2
is 3-connected, the graph (G + θ1θ2) − Y must be connected. Consequently, G − Y contains
exactly one component N distinct from M , and each component contains exactly one of θ1, θ2.
N (distinct from M ) such that one of θ1, θ2 lies in M and the other in N . Let Y = {y1, y2}.
The 2-connectivity of G implies that both (G[V (M ) ∪ Y ], y1, y2) and (G[V (N ) ∪ Y ], y1, y2) are
2-connected rooted graphs, and one can readily verify that their second minimum degrees are
at least k. By Lemma 2.3, both P M
y1,y2 and P N
y1,y2 contain k − 1 admissible paths. The union of
these paths yields (k − 1) + (k − 1) − 1 > k admissible cycles in G (and thus in G⋆). This settles
the case where a component M of G − Y is disjoint from X.
It remains to assume that every component of G − Y intersects X. Let G′ be the graph
obtained from G⋆ by contracting X into x and Y into y. Recall that {θ1, θ2} is the unique
2-cut in G⋆. We proceed by discussing the position of {θ1, θ2}. If {θ1, θ2} ̸= X, then X is not a
2-cut in G⋆. Thus, every component of G⋆ − K has a neighbor in Y (in the host graph G⋆); by
assumption, this component also has a neighbor in X. It follows that (G′, x, y) is a 2-connected
rooted graph with δ2(G′, x, y) ≥ k. If {θ1, θ2} = X, then X is not a cut in G (as G + θ1θ2 is
3-connected). Thus, every component of G − K has neighbors both in X and Y . Note that
G = G⋆ −θ. We deduce that (G′ −θ, x, y) is a 2-connected rooted graph with δ2(G′ −θ, x, y) ≥ k.
Applying Lemma 2.3 to (G′, x, y) or (G′ − θ, x, y), we obtain k − 1 admissible (x, y)-paths in G′.
This implies that ⋃u∈X,v∈Y P G⋆−K
u,v contains k − 1 admissible paths. Since LK
u,v = {1, 3} for any
u ∈ X, v ∈ Y , combining the corresponding path families yields (k − 1) + 2 − 1 = k admissible
cycles in G⋆. This completes the proof of Lemma 6.5.

20

6.2 Tetragonal subgraphs of order at least six

This subsection is devoted to the case |T | ≥ 6, constituting the bulk of the proof of Theorem 6.2.

Lemma 6.6. If |T | ≥ 6, then G⋆ contains k admissible cycles.

By Proposition 3.5, a tetragonal graph on at least 2k +2 vertices contains cycles of all lengths
in {4, 6, . . . , 2k + 2}. Thus, for the proof of Lemma 6.6, we may assume that |T | = 2m with
m ∈ [3, k]. Let R := {v ∈ V (G−T ) : degT (v) ≥ m−1}. In the following proof of this subsection,

the subgraph T ∗ := G[V (T ) ∪ R] will be used as the core subgraph of G.

We refer to Lemma 3.7 for properties of T and R. Our subsequent analysis mainly relies
on examining the structural properties of the components of G − T ∗. Specifically, Lemmas 6.8
and 6.15 investigate components of order at most two, whereas Lemmas 6.9 through 6.14 (except
for Lemma 6.10 dealing with an extreme case) focus on components of order at least three.
The following lemma characterizes the set of path lengths LT ∗
u,v.

Lemma 6.7. Let u1, u2 be two distinct vertices in V (G − T ∗) with positive degrees d1 :=
degT ∗(u1) and d2 := degT ∗(u2). Then one of the following statements holds:

(1) P T ∗
u1,u2 contains at least min{d1 + d2 − 1, m} admissible paths.

(2) LT ∗
u1,u2 ⊇ {2} ∪ {2 + d, 4 + d, . . . , 2m + 2 − d} for some even d ≤ max{2, 2m/ max{d1, d2},
m − d1 − d2 + 3}.

Proof. By Lemma 3.7 (4), for each i ∈ {1, 2}, we have either degT (ui) = 0 or degR(ui) = 0. We
proceed by discussing the degrees of u1 and u2 in R.
First, suppose that both degR(u1) and degR(u2) are positive. It follows from Lemma 3.7 (4)
that d1 = d2 = 1. Thus, item (1) holds, as min{d1 + d2 − 1, m} = 1.
Next, consider the case where exactly one of degR(u1) and degR(u2) is positive. Without
loss of generality, assume degR(u1) > 0. Then Lemma 3.7 (4) implies d1 = 1 and d2 ≤ m − 2.
Let NR(u1) = {p}. Recall that degT (p) ≥ m − 1. By Lemma 2.5 (2), there exist distinct vertices
v1 ∈ NT (p) and v2 ∈ NT (u2) such that dist∂T (v1, v2) ≤ 3. By Proposition 3.5, P T
p,u2 contains at
least m − dist∂T (v1, v2) + 1 ≥ m − 2 ≥ d1 + d2 − 1 admissible paths. Consequently, P T ∗
u1,u2 also
contains d1 + d2 − 1 admissible paths (extended by the edge u1p), so item (1) follows.
Finally, assume that degR(u1) = degR(u2) = 0. If d1 = d2 = 1, then d1 + d2 − 1 = 1,
and item (1) holds trivially. Suppose now that max{d1, d2} ≥ 2. If NT (u1) ∩ NT (u2) = ∅,
then Lemma 2.5 (1) implies that u1 and u2 have neighbors in T with distance along ∂T
at most max{1, m + 2 − d1 − d2}. It follows from Proposition 3.5 that P T
u1,u2 contains
min{d1 + d2 − 1, m} admissible paths, satisfying (1). Otherwise, if NT (u1) ∩ NT (u2) ̸= ∅,
Lemma 2.5 (2) ensures that they have distinct neighbors in T whose distance along ∂T is
bounded by max{3, 2m/ max{d1, d2}, m − d1 − d2 + 3}. In this scenario, Proposition 3.5 implies
that LT
u1,u2 (and thus LT ∗
u1,u2) includes {2} ∪ {2 + d, 4 + d, . . . , 2m + 2 − d} for some even integer
d ≤ max{2, 2m/ max{d1, d2}, m − d1 − d2 + 3}, satisfying (2).

Towards the proof of Lemma 6.6, we then present several lemmas that analyze the structures
of G − T ∗. We first describe the components of G − T ∗ of order at most two. Let N be the
graph obtained from G − T ∗ by deleting all components of order at least three.

Lemma 6.8. The graph N satisfies the following properties:

(1) |V (N )| ≤ 1, and |V (N )| = 1 implies that G⋆ is of Type I and V (N ) = {θ}.

(2) R ∪ V (N ) is an independent set.

Proof. Since every component in N has order at most two, it follows that for every v ∈ V (N ),
degG(v) = degT ∗(v) + degN (v) ≤ (m − 2) + 1 ≤ k − 1, which implies N has order at most two.

21

If |V (N )| = 2, then the inequality above must be an equality. This forces G⋆ to be of Type
II, N to be the edge θ1θ2, and degG(θ1) = degG(θ2) = k − 1. However, the existence of the edge
θ1θ2 in G implies δ(G) ≥ k, a contradiction.
Thus, we must have |V (N )| ≤ 1. When V (N ) = {v}, we have degG(v) = degT ∗(v) ≤ m−2 ≤
k − 2, which implies that G⋆ is of Type I and v = θ. This completes the proof of (1).
For (2), suppose to the contrary that R ∪ V (N ) is not independent. Recall Lemma 3.7 (2)
that R is independent, so V (N ) ̸= ∅. By (1), G⋆ is of Type I and V (N ) = {θ}. Recall that
degG(θ) ≥ δ(G) ≥ 3. By Lemma 3.7 (4), we have degR(θ) = 0, implying that R ∪ V (N ) remains
an independent set, a contradiction. This proves (2).

The following lemma shows that for every component M of G−T ∗ with at least three vertices,
it suffices to consider that the corresponding end-block BM (See Definition 4.7) contains at least
four vertices.

Lemma 6.9. Let M be a component of G − T ∗ of order at least 3. If |BM | ≤ 3, then G contains
k admissible cycles.

Proof. We note that |BM | ̸= 3, as otherwise BM ≃ K3, contradicting the fact that G is bipartite.
Suppose |BM | = 2. Then uM is the unique vertex in V (BM ) \ Cut(BM ). By Lemma 3.7 (4),
degT ∗(uM ) ≤ m − 2, and thus degG(uM ) = 1 + degT ∗(uM ) ≤ 1 + (m − 2) = m − 1 ≤ k − 1. Hence,
G⋆ must be of Type II, for otherwise G⋆ is of Type I and uM must be θ, which contradicts the
condition that θ /∈ V (BM ) \ Cut(BM ). It follows that the inequality for degG(uM ) must hold
with equality. Specifically, we derive that uM ∈ {θ1, θ2}, m = k ≥ 6, and degT ∗(uM ) = k − 2.
Recall from Definition 4.7 that BM is chosen to be an end-block of maximum order satisfying
the stated conditions. Thus, any other end-block B of M (which already satisfies that V (B) \
Cut(B) contains at most one of θ1 and θ2) must also satisfy |B| ≤ 2. This further implies
that the unique vertex in V (B) \ Cut(B) must be in {θ1, θ2}. It follows that M has exactly
two end-blocks, say BM and B, with V (BM ) \ Cut(BM ) = {θ1}, V (B) \ Cut(B) = {θ2}, and
degT ∗(θ1) = degT ∗(θ2) = k − 2. A routine calculation verifies that each case of Lemma 6.7 yields
k admissible paths in P T ∗
θ1,θ2. Therefore, the union of an arbitrary path in P M
θ1,θ2 and paths in
P T ∗
θ1,θ2 produces k admissible cycles in G. This completes the proof.

Now we consider the special case G[V (T )] ≃ Kk,k.

Lemma 6.10. If m = k and G[V (T )] ≃ Kk,k, then G⋆ contains k admissible cycles.

Proof. Suppose for the sake of contradiction that G[V (T )] ≃ Kk,k but G⋆ does not contain k
admissible cycles. We proceed by analyzing the components of G − T ∗.
First, assume that G − T ∗ has a component M of order at least 3. Let u = uM , and let
v ∈ V (M ) \ {u} be a vertex maximizing degT ∗(v). Additionally, if degT ∗(u) = 1, we may
assume NT ∗(v) ̸= NT ∗(u), since the unique neighbor of u in T ∗ cannot be a cut-vertex in G. By
Lemma 3.7 (4), we have 1 ≤ degT ∗(u), degT ∗(v) ≤ k − 2. Consider the sum degT ∗(u) + degT ∗(v).
If degT ∗(u) + degT ∗(v) ≥ k + 1, then degT ∗(u), degT ∗(v) ≥ 3. It follows from Lemma 3.7 (4)
that degR(u) = degR(v) = 0. Since G[V (T )] ≃ Kk,k, the set LT
u,v contains k admissible lengths.
Specifically, LT
u,v = {3, 5, . . . , 2k + 1} if u and v belong to different partite sets, and LT
u,v =
{2, 4, . . . , 2k} otherwise (as u and v share a common neighbor in T ). Hence, the union of an
arbitrary path in P M
u,v with paths in P T
u,v yields k admissible cycles, a contradiction.
Now assume that degT ∗(u) + degT ∗(v) ≤ k. By Lemma 6.9, we have |BM | ≥ 4. By the choice
of u and v, every vertex w ∈ V (BM ) \ {u, v} satisfies degT ∗(w) ≤ min{degT ∗(u), degT ∗(v)} ≤
⌊k/2⌋. Observe that degG(w) ≥ k − 1 holds for all w ∈ V (BM )—except possibly for θ if M is
2-connected, or the vertex in Cut(BM ) otherwise. It follows that for all but at most one vertex
w ∈ V (BM ) \ {u, v}, degBM (w) = degG(w) − degT ∗(w) ≥ k − 1 − ⌊k/2⌋ ≥ 3. Consequently, the
pair (u, v) is 3-valid, and P M
u,v contains 2 admissible paths. Since G[V (T )] ≃ Kk,k, and u, v are
adjacent to distinct vertices in T ∗ (due to the selection of v), it follows that P T ∗
u,v contains k − 1
admissible paths. The union of paths in P M
u,v and P T ∗
u,v thus yields 2 + (k − 1) − 1 = k admissible
cycles.
 22

It remains to consider the case where every component of G − T ∗ has order at most 2, i.e.,
G − T ∗ = N . Let (A, B) be the partite sets of G. We claim that V (G − T ) = R ∪ V (N )
is contained entirely in A or B. If V (N ) = ∅, then the claim follows from Lemma 3.7 (3).
Assume V (N ) ̸= ∅. It follows from Lemma 6.8 that G⋆ is of Type I, V (N ) = {θ}, and R ∪ {θ}
is an independent set. Suppose the claim is false; then there exist a ∈ A ∩ (R ∪ {θ}) and
b ∈ B ∩ (R ∪ {θ}). Every vertex in R has degree at least k − 1 ≥ 6 in T , and degT (θ) ≥ δ(G) ≥ 3;
thus degT (a), degT (b) ≥ 3. Since G[V (T )] ≃ Kk,k, and a, b have at least three neighbors in
distinct partite sets of T , a routine verification confirms that G[V (T ) ∪ {a, b}] contains cycles of
all lengths in {4, 6, . . . , 2k + 2}, a contradiction. This proves the claim; hence, we may assume
R ∪ V (N ) ⊆ A.
We conclude by discussing the type of G⋆. If G⋆ is of Type I, then every vertex in R ∪ V (N )
(with the exception of θ) has degree k in T , hence must be fully connected to V (T ) ∩ B.
Consequently, G⋆ is obtained from G[V (T )] ≃ Kk,k by adding vertices to A that are adjacent
to all vertices in B, with the possible exception of one vertex (namely θ) that is adjacent to at
least three vertices in B. Thus, G⋆ is isomorphic to Kk,k or Hk,n;t for some 3 ≤ t ≤ k < n, a
contradiction. If G⋆ is of Type II, then Lemma 6.8 implies V (N ) = ∅. Moreover, every p ∈ R
has at least k −1 neighbors in V (T )∩B. One can verify that for any distinct a, a′ ∈ A and b ∈ B,
we have LG
a,a′ ⊇ L
V (T )∪{p}
a,a′ ⊇ {2, 4, . . . , 2k} and LG
a,b ⊇ LT
a,b ⊇ {1, 3, . . . , 2k − 1}. If θ1, θ2 ∈ A or if
they belong to different partite sets, then P G
θ1,θ2 contains k admissible paths. Combined with the
path θ1θθ2, we obtain k admissible cycles in G⋆. If θ1, θ2 ∈ B, then R ∩ {θ1, θ2} = ∅ (as R ⊆ A).
Thus, every p ∈ R has degG(p) ≥ k, forcing degT (p) = k (i.e., p is adjacent to all vertices in
B). This implies that G ≃ Kk,n−1 for some n > k, and thus G⋆ ≃ Hk,n;2, a contradiction. This
completes the proof.

Recall that K−
n,n is the graph obtained from Kn,n by removing an edge. The following lemma
considers the case that G − T ∗ contains no component of order at least three.

Lemma 6.11. If G−T ∗ does not contain any component of order at least three, then G⋆ contains
k admissible cycles.

Proof. The assumption implies G − T ∗ = N . By Lemma 6.10, we may assume G[V (T )] ̸≃ Kk,k.
Then Lemma 3.7 (1) implies that every p ∈ R satisfies degT (p) ≤ k −1. Let (A, B) be the partite
sets of G, and select vertices a ∈ A∩V (T ), b ∈ B ∩V (T ) satisfying that degT (a), degT (b) ≤ k −1.
Suppose first that V (N ) ̸= ∅. By Lemma 6.8, G⋆ is of Type I, V (N ) = {θ}, and R ∪ V (N )
is independent. Thus, every p ∈ R has degG(p) ≤ degT (p) ≤ k − 1, implying that R = ∅.
However, one of a, b is not adjacent to θ. This vertex would then have degree less than k in G,
a contradiction.
Thus, we assume V (N ) = ∅. We claim that the set {a} ∪ NR(a) contains a vertex with
degree at most k − 1 in G. Indeed, if NR(a) = ∅, then degG(a) = degT (a) ≤ k − 1. If NR(a) ̸= ∅,
then every p ∈ NR(a) has degG(p) = degT (p) ≤ k − 1, proving the claim. The same holds for
{b} ∪ NR(b). Hence, G⋆ must be of Type II, and each of {a} ∪ NR(a) and {b} ∪ NR(b) contains
exactly one of θ1, θ2. Also, we have θ1θ2 /∈ E(G) (otherwise δ(G) ≥ k).
We distinguish three cases regarding the locations of θ1 and θ2. First, assume that {θ1, θ2} =
{a, b}. In this case, we must have R = ∅, and every vertex in V (T ) \ {a, b} has degree k in T .
Consequently, G[V (T )] ≃ K−
k,k. It follows that G⋆ = G + {θθ1, θθ2} contains cycles of all lengths
in [4, 2k + 1], as desired.
Next, suppose that θ1 = a and θ2 ∈ NR(b) (the symmetric case is analogous). Then R =
{θ2}. Since θ2 is adjacent to all but at most one vertex in V (T ) ∩ B, there exists a neighbor
c ∈ NT (θ2) ⊆ B such that c is adjacent to θ1 on ∂T . Thus, G⋆ = G + {θθ1, θθ2} contains a
tetragonal graph on 2k + 2 vertices, whose boundary cycle is obtained from ∂T by replacing
the edge θ1c with the path θ1θθ2c. By Proposition 3.5, G⋆ contains cycles of all lengths in
{4, 6, . . . , 2k + 2}, which suffices.
Finally, consider the case where θ1 ∈ NR(a) and θ2 ∈ NR(b). Then R = {θ1, θ2}. Observe
that k ≤ degG(a) ≤ 1 + m, which implies m ≥ 5. By Lemma 3.7 (3), R is entirely contained

23

in A or B. However, since a ∈ A and b ∈ B, we necessarily have θ1 ∈ B and θ2 ∈ A. Thus, R
intersects both partite sets, a contradiction. This completes the proof.

According to Lemma 6.11, we may assume that G − T ∗ has a component of order at least
three. Let M be such a component. The following lemma reduces the proof to the scenario
where the degrees of vertices in M are highly constrained.

Lemma 6.12. If there exists w ∈ V (M ) with degT ∗(w) ≥ 3, then G has k admissible cycles.

Proof. Let u denote uM . By Lemma 6.9, we may assume that |BM | ≥ 4. Select a vertex
v ∈ V (M ) \ {u} as follows.

(1) degT ∗(v) = max{degT ∗(w) : w ∈ V (M ) \ {u}}.

(2) Subject to (1), degG(v) is minimum.

Let dmin = min{degT ∗(u), degT ∗(v)} and dmax = max{degT ∗(u), degT ∗(v)}. Then dmax ≥ 3
by the hypothesis, and Lemma 3.7 (4) implies that both dmin and dmax are at most m − 2.
Moreover, we have dmin ≥ 1, since degT ∗(u) ≥ 1 holds by definition, while degT ∗(v) ≥ 1 follows
from the fact that u is not a cut-vertex of G. Combining these bounds yields 1 ≤ dmin ≤ m − 2
and 3 ≤ dmax ≤ m − 2, which forces m ≥ 5.
Using an argument analogous to Lemma 4.8, we deduce that (u, v) is (k − dmin)-valid. In
fact, the proof of Lemma 4.8 relied on the fact that degT ∗(w) ≤ degT ∗(u) for every w ∈ V (BM ) \({u} ∪ Cut(BM )
). Here, by the maximality of degT ∗(v), every w ∈ V (BM ) \ ({u} ∪ Cut(BM )
)

satisfies degT ∗(w) ≤ degT ∗(v), and thus degT ∗(w) ≤ dmin. Substituting this stronger inequality
into the proof of Lemma 4.8 confirms that (u, v) is (k − dmin)-valid. By Observation 4.6, P M
u,v
contains k − dmin − 1 admissible paths. Let L1 denote the set of lengths of these admissible
paths. According to Lemma 6.7, LT ∗
u,v contains a subset L2 with one of the following forms:

• An admissible set of size at least min{dmin + dmax − 1, m};

• {2}∪{2+d, 4+d, · · · , 2m+2−d} for some even d ≤ max{2, 2m/dmax, m−dmin −dmax +3}.

We verify that L1 + L2 is an admissible set of size at least k. If L2 is of the former case, since
3 ≤ dmax ≤ m − 2, the sum L1 + L2 is an admissible set of length at least (k − dmin − 1) +
min{dmin + dmax − 1, m} − 1 ≥ k. In the latter case, the condition for L1 + L2 to form an
admissible set is equivalent to:

d ≤ max{L1} − min{L1} + 2 ⇐⇒ d ≤ 2(k − dmin − 1)

This is guaranteed by the following strict inequality, since d is even.

d ≤ max{2, 2m/dmax, m − dmin − dmax + 3} (∗)
< 2(m − dmin) ≤ 2(k − dmin),

where (∗) is implied by the following three inequalities (as m ≥ 5):

2(m − dmin) ≥ 4 > 2,

2(m − dmin) ≥ 2(m − dmax) > 2m/dmax, and

2(m − dmin) > m − 2dmin + 3 ≥ m − dmin − dmax + 3.

Therefore, L1 + L2 is an admissible set with minimum element min{L1} + 2 and maximum
element max{L1} + max{L2}, thus has size

max{L1} − min{L1} + max{L2}
2 = k + m − dmin − d/2 − 1.

Note that k + m − dmin − d/2 − 1 ≥ k is equivalent to d ≤ 2(m − dmin − 1), which we have already
established via inequality (∗). Hence, L1 + L2 is an admissible set of size at least k, and the
union of paths in P M
u,v and P T ∗
u,v produces k admissible cycles in G. This completes the proof of
Lemma 6.12.
 24

The following lemma addresses the case where G−T ∗ has two components of order at least 3.

Lemma 6.13. If G − T ∗ has two components of order ≥ 3, then G has k admissible cycles.

Proof. Suppose for a contradiction that G − T ∗ contains two distinct components M1 and M2,
both of order at least 3, yet G does not contain k admissible cycles. By Lemma 6.12, every
vertex v ∈ V (M1) ∪ V (M2) satisfies degT ∗(v) ≤ 2.
For i ∈ {1, 2}, let ui = uMi. Since G is 2-connected, Lemma 4.9 guarantees the existence of
vertices wi ∈ V (Mi) \ {ui} for each i, along with two disjoint ({u1, w1}, {u2, w2})-paths whose
internal vertices lie in T ∗. By Observation 4.6 and Lemma 4.8, the set P Mi
ui,wi contains at least
k − degT ∗(ui) − 1 ≥ k − 3 admissible paths. Consequently, the union of the paths in P M1
u1,w1 and
P M2
u2,w2, together with the two connecting paths, yields at least (k − 3) + (k − 3) − 1 = 2k − 7 ≥ k
admissible cycles in G, a contradiction. This completes the proof.

By Lemma 6.13, we may henceforth assume that M is the only component of G − T ∗ of
order at least three. The following lemma further restricts the neighborhood of vertices in M .

Lemma 6.14. If E(M, R) ̸= ∅, then G contains k admissible cycles.

Proof. Suppose for the sake of contradiction that E(M, R) ̸= ∅, yet G⋆ does not contain k
admissible cycles. Let (A, B) be the partite sets of G, and let u denote uM . By Lemmas 3.7 (4)
and 6.12, we have degT ∗(u) ≤ min{2, m − 2}.
We first rule out a specific configuration by showing that its existence yields k admissible
cycles. We say that a triple (v, x, y) is a forbidden triple if v ∈ V (M ) \ {u}, xy ∈ E(∂T ),
and there exist two disjoint (M, T )-paths connecting {u, v} to {x, y}. If such a triple exists,
by Observation 4.6 and Lemma 4.8, P M
u,v contains k − degT ∗(u) − 1 ≥ k − m + 1 admissible
paths. By Proposition 3.5, P T
x,y contains m admissible paths. Consequently, the union of paths
in P M
u,v and P T
x,y, together with the two connecting paths, yields at least (k − m + 1) + m − 1 = k
admissible cycles. Consequently, the existence of a forbidden triple yields a contradiction.
We then claim that R is contained in either A or B. Recall from Lemma 3.7 (3) that this
property already holds when m ≥ 4; thus, we may assume m = 3 (i.e., T consists of two 4-cycles
sharing one edge). In this case, degT ∗(u) = 1. Suppose the claim is false. Let a ∈ R ∩ A
and b ∈ R ∩ B be arbitrary vertices. A routine verification confirms that if degT (a) = 3 (or
degT (b) = 3), then V (T ) ∪ {a, b} would span a larger tetragonal subgraph, a contradiction.
Hence, we must have degT (a) = degT (b) = 2. Recall from Lemma 6.8 that a, b have no neighbor
in N . Given that δ(G) ≥ 3, both a and b must have at least one neighbor in M . We now identify
a forbidden triple as follows. Fix an arbitrary (M, T )-path L (which must have length ≤ 2) that
connects u to some x ∈ V (T ). Without loss of generality, assume x ∈ A. Then there exists
y ∈ NT (a) such that xy ∈ E(∂T ). Let v be an arbitrary vertex in the non-empty set NM (a).
Note that v ̸= u; otherwise, u would be adjacent to both x ∈ V (T ) and a ∈ R, contradicting
Lemma 3.7 (4). Thus, we obtain the disjoint paths L and vay, confirming that (v, x, y) is a
forbidden triple, a contradiction. This proves the claim.
In view of the claim, we may assume without loss of generality that R ⊆ A. We proceed by
discussing the order of T .
For the case m ≤ 4, since δ2(G) > k − 1 ≥ 5 ≥ m + 1, it follows that at most one vertex in
V (T ) ∩ A has no neighbor in M . Recall from Lemma 3.7 (4) that NT ∗(u) is contained in either
V (T ) or R. We consider the specific location of NT ∗(u).
If NT ∗(u) is contained in V (T ) ∩ B or R, then there exists an (M, T )-path L connecting u
to some vertex x ∈ V (T ) ∩ B. Let y ∈ V (T ) ∩ A be adjacent to x on ∂T such that NM (y) ̸= ∅,
and select an arbitrary neighbor v ∈ NM (y). As established before, we must have v ̸= u. Thus,
the disjoint paths L and vy force (v, x, y) to be a forbidden triple, a contradiction.
Suppose instead that NT ∗(u) ⊆ V (T ) ∩ A. Take any x ∈ NT ∗(u). Since E(M, R) ̸= ∅, there
exist vertices p ∈ R ⊆ A and v ∈ NM (p) ⊆ B. Since degT (p) ≥ m − 1, p must be adjacent to
some y ∈ V (T ) ∩ B such that xy ∈ E(∂T ). As established before, we have v ̸= u, which derives
disjoint (M, T )-paths ux and vpy. Hence, (v, x, y) is a forbidden triple, a contradiction.

25

Finally, consider the case where m ≥ 5. Since E(M, R) ̸= ∅, we may select v ∈ V (M ) \ {u}
such that either u or v is adjacent to some r ∈ R. By Observation 4.6 and Lemma 4.8, P M
u,v
contains k − degT ∗(u) − 1 ≥ k − 3 admissible paths. Since degT (r) ≥ m − 1, there are disjoint
(M, T )-paths that connects {u, v} to vertices with distance on ∂T at most two. By Lemma 2.5,
P T
u,v contains m−1 admissible paths. The union of these paths produces (k −3)+(m−1)−1 ≥ k
admissible cycles, a contradiction. This completes the proof.

Based on the previous analysis in the proof of Lemma 6.6, we may assume that G − T ∗

contains exactly one component, denoted by M , of order at least 3. Furthermore, every vertex
in M has degree at most min{2, m − 2} in T ∗, and E(M, R) = ∅. These facts allow us to impose
further constraints on N = G − T ∗ − M , as stated in the following lemma.

Lemma 6.15. If G⋆ does not contain k admissible cycles, then one of the following holds:

• G⋆ is of Type I, and R ∪ V (N ) ⊆ {θ}.

• G⋆ is of Type II, m = k − 1, and V (N ) = R = ∅.

• G⋆ is of Type II, m = k, V (N ) = ∅, and R ⊆ {θ1, θ2}.

In particular, R ∪ V (N ) is contained in one of the partite sets of G.

Proof. We first show that R ∪ V (N ) is a subset of {θ} (for Type I) or {θ1, θ2} (for Type
II). It suffices to show that every p ∈ R satisfies degG(p) ≤ k − 1. By Lemma 6.8 (2) and
Lemma 6.14, for every p ∈ R, we have NG(p) ⊆ V (T ), and thus degG(p) = degT (p) ∈ {m−1, m}.
Consequently, the conclusion follows immediately when m < k. Now assume that m = k. By
Lemma 6.10, G[V (T )] is not isomorphic to Kk,k. It then follows from Lemma 3.7 (1) that every
p ∈ R has degT (p) = k − 1. This confirms that R ∪ V (N ) is included in {θ} or {θ1, θ2}.
Next, consider the case where G⋆ is of Type II. By Lemma 6.8 (1), N must be empty. Observe
that every vertex p ∈ R (if any) satisfies k − 1 ≤ degG(p) = degT (p) ≤ m. Consequently, if
R ̸= ∅, we must have m ∈ {k − 1, k}. It remains to show that if m = k − 1, then R = ∅.
Suppose for a contradiction that R ̸= ∅, then the inequality above becomes an equality, implying
that every p ∈ R has degT (p) = m = k − 1. By Lemma 3.7 (1), we have T ≃ Kk−1,k−1. Let
u = uM . According to Observation 4.6 and Lemma 4.8, for every v ∈ NM (T )\{u}, P M
u,v contains
k − degT ∗(u) − 1 ≥ k − 3 admissible paths. Since T ≃ Kk−1,k−1, P T
u,v contains k − 2 admissible
paths. The union of paths in P M
u,v and P T
u,v thus yields at least (k − 3) + (k − 2) − 1 = 2k − 6 > k
admissible cycles, a contradiction.
The final claim, that R∪V (N ) lies in a single partite set, is trivial when G⋆ is of Type I. When
G⋆ is of Type II, we have m ≥ k − 1 > 4, and the claim follows directly from Lemma 3.7 (3).

Now we are ready to prove Lemma 6.6.

Proof of Lemma 6.6. Suppose G⋆ is a counterexample. Let u = uM , and let ∂T =
v0v1 . . . v2k−1v0. By Observation 4.6 and Lemma 4.8, for any v ∈ V (M ) \ {u}, the set P M
u,v
contains at least k − degT ∗(u) − 1 ≥ max{k − m + 1, k − 3} admissible paths. Let A and B be
the partite sets of G. By Lemma 6.15, we may assume that R ∪ V (N ) ⊆ A. We distinguish
cases based on the order of T .
We begin with the case m ≤ 4. Since k ≥ 7, we have m ≤ k − 3. It follows from Lemma 6.15
that |R ∪ V (N )| ≤ 1. Since δ2(G) ≥ k − 1 ≥ m + 2, it follows that all but at most one vertex in T
has a neighbor in M . Consequently, there exists a vertex v ∈ V (M ) \ {u} such that u and v are
adjacent to consecutive vertices on ∂T . In this scenario, P M
u,v contains max{k − m + 1, k − 3} =
k − m + 1 admissible paths. By Proposition 3.5, P T
u,v contains m admissible paths. Combining
these path families yields (k − m + 1) + m − 1 = k admissible cycles, a contradiction.
Next, assume that 5 ≤ m ≤ k − 1. Fix an arbitrary neighbor vi ∈ NT (u). We claim that
there exists a vertex v ∈ V (M ) \ {u} adjacent to some vj ∈ V (T ) such that dist∂T (vi, vj) ≤ 2.
To see this, first assume G⋆ is of Type I. Since δ2(G) ≥ k ≥ m + 1 and R ∪ V (N ) ⊆ A, all
vertices in V (T ) ∩ A, except possibly θ, have neighbors in M . If u ∈ A, then {vi−1, vi+1} ⊆ A.

26

Thus, at least one of them must have a neighbor v ∈ V (M ) \ {u}, proving the claim. If u ∈ B,
consider {vi−2, vi+2} ⊆ A. If θ /∈ {vi−2, vi+2}, then both vertices have neighbors in M . Since
degT (u) ≤ 2, at least one of them connects to a vertex v ∈ V (M )\{u}, which suffices. Otherwise,
assume without loss of generality that vi−2 = θ. Then vi+2 must have a neighbor in M . If this
neighbor is distinct from u, then the claim follows. Thus, we may assume that vi+2 is adjacent
to u. Repeating the argument for vi+2, we observe that vi+4 ̸= θ (since m ≥ 5). Consequently,
vi+4 must have a neighbor v ∈ V (M ) \ {u}, as desired. Now assume G⋆ is of Type II. By
Lemma 6.15 (2), R = V (N ) = ∅. Since δ3(G) = k ≥ m + 1, at most two vertices in T have
no neighbors in M . If either vi−1 or vi+1 has a neighbor in M , the claim follows immediately.
Otherwise, vi−1 and vi+1 are the only two vertices in T with no neighbors in M . Consequently,
both vi−2 and vi+2 must have neighbors in M . Since degT (u) ≤ 2, u cannot be adjacent to both
vi−2 and vi+2. Thus, one of them has a neighbor in V (M ) \ {u}, proving the claim.
With such a choice of v, P M
u,v contains k − 3 admissible paths. By Proposition 3.5, P T
u,v
contains m − 1 admissible paths. Their union yields (k − 3) + (m − 1) − 1 ≥ k admissible cycles,
a contradiction.
Finally, assume that m = k ≥ 7. Let w be a vertex in V (M ) \ {u} such that u, w connect to
distinct vertices vi, vj ∈ V (T ), minimizing the distance dist∂T (vi, vj). Without loss of generality,
assume 0 ≤ i < j ≤ m, so that dist∂T (vi, vj) = j − i. By Observation 4.6 and Lemma 4.8, P M
u,w
contains at least max{k − m + 1, k − 3} = k − 3 admissible paths. If j − i ≤ 4, Proposition 3.5
implies that P T
u,w contains k − dist∂T (vi, vj) + 1 ≥ k − 3 admissible paths. The union of paths
in P M
u,w and P T
u,w would then yield (k − 3) + (k − 3) − 1 = 2k − 7 ≥ k admissible cycles, a
contradiction.
Thus, we may assume j − i ∈ [5, k]. By the minimality of j − i, each of vi+1, vi+2, vi+3, vi+4
has no neighbor in M . We claim that at least one of these vertices has degree k in T . Recall that
R∪V (N ) ⊆ A, which implies that any v ∈ {vi+1, vi+2, vi+3, vi+4}∩A satisfies degT (v) = degG(v).
Suppose the claim is false. Then both vertices in {vi+1, . . . , vi+4} ∩ A must have degree less than
k in G, which forces G⋆ to be of Type II, and {vi+1, . . . , vi+4} ∩ A = {θ1, θ2}. It follows from
Lemma 6.15 that R = V (N ) = ∅, so the vertices in {vi+1, . . . , vi+4} ∩ B have degree k in T .
This contradiction proves the claim.
According to the claim, assume that degT (vi+ℓ) = k for some ℓ ∈ [4]. Consider (vi, vj)-paths
of the form vivi−1 . . . vαvi+ℓvβvβ+1 . . . vj, where indices satisfy α ∈ [j + 1, i] and β ∈ [i + ℓ + 1, j],
with α and β having different parity from i + ℓ. A routine verification confirms that the lengths
of these paths cover all integers of the appropriate parity in [3, 2k − 4]. In particular, P T
u,w
contains k − 3 admissible paths. Combining these with P M
u,w, we obtain (k − 3) + (k − 3) − 1 ≥ k
admissible cycles in G. This contradiction completes the proof.

6.3 The completion

We now complete the proofs of Theorems 6.1 and 6.2; combined with Theorem 5.1, the latter
yields Theorem 4.2.

Proof of Theorem 6.2. The theorem follows directly from Lemma 6.3, which handles the C4-
free case, and Lemmas 6.4, 6.5, and 6.6, which exhaust all possibilities for the optimal tetragonal
subgraph T . This concludes the proof of Theorem 4.2 for the bipartite case.

Proof of Theorem 6.1. For k ≥ 7, the conclusion follows immediately from Theorem 6.2, as
a collection of k admissible cycles in a bipartite graph covers all even residues modulo k. Now
assume that k = 6. By Theorem 2.4, G contains δ3(G) − 1 ≥ k − 1 = 5 admissible cycles, which
cover all even residues modulo 6. This completes the proof.

Finally, we present the proof of Theorem 1.4, which parallels the proof of Theorem 1.2.

Proof of Theorem 1.4. Let k ≥ 7. We claim that every 2-connected graph G with δ2(G) ≥ k
contains k admissible cycles, unless G is isomorphic to a graph in {Kk+1, Kk,k}∪Hk. By applying
this claim to each end-block of the graph, we obtain Theorem 1.4.

27

To prove the claim, we first note that Corollary 5.7 and Theorem 6.2 guarantee the existence
of k admissible cycles in every k-weak graph not isomorphic to a graph in {Kk+1, Kk,k}∪Hk. We
then proceed via a reduction argument analogous to Section 4.1. Suppose G does not contain k
admissible cycles. Then G cannot be k-weak (of Type I) and thus admits a 2-cut S = {x, y}.
If G − S contains two components of order at least two, then Lemma 2.3 yields (k − 1) +
(k − 1) − 1 > k admissible cycles, which suffices. Otherwise, a component of G − S consists
of a single vertex z. Hence, we may assume that xy /∈ E(G), as otherwise Lemma 2.3 yields
(k − 1) + 2 − 1 = k admissible cycles. Since δ2(G) ≥ k, z is the unique vertex with degree less
than k in G. Hence, S is the unique 2-cut of G, and G is a k-weak graph (of Type II), implying
the existence of admissible cycles. This proves the claim.

Acknowledgments

This work is supported by National Key Research and Development Program of China
2023YFA1010201, National Natural Science Foundation of China grant 12125106, and Inno-
vation Program for Quantum Science and Technology 2021ZD0302902.

References

[1] Noga Alon and Nathan Linial. Cycles of length 0 modulo k in directed graphs. Journal of
Combinatorial Theory, Series B, 47(1):114–119, 1989.

[2] Yandong Bai, Andrzej Grzesik, Binlong Li, and Magdalena Prorok. Cycle lengths in graphs
of given minimum degree. arXiv preprint arXiv:2511.03085, 2025.

[3] Yandong Bai, Binlong Li, Yufeng Pan, and Shenggui Zhang. On graphs without cycles of
length 1 modulo 3. arXiv preprint arXiv:2503.03504, 2025.

[4] B´ela Bollob´as. Cycles modulo k. Bulletin of the London Mathematical Society, 9(1):97–98,
1977.

[5] John Adrian Bondy. Pancyclic graphs i. J. Combin. Theory Ser. B, 11(1):80–84, 1971.

[6] John Adrian Bondy. Basic graph theory: paths and circuits. In Handbook of combinatorics
(vol. 1), pages 3–110. 1996.

[7] Guantao Chen and Akira Saito. Graphs with a cycle of length divisible by three. Journal
of Combinatorial Theory, Series B, 60(2):277–292, 1994.

[8] Shuya Chiba, Katsuhiro Ota, and Tomoki Yamashita. Minimum degree conditions for the
existence of a sequence of cycles whose lengths differ by one or two. Journal of Graph
Theory, 103(2):340–358, 2023.

[9] Nathaniel Dean. Which graphs are pancyclic modulo k? In Sixth International Conference
on the Theory and Applications of Graphs, pages 315–326, Kalamazoo, Michigan, USA,
1988.

[10] Nathaniel Dean, Atsushi Kaneko, Katsuhiro Ota, and Bjarne Toft. Cycles modulo 3. Tech-
nical Report 91-32, DIMACS, 1991.

[11] Nathaniel Dean, Linda Lesniak, and Akira Saito. Cycles of length 0 modulo 4 in graphs.
Discrete mathematics, 121(1-3):37–49, 1993.

[12] Reinhard Diestel. Graph theory. Springer (print edition); Reinhard Diestel (eBooks), 2024.

[13] Ajit A Diwan. Cycles of weight divisible by k. arXiv preprint arXiv:2407.01198, 2024.

28

[14] Paul Erd˝os. Some recent problems and results in graph theory, combinatorics, and number
theory. In Proc. Seventh S-E Conf. Combinatorics, Graph Theory and Computing, pages
3–14, Winnipeg, 1976. Utilitas Math.

[15] Genghua Fan. Distribution of cycle lengths in graphs. Journal of Combinatorial Theory,
Series B, 84(2):187–202, 2002.

[16] Jun Gao, Qingyi Huo, Chun-Hung Liu, and Jie Ma. A unified proof of conjectures on cycle
lengths in graphs. International Mathematics Research Notices, 2022(10):7615–7653, 2022.

[17] Jun Gao, Qingyi Huo, and Jie Ma. A strengthening on odd cycles in graphs of given
chromatic number. SIAM Journal on Discrete Mathematics, 35(4):2317–2327, 2021.

[18] Jun Gao, Binlong Li, Jie Ma, and Tianying Xie. On two cycles of consecutive even lengths.
Journal of Graph Theory, 106(2):225–238, 2024.

[19] Ervin Gy˝ori, Binlong Li, Nika Salia, Casey Tompkins, Kitti Varga, and Meiqiao Zhu. On
graphs without cycles of length 0 modulo 4. Journal of Combinatorial Theory, Series B,
176:7–29, 2026.

[20] Chengli Li and Xingzhi Zhan. Cycles of consecutive lengths in 3-connected graphs. arXiv
preprint arXiv:2508.14915, 2025.

[21] Hao Lin, Guanghui Wang, and Wenling Zhou. A strengthening on consecutive odd cycles
in graphs of given minimum degree. Journal of Graph Theory, 110(4):431–436, 2025.

[22] Chun-Hung Liu and Jie Ma. Cycle lengths and minimum degree of graphs. Journal of
Combinatorial Theory, Series B, 128:66–95, 2018.

[23] Benny Sudakov and Jacques Verstra¨ete. The extremal function for cycles of length ℓ mod
k. The Electronic Journal of Combinatorics, 24(1):P1.7, 2017.

[24] Carsten Thomassen. Graph decomposition with applications to subdivisions and path
systems modulo k. Journal of Graph Theory, 7(2):261–271, 1983.

[25] Carsten Thomassen. On the presence of disjoint subgraphs of a specified type. Journal of
Graph Theory, 12(1):101–111, 1988.

[26] Carsten Thomassen. The even cycle problem for directed graphs. Journal of the American
Mathematical Society, 5(2):217–229, 1992.

[27] Jacques Verstra¨ete. Extremal problems for cycles in graphs. In Recent trends in combina-
torics, pages 83–116. Springer, 2016.

Email address: lyf619311271@mail.ustc.edu.cn

Email address: jiema@ustc.edu.cn

Email address: zyzhao2024@mail.ustc.edu.cn

29
