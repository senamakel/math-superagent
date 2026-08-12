<!-- source: https://arxiv.org/pdf/1403.5636 | converted from PDF -->

arXiv:1403.5636v1  [math.CO]  22 Mar 2014Three Graphs and the Erd˝os-Gy´arf´as Conjecture

Geoﬀrey Exoo
Department of Mathematics and Computer Science
Indiana State University
Terre Haute, IN 47809
ge@cs.indstate.edu

Dec 24, 2013

Abstract

Three graphs related to the Erd˝os-Gy´arf´as Conjecture are presented.
The graphs are derived from the Buckyball, the Petersen graph, and the
Tutte-Coxeter graph. The ﬁrst graph is a partial answer to a question
posed by Heckman and Krakovski [1] in their recent work on the planar
version of the conjecture. The other two graphs appear to be the smallest
known cubic graphs with no 2
m-cycles for m ≤ 4 and for m ≤ 5.

1 Introduction.

The Erd˝os-Gy´arf´as Conjecture asserts that every graph with minimum degree
at least 3 contains a cycle whose length is a power of 2. Recently, Heckman and
Krakovski [1] proved the conjecture for 3-connected cubic planar graphs.

Theorem (Heckman and Krakovski). Every 3-connected planar graph con-
tains a 2m-cycle, for some m ≤ 7.

The authors suggest that the upper bound of 7 might be improved, and that
a value as low as 4 may be possible. In this note, we show that the bound on
m must be at least 5 by constructing a 3-connected cubic planar graph with
neither 4, 8, nor 16 cycles. Then we consider the general problem of ﬁnding,
for a given integer k, the smallest 2m-cycle free cubic graphs for all m < k,
and describe graphs for k = 4 and k = 5 that appear to be the smallest known
examples.

2 A 3-connected cubic planar graph with no cy-
cles of length 4, 8 or 16.

The construction is based on the truncated icosahedron, known to chemists as
C60, the buckminsterfullerene [2], or more popularly as the buckyball. We recall

1

some of the well-known graph theoretic properties of C60. It is a 3-connected
cubic planar vertex-transtive graph of order 60. It contains twelve 5-cycles and
twenty 6-cycles, all of which border faces in a plane drawing of the graph, such
as the one in Figure 1.

Figure 1: The graph of the buckyball.

Under the action of the automorphism group there are two edge orbits.
One orbit contains 60 edges, each of which borders one pentagonal face and
one hexagonal face. These edges are called single-bond edges by chemists, a
terminology we also adopt. The other edge orbit contains the 30 edges that
border two hexagonal faces. These are called double-bond edges. Each vertex is
incident with two single-bond edges and one double-bond edge. It will also be
important to note that C60 contains no other cycle of length less than nine.
To obtain a graph with no 4, 8 or 16 cycles, we replace each vertex in C60
by a copy of the graph H7 shown in Figure 2. The three edges incident with
the replaced buckyball vertex are attached to the vertices labeled u, v and w in
Figure 2. The attachment is done so that vertex u is incident with the double-
bond edge. Since H7 has three vertices of degree 2, and four vertices of degree 3,
the resulting graph will evidently be a 3-connected cubic planar graph of order
420. We denote the graph by G420.
 2

v w

u

Figure 2: The vertex replacement graph H7.

It will be convenient to refer to the natural projection from V (G420) to
V (C60) in which the vertices in each copy of H7 are projected onto the replaced
vertex.
To see that G420 contains no 2m cycles for m ≤ 4, observe that H7 contains
no 2m-cycles for any m, so any such cycle in G420 would project to a cycle in
C60. Consider ﬁrst the cycles of G420 that project to hexagonal face cycles.
Since the minimum distance in H7 between any pair of the attachment vertices
(u, v and w) is at least 2, any such cycle must contain at least 12 edges from
copies of H7, along with 6 edges joining diﬀerent copies, and hence have length
at least 18. Next consider cycles from G420 that project to pentagonal faces.
Since the distance in H7 from v to w is three, each such cycle contains at least
15 edges from copies of H7, along with 5 edges joining the copies, and so has
length at least 20. Finally, because C60 contains no other cycles of length less
than nine, one ﬁnds that there are no 2m cycles in G420 for m ≤ 4 as claimed.

3 The general case.

Next we consider the following variant of Erd˝os-Gy´arf´as Conjecture.

Problem. For k ≥ 3, what are the smallest cubic graphs with no 2m-cycles, for
m ≤ k?

Denote the order of a smallest graph by f (k). It is easy to check that
f (2) = 10. There are three cubic graphs of order 10 with no 4-cycles (including
the Petersen graph) and none of smaller order. Markstr¨om [3] showed that
f (3) = 24, and listed all four minimal graphs. In fact, the graph H7 can viewed
as playing a role in one of Markstr¨om’s graphs. This particular graph can be
obtained from K4 by replacing three of the vertices of K4 by H7 and replacing
the fourth vertex by a copy of K3.
H7 can also be used to construct what appears to be the smallest known
example of a graph with no 2m-cycles for m ≤ 4. In this construction, one
begins with the Petersen graph, drawn as in Figure 3

3

Figure 3: The Petersen graph.

Next we replace the central vertex by a copy of K3 as shown in Figure 4.

Figure 4: G12, the graph obtained from the Petersen graph by replacing one
vertex by a triangle.

The ﬁnal step is to replace all but one of the vertices in G12 with a copy of
H7. In Figure 5 we indicate how this can be done. The solid vertex in the ﬁgure
is the vertex that is not replaced by a copy of H7. The heavy boxes attached to
each of the the other vertices mark the edge that will be incident with vertex
u in that copy of H7. We thus obtain G78, a cubic graph of order 78. To see
that there are no 4, 8 or 16 cycles in G78 one can check all possible cycles that
project from G78 to the single 3-cycle, the six 5-cycles and the ten 6-cycles in

4

G12. The details are left to the reader.

Figure 5: Replacing 11 of the vertices by H7.

The ﬁnal construction gives a graph with no 2m-cycles, for m ≤ 5. It is
based on the girth 8 Tutte-Coxeter graph shown in Figure 6 and on the vertex
replacement graph H15 shown in Figure 7. Note that H15 consists of two copies
of H7 with one extra vertex, and that there are no 2m-cycles in H15. Note also
that the distance in H15 from u to either v or w is 3, while the distance from v
to w is 5.
If one replaces each vertex of Tutte-Coxeter by a copy of H15, there are
clearly no 2m-cycles for m ≤ 4, but if the replacement is done in an arbitary
manner, 32-cycles may result. To avoid this one must be a little careful. Each
vertex of Tutte-Coxeter is incident with two edges on the outer Hamiltonian
cycle (in Figure 6) and with one chord edge. If we replace each Tutte-Coxeter
vertex so that vertex u in each copy of H15 is incident with a chord edge,
then 32-cycles will be avoided. This follows from the observation that any 8-
cycle in Tutte-Coxeter contains (at least) two consecutive edges on the outer
Hamiltonian cycle, and therefore at least one v-w path in a copy of H15. The
resulting graph has order 450 and no 2m-cycles for m ≤ 5, and therefore f (5) ≤
450.
We summarize the known values and bounds on f in the table at the end of
this note. The lower bound for f (4) is an unpublished result of Markstr¨om.

5

Figure 6: The Tutte-Coxeter graph.
 wv
 u

Figure 7: A larger vertex replacement graph H15.

6

k f (k)
2 10
3 24
4 54 – 78
5 ≤ 450

References

[1] Christopher Carl Heckman and Roi Krakovski, Erd˝os-Gy´arf´as Conjecture-
for Cubic Planar Graphs, Electron. J. Combin. 20(2) (2013) P7.

[2] H. W. Kroto, J. R. Heath, S. C. O’Brien, R. F. Curl and R. E. Smalley,
C60: Buckminsterfullerene, Nature 318 (1985) 162-163.

[3] Klas Markstr¨om, Extremal graphs for some problems on cycles in graphs,
Cong. Numer. 171 (2004) 2179-2192.

7
