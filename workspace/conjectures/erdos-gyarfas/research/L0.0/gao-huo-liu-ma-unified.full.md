<!-- source: https://arxiv.org/pdf/1904.08126 | converted from PDF -->

arXiv:1904.08126v3  [math.CO]  26 Jan 2021
A uniﬁed proof of conjectures on cycle lengths in graphs

Jun Gao∗ Qingyi Huo† Chun-Hung Liu
‡ Jie Ma§

Abstract

In this paper, we prove a tight minimum degree condition in general graphs for the existence of
paths between two given endpoints, whose lengths form a long arithmetic progression with common
diﬀerence one or two. This allows us to obtain a number of exact and optimal results on cycle lengths
in graphs of given minimum degree, connectivity or chromatic number.
More precisely, we prove the following statements by a uniﬁed approach.

1. Every graph G with minimum degree at least k + 1 contains cycles of all even lengths modulo k;
in addition, if G is 2-connected and non-bipartite, then it contains cycles of all lengths modulo
k.

2. For all k ≥ 3, every k-connected graph contains a cycle of length zero modulo k.

3. Every 3-connected non-bipartite graph with minimum degree at least k + 1 contains k cycles
of consecutive lengths.

4. Every graph with chromatic number at least k + 2 contains k cycles of consecutive lengths.

The ﬁrst statement is a conjecture of Thomassen, the second is a conjecture of Dean, the third is
a tight answer to a question of Bondy and Vince, and the fourth is a conjecture of Sudakov and
Verstra¨ete. All of the above results are best possible.

1 Introduction

The distribution of cycle lengths has been extensively studied in the literature and remains one of
the most active and fundamental research areas in graph theory. In this paper, along the line of the
previous work [15] of two of the authors, we investigate various relations between cycle lengths and
basic graph parameters such as minimum degree. The core of the results in [15] is an optimal bound on
the longest sequence of consecutive even cycle lengths in bipartite graphs of given minimum degree. In
the current paper, we extend this result from bipartite graphs to general graphs and use it as a primary
tool to derive a number of tight results on cycle lengths in relation to minimum degree, connectivity and
chromatic number. This resolves several conjectures and open problems on cycles of consecutive lengths,
cycle lengths modulo a ﬁxed integer and some other related topics. For a thoughtful introduction on
the background, we direct interested readers to [15, 26].

∗School of Mathematical Sciences, University of Science and Technology of China, Hefei, Anhui 230026, China. Email:
gj0211@mail.ustc.edu.cn.
†School of Mathematical Sciences, University of Science and Technology of China, Hefei, Anhui 230026, China. Email:
qyhuo@mail.ustc.edu.cn.
‡Department of Mathematics, Texas A&M University, College Station, Texas 77843, USA. Email:
chliu@math.tamu.edu. Partially supported by NSF under Grant No. DMS-1664593, DMS-1929851 and DMS-1954054.
§School of Mathematical Sciences, University of Science and Technology of China, Hefei, Anhui 230026, China. Email:
jiema@ustc.edu.cn. Partially supported by NSFC grants 11501539 and 11622110, the project “Analysis and Geometry
on Bundles” of Ministry of Science and Technology of the People’s Republic of China, and Anhui Initiative in Quantum
Information Technologies grant AHY150200.
 1

Throughout this section, let k be a ﬁxed but arbitrary positive integer, unless otherwise speciﬁed.
For a path or a cycle P , the length of P , denoted by |P |, is the number of edges in P .

1.1 Paths and cycles of consecutive lengths

The study of cycles of consecutive lengths can be dated back to a conjecture of Erd˝os (see [2]) stating
that every graph with minimum degree at least three contains two cycles of lengths diﬀering by one
or two. This was solved by Bondy and Vince [2] in the following stronger form: if all but at most
two vertices of a graph G have degree at least three, then G contains two cycles whose lengths diﬀer
by one or two. Since then, this result has inspired extensive research on its generalization to k cycles
of consecutive (even or odd) lengths, including results of H¨aggkvist and Scott [12], Verstra¨ete [25],
Fan [10], Sudakov and Verstra¨ete [19], Ma [17], and Liu and Ma [15].
We say that k paths or k cycles P1, P2, . . . , Pk are admissible if |P1| ≥ 2 and |P1|, |P2|, . . . , |Pk| form
an arithmetic progression of length k with common diﬀerence one or two. The following generalization
of Erd˝os’ conjecture was posted in [15], which was in attempt to attack some related problems.

Conjecture 1.1 (Liu and Ma [15]). Every graph with minimum degree at least k + 1 contains k
admissible cycles.

By considering the complete graph Kk+1 or the complete bipartite graph Kk,n for any n ≥ k, we see that
the condition for the minimum degree in Conjecture 1.1 is best possible. Being an evidence, Conjecture
1.1 was proved for all bipartite graphs in [15].
One of our main results is the following theorem on admissible paths with two given endpoints, from
which Conjecture 1.1 can be inferred as a corollary.

Theorem 1.2. Let G be a 2-connected graph and let x, y be distinct vertices of G. If every vertex of G
other than x and y has degree at least k + 1, then there exist k admissible paths from x to y in G.

The case k = 1 of Theorem 1.2 is trivial, and the case k = 2 follows from a result of Fan in [10]. We
remark that Theorem 1.2 is the main force that will be applied to prove all other results in this paper.
We now show that Conjecture 1.1 is an easy corollary of Theorem 1.2. (For possibly ambiguous
notations, we refer readers to Section 2.)

Theorem 1.3. Every graph G with minimum degree at least k + 1 contains k admissible cycles.

Proof. If G is 2-connected, let B = G and choose xy to be an arbitrary edge in G; otherwise, let B be
an end-block of G with cut-vertex x and choose y ∈ NG(x) ∩ V (B − x). Clearly, B is 2-connected and
every vertex of B other than x has degree at least k + 1. By Theorem 1.2, B contains k admissible
paths P1, ..., Pk from x to y. Since each |Pi| ≥ 2, Pi ∪ xy for all i ∈ [k] form k admissible cycles in G.

Theorem 1.3 improves many previous results such as the results in [10, 12, 15, 25]. As the writeup of
a version of this paper was close to complete, we noticed that very recently, Chiba and Yamashita [4]
independently proved Theorem 1.3 under an extra condition that G is 2-connected, by using a diﬀerent
approach from this paper.
One can ask another natural question: what are necessary or suﬃcient conditions for the existence
of k cycles of consecutive lengths? It is clear that such conditions should include non-bipartiteness.
This was addressed by Bondy and Vince in [2], where they proved that any non-bipartite 3-connected
graph contains two cycles of consecutive lengths. On the other hand, Bondy and Vince showed that
the 3-connectivity is necessary by constructing inﬁnitely many non-bipartite 2-connected graphs with
arbitrarily large minimum degree, yet not containing two cycles of consecutive lengths.

2

More generally, Bondy and Vince [2] asked if there exists a (least) function f such that every non-
bipartite 3-connected graph with minimum degree at least f (k) contains k cycles of consecutive lengths.
The existence of f (k) was conﬁrmed by Fan [10], where he proved f (k) ≤ 3⌈k/2⌉. On the other hand,
the complete graph Kk+1 shows f (k) ≥ k + 1.
Our next result determines f (k) = k + 1 and hence provides the optimal answer to the above
question of Bondy and Vince.

Theorem 1.4. Every non-bipartite 3-connected graph with minimum degree at least k + 1 contains k
cycles of consecutive lengths.

1.2 Cycle lengths modulo a ﬁxed integer

Burr and Erd˝os initiated the study of cycle lengths modulo an integer k; they conjectured (see [8])
that for odd k there exists a constant ck such that every graph with average degree at least ck contains
cycles of all lengths modulo k. This was proved by Bollob´as [1] and then the value ck was improved to
be O(k2) by Thomassen in [21, 22]. Thomassen also proposed two conjectures in [21] as follows.

Conjecture 1.5 (Thomassen [21]). Every graph with minimum degree at least k + 1 contains cycles of
all even lengths modulo k.

Conjecture 1.6 (Thomassen [21]). Every 2-connected non-bipartite graph with minimum degree at
least k + 1 contains cycles of all lengths modulo k.

We remark that 2-connectivity and non-bipartiteness are necessary for even k in Conjecture 1.6; see [15]
for explanations. The minimum degree condition in Conjectures 1.5 and 1.6 are tight, since Kk+1 has
no cycle of length 2 modulo k, and Kk,n has no cycle of length 2 modulo k for n ≥ k and odd k.
Results of Verstra¨ete [25], Fan [10], Diwan [7] and Ma [17] indicate that the minimum degree at
least O(k) suﬃces for both conjectures. For ﬁxed m ≥ 3 and large k, Sudakov and Verstra¨ete [20]
determined the optimal minimum degree condition for cycles of length m modulo k up to a constant
factor.
In [15], Liu and Ma conﬁrmed both Conjectures 1.5 and 1.6 for even k. They also proved that
minimum degree k + 4 suﬃces for odd k, and observed that an aﬃrmative of Conjecture 1.1 would
imply both Conjectures 1.5 and 1.6 for odd k. Therefore, as an immediate corollary of Theorem 1.3,
we obtain the following.

Theorem 1.7. Conjectures 1.5 and 1.6 hold for any positive integer k.

We would like to address that very recently, Chiba and Yamashita [4] independently proved Conjecture
1.6. Also very recently, Lyngsie and Merker [16] proved that for odd k, every 3-connected cubic graph
of large order contains cycles of all lengths modulo k.
The case of cycles of length zero modulo k has received considerable attention. Thomassen [22] gave
a polynomial-time algorithm for ﬁnding a cycle of length zero modulo k in any graph or a certiﬁcate
that no such cycle exists. In 1988, Dean [5] proposed the following conjecture.

Conjecture 1.8 (Dean [5]). For any positive integer k ≥ 3, every k-connected graph contains a cycle
of length zero modulo k.

We point out that Conjecture 1.8 is tight, as for all odd k and n ≥ k − 1, the complete bipartite graph
Kk−1,n is (k − 1)-connected but has no cycles of length zero modulo k. The case k = 3 in Conjecture
1.8 was proved by Chen and Saito [3], and the case k = 4 was solved by Dean, Lesniak and Saito [6].
To the best of our knowledge, this conjecture remained open for any k ≥ 5 prior to this paper.
Taking advantage of Theorem 1.2, we are able to resolve Conjecture 1.8 completely.

3

Theorem 1.9. Conjecture 1.8 holds for any positive integer k ≥ 3.

It turns out that the case k = 5 is the most diﬃcult case for our approach. We would like to point out
that for k ≥ 6, in many cases in fact we are able to ﬁnd k admissible cycles. In particular, our proofs
show that when k ≥ 6, any k-connected graph contains cycles of all even lengths modulo k, except for
the residue class 2 modulo k (see Theorem 5.16 for the precise statement).1

1.3 Consecutive cycle lengths and chromatic number

There has been extensive research on the relation between the chromatic number and cycle lengths. For
a graph G, let Le(G) and Lo(G) be the set of even and odd cycle lengths in G, respectively. Bollob´as
and Erd˝os conjectured and Gyarf´as [11] proved that χ(G) ≤ 2|Lo(G)| + 2 for any graph G. Mihok
and Schiermeyer [18] proved an analog for even cycles that χ(G) ≤ 2|Le(G)| + 3 for any graph G. A
strengthening of the above result was obtained in [15], where the number of even cycle lengths |Le(G)|
was replaced by the longest sequence of consecutive even cycle lengths in G. Conﬁrming a conjecture
of Erd˝os [9], Kostochka, Sudakov and Verstra¨ete [13] proved that every triangle-free graph G with
χ(G) = k contains at least Ω(k2 log k) cycles of consecutive lengths.
For k ≥ 2, let χk be the largest chromatic number of a graph which does not contain k cycles of
consecutive lengths. The complete graph Kk+1 shows that χk ≥ k + 1. In [20], Sudakov and Verstra¨ete
conjectured that the chromatic number of a graph can be bounded by the longest sequence of consecutive
cycle lengths from above.

Conjecture 1.10 (Sudakov and Verstra¨ete [20]). For every integer k ≥ 2, χk = k + 1.

Using Theorem 1.2, we are able to prove Conjecture 1.10.

Theorem 1.11. Conjecture 1.10 holds for every integer k ≥ 2.

The rest of the paper is organized as follows. In Section 2, we deﬁne the notations and include
some preliminaries. In Section 3, we prove Theorem 1.2. In Section 4, we prove Theorems 1.4 and 1.11
by a uniﬁed approach via Theorem 1.2. In Section 5, we prove Theorem 1.9 by extensively applying
Theorem 1.2 as well.

2 Preliminaries

All graphs in this paper are ﬁnite, undirected, and simple. Let H be a subgraph of a graph G. We say
that H and a vertex v ∈ V (G) − V (H) are adjacent in G if v is adjacent in G to some vertex in V (H).
Let NG(H) := ⋃v∈V (H) NG(v) − V (H) and NG[H] := NG(H) ∪ V (H). For a subset S of V (G), G[S]
denotes the subgraph induced by S in G, and G − S denotes the subgraph G[V (G) − S]; we say that
a vertex v and S are adjacent in G if v is adjacent in G to some vertex in S. For two distinct vertices
x, y of G, we deﬁne G + xy to be the graph with V (G + xy) = V (G) and E(G + xy) = E(G) ∪ {xy}. A
clique in G is a subset of V (G) whose vertices are pairwise adjacent in G. A vertex is a leaf in G if it
has degree one in G. We say that a path P is internally disjoint from H if no vertex of P other than
its endpoints is in V (H). For a positive integer k, we write [k] for the set {1, 2, ..., k}.
For a graph G and a subset S of V (G), we say that a graph G′ is obtained from G by contracting S
into a vertex s, if V (G′) = (V (G) − S) ∪ {s} and E(G′) = E(G − S) ∪ {vs : v ∈ V (G) − S is adjacent
to S in G}.

1To see the tightness, note that both of Kk+1 (for even and odd k) and Kk,n (for odd k and n ≥ k) are k-connected
and contain cycles of all lengths 2t modulo k, except for cycles of lengths in the residue class 2 modulo k.

4

A vertex v of a graph G is a cut-vertex of G if G − v contains more components than G. A block
B in G is a maximal connected subgraph of G such that there exists no cut-vertex of B. So a block
is an isolated vertex, an edge or a 2-connected graph. An end-block in G is a block in G containing at
most one cut-vertex of G. If D is an end-block of G and a vertex x is the only cut-vertex of G with
x ∈ V (D), then we say that D is an end-block with cut-vertex x. Let B(G) be the set of blocks in G and
C(G) be the set of cut-vertices of G. The block structure of G is the bipartite graph with bipartition
(B(G), C(G)), where x ∈ C(G) is adjacent to B ∈ B(G) if and only if x ∈ V (B). Note that the block
structure of any graph G is a forest, and it is connected if and only if G is connected. For notations
not deﬁned here, we refer readers to [15].
The next result can be derived from a special case of [10, Theorem 2.5].

Theorem 2.1. Let G be a 2-connected graph and let x, y be distinct vertices of G. If every vertex in
G other than x and y has degree at least 3, then there are two admissible paths from x to y in G.

3 Admissible paths

In this section, we prove Theorem 1.2. We say that (G, x, y) is a rooted graph if G is a graph and x, y
are two distinct vertices of G. The minimum degree of a rooted graph (G, x, y) is min{dG(v) : v ∈
V (G) − {x, y}}. We also say that a rooted graph (G, x, y) is 2-connected if G + xy is 2-connected.
Theorem 1.2 is an immediate corollary of the following theorem.

Theorem 3.1. Let k be a positive integer. If (G, x, y) is a 2-connected rooted graph with minimum
degree at least k + 1, then there exist k admissible paths from x to y in G.

The rest of this section is devoted to a proof of Theorem 3.1. We need the following lemma.

Lemma 3.2. Let (H, u, v) be a rooted graph and W be a subset of V (H). Let s be a positive integer.
Assume that there exist s admissible paths P1, ..., Ps, where Pi is from u to some wi ∈ W for each
i ∈ [s]. Assume that for each i ∈ [s], H − V (Pi − wi) contains t paths Ri
1, ..., Ri
t from wi to v such that
their lengths form an arithmetic progression with common diﬀerence one or two2. If |R1
j | = · · · = |Rs
j |
for every j ∈ [t], then there exist s + t − 1 admissible paths in H from u to v.

Proof. If each of A and B is an arithmetic progression with common diﬀerence one or two, then
A + B = {a + b : a ∈ A, b ∈ B} also forms an arithmetic progression with common diﬀerence one or
two of size at least |A| + |B| − 1. So the set {Pi ∪ Ri
j : i ∈ [s], j ∈ [t]} contains s + t − 1 admissible paths
between u and v in H.

Throughout the rest of this section, let (G, x, y) be a counterexample of Theorem 3.1 with minimum
|V (G)| + |E(G)|. That is, for any 2-connected rooted graph (H, u, v) with |V (H)| + |E(H)| < |V (G)| +
|E(G)|, if the minimum degree of (H, u, v) is at least ℓ + 1, then there exist ℓ admissible paths from u
to v in H.
We now prove a sequence of lemmas and then, according to the order of some speciﬁed component
(this will be clear after Lemma 3.7), the remaining proof will be divided into two subsections which we
handle separately.

Lemma 3.3. G is 2-connected, x and y are not adjacent in G, and k ≥ 3.

2Here, we allow that some path Ri
j has length one.
 5

Proof. Theorem 3.1 is obvious when k = 1, and it follows from Theorem 2.1 when k = 2. So k ≥ 3.
Note that |V (G)| ≥ 4, for otherwise, |V (G)| = 3 and (G, x, y) has minimum degree two and thus k = 1,
a contradiction.
Since G + xy is 2-connected, G is connected. Suppose that G is not 2-connected. Then there exists
a cut-vertex b and two connected subgraphs G1, G2 of G on at least two vertices such that G = G1 ∪ G2
and V (G1) ∩ V (G2) = {b}. We may assume that x ∈ V (G1) − b, y ∈ V (G2) − b and by symmetry,
|V (G1)| ≥ 3. Then it is straightforward to see that (G1, x, b) is 2-connected and has minimum degree at
least k + 1. By the minimality of G, there exist k admissible paths in G1 from x to b. By concatenating
each of these paths with a ﬁxed path in G2 from b to y, we obtain k admissible paths in G from x to
y, a contradiction. Therefore G is 2-connected.
Suppose that x is adjacent to y in G. Let G′ = G − xy. Since G is 2-connected, clearly (G′, x, y) is
2-connected and has minimum degree at least k + 1. By the minimality of G, G′ (and thus G) contains
k admissible paths from x to y, a contradiction.

Lemma 3.4. There is no clique in G − y of size at least three containing x, and there is no clique in
G − x of size at least three containing y.

Proof. Suppose to the contrary that there is a clique K in G − y of size at least three containing x. We
choose K such that |K| is maximum. Let t = |K|. So t ≥ 3. Since x and y are non-adjacent by Lemma
3.3, y ̸∈ K. So there exists a component C of G − K containing y.
Suppose V (C) = {y}. Then NG(y) ⊆ K − x. Let Y = NG(y) ∩ K, and let m = |Y |. Since G is
2-connected, we have m ≥ 2. For each vertex v ∈ K, let Dv denote the family of components D ̸= C of
G − K such that v ∈ NG(D). Let D = ⋃
v∈K Dv, D ′ = ⋃v∈Y Dv and D ′′ = D − D ′. If there is a vertex
v ∈ K − x such that Dv = ∅ or there exists some D ∈ Dv with |V (D)| = 1, then t ≥ k + 1, from which
one can easily ﬁnd k paths of lengths 2, 3, . . . , k + 1 from x to y in G[K ∪ {y}], a contradiction. So for
every v ∈ K − x, Dv ̸= ∅ and |V (D)| ≥ 2 for every D ∈ Dv.
Suppose that there exists some D ∈ D ′\Dx. Let v be a vertex in NG(D) ∩ Y such that D ∈ Dv.
Since G is 2-connected, NG(D) − {v} ̸= ∅. Let G1 be the graph obtained from G[NG[D]] by contracting
NG(D) − {v} into a new vertex u1. Since D ̸∈ Dx, we see |NG(D) − {v}| ≤ t − 2. So (G1, u1, v) is
2-connected and has minimum degree at least k − t + 4. By the minimality of G, G1 contains k − t + 3
admissible paths from u1 to v. Hence, G[V (D) ∪ K] contains k − t + 3 admissible paths Pi from a vertex
pi ∈ NG(D) − {v} to v internally disjoint from K for i ∈ [k − t + 3]. Since K is a clique, K − v contains
t − 2 paths from x to pi with lengths 1, 2, . . . , t − 2, respectively. By Lemma 3.2, by concatenating each
of these paths with Pi ∪ {vy}, we obtain k admissible paths from x to y in G, a contradiction.
Hence D ′ ⊆ Dx. Let G2 be the graph obtained from G − y by contracting Y into a new vertex
u2. Let K ′ = G2[(K − Y ) ∪ {u2}]. Then K ′ is a complete graph of order t − m + 1 ≥ 2 in G2. Any
component D ̸= C of G − K in G is also a component of G2 − V (K ′) in G2. If D ∈ D ′, then D is
adjacent in G2 to both x and u2 (since D ′ ⊆ Dx); otherwise D ∈ D ′′ and D is adjacent to at least two
vertices of K ′ − u2 in G2 since G is 2-connected. Since NG(y) is a clique in G, we have that G − y is
2-connected. Since D ′ ⊆ Dx, (G2, x, u2) is 2-connected and has minimum degree at least k − m + 2.
By the minimality of G, G2 contains k − m + 1 admissible paths from x to u2. Hence, G − y contains
k − m + 1 admissible paths Pi from x to a vertex pi ∈ Y for i ∈ [k − m + 1] internally disjoint from
Y . Since G[Y ∪ {y}] is complete, G[Y ∪ {y}] contains m paths from pi to y with lengths 1, 2, . . . , m,
respectively. By Lemma 3.2, we obtain k admissible paths from x to y in G, a contradiction.
Hence |V (C)| ≥ 2. If C is 2-connected, then let B = C and b = y; otherwise let B be an end-block
of C with cut-vertex b such that y /∈ V (B) − {b}. Suppose B is an edge vb. Then v has at least k
neighbours in K. Since K is a clique, we can ﬁnd k consecutive paths from x to v in G[K ∪ {v}].

6

Concatenating each of these paths with a ﬁxed path in C from v to y, we ﬁnd k admissible paths from
x to y, a contradiction.
Hence B is 2-connected. Let P be a path in C − V (B − b) from b to y. Since G is 2-connected, we
have NG(B − b) ∩ K ̸= ∅.
Suppose that NG(B − b) ∩ (K − {x}) ̸= ∅. Let G3 be the graph obtained from G[V (B) ∪ (NG(B −
b) ∩ (K − {x}))] by contracting NG(B − b) ∩ (K − {x}) into a vertex u3. By the maximality of K, every
vertex in V (B − b) is adjacent to at most t − 1 vertices in K. Then (G3, u3, b) is 2-connected and has
minimum degree at least k − t + 3. By the minimality of G, G3 contains k − t + 2 admissible paths from
u3 to b. Hence, G[V (B) ∪ (NG(B − b) ∩ (K − {x}))] contains k − t + 2 admissible paths Pi from some
vertex pi ∈ NG(B − b) ∩ (K − {x}) to b internally disjoint from K for i ∈ [k − t + 2]. Note that for
each i, G[K] contains t − 1 paths from x to pi with lengths 1, 2, . . . , t − 1, respectively. By Lemma 3.2,
by concatenating each of these paths with Pi ∪ P , we obtain k admissible paths from x to y in G, a
contradiction.
Therefore NG(B − b) ∩ K = {x}. Then the rooted graph (G[V (B) ∪ {x}], x, b) is 2-connected and
has minimum degree at least k + 1. By the minimality of G, G[V (B) ∪ {x}] contains k admissible paths
from x to b. By concatenating each of these paths with P , we obtain k admissible paths from x to y, a
contradiction.
This proves that there is no clique in G − y of size at least three containing x. Similarly, there is no
clique in G − x of size at least three containing y, completing the proof of Lemma 3.4.

In the rest of this section, by symmetry between x and y, we may assume that dG(x) ≤ dG(y).

Lemma 3.5. G − y has a cycle of length four containing x.

Proof. Suppose that x is not contained in any cycle of length four in G − y. Then

|NG(v) ∩ NG(x)| ≤ 1 for every v ∈ V (G) − {x, y}. (1)

Let G1 be the graph obtained from G by contracting NG[x] into a new vertex x1. By (1), G1 is connected
and the minimum degree of (G1, x1, y) is at least k + 1. If G1 is not 2-connected, then x1 is the unique
cut-vertex of G1 and we let B be the end-block of G1 containing x1 and y; otherwise G1 is 2-connected
and let B = G1.
Suppose that B is not an edge. Then (B, x1, y) is 2-connected and has minimum degree at least
k + 1. By the minimality of G, B contains k admissible paths from x1 to y. Then G − x contains k
admissible paths Pi from a vertex pi ∈ NG(x) to y for all i ∈ [k]. By concatenating each of these paths
with xpi, we obtain k admissible paths from x to y in G, a contradiction.
Therefore B is an edge. Since dG(x) ≤ dG(y), we conclude that NG(x) = NG(y). By Lemma 3.4
and k ≥ 3, we see V (G) ̸= NG[x] ∪ {y}. So there exists a component D of G − NG(x) not containing x
and y. Since G is 2-connected, we have |NG(D)| ≥ 2. Fix a vertex u in NG(D). Let G2 be the graph
obtained from G[NG[D]] by contracting NG(D) − {u} into a new vertex v. Then by (1), (G2, u, v) is
2-connected and has minimum degree at least k + 1. By the minimality of G, G2 contains k admissible
paths from u to v. So G − {x, y} contains k admissible paths Pi from u to some vertex pi ∈ NG(x) − {u}
for i ∈ [k]. By concatenating each of these paths with xu and piy, we obtain k admissible paths from
x to y in G, a contradiction.

Lemma 3.6. Let C = xx1ax2x be a cycle of length four in G− y. Then every vertex in V (G)− (V (C)∪
{y}) is not adjacent in G to all of x1, x2, a.

Proof. Suppose to the contrary that there exists a vertex v ∈ V (G) − (V (C) ∪ {y}) adjacent in G to
all of x1, x2, a. Let K be a maximal clique in G − {x, y, x1, x2} such that a ∈ K and every vertex in K
is adjacent to both of x1 and x2. Let t = |K|. So t ≥ 2. We have the following two facts:

7

(a) for any u ∈ K, G[V (C) ∪ K] contains t + 1 admissible paths from x to u of lengths 2, 3, ..., t + 2,
respectively;

(b) for any i ∈ [2], G[V (C) ∪ K] contains t admissible paths from x to xi of lengths 3, 4, ..., t + 2,
respectively.

Let F be the component of G − (V (C) ∪ K) containing y.
Suppose V (F ) = {y}. Then NG(y) ⊆ V (K)∪{x1, x2}. Since G is 2-connected, we have |NG(y)| ≥ 2.
If NG(y) ̸= {x1, x2}, then there exists a triangle containing y in G − x, contradicting Lemma 3.4.
Therefore NG(y) = {x1, x2}. Since dG(x) ≤ dG(y), NG(x) = NG(y) = {x1, x2}. Let G′ = G − {x, y}. It
is clear that (G′, x1, x2) is 2-connected and has minimum degree at least k + 1. By the minimality of
G, G′ contains k admissible paths from x1 to x2. By concatenating each of these paths with xx1 and
x2y, G contains k admissible paths from x to y, a contradiction.
So |V (F )| ≥ 2. If F is 2-connected, let B = F and b = y; otherwise let B be an end-block of F with
cut-vertex b such that y /∈ V (B) − b.
Suppose that B is an edge vb. If v is adjacent to x, then by Lemma 3.4, NG(v) ∩ {x1, x2} = ∅ and
thus t ≥ |NG(v) ∩ K| ≥ k − 1. If v is not adjacent to x, then by the maximality of K, it holds that
t + 1 ≥ |NG(v) ∩ (K ∪ {x1, x2})| ≥ k ≥ 3. So in both cases, we have t ≥ k − 1 and there exists some
u ∈ NG(v) ∩ K. By (a), there exist k admissible paths from x to y in G, a contradiction.
Therefore B is 2-connected. Let P be a path in F − V (B − b) from b to y.
Suppose that NG(B − b) ∩ K ̸= ∅. Let G1 be the graph obtained from G[V (B) ∪ (NG(B − b) ∩ K)]
by contracting NG(B − b) ∩ K into a new vertex u1. Let us consider the degree of any v ∈ V (B − b) in
G1. If v is adjacent to both x1, x2, then by Lemma 3.4 and the maximality of K, v is not adjacent to
x and is adjacent to at most t − 1 vertices in K, implying that dG1(v) ≥ k + 1 − t; if v is adjacent to
exactly one of x1, x2, then v is not adjacent to x and thus dG1(v) ≥ k + 1 − t; if v is adjacent to none
of x1, x2, then v may be adjacent to x and all vertices in K, which also shows that dG1(v) ≥ k + 1 − t.
So (G1, u1, b) is 2-connected and has minimum degree at least k − t + 1. By the minimality of G, G1
contains k − t admissible paths from u1 to b. Hence, G contains k − t admissible paths Pi from a vertex
pi ∈ NG(B − b) ∩ K to b for i ∈ [k − t] internally disjoint from V (C) ∪ K. By (a), G[V (C) ∪ K] contains
t + 1 paths from x to pi with lengths 2, 3, . . . , t + 2, respectively. By Lemma 3.2, concatenating each of
these path with Pi ∪ P leads to k admissible paths from x to y, a contradiction.
Therefore, NG(B − b) ⊆ {x, x1, x2, b}. Since G is 2-connected, NG(B − b) ∩ {x, x1, x2} ̸= ∅. If
x1 ∈ NG(B − b), then (G[B ∪ {x1}], x1, b) is 2-connected and has minimum degree at least k by Lemma
3.4. By the minimality of G, G[B ∪ {x1}] contains k − 1 admissible paths from x1 to b. By (b), there
are t admissible paths from x to x1 in G[C ∪ K]. By concatenating each of the above paths with P ,
we obtain k − 1 + t − 1 ≥ k admissible paths from x to y in G, a contradiction. By symmetry between
x1 and x2, this shows that x1, x2 /∈ NG(B − b). So NG(B − b) = {x, b}. Then (G[B ∪ {x}], x, b) is a
2-connected rooted graph with minimum degree at least k + 1, from which one can obtain k admissible
paths from x to y by the minimality of G, a contradiction. This completes the proof of Lemma 3.6.

Lemma 3.7. There exists a positive integer s and an induced complete bipartite subgraph Q with
bipartition (Q1, Q2) in G satisfying that

1. x ∈ Q2, y /∈ V (Q), |Q1| ≥ |Q2| = s + 1 ≥ 2, and

2. for every v ∈ V (G) − (V (Q) ∪ {y}),

(a) |NG(v) ∩ Q| ≤ s + 1, |NG(v) ∩ Q1| ≤ s + 1, |NG(v) ∩ Q2| ≤ s, and

(b) if v is adjacent to both of Q1 and Q2, then |NG(v) ∩ Q1| = 1.

8

Proof. By Lemma 3.5 there exists a 4-cycle in G−y containing x. Thus there exists a complete bipartite
subgraph Q of G − y with bipartition (Q1, Q2) such that x ∈ Q2, y /∈ V (Q) and |Q1| ≥ |Q2| ≥ 2. We
choose Q so that |Q2| is maximum and subject to this, |Q1| is maximum. Let s be a positive integer
such that |Q2| = s + 1.
We claim that such Q and s satisfy the conclusion of this lemma. Statement 2(b) holds by Lemmas
3.4 and 3.6. By the choice of Q, for every v ∈ V (G) − (V (Q) ∪ {y}), |NG(v) ∩ Q1| ≤ s + 1 and
|NG(v) ∩ Q2| ≤ s. This together with Statement 2(b), we know Statement 2(a) holds. By Lemmas 3.4
and 3.6, Q is an induced subgraph in G. The proof of Lemma 3.7 is completed.

Throughout the remaining of the section, Q and s denote the induced complete bipartite subgraph
and the positive integer s promised by Lemma 3.7, and let C be the component of G − V (Q) containing
y. There are two possibilities for the size of C: |V (C)| = 1 or |V (C)| ≥ 2. We now split the rest of the
proof into two subsections based on these two cases. We shall derive a contradiction in each subsection
and hence show that G is a not a counterexample to complete the proof of Theorem 3.1.

3.1 |V (C)| = 1

In this case we have V (C) = {y}. By Lemma 3.3, xy ̸∈ E(G). So by Lemma 3.4, y is adjacent to exactly
one of Q1 and Q2. Since dG(y) ≥ dG(x), we derive that NG(x) = NG(y) = Q1 and so G[V (Q) ∪ {y}] is
complete bipartite. If s ≥ k − 1, then G[V (Q) ∪ {y}] contains k admissible paths from x to y of lengths
2, 4, . . . , 2k, respectively, a contradiction.
So s ≤ k − 2. This shows that V (G) ̸= V (Q) ∪ {y}, for otherwise every vertex in Q1 has degree
s + 2 ≤ k in G. Hence there exists a component in G − (V (Q) ∪ {y}).
Let D be an arbitrary component of G − (V (Q) ∪ {y}). If there exists a vertex v of D of degree at
most one in D, then by Lemma 3.7, s + 1 ≥ |NG(v) ∩ V (Q)| ≥ k, a contradicting that s ≤ k − 2. So
|V (D)| ≥ 2 and every end-block of D is 2-connected. In addition, NG(x) = Q1, so x /∈ NG(D).
We claim that NG(D) ∩ Q1 ̸= ∅. Suppose to the contrary that NG(D) ∩ Q1 = ∅. Since G is 2-
connected and x /∈ NG(D), we have |NG(D)∩(Q2 −{x})| ≥ 2. Let u1 be a vertex in NG(D)∩(Q2 −{x}).
Let G1 be the graph obtained from G[NG[D]] by contracting NG(D) ∩ (Q2 − {x, u1}) into a new vertex
v1. Therefore (G1, u1, v1) is 2-connected and has minimum degree at least k − s + 3. By the minimality
of G, G1 contains k−s+2 admissible paths from u1 to v1. Hence, G−{x, y} contains k−s+2 admissible
paths Pi from u1 to some vertex pi ∈ Q2 − {x, u1} internally disjoint from V (Q) for i ∈ [k − s + 2].
Let w be a vertex in Q1. Since Q is complete bipartite, Q − {u1, w} contains s − 1 paths from x to pi
of lengths 2, 4, . . . , 2s − 2, respectively. By Lemma 3.2, concatenating each of these paths with Pi and
u1wy leads to k admissible paths from x to y, a contradiction.
We claim that NG(D)∩(Q2 −{x}) ̸= ∅. Suppose to the contrary that NG(D)∩(Q2 −{x}) = ∅. Since
G is 2-connected and x ̸∈ NG(D), |NG(D) ∩ Q1| ≥ 2. Let u2 be a vertex in NG(D) ∩ Q1. Let G2 be the
graph obtained from G[NG[D]] by contracting NG(D)∩(Q1 −{u2}) into a new vertex v2. If |Q1| ≥ s+2,
then let ǫ = 0; if |Q1| = s + 1, then let ǫ = 1. So (G2, u2, v2) is 2-connected and has minimum degree
at least k − s + 1 + ǫ. By the minimality of G, G2 contains k − s + ǫ admissible paths from u2 to v2.
Hence, G − {x, y} contains k − s + ǫ admissible paths Pi from u2 to some vertex pi ∈ Q1 − u2 internally
disjoint from V (Q) for all i ∈ [k − s + ǫ]. Since Q is complete bipartite, Q − u2 contains s + 1 − ǫ paths
from x to pi of lengths 1, 3, . . . , 2(s − ǫ) + 1, respectively. By Lemma 3.2, concatenating each of these
paths with Pi and u2y leads to k admissible paths from x to y, a contradiction. This proves the claim.
Now we claim that there is a matching of size two in G between V (D) and Q1. Suppose that there is
no matching of size two in G between V (D) and Q1. Then either |NG(D)∩Q1| = 1 or |NG(Q1)∩V (D)| =
1. In the former case, let u3 = w3 be the unique vertex in NG(D) ∩ Q1; in the latter case, let u3 be

9

the unique vertex in NG(Q1) ∩ V (D) and let w3 be a vertex in Q1 adjacent in G to u3. Recall that
NG(D) ∩ (Q2 − {x}) ̸= ∅. Let G3 be the graph obtained from G[D ∪ {u3} ∪ (NG(D) ∩ (Q2 − {x}))]
by contracting NG(D) ∩ (Q2 − {x}) into a new vertex v3. Then (G3, u3, v3) is 2-connected and has
minimum degree at least k − s + 2. By the minimality of G, G3 contains k − s + 1 admissible paths from
u3 to v3. Hence, G − y contains k − s + 1 admissible paths Pi from u3 to some vertex pi ∈ Q2 − {x}
internally disjoint from V (Q) for i ∈ [k − s + 1]. Since Q is complete bipartite, Q − w3 contains s paths
from x to pi of lengths 2, 4, . . . , 2s, respectively. By Lemma 3.2, concatenating each of these paths with
Pi and u3w3y, we obtain k admissible paths from x to y in G. This contradiction completes the proof
of the claim.
Suppose that D is not 2-connected and there exists an end-block B of D with cut-vertex b such
that NG(B − b) ∩ V (Q) ⊆ Q2 − {x}. Recall that every end-block of D is 2-connected. So B is 2-
connected. Let G4 be the graph obtained from G[V (B) ∪ (NG(B − b) ∩ (Q2 − {x}))] by contracting
NG(B − b) ∩ (Q2 − {x}) into a new vertex v4. Then (G4, b, v4) is 2-connected and has minimum degree
at least k − s + 2. By the minimality of G, G4 contains k − s + 1 admissible paths from b to v4. Hence,
G contains k − s + 1 admissible paths Pi from b to some vertex pi ∈ Q2 − {x} internally disjoint from
V (Q) for i ∈ [k − s + 1]. Since NG(D) ∩ Q1 ̸= ∅, there exists a path R in G[(D − V (B − b)) ∪ Q1] from
b to some vertex a ∈ Q1 internally disjoint from V (B) ∪ V (Q). Since Q is complete bipartite, Q − a
contains s paths from x to pi with ﬁxed lengths 2, 4, . . . , 2s, respectively. By Lemma 3.2, concatenating
each of these paths with Pi ∪ R ∪ ay leads to k admissible paths from x to y in G, a contradiction.
Therefore, either D is 2-connected, or every end-block B of D with cut-vertex b satisﬁes that
NG(B − b) ∩ Q1 ̸= ∅.
We claim |Q1| = s + 1. Suppose to the contrary that |Q1| ≥ s + 2. Recall that there exists a
matching M of size two in G between V (D) and Q1. So there exists a vertex u5 ∈ NG(D) ∩ Q1
incident with an edge in M such that NG(D) ∩ (Q1 − {u5}) ̸= ∅. Let G5 be the graph obtained from
G[V (D) ∪ (NG(D) ∩ Q1)] by contracting NG(D) ∩ (Q1 − {u5}) into a new vertex v5. Since M is a
matching of size two in G between V (D) and Q1, if D is 2-connected, then (G5, u5, v5) is 2-connected;
if D is not 2-connected, then every end-block of D has a non-cut vertex adjacent in G5 to one of u5, v5,
so (G5, u5, v5) is 2-connected. Moreover, by Lemma 3.7, G5 has minimum degree at least k − s + 1. By
the minimality of G, G5 contains k − s admissible paths from u5 to v5. Hence, G − y contains k − s
admissible paths Pi from u5 to pi ∈ V (Q1 − u5) internally disjoint from V (Q) for i ∈ [k − s]. Since
|Q1| ≥ s + 2, Q − u5 contains s + 1 paths from x to pi of lengths 1, 3, . . . , 2s + 1, respectively. By Lemma
3.2, concatenating each of these paths with Pi ∪ u5y, we obtain k admissible paths from x to y in G, a
contradiction. This proves that |Q1| = s + 1.
Suppose that s = 1. Denote Q1 by {u, v}. As NG(x) = NG(y) = Q1, it is clear that (G− {x, y}, u, v)
is 2-connected and has minimum degree at least k + 1. By the minimality of G, there are k admissible
paths from u to v in G − {x, y}, which can be easily extended to k admissible paths from x to y in G,
a contradiction.
Therefore we have s ≥ 2. Let w be a vertex in Q2 − x. Since s ≤ k − 2, w is adjacent in G to
least two vertices in V (G) − (V (Q) ∪ {y}). So there exists a non-empty set D of all components in
G − (V (Q) ∪ {y}) adjacent to w. Since every member of D is a component of G − (V (Q) ∪ {y}), for
every D′ ∈ D, either D′ is 2-connected or every end-block of D′ has a non-cut-vertex adjacent to Q1.
Let H = ⋃D′∈D V (D′). Since every member D′ of D is a component of G − (V (Q) ∪ {y}), there
exists a matching MD′ of size two in G between V (D′) and Q1, so we have |NG(H) ∩ Q1| ≥ 2. Let
u6 be a vertex in NG(H) ∩ Q1 incident with an edge in MD0 for some D0 ∈ D. Let G6 be the graph
obtained from G[NG[H]] by deleting Q2 − {x, w} and contracting Q1 − u6 into a new vertex v6.
We claim that (G6, u6, v6) is 2-connected. Let G′ = G6 + u6v6. We shall prove that G′ is 2-
connected. It suﬃces to show that for every D′ ∈ D, G′[V (D′) ∪ {u6, v6, w}] is 2-connected. Suppose to

10

the contrary that there exists D′ ∈ D such that G′[V (D′) ∪ {u6, v6, w}] is not 2-connected. Note that
G′[{u6, v6, w}] is isomorphic to K3 and every end-block of D′ is adjacent to {u6, v6}. So G′ is connected,
and there exists a cut-vertex of c of G′[V (D′) ∪ {u6, v6, w}] such that either c ∈ {u6, v6, w} or c is a
cut-vertex of D′. Since V (D′) is adjacent to w and {u6, v6}, if c ∈ {u6, v6, w}, then the component of
G′[V (D′)∪ {u6, v6, w}]− c containing V (D′) also contains {u6, v6, w}, so this component contains equals
G′[V (D′) ∪ {u6, v6, w}] − c, a contradiction. So c is a cut-vertex of D′. But every component of D′ − c
contains a non-cut-vertex of D′ in an end-block of D′, so it is adjacent to {u6, v6}, and hence there
exists a component of G′[V (D′) ∪ {u6, v6, w}] − c contains every component of D′ − c and {u6, v6, w}.
This shows that G′[V (D′) ∪ {u6, v6, w}] − c is connected, a contradiction. So (G6, u6, v6) is 2-connected.
Now we show the minimum degree of (G6, u6, v6) is at least k − s + 2. Let v ∈ V (G6) − {u6, v6, w}.
Then either NG(v) ∩ Q ⊆ Q1, NG(v) ∩ Q ⊆ Q2 − x or v is adjacent to both of Q1 and Q2 − x. By
Lemma 3.7, in either case we can derive that dG6(v) ≥ k − s + 2. In addition, since |Q1| = s + 1,
dG6(w) ≥ k − s + 2. Hence, indeed the minimum degree of (G6, u6, v6) is at least k − s + 2.
By the minimality of G, G6 contains k − s + 1 admissible paths from u6 to v6. Hence, G[NG[H]]
contains k − s + 1 admissible paths Pi from u6 to some vertex pi ∈ Q1 − u6 internally disjoint from
V (Q)−w for i ∈ [k −s+1]. Note that Pi possibly contains w. Since Q is complete bipartite, Q−{u6, w}
contains s paths from x to pi of lengths 1, 3, . . . , 2s − 1, respectively. By Lemma 3.2, by concatenating
each of these paths with Pi ∪ u6y, we obtain k admissible paths from x to y in G, a contradiction. This
ﬁnishes the proof of Subsection 3.1.

3.2 |V (C)| ≥ 2

We ﬁrst show that no vertex in C − y has degree one in C. Suppose to the contrary that there exists
v ∈ V (C − y) with degree one in C. By Lemma 3.7, s + 1 ≥ |NG(v) ∩ V (Q)| ≥ k. If NG(v) ∩ Q1 ̸= ∅,
then there are k paths from x to v in G[Q ∪ {v}] of lengths 2, 4, . . . , 2k, respectively. If NG(v) ∩ Q1 = ∅,
then NG(v) ∩ V (Q) ⊆ Q2, so s ≥ |NG(v) ∩ V (Q)| ≥ k by Lemma 3.7, and hence there are k paths from
x to v in G[Q ∪ {v}] of lengths 3, 5, . . . , 2k + 1, respectively. In both cases, by concatenating each of
these path with a path from v to y in C, we obtain k admissible paths from x to y in G, a contradiction.
So no vertex in C − y has degree one in C. In particular, every end-block of C is 2-connected, except
possibly an end-block consisting of y and its unique neighbor in C.
We say a block of C is a feasible block if it is an end-block of C such that either it equals C, or y is
not a non-cut-vertex of this block. Note that feasible blocks exist, since either C has no cut-vertex, or
C contains at least two end-blocks.
Let B be an arbitrary feasible block. If C is 2-connected, then let b = y; otherwise let b be the
cut-vertex of C contained in B.
We claim that NG(B − b) ⊆ Q2 ∪ {b}. Suppose to the contrary that NG(B − b) ∩ Q1 ̸= ∅. Let G1
be the graph obtained from G[V (B) ∪ (NG(B − b) ∩ Q1)] by contracting NG(B − b) ∩ Q1 into a new
vertex x1. So (G1, x1, b) is 2-connected and has minimum degree at least k − s + 1 by Lemma 3.7. By
the minimality of G, G1 has k − s admissible paths from x1 to b. Therefore there are k − s admissible
paths Pi from some vertex pi ∈ NG(B − b) ∩ Q1 to b internally disjoint from V (Q) for i ∈ [k − s]. Also
Q contains s + 1 paths from x to pi of ﬁxed lengths 1, 3, . . . , 2s + 1, respectively. By Lemma 3.2, by
concatenating each of these paths with Pi and a ﬁxed path in C − V (B − b) from b to y, we obtain k
admissible paths from x to y in G, a contradiction. This proves NG(B − b) ⊆ Q2 ∪ {b}.
Next we show that s = 1 and NG(B − b) ∩ V (Q) = Q2. Let R be a path in C − V (B − b) from
b to y. If NG(B − b) ∩ Q2 = {x}, then (NG[B], x, b) is 2-connected and has minimum degree at least
k + 1, so by the minimality of G, G[V (B) ∪ {x}] contains k admissible paths from x to b, and hence
concatenating each of them with R leads to k admissible paths from x to y in G, a contradiction. So

11

NG(B − b) ∩ (Q2 − {x}) ̸= ∅. Let G2 be the graph obtained from G[V (B) ∪ (NG(B − b) ∩ (Q2 − {x}))]
by contracting NG(B − b) ∩ (Q2 − {x}) into a new vertex x2. If s ≥ 2 or NG(B − b) ∩ V (Q) ⊆ Q2 − {x},
using the facts that NG(B − b) ⊆ Q2 ∪ {b} and |NG(v) ∩ Q2| ≤ s for any v ∈ V (B − b) (the latter
one is from Lemma 3.7 2(a)), one can verify that (G2, x2, b) is 2-connected and has minimum degree at
least k − s + 2. By the minimality of G, G2 has k − s + 1 admissible paths from x2 to b. So there are
k − s + 1 paths Pi from some vertex pi ∈ NG(B − b) ∩ (Q2 − {x}) to b internally disjoint from V (Q) for
i ∈ [k − s + 1]. Also Q contains s admissible paths from x to pi of lengths 2, 4, . . . , 2s, respectively. By
Lemma 3.2, by concatenating each of these paths with Pi and R, we obtain k admissible paths from x
to y, a contradiction. This shows that s = 1 and NG(B − b) ∩ V (Q) = Q2.
We denote Q2 by {x, a}. So NG(B − b) ∩ V (Q) = Q2 = {x, a}.

Case 1. NG(C − y) ∩ Q1 = ∅.

Since NG(B − b) ∩ V (Q) = Q2 = {a, x}, we have that (G[V (B) ∪ {a}], a, b) is 2-connected and has
minimum degree at least k. By the minimality of G, G[V (B) ∪ {a}] contains k − 1 admissible paths
P1, . . . , Pk−1 from a to b. Let Y be a path from b to y in C − V (B − b).
For any v ∈ Q1, if NG(v) ⊆ Q2 ∪ {y}, then the degree of v in G is three, so k ≤ 2, contradicting
Lemma 3.3. Therefore, there exists a component D of G−V (Q∪C) adjacent to v. Since NG(C−y)∩Q1 =
∅, NG(Q1) ∩ V (C) ⊆ {y}. So (G − V (C), x, a) is 2-connected and has minimum degree at least k. By
the minimality of G, there are k − 1 admissible paths R1, ..., Rk−1 from x to a in G − V (C). Then by
Lemma 3.2, Ri ∪ Pj ∪ Y for all i, j ∈ [k − 1] give at least 2k − 3 ≥ k admissible paths from x to y, a
contradiction. This completes the proof of Case 1.

Case 2. NG(C − y) ∩ Q1 ̸= ∅.

If C is 2-connected, then C = B and y = b, contradicting NG(B − b) ∩ V (Q) = {x, a}. So C is
not 2-connected. Let B1, B2, . . . , Bt be all end-blocks of C with cut-vertices b1, b2, . . . , bt, respectively.
Note that t ≥ 2.
Suppose that y /∈ ⋃t
i=1(V (Bi) − {bi}). So for every i ∈ [t], Bi is a feasible block, and hence
NG(Bi − bi) ∩ V (Q) = {x, a} which is disjoint from Q1. Since NG(C − y) ∩ Q1 ̸= ∅, there is a vertex w
in V (C) − (
⋃t
i=1(V (Bi) − {bi}) ∪ {y}) such that NG(w) ∩ Q1 ̸= ∅. Let c be a vertex in NG(w) ∩ Q1.
Using the block structure of C, there exist two end-blocks Bm, Bn for 1 ≤ m < n ≤ t, such that there
are two disjoint paths L1, L2 from bm to w and from bn to y internally disjoint from V (Bn) ∪ V (Bm),
respectively. Since Bm and Bn are feasible, NG(Bm − bm) ∩ V (Q) = {x, a} = NG(Bn − bn) ∩ V (Q). So
both of (G[V (Bm) ∪ {x}], x, bm) and (G[V (Bn) ∪ {a}], a, bn) are 2-connected and have minimum degree
at least k. By the minimality of G, there are k − 1 admissible paths P1, . . . , Pk−1 from x to bm in
G[V (Bm) ∪ {x}]; and there are k − 1 admissible paths R1, . . . , Rk−1 from a to bn in G[V (Bn) ∪ {a}].
By Lemma 3.3, k ≥ 3. So the set {Pi ∪ L1 ∪ wca ∪ Rj ∪ L2 : i, j ∈ [k − 1]} contains at least 2k − 3 ≥ k
admissible paths from x to y in G, a contradiction.
So there exists an end-block, say Bt, of C such that y ∈ V (Bt) − {bt}. We say that a block H of C
other than B1 is a hub if H is 2-connected and contains at most two cut-vertices of C, and every path
in C from B1 to Bt contains all cut-vertices of C contained in V (H).
Suppose there exists a hub B∗ of C. So there exists a cut-vertex x∗ of C contained in B∗ such that
every path in C from b1 to V (B∗) contains x∗. If B∗ = Bt, then let y∗ = y; otherwise, let y∗ be the
cut-vertex of C contained in B∗ such that every path in C from bt to V (B∗) contains y∗. Let Z0 be a
path in C − (V (B1 − b1) ∪ V (B∗ − x∗)) from b1 to x∗, and let Z1 be a path in C from y∗ to y. Since
(G[B1 ∪ {x}], x, b1) is 2-connected with minimum degree at least k, by the minimality of G, G[B1 ∪ {x}]
contains k − 1 admissible paths P1, . . . , Pk−1 from x to b1. If every vertex in V (B∗) − {x∗, y∗} has
at most one neighbor in Q, then (B∗, x∗, y∗) is 2-connected with minimum degree at least k. By the

12

minimality of G, B∗ contains k − 1 admissible paths R1, . . . , Rk−1 from x∗ to y∗. By Lemmas 3.2 and
3.3, the set {Pi ∪ Z0 ∪ Rj ∪ Z1 : i, j ∈ [k − 1]} contains least 2k − 3 ≥ k admissible paths from x to
y in G, a contradiction. Therefore some vertex w ∈ V (B∗) − {x∗, y∗} satisﬁes |NG(w) ∩ V (Q)| ≥ 2.
Since s = 1, we have |NG(w) ∩ V (Q)| = 2 by Lemma 3.7. Let u, v be the vertices in NG(w) ∩ V (Q).
By Lemma 3.7, either {u, v} ⊆ Q1, or by symmetry say u ∈ Q1 and v ∈ Q2. In the former case, there
are two admissible paths L1 = xua and L2 = xuwva from x to a; in the latter case, since there is no
triangle containing x in G − y by Lemma 3.4, we must have v = a, which also gives two admissible
paths L1 = xua and L2 = xuwa from x to a. Since (G[B1 ∪ {a}], a, b1) is 2-connected with minimum
degree at least k, by the minimality of G, there exist k − 1 admissible paths N1, . . . , Nk−1 from a to b1
in G[B1 ∪ {a}]. Since B∗ is 2-connected, there exists a path L′ from x∗ to y∗ in B − w. By Lemma 3.2,
the set {Li ∪ Nj ∪ Z0 ∪ L′ ∪ Z1 : i ∈ [2], j ∈ [k − 1]} contains k admissible paths from x to y in G, a
contradiction.
So there exists no hub. In particular, Bt is not 2-connected, for otherwise Bt is a hub. Therefore
Bt = ybt is an edge. So B1, ..., Bt−1 are the all feasible blocks in C. Recall that NG(Bi − bi) ∩ V (Q) =
{a, x} for all i ∈ [t − 1], which implies dG(x) ≥ |Q1| + t − 1. Since there is no triangle containing y
in G − x by Lemma 3.4, we have dG(y) ≤ |Q1| + 1. Hence |Q1| + t − 1 ≤ dG(x) ≤ dG(y) ≤ |Q1| + 1.
That is, t ≤ 2. As t ≥ 2, this forces t = 2, dG(x) = dG(y) = |Q1| + 1. In other words, there is exactly
one end-block B1 of C other than B2 = yb2, NG(y) = Q1 ∪ {b2} and NG(x) ⊆ Q1 ∪ V (B1 − b1). Note
that the block structure of C is a path. Since there exists no hub, every block of C other than B1 is an
edge. If V (C) = V (B1 ∪ B2), then since NG(C − y) ∩ Q1 ̸= ∅ and NG(B1 − b1) ∩ Q1 = ∅, b2 must have
a neighbor in Q1. If V (C) ̸= V (B1 ∪ B2), then |NG(b2) ∩ V (C)| = 2, and since dG(b2) ≥ k + 1 ≥ 4, we
have |NG(b2) ∩ V (Q)| ≥ 2. Recall that NG(x) ⊆ Q1 ∪ V (B1 − b1), so xb2 /∈ E(G). So in either case, b2
must have a neighbor w∗ in Q1. But G[{y, b2, w∗}] is a triangle, contradicting Lemma 3.4.
This completes the proof of Theorem 3.1 (and of Theorem 1.2).

4 Consecutive cycles

In this section, we prove Theorems 1.4 and 1.11. This will be achieved in a uniﬁed approach, namely,
by ﬁnding optimal number of cycles of consecutive lengths in 2-connected non-bipartite graphs (see
Theorem 4.4).
We begin by introducing a concept on cycles, which is crucial in our approach. We say that a cycle
C in a connected graph G is non-separating if G − V (C) is connected. The study of non-separating
cycles appears in the work of Tutte [24] and is furthered explored by Thomassen and Toft [23]. The
proof of the following lemma can be found in [2] (though it was not formally stated).

Lemma 4.1 (Bondy and Vince [2]). Every non-bipartite 3-connected graph contains a non-separating
induced odd cycle.

We also need the following lemma on non-separating odd cycles from [15], which is a slight modiﬁ-
cation of a result of Fan [10].

Lemma 4.2 (Liu and Ma [15]). Let G be a graph with minimum degree at least four. If G contains
a non-separating induced odd cycle, then G contains a non-separating induced odd cycle C, denoted by
v0v1...v2sv0, such that either

1. C is a triangle, or

2. for every non-cut-vertex v of G − V (C), |NG(v) ∩ V (C)| ≤ 2, and the equality holds if and only if
NG(v) ∩ V (C) = {vi, vi+2} for some i, where the indices are taken under the additive group Z2s+1.

13

The next lemma can be viewed as a corollary of Theorem 3.1, which will be used for ﬁnding paths
in a 2-connected graph with three special vertices.

Lemma 4.3. Let k ≥ 2 be a positive integer. Let G be a 2-connected graph and x, y, z be three distinct
vertices in G. If every vertex of G other than z has degree at least k+1, then G contains k−1 admissible
paths from x to y.

Proof. Since every two vertices are contained in a cycle in a 2-connected graph, there is nothing to
prove when k = 2. So we may assume that k ≥ 3. Note that G − z is connected and has minimum
degree at least k. If G − z is 2-connected, then this lemma follows from Theorem 3.1. Hence we may
assume that G − z is not 2-connected.
Let B be an end-block of G − z with cut-vertex b. Since every vertex in V (B − b) has degree at
least k ≥ 3 in G, we see that B is 2-connected. Suppose that |V (B − b) ∩ {x, y}| = 1. Without loss
of generality, we may assume that x ∈ V (B − b). By Theorem 3.1, B has k − 1 admissible paths from
x to b. Concatenating each of these paths with a path in (G − z) − V (B − b) from b to y gives k − 1
admissible paths in G from x to y. Therefore, there exists an end-block B′ with cut-vertex b′ of G − z
such that V (B′ − b′) ∩ {x, y} = ∅. It follows that NG(B′ − b′) = {b′, z}. Since G is 2-connected, G has
two disjoint paths P1, P2 internally disjoint from V (B′) from x to b′ and from y to z, respectively. Let u
be a vertex in B′ − b′ adjacent to z in G. By Theorem 3.1, B′ has k − 1 admissible paths R1, R2, ..., Rk−1
from b′ to u. Then the set {P1 ∪ Ri ∪ uz ∪ P2 : i ∈ [k − 1]} contains k − 1 admissible paths in G from x
to y. This completes the proof.

We are ready to prove the main result of this section.

Theorem 4.4. Let k be a positive integer and G be a 2-connected graph containing a non-separating
induced odd cycle. If the minimum degree of G is at least k + 1, then G contains k cycles of consecutive
lengths.

Proof. The theorem is obvious when k = 1. For the case k = 2, let C0 be an induced non-separating odd
cycle in G and x, y ∈ V (C0) such that x, y divide C0 into two subpaths say P1, P2 of lengths diﬀering
by one. Since G has minimum degree at least three, each of x, y has at least one neighbor in G − V (C0)
and thus there exists a path L from x to y in G[(V (G) − V (C0)) ∪ {x, y}]. Then L ∪ P1 and L ∪ P2 are
two cycles of consecutive lengths in G.
So we may assume that k ≥ 3. By Lemma 4.2, there exists a non-separating induced odd cycle
C = v0v1...v2sv0 in G satisfying the conclusions of Lemma 4.2. In particular, the minimum degree of
G − V (C) is at least k − 1. Throughout the rest of the proof of this theorem, the subscripts will be
taken under the additive group Z2s+1.
Suppose that C is a triangle v0v1v2v0. Consider the graph G′ obtained from G by contracting v1
and v2 into a vertex u. Then G′ is 2-connected with minimum degree at least k. By Theorem 3.1, there
are k − 1 admissible paths in G′ from u to v0. By the deﬁnition of admissible paths, each of these paths
has length at least two, so it does not contain the edge uv0, and each of those paths corresponds to a
path in G − V (C) from v0 to some vi ∈ {v1, v2}. Concatenating with v0vi and v0v3−ivi, these paths
lead to cycles of at least k consecutive lengths in G.
Therefore we may assume that C is not a triangle and hence s ≥ 2. For any two vertices vi, vj in
C, denote C ′
i,j and C ′′
i,j to be the shorter and longer paths in C from vi to vj, respectively.
Suppose that G − V (C) is 2-connected. We ﬁrst assume that for every v ∈ V (G − C), |NG(v) ∩
V (C)| ≤ 1. Then the minimum degree of G−V (C) ≥ k. Since G has minimum degree at least k +1 ≥ 4,
there exist distinct vertices x, y ∈ V (G − C) such that xv0, yvs ∈ E(G). By Theorem 3.1, G − V (C)
contains k − 1 admissible paths P1, ..., Pk−1 from x to y. Note that C ′
0,s and C ′′
0,s are two paths from

14

v0 to vs of lengths s and s + 1, respectively. Concatenating each of C ′
0,s and C ′′
0,s with v0x ∪ Pi ∪ yvs
for all i ∈ [k − 1] leads to k cycles of consecutive lengths in G. Hence we may assume that there exists
some u ∈ V (G − C) adjacent in G to two vertices of C. By Lemma 4.2, without loss of generality, let
NG(u) ∩ V (C) = {v1, v2s}. Since C is an induced cycle and d(vs) ≥ δ(G) ≥ k + 1 ≥ 4, there exists a
vertex w ∈ V (G − C) − {u} such that wvs ∈ E(G). Since G − V (C) has minimum degree at least k − 1,
by Theorem 3.1, G − V (C) contains k − 2 admissible paths R1, ..., Rk−2 from u to w. Observe that
uv1 ∪ C ′
1,s, uv2s ∪ C ′
s,2s, uv2s ∪ C ′′
s,2s and uv1 ∪ C ′′
1,s are four paths from u to vs of lengths s, s + 1, s + 2
and s + 3, respectively. By concatenating each of these paths with vsw ∪ Ri for i ∈ [k − 2], we obtain
cycles of k + 1 consecutive lengths in G.
Therefore G − V (C) is not 2-connected. Let B be an end-block of G − V (C) with cut-vertex b.
Since every vertex in B − b has degree at least k − 1 ≥ 2 in B, B is 2-connected.
Suppose that |NG(v)∩V (C)| ≤ 1 for every vertex v ∈ V (B −b). Then every vertex in B other than b
has degree at least k in B. We ﬁrst assume that there exist x ∈ V (B − b) and y ∈ V (G − C) − V (B − b)
such that vjx, vj+sy ∈ E(G) for some j, then by Theorem 3.1, B contains k − 1 admissible paths
P1, ..., Pk−1 from x to b. Let P be a path in G − (V (C) ∪ V (B − b)) from b to y. Note that C ′
j,j+s, C ′′
j,j+s
are two paths of lengths s, s + 1, respectively. Then, by concatenating each of these paths with Pi
and P , we ﬁnd k cycles in G with consecutive lengths. Hence, we may assume that for every integer
j with 0 ≤ j ≤ 2s, if vj is adjacent to V (B − b), then NG(vj+s) ∩ V (G − C) ⊆ V (B − b). Since G is
2-connected, there is some vertex vi∗ of C adjacent in G to V (B − b). Since k + 1 ≥ 4, every vertex
in V (C) is adjacent in G to some vertex in V (G − C). So ∅ ̸= NG(vi∗+s) − V (C) ⊆ V (B − b). Hence
we can inductively show that NG(vi∗+rs) − V (C) ⊆ V (B − b) for every positive integer r. Since s is
a generator of Z2s+1, NG(C) ⊆ V (B − b). This implies that b is a cut-vertex of G, contradicting the
2-connectivity of G.
Therefore there exists a vertex x ∈ V (B − b) with at least two neighbors in V (C). By Lemma 4.2,
without loss of generality, we may assume that NG(x) ∩ V (C) = {v1, v2s}. Assume there exists some
y ∈ V (G − C) − V (B − b) such that vsy ∈ E(G). Since every vertex in B − b has degree at least
k − 1 in B, by Theorem 3.1, B contains k − 2 admissible paths Q1, ..., Qk−2 from x to b. Let Q be
a ﬁxed path in G − (V (C) ∪ V (B − b)) from b to y. Note that xv1 ∪ C ′
1,s, xv2s ∪ C ′
s,2s, xv2s ∪ C ′′
s,2s
and xv1 ∪ C ′′
1,s are four paths from x to vs of lengths s, s + 1, s + 2 and s + 3, respectively. By
concatenating each of these paths with Qi ∪ Q ∪ yvs, we ﬁnd k + 1 cycles of consecutive lengths in G.
Hence we have NG(vs) ∩ V (G − C) ⊆ V (B − b). Since |NG(vs) ∩ V (G − C)| ≥ k − 1 ≥ 2, there exists
z ∈ NG(vs) ∩ V (B) − {x, b}. If k ≤ 4, then using the above four paths from x to vs, together with vsz
and a path in B from z to x, we obtain cycles of four consecutive lengths in G. So we may assume
k ≥ 5. Note that every vertex of B other than b has degree at least k − 1 ≥ 4 in B. By Lemma 4.3, B
has k − 3 admissible paths R1, ..., Rk−3 from x to z. Again, concatenating each of these paths with zvs
and the four paths from x to vs, one can ﬁnd cycles of k consecutive lengths in G. This completes the
proof of Theorem 4.4.

Using Theorem 4.4, we can derive Theorems 1.4 and 1.11 easily.

Theorem 1.4. Every non-bipartite 3-connected graph with minimum degree at least k + 1 contains k
cycles of consecutive lengths.

Proof. This theorem immediately follows from Lemma 4.1 and Theorem 4.4.

We say that a graph G is k-critical, if it has chromatic number k but every proper subgraph of G
has chromatic number less than k.
We now prove Theorem 1.11, which we restate as the following.

15

Theorem 4.5. For every positive integer k, every graph with chromatic number at least k + 2 contains
k cycles of consecutive lengths.

Proof. Let G be any graph with chromatic number at least k + 2. We may assume that k ≥ 2, for
otherwise the theorem is obvious. Then there exists a (k + 2)-critical subgraph G′ of G. It is easy to see
that G′ is 2-connected and has minimum degree at least k + 1. It is known that for any integer t ≥ 4,
every t-critical graph contains a non-separating induced odd cycle (the case t = 4 was explicitly stated
and proved by Krusenstjerna-Hafstrøm and Toft [14, Theorem 4], but their proof works for every t ≥ 4
as well). Therefore G′ contains a non-separating induced odd cycle. By Theorem 4.4, we see that G′

(and thus G) contains k cycles of consecutive lengths.

5 Dean’s conjecture

In this section we prove Conjecture 1.8, which will be divided into several lemmas. For a brief overview
of the coming proof, we would suggest readers to have a sketch on the proof of Theorem 5.15, which is
a restatement of Theorem 1.9.
Deﬁne K −
4 to be the graph obtained from K4 by deleting one edge. A chord of a cycle C in a graph
G is an edge e ∈ E(G) − E(C) such that the both ends of e belong to V (C). For a positive integer
t ≥ 4, we deﬁne K ′
t to be the graph obtained from Kt by deleting v1v4 and vivj for every i ∈ {1, 2} and
j ∈ {5, 6, ..., t}, where V (Kt) = {vk : 1 ≤ k ≤ t}. Note that K ′
t contains a Hamilton cycle. Also, for
every positive integer d, let K −
d,d be the graph obtained from Kd,d by deleting an edge.

Lemma 5.1. Let d and t be integers with d + 1 ≥ t ≥ 5. Let G be a graph containing a K −
4 subgraph
but not containing a K ′
t subgraph. If G is (t − 1)-connected, then G contains d cycles of consecutive
lengths.

Proof. Let {x, y, a, b} be a set of four vertices of G inducing a K −
4 subgraph, where x is of degree two
in this K −
4 subgraph and y is a neighbor of x. So there exists a clique in G − {x, y} containing a, b. Let
K be a maximal clique in G − {x, y} containing a, b. Note that |K| ≤ t − 3, for otherwise G[{x, y} ∪ K]
contains a K ′
t subgraph. Hence G − K is 2-connected since G is (t − 1)-connected.
By the maximality of K, every vertex in G − (K ∪ {x, y}) is adjacent in G to at most |K| − 1 vertices
in K. So ((G − K) − xy, x, y) is a 2-connected rooted graph of minimum degree at least d − |K| + 1.
By Theorem 3.1, there exist d − |K| admissible x-y paths P1, P2, ..., Pd−|K| in (G − K) − xy. Note that
there exist |K| + 1 x-y paths Q1, Q2, ..., Q|K|+1 in G[K ∪ {x, y}] with consecutive lengths. For every
integers i, j with 1 ≤ i ≤ d − |K| and 1 ≤ j ≤ |K| + 1, let Ci,j be the cycle obtained by concatenating Pi
and Qj. Let C = {Ci,j : 1 ≤ i ≤ d − |K|, 1 ≤ j ≤ |K| + 1}. If P1, P2, ..., Pd−|K| have consecutive lengths,
then C contains d cycles of consecutive lengths. If the lengths of P1, P2, ..., Pd−|K| form an arithmatic
progression of length two, then C contains 2d − |K| − 2 ≥ d cycles of consecutive lengths.

Lemma 5.2. Let d ≥ 3 be an integer. Let G be a 3-connected graph of minimum degree at least d. If
G contains a K3 subgraph but does not contain a K −
4 subgraph, then G contains d cycles of consecutive
lengths.

Proof. Let {a, b, c} be a set of three vertices of G that induces a K3 subgraph. Let G′ be the graph
obtained from G by contracting the edge bc into a new vertex a∗ and deleting resulting loops and
parallel edges. Since G is 3-connected, G′ is 2-connected, so (G′ − aa∗, a, a∗) is a 2-connected rooted
graph. Since G does not contain a K −
4 subgraph, (G′ − aa∗, a, a∗) has minimum degree at least d. By
Theorem 3.1, there exist d − 1 admissible a-a∗ paths P1, P2, ..., Pd−1 in G′ − aa∗. So there exist paths
P ′
1, P ′
2, ..., P ′
d−1 in G such that their lengths form an arithmetic progression of common diﬀerence one or

16

two, and for every i with 1 ≤ i ≤ d − 1, P ′
i is either an a-b path disjoint from c or an a-c path disjoint
from b. For every integer i with 1 ≤ i ≤ d − 1, let Ci,1 = P ′
i + ab, Ci,2 = P ′
i + ac, Ci,3 = P ′
i ∪ abc, and let
Ci,4 = P ′
i ∪ acb. Then the set {Ci,j : 1 ≤ i ≤ d − 1, 1 ≤ j ≤ 4} contains d cycles of consecutive lengths.

Lemma 5.3. Let ℓ be a positive integer. Let A be a subset of integers such that ℓ elements of A form
an arithmetic progression of common diﬀerence r, where r ∈ {1, 2}.

1. If r = 1 and ℓ ≥ 3, then for every integer x, the set {a + x, a + x + 3 : a ∈ A} contains ℓ + 3
elements that form an arithmetic progression of common diﬀerence one.

2. If r = 2 and ℓ ≥ 2, then for every integer x, the set {a + x, a + x + 3 : a ∈ A} contains 2ℓ − 2
elements that form an arithmetic progression of common diﬀerence one.

Proof. Let a1, a2, ..., aℓ be ℓ elements of A forming an arithmetic progression of common diﬀerence r,
where r ∈ {1, 2}. We may assume that for every i with 1 ≤ i ≤ ℓ, ai = a1 + (i − 1)r. Let x be any
integer, and let S = {ai + x, ai + x + 3 : 1 ≤ i ≤ ℓ}.
If r = 1 and ℓ ≥ 3, then S = {i : a1 + x ≤ i ≤ a1 + ℓ − 1 + x + 3}. If r = 2 and ℓ ≥ 2, then S
contains {i : a1 + 2 + x ≤ i ≤ a1 + 2(ℓ − 1) + x + 1}. This proves the lemma.

Lemma 5.4. Let d be an integer with d ≥ 6. If G is a 3-connected non-bipartite graph with minimum
degree at least d that does not contain a K3 subgraph, then either

1. G contains d cycles of consecutive lengths, or

2. d ∈ {6, 7} and there exists an induced cycle C in G, denoted by v0v1v2...v2sv0, of length at least
ﬁve such that

(a) G − V (C) is connected but not 2-connected,

(b) every end-block of G − V (C) is 2-connected, and

(c) for every non-cut vertex v of G − V (C), |NG(v) ∩ V (C)| ≤ 2, and if |NG(v) ∩ V (C)| = 2,
then NG(v) ∩ V (C) = {vi, vi+2} for some i ∈ Z2s+1 and the indices are computed in Z2s+1.

Proof. We may assume that G does not contain d cycles of consecutive lengths, for otherwise we are
done.
By Lemmas 4.1 and 4.2, since G does not contain a K3 subgraph, there exists an induced odd cycle
C of length at least ﬁve, denoted by v0v1...v2sv0, such that for every non-cut vertex v of G − V (C),
|NG(v) ∩ V (C)| ≤ 2, and if |NG(v) ∩ V (C)| = 2, then NG(v) ∩ V (C) = {vi, vi+2} for some i ∈ Z2s+1
and the indices are computed in Z2s+1.
In particular, no vertex of G − V (C) is of degree at most one in G − V (C), since d ≥ 4. So every
end-block of G − V (C) is 2-connected. Note that for every end-block B of G − V (C), there exists at
most one cut-vertex of G − V (C) contained in V (B), and if such vertex exists, we denote it by bB.
So to prove this lemma, it suﬃces to prove that d ∈ {6, 7} and G − V (C) is not 2-connected.
We ﬁrst suppose to the contrary that G − V (C) is 2-connected.
Suppose that there exists a vertex x ∈ V (G) − V (C) adjacent in G to at least two vertices in
V (C). By symmetry, we may assume that x is adjacent to v0 and v2. Since G is 3-connected and
C is an induced cycle in G, vs+1 is adjacent in G to a vertex y in V (G) − V (C). Since |V (C)| ≥ 5,
vs+1 ̸∈ {v0, v2}, so x ̸= y. Since G − V (C) is 2-connected, every vertex in G − V (C) has degree at
least d − 2, so by Theorem 3.1, there exist d − 3 admissible paths P1, P2, ..., Pd−3 in G − V (C) from
x to y. Let Q1, Q2 be the subpaths of C with ends v0 and vs+1 of length s + 1 and s, respectively.
Let Q3, Q4 be the subpaths of C with ends v2 and vs+1 of length s − 1 and s + 2, respectively. Let

17

C = {(Pi ∪ Qj) + xv0 + yvs+1, (Pi ∪ Qk) + xv2 + yvs+1 : 1 ≤ i ≤ d − 3, 1 ≤ j ≤ 2, 3 ≤ k ≤ 4}. Then C
contains (d − 3) + 4 − 1 = d cycles of consecutive lengths, a contradiction.
So every vertex x ∈ V (G) − V (C) is adjacent in G to at most one vertex in V (C). Since G is
connected, there exists a vertex x′ in V (G) − V (C) adjacent in G to a vertex in V (C). By symmetry,
we may assume that x′ is adjacent to v0. Since G is 3-connected and C is an induced cycle in G, vs−1 is
adjacent in G to a vertex y′ in V (G) − V (C). Since |V (C)| ≥ 5, v0 ̸= vs−1, so x ̸= y. Since every vertex
in G − V (C) has degree at least d − 1, by Theorem 3.1, there exist d − 2 admissible paths P ′
1, P ′
2, ..., P ′
d−2
in G − V (C) from x′ to y′. Let Q′
1, Q′
2 be the subpaths of C with ends v0 and vs−1 of length s − 1 and
s + 2, respectively. Let C′ = {(P ′
i ∪ Q′
j) + xv0 + yvs−1 : 1 ≤ i ≤ d − 2, 1 ≤ j ≤ 2}. Since d − 2 ≥ 3, C′

contains min{d − 2 + 3, 2(d − 2) − 2} ≥ d cycles of consecutive lengths by Lemma 5.3, a contradiction.
Hence G − V (C) is not 2-connected. It suﬃces to prove d ∈ {6, 7}. Suppose to the contrary that
d ≥ 8.
Suppose that there exists an end-block B of G − V (C) and a vertex x ∈ V (B) − {bB} adjacent
in G to vix in V (C) for some 0 ≤ ix ≤ 2s, such that vix+s−1 is adjacent in G to a vertex y ∈
V (G) − (V (C) ∪ (V (B) − {bB})), where the indices are computed in Z2s+1. Since (B, x, bB) is a 2-
connected rooted graph of minimum degree at least d − 2, Theorem 3.1 implies that there exist d − 3
admissible paths in B from x to bB, and hence by concatenating each of them with a ﬁxed path in
G−(V (C)∪(V (B)−{bB})) from bB to y, there exist d−3 admissible paths P ′′
1 , P ′′
2 , ..., P ′′
d−3 in G−V (C)
from x to y. Let Q′′
1, Q′′
2 be the subpaths of C with ends vix and vix+s−1 of length s − 1 and s + 2,
respectively. Let C′′ = {(P ′′
i ∪ Q′′
j ) + xvix + yvix+s−1 : 1 ≤ i ≤ d − 3, 1 ≤ j ≤ 2}. Since d − 3 ≥ 3, by
Lemma 5.3, C′′ contains min{(d − 3) + 3, 2(d − 3) − 2} = min{d, 2d − 8} cycles of consecutive lengths.
Since G does not contain d cycles of consecutive lengths, 2d − 8 < d. Hence d ∈ {6, 7}, a contradiction.
Hence for every end-block B of G − V (C) and every vertex x ∈ V (B) − {bB} adjacent in G to vix
for some 0 ≤ ix ≤ 2s, NG(vix+s−1) ⊆ V (B) − {b}, where the indices are computed in Z2s+1. Similarly,
for every end-block B of G − V (C) and every vertex x ∈ V (B) − {bB} adjacent in G to vix for some
0 ≤ ix ≤ 2s, NG(vix−(s−1)) ⊆ V (B) − {b}, where the indices are computed in Z2s+1.
For every end-block B of G − V (C), let SB = {i : 0 ≤ i ≤ 2s, vi ∈ NG(B − bB)}. Note that for every
end-block B and i ∈ Z2s+1, if i ∈ SB, then {i + (s − 1), i − (s − 1)} ⊆ SB − SB′ for every end-block B′

of G − V (C) other than B. So if s − 1 is relatively prime to 2s + 1, then SB = {i : 0 ≤ i ≤ 2s} for every
end-block B, but there are at least two end-blocks of G − V (C), a contradiction.
Hence s − 1 is not relatively prime to 2s + 1. So there exists a prime p that divides s − 1 and 2s + 1.
Hence p divides (2s + 1) − 2(s − 1) = 3. That is, p = 3, and 3 is the greatest common divisor of 2s + 1
and s − 1. So for every end-block B and i ∈ Z, if i ∈ SB, then since SB contains i + t(s − 1) for every
integer t, where the computation is in Z2s+1, SB contains i + 3t′ for every integer t′. Hence for every
i ∈ {0, 1, 2}, either SB ⊇ {i + 3t : t ∈ Z} or SB ∩ {i + 3t : t ∈ Z} = ∅, where the computation is in
Z2s+1. Since there are at least two end-blocks in G − V (C), there exists an end-block B∗ such that
there uniquely exists i∗ ∈ {0, 1, 2} such that SB∗ ∩ {i∗ + 3t : t ∈ Z} ̸= ∅. This implies that every vertex
in B∗ − bB∗ is adjacent in G to at most one vertex in V (C).
By symmetry, we may assume that i∗ = 0, and there exist x∗, y∗ ∈ V (B∗) − {bB∗ } such that
x∗v0 ∈ E(G) and y∗vs−1 ∈ E(G). Since G is 3-connected, x∗ and y∗ can be chosen to be distinct
vertices. Hence x∗, y∗, bB∗ are distinct vertices. Since B is 2-connected and every vertex in B∗ other
than bB∗ is of degree at least d−1 in B∗, by Lemma 4.3 there exist d−3 admissible paths P ∗
1 , P ∗
2 , ..., P ∗
d−3
in B∗ from x∗ to y∗. Let Q∗
1, Q∗
2 be the subpaths of C with ends v0 and vs−1 of length s − 1 and s + 2,
respectively. Let C∗ = {(P ∗
i ∪ Q∗
j ) + v0x∗ + vs−1y∗ : 1 ≤ i ≤ d − 3, 1 ≤ j ≤ 2}. Since d − 3 ≥ 3, by
Lemma 5.3, C∗ contains min{d − 3 + 3, 2(d − 3) − 2} cycles of consecutive lengths. Since G does not
contain d cycles of consecutive lengths, 2d − 8 < d. Hence d ∈ {6, 7}, a contradiction. This proves the
lemma.
 18

Lemma 5.5. Let d be an integer with d ≥ 6. If G is a 3-connected non-bipartite graph with minimum
degree at least d that does not contain a K3 subgraph, then G contains d admissible cycles. Furthermore,
if d ≥ 8, then G contains d cycles of consecutive lengths; and if d ∈ {6, 7}, then G contains cycles of
all lengths modulo d.

Proof. We may assume that G does not contain d cycles of consecutive lengths, for otherwise we are
done. By Lemma 5.4, d ∈ {6, 7} and there exists an induced cycle C in G, denoted by v0v1v2...v2sv0,
of length at least ﬁve such that

• G − V (C) is connected but not 2-connected,

• every end-block of G − V (C) is 2-connected, and

• for every non-cut vertex v of G − V (C), |NG(v) ∩ V (C)| ≤ 2, and if |NG(v) ∩ V (C)| = 2, then
NG(v) ∩ V (C) = {vi, vi+2} for some i ∈ Z2s+1 and the indices are computed in Z2s+1.

Since d ∈ {6, 7}, to prove this lemma, it suﬃces to prove that G contains d admissible cycles, and prove
that G contains cycles of all lengths modulo d. Note that if d = 7 and G contains d admissible cycles,
then G contains cycles of all lengths modulo d.
Suppose to the contrary that either G does not contain d admissible cycles, or d = 6 and G does
not contain cycles of all lengths modulo d.
Since G − V (C) is not 2-connected and every end-block of G − V (C) is 2-connected, for every end-
block B of G − V (C), there exists exactly one vertex bB in B such that bB is a cut-vertex of G − V (C).
For every end-block B of G−V (C), let uB be a vertex in B −{bB} such that |NG(uB)∩V (C)| is as large
as possible. Note that for every end-block B of G − V (C), (B, uB, bB) is a 2-connected rooted graph
of minimum degree at least d − |NG(uB) ∩ V (C)|, so there exist d − |NG(uB) ∩ V (C)| − 1 admissible
paths PB,1, PB,2, ..., PB,d−|NG(uB )∩V (C)|−1 in B from uB to bB. In addition, for every end-block B of
G − V (C), 1 ≤ |NG(uB) ∩ V (C)| ≤ 2 since uB ∈ V (B) − {bB}.
Suppose that there exists an end-block B1 of G − V (C) such that |NG(uB1 ) ∩ V (C)| = 1. Let B2
be an end-block of G − V (C) other than B1. Let x ∈ NG(uB1 ) ∩ V (C). Since G is 3-connected, uB2
can be chosen such that NG(uB2) ∩ V (C) − {x} ̸= ∅. Let y ∈ NG(uB2) ∩ V (C) − {x}. Let Q be a path
in C from x to y. Let R be a path in G − V (C) from bB1 to bB2. Let C = {(PB1,i ∪ R ∪ PB2,j ∪ Q) +
xuB1 + yuB2 : 1 ≤ i ≤ d − |NG(uB1) ∩ V (C)| − 1, 1 ≤ j ≤ d − |NG(uB2 ) ∩ V (C)| − 1}. So C contains
(d − |NG(uB1 ) ∩ V (C)| − 1) + (d − |NG(uB2) ∩ V (C)| − 1) − 1 = 2d − 4 − |NG(uB2) ∩ V (C)| ≥ 2d − 6 ≥ d
admissible cycles. Hence d = 6 and G does not contain d cycles of consecutive lengths. So the lengths
of the cycles in C form an arithmetic progression of common diﬀerence two. It follows that the set
{PB1,i ∪ R ∪ PB2,j : 1 ≤ i ≤ d − |NG(uB1) ∩ V (C)| − 1, 1 ≤ j ≤ d − |NG(uB2 ) ∩ V (C)| − 1} contains
2d − 6 paths whose of lengths form an arithmetic progression of common diﬀerence two from uB1 to
uB2 in G − V (C). Let Qo be the odd path from x to y in C and Qe be the even path from x to y in
C. By concatenating each of Qo and Qe with PB1,i ∪ R ∪ PB2,j ∪ xuB1 ∪ yuB2, we could obtain 2d − 6
cycles of consecutive odd lengths and 2d − 6 cycles of consecutive even lengths. Since d = 6 is even, G
contains cycles of all lengths modulo d.
Hence for every end-block B of G − V (C), |NG(uB) ∩ V (C)| = 2. Let B3, B4 be two distinct end-
blocks of G − V (C). By symmetry, we may assume that NG(uB3) ∩ V (C) = {v0, v2}. Since G does not
contain a K3 subgraph, |NG(uB4 ) ∩ V (C) ∩ {v0, v1}| ≤ 1, so there exists z ∈ NG(uB4) ∩ V (C) − {v0, v1}.
Let Q1 be the path in C from v0 to z containing v0v1v2, and let Q2 be the subpath of Q1 from
v2 to z. Note that |E(Q1)| = |E(Q2)| + 2. Let R′ be a path in G − V (C) from bB3 to bB4. Let
C′ = {(PB3,i ∪ R′ ∪ PB4,j ∪ Q1) + uB3v0 + uB4z, (PB3,i ∪ R′ ∪ PB4,j ∪ Q2) + uB3v2 + uB4z : 1 ≤ i ≤
d − |NG(uB3 ) ∩ V (C)| − 1, 1 ≤ j ≤ d − |NG(uB4) ∩ V (C)| − 1}. Since |E(Q1)| = |E(Q2)| + 2, C′ contains

19

(d − |NG(uB3) ∩ V (C)| − 1) + (d − |NG(uB4) ∩ V (C)| − 1) − 1 + 2 − 1 = 2d − 6 ≥ d admissible cycles.
So d = 6 and G does not contain d cycles of consecutive lengths. Hence the lengths of these cycles
form an arithmetic progression of common diﬀerence two. It follows that PB3,i ∪ R′ ∪ PB4,j for all
1 ≤ i ≤ d − |NG(uB3) ∩ V (C)| − 1 and 1 ≤ j ≤ d − |NG(uB4) ∩ V (C)| − 1 contains 2d − 7 paths whose of
lengths form an arithmetic progression of common diﬀerence two between uB3 to uB4 in G − V (C). Let
Q′
o and Q′
e be the odd path and even path in C from z to v0, respectively. By concatenating each of Q′
o
and Q′
e with PB3,i ∪ R′ ∪ PB4,j ∪ uB3v0 ∪ uB4 z, we obtain 2d − 7 cycles of consecutive odd lengths and
2d − 7 cycles of consecutive even lengths. Since d = 6 is even, G contains cycles of all lengths modulo
d, a contradiction. This proves the lemma.

Recall that for every positive integer d, K −
d,d is the graph obtained from Kd,d by deleting an edge.

Lemma 5.6. Let d ≥ 3 be an integer. Let G be a max{d, 5}-connected graph of girth exactly four and
of minimum degree at least d that does not contain a cycle of length ﬁve. If G does not contain a K −
d,d
subgraph, then G contains d admissible cycles.

Proof. Suppose to the contrary that G does not contain d admissible cycles.
Since the girth of G equals four, G contains a K2,2 subgraph. So there exists a complete bipartite
subgraph Q of G with bipartition (Q1, Q2) such that

(i) 2 ≤ |Q1| ≤ |Q2|,

(ii) subject to (i), |Q1| is maximum, and

(iii) subject to (i) and (ii), |Q2| is maximum.

Let s = |Q1|. Note that 2 ≤ s ≤ d − 1 since G does not contain a Kd,d subgraph. Since G does not
contain a K3 subgraph, Q is an induced subgraph of G, and for every vertex v of G − V (Q), either
NG(v) ∩ Q1 = ∅ or NG(v) ∩ Q2 = ∅.
For any v ∈ V (G) − V (Q), |NG(v) ∩ Q1| ≤ s − 1 by (iii), and |NG(v) ∩ Q2| ≤ s by (ii). If there exists
a vertex z ∈ V (G) − V (Q) such that z is adjacent in G to at least s vertices in V (Q), then let Z = {z};
otherwise, let Z be the empty set. Note that if Z ̸= ∅, then NG(z) ∩ V (Q) ⊆ Q2 and |Q2| ≥ s + 1, since
G is of girth four and by (i)-(iii).
Suppose there exists t ∈ {1, 2} such that there exists a component M of G − (Qt ∪ Z) disjoint
from Q3−t. Since G is d-connected, |Qt| + |Z| ≥ d. If |Qt| = s, then since d ≥ s + 1, Z ̸= ∅ and
|Qt| = s = d − 1, so t = 1 and |Q3−t| ≥ s + 1 = d, and hence G[V (Q) ∪ Z] contains a K −
d,d subgraph,
a contradiction. Hence |Qt| ≥ s + 1. In particular, t = 2. Note that when s = 2, |Qt| ≥ s + 2, for
otherwise |Qt| + |Z| ≤ (s + 1) + 1 = 4, contradicting that G is 5-connected. Since G − Z is 4-connected,
we have that |NG(M ) ∩ Qt| ≥ 4. If s = 2, let A be a subset of NG(M ) ∩ Qt − NG(z) with size two; if
s ≥ 3, let A be a subset of NG(M ) ∩ Qt with size two. Note that NG(M ) ∩ Qt − A ̸= ∅. If |Qt| = s + 1
and Z ̸= ∅, then let ǫ = 1; for otherwise, let ǫ = 0. Let GM be the graph obtained from G[V (M ) ∪ Qt]
by identifying all vertices in A into a vertex uM , identifying all vertices in Qt − A into a vertex vM , and
deleting all resulting loops and parallel edges. Since |Qt| ≥ s + 1 and t = 2, and since G is of girth four
and does not contain a 5-cycle, no vertex of M is adjacent in G to both Z and Q2, so the minimum
degree of (GM , uM , vM ) is at least d − (s − 2) − |Z| + ǫ by the deﬁnition of Z. So (GM , uM , vM ) is a
rooted graph of minimum degree at least d − (s − 2) − |Z| + ǫ. Since G − Z is 3-connected and M is a
component of G− (Qt ∪ Z), we know (GM , uM , vM ) is a 2-connected rooted graph of minimum degree at
least d − s + 2 − |Z| + ǫ. By Theorem 3.1, there exist d − s + 1 − |Z| + ǫ admissible paths in GM from uM
to vM . So there exist d − s + 1 − |Z| + ǫ admissible paths PM,1, PM,2, ..., PM,d−s+1−|Z|+ǫ in G[V (M ) ∪ Qt]
from A to Qt − A internally disjoint from V (Q) ∪ Z. For each i with 1 ≤ i ≤ d − s + 1 − |Z| + ǫ, let αi

20

be the ends of PM,i in A and let βi be the end of PM,i in Qt − A. Since |Qt| ≥ s + 1 and t = 2 and Q is
a complete bipartite graph, there exist s + |Z| − ǫ admissible paths QM,1, ..., QM,s+|Z|−ǫ in G[V (Q) ∪ Z]
from αi to βi. Then the set {PM,j ∪ QM,k : 1 ≤ j ≤ d − s + 1 − |Z| + ǫ, 1 ≤ k ≤ s + |Z| − ǫ} contains
(d − s + 1 − |Z| + ǫ) + (s + |Z| − ǫ) − 1 = d admissible cycles, a contradiction.
So for every t ∈ {1, 2}, every component of G − (Qt ∪ Z) intersects Q3−t. Let G′ be the graph
obtained from G − Z by identifying all vertices in Q1 into a vertex u′, identifying all vertices in Q2
into a vertex v′, and deleting resulting loops and parallel edges. Since G is of girth four and does not
contain a 5-cycle, no vertex of G − (V (Q) ∪ Z) is adjacent in G to either both Z and Q2 or both Q1 and
Q2, so the minimum degree of (G′, u′, v′) is at least d − (s − 2) − |Z| by the deﬁnition of Z. Since G is
3-connected, G − Z is 2-connected, so every cut-vertex of G′ is u′ or v′. Since for every t ∈ {1, 2}, every
component of G − (Qt ∪ Z) intersects Q3−t, we know G′ is 2-connected. So (G′, u′, v′) is a 2-connected
rooted graph of minimum degree at least d − s − |Z| + 2. By Theorem 3.1, there exist d − s − |Z| + 1
admissible paths in G′ from u′ to v′. So there exist d− s − |Z|+ 1 admissible paths R1, R2, ..., Rd−s−|Z|+1
in G − Z from Q1 to Q2 internally disjoint from V (Q). For every i with 1 ≤ i ≤ d − s − |Z| + 1, let
xi, yi be the ends of Ri in Q1, Q2, respectively. Since Q is a complete bipartite graph, for each i with
1 ≤ i ≤ d − s − |Z| + 1, G[V (Q) ∪ Z] contains s + |Z| admissible paths R′
1, R′
2, ..., R′
s+|Z| from xi to
yi. So the set {Rj ∪ R′
k : 1 ≤ j ≤ d − s − |Z| + 1, 1 ≤ k ≤ s + |Z|} contains d admissible cycles, a
contradiction. This proves the lemma.

Lemma 5.7. Let G be a 3-connected bipartite graph. If G does not contain a cycle of length four,
then G contains a non-separating induced cycle C such that for every non-cut-vertex v of G − V (C),
|NG(v) ∩ V (C)| ≤ 1.

Proof. Let C be a cycle of G such that

(i) the largest component of G − V (C) is as large as possible, and

(ii) subject to (i), |V (C)| is as small as possible.

Let M be a component of G − V (C) with |V (M )| maximum.
If there exists a chord e of C, then one of Pe + e and Qe + e is a cycle shorter than C such that M
is a component of the graph obtained from G by deleting this cycle, a contradiction, where Pe, Qe are
the two subpaths of C with ends the same as e. Hence C is an induced cycle.
Suppose there exists a component M ′ of G − V (C) other than M . Let A = NG(M ) ∩ V (C) and
B = NG(M ′) ∩ V (C). Since G is 3-connected, min{|A|, |B|} ≥ 3. Since |A| ≥ 3 and |B| ≥ 2, there
exists a subpath Q of C whose ends belong to B such that some internal vertex of Q belongs to A.
Since M ′ is connected, there exists a path Q′ from one end of Q to another end of Q such that all
internal vertices belong to V (M ′). Let Q′′ be the subpath of C with the same ends as Q but internally
disjoint from Q. Then Q′ ∪ Q′′ is a cycle in G such that some component of G − V (Q′ ∪ Q′′) contains
M and a vertex in A, contradicting (i).
Hence C is a non-separating cycle in G. Suppose that there exists a non-cut-vertex v of G − V (C)
such that |NG(v) ∩ V (C)| ≥ 2. Let x, y be distinct vertices in NG(v) ∩ V (C) such that no internal
vertex of R1 belongs to NG(v) ∩ V (C), where R1, R2 are the two subpaths of C with ends x and y. If
|E(R1)| ≤ 2, then R1 + vx + vy is a cycle of length at most four, contradicting that G is a bipartite
graph with no 4-cycle. So |E(R1)| ≥ 3. Hence R2 +vx+vy is a cycle shorter than C. Since |E(R1)| ≥ 3,
there exist distinct internal vertices x′, y′ of R1. Since C is an induced cycle and every vertex of G
has degree at least three, NG(x′) − V (C) ̸= ∅ ̸= NG(y′) − V (C). Since C is a non-separating cycle,
NG(x′) ∩ V (M ) = NG(x′) − V (C) ̸= ∅ ̸= NG(y′) − V (C) = NG(y′) ∩ V (M ). Since x′, y′ are internal
vertices of R1, {x′, y′} ∩ NG(v) = ∅. So NG(x′) ∩ V (M ) − {v} ̸= ∅ and NG(y′) ∩ V (M ) − {v} ̸= ∅. Since

21

v is not a cut-vertex of G − V (C), M − v is connected. So some component of G − V (R2 + vx + vy)
contains (V (M ) − {v}) ∪ {x′, y′}, contradicting (i). This proves the lemma.

Lemma 5.8. Let d ≥ 5 be an integer. Let G be a 3-connected bipartite graph of minimum degree at
least d. If G does not contain cycles of length four, then G contains d admissible cycles.

Proof. Suppose to the contrary that G does not contain d admissible cycles. By Lemma 5.7, there
exists a positive integer s and an induced non-separating cycle C = v0v1 . . . v2s−1v0 in G such that for
every non-cut-vertex of G − V (C), it is adjacent in G to at most one vertex in V (C). Since G is a
bipartite graph with no 4-cycle, s ≥ 3. For any any 0 ≤ i < j ≤ 2s − 1, let Qi,j and Q′
i,j be the two
subpaths of C with ends vi, vj.
Suppose G − V (C) is 2-connected. Since C is an induced non-separating cycle and G is of minimum
degree at least d ≥ 4, there exist distinct vertices x, y in V (G) − V (C) such that {xv0, yvs−2} ∈
E(G). Since (G − V (C), x, y) is a 2-connected rooted graph of minimum degree at least d − 1, there
exist d − 2 admissible paths P1, P2, ..., Pd−2 in G − V (C) from x to y by Theorem 3.1. Note that
||E(Q0,s−2)| − |E(Q′
0,s−2)|| = 4. Since d − 2 > 2 and G is bipartite, the set {(Pi ∪ Q0,s−2) + xv0 +
yvs−2, (Pi ∪ Q′
0,s−2) + xv0 + yvs−2 : 1 ≤ i ≤ d − 2} contains d admissible cycles, a contradiction.
So G−V (C) is not 2-connected. In particular, there exist two distinct end-blocks B1, B2 of G−V (C).
Since G is 3-connected, each B1, B2 is 2-connected. For i ∈ {1, 2}, let bi be the cut-vertex of G − V (C)
contained in V (Bi). Since G is 2-connected, for each i ∈ {1, 2}, there exists an integer ri with 0 ≤
ri ≤ 2s − 1 and a vertex ui in V (Bi) − {bi} such that uivri ∈ E(G). Since G is 3-connected, r1
and r2 can be chosen to be distinct. For i ∈ {1, 2}, since (Bi, ui, bi) is a 2-connected rooted graph of
minimum degree at least d − 1, there exist d − 2 admissible paths Pi,1, Pi,2, ..., Pi,d−2 in Bi from ui to
bi. Let Q be a path in G − V (C) from b1 to b2 internally disjoint from V (B1) ∪ V (B2). Then the set
{(P1,i ∪ Q ∪ P2,j ∪ Qr1,r2) + u1vr1 + u2vr2 : 1 ≤ i ≤ d − 2, 1 ≤ j ≤ d − 2} contains 2(d − 2) − 1 = 2d − 5 ≥ d
admissible cycles, a contradiction. This proves the lemma.

For every graph H, a 1-subdivision of H is a graph that is obtained from H by subdividing each
edge exactly once.

Lemma 5.9. Let G be a graph of girth at least ﬁve. Let H be a subgraph of G that is a 1-subdivision
of K4. If there exists a vertex in V (G) − V (H) adjacent in G to two vertices in V (H), then G contains
a cycle of length ﬁve or ten.

Proof. We may assume G is of girth at least six, for otherwise we are done. Let v be a vertex in
V (G) − V (H) adjacent in G to two vertices x, y in V (H). Let S be the set of vertices of H of degree
three. Since G has girth at least ﬁve, at least one of x, y does not belong to S. Then since G has girth
at least six, both x, y do not belong to S. So there exist edges e, e′ of K4 such that x and y are obtained
by subdividing e and e′, respectively. Since G has girth at least ﬁve, e and e′ form a matching in K4.
Let z be a vertex of H obtained by subdividing an edge other than e, e′. Then (H − {z}) + vx + vy has
a Hamiltonian cycle of length ten. This proves the lemma.

We say a graph is a theta graph is a subdivision of K −
4 . The branch vertices of a theta graph are
the vertices of degree at least three. A subgraph H of a graph G is spanning if V (H) = V (G).

Lemma 5.10. Let G be a graph of girth at least six that does not contain a cycle of length ten. Let H
be a subgraph of G isomorphic to a theta graph such that |V (H)| is minimum. Then the following hold.

1. H is an induced subgraph of G.

2. There exists at most one vertex of G − V (H) adjacent in G to at least two vertices in V (H).

22

3. If there exists a vertex v of G − V (H) adjacent in G to at least two vertices in V (H), then
G[V (H) ∪ {v}] is isomorphic to a 1-subdivision of K4.

Proof. Suppose that H is not induced. Then there exists e ∈ E(G) − E(H) with both ends in V (H).
Since the girth of G is at least six, there exists a subgraph H ′ of G with V (H ′) ⊂ V (H) such that H ′

is a theta graph, contradicting the minimality of |V (H)|.
So H is an induced subgraph. We may assume there exists a vertex v of G − V (H) adjacent in G
to at least two vertices in V (H), for otherwise we are done. Let x, y be the branch vertices of H. Let
P1, P2, P3 be the three internally disjoint paths in H from x to y.
By the minimality of |V (H)| and the girth condition of G, v is not adjacent to any branch vertices
of H. Similarly, for each i ∈ {1, 2, 3}, v is adjacent to at most one vertex in V (Pi). So there exist
distinct i, j such that v is adjacent to exactly one vertex a in V (Pi) − {x, y} and exactly one vertex b in
V (Pj) − {x, y}. By symmetry, we may assume i = 1 and j = 2. Since (H − (V (P3) − {x, y})) + av + bv
is a theta graph, by the minimality of |V (H)|, |V (P3)| ≤ 3. Let L1 be the subpath of P1 from x to
a. Since the graph obtained from H + av + bv by deleting all internal vertices of L1 is a theta graph,
L1 contains at most one internal vertex by the minimality of |V (H)|. Similarly, the subpath L2 of P2
from x to b contains at most one internal vertex. Since L1 ∪ L2 ∪ avb is a cycle in G and G has girth
at least six, both L1, L2 contain exactly one internal vertex. Similarly, each of the subpath of P1 from
a to y and the subpath of P2 from b to y contains exactly one vertex. Since P1 ∪ P3 is a cycle in G, P3
contains exactly one internal vertex. Hence G[V (H) ∪ {v}] contains a 1-subdivision of K4 as a spanning
subgraph. Since G is of girth at least six, G[V (H) ∪ {v}] is isomorphic to a 1-subdivision of K4.
If there exists a vertex v′ of V (G)−V (H) other than v adjacent in G to at least two vertices in V (H),
then v′ is adjacent in G to at least two vertices in V (H) ∪ {v} which induces a subgraph isomorphic to
a 1-subdivision of K4, so G contains a cycle of length ten by Lemma 5.9, a contradiction. So v is the
only vertex that is adjacent in G to at least two vertices in V (H). This proves the lemma.

Lemma 5.11. Let d ≥ 5 be an integer. Let G be a 5-connected graph of girth at least six and of
minimum degree at least d that does not contain a cycle of length ten. Let H be an induced subgraph of
G isomorphic to a 1-subdivision of K4. Then G contains d admissible cycles.

Proof. Suppose to the contrary that G does not contain d admissible cycles. Note that every vertex
of G − V (H) is adjacent in G to at most one vertex in V (H) by Lemma 5.9. We say a pair of two
distinct vertices x, y of H are useful if there exist paths H1, H2, H3 in H from x to y of lengths h1, h2, h3,
respectively, such that (h1, h2, h3) ∈ {(1, 5, 7), (2, 4, 6), (3, 5, 7)}.
Let M be a component of G − V (H). Since G is 5-connected, there exists a useful pair of vertices
x, y such that x is adjacent in G to some vertex x′ in V (M ) and y is adjacent in G to some vertex y′

in V (M ). Note that x′ ̸= y′, for otherwise some vertex of M is adjacent in G to two vertices in V (H).
Suppose M is 2-connected. Then (M, x′, y′) is a 2-connected rooted graph of minimum degree at
least d − 1. By Theorem 3.1, there exist d − 2 admissible paths P1, ..., Pd−2 in G′ from x′ to y′. Since
d ≥ 5, the set {(Pi ∪ Hj) + xx′ + yy′ : 1 ≤ i ≤ d − 2, 1 ≤ j ≤ 3} contains d admissible cycles, a
contradiction.
So M is not 2-connected. Let B1, B2 be two distinct end-blocks of M . Let b1, b2 be the cut-vertex
of G − V (H) contained in V (B1), V (B2), respectively. Since G is 3-connected, some vertex x1 in
V (B1) − {b1} is adjacent in G to some vertex u1 in V (H), and some vertex x2 in V (B2) − {b2} is
adjacent in G to some vertex u2 in V (H). For each i ∈ {1, 2}, since (Bi, xi, bi) is a 2-connected rooted
graph of minimum degree at least d − 1, there exist d − 2 admissible paths Qi,1, ..., Qi,d−2 in Bi from xi
to bi. Let Q be a path in M from b1 to b2 internally disjoint from V (B1) ∪ V (B2), and let Q′ be a path
in H from u1 to u2. Then the set {(Q1,i ∪ Q ∪ Q2,j ∪ Q′) + x1u1 + x2u2 : 1 ≤ i ≤ d − 2, 1 ≤ j ≤ d − 2}
contains 2(d − 2) − 1 = 2d − 5 ≥ d admissible cycles, a contradiction. This proves the lemma.

23

Lemma 5.12. Let H be a theta graph. Then there exist two distinct vertices x, y and three paths in H
from x to y such that the lengths of these three paths modulo 5 are pairwise distinct.

Proof. Let P1, P2, P3 be the three internally disjoint paths in H between the branch vertices of H. For
each i ∈ {1, 2, 3}, we denote Pi by vi,0vi,1...vi,|E(Pi)|, where v1,0 = v2,0 = v3,0. For each i ∈ {1, 2, 3} and
each j ∈ {1, ..., |E(Pi)|}, let Li,j = vi,0vi,1...vi,j and let Ri,j = vi,jvi,j+1...vi,|E(Pi)|.
Suppose to the contrary that there do not exist two distinct vertices x, y and three paths from x to y
with pairwise distinct lengths modulo 5. So the lengths of P1, P2, P3 modulo 5 are not pairwise distinct.
Hence, by symmetry, there exists t ∈ {0, 1, 2, 3, 4} such that |E(P1)| and |E(P2)| equal t modulo 5.
Suppose that |E(P3)| = t modulo 5. By symmetry, we may assume that |E(P3)| ≤ |E(Pi)| for every
i ∈ {1, 2}. So min{|E(P1)|, |E(P2)|} ≥ 2. Note that the paths R1,1 ∪R2,2, L1,1 ∪P3 ∪R2,2, R1,1 ∪P3 ∪L2,2
are three paths from v1,1 to v2,2 with lengths 2t − 3, 2t − 1, 2t + 1 modulo 5, respectively, a contradiction.
Hence there exists s ∈ {0, 1, 2, 3, 4} − {t} such that |E(P3)| = s modulo 5. By symmetry, we may
assume that |E(P1)| > 1. For every r ∈ {1, 2}, the paths R1,r, L1,r ∪ P2, L1,r ∪ P3 are three paths from
v1,r to v1,|E(P1)| of lengths t − r, t + r, s + r modulo 5, respectively, so t − r = s + r modulo 5. That is,
t − 1 = s + 1 modulo 5 and t − 2 = s + 2 modulo 5, a contradiction. This proves the lemma.

Lemma 5.13. Let a and d be integers such that d ∈ {1, 2}. Let B be a subset of {0, 1, 2, 3, 4} of size
three. Then the set {a + id + b : 0 ≤ i ≤ 2, b ∈ B} contains a multiple of 5.

Proof. Let X = {a + id + b : 0 ≤ i ≤ 2, b ∈ B}. If there exists an integer s such that the three
elements of B are either s, s + 1, s + 2 modulo 5 or s, s + 2, s + 4 modulo 5, then X contains a multiple
of 5. So by shifting, we may without loss of generality assume that B = {0, 1, 3}. If d = 1, then X ⊇
{a, a+1, a+2, a+3, a+4}, so X contains a multiple of 5. If d = 2, then X ⊇ {a, a+1, a+2, a+3, a+4},
so X contains a multiple of 5. This proves the lemma.

Lemma 5.14. If G is a 5-connected graph of girth at least ﬁve, then G contains a cycle of length 0
modulo 5.

Proof. Suppose to the contrary that G does not contain a cycle of length 0 modulo 5. In particular, G
does not contain a 5-cycle and a 10-cycle, and G does not contain ﬁve admissible cycles. So the girth
of G is at least six, and G does not contain a cycle of length ten.
Let H be a subgraph of G isomorphic to a theta graph with |V (H)| minimum. By Lemma 5.10, H
satisﬁes the following.

• H is an induced subgraph of G.

• There exists at most one vertex of G − V (H) adjacent in G to at least two vertices in V (H).

• If there exists a vertex v of G − V (H) adjacent in G to at least two vertices in V (H), then
G[V (H) ∪ {v}] is isomorphic to a 1-subdivision of K4.

If there exists a vertex of G − V (H) adjacent in G to at least two vertices of V (H), then there exists
an induced subgraph H ′ isomorphic to an induced 1-subdivision of K4, so by Lemma 5.11, G contains
ﬁve admissible cycles, a contradiction.
So every vertex of G − V (H) is adjacent in G to at most one vertex in V (H). Let G′ = G − V (H).
Let d = 5.
Suppose that there exists a component M of G′ such that M is not 2-connected. Let B1, B2 be
distinct end-blocks of M . Since G is 3-connected and every vertex in V (M ) is adjacent in G to at most
one vertex in V (H), B1 and B2 are 2-connected. For each i ∈ {1, 2}, let bi be the cut-vertex of M

24

contained in V (Bi). Since G is 3-connected, for each i ∈ {1, 2}, there exists xi ∈ V (Bi)−{bi} such that xi
is adjacent in G to some vertex yi in V (H). For each i ∈ {1, 2}, since (Bi, xi, bi) is a 2-connected rooted
graph of minimum degree at least d− 1, there exist d− 2 admissible paths Pi,1, ..., Pi,d−2 in Bi from xi to
bi by Theorem 3.1. Let Q be a path in M from b1 to b2 internally disjoint from V (B1)∪V (B2). Let Q′ be
a path in H from y1 to y2. Then the set {(P1,i ∪Q∪P2,j ∪Q′)+x1y1 +x2y2 : 1 ≤ i ≤ d−2, 1 ≤ j ≤ d−2}
contains 2(d − 2) − 1 ≥ d = 5 admissible paths, a contradiction.
So every component of G′ is 2-connected. Suppose that G′ is not connected. Let M1, M2 be two
distinct components of G′. For each i ∈ {1, 2}, since G is 4-connected, there exist distinct vertices xi,1
and xi,2 in V (Mi) such that xi,1 is adjacent in G to a vertex yi,1 in V (H) and xi,2 is adjacent in G to a
vertex yi,2 in V (H). For each i ∈ {1, 2}, since (Mi, xi,1, xi,2) is a 2-connected rooted graph of minimum
degree at least d− 1, there exist d− 2 admissible paths Ri,1, ..., Ri,d−2 in Mi from xi,1 to xi,2 by Theorem
3.1. Since H is 2-connected, there exist two disjoint paths Q1, Q2 in H from {y1,1, y1,2} to {y2,1, y2,2}.
Then the set {(R1,i ∪ Q1 ∪ R2,j ∪ Q2)+ x1,1y1,1 + x1,2y1,2 + x2,1y2,1 + x2,2y2,2 : 1 ≤ i ≤ d− 2, 1 ≤ j ≤ d− 2}
contains 2(d − 2) − 1 ≥ 5 admissible cycles, a contradiction.
So G′ is 2-connected. By Lemma 5.12, there exist two distinct vertices x, y in H such that there
exist three paths A1, A2, A3 in H from x to y with pairwise distinct lengths modulo 5. Since G
is 5-connected and H is an induced subgraph, there exist distinct vertices x′, y′ in V (G′) such that
{xx′, yy′} ⊆ E(G). Since (G′, x′, y′) is a 2-connected rooted graph of minimum degree at least d− 1 = 4,
by Theorem 3.1, there exist three admissible paths Z1, Z2, Z3 in G′ from x′ to y′. By Lemma 5.13, the
set {(Zi ∪ Aj) + xx′ + yy′ : 1 ≤ i ≤ 3, 1 ≤ j ≤ 3} contains a cycle of length 0 modulo 5, a contradiction.
This proves the lemma.

Now we are ready to prove Theorem 1.9. The following is a restatement of Theorem 1.9.

Theorem 5.15. For d ≥ 3, every d-connected graph contains a cycle of length zero modulo d.

Proof. By [3, Theorem 1] and [6, Theorem 1.2], the theorem is true for d ∈ {3, 4}. So we may assume
that d ≥ 5. Suppose to the contrary that G does not contain a cycle of length 0 modulo d. So G does
not contain a K ′
d subgraph and does not contain a K −
d,d subgraph. In addition, G does not contain
d cycles of consecutive length, and when d is odd or G is bipartite, G does not contain d admissible
cycles.
Since G is (d−1)-connected and does not contain a K ′
d subgraph, G does not contain a K −
4 subgraph
by Lemma 5.1. Since G does not contain a K −
4 subgraph, by Lemma 5.2, G does not contain a K3
subgraph. Since G does not contain a K3 subgraph, by Lemma 5.5, either d = 5 or G is bipartite. Since
G does not contain a K3 subgraph and a K −
d,d subgraph, by Lemma 5.6, either G does not contain a
4-cycle, or G contains a cycle of length four and a cycle of length ﬁve, or d is even.
Suppose that G does not contain a 4-cycle. Then G is not bipartite by Lemma 5.8. So d = 5. Since
G does not contain a K3 subgraph and a 4-cycle, G is of girth at least ﬁve. So G contains a cycle of
length 0 modulo 5 = d by Lemma 5.14, a contradiction.
So either G contains a 4-cycle and a 5-cycle, or d is even. Note that either case implies d ̸= 5. So
G is bipartite, contradicting that G contains a 5-cycle. This proves the theorem.

When d ≥ 6, we can strengthen the conclusion of Theorem 5.15.

Theorem 5.16. For integers d ≥ 6 and t satisfying 2t ̸= 2 modulo d, every d-connected graph contains
a cycle of length 2t modulo d.

Proof. Suppose to the contrary that there exist integers d ≥ 6 and t with 2t ̸= 2 modulo d such that
there exists a d-connected graph G that does not contain a cycle of length 2t modulo d. In particular,

25

G does not contain a K ′
d+1 subgraph and does not contain a K −
d,d subgraph. In addition, G does not
contain d cycles of consecutive length, and when d is odd or G is bipartite, G does not contain d
admissible cycles.
By Lemma 5.1, G does not contain a K −
4 subgraph. By Lemma 5.2, G does not contain a K3
subgraph. By Lemma 5.5, G is bipartite. Since G is bipartite, by Lemma 5.6, G does not contain a
4-cycle. By Lemma 5.8, G contains d admissible cycles. But G is bipartite, a contradiction.

References

[1] B. Bollob´as, Cycles modulo k, Bull. London Math. Soc. 9 (1977), 97–98.

[2] J. A. Bondy and A. Vince, Cycles in a graph whose lengths diﬀer by one or two, J. Graph Theory
27 (1998), 11–15.

[3] G. Chen and A. Saito, Graphs with a cycle of length divisible by three, J. Combin. Theory Ser.
B 60 (1994), 277–292.

[4] S. Chiba and T. Yamashita, Minimum degree conditions for the existence of cycles of all lengths
modulo k in graphs, arXiv:1904.03818 [math.CO] 8 April 2019.

[5] N. Dean, Which graphs are pancyclic modulo k?, Sixth Internat. Conf. on the Theory of Applica-
tions of Graphs, Kalamazoo, Michigan (1988) 315–326.

[6] N. Dean, L. Lesniak and A. Saito, Cycles of length 0 modulo 4 in graphs, Discrete Math. 121
(1993), 37–49.

[7] A. Diwan, Cycles of even lengths modulo k, J. Graph Theory 65 (2010), 246–252.

[8] P. Erd˝os, Some recent problems and results in graph theory, combinatorics, and number theory,
Proc. Seventh S-E Conf. Combinatorics, Graph Theory and Computing, Utilitas Math., Winnipeg,
1976, pp. 3–14.

[9] P. Erd˝os, Some of my favourite problems in various branches of combinatorics, Matematiche
(Catania) 47 (1992), 231–240.

[10] G. Fan, Distribution of cycle lengths in graphs, J. Combin. Theory Ser. B 84 (2002), 187–202.

[11] A. Gy´arf´as, Graphs with k odd cycle lengths, Discrete Math. 103 (1992), 41–48.

[12] R. H¨aggkvist and A. Scott, Arithmetic progressions of cycles, Technical Report No. 16 (1998),
Matematiska Institutionen, Ume˚aUniversitet.

[13] A. Kostochka, B. Sudakov and J. Verstra¨ete, Cycles in triangle-free graphs of large chromatic
number, Combinatorica 37 (2017), 481–494.

[14] U. Krusenstjerna-Hafstrøm and B.Toft, Special subdivisions of K4 and 4-chromatic graphs,
Monatsh. Math. 89 (1980), 101–110.

[15] C. Liu and J. Ma, Cycle lengths and minimum degree of graphs, J. Combin. Theory Ser. B 128
(2018), 66–95.

[16] Lyngsie and Merker, Cycle lengths modulo k in large 3-connected cubic graphs, arXiv:1904.05076
[math.CO] 10 April 2019.
 26

[17] J. Ma, Cycles with consecutive odd lengths, European J. Combin. 52 (2016), 74–78.

[18] P. Mih´ok and I. Schiermeyer, Cycle lengths and chromatic number of graphs, Discrete Math. 286
(2004), 147–149.

[19] B. Sudakov and J. Verstra¨ete, Cycle lengths in sparse graphs, Combinatorica 28 (2008), 357–372.

[20] B. Sudakov and J. Verstra¨ete, The extremal function for cycles of length l mod k, Electron. J.
Combin. 24(1) (2017), #P1.7

[21] C. Thomassen, Graph decomposition with applications to subdivisions and path systems modulo
k, J. Graph Theory 7 (1983), 261–271.

[22] C. Thomassen, Paths, circuits and subdivisions, Selected Topics in Graph Theory (L. Beineke and
R. Wilson, eds.), vol. 3, Academic Press, 1988, pp. 97–131.

[23] C. Thomassen and B. Toft, Non-separating induced cycles in graphs, J. Combin. Theory Ser. B
31 (1981), 199–224.

[24] W. T. Tutte, How to draw a graph, Proc. London Math. Soc. 13 (1963), 743–768.

[25] J. Verstra¨ete, On arithmetic progressions of cycle lengths in graphs, Combin. Probab. Comput. 9
(2000), 369–373.

[26] J. Verstra¨ete, Extremal problems for cycles in graphs, In Recent Trends in Combinatorics, A. Bev-
eridge et al. (eds.), The IMA Volumes in Mathematics and its Applications 159, 83–116, Springer,
New York, 2016.
 27
