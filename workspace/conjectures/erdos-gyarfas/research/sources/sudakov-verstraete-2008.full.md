<!-- source: https://arxiv.org/pdf/0707.2117 | converted from PDF -->

arXiv:0707.2117v1  [math.CO]  14 Jul 2007
Cycle lengths in sparse graphs

Benny Sudakov ∗ Jacques Verstra¨ete †

Abstract

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
also Erd˝os [10]) that every graph of minimum degree at least three contains a cycle of length
a power of two, we prove a general theorem which gives an upper bound on the average degree
of an n-vertex graph with no cycle of even length in a prescribed inﬁnite sequence of integers.
For many sequences, including the powers of two, our theorem gives the upper bound eO(log∗n)

on the average degree of graph of order n with no cycle of length in the sequence, where log∗n
is the number of times the binary logarithm must be applied to n to get a number which is at
most one.

1 Introduction

For a graph G, let C(G) denote the set of integers whose elements are lengths of cycles in G.
The study of cycles in graphs has long been fundamental, and many questions about properties
of graphs that guarantee some particular range of cycle length have been considered. The central
goal in this paper is to obtain lower bound on |C(G)| when G is a graph of average degree d and
girth g, or G is an H-free graph, and to determine which integers are guaranteed to appear in
C(G) under density conditions on G.

In the case of dense graphs, there are many results which determine when C(G) is an interval,
or almost an interval. One of the ﬁrst results in this direction was obtained by Bondy [5], who

∗Department of Mathematics, Princeton University, Princeton, NJ 08544, and Institute for Advanced Study,
Princeton. E-mail: bsudakov@math.princeton.edu. Research supported in part by NSF CAREER award DMS-
0546523, NSF grant DMS-0355497, USA-Israeli BSF grant, Alfred P. Sloan fellowship, and the State of New Jersey.
†Department of Combinatorics and Optimization, University of Waterloo, Waterloo, ON N2L 3G1, Canada.
E-mail: jverstra@math.uwaterloo.ca
 1

proved that for every n-vertex graph G of minimum degree larger than n
2 , C(G) = {3, 4, , . . . , n}.
Once the minimum degree of a graph is allowed to pass below n
2 , we can no longer guarantee
any odd cycles, as the graph may be bipartite. Also, one cannot guarantee a hamiltonian cycle,
(equivalently, n ∈ C(G)). In this situation, the natural question is to ask when C(G) contains
all even integers up to 2ℓ, where 2ℓ is the length of a longest even cycle of G. Bollob´as and
Thomason [4] showed that this is the case if G has order n and size at least ⌊ n2
4 ⌋ − n + 59. The
best result on this problem is by Gould, Haxell, and Scott [13], who proved that if an n-vertex
graph G has minimum degree at least cn, where c > 0 is a constant, then C(G) contains all
even integers up to 2ℓ − K for some constant K depending only on c. It is conjectured that for
some constant c > 0, every hamiltonian n by n bipartite graph of minimum degree at least c
√n
contains cycles of all even lengths in {4, 6, 8, . . . , 2n}. All of the above mentioned results are for
dense graphs – graphs whose average degree is linear in the order of the graph. In this paper, we
are interested in studying C(G) for sparse graphs.

Since n-vertex graphs of average degree d may have girth at least logd−1 n, it is clear that for
sparse graphs one cannot hope to state that C(G) contains any integer from a ﬁnite set. Erd˝os
and Hajnal [9] conjectured ∑

ℓ∈C(G)
 1
ℓ = Ω(log d)

whenever G has average degree d. (Here and throughout the paper the notation ad = Ω(bd)
means that there is an absolute constant C such that ad ≥ Cbd when d → ∞.) This conjecture
was proved by Gy´arf´as, Koml´os and Szemer´edi [15]. Their result shows that if a graph does not
have too many short cycles, then it must have many long cycles. However, it appears to be very
diﬃcult to pass from such statement to statements about the size or arithmetic structure of C(G).

1.1 Cycles in graphs of large girth

The ﬁrst problem we study is to determine the size of C(G) for graphs of given average degree
and girth (the girth of G is the length of the shortest cycle in G). The length of a longest cycle
in a graph of girth g was ﬁrst studied by Ore [21]. For graphs of girth at most four and average
degree d, it is straightforward to prove that the longest cycle has length at least d + 1 if the girth
is three, and at least 2d if the girth is four, and the proofs of these facts show |C(G)| ≥ d − 1,
with equality for Kd+1 and Kd,d. Erd˝os [8] conjectured that |C(G)| = Ω(d⌊(g−1)/2⌋) whenever G
has average degree d and girth g. This was proved for g = 5 by Erd˝os, Faudree, Rousseau and
Schelp [11]. They also show that |C(G)| = Ω(d5/2) for g = 7, |C(G)| ≥ Ω(d3) for g = 9 and
|C(G)| = Ω(dg/8) in general. For comparison, Erd˝os’ conjecture is |C(G)| = Ω(d3) for g = 7 and
|C(G)| = Ω(d4) for g = 9. In Section 2, we will give a short proof of Erd˝os’ conjecture. In fact,
we obtain the following stronger theorem.

Theorem 1.1 Let G be a graph of average degree d and girth g. Then C(G) contains Ω(
d⌊(g−1)/2⌋)

consecutive even integers.

The study of the length of a longest cycle in graphs of girth g and average or minimum degree d
was initiated by Ore [21] in 1967 and attracted attention of a number of researchers [7, 11, 24, 25]

2

since then. Our lower bound on |C(G)| improves all of these results, and it best possible up to
constant factors: to see why Theorem 1.1 cannot be improved, recall that the Moore Bound for
a graph G of minimum degree d and girth g states

|V (G)| ≥
 { 1 + d + d(d − 1) + · · · + d(d − 1)
⌊ g−1
2 ⌋−1 if g is odd

2
(1 + (d − 1) + (d − 1)2 + · · · + (d − 1)
⌊ g−1
2 ⌋) if g is even

Up to the constant factor, it is known that this bound is tight for inﬁnitely many values of d
whenever g ≤ 8 or g = 12 and it is also believed that for all other values of g there are graph with
girth g and order O(d⌊(g−1)/2⌋). So it is evident that |C(G)| = O(
d⌊(g−1)/2⌋) for such graphs. A
related problem is to determine the number of odd integers in C(G) when G has large chromatic
number and girth. For example, Gy´arf´as [14] proved that a graph of chromatic number at least
2d + 1 contains cycles of d distinct odd lengths, and equality holds only for graphs all of whose
blocks are complete graphs. Using similar techniques as in the proof of Theorem 1.1 we can
generalize the result of Gy´arf´as as follows: if G is a graph of chromatic number d and girth g,
then C(G) contains Ω(
d⌊(g−1)/2⌋) consecutive integers.

1.2 Cycles in H-free graphs

A graph is H-free if it contains no subgraph isomorphic to H. We consider the following gener-
alization of Theorem 1.1 in Section 3. Given a bipartite graph H, determine a lower bound for
|C(G)| when G is an H-free graph of average degree d. Speciﬁcally, we consider r-half-bounded
bipartite graphs. A bipartite graph is r-half-bounded if the degrees of all the vertices in one color
class are at most r. An example of such graph is a complete bipartite graph Kr,s with parts of
size r ≤ s. Using recent estimates on Tur´an numbers for r-half-bounded graphs due to Alon,
Krivelevich and Sudakov [1], we prove the following result.

Theorem 1.2 Let H be a ﬁxed bipartite graph containing a cycle and let G be an H-free graph
of average degree d. Then there exists a constant t > 1 depending on H such that C(G) contains
Ω(
dt/(t−1)) consecutive even integers. Furthermore, we can take t = r if H is r-half-bounded, and
t = 1 + 1
k−1 if H is a 2k-cycle.

Notice that when H is a 2k-cycle, this result generalizes our Theorem 1.1 from graphs of girth
2k + 1 or 2k + 2 to graphs with no 2k-cycle. The estimate for r-half-bounded graphs in Theorem
1.2 is tight for every value of r ≥ 2. Indeed, by the construction of projective norm graphs in [2]
(modifying that in [16]) for every ﬁxed s ≥ (r − 1)! + 1 there are graphs of order O(
dr/(r−1)) and
average degree d which do not contain copy of Kr,s.

1.3 Arithmetic structure of C(G)

In the second part of the paper, we discuss the arithmetic structure of C(G) for sparse graphs.
The type of question we would like to answer is: what is the smallest d such that every graph
of average degree at least d has a cycle of length equal to a square, or a power of two, or twice
a prime? Our main theorem is motivated by the conjecture of Erd˝os and Gy´arf´as [9], stating

3

that every graph of minimum degree at least three contains a cycle of length a power of two, and
by the questions posed by Erd˝os (see page 228 of [10]). Throughout this section, for a sequence
(σ(i))i≥1 of integers, a σ-cycle is a cycle of length σ(i) for some i ≥ 1. We write π < σ to denote
that π is a subsequence of σ.

Perhaps the most natural starting point is to determine when C(G) contains an integer congruent
to zero modulo a given integer k. The ﬁrst result in this direction was proved by Bollob´as [3],
who showed that if G has average degree at least 2
k (k + 1)k, then G contains a cycle of length zero
modulo k. The main result in [23] (see also Fan [12]) shows that if σ is any inﬁnite increasing
sequence of even integers such that |σ(j) − σ(j − 1)| ≤ k for all j ≥ 2, then every graph of average
degree at least 4k contains a σ-cycle. In this section, we are interested in extending this result
to the case that |σ(j) − σ(j − 1)| is not bounded. The theorem below gives an upper bound on
the average degree of a graph containing no σ-cycles. In this theorem, all logarithms are natural
logarithms.

Theorem 1.3 For any inﬁnite increasing sequence σ of positive even integers and for any n-
vertex graph G, if G contains no σ-cycle, then G has average degree at most

inf
π<σ
r≥1 exp
 (
6r +
 r∑

i=1
 2 log ∆(i)
π(i − 1) + 2 log n
π(r)
 )
 ,

where π(0) := 1, ∆(1) := π(1), and ∆(i) = max{σ(j) − σ(j − 1) : σ(j) ≤ π(i)} for i ≥ 2.

To illustrate this statement consider the case when σ(i) = 2i for i ≥ 1. Then we can take π to be
the sequence of towers of twos, namely
π(1) = 2 π(2) = 2
2 π(3) = 2
22 · · ·

so that π(i) = 2π(i−1), and take r = log*n, where log*n = i whenever π(i − 1) < n ≤ π(i).
Then Theorem 1.3 implies that every graph of order n with no cycle of length a power of two
has average degree exp(O(log∗ n)). In fact, the same bound holds for many sequences, such as
twice primes, squares, and the tower sequence π deﬁned above. We say that a sequence σ is
exponentially bounded if there is an absolute constant C > 1 such that σ(i) ≤ Cσ(i − 1) for all
i ≥ 2.

Corollary 1.4 Let σ denote an inﬁnite increasing exponentially bounded sequence of positive even
integers. Then any n-vertex graph with no σ-cycles has average degree exp(O(log*n)).

This corollary will be proved in Section 4. Also in Section 4, we will construct sequences σ and
n-vertex graphs with no σ-cycles whose average degrees have the same order of magnitude as the
upper bound in Theorem 1.3, up to absolute constant factors in the exponent. However, these
sequences are not exponentially bounded. It would be interesting to see if there are graphs with
arbitrarily large average degree containing no σ-cycles, for some exponentially bounded sequence
σ of positive even integers.
 4

2 Cycles in graphs of large girth

The (open) neighborhood of X ⊂ V (G) in a graph G is deﬁned by

∂X = {y ∈ V (G)\X | ∃x ∈ X : {x, y} ∈ E(G)}.

In words, this is the set of vertices not in X and adjacent to at least one vertex of X. The d-core
of a graph G, when it exists, is the subgraph obtained by repeatedly deleting vertices of degree
at most d − 1. It is a well-known fact that if a graph has integer average degree 2d, then it has
a d-core. It is convenient to assume throughout that d is an integer. Our ﬁrst lemma states that
graphs of large average degree and girth expand on small sets.

Lemma 2.1 Let G be a graph of girth g and minimum degree at least 6(d + 1). Then, for every
X ⊂ V (G) of size at most 1
3 d⌊(g−1)/2⌋,
 |∂X| > 2|X|.

Proof. Suppose |∂X| ≤ 2|X| for some X ⊂ V (G). Let H be the subgraph of G spanned by the
set Y = X ∪ ∂X. Then |Y | ≤ 3|X| and

e(H) ≥ 1
2
 ∑

x∈X d(x) ≥ 3(d + 1)|X| ≥ (d + 1)|Y |.

Thus H contains a subgraph Γ with minimum degree d + 1. Applying the Moore Bound to Γ, we
obtain: 3|X| ≥ |Y | ≥ |V (Γ)| ≥ 1 + (d + 1) ∑

i<⌊(g−1)/2⌋ d
i > d
⌊(g−1)/2⌋

and therefore |X| > 1
3 d⌊(g−1)/2⌋, as required.

Using Lemma 2.1, we prove the conjecture of Erd˝os stating |C(G)| = Ω(d⌊(g−1)/2⌋) when G has
girth g and average degree d. A key ingredient of the proof is a lemma of P´osa [22] (see also [18],
Exercise 10.20) which says that if G is a graph and |∂X| > 2|X| for every X ⊂ V (G) of size at
most m, then G contains a path of length 3m.

Theorem 2.2 For any graph G of girth g and average degree 48(d + 1), |C(G)| ≥ 1
8 d⌊(g−1)/2⌋.

Proof. Let H be a maximum bipartite subgraph of G, containing at least half of the edges of
G. Then some connected component F of H has average degree at least 24(d + 1). Let T be a
breadth ﬁrst search tree in F , and let Li denote the set of vertices of T at distance i from the
root of T . Since F is bipartite, no edge of F joins two vertices of Li. Denote by e(Li, Li+1) the
number of edges of F with one endpoint in Li and one endpoint in Li+1. Then
∑

i e(Li, Li+1) = e(F ) ≥ 12(d + 1)|V (F )| = 12(d + 1) ∑

i |Li|

= 6(d + 1) ∑

i
 (|Li| + |Li+1|
).

5

Thus, there is an index i such that the subgraph Fi ⊂ F induced by Li ∪ Li+1 has average degree
at least 12(d + 1). Then Fi contains a subgraph Γ with minimum degree 6(d + 1). By Lemma 2.1
we have that |∂X| > 2|X| for every X ⊂ V (Γ) of size at most 1
3 d⌊(g−1)/2⌋. Hence Γ contains a
path P of length d⌊(g−1)/2⌋ by P´osa’s Lemma. Let T ′ be a minimal subtree of T whose set of end
vertices is exactly V (P ) ∩ Li. The minimality of T ′ ensures that it branches at the root. Let A
be the set of vertices in V (P ) ∩ Li in one of these branches and let B = (V (P ) ∩ Li) \ A. Then
both A, B are nonempty and all paths from A to B through the root of T ′ have the same length,
say 2h. We may assume that |B| ≥ |A| and |B| ≥ 1
4 |P |. Let a be an arbitrary vertex in A. Then
there are at least 1
2 |B| ≥ 1
8 |P | vertices of B on the same side of path from a. Hence there are
subpaths of P from a to a vertex of B of at least 1
8 |P | diﬀerent lengths. For any such path Q,
there is a unique subpath R of T ′ through the root joining the endpoints of Q, so that Q ∪ R is a
cycle in G. Since all R have the same length 2h, we obtain 1
8 d⌊(g−1)/2⌋ cycles of diﬀerent lengths,
and |C(G)| ≥ 1
8 d⌊(g−1)/2⌋.

2.1 Proof of Theorem 1.1

To obtain Theorem 1.1, we will slightly modify the proof of Theorem 2.2. A θ-graph is a graph
consisting of three internally disjoint paths between two vertices. We observe the following lemma
as a corollary of the proof of Theorem 2.2:

Lemma 2.3 Let G be a graph of average degree 48(d + 1) and girth g, where d⌊(g−1)/2⌋ ≥ 6. Then
G contains a θ-graph containing a cycle of length at least d⌊(g−1)/2⌋ + 2.

Proof. Let the path P , tree T ′ and set Li be deﬁned as in the proof of Theorem 2.2. Since
d⌊(g−1)/2⌋ ≥ 6, we have |V (P ) ∩ Li| ≥ 3. Let Q ⊂ P be a path of length at least |E(P )| − 2 with
endpoints in Li. Then also |V (Q) ∩ Li| ≥ 3 and therefore Q has an interior vertex in Li. If R is
a path in T ′ joining the endpoints of Q, then Q ∪ R is a cycle of length at least d⌊(g−1)/2⌋ + 2.
Finally, for some path S ⊂ T ′ from the root of T ′ to an interior vertex of Q in Li, the subgraph
Q ∪ R ∪ S is the required θ-graph.

It is convenient to deﬁne an AB-path in a graph G to be a path with one endpoint in A and one
endpoint in B, where A, B ⊂ V (G). The following result of Bondy and Simonovits [6] (see also
[23]) will be used to prove Theorem 1.1.

Lemma 2.4 Let Γ be a θ-graph and let (A, B) be a nontrivial partition of V (Γ). Then Γ contains
AB-paths of all lengths less than |V (Γ)| unless Γ is bipartite with bipartition (A, B).

Proof of Theorem 1.1. Let G be a graph of average degree 192(d + 1) and girth g and let H be
a maximum bipartite subgraph of G. Then some connected component F of H has average degree
at least 96(d + 1). Let T be a breadth-ﬁrst search tree in F , and let Li denote the set of vertices
of T at distance i from the root. Then, for some i, the subgraph Fi of F induced by Li ∪ Li+1
has average degree at least 48(d + 1). By Lemma 2.3, Fi contains a θ-graph Γ containing a cycle
of length at least d⌊(g−1)/2⌋ + 2. Let T ′ be the minimal subtree of T whose set of end vertices
is V (Γ) ∩ Li. Then there is a partition (A, B∗) of V (Γ) ∩ Li such that all AB∗-paths in T ′ go

6

through the root and have the same length, say 2h. Let B = V (Γ)\A. By Lemma 2.4, there exist
AB-paths in Γ of all even lengths in {1, 2, . . . , d⌊(g−1)/2⌋ + 2}. Since they have an even length,
each such path is actually an AB∗-path, and the union of this path with the unique subpath of
T ′ of length 2h joining its endpoints is a cycle. Therefore C(G) contains d⌊(g−1)/2⌋ consecutive
even integers, as required.

2.2 Chromatic number and cycle lengths

Using the above methods, we prove that in a graph G of large chromatic number and girth, C(G)
contains long interval of consecutive integers. We only sketch the details, as they resemble the
proof of Theorem 1.1. First we require two simple lemmas.

Lemma 2.5 Let H be a minimal d-chromatic graph, where d ≥ 3. Then for any distinct vertices
u, v ∈ V (H), there is a uv-path of odd length in H and a uv-path of even length in H.

Proof. Since H is minimal d-chromatic, and d ≥ 3, H has no cut-vertex. Fix u, v ∈ V (H), and
an odd cycle C ⊂ H. By Menger’s Theorem, there exist two vertex-disjoint paths P, Q starting
at u, v and ending at vertices w, x ∈ V (C), respectively. Since C is an odd cycle, C = R ∪ S
where R and S are internally disjoint wx-paths whose lengths have diﬀerent parity. It follows
that P ∪ Q ∪ R and P ∪ Q ∪ S are uv-paths whose lengths have diﬀerent parity.

A θ-graph is odd if it is non-bipartite.

Lemma 2.6 Let H be a minimal d-chromatic graph, where d ≥ 3. Then for any even cycle
C ⊂ H, there is an odd θ-graph in H containing C.

Proof. For u, v ∈ V (C), let d(u, v) be the distance from u to v on C. By Lemma 2.5, for any
u, v ∈ V (C) we can ﬁnd a path P such that |E(P )| ̸= d(u, v) (mod 2). Let P = (u0, u1, . . . , ur)
be the shortest path with u0, ur ∈ V (C) and |E(P )| ̸= d(u0, ur) (mod 2). Let Q ⊂ P be the path
(u0, u1, . . . , us) with us ∈ V (C) and ui ̸∈ V (C) for i < s. If |E(Q)| = d(u0, us) (mod 2), then
R = P − {ui : i < s} is a usur-path with |E(R)| ̸= d(us−1, ur) (mod 2), contradicting the choice
of P . So |E(Q)| ̸= d(u0, us) (mod 2), and C ∪ Q is an odd θ-graph.

We now prove our main result concerning the number of odd cycle lengths for graphs of large
chromatic number and girth:

Theorem 2.7 Let G be a graph of chromatic number d and girth g. Then C(G) contains
Ω(
d⌊(g−1)/2⌋) consecutive integers.

Proof. Take a breadth ﬁrst search tree T in a component of G of chromatic number d, and let
Li denote the set of vertices at distance i from the root of T . Then, for some i, the subgraph F
spanned by Li has chromatic number at least 1
2 d. Let H be a minimal 1
2 d-chromatic subgraph of
G[Li]. By Lemma 2.3, assuming d is large, H contains a θ-graph containing a cycle C of length
Ω(
d⌊(g−1)/2⌋). By Lemma 2.6, we can ensure that this θ-graph is an odd θ-graph containing C,

7

which we denote by Γ. If T ′ is a minimal subtree of T whose set of end vertices is V (Γ), then T ′

branches at the root of T ′, and this gives a partition (A, B) of V (Γ) as in the proof of Theorem
1.1. By Lemma 2.4, there are AB-paths of all lengths less than |V (Γ)|, and these paths together
with subpaths of T ′ give the required cycle lengths.

3 Cycles in H-free graphs

To prove Theorems 1.2 and 1.3, we will use the following lemma, which summarizes the ideas of
Section 2. Recall that a property of graphs is monotone if it is closed under taking subgraphs.
The radius of graph G is the smallest integer r for which there is a vertex v in G such that the
distance from any other vertex of G to v is at most r.

Lemma 3.1 Let P be a monotone property of graphs, and suppose that for every graph G ∈ P
with minimum degree d, and every set X ⊂ V (G) of size at most f (d),

|∂X| > 2|X|.

Then every G ∈ P of average degree at least 16d contains cycles of 3f (d) consecutive even lengths,
the shortest having length at most twice the largest radius of any component of G.

Proof. Let G′ be a maximum bipartite subgraph of G, and let T be a breadth-ﬁrst search tree
in a connected component F of G′ of average degree at least 8d. If Li is the set of vertices at
distance i from the root of T in F , then for some i, the subgraph F ∗ of F induced by Li ∪ Li+1
has average degree at least 4d. Let T ∗ be a breadth ﬁrst search tree in a connected component of
F ∗ of average degree at least 4d. If L∗
j is the set of vertices at distance j from the root of T ∗ in
F ∗, then for some j, the subgraph F ∗
j of F ∗ induced by L∗
j ∪ L∗
j+1 has average degree at least 2d.
Now let Γ be a subgraph of F ∗
j with minimum degree at least d. Since P is monotone property
and G ∈ P we have that also Γ ∈ P. Therefore, |∂X| > 2|X| for every subset X ⊂ V (Γ) of size at
most f (d). By P´osa’s Lemma, there is a path P ⊂ Γ of length 3f (d). If T ′ is a minimal subtree
of T ∗ whose set of end vertices is V (P ) ∩ L∗
j , then as in Lemma 2.3, P ∪ T ′ contains a θ-graph,
J, containing a cycle of length 3f (d) + 2. Let T ′′ be the minimal subtree of T whose set of end
vertices is V (J). Applying Lemma 2.4 as in the proof of Theorem 1.1, we see that J ∪ T ′′ contains
cycles of 3f (d) consecutive even lengths in G. Since the shortest cycle has length at most 2i + 2,
the proof is complete.

In what follows, we denote by ex(n, H) the Tur´an number of graph H, which is the maximum
number of edges in an H-free graph on n vertices. To obtain expansion in H-free graphs, where
H is bipartite, we show that it is enough to ﬁnd upper bounds for ex(n, H).

Lemma 3.2 Let a > 0, 1
2 < b < 1 be reals such that for any positive integer n, ex(n, H) ≤ an2b.
Then, for any H-free graph G of minimum degree at least 18ad, and any subset X of vertices of
G of size at most d1/(2b−1), |∂X| > 2|X|.
 8

Proof. Suppose that X is a subset of G of size m such that |∂X| ≤ 2|X|. Let GY be the subgraph
of G induced by Y = X ∪ ∂X. Then |Y | ≤ 3m and e(GY ) ≥ 9ad|X| = 9adm. On the other hand,
since GY is H-free we have that

9adm ≤ e(GY ) ≤ ex(|Y |, H) ≤ a|Y |
2b ≤ a(3m)
2b < 9am2b.

Therefore m2b−1 > d, which proves the lemma.

Proof of Theorem 1.2. By the well known result of K¨ovari, S´os and Tur´an [17], for every
bipartite graph H there are two constants t > 1 and c depending only H such that

ex(n, H) ≤ cn2−1/t.

By Lemma 3.2, with a = c and b = 1 − 1/2t, every H-free graph F of minimum degree at least
18cd has the property that for every X ⊂ V (F ) of size at most f (d) = dt/(t−1), |∂X| > 2|X|.
By Lemma 3.1, with P equal to the set of all H-free graphs, we deduce that every G ∈ P of
average degree 288cd contains 3f (d) cycles of consecutive even lengths, proving the theorem. For
the particular case when H is r-half-bounded, Alon, Krivelevich and Sudakov [1] showed that

ex(n, H) = O(n2− 1
r ),

so the proof above applies with b = 1 − 1/(2r) and gives Ω(dr/(r−1)) cycles of consecutive even
lengths. Finally, if H = C2k, then Corollary 9 in [23] shows

ex(n, H) = 8kn1+ 1
k ,

so we can apply the above proof with b = 1
2 + 1
2k to conclude that for every C2k-free graph G,
C(G) contains Ω(dk) consecutive even integers.

4 Arithmetic structure of C(G).

Fix π < σ, and let Pi, i ≥ 1 denote the monotone property of graphs containing no cycle of length
σ(j) for all σ(j) ≤ π(i), and recall ∆(i) = max{σ(j) − σ(j − 1) : σ(j) ≤ π(i)}. To prove Theorem
1.3, we ﬁrst prove the following claim.

Claim 4.1 Let (ai)i≥1 be positive real numbers such that a1 = 4π(1) and, for all i ≥ 2,

π(i − 1) log ai
288ai−1 ≥ 2 log ∆(i).

Then, for every n-vertex graph G ∈ Pi,
 e(G) ≤ ain1+ 2
π(i) .

9

Proof. We proceed by induction on i. For i = 1, Corollary 9 in [23] gives

e(G) ≤ 4π(1)n1+ 2
π(1) ,

and this proves the claim for i = 1. Suppose we have proved the claim for j < i, and let G ∈ Pi
be an n-vertex graph with e(G) > ain1+2/π(i), where ai satisﬁes the bounds in the claim. By
the induction hypothesis we have that every m-vertex graph in Pi−1 has at most ai−1m1+2/π(i−1)

edges. Therefore by Lemma 3.2, we have that for any graph F ∈ Pi−1 with minimum degree d
every subset X ⊂ V (F ) of size at most

f (d) = ( d
18ai−1
 ) 1
2 π(i−1)

has |∂X| > 2|X|.

Since G has n vertices and e(G) ≥ ain1+2/π(i), by Lemma 6 in [23], there is a subgraph Γ of G of
average degree at least ai and radius at most 1
2 π(i). Note that Γ has property Pi and thus has
also property Pi−1. By Lemma 3.1, Γ contains cycles of at least 3f ( ai
16 ) consecutive even lengths,
the shortest of which has length at most π(i). Since Γ ∈ Pi, there must be less than ∆(i) of these
consecutive even lengths, otherwise Γ contains a cycle of length σ(j) for some j ≤ π(i). Therefore

( ai
288ai−1
 ) π(i−1)
2 = f ( ai
16
 ) < 3f ( ai
16
 ) < ∆(i)

which contradicts the bounds on ai in the claim.

Proof of Theorem 1.3. Recall that π(0) = 1, ∆(1) = π(1) and let

ar = 4π(1)(288)
r−1 r∏

i=2 exp ( 2 log ∆(i)
π(i − 1)
 ) < 1
2 exp
 (

6r +
 r∑

i=1
 2 log ∆(i)
π(i − 1)
 )
 .

Since ar satisﬁes the condition of the Claim 4.1, we have that the estimate on the number of edges
of G from this claim is valid for any r. Therefore the average degree of G is at most

inf
r≥1 2arn2/π(r) ≤ inf
r≥1 exp
 (

6r +
 r∑

i=1
 2 log ∆(i)
π(i − 1) + 2 log n
π(r)
 )
 .

This bound is valid for any π < σ, so this completes the proof of Theorem 1.3.

Proof of Corollary 1.4. Since σ is exponentially bounded, σ(i) ≤ Cσ(i − 1) for all i ≥ 2. Let
r = log*n and let π < σ be chosen so that 2π(i−1) ≤ π(i) ≤ (2C)π(i−1) for all i ≥ 2. Note that
π(r) ≥ n. Then, since ∆(i) ≤ π(i), the upper bound in Theorem 1.3 is

exp
 (

6r +
 r∑

i=1
 2 log π(i)
π(i − 1) + 2 log n
n
 )
 ≤ exp(6r + 2r log(2C) + 2) = e
O(log*n).

This proves Corollary 1.4.
 10

In conclusion, we show that the bound in Theorem 1.3 cannot be improved in general.

Construction. We construct a sequence of graphs G1, G2, G3, . . . such that |V (Gk)| = nk − 2,
Gk is (αk + 1)-regular, and Gk has girth larger than nk−1, where nk is even for all k and n0 := 2.
By known probabilistic and explicit constructions of small graphs of large girth (see, e.g., [19] and
[20]), we may take log nk = nk−1 log αk. Now let σ be deﬁned by σ(i) = ni. Since Gi has girth
larger than ni−1 and Gi has order less than ni, none of the graphs Gi have a σ-cycle. We choose
αi so that αi ≥ 2
22i .

If we take π = σ in Theorem 1.3, and r = i, then we have ∆(i) ∼ ni as i → ∞, and also

log αi∑
j<i log αj → ∞.

Also, as j → ∞, 2 log ∆(j)
π(j − 1) ∼ 2 log nj
nj−1 = 2 log αj,

and the upper bound on the average degree of Gi from Theorem 1.3 is:

exp
 

6i +
 i∑

j=1
 2 log ∆(j)
π(j − 1) + 2 log ni
π(i)
 

 = α
2+o(1)
i .

Since Gi has average degree αi + 1, the bound given by Theorem 1.3 is tight up to the constant
factor in the exponent.

5 Concluding Remarks

• Even cycles. It would be interesting to determine if there is an inﬁnite increasing exponentially
bounded sequence σ for which there are graphs of arbitrarily large average degree containing no
σ-cycles. Erd˝os [10] states that this is probably true when σ is the sequence of powers of two,
although no example of a graph of minimum degree three with no cycle of length a power of two
is known. The construction in Section 4 shows that if we take a sequence σ of positive integers
deﬁned by log σ(i) = 22iσ(i − 1), for i ≥ 1, then there are graphs of arbitrarily large average
degree with no σ-cycles.

• Odd cycles. Erd˝os [10] posed analogous questions for odd cycles in graphs of large chromatic
number, for example, does every graph of inﬁnite chromatic number contain a cycle of length
equal to an odd integer square? By repeating a similar construction to that given in Section 4, it
is possible to show that there are (very fast-growing) inﬁnite increasing sequences of odd integers
σ and graphs of inﬁnite chromatic number containing no σ-cycle. On the other hand, we ask
the following concrete question: does every graph of chromatic number at least four contain a
cycle of length one more than a power of two? This seems to be a natural generalization of the
Erd˝os-Gy´arf´as [9] conjecture.
 11

• Chromatic number and cycle lengths. It seems that the result of Theorem 2.7 can be
further improved. In particular in [8], Erd˝os asked whether for every ǫ > 0 and suﬃciently large
d, every triangle free graph of chromatic number d contains at least Ω(d2−ǫ) cycles of diﬀerent
lengths. More generally one can ask if every graph of girth at least 2t and chromatic number d
contains at least Ω(dt−ǫ) cycles of diﬀerent length. We believe that the techniques which were
developed in this paper may be useful to attack these problems.

Acknowledgment. The authors would like to thank the referee for careful reading of this
manuscript.

References

[1] N. Alon, M. Krivelevich and B. Sudakov, Tur´an numbers of bipartite graphs and related
Ramsey-type questions, Combinatorics Probability and Computing 12 (2003), 477–494.

[2] N. Alon, L. R´onyi and T. Szab´o, Norm-graphs: variations and applications, J. Combinatorial
Theory Ser. B 76 (1999), 280–290.

[3] B. Bollob´as, Cycles modulo k, Bull. London Math. Soc. 9 (1977), 97-98.

[4] B. Bollob´as and A. Thomason, Weakly pancyclic graphs, J. Combinatorial Theory Ser. B 77
(1999), 121–137.

[5] A. Bondy, Pancyclic graphs I, J. Combinatorial Theory Ser. B 11 (1971) 80–84.

[6] A. Bondy and M. Simonovits, Cycles of even length in graphs, J. Combinatorial Theory Ser.
B 16 (1974), 97–105.

[7] M. N. Ellingham and D. K. Menser, Girth, minimum degree, and circumference. J. Graph
Theory 34 (2000), no. 3, 221–233.

[8] P. Erd˝os, Some of my favourite problems in various branches of combinatorics, Matematiche
(Catania) 47 (1992), 231–240.

[9] P. Erd˝os, Some of my favorite solved and unsolved problems in graph theory, Quaestiones
Math. 16 (1993), 333–350.

[10] P. Erd˝os, Some old and new problems in various branches of combinatorics. Graphs and
combinatorics (Marseille, 1995). Discrete Math. 165/166 (1997), 227–231.

[11] P. Erd˝os, R. Faudree, C. Rousseau and R. Schelp, The number of cycle lengths in graphs of
given minimum degree and girth, Discrete Mathematics 200 (1999), 55–60.

[12] G. Fan, Distribution of cycle lengths in graphs, J. Combinatorial Theory Ser. B 84 (2002),
187–202.

[13] R. Gould, P. Haxell and A. Scott, A note on cycle lengths in graphs, Graphs and Combina-
torics 18 (2002), 491–498.
 12

[14] A. Gy´arf´as, Graphs with k odd cycle lengths, Discrete Mathematics 103 (1992), 41–48.

[15] A. Gy´arf´as, J. Koml´os and E. Szemer´edi, On the distribution of cycle lengths in graphs, J.
Graph Theory 8 (1984), 441–462.

[16] J. Koll´ar, L. R´onyai and T. Szab´o, Norm-graphs and bipartite Turan numbers, Combinatorica
16 (1996), 399–406.

[17] T. K¨ovari, V.T. S´os and P. Tur´an, On a problem of K. Zarankiewicz,Colloquium Math. 3
(1954), 50–57.

[18] L. Lov´asz, Combinatorial Problems and Exercises, 2nd Ed., North-Holland, Amsterdam,
1993.

[19] A. Lubotsky, M. Phillips and P. Sarnak, Ramanujan Graphs, Combinatorica 9 (1988), 261–
277.

[20] G. Margulis, Explicit group-theoretic constructions of combinatorial schemes and their appli-
cations in the construction of expanders and concentrators, Problems Inform. Transmission
24 (1988), 39–46.

[21] O. Ore, On a graph theorem by Dirac, J. Combinatorial Theory 2 (1967), 383–392.

[22] L. P´osa, Hamiltonian circuits in random graphs, Discrete Mathematics 14 (1976), 359–364.

[23] J. Verstra¨ete, On arithmetic progressions of cycle lengths in graphs, Combinatorics Proba-
bility and Computing 9 (2000), 369–373.

[24] C. Q. Zhang, Circumference and girth. J. Graph Theory 13 (1989), no. 4, 485–490.

[25] B. Z. Zhao, The circumference and girth of a simple graph. (Chinese) J. Northeast Univ.
Tech. 13 (1992), no. 3, 294–296.
 13
