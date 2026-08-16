<!-- source: https://arxiv.org/pdf/2504.02449 | converted from PDF -->

Strongly regular graphs with parameters (85, 14, 3, 2) do
not exist

Sergey Shpectorov and Tianxiao Zhao

April 4, 2025

Abstract

We investigate the second smallest unresolved feasible set of parameters of strongly
regular graphs, (v, k, λ, µ) = (85, 14, 3, 2). Using the classification of cubic graphs of small
degree, we restrict possible local structure of such a graph G. After that, we exhaustively
enumerate possible neighbourhoods of a maximal 3-clique of G and check them against
a variety of conditions, including the combinatorial ones, coming from λ = 3 and µ = 2,
as well as the linear algebra ones, utilising the Euclidean representation of G. These
conditions yield contradiction in all cases, and hence, no srg(85, 14, 3, 2) exists.

Keywords: strongly regular graph, euclidean representation

1 Introduction

In this paper we consider undirected graphs without loops and multiple edges. A strongly
regular graph is a connected regular graph G such that the number of common neighbours
of two distinct vertices u, v ∈ G depends only on whether or not u and v are adjacent.
Four parameters are used to describe the properties of a strongly regular graph G: the
number of vertices, v, the valency, k, the number of neighbours of two adjacent vertices,
λ, and the number of neighbours of two non-adjacent vertices, µ. We will use the notation
srg(v, k, λ, µ) for any strongly regular graphs with these parameters.
The four parameters are not independent; in fact, they satisfy several feasibility con-
ditions. Parameters satisfying these conditions are called feasible. Given a feasible pa-
rameter set (v, k, λ, µ), one can ask whether there is a strongly regular graph with such
parameters, and if so, how many different srg(v, k, λ, µ) are there up to isomorphism.
The answer to this question varies for different parameter sets. For some feasible
parameters, the corresponding strongly regular graphs exist and occasionally there may
be a significant number of non-isomorphic graphs with the same parameters. For other
feasible parameter sets, no srg(v, k, λ, µ) exist. In other words, feasibility of parameters
does not guarantee the existence of a strongly regular graph. All feasible parameter
sets with v ≤ 1300 are listed in an online catalogue [1] maintained by Brouwer. For each
parameter set, the catalogue lists the key properties of the graph and additional comments
describing what is currently known about this case.
We note that the complement graph of a strongly regular graph is also strongly reg-
ular, as long as it is connected. Hence, strongly regular graphs and their parameter sets
normally come in pairs. For v ≤ 100, there are only nine unresolved cases, where it is not
known whether the strongly regular graphs with the given feasible parameter set exist.
The smallest case is for v = 69 and the next three unresolved cases have v = 85. In this
paper, we resolve one of these three cases. Namely, we prove the following result.

Theorem 1.1. There is no strongly regular graph with parameters (85, 14, 3, 2).

1arXiv:2504.02449v1  [math.CO]  3 Apr 2025
The complementary array is (85, 70, 57, 60) and, clearly, such strongly regular graphs
also cannot exist. Previous knowledge about srg(85, 14, 3, 2) was very limited. Paduchikh
in [10] investigated how automorphisms of prime order could act on such a graph and
what would be the fixed subgraph of such an automorphism.
There are several ingredients to our proof of Theorem 1.1. First of all, each local
subgraph G1(x) (i.e., subgraph induced on the neighbourhood of a vertex x) of G =
srg(85, 14, 3, 2) is a cubic graph on 14 vertices. Connected cubic graphs on at most 14
vertices have been completely enumerated, see e.g., [4, 3]. Going through the list, we
determine all possible local graphs, using the additional strong condition that two non-
adjacent vertices in the local graph can have at most one common neighbour. This holds
since µ = 2. The final list of possible local graphs, called good graphs below, includes
36 connected graphs and 3 disconnected graphs, consisting of two components, a 4-clique
and a connected cubic graph on 10 vertices.
One immediate corollary of this is that G contains maximal 3-cliques. We select one
such clique, Q = {x, y, z}, and we do in the computer algebra system GAP [6] a complete
enumeration of possible subgraphs arising on the set T of vertices adjacent to Q. Since
|T | = 30, this enumeration is huge and it cannot be done carelessly. We represent T as a
union of three 12-vertex segments, Sx = G1(x) \ Q, Sy = G1(y) \ Q and Sz = G1(z) \ Q,
corresponding to the three vertices in Q. Each segment is a subgraph of a local graph,
and so possible segments can be enumerated up to isomorphism, giving us a total of 478
possible segments. Within T , two segments intersect in a 2-vertex set called a handle
(see Section 4 for all relevant definitions and discussion). A handle can be an edge or a
non-edge and this leads to a compatibility condition for pairs of segments within T . We
pre-compute the list of 86333 (ordered) pairs of compatible segments Sx ∪ Sy joined at a
handle, up to isomorphism. These pairs give us the cases into which we split the entire
calculation. In each case, the calculation goes through four steps:

• Step 1: Enumerating possible graph structures on Sx ∪ Sy.

• Step 2: Gluing in a third segment Sz in all possible compatible ways and enumerating
all graph structures on T = Sx ∪ Sy ∪ Sz. A great majority of cases are eliminated
at this step.

• Step 3: For each T not eliminated at Step 2, enumerate all possible sets C of
additional neighbours of a fixed vertex t ∈ X = Sy ∩ Sz.

• Step 4: Enumerate all possible graph structures on C and hence on the entire T ∪ C,
achieving elimination in all cases.

In addition to purely combinatorial arguments involving the parameters of G, we rely
for elimination on the linear algebra conditions coming from the Euclidean representation
of G. It is well-known that a strongly regular graph can be realised as a set of unit
vectors in an eigenspace of its adjacency matrix. The value of the dot product of two
unit vectors corresponding to vertices u and v is given in the so-called cosine sequence of
G, and it depends only on the distance between u and v in G. The eigenvalues of the
adjacency matrix of G and their multiplicities can be computed from the parameters of
G. For G = srg(85, 14, 3, 2), the adjacency matrix has eigenvalues k = 14, 4, and −3, with
respective multiplicities 1, 34, and 50. For our calculation, we selected the unit vector
realisation in the eigenspace E of dimension 34 corresponding to the eigenvalue 4. The
cosine sequence for this Euclidean representation is w0 = 1, w1 = 2
7 , and w2 = − 1
14 . That
is, adjacent vertices lead to the dot product value 2
7 and the non-adjacent vertices lead to
the value − 1
14 .
Once we know all edges on a subset X of G, such as, say, T or T ∪ C (or a subset of
these sets), we can create the Gram matrix corresponding to X. Since the dot product
is positive definite on E, the Gram matrix of every subset of G must be semi-positive
definite, i.e., it cannot have negative eigenvalues. The strength of this linear algebra
condition grows with the size of the subset X we consider. For example, none of the

2

possible sets Sx ∪ Sy (of cardinality 22) is eliminated by this condition. However, for
T = Sx ∪ Sy ∪ Sz (whose size is 30), this condition is very powerful and it eliminates
a large majority of all possible configurations of edges, depending on the specific case.
Clearly, we want to eliminate each configuration as early as possible, so we build up T
vertex by vertex and check semi-positive definiteness along the way.
Also, note that the rank of the Gram matrix cannot exceed dim E = 34. Hence, at
Step 4, where the size of T ∪ C grows to 38 > 34, the rank consideration can be applied
with a devastating effect, eventually eliminating all configurations.
While the overall idea of our four-step enumeration looks quite simple and straightfor-
ward, it was found as a result of much experimentation. Even with our approach above,
the total enumeration involves an astronomical number of possible configurations, and
so the enumeration would not have been possible without a very effective code in GAP.
Because of this, we also devote much attention below to the exact algorithmic details,
including some key data structures and even some code. We do not include the entire
code we created and used, due to its length, but it is available on GitHub [11].

Finally, let us describe the contents of the paper section by section. In Section 2, we
provide the background information on strongly regular graphs and their Euclidean rep-
resentations. In Section 3, we identify the possible local subgraphs of G = srg(85, 14, 3, 2),
starting from the known lists of cubic graphs of small size. In Section 4, we discuss the
concepts of segments and handles, which are the building blocks for our set T . We de-
termine the complete list of possible segments and classify them according to their type.
Gluing of segments over the common handles is described in Section 5, where we develop
the group-theoretic methods allowing us to avoid repetitions. This leads to finding the
list of 86333 pairs of segments glued over a common handle, which constitute the cases
into which we split the calculation. We also describe in this section the main idea of our
approach, focussing on the set T = Sx ∪ Sy ∪ Sz. Not every edge in T is contained in
one of the three segments. Hence, we study the edges that cut across segments, and we
show that such edges form a matching between the subsets in the two segments, called the
cores. This results informs the enumeration method we select, using enumeration trees.
In Section 6, we provide some data and algorithmic details: ordering of the vertices in a
segment and the resulting quad type, which accomplishes a finer classification of segments.
We also discuss in this section the overall organisation of Steps 1 and 2.
By the end of Step 2, we have already eliminated a large majority of all cases. However,
even a tiny percentage of survivors, leads to a very large number of cases, for which we
need to do further steps. In Section 7, we describe properties of the additional vertices
we add, namely to the additional neighbours of a vertex t ∈ X = Sy ∩ Sz. We identify
each additional vertex with its set of neighbours in T , discuss compatibility of additional
vertices, and provide the details of the recursive enumeration we do at Step 3. In Section
8, we similarly discuss the details of Step 4, where we have in hand a complete set C of
neighbours of t and we enumerate the possible edges on C and achieve the final elimination.
In Section 9, we describe an additional idea, based on the careful selection of the 3-clique
Q = {x, y, x}, identifying our set T . This additional idea leads to a significant overall
reduction in the number of cases we need to consider, and it also leads to a more simple
algorithm. Section 10 contains brief concluding remarks. The paper has three appendices.
Appendix A describes the enumeration trees we use at Steps 1 and 2. Appendix B deals
with the details of the LDLT algorithm we use to verify semi-positive definiteness as we
add vertices one by one. Finally, in Appendix C we describe and justify the method we
use to compute projections to E, which we use extensively at Steps 3 and 4.

The enumeration was carried out in parallel on 96 cores in four servers in the School
of Mathematics at the University of Birmingham. We especially thank David Craven,
who manages these servers and who tolerated our 96 copies of GAP, running continuously
from November 2023 till January 2025.
 3

2 Preliminaries

2.1 Graphs

In this section we will briefly introduce some background concepts and facts.
By a graph we mean a simple graph, without loops or multiple edges. We will identify
a graph G with its vertex set and will use E(G) to denote its edge set. We will only deal
with finite graphs, i.e., |G| (and hence also |E(G)|) will be finite. We call v = |G| the
order of the graph G.
For x, y ∈ G, we write x ∼ y (respectively, x ̸∼ y) to indicate that x and y are adjacent
(respectively, non-adjacent). A path from x to y is a sequence p = (x0, x1, . . . , xn) of
vertices, where x = x0, y = xn and xi−1 is adjacent to xi for all i = 1, 2, . . . , n. We call
n the length of the path p. We will typically assume that the graph is connected, that
is, any two vertices of it are connected by a path. Length of the shortest path between x
and y is known as the distance between x and y. The largest distance between vertices
of G is called the diameter of G. For i ≥ 1, by Gi(x) we mean the set of vertices of G at
distance i from x. In particular, G1(x) is the set of neighbours of x in G. Recall that G
is called k-regular if |G1(x)| = k for every x ∈ V (G). Then we call k the degree of the
regular graph G.
For X ⊂ G, we will similarly identify the subset X with the induced subgraph on X.
This is the subgraph that includes all edges with both ends in X. In particular, we will
often refer to G1(x) as the local subgraph of G.
Consider a graph G = {u1, u2, . . . , uv}. The adjacency matrix A = A(G) is the square
matrix of size v, whose entries satisfy:

aij = { 1, if ui ∼ uj,
0, if ui ̸∼ uj.

The spectrum of the graph G is the spectrum of its adjacency matrix A. In other words,
if A has eigenvalues λ1, λ2, . . . , λs with multiplicities m1, m2, . . . , ms, then the multiset
Spec(G) = {λ
m1
1 , λ
m2
2 , . . . , λms
s } is the spectrum. Note that A is symmetric and hence
all its eigenvalues λi are real. Furthermore, A is semisimple (diagonalisable), that is, Rv

decomposes as the direct sum of the eigenspaces of A and hence ∑s
i=1 mi = v.
We also note the following standard fact about symmetric real matrices.

Lemma 2.1. Distinct eigenspaces of A = A(G) are orthogonal with respect to the dot
product on Rv.

Therefore, the above decomposition of Rv as a direct sum of eigenspaces of A is
orthogonal.
If G is k-regular then each row of A has exactly k ones. Hence k is an eigenvalue of A.
Furthermore, if G is connected then k has multiplicity 1. The corresponding eigenspace
is spanned by the all-one vector.

We conclude this section with the following definition. An automorphism of a graph
G is a permutation of G that preserves adjacency. We denote by Aut(G) the group of all
automorphisms of G.

2.2 Strongly regular graphs

A strongly regular graph is a connected regular graph, for which there exist non-negative
integers λ and µ, such that any two adjacent vertices have exactly λ common neighbours
and any two non-adjacent vertices have exactly µ common neighbours. We will write
srg(v, k, λ, µ) for a strongly regular graph on v vertices, of degree k, and with parameters
λ and µ, as above.
We follow [8] for the basic results on strongly regular graphs.

4

Theorem 2.2. For an srg(v, k, λ, µ), let A be its adjacency matrix, I be the identity
matrix and J be the all-one matrix, both of the same order as A. Then the following
relations hold: AJ = kJ and A2 + (µ − λ)A + (µ − k)I = µJ.

As an application of these equations, we have the following theorem.

Theorem 2.3. If G = srg(v, k, λ, µ) then its spectrum is {k1, rf , sg}, where r, s, f, g are
given by:
 r = 1
2 (λ − µ + √
(λ − µ)2 + 4(k − µ)
) ,

s = 1
2 (λ − µ − √
(λ − µ)2 + 4(k − µ)
) ,

f = 1
2
 (
v − 1 − 2k + (v − 1)(λ − µ)
√(λ − µ)2 + 4(k − µ)
 )
 ,

g = 1
2
 (
v − 1 + 2k + (v − 1)(λ − µ)
√(λ − µ)2 + 4(k − µ)
 )
 .

Let us now see what this translates to for a possible srg(85, 14, 3, 2).

Corollary 2.4. If G = srg(85, 14, 3, 2) then A(G) has eigenvalues 14, 4, and −3 with
multiplicities 1, 34, and 50, respectively.

This is obtained by plugging the values of (v, k, λ, µ) = (85, 14, 3, 2) into the formulae
from Theorem 2.3.

2.3 Euclidean representation

Now we introduce the Euclidean representation of a strongly regular graph, which will be
the main tool that we will use to eliminate cases in this project. The theory is mostly
based on the book of Godsil [7]. There it is developed for arbitrary distance-regular
graphs, so we adjust it for our case: strongly regular graphs are distance-regular graphs
of diameter 2. We also slightly alter the notation from the book.
As above, let G = {u1, u2, . . . , uv} be a strongly regular graph with parameters
(v, k, λ, µ). We will identify G with the standard basis of U = Rv.
Recall that k, r and s are the eigenvalues of the adjacency matrix A = A(G) of G,
of multiplicity 1, f and g, respectively. It follows from Theorem 2.3 and the discussion
around Lemma 2.1 that we have the following orthogonal decomposition:

U = Uk ⊕ Ur ⊕ Us,

where Uθ is the θ-eigenspace of A for each θ ∈ {k, r, s}. As we already mentioned, since
G is connected, the 1-dimensional eigenspace Uk is spanned by the all-one vector. For
θ ∈ {k, r, s}, consider the orthogonal projection pθ : U → Uθ. Then we have the following
result (see Lemma 1.2 in Chapter 13 of [7]).

Theorem 2.5. For ui, uj ∈ V (G), the value of pθ(ui)·pθ(uj) depends only on the distance
between ui and uj.

We will represent the vertices of G by their images under pθ, but scaled to have length
1. That is, the Euclidean representation of G with respect to θ represents every vertex
ui by the unit vector ei := 1
|pθ(ui)| pθ(ui) from the subspace Uθ. If the distance between ui
and uj is m ∈ {0, 1, 2} then we have, by Theorem 2.5, that

wm := ei · ej = pθ(ui) · pθ(uj)
|pθ(ui)||pθ(uj)|

is a function of m alone. The values wm, m ∈ {0, 1, 2}, are known as the cosine sequence
of G. We can furthermore claim the following exact formulae for the values of wm.

5

Theorem 2.6 ([2], Section 4.1B). We have that w0 = 1, w1 = θ
k and w2 = θ2−λθ−k
k(k−λ−1) .

We now specialise this to the case of srg(85, 14, 3, 2). First of all, we choose θ = 4 (c.f.
Corollary 2.4), so that our representation is in the eigenspace E := U4 of dimension 34.
From now on, this is our fixed choice.

Corollary 2.7. For G = srg(85, 14, 3, 2) and θ = 4, the cosine sequence is w0 = 1, w1 = 2
7
and w2 = − 1
14 .

Hence, when the vertices ui and uj are adjacent, we have that ei · ej = 2
7 and, when
ui and uj are non-adjacent, we have that ei · ej = − 1
14 . Note that the unit vectors
{e1, e2, . . . , ev} span E. Indeed, this follows from the fact that {u1, u2, . . . , uv} is a basis
of U = Rv.
From this point on, G = srg(85, 14, 3, 2) and it is realised by the unit vectors ei in
the 34-dimensional Euclidean space E as above. Our goal is to obtain a contradiction,
showing non-existence of G, by considering various sets of vectors ei. If X is such a set,
then the Gram matrix corresponding to X must be semi-positive definite, i.e., it cannot
have negative eigenvalues. This is because the dot product on E ⊂ U is positive definite.

3 Local structure of G

Let us focus on the local subgraph G1(x) of G, induced by the 14 neighbours of a vertex
x ∈ G. Since λ = 3, the subgraph G1(x) is cubic, i.e., of degree 3. Connected cubic
graphs on at most 14 have been enumerated, see e.g. [4, 3]. The complete list of all
these graphs can be found on the internet and examined via, say, the computer algebra
system GAP [6]. Since at this point we cannot assume that the local subgraphs G1(x)
are connected, we should also add disconnected cubic graphs on 14 vertices, as unions of
smaller connected cubic graphs. In total, there are, up to isomorphism, 509 connected
cubic graphs on 14 vertices and 31 disconnected ones.

Lemma 3.1. Any two non-adjacent vertices y, z ∈ G1(x) have at most one common
neighbour in G1(x).

Proof. Since µ = 2, any two non-adjacent vertices y, z ∈ G1(x) have two common neigh-
bours in G. One of them is x, hence y and z have at most one common neighbour in
G1(x).

It turns out this simple lemma allows us to reduce significantly the number of possible
graphs G1(x). Going through the list of all 540 cubic graphs on 14 vectices, we discover
that only 39 of them, referred to in this paper as the good cubic graphs, satisfy the
condition from Lemma 3.1. Hence we have the following.

Proposition 3.2. The local subgraph G1(x), for x ∈ G, is isomorphic to one of the 39
good cubic graphs.

Out of these graphs, 36 are connected and 3 are disconnected, namely, they are unions
of a 4-clique and a connected trivalent graph Ti of order 10, i = 1, 2, 3, shown in Figure
1. Note that T3 is the Petersen graph.
 6

(a) T1 (b) T2 (c) T3

Figure 1: Relevant cubic graphs of order 10

Our method later in the text is based on considering on a neighbourhood of a maximal
3-clique in G. We can derive the existence of such maximal cliques from the enumeration
above.

Proposition 3.3. Maximal 3-cliques exist in G.

Proof. For a vertex x ∈ G, maximal 3-cliques containing x correspond to edges in G1(x)
not contained (within G1(x)) in a 3-clique. Hence the existence of maximal 3-cliques can
be established by simply going through the list of 39 possible local graphs.

Alternatively, it is easy to show that if y ∈ G1(x) is not contained in a component of
size 4 of G1(x) then its local graph in G1(x) is either a 3-coclique or a union of an edge
and an isolated vertex. Hence every such edge xy is contained in a maximal 3-clique in
G. We can formulate this as follows, specialising Proposition 3.3.

Proposition 3.4. Every edge xy ∈ E(G) that is not contained in a 5-clique, is contained
in a maximal 3-clique.

In turn, this implies the following.

Corollary 3.5. Every vertex x ∈ G is contained in a maximal 3-clique.

4 Segments and handles

Let Q be a maximal 3-clique in G. For each x ∈ Q, we have that yz = Q \ {x} is an edge
in the local subgraph G1(x). We now focus on the remaining twelve vertices in G1(x) \ yz.
Since Q is maximal, the edge xy is not contained in a 3-clique in the good cubic graph
G1(x).

Definition 4.1. Suppose that H is a good cubic graph and yz is an edge in H not
contained in a 3-clique. Let S be the subgraph of H induced on H \ yz. We call S the
segment corresponding to H and yz.

Since yz is not contained in a 3-clique, y and z have no common neighbours in H.
Let y1 and y2 be the neighbours of y in H, other than z, and symmetrically, let z1 and
z2 be the neighbours of z in H, other than y. Clearly, the pairs {y1, y2} and {z1, z2} are
disjoint and contained in S.

Definition 4.2. We call the pairs {y1, y2} and {z1, z2} the handles of the segment S.

7

We note that the segment is not just the graph S, but rather the triple consisting
of S and the two handles {y1, y2} and {z1, z2}. Note also that while {y1, y2, z1, z2} can
be identified within S as the set of all vertices of S having only two neighbours, this set
can potentially be split into a union of two handles in more than one way. Hence we
need to view a segment as a triple, expressly indicating the handles. The order of the two
handles is less important, but naturally, they are kept in a computer in some order. When
we talk below about isomorphisms of segments S and S′, we mean graph isomorphisms
S → S′ mapping the first and second handles of S to the first and second handles of S′,
respectively.
We now turn to enumeration of segments. The good graph H can be easily recovered
from its segment S. Indeed, we just need to add to S a new vertex y adjacent to the
two vertices in the first handle {y1, y2} and a second new vertex z adjacent to y and the
vertices in the second handle {z1, z2}. In particular, every segment S arises from a unique
good cubic graph H.
This allows for a very efficient enumeration of segments. We go through the list of the
39 good cubic graphs H. In each H, we determine the orbits under Aut(H) on the set
of ordered edges of H. Segments are isomorphic if and only if the come from the same
orbit. Hence we obtain a complete list of segments by choosing one representative yz of
each orbit and constructing the segment H \ yz.
Before we report the results of this calculation, we need to discuss the types of handles
and segments. A handle is a pair of vertices and, naturally, these two vertices can be
adjacent or non-adjacent. Hence the handles are classified into edges and non-edges.
Correspondingly, segments can be of four types depending on their first and second handle:
(1) edge and edge; (2) edge and non-edge; (3) non-edge and edge; and (4) non-edge and
non-edge. Clearly, for every segment of type (2), we obtain a segment of type (3) by
switching the handles. Types (1) and (4) are invariant under this operation.

Proposition 4.3. There are in total 478 segments up to isomorphism. Among them there
are 19, 78, 78, 303 segments of types (1), (2), (3), and (4), respectively.

We now introduce an additional structure on a segment. First, we need the following.

Lemma 4.4. Let S be a segment and Y = {y1, y2} and Z = {z1, z2} be its two handles.
Then yi and zj are non-adjacent for all i, j = 1, 2.

Proof. Let H be the good cubic graph that S is obtained from, and yz be the edge removed
from H. We assume that y1 and y2 are adjacent to y while z1 and z2 are adjacent to z.
Now we can prove our claim: if yi and zj are adjacent then, in H, the vertices yi and
z have two common neighbours, y and zj. This contradicts the condition from Lemma
3.1 that we imposed on good cubic graphs.

We will need the following concept.

Definition 4.5. Let S be a segment and Y and Z be its handles. The core of S with
respect to the handle Y is the set of vertices in S \ (Y ∪ Z) that are not adjacent to a
vertex of Y .

The size of core depends on the type of the handle.

Lemma 4.6. If Y = {y1, y2} is a handle of a segment S then y1 and y2 have no common
neighbours in S. In particular, the core of S with respect to Y consists of six vertices, if
Y is an edge, and the core consists of four vertices, if Y is a non-edge.

Proof. Let H be the good cubic graph from which S was constructed by removing an edge
yz. We assume that y is adjacent to y1 and y2. Suppose that y1 and y2 have a common
neighbour s in S. Then s is not adjacent to y and at the same time, s and y have two

8

common neighbours, y1 and y2. This is a contradiction since H is a good cubic graph.
Thus, y1 and y2 have no joint neighbours in S.
If Y is an edge then y1 has only one neighbour in S, other than y2, and symmetrically,
y2 has only one neighbour in S, other than y1. Note that, by Lemma 4.4, those neighbours
are not in the second handle Z. Hence the core with respect to Y is obtained by removing
from S the vertices in Y , Z and the two neighbours of Y , leaving six vertices in the core.
If Y is a non-edge then each of y1 and y2 has two further neighbours in S and so the
core is obtained in this case by removing Y , Z and the four neighbours of Y . Hence the
core is of size four.

This allows us to attach numerical labels to the segments; namely, each segment S will
be labelled with a pair from {6, 4} × {6, 4}, indicating the size of the cores with respect
to the two handles. That is, type (1) above (edge and edge) becomes type (6, 6); type (2)
(edge and non-edge) becomes (6, 4); type (3) (non-edge and edge) becomes type (4, 6);
and finally, type (4) (non-edge and non-edge) becomes type (4, 4).
In fact, we can classify segments even more finely. For a segment S with handles X
and Y , let the quadruple (nS, rS, lS, bS) be defined as follows: nS = |S0 \ (CX ∪ CY )|,
rS = |CY \ CX |, lS = |CX \ CY |, and bS = |CX ∩ CY |, where S0 = S \ (X ∪ Y ), CX
is the core of S with respect to X, and CY is the core of S with respect to Y . Clearly,
nS + rS + lS + bS = |S0| = 8, lS + bS = |CX |, and rS + bS = |CY |. So this quadruple can
serve as a finer invariant, and we call it the quad type of S.
The table below shows the number of segments of each possible quad type.

type quad type number of segments

(6,6) (2, 0, 0, 6) 0
(1, 1, 1, 5) 5
(0, 2, 2, 4) 14

(6,4) (2, 0, 2, 4) 9
(1, 1, 3, 3) 35
(0, 2, 4, 2) 34

(4,4)
 (4, 0, 0, 4) 4
(3, 1, 1, 3) 23
(2, 2, 2, 2) 146
(1, 3, 3, 1) 102
(0, 4, 4, 0) 28

Table 1: Quad types

Note that there happens to be no segments of quad type (2, 0, 0, 6). Note also that
we skipped the type (4, 6), which clearly has the dual (switching rS and lS) quad type
distribution, compared to the type (6, 4).

5 Gluing segments

The idea of our approach is to investigate the union of three local subgraphs G1(x), x ∈ Q,
where Q is, as above, a maximal 3-clique in G. Once we identify the graph induced on this
set, we can produce the corresponding Gram matrix (since we assume that G is realised
as a set of unit vectors in E) and check this matrix for semi-positive definiteness hoping
to eliminate in this way a great majority of all possibilities.
Before we discuss how to glue local subgraphs together, let us make a slight adjustment.
Namely, we will show that it suffices to glue together the three segments arising from Q.
We will need the following result.
 9

Lemma 5.1. For x ∈ G, we have that ∑
y∈G1(x) y = 4x.

Proof. Let w = ∑
y∈G1(x) y. Using Corollary 2.7, we have that w · w = 14(1 + 3( 2
7 ) +
10(− 1
14 )) = 14 + 12 − 10 = 16 and w · x = x · w = 14( 2
7 ) = 4. In the first calculation, we
used that every y ∈ G1(x) has 3 neighbours and 10 non-neighbours in G1(x).
Hence, for t = w − 4x, we have that t · t = (w − 4x) · (w − 4x) = w · w − 4w · x − 4x · w +
16x · x = 16 − 16 − 16 + 16 = 0. This means that t = 0, that is, w = 4x, as claimed.

As we already stated, we would like to recover the induced graph structure on the
union ∪x∈QG1(x) for a maximal 3-clique Q. Clearly, this set is the union of Q and the
three segments Sx := G1(x) \ Q, x ∈ Q. Let sx := ∑u∈Sx u. Then we have the following
vector equations.

Lemma 5.2. If Q = {x, y, z} then x = 1
10 (3sx + sy + sz), y = 1
10 (sx + 3sy + sz), and
z = 1
10 (sx + sy + 3sz).

Proof. By Lemma 5.1, we have:
 sx + y + z = 4x

sy + x + z = 4y

sz + x + y = 4z

Solving this linear system for x, y and z yields the claim.

According to this lemma, the span of T := ∪x∈QSx includes Q and so the rank of
the Gram matrix on T ∪ Q is the same as the rank of the Gram matrix on T . We will
therefore work with just T , ignoring the three vertices from Q.
Next we discuss how we can recover the graph structure on T , which includes how the
segments Sx, x ∈ Q, intersect, which edges T inherits from these segments, and which
edges in T are extra.
We start with the intersection of segments.

Lemma 5.3. For x, y ∈ Q, x ̸= y, we have that Z := Sx ∩ Sy is a handle in both segments
Sx and Sy.

Proof. If z is the third vertex in Q then Sx is obtained from G1(x) by removing the edge
yz. Hence Sx ∩ G1(y) is a handle in Sx. It remains to see that Sx ∩ G1(y) = Z. On the one
hand, Z = Sx ∩ Sy is clearly contained in Sx ∩ G1(y). On the other hand, the difference
between Sy and G1(y) is the edge xz. Both x and z are not contained in Sx, and hence,
indeed, Sx ∩ G1(y) = Sx ∩ Sy = Z.
Symmetrically, Z is also a handle in Sy.

Let us now fix the notation we will use in the remainder of the paper. Let Q = {x, y, z}
and we set Z := Sx ∩ Sy, as above, and symmetrically, Y := Sx ∩ Sz and X := Sy ∩ Sz.
This is shown in Figure 2.
Our next result concerns the additional edges on Sx ∪ Sy, or equally, any other union
of two segments above. Recall from Section 4 the concept of the core of a segment with
respect to a handle.

Lemma 5.4. Let Cx ⊂ Sx be the core of Sx with respect to Z = Sx∩Sy and, symmetrically,
let Cy ⊂ Sy be the core of Sy with respect to Z. Then every edge within Sx ∪ Sy, that
is not fully contained in Sx or Sy, connects a vertex from Cx with a vertex from Cy.
Furthermore, such edges form a matching between Cx and Cy.

10

Figure 2: The composition of T

Proof. Let u ∈ Sx. If u ∈ Z then every edge from u to a vertex of Sy is contained in
Sy. If u is contained in the second handle, Y , of Sx then u and y already have µ = 2
common neighbours, namely, x and z, and so u has no neighbours in Sy. Similarly, if
v ∈ Sx \ (Y ∪ Z) but v is adjacent to a vertex zi in Z then the common neighbours of
u and y are x and zi, and so again u has no further neighbours in Sy. Hence only the
vertices from Cx can have further neighbours in Sy. Symmetrically, only vertices from Cy
can have further edges in Sx. We have shown that the edges on Sx ∪ Sy that are not fully
in Sx or Sy connect Cx with Cy.
Now let u ∈ Cx. Then x is a common neighbour of v and y. Since µ = 2 and since
u is not adjacent to Z, it must have exactly one neighbour in Sy, and by the above,
this unique neighbour is in Cy. Thus, every vertex in Cx has a unique neighbour in Cy
and, symmetrically, every vertex of Cy has a unique neighbour in Cx; that is, we have a
matching between Cx and Cy, as claimed.

Needless to say, we have similar matchings between the corresponding cores in Sx and
Sz and in Sy and Sz.

The process of forming T = Sx ∪ Sy ∪ Sz consists of several steps. We first glue
together possible segments Sx and Sy by identifying corresponding handles, which become
Z = Sx ∩ Sy. Then we select and add a matching between the cores of Sx and Sy with
respect to Z. Clearly, the segments we identify must be of the same type (edges or non-
edges) and then the two cores do indeed have the same size and matchings are possible.
We note that matchings between two sets of size m are in a natural correspondence with
the elements of the symmetric group Sm, and so we have |S6| = 720 possible matchings if
Z is an edge, and |S4| = 24 possible matchings if Z is a non-edge.
At this point, after choosing a particular matching, we already known the induced
graph on Sx ∪ Sy and so we can write the Gram matrix corresponding to the set of unit
vectors Sx ∪ Sy in E. This could, in principle, lead to elimination of some configurations
due to negative eigenvalues of their Gram matrices. However, as we discovered computa-
tionally, all double unions survive this criterion, and this is why we are forced to consider a
larger triple union of segments. Hence, the next step is to glue in a third possible segment
Sz by identifying its two handles with the remaining unmatched handles in Sx and Sy.
This is followed by a selection of matchings between the cores in Sx and Sz with respect
to Y = Sx ∩ Sz and between the cores in Sy and Sz with respect to X = Sy ∩ Sz. This
completes forming of the induced graph on T and so the whole Gram matrix on T can
be formed and checked for negative eigenvalues. Since |T | = 30 is close to the dimension

11

34 of the ambient Euclidean space E, this check is now quite powerful and eliminates a
great majority of cases.

There are, of course, a lot of technical details concerning this process, which we will
provide later. In the remainder of this section we discuss gluing two graphs over a common
subgraph.

Definition 5.5. A gluing of graphs A and B over isomorphic subgraphs HA ⊆ A and
HB ⊆ B is an isomorphism ϕ : HA → HB.

A gluing produces a new graph by taking the union of A and B and, furthermore,
identifying every vertex h of HA with the corresponding vertex ϕ(h) of HB. Hence HA
and HB merge into the intersection H = A ∩ B. Note that the edges of the glued graph
all come from the edges of A and B. Moreover, since ϕ is a graph isomorphism, edges of
A within HA merge with the corresponding edges of B within HB, so we do not end up
with double edges.
Clearly, HA and HB must indeed be isomorphic or else no gluing is possible. We
will however focus on a different question: how many different graphs can we obtain by
gluing the given A and B over the given isomorphic HA and HB? This is answered by the
following proposition, adapted from statement (2.7) in [9] to the graph-theoretic context.
Instead, of gluing HA directly with HB, we can introduce an independent copy H of
this graph and glue it onto HA and HB via all possible isomorphisms ψA : H → HA
and ψB : H → HB. This point of view stresses symmetry between A and B while
being equivalent to our original gluing construction. In what follows we fix arbitrary
isomorphisms γA : H → HA and γB : H → HB.
Let Aut(A, HA) be the group of all automorphisms of A leaving HA invariant. Sym-
metrically, let Aut(B, HB) be the group of all automorphisms of B stabilising HB. These
automorphisms can be transferred into Aut(H) by conjugating with γA and γA, respec-
tively, giving us subgroups Aut(A, HA)γA and Aut(B, HB)γB of Aut(H). (Naturally, every
element of Aut(A, HA) is first restricted to HA and then conjugated by γA, and similarly,
for the elements of Aut(B, HB).)

Proposition 5.6. The number of non-isomorphic graphs formed by gluing A and B with
respect to isomorphic subgraphs HA and HB coincides with the number of double cosets
in the group Aut(H) of its subgroups Aut(A, HA)γA and Aut(B, HB)γB .

Note that here we only consider isomorphisms between resulting glued graphs that
preserve A and B set-wise. In principle, there could be further isomorphisms, for example,
the ones switching A and B or even more general ones. These are not accounted for
in the above proposition. However, this will be irrelevant for our purposes. The final
remark is that the complete set of different gluings ϕ : HA → HB is given by {γBαiγ−1
A |
i = 1, 2, . . . k}, where k is the number of double cosets above and α1, α2, . . . , αk are
representatives of the double cosets.
In our enumeration, the above proposition is applied to gluing the segments Sx and Sy
over the respective handles. As we already mentioned, the handles must be of the same
type: either both edges or both non-edges. Note that in either case Aut(H) is of order
2 and the number of double cosets is one if the two vertices of the glued handle can be
switched in the (handle-preserving) automorphism group of either of the two segments
Sx and Sy. If the two vertices cannot be switched then the number of double cosets is
two. Clearly, this gives us an easy way to enumerate all segment pairs (graphs obtained
by gluing Sx and Sy) up to isomorphism.
In order to state the result of the enumeration, recall that we dropped all the segments
of type (4, 6), and we are always gluing the first handles from both segments. Therefore,
a segment pair can only be made of two segments of type (6, 6), or a segment of type
(6, 6) and a segment of type (6, 4), or two segments of type (6, 4), or two segments of type
(4, 4).
 12

The following statement, established by enumeration, gives us the number of different
segment pairs.

Proposition 5.7. There are 86333 different segment pairs in total. Among them, there
are 281 segment pairs made of two segments of type (6, 6), 2249 segment pairs made of
a segment of type (6, 6) and a segment of type (6, 4), 4851 segment pairs made of two
segments of type (6, 4), and 78952 segment pairs made of two segments of type (4, 4).

From this statement, we see that the last type of segment pairs is by far the most
numerous. However, this is offset by the fact that the number 24 of possible matchings
between the cores of Sx and Sy arising in this case is much smaller than the number 720
of matchings required for the first three types. Hence the four types of segment pairs are
in fact reasonably balanced in computational terms.

We next discuss the algorithmic details of all these processes.

6 Steps 1 and 2: Building up T

We keep all possible segments in a list according to the type of the segment. First, we
have the 19 segments of type (6, 6), then the 78 segments of type (6, 4), and finally, the
303 segments of type (4, 4).
Each segment S is stored with its vertices ordered in a particular way. First, we have
the two handles, X and Y , then the vertices from S0 = S \ (X ∪ Y ) not contained in the
cores CX and CY , then the vertices in CY \ CX , then CX \ CY , and finally the vertices
from CX ∩ CY . This is shown in the following table, where the numbers in the third
column indicate the size of the part. Note that the last four numbers constitute the quad
type of S.
 X 2
Y 2
none S \ (X ∪ Y ∪ CX ∪ CY ) nS
right CY \ CX rS
left CX \ CY lS
both CX ∩ CY bS

Table 2: Vertices in a segment

The first column indicates the meaning of the part: the two handles do not require
explanation, the following part consists of vertices in neither of the two cores, hence the
label ‘none’; the label ‘right’ indicates that those vertices belong only in the core for the
second handle; ‘left’ means that these are in the core for the first handle; finally, ‘both’
indicates that these vertices are in both cores. (‘Left’/‘right’ was a useful mnemonic that
we adopted during this project.)
When we enumerate segment pairs, we always assume that Sx either precedes Sy on
the list or Sx is the same segment as Sy. This guarantees that we do not overcount
segment pairs. As we have already mentioned, we glue the first handle of Sx onto the first
handle of Sy.

Once we select a specific segment pair from our list of 86333, we need to go at Step 1
through all possible matchings between the cores of Sx and Sy with respect to the handle
Z = Sx ∩ Sy, the first (‘left’) handle in both segments. These two cores are identified
within the corresponding segment records as the union of the parts marked with ‘left’ and
‘both’, i.e., the cores are at the end of the record for both segments. Note that the two
cores are of the same cardinality c ∈ {4, 6}, as Z has the same type in Sx and Sy.

13

Recall that our method involves checking the Gram matrix on an ever growing set of
vertices. In other words, once we know all edges within the subset, i.e., the Gram matrix
on this subset is fully known, we immediately want to check this Gram matrix for semi-
positive definiteness. In principle, such a check becomes more and more expensive as the
subset becomes bigger. However, as we build the set up by adding one vertex at a time, this
amounts to adding one new row (and column) to the Gram matrix. Fortunately, the LDLT
algorithm [5], which we use to verify absence of negative eigenvalues, is iterative exactly
in this sense, and so we can significantly save on time by doing just the iterative part
corresponding to adding one row. The details of this realisation of the LDLT algorithm
are in Appendix B.
Having the cores at the end of the segment record means that the induced subgraph on
the first 22−c vertices of the segment pair (the full size of a segment pair is 12+12−2 = 22
vertices) is the same regardless of the matching we add. That is, we need to account for
the possible matchings only when dealing with the final c vertices.
Recall that possible matchings between two cores Cx ⊂ Sx and Cy ⊂ Sy of equal
size c are indexed by the elements of the symmetric group Sc. Since c ∈ {4, 6}, we have
6! = 720 matchings when Z is an edge and 4! = 24 matchings when Z is a non-edge.
Looking at Proposition 5.7, we see that there are significantly more segment pairs where
Z is a non-edge, so adding the matchings evens out those two cases.
To add a matching to a given segment pair, we scan a pre-computed tree of depth c,
which at each level i decides the neighbour in Cx of the ith vertex yi from Cy. This allows
us to add the data of yi to the Gram matrix and check semi-positive definiteness. This
results in a very efficient enumeration algorithm. Note that we had the option of using
symmetry of the segment pair to cut down on the number of possible segment pairs with
matching. However, in most cases the symmetry is trivial, and so we decided against using
it, as it would not bring us much benefit and it would require a different enumeration tree
for each symmetry type, significantly complicating the algorithm.
As it turns out, none of the resulting segment pairs with matching (corresponding
to the leaves of the enumeration tree) are eliminated by the semi-positive definiteness
criterion. This is why we next add the third segment Sz at Step 2. Again, we could
use the symmetries of the segment pair Sx ∪ Sy and the segment Sz to reduce, using
Proposition 5.6, the number of ways of merging the first and second handles in Sz with
second handles in Sx and Sy, respectively. However, we again decided against it, because
we judged that it would not give us a significant decrease in runtime to justify the trade
off, a less transparent algorithm. Hence we simply allowed all four ways of gluing the
two handles of Sz onto the second handles of Sx and Sy. In hindsight, this may have
been a questionable decision as the majority of the hardest cases came from symmetric
configurations and so, in fact, it may have significantly increased the overall runtime by
doing some slow configurations twice.
Note that we again assume that Sz does not precede Sy (and hence also Sx) in the list
of segments, and this allows us to avoid the most obvious overcounting.

Once the handles of Sz are identified with the corresponding handles of Sx and Sy,
we still need to add two matchings, between the cores in Sx and Sz corresponding to the
handle Y = Sx ∩ Sz and between the cores in Sy and Sz corresponding to the handle
X = Sy ∩ Sz. Just like we used an enumeration tree to account for all matchings in the
segment pair Sx ∪ Sy, we utilise a similar idea and account for the two new matchings
within a single precomputed tree of depth 8 (the cardinality of Sz \ (X ∪ Y )). Hence, at
each level i, the tree chooses the additional neighbours of the ith vertex zi of Sz \ (X ∪ Y )
in Sx and Sy. Referring to Table 2, if zi is in the ‘none’ part of the segment Sz then
it has no additional neighbours and so we can immediately add this vertex to the Gram
matrix and check semi-positive definiteness. If zi is in the ‘right’ part of Sz then it has
an additional neighbour in Sy. Symmetrically, if zi is in the ‘left’ part then it has an
additional neighbour in Sx. Finally, if zi is in the ‘both’ part of Sz, it has two additional

14

neighbours, one in Sx and the other in Sy. Again, once the neighbours of zi are selected,
we add the data of zi to the Gram matrix and check semi-positive definiteness.
From this discussion, it is clear that the exact structure and size of this second enu-
meration tree (we called it the big tree, as opposed to the smaller tree we use for adding
the matching between the cores in Sx and Sy) depends on the quad type (nS, rS, lS, bS)
of S = Sz. We precomputed the big trees for all quad types and then simply use the
correct one depending on the quad type of Sz. Note that while the structure and the
total size of the big tree varies from one quad type to another, the number of final con-
figurations (leaves) in the big tree depends only on the types of the handles X and Y .
Namely, we have exactly 6!6! = 7202 = 518400 leaves when both X and Y are edges,
6!4! = 720 · 24 = 17280 leaves if Y is an edge and X is a non-edge, and 4!4! = 242 = 576
leaves if both X and Y are non-edges.
These numbers indicate the possible numbers of complete configurations T = Sx ∪Sy ∪
Sz for each choice of a segment pair with a matching, Sx ∪ Sz with the third segment Sz
already glued in over the handles. This makes for really astronomical total numbers of
possible configurations T , which would not be possible to enumerate and evaluate. What
makes it a feasible project in the end is that we add vertices one by one and the semi-
positive definiteness criterion kicks in a very non-trivial way after just a few (typically
four or five) vertices of Sz \ (X ∪ Y ) are added. So we rarely, in fact, almost never, have
to visit in our enumeration all leaves of the big tree.

We do not have the exact data which proportion of all configurations is eliminated by
expanding Sx ∪ Sy to the full set T = Sx ∪ Sy ∪ Sz. By our observation, it is well in excess
of 99%. However, a tiny proportion of survivors ends up being a significant number of full
configurations T which are semi-positive definite, and hence, in order to try and eliminate
those, we need an extra step in the algorithm, adding vertices beyond T .

7 Step 3: Beyond T

After extensive experiments trying to find a meaningful way to add additional vertices,
we settled on the following scheme: we add vertices from G \ ˆT , where ˆT = Q ∪ T , that
are adjacent to the first vertex t from the handle X = Sy ∩ Sz. This is the vertex number
13 in T .

7.1 Enumerating additional vertices

Note that t has no neighbours in Sx and it has two neighbours in both Sy and Sz. Hence,
within ˆT , the vertex t has 2 + 2 + 2 = 6 neighbours, if X is a non-edge, and t has
2 + 1 + 1 + 1 = 5 neighbours in ˆT , if X is an edge1. In any case, t has at least 14 − 6 = 8
neighbours in G\ ˆT , and these are the vertices we aim to add to our configuration. Adding
eight extra vertices to T brings the total to 38 vertices, which significantly exceeds the
dimension 34 of E. Hence not only the Gram matrix on this larger set must be semi-
positive definite, but also the rank of the Gram matrix cannot exceed 34, which means
that the radical must be of dimension at least 38 − 34 = 4, and this is a super-strong
condition. On the other hand, we do not know adjacency on the set of extra vertices, as
we do not utilise any concept similar to segment here. We add the extra vertices one by
one, using the restrictions that we now proceed to discuss.

Lemma 7.1. Suppose that u ∈ G \ ˆT , and u is adjacent to t. Then u has exactly two
neighbours in Sx and it has exactly one additional (other than t) neighbour in both Sy and
Sz.

1For the reasons that will be explained later, we never encounter in the actual calculation the case where X
is an edge.
 15

This is immediate since u is not adjacent to any vertex in Q and µ = 2. This means
that u has the maximum of five and the minimum of three (if u is adjacent to vertices in
both handles Y and Z) neighbours in T .
We pre-compute all such possible sets of neighbours in T .

Lemma 7.2. In total, there are exactly 2080 possible configurations of neighbours of u in
T that satisfy Lemma 7.1.

Note that this set of possible sets of neighbours of extra vertices u only depends on
how the segments are embedded in T , and so this calculation needs to be done only once,
as its result, the array we call downs, is applicable to all T . However, a concrete T allows
further elimination of some of these possibilities.
First of all, we note that each u is uniquely identified by its neighbours in T .

Lemma 7.3. If u′ ∈ G \ ˆT has the same neighbours in T as u then u′ = u.

Proof. Indeed, suppose that u′ ̸= u. Since they have at least three common neighbours
in T and µ = 2, we must have that u and u′ are adjacent. Furthermore, since λ = 3, u
and u′ have exactly three neighbours in T , one in each handle. Let t′ be their common
neighbour in the handle Z = Sx ∩ Sy. Then we know from Lemma 4.4 that t and t′ are
non-adjacent and, at the same time, they have three common neighbours, y, u and u′.
This is a contradiction proving the claim.

Hence, each element d of downs describes a unique potential neighbour u of t.

7.2 Eliminating impossible d

To eliminate some d, we first compute the demand for all pairs of vertices from T . That is,
given a pair ti, tj ∈ T , with i < j, we compute how many vertices from G \ ˆT should there
be that are adjacent to both ti and tj. Namely, we start with the total of λ = 3, if ti and
tj are adjacent, and the total of µ = 2, if they are non-adjacent. Then we subtract one
from this total for each common neighbour of ti and tj in ˆT . If we end up with a negative
demand for some pair ti, tj then we can, clearly, discard this particular configuration T
altogether. The diagonal entries in the demand matrix, corresponding to the situation
tj = ti, are not used and hence are not computed.
Once the demand matrix is known and it does not contain negative values, we check
every d in downs against it. If for a pair i, j ∈ d, i < j, we have that the demand for ti
and tj is zero then we discard such a d.
If d survives this check, we then check it for the following condition: for each i ∈
{1, 2, . . . , 30} \ d, we check that the number of known common neighbours between ti and
u (corresponding to d) does not exceed µ = 2. (Note that since i /∈ d, ti and u are not
adjacent.) If such an i is found then d is discarded as well. We also compute at this
stage what we call the halo of the potential vertex u. By definition, this is the set of all
i ∈ {1, 2, . . . , 30} \ d such that ti and u have exactly µ = 2 known common neighbours.
The halo is used at a later stage when we check for possible adjacency among additional
vertices u. Note that to find the number of known common neighbours for ti and u we
simply count the number of j ∈ d such that Mij = 2
7 , where M is the Gram matrix of T ,
which is known at that point.
The next check for d involves verification that adding u to T does not create a non
semi-positive Gram matrix. First, we compute the vector r = (r1, r2, . . . , r30) of all values
u · ti. Hence
 ri = { 2
7 , if i ∈ d;
− 1
14 , otherwise.

This vector allows us to find u·w for every w = ∑30
i=1 citi ∈ W = ⟨T ⟩ by simply computing
the 1 × 1-matrix rcT , where c = (c1, c2, . . . , c30).

16

Non semi-positive definiteness of the extended Gram matrix can manifest itself in two
different ways. First, it arises when rcT ̸= 0 for some vectors c such that u = ∑30
i=1 citi = 0.
We can verify this condition as follows: while checking T for semi-positive definiteness
via the LDLT decomposition, we also compute the matrix R = L−1, with the rows Ri
of R representing an orthogonal basis in R30 endowed with the symmetric bilinear form
represented by the Gram matrix M . (See Appendix B for details.) In particular, the
vectors Ri such that Dii := RiM RT
i = 0 form a basis in the null space of M , and so we
can simply check the above condition for all such c = Ri.
The second way the extended Gram matrix may become non semi-positive definite
is when the projection projW (u) of u to W is longer that u, and so u − projW (u) has
negative (square) length. For this check, we compute the projection matrix P for T . (See
Appendix C for the details.) Then the projection of u is found as ∑30
i=1 piti, where p = rP .
Finally, we find the length of the projection as rpT , and if the entry in this 1 × 1-matrix
exceeds 1 (the length of u) then we reject d.
Filtering out all impossible elements of downs via the above conditions leaves us with
the array verts of all d that may potentially correspond to vertices in G \ ˆT . Turning
to the computational aspect of this, in most cases verts would only be a small part of
downs, having no more than 150 possible d. (Recall that downs has size 2080.) However,
in some difficult cases we observed larger arrays verts of up to 600+ sets d. The checks
themselves were quite quick for each T , but the later calculations could be long when
verts was large.

7.3 Compatibility of additional vertices

Now that the set of possible additional vertices, represented by the array verts, has
a more reasonable size, we can try to select from it the eight neighbours of t. We do
the selection recursively. The current (incomplete) selection of vertices is represented by
the array further and at every stage we have the current unsatisfied demand matrix
and the current version of verts, where the additional vertices u have been checked for
compatibility with the already selected vertices in further. Hence we now proceed to
describe these compatibility conditions.
If u and u′ are two such vertices, corresponding to d and d′, then we have that they
must eventually form an edge or a non-edge. These two options involve different checks.
For a potential edge, we verify that:

(a) the intersection d ∩ d′ is of size at most 3; this is because λ = 3;

(b) d meets trivially the halo of u′ and, symmetrically, d′ meets trivially with the halo
of u; and

(c) adding both u and u′ to T does not lead to non semi-positive definiteness, assuming
that uu′ is an edge.

We need to justify (b) and explain how the check (c) is performed.

Lemma 7.4. For vertices u, u′ ∈ G \ ˆT with sets of neighbours in T given by d and d′,
respectively, if d meets the halo of u′ non-trivially then u and u′ cannot be adjacent in G.

Proof. Recall that the halo of u′ consists of all vertices ti, with i /∈ d′, such that ti has
exactly two neighbours, tj and tk, with j, k ∈ d′. If ti is adjacent to u and u is adjacent
to u′ then u, tj, and tk are common neighbours of ti and u′, which is a contradiction,
because ti and u′ are non-adjacent and µ = 2.

This shows that indeed (b) is a valid check.
As for the check in (c), we use the vectors r and r′ corresponding to u and u′ (see
above) and also the corresponding vectors p = rP and p′ = r′P , which are all known at
this point. Note that, setting w = projW (u), v = w − u, w′ = projW (u′), and v′ = w′ − u′,

17

we must have that v · v′ + w · w′ = u · u′ = 2
7 , if u and u′ are adjacent. Consequently, we
must have that | 2
7 − w · w′| = |v · v′| ≤ |v||v′|, and hence ( 2
7 − w · w′)2 ≤ (v · v)(w′ · w′) =
(u · u − w · w)(u′ · u′ − w′ · w′) = (1 − w · w)(1 − w′ · w′). This results in the condition we
verify in (c): ( 2
7 − r(p′)
T )2 ≤ (1 − rp
T ) (
1 − r′(p′)
T ) .

As usual, we identify the 1 × 1 matrices here, such as, say, r(p′)T , with the entry in it.
Also note that w · w′ = u · w′ and so r(p′)T correctly represents this value (and similarly
for the other terms in the inequality).
The final remark about checking whether u and u′ can form an edge is the the halo
condition (b) is quite strong and it eliminates a lot of pairs u and u′.

To check whether u and u′ can form a non-edge, we verify the following:

(a) the intersection d ∩ d′ is of size at most 2, since µ = 2; and

(b) adding both u and u′ to T does not lead to non semi-positive definiteness, assuming
that uu′ is a non-edge.

We do not have, unfortunately, a halo-type condition for non-edges. The condition (b)
is verified via the inequality
(− 1
14 − r(p′)T )2 ≤ (1 − rp
T ) (
1 − r′(p
′)T ) ,

which is similar to the condition (c) we had for edges.

Finally, additional vertices u and u′ are compartible if they can form an edge, or a non-
edge, or both. In most cases, both u and u′ have very small length, which either eliminates
the pair altogether, as non-compatible, or only one condition, for an edge or for a non-
edge, could be satisfied. However, in difficult cases we may have many compatible pairs,
about which we cannot decide immediately whether they form an edge or a non-edge.

7.4 Recursion

We have already mentioned that we build the possible sets further of additional neigh-
bours of t recursively. The recursor function takes as arguments the current set of possible
extra vertices verts and current demand array. Recall that the demand array records for
each pair i, j ∈ {1, 2, . . . , 30}, i < j, how many additional common vertices of ti and tj we
can still add. The current array further is a global variable and it is affected (extended)
by the recursor. Above we explained how to find the initial demand array and the initial
verts. Clearly, the initial further is empty.
The recursor first checks if we have forced vertices. These are the vertices that must
be added if we are to satisfy the demand. For this, we compute the offer array counting
the common neighbours of all pairs ti, tj among the vertices in verts.
If for some pair i, j, with i < j, demand exceeds offer then, clearly, demand cannot be
met and so we exit the recursor right away, as this configuration cannot be successfully
completed. If demand for i, j is equal to offer then the only way to satisfy demand is
by adding to further all common neighbours of ti and tj from verts, so these common
neighbours are forced and we add them to the array forced, and we do this procedure
for all pairs i, j.
If this results in a non-empty array forced then we do the following checks on it:

(a) the total length of further and forced does not exceed the number of additional
neighbours t can have (which is 8 in the actual calculation); and

(b) the vertices in forced are compatible with each other.

(Note that that these vertices are compatible with all vertices from further, as this holds
for all vertices in the current verts.) If either of the two checks above fails then the
current configuration cannot be completed and we exit the recursor.

18

If the set of forced vertices passes the checks then we add them to further and compute
the new demand matrix and the new verts by removing from it the vertices that are

(a) forced; or

(b) are adjacent to a pair ti, tj with new demand zero; or

(c) are not compatible with some forced vertex.

While computing the new demand, we check that it remains non-negative for all pairs i, j,
or else we exit the recursor. Also, if the length of new further is equal to 8, the number
of required additional neighbours of t, then we have arrived at one of the possible exact
sets of additional vertices of t and so we call a different function (that we describe in the
next section) to see if this can actually lead to a graph G. Once the new demand and
new verts are computed, we call a new instance of the recursor. On return from it, we
exit the current recursor, as nothing else can be done.
If, on the other hand, we find no forced vertices in verts then we select ti ∈ T \ {t}
so that the demand for the pair t and ti is non-zero but as small as possible. The idea
is that we must add an extra vertex satisfying this demand and the minimality condition
hopefully means that we have a short list of possible additional vertices that we can use.
Hence we make the list of vertices from verts that are joint neighbours of t and ti, and
we add to further one vertex from this list in a loop. Note that when we add the ith
vertex from this list, it means we have already tried all preceding vertices and so they
can be removed from further consideration. We compute the new demand array and new
verts, as above. If further has length exactly 8, we again call the function deciding
whether the exact set further can lead to a graph G. Otherwise, we call a new instance
of recursor. On exit from the call, we restore further and continue with the loop, and
when it ends we exit the current recursor, as there is nothing left for us to try.

To summarise this section, if we have a complete set T with a semi-positive definite
Gram matrix then we recursively enumerate all possible sets of 8 additional neighbours
of the vertex t = t13 from the handle X = Sy ∩ Sz. In most cases this procedure is
quite efficient and in a great majority of cases it does not produce any possible exact
sets of additional neighbours of t, thus ruling T out. However, in difficult cases, it can
produce some exact candidates for the additional neighbours of t. Note that we cannot
immediately check the extended set of vertices for semi-positive definiteness, as we may
not know the edges among the additional vertices. So there is a further enumeration step
to be done, and it is described in the next section.

8 Step 4: Exact sets

Suppose that we have a set T with a semi-positive definite Gram matrix M and a set
further of all additional (i.e., not contained in T ) neighbours of t = t13. Clearly, the
graph C = G1(t) on the set of neighbours of t should be a good cubic graph. The issue is
that we do not know all edges in this local graph, but we do have some partial information
about edges. First of all, we organise the vertex set {c1, c2, . . . , c14} of C as follows: we
take c1 = y, c2 = z, c3 and c4 are the neighbours of t in Sy, and c5 and c6 are the
neighbours of t in Sz. (Recall that the handle X is a non-edge, and so our counting is
correct.) The remaining eight vertices c7, c8, . . . , c14 come from the array further.
We know that y = c1 is adjacent to z = c2, as well as c3 and c4, but not to any other
vertex of C. Similarly, z = c2 is also adjacent to c5 and c6, but not to any further vertex
from C. Adjacency among the vertices {c3, c4, c5, c6}, which are in T , can be gleaned
from the available Gram matrix M of T , and so we know all edges there. Also known
are all edges between the vertices v ∈ {c3, c4, c5, c6} and u ∈ {c7, c8, . . . , c14}, because
these are recorded in the element d of downs corresponding to u. However, for pairs of
vertices u, u′ ∈ {c7, c8, . . . , c14}, i.e., in further, we only have partial information: they

19

are compatible, which means that at least one of the two possibilities, an edge or a non-
edge, has not been ruled out for each such pair. So the status of each pair u, u′ from
further is one of the following:

(a) definitely an edge;

(b) definitely a non-edge; or

(c) an edge or a non-edge.

At this final stage, Step 4, of our enumeration algorithm we recursively go through all
possibilities for the local graph C.
The preparation step for this recursion involves computing a 14 × 14 matrix represent-
ing the current information about the edges of C, as above. Namely, for each pair i, j,
the edge matrix records the current status of the pair i, j, according to the cases (a)-(c).
We also compute the demand array, which, for each i, records how many edges the vertex
ci is missing, and the supply array, which similarly records, for each i, how many j ̸= i
are there such that the pair i, j is recorded in the edge matrix as being case (c), i.e., ci
and cj do not currently form an edge, but they may form an edge eventually. Note that
if there is an i such that the demand for ci is greater than supply then this clearly is an
impossible situation and so we exit.
These three arrays, the edge matrix, demand list, and supply list serve as arguments
of the Step 4 recursor function. In this function, we first try to remove some uncertainties
from the edge matrix, i.e., we try to transform each uncertain case (c) into one of the
definitive (a) and (b). We can do this when one of the following conditions is met:

1. if the demand for some i is zero (i.e., ci already has its three neighbours in C), but
the supply for i is not zero, we mark all undecided pairs i, j as non-edges;

2. if the demand for some ci is equal to the supply then all the uncertain pairs i, j are
changed to edges;

3. for each pair i, j, we compute the current number e of known common neighbours
of ni and nj in N ; then

(a) if e ≥ 3 then this is an impossible configuration, so we quit;
(b) if e = 2 then
i. if i, j is a known non-edge then this is a contradiction, since, in a good
graph, two non-adjacent vertices can have at most one common neighbour;
hence we quit;
ii. if i, j is currently recorded as uncertain then we change it to an edge for
the same reason as above;
iii. if i, j is already known to be an edge then we make certain that ci and
cj have no further common neighbours; namely, we go through all vertices
ck ∈ C, k ̸= i, j, and if i, k is an edge and j, k is uncertain, we make it a
non-edge; similarly, if i, k is uncertain and j, k is an edge, we make i, k a
non-edge;
(c) if e = 1 then we can only force change if i, j is a known non-edge; then we
make sure that ci and cj have non further common neighbours, as above: for
k /∈ {i, j}, if i, k is an edge and j, k is uncertain, we make it a non-edge; similarly,
if i, k is uncertain and j, k is an edge, we make i, k a non-edge.

As we implement changes, we also update the demand and supply lists accordingly, and
if supply is ever less than demand then we quit, as this is an impossible situation. Note
that if one of the above checks yields a change in the edge matrix then this may have
consequences for other vertices and hence we iterate the above checks until no further
changes arise.
Now suppose we have removed as much uncertainty from the edge matrix as we could,
but we can still find a pair i, j that is uncertain. Then we try both possibilities for this
pair:
 20

1. we make i, j an edge, update demand and supply accordingly, and call a new instance
of the recursor;

2. on return, we make i, j a non-edge, update supply and demand lists, and again call
a new instance of the recursor;

3. on return from this second attempt, we quit, as there is nothing else we can do.

Finally, if we managed to remove all uncertainty then C is now a good graph and we
know all edges within the set T ∪ C. This allows us to find the Gram matrix N for the
projection of the vertex set of C into the orthogonal complement W ⊥ of W = ⟨T ⟩, which
we can then check for semi-positive definiteness and rank. We compute this Gram matrix
N as follows. First of all, the projection of the vertex ci to W ⊥ is the vector vi = ni − wi,
where wi = projW (ci). Note that the six vertices in C ∩ ˆT are contained in W and so they
have zero projection to W ⊥. Therefore, we only need to take the remaining eight vertices
c7, c8, . . . c14 from further, and so N is of size 8 × 8. The entry of N corresponding to
the pair i, j equals to vi · vj = ci · cj − wi · wi = ci · cj − wi · cj. Recall that the first term
(minuend) here is equal to 1, or 2
7 , or − 1
14 when, correspondingly, ci and cj coincide, or
they form and edge in C, or they form a non-edge. The second term (subtrahend) can
be computed in the matrix form as ripT
j , where the vectors ri and pj = rjP are known,
since we used them to check compatibility of ci and cj. Thus, we have all the necessary
ingredients for this calculation and can readily compute N .
Note that we need to do this calculation exceedingly rarely, so we approximate semi-
positive definiteness in a crude way by simply checking that the determinants of the
principal minors of N are non-negative. We also compute the rank of N and check that
the sum of the ranks of M (Gram matrix of T ) and N does not exceed the total embedding
dimension of 34. Since |T ∪ C| = 38, this latter condition is super strong and in fact it
takes no survivors, and so all configurations are eliminated at this stage, completing the
calculation.

9 Choosing Q

We have described above a multi-stage process of eliminating possible G = srg(85, 14, 3, 2)
by enumerating and checking triple unions T = Sx ∪ Sy ∪ Sz or, in harder cases, T ∪ C,
where C = G1(t) and t = t13 ∈ T . Note that we start it all with a 3-clique Q = {x, y, z},
whose existence is guaranteed. In this short section we describe an improvement to our
algorithm, whereby we select Q in a controlled way and this results in disappearing of a
significant number of segment triples we need to consider.
Recall that Q can be chosen for any x ∈ G by selecting an edge yz in G1(x) that is
not contained within the good graph G1(x) in a larger clique. For each of our 39 types of
good graphs, H, we pre-select a favourite edge yz in H, not contained in a larger clique.
We will call the segment S = H \ yz the favourite segment for the good graph H.

Proposition 9.1. The maximal 3-clique Q = {x, y, z} in G can be chosen so that at least
one of the following holds:

(a) yz is the favourite edge in G1(x); or

(b) xz is the favourite edge in G1(y); or

(c) xy is the favourite edge in G1(z).

That is, in the triple of segments {Sx, Sy, Sz} at least one segment is favourite for its good
graph.

The proof is immediate, and in fact, we could have claimed just one of the three
options. However, the above symmetric form is needed because we only consider ordered
triples of segments Sx, Sy, and Sz. Namely, we assume that Sy does not precede Sx in

21

the list of segments and, similarly, Sz does not precede Sy. If we simply select yz to be
favourite in G1(x) then we cannot be sure that Sy and Sz do not precede Sx. However,
we can, clearly, change the order of vertices in Q, so that the order of three segments in T
is the correct one, and manifestly, the symmetric condition from Proposition 9.1 is then
maintained.

How do we select the favourite edge yz in each good graph H? Our preference is for
an edge such that both handles in the segment S = H \ yz are non-edges (segment type
(4, 4)). In a small number of good graphs, such a choice is impossible, in which case we
select the favourite edge yz so that the first handle in S is an edge and the second handle
is a non-edge (segment type (6, 4)) and this is always possible. So we never need to select
a segment type (6, 6) as our favourite.
The consequence of such a choice is that at least one handle in T is guaranteed to be a
non-edge, and then, because of our ordering of segments, where the segments of type (6, 6)
precede the segments of type (6, 4), which in turn precede the segments of type (4, 4), we
can be sure that the handle X = Sy ∩ Sz is definitely a non-edge. The advantage of
this is that we never encounter the largest possible big enumeration trees and also this
guarantees that our count of 8 additional vertices for t ∈ X is correct.
Our approach with favourite edges also eliminates all triples of segments, where none
of the segments is favourite. Overall, this improvement to the enumeration algorithm
shaves off, by our estimate, close to two orders of magnitude from the total run time, and
hence it contributes significantly to making the enumeration feasible.

10 Conclusion

We do not include in this paper the full enumeration code we produced, as it is quite
long. It can be found on GitHub [11]. We ran it in GAP on 96 cores in four servers in the
School of Mathematics at the University of Birmingham continuously for over a year from
November 2023 to January 2025. Individual cases of segment pairs took anywhere from
several second to several months on a single core. The longest 21 cases had to be split
up further between many cores so they could be completed. This final calculation used a
slight modification of the same code. The longest of the 21 cases took about a month on
32 cores.
As we hopefully already made clear, none of the configurations T or T ∪ C survived
the complete checks, and this means that srg(85, 14, 3, 2) does not exist.

Can this method be generalised and used to study other unresolved case of strongly
regular graphs? This remains to be seen. For it to be successful, we need to have a
relatively low embedding dimension and at the same time a substantial part of the graph
needs to be tight enough so it could be enumerated within a reasonable amount of time.
One possible candidate is Conway’s srg(99, 14, 1, 2)2.

References

[1] A.E. Brouwer. Parameters of strongly regular graphs.
https://www.win.tue.nl/aeb/graphs/srg/srgtab.html.

[2] Andries E. Brouwer, Arjeh M. Cohen, and Arnold Neumaier. Distance-Regular
Graphs. Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge / A Series
of Modern Surveys in Mathematics. Springer Berlin, 1 edition, 1989.

[3] F.C. Bussemaker, S. ˇCobelji´c, D.M. Cvetkovi´c, and J.J. Seidel. Cubic graphs on ≤ 14
vertices. Journal of Combinatorial Theory, Series B, 23(2):234–235, 1977.

2Apparently, John Conway was interested in this set of parameters and he even offered a monetary reward
to anyone who could enumerate this case of strongly regular graphs.

22

[4] I.A. Faradzhev. Constructive enumeration of homogeneous graphs. Uspehi Mat.
Nauk, 31(1(187)):246, 1976.

[5] Peter Frolkoviˇc. Numerical recipes: The art of scientific computing. Acta Applicandae
Mathematica, 19(3):297–299, 1990.

[6] The GAP Group. GAP – Groups, Algorithms, and Programming, Version 4.12.2,
2022. https://www.gap-system.org.

[7] Chris Godsil. Algebraic combinatorics. Chapman and Hall Mathematics Series. Chap-
man & Hall, 1 edition, 1993.

[8] Chris Godsil and Gordon Royle. Algebraic Graph Theory. Springer New York, NY,
1 2001.

[9] David M. Goldschmidt. Automorphisms of trivalent graphs. Annals of Mathematics,
111(2):377–406, 1980.

[10] D.V. Paduchikh. On the automorphisms of the strongly regular graph with parame-
ters (85,14,3,2). Discrete Mathematics and Applications, 19(1):89–111, 2009.

[11] Sergey Shpectorov and Tianxiao Zhao. Enumeration of SRG(85,14,3,2).
https://github.com/shpectorov/srg-85-14-3-2, March 2025.

A Enumeration trees

In this paper, we provide a rather detailed description of the enumeration code we used.
This is because the efficient realisation of the huge enumeration is what makes this entire
project feasible. In this appendix we describe the enumeration trees used in the algorithm.
Recall that it consists of four steps. and the enumeration trees are used for the first two.
At Step 1, we use an enumeration tree to go through all possible ways to attach a matching
to a pair of segments Sx ∪ Sy joined at the handle Z = Sx ∩ Sy. The matching we need
to add is between the cores Cx in Sx and Cy in Sy corresponding to the handle Z.
We have two cases: (a) if Z is an edge then |Cx| = |Cy| = 6; and if Z is a non-edge
then |Cx| = |Cy| = 4. Correspondingly, we have two trees and we refer to them as the
small trees.
Let n ∈ {4, 6} be the size of the cores. The record at the node of a small tree has the
following structure.
 Level k

Neighbour m

Brother bro

Son son

The level k ∈ {1, 2, . . . , n} here refers here both to the depth of this node in the tree and
the number of the vertex in Cy for which we now need to choose a neighbour in Cx. When
we operate with this node record, the neighbours of the first k − 1 vertices of Cy have
already been chosen at the lower levels of the tree and so the current neighbour m should
be different from all of those earlier neighbours.
The brother and son entries specify the tree structure: the brother entry refers to the
next node with the same parent (and hence also at the same level). If the current node
is the last one for its parent then the brother entry is set to zero. The son entry refers to
the first descendent node at the level k + 1 and it is set to zero if the current node is at
the deepest level k = n.
Clearly, the leaves of this tree correspond to complete matchings and so there are
exactly n! ∈ {24, 720} of them. Using this tree structure, we have a simple code that

23

allows us to enumerate all matchings while iteratively computing the necessary data, such
as the LDLT decomposition of the partial Gram matrix. (See Appendix B.)

We also use an enumeration tree at Step 2, where we have a segment pair Sx ∪ Sy,
complete with a matching as above, and the third segment Sz, already glued to Sx ∪ Sy
via the handles Y = Sx ∩ Sz and X = Sy ∩ Sz. At this point we need to add matchings
between the cores in Sz and Sx corresponding to the handle Y and between the cores in
Sz and Sy corresponding to the handle X.
The structure of the big tree, which allows us to to enumerate both matchings at
the same time, depends on the quad type of the segment S = Sz (see Table 2 and the
discussion there). We note that the handles Y and X are second handles in Sx and Sy
and they are the first and second handles in Sy, which is opposite to the order in Table 2.
The node record of a big tree is as follows.

Level k

Left l

Right r

Brother bro

Son son

Here k refers to the depth of the node in the tree and at the same time it refers to the
number of the vertex in the segment S \ (X ∪ Y ), where we disregard the two handles
because they are contained in Sx ∪ Sy. Hence the total depth of a big tree is 12 − 4 = 8,
regardless of quad type. Recall from Table 2 that S \ (X ∪ Y ) consists of four groups.
Depending on the group, a vertex can have no new neighbours (‘none’), only a neighbour
in Sy (‘right’), only a neighbour in Sx (‘left’), or finally a neighbour in Sx and a neighbour
in Sy (‘both’). Clearly, here ‘left’ refers to Sx and ‘right’ refers to Sy. The union of the
‘right’ and ‘both’ groups is the core of S with respect to the second handle of S (currently,
it is X = Sy ∩ Sz) and, similarly, the union of the ‘left’ and ‘both’ groups constitute the
core of S with respect to its first handle (currently, Y = Sx ∩ Sz). Hence for each node of
the big tree the entry l refers to the neighbour of this vertex in the corresponding core in
Sx (or zero, if there is no neighbour in Sx) and, symmetrically, r refers to the neighbour in
the core in Sy (or again zero if there is no neighbour there). The brother and son entries
specify the tree structure, and this is similar to what we described for small trees.
These trees are substantially bigger (hence the name). The number of leaves (nodes
at the bottom level 8) is (6!)2 = 7202 = 518400 for segments of type (6, 6), it is 6! · 4! =
720 · 24 = 17280 for segments of type (6, 4), and it is (4!)2 = 242 = 576 for segments of
type (4, 4). So it is really fortunate that we never need to deal with segments S = Sz of
type (6, 6), as the handle X = Sy ∩ Sx is always a non-edge in the final enumeration. The
total size of the tree varies depending on the exact quad type.
Again, this convenient tree structure allows for a rather uncomplicated enumeration
code allowing us to consider all possible matchings between Sz and the other two segments
in a single loop.

B Implementation of the LDLT algorithm

In this appendix, we provide details of the implementation of the LDLT algorithm. Gen-
erally, the purpose of this algorithm is to decompose a symmetric matrix A as a product
A = LDLT , where L is a lower unitriangular matrix and D is diagonal. We use this to
decide whether A is semi-positive definite, namely, this is so when all (diagonal) entries
of D are non-negative. We apply this to the Gram matrix A = M of the given set of

24

vectors T = Sx ∪ Sy ∪ Sz, which must be semi-positive definite, or else we can eliminate
this particular configuration.
We use the iterative version of the LDLP algorithm3, that is, we start with the empty
set and then extend it by one vertex at a time. As we do it, we extend the current
matrices L and D accordingly, by one dimension. Hence, at the moment when we deal
with k vectors from T , our matrices L and D are of size k × k and LDLT coincides with
the principal k × k minor of M .
Whenever we discover that M is not semi-positive definite, we interrupt right away
and switch to the next configuration T . On the other hand, if M turns out to be semi-
positive definite, the general algorithm involves a further step, adding further vertices to
the 30 vertices of T . At this step, we use a different technique based on the projection
map to the subspace spanned by T . The matrix R = L−1 is needed to determine this
map and we compute R iteratively alongside L and D.
Now that we explained what we are doing in this algorithm, we are ready to present
the code.

#
# extending the LDLT decomposition by one dimension
# if semi positive definite
#
# based on Madeleine Whybrow’s code
#

M:=List([1..30],i->List([1..30],j->0));
L:=List([1..40],i->List([1..30],j->0));
D:=[];

R:=List([1..30],i->List([1..30],j->0));
Id:=IdentityMat(30);

AddOne:=function(r)
local n,i,sum,j;
n:=Length(r);

for i in [1..n] do
sum:=0;
for j in [1..i-1] do
sum:=sum+L[n][j]*L[i][j]*D[j];
od;
if i<n then
if D[i]=0 then
if r[i]=sum then
L[n][i]:=0;
else
return false;
fi;
else
L[n][i]:=(r[i]-sum)/D[i];
fi;
else
L[n][n]:=1;
D[n]:=r[n]-sum;

3We developed our iterative version starting from the code kindly given to us by M. Whybrow.

25

if D[n]<0 then
return false;
fi;
fi;
od;

for i in [1..n] do
M[n][i]:=r[i];
M[i][n]:=r[i];
od;
R[n]:=Id[n];
for j in [1..n-1] do
R[n]:=R[n]-L[n][j]*R[j];
od;

return true;
end;

Note that we build the Gram matrix M alongside L, D, and R = L−1, as we add each
time the new row r of M , which serves as the input to the function AddOne and which
also provides the next size n of L, D, M , and R. Also note that we only keep the diagonal
entries of D, so this is a 1-dimensional array in the code. We treat all the outputs L, D,
R, and M as global variables, as we want to have an easy access to them from our main
enumeration code. It also saves a bit of time as we do not pass them back and forth as
arguments.
The function AddOne returns true if the extended matrix M is semi-positive definite
and it returns false otherwise. Note that the latter can happen in two different ways.
First, as we discussed above, the new entry in D may be negative, which clearly means
that M is not semi-positive definite. The second possibility amounts to the algorithm
being unable to construct the extended L and D. We now show that this may only
happen when M is not semi-positive definite, and so we get our answer anyway.
Note that in this lemma we again treat D as a diagonal matrix.

Lemma B.1. If Dii = 0, for 1 ≤ i < n, and ri ̸= ∑i−1
j=1 LkjLijDjj then M is not
semi-positive definite.

Proof. We start by reviewing the meaning of the matrices L and D. Recall that M is the
Gram matrix of a subset of T with respect to the dot product, but for extra generality, we
view it simply as the Gram matrix of the standard basis e1, e2, . . . , en in Rn with respect
to a symmetric bilinear form (·, ·). Consider the linear map ψ : Rn → W = ⟨T ⟩ sending ei
to ti. Then the required symmetric bilinear form on Rn is defined by (e, f ) := ψ(e) · ψ(f )
for e, f ∈ Rn. Clearly, M is the Gram matrix of (·, ·) with respect to the standard basis
e1, e2, . . . , en.
We now apply the Gram-Schmidt orthogonalisation process to the form (·, ·) to find
an orthogonal basis u1, u2, . . . , un in Rn. Namely, u1 = e1 and, inductively,

ui = ei −
 i−1∑

j=1 Lijuj,

for i = 1, 2, . . . , n. Here
 Lij =
 { 0, if (uj, uj) = 0;
(ei,uj )
(uj ,uj ) , otherwise.

26

Consequently, ei = ∑i
j=1 Lijuj, where Lii = 1. This clarifies the meaning of the lower
triangular matrix L; the diagonal entries from D are given simply by Dii = (ui, ui) for all
i. The basis u1, u2, . . . , un is indeed orthogonal provided that the form (·, ·) is positive
definite or semi-positive definite. Under this condition, if Dii = (ui, ui) = 0 then the
vector ui is in the radical of the form, i.e., it is orthogonal to the entire Rn. In particular,
for k > i, we have 0 = (ek, ui) = (ek, ei−∑i−1
j=1 Lijuj) = (ek, ei)−∑i−1
j=1 Lij(ek, uj) = Mki−
∑i−1
j=1 LjiLkjDjj, since (ek, uj) = LkjDjj for all j ≤ k. This yields Mki = ∑i−1
j=1 LjiLkjDjj,
and the contradiction shows that the form is not semi-positive definite.
It remains to notice that when this is first encountered we have n = k and Mki = ri.

Hence indeed our function AddOne returns false exactly when the extended Gram
matrix M is not semi-positive definite.
We would like to retain the map ψ : Rn → ⟨t1, t2, . . . , tn⟩ introduced in this proof to be
used elsewhere in the paper. Typically, it will be with the full set T , that is, with n = 30.
Then u ∈ R30 can be viewed simply as the coefficient vector of ψ(u) with respect to the
spanning set T = {t1, t2, . . . , t30} of W = ⟨T ⟩. Since the dot product is positive definite
on W , the vectors ui with Dii = (ui, ui) = 0 are in the kernel of ψ and, in fact, such
vectors ui form a basis of ker ψ. On the other hand, the vectors ψ(ui), where Dii ̸= 0,
form an orthogonal basis of W .
The final comment in this section concerns the meaning of the matrix R = L−1. Note
that we have ei = ∑i
j=1 Lijuj = ∑n
j=1 Lijuj, since L is lower triangular. This means
that L is the transition matrix from the orthogonal basis {u1, u2, . . . , un} to the standard
basis {e1, e2, . . . , en} of Rn. Correspondingly, R = L−1 is the transition matrix from the
standard basis to the orthogonal basis {u1, u2, . . . , un}. In other words, the row Ri of
R provides the coefficients of ui with respect to the standard basis, or in simpler terms,
Ri = ui.

C Projection matrix

If the Gram matrix of the full set T happens to be semi-positive definite then we have
to consider vertices beyond T and, at this stage, our strategy of checking semi-positive
definiteness iteratively is not as effective, because we are not working with a pre-selected
segment and, consequently, the graph structure on the additional set of vertices is not
known. Hence we need another approach, and it involves computing the orthogonal
projection of the additional vertices to the subspace W spanned by T . For a vertex
u, we will have the list of its neighbours in T and hence we can form the vector r =
(r1, r2, . . . , rn), where n = |T | = 30 and ri = u · ti is the value of the dot product between
u and the ith vertex ti ∈ T . Hence

ri =
 



 2
7 , if u ∼ ti,

− 1
14 , otherwise

We need to find a matrix P such that p = rP is the list of coefficients of the projection
projW (u) of u to W with respect to the spanning set T = {t1, t2, . . . , tn}. (That is,
projW (u) = ψ(p), where ψ : Rn → W is the linear map introduced in Appendix B.) We
need to make two comments. First, since T may in some cases be linearly dependent, the
vector p is in general not unique. Secondly, for the same reason, some vectors r need to
be eliminated because they lead to non semi-positive definiteness of the inner product on
the expanded space ⟨T ∪ {u}⟩. This happens when the entries in r yield non-orthogonality
of u to some linear combinations of the vectors ti that have zero length.
Here is our function:
 27

# Vertex projection

P:=List([1..30],i->List([1..30],j->0));

ComputeProjMat:=function()
local i;
P:=0*IdentityMat(30);

for i in [1..30] do
if D[i]<>0 then
P:=P+TransposedMat([R[i]])*[R[i]]/D[i];
fi;
od;

end;

Note that we again treat the output, the projection matrix P , as a global variable, because
we want to have easy access to it from the main code.
Here is the lemma that justifies our method of computing P . Recall that when we
need P we have already determined the matrices L (strictly lower triangular) and D
(diagonal), such that M = LDLT is the Gram matrix of the set T . Furthermore, we also
have R = L−1. Let ui = Ri be the ith row of the matrix R. Recall that u1, u2, . . . , un is
the orthogonal basis of Rn with respect to the form (·, ·) with the Gram matrix M .
For generality, we allow an arbitrary n = |T |, but of course, in our application n = 30.
Correspondingly, all matrices are n × n. Let N = {i ∈ {1, 2, . . . , n} | Dii ̸= 0}.

Lemma C.1. For a vertex u /∈ T identified by the vector r, with ri = u · ti, i = 1, 2, . . . , n,
the projection of u onto W = ⟨T ⟩ = ⟨t1, t2, . . . , tn⟩ coincides with w = ∑n
i=1 piti, where
p = (p1, p2, . . . , pn) = rP and
 P = ∑

i∈N
 1
Dii RT
i Ri.

Proof. The projection vector w is identified by the property that w ·v = u·v for all v ∈ W .
In particular, w · ti = u · ti = ri, for i = 1, 2, . . . , n. Transferring this into Rn, we are
looking for a row vector p (coefficients of w with respect to the set T ) such that pM = r.
If M is not positive definite, the set T is linearly dependent, and so such a vector p is not
unique, but it is unique if we select it in the subspace ⟨ui | i ∈ N ⟩, which is a complement
to the radical of the form (·, ·). We claim that the formulae in the lemma give us exactly
such a vector.
Indeed, suppose that p is a row vector such that pM = r and p is a linear combination

28

of the vectors ui, i ∈ N . Using that ui = Ri, for all i, we get

p = ∑

i∈N
 (p, ui)
(ui, ui) ui

= ∑

i∈N
 (p, Ri)
(Ri, Ri) Ri

= ∑

i∈N
 (p, Ri)
Dii Ri

= ∑

i∈N
 1
Dii (pM RT
i )Ri

= pM ∑

i∈N
 1
Dii RT
i Ri

= r ∑

i∈N
 1
Dii RT
i Ri.

Note that, in line 4 of this calculation, the product pM RT
i is a 1 × 1 matrix with the entry
equal to (p, Ri), and so we have a four-term matrix product here, which allows us to use
associativity and distributivity in the following line.

Thus, we have the correct formula for the projection matrix.

29
