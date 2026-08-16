<!-- source: https://arxiv.org/pdf/2605.22867 | converted from PDF -->

A Comprehensive Study of Clique Graphs and Clique Regular

Graphs

An Honors College Project Presented to

the Faculty of the Undergraduate

College of Science and Mathematics

James Madison University

by Connor M. Phillips

December 2025

Accepted by the Faculty of the Department of Mathematics and Statistics, James Madison University, in

partial fulfillment of the requirements for the Honors College.

FACULTY COMMITTEE HONORS COLLEGE APPROVAL

Project Advisor: Joshua Ducey, Ph.D. Bethany Blackstone, Ph.D.

Professor, Pure Math Dean, Honors College

Reader: Rebecca Field, Ph.D.

Associate Professor, Pure Math

Reader: Brant Jones, Ph.D.

Professor, Pure Math

PUBLIC PRESENTATION

Selections of this work were presented at the Shenandoah Undergraduate Mathematics and Statistics

Conference on November 2
nd, 2024 and November 1
st, 2025.arXiv:2605.22867v1  [math.CO]  19 May 2026
Contents

Acknowledgments 3

Abstract 4

1 Introduction 5

1.1 Clique Graphs and Clique Regular Graphs . . . . . . . . . . . . . . . . . . . 7

2 Basic Graph Theory 11

3 Spectral Graph Theory 20

3.1 Spectrum of a Clique Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

4 Strongly Regular Graphs 28

4.1 Strongly Regular Clique Regular Graphs . . . . . . . . . . . . . . . . . . . . 29

4.2 Locally Linear Strongly Regular Graphs . . . . . . . . . . . . . . . . . . . . 35

5 Critical Groups 46

5.1 The Critical Group of a Clique Subdivision Graph . . . . . . . . . . . . . . . 47

6 Examples 58

6.1 Orthogonal Array Block Graphs . . . . . . . . . . . . . . . . . . . . . . . . . 58

6.2 Triangular Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

6.3 Generalized Quadrangle Collinearity Graphs . . . . . . . . . . . . . . . . . . 61

A Finding Feasible Locally Linear Strongly Regular Parameter Sets 64

Bibliography 66

1

List of Figures

1.1 An example of a clique regular graph and its clique graph . . . . . . . . . . . 8

2.1 Graphs used in the proof of Theorem 2.4 . . . . . . . . . . . . . . . . . . . . 13

2.2 An example of a graph satisfying the hypothesis of Theorem 2.8 . . . . . . . 16

2.3 Graphs used to show C3(L(Γ)) ∼= Γ in the proof of Theorem 2.8 . . . . . . . 17

2.4 Graphs used to show (1), (2), and (3) in the proof of Theorem 2.8 . . . . . . 18

2.5 Graphs used to show (4) in the proof of Theorem 2.8 . . . . . . . . . . . . . 19

4.1 The neighborhood of vertex v and the Ti sets . . . . . . . . . . . . . . . . . . 38

5.1 An example of the clique subdivision graph . . . . . . . . . . . . . . . . . . . 48

6.1 An example of an orthogonal array and its block graph . . . . . . . . . . . . 59

6.2 An example of a generalized quadrangle and its collinearity graph . . . . . . 62

2

Acknowledgments

This research was conducted under the supervision of Dr. Ducey, whose guidance and

mentorship over the past two years have been invaluable. Appreciation is also extended to

Dr. Field and Dr. Jones for their careful review and constructive feedback on this project.

Collaboration with Robert Petro during the summer of 2024 contributed to several aspects

of the research, and the results in Chapters 1,2,3,6 and section 4.1 have been published

with Robert Petro in Discrete Mathematics.
 3

Abstract

If Γ is a graph for which every edge is in exactly one clique of order ω, then one can

form a new graph with vertex set equal to these cliques. This is a generalization of the line

graph of Γ. We discover many general results and classifications related to these clique

graphs that will be useful to researchers studying graphs with this property. In particular,

we find bounds on the spectrum of Γ (with exact results when Γ is k-regular) and some

complete classifications when Γ is strongly regular. We apply our results to derive novel

information about the existence questions of certain strongly regular graphs. We also

examine the critical group of graphs with this property and their associated

transformations. Finally, we discuss examples of widely studied families of graphs that

have this property, and provide some examples to make the results more concrete.

4

Chapter 1: Introduction

A famous question in the field of graph theory is: Does there exist a graph on 99

vertices that is 14-regular such that every pair of adjacent vertices is contained in a unique

triangle and every pair of non-adjacent vertices is contained in a unique quadrangle? This

problem has had a $1,000 bounty put on a solution by famous mathematician John

Conway since 2017, which has yet to be claimed. This question is known as the Conway-99

graph problem and while it is widely studied, there is one approach to this problem that

has yet to be explored with much intensity.

If such a graph existed, each edge would be contained in exactly one of its 99·14
6 = 231

triangles, and so one could construct a new graph by taking those triangles as vertices, and

setting two triangles adjacent if and only if they share a vertex. Such a graph would have

properties very closely related to those of the original graph, and so could be used in either

a construction of the graph or a proof of its non-existence.

In general, graphs with the property that each edge is contained in a unique triangle

are called locally linear. In this report, we will introduce a generalization of locally linear

graphs and a graph transformation that seems very natural to do with graphs that have

this property. We will provide many results that relate to these types of graphs and their

associated transformation, including results pertaining to the graphs’ spectrums and

critical groups, and classifications relating to the line graph and strongly regular graphs.

Finally, we will discuss concrete examples of families of graphs that have this property

which are widely studied in the field of graph theory.

But first, we must introduce graph theory and some notation. A graph Γ = (V, E) is

a finite vertex set V , and a finite edge set E containing unordered pairs of vertices. When

we write v ∈ Γ, it is understood that this means v is a vertex of Γ. The graphs we discuss

5

here will have neither loops nor parallel edges. We write an edge between two vertices x

and y as either {x, y} or xy. Two vertices are adjacent if there is an edge between them

and we denote the neighborhood of vertex v as N (v), the set of vertices adjacent to v.

The number of vertices that v is adjacent to is called the degree of the vertex and is

denoted d(v) = |N (v)|. The largest degree of any vertex in Γ is denoted ∆(Γ). If every

vertex in a graph has the same degree k, we say the graph is regular, or more specifically

k-regular. This is the first of many definitions that we will introduce in this report which

include the word regular. We apologize for any confusion this may cause the reader, but all

of these definitions are standard in the literature.

A clique of order ω is a subset of ω vertices such that each vertex is adjacent to every

other vertex. The clique number of a graph, denoted ω(Γ), is the order of the largest

clique in Γ. A clique is maximal if it is not contained in a larger clique, and a clique is

maximum if it is of order ω(Γ).

The complete graph on n vertices, Kn, is the graph with n vertices such that each

vertex is adjacent to every other vertex. A graph is called bipartite if the vertices can be

partitioned into two sets, such that no two vertices in the same set are adjacent. The

complete bipartite graph, Kn,m, is the graph on n + m vertices which are partitioned into

two sets of order n and m such that the graph is bipartite on that partition and any two

vertices in different sets are adjacent.

The line graph of a graph Γ, L(Γ), is the graph with vertices as the edges of Γ, where

two edges are adjacent if and only if they share a vertex in Γ. We will define more terms

and notation as we use them throughout this report. For any other definitions not

specified, please see a standard graph theory reference [11].

6

1.1 Clique Graphs and Clique Regular Graphs

We introduce an ω-clique regular graph as a graph with a nonempty edge set such

that every edge is in a unique clique of order ω. Since a 2-clique is just a single edge every

graph with a nonempty edge set is 2-clique regular. Notice also that since a 3-clique is a

triangle, the locally linear graphs are exactly the 3-clique regular graphs. For this reason

we consider the clique regular property to be a generalization of the locally linear property,

and taking ω = 3 for any of our results reveals a fact about locally linear graphs.

For graphs with the ω-clique regular property, much of the structure of the graph can

be understood by examining its ω-cliques. We develop a very natural graph transformation

that can be be applied to ω-clique regular graphs, which reveals the structure of the

connections between their ω-cliques. This transformation generalizes the way in which the

edges of a graph can be studied using the line graph transformation.

We introduce the ω-clique graph of a graph Γ, which shows the adjacency between

the cliques of order ω in Γ. This graph is denoted Cω(Γ) and is defined in the following

manner:

1. The vertices of the clique graph Cω(Γ) are the cliques of order ω in Γ.

2. Two distinct cliques are adjacent in Cω(Γ) if and only if they have a nonempty

intersection.

While the ω-clique graph construction can be applied to any graph, it is most useful when

the original graph is ω-clique regular. For the most part in this report, we will restrict our

focus only to considering the ω-clique graph of ω-clique regular graphs.

Since a 2-clique is just a single edge, it is clear that for any graph Γ, its line graph is

isomorphic to its 2-clique graph, C2(Γ) ∼= L(Γ). For this reason, we consider the clique

graph construction to be a generalization of the line graph and taking ω = 2 for any of our

7

theorems reveals a fact about the line graph of any nonempty graph. Figure 1.1 shows an

example of a graph that is 3-clique regular and its 3-clique graph.

(a) A 3-clique regular graph Γ
 (b) The graph C3(Γ)

Figure 1.1: An example of a clique regular graph and its clique graph

Our first proposition will enumerate for some graph Γ, what values of ω it could

possibly be ω-clique regular for. This will also justify our choice of the notation ω.

Proposition 1.1. If Γ is an ω-clique regular graph, then ω = 2 or ω = ω(Γ).

Proof. Assume Γ is ω-clique regular and ω ̸= 2. If 2 < ω < ω(Γ), then there exists a clique

in Γ of order ω + 1 contained within a clique of order ω(Γ). Within this (ω + 1)-clique,

removing any vertex generates an ω-clique. So every edge is in at least the ω − 1 cliques of

order ω, that are generated by removing each vertex but the edge’s endpoints. Since

ω − 1 > 1, these edges are not in unique ω-cliques. If ω(Γ) < ω, then there are no ω-cliques

in Γ, and so no edge is contained in an ω-clique. So ω must equal ω(Γ).

To avoid distracting notation throughout this report, we will refer to ω-clique

regularity and ω-clique graphs generally without the quantifier ω when it is clear through

context the value in question, or when the specific value is not relevant to topic of

discussion.
 8

Notice that the definition of clique regularity is similar to that of a regular clique

assembly, as introduced in [10]. They define a regular clique assembly as a regular graph

with clique number at least 2, where every maximal clique is maximum and each edge

belongs to exactly one maximum clique. These constructions form a subset of

clique-regular graphs, and most of the results in this report only require a graph to be

clique-regular rather than a full regular clique assembly. However, in certain specific cases,

we will refer to results from [10] to build upon their findings and establish stronger

conclusions about regular clique assemblies.

Regular clique assemblies are related to edge regular graphs, denoted erg(n, k, λ),

which are defined as k-regular graphs on n vertices with the property that every pair of

adjacent vertices has λ common neighbors. Clearly every regular clique assembly Γ is

ω(Γ)-clique regular and the following theorem will classify when clique regular graphs are

regular clique assemblies.

Theorem 1.2. Suppose Γ is an ω-clique regular graph on n vertices. Then Γ is a regular

clique assembly if and only if Γ is an erg(n, ∆(Γ), ω − 2).

Proof. The proof that any regular clique assembly is an erg(n, ∆(Γ), ω − 2) comes from [10,

p. 304]. So now assume that Γ is ω-clique regular and an erg(n, k, ω − 2) and we will show

that Γ is a regular clique assembly. If ω = 2 or ω = 3 this proof also comes from [10, p. 304]

so assume that ω is the clique number of Γ and is greater than 3. Since Γ is regular from

the hypothesis, it is sufficient to show that every maximal clique in Γ has order ω. Suppose

for contradiction there exists a maximal clique of order less than ω, call it c<, and let x and

y be vertices in that clique. Then the edge xy is in a unique clique of order ω, call it cω, so

x and y have ω − 2 neighbors in that clique. Because c< is maximal, it is not contained in

cω and there exists a vertex z in c< and not in cω. So z is also a common neighbor of x and

y which implies the order of N (x) ∩ N (y) is greater than ω − 2, a contradiction.

9

We denote by rca(n, k, ω), a regular clique assembly on n vertices that is k-regular

with clique number ω. An important result that we will use in section 4.2, comes from the

original paper on regular clique assemblies [10], so we will record it here at the end of the

introduction.

Theorem 1.3. If Γ is an rca(n, k, ω), then Cω(Γ) is an rca
( nk
ω(ω−1), ω ( k
ω−1 − 1) , k
ω−1) and

C k
ω−1 (Cω(Γ)) ∼= Γ.

The proof of this theorem comes from [10, Theorem 1]. Lastly, we introduce another

lemma on regular clique assemblies that will be useful in section 4.2.

Lemma 1.4. Suppose Γ is an rca(n, k, ω) and let u and v be distinct and non-adjacent

vertices in Γ. Then |N (u) ∩ N (v)| ≤ k
ω−1.

Proof. If ω = 2, then the lemma is clear so assume ω ≥ 3. From [10, Proposition 1], the

neighborhood of each vertex in Γ is a disjoint union of Kω−1’s with k
ω−1 components.

Suppose x and y are distinct vertices in N (v) ∩ N (u). If x and y are in the same Kω−1

component of N (v), then since Γ is a regular clique assembly, the clique {x, y, u} is

contained in an ω-clique containing u and the clique {x, y, v} is contained in a different

ω-clique containing v. But this is a contradiction since the edge {x, y} is in two different

ω-cliques. So x and y must be in distinct Kω−1 components in N (v) showing there exists

an injective mapping from N (v) ∩ N (u) to the disjoint Kω−1 components in N (v). This

implies the result.
 10

Chapter 2: Basic Graph Theory

In this section, we investigate which graphs have a clique regular line graph, and for

which the clique graph acts as the “inverse” of the line graph construction; which graphs Γ

satisfy Cω(L(Γ)) ∼= Γ. The following lemmas and theorems will classify for ω ≥ 3, all graphs

which have the first property and all connected graphs that have the second property.

Lemma 2.1. For each vertex v in Γ, the set of edges incident to v form a clique in L(Γ)

with order d(v). If d(v) > 2, then this clique is maximal.

Proof. Vertex v is incident to d(v) edges in Γ all of which share one endpoint v. So in L(Γ)

those edges incident to v form a clique of order d(v). Now assume this clique is not

maximal and we will show d(v) ≤ 2. The clique of the edges of v must then be contained in

a larger clique in L(Γ), and so there must exist an edge e in Γ that is not incident to v but

is adjacent to all other edges incident to v. If v had degree 3 or larger, by the pigeon hole

principle one of the 2 endpoints of e would have to be the endpoint for at least 2 edges

incident to v. But we do not allow parallel edges, so v can have degree at most 2.

Following from Lemma 2.1, for any vertex v ∈ Γ when we refer to the “clique created

by v” we mean the clique in L(Γ) of order d(v) induced by the edges in Γ incident to v.

Lemma 2.2. For ω > 3, L(Γ) ∼= Kω if and only if Γ ∼= K1,ω. Also, L(Γ) ∼= K3 if and only

if Γ ∼= K3 or Γ ∼= K1,3.

Proof. The graph K1,ω has ω edges that all share a common end point, so L(K1,ω) ∼= Kω

for ω ≥ 3. Also, it is clear that L(K3) ∼= K3. The converse for both cases follows from the

Whitney Isomorphism Theorem [15], which states that two graphs are isomorphic if and

only if their line graphs are isomorphic, with the single exception of graphs K3 and

K1,3.
 11

Remark 2.3. Lemma 2.2 implies that the only structures that can create a maximal

clique in L(Γ) are the set of edges incident to a vertex v, i.e. cliques created by a vertex v

following from Lemma 2.1. There is one exception in the case of a 3-clique in L(Γ), which

can also be created by a triangle, K3.

We will begin by classifying graphs that have ω-clique regular line graphs and start

with the case ω ≥ 4.

Theorem 2.4. Suppose ω ≥ 4 and Γ is a graph. Then L(Γ) is ω-clique regular if and only

if the degree of every vertex in Γ is 1 or ω.

Proof. First assume that the degree of every vertex in Γ is 1 or ω. Let e = {xv, yv} be an

edge in L(Γ). Then the vertex v in Γ has degree ω and so by Lemma 2.1 e is in the

maximal ω-clique created by v, and by Remark 2.3, this is the unique ω-clique e is in.

For the converse, assume there exists a vertex v in Γ with degree not equal to either 1

or ω. If 1 < d(v) < ω, then there exists edges e1 and e2 incident to v in Γ. So the edge e1e2

in L(Γ) is in the maximal clique created by v of order less than ω and e1 and e2 share no

other endpoints in Γ so by Remark 2.3, the edge e1e2 is in no clique of order ω. If d(v) > ω,

then there exists a clique of order greater than ω in L(Γ). So in either case L(Γ) is not

ω-clique regular.

The case of the 3-clique regular line graph is more complicated because

L(K3) ∼= K3 ∼= L(K1,3). For this reason, the concept of a triangle-free graph will be useful

in our classification. This is defined as a graph that has no triangles as a subgraph, or

equivalently as a graph Γ with ω(Γ) = 2.

Theorem 2.5. Suppose Γ is a graph with connected components C1, C2, . . . , Cn. Then

L(Γ) is 3-clique regular if and only if whenever Ci ̸∼= K3 , Ci is triangle-free and the degree

of every vertex in Ci is 1 or 3.

Proof. First, assume that for each Ci ̸∼= K3, Ci is triangle-free and the degree of every

vertex in Ci is 1 or 3. Let e = {xv, yv} be an edge in L(Γ) with vertex v in connected

12

component Ci. If Ci ∼= K3, then edge e is in L(Ci) ∼= K3 a connected component of L(Γ) so

we are done. So assume Ci ̸∼= K3 implying by our assumption that the degree of v is 3. So

the 3-clique created by v is maximal by Lemma 2.1 and since Ci is triangle-free by our

assumption, Remark 2.3 implies that this is the only 3-clique containing edge e.

Now assume the converse, that for some Ci ̸∼= K3, Ci contains a triangle or Ci contains

a vertex with degree not equal to either 1 or 3. For the first case, since Ci is connected,

contains a triangle and is not K3, Figure 2.1a is a subgraph of Γ and therefore Figure 2.1b

is a subgraph of L(Γ). So L(Γ) is not 3-clique regular.

(a) Subgraph of Γ (b) Subgraph of L(Γ)

Figure 2.1

Now for the second case, let v be a vertex in Ci with degree not equal to either 1 or 3.

If d(v) > 3, then there exists a clique of order greater than 3 in L(Γ) so L(Γ) is not 3-clique

regular. If d(v) = 2, then let vertices x and y be adjacent to v. If x and y are adjacent,

then {v, x, y} is a triangle in Γ, a contradiction. The edge e = {xv, yv} in L(Γ) is then not

in a 3-clique induced by the edges incident to v and not in a 3-clique induced by a triangle

in Γ. So by Remark 2.3, edge e is not in any 3-clique thus L(Γ) is not 3-clique regular.

Now we restrict our focus to connected graphs and will classify all that are isomorphic

to the ω-clique graph of their line graph. Again, we start with the case ω ≥ 4 and we will

find the following lemma useful.
 13

Lemma 2.6. If ω ≥ 3 and Γ is a connected graph with Cω(L(Γ)) ∼= Γ, then ∆(Γ) ≤ ω.

Proof. First, assume for contradiction ∆(Γ) ≥ ω + 2 and let v be a vertex in Γ with degree

∆ = ∆(Γ). Observe that the number of ω-cliques in the ∆-clique created by v in L(Γ) is
(
∆
ω). Let ck be one of these ω-cliques and we will show that the degree of ck in Cω(L(Γ)) is

at least (
∆
ω) − (
∆−ω
ω ) − 1. In the ∆-clique created by v, ck is only non-adjacent with another

clique if they don’t share any vertices. There are ∆ − ω vertices in the ∆-clique created by

v that are not in ck so there are (∆−ω
ω ) other ω-cliques not adjacent to ck. This implies that

ck is adjacent to (
∆
ω) − (
∆−ω
ω ) − 1 other ω-cliques in the ∆-clique created by v. So

d(ck) ≥ (∆
ω) − (
∆−ω
ω ) − 1. By induction on ∆ ≥ ω + 2, we will show that
(
∆
ω) − (
∆−ω
ω ) − 1 > ∆ which implies d(ck) > ∆(Γ) contradicting Cω(L(Γ)) ∼= Γ. For the base

case let ∆ = ω + 2. Since ω ≥ 3 then (
∆−ω
ω ) = (2
ω) = 0. So

ω + 1
2 ≥ 2

(ω + 2)(ω + 1)
2 − 1 ≥ 2ω + 3 > ω + 2
(ω + 2
ω
 ) − (2
ω
) − 1 > ω + 2.

For the inductive step, assume (∆
ω) − (∆−ω
ω ) − 1 > ∆ for some ∆ ≥ ω + 2 and we will show
(
∆+1
ω ) − (∆+1−ω
ω ) − 1 > ∆ + 1. Recall that for any positive integers a and b,
(
a+1
b ) = (
a
b) + ( a
b−1)
. Then since ( ∆
ω−1
) > (∆−ω
ω−1 ) implies ( ∆
ω−1
) − (∆−ω
ω−1 ) > 0 we get,

(
∆ + 1
ω
 ) − (∆ + 1 − ω
ω
 ) − 1 > (∆
ω
 ) − (
∆ − ω
ω
 ) − 1 ≥ ∆ + 1.

Now for contradiction, assume ∆(Γ) = ω + 1 and let v be a vertex in Γ with degree

ω + 1. Then v creates an (ω + 1)-clique in L(Γ) and observe that every ω-clique in the

(ω + 1)-clique created by v is adjacent to every other ω-clique. So there is an (ω + 1)-clique

in Cω(L(Γ)) since the number of ω-cliques in an (ω + 1)-clique is ω + 1. Because of the

assumed isomorphism, there must be an (ω + 1)-clique in Γ. Then since ∆(Γ) = ω + 1 and

14

Γ is connected, at least one of the vertices in this (ω + 1)-clique has degree ω + 1, call this

vertex u. Consider the set of edges in the (ω + 1)-clique incident with u. This set induces

an ω-clique in L(Γ) we will call ck which we will show has degree in Cω(L(Γ)) greater than

ω + 1. Since the other endpoint of every edge in ck has degree at least ω, they all create at

least one ω-clique in L(Γ) which is adjacent to ck. Since u has degree ω + 1 in Γ, it creates

ω other ω-cliques in L(Γ) also adjacent to ck. So d(ck) ≥ 2ω > ω + 1 = ∆(Γ) since ω ≥ 3,

contradicting the isomorphism.

Theorem 2.7. Suppose ω ≥ 4 and Γ is a connected graph. Then Cω(L(Γ)) ∼= Γ if and only

if Γ is ω-regular.

Proof. First assume Γ is ω-regular. From Lemma 2.1 there is an injective mapping from

the vertices in Γ to the ω-cliques their edges induce in L(Γ). From Remark 2.3 we know

that the cliques created by each vertex in Γ are the only ω-cliques in L(Γ). So the injective

mapping is a bijection from the vertices in Γ to the vertices in Cω(L(Γ)). We will show this

bijection preserves adjacency. If vertices v and u are adjacent in Γ, then the cliques created

by v and by u share the vertex vu in L(Γ). So in Cω(L(Γ)) these two cliques are adjacent.

If v and u are not adjacent, then their cliques in L(Γ) don’t share a vertex so they are not

adjacent in Cω(L(Γ)). Thus it follows Cω(L(Γ)) ∼= Γ.

Now assume that Γ ∼= Cω(L(Γ)) which implies by Lemma 2.6 that ∆(Γ) ≤ ω. Let di

denote the number of vertices in Γ with degree i for 1 ≤ i ≤ ω. By Remark 2.3 and since

∆(Γ) ≤ ω, we know the number of vertices in Cω(L(Γ)) equals dω. We also know the

number of vertices in Γ is ∑ω
i=1 di. Because these graphs are isomorphic, we have

dω = ∑ω
i=1 di implying di = 0 for all i ̸= ω. Thus Γ is ω-regular.

Once again, the case of the 3-clique graph of a line graph is much more complicated

even when restricting to connected graphs.
 15

Theorem 2.8. Suppose Γ is a connected graph. Then C3(L(Γ)) ∼= Γ if and only if:

(1) the degree of every vertex in Γ is 2 or 3,

(2) every degree 2 vertex in Γ is contained in a triangle,

(3) every triangle in Γ contains exactly one degree 2 vertex, and

(4) distinct triangles in Γ share no vertices.

The simplest example of a graph with this property is shown in Figure 2.2a and its

line graph is shown in Figure 2.2b. Observe the bijective adjacency preserving mapping

between the vertices of Figure 2.2a and the triangles of Figure 2.2b.

(a) A graph satisfying (1), (2), (3), and (4) (b) The line graph of (a)

Figure 2.2

Proof. Begin by assuming (1), (2), (3), and (4). From these, observe that each triangle and

each degree two vertex in Γ must exist in a subgraph isomorphic to Figure 2.3a, which has

line graph isomorphic to Figure 2.3b. We define the mapping from the vertices of Γ to the

vertices of C3(L(Γ)) by sending a degree 3 vertex to the triangle it induces in L(Γ) by

Lemma 2.1, and sending a degree 2 vertex to the triangle labeled A in Figure 2.3b; the

triangle in L(Γ) induced by the unique triangle in Γ containing the degree 2 vertex as

implied by (2). Since by Remark 2.3, the only triangles in L(Γ) are those created by a

degree 3 vertex or those induced by a triangle in Γ with unique degree 2 vertex, this

mapping is bijective. We will now show it preserves adjacency. Let u and v be vertices in

16

(a) Subgraph of Γ (b) Subgraph of L(Γ)

Figure 2.3

Γ. If u and v both have degree 3, the vertices they map to in C3(L(Γ)) are adjacent if and

only if u and v are adjacent by the same argument as in Theorem 2.7. If both vertices have

degree 2, then they cannot be adjacent since by (2), this would imply they are in the same

triangle, contradicting (3). And the vertices they map to in C3(L(Γ)) are not adjacent

since this would imply that two edges in the distinct triangles containing u and v share a

vertex, contradicting (4). So now assume WLOG that d(u) = 2 and d(v) = 3. If u and v

are adjacent in Γ, then Figure 2.3a is a subgraph of Γ with u as the vertex 1 and v as the

vertex 0. So v is in the triangle in Γ containing u and the triangles they induce in L(Γ)

share the vertex uv. If the vertices that u and v map to in C3(L(Γ)) are adjacent, then the

triangles induced by the triangle containing u and the edges incident to v share some

vertex in L(Γ). This means the triangle containing u in Γ has some edge incident to v,

implying u and v are adjacent. Thus C3(L(Γ)) ∼= Γ.

For the converse, assume that C3(L(Γ)) ∼= Γ which means by Lemma 2.6 that

∆(Γ) ≤ 3. So for 1 ≤ i ≤ 3, let di denote the number of vertices of degree i, and for

0 ≤ j ≤ 3 let tj denote the number of triangles with j vertices of degree 2. From Remark

2.3, the number of vertices in C3(L(Γ)) is given by d3 + ∑3
j=0 tj. First we will show

17

t0 = t3 = 0. Since Γ is connected, if there exists a triangle with 3 vertices of degree 2 then

Γ ∼= K3 but C3(L(K3)) ∼= K1, a contradiction. If there exists a triangle with no vertices of

degree 2, then Figure 2.4a is a subgraph of Γ where vertices 3, 4 and 5 may or may not be

distinct. So Figure 2.4b is a subgraph of L(Γ).

(a) Subgraph of Γ (b) Subgraph of L(Γ)

Figure 2.4

Figure 2.4b consists of four triangles with each pair sharing at least one vertex, so K4

is a subgraph of C3(L(Γ)) ∼= Γ. Since Γ is connected and ∆(Γ) ≤ 3, we must have Γ ∼= K4.

But it can be verified that C3(L(K4)) ̸∼= K4, a contradiction.

So we have t0 = t3 = 0 implying the number of vertices in C3(L(Γ)) is d3 + t1 + t2 and

since the number of vertices in Γ is given by d1 + d2 + d3, their isomorphism implies

t1 + t2 = d1 + d2. A counting argument shows that d2 ≥ t1 + 2t2 implying

t1 + t2 = d1 + d2

t1 + t2 ≥ d1 + t1 + 2t2

−t2 ≥ d1.

Thus t2 = d1 = 0, since 0 ≥ −t2 ≥ d1 ≥ 0. This implies (1) and (3) and since d2 = t1, we

have (2) as well. To show (4), observe from (1), (2), and (3) that if two distinct triangles

18

share vertices in Γ, Figure 2.5a must be a subgraph of Γ and so Figure 2.5b is a subgraph

of L(Γ).
 (a) Subgraph of Γ (b) Subgraph of L(Γ)

Figure 2.5

Figure 2.5b consists of four triangles all sharing vertex 4, so K4 is a subgraph of

C3(L(Γ)). But as shown above, this leads to a contradiction so we get (4).

19

Chapter 3: Spectral Graph Theory

Given a fixed ordering of vertices V = {v1, v2, . . . , vn} the adjacency matrix of Γ is

defined as the n × n matrix A with rows and columns indexed by the vertices of Γ, with

(A)ij =
 



1 if vi is adjacent to vj

0 otherwise

where (A)ij is the i, jth entry of A. We denote by In the n × n identity matrix. We denote

the characteristic polynomial of any n × n matrix A as p(A; λ) = det(λIn − A) and for a

graph Γ, p(Γ; λ) denotes the characteristic polynomial of the adjacency matrix of Γ.

The spectrum of a graph Γ is the set of eigenvalues of the adjacency matrix of Γ

along with their multiplicities. It is denoted λ
a0
0 , . . . , λar
r where the exponent represents the

multiplicity of that eigenvalue. The spectrum of a graph contains information on a number

of different structural properties of the graph, which is why it is a widely studied graph

invariant, and why we study the spectrum of clique graphs.

One such property of the spectrum is that the largest eigenvalue of a graph is always

less than or equal to the maximum degree of a vertex, with equality if and only if the graph

is regular [6, Proposition 3.1.2]. This means a k-regular graph has k as its largest

eigenvalue, and these facts will be useful later in this chapter and the next.

3.1 Spectrum of a Clique Graph

In this section, we will provide results on the spectrum of clique regular graphs and

their clique graphs. We will provide bounds on their eigenvalues and in the case that Γ is

k-regular, an exact specification on the spectrum of Cω(Γ).

20

Let m be the number of ω-cliques in an ω-clique regular graph Γ so that m
(
ω
2) is the

number of edges in Γ. Let AC be the adjacency matrix of Cω(Γ) with vertices indexed

(c1, . . . , cm) and AL be the adjacency matrix of L(Γ) with vertices indexed (e1, . . . , em(
ω
2))

such that edges {e(i−1)(
ω
2)+1, . . . , ei(ω
2)} constitute clique ci for all 1 ≤ i ≤ m, i.e. clique c1

contains edges e1 through e(
ω
2), clique c2 contains edges e(
ω
2)+1 through e2(
ω
2) and so on.

Now define ˜A = 6
(ω
3)Im + (ω − 1)2AC and define φ : Rm → R
m(
ω
2) by

φ
 



















 a1

a2
...

am





















 =
 









⃗a1

⃗a2
...

⃗am










 where ⃗a :=
 







a
...

a






 ∈ R(ω
2).

So the φ function expands a column vector by a factor of (
ω
2). For example, if m = 2 and

ω = 3 then φ
 







1

2









 = [
1 1 1 2 2 2

]⊤.

Lemma 3.1. If Γ is ω-clique regular with ˜A, φ, and AL as above, then for all v ∈ Rm,

v⊤ ˜Av = φ(v)⊤ALφ(v).

Proof. Let ti be the standard basis vector of R
m with a 1 in the i
th position for 1 ≤ i ≤ m.

It is sufficient to show that for all ti and tj

t
⊤
i ˜Atj = φ(ti)⊤ALφ(tj).

Let Sij denote the sub-matrix of AL with rows corresponding to edges in ci and columns

corresponding to edges in cj. Observe that φ(ti)
⊤ALφ(tj) equals the sum of the entries of

Sij. Similar to above, it is clear that t⊤
i ˜Atj is the 1 × 1 matrix with entry ( ˜A)ij.

21

Now for the first case i = j. Let ek be an edge in Γ with endpoints x and y in ci. So ek

corresponds to a row in Sii. The vertex x is incident to ω − 1 edges in ci one of which is ek

and the same for vertex y. So ek is incident to 2(ω − 2) edges in ci implying the sum of the

ek row in Sii is 2(ω − 2). Since there are (ω
2) rows in Sii, the total sum of entries in Sii is

2(ω − 2)(
ω
2) = 6
(ω
3). So t⊤
i ˜Ati = [6
(
ω
3)] = φ(ti)
⊤ALφ(ti).

Next for the case when ci is adjacent to cj. Let x be the unique vertex in Γ that ci and

cj share and let ek be an edge incident to x with other endpoint in ci. Then ek is incident

to the ω − 1 edges of x with other endpoints in cj implying the sum of the ek row in Sij is

ω − 1. Since there are ω − 1 edges incident to x with other endpoint in ci, and since every

edge in ci that isn’t incident to x is not incident to any edges in cj, the total sum of the

entries in Sij is (ω − 1)
2. So t⊤
i ˜Atj = [(ω − 1)
2] = φ(ti)
⊤ALφ(tj).

Finally for the last case when i ̸= j and ci is not adjacent to cj. Let ek be an edge in

ci. Then since ci and cj don’t share common vertices, ek is not incident to any edges in cj

implying that the total sum of the entries in Sij is 0.

So t⊤
i ˜Atj = [0] = φ(ti)
⊤ALφ(tj).

Theorem 3.2. Suppose Γ is ω-clique regular and the eigenvalues of L(Γ) are

µ1 ≤ · · · ≤ µm(
ω
2). Then for each eigenvalue λ of Cω(Γ),

ω
ω − 1
 ( µ1
2 − ω + 2
) ≤ λ ≤ ω
ω − 1
 ( µm(ω
2)
2 − ω + 2
) .

Proof. For this proof ∥t∥ will denote the euclidean norm of vector t. Let λ be an eigenvalue

of AC with eigenvector u. Clearly, AC and ˜A = 6
(
ω
3)
Im + (ω − 1)2AC share the same

eigenvectors and η = 6(
ω
3) + (ω − 1)2λ is an eigenvalue of ˜A with the eigenvector u. Now

define v = u

∥u∥
√
(
ω
2) so that ∥v∥
2 = 1
(
ω
2) and v is an eigenvector of ˜A with eigenvalue η.

Notice that
 φ(v)
⊤φ(v) = [
|φ(v)|
2] = [(
ω
2
)
∥v∥
2] = [1] = I1.

22

By the Eigenvalue Interlacing Theorem, [6, pg. 26] this implies that the eigenvalue of the

1 × 1 matrix φ(v)
⊤ALφ(v) interlaces the eigenvalues of AL. By Lemma 3.1,

φ(v)
⊤ALφ(v) = v⊤ ˜Av = ηv⊤v = [
η∥v∥
2] =
 [ η
(ω
2)
 ]
 .

So the eigenvalue η
(
ω
2) interlaces the eigenvalues of AL, µ1 ≤ η
(
ω
2) ≤ µm(
ω
2).

Since η = 6
(ω
3) + (ω − 1)2λ, it follows that

1
(ω − 1)2
 ((ω
2
)µ1 − 6(
ω
3
)) ≤ λ ≤ 1
(ω − 1)2
 ((ω
2
)µm(
ω
2) − 6(
ω
3
)) .

Equivalently, ω
ω − 1
 ( µ1
2 − ω + 2
) ≤ λ ≤ ω
ω − 1
 ( µm(ω
2)
2 − ω + 2
) .

From this theorem, we can also derive bounds on the eigenvalues that don’t require

any knowledge of the line graph.

Corollary 3.3. If Γ is ω-clique regular then for each eigenvalue λ of Cω(Γ),

−ω ≤ λ ≤ ω ( ∆(Γ)
ω − 1 − 1)

where ∆(Γ) denotes the largest degree of Γ.

Proof. Let µ1 ≤ · · · ≤ µm(
ω
2) be the eigenvalues of L(Γ). Two classical results in spectral

graph theory are that for any line graph, −2 ≤ µ1 and µm(
ω
2) ≤ ∆(L(Γ)) ≤ 2(∆(Γ) − 1).

From these we get
 −ω ≤ ω
ω − 1
 ( µ1
2 − ω + 2)

and ω
ω − 1
 ( µm(
ω
2)
2 − ω + 2) ≤ ω ( ∆(Γ)
ω − 1 − 1) .

23

So the result follows from Theorem 3.2.

If Γ is an ω-clique regular graph and also k-regular, then we can show that the

characteristic polynomial of Cω(Γ) is a function of the characteristic polynomial of Γ.

Recall that p(Γ; λ) denotes the characteristic polynomial of Γ’s adjacency matrix and that

the roots of this polynomial are the eigenvalues of Γ. Let n be the number of vertices in Γ

and m = nk
ω(ω−1) be the number of ω-cliques in Γ, i.e. the number of vertices in Cω(Γ).

Let A be the adjacency matrix of Γ with vertices indexed (v1, . . . , vn), and let AC be

the adjacency matrix of Cω(Γ) with ω-cliques indexed (c1, . . . , cm). We will define the

ω-clique incidence matrix of Γ as an n × m matrix R such that the rows are indexed by

the vertices in Γ in the same order as in A, and the columns are indexed by the ω-cliques

in Γ in the same order as in AC. The entries of R are defined,

(R)ij =
 



1 if vi ∈ cj

0 otherwise.

Recall also that the degree matrix of Γ is defined as D = diag(d(v1), . . . , d(vn)).

Lemma 3.4. Suppose that Γ is ω-clique regular with ω-clique incidence matrix R and

degree matrix D. Then:

(1) R⊤R = AC + ωIm and

(2) RR⊤ = A + 1
ω−1D.

Proof. (1) We have
 (R⊤R)ij =
 n∑

l=1 (R)li(R)lj,

from which it is clear that (R⊤R)ij is the number of vertices that are in both clique ci and

cj. If i = j, then the sum will equal ω, which is the number of vertices in ci. So

(R⊤R)ii = ω = (AC + ωIm)ii. If ci and cj are adjacent, then they share one vertex in

common. So (R⊤R)ij = 1 = (AC + ωIm)ij. Otherwise (R⊤R)ij = 0 = (AC + ωIm)ij.

24

(2) Similarly, we have that (RR⊤)ij is the number of cliques that vi and vj commonly

belong to. If i = j, then the sum will equal the number of cliques that contain vi. Since vi

has degree d(vi), and each clique with vi contains ω − 1 edges adjacent to vi unique to that

clique, d(vi)
ω−1 is the number of cliques that vi belongs to. So (RR⊤)ij = d(vi)
ω−1 = (A + 1
ω−1D)ij.

If vi and vj are adjacent, then the edge between them belongs to a unique clique so

(RR⊤)ij = 1 = (A + 1
ω−1D)ij. Otherwise (RR⊤)ij = 0 = (A + 1
ω−1D)ij.

Theorem 3.5. If Γ is k-regular and ω-clique regular, then

p(Cω(Γ); λ) = (λ + ω)m−np (
Γ; λ + ω − k
ω − 1
 )

where m = nk
ω(ω−1).

Proof. Define two square block matrices with n + m rows and columns as follows with R

the ω-clique incidence matrix of Γ,

U =
 



(λ + ω)In −R

0 Im
 


 , V =
 


 In R

R⊤ (λ + ω)Im



 .

Then,

U V =
 



(λ + ω)In − RR⊤ 0

R⊤ (λ + ω)Im



 , V U =
 


 (λ + ω)In 0

(λ + ω)R⊤ (λ + ω)Im − R⊤R



 .

Since det(U V ) = det(V U ), it follows that

(λ + ω)mdet((λ + ω)In − RR⊤) = (λ + ω)
ndet((λ + ω)Im − R⊤R)

(λ + ω)m−ndet((λ + ω)In − RR⊤) = det((λ + ω)Im − R⊤R).

25

Using the above equality and Lemma 3.4 we get,

p(Cω(Γ); λ) = det(λIm − AC)

= det((λ + ω)Im − R⊤R)

= (λ + ω)
m−ndet((λ + ω)In − RR⊤)

= (λ + ω)
m−ndet ((
λ + ω − k
ω − 1
 ) In − A)

= (λ + ω)
m−np (Γ; λ + ω − k
ω − 1
 ) .

Note that for the previous lemma and theorem, taking ω = 2 gives the proof from

Biggs [4, p.18-19] for the characteristic polynomial of the line graph of a regular graph.

Here we generalized this proof for the ω-clique graph of any graph that is regular and

ω-clique regular for any ω ≥ 2.

Remark 3.6. Recall that the eigenvalues of a matrix are exactly the roots of the matrix’s

characteristic polynomial. So Theorem 3.5 implies that if the spectrum of a k-regular and

ω-clique regular graph is
 ka0, λ
a1
1 , . . . , λar
r ,

then the spectrum of its ω-clique graph is

( k
ω − 1 + k − ω)a0 , ( k
ω − 1 + λ1 − ω)a1 , . . . , ( k
ω − 1 + λr − ω)ar , −ωm−n

where n is the number of vertices and m = nk
ω(ω−1) is the number of ω-cliques.

26

Corollary 3.7. Suppose Γ is k-regular and ω-clique regular where the smallest eigenvalue

λ1 has multiplicity a1. Then λ1 ≥ −k
ω−1 and if k < ω(ω − 1) as well, then λ1 = −k
ω−1 and

a1 ≥ n − nk
ω(ω−1).

Proof. From Remark 3.6, k
ω−1 + λ1 − ω is an eigenvalue of Cω(Γ) so from Corollary 3.3

−ω ≤ k
ω−1 + λ1 − ω implies λ1 ≥ −k
ω−1. If k < ω(ω − 1) then m − n = nk
ω(ω−1) − n < 0. Since

this is the exponent of the (λ + ω) term in the characteristic polynomial of Cω(Γ) by

Theorem 3.5, there must be the same term in p(Γ; λ + ω − k
ω−1) with exponent greater than

or equal to n − nk
ω(ω−1). By above, this term must come from the smallest eigenvalue so we

get λ1 = −k
ω−1 with multiplicity a1 ≥ n − nk
ω(ω−1).

27

Chapter 4: Strongly Regular Graphs

A graph Γ is called strongly regular with parameters (n, k, λ, µ) and is abbreviated

as srg(n, k, λ, µ) if

• Γ has n vertices,

• Γ is k-regular,

• Adjacent vertices share exactly λ common neighbors, and

• Distinct non-adjacent vertices share exactly µ common neighbors.

Clearly, strongly regular graphs are a subset of edge regular graphs as defined in the

introduction, but with an additional requirement on non-adjacent vertices. The parameters

(n, k, λ, µ) are closely related and must obey,

(n − k − 1)µ = k(k − λ − 1), (4.1)

[6, Theorem 9.1.3].

A graph Γ is strongly regular if and only if it is regular with 3 or fewer distinct

eigenvalues [6, Theorem 9.1.2]. So we can classify strongly regular graphs as either

“boring” (graphs with one or two eigenvalues), disjoint unions of complete graphs and their

complements, or “non-boring” if otherwise. Researchers focus mainly on non-boring

strongly regular graphs, which we will do as well, and a lot of research is devoted to

studying their spectral properties. The spectrum of a strongly regular graph is derivable

from its parameters, which we record in the following theorem.

28

Theorem 4.1. [6, Theorem 9.1.2] If Γ is a non-boring srg(n, k, λ, µ), then it will have

spectrum k1, rf , s
g where k > r > s and the latter two eigenvalues and their multiplicities

are given by the following,

r = 1
2
 [
(λ − µ) + √
(λ − µ)2 + 4(k − µ)] ,

f = 1
2
 [
(n − 1) − 2k + (n − 1)(λ − µ)
√(λ − µ)2 + 4(k − µ)
 ]
 ,

s = 1
2
 [
(λ − µ) − √
(λ − µ)2 + 4(k − µ)] ,

g = 1
2
 [
(n − 1) + 2k + (n − 1)(λ − µ)
√(λ − µ)2 + 4(k − µ)
 ]
 .
 (4.2)

From these it is also provable that λ − µ = r + s and k − µ = −rs.

One of the biggest questions on the topic of strongly regular graphs is: for which sets

of parameters (n, k, λ, µ) does a strongly regular graph exist? Recall from the introduction

the statement of Conway’s 99-graph problem: does there exist a graph on 99 vertices that

is 14-regular such that every pair of adjacent vertices is contained in a unique triangle and

every pair of non-adjacent vertices is contained in a unique quadrangle? We see now that

this is equivalent to asking if there exists an srg(99, 14, 1, 2).

We call a parameter set (n, k, λ, µ) feasible if it satisfies equation (4.1) and its implied

spectrum given by (4.2) are integers with positive integer multiplicities. A large list of

feasible parameter sets can be found on Andries Brouwer’s website [5]. Brouwer’s list

categorizes each set of srg parameters into three groups (existence, non-existence, and

unknown). Boring graphs are excluded from this list.

4.1 Strongly Regular Clique Regular Graphs

There is much overlap between clique regular graphs and strongly regular graphs. If

an srg(n, k, λ, µ) Γ is ω-clique regular, since we know its spectrum is given by k1, rf , s
g

29

from Theorem 4.1, Remark 3.6 implies that the spectrum of Cω(Γ) is given by

( k
ω − 1 + k − ω)1 , ( k
ω − 1 + r − ω)f , ( k
ω − 1 + s − ω)g , −ωm−n (4.3)

where m = nk
ω(ω−1). The following theorem will determine when the ω-clique graph of an

ω-clique regular and strongly regular graph is also strongly regular.

Theorem 4.2. Suppose Γ is ω-clique regular and a non-boring srg(n, k, λ, µ) with spectrum

k1, rf , s
g where r > s. Then the ω-clique graph of Γ is strongly regular if and only if

s = −k
ω−1 or k = ω(ω − 1). If so, Cω(Γ) has parameters

srg ( nk
ω(ω − 1) , ω ( k
ω − 1 − 1) , λ∗, µ∗)

and if λ = ω − 2, then λ
∗ = k
ω−1 − 2 and µ∗ = µ + ω − k
ω−1.

Note that λ∗ and µ∗ are forced by the spectrum of Cω(Γ) and can be always be derived

from it, but if Γ is a regular clique assembly (equivalent to λ = ω − 2 by Theorem 1.2) we

can derive simpler formulas for the srg parameters.

Proof. Since Cω(Γ) is ω( k
ω−1 − 1)-regular, then it is sufficient to show that the adjacency

matrix of Cω(Γ) has 3 or less distinct eigenvalues if and only if s = −k
ω−1 or k = ω(ω − 1).

The spectrum of C3(Γ) is given by (4.3). If s = −k
ω−1, then ( k
ω−1 + s − ω) = −ω and if

k = ω(ω − 1) then m = n implies the multiplicity of −ω is 0. So regardless, Cω(Γ) has no

more than 3 distinct eigenvalues.

Conversely, assume Cω(Γ) has 3 or less distinct eigenvalues. This implies that one of

the multiplicities in the spectrum (4.3) equals 0 or two of the eigenvalues are equal. If the

first case, then m − n must equal 0 since 1, f, g ̸= 0. Then m = nk
ω(ω−1) = n implies

k = ω(ω − 1). If two of the eigenvalues of are equal, we will show s = −k
ω−1. If any of the

latter 3 eigenvalues in (4.3) are equal, it would imply that k = r, k = s or r = s, a

30

contradiction. So −ω is equal to one of the other eigenvalues implying k, r or s must be

equal to −k
ω−1. From Corollary 3.7, we have k > r > s ≥ −k
ω−1 implying s = −k
ω−1.

Now assume that Cω(Γ) is strongly regular and λ = ω − 2. For the case ω = 2 or 3, the

result λ∗ = k
ω−1 − 2 is shown in [10, pg. 304]. So assume ω ≥ 4.

Let c1 and c2 be adjacent vertices in Cω(Γ) (that is, ω-cliques in Γ) and let x ∈ Γ be

the unique vertex that c1 and c2 share. Then c1 and c2 are commonly adjacent to all the

other cliques containing x. So λ
∗ ≥ k
ω−1 − 2. Suppose for contradiction there exists another

clique ci commonly adjacent to c1 and c2 such that x is not in ci. Let y1 and y2 be the

unique common vertices of c1 with ci, and c2 with ci respectively. Since y1 and y2 are both

in clique ci, they share ω − 2 common neighbors in that clique. And because λ = ω − 2,

these are all the common neighbors that they share which contradicts the fact that x is

adjacent to both and x is not in ci. So λ∗ = k
ω−1 − 2.

For µ
∗ recall that for any srg, λ − µ = r + s. So we get

λ∗ − µ∗ = r∗ + s∗

µ∗ = λ
∗ − r∗ − s∗

= ( k
ω − 1 − 2) − ( k
ω − 1 + r − ω) − ( k
ω − 1 + s − ω)

= 2ω − (r + s) − 2 − k
ω − 1

= 2ω − (λ − µ) − 2 − k
ω − 1

= 2ω − (ω − 2 − µ) − 2 − k
ω − 1

= µ + ω − k
ω − 1 .
 31

Corollary 4.3. Suppose Γ is ω-clique regular and a non-boring srg(n, k, λ, µ). Then Γ and

Cω(Γ) are srgs with the same parameters if and only if k = ω(ω − 1).

Proof. If k = ω(ω − 1), then it follows that Γ and Cω(Γ) have the same spectrum, and it is

easily provable that strongly regular graphs with the same spectrum have the same

parameters. Conversely if Γ and Cω(Γ) have the same parameters then nk
ω(ω−1) = n which

implies k = ω(ω − 1).

Even if a strongly regular clique regular graph Γ does not have a strongly regular

clique graph, Cω(Γ) would still have structural properties that we can derive from its

spectrum. Since it would have exactly the four eigenvalues given in (4.3) and would be

regular, it would also have another property called walk-regularity [6, Corollary 15.1.2].

This means that for each vertex in the graph, the number of closed walks of a particular

length is the same and is given by the sum of all eigenvalues of the graph raised to the

power ℓ and divided by the number of vertices of the graph. In our case for example, the

number of closed walks at any vertex v ∈ Cω(Γ) of length ℓ ≥ 1 is given by the expression

1
m
 ((
ω ( k
ω − 1 − 1))ℓ + f ( k
ω − 1 + r − ω)ℓ + g ( k
ω − 1 + s − ω)ℓ + (m − n)(−ω)ℓ)

(4.4)

where m = nk
ω(ω−1).

This gives a necessary condition on the existence of such a graph, since the expression

(4.4) must be a non-negative integer for every positive integer ℓ. Simply put, if we can find

a feasible parameter set (n, k, λ, µ) for which it is provable that any strongly regular graph

with these parameters must be ω-clique regular, but there exists a positive integer ℓ such

that the expression (4.4) is not a positive integer, it would show there exists no strongly

regular graph with parameters (n, k, λ, µ).

If we were to make use of this necessary condition, there would then be two challenges:

finding parameter sets for which any strongly regular graph must be clique regular, and

finding an integer ℓ for which the expression (4.4) is negative or not an integer. We deal

32

with the first challenge in the next section 4.2, in which we discuss a family of feasible

parameter sets for which graphs must be clique regular. Unfortunately however for the

second challenge, we can show that it is functionally impossible.

The first two exponentials in expression 4.4 are always positive and almost always

larger in magnitude than the last two exponentials, so the whole expression is always

positive for any ℓ ≥ 1 as long as (n, k, λ, µ) is a feasible parameter set. We won’t show this

claim rigorously since it is semi-intuitive and not very important for the remainder of our

discussion. The important part is we can show that as long as (n, k, λ, µ) is a feasible

parameter set, the more restrictive condition holds; expression (4.4) is an integer for all

ℓ ≥ 1.

Proposition 4.4. Suppose (n, k, λ, µ) is a feasible strongly regular parameter set with

spectrum k1, rf , s
g and ω ≥ 2 is such that m = nk
ω(ω−1) and k
ω−1 are integers. Then m divides

(
ω ( k
ω − 1 − 1))ℓ + f ( k
ω − 1 + r − ω)ℓ + g ( k
ω − 1 + s − ω)ℓ + (m − n)(−ω)ℓ

for all non-negative integers ℓ.

Note that we only need to show this for positive integers ℓ, but since we will use

stacked inductions on ℓ, having the base case ℓ = 0 makes for an easier proof.

Proof. For brevity, define ˜k = ω ( k
ω−1 − 1)
, ˜r = ( k
ω−1 + r − ω) and ˜s = ( k
ω−1 + s − ω), and

let “≡” represent equivalence modulo m. We will show the theorem by induction on ℓ ≥ 0.

The algebra in each base case follows from equations (4.1) and (4.2). For the first base case

ℓ = 0 we get ˜k0 + f ˜r0 + g˜s0 + (m − n)(−ω)0 = 1 + f + g + m − n = m since 1 + f + g = n.

33

Assuming ˜kℓ + f ˜rℓ + g˜sℓ − n(−ω)ℓ ≡ 0 for some ℓ ≥ 0 gives

˜kℓ+1 + f ˜rℓ+1 + g˜sℓ+1 − n(−ω)ℓ+1

≡ ˜kℓ (ω ( k
ω − 1 − 1)) + f ˜rℓ ( k
ω − 1 + r − ω) + g˜sℓ ( k
ω − 1 + s − ω) + ω(n(−ω)
ℓ)

≡ −ω(˜kℓ + f ˜rℓ + g˜sℓ − n(−ω)ℓ) + k
ω − 1 (˜kℓ + f ˜rℓ + g˜sℓ) + k˜kℓ + f r˜rℓ + gs˜sℓ

≡ k
ω − 1 (n(−ω)
ℓ) + k˜kℓ + f r˜rℓ + gs˜sℓ

≡ ωm(−ω)ℓ + k˜kℓ + f r˜rℓ + gs˜sℓ

≡ k˜kℓ + f r˜rℓ + gs˜sℓ

So it suffices to show that m divides k˜kℓ + f r˜rℓ + gs˜sℓ which we will do by induction on

ℓ ≥ 0. The base case ℓ = 0 is k + f r + gs = 0. Assume k˜kℓ + f r˜rℓ + gs˜sℓ ≡ 0 for some

ℓ ≥ 0 and we get

k˜kℓ+1 + f r˜rℓ+1 + gs˜sℓ+1

≡ k˜kℓ (ω ( k
ω − 1 − 1)) + f r˜rℓ ( k
ω − 1 + r − ω) + gs˜sℓ ( k
ω − 1 + s − ω)

≡ ( k
ω − 1 − ω) (k˜kℓ + f r˜rℓ + gs˜sℓ) + k2˜kℓ + f r2˜rℓ + gs
2˜sℓ

≡ k2˜kℓ + f r2˜rℓ + gs2˜sℓ

≡ k2˜kℓ − r(k˜kℓ + gs˜sℓ) + gs2˜sℓ

≡ k(k − r)˜kℓ + gs(s − r)˜sℓ

So it suffices to show that m divides k(k − r)˜kℓ + gs(s − r)˜s
ℓ which we will again do by

induction on ℓ ≥ 0. The base case is k(k − r) + gs(s − r) = nk = mω(ω − 1). Assume

34

k(k − r)˜kℓ + gs(s − r)˜s
ℓ ≡ 0 for some ℓ ≥ 0 and we get

k(k − r)˜kℓ+1 + gs(s − r)˜s
ℓ+1

≡ k(k − r)˜kℓ (
ω ( k
ω − 1 − 1)) + gs(s − r)˜s
ℓ ( k
ω − 1 + s − ω)

≡ ( k
ω − 1 − ω) (k(k − r)˜kℓ + gs(s − r)˜s
ℓ) + k2(k − r)˜kℓ + gs2(s − r)˜s
ℓ

≡ k2(k − r)˜kℓ + gs
2(s − r)˜s
ℓ

≡ k2(k − r)˜kℓ − s(k(k − r)˜kℓ)

≡ k(k − r)(k − s)˜kℓ

≡ nkµ˜kℓ from equations (4.1) and (4.2)

≡ mω(ω − 1)µ˜kℓ

≡ 0

While this shows we will not be able to eliminate any feasible parameter sets from

possibly existing just by finding an integer ℓ, we show in the next section that the fact

about walk-regularity can be used to find other restrictive conditions on the existence of a

certain family of strongly regular graphs.

4.2 Locally Linear Strongly Regular Graphs

An srg(n, k, λ, µ) is locally linear (3-clique regular) if and only if λ = 1. There are

many other families of strongly regular graphs that have the clique regular property which

we will discuss in chapter 6, but the locally linear strongly regular graphs are interesting

because they are the only ones for which the clique regular property is forced by their

parameters. It follows from Theorem 1.2 that any srg(n, k, 1, µ) is not only 3-clique regular

but also a regular clique assembly.
 35

As discussed in the introduction, the existence problem for these graphs was the main

motivation for this investigation, and so in this section we explore multiple different

approaches to try and find a necessary condition on the existence of these graphs.

Using Theorem 4.2, we can enumerate all non-boring locally linear strongly regular

graphs that have strongly regular 3-clique graphs. It turns out there are only three.

Theorem 4.5. The only non-boring strongly regular locally linear graphs that have strongly

regular 3-clique graphs are the unique graphs with the parameters srg(9, 4, 1, 2),

srg(15, 6, 1, 3), and srg(27, 10, 1, 5).

Proof. These graphs all have strongly regular 3-clique graphs following from Theorem 4.2.

So let Γ be an srg(n, k, 1, µ) such that C3(Γ) is strongly regular and we will show that Γ is

the unique strongly regular graph on one of the enumerated parameters. From Theorem

4.2 either k = 6 or s = − k
2 so first assume k = 6. Then from (n − k − 1)µ = k(k − λ − 1) it

follows that n = 24
µ + 7. So since µ divides 24, µ ∈ {1, 2, 3, 4, 6, 8, 12, 24}. From (4.2), the

multiplicity of the largest eigenvalue of Γ is

f = 1
2
 [( 24
µ + 6) − 12 + ( 24
µ + 6)(1 − µ)
√
(1 − µ)2 + 4(6 − µ)
]
 ,

from which it follows that f is only an integer when µ = 3. This shows that Γ is the unique

srg(15, 6, 1, 3).

Now assume that s = − k
2 . From (4.2) we get

s = 1
2
 [(1 − µ) − √
(1 − µ)2 + 4(k − µ)] = −k
2 ,

which implies that µ = k
2 . So from (n − k − 1)µ = k(k − λ − 1) we get that Γ is an

srg(3(k − 1), k, 1, k
2 ) for some k. So the multiplicity of the smallest eigenvalue of Γ is

g = 8(k − 1)
k + 2 .

36

Since 0 < g < 8 when k > 1, g ∈ {1, . . . , 7} since the multiplicity must be an integer.

Solving for k gives k ∈ {2, 4, 6, 10, 22} since k must also be an integer. If k = 2 this implies

that Γ ∼= K3, a boring graph, and k = 22 gives the parameters of Γ as srg(63, 22, 1, 11)

which violate the absolute bound [5]. The remaining k ∈ {4, 6, 10} give the result.

Even if the 3-clique graph of an srg(n, k, 1, µ) is not strongly regular, it still has some

highly restrictive structural properties. For the remainder of this section, Γ will represent a

non-boring srg(n, k, 1, µ) that is not one of the three enumerated in Theorem 4.5. From

Theorem 4.1, it will have spectrum k1, rf , s
g where these values are given by equations

(4.2). So C3(Γ) will be a connected rca(m, d, ω) from Theorem 1.3 and will have spectrum

d1, ˜rf , ˜sg, −3
(m−n) where
 m = nk
6 , d = 3 ( k
2 − 1) , ω = k
2 ,

˜r = k
2 + r − 3, and ˜s = k
2 + s − 3,

from equation (4.3).

As we discussed in section 4.1, C3(Γ) is walk-regular which means that the number of

closed walks of length ℓ through some vertex in the graph is given by the expression

θℓ := 1
m (
dℓ + f ˜rℓ + g˜sℓ + (m − n)(−3)ℓ)

and is independent of the vertex chosen. Using this idea, we can easily calculate the

number of triangles and quadrangles through a given point respectively as

∆ := θ3
2 and Ξ := θ4 − 2d2 + d
2 .

So now fix some vertex v in C3(Γ). The neighborhood of v is fully understood since

C3(Γ) is an rca(m, d, ω), so we will study the vertices not adjacent to v. Define Ti as the

37

set of vertices not adjacent to v that have exactly i neighbors in common with v, and

τi = |Ti| as the number of these vertices. Formally, for a vertex u ∈ C3(Γ), u ∈ Ti if and

only if u ̸∈ N (v) and |N (v) ∩ N (u)| = i. Following from Lemma 1.4, τi = 0 if i > d
ω−1 = 3

so we need only to consider T0, T1, T2, T3. This setup can be visualized in Figure 4.1.

Figure 4.1: The neighborhood of v and the Ti sets

The authors of [14] used a counting argument to derive a general system of linear

equations that walk-regular graphs must satisfy, and for graph C3(Γ) this system is:

τ0 + τ1 + τ2 + τ3 = m − d − 1,

τ1 + 2τ2 + 3τ3 = d(d − 1) − 2∆,

τ2 + 3τ3 = Ξ − (
d/3 − 1
2
 )d.
 (4.5)

For a graph with the properties of C3(Γ) to exist, there must be at least one positive integer

solution to system (4.5). We will expand this system by introducing 9 new positive integer

variables and 9 new linear equations that they must satisfy. For i, j = 0, 1, 2, 3 we define

38

ρi,j = ρj,i as the number of edges with one endpoint in Ti and the other in Tj. Note that ρi,i

does not double count edges, and is exactly the number of edges in the induced subgraph

on vertices Ti. This implies there are 10 ρ variables, but we can easily show that ρ0,3 = 0.

Proposition 4.6. There are no edges between the sets T0 and T3.

Proof. Suppose to the contrary that xy is an edge in C3(Γ) with x ∈ T0 and y ∈ T3, and

consider x,y and v as triangles in Γ. Each vertex of triangle y must share an edge with a

vertex of v since in C3(Γ) they have three common neighbors. And since x is adjacent to y

in C3(Γ), triangles x and y must share some vertex in Γ. This means at least one vertex in

triangle x is adjacent to a vertex in triangle v, but this implies x and v share a common

neighbor in C3(Γ), contradicting x ∈ T0.

We will refer to (4.5) along with the equations we derive below as the τ, ρ system. The

first four equations in the τ, ρ system involve counting the total edges coming of off the

vertices in the sets T0, T1, T2, T3.

Proposition 4.7. We have
 (d − i)τi = ρi,i +
 3∑

j=0 ρi,j

for each i = 0, 1, 2, 3.

Proof. A vertex not adjacent to v that has i neighbors in common with v has i of its edges

going into N (v) and so the remaining d − i edges are incident with other vertices not

adjacent to v. So these total edges are counted by the sum of ρi,j but the edges between

two vertices each sharing exactly i common neighbors with v is double counted.

These four equations are clearly independent and we can verify with SAGE that so far,

the whole τ, ρ system is also independent. The next four equations arise from counting the

number of 3-walks between v and vertices not adjacent to v.

39

Proposition 4.8. We have

(
9µ + i ( d
3 − 5 − µ
)) τi = iρi,i +
 3∑

j=1 jρi,j

for each i = 0, 1, 2, 3.

Proof. This is equivalent to showing

((9 − i)µ − 4i + 2i (k
2 − 2)) τi = i ( d
3 − 1) τi + iρi,i +
 3∑

j=1 jρi,j.

First, we will show that the coefficient on τi from the left hand side of this equation counts

the number of 3-walks between v and a vertex u ∈ Ti. Consider u and v as triangles in Γ.

Of the 3 vertices in triangle u, i of them are adjacent to a vertex of triangle v. Call the

vertices of triangle u = {u1, u2, u3} and v = {v1, v2, v3}, ordered so that uj is adjacent to vj

for j = 1, . . . , i, where no vertices are adjacent if i = 0.

Consider first a pair of adjacent vertices vj and uj. The edge ujvj is contained in a

unique triangle denoted Cuj vj . The edges of uj are partitioned into k
2 triangles of which u

and Cuj vj are two. In C3(Γ), walking from u to one of these triangles, then to Cuj vj and

finally to v is a 3-walk. There is the same number of 3-walks obtained by considering the

edges at vj and there are i pairs of adjacent vertices to consider, so we add the term

2i ( k
2 − 2) to the coefficient.

Now consider a pair of non adjacent vertices vj and uh with j ̸= h. These vertices

share µ common neighbors in Γ since it is an srg(n, k, 1, µ), but depending on if uh or vj is

adjacent to a vertex in v or u respectively, some of these common neighbors may be in u or

v. Let x ∈ N (vj) ∩ N (uh) a common neighbor that is not in triangle u or v. The edges xvj

and xuh are contained in unique triangles Cxvj and Cxuh, and so there is the 3-walk in

C3(Γ) u → Cxuh → Cxvj → v. Breaking down the cases for each i = 0, 1, 2, 3 and each pair

40

of non-adjacent vertices vj and uh, we can count that the number of these 3-walks is given

by the term (9 − i)µ − 4i.

The right hand side counts the total number of 3-walks between vertices in Ti and v as

well but from the perspective of C3(Γ). Let u ∈ Ti, and for each of the i different vertices

x ∈ N (u) ∩ N (v), and the ( d
3 − 1) vertices y ∈ N (x) ∩ N (v) we have a 3-walk

u → x → y → v. So we add the term i ( d
3 − 1) τi.

Finally, for each edge ux with u ∈ Ti and x ∈ Tj for some j = 0, 1, 2, 3, there are j

3-walks from u to x to each of the j vertices in N (x) ∩ N (v) and then to v. However, we

need to double count the edges within Ti since a 3-walk could start at either endpoint. So

we add a jρi,j term for each j but an additional term for iρi,i.

While it is clear that these four equations are independent, using SAGE we can verify

that the τ, ρ system with the 11 equations we have so far shown has only rank 10, meaning

one of the four equations from Proposition 4.8 is a linear combination of the other 9

equations and does not provide any useful restriction.

The last equation comes from counting the number of closed 5-walks at vertex v. For

this equation we must first count the number of 5-walks in C3(Γ) starting and ending at v

for which every vertex in the walk is either v or adjacent to v.

41

Lemma 4.9. The number of closed 5-walks at v for which every vertex in the walk is either

v or adjacent to v, is given by
 ⋆ := d
4

27 + d3

3 − d2 − d.

Proof. The induced subgraph of C3(Γ) on vertices v and N (v) has adjacency matrix

B :=
 









0 j⊤ j⊤ j⊤

j J d
3 − I d
3 0 0

j 0 J d
3 − I d
3 0

j 0 0 J d
3 − I d
3
 










where j is the all ones column vector of length d
3 and jj⊤ = J d
3 is the d
3 × d
3 all ones matrix.

The number of closed 5-walks at vertex v is given by (B5)1,1 which can be found when we

notice that j⊤j = d
3 . We omit a proof by hand because it is tedious and lengthy, but it can

be verified with SAGE that (B5)1,1 = ⋆.

Proposition 4.10. We have

∑

i≤j ijρi,j = θ5 − ⋆
2 − 4
3∆d − 2 ( d
3 − 1) (
Ξ − (d/3 − 1
2
 )
d) .

Proof. This equation is equivalent to

θ5 = ⋆ + 8
3 ∆d + 4 ( d
3 − 1) (τ2 + 3τ3) + 2 ∑

i≤j ijρi,j

and since θ5 is the total number of closed 5-walks at vertex v, this can be shown with a

counting argument. Since ⋆ counts all 5-walks in which every vertex is v or adjacent to v,

we need now only count the 5-walks in which one or two vertices is not adjacent to v. For

notational convenience, denote N = {v} ∪ N (v).

42

Take some triangle at v with other vertices x and y. For each vertex u ∈ N (x) − N ,

there are the two closed 5-walks at v, v → x → u → x → y → v and the same walk in

reverse order. By the structure of C3(Γ) apparent in Figure 4.1, we have

|N (x) − N | = d − |N (x) ∩ N | = d − d
3 = 2
3d. Since the same number of 5-walks comes from

vertex y and there are ∆ triangles, we add the term 8
3∆d.

Now let u ∈ Ti so that there are i edges going from u into N (v). Choosing two of these

i edges, let x, y ∈ N (v) be the vertices they connect to. For each of the d
3 − 1 vertices

z ∈ N (x) ∩ N (v), there is the 5-walk v → z → x → u → y → v and its reversed order.

Since the same number of 5-walks comes from vertex y and there are (i
2
) ways to choose

the edges off of u, we add the term 4 ( d
3 − 1) (i
2
)τi for each i = 0, 1, 2, 3. Since
(
0
2) = (1
2
) = 0, this becomes the term 4 ( d
3 − 1) (τ2 + 3τ3), and we can replace τ2 + 3τ3 with

Ξ − (
d/3−1
2 )
d from the original system (4.5). These first two terms capture every closed

5-walk with only one vertex not adjacent to v.

And finally, let xy be some edge of C3(Γ) with x ∈ Ti and y ∈ Tj so there are i edges

going from x to N (v) and j edges going from y to N (v). Thus there are ij different ways to

choose some combination of these edges, and each combination corresponds to a closed

5-walk at v and the reversed order walk. Since there are ρi,j such edges, we add the term

2ijρi,j for each i, j = 0, 1, 2, 3 and i ≤ j. This term captures every closed 5-walk with two

vertices not adjacent to v.

Using SAGE, we can verify that this equation is also a linear combination of the other

equations in the τ, ρ system, and so provides no useful information.

While these are theoretical proofs that C3(Γ) must satisfy the τ, ρ system, it is useful

to verify that they hold for real graphs. There are four known constructions of

srg(n, k, 1, µ)’s other than the three from Theorem 4.5. In table 4.1, we show the

parameters of these graphs, the parameters and spectrums of their 3-clique graphs, and the

τ and ρ values of these graphs numbered 1 to 4. We can use SAGE to show that these

values do provide solutions to the τ, ρ system that we derived above.

43

The graphs 1,2 and 4 from table 4.1 are vertex transitive, which means that every

vertex is symmetrical to every other vertex via a graph automorphism. As a consequence,

fixing any vertex produces the same solution to the τ, ρ system. However graph 3, an

srg(378, 52, 1, 8), is not vertex transitive and neither is its clique graph, and so fixing each

vertex produces one of three different solutions to the τ, ρ system.

# Parameters of Γ Parameters of C3(Γ) Spectrum of C3(Γ)
1. srg(81, 20, 1, 6) rca(270, 27, 10) 27
1, 9
60, 0
20, −3
189

2. srg(243, 22, 1, 2) rca(891, 30, 11) 30
1, 12
132, 3
110, −3
648

3. srg(378, 52, 1, 8) rca(3276, 75, 26) 75
1, 27
273, 12
104, −3
2,898

4. srg(729, 112, 1, 4) rca(13608, 165, 56) 165
1, 57
616, 30
104, −3
12,879

# 1. 2. 3. 4.
τ0 8 300 450 450 450 1, 452
τ1 0 540 1, 800 1, 800 1, 800 5, 940
τ2 216 0 900 900 900 5, 940
τ3 18 20 50 50 50 110
ρ0,0 0 1800 3, 525 3, 569 3, 375 21, 780
ρ0,1 0 5400 21, 000 20, 824 21, 600 130, 680
ρ0,2 216 0 5, 700 5, 788 5, 400 65, 340
ρ0,3 0 0 0 0 0 0
ρ1,1 0 4, 860 37, 566 37, 716 36, 900 222, 750
ρ1,2 0 0 35, 136 35, 064 36, 000 392, 040
ρ1,3 0 540 1, 932 1, 880 1, 800 5, 940
ρ2,2 2, 376 0 11, 664 11, 604 11, 250 249, 480
ρ2,3 432 0 1, 536 1, 640 1, 800 11, 880
ρ3,3 0 0 66 40 0 0

Table 4.1: Known srg constructions and their solutions to the τ, ρ system

This non-vertex transitive graph is useful because it provides insight into possible

expansions of the τ, ρ system. For one, since each solution has the same values for the τ

variables, it seems likely that there exists a fourth linearly independent equation in the τ

variables to extend the original system (4.5). Also, subtracting one solution vector from

each of the other two, we can see that the null-space of any expansion of the τ, ρ system

must have dimension at least two. This means there is at most one more linearly

44

independent equation in the τ and ρ variables that could be used to extend the system.

This is a possible path for future research on this topic.

So we have shown for any srg(n, k, 1, µ) to exist, there must be a solution in

non-negative integers to the rank 10, 13 variable τ, ρ system. Although this appears to be a

restrictive condition, it ultimately fails to limit the existence of these graphs. We use a

Python algorithm discussed in Appendix A to find all feasible parameters sets

srg(n, k, 1, µ) with degree k not more than 50 million, and using a tool from Microsoft

Research called Z3 [7], we can show there exists solutions for all these parameter sets. So

this condition does not eliminate any from possibility.

45

Chapter 5: Critical Groups

For a graph Γ = (V, E) with n vertices and c connected components, we define its

Laplacian as L = D − A where D is Γ’s degree matrix and A is its adjacency matrix.

Viewing the Laplacian as a map L : Zn → Z
n, then coker(L) = Z
n/Im(L) ∼= Z
c ⊕ K(Γ) for

some finite abelian group K(Γ) which we call the critical group of Γ.

It is known that the order of K(Γ) is equal to κ(Γ), the number of spanning forests of

the graph. This value κ(Γ) is also equal to the determinant of any sub-matrix of L obtained

by removing the ith row and column, and when the graph is connected this is equal to the

product of the non-zero eigenvalues of the Laplacian divided by n, the number of vertices

of Γ [6, Proposition 1.3.4]. Since the Laplacian only has one zero eigenvalue when Γ is

connected, this is also equal to the expression 1
n limλ→0 (−1)np(L,λ)
−λ , which will be useful later.

There is a different formulation of the critical group of a graph that will turn out to be

more useful for our purposes [8, p. 319]. Fix some arbitrary orientation of the edges of Γ,

that is for each {x, y} ∈ E define one vertex as directed towards the other and write them

now as ordered pairs (x, y) ∈ E. This orientation can be arbitrary and up to isomorphism

will not affect the critical group.

Now consider the free abelian group on the edges of Γ, ZE, with this fixed orientation.

In order to examine edges oriented in the opposite direction, we define (y, x) = −(x, y). For

each vertex v ∈ Γ, the bond of that vertex is defined

b(v) := ∑

u∈N (v)(v, u) ∈ Z
E

and the bond space B ⊆ ZE of Γ is defined as the integer span of the bonds of every

vertex. We also define the cycle space Z ⊆ ZE of Γ as the integer span of all directed

46

cycles of the graph, where a directed cycle is defined as

ℓ∑

j=1 (uj−1, uj) ∈ ZE

where uj−1 is adjacent to uj, u0 = uℓ, and all other vertices are distinct. It is a fact that B

and Z are orthogonal with respect to the standard inner product.

With these definitions, it is possible to show that

K(Γ) ∼= Z
E/(B ⊕ Z) (5.1)

which is much easier to deal with when defining maps between critical groups.

5.1 The Critical Group of a Clique Subdivision Graph

In this section, we will begin establishing connections between the critical groups of Γ

and Cω(Γ) when Γ is ω-clique regular. To do this, it will be helpful to introduce a new

graph transformation, the ω-clique subdivision graph. This is defined so as to be the

halfway transformation between Γ and Cω(Γ) and generalize the concept of the edge

subdivision graph.

Denote the ω-clique subdivision graph of Γ as Sω(Γ). The vertex set of Sω(Γ) is the

vertices of Γ union the ω-cliques of Γ, and the graph is bipartite on this partition with a

vertex adjacent to a clique if and only if the clique contains that vertex. Figure 5.1 shows

an example of this construction.

It should be clear by this definition, that if R is the ω-clique incidence matrix of Γ,

then the adjacency matrix of Sω(Γ) is
 


 0 R⊤

R 0
 


. And if Γ is ω-clique regular with n

47

(a) A 3-clique regular graph Γ (b) The graph S3(Γ)

Figure 5.1: An example of the clique subdivision graph

vertices and m ω-cliques, then the degree matrix of Sω(Γ) is
 


ωIm 0

0 1
ω−1D



 where D is the

degree matrix of Γ.

For the remainder of this chapter, A will be the adjacency matrix of Γ, D the degree

matrix, L = D − A the Laplacian, R the ω-clique incidence matrix, V the vertex set, E the

edge set, and similarly for graphs Sω(Γ) and Cω(Γ) but with the subscripts S and C

respectively.

Theorem 5.1. Suppose Γ = (V, E) is an ω-clique regular graph with n vertices, m

ω-cliques and c connected components. Then

κ(Sω(Γ)) = ωm−n+cκ(Γ). (5.2)

If Γ is also k-regular, then

κ(Cω(Γ)) = ( k
ω − 1
 )m−n−c ωm−n+cκ(Γ). (5.3)

48

Note that this implies if Γ is k-regular, then

κ(Cω(Γ)) = ( k
ω − 1
 )m−n−c κ(Sω(Γ))

and it was this fact which motivated the definition of Sω(Γ). For the remainder of this

section, n, m, and c will be defined as they are in Theorem 5.1.

Proof. We will begin by showing equations (5.2) and (5.3) when Γ is connected (c = 1).

The characteristic polynomial of the Laplacian of Sω(Γ) is given by

(−1)
m+np(LS; λ) =
 ∣
∣
∣
∣
∣
∣
∣
(ω − λ)Im −R⊤

−R 1
ω−1D − λIn
∣
∣
∣
∣
∣
∣
∣

= (ω − λ)m ∣
∣
∣
∣ 1
ω−1D − λIn − 1
ω−λRR⊤∣
∣
∣
∣ from [1, p. 114]

= (ω − λ)m−n ∣
∣
∣
∣ ω−λ
ω−1 D − λ(ω − λ)In − RR⊤∣
∣
∣
∣

= (ω − λ)m−n ∣
∣
∣
∣ ω−λ
ω−1 D − λ(ω − λ)In − A − 1
ω−1D
∣
∣
∣
∣ by Lemma 3.4

= (ω − λ)m−n ∣
∣
∣
∣D − A − λ(ω − λ)In − λ
ω−1D
∣
∣
∣
∣ .

For brevity define M (λ) := D − A − λ(ω − λ)In − λ
ω−1D. So we get

κ(Sω(Γ)) = 1
m + n lim
λ→0 (−1)
m+np(LS; λ)
−λ

= ωm−n

m + n lim
λ→0 |M (λ)|
−λ

= −ωm−n

m + n lim
λ→0 tr (adj(M (λ)) ( −1
ω − 1 D + (2λ − ω)In
))

where this last equality follows from L’hopitals rule, and since the derivative of the

determinant |M (λ)| is given by Jacobi’s formula [12, p. 149].

49

Carrying on and letting v1, . . . , vn be the vertices of Γ and we have

κ(Sω(Γ)) = −ωm−n

m + n tr (adj(D − A) ( −1
ω − 1 D − ωIn
))

= −ωm−n

m + n tr
 






κ(Γ) ( −d(v1)
ω−1 − ω)
 . . .
 κ(Γ) ( −d(vn)
ω−1 − ω)








= −ωm−n

m + n
 ∑

vi∈V κ(Γ) ( −d(vi)
ω − 1 − ω)

= ωm−n+1κ(Γ)
m + n
 ( Σvi∈V d(vi)
ω(ω − 1) + n)

= ωm−n+1κ(Γ)
m + n (m + n) = ωm−n+1κ(Γ)

since the sum of all degrees in a graph is twice the number of edges. Similarly, the

characteristic polynomial of the Laplacian of Cω(Γ) is given by

(−1)
mp(LC; λ) = p (
AC; ω ( k
w − 1 − 1) − λ) since Cω(Γ) is regular

= (ω ( k
w − 1
 ) − λ)m−n p (A; k − λ) by Theorem 3.5

= (ω ( k
w − 1
 ) − λ)m−n (−1)
np (L; λ) . since Γ is regular

So we have
 κ(Cω(Γ)) = 1
m lim
λ→0 (−1)
mp(LC; λ)
−λ

= ω(ω − 1)
nk
 ( k
ω − 1
 )m−n ωm−n lim
λ→0 (−1)
np(L; λ)
−λ

= ( k
ω − 1
 )m−n−1 ωm−n+1 1
n lim
λ→0 (−1)
np(L; λ)
−λ

= ( k
ω − 1
 )m−n−1 ωm−n+1κ(Γ).

50

For any c, the result now follows from the fact that the number of spanning forests equals

the product of the number of spanning trees of each connected component of a graph.

This relationship between the orders suggests a deeper relationship between the groups

and is what motivated this investigation. It was known for the case of the line graph and

edge subdivision graph (ω = 2) but we have generalized this to the ω-clique graph and

ω-clique subdivision graph for any ω ≥ 2.

The authors of [3] used a known relationship between the critical group of a graph and

its edge subdivision graph (2-clique subdivision graph), to derive a relationship between a

graph and its line graph (2-clique graph). We will generalize their argument as far as it is

possible to any ω ≥ 2, to attempt to generalize the relationship between the critical group

of an ω-clique regular graph and its subdivision graph and clique graph.

We begin by examining the relationship between K(Γ) and K(Sω(Γ)). Let B and Z

represent the bond and cycle space of Γ respectively, with BS and ZS representing them for

Sω(Γ). In general, anything with no subscript relates to Γ, and anything with the subscript

S relates to Sω(Γ).

For basis vectors (v, C) ∈ ES, with v a vertex in Γ and C an ω-clique containing v, and

(x, y) ∈ E for arbitrary adjacent vertices x and y, define the Z-module homomorphisms

h : ZES → Z
E

(v, C) ↦→ ∑

u∈C−{v}(v, u)

h
⊤ : Z
E → Z
ES

(x, y) ↦→ (x, Cxy) + (Cxy, y)

where Cxy is the unique ω-clique containing edge (x, y).

51

Lemma 5.2. The functions h and h
⊤ are adjoint.

Proof. It suffices to show for arbitrary basis elements (x, y) and (u, C) of ZE and ZES

respectively, that
 ⟨h(u, C), (x, y)⟩ = ∑

v∈C−{u}
⟨(u, v), (x, y)⟩

=
 



1 if C = Cxy and u = x

−1 if C = Cxy and u = y

0 otherwise

= ⟨(u, C), (x, Cxy)⟩ + ⟨(u, C), (Cxy, y)⟩

= ⟨(u, C), h
⊤(x, y)⟩

where ⟨·, ·⟩ is the standard inner product.

Using the critical group formulation in equation (5.1), we can show that h and h
⊤

induce homomorphisms between the critical groups K(Γ) and K(Sω(Γ)). That is, the maps

defined by x + (B ⊕ Z) ↦→ h⊤(x) + (BS ⊕ ZS) and y + (BS ⊕ ZS) ↦→ h(y) + (B ⊕ Z) are well

defined homomorphisms.

Lemma 5.3. The functions h and h
⊤ induce homomorphisms,

h : K(Sω(Γ)) → K(Γ)

h
⊤ : K(Γ) → K(Sω(Γ)).

Proof. It is clear from equation (5.1) that we must show h(BS ⊕ ZS) ⊆ B ⊕ Z and

h
⊤(B ⊕ Z) ⊆ BS ⊕ ZS. Since h and h
⊤ are adjoint and B is orthogonal to Z, it suffices to

show that h⊤(B) ⊆ BS and h⊤(Z) ⊆ ZS. Since B is spanned by the bonds of Γ, let v ∈ V

52

and we will show h
⊤(b(v)) ∈ BS. We have

h
⊤(b(v)) = h⊤
 

 ∑

v∈N (v)(v, u)




= ∑

u∈N (v)(v, Cvu) + ∑

u∈N (v)(Cvu, u)

= (ω − 1) ∑

C∈NS (v)
(v, C) + ∑

C∈NS (v)
 

 ∑

u∈NS (C)
(C, u)


 − ∑

C∈NS (v)
(C, v)

= ωbS(v) + ∑

C∈NS (v) bS(C)

∈ BS.

Similarly, let z = ∑ℓ
j=1(uj−1, uj) be a directed cycle in Γ and we will show h
⊤(z) ∈ ZS.

We have
 h
⊤(z) = h
⊤ ( ℓ∑

j=1 (uj−1, uj)

)

=
 ℓ∑

j=1
 ((uj−1, Cuj−1uj ) + (Cuj−1uj , uj)
)

∈ ZS.

So the linear functions h and h
⊤ induce homomorphisms between the respective critical

groups, which we also denote with h and h
⊤.

Notice from Theorem 5.1, for groups K(Γ) and K(Sω(Γ)), which group is bigger

entirely depends on the sign of m − n + c. What testing with SAGE indicates is that if

m − n + c ≥ 0, then h is onto and if m − n + c ≤ 0, then h⊤ is onto. In fact, in the relevant

cases it seems that ker(h) ∼= (Z/ωZ)
m−n+c or ker(h⊤) ∼= (Z/ωZ)
n−m−c. If this were the

53

case, it would show the following short exact sequences

0 → (Z/ωZ)m−n+c → K(Sω(Γ)) h
−→ K(Γ) → 0,

0 → (Z/ωZ)n−m−c → K(Γ) h⊤
−→ K(Sω(Γ)) → 0

if m − n + c ≥ 0 or ≤ 0 respectively. Implying K(Γ) ∼= K(Sω(Γ))/ ker(h) or

K(Sω(Γ)) ∼= K(Γ)/ ker(h
⊤) in the relevant cases.

This is where the generalization differs from the argument presented in [3]. In the case

of the line graph (ω = 2) it can be shown that m − n + c ≥ 0 always. But in the

generalization, this is not the case, and so we must do twice as much work.

Starting with the case m − n + c ≥ 0, to show ker(h) ∼= (Z/ωZ)
m−n+c we claim it

suffices to show:

(1) the order of every element in ker(h) divides ω,

(2) ωm−n+c divides | ker(h)| , and

(3) ker(h) can be generated by m − n + c elements.

By the Fundamental Theorem of Finite Abelian Groups, ker(h) ∼= ⊕k
i=1(Z/diZ) for

some natural numbers k and di > 1 such that di divides di+1 for all i. If (1) can be shown,

it would require that di divides ω for all i; di ≤ ω. So if (3) can be shown, it would imply

that k ≤ m − n + c, and thus

| ker(h)| =
 k∏

i=1 di ≤ ωk ≤ ωm−n+c. (5.4)

Given this, showing (2) would imply that | ker(h)| = ωm−n+c. So if di < ω for any i, the

first inequality in (5.4) would be strict, and if k < m − n + c, the second inequality in (5.4)

would be strict. Since either case would imply | ker(h)| < ωm−n+c, we must have di = ω for

all i and k = m − n + c. Thus ker(h) ∼= (Z/ωZ)
m−n+c.

54

A similar argument can be made to show ker(h
⊤) ∼= (Z/ωZ)
n−m−c in the case

m − n + c ≤ 0.

We will begin by showing (1) in both cases.

Lemma 5.4. The composite functions

hh
⊤ : K(Γ) → K(Γ)

h
⊤h : K(Sω(Γ)) → K(Sω(Γ))

are both scalar multiplication by ω.

Proof. It suffices to show this for arbitrary basis elements (x, y) and (v, C) of ZE and ZES

respectively. First we have

h
⊤h(v, C) = h
⊤
 

 ∑

u∈C−{v}(v, u)




= ∑

u∈C−{v}
 ((v, C) + (C, u)
)

= (ω − 1)(v, C) + ∑

u∈C−{v}(C, u)

= ω(v, C) + ∑

u∈C(C, u)

= ω(v, C) + bS(C)

= ω(v, C) (mod BS).

55

And we also have

hh
⊤(x, y) = h((x, Cxy) + (Cxy, y)
)

= ∑

u∈Cxy−{x}
(x, u) + ∑

w∈Cxy−{y}
(w, y)

= 2(x, y) + ∑

u∈Cxy−{x,y}
 ((x, u) + (u, y)
)

= ω(x, y) + (ω − 2)(y, x) + ∑

u∈Cxy−{x,y}
 ((x, u) + (u, y)
)

= ω(x, y) + ∑

u∈Cxy−{x,y}
 ((x, u) + (u, y) + (y, x))

= ω(x, y) (mod Z).

Corollary 5.5. The order of each element in ker(h) and ker(h
⊤), divides ω.

Proof. Let x ∈ ker(h) and y ∈ ker(h
⊤). Then using Lemma 5.4

ωx = h⊤h(x) = h⊤(0) = 0 and ωy = hh
⊤(y) = h(0) = 0.

By Lagrange’s Theorem, this implies the order of x and the order of y both divide ω.

Now we will show (2) in both cases.

Lemma 5.6. If m − n + c ≥ 0, then ωm−n+c divides | ker(h)| and, if m − n + c ≤ 0, then

ωn−m−c divides | ker(h⊤)|.

Proof. We will start with the first case so assume m − n + c ≥ 0 which implies that ωm−n+c

is an integer. Since im(h) is a subgroup of K(Γ), by Lagrange’s Theorem |im(h)| divides

|K(Γ)| so there exists an integer a such that a|im(h)| = |K(Γ)|. So since the First

Isomorphism Theorem implies K(Sω(Γ))/ ker(h) ∼= im(h) and Theorem 5.1 states

56

|K(Sω(Γ))| = ωm−n+c|K(Γ)|, we have

|K(Sω(Γ))|
| ker(h)| = |im(h)|

a|K(Sω(Γ))|
| ker(h)| = |K(Γ)|

aωm−n+c|K(Γ)| = | ker(h)||K(Γ)|

aωm−n+c = | ker(h)|.

Thus ωm−n+c divides | ker(h)|. In the case of m − n + c ≤ 0, ωn−m−c is an integer and

Theorem 5.1 implies |K(Γ)| = ωn−m−c|K(Sω(Γ))|. So a similar argument applies to show

ωn−m−c divides | ker(h
⊤)|.

It now remains to show (3), that ker(h) can be generated by m − n + c ≥ 0 elements

and ker(h
⊤) can be generated by n − m − c ≥ 0 elements. This also differs from the

argument of the authors of [3]. In the case of the edge subdivision graph (ω = 2), it is

provable by an induction argument that both K(Γ) and K(S2(Γ)) can be generated with

m − n + c elements since m is the number of edges in this case. However, this fact does not

generalize to any ω ≥ 2, and using SAGE we can easily find examples of graphs that

require more generators. It is the same in the case that m − n + c ≤ 0.

We leave this as a path for future research, along with examining the relationship

between K(Sω(Γ)) and K(Cω(Γ)).
 57

Chapter 6: Examples

We will conclude with a discussion of certain families of graphs that have the clique

regular property. These examples are widely studied in graph theory and represent

concrete examples of the graph properties that we have been studying only theoretically

until this point. Examining these families allows for a better understanding of how our

results manifest in specific cases.

6.1 Orthogonal Array Block Graphs

An orthogonal array, denoted OA(n, m), is an n
2 × m array with entries from an

n-element set with the property that the rows of any n2 × 2 sub array consist of all n
2

possible pairs exactly once. The block graph of an orthogonal array is the graph with

vertices as the 1 × m row vectors of the OA(n, m), where two vectors are adjacent if and

only if they have the same entry in some coordinate position. This means they share the

same entry in exactly one position, since by the construction of the orthogonal array no

two vectors can share the same entry in more than one position. Figure 6.1 shows an

example of an orthogonal array and its block graph.

A clique in an orthogonal array block graph is called a canonical clique, denoted Sri,

if every vector in the clique shares the same entry i in the same column r. Clearly every

maximal clique of this form has order n.

Lemma 6.1. If Γ is the block graph of an OA(n, m) and n > (m − 1)
2, then every clique of

order n is a canonical clique.

The proof of this lemma comes from [9, pg. 99] Corollary 5.5.3.

58

1 1 1
1 2 2
1 3 3
2 1 2
2 2 3
2 3 1
3 1 3
3 2 1
3 3 2

(a) An OA(3, 3) and (b) its Block Graph

Figure 6.1

Corollary 6.2. If Γ is the block graph of an OA(n, m) and n > (m − 1)
2, then Γ is

n-clique regular and Cn(Γ) is isomorphic to the complete m-partite graph where each

independent set of vertices has order n.

Proof. If two vectors v and u are adjacent in Γ, then they share the same entry i in some

column r. This is the only entry that the two vectors share by the construction of the

orthogonal array. So the only canonical clique the edge vu is in is Sri and by Lemma 6.1

this is the only n-clique the edge is in.

Also by Lemma 6.1, the canonical cliques of Γ form all the vertices in Cn(Γ). Notice

that if i ̸= j then for all columns r, Sri and Srj have an empty intersection so are not

adjacent in Cn(Γ). Also notice that by the definition of an orthogonal array, if r ̸= t then

for all i and j, Sri and Stj share the vector with entry i in column r and entry j in column

t and so are adjacent in Cn(Γ). So there are m independent sets of order n in Cn(Γ) and

each vertex in each set is adjacent to every other vertex of every other independent set.

Thus, Cn(Γ) is isomorphic to the complete m-partite graph where each independent set of

vertices has order n.

A square rook graph is the graph with vertices as the points in a square grid where

two points are adjacent if and only if they are in the same row or column.

59

Corollary 6.3. If Γ is the square rook graph on n2 vertices, then Γ is n-clique regular and

Cn(Γ) ∼= Kn,n.

Proof. Since the square rook graph on n
2 vertices is the block graph of an OA(n, 2), the

result follows from Corollary 6.2.

The result also follows from Theorems 2.4 - 2.8 since the square rook graph on n
2

vertices is the line graph of Kn,n which is n-regular and triangle-free.

It also follows using the graph’s spectrum since the square rook graph on n2 vertices is

an srg(n2, 2(n − 1), n − 2, 2) with spectrum

2(n − 1)1, (n − 2)
2(n−1), −2
(n−1)2.

Using Remark 3.6, the spectrum of Cn(Γ) is

n1, 0
2(n−1), −n
1

and a classical result in spectral graph theory states this spectrum uniquely determines

that Cn(Γ) ∼= Kn,n.
 6.2 Triangular Graphs

A triangular graph, denoted Tn, is the line graph of the complete graph on n

vertices, Kn.

Corollary 6.4. If n = 3 or n > 4, then Tn is (n − 1)-clique regular and Cn−1(Tn) ∼= Kn.

Proof. This follows from Theorems 2.4 and 2.7 since Kn is (n − 1)-regular. Note that T4 is

not included since K4 is 3-regular but not triangle-free.

Alternatively we can prove this using the spectrum of Tn which is

2(n − 2)1, (n − 4)
n−1, −2 n(n−3)
2

60

because Tn is an srg( 1
2n(n − 1), 2(n − 2), n − 2, 4). Also since Tn is also (n − 1)-clique

regular and 2(n − 2)-regular, Remark 3.6 gives the spectrum of Cn−1(Tn) as

(n − 1)1, −1n−1.

A well known result in spectral graph theory is that the only regular graph with this

spectrum is the complete graph on n vertices. So Cn−1(Tn) ∼= Kn.

6.3 Generalized Quadrangle Collinearity Graphs

A Generalized Quadrangle GQ(s, t) is a point-line incidence structure satisfying

the following properties for some s, t ≥ 1:

• every line has s + 1 points,

• every point lies on t + 1 lines,

• there is at most one point common to any two distinct lines, and

• if point P is not on line ℓ, then there is a unique line incident with P meeting ℓ.

The collinearity graph of a GQ(s, t) is the graph where the vertices are the set of points

in the GQ(s, t) where two points are adjacent if and only if there is some line in the

GQ(s, t) that they are commonly incident to. Figure 6.2 shows an example of a generalized

quadrangle and it’s collinearity graph.

Corollary 6.5. Suppose Γ is the collinearity graph of a GQ(s, t). Then Γ is (s + 1)-clique

regular and a regular clique assembly.

Proof. Observe that the s + 1 points on any line in the GQ(s, t) induce an (s + 1)-clique in

Γ. It follows from the definition that generalized quadrangles contain no triangles, so the

only (s + 1)-cliques in Γ are those induced by the set of points on some line. So if points v

61

(a) A GQ(2, 2) and (b) its Collinearity Graph

Figure 6.2

and u are adjacent in Γ then they are commonly incident to some line ℓ in GQ(s, t). So the

edge uv is in the (s + 1)-clique induced by the points on line ℓ and points u and v are

commonly incident to no other lines, so the edge uv is in a unique (s + 1)-clique in Γ.

Since the collinearity graph of a GQ(s, t) is an srg((s + 1)(st + 1), s(t + 1), s − 1, t + 1),

then Γ is a regular clique assembly by Theorem 1.2.

For our final result, recall that the dual of a point line incidence structure is the

structure formed by swapping the points and the lines of the original structure. If β is a

point line incidence structure, then point P is on line ℓ in β if and only if point ℓ is on line

P in the dual of β. In the case of generalized quadrangles, it turns out that the dual of a

GQ(s, t) is a GQ(t, s) and so has a strongly regular collinearity graph. The following

theorem gives an alternate proof that the dual of a GQ(s, t) has a strongly regular

collinearity graph.
 62

Corollary 6.6. If Γ is the collinearity graph of a GQ(s, t), then Cs+1(Γ) is isomorphic to

the collinearity graph of the dual of the GQ(s, t) structure that formed Γ and is strongly

regular with parameters
 srg((t + 1) (st + 1) , t(s + 1), t − 1, s + 1).

Proof. Let Γ be the collinearity graph of a GQ(s, t). As shown in Corollary 6.5, there

exists a bijection between the lines of the GQ(s, t) and the (s + 1)-cliques of Γ that sends a

line in the GQ(s, t) to the set of points in Γ that are incident to that line. Since the lines in

the GQ(s, t) form the points in the structure’s dual, this is a bijection between the vertices

of Cs+1(Γ) and the points on the collinearity graph of the dual of the GQ(s, t). We will

show this bijection is an isomorphism. If two points u and v are adjacent in the collinearity

graph of the dual of the GQ(s, t), then they are commonly incident to some line ℓ in the

dual of the GQ(s, t). This means that point ℓ is incident to lines u and v in the GQ(s, t)

and so the (s + 1)-cliques they form in Γ share a vertex and are adjacent in Cs+1(Γ). If

these two points are not adjacent in the collinearity graph of the dual of the GQ(s, t), then

there is no line that they are commonly incident to. So in the GQ(s, t), lines u and v share

no common point and so their (s + 1)-cliques in Γ share no vertices and are therefore not

adjacent in Cs+1(Γ). So the collinearity graph of the dual of the GQ(s, t) that formed Γ is

isomorphic to the (s + 1)-clique graph of Γ.

Now we will show that Cs+1(Γ) is strongly regular. As above, it is well known that Γ is

an srg((s + 1)(st + 1), s(t + 1), s − 1, t + 1) so it has the spectrum

s(t + 1)1, (s − 1)
 st(t+1)(s+1)
s+t , (−t − 1)
 s2(st+1)
s+t .

Since Γ is (s + 1)-clique regular and a regular clique assembly from Corollary 6.5, and the

smallest eigenvalue of Γ is equal to − s(t+1)
(s+1)−1 = −t − 1, then Theorem 4.2 tells us that

Cs+1(Γ) is strongly regular with parameters as above.

63

Appendix A

Finding Feasible Locally Linear

Strongly Regular Parameter Sets

As discussed in section 4.2, to see if our necessary condition would eliminate any

feasible locally linear strongly regular parameter sets, we needed a way to find a large

number of these sets. Strongly regular graphs have four parameters (n, k, λ, µ), but they

must satisfy the equation (n − k − 1)µ = k(k − λ − 1). This restriction reduces the feasible

parameter space from four to three dimensions, and since the locally linear restriction also

forces λ = 1, we need only check in a two dimensional space.

This means, we could write an algorithm that uses nested loops to iterate over only

two of the parameters k and n, checks if the µ value implied by the equation

(n − k − 1)µ = k(k − 2) is a non-negative integer, and finally checks that the resulting

parameter set’s spectrum, given by equations (4.2), are integral with positive integer

multiplicities. Thus, finding all parameters with k less than some large value K in this

manner, would have an average time complexity of O(K 2).

We employ a method which is faster than this naive method, shown in Algorithm 1.

Instead of iterating over k and n, we solve equation (4.2) for n = k(k−2)
µ + k + 1, and notice

this implies µ must divide k(k − 2) since n must be an integer. So while our algorithm’s

outer loop still iterates over all k less than K, the inner loop needs only to iterate over the

µ which are divisors of k(k − 2) and also less than k.

To enumerate all possible values of µ, we define a Python function which we will

denote here as MuSet(k). It takes as input an integer k, and outputs all the positive

64

divisors of k(k − 2) which are less than k. The function primarily uses the prime

factorization function factorint from the Python library SymPy, which for an integer k,

finds its prime factorization with an average time complexity of O(√k) [13]. Since we need

to find divisors of k(k − 2), we use factorint to find the prime factorizations of k and

k − 2 individually which each have a runtime of O(√k). So factorizing k(k − 2) in this

manner means MuSet(k) has a runtime of O(
√k).

Since on average for each k up to K, the size of MuSet(k) is O(log K)

[2, Theorem 3.3], this is also the average time complexity of the Inner Loop in

Algorithm 1. So we get that the runtime of the Outer Loop in Algorithm 1 is given by

O(K√K) + O(K log K) = O(K 1.5), which is faster than the naive method’s runtime of

O(K 2) as desired.

Algorithm 1: Enumerate Feasible Locally Linear SRG Parameter Sets
Input: Max value of k, K
Output: Set of Feasible Locally Linear SRG Parameter Sets with k ≤ K
FeasibleParameters ← {}
for k ← 1 to K // Outer Loop
do
for µ ∈ MuSet(k) // Inner Loop
do
n ← k(k−2)
µ + k + 1
if r, s, f, g given by equations (4.2) are integers and f, g are positive then
append (n, k, 1, µ) to FeasibleParameters
end
end
end
return FeasibleParameters
 65

Bibliography

[1] K.M. Abadir and J.R. Magnus. Matrix Algebra. Econometric Exercises. Cambridge

University Press, 2005. URL: https://books.google.com/books?id=1I70zwUf1cAC.

[2] Tom M. Apostol. Introduction to analytic number theory. Springer, 1976.

[3] Andrew Berget, Andrew Manion, Molly Maxwell, Aaron Potechin, and Victor Reiner.

The critical group of a line graph, 2010. URL: https://arxiv.org/abs/0904.1246,

arXiv:0904.1246.

[4] Norman Biggs. Algebraic graph theory. Cambridge Mathematical Library. Cambridge

University Press, Cambridge, second edition, 1993.

[5] Andries E. Brouwer. Parameters of strongly regular graphs. URL:

https://aeb.win.tue.nl/graphs/srg/srgtab.html.

[6] Andries E. Brouwer and Willem H. Haemers. Spectra of graphs. Universitext.

Springer, New York, 2012. doi:10.1007/978-1-4614-1939-6.

[7] Leonardo de Moura and Nikolaj Bjørner. Z3: An efficient smt solver. In C. R.

Ramakrishnan and Jakob Rehof, editors, Tools and Algorithms for the Construction

and Analysis of Systems, pages 337–340, Berlin, Heidelberg, 2008. Springer Berlin

Heidelberg.

[8] C. D. Godsil and Gordon Royle. Algebraic graph theory. Graduate texts in

mathematics ; 207. Springer, New York, 2001.

66

[9] Chris Godsil and Karen Meagher. Erd˝os-Ko-Rado theorems: algebraic approaches,

volume 149 of Cambridge Studies in Advanced Mathematics. Cambridge University

Press, Cambridge, 2016. doi:10.1017/CBO9781316414958.

[10] Kelly B. Guest, James M. Hammer, Peter D. Johnson, and Kenneth J. Roblee.

Regular clique assemblies, configurations, and friendship in edge-regular graphs.

Tamkang Journal of Mathematics, 48:301–320, 2017.

doi:10.5556/j.tkjm.48.2017.2237.

[11] Frank Harary. Graph theory. Addison-Wesley Publishing Co., Reading, Mass.-Menlo

Park, Calif.-London, 1969.

[12] J.R. Magnus and H. Neudecker. Matrix Differential Calculus with Applications in

Statistics and Econometrics. PROBABILISTICS AND STATISTICS. Wiley, 1988.

URL: https://books.google.com/books?id=0CXXdKKiIpQC.

[13] SymPy. Sympy 1.14.0 documentation, Apr 2025. URL: https://docs.sympy.org/

latest/modules/ntheory.html#sympy.ntheory.factor_.factorint.

[14] Edwin R. van Dam and Edward Spence. Small regular graphs with four eigenvalues.

Discrete Mathematics, 189(1):233–257, 1998. URL:

https://www.sciencedirect.com/science/article/pii/S0012365X98000855,

doi:10.1016/S0012-365X(98)00085-5.

[15] Hassler Whitney. Congruent Graphs and the Connectivity of Graphs. Amer. J. Math.,

54(1):150–168, 1932. doi:10.2307/2371086.

67
