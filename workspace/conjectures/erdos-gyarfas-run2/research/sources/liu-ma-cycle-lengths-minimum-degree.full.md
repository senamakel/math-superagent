<!-- source: https://arxiv.org/html/1508.07912v1 | converted from HTML -->

Cycle lengths and minimum degree of graphs

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1508.07912v1 [math.CO] 31 Aug 2015

# Cycle lengths and minimum degree of graphs

Chun-Hung Liu Thanks: Department of Mathematics, Princeton University, Princeton, New Jersey 08544, USA. Email: chliu@math.princeton.edu. Jie Ma Thanks: School of Mathematical Sciences, University of Science and Technology of China, Hefei, Anhui 230026, China. Email: jiema@ustc.edu.cn. Partially supported by NSFC project 11501539.

###### Abstract

There has been extensive research on cycle lengths in graphs with large minimum degree. In this paper, we obtain several new and tight results in this area. Let G G be a graph with minimum degree at least k + 1 k+1. We prove that if G G is bipartite, then there are k k cycles in G G whose lengths form an arithmetic progression with common difference two. For general graph G G, we show that G G contains ⌊ k / 2 ⌋ \lfloor k/2\rfloor cycles with consecutive even lengths and k − 3 k-3 cycles whose lengths form an arithmetic progression with common difference one or two. In addition, if G G is 2-connected and non-bipartite, then G G contains ⌊ k / 2 ⌋ \lfloor k/2\rfloor cycles with consecutive odd lengths.

Thomassen (1983) made two conjectures on cycle lengths modulo a fixed integer k k: (1) every graph with minimum degree at least k + 1 k+1 contains cycles of all even lengths modulo k k; (2) every 2-connected non-bipartite graph with minimum degree at least k + 1 k+1 contains cycles of all lengths modulo k k. These two conjectures, if true, are best possible. Our results confirm both conjectures when k k is even. And when k k is odd, we show that minimum degree at least k + 4 k+4 suffices. This improves all previous results in this direction. Moreover, our results derive new upper bounds of the chromatic number in terms of the longest sequence of cycles with consecutive (even or odd) lengths.

## 1 Introduction

The study of the distribution of cycle lengths is a fundamental area in modern graph theory, which has led to numerous results in abundant subjects. A common practice is investigating if certain graph properties, such as large average degree, large chromatic number, large connectivity, or nice expansion properties, are sufficient to ensure the existence of cycles of some particular lengths. In this article, all graphs are simple and we consider the distribution of cycle lengths in graphs with large minimum degree, aiming to understand the relation between cycle lengths and minimum degree in great depth.

One classical result in this direction is due to Dirac [11] in 1950s: every graph G G with n ≥ 3 n\geq 3 vertices and with minimum degree at least n / 2 n/2 contains a Hamilton cycle (i.e., a cycle passing through all vertices of G G). Since then, there has been extensive research to investigate cycle lengths in graphs G G with large minimum degree δ ⁡ ( G) \delta(G), where δ ⁡ ( G) \delta(G) desponds on | V ⁡ ( G) | |V(G)|. To name a few, [1, 7, 3] are about the length of the longest cycle, [22] is about the existence of cycles with specified lengths, and [4, 17, 5, 21, 29, 30] are about the range of cycle lengths.

However, it is more general if the minimum degree is independent with the number of vertices. Dirac [11] proved that every 2-connected graph with n n vertices and minimum degree k k contains a cycle of length at least min ⁡ { n, 2 ​ k } \min\{n,2k\}. Voss and Zuluaga [36] generalized this by proving that every 2-connected non-bipartite graph with n n vertices and minimum degree k k contains an even cycle of length at least min ⁡ { n, 2 ​ k } \min\{n,2k\} and an odd cycle of length at least min ⁡ { n, 2 ​ k − 1 } \min\{n,2k-1\}. Bondy and Vince [6] solved a question of Erdős by proving that if all but at most two vertices of G G have degree at least three, then there are two cycles in G G whose lengths differ by one or two. Häggkvist and Scott [24] proved that every connected cubic graph other than K 4 K_{4} contains two cycles whose lengths differ by two.

Bondy and Vince’s theorem was improved by several authors. Häggkvist and Scott [23] proved that every graph with minimum degree Ω ⁡ ( k 2) \Omega(k^{2}) contains k k cycles of consecutive even lengths. Verstraëte [35] improved this quadratic bound to be linear by proving that every graph with average degree at least 8 ​ k 8k and even girth g g contains ( g / 2 − 1) ​ k (g/2-1)k cycles of consecutive even lengths. In [31], Sudakov and Verstraëte further pushed the number of lengths of the cycles to be exponential: every graph with average degree 192 ​ ( k + 1) 192(k+1) and girth g g contains k ⌊ ( g − 1) / 2 ⌋ k^{\lfloor(g-1)/2\rfloor} cycles of consecutive even lengths. Very recently, the second author [27] obtained an analogue for odd cycle: every 2-connected non-bipartite graph with average degree 456 ​ k 456k and girth g g contains k ⌊ ( g − 1) / 2 ⌋ k^{\lfloor(g-1)/2\rfloor} cycles of consecutive odd lengths. On the other hand, without considering the parity of the cycles, Fan [19] obtained similar results with better minimum degree conditions by proving the following result. Every graph G G with minimum degree δ ⁡ ( G) ≥ 3 ​ k \delta(G)\geq 3k contains k + 1 k+1 cycles C 0, C 1, …, C k C_{0},C_{1},...,C_{k} such that | E ⁡ ( C 0) | > k + 1, | E ⁡ ( C i) | − | E ⁡ ( C i − 1) | = 2 |E(C_{0})|>k+1,|E(C_{i})|-|E(C_{i-1})|=2 for all 1 ≤ i ≤ k − 1 1\leq i\leq k-1 and 1 ≤ | E ⁡ ( C k) | − | E ⁡ ( C k − 1) | ≤ 2 1\leq|E(C_{k})|-|E(C_{k-1})|\leq 2, and furthermore, if δ ⁡ ( G) ≥ 3 ​ k + 1 \delta(G)\geq 3k+1, then | E ⁡ ( C k) | − | E ⁡ ( C k − 1) | = 2 |E(C_{k})|-|E(C_{k-1})|=2. In the same paper [19], he also resolved a problem of Bondy and Vince [6] by showing that every 3-connected non-bipartite graph G G with δ ⁡ ( G) ≥ 3 ​ k \delta(G)\geq 3k contains 2 ​ k 2k cycles with consecutive lengths m, m + 1, …, m + 2 ​ k − 1 m,m+1,...,m+2k-1 for some integer m ≥ k + 2 m\geq k+2.

To better understand the above results, we remark that in order to ensure two or more odd cycle lengths, 2-connectedness is necessary in addition to the non-bipartiteness. There exist infinitely many non-bipartite connected graphs with arbitrary large minimum degree but containing a unique odd cycle: for arbitrary t t and odd s s, let G G be obtained from s s disjoint copies of K t, t K_{t,t} and an odd cycle C s C_{s} such that each K t, t K_{t,t} intersects C s C_{s} in exactly one vertex.

### 1.1 Paths and cycles of consecutive lengths

Throughout the rest of this paper, k k is a fixed positive integer, unless otherwise specified. We say that a sequence of paths or cycles H 1, H 2, …, H k H_{1},H_{2},...,H_{k} satisfies the length condition if | E ⁡ ( H 1) | ≥ 2 \lvert E(H_{1})\rvert\geq 2 and | E ⁡ ( H i + 1) | − | E ⁡ ( H i) | = 2 \lvert E(H_{i+1})\rvert-\lvert E(H_{i})\rvert=2 for 1 ≤ i ≤ k − 1 1\leq i\leq k-1. We also say that k k paths or k k cycles satisfy the length condition if they can form such a sequence.

In order to study cycles of consecutive (even or odd) lengths in graphs, we begin by considering paths in bipartite graphs. Our first theorem says that there exist optimal number of paths in bipartite graphs between two fixed vertices and satisfying the length condition.

###### Theorem 1.1.

Let G G be a 2-connected bipartite graph and x, y x,y distinct vertices of G G. If every vertex in G G other than x, y x,y has degree at least k + 1 k+1, then there exist k k paths P 1, P 2, …, P k P_{1},P_{2},...,P_{k} from x x to y y in G G with the length condition.

We point out that this result is crucial to the proofs of all other results in this paper. The minimum degree condition in Theorem 1.1 is tight for infinitely many graphs, by considering the complete bipartite graphs K k, n K_{k,n} for all n ≥ k n\geq k, where x, y x,y are two vertices in the part of size k k.

The following theorem on cycles in bipartite graphs can be derived from Theorem 1.1.

###### Theorem 1.2.

Let G G be a bipartite graph and v v a vertex of G G. If every vertex of G G other than v v has degree at least k + 1 k+1, then G G contains k k cycles with the length condition.

An immediate corollary of Theorem 1.2 is that every bipartite graph with minimum degree at least k + 1 k+1 contains k k cycles with the length condition. The complete bipartite graphs K k, n K_{k,n} for all n ≥ k n\geq k also show the tightness of the minimum degree condition.

We then investigate cycle lengths in general graphs.

###### Theorem 1.3.

If the minimum degree of graph G G is at least k + 1 k+1, then G G contains ⌊ k / 2 ⌋ \lfloor k/2\rfloor cycles with consecutive even lengths. Furthermore, if G G is 2-connected and non-bipartite, then G G contains ⌊ k / 2 ⌋ \lfloor k/2\rfloor cycles with consecutive odd lengths.

We see that Theorem 1.3 is tight, as the complete graph K k + 2 K_{k+2} has exactly ⌊ k / 2 ⌋ \lfloor k/2\rfloor different even cycle lengths regardless of the parity of k k, and it has exactly ⌊ k / 2 ⌋ \lfloor k/2\rfloor different odd cycle lengths when k k is even.

In the coming two theorems, we consider 3-connected and 2-connected non-bipartite graphs respectively.

###### Theorem 1.4.

If G G is a 3-connected non-bipartite graph with minimum degree at least k + 1 k+1, then G G contains 2 ​ ⌊ k − 1 2 ⌋ 2\lfloor\frac{k-1}{2}\rfloor cycles with consecutive lengths.

###### Theorem 1.5.

If G G is a 2-connected non-bipartite graph with minimum degree at least k + 3 k+3, then G G contains k k cycles with consecutive lengths or the length condition.

Theorem 1.4 improves a result of Fan [19], which was originally asked by Bondy and Vince [6]. Note that Bondy and Vince [6] constructed an infinite family of 2-connected non-bipartite graphs with arbitrarily large minimum degree but containing no two cycles whose lengths differ by one. So the connectivity condition in Theorem 1.4 cannot be lowered, and the conclusion for cycles with the length condition in Theorem 1.5 cannot be dropped. Moreover, every graph on at most 2 ​ k 2k vertices does not have k k cycle with the length condition. Hence, K 2 ​ k K_{2k} is an example showing that the conclusion for cycles with consecutive lengths in Theorem 1.5 also cannot be removed when k ≥ 4 k\geq 4. (But Theorem 1.3 ensures the existence of cycles with the length condition when k = 2 k=2.) Therefore, Theorem 1.5 cannot be further improved to require only cycles with consecutive lengths or only cycles with the length condition in general. By considering complete graphs of certain orders, we can see that the difference between the minimum degree conditions in Theorems 1.4 and 1.5 and the optimal bounds is at most two.

The next result studies cycle lengths in general graphs, without assuming connectivity and bipartiteness.

###### Theorem 1.6.

If G G is a graph with minimum degree at least k + 4 k+4, then G G contains k k cycles with consecutive lengths or the length condition.

This improves some aforementioned results in [35, 19]. We direct readers to Section 6 for a discussion on the tightness of this theorem.

### 1.2 Cycle lengths modulo k k

The study of cycle lengths modulo an integer k k can be dated to Burr and Erdős (See [14]). They conjectured that there exists a constant c k c_{k} for each odd k k such that every graph with average degree at least c k c_{k} contains cycles of all lengths modulo k k. This conjecture was resolved by Bollobás in [2], where he proved that c k ≤ 2 ​ [( k + 1) k − 1] / k c_{k}\leq 2[(k+1)^{k}-1]/k. Thomassen [32, 33] generalized this by showing that every graph G G with minimum degree at least 4 ​ k ​ ( k + 1) 4k(k+1) contains cycles of all lengths m m modulo k k, except when m m is odd and k k is even. Note that the exceptional case is needed, as when k k is even and G G is bipartite, there is no odd cycle in G G and thus no cycle of odd length m m modulo k k. Thomassen [32] observed that K k + 1 K_{k+1} has no cycle of length 2 modulo k k, and made the following conjecture.

###### Conjecture 1.7 (Thomassen [32]).

For every positive integer k k, every graph with minimum degree at least k + 1 k+1 contains cycles of all even lengths modulo k k.

Thomassen [32] also proved that there exists a function θ ⁡ ( k) \theta(k) for every k k such that every 2-connected non-bipartite graph with minimum degree at least θ ⁡ ( k) \theta(k) contains cycles of all lengths modulo k k. Note that the same graphs defined before Section 1.1 show that 2-connectivity and non-bipartiteness are necessary conditions here (for even k k).

###### Conjecture 1.8 (Thomassen [32]).

For every positive integer k k, every 2-connected non-bipartite graph with minimum degree at least k + 1 k+1 contains cycles of all lengths modulo k k. 1 1 1 It is quoted from [32] that “ K k + 2 K_{k+2} shows that θ ⁡ ( k) ≥ k + 2 \theta(k)\geq k+2. It is tempting to conjecture that equality holds.” Since K k + 2 K_{k+2} does contain cycles of all lengths modulo k k, we believe that it meant to conjecture θ ⁡ ( k) = k + 1 \theta(k)=k+1.

It is known that the minimum degree Ω ⁡ ( k) \Omega(k) suffices for both Conjectures 1.7 and 1.8. A theorem of Verstraëte [35] implies that for all k k, every graph with average degree at least 8 ​ k 8k contains cycles of all even lengths modulo k k. For all odd k k, a result of Fan [19] shows that minimum degree at least 3 ​ k − 2 3k-2 suffices. Diwan [12] obtained a better bound for Conjecture 1.7 that for every positive integer k k, every graph G G with minimum degree at least 2 ​ k − 1 2k-1 contains cycles of all even lengths modulo k k, and every graph with minimum degree at least k + 1 k+1 contains a cycle of length 4 modulo k k. For Conjecture 1.8, a recent result of [27] about consecutive odd cycles implies that minimum degree Ω ⁡ ( k) \Omega(k) is suffices to ensure the existence of cycles of all lengths modulo k k.

Using our results in Section 1.1, we obtain several consequences on cycle lengths modulo k k, which improve all previous bounds on Conjectures 1.7 and 1.8. In particular, the following theorem settles both Conjectures 1.7 and 1.8 for all even integers k k.

###### Theorem 1.9.

Let k k be a positive even integer. If G G is a graph with minimum degree at least k + 1 k+1, then G G contains cycles of all even lengths modulo k k. Furthermore, if G G is 2-connected and non-bipartite, then G G contains cycles of all lengths modulo k k.

The case for odd k k seems more intricate than the case for even k k. The next two theorems can be derived from Theorems 1.5 and 1.6, respectively.

###### Theorem 1.10.

Let k k be a positive odd integer. If G G is a 2-connected non-bipartite graph with minimum degree at least k + 3 k+3, then G G contains cycles of all lengths modulo k k.

###### Theorem 1.11.

Let k k be a positive odd integer. If G G is a graph with minimum degree at least k + 4 k+4, then G G contains cycles of all lengths modulo k k.

In other words, when k k is odd, the difference between the minimum degree conditions of our results and the bounds of Thomassen’s conjectures is at most three.

### 1.3 Cycles of consecutive lengths and chromatic number

The chromatic number and the length of cycles are also related. Diwan, Kenkre and Vishwanathan [13] conjectured that for every pair of integers m m and k k, if graph G G has no cycle of length m m modulo k k, then the chromatic number of G G is at most k + o ⁡ ( k) k+o(k). This was resolved by Chen, Ma and Zang in a recent paper [8], where they also studied the relations between cycle lengths modulo k k and chromatic number of digraphs.

Given a graph G G, define L e ​ ( G) L_{e}(G) and L o ​ ( G) L_{o}(G) to be the sets of even and odd cycle lengths in G G, respectively. We define c ​ e ​ ( G) ce(G) and c ​ o ​ ( G) co(G) to be the largest integers m m and n n, respectively, such that G G contains m m cycles of consecutive even lengths and n n cycles of consecutive odd lengths. And we denote the largest integer ℓ \ell by c ⁡ ( G) c(G) such that G G contains ℓ \ell cycles of consecutive lengths.

We say that a graph G G is k k -chromatic if its chromatic number χ ⁡ ( G) \chi(G) equals k k. It is well-known that every k k -chromatic graph has a cycle of length at least k k. In 1966, Erdős and Hajnal [18] provided an analogue that every k k -chromatic graph has an odd cycle of length at least k − 1 k-1. Confirming a conjecture of Bollobás and Erdős, Gyarfás [20] generalized the result of Erdős and Hajnal by showing that every graph G G satisfies χ ⁡ ( G) ≤ 2 ​ | L o ​ ( G) | + 2 \chi(G)\leq 2|L_{o}(G)|+2. Mihok and Schiermeyer [28] proved that χ ⁡ ( G) ≤ 2 ​ | L e ​ ( G) | + 3 \chi(G)\leq 2|L_{e}(G)|+3 for every graph G G. Recently, Kostochka, Sudakov and Verstraëte [25] proved a conjecture of Erdős [15] that every triangle-free k k -chromatic graph G G contains at least Ω ⁡ ( k 2 ​ log ⁡ k) \Omega(k^{2}\log k) cycles of consecutive lengths.

Using Theorem 1.3, we obtain a new upper bound of the chromatic number in terms of the longest sequence of consecutive even or odd cycle lengths.

###### Theorem 1.12.

For every graph G G, χ ⁡ ( G) ≤ 2 ​ min ⁡ { c ​ e ​ ( G), c ​ o ​ ( G) } + 3 \chi(G)\leq 2\min\{ce(G),co(G)\}+3.

This strengthens the result of Mihok and Schiermeyer [28], as clearly c ​ e ​ ( G) ≤ | L e ​ ( G) | ce(G)\leq|L_{e}(G)|. In addition, Theorem 1.12 is tight for the complete graphs on odd number of vertices, as min ⁡ { c ​ e ​ ( K 2 ​ k + 3), c ​ o ​ ( K 2 ​ k + 3) } = k \min\{ce(K_{2k+3}),co(K_{2k+3})\}=k.

Moreover, we show that the chromatic number can be bounded from above by the longest sequence of consecutive cycle lengths.

###### Theorem 1.13.

For every graphs G G, χ ⁡ ( G) ≤ c ⁡ ( G) + 4 \chi(G)\leq c(G)+4.

On the other hand, complete graphs show that χ ⁡ ( G) ≥ c ⁡ ( G) + 2 \chi(G)\geq c(G)+2.

### 1.4 Notation and organization

Let G G be a graph and X X a subset of V ⁡ ( G) V(G). We denote the set of vertices not in X X but adjacent to some vertex in X X by N G ​ ( X) N_{G}(X), and we define N G ​ [X]:= N G ​ ( X) ∪ X N_{G}[X]:=N_{G}(X)\cup X. If X = { x } X=\{x\}, we simply write N G ​ ( x) N_{G}(x) and N G ​ [x] N_{G}[x] instead. For a subgraph D D of G G, we define N G ​ ( D):= N G ​ ( V ⁡ ( D)) N_{G}(D):=N_{G}(V(D)) and N G ​ [D]:= N G ​ [V ⁡ ( D)] N_{G}[D]:=N_{G}[V(D)]. Often we drop the subscript when G G is clear from context. For a vertex v v of G G, the degree of v v, denoted by d G ​ ( v) d_{G}(v), is the number of edges in G G incident with v v, and we define d X ​ ( v):= | N G ​ ( v) ∩ X | d_{X}(v):=\lvert N_{G}(v)\cap X\rvert. A vertex is a leaf in G G if it has degree one in G G. For S ⊆ V ⁡ ( G) S\subseteq V(G), we denote the subgraph of G G induced on V ⁡ ( G) − S V(G)-S by G − S G-S; for S ⊆ E ⁡ ( G) S\subseteq E(G), we denote the graph ( V ⁡ ( G), E ⁡ ( G) − S) (V(G),E(G)-S) by G − S G-S. When S ⊆ V ⁡ ( G) ∪ E ⁡ ( G) S\subseteq V(G)\cup E(G) with | S | = 1 \lvert S\rvert=1, we write G − S G-S as G − s G-s, where s s is the unique element of S S. When we identify a subset S S of V ⁡ ( G) V(G), we always delete all resulting loops and parallel edges to keep the graph simple.

A pair ( A, B) (A,B) of subsets of V ⁡ ( G) V(G) is a separation of G G of order k k, if V ⁡ ( G) = A ∪ B V(G)=A\cup B, | A ∩ B | = k |A\cap B|=k and G G has no edge with one end in A − B A-B and the other in B − A B-A. A vertex v v of a graph G G is a cut-vertex if G − v G-v contains more components than G G. A block B B in G G is a maximal connected subgraph of G G such that there exists no cut-vertex of B B. So a block is an isolated vertex, an edge or a 2-connected graph. An end-block in G G is a block in G G containing at most one cut-vertex of G G. If D D is an end-block of G G and a vertex x x is the only cut-vertex of G G with x ∈ V ⁡ ( B) x\in V(B), then we say that D D is an end-block with cut-vertex x x. Let ℬ ⁡ ( G) {\mathcal{B}}(G) be the set of blocks in G G and 𝒞 ⁡ ( G) {\mathcal{C}}(G) be the set of cut-vertices of G G. The block structure of G G is the bipartite graph with bipartition ( ℬ ⁡ ( G), 𝒞 ⁡ ( G)) ({\mathcal{B}}(G),{\mathcal{C}}(G)), where x ∈ 𝒞 ⁡ ( G) x\in{\mathcal{C}}(G) is adjacent to B ∈ ℬ ⁡ ( G) B\in{\mathcal{B}}(G) if and only if x ∈ V ⁡ ( B) x\in V(B). Note that the block structure of any graph G G is a forest, and it is connected if and only if G G is connected. For every positive integer k k, we say that a graph G G is k k -critical if it has chromatic number k k and every proper subgraph of G G has chromatic number less than k k.

The rest of this paper is organized as follows. In Section 2, we consider paths in bipartite graphs and prove Theorem 1.1 by induction. We then apply Theorem 1.1 in Section 3 to obtain results about paths in general graphs, which will be heavily used later. In Section 4, we focus on cycles with the length condition and prove Theorems 1.2 and 1.3, from which we also derive Theorems 1.9 and 1.12. In Section 5, we first prove Theorem 5.2 on cycles of consecutive lengths, and then show how to derive the rest theorems mentioned in this section. Finally, we close the paper by mentioning some concluding remarks and open problems in Section 6.

## 2 Consecutive paths in bipartite graphs

We shall prove Theorem 1.1 in this section. To simplify the arguments, we shall prove a more general (but indeed equivalent) result. For this purpose, we introduce the following important concepts. We say that ( G, x, y) (G,x,y) is a rooted graph if G G is a graph and x, y x,y are distinct vertices of G G. The vertices x, y x,y are called the roots of ( G, x, y) (G,x,y). A rooted graph ( G, x, y) (G,x,y) is bipartite if and only if G G is bipartite. The minimum degree of ( G, x, y) (G,x,y) is min ⁡ { d G ​ ( u): u ∈ V ⁡ ( G) − { x, y } } \min\{d_{G}(u):u\in V(G)-\{x,y\}\}. We say that ( G, x, y) (G,x,y) is 2-connected if

- •

G G is a connected graph with | V ⁡ ( G) | ≥ 3 |V(G)|\geq 3, and

- •

every end-block of G G contains at least one of x, y x,y as a non-cut-vertex.

Note that the block structure of G G is a path if ( G, x, y) (G,x,y) is 2-connected. And x, y x,y are in the same block of G G if and only if G G is 2-connected.

On the other hand, if G G is 2-connected, then ( G, x, y) (G,x,y) is 2-connected for every pair of distinct vertices x, y x,y. Therefore, Theorem 1.1 is an immediate corollary of the following theorem.

###### Theorem 2.1.

Let ( G, x, y) (G,x,y) be a 2-connected bipartite rooted graph. For any positive integer k k, if the minimum degree of ( G, x, y) (G,x,y) is at least k + 1 k+1, then there exist k k paths in G G from x x to y y satisfying the length condition.

We shall prove Theorem 2.1 by induction on | V ⁡ ( G) | + | E ⁡ ( G) | \lvert V(G)\rvert+\lvert E(G)\rvert. In the rest of this section, we define ( G, x, y) (G,x,y) to be a minimum counterexample (with respect to | V ⁡ ( G) | + | E ⁡ ( G) | \lvert V(G)\rvert+\lvert E(G)\rvert). That is, ( G, x, y) (G,x,y) is a 2-connected bipartite rooted graph with minimum degree at least k + 1 k+1 such that G G does not contain k k paths from x x to y y satisfying the length condition; however, for any 2-connected bipartite rooted graph ( H, u, v) (H,u,v) with | V ⁡ ( H) | + | E ⁡ ( H) | < | V ⁡ ( G) | + | E ⁡ ( G) | \lvert V(H)\rvert+\lvert E(H)\rvert<\lvert V(G)\rvert+\lvert E(G)\rvert and for any positive integer r r, if the minimum degree of ( H, u, v) (H,u,v) is at least r + 1 r+1, then there are r r paths in H H from u u to v v satisfying the length condition. By symmetry, we assume that

 | d G ​ ( x) ≤ d G ​ ( y). \displaystyle d_{G}(x)\leq d_{G}(y). |  | (1) |

Throughout the rest of this section, we will exploit related properties of G G and prove a series of lemmas, which will lead to the final contradiction and thus complete the proof of Theorem 2.1. We start by proving the following useful lemma.

###### Lemma 2.2.

| V ⁡ ( G) | ≥ 4 |V(G)|\geq 4, G G is 2-connected, and k ≥ 3 k\geq 3.

Proof. If | V ⁡ ( G) | = 3 \lvert V(G)\rvert=3, then ( G, x, y) (G,x,y) has minimum degree two, so k = 1 k=1 and the theorem follows. Hence | V ⁡ ( G) | ≥ 4 \lvert V(G)\rvert\geq 4.

Suppose that G G is not 2-connected. Then there exist a cut-vertex b b and two connected subgraphs G 1, G 2 G_{1},G_{2} of G G such that G = G 1 ∪ G 2 G=G_{1}\cup G_{2} and V ⁡ ( G 1) ∩ V ⁡ ( G 2) = { b } V(G_{1})\cap V(G_{2})=\{b\}, where x ∈ V ⁡ ( G 1) − b x\in V(G_{1})-b and y ∈ V ⁡ ( G 2) − b y\in V(G_{2})-b. Since | V ⁡ ( G 1) | + | V ⁡ ( G 2) | = | V ⁡ ( G) | + 1 ≥ 5 \lvert V(G_{1})\rvert+\lvert V(G_{2})\rvert=\lvert V(G)\rvert+1\geq 5, by symmetry we may assume that | V ⁡ ( G 1) | ≥ 3 \lvert V(G_{1})\rvert\geq 3. So ( G 1, x, b) (G_{1},x,b) is 2-connected bipartite with minimum degree at least k + 1 k+1. By induction, there exist k k paths P 1, …, P k P_{1},...,P_{k} in G 1 G_{1} from x x to b b with the length condition. Let P P be a path in G 2 G_{2} from b b to y y. Concatenating P P with each P i P_{i} leads to k k paths in G G from x x to y y with the length condition, a contradiction. Therefore G G is 2-connected.

Since G G is 2-connected, Theorem 2.1 is obvious when k = 1 k=1. The case k = 2 k=2 can be derived by the following special case of [19, Corollary 3.1]: if H H is a 2-connected (not necessarily bipartite) graph and every vertex of H H other than two distinct vertices u, v u,v has degree at least three, then H H contains two paths R 1, R 2 R_{1},R_{2} from u u to v v such that | E ⁡ ( R 1) | ≥ 2 \lvert E(R_{1})\rvert\geq 2 and 1 ≤ | E ⁡ ( R 2) | − | E ⁡ ( R 1) | ≤ 2 1\leq\lvert E(R_{2})\rvert-\lvert E(R_{1})\rvert\leq 2. To see the implication for the case k = 2 k=2, just notice that G G is bipartite and thus all paths in G G from x x to y y are of the same parity, implying | E ⁡ ( R 2) | − | E ⁡ ( R 1) | = 2 \lvert E(R_{2})\rvert-\lvert E(R_{1})\rvert=2. This shows that k ≥ 3 k\geq 3.

###### Lemma 2.3.

x x and y y are not adjacent in G G.

Proof. Suppose that x x is adjacent to y y in G G. Let G ′ = G − x ​ y G^{\prime}=G-xy. Since G G is 2-connected, every end-block of G ′ G^{\prime} contains at least one of x, y x,y as non-cut-vertex. Therefore, ( G ′, x, y) (G^{\prime},x,y) is 2-connected bipartite with minimum degree at least k + 1 k+1. The induction hypothesis implies that G ′ G^{\prime}, and hence G G, contains k k paths from x x to y y with the length condition, a contradiction.

###### Lemma 2.4.

G − y G-y has a cycle of length four containing x x.

Proof. Suppose that x x is not contained in any 4-cycle in G − y G-y. Then d N ⁡ ( x) ​ ( v) ≤ 1 ​ for every ​ v ∈ V ⁡ ( G) − { x, y } d_{N(x)}(v)\leq 1\text{ for every }v\in V(G)-\{x,y\}.

Let G ′ G^{\prime} be the graph obtained from G G by contracting N ⁡ [x] N[x] into a new vertex x ′ x^{\prime}. It is clear that G ′ G^{\prime} is connected and bipartite, and the minimum degree of ( G ′, x ′, y) (G^{\prime},x^{\prime},y) is at least k + 1 k+1 in G ′ G^{\prime}. If G ′ G^{\prime} is not 2-connected, then x ′ x^{\prime} is the unique cut-vertex of G ′ G^{\prime}. Let H H be the block of G ′ G^{\prime} containing x ′ x^{\prime} and y y. Note that H = G ′ H=G^{\prime} if G ′ G^{\prime} is 2-connected.

Suppose that H H is not an edge, then ( H, x ′, y) (H,x^{\prime},y) is 2-connected bipartite with minimum degree at least k + 1 k+1. By the induction hypothesis, H H contains k k paths P 1 ′, …, P k ′ P_{1}^{\prime},...,P_{k}^{\prime} from x ′ x^{\prime} to y y with the length condition. So G − x G-x contains k k paths P 1, …, P k P_{1},...,P_{k} from N G ​ ( x) N_{G}(x) to y y with the length condition. Let x i x_{i} be the end of P i P_{i} contained in N G ​ ( x) N_{G}(x) for each 1 ≤ i ≤ k 1\leq i\leq k. By concatenating the edge x ​ x i xx_{i} with P i P_{i} for each 1 ≤ i ≤ k 1\leq i\leq k, G G contains k k paths from x x to y y with the length condition, a contradiction.

Therefore, H H is an edge, which together with Lemma 2.3 shows that N G ​ ( y) ⊆ N G ​ ( x) N_{G}(y)\subseteq N_{G}(x). By ( 1), N G ​ ( x) = N G ​ ( y) N_{G}(x)=N_{G}(y). We denote N G ​ ( x) N_{G}(x) by N N.

Since k ≥ 3 k\geq 3 and G G is bipartite, V ⁡ ( G) ≠ N ∪ { x, y } V(G)\neq N\cup\{x,y\}. So there exists a component D D of G − N G-N not containing x x and y y. Since G G is 2-connected, | N G ​ ( D) | ≥ 2 |N_{G}(D)|\geq 2. Fixing a vertex x ′′ ∈ N G ​ ( D) x^{\prime\prime}\in N_{G}(D), let G ′′ G^{\prime\prime} be the graph obtained from G ​ [N G ​ [D]] G[N_{G}[D]] by identifying N G ​ ( D) − x ′′ N_{G}(D)-x^{\prime\prime} into a new vertex y ′′ y^{\prime\prime}. Since G G is 2-connected and bipartite, ( G ′′, x ′′, y ′′) (G^{\prime\prime},x^{\prime\prime},y^{\prime\prime}) is also 2-connected and bipartite. Since d N ​ ( v) ≤ 1 ​ for every ​ v ∈ V ⁡ ( D) d_{N}(v)\leq 1\text{ for every }v\in V(D), the minimum degree of ( G ′′, x ′′, y ′′) (G^{\prime\prime},x^{\prime\prime},y^{\prime\prime}) is at least k + 1 k+1. By induction, there exists a sequence of k k paths in G ′′ G^{\prime\prime} from x ′′ x^{\prime\prime} to y ′′ y^{\prime\prime} with the length condition. So G − { x, y } G-\{x,y\} contains k k paths from N N to N N with the length condition. By adding an edge between x x and N N and an edge between between y y and N N into each of these k k paths, we can obtain k k paths in G G from x x to y y with the length condition, a contradiction.

The following notion is critical for the rest of the proof in this section. Let s s be a positive integer. A complete bipartite subgraph Q Q of G G with bipartition ( Q 1, Q 2) (Q_{1},Q_{2}) is called an s s -core if x ∈ Q 2 x\in Q_{2}, y ∉ V ⁡ ( Q) y\notin V(Q), | Q 1 | ≥ | Q 2 | = s + 1 |Q_{1}|\geq|Q_{2}|=s+1, and for every v ∈ V ⁡ ( G) − ( V ⁡ ( Q) ∪ { y }) v\in V(G)-(V(Q)\cup\{y\}),

 | d Q 1 ​ ( v) ≤ s + 1 ​ and ​ d Q 2 ​ ( v) ≤ s. \displaystyle d_{Q_{1}}(v)\leq s+1\text{~~~ and ~~~}d_{Q_{2}}(v)\leq s. |  | (2) |

Since G G is bipartite, every vertex v ∈ V ⁡ ( G) − ( V ⁡ ( Q) ∪ { y }) v\in V(G)-(V(Q)\cup\{y\}) is adjacent to at most one of Q 1 Q_{1} and Q 2 Q_{2}, so d Q ​ ( v) = max ⁡ { d Q 1 ​ ( v), d Q 2 ​ ( v) } ≤ s + 1 d_{Q}(v)=\max\{d_{Q_{1}}(v),d_{Q_{2}}(v)\}\leq s+1.

The next lemma is straightforward but will be frequently used. We omit the proof.

###### Lemma 2.5.

If Q Q is an s s -core in G G, then for every u ∈ Q 1 u\in Q_{1} there exist s + 1 s+1 paths in Q Q from x x to u u with lengths 1, 3, …, 2 ​ s + 1 1,3,\ldots,2s+1, respectively, and for every v ∈ Q 2 − x v\in Q_{2}-x there exist s s paths in Q Q from x x to v v with lengths 2, 4, …, 2 ​ s 2,4,\ldots,2s, respectively.

###### Lemma 2.6.

G G contains an s s -core Q Q for some integer s ≥ 1 s\geq 1 such that the following hold. Let C C be the component of G − Q G-Q containing y y. If G G has an edge between C C and Q 2 − x Q_{2}-x, then for every v ∈ V ⁡ ( G) − V ⁡ ( Q ∪ C) v\in V(G)-V(Q\cup C), d Q 1 ​ ( v) ≤ s d_{Q_{1}}(v)\leq s and thus d Q ​ ( v) ≤ s d_{Q}(v)\leq s.

Proof. Recall that y y is not adjacent to x x by Lemma 2.3. By Lemma 2.4 there exists a 4-cycle in G − y G-y containing x x. Thus there exists a complete bipartite subgraph Q Q of G − y G-y with bipartition ( Q 1, Q 2) (Q_{1},Q_{2}) such that x ∈ Q 2 x\in Q_{2} and | Q 1 | ≥ | Q 2 | ≥ 2 \lvert Q_{1}\rvert\geq\lvert Q_{2}\rvert\geq 2. Let C C be the component of G − V ⁡ ( Q) G-V(Q) containing y y. We further choose Q Q such that

1. (a).

| Q 2 | \lvert Q_{2}\rvert is maximum,

2. (b).

subject to (a), Q 1 Q_{1} is maximal, and

3. (c).

subject to (a) and (b), | V ⁡ ( C) | \lvert V(C)\rvert is maximum.

Let s = | Q 2 | − 1 s=|Q_{2}|-1. We first prove that Q Q is an s s -core, which suffices to show ( 2). Suppose to the contrary that there exists a vertex v ∈ V ⁡ ( G) − ( V ⁡ ( Q) ∪ { y }) v\in V(G)-(V(Q)\cup\{y\}) satisfying that d Q 1 ​ ( v) ≥ s + 2 d_{Q_{1}}(v)\geq s+2 or d Q 2 ​ ( v) ≥ s + 1 d_{Q_{2}}(v)\geq s+1. If d Q 1 ​ ( v) ≥ s + 2 d_{Q_{1}}(v)\geq s+2, then | N G ​ ( v) ∩ Q 1 | ≥ s + 2 = | Q 2 ∪ { v } | |N_{G}(v)\cap Q_{1}|\geq s+2=|Q_{2}\cup\{v\}|, and G ⁡ [( N G ​ ( v) ∩ Q 1) ∪ Q 2 ∪ { v }] G[(N_{G}(v)\cap Q_{1})\cup Q_{2}\cup\{v\}] is a complete bipartite subgraph in G − y G-y with bipartition ( N G ​ ( v) ∩ Q 1, Q 2 ∪ { v }) (N_{G}(v)\cap Q_{1},Q_{2}\cup\{v\}), contradicting (a). So d Q 2 ​ ( v) ≥ s + 1 d_{Q_{2}}(v)\geq s+1, that is Q 2 ⊆ N G ​ ( v) Q_{2}\subseteq N_{G}(v). Hence ( Q 1 ∪ { v }, Q 2) (Q_{1}\cup\{v\},Q_{2}) is a complete bipartite subgraph of G − y G-y, contradicting (b). Therefore Q Q is indeed an s s -core.

Suppose that the lemma does not hold. So by ( 2), there exists a vertex v ∈ V ⁡ ( G) − V ⁡ ( Q ∪ C) v\in V(G)-V(Q\cup C) such that | N G ​ ( v) ∩ Q 1 | = s + 1 \lvert N_{G}(v)\cap Q_{1}\rvert=s+1. Assume that some vertex in C C is adjacent to a vertex z ∈ Q 2 − x z\in Q_{2}-x. Let Q 2 ′ = Q 2 ∪ { v } − { z } Q_{2}^{\prime}=Q_{2}\cup\{v\}-\{z\}, Q 1 ′ = { a ∈ V ⁡ ( G): Q 2 ′ ⊆ N G ​ ( a) } Q_{1}^{\prime}=\{a\in V(G):Q_{2}^{\prime}\subseteq N_{G}(a)\}, and Q ′ = G ⁡ [Q 1 ′ ∪ Q 2 ′] Q^{\prime}=G[Q_{1}^{\prime}\cup Q_{2}^{\prime}]. Since y y is not adjacent to x x in G G, y ∉ Q 1 ′ y\not\in Q_{1}^{\prime} and thus y ∉ V ⁡ ( Q ′) y\notin V(Q^{\prime}). Furthermore, N G ​ ( v) ∩ Q 1 ⊆ Q 1 ′ N_{G}(v)\cap Q_{1}\subseteq Q_{1}^{\prime}, so Q ′ Q^{\prime} is a complete bipartite subgraph of G − y G-y containing x x with | Q 1 ′ | ≥ s + 1 = | Q 2 ′ | |Q_{1}^{\prime}|\geq s+1=|Q_{2}^{\prime}|, which also satisfies (a) and (b). However, since v v is in a component of G − V ⁡ ( Q) G-V(Q) different from C C, the component of G − V ⁡ ( Q ′) G-V(Q^{\prime}) containing y y contains C C and z z. This contradicts the choice of Q Q as it violates (c). This proves the lemma.

In the rest of this section, Q Q denotes the s s -core mentioned in Lemma 2.6, and we let C C be the component of G − V ⁡ ( Q) G-V(Q) containing y y.

Next we study the situation when there is an edge between C C and Q 2 − x Q_{2}-x. We will constantly use the following easy fact in the proofs: if A A and B B are two arithmetic progressions with common difference two, then the elements of the set { a + b: a ∈ A, b ∈ B } \{a+b:a\in A,b\in B\} form an arithmetic progression of length | A | + | B | − 1 \lvert A\rvert+\lvert B\rvert-1 with common difference two.

###### Lemma 2.7.

If C C is adjacent in G G to some vertex a ∈ Q 2 − x a\in Q_{2}-x, then the following hold.

1. 1.

G − V ⁡ ( C) G-V(C) does not contain k k paths from x x to a a satisfying the length condition.

2. 2.

G − V ⁡ ( C) G-V(C) does not contain k − s + 1 k-s+1 paths from Q 1 Q_{1} to Q 1 Q_{1} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition.

3. 3.

G − V ⁡ ( C) G-V(C) does not contain k − s + 2 k-s+2 paths from Q 1 Q_{1} to Q 2 − { x, a } Q_{2}-\{x,a\} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition.

4. 4.

G − V ⁡ ( C) G-V(C) does not contain k − s + 1 k-s+1 paths from Q 1 Q_{1} to { x, a } \{x,a\} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition.

Proof. Suppose that G − V ⁡ ( C) G-V(C) contains k k paths from x x to a a satisfying the length condition. Then concatenating each path with a fixed path in G ⁡ [V ⁡ ( C) ∪ { a }] G[V(C)\cup\{a\}] from a a to y y, we obtain k k paths in G G from x x to y y satisfying the length condition, a contradiction.

Suppose that G − V ⁡ ( C) G-V(C) contains k − s + 1 k-s+1 paths P 1, P 2, …, P k − s + 1 P_{1},P_{2},\ldots,P_{k-s+1} from Q 1 Q_{1} to Q 1 Q_{1} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition. For each i i, let u i, v i ∈ Q 1 u_{i},v_{i}\in Q_{1} be the two ends of P i P_{i}. Then Q − { v i, a } Q-\{v_{i},a\} contains s s paths from x x to u i u_{i} with length 1, 3, …, 2 ​ s − 1 1,3,\ldots,2s-1, respectively. By concatenating these s s paths with P i P_{i} and the edge v i ​ a v_{i}a for all 1 ≤ i ≤ k − s + 1 1\leq i\leq k-s+1, we obtain k k paths in G − V ⁡ ( C) G-V(C) from x x to a a with the length condition, a contradiction.

Suppose that G − V ⁡ ( C) G-V(C) contains k − s + 2 k-s+2 paths P 1, P 2, …, P k − s + 2 P_{1},P_{2},\ldots,P_{k-s+2} from Q 1 Q_{1} to Q 2 − { x, a } Q_{2}-\{x,a\} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition. For each i i, let u i ∈ Q 2 − { x, a } u_{i}\in Q_{2}-\{x,a\} and v i ∈ Q 1 v_{i}\in Q_{1} be the ends of P i P_{i}. Then Q − { v i, a } Q-\{v_{i},a\} contains s − 1 s-1 paths from x x to u i u_{i} with length 2, 4, …, 2 ​ s − 2 2,4,\ldots,2s-2, respectively. By concatenating these s − 1 s-1 paths with P i P_{i} and the edge v i ​ a v_{i}a for all 1 ≤ i ≤ k − s + 2 1\leq i\leq k-s+2, we obtain k k paths in G − V ⁡ ( C) G-V(C) from x x to a a with the length condition, a contradiction.

Suppose that G − V ⁡ ( C) G-V(C) contains k − s + 1 k-s+1 paths P 1, P 2, …, P k − s + 1 P_{1},P_{2},\ldots,P_{k-s+1} from Q 1 Q_{1} to { x, a } \{x,a\} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition. For each i i, let u i ∈ Q 1 u_{i}\in Q_{1} and v i ∈ { x, a } v_{i}\in\{x,a\} be the ends of P i P_{i}. Then Q − v i Q-v_{i} contains s s paths from u i u_{i} to { x, a } − v i \{x,a\}-v_{i} with lengths 1, 3, …, 2 ​ s − 1 1,3,\ldots,2s-1, respectively. Concatenating these s s paths with P i P_{i} for all 1 ≤ i ≤ k − s + 1 1\leq i\leq k-s+1, this gives rise to k k paths in G − V ⁡ ( C) G-V(C) from x x to a a with the length condition, a contradiction.

###### Lemma 2.8.

If C C is adjacent in G G to some vertex a ∈ Q 2 − x a\in Q_{2}-x, then N G ​ ( Q 1) ⊆ Q 2 ∪ V ⁡ ( C) N_{G}(Q_{1})\subseteq Q_{2}\cup V(C).

Proof. Suppose that N G ​ ( Q 1) ⊈ Q 2 ∪ V ⁡ ( C) N_{G}(Q_{1})\not\subseteq Q_{2}\cup V(C). Then there is a component D D of G − V ⁡ ( Q) G-V(Q) other than C C with | N G ​ ( D) ∩ Q 1 | ≥ 1 \lvert N_{G}(D)\cap Q_{1}\rvert\geq 1. Since Q Q contains s s paths from x x to a a with the length condition, s ≤ k − 1 s\leq k-1 by Lemma 2.7.

Claim 1: If B B is an end-block of D D, then N G ​ ( B − b) ∩ ( Q 1 ∪ { x, a }) ≠ ∅ N_{G}(B-b)\cap(Q_{1}\cup\{x,a\})\neq\emptyset, where b b is the cut-vertex of D D contained in B B.

Proof of Claim 1. Suppose to the contrary that N G ​ ( B − b) ∩ V ⁡ ( Q) ⊆ Q 2 − { x, a } N_{G}(B-b)\cap V(Q)\subseteq Q_{2}-\{x,a\}. Since G G is 2-connected, we have | V ⁡ ( Q 2) − { x, a } | ≥ 1 |V(Q_{2})-\{x,a\}|\geq 1 and thus s ≥ 2 s\geq 2. Let G 1 G_{1} be the graph obtained from G ⁡ [V ⁡ ( B) ∪ ( N G ​ ( B − b) ∩ V ⁡ ( Q))] G[V(B)\cup(N_{G}(B-b)\cap V(Q))] by identifying N G ​ ( B − b) ∩ V ⁡ ( Q) N_{G}(B-b)\cap V(Q) into a vertex x 1 x_{1}. So ( G 1, x 1, b) (G_{1},x_{1},b) is 2-connected bipartite and has minimum degree at least ( k + 1) − ( s − 2) (k+1)-(s-2). By induction G 1 G_{1} has k − s + 2 k-s+2 paths from x 1 x_{1} to b b with the length condition. There is a path in N G ​ [D − V ⁡ ( B − b)] N_{G}[D-V(B-b)] from b b to Q 1 Q_{1}. So G − V ⁡ ( C) G-V(C) has k − s + 2 k-s+2 paths from Q 2 − { x, a } Q_{2}-\{x,a\} to Q 1 Q_{1} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition, contradicting Lemma 2.7. □ \Box

Claim 2: N G ​ ( D) ∩ { x, a } = ∅ N_{G}(D)\cap\{x,a\}=\emptyset.

Proof of Claim 2. Suppose that N G ​ ( D) ∩ { x, a } ≠ ∅ N_{G}(D)\cap\{x,a\}\neq\emptyset. Let G 2 G_{2} be the graph obtained from N G ​ [D] − ( Q 2 − { x, a }) N_{G}[D]-(Q_{2}-\{x,a\}) by identifying N G ​ ( D) ∩ { x, a } N_{G}(D)\cap\{x,a\} into a vertex x 2 x_{2} and identifying N G ​ ( D) ∩ Q 1 N_{G}(D)\cap Q_{1} into a vertex y 2 y_{2}. For every v ∈ V ⁡ ( G 2) − { x 2, y 2 } v\in V(G_{2})-\{x_{2},y_{2}\}, d Q ​ ( v) ≤ s d_{Q}(v)\leq s by Lemma 2.6, and v v is adjacent to at most one of Q 1 Q_{1} and Q 2 Q_{2}. If v v is not adjacent to Q 1 Q_{1} or Q 2 Q_{2}, then d G 2 ​ ( v) ≥ k + 1 d_{G_{2}}(v)\geq k+1; if v v is adjacent to Q 1 Q_{1}, it is clear that d G 2 ​ ( v) ≥ ( k + 1) − ( s − 1) d_{G_{2}}(v)\geq(k+1)-(s-1); if v v is adjacent to Q 2 Q_{2} but not to any one of x, a x,a, then d Q ​ ( v) ≤ s − 1 d_{Q}(v)\leq s-1, implying that d G 2 ​ ( v) ≥ ( k + 1) − ( s − 1) d_{G_{2}}(v)\geq(k+1)-(s-1); otherwise v v is adjacent to at least one of x, a x,a, then d G 2 ​ ( v) ≥ ( k + 1) − ( s − 1) d_{G_{2}}(v)\geq(k+1)-(s-1). Therefore ( G 2, x 2, y 2) (G_{2},x_{2},y_{2}) has minimum degree at least k − s + 2 k-s+2. By Claim 1, every end-block of G 2 G_{2} contains at least one of x 2, y 2 x_{2},y_{2} as a non-cut-vertex, so ( G 2, x 2, y 2) (G_{2},x_{2},y_{2}) is 2-connected and bipartite. By induction, G 2 G_{2} contains k − s + 1 k-s+1 paths from x 2 x_{2} to y 2 y_{2} satisfying the length condition. So G − V ⁡ ( C) G-V(C) contains k − s + 1 k-s+1 paths from { x, a } \{x,a\} to Q 1 Q_{1} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition, contradicting Lemma 2.7. □ \Box

Claim 3: | N G ​ ( D) ∩ Q 1 | ≥ 2 \lvert N_{G}(D)\cap Q_{1}\rvert\geq 2.

Proof of Claim 3. Suppose to the contrary that | N G ​ ( D) ∩ Q 1 | ≤ 1 \lvert N_{G}(D)\cap Q_{1}\rvert\leq 1. By the choice of the component D D, N G ​ ( D) ∩ Q 1 = { x 3 } N_{G}(D)\cap Q_{1}=\{x_{3}\} for some vertex x 3 x_{3}. Since G G is 2-connected, Claim 2 implies that | N G ​ ( D) ∩ ( Q 2 − { x, a }) | ≥ 1 |N_{G}(D)\cap(Q_{2}-\{x,a\})|\geq 1, so s ≥ 2 s\geq 2. Let G 3 G_{3} be the graph obtained from N G ​ [D] N_{G}[D] by identifying N G ​ ( D) ∩ ( Q 2 − { x, a }) N_{G}(D)\cap(Q_{2}-\{x,a\}) into a vertex y 3 y_{3}. In view of Claim 2, every end-block of G 3 G_{3} contains at least one of x 3, y 3 x_{3},y_{3} as a non-cut-vertex, so ( G 3, x 3, y 3) (G_{3},x_{3},y_{3}) is 2-connected and bipartite. For any v ∈ V ⁡ ( G 3) − { x 3, y 3 } v\in V(G_{3})-\{x_{3},y_{3}\}, if v v is adjacent to Q 1 Q_{1}, then d G 3 ​ ( v) = d G ​ ( v) ≥ k − s + 3 d_{G_{3}}(v)=d_{G}(v)\geq k-s+3; otherwise N G ​ ( v) ∩ Q ⊆ Q 2 − { x, a } N_{G}(v)\cap Q\subseteq Q_{2}-\{x,a\}, also implying d G 3 ​ ( v) ≥ ( k + 1) − ( s − 2) = k − s + 3 d_{G_{3}}(v)\geq(k+1)-(s-2)=k-s+3. By induction, G 3 G_{3} contains k − s + 2 k-s+2 paths from x 3 x_{3} to y 3 y_{3} with the length condition. Hence, G − V ⁡ ( C) G-V(C) contains k − s + 2 k-s+2 paths from Q 1 Q_{1} to Q 2 − { x, a } Q_{2}-\{x,a\} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition, contradicting Lemma 2.7. □ \Box

Fix a vertex x 4 ∈ N G ​ ( D) ∩ Q 1 x_{4}\in N_{G}(D)\cap Q_{1}. Claim 3 ensures that N G ​ ( D) ∩ Q 1 − x 4 ≠ ∅ N_{G}(D)\cap Q_{1}-x_{4}\neq\emptyset. Let G 4 G_{4} be the graph obtained from G ⁡ [N G ​ [D] − Q 2] G[N_{G}[D]-Q_{2}] by identifying N G ​ ( D) ∩ Q 1 − x 4 N_{G}(D)\cap Q_{1}-x_{4} into a vertex y 4 y_{4}. Recall Lemma 2.6 that d Q ​ ( v) ≤ s d_{Q}(v)\leq s for every v ∈ V ⁡ ( D) v\in V(D). For every v ∈ V ⁡ ( G 4) − { x 4, y 4 } v\in V(G_{4})-\{x_{4},y_{4}\} adjacent in G G to Q Q, if v v is adjacent to Q 1 Q_{1}, then d G 4 ​ ( v) ≥ ( k + 1) − ( s − 1) d_{G_{4}}(v)\geq(k+1)-(s-1); otherwise v v is adjacent to Q 2 Q_{2}, so d G 4 ​ ( v) ≥ ( k + 1) − ( s − 1) d_{G_{4}}(v)\geq(k+1)-(s-1) by Claim 2. Hence ( G 4, x 4, y 4) (G_{4},x_{4},y_{4}) has minimum degree at least k − s + 2 k-s+2. By Claims 1 and 2, every end-block of G 4 G_{4} contains at least one of x 4, y 4 x_{4},y_{4} as a non-cut-vertex, so ( G 4, x 4, y 4) (G_{4},x_{4},y_{4}) is 2-connected and bipartite. By induction, G 4 G_{4} contains k − s + 1 k-s+1 paths from x 4 x_{4} to y 4 y_{4} satisfying the length condition. So G − V ⁡ ( C) G-V(C) contains k − s + 1 k-s+1 paths from Q 1 Q_{1} to Q 1 Q_{1} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition, contradicting Lemma 2.7.

###### Lemma 2.9.

C C contains at least two vertices, and no vertex of C − y C-y is a leaf in C C.

Proof. We first prove that no vertex of C − y C-y is a leaf in C C. Suppose that C C has a leaf z ∈ V ⁡ ( C − y) z\in V(C-y). If z z is adjacent to Q 1 Q_{1}, by ( 2) we have s + 1 ≥ d Q 1 ​ ( z) ≥ k s+1\geq d_{Q_{1}}(z)\geq k, so by Lemma 2.5, there are k k paths in V ⁡ ( Q) V(Q) from x x to N G ​ ( z) ∩ Q 1 N_{G}(z)\cap Q_{1} with lengths 1, 3, …, 2 ​ k − 1 1,3,\ldots,2k-1, respectively, which can be easily extended to k k paths in G G from x x to y y with the length condition. Hence z z is adjacent to Q 2 Q_{2}. By Lemma 2.2 and ( 2), we have s ≥ d Q 2 ​ ( z) ≥ k ≥ 3 s\geq d_{Q_{2}}(z)\geq k\geq 3, so there is a vertex a ∈ N G ​ ( z) ∩ Q 2 − x a\in N_{G}(z)\cap Q_{2}-x. By Lemma 2.5, there are k k paths in Q Q from x x to a a with the length condition, contradicting Lemma 2.7.

It suffices to show that C C has at least two vertices. We suppose for a contradiction that C C consists of one vertex, i.e., V ⁡ ( C) = { y } V(C)=\{y\}.

Claim 1: N G ​ ( x) = N G ​ ( y) = Q 1 N_{G}(x)=N_{G}(y)=Q_{1} and V ⁡ ( G) ≠ V ⁡ ( Q ∪ C) V(G)\neq V(Q\cup C).

Proof of Claim 1: If y y is adjacent in G G to a vertex a ∈ Q 2 − x a\in Q_{2}-x, then N G ​ ( Q 1) ⊆ Q 2 ∪ { y } N_{G}(Q_{1})\subseteq Q_{2}\cup\{y\} by Lemma 2.8. Since G G is bipartite, N G ​ ( Q 1) ⊆ Q 2 N_{G}(Q_{1})\subseteq Q_{2}, so s ≥ k s\geq k. Then by Lemma 2.5, Q Q contains k k paths from x x to a a with the length condition, contradicting Lemma 2.7. Hence N G ​ ( y) ⊆ Q 1 ∪ { x } N_{G}(y)\subseteq Q_{1}\cup\{x\}. But x x is not adjacent to y y, so N G ​ ( y) ⊆ Q 1 ⊆ N G ​ ( x) N_{G}(y)\subseteq Q_{1}\subseteq N_{G}(x). By the assumption ( 1), the degree of x x in G G is at most the degree of y y in G G. This proves that N G ​ ( x) = N G ​ ( y) = Q 1 N_{G}(x)=N_{G}(y)=Q_{1}.

Similarly, if V ⁡ ( G) = V ⁡ ( Q ∪ C) V(G)=V(Q\cup C), then N G ​ ( Q 1) = Q 2 ∪ { y } N_{G}(Q_{1})=Q_{2}\cup\{y\} and s ≥ k − 1 s\geq k-1. Let z ∈ N G ​ ( y) ∩ Q 1 z\in N_{G}(y)\cap Q_{1}. By Lemma 2.5, Q Q contains s + 1 ≥ k s+1\geq k paths from x x to z z with the length condition, a contradiction. Therefore, V ⁡ ( G) ≠ V ⁡ ( Q ∪ C) V(G)\neq V(Q\cup C). □ \Box

Claim 2: | Q 1 | ≥ 3 \lvert Q_{1}\rvert\geq 3.

Proof of Claim 2: Suppose | Q 1 | ≤ 2 \lvert Q_{1}\rvert\leq 2, then | Q 1 | = 2 \lvert Q_{1}\rvert=2 and s = 1 s=1. Let Q 1 = { u, w } Q_{1}=\{u,w\}, Q 2 = { v, x } Q_{2}=\{v,x\} and G 1 = G − { x, y } G_{1}=G-\{x,y\}. Note that G 1 G_{1} is connected. By Claim 1, N G ​ ( x) = N G ​ ( y) = { u, w } N_{G}(x)=N_{G}(y)=\{u,w\}, so ( G 1, u, w) (G_{1},u,w) has minimum degree at least k + 1 k+1 in G 1 G_{1}. If G 1 G_{1} is 2-connected, then ( G 1, u, w) (G_{1},u,w) is 2-connected. Otherwise, since G G is 2-connected and N G ​ ( x) = N G ​ ( y) = { u, w } N_{G}(x)=N_{G}(y)=\{u,w\}, u u and w w are in different end-blocks of G 1 G_{1}; since u, w ∈ N G ​ ( v) u,w\in N_{G}(v), v v is the cut-vertex of G 1 G_{1} contained in both of the two end-blocks of G 1 G_{1}. So ( G 1, u, w) (G_{1},u,w) is 2-connected in either case. Therefore, by induction, G 1 G_{1} has k k paths from u u to w w satisfying the length condition. Concatenating them with x ​ u, w ​ y xu,wy gives k k path in G G from x x to y y satisfying the length condition. □ \Box

Let u ∈ Q 1 u\in Q_{1} and v ∈ Q 2 − x v\in Q_{2}-x be fixed. Then any vertex in G − { u, v } G-\{u,v\} other than x, y x,y has degree at least k k in G − { u, v } G-\{u,v\}. If G − { u, v } G-\{u,v\} is 2-connected, then G − { u, v } G-\{u,v\} contains k − 1 k-1 paths from x x to y y with the length condition. Among these paths, let R R be the longest one such that w ∈ Q 1 − u w\in Q_{1}-u is the end of R − y R-y other than x x. These k − 1 k-1 paths from x x to y y together with the path ( R − y) ∪ w ​ v ​ u ​ y (R-y)\cup wvuy are k k paths in G G from x x to y y with the length condition. Hence G − { u, v } G-\{u,v\} is not 2-connected and contains at least two end-blocks.

Suppose that there exists a component H H of G − { u, v } G-\{u,v\} disjoint from Q ∪ C Q\cup C. Since G G is 2-connected, ( G ⁡ [V ⁡ ( H) ∪ { u, v }], u, v) (G[V(H)\cup\{u,v\}],u,v) is 2-connected bipartite and has minimum degree at least k + 1 k+1. So G G contains k k paths from u u to v v internally disjoint from V ⁡ ( Q) ∪ { y } V(Q)\cup\{y\} with the length condition. By concatenating x ​ u xu and v ​ w ​ y vwy with each path, where w w is a vertex in Q 1 − u Q_{1}-u, we obtain k k paths in G G from x x to y y with the length condition, a contradiction. Therefore, G − { u, v } G-\{u,v\} is connected.

By Claims 1 and 2, G ⁡ [V ⁡ ( Q ∪ C)] − { u, v } G[V(Q\cup C)]-\{u,v\} is 2-connected. So there is an end-block B B of G − { u, v } G-\{u,v\} with the cut-vertex b b such that ( B − b) ∩ ( ( Q ∪ C) − { u, v }) = ∅ (B-b)\cap((Q\cup C)-\{u,v\})=\emptyset. Since G − { u, v } G-\{u,v\} is connected, there exists a path P P in G − { u, v } G-\{u,v\} from b b to some vertex z ∈ V ⁡ ( Q ∪ C) − { u, v } z\in V(Q\cup C)-\{u,v\} internally disjoint from ( B ∪ Q ∪ C) − { u, v } (B\cup Q\cup C)-\{u,v\}. Note that z ∉ { x, y } z\notin\{x,y\} as N G ​ ( x) = N G ​ ( y) = Q 1 N_{G}(x)=N_{G}(y)=Q_{1}. So z ∈ V ⁡ ( Q) − { u, v, x } z\in V(Q)-\{u,v,x\}.

Note that N G ​ ( B − b) ⊆ { u, v, b } N_{G}(B-b)\subseteq\{u,v,b\}. Suppose that u ∉ N G ​ ( B − b) u\not\in N_{G}(B-b). Then ( G ⁡ [V ⁡ ( B) ∪ { v }], v, b) (G[V(B)\cup\{v\}],v,b) is 2-connected bipartite with minimum degree at least k + 1 k+1. So induction ensures that G ⁡ [V ⁡ ( B) ∪ { v }] G[V(B)\cup\{v\}] contains k k paths P 1, P 2, …, P k P_{1},P_{2},...,P_{k} from v v to b b with the length condition. If z ∈ Q 1 z\in Q_{1}, let P ′ = P ∪ { z ​ y } P^{\prime}=P\cup\{zy\}; if z ∈ Q 2 z\in Q_{2}, fix a vertex w ∈ Q 1 − u w\in Q_{1}-u and let P ′ = P ∪ { z ​ w, w ​ y } P^{\prime}=P\cup\{zw,wy\}. So in either case P ′ P^{\prime} is a path from b b to y y and internally disjoint from B ∪ { u, v, x } B\cup\{u,v,x\}. By concatenating P i P_{i} with x ​ u ​ v xuv and P ′ P^{\prime} for each 1 ≤ i ≤ k 1\leq i\leq k, we obtain k k paths in G G from x x to y y with the length condition. Therefore, u ∈ N G ​ ( B − b) u\in N_{G}(B-b) and hence ( G ⁡ [V ⁡ ( B) ∪ { u }], u, b) (G[V(B)\cup\{u\}],u,b) is 2-connected.

Since ( G ⁡ [V ⁡ ( B) ∪ { u }], u, b) (G[V(B)\cup\{u\}],u,b) is 2-connected bipartite with minimum degree at least k k, G ⁡ [V ⁡ ( B) ∪ { u }] G[V(B)\cup\{u\}] contains k − 1 k-1 paths from u u to b b with the length condition. By concatenating these paths with P P, this gives a sequence of k − 1 k-1 paths R 1, R 2, …, R k − 1 R_{1},R_{2},...,R_{k-1} in G − v G-v from u u to z z internally disjoint from V ⁡ ( Q ∪ C) V(Q\cup C) with the length condition. If z ∈ Q 1 z\in Q_{1}, then by Claim 2, there exists a vertex w ∈ Q 1 − { u, z } w\in Q_{1}-\{u,z\}, and we let R k R_{k} be the path obtained from R k − 1 R_{k-1} by concatenating z ​ v ​ w zvw. Then R 1, R 2, …, R k R_{1},R_{2},...,R_{k} form a sequence of k k paths in G − { x, y } G-\{x,y\} from Q 1 Q_{1} to Q 1 Q_{1} with the length condition, which, by Claim 1, can be easily extended to k k path in G G from x x to y y with the length condition. Thus z ∈ Q 2 z\in Q_{2}. By Claim 2, there exist two distinct vertices w, w ′ ∈ Q 1 − u w,w^{\prime}\in Q_{1}-u. For each 1 ≤ i ≤ k − 1 1\leq i\leq k-1, let R i ′ R_{i}^{\prime} be the path obtained from R i R_{i} by concatenating x ​ u xu and z ​ w ​ y zwy; and let R k ′ R_{k}^{\prime} be the path obtained from R k − 1 R_{k-1} by concatenating x ​ u xu and z ​ w ​ v ​ w ′ ​ y zwvw^{\prime}y. Therefore, R 1 ′, R 2 ′, …, R k ′ R_{1}^{\prime},R_{2}^{\prime},...,R_{k}^{\prime} form a sequence of k k paths in G G from x x to y y with the length condition. This proves the lemma.

###### Lemma 2.10.

G G has an edge between Q 1 Q_{1} and C − y C-y.

Proof. Note that C − y ≠ ∅ C-y\neq\emptyset by Lemma 2.9. Suppose to the contrary that N G ​ ( C − y) ∩ Q 1 = ∅ N_{G}(C-y)\cap Q_{1}=\emptyset.

We claim that N G ​ ( C − y) ∩ ( Q 2 − x) = ∅ N_{G}(C-y)\cap(Q_{2}-x)=\emptyset. Otherwise, C − y C-y is adjacent to some vertex a ∈ Q 2 − x a\in Q_{2}-x. By Lemma 2.8 and the assumption N G ​ ( C − y) ∩ Q 1 = ∅ N_{G}(C-y)\cap Q_{1}=\emptyset, it follows that N G ​ ( Q 1) ⊆ Q 2 ∪ { y } N_{G}(Q_{1})\subseteq Q_{2}\cup\{y\}. So for some u ∈ Q 1 u\in Q_{1}, N G ​ ( u) ⊆ Q 2 ∪ { y } N_{G}(u)\subseteq Q_{2}\cup\{y\}. This implies that s ≥ k − 1 s\geq k-1, and if s = k − 1 s=k-1, then u ​ y ∈ E ⁡ ( G) uy\in E(G). If s ≥ k s\geq k, by Lemma 2.5, there are at least k k paths in Q Q from x x to a a with the length condition, contradicting Lemma 2.7. So s = k − 1 s=k-1 and thus u ​ y ∈ E ⁡ ( G) uy\in E(G). Again by Lemma 2.5, there are at least k k paths in Q Q from x x to u u with the length condition. Concatenating them with u ​ y uy gives k k paths from x x to y y with the length condition, a contradiction. This proves that N G ​ ( C − y) ∩ ( Q 2 − x) = ∅ N_{G}(C-y)\cap(Q_{2}-x)=\emptyset.

Therefore, N G ​ ( C − y) = { x, y } N_{G}(C-y)=\{x,y\}. Since G G is 2-connected, ( G ⁡ [V ⁡ ( C) ∪ { x }], x, y) (G[V(C)\cup\{x\}],x,y) is 2-connected bipartite and has minimum degree at least k + 1 k+1. By the induction hypothesis, G G contains k k paths from x x to y y satisfying the length condition.

###### Lemma 2.11.

G G does not contain k − s k-s paths from y y to Q 1 Q_{1} internally disjoint from V ⁡ ( Q) V(Q) with the length condition nor k − s + 1 k-s+1 paths from y y to Q 2 − x Q_{2}-x internally disjoint from V ⁡ ( Q) V(Q) with the length condition.

Proof. Suppose to the contrary that there exist k − s k-s paths P 1, …, P k − s P_{1},\dots,P_{k-s} in G G from y y to Q 1 Q_{1} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition. For each 1 ≤ i ≤ k − s 1\leq i\leq k-s, let u i ∈ Q 1 u_{i}\in Q_{1} be the end of P i P_{i} other than y y. By Lemma 2.5, Q Q contains s + 1 s+1 paths from x x to u i u_{i} with lengths 1, 3, …, 2 ​ s + 1 1,3,...,2s+1, respectively. Then concatenating these s + 1 s+1 paths with P i P_{i} for each 1 ≤ i ≤ k − s 1\leq i\leq k-s leads to k k paths in G G from x x to y y with the length condition, a contradiction.

Suppose to the contrary that there exist k − s + 1 k-s+1 paths R 1, …, R k − s + 1 R_{1},\dots,R_{k-s+1} in G G from y y to Q 2 − x Q_{2}-x internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition. For each 1 ≤ j ≤ k − s + 1 1\leq j\leq k-s+1, let v j ∈ Q 2 − x v_{j}\in Q_{2}-x be the end of R j R_{j} other than y y. By Lemma 2.5, Q Q contains s s paths from x x to v j v_{j} with lengths 2, 4, …, 2 ​ s 2,4,\ldots,2s, respectively. Then concatenating these s s paths with R j R_{j} for each 1 ≤ j ≤ k − s + 1 1\leq j\leq k-s+1 leads to k k paths in G G from x x to y y with the length condition, a contradiction.

We say that an end-block B B of C C is feasible if y ∉ V ⁡ ( B − b) y\notin V(B-b), where b b is the cut-vertex of C C contained in B B.

###### Lemma 2.12.

s = 1 s=1, and C C is not 2-connected. Moreover, if B B is a feasible end-block of C C with the cut-vertex b b, then B B is 2-connected and N G ​ ( B − b) = Q 2 ∪ { b } N_{G}(B-b)=Q_{2}\cup\{b\}.

Proof. Recall that C C contains at least two vertices, and no vertex of C − y C-y is a leaf in C C by Lemma 2.9. So every feasible end-block of C C is 2-connected.

Claim 1: C C is not 2-connected, and for each feasible end-block B B of C C with cut-vertex b b, N G ​ ( B − b) ∩ Q 1 = ∅ N_{G}(B-b)\cap Q_{1}=\emptyset.

Proof of Claim 1. Suppose to the contrary. So either C C is 2-connected, or there is an end-block B B of C C with cut-vertex b b such that y ∉ V ⁡ ( B − b) y\notin V(B-b) and B − b B-b is adjacent in G G to Q 1 Q_{1}. In the former case, define B ′ = C B^{\prime}=C and b ′ = y b^{\prime}=y, so B ′ − b ′ B^{\prime}-b^{\prime} is adjacent to Q 1 Q_{1} by Lemma 2.10; in the latter case, define B ′ = B B^{\prime}=B and b ′ = b b^{\prime}=b, so B ′ − b ′ B^{\prime}-b^{\prime} is adjacent to Q 1 Q_{1} by the assumption. Note that there is a path P P in C C from b ′ b^{\prime} to y y internally disjoint from B ′ B^{\prime}. Let X = N G ​ ( B ′ − b ′) ∩ Q 1 X=N_{G}(B^{\prime}-b^{\prime})\cap Q_{1} and define G 1 G_{1} to be the graph obtained from G ⁡ [B ′ ∪ X] G[B^{\prime}\cup X] by identifying X X into a vertex x 1 x_{1}. By ( 2), ( G 1, x 1, b ′) (G_{1},x_{1},b^{\prime}) has minimum degree at least k + 1 − s k+1-s. Since ( G 1, x 1, b ′) (G_{1},x_{1},b^{\prime}) is 2-connected and bipartite, by induction G 1 G_{1} has k − s k-s paths from b ′ b^{\prime} to x 1 x_{1} with the length condition. By concatenating with the path P P, it is easy to obtain k − s k-s paths in G G from y y to Q 1 Q_{1} internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition, contradicting Lemma 2.11. □ \Box

Claim 1 implies that feasible end-blocks of C C exist. Let B B be an arbitrary feasible end-block of C C, and let b b be the cut-vertex of C C contained in B B.

Claim 2: N G ​ ( B − b) ∩ ( Q 2 − x) ≠ ∅ N_{G}(B-b)\cap(Q_{2}-x)\neq\emptyset.

Proof of Claim 2. Suppose to the contrary that N G ​ ( B − b) ∩ ( Q 2 − x) = ∅ N_{G}(B-b)\cap(Q_{2}-x)=\emptyset. By Claim 1 and the 2-connectivity of G G, N G ​ ( B − b) = { b, x } N_{G}(B-b)=\{b,x\}. Define G 2 = G ⁡ [V ⁡ ( B) ∪ { x }] G_{2}=G[V(B)\cup\{x\}]. Since ( G 2, x, b) (G_{2},x,b) is 2-connected bipartite and has minimum degree at least k + 1 k+1, G 2 G_{2} has k k paths from x x to b b with the length condition. By concatenating them with a fixed path in C − V ⁡ ( B − b) C-V(B-b) from b b to y y, we obtain k k paths in G G from x x to y y with the length condition. □ \Box

Finally, we shall prove that s = 1 s=1 and N G ​ ( B − b) = Q 2 ∪ { b } N_{G}(B-b)=Q_{2}\cup\{b\}. Suppose that either s ≥ 2 s\geq 2, or s = 1 s=1 but N G ​ ( B − b) ≠ Q 2 ∪ { b } N_{G}(B-b)\neq Q_{2}\cup\{b\}. Note that the latter case implies that N G ​ ( B − b) = { b } ∪ ( Q 2 − x) N_{G}(B-b)=\{b\}\cup(Q_{2}-x) by Claims 1 and 2. Define G 3 G_{3} to be the graph obtained from G ⁡ [V ⁡ ( B) ∪ ( Q 2 − x)] G[V(B)\cup(Q_{2}-x)] by identifying Q 2 − x Q_{2}-x into vertex a ′ a^{\prime}. Claim 2 implies that ( G 3, a ′, b) (G_{3},a^{\prime},b) is 2-connected and bipartite.

We show that every vertex v ∈ V ⁡ ( G 3) − { a ′, b } v\in V(G_{3})-\{a^{\prime},b\} has degree at least k − s + 2 k-s+2 in G 3 G_{3}. Note that v v has at most s s neighbors in Q 2 Q_{2} by ( 2) and no neighbor in Q 1 Q_{1} by Claim 1. If s ≥ 2 s\geq 2 and v v has at most s − 1 s-1 neighbors in Q 2 Q_{2}, then it is clear that d G 3 ​ ( v) ≥ ( k + 1) − ( s − 1) d_{G_{3}}(v)\geq(k+1)-(s-1). If s ≥ 2 s\geq 2 and v v has exactly s s neighbors in Q 2 Q_{2}, then at least one of them is in Q 2 − x Q_{2}-x and thus d G 3 ​ ( v) ≥ ( k + 1) − ( s − 1) d_{G_{3}}(v)\geq(k+1)-(s-1). It remains to consider s = 1 s=1. In this case, as x ∉ N G ​ ( B − b) x\notin N_{G}(B-b), it is easy to see that d G 3 ​ ( v) ≥ k + 1 d_{G_{3}}(v)\geq k+1. Therefore, ( G 3, a ′, b) (G_{3},a^{\prime},b) has minimum degree at least k − s + 2 k-s+2.

By induction, G 3 G_{3} has k − s + 1 k-s+1 paths from a ′ a^{\prime} to b b with the length condition. Concatenating them with a fixed path in C − V ⁡ ( B − b) C-V(B-b) from b b to y y, we can obtain k − s + 1 k-s+1 paths in G G from y y to Q 2 − x Q_{2}-x internally disjoint from V ⁡ ( Q) V(Q) and satisfying the length condition, contradicting Lemma 2.11.

By Lemma 2.12, C C has at least two end-blocks, but at most one of them contains y y as a non-cut-vertex. So there is at least one feasible end-block of C C. We also see that Q 2 − x Q_{2}-x contains exactly one vertex from Lemma 2.12. In the rest of this section, we denote this vertex by a a. Namely, Q 2 = { a, x } Q_{2}=\{a,x\}.

###### Lemma 2.13.

Let B B be a feasible end-block of C C with the cut-vertex b b. For each vertex u u in Q 2 = { a, x } Q_{2}=\{a,x\}, G ⁡ [V ⁡ ( B) ∪ { u }] G[V(B)\cup\{u\}] has k − 1 k-1 paths from u u to b b with the length condition.

Proof. Define G ′ = G ⁡ [V ⁡ ( B) ∪ { u }] G^{\prime}=G[V(B)\cup\{u\}]. So ( G ′, u, b) (G^{\prime},u,b) is 2-connected and bipartite. By Lemma 2.12, ( G ′, u, b) (G^{\prime},u,b) has minimum degree at least k k. By induction, G ′ G^{\prime} has k − 1 k-1 paths from u u to b b with the length condition.

We complete the proof of Theorem 2.1 in the coming last lemma of this section.

###### Lemma 2.14.

G G is not a counterexample of Theorem 2.1.

Proof. Define N = N G ​ ( Q 1) ∩ V ⁡ ( C − y) N=N_{G}(Q_{1})\cap V(C-y). Lemma 2.10 implies that N ≠ ∅ N\neq\emptyset. Let B 1, B 2, …, B t B_{1},B_{2},...,B_{t} be all feasible end-blocks of C C, and let b i b_{i} be the cut-vertex of C C contained in B i B_{i} for each i i. Let C ′ C^{\prime} be obtained from C C by deleting V ⁡ ( B i − b i) V(B_{i}-b_{i}) for all i i. By Lemma 2.12 and the definition of feasible end-blocks, C ′ C^{\prime} is connected and contains N ∪ { y, b 1, b 2, …, b t } N\cup\{y,b_{1},b_{2},...,b_{t}\}.

Claim 1: There exists c ∈ V ⁡ ( C ′) c\in V(C^{\prime}) such that no path in C ′ − c C^{\prime}-c is from N ∪ { y } N\cup\{y\} to { b 1, b 2, …, b t } \{b_{1},b_{2},...,b_{t}\}.

Proof of Claim 1. Suppose to the contrary that there exist two disjoint paths P 1, P 2 P_{1},P_{2} in C ′ C^{\prime} from N ∪ { y } N\cup\{y\} to { b 1, b 2, …, b t } \{b_{1},b_{2},...,b_{t}\}. Since C ′ C^{\prime} is connected, we may assume that y y is an end of one of P 1, P 2 P_{1},P_{2}, say P 1 P_{1}, by rerouting paths. Denote the end of P 2 P_{2} in N N by w w. By symmetry, we may without loss of generality assume that the ends of P 1, P 2 P_{1},P_{2} in { b 1, b 2, …, b t } \{b_{1},b_{2},...,b_{t}\} are b 1 b_{1} and b 2 b_{2}, respectively. By Lemma 2.13, there exist a sequence of k − 1 k-1 paths R 1, R 2, …, R k − 1 R_{1},R_{2},...,R_{k-1} in G ⁡ [V ⁡ ( B 1) ∪ { a }] G[V(B_{1})\cup\{a\}] from a a to b 1 b_{1} with the length condition and a sequence of k − 1 k-1 paths L 1, L 2, …, L k − 1 L_{1},L_{2},...,L_{k-1} in G ⁡ [V ⁡ ( B 2) ∪ { x }] G[V(B_{2})\cup\{x\}] from x x to b 2 b_{2} with the length condition. Let w ′ ∈ Q 1 ∩ N G ​ ( w) w^{\prime}\in Q_{1}\cap N_{G}(w). Since k ≥ 3 k\geq 3 by Lemma 2.2, for all i, j ∈ { 1, 2, …, k − 1 } i,j\in\{1,2,...,k-1\}, the paths L i ∪ P 2 ∪ w ​ w ′ ​ a ∪ R j ∪ P 1 L_{i}\cup P_{2}\cup ww^{\prime}a\cup R_{j}\cup P_{1} give rise to at least 2 ​ k − 3 ≥ k 2k-3\geq k paths in G G from x x to y y satisfying the length condition, a contradiction. □ \Box

Claim 2: There exists an end-block B y B_{y} of C C with cut-vertex b y b_{y} such that y ∈ V ⁡ ( B y − b y) y\in V(B_{y}-b_{y}).

Proof of Claim 2. Otherwise, all end-blocks of C C are feasible. By Claim 1, there exist a cut-vertex c c of C ′ C^{\prime} and two subgraphs C 1, C 2 C_{1},C_{2} of C ′ C^{\prime} such that C ′ = C 1 ∪ C 2 C^{\prime}=C_{1}\cup C_{2} and V ⁡ ( C 1) ∩ V ⁡ ( C 2) = { c } V(C_{1})\cap V(C_{2})=\{c\}, where N ∪ { y } ⊆ C 1 N\cup\{y\}\subseteq C_{1} and { b 1, b 2, …, b t } ⊆ C 2 \{b_{1},b_{2},...,b_{t}\}\subseteq C_{2}. But C 2 C_{2} contains all cut-vertices of C C contained in some end-blocks of C C, a contradiction. □ \Box

Claim 3: For every v ∈ V ⁡ ( C − y) v\in V(C-y), either d Q ​ ( v) ≤ 1 d_{Q}(v)\leq 1 or v v is a cut-vertex of C C separating y y and all feasible end-blocks of C C.

Proof of Claim 3. Suppose to the contrary that there exist a vertex v ∈ V ⁡ ( C − y) v\in V(C-y) with d Q ​ ( v) ≥ 2 d_{Q}(v)\geq 2 and a feasible end-block B B of C C with cut-vertex b b such that C − v C-v has a path L L from y y to b b internally disjoint from B B. Since s = 1 s=1 by Lemma 2.12, ( 2) ensures that v v is adjacent to two distinct vertices in Q 1 Q_{1}, say u 1, u 2 u_{1},u_{2}. By Lemma 2.13, there exists a sequence of k − 1 k-1 paths P 1, P 2, …, P k − 1 P_{1},P_{2},...,P_{k-1} in G ⁡ [V ⁡ ( B) ∪ { a }] G[V(B)\cup\{a\}] from a a to b b with the length condition. Then x ​ u 1 ​ a ∪ P i ∪ L xu_{1}a\cup P_{i}\cup L for all 1 ≤ i ≤ k − 1 1\leq i\leq k-1 together with x ​ u 2 ​ v ​ u 1 ​ a ∪ P k − 1 ∪ L xu_{2}vu_{1}a\cup P_{k-1}\cup L are k k paths in G G from x x to y y with the length condition, a contradiction. □ \Box

Fix a feasible end-block B B of C C, and let b b be the cut-vertex of C C contained in B B. By Lemma 2.13, there exists a sequence of k − 1 k-1 paths P 1, P 2, …, P k − 1 P_{1},P_{2},...,P_{k-1} in G ⁡ [V ⁡ ( B) ∪ { x }] G[V(B)\cup\{x\}] from x x to b b with the length condition. Concatenating them with a fixed path in C C from b b to b y b_{y}, we obtain a sequence of k − 1 k-1 paths R 1, R 2, …, R k − 1 R_{1},R_{2},...,R_{k-1} in G ⁡ [( V ⁡ ( C) ∪ { x }) − V ⁡ ( B y − b y)] G[(V(C)\cup\{x\})-V(B_{y}-b_{y})] from x x to b y b_{y} with the length condition.

Claim 4: B y B_{y} is an edge y ​ b y yb_{y}.

Proof of Claim 4. Suppose to the contrary that B y B_{y} is 2-connected. For every v ∈ V ⁡ ( B y) − { y, b y } v\in V(B_{y})-\{y,b_{y}\}, v v is not a cut-vertex of C C separating y y and feasible end-blocks of C C, so d Q ​ ( v) ≤ 1 d_{Q}(v)\leq 1 by Claim 3. So ( B y, y, b y) (B_{y},y,b_{y}) is 2-connected bipartite with minimum degree at least k k. By induction, B y B_{y} contains k − 1 k-1 paths from y y to b y b_{y} with the length condition. Concatenating these k − 1 k-1 paths with R i R_{i} for each 1 ≤ i ≤ k − 1 1\leq i\leq k-1, we obtain 2 ​ k − 3 ≥ k 2k-3\geq k paths in G G from x x to y y with the length condition, a contradiction. □ \Box

Suppose that b y b_{y} is adjacent in G G to a vertex z ∈ Q 1 z\in Q_{1}. If y y is adjacent to Q 1 Q_{1}, then Claim 4 will force an odd cycle in G G, a contradiction as G G is bipartite. So N G ​ ( y) ⊆ Q 2 ∪ { b y } N_{G}(y)\subseteq Q_{2}\cup\{b_{y}\}. Since G G is 2-connected and x ​ y ∉ E ⁡ ( G) xy\notin E(G), N G ​ ( y) = { a, b y } N_{G}(y)=\{a,b_{y}\}. Then R i ∪ b y ​ y R_{i}\cup b_{y}y for all 1 ≤ i ≤ k − 1 1\leq i\leq k-1 together with R k − 1 ∪ b y ​ z ​ a ​ y R_{k-1}\cup b_{y}zay form k k paths in G G from x x to y y with the length condition, a contradiction. Therefore, b y b_{y} is not adjacent to Q 1 Q_{1}, that is, b y ∉ N b_{y}\notin N. Also by ( 2), d Q ​ ( b y) ≤ 1 d_{Q}(b_{y})\leq 1.

Let W W be a block of C − y C-y containing b y b_{y}. Since d Q ​ ( b y) ≤ 1 d_{Q}(b_{y})\leq 1, we have d C − y ​ ( b y) ≥ k − 1 ≥ 2 d_{C-y}(b_{y})\geq k-1\geq 2, so W W is 2-connected. If W = B i W=B_{i} for some i i, then V ⁡ ( C) = V ⁡ ( B i) ∪ { y } V(C)=V(B_{i})\cup\{y\}, b y = b i b_{y}=b_{i}, and b y b_{y} is adjacent to Q 1 Q_{1} by Lemmas 2.10 and 2.12, a contradiction. So W W is not an end-block of C C and thus W ∪ { y } ⊆ C ′ W\cup\{y\}\subseteq C^{\prime}.

Since W W is 2-connected and b y ∉ N b_{y}\notin N, Claim 1 implies that there exists a cut-vertex of C ′ C^{\prime} separating N ∪ W ∪ { y } N\cup W\cup\{y\} and { b 1, b 2, …, b t } \{b_{1},b_{2},...,b_{t}\}. Hence C − y C-y has a cut-vertex separating W W and all feasible end-blocks of C C. Note that every cut-vertex of C − y C-y contained in W W has a path to some feasible end-block of C C internally disjoint from W W. Therefore, W W has the unique cut-vertex w w of C − y C-y.

For every v ∈ V ⁡ ( W) − { w, b y } v\in V(W)-\{w,b_{y}\}, since v v is not a cut-vertex of C C separating y y and all feasible end-blocks of C C, we have d Q ​ ( v) ≤ 1 d_{Q}(v)\leq 1 by Claim 3. This together with d Q ​ ( b y) ≤ 1 d_{Q}(b_{y})\leq 1 imply that ( G ⁡ [V ⁡ ( W) ∪ { y }], w, y) (G[V(W)\cup\{y\}],w,y) is 2-connected bipartite with minimum degree at least k k. By induction, there exists a sequence of k − 1 k-1 paths L 1, L 2, …, L k − 1 L_{1},L_{2},...,L_{k-1} in G ⁡ [V ⁡ ( W) ∪ { y }] G[V(W)\cup\{y\}] from w w to y y with the length condition. Recall the k − 1 k-1 paths P 1, P 2, …, P k − 1 P_{1},P_{2},...,P_{k-1} in G ⁡ [V ⁡ ( B) ∪ { x }] G[V(B)\cup\{x\}] from x x to b b. Let R R be a path in C C from b b to w w internally disjoint from B ∪ W ∪ { y } B\cup W\cup\{y\}. Then for all i, j ∈ { 1, 2, …, k − 1 } i,j\in\{1,2,...,k-1\}, the paths P i ∪ R ∪ L j P_{i}\cup R\cup L_{j} give rise to 2 ​ k − 3 ≥ k 2k-3\geq k paths in G G from x x to y y with the length condition, a contradiction.

This proves Theorem 2.1, which implies Theorem 1.1.

## 3 Consecutive paths in general graphs

The following two lemmas extend Theorem 2.1 from bipartite graphs to general graphs, which will be extensively used in the coming sections for finding cycles.

###### Lemma 3.1.

Let ( G, x, y) (G,x,y) be a 2-connected rooted graph. If the minimum degree of ( G, x, y) (G,x,y) is at least k + 1 k+1, then G G contains ⌊ k / 2 ⌋ \lfloor k/2\rfloor paths from x x to y y satisfying the length condition.

Proof. Let G ′ G^{\prime} be a spanning bipartite subgraph of G G with maximum number of edges. So for every vertex v ∈ V ⁡ ( G) v\in V(G), we have d G ′ ​ ( v) ≥ ⌈ d G ​ ( v) / 2 ⌉ d_{G^{\prime}}(v)\geq\lceil d_{G}(v)/2\rceil. Hence, every vertex of G ′ G^{\prime} other than x, y x,y has degree at least ⌊ k / 2 ⌋ + 1 \lfloor k/2\rfloor+1. By the maximality, G ′ G^{\prime} is connected.

Suppose that there exists an end-block B B of G ′ G^{\prime} such that V ⁡ ( B − b) ∩ { x, y } = ∅ V(B-b)\cap\{x,y\}=\emptyset, where b b is the cut-vertex of G ′ G^{\prime} contained in B B. There exists a path P P in G − ( B − b) G-(B-b) from b b to { x, y } \{x,y\} as G ′ G^{\prime} is connected. Since ( G, x, y) (G,x,y) is 2-connected, there exist two disjoint paths in G G from V ⁡ ( B) V(B) to { x, y } \{x,y\} internally disjoint from V ⁡ ( B) V(B). Rerouting these two paths by the path P P, we can further obtain two disjoint paths P 1, P 2 P_{1},P_{2} in G G from V ⁡ ( B) V(B) to { x, y } \{x,y\} internally disjoint from V ⁡ ( B) V(B) such that b b is an end of P 1 P_{1} or P 2 P_{2}, say P 1 P_{1}. We denote the end of P 2 P_{2} in B B by u u. Every vertex in V ⁡ ( B − b) V(B-b) has degree at least ⌊ k / 2 ⌋ + 1 \lfloor k/2\rfloor+1 in B B, so B B is 2-connected bipartite with minimum degree at least ⌊ k / 2 ⌋ + 1 \lfloor k/2\rfloor+1. By Theorem 1.1, B B contains ⌊ k / 2 ⌋ \lfloor k/2\rfloor paths from b b to u u with the length condition. By concatenating each of them with the paths P 1, P 2 P_{1},P_{2}, we obtain ⌊ k / 2 ⌋ \lfloor k/2\rfloor paths in G G from x x to y y satisfying the length condition.

Therefore, every end-block of G ′ G^{\prime} contains at least one of x, y x,y as a non-cut-vertex. So ( G ′, x, y) (G^{\prime},x,y) is 2-connected bipartite with minimum degree at least ⌊ k / 2 ⌋ + 1 \lfloor k/2\rfloor+1, by Theorem 2.1 there exist ⌊ k / 2 ⌋ \lfloor k/2\rfloor paths in G ′ G^{\prime} (and hence in G G) from x x to y y satisfying the length condition.

###### Lemma 3.2.

Let G G a 2-connected graph and x, y, v x,y,v be distinct vertices of G G. If every vertex of G G other than v v has degree at least k + 1 k+1, then G G contains ⌊ ( k − 1) / 2 ⌋ \lfloor(k-1)/2\rfloor paths from x x to y y satisfying the length condition.

Proof. There is nothing to prove when k ≤ 2 k\leq 2, so we may assume that k ≥ 3 k\geq 3. Note that G − v G-v is connected and has minimum degree at least k k. If G − v G-v is 2-connected, then it follows from Lemma 3.1. Hence we may assume that G − v G-v is not 2-connected. Then any end-block of G − v G-v is 2-connected and has a non-cut-vertex adjacent to v v in G G.

Let B B be an arbitrary end-block of G − v G-v, and let b b be the cut-vertex of G − v G-v contained in B B. Suppose that | V ⁡ ( B − b) ∩ { x, y } | = 1 \lvert V(B-b)\cap\{x,y\}\rvert=1. Without loss of generality, we may assume that x ∈ V ⁡ ( B − b) x\in V(B-b). By Lemma 3.1, B B has ⌊ ( k − 1) / 2 ⌋ \lfloor(k-1)/2\rfloor paths from x x to b b with the length condition. Concatenating those paths with a fixed path in ( G − v) − V ⁡ ( B − b) (G-v)-V(B-b) from b b to y y gives ⌊ ( k − 1) / 2 ⌋ \lfloor(k-1)/2\rfloor paths in G G from x x to y y with the length condition. Therefore, | V ⁡ ( B − b) ∩ { x, y } | ∈ { 0, 2 } \lvert V(B-b)\cap\{x,y\}\rvert\in\{0,2\}.

Since G − v G-v is not 2-connected, there exists an end-block B ′ B^{\prime} of G − v G-v with V ⁡ ( B ′ − b ′) ∩ { x, y } = ∅ V(B^{\prime}-b^{\prime})\cap\{x,y\}=\emptyset, where b ′ b^{\prime} is the cut-vertex of G − v G-v contained in B ′ B^{\prime}. It follows that N G ​ ( B ′ − b ′) = { b ′, v } N_{G}(B^{\prime}-b^{\prime})=\{b^{\prime},v\}. Since G G is 2-connected, G G has two disjoint paths P 1, P 2 P_{1},P_{2} from { x, y } \{x,y\} to { b ′, v } \{b^{\prime},v\} and internally disjoint from B B. Without loss of generality, we may assume that P 1 P_{1} is from x x to b ′ b^{\prime} and P 2 P_{2} is from y y to v v. Let u u be a vertex in B ′ − b ′ B^{\prime}-b^{\prime} adjacent to v v in G G. By Lemma 3.1, B ′ B^{\prime} has ⌊ ( k − 1) / 2 ⌋ \lfloor(k-1)/2\rfloor paths R 1, R 2, …, R ⌊ ( k − 1) / 2 ⌋ R_{1},R_{2},...,R_{\lfloor(k-1)/2\rfloor} from b ′ b^{\prime} to u u with the length condition. Then P 1 ∪ R i ∪ u ​ v ∪ P 2 P_{1}\cup R_{i}\cup uv\cup P_{2} for all i i are ⌊ ( k − 1) / 2 ⌋ \lfloor(k-1)/2\rfloor paths in G G from x x to y y with the length condition. This proves the lemma.

## 4 Cycles with the length condition

In this section, we consider cycles with the length condition. We first prove Theorem 1.2 in bipartite graphs. We restate Theorem 1.2 here for the convenience of readers.

Theorem 1.2. Let G G be a bipartite graph and v v a vertex of G G. If every vertex of G G other than v v has degree at least k + 1 k+1, then G G contains k k cycles with the length condition.

Proof. Since there is nothing to prove when k = 0 k=0, we may assume that k ≥ 1 k\geq 1. We define a 2-connected end-block H H of G G and an edge x ​ y ∈ E ⁡ ( H) xy\in E(H) as following. If G G is 2-connected, define H = G H=G, x = v x=v and y y to be any neighbor of x x in G G; if G G is not 2-connected, then define H H to be an end-block of G G such that v ∉ V ⁡ ( H − h) v\notin V(H-h), where h h is the cut-vertex of G G contained in H H, and define x = h x=h and y y to be any neighbor of x x in H H. In either case, we see that every vertex of H H other than x x has degree at least k + 1 k+1, and thus H H is 2-connected bipartite with at least three vertices. By Theorem 1.1, H H has k k paths from x x to y y with the length condition. Note that each path has length at least two and thus does not contain the edge x ​ y xy. By adding the edge x ​ y xy, we then obtain k k cycles in H H (and hence in G G) with the length condition.

Remark. From the above proof, it is easy to see that if G G is 2-connected bipartite with minimum degree at least k + 1 k+1, then for every edge e e of G G, there are k k cycles in G G with the length condition, and all of those cycles contain e e.

We then draw our attention to general graphs and prove Theorem 1.3, which provides optimal bounds for cycles of consecutive even lengths as well as consecutive odd lengths.

Theorem 1.3. If the minimum degree of graph G G is at least k + 1 k+1, then G G contains ⌊ k / 2 ⌋ \lfloor k/2\rfloor cycles with consecutive even lengths. Furthermore, if G G is 2-connected and non-bipartite, then G G contains ⌊ k / 2 ⌋ \lfloor k/2\rfloor cycles with consecutive odd lengths.

Proof. We may assume that k ≥ 2 k\geq 2, as the case k = 1 k=1 is trivial. Let G ′ G^{\prime} be a spanning bipartite subgraph of G G with the maximum number of edges, and let ( A, B) (A,B) be the bipartition of G ′ G^{\prime}. If G ′ G^{\prime} contains a vertex, say v ∈ A v\in A, of degree at most ⌊ k / 2 ⌋ \lfloor k/2\rfloor in G ′ G^{\prime}, then ( A − v, B ∪ { v }) (A-v,B\cup\{v\}) will induce a bipartite subgraph of G G with more edges than G ′ G^{\prime}, a contradiction. So G ′ G^{\prime} has minimum degree at least ⌊ k / 2 ⌋ + 1 \lfloor k/2\rfloor+1. By Theorem 1.2, G ′ G^{\prime} (and hence G G) contains ⌊ k / 2 ⌋ \lfloor k/2\rfloor cycles with the length condition. Note that each of those cycle has even length as G ′ G^{\prime} is bipartite.

Now we assume that G G is 2-connected and non-bipartite additionally. Note that by the maximality, G ′ G^{\prime} is connected and bipartite with minimum degree at least ⌊ k / 2 ⌋ + 1 \lfloor k/2\rfloor+1. Suppose that G ′ G^{\prime} is 2-connected. Since G G is non-bipartite, there exist two vertices x, y x,y such that x ​ y ∈ E ⁡ ( G) − E ⁡ ( G ′) xy\in E(G)-E(G^{\prime}). So both x, y x,y are in the same part of the bipartition ( A, B) (A,B). By Theorem 1.1, G ′ G^{\prime} has ⌊ k / 2 ⌋ \lfloor k/2\rfloor paths from x x to y y with the length condition. Since both of x, y x,y are in the same part in the bipartition, each of these paths of G ′ G^{\prime} has even length. By concatenating these paths with the edge x ​ y xy, we obtain ⌊ k / 2 ⌋ \lfloor k/2\rfloor cycles in G G with consecutive odd lengths. Hence, G ′ G^{\prime} is not 2-connected. Let H H be an end-block of G ′ G^{\prime} and h h be the cut-vertex of G ′ G^{\prime} contained in H H. Every vertex of H H other than h h has degree at least ⌊ k / 2 ⌋ + 1 ≥ 2 \lfloor k/2\rfloor+1\geq 2, so H H is 2-connected. Since G G is 2-connected, there exist z ∈ V ⁡ ( H − h) z\in V(H-h) and w ∈ V ⁡ ( G) − V ⁡ ( H) w\in V(G)-V(H) such that z ​ w ∈ E ⁡ ( G) − E ⁡ ( G ′) zw\in E(G)-E(G^{\prime}). By Theorem 1.1, H H has ⌊ k / 2 ⌋ \lfloor k/2\rfloor paths from z z to h h with the length condition, which, together with a fixed path in G ′ − V ⁡ ( H − h) G^{\prime}-V(H-h) from h h to w w, give ⌊ k / 2 ⌋ \lfloor k/2\rfloor paths in G ′ G^{\prime} from z z to w w with the length condition. As z ​ w ∈ E ⁡ ( G) − E ⁡ ( G ′) zw\in E(G)-E(G^{\prime}), z z and w w are in the same part in the bipartition, so each of those mentioned paths in G ′ G^{\prime} from z z to w w has even length. By concatenating these paths with the edge z ​ w zw, we obtain ⌊ k / 2 ⌋ \lfloor k/2\rfloor cycles in G G with consecutive odd lengths. This proves the theorem.

Remark. In fact, we can obtain ⌊ k / 2 ⌋ \lfloor k/2\rfloor cycles in G G with consecutive even lengths under a weaker condition that all vertices of G G, but one, have degree at least k + 1 k+1. On the other hand, we do not know if this weaker condition can guarantee the existence of ⌊ k / 2 ⌋ \lfloor k/2\rfloor consecutive odd cycles in Theorem 1.3.

As an immediate corollary of Theorem 1.3, we can derive Theorem 1.9, which proves Conjectures 1.7 and 1.8 when k k is even.

Theorem 1.9. Let k k be a positive even integer. If the minimum degree of graph G G is at least k + 1 k+1, then G G contains cycles of all even lengths modulo k k. Furthermore, if G G is 2-connected and non-bipartite, then G G contains cycles of all lengths modulo k k.

Theorem 1.3 also can be used to prove Theorem 1.12, which gives a tight relation between chromatic number and the number of cycles with the length condition.

Theorem 1.12. For every graphs G G, χ ⁡ ( G) ≤ 2 ​ min ⁡ { c ​ e ​ ( G), c ​ o ​ ( G) } + 3 \chi(G)\leq 2\min\{ce(G),co(G)\}+3.

Proof. We may assume that χ ⁡ ( G) ≥ 3 \chi(G)\geq 3, otherwise the theorem is easy. Let G ′ G^{\prime} be a χ ⁡ ( G) \chi(G) -critical subgraph of G G. Since G ′ G^{\prime} is χ ⁡ ( G) \chi(G) -critical, G ′ G^{\prime} is 2-connected non-bipartite and G ′ G^{\prime} has minimum degree at least χ ⁡ ( G) − 1 \chi(G)-1. By Theorem 1.3, G ′ G^{\prime} contains ⌊ χ ⁡ ( G) / 2 ⌋ − 1 \lfloor\chi(G)/2\rfloor-1 cycles with consecutive even lengths and contains ⌊ χ ⁡ ( G) / 2 ⌋ − 1 \lfloor\chi(G)/2\rfloor-1 cycles with consecutive odd lengths. Hence min ⁡ { c ​ e ​ ( G ′), c ​ o ​ ( G ′) } ≥ ⌊ χ ⁡ ( G) / 2 ⌋ − 1 \min\{ce(G^{\prime}),co(G^{\prime})\}\geq\lfloor\chi(G)/2\rfloor-1. As every cycle in G ′ G^{\prime} is a cycle in G G, min ⁡ { c ​ e ​ ( G), c ​ o ​ ( G) } ≥ min ⁡ { c ​ e ​ ( G ′), c ​ o ​ ( G ′) } ≥ ⌊ χ ⁡ ( G) / 2 ⌋ − 1 ≥ ( χ ⁡ ( G) − 1) / 2 − 1 \min\{ce(G),co(G)\}\geq\min\{ce(G^{\prime}),co(G^{\prime})\}\geq\lfloor\chi(G)/2\rfloor-1\geq(\chi(G)-1)/2-1. This proves the theorem.

We conclude this section by proving a lemma about cycles with the length condition.

###### Lemma 4.1.

Let G G be a 2-connected but not 3-connected graph. If the minimum degree of G G is at least k + 1 k+1, then G G contains 2 ​ ⌊ k / 2 ⌋ − 1 2\lfloor k/2\rfloor-1 cycles satisfying the length condition. Furthermore, if G G is bipartite, then G G contains 2 ​ k − 1 2k-1 cycles satisfying the length condition.

Proof. If G G is bipartite, let t = k t=k; otherwise, let t = ⌊ k / 2 ⌋ t=\lfloor k/2\rfloor. Hence, by Theorem 2.1 and Lemma 3.1, for any subgraph G ′ G^{\prime} of G G, if ( G ′, x, y) (G^{\prime},x,y) is 2-connected with minimum degree at least t + 1 t+1, then G ′ G^{\prime} has t t paths from x x to y y with the length condition. We shall prove that G G contains 2 ​ t − 1 2t-1 cycles satisfying the length condition.

Since G G is 2-connected but not 3-connected, there exists a separation ( A, B) (A,B) of G G of order two. Let A ∩ B = { u, v } A\cap B=\{u,v\}. One can easily verify that each of ( G ⁡ [A], u, v) (G[A],u,v) and ( G ⁡ [B], u, v) (G[B],u,v) is a 2-connected rooted graph with minimum degree at least k + 1 k+1. Therefore, G ⁡ [A] G[A] has t t paths P 1, P 2, …, P t P_{1},P_{2},...,P_{t} from u u to v v with the length condition, and G ⁡ [B] G[B] has t t paths R 1, R 2, …, R t R_{1},R_{2},...,R_{t} from u u to v v with the length condition. Then P i ∪ R j P_{i}\cup R_{j} for all 1 ≤ i, j ≤ t 1\leq i,j\leq t are 2 ​ t − 1 2t-1 cycles satisfying the length condition.

## 5 Consecutive cycles

We say that a cycle C C in a connected graph G G is non-separating if G − V ⁡ ( C) G-V(C) is connected. The following lemma studies some property of non-separating odd cycle, which is a slight extension of [19, Lemma 3.4].

###### Lemma 5.1.

Let G G be a graph with minimum degree at least four. If G G contains a non-separating induced odd cycle, then G G contains a non-separating induced odd cycle C C, denoted by v 0 ​ v 1 ​ … ​ v 2 ​ s ​ v 0 v_{0}v_{1}...v_{2s}v_{0}, such that either

1. 1.

C C is a triangle, or

2. 2.

for every non-cut-vertex v v of G − V ⁡ ( C) G-V(C), | N G ​ ( v) ∩ V ⁡ ( C) | ≤ 2 \lvert N_{G}(v)\cap V(C)\rvert\leq 2, and the equality holds if and only if N G ​ ( v) ∩ V ⁡ ( C) = { v i, v i + 2 } N_{G}(v)\cap V(C)=\{v_{i},v_{i+2}\} for some i i, where the indices are taken under the additive group ℤ 2 ​ s + 1 \mathbb{Z}_{2s+1}.

Proof. Let C C be a shortest non-separating induced odd cycle in G G. We denote C = v 0 ​ v 1 ​ … ​ v 2 ​ s ​ v 0 C=v_{0}v_{1}...v_{2s}v_{0}. Let v v be a non-cut-vertex of G − V ⁡ ( C) G-V(C), and let N G ​ ( v) ∩ V ⁡ ( C) = { v i 1, …, v i t } N_{G}(v)\cap V(C)=\{v_{i_{1}},...,v_{i_{t}}\} for some integers i 1, …, i t i_{1},...,i_{t} with 0 ≤ i 1 < … < i t ≤ 2 ​ s 0\leq i_{1}<...<i_{t}\leq 2s. Without loss of generality, we may assume that i 1 = 0 i_{1}=0. For every 1 ≤ j ≤ t 1\leq j\leq t, let C j C_{j} be the cycle v ​ v i j ​ v i j + 1 ​ … ​ v i j + 1 ​ v vv_{i_{j}}v_{i_{j}+1}...v_{i_{j+1}}v. Since the minimum degree of G G is at least four, every vertex in C C has at least one neighbor in G − v − V ⁡ ( C) G-v-V(C), implying that C j C_{j} is non-separating. If i j − 1 = i j + 1 i_{j-1}=i_{j}+1 for some j j, then clearly C j C_{j} is a non-separating triangle and hence C C is a triangle by the minimality. So we may assume that i j + 1 − i j ≥ 2 i_{j+1}-i_{j}\geq 2, for each j j with 1 ≤ j ≤ t − 1 1\leq j\leq t-1, and ( 2 ​ s + 1) − i t ≥ 2 (2s+1)-i_{t}\geq 2. If t ≥ 3 t\geq 3, then for some j j the length of C j C_{j} is odd and less than the length of C C. But C j C_{j} is induced and non-separating, a contradiction to the minimality of | V ⁡ ( C) | |V(C)|. So t ≤ 2 t\leq 2. When t = 2 t=2, by the minimality of | V ⁡ ( C) | |V(C)|, the unique even path in C C from v i 1 v_{i_{1}} to v i 2 v_{i_{2}} has to be of length two. This completes the proof.

###### Theorem 5.2.

Let G G be a 2-connected graph containing a non-separating induced odd cycle. If the minimum degree of G G is at least k + 1 k+1, then G G contains 2 ​ ⌊ k − 1 2 ⌋ 2\lfloor\frac{k-1}{2}\rfloor cycles with consecutive lengths.

Proof. The theorem is obvious when k ≤ 2 k\leq 2. So we may assume that k ≥ 3 k\geq 3. By Lemma 5.1, there exists a non-separating induced odd cycle C = v 0 ​ v 1 ​ … ​ v 2 ​ s ​ v 0 C=v_{0}v_{1}...v_{2s}v_{0} in G G satisfying the conclusions of Lemma 5.1. Throughout this proof, the subscripts will be taken in the additive group ℤ 2 ​ s + 1 \mathbb{Z}_{2s+1}.

Claim 1: s ≥ 2 s\geq 2 and hence C C is not a triangle.

Proof of Claim 1. Suppose to the contrary that C C is a non-separating triangle a ​ b ​ c ​ a abca. Let G ′ = ( G − c) − { a ​ b } G^{\prime}=(G-c)-\{ab\}. Since G G is 2-connected, ( G ′, a, b) (G^{\prime},a,b) is a 2-connected rooted graph with minimum degree at least k k. By Lemma 3.1, G ′ G^{\prime} contains a sequence of ⌊ ( k − 1) / 2 ⌋ \lfloor(k-1)/2\rfloor paths P 1, …, P ⌊ ( k − 1) / 2 ⌋ P_{1},...,P_{\lfloor(k-1)/2\rfloor} from a a to b b satisfying the length condition. Then P i ∪ b ​ a P_{i}\cup ba and P i ∪ b ​ c ​ a P_{i}\cup bca for all 1 ≤ i ≤ ⌊ ( k − 1) / 2 ⌋ 1\leq i\leq\lfloor(k-1)/2\rfloor are 2 ​ ⌊ ( k − 1) / 2 ⌋ 2\lfloor(k-1)/2\rfloor cycles in G G with consecutive lengths. □ \Box

So every non-cut-vertex v v of G − V ⁡ ( C) G-V(C) has d G − V ⁡ ( C) ​ ( v) ≥ k − 1 d_{G-V(C)}(v)\geq k-1. Note that s s is a generator of the additive group ℤ 2 ​ s + 1 {\mathbb{Z}}_{2s+1}. For each 0 ≤ i ≤ 2 ​ s 0\leq i\leq 2s, let v i ′ = v i + s v_{i}^{\prime}=v_{i+s} and v i ′′ = v i + s + 1 v_{i}^{\prime\prime}=v_{i+s+1}. For any two vertices v i, v j v_{i},v_{j} in C C, denote C i, j ′ C^{\prime}_{i,j} and C i, j ′′ C^{\prime\prime}_{i,j} to be the shorter and longer paths in C C from v i v_{i} to v j v_{j}, respectively.

Claim 2: G − V ⁡ ( C) G-V(C) is not 2-connected.

Proof of Claim 2. Suppose to the contrary that G − V ⁡ ( C) G-V(C) is 2-connected. First assume that every vertex of G − V ⁡ ( C) G-V(C) is adjacent in G G to at most one vertex of C C. Then every vertex v ∈ V ⁡ ( G − C) v\in V(G-C) has d G − V ⁡ ( C) ​ ( v) ≥ k d_{G-V(C)}(v)\geq k. There exist distinct vertices x, y ∈ V ⁡ ( G − C) x,y\in V(G-C) such that x ​ v 0, y ​ v s ∈ E ⁡ ( G) xv_{0},yv_{s}\in E(G). By Lemma 3.1, G − V ⁡ ( C) G-V(C) contains ⌊ ( k − 1) / 2 ⌋ \lfloor(k-1)/2\rfloor paths Q 1, …, Q ⌊ ( k − 1) / 2 ⌋ Q_{1},...,Q_{\lfloor(k-1)/2\rfloor} from x x to y y with the length condition. Note that C 0, s ′ C^{\prime}_{0,s} and C 0, s ′′ C^{\prime\prime}_{0,s} are two paths from v 0 v_{0} to v s v_{s} of lengths s, s + 1 s,s+1, respectively. So v 0 ​ x ∪ Q i ∪ y ​ v s ∪ C 0, s ′ v_{0}x\cup Q_{i}\cup yv_{s}\cup C^{\prime}_{0,s} and v 0 ​ x ∪ Q i ∪ y ​ v s ∪ ∪ C 0, s ′′ v_{0}x\cup Q_{i}\cup yv_{s}\cup\cup C^{\prime\prime}_{0,s} for all 1 ≤ i ≤ ⌊ ( k − 1) / 2 ⌋ 1\leq i\leq\lfloor(k-1)/2\rfloor are 2 ​ ⌊ ( k − 1) / 2 ⌋ 2\lfloor(k-1)/2\rfloor cycles in G G with consecutive lengths.

Hence we may assume that there exists some u ∈ V ⁡ ( G − C) u\in V(G-C) adjacent to two vertices of C C in G G. Without loss of generality, let N G ​ ( u) ∩ V ⁡ ( C) = { v 1, v 2 ​ s } N_{G}(u)\cap V(C)=\{v_{1},v_{2s}\}, and let w ∈ V ⁡ ( G − C) w\in V(G-C) such that w ​ v s ∈ E ⁡ ( G) wv_{s}\in E(G). Since G − V ⁡ ( C) G-V(C) is 2-connected with minimum degree at least k − 1 k-1, by Lemma 3.1, G − V ⁡ ( C) G-V(C) contains a sequence of ⌊ ( k − 2) / 2 ⌋ \lfloor(k-2)/2\rfloor paths R 1, …, R ⌊ ( k − 2) / 2 ⌋ R_{1},...,R_{\lfloor(k-2)/2\rfloor} from u u to w w with the length condition. Observe that C 1, s ′ C^{\prime}_{1,s} and C s, 2 ​ s ′ C^{\prime}_{s,2s} are two paths of lengths s − 1 s-1 and s s, respectively and internally disjoint from { v 0, v 1, v 2 ​ s } \{v_{0},v_{1},v_{2s}\}. Thus, v 1 ​ u ∪ R i ∪ w ​ v s ∪ C 1, s ′ v_{1}u\cup R_{i}\cup wv_{s}\cup C^{\prime}_{1,s} and v 2 ​ s ​ u ∪ R i ∪ w ​ v s ∪ C s, 2 ​ s ′ v_{2s}u\cup R_{i}\cup wv_{s}\cup C^{\prime}_{s,2s} for all 1 ≤ i ≤ ⌊ ( k − 2) / 2 ⌋ 1\leq i\leq\lfloor(k-2)/2\rfloor together with v 1 ​ v 0 ​ v 2 ​ s ​ u ∪ R ⌊ ( k − 2) / 2 ⌋ ∪ w ​ v s ∪ C 1, s ′ v_{1}v_{0}v_{2s}u\cup R_{\lfloor(k-2)/2\rfloor}\cup wv_{s}\cup C^{\prime}_{1,s} and v 2 ​ s ​ v 0 ​ v 1 ​ u ∪ R ⌊ ( k − 2) / 2 ⌋ ∪ w ​ v s ∪ C s, 2 ​ s ′ v_{2s}v_{0}v_{1}u\cup R_{\lfloor(k-2)/2\rfloor}\cup wv_{s}\cup C^{\prime}_{s,2s} give 2 ​ ⌊ k / 2 ⌋ 2\lfloor k/2\rfloor cycles in G G with consecutive lengths. □ \Box

Let B B be an end-block of G − V ⁡ ( C) G-V(C) and b b the cut-vertex of G − V ⁡ ( C) G-V(C) contained in B B. Every vertex in B − b B-b has degree at least k − 1 ≥ 2 k-1\geq 2 in B B, and so B B is 2-connected.

Claim 3: There exists x ∈ V ⁡ ( B − b) x\in V(B-b) such that N G ​ ( x) ∩ V ⁡ ( C) = { v j − 1, v j + 1 } N_{G}(x)\cap V(C)=\{v_{j-1},v_{j+1}\} for some j j.

Proof of Claim 3. Suppose not that every vertex in B − b B-b is adjacent in G G to at most one vertex of C C. Then every vertex v ∈ V ⁡ ( B − b) v\in V(B-b) has d B ​ ( v) ≥ k d_{B}(v)\geq k. If there exist x ∈ V ⁡ ( B − b) x\in V(B-b) and y ∈ V ⁡ ( G − C) − V ⁡ ( B − b) y\in V(G-C)-V(B-b) such that v j ​ x, v j ′ ​ y ∈ E ⁡ ( G) v_{j}x,v_{j}^{\prime}y\in E(G) for some j j, then by Lemma 3.1, B B contains ⌊ ( k − 1) / 2 ⌋ \lfloor(k-1)/2\rfloor paths P 1, …, P ⌊ ( k − 1) / 2 ⌋ P_{1},...,P_{\lfloor(k-1)/2\rfloor} from x x to b b with the length condition. Let P P be a path in G − V ⁡ ( C) − V ⁡ ( B − b) G-V(C)-V(B-b) from b b to y y. Also note that C j, j + s ′ C^{\prime}_{j,j+s} and C j, j + s ′′ C^{\prime\prime}_{j,j+s} are two paths in C C from v j v_{j} to v j ′ v_{j}^{\prime} of lengths s s and s + 1 s+1, respectively. Then, v j ​ x ∪ P i ∪ P ∪ y ​ v j ′ ∪ C j, j + s ′ v_{j}x\cup P_{i}\cup P\cup yv_{j}^{\prime}\cup C^{\prime}_{j,j+s} and v j ​ x ∪ P i ∪ P ∪ y ​ v j ′ ∪ C j, j + s ′′ v_{j}x\cup P_{i}\cup P\cup yv_{j}^{\prime}\cup C^{\prime\prime}_{j,j+s} for all 1 ≤ i ≤ ⌊ ( k − 1) / 2 ⌋ 1\leq i\leq\lfloor(k-1)/2\rfloor are 2 ​ ⌊ ( k − 1) / 2 ⌋ 2\lfloor(k-1)/2\rfloor cycles in G G with consecutive lengths. Hence, we may assume that if v j v_{j} is adjacent to V ⁡ ( B − b) V(B-b), then N G ​ ( v j ′) ∩ V ⁡ ( G − C) ⊆ V ⁡ ( B − b) N_{G}(v_{j}^{\prime})\cap V(G-C)\subseteq V(B-b). There is some vertex of C C adjacent in G G to V ⁡ ( B − b) V(B-b), and s s is a generator of ℤ 2 ​ s + 1 {\mathbb{Z}}_{2s+1}, so we derive that N G ​ ( C) ⊆ V ⁡ ( B − b) N_{G}(C)\subseteq V(B-b). This implies that b b is a cut-vertex of G G, but G G is 2-connected, a contradiction. □ \Box

Claim 4: N G ​ ( { v j ′, v j ′′ }) ∩ V ⁡ ( G − C) ⊆ V ⁡ ( B − b) N_{G}(\{v^{\prime}_{j},v^{\prime\prime}_{j}\})\cap V(G-C)\subseteq V(B-b).

Proof of Claim 4. Suppose not, by symmetry we may assume that v j ′ ​ y ∈ E ⁡ ( G) v^{\prime}_{j}y\in E(G) for some y ∈ V ⁡ ( G − C) − V ⁡ ( B − b) y\in V(G-C)-V(B-b). Since every vertex in B − b B-b has degree at least k − 1 k-1, by Lemma 3.1, B B contains ⌊ ( k − 2) / 2 ⌋ \lfloor(k-2)/2\rfloor paths Q 1, …, Q ⌊ ( k − 2) / 2 ⌋ Q_{1},...,Q_{\lfloor(k-2)/2\rfloor} from x x to b b with the length condition. Let Q Q be a fixed path in G − V ⁡ ( C) − V ⁡ ( B − b) G-V(C)-V(B-b) from b b to y y. Note that C j + 1, j + s ′, C j − 1, j + s ′ C^{\prime}_{j+1,j+s},C^{\prime}_{j-1,j+s} are two paths in C C from v j ′ v_{j}^{\prime} to v j + 1, v j − 1 v_{j+1},v_{j-1} with lengths s − 1, s s-1,s, respectively and internally disjoint from { v j − 1, v j, v j + 1 } \{v_{j-1},v_{j},v_{j+1}\}. Then, v j + 1 ​ x ∪ Q i ∪ Q ∪ y ​ v j ′ ∪ C j + 1, j + s ′ v_{j+1}x\cup Q_{i}\cup Q\cup yv^{\prime}_{j}\cup C^{\prime}_{j+1,j+s} and v j − 1 ​ x ∪ Q i ∪ Q ∪ y ​ v j ′ ∪ C j − 1, j + s ′ v_{j-1}x\cup Q_{i}\cup Q\cup yv^{\prime}_{j}\cup C^{\prime}_{j-1,j+s} for all 1 ≤ i ≤ ⌊ ( k − 2) / 2 ⌋ 1\leq i\leq\lfloor(k-2)/2\rfloor, together with v j + 1 ​ v j ​ v j − 1 ​ x ∪ Q ⌊ ( k − 2) / 2 ⌋ ∪ Q ∪ y ​ v j ′ ∪ C j + 1, j + s ′ v_{j+1}v_{j}v_{j-1}x\cup Q_{\lfloor(k-2)/2\rfloor}\cup Q\cup yv^{\prime}_{j}\cup C^{\prime}_{j+1,j+s} and v j − 1 ​ v j ​ v j + 1 ​ x ∪ Q ⌊ ( k − 2) / 2 ⌋ ∪ Q ∪ y ​ v j ′ ∪ C j − 1, j + s ′ v_{j-1}v_{j}v_{j+1}x\cup Q_{\lfloor(k-2)/2\rfloor}\cup Q\cup yv^{\prime}_{j}\cup C^{\prime}_{j-1,j+s}, are 2 ​ ⌊ k / 2 ⌋ 2\lfloor k/2\rfloor cycles in G G with consecutive lengths. □ \Box

Since d G − V ⁡ ( C) ​ ( v j ′) ≥ k − 1 ≥ 2 d_{G-V(C)}(v^{\prime}_{j})\geq k-1\geq 2, there exists z ∈ V ⁡ ( B) − { b, x } z\in V(B)-\{b,x\} adjacent to v j ′ v^{\prime}_{j}. Every vertex of B B other than b b has degree at least k − 1 k-1 in B B. By Lemma 3.2, B B has ⌊ ( k − 3) / 2 ⌋ \lfloor(k-3)/2\rfloor paths R 1, …, R ⌊ ( k − 3) / 2 ⌋ R_{1},...,R_{\lfloor(k-3)/2\rfloor} from x x to z z with the length condition. Then, v j + 1 ​ x ∪ R i ∪ z ​ v j ′ ∪ C j + 1, j + s ′ v_{j+1}x\cup R_{i}\cup zv^{\prime}_{j}\cup C^{\prime}_{j+1,j+s} and v j − 1 ​ x ∪ R i ∪ z ​ v j ′ ∪ C j − 1, j + s ′ v_{j-1}x\cup R_{i}\cup zv^{\prime}_{j}\cup C^{\prime}_{j-1,j+s} for all 1 ≤ i ≤ ⌊ ( k − 3) / 2 ⌋ 1\leq i\leq\lfloor(k-3)/2\rfloor, together with v j + 1 ​ v j ​ v j − 1 ​ x ∪ R ⌊ ( k − 3) / 2 ⌋ ∪ z ​ v j ′ ∪ C j + 1, j + s ′ v_{j+1}v_{j}v_{j-1}x\cup R_{\lfloor(k-3)/2\rfloor}\cup zv^{\prime}_{j}\cup C^{\prime}_{j+1,j+s} and v j − 1 ​ v j ​ v j + 1 ​ x ∪ R ⌊ ( k − 3) / 2 ⌋ ∪ z ​ v j ′ ∪ C j − 1, j + s ′ v_{j-1}v_{j}v_{j+1}x\cup R_{\lfloor(k-3)/2\rfloor}\cup zv^{\prime}_{j}\cup C^{\prime}_{j-1,j+s}, are ⌊ ( k − 1) / 2 ⌋ \lfloor(k-1)/2\rfloor cycles in G G with consecutive lengths. This completes the proof of Theorem 5.2.

Now we are ready to prove Theorems 1.4 and 1.5.

Theorem 1.4. If G G is a 3-connected non-bipartite graph with minimum degree at least k + 1 k+1, then G G contains 2 ​ ⌊ k − 1 2 ⌋ 2\lfloor\frac{k-1}{2}\rfloor cycles with consecutive lengths.

Proof. It was proved by several groups (see [34, 6]) that every 3-connected non-bipartite graph contains a non-separating induced odd cycle. This, together with Theorem 5.2, immediately imply this theorem.

Theorem 1.5. If G G is a 2-connected non-bipartite graph with minimum degree at least k + 3 k+3, then G G contains k k cycles with consecutive lengths or the length condition.

Proof. If G G is 3-connected, then by Theorem 1.4, G G contains 2 ​ ⌊ ( k + 1) / 2 ⌋ ≥ k 2\lfloor(k+1)/2\rfloor\geq k cycles with consecutive lengths. Otherwise G G is 2-connected but not 3-connected, by Lemma 4.1, G G contains 2 ​ ⌊ ( k + 2) / 2 ⌋ − 1 ≥ k 2\lfloor(k+2)/2\rfloor-1\geq k cycles with the length condition.

From this result, we can prove Theorem 1.10 promptly.

Theorem 1.10. Let k k be a positive odd integer. If G G is a 2-connected non-bipartite graph with minimum degree at least k + 3 k+3, then G G contains cycles of all lengths modulo k k.

Proof. By Theorem 1.5, G G contains k k cycles with consecutive lengths or the length condition. Since k k is odd, in either case, the set of these cycle lengths intersect each of the residue classes modulo k k.

The following theorem will be used for proving Theorem 1.6.

###### Theorem 5.3.

Let G G be a 2-connected graph and v v a vertex of G G. If every vertex of G G other than v v has degree at least k + 4 k+4, then G G contains k k cycles with consecutive lengths or with the length condition.

Proof. Let G ′ = G − { v } G^{\prime}=G-\{v\}. So G ′ G^{\prime} has minimum degree at least k + 3 k+3. If G ′ G^{\prime} is bipartite, then G ′ G^{\prime} contains k + 2 k+2 cycles with the length condition by Theorem 1.2. So we may assume that G ′ G^{\prime} is non-bipartite.

If G ′ G^{\prime} is 2-connected, then by Theorem 1.5, G ′ G^{\prime} contains k k cycles with consecutive lengths or the length condition. So we may assume that G ′ G^{\prime} is not 2-connected. Note that the minimum degree of G ′ G^{\prime} is at least k + 3 k+3, so every end-block of G ′ G^{\prime} is 2-connected.

Since G G is 2-connected, G ′ G^{\prime} contains two end-blocks B 1, B 2 B_{1},B_{2} such that for each i ∈ { 1, 2 } i\in\{1,2\}, B i − b i B_{i}-b_{i} contains a vertex v i v_{i} adjacent in G G to v v, where b i b_{i} is the cut-vertex of G ′ G^{\prime} contained in B i B_{i}. By Lemma 3.1, for each i ∈ { 1, 2 } i\in\{1,2\}, B i B_{i} contains ⌊ ( k + 2) / 2 ⌋ \lfloor(k+2)/2\rfloor paths P i, 1, …, P i, ⌊ ( k + 2) / 2 ⌋ P_{i,1},...,P_{i,\lfloor(k+2)/2\rfloor} from b i b_{i} to v i v_{i} with the length condition. Let R R be a path in G ′ G^{\prime} from b 1 b_{1} to b 2 b_{2} internally disjoint from V ⁡ ( B 1) ∪ V ⁡ ( B 2) V(B_{1})\cup V(B_{2}). Then for 1 ≤ j, j ′ ≤ ⌊ ( k + 2) / 2 ⌋ 1\leq j,j^{\prime}\leq\lfloor(k+2)/2\rfloor, P 1, j ∪ R ∪ P 2, j ′ ∪ v 2 ​ v ​ v 1 P_{1,j}\cup R\cup P_{2,j^{\prime}}\cup v_{2}vv_{1} are 2 ​ ⌊ ( k + 2) / 2 ⌋ − 1 ≥ k 2\lfloor(k+2)/2\rfloor-1\geq k cycles in G G with the length condition.

Theorem 1.6. If G G is a graph with minimum degree at least k + 4 k+4, then G G contains k k cycles with consecutive lengths or the length condition.

Proof. Let B B be an end-block of G G and let b b be the cut-vertex of G G contained in B B. Every vertex of B B other than b b has minimum degree at least k + 4 k+4 and hence B B is 2-connected. By Theorem 5.3, B B (and hence G G) contains k k cycles with consecutive lengths or with the length condition.

It is straightforward to obtain Theorem 1.11 from Theorem 1.6.

Theorem 1.11. Let k k be a positive odd integer. If G G is a graph with minimum degree at least k + 4 k+4, then G G contains cycles of all lengths modulo k k.

Proof. By Theorem 1.6, G G contains k k cycles with consecutive lengths or the length condition. Since k k is odd, in either case, the set of these cycle lengths intersect each of the residue classes modulo k k.

Lastly, we derive Theorem 1.13 from Theorem 5.2.

Theorem 1.13. For every graphs G G, χ ⁡ ( G) ≤ c ⁡ ( G) + 4 \chi(G)\leq c(G)+4.

Proof. Suppose to the contrary that there exists a graph G G with χ ⁡ ( G) ≥ c ⁡ ( G) + 5 \chi(G)\geq c(G)+5. Let G ′ G^{\prime} be a χ ⁡ ( G) \chi(G) -critical subgraph of G G. Note that G ′ G^{\prime} is 2-connected and has minimum degree at least χ ⁡ ( G) − 1 ≥ c ⁡ ( G) + 4 \chi(G)-1\geq c(G)+4. A result of Krusenstjerna-Hafstrøm and Toft (see [26], Theorem 4) states that every 4-critical graph contains a non-separating induced odd cycle, but in fact their proof also works for k k -critical graph for every k ≥ 4 k\geq 4. (We direct interested readers to the original proof in [26].) Thus, G ′ G^{\prime} also contains a non-separating induced odd cycle. By Theorem 5.2, G ′ G^{\prime} contains 2 ​ ⌊ c ⁡ ( G) + 2 2 ⌋ ≥ c ⁡ ( G) + 1 2\lfloor\frac{c(G)+2}{2}\rfloor\geq c(G)+1 consecutive cycles. However, every cycle in G ′ G^{\prime} is a cycle in G ′ G^{\prime}, so c ⁡ ( G) ≥ c ⁡ ( G ′) ≥ c ⁡ ( G) + 1 c(G)\geq c(G^{\prime})\geq c(G)+1, a contradiction. This completes the proof.

## 6 Concluding remarks

In this paper, we have obtained several tight or nearly tight results on the relation between cycle lengths and minimum degree. It will be interesting if one can close the gap between our results and the best possible upper bounds, such as in Theorems 1.4 and 1.5. A good starting point may be the following strengthening of Theorem 1.3.

###### Conjecture 6.1.

If G G is a 2-connected non-bipartite graph with minimum degree at least k + 1 k+1, then G G contains ⌈ k / 2 ⌉ \lceil k/2\rceil cycles with consecutive odd lengths.

If it is true, then one can prove χ ⁡ ( G) ≤ 2 ​ c ​ o ​ ( G) + 2 \chi(G)\leq 2co(G)+2 as in Theorem 1.12.

In Theorem 1.6, we prove that every graph G G with δ ⁡ ( G) ≥ k + 4 \delta(G)\geq k+4 contains k k cycles with consecutive lengths or the length condition. The following examples show that the bound δ ⁡ ( G) ≥ k + 4 \delta(G)\geq k+4 is tight up to the constant term: the complete graph K k + 2 K_{k+2} has precisely k k cycles of consecutive lengths 3, 4, …, k + 2 3,4,...,k+2, while for every n ≥ k + 1 n\geq k+1 the complete bipartite graph K k + 1, n K_{k+1,n} has precisely k k cycles of consecutive even lengths 4, 6,.., 2 ​ k + 2 4,6,..,2k+2. All such graphs have minimum degree k + 1 k+1, and thus we conjecture that δ ⁡ ( G) ≥ k + 1 \delta(G)\geq k+1 is optimal.

###### Conjecture 6.2.

Every graph with minimum degree at least k + 1 k+1 contains k k cycles with consecutive lengths or the length condition.

If true, this would imply both Conjectures 1.7 and 1.8 when k k is odd, and thus, together with Theorems 1.9, imply these conjectures in full generality.

Our results show that if a graph G G has δ ⁡ ( G) ≥ k + 4 \delta(G)\geq k+4 (and satisfies some necessary conditions), then G G contains cycles of all lengths modulo k k. This is tight up to the constant term. However, for fixed integer m m, we know very little about the least function f ⁡ ( m, k) f(m,k) such that every graph G G with δ ⁡ ( G) ≥ f ⁡ ( m, k) \delta(G)\geq f(m,k) contains a cycle of length m m modulo k k. (If k k is even and m m is odd, then one has to restrict to 2-connected non-bipartite graphs G G here.) A conjecture of Dean (see [10]) considered the case when m = 0 m=0, which asserted that every k k -connected graph contains a cycle of length 0 0 modulo k k. Note that this (if true) is best possible for odd k k, as for every n ≥ k − 1 n\geq k-1, K k − 1, n K_{k-1,n} is ( k − 1) (k-1) -connected but has no cycles of length 0 0 modulo k k. Dean’s conjecture was confirmed for k = 3 k=3 in [9] and k = 4 k=4 in [10]. Another interesting special case is m = 3 m=3 (for the sake of convenience, let k k be odd). So f ⁡ ( 3, k) f(3,k) becomes the least function such that every triangle-free graph G G with minimum degree f ⁡ ( 3, k) f(3,k) contains a cycle of length 3 modulo k k. We speculate that f ⁡ ( 3, k) = o ⁡ ( k) f(3,k)=o(k). This may be related to the recent result of [25].

Despite much research has been done, the distribution of cycle lengths in graphs with large minimum degree is still mysterious and unclear. We conclude this paper by mentioning a conjecture of Erdő and Gyárfás [16]: every graph with minimum degree at least three contains a cycle of length a power of two.

## References

- [1] N. Alon, The largest cycle of a graph with a large minimal degree, *J. Graph Theory*10 (1986), 123–127.
- [2] B. Bollobás, Cycles modulo k, *Bull. London Math. Soc.*9 (1977), 97–98.
- [3] B. Bollobás and R. Häggkvist, The circumference of a graph with given minimal degree, *A tribute to Paul Erdős*(A. Baker, B. Bollobás and A. Hajnal eds.), Cambridge University Press 1989.
- [4] J. A. Bondy, Pancyclic graphs I, *J. Combin. Theory Ser. B*11 (1971), 80–84.
- [5] J. A. Bondy and M. Simonovits, Cycles of even length in graphs, *J. Combin. Theory Ser. B*16 (1974), 97–105.
- [6] J. A. Bondy and A. Vince, Cycles in a graph whose lengths differ by one or two, *J. Graph Theory*27 (1998), 11–15.
- [7] S. Brandt, R. Faudree, W. Goddard, Weakly pancyclic graphs, *J. Graph Theory*27 (1998), 141–176.
- [8] Z. Chen, J. Ma and W. Zang, Coloring digraphs with forbidden cycles, *J. Comb. Theory, Ser. B*, to appear. http://dx.doi.org/10.1016/j.jctb.2015.06.001
- [9] G. Chen and A. Saito, Graphs with a cycle of length divisible by three, *J. Combin. Theory Ser. B*60 (1994), 277–292.
- [10] N. Dean, L. Lesniak and A. Saito, Cycles of length 0 modulo 4 in graphs, *Discrete Math.*121 (1993), 37–49.
- [11] G. A. Dirac, Some theorems on abstract graphs, *Proc. London Math. Soc.*2 (1952), 69–81.
- [12] A. Diwan, Cycles of even lengths modulo k, *J. Graph Theory*65 (2010), 246–252.
- [13] A. Diwan, S. Kenkre and S. Vishwanathan, Circumference, chromatic number and online coloring, *Combinatorica*33 (2013), 319–334.
- [14] P. Erdős, Some recent problems and results in graph theory, combinatorics, and number theory, *Proc. Seventh S-E Conf. Combinatorics, Graph Theory and Computing, Utilitas Math.*, Winnipeg, 1976, pp. 3–14.
- [15] P. Erdős, Some of my favourite problems in various branches of combinatorics, *Matematiche (Catania)*47 (1992), 231–240.
- [16] P. Erdős, Some of my favorite solved and unsolved problems in graph theory, *Quaestiones Math.*16 (1993), 333–350.
- [17] P. Erdős, R. Faudree, A. Gyárfás and R. Schelp, Odd cycles in graphs of given minimum degree, In *Graph Theory, Combinatorics, and Applications*, Vol. 1 (Kalamazoo, MI, 1988), Wiley-Interscience Publications, Wiley, New York, 1991, pp. 407–418.
- [18] P. Erdős and A. Hajnal, On chromatic numbers of graphs and set systems, *Acta Math. Sci. Hungar.*17 (1966), 61–99.
- [19] G. Fan, Distribution of cycle lengths in graphs, *J. Combin. Theory Ser. B*84 (2002), 187–202.
- [20] A. Gyárfás, Graphs with k k odd cycle lengths, *Discrete Math.*103 (1992), 41–48.
- [21] R. Gould, P. Haxell and A. Scott, A note on cycle lengths in graphs, *Graphs Combin.*18 (2002), 491–498.
- [22] R. Häggkvist, Odd cycles of specified length in nonbipartite graphs, *Graph Theory (Cambridge, 1981)*, North-Holland Math. Stud., 62, North-Holland, Amsterdam, New York, 1982, pp. 89–99.
- [23] R. Häggkvist and A. Scott, Arithmetic progressions of cycles, *Technical Report*No. 16 (1998), Matematiska Institutionen, UmeåUniversitet.
- [24] R. Häggkvist and A. Scott, Cycles of nearly equal length in cubic graphs, Preprint.
- [25] A. Kostochka, B. Sudakov and J. Verstraëte, Cycles in triangle-free graphs of large chromatic number, Submitted. arXiv:1404.4544 [math.CO]
- [26] U.Krusenstjerna-Hafstrøm and B.Toft, Special subdivisions of K 4 K_{4} and 4-chromatic graphs, *Monatsh. Math.*89 (1980), 101–110.
- [27] J. Ma, Cycles with consecutive odd lengths, arXiv:1410.0430, submitted.
- [28] P. Mihók and I. Schiermeyer, Cycle lengths and chromatic number of graphs, *Discrete Math.*286 (2004), 147–149.
- [29] V. Nikiforov and R. Schelp, Paths and cycles in graph of large minimal degree, *J. Graph Theory*47 (2004), 39–52.
- [30] V. Nikiforov and R. Schelp, Cycle lengths in graphs with large minimum degree, *J. Graph Theory*52 (2006), 157–170.
- [31] B. Sudakov and J. Verstraëte, Cycle lengths in sparse graphs, *Combinatorica*28 (2008), 357–372.
- [32] C. Thomassen, Graph decomposition with applications to subdivisions and path systems modulo k, *J. Graph Theory*7 (1983), 261–271.
- [33] C. Thomassen, Paths, circuits and subdivisions, *Selected Topics in Graph Theory (L. Beineke and R. Wilson, eds.)*, vol. 3, Academic Press, 1988, pp. 97–131.
- [34] C. Thomassen and B. Toft, Non-separating induced cycles in graphs, *J. Combin. Theory Ser. B*31 (1981), 199–224.
- [35] J. Verstraëte, On arithmetic progressions of cycle lengths in graphs, *Combin. Probab. Comput.*9 (2000), 369–373.
- [36] H. Voss and C. Zuluaga, Maximale gerade und ungerade Kreise in Graphen I (German), *Wiss. Z. Techn. Hochsch. Ilmenau*23 (1977), 57–70.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
