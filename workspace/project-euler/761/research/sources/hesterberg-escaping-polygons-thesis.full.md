<!-- source: https://erikdemaine.org/theses/ahesterberg.pdf | converted from PDF -->

Closed Quasigeodesics, Escaping from
Polygons, and Conﬂict-Free Graph Coloring

by

Adam Classen Hesterberg

A.B., Princeton University (2011)

Submitted to the Department of Mathematics
in Partial Fulﬁllment of the Requirements for the Degree of

Doctor of Philosophy
at the
MASSACHUSETTS INSTITUTE OF TECHNOLOGY

June 2018

c⃝2018 Massachusetts Institute of Technology. All rights reserved.

Signature of Author:
 Department of Mathematics
May 11, 2018

Certiﬁed by:
 Erik Demaine
Professor of Computer Science and Engineering
Thesis Supervisor

Accepted by:
 Jonathan Kelner
Mark Hyman, Jr. Career Development Associate Professor of Applied Mathematics
Chairman, Department Committee on Graduate Theses

1

Closed Quasigeodesics, Escaping from Polygons, and Conﬂict-Free Graph Coloring

by

Adam Classen Hesterberg

Submitted to the Department of Mathematics
on May 11, 2018 in Partial Fulﬁllment of the
Requirements for the Degree of Doctor of Philosophy in
Mathematics

ABSTRACT

Closed quasigeodesics

A closed quasigeodesic on the surface of a polyhedron is a loop which can everywhere locally be
unfolded to a straight line: thus, it’s straight on faces, uniquely determined on edges, and has as
much ﬂexibility at a vertex as that vertex’s curvature. On any polyhedron, at least three closed
quasigeodesics are known to exist, by a nonconstructive topological proof. We present an algorithm
to ﬁnd one on any convex polyhedron in time O(n2ε−2Lℓ−1), where ε is the minimum curvature of
a vertex, L is the length of the longest side, and ℓ is the smallest distance within a face between a
vertex and an edge not containing it.

Escaping from polygons

You move continuously at speed 1 in the interior of a polygon P , trying to reach the boundary.
A zombie moves continuously at speed r outside P , trying to be at the boundary when you reach
it. For what r can you escape and for what r can the zombie catch you? We give exact results
for some P . For general P , we give a simple approximation to within a factor of roughly 9.2504.
We also give a pseudopolynomial-time approximation scheme. Finally, we prove NP-hardness and
hardness of approximation results for related problems with multiple zombies and/or humans.

Conﬂict-free graph coloring

A conﬂict-free k-coloring of a graph assigns one of k diﬀerent colors to some of the vertices such that,
for every vertex v, there is a color that is assigned to exactly one vertex among v and v’s neighbors.
We study the natural problem of the conﬂict-free chromatic number χCF (G) (the smallest k for
which conﬂict-free k-colorings exist), with a focus on planar graphs.

Thesis Supervisor: Erik Demaine
Title: Professor of Computer Science and Engineering

2

Thanks to my advisor, Erik Demaine.

For Canada/USA Mathcamp and my parents, Bev and Tim Hesterberg.

3

Contents

0 Overview 6

1 Closed Quasigeodesics 7
1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.2 Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.2.1 Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.2.2 Extending Quasigeodesic Rays . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.2.3 Full Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.3 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

2 Escaping from Polygons 15
2.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.2 Exact Answers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.2.1 Circle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.2.2 Wedge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.3 Approximation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.3.1 O(1)-approximation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.3.2 Pseudopolynomial-Time Approximation Scheme . . . . . . . . . . . . . . . . 21
2.4 Multiple Zombies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.4.1 Approximation Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.4.2 Slow Zombies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
2.5 Computational Complexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
2.6 Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

3 Conﬂict-Free Graph Coloring 34
3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.1.1 Our Contribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.1.2 Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.2 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.3 Closed Neighborhoods: Conﬂict-Free Coloring of General Graphs . . . . . . . . . . . 38
3.3.1 Complexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.3.2 A Suﬃcient Criterion for k-Colorability . . . . . . . . . . . . . . . . . . . . . 40
3.3.3 Conﬂict-Free Domination Number . . . . . . . . . . . . . . . . . . . . . . . . 41
3.4 Closed Neighborhoods: Planar Conﬂict-Free Coloring . . . . . . . . . . . . . . . . . . 42
3.4.1 Complexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.4.2 Suﬃcient Number of Colors . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.5 Closed Neighborhoods: Planar Conﬂict-Free Domination . . . . . . . . . . . . . . . . 45

4

3.5.1 At Most Two Colors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.5.2 Approximability for Three or More Colors . . . . . . . . . . . . . . . . . . . . 48
3.6 Open Neighborhoods: Planar Conﬂict-Free Coloring . . . . . . . . . . . . . . . . . . 50
3.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

5

Chapter 0

Overview

This thesis has three technical chapters.

Chapter 1 is about closed quasigeodesics on polyhedra, and is joint work with Erik Demaine and
Jason Ku, with help from discussions with Zachary Abel, Nadia Benbernou, Fae Charlton, Jayson
Lynch, Joseph O’Rourke, Diane Souvaine, and David Stalfa.

Chapter 2 is about a game of escaping from polygons, and is joint work with Zachary Abel, Erik
Demaine, Martin Demaine, Jason Ku, and Jayson Lynch, with help from discussions with Greg
Aloupis and Fae Charlton.

Chapter 3 is about “conﬂict-free” graph coloring and is joint work with Zachary Abel, Victor Al-
varez, Erik Demaine, S´andor Fekete, Aman Gour, Phillip Keldenich, and Christian Scheﬀer, with
help from discussions with Bruno Crepaldi, Pedro de Rezende, Cid de Souza, Stephan Friedrichs,
Michael Hemmer, and Frank Quedenfeld. It has appeared in the proceedings of the ACM-SIAM
Symposium on Discrete Algorithms [AAG+18].
 6

Chapter 1

Closed Quasigeodesics

This chapter is joint work with Erik Demaine and Jason Ku, with help from discussions with
Zachary Abel, Nadia Benbernou, Fae Charlton, Jayson Lynch, Joseph O’Rourke, Diane Souvaine,
and David Stalfa.

1.1 Introduction

A geodesic on a surface is a path which is, local to every point on it, a shortest path; a closed
geodesic on a surface is a loop with the same property. Poincar´e conjectured in 1905 [Poi05], and
Pogorelov [Pog73] and Ballmann [Bal78] independently proved, building on work of Lyusternik and
Schnirelmann [LS29], that every smooth surface of genus 0 has at least three non-self-intersecting
closed geodesics.
For non-smooth surfaces (say, polyhedra), an analog of a geodesic is a quasigeodesic, a path
which can locally be unfolded to a straight line. That is, on a face, a quasigeodesic is a straight
line; at an edge, it’s a straight line after the faces meeting at that edges are unfolded to be ﬂat at
that edge; and at a vertex of curvature κ (that is, one at which the sum of the angles is 2π − κ),
a quasigeodesic entering the vertex at a given angle can exit it anywhere in an angular interval of
length κ, as in Figure 1.1. Analogously, a closed quasigeodesic is a loop which is quasigeodesic,
and a (quasi)geodesic ray/segment is a one/two-ended path which is (quasi)geodesic. The same
proof of Ballmann’s [Bal78] also shows that there are at least three non-self-intersecting closed
quasigeodesics on every polyhedron, by approximating it with smooth surfaces.
The proof of existence of those closed quasigeodesics is nonconstructive, and [DO07, Open
Problem] asks, in 2007, for a polynomial (or any) algorithm to ﬁnd one. We provide, in Sec-
tion 1.2, an algorithm which ﬁnds at least one closed quasigeodesic on a convex polyhedron in time
O(n2ε−2Lℓ−1), where n is the number of vertices of the polyhedron, ε is the smallest curvature at
a vertex, L is the length of the longest side, and ℓ is the smallest distance within a face between
a vertex and an edge not containing it. This running time is pseudopolynomial, since L, ℓ−1, and
ε−1 may be exponential in the length of a binary description of the polyhedron, so this does not
resolve the question of a polynomial-time algorithm. Also, a closed quasigeodesic found by our
algorithm may be self-intersecting, even though a non-self-intersecting one is guaranteed to exist.
In Section 1.3 we discuss some of the diﬃculties involved in resolving either of these issues.

7

κ
 κ

κ
 κ

Figure 1.1: At a vertex of curvature κ, there’s an angular interval of size κ in which a segment of a
quasigeodesic can be extended: the segment of geodesic starting on the left can continue straight in
either of the pictured unfoldings or any of the intermediate unfoldings in which the right pentagon
touches only at a vertex.

1.2 Algorithm

In this section, we give an algorithm to ﬁnd a closed quasigeodesic on the surface of a convex
polyhedron P .

1.2.1 Outline

The idea of the algorithm is roughly as follows: ﬁrst, we deﬁne a directed graph for which each
node1 is a pair (V, [ϕ1, ϕ2]) of a vertex V of P and a small interval of directions at it, with an edge
from one such pair to another if a geodesic starting at the former vertex and somewhere in the
former range of directions can reach the latter vertex and continue everywhere in the latter range
of directions. We show how to calculate at least one out-edge from every node of that graph, so we
can start anywhere and follow edges until hitting a node twice, giving a closed quasigeodesic.
The key part of this algorithm is to calculate, given a vertex U and a range of directions,
another vertex V that can be reached starting from that vertex and in that range of directions,
even though reaching V may require crossing superpolynomially many faces. First we prove some
lemmas toward that goal.

Deﬁnition 1.2.1. If X is a point on the surface of a polyhedron, ϕ is a direction at X, and
d > 0, then R(X, ϕ, d) is the geodesic segment starting at X in the direction ϕ and continuing for a
distance d or until it hits a vertex, whichever comes ﬁrst. We allow d = ∞; in that case, R(X, ϕ, d)
is a geodesic ray.

1We call vertices of the graph “nodes” to distinguish them from vertices of the polyhedron.

8

Figure 1.2: A segment of a geodesic is a straight line in the unfolding of the sequence of faces
through which it passes, as in this unfolding of a regular dodecahedron.

Deﬁnition 1.2.2. If R(X, ϕ, d) is a geodesic segment or ray, the face sequence F (R(X, ϕ, d)) is
the (possibly inﬁnite) sequence of faces that R(X, ϕ, d) visits.

Lemma 1.2.1. If R1 = R(X, ϕ1, ∞) and R2 = R(X, ϕ2, ∞) are two geodesic rays from a common
starting point X with an angle between them of θ ∈ (0, π), the face sequences F (R1) and F (R2) are
distinct, and the ﬁrst diﬀerence between them occurs at most one face after a geodesic distance of
O(θ−1L).

Proof. Given a (preﬁx of) F (Ri), the segment of Ri on it is a straight line, so while F (R1) = F (R2),
the two geodesics R1 and R2 form a wedge in a common unfolding, as in Figure 1.2. The distance
between the points on the rays at distance d from X is 2d sin θ
2 > dθ/π (since θ
2 < π
2 ), so at a
distance of O(θ−1L), that distance is at least L. So either F (R1) and F (R2) diﬀer before then, or
the next edge that R1 and R2 cross can’t be the same edge, in which case F (R1) and F (R2) diﬀer
in the next face, as claimed.

If we had deﬁned L analogously to ℓ as not just the length of the longest side but the greatest
distance within a face between a vertex and an edge not containing it, we could remove the “at
most one face after” condition from Lemma 1.2.1.

1.2.2 Extending Quasigeodesic Rays

Although Lemma 1.2.1 gives a bound on the geodesic distance to the ﬁrst diﬀerence in the face
sequences (or one face before it), it’s not a bound on the number of faces traversed before that
diﬀerence, which might be large if the two paths come very close to a vertex of high curvature, as
in Figure 1.3, or repeat the same sequence of edges many times, as in Figure 1.4.

9

Figure 1.3: Even a short geodesic path between two vertices u and v may cross many edges.

Figure 1.4: If a geodesic path encounters the same edge twice in nearly the same place and nearly
the same direction, as is the case for the thick quasigeodesic path through the center of this ﬁgure
if every fourth triangle is the same face, it may pass the same sequence of faces in the same order
a superpolynomial number of times.

Nonetheless, in both of these cases, we can describe a geodesic ray’s path eﬃciently:

Lemma 1.2.2. Let R = (X, ϕ, d) be a geodesic segment with d < ℓ. In O(n) time, we can calculate
F (R), expressed as a sequence S1 of O(n) faces, followed by another sequence S2 of O(n) faces and
a distance over which R visits the faces of S2 periodically2. Also, we can calculate the face, location
in the face, and direction of R at its endpoint other than X.

Proof. If R enters a face f on an edge e1 and exits at a point P2 on an edge e2, then we claim that
every time R enters f by e1, it must exit f by e2. It can’t exit by the same edge e1 by which it

2The length of the sequence of faces may be too large to even write down the number of repetitions.

10

Figure 1.5: If a geodesic visits three edges of the same face, the total distance traveled is at least ℓ.

entered, so suppose for contradiction that in some visit to f , it enters at a point P1 on the edge
e1 and exits at a point P3 on another edge e3, as shown in Figure 1.5. If any two of e1, e2, and
e3 are nonincident, then R has gone from a point on one edge to a point on a nonincident edge.
By the deﬁnition of ℓ, that’s a distance of at least ℓ. Otherwise, e1, e2, and e3 are the three edges
of a triangular face, and the total geodesic distance is at least d(P1, P2) + d(P1, P3). Consider the
reﬂection e4 of e3 across e2 and the reﬂected point P4 on e4. The path from P4 to P2 via P1 is
at least the distance from P2 to P4, which is at least the shortest distance from a point on e4 to
a point on e2, which is attained at an endpoint of at least one of e2 and e4, say an endpoint of
e4. The path making that shortest distance (shown in gray) goes through e1, so it’s at least the
distance from e1 to the opposite vertex, which is at least ℓ, farther than the conditions under which
this lemma applies. Hence each edge crossed determines the next edge crossed, so F (R) is periodic
after crossing each edge at most once. Also, there are only O(n) edges, so after crossing at most
O(n) edges, F (R) repeats periodically with period O(n).
In total time O(n), we can calculate the path of R before it repeats periodically for each face f
it enters, as follows:

1. For each edge e of f , we can calculate in how much distance R would cross e, in O(1) time.

2. The edge on which R exits f is the one minimizing that distance. We can, in O(1) time,
calculate where on that edge and at what angle R crosses it.

There are O(n) pairs of a face and an edge of that face, so the total amount of computation before
the face sequence repeats periodically is O(n). (If R ends at a vertex before then, we calculate so
because R exits a face by two edges at the same time.)
Consider the shape formed by the faces of F (R) that repeat periodically, as in the bolded part
of Figure 1.6. Copies of this shape attach to each other on copies of a repeated edge e; that is, the
entire shape is translated and possibly rotated to identify the copies of e. If there’s no rotation,
as in Figure 1.6, all copies of each edge e are translates of each other by a constant amount, and

11

Figure 1.6: When a quasigeodesic path passes through the same sequence of faces several times,
the unfolding of the faces it passes through repeats regularly.

we can calculate in O(1) time where in the translated ﬁgure the other endpoint of R is and in
O(n) time which face that corresponds to and where. If there is rotation, all copies of each edge
e are rotations around a consistent center point C (in the plane of the unfolding). Again, we can
determine the path in time O(n) by calculating the last time it hits a rotation of each edge e; for
each such calculation, we only need to check where the line intersects the circle along which each
endpoint of e rotates.

Corollary 1.2.3. In O(ndℓ−1) time, we can calculate R(X, ϕ, d).

Proof. Apply Lemma 1.2.2 to R = R(X, ϕ, ℓ
2 ), which gives us the point X ′ and direction ϕ′ of the
endpoint of R other than X. Apply Lemma 1.2.2 to R(X ′, ϕ′, ℓ
2 ), and repeat 2dℓ−1 times.

1.2.3 Full Algorithm

We are now ready to state the algorithm for ﬁnding a closed quasigeodesic in O(n2ε−2Lℓ−1) time:

Theorem 1.2.4. Let P be a convex polyhedron with n vertices all of curvature at least ε, let L be
the length of the longest side, and let ℓ be the least distance between points on edges sharing a face
but not a vertex. Then in O(n2ε−2Lℓ−1) time, we can ﬁnd a closed quasigeodesic on P . We can
express such a closed quasigeodesic as a sequence of O(n3ε−2Lℓ−1) subsequences of faces, where for
each subsequence we give a distance for which the closed quasigeodesic visits that subsequence of
faces periodically.

Proof. For each vertex V of P , divide the total angle at that vertex (that is, the angles at that
vertex in the faces that meet at that vertex) into arcs of size between ε/4 and ε/2 < π, making
O(ε−1) such arcs at each vertex.
Construct a directed graph G whose nodes are pairs of a vertex of V and one of those arcs,
giving the graph O(nε−1) nodes, with an edge from a node3 u to a node v if there exists a direction
at u that hits v’s vertex and can continue from every angle in v’s arc.

3We use capital letters and the word “vertex” for vertices of a polyhedron and lower-case letters and the word
“node” for vertices of a graph.
 12

Let v be a node of G, with corresponding vertex V and angles from ϕ1 to ϕ2. By Corollary 1.2.3
we can, in O(nε−1Lℓ−1) time, follow each of the rays R1 = R(V, ϕ1) and R2 = R(V, ϕ2) for a
distance of ε−1L and compare their face sequences F (R1) and F (R2). By Lemma 1.2.1, either
F (R1) and F (R2) diﬀer or we can reach a diﬀerence by extending each of R1 and R2 to the end
of its current face (which we can calculate in O(n) more time). The ﬁrst diﬀerence in the face
sequences F (R1) and F (R2) determines a vertex reachable in the wedge between R1 and R2. That
is, given a vertex V and a range of angles at it from ϕ1 to ϕ2, we can, in O(nℓ−1Lε−1) time,
determine a vertex reachable from V via an angle between ϕ1 and ϕ2. Once we reach such a vertex,
a quasigeodesic can exit the vertex anywhere in an angle equal to that vertex’s curvature, which is
at least ε, so for at least one of the arcs of size at most ε/2 at that vertex, the quasigeodesic can
exit anywhere in that arc.
Hence in time O(nℓ−1Lε−1) we can ﬁnd and follow an out-edge from any node of G. After at
most as many such transitions as the number of nodes of G, O(nε−1), we ﬁnd a cycle, which is
exactly a closed quasigeodesic.
Also, that quasigeodesic is composed of O(nε−1) edges of the graph. Each of those edges is a
geodesic distance of O(Lε−1) plus at most one face. Over the distance of O(Lε−1), each segment of
length ℓ
2 is described by Lemma 1.2.2 as a subsequence of O(n) faces, possibly visited periodically
over some geodesic distance. So, each of the edges is described as a sequence of O(nε−2Lℓ−1) faces,
with subsequences possibly visited periodically, and the whole geodesic is described as a sequence
of O(n2ε−3Lℓ−1) faces, with subsequences possibly visited periodically over speciﬁed distances, as
desired.

If D is the greatest diameter of a face, then a closed quasigeodesic found by Theorem 1.2.4
has length O(nε−1(ε−1L + D)), because the quasigeodesic visits O(nε−1) graph nodes, and, by
Lemma 1.2.1, goes a distance at most ε−1L + D between each consecutive pair.

1.3 Conclusion

It has been known for four decades (as in [Bal78]) that every convex polyhedron has a closed
quasigeodesic; we give the ﬁrst algorithm to ﬁnd one. This algorithm is polynomial in not just
the number of vertices of the input polyhedron, but instead also depends on some features of that
polyhedron, leaving some questions open.

Question 1. Theorem 1.2.4 does not necessarily ﬁnd a non-self-intersecting closed quasigeodesic,
even though at least three are guaranteed to exist. Is there an algorithm to ﬁnd one? In particular,
can we ﬁnd the shortest closed quasigeodesic?

Any approach similar to Theorem 1.2.4 is unlikely to resolve this, for several reasons:

1. Parts of a quasigeodesic could enter a vertex at inﬁnitely many angles. Theorem 1.2.4 makes
this manageable by grouping similar angles of entry to a vertex, but if similar angles of entry to
a vertex are combined, extensions that would be valid for some of them but invalid for others
are treated as invalid for all of them. For instance, a quasigeodesic found by Theorem 1.2.4
will almost never turn by the maximum allowed at any vertex, since exiting a vertex at the
maximum possible turn from one entry angle to the vertex may mean exiting it with more of a
turn than allowed for another very close entry angle. So there are some closed quasigeodesics
that Theorem 1.2.4 can’t ﬁnd, and those may include non-self-intersecting ones.

2. Given a vertex and a wedge determined by a range of directions from it, we can ﬁnd one vertex
in the wedge, but if we wish to ﬁnd more than one, the problem becomes more complicated.

13

When we seek only one vertex, there’s only one unfolding of the faces to consider, which
the entire wedge stays in until it hits a vertex; when we pass a vertex, the unfoldings on
each side of it might be diﬀerent, so we multiply the size of the problem by 2 every time we
pass a vertex. There may, in fact, be exponentially many non-self-intersecting geodesic paths
between two vertices: for instance, O’Rourke [O’R18] gives the example of a doubly-covered
regular polygon, in which a geodesic path may visit every vertex in order around the cycle
but may skip vertices.

Question 2. Theorem 1.2.4 assumes that arithmetic operations with real numbers can be done
in O(1) time, even when the input is given with ﬁnitely many bits (say, integer coordinates for
the vertices). It may, however, be the case that every vertex unfolds to a point with algebraic
coordinates; if so, is there an analog of Theorem 1.2.4 using only arithmetic operations on rational
numbers?

Question 3. Theorem 1.2.4 is polynomial in not just n but the smallest curvature at a vertex, the
length of the longest side, and the shortest distance within a face between a vertex and an edge not
containing it. Are all of those necessary? Can the last be simpliﬁed to the length of the shortest
side?

Question 4. Can the algorithm of Theorem 1.2.4 be extended to nonconvex polyhedra P ?

Question 5. Is there an algorithm to ﬁnd a closed quasigeodesic passing through a number of faces
bounded by a polynomial function of n, ε, L, ℓ, and perhaps the minimum total angle of a polyhedron
vertex? Does Theorem 1.2.4 already have such a bound?

A single quasigeodesic ray may pass through a number of faces not bounded by a function of
those parameters before ceasing to cycle periodically: for instance, the geodesic ray of Figure 1.4
does. However, we have no example for which a whole geodesic wedge passes through a number of
faces not bounded by a function of those parameters before containing a vertex.

14

Chapter 2

Escaping from Polygons

This chapter is joint work with Zachary Abel, Erik Demaine, Martin Demaine, Jason Ku, and
Jayson Lynch, with help from discussions with Greg Aloupis and Fae Charlton.

2.1 Introduction

In 1961, Richard Guy [Guy61] posed the following classic puzzle, reproduced in [O’B61]:

Some robbers have stolen the green eye of a little yellow god from a temple on a
small island in the middle of a circular lake. As they embark in their boat, they are
observed by a solitary guard on the shore, who can run four times as fast as they can
row the boat. Can they be sure of reaching the shore and escaping with their loot?
If so, how? And what if the guard could move four and a half times as fast as the
robbers?

The same problem was rethemed by Martin Gardner [Gar65] to be about a maiden on a rowboat.
In this chapter, we retheme again and ask about shapes other than a circle:

Problem 1. A human chooses a position in a human play area, a subset of a metric space. Then a
number nz of zombies, who can each run r times as fast1 as the human, choose positions in a zombie
play area, another subset of the same metric space. The humans and zombies move simultaneously
and continuously, staying in their own play areas, with every player having full knowledge of every
other player’s movement plans. The human wins if they can reach a point of the zombie play area
with no zombie at the same point; if the zombies can prevent that for arbitrarily long, then the
zombies win. Given such a setup, what is the critical speed ratio r∗ ≥ 0 such that the human wins if
the zombies are less than r∗ times faster and the zombies win if they’re more than r∗ times faster?

We give names to some common types of human play area and zombie play area:

1. In the “moat model”2, the human play area is the interior and boundary of a (possibly
unbounded) polygon P , and the zombie play area is the boundary of P .

2. In the “standard model”, the human play area is a (possibly unbounded) polygon P with its
boundary, and the zombie play area is the exterior and boundary of P .

1For simplicity, we make the human’s speed always 1, and use “speed ratio” and “zombie’s speed” interchangeably
for r.
2So named as if the zombie is trapped in a moat.
 15

3. In the “Jordan model” (which can be applied with either the moat model or the standard
model), the human play area is a Jordan region in the plane instead of a polygon. For
instance, Guy’s problem is in the Jordan model where the region is a disk.

4. In the “graph model”, the human play area is the edges and vertices of a graph, and the zombie
play area is the edges and vertices of another graph (possibly overlapping the human’s).

In this chapter, we investigate the following cases of this problem. Unless speciﬁed otherwise,
all results in the chapter are for the standard model and the moat model, with nz = 1 zombie.

1. In Section 2.2, we calculate the critical speed ratio in two cases simple enough to calculate
it exactly: Guy’s problem (from [O’B61]) and an inﬁnite wedge (in any of the models), both
with nz = 1.

2. In Section 2.3, we give bounds on the critical speed ratio r∗ that diﬀer by a factor of approx-
imately 9.2504, in the moat model and standard model with nz = 1.

3. Also in Section 2.3, we give a pseudopolynomial-time approximation scheme for the critical
speed ratio r∗, in the moat model and the standard model with nz = 1.

4. In Section 2.4, we consider nz > 1, and give miscellaneous results in all the models.

5. In Section 2.5, we prove NP-hardness and hardness of approximation results in the graph
model with arbitrary nz.

2.2 Exact Answers

First we investigate two shapes for which the critical speed ratio can be calculated exactly: a circle
and an unbounded intersection of halfplanes.

2.2.1 Circle

Theorem 2.2.1. Let ϕ ≈ 0.43π be the angle such that tan ϕ = π + ϕ. Then the critical speed ratio
r∗ for a circle is sec ϕ ≈ 4.60.

This result comes from [O’B61], as does the proof that r∗ ≥ sec ϕ; we reproduce that proof,
ﬂesh out some details, and also prove that r∗ ≤ sec ϕ:

Proof. First we reproduce the proof from [O’B61] that r∗ ≥ sec ϕ. That is, we’ll prove that, if
r < sec ϕ, then the human can escape. While the human is within distance d ≤ cos ϕ of the center
of the circle, its maximum angular speed around the center is greater than the zombie’s, so the
human can reach a point opposite the zombie at a distance of cos ϕ from the center.
Let the human be at a position H at distance d ≥ cos ϕ from the center of the circle, opposite
the zombie’s position Z, as in Figure 2.1. We claim that the human can either reach such a position
with greater d or escape. First, let the human move straight away from the center of the circle
until the zombie is no longer on the same diameter; without loss of generality, let the zombie move
counterclockwise. Then let the human pick a point T on the boundary of the circle such that
HT ⊥ ZT and the zombie is moving on the major arc from Z to T , and run straight toward T
until they either reach T or the zombie is again diametrically opposite them. Note that the angle
at the center of the circle between T and H is arccos d; if the human is at a distance of exactly
cos ϕ from the center of the circle, then the angle at the center of the circle between T and H is

16

Figure 2.1: Human and zombie strategies at one position in the game on a circle.

ϕ, and otherwise arccos d < ϕ. If the zombie ever crosses a point antipodal to the human again,
then the human has reached the same position with greater d; otherwise, the zombie must travel a
distance of at least π + arccos d to reach T , which takes time at least

π + arccos d
r > (π + arccos d) cos ϕ,

and the human can get there in time sin arccos d, and it suﬃces to show that

(π + arccos d) cos ϕ − sin arccos d ≥ 0.

But if x ≤ ϕ, then d ((π + x) cos ϕ)
dx = cos ϕ ≤ cos x = d sin x
dx ,

so for d ≥ cos ϕ, that is, for arccos d ≤ ϕ, that expression is minimized at d = cos ϕ, and there it’s
(π + ϕ) cos ϕ − sin ϕ = 0, as desired. So, the human reaches T ﬁrst and escapes.
Conversely, if the zombie’s speed r is more than sec ϕ greater than the human’s, we claim that
the human cannot escape. The zombie’s strategy is simple:

1. While the human is within 1
r of the center of the circle, stand still. Imagine eating the human’s
brain, to work up an appetite.

2. While the human is more than 1
r from the center of the circle, move mindlessly along the
shorter arc toward the closest point on the boundary of the circle to the human (breaking
ties arbitrarily).
 17

Suppose for contradiction that the human can escape. If the human starts within 1
r of the center
of the circle, let H (without loss of generality, on the positive x axis) be the last point at distance
at most 1
r of the center of the circle that the human passed through; otherwise, let the human start
on the positive x axis, let H = ( 1
r , 0), and let the zombie start at (1, 0). Let T = (cos ϕ, sin ϕ) be
the point at which the human eventually escapes. The human can’t get to T faster than by the

straight line from H to T , at a distance of √
(cos ϕ − 1
r )2 + sin2 ϕ. If the human is outside the circle

of radius 1
r , then the zombie’s angular velocity around the center of the circle is greater than the
human’s, so the arclength between the zombie and the closest point of the human to the boundary
of the circle only decreases; that is, the zombie can choose to run in a consistent direction. So the
zombie reaches T in time at most π+ϕ
r (less if the human started outside the circle of radius 1
r ).
But by calculations similar to the above, the zombie gets there ﬁrst:
√

sin
2 ϕ + (cos ϕ − 1
r )2

=
√
1 − 2r−1 cos ϕ + r−2

=
√
1 − 2 cos ϕ cos ϕ + cos2 ϕ + (r−1 − cos ϕ)(r−1 + cos ϕ − 2 cos ϕ)

≥
√
1 − cos2 ϕ

= sin ϕ

= tan ϕ cos ϕ

=(π + ϕ) cos ϕ

≥(π + ϕ)/r,

so the zombie catches the human, ﬁnishing the proof and the human’s brain.

2.2.2 Wedge

If the human play area is a wedge (an unbounded intersection of halfplanes, whose boundary is
simply connected), we can calculate the critical speed ratio exactly:

Theorem 2.2.2. If P is an unbounded intersection of halfplanes and the angle between the two
extreme halfplanes is 2θ ∈ (0, π], then the critical speed ratio r∗ is csc θ.

Proof. If P is just a halfplane, a zombie of speed 1 = csc π
2 can win by staying at the projection of
the human onto the boundary, since that projection moves at most as fast as the human. A zombie
of speed less than 1 loses to a human who moves along the boundary. Otherwise, the two extreme
halfplanes are distinct.
Orient the wedge so that the boundaries of the two extreme halfplanes are at angles of ±θ from
the positive x axis, and their intersection (which may not be in the wedge, if the wedge is bounded
by more than two halfplanes) is the origin, as in Figure 2.2.
If the zombie’s speed r is at least csc θ times the human’s, then the zombie can stay at the same
y coordinate as the human while staying on the boundary: the human’s speed in the y coordinate
is at most 1, and the zombie’s speed in the y coordinate while staying on part of the boundary
with slope ϕ ∈ [−θ, θ] is r
csc ϕ ≥ csc θ
csc θ = 1. A point on the boundary is uniquely determined by its
y coordinate, so if the human reaches a point on the boundary, then the zombie is there too to
catch it.
If the zombie’s speed r is less than csc θ times the human’s, then the human can go to a point
( 1
ε , 0) (that is, on the angular bisector of the two halfplanes at a very large distance from each

18

 Figure 2.2: Zombie strategy if the play area is a wedge.

of them), for some ε to be chosen later. Without loss of generality, the zombie has a nonpositive
y coordinate; then the human moves straight up toward the point T = ( 1
ε , tan θ
ε ), reaching it in time
tan θ
ε . If the intersection of the boundary with the positive x axis is at (x0, 0), the zombie’s path to
the human’s escape point T must take it through the x axis at a point no closer to T than (x0, 0),

from which the distance to the human’s escape point is √
( 1
ε − x0)2 + ( tan θ
ε ))2. For suﬃciently

small ε, that’s close to sec θ
ε , so the zombie needs time close to sec θ
rε to reach T . For r < csc θ, the
human gets there ﬁrst and escapes, as claimed.

2.3 Approximation

In the previous section, we found the exact critical speed ratio for speciﬁc human play areas P by
methods that don’t generalize to arbitrary polygons or Jordan regions. We don’t have an algorithm
to compute the exact critical speed ratio for arbitrary P , but we can approximate it, as the following
two results show. All theorems in this section are valid for the standard model and moat model,
and have nz = 1 zombies.

2.3.1 O(1)-approximation

Theorem 2.3.1. Let P be any polygon. Then the critical speed ratio r∗ is at least maxp,q∈δP dz(p,q)
dh(p,q)
(where dz and dh are the geodesic distances in the zombie and human play areas, respectively).

Proof. Let p and q be points maximizing the expression above. The human can ﬁrst go to p; if
the zombie doesn’t go to p as well, the human escapes at p. If the zombie does come to p, the
human can run toward q. The human’s distance to p is dh(p, q) and the zombie’s is dz(p, q), so if
the zombie’s speed is less than dz(p,q)
dh(p,q) , then the human can reach q ﬁrst and escape.

Theorem 2.3.2. Let P be any polygon. Then the critical speed ratio r∗ is at most 9.2504 maxp,q∈δP dz(p,q)
dh(p,q)
(where dz and dh are the geodesic distances in the zombie and human play areas, respectively).

Proof. Divide the polygon into regions by its medial axis; that is, each region is associated with an
edge of the polygon and is the set of points inside the polygon closest to that edge of the polygon,
as shown in Figure 2.3. Also, for each region, deﬁne the fringe of that region to be the union, over
points p inside the region, of the circle centered at p with radius x · d(p, δP ), where d(p, δP ) is the
distance from p to the nearest point on the boundary of P and x ≈ 0.465 is a fringe size parameter.
Let the zombie’s strategy be as follows:

1. At all times, the zombie has a target edge e such that it attempts to be at the closest point
on e to the human. Initially, this edge is the one closest to the human.

19

Figure 2.3: A polygon and its medial axis.

2. When the human exits the fringe of the medial axis region corresponding to e, the zombie
runs to the closest point on the boundary to the human. If that point is on edge f , the zombie
switches its target edge to f .

This strategy works as long as, when the human leaves the fringe of the medial axis region for
the zombie’s target edge e, the zombie can run into position for the medial axis region R for its
new target edge f before the human leaves the fringe of R (triggering another strategy change) or
reaches the boundary and escapes.
First, we deﬁne some points, as in Figure 2.4. Let h be the point at which the human leaves
the fringe (drawn in blue) of a region R (drawn in red) with corresponding edge e. Then h is in
the fringe of R because it’s in a circle centered at a point o in R; if p is the closest point to o on
e, then d(o, h) = x · d(o, p). Also, let z be the closest point on R’s edge to h, which is where the
zombie stands when the human exits the fringe at h, let q be the closest point to o on δP , and let
f be q’s edge. Also, let θ be the angle between (the extensions of) e and f , so π − θ is the angle at
o between oq and op.
When the human leaves at h, their distance to the boundary is d(h, q) = d(o, q) − d(o, h) =
d(o, q)(1 − x) = d(o, p)(1 − x). So, to leave the fringe of their new region, the human must go a
distance of at least d(o, p)x(1 − x). Before they do, the zombie must be in position for the new
strategy, which requires moving at most:

1. d(z, p) to return to p. Since z is the closest point on its edge to h, it’s at least as close to p as
the projection of h onto e (possibly closer, if e doesn’t extend that far). The length of that
projection is d(o, h) sin θ = d(o, p)x sin θ, so that’s an upper bound on the zombie’s distance
to return to p.

2. dz(p, q) to reach q.

3. d(o, p)x(1 − x) to match the human’s move (projected onto f ).

20

Figure 2.4: A section of a polygon with a region deﬁned by the medial axis and its fringe region.

So, if the zombie’s speed is enough to travel those three distances in the time the human travels
a distance of d(o, p)x(1 − x), the zombie can be in position in time for the human’s next region
change. That is, the critical speed ratio r∗ is at most

d(o, p)x sin θ + dz(p, q) + d(o, p)x(1 − x)
d(o, p)x(1 − x) = 1 + sin θ
1 − x + dz(p, q)
d(o, p)x(1 − x) .

Also, since a closest point to o on δP is p, the circle centered at o with radius d(o, p) is contained
in P , so dz(p, q) ≥ (π − θ)d(o, p), the distance from p to q along the circle centered at o. Also,
that circle (and hence P ) contains the line segment from p to q, so dh(p, q) ≤ 2d(o, p) cos θ
2 . So
dz(p,q)
dh(p,q) ≥ π−θ
2 cos θ
2 , so the critical speed ratio is at most

max
p,q∈δP dz(p, q)
dh(p, q) max
θ
 ((1 + sin θ
1 − x
 ) ( 2 cos θ
2
π − θ
 )
 + 2 cos θ
2
x(1 − x)
 )
 .

Having chosen the fringe size parameter x ≈ 0.465, that expression is maximized at roughly θ =
0.24π with the value 9.2504 maxp,q∈δP dz(p,q)
dh(p,q) , so the zombie can win if it’s faster than that, as
claimed.

2.3.2 Pseudopolynomial-Time Approximation Scheme

Although Theorem 2.3.2 describes the critical speed ratio in terms of the polygon, it’s not an
algorithm (since ﬁnding the pair (p, q) of points maximizing dz(p,q)
dh(p,q) may take some work) nor can
it approximate arbitrarily closely. To remedy those ﬂaws, we also give a pseudopolynomial-time
approximation scheme for the critical speed ratio r∗ for any polygon P ; that is, given P and ε > 0,
we describe a scheme for approximating r∗ to within a factor of 1 + ε in time polynomial in ε−1

and the coordinates of P . (Since the side lengths of P can be exponential in the length of their
encoding, the approximation scheme is only pseudopolynomial.)
First, we deﬁne a discrete analogue of the game.

Deﬁnition 2.3.1. Let P be a closed subset of the plane whose boundary is a union of line segments,
and let ε > 0. The ε-discretization of P is the graph whose vertices are the following points p in
the plane:
 21

1. If p is on an edge of P , the distance to one endpoint of that edge is a multiple of ε2.

2. If p is in the interior of P , x and y are both multiples of ε2.

There is an edge between two vertices if and only if the distance between the corresponding points
is at most ε.

Deﬁnition 2.3.2. Let P be a closed subset of the plane whose boundary is a union of line segments,
let ε > 0, and let z and h be positive integers. The (P, ε, z, h) discrete game is as follows:

1. First, the human chooses a vertex, their start location, of the ε-discretization of P .

2. Second, if hull(P ) and int(P ) are the convex hull and interior of P , respectively, the zombie
chooses a vertex, their start location, of a graph: the ε-discretization of hull(P ) \ int(P ) if
the game is in the standard model, or the ε-discretization of δP if the game is in the moat
model.

3. The human and zombie alternate turns, starting with the human.

4. In the human’s turn, the human moves to a vertex at distance at most h in the graph from
their current vertex.

5. In the zombie’s turn, the zombie moves to a vertex at distance at most z in the graph from
their current vertex.

6. If, at the end of the zombie’s turn, the human is at a vertex on the edge of P , and the zombie
is not at the same vertex, the human wins.

There is no loss condition for the human, but we say the human loses if they can never win.

Theorem 2.3.3. For every polygon P there exists an ε0 > 0, such that ε−1
0 is polynomial in the
coordinates of P and if r∗ is the critical speed ratio for P , then for all ε ∈ (0, ε0) and for all integers
z, h ∈ (0, ε−1), the human wins the (P, ε5, z, h) game if z/h ∈ [1, r∗ 1
(1+ε)3 ) and the zombie wins if
z/h > r∗(1 + ε)3.

In particular, we will prove Theorem 2.3.3 for any ε0 such that:

1. There’s a point in P at distance more than ε0 from the nearest boundary. We can calculate
a lower bound on this by triangulating P , choosing any of that triangulation’s triangles, and
using the inradius of that triangle. The inradius is the area divided by half the perimeter,
and both of those are polynomial functions of the input coordinates, so this bound on ε0 is
polynomial in the coordinates of P .

2. No disk of radius 2
√ε0 contains two edges not sharing a vertex. We can calculate a lower
bound on this: the minimum distance between two edges not sharing a vertex is attained
either by a pair of vertices (and we can calculate the minimum distance between pairs of
vertices) or by the perpendicular from a vertex v to an edge (u, w). The length of that
perpendicular is the area of the triangle with vertices u, v, and w divided by the distance
from u to w, and those are both polynomial in u, v, and w, so this bound on ε0 has length
(in bits) polynomial in the length (in bits) of P .

22

3. ε0 < 1/(2r(P )2) if r(P ) is the critical speed ratio for P . We can calculate a bound on
this depending only on P by Theorem 2.3.2 as follows: the critical speed ratio is between
maxp,q∈δP dz(p,q)
dh(p,q) and 9.2504 maxp,q∈δP dz(p,q)
dh(p,q) . If p and q are on the same edge, then maxp,q∈δP dz(p,q)
dh(p,q)
is the cosecant of half the angle between them, as in Theorem 2.2.2; if not, then dh(p, q) is
at least the minimum distance between two points on edges not sharing a vertex, which is
polynomial as above, and dz(p, q) is at most the perimeter of P , which is polynomial, giving
an upper bound on maxp,q∈δP dz(p,q)
dh(p,q) .

Before we prove Theorem 2.3.3, we note that this implies the existence of a pseudopolynomial-
time approximation scheme. First, note that we can solve a (P, ε, z, h) discrete game in time
polynomial in ε−1:

1. Each graph has polynomial size: the area of the convex hull of P and the length of the
perimeter of P are both polynomial, so the sizes of the graphs are polynomial, so the game
can only be in polynomially many states, described by a human vertex, a zombie vertex, and
whose turn it is.

2. We can calculate all legal transitions between pairs of game states in polynomial time.

3. We can calculate all winning positions in the discrete game: First mark as human wins all
game states for which the human is at a vertex corresponding to a point on δP , the zombie
is not there, and it’s the human’s turn to move. Then, for at most as many rounds as the
(polynomial) number of possible game states, mark each game state as a human win if either

(a) it’s the human’s turn and they can move to any game state already marked as a human
win, or

(b) it’s the zombie’s turn and every game state they can move to is already marked as a
human win.

After at most as many rounds as the number of game states, every game state from which
the human wins will be so marked since, at each round, either at least one game state not
previously marked as a human win will be or no new game states will be marked and every
following round will be the same. In each round, we do polynomially much work, making this
scheme polynomial.

4. The human wins the discrete game if and only if there’s a human starting position (x, y) such
that for every zombie starting position (x′, y′), the state with the human at (x, y), the zombie
at (x′, y′), and the zombie to move is a human win.

Second, given an ε, we can approximate the critical speed ratio to within (1 + ε)6 by binary
search:

1. The critical speed ratio is between 1 and 1
2
√ε0 (as determined above in the deﬁnition of ε0).

That is, if h0 = ⌊ε−5⌋, so there is some integer z0 ∈ [h, h
2
√ε0 ] such that the human wins the
(P, ε5, z0, h0) discrete game and the zombie wins the (P, ε5, z0 + 1, h0) discrete game. Binary
search for z0, which takes at most log2( 1
2ε5√ε0 ) = O(ε−1) games, each of which takes time

polynomial in ε−1.

2. The interval in which the theorem says nothing about the winner of the (P, ε5, z, h) game is
a factor of (1 + ε)6, so the previous step tells us the critical speed ratio r∗ to within a factor
of (1 + ε)6.
 23

The key part of proving Theorem 2.3.3 is to prove the seemingly innocuous claim that if the
human can win the continuous game at all, and then the zombie becomes slightly slower, the human
can win with a bit of time to spare; this is Lemma 2.3.7. To prove this, though, we ﬁrst need some
other lemmas:

Lemma 2.3.4. If the human wins the continuous game, then there exists ε > 0 (not necessarily
bounded by a function of ε0) such that the zombie is at distance at least ε when the human wins.

Proof. When the human wins, the zombie is not at the human’s location, so the zombie’s distance
to the human is some positive number.

Lemma 2.3.5. If the human wins the continuous game at a speed ratio r, then there exists ε > 0
(not necessarily bounded by a function of ε0) such that the human can commit to moving in a
straight line for the last ε of their movement, and still win.

Proof. Suppose that when the human wins at a point p ∈ δP the zombie is at distance ε. At
time less than ε 1
2r+3 before the human wins, the human is at distance less than ε 1
2r+3 from p, and
the zombie is at distance more than ε r+2
2r+3 from the human (because in time less than ε 1
2r+3 , the
distance between the zombie and human decreases by less than ε r+1
2r+3 and reaches at least ε 2r+3
2r+3 ).
Therefore, if the human runs straight toward p at that point, they either

1. get to it ﬁrst and win, or

2. hit another point on the boundary, and also win because in time less than ε 1
2r+3 , the distance
between the human and zombie decrease by less than ε r+1
2r+3 from its starting value of ε r+2
2r+3 .

Either way, the human ran straight for some positive distance.

Lemma 2.3.6. If the zombie has a winning strategy that leaves the convex hull of P , then it has a
winning strategy that doesn’t.

Proof. Let Zarathustra be the zombie with a winning strategy that leaves the convex hull of P .
Another zombie, Zane, can win without leaving the convex hull by simulating Zarathustra’s strategy
and staying at the closest point on the convex hull to Zarathustra. That closest point can’t move
faster than Zarathustra does, since the closest point to Zarathustra on every edge of the convex
hull moves at most as fast as Zarathustra does, and the closest point moves continuously.

Deﬁnition 2.3.3. Let Gdistance ε be the game which is the same as the original game, except that
the human wins by reaching the boundary while the zombie is at a distance greater than ε. (Perhaps
the human needs time to start up a getaway car?) In particular, G0 is the original (continuous)
game.

Lemma 2.3.7. If P is a polygon, then there exists ε0 > 0 (the same as in Theorem 2.3.3) such
that for all ε ∈ (0, ε0), if the human wins the continuous game G0 in a polygon P at a speed ratio
r, then the human wins the game Gdistance ε3 at speed ratio r 1
1+ε .

Proof. The human should start at some point h at distance more than ε from the nearest boundary;
ε0 was chosen small enough that such a place exists. The human can still win G0: if they could
win by some other starting position, the human can immediately run to that position; wherever the
zombie is after that run, the zombie could have started, so the human can simulate their winning
strategy from that starting position to win.
 24

If, from that starting position, there’s a point p on the boundary such that the human can win
G0 with speed ratio r by committing to running straight to p (that is, if there’s a point p ∈ δP
such that r · dh(h, p) < dz(z, p), where z is the zombie’s starting position), then the human can
win Gdistance ε2 with speed ratio r 1
1+ε by running straight to that point. The human’s time to get
there is dh(h, p), in which time the zombie moves at most r 1
1+ε · dh(h, p) < 1
1+ε · dz(z, p), leaving a

distance of at least ε
1+ε · dz(z, p) > ε
2r · dh(h, p) > ε2
2r > ε3, as desired.
Otherwise, the human can’t immediately win G0 with speed ratio r by picking a point on δP
and running straight to it, but can eventually win by doing so by Lemma 2.3.5, so consider the
human’s position h and zombie’s position z at the last time when the human can’t so win.
When the human is at h and the zombie at z, there’s at least one point on the boundary that
the human can reach in the same time as the zombie, since, by the choice of h, after any positive
amount of movement, there’s a point on the boundary that the human can get there in less time
than the zombie.
If there’s any such boundary point at distance more than ε from h, then by the same calculation
as above, the human can win Gdistance ε3 at speed ratio r 1
1+ε by running straight to it. Otherwise,
every such boundary point is within ε of h.
We chose ε0 small enough that no disk of radius 2√
ε0 contains two edges not sharing a vertex.
If all such boundary points are within ε of h, note that the disk of radius 2√ε0 centered at h
contains at least one edge (one with such a boundary point) and at most two; if two, they share a
vertex. Note that the zombie’s distance to any such boundary point is at most rε. As above, we
have ε < ε0 < 1/(2r(P )2) ≤ 1/(2r2) < r−2 (where r(P ) is the critical speed ratio for P ), so the
zombie’s distance to each of them is at most rε < √ε, and the human’s distance to each of them
is also at most that, so z is in a circle of radius 2
√ε0 centered at h.
But we claim that the human can’t win at all with at most ε more movement, much less by
committing to moving straight to one of those boundary points within ε of h, contradicting the
choice of h. The zombie can use the following strategy: keep the line between it and the human
parallel to hz, and use any remaining movement to move toward the human, if the zombie isn’t
already as close as it can get (that is, on δP ). If a zombie follows this strategy, the only relevant
distances are the distances on the line between the human and zombie. For any direction the
human runs in, the zombie’s distance on that line decreases at least as fast (as a fraction of its total
distance) as the human’s does (as a fraction of its total distance); otherwise, the human could win
by running straight in that direction, but we assumed the human couldn’t yet win by doing so.
So as long as the human and zombie stay within that circle of radius 2√ε0, the human can’t
win, contradicting the assumption that, a moment later, the human could win by running straight
a distance at most ε.
In every surviving case, the human can win Gdistance ε3 with speed ratio r 1
1+ε , as desired.

Deﬁnition 2.3.4. Let Gdelay ε be the game where the human can only see and react to where
the zombie was a time ε ago (perhaps due to the ﬁnite speed of neural impulses in the human’s
delicious brain?); the human wins by reaching a point on the boundary that the zombie can’t get
to even with ε more time.

Lemma 2.3.8. If the human has a winning strategy in Gdistance ε, then the human has a winning
strategy in Gdelay ε/2r, where r is the speed ratio.

Proof. If the human, Alice, has a winning strategy in Gdistance ε, we wish to construct a winning
strategy for the human, Bob, in Gdelay ε/2r. Let Alice’s zombie move exactly as Bob’s did a time
ε
2r ago, and let Bob move exactly as Alice does; Bob can do so because Alice’s moves at time t
depend only on the position of Alice’s zombie at time at most t, which is the position of Bob’s

25

zombie at time at most t − ε
2r , which Bob knows at time t. Since Alice has a winning strategy
in her game, she has a winning strategy against any zombie strategy, in particular, against this
taking-orders-from-Bob strategy. So, Alice wins her game, that is, she reaches the boundary while
her zombie is still at a distance at least ε. Bob reaches the boundary at the same time. Since
Alice’s zombie is at distance more than ε from her, Bob’s zombie was at distance more than ε a
time ε
2r ago, and in that much time the zombie can only move a distance less than ε
2 . That leaves
the zombie at a distance more than ε
2 , so the zombie can’t get to Bob’s position even with ε
2r more
time, as claimed.

By the composition of Lemmas 2.3.4, 2.3.5, 2.3.7, and 2.3.8, if the human wins at a speed ratio
r in a polygon P , then there exists ε0 > 0, depending only on P , such that for all ε ∈ (0, ε0), the
human wins Gdelay ε3/2r with speed ratio r 1
(1+ε) ; also, since 2rε < 1, the human wins Gdelay ε4 with
that speed ratio.
We are now ready to prove Theorem 2.3.3.

Proof. Let P be a polygon with critical speed ratio r∗, choose ε0 small enough for Lemma 2.3.8,
and let ε ∈ (0, ε0). Then, by the deﬁnition of r∗, the human wins the continuous game at a speed
ratio of r∗ 1
1+ε . So, by Lemma 2.3.8, the human has a winning strategy in the delayed-information
game Gdelay ε4 with speed ratio r∗ 1
(1+ε)2 .
Suppose z and h satisfy the conditions of Theorem 2.3.3, that is, they’re integers with 0 <
z, h < ε−1 and z/h < r∗ 1
(1+ε)3 . We’ll construct a winning strategy for the human, Bob, in the
(P, ε5, z, h) discrete game. Bob will simulate an Alice playing the Gdelay ε4 game; if Bob has made
m moves in his game, he’ll make that correspond to a time m z
h 1
r∗ ε5(1 + ε)2 in Alice’s simulated
Gdelay ε4 game.
Bob’s strategy is to follow Alice as closely as he can, by ensuring that after m moves he is within
ε8 of Alice’s position at time m z
h 1
r∗ ε5(1 + ε)2. To enact this strategy, Bob needs to ﬁnd a vertex
within ε8 of any point in P , be able to move there in time, and be able to answer Alice’s questions
about where the zombie is.

1. First, we claim that there is a point of the discrete game within ε8 of any point in P where
Alice could be: if the circle of radius ε9 centered at Alice’s position is contained in P , then it
contains a point of ε10Z2, which is a point of the graph; otherwise, Alice is within ε9 of the
boundary, in which case the circle of radius ε8 centered at Alice contains at least 2ε8−2ε9 > ε8

of the boundary, and there are points on the boundary spaced at distance between ε10 and
2ε10, so one of them is within that circle.

2. Second, we claim that Bob can follow Alice’s movement in time at most z
h 1
r∗ ε5(1 + ε)2 in one
step. In time z
h 1
r∗ ε5(1 + ε)2, Alice moves a distance at most z
h 1
r∗ ε5(1 + ε)2. Bob starts within
ε8 of Alice’s starting position and ends within ε8 of Alice’s ending position, so by the triangle
inequality, the distance between Bob’s starting and ending vertices is at most
z
h 1
r∗ ε5(1 + ε)
2 + 2ε8 ≤ z
h 1
r∗ (ε5(1 + ε)
2 + ε8r∗)

< z
h 1
r∗ (ε5(1 + ε)
2 + ε6)

< z
h 1
r∗ (ε5(1 + ε)
3)

< ε
5,

so Bob’s starting vertex and desired ending vertex are adjacent in the graph, and he can keep
up with the simulated Alice.
 26

3. When Alice asks where the zombie is, she’s only allowed to ask about times at least ε4 ago. A
time of ε4 in her game corresponds to at least ⌊ h
z r∗ ε4
ε5 1
(1+ε)2 ⌋ ≥ ⌊ 1
ε ⌋ ≥ h steps for Bob in Bob’s
game. Bob and his zombie alternate, with Bob taking h steps for every z of his zombie’s, so
if Alice asks about a time at least h steps ago in Bob’s game, the zombie has moved in Bob’s
game since then, so Bob knows its position on the graph for his game up until the time Alice
asks about.

4. One step by the zombie in Bob’s game corresponds to a time 1
r∗ ε5(1 + ε)2 in Alice’s simulated
Gdelay ε4 game. In that much time, Alice’s zombie, which has speed r∗ 1
(1+ε)2 , is allowed to
move a distance of ε5. Every pair of adjacent vertices in Bob’s zombie’s graph correspond
to points at distance at most ε5 for Alice’s zombie, so Alice’s zombie can keep up with the
position of Bob’s zombie.

So, Bob can simulate Alice’s game of Gdelay ε4 with speed ratio r∗ 1
(1+ε)2 . Alice has a winning
strategy for that game; that is, she reaches a point on the boundary when her zombie can’t get
there in time ε4. In time ε4, her zombie can move a distance of r∗ε4 1
(1+ε)2 , so her zombie is at

least that distance away, corresponding to at least r∗ 1
ε 1
(1+ε)2 > z
h 1
ε (1 + ε) > z
h 1
ε > z steps in
Bob’s zombie’s graph, so Bob’s zombie can’t reach Bob in the turn after Bob reaches the boundary
following Alice’s strategy, and Bob wins, as desired.
For the other direction, if z/h > r∗(1 + ε)3, we need to show that a human can’t win the
(P, ε5, z, h) game, so suppose for contradiction that Alice has a winning strategy in that game;
we’ll construct a winning strategy for the human, Bob, in the original game with a speed ratio
of z
h 1
(1+ε)3 > r∗, contradicting the deﬁnition of r∗. Bob will make it so that one step for Alice in
the simulated (P, ε5, z, h) correspond to a time of ε5 in his game; one step for Alice is a distance
of at most ε5, so Bob can keep up with the simulated Alice. When Alice’s zombie needs to be
given instructions at the end of a block of h of Alice’s moves, corresponding to time hε5 for Bob,
Bob will use Bob’s zombie’s moves from the last hε5 time, with each of the zombie’s z steps in
that time corresponding to h
z ε5 time in Bob’s game. Bob will instruct Alice’s simulated zombie to,
at each step, move to a point within ε8 of where Bob’s zombie is. There always is such a point,
by the same argument as for Bob in the other direction of this proof, with the added note that
we can assume, by Lemma 2.3.6, that the zombie is in the convex hull (where there are points of
the zombie’s graph). Bob’s zombie moves a distance of at most h
z ε5r∗ < ε5 1
(1+ε)3 in that time,
so the distance between the point corresponding to Alice’s zombie’s start vertex and the point
corresponding to Alice’s zombie’s target vertex is at most ε5 1
(1+ε)3 + 2ε8 by the triangle inequality,
and that’s at most ε5, so Alice’s zombie can keep up with Bob’s. By assumption, Alice wins her
game, so she reaches the boundary when her zombie can’t, even with z more steps. Those z steps
let Alice’s zombie’s time catch up with Bob’s zombie’s time (when Alice moves h steps and then
Alice’s zombie moves z steps, those correspond to the same time interval in Bob’s game), so when
Bob reaches the boundary, Bob’s zombie isn’t there and he wins, as desired.

This proof of Theorem 2.3.3 suﬃces for a polynomial-time approximation scheme for the critical
speed ratio for any particular polygon P , as discussed just after the statement of Theorem 2.3.3.

2.4 Multiple Zombies

In the previous section, we discussed approximating the critical speed ratio below which a human
can win and above which they can’t. In the next section, we’ll prove the computational hardness of

27

calculating or approximating that critical speed ratio under slightly diﬀerent sets of assumptions;
in particular, all of the hardness proofs will require that there be multiple zombies, not just one,
such that any one of them can block the human’s escape; some will also require that there be
multiple humans, who win if at least one escapes. To make the hardness proofs of the next section
more satisfying, therefore, we ﬁrst, in this section, discuss what we can determine when there are
multiple zombies and possibly multiple humans.

Theorem 2.4.1. Every human can escape in a game with multiple humans if and only if the lone
human could escape in the same game with only one human.

Proof. If one human can escape in the game with only one human, all the humans can stay together,
moving as that one human would, and escape. If the zombies can keep a lone human from escaping,
they can ignore all but one of the humans and keep that human from escaping.

Given this result, we’ll assume that, if there are multiple humans, the goal is for at least one
human to escape, perhaps to call for help.

Theorem 2.4.2. If there are nz zombies and nh > nz humans, then one human can always escape.

Proof. Each of the humans can stand at a distinct one of nh spots along the boundary. At at least
nh − nz of those spots, there’s no zombie, so the humans at those spots escape.

2.4.1 Approximation Algorithms

Theorem 2.3.3 in Section 2.3.1 still gives a pseudopolynomial approximation scheme if there are
multiple (but O(1)) humans and/or zombies. The proof is essentially the same: we can solve a
discrete game with O(1) zombies, and the critical speed ratio is bounded above by the critical speed
ratio for one zombie.
One side of Theorem 2.3.2 has an analogue:

Theorem 2.4.3. If P is a polygon and there are nz zombies and one human, then the zombies
win if their speed is at least the minimum over partitions of the boundary into (not necessarily
connected) regions of
 max
p,q in same region dz(p, q)
dh(p, q) .

Proof. Each zombie can ignore all of the boundary but the part assigned to it and use the strategy
of Theorem 2.3.2.

However, for the other side we have no analogue.

Open Problem 1. Does there exist c > 0 such that if P is a polygon and there are nz zombies and
one human, then the human wins if the zombies’ speed is less than the minimum over partitions of
the boundary into (not necessarily connected) regions of

c · max
p,q in same region dz(p, q)
dh(p, q) .

28

2.4.2 Slow Zombies

When there was only one zombie, it only made sense to consider cases where the zombie was faster
than the human; if the zombie is the same speed as the human or slower and there’s any convex
vertex, a human standing near it can win. With multiple zombies, it’s still only nontrivial if the
zombies are at least as fast as the human, since if the human’s faster, it can stand near any edge
and win. However, the case where the humans and the zombies have the same speed becomes
interesting.

Theorem 2.4.4. If the speeds of the human and zombies are equal, and the exterior of the polygon
can be divided into nz convex regions that cover the boundary of the polygon, then the zombies win.

Proof. Each zombie can stay in one region, staying at the closest point in that region to the human.
The closest point in a convex region to the human can’t move faster than the human can, so the
zombies can keep up with this strategy. If the human reaches the boundary, there’s a zombie region
containing that boundary, and therefore a zombie at the closest point in that region to the human,
which is the human’s location itself. So, the human can’t escape.

Corollary 2.4.5. If a polygon P has n vertices and there are n zombies with the same speed as
the human, the human can’t win.

Proof. One zombie can cover each edge.

Theorem 2.4.6. If P is a convex n-gon and there’s one human and ⌈ n
2 ⌉ + 1 zombies, all with the
same speed, then the human can win.

Proof. The human should start at any vertex h on the boundary. Let h′ be the point opposite h
on δP , that is, the point for which the zombie distance from h is maximal. The points h and h′

split δP into two sections, at least one of which must have at least ⌈ n
2 ⌉ vertices (counting h but
not h′). The human should run along that section of perimeter. If at some vertex there’s only one
zombie, then the human can approach one edge not at the vertex, forcing the zombie to that edge,
then shortcut through the polygon to a point near the vertex but on the other edge and escape.
If there are two zombies, the human can do the same thing to ensure that at least one of them is
behind the human when the human moves on to the next vertex. So, for each of the ⌈ n
2 ⌉ vertices,
there must be at least one new zombie guard, plus one zombie guard at the center, and these must
all be distinct because the zombies from h don’t have time to run around past h′ before the human
gets there.

Although Theorem 2.4.6 is, like all other results in this chapter for which the model is unspeci-
ﬁed, true for both the standard model and the moat model as deﬁned in Section 2.1, we can make
a slightly stronger statement in the moat model, with the same proof: even if P is nonconvex, if it
has c convex vertices, then the human can escape from ⌈ c
2 ⌉ + 1 zombies of the same speed as theirs.
There is no analogous lower bound, because 4 zombies suﬃce to guard polygons like the one in
Figure 2.5 with arbitrarily many vertices. Two zombies can stay on the top and two on the bottom;
each of those can be assigned to guard every other triangular region of the convex hull outside P .

2.5 Computational Complexity

In this section, we prove NP-hardness and hardness of approximation results, as speciﬁed in Ta-
ble 2.1, for problems of escaping from zombies with various combinations of parameters:

29

Figure 2.5: A polygon guardable by 4 zombies with speed equal to the human’s, with the (discon-
nected) region for one zombie to guard shaded blue.

1. There could be one human, as in the original problem, or many, as discussed in Section 2.4.

2. There could be one zombie, as in the original problem, or many, as discussed in Section 2.4.

3. In the original problem, the human and zombie moved in a polygon with boundary and its
complement with boundary, respectively. Here we reduce the space from a 2-dimensional
polygon to a 1-dimensional graph, on which we might also be able to impose the additional
constraint that that graph be planar or connected.

4. In the original problem, a human could move into a spot where a zombie was (but not declare
victory); here we may make zombies block human movement.

Theorem 2.5.1. In a game in the graph model (see Section 2.1) in which the zombies win if a
zombie is ever at the same place as a human and there are multiple humans of which only one needs
to escape, it’s NP-hard to decide whether the humans win, even if the graph is planar. Since the
zombies’ movement is irrelevant3, it’s NP-hard to distinguish a critical speed ratio of 0 from ∞.

Proof. We reduce from the Planar Vertex Cover problem of ﬁnding a set of at most k vertices
in a planar graph such that every edge contains at least one of them, which [Lic82] shows to be
NP-hard. Given an instance of Planar Vertex Cover consisting of a planar graph G with e edges
and a target number of vertices k, make a zombie problem with a drawing of that graph for the
humans, an exit vertex (where a zombie could stand and block movement) on each edge, k humans,
and e − 1 zombies; the zombies have nowhere to move.
If there exists a planar vertex cover, the humans can start at the vertices corresponding to
it; then there’s at least one edge that no zombie starts on, and a human who starts at a vertex
contained in that edge can escape by that edge.
If the humans can win the zombie problem, consider the connected components of the drawing
of G minus the exit vertices; there’s one of them per vertex of G. Each human starts in one of
them, and can’t change between them except by passing through an exit vertex, at which point
they could just escape. They start in at most k vertices, which we choose as the vertex cover. If
there’s any edge those vertices don’t cover, the zombies can choose to start everywhere but that

3Perhaps these are zombie plants?

Humans Zombies Geometry Zombies block Result Theorem
Multiple Multiple Planar graph Yes NP-hard, inapproximable Theorem 2.5.1
Multiple Multiple Connected graph No Exp-APX-hard Theorem 2.5.2
1 Multiple Graph Yes 2-inapproximable Theorem 2.5.3

Table 2.1: Complexity results and the assumptions they require.

30

Figure 2.6: A graph for which it’s EXP-APX-hard to determine the critical speed ratio.

edge’s exit vertex, and the humans can’t escape; since the humans win, they must cover every edge,
as desired.

Theorem 2.5.2. In a game in the graph model in which the zombies win if a zombie is ever at the
same place as a human and there are multiple humans of which only one needs to escape, it’s EXP-
APX-hard to ﬁnd the critical speed ratio r∗. That is, unless P = NP, there’s no polynomial-time
algorithm to approximate r∗ to within a factor exponential in the input length.

The exponential inapproximability comes from the lengths of the edges. If the edge lengths are
integers at most L, then the same proof shows that it’s hard to approximate r∗ to within a factor
of L.

Proof. We reduce from the Vertex Cover problem of ﬁnding a set of at most k vertices in a graph
such that every edge contains at least one of them, which is one of Karp’s original 21 NP-hard
problems (from [Kar72]). Given an instance of Vertex Cover consisting of a graph G with e edges
and a target number of vertices k, make a zombie problem with k humans, e − 1 zombies, and
graphs as shown in Figure 2.6: have a human-accessible vertex for each vertex in V (G), edges of
length 2n connecting each of them to a common vertex h, an exit vertex for each edge in E(G),
edges of length 2n connecting each of them to a common vertex z, and edges of length 1 connecting
each edge to its incident vertices.
If there exists a vertex cover, then the humans can start at the vertices corresponding to it.
Then there’s at least one edge that no zombie starts within 2n of, and a human who starts at a
vertex contained in that edge can escape by that edge in time 1, so the critical speed ratio is at
least 2n.
If there’s no vertex cover, then we claim that zombies of speed 4 can win. At all times, there’s
an exit that there’s no human within a distance 2n−1 of (otherwise the set of vertices that humans
are closest to is a vertex cover). The zombies should start at e − 1 exits including every exit there’s
a human within 2n−1 of. Whenever a human comes within 2n−1 of the unguarded exit, there’s a
zombie at an exit that no human’s near; that zombie should run to the newly-threatened exit, a
distance of 2n+1, which the zombie of speed 4 can cover before the human either reaches the exit
or goes back through h to threaten another exit.
So, if we could determine whether the critical speed ratio is at most 4 or at least 2n, we could
solve the vertex cover problem, making this problem EXP-APX-hard, as desired.

Theorem 2.5.3. In a game in the graph model in which the zombies win if a zombie is ever at the
same place as a human, it’s NP-hard to approximate the critical speed ratio r to within a factor of
2.
 31

Figure 2.7: A graph with one human for which it’s NP-hard to determine the critical speed ratio.

Proof. We again reduce from the Vertex Cover problem of ﬁnding a set of at most k vertices in
a graph such that every edge contains at least one of them, which is one of Karp’s original 21
NP-hard problems (from [Kar72]). Given an instance of Vertex Cover consisting of a graph G with
e edges and a target number of vertices k, make a zombie problem with 1 human, k − 1 zombies,
and graphs as shown in Figure 2.6: have a zombie-accessible vertex for each vertex in V (G), an
exit vertex for each edge in E(G), human-accessible edges of length 1 connecting each of them to
a common vertex h, and edges of length 1 connecting each edge to its incident vertices.
If there’s a vertex cover, the zombies can place themselves at the vertices of it, and whenever
the human moves toward an exit, the zombie on the vertex that covers the edge corresponding to
that exit can move to block it (and move back as the human does, staying exactly as close to the
exit as the human is); in this way, even zombies of the same speed as the human can prevent human
escape.
If there’s no vertex cover, the human can start at h, and there’s an exit that no zombie is within
distance 2 of: only a zombie within distance 1 of a vertex contained in that exit’s corresponding
edge is within distance two of the exit, and the regions within distance 1 of each vertex are disjoint,
so if there were a zombie within distance 2 of every vertex, that’d give a vertex cover. The human
can run straight to that exit, and not even a speed 2 zombie can catch it.
So it’s NP-hard to distinguish a critical speed ratio of at most 1 from one at least 2, as claimed.

2.6 Open Problems

The following are some possible directions for further work:

1. Section 2.3 gives only a pseudopolynomial-time approximation scheme for the critical speed
ratio for a polygon P . Is this the best one can do, or is there an approximation scheme whose
time depends only polynomially on at least the length of the description of P , if not also on
log 1
ε ?

2. Theorem 2.3.2 bounds the critical speed ratio between 1 and 9.2504 times maxp,q∈δP dz(p,q)
dh(p,q) .
What’s the range of possible values of that constant? (For a circle, it’s 4.60/(π/2) ≈ 2.93,
but we conjecture that it’s higher for an equilateral triangle.)

3. Is there an analogue of Theorem 2.3.2 describing the critical speed ratio to within a constant
factor when there are two (or O(1)) zombies?

The most obvious analogue, using a 2nd-order Voronoi diagram, does not work: if P is a
long, thin rectangle with one long side subdivided, one zombie should stay on each side, but

32

a 2nd-order Voronoi diagram might put both zombies on one side.

The other most obvious analogue would have one zombie attempts to guard the edge the
human is closest to, the second zombie greedily guards whatever point the ﬁrst zombie would
have the most trouble reaching, and both zombies delay changing their strategies by the use of
fringe regions as in Theorem 2.3.2, but the human might exit multiple fringes simultaneously,
which seems hard for the zombies to account for without paying an extra factor equal to the
number of zombies.

4. We’ve calculated the exact critical speed ratio for circles and for unbounded intersections of
halfplanes, but for even for the simplest bounded intersection of halfplanes, an equilateral
triangle, we can’t calculate the exact speed ratio.

33

Chapter 3

Conﬂict-Free Graph Coloring

This chapter is joint work with Zachary Abel, Victor Alvarez, Erik Demaine, S´andor Fekete, Aman
Gour, Phillip Keldenich, and Christian Scheﬀer, with help from discussions with Bruno Crepaldi,
Pedro de Rezende, Cid de Souza, Stephan Friedrichs, Michael Hemmer, and Frank Quedenfeld. It
has appeared in the proceedings of the ACM-SIAM Symposium on Discrete Algorithms [AAG+18].

3.1 Introduction

Coloring the vertices of a graph is one of the fundamental problems in graph theory, both scien-
tiﬁcally and historically. Proving that four colors always suﬃce to color a planar graph [AH77a,
AH77b, RSST97] was a tantalizing open problem for more than 100 years; the quest for solving
this challenge contributed to the development of graph theory, but also to computers in theorem
proving [Wil13]. A generalization that is still unsolved is the Hadwiger Conjecture [Had43]: A
graph is k-colorable if it has no Kk+1 minor.
Over the years, there have been many variations on coloring, often motivated by particular
applications. One such context is wireless communication, where “colors” correspond to diﬀerent
frequencies. This also plays a role in robot navigation, where diﬀerent beacons are used for providing
direction. To this end, it is vital that in any given location, a robot is adjacent to a beacon with a
frequency that is unique among the ones that can be received. This notion has been introduced as
conﬂict-free coloring, formalized as follows. For any vertex v ∈ V of a simple graph G = (V, E), the
closed neighborhood N [v] consists of all vertices adjacent to v and v itself. A conﬂict-free k-coloring
of G assigns one of k diﬀerent colors to a (possibly proper) subset S ⊆ V of vertices, such that for
every vertex v ∈ V , there is a vertex y ∈ N [v], called the conﬂict-free neighbor of v, such that the
color of y is unique in the closed neighborhood of v. The conﬂict-free chromatic number χCF (G)
of G is the smallest k for which a conﬂict-free coloring exists. Observe that χCF (G) is bounded
from above by the proper chromatic number χ(G) because in a proper coloring, every vertex is its
own conﬂict-free neighbor.
Similar questions can be considered for open neighborhoods N (v) = N [v] \ {v}.
Conﬂict-free coloring has received an increasing amount of attention. Because of the relationship
to classic coloring, it is natural to investigate the conﬂict-free coloring of planar graphs. In addition,
previous work has considered either general graphs and hypergraphs (e.g., see [PT09]) or geometric
scenarios (e.g., see [HKS+15]); we give a more detailed overview further down. This adds to
the relevance of conﬂict-free coloring of planar graphs, which constitute the intersection of general
graphs and geometry. In addition, the subclass of outerplanar graphs is of interest, as it corresponds
to subdividing simple polygons by chords.
 34

There is a spectrum of diﬀerent scientiﬁc challenges when studying conﬂict-free coloring. What
are worst-case bounds on the necessary number of colors? When is it NP-hard to determine
the existence of a conﬂict-free k-coloring, when polynomially solvable? What can be said about
approximation? Are there suﬃcient conditions for more general graphs? And what can be said
about the bicriteria problem, in which also the number of colored vertices is considered? We provide
extensive answers for all of these aspects, basically providing a complete characterization for planar
and outerplanar graphs.

3.1.1 Our Contribution

We present the following results; items 1-7 are for closed neighborhoods, while items 8-11 are for
open neighborhoods.

1. For general graphs, we provide the conﬂict-free variant of the Hadwiger Conjecture: If G does
not contain Kk+1 as a minor, then χCF (G) ≤ k.

2. It is NP-complete to decide whether a planar graph has a conﬂict-free coloring with one color.
For outerplanar graphs, this question can be decided in polynomial time.

3. It is NP-complete to decide whether a planar graph has a conﬂict-free coloring with two
colors. For outerplanar graphs, two colors always suﬃce.

4. Three colors are sometimes necessary and always suﬃcient for conﬂict-free coloring of a planar
graph.

5. For the bicriteria problem of minimizing the number of colored vertices subject to a given
bound χCF (G) ≤ k with k ∈ {1, 2}, we prove that the problem is NP-hard for planar and
polynomially solvable in outerplanar graphs.

6. For planar graphs and k = 3 colors, minimizing the number of colored vertices does not have
a constant-factor approximation, unless P = NP.

7. For planar graphs and k ≥ 4 colors, it is NP-complete to minimize the number of colored
vertices. The problem is ﬁxed-parameter tractable (FPT) and allows a PTAS.

8. Four colors are sometimes necessary and always suﬃcient for conﬂict-free coloring with open
neighborhoods of planar bipartite graphs.

9. It is NP-complete to decide whether a planar bipartite graph has a conﬂict-free coloring with
open neighborhoods with k colors for k ∈ {1, 2, 3}.

10. Eight colors always suﬃce for conﬂict-free coloring with open neighborhoods of planar graphs.

3.1.2 Related Work

In a geometric context, the study of conﬂict-free coloring was started by Even, Lotker, Ron, and
Smorodinsky [ELRS03] and Smorodinsky [Smo03], who motivate the problem by frequency assign-
ment in cellular networks: There, a set of n base stations is given, each covering some geometric
region in the plane. The base stations service mobile clients that can be at any point in the total
covered area. To avoid interference, there must be at least one base station in range using a unique
frequency for every point in the entire covered area. The task is to assign a frequency to each base

35

station minimizing the number of frequencies. On an abstract level, this induces a coloring prob-
lem on a hypergraph where the base stations correspond to the vertices and there is an hyperedge
between some vertices if the range of the corresponding base stations has a non-empty common
intersection.
If the hypergraph is induced by disks, Even et al. [ELRS03] prove that O(log n) colors are
always suﬃcient. Alon and Smorodinsky [AS06] extend this by showing that each family of disks,
where each disk intersects at most k others, can be colored using O(log3 k) colors. Furthermore, for
unit disks, Lev-Tov and Peleg [LTP09] present an O(1)-approximation algorithm for the number
of colors. Horev et al. [HKS10] extend this by showing that any set of n disks can be colored with
O(k log n) colors, even if every point must see k distinct unique colors. Abam et al. [AdBP08]
discuss the problem in the context of cellular networks where the network has to be reliable even
if some number of base stations fault, giving worst-case bounds for the number of colors required.
For the dual problem of coloring a set of points such that each region from some family of regions
contains at least one uniquely colored point, Har-Peled and Smorodinsky [HPS05] prove that with
respect to every family of pseudo-disks, every set of points can be colored using O(log n) colors.
For rectangle ranges, Elbassioni and Mustafa [EM06] show that it is possible to add a sublinear
number of points such that a conﬂict-free coloring with O(n3/8·(1+ε)) colors becomes possible.
Ajwani et al. [AEGR07] complement this by showing that coloring a set of points with respect
to rectangle ranges is always possible using O(n0.382) colors. For coloring points on a line with
respect to intervals, Cheilaris et al. [CGRS14] present a 2-approximation algorithm, and a (5 − 2
k )-
approximation algorithm when every interval must see k uniquely colored vertices. Hoﬀman et
al. [HKS+15] give tight bounds for the conﬂict-free chromatic art gallery problem under rectangular
visibility in orthogonal polygons: Θ(log log n) are sometimes necessary and always suﬃcient. Chen
et al. [CFK+07] consider the online version of the conﬂict-free coloring of a set of points on the
line, where each newly inserted point must be assigned a color upon insertion, and at all times the
coloring has to be conﬂict-free. Also in the online scenario, Bar-Nov et al. [BNCOS10] consider a
certain class of k-degenerate hypergraphs which sometimes arise as intersection graphs of geometric
objects, presenting an online algorithm using O(k log n) colors.
On the combinatorial side, some authors consider the variant in which all vertices need to be
colored; note that this does not change asymptotic results for general graphs and hypergraphs: it
suﬃces to introduce one additional color for vertices that are left uncolored in our constructions.
Regarding general hypergraphs, Ashok et al. [ADK15] prove that maximizing the number of conﬂict-
freely colored edges in a hypergraph is FPT when parameterized by the number of conﬂict-free edges
in the solution. Cheilaris et al. [CSS11] consider the case of hypergraphs induced by a set of planar
Jordan regions and prove an asymptotically tight upper bound of O(log n) for the conﬂict-free list
chromatic number of such hypergraphs. They also consider hypergraphs induced by the simple
paths of a planar graph and prove an upper bound of O(√n) for the conﬂict-free list chromatic
number. For hypergraphs induced by the paths of a simple graph G, Cheilaris and T´oth [CT11]
prove that it is coNP-complete to decide whether a given coloring is conﬂict-free if the input is G.
Regarding the case in which the hypergraph is induced by the neighborhoods of a simple graph
G, which resembles our scenario, Pach and T´ardos [PT09] prove that the conﬂict-free chromatic
number of an n-vertex graph is in O(log2 n). Glebov et al. [GST14] extend this from an extremal and
probabilistic point of view by proving that almost all G(n, p)-graphs have conﬂict-free chromatic
number O(log n) for p ∈ ω(1/n), and by giving a randomized construction for graphs having
conﬂict-free chromatic number Θ(log2 n). In more recent work, Gargano and Rescigno [GR15]
show that ﬁnding the conﬂict-free chromatic number for general graphs is NP-complete, and prove
that the problem is FPT w.r.t. vertex cover or neighborhood diversity number.

36

3.2 Preliminaries

For every vertex v ∈ V , the open neighborhood of v in G is denoted by NG(v) := {w ∈ V (G) | vw ∈
E(G)}, and the closed neighborhood is denoted by NG[v] := NG(v) ∪ {v}. We sometimes write
N (v) instead of NG(v) when G is clear from the context.
A partial k-coloring of G is an assignment χ : V ′ → {1, . . . , k} of colors to a subset V ′ ⊆ V (G) of
the vertices. χ is called closed-neighborhood conﬂict-free k-coloring of G iﬀ, for each vertex v ∈ V ,
there is a vertex w ∈ NG[v]∩V ′ such that χ(w) is unique in NG[v], i.e., for all other w′ ∈ NG[v]∩V ′,
χ(w′) ̸= χ(w). We call w the conﬂict-free neighbor of v. Analogously, χ is called open-neighborhood
conﬂict-free k-coloring of G iﬀ, for each vertex v ∈ V , there is a conﬂict-free neighbor w ∈ NG(v).
In order to avoid confusion with proper k-colorings, i.e., colorings that color all vertices such
that no adjacent vertices receive the same color, we use the term proper coloring when referring
to this kind of coloring. The minimum number of colors needed for a proper coloring of G, also
known as the chromatic number of G, is denoted by χP (G), whereas the minimum number of colors
required for a closed-neighborhood conﬂict-free coloring of G (G’s closed-neighborhood conﬂict-free
chromatic number ) is written as χCF (G). The open-neighborhood conﬂict-free chromatic number
of G is χO(G). To improve readability we sometimes omit the type of neighborhood if it is clear
from the context.
Note that, because every vertex satisﬁes v ∈ N [v], every proper coloring of G is also a closed-
neighborhood conﬂict-free coloring of G, and thus χCF (G) ≤ χP (G). The same does not hold for
open neighborhoods. There is no constant factor c1 > 0 such that either c1 · χO(G) ≤ χP (G) or
c1 · χP (G) ≤ χO(G) holds for all graphs G.
For closed neighborhoods, we deﬁne the conﬂict-free domination number γk
CF (G) of G to be
the minimum number of vertices that have to be colored in a conﬂict-free k-coloring of G. We
set γk
CF (G) = ∞ if G is not conﬂict-free k-colorable. Because the set of colored vertices is a
dominating set, the conﬂict-free domination number satisﬁes γk
CF (G) ≥ γ(G) for all k, where γ(G),
the domination number of G, is the size of a minimum dominating set of G. Moreover, for any
graph, there is a k ≤ γ(G) such that γk
CF (G) = γ(G).
We denote the complete graph on n vertices by Kn:= ({1, . . . , n}, {{u, v} | u, v ∈ {1, . . . , n},
u ̸= v}), and the complete bipartite graph on n and m vertices as Kn,m. We deﬁne the graph
K−3
n := (V (Kn), E(Kn) \ E(K3)), which is obtained by removing any three edges forming a single
triangle from a Kn.
We also provide a number of results for outerplanar graphs. An outerplanar graph is a graph
that has a planar embedding for which all vertices belong to the outer face of the embedding.
An outerplanar graph is called maximal iﬀ no edges can be added to the graph without losing
outerplanarity [BH94]. Maximal outerplanar graphs can also be characterized as the graphs having
an embedding corresponding to a polygon triangulation, which illustrates their particular relevance
in a geometric context. In addition, maximal outerplanar graphs exhibit a number of interesting
graph-theoretic properties. Every maximal outerplanar graph is chordal, a 2-tree and a series-
parallel graph. Also, every maximal outerplanar graph is the visibility graph of a simple polygon.
For some of our NP-hardness proofs, we use a variant of the planar 3-SAT problem, called
Positive Planar 1-in-3-SAT. This problem was introduced and shown to be NP-complete by
Mulzer and Rote [MR08], and consists of deciding whether a given positive planar 3-CNF formula
allows a truth assignment such that in each clause, exactly one literal is true.

Deﬁnition 3.2.1 (Positive planar formulas).
A formula φ in 3-CNF is called positive planar iﬀ it is both positive and backbone planar. A formula
φ is called positive iﬀ it does not contain any negation, i.e. iﬀ all occurring literals are positive. A

37

formula φ, with clause set C = {c1, . . . , cl} and variable set X = {x1, . . . , xn}, is called backbone
planar iﬀ its associated graph G(φ) := (X ∪ C, E(φ)) is planar, where E(φ) is deﬁned as follows:

• xicj ∈ E(φ) for a clause cj ∈ C and a variable xi ∈ X iﬀ xi occurs in cj,

• xixi+1 ∈ E(φ) for all 1 ≤ i < n.

The path formed by the latter edges is also called the backbone of the formula graph G(φ).

3.3 Closed Neighborhoods: Conﬂict-Free Coloring of General Graphs

In this section we consider the Conflict-Free k-Coloring problem on general simple graphs
with respect to closed neighborhoods. In § 3.3.1, we prove that this problem is NP-complete for
any k ≥ 1. In § 3.3.2, we provide a suﬃcient criterion that guarantees conﬂict-free k-colorability.
In § 3.3.3, we consider the conﬂict-free domination number and prove that, for any k ≥ 3, there is
no constant-factor approximation algorithm for γk
CF .

3.3.1 Complexity

Theorem 3.3.1. Conflict-Free k-Coloring is NP-complete for any ﬁxed k ≥ 1.

Membership in NP is clear. For k ≥ 3, we prove NP-hardness using a reduction from proper k-
Coloring. For k ∈ {1, 2}, refer to § 3.4, where we prove Conflict-Free k-Coloring of planar
graphs to be NP-complete for k ∈ {1, 2}.
Central to the proof is the following lemma that enables us to enforce certain vertices to be
colored, and both ends of an edge to be colored using distinct colors.

Lemma 3.3.2. Let G be any graph, u, v ∈ V (G) and vu = e ∈ E(G). If N (v) contains two disjoint
and independent copies of a graph H with χCF (H) = k, not adjacent to any other vertex w ∈ G,
every conﬂict-free k-coloring of G colors v. If the same holds for u and in addition, NG(u) ∩ NG(v)
contains two disjoint and independent copies of a graph J with χCF (J) = k − 1, not adjacent to
any other vertex w ∈ G, every conﬂict-free k-coloring of G colors u and v with diﬀerent colors.

Proof. Assume towards a contradiction that there was a conﬂict-free k-coloring χ that avoids col-
oring v. Then, due to the copies of H being independent, disjoint and not connected to any other
vertex, the restriction of χ to the vertices of each of the two copies must induce a conﬂict-free
coloring on H. As χCF (H) = k, this implies that χ uses k colors on each copy. Therefore, in the
open neighborhood of v, there are at least two vertices colored with each color. This leads to a
contradiction, because v cannot have a conﬂict-free neighbor.
For the second proposition, suppose there was a conﬂict-free coloring assigning the same color
to u and v. Without loss of generality, let this color be 1. As every vertex of the two copies of
J now sees two occurrences of color 1, color 1 can not be the color of the unique neighbor of any
vertex of J, and any occurrence of color 1 on the vertices of J can be removed. Therefore, we
can assume each of the two copies of J to be colored in a conﬂict-free manner using the colors
{2, . . . , k}. Observe that, due to χCF (J) = k − 1, each of these colors must be used at least once
in each copy. This implies that both u and v see each color at least twice: The two copies of J
enforce two occurrences of the colors {2, . . . , k}, and color 1 is assigned to both u and v, which are
connected by an edge. This is a contradiction, and therefore, both u and v must be colored with
distinct colors.
 38

Next, we give an inductive construction of graphs, Gk, with χCF (Gk) = k. The proof of NP-
hardness relies on this hierarchy.

1. The ﬁrst graph G1 of the hierarchy consists of a single isolated vertex. G2 is a K1,3 with
one edge subdivided by another vertex, or, equivalently, a path of length 3 with a leaf vertex
attached to one of the inner vertices.

2. Given Gk and Gk−1, Gk+1 is constructed as follows for k ≥ 2:

• Take a complete graph G = Kk+1 on k + 1 vertices.

• To each vertex v ∈ V (Kk+1), attach two disjoint and independent copies of Gk, adding
an edge from v to every vertex of both copies of Gk.

• For each edge e = vw ∈ E(Kk+1), add two disjoint and independent copies of Gk−1,
adding an edge from v and w to every vertex of both copies.

The number of vertices of the graphs Gk obtained by the above construction satisﬁes the recursive
formula |G1| = 1, |G2| = 5, |Gk+1| = (k + 1) · (2|Gk| + k|Gk−1| + 1),

which is in Ω (2k) and O (2k log k). Figure 3.1 depicts the graph G3, which in addition to being
planar is a series-parallel graph.

G 2 G 2

G 1

G 1

Figure 3.1: The graph G3.

Lemma 3.3.3. For Gk constructed in this manner, χCF (Gk) = k.

Proof. The proof uses induction over k. Application of Lemma 3.3.2 implies that all vertices of the
Kk+1 underlying Gk+1 have to be colored using diﬀerent colors. Therefore, χCF (Gk+1) ≥ k + 1.
By coloring all k + 1 vertices of the underlying Kk+1 with a diﬀerent color, we obtain a conﬂict-free
(k + 1)-coloring of Gk+1, implying χCF (Gk+1) ≤ k + 1.

Lemma 3.3.4. For k ≥ 2, k-Coloring ≼ Conflict-Free k-Coloring. Therefore, for k ≥ 3,
Conflict-Free k-Coloring is NP-complete.
 39

Proof. Given a graph G for which to decide proper k-colorability for a ﬁxed k. We construct a
graph G′ that is conﬂict-free k-colorable iﬀ G is k-colorable. G′ is constructed from G by attaching
two copies of Gk to each vertex v ∈ V (G), by adding an edge from v to each vertex of the copies
of Gk. For each edge uv ∈ E(G), we attach two copies of Gk−1 to both endpoints of uv by adding
an edge from u and v to all vertices of both copies. As k is ﬁxed, |Gk| and |Gk−1| are constant,
implying that G′ can be constructed in polynomial time.
A proper k-coloring of G induces a conﬂict-free k-coloring of G′ by leaving all other vertices
uncolored. On the other hand, by Lemma 3.3.2, a conﬂict-free k-coloring χ of G′ colors all vertices
v ∈ V (G) and for every edge, the colors of both endpoints are distinct. Therefore, the restriction
of χ to V (G) is a proper k-coloring of G.

3.3.2 A Suﬃcient Criterion for k-Colorability

In this section we present a suﬃcient criterion for conﬂict-free k-colorability together with an
eﬃcient heuristic that can be used to color graphs satisfying this criterion with k colors in a
conﬂict-free manner. This heuristic is called iterated elimination of distance-3-sets and is detailed
in Algorithm 1. The main idea of this heuristic is to iteratively compute maximal sets of vertices at
pairwise (link) distance at least 3, coloring all vertices in one of these sets using one color, and then
removing these vertices and their neighbors until all that remains is a collection of disconnected
paths, which can then be colored using one color.

Algorithm 1 Iterated elimination of distance-3-sets

1: i ← 1, χ ← ∅

2: Remove all isolated paths from G

3: while G is not empty do

4: D ← ∅

5: For each component of G, select some vertex v and add it to D

6: while there is a vertex w at distance ≥ 3 from all vertices in D do

7: Choose w at distance exactly 3 from some vertex in D

8: D ← D ∪ {w}

9: ∀u ∈ D : χ(u) ← i

10: i ← i + 1

11: Remove N [D] from G

12: Remove all isolated paths from G

13: Color all removed isolated paths using color i

Theorem 3.3.5. Let G be a graph and k ≥ 1. If G has neither Kk+2 nor K−3
k+3 as a minor, G
admits a conﬂict-free k-coloring that can be found in polynomial time using iterated elimination of
distance-3 sets.

Proof. For k = 1, a graph G with neither a K3 nor a K−3
4 = K1,3 minor consists of a collection of
isolated paths. A path on 3n vertices can be colored with one color by coloring the middle vertex
of every three vertices. This does not color the vertices at either end, so up to two vertices can be
removed from the path to get colorings for paths on 3n − 1 and 3n − 2 vertices.
For k ≥ 2, we use induction as follows: First, we color an inclusion-wise maximal subset D ⊆ V
of vertices at pairwise distance at least 3 to each other using color 1. This set D is chosen such that
each vertex v ∈ D is at distance exactly 3 from some v′ ∈ D. Coloring D provides a conﬂict-free

40

neighbor of color 1 to every vertex in N [D]. Therefore, the vertices in N [D] are covered and can
be removed from the graph. The remaining graph consists of vertices at distance 2 to some vertex
in D; we call these vertices unseen in the remainder of the proof. We show that the remaining
graph has no Kk+1 and no K−3
k+2 as a minor. By induction, iterated elimination of distance 3 sets
requires k − 1 colors to color the remaining graph, and thus k colors suﬃce for G.
If the graph is disconnected, iterated elimination of distance 3 sets works on all components
separately, so we can assume G to be connected. We claim that there is no set U of unseen vertices
that is a cutset of G. Suppose there were such a cutset U and let H be any component of G \ U
not containing v, the ﬁrst selected vertex during the construction of D. At least one vertex of H is
colored: every vertex in U is at distance at least two from every colored vertex not in H, therefore,
every vertex in H is at distance at least three from every colored vertex not in H. Consider the
iteration where the ﬁrst vertex w of H is added to the set of colored vertices D. At this point, w
is at distance exactly 3 from some colored vertex not in H. However, this implies w is adjacent to
some vertex from U , contradicting the fact that all vertices in U are unseen.
Now, suppose for the sake of contradiction that the set W of unseen vertices contains a Kk+1
or K−3
k+2 minor. W is not the whole graph, because at least one vertex is colored, so there must be
a vertex v not in the Kk+1 or K−3
k+2 minor. For every vertex w ∈ W , there is a path from v to w
that intersects W only at w. Otherwise, W \ {w} would be a cutset separating v from w. So, if
the graph induced by W had a Kk+1 or K−3
k+2 minor, we could contract G \ W to a single vertex,
which would be adjacent to all vertices in W , yielding a Kk+2 or K−3
k+3 minor of G, which does not
exist.

Observe that Gk+1 contains a K−3
k+3 as a minor, but not a Kk+2, proving that just excluding Kk+2
as a minor does not suﬃce to guarantee k-colorability. Moreover, note that Kk+1 is a minor of
Kk+2 and K−3
k+3.
This yields the following corollary, which is the conﬂict-free variant of the Hadwiger Conjecture.

Corollary 3.3.6. All graphs that do not have Kk+1 as a minor are conﬂict-free k-colorable.

3.3.3 Conﬂict-Free Domination Number

In this section we consider the problem of minimizing the number of colored vertices in a conﬂict-free
k-coloring for a ﬁxed k, which is equivalent to computing γk
CF . We call the corresponding decision
problem k-Conflict-Free Dominating Set. We show that approximating the conﬂict-free
domination number in general graphs is hard for any ﬁxed k. In § 3.5 we discuss the k-Conflict-
Free Dominating Set problem for planar graphs.

Theorem 3.3.7. Unless P = NP, for any k ≥ 3, there is no polynomial-time approximation
algorithm for γk
CF (G) with constant approximation factor.

Proof. We use a reduction from proper k-Coloring for the proof. Assume towards a contradiction
that there was a polynomial-time approximation algorithm for γk
CF (G) with approximation factor
c ≥ 1. Let G be a graph on n vertices for which we want to decide k-colorability. For each vertex
v of G, add M := (n + 1)(c + 1) vertices uv to G and connect them to v. For each edge vw of
G, add M vertices uvw to G and connect them to both v and w. Let G′ be the resulting graph.
Clearly, the size of G′ is polynomial in the size of G. Additionally, G′ is planar if G is, and G′

has a conﬂict-free k-coloring of size n iﬀ G is properly k-colorable: Any proper k-coloring of G is a
conﬂict-free k-coloring of G′, as every vertex added to G is either adjacent to two distinctly colored
vertices of G, or adjacent to just one vertex of G. Conversely, let χ be a conﬂict-free coloring of G′,

41

coloring just n vertices. If χ did not assign a color to some vertex v of G, it would have to color
all M ≥ n + 1 neighbors of v. If χ assigned the same color to any pair v, w of vertices adjacent
in G, it would have to color all M vertices adjacent only to v and w. Therefore, χ is a proper
coloring of G. Running a c-approximation algorithm A for γk
CF on G′ results in an approximate
value A(G′) ≤ c · γk
CF (G′). We have A(G′) ≤ c · n < M if G is k-colorable, and A(G′) ≥ M if G is
not; thus we could decide proper k-colorability in polynomial time.

3.4 Closed Neighborhoods: Planar Conﬂict-Free Coloring

This section deals with the Planar Conflict-Free k-Coloring problem which consists of
deciding conﬂict-free k-colorability for ﬁxed k on planar graphs. Due to the 4-color theorem, we
immediately know that every planar graph is conﬂict-free 4-colorable. This naturally leads to the
question of whether there are planar graphs requiring 4 colors or whether fewer colors might already
suﬃce for a conﬂict-free coloring, which we address in the following two sections.

3.4.1 Complexity

For k ∈ {1, 2} colors, we show that the problem of deciding conﬂict-free k-colorability on planar
graphs is NP-complete. This implies that 2 colors are not suﬃcient.

Theorem 3.4.1. Deciding planar conﬂict-free 1-colorability is NP-complete.

Proof. Membership in NP is obvious. The proof of NP-hardness is done by reduction from the
problem Positive Planar 1-in-3-SAT. From a positive planar 3-CNF formula φ with clauses
C = {c1, . . . , cl} and variables X = {x1, . . . , xn} we construct in polynomial time a graph G1(φ)
such that φ is 1-in-3-satisﬁable iﬀ G1(φ) admits a conﬂict-free 1-coloring.
First, ﬁnd and ﬁx a planar embedding d of G(φ). G1(φ) is constructed from G(φ) and d
as follows: For every variable xi, there is a cycle Zi = (zi,1, . . . , zi,12) of length 12. The vertices
zi,1, zi,4, zi,7, zi,10 are referred to as true vertices of Zi, all other vertices are false vertices. Moreover,
vertices zi,1, zi,2, zi,3 are called upper vertices of Zi, and vertices zi,7, zi,8, zi,9 are called lower vertices
of Zi. Additionally, vertices zi,4, zi,5, zi,6 are called right vertices of Zi and zi,10, zi,11, zi,12 are called
left vertices of Zi.
For each clause cj, there is a cycle (cj,1, . . . , cj,4) of length 4 in G1(φ). To each variable xi for
i ∈ {2, . . . , n − 1}, we associate two disjoint sequences Ui = (uj)|Ui|
j=1 and Li = (lj)|Li|
j=1 of clauses xi
appears in. The sequences are constructed using a clockwise (with respect to d) enumeration of the
edges of xi in G(φ), starting with xi−1xi. Let (xi−1xi, xicj1, . . . , xicjλ, xixi+1, xicjλ+1, . . . , xicjµ)
be the sequence of edges encountered in this manner and set Ui := (cj1, . . . , cjλ) and Li :=
(cjλ+1, . . . , cjµ). For i ∈ {1, n}, Li is empty and Ui contains all clauses xi appears in, again in
clockwise order. In G1(φ), the clauses and variables are connected such that for each clause cj that
xi occurs in, either the upper or the lower true vertex of xi is adjacent to cj,1. More precisely, for
variable xi, if cj = um, we add the edge cj,1zi,1 to connect the upper true vertex to the clause.
If cj = lm, we add cj,1zi,7 to connect the lower true vertex to the clause. Because the order of
edges around each vertex is preserved by the construction, the graph G1(φ) obtained in this way
can be embedded in the plane by a suitable adaptation of d. See Figure 3.2 for an example of the
construction.
Now we prove that G1(φ) is conﬂict-free 1-colorable iﬀ φ is 1-in-3-satisﬁable. Regarding ne-
cessity, a valid truth assignment b : X → B yields a valid conﬂict-free coloring by coloring the
vertex cj,3 of every clause, coloring all true vertices of variables with b(xi) = 1 and coloring the

42

x 1 x 2 x 3 x 4 x 5

c1 c2

c3 c4

z 1∅1

c1∅1
 c1∅3

z 1∅3

Figure 3.2: A formula graph G(φ) (dashed) and the corresponding G1(φ) (solid).

false vertices zi,3, zi,6, zi,9, zi,12 of all other variables. Thus, in every cycle Zi, every third vertex
is colored, providing a conﬂict-free neighbor to every vertex of Zi. Moreover, in each clause, by
virtue of cj,3 being colored, vertices cj,2, cj,3, cj,4 have a conﬂict-free neighbor. Because b is a valid
truth assignment, for each clause, the vertex cj,1 is adjacent to exactly one colored true vertex.
Therefore, the coloring constructed in this way is conﬂict-free.
Regarding suﬃciency, we ﬁrst argue that the vertices cj,1, cj,2, cj,4 can never be colored: If cj,1
receives a color, then cj,3 still enforces that one of cj,2, cj,3, cj,4 is colored, leading to a contradiction
in either case. If cj,2 receives a color, then cj,4 cannot have a conﬂict-free neighbor and vice versa.
Therefore, no clause vertex can be the conﬂict-free neighbor of any vertex of Zi. Thus, the conﬂict-
free neighbor of every vertex of Zi must itself be a vertex of Zi. Moreover, the conﬂict-free neighbor
of every vertex cj,1 must be a true vertex. Thus, there are exactly three ways to color each cycle
Zi: either by coloring the true vertices (one possibility), or by coloring every other false vertex
(two possibilities). A valid conﬂict-free 1-coloring of G1(φ) satisﬁes the property that for each
clause cj, exactly one of the true vertices adjacent to cj,1 is colored. Hence, a valid conﬂict-free
1-coloring of G1(φ) induces a valid truth assignment b by setting b(xi) = 1 iﬀ all true vertices of xi
are colored.

Theorem 3.4.2. It is NP-complete to decide whether a planar graph admits a conﬂict-free 2-
coloring.

The proof requires the gadget G≤1 depicted in Figure 3.3. G≤1 consists of three vertices v, w1, w2
forming a triangle. Each edge ux of the triangle has two corresponding vertices y1
ux, y2
ux, each
connected to u and x. Furthermore, both w1 and w2 are attached to two copies of a cycle on 4
vertices, where every vertex of both cycles is adjacent to the corresponding wi. G≤1 can be used
to enforce that the vertices connected to its central vertex v are colored using at most one distinct
color:

Lemma 3.4.3. Let G = (V, E) be any graph, let v ∈ V and let G′ be the graph resulting from
adding a copy of G≤1 to G by identifying v in G with v in G≤1. Then (1) G′ is planar if G is, and
(2) every conﬂict-free 2-coloring of G′ leaves v uncolored and uses at most one color on NG[v].

Proof. The planarity of G′ follows from the planarity of G by the observation that G≤1 is planar
and can be embedded in any face incident to v in a planar embedding of G. Now consider a

43

conﬂict-free 2-coloring χ of G′. χ must color both w1 and w2. Otherwise, χ restricted to each of
the two 4-cycles adjacent to wi must be a valid conﬂict-free 2-coloring. However, as C4 requires
at least 2 diﬀerent colors, wi then sees two occurrences of both colors, and thus cannot have a
conﬂict-free neighbor anymore. Furthermore, χ(w1) ̸= χ(w2), as otherwise, y1
w1w2 and y2
w1w2 must
both be colored with the other color; but then, w1 and w2 again see two occurrences of both colors.
By an analogous argument, χ must not color v. Moreover, χ cannot use more than one color on
NG[v], because v already sees one occurrence of each color, so adding another occurrence of both
colors would yield a conﬂict at v.

v  1

: : : : : :

w1 w2

NG [v]

y1
w1w2

Figure 3.3: Gadget G≤1
 Z i
 ≤ 1 Z i +1≤ 1
 ≤ 1
 c j; 3

c j; 1
 ≤ 1
 c j

Z i −1
 upper

lower

left right

t f f

Figure 3.4: Clause and variable gadget for k = 2

Proof of Theorem 3.4.2. NP-hardness is proven by constructing, in polynomial time, a planar graph
G2(φ) from the graph G1(φ) used in the hardness proof for k = 1, such that G2(φ) is conﬂict-free
2-colorable iﬀ G1(φ) is conﬂict-free 1-colorable.
The construction is carried out by adding a gadget G≤1 to every variable cycle Zi of G1(φ),
to every clause cycle and between the right and left vertices of two adjacent variable cycles Zi
and Zi+1. This is depicted in Figure 3.4. More precisely, for every cycle Zi, we add one copy of
gadget G≤1, and connect its central vertex v to all vertices of the cycle. In a planar embedding of
G2(φ), these gadgets can be embedded within the face deﬁned by the cycles Zi and thus do not
harm planarity. By Lemma 3.4.3, this enforces that on every cycle, only one color can be used.
Moreover, for every edge xixi+1 in G(φ), we add one copy of G≤1 that we connect to the right
vertices of xi and the left vertices of xi+1. This preserves planarity because these gadgets and the
added edges can be embedded in the face crossed by xixi+1 in some ﬁxed embedding d of G(φ).
As one of the right vertices of xi and one of the left vertices of xi+1 must be colored, this enforces
that the same single color must be used to color all cycles Zi. Finally, we add a copy of G≤1 to
every clause cj and connect it to cj,1, . . . , cj,4. Again, this preserves planarity because the gadget
may be embedded in the face deﬁned by (cj,1, . . . , cj,4).
We now argue that G2(φ) is conﬂict-free 2-colorable iﬀ G1(φ) is conﬂict-free 1-colorable. A
1-coloring of G1(φ) induces a 2-coloring of G2(φ) by copying the color assignment and coloring the
internal vertices of the added gadgets as described in the proof of Lemma 3.4.3. Now, let G2(φ) be
conﬂict-free 2-colorable and ﬁx a valid 2-coloring χ. In each clause, χ must color cj,3 and neither
of cj,1, cj,2 nor cj,4 can be colored. Therefore, no clause vertex can be the conﬂict-free neighbor of
any vertex of Zi. Thus, the conﬂict-free neighbor of every vertex of Zi must itself be a vertex of Zi.
Moreover, the conﬂict-free neighbor of every vertex cj,1 must be a true vertex. As there is only one

44

color available to color all cycle vertices of all variables, the restriction of χ to the vertices of G1(φ)
yields a valid 1-coloring except for the fact that some cj,3 might use a diﬀerent color than the one
used for the variables. However, this can be ﬁxed by simply replacing all occurring colors with one
single color. Hence, G2(φ) is conﬂict-free 2-colorable iﬀ G1(φ) is conﬂict-free 1-colorable.

3.4.2 Suﬃcient Number of Colors

As shown above, it is NP-complete to decide whether a planar graph has a conﬂict-free k-coloring
for k ∈ {1, 2}. On the positive side, we can establish the following result, which follows from the
more general results discussed in § 3.3.2.

Corollary 3.4.4 (of Theorem 3.3.5). Every outerplanar graph is conﬂict-free 2-colorable and every
planar graph is conﬂict-free 3-colorable. Moreover, such colorings can be computed in polynomial
time.

Outerplanar graphs are not the only interesting graph class for which one might suspect two
colors to be suﬃcient. Two other interesting subclasses of planar graphs are series-parallel graphs
and pseudomaximal planar graphs. However, each of these classes contains graphs that do not admit
a conﬂict-free 2-coloring: The graph G3 as deﬁned in § 3.3 is an example of a series-parallel graph
requiring three colors. Figure 3.5 depicts a maximal outerplanar graph O9 satisfying χCF (O9) = 2.
This graph can be used to obtain a pseudomaximal planar graph M with χCF (M ) = 3 by adding
two copies of O9 to the neighborhood of every vertex of a triangle, similar to the construction of
G3, and adding gadgets on the inside of the triangle as depicted in Figure 3.6.

Figure 3.5: The maximal outerplanar graph O9.

Furthermore, observe that Theorem 3.4.4 does not hold if every vertex must be colored. In this
case, there are outerplanar graphs requiring 3 colors for a conﬂict-free coloring. One can obtain an
example of such a graph by adding a chord to a cycle of length 5.

3.5 Closed Neighborhoods: Planar Conﬂict-Free Domination

In this section we consider the decision problem k-Conflict-Free Dominating Set for planar
graphs. In § 3.5.1, we deal with the cases when k ∈ {1, 2} for planar and outerplanar graphs, and
we give a polynomial time algorithm to compute an optimal conﬂict-free coloring of outerplanar
graphs with k ∈ {1, 2} colors. Section 3.5.2 discusses the problem for k ≥ 3.

3.5.1 At Most Two Colors

We start by pointing out that, for every conﬂict-free 1-colorable graph G, γ1
CF (G) = γ(G) holds.
Moreover, Corollary 3.5.1 discusses the complexity of k-Conflict-Free Dominating Set and

45

Figure 3.6: The pseudomaximal planar graph M , without the O9 gadgets.

Theorem 3.5.2 states positive results for outerplanar graphs.

Corollary 3.5.1 (of Theorems 3.4.1 and 3.4.2).
k-Conflict-Free Dominating Set is NP-complete for k ∈ {1, 2} for planar graphs.

Theorem 3.5.2. Let k ∈ {1, 2} and let G be an outerplanar graph. We can decide in polynomial
time whether χCF (G) ≤ k. Moreover, we can compute a conﬂict-free k-coloring of G that minimizes
the number of colored vertices in O(n4k+1) time.

The proof of Theorem 3.5.2 relies on a polynomial-time algorithm that computes a k-coloring of
the input outerplanar graph G if and only if such a coloring exists (which thus solves the decision
problem). In the following, we describe our algorithm.
Let G = (V, E) be an outerplanar graph. Let χ : V ′ ⊆ V (G) → {0, 1, . . . , k} be a partial
coloring of the vertices of G and let v ∈ V . Observe that χ deﬁned like this diﬀers from the
deﬁnition given earlier in the introduction. We call a pair Cv = [χ(v), Sv] a conﬁguration of v,
where χ(v) ∈ {0, 1, . . . , k} denotes the color of v. If χ(v) = 0, we regard v as uncolored. The set
Sv ⊆ N [v] is the set of conﬂict-free neighbors of v, along with their colors. That is, every w ∈ Sv
is a conﬂict-free neighbor of v under χ. For e = uv ∈ E we call a pair Ce = [Cu, Cv] a conﬁguration
of e. By Cw
e we denote the conﬁguration of an endpoint w ∈ {u, v} of e. Observe that if χ was
conﬂict-free, then Sv ̸= ∅, and Cu and Cv do not conﬂict with each other. For the latter property
we say that Cu and Cv are compatible and we denote this by Cu ↔ Cv. If Cv
e = Cv
e′ for a pair
e = uv, e′ = vw of incident edges, then we say Ce′ is compatible with Ce. The following observation
is straightforward:

Observation 3.5.3. Let G be an outerplanar graph. Let C = {C1, . . . , C|E|} be a set of conﬁgu-
rations over the edges of G using k colors. If for every pair e = uv, e′ = vw of incident edges,
Cu ↔ Cv and Cv ↔ Cw holds and Ce′ is compatible with Ce, then a conﬂict-free k-coloring can be
obtained from C.

Now let v ∈ V (G). Observe that the number of diﬀerent conﬁgurations Cv = [χ(v), Sv] is upper-

bounded by O(nk), as there cannot be more than (
|N [v]|
k
 ) · k! diﬀerent sets Sv. Thus the following

observation is straightforward.

Observation 3.5.4. Let G = (V, E) be an outerplanar graph and let e = uv ∈ E. The number of
diﬀerent conﬁgurations Ce = [Cu, Cv] is upper-bounded by O(n2k).

46

We can now describe our algorithm, which is based on non-serial dynamic programming. For
the sake of simplicity, let us assume that the weak dual G∗ = (V ∗, E∗) of the outerplanar graph G
is connected. This means that G∗ is a tree. It is well-know that, in general, the weak dual graph of
an outerplanar graph G is a forest [Sys79]. We discuss later how to convert this forest into a tree
as long as G is connected.
Let us root G∗ at an arbitrary dual vertex r ∈ V ∗. Thus, each dual vertex has a unique parent
vertex on the path from the vertex to r. For an edge e = vw ∈ E∗, where v is the parent of w, we
consider the subtree Te rooted at w. Let Ge be the primal subgraph of G whose dual graph is Te.
We deﬁne a window b as the edge or vertex in the primal graph G separating two faces f1, f2.
Observe that b corresponds to an edge e in the dual graph G∗. If f ∗
1 and f ∗
2 are two (dual) vertices
in the dual graph, then the corresponding faces f1 and f2 only have b in common, see Figure 3.7.
Assume that f2 has been conﬂict-free k-colored. Then, to color f1 in a conﬂict-free manner, we
would need all the possible conﬁgurations of the window b allowed by the conﬂict-free coloring of
the face f2. The algorithm performs dynamic programming starting by computing all possible
conﬁgurations of the leaves of G∗ and propagating them towards the root in a compatible manner
(conﬂict-freely).
 r
 f 1 f 2

b

e
 G e

f ∗
1
 f ∗
2

Figure 3.7: Graph construction of faces, windows, and the corresponding dual (sub)graphs. The
shaded are corresponds to already processed faces of G (the past). The face f1 is the face to be
processed next (the present). Edge b is the window between f1 and f2. The rest of the graph
corresponds to faces to be processed in the future.

Let f be a face of G and f ∗ be the corresponding dual vertex in G∗. Let b be the window of f
and let e = b∗ be the dual edge of b connecting f ∗ to its parent p = p(f ∗). For any conﬁguration
Cb, we compute the score S(Cb), which is the number of colored vertices corresponding to Cb in the
conﬂict-free k-coloring of the subgraph Ge. We store the pairs (Cw, S(Cw)
) which are then combined
with the other children of p to compute the compatible conﬁgurations of p. Given a window w of
a face fl, the algorithm GenerateScore computes S(Cw) for a given conﬁguration Cw. Let fl
consist of the edges ⟨e1 = (u1, v1), . . . , eℓ = (uℓ, vℓ)⟩ where, without loss of generality, w = e1 if w is
an edge. Otherwise w = u1 if w is a vertex. Also, let L(ei) be the set of all possible conﬁgurations
of the edge ei. By CS
u1 we denote the number of conﬂict-free neighbors of u1 given the conﬁguration
Cu1, i.e., if Cu1 = (χ(u1), Su1), then CS
u1 = |Su1|. The algorithm populates a family {Pi} of sets
containing pairs of compatible conﬁgurations and their scores. In the algorithm GenerateScore,
δ(Cei, Cei−1) is the number of newly-colored vertices resulting from combining the two compatible
conﬁgurations Cei and Cei−1.

Lemma 3.5.5. For a ﬁxed k ≥ 1, we can compute the scores S(Cb) for all conﬁgurations Cb of all
windows b in O(n4k+1) time.
 47

Algorithm 2 Processing a conﬁguration of a window

1: function GenerateScore(Ce1, f = ⟨e1 = (u1, v1), . . . , eℓ = (uℓ, vℓ)⟩)

2: P1 ← {(Ce1, CS
u1)}

3: for i = 2, . . . , ℓ do

4: Pi ← ∅

5: for (Cei−1, h) ∈ Pi−1 do

6: for Cei ∈ L(ei) do

7: if Cei−1 is compatible with Cei then

8: Pi ← Pi ∪ {(Cei, h + δ(Cei, Cei−1))}

9: S(Ce1) ← ∞

10: for (Ceℓ, h) ∈ Pℓ do

11: if Ceℓ is compatible with Ce1 then

12: S(Ce1) ← min{S(Ce1), h}

Proof. We process the dual graph G∗ starting from the leaves. Let b be the window between the
two faces f1 and f2. The window corresponds to an edge between the a dual vertex and its parent in
the dual graph. Let f1 = ⟨e1 = (u1, v1), . . . , eℓ = (uℓ, vℓ)⟩ such that e1 = b, vℓ = u1, and vi = ui+1
for i ∈ {1, . . . , ℓ − 1}. We compute S(Cb) by applying Algorithm 2. Inductively, we can compute
the score for all conﬁgurations of all windows going up in the dual graph in this manner.
For each window there are at most O(n2k) conﬁgurations. This implies that for each pair of
edges, there are at most O(n4k) pairs of conﬁgurations. As Algorithm 2 considers O(n) pairs of
edges overall, we obtain a running time of O(n4k+1) for the algorithm.

Proof of Theorem 3.5.2. By applying the approach of Algorithm 2 we can compute the scores of
all windows of the graph G. At the root node we have a set of conﬁguration for each window that
results in the minimum number of colored vertices in the whole graph. Such a set can be obtained
by backtracking. Combining this with Observation 3.5.3, we get a conﬂict-free coloring with a
minimal number of colored vertices for the graph G, if and only if χCF (G) ≤ k.

What remains to be discussed is how we treat the case in which G∗ is not a tree but a forest
(assuming G is connected). The dual G∗ becomes disconnected if G has cut edges or cut vertices.
In such a case, we use the following construction depicted in Figure 3.8 to connect the components
of G∗ to obtain a tree.

(1) For a cut vertex v, let ⟨f1, . . . , ft⟩ be the t faces containing v. Let ⟨f ∗
1 , . . . , f ∗
t ⟩ be the cor-
responding vertices in G∗. We make one of f ∗
i a parent to all the others by adding an edge
between them. Note that this does not create a cycle because G is outerplanar.

(2) If we have a cut edge, we consider the cut edge as a face. In this way, for a cut edge, we have
a vertex in the dual graph.

3.5.2 Approximability for Three or More Colors

In § 3.4.2 we stated that every planar graph is conﬂict-free 3-colorable. In this section we deal
with conﬂict-free 3-colorings of planar graphs that, additionally, minimize the number of colored
vertices.

Theorem 3.5.6. Let k ≥ 3 and let G be a planar graph. The following holds:

48

vf 1 f t

: : : : : :
f i
 v w
f 1 f 2

(1) (2)

Figure 3.8: Two cases leading to a forest: (1) a cut vertex, (2) a cut edge.

(1) Unless P = NP, there is no polynomial-time approximation algorithm providing a constant-
factor approximation of γ3
CF (G) for planar graphs. 3-Conflict-Free Dominating Set is
NP-complete for planar graphs.

(2) For k ≥ 4, k-Conflict-Free Dominating Set is NP-complete. Also, γk
CF (G) = γ(G),
and the problem is ﬁxed-parameter tractable with parameter γk
CF (G). Furthermore, there is a
PTAS for γk
CF (G).

(3) If G is outerplanar, then γk
CF (G) = γ(G) and there is a linear-time algorithm to com-
pute γk
CF (G).

The proof of Theorem 3.5.6 is based on the following polynomial-time algorithm, which trans-
forms a dominating set D of a planar graph G into a conﬂict-free k-coloring of G, coloring only
the vertices of D: Let D be a dominating set of a planar graph G. Every vertex v ∈ V (G) \ D is
adjacent to at least one vertex in D. Pick any such vertex u ∈ D and contract the edge uv ∈ E(G)
towards u. Repeat this until only the vertices from D remain. Because G is planar, the graph
G′ = (D, E′) obtained in this way is planar, as G′ is a minor of G. By the 4-coloring theorem, we
can compute a proper 4-coloring of G′.

Lemma 3.5.7. The 4-coloring generated by this procedure induces a conﬂict-free 4-coloring of G.

Proof. Every vertex u ∈ D is a conﬂict-free neighbor to itself as its color does not appear in NG(u).
Let v ∈ V (G) \ D be some uncolored vertex, and let u ∈ D be the vertex that v was contracted
towards by the algorithm. In G′, this contraction made u adjacent to all other vertices in NG(v)∩D,
which guarantees that the color of u is unique in NG(v) ∩ D. As V (G) \ D remains uncolored, the
color of u is thus unique in NG[v].

Proof of Theorem 3.5.6. Proposition (1) follows from Theorem 3.3.7 of § 3.3.3: The reduction
used there preserves planarity and proper planar 3-coloring is NP-complete. For (2), γk
CF (G) =
γ(G) implies NP-hardness in planar graphs because planar minimum dominating set is NP-hard.
Moreover, the coloring algorithm lets us apply any approximation scheme for planar dominating set
to conﬂict-free k-coloring. We obtain a PTAS for the conﬂict-free domination number by applying
our coloring algorithm to the dominating set produced by the PTAS of Baker and Hill [BH94].
Additionally, Alber et al. [AFN04] proved that planar dominating set is FPT with parameter
γ(G), implying that computing the planar conﬂict-free domination number for k ≥ 4 is FPT with
parameter γk
CF (G). For (3), the class of outerplanar graphs is properly 3-colorable in linear time
and closed under taking minors. Kikuno et al. [KYK83] present a linear time algorithm for ﬁnding
a minimum dominating set in a series-parallel graph, which includes outerplanar graphs. The result
follows by combining this linear time algorithm with the coloring algorithm mentioned above, but
using just three colors instead of four.
 49

Figure 3.9: The graph G′ resulting from applying the reduction to K4. This bipartite planar graph
has χO(G′) = 4.

3.6 Open Neighborhoods: Planar Conﬂict-Free Coloring

In this section we discuss the problem of conﬂict-free coloring with open neighborhoods. Recall
that an open-neighborhood conﬂict-free coloring is a coloring of some vertices of a graph G such
that every vertex has a conﬂict-free neighbor in its open neighborhood N (v). In some settings, this
problem is a natural alternative to the closed-neighborhood variant; for instance, when guiding a
robot from one location to another, a uniquely colored beacon at the robot’s current position may
be insuﬃcient.
Note that isolated vertices are problematic for this variant of conﬂict-free coloring; therefore,
in the following, we assume that G does not contain isolated vertices. Moreover, we observe the
following.

Observation 3.6.1. Let G be a graph, v, w ∈ V (G), and deg(v) = 1, deg(w) = 2. Then, for
any number k of colors, in any conﬂict-free k-coloring, the unique neighbor of v must be colored.
Moreover, the two neighbors of w cannot have the same color.

This leads to a straightforward reduction from proper coloring to conﬂict-free coloring. Given
a graph G, adding an otherwise isolated neighbor to each original vertex and placing a vertex
with degree 2 on every original edge yields a graph G′ with χO(G′) = χP (G). See Figure 3.9
for an example of this reduction. The resulting graph G′ is bipartite. Furthermore, the reduction
preserves planarity, implying that bipartite planar graphs may require at least 4 colors in a conﬂict-
free coloring. Moreover, even though this reduction does not necessarily preserve outerplanarity,
applying it to a K3 yields an outerplanar graph that requires at least 3 colors. For bipartite planar
and outerplanar graphs, these bounds are tight.

Corollary 3.6.2. It is NP-complete to decide whether a bipartite planar graph G is open-neighborhood
conﬂict-free 3-colorable.

Theorem 3.6.3. Every bipartite planar graph is open-neighborhood conﬂict-free 4-colorable. For
bipartite outerplanar graphs, three colors are suﬃcient.

Proof. Let G = (V1 ∪ V2, E) be a bipartite planar graph with partitions V1 and V2; the proof
proceeds analogously for outerplanar graphs. We construct two minors G1 and G2 of G, to each
of which we apply the planar four-color theorem. We build G1 by merging all vertices v ∈ V2 into
an arbitrarily chosen neighbor v1(v) ∈ V1. Because G is bipartite and does not contain isolated
vertices, it is possible to continue this process until no vertices from V2 remain. G2 is constructed

50

analogously, merging all vertices v ∈ V1 into an arbitrarily chosen neighbor v2(v) ∈ V2. Each of
the two resulting graphs Gi contains exactly the vertices from Vi. Moreover, as a minor of G, Gi is
planar and therefore has a proper coloring with four colors. We assign the colors from this coloring
to the vertices in Vi.
It remains to show that this induces an open-neighborhood conﬂict-free coloring of G. Let v
be a vertex of G. W.l.o.g., assume v ∈ V1. During the construction of G2, v was merged into its
neighbor v2(v) ∈ V2. Therefore in G2, v2(v) is adjacent to all other neighbors of v in G. Because
all neighbors of v are in V2, this implies that the color of v2(v) is unique in NG(v), and v2(v) is a
conﬂict-free neighbor of v.

On the other hand, for non-bipartite planar graphs, we can show the following upper bound on
the number of colors.

Theorem 3.6.4. Every planar graph has an open-neighborhood conﬂict-free coloring using at most
eight colors.

Proof. Let G = (V, E) be a planar graph. Analogous to the proof of Theorem 3.6.3 we proceed by
producing two minors G1 and G2 of G, to each of which we apply the planar four-color theorem.
However, without the assumption of bipartiteness, we cannot use the same set of four colors for G1
and G2, leading to a conﬂict-free coloring with eight colors.
We start by constructing an independent dominating set V1 of G. Let V2 := V \V1. We construct
the minor Gi of G by contracting each vertex v ∈ V3−i into an arbitrarily chosen neighbor vi(v) ∈ Vi.
Then we apply the planar four-color theorem to G1 and G2 with colors {1, 2, 3, 4} and {5, 6, 7, 8}.
To build a conﬂict-free coloring of G, we assign to each v ∈ Vi its color in the proper coloring of
Gi. This results in a conﬂict-free coloring because v3−i(v) is a conﬂict-free neighbor of v.

Similar to the situation for closed neighborhoods, open neighborhood conﬂict-free coloring is
hard even for k = 1 and k = 2. For closed neighborhoods, a conﬂict-free 1-coloring corresponds to
a dominating set consisting of vertices at pairwise distance at least 3. For open neighborhoods, a
conﬂict-free 1-coloring corresponds to a matching whose vertices form a dominating set and are at
pairwise distance at least 3 (except for those adjacent in the matching).

Theorem 3.6.5. It is NP-complete to decide whether a bipartite planar graph G is open-neighborhood
conﬂict-free 1-colorable.

Proof. We prove hardness using a reduction from Positive Planar 1-in-3-SAT. In a manner
similar to the proof of Theorem 3.4.1, from a positive planar 3-CNF formula φ with clauses C =
{c1, . . . , cl} and variables X = {x1, . . . , xn} and its plane formula graph G(φ), we construct in
polynomial time a bipartite planar graph G′
1(φ) such that φ is 1-in-3-satisﬁable iﬀ χO(G′
1(φ)) = 1.
The graph G′
1(φ) has one variable cycle v0
i · · · v15
i of length 16 for each variable xi. There are exactly
four ways to color a variable cycle; see Figure 3.10. Two of these color v0
i and v8
i ; using one of these
colorings for the variable cycle of xi correspond to setting xi to true. Leaving v0
i and v8
i uncolored
corresponds to setting xi to false. For each clause cj, G′
1(φ) contains a copy of the clause gadget
depicted in Figure 3.10. We can compute an embedding of the formula graph G(φ) in which the
variable vertices are placed on a horizontal line. The clause vertices are embedded above and below
this horizontal line. If a clause cj is embedded below the variables, we connect its black vertex to
vertex v8
i of all variables occurring in cj; otherwise, we use v0
i . An example of this construction is
depicted in Figure 3.11.
If φ is 1-in-3-satisﬁable, coloring the variable cycles according to a satisfying assignment and
the clause gadgets according to Figure 3.10 yields a coloring of G′
1(φ) in which the black vertex

51

v 0
iv 1
iv 2
iv 3
iv 4
iv 5
iv 6
iv 7
iv 8
iv 9
iv 10
iv 11
iv 12
iv 13
iv 14
iv 15
i
 (a) A variable cycle, with a conﬂict-free
1-coloring that corresponds to setting
the variable to true. All conﬂict-free
1-colorings of a variable cycle result
from this coloring by shifting the
groups of colored vertices around the
cycle. The vertices v0
i and v8
i that may
be connected to the clause gadgets are
drawn with a bold outline.
 (b) A clause gadget. The orange
vertices must be colored in any
conﬂict-free 1-coloring. The white
vertices cannot be colored. The black
vertex cannot be colored, but does not
have a conﬂict-free neighbor within the
gadget. It is connected to the variables
occurring in the clause, thus enforcing
that exactly one of them is set to true.

Figure 3.10: Variable and clause gadgets for the reduction.

x 1x 2x 3x 4x 5
 Figure 3.11: The graph G′
1(φ) resulting from applying the reduction to{{x1, x2, x3}, {x1, x2, x5}, {x2, x4, x5}, {x3, x4, x5}}, and an open-neighborhood conﬂict-free
1-coloring (orange vertices) corresponding to setting x1 and x4 to true.

of each clause is adjacent to exactly one colored neighbor. This coloring is an open-neighborhood
conﬂict-free 1-coloring of φ. On the other hand, let G′
1(φ) have an open-neighborhood conﬂict-free
1-coloring χ. In each clause gadget, χ colors exactly the two orange vertices from Figure 3.10.
Therefore, the black vertex of each clause has to be adjacent to exactly one colored variable vertex.
Setting the variables corresponding to variable cycles with colored vertices v0
i and v8
i to true thus
yields a 1-in-3-satisfying assignment for φ.
 52

The same holds for k = 2 colors, but the restriction to bipartite planar graphs requires a slightly
more sophisticated argument.

Theorem 3.6.6. It is NP-complete to decide whether a bipartite planar graph G is open-neighborhood
conﬂict-free 2-colorable.

Proof. Again we prove hardness using a reduction from Positive Planar 1-in-3-SAT. From a
positive planar 3-CNF formula φ with clauses C = {c1, . . . , cl} and variables X = {x1, . . . , xn}
and its plane formula graph G(φ), we construct in polynomial time a bipartite planar graph G′
2(φ)
such that φ is 1-in-3-satisﬁable iﬀ χO(G′
2(φ)) ≤ 2. The graph G′
2(φ) has a variable path v1
i v2
i v3
i of
length 3 for each variable xi. For each clause cj, there is a clause gadget as depicted in Figure 3.12;
this gadget contains a distinguished clause vertex. The gadget prevents the clause vertex from
being colored and cannot be used to provide a conﬂict-free neighbor to the clause vertex. We
connect vertex v1
i to the clause vertex of cj with an edge iﬀ xi occurs in cj; the other vertices of
clause gadgets and variable gadgets are not connected to any vertex outside their respective gadget.
Therefore, variable vertex v1
i can provide a conﬂict-free neighbor to the clause vertex of cj iﬀ xi
occurs in cj.
We still have to enforce that the color of the conﬂict-free neighbor of the clause vertex is the
same for all clauses. To this end, we connect the clause vertices using the equality gadget depicted
in Figure 3.13. This gadget ensures that the conﬂict-free neighbors of the two clause vertices
connected by it have the same color in any conﬂict-free 2-coloring. We cannot add this gadget
between all pairs of clause vertices because this would destroy planarity. Instead, we compute a
spanning tree T on the clause vertices that could be added to G′
2(φ), preserving planarity. Then,
for each edge cacb of T , we add a copy of the equality gadget to G′
2(φ), using it to connect the
clause vertices ca and cb. Because adding the edges of T preserves planarity, the graph resulting
from adding the gadgets is planar as well. Moreover, because the equality gadget works transitively
and T is connected, the conﬂict-free neighbors of all clause vertices must receive the same color in
any conﬂict-free 2-coloring.
It remains to prove that such a T always exists. For this purpose, consider the plane formula
graph G(φ), including the backbone of the formula. Because only one vertex of each variable
or clause gadget is connected to vertices outside the gadget, these gadgets do not inﬂuence the
planarity of G′
2(φ). Therefore, if adding T preserves the planarity of G(φ), it also preserves the
planarity of G′
2(φ). As root of T , we choose an arbitrary clause vertex r on the boundary of the
unbounded face of G(φ). We add an edge from r to all other clause vertices on the boundary of the
unbounded face to T . Now we consider the connected component R of r in T . Either R = V (T ),
in which case we are done, or there must be a vertex v ∈ R that lies on a face whose boundary
contains a vertex w /∈ R. For each such vertex v, we add an edge to all such vertices w /∈ R. We
iterate this procedure until we are done.
Let φ be 1-in-3-satisﬁable and let Γ be the set of true variables in a 1-in-3-satisfying assignment
of φ. We construct a conﬂict-free 2-coloring of G′
2(φ) by assigning color 1 to v1
i and v2
i for all
xi ∈ Γ and to v3
i and v2
i for xi /∈ Γ. The vertices in equality gadgets that are adjacent to clause
vertices receive color 2. All other vertices in the gadgets are colored as sketched in Figures 3.12
and 3.13. All clause vertices are adjacent to exactly one variable vertex carrying color 1 and thus
have a conﬂict-free neighbor. Therefore, the coloring constructed in this way is a valid conﬂict-free
2-coloring.
Now assume that G′
2(φ) has a conﬂict-free 2-coloring χ. By the argument above, the conﬂict-
free neighbor of each clause vertex is a variable vertex v1
i . Moreover, all clause vertices have a
conﬂict-free neighbor of the same color; w.l.o.g., color 1. Therefore, each clause vertex is adjacent

53

c
 Figure 3.12: The bipartite clause gadget with clause vertex c; the components of the bipartition
are indicated using squares and circles. Gray vertices cannot receive a color. Vertices colored green
or orange must be colored. Except for automorphisms and swapping colors, orange vertices have
to receive color 1 and green vertices have to receive color 2. White vertices may be colored or may
remain uncolored; it is straightforward to extend the depicted coloring to a conﬂict-free 2-coloring
of the gadget (except for c) by coloring the white vertices of degree 1. By construction, one of c’s
neighbors has three neighbors of color 1 and a conﬂict-free neighbor of color 2 (and vice versa for
c’s other neighbor). In total, the gadget guarantees that c remains uncolored and cannot have a
colored neighbor within the gadget.

ab
 Figure 3.13: The equality gadget that can be used to connect two terminal vertices (marked a and
b) in the same partition of a bipartite graph. It adds two occurrences of the same color to the
neighborhoods of a and b, thereby forcing the conﬂict-free neighbor of a and b to have the same
color.

to exactly one variable vertex with color 1, and the set of variables xi where χ(v1
i ) = 1 induces a
satisfying assignment of φ.
 54

3.7 Conclusion

A spectrum of open questions remain. Many of them are related to general graphs, in particular
with our suﬃcient condition for general graphs. For every k ≥ 2, Gk+1 provides an example that
excluding Kk+2 as a minor is not suﬃcient to guarantee k-colorability. However, for k ≥ 2 we have
no example where excluding K−3
k+3 as a minor does not suﬃce.
With respect to open-neighborhood conﬂict-free coloring, several open questions remain. Are
four colors always suﬃcient for general planar graphs? Are three colors always suﬃcient for outer-
planar graphs?
Another variant of our problem arises from requiring that all vertices must be colored. It is
clear that one extra color suﬃces for this purpose; however, it is not always clear that this is
also necessary, in particular, for planar graphs. Adapting our argument to this situation does not
seem straightforward, especially because there are outerplanar graphs requiring three colors in this
setting.
In addition, there is a large set of questions related to geometric versions of the problem. What
is the worst-case number of colors for straight-line visibility graphs within simple polygons? It
is conceivable that Θ(log log n) is the right answer, just like for rectangular visibility, but this
is still an open problem, just like complexity and approximation. Other questions arise from
considering geometric intersection graphs, such as unit-disk intersection graphs, for which necessary
and suﬃcient conditions, just like upper and lower bounds, would be quite interesting.

55

Bibliography

[AAG+18] Zachary Abel, Victor Alvarez, Aman Gour, Adam Hesterberg, Erik D. Demaine,
S´andor P. Fekete, Phillip Keldenich, and Christian Scheﬀer. Three colors suf-
ﬁce: Conﬂict-free coloring of planar graphs. Proceeedings of the Twenty-Eighth
Annual ACM-SIAM Symposium on Discrete Algorithms (SODA 2017), 2018. doi
10.1137/1.9781611974782.127.

[AdBP08] Mohammad Ali Abam, Mark de Berg, and Sheung-Hung Poon. Fault-tolerant conﬂict-
free colorings. In Proc. 20th Canadian Conference on Computational Geometry
(CCCG’08), pages 13–16, 2008.

[ADK15] Pradeesha Ashok, Aditi Dudeja, and Sudeshna Kolay. Exact and FPT algorithms for
max-conﬂict free coloring in hypergraphs. In Proc. 26th International Symposium on
Algorithms and Computation, pages 271–282, 2015.

[AEGR07] Deepak Ajwani, Khaled Elbassioni, Sathish Govindarajan, and Saurabh Ray. Conﬂict-
free coloring for rectangle ranges using O(n.382) colors. In SPAA ’07: Proc. 19th ACM
Symposium on Parallelism in Algorithms and Architectures, pages 181–187, 2007.

[AFN04] Jochen Alber, Michael R Fellows, and Rolf Niedermeier. Polynomial-time data reduc-
tion for dominating set. Journal of the ACM, 51(3):363–384, 2004.

[AH77a] K. Appel and W. Haken. Every planar map is four colorable. Part I. Discharging.
Illinois J. Math., 21:429–490, 1977.

[AH77b] K. Appel and W. Haken. Every planar map is four colorable. Part II. Reducibility.
Illinois J. Math., 21:491–567, 1977.

[AS06] Noga Alon and Shakhar Smorodinsky. Conﬂict-free colorings of shallow discs. In Proc.
22nd Annual Symposium on Computational Geometry, pages 41–43. ACM, 2006.

[Bal78] Hans Werner Ballmann. Der Satz von Lusternik und Schnirelmann. Bonner Mathe-
matische Schriften, 102:1–25, 1978.

[BH94] Brenda S. Baker. and Murray Hill. Approximation algorithms for NP-complete prob-
lems on planar graphs. Journal of the ACM, 41(1):153–180, 1994.

[BNCOS10] Amotz Bar-Noy, Panagiotis Cheilaris, Svetlana Olonetsky, and Shakhar Smorodin-
sky. Online conﬂict-free colouring for hypergraphs. Combinatorics, Probability and
Computing, 19(04):493–516, 2010.

[CFK+07] K. Chen, A. Fiat, H. Kaplan, M. Levy, J. Matousek, E. Mossel, J. Pach, M. Sharir,
S. Smorodinsky, U. Wagner, and E. Welzl. Online conﬂict-free coloring for intervals.
SIAM J. Computing, 36:1342–1359, 2007.

56

[CGRS14] Panagiotis Cheilaris, Luisa Gargano, Adele A Rescigno, and Shakhar Smorodinsky.
Strong conﬂict-free coloring for intervals. Algorithmica, 70(4):732–749, 2014.

[CSS11] Panagiotis Cheilaris, Shakhar Smorodinsky, and Marek Sulovsky. The potential to
improve the choice: list conﬂict-free coloring for geometric hypergraphs. In Proc. 27th
Annual Symposium on Computational Geometry, pages 424–432. ACM, 2011.

[CT11] Panagiotis Cheilaris and G´eza T´oth. Graph unique-maximum and conﬂict-free color-
ings. Journal of Discrete Algorithms, 9(3):241–251, 2011.

[DO07] Erik D. Demaine and Joseph O’Rourke. Reducibility among combinatorial prob-
lems. In Geometric Folding Algorithms: Linkages, Origami, Polyhedra, chapter 24
Geodesics: Lyusternik-Schnirelmann, pages 372–375. Cambridge University Press,
Cambridge, 2007.

[ELRS03] G. Even, Z. Lotker, D. Ron, and S. Smorodinsky. Conﬂict-free colorings of simple ge-
ometric regions with applications to frequency assignment in cellular networks. SIAM
Journal on Computing, 33(1):94–136, 2003.

[EM06] Khaled Elbassioni and Nabil H Mustafa. Conﬂict-free colorings of rectangles ranges.
In Annual Symposium on Theoretical Aspects of Computer Science, pages 254–263.
Springer, 2006.

[Gar65] Martin Gardner. Letters. Scientiﬁc American, 213(5):10–12, November 1965. Repro-
duced in [Gar90].

[Gar90] Martin Gardner. Mathematical Carnival. Penguin Books, London, 1990.

[GR15] Luisa Gargano and Adele A. Rescigno. Complexity of conﬂict-free colorings of graphs.
Theoretical Computer Science, 566:39–49, 2015.

[GST14] Roman Glebov, Tibor Szab´o, and G´abor Tardos. Conﬂict-free coloring of graphs.
Combinatorics, Probability and Computing, 23:434–448, 2014.

[Guy61] Richard K. Guy. The jewel thief. NABLA, 8:149–150, September 1961.

[Had43] Hugo Hadwiger. ¨Uber eine Klassiﬁkation der Streckenkomplexe. Vierteljschr. Natur-
forsch. Ges. Z¨urich, 88:133–143, 1943.

[HKS10] Elad Horev, Roi Krakovski, and Shakhar Smorodinsky. Conﬂict-free coloring made
stronger. In Proc. 12th Scandinavian Symposium and Workshop on Algorithm Theory,
volume 6139, pages 105–117, 2010.

[HKS+15] Frank Hoﬀmann, Klaus Kriegel, Subhash Suri, Kevin Verbeek, and Max Willert. Tight
bounds for conﬂict-free chromatic guarding of orthogonal art galleries. In 31st Interna-
tional Symposium on Computational Geometry, volume 34 of LIPIcs, pages 421–435,
2015.

[HPS05] Sariel Har-Peled and Shakhar Smorodinsky. Conﬂict-free coloring of points and simple
regions in the plane. Discrete & Computational Geometry, 34(1):47–70, 2005.

[Kar72] Richard Karp. Reducibility among combinatorial problems. In R. E. Miller, J. W.
Thatcher, J. D., and Bohlinger, editors, Complexity of Computer Computations, pages
85–103. Springer, Boston, 1972.
 57

[KYK83] Tohru Kikuno, Noriyoshi Yoshida, and Yoshiaki Kakuda. A linear algorithm for the
domination number of a series-parallel graph. Discrete Applied Mathematics, 1983.

[Lic82] David Lichtenstein. Planar formulae and their uses. SIAM Journal on Computing,
11(2):329–343, 1982.

[LS29] Lazar Lyusternik and Lev Schnirelmann. Sur le probl´eme de trois g´eod´esiques ferm´ees
sur les surfaces de genre 0. Comptes Rendus de l’Acad´emie des Sciences de Paris,
189:269–271, 1929.

[LTP09] Nissan Lev-Tov and David Peleg. Conﬂict-free coloring of unit disks. Discrete Applied
Mathematics, 157(7):1521–1532, 2009.

[MR08] Wolfgang Mulzer and G¨unter Rote. Minimum-weight triangulation is NP-hard. Jour-
nal of the ACM, 55(2):11, 2008.

[O’B61] Thomas H. O’Beirne. Christmas puzzles and paradoxes. The New Scientist, 266:753,
December 1961.

[O’R18] Joseph O’Rourke. Personal communication, 2018. Alluded to in [DO07].

[Pog73] Aleksej Vasilevich Pogorelov. Extrinsic Geometry of Convex Surfaces. 1973.

[Poi05] Henri Poincar´e. Sur les lignes g´eod´esiques des surfaces convexes. Transactions of the
American Mathematical Society, 6(3):237–274, 1905.

[PT09] J. Pach and G. T´ardos. Conﬂict-free colourings of graphs and hypergraphs. Combi-
natorics, Probability and Computing, 18(05):819–834, September 2009.

[RSST97] N. Robertson, D. Sanders, P. Seymour, and R. Thomas. The four-colour theorem. J.
Combinatorial Theory Series B, 70:2–44, 1997.

[Smo03] S. Smorodinsky. Combinatorial Problems in Computational Geometry. PhD thesis,
School of Computer Science, Tel-Aviv University, 2003.

[Sys79] Maciej M. Sys lo. Characterizations of outerplanar graphs. Discrete Mathematics,
26:47–53, 1979.

[Wil13] R. Wilson. Four colours suﬃce: How the map problem was solved. Princeton University
Press, 2013.
 58
