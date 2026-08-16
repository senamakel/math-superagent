<!-- source: https://arxiv.org/pdf/1212.4175 | converted from PDF -->

The graph formulation of the union-closed sets
conjecture

Henning Bruhn1, Pierre Charbit
2, Oliver Schaudt1, and Jan Arne
Telle∗3

1IMJ, Universit´e Pierre et Marie Curie
2LIAFA, Universit´e Paris Diderot
3Department of Informatics, University of Bergen

Abstract

In 1979 Frankl conjectured that in a ﬁnite non-trivial union-closed
collection of sets there has to be an element that belongs to at least half
the sets. We show that this is equivalent to the conjecture that in a ﬁnite
non-trivial graph there are two adjacent vertices each belonging to at most
half of the maximal stable sets. In this graph formulation other special
cases become natural. The conjecture is trivially true for non-bipartite
graphs and we show that it holds also for the classes of chordal bipar-
tite graphs, subcubic bipartite graphs, bipartite series-parallel graphs and
bipartitioned circular interval graphs.

1 Introduction

A set X of sets is union-closed if X, Y ∈ X implies X ∪ Y ∈ X . The following
conjecture was formulated by Peter Frankl in 1979 [8].

Union-closed sets conjecture. Let X be a ﬁnite union-closed set of sets with
X ̸= {∅}. Then there is a x ∈ ⋃
X∈X X that lies in at least half of the members
of X .

In spite of a great number of papers, see e.g. the good bibliography of
Markovi´c [16] for papers up to 2007, this conjecture is still wide open. Sev-
eral special cases are known to hold, for example when | ⋃
X∈X X| is upper
bounded, with current best being 11 by Boˇsnjak and Markovi´c [1], or when |X |
is upper bounded, with current best being 46. This follows from a lemma by
Lo Faro [7], and independently by Roberts and Simpson [22]. The conjecture
also holds when certain sets are present in X , such as a set of size 2 as shown
by Sarvate and Renaud [24]. Possibly as a reﬂection of its general diﬃculty,
Gowers [10] suggested that work on this conjecture could fruitfully be done as
a collaborative Polymath project. See [2] for a survey of the literature on the
union-closed sets conjecture.

∗Part of this research done while visiting LIAFA in 2011

1arXiv:1212.4175v2  [math.CO]  16 May 2013
Various equivalent formulations have been discovered. We mention in par-
ticular Poonen [18] who translates the conjecture into the language of lattice
theory. Several subsequent results together with their proofs belong to lattice
theory, for example Reinhold [21] who proves this conjecture for lower semi-
modular lattices. A version of the conjecture is also known for hypergraphs; see
El-Zahar [6].
In this paper we give a formulation of the conjecture in the language of graph
theory. A set of vertices in a graph is stable if no two vertices of the set are
adjacent. A stable set is maximal if it is maximal under inclusion, that is, every
vertex outside has a neighbour in the stable set.

Conjecture 1. Let G be a ﬁnite graph with at least one edge. Then there will
be two adjacent vertices each belonging to at most half of the maximal stable
sets.

Note that Conjecture 1 is true for non-bipartite graphs. Indeed, if vertices
u and v are adjacent there is no stable set containing them both and so one
of them must belong to at most half of the maximal stable sets. An odd cycle
will therefore imply the existence of two adjacent vertices each belonging to at
most half of the maximal stable sets. The conjecture is for this reason open
only for bipartite graphs. Moreover, in a connected bipartite graph, for any
two vertices u and v in diﬀerent bipartition classes we have a path from u to v
containing an odd number of edges, so that if u and v each belongs to at most
half the maximal stable sets there will be two adjacent vertices each belonging
to at most half the maximal stable sets. Conjecture 1 is therefore equivalent to
the following.

Conjecture 2. Let G be a ﬁnite bipartite graph with at least one edge. Then
each of the two bipartition classes contains a vertex belonging to at most half of
the maximal stable sets.

In this paper we show that Conjectures 1 and 2 are equivalent to the union-
closed sets conjecture. The merit of this graph formulation is that other special
cases become natural, in particular subclasses of bipartite graphs. We show that
the conjecture holds for the classes of chordal bipartite graphs and bipartitioned
circular interval graphs, and for subcubic and series-parallel bipartite graphs.
Moreover, the reformulation allows to test Frankl’s conjecture in a probabilistic
sense: In [3] it is shown that almost every random bipartite graph satisﬁes
Conjecture 2 up to any given δ > 0, that is, almost every such graph contains
in each bipartition class a vertex for which the number of maximal stable sets
containing it is at most 1
2 + δ times the total number of maximal stable sets.

Stable sets are also called independent sets, with the maximal stable sets
being exactly the independent dominating sets. A stable set of a graph is a
clique of the complement graph and the graph formulation of the conjecture can
also be stated in terms of maximal cliques, instead of maximal stable sets. The
set of all maximal stable sets of a bipartite graph, or rather maximal complete
bipartite cliques (bicliques) of the bipartite complement graph, was studied by
Prisner [19] who gave upper bounds on the size of this set, also when excluding
certain subgraphs. More recently, Duﬀus, Frankl and R¨odl [5] and Ilinca and
Kahn [12] investigate the number of maximal stable sets in certain regular and

2

biregular bipartite graphs. In work related to the graph parameter boolean-
width, Rabinovich, Vatshelle and Telle [20] study balanced bipartitions of a
graph that bound the number of maximal stable sets. However, we have not
found in the graph theory literature any previous work focusing on the number
of maximal stable sets that vertices belong to.

2 Equivalence of the conjectures

For a subset S of vertices of a graph we denote by N (S) the set of vertices
adjacent to a vertex in S. All our graphs will be ﬁnite, and whenever we consider
a union-closed set X of sets, it will be a ﬁnite set, all of whose member-sets will
be ﬁnite as well. As Poonen [18] observed the latter assumption does not restrict
generality, while the conjecture becomes false if X is allowed to have inﬁnitely
many sets.
We need two easy lemmas. The proof of the ﬁrst is trivial.

Lemma 3. Let G be a bipartite graph with bipartition U, W , and let S be a
maximal stable set. Then S = (U ∩ S) ∪ (W \ N (U ∩ S)).

Lemma 4. Let G be a bipartite graph with bipartition U, W , and let S and T
be maximal stable sets. Then (U ∩ S ∩ T ) ∪ (W \ N (S ∩ T )) is a maximal stable
set.

Proof. Clearly, R = (U ∩ S ∩ T ) ∪ (W \ N (S ∩ T )) is stable. Trivially, any vertex
in W \ R has a neighbour in R. A vertex u in U \ R does not lie in S or not in T
(perhaps, it is not contained in either), let us say that u /∈ T . As T is maximal,
u has a neighbour w ∈ W ∩ T . This neighbour w cannot be adjacent to any
vertex in U ∩ S ∩ T as T is stable. So, w belongs to R as well, which shows that
R is a maximal stable set.

For a ﬁxed graph G let us denote by A the set of all maximal stable sets,
and for any vertex v let us write Av for the sets of A that contain v and Av for
the sets of A that do not contain v. Let us call a vertex v rare if |Av| ≤ 1
2 |A|.

Theorem 5. Conjecture 2 is equivalent to the union-closed sets conjecture.

Proof. Let us consider ﬁrst a union-closed set X ̸= {∅}, which, without restrict-
ing generality, we may assume to include ∅ as a member. We put U = ⋃
X∈X X
and we deﬁne a bipartite graph G with vertex set U ∪ X , where we make X ∈ X
adjacent with all u ∈ X.
Now we claim that τ : S ↦→ U \ S is a bijection between A and X . First
note that indeed τ (S) ∈ X for every maximal stable set: Set A = U ∩ S and
B = X ∩ S. If U ⊆ S then U \ S = ∅ ∈ X , by assumption. So, assume
U ⊈ S, which implies B ̸= ∅. As S is a maximal stable set, it follows that
U \ S = U \ A = N (B). On the other hand, N (B) is just the union of the
X ∈ S ∩ X = B, which is by the union-closed property equal to a set X ′ in X .
To see that τ is injective note that, by Lemma 3, S is determined by U ∩ S,
which in turn determines U \ S. For surjectivity, consider X ∈ X . We set
A = U \ N (X) and observe that S = A ∪ (X \ N (A)) is a stable set. Moreover,
as X ∈ X \ N (A) every vertex in U \ A is a neighbour of X ∈ S, which means
that S is maximal.
 3

Now, assuming that Conjecture 2 is true, there is an rare u ∈ U , that is, it
holds that |Au| ≤ 1
2 |A|. Clearly A is the disjoint union of Au and of Au, so
that |τ (Au)| = |Au| ≥ 1
2 |A| = 1
2 |X |.

As u ∈ τ (S) ∈ X for every S ∈ Au, the union-closed sets conjecture follows.

For the other direction, consider a bipartite graph with bipartition U, W and
at least one edge. Deﬁne X := {U \ S : S ∈ A}, and note that X ̸= {∅} as G
has at least two distinct maximal stable sets. By Lemma 3, there is a bijection
between X and A. Moreover, it is a direct consequence of Lemma 4 that X
is union-closed. From this, it is straightforward that Conjecture 2 follows from
the union-closed sets conjecture.

3 Application to four graph classes

For a set X of vertices we deﬁne AX to be the set of maximal stable sets
containing all of X. As before, we abbreviate A{x} to Ax.

Lemma 6. Let x be a vertex of a bipartite graph G. Then there is an injection
AN (x) → Ax.

Proof. We deﬁne

i : AN (x) → Ax, S ↦→ S \ L1 ∪ {x} ∪ (L2 \ N (S ∩ L3)),

where Li denotes the set of vertices at distance i to x. That i(S) is stable and
maximal is a direct consequence of the deﬁnition. Moreover, i(S) = i(T ) for
S, T ∈ AN (x) implies that S and T are identical outside L1 ∪ L2. Moreover, S
and T are also identical on L1 ∪ L2: First, L1 = N (x) shows that L1 lies in both
S and T . Second, since every vertex in L2 is a neighbour of one in L1 ⊆ S ∩ T ,
no vertex of L2 can lie in either of S or T . Thus, S = T , and we see that i is
an injection.

We denote by N 2(x) = N (N (x)) the second neighbourhood of a vertex
x. The following lemma generalises the observation that if a union-closed set
contains a singleton then it satisﬁes the union-closed sets conjecture:

Lemma 7. Let x, y be two adjacent vertices in a bipartite graph G with N 2(x) ⊆
N (y). Then y is rare.

Proof. From N 2(x) ⊆ N (y) it follows that every maximal stable set containing
y must contain all of N (x). Thus, Ay = AN (x), which means by Lemma 6 that
|Ay| ≤ |Ax| and as |Ay| + |Ax| ≤ |A| the lemma is proved.

We now apply the lemma to the class of chordal bipartite graphs. This is
the class of bipartite graphs in which every cycle with length at least six has a
chord.

This graph class was originally deﬁned in 1978 by Golumbic and Gross [9].
It is also known as the class of bipartite weakly chordal graphs.
A vertex v in a bipartite graph is weakly simplicial if the neighbourhoods
of its neighbours form a chain under inclusion. Hammer, Maﬀray and Preiss-
mann [11], and also Pelsmajer, Tokaz and West [17] prove the following:

4

Theorem 8. A bipartite graph with at least one edge is chordal bipartite if and
only if every induced subgraph has a weakly simplicial vertex. Moreover, such a
vertex can be found in each of the two bipartition classes.

Let us say that a bipartite graph satisﬁes Frankl’s conjecture if each of its
bipartition classes contains a rare vertex. In order to avoid repeating the trivial
condition that the graph has to contain at least one edge, we will also consider
edgeless graphs to satisfy Frankl’s conjecture.

Theorem 9. Chordal bipartite graphs satisfy Frankl’s conjecture.

Proof. For a given bipartition class, let x be a weakly simplicial vertex in it.
Among the neighbours of x denote by y the one whose neighbourhood includes
the neighbourhoods of all other neighbours of x. Then y is rare, by Lemma 7.

Going beyond chordal bipartite graphs, we quickly encounter graphs that
cannot be handled anymore by Lemma 7: No vertex in an even cycle of length
at least six can be proved to be rare by applying Lemma 7. We will, therefore,
strengthen the lemma to at least cover all even cycles.
For this, let us extend our notation a bit. For two vertices u, v let us denote
by Auv the set of S ∈ A containing both of u and v, by Auv the set of S ∈ A
containing u and but not v, and by Auv the set of S ∈ A containing neither of
u and v.

Lemma 10. Let G be a bipartite graph. Let y and z be two neighbours of a
vertex x so that N 2(x) ⊆ N (y) ∪ N (z). Then one of y and z is rare.

Proof. We may assume that |Ayz| ≤ |Ayz|. Now, from N 2(x) ⊆ N (y) ∪ N (z)
we deduce that Ayz = AN (x). Thus, by Lemma 6, we obtain |Ayz| ≤ |Ax|.
Since Ax ⊆ Ayz it follows that |Ay| = |Ayz| + |Ayz| ≤ |Ayz| + |Ayz| = |Ay|. As
|A| = |Ay| + |Ay|, we see that y is rare.

Again, the lemma generalises a fact that is well known for the set formulation
of the union-closed sets conjecture: If one of the sets in the union-closed set X
contains exactly two elements then one of the two elements will lie in at least
half of the members of X ; see Sarvate and Renaud [24].

Next we give an application of Lemma 10 to a class of graphs derived from
circular interval graphs. The class of circular interval graphs plays a funda-
mental role in the structure theorem of claw-free graphs of Chudnovsky and
Seymour [4]. Circular interval graphs are deﬁned as follows: Let a ﬁnite subset
of a circle be the vertex set, and for a given set of subintervals of the circle
consider two vertices to be adjacent if there is an interval containing them both.
This class is equivalent to what is known as the proper circular arc graphs.
Circular interval graphs are not normally bipartite. The only exceptions are
even cycles and disjoint unions of paths. Nevertheless, we may obtain a rich
class of bipartite graphs from circular interval graphs: For any circular interval
graph, partition its vertex set and delete every edge with both its endvertices in
the same class. We call any graph arising in this manner a bipartitioned circular
interval graph.

Theorem 11. Bipartitioned circular interval graph satisfy Frankl’s conjecture.

5

Figure 1: A bipartitioned circular interval graph

Proof. Consider a bipartitioned circular interval graph deﬁned by intervals I,
and let x be a non-isolated vertex of the graph.
For every neighbour u of x we choose an interval Iu ∈ I containing both x
and u. If ⋃
v∈N (x) Iv covers the whole circle, then there are already two such
intervals Iy and Iz that cover the circle. Clearly, every vertex not in the same
bipartition class as y and z is adjacent to at least one of them. In particular,
N 2(x) ⊆ N (y) ∪ N (z).
So, let us assume that there is a point p on the circle that is not covered by
any Iv, v ∈ N (x). We choose y as the ﬁrst neighbour of x from p in clockwise
direction, and z as the ﬁrst neighbour of x from p in counterclockwise direction.
Then y, v, z appear in clockwise order for every v ∈ N (x) and v′ ∈ Iy ∪ Iz for
every vertex v′ so that y, v′, z appear in clockwise order.
Let us show that again N 2(x) ⊆ N (y)∪N (z). For this consider a u ∈ N 2(x),
and a neighbour w of x that is adjacent to u. Thus, there is a J ∈ I containing
both u and w. If y, u, z appear in clockwise order, then u ∈ Iy ∪ Iz, which
implies u ∈ N (y) ∪ N (z). If not, then J meets one of y or z as y, w, z appear in
clockwise order. Thus, by virtue of J, the vertex u is adjacent to at least one
of y and z.
In both cases, we apply Lemma 10 in order to see that one of y and z is
rare. As the choice of x was arbitrary, we ﬁnd rare vertices in both bipartition
classes.

Let us now turn to subcubic bipartite graphs: Bipartite graphs in which no
vertex has a degree greater than 3.

Theorem 12. Subcubic bipartite graphs satisfy Frankl’s conjecture.

Our proof of Theorem 12 needs some preparation. Let us call a graph G re-
duced if there is no vertex v whose neighbourhood is equal to the union of neigh-
bourhoods of some other vertices. In particular, reduced graphs are twin-free,
that is, no two vertices have identical neighbourhoods. The following lemma
tells us that we may restrict our attention to reduced bipartite graphs.

Lemma 13. For any bipartite graph G there is a reduced induced subgraph G
′

so that G satisﬁes Frankl’s conjecture if G
′ satisﬁes it.

Proof. Assume there are pairwise distinct vertices u, v1, v2, . . . , vk such that
N (u) = ⋃k
i=1 N (vi). Then Au = A{v1,v2,...,vk}. Thus, if A is a maximal stable
set of G, then A − u is one of G − u, and conversely, any maximal stable set

6

A′ of G − u is already maximally stable in G if {v1, v2, . . . , vk} ̸⊆ A′; otherwise
A′ + u is a maximal stable set of G. Hence, a rare vertex of G − u is also rare
in G. The assertion is now obtained by iteratively deleting vertices such as u
from G.

Unlike the two classes above, subcubic graphs do not have an easily ex-
ploitable local structure. In particular, Lemmas 7 and 10 will have only limited
use. Nevertheless, we can verify Frankl’s conjecture by adapting two results on
the set formulation of the union-closed sets conjecture into the graph setting.
Both results, one of Vaughan and the other of Knill, have surprisingly involved
proofs. For a union-closed set X , we say that an element of ⋃ X is abundant if
the element appears in at least half of the member-sets of X .

Theorem 14 (Vaughan [25]). Let X be a union-closed set containing three
distinct sets of size 3 all of which have one element in common. Then there is
an abundant element in the union of the three sets.

While Vaughan’s theorem gives a local condition, not unlike Lemmas 7
and 10, when a particular union-closed set satisﬁes the conjecture, the following
result of Knill treats a special class of union-closed sets, which he calls graph-
generated families. In this context, we view edges of a graph H as subsets of
V (H) of size two.

Theorem 15 (Knill [14]). Given a graph H with at least one edge, let B =
{
⋃ F : F ⊆ E(H)}. Then there is an edge e ∈ E(H) such that |{S ∈ B : e ⊆
S}| ≤ |B|
2 .

Probably unaware of Knill’s result, it was restated as a conjecture by El-
Zahar [6]. Finally, as a response to El-Zahar’s paper, it was reproven by Llano,
Montellano-Ballesteros, Rivera-Campo and Strausz [15].
We ﬁrst translate Knill’s theorem to the graph setting:

Lemma 16. Let G be a twin-free bipartite graph with bipartition U ∪ W , where
every vertex in U is of degree 2. Then there is a rare vertex in U .

Proof. Again, let A be the set of maximal stable sets of G. Observe that G is
the subdivision of the graph H on vertex set W , where any two distinct vertices
x, y of H are adjacent if and only if they have a common neighbor u ∈ U in
G. As G is twin-free, every edge e = xy of H corresponds to a unique vertex
ue ∈ U with N (ue) = {x, y}.
Let B = {
⋃ F : F ⊆ E(H)}, and note that B = {NG(U ′) : U ′ ⊆ U }. We will
establish a bijection between B and A. For this, denote by A∩W the intersections
of maximal stable sets of G with W . Then we deﬁne the mapping B → A∩W by
NG(U ′) ↦→ W \ NG(U ′), for U ′ ⊆ U . As (W \ NG(U ′)) ∪ (U \ NG(W \ NG(U ′)))
is a maximal stable set, the mapping is a bijection. Recall that Lemma 3 asserts
that every maximal stable set is determined by its intersection with one of the
bipartition classes. Thus, the bijection B → A∩W extends to a bijection B → A.
In particular, |A| = |B|.
Now, for any S ∈ B there exists U ′ ⊆ U so that NG(U ′) = S. Any edge
e ∈ E(H) between vertices x, y ∈ W is contained in S if and only if x, y /∈
W NG(U ′), which means that the unique maximal stable set A ∈ A with A ∩
W = W \ NG(U ′) needs to contain ue, the vertex in U with neighbours x, y.

7

Therefore, the number of S ∈ B with e ⊆ S is equal to the number of maximal
stable sets containing ue.
Applying Theorem 15 we obtain an edge e = xy ∈ E(H) such that |{S ∈ B :
{x, y} ⊆ S}| ≤ |B|
2 . This then implies that ue lies in at most |B|
2 = |A|
2 maximal
stable sets, which completes the proof.

Proof of Theorem 12. Let G be a subcubic bipartite graph with bipartition U ∪
W , and let A be the set of maximal stable sets of G. By Lemma 13, we may
assume that G is reduced and, in particular, twin-free.
Let us prove that there is a rare vertex in U . Then, by symmetry, we know
that there must be a rare vertex in W too. If W contains a vertex of degree 1
or 2, we are done by Lemma 10. So, let us assume that every vertex in W has
degree 3.
First assume that there is a vertex u ∈ U of degree 1. Let x ∈ W be its
unique neighbor, and let y, z ∈ U be the other two neighbors of x. By Lemma 10,
y or z is rare and we are done.
Now assume that there is a vertex u ∈ U of degree 3, say N (u) = {x, y, z}.
Consider the set B = {U \ S : S ∈ A}, which is union-closed by Lemma 4. Then
N (x), N (y), N (z) ∈ B, and u ∈ N (x)∩N (y)∩N (z). Note that N (x), N (y), N (z)
are three distinct sets as G is twin-free. From Theorem 14 we know that there is
an abundant element of B in N (x) ∪ N (y) ∪ N (z), and hence this is a rare vertex
in U .
The remaining case, when every vertex in U is of degree 2 is taken care of
by Lemma 16.

Recall that a graph is called series-parallel if it does not contain K4 as a
minor. Equivalently, a graph is series-parallel if and only if it is of treewidth
at most two. Reusing some of the tools presented above, we can settle Frankl’s
conjecture for bipartite series-parallel graphs.

Theorem 17. Bipartite series-parallel graphs satisfy Frankl’s conjecture.

The following lemma gives us enough information on the local structure of
a series-parallel graph to prove the theorem with Lemmas 7 and 10.

Lemma 18 (Juvan, Mohar and Thomas [13]). Every non-empty series-parallel
graph G has one of the following:

(a) a vertex of degree at most one,

(b) two twins of degree two,

(c) two distinct vertices u, v and two not necessarily distinct vertices w, z ∈
V (G) \ {u, v} such that N (v) = {u, w} and N (u) ⊆ {v, w, z}, or

(d) ﬁve distinct vertices v1, v2, u1, u2, w such that N (w) = {u1, u2, v1, v2} and
N (vi) = {w, ui} for i = 1, 2.

Proof of Theorem 17. Let G be a non-empty bipartite series-parallel graph, say
with bipartition classes (U, W ), and we may assume that G does not contain
any isolated vertex. Our argumentation is symmetric, so it suﬃces to show that
there is a rare vertex among the vertices in U . The class of series-parallel graphs

8

is closed under induced subgraphs, and thus by Lemma 13 we may assume that
G is reduced.
Let L be the set of leaves of G, that is, the set of degree 1 vertices. If there
is a leaf in W , we obtain with Lemma 7 a rare vertex in U . So we may assume
that L ⊆ U . Let G
′ = G − L be the graph obtained by deleting all leaves. Since
L ⊆ U , every vertex in U ∩ V (G
′) is of degree at least 2. In particular, G′ is
not empty.
We claim that in G
′ there is some vertex x ∈ W of degree at most 2. If the
claim is true then Lemma 10 yields that some y ∈ NG′(x) ⊆ U is rare in G,
since every neighbour of x in G − G
′ is a leaf.
So it remains to prove the claim. Lemma 18 yields that G
′ contains one of
the conﬁgurations in (a), (b), (c), or (d). Clearly, (d) is not possible since G
′ is
bipartite and thus triangle-free.
In case (a), there is a leaf in G
′, which then needs to be contained in W
because every vertex in U ∩ V (G′) has degree at least 2. In case (b), let u, v
be the two twins of degree 2. If u, v ∈ U then u and v are twins in G as well,
which is impossible as G is reduced. Consequently, u, v ∈ W and the claim is
again veriﬁed. In the last case (c), there are two distinct vertices u, v and two
not necessarily distinct vertices w, z ∈ V (G) \ {u, v} such that N (v) = {u, w}
and N (u) ⊆ {v, w, z}. But G
′ is bipartite and so uw /∈ E(G
′). In particular,
both u and v are of degree at most two. Since u and v are adjacent, one of them
is contained in W . This completes the proof.

4 Discussion

Lemmas 7 and 10 generalise the cases when there is a vertex x of degree 1 or 2.
Then, one of the neighbours of x is rare. In contrast, the subcubic case required
a bit of work. This is because none of the neighbours of a vertex of degree at
least 3 have to be rare. An example is given in Figure 2 on the left, where
no neighbour of the vertex v is rare. Note that both graphs in Figure 2 are
subcubic.
Again, this is not new, in the sense that it corresponds directly to an ob-
servation of Sarvate and Renaud [23] in the set formulation: A set of size three
need not contain any element appearing in at least half of the member sets of
the union-closed set.

v
 Figure 2: Left: No neighbour of v is rare. Right: Lemmas 7 or 10 not applicable

As chordal bipartite graphs are exactly the (C6, C8, C10, . . .)-free graphs one
may be tempted to generalise Theorem 9 by allowing one more even cycle, the
6-cycle, as induced subgraph. While Lemma 7 is no longer strong enough even

9

for the C6, Lemma 10 easily takes care of any graph with a degree 2 vertex in
each bipartition class. In general, however, Lemma 10 turns out to be too weak
as well to prove the conjecture for (C8, C10, C12, . . .)-free graphs: The graph on
the right in Figure 2 is of that form but has no vertices covered by Lemma 10.

We contend that the results in the previous section substantiate the useful-
ness of the graph formulation of the union-closed sets conjecture. Moreover,
we believe that a good number of other graph classes should be within reach.
Does Frankl’s conjecture hold for planar graphs, regular graphs or for graphs of
treewidth 3?

References

[1] I. Boˇsnjak and P. Markovi´c, The 11-element case of Frankl’s conjecture,
Electr. J. Comb. 15 (2008), R88.

[2] H. Bruhn and O. Schaudt, The journey of the union-closed sets conjecture,
in preparation.

[3] , The union-closed sets conjecture almost holds for almost all ran-
dom bipartite graphs, preprint 2013.

[4] M. Chudnovsky and P.D. Seymour, Claw-free graphs. III. Circular interval
graphs, J. Combin. Theory (Series B) 98 (2008), no. 4, 812–834.

[5] D. Duﬀus, P. Frankl, and V. R¨odl, Maximal independent sets in bipartite
graphs obtained from boolean lattices, Eur. J. Comb. 32 (2011), no. 1, 1–9.

[6] M. El-Zahar, A graph-theoretic version of the union-closed sets conjecture,
J. Graph Theory 26 (1997), 155–163.

[7] G. Lo Faro, Union-closed sets conjecture: Improved bounds, J. Com-
bin. Math. Combin. Comput. 16 (1994), 97–102.

[8] P. Frankl, Handbook of combinatorics (vol. 2), MIT Press, Cambridge, MA,
USA, 1995, pp. 1293–1329.

[9] M.C. Golumbic and C.F. Goss, Perfect elimination and chordal bipartite
graphs, J. Graph Theory 2 (1978), 155–163.

[10] T. Gowers, Gowers’s weblog: Possible future PolyMath projects,
http://gowers.wordpress.com/2009/09/16/possible-future-polymath-
projects, 2009.

[11] P.L. Hammer, F. Maﬀray, and M. Preissmann, A characterization of
chordal bipartite graphs, Rutcor research report, Rutgers University, New
Brunswick, NJ, 1989.

[12] L. Ilinca and J. Kahn, Counting maximal antichains and independent sets,
CoRR abs/1202.4427 (2012).

[13] M. Juvan, B. Mohar, and R. Thomas, List edge-colorings of series-parallel
graphs, Electron. J. Combin. 6 (1999), 1077–8926.

10

[14] E. Knill, Graph generated union-closed families of sets,
arXiv:math/9409215v1 [math.CO], 1994.

[15] B. Llano, J.J. Montellano-Ballesteros, E. Rivera-Campo, and R. Strausz,
On conjectures of frankl and el-zahar, J. Graph Theory 57 (2008), 344–352.

[16] P. Markovi´c, An attempt at Frankl’s conjecture., Publications de l’Institut
Math´ematique. Nouvelle S´erie 81(95) (2007), 29–43.

[17] M.J. Pelsmajer, J. Tokaz, and D.B. West, New proofs for strongly chordal
graphs and chordal bipartite graphs, preprint 2004.

[18] B. Poonen, Union-closed families, J. Combin. Theory (Series A) 59 (1992),
253–268.

[19] E. Prisner, Bicliques in graphs I: Bounds on their number, Combinatorica
20 (2000), no. 1, 109–117.

[20] Y. Rabinovich, J.A. Telle, and M. Vatshelle, Upper bounds on the boolean
width of graphs with an application to exact algorithms, submitted, 2012.

[21] J. Reinhold, Frankl’s conjecture is true for lower semimodular lattices,
Graphs and Combinatorics 16 (2000), no. 1, 115–116.

[22] I. Roberts and J. Simpson, A note on the union-closed sets conjecture,
Austral. J. Combin. 47 (2010), 265–269.

[23] D.G. Sarvate and J.-C. Renaud, Improved bounds for the union-closed sets
conjecture, Ars Combin. 29 (1989), 181–185.

[24] , On the union-closed sets conjecture, Ars Combin. 27 (1989), 149–
154.

[25] T.P. Vaughan, Three-sets in a union-closed family, J. Combin. Math. Com-
bin. Comput. 49 (2004), 73–84.
 11
