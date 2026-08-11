<!-- source: https://arxiv.org/pdf/2010.15802 | converted from PDF -->

arXiv:2010.15802v2  [math.CO]  19 Sep 2022
A solution to Erd˝os and Hajnal’s odd cycle problem

Hong Liu ∗ Richard Montgomery †

September 20, 2022

Abstract

In 1981, Erd˝os and Hajnal asked whether the sum of the reciprocals of the odd cycle lengths
in a graph with inﬁnite chromatic number is necessarily inﬁnite. Let C(G) be the set of cycle
lengths in a graph G and let Codd(G) be the set of odd numbers in C(G). We prove that, if
G has chromatic number k, then ∑ℓ∈Codd(G) 1/ℓ ≥ (1/2 − ok(1)) log k. This solves Erd˝os and
Hajnal’s odd cycle problem, and, furthermore, this bound is asymptotically optimal.
In 1984, Erd˝os asked whether there is some d such that each graph with chromatic number
at least d (or perhaps even only average degree at least d) has a cycle whose length is a power
of 2. We show that an average degree condition is suﬃcient for this problem, solving it with
methods that apply to a wide range of sequences in addition to the powers of 2.
Finally, we use our methods to show that, for every k, there is some d so that every graph
with average degree at least d has a subdivision of the complete graph Kk in which each edge
is subdivided the same number of times. This conﬁrms a conjecture of Thomassen from 1984.

1 Introduction

Does the chromatic number or the average degree imply anything about the cycle lengths of a
graph? For any ﬁxed k, we can never infer the presence of a cycle with length k, as a graph may
have arbitrarily high chromatic number yet no such cycle (as Erd˝os famously showed in 1959 [1]).
Can we, however, say something about the density of cycle lengths or infer the existence of a cycle
with length in some given inﬁnite set of integers?
We will consider these two questions for both the even cycles and the odd cycles of a graph.
From an average degree condition, we can only say something about the even cycles of a graph, as,
of course, a graph with high average degree may have no odd cycles. The natural corresponding
condition to impose for odd cycles is one on the chromatic number (see, for example, the survey
by Verstra¨ete [24]).
In this paper, we give the ﬁrst constructions for even cycles with precise lengths using only an
average degree condition. We then develop our methods further to ﬁnd many odd cycle lengths
in graphs with a chromatic number condition. This development, while itself novel, relies on the

∗Extremal Combinatorics and Probability Group (ECOPRO), Institute for Basic Science (IBS), Daejeon, South
Korea. Email: hongliu@ibs.re.kr. Supported by the Institute for Basic Science (IBS-R029-C4) and the UK Research
and Innovation Future Leaders Fellowship MR/S016325/1.
†Mathematics Institute, University of Warwick, Coventry, CV4 7AL, UK. Email:
richard.montgomery@warwick.ac.uk. Supported by the European Research Council (ERC) under the Euro-
pean Union Horizon 2020 research and innovation programme (grant agreement No. 947978) and the Leverhulme
trust.
 1

strength of our results on even cycles and cannot be done using the previous results guaranteeing
diﬀerent even cycle lengths.
We now discuss further, and state our results on, even cycles in graphs with an average de-
gree condition (in Section 1.1) and odd cycles in graphs with a chromatic number condition (in
Section 1.2). We then give a further application of our work which conﬁrms a conjecture of
Thomassen [20] on subdivisions (in Section 1.3). For questions on cycle lengths in graphs un-
der additional conditions, and the background on them, we refer the reader to the comprehensive
survey by Verstra¨ete [24].

1.1 Average degree and even cycle lengths

In 1966, Erd˝os and Hajnal [8] suggested the harmonic sum of the cycle lengths in a graph as a
measure of the density of its cycle lengths. In particular, letting C(G) be the set of cycle lengths
in a graph G, Erd˝os and Hajnal [8] asked whether

∑

ℓ∈C(G)
 1
ℓ → ∞ as χ(G) → ∞, (1)

where χ(G) is the chromatic number of G. As Erd˝os later wrote [4], they felt that (1) should even
hold under the weaker condition d(G) → ∞, where d(G) is the average degree of the graph G. In
1984, Gy´arf´as, Koml´os and Szemer´edi [10] conﬁrmed this stronger conjecture by proving that any
graph G with average degree d has ∑ℓ∈C(G) 1/ℓ = Ωd(log d). If G is a complete balanced bipartite
graph with average degree d, then ∑ℓ∈C(G) 1/ℓ = (1/2 + od(1)) log d, so this lower bound is tight up
to the implicit constant. Here and throughout the paper, we write log for the natural logarithm.
Erd˝os [4] had previously stated, in 1975, that it was likely that (1/2 + od(1)) log d is the correct
asymptotic lower bound, over all graphs G with d(G) ≥ d, and this remained an open problem.
We say an increasing sequence σ1, σ2, σ3, . . . of integers is unavoidable with high average degree
if there is some d such that any graph with average degree at least d has a cycle with length in
σ1, σ2, σ3, . . .. In 1977, Bollob´as [2] conﬁrmed a conjecture of Burr and Erd˝os by showing that,
if σi forms an arithmetic progression containing even numbers, then σi is unavoidable with high
average degree. Solving a problem of Erd˝os, in 2005 Verstra¨ete [23] showed that some unavoidable
sequence with density 0 must exist, without giving an explicit sequence.
In 2008, Sudakov and Verstra¨ete [18] showed that many increasing sequences of integers are
unavoidable in all but (potentially) exceptionally sparse graphs. In particular, they showed that,
for any exponentially bounded increasing sequence of even integers σi (that is, where σi+1 ≤ Cσi
for each i ∈ N and some ﬁxed C > 1), any n-vertex graph G with σi /∈ C(G) for each i ∈ N must
have average degree at most eO(log∗ n), where log∗ n is the iterated logarithm function. In 1984,
Erd˝os [6] had asked whether the powers of 2 are unavoidable with high average degree, but, despite
the results quoted here, there remained no explicit sequence with density 0 which was known to be
unavoidable with high average degree (or even unavoidable with high chromatic number, as deﬁned
analogously in Section 1.2).
In this paper, we introduce new techniques for constructing even cycles while controlling their
length. This allows us to ﬁnd, in any graph G, a long interval of consecutive even numbers in C(G),
as follows.
 2

Theorem 1.1. There is d0 > 0 such that the following holds. If G is a graph with average degree
d ≥ d0, then, there is some ℓ ≥ d/(10 log12 d) such that C(G) contains every even integer in
[log8 ℓ, ℓ].

From the density of the even numbers in the interval [log8 ℓ, ℓ] as ℓ increases, we get immediately
the following improvement of the result of Gy´arf´as, Koml´os and Szemer´edi [10], which conﬁrms the
asymptotically correct lower bound on the harmonic sum of C(G), as conjectured by Erd˝os [4].

Corollary 1.2. If a graph G has average degree d, then

∑

ℓ∈C(G)
 1
ℓ ≥ (1
2 − od(1)
) log d.

By Theorem 1.1, any avoidable sequence of cycle lengths must continue to avoid some intervals
[log8 ℓ, ℓ] as ℓ → ∞. Thus, many increasing sequences of even integers are unavoidable with high
average degree, as follows.

Corollary 1.3. There is some d0 > 0 such that the following holds. Given any inﬁnite sequence
σi, i ∈ N, of increasing even integers with σi+1 ≤ exp(σ1/10
i ) for each i ∈ N, any graph G with
average degree at least max{d0, σ2
1} has some i ∈ N with σi ∈ C(G).

In particular, this answers the question of Erd˝os [6] mentioned above by showing that the
powers of 2 are unavoidable with high average degree, as, furthermore, is any exponentially bounded
sequence of increasing even numbers. This latter implication answers a question of Sudakov and
Verstra¨ete [18]; for further questions on speciﬁc sequences answered by Corollary 1.3, we refer the
readers to [7].
On the other hand, the sequence deﬁned by σ1 = 1 and σi+1 = 2(i+ 1)σi for each i ∈ N is known
to be avoidable (see [18]). Corollary 1.3 is thus optimal up to the fraction 1/10 in the exponent,
though it may hold with 1/10 replaced by 1−oi(1). We have not optimised our methods to maximise
the fraction 1/10, but note that doing so could not increase it beyond 1/3 (see Section 2.4.4).

1.2 Chromatic number and odd cycle lengths

Consider the set of odd cycle lengths in G, by letting Codd(G) = {ℓ ∈ C(G) : ℓ is odd}. As noted
above, a natural condition to impose in search of odd cycles is one on the chromatic number rather
than the average degree, and, for example, Gy´arf´as [9] proved in 1992 that a graph with chromatic
number at least 2k + 1 must have |Codd(G)| ≥ k. In 1981, Erd˝os and Hajnal [5] asked whether
∑

ℓ∈Codd(G)
 1
ℓ → ∞ as χ(G) → ∞. (2)

As Erd˝os noted [6], this gives a ‘much deeper question’ than the corresponding question for all
cycle lengths and chromatic number that we considered in Section 1.1. Indeed, the only relevant
result towards this has been by Sudakov and Verstra¨ete [19], who showed that ∑ℓ∈Codd(G) 1/ℓ → ∞
if the independence ratio of G is not extremely small compared to its number of vertices. Here,
the independence ratio of G is supX⊆V (G) |X|
α(X) , where α(X) is the independence number of the
subgraph of G induced on X and the supremum is taken over all non-empty vertex subsets.
Building on our methods for even cycles, we use the precision of these techniques to construct
a large interval of cycle lengths using a high chromatic number, as follows.

3

Theorem 1.4. For each ε > 0, there is some k0 ∈ N such that the following holds for each k ≥ k0.
If G is a graph with chromatic number k, then, for some ℓ ∈ N, C(G) contains every odd integer in
[ℓ, ℓ · k1−ε].

As the harmonic sum of the odd integers in [ℓ, ℓ · k1−ε] diverges as k → ∞ (for all values of ℓ),
this solves Erd˝os and Hajnal’s odd cycle problem by conﬁrming (2). Furthermore, in combination
with Theorem 1.1, we get the following immediate lower bound for the harmonic sum of the cycle
lengths of any speciﬁc residue, which answers another question of Erd˝os [6].

Corollary 1.5. Let a, b ∈ N, and let Ca,b(G) = {ℓ ∈ C(G) : ℓ ≡ a mod b}. If G has chromatic
number k, then ∑

ℓ∈Ca,b(G)
 1
ℓ ≥ ( 1
b − ok(1)
) log k.

We say an increasing sequence σ1, σ2, σ3, . . . of integers is unavoidable with high chromatic
number if there is some k such that any graph with chromatic number at least k has a cycle with
length in σ1, σ2, σ3, . . .. There have previously been no non-trivial sequences of increasing odd
integers which were known to be unavoidable with high chromatic number, but, similarly to in
Section 1.1, Theorem 1.4 immediately implies that many such sequences are unavoidable with high
chromatic number, as follows.

Corollary 1.6. Given C ∈ N, there exists k0 ∈ N such that the following holds. Let σ1, σ2, . . . be
an inﬁnite increasing sequence of odd integers such that σi+1 ≤ Cσi for each i ∈ N. Then, every
graph G with chromatic number at least max{k0, σ2
1} has some i ∈ N with σi ∈ C(G).

We remark that our proof in fact shows that Theorem 1.4 (and hence also Corollaries 1.5
and 1.6) holds with the weaker hypothesis that the graph G is ‘not too close’ to being bipartite.
That is, as seen in Section 5.1.1, we use only the condition that, after removing the edge-set of any
bipartite graph from G, there is still a subgraph with average degree Ω(k).

1.3 Balanced subdivisions

A subdivision of a graph G is obtained by replacing each edge of G by a path, such that the new
paths are internally vertex disjoint. This notion has played a central role in topological graph
theory since the seminal result of Kuratowski in 1930 that a graph is planar if and only if it does
not contain a subdivision of the complete graph with ﬁve vertices or a subdivision of the complete
bipartite graph with three vertices on each side [14].
In 1967, Mader [16] proved that, for each k ∈ N, there is some d = d(k) such that every graph
with average degree at least d contains a subdivision of the complete graph Kk. After improved
bounds on d(k) by Mader [17], and Koml´os and Szemer´edi [12], Bollob´as and Thomason [3] proved
that, optimally, we may take d(k) = O(k2). Koml´os and Szemer´edi [13] later improved their own
methods to give an independent proof of this, and the graph expansion methods they introduced
(see Section 2.2) form the basis for many constructions in sparse graphs both here and elsewhere
(see, for example, [11, 15]).
Our constructive approach to controlling the length of cycles also allows us to control the
length of paths, and thus construct subdivisions in which each edge is replaced by a path of the
same length. For integers ℓ, k ∈ N, denote by TK
(ℓ)
k a subdivision of a complete graph Kk in which
each edge is replaced by a path with length ℓ. We say that TK
(ℓ)
k is a balanced subdivision of Kk.

4

In 1984, Thomassen [20] (see also [21], [22]) conjectured that, for each k ∈ N, high average
degree in a graph is suﬃcient to guarantee a balanced subdivision of Kk. This was open even for
k = 4. We conﬁrm Thomassen’s conjecture, as follows.

Theorem 1.7. For each k ∈ N, there exists d such that every graph with average degree at least d
contains a TK
(ℓ)
k for some ℓ ∈ N.

We note that it is conceivable that there is some ε > 0 such that any graph with average degree
at least d in fact contains a TK
(ℓ)
ε√
d, which would be optimal up to the value of ε. Furthermore,
this may be provable using appropriate extensions of our methods (in particular along the lines of
the techniques in [15]). However, though the balanced subdivision problem was the original focus
of our work, we do not push these techniques further at the expense of a clear presentation of the
new cycle construction techniques.

2 Structure and proof sketches

After describing our notation in Section 2.1, in Section 2.2 we recall the graph expansion concepts
introduced by Koml´os and Szemer´edi in [12, 13]. This allows us to give our main theorem, Theo-
rem 2.7, in Section 2.3 and derive Theorem 1.1, while noting how we use similar methods to prove
Theorem 1.7. We then sketch the proof of Theorem 2.7 in Section 2.4. The proof of Theorem 1.4
is sketched in Section 2.5. Finally, in Section 2.6, we highlight one particular innovation for our
constructions in expanders, which may prove useful elsewhere.

2.1 Notation

Let G be a graph, let v ∈ V (G) be a vertex and let W ⊆ V (G) be a set of vertices. We write
|G| = |V (G)| for the order of the graph. Let δ(G), d(G) and ∆(G) be the minimum, average and
maximum degree of G respectively, and let NG(v) be the set of neighbours of v in G. Denote by
NG(v, W ) the set of neighbours of v in W , and denote by dG(v, W ) = |NG(v, W )| the degree of
v into W in G. Denote the (external) neighbourhood of W by NG(W ) = (∪v∈W N (v)) \ W . Let
G[W ] ⊆ G be the induced subgraph of G with vertex set W . Denote by G−W the induced subgraph
G[V (G) \ W ]. We write N 0
G(W ) = W , and, for each integer k ≥ 1, let N k
G(W ) = NG(N k−1
G (W ))
be the set of vertices a graph distance k from W , and let Bk
G(W ) = ∪0≤j≤kN j
G(W ) be the ball of
radius k around W in G. We let B(W ) = B1(W ).
Given graphs G and H, the graph G∪H has vertex set V (G)∪V (H) and edge set E(G)∪E(H).
Denote by G \ H the graph with vertex set V (G) and edge set E(G) \ E(H). For a collection P of
graphs, denote by |P| the number of graphs in P and write V (P) = ∪G∈PV (G).
For a path P , let its length be ℓ(P ). Where we say P is a path from a vertex set A to a disjoint
vertex set B, we mean that P has one endvertex in each of A and B, and no internal vertices in
A ∪ B. For each ℓ ∈ N and k > 0, TK
(ℓ)
k is a subdivision of a complete graph K⌊k⌋ in which each
edge is replaced by a path with length ℓ.
Many of our results that build to the theorems stated in Section 1 state that for each ε1, ε2 > 0
(and perhaps each k ∈ N), there is some d0(ε1, ε2) (or d0(ε1, ε2, k)) such that some property holds
for n ≥ d ≥ d0. For brevity, we do not calculate the function d0(ε1, ε2) (or d0(ε1, ε2, k)) and assume
implicitly in our proofs that n and d are as large as needed, depending on ε1 and ε2 (and perhaps k)
— where it may help the reader we recall this at various points in the proofs. The results from now

5

on in this paper are stated and proved in order, so that these functions could be chosen sequentially
through the paper.
We omit the subscript G when the underlying graph G is clear. When it is not essential, we
omit the ﬂoors and ceilings. All logarithms are natural.

2.2 Koml´os-Szemer´edi graph expansion

An expansion property in a graph G is typically one in which every set X ⊆ V (G) satisﬁes
|NG(X)| ≥ ε|X| for some function ε depending on the size of X. Expansion is key to all of
our constructions. Our expansion must therefore exist in some subgraph of any graph. Following
Koml´os and Szemer´edi [12, 13], eﬀectively we use the strongest expansion that can be found in
some subgraph of any graph, based on its average degree.

Deﬁnition 2.1. For each ε1 > 0 and k > 0, a graph G is an (ε1, k)-expander if

|N (X)| ≥ ε(|X|, ε1, k) · |X|

for all X ⊆ V (G) with k/2 ≤ |X| ≤ |G|/2, where

ε(x, ε1, k) := { 0 if x < k/5,
ε1/ log2(15x/k) if x ≥ k/5. (3)

Whenever the choices of ε1, k are clear, we omit them and write ε(x) for ε(x, ε1, k).

If an n-vertex graph G is an (ε1, k)-expander and X ⊆ V (G) has size at least k/2, then
Bi
G(X) increases as i increases, until the set contains at least n/2 vertices. The rate of expansion,
|NG(Bi
G(X))|/|Bi
G(X)| ≥ ε(|Bi
G(X)|, ε1, k) guaranteed by the expansion condition decreases as i
increases (see, for example, [13]). That is, ε(x, ε1, k) decreases as x ≥ k/2 increases. However,
ε(x, ε1, k) · x increases as x does, so the lower bound from expansion we have for |NG(Bi
G(X))|
increases as i increases.
As Koml´os and Szemer´edi [13] showed, every graph G contains an expander with comparable
average degree to G, as follows.

Theorem 2.2 ([13]). There exists some ε1 > 0 such that the following holds for every k > 0. Every
graph G has an (ε1, k)-expander subgraph H with d(H) ≥ d(G)/2 and δ(H) ≥ d(H)/2.

Note that, in Theorem 2.2, the expander subgraph H can be much smaller than the original
graph G in size. Indeed, G could be the disjoint union of many copies of such a graph H.
We use expansion to expand and connect vertex sets, creating paths to construct cycles of
varying lengths. A typical use is the following result of Koml´os and Szemer´edi, though we use the
comparable Lemma 3.4.

Lemma 2.3 ([13]). Let ε1, k > 0. If G is an n-vertex (ε1, k)-expander, then any two vertex sets,
each of size at least x ≥ k, are of distance at most 2
ε1 log3(15n/k) apart. This remains true even
after deleting x · ε(x)/4 arbitrary vertices from G.

It is convenient to work in a bipartite graph; to do this we use the following simple and well
known result.

Proposition 2.4. Within any graph G there is a bipartite subgraph H with d(H) ≥ d(G)/2.

Combining this with Theorem 2.2, we get the following immediate corollary.

Corollary 2.5. There exists some ε1 > 0 such that the following holds for every ε2 > 0 and d ∈ N.
Every graph G with d(G) ≥ 8d has a bipartite (ε1, ε2d)-expander subgraph H with δ(H) ≥ d.

6

2.3 A stronger version of Theorem 1.1

We will prove Theorem 1.1 in the slightly stronger form of Theorem 2.7 below, which applies to an
expander. Combining this with Corollary 2.5 easily gives Theorem 1.1, as shown below. We use
Theorem 2.7 to prove Theorem 1.4, as outlined in Section 2.5. Theorem 1.7 is proved using very
similar methods to Theorem 2.7, and we comment on this below.
In order to state Theorem 2.7, we use the following deﬁnition, which records whether there will
be even or odd length paths between two vertices u and v in a connected bipartite graph H.

Deﬁnition 2.6. For any connected bipartite graph H and u, v ∈ V (H), let

π(u, v, H) =
 



 0 if u = v,
1 if u and v are in diﬀerent vertex classes in the (unique) bipartition of H,
2 if u and v are in the same vertex class and u ̸= v.

Note that, for example by Lemma 2.3, any (ε1, k)-expander subgraph with minimum degree at least
k is connected, and this will allow us to use this deﬁnition for the bipartite expanders we use.
In common with many of our results in the rest of this paper, Theorem 2.7 applies only to
TK
(2)
ℓ -free graphs for some ℓ (often ℓ = d/2). A subdivision of the complete graph on ℓ vertices,
with each edge subdivided into a path of length 2, has many diﬀerent even cycle lengths, and many
diﬀerent path lengths between pairs of vertices. As our aim in applying Theorem 2.7 is to ﬁnd
only some subgraph with this property (see, for example, the proof of Corollary 5.1), we need look
no further than such a subdivision. Why our constructions require the graph to be TK
(2)
ℓ -free is
commented on in Section 3.7.

Theorem 2.7. There exists ε1 > 0, such that, for each 0 < ε2 < 1/5, there exists d0 = d0(ε1, ε2)
such that the following holds for each n ≥ d ≥ d0. Suppose that H is a TK
(2)
d/2-free bipartite n-vertex
(ε1, ε2d)-expander with δ(H) ≥ d. Let x, y ∈ V (H) be distinct, and let

ℓ ∈ [log7 n, n/ log12 n]

satisfy π(x, y, H) = ℓ mod 2.
Then, H contains an x, y-path with length ℓ.

Theorem 1.1 follows from Theorem 2.7 and Corollary 2.5, as follows.

Proof of Theorem 1.1. Let ε1 > 0 be such that the condition in Corollary 2.5 applies, and let
ε2 = 1/100. Let d0 be large (see Section 2.1), and in particular large enough that the property in
Theorem 2.7 holds for ε1 and ε′
2 = 8ε2, for each d ≥ d0/8.
Let G be a graph with average degree d ≥ d0 and let ¯d = d/8. By the property from Corol-
lary 2.5, G contains a bipartite (ε1, ε2d)-expander subgraph H with δ(H) ≥ ¯d. As ¯d = d/8, H is
an (ε1, 8ε2 ¯d)-expander. If H contains a TK
(2)
¯d/2, then H contains every even cycle length between 6

and ¯d. As ¯d = d/8 is large, the property in the theorem holds with ℓ = ¯d as log8 ¯d ≥ 6.
Assume then that H is TK
(2)
¯d/2-free. As δ(H) ≥ ¯d > 0, we can pick distinct vertices x, y ∈ V (H)

such that xy ∈ E(H). Note that π(x, y, H) = 1. Let n = |H| and ℓ = n/ log12 n ≥ ¯d/ log12 ¯d ≥
d/(10 log12 d), as ¯d = d/8 is large.
For every even ℓ′ ∈ [log8 ℓ, ℓ], (ℓ′ − 1) is an odd number in [log7 n, n/ log12 n]. Then, by the
property from Theorem 2.7 applied with x and y, there is an x, y-path with length ℓ′ − 1 in H, and
therefore a cycle with length ℓ′ in H.
 7

For Theorem 1.7, essentially, we ﬁnd a copy of TK
(ℓ)
k , for some ℓ ∈ N, by ﬁrst taking an expander
subgraph and k distinct vertices within it to be the core vertices. Core vertices in a Kk-subdivision
are the vertices which are not interior vertices of a path which replaces an edge. Using the same
construction as for Theorem 2.7 multiple times, we then ﬁnd internally vertex disjoint paths with
the same length between each pair of core vertices. This is done in Section 4.4.

2.4 Proof sketch for Theorem 2.7

To discuss the proof of Theorem 2.7, let H be a TK
(2)
d/2-free bipartite n-vertex (ε1, ε2d)-expander,
with 0 < ε1, ε2 < 1, such that δ(H) ≥ d, and let x, y ∈ V (H) be distinct.
Our aim is to ﬁnd a sequence of x, y-paths in H whose lengths increase by 2 each time. In
Section 2.4.1 we describe how one cycle can be used to ﬁnd two paths with the same endvertices
and lengths diﬀering by 2, and how a connected sequence of cycles can create a longer sequence of
paths with lengths increasing by 2 each time. In Section 2.4.2, we discuss how a sequence of cycles
can be connected, and introduce the concept of an adjuster. In Section 2.4.3, we describe how a
polylogarithmic number of adjusters can be used to ﬁnd long paths with the lengths required by
Theorem 2.7. In Section 2.4.4, we discuss the natural limitations of these methods.

2.4.1 Creating a little adjustment with small cycles

Our proof of Theorem 2.7 is based on the following simple idea. Suppose we can ﬁnd in H a short
cycle C, with length 2ℓ say, which does not contain x or y. Take two vertices v1 and v2 a distance
ℓ − 1 apart on C. Then, C contains one v1, v2-path with length ℓ − 1 and another with length ℓ + 1.
If we can ﬁnd, using new internal vertices, disjoint paths from x to v1 and from y to v2, then we
have two x, y-paths whose lengths diﬀer by 2 (see Figure 1(a)).
If we can chain together many cycles between x and y in this fashion, then, by choosing the
length of the path we take around each cycle, we can vary the length of the path between x and y
in increments of 2 (see Figure 1(c)).

C

P2

P1

v1 v2x y

(a) x, y-paths with lengths diﬀering by 2.
 F1 F2C

P2

P1

v1 v2

(b) An adjuster

x y

(c) x, y-paths with varying lengths depending on the paths taken through the cycles.

Figure 1: Creating x, y-paths of diﬀerent lengths using cycles.

8

2.4.2 Connecting the cycles

In the situation above, if C is a shortest cycle in H, then it is not too diﬃcult to connect x to v1 and
y to v2 (relabelling v1 and v2 if necessary). Indeed, for each i ≥ 0 and v ∈ V (H), any neighbours
of the ball Bi
G−V (C)+v(v) in V (C) must be within distance 2i + 2 of each other on the cycle C,
for otherwise H contains a shorter cycle than C. Given our expansion conditions, this will mean
that Bi
G−V (C)+v1 (v1) and Bi
G−V (C)(x) will both expand as i increases (see Section 3.1). Expanding
these sets until they intersect allows us to ﬁnd a short path from v1 to x while avoiding V (C)\{v1}.
Roughly speaking, setting aside a shortest path P from {v1} to {x, y} which avoids V (C) \ {v1},
we then expand around v2 and the vertex left in {x, y} \ V (P ) while avoiding (V (P ) ∪ V (C)) \ {v2}
to ﬁnd the second path described above.
Connecting multiple cycles is more diﬃcult, simply as there are more vertices to avoid. Due to
this, instead of cycles, we will ﬁnd structures we call simple adjusters. These correspond to the cycle
C, vertices v1 and v2, as well as vertex disjoint subgraphs F1, F2 ⊆ H such that V (F1)∩V (C) = {v1}
and V (F2) ∩ V (C) = {v2} (see Figure 1(b) and Deﬁnition 4.1). The graph F1 (and analogously
F2) has the property that every vertex is a distance Oε1(log3 n) away from v1 in F1, and therefore
a path leading into F1 can be extended with a few additional vertices from V (F1) to one ending
with v1. Furthermore, |F1| will be comfortably larger than C so that F1 can be expanded and
connected while avoiding V (C) \ {v1}. The distance Oε1(log3 n) here comes from an application of
Lemma 3.4.
The heart of our paper is the robust construction of these simple adjusters – that is, having
some set of vertices U which is not too large, we ﬁnd an adjuster in H − U . More discussion of
this construction we defer till Section 4, but we will highlight the key innovation that allows this
in Section 2.6.

2.4.3 Increasing the size of the interval of path lengths

In an n-vertex (ε1, ε2d)-expander H, any two vertices x, y are a distance at most m = Θε1(log3 n)
apart (see Lemma 3.4). Using fairly straightforward methods (see those in Section 3.6), we can use
the expansion conditions to ﬁnd, for any 20m ≤ ℓ ≤ n/ log10 n, a path with length between ℓ − 20m
and ℓ between x and y (see Corollary 3.15). If we can ﬁnd such a path which contains 10m simple
adjusters, then, as long as ℓ = π(x, y, H) mod 2, we can use these adjusters to increase the path
by length 2 until it has length exactly ℓ (see Section 4.3).

2.4.4 The limitations of our methods

Our methods are limited by the length of the paths we ﬁnd between vertex pairs using the
Koml´os-Szemer´edi graph expansion. Here, we can only guarantee a path with length at most
m = Θε1(log3 n). Therefore the lower bound of the interval of path/cycle lengths in Theorem 2.7
and Theorem 1.1 cannot be reduced below Ω(log3 n) while using connection methods with this
graph expansion. Correspondingly, optimising our methods cannot increase the fraction 1/10 in
Corollary 1.3 beyond 1/3.
For simplicity, we connect together around m = Θε1(log3 n) cycles which can each be used to
adjust the length of the paths we ﬁnd by 2. We note that, by using diﬀerent cycles to adjust
the length by diﬀerent amounts, we could use perhaps O(log m) = Oε1(log log n) cycles instead of
around m cycles. However, this saving does not reach a plausible optimal bound as we cannot
guarantee our connecting paths are any shorter.
 9

2.5 Outline of the proof of Theorem 1.4

Note that in a graph H which is a copy of TK
(2)
d , if d ≥ 3, then every edge between two vertices u, v
can be replaced with a path with any odd length in [5, 2d − 1]. If d is large, then this includes paths
with any odd length in [log8 d, d]. Using Corollary 2.5 and Theorem 2.7, then, in any graph with
average degree at least 16d, we can ﬁnd a bipartite subgraph H satisfying the following property.

P There is some ℓH ≥ d/ log12 d such that each edge uv in H can be replaced with a path with
any odd length in [log8 ℓH , ℓH].

Now, suppose G has chromatic number at least 300d and ﬁnd in G a maximal collection H
of edge disjoint bipartite subgraphs H satisfying P with some integer ℓH. We can show that the
chromatic number of the union of these graphs ∪H∈HH is at least 3, for otherwise G \ (∪H∈HH)
has high enough degree that some other bipartite subgraph satisfying P must exist, contradicting
the maximality of H. Therefore, ∪H∈HH contains some odd cycle, C say. Our aim is to use P to
take many edges e of C, and, where He ∈ H is such that e ∈ E(He), replace e with odd paths in
He with many diﬀerent lengths. This would allow us to transform C into odd cycles of diﬀerent
lengths. The challenge is to do this so that all of the paths replacing these edges are vertex disjoint.
This is possible by taking a certain minimal odd cycle C and replacing edges e corresponding to
vertex disjoint graphs He ∈ H. This is discussed in more detail at the start of Section 5, before
Theorem 1.4 is then proved.

2.6 A new construction method: Robust construction of gadgets.

Here, we will highlight an innovation for constructions using Koml´os-Szemer´edi expansion. Roughly
speaking, this technique overcomes the sublinear property of the expansion we work with. For
more details, see Section 3.3. Recall from (3) that in an expander H, any vertex set A ⊆ V (G)
of suitable size has neighbourhood with size Ω(|A|/ log2 |A|), expanding with at least a factor of
ε(|A|) = Θ(1/ log2 |A|).
Our aim is to ﬁnd some special subgraph – let us call it here a gadget – in an expander H while
avoiding a vertex set W . Roughly speaking, it is natural to pick a vertex v in H − W and try to
construct a gadget locally in H around v using the expansion property. If this fails there will then
be some vertex set Av containing v which does not expand in H − W , not even by a reduced factor
of ε(|Av|)/10. If we fail repeatedly, then we ﬁnd many disjoint sets Av, say for the vertices v ∈ V ,
which do not expand in H − W by a factor of ε(|Av|)/10. Eventually, ∪v∈V Av will be much larger
than W , so it expands in H − W by a factor of at least ε(| ∪v∈V Av|)/2. However, as the expansion
function in Section 2.2 is sublinear in x, it is not a contradiction that ∪v∈V Av expands, yet no set
Av does even if the expansion factor required is reduced by a factor of 5.
Instead, we reach a contradiction by exploiting our particular circumstance. We will have that
W is polylogarithmic size (in n), that |V | ≥ n1/2, and the TK
(2)
d/2-free condition will allow us to
have that |NH (Av, W )| ≤ |Av|2 for each v ∈ V . Note that, as, for each v ∈ V , Av does not expand
in H − W by a factor of ε(|Av|)/10, the set Av must have size at most |W | log3 n.
Now, ﬁrstly, if many of the sets Av, v ∈ V , have size at least (log n)1/3, then we ﬁnd a set
V ′ ⊆ V indexing some of these vertices so that |W | log3 n ≤ | ∪v∈V ′ Av| ≤ 2|W | log3 n. Then,
A := ∪v∈V ′Av is large enough to expand past W , and hence expand in H − W with a factor of least
ε(|A|)/2. As, for each v ∈ V ′, log |Av| ≈ log log n ≈ log |A|, the expansion function ε for these sets

10

is essentially the same – near enough that we can get a contradiction from each set Av, v ∈ V ′, not
expanding in H − W by a factor of at least ε(|Av|)/10 yet A = ∪v∈V ′Av expanding in H − W by a
factor of at least ε(|A|)/2.
Thus, we can assume that most of the sets Av, v ∈ V , have size at most (log n)1/3. This gives
us, for such v ∈ V , that |NH (Av, W )| ≤ |Av|2 ≤ (log n)2/3. As W is polylogarithmic in size,
we have at most |W |(log n)2/3 = no(1) subsets of W with size at most (log n)2/3. Thus, for some
r ≤ (log n)1/3, there must be at least r2 vertices v ∈ V – say those in V ′′ – such that |Av| = r for
each v ∈ V ′′ and, over v ∈ V ′′, NH(Av, W ) is the same set, W ′ ⊆ W say. Let A = ∪v∈V ′′Av, so that
W ′ = ∪v∈V ′′NH (Av, W ) = NH(A, W ), and, for each v ∈ V ′′, |Av| = r, and |W ′| ≤ |Av|2 = r2. As
|A| = r|V ′′| = r3, and |NH (A, W )| = |W ′| ≤ r2, A does not expand well into W in H, and hence
must expand in H − W by a factor of at least ε(|A|)/2. Again, we have that Av does not expand
in H − W by a factor of at least ε(|Av|)/10 and log |Av| ≈ log |A|, for each v ∈ V ′′. As before, this
gives a contradiction.

3 Preliminary expansion results

In this section we cover the preliminary results on expansion that we use in Section 4. The
main results of this section are Lemmas 3.2, 3.4, 3.5, 3.11, 3.12 and 3.14 which we prove in Sec-
tions 3.1, 3.2, 3.3, 3.4, 3.5 and 3.6 respectively.

3.1 Expanding while avoiding sets

In an expander H, we often want to expand a vertex set A, while avoiding another set X. We can
do this if the set satisﬁes one of three conditions (matching the conditions A1–A3 in Lemma 3.2).

1. Firstly, if X is much smaller than A.

2. Secondly, if X is far enough (in graph distance) from A in H that A expands to become much
larger than X before it encounters X.

3. Finally, if X does not intersect too much with each sphere around A during the expansion.
That is, if NH(Bi
H−X(A)) does not intersect too much with X for each i ≥ 0.

For the last condition above, if Bi
H−X(A) grows with i, then we can permit the intersection
of NH(Bi
H−X (A)) with X to increase as i increases. This condition is formally captured in the
following notion, before we give our main lemma expanding a vertex set A while avoiding some
other vertex sets.

Deﬁnition 3.1. A vertex set A has k-limited contact with a vertex set X in a graph H if, for each
i ∈ N, |NH(Bi−1
H−X (A)) ∩ X| ≤ ki.

Lemma 3.2. Let 0 < ε1, ε2 < 1 and k ∈ N. There is some d0 = d0(ε1, ε2, k) for which the following
holds for each n ≥ d ≥ d0.
Suppose H is an n-vertex (ε1, ε2d)-expander. Let m = 16
ε1 log3 n and ℓ0 = (log log n)5. Let
A ⊆ V (H) with |A| ≥ ε2d/2 and let X, Y, Z ⊆ V (H) \ A be such that the following hold.

A1 |X| ≤ |A|ε(|A|)/4.
 11

A2 Bℓ0
H−X−Z (A) ∩ Y = ∅ and |Y | ≤ m300k.

A3 A has k-limited contact with Z in H.

Then,

(i) |Bℓ0
H−X−Y −Z (A)| > m400k, and

(ii) |Bm
H−X−Y −Z (A)| > n/2.

Proof. We ﬁrst prove (i). Note that, by A2, we have Bℓ0
H−X−Y −Z (A) = Bℓ0
H−X−Z (A). Let F =
H − X − Z, and suppose that |Bℓ0
F (A)| ≤ m400k, for otherwise (i) holds. We will show the following
claim.

Claim 3.3. For each 0 ≤ r ≤ ℓ0 − 1,

|NF (Br
F (A))| ≥ 1
4 |Br
F (A)| · ε(|Br
F (A)|). (4)

Given Claim 3.3, we reach a contradiction as follows, and thus (i) must hold. For each 0 ≤ r < ℓ0,
we have |Br
F (A)| ≤ |Bℓ0
F (A)| ≤ m400k, and hence, as n ≥ d ≥ d0(ε1, ε2, k) is large,

ε(|Br
F (A)|) ≥ ε(m400k) = ε1
log2(15m400k/ε2d) ≥ 4
(log log n)3 .

Therefore, for each 0 ≤ r < ℓ0, by Claim 3.3,

|Br+1
F (A)| = |Br
F (A)| + |NF (Br
F (A))| ≥ (1 + ε(|Br
F (A)|)
4
 ) |Br
F (A)| ≥ (
1 + 1
(log log n)3
 ) |Br
F (A)|.

Therefore,

|Bℓ0
F (A)| ≥ (1 + 1
(log log n)3
 )ℓ0 |A| ≥ exp ( ℓ0
2(log log n)3
 ) = exp ( (log log n)2

2
 ) = ω(m400k), (5)

which contradicts our assumption that (i) does not hold as n ≥ d0(ε1, ε2, k) is large. For (i), it is
left then to prove Claim 3.3.

Proof of claim. We prove this by induction on r. For the base case r = 0, as x · ε(x) increases in
x ≥ ε2d/2, we have
 |A|ε(|A|) ≥ ε2d
2 · ε(ε2d/2) = ε1ε2d
2 log2(15/2) ≥ 4k,

where we have used that d ≥ d0(ε1, ε2, k) is large. In combination with A3, we have |NH (A) ∩ Z| ≤
k ≤ |A|ε(|A|)/4. Thus, from the expansion of H and A1, we have

|NF (A)| ≥ |NH (A)| − |NH (A) ∩ X| − |NH (A) ∩ Z| ≥ (1 − 1
4 − 1
4
 ) |A|ε(|A|) ≥ 1
4 |A|ε(|A|).

Suppose then that r ≥ 1 and that (4) holds with r replaced by r′ for each 0 ≤ r′ < r. Then,
similarly to (5),
 |Br
F (A)| ≥ |A| (1 + ε(|Br
F (A)|)
4
 )r . (6)

12

Now, let α be deﬁned by |Br
F (A)| = αε2d/15. As |Br
F (A)| ≥ |A| ≥ ε2d/2, α ≥ 15/2, and thus
ε(|Br
F (A)|) = ε1/ log2 α ≤ 1/2. Therefore, from (6), we have

α ≥ |Br
F (A)|
|A| ≥ (1 + ε1
4 log2 α
 )r ≥ exp ( ε1r
8 log2 α
 ) ,

which gives r ≤ 8 log3 α/ε1. As α ≥ 15/2, we have log5 α/α ≤ 100, so that

r + 1 ≤ 2r ≤ 1600α
ε1 log2 α = 1600α · ε(|Br
F (A)|)
ε2
1 = 1600 · 15
ε2d · ε2
1 · |Br
F (A)|ε(|Br
F (A)|). (7)

As d ≥ d0(ε1, ε2, k) is large, by A3, we have

|NH (Br
H−Z (A)) ∩ Z)| ≤ k(r + 1) (7)
≤ k · 1600 · 15
ε2d · ε2
1 · |Br
F (A)|ε(|Br
F (A)|) ≤ 1
4 |Br
F (A)|ε(|Br
F (A)|). (8)

As x · ε(x) increases with x ≥ ε2d/2, by A1 we have |X| ≤ |A|ε(|A|)/4 ≤ |Br
F (A)|ε(|Br
F (A)|)/4.
Therefore, using the expansion of H, we have

|NF (Br
F (A))| ≥ |NH (Br
F (A))| − |NH (Br
F (A)) ∩ X)| − |NH(Br
H−Z (A)) ∩ Z)|

≥ |NH (Br
F (A))| − |X| − |NH (Br
H−Z (A)) ∩ Z)| (8)
≥ 1
4 |Br
F (A)| · ε(|Br
F (A)|),

and hence (4) holds for r. ■

We now prove (ii). Suppose, for contradiction, that |N m
H−X−Y −Z(A)| ≤ n/2. Let F ′ = H −
X − Y − Z, and for each ℓ0 ≤ r ≤ m − 1, let Ar = Br
F ′(A), so that, by (i), we have |Ar| ≥ m400k.
Now, as n ≥ d0(ε1, ε2, k) is large,

ε(|Ar|) ≥ ε(n) ≥ ε1/ log2 n ≥ 1/m, (9)

and thus |Ar|ε(|Ar|)/4 ≥ m400k−1/4 ≥ km300k. Therefore, by A2, |Ar|ε(|Ar|)/4 ≥ |Y | and, by A3,

|NH (Ar) ∩ Z| ≤ |NH(Br
H−Z (A)) ∩ Z| ≤ k(r + 1) ≤ km ≤ |Ar|ε(|Ar|)/4.

As |Ar| ≥ |A| and x · ε(x) increases with x ≥ ε2d/2, we have, by A1, that |Ar|ε(|Ar|)/4 ≥ |X|. In
total, then,
 |X| + |Y | + |NH(Ar) ∩ Z| ≤ 3
4 |Ar|ε(|Ar|). (10)

Thus, using the expansion of H, we have

|NF ′(Ar)| ≥ |NH (Ar)| − |X ∪ Y | − |NH (Ar) ∩ Z)| (10)
≥ 1
4 |Ar| · ε(|Ar|) (9)
≥ ε1|Ar|
4 log2 n .

As this holds for all r with ℓ0 ≤ r ≤ m − 1, we have

|Bm
F ′(A)| ≥ (1 + ε1
4 log2 n
 )m−ℓ0 |Aℓ0| ≥ (1 + ε1
4 log2 n
 )m/2

≥ exp ( ε1m
16 log2 n
 ) = exp(log n) > n/2,

a contradiction.
 13

3.2 Connecting sets with paths

Lemma 3.2 allows us to ﬁnd paths between sets A and B in an expander, as follows.

Lemma 3.4. For each 0 < ε1, ε2 < 1, there exists d0 = d0(ε1, ε2) such that the following holds for
each n ≥ d ≥ d0 and x ≥ 1. Let G be an n-vertex (ε1, ε2d)-expander with δ(G) ≥ d − 1.
Let A, B ⊆ V (G) with |A|, |B| ≥ x, and let W ⊆ V (G) \ (A ∪ B) satisfy |W | log3 n ≤ 10x. Then,
there is a path from A to B in G − W with length at most 40
ε1 log3 n.

Proof. If x ≥ ε2d/2, then, as n ≥ d ≥ d0(ε1, ε2) is large, we have

x · ε(x)
4 = ε1x
4 log2(15x/ε2d) ≥ ε1x
4 log2(15n) ≥ ε1x
8 log2 n ≥ 10x
log3 n ≥ |W |. (11)

Therefore, letting m = 16
ε1 log3 n, by Lemma 3.2 applied with X = W and Y = Z = ∅, we have
|Bm
G−W (A)|, |Bm
G−W (B)| > n/2. Thus, there is a path from A to B in G − W with length at most
2m ≤ 40
ε1 log3 n.
Suppose then that x < ε2d/2 ≤ d/2. Let x′ = min{|A∪NG−W (A)|, |B∪NG−W (B)|}. As x < d/2
and A, B ̸= ∅, we have x′ ≥ δ(G) − |W | ≥ d − 1 − 10d/ log3 n ≥ d/2 ≥ ε2d/2, as n ≥ d ≥ d0(ε1, ε2)
is large. Therefore, as above, there is a path from A ∪ NG−W (A) to B ∪ NG−W (B) in G − W with
length at most 2m, and hence a path with length at most 2m + 2 ≤ 40
ε1 log3 n between A and B in
G − W , as required.

3.3 Expansion of sets of lower degree vertices

The following lemma is the key new technicality that allows our constructions, as discussed in
Section 2.6. We then develop it for convenience of use to get Lemma 3.7.

Lemma 3.5. For any 0 < ε1, ε2 < 1, there exists d0 = d0(ε1, ε2) such that the following holds for
each n ≥ d ≥ d0. Suppose that G is an n-vertex bipartite (ε1, ε2d)-expander with δ(G) ≥ d.
Let U ⊆ V (G) satisfy |U | ≤ exp((log log n)2), and let K = G − U . Let I be any set and
Vi ⊆ V (K), i ∈ I, be pairwise disjoint sets such that, for each i ∈ I,

B1 ε2d ≤ |Vi| ≤ exp((log log n)2),

B2 |NK (Vi)| ≤ 5|Vi|
log10 |Vi| , and

B3 dG(v, U ) ≤ d/2 for each v ∈ Vi.

Then, | ∪i∈I Vi| < n1/8.

Proof. Suppose to the contrary that | ∪i∈I Vi| ≥ n1/8 and let D = exp((log log n)2). Let I1 = {i ∈
I : |Vi| ≥ (log n)1/10} and I2 = I \ I1.
First, suppose that | ∪i∈I1 Vi| ≥ n1/8/2. Then, as |Vi| ≤ D for each i ∈ I, |I1| ≥ n1/9 ≥ D2.
Let I0 ⊆ I1 be a subset of I1 of size D2, and let W = ∪i∈I0Vi. Now, for each i ∈ I0, log |Vi| ≥
(log log n)/10, while |W | ≤ |I0|D ≤ D3, so that log |W | ≤ 3(log log n)2. Thus, we have

|NG(W )| ≤ |U | + |NK (∪i∈I0Vi)| ≤ D + ∑

i∈I0 |NK (Vi)| B2
≤ D + ∑

i∈I0
 5|Vi|
log10 |Vi|

≤ D + ∑

i∈I0
 5(10)10|Vi|
(log log n)10 = D + 5(10)10|W |
(log log n)10 < ε1|W |
log3 |W | ≤ ε(|W |)|W |,

14

as |W | ≥ D2, log |W | ≤ 3(log log n)2 and n ≥ d0(ε1, ε2) is large. As |W | ≤ D3, this contradicts the
fact that G is an (ε1, ε2d)-expander. Thus, we have | ∪i∈I1 Vi| ≤ n1/8/2.
Therefore, we have | ∪i∈I2 Vi| ≥ n1/8/2. Thus, I2 ̸= ∅, and hence by deﬁnition, taking any
i ∈ I2, we have ε2d ≤ |Vi| ≤ (log n)1/10 so that d ≤ (log n)1/10/ε2. Furthermore, by the pigeonhole
principle there must be some r ∈ N with ε2d ≤ r ≤ (log n)1/10 for which there are at least
|I2|/(log n)1/10 ≥ | ∪i∈I2 Vi|/((log n)1/10)2 ≥ n1/9 indices i ∈ I2 with |Vi| = r. Taking such an r, let
I3 = {i ∈ I2 : |Vi| = r}, so that |I3| ≥ n1/9.
Now, for each i ∈ I3, as dG(v, U ) ≤ d ≤ r/ε2 for each v ∈ Vi, we have |NG(Vi) ∩ U | ≤ r2/ε2 ≤
(log n)1/4, as n ≥ d0(ε1, ε2) is large. As |U | ≤ D, the number of sets of size at most (log n)1/4 in U
is at most (log n)1/4
∑

i=0
 (D
i
 ) ≤ (log n)
1/4D(log n)1/4 ≤ exp((log n)
1/3).

Therefore, there must be at least n1/9/ exp((log n)1/3) ≥ n1/10 indices i ∈ I3 for which NG(Vi) ∩ U
is the same set, Z say. Taking any i ∈ I3, note that, by B3, |Z| = |NG(Vi) ∩ U | ≤ dr ≤ r2/ε2. Let
I4 be a set of r2 ≤ (log n)1/5 indices i ∈ I3 for which NG(Vi) ∩ U = Z.
Let Y = ∪i∈I4Vi, so that NG(Y ) ∩ U = Z and |Y | = r|I4| = r3. Then, as d ≥ d0(ε1, ε2) is large
and r ≥ ε2d, we have

|NG(Y )| ≤ |Z| + ∑

i∈I4 |NK (Vi)| B2
≤ r2

ε2 + 5r3

log10 r ≤ ε1r3

log3(r3) = ε1|Y |
log3 |Y | < ε(|Y |)|Y |,

contradicting that G is an (ε1, ε2d)-expander.

Lemma 3.5 is used three times, each in a similar situation, so for its application, we prove
Lemma 3.7 below. In this lemma, with r = n1/8, we have sets Ai, i ∈ [r], and wish to ﬁnd some set
Aj which expands while avoiding some set Bj ∪ Cj which depends on j, as well as avoiding some
large common set U . To ﬁnd such an Aj, we assume for contradiction that no such set Aj exists,
before recording as Vi the ﬁrst ball around Ai which does not expand nicely. Applying Lemma 3.5
to the sets Vi, i ∈ [r], will then reach a contradiction.
To prove the lemma, we will also use the following very simple proposition.

Proposition 3.6. For each i, ℓ ≥ 1, we have ℓ2−i − (ℓ − 1)2−i ≤ ℓ−1+2−i.

Proof. Not that this is true for any ℓ with equality if i = 0. Assume then for induction that i > 0
and it is true for ℓ with i replaced with i − 1. We have

ℓ−1+2−(i−1) ≥ ℓ2−(i−1) − (ℓ − 1)
2−(i−1) = (ℓ2−i + (ℓ − 1)
2−i )(ℓ2−i − (ℓ − 1)
2−i ) ≥ ℓ2−i(ℓ2−i − (ℓ − 1)
2−i ),

and therefore ℓ2−i − (ℓ − 1)2−i ≤ ℓ−1+2−(i−1)−2−i = ℓ−1+2−i, as required.

Lemma 3.7. For each 0 < ε1 < 1, 0 < ε2 < 1/5 and k ∈ N, there exists d0 = d0(ε1, ε2, k) such that
the following holds for each n ≥ d ≥ d0. Suppose that G is an n-vertex bipartite (ε1, ε2d)-expander
with δ(G) ≥ d. Let U ⊆ V (G) satisfy |U | ≤ exp((log log n)2). Let r = n1/8 and ℓ0 = (log log n)20.
Suppose (Ai, Bi, Ci), i ∈ [r], are such that the following hold for each i ∈ [r].

C1 |Ai| ≥ d0.
 15

C2 Bi ∪ Ci and Ai are disjoint sets in V (G) \ U , with |Bi| ≤ |Ai|/ log10 |Ai|.

C3 Ai has 4-limited contact with Ci in G − U − Bi.

C4 Each vertex in Bℓ0
G−U −Bi−Ci(Ai) has at most d/2 neighbours in U .

C5 For each j ∈ [r] \ {i}, Ai and Aj are at least a distance 2ℓ0 apart in G − U − Bi − Ci − Bj − Cj.

Then, for some i ∈ [r], |Bℓ0
G−U −Bi−Ci(Ai)| ≥ logk n.

Proof. Suppose, for contradiction, that |Bℓ0
G−U −Bi−Ci(Ai)| < logk n for each i ∈ [r]. Let α = 1/16,
and note that exp(ℓα
0 ) = exp((log log n)1.25) > logk n, as n ≥ d0(ε1, ε2, k) is large, and hence
|Bℓ0
G−U −Bi−Ci(Ai)| < exp(ℓα
0 ) for each i ∈ [r]. Therefore, for each i ∈ [r], we can let ℓi be the
smallest ℓ ∈ [ℓ0] such that |Bℓ
G−U −Bi−Ci(Ai)| ≤ exp(ℓα). (12)

For each i ∈ [r], let Vi = Bℓi−1
G−U −Bi−Ci(Ai). By the deﬁnition of ℓi, we have that

|Vi| ≥ exp((ℓi − 1)
α) and |BG−U −Bi−Ci(Vi)| ≤ exp(ℓα
i ). (13)

Claim 3.8. For each i ∈ [r], we have |NG−U (Vi)| ≤ 5|Vi|
log10 |Vi| .

Proof of claim. Fix i ∈ [r]. By Proposition 3.6, we have ℓα
i −(ℓi−1)α ≤ ℓ−1+α
i ≤ (ℓα
i )−10. Note that,
as d ≥ d0(ε1, ε2, k) is large, we have that ℓi ≥ log d0 is large by C1 and (12). As exp(1/x) − 1 ≤ 2/x
for large x > 0, we thus have

exp(ℓα
i − (ℓi − 1)
α) − 1 ≤ exp((ℓα
i )
−10) − 1 ≤ 2/(ℓα
i )
10. (14)

Then,
 |NG−U −Bi−Ci(Vi)| ≤ |BG−U −Bi−Ci(Vi)| − |Vi| = ( |BG−U −Bi−Ci(Vi)|
|Vi| − 1
) |Vi|

(13)
≤ ( exp(ℓα
i )
exp((ℓi − 1)α) − 1
) |Vi| (14)
≤ 2|Vi|
(ℓα
i )10
 (13)
≤ 2|Vi|
log10 |Vi| . (15)

Now, due to C3, we have

|NG−U −Bi(Vi) ∩ Ci| ≤ 4ℓi (13)
≤ 4(log16 |Vi| + 1) ≤ |Vi|
log10 |Vi| , (16)

as, by C1, |Vi| ≥ |Ai| ≥ d0(ε1, ε2, k) is large. Therefore, as

|NG−U (Vi)| ≤ |NG−U −Bi−Ci(Vi)| + |Bi| + |NG−U −Bi(Vi) ∩ Ci|,

the claim follows from (15), (16), |Ai| ≤ |Vi| and C2. ■

We now check the conditions to appy Lemma 3.5 to the sets Vi, i ∈ [r]. By C5, the sets Vi, i ∈ [r],
are pairwise disjoint. Note that |Vi| ≥ |BG−U −Bi−Ci(Ai)| ≥ ε2d. Indeed, if |Ai| ≥ ε2d, this holds
clearly; if |Ai| < ε2d, then by C2, C3 and C4, |BG−U −Bi−Ci(Ai)| ≥ δ(G) − |Bi| − 4 − d/2 ≥ ε2d.
Thus, for each i ∈ [r], ε2d ≤ |Vi| < logk n ≤ exp((log log n)2). By Claim 3.8, if K = G − U ,
then |NK (Vi)| ≤ 5|Vi|/ log10 |Vi| for each i ∈ [r]. By C4, for each i ∈ [r] and v ∈ Vi, we have
dG(v, U ) ≤ d/2. Therefore, by Lemma 3.5, we have r ≤ | ∪i∈[r] Vi| < n1/8, a contradiction.

16

3.4 Disjoint vertex expansions

In order to connect structures together in an expander, we typically ﬁnd the structures we want
with an extra subgraph attached to the vertex, v say, we wish to make connections from. This
extra subgraph, F say, should have enough vertices that either Lemma 3.2 or Lemma 3.4 can be
used to connect V (F ) to another vertex set while avoiding some structures that we have already
found. The graph F should also have a short path from v to any other vertex in F , so that a
path to V (F ) can be extended to one to v without many additional vertices. This motivates the
following deﬁnition.

Deﬁnition 3.9. Given a vertex v in a graph F , F is a (D, m)-expansion of v if |F | = D and v is
a distance at most m in F from any other vertex of F .

Before we ﬁnd vertex expansions, we ﬁrst prove the following simple proposition which ﬁnds a
smaller expansion within any expansion.

Proposition 3.10. Let D, m ∈ N and 1 ≤ D′ ≤ D. Then, any graph F which is a (D, m)-expansion
of v contains a subgraph which is a (D′, m)-expansion of v.

Proof. We prove this for each 1 ≤ D′ ≤ D by induction on D′ for D′ = D, D − 1, . . . , 1. Note
that F demonstrates this is true for D′ = D. Suppose then it is true for D′ ≥ 2, and let F ′ with
|F ′| = D′ be a (D′, m)-expansion of v. Let w ∈ V (F ′) maximise the graph distance from v to w in
F ′. As D′ ≥ 2, v ̸= w. Noting that F ′ − w is a (D′ − 1, m)-expansion of v completes the proof of
the inductive step, and hence the proposition.

We now give our lemma which ﬁnds vertex expansions. Its proof is diﬀerent according to
whether there are many vertices in the graph of high degree (Case I) or not (Case II). We will
construct structures using short cycles later, so for the application of this lemma we need to ﬁnd
vertex expansions while avoiding a short cycle as much as possible.

Lemma 3.11. For each k ∈ N and any 0 < ε1, ε2 < 1, there exists d0 = d0(ε1, ε2, k) such that the
following holds for each n ≥ d ≥ d0.
Suppose that G is an n-vertex bipartite (ε1, ε2d)-expander with δ(G) ≥ d − 1. Let m = 40
ε1 log3 n.
Let C be a shortest cycle in G, and let x1, . . . , xk be distinct vertices in G. For each i, j ∈ [k], let
Di,j ∈ [1, log5k n].
Then, there are graphs Fi,j ⊆ G, i, j ∈ [k], such that the following hold.

• For each i, j ∈ [k], Fi,j is a (Di,j, 5m)-expansion around xi which contains no vertices other
than xi in V (C) ∪ {x1, . . . , xk}.

• The sets V (Fi,j) \ {xi}, i, j ∈ [k], are pairwise disjoint.

Proof. Note ﬁrst that, as δ(G) ≥ d − 1, |C| ≤ 2 log n/ log(d − 1). Let D = log5k n. By Propo-
sition 3.10, we can assume that Di,j = D for all i, j ∈ [k]. Let r = k2 and let L be the set of
vertices in G with degree at least ∆ = D2. We will split into two cases depending on whether
|L \ V (C)| ≥ 2r or not.

Case I: First suppose that there are 2r vertices v1, . . . , v2r ∈ L \ V (C). Assume, by relabelling if
necessary, that V := {v1, . . . , vr} is disjoint from X := {x1, . . . , xk}.
Let P be a maximal collection of paths in G from X to V such that

17

• each path in P has length at most 3m and internal vertices in V (G) \ (V (C) ∪ X ∪ V ),

• the paths in P are vertex disjoint outside of X, and

• there are at most k paths containing each vertex in X.

Subject to |P| being maximal, suppose that ∑P ∈P ℓ(P ) is minimised. Note that, as there are at
most k paths containing each vertex in X, |P| ≤ k2.
Now, suppose for contradiction that there is some x ∈ X which is in fewer than k paths in P,
and so |P| < k2. Let U = (V ∪ X ∪ V (P) ∪ V (C)) \ {x}. For each path P ∈ P and ℓ ∈ N, at most
ℓ + 1 vertices in NG(Bℓ−1
G−U (x)) can lie on P , otherwise we can ﬁnd a shorter path than P from x
to V (P ) ∩ V in G − (U \ V (P )). Swapping P for this shorter path contradicts the minimality of∑P ′∈P ℓ(P ′). Therefore, for each ℓ ∈ N,

|NG(Bℓ−1
G−U (x)) ∩ V (P)| ≤ ∑

P ∈P |NG(Bℓ−1
G−U (x)) ∩ V (P )| ≤ (ℓ + 1)|P| ≤ (ℓ + 1)k2. (17)

Furthermore, for any vertex v and any integer ℓ ∈ N, at most 2ℓ + 1 vertices in Bℓ
G(v) can lie on
C, as C is a shortest cycle in G. Therefore,

|NG(Bℓ−1
G−U (x)) ∩ U | ≤ |V ∪ X| + |NG(Bℓ−1
G−U (x)) ∩ V (P)| + |NG(Bℓ−1
G−V (C)+x(x)) ∩ V (C)|

(17)
≤ 2k2 + (ℓ + 1)k2 + |Bℓ
G(x) ∩ V (C)| ≤ (ℓ + 3)k2 + (2ℓ + 1) ≤ 10ℓk2.

Thus, {x} has 10k2-limited contact with U in G, so that BG−U (x) has 20k2-limited contact with U
in G. We also have |BG−U (x)| ≥ δ(G) − 10k2 ≥ d/2 ≥ ε2d/2. Therefore, applying Lemma 3.2 with
(A, X, Y, Z, k)3.2 = (BG−U (x), ∅, ∅, U, 20k2), we get that |Bm+1
G−U (x)| = |Bm
G−U (BG−U (x))| > n/2.
Note that, by the choice of P, each P ∈ P has a distinct vertex in V . As |P| < k2, we can
choose a vertex v ∈ V \ V (P). Note that |U | ≤ 2k2 + k2 · (3m + 1) + 2 log n/ log(d − 1) ≤ log4 n.
As dG(v) ≥ ∆ = log10k n ≥ |U | log3 n/10 and |Bm+1
G−U (x)| > n/2 ≥ |U | log3 n/10, using Lemma 3.4,
we can connect Bm+1
G−U (x) and NG(v) with a path of length at most m in G − U , which extends in
Bm+1
G−U (x) ∪ {v} to an x, v-path in G − U with length at most 3m, contradicting the maximality
of P.
Therefore, each vertex in X is in exactly k paths in P. Label the paths in P as Pi,j, i, j ∈ [k],
so that xi is an endvertex of Pi,j, and let vi,j be the endvertex of Pi,j in V . Greedily, using that
|NG(vi,j) \ (V ∪ X ∪ V (C) ∪ V (P))| ≥ ∆ − log4 n ≥ k2D for each i, j ∈ [k], pick disjoint sets
Ai,j ⊆ NG(vi,j) \ (V ∪ X ∪ V (C) ∪ V (P)), i, j ∈ [k], with size D − |Pi,j|. Then Fi,j = G[Ai,j] ∪ Pi,j,
i, j ∈ [k], are easily seen to be the (D, 5m)-expansions we require.

Case II: Suppose then that |L \ V (C)| < 2r. Relabelling if necessary, let 0 ≤ k′ ≤ k be such that
{x1, . . . , xk}\L = {x1, . . . , xk′}. Let G′ = G− L, X = {x1, . . . , xk′}, r′ = k′k and ℓ0 = 2(log log n)5.
Let s ≤ r′ be the largest integer for which there are vertices w1, . . . , ws ∈ V (G′) such that

• the sets B5ℓ0
G′ (wi), i ∈ [s], X and V (C) \ L are all pairwise disjoint.

Suppose s < r′. Then, we must have V (G′) = B10ℓ0
G′ (({w1, . . . , ws} ∪ X ∪ V (C)) \ L). However,
as ∆(G′) ≤ ∆ = D2 and |C| ≤ 2 log n/ log(d − 1) ≤ 2 log n,

|G
′| = |B10ℓ0
G′ (({w1, . . . , ws}∪ X ∪ V (C))\L)| ≤ 2·(r′ + k′ + 2 log n)·∆10ℓ0 ≤ exp((log log n)
7) < n/2,

18

contradicting |G′| ≥ n − |L \ V (C)| − |C| ≥ n − 2r − 2 log n ≥ n/2. Therefore, s = r′.
Now, ﬁxing an arbitrary i ∈ [r′], similarly to before, for each ℓ ∈ N at most 2ℓ + 1 vertices in
Bℓ
G(wi) can lie on C, otherwise there is a shorter cycle in G than C. Thus,

|BG′−V (C)(wi)| ≥ δ(G) − |L \ V (C)| − 3 ≥ δ(G) − 2r − 3 ≥ d/2, (18)

and, for each ℓ ∈ N,

|NG(Bℓ−1
G−V (C)(BG′−V (C)(wi))) ∩ V (C)| ≤ |Bℓ+1
G (wi) ∩ V (C)| ≤ 2ℓ + 3 ≤ 5ℓ.

Therefore, BG′−V (C)(wi) has 5-limited contact with V (C) in G. Let z = |BG′−V (C)(wi)|, and
note that, as |L \ V (C)| ≤ 2r = 2k2 and, by (18), z ≥ d/2 ≥ d0(ε1, ε2, k)/2 is large, we have
that |L \ V (C)| ≤ ε(z)z/4. Thus, by Lemma 3.2 with (A, X, Y, Z, k)3.2 = (BG′−V (C)(wi), L \
V (C), ∅, V (C), k + 5) we get that |Bℓ0+1
G′−V (C)(wi)| ≥ D2 = ∆. Hence, by Proposition 3.10 we can

pick a subgraph Fi ⊆ G′ induced on a subset of Bℓ0
G′−V (C)(wi) which is a (∆, 2ℓ0)-expansion of wi.
Now, let P be a maximal collection of paths in G′ from X to V := ∪i∈[r′]V (Fi) such that

• each path in P has length at most 3m and internal vertices in V (G′) \ (V (C) ∪ X ∪ V ),

• the paths in P are vertex disjoint outside of X,

• at most one path in P has a vertex in V (Fi), for each i ∈ [r′], and

• there are at most k paths containing each vertex in X.

Subject to |P| being maximal, suppose that ∑P ∈P ℓ(P ) is minimised.
Suppose again there is some x ∈ X in fewer than k paths in P and let U = (L ∪ X ∪ V (P) ∪
V (C)) \ {x}. As in Case I, by the minimality of ∑P ′∈P ℓ(P ′), for each path P ∈ P and ℓ ∈ N, at
most ℓ + 1 vertices in NG(Bℓ−1
G−U (x)) can lie on P . Therefore, for each ℓ ∈ N,

|NG(Bℓ−1
G−U (x)) ∩ V (P)| ≤ ∑

P ∈P |NG(Bℓ−1
G−U (x)) ∩ V (P )| ≤ (ℓ + 1)|P| ≤ (ℓ + 1)k2.

Again, for any integer ℓ ∈ N, at most 2ℓ + 1 vertices in Bℓ
G(x) can lie on C, as C is a shortest cycle
in G. Thus,

|NG(Bℓ−1
G−U (x)) ∩ U | ≤ |X ∪ (L \ V (C))| + |NG(Bℓ−1
G−U (x)) ∩ V (P)| + |Bℓ
G(x) ∩ V (C)|

≤ k + 2r + (ℓ + 1)k2 + (2ℓ + 1) ≤ 10ℓk2.

Therefore, {x} has 10k2-limited contact with U in G, and so BG−U (x) has 20k2-limited contact
with U in G. Furthermore, by the choice of the wi, Bℓ0
G−U (x) ∩ V = ∅, thus

|BG−U −V (x)| = |BG−U (x)| ≥ d − 10k2 ≥ d/2.

We also have that |V | ≤ k2∆ = k2 log10k n. Therefore, by Lemma 3.2 with (A, X, Y, Z, k)3.2 =
(BG−U (x), ∅, V, U, 20k2), |Bm+1
G−U −V (x)| > n/2.
By the choice of P, each P ∈ P has exactly one vertex in V (Fi) for some i ∈ [r′]. As |P| <
k′k = r′, there is some j ∈ [r′] such that V (P) has no vertex in V (Fj ). Now, the vertices wi,
i ∈ [r′], are pairwise at least 10ℓ0-far in G′, and Fi is a (∆, ℓ0)-expansion around wi. Therefore,

19

the subgraphs Fi, i ∈ [r′], are pairwise at least 8ℓ0-far from each other in G′, so that Fj is at least
8ℓ0-far from V \ V (Fj ).
Now, as |U | ≤ |X| + |L \ V (C)| + |C| + |V (P)| ≤ k + 2r + 2 log n + (3m + 1)r ≤ log4 n, we
have |Fj| = ∆ ≥ m|U |. As L ̸= V (G), we have ∆ > δ(G) ≥ ε2d, so that |Fj| ≥ ε2d. Therefore, by
Lemma 3.2 with (A, X, Y, Z, k)3.2 = (V (Fj), U, V \ V (Fj ), ∅, k), we have

|Bm
G−U −(V \V (Fj))(V (Fj))| > n/2.

Thus, as |Bm+1
G−U −V (x)| > n/2, there is a path from {x} to V (Fj ) in G′ with length at most 3m
which is internally disjoint from V (C) ∪ X ∪ V . This contradicts the maximality of P.
Therefore, each vertex in X is in exactly k paths in P. Label the paths in P with Pi,j, i ∈ [k′]
and j ∈ [k], and graphs Fi′, i′ ∈ [r′], as F ′
i,j, i ∈ [k′] and j ∈ [k], so that, for each i ∈ [k′] and
j ∈ [k], Pi,j is a path from xi to F ′
i,j. Recall that, for a path P , we write ℓ(P ) for its length. Note
that Pi,j ∪ F ′
i,j is a (|Pi,j ∪ F ′
i,j|, ℓ(Pi,j) + 2ℓ0)-expansion of xi, for each i ∈ [k′] and j ∈ [k]. For each
i ∈ [k′] and j ∈ [k], apply Proposition 3.10 to obtain a (D, 5m)-expansion Fi,j ⊆ Pi,j ∪ F ′
i,j around
xi. Lastly, for each k′ + 1 ≤ i ≤ k and j ∈ [k], as xi ∈ L we can greedily pick pairwise disjoint
(D, 1)-expansions Fi,j induced on a subset of NG(xi) \ (V (C) ∪ (∪i′∈[k′],j′∈[k]V (Fi′,j′))).

3.5 Enlarging vertex expansions

In this section, we take up to 4 disjoint vertex expansions, and expand them disjointly to get larger
vertex expansions around the same vertices (see Lemma 3.13). This enlargement allows us to later
connect vertex expansions with very long paths, as our path lengths need to be smaller than the
expansions (see Section 3.6).
We ﬁrst show for Lemma 3.12 that we can always ﬁnd a linear size vertex set with polyloga-
rithmic diameter in G while avoiding an arbitrary set of up to Θ(n/ log2 n) vertices. This is used
for Lemma 3.13 and Lemma 3.14, as well as later in Section 4.2

Lemma 3.12. For any 0 < ε1, ε2 < 1, there exists d0 = d0(ε1, ε2) such that the following holds for
each n ≥ d ≥ d0. Suppose that G is an n-vertex bipartite (ε1, ε2d)-expander with δ(G) ≥ d and let
m = 50
ε1 log3 n.
For any set W ⊆ V (G) with |W | ≤ ε1n/100 log2 n, there is a set B ⊆ G − W with size at
least n/25 and diameter at most 2m, and such that G[B] is a (D, m)-expansion around some vertex
v ∈ B for D = |B|.

Proof. Let ℓ0 = 50
ε1 log2 n. Suppose that G and W ⊆ V (G) satisfy the conditions in the lemma and
let G′ = G − W . Take the largest integer r ≤ log n such that there is a set of at most 1 + n/(10 · 4r )
vertices V ⊆ V (G′) with |Bℓ0r
G′ (V )| ≥ n/25. Note that such a set of vertices exists for r = 0, as
|G′| ≥ n − ε1n/100 log2 n ≥ n/25 and n ≥ d0(ε1, ε2) is large. Suppose, for contradiction, that
|V | > 1, and hence, that r ≤ log n − 1.
Let A = Bℓ0r
G′ (V ). As |W | ≤ ε1n/100 log2 n ≤ ε1|A|/4 log2 n, for each ℓ with |Bℓ
G′(A)| < n/2,
we have, by the expansion property of G, and as ε(|Bℓ
G′ (A)|) ≥ ε(n) ≥ ε1/ log2 n,

|NG′(Bℓ
G′(A))| ≥ |NG(Bℓ
G′(A))| − |W | ≥ ε1
log2 n · |Bℓ
G′(A)| − ε1|A|
4 log2 n ≥ ε1
2 log2 n · |Bℓ
G′(A)|,

20

so that |Bℓ+1
G′ (A)| ≥ (1 + ε1/2 log2 n)|Bℓ
G′(A)|. If |Bℓ0
G′(A)| < n/2, then

|Bℓ0
G′(A)| ≥ (1 + ε1
2 log2 n
 )ℓ0 |A| ≥ ε1ℓ0
2 log2 n · n
25 ≥ n/2,

a contradiction. Therefore, we have

|Bℓ0(r+1)
G′ (V )| = |Bℓ0
G′(A)| ≥ n/2.

Consequently, by averaging, there exists a set of at most ⌈|V |/12⌉ vertices V ′ ⊆ V such that
|Bℓ0(r+1)
G′ (V ′)| ≥ |Bℓ0(r+1)
G′ (V )|/12 ≥ n/25. Noting that, as |V | ≥ 2,

⌈|V |/12⌉ ≤ 1 + (|V | − 1)/12 ≤ 1 + n/(10 · 4
r+1),

this contradicts the maximality of r.
Therefore, we have |V | = 1. That is, there is some vertex v ∈ V (G′) with |Bℓ0r
G′ (v)| ≥ n/25.
Letting B = Bℓ0r
G′ (v), we have that |B| ≥ n/25 and B has diameter at most 2ℓ0r ≤ 100
ε1 log3 n = 2m,
as required, noting that G[B] is a (D, m)-expansion around v for D = |B|.

The large vertex sets with small diameter found in Lemma 3.12 are large vertex expansions
around some vertex. To ﬁnd large vertex expansions around particular vertices, which themselves
sit in smaller vertex expansions, we take disjointly many large vertex expansions, then expand and
connect the smaller vertex expansions to the larger ones, for the following lemma.

Lemma 3.13. For any 0 < ε1, ε2 < 1, there exists d0 = d0(ε1, ε2) such that the following holds for
each n ≥ d ≥ d0. Suppose that G is an n-vertex bipartite (ε1, ε2d)-expander with δ(G) ≥ d.
Let log10 n ≤ D ≤ n/ log10 n and m = 100
ε1 log3 n. Let A ⊆ V (G) satisfy |A| ≤ D/ log3 n. Let
F1, . . . , F4 ⊆ G − A be vertex disjoint subgraphs and v1, . . . , v4 be vertices such that, for each i ∈ [4],
Fi is a (D, m)-expansion of vi. Then, G − A contains vertex disjoint subgraphs F ′
1, . . . , F ′
4 such
that, for each i ∈ [4], F ′
i is an (n/m2, 3m)-expansion of vi.

Proof. Let W = V (F1) ∪ . . . ∪ V (F4) ∪ A so that |W | ≤ 5D ≤ 5n/ log10 n. Applying Lemma 3.12
iteratively 32m times, we can ﬁnd disjoint sets B1, . . . , B32m in G − W such that each Bi has
size n/m2 and diameter at most m. Note that this is possible, as after we have found Bi, where
i ∈ [32m], we have W ∪ (∪j∈[i]Bj) ≤ 5n/ log10 n + 32m · n/m2 ≤ ε1n/100 log2 n, as n ≥ d0(ε1, ε2)
is large. Lemma 3.12 and Proposition 3.10 then shows that G − W ∪ (∪j∈[i]Bj) contains a set with
n/m2 vertices and diameter at most m.
Next, take a maximal set I ⊆ [4] such that there are paths Pi,j, with i ∈ I and j ∈ [8m], and
distinct ki,j ∈ [32m], satisfying the following.

D1 Pi,j is a path from vi to Bki,j of length at most 2m.

D2 The sets V (Pi,j) \ V (Fi) are vertex disjoint across i ∈ I and j ∈ [8m].

D3 There is an ordering σ on I such that V (Pi,j) is disjoint from ∪i′∈[4]\I ′V (Fi′), where I ′ = {i′ ∈
I : σ(i′) ≤ σ(i)}.
 21

Suppose, for contradiction, that J := [4] \ I ̸= ∅, and let σ : I → [|I|] be an ordering for which
D3 holds. Let W ′ = A∪(∪i∈I,j∈[8m]V (Pi,j)). Take a maximal set K ⊆ [32m]\{ki,j : i ∈ I, j ∈ [8m]}
for which there are paths Pk, k ∈ K, with length at most m from ∪i∈J V (Fi) to Bk, which avoid
W ′ and which are vertex disjoint. Suppose, to contradict the maximality of K, that there is some
j′ ∈ [32m] \ {ki,j : i ∈ I, j ∈ [8m]}. Note that | ∪i∈J V (Fi)| ≥ D and |Bj′| = n/m2 ≥ D. Noting
that |W ′ ∪ (∪k∈KV (Pk))| ≤ D/ log3 n + 32m(2m + 1) ≤ 2D/ log3 n, by Lemma 3.4, there is a path
between ∪i∈J V (Fi) and Bj′ with length at most m which avoids W ′ ∪ (∪k∈KV (Pk)), contradicting
the maximality of K.
Therefore, we have K = [32m] \ {ki,j : i ∈ I, j ∈ [8m]}, and hence |K| = 32m − 8m|I| = 8m|J|.
Consequently, for some i′ ∈ J, there are at least 8m values of k ∈ K for which Pk has a vertex
in V (Fi′ ). Taking ki′,1, . . . , ki′,8m to be distinct such values of k, for each j ∈ [8m], as Fi′ is a
(D, m)-expansion of vi′, we can ﬁnd a path Pi′,j ⊆ Pki′,j ∪ Fi′ from vi′ to Bki′,j with length at most
2m. The paths Pi,j, i ∈ I ∪ {i′} and j ∈ [8m], satisfy D1–D3 (the last with the ordering σ extended
by setting σ(i′) = |I| + 1), contradicting the maximality of I.
Thus, we have I = [4]. By relabelling if necessary, assume from D3 that V (Pi,j) is disjoint
from V (Fi′ ) for each i′ > i and j ∈ [8m]. Now, for each 1 ≤ i ≤ 4, greedily select ri ∈ [8m] in
turn such that V (Pi,ri) ∪ Bki,ri has no vertices in ∪i′<iPi′,ri′ . Note that this is possible as, for each
i ∈ [4], ∪i′<iV (Pi′,ri′ ) contains at most 3(2m + 1) vertices, none of which are in V (Fi), and the sets
V (Pi,j) ∪ Bki,j , j ∈ [8m] are disjoint outside of V (Fi).
For each i ∈ [4], let F ′′
i = Pi,ri ∪ G[Bki,ri ]. Note that the subgraphs F ′′
i , i ∈ [4], are vertex
disjoint, and, as each set Bi, i ∈ [32m], has diameter at most m, for each i ∈ [4], F ′′
i is a (Di, 3m)-
expansion of vi for some Di ≥ n/m2. For each i ∈ [4], using Proposition 3.10, let F ′
i ⊆ F ′′
i be an
(n/m2, 3m)-expansion of vi, completing the proof.

3.6 Long paths between vertex expansions

Our goal now is, given some desired path length, to connect two vertices with an initial path with
close to this desired length. Section 4 then makes the ﬁne adjustment to this path so that it has
exactly the desired length. Given vertex expansions around the vertices to be connected, we ﬁnd
such an initial path, as follows.

Lemma 3.14. For any 0 < ε1, ε2 < 1, there exists d0 = d0(ε1, ε2) such that the following holds for
each n ≥ d ≥ d0. Suppose that G is an n-vertex bipartite (ε1, ε2d)-expander with δ(G) ≥ d.
Let log3 n ≤ D ≤ n/ log4 n and 300
ε1 log3 n ≤ m ≤ 3 log4 n. Suppose F1, F2 are vertex disjoint
(D, m)-expansions of vertices v1, v2 ∈ V (G) respectively. Suppose W ⊆ V (G) \ (V (F1) ∪ V (F2))
satisﬁes |W | ≤ D/ log3 n. Then, for any ℓ ≤ D/ log3 n, there is a v1, v2-path in G − W with length
between ℓ and ℓ + 5m.

Proof. Let (P1, v3, F3, P2, v4, F4) be such that ℓ(P1) + ℓ(P2) is maximised subject to the following
properties.

E1 For each i ∈ [2], Pi is a vi, vi+2-path in G − W .

E2 ℓ(P1) + ℓ(P2) ≤ ℓ + 2m.

E3 For each i ∈ {3, 4}, Fi is a (D, m)-expansion of vi in G − W with V (Fi) ∩ V (Pi−2) = {vi}.

E4 V (P1 ∪ F3) and V (P2 ∪ F4) are vertex disjoint.

22

Note that P1 = G[{v3}], v3 = v1, F3 = F1, P2 = G[{v4}], v4 = v2, F4 = F2 satisfy E1–E4, and
therefore such a sextuple (P1, v3, F3, P2, v4, F4) exists.
We claim that ℓ(P1) + ℓ(P2) ≥ ℓ. Suppose for contradiction that ℓ(P1) + ℓ(P2) < ℓ. Note that
|W ∪V (F3 ∪F4 ∪P1 ∪P2)| ≤ 3D +ℓ ≤ n/ log3 n. By Lemma 3.12, then, G−W −V (F3 ∪F4 ∪P1 ∪P2)
contains a set, B say, with size at least D and diameter at most m. Note furthermore that
|W ∪ V (P1) ∪ V (P2)| ≤ D/ log3 n + ℓ + 2 ≤ 10D/ log3 n. By Lemma 3.4, there is a path, Q′ say,
from B to V (F3) ∪ V (F4) which avoids (W ∪ V (P1) ∪ V (P2)) \ {v3, v4} and has length at most m.
Say without loss of generality that Q′ has endvertices v′′
3 ∈ V (F3) and v′
3 ∈ B. By E3 and E4, we
can extend Q′ in F3 to a v3, v′
3-path Q with length at most 2m which is vertex disjoint from P2
and P1 − v3.
Using Proposition 3.10, let F ′
3 ⊆ G[B] be a (D, m)-expansion around v′
3. Let P ′
1 = P1 ∪ Q and
note that, as v′
3 ∈ B and ℓ(Q) ≤ 2m, this is a v1, v′
3-path with length at least ℓ(P1) + 1 and at
most ℓ(P1) + 2m. Then, P ′
1, v′
3, F ′
3, P2, v4, F4 satisfy E1–E4 with P ′
1, v′
3, F ′
3 in place of P1, v3, F3,
and ℓ(P ′
1) + ℓ(P2) > ℓ(P1) + ℓ(P2), a contradiction. Therefore, ℓ(P1) + ℓ(P2) ≥ ℓ.
Now, as |W ∪ V (P1) ∪ V (P2)| ≤ 10D/ log3 n, by Lemma 3.4 there is a path, R say, from some
r1 ∈ V (F3) to some r2 ∈ V (F4) avoiding (W ∪ V (P1) ∪ V (P2)) \ {v3, v4} with length at most
m. For each i ∈ [2], let Qi be a path from vi+2 to ri in Fi+2 with length at most m. Then,
P1 ∪ Q1 ∪ R ∪ Q2 ∪ P2 is a v1, v2-path in G − W with length at least ℓ(P1) + ℓ(P2) ≥ ℓ and at most,
by E2, ℓ + 2m + 3m ≤ ℓ + 5m.

Combining Lemma 3.14 with our result on extending vertex expansions, we now convert Lemma 3.14
into the precise form we apply later. The following corollary ﬁnds not one but two paths, whose
combined length is close to some desired length. We later apply it so that these two paths connect
two vertices with a string of simple adjusters in the middle.

Corollary 3.15. For any 0 < ε1, ε2 < 1, there exists d0 = d0(ε1, ε2) such that the following holds
for each n ≥ d ≥ d0. Suppose that G is an n-vertex bipartite (ε1, ε2d)-expander with δ(G) ≥ d.
Let log10 n ≤ D ≤ n/ log10 n, 100
ε1 log3 n ≤ m ≤ log4 n and ℓ ≤ n/ log12 n. Let A ⊆ V (G) satisfy
|A| ≤ D/ log3 n. Let F1, . . . , F4 ⊆ G − A be vertex disjoint subgraphs and v1, . . . , v4 be vertices such
that, for each i ∈ [4], Fi is a (D, m)-expansion of vi.
Then, G − A contains vertex disjoint paths P and Q with ℓ ≤ ℓ(P ) + ℓ(Q) ≤ ℓ + 22m such that
both P and Q connect {v1, v2} to {v3, v4}.

Proof. By Lemma 3.13, G − A contains disjoint subgraphs F ′
1, . . . , F ′
4 such that, for each i ∈ [4], F ′
i
is an (n/m2, 3m)-expansion of vi. By Lemma 3.4, there is a path P ′ ⊆ G − A from V (F ′
1) ∪ V (F ′
2)
to V (F ′
3) ∪ V (F ′
4) with length at most m. Note that we can assume, without loss of generality, that
P ′ goes from V (F ′
1) to V (F ′
3). Using that F ′
1 and F ′
3 are (n/m2, 3m)-vertex expansions of v1 and
v3, respectively, let P be a v1, v3-path with length at most 7m in F ′
1 ∪ P ′ ∪ F ′
3.
Let W = A ∪ V (P ), noting that |W | ≤ D/ log3 n + 7m + 1 ≤ n/m2 log3 n. Note that 0 ≤ ℓ −
ℓ(P ) + 7m ≤ 2n/ log12 n ≤ n/m2 log3 n. Therefore, by Lemma 3.14 with (F1, F2, D, m, W, ℓ)3.14 =
(F ′
2, F ′
4, n/m2, 3m, W, ℓ − ℓ(P ) + 7m), there is a path Q in G − W from v2 to v4 with length between
ℓ − ℓ(P ) + 7m and ℓ − ℓ(P ) + 22m. As ℓ ≤ ℓ(P ) + ℓ(Q) ≤ ℓ + 22m, the paths P and Q satisfy the
property in the corollary.
 23

3.7 Subdivisions in skewed bipartite graphs

As commented on before Theorem 2.7, we often work in graphs without a subdivision of a certain
size clique with each edge divided once, that is, in a TK
(2)
ℓ -free graph for some ℓ. This is because
we often construct structures in a graph G while avoiding a vertex set, say W , for which we need
many edges in G − W . For the sizes of W and values of ℓ that we use, if the graph G is TK
(2)
ℓ -free,
then the following simple proposition shows that there cannot be too many edges between W and
V (G) \ W . In our implementation this will imply that G − W contains many edges.

Proposition 3.16. Let d ∈ N and let G be a graph containing disjoint vertex sets U and W such
that |U | ≥ |W |2 and every vertex in U has at least d neighbours in W . Then, G contains a TK
(2)
d .

Proof. Take a maximal set I ⊆ W (2) for which there is a set of distinct vertices v{x,y}, {x, y} ∈ I,
in U such that x, y ∈ N (v{x,y}) for each {x, y} ∈ I. Now, as |U | ≥ |W |2 > |W (2)|, there is some
u ∈ U \ {v{x,y} : {x, y} ∈ I}. Let A = N (u, W ), so that |A| ≥ d. In the choice of I, the vertex u is
a good candidate for v{x,y} for each {x, y} ∈ A(2). Thus, by the maximality of I, we have A(2) ⊆ I.

Taking the TK
(2)
d with vertex set A ∪ {v{x,y} : {x, y} ∈ A(2)} and edge set {xv{x,y}, yv{x,y} :

{x, y} ∈ A(2)}, then gives a TK
(2)
d in G, as required.

4 Proof of Theorem 2.7

In this section, we prove Theorem 2.7. As discussed in Section 2.4, the basic mechanism we use to
adjust the length of a path is an adjuster, which we formally deﬁne as follows (see Figure 1(b) for
an illustration).

Deﬁnition 4.1. A (D, m, k)-adjuster A = (v1, F1, v2, F2, A) in a graph G consists of vertices
v1, v2 ∈ V (G), graphs F1, F2 ⊆ G and a vertex set A ⊆ V (G) such that the following hold for some
ℓ ∈ N.

F1 A, V (F1) and V (F2) are pairwise disjoint.

F2 For each i ∈ [2], Fi is a (D, m)-expansion around vi.

F3 |A| ≤ 10mk.

F4 For each i ∈ {0, 1, . . . , k}, there is a v1, v2-path in G[A ∪ {v1, v2}] with length ℓ + 2i.

We call the smallest such ℓ for which these properties hold the length of the adjuster and denote it
ℓ(A). Note that it immediately follows that ℓ(A) ≤ |A|+1 ≤ 10mk +1. We call a (D, m, 1)-adjuster
a simple adjuster. We refer to the subgraphs F1 and F2 of an adjuster A = (v1, F1, v2, F2, A) as the
ends of the adjuster, and let V (A) = V (F1) ∪ V (F2) ∪ A.

In this section, we start by ﬁnding one simple adjuster in an expander for Lemma 4.2 in
Section 4.1. We then ﬁnd such an adjuster despite the removal of any medium-sized vertex set
from the expander, giving Lemma 4.3 in Section 4.2. In Section 4.3, we chain simple adjusters
together for Lemma 4.7, before using this to join vertex expansions by paths with precise lengths
for Lemma 4.8. Finally, we prove Theorem 1.7 in Section 4.4 and Theorem 2.7 in Section 4.5.

24

4.1 Finding one simple adjuster

Here, we ﬁnd one simple adjuster, proving Lemma 4.2. The adjuster (v1, F1, v2, F2, A) is found for
prespeciﬁed vertices v1 and v2, as required by one of the applications of Lemma 4.2.

Lemma 4.2. For any 0 < ε1 < 1, 0 < ε2 < 1/5 and k ∈ N, there exists d0 = d0(ε1, ε2, k) such that
the following is true for each n ≥ d ≥ d0. Suppose that G is an n-vertex bipartite (ε1, ε2d)-expander
with δ(G) ≥ d − 1.
Let C be a shortest cycle in G and let x1, x2 be distinct vertices in V (G) \ V (C). Let m =
200
ε1 log3 n and D ≤ log5k n.
Then, G contains a (D, m, 1)-adjuster (v1, F1, v2, F2, A) with v1 = x1, v2 = x2 and V (C) ⊆ A.

Proof. Noting that, as G is bipartite, C has even length, let ℓ0 be such that 2ℓ0 is the length of C.
Since δ(G) ≥ d − 1, we must have ℓ0 ≤ log n/ log(d − 1) ≤ m, as n ≥ d0(ε1, ε2, k) is large. Pick
vertices x3, x4 ∈ V (C) which are distance ℓ0 − 1 apart on C and let the paths separating them in
C be R1 and R2, where R1 is the shorter path.
Let D1,1 = D2,1 = D, D1,2 = D3,1 = m3D, D2,2 = D4,1 = m2D, and note that m3D ≤ log15k n.
Using any arbitrary vertices x5, x6, . . . , x15k and Di,j = D for any i, j ∈ [15k] not already chosen,
apply Lemma 3.11 to x1, x2, . . . , x15k and C with (k, m)3.11 = (15k, m/5) to get graphs Fi,j,
i, j ∈ [2] and F3,1, F4,1, for which the following hold.

• For each i, j ∈ [2] or i ∈ {3, 4} and j = 1, Fi,j is a (Di,j, m)-expansion around xi in G which
contains no vertices other than xi in {x1, . . . , x4} ∪ V (C).

• The sets V (Fi,j) \ {xi}, i, j ∈ [2] or i ∈ {3, 4} and j = 1, are pairwise disjoint.

Now, we have |V (C) ∪ V (F1,1 ∪ F2,1 ∪ F2,2 ∪ F4,1)| ≤ m + 2D + 2m2D ≤ 10m3D/ log3 n.
Therefore, as |F1,2| = |F3,1| = m3D, by Lemma 3.4, we can ﬁnd a path P ′ with length at most m
from V (F1,2) to V (F3,1) with no vertices in (V (C) ∪ V (F1,1 ∪ F2,1 ∪ F2,2 ∪ F4,1)) \ {x1, x3}. As,
F1,2 is a (D1,2, m)-expansion of x1, and F3,1 is a (D3,1, m)-expansion of x3, we can extend P ′ using
vertices from V (F1,2 ∪ F1,3) to get an x1, x3-path, say P , with length at most 3m, which has no
vertices in (V (C) ∪ V (F1,1 ∪ F2,1 ∪ F2,2 ∪ F4,1)) \ {x1, x3}.
Next, observe that |V (C) ∪ V (P ) ∪ V (F1,1) ∪ V (F2,1)| ≤ m + 3m + 1 + 2D ≤ 10m2D/ log3 n.
Therefore, as |F2,2| = |F4,1| = m2D, by Lemma 3.4, we can ﬁnd a path Q′ with length at most m
from V (F2,2) and V (F4,1) which has no vertices in (V (C) ∪ V (P ) ∪ V (F1,1) ∪ V (F2,1)) \ {x2, x4}.
As, F2,2 is a (D2,2, m)-expansion of x2, and F4,1 is a (D4,1, m)-expansion of x4, we can extend Q′

using vertices from V (F2,2 ∪ F4,1) to get an x2, x4-path, say Q, with length at most 3m and no
vertices in (V (C) ∪ V (P ) ∪ V (F1,1) ∪ V (F2,1)) \ {x2, x4}.
Set now v1 = x1, v2 = x2, F1 = F1,1, F2 = F2,1 and A = V (P ∪ Q ∪ R1 ∪ R2) \ {v1, v2}.
Then, |A| ≤ 2(3m + 1) + 2ℓ0 ≤ 10m and note that A is disjoint from V (F1) ∪ V (F2). Letting
ℓ = ℓ(P ∪ R1 ∪ Q), note that P ∪ R1 ∪ Q and P ∪ R2 ∪ Q are v1, v2-paths in G[A ∪ {v1, v2}] with
length ℓ and ℓ + 2 respectively. Thus, (v1, F1, v2, F2, A) is a (D, m, 1)-adjuster, as desired.

4.2 Finding simple adjusters robustly

In this section, we prove Lemma 4.3, a key component of our proof. This ﬁnds a simple adjuster
robustly in an expander G – that is, given any subset U ⊆ V (G) with moderate size, we construct
an adjuster in G − U .
 25

Lemma 4.3. There exists some ε1 > 0 such that, for every 0 < ε2 < 1 and k ∈ N, there exists
d0 = d0(ε1, ε2, k) such that the following is true for each n ≥ d ≥ d0. Suppose that G is a TK
(2)
d/2-

free n-vertex bipartite (ε1, ε2d)-expander with δ(G) ≥ d. Let m = 200
ε1 log3 n and D ≤ logk n. Let
U ⊆ V (G) satisfy |U | ≤ 10D.
Then, G − U contains a (D, 2m, 1)-adjuster.

The following proof sketch is illustrated in Figure 2. Essentially, we ﬁnd an expander subgraph
in H ⊆ G − U and apply Lemma 4.2 to ﬁnd a simple adjuster in H. However, H may be much
smaller than G, so this simple adjuster may be far too small to satisfy Lemma 4.3. We thus ﬁnd
many of these simple adjusters and use Lemma 3.7 to expand the ends of one of them to make
them large enough to satisfy Lemma 4.3.
More precisely, to prove Lemma 4.3, we assume no such adjuster exists, before collecting the
high degree vertices in a set L. We take a maximal set of adjusters A0 in G − U so that their ends
(the sets V (F1) and V (F2) in an adjuster (v1, F1, v2, F2, A)) are in G − L, and furthermore the ends
of diﬀerent adjusters in A0 are far apart in G − L. The adjusters in A0 will each not have large
enough ends to be a (D, m, 1)-adjuster, so we wish to expand the ends of some adjuster to make
them larger. The challenge is to do this while avoiding U .
We ﬁrst show that A0 contains many adjusters (see Claim 4.4). If this is not the case, then,
collecting together U with the adjusters in A0 and any vertices near their ends in G − L, we remove
them and show that there must be an expander subgraph H in what remains. Applying Lemma 4.2
to (essentially) H, we get an adjuster that either satisﬁes the lemma (a contradiction) or should
have belonged in A0 (another contradiction).
If many adjusters in A0 have an end with a short path to L \ U , then applying Lemma 3.7
shows that in one of these adjusters the other end must expand while avoiding the short path to
L \ U . Larger ends can then be chosen for this adjuster respectively from the expansion and from
the short path to L \ U and the neighbourhood of its endvertex in L \ U . This gives an adjuster
satisfying the lemma (a contradiction). Thus, many adjusters in A0 have no short path to L \ U
(see Claim 4.5) – we collect such adjusters in A1 ⊆ A0.
We then ﬁnd a large set Z in G− L with small diameter using Lemma 3.12 – destined to provide
a large expansion for the end of an adjuster. If many adjusters in A1 have an end with a short path
to Z, then applying Lemma 3.7 shows that, for one of these adjusters, the other end must expand
while avoiding the short path to Z. Larger ends can then be chosen for this adjuster respectively
from the expansion and from the short path to Z and Z itself. This gives an adjuster satisfying
the lemma (a contradiction). Thus, many adjusters in A1 have no short path to Z (see Claim 4.6)
– we collect such adjusters in A2 ⊆ A1.
However, by Lemma 3.7, the ends of the adjusters in A2 must expand while avoiding U . There-
fore, by Lemma 3.4, one of them must connect to Z, giving the ﬁnal contradiction which completes
the proof.

Proof of Lemma 4.3. Let 0 < ε1 < 1 be small enough that the property in Corollary 2.5 holds.
Suppose, for contradiction, that G − U contains no (D, 2m, 1)-adjuster. Let ∆ = 200mD, L = {v ∈
V (G) : dG(v) ≥ ∆} and G′ = G − L, so that ∆(G′) ≤ ∆.
Set ℓ0 = (log log n)20. Let U0 = {v ∈ V (G) \ U : dG(v, U ) ≥ d/2}. Note that if |U0| ≥ 100D2 ≥
|U |2, then by Proposition 3.16 with (U, W )3.16 = (U0, U ), G contains a TK
(2)
d/2, a contradiction.
Therefore, we can assume that |U0| ≤ 100D2, and hence, as δ(G) ≥ d and n ≥ d0(ε1, ε2, k) is

26

Z L
 U

A0A1A2

Figure 2: An illustration of the proof of Lemma 4.3. We ﬁnd A0, a large set of adjusters in G − U ,
before discarding those with a short path to L \ U , and then those with a short path to Z. Showing
that many adjusters still remain, in the set A2, leads to a contradiction.

large, G − U contains at least (n − |U | − |U0|) · (d/2)/2 ≥ nd/8 edges. Let U1 = U ∪ U0, so that
|U1| ≤ 200D2 ≤ 200 log2k n.
Take a maximal collection A0 of adjusters in G − U , such that the following hold.

G1 The sets V (F1 ∪ F2), (v1, F1, v2, F2, A) ∈ A0, are subsets of V (G′) and are all at least a
distance 10ℓ0 apart from each other and from U1 \ L in G′.

G2 For each A ∈ A0, for some mA with log3 d0 ≤ mA ≤ m, A is an (m2
A, mA, 1)-adjuster.

Claim 4.4. |A0| ≥ n1/4.

Proof of claim. Suppose, for contradiction, that |A0| < n1/4. Let W = (U1 ∪ (∪A∈A0 V (A)) \ L.
For each A = (v1, F1, v2, F2, A) ∈ A0, |V (A)| = |F1| + |F2| + |A| ≤ 2m2
A + 10mA ≤ 3m2, and
therefore |W | ≤ n1/4 · 3m3 + 200 log2k n ≤ n1/3. Let W ′ = B10ℓ0
G′ (W ), so, as ∆(G′) ≤ ∆, we have
that |W ′| ≤ 2|W | · ∆10ℓ0 ≤ n1/2.
Now, there are at most |W ′|∆ ≤ ∆n1/2 ≤ nd/16 edges in G with some vertex in W ′. Let
¯d = d/64. As G − U contains at least nd/8 edges, G − U − W ′ contains at least nd/16 edges, so that
d(G − U − W ′) ≥ d/8 = 8 ¯d. Then, by Corollary 2.5, G − U − W ′ contains an (ε1, ε2 ¯d)-expander
H with δ(H) ≥ ¯d. Let C be a shortest cycle in H. We will consider two cases, depending on how
many vertices of L there are in V (H) \ V (C).

Case I: |(V (H) \ V (C)) ∩ L| ≤ 1. Let H ′ = H − (V (H) \ V (C)) ∩ L, so that δ(H ′) ≥ ¯d − 1. Note
that, for each X ⊆ V (H ′) with ε2 ¯d/2 ≤ |X| ≤ |H ′|/2 < |H|/2, we have

|NH ′(X)| ≥ |NH (X)| − 1 ≥ |X| · ε(|X|, ε1, ε2 ¯d) − 1

≥ 1
2 |X| · ε(|X|, ε1, ε2 ¯d) + ε2 ¯d
4 · ε(ε2 ¯d/2, ε1, ε2 ¯d) − 1

≥ |X| · ε(|X|, ε1/2, ε2 ¯d) + ε2 ¯d
4 · ε1
log2(15/2) − 1 ≥ |X| · ε(|X|, ε1/2, ε2 ¯d),

where the last inequality follows as ¯d ≥ d0(ε1, ε2, k)/64 is large. Therefore, H ′ is a (ε1/2, ε2 ¯d)-
expander with δ(H ′) ≥ ¯d − 1. Note that C is a shortest cycle in H ′.
Let mH ′ = 200 log3 |H ′|/ε1 ≤ m, and note that, as |H ′| ≥ δ(H ′) + 1 ≥ ¯d ≥ d0/64, and
d0 = d0(ε1, ε2, k) is large, mH ′ ≥ log3 d0. Picking arbitrary vertices x1, x2 ∈ V (H ′) \ V (C) and

27

noting that ¯d ≥ d0(ε1, ε2, k)/64 is large, by Lemma 4.2 with (k, D)4.2 = (10, m2
H ′ ), H ′ contains
an (m2
H ′, mH ′, 1)-adjuster (v1, F1, v2, F2, A) with V (C) ⊆ A. As A is disjoint from V (F1 ∪ F2),
V (C) ⊆ A and (V (H ′) \ V (C)) ∩ L = ∅, we have that V (F1 ∪ F2) is disjoint from L, and hence lies
in V (G′). Together with V (F1 ∪ F2) ⊆ V (H ′) being disjoint from W ′ and so 10ℓ0-far in G′ from the
ends of the adjusters in A0 and from U1 \ L, this violates the maximality of A0, a contradiction.

Case II: |(V (H) \ V (C)) ∩ L| ≥ 2. Let x1, x2 ∈ (V (H) \ V (C)) ∩ L be distinct and let mH ′ =
200 log3 |H ′|/ε1 ≤ m. By Lemma 4.2 with (k, D)4.2 = (1, 1), H contains a (1, mH ′ , 1)-adjuster
(v1, F1, v2, F2, A) with v1 = x1 and v2 = x2. Using that |A| ≤ 10mH ′ ≤ 10m, |U | ≤ 10D, and
dG(x1), dG(x2) ≥ ∆ = 200mD, pick disjointly sets X1 ⊆ NG(x1)\(U ∪A∪{x2}) and X2 ⊆ NG(x2)\
(U ∪ A ∪ {x1}) with |X1| = |X2| = D − 1. Letting F ′
i = G[{xi} ∪ Xi] for each i ∈ [2], and noting
|A| ≤ 20m, we have that (x1, F ′
1, x2, F ′
2, A) is a (D, 2m, 1)-adjuster in G − U , a contradiction. ■

Now, let A1 ⊆ A0 be the set of adjusters (v1, F1, v2, F2, A) ∈ A0 for which there is no path
with length at most ℓ0 from V (F1) ∪ V (F2) to L \ U in G − U − A.

Claim 4.5. |A1| ≥ n1/4/2.

Proof of claim. Let r = n1/8. Suppose, for contradiction, that we can label distinct A1, . . . , Ar ∈
A0 \ A1. Say, for each i ∈ [r], that Ai = (vi,1, Fi,1, vi,2, Fi,2, ¯Ai) and let P ′
i be a shortest path with
length at most ℓ0 from V (Fi,1) ∪ V (Fi,2) to L \ U in G − U − ¯Ai. Relabelling, if necessary, for each
i ∈ [r] suppose the endvertex of P ′
i in V (Fi,1 ∪ Fi,2) is in V (Fi,1), and let Qi be a path from this
endvertex of P ′
i to vi,1 in Fi,1 with length at most mAi.
For each i ∈ [r], let xi be the endpoint of P ′
i in L \ U , and let Pi = P ′
i − xi. We shall apply
Lemma 3.7 by setting, for each i ∈ [r], Ai = V (Fi,2), Bi = ¯Ai ∪ V (Qi) ∪ {xi} and Ci = V (Pi).
Firstly, as |Ai| = m2
Ai ≥ log6 d0 by G2 and d0 = d0(ε1, ε2, k) is large, we have that |Ai| ≥ d3.7
0 ,

where d3.7
0 is the function in Lemma 3.7, so that C1 holds.
As V (Fi,2) ⊆ V (G′) = V (G) \ L by G1, and V (Fi,2) is disjoint from V (Fi,1) and ¯Ai by F1, we
have that Ai and Bi∪Ci are disjoint. Furthermore, |Bi| ≤ | ¯Ai|+|Qi|+1 ≤ 20mAi ≤ m2
Ai/ log10(m2
Ai)
as mAi ≥ log3(d0(ε1, ε2, k)) is large, and thus C2 holds.
Now, as P ′
i is a shortest path from V (Fi,1) ∪ V (Fi,2) to L \ U in G − U − ¯Ai, which has an
endvertex in V (Fi,1), and Ai = V (Fi,2), we have, for each ℓ ∈ N, that Bℓ
G−U − ¯Ai(Ai) has at most
ℓ + 1 vertices in P ′
i , and hence Pi. Therefore, Ai has 4-limited contact with Ci in G − U − ¯Ai, and
hence in G − U − Bi, and thus C3 holds.
Suppose there is a path, Ri say, with length at most 10ℓ0 from Ai to L \ (U ∪ {xi}) in G − U −
Bi − Ci. Then, there is a path R′
i ⊆ Ri ∪ Fi,2 from vi,2 to some vertex yi ∈ L \ (U ∪ {xi}) with length
at most 10ℓ0 + mAi ≤ 2m − 1, and the path Qi ∪ P ′
i is a path from vi,1 to xi with length at most
mAi + ℓ0 ≤ 2m − 1 in G − U − ¯Ai with vertices in Bi ∪ Ci. Then, as |U ∪ Ai ∪ V (R′
i) ∪ V (Qi ∪ P ′
i )| ≤
10D + 10mAi + 4m ≤ 10D + 15m, as xi, yi ∈ L both have degree at least ∆ = 200mD, we
can comfortably choose Xi ⊆ NG(xi) and Yi ⊆ NG(yi) which are disjoint from each other and
from U ∪ Ai ∪ V (R′
i) ∪ V (Qi ∪ P ′
i ) and have size D − |P ′
i ∪ Qi| and D − |R′
i| respectively. Then,
(vi,1, G[Xi ∪V (P ′
i )∪V (Qi)], vi,2, G[Yi ∪V (R′
i)], Ai) is a (D, 2m, 1)-adjuster in G−U , a contradiction.
Therefore, there is no such path Ri. Consequently, recalling that Ai = V (Fi,2), we have

Bℓ0
G−U −Bi−Ci(Ai) = Bℓ0
G′−U −Bi−Ci(Ai),

which, by G1, is disjoint from U1. By the choice of U0 ⊆ U1, we have that C4 holds.

28

Now, similarly, for any j ∈ [r] \ {i}, we have that Bℓ0
G−U −Bj −Cj (Aj) = Bℓ0
G′−U −Bj−Cj (Aj), so

that, by G1, Bℓ0
G−U −Bj −Cj (Aj ) and Bℓ0
G−U −Bi−Ci(Ai) are disjoint. In particular, Ai and Aj are a
distance at least 2ℓ0 apart in G − U − Bi − Ci − Bj − Cj, and therefore C5 holds.
Thus, by Lemma 3.7, there is some j ∈ [r] for which |Bℓ0
G−U −Bj −Cj (Aj )| ≥ logk n ≥ D. As
Fj,2 is an (m2
Aj , mAj )-expansion of vj,2 in G′ − U − Bj − Cj, mAj ≤ m and Aj = V (Fj,2), we
have that |B2m
G−U −Bj−Cj (vj,2)| ≥ D as ℓ0 ≪ m. Therefore, by Proposition 3.10, we can pick a
(D, 2m)-expansion, F ′
j,2 say, of vj,2 in G − U − Bi − Cj.
As xj ∈ L, we can then pick a set U ′ of neighbours of xj disjoint from U ∪ V (F ′
j,2)∪ ¯Aj ∪ V (Qj)∪
V (P ′
j) with |U ′| = D − |V (P ′
j ∪ Qj)|. Let F ′
j,1 = G[U ′ ∪ V (P ′
j) ∪ V (Qj)]. Note that F ′
j,1 is then a
(D, 2m)-expansion of vj,1 as Qj ∪P ′
j is a vj,1, xj-path with length at most mAj +ℓ0 ≤ 2m−1. Finally,
note that (vj,1, F ′
j,1, vj,2, F ′
j,2, ¯Aj ) is a (D, 2m, 1)-adjuster in G − U , a contradiction. Therefore,
|A0 \ A1| < r = n1/8, and so by Claim 4.4, we have |A1| > n1/4 − r ≥ n1/4/2. ■

Let A′
1 ⊆ A1 satisfy |A′
1| = n1/4/2. Then, |∪A∈A′
1 V (A)| ≤ n1/4 ·3m2 ≤ n1/3 by G2. Therefore,

|U ∪ Bℓ0
G′(∪A∈A′
1 (V (A) \ L))| ≤ 10D + n1/3 · 2∆ℓ0 ≤ n1/2.

Thus, by Lemma 3.12, there is a set Z ⊆ V (G) \ U which has diameter at most m/2 and size
10m2D, and is a distance at least ℓ0 in G′ from V (A) \ L for each A ∈ A′
1.
Let A2 ⊆ A′
1 be the set of adjusters (v1, F1, v2, F2, A) ∈ A′
1 for which there is no path with
length at most m/2 from V (F1) ∪ V (F2) to Z in G − U − A.

Claim 4.6. |A2| ≥ n1/4/4.

Proof of claim. Let r = n1/8. Suppose, for contradiction, we can label distinct A1, . . . , Ar ∈
A′
1 \ A2. Say, for each i ∈ [r], that Ai = (vi,1, Fi,1, vi,2, Fi,2, ¯Ai) and let Pi be a shortest path with
length at most m/2 from V (Fi,1) ∪ V (Fi,2) to Z in G − U − ¯Ai. Relabelling, if necessary, for each
i ∈ [r] suppose the endvertex of Pi in V (Fi,1 ∪ Fi,2) is in V (Fi,1), and let Qi be a path from this
endvertex of V (Pi) to vi,1 in Fi,1 with length at most mAi.
We will apply Lemma 3.7 to Ai = V (Fi,2), Bi = ¯Ai ∪V (Qi) and Ci = V (Pi), for each i ∈ [r]. For
each i ∈ [r], similarly to the proof of Claim 4.5, we have that C1–C3 hold. By the choice of A1, for
each i ∈ [r], there is no path of length at most ℓ0 from Ai to L \U in G− U − Bi − Ci. Therefore, the
sets Bℓ0
G−U −Bi−Ci(Ai) and Bℓ0
G′−U −Bi−Ci(Ai) are the same set, and thus, by G1, this set is disjoint
from U1. Thus, C4 holds by the deﬁnition of U1. It similarly follows that Bℓ0
G−U −Bi−Ci(Ai) and
Bℓ0
G−U −Bj−Cj (Aj) are vertex disjoint for each j ∈ [r] \ {i}, and thus C5 holds.

Thus, by Lemma 3.7, there is some j ∈ [r] for which |Bℓ0
G′−U −Bj−Cj (Aj)| = |Bℓ0
G−U −Bj −Cj (Aj)| ≥
D. Thus, as Fj,2 is an (m2
Aj , mAj )-expansion of vj,2 in G′ − U − Bj − Cj by G1 and G2, and Aj =

V (Fj,2), by Proposition 3.10, there is a (D, 2m)-expansion, F ′
j,2 say, of vj,2 in Bℓ0
G′−U −Bj−Cj (V (Fj,2)).
As Z was chosen to have a distance at least ℓ0 in G′ from V (Aj)\L, we have that V (F ′
j,2) is disjoint
from Z.
Now, as Z has diameter at most m/2 in G, Qj ∪ Pj ∪ G[Z] is an expansion of vj,1 with radius
at most ℓ(Qj) + ℓ(Pj ) + m/2 ≤ 2m and size at least D. Therefore, by Proposition 3.10, we can ﬁnd
within Qj ∪ Pj ∪ G[Z] a (D, 2m)-expansion, F ′
j,1 say, of vj,1, which then must be vertex-disjoint
from ¯Aj and from V (F ′
j,2) ⊆ Bℓ0
G′−U −Bj −Cj (V (Fj,2)). Thus, we have that (vj,1, F ′
j,1, vj,2, F ′
j,2, ¯Aj) is

a (D, 2m, 1)-adjuster in G − U , a contradiction. Thus, |A2| ≥ |A1| − r ≥ n1/4/4, by Claim 4.5. ■

29

Let r = n1/8. Using Claim 4.6, label distinct A1, . . . , Ar ∈ A2, and say, for each i ∈ [r], that
Ai = (vi,1, Fi,1, vi,2, Fi,2, ¯Ai). We shall apply Lemma 3.7 to Ai = V (Fi,1 ∪Fi,2), Bi = ¯Ai and Ci = ∅.
Similarly as in the proof of Claim 4.6, the only diﬀerence being that C3 holds trivially as Ci = ∅
and Ai is slightly larger, we have that C1–C5 hold.
Thus, by Lemma 3.7, there is some j ∈ [r] with |Bℓ0
G−U −Bj−Cj (Aj)| = |Bℓ0
G−U −Bj (Aj)| ≥
10m2D ≥ 10 log3 n|U ∪ Bj|. Therefore, by Lemma 3.4, there is a path in G − U − Bj from
Bℓ0
G−U −Bj (Aj) to Z with length at most m/4. Then, as Aj = V (Fj,1 ∪ Fj,2) and Bj = ¯Aj, there is
a path in G − U − ¯Aj from V (Fj,1 ∪ Fj,2) to Z with length at most m/2, contradicting Aj ∈ A2,
and completing the proof.

4.3 Connecting simple adjusters for paths with speciﬁc lengths

Using Lemma 4.3, we can ﬁnd many vertex disjoint simple adjusters. We now connect them together
into a larger adjuster, for Lemma 4.7, before using these to construct paths with speciﬁc lengths
for Lemma 4.8.

Lemma 4.7. There exists some ε1 > 0 such that, for any 0 < ε2 < 1/5 and k ≥ 10, there exists
d0 = d0(ε1, ε2, k) such that the following holds for each n ≥ d ≥ d0. Suppose that G is an n-vertex
TK
(2)
d/2-free bipartite (ε1, ε2d)-expander with δ(G) ≥ d.

Let m = 800
ε1 log3 n. Suppose log10 n ≤ D ≤ logk n, 1 ≤ r ≤ 30m and U ⊆ V (G) with |U | ≤ D.
Then, there is a (D, m, r)-adjuster in G − U .

Proof. Let ε1 > 0 be such that the property in Lemma 4.3 holds. By this property, as d ≥
d0(ε1, ε2, k) is large, for every set V ⊆ V (G) with |V | ≤ log2k n, G − V contains a (D, m/2, 1)-
adjuster. By Lemma 3.4, as d ≥ d0(ε1, ε2, k) is large, for any sets X and Y with size at least 2D,
and any set V ⊆ V (G) \ (X ∪ Y ) with size at most 20D/ log3 n, there is a path from X to Y in
G − V with length at most m.
We now prove the property in the lemma by induction on r. Note that, we already have
this property for r = 1 as |U | ≤ D ≤ log2k n, and a (D, m/2, 1)-adjuster is also a (D, m, 1)-
adjuster. Suppose then, for some r with 1 ≤ r < 30m, G − U contains a (D, m, r)-adjuster,
(v1, F1, v2, F2, A1) say. Let U ′ = U ∪ A1 ∪ V (F1) ∪ V (F2), so that |U ′| ≤ 4D ≤ log2k n. Therefore,
G − U ′ contains a (D, m/2, 1)-adjuster, (v3, F3, v4, F4, A2) say. As |F1 ∪ F2| = |F3 ∪ F4| = 2D,
and |A1 ∪ A2| ≤ 20rm ≤ 600m2 ≤ D/ log3 n, there is a path, P say, with length at most m, from
V (F1) ∪ V (F2) to V (F3) ∪ V (F4) avoiding A1 ∪ A2.
Note that, without loss of generality, we can assume that P is a path from V (F1) to V (F3). Using
that F1 and F3 are (D, m)-expansions of v1 and v3 respectively, take a v1, v3-path Q ⊆ F1 ∪ P ∪ F3
with length at most 5m. Then, we claim (v2, F2, v4, F4, A1 ∪ A2 ∪ V (Q)) is a (D, m, r + 1)-adjuster.
Indeed, we easily have that F1 and F2 hold, and |A1 ∪ A2 ∪ V (Q)| ≤ 5m + 10 · (m/2) + 10mr =
10(r + 1)m, so that F3 holds.
Finally, let ℓ1 = ℓ((v1, F1, v2, F2, A1)), ℓ2 = ℓ((v3, F3, v4, F4, A2)) and ℓ = ℓ1 + ℓ2 + ℓ(Q). If
i ∈ {0, 1, . . . , r + 1}, then there is some i1 ∈ {0, 1, . . . , r} and i2 ∈ {0, 1} with i = i1 + i2. Let P1 be
a v2, v1-path in G[A1 ∪ {v1, v2}] with length ℓ1 + 2i1 and let P2 be a v3, v4-path with length ℓ2 + 2i2
in G[A2 ∪ {v3, v4}]. Then, P1 ∪ Q ∪ P2 is a v2, v4-path in G[A1 ∪ A2 ∪ V (Q)] with length ℓ + 2i, and
thus ℓ satisﬁes F4.

Combining Lemma 4.7 with Corollary 3.15, we can ﬁnally ﬁnd paths with exactly some desired
length, as follows.
 30

Lemma 4.8. There exists some ε1 > 0 such that, for any 0 < ε2 < 1/5 and k ≥ 10, there exists
d0 = d0(ε1, ε2, k) such that the following holds for each n ≥ d ≥ d0. Suppose that G is an n-vertex
TK
(2)
d/2-free bipartite (ε1, ε2d)-expander with δ(G) ≥ d.

Suppose log10 n ≤ D ≤ logk n, and U ⊆ V (G) with |U | ≤ D/2 log3 n, and let m = 800
ε1 log3 n.
Suppose F1, F2 ⊆ G−U are vertex disjoint such that Fi is a (D, m)-expansion of vi, for each i ∈ [2].
Let log7 n ≤ ℓ ≤ n/ log12 n be such that ℓ = π(v1, v2, G) mod 2.
Then, there is a v1, v2-path with length ℓ in G − U .

Proof. By Lemma 4.7, there is a (D, m, 22m)-adjuster, A = (v3, F3, v4, F4, A) say, in G − U with
length ℓ(A) ≤ |A| + 1 ≤ 500m2. Let ¯ℓ = ℓ − 22m − ℓ(A), so that 0 ≤ ¯ℓ ≤ n/ log12 n. As
|A ∪ U | ≤ 500m2 + D/2 log3 n ≤ D/ log3 n, by Corollary 3.15, there are paths P and Q in G − U − A
which are vertex disjoint, both connect {v1, v2} to {v3, v4} and so that ¯ℓ ≤ ℓ(P ) + ℓ(Q) ≤ ¯ℓ + 22m.
Note that we can assume, without loss of generality, that P is a v1, v3-path and Q is a v2, v4-path.
Now, 0 ≤ ℓ − ℓ(P ) − ℓ(Q) − ℓ(A) ≤ 22m. As A is a (D, m, 22m)-adjuster there is a v3, v4-
path in G[A ∪ {v3, v4}] with length ℓ(A), and therefore ℓ(A) = π(v3, v4, G) mod 2. Then, as
ℓ(P ) = π(v1, v3, G) mod 2, ℓ(Q) = π(v2, v4, G) mod 2, ℓ = π(v1, v2, G) mod 2 and π(v1, v2, G) =
π(v1, v3, G) + π(v3, v4, G) + π(v4, v2, G) mod 2, we have ℓ − ℓ(P ) − ℓ(Q) − ℓ(A) = 0 mod 2. That
is, there is some i ∈ N with 2i = ℓ − ℓ(P ) − ℓ(Q) − ℓ(A), where i ≤ 11m.
Therefore, by the property of the adjuster, there is a v3, v4-path, R say, with length ℓ(A) + 2i =
ℓ − ℓ(P ) − ℓ(Q) in G[A ∪ {v3, v4}]. Then, P ∪ R ∪ Q is a v1, v2-path with length ℓ in G − U .

4.4 Proof of Theorem 1.7

We can now prove Theorem 1.7. We take some core vertices v1, . . . , vk in an expander, ﬁnd expan-
sions around them using Lemma 3.11 and then connect each pair of core vertices using Lemma 4.8.

Proof of Theorem 1.7. Let ε1 > 0 be such that the properties in Corollary 2.5 and Lemma 4.8 hold.
Let ε2 = 1/10. Let d0 = d0(ε1, ε2, k) be large, and let d = 8d0. Let G be a graph with d(G) ≥ d.
By Corollary 2.5, we can ﬁnd a bipartite (ε1, ε2d)-expander H ⊆ G with δ(H) ≥ d0. Let
K = (k
2), n = |H| ≥ d0, m = 800
ε1 log3 n and ℓ = log7 n. Take k distinct vertices in the same

partition in H, say v1, . . . , vk. As d0(ε1, ε2, k) is large and m10K ≤ log30k2 n, by Lemma 3.11 with
k3.11 = 30k2 (and C3.11 an arbitrary shortest cycle in H, which will not play a role here), we can
ﬁnd, for each i, j ∈ [k] an (m10K , m)-expansion Fi,j ⊆ H of vi so that the sets V (Fi,j) \ {vi} are
pairwise disjoint over i, j ∈ [k].
Let f : [K] → [k](2) be a bijection and let g, h : [K] → [k] be such that f (i) = {g(i), h(i)} for
each i ∈ [K]. For each i ∈ [K], using Proposition 3.10, let Hi,1 ⊆ Fg(i),h(i) be such that Hi,1 is an
(m10(K+1−i), m)-expansion of vg(i) and let Hi,2 ⊆ Fh(i),g(i) be such that Hi,2 is an (m10(K+1−i), m)-
expansion of vh(i).
We shall connect pairs of core vertices, in the order given by f . For each i ∈ [K], the expansions
Hi,1 and Hi,2 will be used to connect vg(i) and vh(i). We will make sure that the expansions that
are not yet used are protected. More precisely, we will ﬁnd paths P1, . . . , PK , each with length ℓ,
so that the following hold.

H1 For each i ∈ [K], Pi is a vg(i), vh(i)-path with length ℓ.

H2 For each i ∈ [K], V (Pi) is disjoint from

Ui := ({vj : j ∈ [k]} ∪ (∪j>i(V (Hj,1) ∪ V (Hj,2))) ∪ (∪j<iV (Pj))) \ {vg(i), vh(i)}.

31

This is suﬃcient to prove the theorem. Indeed, by H2, for each 1 ≤ i < j ≤ K, as V (Pi) \
({vg(i), vh(i)} ∩ {vg(j), vh(j)}) ⊆ Uj, we have that Pi and Pj are internally disjoint. Therefore,

∪i∈[K]Pi is a copy of TK
(ℓ)
k .
Suppose then that 1 ≤ i ≤ K, and we have found paths P1, . . . , Pi−1 satisfying H1 and H2.
Note that

|Ui| ≤ k + ∑

j>i 2m10(K+1−j) + ∑

j<i ℓ ≤ k + 4m10(K−i) + k2m3 ≤ m10(K+1−i)

m3 = |Hi,1|
m3 = |Hi,2|
m3 .

Therefore, by Lemma 4.8 with (v1, F1, v2, F2, U )4.8 = (vg(i), Hi,1, vh(i), Hi,2, Ui), there is a path Pi
with length ℓ between vg(i) and vh(i) which does not intersect Ui. This completes the proof.

4.5 Proof of Theorem 2.7

Finally, we combine Lemmas 3.11 and 4.8 to prove Theorem 2.7.

Proof of Theorem 2.7. Let ε1 > 0 be such that the property in Lemma 4.8 holds. Let k = 10, let
d0 = d0(ε1, ε2) be large and let n ≥ d ≥ d0. Suppose then that H is a TK
(2)
d/2-free bipartite n-vertex

(ε1, ε2d)-expander with δ(H) ≥ d and let x, y ∈ V (H) be distinct. Let ℓ ∈ [log7 n, n/ log12 n] satisfy
ℓ = π(x, y, H) mod 2. We will show that H contains an x, y path with length ℓ.
Let m = 800
ε1 log3 n and D = log10 n. Then, by Lemma 3.11 (applied with C taken to be an
arbitrary shortest cycle in H), there are vertex disjoint graphs Fx, Fy ⊆ H so that Fx is a (D, m)-
expansion of x and Fy is a (D, m)-expansion of y. Then, by Lemma 4.8 with U = ∅, there is a
x, y-path with length ℓ in H, as required.

5 Proof of Theorem 1.4

We will now prove Theorem 1.4 using Theorem 2.7. For convenience, before we discuss the proof
further, we will prove the following corollary of Theorem 2.7.

Corollary 5.1. For each ε > 0, there is some d0 such that the following holds for each d ≥ d0.
If a graph G has d(G) ≥ 8d, then it contains a connected bipartite subgraph H for which there is
some positive integer ℓ such that the following holds.

I For any u, v ∈ V (H) with u ̸= v and t ∈ [ℓ, ℓ · d1−ε] with t = π(u, v, H) mod 2, there is a
u, v-path in H with length t.

Proof. Let ε1 > 0 be such that the properties in Theorem 2.7 and Corollary 2.5 hold, and let
ε2 = 1/10. Let d0 = d0(ε, ε1, ε2) be large. Suppose then that the graph G has d(G) ≥ 8d.
If possible, let H ⊆ G be a copy of TK
(2)
d/2, and let ℓ = 6. Then, as d ≥ d0(ε, ε1, ε2) is large, for
any two distinct vertices u, v in H and any integer t ∈ [ℓ, ℓ · d1−ε] ⊆ [6, d − 8] with t = π(u, v, H)
mod 2, it is easy to see that there is a u, v-path in H with length t.
Assume then that G is TK
(2)
d/2-free. By Corollary 2.5, G contains a bipartite (ε1, ε2d)-expander

H with δ(H) ≥ d(G)/8 ≥ d. Let ℓ = log7 |H|. Note that |H| ≥ δ(H) + 1 ≥ d + 1, and
d ≥ d0 = d0(ε, ε1, ε2) is large, so that |H|/ log12 |H| ≥ ℓ · d1−ε. As n ≥ d ≥ d0(ε, ε1, ε2) is
large, by Theorem 2.7, for any two distinct vertices u, v in H and any integer t ∈ [ℓ, ℓ · d1−ε] ⊆
[log7 |H|, |H|/ log12 |H|] with t = π(u, v, H) mod 2, there is a u, v-path in H with length t.

32

The following sketch is illustrated in Figure 3. For Theorem 1.4, we have a graph G with
χ(G) = k and wish to ﬁnd a long interval in the set of odd cycle lengths in G. Letting d ≈ k/30,
we ﬁrst ﬁnd a maximal collection Hi, i ∈ [s], of edge disjoint bipartite graphs and corresponding
integers ℓi, i ∈ [s], which satisfy I. As χ(G) = k ≈ 30d is large, it will follow from the maximality
of this collection and Corollary 5.1 that ∪i∈[s]Hi has high enough chromatic number that it must
contain some odd cycle.
Now, say each bipartite Hi has vertex classes Ai and Bi, and consider the auxilliary graph K
formed from ∪i∈[s]Hi by including any missing edges between Ai and Bi for each i ∈ [s]. As ∪i∈[s]Hi
has an odd cycle, so does K. Consider a shortest odd cycle C in K. Each edge in C, say the edge
e between Ai(e) and Bi(e), can be replaced with a path with any odd length in [ℓi(e), ℓi(e) · k1−o(1)]
by I. Roughly speaking, doing this for each edge in C creates cycles with all possible odd lengths
in [ℓ, ℓ · k1−o(1)], with ℓ = ∑e∈E(C) ℓi(e).

H1
 H2
 H5
 H4

H3

Figure 3: An illustration of the proof of Theorem 1.4. As seen on the left, we ﬁnd a collection
of edge disjoint bipartite expander graphs, here H1, . . . , H5, so that Hi intersects with Hi−1 and
Hi+1 on at least one vertex each (working mod 5 in the indices), and any cycle around the ‘cycle
of subgraphs’ is odd.
We then form diﬀerent length odd cycles by choosing short paths between the intersecting vertices in
some of the expanders Hi, while varying the length of the paths between a vertex disjoint collection
of the expanders (here, H3 and H5).

The main complication omitted in this sketch is that the paths replacing the edges in C need
to be internally vertex disjoint from each other and V (C). To ensure this, we only replace some of
the edges with paths of varying length, only doing so for a suitable large collection of the edges on
C. If two edges on C are far apart, yet their containing bipartite graphs Hi intersect, then we can
ﬁnd a shorter odd cycle in K than C, a contradiction. Therefore, we choose a subset E ⊆ E(C) of
edges which are pairwise nicely separated on C (and which maximises ∑e∈E ℓi(e) subject to this).
We replace each edge in E by an odd length path with length from [ℓi(e), ℓi(e)k1−o(1)], while we
(essentially) replace each edge in E(C) \ E with some minimal path between the same vertices in
the corresponding graph Hi, in order to connect the paths corresponding to E into a cycle.

Recalling Deﬁnition 2.6, we use the following simple proposition.

Proposition 5.2. Given any connected bipartite graph H containing three distinct vertices a1, a2
and a3, we have π(a1, a3, H) + π(a2, a3, H) − π(a1, a2, H) ∈ {0, 2}. (19)

Furthermore, for any (not necessarily distinct) vertices a1, a2 and a3, we have

π(a1, a3, H) + π(a2, a3, H) = π(a1, a2, H) mod 2 (20)

33

Proof. First, suppose that a1, a2 and a3 are distinct. Let the vertex classes of H be A and B, and
assume without loss of generality that a3 ∈ A. If a1, a2 ∈ A, then π(a1, a3, H) + π(a2, a3, H) −
π(a1, a2, H) = 2+2−2 = 2. If a1, a2 ∈ B, then π(a1, a3, H)+π(a2, a3, H)−π(a1, a2, H) = 1+1−2 =
0. We may then assume that a1 ∈ A and a2 ∈ B, and so π(a1, a3, H) + π(a2, a3, H) − π(a1, a2, H) =
2 + 1 − 1 = 2. Therefore, whenever a1, a2 and a3 are distinct, (19) holds, and furthermore (20)
holds in this case as well.
Now, note that if a1 = a2 = a, then (20) holds as 2π(a, a3, H) = 0 = π(a, a, H) mod 2, while if
a1 = a3 = a, then 0 + π(a2, a, H) = π(a, a2, H) mod 2, and, similarly, (20) holds if a2 = a3. This
completes the remaining cases when a1, a2 and a3 are not necessarily distinct.

We are now ready to prove Theorem 1.4, which we do throughout Section 5.1.

5.1 Proof of Theorem 1.4

Let ε > 0. To prove Theorem 1.4, we will show that there is some k0 ∈ N such that the following
holds for each k ≥ k0. If G is a graph with chromatic number k, then, for some ℓ ∈ N, C(G)
contains every odd integer in [ℓ, ℓ · k1−ε].
Let then d0 be large enough that d1−ε/4 ≥ (30(d + 1))1−ε/2 holds for each d ≥ d0 and the
property in Corollary 5.1 holds for d0 with ε5.1 = ε/4. Let k0 = 30d0. Suppose k ≥ k0 and that
the graph G has χ(G) = k. Let d = ⌊k/30⌋.
As outlined at the beginning of this section, using the high chromatic number of G, we ﬁrst
ﬁnd a minimal ‘cycle of subgraphs’ that could potentially oﬀer many distinct odd cycle lengths
(in Section 5.1.1). We then prove that non-consecutive subgraphs in this cycle are vertex disjoint
(in Section 5.1.2). We then choose some of these non-consecutive subgraphs in which to vary the
path lengths (in Section 5.1.3). Finally, we take diﬀerent path lengths in the chosen subgraphs and
connect them up into a cycle, getting many odd cycles (in Section 5.1.4).

5.1.1 A minimal ‘cycle of subgraphs’

Let H1, . . . , Hs be a maximal collection of edge disjoint connected bipartite subgraphs of G such
that, for each i ∈ [s], there is a positive integer ℓi for which the following holds.

J For any two distinct vertices u, v in Hi and any integer t ∈ [ℓi, ℓi · k1−ε/2] with t = π(u, v, Hi)
mod 2, there is a u, v-path in Hi with length t.

Let H = ∪i∈[s]Hi. Let G′ = G \ H. As d1−ε/4 ≥ (30(d + 1))1−ε/2 ≥ k1−ε/2, by the maximality of
the collection H1, . . . , Hs and Corollary 5.1, G′ has no subgraph with average degree at least 8d.
Therefore, every subgraph of G′ has a vertex with degree in that subgraph less than 8d, and hence,
as is well known, chromatic number less than 8d.
We will now show that χ(H) ≥ 3. Indeed, suppose to the contrary that χ(H) < 3. Let
c1 : V (G′) → [8d] be a proper colouring of G′ and let c2 : V (H) → [2] be a proper colouring of H.
Then, c : V (G) → [8d] × [2] deﬁned by c(v) = (c1(v), c2(v)) is easily seen to be a proper colouring
of G. Therefore, χ(G) ≤ 16d < k, a contradiction. Thus, we have that χ(H) ≥ 3.
Therefore, we can choose an odd cycle C in H. Say that C has length r′ and vertices a1 . . . ar′+1
where a1 = ar′+1. We now take a certain minimal sequence, where C will demonstrate that such a
sequence exists. That is, we take a sequence

S = b1F1b2F2b3 . . . brFrbr+1

34

such that, setting r(S) = r, we have

K1 b1, . . . , br are distinct vertices and b1 = br+1,

K2 for each i ∈ [r], Fi ∈ {H1, . . . , Hs} and bi, bi+1 ∈ V (Fi),

K3 π(S) := ∑r
i=1 π(bi, bi+1, Fi) is odd, and

K4 subject to K1–K3, π(S) + r(S) is minimised.

Indeed, such a sequence exists as the sequence S ′ = a1G1a2G2a3 . . . ar′Gr′ar′+1 satisﬁes K1–K3,
where for each i ∈ [r′], Gi = Hj for the j ∈ [s] with aiai+1 ∈ E(Hj), and we have that π(S ′) =
∑r′
i=1 π(ai, ai+1, Gi) = r′ is odd.
Note that we must have r ≥ 2. Indeed, if r = 1, then K1 implies that π(b1, b2, F1) =
π(b1, b1, F1) = 0, violating K3.

5.1.2 Non-consecutive subgraphs are vertex disjoint

We will now use the minimality of S (that is, K4) to infer two key properties. These are (roughly)
that non-consecutive graphs in F1, . . . , Fr are vertex disjoint (Claim 5.3) and that each graph is a
diﬀerent graph in {H1, . . . , Hs} (Claim 5.4).

Claim 5.3. For each i, j ∈ [r] with i ̸= j and i ̸= j ± 1 mod r, Fi and Fj are vertex disjoint.

Proof of claim. Suppose, for contradiction, we have some distinct i, j ∈ [r] with i ̸= j ± 1 mod r
(and thus r ≥ 4) and that Fi and Fj are not vertex disjoint. We consider separately the case
when Fi and Fj share some vertex not in {b1, . . . , br} (Case I) and when they share some vertex in
{b1, . . . , br} (Case II).

Case I. Suppose then that Fi and Fj share some vertex a /∈ {b1, . . . , br}. Assume, without loss of
generality, that i < j. As depicted in Figure 4, consider the two sequences

S1 = b1F1b2 . . . biFiaFjbj+1 . . . brFrbr+1 and S2 = bi+1Fi+1bi+2Fi+2 . . . bjFjaFibi+1.

We will show that one of these sequences satisﬁes K1–K3 in place of S and contradicts the min-
imality of S in K4. That each sequence S1 and S2 satisﬁes the corresponding version of K1 and
K2 follows immediately from K1 and K2 and as a /∈ {b1, . . . , br} is in both V (Fi) and V (Fj).
Deﬁne π(S1) and π(S2) similarly to π(S) in K3, that is, let

π(S1) = ∑

1≤i′<i π(bi′, bi′+1, Fi′ ) + π(bi, a, Fi) + π(a, bj+1, Fj ) + ∑

j<i′≤r π(bi′, bi′+1, Fi′),

and π(S2) = ∑

i<i′<j π(bi′, bi′+1, Fi′) + π(bj, a, Fj ) + π(a, bi+1, Fi).

Then,

π(S1) + π(S2) − π(S) (21)

= π(bi, a, Fi) + π(a, bj+1, Fj) + π(bj, a, Fj ) + π(a, bi+1, Fi) − π(bi, bi+1, Fi) − π(bi, bj+1, Fj).

35

By K1, and as a /∈ {b1, . . . , br}, a, bi and bi+1 are distinct. Thus, by Proposition 5.2, π(bi, a, Fi) +
π(bi+1, a, Fi)−π(bi, bi+1, Fi) ∈ {0, 2}. Similarly, π(bj, a, Fj )+π(bj+1, a, Fj )−π(bj, bj+1, Fj) ∈ {0, 2}.
Therefore, (21) implies that π(S1) + π(S2) − π(S) ∈ {0, 2, 4}.
Now, as i ̸= j ± 1 mod r, both π(S1) and π(S2) are sums of at least three numbers from {1, 2}.
Therefore, if π(S1) or π(S2) is even, they must be at least 4. As π(S) is odd, if π(S1) is even, then
π(S2) ≤ 4 + π(S) − π(S1) ≤ π(S) and π(S2) is odd. Similarly, if π(S2) is even, then π(S1) ≤ π(S)
and π(S1) is odd. Therefore, one of π(Si), i ∈ [2], is odd.
Including the repetition of b1 = br+1 and bi+1 respectively, as i ̸= j ± 1 mod r, the sequence
S1 contains i + 1 + (r + 1) − j < r + 1 vertices and the sequence S2 contains j − i + 2 < r + 1
vertices. Thus, r(S1), r(S2) < r = r(S). Therefore, taking the sequence Si′ with i′ ∈ [2] such that
π(Si′) ≤ π(S) is odd (so that the corresponding versions of K1–K3 hold for Si′) contradicts K4.

Case II. Suppose then that Fi and Fj share some vertex, say bi′, in {b1, . . . , br}. We ﬁrst show
that we can assume that bj ∈ V (Fi). If i′ = j, then this already holds. If i′ = i then switch i and
j to get the previous case of i′ = j. If i′ ̸= i − 1, i, i + 1 mod r, then keep i unchanged and relabel
j = i′. If i′ ̸= j − 1, j, j + 1 mod r, then relabel j = i and i = i′. In each case we then get i ̸= j ± 1
mod r, i ̸= j and bj ∈ V (Fi).
This leaves only the case that i′ ∈ {i − 1, i + 1} mod r and i′ ∈ {j − 1, j + 1} mod r. Therefore,
switching i and j if necessary, we have that i + 1 = i′ = j − 1 mod r. We have that bi′ = bi+1 is
in V (Fj ), and now reverse the sequence S so that, roughly speaking, bi+1 and Fi are assigned the
same index. That is, consider the sequence S ′ created by reversing S, taking that

S ′ = b′
1F ′
1b′
2F ′
2b′
3 . . . b′
rF ′
rb′
r+1 = br+1FrbrFr−1br−1 . . . b2F1b1,

where b′
j′ = br+2−j′ for each j′ ∈ [r + 1] and F ′
j′ = Fr+1−j′ for each j′ ∈ [r]. Then, b′
r+1−i = bi+1 ∈
V (Fj ) = V (F ′
r+1−j). Thus, relabelling i = r + 1 − j and j = r + 1 − i we have i ̸= j ± 1 mod r,
i ̸= j and b′
j ∈ V (F ′
i ). Using the corresponding deﬁnition for S ′ in K3, we have π(S ′) = π(S) and
r(S ′) = r = r(S), so that S ′ satisﬁes its corresponding versions of K1–K4. Thus, taking S ′ instead
of S if necessary, we can always assume that i ̸= j ± 1 mod r, i ̸= j and bj ∈ V (Fi).
Now we show that we can assume that j > i. If j < i, then consider the rotated sequence of S
in which the index i is shifted to 1, that is,

S ′′ = b′′
1F ′′
1 b
′′
2F ′′
2 b
′′
3 . . . b′′
r F ′′
r b′′
r+1 = biFibi+1 . . . brFrbr+1F1b2 . . . bi−1Fi−1bi,

bj
bi+1

bi
 b2
 b1
 br
 bj+1

Fi+1

Fi
 F1 Fr
 Fj
S2

S1
 a
 bj
bi+1

bi
 b2
 b1
 br
 bj+1

Fi+1

Fi
 F1 Fr
 Fj
S4

S3

Figure 4: The sequence S split into S1 and S2 on the left and S3 and S4 on the right.

36

where b′′
j′ = bj′+i−1 and F ′′
j′ = bj′+i−1 for each j′ ∈ [r] with addition modulo r in the indices and
b′′
r+1 = bi. Let i′′ = 1 and j′′ = r + j − i + 1, and note that i′′ < j′′ and i′′ ̸= j′′ ± 1 mod r.
Furthermore, b′′
j′′ = bj ∈ V (Fi) = V (F ′′
i′′ ). Similarly to S ′, S ′′ satisﬁes its corresponding versions of
K1–K4, and therefore, taking S ′′ instead of S if necessary, we can assume that i < j.
Thus, we have that i < j, i ̸= j ± 1 mod r and bj ∈ V (Fi). As depicted in Figure 4, consider
now the sequences

S3 = b1F1b2F2 . . . biFibjFjbj+1 . . . Frbr+1 and S4 = bjFibi+1Fi+1bi+2 . . . Fj−1bj.

We will show that one of these sequences satisﬁes K1–K3 in place of S and contradicts the mini-
mality of S in K4. That each sequence S3 and S4 satisﬁes the corresponding versions of K1 and
K2 follows immediately from K1 and K2 as bj ∈ V (Fj).
Writing
 π(S3) = ∑

1≤i′<i π(bi′, bi′+1, Fi′) + π(bi, bj, Fi) + ∑

j≤i′≤r π(bi′, bi′+1, Fi′ ),

and π(S4) = π(bj, bi+1, Fi) + ∑

i<i′<j π(bi′, bi′+1, Fi′ ),

we have
 π(S3) + π(S4) − π(S) = π(bi, bj, Fi) + π(bj, bi+1, Fi) − π(bi, bi+1, Fi). (22)

By K1 and Proposition 5.2, we have π(bi, bj, Fi) + π(bj, bi+1, Fi) − π(bi, bi+1, Fi) ∈ {0, 2}. Thus, by
(22), we have π(S3) + π(S4) − π(S) ∈ {0, 2}.
Now, as i ̸= j ± 1 mod r, both π(S3) and π(S4) are sums of at least two numbers from {1, 2},
and are therefore at least 2. As π(S) is odd, if π(S3) is even then π(S4) ≤ 2 + π(S) − π(S3) ≤ π(S)
and π(S4) is odd. Similarly, if π(S4) is even, then π(S3) ≤ π(S) and π(S3) is odd. Therefore, one
of π(Si), i ∈ {3, 4} is odd.
Including the repetition of b1 = br+1 and bj respectively, the sequence S3 contains i + (r +
1) − j + 1 < r + 1 vertices and the sequence S4 contains j − i + 1 < r + 1 vertices. Thus,
r(S3), r(S4) < r = r(S). Therefore, taking the sequence Si′ with i′ ∈ {3, 4} such that π(Si′) is odd
(so that the corresponding versions of K1–K3 hold for Si′) contradicts K4, completing the proof
of the claim. ■

Using Claim 5.3, we can show that each graph Fi in the minimal sequence S is distinct.

Claim 5.4. F1, . . . , Fr are distinct graphs in {H1, . . . , Hs}, and thus are pairwise edge disjoint.

Proof of claim. If r = 2 and F1 = F2, then K1 implies that ∑r
i=1 π(bi, bi+1, Fi) = π(b1, b2, F1) +
π(b2, b1, F2) = 2π(b1, b2, F1) = 0 mod 2, violating K3. Thus, the claim holds for r = 2 by K2.
Now suppose r ≥ 3 and that, for distinct i, j ∈ [r], Fi = Fj. Then, by Claim 5.3, it must be
that i = j ± 1 mod r. Say then, without loss of generality, that i = j − 1 mod r. Furthermore,
by relabelling the indices in the sequence S cyclically (as for S ′′ above), we can assume that i < r,
and hence j = i + 1, so that Fi = Fi+1. Consider the sequence S ′ formed from S by replacing
Fibi+1Fi+1 by Fi in S, so that

S ′ = b1F1b2F2b3 . . . bi−1Fi−1biFibi+2Fi+2 . . . brFrbr+1,

37

and note that S ′ satisﬁes its corresponding versions of K1 and K2. By Proposition 5.2 and K1, as
Fi = Fi+1, we have that π(bi, bi+1, Fi) + π(bi+1, bi+2, Fi+1) − π(bi, bi+2, Fi) ∈ {0, 2}. Then, deﬁning
π(S ′) as in K3,

π(S ′) = π(S) − π(bi, bi+1, Fi) − π(bi+1, bi+2, Fi+1) + π(bi, bi+2, Fi) ∈ {π(S), π(S) − 2}.

As π(S) is odd, π(S ′) ≤ π(S) and π(S ′) is odd. Therefore, as r(S ′) = r−1, this contradicts K4. ■

5.1.3 The right subgraphs in which to vary path lengths

Using the previous claims in this section, we can now choose a large subcollection of graphs Fi in
S, varying the paths in which leads to many odd cycles of distinct lengths. Firstly, by Claim 5.4
and relabelling, we can assume that Fi = Hi for each i ∈ [r]. Recall then that we have positive
integers ℓi, i ∈ [r], such that J holds with Hi = Fi.
Now, partition [r] as I1 ∪ I2 ∪ I3 and ﬁnd distinct vertices u1 = ur+1, u2, . . . , ur with ui, ui+1 ∈
V (Fi) for each i ∈ [r], and paths Pi, i ∈ I2 ∪ I3, such that the following hold.

L1 3 ∑i∈I1(ℓi + 1) ≥ ∑i∈[r](ℓi + 1).

L2 Any collection of paths containing exactly one ui, ui+1-path in Fi, for each i ∈ I1, and
{Pi}i∈I2∪I3 form a cycle.

L3 The paths Pi, i ∈ I2 ∪ I3, have total length ℓ0 ≤ ∑i∈I2∪I3(ℓi + 1), where ℓ0 is such that
ℓ0 + ∑i∈I1 π(ui, ui+1, Fi) is odd.

We ﬁnd the partition, vertices and paths diﬀerently depending on the length of the sequence S.
If r ≥ 4, then we are in Case 1, if r = 2, then we are in Case 2, and if r = 3 we are in Case 3.

Case 1. Suppose ﬁrst that r ≥ 4. Partition [r] = I1 ∪ I2 ∪ I3 so that, for each j ∈ [3], there
is no solution to x = y + 1 mod r with x, y ∈ Ij. Thus, by Claim 5.3, for every j ∈ [3], graphs
in {Fi : i ∈ Ij} are pairwise vertex disjoint. By averaging, there exists some j ∈ [3] such that∑i∈Ij (ℓi + 1) ≥ ∑i∈[r](ℓi + 1)/3. By relabelling, we may assume that j = 1, and hence L1 holds.
Now, for each i ∈ I2, ﬁnd a shortest path Pi between V (Fi−1) and V (Fi+1) in Fi, and label
vertices so that this is a ui, ui+1-path with ui ∈ V (Fi−1) and ui+1 ∈ V (Fi+1). Note that, by
minimality of Pi, all internal vertices of Pi lie in V (Fi) \ (V (Fi−1) ∪ V (Fi+1)). Furthermore, as
r ≥ 4, by Claim 5.3, we have that ui ̸= ui+1.
For each i ∈ I3, if i − 1, i + 1 ∈ I2, let Pi be a shortest ui, ui+1-path in Fi. If i − 1 ∈ I2 and
i + 1 /∈ I2, let Pi be a shortest path from ui to V (Fi+1) in Fi and label its endpoint in V (Fi+1) by
ui+1. If i − 1 /∈ I2 and i + 1 ∈ I2, let Pi be a shortest path from V (Fi−1) to ui+1 in Fi and label its
endpoint in V (Fi−1) by ui. If i−1, i+1 /∈ I2, let Pi be a shortest path between V (Fi−1) and V (Fi+1)
in Fi, and label vertices so that this is a ui, ui+1-path with ui ∈ V (Fi−1) and ui+1 ∈ V (Fi+1).
Note that we have chosen a vertex ui for each i ∈ [r] with i or i − 1 in I2 ∪ I3, and, for each
i ∈ I2 ∪ I3, a path Pi. As there is no solution to x = y + 1 mod r in I1, {i, i + 1 : i ∈ I2 ∪ I3} = [r].
Thus, we have in fact chosen vertices ui for all i ∈ [r]. To see that vertices ui, i ∈ [r], are distinct,
note that, for each i ∈ [r], we chose ui ∈ V (Fi−1) ∩ V (Fi). Therefore, if there is some i ̸= j with
ui = uj, then as uj ∈ V (Fi−1) ∩ V (Fi) and r ≥ 4, by Claim 5.3, we must have j = i − 1 mod r.
However, similarly, as ui ∈ V (Fj−1) ∩ V (Fj), we must have i = j − 1 mod r, a contradiction.

38

Let ur+1 = u1. For each i ∈ I2 ∪ I3, Pi was a shortest path between two vertices in Fi, and thus
by J, has length at most ℓi + 1. Observe crucially that, by our careful selection of shortest paths,
the paths in {Pi : i ∈ I2 ∪ I3} are pairwise internally disjoint, and furthermore internally disjoint
from any ui, ui+1-path in Fi for any i ∈ I1. In particular, this, together with the graphs Fi, i ∈ I1,
being pairwise vertex disjoint, implies that L2 holds. It is left to show that L3 holds. Let ℓ0 be
the total length of the paths Pi, i ∈ I2 ∪ I3. As, for each i ∈ I2 ∪ I3, Pi has length at most ℓi + 1,
we have ℓ0 ≤ ∑i∈I2∪I3(ℓi + 1), as required in L3.
For the rest of L3, we need to show that ℓ0 + ∑i∈I1 π(ui, ui+1, Fi) is odd. Now, as r ≥ 4, we
have π(S) ≥ 5 by K3, and hence π(S) + r(S) ≥ 9. Now, suppose for some i, j ∈ [r] with j = i − 1
mod r, π(ui, bi, Fi) + π(ui, bi, Fj) is odd. Then, ui ̸= bi, and therefore π(ui, bi, Fi) + π(ui, bi, Fj ) = 3.
Thus, the sequence S ′ = uiFibiFjui has π(S ′) + r(S ′) = 5 and satisﬁes its corresponding version of
K1–K3, contradicting K4. Therefore, working mod r in the indices, for each i ∈ [r], we have

π(ui, bi, Fi) + π(ui, bi, Fi−1) = 0 mod 2. (23)

Futhermore, for each i ∈ [r], we have by two applications of (the second part of) Proposition 5.2,
that

π(ui, ui+1, Fi) = π(ui, bi, Fi)+π(bi, ui+1, Fi) = π(ui, bi, Fi)+π(bi, bi+1, Fi)+π(bi+1, ui+1, Fi) mod 2.

Thus, working mod r in the indices, we have
∑

i∈[r] π(ui, ui+1, Fi) = ∑

i∈[r] π(ui, bi, Fi) + ∑

i∈[r] π(bi, bi+1, Fi) + ∑

i∈[r] π(bi+1, ui+1, Fi) mod 2

= ∑

i∈[r] π(bi, bi+1, Fi) + ∑

i∈[r]
(π(ui, bi, Fi) + π(ui, bi, Fi−1)) mod 2

(23)
= ∑

i∈[r] π(bi, bi+1, Fi) mod 2.

For each i ∈ I2 ∪ I3, Pi is a ui, ui+1-path in Fi, and therefore has length equal to π(ui, ui+1, Fi)
mod 2. Thus, ℓ0 is equal to ∑i∈I2∪I3 π(ui, ui+1, Fi) mod 2. Therefore,

ℓ0 + ∑

i∈I1 π(ui, ui+1, Fi) = ∑

i∈[r] π(ui, ui+1, Fi) = ∑

i∈[r] π(bi, bi+1, Fi) mod 2.

Combined with K3, we have that ℓ0 + ∑i∈I1 π(ui, ui+1, Fi) is odd, completing the proof of L3.

Case 2. Suppose then that r = 2. Assume, by relabelling that ℓ1 ≥ ℓ2 and let I1 = {1}, I2 = {2}
and I3 = ∅. Note that L1 holds. By K3, we have that π(b1, b2, F1) + π(b1, b2, F2) is odd. Find
distinct vertices u1, u2 ∈ V (F1) ∩ V (F2) and a u1, u2-path P2 in F2 so that ℓ(P2) + π(u1, u2, F1) is
odd, and subject to this P2 has the shortest possible length. Note that this is possible as taking
u1 = b1, u2 = b2 and letting P2 be any u1, u2-path in F2 (which exists due to J) satisﬁes these
conditions, and, furthermore, by J, P2 has length at most ℓ2 + 1. Therefore, L3 holds for P2.
Now, suppose P2 has some internal vertex u in F1. Then, note u ∈ V (P2) ⊆ V (F2), and split
P2 as a u1, u-path Q1 and a u, u2-path Q2. By Proposition 5.2, we have, working mod 2, that

1 = ℓ(P2) + π(u1, u2, F1) = ℓ(Q1) + π(u1, u, F1) + ℓ(Q2) + π(u, u2, F1) mod 2.

39

Therefore, one of ℓ(Q1) + π(u1, u, F1) or ℓ(Q2) + π(u, u2, F1) must be odd, contradicting the mini-
mality of P2. Therefore, P2 has no internal vertices in F1, and hence L2 holds.

Case 3. Suppose ﬁnally that r = 3. Assume, by relabelling, that ℓ1 = maxi∈[r] ℓi and let I1 = {1},
I2 = {2} and I3 = {3}. Note that L1 holds.
Let us ﬁrst show that F1 ∪ F2, F2 ∪ F3, and F1 ∪ F3 are bipartite. Suppose, for contradiction,
that F2 ∪ F3 is not bipartite, and let A, B and A′, B′ be the bipartitions of F2 and F3, labelled so
that b3 ∈ A ∩ A′. As A ∪ A′, B ∪ B′ is not a bipartition of F2 ∪ F3, there must be some vertex, u
say, in A ∩ B′ or A′ ∩ B. Then, π(b3, u, F2) + π(u, b3, F3) = 3. Thus, S ′ = b3F2uF3b3 satisﬁes the
corresponding version of K1–K3 with r(S ′) + π(S ′) = 5. By K1 and K3, π(S) ≥ 3, and therefore
π(S) + r(S) ≥ 6, contradicting K4. Therefore, F2 ∪ F3 must be bipartite. Similarly, F1 ∪ F2 and
F1 ∪ F3 are bipartite.
As F2 ∪ F3 is bipartite, we have, by Proposition 5.2, that

π(b2, b4, F2 ∪ F3) = π(b2, b3, F2 ∪ F3) + π(b3, b4, F2 ∪ F3) = π(b2, b3, F2) + π(b3, b4, F3) mod 2.

Let Q be a shortest b2, b4-path in F2 ∪F3, so that ℓ(Q) = π(b2, b4, F2 ∪F3) mod 2. As F2 and F3
have diameter at most ℓ2 + 1 and ℓ3 + 1 respectively by J, we have ℓ(Q) ≤ ℓ2 + ℓ3 + 2. As b4 = b1, Q
is a b1, b2-path. Now, ﬁnd distinct vertices u1, u2 with u1 ∈ V (F1) ∩ V (F3) and u2 ∈ V (F1) ∩ V (F2),
and a u1, u2-path P2 in F2 ∪ F3 so that ℓ(P2) + π(u1, u2, F1) is odd, and subject to this ℓ(P2) has
the shortest possible length. Note that such a shortest path P2 indeed exists as the path Q satisﬁes
the other requirements with u1 = b1 and u2 = b2 as ℓ(Q) + π(b1, b2, F1) is odd due to K3. Thus,
ℓ(P2) ≤ ℓ(Q) ≤ ℓ2 + ℓ3 + 2. Let P3 be the path with only the vertex u2. Therefore, L3 holds for
P2 and P3.
Suppose to the contrary that P2 has some internal vertex u in F1. Then, note u ∈ V (P2) ⊆
V (F2), and split P2 as a u1, u-path Q1 and a u, u2-path Q2. By Proposition 5.2, we have

1 = ℓ(P2) + π(u1, u2, F1) = ℓ(Q1) + π(u1, u, F1) + ℓ(Q2) + π(u, u2, F1) mod 2.

Therefore, one of ℓ(Q1) + π(u1, u, F1) or ℓ(Q2) + π(u, u2, F1) must be odd, contradicting the mini-
mality of P2. Therefore, P2 has no internal vertices in F1, and hence L2 holds.
Now, combining P2 with any u1, u2-path in F1 with length equivalent to π(u1, u2, F1) mod 2
gives an odd cycle. Thus, as both F1 ∪ F2 and F1 ∪ F3 are bipartite, P2 must have some edge
from F2 and some edge from F3, and hence we can pick u3 as an arbitrary internal vertex of P2 in
V (F2) ∩ V (F3). This completes the partition [3] = I1 ∪ I2 ∪ I3, distinct vertices u1, u2 and u3, with
u1, u2 ∈ V (F1), u2, u3 ∈ V (F2) and u3, u1 ∈ V (F3), and paths P2 and P3 such that L1–L3 hold.

5.1.4 Varying paths in the chosen subgraphs

Thus, in each of the three cases, we have a partition [r] = I1 ∪ I2 ∪ I3, distinct vertices u1 =
ur+1, u2, . . . , ur with ui, ui+1 ∈ V (Fi) for each i ∈ [r], and paths Pi, i ∈ I2 ∪ I3, for which L1–L3
hold. Let
 ℓ = ℓ0 + ∑

i∈I1(ℓi + 1) L3
≤ ∑

i∈[r]
(ℓi + 1) L1
≤ 3 ∑

i∈I1(ℓi + 1). (24)

Now, if ℓ′
i, i ∈ I1, is a collection of integers satisfying ℓ′
i ∈ [ℓi, ℓi · k1−ε/2] and ℓ′
i = π(ui, ui+1, Fi)
mod 2, for each i ∈ I1, then, by taking a ui, ui+1-path in Fi with length ℓ′
i by J, for each i ∈ I1, and
combining these paths with the paths Pi, i ∈ I2 ∪ I3, by L2 we get a cycle with length ℓ0 + ∑i∈I1 ℓ′
i.

40

As, by L3, ℓ0 + ∑
i∈I1 π(ui, ui+1, Fi) is odd, there are sets of such numbers ℓ′
i, i ∈ I1, with
ℓ0 + ∑i∈I1 ℓ′
i = t for any odd number t such that

ℓ0 + ∑

i∈I1(ℓi + 1) ≤ t ≤ ℓ0 + ∑

i∈I1(⌊ℓi · k1−ε/2⌋ − 1).

Now, we have ℓ = ℓ0 + ∑i∈I1(ℓi + 1), so, as kε/2 ≥ d
ε/2
0 ≥ 8, we have

ℓ0 + ∑

i∈I1(⌊ℓi · k1−ε/2⌋ − 1) ≥ ∑

i∈I1(ℓi · k1−ε/2 − 2) ≥ ∑

i∈I1(8ℓi · k1−ε − 2) ≥ ∑

i∈I1(3ℓi + 3) · k1−ε (24)
≥ ℓ · k1−ε.

Thus, for each odd integer t ∈ [ℓ, ℓ · k1−ε], G contains a cycle with length t. This completes the
proof of Theorem 1.4.

Acknowledgements

We are very grateful to Benny Sudakov, and the referee, for suggestions that improved the presen-
tation of this paper.

References

[1] N. Alon and J. H. Spencer. The Probabilistic Method. John Wiley & Sons, 2004.

[2] B. Bollob´as. Cycles modulo k. Bulletin of the London Mathematical Society, 9(1):97–98, 1977.

[3] B. Bollob´as and A. Thomason. Proof of a conjecture of Mader, Erd˝os and Hajnal on topological
complete subgraphs. European Journal of Combinatorics, 19(8):883–887, 1998.

[4] P. Erd˝os. Some recent progress on extremal problems in graph theory. Congr. Numer, 14:3–14,
1975.

[5] P. Erd˝os. Problems and results in graph theory. The theory and applications of graphs (Kala-
mazoo, MI, 1980), pages 331–341, 1981.

[6] P. Erd˝os. Some new and old problems on chromatic graphs. Combinatorics and applications,
pages 118–126, 1984.

[7] P. Erd˝os. Some old and new problems in various branches of combinatorics. Discrete Mathe-
matics, 165:227–231, 1997.

[8] P. Erd˝os and A. Hajnal. On chromatic number of graphs and set-systems. Acta Mathematica
Hungarica, 17(1-2):61–99, 1966.

[9] A. Gy´arf´as. Graphs with k odd cycle lengths. Discrete Mathematics, 103(1):41–48, 1992.

[10] A. Gy´arf´as, J. Koml´os, and E. Szemer´edi. On the distribution of cycle lengths in graphs.
Journal of Graph Theory, 8(4):441–462, 1984.

41

[11] J. Kim, H. Liu, M. Sharifzadeh, and K. Staden. Proof of Koml´os’s conjecture on Hamiltonian
subsets. Proceedings of the London Mathematical Society, 115(5):974–1013, 2017.

[12] J. Koml´os and E. Szemer´edi. Topological cliques in graphs. Combinatorics, Probability and
Computing, 3(2):247–256, 1994.

[13] J. Koml´os and E. Szemer´edi. Topological cliques in graphs II. Combinatorics, Probability and
Computing, 5(1):79–90, 1996.

[14] K. Kuratowski. Sur le probleme des courbes gauches en topologie. Fund. Math., 16:271–283,
1930.

[15] H. Liu and R. Montgomery. A proof of Mader’s conjecture on large clique subdivisions in
C4-free graphs. Journal of the London Mathematical Society, 95(1):203–222, 2017.

[16] W. Mader. Homomorphieeigenschaften und mittlere Kantendichte von Graphen. Mathematis-
che Annalen, 174(4):265–268, 1967.

[17] W. Mader. Hinreichende Bedingungen f¨ur die Existenz von Teilgraphen, die zu einem
vollst¨andigen Graphen hom¨oomorph sind. Mathematische Nachrichten, 53(1-6):145–150, 1972.

[18] B. Sudakov and J. Verstra¨ete. Cycle lengths in sparse graphs. Combinatorica, 28:357–372,
2008.

[19] B. Sudakov and J. Verstra¨ete. Cycles in graphs with large independence ratio. Journal of
Combinatorics, 2(1):83–102, 2011.

[20] C. Thomassen. Subdivisions of graphs with large minimum degree. Journal of Graph Theory,
8(1):23–28, 1984.

[21] C. Thomassen. Problems 20 and 21. In Graphs, Hypergraphs and Applications. H. Sachs, Ed.:
217. Teubner. Leipzig., 1985.

[22] C. Thomassen. Conﬁgurations in graphs of large minimum degree, connectivity, or chromatic
number. In Proceedings of the third international conference on Combinatorial mathematics,
pages 402–412, 1989.

[23] J. Verstra¨ete. Unavoidable cycle lengths in graphs. J. Graph Theory, 49:151–167, 2005.

[24] J. Verstra¨ete. Extremal problems for cycles in graphs. In Recent trends in combinatorics,
pages 83–116. Springer, 2016.
 42
