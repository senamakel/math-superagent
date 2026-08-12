<!-- source: https://bibliotekanauki.pl/articles/30148697.pdf | converted from PDF -->

Discussiones Mathematicae
Graph Theory 34 (2014) 635–640
doi:10.7151/dmgt.1732
 Note

ON THE ERD ˝OS-GY ´ARF ´AS CONJECTURE
IN CLAW-FREE GRAPHS

Pouria Salehi Nowbandegani1, Hossein Esfandiari2

Mohammad Hassan Shirdareh Haghighi1 and Khodakhast Bibak3

1 Department of Mathematics
Shiraz University
Shiraz 71454, Iran

2Department of Computer Science
University of Maryland College Park
College Park, MD 20742, USA

3 Department of Combinatorics and Optimization
University of Waterloo
Waterloo, Ontario, Canada N2L 3G1

e-mail: pouria.salehi@gmail.com
hossein@cs.umd.edu
shirdareh@susc.ac.ir
kbibak@uwaterloo.ca

Abstract

The Erd˝os-Gy´arf´as conjecture states that every graph with minimum
degree at least three has a cycle whose length is a power of 2. Since this
conjecture has proven to be far from reach, Hobbs asked if the Erd˝os-Gy´arf´as
conjecture holds in claw-free graphs. In this paper, we obtain some results
on this question, in particular for cubic claw-free graphs.

Keywords: Erd˝os-Gy´arf´as conjecture, claw-free graphs, cycles.

2010 Mathematics Subject Classiﬁcation: C5038, C5038.

1. Introduction

All graphs in this paper are assumed to be simple, that is, without any loops and
multiple edges. Let us ﬁrst recall here brieﬂy some notation and terminology we
will need in this paper. We denote by δ = δ(G) the minimum degree of the the
vertices in the graph G = (V, E). A uv-path is a path having the vertices u and

636 P. Salehi, H. Esfandiari, M.H. Shirdareh and Kh. Bibak

v as its ends. The length of a path P (or a cycle C) is denoted by l(P ) (resp.
l(C)). Also, we denote the distance between the vertices u and v by d(u, v), that
is the length of a shortest uv-path. A graph that does not contain a particular
graph H as an induced subgraph is called H-free. The complete bipartite graph
K1,3 is referred to as a claw ; so a graph is called claw-free if it does not have K1,3
as an induced subgraph. A triangle is a cycle of length three. A chord of a cycle
C is an edge between two vertices of C which are not adjacent in C. By a hole
we mean a chordless cycle of length at least four. A hole of length n is called an
n-hole.
Several questions on cycles in graphs have been posed by Erd˝os and his
colleagues (see, e.g., [1]). In particular, in 1995 Erd˝os and Gy´arf´as [4] asked:
If G is a graph with minimum degree at least three, does G have a cycle whose
length is a power of 2?
This is known as the Erd˝os-Gy´arf´as conjecture. In fact, Erd˝os and Gy´arf´as [4]
said that “we are convinced now that this is false and no doubt there are graphs
for every r every vertex of which has degree ≥ r and which contain no cycle of
length 2k, but we never found a counterexample even for r = 3”.
There seems to be very little published on the Erd˝os-Gy´arf´as conjecture.
Markstr¨om [5] (via computer searches) asserted that any cubic counterexample
must have at least 30 vertices. Salehi Nowbandegani and Esfandiari [6] prove
that any bipartite counterexample must have at least 32 vertices.
More generally, Erd˝os asked does there exist an integer sequence a1, a2, a3, . . .
with zero density, and a constant c such that every graph with average degree
at least c contains a cycle of length ai for some i. This question is answered
aﬃrmatively by Verstra¨ete [8].
Hobbs asked if the Erd˝os-Gy´arf´as conjecture holds in claw-free graphs [3].
Shauger [7] proved the conjecture for K1,m-free graphs having minimum degree
at least m + 1 or maximum degree at least 2m − 1. Also, Daniel and Shauger
[3] proved it for planar claw-free graphs. In this paper, we investigate claw-free
graphs with δ ≥4 and cubic claw-free graphs.

2. Two-power Cycle Lengths in Claw-free Graphs

Our ﬁrst theorem concerns claw-free graphs with δ ≥ 3.

Theorem 1. Suppose that G is a claw-free graph with δ ≥ 3. Then G has a cycle
whose length is 2k, or 3 · 2k, for some positive integer k.

To prove Theorem 1 we need the following lemma.

Lemma 2. Let G be a graph with δ ≥ 3. If G does not have C4 as a subgraph,
then for some n ≥ 5 it has an n-hole.

On the Erd˝os-Gy´arf´as Conjecture in Claw-free Graphs 637

Proof. It is known that every graph with δ ≥ 2 contains a cycle of length at
least δ + 1 (see, e.g., [2, Exercise 2.1.5]). Thus G has a cycle D1 of length n1 ≥ 5.
If n = 5, D1 must clearly be chordless. If n > 5, and D1 has no chord, we are
ﬁnished, so suppose D1 has a chord. The chord separates D1 into two shorter
cycles, none of which have length 4, by assumption. Thus at least one of these
two cycles, say D2, must have length 5 ≤ n2 < n1. Since G is ﬁnite, we must by
repeating this argument eventually ﬁnd a chordless cycle Dk of length nk ≥ 5.

Deﬁnition. We call an edge of a graph triangulated if it is contained in a triangle.
Also if such a triangle is unique, we call the edge uniquely triangulated.

Now we are ready to prove Theorem 1.

Proof of Theorem 1. If G has a cycle of length four, the theorem holds, with
k =2. We may therefore assume that G does not contain any C4. Thus, by
Lemma 2, for some n ≥ 5, G has an n-hole. Let C : a1a2 . . . asa1, s ≥ 5, be a
smallest hole in G. Since δ ≥ 3 and C is a hole, each vertex of C has a neighbour
in G − V (C). For i, (1 ≤ i ≤ s), suppose that aibi ∈ E(G), where ai ∈ C and
bi ∈ V (G) \ V (C). Then either ai−1bi ∈ E(G), or ai+1bi ∈ E(G), because G is
claw-free. Now we show that bi ̸= bj if |j − i| ≥ 2. To get a contradiction, ﬁx i
and let aj be the ﬁrst vertex of C after ai such that bi = bj = b, |j − i| ≥ 2. If
j − i = 2, then we get the C4 : aiai+1ai+2bai, which is absurd. If |j − i| > 2, then
we get the hole ai+1 · · · ajbai+1 which is certainly smaller than C (note that we
do not reject the case that this hole may be a C4).
Therefore, it follows that every other edge of C is uniquely triangulated;
we mark them. Moreover, the third vertices of the corresponding triangles are
disjoint. Note also that s is even. Consequently, we ﬁnd cycles of lengths s, s +
1, . . . , 3
2 s by traversing C such that as we reach a marked edge, we pass it directly
or through the third vertex of its corresponding triangle. Since either there exists
a 2k or a 3 · 2k−1 between s and 3
2 s, the proof is complete.

As mentioned above, Shauger [7] proved the Erd˝os-Gy´arf´as conjecture for K1,m-
free graphs having minimum degree at least m + 1 or maximum degree at least
2m − 1. Theorem 5 improves on the result of Shauger in claw-free graphs. First
we state the following proposition. We omit the easy proof.

Proposition 3. In a 4-regular claw-free graph which does not contain C4, every
edge is uniquely triangulated.

Lemma 4. Let G be a 4-regular claw-free graph which does not contain C4 and v
be a vertex of G. Let C be a smallest n-hole in G containing v, n ≥ 5. Then for
every edge xy of C, the third vertex z = z(xy) of the corresponding triangle of xy
is out of C. Furthermore, if uw ̸= xy are two edges of C, then z(uw) ̸= z(xy).

638 P. Salehi, H. Esfandiari, M.H. Shirdareh and Kh. Bibak

Proof. First note that since C is a hole, for every edge xy in C, z = z(xy) /∈ C.
Let uw and wx be two consecutive edges in C. If z = z(uw) = z(wx), then we get
the C4 : uwxzu. Hence z(uw) ̸= z(wx). Suppose that uw and xy are two non-
consecutive edges in C and suppose C traverses the vertices in order u, w, x, y,
and then v. Let Q be the yvu segment of C. Now if z = z(uw) = z(xy), then
the cycle uQyzu is a smaller hole containing v; unless u and y are adjacent in C
(and hence v is one of them). But in this case, we see that uzxyu is a C4 in G.
This contradiction shows that z(uw) = z(xy) for uw ̸= xy is impossible.

Theorem 5. Let G be a claw-free graph with δ ≥ 4, which does not contain C4.
Then every non-cut vertex of G lies on a cycle whose length is a power of 2.

Proof. Since δ ≥ 4 and G is claw-free, if G has a vertex with degree at least
5, then this vertex lies on a C4; so we can assume that G is 4-regular. Suppose
that v is a non-cut vertex of G and let w, x, y, and u be its neighbours. Hence,
G − v is connected. In view of G is claw-free, we can assume that wu, xy ∈ E(G).
Let P1, P2, P3, and P4 be the shortest wy-path, wx-path, xu-path, and yu-path
in G − v, respectively. Also, without loss of generality assume that l(P1) =
min{l(P1), l(P2), l(P3), l(P4)}. The path P1 together with the edges vw and vy
make a cycle C. Clearly, l(P1) > 1, otherwise ywuvy will be a C4. Therefore,
l(C) = s ≥ 5. Since P1 was the shortest path among P1, P2, P3, and P4, we see
that neither x nor u are in P1 and, in fact, C is the shortest non-triangle hole
containing the vertex v; for if v lies on another non-triangle shorter hole, then two
of its neighbours would have distance less than l(P1) in G − v. By Lemma 4, each
edge of C is uniquely triangulated such that the third vertex of its corresponding
triangle is not on C and this correspondence is one to one. Since l(C) = s, then
G contains cycles of lengths s, s + 1, . . . , 2s. For, as in the proof of Theorem 1,
when we traverse the vertices of C, we can either pass the two ends of every edge
directly or through the third vertex of its corresponding triangle.
This implies that G has a cycle containing v whose length is 2k, for some
k ≥ 3.

3. The Erd˝os-Gy´arf´as Conjecture in Cubic Claw-free Graphs

In this section, we investigate the Erd˝os-Gy´arf´as conjecture in cubic claw-free
graphs. Indeed, we discuss on the cubic claw-free graphs for which the Erd˝os-
Gy´arf´as conjecture possibly does not hold.
Suppose that G is a cubic claw-free graph that does not contain C4. Let v be
an arbitrary vertex of G, and let its neighbours be x, y, and z. Since G is claw-free,
so we can assume that xy ∈ E(G). Thus, xz, yz /∈ E(G); otherwise a C4 appears.
Let x1 and y1 be respectively the other neighbours of x and y. Easily we see that

On the Erd˝os-Gy´arf´as Conjecture in Claw-free Graphs 639

x1 ̸= y1. Therefore, for every vertex there exists a unique triangle containing
it, such that the other neighbours of its vertices are distinct. Hence G consists
of some vertex-disjoint triangles which are connected by a perfect matching of
G. Furthermore, if two vertices from two triangles are matched, then there is
no more link between these two triangles, again because we have no C4 in G.
This means if we look locally at the graph, we see a triangle together with three
appended edges, such that these edges connect to three disjoint triangles. Now
deﬁne ˆG to be the graph whose vertices are triangles of G and two vertices are
adjacent in ˆG whenever their corresponding triangles in G are linked by an edge.
The graph ˆG is then a simple cubic graph. We can imagine ˆG as a graph obtained
from G by shrinking each triangle to a vertex.
Conversely, we can start from a simple cubic graph ˆG and replacing each
vertex v with a triangle T ; linking the three vertices of T to the three triangles
corresponding to the three neighbours of v. This procedure results in a cubic
claw-free graph G without C4. To sum up, we have the following proposition.

Proposition 6. The mapping G ↔ ˆG is a one to one correspondence between
simple cubic graphs and simple cubic claw-free graphs without C4.

Corollary 7. If ˆG contains a cycle of length k, then this cycle provides cycles of
lengths 2k, 2k + 1, . . . , 3k in G.

Proof. Consider a cycle ˆC of length k in ˆG. The subgraph S of G corresponding
to ˆC consists of a cycle of length 2k such that every other edge of it is triangulated.
Hence we can ﬁnd cycles of lengths 2k, 2k + 1, . . . , 3k in S.

Based on Proposition 6 and Corollary 7, we think the following conjecture is true.

Conjecture 8. Every cubic graph contains a cycle of length l such that 2l ≤
2k < 3l, for some positive integer k.

If this conjecture holds, it will lead to a proof of the Erd˝os-Gy´arf´as conjecture in
cubic claw-free graphs. Also note that this conjecture can be easily deduced from
the Erd˝os-Gy´arf´as conjecture. But for simplicity, we restrict ourselves to cubic
graphs, and the length of the desired cycle has a very wide range.
At the end, we investigate minimal cubic claw-free graphs which possibly
have no cycle with length a power of 2.

Theorem 9. Any counterexample to the Erd˝os-Gy´arf´as conjecture in cubic claw-
free graphs must have at least 114 vertices.

Proof. Let G be a claw-free cubic graph of order 3n. Then ˆG (deﬁned in Propo-
sition 6) is a cubic graph of order n. By Corollary 7, if ˆG contains a cycle of
length l, where l ∈ {2, 3, 4, 6, 7, 8}, then the Erd˝os-Gy´arf´as conjecture holds for

640 P. Salehi, H. Esfandiari, M.H. Shirdareh and Kh. Bibak

G. So let us assume that ˆG does not contain such cycles. Let v0 be a vertex of
ˆG. We consider {v0} as level 0, and deﬁne level i, i ≥ 1, as the set

Li = {v ∈ V ( ˆG) : d(v, v0) = i}.

Clearly, L1 is an independent set. It is easy to see that the subgraph induced by
L2 has at most one edge. One can check that if the subgraph induced by L2 has
no edge, then the subgraph induced by L3 has at most three edges, and if the
subgraph induced by L2 has one edge, then the subgraph induced by L3 has at
most one edge. No two elements of L3 have common neighbours in L4, because
otherwise, ˆG contains the cycles of lengths 2, 4, 6, or 8. An easy calculation
shows that ˆG has at least 38 vertices. Consequently, any counterexample for the
Erd˝os-Gy´arf´as conjecture must have at least 3 × 38 = 114 vertices.

Acknowledgments

The authors would like to thank anonymous referees for helpful mathematical
and grammatical comments.
 References

[1] J.A. Bondy, Extremal problems of Paul Erd˝os on circuits in graphs, in: Paul Erd˝os
and his Mathematics, II, Bolyai Soc. Math. Stud., 11, Janos Bolyai Math. Soc.,
Budapest (2002), 135–156.

[2] J.A. Bondy and U.S.R. Murty, Graph Theory (Springer-Verlag, New York, 2008).

[3] D. Daniel and S.E. Shauger, A result on the Erd˝os-Gy´arf´as conjecture in planar
graphs, Congr. Numer. 153 (2001) 129–140.

[4] P. Erd˝os, Some old and new problems in various branches of combinatorics, Discrete
Math. 165/166 (1997) 227–231.
doi:10.1016/S0012-365X(96)00173-2

[5] K. Markstr¨om, Extremal graphs for some problems on cycles in graphs, Congr. Nu-
mer. 171 (2004) 179–192.

[6] P. Salehi Nowbandegani and H. Esfandiari, An experimental result on the Erd˝os-
Gy´arf´as conjecture in bipartite graphs, 14th Workshop on Graph Theory CID,
September 18–23, 2011, Szklarska Por¸eba, Poland.

[7] S.E. Shauger, Results on the Erd˝os-Gy´arf´as conjecture in K1,m-free graphs, Congr.
Numer. 134 (1998) 61–65.

[8] J. Verstra¨ete, Unavoidable cycle lengths in graphs, J. Graph Theory 49 (2005) 151–
167.
doi:10.1002/jgt.20072
 Received 29 August 2012
Revised 6 February 2013
Accepted 6 February 2013

Powered by TCPDF (www.tcpdf.org)
