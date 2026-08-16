<!-- source: https://arxiv.org/pdf/1401.6816 | converted from PDF -->

arXiv:1401.6816v1  [math.CO]  27 Jan 2014Strongly Regular Graphs With The 7-Vertex
Condition

Sven Reichard
∗

Institut f¨ur Algebra
Technische Universit¨at Dresden

February 24, 2018

Abstract

The t-vertex condition, for an integer t ≥ 2, was introduced by Hestenes
and Higman in 1971, providing a combinatorial invariant deﬁned on edges
and non-edges of a graph. Finite rank 3 graphs satisfy the condition for
all values of t. Moreover, a long-standing conjecture of M. Klin asserts
the existence of an integer t0 such that a graph satisﬁes the t0-vertex
condition if and only if it is a rank 3 graph.
We construct the ﬁrst inﬁnite family of non-rank 3 strongly regular
graphs satisfying the 7-vertex condition. This implies that the Klin pa-
rameter t0 is at least 8. The examples are the point graphs of a certain
family of generalised quadrangles.

1 Introduction

Strongly regular graphs (see Section 2) occur naturally as rank 3 representations
of ﬁnite permutation groups, and there are many other examples. Whereas in
principle all ﬁnite rank 3 graphs are known (see, e.g., [25], [30]), the more gen-
eral problem of classifying the ﬁnite strongly regular graphs appears completely
hopeless. Hence, it is natural to consider properties of graphs which are satisﬁed
by the rank 3 graphs and also some other, but not all, strongly regular graphs.
Hestenes and Higman [19] introduced a family of such properties of this type
that are called the t-vertex condition for integers t ≥ 2. These conditions are
described in detail in Section 4. For a graph Γ and integer t ≥ 3 the t-vertex
condition leads to a combinatorial invariant on pairs of distinct vertices of Γ;
if this invariant is constant on the edges, we say that Γ satisﬁes the t-vertex
condition on edges, and similarly for non-edges.
The 2-vertex condition is equivalent to regularity of graphs, while the 3-
vertex condition is equivalent to strong regularity. Also for any t ≥ 3, if a

∗Partially supported by the School of Mathematics and Statistics at the University of
Western Australia
 1

graph satisﬁes the t-vertex condition then it also satisﬁes the (t − 1)-vertex
condition (see Section 4). In a rank 3 graph, all edges and all non-edges are
equivalent under the automorphism group, and hence cannot be distinguished
combinatorially, therefore these graphs satisfy the t-vertex condition for any t.
There is a long-standing conjecture by M. Klin [15] that there exists a number
t0 such that the only graphs satisfying the t0-vertex condition are the rank 3
graphs. Since for any ﬁxed t the t-vertex condition can be checked in polynomial
time (see Theorem 4), a proof of Klin’s conjecture would have the remarkable
consequence that rank 3 graphs can be recognised combinatorially in polynomial
time.
Hence it is interesting to consider graphs which are not rank 3 graphs, but
which satisfy the t-vertex condition for large t.

1. For t = 2 it is easy to ﬁnd regular graphs which are not strongly regular,
and hence not rank 3 graphs; a small example being the cycle C6.

2. The smallest strongly regular graph (t = 3) which is not a rank 3 graph is
the well-known Shrikhande graph on 16 vertices, which can be constructed
from a Latin square of order 4.

3. In 1971, Higman [20] gave the ﬁrst examples for t = 4. He showed that the
point graphs of generalised quadrangles (see Section 5) satisfy the 4-vertex
condition. The smallest example of a generalised quadrangle which does
not admit a rank 3 group is the unique GQ(5, 3) on 96 points.

4. In the late 1980’s Ivanov [21] constructed the ﬁrst graph with the 5-vertex
condition that was not a rank 3 graph. It has the parameters of a Latin
square graph L8(16) on 256 vertices. Its ﬁrst and second sub-constituents
(subgraphs induced by the neighbours and non-neighbours, respectively,
of a given vertex) of orders 120 and 135 are strongly regular and satisfy the
4-vertex condition. The graph on 135 vertices was the ﬁrst example known
to satisfy the 4-vertex condition and have an intransitive automorphism
group.

5. Later, Brouwer, Ivanov, and Klin [4] generalised the construction above,
obtaining an inﬁnite series of graphs of order 4k with the 4-vertex condi-
tion. These graphs in fact satisfy the 5-vertex condition as was shown by
the author in [36].

For more historical details we refer to Section 9.
Here, we will once more look at the point graphs of generalised quadrangles.
We show the following:

Theorem 1. The point graph of a generalised quadrangle satisﬁes the 5-vertex
condition.

Theorem 2. For an integer s, the point graph of a generalised quadrangle of
order (s, s2) satisﬁes the 7-vertex condition.

2

Both results are best possible in the sense that there is a generalised quad-
rangle of order (5, 3) which does not satisfy the 6-vertex condition, and there
is a generalised quadrangle of order (5, 25) which does not satisfy the 8-vertex
condition.
This provides us with an inﬁnite family of graphs with intransitive automor-
phism groups which satisfy the 7-vertex condition.

Corollary 1.1. The constant t0 in Klin’s Conjecture is at least 8.

The author acknowledges a set of notes by A. Pasini [33], communicated by
M. Klin, which give the proof of the 5-vertex condition for generalised quad-
rangles of order (s, s2). Thanks to M. Klin for attracting my attention to this
problem, and for countless proposed improvements. He also contributed essen-
tially to the discussion in Section 9. Thanks also to C. Praeger, A. Niemeyer
and C. Pech for helpful discussions, as well as to A. Woldar for helping to polish
the text.

2 Strongly regular graphs

All graphs considered in this text are ﬁnite and simple, i.e., undirected and
without loops or multiple edges. Thus, a graph Γ is a ﬁnite set V = V (Γ) of
vertices together with a binary symmetric and anti-reﬂexive relation referred to
as adjacency. We call v = |V | the order of Γ.
If x and y are distinct vertices of Γ, we write x ∼ y if they are adjacent, and
say that y is a neighbour of x. Otherwise, we call y a non-neighbour of x, and
write x ̸∼ y.
Let Γ(x) = {y ∈ V |x ∼ y} denote the set of neighbours of x in Γ. The
valency of x is deﬁned as val(x) = |Γ(x)|.

Deﬁnition 1 (Regular graph). A graph Γ is regular if there is a number k such
that val(x) = k for all vertices x ∈ V . In this case, k is called the valency of Γ.

Deﬁnition 2 (Strongly regular graph). A graph Γ is strongly regular if there
are numbers k, λ, µ such that

• Γ is regular of valency k;

• any two adjacent vertices of Γ have exactly λ common neighbours, i.e.,
|Γ(x) ∩ Γ(y)| = λ whenever x ∼ y.

• any two distinct, non-adjacent vertices of Γ have exactly µ common neigh-
bours, i.e., |Γ(x) ∩ Γ(y)| = µ whenever x ̸∼ y.

In this case, the numbers (v, k, λ, µ) are called the parameters of Γ, where v = |V |
is its order.

We refer to Section 9 for a brief discussion of numerical restrictions on pu-
tative parameters of Γ.
 3

3 Isoregular graphs

There are several ways to generalise the concept of strong regularity. One of
them is the t-vertex condition, which we will discuss in Section 4. Another one
is isoregularity.
Let Γ = (V, E) be a graph, and let S ⊂ V be a set of vertices. We deﬁne the
valency of S as
 val(S) =
 ∣
∣
∣
∣
∣
 ⋂

x∈S Γ(x)

∣
∣
∣
∣
∣ ,

i.e., the number of vertices adjacent to all elements of S. Note that this gener-
alises the notion of valency since for any vertex x, val ({x}) = val(x).

Deﬁnition 3. Let Γ = (V, E) be a graph, and k ≥ 1 be an integer. Suppose
that for each set S of at most k vertices, the valency of S depends only on
the isomorphism class of the subgraph of Γ induced by S. Then Γ is called
k-isoregular.

Proposition 3.1. For k > 1, k-isoregularity implies (k − 1)-isoregularity.

Proof. Follows directly from the deﬁnition. If the valency of any set S of up
to k elements depends only on the isomorphism class of the induced subgraph,
this holds in particular for all sets of up to k − 1 elements.

Proposition 3.2. A graph Γ is k-isoregular if and only if its complement Γ is
k-isoregular.

Proof. Let Γ be k-isoregular. Let S be a set of k vertices in Γ. Since we have i-
isoregularity for 1 ≤ i ≤ k, we know the valency of every subset of S. Using the
Principle of Inclusion and Exclusion, we can determine the number of vertices
not adjacent to any element of S, i.e., the valency of S in the complement of Γ.
Since the calculation depends only on the isomorphism class of the subgraph of
Γ induced by S, and since this holds for any k-subset S, Γ is k-isoregular.

Proposition 3.3. A graph Γ is 1-isoregular if and only if it is regular. It is
2-isoregular if and only if it is strongly regular.

Proof. Since there is only one isomorphism class of graphs of order 1, and since
the valency of a singleton {x} is the same as the valency of the vertex x, a graph
is 1-isoregular if and only if each vertex has the same valency, in other words,
if and only if the graph is regular.
There are two isomorphism classes of graphs of order 2, namely, edges and
non-edges. A graph is 2-isoregular if and only if it is 1-isoregular, i.e., regular,
and if the number of common neighbours of two distinct vertices x and y depends
only on whether x is adjacent to y. However, this is exactly the deﬁnition of
strong regularity.

For a graph Γ, a vertex x, and an integer i, we deﬁne the i-th subconstituent
Γi(x) as the subgraph of Γ induced by all vertices at distance i from x.

4

Proposition 3.4. For a strongly regular graph Γ, the following are equivalent:

• Γ is 3-isoregular.

• The subconstituents Γi(x), i = 1, 2, are strongly regular, with parameters
which do not depend on the choice of x.

Proof. There are four isomorphism classes of graphs of order 3, determined
uniquely by the number of edges they contain. We will denote these classes by
∆i, where 0 ≤ i ≤ 3 is the number of edges.
Let Γ be a 3-isoregular graph. By Proposition 3.1, it is 2-isoregular, and
hence strongly regular, with parameters (v, k, λ, µ).
Let x be a vertex of Γ, and let Γ1 = Γ(x), the subgraph induced by the
neighbours of x. Γ1 is a regular graph of order k and valency λ. Let y and z be
vertices of Γ1. Then the common neighbours of y and z in Γ1 are exactly the
common neighbours of x, y, z in Γ.
If y ∼ z, then x, y, z induce a complete graph ∆3 in Γ. Hence, y and z have
val(∆3) neighbours in Γ1. Similarly, if y ̸∼ z, x, y, z induce the graph ∆2 in
Γ. Thus y and z have val(∆2) neighbours in Γ1. So we get that Γ1 is strongly
regular, with parameters
 v1 = k

k1 = λ

λ1 = val(∆3)
µ1 = val(∆2)).

We get strong regularity for the second subconstituents by working with the
complement of Γ. More precisely, if Γ is 3-isoregular, then so is the complement
¯Γ, by Proposition 3.2. Then, by the argument above, the ﬁrst subconstituent
of ¯Γ is strongly regular; however, this is precisely the complement of the second
subconstituent of Γ.
Conversely, assume that Γ is a strongly regular graph with parameters
(v, k, λ, µ), such that the subconstituents Γi(x), i = 1, 2, are strongly regu-
lar with parameters (vi, ki, λi, µi). By assumption, Γ is 2-isoregular, hence we
only need to check the graphs ∆i of order 3. Clearly, in Γ we have val(∆3) = λ1,
and val(∆2) = µ1.
Let x, y, z be pairwise non-adjacent vertices in Γ. y and z have µ common
neighbours in Γ; of these, µ2 are not neighbours of x. Hence we get that
val(∆0) = µ − µ2.
Similarly, if y ∼ z, and both are non-adjacent to x, they have λ neighbours
in Γ, and λ2 neighbours in Γ2. Hence, val(∆1) = λ − λ2.
Altogether, we get that Γ is 3-isoregular.

4 The t-vertex condition

Here, we discuss another way of generalising strong regularity. Let Γ be a graph
of order v. Let T be a graph of order t, with two distinguished vertices x0 and

5

y0. We will denote such a triple (T, x0, y0) as a graph type. x0 and y0 will be
called ﬁxed vertices, the other vertices of T will be called additional vertices.
Let x, y be vertices of Γ, and let ∆ be an induced subgraph of Γ containing
both x and y. ∆ is said to be of type T (with respect to x and y) if there is an
isomorphism φ : T → ∆ which maps x0 to x and y0 to y.

Deﬁnition 4. Let Γ be a graph, and let t ≥ 2 be an integer. Suppose that for
any graph type (T, x0, y0) of order at most t, and for any pair of vertices (x, y)
of Γ, the number of subgraphs of Γ which are of type T w.r.t. x and y depends
only on whether x and y are equal, adjacent, or non-adjacent. Then Γ is said
to satisfy the t-vertex condition.

In other words, Γ satisﬁes the t-vertex condition if we cannot distinguish its
edges (vertices, non-edges) by considering subgraphs of order up to t.

Proposition 4.1. For t > 2, the t-vertex condition implies the (t − 1)-vertex
condition.

Proof. Follows directly from the deﬁnition.

Proposition 4.2. A graph Γ satisﬁes the 2-vertex condition if and only if it is
regular. It satisﬁes the 3-vertex condition if and only if it is strongly regular.

Proposition 4.3. A rank 3 graph of order v satisﬁes the v-vertex condition.

Proof. In a rank 3 graph, the automorphism group acts transitively on vertices,
(directed) edges and non-edges. Hence we cannot distinguish edges (resp. non-
edges) on a combinatorial level.

For growing t, the number of graph types to check increases very quickly.
However, it turns out that many of these checks are redundant.

Theorem 3 ([36]). Let Γ be a k-isoregular graph which satisﬁes the (t−1)-vertex
condition. In order to check that Γ satisﬁes the t-vertex condition it suﬃces to
consider graph types in which each additional vertex has valency at least k + 1.

The idea behind the proof is the following: Suppose that Γ does not satisfy
the t-vertex condition. Then there is a graph type (T, x, y) such that the number
of induced subgraphs of this type does depend on the choice of x and y. We may
assume that T is maximal with this property, in other words, for any graph type
T ′ where T ′ properly containing T , the numbers are invariant. If T contains
an vertex z (other than x and y) of valency at most k, we can delete z and use
the (t − 1) vertex condition to count the resulting graph type; after that we
use the k-isoregularity to recover the number of graphs of type (T, x, y). This
contradicts the choice of T .
In fact, we will be using the following reformulation of Theorem 3:

Corollary 4.1. Let Γ be a graph which is k-isoregular, and which satisﬁes the
(t − 1)-vertex condition, but not the t-vertex condition. Then there is a graph
type (T, x, y) such that all vertices other than x and y have valency at least k +1,
and such that the number of graphs of type (T, x, y) depends on the choice of x
and y in Γ.
 6

Finally, we present a complexity result related to the t-vertex condition:

Theorem 4. For a ﬁxed integer t and a graph Γ of order n, the t-vertex con-
dition can be checked in time polynomial in n.

Proof. We may assume that t ≥ 3, and that the (t − 1)-vertex condition has
already been checked.
Fix a graph type T = (∆, z1, z2) of order t and two vertices z′
1, z′
2 of Γ.
Suppose that either both (z1, z2) is an edge in ∆ and (z′
1, z′
2) is an edge in Γ,
or both pairs are non-edges in their respective graphs. Arbitrarily label the
remaining vertices in ∆ by z3, . . . , zt.
Now we consider all sequences (z′
3, . . . , z′
t) of distinct vertices in Γ; there
are fewer than nt−2 of them. For each sequence we may consider the labelled
subgraph induced by the z′
i, 1 ≤ i ≤ t. We can check in time proportional to t2

whether φ : zi ↦→ z′
i is a graph isomorphism. Hence, in time O(nt−2t2) we can
count the graphs of type T with respect to the given vertices z′
1 and z′
2.
There are fewer than n2 possible pairs (z′
1, z′
2) of vertices. Repeating the
count for all of them gives us the numbers of graphs of type T for all these pairs
in time O(nt−2 · n2) = O(nt), since t is constant. Since there are only ﬁnitely
many graph types of order t, this proves the theorem.

5 Generalised quadrangles

Deﬁnition 5. Let P be a ﬁnite set of points. Let L be a set of distinguished
subsets of P , called lines. Suppose there are integers s and t such that

• any two lines intersect in at most one point;

• each line contains exactly s + 1 points;

• each point is contained in exactly t + 1 lines.

Then (P, L) is a partial linear space of order (s, t).

We use the traditional geometric language: Two points are collinear if they
lie on a common line; two lines are concurrent if they intersect.
Given a partial linear space, we can deﬁne a graph as follows:

Deﬁnition 6. Let (P, L) be a partial linear space. Let Γ be the graph with
vertex set P , two points being adjacent if they are collinear. Then Γ is called
the point graph of (P, L).

Generalised quadrangles are partial linear spaces which satisfy one additional
regularity property.

Deﬁnition 7. Let (P, L) be a partial linear space. Suppose that for each line l
and each point P /∈ l, there is exactly one point on l collinear to P . Then (P, L)
is a generalised quadrangle of order (s, t), or a GQ(s, t) for short.

7

Below we survey a few classical results about generalized quadrangles.

Theorem 5. The point graph of a GQ(s, t) is strongly regular, with parameters

v = (s + 1)(st + 1)
k = (s − 1)t

λ = s − 1
µ = t + 1

We now look at subgraphs of the point graphs of generalised quadrangles.

Theorem 6 (Cameron [10]). The point graph of a generalised quadrangle does
not contain K4 − e as an induced subgraph. Here, K4 − e denotes the graph
obtained by removing one edge from the complete graph on 4 vertices.

Deﬁnition 8. A triad in a GQ(s, t) is a triple {x, y, z} of pairwise non-collinear
points. A center of a triad is a point collinear to all three points of the triad.

Theorem 7 (see [35]). For a generalised quadrangle of order (s, t), we have
s2 ≥ t. Equality holds if and only if each triad has exactly s + 1 centers.

Corollary 5.1. The point graph of a generalised quadrangle of order (s, s2) is
3-isoregular.

Proof. The isomorphism class of a graph of order 3 is uniquely determined by
the number of edges. By Theorem 7, each graph with 0 edges has s + 1 common
neighbours. By Theorem 6, each graph with 2 edges has no common neighbours.
If the graph has 1 edge, two of the points are connected by a line. The
third point has exactly one neighbour on this line, which is the unique common
neighbour of all three points. Thus, a graph with 1 edge has one common
neighbour.
If the graph has 3 edges, it is complete, and hence contained in a line. The
common neighbours of the three points are the remaining s − 2 points on this
line.

6 Proof of Theorem 1

6.1 Goals and strategy

In this section we prove Theorem 1, which states that the point graph of a gen-
eralised quadrangle satisﬁes the 5-vertex condition. For generalised quadrangles
of order (s, s2), this has been previously shown by A. Pasini (unpublished [33]).
Although the proof presented here is independent, the result in [33] showed that
generalised quadrangles yield a class of strongly regular graphs which should be
further investigated. Also, some of the techniques used by Pasini helped to
obtain the result presented here.
By Theorem 3 we have to count graphs with minimal valency 3 and order 5.
In other words, if x, y are the ﬁxed vertices, and a, b, c the additional vertices,

8

we need to consider the graphs in which each of a, b, c is non-adjacent to at most
one vertex.
If we take the complements of these graphs, we get that the valency of a, b, c
is at most 1. If we discard a possible edge (x, y), that implies that the size of
the graph, i.e., the number of its edges, is at most 3. Thus, we use the following
strategy:

1. Enumerate all graphs of order 5 and size i = 0, 1, 2, 3 (Subsection 6.2);

2. Discard those graphs which cannot appear as subgraphs of generalised
quadrangles (Subsection 6.3);

3. For the few remaining graph types, check that their numbers do not de-
pend on the choice of the edge or non-edge (x, y) (Subsection 6.4).

6.2 Graph types relevant to the 5-vertex condition

We start by determining all graph types which need to be considered in order to
check whether a given graph satisﬁes the 5-vertex condition. As stated above,
the size of the complements of these graph types is bounded by 3, in other
words, the complements contain at most 3 edges.
In order to be sure not to miss anything, we will completely enumerate
these complements. In the following we enumerate the relevant graphs up to
isomorphism under the group S({x, y}) × S({a, b, c}) of order 12, counting also
the cardinalities of the related isomorphism classes. We will not consider the
set {x, y} as a possible edge. This leaves (
5
2) − 1 = 9 possible edges.
We denote graphs by a list of its edges.

Graphs of size 0

The empty graph is uniquely determined by its size.

Graphs of size 1

a. {x, a}, Aut = ⟨(b, c)⟩ , |Aut| = 2, length of orbit: 6.

b. {a, b}, Aut = ⟨(a, b), (x, y)⟩ , |Aut| = 4, length of orbit: 3.

This accounts for 6 + 3 = 9 = (
9
1
) graphs.

Graphs of size 2

a. {x, a}, {x, b}, Aut = ⟨(a, b)⟩ , |Aut| = 2, length of orbit: 6.

b. {x, a}, {y, b}, Aut = ⟨(a, b)(x, y)⟩ , |Aut| = 2, length of orbit: 6.

c. {x, a}, {b, c}, Aut = ⟨(b, c)⟩ , |Aut| = 2, length of orbit: 6.

d. {x, a}, {y, a}, Aut = ⟨(x, y), (b, c)⟩ , |Aut| = 4, length of orbit: 3.

e. {x, a}, {a, b}, Aut = ⟨e⟩ , |Aut| = 1, length of orbit: 12.

f. {a, b}, {b, c}, Aut = ⟨(a, c), (x, y)⟩ , |Aut| = 4, length of orbit: 3.

9

This accounts for 6 + 6 + 3 + 12 + 6 + 3 = 36 = (
9
2
) graphs.

Graphs of size 3

a. {x, a}, {x, b}, {x, c}, Aut = S({a, b, c}, |Aut| = 6, length of orbit: 2.

b. {x, a}, {x, b}, {y, c}, Aut = ⟨(a, b)⟩, |Aut| = 2, length of orbit: 6.

c. {x, a}, {x, b}, {y, a}, Aut = ⟨e⟩, |Aut| = 1, length of orbit: 12.

d. {x, a}, {x, b}, {a, b}, Aut = ⟨(a, b)⟩, |Aut| = 2, length of orbit: 6.

e. {x, a}, {x, b}, {a, c}, Aut = ⟨e⟩, |Aut| = 1, length of orbit: 12.

f. {x, a}, {y, a}, {a, b}, Aut = ⟨(x, y)⟩, |Aut| = 2, length of orbit: 6.

g. {x, a}, {y, a}, {b, c}, Aut = ⟨(x, y), (b, c)⟩, |Aut| = 4, length of orbit:
3.

h. {x, a}, {y, b}, {a, b}, Aut = ⟨(a, b)(x, y)⟩, |Aut| = 2, length of orbit:
6.

i. {x, a}, {y, b}, {a, c}, Aut = ⟨e⟩, |Aut| = 1, length of orbit: 12.

j. {x, a}, {a, b}, {a, c}, Aut = ⟨(b, c)⟩, |Aut| = 2, length of orbit: 6.

k. {x, a}, {a, b}, {b, c}, Aut = ⟨e⟩, |Aut| = 1, length of orbit: 12.

l. {a, b}, {a, c}, {b, c}, Aut = ⟨(x, y), (a, b), (a, b, c)⟩, |Aut| = 12, length
of orbit: 1.

This accounts for 2 + 4 · 12 + 5 · 6 + 3 + 1 = 84 = (
9
3
) graphs. This check
sum conﬁrms that our enumeration is complete.

The following graphs can be discarded because one of the additional vertices
has valency greater than 1: 2.d–f, 3.c–l
This can be summarised as follows (recall that above we enumerated the
complements of the relevant graphs):

Theorem 8. If a graph Γ satisﬁes the 4-vertex condition, then to check the
5-vertex condition it is suﬃcient to count the graphs of the eight types given
in Table 1. Here, a dashed line indicates an optional edge connecting the ﬁxed
vertices.

6.3 Easily discarded cases

We now proceed to apply the results obtained above to point graphs of gener-
alised quadrangles. In this case, most of these graph types can be discarded
since they contain a subgraph K4 − e, which cannot happen in a generalised
quadrangle (see Theorem 6).

Lemma 6.1. In a generalised quadrangle, the following graph types do not
appear: 1a, 1b, 2b, 2c, 3b.
 10

    
          
     

    

x y
0 1a 1b

2a 2b 2c

3a 3b

x y x y x y

x y x y

Table 1: Types to check for 5-vertex condition

11

Proof. In the pictures of Table 1, we denote the ﬁxed vertices left to right by
x, y, and the additional vertices left to right by a, b, c. For each of the graph
types, we note a set of vertices which induces a K4 − e:

1a: x, a, b, c

1b: x, a, b, c

2b: x, a, b, c

2c: y, a, b, c

3b: y, a, b, c

So these types do not occur, independent of whether x and y are adjacent.

6.4 The remaining cases

This leaves us to check the following types: 0, 2a, 3a.
We will now show that the numbers for these subgraphs are uniquely deter-
mined by the axioms of generalised quadrangles. We will arrange these veriﬁ-
cations in three lemmas, one for each type.

Lemma 6.2. The number of graphs of type 0 w.r.t. x and y is (
s−1
3 ) if x ∼ y,
0 otherwise.

Proof. If x ̸∼ y, then the graph contains a K4 − e. Otherwise, each additional
vertex is adjacent to both x and y and hence lies on the line connecting them.
Each set of three points on this line yields a graph of type 0.

Lemma 6.3. The number of graphs of type 2a is 0 if x ∼ y. Otherwise, it is
(t + 1)
(
s−1
2 )
.

Proof. If x ∼ y, then {x, y, b, c} induces a K4 − e. Let x ̸∼ y. The points
{y, a, b, c} form a clique, hence lie on a line. Thus to ﬁnd such a graph, we
choose a line l through y, with t + 1 possibilities. The point c is the unique
neighbour of x on l; for a and b we can choose any two of the remaining points
on l.

Lemma 6.4. The number of graphs of type 3a is t(
s
3
) if x ∼ y, (t + 1)
(
s−1
3 )

otherwise.

Proof. The vertices {y, a, b, c} form a clique, hence are collinear. If x ∼ y, we
can choose any line through y but not through x; there are t such lines. We
need to choose 3 other points on this line; this gives us (s
3
) choices.
If x ̸∼ y, then we can choose any line through y (t + 1 possibilities) and then
choose any three points on that line that are not adjacent to x, giving (
s−1
3 )

choices.

We see that for all the graph types we have to check, the numbers do not
depend on the particular choice of x and y. Together with Theorem 3, this
proves Main Theorem 1.
 12

7 Proof of Theorem 2

7.1 Goals and preliminaries

For the remainder of the text, we concentrate on point graphs of generalised
quadrangles of order (s, s2). Thus, let s be ﬁxed, and let Γ be the point graph
of such a generalised quadrangle.
Suppose that Γ does not satisfy the t0-vertex condition for some value of t0.
We may assume that t0 is minimal with this property. Thus there is a graph
type (T, x0, y0) of order t0 such that the number of graphs of type T with respect
to x and y does depend on the choice of x and y. We may further assume that
T is maximal, i.e., adding an edge to T leads to a graph type such that the
corresponding number does not depend on the choice of the ﬁxed vertices.
We will try to ﬁnd a lower bound on t0; this will yield the result that Γ
satisﬁes the (t0 − 1)-vertex condition.
First, let us collect some properties of T .

Proposition 7.1. We may assume that the valency of any additional vertex in
T is at least 4.

Proof. Since Γ is 3-isoregular by Corollary 5.1, this follows from Corollary 4.1.

Lemma 7.1. T does not contain an induced subgraph isomorphic to K4 − e.

Proof. Follows from Theorem 6 and the fact that T is an induced subgraph of
Γ.

Proposition 7.2. Let X be the set of vertices adjacent to both x and y in T . If
x ∼ y, then the subgraph induced by X is complete. If x ̸∼ y, then the subgraph
induced by X is empty.

Proof. Let w and z be two distinct vertices both adjacent to each of x and y.
If exactly one of (x, y), (w, z) is an edge in T , then these four vertices induce a
graph isomorphic to K4 − e, contradicting the lemma above.

Let S be the subgraph obtained from T by deleting x and y, and all edges
incident with either x or y, see Figure 1. Then we have

• S has order t0 − 2;

• S has minimal valency at least 2;

• The vertices of valency 2 in S induce either a complete graph or an empty
graph.

• For any maximal clique C in S and any vertex z not in C, z has at most
one neighbour in C.

We now look at the possible subgraphs induced by S. In Subsection 7.2, we
look at the case that S induces a complete graph. In Subsection 7.3, we consider
the other case.
 13
 T

S

x y

Figure 1: The graphs S and T

7.2 S is complete

We ﬁrst consider the case that S induces a complete graph in T . In this case,
we can determine the number of graphs of type T , independent of the size of S.

Theorem 9. Let Γ be the point graph of a GQ(s, s2). Let (T, x, y) be a graph
type of arbitrary size t0, such that the additional vertices induce a complete graph
S in T . Then the number of graphs of type (T, x0, y0) with respect to vertices x
and y does not depend on the choice of x and y in Γ.

Proof. If S is a complete graph, then S is contained in a line, say l. Either x ∈ l
and thus is collinear to all t0 − 2 points in S, or it has at most one neighbour
in S. The same holds for y. Let dx = |T (x) ∩ S| be the number of neighbours
of x in S, and similar dy = |T (y) ∩ S|. We have that dx, dy ∈ {0, 1, t0 − 2}, and
without loss of generality we may assume that dx ≥ dy. We get six possibilities
for the pair (dx, dy), and in each case we can determine the number of graphs
of type T with respect to any pair (x, y) of distinct vertices in Γ.

(dx, dy) = (t0 − 2, t0 − 2) :

In this case, both x and y are contained in l; in particular, x ∼ y. Thus
there are (
s−1
|S| ) choices for the additional vertices.

(dx, dy) = (t0 − 2, 1) : Here, x ∈ l, y /∈ l, and the unique neighbour z of y on l
lies in S. We have to distinguish the cases x = z and x ̸= z.

14

If x ∼ y, we can choose any line l through x but not through y, which
gives s2 possibilities. Then we need to choose a subset S ⊆ l \ {x}. Hence,
altogether there are s2( s
t0−2
) such graphs.

If x ̸= z, then x ̸∼ y. In order to ﬁnd such a graph, we have to ﬁrst choose
the line l through x, which gives s2 + 1 possibilities. The point z ∈ l is
uniquely determined by y, and we need to choose the t0 − 3 remaining
vertices of S on l. Altogether, there are (s2 + 1)
( s−1
t0−3
) such graphs.

(dx, dy) = (t0 − 2, 0) : Here, x ∈ l, and the unique neighbour z of y on l does
not lie in S. In particular, x ̸∼ y.

We can choose any line l through x, and then a subset S ⊆ l avoiding
both x and the unique neighbour of y on l. Thus, the total number of
such graphs is (s2 + 1)
( s−1
t0−2
).

(dx, dy) = (1, 1) : Neither x nor y lie on l, and their unique neighbours zx and
zy lie in S. We need to distinguish four cases, according as x ∼ y, and
zx = zy.

x ̸∼ y, zx ̸= zy :

Choose any line l1 through x (s2 + 1 possibilities). On l1 we take
any other point zx which is not adjacent to y (s − 1 possibilities).
Through zx we take any line l ̸= l1 (s2 choices). On l, zx and zy are

15

ﬁxed, so we have to choose |S| − 2 additional points. Thus the total
number of such graphs is

s2(s2 + 1)(s − 1)
( s − 1
|S| − 2
)
.

x ∼ y, zx ̸= zy :

Take any line l1 through x which does not contain y (s2 choices).
Choose zx ̸= x on l1 (s choices). By construction, zx ̸∼ y. Take any
line l ̸= l1 through zx (s2 choices); this determines zy. Again, we
need to choose the remaining |S| − 2 points on l. The total number
is
 s5( s − 1
|S| − 2
)
.

x ̸∼ y, zx = zy :

We take any common neighbour z of x and y (µ choices). Through
z there are s2 − 1 lines l which do not contain x or y. On l, we need
to choose |S| − 1 additional points. Hence, we get a total number of

µ(s2 − 1)
( s
|S| − 1
)
.

x ∼ y, zx = zy :

Here, the points x, y, and zx are pairwise adjacent, hence they are
collinear. Let l1 be the line through x and y. We can choose any
third point zx on l1 (s − 1 possibilities) and any line l ̸= l1 through
zx (s2 possibilities). Finally, we need to take |S| − 1 additional points
on l. The total number is

s2(s − 1)
( s
|S| − 1

)
.

16

(dx, dy) = (1, 0) : Again, we distinguish the cases x ∼ y and x ̸∼ y.

If x ̸∼ y, we can take any line l1 through x, and choose x ̸= zx ̸∼ y.
Through zx we take any line l ̸= l1, and on l we need |S| − 1 additional
points, avoiding the neighbour of y. The total number of choices is

(s2 + 1)(s − 1)s2( s − 1
|S| − 1
)
.

If x ∼ y, we choose x ∈ lx ̸∋ y. On lx we take any point zx ̸= x. Through
zx we take any line l ̸= lx, and on l we need |S| − 1 more points, none of
which is adjacent to y. The total number is

s2 · s · s2( s − 1
|S| − 1

)
.

(dx, dy) = (0, 0) :

If x ̸∼ y, we can divide all lines in the GQ into three diﬀerent parts.
There are 2(s2 + 1) lines which pass through either x and y. On each of
the remaining lines, both x and y have one common neighbour each. Let
L1 be the set of lines where these neighbours coincide, and L2 the set of
lines where the neighbours are distinct.

Now x and y have µ common neighbours. Through each such neighbour
there are s2 − 1 lines which do not pass through either x or y. All these
lines are distinct, since otherwise, x would have two neighbours on one line.
Hence, we get that |L1| = µ(s2 − 1), and thus |L2| = l − |L1| − 2(s2 + 1),
where l is the total number of lines.

In order to obtain a graph depicted above, we take any line from L1 ∪ L2.
On this line, we need to choose |S| points avoiding the neighbours of x
and y. Thus, the total number of such graphs is

|L1|( s
|S|
) + |L2|(
s − 1
|S|
 )
.

17

If x ∼ y, we distinguish four types of lines: The line l0 connecting x and
y; the set L1 of lines intersecting l0 in either x or y; the set L2 of lines
intersecting l0 in other points; and ﬁnally the set L3 of lines skew to l0.

Clearly, |L1| = 2s2. There are s − 1 additional points on l0; through each
of them, there are s2 lines distinct from l0. All these lines are distinct,
since otherwise, two lines would intersect in more than one point. Hence
we get that |L2| = s2(s − 1), and hence, |L3| = l − 1 − |L1| − |L2|.

Now, by a similar reasoning as above, we get that the total number of
graphs is
 |L2|( s
|S|
) + |L3|(
s − 1
|S|
 )
.

This completes the proof.

7.3 S is not complete

Recall that S is a set of t0 − 2 vertices in the graph T of order t0.

Proposition 7.3. S does not contain a clique of size t0 − 3.

Proof. If S contains only one point z not contained in a maximal clique C, then
z has to have two neighbours in C, which is a contradiction.

Proposition 7.4. S does not contain a clique of size t0 − 4.

Proof. Suppose that S contains such a clique C′, and that it contains two more
vertices, w and z. By the condition on the minimal valency, w and z are
adjacent, and both have exactly one neighbour in C′. Moreover, in T , they
are both adjacent to each of x and y, forcing x ∼ y. Thus, in T , we have two
cliques, C′ of size t0 − 4, and C = {x, y, w, z} of size 4.
Let l be the line in the generalised quadrangle containing C, and let l′ be the
line connecting x and y. The latter is uniquely determined. Denote the unique
neighbours of x, y, w, z on l′ by x
′, y′, w′, z′ respectively.
If w′ = z′, then l and l′ intersect, and x
′ = y′ = w′ ∈ C′. In this case, we can
count the graphs as follows: We select w and z on the line connecting x and y.
The intersection point x
′ has to lie on l \ C, which gives s − 3 choices. There are
s2 other lines through x
′; we choose one of them and then select t0 −5 additional
points on this line. Altogether, we get (
s−1
2 )
(s − 3)s2( s
t0−5
) such graphs.

18

x y w z

l

If w′ ̸= z′, then l and l′ do not intersect, and hence x
′, y′, w′, z′ are all
distinct. We choose the points w and z on l, and a line l′ not intersecting l. The
points w′ and z′ are uniquely determined; we can choose the remaining points
according to whether or not x
′ and y′ are in C′. In each case, we can count
easily how many graphs we obtain.
Thus, the number of graphs of type T with respect to x and y does not
depend on the choice of x and y, which is a contradiction to the choice of T .

Collecting what we have so far, we get:

Corollary 7.1. S is a graph of order t0 − 2 of minimal valency at least 2 not
containing a t0 − 4 clique.

Corollary 7.2. t0 ≥ 7.

Proof. By the minimal valency condition, S contains an edge, i.e., a 2-clique.
Thus t0 − 4 > 2.

We now consider how many vertices in S can have valency 2.

Proposition 7.5. If x ∼ y, then there are at most three vertices in S of valency
2.

Proof. In this case, the vertices of valency 2 induce a complete graph by Propo-
sition 7.2.

Proposition 7.6. If x ̸∼ y, then there are at least two vertices with valency at
least 3.

Proof. In this case, the vertices of valency 2 induce an empty graph by Proposi-
tion 7.2. Each one has to have two neighbours, which necessarily have a valency
greater than 2.

Proposition 7.7. Let x ̸∼ y. Let z be a vertex of valency 3 in S. Then z can
be adjacent to at most one vertex of valency 2.

Proof. Let z be a vertex of valency 3. In T it has to be adjacent to at least one
of x and y; let us assume that z ∼ x. Let v and w be two vertices of valency
2 adjacent to z; this implies v ̸∼ w. Both v and w have to be adjacent to x,
which implies that {x, z, v, w} induces a K4 − e.

Proposition 7.8. The case t0 = 7 is impossible.

19

Figure 2: Graphs relevant to the 8-vertex condition

Proof. Assume that t0 = 7, i.e., S has t0 − 2 = 5 vertices. Then S does not
contain a 3-clique. Let z be a vertex with maximal valency in S. Then z has at
least 3 neighbours. These neighbours must be mutually non-adjacent to avoid
a 3-clique. Since they have valency at least 2, they are all adjacent to one
additional vertex. Since this accounts for 5 vertices, there are no additional
vertices or edges in S.
However, now z has valency 3, and it is adjacent to three non-adjacent
vertices of valency 2, which is a contradiction.

Thus we have proved Theorem 2.

Corollary 7.3. The constant t0 in Klin’s Conjecture is at least 8.

Proof. There are generalised quadrangles of order (s, s2) for some prime powers
s ≥ 5 with intransitive automorphism groups, see [34].

8 Towards the 8-vertex condition

For the 8-vertex condition, we have to consider a 6-vertex graph S satisfying
all the conditions stated in the previous section. A computer search has been
performed, and the result is that there are 5 diﬀerent graphs to consider: The
complete bipartite graphs K3,3 and K4,2; the graph K3,3 − e obtained by remov-
ing an edge from the complete bipartite graph; the triangular prism K3 ◦ K2,
and the graph obtained from the prism by removing one edge from the prism
which is not contained in a 3-clique. These graphs are shown in Figure 2.
It can be shown that the number of graphs of the types related to the prism
can be determined in a generalised quadrangle of order (s, s2). However, for the
bipartite graph types this is not the case:

20

Proposition 8.1. There is a GQ(5, 25) whose point graph does not satisfy the
8-vertex condition.

This result was obtained via computer search using known generalised quad-
rangles. The quadrangle in question is obtained using the set of matrices
{(t 3t2

0 3t3
)∣
∣
∣
∣t ∈ GF (5)
} ,

see [35] and [34] for details of this construction. Its automorphism group has sev-
eral orbits on edges, which can be distinguished by counting complete bipartite
graphs K4,4 containing a given edge.

9 Discussion

In this section we consider a number of topics which are naturally related to
the main part of the paper but which were not immediately required for our
presentation.
Nevertheless, we believe that a wider picture may be helpful for the reader.
Also credits should be given to many other researchers who were dealing with
the t-vertex condition, either explicitly or implicitly.
It is also worth mentioning that a ﬁrst draft of the result given above ap-
peared in the authors thesis [37], prepared at the University of Delaware.

9.1 More about strongly regular graphs

The classical concept of a strongly regular graph (SRG) goes back to the in-
vestigations of R.C. Bose in relation to the design of statistical experiments.
For more than two decades it was considered in terms of partially balanced
incomplete block designs, while the term itself was coined in [3].
There are a number of necessary conditions for the parameters (v, k, λ, µ) of
a putative SRG, which are formulated by means of standard (or slightly more
sophisticated) tools from spectral graph theory (cf. [6]) and which are called
feasibility conditions.
There are many known inﬁnite classes and series of SRG’s, in particular
those coming from ﬁnite permutation groups and ﬁnite geometries.
There is a continuous interest to know all SRG’s (up to isomorphism) for a
given feasible parameter set. A lot of such information is accumulated on the
home page of Andries Brouwer [5].
On the other hand there exist so-called proliﬁc constructions of SRG’s (in
the sense of [9]); this usually means that for a given inﬁnite series of feasible
parameter sets the number of SRG’s grows exponentially. Techniques to present
such proliﬁc constructions were suggested by W.D. Wallis and developed quite
essentially by D. Fon-Der-Flaass and M. Muzychuk, see [31].
The discovery of proliﬁc constructions put a ﬁnal dot in the understanding
of the fact that the full classiﬁcation of SRG’s is a hopeless problem.

21

One who is interested in “nice” SRG’s is forced to rigorously formulate addi-
tional requirements to the considered objects, using suitable group-theoretical
or combinatorial language.

9.2 k-isoregular graphs

The concept of a k-isoregular graph has two independent origins, both related to
the investigation of rank 3 permutation groups. The ﬁrst origin is the Ph.D. the-
sis of J.M.J. Buczak (1980), fulﬁlled at Oxford. The main results of this thesis
were brieﬂy mentioned in Section 8 of [8], while the text itself was not available
to M. Klin and his colleagues for three decades.
The other origin is the paper [17], where all absolutely homogeneous graphs
were classiﬁed and ﬁrst steps were taken towards the investigation of k-homo-
geneous graphs for k ≥ 2; note that 2-homogeneous graphs are exactly rank 3
graphs.
It should be mentioned that the investigation of absolutely homogeneous
graphs was an attractive goal for many other researchers. More or less at the
same time the full classiﬁcation was suggested in publications by G. Cherlin,
A.D. Gardiner, H. Enomoto, Ch. Ronse, J. Sheehan and others, see, e.g., the
detailed bibliography in the book [12].
It was Ja. Gol’fand who ﬁrst realized that the concept of a k-homogeneous
graph may be approximated in purely combinatorial terms bz k-isoregular graphs.
In particular, absolutely regular graphs coincide with the absolutely homoge-
neous graphs, and the proof of this fact may be achieved without any use of
group-theoretical arguments. An outline of the proof (due to Gol’fand) is pre-
sented in the Section 4.3 of [28].
In fact, the history of this proof is just a small visible part of the related
drama of ideas. Around 1979-80 Gol’fand prepared a manuscript with the claim
that each 5-regular graph is absolutely regular. Unfortunately a fatal mistake
(discovered by M. Klin) appeared on the very last page of this detailed text.
However, all previous results in this ingenious text were correct, thus the real
claim obtained by Gol’fand was the description of two putative inﬁnite classes of
parameter sets for 4-regular graphs. One class corresponds to absolutely regular
graphs, while the other class, denoted M (r) by Gol’fand, was presenting an
inﬁnite series of possible parameters. The graph M (1) in this series corresponds
to the famous Schl¨aﬂi graph on 27 vertices, while M (2) is the unique McLaughlin
graph with the parameters (275, 112, 30, 56). The existence of the graphs M (r)
for r ≥ 3 remained open. (A brief introduction about this series is also available
in [28].)
Klin and his colleagues made a lot of eﬀorts to convince Gol’fand to publish
his brilliant result (without the ﬁnal page), however they never succeeded.
Gol’fand spent many years in attempts to reach the full desired result. After
the collapse of the USSR he lived in relative poverty. At the end of the century
he was killed in his apartment under unclear circumstances.
Around 1995, when he was still alive, Klin and Woldar established an at-
tempt to publish a series of papers, starting from Gol’fand’s text as Part I and

22

with [27] as Part II. Unfortunately after Gol’fand’s death the fate of his her-
itage still remains indeﬁnite, this is one of the reasons why the work over the
unﬁnished text [27] was conserved.
It should be mentioned that the original term k-regular suggested by Gol’fand
lead to possible confusion. Indeed, for many researchers in graph theory, k-
regular means regular of valency k. This is why Klin and Woldar in [27] decided
to use the new term k-isoregular, which does not imply any confusion.
We refer to [36] for all necessary precise formulations related to the concept
of k-isoregularity.
One more approach, inﬂuenced by the consideration of graphs with the t-
vertex condition is developed in publications by J. Wojdylo, see [40] for example.

9.3 Smith graphs

In 1975 a few papers were published by M. Smith, see for example [38], devoted
to rank 3 permutation groups with the property that each of the two transitive
subconstituents is also a rank 3 group. All possible feasible parameters for the
corresponding SRG’s were presented in evident form. At that time the result
was regarded as a program for further attacks toward a better understanding of
such graphs. A few years later, with the announcement of the classiﬁcation of
ﬁnite simple groups, this research program became obsolete.
Since that time any SRG with the parameters described by Smith is called
a Smith graph, be it rank 3 or not. A great signiﬁcance of Smith graphs in
the current context follows from the the paper [11], in which those SRG’s were
investigated for which for each vertex x both induced subgraphs Γ1(x) and Γ2(x)
are also SRG’s. It is easy to check that this class of graphs strictly coincides
with 3-isoregular graphs. (Note that the complete graph and the empty graph
may be regarded as degenerate SRG’s.)
The main result in [11] claims that each 3-isoregular graph is either the
pentagon, a pseudo Latin square or negative Latin square graph, or (up to com-
plement) a Smith graph. Another signiﬁcant ingredient of [11] is the established
link of the class of 3-isoregular graphs with extremal properties of the Krein pa-
rameters of SRG’s and spherical t-designs (this link will be brieﬂy mentioned in
Section 9.6).
We should also mention Section 8 of [11] which deals with generalised quad-
rangles of order (q, q2). It was proved there that such geometrical structures
coexist with orthogonal arrays of strength 3 and order q, as well as with certain
codes over an alphabet with q letters. This coexistence creates an additional
challenge for the reader to try to obtain our main result in absolutely diﬀerent
context, relying only on the geometrical analysis of the related codes.
We wish also to mention that 3-isoregular graphs are frequently called triply
regular graphs, which from time to time are subject of ongoing research, see
[18]. Hopefully this section of our paper will help the modern investigators to
better comprehend all the facets of these striking combinatorial objects.
The concept of a 3-isoregular graph can be generalised to an arbitrary sym-
metric association scheme. In this more general approach links with spherical

23

designs are well visible, see [39].

9.4 The 4-vertex condition

Here we provide more details regarding the consideration of the 4-vertex condi-
tion.
The paper [22] (the last research input by Andrei Ivanov before his transfer to
the software industry) introduces two inﬁnite families of graphs on 22n vertices
via the use of suitable ﬁnite geometries. It also contains a rigorous proof of a
folklore claim that in the deﬁnition of the t-vertex condition for a regular graph
it is enough to check its fulﬁllment just on edges and non-edges (that is, the
inspection of loops is redundant).
Note that [22] contains interesting conjectures about the induces subgraphs
of his graphs which still remain unnoticed by modern researchers (although one
of the conjectures was conﬁrmed in [36]).
Besides the well-known paper [19], Higman himself was considering graphs
with the 4-vertex condition in (at least) one more paper [20]. In particular, he
considered the block graphs of Steiner triple systems with m vertices (brieﬂy
ST S(m)), which are known to be SRG’s. Highman proved that the block graph
satisﬁes the 4-vertex condition if the ST S(m) consists of the points and lines
in projective space P G(n, 2) over the ﬁeld of two elements, here, m = 2n − 1.
Besides this, the 4-condition may be satisﬁed for ST S(m), for m ∈ {9, 13, 25}.
While the cases m = 9 and m = 13 can be easily settled, the case m = 25
remained open for four decades. Following the advice of M. Klin, P. Kaski
et al obtained the negative answer (see [26]), essentially relying on the use of
computer and some extra clever ad hoc tricks (the complete enumeration of all
ST S(25) looks hopeless at the moment).
There are also known a few sporadic proper (non rank 3) SRG’s which satisfy
the 4-condition. The smallest such graphs have 36 vertices, they were carefully
investigated in [29].

9.5 Generalisations for association schemes

Every SRG Γ together with the complement Γ forms a symmetric association
scheme with two classes (or of rank 3). Therefore it is natural to consider the
concept of the t-vertex condition for arbitrary association schemes.
Non-symmetric schemes with two classes are equivalent to pairs of com-
plementary doubly regular tournaments. Each such (skew-symmetric) scheme
satisﬁes the 4-vertex condition [32].
The situation for higher ranks is much more sophisticated and goes beyond
the scope of this survey. The ﬁrst results in this direction were presented in [16]
and [7], though without the evident use of association schemes. Further steps
stem from [14].
 24

9.6 Interactions with other problems

During the last two decades highly symmetrical assocaiation schemes, and in
particular SRG’s, were used quite essentially in a number of signiﬁcant research
approaches in diverse parts of mathematics. For each such case it is not so easy
to recognize immediately which properties of the related graphs or schemes are
exactly requested. The reason of diﬃculties is as a rule a serious discrepancy in
the languages adopted in the corresponding parts of mathematics.
A few examples are brieﬂy mentioned below, each together with at least one
striking reference.
Two decades ago F. Jaeger demonstrated in [24] how one could produce
spin models for the applications in the theory of link invariants (in the sense
of V.R.F. Jones), using suitable self-dual association schemes. The requested
SRG’s should be 3-isoregular.
The problem of description of ﬁnite point systems in Euclidean space which
satisfy some energy minimization criteria was attacked by H. Cohn et al in a
number of publications throughout the last decade. Surprisingly, they estab-
lished links of putative optimal systems with some famous SRG’s, among them
there are a few 3-isoregular graphs, see [13].
Deterministic polynomial factoring is considered in the framework of m-
schemes as they are called in [23]. In fact, this class of objects is strictly re-
lated to diverse kinds of highly symmetrical association schemes (as they were
mentioned in Section 9.5). The recent thesis [1] is a good source to digest
sophisticated interactions, which appear in this new line of research.
Spherical designs are intimately related to the existence of some classes of
SRG’s, in particular to putative 3- and 4-isoregular graphs. The survey [13] may
be helpful as an initial introduction. In this context, the negative results pre-
sented in [2] imply the non-existence of inﬁnitely many 4-isoregular graphs. This
is, in a sense, a partial fulﬁlment of the foremost dream of the late Ja. Gol’fand.
It should be mentioned that such an implication is not immediately visible for
a non-perplexed reader.

10 Conclusion

We have shown that the point graphs of generalised quadrangles of order (s, s2)
satisfy the 7-vertex condition. This provides us with an inﬁnite family of
strongly regular graphs satisfying that condition which have intransitive au-
tomorphism groups.
Hence, if Klin’s Conjecture holds (i.e., if there is a number t0 such that the
t0-vertex condition implies a rank 3 automorphism group) then t0 ≥ 8.
Still, the proof of this conjecture in its full generality appears intractable. If
we restrict ourselves to point graphs of generalised quadrangles, then it looks
reasonable to prove a similar statement, in particular since many characteriza-
tion of the “classical” generalised quadrangles (which include those with a rank
3 group) are known.
 25

References

[1] Manuel Arora. Extensibility of Association Schemes and GRH-Based Deter-
ministic Polynomial Factoring. PhD thesis, Rheinische Friedrich-Wilhelms-
Universit¨at, Bonn, 2013.
http://nbn-resolving.de/urn:nbn:de:hbz:5n-31587.

[2] E. Bannai, A. Munemasa, and B. Venkov. The nonexistence of certain tight
spherical designs. Algebra i Analiz, 16(4):1–23, 2004.

[3] R. C. Bose. Strongly regular graphs, partial geometries and partially bal-
anced designs. Paciﬁc J. Math., 13:389–419, 1963.

[4] A. E. Brouwer, A. V. Ivanov, and M. H. Klin. Some new strongly regular
graphs. Combinatorica, 9(4):339–344, 1989.

[5] A.E. Brouwer. Homepage. http://www.win.tue.nl/~aeb.

[6] Andries E. Brouwer and Willem H. Haemers. Spectra of graphs. Universi-
text. Springer, New York, 2012.

[7] Jin-Yi Cai, Martin F¨urer, and Neil Immerman. An optimal lower bound on
the number of variables for graph identiﬁcation. Combinatorica, 12(4):389–
410, 1992.

[8] P. J. Cameron and J. H. van Lint. Designs, graphs, codes and their links.
London Mathematical Society Student Texts. Cambridge University Press,
1991.

[9] Peter J. Cameron and Dudley Stark. A proliﬁc construction of strongly
regular graphs with the n-e.c. property. Electron. J. Combin., 9(1):Research
Paper 31, 12 pp. (electronic), 2002.

[10] P.J. Cameron. Partial quadrangles. Quart. J. Math., 26:61–73, 1975.

[11] P.J. Cameron, J.M. Goethals, and J.J. Seidel. Strongly regular graphs
having strongly regular subconstituents. J. Algebra, 55:257–280, 1978.

[12] Gregory L. Cherlin. The classiﬁcation of countable homogeneous directed
graphs and countable homogeneous n-tournaments, volume 131. Mem.
Amer. Math. Soc., 1998.

[13] Henry Cohn and Abhinav Kumar. Universally optimal distribution of
points on spheres. J. Amer. Math. Soc., 20(1):99–148, 2007.

[14] Sergei Evdokimov and Ilia Ponomarenko. On highly closed cellular algebras
and highly closed isomorphisms. Electron. J. Combin., 6:Research Paper
18, 31 pp. 1999.
 26

[15] I. A. Faradˇzev, M. H. Klin, and M. E. Muzichuk. Cellular rings and groups
of automorphisms of graphs. In Investigations in algebraic theory of com-
binatorial objects, volume 84 of Math. Appl. (Soviet Ser.), pages 1–152.
Kluwer Acad. Publ., Dordrecht, 1994.

[16] Martin F¨urer. A counterexample in graph isomorphism testing. Technical
Report CS-87-36, Dept. of Computer Science, Pennsylvania State Univer-
sity, 1987.

[17] Ja. Ju. Gol′fand and M. H. Klin. On k-homogeneous graphs. In Algorith-
mic studies in combinatorics (Russian), pages 76–85, 186 (errata insert).
“Nauka”, Moscow, 1978.

[18] Krystal J. Guo. Triply regular graphs, 2011.
http://www.sfu.ca/~krystalg/triplyregular.pdf.

[19] M.D. Hestenes and D.G. Higman. Rank 3 groups and strongly regular
graphs. SIAM Amer. Math.Soc. Proc., 4:141–160, 1971.

[20] D. G. Higman. Partial geometries, generalized quadrangles and strongly
regular graphs. In Atti del Convegno di Geometria Combinatoria e sue Ap-
plicazioni (Univ. Perugia, Perugia, 1970), pages 263–293. Ist. Mat., Univ.
Perugia, Perugia, 1971.

[21] A.V. Ivanov. Non-rank-3 strongly regular graphs with the 5-vertex condi-
tion. Combinatorica, 9(3):255–260, 1989.

[22] A.V. Ivanov. Two families of strongly regular graphs with the 4-vertex
condition. Discrete Math., 127:221–242, 1994.

[23] G´abor Ivanyos, Marek Karpinski, and Nitin Saxena. Schemes for deter-
ministic polynomial factoring. In ISSAC 2009—Proceedings of the 2009
International Symposium on Symbolic and Algebraic Computation, pages
191–198. ACM, New York, 2009.

[24] Fran¸cois Jaeger. Strongly regular graphs and spin models for the Kauﬀman
polynomial. Geom. Dedicata, 44(1):23–52, 1992.

[25] William M. Kantor and Robert A Liebler. The rank 3 permutation rep-
resentations of the ﬁnite classical groups. Transactions AMS, 271(1):1–71,
1982.

[26] Petteri Kaski, Mahdad Khatirinejad, and Patric R. J. ¨Osterg˚ard. Steiner
triple systems satisfying the 4-vertex condition. Des. Codes Cryptogr.,
62(3):323–330, 2012.

[27] M. Klin and A.Woldar. On 4-isoregular graphs, II. 4-isoregularity of the
McLaughlin graph. Manuscript.
 27

[28] M. Ch. Klin, R. P¨oschel, and K. Rosenbaum. Angewandte Al-
gebra f¨ur Mathematiker und Informatiker. VEB Deutscher Verlag
der Wissenschaften, Berlin, 1988. Einf¨uhrung in gruppentheoretisch-
kombinatorische Methoden. [Introduction to group-theoretical combinato-
rial methods].

[29] Mikhail Klin, Mariusz Meszka, Sven Reichard, and Alex Rosa. The smallest
non-rank 3 strongly regular graphs which satisfy the 4-vertex condition.
Bayreuth. Math. Schr., 74:145–205, 2005.

[30] M.W. Liebeck and J. Saxl. The ﬁnite primitive permutation groups of rank
three. Bull. London Math. Soc, 18:165–172, 1986.

[31] Mikhail Muzychuk. A generalization of Wallis-Fon-Der-Flaass construction
of strongly regular graphs. J. Algebraic Combin., 25(2):169–187, 2007.

[32] Dmitrii V. Pasechnik. Skew-symmetric association schemes with two classes
and strongly regular graphs of type L2n−1(4n − 1). Acta Appl. Math., 29(1-
2):129–138, 1992. Interactions between algebra and combinatorics.

[33] A. Pasini. Private communication to M. Klin, Oberwolfach, 1991.

[34] S.E. Payne. Collineations of the generalized quadrangles associated with
q-clans. Ann. Discrete Math., 52:449–461, 1992.

[35] S.E. Payne and J.A. Thas. Finite Generalized Quadrangles. Research Notes
in Mathematics. Pitman, 1984.

[36] S. Reichard. A criterion for the t-vertex condition of graphs. J. Comb. Th.
A, 90:304–314, 2000.

[37] S. Reichard. Computational and Theoretical Analysis of Coherent Con-
ﬁgurations and Related Incidence Structures. PhD thesis, University of
Delaware, Newark, DE, Summer 2003.

[38] M. S. Smith. On rank 3 permutation groups. J. Algebra, 33:22–42, 1975.

[39] Sho Suda. Coherent conﬁgurations and triply regular association schemes
obtained from spherical designs. J. Combin. Theory Ser. A, 117(8):1178–
1194, 2010.

[40] Jerzy Wojdy lo. Relation algebras and t-vertex condition graphs. European
J. Combin., 19(8):981–986, 1998.
 28
