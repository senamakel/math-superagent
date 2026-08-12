<!-- source: https://arxiv.org/html/2504.11656v2 | converted from HTML -->

Leaf-to-leaf paths and cycles in degree-critical graphs

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2504.11656v2 [math.CO] 04 Mar 2026

# Leaf-to-leaf paths and cycles in degree-critical graphs

Francesco Di Braccio Thanks: Department of Mathematics, London School of Economics, UK. Email: f.di-braccio@lse.ac.uk Kyriakos Katsamaktsis Thanks: Department of Mathematics, University College London, UK. Research supported by the Engineering and Physical Sciences Research Council [grant number EP/W523835/1]. Email: kyriakos.katsamaktsis.21@ucl.ac.uk Jie Ma Thanks: School of Mathematical Sciences, University of Science and Technology of China, Hefei, Anhui 230026, China, and Yau Mathematical Sciences Center, Tsinghua University, Beijing 100084, China. Research supported by National Key Research and Development Program of China 2023YFA1010201 and National Natural Science Foundation of China grant 12125106. Email: jiema@ustc.edu.cn Alexandru Malekshahian Thanks: Mathematical Institute, University of Oxford, UK. Email: alex.malekshahian@maths.ox.ac.uk. Research completed while the author was affiliated with the Department of Mathematics, King’s College London, UK. Ziyuan Zhao Thanks: School of Mathematical Sciences, University of Science and Technology of China, Hefei, Anhui 230026, China. Research supported by Innovation Program for Quantum Science and Technology 2021ZD0302902. Email: zyzhao2024@mail.ustc.edu.cn

###### Abstract

An n n -vertex graph is *degree 3-critical*if it has 2 ​ n − 2 2n-2 edges and no proper induced subgraph with minimum degree at least 3. In 1988, Erdős, Faudree, Gyárfás, and Schelp asked whether one can always find cycles of all short lengths in these graphs, which was disproven by Narins, Pokrovskiy, and Szabó through a construction based on leaf-to-leaf paths in trees whose vertices have degree either 1 or 3. They went on to suggest several weaker conjectures about cycle lengths in degree 3-critical graphs and leaf-to-leaf path lengths in these so-called 1-3 trees. We resolve three of their questions either fully or up to a constant factor. Our main results are the following:

- •

every n n -vertex degree 3-critical graph has Ω ⁡ ( log ⁡ n) \Omega(\log n) distinct cycle lengths;

- •

every tree with maximum degree Δ ≥ 3 \Delta\geq 3 and ℓ \ell leaves has at least log Δ − 1 ⁡ ( ( Δ − 2) ​ ℓ) \log_{\Delta-1}\,((\Delta-2)\ell) distinct leaf-to-leaf path lengths;

- •

for every integer N ≥ 1 N\geq 1, there exist arbitrarily large 1–3 trees which have O ⁡ ( N 0.91) O(N^{0.91}) distinct leaf-to-leaf path lengths smaller than N N, and, conversely, every 1–3 tree on at least 2 N 2^{N} vertices has Ω ⁡ ( N 2 / 3) \Omega(N^{2/3}) distinct leaf-to-leaf path lengths smaller than N N.

Several of our proofs rely on purely combinatorial means, while others exploit a connection to an additive problem that might be of independent interest.

## 1 Introduction

There is a long line of research in combinatorics seeking to understand what conditions guarantee that a graph contains cycles of many different lengths. In 1973, Bondy [5] made the famous meta-conjecture that any non-trivial condition that guarantees Hamiltonicity is enough to ensure that the n n -vertex graph is *pancyclic*, i.e. that it contains all cycle lengths in { 3, …, n } \{3,\dots,n\}. This led to a host of interesting results in the following fifty years bringing support to Bondy’s conjecture in a variety of different settings [17, 9, 5, 1, 6]. However, most of the results in the area concern (somewhat) dense graphs, and for very sparse graphs our understanding of which graphs contain many cycle lengths is more fragmentary. Sudakov and Verstraëte [22] showed that graphs with average degree d d and girth at least g g contain Ω ⁡ ( d ⌊ ( g − 1) / 2 ⌋) \Omega(d^{\lfloor(g-1)/2\rfloor}) distinct cycles lengths, thus proving a conjecture of Erdős [13]. A related conjecture of Erdős and Hajnal [13] was resolved by Gyárfás, Komlós, and Szemerédi [14], who proved that in a graph with average degree d d, the sum of the reciprocals of the distinct cycle lengths is Ω ⁡ ( log ⁡ d) \Omega(\log d).

The starting point of the present work is a conjecture of Erdős, Faudree, Gyárfás, and Schelp [10], who asked whether many cycle lengths can be found in a specific class of sparse graphs called *degree 3-critical graphs*. These are defined to be graphs with n n vertices, 2 ​ n − 2 2n-2 edges and no proper induced subgraph with minimum degree at least 3; it is not hard to see that these graphs necessarily have minimum degree 3. Degree 3-critical graphs satisfy several interesting properties; for example, they have no proper induced subgraph H H on 2 ​ | V ⁡ ( H) | − 2 2|V(H)|-2 edges, and hence, by a theorem of Nash-Williams [19], they are the union of two edge-disjoint spanning trees.

Erdős, Faudree, Gyárfás, and Schelp [10] proved that any n n -vertex degree 3-critical graph contains a cycle of length 3, 4, and 5, as well as a cycle of length at least log ⁡ n \log n. 1 1 1 Unless indicated otherwise, logarithms throughout this paper are base 2. This last bound was later improved by Bollobás and Brightwell [2] to 4 ​ log ⁡ n + O ⁡ ( log ⁡ log ⁡ n) 4\log n+O(\log\log n), which is asymptotically best possible. In an effort to reveal a rich structure of cycle lengths in such graphs, Erdős et al. [10] (also see [12]) conjectured that it should be possible to find cycle lengths 3, 4, 5 ​ …, N 3,4,5\dots,N for some N = N ⁡ ( n) → ∞ N=N(n)\to\infty as n → ∞ n\to\infty. Their conjecture, however, was disproven by Narins, Pokrovskiy, and Szabó [18] who showed that there are arbitrarily large degree 3-critical graphs with no cycle of length 23. The crucial ingredient of their construction is a particular class of trees called *1–3 trees*. A 1–3 tree is a tree where every vertex has degree either 1 or 3. It was shown in [18] that there exist infinitely many 1–3 trees with no two leaves at distance 20 20 from one another, which then yielded the desired degree 3-critical graphs by adding two vertices adjacent to all leaves and to each other.

Despite their surprising counterexamples, the authors of [18] proved that any degree 3-critical graph with at least six vertices contains a cycle of length 6, and asked whether it might still be the case that degree 3-critical graphs contain many cycle lengths. They posed the following conjecture.

###### Conjecture A (​​ [18, Conjecture 6.2]).

Every degree 3-critical graph on n n vertices contains cycles of at least 3 ​ log ⁡ n + O ⁡ ( 1) 3\log n+O(1) distinct lengths.

A classical construction of Bollobás and Brightwell [2] shows that, if true, A is best possible. Our first result proves that A is true up to a constant factor.

###### Theorem 1.

Every degree 3-critical graph on n n vertices contains cycles of at least log ⁡ n 3 + log ⁡ 3 + O ⁡ ( 1) \frac{\log n}{3+\log 3}+O(1) distinct lengths.

This provides the first bound on the number of cycle lengths as a function of n n tending to infinity, and arguably can be viewed as confirmation of the original motivation of Erdős et al. [10] to demonstrate the abundance of cycle lengths in such graphs. In fact, we establish this result as a corollary of a more general theorem (Theorem 12) which applies to *degree k k -critical graphs*for any k ≥ 3 k\geq 3, i.e., n n -vertex graphs with ( k − 1) ​ n − ( k 2) + 1 (k-1)n-\binom{k}{2}+1 edges and no proper induced subgraph with minimum degree at least k k. This family was introduced by Bollobás and Brightwell [2] as a natural generalization of degree 3-critical graphs, and a problem closely related to this family was studied more recently by Sauermann [21].

The key idea behind the proof of Theorem 1 is to define an appropriate partial ordering on the vertex set of the given graph. By Dilworth’s theorem, this either gives a long chain or a long antichain. The first case yields a long path P P together with a collection of paths that intersect P P in a special way (a structure known as a *vine*). In the second case, we find two large trees that are vertex-disjoint except for the fact that they share the same set of leaves. A careful analysis then yields many cycle lengths in either case.

Motivated by the connection between degree 3-critical graphs and 1–3 trees that they established, the authors of [18] also formulated two conjectures about leaf-to-leaf path lengths in 1–3 trees. The first of these conjectures is as follows.

###### Conjecture B (​​ [18, Conjecture 6.3], corrected version).

Every 1–3 tree T T of order n n has leaf-to-leaf paths of at least log ⁡ ( n + 2) − 1 \log(n+2)-1 distinct lengths.

Here and throughout the rest of this paper, the length of a path is equal to the number of edges of the path, and we consider a single vertex to be a path of length 0.

The original form of B in [18] asks for at least log ⁡ n \log n distinct lengths, but as stated this is false, as the following example shows. For any d ≥ 2 d\geq 2, consider the (unique) 1-3 tree T T in which, for some root r ∈ V ⁡ ( T) r\in V(T), every leaf is at distance precisely d d from r r. It is not hard to see that T T contains 3 ⋅ 2 d − 2 3\cdot 2^{d}-2 vertices but only d + 1 < log ⁡ ( 3 ⋅ 2 d − 2) d+1<\log(3\cdot 2^{d}-2) distinct leaf-to-leaf path lengths (namely, the ones in { 0, 2, 4, …, 2 ​ d } \{0,2,4,\dots,2d\}). This example also shows that B is tight whenever n = 3 ⋅ 2 d − 2 n=3\cdot 2^{d}-2 for some d ≥ 2 d\geq 2.

Our second result resolves B in a strong form. Our proof works for arbitrary trees, and gives a bound depending on the maximum degree. Consider, however, for any n > Δ ≥ 2 n>\Delta\geq 2, the tree obtained from a star S Δ S_{\Delta} by subdividing an edge n − Δ − 1 n-\Delta-1 times. This yields a tree with n n vertices and maximum degree Δ \Delta with only three distinct leaf-to-leaf path lengths, so we cannot expect to give a bound in terms of just n n and Δ \Delta. Instead, we require control over the number of *leaves*, say ℓ \ell, of the tree.

###### Theorem 2.

Let T T be a tree with maximum degree Δ ≥ 3 \Delta\geq 3 and ℓ \ell leaves. Then T T has at least log Δ − 1 ⁡ ( ( Δ − 2) ​ ℓ) \log_{\Delta-1}\,((\Delta-2)\ell) distinct leaf-to-leaf path lengths.

Theorem 2 for Δ = 3 \Delta=3 implies B since any 1–3 tree on n n vertices has precisely n + 2 2 \frac{n+2}{2} leaves. More generally, our result is tight whenever ℓ = Δ ​ ( Δ − 1) d − 1 \ell=\Delta(\Delta-1)^{d-1} for some d ≥ 2 d\geq 2, as demonstrated by the tree T T in which each vertex has degree 1 or Δ \Delta and each leaf is at distance precisely d d from some root r ∈ V ⁡ ( T) r\in V(T) (whose leaf-to-leaf path lengths are 0, 2, …, 2 ​ d 0,2,\dots,2d). In fact, noticing that T T ’s leaves can be grouped into ( Δ − 1) (\Delta-1) -tuples of sister leaves that share a neighbour, and that deleting at most ( Δ − 2) (\Delta-2) leaves in each tuple does not affect the path lengths of the tree, we may construct for each ℓ ′ > Δ ​ ( Δ − 1) d − 2 \ell^{\prime}>\Delta(\Delta-1)^{d-2} a tree T ′ T^{\prime} with maximum degree Δ \Delta and ℓ ′ \ell^{\prime} leaves and only d + 1 d+1 distinct leaf-to-leaf path lengths. This shows that Theorem 2 is tight for all values of ℓ \ell and Δ \Delta, up to an additive term of 1. The proof proceeds by finding a suitable choice of root vertex through Helly’s theorem for trees, deleting the leaves that are at a certain distance from the root, and then applying induction.

While B imposes no restrictions on the lengths considered, the final conjecture of Narins, Pokrovskiy and Szabó [18] that we address asks to determine how many *short*leaf-to-leaf path lengths can be found. They conjectured that for 1–3 trees, one can find path lengths which are dense in an interval of the form [0, N] [0,N].

###### Conjecture C (​​ [18, Conjecture 6.4]).

There exist a constant α > 0 \alpha>0 and a function N = N ⁡ ( n) N=N(n) tending to infinity as n → ∞ n\rightarrow\infty such that every 1–3 tree of order n n contains at least α ​ N \alpha N distinct leaf-to-leaf path lengths between 0 and N N.

Our next result disproves C in the following strong form, namely, with a poly-sublinear upper bound.

###### Theorem 3.

There exists an absolute constant c ∈ ( 0, 1) c\in(0,1) such that the following holds.

For all N ≥ 1 N\geq 1 and all even n ≥ N n\geq N, there exists an n n -vertex 1–3 tree with O ⁡ ( N c) O(N^{c}) distinct leaf-to-leaf path lengths between 0 and N N.

The proof of Theorem 3 yields c = ( 2 − log ⁡ 10 log ⁡ 13) − 1 ≈ 0.9073 c=\left(2-\frac{\log 10}{\log 13}\right)^{-1}\approx 0.9073. We complement this result by also providing a polynomial lower bound on the number of short lengths that may be found, which shows that we cannot take c < 2 / 3 c<2/3 in Theorem 3.

###### Theorem 4.

For all N ≥ 1 N\geq 1 and all even n ≥ 2 N / 2 n\geq 2^{N/2}, every n n -vertex 1-3 tree contains leaf-to-leaf paths of Ω ⁡ ( N 2 / 3) \Omega(N^{2/3}) distinct lengths between 0 0 and N N.

In fact, Theorem 4 is an immediate corollary of a more general statement about trees with no vertices of degree 2. Given a tree T T and a leaf v ∈ V ⁡ ( T) v\in V(T), we say that v v*witnesses*the length ℓ \ell if there is a leaf-to-leaf path of length ℓ \ell containing v v (as an endpoint).

###### Theorem 5.

For all N ≥ 1 N\geq 1 sufficiently large, both of the following statements hold.

1. (i)

Let T T be a tree containing no vertex of degree 2. If T T contains a path of length at least N / 2 N/2, then T T contains Ω ⁡ ( N 2 / 3) \Omega(N^{2/3}) leaf-to-leaf paths of distinct lengths between 0 0 and N N, all witnessed by the same leaf v ∈ V ⁡ ( T) v\in V(T).

2. (ii)

For all even n n, there exists an n n -vertex 1–3 tree in which no leaf witnesses more than O ⁡ ( N 2 / 3) O(N^{2/3}) distinct lengths between 0 and N N.

Note that the assumption that there are no vertices of degree 2 in the lower bound of Theorem 5 is necessary, as shown again by the example of a subdivided star. Since every n n -vertex 1-3 tree has diameter at least log ⁡ n − 2 \log n-2 (for instance, by Theorem 2), we see that indeed the first part of Theorem 5 implies Theorem 4.

The proof of the first part of Theorem 5 proceeds as follows: if T T contains many disjoint (rooted) subtrees in which some leaf is very close to the root, then we use the Erdős-Szekeres theorem to find a subfamily of such subtrees for which we can control the lengths of paths between leaves in distinct subtrees. If instead T T contains a subtree T ′ T^{\prime} in which every leaf is far from the root, then we find many distinct leaf-to-leaf path lengths inside of T ′ T^{\prime}.

The proofs of Theorem 3 and the second part of Theorem 5 rely on a connection to an additive combinatorics question which may be interesting in its own right. More specifically, we construct a tree T T by appending balanced binary trees of varying depths to a long path; it then turns out that the set of leaf-to-leaf path lengths in T T can be controlled by the additive structure of the sequence of subtree depths. For Theorem 3, this allows us to relate the problem to the construction of a pair of finite sets U, V ⊆ ℕ U,V\subseteq\mathbb{N} such that, for some large m ≥ 1 m\geq 1, U − V = [m] U-V=[m] and | U + V | = O ⁡ ( m β) |U+V|=O(m^{\beta}) for some suitable β ∈ ( 0, 1) \beta\in(0,1). We discuss this in more detail in the concluding remarks ( Section 5).

### 1.1 Notation

We use standard asymptotic notation and graph theory notation and terminology – see [3].

In particular, given a (simple, undirected) graph G G we write N G ​ ( v) N_{G}(v) for the neighbourhood of a vertex v v in G G, deg G ⁡ ( v) \deg_{G}(v) for the degree of v v and d G ​ ( u, v) d_{G}(u,v) for the distance between u u and v v in a graph, i.e. the number of edges of the shortest path connecting them. We will drop the subscript G G from the above notations if the graph G G is clear from context. We also write Δ ⁡ ( G) \Delta(G) for the maximum degree of G G. For U ⊆ V ⁡ ( G) U\subseteq V(G), let G ⁡ [U] G[U] be the induced subgraph of G G with the vertex set U U. For a path P P and a cycle C C in G G, we denote the length of P P (resp. C C) by ℓ ⁡ ( P) \ell(P) (resp. ℓ ⁡ ( C) \ell(C)), meaning the number of edges in P P (resp. C C).

For positive integers s, t s,t, we write ( t) s (t)_{s} for the residue of t mod s t\mod s (as an integer in { 0, 1, …, s − 1 } \{0,1,\dots,s-1\}) and also use the nonstandard notation ( t) s ∗ (t)_{s}^{*} for the same residue considered as an integer in { 1, 2, …, s } \{1,2,\dots,s\}. When s ≤ t s\leq t, define [s, t] = { i ∈ ℤ: s ≤ i ≤ t } [s,t]=\{i\in\mathbb{Z}:s\leq i\leq t\} and let [t] = [1, t] [t]=[1,t].

Given a rooted tree ( T, r) (T,r), its *layers*are the sets { v ∈ V ⁡ ( T): d ⁡ ( v, r) = i } \{v\in V(T):d(v,r)=i\} for i ≥ 0 i\geq 0. Given ℓ ≥ 1 \ell\geq 1, we call ( T, r) (T,r) a *perfect binary tree on ℓ \ell layers*if T T is a binary tree rooted at r r and every leaf v ∈ T v\in T satisfies d ⁡ ( r, v) = ℓ − 1 d(r,v)=\ell-1. We denote the set of leaves of T T by L ⁡ ( T) L(T). For u, v ∈ V ⁡ ( T) u,v\in V(T), we write T ⁡ [u, v] T[u,v] to denote the unique ( u, v) (u,v) path in T T.

We also employ a common abuse of notation by omitting floor and ceiling symbols and ignoring the rounding errors this causes whenever it is not essential for our argument; we emphasize this will only occur in the proofs of our asymptotic results and not in the case of Theorem 2.

### 1.2 Organization

The remainder of the paper is organized as follows. We prove that we can find many leaf-to-leaf path lengths in trees – Theorem 2 and the first part of Theorem 5 – in Section 2. We provide constructions of trees with a small number of distinct leaf-to-leaf path lengths – Theorem 3 and the second part of Theorem 5 – in Section 3. We prove Theorem 1 – that we can find many distinct cycle lengths in degree 3-critical graphs – in Section 4. We discuss several open problems in Section 5.

## 2 Finding many leaf-to-leaf path lengths

### 2.1 Paths of unrestricted length

In this section, we prove Theorem 2. We begin with a lemma showing how to find many lengths in a rooted tree with many leaves at the same distance from the root.

###### Lemma 6.

Let Δ ≥ 3 \Delta\geq 3 and let T T be a rooted tree with root r r and Δ ⁡ ( T) ≤ Δ \Delta(T)\leq\Delta. Assume that for some a ≥ 1 a\geq 1 there are m m distinct leaves x 1, …, x m x_{1},\dots,x_{m} such that d ⁡ ( r, x i) = a d(r,x_{i})=a for all 1 ≤ i ≤ m 1\leq i\leq m. Then there exists an i ∈ [m] i\in[m] such that T T contains leaf-to-leaf paths of at least log Δ − 1 ⁡ ( m / Δ) + 2 \log_{\Delta-1}(m/\Delta)+2 distinct lengths between 0 0 and 2 ​ a 2a, all witnessed by x i x_{i}.

###### Proof.

Denote the root’s neighbours by r 1, …, r k r_{1},\dots,r_{k} with k ≤ Δ k\leq\Delta. Deleting the root r r from T T gives k k new rooted trees T 1, … ​ T k T_{1},\dots T_{k}, with the new roots being the r i r_{i} ’s.

Case 1: deg ⁡ ( r) ≤ Δ − 1 \deg(r)\leq\Delta-1. In this case, we will prove the slightly stronger result that we can find at least log Δ − 1 ⁡ m + 1 \log_{\Delta-1}m+1 suitable lengths, all witnessed by the same x i x_{i}. We proceed by induction on the number of vertices of T T.

As a base case, note that if T T has only one vertex x 1 x_{1}, then there is precisely log Δ − 1 ⁡ ( 1) + 1 = 1 \log_{\Delta-1}(1)+1=1 leaf-to-leaf path, namely that of length 0 (witnessed by x 1 x_{1}).

For the inductive step, we distinguish two further subcases. If one of the T i T_{i} ’s contains all leaves x 1, …, x m x_{1},\dots,x_{m}, then the claim follows by the induction hypothesis applied to T i T_{i}, since the root of T i T_{i} has degree at most Δ − 1 \Delta-1. Otherwise, by relabelling if necessary, we may assume that T 1 T_{1} contains at least m / ( Δ − 1) m/(\Delta-1) of the leaves x 1, …, x m x_{1},\dots,x_{m}, and that T 2 T_{2} contains at least one leaf x j x_{j}.

Moreover, the root of T 1 T_{1} has degree at most Δ − 1 \Delta-1. By the inductive hypothesis, T 1 T_{1} contains at least log Δ − 1 ⁡ ( m / ( Δ − 1)) + 1 = log Δ − 1 ⁡ ( m) \log_{\Delta-1}(m/(\Delta-1))+1=\log_{\Delta-1}(m) distinct lengths of leaf-to-leaf paths between 0 0 and 2 ​ ( a − 1) 2(a-1), all witnessed by a some leaf x i x_{i}. Observe that the unique path from x i x_{i} to x j x_{j} has length 2 ​ a 2a. This gives log Δ − 1 ⁡ ( m) + 1 \log_{\Delta-1}(m)+1 lengths of paths between 0 0 and 2 ​ a 2a, all witnessed by x i x_{i}.

Case 2: deg ⁡ ( r) = Δ \deg(r)=\Delta. We again induct on the number of vertices of T T. If T T has Δ + 1 \Delta+1 vertices, then m = Δ m=\Delta and each leaf witnesses lengths 0 and 1, so the conclusion holds.

For the inductive step, again consider the two subcases outlined above. If one of the T i T_{i} ’s contains all m m leaves x 1, …, x m x_{1},\dots,x_{m}, then the claim follows by the inductive hypothesis applied to T i T_{i}. Otherwise, again like in Case 1 we may assume that T 1 T_{1} has at least m / Δ m/\Delta leaves from the set { x 1, …, x m } \{x_{1},\dots,x_{m}\} and T 2 T_{2} has at least one leaf x j x_{j}. Now the root of T 1 T_{1} has degree at most Δ − 1 \Delta-1, so we may use the slightly stronger bound obtained in Case 1 to find at least log Δ − 1 ⁡ ( m / Δ) + 1 \log_{\Delta-1}(m/\Delta)+1 distinct lengths between 0 0 and 2 ​ ( a − 1) 2(a-1), all witnessed by some x i x_{i}. Together with the path of length 2 ​ a 2a connecting x i x_{i} to x j x_{j}, we obtain at least log Δ − 1 ⁡ ( m / Δ) + 2 \log_{\Delta-1}(m/\Delta)+2 lengths of paths between 0 0 and 2 ​ a 2a, all witnessed by x i x_{i}. ∎

Our proof of Theorem 2 proceeds by induction on the number of leaves in the tree T T. After choosing a root appropriately, we either find many leaves at the same distance from it (and thus Lemma 6 applies), or instead find a subtree T ′ T^{\prime} with strictly smaller diameter but still having many leaves of T T (to which the inductive hypothesis applies). For the choice of root, we need the following well-known Helly-type lemma for trees (see, for instance, [15] or [16]).

###### Lemma 7.

Let T T be a tree and T 1, …, T s T_{1},\ldots,T_{s} be a collection of subtrees of T T such that V ⁡ ( T i) ∩ V ⁡ ( T j) ≠ ∅ V(T_{i})\cap V(T_{j})\neq\emptyset for all 1 ≤ i < j ≤ s 1\leq i<j\leq s. Then ∩ i = 1 s V ( T i) ≠ ∅ \cap_{i=1}^{s}V(T_{i})\neq\emptyset.

We are now ready to prove the main result of this section.

###### Proof of Theorem 2.

The proof is by induction on | L ⁡ ( T) | |L(T)|. Note that the statement is trivial when | L ⁡ ( T) | = 1 |L(T)|=1, since there is one path length (namely zero), and when | L ⁡ ( T) | ∈ [2, Δ] |L(T)|\in[2,\Delta], since there are at least two path lengths in T T and log Δ − 1 ⁡ ( Δ ⁡ ( Δ − 2)) ≤ 2 \log_{\Delta-1}(\Delta(\Delta-2))\leq 2. Assume that the statement is true for all ℓ ′ < ℓ \ell^{\prime}<\ell and consider a tree T T with ℓ \ell leaves. It is not hard to see that any two longest paths in T T share a vertex and thus Lemma 7 implies there is a vertex v v which is contained in every longest path. Moreover, we may assume without loss of generality that v v is not a leaf, since otherwise its neighbour also satisfies this condition. Let m m be the length of the longest path in T T. We consider two cases.

Case 1: There is some leaf x x with d ⁡ ( x, v) > m / 2 d(x,v)>m/2.

Firstly, take a leaf x x that maximizes d ⁡ ( x, v) d(x,v). Let e = v ​ u e=vu be the edge incident to v v on T ⁡ [v, x] T[v,x]. Note that every leaf y y that is connected to v v by a path not containing e e satisfies d ⁡ ( y, v) ≤ m − d ⁡ ( x, v) < m / 2 d(y,v)\leq m-d(x,v)<m/2, as otherwise T ⁡ [x, y] = T ⁡ [x, v] ∪ T ⁡ [v, y] T[x,y]=T[x,v]\cup T[v,y] would be a path of length greater than m m. Moreover, since every longest path in T T passes through v v, there must exist some leaf y y satisfying e ∉ T ⁡ [y, v] e\notin T[y,v] and d ⁡ ( y, v) = m − d ⁡ ( v, x) d(y,v)=m-d(v,x). It follows that every longest path in T T is formed by concatenating a path of length d ⁡ ( x, v) d(x,v) from a leaf to v v (passing through e e) together with a path of length m − d ⁡ ( x, v) m-d(x,v) from v v to another leaf (avoiding e e).

Now, let X 1 X_{1} be the set of leaves whose distance from v v is equal to d ⁡ ( x, v) d(x,v) and let X 2 X_{2} be the set of leaves whose distance from v v is equal to m − d ⁡ ( x, v) m-d(x,v). X 1 X_{1} and X 2 X_{2} are clearly disjoint, and by the above, every longest path in T T goes from a vertex in X 1 X_{1} to a vertex in X 2 X_{2}.

By relabelling if necessary, we may assume that | X 1 | ≤ | X 2 | |X_{1}|\leq|X_{2}|. Let L = L ⁡ ( T) L=L(T) be the set of leaves in T T, and observe that | L ∖ X 1 | ≥ ℓ / 2 |L\setminus X_{1}|\geq\ell/2. We define T ′ T^{\prime} to be the smallest subtree of T T such that L ∖ X 1 ⊆ V ⁡ ( T ′) L\setminus X_{1}\subseteq V(T^{\prime}), and claim that L ⁡ ( T ′) = L ∖ X 1 L(T^{\prime})=L\setminus X_{1}. Indeed, if T ′ T^{\prime} contained some other leaf u ∉ L ∖ X 1 u\notin L\setminus X_{1}, then T ′ − u T^{\prime}-u would still be connected and we would have L ∖ X 1 ⊆ V ⁡ ( T ′ − u) L\setminus X_{1}\subseteq V(T^{\prime}-u), a contradiction. Thus, L ⁡ ( T ′) = L ∖ X 1 ⊆ L ⁡ ( T) L(T^{\prime})=L\setminus X_{1}\subseteq L(T), which implies that leaf-to-leaf paths in T ′ T^{\prime} are also leaf-to-leaf paths in T T. Crucially, V ⁡ ( T ′) ∩ X 1 = ∅ V(T^{\prime})\cap X_{1}=\emptyset and thus the longest path in T ′ T^{\prime} is of length strictly less than m m.

By the induction hypothesis, T ′ T^{\prime} contains leaf-to-leaf paths of at least

 | log Δ − 1 ⁡ ( ℓ / 2) + log Δ − 1 ⁡ ( Δ − 2) ≥ log Δ − 1 ⁡ ℓ + log Δ − 1 ⁡ ( Δ − 2) − 1 \log_{\Delta-1}(\ell/2)+\log_{\Delta-1}(\Delta-2)\geq\log_{\Delta-1}\ell+\log_{\Delta-1}(\Delta-2)-1 |  |

distinct lengths, all strictly smaller than m m. Together with the length m m, we conclude that T T contains at least log Δ − 1 ⁡ ℓ + log Δ − 1 ⁡ ( Δ − 2) \log_{\Delta-1}\ell+\log_{\Delta-1}(\Delta-2) distinct leaf-to-leaf path lengths.

Case 2: The furthest leaf x x from v v satisfies d ⁡ ( x, v) = m / 2 d(x,v)=m/2.

In this case, every longest path is obtained by concatenating two internally vertex-disjoint paths of length m / 2 m/2 from v v to different leaves. Let X X be the set of leaves of T T which are at distance precisely m / 2 m/2 from v v. Now we split into two further subcases.

Case 2.1: | X | < ( 1 − ( Δ − 1) − 2) ​ ℓ |X|<(1-(\Delta-1)^{-2})\ell. Consider the collection of subtrees of T T obtained by deleting the vertex v v, and let T ¯ \overline{T} be one which contains at least | X | / Δ |X|/\Delta elements of X X.

Define X ′ = X ∖ V ⁡ ( T ¯) X^{\prime}=X\setminus V(\overline{T}), so that | X ′ | ≤ ( 1 − Δ − 1) ​ | X | |X^{\prime}|\leq(1-\Delta^{-1})|X|. Recalling that L L is the set of leaves of T T and | L | = ℓ |L|=\ell, we define T ′ T^{\prime} to be the smallest subtree of T T such that L ∖ X ′ ⊆ V ⁡ ( T ′) L\setminus X^{\prime}\subseteq V(T^{\prime}). Using the same argument as in Case 1, it is easy to see that L ⁡ ( T ′) = L ∖ X ′ L(T^{\prime})=L\setminus X^{\prime}. Hence we have

 | | L ∖ L ⁡ ( T ′) | = | X ′ | ≤ Δ − 1 Δ ​ | X | ≤ ( 1 − 1 Δ − 1 Δ ⁡ ( Δ − 1)) ​ ℓ = ( 1 − 1 / ( Δ − 1)) ​ ℓ. |L\setminus L(T^{\prime})|=|X^{\prime}|\leq\frac{\Delta-1}{\Delta}|X|\leq\left(1-\frac{1}{\Delta}-\frac{1}{\Delta(\Delta-1)}\right)\ell=(1-1/(\Delta-1))\ell. |  |

Thus, T ′ T^{\prime} has maximum degree at most Δ \Delta, at least ℓ / ( Δ − 1) \ell/(\Delta-1) leaves and by construction the longest path in T ′ T^{\prime} is strictly shorter than m m in length. Indeed, given a longest path, it has leaves u 1 u_{1} and u 2 u_{2}, say, as endpoints. Supposing this path has length m m, by the assumption of Case 2 above we know that d ⁡ ( v, u 1) = d ⁡ ( v, u 2) = m / 2 d(v,u_{1})=d(v,u_{2})=m/2, and so u 1, u 2 ∈ X ∖ X ′ u_{1},u_{2}\in X\setminus X^{\prime}. But then both u 1 u_{1} and u 2 u_{2} belong to the subtree T ¯ \overline{T}, and hence the path connecting them doesn’t pass through v v, contradiction.

Thus, by the induction hypothesis, the leaf-to-leaf paths in T ′ T^{\prime} have at least log Δ − 1 ⁡ ( ( Δ − 2) ​ ℓ) − 1 \log_{\Delta-1}((\Delta-2)\ell)-1 many distinct lengths, and all of these also occur in T T. Together with a leaf-to-leaf path of length m m in T T, we get the required bound.

Case 2.2: | X | ≥ ( 1 − ( Δ − 1) − 2) ​ ℓ |X|\geq(1-(\Delta-1)^{-2})\ell. Then, it follows by applying Lemma 6 to T T rooted at v v that there are at least

 | log Δ − 1 ⁡ ( ( 1 − ( Δ − 1) − 2) ​ ℓ Δ) + 2 = log Δ − 1 ⁡ ( ( Δ − 2) ​ ℓ) \log_{\Delta-1}\left(\frac{(1-(\Delta-1)^{-2})\ell}{\Delta}\right)+2=\log_{\Delta-1}((\Delta-2)\ell) |  |

distinct leaf-to-leaf path lengths, as required. ∎

### 2.2 Paths of restricted length

The aim of this section is to prove the lower bound of Theorem 5, which guarantees many lengths of short leaf-to-leaf paths in trees with not-too-small diameter and no vertices of degree 2.

We will consider a path of maximum length in T T and look at its initial segment P P of length N / 2 N/2. Each vertex v v in P P has a subtree hanging from it (which we root at v v). We will split into two cases depending on the minimum root-to-leaf distance in each of these subtrees. If one of them is very deep, we will be able to find many short leaf-to-leaf paths inside of it; this is inspired by the approach of [18]. Otherwise, all of the subtrees have shallow leaves and we will travel along P P to find many paths of distinct lengths connecting them.

We will require the following classical result.

###### Theorem 8 (Erdős-Szekeres [11]).

Any sequence of n n not necessarily distinct real numbers contains a monotone subsequence of length at least n \sqrt{n}.

We use Theorem 8 to prove the following lemma, which will be useful for proving Theorem 5*(i)*.

###### Lemma 9.

Let ( a 1, …, a n) (a_{1},\dots,a_{n}) be a sequence of non-negative real numbers such that a i ≤ m a_{i}\leq m for each 1 ≤ i ≤ n 1\leq i\leq n and some m > 0 m>0. Then

 | max ⁡ { | { a i + i: 1 ≤ i ≤ n } |, | { a i − i: 1 ≤ i ≤ n } | } ≥ n 4 ​ m. \max\bigg\{\big|\{a_{i}+i:1\leq i\leq n\}\big|,\big|\{a_{i}-i:1\leq i\leq n\}\big|\bigg\}\geq\frac{n}{4\sqrt{m}}. |  |

###### Proof.

First, suppose that m ≤ n / 2 m\leq n/2. For each 1 ≤ i ≤ n / ( 2 ​ m) 1\leq i\leq n/(2m), set A i ≔ ( a j) j = 2 ​ ( i − 1) ​ m + 1 ( 2 ​ i − 1) ​ m A_{i}\coloneqq(a_{j})_{j=2(i-1)m+1}^{(2i-1)m}. Theorem 8 implies that each sequence A i A_{i} contains a monotone subsequence of length at least m \sqrt{m}. Let B i B_{i} be the set of indices of this subsequence, so that | B i | ≥ m |B_{i}|\geq\sqrt{m} and B i ⊆ [2 ​ ( i − 1) ​ m + 1, ( 2 ​ i − 1) ​ m] B_{i}\subseteq[2(i-1)m+1,(2i-1)m].

Let X X be the set of indices 1 ≤ k ≤ n 2 ​ m 1\leq k\leq\frac{n}{2m} for which ( a i) i ∈ B k (a_{i})_{i\in B_{k}} is an increasing sequence, and set Y ≔ [n 2 ​ m] ∖ X Y\coloneqq\left[\frac{n}{2m}\right]\setminus X. Suppose | X | ≥ n 4 ​ m |X|\geq\frac{n}{4m}. For each k ∈ X k\in X and i, j ∈ B k i,j\in B_{k} with i < j i<j, we have a i + i < a j + j a_{i}+i<a_{j}+j, so the set A k ′ = { a i + i: i ∈ B k } A_{k}^{\prime}=\{a_{i}+i:i\in B_{k}\} consists of | B k | ≥ m |B_{k}|\geq\sqrt{m} distinct elements. Moreover, given integers 1 ≤ k 1 < k 2 ≤ n 2 ​ m 1\leq k_{1}<k_{2}\leq\frac{n}{2m}, for any i 1 ∈ B k 1 i_{1}\in B_{k_{1}} and i 2 ∈ B k 2 i_{2}\in B_{k_{2}} we have

 | a i 1 + i 1 ≤ m + ( 2 ​ k 1 − 1) ​ m = 2 ​ k 1 ​ m, a_{i_{1}}+i_{1}\leq m+(2k_{1}-1)m=2k_{1}m, |  |

and

 | a i 2 + i 2 ≥ 0 + 2 ​ ( k 2 − 1) ​ m + 1 ≥ 2 ​ k 1 ​ m + 1, a_{i_{2}}+i_{2}\geq 0+2(k_{2}-1)m+1\geq 2k_{1}m+1, |  |

so the sets A k ′ A_{k}^{\prime} are pairwise disjoint. We conclude that

 | | { a i + i: 1 ≤ i ≤ n } | ≥ ∑ k ∈ X | A k ′ | ≥ n 4 ​ m ⋅ m = n 4 ​ m. |\{a_{i}+i:1\leq i\leq n\}|\geq\sum_{k\in X}|A_{k}^{\prime}|\geq\frac{n}{4m}\cdot\sqrt{m}=\frac{n}{4\sqrt{m}}. |  |

If instead we have | X | < n 4 ​ m |X|<\frac{n}{4m}, then | Y | ≥ n 4 ​ m |Y|\geq\frac{n}{4m}, and for every k ∈ Y k\in Y, ( a i) i ∈ B k (a_{i})_{i\in B_{k}} is a decreasing subsequence. An analogous argument shows that in this case | { a i − i: 1 ≤ i ≤ n } | ≥ n 4 ​ m |\{a_{i}-i:1\leq i\leq n\}|\geq\frac{n}{4\sqrt{m}}.

If m > n / 2 m>n/2, Theorem 8 guarantees that the sequence ( a i) i = 1 n (a_{i})_{i=1}^{n} has a monotone subsequence of length at least n \sqrt{n}. If this sequence is increasing, then | { a i + i: 1 ≤ i ≤ n } | ≥ n |\{a_{i}+i:1\leq i\leq n\}|\geq\sqrt{n}, while if the sequence is decreasing, then | { a i − i: 1 ≤ i ≤ n } | ≥ n |\{a_{i}-i:1\leq i\leq n\}|\geq\sqrt{n}, and note that both quantities are at least n 4 ​ m \frac{n}{4\sqrt{m}}, as required. ∎

###### Proof of Theorem 5 (i).

We can assume that N N is an even integer. Let P = v 0 ​ v 1 ​ … ​ v M P=v_{0}v_{1}\dots v_{M} be a path of maximum length in T T and let P ′ = v 0 ​ v 1 ​ … ​ v N / 2 P^{\prime}=v_{0}v_{1}\dots v_{N/2} be its initial segment of length N / 2 N/2. For each 1 ≤ i ≤ N / 2 1\leq i\leq N/2, let T i T_{i} be the connected component of T ∖ E ⁡ ( P) T\setminus E(P) that contains v i v_{i}.

Observe that for every 1 ≤ i ≤ N / 2 1\leq i\leq N/2 and every leaf x ∈ T i ∖ { v i } x\in T_{i}\setminus\{v_{i}\}, we must have d ⁡ ( x, v i) ≤ N / 2 d(x,v_{i})\leq N/2, as otherwise we would have d ⁡ ( x, v M) > M d(x,v_{M})>M, a contradiction.

Case 1: There exists some 1 ≤ i ≤ N / 2 1\leq i\leq N/2 such that for every leaf x ∈ T i ∖ { v i } x\in T_{i}\setminus\{v_{i}\}, we have d ⁡ ( x, v i) > N 2 / 3 / 2 d(x,v_{i})>N^{2/3}/2. Then v i v_{i} has a neighbour u i ∈ V ⁡ ( T i) u_{i}\in V(T_{i}) which is not a leaf and hence has degree at least 3 in T i T_{i}. Let T ′ T^{\prime} be a maximal binary subtree of T i − v i T_{i}-v_{i} rooted at u i u_{i}, and note that every leaf of T ′ T^{\prime} is also a leaf of T T. Every leaf of T ′ T^{\prime} is at distance at least N 2 / 3 / 2 − 1 N^{2/3}/2-1 from u i u_{i}. Together with the fact that each non-leaf vertex in T ′ T^{\prime} has two children, this implies that T ′ T^{\prime} contains at least 2 N 2 / 3 / 2 − 1 2^{N^{2/3}/2-1} leaves. As established above, each of these leaves is at distance at most N / 2 N/2 from v i v_{i}. Thus, there exists some 1 ≤ d ≤ N / 2 1\leq d\leq N/2 for which at least 2 N 2 / 3 / 2 / N ≥ 2 N 2 / 3 / 3 2^{N^{2/3}/2}/N\geq 2^{N^{2/3}/3} distinct leaves in T i T_{i} are all at distance precisely d d from v i v_{i}. By Lemma 6 we can then find a leaf x ∈ T i x\in T_{i} witnessing at least log ⁡ ( 2 N 2 / 3 / 3 / 3) + 2 ≥ N 2 / 3 / 3 \log(2^{N^{2/3}/3}/3)+2\geq N^{2/3}/3 distinct leaf-to-leaf path lengths in T T, and all of these lengths are at most equal to 2 ​ d ≤ N 2d\leq N.

Case 2: For every 1 ≤ i ≤ N / 2 1\leq i\leq N/2 there exists a leaf x i ∈ T i x_{i}\in T_{i}, x i ≠ v i x_{i}\neq v_{i}, such that a i ≔ d ⁡ ( x i, v i) ≤ N 2 / 3 / 2 a_{i}\coloneqq d(x_{i},v_{i})\leq N^{2/3}/2.

Observe that the set of path lengths connecting pairs in { x 1, …, x N / 2 } \{x_{1},\dots,x_{N/2}\} is precisely

 | X = { a i + a j + j − i: 1 ≤ i < j ≤ N / 2 }. X=\{a_{i}+a_{j}+j-i:1\leq i<j\leq N/2\}. |  |

Moreover, any ( x i, x j) (x_{i},x_{j}) -path has length at most N / 2 + N 2 / 3 ≤ N N/2+N^{2/3}\leq N. By applying Lemma 9 with m = N 2 / 3 / 2 m=N^{2/3}/2, we see that

 | max ⁡ ( | { a i + i: 1 ≤ i ≤ N / 2 } |, | { a i − i: 1 ≤ i ≤ N / 2 } |) ≥ N 2 / 3 4 ​ 2. \max\left(\big|\{a_{i}+i:1\leq i\leq N/2\}\big|,\big|\{a_{i}-i:1\leq i\leq N/2\}\big|\right)\geq\frac{N^{2/3}}{4\sqrt{2}}. |  |

If the inequality holds for { a i + i: 1 ≤ i ≤ N / 2 } \{a_{i}+i:1\leq i\leq N/2\}, then

 | | X | ≥ | { a 1 − 1 + ( a i + i): 2 ≤ i ≤ N / 2 } | ≥ N 2 / 3 / 6, |X|\geq|\{a_{1}-1+(a_{i}+i):2\leq i\leq N/2\}|\geq N^{2/3}/6, |  |

with N 2 / 3 / 6 N^{2/3}/6 distinct lengths being witnessed by x 1 x_{1}. If it holds for { a i − i: 1 ≤ i ≤ N / 2 } \{a_{i}-i:1\leq i\leq N/2\}, then

 | | X | ≥ | { a N / 2 + ( N / 2) + ( a i − i): 1 ≤ i ≤ ( N / 2) − 1 } | ≥ N 2 / 3 / 6, |X|\geq|\{a_{N/2}+(N/2)+(a_{i}-i):1\leq i\leq(N/2)-1\}|\geq N^{2/3}/6, |  |

with x N / 2 x_{N/2} witnessing all these lengths, as desired.∎

## 3 Trees with few leaf-to-leaf path lengths

In this section we prove Theorem 3 and the second part of Theorem 5. Each result is obtained by taking a sequence ( a i) (a_{i}) with a suitable additive structure and constructing an n n -vertex tree T n ​ ( ( a i)) T_{n}((a_{i})) from it. We first describe the general construction, and then provide a suitable choice of ( a i) (a_{i}) for each of the two results.

### 3.1 The general construction

Let n ≥ 4 n\geq 4 be even. Let m ∈ ℕ m\in\mathbb{N} and consider a positive integer sequence ( a i) i = 1 m (a_{i})_{i=1}^{m}. We will now describe a general construction of an n n -vertex 1–3 tree T n ​ ( ( a i)) T_{n}((a_{i})) based on this sequence. For the most part, our construction consists of a path together with a collection of perfect binary trees attached to the path’s internal vertices, with the sequence ( a i) (a_{i}) dictating the depths of the perfect trees.

Consider the periodic sequence ( a i ′) i ≥ 1 (a^{\prime}_{i})_{i\geq 1} given by

 | a 1, …, a m, a 1, …, a m, a 1, …, a_{1},\dots,a_{m},a_{1},\dots,a_{m},a_{1},\dots, |  |

and take its shortest initial segment ( a 1 ′, …, a t ′) (a^{\prime}_{1},\dots,a^{\prime}_{t}) with the property that S ≔ 2 + ∑ i = 1 t 2 a i ′ ≥ n S\coloneqq 2+\sum_{i=1}^{t}2^{a^{\prime}_{i}}\geq n. Note that t ≥ 1 t\geq 1. Based on our choice of t t and the fact that n n and S S are even, it must be the case that S − 2 a t ′ ≤ n − 2 S-2^{a^{\prime}_{t}}\leq n-2.

We will now describe how to construct T n ​ ( ( a i)) T_{n}((a_{i})). We start with a path P = v 0 ​ v 1 ​ … ​ v t + 1 P=v_{0}v_{1}\dots v_{t+1}. For each i ∈ [t − 1] i\in[t-1], we take a perfect binary tree ( T i, r i) (T_{i},r_{i}) on a i ′ a^{\prime}_{i} layers, and add an edge from v i v_{i} to r i r_{i}. Thus far, every vertex in the tree other than v t v_{t} has degree either 1 or 3 and the total number of vertices is

 | t + 2 + ∑ i = 1 t − 1 ( 2 a i ′ − 1) = S − 2 a t ′ + 1 ≤ n − 1. t+2+\sum_{i=1}^{t-1}(2^{a^{\prime}_{i}}-1)=S-2^{a_{t}^{\prime}}+1\leq n-1. |  |

Let L = n − ( S − 2 a t ′ + 1) ≥ 1 L=n-(S-2^{a^{\prime}_{t}}+1)\geq 1, which must be odd since n n and S S are even. Since S ≥ n S\geq n, we have that L ≤ 2 a t ′ − 1 L\leq 2^{a^{\prime}_{t}}-1. We take a perfect binary tree ( T ~, r t) (\tilde{T},r_{t}) on ⌈ log ⁡ ( L + 1) ⌉ ≤ a t ′ \lceil\log(L+1)\rceil\leq a^{\prime}_{t} layers. With this choice, we have L ≤ | V ⁡ ( T ~) | < 2 ​ L L\leq|V(\tilde{T})|<2L. We now proceed to iteratively delete pairs of leaves sharing a parent from the lowest layer of T ~ \tilde{T}, until we obtain a tree T t T_{t} which has precisely L L vertices (which is possible since both L L and | V ⁡ ( T ~) | |V(\tilde{T})| are odd). By removing pairs of leaves which share a parent, and always from the lowest layer, we guarantee that the resulting T t T_{t} is still a binary tree, with its leaves spanning at most two layers. Adding an edge from r t r_{t} to v t v_{t} then completes the construction of T n ​ ( ( a i)) T_{n}((a_{i})). Observe that for any two leaves x i ∈ T i x_{i}\in T_{i}, x j ∈ T j x_{j}\in T_{j} with i ≠ j i\neq j, the unique path from x i x_{i} to x j x_{j} consists of the path inside T i T_{i} from x i x_{i} to r i r_{i}, the edge r i ​ v i r_{i}v_{i}, the path from v i v_{i} to v j v_{j} in P P, the edge v j ​ r j v_{j}r_{j} and finally the path from r j r_{j} to x j x_{j}; cf. Figure 1.

v 0 v_{0} v t + 1 v_{t+1} v 1 v_{1} v t v_{t} r t r_{t} P P v 1 v_{1} a 1 a_{1} r 1 r_{1} T 1 T_{1} v 2 v_{2} a 2 a_{2} r 2 r_{2} T 2 T_{2} … \dots v m v_{m} a m a_{m} r m r_{m} T m T_{m} v m + 1 v_{m+1} a 1 a_{1} r m + 1 r_{m+1} T m + 1 T_{m+1} … \dots v 2 ​ m v_{2m} a m a_{m} r 2 ​ m r_{2m} T 2 ​ m T_{2m} … \dots T t T_{t} Figure 1: The construction of the tree T n ​ ( ( a i)) T_{n}((a_{i})). Each subtree T i + m ​ j T_{i+mj} for j ≥ 1 j\geq 1, except T t T_{t}, represents a perfect binary tree on a i a_{i} layers, whose root neighbours the corresponding vertex on the horizontal path P P. Note that this pattern repeats cyclically every m m steps. To the vertex v t v_{t}, we instead append the specific tree T t T_{t}, as described in the context.

### 3.2 Upper bound on path lengths in [N] [N]

For a set U ⊆ ℤ U\subseteq\mathbb{Z} and k ∈ ℤ k\in\mathbb{Z}, let k ⋅ U ≔ { k ​ u: u ∈ U } k\cdot U\coloneqq\{ku:u\in U\} and k + U = U + k ≔ { u + k: u ∈ U } k+U=U+k\coloneqq\{u+k:u\in U\}.

###### Proposition 10.

Suppose that there exist a positive integer m m, sets U, V ⊆ ℤ U,V\subseteq\mathbb{Z} and a real β ∈ ( 0, 1) \beta\in(0,1) that satisfy the following:

1. 1.

U + V ⊆ [m] ⊆ U − V U+V\subseteq[m]\subseteq U-V; and

2. 2.

| U + V | = m β \left|U+V\right|=m^{\beta}.

Let M = ⌊ m 2 − β ⌋ M=\lfloor m^{2-\beta}\rfloor and n ≥ M n\geq M even. If m 1 − β ≥ 4 m^{1-\beta}\geq 4, then there exists a 1–3 tree T T on n n vertices such that the number of distinct leaf-to-leaf path lengths in [M] [M] is at most 26 ​ M 1 2 − β 26M^{\frac{1}{2-\beta}}.

###### Proof.

Since U − V = [m] U-V=[m], we can find a sequence of pairs ( u i, v i) i = 1 m (u_{i},v_{i})_{i=1}^{m} such that i = u i − v i i=u_{i}-v_{i}. Consider the sequence ( a i) i = 1 m (a_{i})_{i=1}^{m}, defined by a i = u i + v i a_{i}=u_{i}+v_{i}. Let T T be the tree T n ​ ( ( a i)) T_{n}((a_{i})) as defined in Section 3.1.

We proceed to count the number of leaf-to-leaf path lengths at most M M in T T. We will prove that there are at most 13 ​ m 13m such paths, which suffices to prove the proposition since

 | M 1 2 − β ≥ ( m 2 − β − 1) 1 2 − β ≥ m 2 1 2 − β ≥ m 2, M^{\frac{1}{2-\beta}}\geq(m^{2-\beta}-1)^{\frac{1}{2-\beta}}\geq\frac{m}{2^{\frac{1}{2-\beta}}}\geq\frac{m}{2}, |  |

where we used m 1 − β ≥ 4 m^{1-\beta}\geq 4 in the second inequality.

First note that, for two leaves u u and v v belonging to the same subtree T i T_{i}, say, we must have d ⁡ ( u, v) ≤ 2 ​ m d(u,v)\leq 2m. It therefore suffices to show that there are at most 11 ​ m 11m lengths arising when we consider leaves belonging to different subtrees, say u ∈ T i u\in T_{i} and v ∈ T j v\in T_{j} with 1 ≤ i < j ≤ t 1\leq i<j\leq t and d ⁡ ( u, v) ≤ M d(u,v)\leq M, or when u = v 0 u=v_{0} or v = v t + 1 v=v_{t+1}.

Recall that we write ( i) m ∗ (i)_{m}^{*} for the integer in { 1, 2, … ​ m } \{1,2,\dots m\} congruent to i mod m i\mod m. Write i = ( i) m ∗ + ℓ i ⋅ m i=(i)_{m}^{*}+\ell_{i}\cdot m, and j = ( j) m ∗ + ℓ j ⋅ m j=(j)_{m}^{*}+\ell_{j}\cdot m.

Case 1. If u ≠ v 0, v ≠ v t + 1 u\neq v_{0},v\neq v_{t+1} and j ≠ t j\neq t, then d ⁡ ( u, v) d(u,v) is precisely equal to

 | a ( i) m ∗ + j − i + a ( j) m ∗ = a ( i) m ∗ + ( j) m ∗ − ( i) m ∗ + a ( j) m ∗ + ( ℓ j − ℓ i) ​ m = 2 ​ u ( j) m ∗ + 2 ​ v ( i) m ∗ + ( ℓ j − ℓ i) ​ m, a_{(i)_{m}^{*}}+j-i+a_{(j)_{m}^{*}}=a_{(i)_{m}^{*}}+(j)_{m}^{*}-(i)_{m}^{*}+a_{(j)_{m}^{*}}+(\ell_{j}-\ell_{i})m=2u_{(j)_{m}^{*}}+2v_{(i)_{m}^{*}}+(\ell_{j}-\ell_{i})m, |  |

where we have used the fact that a i + i = 2 ​ u i a_{i}+i=2u_{i} and a i − i = 2 ​ v i a_{i}-i=2v_{i} for all i i. Since d ⁡ ( u, v) ∈ [M] d(u,v)\in[M], we must have 0 ≤ ℓ j − ℓ i ≤ ⌈ M / m ⌉ 0\leq\ell_{j}-\ell_{i}\leq\lceil M/m\rceil and thus

 | d ⁡ ( u, v) ∈ 2 ⋅ ( U + V) + m ⋅ { 0, …, ⌈ M / m ⌉ } ≕ A. d(u,v)\in 2\cdot(U+V)+m\cdot\{0,\dots,\lceil M/m\rceil\}\eqqcolon A. |  |

But note that | A | ≤ | U + V | ⋅ ( 2 ​ M / m) ≤ 2 ​ m |A|\leq|U+V|\cdot(2M/m)\leq 2m, so there are at most 2 ​ m 2m distances we can find in this case.

Case 2. If u ≠ v 0 u\neq v_{0} and j = t j=t, then let c ∈ ℕ c\in\mathbb{N} be such that the leaves in T t T_{t} are all at distance either a ( t) m ∗ − c a_{(t)_{m}^{*}}-c or a ( t) m ∗ − c − 1 a_{(t)_{m}^{*}}-c-1 from the root.

We then have that d ⁡ ( u, v) d(u,v) is precisely either

 | a ( t) m ∗ − c + t − i + a ( i) m ∗ a_{(t)_{m}^{*}}-c+t-i+a_{(i)_{m}^{*}} |  |

or

 | a ( t) m ∗ − c − 1 + t − i + a ( i) m ∗, a_{(t)_{m}^{*}}-c-1+t-i+a_{(i)_{m}^{*}}, |  |

i.e. we have d ⁡ ( u, v) ∈ ( A − c) ∪ ( A − c − 1) d(u,v)\in(A-c)\cup(A-c-1), and so we obtain at most 4 ​ m 4m distances in this case.

Case 3. If u = v 0 u=v_{0}, then the cases of v = v t + 1 v=v_{t+1} or j = t j=t provide at most three new distances. If we instead have j ≠ t j\neq t, then j ≤ M j\leq M since d ⁡ ( u, v) ≤ M d(u,v)\leq M, and so 0 ≤ ℓ j ≤ ⌈ M / m ⌉ 0\leq\ell_{j}\leq\lceil M/m\rceil. Thus,

 | d ⁡ ( u, v) = a ( j) m ∗ + j + 1 = 2 ​ u ( j) m ∗ + 1 + ℓ j ​ m ∈ 2 ⋅ U + 1 + m ⋅ { 0, 1, …, ⌈ M / m ⌉ } d(u,v)=a_{(j)_{m}^{*}}+j+1=2u_{(j)_{m}^{*}}+1+\ell_{j}m\in 2\cdot U+1+m\cdot\{0,1,\dots,\lceil M/m\rceil\} |  |

which is a set of size at most | U + V | ⋅ 2 ​ M / m ≤ 2 ​ m |U+V|\cdot 2M/m\leq 2m.

Case 4. If v = v t + 1 v=v_{t+1}, then the case i = t i=t provides at most two new distances. Assuming that u ≠ v 0 u\neq v_{0} and i ≠ t i\neq t, we have that i ≥ ( t + 1) − M i\geq(t+1)-M since d ⁡ ( u, v) ≤ M d(u,v)\leq M, and by proceeding similarly to the previous case we have again at most 2 ​ m 2m new distances.

Putting everything together, we see that indeed d ⁡ ( u, v) d(u,v) can take at most 10 ​ m + 5 ≤ 11 ​ m 10m+5\leq 11m distinct values when u u and v v do not lie in the same subtree, which completes the proof. ∎

###### Proof of Theorem 3.

Given N N in the statement of the theorem, it is clear that we may assume n > 20 ​ N n>20N, say, as for smaller n n the conclusion follows by considering the almost-perfect tree on n n vertices, which only has about log ⁡ n \log n leaf-to-leaf path lengths in total. Let k ∈ ℕ k\in\mathbb{N} be the smallest integer such that N ≤ ( 169 / 10) k N\leq(169/10)^{k}. Set

 | X = { 1, 2, 5, 7 } ​ and ​ Y = { − 5, − 4, − 1, 1 } X=\{1,2,5,7\}\text{ and }Y=\{-5,-4,-1,1\} |  |

and observe that

 | X − Y = [0, 12] ​ and ​ X + Y = { − 4, − 3, − 2, 0, 1, 2, 3, 4, 6, 8 }. X-Y=[0,12]\text{ and }X+Y=\{-4,-3,-2,0,1,2,3,4,6,8\}. |  |

We further set

 | U = { ∑ i = 0 k − 1 x i ​ 13 i: x i ∈ X } + 13 k − 1 6 + 1 U=\left\{\sum_{i=0}^{k-1}x_{i}13^{i}:x_{i}\in X\right\}+\frac{13^{k}-1}{6}+1 |  |

and

 | V = { ∑ i = 0 k − 1 y i ​ 13 i: y i ∈ Y } + 13 k − 1 6. V=\left\{\sum_{i=0}^{k-1}y_{i}13^{i}:y_{i}\in Y\right\}+\frac{13^{k}-1}{6}. |  |

Observe that U − V = [13 k] U-V=[13^{k}] and | U + V | = 10 k \left|U+V\right|=10^{k}. Thus for any even n ≥ ( 169 / 10) k n\geq(169/10)^{k}, applying Proposition 10 with m = 13 k m=13^{k} and β = log ⁡ 10 / log ⁡ 13 \beta=\log 10/\log 13 (and hence M = ⌊ ( 169 / 10) k ⌋ M=\lfloor(169/10)^{k}\rfloor) gives a tree T T on n n vertices with at most 26 ​ M 1 2 − β 26M^{\frac{1}{2-\beta}} leaf-to-leaf path lengths in [M] [M]. In particular, as 10 ​ M / 169 < N ≤ M 10M/169<N\leq M, there are at most 500 ​ N 1 2 − β 500N^{\frac{1}{2-\beta}} lengths in [N] [N], and so the conclusion of the theorem follows. ∎

Similar constructions to those in the above proof can be found in the work of Ruzsa [20].

### 3.3 Upper bound on path lengths witnessed by a leaf

###### Proof of Theorem 5 (ii).

We will provide an explicit construction of an n n -vertex 1–3 tree in which each individual leaf witnesses at most 20 ​ N 2 / 3 20N^{2/3} distinct leaf-to-leaf path lengths between 0 and N N.

Let m ≔ ⌊ N 1 / 3 ⌋ m\coloneqq\lfloor N^{1/3}\rfloor. Recall that we write ( i) m (i)_{m} for the residue of i mod m i\mod m, considered as an element of { 0, 1, …, m − 1 } \{0,1,\dots,m-1\}, and define the sequence ( a 1, …, a m 2) (a_{1},\dots,a_{m^{2}}) by

 | a i ≔ ⌈ i m ⌉ ⋅ m − ( i − 1) m. a_{i}\coloneqq\left\lceil\frac{i}{m}\right\rceil\cdot m-(i-1)_{m}. |  |

Observe that 1 ≤ a i ≤ m 2 ≤ N 2 / 3 1\leq a_{i}\leq m^{2}\leq N^{2/3} for each i ∈ [m 2] i\in[m^{2}]. Consider the tree T = T n ​ ( ( a i) i = 1 m 2) T=T_{n}((a_{i})_{i=1}^{m^{2}}) described in Section 3.1.

We claim that T T satisfies the conditions of the theorem. Suppose for the sake of contradiction that there is a leaf u ∈ V ⁡ ( T) u\in V(T) witnessing more than 20 ​ N 2 / 3 20N^{2/3} distinct lengths in [0, N] [0,N]. Then u u witnesses at least 18 ​ N 2 / 3 18N^{2/3} distinct lengths in [2 ​ N 2 / 3, N] [2N^{2/3},N]. We will show how to handle the case when u ∈ T j 0 u\in T_{j_{0}} for some j 0 ∈ [t] j_{0}\in[t], since the case when u ∈ { v 0, v t + 1 } u\in\{v_{0},v_{t+1}\} is only easier, as it will be clear by the end of the proof. Set q = ⌊ 18 ​ N 2 / 3 ⌋ q=\lfloor 18N^{2/3}\rfloor and let s 1, …, s q s_{1},\dots,s_{q} be leaves such that the distances d ⁡ ( u, s i) d(u,s_{i}) are all distinct and in the interval [2 ​ N 2 / 3, N] [2N^{2/3},N].

Since T j 0 T_{j_{0}} has at most N 2 / 3 N^{2/3} layers, every leaf-to-leaf path in T j 0 T_{j_{0}} is of length at most 2 ​ N 2 / 3 − 2 2N^{2/3}-2. But for every s i s_{i} we have d ⁡ ( s i, u) ≥ 2 ​ N 2 / 3 d(s_{i},u)\geq 2N^{2/3}, and thus s i ∉ T j 0 s_{i}\notin T_{j_{0}} for all i i.

For j ≠ j 0, t j\neq j_{0},t, any two leaves in T j T_{j} clearly are at the same distance from u u, since T j T_{j} is a perfect binary tree; and, provided j 0 ≠ t j_{0}\neq t, leaves in T t T_{t} can have at most two distinct distances to u u, since leaves in T t T_{t} are spread over at most two layers. Moreover, the only leaves not in any tree T i T_{i} are v 0, v t + 1 v_{0},v_{t+1}. Therefore, after relabeling the leaves s i s_{i} if necessary, we may assume that for 1 ≤ i ≤ q − 4 1\leq i\leq q-4, there exists j i ∈ [t] ∖ { j 0, t } j_{i}\in[t]\setminus\{j_{0},t\} with s i ∈ T j i s_{i}\in T_{j_{i}}, and the indices j i j_{i} are pairwise distinct.

For each integer 0 ≤ k ≤ t / m 2 0\leq k\leq t/m^{2}, define I k ≔ { k ​ m 2 + 1, …, ( k + 1) ​ m 2 } I_{k}\coloneqq\{km^{2}+1,\dots,(k+1)m^{2}\}. Let k 0 k_{0} satisfy I k 0 ∋ j 0 I_{k_{0}}\ni j_{0}. For each i ∈ [q − 4] i\in[q-4], if j i ∈ I k j_{i}\in I_{k} then we must have | k − k 0 | < 2 ​ N 1 / 3 |k-k_{0}|<2N^{1/3} since d ⁡ ( s i, u) ≤ N d(s_{i},u)\leq N. Then, by pigeonhole there exists k k such that

 | | I k ∩ { j i: i ∈ [q − 4] } | ≥ q − 4 4 ​ N 1 / 3 ≥ 4 ​ N 1 / 3 ≥ 4 ​ m. |I_{k}\cap\{j_{i}:i\in[q-4]\}|\geq\frac{q-4}{4N^{1/3}}\geq 4N^{1/3}\geq 4m. |  |

We split I k I_{k} into I L = I k ∩ [0, j 0) I_{L}=I_{k}\cap[0,j_{0}) and I R = I k ∩ ( j 0, t − 1] I_{R}=I_{k}\cap(j_{0},t-1], and observe that both I L I_{L} and I R I_{R} are non-empty if and only if k = k 0 k=k_{0}.

Recall that T j i T_{j_{i}} is a perfect binary tree on a ( j i) m 2 ∗ a_{(j_{i})_{m^{2}}^{*}} layers. For every i ∈ [q − 4] i\in[q-4] with j i ∈ I R j_{i}\in I_{R}, we have j i > j 0 j_{i}>j_{0} and thus

 | d ⁡ ( u, s i) = a ( j 0) m 2 ∗ + j i − j 0 + a ( j i) m 2 ∗ = a ( j 0) m 2 ∗ + ( j i) m 2 ∗ + k ​ m 2 − j 0 + a ( j i) m 2 ∗, d(u,s_{i})=a_{(j_{0})_{m^{2}}^{*}}+j_{i}-j_{0}+a_{(j_{i})_{m^{2}}^{*}}=a_{(j_{0})_{m^{2}}^{*}}+(j_{i})_{m^{2}}^{*}+km^{2}-j_{0}+a_{(j_{i})_{m^{2}}^{*}}, |  | (1) |

since the distance between u u and v j 0 v_{j_{0}} in T j 0 T_{j_{0}} is a ( j 0) m 2 ∗ a_{(j_{0})_{m^{2}}^{*}}, the distance between v j 0 v_{j_{0}} and v j i v_{j_{i}} in P P is j i − j 0 j_{i}-j_{0}, and the distance between v j i v_{j_{i}} and s i s_{i} in T j i T_{j_{i}} is a ( j i) m 2 ∗ a_{(j_{i})_{m^{2}}^{*}}. However, from the definition of a ( j i) m 2 ∗ a_{(j_{i})_{m^{2}}^{*}} it easily follows that a ( j i) m 2 ∗ + ( j i) m 2 ∗ ≡ 1 ( mod m) a_{(j_{i})_{m^{2}}^{*}}+(j_{i})_{m^{2}}^{*}\equiv 1\pmod{m}, which implies that the RHS of ( 1) can take at most m m distinct values as j i ∈ I R j_{i}\in I_{R} varies. Hence we must have | I R | ≤ m |I_{R}|\leq m, which implies | I L | ≥ | I k | − m ≥ 3 ​ m |I_{L}|\geq|I_{k}|-m\geq 3m.

Similarly, for j i ∈ I L j_{i}\in I_{L} we have j i < j 0 j_{i}<j_{0} and thus

 | d ⁡ ( u, s i) = a ( j i) m 2 ∗ + j 0 − j i + a ( j 0) m 2 ∗ = a ( j i) m 2 ∗ + j 0 − ( j i) m 2 ∗ − k ​ m 2 + a ( j 0) m 2 ∗. d(u,s_{i})=a_{(j_{i})_{m^{2}}^{*}}+j_{0}-j_{i}+a_{(j_{0})_{m^{2}}^{*}}=a_{(j_{i})_{m^{2}}^{*}}+j_{0}-(j_{i})_{m^{2}}^{*}-km^{2}+a_{(j_{0})_{m^{2}}^{*}}. |  | (2) |

However, for each s ∈ [m 2] s\in[m^{2}] we see from the definition of a s a_{s} that

 | − m + 1 ≤ ( s m ⋅ m − ( s − 1) m) − s ≤ a s − s ≤ ( ( s m + 1) ⋅ m − ( s − 1) m) − s ≤ m. -m+1\leq\left(\frac{s}{m}\cdot m-(s-1)_{m}\right)-s\leq a_{s}-s\leq\left(\left(\frac{s}{m}+1\right)\cdot m-(s-1)_{m}\right)-s\leq m. |  |

This implies that the RHS of ( 2) can take at most 2 ​ m 2m distinct values as j i ∈ I L j_{i}\in I_{L} varies. Together with the fact that | I L | ≥ 3 ​ m |I_{L}|\geq 3m, this yields the desired contradiction.

It is not hard to see that when u ∈ { v 0, v t + 1 } u\in\{v_{0},v_{t+1}\} essentially the same argument again gives a contradiction. ∎

## 4 Cycles in degree k k -critical graphs

Recall that an n n -vertex graph is *degree k k -critical*for some k ≥ 3 k\geq 3 if it has ( k − 1) ​ n − ( k 2) + 1 (k-1)n-{k\choose{2}}+1 edges and no proper induced subgraph with minimum degree at least k k. In this section, we prove a lower bound on the number of cycle lengths in graphs belonging to a general family that contains all degree k k -critical graphs (i.e. Theorem 12 below). By taking k = 3 k=3, this result implies Theorem 1.

Our first lemma provides a useful ordering of the vertex set of a degree k k -critical graph; we remark that the case k = 3 k=3 was already proven in [10, Lemma 1]. Let 𝒳 = x 1, x 2, …, x n \mathcal{X}=x_{1},x_{2},\dots,x_{n} be a given ordering of the vertex set V V of a graph G G. For x i ∈ V x_{i}\in V, define N 𝒳 + ​ ( x i) = { x j ∈ N G ​ ( x i): i < j } N_{\mathcal{X}}^{+}(x_{i})=\{x_{j}\in N_{G}(x_{i}):i<j\} and N 𝒳 − ​ ( x i) = { x j ∈ N G ​ ( x i): i > j } N_{\mathcal{X}}^{-}(x_{i})=\{x_{j}\in N_{G}(x_{i}):i>j\}. We also define d 𝒳 + ​ ( x i) = | N 𝒳 + ​ ( x i) | d_{\mathcal{X}}^{+}(x_{i})=|N_{\mathcal{X}}^{+}(x_{i})| and d 𝒳 − ​ ( x i) = | N 𝒳 − ​ ( x i) | d_{\mathcal{X}}^{-}(x_{i})=|N_{\mathcal{X}}^{-}(x_{i})|. We will generally omit the subscript 𝒳 \mathcal{X} if the ordering is clear from context.

###### Lemma 11.

Let k ≥ 3 k\geq 3 and n ≥ k + 1 n\geq k+1. Given any n n -vertex degree k k -critical graph G G, there exists an ordering 𝒳 = x 1, x 2, …, x n \mathcal{X}=x_{1},x_{2},\dots,x_{n} of V = V ⁡ ( G) V=V(G) such that

 | d + ​ ( x i) = { k if ​ i = 1, k − 1 if ​ i ∈ [2, n − k + 1], n − i if ​ i ∈ [n − k + 2, n]. \displaystyle d^{+}(x_{i})=\left\{\begin{array}[]{rcl}k&&\text{if }i=1,\\ k-1&&\text{if }i\in[2,n-k+1],\\ n-i&&\text{if }i\in[n-k+2,n].\end{array}\right. |  |

###### Proof.

We construct the ordering x 1, x 2, …, x n x_{1},x_{2},\dots,x_{n} iteratively. As a first step, note that by definition there exists a vertex x 1 ∈ V x_{1}\in V satisfying d G ​ ( x 1) ≤ k d_{G}(x_{1})\leq k; otherwise, deleting any vertex in G G would leave a proper induced subgraph with minimum degree at least k k.

Assume we have chosen { x 1, …, x ℓ } \{x_{1},\dots,x_{\ell}\} for some ℓ ∈ [n − k] \ell\in[n-k]. Since the minimum degree of the proper induced subgraph G ⁡ [V ∖ { x 1, …, x ℓ }] G[V\setminus\{x_{1},\dots,x_{\ell}\}] is less than k k, there exists a vertex v ∈ V ∖ { x 1, …, x ℓ } v\in V\setminus\{x_{1},\dots,x_{\ell}\} such that | N G ​ ( v) ∖ { x 1, …, x ℓ } | ≤ k − 1 |N_{G}(v)\setminus\{x_{1},\dots,x_{\ell}\}|\leq k-1. Define x ℓ + 1 = v x_{\ell+1}=v.

After selecting { x 1, …, x n − k + 1 } \{x_{1},\dots,x_{n-k+1}\}, we order the remaining k − 1 k-1 vertices arbitrarily as x n − k + 2, …, x n x_{n-k+2},\dots,x_{n}. Then the ordering x 1, x 2, …, x n x_{1},x_{2},\dots,x_{n} satisfies d + ​ ( x 1) ≤ k d^{+}(x_{1})\leq k, d + ​ ( x i) ≤ k − 1 d^{+}(x_{i})\leq k-1 for i ∈ [2, n − k + 1] i\in[2,n-k+1], and d + ​ ( x i) ≤ n − i d^{+}(x_{i})\leq n-i for i ∈ [n − k + 2, n] i\in[n-k+2,n].

We can thus bound the number of edges in G G as

 | | E ⁡ ( G) | = ∑ i = 1 n d + ​ ( x i) ≤ k + ( k − 1) ​ ( n − k) + ∑ i = 0 k − 2 i = n ⁡ ( k − 1) − k ⁡ ( k − 1) 2 + 1. |E(G)|=\sum_{i=1}^{n}d^{+}(x_{i})\leq k+(k-1)(n-k)+\sum_{i=0}^{k-2}i=n(k-1)-\frac{k(k-1)}{2}+1. |  |

By definition, G G has exactly n ⁡ ( k − 1) − k ⁡ ( k − 1) 2 + 1 n(k-1)-\frac{k(k-1)}{2}+1 edges, hence all inequalities in the previous expression must hold with equality, which proves the lemma. ∎

Fix an integer k ≥ 3 k\geq 3. Let G G be a graph on n n vertices and let 𝒳 = x 1, x 2, …, x n \mathcal{X}=x_{1},x_{2},\dots,x_{n} be an ordering of V ⁡ ( G) V(G). We say that ( G, 𝒳) (G,\mathcal{X}) is a k-ordered graph if

- (1)

x n − 1 ​ x n ∈ E ⁡ ( G) x_{n-1}x_{n}\in E(G),

- (2)

d + ​ ( x i) ∈ [2, k] d^{+}(x_{i})\in[2,k] for i ∈ [1, n − 2], i\in[1,n-2], and

- (3)

d − ​ ( x i) ≥ 1 d^{-}(x_{i})\geq 1 for i ∈ [2, n]. i\in[2,n].

Suppose G G is a degree k k -critical graph on n n vertices and let 𝒳 = x 1, x 2, …, x n \mathcal{X}=x_{1},x_{2},\dots,x_{n} be the ordering given by Lemma 11. Then it is easy to verify that ( G, 𝒳) (G,\mathcal{X}) is a k k -ordered graph.

Given a graph G G, we use 𝒞 G \mathcal{C}_{G} to denote the set of cycle lengths in G G. We can now state the main result of this section.

###### Theorem 12.

Let k ≥ 3 k\geq 3 and n ≥ k + 1 n\geq k+1. If ( G, 𝒳) (G,\mathcal{X}) is a k k -ordered graph on n n vertices, then | 𝒞 G | ≥ log ⁡ n 3 + log ⁡ k − 2 |\mathcal{C}_{G}|\geq\frac{\log n}{3+\log k}-2.

Throughout the rest of this section, we will assume that ( G, 𝒳) (G,\mathcal{X}) is a k k -ordered graph. Let u, v ∈ V ⁡ ( G) u,v\in V(G) and P = w 1 w 2 ⋯ w t P=w_{1}w_{2}\cdots w_{t} be a path in G G where w 1 = u w_{1}=u and w t = v w_{t}=v. We call P P a forward (u,v)-path if w i + 1 ∈ N 𝒳 + ​ ( w i) w_{i+1}\in N_{\mathcal{X}}^{+}(w_{i}) for every i ∈ [t − 1] i\in[t-1]. In particular, we also view a path consisting of a single vertex as a forward path.

Towards the proof of Theorem 12, we start with a series of lemmas. The first lemma establishes a lower bound on | 𝒞 G | |\mathcal{C}_{G}| based on the length of the longest forward path in G G.

###### Lemma 13.

Let k ≥ 3 k\geq 3 and let ( G, 𝒳) (G,\mathcal{X}) be a k k -ordered graph. For any integer ℓ ≥ 2 \ell\geq 2, if G G contains a forward path of length ℓ \ell, then | 𝒞 G | ≥ log ⁡ ( ℓ + 1) − 1 |\mathcal{C}_{G}|\geq\log(\ell+1)-1.

###### Proof.

Fix a vertex v 1 ∈ V ⁡ ( G) ∖ { x n − 1, x n } v_{1}\in V(G)\setminus\{x_{n-1},x_{n}\}. Let P = v 1 ⋯ v t P=v_{1}\cdots v_{t} be a longest forward path starting at v 1 v_{1}. Note that d + ​ ( v 1) ≥ 2 d^{+}(v_{1})\geq 2, and thus v 1 v_{1} has a forward neighbour v ′ ∈ V ∖ { x n } v^{\prime}\in V\setminus\{x_{n}\}. Since each v ∈ V ∖ { x n } v\in V\setminus\{x_{n}\} satisfies d + ​ ( v) ≥ 1 d^{+}(v)\geq 1, there exists a forward path from v ′ v^{\prime} to x n x_{n}. For the same reason, each longest forward path has x n x_{n} as its endpoint. Thus, v t = x n v_{t}=x_{n} and t ≥ 3 t\geq 3.

We claim that 𝒞 G ∩ [t, 2 ​ t − 2] ≠ ∅ \mathcal{C}_{G}\cap[t,2t-2]\neq\emptyset. We will construct a cycle of suitable length by following a strategy similar to [2]. Given two vertices a, b ∈ V ⁡ ( P) a,b\in V(P), we write a < b a<b if a a precedes b b in P P, and we write a ≤ b a\leq b if either a < b a<b or a = b a=b. Given a path Q Q and vertices u, v ∈ Q u,v\in Q, recall that Q ⁡ [u, v] Q[u,v] denotes the unique subpath of Q Q whose endpoints are u u and v v. Following the idea in [4], we define a slightly stronger version of *vine*based on P P as a collection of internally vertex-disjoint forward paths 𝒬 = { Q i: i ∈ [m] } \mathcal{Q}=\{Q_{i}:i\in[m]\} such that the ends of Q i Q_{i} are ( a i, b i) (a_{i},b_{i}) and the following are satisfied:

1. (1)

V ⁡ ( Q i) ∩ V ⁡ ( P) = { a i, b i } V(Q_{i})\cap V(P)=\{a_{i},b_{i}\} and ℓ ⁡ ( P ⁡ [a i, b i]) ≥ 2 \ell(P[a_{i},b_{i}])\geq 2 for every i ∈ [m] i\in[m];

2. (2)

v 1 = a 1 < a 2 < b 1 ≤ a 3 < b 2 ≤ a 4 < b 3 ≤ ⋯ ≤ a m < b m − 1 < b m = x n v_{1}=a_{1}<a_{2}<b_{1}\leq a_{3}<b_{2}\leq a_{4}<b_{3}\leq\cdots\leq a_{m}<b_{m-1}<b_{m}=x_{n}; and

3. (3)

a i + 1 a_{i+1} is the immediate predecessor of b i b_{i} on P P for every i ∈ [m − 1]. i\in[m-1].

We will first show the existence of the above structure 𝒬 \mathcal{Q} based on P P and then argue that this implies the existence of a cycle of the desired length. For the first of these tasks, we argue inductively that we can construct a collection of paths 𝒬 \mathcal{Q} satisfying (1), (2), and (3), and then show that satisfying these conditions implies that the paths are internally vertex-disjoint.

Suppose that for some r ≥ 0 r\geq 0 we have constructed paths Q 1, …, Q r Q_{1},\dots,Q_{r} satisfying (1), (3), as well as

1. (2 ′)

v 1 = a 1 < a 2 < b 1 ≤ a 3 < b 2 ≤ a 4 < b 3 ≤ ⋯ ≤ a r < b r − 1 < b r v_{1}=a_{1}<a_{2}<b_{1}\leq a_{3}<b_{2}\leq a_{4}<b_{3}\leq\dots\leq a_{r}<b_{r-1}<b_{r}.

Let us show how to construct Q r + 1 Q_{r+1}. If r = 0 r=0, we let a r + 1 = v 1 a_{r+1}=v_{1}, and observe that with this choice we have d + ​ ( a r + 1) ≥ 2 d^{+}(a_{r+1})\geq 2. If r > 0 r>0, then we may assume that b r < x n b_{r}<x_{n} as otherwise (2) is also satisfied and we are done. In this case, we let a r + 1 a_{r+1} be the immediate predecessor of b r b_{r} on P P, and observe that again d + ​ ( a r + 1) ≥ 2 d^{+}(a_{r+1})\geq 2 since a r + 1 < b r < x n a_{r+1}<b_{r}<x_{n}.

Since d + ​ ( a r + 1) ≥ 2 d^{+}(a_{r+1})\geq 2, a r + 1 a_{r+1} has a neighbour c r + 1 ∈ N + ​ ( a r + 1) ∖ { b r } c_{r+1}\in N^{+}(a_{r+1})\setminus\{b_{r}\}. Let P r + 1 P_{r+1} be a forward ( c r + 1, x n) (c_{r+1},x_{n}) -path, and let b r + 1 b_{r+1} be the vertex in V ⁡ ( P r + 1) ∩ V ⁡ ( P) V(P_{r+1})\cap V(P) which minimizes ℓ ⁡ ( P r + 1 ​ [c r + 1, b r + 1]) \ell(P_{r+1}[c_{r+1},b_{r+1}]). Indeed, x n ∈ V ⁡ ( P r + 1) ∩ V ⁡ ( P) x_{n}\in V(P_{r+1})\cap V(P) and thus such a vertex must exist. Define

 | Q r + 1 = { a r + 1 ​ c r + 1 } ∪ P r + 1 ​ [c r + 1, b r + 1], Q_{r+1}=\{a_{r+1}c_{r+1}\}\cup P_{r+1}[c_{r+1},b_{r+1}], |  |

so that Q r + 1 Q_{r+1} is a forward path. By definition, V ⁡ ( Q r + 1) ∩ V ⁡ ( P) = { a r + 1, b r + 1 } V(Q_{r+1})\cap V(P)=\{a_{r+1},b_{r+1}\}. Moreover, ℓ ⁡ ( P ⁡ [a r + 1, b r + 1]) ≥ 2 \ell(P[a_{r+1},b_{r+1}])\geq 2, since otherwise a r + 1 ​ b r + 1 ∈ E ⁡ ( P) a_{r+1}b_{r+1}\in E(P), and as Q r + 1 Q_{r+1} is a forward path it would follow that b r + 1 = b r ≠ c r + 1 b_{r+1}=b_{r}\neq c_{r+1}, and thus ( P ∖ { a r + 1 ​ b r + 1 }) ∪ Q r + 1 (P\setminus\{a_{r+1}b_{r+1}\})\cup Q_{r+1} is a longer forward path starting at v 1 v_{1}, contradiction. Finally, if r ≥ 2 r\geq 2, we have b r − 1 ≤ a r + 1 b_{r-1}\leq a_{r+1}, since a r a_{r} is the predecessor of b r − 1 b_{r-1} and a r + 1 a_{r+1} is the predecessor of b r b_{r}. This shows that Q 1, …, Q r + 1 Q_{1},\dots,Q_{r+1} satisfy conditions (1), (2′), and (3).

We repeat this procedure as long as possible, eventually obtaining a collection of paths 𝒬 = { Q 1, …, Q m } \mathcal{Q}=\{Q_{1},\dots,Q_{m}\} satisfying (1), (2), and (3). We claim that for any i < j i<j, Q i Q_{i} and Q j Q_{j} are internally vertex-disjoint. If i + 2 ≤ j i+2\leq j, then (2) implies that a i < b i ≤ a j < b j a_{i}<b_{i}\leq a_{j}<b_{j} and thus Q i Q_{i} and Q j Q_{j} are internally disjoint since they are both forward paths. In the case j = i + 1 j=i+1, suppose for a contradiction that the interiors of Q i Q_{i} and Q j Q_{j} intersect at c ∈ V ⁡ ( G) c\in V(G). Then Q i + 1 ​ [a i + 1, c] ∪ Q i ​ [c, b i] Q_{i+1}[a_{i+1},c]\cup Q_{i}[c,b_{i}] is a forward ( a i + 1, b i) (a_{i+1},b_{i}) -path of length at least 2. Hence ( P ∖ { a i + 1 ​ b i }) ∪ Q i + 1 ​ [a i + 1, c] ∪ Q i ​ [c, b i] \left(P\setminus\{a_{i+1}b_{i}\}\right)\cup Q_{i+1}[a_{i+1},c]\cup Q_{i}[c,b_{i}] is a forward ( v 1, x n) (v_{1},x_{n}) -path of length at least t t, which is strictly greater than ℓ ⁡ ( P) \ell(P), contradicting the maximality of P P.

a 1 a_{1} b 1 b_{1} a 2 a_{2} b 2 b_{2} a 6 a_{6} b 6 b_{6} a 7 a_{7} b 7 b_{7} a 4 a_{4} b 4 b_{4} a 3 a_{3} b 3 = a 5 b_{3}=a_{5} b 5 b_{5} Figure 2: An example of the forward path P P and the path collection 𝒬 \mathcal{Q} forming a vine. The cycle C C is illustrated by the bold line.

The vine 𝒬 \mathcal{Q} just constructed yields the cycle (cf. Figure 2)

 | C = ( P ∖ { a j + 1 ​ b j: j ∈ [m − 1] }) ∪ ( ⋃ i ∈ [m] Q i ​ [a i, b i]). C=\big(P\setminus\{a_{j+1}b_{j}:j\in[m-1]\}\big)\cup\left(\bigcup\limits_{i\in[m]}Q_{i}[a_{i},b_{i}]\right). |  |

In other words, if m m is odd, this cycle is precisely

 | a 1 ​ Q 1 ​ b 1 ​ P ¯ ​ a 3 ​ Q 3 ​ b 3 ​ … ​ a m ​ Q m ​ b m ​ P ¯ ​ b m − 1 ​ Q m − 1 ​ a m − 1 ​ … ​ a 2 ​ P ¯ ​ a 1, a_{1}Q_{1}b_{1}\overline{P}a_{3}Q_{3}b_{3}\dots a_{m}Q_{m}b_{m}\overline{P}b_{m-1}Q_{m-1}a_{m-1}\dots a_{2}\overline{P}a_{1}, |  |

whereas if it is even, the cycle we get is

 | a 1 ​ Q 1 ​ b 1 ​ P ¯ ​ a 3 ​ Q 3 ​ b 3 ​ … ​ a m − 1 ​ Q m − 1 ​ b m − 1 ​ P ¯ ​ b m ​ Q m ​ a m ​ … ​ a 2 ​ P ¯ ​ a 1, a_{1}Q_{1}b_{1}\overline{P}a_{3}Q_{3}b_{3}\dots a_{m-1}Q_{m-1}b_{m-1}\overline{P}b_{m}Q_{m}a_{m}\dots a_{2}\overline{P}a_{1}, |  |

where we informally write P ¯ \overline{P} above to refer to any subpath between two specified vertices on the path P P.

It remains to verify that ℓ ⁡ ( C) ∈ [t, 2 ​ t − 2] \ell(C)\in[t,2t-2]. Since V ⁡ ( C) ⊇ V ⁡ ( P) V(C)\supseteq V(P), we have that ℓ ⁡ ( C) ≥ t \ell(C)\geq t. We also have ℓ ⁡ ( Q i) ≤ ℓ ⁡ ( P ⁡ [a i, b i]) \ell(Q_{i})\leq\ell(P[a_{i},b_{i}]), as otherwise the forward path ( P ∖ P ⁡ [a i, b i]) ∪ Q i ​ [a i, b i] \big(P\setminus P[a_{i},b_{i}]\big)\cup Q_{i}[a_{i},b_{i}] contradicts the maximality of P P. Hence, we have

 | ℓ ⁡ ( C) = ℓ ⁡ ( P) + ∑ i = 1 m ℓ ⁡ ( Q i) − ( m − 1) ≤ ℓ ⁡ ( P) + ∑ i = 1 m ℓ ⁡ ( P ⁡ [a i, b i]) − ( m − 1) = 2 ​ ℓ ​ ( P) = 2 ​ t − 2. \ell(C)=\ell(P)+\sum\limits_{i=1}^{m}\ell(Q_{i})-(m-1)\leq\ell(P)+\sum\limits_{i=1}^{m}\ell(P[a_{i},b_{i}])-(m-1)=2\ell(P)=2t-2. |  |

Let Q = u 1 u 2 ⋯ u ℓ + 1 Q=u_{1}u_{2}\cdots u_{\ell+1} be a longest forward path in G G, so that u ℓ + 1 = x n u_{\ell+1}=x_{n}. Then for every t ∈ [2, ℓ] t\in[2,\ell], Q ⁡ [u ℓ + 1 − t, x n] Q[u_{\ell+1-t},x_{n}] is a longest forward path with t + 1 ≥ 3 t+1\geq 3 vertices starting at the vertex u ℓ + 1 − t u_{\ell+1-t} in G G. By the argument above, each of these paths yields a cycle whose length belongs to the interval [t + 1, 2 ​ t] [t+1,2t]. Thus, 𝒞 G ∩ [t + 1, 2 ​ t] ≠ ∅ \mathcal{C}_{G}\cap[t+1,2t]\neq\emptyset for every t ∈ [2, ℓ] t\in[2,\ell], which implies 𝒞 G ∩ [2 s + 1, 2 s + 1] ≠ ∅ \mathcal{C}_{G}\cap[2^{s}+1,2^{s+1}]\neq\emptyset for every s ∈ [⌊ log ⁡ ℓ ⌋] s\in\big[\lfloor\log\ell\rfloor\big]. Since the intervals [2 s + 1, 2 s + 1] [2^{s}+1,2^{s+1}] are pairwise disjoint, we obtain | 𝒞 G | ≥ ⌊ log ⁡ ℓ ⌋ ≥ log ⁡ ( ℓ + 1) − 1 |\mathcal{C}_{G}|\geq\lfloor\log\ell\rfloor\geq\log(\ell+1)-1, as desired. ∎

Our next goal is to establish a lower bound on | 𝒞 G | |\mathcal{C}_{G}| under the assumption that G G contains no long forward path. Our proof proceeds by defining a suitable partial order on V ⁡ ( G) V(G) and then showing that the absence of long forward paths in G G implies the absence of long chains in this partial order. Thanks to the following classical theorem, this will allow us to reduce the problem to the case where G G has a long antichain.

###### Theorem 14 (Dilworth [8]).

In any finite partial order, the maximum size of an antichain is equal to the minimum number of chains required to cover all its elements.

Let ( G, 𝒳) (G,\mathcal{X}) be a k k -ordered graph and let V = V ⁡ ( G) V=V(G). For u, v ∈ V u,v\in V, let u ⪯ v u\preceq v if there exists a forward ( u, v) (u,v) -path in G G. It is easy to see that ( V, ⪯) (V,\preceq) is a partial order. We call ( V, ⪯) (V,\preceq) the partial order generated by 𝒳 \mathcal{X}. We also write u ≺ v u\prec v when u ⪯ v u\preceq v and u ≠ v u\neq v. Observe that if v 1 ≺ v 2 ≺ ⋯ ≺ v ℓ v_{1}\prec v_{2}\prec\cdots\prec v_{\ell} is a chain under the partial order ( V, ⪯) (V,\preceq), then there exists a forward path P P such that v 1, v 2, ⋯, v ℓ v_{1},v_{2},\cdots,v_{\ell} occur sequentially along P P. Hence if every forward path in G G has length at most ℓ \ell, then every chain under ( V, ⪯) (V,\preceq) contains at most ℓ + 1 \ell+1 elements. If so, by Theorem 14, ( V, ⪯) (V,\preceq) contains an antichain on at least n / ( ℓ + 1) n/(\ell+1) elements.

The next lemma shows that, given any antichain L L, one can find two trees whose leaf set is precisely L L and which have no other vertices in common. A subtree T T of G G rooted at u u is called forward-directed (resp. backward-directed) if

- (1)

for any subpath P = u 1 u 2 ⋯ u t P=u_{1}u_{2}\cdots u_{t} of T T with u 1 = u u_{1}=u and u t ∈ L ⁡ ( T) u_{t}\in L(T), u i ⪯ u i + 1 u_{i}\preceq u_{i+1} (resp. u i + 1 ⪯ u i u_{i+1}\preceq u_{i}) for every i ∈ [t − 1] i\in[t-1]; and

- (2)

either d T ​ ( u) ≥ 2 d_{T}(u)\geq 2 or T T consists of a single vertex.

Hence the root of a forward-directed (resp. backward-directed) tree T T is its minimum (maximum) vertex under ⪯ \preceq.

###### Lemma 15.

Let ( G, 𝒳) (G,\mathcal{X}) be a k k -ordered graph for some k ≥ 3 k\geq 3 and let ( V, ⪯) (V,\preceq) be the partial order generated by 𝒳 \mathcal{X}. Then for any given antichain L = { v 1, v 2, ⋯, v m } L=\{v_{1},v_{2},\cdots,v_{m}\} under ⪯ \preceq, there exist a forward-directed subtree S S and a backward-directed subtree T T of G G satisfying L ⁡ ( S) = L ⁡ ( T) = L L(S)=L(T)=L.

###### Proof.

We will just prove the existence of a forward-directed tree S S such that L ⁡ ( S) = L L(S)=L, since, as will be clear by the end of the proof, the existence of the required backward-directed tree follows by symmetry.

S S is constructed through the following procedure. At the start, we let S 1 = { v 1 } S_{1}=\{v_{1}\}, which we view as a one-vertex tree rooted at v 1 v_{1}. Now, suppose that we have already constructed a forward-directed tree S i S_{i} for some integer i ∈ [m − 1] i\in[m-1], and that L ⁡ ( S i) = { v 1, ⋯, v i } L(S_{i})=\{v_{1},\cdots,v_{i}\}. Let u i u_{i} be the root of S i S_{i}. Then v i + 1 ⪯ u i v_{i+1}\preceq u_{i} cannot hold, as otherwise v i + 1 ⪯ u i ⪯ v 1 v_{i+1}\preceq u_{i}\preceq v_{1}, contradicting the fact that L L forms an antichain under ⪯ \preceq.

We will now show how to extend S i S_{i} to a larger forward-directed tree S i + 1 S_{i+1} with L ⁡ ( S i + 1) = { v 1, …, v i + 1 } L(S_{i+1})=\{v_{1},\dots,v_{i+1}\}. We split into two cases.

Case 1: u i ≺ v i + 1 u_{i}\prec v_{i+1}.

Note that this cannot happen when i = 1 i=1, hence we may assume that | L ⁡ ( S i) | ≥ 2 |L(S_{i})|\geq 2 and d S i ​ ( u i) ≥ 2 d_{S_{i}}(u_{i})\geq 2. Let v ∈ V ⁡ ( S i) v\in V(S_{i}) be a maximal vertex under ⪯ \preceq such that v ⪯ v i + 1 v\preceq v_{i+1}. Select an arbitrary forward ( v, v i + 1) (v,v_{i+1}) path P P in G G, which implies V ⁡ ( P) ∩ V ⁡ ( S i) = { v } V(P)\cap V(S_{i})=\{v\} by maximality of v v. Let S i + 1 = S i ∪ P S_{i+1}=S_{i}\cup P, and observe that d S i + 1 ​ ( u i) ≥ d S i ​ ( u i) ≥ 2 d_{S_{i+1}}(u_{i})\geq d_{S_{i}}(u_{i})\geq 2. Thus, S i + 1 S_{i+1} is a forward-directed tree rooted at u i u_{i} such that L ⁡ ( S i + 1) = { v 1, ⋯, v i + 1 } L(S_{i+1})=\{v_{1},\cdots,v_{i+1}\}.

Case 2: u i ⊀ v i + 1 u_{i}\nprec v_{i+1}.

Let w ∈ V ⁡ ( G) w\in V(G) be a maximal vertex under ⪯ \preceq such that w ⪯ v i + 1 w\preceq v_{i+1} and w ⪯ u i w\preceq u_{i}. Indeed, such a vertex w w exists since x 1 ⪯ u i x_{1}\preceq u_{i} and x 1 ⪯ v i + 1 x_{1}\preceq v_{i+1} (recall that each vertex x ∈ V ⁡ ( G) ∖ { x 1 } x\in V(G)\setminus\{x_{1}\} satisfies d − ​ ( x) ≥ 1 d^{-}(x)\geq 1, and thus x 1 ⪯ x x_{1}\preceq x). Select an arbitrary forward ( w, u i) (w,u_{i}) path P P and an arbitrary forward ( w, v i + 1) (w,v_{i+1}) path Q Q. Then, our choice of w w and the fact that u i ⊀ v i + 1 u_{i}\nprec v_{i+1} imply that V ⁡ ( P) ∩ V ⁡ ( S i) = { u i } V(P)\cap V(S_{i})=\{u_{i}\}, V ⁡ ( Q) ∩ V ⁡ ( S i) = ∅ V(Q)\cap V(S_{i})=\emptyset, and V ⁡ ( P) ∩ V ⁡ ( Q) = { w } V(P)\cap V(Q)=\{w\}. Letting S i + 1 = S i ∪ P ∪ Q S_{i+1}=S_{i}\cup P\cup Q, we have d S i + 1 ​ ( w) ≥ 2 d_{S_{i+1}}(w)\geq 2. Thus, S i + 1 S_{i+1} is a forward-directed tree rooted at w w such that L ⁡ ( S i + 1) = { v 1, ⋯, v i + 1 } L(S_{i+1})=\{v_{1},\cdots,v_{i+1}\}.

The algorithm terminates with a forward-directed tree S m S_{m} with L ⁡ ( S m) = L L(S_{m})=L, as required. It can be easily checked that the same argument yields a backward-directed tree T T such that L ⁡ ( T) = L L(T)=L. The only part of the argument that does not follow directly from the symmetry of the partial order is in Case 2, where we instead use the fact that x ⪯ x n x\preceq x_{n} for each x ∈ V ⁡ ( G) ∖ { x n } x\in V(G)\setminus\{x_{n}\} since d + ​ ( x) ≥ 1 d^{+}(x)\geq 1. ∎

We call a tree T T rooted at u u*fair*if, for some q ≥ 1 q\geq 1, each leaf x ∈ L ⁡ ( T) x\in L(T) satisfies d ⁡ ( u, x) = q d(u,x)=q. The following lemma shows that by reducing the size of the antichain L L by at most a constant factor, we can essentially assume that the forward-directed and backward-directed subtrees guaranteed by Lemma 15 are both fair.

###### Lemma 16.

Let k ≥ 3, c ≥ 1 k\geq 3,c\geq 1. Let ( G, 𝒳) (G,\mathcal{X}) be a k k -ordered graph with no forward path of length c c, and let ( V, ⪯) (V,\preceq) be the partial order generated by 𝒳 \mathcal{X}. Then G G contains an antichain L 0 ⊆ V L_{0}\subseteq V, a fair forward-directed tree S 0 S_{0}, and a fair backward-directed tree T 0 T_{0}, satisfying L ⁡ ( S 0) = L ⁡ ( T 0) = L 0 L(S_{0})=L(T_{0})=L_{0}. Moreover, | L 0 | ≥ | V | c 3 |L_{0}|\geq\frac{|V|}{c^{3}}.

###### Proof.

First, observe that if | V | ≤ c 3 |V|\leq c^{3}, then the statement can be seen to be trivially true by choosing L 0 = { v } L_{0}=\{v\} where v ∈ V v\in V is arbitrary, and letting S 0 S_{0} and T 0 T_{0} be one-vertex trees with vertex set { v } \{v\}. With this choice, | L 0 | = 1 ≥ | V | / c 3 |L_{0}|=1\geq|V|/c^{3}.

From now on, we will assume that | V | > c 3 |V|>c^{3}. By our assumption on the length of forward paths in ( G, 𝒳) (G,\mathcal{X}), every chain under ⪯ \preceq contains at most c c elements. By Theorem 14, this implies that there is an antichain L L satisfying | L | ≥ | V | c |L|\geq\frac{|V|}{c}.

By Lemma 15, there exist a forward-directed tree S S rooted at u u and a backward-directed tree T T rooted at v v with L ⁡ ( S) = L ⁡ ( T) = L L(S)=L(T)=L. Observe that the path in S S connecting u u to any given w ∈ L w\in L is a forward path, and thus of length at most c c. So, there is a subset L 1 ⊆ L L_{1}\subseteq L with | L 1 | ≥ | L | c ≥ | V | c 2 ≥ 2 |L_{1}|\geq\frac{|L|}{c}\geq\frac{|V|}{c^{2}}\geq 2 such that any two leaves in L 1 L_{1} are at the same distance from u u in S S. Let S 1 S_{1} and T 1 T_{1} be the unique subtrees of S S and T T such that L ⁡ ( S 1) = L ⁡ ( T 1) = L 1 L(S_{1})=L(T_{1})=L_{1}. Let u ′ ∈ V ⁡ ( S 1) u^{\prime}\in V(S_{1}) be the minimum vertex under ≺ \prec. Then d S 1 ​ ( u ′) ≥ 2 d_{S_{1}}(u^{\prime})\geq 2 and S 1 S_{1} is a forward-directed tree rooted at u ′ u^{\prime}. Analogously, by choosing v ′ ∈ V ⁡ ( T 1) v^{\prime}\in V(T_{1}) to be the maximum vertex under ≺ \prec, we get that T 1 T_{1} is a backward-directed tree rooted at v ′ v^{\prime}. Moreover, S 1 S_{1} is fair.

We now apply a similar procedure to T 1 T_{1}. Again, there must be a subset L 0 ⊆ L 1 L_{0}\subseteq L_{1} with | L 0 | ≥ | L 1 | c ≥ | V | c 3 > 1 |L_{0}|\geq\frac{|L_{1}|}{c}\geq\frac{|V|}{c^{3}}>1 such that any two leaves in L 0 L_{0} are at the same distance from v ′ v^{\prime} in T 1 T_{1}. Let S 0 S_{0} and T 0 T_{0} be the unique subtrees of S 1 S_{1} and T 1 T_{1} respectively, such that L ⁡ ( S 0) = L ⁡ ( T 0) = L 0 L(S_{0})=L(T_{0})=L_{0}. By the same argument as before, S 0 S_{0} is a forward-directed tree and T 0 T_{0} is a backward-directed tree. Moreover, both S 0 S_{0} and T 0 T_{0} are fair, as required. ∎

Next, we obtain a lower bound on | 𝒞 G | |\mathcal{C}_{G}| using the structure from Lemma 16. It will be sufficient for our purposes to consider cycles of a special kind. We call a cycle C C*good*if C C is the union of two internally-disjoint forward ( u, v) (u,v) -paths for two vertices u, v ∈ V u,v\in V. Denote the set of all lengths of good cycles in G G by 𝒞 1 ​ ( G) \mathcal{C}_{1}(G).

###### Lemma 17.

Let k ≥ 3, Δ ≥ 2 k\geq 3,\Delta\geq 2, and let ( G, 𝒳) (G,\mathcal{X}) be a k k -ordered graph. Suppose that S S is a fair forward-directed tree in G G, and that T T is a fair backward-directed tree in G G, such that L ⁡ ( S) = L ⁡ ( T) = L L(S)=L(T)=L where | L | ≥ 2 |L|\geq 2. Further assume that Δ ⁡ ( S) ≤ Δ \Delta(S)\leq\Delta. Then | 𝒞 1 ​ ( S ∪ T) | ≥ log ⁡ | L | log ⁡ Δ |\mathcal{C}_{1}(S\cup T)|\geq\frac{\log|L|}{\log\Delta}.

###### Proof.

Let ( V, ⪯) (V,\preceq) be the partial order generated by 𝒳 \mathcal{X}. We prove the lemma by induction on | L | |L|. As a base case, let | L | ∈ [2, Δ] |L|\in[2,\Delta]. Pick any two leaves in L L, and note that they are connected by a path P 1 P_{1} in S S and a path P 2 P_{2} in T T. Then, P 1 ∪ P 2 P_{1}\cup P_{2} is a good cycle, so that | 𝒞 1 ​ ( S ∪ T) | ≥ 1 ≥ log ⁡ | L | log ⁡ Δ |\mathcal{C}_{1}(S\cup T)|\geq 1\geq\frac{\log|L|}{\log\Delta}.

Assume that the lemma holds for | L | ≤ t − 1 |L|\leq t-1 and consider the case | L | = t > Δ |L|=t>\Delta. Let u u and v v be the roots of S S and T T respectively. Let r 1, …, r Δ ′ r_{1},\dots,r_{\Delta^{\prime}} ( Δ ′ ≤ Δ \Delta^{\prime}\leq\Delta) be the neighbours of u u in S S. Observe that for some i ∈ [Δ ′] i\in[\Delta^{\prime}] the subtree S ′ S^{\prime} rooted at r i r_{i} obtained by deleting u u from S S contains at least | L | / Δ ≥ 2 |L|/\Delta\geq 2 leaves distinct from r i r_{i}. Let u 0 u_{0} be maximal under ⪯ \preceq such that u 0 u_{0} is contained in every path from r i r_{i} to L ⁡ ( S ′) L(S^{\prime}) in S S. Let S 0 S_{0} be the unique subtree of S ′ S^{\prime} whose leaf set is precisely L 0:= L ⁡ ( S ′) L_{0}:=L(S^{\prime}), then S 0 S_{0} is a fair forward-directed tree rooted at u 0 u_{0} with | L 0 | ≥ | L | / Δ |L_{0}|\geq|L|/\Delta. Let T 0 ⊆ T T_{0}\subseteq T be the unique backward-directed subtree of T T with L ⁡ ( T 0) = L 0 L(T_{0})=L_{0}. Letting v 0 v_{0} be the minimal vertex under ⪯ \preceq that is on every path from v v to L 0 L_{0} in T T, we view T 0 T_{0} as rooted at v 0 v_{0}, so that T 0 T_{0} is also fair.

By the inductive hypothesis applied to L 0 L_{0}, S 0 S_{0} and T 0 T_{0}, we have

 | | 𝒞 1 ​ ( S 0 ∪ T 0) | ≥ log ⁡ | L 0 | log ⁡ Δ ≥ log ⁡ | L | log ⁡ Δ − 1. |\mathcal{C}_{1}(S_{0}\cup T_{0})|\geq\frac{\log|L_{0}|}{\log\Delta}\geq\frac{\log|L|}{\log\Delta}-1. |  |

Let d S, d T ≥ 1 d_{S},d_{T}\geq 1 satisfy d S ​ ( u, w) = d S d_{S}(u,w)=d_{S} and d T ​ ( v, w) = d T d_{T}(v,w)=d_{T} for each w ∈ L w\in L. Any cycle contained in S 0 ∪ T 0 S_{0}\cup T_{0} is of length at most 2 ​ d S + 2 ​ d T − 2 2d_{S}+2d_{T}-2. Therefore, to complete the proof it suffices to show that there exists a good cycle in S ∪ T S\cup T containing u u and v v, which must have length precisely 2 ​ d S + 2 ​ d T 2d_{S}+2d_{T}.

Suppose otherwise. By our choice of L 0 L_{0}, every subpath of S S connecting L 0 L_{0} and L ∖ L 0 L\setminus L_{0} must contain u u. So, we may assume that every subpath in T T connecting L 0 L_{0} and L ∖ L 0 L\setminus L_{0} avoids v v. Let r 1 ′, …, r Δ ′′ ′ r^{\prime}_{1},\dots,r^{\prime}_{\Delta^{\prime\prime}} ( Δ ′′ ≤ Δ \Delta^{\prime\prime}\leq\Delta) be the neighbours of v v in T T, and let T i T_{i} ( i ∈ [Δ ′′] i\in[\Delta^{\prime\prime}]) be the subtree of T T containing r i ′ r^{\prime}_{i} after deleting v v. If there are distinct i, j ∈ [Δ ′′] i,j\in[\Delta^{\prime\prime}] such that L 0 ∩ V ⁡ ( T i) L_{0}\cap V(T_{i}) and ( L ∖ L 0) ∩ V ⁡ ( T j) (L\setminus L_{0})\cap V(T_{j}) are non-empty, then we obtain a path from L L to L ∖ L 0 L\setminus L_{0} in T T containing v v (passing through r i ′ r^{\prime}_{i} and r j ′ r^{\prime}_{j}), giving a contradiction. Thus, there is some i ∈ [Δ ′′] i\in[\Delta^{\prime\prime}] such that L = L 0 ∪ ( L ∖ L 0) ⊆ V ⁡ ( T i) L=L_{0}\cup(L\setminus L_{0})\subseteq V(T_{i}), which is only possible if d T ​ ( v) = 1 d_{T}(v)=1, contradicting the fact that T T is a backward-directed tree.

Hence, there exists a good cycle in S ∪ T S\cup T containing u u and v v. This cycle is necessarily of length 2 ​ d S + 2 ​ d T 2d_{S}+2d_{T}, and thus

 | | 𝒞 1 ​ ( S ∪ T) | ≥ | 𝒞 1 ​ ( S 0 ∪ T 0) | + 1 ≥ log ⁡ | L | log ⁡ Δ, |\mathcal{C}_{1}(S\cup T)|\geq|\mathcal{C}_{1}(S_{0}\cup T_{0})|+1\geq\frac{\log|L|}{\log\Delta}, |  |

which completes the proof. ∎

Finally, we are ready to complete the proof of Theorem 12.

###### Proof of Theorem 12.

Suppose the maximum length of a forward path in G G is c − 1 c-1. By Lemma 13, | 𝒞 G | ≥ log ⁡ c − 1 |\mathcal{C}_{G}|\geq\log c-1. Hence if n < 2 ​ c 3 n<2c^{3}, we have | 𝒞 G | ≥ log ⁡ n − 4 3 > log ⁡ n 3 + log ⁡ k − 2 |\mathcal{C}_{G}|\geq\frac{\log n-4}{3}>\frac{\log n}{3+\log k}-2. Consider the case n ≥ 2 ​ c 3 n\geq 2c^{3}. Applying Lemma 16, we obtain L ⊆ V L\subseteq V, a fair forward-directed subtree S S and a fair backward-directed subtree T T of G G, satisfying L ⁡ ( S) = L ⁡ ( T) = L L(S)=L(T)=L and | L | ≥ n c 3 ≥ 2 |L|\geq\frac{n}{c^{3}}\geq 2. Since ( G, 𝒳) (G,\mathcal{X}) is k k -ordered, S S has maximum degree at most k k. From Lemma 17, it follows that

 | | 𝒞 G | ≥ | 𝒞 1 ​ ( S ∪ T) | ≥ log ⁡ | L | log ⁡ k ≥ log ⁡ n − 3 ​ log ⁡ c log ⁡ k. |\mathcal{C}_{G}|\geq\big|\mathcal{C}_{1}(S\cup T)\big|\geq\frac{\log|L|}{\log k}\geq\frac{\log n-3\log c}{\log k}. |  |

Now we complete the proof by deducing that

 | | 𝒞 G | \displaystyle\big|\mathcal{C}_{G}\big| | ≥ min c > 0 ⁡ max ⁡ { log ⁡ c − 1, log ⁡ n − 3 ​ log ⁡ c log ⁡ k } = log ⁡ n − 3 3 + log ⁡ k, \displaystyle\geq\min_{c>0}\max\left\{\log c-1,\frac{\log n-3\log c}{\log k}\right\}=\frac{\log n-3}{3+\log k}, |  |

where max ⁡ { log ⁡ c − 1, log ⁡ n − 3 ​ log ⁡ c log ⁡ k } \max\left\{\log c-1,\frac{\log n-3\log c}{\log k}\right\} achieves its minimum when log ⁡ c = log ⁡ n + log ⁡ k 3 + log ⁡ k \log c=\frac{\log n+\log k}{3+\log k}. ∎

Theorem 1 promptly follows by setting k = 3 k=3 and combining Lemma 11 with Theorem 12.

## 5 Conclusion and open problems

In this paper, we answered several questions of Narins, Pokrovskiy and Szabó [18] on lengths of cycles in degree-critical graphs and leaf-to-leaf paths in trees. We have proven B and disproven C, but several questions still remain. The most obvious one would be to improve the leading coefficient of the bound we prove in Theorem 1 and completely settle A.

Another interesting question is to determine ‘how far’ C is from being true, i.e. find the value of the best possible constant c c in Theorem 3.

###### Problem D.

Determine the supremum c ∗ c^{*} over all c ∈ [0, 1] c\in[0,1] for which the following holds: for all N N and all sufficiently large even n n (as a function of N N and c c), every n n -vertex 1–3 tree contains leaf-to-leaf paths of Ω ⁡ ( N c) \Omega(N^{c}) distinct lengths between 0 0 and N N.

We do not have a guess for what the true value of c ∗ c^{*} should be. Theorem 4 shows that c ∗ ≥ 2 / 3 c^{*}\geq 2/3. In the proof of Theorem 4, however, we could only obtain leaf-to-leaf paths which are all witnessed by the same leaf, and Theorem 5 shows that our bound in this setting is essentially best possible. It is natural to attempt and improve this lower bound on c ∗ c^{*} by sharpening the bound in Lemma 9, i.e. improving on the lower bound c ′ ≥ 2 / 3 c^{\prime}\geq 2/3 in the setting below.

###### Problem E.

Determine the supremum c ′ c^{\prime} over all c ∈ [0, 1] c\in[0,1] for which the following holds: for all sufficiently large n n and all sequences ( a i) i = 1 n (a_{i})_{i=1}^{n} of non-negative integers such that a i ≤ n c a_{i}\leq n^{c}, we have

 | | { a i + a j + ( j − i): 1 ≤ i < j ≤ n } | = Ω ⁡ ( n c). |\{a_{i}+a_{j}+(j-i):1\leq i<j\leq n\}|=\Omega\left(n^{c}\right). |  |

On the other hand, Theorem 3 shows that c ∗ ≤ ( 2 − log ⁡ 10 log ⁡ 13) − 1 ≈ 0.9073 c^{*}\leq\left(2-\frac{\log 10}{\log 13}\right)^{-1}\approx 0.9073, and a straightforward application of the Ruzsa triangle inequality shows that our proof method cannot improve this beyond 0.75 0.75 (more specifically, it is proven in [20] that one has | U + V | ≥ | U − V | 2 / 3 |U+V|\geq|U-V|^{2/3} for any U, V ⊆ ℤ U,V\subseteq\mathbb{Z}, so we cannot take β < 2 / 3 \beta<2/3 in Proposition 10).

As a related problem, it would be interesting to determine the optimal value of β \beta that one could take in Proposition 10. We remark that even the more basic question of determining how small A + B A+B can be relative to A − B A-B for A, B ⊆ ℕ A,B\subseteq\mathbb{N} seems to be wide open – the best bound we are aware of is the construction of Cutler, Pebody, and Sarkar [7] which gives | A + A | ≤ | A − A | 0.868. |A+A|\leq|A-A|^{0.868}.

Lastly, let us mention one more problem stated in [18].

###### Problem F (​​ [18, Problem 6.1]).

Is there a function C ⁡ ( n) C(n) tending to infinity such that every degree 3-critical graph on n n vertices contains cycles of all lengths 4, 6, 8, …, 2 ​ C ​ ( n) 4,6,8,...,2C(n)?

The tools used in the present paper seem insufficient to be able to answer this, and we do not speculate on what the answer might be.

## Acknowledgements

We thank the anonymous referees for their careful reading of this paper and their valuable comments. We would also like to thank Jozef Skokan for a careful reading of a preliminary version of this manuscript.

## References

- [1] D. Bauer and E. Schmeichel (1990) Hamiltonian degree conditions which imply a graph is pancyclic. Journal of Combinatorial Theory, Series B 48 ( 1), pp. 111–116. Cited by: §1.
- [2] B. Bollobás and G. Brightwell (1989) Long cycles in graphs with no subgraphs of minimal degree 3. In Annals of Discrete Mathematics, Vol. 43, pp. 47–53. Cited by: §1, §1, §1, §4.
- [3] B. Bollobás (1998) Modern graph theory. Graduate Texts in Mathematics, Vol. 184, Springer, New York. Cited by: §1.1.
- [4] J. A. Bondy and S. C. Locke (1981) Relative lengths of paths and cycles in 3-connected graphs. Discrete Mathematics 33 ( 2), pp. 111–122. Cited by: §4.
- [5] J. A. Bondy (1971) Pancyclic graphs I. Journal of Combinatorial Theory, Series B 11 ( 1), pp. 80–84. Cited by: §1.
- [6] M. Bucić, L. Gishboliner, and B. Sudakov (2022) Cycles of many lengths in Hamiltonian graphs. Forum of Mathematics, Sigma 10, pp. e70. External Links: [Document][3] Cited by: §1.
- [7] J. Cutler, L. Pebody, and A. Sarkar (2024) Sums, Differences and Dilates. arXiv preprint arXiv:2402.18297. Cited by: §5.
- [8] R. P. Dilworth (1950) A decomposition theorem for partially ordered sets. Annals of Mathematics 51 ( 1), pp. 161–166. External Links: ISSN 0003486X, 19398980, [Link][4] Cited by: Theorem 14.
- [9] N. Draganić, D. M. Correia, and B. Sudakov (2024) Pancyclicity of Hamiltonian graphs. Journal of the European Mathematical Society. Cited by: §1.
- [10] P. Erdős, R. J. Faudree, A. Gyárfás, and R. H. Schelp (1988) Cycles in graphs without proper subgraphs of minimum degree 3. Ars Combinatorica 25, pp. 195–201. Cited by: §1, §1, §1, §4.
- [11] P. Erdős and G. Szekeres (1935) A combinatorial problem in geometry. Compositio Mathematica 2, pp. 463–470. Cited by: Theorem 8.
- [12] P. Erdős (1991) Problems and results in combinatorial analysis and combinatorial number theory. Graph theory, combinatorics, and applications Vol. 1 (Kalamazoo, MI, 1988), pp. 397–406. Cited by: §1.
- [13] P. Erdős (1993) Some of my favorite solved and unsolved problems in graph theory. Quaestiones Mathematicae 16 ( 3), pp. 333–350. Cited by: §1.
- [14] A. Gyárfás, J. Komlós, and E. Szemerédi (1984) On the distribution of cycle lengths in graphs. Journal of Graph Theory 8 ( 4), pp. 441–462. Cited by: §1.
- [15] A. Gyárfás and J. Lehel (1970) A Helly-type problem in trees. In Combinatorial theory and its applications, I-III (Proceedings of the Colloquium held at Balatonfüred, 1969), Colloquia Mathematica Societatis János Bolyai, Vol. 4, pp. 571–584. External Links: [MathReview (Branko Grunbaum)][5] Cited by: §2.1.
- [16] W. A. Horn (1972) Three results for trees, using mathematical induction. Journal of Research of the National Bureau of Standards 76B, pp. 39–43. Cited by: §2.1.
- [17] S. Letzter (2023) Pancyclicity of highly connected graphs. arXiv preprint arXiv:2306.12579. Cited by: §1.
- [18] L. Narins, A. Pokrovskiy, and T. Szabó (2017) Graphs without proper subgraphs of minimum degree 3 and short cycles. Combinatorica 37, pp. 495–519. Cited by: §1, §1, §1, §1, §1, §2.2, §5, §5, Conjecture A, Conjecture B, Conjecture C, Problem F.
- [19] C. St. J. A. Nash-Williams (1964) Decomposition of finite graphs into forests. Journal of the London Mathematical Society s1-39 ( 1), pp. 12–12. External Links: [Document][6], [Link][7], https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/jlms/s1-39.1.12 Cited by: §1.
- [20] I. Ruzsa (1996) Sums of finite sets. In Number Theory: New York Seminar, D.V. Chudnovsky, G.V. Chudnovsky, and M.B. Nathanson (Eds.), Cited by: §3.2, §5.
- [21] L. Sauermann (2019) A proof of a conjecture of Erdős, Faudree, Rousseau and Schelp on subgraphs of minimum degree k k. Journal of Combinatorial Theory, Series B 134, pp. 36–75. Cited by: §1.
- [22] B. Sudakov and J. Verstraëte (2008) Cycle lengths in sparse graphs. Combinatorica 28 ( 3), pp. 357–372. Cited by: §1.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://dx.doi.org/10.1017/fms.2022.42
[4]: http://www.jstor.org/stable/1969503
[5]: https://www.ams.org/mathscinet-getitem?mr=298550
[6]: https://dx.doi.org/https%3A//doi.org/10.1112/jlms/s1-39.1.12
[7]: https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms/s1-39.1.12
