<!-- source: https://arxiv.org/pdf/1904.05076v2 | converted from PDF -->

ADVANCES IN COMBINATORICS, 2021:3, 36 pp.
www.advancesincombinatorics.com

Cycle Lengths Modulo k in Large
3-connected Cubic Graphs

Kasper Szabo Lyngsie Martin Merker*

Received 11 April 2019; Revised 5 June 2020; Published 3 February 2021

Abstract: We prove that for all natural numbers m and k where k is odd, there exists
a natural number N(k) such that any 3-connected cubic graph with at least N(k) vertices
contains a cycle of length m modulo k. We also construct a family of graphs showing that
this is not true for 2-connected cubic graphs if m and k are divisible by 3 and k ≥ 12.

1 Introduction

1.1 Cycle lengths modulo k

Let G be a graph and let A be a set of natural numbers. Which properties of G and A guarantee the
existence of a cycle in G whose length is in A? Erd˝os asked many years ago whether there exists a set
A ⊂ N of density zero and two constants cA, nA such that every graph with at least nA vertices and average
degree at least cA contains a cycle whose length is in A, see [5]. Verstraëte [22] answered this question in
the afﬁrmative by showing that any graph with average degree at least 10 contains a cycle whose length is
in a prescribed set A ⊂ N satisfying |A ∩ {1, . . . , n}| = O(n0.99).
Of particular interest in the literature is the case where A is a residue class modulo some natural
number k. There are many results concerning sufﬁcient conditions for the existence of a cycle of length m
modulo k where m ∈ {0, 1, 2} and k ∈ {3, 4}, see for example [6, 4, 14, 15]. In 1976, Erd˝os and Burr [8]
conjectured that for all natural numbers m and k where k is odd, there exists a constant ck(m) such that
every graph with average degree at least ck(m) has a cycle of length m modulo k. Note that the restriction
to odd natural numbers k is necessary since bipartite graphs contain no cycles of odd length. Bollobás [1]

*Supported by the Danish Council for Independent Research, Natural Sciences, grant DFF-8021-00249, AlgoGraph.

© 2021 Kasper Szabo Lyngsie and Martin Merker
cb Licensed under a Creative Commons Attribution License (CC-BY) DOI: 10.19086/aic.18971arXiv:1904.05076v2  [math.CO]  30 Jan 2021
KASPER SZABO LYNGSIE AND MARTIN MERKER

showed that ck(m) = 2
k ((k + 1)k − 1) sufﬁces, proving the conjecture by Erd˝os and Burr. Sudakov and
Verstraëte [17] showed that ck(m) = O(mk 2
m ).
In 1983, Thomassen [19] conjectured that for all natural numbers m and k, every graph of minimum
degree at least k + 1 contains a cycle of length 2m modulo k. Thomassen showed that minimum degree
4m(k + 1) sufﬁces. Cai and Shreve [3] showed that claw-free graphs of minimum degree k + 1 have
cycles of all lengths modulo k. Diwan [7] proved that graphs of minimum degree 2k − 1 have cycles of
all even lengths modulo k and that Thomassen’s conjecture holds for m = 2. The currently best known
result is by Liu and Ma [12] who veriﬁed Thomassen’s conjecture if k is even and showed that minimum
degree k + 4 sufﬁces if k is odd.
A commonly used method to show that a graph has cycles of every even length modulo k is to
construct a sequence of cycles whose lengths form an arithmetic progression with difference 2. Bondy
and Vince [2] answered a question of Erd˝os by showing that a graph with minimum degree 3 contains
two cycles whose lengths differ by 1 or 2. Fan [10] showed that graphs of minimum degree 3k − 2
contain k cycles whose lengths form an arithmetic progression with difference 2. A similar result was
proved by Verstraëte [21] who showed that graphs of average degree 8k and even girth g contain ( g
2 − 1)k
cycles of consecutive even lengths. Sudakov and Verstraëte [16] showed that a graph with average degree
d and girth g has Ω(d⌊ g−1
2 ⌋) cycles of consecutive even lengths, proving a conjecture by Erd˝os about
the minimum number of distinct cycle lengths. Ma [13] proved an analogous result about cycles with
consecutive odd lengths in non-bipartite 2-connected graphs. Liu and Ma [12] showed that every graph
with minimum degree k + 1 contains ⌊ k
2 ⌋ cycles of consecutive even lengths.
Most sufﬁcient conditions for the existence of cycles of length m modulo k require a minimum
degree which grows linearly in k. The reason for that is that graphs where every block is a clique on
at most k + 1 vertices contain no cycles of length 2 modulo k. In this paper we focus on cycles in
cubic graphs. Thomassen [18] proved that a graph with minimum degree at least 3 and girth at least
2(k2 + 1)(3 · 2k2+1 + (k2 + 1)2 − 1) contains cycles of all even lengths modulo k, which is the strongest
known result for the class of cubic graphs. We prove a similar statement for cubic graphs under the mild
assumption that the graph is sufﬁciently large and 3-connected.

Theorem 1.1. For every odd natural number k, there exists a natural number N(k) such that every
3-connected cubic graph with at least N(k) vertices contains a cycle of length m modulo k for every
natural number m.

Theorem 1.1 does not hold if k is even since bipartite graphs have no cycles of odd length. If k is even
and not divisible by 4, then our proofs imply that the set of cycle lengths of every sufﬁciently large cubic
3-connected graph contains all odd residues or all even residues modulo k. It looks plausible that it will
always contain all even residues, but our methods are not sufﬁcient to prove it. Similarly, if k is divisible
by 4, then we can show that the set of cycle lengths will contain at least a quarter of all residues modulo k.
To be more precise, for some i ∈ {0, 1, 2, 3}, it will contain all residues that are congruent to i modulo 4.
Theorem 1.1 is not true for 3-connected graphs of minimum degree d where d ≥ 3 and d < k
2 . To see
this, note that for n ≥ d the complete bipartite graph Kd,n is 3-connected and contains no cycle of length
divisible by k. However, it might be true for d-regular graphs. The methods in this paper have been
tailored to cubic graphs, but the general ideas extend to regular graphs. In particular, we believe that the
structures we ﬁnd in large cubic graphs also exist in large d-regular graphs. An extension of the proof to

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 2

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

d-regular graphs might be possible but there appear to be various technical obstacles.
We also show that the connectivity condition in Theorem 1.1 cannot be lowered to 2-connectivity in
general. Given natural numbers m, k, and N such that k ≥ 12 and m and k are divisible by 3, we construct
a 2-connected cubic graph on at least N vertices which has no cycles of length m modulo k.

1.2 Proof overview and structure of the paper

In the proof of Theorem 1.1, we show that in large 3-connected cubic graphs there exists a subgraph of a
certain structure which has cycles of every length modulo k. The structure we use is necklace-like: it
consists of a collection of 2-connected subgraphs which are joined by paths in a cyclic order. The general
idea is that in such a structure we can take a cycle and modify it locally inside one of the 2-connected
subgraphs to obtain a new cycle which ideally has a different length modulo k. If there are sufﬁciently
many 2-connected subgraphs, then we have enough freedom to ﬁnd all cycle lengths modulo k. Of course
we need additional assumptions to ensure that there is a local modiﬁcation which changes the length
modulo k. We distinguish two types of such necklaces which are deﬁned in Section 2.
The ﬁrst type of necklace is a so-called θ -necklace. In this case there are several 2-connected
subgraphs, each consisting of a cycle and a path of a given length which attaches to the cycle. In this
case we cannot bound the difference of the cycle lengths if we change the cycle locally. However, if the
length of the path is a power of 2, then we can obtain all residues modulo k for odd k by combining local
modiﬁcations. We usually show the existence of a θ -necklace by ﬁnding a path and a cycle which are
joined by many disjoint paths of the same length. We call such a cycle and path close since we are mainly
interested in the case where the paths have length at most 2. To ﬁnd a cycle and a path which are close,
we can pick a cycle C in G and then try to ﬁnd a path which contains many neighbours of C, or vertices at
distance 2. In Section 3 we show that we can ﬁnd such a path provided G −C has a block containing
sufﬁciently many neighbours of C.
In the second type of necklace we require many 2-connected parts where we can change the length
of the cycle by 1 or 2. We call such a necklace wiggly. In wiggly necklaces we can ﬁnd a sequence of
cycles such that their lengths form an arithmetic progression with difference 1 or 2. For our purposes
it is only important that the differences are a power of 2 to make sure that we can obtain all residues
modulo k for odd k. To show the existence of wiggly necklaces, we need two paths between two given
vertices x and y whose lengths differ by 1 or 2. A result by Fan [10] implies that such paths exist in a
subcubic 2-connected graph if x and y are the only vertices of degree 2. However, in the main proof we
need to ﬁnd these paths when there is also a third vertex of degree 2 (and in some cases even a fourth
such vertex). Thus, we need to prove extensions of Fan’s results in the case of subcubic graphs, which we
do in Section 4.
Section 5 contains the main part of the proof of Theorem 1.1. We start by choosing a subgraph Θ in G
which consists of three internally disjoint paths between two vertices. There are several cases depending
on the number of 2-connected endblocks in G − Θ and how these endblocks attach to Θ. If there are
many 2-connected endblocks which have many neighbours on Θ, then we ﬁnd a θ -necklace. If there are
many 2-connected endblocks with only few neighbours on Θ, then we ﬁnd a wiggly necklace. Finally,
if there are only few 2-connected endblocks, then we also ﬁnd a θ -necklace. For technical reasons the
case distinction in Section 5 is slightly different. We distinguish between Θ-isolated endblocks which are
endblocks with neighbours on only one of the three paths in Θ and Θ-connecting endblocks which have

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 3

KASPER SZABO LYNGSIE AND MARTIN MERKER

neighbours on at least two different paths.
In Section 6, we show that Theorem 1.1 does not hold in general for 2-connected cubic graphs. For
k ≥ 12 and k divisible by 3, we construct an inﬁnite family of 2-connected graphs which do not contain
cycles of every length modulo k.

1.3 Notation and preliminaries

All graphs in this paper are simple and ﬁnite unless stated otherwise. We denote the vertex set and
edge set of a graph G by V (G) and E(G), respectively. If H is a subgraph of G or H ⊆ V (G), we write
G − H or G −V (H) to denote the graph obtained from G by removing all vertices in H. We write G[A]
to denote the subgraph of G induced by the vertices in A. If v ∈ V (G) and e ∈ E(G), then G − v and
G − e are the graphs obtained from G by removing v and e, respectively. We write d(v) and N(v) for the
degree and the neighbourhood of v, respectively. If H is a subgraph of G, then NH(u) = N(u) ∩V (H) and
dH(u) = |NH(u)|. If A ⊆ V (G) or A is a subgraph of a graph G, then N(A) denotes the set of vertices in
G − A which have a neighbour in A. If B ⊆ V (G) or B is a subgraph of G, then NB(A) denotes the set of
vertices in B which have a neighbour in A and E(A, B) denotes the set of edges having an end in both A
and B. If H is a subgraph of a graph G and x, y ∈ V (H), then H + xy is the graph obtained from H by
adding the edge xy. A path from a vertex u to a vertex v is called a u − v path and, more generally, if A
and B are vertex sets or subgraphs of a graph G, then an A − B path is a path having one end in A, one
end in B, and no internal vertices in A ∪ B. If x and y are vertices on a path P, then xPy denotes the x − y
subpath of P. If G is connected and u, v ∈ V (G), then we write dist(u, v) for the length of a shortest u − v
path in G.
A block in a graph G is a maximal connected subgraph of G without any cut-vertices. Note that a
block of a graph G is either a maximal 2-connected subgraph of G, a bridge in G or an isolated vertex. The
block graph B(G) of a graph G is the bipartite graph whose vertex set consists of the cut-vertices and the
blocks in G, and whose edges are of the form vB where v is a cut-vertex in G and B is a block containing
v. If G is connected, then B(G) is a tree. A block in G corresponding to a vertex of degree at most 1 in
B(G) is called an endblock. We call a 2-edge-cut non-trivial if it separates G into two components each
containing at least two vertices.
The following lemma is well-known.

Lemma 1.2. Let G be a connected graph and let S ⊂ V (G). If |S| is even, then there exist |S|
2 pairwise
edge-disjoint paths with endvertices in S such that each vertex of S is an endvertex of exactly one of the
paths.

Proof. We may assume that G is a tree. Let P be a collection of |S|
2 paths such that each vertex of S is
an endvertex of precisely one of them, and such that sum of the lengths of the paths in P is minimal. It
follows easily that the paths in P are edge-disjoint.

We will apply Lemma 1.2 where G is a subcubic graph. Note that in this case any two edge-disjoint
paths are also internally vertex-disjoint.
The following classical result by Erd˝os and Szekeres is used several times throughout the paper.

Theorem 1.3 (Erd˝os, Szekeres [9]). Every sequence of at least (r − 1)(s − 1) + 1 distinct elements of an
ordered set contain an increasing subsequence of length r or a decreasing subsequence of length s.

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 4

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

A cycle C in a graph G is called non-separating if G −V (C) is connected. In Section 4 the existence of
non-separating cycles plays an important role. We use the following theorem by Tutte on non-separating
cycles in 3-connected graphs.

Theorem 1.4 (Tutte [20]). Let G be a graph, st ∈ E(G), and r ∈ V (G) \ {s,t}. If G is 3-connected, then
G contains a non-separating induced cycle C such that st ∈ E(C) and r /∈ V (C).

2 Necklaces

In this section we deﬁne two types of necklaces: θ -necklaces and wiggly necklaces. We prove sufﬁcient
conditions for the existence of cycles of every length modulo k in these necklaces. We begin by deﬁning
θ -graphs, which are the building blocks of θ -necklaces.

Deﬁnition 2.1 (θ -graph). A θ -graph Θ consists of two vertices u and v and three u − v paths P1, P2, and
P3 which are pairwise internally disjoint. We call P1, P2, and P3 the legs of Θ and write Θ = (P1, P2, P3).
We also call Θ a u, v-θ -graph.

Note that if x and y are vertices on different legs of a θ -graph Θ, then Θ contains four x − y paths.
Under the mild assumption that the length of the third path has no common divisors with k, this guarantees
the existence of x −y paths with different lengths modulo k. A θ (k, i)-necklace consists of k such θ -graphs
where the third path has length i and which are connected by paths in a cyclic order.

Deﬁnition 2.2 (θ (k, i)-necklace). Let k and i be natural numbers. A θ (k, i)-necklace is a connected
subcubic graph consisting of k disjoint θ -graphs Θ1,. . . ,Θk and k disjoint paths P1, . . . ,Pk such that

• Θ j has legs L j,1, L j,2, L j,3 where L j,3 is a path of length i for j ∈ {1, . . . , k},

• Pj is an L j,2 − L j+1,1 path for j ∈ {1, . . . , k − 1}, Pk is an Lk,2 − L1,1 path, and

• for every j, j′ ∈ {1, . . . , k}, no interior vertex of Pj is contained in Θ j′.

See Figure 1(a) for an example of a θ (4, 2)-necklace. A graph is a θ -necklace if it is a θ (k, i)-necklace
for some natural numbers k and i. The following lemma gives a sufﬁcient condition for a θ -necklace
to contain cycles of every length modulo k. In the main proof we will only construct θ (k, i)-necklaces
where i ∈ {1, 2}.

Lemma 2.3. Let m, k, and i be natural numbers and let G be a θ (3k4, i)-necklace. If gcd(k, 2i) = 1, then
G has a cycle of length m modulo k.

Proof. Let Θ j, L j,1, L j,2, L j,3, and Pj (for j ∈ {1, . . . , 3k4}) be as in Deﬁnition 2.2. For j ∈ {1, . . . , 3k4},
let u j, v j denote the vertices in L j,1 ∩L j,2 ∩L j,3 and let w j,1 ∈ V (L j,1) and w j,2 ∈ V (L j,2) denote the ends of
Pj−1 and Pj, respectively. Let a j, b j, c j, d j be integers such that |E(w j,1L j,1u j)| = a j, |E(u jL j,2w j,2)| = b j,
|E(w j,1L j,1v j)| = c j − i, and |E(v jL j,2w j,2)| = d j − i. Note that Θ j contains four w j,1 − w j,2 paths whose
lengths are a j + b j, a j + d j, c j + b j, and c j + d j − 2i.
Let C be the cycle in G obtained by taking the union of all the paths Pj, w j,1L j,1u j, and u jL j,2w j,2 for
j ∈ {1, . . . , 3k4}. We can modify C by replacing the path within Θ j by a different w j,1 − w j,2 path, which

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 5

KASPER SZABO LYNGSIE AND MARTIN MERKER

(a) A θ (4, 2)-necklace (b) A 4-wiggly necklace

Figure 1: Two types of necklaces

increases the length of C by d j − b j, c j − a j, or c j + d j − 2i − a j − b j. By the pigeonhole principle there
are at least 3k indices j for which the 3-tuples (d j − b j, c j − a j, c j + d j − 2i − a j − b j) are equal modulo k.
Thus, there exists a subset I ⊂ {1, . . . , 3k4} with |I| ≥ 3k and integers a, b, c, d, such that for j ∈ I we have

d j − b j ≡ d − b mod k

c j − a j ≡ c − a mod k

c j + d j − 2i − a j − b j ≡ c + d − 2i − a − b mod k

By possibly modifying the cycle C inside each Θ j for j ∈ I we can obtain all cycle lengths of the form
|E(C)| + λ1(d − b) + λ2(c − a) + λ3(c + d − 2i − a − b) mod k where λ1, λ2, λ3 are non-negative integers
with λ1 + λ2 + λ3 ≤ 3k. For every integer λ , we can obtain all cycle lengths of the form |E(C)| + 2iλ
mod k by choosing λ1, λ2, λ3 ∈ {0, . . . , k − 1} such that λ1 ≡ λ2 ≡ λ ≡ −λ3 mod k. Since gcd(k, 2i) = 1
this implies that G contains cycles of length m modulo k for every integer m.

If k is even, then the proof above still shows that for a θ (3k4, i)-necklace Θ, there is a natural number
c such that for every integer λ there is a cycle of length c + 2iλ modulo k in Θ. However, now this set
will not cover all residues. If i = 1 then the set will contain either all even or all odd residues modulo k.
This is also the case if i = 2 and k is not divisible by 4. If i = 2 and k is divisible by 4, then the set will
contain only those residues that are in the same residue class modulo 4 as c.
As can be seen below, one way to ﬁnd a θ (k, 1)-necklace or a θ (k, 2)-necklace inside a cubic graph G is
to ﬁnd a cycle and a path which are disjoint and have many disjoint paths of length at most 2 connecting
them. This motivates the following deﬁnition.

Deﬁnition 2.4 (k-close). Two subgraphs H1 and H2 of a graph G are k-close if H1 and H2 are disjoint
and there exist k pairwise disjoint H1 − H2 paths of length at most 2.

Sometimes we will slightly abuse this notation by saying that P1 is k-close to P2 ∪ P3 where P1, P2,
and P3 are the legs of a θ -graph. Note that in this case the subpath induced by the interior vertices of P1 is
k-close to P2 ∪ P3.
 ADVANCES IN COMBINATORICS, 2021:3, 36pp. 6

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

Lemma 2.5. If a graph contains a cycle and a path which are 18k2-close, then it contains a θ (k, 1)-
necklace or a θ (k, 2)-necklace.

Proof. Let G be a graph containing a path P = p1 p2 . . . pn and a cycle C = c1c2 . . . cmc1 which are 18k2-
close. Let C′ = C − cmc1. Either |E(P,C)| ≥ 9k2 or P and C are joined by at least 9k2 disjoint paths of
length 2. Suppose |E(P,C)| ≥ 9k2. Deﬁne a total ordering of V (P) by pi ≤ p j if and only if i ≤ j and a
total ordering of V (C) by ci ≤ c j if and only if i ≤ j. Given an edge e between P and C let p(e) denote the
end of e on P and let c(e) denote the end of e on C. Let e1, . . . , e9k2 be distinct edges between P and C such
that p(ei) ≤ p(e j) whenever i ≤ j. Let S = (c(e1), c(e2), . . . , c(e9k2)). Note that 9k2 ≥ (3k − 1)2 + 1 so by
Theorem 1.3 S has a subsequence S′ = (c(e′
1), . . . , c(e′
3k)) of length 3k which is increasing or decreasing.
For each i ∈ {1, . . . , k}, let Ci be the cycle obtained from the union of the paths p(e′
3i−2)Pp(e′
3i) and
c(e′
3i−2)C′c(e′
3i) together with the edges e′
3i−2 and e′
3i Note that each Ci has a chord e′
3i−1. Now the union
of the θ -graphs Ci + e′
3i−1 and the cycle C forms a θ (k, 1)-necklace.
If P and C are joined by at least 9k2 disjoint paths of length 2 the proof is analogous. The only difference
is that the chords of the cycles Ci are now subdivided once. Thus, we obtain a θ (k, 2)-necklace in this
case.

The following deﬁnition is similar to that of a θ -necklace but allows more general building blocks.

Deﬁnition 2.6 (B-necklace, k-wiggly necklace). Let k and ℓ be natural numbers. Let B = {B1, . . . , Bℓ}
be a collection of 2-connected pairwise disjoint subgraphs of a graph G. A B-necklace N is a subgraph
of G consisting of B1,. . . ,Bℓ and ℓ pairwise disjoint paths P1, . . . ,Pℓ such that

• Pi is a Bi − Bi+1 path for i ∈ {1, . . . , ℓ − 1}, Pℓ is a Bℓ − B1 path, and

• for every i, j ∈ {1, . . . , ℓ}, no interior vertex of Pi is contained in B j.

For i ∈ {1, . . . , ℓ}, let xi, yi denote the two vertices of Bi which are contained in some path Pj. We say N is
k-wiggly if there exists I ⊆ {1, . . . , ℓ} with |I| = k such that Bi contains two xi − yi paths whose lengths
differ by 1 or 2 for every i ∈ I.

Note that the two paths inside each Bi are not necessarily disjoint. For example, B2 in the 4-wiggly
necklace in Figure 1(b) contains x2 − y2 paths of lengths 2, 4, and 5, but no two disjoint x2 − y2 paths
whose lengths differ by 1 or 2.
In a k-wiggly necklace there exists a cycle which we can modify locally in k places so that each time its
length increases by 1 or 2. We use this to show that 2k-wiggly necklaces contain cycles of every length
modulo k.

Lemma 2.7. Let k and m be natural numbers with k odd. If a necklace is 2k-wiggly, then it has a cycle of
length m modulo k.

Proof. Let G be a 2k-wiggly necklace with 2-connected subgraphs B0, . . . , B2k−1 and paths P0, . . . , P2k−1
as in Deﬁnition 2.6. For each j ∈ {0, . . . , 2k − 1}, let Pj,1, Pj,2 be two Pj−1 − Pj paths in B j such that
|E(Pj,2)| − |E(Pj,1)| ∈ {1, 2}. Let C be the cycle consisting of the union of all paths Pj and Pj,1 for
j ∈ {0, . . . , 2k − 1}. For each B j, we can modify C by replacing the path Pj,1 by Pj,2 which increases
the length of the cycle by x j with x j ∈ {1, 2}. There are at least k indices j for which the values x j are
the same. Thus we can obtain cycles of all lengths in {|E(C)|, |E(C)| + x, . . . , |E(C)| + kx} for some
x ∈ {1, 2}. Since gcd(k, x) = 1, this set contains all residues modulo k.

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 7

KASPER SZABO LYNGSIE AND MARTIN MERKER

If k is even and x = 2, then the set {|E(C)|, |E(C)| + x, . . . , |E(C)| + kx} at the end of the proof
contains either all even or all odd residues modulo k. Thus, if k is even we can only guarantee that at least
half of all possible residues modulo k occur in a 2k-wiggly necklace.
To simplify the calculations in the main proof we introduce the following deﬁnition.

Deﬁnition 2.8 (k-good). A graph G is called k-good if it contains at least one of the following graphs as
a subgraph:

• a θ (k, i)-necklace with i ∈ {1, 2},

• a k-wiggly necklace, or

• a path and a cycle which are k-close.

Note if a graph is k-good for some natural number k, then it is also k′-good for every natural number
k′ with k′ ≤ k. It follows from Lemma 2.3, Lemma 2.5, and Lemma 2.7 that for every odd natural number
k there exists a natural number f (k) such that every f (k)-good graph contains cycles of every length
modulo k.

Theorem 2.9. Let G be a graph and k, m natural numbers with k odd. If G is 162k8-good, then G
contains a cycle whose length is congruent to m modulo k.

Proof. By Lemma 2.7, we can assume that G contains a path and a cycle which are 162k8-close or a
θ (162k8, i)-necklace where i ∈ {1, 2}. Since 162k8 > 3k4, by Lemma 2.3, we can assume that G contains
a path and a cycle which are 162k8-close. By Lemma 2.5, the graph G contains a θ (3k4, i)-necklace
where i ∈ {1, 2}. Now G contains a cycle whose length is congruent to m modulo k by Lemma 2.3.

Thus, to prove Theorem 1.1 it sufﬁces to show that for any natural number k, every sufﬁciently large
3-connected cubic graph is k-good.

3 Paths containing given edges

In this section we investigate the following question: Given a set S of edges in a subcubic graph G, does
there exist a path in G containing k edges of S? We show that such a path exists if |S| is sufﬁciently large
and G is 2-connected. Note that 2-connectivity is a necessary constraint, since we cannot ﬁnd such a path
for k = 3 if G is a tree and S contains all edges incident with vertices of degree 1.
We apply this result in Section 5 to construct cycles and paths which are k-close: If C is a cycle such that
G −C has a block B containing many vertices which have distance at most 2 from C, then we can ﬁnd a
path P containing k of these vertices and P is k-close to C.
Before we prove the main theorem of this section, we prove the special case where G has a Hamiltonian
path and S consists of the edges which are not contained in the Hamiltonian path. Note that in this case
we allow multiple edges in G and we do not require G to be 2-connected.

Lemma 3.1. Let k be a natural number, G a subcubic multigraph with a Hamiltonian path H, and
M = E(G) \ E(H). If |M| ≥ 8
3 k(k − 1) + 1, then there exists a path P in G such that |E(P) ∩ M| ≥ k.

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 8

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

Proof. Let H = p1 . . . pn. We deﬁne a total ordering on V (G) by pi ≤ p j if and only if i ≤ j. We write
u < v for u, v ∈ V (G) if u ≤ v and u ̸= v. Let f (k) = ⌈ 8
3 k(k − 1) + 1⌉. We may assume |M| = f (k) and
M = {e1, . . . , e f (k)}. For i ∈ {1, . . . , f (k)}, let ℓi and ri denote the end points of ei such that ℓi < ri. By
possibly relabeling the edges in M, we may assume that ℓi < ℓ j whenever i < j. Now consider the
sequence S = (r1, r2, . . . , r f (k)). Since |S| ≥ (⌈ 8
3 k⌉ − 1)(k − 1) + 1, by Theorem 1.3 the sequence S has a
decreasing subsequence of length k or an increasing subsequence of length ⌈ 8
3 k⌉. If S has a decreasing
subsequence S> of length k, then it is easy to see that there exists a path containing the k edges of M
which are incident with a vertex in S>. Thus, we may assume that S contains an increasing subsequence
S< of length ⌈ 8
3 k⌉. Let M′ ⊂ M be the set of edges in M which are incident to a vertex in S<. We say two
edges e, f ∈ M′ are non-crossing if r(e) < ℓ( f ) or r( f ) < ℓ(e). For e ∈ M′, let

R(e) = {e′ ∈ M′ | r(e) < ℓ(e
′)} .

We deﬁne a set E′ = {e′
1, . . . , e′
m} of edges in the following way. Let e′
1 be the edge in M′ for which ℓ(e′
1)
is minimal. Suppose e′
i is deﬁned and R(e′
i) is non-empty, then we deﬁne e′
i+1 as the edge in R(e′
i) for
which ℓ(e′
i+1) is minimal. We continue like this until we reach an index m such that R(e′
m) = /0. Note
that the edges in E′ are pairwise non-crossing and there exists a path in G containing all edges in E′, see
Figure 2. Thus, we may assume m < k. For e ∈ E′ we deﬁne

C(e) = {e′ ∈ M′ | ℓ(e) ≤ ℓ(e
′) < r(e)} .

By construction of E′, the sets C(e′
1), . . . ,C(e′
m) form a partition of M′. For e ∈ E′, let H(e) denote the
shortest subpath of H containing the ends of all edges in C(e). For each i ∈ {1, . . . , m}, we now construct
a path Pi in H(e′
i) ∪ C(e′
i) containing at least 3
4 |C(e′
i)| of the edges in C(e′
i) and whose endvertices are
the endvertices of H(e′
i). Let C(e′
i) = { f1, . . . , ft} with ℓ( f1) < · · · < ℓ( ft). Note that f1 = e′
i. Since
C(e′
i) ⊆ M′, we have r( f1) < · · · < r( ft) and H(e′
i) = ℓ( f1)Hr( ft). If t = 1 or t = 2, deﬁne Pi = f1 or
Pi = f1 + r( f1)Hℓ( f2) + f2, respectively. If t ≥ 3 is odd, then deﬁne

Pi = f1 + r( f1)Hr( f2) + f2 + ℓ( f2)Hℓ( f3) + f3 + . . . + ft−1 + ℓ( ft−1)Hℓ( ft) + ft .

If t ≥ 4 is even, then we deﬁne

Pi = f1 + r( f1)Hr( f2) + f2 + ℓ( f2)Hℓ( f3) + f3 + . . . + ℓ( ft−2)Hℓ( ft−1) + ft−1 + r( ft−1)Hr( ft) .

In this case Pi contains all edges in C(e′
i) apart from ft, while in the other cases Pi contains all edges in
C(e′
i). This implies |E(Pi) ∩C(e′
i)| ≥ 3
4 |C(e′
i)|.
Note that if e ∈ C(e′
i), f ∈ C(e′
j), and i + 2 ≤ j, then e and f are not crossing. Thus, the paths Pi and Pj are
disjoint for i, j ∈ {1, . . . , m} with i + 2 ≤ j. Let Modd denote the union of all C(e′
i) where i ∈ {1, . . . , m}
is odd, and Meven = M′ \ Modd. One of Modd and Meven, say Modd, contains least 4
3 k edges. Let P be a
path which contains all the paths Pi with i odd as a subpath. Now P contains at least 3
4 |Modd| ≥ k edges
of M.

The lower bound for the size of M in Lemma 3.1 is best possible up to a constant factor. To see this,
let K be a natural number and let GK be the graph consisting of a Hamiltonian path and a matching M on
K2 edges as in Figure 3. It is easy to see that every path in GK contains at most 3K − 2 edges of M. Thus,
if there is a path containing at least k edges of M, then K > k
3 and |M| ≥ k2
9 .
We use Lemma 3.1 to prove a more general statement that holds for all subcubic 2-connected graphs.

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 9

KASPER SZABO LYNGSIE AND MARTIN MERKER

Figure 2: Proof of Lemma 3.1

Figure 3: A graph where |M| = K2 and |E(P) ∩ M| ≤ 3K − 2 for every path P.

Theorem 3.2. Let G be a 2-connected subcubic graph, S ⊆ E(G), and k a natural number. If |S| ≥ 24k2,
then there exists a path P in G such that |E(P) ∩ S| ≥ k.

Proof. Suppose the lemma is false and let (G, S, k) be a counterexample where |E(G)| is minimal. We
may assume k ≥ 3 since G is 2-connected. We call the edges in S special. If an edge e is not special and
not contained in a 2-edge-cut, then by minimality of G, there exists a path containing k special edges in
G − e, and thus also in G. Hence, we may assume that every edge which is not special is contained in a
2-edge-cut.
Suppose there exists a vertex v of degree 2 which is not incident with a special edge. Let G′ be the graph
we obtain from G by suppressing v. If G′ is simple, then G′ is a smaller counterexample. If G′ is not
simple, then G − v is 2-connected and G − v is a smaller counterexample. Thus we may assume that every
vertex of degree 2 is incident with at least one special edge.
Suppose {e, f } is a non-trivial 2-edge-cut and K1 and K2 are the two components of G−e− f . Suppose K1
does not contain a special edge. Then the graph G′ we obtain from G by contracting K1 into a single vertex
has fewer edges than G but the same number of special edges. Since G is a minimal counterexample, we
can ﬁnd a path containing k special edges in G′ and therefore also in G. Thus, we may assume that every
non-trivial 2-edge-cut separates the graph into two components which contain special edges.
Since |S| ≥ 24k2, the graph G has at least 2
3 · 24k2 vertices. Let v be any vertex in G. Since G is subcubic,
the distance class at distance m away from v contains at most 3 · 2m−1 vertices. Let dmax denote the
maximum distance from a vertex to v in G. We have

2
3 · 2
3k2 ≤ |V (G)| ≤ 1 + dmax
∑
i=1 3 · 2i−1 = 3
2 · 2dmax+1 − 2 .

Thus, we have 2dmax+1 ≥ 24k2−2 and dmax ≥ 4k2 − 3. Since G is 2-connected, this implies that G has a
cycle C of length at least 8k2 − 6. Let X be the set of vertices of C that have degree 3 in G. We may assume
that C contains at most k − 1 special edges. Since every vertex of degree 2 is incident with a special edge,
C contains at most 2(k − 1) vertices of degree 2. Thus, |X| ≥ 8k2 − 6 − 2(k − 1) = 8k2 − 2k − 4.
Let H = G − E(C). If K is a component of H, then either |V (K) ∩ X| ≥ 2 or K is an isolated vertex and
V (K) ∩ X = /0. By Lemma 1.2, we can choose in each component K a collection of disjoint paths pairing
up the vertices of V (K) ∩ X (apart from possibly one if |V (K) ∩ X| is odd). This deﬁnes a set of paths

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 10

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

P with |P| ≥ 1
3 |X| ≥ 1
3 (8k2 − 2k − 4). Let G′ be an auxiliary graph we obtain by taking the cycle C and
adding a chord between the ends of each path in P. In G′ the cycle C has |P| chords. Note that since
|P| ≥ 8
3 k(k − 1) + 1 for k ≥ 3, there is a path in G′ containing at least k chords of C by Lemma 3.1. This
corresponds to a path P in G which uses edges of C and at least k paths in P. Let P′ ⊆ P be the set of
paths contained in P, so |P′| ≥ k.
Let Q be a path in P′ which joins the vertices u and v of C, and let e be the edge of Q incident with u. If e
is not special, then there exists an edge f such that G − e − f is disconnected. Note that f ∈ E(Q). Let K
be the component of G − e − f not containing C. If K is an isolated vertex, then e or f is special. If K is
not an isolated vertex, then K contains a special edge s. Since Q contains e and f which separate K from
C, there is no other path in P′ which contains a vertex of K. Since G is 2-connected we can modify P in K
so that it contains s. That is, we replace Q by a path Q′ in H which joins u and v, contains s and is disjoint
from all paths in P′ \ {Q}. By repeating this modiﬁcation of P, we obtain a path in G that contains at
least one special edge for each path in P′. Since |P′| ≥ k, this path contains at least k special edges.

We do not believe that the lower bound for |S| in Theorem 3.2 is optimal. However, Lang and
Walther [11] constructed a family of 2-connected cubic graphs where the length of a longest path in G is
O(log2(|E(G)|)). By choosing S = E(G), this shows that the lower bound for |S| in Theorem 3.2 cannot
be smaller than Ω(2
√
k).
We conclude this section by proving a more specialized lemma which we use in Section 5.

Lemma 3.3. Let k be a natural number and G a subcubic graph which is the union of a θ -graph
Θ = (P1, P2, P3) and a matching M such that every edge in M has its endpoints on two different legs of Θ.
If |M| ≥ 3k2, then G has a cycle C such that |E(C) ∩ M| ≥ k.

Proof. For one pair of legs of Θ, say P1 and P2, we have |E(P1, P2)| ≥ k2. Let P1 = p1 p2 . . . pn and
P2 = q1q2 . . . qm with p1 = q1 and pn = qm. Deﬁne a total ordering of V (P1) by pi ≤ p j if and only if
i ≤ j and a total ordering of V (P2) by qi ≤ q j if and only if i ≤ j. Given an edge e between P1 and P2
let pi(e) denote the end of e on Pi for i ∈ {1, 2}. Let e1, . . . , ek2 ∈ M be distinct edges between P1 and P2
where p1(ei) ≤ p1(e j) whenever i ≤ j. By Theorem 1.3, the sequence S = (p2(e1), . . . , p2(ek2)) has a
subsequence S′ = (p2(e′
1), . . . , p2(e′
k)) of length k which is increasing or decreasing. In each case, there
is a cycle C in G containing all the edges e′
i for i ∈ {1, . . . , k}, see Figure 4.

4 Paths whose lengths differ by 1 or 2

Let G be a 2-connected subcubic graph and x, y ∈ V (G). A result by Fan [10] implies that if d(v) = 3 for
every v ∈ V (G) \ {x, y}, then there exist two x − y paths whose lengths differ by 1 or 2. In this section we
extend this result to the case where V (G) \ {x, y} contains one or two vertices of degree 2. This will allow
us in Section 5 to use non-trivial 3-edge-cuts for the construction of k-wiggly necklaces.

Deﬁnition 4.1 ( fC(x, y)). Let C be a cycle in a graph and let x, y be two distinct vertices of C. We deﬁne
fC(x, y) as the absolute difference of the lengths of the two x − y paths on C.

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 11

KASPER SZABO LYNGSIE AND MARTIN MERKER

(a) S′ is decreasing and k odd (b) S′ is decreasing and k even

(c) S′ is increasing

Figure 4: Proof of Lemma 3.3

Lemma 4.2. Let G be a 2-connected graph which is not a 3-cycle, xy ∈ E(G) and z ∈ V (G) \ {x, y}. If
dG(x) ≤ 4, dG(y) ≤ 4, dG(z) ≤ 3 and dG(v) = 3 for all v ∈ V (G) \ {x, y, z}, then there are two x − y paths
P1, P2 in G − xy with 1 ≤ |E(P1)| − |E(P2)| ≤ 2.

Proof. Suppose the theorem is false and let (G, x, y, z) be a counterexample where |V (G)| + |E(G)| is
minimum. Clearly |V (G)| ≥ 4. Let G′ = G − xy. Note that dG′(v) ≥ 2 for every v ∈ V (G′) \ {x, y}. We
may assume there are no two x − y paths in G′ whose lengths differ by 1 or 2.

Claim 1: G′ is 2-connected.
Suppose G′ is not 2-connected. Since G is not a cycle, there exists a 2-connected block B in G′. Let Q1 be
an x − B path and let Q2 be a B − y path in G′. Note that Q1 ∩ Q2 = /0. Let q1 and q2 be the endvertices of
Q1 and Q2 in B, respectively. Since G is 2-connected, the block graph of G′ is a path, so the only vertices
of degree 2 in B are q1, q2, and possibly z. Let B′ = B + q1q2 if q1q2 /∈ E(B) and B′ = B otherwise. If
B′ is a triangle, then B′ = B and there are two q1 − q2 paths R1, R2 in B of lengths 1 and 2. If B′ is not
a triangle, then by minimality of G there are two q1 − q2 paths R1, R2 in B whose lengths differ by 1
or 2. Now P1 = Q1 ∪R1 ∪Q2 and P2 = Q1 ∪R2 ∪Q2 are two x−y paths in G′ whose lengths differ by 1 or 2.

Claim 2: There are no non-trivial 2-edge-cuts in G′.
Suppose the claim is false, so there exists a non-trivial 2-edge-cut {e, f } with e, f ∈ E(G′). Let K be the
component of G′ − e − f with |V (K) ∩ {x, y, z}| ≤ 1. We choose e, f over all non-trivial 2-edge-cuts to
minimise the order of K. By the choice of e and f the component K is 2-connected. Let eK and fK denote
the ends of e and f in K, respectively. We may assume x /∈ V (K).
First suppose y /∈ V (K). By Claim 1, G′ is 2-connected so there are two disjoint {x, y} − {eK, fK} paths
Q1 and Q2 in G′. If K is a triangle, then let P1, P2 denote the eK − fK paths in K of lengths 1 and 2,

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 12

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

respectively. If K is not a triangle, then by minimality of G, there are two eK − fK paths P1, P2 in K whose
lengths differ by 1 or 2. Now Q1 ∪ P1 ∪ Q2 and Q1 ∪ P2 ∪ Q2 are two x − y paths in G′ whose lengths differ
by 1 or 2.
Thus, we may assume y ∈ V (K) and z /∈ V (K). We may assume y ̸= eK. If K is a triangle, then let P1,
P2 denote the eK − y paths in K of lengths 1 and 2, respectively. If K is not a triangle, then either K or
K + eKy satisﬁes the conditions of Lemma 4.2. By minimality of G there are two eK − y paths P1, P2 in
K whose lengths differ by 1 or 2. Let Q be an x − eK path in G′ having no edges in K. Now Q ∪ P1 and
Q ∪ P2 are two x − y paths in G′ whose lengths differ by 1 or 2.

Note that Claim 1 implies that if u, v ∈ {x, y, z} and dG(u) = dG(v) = 2, then u and v are non-adjacent.
Let G′′ denote the graph obtained from G′ by suppressing the vertices of degree 2. Note that G′′ is
cubic. If G′′ is not simple, then Claim 2 implies that G′′ consists of three parallel edges and G′ is a
θ -graph consisting of 4 or 5 vertices. In this case it easy to see that there are two x − y paths in G′ whose
lengths differ by 1 or 2. Thus we may assume that G′′ is simple. By Claim 2, G′′ is 3-connected, so by
Theorem 1.4 there exists an induced non-separating cycle C in G′ containing x and not containing y. Let
w ∈ V (C) \ {z} such that fC(x, w) ∈ {1, 2}. Let P1 and P2 denote the two x − w paths in C, and let Q be a
w − y path intersecting C only in w. Now P1 ∪ Q and P2 ∪ Q are two x − y paths in G′ whose lengths differ
by 1 or 2.

From Lemma 4.2 we can immediately derive the following.

Theorem 4.3. Let G be a 2-connected subcubic graph and x, y, z ∈ V (G). If d(v) = 3 for all v ∈
V (G) \ {x, y, z}, then there are two x − y paths P1, P2 with 1 ≤ |E(P1)| − |E(P2)| ≤ 2.

Proof. The statement is trivial if G is a 3-cycle. If xy ∈ E(G) and G is not a 3-cycle, then by Lemma 4.2
there exist two x − y paths in G − xy whose lengths differ by 1 or 2. If xy /∈ E(G), then G′ = G + xy
satisﬁes the conditions of Lemma 4.2. Thus there are two x − y paths in G whose lengths differ by 1 or
2.
 The next step is to allow two vertices of degree 2 in V (G) \ {x, y}. Note that in the following theorem
we require the vertices x1, x2, y, z to have degree exactly 2.

Theorem 4.4. Let x1, x2, y, z be four distinct vertices of degree 2 in a 2-connected graph G. If d(v) = 3
for all v ∈ V (G) \ {x1, x2, y, z}, the vertices x1, x2 are not adjacent, and x1, x2 are not opposite vertices in
a 4-cycle in G, then there are two x1 − x2 paths P1, P2 with |E(P1)| − |E(P2)| ∈ {1, 2}.

Proof. Suppose the theorem is false and let (G, x1, x2, y, z) be a counterexample where G has minimum
size. Clearly we can assume |V (G)| ≥ 5.

Claim 1: x1y, x1z, x2y, x2z /∈ E(G).
Suppose the claim is false. We may assume x1y ∈ E(G). Let x′
1 be the neighbour of x1 distinct from y and
let y′ be the neighbour of y distinct from x′
1. Since G is 2-connected and x1x2 /∈ E(G), we have x′
1 ̸= y′

and x′
1 ̸= x2.
First suppose x′
1y′ ∈ E(G). In this case both x′
1 and y′ have degree 3 in G. We can assume that there are
no two x′
1 − x2 paths in G′ = G − x1 − y whose lengths differ by 1 or 2, since otherwise there are also two

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 13

KASPER SZABO LYNGSIE AND MARTIN MERKER

x1 − x2 paths in G whose lengths differ by 1 or 2. Thus, by minimality of G, we have x′
1x2 ∈ E(G′) or x′
1,
x2 are contained in a 4-cycle. Similarly, we can assume that there are no two y′ − x2 paths in G′ whose
lengths differ by 1 or 2. Again, minimality of G implies that y′x2 ∈ E(G′) or y′, x2 are contained in a
4-cycle. Note that x2 cannot be adjacent to both x′
1 and y′ since otherwise G is a 5-cycle with a chord
and contains only three vertices of degree 2. Thus x2 is contained in a 4-cycle with x′
1 and it follows by
2-connectivity of G that G is a 6-cycle with chord x′
1y′. It is easy to see that also in this case there are two
x1 − x2 paths whose lengths differ by 1 or 2.
Now suppose x′
1y′ /∈ E(G). Let G′′ be the graph obtained from G − x1 − y by adding the edge e = x′
1y′.
Note that G′′ is 2-connected and x2, z are the only vertices of degree 2 in G′′. By Theorem 4.3, there
are two x′
1 − x2 paths Q1, Q2 in G′′ whose lengths differ by 1 or 2. If Q1 does not contain e, let P1 be
the x1 − x2 path consisting of x1x′
1 and Q1. If Q1 contains e, let P1 be the x1 − x2 path we obtain from
Q1 by replacing e with the path x1yy′. We analogously deﬁne an x1 − x2 path P2 using Q2. Note that
|E(P1)| = |E(Q1)| + 1 and |E(P2)| = |E(Q2)| + 1, so P1 and P2 are as desired.

Claim 2: There are no non-trivial 2-edge-cuts in G.
First, suppose there exists a non-trivial 2-edge-cut {e, f } such that G − e − f has a component K with
|V (K) ∩ {x1, x2, y, z}| ≤ 1. We choose such a 2-edge-cut {e, f } for which the component K containing
at most one vertex of {x1, x2, y, z} has minimal size. Note that K is 2-connected. Let eK, fK denote
the ends of e and f in K. If V (K) ∩ {x1, x2} = /0, then, since G is 2-connected, there exist two disjoint
{x1, x2} − {eK, fK} paths P1, P2 in G − E(K). Since K is 2-connected, by Theorem 4.3 there are two
eK − fK paths Q1, Q2 in K whose lengths differ by 1 or 2. Now P1 ∪ Q1 ∪ P2 and P1 ∪ Q2 ∪ P2 are two
x1 − x2 paths whose lengths differ by 1 or 2. Thus, we may assume x1 ∈ V (K). Again, by Theorem 4.3,
there are two x1 − eK paths Q1, Q2 whose lengths differ by 1 or 2. Let P be an eK − x2 path in G − E(K).
Now Q1 ∪ P and Q2 ∪ P are two x1 − x2 paths whose lengths differ by 1 or 2. Thus, we have the following:

(*) For every non-trivial 2-edge-cut {e, f } in G, each component of G − e − f contains two vertices of
{x1, x2, y, z}.

Let {e, f } be a non-trivial 2-edge-cut for which the component K of G − e − f containing x1 has minimal
size. Now K is 2-connected by (*), Claim 1, and since x1 is not adjacent to x2. Let eK and fK denote the
ends of e and f in K. Let L be the component of G − e − f different from K. First suppose x2 ∈ V (K). By
(*), we have y ∈ V (L) and z ∈ V (L). By minimality of G there are two x1 − x2 paths in K whose lengths
differ by 1 or 2. Thus we may assume x2 ∈ V (L). By (*), we may assume y ∈ V (K) and z ∈ V (L). If x1 is
not adjacent to eK and x1, eK are not opposite vertices in a 4-cycle, then by minimality of G there are two
x1 − eK paths in K whose lengths differ by 1 or 2. Since these paths can be extended to x1 − x2 paths in G,
we may assume that x1 is adjacent to eK or x1, eK are opposite vertices in a 4-cycle. Similarly we can
assume that either x1 is adjacent to fK or x1, fK are opposite vertices in a 4-cycle. If x1 is adjacent to both
eK and fK, then K is a 4-cycle where x1 and y are opposite vertices in a 4-cycle. In this case there exist
x1 − eK paths in K of lengths 1 and 3. Thus, we may assume that x1 and fK are opposite vertices in a 4-
cycle. If also x1, eK are opposite vertices in a 4-cycle, then there are x1 − eK paths of length 2 and 4 in K. If
x1 is adjacent to eK then there are x1 −eK paths of length 1 and 3 in K. This concludes the proof of Claim 2.

Let G′ denote the graph obtained from G by suppressing the vertices of degree 2. By Claim 2 and the
fact that G′ is cubic, the graph G′ is simple and 3-connected. Now Theorem 1.4 implies that there is a

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 14

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

Figure 5: Proof of Theorem 4.4

non-separating induced cycle C in G containing x1 and not containing z.
Suppose x2 /∈ V (C). There are two different vertices v1, v2 ∈ V (C) such that fC(x1, v1) = fC(x1, v2) ∈
{1, 2}. In particular, there exists a vertex v ∈ V (C) different from y for which fC(x1, v) ∈ {1, 2}. Let P be
a v − x2 path in G − E(C), and let Q1, Q2 be the two x1 − v paths on C. Now Q1 ∪ P and Q2 ∪ P are two
x1 − x2 paths whose lengths differ by 1 or 2.
Thus we may assume x2 ∈ V (C). Let C1 and C2 be the two x1 − x2 paths on C. We may assume
|E(C1)| ≤ |E(C2)|. If |E(C1)| = |E(C2)|, we may assume that C2 does not contain y. Let v be the
neighbour of x2 on C1. Note that v ∈ V (C) \ {x1, x2, y}. For a vertex w ∈ V (C2), let Q1(w) = x1C2w and
Q2(w) = wC2x2, see Figure 5. Moreover, for w ∈ V (C2), let

f (w) = |E(C1)| − 2 + |E(Q2(w))| − |E(Q1(w))| .

Note that as we move from x1 to x2 along C2, the function f decreases by 2 at every vertex. We have
f (x1) = |E(C)| − 2. Since |E(C)| ≥ 5, we have f (x1) ≥ 3.
By deﬁnition, f (x2) = |E(C1)| − |E(C2)| − 2 ≤ −2. If f (x2) < −2, then there are two vertices w1, w2 ∈
V (C2) \ {x1, x2} such that | f (w1)| = | f (w2)| ∈ {1, 2}. In particular, there exists a vertex w ∈ V (C2) \
{x1, x2, y} with | f (w)| ∈ {1, 2}. If f (x2) = −2, then |E(C1)| = |E(C2)| and y is not contained in C2. Also
in this case there exists a vertex w ∈ V (C2) \ {x1, x2, y} with | f (w)| ∈ {1, 2}.
In each case, we can choose w ∈ V (C2) such that d(w) = 3 and | f (w)| ∈ {1, 2}. Let P be a v − w path in
G − E(C). Now (C1 − vx2) ∪ P ∪ Q2(w) and Q1(w) ∪ P ∪ {vx2} are two x1 − x2 paths and the difference of
their lengths is |E(C1)| − 2 + |E(Q2(w))| − |E(Q1(w))| = | f (w)|, which is 1 or 2 by our choice of w.

The graph G in Figure 6 shows that Theorem 4.4 is not true if we allow x1 and x2 to be opposite
vertices in a 4-cycle C. Let G′ = G − C and let x′
1, x′
2 be the two vertices in N(C). There are no two
x′
1 − x′
2 paths in G′ whose lengths differ by 1 or 2 which shows that Theorem 4.4 is not true if we allow

Figure 6: A graph where no two x1, x2-paths differ by one or two in length.

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 15

KASPER SZABO LYNGSIE AND MARTIN MERKER

x1 and x2 to be adjacent. Note that the graph in Figure 6 contains two disjoint {x1, x2} − {y, z} paths
which are k-close provided that dist(x1, y) ≥ k. The following lemma shows that if dist(x1, y) ≥ k and
dist(x2, y) ≥ k, then we can always ﬁnd two disjoint {x1, x2} − {y, z} paths which are k-close or two
x1 − x2 paths whose lengths differ by 1 or 2. These k-close paths can be used in Section 5 to ﬁnd a cycle
and a path which are k-close.

Lemma 4.5. Let k be a natural number, G a 2-connected graph and x1, x2, y, z ∈ V (G) distinct vertices
of degree 2. Assume that dist(xi, y) ≥ k for i = 1, 2. If d(v) = 3 for all v ∈ V (G) \ {x1, x2, y, z}, then G
contains two x1 − x2 paths P1, P2 with |E(P1)| − |E(P2)| ∈ {1, 2}, or G contains two disjoint {x1, x2} −
{y, z} paths Q1, Q2 such that |E(Q1, Q2)| ≥ k.

Proof. We prove the statement by induction on k. If x1 and x2 are not adjacent and not opposite vertices
in a 4-cycle, then the existence of the two desired x1 − x2 paths follows immediately from Theorem 4.4.
Thus we may assume that x1 and x2 are adjacent or opposite vertices in a 4-cycle. We can easily ﬁnd two
disjoint {x1, x2} − {y, z} paths Q1 and Q2 with |E(Q1, Q2)| ≥ 1 so the statement is true for k ≤ 1. Suppose
now k ≥ 2 and that the statement is true for k − 1 and k − 2. If x1 and x2 are adjacent, we deﬁne x′
1 to be
the neighbour of x1 different from x2, unless this vertex is z, in which case we choose the neighbour of z
different from x1 to be x′
1. We analogously deﬁne x′
2. We set G′ = G − x1 − x2 − z if z was a neighbour of
x1 or x2 and G′ = G − x1 − x2 otherwise.
If x1 and x2 are opposite vertices in a 4-cycle C, then let u and v be the two vertices in N(C). If one of
these vertices is z, say u, then we deﬁne x′
1 as the neighbour of z not in C and x′
2 as v, otherwise we choose
u and v as x′
1 and x′
2. We set G′ = G −V (C) − z if z had a neighbour on C and G′ = G −V (C) otherwise.
It is easy to see that G′ is connected. Suppose G′ is not 2-connected. Then the block B1 containing x′
1
is different from the block B2 containing x′
2 and both blocks are endblocks. We may assume that B1
contains at most one of y and z. Let c be the cutvertex of G′ which is contained in B1. By Theorem 4.3,
there are two x′
1 − c paths P1 and P2 in B1 whose lengths differ by 1 or 2. Let P be a c − x′
2 path in G′.
Now P1 ∪ P and P2 ∪ P are two x′
1 − x′
2 paths whose lengths differ by 1 or 2 and it is easy to see how they
can be extended to x1 − x2 paths with the same property. Hence, we may assume that G′ is 2-connected.
If z /∈ V (G′), then by Theorem 4.3 there exist two x′
1 − x′
2 paths in G′ whose lengths differ by 1 or 2 and
they can be extended to x1 − x2 paths with this property. Thus, we may assume that z ∈ V (G′). Note that
if x1 and x2 are adjacent, then dist(x′
1, y) ≥ dist(x1, y) − 1 ≥ (k − 1) and dist(x′
2, y) ≥ (k − 1). If x1 and
x2 are opposite vertices in a 4-cycle, then dist(x′
1, y) ≥ dist(x1, y) − 2 ≥ (k − 2) and dist(x′
2, y) ≥ (k − 2).
We may assume that there are no two x′
1 − x′
2 paths in G′ whose lengths differ by 1 or 2. By induction
there exist two {x′
1, x′
2} − {y, z} paths Q′
1 and Q′
2 such that |E(Q′
1, Q′
2)| ≥ k − 1 (if x1 and x2 are adjacent
in G) or |E(Q′
1, Q′
2)| ≥ k − 2 (if x1 and x2 are opposite vertices in a 4-cycle). The paths Q′
1 and Q′
2
can be extended to {x1, x2} − {y, z} paths Q1 and Q2. If x1 and x2 were adjacent, then |E(Q1, Q2)| =
|E(Q′
1, Q′
2)| + 1 ≥ k. If they were opposite vertices in a 4-cycle, then |E(Q1, Q2)| = |E(Q′
1, Q′
2)| + 2 ≥ k.
In any case, |E(Q1, Q2)| ≥ k.

5 Proof of the main theorem

In this section we prove the main theorem of this paper. The general idea is to show that if G is large
enough, then G is k-good. We begin the proof by taking a minimal u, v-θ -graph Θ in G where u and v

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 16

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

are far apart in G. We would like to investigate the 2-connected endblocks of G − Θ, but unfortunately
G − Θ might contain many vertices of degree 1. Instead we investigate the subgraph H of G − Θ which is
induced by the vertices of degree at least 2 in G − Θ. Now there might be vertices of degree less than 2
in H, but we show in Section 5.1 that we may assume there are only few of them. We distinguish two
types of 2-connected endblocks of H depending on whether its neighbours on Θ lie on only one leg or
on at least two different legs. We call these endblocks Θ-isolated and Θ-connecting, respectively. In
Section 5.2 we show that G is k-good if the number of Θ-connecting endblocks in H is sufﬁciently large.
In Section 5.3 we show the same if H has many Θ-isolated endblocks. Finally, the only remaining case
is where H has only few 2-connected endblocks. This is dealt with in Section 5.4 which concludes the
proof.

5.1 General framework and initial observations

Deﬁnition 5.1 (short θ -graph). A shortest u, v-θ -graph in G is a u, v-θ -graph Θ = (P1, P2, P3) for which
|E(Θ)| is minimal. We say a graph is a short θ -graph if it is a shortest u, v-θ -graph for some vertices
u, v.

Note that by Menger’s theorem a shortest u, v-θ -graph in G exists if and only if there exists no 2-cut
separating u and v. In particular, it always exists if G is 3-connected.

Deﬁnition 5.2 (F(Θ), Θ-friendly). Let Θ = (P1, P2, P3) be a short θ -graph in a 3-connected cubic graph
G. We write F(Θ) for the set of all vertices in G − Θ with at least two neighbours in Θ. We say a vertex
v ∈ V (G) is Θ-friendly if v ∈ F(Θ) and NΘ(v) ̸⊆ V (Pi) for every i ∈ {1, 2, 3}.

Every vertex v ∈ F(Θ) is either Θ-friendly or NΘ(v) is contained in one leg of Θ. If v ∈ F(Θ) is not
Θ-friendly, then any two neighbours of v in Θ have distance at most 2 on Θ since the legs have minimal
length. The following shows that we can assume that F(Θ) has only few vertices which are Θ-friendly or
whose neighbours have distance 1 on Θ.

Lemma 5.3. Let Θ = (P1, P2, P3) be a short θ -graph in a 3-connected cubic graph G. If

(a) G − E(Θ) has at least 3
2 k edges with both ends in V (Θ), or

(b) G − Θ has at least 3
2 k vertices which are Θ-friendly, or

(c) G − Θ has at least 3k isolated vertices, or

(d) G − Θ has at least 3k isolated edges, or

(e) Θ has at least 3
2 k edges which are contained in a triangle in G,

then G is k-good.

Proof. (a) Since Θ is a short θ -graph, all the legs are induced paths in G. If G − E(Θ) has at least 3
2 k
edges with both ends in V (Θ), then there is a leg, say P1, such that k of the edges are incident with P1.
Now P1 and the cycle P2 ∪ P3 are k-close.

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 17

KASPER SZABO LYNGSIE AND MARTIN MERKER

(b) If G − Θ has at least 3
2 k vertices which are Θ-friendly, then there exists a leg of Θ, say P1, such
that at least k vertices of G − Θ have one neighbour on P1 and one neighbour on a different leg. Now P1
and the cycle P2 ∪ P3 are k-close.
(c) Let S denote the set of isolated vertices in G − Θ which are not Θ-friendly. By (b), we may assume
|S| ≥ 3
2 k. Since Θ is a short θ -graph, the neighbours of v on Θ induce a path of length 2 for every v ∈ S.
Now there are two legs of Θ, say P1 and P2, such that at least k vertices in S have their neighbours on P1
or P2. These k vertices and their incident edges together with P1 and P2 form a θ (k, 1)-necklace.
(d) We colour some vertices in G − Θ with colours 1,2,3 such that v ∈ V (G) has colour i if v is
contained in an isolated edge in G − Θ and NΘ(v) ⊂ V (Pi). Let X denote the set of isolated edges in
G − Θ in which both vertices received a colour. It is easy to see that since Θ is a short θ -graph and G is
3-connected, no two adjacent vertices are coloured the same. Since there are at least 3k isolated edges in
G − Θ, we may assume by (b) that |X| ≥ 3k − 3
2 k = 3
2 k. Thus |V (X)| ≥ 3k, so at least k vertices in V (X)
have the same colour, say colour 1. Let Y ⊂ V (X) denote the set of vertices coloured 1. Since Θ is a short
θ -graph, the neighbours on P1 of any vertex in Y induce a path of length at most 2 in P1. Hence there is
a path P′ contained in the subgraph of G induced by P1 and Y , containing all vertices in Y . Since each
vertex in Y has a neighbour in colour 2 or 3, the path P′ and the cycle P2 ∪ P3 are k-close.
(e) In this case there are two legs of Θ, say P1 and P2, such that P1 ∪ P2 contains k edges which are
contained in triangles T1, . . . , Tk in G. Now the union of P1, P2 and T1, . . . , Tk is a k-wiggly necklace.

It is possible that F(Θ) contains many vertices which are not Θ-friendly. Unfortunately such vertices
make it more difﬁcult to show that G is k-good. In the following we will therefore be interested in
subgraphs of G − (Θ ∪ F(Θ)).

Deﬁnition 5.4 (B+, Θ+). Let Θ be a short θ -graph in a 3-connected cubic graph G and let B be a
connected subgraph of G − Θ. We deﬁne B+ as the subgraph of G induced by B ∪ NF(Θ)(B) and Θ+ as
the subgraph of G induced by Θ ∪ F(Θ).

Note that (B+)+ = B+ for every connected subgraph B of G − Θ. From now on we focus on the
structure of G − Θ+. We start by showing that G is k-good if G − Θ+ contains many vertices of degree
less than 2. This implies that G is k-good if G − Θ+ has many endblocks which are not 2-connected.

Theorem 5.5. Let Θ = (P1, P2, P3) be a short θ -graph in a 3-connected cubic graph G. If G − Θ+ has at
least 8k vertices of degree at most 1, then G is k-good.

Proof. Let L denote the set of vertices in G − Θ+ which have degree at most 1, so |L| ≥ 8k. Every vertex
in L has either at least two neighbours in F(Θ) or exactly one neighbour in each of F(Θ) and Θ. Let
L′ ⊆ L denote the set of vertices having no θ -friendly neighbour. By Lemma 5.3 (b) we may assume
|L′| ≥ |L| − 3
2 k > 6k. For i ∈ {1, 2, 3}, let Fi be the set of vertices in F(Θ) with two neighbours on Pi. For
i, j ∈ {1, 2, 3} with i ̸= j, let Xi, j be the set of vertices in L′ having a neighbour in both Fi and Fj. Let Yi, j
be the set of vertices in L′ having a neighbour in Fi and in Pj. Finally, let Zi be the set of vertices in L′

having at least two neighbours in Fi or exactly one in both Fi and Pi. Let

X = X1,2 ∪ X2,3 ∪ X1,3
Y = Y1,2 ∪Y1,3 ∪Y2,1 ∪Y2,3 ∪Y3,1 ∪Y3,2
Z = Z1 ∪ Z2 ∪ Z3

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 18

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

Clearly, X ∪Y ∪ Z = L′, so |X| + |Y | + |Z| > 6k. We distinguish three cases.

Case 1: |X| ≥ 3
2 k.
We may assume that |X1,2 ∪ X1,3| ≥ k. Let F ′
i ⊆ Fi be the set of vertices that have a neighbour in
X1,2 ∪ X1,3. Since Θ is a short θ -graph, for i ∈ {1, 2, 3} there exists a path P′
i in G[V (Pi) ∪ F ′
i ] which
contains F ′
i . We can combine the paths P′
2 and P′
3 to a cycle C in Θ+ which contains F ′
2 ∪ F ′
3 but no in-
terior vertices of P1. Now P′
1 and C are k-close since every x ∈ X1,2 ∪ X1,3 has a neighbour in both P′
1 and C.

Case 2: |Y | ≥ 3k.
We may assume that |Y1,2 ∪Y1,3| ≥ k. For every x ∈ Y1,2 ∪Y1,3, let y(x) ∈ F1 be a neighbour of x. Since Θ
is a short θ -graph, there exists a path P′
1 in G[V (P1) ∪ F1] which contains y(x) for every x ∈ Y1,2 ∪Y1,3.
Now P′
1 and the cycle P2 ∪ P3 are k-close.

Case 3: |Z| ≥ 3
2 k.
We may assume that |Z1 ∪ Z2| ≥ k. For every x ∈ Zi, let Px denote the shortest subpath of Pi containing
NPi(x) and the neighbours of NFi(x) on Pi. Since Θ is a short θ -graph, the length of Px is at most 4. Note
that this implies that x has at most two neighbours in Fi. Let Gx be the subgraph of G induced by Px,
NFi(x), and x. We deﬁne a subgraph Hx of Gx in the following way. If Gx contains a cycle Cx of length
3 or 4 such that |E(Cx ∩ Px)| = 1, then we set Hx = Cx. It is easy to check that Gx contains such a cycle
unless Px has length 3 and x has two neighbours in Fi, as shown in Figure 7(b). In this case, we set
Hx = Gx. Note that if Hx = Gx, then x and the two endvertices of Px form a 3-cut in G. It easy to see that
in each case the endvertices of Hx ∩ Px can be joined by two paths in Hx whose lengths differ by 1 or 2.
Moreover, the graphs Hx are pairwise disjoint. Hence, the graph formed by the union of P1 ∪ P2 and all
the graphs Hx with x ∈ Z1 ∪ Z2 is a k-wiggly necklace.

(a) |E(Px)| ∈ {3, 4} (b) |E(Px)| = 3

(c) |E(Px)| ∈ {2, 3} (d) |E(Px)| = 2

Figure 7: Proof of Theorem 5.5. The four ways x ∈ Z can be joined to Θ+.

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 19

KASPER SZABO LYNGSIE AND MARTIN MERKER

Deﬁnition 5.6 (Θ-isolated, Θ-connecting). We say a connected subgraph B of G − Θ+ is Θ-connecting if
NΘ(B+) ̸⊆ V (Pi) for every i ∈ {1, 2, 3}. We say B is Θ-isolated if NΘ(B+) ̸= /0 and B is not Θ-connecting.

Note that each 2-connected endblock of G − Θ+ is either Θ-connecting or Θ-isolated.

5.2 Many Θ-connecting 2-connected endblocks in G − Θ+

Given a subgraph H of G − Θ+, we are often interested in how it attaches to Θ. We are typically interested
in NΘ(H+), but we only want to include at most one neighbour for each vertex in H+ − H. For this
purpose we deﬁne Θ-projections which map vertices in NH(Θ+) to neighbours in Θ or vertices at distance
2 in Θ.

Deﬁnition 5.7 (Θ-projection π). Let Θ be a short θ -graph in G and H = G − Θ+. A function π :
NH(Θ+) → V (Θ) is called a Θ-projection if π(v) is a vertex in Θ whose distance to v in G is minimal.

By deﬁnition, if v ∈ G − Θ+ has a neighbour u in Θ, then π(v) = u. If v ∈ G − Θ+ has a neighbour in
Θ+ but not in Θ, then there exists a vertex w ∈ F(Θ) which is adjacent to both v and π(v). We now show
that G is k-good if G − Θ+ contains sufﬁciently many Θ-connecting 2-connected endblocks.

Theorem 5.8. Let Θ = (P1, P2, P3) be a short θ -graph in a cubic 3-connected graph G and H = G − Θ+.
If the number of Θ-connecting 2-connected endblocks in H is at least 21k2 + 3
2 k, then G is k-good.

Proof. Let S be the set of vertices which are contained in a Θ-connecting 2-connected endblock of H and
which have a neighbour in Θ+. We colour the vertices in S with colours 0, 1, 2, and 3 in the following
way: If for some i ∈ {1, 2, 3}, the vertex v has a neighbour in Pi, or v has a neighbour in F(Θ) which
has two neighbours in Pi, then v receives colour i. Otherwise, v receives colour 0. Notice that v receives
colour 0 if and only if v has a neighbour in F(Θ) which is Θ-friendly. Let B be the set of Θ-connecting
2-connected endblocks in H which contain no vertices in colour 0. Notice that the blocks in B are
pairwise disjoint since G is cubic. By Lemma 5.3 (b) we may assume that at most 3
2 k vertices are coloured
0 and thus |B| ≥ 21k2. Notice that each block in B contains vertices in at least two different colours
since the blocks in B are Θ-connecting. Let B0 be the sets of blocks in B which contain no two vertices
of the same colour. For i ∈ {1, 2, 3}, let Bi be the set of blocks in B which contain at least two vertices
in colour i. Notice that B0 is disjoint from B1 ∪ B2 ∪ B3 and thus |B0| + |B1 ∪ B2 ∪ B3| ≥ 21k2. Let
π : NH(Θ+) → V (Θ) be a Θ-projection. We distinguish the following two cases.

Case 1: |B1 ∪ B2 ∪ B3| ≥ 8k2.
We may assume |B1| ≥ 8
3 k2. For each B ∈ B1, let uB and vB denote two vertices coloured 1 in B. Let
G1 be the graph obtained from P1 by adding the edges π(uB)π(vB) for every B ∈ B1. Finally, let PB
be a π(uB) − π(vB) path whose interior vertices lie in B+ and which contains a coloured vertex in B
whose colour is not 1 (such a path exists since B is 2-connected). See Figure 8(a) for an illustration. By
Lemma 3.1, there exists a path P′ in G1 containing at least k edges of the form π(uB)π(vB). We obtain a
path P in G from P′ by replacing each edge of the form π(uB)π(vB) by PB. Now P and the cycle P2 ∪ P3
are k-close.
 ADVANCES IN COMBINATORICS, 2021:3, 36pp. 20

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

(a) Case 1 (b) Case 2.1.1

Figure 8: Proof of Theorem 5.8

Case 2: |B0| ≥ 13k2.
Each block in B0 contains at most three coloured vertices, and at most one cutvertex in H. In particular,
each block in B0 contains at most four vertices of degree 2. Let B4 denote the set of blocks in B0
containing four vertices of degree 2, and B′ = B0 \ B4. Notice that by 3-connectivity of G, each block
in B′ contains precisely three vertices of degree 2 and at least two of them are coloured. We have
|B4| + |B′| ≥ 13k2.

Case 2.1: |B4| ≥ 10k2.
Each B ∈ B4 contains precisely one vertex of each colour and precisely one vertex xB which is a cutvertex
in H. Let yB, zB ∈ B be coloured vertices such that yB has colour 1 and zB has colour 2. We deﬁne QB as
a π(yB) − xB path which contains zB and whose interior vertices lie in B+. Let X = {xB : B ∈ B4}. We
deﬁne X1 ⊂ X as the subset of vertices which lie in a component of H containing only one vertex of X.
Let X2 = X \ X1. Note that |X1| + |X2| ≥ 10k2. We consider two cases.

Case 2.1.1: |X1| ≥ 8k2.
For every xB ∈ X1, let PB be an xB − Θ path with PB ∩ B = {xB} and let x′
B be the endvertex of PB on
Θ, see Figure 8(b). We may assume that at least 8
3 k2 vertices of the form x′
B lie on P1. Let G1 be the
graph obtained from P1 by adding the edges π(yB)x′
B for every B ∈ B4 with xB ∈ X1 and x′
B ∈ V (P1). By
Lemma 3.1, there exists a path P′ in G1 containing at least k edges of the form π(yB)x′
B. We obtain a path
P in G from P′ by replacing each edge of the form π(yB)x′
B by QB ∪ PB. Now P and the cycle P2 ∪ P3 are
k-close.

Case 2.1.2: |X2| ≥ 2k2.
Let P be a collection of disjoint paths in H such that for every P ∈ P the endvertices of P are in X2 and |P|
is maximal. By Lemma 1.2, in every component of H there is at most one vertex of X2 which is not an end-
vertex of a path in P. This implies |P| ≥ 1
3 |X2| ≥ 2
3 k2. For any two blocks B, B′ ∈ B4 which are joined by

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 21

KASPER SZABO LYNGSIE AND MARTIN MERKER

(a) Case 2.1.2 (b) Case 2.2

Figure 9: Proof of Theorem 5.8

an xB − xB′ path P ∈ P, let QB,B′ be the path QB ∪ P ∪ QB′. Let G1 be the graph obtained from P1 by adding
the edges π(yB)π(yB′) for every pair of blocks B, B′ ∈ B4 which are joined by a path in P, see Figure 9(a).
Since |P| ≥ 2
3 k2 ≥ 8
3 · k
2 ( k
2 − 1) + 1, by Lemma 3.1 there exists a path P′ in G1 containing at least k
2 edges
of the form π(yB)π(yB′). We obtain a path P in G from P′ by replacing each edge of the form π(yB)π(yB′)
by QB,B′. Since the path QB,B′ contains zB and zB′, the path P and the cycle formed by P2 and P3 are k-close.

Case 2.2: |B′| ≥ 3k2.
For each B ∈ B′, let uB and vB denote two distinct coloured vertices in B. Let PB be a π(uB) − π(vB) path
whose interior vertices lie in B+ and let G′ be the graph obtained from Θ by adding the edges π(uB)π(vB)
for every B ∈ B′, see Figure 9(b). By Lemma 3.3, there exists a cycle C′ in G′ containing at least k edges
of the form π(uB)π(vB). Let B′′ ⊂ B′ be the set of blocks B for which π(uB)π(vB) ∈ E(C′). Let C be the
cycle in G which is obtained from C′ by replacing π(uB)π(vB) by PB for every B ∈ B′′. By Theorem 4.3,
every B ∈ B′′ contains two uB − vB paths whose lengths differ by 1 or 2. Thus, the B′′-necklace formed
by the union of C and the blocks in B′′ is k-wiggly.

5.3 Many Θ-isolated 2-connected endblocks in G − Θ+

We now focus on Θ-isolated subgraphs H in G − Θ+. Typically H is an endblock or a connected
component of G − Θ+, so |NΘ(H+)| ≥ 2.

Deﬁnition 5.9 (Θ-span). Let B be a Θ-isolated subgraph of G − Θ+ with NΘ(B+) ⊂ V (Pi). Let QB be
the shortest subpath of Pi containing NΘ(B+). The Θ-span of B, denoted Sp(B), is deﬁned as the vertex
set of QB.

The Θ-span is very useful for studying the interplay between different Θ-isolated subgraphs. If
there are many Θ-isolated endblocks whose Θ-spans are pairwise disjoint, then it is easy to ﬁnd a long
θ -necklace or a k-wiggly necklace. If there are many Θ-isolated endblocks whose Θ-spans have pairwise

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 22

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

non-empty intersection, then we distinguish two cases depending on whether many of them are pairwise
crossing according to the following deﬁnition.

Deﬁnition 5.10 (crossing subgraphs). Let B1 and B2 be two Θ-isolated connected subgraphs of G − Θ+

with NΘ(B
+
1 ∪ B
+
2 ) ⊂ V (Pi). We say B1 and B2 are crossing if there exist vertices x1, y1 ∈ NΘ(B+
1 ) and
x2, y2 ∈ NΘ(B+
2 ) such that x2 ∈ x1Piy1, y1 ∈ x2Piy2.

If B1, B2 are two disjoint Θ-isolated endblocks with Sp(B1) ∩ Sp(B2) ̸= /0 and B1, B2 are not crossing,
then one of the two Θ-spans is contained in the other. This motivates the following deﬁnition.

Deﬁnition 5.11 (<Θ). Let B1 and B2 be two disjoint Θ-isolated subgraphs of G − Θ+. We write B1 <Θ B2
if and only if B1 and B2 are not crossing and Sp(B1) ⊂ Sp(B2).

It is easy to see that two disjoint Θ-isolated subgraphs B1, B2 of G − Θ+ satisfy B1 <Θ B2 if and only
if Sp(B1) ⊂ Sp(B2) and Sp(B1) ∩ NΘ(B+
2 ) = /0.

Deﬁnition 5.12 (Θ-chain). A Θ-chain C of length n is a sequence (H1, H2, . . . , Hn) of pairwise disjoint
Θ-isolated components of G − Θ+ with Hi <Θ Hi+1 for i ∈ {1, . . . , n − 1}. We say C is special if each Hi
has only 2-connected endblocks.

Note that if B1, B2, B3 are pairwise disjoint and B1 <Θ B2 and B2 <Θ B3, then Sp(B1) ∩ NΘ(B
+
3 ) ⊆
Sp(B2) ∩ NΘ(B
+
3 ) = /0 and thus B1 <Θ B3. This shows that every subsequence of a Θ-chain is again a
Θ-chain.
We now prove that if G contains a long special Θ-chain, then G is k-good. The proof consists of several
cases depending on the structure of the components in the Θ-chain. As a rough guideline, if many
endblocks have only few vertices of degree 2, then we ﬁnd a k-wiggly necklace by using the results
from Section 4. If there are many endblocks with many vertices of degree 2, then we construct a
θ (k, i)-necklace with i ∈ {1, 2}.

Lemma 5.13. Let Θ = (P1, P2, P3) be a shortest u, v-θ -graph in a cubic 3-connected graph G. If G
contains a special Θ-chain C of length 5k, then G is k-good.

Proof. Let H = G − Θ+. We may assume NΘ(C+) ⊂ V (P1) for every component C in C. Let C0 be the
ﬁrst component in C and c a vertex in Sp(C0) − NΘ+(C0) (such a vertex exists since otherwise the two
endvertices of Sp(C0) form a 2-cut in G). Note that c is contained in the Θ-span of every component in
C. Let L = uP1c and R = cP1v. We deﬁne SpL(B) = Sp(B) ∩V (L) and SpR(B) = Sp(B) ∩V (R) for every
Θ-isolated subgraph B of H with NΘ(B+) ⊂ V (P1). If SpL(B) ̸= /0, let ℓ1(B), ℓ2(B) denote the vertices of
SpL(B) which are closest to u and v on P1, respectively. Note that ℓ1(B) = ℓ2(B) if and only if SpL(B)
consists of a single vertex. If SpR(B) ̸= /0, we similarly deﬁne r1(B), r2(B) as the vertices of SpR(B)
which are closest to u and v, respectively. We colour the vertices of NH(Θ+) with colours 1 and 2 so
that v is coloured 1 if and only if v ∈ NH(L) or v has a neighbour in NF(Θ)(L). We say an endblock B of H
is unbalanced if B contains three vertices in the same colour. We say a component of H is unbalanced if it
contains an unbalanced endblock. Finally, we say a block or component is balanced if it is not unbalanced.

Case 1: C contains at least k unbalanced components.
Let C′ = (C1, . . . ,Ck) be a subsequence of C consisting of unbalanced components. For i ∈ {1, . . . , k}, let

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 23

KASPER SZABO LYNGSIE AND MARTIN MERKER

Figure 10: Proof of Lemma 5.13 Case 1

Bi denote an unbalanced endblock of Ci.
Suppose Bi contains three vertices coloured 1. If there exists x ∈ Bi and u ∈ F(Θ) with N(u) =
{ℓ1(Bi), ℓ2(Bi), x}, then ℓ1(Bi) and ℓ2(Bi) have distance at most 2. Since Θ is a short θ -graph, this implies
|SpL(Bi)| ≤ 3. Now there is at most one vertex in NΘ(B
+
i ) \ {ℓ1(Bi), ℓ2(Bi)} while there are at least two
vertices in Bi \ {x} coloured 1, a contradiction. Thus, there exists a Θ-projection π : NH(Θ+) → V (Θ)
such that ℓ1(Bi), ℓ2(Bi) ∈ π(NBi(Θ+)). Now let xi, yi, zi ∈ NBi(Θ+) be three vertices in colour 1 with
π(xi) = ℓ1(Bi) and π(yi) = ℓ2(Bi). Note that we have π(zi) ∈ SpL(Bi). Let wi denote the neighbour of zi
in Θ+. Let Qi be an ℓ1(Bi) − ℓ2(Bi) path which contains zi and whose interior vertices lie in B
+
i (such
a path exists since Bi is 2-connected). It is easy to see that there exists an ℓ1(Bi) − ℓ2(Bi) path Ri in Θ+

which contains wi, see Figure 10.
If Bi contains three vertices in colour 2, then we similarly choose xi, yi, zi ∈ NBi(Θ+) such that π(xi) =
r1(Bi) and π(yi) = r2(Bi). We deﬁne Qi as an r1(Bi) − r2(Bi) path which contains zi and whose interior
vertices lie in B+
i . We deﬁne Ri as an r1(Bi) − r2(Bi) path in Θ+ which contains wi, the neighbour of zi in
Θ+.
For each i ∈ {1, . . . , k}, let Θi be the union of Qi, Ri, and the edge wizi. Note that Θi is a θ -graph and
V (Θi) ⊂ V (C+
i ) ∪ SpL(Ci) ∪ SpR(Ci). Since SpL(C) ∩ SpL(C′) = /0 whenever C and C′ are two different
components of C, we have that Θ1, . . . , Θk are pairwise disjoint. Now the union of P1 ∪ P2 and all sub-
graphs Θi with i ∈ {1, . . . , k} contains a θ (k, 1)-necklace.

Case 2: C contains at least 4k balanced components.
Let C′ be a subsequence of C of length 4k containing no unbalanced components. For an endblock B of
H, let d2(B) denote the number of vertices of degree 2 in B. By 3-connectivity of G we have d2(B) ≥ 3
for every 2-connected endblock B. Note that the number of coloured vertices in a 2-connected endblock
B is d2(B) if B is a component in H. If B contains a cutvertex in H, then d2(B) − 1 vertices in B are
coloured. Thus, if d2(B) ≥ 6 then B is unbalanced. In particular, we have d2(B) ≤ 5 if B is an endblock
of a component in C′. We deﬁne

d2(C) = min{d2(B) : B is an endblock of C}

for every component C in C′. For i ∈ {3, 4, 5}, we deﬁne Ci as the subsequence of C′ containing all the
components C with d2(C) = i. Note that |C3| + |C4| + |C5| = |C′| = 4k.

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 24

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

Case 2.1: |C3| ≥ k.
We may assume |C3| = k and C3 = (C1, . . . ,Ck). Let Bi be an endblock of Ci with d2(Bi) = 3 for every
i ∈ {1, . . . , k}, and B = {B1, . . . , Bk}. Let π : NH(Θ+) → V (Θ) be a Θ-projection. For i ∈ {1, . . . , k}, we
deﬁne a path Qi in the following way. If Bi has two vertices of the same colour, say xi and yi, then let Qi
be an π(xi) − π(yi) path with interior vertices in B
+
i .
If Bi contains no two vertices of the same colour, then it contains a vertex in each colour and a cutvertex
in Ci. In this case, let xi be a coloured vertex in Ci which is not contained in Bi. Let yi be the coloured
vertex of Bi which has the same colour as xi. Now let Qi be an π(xi) − π(yi) path with interior vertices in
C+
i .
Since xi and yi have the same colour, the vertices of π(xi)P1π(yi) are contained in SpL(Ci) or SpR(Ci).
We have SpL(Ci) ∩ SpL(C j) = /0 and SpR(Ci) ∩ SpR(C j) = /0 for i, j ∈ {1, . . . , k} with i ̸= j since C3 is a
special Θ-chain. Thus, the k subpaths of the form π(xi)P1π(yi) with i ∈ {1, . . . , k} are pairwise disjoint.
Let C be the cycle we obtain from P1 ∪ P2 by replacing the path π(xi)P1π(yi) by the path Qi for each
i ∈ {1, . . . , k}. Let N be the union of C and all the blocks in B. Clearly N is a B-necklace. Since each
block in B has only three vertices of degree 2, the necklace N is k-wiggly by Theorem 4.3.

Case 2.2: |C4| ≥ 2k.
We may assume |C4| = 2k and C4 = (C1, . . . ,C2k). Let Bi be an endblock of Ci with d2(Bi) = 4 for every
i ∈ {1, . . . , 2k}, and B = {Bk+1, . . . , B2k}. Let π : NH(Θ+) → V (Θ) be a Θ-projection. Each Bi contains
at least three coloured vertices. Thus, Bi contains two vertices xi,1 and xi,2 of the same colour and a third
vertex yi of a different colour. Let zi be the fourth vertex of degree 2 in Bi. Either zi is a cutvertex in Ci or
it has the same colour as yi.
Let Si = ℓ2(Bi)P1r1(Bi) for i ∈ {1, . . . , 2k}. Note that NΘ(C+
j ) ⊂ Si for j ∈ {1, . . . , i−1} and |NΘ(C+
j )| ≥ 4.
This implies |E(Si)| ≥ 4(i − 1) + 1. In particular, the distance between π(xi,1) and π(yi) on P1 is at least
4i − 3. Let S′
i be a shortest xi,1 − yi path in Bi. Since Θ is a short θ -graph, we have |E(S′
i)| + 4 ≥ 4i − 3.
Thus for i ∈ {k + 1, . . . 2k} we have |E(S′
i)| ≥ 4i − 7 ≥ 4k − 3 ≥ k. For the same reason, the distance
between xi,2 and yi in Bi is at least k for i ∈ {k + 1, . . . , 2k}.
Now we can apply Lemma 4.5 to each block in B. Suppose for some i ∈ {k + 1, . . . , 2k} there exist two
disjoint {xi,2, xi,1} − {yi, zi} paths Qi,1, Qi,2 in Bi with |E(Qi,1, Qi,2)| ≥ k. It is easy to see that either Qi,1
can be extended to a cycle which is k-close to Qi,2, or Qi,2 can be extended to a cycle which is k-close
to Qi,1, see Figure 11. Thus, we can assume by Lemma 4.5 that for each i ∈ {k + 1, . . . , 2k} there exist
two xi,1 − xi,2 paths Pi,1 and Pi,2 such that |E(Pi,1)| − |E(Pi,2)| ∈ {1, 2}. As in Case 2.1, we can now ﬁnd
a cycle C which contains all the paths Pi,1 for i ∈ {k + 1, . . . , 2k}. The union of C with the blocks in B
forms a k-wiggly B-necklace.

Case 2.3: |C5| ≥ k.
We may assume |C5| = k and C5 = (C1, . . . ,Ck). If B is an endblock of some component in C5, then we
have 5 ≤ d2(B) by deﬁnition of C5 and d2(B) < 6 since B is balanced. Thus, we have d2(B) = 5 for
every endblock B of a component in C5. There are two vertices of each colour in B and one cutvertex. In
particular, the vertices ℓ1(B), ℓ2(B), r1(B), r2(B) exist and are pairwise distinct. Let π : NH(Θ+) → V (Θ)
be a Θ-projection such that r1(B) ∈ π(NB(Θ+)) for every endblock B of a component in C5. It is possible
that there exists a vertex in B+ which is adjacent to both r1(B) and r2(B), in which case r1(B) and r2(B)

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 25

KASPER SZABO LYNGSIE AND MARTIN MERKER

Figure 11: Proof of Lemma 5.13 Case 2.2

have distance 2 on Θ and their common neighbour on Θ, say s(B), is contained in π(NB(Θ+)). In this
situation we choose z(B) ∈ NB(Θ+) such that π(z(B)) = s(B). If r1(B) and r2(B) have no common
neighbour in B+, then we choose z(B) ∈ NB(Θ+) such that π(z(B)) = r1(B).
Let w(B) be the neighbour of z(B) in Θ+. Let Bi and B′
i be two different endblocks of Ci for i ∈ {1, . . . , k}.
We may assume r1(Bi) ∈ cP1r1(B′
i). Let Qi be an r1(Bi) − r2(B′
i) path whose interior vertices lie in C+
i
and which contains z(B′
i) (such a path exists since B′
i is 2-connected). It is easy to see that there exists an
r1(Bi) − r2(B′
i) path Ri in Θ+ which contains w(B′
i). For each i ∈ {1, . . . , k}, let Θi be the union of Qi, Ri,
and the edge w(B′
i)z(B′
i). As in Case 1, the θ -graphs Θ1,. . . ,Θk are pairwise disjoint. Now the union of
P1 ∪ P2 and Θ1, . . . , Θk contains a θ (k, 1)-necklace.

We now show that a graph with many Θ-isolated 2-connected endblocks is k-good. We distinguish
essentially three cases: there are many endblocks with pairwise disjoint spans, or many endblocks which
are pairwise crossing, or a sequence of endblocks B1,. . . ,Bℓ such that Bi <Θ B j for i < j. In the last case
we use this sequence to construct a Θ-chain which contains a special Θ-chain as a subsequence.

Theorem 5.14. Let Θ = (P1, P2, P3) be a shortest u, v-θ -graph in a cubic 3-connected graph G and
H = G − Θ+. If the number of Θ-isolated 2-connected endblocks in H is at least 5700k6, then G is
k-good.

Proof. We may assume k ≥ 3 since Θ contains a path and a cycle which are 2-close. Let n = 1900k6. We
may assume that there exist n pairwise disjoint Θ-isolated 2-connected endblocks B1, . . . , Bn such that
NΘ(B+
i ) ⊂ V (P1) for i ∈ {1, , . . . , n}. For two vertices x, y ∈ V (P1) we write x ≤ y if x ∈ uP1y. Note that
this deﬁnes a total order on V (P1). We write x < y if x ≤ y and x ̸= y. For an endblock B of H, let ℓ(B) and
r(B) denote the vertices of Sp(B) which are closest to u and v on P1, respectively. Let π : NH(Θ+) → V (Θ)
be a Θ-projection such that {ℓ(B), r(B)} ⊂ π(NB(Θ+)) for each 2-connected endblock B of H for which
ℓ(B) and r(B) have no common neighbour in F(Θ). We will only use π in this proof when we consider
blocks B that contain at least four vertices of degree 2. In this case it is easy to see that ℓ(B) and r(B) have
no common neighbour in F(Θ) since otherwise Sp(B) could contain at most three vertices. Let ℓi = ℓ(Bi)
and ri = r(Bi). We may assume ℓi < ℓi+1 for i ∈ {1, . . . , n − 1}. Since n > 1896k6 = 12k3 · 158k3, by
Theorem 1.3 the sequence R = (r1, . . . , rn) has a strictly decreasing subsequence of length 158k3 or a

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 26

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

strictly increasing subsequence of length 12k3.

Case 1: R has a strictly increasing subsequence of length 12k3.
Let B′
1, . . . , B′
12k3 be the blocks corresponding to the increasing subsequence of R. Let ℓ′
i = ℓ(B′
i) and
r′
i = r(B′
i). Thus we have ℓ′
i < ℓ′
i+1 and r′
i < r′
i+1 for i ∈ {1, . . . , 12k3 − 1}. We distinguish two cases.

Case 1.1: Sp(B′
i) ∩ Sp(B′
i+6k2) ̸= /0 for some i ∈ {1, . . . , 12k3 − 6k2}.
Let B = {B′
i, . . . , B′
i+6k2}. For j ∈ {i + 1, . . . , i + 6k2 − 1} we have ℓ′
j < ℓ′
i+6k2 < r′
i < r′
j, so r′
i ∈ Sp(B′
j).
In particular, r′
i is contained in Sp(B) for every B ∈ B. Let G′ be the graph we get by adding the edges
ℓ(B)r(B) for every B ∈ B to P1 ∪ P2. Note that G′ is the cycle P1 ∪ P2 together with 6k2 + 1 chords
which are pairwise crossing. It is easy to see that G′ has a cycle C′ which contains all edges of the form
ℓ(B)r(B) apart from possibly one. Let C be the cycle we get by replacing each edge ℓ(B)r(B) of C′ by an
ℓ(B) − r(B) path with interior vertices in B+. Let B3 ⊆ B be the subset of blocks which contain precisely
three vertices of degree 2. If |B3| ≥ k + 1, then by Theorem 4.3 the B3-necklace formed by the union of
C and the blocks in B3 is k-wiggly. Thus, we may assume |B3| ≤ k.
Let B′ = B \ B3. Note that |B′| ≥ 6k2 − k + 1. We have |NB(Θ+)| ≥ 3 for each B ∈ B′ so there exist
xB, yB, zB ∈ NB(Θ+) such that π(xB) = ℓ(B), π(yB) = r(B), and π(zB) /∈ {ℓ(B), r(B)}. Let B0 be the block
in B′ for which ℓ(B0) is closest to u on P1. The vertices ℓ(B0) and r(B0) split the cycle P1 ∪ P2 into
two paths Q1 and Q2, see Figure 12. We may assume that Q1 contains ℓ(B) and Q2 contains r(B) for
every B ∈ B′. One of these two paths, say Q1, contains at least 1
2 (|B′| − 1) vertices of the form π(zB)
with B ∈ B′ \ {B0}. Let Q′ be the graph we get from Q1 by adding the edges π(xB)π(zB) for every
B ∈ B′ \ {B0} with π(zB) ∈ V (Q1). Note that

1
2 (|B′| − 1) ≥ 3k2 − 1
2 k ≥ 8
3 k(k − 1) + 1 ,

so by Lemma 3.1 there exists a path P′ in Q′ containing at least k edges of the form π(xB)π(zB). For
each B ∈ B′, let PB be a π(xB) − π(zB) path which contains yB and whose interior vertices lie in B+. By
replacing each edge π(xB)π(zB) in P′ by PB, we obtain a path P which is k-close to Q2. Let P0 be an
ℓ(B0) − r(B0) path with interior vertices in B
+
0 . Now P and the cycle P0 ∪ Q2 are k-close.

Case 1.2: Sp(B′
i) ∩ Sp(B′
i+6k2) = /0 for all i ∈ {1, . . . , 12k3 − 6k2}.
For i ∈ {0, . . . , 2k − 1}, let B′′
i = B′
1+6ik2 and B = {B′′
0, . . . , B′′
2k−1}. Note that the Θ-spans of the blocks
in B are pairwise disjoint. Clearly G has a cycle C which goes through every block in B. Let B3 ⊆ B
be the subset of blocks which contain precisely three vertices of degree 2. If |B3| ≥ k, then by The-
orem 4.3 the B3-necklace formed by the union of C and the blocks in B3 is k-wiggly. Thus, we may
assume |B3| < k. Let B′ = B \ B3. Note that |B′| ≥ k. Let xB, yB, zB ∈ NB(Θ+) such that π(xB) = ℓ(B),
π(yB) = r(B), and π(zB) /∈ {ℓ(B), r(B)} for each B ∈ B′. Let PB be a π(xB) − π(yB) path which contains
zB and whose interior vertices lie in B+, and let wB be the neighbour of zB in Θ+. It is easy to see that
there exists a π(xB) − π(yB) path QB in Θ+ which contains wB. Finally let ΘB be the union of PB, QB,
and the edge wBzB. Now the union of P1 ∪P2 and all subgraphs ΘB with B ∈ B′ contains a θ (k, 1)-necklace.

Case 2: R has a strictly decreasing subsequence of length 158k3.
Note that if ℓi < ℓ j and r j < ri, then Sp(B j) ⊂ Sp(Bi). Thus, there exist 158k3 pairwise disjoint Θ-isolated

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 27

KASPER SZABO LYNGSIE AND MARTIN MERKER

Figure 12: Proof of Theorem 5.14 Case 1.1

2-connected endblocks B′
1, . . . , B′
158k3 such that Sp(B′
i) ⊂ Sp(B′
i+1) for i ∈ {1, . . . , 158k3 − 1}. Let Ci
denote the component of H containing B′
i and let C = (C1, . . . ,C158k3). The components in C are not nec-
essarily distinct. Note that 158k3 ≥ 156k3 + 6k2 for k ≥ 3, so the following expressions are well-deﬁned.
We distinguish three cases.

Case 2.1: NΘ(C+
i+6k2) ∩ Sp(B′
i) ̸= /0 for some i ∈ {1, . . . , 156k3}.
Let x ∈ NΘ(C+
i+6k2)∩Sp(B′
i) and let Bx be the block of Ci+6k2 with x ∈ NΘ(B+
x ). Let B = {B′
i, . . . , B′
i+6k2−1}\
{Bx}, ℓ = ℓ(B′
i+6k2), and r = r(B′
i+6k2). Let Pr be an r − x path with interior vertices in C+
i+6k2. Note that
Pr is disjoint from B for every B ∈ B. Let B3 ⊆ B be the set of blocks which contain three vertices of
degree 2. It is easy to see that there exists a cycle C in G which contains Pr and goes through every block
in B. If |B3| ≥ k, then the union of C and the blocks in B3 is a k-wiggly B3-necklace. So we may assume
|B3| < k.
Let B′ = B \ B3. Note that x ∈ ℓP1r, so we can deﬁne Q1 = ℓP1x and Q2 = xP1r. For every B ∈ B′ there
exists a vertex xB ∈ B such that π(xB) ∈ (Q1 ∪ Q2) \ {ℓ(B), r(B)}. We may assume that at least 1
2 |B′| of
the vertices π(xB) with B ∈ B′ are contained in Q1. For every B ∈ B′, let zB ∈ B such that π(zB) = r(B)
and let PB be a π(xB) − ℓ(B) path with interior vertices in B+ and containing zB. Let Q′ be the graph we
get from Q1 by adding the edges π(xB)ℓ(B) for every B ∈ B′ with π(xB) ∈ V (Q1), see Figure 13. The
number of edges added is at least 1
2 |B′| ≥ 1
2 (6k2 − k) ≥ 8
3 k(k − 1) + 1, so there exists a path P′ in Q′

containing at least k of these edges by Lemma 3.1. As in Case 1.1, we can modify P′ by replacing the
edges π(xB)ℓ(B) by the paths PB to obtain a path P in G. Now P and the cycle Q2 ∪ Pr are k-close.

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 28

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

Figure 13: Proof of Theorem 5.14 Case 2.1

Case 2.2: NΘ(C+
i ) \ Sp(B′
i+6k2) ̸= /0 for some i ∈ {1, . . . , 156k3}.
Let x ∈ NΘ(C+
i ) \ Sp(B′
i+6k2) and let Bx be the block of Ci with x ∈ NΘ(B+
x ). We may assume that
x is contained in the cycle P1 ∪ P2. Let Pr be an x − r(B′
i)-path with interior vertices in C+
i . Let
B = {B′
i+1, . . . , B′
i+6k2} \ {Bx} and B3 ⊆ B the set of blocks with three vertices of degree 2. The vertices
x and r(B′
i) split the cycle P1 ∪ P2 into two paths Q1 and Q2. We may assume that Q1 contains ℓ(B) and
Q2 contains r(B) for every B ∈ B. Now we proceed as in the previous case.
If |B3| ≥ k, then we can ﬁnd a k-wiggly B3-necklace. So we may assume |B3| < k. Let B′ = B \ B3. For
every B ∈ B′ there exists a vertex xB ∈ B such that π(xB) ∈ (Q1 ∪ Q2) \ {ℓ(B), r(B)}. We may assume that
at least 1
2 |B′| ≥ 8
3 k(k − 1) + 1 of the vertices π(xB) with B ∈ B′ are contained in Q1. For every B ∈ B′,
let zB ∈ B such that π(zB) = r(B). As before, there exists a path P which is disjoint from Q2 ∪ Pr and
contains at least k vertices zB. Now P and the cycle Q2 ∪ Pr are k-close.

Case 2.3: NΘ(C+
i ) ⊂ Sp(B′
i+6k2) and NΘ(C+
i+6k2) ∩ Sp(B′
i) = /0 for all i ∈ {1, . . . , 156k3}.
Note that NΘ(C+
i ) ⊂ Sp(B′
i+6k2) implies that every component in C is Θ-isolated. Let C′
i = C12ik2 for
i ∈ {1, . . . , 13k}, and C′ = (C′
1, . . . ,C′
13k). We show that C′ is a Θ-chain. For i, j ∈ {1, . . . , 156k3} with
j ≥ i + 12k2, we have NΘ(C+
i ) ⊂ Sp(B′
i+6k2) ⊆ Sp(B′
j−6k2) and NΘ(C+
j ) ∩ Sp(B′
j−6k2) = /0, which implies
Sp(Ci) ∩ NΘ(C+
j ) = /0. Thus, Ci and C j are not crossing, which implies that the components in C′ are
pairwise not crossing. Moreover, Sp(Ci) ⊆ Sp(B′
i+6k2) ⊂ Sp(B′
j) ⊆ Sp(C j) for i, j ∈ {1, . . . , 156k3} with
j ≥ i + 12k2. Thus, C′
i ≤Θ C′
i+1 for i ∈ {1, . . . , 13k} and C′ is a Θ-chain. By Theorem 5.5, we may assume

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 29

KASPER SZABO LYNGSIE AND MARTIN MERKER

that there are less than 8k components containing an endblock which is not 2-connected. Since C′ has
length 13k, it contains a subsequence of length 5k which is a special Θ-chain. Now G is k-good by
Lemma 5.13.

5.4 Few 2-connected endblocks in G − Θ+

Combining the results of Section 5.2 and Section 5.3, the only remaining case in the proof of Theorem 1.1
is when G − Θ+ does not contain many 2-connected endblocks. By Theorem 5.5 we can assume that
there are not many endblocks in G − Θ+. In this case we can ﬁnd a path and a cycle which are k-close.

Theorem 5.15. Let G be a cubic 3-connected graph and k a natural number. If the diameter of G is at
least 109k1329k2, then G is k-good.

Proof. Let f (k) = 109k1329k2 and let u, v ∈ V (G) such that u and v have distance at least f (k) in G. Let
Θ = (P1, P2, P3) be a shortest u, v-θ -graph in G and H = G − Θ+. We may assume k ≥ 3 since Θ is
2-good. By Lemma 5.3 (a) we can assume that there are less than 3
2 k edges in G − E(Θ) with both ends
in V (Θ). Thus, we have
 |E(Θ, G − Θ)| > 3( f (k) − 1) − 3k .

Let v0 and e0 denote the number of isolated vertices and isolated edges in G − Θ, respectively. By
Lemma 5.3 (c) and (d) we may assume v0 < 3k and e0 < 3k. Note that |E(Θ, F(Θ))| = 2|E(F(Θ), H)| +
3v0 + 4e0 < 2|E(F(Θ), H)| + 21k, and thus

|E(F(Θ), H)| > 1
2 (|E(Θ, F(Θ))| − 21k) .

Since |E(Θ, G − Θ)| = |E(Θ, H)| + |E(Θ, F(Θ))|, this implies

|E(Θ
+, H)| = |E(Θ, H)| + |E(F(Θ), H)|

> |E(Θ, H)| + 1
2 (|E(Θ, F(Θ))| − 21k)

≥ 1
2 (|E(Θ, G − Θ)| − 21k)

> 3
2 ( f (k) − 1) − 12k .

Let S = NH(Θ+) and let s1 denote the number of vertices of degree at most 1 in H. Each vertex in S has
degree at most 1 in H or it is incident with exactly one edge in E(Θ+, H), so |S| ≥ |E(Θ+, H)| − 2s1. By
Theorem 5.5 we may assume s1 < 8k. Thus,

|S| ≥ |E(Θ+, H)| − 16k > 3
2 f (k) − 29k > f (k) .

By Theorem 5.8 and Theorem 5.14, we may assume that the number of 2-connected endblocks in H is
less than 21k2 + 3
2 k + 5700k6. By Theorem 5.5 we can assume that there are less than 8k endblocks in

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 30

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

H which are not 2-connected. In total, H has less than 104k6 endblocks and in particular also less than
104k6 components. Let K be a component of H for which |K ∩ S| is maximal. Since |S| > f (k), we have

|K ∩ S| > |S|
104k6 > f (k)
104k6 = 29k210
5k7 > 3 · 29k210
4k7 . (5.1)

Let B be the set of blocks of K which contain a vertex in S. Since we can 2-colour the blocks of K
such that any two blocks of the same colour are disjoint, there exists a subset of pairwise disjoint blocks
B′ ⊆ B with |B′| ≥ 1
2 |B|.
Suppose there exists a block B in H containing at least 29k2 vertices of S. By Theorem 3.2, there exists a
path P in B containing at least 3
2 k vertices in S. Now P is k-close to one of the cycles P1 ∪ P2, P1 ∪ P3, or
P2 ∪ P3. Thus we may assume that each block contains less than 29k2 vertices of S. Together with (5.1)
this implies |B| ≥ 3 · 104k7.
Let P be a minimal collection of paths in K such that at least one edge of each block in B′ is contained
in some path of P. It is easy to see that P contains at most as many paths as K has endblocks, thus
|P| < 104k6. Thus, there exists a path P ∈ P such that P contains edges of at least

|B′|
|P| >
 1
2 · 3 · 104k7

104k6 = 3
2 k

different blocks in B′. We can modify P so that it contains a vertex of S in each of these blocks. Now P is
k-close to one of the cycles P1 ∪ P2, P1 ∪ P3, or P2 ∪ P3.

The following corollary is an immediate application of Theorem 5.15 which concludes the proof of
Theorem 1.1.

Corollary 5.16. Let G be a cubic 3-connected graph and m, k natural numbers with k odd, and f (k) =
2106k16. If |V (G)| ≥ 3 · 2 f (k) then G contains a cycle whose length is congruent to m modulo k.

Proof. We may assume k ≥ 3. The diameter of G is at least f (k). Note that 16213 < 1029. By Bernoulli’s
inequality we have

2 1
2 106k16 = (
2 1
2 105k16)10 > ( 1
2 10
5k16)10 > 10
46k160 > 10
9(162k8)
13 .

Since 1
2 106 > 9 · (162)2, we have

f (k) = 2 1
2 106k16 · 2 1
2 106k16 > 10
9(162k8)
132
9(162k8)2 .

Thus, G is (162k8)-good by Theorem 5.15. By Theorem 2.9, G has a cycle whose length is congruent to
m modulo k.
 ADVANCES IN COMBINATORICS, 2021:3, 36pp. 31

KASPER SZABO LYNGSIE AND MARTIN MERKER

6 Counterexamples for 2-connected cubic graphs

In some cases weaker conditions sufﬁce to show that a graph contains a cycle whose length is congruent
to m modulo k. This is in particular true for small values of k. For example, Chen and Saito [4] proved
that every graph of minimum degree 3 contains a cycle whose length is divisible by 3. However, in this
section we construct families of graphs which show that in general Theorem 1.1 cannot be extended to
2-connected cubic graphs. The graphs we construct consist of two disjoint copies of a small graph that
are joined by a so-called cross-ladder which is deﬁned as follows.

Deﬁnition 6.1 (Cross-ladder). Let N ≥ 1 be a natural number. A cross-ladder of length 3N is a graph
consisting of a path P = u0u1 . . . u3N−1u3Nv3Nv3N−1 . . . v1v0 and edges u3iv3i, u3i+1v3i+2, u3i+2v3i+1 for
every i ∈ {0, . . . , N − 1}.

Note that every cross-ladder is a 2-connected subcubic graph. Each cross-ladder contains precisely
four vertices of degree 2 (u0, v0, u3N, and v3N) and they induce a matching in the cross-ladder. We now
deﬁne an operation that allows us to connect two disjoint graphs using a cross-ladder.

Deﬁnition 6.2 (G1 ⊗N G2). Let N ≥ 1 be a natural number, G1 and G2 2-connected graphs with xi, yi ∈
V (Gi) such that d(xi) = d(yi) = 2 and d(v) = 3 for i ∈ {1, 2} and v ∈ V (Gi) \ {xi, yi}. Let L be a cross-
ladder of length 3N and u0, v0, u3N, v3N ∈ V (L) distinct vertices of degree 2 such that u0v0, u3Nv3N ∈ E(L).
We deﬁne G1 ⊗N G2 as the graph we obtain from the disjoint union of G1, G2, and L by adding the edges
x1u0, y1v0, x2u3N, and y2v3N.

It is easy to see that G1 ⊗N G2 is a cubic 2-connected graph, see Figure 14. Moreover, if G1 + x1y1
and G2 + x2y2 are planar, then also G1 ⊗N G2 is planar. The following lemma shows that under some
mild assumption on G we can control the cycle lengths which are divisible by 3 in G ⊗N G.

Lemma 6.3. Let N ≥ 1 be a natural number and G a 2-connected graph with x, y ∈ V (G) such that
d(x) = d(y) = 2 and d(v) = 3 for v ∈ V (G) \ {x, y}. Suppose that G contains no x − y path whose length
is divisible by 3. Let G′ = G ⊗N G and let G1 and G2 denote the two disjoint copies of G in G′. If C
is a cycle in G′ whose length is divisible by 3, then either C is a cycle in G1 or G2, or C has length
6N + 4 + p1 + p2 where p1 and p2 are lengths of x − y paths in G.

Figure 14: G1 ⊗N G2

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 32

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

Proof. Let x1, y1 ∈ V (G1) and x2, y2 ∈ V (G2) denote the vertices corresponding to x and y in G. Let H
be the subgraph of G′ which is induced by the copy of the cross-ladder of length 3N and the vertices
x1, y1, x2, and y2. Note that H contains no cycles of length divisible by 3, so we can assume C contains a
vertex in at least one of G1 and G2, say G1. We may assume C is not a cycle in G1, so it contains both x1
and y1. Note that the length of every x1 − y1 path in H is congruent to 0 modulo 3. If C is contained in
G1 ∪ H, then
 |E(C)| = |E(C) ∩ E(G1)| + |E(C) ∩ E(H)| ≡ |E(C) ∩ E(G1)| ̸≡ 0 mod 3 ,

since |E(C) ∩ E(G1)| is the length of an x − y path in G. Thus we can assume that C also contains
vertices in G2. Now it is easy to see that |E(C) ∩ E(H)| = 6N + 4. Let p1 = |E(C) ∩ E(G1)| and
p2 = |E(C) ∩ E(G2)|. It follows that |E(C)| = 6N + 4 + p1 + p2.

Note that in Lemma 6.3, both p1 and p2 are lengths of x − y paths in G and thus not divisible by 3.
Since |E(C)| is divisible by 3, we have p1 + p2 ≡ 2 modulo 3 and both p1 and p2 are congruent to 1
modulo 3.
(a) H1 (b) H2 (c) H3

Figure 15: Three different building blocks used in the proof of Theorem 6.4

Theorem 6.4. Let m, k, and N be natural numbers with k ≥ 12. If m and k are divisible by 3, then there
exists a 2-connected cubic graph G with at least N vertices such that no cycle of G has length congruent
to m modulo k.

Proof. We may assume m ∈ {0, . . . , k − 1}. We deﬁne a number N′ and a graph G depending on k, m,
and N as follows.

• If m /∈ {3, 9}, let N′ ≥ N be a natural number such that 6N′ + 12 ̸≡ m mod k and let G = H1 be
the graph in Figure 15(a).

• If m = 9, let N′ ≥ N be a natural number such that N′ ≡ 1 (mod k) and let G = H2 be the graph in
Figure 15(b).
 ADVANCES IN COMBINATORICS, 2021:3, 36pp. 33

KASPER SZABO LYNGSIE AND MARTIN MERKER

• If m = 3, let N′ ≥ N be a natural number such that N′ ≡ −1 (mod k) and let G = H3 be the Petersen
Graph with one edge removed, see Figure 15(c).

Let x and y denote the two vertices of degree 2 in G. Note that in each case there is no x − y path in G
whose length is divisible by 3. Let G′ = G ⊗N′ G and let G1, G2 denote the two copies of G in G′. Let C
be a cycle in G′ whose length is divisible by 3. We distinguish between the three cases above.

Case 1: m /∈ {3, 9}.
The only cycles of length divisible by 3 in H1 have length 3 or 9. Thus, if C is contained in G1 or
G2, then C has length 3 or 9. By Lemma 6.3, we may assume that |E(C)| = 6N′ + 4 + p1 + p2 where
p1, p2 ∈ {4, 5}. Since |E(C)| is divisible by 3, it follows that |E(C)| = 6N′ + 12, so the length of C is not
congruent to m modulo k by the choice of N′.

Case 2: m = 9.
If C is contained in G1 or G2, then C has length 3 or 6. By Lemma 6.3, we may assume that
|E(C)| = 6N′ + 4 + p1 + p2 where p1, p2 ∈ {1, 4, 5}. Since |E(C)| is divisible by 3, we have |E(C)| ∈
{6N′ + 6, 6N′ + 9, 6N′ + 12}. Thus |E(C)| is congruent to 12, 15, or 18 modulo k. Since k ≥ 12, the
length of C is not congruent to 9 modulo k.

Case 3: m = 3.
Since H3 has no cycle whose length is congruent to 3 modulo k, we can assume by Lemma 6.3 that
|E(C)| = 6N′ + 4 + p1 + p2 where p1, p2 ∈ {4, 5, 7, 8}. Thus |E(C)| ∈ {6N′ + 12, 6N′ + 15, 6N′ + 18}
and |E(C)| is congruent to 6, 9, or 12 modulo k. Since k ≥ 12, the length of C is not congruent to 3
modulo k.

We conclude this paper with the following open problem.

Question. For which natural numbers m and k does every sufﬁciently large 2-connected cubic graph
contain a cycle whose length is congruent to m modulo k?

References

[1] B. BOLLOBÁS, Cycles modulo k, Bull. London Math. Soc. 9 (1977), 97-98. 1

[2] J.A. BONDY, A. VINCE, Cycles in a Graph Whose Lengths Differ by One or Two, J. Graph Theory
27 (1998), 11-15. 2

[3] X. CAI, W. SHREVE, Pancyclicity mod k of claw-free graphs and K1,4-free graphs, Discrete
Mathematics 230 (2001), 113-118. 2

[4] G.T. CHEN, A. SAITO, Graphs with a Cycle of Length Divisible by Three, J. Combin. Theory Ser.
B 60 (1994), 277-292. 1, 32

[5] F. CHUNG, Open problems of Paul Erd˝os in graph theory, J. Graph Theory 25 (1997), 3-36. 1

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 34

CYCLE LENGTHS MODULO k IN LARGE 3-CONNECTED CUBIC GRAPHS

[6] N. DEAN, L. LESNIAK, A. SAITO, Cycles of length 0 modulo 4 in graphs, Discrete Mathematics
121 (1993), 37-49. 1

[7] A.A. DIWAN, Cycles of even lengths modulo k, J. Graph Theory 65 (2010), 246-252. 2

[8] P. ERD ˝OS, Some recent problems and results in graph theory, combinatorics, and number theory,
Proceedings of Seventh S-E Conference on Combinatorics, Graph Theory and Computing, Utilitas
Mathematica, Winnipeg (1976), 3–14. 1

[9] P. ERD ˝OS, G. SZEKERES, A combinatorial problem in geometry, Compositio Mathematica 2 (1935),
463-470. 4

[10] G. FAN, Distribution of Cycle Lengths in Graphs, J. Combin. Theory Ser. B 82 (2002), 187-202. 2,
3, 11

[11] R. LANG, H. WALTHER, Über Längste Kreise in regulären Graphen, Beiträge zur Graphentheorie,
Kolloquium, Manebach 1967, Teubner, Leipzig (1968), 91-98. 11

[12] C.H. LIU, J. MA, Cycle lengths and minimum degree of graphs, J. Combin. Theory, Ser. B 128
(2018), 66-95. 2

[13] J. MA, Cycles with consecutive odd lengths, European J. Combin 52 (2016), 74-78. 2

[14] L. MEI, Y. ZHENGGUANG, Cycles of length 1 modulo 3 in graph, Discrete Applied Mathematics
113 (2001), 329-336. 1

[15] A. SAITO, Cycles of length 2 modulo 3 in graphs, Discrete Mathematics 101 (1992), 285-289. 1

[16] B. SUDAKOV, J. VERSTRAËTE, Cycle lengths in sparse graphs, Combinatorica 28 (2008), 357-372.
2

[17] B. SUDAKOV, J. VERSTRAËTE, The extremal function for cycles of length ℓ mod k, Electronic J.
Combin. 24 (2017), #P1.7. 2

[18] C. THOMASSEN, Girth in graphs, J. Combin. Theory Ser. B 35 (1983), 129-141. 2

[19] C. THOMASSEN, Graph Decomposition with Applications to Subdivisions and Path Systems Modulo
k, J. Graph Theory 7 (1983), 261-271. 2

[20] W.T. TUTTE, How to draw a graph, Proc. London Math. Soc. 13 (1989), 175-188. 5

[21] J. VERSTRAËTE, On Arithmetic Progressions of Cycle Lengths in Graphs, Combinatorics, Probabil-
ity and Computing 9 (2000), 369-373. 2

[22] J. VERSTRAËTE, Unavoidable cycle lengths in graphs, J. Graph Theory 49 (2005), 151-167. 1

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 35

KASPER SZABO LYNGSIE AND MARTIN MERKER

AUTHORS

Kasper Szabo Lyngsie
Department of Applied Mathematics and Computer Science
Technical University of Denmark
Lyngby, Denmark
kasperszabo hotmail com

Martin Merker
Department of Applied Mathematics and Computer Science
Technical University of Denmark
Lyngby, Denmark
merkermartin gmail com

ADVANCES IN COMBINATORICS, 2021:3, 36pp. 36
