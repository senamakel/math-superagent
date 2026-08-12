<!-- source: https://arxiv.org/html/2109.01277v1 | converted from HTML -->

Erdős-Gyárfás Conjecture for P 8 -free graphs

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2109.01277v1 [math.CO] 03 Sep 2021

# Erdős-Gyárfás Conjecture for P 8 P_{8} -free graphs

Yuping Gao Songling Shan a. School of Mathematics and Statistics, Lanzhou University, Lanzhou 730000, Chinab. Department of Mathematics, Illinois State University, Normal, IL 61790, USA

###### Abstract

A graph is P 8 P_{8} -free if it contains no induced subgraph isomorphic to the path P 8 P_{8} on eight vertices. In 1995, Erdős and Gyárfás conjectured that every graph of minimum degree at least three contains a cycle whose length is a power of two. In this paper, we confirm the conjecture for P 8 P_{8} -free graphs by showing that there exists a cycle of length four or eight in every P 8 P_{8} -free graph with minimum degree at least three.

Keywords: Erdős-Gyárfás Conjecture; P 8 P_{8} -free graph; Cycle

## 1 Introduction

All graphs considered in this paper are undirected and simple. Let G G be a graph. The vertex set, the edge set, the maximum degree and the minimum degree of G G are denoted by V ⁡ ( G) V(G), E ⁡ ( G) E(G), Δ ⁡ ( G) \Delta(G) and δ ⁡ ( G) \delta(G), respectively. For a vertex v ∈ V ⁡ ( G) v\in V(G), the set of neighbors of v v in G G is denoted by N G ​ ( v) N_{G}(v) or N ⁡ ( v) N(v) if G G is understood. Let S ⊆ V ⁡ ( G) S\subseteq V(G), we use G ⁡ [S] G[S] to denote the subgraph of G G induced by S S and G − S G-S to denote the subgraph G ⁡ [V ⁡ ( G) ∖ S] G[V(G)\setminus S]. We write u ∼ v u\thicksim v if u ​ v ∈ E ⁡ ( G) uv\in E(G) and u ≁ v u\nsim v otherwise. The connectivity of G G is denoted by κ ⁡ ( G) \kappa(G). A u ​ v uv -*path*is a path having ends as u u and v v. Let P P be a path and x, y ∈ V ⁡ ( P) x,y\in V(P), we use x ​ P ​ y xPy to denote the subpath of P P with ends x x and y y.

A path on k k vertices is denoted by P k P_{k}. A cycle on k k vertices is denoted by C k C_{k} and is called a k k -*cycle*. The length of a path or cycle is the number of edges it contains. The well-known Erdős-Gyárfás Conjecture [2] states that every graph of minimum degree at least three contains a 2 m 2^{m} -cycle for some integer m ≥ 2 m\geq 2. The conjecture is confirmed for some graph classes including K 1, m K_{1,m} -free graphs of minimum degree at least m + 1 m+1 or maximum degree at least 2 ​ m − 1 2m-1 [7], 3-connected cubic planar graphs [5], planar claw-free graphs [1] and some Cayley graphs [3, 4]. In [6], it is proved that every cubic claw-free graph contains a cycle whose length is 2 k 2^{k}, or 3 ⋅ 2 k 3\cdot 2^{k}, for some positive integer k k.

Given a graph H H, a graph G G is H H -*free*if G G does not contain any induced subgraph isomorphic to H H. In this paper, we confirm Erdős-Gyárfás Conjecture for P 8 P_{8} -free graphs by showing the following two theorems.

###### Theorem 1.1.

Every P 5 P_{5} -free graph with minimum degree at least three contains a 4 4 -cycle.

###### Theorem 1.2.

Every P 8 P_{8} -free graph with minimum degree at least three contains a 4 4 -cycle or 8 8 -cycle.

In confirming the Erdős-Gyárfás Conjecture for P 8 P_{8} -free graphs, Theorem 1.2 alone suffices. But we include Theorem 1.1 as it is stronger than the restriction of Theorem 1.2 on P 5 P_{5} -free graphs and also its proof technique may be of independent interests.

The remainder of the paper is organized as follows. In Section 2, we prove Theorem 1.1. In Section 3, we prove Theorem 1.2.

## 2 Proof of Theorem 1.1

###### Proof of Theorem 1.1.

Let G G be a P 5 P_{5} -free graph with δ ⁡ ( G) ≥ 3 \delta(G)\geq 3. We may assume that G G is connected. Otherwise, we consider a component of G G instead. Furthermore, assume that G G is not complete and G G contains no C 4 C_{4} since otherwise we are done. Let S S be a minimum cut-set of G G. For x ∈ S x\in S, a component D D of G − S G-S is a *complete neighborhood component*(*CNC*) of x x if x x is adjacent in G G to every vertex of D D, and D D is a *non-CNC*of x x otherwise. We need the following claim.

###### Claim 2.1.

(i) For any vertex x ∈ S x\in S and any component D D of G − S G-S, N G ​ ( x) ∩ V ⁡ ( D) ≠ ∅ N_{G}(x)\cap V(D)\neq\emptyset.

(ii) For any vertex x ∈ S x\in S, x x has at least c ⁡ ( G − S) − 1 c(G-S)-1 CNCs. Equivalently, x x has at most one non-CNC.

(iii) For any CNC D D of a vertex x ∈ S x\in S, | V ⁡ ( D) | ≤ 2 |V(D)|\leq 2.

(iv) | S | ≥ 2 |S|\geq 2, i.e., κ ⁡ ( G) ≥ 2 \kappa(G)\geq 2.

Moreover, let x, y ∈ S x,y\in S be distinct. Then the following statements hold.

(v) If x x and y y have a common CNC D D, then | V ⁡ ( D) | = 1 |V(D)|=1.

(vi) x x and y y have at most one common CNC.

(vii) c ⁡ ( G − S) ≤ 3 c(G-S)\leq 3. Furthermore, if c ⁡ ( G − S) = 3 c(G-S)=3, then x x and y y have exactly one common CNC.

(viii) There exist two vertices from S S that are nonadjacent in G G.

###### Proof.

For Statement (i), as S S is a minimum cut-set of G G, for any x ∈ S x\in S and any component D D of G − S G-S, it follows that N G ​ ( x) ∩ V ⁡ ( D) ≠ ∅ N_{G}(x)\cap V(D)\neq\emptyset.

For Statement (ii), suppose instead that x x has two non-CNCs D 1 D_{1} and D 2 D_{2}. Let u i ∈ V ⁡ ( D i) u_{i}\in V(D_{i}) such that x ≁ u i x\nsim u_{i}, and P i P_{i} be a shortest path of D i D_{i} from u i u_{i} to a neighbor, say x i x_{i} of x x in G G from V ⁡ ( D i) V(D_{i}), i = 1, 2 i=1,2. By the choice, P i P_{i} is an induced path of D i D_{i} such that the only vertex of P i P_{i} that is adjacent in G G to x x is x i x_{i}, i = 1, 2 i=1,2. Then u 1 ​ P 1 ​ x 1 ​ x ​ x 2 ​ P 2 ​ u 2 u_{1}P_{1}x_{1}xx_{2}P_{2}u_{2} contains an induced P 5 P_{5}, contradicting G G being P 5 P_{5} -free.

For Statement (iii), suppose instead that | V ⁡ ( D) | ≥ 3 |V(D)|\geq 3. If D D is a complete graph, then G ⁡ [V ⁡ ( D) ∪ { x }] G[V(D)\cup\{x\}] contains a C 4 C_{4} and we are done. So assume that D D is not a complete graph. Then D D contains an induced P 3 P_{3}. Since x x is adjacent to every vertex in D D, especially adjacent to every vertex in the P 3 P_{3}. It follows that G G contains a C 4 C_{4}.

For Statement (iv), by (ii), each vertex x ∈ S x\in S has a CNC D D. By (iii), | V ⁡ ( D) | ≤ 2 |V(D)|\leq 2. Let u ∈ V ⁡ ( D) u\in V(D). Then u u has a neighbor y ∈ S ∖ { x } y\in S\setminus\{x\} by δ ⁡ ( G) ≥ 3 \delta(G)\geq 3. So | S | ≥ 2 |S|\geq 2.

Statements (v) and (vi) follow by the assumption that G G contains no C 4 C_{4}.

For Statement (vii), by (ii), each of x x and y y has at most one non-CNC. Then x x and y y have at least c ⁡ ( G − S) − 2 c(G-S)-2 common CNCs. This is a contradiction to statement (vi) if c ⁡ ( G − S) ≥ 4 c(G-S)\geq 4. Furthermore, if c ⁡ ( G − S) = 3 c(G-S)=3, then x x and y y have exactly one common CNC.

For Statement (viii), by (ii) and (iii), x x has a CNC D D with | V ⁡ ( D) | ≤ 2 |V(D)|\leq 2. Let u ∈ V ⁡ ( D) u\in V(D). If u u has at least three neighbors from S S, then there exist two nonadjacent vertices in N ⁡ ( u) ∩ S N(u)\cap S since G G contains no C 4 C_{4}. So u u has at most two neighbors in S S. This, together with δ ⁡ ( G) ≥ 3 \delta(G)\geq 3, implies | V ⁡ ( D) | = 2 |V(D)|=2. Let v v be the neighbor of u u in D D. Since | V ⁡ ( D) | ≤ 2 |V(D)|\leq 2 and δ ⁡ ( G) ≥ 3 \delta(G)\geq 3, u u has a neighbor y ∈ S ∖ { x } y\in S\setminus\{x\}. Furthermore, y ≁ x y\nsim x, for otherwise y ​ u ​ v ​ x ​ y yuvxy is a C 4 C_{4} of G G. ∎

By Claim 2.1 (viii), we let x, y ∈ S x,y\in S such that x ≁ y x\nsim y in G G.

###### Claim 2.2.

c ⁡ ( G − S) = 2 c(G-S)=2.

###### Proof.

By Claim 2.1 (vii), c ⁡ ( G − S) ≤ 3 c(G-S)\leq 3. Suppose that c ⁡ ( G − S) = 3 c(G-S)=3. By Claim 2.1 (vii), x x and y y have exactly one common CNC D 1 D_{1}. By Claim 2.1 (ii), let D 2 D_{2} be a CNC of x x, D 3 D_{3} be a CNC of y y. Note that D 2 ≠ D 3 D_{2}\neq D_{3}. Let u i ∈ V ( D i), i = 1, 2, 3 u_{i}\in V(D_{i}),i=1,2,3. Then u 3 ≁ x, u 2 ≁ y u_{3}\nsim x,u_{2}\nsim y since G G contains no C 4 C_{4}. It follows that u 3 ​ y ​ u 1 ​ x ​ u 2 u_{3}yu_{1}xu_{2} is an induced P 5 P_{5} in G G, a contradiction. ∎

By Claim 2.2, c ⁡ ( G − S) = 2 c(G-S)=2. Let D 1, D 2 D_{1},D_{2} be the two components of G − S G-S. Assume first that x x and y y have no common CNC. By Claim 2.1 (ii), assume by symmetry that D 1 D_{1} is a CNC of x x and D 2 D_{2} is a CNC of y y. By Claim 2.1 (i), there exist y 1 ∈ N ⁡ ( y) ∩ V ⁡ ( D 1) y_{1}\in N(y)\cap V(D_{1}) and x 1 ∈ N ⁡ ( x) ∩ V ⁡ ( D 2) x_{1}\in N(x)\cap V(D_{2}). Then x ​ y 1 ​ y ​ x 1 ​ x xy_{1}yx_{1}x is a C 4 C_{4}, giving a contradiction.

Now assume that x x and y y have a common CNC D 1 D_{1} and let u ∈ V ⁡ ( D 1) u\in V(D_{1}). Then | V ⁡ ( D 1) | = 1 |V(D_{1})|=1 by Claim 2.1 (v). By Claim 2.1 (i), there exist x 1 ∈ N ⁡ ( x) ∩ V ⁡ ( D 2) x_{1}\in N(x)\cap V(D_{2}) and y 1 ∈ N ⁡ ( y) ∩ V ⁡ ( D 2) y_{1}\in N(y)\cap V(D_{2}). Note that x 1 ≠ y 1 x_{1}\neq y_{1}. If x 1 ≁ y 1 x_{1}\nsim y_{1}, then x 1 ​ x ​ u ​ y ​ y 1 x_{1}xuyy_{1} is an induced P 5 P_{5} in G G. So x 1 ∼ y 1 x_{1}\thicksim y_{1}. Since δ ⁡ ( G) ≥ 3 \delta(G)\geq 3, u u has a neighbor z ∈ S ∖ { x, y } z\in S\setminus\{x,y\}. Because G G has no C 4 C_{4}, we have z ≁ x 1, y 1 z\nsim x_{1},y_{1}. Now it must be the case that z ∼ x z\thicksim x, as otherwise z ​ u ​ x ​ x 1 ​ y 1 zuxx_{1}y_{1} is an induced P 5 P_{5} in G G. Similarly, z ∼ y z\sim y. However, it follows that z z is a common neighbor of x x and y y other than u u, showing a contradiction. We complete the proof of Theorem 1.1. ∎

## 3 Proof of Theorem 1.2

The Lemma below was shown in [6].

###### Lemma 3.1.

Let G G be a graph with δ ⁡ ( G) ≥ 3 \delta(G)\geq 3. If G G does not contain C 4 C_{4}, then G G has an induced cycle C k C_{k} for some k ≥ 5 k\geq 5.

###### Proof of Theorem 1.2.

Let G G be a P 8 P_{8} -free graph with δ ⁡ ( G) ≥ 3 \delta(G)\geq 3. We may assume that G G is connected. Otherwise, we just consider a component of G G. Furthermore, assume that G G contains neither C 4 C_{4} nor C 8 C_{8} since otherwise we are done. By Lemma 3.1, G G contains an induced C k C_{k} for some k ≥ 5 k\geq 5. Let C = v 1 ​ v 2 ​ … ​ v k ​ v 1 C=v_{1}v_{2}\ldots v_{k}v_{1} be a shortest induced cycle in G G of length at least 5. Then 5 ≤ k ≤ 7 5\leq k\leq 7 since G G is P 8 P_{8} -free and G G contains neither C 4 C_{4} nor C 8 C_{8}.

###### Claim 3.2.

If k = 5 k=5, then no two consecutive vertices on C C share a common neighbor in G G.

###### Proof.

Suppose the claim does not hold. We assume, without loss of generality, that v 1 v_{1} and v 2 v_{2} have a common neighbor v 6 ∉ { v 1, v 2, …, v 5 } v_{6}\not\in\{v_{1},v_{2},\ldots,v_{5}\}. Then v 6 ≁ v i v_{6}\nsim v_{i} for i ∈ { 3, 4, 5 } i\in\{3,4,5\} as G G contains no C 4 C_{4}. We conclude that v 6 v_{6} has a neighbor v 7 ∉ { v 1, v 2, …, v 6 } v_{7}\not\in\{v_{1},v_{2},\ldots,v_{6}\} since δ ⁡ ( G) ≥ 3 \delta(G)\geq 3. The minimum degree condition is repeatedly used in the following proof and we omit the reason in the following when we say that v i v_{i} has a neighbor v j v_{j} for i ≠ j i\neq j. It can be seen that v 7 ≁ v i v_{7}\nsim v_{i} for i ∈ { 1, 2, 3, 5 } i\in\{1,2,3,5\} as G G contains no C 4 C_{4}.

Case 1 v 7 ∼ v 4 v_{7}\thicksim v_{4}.

In this case, v 7 v_{7} has a neighbor v 8 ∉ { v 1, v 2, …, v 7 } v_{8}\not\in\{v_{1},v_{2},\ldots,v_{7}\}. And v 8 ≁ v i v_{8}\nsim v_{i} for i ∈ { 1, 2, 3, 5 } i\in\{1,2,3,5\} since G G contains no C 4 C_{4} or C 8 C_{8}.

Subcase 1.1 v 8 ∼ v 6 v_{8}\thicksim v_{6}.

In this case, v 8 ≁ v 4 v_{8}\nsim v_{4} otherwise v 8 ​ v 4 ​ v 7 ​ v 6 ​ v 8 v_{8}v_{4}v_{7}v_{6}v_{8} is a C 4 C_{4}. It follows that v 8 v_{8} has a neighbor v 9 ∉ { v 1, v 2, …, v 8 } v_{9}\not\in\{v_{1},v_{2},\ldots,v_{8}\}. And v 9 ≁ v 1 v_{9}\nsim v_{1} otherwise v 9 ​ v 1 ​ v 6 ​ v 8 ​ v 9 v_{9}v_{1}v_{6}v_{8}v_{9} is a C 4 C_{4}, v 9 ≁ v 2 v_{9}\nsim v_{2} otherwise v 9 ​ v 2 ​ v 6 ​ v 8 ​ v 9 v_{9}v_{2}v_{6}v_{8}v_{9} is a C 4 C_{4}, v 9 ≁ v 3 v_{9}\nsim v_{3} otherwise v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 5 ​ v 1 ​ v 2 ​ v 3 ​ v 9 v_{9}v_{8}v_{7}v_{4}v_{5}v_{1}v_{2}v_{3}v_{9} is a C 8 C_{8}, v 9 ≁ v 4 v_{9}\nsim v_{4} otherwise v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 9 v_{9}v_{8}v_{7}v_{4}v_{9} is a C 4 C_{4}, v 9 ≁ v 5 v_{9}\nsim v_{5} otherwise v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 2 ​ v 3 ​ v 4 ​ v 5 ​ v 9 v_{9}v_{8}v_{7}v_{6}v_{2}v_{3}v_{4}v_{5}v_{9} is a C 8 C_{8}, v 9 ≁ v 6 v_{9}\nsim v_{6} otherwise v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 9 v_{9}v_{8}v_{7}v_{6}v_{9} is a C 4 C_{4}, v 9 ≁ v 7 v_{9}\nsim v_{7} otherwise v 9 ​ v 8 ​ v 6 ​ v 7 ​ v 9 v_{9}v_{8}v_{6}v_{7}v_{9} is a C 4 C_{4}. So v 9 v_{9} has two neighbors v 10, v 11 ∉ { v 1, v 2, ⋯, v 9 } v_{10},v_{11}\not\in\{v_{1},v_{2},\cdots,v_{9}\}. At least one of v 10 v_{10} and v 11 v_{11}, say v 10 v_{10}, is not adjacent to v 8 v_{8}. Note that v 10 ≁ v 7 v_{10}\nsim v_{7} otherwise v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 10 v_{10}v_{9}v_{8}v_{7}v_{10} is a C 4 C_{4}, v 10 ≁ v 4 v_{10}\nsim v_{4} otherwise v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 2 ​ v 3 ​ v 4 ​ v 10 v_{10}v_{9}v_{8}v_{7}v_{6}v_{2}v_{3}v_{4}v_{10} is a C 8 C_{8}, v 10 ≁ v 5 v_{10}\nsim v_{5} otherwise v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 2 ​ v 1 ​ v 5 ​ v 10 v_{10}v_{9}v_{8}v_{7}v_{6}v_{2}v_{1}v_{5}v_{10} is a C 8 C_{8}, v 10 ≁ v 1 v_{10}\nsim v_{1} otherwise v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 3 ​ v 2 ​ v 1 ​ v 10 v_{10}v_{9}v_{8}v_{7}v_{4}v_{3}v_{2}v_{1}v_{10} is a C 8 C_{8}. Similarly, v 10 ≁ v 2 v_{10}\not\sim v_{2}. So v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 5 ​ v 1 ​ v 2 v_{10}v_{9}v_{8}v_{7}v_{4}v_{5}v_{1}v_{2} is an induced P 8 P_{8} in G G, a contradiction. (See Figure 1(a) for an illustration.)

v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} v 8 v_{8} v 9 v_{9} v 10 v_{10} v 11 v_{11} (a) Subcase 1.1 v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} v 8 v_{8} v 9 v_{9} v 10 v_{10} v 11 v_{11} v 12 v_{12} (b) Subcase 1.2

(c) Subcase 1.2 v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} v 8 v_{8} v 9 v_{9} v 10 v_{10} v 11 v_{11} v 12 v_{12} v 13 v_{13} v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} v 8 v_{8} v 9 v_{9} v 10 v_{10} v 11 v_{11} (d) Case 2 Figure 1: Illustration for Claim 3.2

Subcase 1.2 v 8 ≁ v 6 v_{8}\nsim v_{6}.

If v 8 ≁ v 4 v_{8}\nsim v_{4}, then v 8 v_{8} has two neighbors v 9, v 10 ∉ { v 1, v 2, …, v 8 } v_{9},v_{10}\not\in\{v_{1},v_{2},\ldots,v_{8}\}. At least one of v 9 v_{9} and v 10 v_{10}, say v 9 v_{9}, is not adjacent to v 7 v_{7}. Moreover, v 9 ≁ v 1 v_{9}\nsim v_{1} otherwise v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 3 ​ v 2 ​ v 6 ​ v 1 ​ v 9 v_{9}v_{8}v_{7}v_{4}v_{3}v_{2}v_{6}v_{1}v_{9} is a C 8 C_{8}, v 9 ≁ v 2 v_{9}\nsim v_{2} otherwise v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 5 ​ v 1 ​ v 6 ​ v 2 ​ v 9 v_{9}v_{8}v_{7}v_{4}v_{5}v_{1}v_{6}v_{2}v_{9} is a C 8 C_{8}, v 9 ≁ v 3 v_{9}\nsim v_{3} otherwise v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 5 ​ v 1 ​ v 2 ​ v 3 ​ v 9 v_{9}v_{8}v_{7}v_{4}v_{5}v_{1}v_{2}v_{3}v_{9} is a C 8 C_{8}, v 9 ≁ v 4 v_{9}\nsim v_{4} otherwise v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 9 v_{9}v_{8}v_{7}v_{4}v_{9} is a C 4 C_{4}, v 9 ≁ v 5 v_{9}\nsim v_{5} otherwise v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 2 ​ v 3 ​ v 4 ​ v 5 ​ v 9 v_{9}v_{8}v_{7}v_{6}v_{2}v_{3}v_{4}v_{5}v_{9} is a C 8 C_{8}, v 9 ≁ v 6 v_{9}\nsim v_{6} otherwise v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 9 v_{9}v_{8}v_{7}v_{6}v_{9} is a C 4 C_{4}. So v 9 v_{9} has two neighbors v 11, v 12 ∉ { v 1, v 2, …, v 9 } v_{11},v_{12}\not\in\{v_{1},v_{2},\ldots,v_{9}\}. At least one of v 11 v_{11} and v 12 v_{12}, say v 11 v_{11}, is not adjacent to v 8 v_{8}. Moreover, v 11 ≁ v 7 v_{11}\nsim v_{7} otherwise v 11 ​ v 9 ​ v 8 ​ v 7 ​ v 11 v_{11}v_{9}v_{8}v_{7}v_{11} is a C 4 C_{4}, v 11 ≁ v 4 v_{11}\nsim v_{4} otherwise v 11 ​ v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 2 ​ v 3 ​ v 4 ​ v 11 v_{11}v_{9}v_{8}v_{7}v_{6}v_{2}v_{3}v_{4}v_{11} is a C 8 C_{8}, v 11 ≁ v 5 v_{11}\nsim v_{5} otherwise v 11 ​ v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 2 ​ v 1 ​ v 5 ​ v 11 v_{11}v_{9}v_{8}v_{7}v_{6}v_{2}v_{1}v_{5}v_{11} is a C 8 C_{8}, v 11 ≁ v 1 v_{11}\nsim v_{1} otherwise v 11 ​ v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 3 ​ v 2 ​ v 1 ​ v 11 v_{11}v_{9}v_{8}v_{7}v_{4}v_{3}v_{2}v_{1}v_{11} is a C 8 C_{8}, v 11 ≁ v 2 v_{11}\nsim v_{2} otherwise v 11 ​ v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 5 ​ v 1 ​ v 2 ​ v 11 v_{11}v_{9}v_{8}v_{7}v_{4}v_{5}v_{1}v_{2}v_{11} is a C 8 C_{8}. It follows that v 11 ​ v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 5 ​ v 1 ​ v 2 v_{11}v_{9}v_{8}v_{7}v_{4}v_{5}v_{1}v_{2} is an induced P 8 P_{8} in G G, a contradiction. (See Figure 1(b) for an illustration.)

Now assume that v 8 ∼ v 4 v_{8}\thicksim v_{4}. Then v 8 v_{8} has a neighbor v 9 ∉ { v 1, v 2, …, v 8 } v_{9}\not\in\{v_{1},v_{2},\ldots,v_{8}\}. Furthermore, v 9 ≁ v i v_{9}\nsim v_{i} for i ∈ { 1, 2, …, 6 } i\in\{1,2,\ldots,6\} same as the case when v 8 ≁ v 4 v_{8}\nsim v_{4}. And v 9 ≁ v 7 v_{9}\nsim v_{7} otherwise v 9 ​ v 8 ​ v 4 ​ v 7 ​ v 9 v_{9}v_{8}v_{4}v_{7}v_{9} is a C 4 C_{4}. It follows that v 9 v_{9} has two neighbors v 10, v 11 ∉ { v 1, v 2, …, v 9 } v_{10},v_{11}\not\in\{v_{1},v_{2},\ldots,v_{9}\}. At least one of v 10 v_{10} and v 11 v_{11}, say v 10 v_{10}, is not adjacent to v 8 v_{8}. Moreover, v 10 ≁ v 1 v_{10}\nsim v_{1} otherwise v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 3 ​ v 2 ​ v 1 ​ v 10 v_{10}v_{9}v_{8}v_{7}v_{4}v_{3}v_{2}v_{1}v_{10} is a C 8 C_{8}, v 10 ≁ v 2 v_{10}\nsim v_{2} otherwise v 10 ​ v 9 ​ v 8 ​ v 4 ​ v 7 ​ v 6 ​ v 1 ​ v 2 ​ v 10 v_{10}v_{9}v_{8}v_{4}v_{7}v_{6}v_{1}v_{2}v_{10} is a C 8 C_{8}, v 10 ≁ v 3 v_{10}\nsim v_{3} otherwise v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 1 ​ v 2 ​ v 3 ​ v 10 v_{10}v_{9}v_{8}v_{7}v_{6}v_{1}v_{2}v_{3}v_{10} is a C 8 C_{8}, v 10 ≁ v 4 v_{10}\nsim v_{4} otherwise v 10 ​ v 9 ​ v 8 ​ v 4 ​ v 10 v_{10}v_{9}v_{8}v_{4}v_{10} is a C 4 C_{4}, v 10 ≁ v 5 v_{10}\nsim v_{5} otherwise v 10 ​ v 9 ​ v 8 ​ v 4 ​ v 3 ​ v 2 ​ v 1 ​ v 5 ​ v 10 v_{10}v_{9}v_{8}v_{4}v_{3}v_{2}v_{1}v_{5}v_{10} is a C 8 C_{8}, v 10 ≁ v 6 v_{10}\nsim v_{6} otherwise v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 4 ​ v 3 ​ v 2 ​ v 6 ​ v 10 v_{10}v_{9}v_{8}v_{7}v_{4}v_{3}v_{2}v_{6}v_{10} is a C 8 C_{8}, v 10 ≁ v 7 v_{10}\nsim v_{7} otherwise v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 10 v_{10}v_{9}v_{8}v_{7}v_{10} is a C 4 C_{4}. So v 10 v_{10} has two neighbors v 12, v 13 ∉ { v 1, v 2, …, v 10 } v_{12},v_{13}\not\in\{v_{1},v_{2},\ldots,v_{10}\}. At least one of v 12 v_{12} and v 13 v_{13}, say v 12 v_{12}, is not adjacent to v 9 v_{9}. Moreover, v 12 ≁ v 1 v_{12}\nsim v_{1} otherwise v 12 ​ v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 2 ​ v 1 ​ v 12 v_{12}v_{10}v_{9}v_{8}v_{7}v_{6}v_{2}v_{1}v_{12} is a C 8 C_{8}, v 12 ≁ v 2 v_{12}\nsim v_{2} otherwise v 12 ​ v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 1 ​ v 2 ​ v 12 v_{12}v_{10}v_{9}v_{8}v_{7}v_{6}v_{1}v_{2}v_{12} is a C 8 C_{8}, v 12 ≁ v 5 v_{12}\nsim v_{5} otherwise v 12 ​ v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 1 ​ v 5 ​ v 12 v_{12}v_{10}v_{9}v_{8}v_{7}v_{6}v_{1}v_{5}v_{12} is a C 8 C_{8}, v 12 ≁ v 6 v_{12}\nsim v_{6} otherwise v 12 ​ v 10 ​ v 9 ​ v 8 ​ v 4 ​ v 5 ​ v 1 ​ v 6 ​ v 12 v_{12}v_{10}v_{9}v_{8}v_{4}v_{5}v_{1}v_{6}v_{12} is a C 8 C_{8}, v 12 ≁ v 8 v_{12}\nsim v_{8} otherwise v 12 ​ v 10 ​ v 9 ​ v 8 ​ v 12 v_{12}v_{10}v_{9}v_{8}v_{12} is a C 4 C_{4}. Note that v 12 v_{12} can not be adjacent to both v 4 v_{4} and v 7 v_{7} since otherwise v 12 ​ v 7 ​ v 8 ​ v 4 ​ v 12 v_{12}v_{7}v_{8}v_{4}v_{12} is a C 4 C_{4}. If v 12 ≁ v 7 v_{12}\nsim v_{7}, then v 12 ​ v 10 ​ v 9 ​ v 8 ​ v 7 ​ v 6 ​ v 1 ​ v 5 v_{12}v_{10}v_{9}v_{8}v_{7}v_{6}v_{1}v_{5} is an induced P 8 P_{8} in G G, a contradiction. If v 12 ≁ v 4 v_{12}\nsim v_{4}, then v 12 ​ v 10 ​ v 9 ​ v 8 ​ v 4 ​ v 5 ​ v 1 ​ v 2 v_{12}v_{10}v_{9}v_{8}v_{4}v_{5}v_{1}v_{2} is an induced P 8 P_{8} in G G, a contradiction. (See Figure 1(c) for an illustration.)

Case 2 v 7 ≁ v 4 v_{7}\nsim v_{4}.

In this case, v 7 v_{7} has two neighbors v 8, v 9 ∉ { v 1, v 2, …, v 7 } v_{8},v_{9}\not\in\{v_{1},v_{2},\ldots,v_{7}\}. We claim that we may assume v 8 ≁ v 4, v 8 ≁ v 6 v_{8}\nsim v_{4},v_{8}\nsim v_{6}. Otherwise, if one of v 8 v_{8} and v 9 v_{9}, say v 9 v_{9}, is adjacent to v 4 v_{4}, then v 8 ≁ v 4 v_{8}\nsim v_{4} otherwise v 8 ​ v 4 ​ v 9 ​ v 7 ​ v 8 v_{8}v_{4}v_{9}v_{7}v_{8} is a C 4 C_{4} and v 8 ≁ v 6 v_{8}\nsim v_{6} otherwise v 8 ​ v 6 ​ v 2 ​ v 1 ​ v 5 ​ v 4 ​ v 9 ​ v 7 ​ v 8 v_{8}v_{6}v_{2}v_{1}v_{5}v_{4}v_{9}v_{7}v_{8} is a C 8 C_{8}. So assume that v 8 ≁ v 4, v 9 ≁ v 4 v_{8}\nsim v_{4},v_{9}\nsim v_{4}. We can also assume that v 8 ≁ v 6 v_{8}\nsim v_{6} since v 8 v_{8} and v 9 v_{9} can not both be adjacent to v 6 v_{6}.

Furthermore, v 8 ≁ v 1 v_{8}\nsim v_{1} otherwise v 8 ​ v 7 ​ v 6 ​ v 1 ​ v 8 v_{8}v_{7}v_{6}v_{1}v_{8} is a C 4 C_{4}, v 8 ≁ v 2 v_{8}\nsim v_{2} otherwise v 8 ​ v 7 ​ v 6 ​ v 2 ​ v 8 v_{8}v_{7}v_{6}v_{2}v_{8} is a C 4 C_{4}, v 8 ≁ v 3 v_{8}\nsim v_{3} otherwise v 8 ​ v 7 ​ v 6 ​ v 2 ​ v 1 ​ v 5 ​ v 4 ​ v 3 ​ v 8 v_{8}v_{7}v_{6}v_{2}v_{1}v_{5}v_{4}v_{3}v_{8} is a C 8 C_{8}, v 8 ≁ v 5 v_{8}\nsim v_{5} otherwise v 8 ​ v 7 ​ v 6 ​ v 1 ​ v 2 ​ v 3 ​ v 4 ​ v 5 ​ v 8 v_{8}v_{7}v_{6}v_{1}v_{2}v_{3}v_{4}v_{5}v_{8} is a C 8 C_{8}. So v 8 v_{8} has two neighbors v 10, v 11 ∉ { v 1, v 2, …, v 8 } v_{10},v_{11}\not\in\{v_{1},v_{2},\ldots,v_{8}\}. At least one of v 10 v_{10} and v 11 v_{11}, say v 10 v_{10}, is not adjacent to v 7 v_{7}. And v 10 ≁ v 3 v_{10}\nsim v_{3} otherwise v 10 ​ v 8 ​ v 7 ​ v 6 ​ v 1 ​ v 5 ​ v 4 ​ v 3 ​ v 10 v_{10}v_{8}v_{7}v_{6}v_{1}v_{5}v_{4}v_{3}v_{10} is a C 8 C_{8}, v 10 ≁ v 4 v_{10}\nsim v_{4} otherwise v 10 ​ v 8 ​ v 7 ​ v 6 ​ v 1 ​ v 2 ​ v 3 ​ v 4 ​ v 10 v_{10}v_{8}v_{7}v_{6}v_{1}v_{2}v_{3}v_{4}v_{10} is a C 8 C_{8}, v 10 ≁ v 5 v_{10}\nsim v_{5} otherwise v 10 ​ v 8 ​ v 7 ​ v 6 ​ v 2 ​ v 3 ​ v 4 ​ v 5 ​ v 10 v_{10}v_{8}v_{7}v_{6}v_{2}v_{3}v_{4}v_{5}v_{10} is a C 8 C_{8}, v 10 ≁ v 6 v_{10}\nsim v_{6} otherwise v 10 ​ v 8 ​ v 7 ​ v 6 ​ v 10 v_{10}v_{8}v_{7}v_{6}v_{10} is a C 4 C_{4}. Note that v 10 v_{10} can not be adjacent to both v 1 v_{1} and v 2 v_{2}, otherwise v 10 ​ v 1 ​ v 6 ​ v 2 ​ v 10 v_{10}v_{1}v_{6}v_{2}v_{10} is a C 4 C_{4}. If v 10 ≁ v 1 v_{10}\nsim v_{1}, then v 10 ​ v 8 ​ v 7 ​ v 6 ​ v 1 ​ v 5 ​ v 4 ​ v 3 v_{10}v_{8}v_{7}v_{6}v_{1}v_{5}v_{4}v_{3} is an induced P 8 P_{8} in G G, a contradiction. If v 10 ≁ v 2 v_{10}\nsim v_{2}, then v 10 ​ v 8 ​ v 7 ​ v 6 ​ v 2 ​ v 3 ​ v 4 ​ v 5 v_{10}v_{8}v_{7}v_{6}v_{2}v_{3}v_{4}v_{5} is an induced P 8 P_{8} in G G, a contradiction. (See Figure 1(d) for an illustration.) ∎

###### Claim 3.3.

k ≥ 6 k\geq 6.

###### Proof.

Suppose that k = 5 k=5. Since δ ⁡ ( G) ≥ 3 \delta(G)\geq 3, v 1 v_{1} has a neighbor v 6 ∉ { v 1, v 2, …, v 5 } v_{6}\not\in\{v_{1},v_{2},\ldots,v_{5}\}. By Claim 3.2 and G G contains no C 4 C_{4}, v 6 ≁ v i v_{6}\nsim v_{i} for i ∈ { 2, 3, 4, 5 } i\in\{2,3,4,5\}. So v 6 v_{6} has two neighbors v 7, v 8 ∉ { v 1, v 2, …, v 5 } v_{7},v_{8}\not\in\{v_{1},v_{2},\ldots,v_{5}\}.

We claim that we may assume v 7 ≁ v 3, v 7 ≁ v 4 v_{7}\nsim v_{3},v_{7}\nsim v_{4}. If one of v 7 v_{7} and v 8 v_{8}, say v 8 v_{8}, is adjacent to v 3 v_{3}, then v 7 ≁ v 3 v_{7}\nsim v_{3} otherwise v 7 ​ v 3 ​ v 8 ​ v 6 ​ v 7 v_{7}v_{3}v_{8}v_{6}v_{7} is a C 4 C_{4}, and v 7 ≁ v 4 v_{7}\nsim v_{4} otherwise v 7 ​ v 6 ​ v 8 ​ v 3 ​ v 2 ​ v 1 ​ v 5 ​ v 4 ​ v 7 v_{7}v_{6}v_{8}v_{3}v_{2}v_{1}v_{5}v_{4}v_{7} is a C 8 C_{8}. By the symmetry between v 7 v_{7} and v 8 v_{8}, we then assume that v 7 ≁ v 3 v_{7}\nsim v_{3} and v 8 ≁ v 3 v_{8}\nsim v_{3}. Furthermore, we can assume that v 7 ≁ v 4 v_{7}\nsim v_{4} since v 7 v_{7} and v 8 v_{8} can not be both adjacent to v 4 v_{4}.

We can also assume v 7 ≁ v 1 v_{7}\nsim v_{1}. Otherwise, suppose that v 7 ∼ v 1 v_{7}\thicksim v_{1}. Then v 8 ≁ v 1 v_{8}\nsim v_{1} otherwise v 7 ​ v 6 ​ v 8 ​ v 1 ​ v 7 v_{7}v_{6}v_{8}v_{1}v_{7} is a C 4 C_{4}, v 8 ≁ v 3 v_{8}\nsim v_{3} otherwise take C = v 1 ​ v 2 ​ v 3 ​ v 8 ​ v 6 ​ v 1 C=v_{1}v_{2}v_{3}v_{8}v_{6}v_{1} and we obtain a contradiction to Claim 3.2, v 8 ≁ v 4 v_{8}\nsim v_{4} otherwise take C = v 1 ​ v 6 ​ v 8 ​ v 4 ​ v 5 ​ v 1 C=v_{1}v_{6}v_{8}v_{4}v_{5}v_{1} and we obtain a contradiction to Claim 3.2. So we take v 8 v_{8} to play the role of v 7 v_{7}.

Furthermore, v 7 ≁ v 2, v 7 ≁ v 5 v_{7}\nsim v_{2},v_{7}\nsim v_{5}, otherwise there is a C 4 C_{4} in G G. By the discussion above, v 7 v_{7} has two neighbors v 9, v 10 ∉ { v 1, v 2, …, v 7 } v_{9},v_{10}\not\in\{v_{1},v_{2},\ldots,v_{7}\}. We claim that we may assume v 9 ≁ v i v_{9}\nsim v_{i}, i ∈ { 1, 2, …, 6 } i\in\{1,2,\ldots,6\}. It is easy to check that v 9 ≁ v 1 v_{9}\nsim v_{1} otherwise v 9 ​ v 7 ​ v 6 ​ v 1 ​ v 9 v_{9}v_{7}v_{6}v_{1}v_{9} is a C 4 C_{4}, v 9 ≁ v 2 v_{9}\nsim v_{2} otherwise v 9 ​ v 7 ​ v 6 ​ v 1 ​ v 5 ​ v 4 ​ v 3 ​ v 2 ​ v 9 v_{9}v_{7}v_{6}v_{1}v_{5}v_{4}v_{3}v_{2}v_{9} is a C 8 C_{8}, v 9 ≁ v 5 v_{9}\nsim v_{5} otherwise v 9 ​ v 7 ​ v 6 ​ v 1 ​ v 2 ​ v 3 ​ v 4 ​ v 5 ​ v 9 v_{9}v_{7}v_{6}v_{1}v_{2}v_{3}v_{4}v_{5}v_{9} is a C 8 C_{8}. By symmetry, v 10 ≁ v 1, v 2, v 5 v_{10}\not\sim v_{1},v_{2},v_{5}. If one of v 9 v_{9} and v 10 v_{10}, say v 10 v_{10}, is adjacent to v 6 v_{6}, then v 9 ≁ v 6 v_{9}\nsim v_{6} otherwise v 9 ​ v 7 ​ v 10 ​ v 6 ​ v 9 v_{9}v_{7}v_{10}v_{6}v_{9} is a C 4 C_{4}, v 9 ≁ v 3 v_{9}\nsim v_{3} otherwise v 9 ​ v 7 ​ v 10 ​ v 6 ​ v 1 ​ v 5 ​ v 4 ​ v 3 ​ v 9 v_{9}v_{7}v_{10}v_{6}v_{1}v_{5}v_{4}v_{3}v_{9} is a C 8 C_{8}, v 9 ≁ v 4 v_{9}\nsim v_{4} otherwise v 9 ​ v 7 ​ v 10 ​ v 6 ​ v 1 ​ v 2 ​ v 3 ​ v 4 ​ v 9 v_{9}v_{7}v_{10}v_{6}v_{1}v_{2}v_{3}v_{4}v_{9} is a C 8 C_{8}. By the symmetry between v 9 v_{9} and v 10 v_{10}, we assume that v 9 ≁ v 6 v_{9}\nsim v_{6} and v 10 ≁ v 6 v_{10}\nsim v_{6}. If one of v 9 v_{9} and v 10 v_{10}, say v 10 v_{10}, is adjacent to v 3 v_{3}, then v 9 ≁ v 3 v_{9}\nsim v_{3} otherwise v 9 ​ v 7 ​ v 10 ​ v 3 ​ v 9 v_{9}v_{7}v_{10}v_{3}v_{9} is a C 4 C_{4}, v 9 ≁ v 4 v_{9}\nsim v_{4} otherwise v 9 ​ v 7 ​ v 10 ​ v 3 ​ v 2 ​ v 1 ​ v 5 ​ v 4 ​ v 9 v_{9}v_{7}v_{10}v_{3}v_{2}v_{1}v_{5}v_{4}v_{9} is a C 8 C_{8}. So assume that v 9 ≁ v 3, v 10 ≁ v 3 v_{9}\nsim v_{3},v_{10}\nsim v_{3}. Finally we can assume that v 9 ≁ v 4 v_{9}\nsim v_{4} since v 9 v_{9} and v 10 v_{10} can not be both adjacent to v 4 v_{4}.

v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} v 8 v_{8} v 9 v_{9} v 10 v_{10} v 11 v_{11} v 12 v_{12} Figure 2: Illustration for Claim 3.3

By the assumption that v 9 ≁ v i v_{9}\nsim v_{i}, i ∈ { 1, 2, …, 6 } i\in\{1,2,\ldots,6\}, v 9 v_{9} has has two neighbors v 11, v 12 ∉ { v 1, v 2, …, v 7 } v_{11},v_{12}\not\in\{v_{1},v_{2},\ldots,v_{7}\}. We claim that by the symmetry between v 11 v_{11} and v 12 v_{12}, we may assume that v 11 ≁ v i v_{11}\nsim v_{i}, i ∈ { 7, 6, 1, 3, 4 } i\in\{7,6,1,3,4\}. It is easy to check that v 11 ≁ v 6 v_{11}\nsim v_{6} otherwise v 11 ​ v 9 ​ v 7 ​ v 6 ​ v 11 v_{11}v_{9}v_{7}v_{6}v_{11} is a C 4 C_{4}, v 11 ≁ v 3 v_{11}\nsim v_{3} otherwise v 11 ​ v 9 ​ v 7 ​ v 6 ​ v 1 ​ v 5 ​ v 4 ​ v 3 ​ v 11 v_{11}v_{9}v_{7}v_{6}v_{1}v_{5}v_{4}v_{3}v_{11} is a C 8 C_{8}, v 11 ≁ v 4 v_{11}\nsim v_{4} otherwise v 11 ​ v 9 ​ v 7 ​ v 6 ​ v 1 ​ v 2 ​ v 3 ​ v 4 ​ v 11 v_{11}v_{9}v_{7}v_{6}v_{1}v_{2}v_{3}v_{4}v_{11} is a C 8 C_{8}. Symmetrically, v 12 ≁ v 6, v 3, v 4 v_{12}\not\sim v_{6},v_{3},v_{4}. If one of v 11 v_{11} and v 12 v_{12}, say v 12 v_{12}, is adjacent to v 7 v_{7}, then v 11 ≁ v 1 v_{11}\nsim v_{1} otherwise take C = v 11 ​ v 9 ​ v 7 ​ v 6 ​ v 1 ​ v 11 C=v_{11}v_{9}v_{7}v_{6}v_{1}v_{11} and we obtain a contradiction to Claim 3.2, v 11 ≁ v 7 v_{11}\nsim v_{7} otherwise v 11 ​ v 9 ​ v 12 ​ v 7 ​ v 11 v_{11}v_{9}v_{12}v_{7}v_{11} is a C 4 C_{4}. So assume that v 11 ≁ v 7, v 12 ≁ v 7 v_{11}\nsim v_{7},v_{12}\nsim v_{7}. Finally we can assume that v 11 ≁ v 1 v_{11}\nsim v_{1} since v 11 v_{11} and v 12 v_{12} can not be both adjacent to v 1 v_{1}.

Note that v 11 ∼ v 2 v_{11}\thicksim v_{2} and v 11 ∼ v 5 v_{11}\thicksim v_{5} can not be both hold since otherwise v 11 ​ v 2 ​ v 1 ​ v 5 ​ v 11 v_{11}v_{2}v_{1}v_{5}v_{11} is a C 4 C_{4}. If v 11 ≁ v 5 v_{11}\nsim v_{5}, then v 11 ​ v 9 ​ v 7 ​ v 6 ​ v 1 ​ v 5 ​ v 4 ​ v 3 v_{11}v_{9}v_{7}v_{6}v_{1}v_{5}v_{4}v_{3} is an induced P 8 P_{8} in G G, a contradiction. If v 11 ≁ v 2 v_{11}\nsim v_{2}, then v 11 ​ v 9 ​ v 7 ​ v 6 ​ v 1 ​ v 2 ​ v 3 ​ v 4 v_{11}v_{9}v_{7}v_{6}v_{1}v_{2}v_{3}v_{4} is an induced P 8 P_{8} in G G, a contradiction. (See Figure 2 for an illustration.) ∎

###### Claim 3.4.

k = 7 k=7.

###### Proof.

Suppose that k ≤ 6 k\leq 6, then k = 6 k=6 by Claim 3.3. So G G contains no C 5 C_{5} since G G contains no induced C 5 C_{5} and no C 4 C_{4}.

Case 1 The cycle C C has two consecutive vertices that have a common neighbor in G G.

We assume, without loss of generality, that v 1 v_{1} and v 2 v_{2} have a common neighbor v 7 v_{7}. Then v 7 ≁ v i v_{7}\nsim v_{i} for i ∈ { 3, 4, 5, 6 } i\in\{3,4,5,6\} as G G contains no C 4, C 5 C_{4},C_{5} or C 8 C_{8}. So v 7 v_{7} has a neighbor v 8 ∉ { v 1, v 2, …, v 7 } v_{8}\not\in\{v_{1},v_{2},\ldots,v_{7}\}. Then v 8 ≁ v i v_{8}\nsim v_{i} for i ∈ { 1, 2, …, 6 } i\in\{1,2,\ldots,6\} as G G contains no C 4, C 5 C_{4},C_{5} or C 8 C_{8}. It follows that v 8 v_{8} has two neighbors v 9, v 10 ∉ { v 1, v 2, …, v 8 } v_{9},v_{10}\not\in\{v_{1},v_{2},\ldots,v_{8}\}. At least one of v 9 v_{9} and v 10 v_{10}, say v 9 v_{9}, is not adjacent to v 7 v_{7} since there is no C 4 C_{4} in G G. Moreover, v 9 ≁ v i v_{9}\nsim v_{i} for i ∈ { 1, 2, …, 6 } i\in\{1,2,\ldots,6\} as G G contains no C 4, C 5 C_{4},C_{5} or C 8 C_{8}. So v 9 ​ v 8 ​ v 7 ​ v 2 ​ v 3 ​ v 4 ​ v 5 ​ v 6 v_{9}v_{8}v_{7}v_{2}v_{3}v_{4}v_{5}v_{6} is an induced P 8 P_{8} in G G, a contradiction. (See Figure 3(a) for an illustration.)

v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} v 8 v_{8} v 9 v_{9} v 10 v_{10} (a) Case 1 v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} v 8 v_{8} v 9 v_{9} v 10 v_{10} v 11 v_{11} (b) Case 2 Figure 3: Illustration for Claim 3.4

Case 2 No two consecutive vertices on C C share a common neighbor in G G.

Since δ ⁡ ( G) ≥ 3 \delta(G)\geq 3, v 1 v_{1} has a neighbor v 7 ∉ { v 1, v 2, …, v 6 } v_{7}\not\in\{v_{1},v_{2},\ldots,v_{6}\}. Then v 7 ≁ v i v_{7}\nsim v_{i} for i ∈ { 2, 3, …, 6 } i\in\{2,3,\ldots,6\} since G G contains no C 4 C_{4} or C 5 C_{5} and by the assumption of Case 2. So v 7 v_{7} have two neighbors v 8, v 9 ∉ { v 1, v 2, …, v 7 } v_{8},v_{9}\not\in\{v_{1},v_{2},\ldots,v_{7}\}. We claim that by the symmetry between v 8 v_{8} and v 9 v_{9}, we may assume that v 8 ≁ v 1 v_{8}\nsim v_{1} and v 8 ≁ v 4 v_{8}\nsim v_{4}. If one of v 8 v_{8} and v 9 v_{9}, say v 9 v_{9}, is adjacent to v 1 v_{1}, then v 8 ≁ v 1 v_{8}\nsim v_{1} otherwise v 8 ​ v 1 ​ v 9 ​ v 7 ​ v 8 v_{8}v_{1}v_{9}v_{7}v_{8} is a C 4 C_{4}, v 8 ≁ v 4 v_{8}\nsim v_{4} otherwise we take C = v 8 ​ v 7 ​ v 1 ​ v 2 ​ v 3 ​ v 4 ​ v 8 C=v_{8}v_{7}v_{1}v_{2}v_{3}v_{4}v_{8} and it is back to Case 1. So we assume v 8 ≁ v 1 v_{8}\nsim v_{1} and v 9 ≁ v 1 v_{9}\nsim v_{1}. We can assume that v 8 ≁ v 4 v_{8}\nsim v_{4} since v 8 v_{8} and v 9 v_{9} can not be both adjacent to v 4 v_{4}.

Moreover v 8 ≁ v i v_{8}\nsim v_{i} for i ∈ { 2, 3, 5, 6 } i\in\{2,3,5,6\} since G G contains no C 4, C 5 C_{4},C_{5} or C 8 C_{8}. So v 8 v_{8} has two neighbors v 10, v 11 ∉ { v 1, v 2, …, v 8 } v_{10},v_{11}\not\in\{v_{1},v_{2},\ldots,v_{8}\}. By the symmetry between v 10 v_{10} and v 11 v_{11}, we claim that we may assume v 10 ≁ v 7, v 10 ≁ v 4 v_{10}\nsim v_{7},v_{10}\nsim v_{4}. If one of v 10 v_{10} and v 11 v_{11}, say v 11 v_{11}, is adjacent to v 7 v_{7}, then v 10 ≁ v 7 v_{10}\nsim v_{7} otherwise v 10 ​ v 8 ​ v 11 ​ v 7 ​ v 10 v_{10}v_{8}v_{11}v_{7}v_{10} is a C 4 C_{4}, v 10 ≁ v 4 v_{10}\nsim v_{4} otherwise v 10 ​ v 8 ​ v 11 ​ v 7 ​ v 1 ​ v 2 ​ v 3 ​ v 4 ​ v 10 v_{10}v_{8}v_{11}v_{7}v_{1}v_{2}v_{3}v_{4}v_{10} is a C 8 C_{8}. So we assume v 10 ≁ v 7 v_{10}\nsim v_{7} and v 11 ≁ v 7 v_{11}\nsim v_{7}. Finally we may assume that v 10 ≁ v 4 v_{10}\nsim v_{4} since v 10 v_{10} and v 11 v_{11} can not be both adjacent to v 4 v_{4}.

Furthermore, v 10 ≁ v i v_{10}\nsim v_{i} for i ∈ { 1, 2, 3, 5, 6 } i\in\{1,2,3,5,6\} since G G contains no C 4, C 5 C_{4},C_{5} or C 8 C_{8}. Then v 10 ​ v 8 ​ v 7 ​ v 1 ​ v 2 ​ v 3 ​ v 4 ​ v 5 v_{10}v_{8}v_{7}v_{1}v_{2}v_{3}v_{4}v_{5} is an induced P 8 P_{8}, a contradiction. (See Figure 3(b) for an illustration.) ∎

By Claim 3.4, k = 7 k=7. Then G G contains no C i C_{i} for i ∈ { 4, 5, 6, 8 } i\in\{4,5,6,8\}. Since δ ⁡ ( G) ≥ 3 \delta(G)\geq 3, v 1 v_{1} has a neighbor v 8 ∉ { v 1, v 2, …, v 7 } v_{8}\not\in\{v_{1},v_{2},\ldots,v_{7}\}. Then v 8 ≁ v i v_{8}\nsim v_{i} for i ∈ { 2, 3, …, 7 } i\in\{2,3,\ldots,7\}. It follows that v 8 v_{8} has two neighbors v 9, v 10 ∉ { v 1, v 2, …, v 8 } v_{9},v_{10}\not\in\{v_{1},v_{2},\ldots,v_{8}\}. We assume, without loss of generality, that v 9 ≁ v 1 v_{9}\nsim v_{1}. Since G G contains no C i C_{i} for i ∈ { 4, 5, 6, 8 } i\in\{4,5,6,8\}, then v 9 ≁ v i v_{9}\nsim v_{i} for i ∈ { 2, 3, …, 7 } i\in\{2,3,\ldots,7\}. It follows that v 9 ​ v 8 ​ v 1 ​ v 2 ​ v 3 ​ v 4 ​ v 5 ​ v 6 v_{9}v_{8}v_{1}v_{2}v_{3}v_{4}v_{5}v_{6} is an induced P 8 P_{8} in G G, a contradiction. (See Figure 4 for an illustration.)

v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} v 8 v_{8} v 9 v_{9} v 10 v_{10} Figure 4: Illustration for k = 7 k=7

We complete the proof of Theorem 1.2. ∎

## References

- [1] Dale Daniel and Stephen E. Shauger. A result on the Erdős-Gyárfás conjecture in planar graphs. In Proceedings of the Thirty-second Southeastern International Conference on Combinatorics, Graph Theory and Computing (Baton Rouge, LA, 2001), volume 153, pages 129–139, 2001.
- [2] Paul Erdős. Some old and new problems in various branches of combinatorics. volume 165/166, pages 227–231. 1997. Graphs and combinatorics (Marseille, 1995).
- [3] Mohammad Hossein Ghaffari and Zohreh Mostaghim. Erdős-Gyárfás conjecture for some families of Cayley graphs. Aequationes Math., 92(1):1–6, 2018.
- [4] Mohsen Ghasemi and Rezvan Varmazyar. On the Erdős-Gyárfás conjecture for some Cayley graphs. Mat. Vesnik, 73(1):37–42, 2021.
- [5] Christopher Carl Heckman and Roi Krakovski. Erdős-Gyárfás conjecture for cubic planar graphs. Electron. J. Combin., 20(2):Paper 7, 43, 2013.
- [6] Pouria Salehi Nowbandegani, Hossein Esfandiari, Mohammad Hassan Shirdareh Haghighi, and Khodakhast Bibak. On the Erdős-Gyárfás conjecture in claw-free graphs. Discuss. Math. Graph Theory, 34(3):635–640, 2014.
- [7] Stephen E. Shauger. Results on the Erdős-Gyárfás conjecture in K 1, m K_{1,m} -free graphs. In Proceedings of the Twenty-ninth Southeastern International Conference on Combinatorics, Graph Theory and Computing (Boca Raton, FL, 1998), volume 134, pages 61–65, 1998.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
