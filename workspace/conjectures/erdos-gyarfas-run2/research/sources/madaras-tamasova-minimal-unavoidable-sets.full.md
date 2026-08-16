<!-- source: https://doi.org/10.7494/opmath.2018.38.6.859 | converted from PDF -->

Opuscula Math. 38, no. 6 (2018), 859–870
https://doi.org/10.7494/OpMath.2018.38.6.859 Opuscula Mathematica

MINIMAL UNAVOIDABLE SETS OF CYCLES
IN PLANE GRAPHS

Tomáš Madaras and Martina Tamášová

Communicated by Ingo Schiermeyer

Abstract. A set S of cycles is minimal unavoidable in a graph family G if each graph
G ∈ G contains a cycle from S and, for each proper subset S′ ⊂ S, there exists an inﬁnite
subfamily G′ ⊆ G such that no graph from G′ contains a cycle from S′. In this paper, we
study minimal unavoidable sets of cycles in plane graphs of minimum degree at least 3 and
present several graph constructions which forbid many cycle sets to be unavoidable. We also
show the minimality of several small sets consisting of short cycles.

Keywords: plane graph, polyhedral graph, set of cycles.

Mathematics Subject Classiﬁcation: 05C10.

1. INTRODUCTION

Throughout this paper, we consider connected graphs without loops and multiple
edges, which are planar (that is, they can be drawn in the plane without crossing their
edges). A particular plane drawing D of a planar graph G is represented by a triple
(V, E, F ) where V is the vertex set, E is the edge set and F is the set of faces. Two
faces are adjacent if they share a common edge. Each face α ∈ F is described by its
facial walk which is a clockwise-oriented closed walk v1, e1, v2, e2, . . . , ek−1, vk, ek, v1
whose vertices and edges are incident with α and, for all i ∈ {1, . . . , k}, ei follows
ei−1 (indices modulo k) in the counter-clockwise order of edges around vi in D; in the
sequel, we will consider facial walks simply as clockwise-ordered lists of their vertices.
The number k is called the size of α, and is denoted by deg(α). A face of size k (at
least k) is further referred as k-face (≥ k-face); similarly, a vertex of degree k (at least
k or at most k) is a k-vertex (≥ k-vertex or ≤ k-vertex, respectively). A face whose
facial walk is a cycle will be called nice face. Two adjacent faces form a nice pair if
their common vertices are exactly the endvertices of the common edge.

c⃝ Wydawnictwa AGH, Krakow 2018 859

860 Tomáš Madaras and Martina Tamášová

By Ck, k ≥ 3, we denote the cycle on k vertices. For positive integers k1, . . . , kℓ ≥ 3,
we set Sk1,...,kℓ = {Ck1 , . . . , Ckℓ};

in addition, Sk1,...,kℓ,k+ = {Ck1 , . . . , Ckℓ } ∪ {Cl : l ≥ k}

(here we also allow ℓ = 0).
We introduce the following deﬁnition: A set S of cycles is minimal unavoidable in
a graph family G if each graph G ∈ G contains a cycle from S and, for each proper
subset S′ ⊂ S, there exists an inﬁnite subfamily G′ ⊆ G such that no graph from
G′ contains a cycle from S′. This notion provides a certain uniﬁed framework for
the study of the cycle structure of graphs of particular families. For example, the
Erdős–Gyárfás conjecture says that the set S{2k: k≥2} is unavoidable in the family of
graphs of minimum degree ≥ 3 although it is not known whether is also minimal (see
the discussion in [1] and its negative results for cycle lengths being powers of q ≥ 3).
The results of [4] yield that S4,8,16,32,64,128 is unavoidable in the family of 3-connected
cubic plane graphs, with the possible minimal unavoidability of S4,8,16,32 (see also [3]).
The aim of this paper is to explore minimal unavoidable sets of cycles in plane
graphs. It is well known that each plane graph of minimum degree at least 3 contains
a k-cycle (in fact, a boundary of a k-face), 3 ≤ k ≤ 5; moreover, it is not hard to
construct inﬁnite families of plane graphs of minimum degree 3 which avoid any two
cycles from S3,4,5. Thus, in that family, the set S3,4,5 is minimal unavoidable. Apart
of this result, it seems that a systematic research of minimal unavoidable sets in
plane graphs was not performed. We contribute to this topic by specifying the large
collection of cycle sets which are not unavoidable (see Section 2) and by showing that
the sets S3,4,11, S3,4,8,9, S3,4,6,8, S3,4,7,9 and S3,5,6,7 are minimal unavoidable (Section 3).
The paper concludes with several open problems.

2. NEGATIVE RESULTS

The main tool for showing that some sets of cycles are not unavoidable in the family G3
of plane graphs of minimum degree at least 3 is the following construction: take a plane
graph G which does not contain cycles of lengths ℓ1, . . . , ℓk, and let x be an arbitrary
vertex on the outerface of G. Now, take n copies of G and identify all vertices which
are counterparts of x; since the resulting graph Gn is planar, one has just take care to
choose G such that Gn ∈ G3. In this way, we obtain an inﬁnite sequence {Gn}∞
n=1 of
graphs of G3, none of which containing cycles of lengths ℓ1, . . . , ℓk and ℓ ≥ c(G) + 1
where c(G) is the circumference (the length of the longest cycle) in G.
The source graph G is often built from a smaller plane graph using several operations
which replace parts of graphs (mostly vertices and edges) with another conﬁgurations.
The general operations are the following ones (see Figure 1):
– truncation: each k-vertex is replaced by k-face, resulting in plane cubic graph,
– rectiﬁcation: each k-vertex is replaced by k-face, resulting in plane 4-regular graph,
– edge-truncation: each edge is replaced by 6-face,
– edge-pentagonalization: after edge-truncation, each of new 6-faces is divided by
a new edge into two 5-faces.

Minimal unavoidable sets of cycles in plane graphs 861

Fig. 1. Four operations on plane graphs

In addition, we use particular operations which replace 3-faces of a plane graph
with suitable small graph (see Figure 2; the original vertices of 3-face correspond to
2-vertices of considered replacement graph):

– △+ -substitution: each 3-face is replaced by a 6-gon with three attached triangles,
– △− -substitution: works similarly, just the replacement graph is a 5-gon with two
attached triangles; note that, unlike △+ -substitution, the resulting graph depends
on the way how 3-faces of the original graph were replaced,
– △· -substitution: as above, just the replacement graph is the graph of 3-cube without
a vertex.

Among small starter-graphs which are used in the subsequent constructions, there
are well-known graphs of ﬁve Platonic polyhedra, and, further, soccerball graph (the
truncated icosahedron graph).
For planar graphs of minimum degree at least 3, we will construct, in the above
manner, a suitable sequence {Gn}
∞
n=1 for the following sets of cycles:

(a) If S ⊂ S5+, then set G = K4.
(b) If S ⊂ S3,5,7,9+, then choose G to be the graph of 3-cube.
(c) If S ⊂ S4,...,9,61+, then choose G to be the truncated dodecahedron graph.
(d) If S ⊂ S4,5,13+, then choose G to be the truncated tetrahedron graph.

862 Tomáš Madaras and Martina Tamášová

(e) For S ⊂ S3,4,6,7,21+, choose G to be dodecahedron graph.
(f) For S ⊂ S3,4,7,8,61+, choose G to be soccerball graph.
(g) For S ⊂ S3,4,9,85+, choose G to be the graph on Figure 3.
(h) For S ⊂ S3,4,10,51+, choose G to be edge-pentagonalized graph of 3-cube.
(i) For S ⊂ S4,5,10,...,19,180+, choose G to be △+ -substituted truncated dodecahedron
graph.
(j) For S ⊂ S4,8,...,14,141+, choose G to be △− -substituted truncated dodecahedron
graph.
(k) For S ⊂ S3,5,7,...,14,141+, choose G to be △· -substituted truncated dodecahedron
graph.
(l) For S ⊂ S3,5,6,8,10,81+, choose G to be 80-vertex plane cubic graph having only
4- and 7-faces such that 4-faces are not adjacent, see Figure 4.
(m) For S ⊂ S3,6,15+, choose G to be plane cubic graph on 14 vertices consisting of
six 5-faces and three nonadjacent 4-faces, see Figure 5.
(n) For S ⊂ S3,6,9,145+ , choose G to be plane graph constructed by circular gluing of
four copies of the conﬁguration on Figure 6.

Fig. 2. The △+ -, △− - and △· -substitutions

Fig. 3. The basic graph for the set S3,4,9,85+

Minimal unavoidable sets of cycles in plane graphs 863

Fig. 4. The basic graph for the set S3,5,6,8,10,81+

Fig. 5. The basic graph for the set S3,6,15+

Fig. 6. The one-fourth of basic graph for the set S3,6,9

These results imply, in particular, that Sk,l is never unavoidable in the family G3.

3. MINIMAL UNAVOIDABLE SETS IN G3

Our main positive result is the following

Theorem 3.1. The set S3,4,11 is minimal unavoidable in G3.

Proof. By contradiction. Consider a plane graph G = (V, E, F ) of minimum degree at
least 3 which has neither a 3-cycle nor a 4-cycle nor else an 11-cycle.

864 Tomáš Madaras and Martina Tamášová

For the purposes of this proof, we deﬁne forbidden clusters of small faces of G (see
Figure 7; note that all vertices on the boundary of each cluster are distinct):

– three 5-faces forming a linear chain,
– two 6-faces and one 5-face incident with common 3-vertex,
– two 5-faces and one 7-face incident with common 3-vertex,
– a 7-face forming a nice pair with a 6-face,
– an 8-face forming a nice pair with a 5-face.

Fig. 7. Five forbidden clusters of faces

It is easy to see that each forbidden cluster contains an 11-cycle.
We proceed by Discharging Method: according to the consequence of Euler’s
formula on the number of vertices, edges and faces of a plane graph,
∑

v∈V (2 deg(v) − 6) + ∑

α∈F (deg(α) − 6) = −12

assign to vertices and faces of G initial charges µ : V ∪ F → Z such that
µ(v) = 2 deg(v) − 6 for each v ∈ V and µ(f ) = deg(f ) − 6 for each f ∈ F . Thus∑

x∈V ∪F µ(x) = −12.

Next, the charges of vertices and faces are redistributed locally in the way that the
total sum of the charges remains the same. This redistribution is done by the following
discharging rules:

Rule 1: Every k-vertex, k ≥ 4, sends 1 to each incident 5-face.

Rule 2: Let x be a k-vertex, k ≥ 4 which has a positive charge ̂µ(x) after application
of Rule 1. Denote by ℓ(x) the number of 5-faces with the property that each of them

Minimal unavoidable sets of cycles in plane graphs 865

is incident with a 3-vertex y which is the neighbour of x. Then x sends ̂µ(x)
ℓ(x) to every

such 5-face provided ℓ(x) > 0; if ℓ(x) = 0, no charge is transferred.

Rule 3: Let α be a 7-face having a common edge xy with a 5-face β which is incident
only with 3-vertices. Then α sends 1
3 through xy to β.

Rule 4: Let α be an ≥ 9-face having a common edge xy with a 5-face β which is
incident only with 3-vertices. Then α sends 1
2 through xy to β.

Before the analysis of ﬁnal charges ̃µ : V ∪ F → Q of vertices and faces, we prove
the following auxiliary statements:

Proposition 3.2. Three transfers of a charge from a face α through three consecutive
edges on face boundary of α are not possible.

Proof. In the opposite case, there exist three consecutive 5-faces β, γ, ρ adjacent to α.
Due to the formulation of Rules 3 and 4, all vertices of these faces are distinct; but
then β, γ, ρ form a forbidden cluster, a contradiction.

Proposition 3.3. Let x be a k-vertex, k ≥ 6, incident with at least two ≥ 6-faces, or
a 5-vertex incident with at least three ≥ 6-faces. Then the amount of charge sent from
x to a 5-face by Rule 2 is at least 1
3 .

Proof. In the former case, ̂µ(x) ≥ 2k − 6 − (k − 2) = k − 4 and ℓ(x) ≤ k, thus the
contribution of x by Rule 2 is at least k−4
k ≥ 1
3 ; in the latter case, the contribution is
at least 2·5−6−2·1
5 = 2
5 > 1
3 .

Next, by case analysis, we show that ̃µ is nonnegative function, yielding a contra-
diction because −12 = ∑

x∈V ∪F µ(x) = ∑

x∈V ∪F ̃µ(x) ≥ 0.

Case 1. Let v be a vertex of G.

Case 1.1. If v is a 3-vertex or a k-vertex with k ≥ 6 then ̃µ(v) = µ(v) = 2 · 3 − 6 = 0
or ̂µ(v) ≥ 2k − 6 − k · 1 = k − 6 ≥ 0 which yields, due to Rule 2, ̃µ(x) ≥ 0.

Case 1.2. Let v be a 4-vertex. Assume that v is incident with three 5-faces
[v1vv2w1w2], [v2vv3w3w4], [v3vv4w5w6]. If all wi, i = 1, . . . , 6 are distinct and none
of them coincides with a vertex from {v1, . . . , v4}, then these 5-faces form a forbidden
cluster. If there are i ∈ {1, . . . , 6}, j ∈ {1, . . . , 4} such that wi = vj, then v and two
of its neighbours form a 3-cycle. Finally, if wi = wj for some i, j ∈ {1, . . . , 6}, then
wi, v and some two neighbours of v form a 4-cycle. Therefore, we conclude that v is
incident with at most two 5-faces, yielding ̃µ(v) ≥ 2 · 4 − 6 − 2 · 1 = 0.

Case 1.3. Let v be a 5-vertex. By similar argument as in Case 1.2, we obtain that v is
incident with at most three 5-faces, thus ̂µ(v) ≥ 2 · 5 − 6 − 3 · 1 > 0 which also yields
̃µ(x) ≥ 0.

Case 2. Let α = [x1x2x3x4x5] be a 5-face.

Case 2.1. If α is incident with an ≥ 4-vertex, then, by Rule 1, ̃µ(α) ≥ −1 + 1 = 0.

866 Tomáš Madaras and Martina Tamášová

Case 2.2. Assume that α is incident only with 3-vertices (denote by yi, i = 1, . . . , 5
the neighbour of xi distinct from xi−1, xi+1; observe that all xi, yi are distinct) and
let β, η, γ, ρ and ω be faces around α which contain the edge x1x2, x2x3, x3x4, x4x5
and x5x1. Note that α cannot be adjacent with an 8-face (such an 8-face must be
nice and, due to absence of 3-and 4-cycles, it forms a forbidden cluster with α).
If α is adjacent with at least two ≥ 9-faces or with at least three 7-faces or else
with one ≥ 9-face and two 7-faces, then, by Rule 4 or 3, ̃µ(α) ≥ −1 + 2 · 1
2 = 0 or
̃µ(α) ≥ −1 + 3 · 1
3 = 0 or else ̃µ(α) ≥ −1 + 1
2 + 2 · 1
3 > 0. Hence, in subsequent analysis,
we suppose that these possibilities do not occur. Then α is adjacent with (at least)
three ≤ 6-faces. Taking into account the symmetries, we discuss several possibilities
for degrees of α and neighbouring faces.

Case 2.2.1. Around α, there are two nonadjacent 5-faces, say β = [x1x2y2uy1] and
γ = [x3x4y4vy3]. To prevent α, β, γ to form a forbidden cluster, some of their vertices
must coincide, which yields, up to symmetry, the following cases to analyze:
If u = v, then the neighbours of y1 and y5 incident with ω are distinct from all
xi, yi and u. Taking into account the paths y5x5x4y4uy3x3x2x1y1, y5x5x1x2x3x4y4uy1,
ω is neither a 5-face nor a 6-face nor else a 7-face (note that, in this case, ω is nice
and none of its vertices coincides with u, hence, it forms a forbidden cluster with
α, β). The same argument holds for the face ρ. Hence, both ω and ρ are ≥ 9-faces,
a contradiction.
If u = y4, then again ω cannot be 5-, 6- or 7-face (as an 11-cycle always appears
then), hence it is an ≥ 9-face. Further, observe that η cannot be a 5-face [x2x3y3zy2],
as it forms an 11-cycle x1x5x4x3x2y2zy3vy4y1x1. If η is a 6-face [x2y2zwy3x3], then ρ
is neither a 5-face nor a 6-face nor else a 7-face (because the paths x5x1x2y2zwy3vy4,
x5x4x3y3wzy2y4 and x5x1x2x3y3vy4 form, together with a part of the boundary of ρ,
an 11-cycle); hence, it must be an ≥ 9-face. Finally, η cannot be a 7-face, as the part
of its boundary forms, together with path x2x1x5x4vy3, an 11-cycle. Thus we obtain
that α is always adjacent with at least two ≥ 9-faces, a contradiction.

Case 2.2.2. Around α, there are two adjacent 5-faces, say β = [x1x2y2uy1] and
η = [x2x3y3vy2] (note that, due to Case 2.2.1, γ, ρ and ω are ≥ 6-faces). Then β, η
form a nice pair. Consider the face γ and discuss ﬁrst the case when γ = [x3x4y4wzy3]
is a 6-face and y4, w, z are distinct from v, u, y1, y2. Then x1y1uy2vy3zwy4x4x5x1 is
an 11-cycle, thus, some of the mentioned vertices must coincide. Taking into account
the absence of 3- and 4-cycles, we get that either z = y1 or u = w or else w = y1.
Let z = y1. If ρ is a 6-face, then it is either incident with y1 (which yields a 3- or
4-cycle) or it forms a forbidden cluster with α and γ. Similarly, if ρ is a 7-face, then
it either forms a forbidden cluster with γ or is incident with y1 or w (this, however,
yields a 3- or 4-cycle). Hence, ρ is an ≥ 9-face. Next, if ω is a 6-face, then it forms,
with α, β and η, a face cluster containing an 11-cycle, and if it is a 7-face, then it
forms forbidden cluster with α and β. Therefore ω is also an ≥ 9-face, a contradiction.
If u = w, then ρ is neither a 6-face (as it either forms a forbidden cluster with γ
and α or has three common vertices with γ resulting in a 3- or 4-cycle) nor a 7-face
(from similar reason with respect to γ), hence, it is an ≥ 9-face. Now ω being a 6- or

Minimal unavoidable sets of cycles in plane graphs 867

a 7-face forms either a forbidden cluster (with α, β, η or α, β) or yields a 3- or 4-cycle
in G. Thus, it is also an ≥ 9-face, a contradiction.
The same conclusion (following the same argumentation) for the sizes of ρ and ω
is obtained also in the case when w = y1.
The above considerations then exclude γ from being a 6-face, which applies also
to ω due to symmetry. Both γ and ω are thus ≥ 7-faces. Note that if γ is a 7-face,
then it either forms a forbidden cluster with η and α, or y2 and y4 are adjacent; in
the latter case, however, the face ρ is not a 6-face as it would form a forbidden cluster
with γ, or a 3- or 4-cycle. We can conclude that β, η are the only ≤ 6-faces around α,
a contradiction.

Case 2.2.3. α is incident with exactly one 5-face β = [x1x2y2uy1]. Assume ﬁrst that
γ = [x3x4y4vzy3] is a 6-face having no common vertices with β. If η = [y2x2x3y3wt]
is a 6-face, then it either forms a forbidden cluster with α, γ or, when t = y4, the
11-cycle uy1x1x5x4y4wy3x3x2y2u. In addition, if η = [y2x2x3y3wts] is a 7-face, then
it either forms a forbidden cluster with α, β or, when t = y4 or s = v, the 11-cycle
uy1x1x5x4x3y3wtsy2u. Hence η is necessarily an ≥ 9-face. Consider now the faces
ρ, ω. If ω = [y5x5x1y1pq], ρ = [y4x4x5y5rs] are both 6-faces, then either they form
a forbidden cluster with α, or s = y1 with vzy3x3x4x5y5qpy1y4v being an 11-cycle. If
ω = [y5x5x1y1pq] is a 6-face and ρ = [y4x4x5y5rsc] is a 7-face, then ρ, ω either form
a forbidden cluster, or y1 = s with cy4vzy3x3x4x5y5rsc being an 11-cycle. In addition,
if ω is a 7-face and ρ is a 6-face, then ω forms a bad cluster either with α, β or (if it it
incident with y2) with ρ. Thus we have, around α, either two ≥ 9-faces of one ≥ 9-face
and two ≥ 7-faces, a contradiction.
Next, assume that γ = [x3x4y4vzy3] is a 6-face having some common vertices with
β (this can be assumed, due to symmetry, also for the face ρ). There are six cases:
z ∈ {y1, u}, v ∈ {u, y1, y2}, and u = y4. Note that, in each of these cases, η cannot be
a 6-face, as it either forms a forbidden cluster with γ, α or has at least three common
vertices with γ, but this yields a 3- or 4-cycle in G. If η is a 7-face, then it either forms
a forbidden cluster with γ or a forbidden cluster with α, β or else a 3- or 4-cycle in
neighbourhood of α. Thus, η is always an ≥ 9-face. Similarly, ρ is not a 6-face (due to
forbidden cluster with α and γ or to appearance of short forbidden cycles), and not
a 7-face except of the case when z = u and u is incident with ρ. In that case, there is
no 11-cycle formed of some vertices of α, β, γ, ρ, but if, in addition, ω is a 6-face, then
the pair ρ, ω is nice and subsequently forms a forbidden cluster; hence α is surrounded
with ≥ 9-face and two ≥ 7-faces, a contradiction.
Hence, we may assume that both γ, ρ are ≥ 7-faces, thus η = [y3x3x2y2wz] and ω
are 6-faces. Let γ = [y4x4x3y3rqp] be a 7-face. Then either γ forms a bad cluster with
η, or they have at least three vertices in common. If w = p, then uy2pqry3x3x4x5x1y1u
is an 11-cycle. Similarly, if q = y2, then qwzy3x3x2x1x5x4y4pq is an 11-cycle, and
if y4 = w, then uy2x2x3y3zwx4x5x1y1u is also an 11-cycle. Let p = y2. Then y2 is
≥ 5-vertex and in the case when it is a 5-vertex, the face that shares the edge uy2
with β is not a 5-face (since y4 would be a 2-vertex). Thus, Rule 2 is applied with
the contribution from y2 to α being at least 1
3 , and we have, with two contributions
by Rule 3 (from γ) and Rule 3 / Rule 4 (from ρ), ̃µ(α) ≥ −1 + 3 · 1
3 = 0. The same

868 Tomáš Madaras and Martina Tamášová

consideration can be used, due to symmetry, also when ρ is a 7-face. We conclude
then that both γ, ρ are ≥ 9-faces, a contradiction.

Case 2.2.4. Let α be surrounded only with ≥ 6-faces. Note that at least three of them
are exactly 6-faces, hence two of them have to be adjacent, say β = [x1x2y2uwy1] and
η = [x2x3y3vzy2]. If β and η form a nice pair, then the cluster of α, β and η is forbidden;
hence, some of their vertices coincide. Taking into account that all yi, i = 1, . . . , 5 are
distinct, we have v = y1 or w = y3 which yields symmetric cases. Thus, without loss
of generality, let v = y1. If ω is a 6-face or a 7-face, then it forms a forbidden cluster
with α, β or with β; hence, it is an ≥ 9-face. Similarly, γ being a 6-face forms either
a forbidden cluster with α, η), or a 3- or 4-cycle (if y1 is incident with γ); when γ
is a 7-face, it forms either a forbidden cluster with η , or again a 3- or 4-cycle (if it
contains y1). Thus γ is also an ≥ 9-face, a contradiction.

Case 3. Let α be a 7-face. Note that, due to the absence of 3- and 4-cycles in G, α
is a nice face. Suppose that there are two transfers of a charge from α by Rule 3 to
5-faces β, γ through consecutive edges on face boundary of α. Then the only possibility
to avoid 3- or 4-cycles or having ≥ 4-vertices on β or γ is that the faces α, β and γ
form a forbidden cluster. Therefore, we conclude that, from α, at most three transfers
by Rule 3 are possible, and so ̃µ(α) ≥ 7 − 6 − 3 · 1
3 = 0.

Case 4. Let α be a k-face, k ≥ 9. According to the above proposition, at most ⌈ 2
3 k⌉

transfers of a charge by Rule 4 from α are possible, thus ̃µ(α) ≥ k − 6 − 1
2 · ⌈ 2
3 k⌉ ≥ 0.

This proves the unavoidability of S3,4,11; its minimality follows from the construc-
tions (5), (9) and (11) of Section 2.

Theorem 3.4. The sets S3,4,6,8 and S3,4,8,9 are minimal unavoidable in G3.

Proof. Let G ∈ G3 be a graph without 3-cycle or 4-cycle. Using a non-polyhedral
variant of theorem of Wernicke [8] (the details are left to reader), we obtain that G
contains a 5-face adjacent to an ≤ 6-face. Observe that these two faces necessarily
form a nice pair (otherwise a 3- or 4-cycle is found in G); since two adjacent 5-faces
(a 5-face with a 6-face) then form an 8-cycle (a 9-cycle), the unavoidability of the
above mentioned sets follows. The minimality of S3,4,6,8 follows from the constructions
(1), (3), (4) and (10) of Section 2, the minimality of S3,4,8,9 similarly follows from the
constructions (4), (5), (8) and (9).

Theorem 3.5. The set S3,4,7,9 is minimal unavoidable in G3.

Proof. Let G ∈ G3 be a graph of girth 5. By dual variant of result of Borodin [2], G
contains a 3-vertex surrounded by three faces such that the sum of their sizes is at
most 17. Now,

– if one of these faces is a 7-face, then it is necessarily nice, hence it bounds a 7-cycle,
– if one of these faces is a 6-face and another one is a 5-face, then they form a nice
pair and, consequently, a 9-cycle,
– if all three faces are 5-faces, then, due to absence of 3- and 4-cycles in G, any two
of them form a nice pair, thus together, they form a 9-cycle.

Minimal unavoidable sets of cycles in plane graphs 869

This proves the unavoidability of S3,4,7,9; its minimality follows from the constructions
(5), (7), (11) and (3) of Section 2.

Theorem 3.6. The set S3,5,6,7 is minimal unavoidable in G3.

Proof. Let G ∈ G3 be a graph without 3-cycle. By non-polyhedral variant of Kotzig
theorem [6] (in dual form), G contains a 4-face α adjacent to an ≤ 7-face β, or a 5-face
α′ adjacent to an ≤ 6-face β′. Now,

– if β is a 4-face, then it forms a nice pair with α (otherwise a 3-cycle is found),
thereby forming with α a 6-cycle,
– if β is a 6-face or a 7-face, then it is nice (otherwise one ﬁnds a 3-cycle in G), hence
it bounds a 6-or 7-cycle,
– if none of the above possibilities happen, then a 5-face β or α′ forms a 5-cycle in G.

This proves the unavoidability of S3,5,6,7; its minimality follows from the constructions
(3), (5), (11) and (12) of Section 2.

4. CONCLUDING REMARKS

Although the negative results of Section 2 ﬁlter out many sets of cycles, the character-
izations of minimal unavoidable sets is still far from being complete. The ﬁrst open
cases are the sets S3,4,k for 12 ≤ k ≤ 20. The minimal unavoidability of S3,4,14 may
be also indirectly indicated by the fact from [5] that the only cycle whose heaviness
could not be proved (using specialized constructions), for the family of 3-connected
planar graphs without triangular and quadrangular faces, is exactly C14 (we note that
the existence of a planar graph of girth 5 with 2-valent vertices being far apart and no
14-cycle would lead to the constructions of graphs whose 14-cycles necessarily pass
through vertices of high degree). Since proving the lightness of C14 may be diﬃcult,
a little easier task would be to show, at least, the presence of C14 in these plane graphs.
Note also that although a particular cycle is heavy in a graph family, still it can be
unavoidable; for example, C11 and C12 might exist in each plane graph of minimum
degree 5 whereas they are known to be heavy in that graph family.
The constructions of Section 2 to exclude certain sets of cycles from being un-
avoidable are mostly based on graphs which have cut vertices. Under the restriction of
3-connectedness on plane graphs, one has to develop other types of constructions; also,
it may happen that a certain set of cycles which is not unavoidable in planar graphs
of minimum degree 3 is indeed minimal unavoidable in polyhedral graphs. This is the
subject of further research in the paper [7].

Acknowledgements
This work was supported by the Slovak Research and Development Agency under the
Contract No. APVV-15-0116, by the Slovak VEGA Grant 1/0368/16 and by P.J.
Šafárik University grant VVGS-PF-2016-72604, and partially supported by DAAD,
Germany (as part of BMBF) and by the Ministry of Education, Science, Research and
Sport of the Slovak Republic within the project 57320575.

870 Tomáš Madaras and Martina Tamášová

REFERENCES

[1] J. Bensmail, On q-power cycles in cubic graphs, Discuss. Math. Graph Theory 37
(2017), 211–220.

[2] O.V. Borodin, Solution of problems of Kotzig and Grünbaum concerning the isolation
of cycles in planar graphs, Math. Notes 46 (1989), 835–837 (English translation), Mat.
Zametki 46 (1989), 9–12 [in Russian].

[3] G. Exoo, Three graphs and the Erdös–Gyárfás conjecture, arXiv:1403.5636 [math.CO].

[4] C.C. Heckman, R. Krakovski, Erdös–Gyárfás conjecture for cubic planar graphs, Electron.
J. Combin. 20 (2013) P7.

[5] S. Jendrol’, P.J. Owens, On light graphs in 3-connected plane graphs without triangular
or quadrangular faces, Graphs and Combinatorics 17 (2001) 4, 659–680.

[6] A. Kotzig, Contribution to the theory of Eulerian polyhedra, Mat. Čas. SAV (Math.
Slovaca) 5 (1955), 101–113.

[7] T. Madaras, M. Tamášová, Minimal unavoidable sets of cycles in polyhedral graphs,
manuscript.

[8] P. Wernicke, Über den kartographischen Vierfarbensatz, Math. Ann. 58 (1904), 413–426.

[9] D. West, Introduction to Graph Theory, 2nd ed., Prentice Hall, 2001.

Tomáš Madaras
tomas.madaras@upjs.sk

Pavol Jozef Šafárik University
Faculty of Science
Institute of Mathematics
Jesenná 5, 04001 Košice, Slovakia

Martina Tamášová
martina.tamasova@upjs.student.sk

Pavol Jozef Šafárik University
Faculty of Science
Institute of Mathematics
Jesenná 5, 04001 Košice, Slovakia

Received: November 28, 2017.
Revised: June 8, 2018.
Accepted: June 8, 2018.
