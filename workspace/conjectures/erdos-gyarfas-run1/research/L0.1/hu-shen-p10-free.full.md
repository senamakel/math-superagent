<!-- source: https://arxiv.org/pdf/2308.05675 | converted from PDF -->

arXiv:2308.05675v2  [math.CO]  12 Aug 2023
Erd˝os-Gy´arf´as Conjecture for P10-free
Graphs
∗

Zhiquan Hu†, Changlong Shen‡

School of Mathematics and Statistics, and

Key Laboratory of Nonlinear Analysis and Applications (Ministry of Education),

Central China Normal University, Wuhan 430079, P. R. China

Abstract: Let P10 be a path on 10 vertices. A graph is said to be P10-free if
it does not contain P10 as an induced subgraph. The well-known Erd˝os-Gy´arf´as
Conjecture states that every graph with minimum degree at least three has a cycle
whose length is a power of 2. In this paper, we show that every P10-free graph with
minimum degree at least three contains a cycle of length 4 or 8. This implies that
the conjecture is true for P10-free graphs.

Keywords: Erd˝os-Gy´arf´as Conjecture; P10-free graph; cycle

1 Introduction

All graphs considered here are ﬁnite and simple. Let G be a graph. The vertex
set, the edge set and the minimum degree of G are denoted by V (G), E(G) and
δ(G), respectively. For a vertex v ∈ V (G), we denote by NG(v) the neighbors of v
in G. For S ⊆ V (G), let NG(S) = ∪x∈SNG(x) − S. For convenience, we write N(v)
and N(S) for NG(v) and NG(S), respectively. Denote by G[S] the subgraph of G
induced by S. For X, Y ⊆ V (G), EG(X, Y ) represents the set consisting of all edges
in G with one end in X and the other in Y . Let H be a graph. We say that G is
H-free if it does not contain an induced subgraph isomorphic to H. For H ⊆ G, we
use G − H to denote the subgraph of G induced by V (G) − V (H). Let x, y be two
distinct vertices of G. An (x, y)-path in G is a path from x to y. The length of a

∗Supported by NSFC grants 11771172, 11871239 and 11971196.
†School of Mathematics and Statistics, Central China Normal University, Wuhan, China,
hu zhiq@aliyun.com
‡School of Mathematics and Statistics, Central China Normal University, Wuhan, China,
clshen2019@foxmail.com
 1

shortest (x, y)-path in G is denoted by dG(x, y). If P is an (x, y)-path in G − E(H)
such that V (P ) ∩ V (H) = {x, y}, then we call P an H-path in G. (To specify the
end vertices of P , we also call P an H-(x, y)-path). We denote a path on k vertices
(resp. a cycle on k vertices) by Pk (resp. Ck). A cycle of length three is also called
a triangle. An edge is a triangulated edge if it lies in a triangle. The length of a
cycle C is denoted by ℓ(C). A chord of a cycle C is an edge of G − E(C) joining
two vertices of C. A hole of G is an induced cycle, that is, a cycle without a chord.
An m-hole is a hole of length m.

The well-known Erd˝os-Gy´arf´as Conjecture [2] states that every graph with min-
imum degree at least three has a cycle whose length is a power of 2. Markstr¨om [8]
has shown that any cubic counterexample to this conjecture must have at least 30
vertices. Nowbandegani and Esfandiari [10] showed that any bipartite counterex-
ample must have at least 32 vertices. Nowbandegani et al. [9] proved that any cubic
claw-free counterexample must have at least 114 vertices. Moreover, the conjec-
ture was conﬁrmed in the following graph classes: K1,m-free graphs with minimum
degree at least m + 1 or maximum degree at least 2m − 1 [11], planar claw-free
graphs [1], 3-connected cubic planar graphs [6], P8-free graphs [3] and some Cayley
graphs [4, 5]. In [9], Nowbandegani et al. showed that every claw-free graph with
minimum degree at least 3 has a cycle whose length is 2k or 3 · 2k, for some positive
integer k. Very recently, Liu and Montgomery [7] proved, using a new technique for
constructing even cycles, that there exists a constant c such that every graph with
average degree at least c contains a cycle whose length is a power of 2.

In this paper, we conﬁrm the Erd˝os-Gy´arf´as Conjecture for P10-free graphs by
providing the following theorem.

Theorem 1.1 Every P10-free graph with minimum degree at least three contains a
C4 or C8.

2 Preliminaries

In this section, we give some notations and lemmas used in this article. For two
integers s and t with s ≤ t , we use [s, t] to denote the set of all integers between s
and t.

For a cycle C = x1x2 · · · xmx1, we specify that the positive direction of C is the
direction in which the subscripts of vertices increase successively, and the opposite
is the negative direction. For i, j ∈ [1, m], xi−→
C xj is a path from xi to xj along C
with a positive direction. xi←−
C xj is a path from xi to xj along C with a negative
direction. For convenience, we let

NC(x) := N(x) ∩ V (C), ∀ x ∈ V (G).

2

Set Ai := NG−C(xi), 1 ≤ i ≤ m.

Moreover, we let
 IC := {xi : i ∈ [1, m] and Ai ∩ Ai+1 ̸= ∅}

and I +
C := {xi : xi−1 ∈ IC},

where the subscripts of xi and Ai are taken modulo m. Clearly, if C is an m-hole
with m ≥ 4, then xi ∈ IC if and only if the edge xixi+1 lies in a triangle.

Deﬁnition 2.1 A hole C of length at least 5 in G is good if

• there exists no hole C ′ in G such that 5 ≤ ℓ(C ′) < ℓ(C), and

• subject to this, |IC| is as large as possible.

If, in addition, ℓ(C) = m, then we call C a good m-hole.

Deﬁnition 2.2 Let H be a subgraph of a graph G and let X ⊆ V (H). If P :=
u1 . . . ut is an induced path of G − H such that

EG(V (P ), V (H)) = {u1x : x ∈ X},

then we call P a good path for (H, X). If, in addition, X = {x}, we call xu1 . . . ut
a good (H, x)-path.

Now, we show some technical lemmas for graphs without C4, which will be used
in the proof of Theorem 1.1.

Lemma 2.1 Let G be a graph with δ(G) ≥ 3 and C a cycle of length at least 4 in
G. If G does not contain C4, then G[V (C)] has an m-hole for some integer m with
5 ≤ m ≤ ℓ(C).

Proof Pick a cycle D in G[V (C)] such that

(i) ℓ(D) ≥ 4, and

(ii) subject to (i), ℓ(D) is as small as possible.

Then, ℓ(D) ≤ ℓ(C). As G does not contain C4, ℓ(D) ≥ 5. If D has no chord,
then D is the desired m-hole with m = ℓ(D). By way of contradiction, assume that
D contains a chord xy. Set C ′ = x
−→
D yx and C ′′ = x
←−
D yx. Then, C ′ and C ′′ are
cycles in G such that ℓ(C ′) + ℓ(C ′′) = ℓ(D) + 2. By symmetry, we may assume that

3

ℓ(C ′) ≥ ℓ(C ′′). Then, C ′ is a cycle in G[V (C)] with 4 ≤ ℓ(C ′) ≤ ℓ(D) − 1, contrary
to the choice of D. Hence, Lemma 2.1 is true. ✷

Note that every graph with minimum degree at least 3 admits a cycle of length
at least 4. By Lemma 2.1, the following lemma, due to Nowbandegani et al., holds.

Lemma 2.2 [9] Let G be a graph with δ(G) ≥ 3. If G does not contain C4 as a
subgraph, then G has an m-hole for some m ≥ 5.

Lemma 2.3 Let G be a graph and u, v, v′ three vertices of G such that v, v′ ∈ N(u).
Let A be a subset of V (G) − {u, v, v′} such that

min {|N(v) ∩ A|, |N(v′) ∩ A|} > 0.

If G does not contain C4 as a subgraph, then there exist two independent edges from
{v, v′} to A.

Proof By way of contradiction, assume that Lemma 2.3 is false. Then, v and v′

share a common neighbor, say w, in A. It follows that vwv′uv is a C4 in G, a
contradiction. Hence, Lemma 2.3 is true. ✷

Lemma 2.4 Let G be a graph and let C := x1x2 . . . xmx1 be a cycle in G with
5 ≤ m ≤ 7. If G contains neither C4 nor C8 as a subgraph, then |IC| ≤ 7 − m.

Proof By way of contradiction, assume that Lemma 2.4 is false. Then, t := |IC| ≥
8 − m. Denote IC := {xi1, . . . , xit}, where 1 ≤ i1 < . . . < it ≤ m. For each j ∈ [1, t],
let yij ∈ Aij ∩ Aij +1, that is, yij ∈ NG−C(xij ) ∩ NG−C(xij +1). We claim that

N(yi) ∩ {xi, xi+1, xi+2, xi+3} = {xi, xi+1}, ∀ xi ∈ IC. (1)

By way of contradiction, assume that (1) is false. Then, xj ∈ N(yi) holds for some
j ∈ {i + 2, i + 3}. Noting that xj−2 ∈ N(yi), we conclude that xj−2xj−1xjyixj−2 is
a C4 in G, a contradiction. Hence, (1) is true. By symmetry, we also have

N(yi) ∩ {xi−2, xi−1, xi, xi+1} = {xi, xi+1}, ∀ xi ∈ IC.

This together with (1) and m ≤ 7 implies that

{xi, xi+1} ⊆ NC(yi) ⊆ {xi, xi+1} ∪ ({xi+4} ∩ {xi−3}), ∀ xi ∈ IC.

Hence, yi1, . . . , yit are distinct vertices of V (G)−V (C). Let C ′ be the cycle obtained
from C by replacing ∪
8−m
j=1 {xij xij +1} with ∪
8−m
j=1 {xij yij xij +1}. Then, C ′ is a C8 in G,
a contradiction. Hence, Lemma 2.4 is true. ✷

4

Lemma 2.5 Let G be a graph with δ(G) ≥ 3 and let C := x1x2 . . . xmx1 be a good
hole in G. If G contains neither C4 nor C8 as a subgraph, then for each i ∈ [1, m],
there exists a good path for (C, Xi) with order min {⌊m/2⌋ − 1, 2}, where

Xi :=
 



 {xi, xi+1} if xi ∈ IC
{xi−1, xi} if xi ∈ I +
C \ IC
{xi} if xi /∈ IC ∪ I +
C .

Proof As C is a hole, |Ai| = |N(xi) − {xi−1, xi+1}| ≥ 1. We claim that

NC(u) ⊆ {xi−1, xi, xi+1}, ∀ u ∈ Ai. (2)

By way of contradiction, assume that (2) is false. Then, there exists u ∈ Ai such
that N(u) ∩ (V (C) − {xi−1, xi, xi+1}) contains at least one vertex, say xj. Set
C ′ = xi−→
C xjuxi and C ′′ = xi←−
C xjuxi. Then, C ′ and C ′′ are cycles of length at least
4 in G such that ℓ(C ′) + ℓ(C ′′) = ℓ(C) + 4. By symmetry, we may assume that
ℓ(C ′) ≤ ℓ(C ′′). Then,
 4 ≤ ℓ(C ′) ≤ ℓ(C) + 4
2 < ℓ(C).

By Lemma 2.1, G has a hole C ∗ such that 5 ≤ ℓ(C ∗) ≤ ℓ(C ′) < ℓ(C), a contradiction.
Hence, (2) is true.

Choose u1 ∈ Ai such that

• u1 ∈ Ai ∩ Ai+1 if xi ∈ IC, and

• u1 ∈ Ai−1 ∩ Ai if xi ∈ I +
C \ IC.

If {xi−1, xi+1} ⊆ N(u1), then xi−1xixi+1u1xi−1 is a C4 in G, a contradiction. Hence,
{xi−1, xi+1} ̸⊆ N(u1). This together with (2) and the choice of u1 implies that

NC(u1) = Xi. (3)

It follows from (3) that u1 is a good path for (C, Xi), and hence Lemma 2.5 holds
for m = 5. In the following, we assume that m ≥ 6.

By (3), |N(u1) − V (C)| ≥ d(u1) − 2 ≥ 1, and hence N(u1) − V (C) ̸= ∅. Choose
u2 ∈ N(u1) − V (C) such that

(i) |N(u2) ∩ {xi}| achieves the minimum, and

(ii) subject to (i), |NC(u2)| is as small as possible.

We claim that xi /∈ N(u2). (4)

By way of contradiction, assume that xi ∈ N(u2). Then, by the choice of u2, we have
N(u1)−V (C) ⊆ N(xi). If N(u1)−V (C) contains a vertex u′
2 ̸= u2, then u′
2 ∈ N(xi),

5

 
    
  

  
    

 

PSfrag replacements
 xi

xi+1 xi+2

xi+3

xi+4xi+5
 u1 u2

u′
2

Figure 1: Illustration of the nonexistence of the edge xiu′
2.

and hence u2u1u′
2xiu2 is a C4 in G, a contradiction. Hence, N(u1) − V (C) = {u2}.
As δ(G) ≥ 3, |NC(u1)| ≥ 2. This together with (3) implies that NC(u1) = {xi, xj}
holds for some xj with j ≡ i ± 1 (mod m). Noting that xixj ∈ E(C), we conclude
that xiu2u1xjxi is a C4 in G, a contradiction. Hence, (4) is true.

If NC(u2) = ∅, then by (3), we see that u1u2 is a good path for (C, Xi), which
implies that Lemma 2.5 is true. By way of contradiction, assume that Lemma 2.5
is false, then NC(u2) ̸= ∅. Say xj ∈ NC(u2) for some j ∈ [1, m]. By (4), j ̸= i. Set
D′ = xi−→
C xju2u1xi and D′′ = xi←−
C xju2u1xi. Then, D′ and D′′ are cycles of length
at least 4 in G such that ℓ(D′) + ℓ(D′′) = ℓ(C) + 6. By symmetry, we may assume
that ℓ(D′) ≤ ℓ(D′′). Then,
 4 ≤ ℓ(D′) ≤ ℓ(C) + 6
2 .

By Lemma 2.1, G has a hole C ∗ with 5 ≤ ℓ(C ∗) ≤ ℓ(D′) ≤ ℓ(C)+6
2 ≤ ℓ(C). As C is
a good m-hole, ℓ(C ∗) ≥ ℓ(C), and hence ℓ(C ∗) = ℓ(D′) = ℓ(C) = m = 6, which in
turn means j = i + 3 (mod m). It follows that both D′ and D′′ are 6-holes. Thus,

NC(u1) = {xi} and NC(u2) = {xi+3}. (5)

As δ(G) ≥ 3, u1 has a neighbor u′
2 ∈ V (G) − (V (C) ∪ {u2}). If xi ∈ N(u′
2), then
xiu1u′
2xi is a triangle in G, and hence u1 ∈ ID′ ∩ ID′′ (see Figure 1). This together
with the choice of C implies that IC ̸= ∅. Say xk ∈ IC for some k ∈ [1, 6].

• If xk ∈ {xi, xi+1, xi+2}, then D′ is a 6-hole with ID′ ⊇ {u1, xk};

• if xk ∈ {xi+3, xi+4, xi+5}, then D′′ is a 6-hole with ID′′ ⊇ {u1, xk}.

In each case, we get a contradiction to Lemma 2.4. Hence, xi /∈ N(u′
2). This
together with the choice of u2 implies that NC(u′
2) ̸= ∅. By an argument similar to

6

 
    
  

  
  

PSfrag replacements
 y
x1
 x2 x3
 x4

x5x6

Figure 2: The graph θ(2, 3, 3).

that in the proof of (5), we can derive that NC(u′
2) = {xi+3}. This together with
(5) implies that u1u2xi+3u′
2u1 is a C4 in G, a contradiction. Hence, Lemma 2.5 is
true. ✷

For m ≥ 5, let tm(G) be the minimum non-negative integer t such that every
m-hole of G admits at most t triangulated edges. (If G does not contain any m-hole,
we let tm(G) = 0).

A theta-graph θ(a, b, c), 1 ≤ a ≤ b ≤ c, b ≥ 2, is a simple graph consisting of 3
internally disjoint paths of lengths a, b and c between a pair of vertices of degree 3.
We conclude this section with the following lemma on theta-graphs.

Lemma 2.6 Let G be a P10-free graph with minimum degree at least 3 and let H be
a subgraph of G isomorphic to θ(2, 3, 3). If t5(G) = 0, then G admits a C4 or C8.

Proof By way of contradiction, assume that G contains neither C4 nor C8. Mark
the vertices of H as in Figure 2. Set C ′ := x1x2x3x4yx1 and C ′′ := x4x5x6x1yx4.

As G does not contain C4, both C ′ and C ′′ are 5-holes of G. If H is not any
induced subgraph of G, then xixj ∈ E(G) holds for some integers i, j with i ∈ {2, 3}
and j ∈ {5, 6}. By symmetry, we may assume i = 2. If j = 5, then x2x3x4x5x2 is a
C4 in G; if j = 6, then x1x2 is a triangulated edge in the 5-hole C ′, which implies
t5(G) ≥ 1. Either way leads a contradiction. Hence, H is an induced subgraph of
G.
 Set Yi := N(xi) − V (H), i = 2, 3, 5, 6.

As δ(G) ≥ 3, Yi ̸= ∅, i = 2, 3, 5, 6. Let y2 ∈ Y2. If x1 ∈ N(y2), then x1x2
is a triangulated edge in the 5-hole C ′, a contradiction. Hence, x1 /∈ N(y2).
Likewise, x3 /∈ N(y2). If x5 ∈ N(y2), then x2y2x5x6x1yx4x3x2 is a C8 in G, a

7

 
    
  

  
  
  

 

 
  

 
  

PSfrag replacements
 y
 P

Q

x1

x2 x3
 x4

x5x6
 y2
 y5

y6
 y3

Figure 3: Illustration of the nonexistence of the two H-paths P and Q.

contradiction. Hence, x5 /∈ N(y2). Finally, x4, x6, y /∈ N(y2), since otherwise
x4y2x2x3x4, x6y2x2x1x6 or yy2x2x1y is a C4 in G, a contradiction. Therefore,
N(y2) ∩ V (H) = {x2}. Likewise, we have

N(Yi) ∩ V (H) = {xi}, ∀ i ∈ {2, 3, 5, 6}. (6)

If there exists two H-paths P and Q of length 3 connecting x2, x5 and x3, x6 respec-
tively, say P := x2y2y5x5 and Q := x3y3y6x6, then by (6), we can derive that

N(yi) ∩ V (H) = {xi}, i = 2, 3, 5, 6.

It follows that N(yi) ∩ V (H), i = 2, 3, 5, 6, are distinct subsets of V (H), and hence
y2, y3, y5, y6 are distinct vertices of G − H. Thus, x2y2y5x5x6y6y3x3x2 is a C8 in G
(see Figure 3), a contradiction. By symmetry, we may assume that there exists no
H-(x2, x5)-path of length 3 in G.

If there exists an H-(x2, x5)-path R of length at most 5 in G, then ℓ(R) ∈
{1, 2, 4, 5}, and hence

C ∗ :=
 



 x2x5x4x3x2, if ℓ(R) = 1
x2−→
R x5x6x1yx4x3x2, if ℓ(R) = 2
x2−→
R x5x4yx1x2, if ℓ(R) = 4
x2−→
R x5x6x1x2, if ℓ(R) = 5

is a C4 or C8 in G, a contradiction. Thus,

there exists no H-(x2, x5)-path of length at most 5 in G. (7)

Now, we prove the following claim.

Claim 2.1 For i = 2, 5, G contains a good (H, xi)-path of length 3.

8

 
    
  

  
  
  

   
  

 

PSfrag replacements
 y
x1
 x2 x3
 x4

x5x6
 y2 z2

z′
2
 u2

u′
2

Figure 4: Vertices used in the proof of Claim 2.1.

Proof By symmetry, it suﬃces to show Claim 2.1 for i = 2. Consider any vertex y2
in Y2. By (6), N(y2) ∩ V (H) = {x2}. As δ(G) ≥ 3, y2 has at least two neighbors,
say z2 and z′
2, in V (G) − V (H). We claim that

min {|N(z2) ∩ {x2, x4}|, |N(z′
2) ∩ {x2, x4}|} = 0. (8)

By way of contradiction, assume (8) is false. Then, both z2 and z′
2 has a neighbor
in {x2, x4}. By applying Lemma 2.3 with (u, v, v′, A) := (y2, z2, z′
2, {x2, x4}), we can
derive that EG({z2, z′
2}, {x2, x4}) contains two independent edges. By renaming z2
and z′
2 (if necessary), we may assume that x2 ∈ N(z2) and x4 ∈ N(z′
2). Then,
x2z2y2z′
2x4x5x6x1x2 is a C8 in G, a contradiction. Hence, (8) is true.

By symmetry, we may assume that N(z2) ∩ {x2, x4} = ∅. We claim that

N(z2) ∩ V (H) = ∅. (9)

Otherwise, we have N(z2) ∩ {y, x1, x3, x5, x6} ̸= ∅.

• If y ∈ N(z2), then x2y2z2yx4x5x6x1x2 is a C8 in G;

• if xk ∈ N(z2) for some k ∈ {1, 3}, then x2y2z2xkx2 is a C4 in G;

• if x5 ∈ N(z2), then x2y2z2x5 is an H-path in G contradicting (7);

• if x6 ∈ N(z2), then x2y2z2x6x5x4yx1x2 is a C8 in G.

Thus in all cases, we obtain a contradiction. Hence, (9) is true.

It follows from (9) that N(z2) ∩ (V (H) ∪ {y2}) = {y2}. As δ(G) ≥ 3, z2 has two
neighbors, say u2 and u′
2, in V (G) − (V (H) ∪ {y2}) (see Figure 4). We claim that

min {|N(u2) ∩ {y2, y}|, |N(u′
2) ∩ {y2, y}|} = 0. (10)

9

By way of contradiction, assume (10) is false. Then, both u2 and u′
2 has a neighbor
in {y2, y}. By applying lemma 2.3 with (u, v, v′, A) := (z2, u2, u′
2, {y2, y}), we can
derive that EG({u2, u′
2}, {y2, y}) contains two independent edges. By renaming u2
and u′
2 (if necessary), we may assume that y2 ∈ N(u2) and y ∈ N(u′
2). Then,
x2y2u2z2u′
2yx4x3x2 is a C8 in G, a contradiction. Hence, (10) is true.

By symmetry, we may assume that

N(u2) ∩ {y2, y} = ∅. (11)

If N(u2) ∩ V (H) ̸= ∅, then by (11), we can derive that u2xk ∈ E(G) for some
k ∈ [1, 6]. Set
 D :=
 



 x2y2z2u2x1yx4x3x2, if k = 1
x2y2z2u2x2, if k = 2
x2y2z2u2x3x4yx1x2, if k = 3
x2y2z2u2x4x5x6x1x2, if k = 4
x2y2z2u2x5x4yx1x2, if k = 5
x2y2z2u2x6x5x4x3x2, if k = 6.

Then, D is a C4 or C8 in G, a contradiction. Hence,

N(u2) ∩ V (H) = ∅. (12)

Recall that N(y2) ∩ V (H) = {x2}. By (9), (11) and (12), we see that x2y2z2u2
is a good (H, x2)-path in G. Likewise, G contains a good (H, x5)-path of length 3.
Hence, Claim 2.1 is true. ✷

It follows from Claim 2.1 that for each i = 2, 5, G contains a good good (H, xi)-
path, say xiyiziui, of length 3. Set R2 := y2z2u2 and R5 := y5z5. Then, both R2
and R5 are induced paths of G − V (H), and

EG(V (Ri), V (H)) = {yixi}, i = 2, 5. (13)

If V (R2)∩V (R5) ̸= ∅, then G[V (R2)∪V (R5)] contains a (y2, y5)-path Q of length
at most 3. It follows that x2y2Qy5x5 is an H-(x2, x5)-path of length at most 5 in G,
contrary to (7). Hence, V (R2) ∩ V (R5) = ∅. Similarly, we have

EG(V (R2), V (R5)) ⊆ {u2z5}. (14)

Recall that y2z2u2 and y5z5u5 are induced paths of G − V (H). If u2z5 /∈ E(G), then
by (13) and (14), we can derive that u2z2y2x2x1yx4x5y5z5 is an induced P10 in G, a
contradiction. Hence, u2z5 ∈ E(G). (15)

10

 
    
  

  
  

   

 
  

 
  

 

PSfrag replacements
 y
x1
 x2 x3
 x4

x5x6
 y2 z2

u2
 y5

z5
 y3

y6

Figure 5: An induced P10 in case N(y3) ∩ {y2, z2, y5, z5} = ∅.

For i = 3, 6, let yi ∈ Yi. It follows from (6) that

N(yi) ∩ V (H) = {xi}, i = 3, 6. (16)

This together with (13) implies that y3 ̸= y6 and {y3, y6} ∩ {y2, z2, u2, y5, z5} =
∅. If {y3, y6} ⊆ N(u2), then x3y3u2y6x6x1yx4x3 is a C8 in G, a contradiction.
Hence, {y3, y6} ̸⊆ N(u2). By symmetry, we may assume that y3 /∈ N(u2). If
N(y3) ∩ {y2, z2, y5, z5} = ∅, then by (13), (14), (15) and (16), we can derive that
y3x3x2y2z2u2z5y5x5x6 is an induced P10 in G (see Figure 5), a contradiction. Hence,
N(y3) ∩ {y2, z2, y5, z5} ̸= ∅. Set

D∗ =
 



 x3y3y2x2x3, if y2 ∈ N(y3)
x3y3z2y2x2x1yx4x3, if z2 ∈ N(y3)
x3y3z5y5x5x6x1x2x3, if z5 ∈ N(y3)
x3y3y5x5x4yx1x2x3, if y5 ∈ N(y3).

Then, D∗ is a C4 or C8 in G, a contradiction. This completes the proof of Lemma
2.6. ✷

3 Proof of Theorem 1.1.

Suppose, by contradiction, that G contains neither C4 nor C8. By Lemma 2.2, G
contains a hole of length at least 5. Let C := x1x2 · · · xmx1 be a hole in G such that

(T1) ℓ(C) ≥ 5;

(T2) subject to (T1), ℓ(C) is as small as possible;

(T3) subject to (T1) and (T2), |IC| is as large as possible.

11

Then, C is a good m-hole. Deﬁne Ai, i ∈ [1, m], as that in Section 2. We show some
claims, the ﬁrst one of which is used frequently.

Claim 3.1 Let D be a cycle of G. If 4 ≤ ℓ(D) ≤ ℓ(C), then D is an m-hole and
|ID| ≤ |IC|. As a consequence, there exists no cycle of length k in G with 4 ≤ k < m.

Proof By Lemma 2.1, G[V (D)] contains a hole D∗ with 5 ≤ ℓ(D∗) ≤ ℓ(D) ≤ ℓ(C).
This together with the choice of C implies that D∗ is an m-hole, and hence D = D∗.
By the choice of C, we see that |ID| ≤ |IC|. Hence, Claim 3.1 is true. ✷

Claim 3.2 ℓ(C) ≤ 6.

Proof By way of contradiction, assume that Claim 3.2 is false. Then, m ≥ 7. By
Lemma 2.5, for each i ∈ [1, m], G has a good path, say yizi, for (C, Xi) with order
2, where
 Xi :=
 



 {xi, xi+1} if xi ∈ IC
{xi−1, xi} if xi ∈ I +
C \ IC
{xi} if xi /∈ IC ∪ I +
C .

Then, yi, zi ∈ V (G) − V (C) and

EG({yi, zi}, V (C)) = {yix : x ∈ Xi}, ∀ i ∈ [1, m]. (17)

By reversing the orientation of C (if necessary), we may assume that N(y1)∩V (C) ⊆
{xm, x1}. If m ≥ 9, then by (17), we can derive that z1y1x1x2 . . . x8 is an induced
P10 in G, a contradiction. Thus, m ≤ 8. As G does not contain C8, m = 7.

It follows from Lemma 2.4 that IC = ∅. This together with (17) implies that

EG({yi, zi}, V (C)) = {yixi}, ∀ i ∈ [1, 7]. (18)

It follows that NC(y1), NC(y2), . . . , NC(y7) are distinct subsets of V (C), and hence
y1, y2, . . . , y7 are distinct vertices of G − C. We claim that

{yi, zi} ∩ {yj, zj} = ∅, 1 ≤ i < j ≤ 7. (19)

By way of contradiction, assume that (19) is false for some integers i, j with 1 ≤
i < j ≤ 7. Then, by (18), we can derive that {yi, zi} ∩ {yj, zj} = {zi} ∩ {zj} = {zi}.
Set C ′ := xi−→
C xjyjziyixi and C ′′ := xi←−
C xjyjziyixi. Then, C ′ and C ′′ are cycles in G
of length at least 5 such that

ℓ(C ′) + ℓ(C ′′) = ℓ(C) + 8 = 15. (20)

12

By symmetry, we may assume that ℓ(C ′) ≤ ℓ(C ′′). This together with (20) and
ℓ(C ′′) ̸= 8 implies that ℓ(C ′) ≤ 6 < ℓ(C), contrary to Claim 3.1. Hence, (19) is true.
By an argument similar to that in the proof of (19), we can derive that

EG({yi, zi}, {yj, zj}) ⊆ {zizj}, 1 ≤ i < j ≤ 7. (21)

If z1z3 /∈ E(G), then by (18), (19) and (21), we can derive that

z3y3x3x4x5x6x7x1y1z1z3

is an induced P10 in G, a contradiction. Hence, z1z3 ∈ E(G). Similarly, we have
z3z5, z5z7 ∈ E(G). This together with (19) implies that x1y1z1z3z5z7y7x7x1 is a C8
in G, a contradiction. Hence, Claim 3.2 is true. ✷

Claim 3.3 ℓ(C) ̸= 6.

Proof By way of contradiction, assume that ℓ(C) = 6. By Lemma 2.4, we have
|IC| ≤ 1. By permuting the indices of xi (if necessary), we may assume that IC ⊆
{x1}. By Lemma 2.5, for each i ∈ [1, 6], G has a good path, say yizi, for (C, Xi)
with order 2, where
 Xi :=
 



 {xi, xi+1} if xi ∈ IC
{xi−1, xi} if xi ∈ I +
C \ IC
{xi} if xi /∈ IC ∪ I +
C .

Then, yi, zi /∈ V (C),

EG({y1, z1}, V (C)) = { {y1x1, y1x2}, if IC = {x1}
{y1x1}, if IC = ∅ (22)

and EG({yi, zi}, V (C)) = {yixi}, i ∈ [3, 6]. (23)

It follows from (22) that N(z1) ∩ V (C) = ∅. As δ(G) ≥ 3, z1 has two neighbors, say
u1, u′
1, in V (G) − (V (C) ∪ {y1}). We claim that

min {|N(u1) ∩ {y1, x4}|, |N(u′
1) ∩ {y1, x4}|} = 0. (24)

By way of contradiction, assume (24) is false. Then, both u1 and u′
1 has a neighbor
in {y1, x4}. By applying Lemma 2.3 with (u, v, v′, A) := (z1, u1, u′
1, {y1, x4}), we can
derive that EG({u1, u′
1}, {y1, x4}) contains two independent edges. By renaming u1
and u′
1 (if necessary), we may assume that y1 ∈ N(u1) and x4 ∈ N(u′
1). Then,
x1y1u1z1u′
1x4x5x6x1 is a C8 in G, a contradiction. Hence, (24) is true.

13

By symmetry, we may assume that

N(u1) ∩ {y1, x4} = ∅. (25)

If N(u1) ∩ (V (C) ∪ {y1}) ̸= ∅, then by (25), we see that xi ∈ N(u1) holds for some
i ∈ {1, 2, 3, 5, 6}. If i ∈ {1, 3, 5}, then

C ′ :=
 



 x1y1z1u1x1, if i = 1
x1y1z1u1x3x4x5x6x1, if i = 3
x1y1z1u1x5x4x3x2x1 if i = 5

is a C4 or C8 in G, a contradiction. Hence, i /∈ {1, 3, 5}, which in turn means
i ∈ {2, 6}. It follows that x1y1z1u1xix1 is a C5 in G, contrary to Claim 3.1. Hence,

N(u1) ∩ (V (C) ∪ {y1}) = ∅. (26)

Let i ∈ {1, 3, 5} and deﬁne (xj, yj, zj) := (xj−6, yj−6, zj−6), where j ∈ [7, 12]. It
follows from (22) and (23) that NC(zi) = ∅, and

NC(yi) = { {x1, x2}, if i = 1 and IC = {x1}
{xi}, otherwise.

Thus, {yi, zi} ∩ {yi+2, zi+2} ⊆ {zi} ∩ {zi+2}. If zi = zi+2, then xiyiziyi+2xi+2−→
C xi is
a C8 in G, a contradiction. Hence, zi ̸= zi+2. It follows that

{yi, zi} ∩ {yi+2, zi+2} = ∅, i = 1, 3, 5. (27)

By an argument similar to that in the proof of zi ̸= zi+2, we can derive that
ziyi+2, yizi+2 /∈ E(G). If yiyi+2 ∈ E(G), then xiyiyi+2xi+2xi+1xi is a C5 in G,
contrary to Claim 3.1. Hence, yiyi+2 /∈ E(G). Therefore,

EG({yi, zi}, {yi+2, zi+2}) ⊆ {zizi+2}, i = 1, 3, 5. (28)

We claim that |E(G) ∩ {z1z3, z3z5, z5z1}| ≤ 1. (29)

Otherwise, there exists i ∈ {1, 3, 5} such that {zizi+2, zi+2zi+4} ⊆ E(G). It follows
that xiyizizi+2zi+4yi+4xi+4xi+5xi is a C8 in G, a contradiction. Hence, (29) is true.
Now, we claim that
 EG({yi, zi}, {yi+2, zi+2}) = ∅, i = 1, 3, 5. (30)

By way of contradiction, assume that (30) is false for some integer i ∈ {1, 3, 5}.
Then, by (28) and (29), we may assume that

EG({yj, zj}, {yj+2, zj+2}) = { {zizi+2}, if j = i
∅, if j = i + 2, i + 4.

14

 
    
  

 
 
  
  

 

 

     
    
  

 
 
  
  

 

 

   

   

PSfrag replacements
 xixi
 xi+1xi+1 xi+2xi+2
 xi+3xi+3
 xi+4xi+4 xi+5xi+5
 yiyi zizi
 yi+2yi+2 zi+2zi+2
 yi+4yi+4 zi+4zi+4

IC ̸= {xi+2} IC = {xi+2}

Figure 6: Illustration of the nonexistence of the edge zizi+2.

This together with (22) and (23) implies that

R := { xiyizizi+2yi+2xi+2xi+3xi+4yi+4zi+4, if IC ̸= {xi+2}
zi+4yi+4xi+4xi+5xiyizizi+2yi+2xi+2, if IC = {xi+2}.

is an induced P10 in G (see Figure 6), a contradiction. Hence, (30) is true.

Recall that u1 ∈ N(z1) −(V (C) ∪{y1}). By (30), we can derive that y1, z1, u1, y3,
z3, y5, z5 are distinct vertices of G − C. If u1 /∈ N(y3) ∪ N(z3), then by (22), (23),
(26) and (30), we can derive that z3y3x3x4x5x6x1y1z1u1 is an induced P10 in G, a
contradiction. Hence, u1 ∈ N(y3) ∪ N(z3). (31)

If u1 ∈ N(z3), then x1y1z1u1z3y3x3x2x1 is a C8 in G, a contradiction. Hence,
u1 /∈ N(z3). By combining this with (31), we get u1 ∈ N(y3). This together
with (23) and (26) implies that y3u1 is a good path for (C, X3). Recall that y1z1 is a
good path for (C, X1). By an argument similar to that in the proof of (30), we can
derive that EG({y1, z1}, {y3, u1}) = ∅, contrary to u1 ∈ N(z1). Hence, Claim 3.3 is
true. ✷

It follows from Claims 3.2 and 3.3 that ℓ(C) = 5. In order to complete the
proof of Theorem 1.1, we show some claims about the structure of G − C, where
the indices of xi and Ai are taken modulo 5.

Claim 3.4 Let i, j be two distinct integers in [1, 5] and let P be a (u, v)-path in
G − V (C) with u ∈ Ai and v ∈ Aj. Then

(i) if j ≡ i ± 1 (mod 5), then ℓ(P ) ̸= 1, 2, 5; and

(ii) if j ≡ i ± 2 (mod 5), then ℓ(P ) ̸= 0, 3, 4.

15

Proof By way of contradiction, assume that Claim 3.4 is false. By reversing the
orientation of C (if necessary), we may assume that j = i+1, i+2. Then ℓ(xi−→
C xj) =
j − i and ℓ(xi←−
C xj) = 5 − (j − i). It follows that

C ′ :=
 { xi−→
C xjvP uxi, if (j − i, ℓ(P )) = (1, 1), (1, 5), (2, 0), (2, 4)
xi←−
C xjvP uxi, if (j − i, ℓ(P )) = (1, 2), (2, 3)

is a C4 or C8 in G, a contradiction. Hence, Claim 3.4 is true. ✷

Claim 3.5 Let xi ∈ IC and let P := u1 . . . us, Q := v1 . . . vt be two paths in G − C
such that u1 ∈ Ai ∩ Ai+1 and v1 ∈ Ai+2 ∪ Ai+4.

(i) If s + t ≤ 7, then V (P ) ∩ V (Q) = ∅; and

(ii) if s + t ≤ 6, then EG(V (P ), V (Q)) = ∅.

Proof By way of contradiction, assume that Claim 3.5 is false. Then G[V (P )∪V (Q)]
contains a (u1, v1)-path R of length at most ﬁve with u1 ∈ Ai ∩ Ai+1 and v1 ∈
Ai+2 ∪ Ai+4 such that V (R) ⊆ V (G) − V (C). Note that Ai+4 = Ai−1. We may
assume, by symmetry, that v1 ∈ Ai+2.

• If ℓ(R) ∈ {1, 2, 5}, then by Claim 3.4 (i), we can derive that u1 /∈ Ai+1;

• If ℓ(R) ∈ {0, 3, 4}, then by Claim 3.4 (ii), we have u1 /∈ Ai.

In both cases, we get a contradiction. Hence, Claim 3.5 is true. ✷

An xi-path in G is a path starting from xi. If P is an xi-path in G such that
V (P ) ∩ V (C) = {xi}, then we call P a pendent xi-path for C.

Claim 3.6 Let i ∈ [1, 5] and let P := xiuvw be a pendent xi-path for C. Then
xi−1, xi, xi+1 /∈ N(w).

Proof By way of contradiction, assume that Claim 3.6 is false. Then, w has a
neighbor, say z, in {xi−1, xi, xi+1}. Set

C ′ :=
 



 xiuvwxi−1←−
C xi, if z = xi−1
xiuvwxi, if z = xi
xiuvwxi+1−→
C xi, if z = xi+1.

Then, C ′ is a C4 or C8 in G, a contradiction. Hence, Claim 3.6 is true. ✷

Deﬁnition 3.1 Let w1 . . . wℓ be an induced path of G − C with length 2 or 3. If
there exists an integer i ∈ [1, 5] such that

16

• NC(w1) = {xi, xi+1}, NC(w2) ⊆ {xi+3}, NC(w3) = ∅, and

• NC(w4) ⊆ {xi, xi+1} if ℓ = 4,

then we call xiw1 . . . wℓ a near-good (C, xi)-path of length ℓ.

Claim 3.7 For each xi ∈ IC, there exists a near-good (C, xi)-path.

Proof Let xi ∈ IC. Then, Ai ∩ Ai+1 ̸= ∅. We will ﬁnd a near-good (C, xi)-path
xiyiziuivi step by step.

First, we let yi ∈ Ai ∩ Ai+1. By the proof of Lemma 2.5, we see that yi is a good
(C, {xi, xi+1})-path. Thus, NC(yi) = {xi, xi+1}. (32)

Note that δ(G) ≥ 3. By (32), we have N(yi) − V (C) ̸= ∅. Choose zi ∈ N(yi) −
V (C) such that |NC(zi)| is as small as possible. We claim that

NC(zi) ⊆ {xi+3}. (33)

Otherwise, zixj ∈ E(G) holds for some j ∈ {i − 1, i, i + 1, i + 2}. By symmetry,
we may assume that j ∈ {i + 1, i + 2}. Then, yixj−1 ∈ E(G). It follows that
xj−1yizixjxj−1 is a C4 in G, a contradiction. Hence, (33) is true.

It follows from (33) that N(zi)−(V (C)∪{yi}) = N(zi)−{xi+3, yi}. As δ(G) ≥ 3,
N(zi) − (V (C) ∪ {yi}) ̸= ∅. Among all vertices of N(zi) − (V (C) ∪ {yi}), choose one,
say ui, such that |N(ui) ∩ {xi+3, yi}| achieves the minimum. We claim that

N(ui) ∩ {xi+3, yi} = ∅. (34)

By way of contradiction, assume that (34) is false. We consider two cases.

• N(zi)−(V (C)∪{yi}) = {ui}. As δ(G) ≥ 3, we have NC(zi) ̸= ∅. This together
with (33) implies that NC(zi) = {xi+3}. As (34) is false, N(ui) ∩ {xi+3, yi} ̸=
∅. If N(ui) ⊇ {xi+3, yi}, then yizixi+3uiyi is a C4 in G (see Figure 7), a
contradiction. Hence, |N(ui) ∩ {xi+3, yi}| = 1.

Set C ′ := xiyizixi+3xi+4xi and C ′′ := xi+1xi+2xi+3ziyixi+1. Then, both C ′ and
C ′′ are 5-holes in G. Note that

IC′ = { (IC ∩ {xi+3, xi+4}) ∪ {xi, zi}, if xi+3 ∈ N(ui)
(IC ∩ {xi+3, xi+4}) ∪ {xi, yi}, if yi ∈ N(ui)

and
 IC′′ = { (IC ∩ {xi+1, xi+2}) ∪ {yi, xi+3}, if xi+3 ∈ N(ui)
(IC ∩ {xi+1, xi+2}) ∪ {yi, zi}, if yi ∈ N(ui).

Hence, |IC′| + |IC′′| = |IC| + 3. On the other hand, by the choice of C, we have
|IC| ≥ |IC′|, and hence |IC′′| ≥ 3, contrary to Lemma 2.4.

17

 
  
 
   
  
  
  

PSfrag replacements
 xi
 xi+1
 xi+2

xi+3xi+4
 yi

zi
 ui

Figure 7: Exactly one of xi+3 and yi is a neighbor of ui.

• N(zi) − (V (C) ∪ {yi}) ̸= {ui}. Let u′
i be a vertex of N(zi) − (V (C) ∪ {yi})
with u′
i ̸= ui. As (34) is false, we have

min {|N(ui) ∩ {xi+3, yi}|, |N(u′
i) ∩ {xi+3, yi}|} > 0.

By applying Lemma 2.3 with (u, v, v′, A) := (zi, ui, u′
i, {xi+3, yi}), we see that
EG({ui, u′
i}, {xi+3, yi}) contains two independent edges. By symmetry, we may
assume that uixi+3, u′
iyi ∈ E(G). Then, xiyiu′
iziuixi+3xi+2xi+1xi is a C8 in G,
a contradiction.

In both cases, we get a contradiction. Hence, (34) is true.

Note that both xiyiziui and xi+1yiziui are pendent paths for C with length three.
By Claim 3.6, we can derive that xi−1, xi, xi+1, xi+2 /∈ N(ui). This together with
(34) implies that N(ui) ∩ (V (C) ∪ {yi}) = ∅. (35)

It follows from (35) that |N(ui) − (V (C) ∪ {yi, zi})| = |N(ui) − {zi})| ≥ 2. Let
vi, v′
i be two vertices of N(ui) − (V (C) ∪ {yi, zi}). If vi, v′
i ∈ N(zi), then viziv′
iuivi is
a C4 in G, a contradiction. Hence, {vi, v′
i} ̸⊆ N(zi). By symmetry, we may assume
that vi /∈ N(zi). We claim that

N(vi) ∩ (V (C) ∪ {yi, zi}) ⊆ {xi, xi+1}. (36)

Otherwise, wvi ∈ E(G) holds for some vertex w ∈ {xi+2, xi+3, xi+4, yi}. Set

C ∗ :=
 



 xiyiziuivixi+2xi+3xi+4xi, if w = xi+2
xixi+1yiziuivixi+3xi+4xi, if w = xi+3
xi+1yiziuivixi+4xi+3xi+2xi+1, if w = xi+4
yiziuiviyi, if w = yi.

18
  

 

 

 

 
  
   
  

 

PSfrag replacements
 xi
 xi+1

xi+2xi+3

xi+4
 yi
 ziz′
i e1

e2

Figure 8: The case {e1, e2} = {zixi+2, z′
ixi}.

Then, C ∗ is a C4 or C8 in G, a contradiction. Hence, (36) is true.

It follows from (32),(33),(35) and (36) that xiyiziuivi is a near-good (C, xi)-path.
Hence, Claim 3.7 is true. ✷

Claim 3.8 Let i be an integer in [1, 5] such that xi /∈ IC ∪ I +
C , then there exists a
good (C, xi)-path of length three in G.

Proof It follows from Lemma 2.5 that G contains a good (C, xi)-path, say xiyi, of
length one. As xi /∈ IC ∪ I +
C , EG({yi}, V (C)) = {yixi}. Thus,

NC(yi) = {xi}. (37)

As δ(G) ≥ 3, yi has at least two neighbors, say zi and z′
i, in V (G) − V (C). We claim
that min {|N(zi) ∩ {xi, xi+2, xi+3}|, |N(z′
i) ∩ {xi, xi+2, xi+3}|} = 0. (38)

By way of contradiction, assume that (38) is false. By applying Lemma 2.3 with
(u, v, v′, A) := (yi, zi, z′
i, {xi, xi+2, xi+3}), we see that there exists two independent
edges, say e1 and e2, in EG({zi, z′
i}, {xi, xi+2, xi+3}) such that e1 has an end vertex
in {xi+2, xi+3}. Based on (C, xiyi), zi and z′
i are symmetrical, while xi+2 and xi+3
are symmetrical (see Figure 8). Thus, we may assume that e1 = zixi+2, which in
turn means e2 ∈ {z′
ixi, z′
ixi+3}.

• If e2 = z′
ixi+3, then xi+2ziyiz′
ixi+3xi+4xixi+1xi+2 is a C8 in G, a contradiction.

• If e2 = z′
ixi, set C ′ := xixi+1xi+2ziyixi and C ′′ := xiyizixi+2xi+3xi+4xi. Then,
C ′ is a 5-hole in G with IC′ ⊇ (IC ∩ {xi+1}) ∪ {yi}. By the choice of C, we have
|IC| ≥ |IC′|, and hence IC \{xi+1} ̸= ∅. This together with xi /∈ IC ∪I +
C implies

19
  

 

 

 

   
  
  
   

 

PSfrag replacements
 xi
 xi+1

xi+2xi+3

xi+4 yi

zi
 ui
u′
i f1

f2

Figure 9: The case (f1, f2) = (uixi+2, u′
iyi).

that IC ∩ {xi+2, xi+3} ̸= ∅. Thus, xj ∈ IC holds for some j ∈ {i + 2, i + 3}. It
follows that C ′′ is a C6 in G such that IC′′ ⊇ {xi, xj}. On the other hand, by
Lemma 2.4, we have |IC′′| ≤ 7 − 6, a contradiction.

Therefore, (38) is true.

By symmetry, we may assume that N(zi) ∩ {xi, xi+2, xi+3} = ∅. If NC(zi) ̸= ∅,
then zi has a neighbor, say w, in {xi+1, xi+4}. It follows that xiyiziwxi is a C4 in G,
a contradiction. Hence, NC(zi) = ∅. (39)

It follows from (39) that |N(zi) − (V (C) ∪ {yi})| = d(zi) − 1 ≥ 2. Let ui and u′
i
be two neighbors of zi in V (G) − (V (C) ∪ {yi}). We claim that

min {|N(ui) ∩ {yi, xi+2, xi+3}|, |N(u′
i) ∩ {yi, xi+2, xi+3}|} = 0. (40)

By way of contradiction, assume that (40) is false. By applying Lemma 2.3 with
(u, v, v′, A) := (zi, ui, u′
i, {yi, xi+2, xi+3}), we see that there exists two independent
edges, say f1 and f2, in EG({ui, u′
i}, {yi, xi+2, xi+3}) such that f1 has an end vertex
in {xi+2, xi+3}). Based on (C, xiyizi), ui and u′
i are symmetrical, while xi+2 and xi+3
are symmetrical (see Figure 9). Thus, we may assume that f1 = uixi+2, which in
turn means f2 ∈ {u′
iyi, u′
ixi+3}. It follows that

D′ := { xiyiu′
iziuixi+2xi+3xi+4xi, if f2 = u′
iyi
xi+2uiziu′
ixi+3xi+4xixi+1xi+2, if f2 = u′
ixi+3

is a C8 in G, a contradiction. Hence, (40) is true.

By symmetry, we may assume that N(ui) ∩ {yi, xi+2, xi+3} = ∅. If N(ui) ∩

20

(V (C) ∪ {yi}) ̸= ∅, then ui has a neighbor, say w, in {xi, xi+1, xi+4}. It follows that

D′′ :=
 



 xiyiziuixi, if w = xi
xiyiziuixi+1xi+2xi+3xi+4xi, if w = xi+1
xiyiziuixi+4xi+3xi+2xi+1xi, if w = xi+4

is a C4 or C8 in G, a contradiction. Hence,

N(ui) ∩ (V (C) ∪ {yi}) = ∅. (41)

By (37),(39) and (41), we see that xiyiziui is a good (C, xi)-path of length three in
G. Hence, Claim 3.8 is true. ✷

Claim 3.9 For each xi ∈ IC, there exists a near-good (C, xi)-path xiyiziuivi such
that EG({yi, zi, ui, vi}, V (C)) = {yixi, yixi+1, zixi+3}.

Proof Let xi ∈ IC. By Claim 3.7, G contains a near-good (C, xi)-path, say
xiyiziuivi, of length 4. It follows from Lemma 2.4 that |IC| ≤ 7 − 5, and hence
|IC ∩ {xi+1, xi+2}| + |IC ∩ {xi−1, xi−2}| ≤ 1. By symmetry, we may assume that
IC ∩ {xi+1, xi+2} = ∅. Then, xi+2 /∈ IC ∪ I +
C . By Claim 3.8, G contains a good
(C, xi+2)-path, say xi+2yi+2zi+2ui+2, of length 3. It follows from Deﬁnitions 2.2 and
3.1 that both yiziuivi and yi+2zi+2ui+2 are induced paths of G − C such that

{yixi, yixi+1} ⊆ EG({yi, zi, ui, vi}, V (C)) ⊆ {yixi, yixi+1, zixi+3, vixi, vixi+1} (42)

and EG({yi+2, zi+2, ui+2}, V (C)) = {yi+2xi+2}. (43)

Note that yi ∈ Ai ∩ Ai+1 and yi+2 ∈ Ai+2. By applying Claim 3.5 with P := yiziuivi
and Q := yi+2zi+2ui+2, we have

{yi, zi, ui, vi} ∩ {yi+2, zi+2, ui+2} = ∅ (44)

and EG({yi, zi, ui, vi}, {yi+2, zi+2, ui+2}) ⊆ {viui+2}. (45)

If zixi+3 /∈ E(G), then by (42)-(45), we can derive that

ui+2zi+2yi+2xi+2xi+3xi+4xiyiziui

is an induced P10 in G (see Figure 10), a contradiction. Hence, zixi+3 ∈ E(G). If
Claim 3.9 is not true, then by (42), we can derive that {vixi, vixi+1} ∩ E(G) ̸= ∅.
If vixi ∈ E(G), then xiyixi+1xi+2xi+3ziuivixi is a C8 in G; if vixi+1 ∈ E(G), then
xiyixi+1viuizixi+3xi+4xi is a C8 in G; either way gives a contradiction. Hence, Claim
3.9 is true. ✷

21
  
   
  
 
    

 
 
  

 

 
  

PSfrag replacements
 xi
 xi+1
 xi+2

xi+3xi+4

yi

zi

ui
 vi
 yi+2

zi+2

ui+2

Possible edges of G

Figure 10: Induced P10 in case zixi+3 /∈ E(G).

Claim 3.10 IC = ∅.

Proof It follows from Lemma 2.4 that |IC| ≤ 7−5. If Claim 3.10 is not true, then 1 ≤
|IC| ≤ 2. As |V (C)| = 5, there exists i0 ∈ [1, 5] such that IC ∩ {xi0, xi0+1, xi0+2} =
{xi0}. By permuting the vertices of C (if necessary), we may assume that i0 = 1,
that is IC ∩ {x1, x2, x3} = {x1}. Recall that |IC| ≤ 2. There are following two cases.

• IC = {x1, xk}, where k ∈ {4, 5}. For i = 1, k, Let xiyiziuivi be a near-good
(C, xi)-path satisfying Claim 3.9. Then,

EG({yi, zi, ui, vi}, V (C)) = {yixi, yixi+1, zixi+3}, i = 1, k. (46)

Note that yk ∈ Ak ∩ Ak+1 and y1 ∈ Ak+2. By applying Claim 3.5 with P :=
ykzkukvk and Q := y1z1u1, we can derive that {yk, zk, uk, vk} ∩ {y1, z1, u1} = ∅.
This together with (46) implies that

C ′ = { x1y1z1x4x5y4z4x2x1, if k = 4
x2y1z1x4x3z5y5x1x2, if k = 5

is a C8 in G, a contradiction (see Figure 11).

• IC = {x1}. Let x1y1z1u1v1 be a near-good (C, x1)-path satisfying Claim 3.9.
Then, y1z1u1v1 is an induced path of G − C such that

EG({y1, z1, u1, v1}, V (C)) = {y1x1, y1x2, z1x4}. (47)

Let k be an integer with k ∈ {3, 5}. Then, xk /∈ IC ∪ I +
C . By applying Claim
3.8 with i = k, we obtain a good (C, xk)-path, say xkykzkuk, of length 3 in G.

22

 
  
 
   
  
    

 
      

 
  
  

 

 
    
 
  

 

 

 

 
  

PSfrag replacements
 x1x1
 x2x2
 x3x3
 x4x4 x5x5
 y1
y1
 z1

z1 u1
u1

y4

z4 u4 v4

k = 4 k = 5

y5
 z5

u5

v5

Figure 11: The C8 in case IC = {x1, xk}, k = 4, 5.

It follows from Deﬁnitions 2.2 that ykzkuk is an induced path of G − C such
that EG({yk, zk, uk}, V (C)) = {ykxk}, k = 3, 5. (48)

Note that y1 ∈ A1 ∩ A2 and yk ∈ A1+2 ∪ A1+4. By applying Claim 3.5 with
P := y1z1u1v1 and Q := ykzkuk, we can derive that

{y1, z1, u1, v1} ∩ {yk, zk, uk} = ∅, k = 3, 5 (49)

and EG({y1, z1, u1, v1}, {yk, zk, uk}) ⊆ {v1uk}, k = 3, 5. (50)

It follows from (48) that y3 ̸= y5. Set H35 := G[{y3, z3, u3} ∪ {y5, z5, u5}]. If
H35 is not connected, then by (48), we can derive that

u5z5y5x5x1x2x3y3z3u3

is an induced P10 in G, a contradiction (see Figure 12). Hence,

H35 is a connected subgraph of G − C. (51)

Let Q be a shortest (y3, y5)-path in H. Then, ℓ(Q) ≥ 1. If ℓ(Q) = 1, then
y3y5 ∈ E(G) and x3y3y5x5x1y1z1x4x3 is a C8 in G, a contradiction. Hence,
ℓ(Q) ≥ 2. Set
 R :=
 { x3y3−→
Q y5x5x1y1z1u1v1, if u3, u5 /∈ V (Q)
x3y3−→
Q y5x5x1y1z1u1, otherwise.

23

 
  

 
  

 
  

   

     

   
  

 
  

PSfrag replacements
 x1

x2
 x3
 x4

x5
 y3 z3 u3

y5 z5 u5

y1 z1
 u1

v1
 H35

Figure 12: Induced P10 when H35 is not connected

By (47)-(50), we see that R is an induced path of G. As G is P10-free, ℓ(R) ≤ 8.
This together with ℓ(Q) ≥ 2 implies that ℓ(Q) = 2 and V (Q)∩({u3}∪{u5}) ̸=
∅. Hence, Q = y3u3y5 or Q = y3u5y5, contrary to the fact that both y3z3u3
and y5z5u5 are induced paths of G − C.

In each case, we get a contradiction. Hence, Claim 3.10 is true. ✷

It follows from Claim 3.10 that IC = ∅. Let i be an integer with i ∈ [1, 5]. Then,
xi /∈ IC ∪ I +
C . By Claim 3.8 and Deﬁnition 2.2, we see that G − C contains an
induced path yiziui such that

EG({yi, zi, ui}, V (C)) = {yixi}, i ∈ [1, 5]. (52)

It follows that NC(zi), NC(y1), NC(y2), NC(y3), NC(y4), NC(y5) are distinct subsets
of V (C), and hence zi, y1, y2, y3, y4, y5 are distinct vertices of G − C. Set

Hi := G[{xi, yi, zi} ∪ {xi+2, yi+2, zi+2}], i ∈ [1, 5].

By an analogy similar to that in the proof of (51), we can derive that Hi is a
connected subgraph of G − C. Let Qi be a shortest (yi, yi+2)-path in Hi. Then,
ℓ(Qi) ≥ 1. If ℓ(Qi) = 1, then yiyi+2 ∈ E(G). By (52), we see that G[V (C) ∪
{yi, yi+2}] ∼= θ(2, 3, 3). This together with Lemma 2.6 implies that G admits a C4
or C8, a contradiction. Hence, ℓ(Qi) ≥ 2. By applying Claim 3.4 with (P, j, u, v) :=
(Qi, i + 2, yi, yi+2), we see that ℓ(Qi) ̸= 3, 4. Hence,

ℓ(Qi) ∈ {2, 5}, i ∈ [1, 5]. (53)

24

 

 
  

 
  

 
  

  

 
  
  

 

 
  

PSfrag replacements
 x1

x2
 x3

x4
 x5

y1
 y3

y5y2

y4
 v1
 v3

v5

v2
 v4

Figure 13: The subgraph H of G.

We consider the following two cases.

Case 1. ℓ(Qi) = 5 holds for some i ∈ [1, 5].

By permuting the vertices of C (if necessary), we may assume that ℓ(Q1) = 5.
Then, EG({y1, z1, u1}, {y3, z3, u3}) = {u1u3}. (54)

This together with (52) implies that y1, z1, u1, y3, z3, u3, y4 are distinct vertices of
G − C. If EG({y4}, {y1, z1, u1, y3, z3, u3}) = ∅, then by (52) and (54), we can derive
that y4x4x3y3z3u3u1z1y1x1 is an induced P10 in G, a contradiction. Hence,

EG({y4}, {y1, z1, u1, y3, z3, u3}) ̸= ∅. (55)

On the other hand, by applying (53) with i = 4, we have ℓ(Q4) ∈ {2, 5}, and hence
y4y1 /∈ E(G). This together with (55) implies that y4w ∈ E(G) holds for some
vertex w ∈ {z1, u1, y3, z3, u3}. Set

C ∗ :=
 



 y4z1u1u3z3y3x3x4y4, if w = z1
y4u1z1y1x1x2x3x4y4, if w = u1
y4y3x3x4y4, if w = y3
y4z3y3x3x2x1x5x4y4, if w = z3
y4u3u1z1y1x1x5x4y4, if w = u3

Then, C ∗ is a C4 or C8 in G, a contradiction.

Case 2. ℓ(Qi) = 2 for all i ∈ [1, 5].

For i ∈ [1, 5], let Qi := yiviyi+2. Then, vi ∈ {zi, zi+2}. This together with (52)
implies that EG({yi, vi}, V (C)) = {yixi}, i ∈ [1, 5]. (56)

25

It follows from (56) that for each i ∈ [1, 5]

y1, y2, y3, y4, y5, vi are distinct vertices of G − C. (57)

We claim that for all i ∈ [1, 5]

N(vi) ∩ {y1, y2, y3, y4, y5} = {yi, yi+2}, (58)

where y6 := y1 and y7 := y2. By way of contradiction, assume that (58) is false.
Then, viyj ∈ E(G) holds for some j ∈ {i+1, i+3, i+4}. Set k := j if j ∈ {i+1, i+4},
and k := j − 1 if j = i + 3. Then, xkykviyk+1xk+1 is a C-path in G. This together
with (57) implies that xkykviyk+1xk+1−→
C xk is a C8 in G, a contradiction. Hence, (58)
is true.

It follows from (57) and (58) that y1, y2, y3, y4, y5, v1, v2, v3, v4, v5 are distinct ver-
tices of G − C, and hence the graph H, depicted in Figure 13, is a subgraph of G.
We claim that

G[{x1, x2, x3, x4, x5, y1, y2, y3, y4, y5, v1, v2, v3, v4, v5}] ∼= H. (59)

By way of contradiction, assume that (59) is false. Then, by (56) and (58), we can
derive that one of {y1, y2, y3, y4, y5} and {v1, v2, v3, v4, v5} is not independent in G.
And hence there exists a pair of integers (i, j) with i ∈ [1, 5] and j ∈ {i + 1, i + 2}
such that {yiyj, vivj} ∩ E(G) ̸= ∅. By symmetry, we may assume that i = 1 and
j ∈ {2, 3}. Then, G admits an edge e
∗ in {y1y2, y1y3, v1v2, v1v3}. Deﬁne

D∗ :=
 



 y1y2x2x1y1, if e
∗ = y1y2
y1y3x3x2y2v2y4v4y1, if e
∗ = y1y3
v1v2y2v5y5x5x1y1v1, if e
∗ = v1v2
v1v3y3x3x4x5x1y1v1, if e
∗ = v1v3.

Then, D∗ is a C4 or C8 in G, a contradiction. Hence, (59) is true.

It follows from (59) that x1y1v1y3v3y5v5y2v2y4 is an induced P10 in G, a contra-
diction. This completes the proof of Theorem 1.1. ✷

References

[1] D. Daniel, S. E. Shauger, A result on the Erd˝os-Gy´arf´as conjecture in planar
graphs, Congr. vol. 153 (2001) 129-139.

[2] P. Erd˝os, Some old and new problems in various branches of combinatorics,
Discrete Math. 165/166 (1997) 227-231.

26

[3] Y. Gao, S. Shan, Erd˝os-Gy´arf´as conjecture for P8-free graphs, Graphs Combin.
168 (2022).

[4] M. H. Ghaﬀari, Z. Mostaghim, Erd˝os-Gy´arf´as conjecture for some families of
Cayley graphs, Aequ. Math. 92(1) (2018) 1-6.

[5] M. Ghasemi, R. Varmazyar, On the Erd˝os-Gy´arf´as conjecture for some Cayley
graphs, Matematichki Vesnik 73(1) (2021) 37-42.

[6] C. C. Heckman, R. Krakovski, Erd˝os-Gy´arf´as conjecture for cubic planar
graphs, Electron. J. Comb. 20(2) (2013) 7-43.

[7] H. Liu, R. Montgomery, A solution to Erd˝os and Hajnal’s odd cycle problem,
J. Amer. Math. Soc. 36 (2023), 1191-1234.

[8] K. Markstr¨om, Extremal graphs for some problems on cycles in graphs, Congr.
Numer. 171 (2004) 179-192.

[9] P. S. Nowbandegani, H. Esfandiari, M.H. Shirdareh Haghighi, K. Bibak, On the
Erd˝os-Gy´arf´as conjecture in claw-free graphs, Discuss. Math. Graph Theory.
34(3) (2014), 635-640.

[10] P. S. Nowbandegani, H. Esfandiari, An experimental result on the Erd˝os-
Gy´arf´as conjecture in bipartite graphs, 14th Workshop on Graph Theory CID,
September 2011, 18-23, Szklarska Por¸eba, Poland.

[11] S. E. Shauger, Results on the Erd˝os-Gy´arf´as conjecture in K1,m-free graphs,
Congr. Numer. 134 (1998) 61-65.
 27
