<!-- source: https://arxiv.org/pdf/2107.00076 | converted from PDF -->

arXiv:2107.00076v2  [math.CO]  8 Sep 2022
Strongly regular graphs satisfying the 4-vertex
condition

A. E. Brouwer1 & F. Ihringer2 & W. M. Kantor1

30 Jun 2021

Abstract

We survey the area of strongly regular graphs satisfying the 4-vertex
condition and ﬁnd several new families. We describe a switching operation
on collinearity graphs of polar spaces that produces cospectral graphs.
The obtained graphs satisfy the 4-vertex condition if the original graph
belongs to a symplectic polar space.

1 Introduction

In this note we look at graphs with high combinatorial regularity, where this
regularity is not an obvious consequence of properties of their group of auto-
morphisms.
A graph Γ is said to satisfy the t-vertex condition if, for all triples (T, x0, y0)
consisting of a t-vertex graph T together with two distinct distinguished vertices
x0, y0 of T , and all pairs of distinct vertices x, y of Γ, the number of isomorphic
copies of T in Γ, where the isomorphism maps x0 to x and y0 to y, does not
depend on the choice of the pair x, y but only on whether x, y are adjacent or
nonadjacent.
This concept was introduced by Hestenes & Higman [13] (who refer to the
unpublished Sims [32]) in order to study rank 3 graphs. Clearly, a rank 3 graph
satisﬁes the t-vertex condition for all t. If the graph Γ satisﬁes the t-vertex
condition, where Γ has v vertices and 3 ≤ t ≤ v, then Γ also satisﬁes the (t − 1)-
vertex condition. A graph satisﬁes the 3-vertex condition if and only if it is
strongly regular (or complete or edgeless). It satisﬁes the v-vertex condition if
and only if it is rank 3. Thus, we get a hierarchy of conditions of increasing
strength between strongly regular and rank 3.
The present paper will focus almost exclusively on the case t = 4. A simple
criterion for the 4-vertex condition is given in Proposition 2.1. Previously not
many graphs were known that satisfy the 4-vertex condition without being rank
3. Here we survey the known examples and give several new constructions. One
of our constructions proceeds by switching symplectic graphs (see Section 7).
As a consequence we ﬁnd

1Retired
2Dept. of Mathematics: Analysis, Logic and Discrete Math., Ghent University, Belgium.
E-mail: ferdinand.ihringer@ugent.be
 1

Theorem 1.1 For v ≥ 4 there are at least ⌊v1/6⌋! strongly regular graphs of
order at most v satisfying the 4-vertex condition.

It follows that among all non-isomorphic strongly regular graphs of order at
most v that satisfy the 4-vertex condition the fraction that is determined by
their spectrum goes to 0 when v goes to inﬁnity.

2 The 4-vertex condition

A graph of order v is called strongly regular with parameters (v, k, λ, µ) if it is neither complete
nor edgeless, each vertex has degree k, any two adjacent vertices have exactly λ common
neighbors, and any two non-adjacent vertices have exactly µ common neighbors.
A graph with vertex set V has rank r if its automorphism group is transitive on V and
has exactly r orbits on V × V . Rank 3 graphs are strongly regular.
If x is a vertex of the graph Γ, then the local graph Γ(x) of Γ at x is the induced subgraph
in Γ on the neighborhood of x. We say that Γ is locally P when all local graphs of Γ have
property P. If Γ is strongly regular, then its 1st subconstituent (at a vertex x) is the local graph
at x, while its 2nd subconstituent (at x) is the induced subgraph on the non-neighborhood of
x. If xy is an edge (resp. nonedge) in Γ, then the subgraph induced on Γ(x) ∩ Γ(y) is called
a λ-graph (resp. µ-graph).
See [6] for further information about strongly regular graphs.

Details on the parameters of graphs satisfying the 4-vertex condition are
given in [13]. In particular, we have the following simple criterion for the 4-
vertex condition:

Proposition 2.1 (Sims [32]) A strongly regular graph Γ with parameters (v, k,
λ, µ) satisﬁes the 4-vertex condition, with parameters (α, β), if and only if the
number of edges in Γ(x) ∩ Γ(y) is α (resp. β) whenever the vertices x, y are
adjacent (resp. nonadjacent). In this case, k((
λ
2) − α
) = β(v − k − 1).

The equality here follows by counting 4-cliques minus an edge.
It immediately follows that the collinearity graph of a generalized quadrangle
(cf. [28]) or partial quadrangle (cf. [7]) satisﬁes the 4-vertex condition (with
α = (
λ
2) and β = 0). The same holds for a graph Γ with λ ≤ 1.
If Γ is locally strongly regular, say with local parameters (v′, k′, λ
′, µ′) (where
clearly v′ = k and k′ = λ), then Γ(x) ∩ Γ(y) has valency λ
′ (resp. µ′) when
x ∼ y (resp. x ̸∼ y) so that Γ satisﬁes the 4-vertex condition with α = λλ
′/2
and β = µµ′/2.

2.1 A few rank 4 examples

Below we give a small table with the parameters of some edge-transitive rank
4 graphs satisfying the 4-vertex condition. Except for the example with group
HJ.2 due to Reichard [30], these do not seem to have been noticed in print.

v k λ µ λ′ µ′ α β group name ref
144 55 22 20 - 9 87 90 M12.2
280 36 8 4 - 2 1 4 HJ.2 [30]
300 104 28 40 - 8 78 160 PGO5(5) N O−
5 (5) §6
325 144 68 60 - 30 1153 900 PGO5(5) N O+
5 (5) §6
512 196 60 84 14 20 420 840 29.ΓL3(8) dual hyperoval §4
729 112 1 20 0 0 0 0 36.2.L3(4).2 Games graph [5]
1120 729 468 486 297 306 69498 74358 PSp6(3).2 disj. t.i. planes §5
1849 462 131 110 - - 2980 1845 432:(42×D22) power diﬀ. set §3.6

2

The numbers λ
′, µ′ give the valency of the λ- and µ-graphs in case these are
regular (and then α = λλ
′/2 and β = µµ′/2).

The examples on 144 and 729 vertices also satisfy the 5-vertex condition.

2.2 Strongly regular graphs with strongly regular subcon-
stituents

As we saw, graphs that are locally strongly regular satisfy the 4-vertex condition.
Sometimes it follows that also the 2nd subconstituents must be strongly regular.

Lemma 2.2 Suppose that a strongly regular graph with parameters (v, k, λ, µ) =
(4t2, 2t2 − εt, t2 − εt, t2 − εt) (where ε = ±1) has ﬁrst subconstituents that are
strongly regular with parameters (v′, k′, λ
′, µ′) = (
2t2 −εt, t2 −εt, 1
2 t(t−ε), t( 1
2 t−
ε)
)
. Then its second subconstituents are strongly regular with parameters (v′′, k′′,
λ
′′, µ′′) = (
2t2 + εt − 1, t2, 1
2 t(t − ε), 1
2 t2)
.

More generally, the spectrum of the 2nd subconstituent at any vertex of a strongly regular
graph follows from that of the 1st subconstituent—see [8], Theorem 5.1.

Call the three parameter sets in the above lemma A(εt), B(εt), and C(εt),
respectively. They occur again in §3.3. The parameter sets A(t) and A(−t)
are known as (negative) Latin square parameters LSt(2t) (resp. NLt(2t)). The
complementary graphs have parameters LSt+1(2t) (resp. NLt−1(2t)).

Cameron, Goethals & Seidel [8] studied the situation of a primitive strongly
regular graph such that, for some vertex, both subconstituents are strongly
regular, and found that such a graph either has a vanishing Krein parameter
q1
11 or q2
22, or has Latin square or negative Latin square parameters. They
conjectured that every non-grid example of the latter has parameters as in the
above lemma or has a complement with these parameters.

3 Survey of the known examples and results

3.1 Complements

A graph satisﬁes the t-vertex condition if and only if its complement does.

3.2 Generalized quadrangles

Higman [14] observed that the collinearity graphs of generalized quadrangles
satisfy the 4-vertex condition (and there are many examples that are not rank 3,
cf. [23]).

More generally the 4-vertex condition holds for partial quadrangles. For example, the Hill
graph with parameters (v, k, λ, µ) = (4096, 234, 2, 14) (derived from the cap constructed in
[15]) has a rank 10 group and satisﬁes the 4-vertex condition with α = 1, β = 0.

Reichard [31] showed that the collinearity graphs of generalized quadrangles
satisfy the 5-vertex condition, and that the collinearity graphs of generalized
quadrangles GQ(s, s2) satisfy the 7-vertex condition.

More generally the 5-vertex condition holds for partial quadrangles.

3

3.3 Binary vector spaces with a quadratic form

The ﬁrst non-rank-3 graph satisfying the 5-vertex condition was constructed by
A. V. Ivanov [21]: a strongly regular graph Γ0 whose subconstituents Γ1, Γ2
satisfy the 4-vertex condition. The parameters are as follows.
v k λ µ α β |G| remarks
Γ0 256 120 56 56 784 672 220 · 32 · 5 · 7 rank 4: 1 + 120 + 120 + 15
Γ1 120 56 28 24 216 144 212 · 32 · 5 · 7 rank 4: 1 + 56 + 56 + 7
Γ2 135 64 28 32 168 192 212 · 32 · 5 · 7 intransitive: 120 + 15

In [4] an inﬁnite family of graphs Γ(m) (m ≥ 1) is constructed by taking as
vertex set F 2m
2 , where vectors are adjacent when the line joining them meets the
hyperplane at inﬁnity in a ﬁxed hyperbolic quadric minus a maximal t.i. sub-
space. The graphs Γ(m) have parameters A(2m−1) (see §2.2). They have a rank
4 group (for m ≥ 4) and satisfy the 4-vertex condition.
The local graphs ∆
(m) are strongly regular with parameters B(2m−1). They
have a rank 4 group (for m ≥ 4) and satisfy the 4-vertex condition.
By Lemma 2.2 also the 2nd subconstituents E(m) are strongly regular, with
parameters C(2m−1).
We checked by computer that the graph Γ(4) is isomorphic to the above Γ0.

In [30] it is shown that the graphs Γ(m) satisfy the 5-vertex condition.
In [29] it is shown that the graphs Γ(m) are triplewise 5-regular, a.k.a. (3,5)-regular,
where (s, t)-regularity is the analog of the t-vertex condition where s instead of two vertices
are distinguished. It follows that the 2nd subconstituents E(m) of the graphs Γ(m) also satisfy
the 4-vertex condition.

In [22], two inﬁnite families of graphs are constructed. One is the above
Γ(m). The second family has members Σ(m) with vertex set F 2m
2 , where vectors
are adjacent when the line joining them hits the hyperplane at inﬁnity either
in a ﬁxed elliptic quadric minus a maximal t.i. subspace S or in S⊥\S. The
graphs Σ(m) have parameters A(−2m−1), have rank 5 (for m ≥ 5), and satisfy
the 4-vertex condition.
Let Γ(V, X) be the graph on a vector space V where two vectors are adjacent precisely
when the joining line hits the subset X of the hyperplane P V at inﬁnity. Since Γ(V, X) is
strongly regular if and only if X is a 2-character set ([11]), that is, if and only if |X ∩ H| takes
only two distinct values when H runs through the hyperplanes of P V , the set (Q\S)∪(S⊥ \S)
is a 2-character set when Q is an elliptic quadric, and S a maximal t.i. subspace.
Let V be a vector space over F2. Then the local graph of Γ(V, X) is the collinearity graph
of the partial linear space with point set X and whose lines are the projective lines (of size 3)
contained in X.
The local graphs T(m) are strongly regular with parameters B(−2m−1).
They are intransitive (for m ≥ 5).
It follows from Lemma 2.2 that also the 2nd subconstituents Υ(m) are strongly
regular, with parameters C(−2m−1). There is a tower of graphs here: If Υ is
the 2nd subconstituent of Σ(m) at a vertex x, and s ∈ S, then the local graph
of Υ at its vertex x + s is isomorphic to Σ(m−1). (For a proof, see Appendix A.)

In [22] it is conjectured that the graphs Σ(m) satisfy the 5-vertex condition, and that the
graphs T(m) and Υ(m) satisfy the 4-vertex condition. The former was proved in [30]. The
latter is proved in Appendix A. In [29] it is announced that Σ(m) is even (3, 5)-regular, but
we are not aware of a proof in print.

3.4 Block graphs of Steiner triple systems

Higman [14] investigated for which v-point Steiner triple systems the block graph
satisﬁes the 4-vertex condition. He found that either the system is a projective

4

space PG(m, 2) or v is one of 9, 13, 25. In [25] the cases 13 and 25 are ruled
out, so that the only other example is the aﬃne plane AG(2, 3). The examples
are rank 3.

3.5 Smallest example

In [26] it is shown that the smallest non-rank-3 strongly regular graphs satisfying
the 4-vertex condition have v = 36 vertices. There are three examples. All have
(v, k, λ, µ) = (36, 14, 4, 6) and α = 0, β = 4.

3.6 Cyclotomic examples

Given (q, e, J), where e | (q − 1)/2 and J is a set of nonnegative integers, and a
ﬁxed primitive element η of Fq, consider the cyclotomic graph with vertex set
Fq, where two elements are adjacent when their diﬀerence is in D = {ηie+j |
0 ≤ i < (q − 1)/e, j ∈ J}. In some cases this yields a strongly regular graph
that satisﬁes the 4-vertex condition. We give a few examples. The examples on
112 and 232 vertices are due to Klin & Pech [27].

q pf e J η α β rk
1849 432 4 {0} any 2980 1845 4
146689 3832 4 {0} any 11353825 10662960 4
121 112 6 {0, 1, 2} any 200 206 5
625 54 6 {0, 1, 2} any 5913 6022 5
5041 712 6 {0, 1, 2} any 395641 396270 5
529 232 8 {0, 1, 2, 3} η2 = η + 4 4215 4300 5

In all cases q = pf where p is semiprimitive mod e (that is, e | (pi + 1) for
some i), so that the parameters of the strongly regular graph can be found in
[6, Thm. 7.3.2].

4 Graphs from hyperovals

In [17], Huang, Huang & Lin constructed various families of graphs. The
complement of one of them can be described as follows ([2]). For q = 2m,
take F 3
q as the vertex set of Γ. Let π be the plane at inﬁnity of F 3
q . Let H ∗

be a dual hyperoval of π (that is, a set of q + 2 lines, no three on a point).
The plane π is partitioned into two parts, 1
2 (q + 1)(q + 2) points on two lines
of H ∗ and 1
2 q(q − 1) exterior points on no line of H ∗. Two vertices of Γ are
adjacent when the line joining them hits π in one of the exterior points. Then
Γ is strongly regular and has parameters

(v, k, λ, µ) = (
q3, 1
2 q(q − 1)
2, 1
4 q(q − 2)(q − 3), 1
4 q(q − 1)(q − 2)
)
.

Its local graphs are strongly regular with parameters
( 1
2 q(q − 1)
2, 1
4 q(q − 2)(q − 3), 1
8 q(q2 − 9q + 22), 1
8 q(q − 3)(q − 4)
)
.

Hence, as noted in Section 2, Γ satisﬁes the 4-vertex condition. If m = 3, then
Γ has rank 4.
 5

5 Disjoint t.i. planes in symplectic 6-space

Let V be a 6-dimensional vector space over Fq, provided with a nondegenerate
symplectic form. Let Γ be the graph with as vertices the totally isotropic planes,
adjacent when disjoint.

Proposition 5.1 The graph Γ is strongly regular, with parameters v = (q3 +
1)(q2 + 1)(q + 1), k = q6, λ = q2(q3 − 1)(q − 1), µ = (q − 1)q5. If q is even,
then Γ is rank 3, otherwise rank 4. Its local graph ∆ is strongly regular with
parameters v′ = k, k′ = λ, λ
′ = µ′ − q2(q − 2) and µ′ = q2(q − 1)(q3 − q2 − 1).
It follows that Γ satisﬁes the 4-vertex condition.

For convenience, we give the parameters of ¯∆, the complement of ∆:
¯v = q6, ¯k = (q2 + 1)(q3 − 1), ¯λ = q4 + q3 − q2 − 2, ¯µ = q4 + q2.

Proof. The dual polar graph Σ belonging to Sp6(q) is distance-regular of diameter 3 and has
eigenvalue −1. It follows that its distance-3 graph Γ is strongly regular (see [3], Prop. 4.2.17).
More generally, the distance 1-or-2 graph of the symplectic dual polar space Sp2m(q) is
distance-regular (cf. [3], Prop. 9.4.10). For m = 3 it is the complement of Γ.
For any vertex x, the subgraph induced by Σ on Σ3(x) is isomorphic to the symmetric
bilinear forms graph on F 3
q (see [3], Prop. 9.5.10). If q is odd, then distance j (j = 0, 1, 2, 3)
in Σ3(x) corresponds to rk(f − g) = j in the symmetric bilinear forms graph and hence to
distance ⌊(j + 1)/2⌋ in the quadratic forms graph (see [3], §9.6). It follows that ∆ is the
complement of the quadratic forms graph, and has parameters as claimed.
If q is even, then Γ is rank 3 (by triality, it is the complement of the O+
8 (q) polar graph),
and ∆ is the complement of the rank 3 graph V O+
6 (q), with parameters as claimed. ✷

6 Nonsingular points joined by a tangent

Let V be a vector space of dimension 2m + 1 over Fq with q odd, and let Q be
a nondegenerate quadratic form on V . We also use Q as the symbol for the set
of singular projective points.
The projective space P V has (q2m+1 − 1)/(q − 1) points, (q2m − 1)/(q − 1)
singular, and q2m nonsingular. The nonsingular points come in two types: there
are 1
2 qm(qm + ε) points of type ε (where ε = ±1), with ε = +1 (resp. −1) for
points x for which x
⊥, the hyperplane of points orthogonal to x, is hyperbolic
(resp. elliptic).
Consider the graph N Oε
2m+1(q) that has as vertex set the set of nonsingular
points of type ε, where two points are adjacent when the joining line is a tangent.

Proposition 6.1 (Wilbrink [34], cf. [5]) Let m ≥ 2. The graph N Oε
2m+1(q) is
strongly regular with parameters v = 1
2 qm(qm + ε), k = (qm−1 + ε)(qm − ε),
λ = 2(q2m−2 − 1) + εqm−1(q − 1), µ = 2qm−1(qm−1 + ε).

For m = 1, ε = −1 the graph is edgeless. For m = 1, ε = 1 we have the
triangular graph T (q + 1). Wilbrink also handled the case of even q. We give
an explicit proof here; for a diﬀerent and more general proof see [1].

Proof. The neighbors of a vertex x lie on the tangents joining x with a singular point of
x⊥, and x⊥ has (qm−1 + ε)(qm − ε)/(q − 1) singular points. This gives the value of k.
A common neighbor z of two adjacent vertices x, y lies on the line xy (and there are q − 2
choices) or on some other tangent T on x. In the latter case the plane ⟨x, y, z⟩ meets Q in
a conic or double line. If it is a conic, then z is uniquely determined on T by the fact that
yz is the tangent on y other than xy. If it is a double line, then each nonsingular point of
T \ {x} is suitable. Let p be the singular point on xy. Then {p, x}⊥/⟨p⟩ is a nondegenerate

6

(2m − 2)-space of type ε, and has a = (qm−2 + ε)(qm−1 − ε)/(q − 1) singular points. It follows
that xy is in a planes that hit Q in a double line, and in q2m−2 planes that hit Q in a conic.
Consequently, λ = q − 2 + q2m−2 + (q − 1)qa, as desired.
A common neighbor z of two nonadjacent vertices x, y determines a nondegenerate plane
π = ⟨x, y, z⟩ in which xz and yz are tangents, so that x, y, z are exterior points. Now x, y are
on two tangents each, and π contains 4 common neighbors of x, y. If Q is a quadratic form
on a (2m + 1)-space, then a point p is exterior if and only if (−1)m det(Q) Q(p) is a nonzero
square. In order to have p exterior in π but a ε-point in V , the (2m − 2)-space π⊥ must be
an ε-subspace of the (2m − 1)-space {x, y}⊥. Since there are b = 1
2 qm−1(qm−1 + ε) such
ε-subspaces, we ﬁnd µ = 4b, as desired. ✷

The automorphism group PΓO2m+1(q) of the graph contains PGO2m+1(q).
The latter has (q + 3)/2 orbits on pairs of vertices [1]. Hence, the graph has
rank (q + 3)/2 if q is prime.
For m = 2, ε = −1, this is the collinearity graph of a semi-partial geometry
found by Metz. Its lines have size s + 1 = q and there are t + 1 = q2 + 1 lines
on each point. Each point outside a line has either 0 or α = 2 neighbors on the
line. See Debroey [9], voorbeeld 1.1.3d, and Debroey-Thas [10], example 1.4d,
and Hirschfeld-Thas [16], p. 268, and Brouwer-van Lint [5], §7A, and Brouwer-
Van Maldeghem §8.7, example (ix).
For m = 2, ε = +1 this is the collinearity graph of a geometry with t + 1 =
(q + 1)
2 lines of size s + 1 = q on each point, such that each point outside a line
has 0, 2, or q neighbors on the line ([5], §7B).

We shall prove that these graphs satisfy the 4-vertex condition. First a
lemma.

Lemma 6.2 Let S be a solid such that Q∣
∣
S is nondegenerate. Let x, y, z be
distinct nonsingular points of the same type ε such that ⟨z, x⟩ and ⟨z, y⟩ are
tangents and ⟨x, y⟩ is nondegenerate. Put π = ⟨x, y, z⟩. Then there are either 0
or 2 nonsingular points w ∈ S \ π of type ε such that ⟨x, w⟩, ⟨y, w⟩, and ⟨z, w⟩
are tangents. For x, y, z given, the number of w only depends on the type of S.
It equals 2 if and only if the nonzero number 2( B(z,z)B(x,y)
B(x,z)B(y,z) − 1) det(Q∣
∣
S) is a
square.

Proof.
Replace x by B(z,z)
B(x,z) x and y by B(z,z)
B(y,z) y. Then B(x, z) = B(z, z) = B(y, z).
Put x0 = x−z, y0 = y −z, w0 = w−z, then B(x0, z) = B(y0, z) = B(w0, z) = 0.
Since the lines ⟨z, x⟩, ⟨z, y⟩, and ⟨z, w⟩ are tangents, the points x0, y0, z0 are
singular, that is, Q(x0) = Q(y0) = Q(w0) = 0. The line ⟨x, w⟩ is a tangent, so
Q(x + tw) = 0 has a unique solution t. Now

Q(x + tw) = Q(z + x0 + t(z + w0)) = Q((1 + t)z + x0 + tw0)

= (1 + t)
2Q(z) + Q(x0 + tw0) = (1 + t)
2Q(z) + tB(x0, w0).

It follows that (2 + B(x0,w0)
Q(z) )
2 = 4, that is B(x0,w0)
Q(z) ∈ {0, −4}.
As Q∣
∣
S is nondegenerate, z⊥ ∩ S is a nondegenerate plane. If B(x0, w0) =
0, then ⟨x0, w0⟩ is a totally singular line in this plane, impossible. Hence,
B(x0, w0) = −4Q(z). Similarly, B(y0, w0) = −4Q(z).
In the plane z⊥ ∩S, let u be the point of intersection of the tangents through
the points x0 and y0 and write w0 = ax0 + by0 + cu. Then B(x0, u) = B(y0, u) =
0 and −4Q(z) = B(x0, w0) = B(x0, ax0 + by0 + cu) = bB(x0, y0). Similarly,

7

−4Q(z) = B(y0, w0) = aB(x0, y0), so that a = b = −4Q(z)
B(x0,y0) , independent of w.
Also,

0 = Q(w0) = Q(ax0 + by0 + cu) = abB(x0, y0) + c2Q(u) = 16Q(z)
2

B(x0, y0) + c2Q(u).

If −B(x0, y0)Q(u) is a square, then we have two solutions for c (so also w0
and, therefore, w) and otherwise none. Since u is an exterior point in the plane
σ = z⊥∩S, the number −Q(u) det Q∣
∣
σ is a square. Also, det Q∣
∣
S = Q(z) det Q∣
∣σ
and B(x, y) = B(x0, y0) + B(z, z). ✷

Proposition 6.3 The graph N Oε
2m+1(q) satisﬁes the 4-vertex condition.

Proof. By Proposition 2.1 it suﬃces to check for x ̸= y that the number of
edges in Γ(x) ∩ Γ(y) does not depend on the choice of the points x, y, but only
on whether x, y are adjacent or not.
Since Aut Γ is edge-transitive, we only need to check Γ(x) ∩ Γ(y) for x ̸∼ y.

Claim: this subgraph Γ(x) ∩ Γ(y) is regular of valency 4q2m−3 + 3εqm−1 −
4εqm−2 − 1. In other words, this is the value of µ in the local graph (which is
regular, but not strongly regular).
If x ∼ z ∼ y, x ̸∼ y, then π = ⟨x, y, z⟩ is a nondegenerate plane in which
the common neighbors of x, y form a 4-cycle, so that x, y, z have two common
neighbors in π, say a and b.
The plane π lies in (q2m−3 − εqm−2)/2 solids of type O−(4, q), equally many
solids of type O+(4, q), and (qm−2 + ε)(qm−1 − ε)/(q − 1) degenerate solids.
If S is a degenerate solid through π with apex p, we see that w ∈ S \ π is
in Γ(x) ∩ Γ(y) ∩ Γ(z) if and only if gets projected from p onto an element of
{a, b, z} in π. Hence, |Γ(x) ∩ Γ(y) ∩ Γ(z) ∩ S \ π| = 3(q − 1). Hence, the total
number of choices for w equals 3(qm−2 + ε)(qm−1 − ε).
Now let S be a nondegenerate solid on π, and let p = S ∩π⊥. By Lemma 6.2,
the number of w in S is 0 or 2, depending on the determinant of Q restricted to
S. Since π⊥ contains equally many points p with Q(p) a square as with Q(p) a
non-square, the total number of choices for w equals the number of choices for
p which is q2m−3 − εqm−2.
So the induced subgraph on Γ(x) ∩ Γ(y) has valency 2 + 3(qm−2 + ε)(qm−1 −
ε) + (q2m−3 − εqm−2) = 4q2m−3 + 3εqm−1 − 4εqm−2 − 1. ✷

7 Polar switching

A polar space is a partial linear space such that for each line L any point outside L is collinear
to either all or precisely one of the points of L. A singular subspace is a line-closed set of
points, any two of which are collinear. The polar space is called nondegenerate when no point
is collinear to all points. Finite nondegenerate polar spaces are the sets of totally isotropic
(t.i.) or totally singular (t.s.) points and lines in a vector space over a ﬁnite ﬁeld provided
with a suitable symplectic, quadratic or hermitian form. The rank of the polar space is the
(vector space) dimension of its maximal singular subspaces.

Let P be a nondegenerate polar space of rank d ≥ 3 in a vector space V
over Fq. Its collinearity graph Γ0 is strongly regular and satisﬁes the 4-vertex
condition (since it is rank 3). We shall construct cospectral graphs that satisfy

8

the 4-vertex condition (but are not rank 3) by a switching construction. Let x
⊥

be the set of points collinear with x (including x itself).

Suppose U is a maximal singular subspace of P (i.e., a maximal clique in Γ0), and let
H1, H2 be two hyperplanes of U . We can redeﬁne adjacency and make the points x with
x⊥ ∩ U = H1 or H2 adjacent to the points in H2 or H1, respectively, and leave all other
adjacencies unchanged. This is an example of WQH-switching (Wang, Qiu & Hu [33], cf. [19])
and yields a graph cospectral with Γ0. One can repeat this interchange of hyperplanes and get
arbitrary permutations of all hyperplanes. We generalize this, even allowing diﬀerent designs
on U .

7.1 Construction

Let P be the point set of P, and let the subset U be (the set of points of) a totally
isotropic d-space. Let D be a symmetric design with the same parameters as the
symmetric design of points and hyperplanes of PG(d − 1, q), so its parameters
are 2-( qd−1
q−1 , qd−1−1
q−1 , qd−2−1
q−1 )
. Let ϕ be a bijection from the set H of hyperplanes
of U to the blocks of D. We assume that the points of U are also the points of
D. Following ideas in [24] and [12] we deﬁne a graph Γϕ on the vertex set of Γ0
as follows:

1. Vertices in U are pairwise adjacent.

2. Distinct vertices x, y /∈ U are adjacent if x ∈ y⊥.

3. Vertices x ∈ U , y /∈ U are adjacent if x ∈ (y⊥ ∩ U )
ϕ.

Clearly, Γϕ = Γ0 if we take the hyperplanes of U for the blocks of D and ϕ
as the identity.

Theorem 7.1 The graph Γϕ is strongly regular with the same parameters as
the classical graph Γ0.

Proof. Let x and y be any two vertices. We show that the number of common neighbors
z of x, y in Γϕ does not depend on ϕ (but depends on whether x, y are equal, adjacent or
nonadjacent in Γϕ).
If x, y ∈ U , then any z ∈ U is a common neighbor. The number of z ∈ P \ U such
that x, y ∈ (z⊥ ∩ U )ϕ does not depend on ϕ: each hyperplane H of U such that x, y ∈ H ϕ

contributes |H ⊥ \ U | such z.
Suppose that x, y /∈ U . Then we are counting the z in (x⊥ ∩ U )ϕ ∩ (y⊥ ∩ U )ϕ, and also
the z in (x⊥ ∩ y⊥) \ U . The numbers of such z does not depend on ϕ.
The remainder of the proof concerns the case x ∈ U , y /∈ U . If z ∈ U then the requirements
are z ̸= x and z ∈ (y⊥ ∩ U )ϕ. The number of such z does not depend on ϕ.
So we need to count the z /∈ U . First set I := y⊥ ∩ U , so Y := ⟨y, I⟩ is totally isotropic.
If z ∈ Y then I ϕ = (z⊥ ∩ U )ϕ, and x, z are adjacent if and only if x, y are adjacent. The
number of such z is independent of ϕ.
It remains to count the z in y⊥ \ Y such that x ∈ (z⊥ ∩ U )ϕ; here z⊥ ∩ U ̸= I as z /∈ Y .
Let H ̸= I be a hyperplane of U such that x ∈ H ϕ. The number of H does not depend on ϕ
(note that x ∈ I ϕ if and only if x, y are adjacent in Γϕ). We show that the number of z in
y⊥ \ Y with z⊥ ∩ U = H does not depend on ϕ or H. Using bars to project (H ∩ I)⊥ into the
nondegenerate rank 2 polar space (H ∩ I)⊥/(H ∩ I), we see totally isotropic lines ¯U and ¯Y
meeting at a point ¯I, and a nondegenerate 2-space ⟨¯y, ¯H⟩; the number of ¯z in ⟨¯y, ¯H⟩⊥\ ¯I does
not depend on ϕ or H, so neither does the number of required z. ✷

9

7.2 Isomorphisms

Emptying bijections ϕ

Call a vertex e ∈ U emptying for ϕ if ⋂
{H | H ∈ H, e ∈ H ϕ} = ∅. Call ϕ
emptying if the subspace U is spanned by emptying vertices.
Call a vertex f ∈ U dually emptying for ϕ if ⋂
{H ϕ | f ∈ H ∈ H} = ∅. Call
ϕ dually emptying if the subspace U is spanned by dually emptying vertices.

If a is not emptying, then ⋂{H | H ∈ H, a ∈ H ϕ} = {b} for some vertex b. If b is not
dually emptying, then ⋂{H ϕ | b ∈ H ∈ H} = {a} for some vertex a. This establishes a 1-1
correspondence between not emptying vertices a and not dually emptying vertices b.

Proposition 7.2 If a permutation ϕ of H is not dually emptying, then it is in
PΓL(U ).

Proof. Let E denote the set of emptying vertices of U , and put A = U \ E. Let F denote
the set of dually emptying vertices of U , and put B = U \ F . Let ψ : B → A be the 1-1
correspondence found above. We show that if L is a line in U with |L ∩ B| ≥ q, then L ⊆ B
and Lψ is a line.
Indeed, let b, b′ ∈ L ∩ B and set M = ⟨bψ , b′ψ⟩. Then L ⊆ H is equivalent to M ⊆ H ϕ so
that (L ∩ B)ψ = M ∩ A. If all points of L are in B with a single exception w, then all points
of M are in A with a single exception v, and all hyperplanes H with w ∈ H satisfy v ∈ H ϕ

(since every line meets every hyperplane), and v = wψ, that is, w was no exception.
If ϕ is not dually emptying, then there exists a hyperplane H such that U \ H ⊆ B. By
the above this implies B = U and ψ is in PΓL(U ) and induces ϕ on the set H. ✷

Large cliques

We use the presence of maximal cliques of various sizes to study the structure
of the graphs Γϕ when ϕ is a permutation.

Abbreviate the size qi−1
q−1 of an i-space with mi, so that maximal singular
subspaces have size md. Since md is the Delsarte-Hoﬀman upper bound for
the size of cliques in Γϕ, each vertex outside a clique of this size is adjacent to
precisely md−1 vertices inside, cf. [6, Proposition 1.1.7].

Lemma 7.3 Let d ≥ 3.
(i) If M ̸= U is a maximal singular subspace of P, then C = (M \ U ) ∪⋂
{H ϕ | M ∩ U ⊆ H ∈ H} is a maximal clique in Γϕ of size at least qd−2(q + 1)
(and C \ U = M \ U ).
(ii) If C ̸= U is a maximal clique in Γϕ of size at least qd−2(q + 1), then
M = ⟨C \ U ⟩ is a maximal singular subspace of P.
If, moreover, |C| = md, then M \ U = C \ U .

Proof. (i) Let M be a maximal singular subspace other than U . Then C =
(M \ U )∪⋂{H ϕ | M ∩U ⊆ H ∈ H} is the largest clique in Γϕ containing M \ U .
(Indeed, the set of hyperplanes of U of the form m⊥ ∩ U where m ∈ M \ U
equals the set of hyperplanes containing M ∩ U , so C is a clique. No further
point outside U ∪ C can be adjacent to all of C, since |M \ U | > md−1.) If
dim M ∩ U = d − 1, then |C| = |M | = md. If dim M ∩ U ≤ d − 2, then
|C| ≥ |M \ U | ≥ md − md−2 = qd−2(q + 1).
(ii) Let C ̸= U be a maximal clique of size at least qd−2(q + 1). If |C \ U | ≤
md−1, then |C ∩ U | ≥ qd−2(q + 1) − md−1 > md−2. The set C ∩ U is the
intersection of sets H ϕ, each of size md−1, and any two distinct such sets meet

10

in md−2 points. It follows that no two diﬀerent H occur, that is, H = c⊥ ∩ U
is independent of the choice of c ∈ C \ U . Now C is contained in, and hence
equals, H ϕ ∪ (C \ U ), and |C \ U | = md − md−1 > md−1, a contradiction.
If S is a clique in Γ0, then also ⟨S⟩ is a clique in Γ0. In particular, ⟨C \ U ⟩
is a singular subspace. It is maximal since |⟨C \ U ⟩| > md−1.
If |C| = md, then each vertex outside C is adjacent to precisely md−1 vertices
inside. Hence no point outside C ∪ U can be adjacent to all of C \ U . ✷

Lemma 7.4 If the permutation ϕ is dually emptying, then U is uniquely deter-
mined within the graph Γϕ.

Proof. The subspace U is a clique of size md in Γϕ, with the two properties
(i) in the subgraph induced on its complement P \ U all maximal cliques N
have size md − mi (where mi = |⟨N ⟩ ∩ U |) for some i, 0 ≤ i ≤ d − 1, and
(ii) the number of maximal cliques of size md disjoint from U equals the
number of maximal singular subspaces disjoint from any given one.

Let E ̸= U be a clique of Γϕ of size md with the same two properties. First
we use (i) to see that E ∩ U must be a hyperplane in U .

Since E is a maximal clique, and ϕ is a permutation, E ∩ U is an intersection
of hyperplanes and hence a subspace of U . By hypothesis, we can ﬁnd a dually
emptying point f of U not in E. If g ∈ f ⊥ ∩ (E \ U ) (g will exist unless
f ⊥ ∩ E = U ∩ E) and M is a maximal singular subspace containing f and g,
and meeting U in {f }, then C = M \ {f } is a maximal clique in Γϕ of size
md − 1. And N = C \ E is a maximal clique in P \ E of size md − mi − 1 in
case |M ∩ E| = mi. (Note that C \ U = M \ U .)

Why is N maximal? No point can be added since |N | > md−1, unless q = 2 and |N | =
|M ∩ E| = md−1. In that case, no point outside U can be added since ⟨N ⟩ = M . And no point
inside U can be added since N determines all hyperplanes on f , and f is dually emptying.

Since M ∩ E ̸= ∅, we have 1 ≤ i ≤ d − 1, and md − mi − 1 is not of the form
md − mh, violating (i). Therefore, f ⊥ ∩ E = U ∩ E, so that H = ⟨E \ U ⟩ ∩ U
and H ϕ = E ∩ U are hyperplanes.

Now we use (ii) to arrive at a contradiction.
We claim that if a maximal clique F of size md is disjoint from E, then
⟨F \ U ⟩ is disjoint from ⟨E \ U ⟩. Suppose not. Since ⟨E \ U ⟩ \ U = E \ U and
⟨F \ U ⟩ \ U = F \ U by Lemma 7.3(ii), a common vertex must lie in U . If
⟨F \ U ⟩ meets U in me vertices with e ≥ 2, then F meets U in a subspace of
dimension e, but that would meet H ϕ, impossible. So, ⟨F \ U ⟩ meets U in a
singleton {f } on the hyperplane H. As F has size md, f is not dually emptying,
so ⋂
{H ϕ | f ∈ H} = {f ′} for some point f ′. Now f ′ ∈ E ∩ F , a contradiction.
This shows our claim.
By the claim and Lemma 7.3, we have an injection from the set of maximal
cliques of size md disjoint from E into the set of maximal singular subspaces
disjoint from ⟨E \ U ⟩. Since E satisﬁes (ii), both sets have the same size, so the
injection is also a surjection.
On the other hand, since ϕ is dually emptying, there is a dually emptying
point o in U \ H. This o lies in a maximal singular subspace O disjoint from
⟨E \ U ⟩, and this O is not in the image of the surjection. Contradiction. ✷

11

Lemma 7.5 Let P be a nondegenerate polar space with point set P , and U
a maximal totally isotropic subspace. Let h : P \ U → P \ U be a bijection
preserving collinearity. Then h can be uniquely extended to an automorphism
h′ of P.

Proof. Indeed, we can extend h as follows. For u ∈ U , let R be a maximal t.i. subspace
with U ∩ R = {u}. Then R \ {u} is a subspace of L of size |U | − 1 and is mapped by h to
a similar subspace S. In P this subspace is contained in a unique maximal t.i. subspace ⟨S⟩
(= S⊥) and we can deﬁne h′(u) = v when ⟨S⟩ \ S = {v}.
This is well-deﬁned: if R′ is a maximal t.i. subspace with U ∩ R′ = {u} and R, R′ meet in
codimension 1, and h maps R′ \ {u} to S′, then ⟨S ∩ S′⟩ = (S ∩ S′) ∪ {v}. Since the graph on
such subspaces R, adjacent when they meet in codimension 1, is connected, v is well-deﬁned.
This preserves orthogonality: if u ∈ x⊥, then there is a maximal t.i. subspace R containing
u, x with R ∩ U = {u}. Now h(u) = v lies in the t.i. subspace ⟨h(R \ {u})⟩ which also contains
h(x). ✷

Proposition 7.6 Let P be a nondegenerate polar space and U a maximal t.i. sub-
space. Let ϕ and χ be permutations of H such that Γϕ is isomorphic to Γχ. Then
ϕ and χ are in the same PΓL(U )-double coset in Sym(H).

Proof. If ϕ ∈ PΓL(U ), then Γϕ is isomorphic to Γ0 and its group of automor-
phisms is transitive on the set of maximal singular subspaces. If ϕ /∈ PΓL(U ),
then according to Lemma 7.4 and Proposition 7.2 the maximal singular subspace
U can be recognized in Γϕ, and hence Γϕ is not isomorphic to Γ0. Since by
assumption Γϕ and Γχ are isomorphic, either both or neither are isomorphic
to Γ0. In the former case both ϕ and χ are in PΓL(U ) and the claim holds.
Assume in the following that ϕ and χ are not in PΓL(U ).

We have the set P , the point set of P, with three structures deﬁned on it.
The polar space structure P, with relation ⊥, and the two graph structures Γϕ
and Γχ. We translate what it means for Γϕ and Γχ to be isomorphic in terms
of the polar space.
Let g : Γϕ → Γχ be an isomorphism. By Lemma 7.4, it sends U to itself.
The number of common neighbors of a triple of points in U equals λ − 1 for
collinear triples and is smaller for noncollinear triples. It follows that g preserves
projective lines in U , and hence induces a permutation ¯g of H that is in PΓL(U ).
Let h denote the restriction of g to P \ U . Then h preserves collinearity
(since we have {x, y, z}⊥ ∩ (P \ U ) = {x, y}⊥ ∩ (P \ U ) for a triple of pairwise
adjacent points x, y, z of P \ U if and only if x, y, z are collinear). By Lemma
7.5, h can be uniquely extended to an automorphism h′ of P.

Let ¯h be the permutation of H induced by h′. Then ¯h ∈ PΓL(U ).
For x ∈ U and y /∈ U , if x and y are adjacent in Γϕ, then x
g and yg are
adjacent in Γχ. This says that x ∈ (y⊥ ∩ U )
ϕ implies that x
g ∈ (yg⊥ ∩ U )
χ:
g maps the points of any hyperplane of U to the points of another hyperplane.
Then (y⊥ ∩ U )
ϕg = (yg⊥ ∩ U )
χ = (yh⊥ ∩ U )
χ = (y⊥ ∩ U )¯hχ, so that ϕ¯g = ¯hχ.
✷

Theorem 7.7 Let d ≥ 3. There are at least qd−2! pairwise nonisomorphic
strongly regular graphs having the same parameters as the collinearity graph Γ0
of the polar space P.
 12

Proof. Let q = pe, where p is prime. Then |PΓL(U )| < eqd2. In view of
Proposition 7.6, we have obtained at least md!/|PΓL(U )|2 > qd−2! pairwise
nonisomorphic strongly regular graphs unless (d, q) = (3, 2). For (d, q) = (3, 2),
we have four PΓL(U )-double cosets in Sym(H). ✷

Similar estimates would follow if one generalized Lemma 7.4 to show that U
is uniquely determined in P for arbitrary designs D (that is, for ϕ that are not
permutations). The blocks of D are then found as {Γϕ(x) ∩ U | x ∈ P \ U }. In
[24, Corollary 3.2] it is shown that for d ≥ 4 there are at least qd−2! choices for
D. Hence, one would obtain the same estimate as in Theorem 7.7 for d ≥ 4.

7.3 Switched symplectic graphs with 4-vertex condition

We show that in the symplectic case the graphs Γϕ satisfy the 4-vertex condition.
Let P be Sp2d(q), and let V be a 2d-dimensional vector space over Fq, provided
with a nondegenerate symplectic form.

The parameters of Γ0 are v = (q2d −1)/(q −1), k = q(q2d−2 −1)/(q −1), v −k −1 = q2d−1,
λ = q2(q2d−4−1)/(q−1)+q−1, µ = (q2d−2−1)/(q−1) and (λ
2)−α = 1
2 q2d−1(q2d−4−1)/(q−1),
β = 1
2 q(q2d−2 − 1)(q2d−4 − 1)/(q − 1)2, and those of Γϕ will turn out to be the same.

Proposition 7.8 The graph Γϕ satisﬁes the 4-vertex condition.

Proof. Let x, y be two vertices of Γϕ. We show that the number of edges
in Γϕ(x) ∩ Γϕ(y) is independent of ϕ, and only depends on whether x, y are
adjacent or nonadjacent. Since Γ0 satisﬁes the 4-vertex condition, Γϕ does too.
Count edges ab in Γϕ(x) ∩ Γϕ(y). The vertices x, y, a, b are pairwise adja-
cent, except that x and y need not be adjacent. We distinguish several cases
depending on which of x, y, a, b are in U . Each of the separate counts will be
independent of ϕ. If x /∈ U then let X = x
⊥ ∩ U . If y /∈ U then let Y = y⊥ ∩ U .

Case x, y, a, b /∈ U . In this case adjacencies and counts do not involve ϕ.

Case a, b ∈ U . Here a, b must be chosen distinct from x, y in case x, y ∈ U ,
or distinct from x and in Y ϕ in case x ∈ U , y /∈ U (and the count depends on
whether x ∼ y), or in X ϕ ∩ Y ϕ in case x, y /∈ U (and the count depends on
whether X = Y ). In all cases the count is independent of ϕ.

Case x, y, a ∈ U , b /∈ U . For each hyperplane H such that x, y ∈ H ϕ we count
the b ∈ H ⊥ \ U and the a ∈ H ϕ distinct from x, y.

Case x, y ∈ U , a, b /∈ U . For any two hyperplanes H, H ′ of U with x, y ∈
H ϕ ∩ H ′ϕ count adjacent a, b with a ∈ H ⊥ \ U and b ∈ H ′⊥ \ U . (The counts
will depend on whether H = H ′, but not on ϕ.)

Case x, a ∈ U , y, b /∈ U . For each hyperplane H with x ∈ H ϕ, count the
a ∈ H ϕ ∩ Y ϕ distinct from x, and b ∈ H ⊥ \ U adjacent to y. (Here H = Y
occurs when x ∼ y. The counts for H ̸= Y do not depend on H.)

13

Case x ∈ U , y, a, b /∈ U . For any two hyperplanes H, H ′ with x ∈ H ϕ ∩ H ′ϕ,
count edges ab with a ∈ H ⊥ and b ∈ H ′⊥ in y⊥ \ (U ∪ {y}). (Here H = Y or
H ′ = Y occur when x ∼ y. The counts for H, H ′ ̸= Y do not depend on the
hyperplanes chosen but only on whether H = Y or H ′ = Y or H = H ′.)

Finally the least trivial case.

Case a ∈ U , x, y, b /∈ U . Count a, H, b with a ∈ X ϕ ∩ Y ϕ and H a hyperplane
of U on a and b ∈ ⟨x, y, H⟩
⊥ \ (U ∪ {x, y}). The count for a depends on whether
X = Y , that for b depends on whether H = X or H = Y or H ⊇ X ∩ Y , but
does not otherwise depend on the choice of H.

Since all counts were independent of ϕ, this proves our proposition. ✷

By Theorem 7.7, this shows that there are many strongly regular graphs
which satisfy the 4-vertex condition. But we still have to show the simpliﬁed
version of this statement given in the introduction as Theorem 1.1.

Proof of Theorem 1.1. Note that here v refers to a nonnegative integer as
in Theorem 1.1 and no longer is the number of vertices in Γϕ.
Apply Theorem 7.7 for d = 3 to ﬁnd at least q! strongly regular graphs
satisfying the 4-vertex condition on ˜v vertices, for ˜v = q6−1
q−1 . Given v, there
is a prime q between v1/6 and 2v1/6 by Bertrand’s postulate. Now ˜v < 2q5 <
64v5/6 < v for v > 236. Checking the prime powers q for 7 ≤ q ≤ 64 one sees
that there is a q with ˜v ≤ v ≤ q6 for v ≥ 19608. One easily veriﬁes the assertion
for v < 19608 using rank 3 graphs. ✷

Further graphs with the same parameters satisfy the 4-vertex condition. Additional
examples can be obtained by repeated WQH-switching, see §7.4 and [19], and there are more
examples among the graphs constructed in [18]. We have not tried (much) to determine
precisely which graphs in [18] do satisfy the 4-vertex condition. Similarly, we do not know
when WQH-switching preserves the 4-vertex condition.

7.4 Small examples

Examples on 63 vertices

In [20] a large number of strongly regular graphs are found by applying GM-
switching to the Sp6(2) polar graph. Among these are 280 non-rank-3 strongly
regular graphs with (v, k, λ, µ) = (63, 30, 13, 15) satisfying the 4-vertex condition.
All have α = 30 and β = 45. Three of these are among the Γϕ constructed above.
We list for each occurring group size the number of examples found.

|G| 4 8 16 32 48 64 96 128 192 256 384 512 768 1344 1536 4608
# 3 16 76 62 1 60 2 30 5 12 3 3 2 1 3 1

None of these examples has a transitive group. We list the orbit lengths in
the seven cases with fewer than six orbits.

|G| 768 768 1344 1536 1536 (twice) 4608
orbits 3+12+48 1+6+24+32 7+56 1+6+24+32 3+4+8+48 3+12+48

14

Permutations of hyperplanes

Let P be Sp2d(q), and let ϕ be a permutation of the set H of hyperplanes of
U . For (d, q) = (3, 2), (3, 3), (4, 2), the number of double cosets of PΓL(d, q)
in Sym(H) is 4, 252, and 3374, respectively, and these are the numbers of non-
isomorphic graphs Γϕ. In each case, exactly one has rank 3. None of the others
has a transitive group (since U can be recognized). The pointwise stabiliser of
U in Aut(Γ0) has size N = q(
d+1
2 )(q − 1) and is always contained in Aut(Γϕ).
Hence, N divides |Aut(Γϕ)|.

Case (d, q) = (3, 3). Here N = 1458. We list the group sizes for the 251
graphs Γϕ other than Γ0.

|G|/N 1 2 3 4 6 8 12 16 18 24 39 54 72 144
# 172 26 29 6 3 2 2 2 1 1 3 1 2 1

We list the orbit lengths in the ﬁve cases with fewer than six orbits.

|G|/N 39 (thrice) 72 144
orbits 13+351 1+12+108+243 1+12+108+243

Case (d, q) = (4, 2). Here N = 1024. We list the group sizes for the 3373
graphs Γϕ other than Γ0.

|G|/N 1 2 3 4 5 6 7 8 12 16 18 21 24 32 56 60 96 192 288 1344
# 3148 85 40 24 4 10 6 26 1 4 1 2 11 2 2 1 2 2 1 1

We list the orbit lengths in the eight cases with fewer than six orbits.

|G|/N 12 18 24 56 (twice)
orbits 3+12+48+192 6+9+96+144 3+12+48+192 1+14+112+128
|G|/N 60 288 1344
orbits 15+240 3+12+48+192 7+8+16+224

Other polar spaces

We made the same exhaustive investigation of all permutations ϕ for the other
choices of P in the cases (d, q) ∈ {(3, 2), (3, 3), (4, 2)}. The only non-rank-3
examples satisfying the 4-vertex condition occur for O7(3). Here we obtain 252
graphs in total, of which one is rank 3, and three more satisfy the 4-vertex
condition. They all have two orbits (of sizes 13+351) and an automorphism
group of size 56862. All other graphs Γϕ obtained from O7(3) have more than
two orbits.
One might wonder whether a graph Γϕ from O2d+1(q) satisﬁes the 4-vertex
condition if and only if it has at most two orbits. And whether a non-rank-3
graph Γϕ can only satisfy the 4-vertex condition if P is Sp2d(q) or O2d+1(q).

Other designs

There are four 2-(15, 7, 3) designs D other than that of the hyperplanes of
PG(3, 2). We investigated the case where (d, q) = (4, 2) and P is Sp2(8), so
that the resulting examples satisfy the 4-vertex condition. We generated several
hundred thousand graphs Γϕ for each of these designs. None of these graphs
occurs for two diﬀerent designs. We believe our enumeration to be complete.

15

|Aut(D)| point orbits block orbits # Γϕ
576 3+12 3+12 113519
168 7+8 1+14 340730
168 1+14 7+8 328078
96 1+6+8 1+6+8 677460

Appendix A — Details on Ivanov’s graphs

In Section 3.3 we discussed the graphs Γ(m) from [4] and Σ(m) from [22]. Here we give some
more detail on the latter.
For m ≥ 2, consider V = F 2m
2 provided with the elliptic quadratic form q(x) = x 2
1 +
x 2
2 + x1x2 + x3x4 + ... + x2m−1x2m. Identify the set of projective points (1-spaces) in V with
V ∗ = V \ {0}. Let Q = {x ∈ V ∗ | q(x) = 0} and let S be the maximal t.s. subspace given by
S = {x ∈ V ∗ | x1 = x2 = 0 and x2i−1 = 0 (2 ≤ i ≤ m)}. Then S⊥ = {x ∈ V ∗ | x2i−1 = 0
(2 ≤ i ≤ m)}. The graph Σ(m) has V as vertex set, where two distinct vertices v, w are
adjacent when v − w ∈ (Q ∪ S⊥) \ S. Let T(m) and Υ(m) be the induced subgraphs on the
neighbors (nonneighbors) of the vertex 0. Put R = V ∗ \ (Q ∪ S⊥).

Proposition.
(i) For m ≤ 4, the graphs Σ(m) are rank 3, and are isomorphic to the complement of
V O−
2m(2).
(ii) For m ≥ 5, the automorphism group of T(m) has two vertex orbits S⊥ \ S and Q \ S,
of sizes 3 · 2m−1 and 22m−1 − 2m, respectively. For 2 ≤ m ≤ 4, the group is rank 3, and the
graph is the complement of N O−
2m(2).
(iii) For m ≥ 5, the automorphism group of Υ(m) has two vertex orbits S and R of sizes
2m−1 − 1 and 22m−1 − 2m, respectively. For 3 ≤ m ≤ 4, the group is rank 3, and the graph
is the complement of O−
2m(2).
(iv) The λ- and µ-graphs in Υ(m) and the µ-graphs in T(m) are all regular of valency
2m−2(2m−2 + 1). In particular, Υ(m) satisﬁes the 4-vertex condition.
(v) The λ-graphs in T(m) have vertices of valencies in 0, 22m−4 −2m, 22m−4, 22m−3 −2m.
Edges not in a line contained in Q have λ-graphs with a single isolated vertex and λ − 1
vertices of valency 22m−4. For edges in a line contained in Q the λ-graphs have a single
vertex with valency 22m−3 − 2m, and 2m−3 − 1 vertices with valency 22m−4 − 2m, and
the remaining 22m−3 + 2m−3 vertices have valency 22m−4. In particular, T(m) satisﬁes the
4-vertex condition, with α = 22m−5(22m−3 + 2m−2 − 1) and β = 1
2 µµ′ = 22m−4(2m−2 + 1)2.
(vi) The local graph of Υ(m) at a vertex s ∈ S is isomorphic to Σ(m−1).

Proof. (i)–(iii) This is clear, and can also be found in [22].
(iv)-(v) (the part about T(m)):
Let (v, w) = q(v + w) − q(v) − q(w) be the symmetric bilinear form belonging to q. Let
X = (Q ∪ S⊥) \ S. Then T(m) is the graph with vertex set X, where two vertices x, y are
adjacent when the projective line {x, y, x + y} they span is contained in X. If at least one
of x, y is in S⊥ \ S, then this is equivalent to (x, y) = 1. If both are in Q \ S, then this is
equivalent to ((x, y) = 0 and x + y /∈ S) or ((x, y) = 1 and x + y ∈ S⊥ \ S).
Let x, y, z be pairwise adjacent vertices. The valency c of z in the λ-graph λ(x, y) is the
number of common neighbors of x, y, z. Distinguish several cases.
If z = x + y, then if x, y, z ∈ Q we ﬁnd c = |{x, y}⊥ ∩ (Q \ S)| − 3 = 22m−3 − 2m. If
z = x + y and at least one of x, y, z lies in S⊥, then c = 0.
Now let z ̸= x + y. The claims are true for m ≤ 4. Let m ≥ 5 and use induction on m.
Choose coordinates so that x, y, z have ﬁnal coordinates 00 and let x′, y′, z′ be these points
without the ﬁnal two coordinates. If they have c′ common neighbors w′ in T(m−1), then we
ﬁnd 2c′ common neighbors w = (w′, 0, ∗). Moreover (since x, y, z are linearly independent),
we ﬁnd 22m−5 common neighbors (w′, 1, q′(w′)) in Q, where w′ runs through all vectors with
the desired inner products with x′, y′, z′. Altogether c = 2c′ + 22m−5, as claimed.
For the µ-graphs the argument is similar and simpler: by the deﬁnition of adjacency three
dependent vertices are pairwise adjacent, so that the case z = x + y does not occur here.
(iv) (the part about Υ(m)): Let Y = V ∗ \ X. Then Υ(m) is the graph with vertex set
Y , where two vertices x, y are adjacent when the projective line {x, y, x + y} they span is not
contained in Y . The same argument as before yields the valencies of the λ- and µ-graphs.
(vi) Consider the graph Σ(m). The nonneighbors z of 0 that are neighbors of s are the
vertices of the form z = s + b with z ∈ S ∪ R and b ∈ (Q ∪ S⊥) \ S. It follows that

16

s + z ∈ Q \ s⊥. Let s = (0 . . . 01), then Q \ s⊥ can be identiﬁed with W = F 2m−2
2 via
w → i(w) = (w, 1, ¯q(w)) for w ∈ F 2m−2
2 and ¯q(w) determined by q(i(w)) = 0. The local
graph of Υ at s can be identiﬁed with the graph with vertices w, where w, w′ are adjacent
when the line joining i(w), i(w′) has third point (w + w′, 0, ∗) ∈ (Q ∪ S⊥) \ S, that is, the line
joining w, w′ has third point w′′ = w + w′ satisfying w′′ /∈ T and (¯q(w′′) = 0 or w′′ ∈ T ⊥)
where T = {w ∈ W | w1 = w2 = w3 = w5 = ... = w2m−3 = 0}. But this is Σ(m−1). ✷

Acknowledgment The second author is supported by a postdoctoral fellow-
ship of the Research Foundation – Flanders (FWO).

References

[1] E. Bannai, S. Hao & S.-Y. Song, Character tables of the association schemes
of ﬁnite orthogonal groups acting on the nonisotropic points, J. Comb. Th.
(A) 54 (1990) 164–200.

[2] A. E. Brouwer, Strongly regular graphs from hyperovals, https://
www.win.tue.nl/~aeb/preprints/hhl.pdf, accessed on 2021-02-21.

[3] A. E. Brouwer, A. M. Cohen & A. Neumaier, Distance-regular graphs,
Springer, Heidelberg, 1989.

[4] A. E. Brouwer, A. V. Ivanov & M. H. Klin, Some new strongly regular
graphs, Combinatorica 9 (1989) 339–344.

[5] A. E. Brouwer & J. H. van Lint, Strongly regular graphs and partial
geometries, pp. 85–122 in: Enumeration and design (Waterloo, Ont., 1982),
Academic Press, 1984.

[6] A. E. Brouwer & H. Van Maldeghem, Strongly regular graphs, Cambridge
Univ. Press, Cambridge, 2022.

[7] P. J. Cameron, Partial quadrangles, Quart. J. Math. Oxford, 25(3) (1974),
1–13.

[8] P. J. Cameron, J. M. Goethals & J. J. Seidel, Strongly regular graphs having
strongly regular subconstituents, J. Algebra 55 (1978) 257–280.

[9] I. Debroey, Semi partiële meetkunden, Ph. D. thesis, University of Ghent,
1978.

[10] I. Debroey & J. A. Thas, On semipartial geometries, J. Comb. Th. (A) 25
(1978) 242–250.

[11] Ph. Delsarte, Weights of linear codes and strongly regular normed spaces,
Discr. Math. 3 (1972) 47–64.

[12] U. Dempwolﬀ & W. M. Kantor, Distorting symmetric designs, Des. Codes
Cryptogr. 48 (2008) 307–322.

[13] M. D. Hestenes & D. G. Higman, Rank 3 groups and strongly regular graphs,
pp. 141–159 in: Computers in algebra and number theory (Proc. New York
Symp., 1970), G. Birkhoﬀ & M. Hall jr (eds.), SIAM-AMS Proc., Vol IV,
Providence, R.I., 1971.
 17

[14] D. G. Higman, Partial geometries, generalized quadrangles and strongly
regular graphs, pp. 263–293 in: Atti del Convegno di Geometria Combi-
natoria e sue Applicazioni (Univ. Perugia, Perugia, 1970), Ist. Mat., Univ.
Perugia, Perugia (1971).

[15] R. Hill, Caps and groups, pp. 389–394 in: Colloquio Internazionale sulle
Teorie Combinatorie (Rome, 1973), Tomo II, Atti dei Convegni Lincei, No.
17, Accad. Naz. Lincei, Rome, 1976.

[16] J. W. P. Hirschfeld & J. A. Thas, Sets of type (1, n, q + 1) in P G(d, q),
Proc. London Math. Soc. (3) 41 (1980) 254–278.

[17] T. Huang, L. Huang & M.-I. Lin, On a class of strongly regular designs
and quasi-semisymmetric designs, pp. 129–153 in: Recent developments
in algebra and related areas, Proceedings Conf. Beijing 2007, Chongying
Dong et al. (eds.), Adv. Lect. Math. (ALM) 8, Higher Education Press and
Int. Press, Beijing-Boston, 2009.

[18] F. Ihringer, A switching for all strongly regular collinearity graphs from
polar spaces, J. Algebr. Comb. 46 (2017), 263–274.

[19] F. Ihringer & A. Munemasa, New strongly regular graphs from ﬁnite
geometries via switching, Linear Algebra Appl. 580 (2019), 464–474.

[20] F. Ihringer, Switching for Small Strongly Regular Graphs, arXiv:
2012.08390v1 (2020).

[21] A. V. Ivanov, Non rank 3 strongly regular graphs with the 5-vertex condition,
Combinatorica 9 (1989) 255–260.

[22] A. V. Ivanov, Two families of strongly regular graphs with the 4-vertex
condition, Discr. Math. 127 (1994) 221–242.

[23] W. M. Kantor, Some generalized quadrangles with parameters (q2, q), Math.
Z. 192 (1986) 45–50.

[24] W. M. Kantor, Automorphisms and isomorphisms of symmetric and aﬃne
designs, J. Alg. Comb. 3 (1994) 307–338.

[25] P. Kaski, M. Khatirinejad & P. R. J. Östergård, Steiner triple systems
satisfying the 4-vertex condition, Des. Codes Cryptogr. 62 (2012) 323–330.

[26] M. Klin, M. Meszka, S. Reichard & A. Rosa, The smallest non-rank 3
strongly regular graphs which satisfy the 4-vertex condition, Bayreuther
Mathematische Schriften 74 (2005) 145–205.

[27] M. Klin & C. Pech, May 2008, unpublished notes.

[28] S. E. Payne & J. A. Thas, Finite generalized quadrangles, Research Notes in
Mathematics, 110. Pitman (Advanced Publishing Program), Boston, MA,
1984. vi+312 pp.

[29] C. Pech & M. Pech, On a family of highly regular graphs by Brouwer,
Ivanov, and Klin, Discr. Math. 342 (2019) 1361–1377.

18

[30] S. Reichard, A criterion for the t-vertex condition on graphs, J. Comb. Th.
(A) 90 (2000) 304–314.

[31] S. Reichard, Strongly regular graphs with the 7-vertex condition, J. Algebr.
Comb. 41 (2015) 817–842.

[32] C. C. Sims, On graphs with rank 3 automorphism groups, unpublished,
1968.

[33] W. Wang, L. Qiu & Y. Hu, Cospectral graphs, GM-switching and regular
rational orthogonal matrices of level p, Lin. Alg. Appl. 563 (2019) 154–177.

[34] H. A. Wilbrink, unpublished, 1982.

19
