<!-- source: https://arxiv.org/pdf/2011.11935 | converted from PDF -->

arXiv:2011.11935v1  [math.CO]  24 Nov 2020
Recent progress on graphs with ﬁxed smallest

eigenvalue

Jack H. Koolen
a,b, Meng-Yue Caoc, and Qianqian Yang∗a

aSchool of Mathematical Sciences, University of Science and Technology of China, 96 Jinzhai Road, Hefei, 230026,

Anhui, PR China.

bCAS Wu Wen-Tsun Key Laboratory of Mathematics, University of Science and Technology of China, 96 Jinzhai

Road, Hefei, Anhui, 230026, PR China

cSchool of Mathematical Sciences, Beijing Normal University, 19 Xinjiekouwai Street, Beijing, 100875, PR China.

November 25, 2020

Abstract

We give a survey on graphs with ﬁxed smallest eigenvalue, especially on graphs with large

minimal valency and also on graphs with good structures. Our survey mainly consists of the

following two parts:

(i) Hoﬀman graphs, the basic theory related to Hoﬀman graphs and the applications of

Hoﬀman graphs to graphs with ﬁxed smallest eigenvalue and large minimal valency;

(ii) recent results on distance-regular graphs and co-edge regular graphs with ﬁxed smallest

eigenvalue and the characterizations of certain families of distance-regular graphs.

At the end of the survey, we also discuss signed graphs with ﬁxed smallest eigenvalue and

present some new ﬁndings.

1 Introduction

All graphs mentioned in this paper are ﬁnite, undirected and simple. For undeﬁned notations

see [13], [35] and [43]. Unless we specify a diﬀerent matrix, by an eigenvalue of a graph, we mean

∗Corresponding author.
2010 Mathematics Subject Classiﬁcation. Primary 05C50. Secondary 05C22, 05C75, 05E30, 05D99, 11H06.
E-mail addresses: koolen@ustc.edu.cn (J.H. Koolen), cmy1325@163.com (M.-Y. Cao), qqyang91@ustc.edu.cn

(Q. Yang).
 1

an eigenvalue of its adjacency matrix. Note that as the adjacency matrix of a graph is a symmetric

real matrix, it is diagonalizable and all its eigenvalues are real.

In this paper, we mainly study the smallest eigenvalue of a graph. One of the oldest results

is that for a connected graph, its smallest eigenvalue is in absolute value at most the largest

eigenvalue and equality holds if and only if this graph is bipartite (see [13, Proposition 3.1.1,

Proposition 3.4.1]). This is a consequence of the Perron-Frobenius Theorem.

An important result by Hoﬀman gives a bound on the stability number α of a k-regular graph

G with order n and smallest eigenvalue λmin(G) as follows:

α ≤ n
1 + k
−λmin(G)

(unpublished; see [13, Theorem 3.5.2]). We call this bound the Hoﬀman bound or the ratio bound.

This bound has many applications, for example in extremal combinatorics. Godsil and Meagher

[42] used this bound to show many Erd˝os-Ko-Rado theorems. This bound also gives a lower bound

on the chromatic number χ of G, that is χ ≥ 1 + k
−λmin(G) , as each color class of G is a stable set.

Recently, Bramoull´e, Kranton and D’Amours [11] have shown that the equilibria of many

economic systems only depend on the smallest eigenvalue of the underlying network.

The main topic of this paper is to survey the area of graphs with ﬁxed smallest eigenvalue.

In Section 2, we describe the classical 1976 result of Cameron, Goethals, Seidel and Shult [15]

characterizing graphs with smallest eigenvalue at least −2 and the corresponding 2018 result of

Koolen, Yang and Yang [62] for graphs with smallest eigenvalue at least −3. Also in this section,

we present two classical results of Hoﬀman and related results by Woo and Neumaier [94], Yu [97]

and Aharoni, Alon and Berger [1]. The ﬁrst result of Hoﬀman [49] shows the following: Let G

be a graph with smallest eigenvalue λmin(G) and large minimal valency. If λmin(G) > −2, then

λmin(G) = −1 and G is a disjoint union of cliques; if λmin(G) > −1 − √2, then λmin(G) = −2

and G is a generalized line graph. The second result of Hoﬀman [48] shows that the smallest

eigenvalue of a graph depends very much on its local structure. For recent surveys on graphs

with smallest eigenvalue at least −2, we refer to Cvetkovi´c, Rowlinson and Simi´c [33] and [34]. In

Section 3, we deﬁne Hoﬀman graphs and present the basic theory of Hoﬀman graphs. In Section 4,

we investigate graphs with bounded smallest eigenvalue and large minimal valency. In Section 5 we

discuss distance-regular graphs. We look at distance-regular graphs with ﬁxed smallest eigenvalue

and also at characterizations of certain families of distance-regular graphs. In Section 6 we discuss

co-edge regular graphs. In Section 7 we explore signed graphs and Seidel matrices. In Section 8,

we give several problems on unsigned and signed graphs. In Appendix A, we deﬁne Q-polynomial

distance-regular graphs and their Terwilliger algebra.

Note that if a regular graph G has smallest eigenvalue λmin(G), then its complement G is also

2

regular with second largest eigenvalue −λmin(G) − 1. Henceforth we scratch the area of regular

graphs with ﬁxed second largest eigenvalue.

1.1 Regular graphs with ﬁxed second largest eigenvalue

There is a tremendous amount of literature about regular graphs with ﬁxed second largest

eigenvalue. In this subsection, we give some highlights of this area, but we do not intend to survey

the area. One of the reasons is that the area has quite a bit of diﬀerent ﬂavors from the rest of

this paper, and another is that there is so much literature that probably will make a small book.

We follow [13, Chapter 4]. For more details, see also that chapter.

An expander is a (preferably sparse) graph with the property that the number of vertices at

distance at most 1 from any given (not too large) set S of vertices is at least a ﬁxed constant (> 1)

times the size of S. Expanders became famous, because of their role in sorting networks (cf. Ajtai,

Koml´os and Szemer´edi [2]). For a recent survey on expanders, see [51].

Let G be a connected k-regular graph with distinct eigenvalues k > λ1 > · · · > λt. Let

λ := max{λ1, −λt}. It is shown in [13, Proposition 4.3.1, Proposition 4.5.1], also in [4], that if

the ratio k
λ is larger, then the expansion properties of G are better. Also if the ratio k
λ is large,

then the graph has good connectivity and randomness properties. For a survey on pseudo-random

graphs, that is, graphs with good randomness properties, see [66].

A theorem by Alon and Boppana shows that the second largest eigenvalue of a k-regular graph

can not be much smaller than 2
√k − 1.

Theorem 1.1 ( [3, Alon-Boppana]). Let k ≥ 3 be an integer. There exists a positive constant C

such that the second largest eigenvalue λ1 of a k-regular graph of order n satisﬁes

λ1 ≥ √
k − 1(1 − C ln (k − 1)
ln n ).

Serre [80] has shown that for a k-regular graph, many of its eigenvalues are not much smaller

than 2
√k − 1.

Theorem 1.2. Fix k ≥ 1. For each ε > 0, there exists a positive constant c = c(k, ε) such that

for any k-regular graph G of order n, the number of eigenvalues larger than (2 − ε)
√k − 1 is at

least cn.

There are many improvements and generalizations of the above two theorems with applications

to coding theory and other areas, see for example [30], [50] and [69].

Alon [3] conjectured that for ﬁxed k, ε > 0 and n suﬃciently large, a random k-regular graph

of order n has second largest eigenvalue at most 2
√k − 1 + ε. This conjecture was shown to be

true by Friedman [36].
 3

These results show that the above mentioned ratio k
λ can not be much larger than k
2
√k−1. This

leads us to deﬁne Ramanujan graphs. A Ramanujan graph is a connected k-regular graph such that

any eigenvalue λ ̸= ±k satisﬁes |λ| ≤ 2
√k − 1. Complete graphs are Ramanujan graphs. Note that

a sparse non-bipartite Ramanujan graph is a particular good expander. It is of very great interest

to construct inﬁnite families of Ramanujan graphs with ﬁxed valency k and unbounded number

of vertices. There are several constructions known of inﬁnite families of non-bipartite Ramanujan

graphs, for example, by Lubotzky, Phillips and Sarnak [70], Margulis [72] and Morgenstern [75],

but they are only known for particular k. Recently, Marcus, Spielman and Srivastava [71] found

for every k ≥ 3 an inﬁnite family of bipartite Ramanujan graphs with valency k and unbounded

number of vertices. It still remains an open problem to construct inﬁnite families of non-bipartite

k-regular Ramanujan graphs for all of k ≥ 3.

2 An overview of the main results

In this section, we give an overview of the main results in the area of graphs with ﬁxed smallest

eigenvalue. At the beginning of this section, we introduce some basic terminology.

Let G be a graph with vertex set V (G) and edge set E(G) ⊆ (V (G)
2 ), where V (G) is a ﬁnite

set. If {x, y} is in E(G), then we say that x and y are neighbors or x and y are adjacent and write

x ∼ y in this case. We say that a vertex x is incident with an edge e if x ∈ e.

The adjacency matrix A(G) of a graph G is the square (0, 1)-matrix with rows and columns

are indexed by V (G), such that the (x, y)-entry of A(G) is 1 if and only if x and y are adjacent.

As A(G) is a symmetric matrix, all its eigenvalues are real. The eigenvalues of G are just the

eigenvalues of A(G). We call the multiset of eigenvalues of G with their multiplicities the spectrum

of G. We call two graphs cospectral if they have the same spectrum. In this paper, we are mainly

interested in the smallest eigenvalue of G, which is denoted by λmin(G).

2.1 s-Integrability of graphs

Let Σ be a ﬁnite set of vectors in Rn. The lattice Λ generated by Σ is deﬁned as

Λ :=
 {∑

v∈Σ αvv | αv ∈ Z for all v ∈ Σ
}
 ,

and denoted by ⟨Σ⟩Z. The lattice Λ is called integral, if the standard inner product (v1, v2) is

integral for all v1, v2 ∈ Σ. Let Gr(Σ) be the matrix with rows and columns are indexed by the set

Σ, such that the (v1, v2)-entry of Gr(Σ) is (v1, v2). Note that the lattice Λ is integral if and only

if the matrix Gr(Σ) is an integral matrix.

Following Conway and Sloane [31], we say that an integral lattice Λ is s-integrable (for some

positive integer s) if √
sΛ is a sublattice of a standard lattice, which is a lattice generated by a set

4

of orthonormal vectors. This is equivalent with the condition that sGr(Σ) = N T N holds for some

integral matrix N .

Let G be a graph with A(G) as its adjacency matrix. Then the matrix B(G) := A(G) +

⌈−λmin(G)⌉I is positive semideﬁnite and hence can be written as B(G) = M T M for some real

matrix M . Denote by Λ(G) the lattice generated by the columns of M . Note that the isomorphism

class of Λ(G) only depends on B(G), not on M . For a positive integer s, we say that the graph

G is s-integrable if the lattice Λ(G) is s-integrable, or equivalently, sB(G) = N T N holds for some

integral matrix N . Note that if a graph G is s-integrable and t-integrable, then G is (s + t)-

integrable. So a 1-integrable graph is s-integrable for s ≥ 1.

In 1976, Cameron et al. [15] showed the following result:

Theorem 2.1 (cf. [15, Theorem 4.3, Theorem 4.10]). If G is a connected graph with λmin(G) ≥ −2,

then G is s-integrable for any s ≥ 2. Moreover, if G has at least 37 vertices, then G is 1-integrable.

A graph is a generalized line graph if it is 1-integrable with smallest eigenvalue at least −2.

Let G be a graph. The line graph of G, denoted by L(G), is the graph with vertex set E(G) such

that edges e and f are adjacent in L(G) if there is a unique vertex x incident with e and f in G.

Let N be the |V (G)| × |E(G)| (0, 1)-matrix whose (x, e)-entry equals 1 if and only if the vertex

x is incident with the edge e. Then A(L(G)) + 2I = N T N . This means that L(G) has smallest

eigenvalue at least −2 and is 1-integrable. But for a generalized line graph H, if an integral matrix

N ′ satisﬁes A(H) + 2I = (N ′)T N ′, then N ′ is a (0, ±1)-matrix.

For more about graphs with smallest eigenvalue at least −2, we refer to [33] and [34].

Later in 2018, Koolen et al. [62] studied the integrability of graphs with smallest eigenvalue at

least −3 and proved that:

Theorem 2.2 (cf. [62, Theorem 1.3]). There exists a positive constant κ1 such that, if G is a

graph with λmin(G) ≥ −3 and minimal valency at least κ1, then G is s-integrable for any s ≥ 2.

To prove the above theorem, they use Hoﬀman graphs as their main tool, which will be intro-

duced in the next section.

Remark 2.3. (i) After Theorem 4.8, we give a sketch of the proof of Theorem 2.2.

(ii) It is known that κ1 is at least 166 by results of Koolen and Munemasa [59] and Koolen,

Rehman and Yang [61].

2.2 Two results of Hoﬀman

Hoﬀman [49] in 1977 showed the following related results.

5

Theorem 2.4 (cf. [49, Theorem 1.1]). (i) For any real number λ ∈ (−2, −1], there exists a

constant C1(λ) such that, if G is a graph with λmin(G) ≥ λ and minimal valency at least

C1(λ), then λmin(G) = −1 and G is a disjoint union of cliques.

(ii) For any real number λ ∈ (−1 − √2, −2], there exists a constant C1(λ) such that, if G is a

graph with λmin(G) ≥ λ and minimal valency at least C1(λ), then λmin(G) ≥ −2 and G is a

generalized line graph and hence is 1-integrable.

The second item of this theorem can be reformulated as follows:

Theorem 2.5 (cf. [12, Theorem 3.12.5]). Let ˆθk be the supremum of the smallest eigenvalues of

graphs with minimal valency at least k and smallest eigenvalue less than −2. Then {ˆθk}∞
k=1 forms

a monotone decreasing sequence with limit −1 − √2.

Following the ideas of Hoﬀman, Woo and Neumaier [94] in 1995 showed that

Theorem 2.6 (cf. [94, Theorem 5.1]). For any real number λ ∈ (α1, −1−√
2], where α1 ≈ −2.4812

is the smallest root of the polynomial x3 + 2x2 − 2x − 2, there exists a positive constant C1(λ) such

that, if G is a graph with λmin(G) ≥ λ and minimal valency at least C1(λ), then λmin(G) ≥ −1−√2.

This theorem can also be reformulated as follows:

Theorem 2.7 ( [97, Theorem 1.3]). Let ˆσk be the supremum of the smallest eigenvalues of graphs

with minimal valency at least k and smallest eigenvalue less than −1 − √
2. Then {ˆσk}∞
k=1 forms a

monotone decreasing sequence with limit α1, the smallest root of the polynomial x3 + 2x2 − 2x − 2.

Remark 2.8. (i) Bussemaker and Neumaier [14] showed that ˆθ1 is the smallest eigenvalue of

the graph E10 (for a picture see below) and this graph is the unique connected graph with

ˆθ1 as its smallest eigenvalue, which is approximately −2.006594, the smallest root of the

polynomial x2(x2 − 1)2(x2 − 3)(x2 − 4) − 1.

E10

(ii) Let ˆηk be the supremum of the smallest eigenvalues of k-regular graphs with smallest eigen-

value less than −2. Then the limit of the sequence {ˆηk}∞
k=1 is −1 − √2 (see [97]).

(iii) Yu [97] also showed that ˆη3 is the smallest eigenvalue of the Yu-graph (for a picture see below)

and this graph is the unique connected 3-regular graph with ˆη3 as its smallest eigenvalue,

which is approximately −2.0391, the smallest root of the polynomial x6 − 3x5 − 7x4 + 21x3 +

13x2 − 35x − 4.
 6

Yu-graph

(iv) Let ˆξk be the supremum of the smallest eigenvalues of k-regular graphs with smallest eigen-

value less than −1 − √
2. Then the limit of the sequence {ξk}∞
k=1 is α1 (see [97]).

Now we look at graphs with a bounded smallest eigenvalue. In order to state the results we

need to introduce the graph ̃K2t. Let t be a positive integer. Denote by ̃K2t the graph with 2t + 1

vertices consisting of a clique K2t together with a vertex that is adjacent to exactly t vertices of

the clique. Note that the smallest eigenvalue of ̃K2t goes to −∞ as t goes to ∞. (For a proof,

see [95, Lemma 3.2].) It is fairly easy to see that the smallest eigenvalue of the t-claw K1,t also

goes to −∞ as t goes to ∞, as λmin(K1,t) = −√
t.

Hoﬀman [48] in 1973 showed the following results:

Theorem 2.9 ( [48, p. 278]). (i) Let λ be a positive real number. Then there exists a positive

integer T = T (λ) such that, if G is a graph with λmin(G) ≥ −λ, then G contains neither

K1,T nor ̃K2T as an induced subgraph.

(ii) Let t ≥ 3 be a positive integer. Then there exists a positive constant λ = λ(t) such that, if a

graph G does not contain K1,t and ̃K2t, then λmin(G) ≥ −λ.

This theorem shows that the smallest eigenvalue of a graph is quite dependent on the local

information.

A related result is obtained by Aharoni et al. [1]. Before we state their result we need to

introduce the Laplacian matrix. For a graph G on n vertices, deﬁne its Laplacian matrix L(G)

as follows: L(G) = ∆(G) − A(G), where ∆(G) is the diagonal matrix with ∆(G)x,x = kG(x), the

valency of x in G, and A(G) is the adjacency matrix of G. They obtained the following result:

Theorem 2.10 ( [1, Theorem 1.1]). Let G be a graph with maximal valency k containing no

induced K1,ℓ’s. Let t(k, ℓ) denote the minimum possible number of edges of a graph on k vertices

with no stable set of size ℓ. If θ is the maximal eigenvalue of the Laplacian matrix of G, then

θ ≤ 2k − t(k,ℓ)
k−1 .

It is known by Tur´an’s Theorem that t(k, ℓ) = (1 + o(1)) k2
2ℓ−2 , where the o(1)-term tends to

zero as k tends to inﬁnity.

For regular graphs, we obtain the following corollary:

Corollary 2.11. Let G be a k-regular graph containing no induced K1,ℓ’s. Then λmin(G) ≥

−(1 + o(1)) 2ℓ−3
2ℓ−2 k.
 7

Proof . This follows from Theorem 2.10 immediately.

It is not clear whether the lower bound in Corollary 2.11 is the best bound on the smallest

eigenvalue of regular graphs. Here, given an integer ℓ ≥ 2 and a connected bipartite (ℓ − 1)-

regular graph G′, we are able to construct an inﬁnite family of regular graphs {G1, G2, . . . , Gs, . . .}

satisfying

(i) Gs is ks-regular and does not contain induced K1,ℓ’s, for s = 1, 2, . . .;

(ii) ks → ∞, as s → ∞;

(iii) lims→∞ λmin(Gs)
ks = − ℓ−2
ℓ .

For this, we need to introduce the clique extension of a given graph. For a positive integer s

and a graph H, the s-clique extension of H is the graph ̃H obtained from H by replacing each

vertex x ∈ V (H) by a clique ̃X with s vertices, such that ˜x ∼ ˜y (for ˜x ∈ ̃X, ˜y ∈ ̃Y , ̃X ̸= ̃Y ) in ̃H

if and only if x ∼ y in H. In particular, if H has spectrum

{λ
m0
0 , λ
m1
1 , . . . , λmt
t } , (1)

then ̃H has spectrum

{(s(λ0 + 1) − 1)
m0 , (s(λ1 + 1) − 1)
m1 , . . . , (s(λt + 1) − 1)
mt , (−1)
(m0+m1+···+mt)} (2)

(see [47, p. 107]).

Now we start our construction. For each s, let Gs be the s-clique extension of G′. Then Gs is

regular with valency ks := ℓs − 1 and with smallest eigenvalue λmin(Gs) := −ℓs + 2s − 1. It is not

hard to check that these graphs Gs’s satisfy the above properties.

Let λℓ,k := inf {λmin(G) | G is k-regular and does not contain induced K1,ℓ’s} be a real number.

Consider
 τℓ := inf { λℓ,k
k | k = 3, 4, . . .} .

Corollary 2.10 and the above examples we constructed imply − 2ℓ−3
2ℓ−2 ≤ τℓ ≤ − ℓ−2
ℓ .

Problem 2.12. Determine τℓ for all ℓ ≥ 3.

For the particular case where ℓ = 3, Cioab˘a, Elzinga and Gregory [28, Theorem 4.5] proved

λ3,3 ≥ θ ≈ −2.272, where θ is the smallest root of the polynomial x3 + x + 14. Furthermore, for

graphs containing no induced K1,3’s, that is, claw-free graphs, Chudnovsky and Seymour [20–27],

developed a structure theory. This may help to determine τ2.

8

3 Hoﬀman graphs

We describe now two methods used to study graphs with ﬁxed smallest eigenvalues. The ﬁrst

technique is the so-called Bose-Laskar method. In this method, they use the fact that if a graph

does not contain induced t-claws with large t, then this graph must contain large cliques. This

method works best if there is some local regularity in the graph. The second method is to use

Hoﬀman graphs as a tool, which was introduced by Woo and Neumaier [94], following ideas of

Hoﬀman. This method gives more precise local information of a graph than the Bose-Laskar

method, but the disadvantage of this method is that we need to assume that the minimal valency

of graphs is very large, as we need Ramsey theory to show the existence of large cliques. In this

section we discuss Hoﬀman graphs and give the basic theory for them.

Deﬁnition 3.1 (Hoﬀman graph). A Hoﬀman graph h is a pair (H, ℓ), where H = (V, E) is a graph

and ℓ : V → {f, s} is a labeling map satisfying the following conditions:

(i) vertices with label f are pairwise non-adjacent,

(ii) every vertex with label f is adjacent to at least one vertex with label s.

We call a vertex with label s a slim vertex, and a vertex with label f a fat vertex. We denote

by Vslim(h) (resp. Vfat(h)) the set of slim (resp. fat) vertices of h.

For a vertex x of h, we deﬁne N s
h (x) (resp. N f
h (x)) the set of slim (resp. fat) neighbors of x in

h. If every slim vertex of h has a fat neighbor, then we call h fat, and if every slim vertex of h has

at least t fat neighbors, we call h t-fat. In a similar fashion, we deﬁne N f
h (x1, x2) to be the set of

common fat neighbors of two slim vertices x1 and x2 in h and N s
h (f1, f2) to be the set of common

slim neighbors of two fat vertices f1 and f2 in h.

The slim graph of the Hoﬀman graph h is the subgraph of H induced on Vslim(h). Note that

any graph can be considered as a Hoﬀman graph with only slim vertices, and vice versa. We will

not distinguish between Hoﬀman graphs with only slim vertices and graphs.

A Hoﬀman graph h1 = (H1, ℓ1) is called an (proper ) induced Hoﬀman subgraph of h = (H, ℓ),

if H1 is an (proper) induced subgraph of H and ℓ1(x) = ℓ(x) holds for all vertices x of H1.

Let W be a subset of Vslim(h). An induced Hoﬀman subgraph of h generated by W , denoted

by ⟨W ⟩h, is the Hoﬀman subgraph of h induced on W ∪ {f ∈ Vfat(h) | f ∼ w for some w ∈ W }.

For a fat vertex f of h, a quasi-clique (with respect to f ) is a subgraph of the slim graph of h

induced on the slim vertices adjacent to f in h, and we denote it by Qh(f ).

Deﬁnition 3.2 (isomorphism of Hoﬀman graphs). Two Hoﬀman graphs h = (H, ℓ) and h′ =

(H ′, ℓ′) are isomorphic if there exists an isomorphism from H to H ′ which preserves the labeling.

9

Deﬁnition 3.3 (strong isomorphism of Hoﬀman graphs). Two Hoﬀman graphs h = (H, ℓ) and

h′ = (H ′, ℓ′) are strongly isomorphic if they have the same set of slim vertices and there exists an

isomorphism from h to h′ which ﬁxes the set of slim vertices vertex-wise.

Note that if two Hoﬀman graphs are strongly isomorphic, then they have the same slim graph.

Deﬁnition 3.4 (special matrix). For a Hoﬀman graph h = (H, ℓ), there exists a matrix C such

that the adjacency matrix A of H satisﬁes

A =
 

 As C

C T O
 

 ,

where As is the adjacency matrix of the slim graph of h. The special matrix Sp(h) of h is the real

symmetric matrix As − CC T .

The eigenvalues of h are the eigenvalues of its special matrix Sp(h), and the smallest eigenvalue

of h is denoted by λmin(h). Note that h is not determined by its special matrix in general, since

diﬀerent h’s may have the same special matrix. Observe also that if there are no fat vertices in h,

then Sp(h) = As is just the standard adjacency matrix.

Lemma 3.5 ( [94, Lemma 3.4]). Let h be a Hoﬀman graph and let xi and xj be two distinct slim

vertices of h. The special matrix Sp(h) has diagonal entries

Sp(h)xi,xi = −|N f
h (xi)|

and oﬀ-diagonal entries
 Sp(h)xi,xj = (As)xi,xj − |N f
h (xi, xj)|.

For the smallest eigenvalues of Hoﬀman graphs and their induced Hoﬀman subgraphs, Woo

and Neumaier showed the following inequality.

Lemma 3.6 ( [94, Corollary 3.3]). If h1 is an induced Hoﬀman subgraph of a Hoﬀman graph h,

then λmin(h1) ≥ λmin(h) holds.

As a corollary of Lemma 3.6, we have:

Lemma 3.7. If G1 is an induced subgraph of G, then λmin(G1) ≥ λmin(G) holds.

Deﬁnition 3.8 (µ-saturated Hoﬀman graph). Let µ ≤ −1 be a real number and let h be a Hoﬀman

graph with smallest eigenvalue at least µ. Then h is µ-saturated if no fat vertex can be attached

to h in such a way that the resulting Hoﬀman graph has smallest eigenvalue at least µ.

10

Now we introduce a result of Hoﬀman and Ostrowski. In order to state this, we need to

introduce the following notations. Suppose h is a Hoﬀman graph and {f1, . . . , fr} is a subset

of Vfat(h). Let gn1,...,nr (h) be the Hoﬀman graph obtained from h by replacing the fat vertex fi

by a slim ni-clique K fi, and joining all the neighbors of fi (in h) with all the vertices of K fi

for all i. We will write G(h, n) for the graph gn1,...,nr (h), when Vfat(h) = {f1, f2, . . . , fr} and

n1 = n2 = · · · = nr = n. With the above notations, we can now state the result of Hoﬀman and

Ostrowski. For a proof of it, see [52, Theorem 2.14].

Theorem 3.9. Suppose h is a Hoﬀman graph with fat vertices f1, f2, . . . , fr.Then

λmin(gn1,...,nr (h)) ≥ λmin(h),

and
 lim
n1,...,nr→∞ λmin(gn1,...,nr (h)) = λmin(h).

Deﬁnition 3.10 (representation of Hoﬀman graphs). For a Hoﬀman graph h and a positive integer

m, a mapping φ : V (h) → Rm (resp. φ : V (h) → Zm) satisfying

(φ(x), φ(y)) =
 



 t if x = y and x, y ∈ Vslim(h);

1 if x = y and x, y ∈ Vfat(h);

1 if x ∼ y;

0 otherwise,

is a (resp. integral) representation of h of norm t.

We denote by Λ(h, t) the lattice generated by the set {φ(x) | x ∈ V (h)}. Note that the

isomorphism class of Λ(h, t) depends only on h and t, and is independent of φ, justifying the

notation.

Deﬁnition 3.11 (reduced representation of Hoﬀman graphs). For a Hoﬀman graph h and a

positive integer m, a mapping ψ : Vslim(h) → Rm (resp. φ : V (h) → Zm) satisfying

(ψ(x), ψ(y)) =
 



 t − |N f
h (x)| if x = y;

1 − |N f
h (x, y)| if x ∼ y;

−|N f
h (x, y)| otherwise,

is a (resp. integral) reduced representation of h of norm t.

We denote by Λred(h, t) the lattice generated by the set {ψ(x) | x ∈ Vslim(h)}. Note that the

isomorphism class of Λred(h, t) also depends only on h and t, and is independent of ψ, justifying

the notation.

Lemma 3.12 ( [52, Theorem 2.8]). For a Hoﬀman graph h, the following conditions are equivalent:

11

(i) h has a representation of norm t;

(ii) h has a reduced representation of norm t;

(iii) λmin(h) ≥ −t.

A Hoﬀman graph h is called integrally representable of norm t, if h has an integral representation

φ : V (h) → Zm of norm t for some m.

3.1 Sum and decomposition

Deﬁnition 3.13 (sum). Let h1 and h2 be two Hoﬀman graphs. A Hoﬀman graph h is the sum of

h1 and h2, denoted by h = h1 ⊎ h2, if h satisﬁes the following condition:

There exists a partition {
V 1
slim(h), V 2
slim(h)
} of Vslim(h) such that induced Hoﬀman subgraphs

generated by V i
slim(h) are hi for i = 1, 2 and

Sp(h) =
 


Sp(h1) O

O Sp(h2)





with respect to the partition {
V 1
slim(h), V 2
slim(h)
} of Vslim(h).

Clearly, by deﬁnition, the sum is associative, so that the sum ⊎r
i=1 hi is well-deﬁned. We can

check that h is a sum of two non-empty Hoﬀman graphs if and only if Sp(h) is a block matrix with

at least two blocks. If h = h1 ⊎ h2 for some non-empty Hoﬀman subgraphs h1 and h2, then we call

h decomposable with {h1, h2} as a decomposition and call h1, h2 factors of h. Otherwise, h is called

indecomposable.

The following lemma gives a combinatorial way to deﬁne the sum of Hoﬀman graphs.

Lemma 3.14 ( [64, Lemma 2.11]). Let h be a Hoﬀman graph and h1 and h2 be two induced

Hoﬀman subgraphs of h. The Hoﬀman graph h is the sum of h1 and h2 if and only if h1, h2, and

h satisfy the following conditions:

(i) V (h) = V (h1) ∪ V (h2);

(ii) {Vslim(h1), Vslim(h2)
} is a partition of Vslim(h);

(iii) if x ∈ Vslim(hi), f ∈ Vfat(h) and x ∼ f , then f ∈ Vfat(hi);

(iv) if x ∈ Vslim(h1) and y ∈ Vslim(h2), then x and y have at most one common fat neighbor, and

they have one if and only if they are adjacent.

Let µ ≤ −1 be a real number and h a Hoﬀman graph with λmin(h) ≥ µ. The Hoﬀman graph

h is said to be µ-reducible if there exists a Hoﬀman graph ̃h containing h as an induced Hoﬀman

12

subgraph, such that there is a decomposition {̃hi}2
i=1 of ̃h with λmin(̃hi) ≥ µ and Vs(̃hi) ∩ Vs(h) ̸=

∅ (i = 1, 2). We say that h is µ-irreducible if λmin(h) ≥ µ and h is not µ-reducible. A Hoﬀman

graph h is said to be reducible if h is λmin(h)-reducible. We say h is irreducible if h is not reducible.

Deﬁnition 3.15 (line Hoﬀman graph). Let H be a family of pairwise non-isomorphic Hoﬀman

graphs. A Hoﬀman graph h is an H-line Hoﬀman graph if there exists a Hoﬀman graph h′ satisfying

the following conditions:

(i) h′ has h as an induced Hoﬀman subgraph;

(ii) h′ has the same slim graph as h;

(iii) h′ = ⊎r
i=1 h′
i, where h′
i is isomorphic to an induced Hoﬀman subgraph of some Hoﬀman graph

in H for i = 1, . . . , r.

Deﬁnition 3.16 (H-saturated Hoﬀman graph). Let H be a family of pairwise non-isomorphic

Hoﬀman graphs. A Hoﬀman graph h is H-saturated, if h is an H-line Hoﬀman graph, and no

fat vertex can be attached to h in such a way that the resulting Hoﬀman graph is also an H-line

Hoﬀman graph.

Note that if we set H to be the family of pairwise non-isomorphic µ-irreducible Hoﬀman graphs,

then a µ-saturated Hoﬀman graph is H-saturated.

3.2 H-Saturated Hoﬀman graphs

Now we depict several Hoﬀman graphs as follows. They appeared in [94] for the ﬁrst time.

Actually some of them are not used in this paper, but we use the same symbols as in [94] to avoid

confusion.

h1 = h2 = h3 =

h4 = h5 = h6 =

h7 = h8 = h9 =

Figure 1

13

We ﬁrst state a classical result by Krausz [65].

Theorem 3.17. A graph G of order n is a line graph if and only if one can partition the edge-set

of G into cliques {C1, C2, . . . , Ct} such that each vertex lies in at most 2 Ci’s. Moreover, if G is a

connected line graph and n ≥ 7, then this partition into cliques is unique.

In terms of line Hoﬀman graphs, we can formulate this result as follows.

Theorem 3.18. Every {h2}-line Hoﬀman graph whose slim graph is connected of order at least 7

has a unique {h2}-saturated Hoﬀman graph containing it, up to strong isomorphism.

In [32], Cvetkovi´c, Doob and Simi´c showed a similar result for generalized line graphs. We

formulate their result in terms of line Hoﬀman graphs as follows.

Theorem 3.19. Every {h2, h3}-line Hoﬀman graph whose slim graph is connected of order at least

7 has a unique {h2, h3}-saturated Hoﬀman graph containing it, up to strong isomorphism.

Taniguchi [84] showed the following result, although in his paper he used diﬀerent terminology.

Theorem 3.20. Every {h2, h5}-line Hoﬀman graph whose slim graph is connected of order at least

8 has a unique {h2, h5}-saturated Hoﬀman graph containing it, up to strong isomorphism.

In [37], Furuya, Kubota, Taniguchi and Yoshino generalized Theorem 3.20. In [85], Taniguchi

showed that if a graph is not the slim graph of a {h2, h5}-line Hoﬀman graph but each of its

proper induced subgraph is the slim graph of a {h2, h5}-line Hoﬀman graph, then this graph is just

isomorphic to one of 38 graphs, found by computer. In [67], Kubota, Taniguchi and Yoshino gave

more related results.

3.3 Minimal fat Hoﬀman graphs

Let µ < 0 be a real number. A Hoﬀman graph h is said to be t-fat-minimal for µ, if it is t-fat,

its smallest eigenvalue is less than µ, and each of its proper t-fat induced Hoﬀman subgraph has

smallest eigenvalue at least µ. For convenience, a 1-fat-minimal Hoﬀman graph for µ is also said

to be fat-minimal for µ.

Woo and Neumaier [94] determined all the fat-minimal Hoﬀman graphs for −1 − √2. By

checking their results, one can ﬁnd that every fat-minimal Hoﬀman graph for −1 − √
2 has at most

4 slim vertices.

Later Koolen et al. [62] studied fat-minimal Hoﬀman graphs for −3. They found that every fat-

minimal Hoﬀman graph for −3 has at most 10 slim vertices. Moreover, if a fat-minimal Hoﬀman

graph for −3 has a slim vertex with at least 2 fat neighbors, then it has at most 2 slim vertices.

14

Here we introduce an important family of fat Hoﬀman graphs. Let H be a graph. Let q(H) be

the fat Hoﬀman graph with slim graph H and one fat vertex attached to all slim vertices. Then

the special matrix of q(H) is −I − A(H), where H is the complement of H. Let λ0(H) be the

largest eigenvalue of H. We have:
 λmin(q(H)) = −1 − λ0(H) (3)

immediately. We will show that if q(H) is fat-minimal for µ, then its smallest eigenvalue can not

be much smaller than µ. To prove it, some preparation is necessary.

Lemma 3.21 ( [81, Corollary 2.2]). Let G = (V (G), E(G)) be a connected graph with the largest

eigenvalue λ0(G) and the principal eigenvector v, the positive eigenvector of norm 1 with eigenvalue

λ0(G). For each vertex x of G, let G − x be the subgraph of G induced on V (G) − {x} with the

largest eigenvalue λ0(G − x). Then

1 − 2v2
x
1 − v2
x λ0(G) ≤ λ0(G − x) ≤ λ0(G), (4)

where vx is the x-coordinate of the vector v.

This lemma has the following consequence.

Proposition 3.22. Let λ be a positive real number and G a graph of order n ≥ 3 with the

largest eigenvalue λ0(G). If λ0(G) > λ and for every proper induced subgraph H of G, the largest

eigenvalue λ0(H) of H is at most λ, then λ0(G) ≤ n−1
n−2 λ.

Proof . It is not hard to see that G is connected. Let v be the principal eigenvector of G. Take a

vertex x of G such that vx is minimal. Then vx ≤ 1√n as the norm of x is equal to 1. Now apply

Lemma 3.21 to this vertex x and we obtain the desired inequality. This completes the proof.

Lemma 3.23. Let µ < 0 be a real number and n ≥ 3 a positive integer. Let q(H) be a Hoﬀman

graph with n slim vertices. If q(H) is fat-minimal for µ, then λmin(q(H)) ≥ µ + 1+µ
n−2 .

Proof . As q(H) is a fat-minimal Hoﬀman graph for µ, we have λmin(q(H)) < µ, and thus λ0(H) >

−1 − µ by (3). Assume K := H ′ is a proper induced subgraph of H, where H ′ is a proper induced

subgraph of H. Considering the minimality of q(H), we have −1 − λ0(H ′) = λmin(q(H ′)) ≥ µ by

(3). This means λ0(K) = λ0(H ′) ≤ −1 − µ. Now the conditions of Proposition 3.22 are satisﬁed,

and we can easily obtain λ0(H) ≤ n−1
n−2 (−1 − µ). By using (3) again, we have λmin(q(H)) =

−1 − λ0(H) ≥ µ + 1+µ
n−2 .
 15

3.4 Maximal µ-irreducible Hoﬀman graphs

A µ-irreducible Hoﬀman graph is maximal, if it is not a proper induced Hoﬀman subgraph of

another µ-irreducible Hoﬀman graph. Notice that if a µ-irreducible Hoﬀman graph is maximal,

then it is µ-saturated and indecomposable.

Woo and Neumaier [94] found that there are exactly 4 maximal (−1 − √2)-irreducible Hoﬀman

graphs, up to isomorphism, and they are h2, h5, h7 and h9 in Figure 1.

Let τ be the golden ratio 1+√5
2 . In 2014, Munemasa, Sano and Taniguchi [76] found that there

are exactly 18 maximal (−1 − τ )-irreducible Hoﬀman graphs, up to isomorphism, and they also

gave a list of these 18 Hoﬀman graphs.

As for the fat maximal (−3)-irreducible Hoﬀman graphs, we refer to [52] and [58]. To state the

main results there, we need to deﬁne the special graph of a Hoﬀman graph. (Signed graphs and

switching equivalence will be introduced in Section 7.)

Deﬁnition 3.24 (special graph). The special graph of a Hoﬀman graph h is the signed graph

S(h) := (V (S(h)), E+(S(h)), E−(S(h))),

where V (S(h)) = Vslim(h) and

E+(S(h)) ={{x, y} | x, y ∈ Vslim(h), x ̸= y, {x, y} ∈ E(h), N f
h (x, y) = ∅},

E−(S(h)) ={{x, y} | x, y ∈ Vslim(h), x ̸= y, {x, y} ∈ E(h), |N f
h (x, y)| ≥ 2}

∪{{x, y} | x, y ∈ Vslim(h), x ̸= y, {x, y} ̸∈ E(h), N f
h (x, y) ̸= ∅}.

The special ε-graph of h is the graph Sǫ(h) = (Vslim(h), Eǫ(S(h))) for ǫ ∈ {+, −}.

Let h be a fat indecomposable Hoﬀman graph with λmin(h) ≥ −3. It is shown in [52] that, if h is

not the Hoﬀman graph , then its special graph is connected and the lattice Λred(h, 3) is either an

irreducible root lattice or a sublattice of the standard lattice. Moreover, if h is a fat maximal (−3)-

irreducible Hoﬀman graph and the lattice Λred(h, 3) is a sublattice of the standard lattice, that is

h is fat maximal (−3)-irreducible with an integral representation of norm 3, then the graph S−(h)

is connected and is (isomorphic to) the Dynkin diagrams An, Dn or the extended Dynkin diagram

ˆAn, ˆDn for some positive integer n (see Figure 2). Using this result of [52], Koolen, Li and Yang [58]

classiﬁed the fat maximal (−3)-irreducible Hoﬀman graphs with an integral representation of norm

3. As for the fat maximal (−3)-irreducible Hoﬀman graphs with no integral representation of norm

3, the classiﬁcation is still open.

A related result was shown by Munemasa, Sano and Taniguchi [77] and Greaves, Koolen,

Munemasa, Sano and Taniguchi [45]. In [77], Munemasa et al. gave a characterization of special

16

An Dn

ˆAn ˆDn

Figure 2

graphs of fat Hoﬀman graphs with smallest eigenvalue greater than −3 which contain a slim vertex

having two fat neighbors. In [45, Theorem 20], Greaves et al. showed that for a fat Hoﬀman graph

in which every slim vertex has exactly one fat neighbor, it has smallest eigenvalue greater than −3

if and only if its special graph is switching equivalent to certain signed graphs.

4 Graphs with large minimal valency

In this section, we give some results on graphs with ﬁxed smallest eigenvalue and large minimal

valency. We start with the associated Hoﬀman graphs.

4.1 Associated Hoﬀman graphs

In this subsection, we summarize some facts about associated Hoﬀman graphs and quasi-cliques,

which provide some connections between Hoﬀman graphs and graphs. For more details, we refer

to [54] and [64].

Let m be a positive integer and G a graph that does not contain ̃K2m as an induced subgraph,

where ̃K2m is the graph deﬁned before Theorem 2.9. Let C(n) = {C | C is a maximal clique of G

of order at least n}. Deﬁne the relation ≡m
n on C(n) by C1 ≡m
n C2 if each vertex x ∈ C1 has at

most m − 1 non-neighbors in C2 and each vertex y ∈ C2 has at most m − 1 non-neighbors in C1.

Note that ≡m
n is an equivalence relation if n ≥ (m + 1)2.

Let [C]m
n denote the equivalence class of C(n) of G under the equivalence relation ≡m
n containing

the maximal clique C of C(n). We deﬁne the quasi-clique Q([C]m
n ) of C with respect to the pair

(m, n) as the subgraph of G induced on the set {x ∈ V (G) | x has at most m − 1 non-neighbors in

C}. Note that for any C ′ ∈ [C]m
n , we have Q([C ′]m
n ) = Q([C]m
n ) (see [54, Lemma 3.3]).

Let [C1]m
n , . . . , [Cr]m
n be the equivalence classes of maximal cliques under ≡m
n . The associated

Hoﬀman graph g = g(G, m, n) is the Hoﬀman graph satisfying the following conditions:

(i) Vslim(g) = V (G), Vfat(g) = {f1, f2, . . . , fr};

(ii) the slim graph of g equals G;
 17

(iii) for each i, the fat vertex fi is adjacent to exactly all the vertices of Q([Ci]m
n ) for i = 1, 2, . . . , r.

From the above deﬁnition of associated Hoﬀman graphs, we ﬁnd that for each i = 1, . . . , r, the

quasi-clique Q([Ci]m
n ) of Ci with respect to the pair (m, n) is exactly the quasi-clique Qg(fi) in g

with respect to the fat vertex fi.

The following result, which is a crucial tool for the study of graphs with ﬁxed smallest eigenvalue

and large minimal valency, was shown in [54, Proposition 4.1].

Proposition 4.1. Let G be a graph and let m ≥ 2, φ, σ, p ≥ 1 be integers. There exists a positive

integer n = n(m, φ, σ, p) ≥ (m + 1)2 such that, for any integer q ≥ n and any Hoﬀman graph h

with at most φ fat vertices and at most σ slim vertices, the graph G(h, p) is an induced subgraph

of G, provided that the graph G satisﬁes the following conditions:

(i) the graph G does not contain ̃K2m as an induced subgraph,

(ii) its associated Hoﬀman graph g = g(G, m, q) contains h as an induced Hoﬀman subgraph.

In order to use this proposition well, we need the following deﬁnition.

Deﬁnition 4.2 ((r, λ)-nice Hoﬀman graph). Let r be a positive integer and λ ≤ −1 a real number.

A Hoﬀman graph h is (r, λ)-nice, if it contains no induced Hoﬀman subgraph with the number of

slim vertices at most r and smallest eigenvalue less than λ.

Theorem 4.3. Let λ ≤ −2 be a real number and r a positive integer. Let m be such that the

smallest eigenvalue of ̃K2m is less than λ. Then there exists a positive integer N = N (λ, m, r) ≥

(m + 1)2 such that, for any graph G with smallest eigenvalue at least λ, the associated Hoﬀman

graph g = g(G, m, q) is (r, λ)-nice if q ≥ N .

Proof . Let h(⌈−λ⌉+1) be the Hoﬀman graph with one slim vertex adjacent to ⌈−λ⌉ + 1 fat vertices,

and let

G = {h
(⌈−λ⌉+1)} ∪ {h | λmin(h) < λ, |Vslim(h)| ≤ r, |N f
h (x)| ≤ ⌈−λ⌉ for all x ∈ Vslim(h)
}

be a family of pairwise non-isomorphic Hoﬀman graphs. It is not hard to see that the family G

is ﬁnite and we may assume G = {f1, f2, . . . , fs}. As λmin(fi) < λ for each i = 1, . . . , s, there exist

positive integers pi’s such that λmin(G(fi, pi)) < λ hold by Theorem 3.9. Let p = max1≤i≤s pi,

φ = max1≤i≤s |Vfat(fi)| and let N be the positive integer n(m, φ, r, p) such that Proposition 4.1

holds. Now for a given graph G with λmin(G) ≥ λ and an integer q > N , we will show that

the associated Hoﬀman graph g(G, m, q) is (r, λ)-nice. Suppose not. Then g(G, m, q) contains

a Hoﬀman graph in G as an induced Hoﬀman subgraph. Without loss of generality, we may

assume f1 is an induced Hoﬀman subgraph of g(G, m, q). Proposition 4.1 says that under this

condition the graph G contains G(f1, p) as an induced subgraph. Now we obtain a contradiction,

as λmin(G(f1, p)) < λ and λmin(G) ≥ λ. Hence the theorem holds.

18

4.2 Graphs with large minimal valency

In this subsection, we focus on graphs with ﬁxed smallest eigenvalue and large minimal valency.

Let G be a graph. For a given vertex x of G, we call the subgraph of G induced on the neighbors

of x the local graph of G at x, and denote it by ∆G(x). For convenience, we also denote by kG(x)

the valency of x and ¯k(∆G(x)) the average valency of the graph ∆G(x), that is,

kG(x) = |V (∆G(x))|, and¯k(∆G(x)) = 2|E(∆G(x))|
|V (∆G(x))| .

Let p be a positive integer. A p-plex is an induced subgraph in which each vertex is adjacent

to all but at most p of the vertices. Note that a clique is exactly the same as a 1-plex.

We deﬁne G(t) to be the family of pairwise non-isomorphic indecomposable t-fat Hoﬀman

graphs with special matrix (−t − 1) or
 

Js1 − (t + 1)I −J

−J Js2 − (t + 1)I


 where 1 ≤ s1, s2 ≤ t.

Using associated Hoﬀman graphs the following ﬁve results have been shown.

Theorem 4.4 (cf. [64, Theorem 1.2]). Let t ≥ 2 be an integer. Then there exists a positive integer

C2(t) such that, if a graph G satisﬁes the following conditions:

(i) kG(x) > C2(t) holds for all x ∈ V (G),

(ii) any (t2 + 1)-plex containing x has order at most kG(x)−C2(t)
t for all x ∈ V (G),

(iii) λmin(G) ≥ −t − 1,

then G is the slim graph of a t-fat G(t)-line Hoﬀman graph.

Theorem 4.5 (cf. [64, Theorem 1.3]). Let t ≥ 2 be an integer. Then there exists a positive integer

C3(t) such that, if a graph G satisﬁes the following conditions:

(i) kG(x) > C3(t) holds for all x ∈ V (G),

(ii) ¯k(∆G(x)) ≤ kG(x)−C3(t)
t holds for all x ∈ V (G),

(iii) λmin(G) ≥ −t − 1,

then G is the slim graph of a t-fat G(t)-line Hoﬀman graph.

In the next two results, we focus on graphs with smallest eigenvalue at least −3.

Theorem 4.6 ( [64, Theorem 1.4]). There exists a positive integer κ2 such that, if a graph G

satisﬁes the following conditions:

(i) kG(x) > κ2 holds for all x ∈ V (G),
 19

(ii) any 5-plex containing x has order at most kG(x) − κ2 for all x ∈ V (G),

(iii) λmin(G) ≥ −3,

then G is the slim graph of a 2-fat { , , }
-line Hoﬀman graph.

Theorem 4.7 ( [64, Theorem 1.5]). There exists a positive integer κ3 such that, if a graph G

satisﬁes the following conditions:

(i) kG(x) > κ3 holds for all x ∈ V (G),

(ii) ¯k(∆G(x)) ≤ kG(x) − κ3 holds for all x ∈ V (G),

(iii) λmin(G) ≥ −3,

then G is the slim graph of a 2-fat { , , }
-line Hoﬀman graph.

The following result is important in the proof of Theorem 2.2.

Theorem 4.8 ( [62, Theorem 5.3]). There exists a positive integer κ4 such that, if G is a graph

with smallest eigenvalue at least −3 and minimal valency at least κ4, then G is the slim graph of

a fat Hoﬀman graph with smallest eigenvalue at least −3.

We now show how to obtain Theorem 2.2 from Theorem 4.8. Assume that G is the slim graph

of the fat Hoﬀman graph h with smallest eigenvalue at least −3. Without loss of generality, we

may assume −3 ≤ λmin(G) < −2 by Theorem 2.1. Following from Lemma 3.12, we ﬁnd that h

has a reduced representation of norm 3 and denote it by ψ. Then for each vertex x of G, we let

Nx := ψ(x) + ∑

f ∼x,f ∈Vfat(h) ef , where {ef | f ∈ Vfat(h)} is a set of orthonormal integral vectors

which are orthogonal to all of the vectors in the set {ψ(y) | y ∈ V (G)}. It is not hard to check

that the matrix N with Nx’s as its columns satisﬁes the equation A(G) + 3I = N T N . Thus

Λ(G) = ⟨Nx | x ∈ V (G)⟩Z = ⟨ψ(x) + ∑

f ∼x,
f ∈Vfat(h)
 ef | x ∈ V (G)⟩Z.

This implies that the integrability of the integral lattice Λ(G) depends on the integrability of the

integral lattice Λred(h, 3) := ⟨ψ(x) | x ∈ V (G)⟩Z. Note that for each x, the norm of the vector ψ(x)

is at most 2, as h is fat. Hence the integral lattice Λred(h, 3) is the direct sum of Ei’s, Di’s, Ai’s and

Zq where q is a non-negative integer. As each of these lattices is s-integrable (see [31, Corollary

23]) for any s ≥ 2, Theorem 4.8 holds.

5 Distance-regular graphs

In this section, we give some results on distance-regular graphs that have ﬁxed smallest eigen-

value or whose local graphs have ﬁxed smallest eigenvalue. We start with some deﬁnitions.

20

5.1 Deﬁnitions

Let G be a k-regular graph of order n. If every pair of adjacent vertices of G has exactly a

common neighbors, and every pair of distinct and non-adjacent vertices of G has exactly c common

neighbors, then G is called strongly regular with parameters (n, k, a, c).

Let G be a connected graph with diameter D. For each vertex x of G, denote by Gi(x) the

set of vertices at distance precisely i from x, where 0 ≤ i ≤ D. For any two vertices x and y,

denote by d(x, y) the distance between x and y. The graph G is called distance-regular if there

are positive integers
 b0, b1, . . . , bD−1, c1 = 1, c2, . . . , cD

such that for any two vertices x and y with d(x, y) = i, |Gi−1(x) ∩ G1(y)| = ci (1 ≤ i ≤ D) and

|Gi+1(x)∩G1(y)| = bi (0 ≤ i ≤ D−1). Set bD = c0 = 0. The numbers bi, ci and ai := b0−bi−ci (0 ≤

i ≤ D) are called the intersection numbers of G. The array ι(G) := {b0, b1, . . . , bD−1; c1, c2, . . . , cD}

is called the intersection array of G. Note that a distance-regular graph of diameter 2 and order

n is a strongly regular graph with parameters (n, b0, a1, c2).

Let G be a distance-regular graph with valency k and smallest eigenvalue λmin(G). As observed

by Godsil, the order of a clique C in G satisﬁes the Delsarte bound, that is,

|V (C)| ≤ 1 + k
−λmin(G) ,

and we say that C is a Delsarte clique if its order equals 1 + k
−λmin(G) . We say that G is geometric

if there exists a family F of Delsarte cliques in G such that each edge of G lies in exactly one of

the Delsarte cliques of F. Although the family F of Delsarte cliques in geometric distance-regular

graphs is not always unique, usually it is.

5.2 Strongly regular graphs with ﬁxed smallest eigenvalue

It is well-known that a connected strongly regular graph such that its complement is discon-

nected is complete multipartite (see [43, Lemma 10.1.1]). So in this subsection, we will deal with

connected strongly regular graphs whose complements are also connected, that is, the so-called

primitive strongly regular graphs.

We start this subsection with two important families of geometric primitive strongly regular

graphs.

Family 1: A Steiner system S(2, t, v) is a pair (P, B), where P is a v-element set called a

point set and B is a family of t-element subsets of P called a block set such that each 2-element

subset of P is contained in exactly one block. Take a Steiner system S(2, t, v). Construct a

graph as follows: its vertex set is the block set of this Steiner system, and two blocks are adjacent

21

whenever they intersect in one point. This gives a geometric strongly regular graph with parameters

( v(v−1)
t(t−1) , t(v−t)
t−1 , (t−1)2 + v−1
t−1 −2, t2) (see [29, p. 5]). We call this graph the block graph of the Steiner

system and call this family the Steiner family.

Family 2: An orthogonal array with parameters t and v is a t × v2 array with entries in

{1, 2, . . . , v} such that the v2 ordered pairs in any two distinct rows are all diﬀerent. We denote

an orthogonal array with these parameters by OA(v, t). Note that an OA(v, 3) is equivalent

to a Latin square. Take an OA(v, t) orthogonal array O. Construct a graph as follows: its

vertex set is the set of columns of O, and two columns are adjacent whenever they have the same

entries in (exactly) one position. This gives a geometric strongly regular graph with parameters

(v2, (v − 1)t, v − 2 + (t − 1)(t − 2), t(t − 1)) (see [43, Theorem 10.4.2]). We call this family the Latin

square family.

Neumaier [79] showed the following theorem for strongly regular graphs with ﬁxed smallest

eigenvalue.

Theorem 5.1 (cf. [79, Theorem 4.7]). Let G be a primitive strongly regular graph with parameters

(n, k, a, c) and smallest eigenvalue −λ, where λ ≥ 2 is an integer. If (λ+1)(a+1)−k > (c−1)
(λ+1
2 )
,

then one of the following holds:

(i) G is in the Latin square family with parameters ((s + 1)2, sλ, s − 1 + (λ − 1)(λ − 2), λ(λ − 1)),

where s is a positive integer;

(ii) G is in the Steiner family with parameters (n, sλ, s − 1 + (λ − 1)2, λ2), where s is a positive

integer and n = (s + 1)(s(λ − 1) + λ)/λ.

He showed this theorem in two steps. The ﬁrst step was to show the following result.

Theorem 5.2 (cf. [79, Theorem 4.6]). Let G be a primitive strongly regular graph with parameters

(n, k, a, c) and smallest eigenvalue −λ, where λ ≥ 2 is an integer. If (λ+1)(a+1)−k > (c−1)
(λ+1
2 )
,

then G is geometric.

As step two, he determined the geometric strongly regular graphs with parameters (n, k, a, c)

and smallest eigenvalue −λ, where λ ≥ 2 is an integer, such that (λ + 1)(a + 1) − k > (c − 1)
(λ+1
2 ).

A non-complete connected regular graph is strongly regular if and only if it has exactly 3 distinct

eigenvalues (see [43, Lemma 10.2.1]). Now we discuss some results on connected non-regular graphs

with 3 distinct eigenvalues.

In [90], Van Dam determined the connected non-regular graphs with 3 distinct eigenvalues with

smallest eigenvalue at least −2.

In [18], Cheng, Greaves and Koolen determined the connected non-regular graphs with 3 dis-

tinct eigenvalues with second largest eigenvalue at most 1.

22

Motivated by Neumaier’s theorem, that is Theorem 5.1, Cheng, Gavrilyuk, Greaves, and Koolen

[17] showed that for any λ ≥ 2, there exists a constant n1(λ) such that any connected non-bipartite

biregular graph, with exactly 3 distinct eigenvalues λ0 > λ1 > λ2 satisfying λ1 ≤ λ, has at most

n1(λ) vertices. In the same paper, Cheng et al. asked whether the conclusion holds if the condition

λ1 ≤ λ is replaced by λ2 ≥ −λ. Cheng and Koolen [19] answered this question in the aﬃrmative.

This latter paper used the ideas of Hoﬀman, without actually introducing Hoﬀman graphs.

5.3 Distance-regular graphs with ﬁxed smallest eigenvalue

There are four important families of geometric distance-regular graphs: the Hamming graphs,

the Johnson graphs, the Grassmann graphs and the bilinear forms graphs. One of the reasons that

they are important is that for ﬁxed diameter there are inﬁnitely many graphs in each of these four

families.

Let D ≥ 1 and q ≥ 2 be integers. Let X be a ﬁnite set of size q. The Hamming graph H(D, q)

is the graph with the vertex set X D := ∏D
i=1 X (the Cartesian product of D copies of X), where

two vertices are adjacent whenever they diﬀer in precisely one coordinate. In particular, if D = 2,

then a Hamming graph H(2, q) is the line graph of a complete bipartite graph Kq,q. We also call

a Hamming graph H(2, q) a (q × q)-grid.

Let v, D be integers. Let X be a ﬁnite set of size v. The Johnson graph J(v, D) is the graph

with vertex set (X
D), the set of all D-element subsets of X, where two vertices are adjacent whenever

they intersect in precisely D − 1 elements. In particular, if D = 2, then a Johnson graph J(v, 2)

is the line graph of a complete graph Kv. We also call a Johnson graph J(v, 2) a triangular graph

and denote it by T (v). (Since the Johnson graph J(v, D) is isomorphic to the Johnson graph

J(v, v − D), we always assume v ≥ 2D.)

Let v, D be integers such that v ≥ D and q a prime power. Let F be a ﬁnite ﬁeld of order q and

V a v-dimensional vector space over F. The Grassmann graph Jq(v, D) is the graph with the set

of all D-dimensional subspaces of V as the vertex set, where two vertices are adjacent whenever

their intersection is a (D − 1)-dimensional subspace of V . (Since the Grassmann graph Jq(v, D) is

isomorphic to the Grassmann graph Jq(v, v − D), we will also always assume v ≥ 2D.)

Let D, e be integers such that e ≥ D and q a prime power. Let F be a ﬁnite ﬁeld of order q.

The bilinear forms graph Bil(D × e, q) is the graph with the set of all D × e matrices over F as

the vertex set, where two vertices are adjacent whenever the rank of their diﬀerence equals one.

Koolen and Bang [55] generalized Theorem 5.2 to the class of distance-regular graphs under

the extra condition that c2 ≥ 2, by showing:

Theorem 5.3 (cf. [55, Theorem 1.3]). For given λ ≥ 2, there are only ﬁnitely many non-geometric

distance-regular graphs with both valency and diameter at least 3, c2 ≥ 2 and smallest eigenvalue

23

at least −λ.

Now we are going to show that in Theorem 5.3, the condition c2 ≥ 2 can be removed. Suppose

that G is distance-regular with c2 = 1. It is not hard to see that G has no induced K2,1,1’s, and

thus G is locally the disjoint union of (a1 + 1)-cliques, that is, the local graph of G at each vertex

is the disjoint union of (a1 + 1)-cliques (see [6, Propositon 1.2.1]). We say that a distance-regular

graph is of order (s, t), if it is locally the disjoint union of t + 1 Ks’s. The next lemma gives a

suﬃcient condition for a distance-regular graph of order (s, t) to be geometric.

Lemma 5.4 (cf. [82, Proposition 3.1.6], [93, Corollary 7.7]). Let G be a distance-regular graph of

order (s, t) with diameter D ≥ 2. If s > t, then G is geometric.

Lemma 5.4 implies that for a non-geometric distance-regular graph of order (s, t) with smallest

eigenvalue at least −λ, its valency k satisﬁes k = s(t + 1) ≤ t(t + 1) ≤ (λ2 − 1)λ2, as it contains

a (t + 1)-claw K1,t+1 with smallest eigenvalue −√
t + 1 as an induced subgraph, which implies

−√t + 1 ≥ −λ by Lemma 3.7. Now using the fact that the Bannai-Ito conjecture, that is, for ﬁxed

k ≥ 3 there are only ﬁnitely many distance-regular graphs with valency k, is true (see [7, Theorem

1.1]), we ﬁnd that there are only ﬁnitely many non-geometric distance-regular graphs with both

valency and diameter at least 3, c2 = 1 and smallest eigenvalue at least −λ. Hence we obtain:

Theorem 5.5. For given λ ≥ 2, there are only ﬁnitely many non-geometric distance-regular graphs

with both valency and diameter at least 3 and smallest eigenvalue at least −λ.

Remark 5.6. (i) Note that the (general) result was known for λ = 2, see [12, Theorem 3.12.4, The-

orem 4.2.16].

(ii) Godsil [44] gave a special case for this result for antipodal distance-regular graphs of diameter

3.

Koolen and Bang [55] gave the following two conjectures for geometric distance-regular graphs.

Conjecture 5.7 ( [55, Conjecture 7.4]). For a ﬁxed integer λ ≥ 2, any geometric distance-regular

graph with smallest eigenvalue −λ, diameter D ≥ 3 and c2 ≥ 2 either is a Hamming graph, a

Johnson graph, a Grassmann graph, a bilinear forms graph, or has the number of vertices bounded

above by a function of λ.

Conjecture 5.8 ( [55, Conjecture 7.5]). For a ﬁxed integer λ ≥ 2, the diameter of a geometric

distance-regular graph with smallest eigenvalue −λ and valency at least 3 is bounded above by a

function of λ.

Note that Conjecture 5.7 can be seen as a generalization of Theorem 5.1 for the class of distance-

regular graphs. Now we discuss recent progress on Conjecture 5.8. Bang [6] showed the following

result:
 24

Proposition 5.9 (cf. [6, Theorem 1.1]). Fix an integer λ ≥ 2. Suppose that G is a geometric

distance-regular graph with diameter D ≥ 2 and smallest eigenvalue −λ. If G contains an induced

subgraph K2,1,1, then D ≤ λ.

For a distance-regular graph G with intersection array {b0, b1, . . . , bD−1; c1, c2, . . . , cD}, deﬁne

the head h := h(G) = |{i | (ci, ai, bi) = (c1, a1, b1)}|. The following is known for geometric

distance-regular graphs with order (s, t) and is due to Suzuki [82].

Proposition 5.10 (cf. [82, Proposition 3.1.6], [93, Corollary 7.7]). Let G be a distance-regular

graph of order (s, t) with head h and diameter D ≥ 2. If s > t, then D ≤ t(h + 1) + 1.

Note that the smallest eigenvalue of a geometric distance-regular graph of order (s, t) is equal

to −t − 1. Combining Propositions 5.9 and 5.10, we obtain:

Corollary 5.11. Let λ ≥ 2 be an integer and G a geometric distance-regular graph with head h,

diameter D ≥ 2 and smallest eigenvalue −λ. Then D ≤ (λ − 1)(h + 1) + 1.

This means that in order to solve Conjecture 5.8, we only need to show that the head of a

geometric distance-regular graph with smallest eigenvalue −λ is bounded above by a function of

λ.

5.4 Characterizations of distance-regular graphs

Note that Bannai’s problem asks to classify the Q-polynomial distance-regular graphs with

large diameter. (See Appendix A for the deﬁnition of a Q-polynomial distance-regular graph.)

One part of this problem is to characterize the known inﬁnite families as a distance-regular graph.

We say that a distance-regular graph has classical parameters (D, b, α, β), if its diameter is D and

its intersection array is given as follows:

bi =(
[D
1
 ] − [i
1

])(β − α
[i
1

]),

ci =[i
1

](1 + α
[i − 1
1
 ])

(i = 0, 1, . . . , D), where
 [i
j
] =
 



 j−1∏

ℓ=0
 i−ℓ
j−ℓ if b = 1,

j−1∏

ℓ=0
 bi−bℓ
bj−bℓ if b ̸= 1.

An important subproblem of Bannai’s problem is to classify the distance-regular graphs with

classical parameters (D, b, α, β), as every distance-regular graph with classical parameters is Q-

polynomial (see [12, Corollary 8.4.1]). Note that all the known inﬁnite families of distance-regular

graphs with unbounded diameter are either classical or closely related to classical distance-regular

25

graphs. If a distance-regular graph G has classical parameters (D, b, α, β) where D ≥ 3, then

b is an integer equals neither 0 nor −1 and if b is positive, then the second largest eigenvalue

λ1 of G satisﬁes λ1 = b1
b − 1 (see [12, Proposition 6.2.1] and [12, Corollary 8.4.2]). In Lemma

6.2 we will relate the smallest eigenvalue of any local graph of a distance-regular graph with

b1
λ1+1 , where λ1 is the second largest eigenvalue of this distance-regular graph. For the rest of

this subsection, we discuss the characterization of distance-regular graphs with second largest

eigenvalue λ1 = b1 − 1, the Grassmann graphs and the bilinear forms graphs. For more details and

also for more characterizations, see [40] and [93, Section 9]. For more information on the known

families of distance-regular graphs with unbounded diameter, see [12, Chapter 9].

Characterization of distance-regular graphs with second largest eigenvalue λ1 = b1 − 1

It is known that, if a distance-regular graph contains an induced quadrangle, then the second

largest eigenvalue λ1 is at most b1 − 1 (see [12, Proposition 4.4.9]). Distance-regular graphs that

have second largest eigenvalue b1 − 1 include the Hamming graphs and the Johnson graphs. In the

next result we characterize the distance-regular graphs with second largest eigenvalue λ1 = b1 − 1.

This result is due to Terwilliger and Neumaier, independently.

Theorem 5.12 (cf. [12, Thoerem 4.4.11]). Let G be a distance-regular graph with second largest

eigenvalue λ1 = b1 − 1. Then at least one of the following holds:

(i) G is a strongly regular graphs with smallest eigenvalue −2;

(ii) c2 = 1;

(iii) c2 = 2 and G is a Hamming graph H(D, q), a Doob graph (see [12, p. 262]), the Conway-

Smith graph with intersection array {10, 6, 4, 1; 1, 2, 6, 10} (see [12, p. 399]) or the Doro graph

with intersection array {10, 6, 4; 1, 2, 5} (see [12, Chapter 12.1]);

(iv) c2 = 4 and G is a Johnson graph J(v, D) where v ≥ 2D;

(v) c2 = 6 and G is a halved cube (see [12, p. 264]);

(vi) c2 = 10 and G is the Gosset graph with intersection array {27, 10, 1; 1, 10, 27} (see [12,

p. 103]).

Note that this theorem also classiﬁes the distance-regular graphs with classical parameters

(D, 1, α, β) (see [12, Theorem 6.1.1]).

As corollaries we have the following characterizations of the Hamming graphs and the Johnson

graphs. The characterization of the Hamming graphs is due to Egawa and the characterization of

the Johnson graphs is due to Terwilliger.
 26

Theorem 5.13 (cf. [12, Corollary 9.2.5]). Let G be a distance-regular graph with the same inter-

section array as a Hamming graph H(D, q). Then G is the Hamming graph H(D, q) or, if q = 4,

a Doob graph.

Theorem 5.14 (cf. [86, Corollary 1.2]). Let G be a distance-regular graph with the same intersec-

tion array as a Johnson graph J(v, D), where v ≥ 2D. Then G is the Johnson graph J(v, D), or

if (v, D) = (8, 2), a Chang graph.

Characterization of the Grassmann graphs

Metsch [73], building on work of many people, characterized the Grassmann graphs as follows.

Theorem 5.15 ( [73, Corollary 1.2]). Let G be a distance-regular graph with the same intersection

array as a Grassmann graph Jq(v, D), where v ≥ 2D ≥ 6 are integers and q ≥ 2 is a prime power.

Then G is the Grassmann graph Jq(v, D) if v ≥ max{2D + 2, 2D + 6 − q}.

His approach is to ﬁnd large cliques, called grand cliques and show that each edge lies in such

a unique grand clique.

Gavrilyuk and Koolen [38] characterized the Grassmann graph Jq(2D, D) as follows.

Theorem 5.16. Let G be a distance-regular graph with the same intersection array as a Grassmann

graph Jq(2D, D), where D ≥ 3 is an integer and q ≥ 2 is a prime power. Then G is the Grassmann

graph Jq(2D, D) if D ≥ 9.

They ﬁrst showed that the local graph of such a graph must have the same spectrum as the

q-clique extension of the ( qD−1
q−1 × qD−1
q−1 )-grid. Furthermore, using the Q-polynomial property they

showed that the local graph at any vertex satisﬁes that every pair of distinct non-adjacent vertices

has the same number of common neighbors (we call graphs with this property co-edge regular

graphs and study them in the next section). Then following from Theorem 6.7, they had that the

local graph is really the q-clique extension of the ( qD−1
q−1 × qD−1
q−1 )-grid, if D ≥ 9. Now building on

work of Numata, Cooperstein and Cohen (see [12, Theorem 9.3.8]), they completed their proof.

Note that the situation for distance-regular graphs with the same parameters as a Grassmann

graph Jq(2D + 1, D) is very diﬀerent, as Van Dam and Koolen [92] constructed a distance-regular

graph ˜Jq(2D + 1, D) with the same parameters as Jq(2D + 1, D), where q is a prime power and

D ≥ 2 is an integer. For these graphs, not every edge lies in a maximum clique. This shows that

the method used by Metsch can not work in this case. Whether there is a geometric argument

for this case is not clear on this moment. Note that Munemasa and Tonchev [78] showed that the

block graph of the design constructed by Jungnickel and Tonchev [53] is (isomorphic to) the graph

˜Jq(2D + 1, D).
 27

Characterization of the bilinear forms graphs.

Metsch [74], again building on work of many people, characterized the bilinear forms graphs

as follows.

Theorem 5.17 ( [74, Corollary 1.2]). Let G be a distance-regular graph with the same intersection

array as a bilinear forms graph Bil(D × e, q), where e ≥ D ≥ 3 are integers and q ≥ 2 is a prime

power. If q = 2 and e ≥ D + 4 or q ≥ 3 and e ≥ D + 3, then G is the bilinear forms graph

Bil(D × e, q).

His approach is the same as for the Grassmann graphs.

Gavrilyuk and Koolen [39] characterized the bilinear forms graph Bil(D × D, 2) as follows.

Theorem 5.18 ( [39, Theorem 1.3]). Let G be a distance-regular graph with the same intersection

array as a bilinear forms graph Bil(D × D, 2), where D ≥ 3 is an integer. Then G is the bilinear

forms graph Bil(D × D, 2).

They ﬁrst showed that the local graph of such a graph must be a ((2D − 1) × (2D − 1))-grid

by showing that the local graph must have the same spectrum as the ((2D − 1) × (2D − 1))-grid.

Then they used the cliques of order 2D to construct a geometry and using this geometry they were

able to show that the graph must be the bilinear forms graph Bil(D × D, 2).

5.5 Graphs cospectral to a distance-regular graph

In this subsection, we give some results on graphs cospectral to a distance-regular graph.

We start with the Hamming graphs. Bang, Van Dam and Koolen [9] showed the following

results.

Proposition 5.19 ( [9, Theorem 3.4]). Let q and D ≥ 2 be positive integers. Let 2q > D4 +

2D3 + 2D2 − 5D − 4. Then any graph that is cospectral to H(D, q) is locally the disjoint union of

D cliques of order q − 1.

They employed this result to show:

Proposition 5.20 ( [9, Theorem 4.5]). Let q ≥ 36. Then the Hamming graph H(3, q) is determined

by its spectrum.

Using Theorem 4.5, Koolen Yang and Yang showed the following weaker result.

Theorem 5.21 (cf. [64, Theorem 1.6]). There exists a positive integer q′ such that for each q ≥ q′,

any graph that is cospectral to the Hamming graph H(3, q) is the slim graph of a 3-fat { }
-line

Hoﬀman graph.
 28

Next, we discuss the Johnson graphs. Again using Theorem 4.5, Koolen et al. showed the

following result.

Theorem 5.22 (cf. [64, Theorem 1.7]). There exists a positive integer v′ such that for each v ≥ v′,

any graph that is cospectral to the Johnson graph J(v, 3) is the slim graph of a 3-fat { }
-line

Hoﬀman graph.

Van Dam, Haemers, Koolen and Spence [91, p. 1814] gave a construction of cospectral graphs

of the Johnson graph J(v, D) (v ≥ 2D ≥ 4) that are the block graphs of certain designs.

Similar results can be obtained for cospectral graphs of the Grassmann graphs and the bilinear

forms graphs.

6 Co-edge regular graphs

In this section, we discuss co-edge regular graphs with ﬁxed smallest eigenvalue. A k-regular

graph of order n is called co-edge regular with parameters (n, k, c), if every pair of distinct and non-

adjacent vertices has exactly c common neighbors. Note that a (t1 ×t2)-grid, which is the line graph

of a complete bipartite graph Kt1,t2, is a co-edge regular graph with parameters (t1t2, t1 + t2 − 2, 2).

The results in this section are motivated by two results of Terwilliger for distance-regular

graphs. The ﬁrst result concerns the local graph of a thin Q-polynomial distance-regular graph.

For the deﬁnition of a thin Q-polynomial distance-regular graph, see Appendix A.

Lemma 6.1 (cf. [88, Theorem 77]). Let G be a thin Q-polynomial distance-regular graph with

diameter D ≥ 5. Then there exists a non-negative integer c such that for each vertex x of G,

the local graph ∆G(x) at x is co-edge regular with parameters (k, a1, c). Moreover, the local graph

∆G(x) at x has at most 5 distinct eigenvalues.

The second result shows a relation between the second largest eigenvalue of a distance-regular

graph and the smallest eigenvalue of its local graph at any vertex.

Lemma 6.2 (cf. [12, Theorem 4.4.3]). Let G be a distance-regular graph with diameter D ≥ 3

and second largest eigenvalue λ1. Then for each vertex x of G, the local graph ∆G(x) at x has the

smallest eigenvalue at least − b1
λ1+1 − 1.

Now we present an important tool shown by Yang and Koolen [95], by using Hoﬀman graphs.

Proposition 6.3 ( [95, Proposition 1.3]). Let λ ≥ 2 be a real number. Then there exists a constant

M1(λ) ≥ λ3 such that, if a graph G satiﬁes

(i) every pair of vertices at distance 2 has at least M1(λ) common neighbors, and

29

(ii) λmin(G) ≥ −λ,

then G has diameter 2 and for each x, the number of vertices at distance 2 to x is at most

⌊λ⌋⌊(λ − 1)2⌋.

Next we give an upper bound on the parameter c for co-edge regular graphs in terms of its

smallest eigenvalue, due to Yang and Koolen [95]. They showed the following:

Theorem 6.4 ( [95, Theorem 7.1]). Let λ ≥ 2 be a real number. There exists a real number M2(λ)

such that, for any connected co-edge regular graph G with parameters (n, k, c), if λmin(G) ≥ −λ,

then c > M2(λ) implies that n − k − 1 ≤ (λ−1)2
4 + 1 holds.

Their proof used Proposition 6.3 and the Alon-Boppana Theorem. Later Koolen, Gebremichel

and Yang [57] observed that this result is also true when the condition co-edge regular is replaced

by sesqui-regular, which we are going to introduce. A k-regular graph of order n is called sesqui-

regular with parameters (n, k, c), if every pair of vertices at distance 2 has exactly c common

neighbors.

They further extended this result as follows:

Theorem 6.5. Let λ ≥ 2 be an integer. There exists a constant C4(λ) such that, for any sesqui-

regular graph G with parameters (n, k, c), if λmin(G) ≥ −λ and k ≥ C4(λ), then one of the following

holds:

(i) c ≤ λ2(λ − 1),

(ii) n − k − 1 ≤ (λ−1)2
4 + 1.

Remark 6.6. (i) The block graph of a Steiner system S(2, t, v) is strongly regular with param-

eters ( v(v−1)
t(t−1) , t(v−t)
t−1 , (t − 1)2 + v−1
t−1 − 2, t2) and smallest eigenvalue −t. This shows that the

bound in the ﬁrst item of the above theorem can not be improved too much.

(ii) There exists an inﬁnite family of bipartite Ramanujan graphs with valency k and unbounded

number of vertices, which were found by Marcus et al. [71], as we already discussed in Section

1.1. Let G be a graph in this family, say of order n. Consider the complement G of G. Then

the following holds:

(a) G has valency n − k − 1;

(b) G has smallest eigenvalue at least −1 − 2
√k − 1 as G has second largest eigenvalue at

most 2
√k − 1.

This shows that the bound in the second item of Theorem 6.5 is tight.

30

(iii) In [56], it is shown that for λ = 3, one can improve the bound in the ﬁrst item of the above

theorem to λ2. Whether this is true for general λ, it is not known.

Now we give some spectral characterizations of some families of graphs under the extra as-

sumption that the graphs are co-edge regular. Hayat, Koolen and Riaz [47] showed the following

result for the clique-extensions of the square grid graphs.

Theorem 6.7 ( [47, Theorem 1.1]). Let G be a co-edge regular graph with spectrum
{(s(2t + 1) − 1
)1, (st − 1)
2t, (−1)
(s−1)(t+1)2 , (−s − 1)
t2 } ,

where s ≥ 2, t ≥ 1 are integers. If t ≥ 11(s + 1)3(s + 2), then G is the s-clique extension of the

((t + 1) × (t + 1))-grid.

Tan, Koolen and Xia [83] showed a similar result for the clique-extensions of triangular graphs:

Theorem 6.8 ( [83, Theorem 1]). Let G be a co-edge regular graph with spectrum
{
(2sv − 3s − 1)
1, (sv − 3s − 1)
v−1, (−s − 1) v2 −3v
2 , (−1) (s−1)v(v−1)
2 } ,

where s ≥ 2 and v ≥ 1 are integers. If v ≥ 48s, then G is the s-clique extension of the triangular

graph T (v).

Remark 6.9. (i) Note that to prove both Theorems 6.7 and 6.8, they used the claw-clique

method of Bose and Laskar.

(ii) Using the method in [83], one could improve the bound t ≥ 11(s + 1)3(s + 2) of Theorem 6.7.

Tan et al. [83] also gave the following conjecture:

Conjecture 6.10 ( [83, Conjecture 3]). Let G be a connected co-edge regular graph with parameters

(n, k, c) having four distinct eigenvalues. Let λ ≥ 2 be an integer. Then there exists a constant

n2(λ) such that, if λmin(G) ≥ −λ, n ≥ n2(λ) and k < n − 2 − (λ−1)2

4 , then either G is the s-clique

extension of a strongly regular graph for 2 ≤ s ≤ λ − 1 or G is a (p × q)-grid with p > q ≥ 2.

Yang, Abiad and Koolen [96] showed the following spectral characterization of 2-clique ex-

tensions of the square grid graphs, using Hoﬀman graphs. They did not need the assumption of

co-edge regularity, but they needed a very large lower bound on the valency.

Theorem 6.11 ( [96, Theorem 1]). The 2-clique extension of the (t × t)-grid is characterized by

its spectrum if t is large enough.

In their proof, they used the following result of Koolen et al. [64].

Theorem 6.12 ( [64, Theorem 1.8]). There exists a positive integer t such that for each pair

(t1, t2) with t1 ≥ t2 ≥ t, any graph that is cospectral to the 2-clique extension of the (t1 × t2)-grid

is the slim graph of a 2-fat { , , }-line Hoﬀman graph.

31

7 Signed graphs

7.1 Deﬁnitions

Deﬁnition 7.1 (signed graph). A signed graph (G, τ ) is a pair of a graph G = (V (G), E(G)) and

a signing τ : E(G) → {+1, −1}.

The adjacency matrix A(G, τ ) of the signed graph (G, τ ) is the symmetric matrix whose rows

and columns are indexed by V (G) such that A(G, τ )x,y = τ ({x, y}) if {x, y} is an edge of G and 0

otherwise.

A real number λ is an eigenvalue of (G, τ ), if λ is an eigenvalue of its adjacency matrix A(G, τ ).

The spectrum of (G, τ ) is the spectrum of A(G, τ ). In a similar fashion, we denote by λmin(G, τ )

the smallest eigenvalue of the signed graph (G, τ ).

For ε ∈ {+, −}, the ε-graph of (G, τ ) is the graph (G, τ )ε with vertex set V (G) and edge set

Eε, where Eε = {e ∈ E(G) | τ (e) = ε1}. We also represent the signed graph (G, τ ) by the triple

(V (G), E+, E−).

Two signed graphs (G, τ ) and (H, ξ) are switching equivalent if there exist a permutation matrix

P and a diagonal matrix D with diagonal entries in {−1, +1} such that P A(G, τ )P T = DA(H, ξ)D

holds.

7.2 Seidel matrices

In this subsection, we introduce and study Seidel matrices.

Deﬁnition 7.2 (Seidel matrix). (i) A Seidel matrix S of order n is a symmetric (0, ±1)-matrix

with 0 on the diagonal and ±1 otherwise.

(ii) Let G be a graph. The Seidel matrix S(G) of G is the matrix J − I − 2A(G), where A(G)

is the adjacency matrix of G.

Note that the Seidel matrix S(G) of a graph G of order n is the adjacency matrix of the signed

graph (Kn, τG) satisfying (Kn, τG)− = G. Therefore, for a given graph G of order n, we denote by

(Kn, τG) the signed graph with S(G) as its adjacency matrix. Two graphs G and H of order n are

called switching equivalent if the signed graphs (Kn, τG) and (Kn, τH) are switching equivalent.

If the graphs G and H are switching equivalent, then there exists a subset V ′ of the vertex set

V (G) of G, such that the resulting graph, by changing all the edges between V ′ and V (G) − V ′

to non-edges, and all the non-edges between V ′ and V (G) − V ′ to edges, is H. This operation is

called switching on the subset V ′.
 32

Note that switching equivalence is an equivalence relation. The equivalence class of G is called

the switching class of G and is denoted by [G]. If H ∈ [G], the matrices S(H) and S(G) are similar

and hence have the same spectrum.

The motivation to study Seidel matrix with ﬁxed smallest eigenvalue with large multiplicity

comes from the study of equiangular lines in the Euclidean space.

Deﬁnition 7.3 (equiangular lines). A system of lines through the origin in the r-dimensional

Euclidean space Rr is called equiangular if the angle between any pair of lines is the same.

Seidel matrices and systems of equiangular lines, are related as follows (see for example, [43,

Section 11.1]):

Proposition 7.4. Let n > r ≥ 2 be integers. There exists a system of n equiangular lines in Rr

with common angle arccos α if and only if there exists a Seidel matrix S of order n such that S

has smallest eigenvalue at least − 1
α and rank(S + 1
α I) ≤ r.

We are going to use the theory of Hoﬀman graphs to study Seidel matrices with ﬁxed smallest

eigenvalue. Our approach is diﬀerent from, but closely related to the approach of Balla, Dr¨axler,

Keevash and Sudakov [5, Section 2].

Let S be a Seidel matrix of order n. The graph G+(S) is the graph with adjacency matrix

1
2 (S + J − I). If λmin(S) = 2λ + 1, then λmin(G+(S)) ≥ λ. Note that for each graph in [G+(S)],

its smallest eigenvalue is at least λ. Let C be a clique of order q in H ∈ [G+(S)]. If necessary, by

switching, we can obtain a graph in [G+(S)] such that C is still a clique and every vertex outside

C has at least q/2 neighbors in C. We denote such a graph by HC.

Theorem 7.5. Let λ ≤ −2 be a real number and r a positive integer. Let m be such that the

smallest eigenvalue of ̃K2m is less than λ. Then there exists a positive integer Q = Q(λ, m, r) ≥

(m + 1)2 such that for each integer q ≥ Q and each Seidel matrix S with λmin(S) ≥ 2λ + 1, if

a graph H ∈ [G+(S)] contains a clique C of order at least q, then the associated Hoﬀman graph

g = g(HC, m, q) is (r, λ)-nice and has exactly one fat vertex and this fat vertex is adjacent to all

slim vertices.

Moreover there exists a positive integer n = n(λ, q) such that if the order of the Seidel matrix

S is at least n, then every graph in [G+(S)] contains a clique of order at least q.

Proof . Let Q := Q(λ, m, r) be the integer such that Theorem 4.3 holds. Let q ≥ Q. Suppose

a graph H ∈ [G+(S)] has a clique C of order at least q. Without loss of generality, we may

assume C is a maximal clique in H. Now we look at a graph HC. It is known that all vertices

outside C have at least q/2 neighbors in C. We claim that every vertex outside C has at most

m − 1 non-neighbors in C. Suppose this is not the case, and the vertex x outside C has at least

33

m non-neighbors in C. Then we can ﬁnd m vertices y1, y2, . . . , ym in C which are not adjacent

to x. Since x also has at least q/2 neighbors in C, where q/2 ≥ (m + 1)2/2 ≥ m, we can ﬁnd

z1, z2, . . . , zm in C which are adjacent to x. It is not hard to see that the subgraph of HC induced

on {x, y1, y2, . . . , ym, z1, z2, . . . , zm} is ̃K2m, which has smallest eigenvalue less than λ. This is not

possible, as λmin(HC) ≥ λ. Hence, the claim holds, and under the equivalence relation ≡m
q , the

set of maximal cliques in HC of order at least q has exactly one equivalence class, which consists

of all vertices of HC. This means that the associated Hoﬀman graph g(HC, m, q) has exactly

one fat vertex and this fat vertex is adjacent to all the slim vertices of g(HC, m, q). Considering

q ≥ Q(λ, m, r), we have that g(HC, m, q) is (r, λ)-nice by Theorem 4.3.

Let n := R(q, ⌈−2λ⌉ + 1), where R(q, ⌈−2λ⌉ + 1) is the Ramsey number. For a graph H ′ ∈

[G+(S)] with Seidel matrix S(H ′), we claim that H ′ does not contain a stable set of size ⌈−2λ⌉+ 1.

Otherwise, the matrix S(H ′) contains a ((⌈−2λ⌉+1)×(⌈−2λ⌉+1)) principal submatrix J⌈−2λ⌉+1 −

I⌈−2λ⌉+1. In other words, the matrix −S(H ′) contains a principal submatrix −J⌈−2λ⌉+1 + I⌈−2λ⌉+1.

Note that the matrix −S(H ′) has the same spectrum as S. Thus

⌈2λ⌉ = λmin(−J⌈−2λ⌉+1 + I⌈−2λ⌉+1) ≥ λmin(−S(H ′)) ≥ 2λ + 1,

which gives a contradiction. (For the ﬁrst inequality, see [42, Theorem 9.1.1].) Therefore, our

claim holds and by Ramsey theory, the graph H ′ contains a clique of order q.

This completes the proof.

7.3 Signed graphs

Following a straightforward way, the notion of the s-integrability of graphs can be extended to

signed graph. For a positive integer s, we say that a signed graph (G, τ ) with smallest eigenvalue

λmin(G, τ ) is s-integrable, if there exists an integral matrix N such that the equality

s(A(G, τ ) + ⌈−λmin(G, τ )⌉I) = N T N

holds, where A(G, τ ) is the adjacency matrix of (G, τ ).

Not so much is known about signed graphs with ﬁxed smallest eigenvalue. Using the same

proof as in Theorem 2.1 one can show:

Theorem 7.6 ( [10, Theorem 3.13]). If (G, τ ) is a connected signed graph with λmin(G, τ ) ≥ −2,

then (G, τ ) is s-integrable for s ≥ 2. Moreover, if (G, τ ) has at least 121 vertices, then (G, τ ) is

1-integrable.

Theorem 2.4 (i) has been extended to the class of signed graphs by Gavrilyuk, Munemasa,

Sano and Taniguchi [41] as follows.
 34

Theorem 7.7. For any real number λ ∈ (−2, −1], there exists a constant C5(λ) such that if (G, τ )

is a connected signed graph on n vertices with λmin(G, τ ) ≥ λ and minimal valency at least C5(λ),

then λmin(G, τ ) = −1 and (G, τ ) is switching equivalent to (Kn, +), and hence is 1-integrable.

8 Future work

At the end of this survey, we give some problems for discussion.

8.1 Problems on graphs and signed graphs

First we discuss unsigned graphs. As a generalization of Theorem 2.2, we have

Problem 8.1 ( [63, Conjecture 3.2]). There exist constants κ5 and s1 such that, for any graph G

with λmin(G) ≥ −4 and minimal valency at least κ5, G is s1-integrable.

To solve this problem, we have to have a good understanding of fat Hoﬀman graphs with

smallest eigenvalue at least −4. The ﬁrst step is to look at the family H of indecomposable fat

Hoﬀman graphs with smallest eigenvalue at least −4, in which every slim vertex has exactly one

fat neighbor and any two distinct slim vertices have no common fat neighbor. Note that for any

Hoﬀman graph in H, its slim graph is a connected graph with smallest eigenvalue at least −3.

Therefore, as a subproblem of Problem 8.1, we have

Problem 8.2 ( [63, Conjecture 3.1]). There exists a constant s2 such that, for any graph G with

λmin(G) ≥ −3, G is s2-integrable.

In [61], Koolen et al. showed that the complement of the McLaughlin graph has smallest

eigenvalue −3 and can not be 2-integrated, but it is 4-integrable. It is not clear whether any graph

with smallest eigenvalue at least −3 is always 4-integrable. The situation for graphs with smallest

eigenvalue at least −3 is diﬀerent from the situation for graphs with smallest eigenvalue at least

−2, as there exists an inﬁnite family of connected graphs with unbounded vertices such that none

of them can be 2-integrated (see [62, Remark 1.4 (v)]).

As a special case, we look at the integrability of trees with smallest eigenvalue at least −3.

Problem 8.3. Is it true that any tree with smallest eigenvalue at least −3 is 2-integrable?

In [60], Koolen, Rehman and Yang characterized 1-integrable trees with smallest eigenvalue at

least −3.

For signed graphs we propose the following problems.

Problem 8.4. For any real number λ ∈ (−1 − √2, −2], there exists a constant C6(λ) such that, if

(G, τ ) is a signed graph with λmin(G, τ ) ≥ λ and minimal valency at least C6(λ), then λmin(G, τ ) =

−2 and (G, τ ) is 1-integrable.
 35

Problem 8.5. There exists a constant κ6 such that, if (G, τ ) is a signed graph with λmin(G, τ ) ≥

−3 and minimal valency at least κ6, then (G, τ ) is s-integrable for any s ≥ 2.

To solve above two problems, one problem to overcome is how to deal with switching classes of

signed graphs. Is there a natural generalization of Hoﬀman graphs to the class of signed graphs?

In [41], they considered a generalization of line Hoﬀman graphs. For more problems on graphs and

signed graphs with ﬁxed smallest eigenvalue, see [63]. For more general problems on the spectral

theory of signed graphs, see [10].

8.2 Reﬁning ̃K2t

Denote by H(a, t) the graph on a + t + 1 vertices consisting of a clique Ka+t together with a

vertex that is adjacent to precisely a vertices of this clique. Note that ̃K2t is exactly the graph

H(t, t).

In [46], Greaves, Koolen, and Park showed the following.

Lemma 8.6. Let G be a graph having smallest eigenvalue −m that contains H(a, t) as an induced

subgraph. Then
 (a − m(m − 1))(t − (m − 1)
2) ⩽ (m(m − 1))
2. (5)

Using the above result, they obtain bounds on the clique order in strongly regular graphs.

Their result can also be extended to other classes of graphs, for example, distance-regular graphs.

Lemmens and Seidel [68] conjectured that for each Seidel matrix S of order n, the rank of the

matrix S + 5I is at least ⌊ 2n
3 ⌋ + 1. This was shown to be true by Cao, Koolen, Lin and Yu [16].

Their main tool is to use the Seidel matrices of the complements of H(a, t)’s as minimal forbidden

principal submatrices.

Acknowledgments

J.H. Koolen is partially supported by the National Natural Science Foundation of China (No.

12071454) and Anhui Initiative in Quantum Information Technologies (No. AHY150000).

Q. Yang is partially supported by the Fellowship of China Postdoctoral Science Foundation

(No. 2020M671855).

We greatly thank Prof. Min Xu for supporting M.-Y. Cao to visit University of Science and

Technology of China.

We are also grateful to Prof. Sebastian M. Cioab˘a, Prof. Akihiro Munemasa, Dr. Jongyook

Park and Mr. Kiyoto Yoshino for their careful reading and valuable comments.

36

Appendix A. Q-polynomial distance-regular graphs

Let V denote a non-empty ﬁnite set. Let MatV (C) denote the C-algebra consisting of all

complex matrices whose rows and columns are indexed by V . Let U = CV denote the C-vector

space consisting of all complex vectors indexed by V . We endow U with standard Hermitian inner

product (u, v) = uT v for u, v ∈ U. We view U as a left module for MatV (C), called the standard

module.

Let G be a distance-regular graph of diameter D. Let V be the vertex set of G. For 0 ≤ i ≤ D,

let Ai denote the matrix in MaxV (C) deﬁned by

(Ai)x,y =
 


 1 if d(x, y) = i,

0 otherwise,

where x, y ∈ V . We call Ai the ith distance matrix of G. We abbreviate A := A1. Observe that

(1a) A0 = I;

(1b) ∑D
i=0 Ai = J, the all-ones matrix;

(1c) each Ai is real symmetric;

(1d) there exist ph
ij for 0 ≤ i, j, h ≤ D, such that AiAj = AjAi = ∑D
h=0 ph
ijAh hold.

Notice that (1a) implies for each pair vertices x, y ∈ V with d(x, y) = h, the equality |Gi(x) ∩

Gj(y)| = ph
ij holds. Therefore, for all integers 0 ≤ h, i, j ≤ D, ph
ij = 0 (resp. ph
ij ̸= 0) if one

of h, i, j is greater than (resp. equal to) the sum of the other two. By these facts, we ﬁnd that

A0, A1, . . . , AD is a basis for a commutative subalgebra M of MatV (C), which we call the Bose-

Mesner algebra of G. It is known that A generates M , as AAi = ci+1Ai+1 + aiAi + bi−1Ai−1

(0 ≤ i ≤ D) by condition (iv), where {b0, b1, . . . , bD−1; c1, c2, . . . , cD} is the intersection array of G.

The algebra M has a second basis E0, E1, . . . , ED such that

(2a) E0 = |V |−1J,

(2b) ∑D
i=0 Ei = I,

(2c) each Ei is real symmetric,

(2d) EiEj = EjEi = δijEi

(see [12, p. 45]). We call Ei the ith primitive idempotent of G. Since {Ei}D
i=0 is a basis for M ,

there exist complex scalars {θi}D
i=0 such that A = ∑D
i=0 θiEi. (Note that {θi}D
i=0 are exactly all of

the distinct eigenvalues of G and they are real.) Observe AEi = EiA = θiEi for 0 ≤ i ≤ D. We

call θi the eigenvalue of G associated with Ei for 0 ≤ i ≤ D. Observe U = E0U⊕ E1U⊕ · · · ⊕ EDU,

37

an orthogonal direct sum. For 0 ≤ i ≤ D, EiU is the eigenspace of A associated with θi. Denote

by mi the rank of Ei and observe mi = dim(EiU), the multiplicity of the eigenvalue θi.

We now introduce the notion of Q-polynomial property of G. Let ◦ denote the entrywise

product in MatV (C). Since Ai ◦ Aj = δijAi, the Bose-Mesner algebra M is closed under ◦. Also

as {Ei}D
i=0 is a basis for M , there exist complex scalars qh
ij such that

Ei ◦ Ej = |V |
−1 D∑

h=0 qh
ijEh.

By [12, p. 48, p. 49], the scalars qh
ij are real and non-negative. We say G is Q-polynomial (with

respect to the given ordering E0, E1, . . . , ED) whenever for all integers 0 ≤ h, i, j ≤ D, qh
ij = 0

(resp. qh
ij ̸= 0) if one of h, i, j is greater than (resp. equal to) the sum of the other two [12, p. 235].

We assume G is Q-polynomial with respect to the ordering E0, E1, . . . , ED. Fix a vertex

x ∈ V . We refer to x as a “base” vertex. For 0 ≤ i ≤ D, we deﬁne the diagonal matrix

E∗
i = E∗
i (x) ∈ MatV (C) with diagonal entry

(E∗
i )y,y =
 


 1 if d(x, y) = i,

0 otherwise,

where y ∈ V . We call E∗
i the ith dual primitive idempotent of G with respect to x. Observe

(3a) ∑D
i=0 E∗
i = I,

(3b) each E∗
i is real symmetric,

(3c) E∗
i E∗
j = δijE∗
i .

By these facts, E∗
0 , E∗
1 , . . . , E∗
D is a basis for a commutative subalgebra M ∗ of MatV (C), which we

call the dual Bose-Mesner algebra of G.

Deﬁne the diagonal matrix A∗
i = A∗
i (x) ∈ MatV (C) with diagonal entry (A∗
i )y,y = |V |(Ei)x,y

for y ∈ V . By [87, p. 379], A∗
0, A∗
1, . . . , A∗
D is also a basis for M ∗, and moreover

(4a) A∗
0 = I,

(4b) ∑D
i=0 A∗
i = |V |E∗
0 ,

(4c) each A∗
i is real and symmetric,

(4d) A∗
i A∗
j = A∗
j A∗
i = ∑D
h=0 qh
ijA∗
h.

We call A∗
i the ith dual distance matrix of G with respect to x. We abbreviate A∗ = A∗
1, called

the dual adjacency matrix of G with respect to x. From conditions (4a) and (4d), we ﬁnd that

the matrix A∗ generates M ∗. Since {E∗
i }D
i=0 is a basis for M ∗, there exist complex scalars {θ∗
i }D
i=0

38

such that A∗ = ∑D
i=0 θ∗
i E∗
i . Observe A∗E∗
i = E∗
i A∗ = θ∗
i E∗
i for 0 ≤ i ≤ D. The scalars {θ∗
i }D
i=0

are real [87, Lemma 3.11] and mutually distinct. We call θ∗
i the dual eigenvalue of G associated

with E∗
i . Observe U = E∗
0 U ⊕ E∗
1U ⊕ · · · ⊕ E∗
DU, an orthogonal direct sum. For 0 ≤ i ≤ D, the

space E∗
i U is the eigenspace of A∗ associated with θ∗
i .

Let T = T (x) denote the subalgebra of MatV (C) generated by M and M ∗. We call T the

Terwilliger algebra (or subconstituent algebra) of G with respect to x [87]. Note that A and A∗(x)

generates T . The algebra T is ﬁnite dimensional and non-commutative. It is also semi-simple since

it is closed under conjugate and transpose map. The following are relations in T [87, Lemma 3.2].

For 0 ≤ h, i, j ≤ D,
 E∗
i AhE∗
j = 0 if and only if ph
ij = 0,

EiA
∗
hEj = 0 if and only if qh
ij = 0.

Note that T may depend on the choice of the base vertex (see [8]).

By a T -module, we mean a subspace W of U such that BW ⊆ W for all B ∈ T . Observe that

U is a T -module, called the standard module of T (or standard T -module). A T -module is called

irreducible if it contains no T -submodule except itself and zero module.

Let W be a T -module and W1 a T -submodule of W. Then the orthogonal complement of W1 in

W is a T -module, since T is closed under conjugate transpose map. It follows that W decomposes

into an orthogonal direct sum of irreducible T -modules.

Let W denote an irreducible T -module. Then W decomposes into a direct sum of nonzero

spaces among E∗
i W , 0 ≤ i ≤ D. By the endpoint of W , we mean min{i | 0 ≤ i ≤ D, E∗
i W ̸= 0}.

By the diameter of W , we mean |{i | 0 ≤ i ≤ D, E∗
i W ̸= 0}| − 1. Let r denote the endpoint of W

and d the diameter of W . By [87, Lemma 3.9], we have (i) E∗
i W ̸= 0 if and only if r ≤ i ≤ r + d;

(ii) W = ⊕d
h=0 E∗
r+hW , an orthogonal direct sum. An irreducible T -module W is said to be thin

whenever dim(E∗
i W ) ≤ 1 for 0 ≤ i ≤ D. There exists a unique thin irreducible T -module with

endpoint 0 and diameter D, which we call it the primary T -module. The primary T -module has

a basis E∗
0 j, . . . , E∗
Dj [87, Lemma 3.6], where j is the all-ones vector.

The graph G is said to be thin with respect to x whenever every irreducible T (x)-module is

thin. The graph G is said to be thin whenever G is thin with respect to every vertex x of G.

See [89, Section 6] for examples of thin Q-polynomial distance-regular graphs.

References

[1] R. Aharoni, N. Alon, and E. Berger. Eigenvalues of K1,k-free graphs and the connectivity of

their independence complexes. J. Graph Theory, 83(4):384–391, 2016.

39

[2] M. Ajtai, J. Koml´os, and E. Szemer´edi. Sorting in c log n parallel steps. Combinatorica,

3(1):1–19, 1983.

[3] N. Alon. Eigenvalues and expanders. Combinatorica, 6(2):83–96, 1986.

[4] N. Alon and F. R. K. Chung. Explicit construction of linear sized tolerant networks. Discrete

Math., 72(1–3):15–19, 1988.

[5] I. Balla, F. Dr¨axler, P. Keevash, and B. Sudakov. Equiangular lines and spherical codes in

Euclidean space. Invent. Math., 211:179–212, 2018.

[6] S. Bang. Diameter bounds for geometric distance-regular graphs. Discrete Math., 341(1):253–

260, 2018.

[7] S. Bang, A. Dubickas, J. H. Koolen, and V. Moulton. There are only ﬁnitely many distance-

regular graphs of ﬁxed valency greater than two. Adv. Math., 269:1–55, 2015.

[8] S. Bang, T. Fujisaki, and J. H. Koolen. The spectra of the local graphs of the twisted

Grassmann graphs. European J. Combin., 30(3):638–654, 2009.

[9] S. Bang, E. R. van Dam, and J. H. Koolen. Spectral characterization of the Hamming graphs.

Linear Algebra Appl., 429(11–12):2678–2686, 2008.

[10] F. Belardo, S. M. Cioab˘a, J. H. Koolen, and J. F. Wang. Open problems in the spectral

theory of signed graphs. Art Discrete Appl. Math., 1(2):#P2.10, 2018.

[11] Y. Bramoull´e, R. Kranton, and M. D’Amours. Strategic interaction and networks. Am. Econ.

Rev., 104(3):898–930, 2014.

[12] A. E. Brouwer, A. M. Cohen, and A. Neumaier. Distance-Regular Graphs. Springer-Verlag

Berlin Heidelberg, 1989.

[13] A. E. Brouwer and W. H. Haemers. Spectra of Graphs. Springer Heidelberg, 2012.

[14] F. C. Bussemaker and A. Neumaier. Exceptional graphs with smallest eigenvalue −2 and

related problems. Math. Comp., 59(200):583–608, 1992.

[15] P. J. Cameron, J. M. Goethals, J. J. Seidel, and E. E. Shult. Line graphs, root systems, and

elliptic geometry. J. Algebra, 43:305–327, 1976.

[16] M.-Y. Cao, J. H. Koolen, Y.-C. R. Lin, and W.-H. Yu. The Lemmens-Seidel conjecture and

forbidden subgraphs. arXiv:2003.07511v1, 2020.

40

[17] X.-M. Cheng, A. L. Gavrilyuk, G. R. W. Greaves, and J. H. Koolen. Biregular graphs with

three eigenvalues. European J. Combin., 56:57–80, 2016.

[18] X.-M. Cheng, G. R. W. Greaves, and J. H. Koolen. Graphs with three eigenvalues and second

largest eigenvalue at most 1. J. Combin. Theory Ser. B, 129:55–78, 2018.

[19] X.-M. Cheng and J. H. Koolen. A generalization of a theorem of Neumaier. Des. Codes

Cryptogr., 84:135–142, 2017.

[20] M. Chudnovsky and P. Seymour. The structure of claw-free graphs. Surveys in Combinatorics,

London Math. Soc. Lecture Note Ser., 327:153–172, 2005.

[21] M. Chudnovsky and P. Seymour. Claw-free graphs. I. Orientable prismatic graphs. J. Combin.

Theory Ser. B, 97(6):867–903, 2007.

[22] M. Chudnovsky and P. Seymour. Claw-free graphs. II. Non-orientable prismatic graphs. J.

Combin. Theory Ser. B, 98(2):249–290, 2008.

[23] M. Chudnovsky and P. Seymour. Claw-free graphs. III. Circular interval graphs. J. Combin.

Theory Ser. B, 98(4):812–834, 2008.

[24] M. Chudnovsky and P. Seymour. Claw-free graphs. IV. Decomposition theorem. J. Combin.

Theory Ser. B, 98(5):839–938, 2008.

[25] M. Chudnovsky and P. Seymour. Claw-free graphs. V. Global structure. J. Combin. Theory

Ser. B, 98(6):1373–1410, 2008.

[26] M. Chudnovsky and P. Seymour. Claw-free graphs. VI. Colouring. J. Combin. Theory Ser.

B, 100(6):560–572, 2010.

[27] M. Chudnovsky and P. Seymour. Claw-free graphs. VII. Quasi-line graphs. J. Combin. Theory

Ser. B, 102(6):1267–1294, 2012.

[28] S. M. Cioab˘a, R. J. Elzinga, and D. A. Gregory. Some observations on the smallest adjacency

eigenvalue of a graph. Discuss. Math. Graph Theory, 40(2):467–493, 2020.

[29] S. M. Cioab˘a, J. H. Koolen, and W. Li. Disconnecting strongly regular graphs. European J.

Combin., 38:1–11, 2014.

[30] S. M. Cioab˘a, J. H. Koolen, and H. Nozaki. A spectral version of the Moore problem for

bipartite regular graphs. Algebr. Comb., 2(6):1219–1238, 2019.

[31] J. H. Conway and N. J. A. Sloane. Low-dimensional lattices V. Integral coordinates for integral

lattices. Proc. R. Soc. Lond. A, 426:211–232, 1989.

41

[32] D. Cvetkovi´c, M. Doob, and S. Simi´c. Generalized line graphs. J. Graph Theory, 5(4):385–399,

1981.

[33] D. Cvetkovi´c, P. Rowlinson, and S. Simi´c. Spectral Generalizations of Line Graphs: On Graphs

with Least Eigenvalue −2. Cambridge Univ. Press, Cambridge, 2004.

[34] D. Cvetkovi´c, P. Rowlinson, and S. Simi´c. Graphs with least eigenvalue −2: Ten years on.

Linear Algebra Appl., 484:504–539, 2015.

[35] W. Ebeling. Lattices and Codes: A Course Partially Based on Lectures by F. Hirzebruch.

Friedr. Vieweg & Sohn, Braunschweig, 1994.

[36] J. Friedman. A proof of Alon’s second eigenvalue conjecture and related problems. Mem.

Amer. Math. Soc., 195(910):100pp, 2008.

[37] M. Furuya, S. Kubota, T. Taniguchi, and K. Yoshino. The uniqueness of covers for widely

generalized line graphs. arXiv:2002.08049v1, 2020.

[38] A. L. Gavrilyuk and J. H. Koolen. On a characterization of the Grassmann graphs.

arXiv:1806.02652v1, 2018.

[39] A. L. Gavrilyuk and J. H. Koolen. A characterization of the graphs of bilinear (d × d)-forms

over F2. Combinatorica, 39(2):289–321, 2019.

[40] A. L. Gavrilyuk and J. H. Koolen. On some recent progress in the classiﬁcation of (P and

Q)-polynomial association schemes. Arab. J. Math., 2019.

[41] A. L. Gavrilyuk, A. Munemasa, Y. Sano, and T. Taniguchi. Signed analogue of line graphs

and their smallest eigenvalues. arXiv:2003.05578v1, 2020.

[42] C. Godsil and K. Meagher. Erd˝os–Ko–Rado Theorems: Algebraic Approaches. Cambridge

University Press, Cambridge, 2016.

[43] C. Godsil and G. Royle. Algebraic Graph Theory. Springer-Verlag, Berlin, 2001.

[44] C. D. Godsil. Geometric distance-regular covers. New Zealand J. Math., 22:31–38, 1993.

[45] G. Greaves, J. Koolen, A. Munemasa, Y. Sano, and T. Taniguchi. Edge-signed graphs with

smallest eigenvalue greater than −2. J. Combin. Theory Ser. B, 110:90–111, 2015.

[46] G. Greaves, J. H. Koolen, and J. Park. Improving the Delsarte bound. Manuscript, 2020.

[47] S. Hayat, J. H. Koolen, and M. Riaz. A spectral characterization of the s-clique extension of

the square grid graphs. European J. Combin., 76:104–116, 2019.

42

[48] A. J. Hoﬀman. On spectrally bounded graphs. A Survey of Combinatorial Theory, pp. 277–

283, 1973.

[49] A. J. Hoﬀman. On graphs whose least eigenvalue exceeds −1 − √
2. Linear Algebra Appl.,

16:153–165, 1977.

[50] T. Høholdt and J. Justesen. On the sizes of expander graphs and minimum distances of graph

codes. Discrete Math., 325:38–46, 2014.

[51] S. Hoory, N. Linial, and A. Wigderson. Expander graphs and their applications. Bull. Amer.

Math. Soc. (N.S.), 43(4):439–561, 2006.

[52] H. J. Jang, J. Koolen, A. Munemasa, and T. Taniguchi. On fat Hoﬀman graphs with smallest

eigenvalue at least −3. Ars Math. Contemp., 7(1):105–121, 2014.

[53] D. Jungnickel and V. D. Tonchev. Polarities, quasi-symmetric designs, and Hamada’s conjec-

ture. Des. Codes Cryptogr., 51(2):131–140, 2009.

[54] H. K. Kim, J. H. Koolen, and J. Y. Yang. A structure theory for graphs with ﬁxed smallest

eigenvalue. Linear Algebra Appl., 540:1–13, 2016.

[55] J. H. Koolen and S. Bang. On distance-regular graphs with smallest eigenvalue at least −m.

J. Combin. Theory Ser. B, 100:573–584, 2010.

[56] J. H. Koolen, B. Gebremichel, M. U. Rehman, J. Y. Yang, and Q. Yang. Sesqui-regular graphs

with smallest eigenvalue at least −3. In preparation.

[57] J. H. Koolen, B. Gebremichel, and J. Y. Yang. Sesqui-regular graphs with ﬁxed smallest

eigenvalue. arXiv:1904.01274v1, 2019.

[58] J. H. Koolen, Y.-R. Li, and Q. Yang. On fat Hoﬀman graphs with smallest eigenvalue at least

−3, part II. Linear Algebra Appl., 550:121–143, 2018.

[59] J. H. Koolen and A. Munemasa. The regular two-graph on 276 vertices revisited. Manuscript,

2020.

[60] J. H. Koolen, M. U. Rehman, and Q. Yang. The integrally representable trees of norm 3.

Ann. Math. Sci. Appl., 2(2):385–408, 2017.

[61] J. H. Koolen, M. U. Rehman, and Q. Yang. On the integrability of strongly regular graphs.

Graphs Combin., 35:1273–1291, 2019.

[62] J. H. Koolen, J. Y. Yang, and Q. Yang. On graphs with smallest eigenvalue at least −3 and

their lattices. Adv. Math., 338:847–864, 2018.

43

[63] J. H. Koolen and Q. Yang. Problems on graphs with ﬁxed smallest eigenvalue. Algebra Colloq.,

27(1):51–54, 2020.

[64] J. H. Koolen, Q. Yang, and J. Y. Yang. A generalization of a theorem of Hoﬀman. J. Combin.

Theory Ser. B, 135:75–95, 2019.

[65] J. Krausz. D´emonstration nouvelle d’une th´eor`eme de Whitney sur les r´eseaux (Hungarian).

Mat. Fiz. Lapok, 50:75–85, 1943.

[66] M. Krivelevich and B. Sudakov. Pseudo-random graphs. More sets, graphs and numbers,

Bolyai Soc. Math. Stud., 15:199–262, 2006.

[67] S. Kubota, T. Taniguchi, and K. Yoshino. On graphs with the smallest eigenvalue at least

−1 − √2, part III. Ars Math. Contemp., 17(2):555–579, 2019.

[68] P. W. H. Lemmens and J. J. Seidel. Equiangular lines. J. Algebra, 24(3):494–512, 1973.

[69] W.-C. W. Li and P. Sol´e. Spectra of regular graphs and hypergraphs and orthogonal polyno-

mials. European J. Combin., 17(5):461–477, 1996.

[70] A. Lubotzky, R. Phillips, and P. Sarnak. Ramanujan graphs. Combinatorica, 8(3):261–277,

1988.

[71] A. W. Marcus, D. A. Spielman, and N. Srivastava. Interlacing families I: Bipartite Ramanujan

graphs of all degrees. Ann. of Math. (2), 182(1):307–325, 2015.

[72] G. A. Margulis. Explicit group-theoretical constructions of combinatorial schemes and their

application to the design of expanders and concentrators (Russian). Probl. Peredachi Inf.,

24(1):51–60, 1988.

[73] K. Metsch. A characterization of Grassmann graphs. European J. Combin., 16(6):639–644,

1995.

[74] K. Metsch. On a characterization of bilinear forms graphs. European J. Combin., 20(4):293–

306, 1999.

[75] M. Morgenstern. Existence and explicit constructions of q + 1 regular Ramanujan graphs for

every prime power q. J. Combin. Theory Ser. B, 62(1):44–62, 1994.

[76] A. Munemasa, Y. Sano, and T. Taniguchi. Fat Hoﬀman graphs with smallest eigenvalue at

least −1 − τ . Ars Math. Contemp., 7(1):247–262, 2014.

[77] A. Munemasa, Y. Sano, and T. Taniguchi. Fat Hoﬀman graphs with smallest eigenvalue

greater than −3. Discrete Appl. Math., 176:78–88, 2014.

44

[78] A. Munemasa and V. D. Tonchev. The twisted Grassmann graph is the block graph of a

design. Innov. Incidence Geom., 12(1):1–6, 2011.

[79] A. Neumaier. Strongly regular graphs with smallest eigenvalue −m. Arch. Math., 33:392–400,

1979.

[80] J.-P. Serre. R´epartition asymptotique des valeurs propres de l’op´erateur de Hecke Tp. (French).

J. Amer. Math. Soc., 10(1):75–102, 1997.

[81] D. Stevanovi´c. Spectral Radius of Graphs. Academic Press, 2015.

[82] H. Suzuki. An introduction to distance-regular graphs, Lecture Note, in Three Lectures in

Algebra. Sophia University Lecture Note Series, 41:57–132, 1999.

[83] Y.-Y. Tan, J. H. Koolen, and Z.-J. Xia. A spectral characterization of the s-clique extension

of the triangular graphs. Discuss. Math. Graph Theory, 40:663–676, 2020.

[84] T. Taniguchi. On graphs with the smallest eigenvalue at least −1 − √
2, part I. Ars Math.

Contemp., 1(1):81–98, 2008.

[85] T. Taniguchi. On graphs with the smallest eigenvalue at least −1 − √
2, part II. Ars Math.

Contemp., 5(2):243–258, 2012.

[86] P. Terwilliger. The Johnson graph J(d, r) is unique if (d, r) ̸= (2, 8). Discrete Math., 58(2):175–

189, 1986.

[87] P. Terwilliger. The subconstituent algebra of an association scheme, (part I). J. Algebraic

Combin., 1:363–388, 1992.

[88] P. Terwilliger. Lecture note on Terwilliger algebra (edited by H. Suzuki), 1993.

https://icu-hsuzuki.github.io/lecturenote/, visited: 13-11-2020.

[89] P. Terwilliger. The subconstituent algebra of an association scheme (part III). J. Algebraic

Combin., 2:177–210, 1993.

[90] E. R. van Dam. Nonregular graphs with three eigenvalues. J. Combin. Theory Ser. B,

73(2):101–118, 1998.

[91] E. R. van Dam, W. H. Haemers, J. H. Koolen, and E. Spence. Characterizing distance-

regularity of graphs by the spectrum. J. Combin. Theory Ser. A, 113(8):1805–1820, 2006.

[92] E. R. van Dam and J. H. Koolen. A new family of distance-regular graphs with unbounded

diameter. Invent. math., 162(1):189–193, 2005.

45

[93] E. R. van Dam, J. H. Koolen, and H. Tanaka. Distance-regular graphs. Electron. J. Combin.,

Dynamic Surveys:#DS22, 2016.

[94] R. Woo and A. Neumaier. On graphs whose smallest eigenvalue is at least −1 − √2. Linear

Algebra Appl., 226–228:577–591, 1995.

[95] J. Y. Yang and J. H. Koolen. On the order of regular graphs with ﬁxed second largest

eigenvalue. Linear Algebra Appl., 610:29–39, 2021.

[96] Q. Yang, A. Abiad, and J. H. Koolen. An application of Hoﬀman graphs for spectral charac-

terizations of graphs. Electron. J. Combin., 24(1):#P1.12, 2017.

[97] H. Yu. On the limit points of the smallest eigenvalues of regular graphs. Des. Codes Cryptogr.,

65:77–88, 2012.
 46
