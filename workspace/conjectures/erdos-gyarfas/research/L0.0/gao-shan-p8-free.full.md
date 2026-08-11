<!-- source: https://arxiv.org/pdf/2109.01277 | converted from PDF -->

arXiv:2109.01277v1  [math.CO]  3 Sep 2021
Erdős-Gyárfás Conjecture for P8-free graphs

Yuping Gaoa, Songling Shan
b

a. School of Mathematics and Statistics, Lanzhou University, Lanzhou 730000, China

b. Department of Mathematics, Illinois State University, Normal, IL 61790, USA

Abstract

A graph is P8-free if it contains no induced subgraph isomorphic to the path P8 on
eight vertices. In 1995, Erdős and Gyárfás conjectured that every graph of minimum
degree at least three contains a cycle whose length is a power of two. In this paper, we
conﬁrm the conjecture for P8-free graphs by showing that there exists a cycle of length
four or eight in every P8-free graph with minimum degree at least three.

Keywords: Erdős-Gyárfás Conjecture; P8-free graph; Cycle

1 Introduction

All graphs considered in this paper are undirected and simple. Let G be a graph. The vertex

set, the edge set, the maximum degree and the minimum degree of G are denoted by V (G),

E(G), ∆(G) and δ(G), respectively. For a vertex v ∈ V (G), the set of neighbors of v in G

is denoted by NG(v) or N(v) if G is understood. Let S ⊆ V (G), we use G[S] to denote the

subgraph of G induced by S and G − S to denote the subgraph G[V (G) \ S]. We write u ∼ v

if uv ∈ E(G) and u ≁ v otherwise. The connectivity of G is denoted by κ(G). A uv-path is

a path having ends as u and v. Let P be a path and x, y ∈ V (P ), we use xP y to denote the

subpath of P with ends x and y.

A path on k vertices is denoted by Pk. A cycle on k vertices is denoted by Ck and is

called a k-cycle. The length of a path or cycle is the number of edges it contains. The well-

known Erdős-Gyárfás Conjecture [2] states that every graph of minimum degree at least

three contains a 2m-cycle for some integer m ≥ 2. The conjecture is conﬁrmed for some

graph classes including K1,m-free graphs of minimum degree at least m + 1 or maximum

degree at least 2m − 1 [7], 3-connected cubic planar graphs [5], planar claw-free graphs [1]

and some Cayley graphs [3, 4]. In [6], it is proved that every cubic claw-free graph contains

a cycle whose length is 2k, or 3 · 2k, for some positive integer k.

Given a graph H, a graph G is H-free if G does not contain any induced subgraph

isomorphic to H. In this paper, we conﬁrm Erdős-Gyárfás Conjecture for P8-free graphs by

1

showing the following two theorems.

Theorem 1.1. Every P5-free graph with minimum degree at least three contains a 4-cycle.

Theorem 1.2. Every P8-free graph with minimum degree at least three contains a 4-cycle

or 8-cycle.

In conﬁrming the Erdős-Gyárfás Conjecture for P8-free graphs, Theorem 1.2 alone suf-

ﬁces. But we include Theorem 1.1 as it is stronger than the restriction of Theorem 1.2 on

P5-free graphs and also its proof technique may be of independent interests.

The remainder of the paper is organized as follows. In Section 2, we prove Theorem 1.1.

In Section 3, we prove Theorem 1.2.

2 Proof of Theorem 1.1

Proof of Theorem 1.1. Let G be a P5-free graph with δ(G) ≥ 3. We may assume that G is

connected. Otherwise, we consider a component of G instead. Furthermore, assume that G

is not complete and G contains no C4 since otherwise we are done. Let S be a minimum

cut-set of G. For x ∈ S, a component D of G − S is a complete neighborhood component

(CNC ) of x if x is adjacent in G to every vertex of D, and D is a non-CNC of x otherwise.

We need the following claim.

Claim 2.1. (i) For any vertex x ∈ S and any component D of G − S, NG(x) ∩ V (D) ̸= ∅.

(ii) For any vertex x ∈ S, x has at least c(G − S) − 1 CNCs. Equivalently, x has at most

one non-CNC.

(iii) For any CNC D of a vertex x ∈ S, |V (D)| ≤ 2.

(iv) |S| ≥ 2, i.e., κ(G) ≥ 2.

Moreover, let x, y ∈ S be distinct. Then the following statements hold.

(v) If x and y have a common CNC D, then |V (D)| = 1.

(vi) x and y have at most one common CNC.

(vii) c(G − S) ≤ 3. Furthermore, if c(G − S) = 3, then x and y have exactly one common

CNC.

(viii) There exist two vertices from S that are nonadjacent in G.

Proof. For Statement (i), as S is a minimum cut-set of G, for any x ∈ S and any component

D of G − S, it follows that NG(x) ∩ V (D) ̸= ∅.

For Statement (ii), suppose instead that x has two non-CNCs D1 and D2. Let ui ∈ V (Di)

such that x ≁ ui, and Pi be a shortest path of Di from ui to a neighbor, say xi of x in G

2

from V (Di), i = 1, 2. By the choice, Pi is an induced path of Di such that the only vertex

of Pi that is adjacent in G to x is xi, i = 1, 2. Then u1P1x1xx2P2u2 contains an induced P5,

contradicting G being P5-free.

For Statement (iii), suppose instead that |V (D)| ≥ 3. If D is a complete graph, then

G[V (D) ∪ {x}] contains a C4 and we are done. So assume that D is not a complete graph.

Then D contains an induced P3. Since x is adjacent to every vertex in D, especially adjacent

to every vertex in the P3. It follows that G contains a C4.

For Statement (iv), by (ii), each vertex x ∈ S has a CNC D. By (iii), |V (D)| ≤ 2. Let

u ∈ V (D). Then u has a neighbor y ∈ S \ {x} by δ(G) ≥ 3. So |S| ≥ 2.

Statements (v) and (vi) follow by the assumption that G contains no C4.

For Statement (vii), by (ii), each of x and y has at most one non-CNC. Then x and

y have at least c(G − S) − 2 common CNCs. This is a contradiction to statement (vi) if

c(G − S) ≥ 4. Furthermore, if c(G − S) = 3, then x and y have exactly one common CNC.

For Statement (viii), by (ii) and (iii), x has a CNC D with |V (D)| ≤ 2. Let u ∈ V (D). If

u has at least three neighbors from S, then there exist two nonadjacent vertices in N(u) ∩ S

since G contains no C4. So u has at most two neighbors in S. This, together with δ(G) ≥ 3,

implies |V (D)| = 2. Let v be the neighbor of u in D. Since |V (D)| ≤ 2 and δ(G) ≥ 3, u has

a neighbor y ∈ S \ {x}. Furthermore, y ≁ x, for otherwise yuvxy is a C4 of G.

By Claim 2.1(viii), we let x, y ∈ S such that x ≁ y in G.

Claim 2.2. c(G − S) = 2.

Proof. By Claim 2.1(vii), c(G − S) ≤ 3. Suppose that c(G − S) = 3. By Claim 2.1(vii), x

and y have exactly one common CNC D1. By Claim 2.1(ii), let D2 be a CNC of x, D3 be

a CNC of y. Note that D2 ̸= D3. Let ui ∈ V (Di), i = 1, 2, 3. Then u3 ≁ x, u2 ≁ y since G

contains no C4. It follows that u3yu1xu2 is an induced P5 in G, a contradiction.

By Claim 2.2, c(G − S) = 2. Let D1, D2 be the two components of G − S. Assume

ﬁrst that x and y have no common CNC. By Claim 2.1(ii), assume by symmetry that D1
is a CNC of x and D2 is a CNC of y. By Claim 2.1(i), there exist y1 ∈ N(y) ∩ V (D1) and

x1 ∈ N(x) ∩ V (D2). Then xy1yx1x is a C4, giving a contradiction.

Now assume that x and y have a common CNC D1 and let u ∈ V (D1). Then |V (D1)| = 1

by Claim 2.1(v). By Claim 2.1(i), there exist x1 ∈ N(x) ∩ V (D2) and y1 ∈ N(y) ∩ V (D2).

Note that x1 ̸= y1. If x1 ≁ y1, then x1xuyy1 is an induced P5 in G. So x1 ∼ y1. Since

δ(G) ≥ 3, u has a neighbor z ∈ S \ {x, y}. Because G has no C4, we have z ≁ x1, y1. Now

it must be the case that z ∼ x, as otherwise zuxx1y1 is an induced P5 in G. Similarly,

3

z ∼ y. However, it follows that z is a common neighbor of x and y other than u, showing a

contradiction. We complete the proof of Theorem 1.1.

3 Proof of Theorem 1.2

The Lemma below was shown in [6].

Lemma 3.1. Let G be a graph with δ(G) ≥ 3. If G does not contain C4, then G has an

induced cycle Ck for some k ≥ 5.

Proof of Theorem 1.2. Let G be a P8-free graph with δ(G) ≥ 3. We may assume that G

is connected. Otherwise, we just consider a component of G. Furthermore, assume that

G contains neither C4 nor C8 since otherwise we are done. By Lemma 3.1, G contains an

induced Ck for some k ≥ 5. Let C = v1v2 . . . vkv1 be a shortest induced cycle in G of length

at least 5. Then 5 ≤ k ≤ 7 since G is P8-free and G contains neither C4 nor C8.

Claim 3.2. If k = 5, then no two consecutive vertices on C share a common neighbor in G.

Proof. Suppose the claim does not hold. We assume, without loss of generality, that v1
and v2 have a common neighbor v6 ̸∈ {v1, v2, . . . , v5}. Then v6 ≁ vi for i ∈ {3, 4, 5} as G

contains no C4. We conclude that v6 has a neighbor v7 ̸∈ {v1, v2, . . . , v6} since δ(G) ≥ 3.

The minimum degree condition is repeatedly used in the following proof and we omit the

reason in the following when we say that vi has a neighbor vj for i ̸= j. It can be seen that

v7 ≁ vi for i ∈ {1, 2, 3, 5} as G contains no C4.

Case 1 v7 ∼ v4.

In this case, v7 has a neighbor v8 ̸∈ {v1, v2, . . . , v7}. And v8 ≁ vi for i ∈ {1, 2, 3, 5} since

G contains no C4 or C8.

Subcase 1.1 v8 ∼ v6.

In this case, v8 ≁ v4 otherwise v8v4v7v6v8 is a C4. It follows that v8 has a neighbor

v9 ̸∈ {v1, v2, . . . , v8}. And v9 ≁ v1 otherwise v9v1v6v8v9 is a C4, v9 ≁ v2 otherwise v9v2v6v8v9
is a C4, v9 ≁ v3 otherwise v9v8v7v4v5v1v2v3v9 is a C8, v9 ≁ v4 otherwise v9v8v7v4v9 is a C4,

v9 ≁ v5 otherwise v9v8v7v6v2v3v4v5v9 is a C8, v9 ≁ v6 otherwise v9v8v7v6v9 is a C4, v9 ≁ v7
otherwise v9v8v6v7v9 is a C4. So v9 has two neighbors v10, v11 ̸∈ {v1, v2, · · · , v9}. At least one

of v10 and v11, say v10, is not adjacent to v8. Note that v10 ≁ v7 otherwise v10v9v8v7v10 is a C4,

v10 ≁ v4 otherwise v10v9v8v7v6v2v3v4v10 is a C8, v10 ≁ v5 otherwise v10v9v8v7v6v2v1v5v10 is a

C8, v10 ≁ v1 otherwise v10v9v8v7v4v3v2v1v10 is a C8. Similarly, v10 ̸∼ v2. So v10v9v8v7v4v5v1v2
is an induced P8 in G, a contradiction. (See Figure 1(a) for an illustration.)

4

v1 v2 v3 v4 v5
v6

v7

v8

v9

v10 v11

(a) Subcase 1.1
 v1 v2 v3 v4 v5
v6

v7

v8

v9 v10

v11 v12

(b) Subcase 1.2

(c) Subcase 1.2

v1 v2 v3 v4 v5
v6

v7

v8

v9

v10 v11

v12 v13
 v1 v2 v3 v4 v5
v6

v7

v8 v9

v10 v11

(d) Case 2

Figure 1: Illustration for Claim 3.2

Subcase 1.2 v8 ≁ v6.

If v8 ≁ v4, then v8 has two neighbors v9, v10 ̸∈ {v1, v2, . . . , v8}. At least one of v9 and v10,

say v9, is not adjacent to v7. Moreover, v9 ≁ v1 otherwise v9v8v7v4v3v2v6v1v9 is a C8, v9 ≁ v2
otherwise v9v8v7v4v5v1v6v2v9 is a C8, v9 ≁ v3 otherwise v9v8v7v4v5v1v2v3v9 is a C8, v9 ≁ v4
otherwise v9v8v7v4v9 is a C4, v9 ≁ v5 otherwise v9v8v7v6v2v3v4v5v9 is a C8, v9 ≁ v6 otherwise

v9v8v7v6v9 is a C4. So v9 has two neighbors v11, v12 ̸∈ {v1, v2, . . . , v9}. At least one of v11
and v12, say v11, is not adjacent to v8. Moreover, v11 ≁ v7 otherwise v11v9v8v7v11 is a C4,

v11 ≁ v4 otherwise v11v9v8v7v6v2v3v4v11 is a C8, v11 ≁ v5 otherwise v11v9v8v7v6v2v1v5v11 is a

C8, v11 ≁ v1 otherwise v11v9v8v7v4v3v2v1v11 is a C8, v11 ≁ v2 otherwise v11v9v8v7v4v5v1v2v11
is a C8. It follows that v11v9v8v7v4v5v1v2 is an induced P8 in G, a contradiction. (See

5

Figure 1(b) for an illustration.)

Now assume that v8 ∼ v4. Then v8 has a neighbor v9 ̸∈ {v1, v2, . . . , v8}. Furthermore,

v9 ≁ vi for i ∈ {1, 2, . . . , 6} same as the case when v8 ≁ v4. And v9 ≁ v7 otherwise v9v8v4v7v9
is a C4. It follows that v9 has two neighbors v10, v11 ̸∈ {v1, v2, . . . , v9}. At least one of v10
and v11, say v10, is not adjacent to v8. Moreover, v10 ≁ v1 otherwise v10v9v8v7v4v3v2v1v10 is a

C8, v10 ≁ v2 otherwise v10v9v8v4v7v6v1v2v10 is a C8, v10 ≁ v3 otherwise v10v9v8v7v6v1v2v3v10
is a C8, v10 ≁ v4 otherwise v10v9v8v4v10 is a C4, v10 ≁ v5 otherwise v10v9v8v4v3v2v1v5v10
is a C8, v10 ≁ v6 otherwise v10v9v8v7v4v3v2v6v10 is a C8, v10 ≁ v7 otherwise v10v9v8v7v10
is a C4. So v10 has two neighbors v12, v13 ̸∈ {v1, v2, . . . , v10}. At least one of v12 and v13,

say v12, is not adjacent to v9. Moreover, v12 ≁ v1 otherwise v12v10v9v8v7v6v2v1v12 is a C8,

v12 ≁ v2 otherwise v12v10v9v8v7v6v1v2v12 is a C8, v12 ≁ v5 otherwise v12v10v9v8v7v6v1v5v12
is a C8, v12 ≁ v6 otherwise v12v10v9v8v4v5v1v6v12 is a C8, v12 ≁ v8 otherwise v12v10v9v8v12
is a C4. Note that v12 can not be adjacent to both v4 and v7 since otherwise v12v7v8v4v12
is a C4. If v12 ≁ v7, then v12v10v9v8v7v6v1v5 is an induced P8 in G, a contradiction. If

v12 ≁ v4, then v12v10v9v8v4v5v1v2 is an induced P8 in G, a contradiction. (See Figure 1(c)

for an illustration.)

Case 2 v7 ≁ v4.

In this case, v7 has two neighbors v8, v9 ̸∈ {v1, v2, . . . , v7}. We claim that we may assume

v8 ≁ v4, v8 ≁ v6. Otherwise, if one of v8 and v9, say v9, is adjacent to v4, then v8 ≁ v4
otherwise v8v4v9v7v8 is a C4 and v8 ≁ v6 otherwise v8v6v2v1v5v4v9v7v8 is a C8. So assume

that v8 ≁ v4, v9 ≁ v4. We can also assume that v8 ≁ v6 since v8 and v9 can not both be

adjacent to v6.

Furthermore, v8 ≁ v1 otherwise v8v7v6v1v8 is a C4, v8 ≁ v2 otherwise v8v7v6v2v8 is a

C4, v8 ≁ v3 otherwise v8v7v6v2v1v5v4v3v8 is a C8, v8 ≁ v5 otherwise v8v7v6v1v2v3v4v5v8 is

a C8. So v8 has two neighbors v10, v11 ̸∈ {v1, v2, . . . , v8}. At least one of v10 and v11, say

v10, is not adjacent to v7. And v10 ≁ v3 otherwise v10v8v7v6v1v5v4v3v10 is a C8, v10 ≁ v4
otherwise v10v8v7v6v1v2v3v4v10 is a C8, v10 ≁ v5 otherwise v10v8v7v6v2v3v4v5v10 is a C8, v10 ≁

v6 otherwise v10v8v7v6v10 is a C4. Note that v10 can not be adjacent to both v1 and v2,

otherwise v10v1v6v2v10 is a C4. If v10 ≁ v1, then v10v8v7v6v1v5v4v3 is an induced P8 in G,

a contradiction. If v10 ≁ v2, then v10v8v7v6v2v3v4v5 is an induced P8 in G, a contradiction.

(See Figure 1(d) for an illustration.)

Claim 3.3. k ≥ 6.

Proof. Suppose that k = 5. Since δ(G) ≥ 3, v1 has a neighbor v6 ̸∈ {v1, v2, . . . , v5}. By

Claim 3.2 and G contains no C4, v6 ≁ vi for i ∈ {2, 3, 4, 5}. So v6 has two neighbors

6

v7, v8 ̸∈ {v1, v2, . . . , v5}.

We claim that we may assume v7 ≁ v3, v7 ≁ v4. If one of v7 and v8, say v8, is adjacent

to v3, then v7 ≁ v3 otherwise v7v3v8v6v7 is a C4, and v7 ≁ v4 otherwise v7v6v8v3v2v1v5v4v7
is a C8. By the symmetry between v7 and v8, we then assume that v7 ≁ v3 and v8 ≁ v3.

Furthermore, we can assume that v7 ≁ v4 since v7 and v8 can not be both adjacent to v4.

We can also assume v7 ≁ v1. Otherwise, suppose that v7 ∼ v1. Then v8 ≁ v1 otherwise

v7v6v8v1v7 is a C4, v8 ≁ v3 otherwise take C = v1v2v3v8v6v1 and we obtain a contradiction

to Claim 3.2, v8 ≁ v4 otherwise take C = v1v6v8v4v5v1 and we obtain a contradiction to

Claim 3.2. So we take v8 to play the role of v7.

Furthermore, v7 ≁ v2, v7 ≁ v5, otherwise there is a C4 in G. By the discussion above,

v7 has two neighbors v9, v10 ̸∈ {v1, v2, . . . , v7}. We claim that we may assume v9 ≁ vi,

i ∈ {1, 2, . . . , 6}. It is easy to check that v9 ≁ v1 otherwise v9v7v6v1v9 is a C4, v9 ≁ v2
otherwise v9v7v6v1v5v4v3v2v9 is a C8, v9 ≁ v5 otherwise v9v7v6v1v2v3v4v5v9 is a C8. By

symmetry, v10 ̸∼ v1, v2, v5. If one of v9 and v10, say v10, is adjacent to v6, then v9 ≁ v6
otherwise v9v7v10v6v9 is a C4, v9 ≁ v3 otherwise v9v7v10v6v1v5v4v3v9 is a C8, v9 ≁ v4 otherwise

v9v7v10v6v1v2v3v4v9 is a C8. By the symmetry between v9 and v10, we assume that v9 ≁ v6
and v10 ≁ v6. If one of v9 and v10, say v10, is adjacent to v3, then v9 ≁ v3 otherwise v9v7v10v3v9
is a C4, v9 ≁ v4 otherwise v9v7v10v3v2v1v5v4v9 is a C8. So assume that v9 ≁ v3, v10 ≁ v3.

Finally we can assume that v9 ≁ v4 since v9 and v10 can not be both adjacent to v4.

v1 v2 v3 v4 v5

v6

v7 v8

v9 v10

v11 v12

Figure 2: Illustration for Claim 3.3

By the assumption that v9 ≁ vi, i ∈ {1, 2, . . . , 6}, v9 has has two neighbors v11, v12 ̸∈

{v1, v2, . . . , v7}. We claim that by the symmetry between v11 and v12, we may assume that

v11 ≁ vi, i ∈ {7, 6, 1, 3, 4}. It is easy to check that v11 ≁ v6 otherwise v11v9v7v6v11 is a C4,

v11 ≁ v3 otherwise v11v9v7v6v1v5v4v3v11 is a C8, v11 ≁ v4 otherwise v11v9v7v6v1v2v3v4v11 is

a C8. Symmetrically, v12 ̸∼ v6, v3, v4. If one of v11 and v12, say v12, is adjacent to v7, then

v11 ≁ v1 otherwise take C = v11v9v7v6v1v11 and we obtain a contradiction to Claim 3.2,

7

v11 ≁ v7 otherwise v11v9v12v7v11 is a C4. So assume that v11 ≁ v7, v12 ≁ v7. Finally we can

assume that v11 ≁ v1 since v11 and v12 can not be both adjacent to v1.

Note that v11 ∼ v2 and v11 ∼ v5 can not be both hold since otherwise v11v2v1v5v11
is a C4. If v11 ≁ v5, then v11v9v7v6v1v5v4v3 is an induced P8 in G, a contradiction. If

v11 ≁ v2, then v11v9v7v6v1v2v3v4 is an induced P8 in G, a contradiction. (See Figure 2 for an

illustration.)

Claim 3.4. k = 7.

Proof. Suppose that k ≤ 6, then k = 6 by Claim 3.3. So G contains no C5 since G contains

no induced C5 and no C4.

Case 1 The cycle C has two consecutive vertices that have a common neighbor in G.

We assume, without loss of generality, that v1 and v2 have a common neighbor v7. Then

v7 ≁ vi for i ∈ {3, 4, 5, 6} as G contains no C4, C5 or C8. So v7 has a neighbor v8 ̸∈

{v1, v2, . . . , v7}. Then v8 ≁ vi for i ∈ {1, 2, . . . , 6} as G contains no C4, C5 or C8. It follows

that v8 has two neighbors v9, v10 ̸∈ {v1, v2, . . . , v8}. At least one of v9 and v10, say v9, is not

adjacent to v7 since there is no C4 in G. Moreover, v9 ≁ vi for i ∈ {1, 2, . . . , 6} as G contains

no C4, C5 or C8. So v9v8v7v2v3v4v5v6 is an induced P8 in G, a contradiction. (See Figure 3(a)

for an illustration.)

v1 v2 v3 v4 v5 v6
v7

v8

v9 v10

(a) Case 1
 v1 v2 v3 v4 v5 v6

v7

v8 v9

v10 v11
 (b) Case 2

Figure 3: Illustration for Claim 3.4

Case 2 No two consecutive vertices on C share a common neighbor in G.

Since δ(G) ≥ 3, v1 has a neighbor v7 ̸∈ {v1, v2, . . . , v6}. Then v7 ≁ vi for i ∈ {2, 3, . . . , 6}

since G contains no C4 or C5 and by the assumption of Case 2. So v7 have two neighbors

v8, v9 ̸∈ {v1, v2, . . . , v7}. We claim that by the symmetry between v8 and v9, we may assume

that v8 ≁ v1 and v8 ≁ v4. If one of v8 and v9, say v9, is adjacent to v1, then v8 ≁ v1 otherwise

v8v1v9v7v8 is a C4, v8 ≁ v4 otherwise we take C = v8v7v1v2v3v4v8 and it is back to Case 1.

So we assume v8 ≁ v1 and v9 ≁ v1. We can assume that v8 ≁ v4 since v8 and v9 can not be

both adjacent to v4.
 8

Moreover v8 ≁ vi for i ∈ {2, 3, 5, 6} since G contains no C4, C5 or C8. So v8 has two

neighbors v10, v11 ̸∈ {v1, v2, . . . , v8}. By the symmetry between v10 and v11, we claim that

we may assume v10 ≁ v7, v10 ≁ v4. If one of v10 and v11, say v11, is adjacent to v7, then

v10 ≁ v7 otherwise v10v8v11v7v10 is a C4, v10 ≁ v4 otherwise v10v8v11v7v1v2v3v4v10 is a C8. So

we assume v10 ≁ v7 and v11 ≁ v7. Finally we may assume that v10 ≁ v4 since v10 and v11 can

not be both adjacent to v4.

Furthermore, v10 ≁ vi for i ∈ {1, 2, 3, 5, 6} since G contains no C4, C5 or C8. Then

v10v8v7v1v2v3v4v5 is an induced P8, a contradiction. (See Figure 3(b) for an illustration.)

By Claim 3.4, k = 7. Then G contains no Ci for i ∈ {4, 5, 6, 8}. Since δ(G) ≥ 3, v1 has

a neighbor v8 ̸∈ {v1, v2, . . . , v7}. Then v8 ≁ vi for i ∈ {2, 3, . . . , 7}. It follows that v8 has

two neighbors v9, v10 ̸∈ {v1, v2, . . . , v8}. We assume, without loss of generality, that v9 ≁ v1.

Since G contains no Ci for i ∈ {4, 5, 6, 8}, then v9 ≁ vi for i ∈ {2, 3, . . . , 7}. It follows that

v9v8v1v2v3v4v5v6 is an induced P8 in G, a contradiction. (See Figure 4 for an illustration.)

v1 v2 v3 v4 v5 v6 v7

v8

v9 v10
Figure 4: Illustration for k = 7

We complete the proof of Theorem 1.2.

References

[1] Dale Daniel and Stephen E. Shauger. A result on the Erdős-Gyárfás conjecture in planar

graphs. In Proceedings of the Thirty-second Southeastern International Conference on

Combinatorics, Graph Theory and Computing (Baton Rouge, LA, 2001), volume 153,

pages 129–139, 2001.

[2] Paul Erdős. Some old and new problems in various branches of combinatorics. volume

165/166, pages 227–231. 1997. Graphs and combinatorics (Marseille, 1995).

[3] Mohammad Hossein Ghaﬀari and Zohreh Mostaghim. Erdős-Gyárfás conjecture for some

families of Cayley graphs. Aequationes Math., 92(1):1–6, 2018.

[4] Mohsen Ghasemi and Rezvan Varmazyar. On the Erdős-Gyárfás conjecture for some

Cayley graphs. Mat. Vesnik, 73(1):37–42, 2021.

9

[5] Christopher Carl Heckman and Roi Krakovski. Erdős-Gyárfás conjecture for cubic planar

graphs. Electron. J. Combin., 20(2):Paper 7, 43, 2013.

[6] Pouria Salehi Nowbandegani, Hossein Esfandiari, Mohammad Hassan Shir-

dareh Haghighi, and Khodakhast Bibak. On the Erdős-Gyárfás conjecture in

claw-free graphs. Discuss. Math. Graph Theory, 34(3):635–640, 2014.

[7] Stephen E. Shauger. Results on the Erdős-Gyárfás conjecture in K1,m-free graphs. In Pro-

ceedings of the Twenty-ninth Southeastern International Conference on Combinatorics,

Graph Theory and Computing (Boca Raton, FL, 1998), volume 134, pages 61–65, 1998.

10
