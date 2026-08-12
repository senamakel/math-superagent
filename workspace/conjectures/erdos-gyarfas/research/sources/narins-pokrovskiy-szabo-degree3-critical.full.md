<!-- source: https://ar5iv.labs.arxiv.org/html/1408.5289 | converted from HTML -->

[1408.5289] Graphs without proper subgraphs of minimum degree 3 and short cycles

# Graphs without proper subgraphs of minimum degree 3 and short cycles

Lothar Narins Thanks: Research supported by the Research Training Group Methods for Discrete Structures and the Berlin Mathematical School. Alexey Pokrovskiy Thanks: Research supported by the Research Training Group Methods for Discrete Structures. Tibor Szabó Thanks: Research partially supported by DFG within the Research Training Group Methods for Discrete Structures. Affiliation: Department of Mathematics, Affiliation: Freie Universität, Affiliation: Berlin, Germany.

###### Abstract

We study graphs on n n vertices which have 2 ​ n − 2 2n-2 edges and no proper induced subgraphs of minimum degree 3 3. Erdős, Faudree, Gyárfás, and Schelp conjectured that such graphs always have cycles of lengths 3, 4, 5, …, C ⁡ ( n) 3,4,5,\dots,C(n) for some function C ⁡ ( n) C(n) tending to infinity. We disprove this conjecture, resolve a related problem about leaf-to-leaf path lengths in trees, and characterize graphs with n n vertices and 2 ​ n − 2 2n-2 edges, containing no proper subgraph of minimum degree 3 3.

## 1 Introduction

A simple exercise in graph theory is to show that every graph G G with n n vertices and at least 2 ​ n − 2 2n-2 edges must have an induced subgraph with minimum degree 3 3. Moreover, this statement is best possible: there are several constructions with 2 ​ n − 3 2n-3 edges which do not have this property. So every graph with n n vertices and 2 ​ n − 2 2n-2 edges must contain an induced subgraph with minimum degree 3 3, however this subgraph might be the whole graph. A subgraph H H of G G is called proper if H ≠ G H\neq G. See Figure 1 for two examples of graphs with 2 ​ | G | − 2 2|G|-2 edges but no proper induced subgraphs of minimum degree 3 3. The first of these, has an even stronger property—it has no proper induced or non-induced subgraphs with minimum degree 3 3. On the other hand, the second example has a proper non-induced subgraph with minimum degree 3 3 formed by removing the edge between the two vertices of degree 4 4.

Figure 1: Two examples of graphs on 6 6 vertices with 10 10 edges and no proper induced subgraphs with minimum degree 3 3.

In this paper we will study graphs with n n vertices 2 ​ n − 2 2n-2 edges which have no proper induced subgraphs with minimum degree 3 3. Following Bollobás and Brightwell [2] we call such graphs degree 3 3 -critical. It is easy to see that graphs with n n vertices and at least 2 ​ n − 1 2n-1 edges contain a proper degree 3 3 -critical subgraph. Erdős (cf [4]) conjectured that they should contain a degree 3 3 -critical subgraph not only on at most n − 1 n-1, but on at most ( 1 − ϵ) ​ n (1-\epsilon)n vertices, for some constant ϵ > 0 \epsilon>0. Degree 3 3 -critical graphs are closely related to several other interesting classes of graphs. For example, they have the property that all their proper subgraphs are 2-degenerate (where a graph is defined to be 2 2 -degenerate if it has no subgraph of minimum degree 3 3). Also notice that degree 3 3 -critical graphs certainly have no proper subgraphs H H with 2 ​ | H | − 2 2|H|-2 edges. Graphs with 2 ​ n − 2 2n-2 edges and no proper subgraphs H H with 2 ​ | H | − 2 2|H|-2 edges have a number of interesting properties. They are rigidity circuits: by a theorem of Laman, removing any edge from such a graph produces a graph H H which is *minimally rigid in the plane*, i.e., any embedding of it into the plane where the vertices are substituted by joints and the edges by rods produces a rigid structure, but no proper subgraph of H H has this property. Furthermore, by a special case of a theorem of Nash-Williams these graphs are exactly the ones that are the union of two disjoint spanning trees and Lehman’s Theorem characterizes them as the minimal graphs to win the so-called connectivity game on. That is, with two players alternately occupying the edges of G G, the player playing second is able to occupy a spanning tree.

The study of degree 3 3 -critical graphs was initiated by Erdős, Faudree, Gyárfás, and Schelp [3], where they investigated the possible cycle lengths. They showed that degree 3 3 -critical graphs on n ≥ 5 n\geq 5 vertices always contain a cycle of length 3 3, 4 4, and 5 5, as well as a cycle of length at least ⌊ log 2 ⁡ n ⌋ \lfloor\log_{2}n\rfloor, but not necessarily of length more than n \sqrt{n}. Bollobás and Brightwell [2] resolved asymptotically the question of how short the longest cycle length in degree 3 3 -critical graphs can be. They showed that every degree 3 3 -critical graph contains a cycle of length at least 4 ​ log 2 ​ n − o ⁡ ( log ⁡ n) 4\log_{2}n-o(\log n) and constructed degree 3 3 -critical graphs with no cycles of length more than 4 ​ log 2 ​ n + O ⁡ ( 1) 4\log_{2}n+O(1). Erdős, et al. [3] made the following conjecture about possible cycle lengths in degree 3 3 -graphs.

###### Conjecture 1.1 (Erdős, Faudree, Gyárfás, and Schelp, [3]).

There is an increasing function C ⁡ ( n) C(n) such that the following holds such that every degree 3 3 -critical graph on n n vertices contains all cycles of lengths 3, 4, 5, 6, …, C ⁡ ( n) 3,4,5,6,\dots,C(n).

A historical remark must be made here. The exact phrasing of Conjecture 1.1 in [3] is not quite what is stated above. In [3] first a class of graphs, G ∗ ​ ( n, m) G^{*}(n,m), is defined as “the set of graphs with n n vertices, m m edges, and with the property that no proper subgraph has minimum degree 3 3.” Then Conjecture 1.1 is stated as “If G ∈ G ∗ ​ ( n, 2 ​ n − 2) G\in G^{*}(n,2n-2), then G G contains all cycles of length at most k k where k k tends to infinity.” Notice that the word “induced” is not present in the original formulation. However a careful reading of [3] shows that in that paper “proper subgraph” implicitly must mean “proper induced subgraph”. Indeed many of the constructions given in [3] (such as Examples 1, 2, 3, 5, and 6 on pages 197-201) of graphs which have “no proper subgraphs of minimum degree 3 3 ” actually do have proper non-induced subgraphs with minimum degree 3 3. In addition, one can check that all the results and proofs given in [3] concerning graphs with “no proper subgraphs of minimum degree 3 3 ” hold also for graphs with “no proper induced subgraphs of minimum degree 3 3 ”. Therefore, it is plausible to assume that the word “induced” should be present in the statement of Conjecture 1.1. This also coincides with the interpretation of the concept in the paper of Bollobás and Brightwell [2].

Consequently throughout most of this paper will study Conjecture 1.1 as it is stated above. However, for the sake of completeness, in Section 4 we will diverge and consider the special case of Conjecture 1.1 when G G contains neither induced nor non-induced subgraphs with minimum degree 3 3.

The main result of this paper is a disproof of Conjecture 1.1. We prove the following.

###### Theorem 1.2.

There is an infinite sequence of degree 3 3 -critical graphs ( G n) n = 1 ∞ (G_{n})_{n=1}^{\infty} which do not contain a cycle of length 23 23.

In the process of proving this theorem, we will naturally arrive to a question of independent interest, concerning the various leaf-leaf path lengths (i.e., the lengths of paths going between two leaves) that must occur in a tree. Obviously, if T T is just a path, then T T only has a single leaf-leaf path. However if T T has no degree 2 2 vertices, then one would expect T T to have many different leaf-leaf path lengths. Of particular relevance to Conjecture 1.1 will be even 1 1 - 3 3 trees. A tree is called *even*if all of its leaves are in the same class of the tree’s unique bipartition and a tree is called a 1 1 - 3 3 -tree if every vertex has degree 1 1 or 3 3. On our way towards the proof of Theorem 1.2 we determine the smallest even number which does not occur as a leaf-leaf path in every even 1 1 - 3 3 -tree.

###### Theorem 1.3.

1. (i)

There is an integer N 0 N_{0} such that every even 1 1 - 3 3 tree T T with | T | ≥ N 0 |T|\geq N_{0} contains leaf-leaf paths of lengths 0, 2, 4, …, 18 0,2,4,\dots,18.

2. (ii)

There is an infinite family of even 1 1 - 3 3 trees ( T n) n = 1 ∞ (T_{n})_{n=1}^{\infty}, such that T n T_{n} contains no leaf-leaf path of length 20 20.

Part ( i ​ i) (ii) of Theorem 1.3 will be used to construct our counterexample to Conjecture 1.1, while part ( i) (i) shows that our method, as is, can not deliver a stronger counterexample. Hence it would be interesting to determine the shortest cycle length which is not present in every sufficiently large degree 3 3 -critical graph. Theorem 1.2 shows that this number is at most 23 23, while Erdős et al. [3] showed that it is at least 6 6. They also mention that their methods could be extended to work for 7 7. In Section 5 we verify their statement, by giving a short proof that every degree 3 3 -critical graph must contain C 6 C_{6}.

Finally, we revisit Conjecture 1.1 with the word “induced” removed from the definition of degree 3 3 -critical. We characterize all n n -vertex graph with 2 ​ n − 2 2n-2 edges and no proper (not necessarily induced) subgraph with minimum degree 3 3 and show that the conjecture is true for them in a much stronger form.

###### Theorem 1.4.

Let G G be a graph with n n vertices, 2 ​ n − 2 2n-2 edges and no proper subgraph with minimum degree 3 3. Then G G is pancyclic, that is, it contains cycles of length i i for every i = 3, 4, 5, …, i=3,4,5,\dots, and n n.

Theorem 1.4 will follow from a structure theorem which we shall prove about graphs with n n vertices, 2 ​ n − 2 2n-2 edges and no proper (not necessarily induced) subgraphs with minimum degree 3 3. It will turn out that there are only two particular families of graphs satisfying these conditions. One of them is the family of wheels and the other is a family of graphs obtained from a wheel by replacing one of its edges with a certain other graph.

The structure of this paper is as follows. In Section 2 we construct our counterexamples to Conjecture 1.1 via proving part ( i ​ i) (ii) of Theorem 1.3 and Theorem 1.2. In Section 3 we study necessary leaf-leaf path lengths in even 1 1 - 3 3 trees and prove part ( i) (i) Theorem 1.3. In Section 4 we prove the weakening of Conjecture 1.1 when the word “induced” is removed from the definition. In Section 5 we show that degree 3 3 -critical graphs on at least 6 6 vertices always contain a six-cycle. In Section 6 we make some concluding remarks and pose several interesting open problems raised naturally by our results. Our notation follows mostly that of [1].

## 2 Counterexample to Conjecture 1.1

The goal of this section is to prove Theorem 1.2. First we need some preliminary results about 1-3 trees.

Given a tree T T, define G ⁡ ( T) G(T) to be the graph formed from T T by adding two new vertices x x and y y, the edge x ​ y xy as well as every edge between { x, y } \{x,y\} and the leaves of T T. See Figure 2 for an example of a graph G ⁡ ( T) G(T).

Notice that if T T is a 1 1 - 3 3 tree then G ⁡ ( T) G(T) is degree 3 3 -critical. In the case when T T is an even 1 1 - 3 3 tree, the cycles of G ⁡ ( T) G(T) have nice properties.

x x y y T T Figure 2: The graph G ⁡ ( T) G(T) for an even 1 1 - 3 3 tree T T.

###### Lemma 2.1.

Let T T be an even 1 1 - 3 3 -tree. Then the following hold:

1. (i)

The graph G ⁡ ( T) G(T) contains a cycle of length 2 ​ k + 1 2k+1 ⇔ \iff T T contains a leaf-leaf path of length 2 ​ k − 2 2k-2.

2. (ii)

The graph G ⁡ ( T) G(T) contains a cycle of length 2 ​ k 2k ⇔ \iff T T contains two vertex-disjoint leaf-leaf paths P 1 P_{1} and P 2 P_{2} such that e ⁡ ( P 1) + e ⁡ ( P 2) = 2 ​ k − 4 e(P_{1})+e(P_{2})=2k-4 or T T contains a leaf-leaf path of length 2 ​ k − 2 2k-2.

###### Proof.

For (i), let C C be a ( 2 ​ k + 1) (2k+1) -cycle in G ⁡ ( T) G(T). Notice that since T T is an even tree, G ⁡ ( T) − x ​ y G(T)-xy is bipartite. So C C must contain the edge x ​ y xy and hence C − x − y C-x-y must be a leaf-leaf path of length 2 ​ k − 2 2k-2 as required. For the converse, notice that any path P ⊆ T P\subseteq T of length ℓ \ell between leaves u 1 u_{1} and u 2 u_{2} can be turned into a cycle of length ℓ + 3 \ell+3 by adding the vertices x x and y y as well as the edges u 1 ​ x, x ​ y, y ​ u 2 u_{1}x,xy,yu_{2} of G ⁡ ( T) G(T).

For (ii), let C C now be a 2 ​ k 2k -cycle in G ⁡ ( T) G(T). If | C ∩ { x, y } | = 1 |C\cap\{x,y\}|=1 then C − x − y C-x-y is a leaf-leaf path in T T of length 2 ​ k − 2 2k-2. Now suppose that both x, y ∈ V ⁡ ( C) x,y\in V(C). Notice that since T T is even, all leaf-leaf paths in T T have even length. Therefore, all cycles containing the edge x ​ y xy in G ⁡ ( T) G(T) must have odd length, and hence C C does not contain x ​ y xy. Thus C − x − y C-x-y consists of two vertex-disjoint leaf-leaf paths P 1, P 2 ⊆ T P_{1},P_{2}\subseteq T such that their lengths sum to 2 ​ k − 4 2k-4, as required. For the converse, first notice that any leaf-leaf path P ⊆ T P\subseteq T of length ℓ \ell can be turned into a cycle of length ℓ + 2 \ell+2 in G ⁡ ( T) G(T) by adding the vertex x x and the edges between the endpoints of P P and x x. Also, any two vertex-disjoint leaf-leaf paths P 1 ⊆ T P_{1}\subseteq T of length ℓ 1 \ell_{1} with endpoints u 1, w 1 u_{1},w_{1} and P 2 ⊆ T P_{2}\subseteq T of length ℓ 2 \ell_{2} with endpoints u 2 u_{2} and w 2 w_{2} can be turned into a cycle of length ℓ 1 + ℓ 2 + 4 \ell_{1}+\ell_{2}+4 in G ⁡ ( T) G(T) by adding the vertices x x and y y, and the edges u 1 ​ x, x ​ u 2, w 2 ​ y u_{1}x,xu_{2},w_{2}y, and y ​ w 1 yw_{1} of G ⁡ ( T) G(T). ∎

We say that a rooted binary tree T T is *perfect*if all non-leaf vertices have two children and all root-leaf paths have the same length d d (or, alternatively if | V ⁡ ( T) | = 2 d + 1 − 1 |V(T)|=2^{d+1}-1 where d d is the depth of T T). Given a sequence of positive integers x 1, …, x n x_{1},\dots,x_{n}, we define a tree T ⁡ ( x 1 ​ … ​ x n) T(x_{1}\dots x_{n}) as follows. First consider a path on n n vertices with vertex sequence v 1, …, v n v_{1},\dots,v_{n}. For each i i satisfying 2 ≤ i ≤ n − 1 2\leq i\leq n-1, add a perfect rooted binary tree T i T_{i} of depth x i − 1 x_{i}-1 with root vertex u i u_{i}. For i = 1 i=1 and n n add two perfect rooted binary trees each: trees T 1 ( 1) T^{(1)}_{1} and T 1 ( 1) T^{(1)}_{1} of depths x 1 − 1 x_{1}-1 with root vertices u 1 ( 1) u^{(1)}_{1} and u 1 ( 2) u^{(2)}_{1}, respectively and trees T n ( 1) T^{(1)}_{n} and T n ( 1) T^{(1)}_{n} of depths x n − 1 x_{n}-1 with root vertices u n ( 1) u^{(1)}_{n} and u n ( 2) u^{(2)}_{n}, respectively. Finally, for each i, 2 ≤ i ≤ n − 1 i,2\leq i\leq n-1, we add the edges v i ​ u i v_{i}u_{i}, as well as the edges v 1 ​ u 1 ( 1) v_{1}u^{(1)}_{1}, v 1 ​ u 1 ( 2) v_{1}u^{(2)}_{1}, v n ​ u n ( 1) v_{n}u^{(1)}_{n}, and v n ​ u n ( 2) v_{n}u^{(2)}_{n}. See Figure 3 for an example of a graph G ⁡ ( T) G(T).

Notice that for any sequence x 1, …, x n x_{1},\dots,x_{n} of positive integers, the tree T ⁡ ( x 1 ​ … ​ x n) T(x_{1}\dots x_{n}) is a 1 1 - 3 3 tree. We will mainly be concerned with odd-even sequences, that is, sequences for which x i ≡ i ( mod 2) x_{i}\equiv i\pmod{2} for all i i (that is, x i x_{i} is even ⇔ \iff i i is even). It turns out that for odd-even sequences the leaf-leaf path length of the tree T ⁡ ( x 1 ​ … ​ x n) T(x_{1}\dots x_{n}) are easy to characterize.

v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} Figure 3: The 1 1 - 3 3 tree T ⁡ ( 2, 3, 2, 3, 2) T(2,3,2,3,2).

###### Lemma 2.2.

Let x 1, …, x n x_{1},\dots,x_{n} be an odd-even sequence. Then we have the following:

1. (i)

The tree T ⁡ ( x 1 ​ … ​ x n) T(x_{1}\dots x_{n}) contains no leaf-leaf path of odd length. In particular, T ⁡ ( x 1, …, x n) T(x_{1},\ldots,x_{n}) is an even tree.

2. (ii)

For every integer m m, 0 ≤ m < max i = 1 n ​ x i 0\leq m<\max_{i=1}^{n}x_{i}, the tree T ⁡ ( x 1 ​ … ​ x n) T(x_{1}\dots x_{n}) contains a leaf-leaf path of length 2 ​ m 2m.

3. (iii)

For m = max i = 1 n ​ x i m=\max_{i=1}^{n}x_{i}, the tree T ⁡ ( x 1 ​ … ​ x n) T(x_{1}\dots x_{n}) contains a leaf-leaf path of length 2 ​ m 2m if and only if either max ⁡ { x 1, x n } = max i = 1 n ​ x i \max\{x_{1},x_{n}\}=\max_{i=1}^{n}x_{i} or there are two distinct integers i i and j j such that x i + x j + | i − j | = 2 ​ m x_{i}+x_{j}+|i-j|=2m.

4. (iv)

For every m > max i = 1 n ​ x i m>\max_{i=1}^{n}x_{i}, the tree T ⁡ ( x 1 ​ … ​ x n) T(x_{1}\dots x_{n}) contains a leaf-leaf path of length 2 ​ m 2m if and only if there are two distinct integers i i and j j such that x i + x j + | i − j | = 2 ​ m x_{i}+x_{j}+|i-j|=2m.

###### Proof.

Leaf-leaf paths of T ⁡ ( x 1, …, x n) T(x_{1},\ldots,x_{n}) can be classified based on their intersection with the path v 1, …, v n v_{1},\ldots,v_{n}. Note that this intersection is always a (potentially empty) path.

If the intersection is empty then the path is a leaf-leaf path of a perfect binary tree of depth x i − 1 x_{i}-1 for some i i, and hence its length is 2 ​ m 2m for some m m, 0 ≤ m < max i = 1 n ​ x i 0\leq m<\max_{i=1}^{n}x_{i}.

If the intersection is a single vertex, then this vertex must be either v 1 v_{1} or v n v_{n}. Then the path is a leaf-leaf path going through the root in one of the perfect binary trees on V ⁡ ( T 1 ( 1)) ∪ V ⁡ ( T 1 ( 2)) ∪ { v 1 } V(T^{(1)}_{1})\cup V(T^{(2)}_{1})\cup\{v_{1}\} and V ⁡ ( T n ( 1)) ∪ V ⁡ ( T n ( 2)) ∪ { v n } V(T^{(1)}_{n})\cup V(T^{(2)}_{n})\cup\{v_{n}\} of depths x 1 x_{1} and x n x_{n}, respectively, and hence its length is 2 ​ x 1 2x_{1} or 2 ​ x n 2x_{n}, respectively.

If the intersection is a segment v i, …, v j v_{i},\ldots,v_{j} for some 1 ≤ i < j ≤ n 1\leq i<j\leq n, then the path has length x i + j − i + x j x_{i}+j-i+x_{j}. This implies the “only if ” part of (iii) and (iv). Note also that all these paths have even length ( x i + j − i + x j x_{i}+j-i+x_{j} is even because ( x 1, …, x n) (x_{1},\ldots,x_{n}) is an odd-even sequence), and so (i) holds.

For (ii) and the “if” part of (iii) and (iv) one must only note that a perfect tree of depth d d contains a leaf-leaf path of every even length 0, 2, …, 2 ​ d 0,2,\dots,2d and hence all leaf-leaf path-lengths given by the classification can actually be realized. ∎

We now produce a sequence of integers ( x n) n = 1 ∞ (x_{n})_{n=1}^{\infty} such that for every n n, the tree T ⁡ ( x 1 ​ … ​ x n) T(x_{1}\dots x_{n}) will not have leaf-leaf paths of length 20 20.

### 2.1 k k -avoiding sequences

We will be concerned with two-sided sequences ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} of positive integers. Again, we say that such a sequence is an *odd-even sequence*if a i ≡ i ( mod 2) a_{i}\equiv i\pmod{2} for all i ∈ ℤ i\in\mathbb{Z}.

###### Definition 2.3.

Let k k be a positive even integer. A two-sided sequence ( x i) i ∈ ℤ ({x}_{i})_{i\in\mathbb{Z}} of positive integers is called *k k -avoiding*if a i ≤ k / 2 a_{i}\leq k/2 for all i ∈ ℤ i\in\mathbb{Z} and if for every i, j ∈ ℤ i,j\in\mathbb{Z}, i ≠ j i\neq j, we have a i + a j + | i − j | ≠ k a_{i}+a_{j}+\left|i-j\right|\neq k.

In order to check if an odd-even sequence ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} with a i ≤ k / 2 a_{i}\leq k/2 for all i ∈ ℤ i\in\mathbb{Z} is k k -avoiding, consider the graph { ( i, a i): i ∈ ℤ } \left\{(i,a_{i}):i\in\mathbb{Z}\right\} of the sequence. Call a point ( x, y) ∈ ℤ × [1, k / 2] (x,y)\in\mathbb{Z}\times[1,k/2]*in conflict*with another point ( z, w) ∈ ℤ × [1, k / 2] (z,w)\in\mathbb{Z}\times[1,k/2], ( z, w) ≠ ( x, y) (z,w)\neq(x,y), if y + w + | x − z | = k y+w+\left|x-z\right|=k. Notice that the points ( x, y) (x,y) in conflict with a fixed point ( c, d) (c,d) lie on the two diagonal lines y = − x + ( k + c − d) y=-x+(k+c-d) and y = x + ( k − c − d) y=x+(k-c-d). Since being in conflict is a symmetric relation we can say that we blame a conflict on the point with lower first coordinate (the first coordinates of points in conflict cannot be equal). Then the points ( x, y) ∈ ℤ × [1, k / 2] (x,y)\in\mathbb{Z}\times[1,k/2], whose conflicts with ( c, d) (c,d) are blamed on ( c, d) (c,d) lie on the single line y = − x + ( k + c − d) y=-x+(k+c-d). Indeed, the first coordinates of a point ( x, y) (x,y) on the other diagonal line is x = y − k + c + d ≤ k / 2 − k + c + k / 2 x=y-k+c+d\leq k/2-k+c+k/2 at most c c, hence these conflicts are not blamed on ( c, d) (c,d). We define the *fault line*of the point ( c, d) (c,d) to be the line y = − x + ( k + c − d) y=-x+(k+c-d). From the above discussion we obtain the following proposition.

###### Proposition 2.4.

A sequence ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} is k k -avoiding if, and only if, there do not exist two distinct indices i i and j j such that ( i, a i) (i,a_{i}) lies on the fault line of ( j, a j) (j,a_{j}).

It is useful to note that all the points on the line y = x + b y=x+b have the same fault line y = − x + b + k y=-x+b+k.

###### Theorem 2.5.

There is a 20 20 -avoiding odd-even sequence.

###### Proof.

Let ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} be the periodic sequence of period 24 24 consisting of repetitions of

 | …, 1, 2, 1, 4, 3, 2, 7, 6, 5, 6, 7, 2, 3, 4, 1, 2, 1, 8, 9, 6, 5, 6, 9, 8, …. \dots,1,2,1,4,3,2,7,6,5,6,7,2,3,4,1,2,1,8,9,6,5,6,9,8,\dots. |  |

We claim ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} is a 20 20 -avoiding odd-even sequence. It is clearly an odd-even sequence, and a i ≤ 10 = 20 / 2 a_{i}\leq 10=20/2 for all i ∈ ℤ i\in\mathbb{Z}. We prove that it is 20 20 -avoiding by showing that in the graph of this sequence, no point lies on the fault line of another point. Then Proposition 2.4 implies the theorem.

Figure 4 is a snapshot of two periods of the graph. The points on the graph are black circles, and the fault lines are drawn in red. Note that points on a line ℓ \ell parallel to the line “ x = y x=y ” have the same fault line, and that this fault line crosses ℓ \ell when the second coordinate is 10 10.

1 2 3 4 5 6 7 8 9 10 5 10 15 20 25 30 35 40 45 Figure 4: A snapshot of the graph of a periodic 20 20 -avoiding odd-even sequence.

From the picture we see that no point of the sequence lies on a fault line of another point, implying that ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} is indeed 20 20 -avoiding. ∎

We are now ready to prove part (ii) of Theorem 1.3 and Theorem 1.2.

###### Proof of part (ii) of Theorem 1.3.

Let x 1, …, x n x_{1},\dots,x_{n} be the first n n terms (starting at 1 1) of the 20 20 -avoiding sequence produced by Theorem 2.5. The tree T n = T ⁡ ( x 1 ​ … ​ x n) T_{n}=T(x_{1}\dots x_{n}) is a 1-3-tree for any sequence ( x 1, …, x n) (x_{1},\ldots,x_{n}) by construction. Since ( x 1, …, x n) (x_{1},\ldots,x_{n}) is an odd-even sequence, T n T_{n} is also an even tree by part (i) of Lemma 2.2. The tree T n T_{n} contains no leaf-leaf paths of length 20 20, since 20 > 2 ⋅ max ⁡ x i = 18 20>2\cdot\max x_{i}=18 and part (iv) of Lemma 2.2 tells us that a leaf-leaf path of length 20 20 exists only if there are distinct i i and j j such that x i + x j + | i − j | = 20 x_{i}+x_{j}+|i-j|=20, which is not case since x 1, …, x n x_{1},\ldots,x_{n} is 20 20 -avoiding. ∎

###### Proof of Theorem 1.2.

We let G n = G ⁡ ( T n) G_{n}=G(T_{n}) be the graph constructed from the tree T n T_{n} given by part (ii) of Theorem 1.3. Since T n T_{n} is a 1-3-tree, the graph G n G_{n} is degree 3 3 -critical, as required. Since T n T_{n} is an even 1-3-tree, we can use part (i) of Lemma 2.1 and the fact that T n T_{n} does not contain a leaf-leaf path of length 20 20 to conclude that G n G_{n} contains no cycle of length 23 23. ∎

## 3 Possible leaf-leaf path lengths in even 1 1 - 3 3 trees

In this section we prove part (i) of Theorem 1.3. We first need a lemma about possible lengths of leaf-leaf paths in binary trees which have no short root-leaf paths.

###### Lemma 3.1.

Let T T be an even rooted binary tree and let m m be the length of its shortest root-leaf path. Then T T contains leaf-leaf paths of lengths 0, 2, 4, …, 2 ​ m 0,2,4,\dots,2m.

###### Proof.

The proof is by induction on | V ⁡ ( T) | |V(T)|. The statement is certainly true for | V ⁡ ( T) | = 1 |V(T)|=1. Let now | V ⁡ ( T) | > 1 |V(T)|>1 and let x x and y y be the children of of the root r r.

Suppose first that in one of the subtrees T x T_{x} and T y ⊆ T T_{y}\subseteq T, rooted at x x and y y, respectively, the shortest root-leaf path is of length m m as well. In this case we can apply induction to this subtree and find in it a leaf-leaf paths of all length 0, 2, …, 2 ​ m 0,2,\ldots,2m. The leaf-leaf path of the subtree are of course leaf-leaf paths of T T, so we are done in this case.

Otherwise, the length of the shortest root-leaf path of both subtrees T x T_{x} and T y T_{y} are m − 1 m-1 (the subtrees cannot contain a shorter root-leaf path, because T T itself does not contain a root-leaf path shorter than m m). Then by induction there are leaf-leaf path of all length 0, 2, …, 2 ​ m − 2 0,2,\ldots,2m-2 in both of these subtrees and hence also in T T. To construct a leaf-leaf path of length 2 ​ m 2m in T T let P x P_{x} be a path between x x and a leaf of T T of length m − 1 m-1, and P y P_{y} be a path between y y and a leaf of T T of length m − 1 m-1. Then the path P x + r + P y P_{x}+r+P_{y} formed by joining P x P_{x} and P y P_{y} to r r using the edges r ​ x rx and r ​ y ry is a leaf-leaf path in T T of length 2 ​ m 2m. ∎

The following proposition shows that finding which leaf-leaf paths lengths always occur in sufficiently large trees is equivalent to finding the k k for which k k -avoiding sequences exist.

###### Proposition 3.2.

Let m m be a positive integer. The following are equivalent.

1. (i)

There is an integer N 0 ​ ( m) N_{0}(m) such that every even 1-3-tree of order at least N 0 ​ ( m) N_{0}(m) contains a leaf-leaf path of length 2 ​ m 2m.

2. (ii)

There exists no 2 ​ m 2m -avoiding odd-even sequence ( x n) n ∈ ℤ (x_{n})_{n\in\mathbb{Z}}.

###### Proof.

Let us assume first that (i) holds with integer N 0 ​ ( m) = N 0 N_{0}(m)=N_{0}. Let ( x n) n = 1 ∞ (x_{n})_{n=1}^{\infty} be an arbitrary odd-even sequence such that max i = 1 n ​ x i ≤ m \max_{i=1}^{n}x_{i}\leq m. Notice that since x i x_{i} is even if and only if i i is even, there are infinitely many indices a a for which x a < max i = 1 n ​ x i x_{a}<\max_{i=1}^{n}x_{i}. Therefore we can choose two indices a a and b b such that a − b ≥ N 0 a-b\geq N_{0} and x a x_{a}, x b < m x_{b}<m. Then by parts (iii) and (iv) of Lemma 2.2, the tree T ⁡ ( x a ​ … ​ x b) T(x_{a}\dots x_{b}) has a leaf-leaf path of length 2 ​ m 2m if and only if there are two distinct indices i i and j j such that x i + x j + | i − j | = 2 ​ m x_{i}+x_{j}+|i-j|=2m holds. On the other hand notice that by part (i) of Lemma 2.2, T ⁡ ( x a ​ … ​ x b) T(x_{a}\dots x_{b}) is an even 1-3 tree and hence, since its order is at least N 0 N_{0}, does have a leaf-leaf path of length 2 ​ m 2m. That is, there do exist indices i ≠ j i\neq j such that x i + x j + | i − j | = 2 ​ m x_{i}+x_{j}+|i-j|=2m holds, implying that ( x n) n = 1 ∞ (x_{n})_{n=1}^{\infty} is not 2 ​ m 2m -avoiding.

Now assume that (ii) holds. Let us define N 0 ​ ( m) = N 0 = 3 2 ⋅ 2 N 1 / 2 − 1 N_{0}(m)=N_{0}=\frac{3}{2}\cdot 2^{N_{1}/2}-1, where N 1 = m 2 ​ m + 2 ​ m N_{1}=m^{2m}+2m. Let T T be an arbitrary even 1 1 - 3 3 tree of order at least N 0 N_{0}. We will show that T T contains a leaf-leaf path of length 2 ​ m 2m. Since T T is a tree of maximum degree at most 3 3 on N 0 N_{0} vertices it must contain a path v 1, v 2, …, v N 1 v_{1},v_{2},\dots,v_{N_{1}} with N 1 N_{1} vertices. Let T i T_{i} be the subtree of T T consisting of the connected component of T − v i + 1 − v i − 1 T-v_{i+1}-v_{i-1} containing v i v_{i} and let x i x_{i} be the length of the shortest path from v i v_{i} to a leaf of T i T_{i}. Note that ( x i) i = 1 N 1 (x_{i})_{i=1}^{N_{1}} is an odd-even sequence, because T T is an even tree.

Suppose first that we have m < max i = 1 N 1 ​ x i m<\max_{i=1}^{N_{1}}x_{i}. Choose an index i i such that x i > m x_{i}>m holds and let T ′ = T i − v i T^{\prime}=T_{i}-v_{i}. Then T ′ T^{\prime} is a binary tree rooted at the neighbour of v i v_{i}, with no root-leaf paths shorter than m m, so Lemma 3.1 gives us a leaf-leaf path of length 2 ​ m 2m.

Suppose now that we have m ≥ max i = 1 N 1 ​ x i m\geq\max_{i=1}^{N_{1}}x_{i}. Since N 1 > m 2 ​ m + 2 ​ m − 1 N_{1}>m^{2m}+2m-1, the Pigeonhole Principle implies that there must be indices a < b a<b such that x a = x b, x a + 1 = x b + 1, …, x a + 2 ​ m − 1 = x b + 2 ​ m − 1 x_{a}=x_{b},x_{a+1}=x_{b+1},\dots,x_{a+2m-1}=x_{b+2m-1} all hold. Consider now the infinite periodic sequence

 | …, x a, x a + 1, …, x b − 1, x a, x a + 1, …, x b − 1, x a, …, \dots,x_{a},x_{a+1},\dots,x_{b-1},x_{a},x_{a+1},\dots,x_{b-1},x_{a},\dots, |  |

denoted by ( y i) i ∈ ℤ (y_{i})_{i\in\mathbb{Z}}. This is an odd-even sequence as the sequence ( x i) i = 1 N 1 (x_{i})_{i=1}^{N_{1}} was odd-even. By our assumption ( y i) i ∈ ℤ (y_{i})_{i\in\mathbb{Z}} is not 2 ​ m 2m -avoiding. But m ≥ max i = 1 n ​ x i = max i = 1 n ​ y i m\geq\max_{i=1}^{n}x_{i}=\max_{i=1}^{n}y_{i}, so there must be indices i ≠ j i\neq j such that y i + y j + | i − j | = 2 ​ m y_{i}+y_{j}+|i-j|=2m. Since the sequence is positive we must have | i − j | < 2 ​ m |i-j|<2m and by periodicity we can assume that a ≤ i < j ≤ b + 2 ​ m − 1 a\leq i<j\leq b+2m-1. The way we chose a a and b b ensures that x i = y i x_{i}=y_{i} for every i i between a a and b + 2 ​ m − 1 b+2m-1, so we also have x i + x j + | i − j | = 2 ​ m x_{i}+x_{j}+|i-j|=2m. We can now find a leaf-leaf path in T T of length 2 ​ m = x i + x j + | i − j | 2m=x_{i}+x_{j}+|i-j| by concatenating a shortest path from v i v_{i} to a leaf of T i T_{i}, the path between v i v_{i} and v j v_{j} and a shortest path from v j v_{j} to a leaf of T j T_{j}. ∎

We now proceed to prove part (i) of Theorem 1.3. We do this by showing that part (ii) of Proposition 3.2 holds for m ≤ 9 m\leq 9.

###### Theorem 3.3.

There is no 18 18 -avoiding odd-even sequence.

###### Proof.

Consider an odd-even sequence ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} with a i ≤ 9 a_{i}\leq 9 for all i ∈ ℤ i\in\mathbb{Z}. Assume that it is 18 18 -avoiding. As in the proof of Theorem 2.5, we will consider the graph of ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} and consider fault lines. In this case, the fault line of a point ( c, d) (c,d) is the line y = − x + ( 18 + c − d) y=-x+(18+c-d). Since ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} is 18 18 -avoiding, Proposition 2.4 implies that no point of the graph lies on the fault line of another point of the graph. Notice however, that a point of the form ( x, 9) (x,9), which by definition lies on its own fault line, is not itself a barrier to a sequence being 18 18 -avoiding.

We start with some lemmas about configurations of fault lines that lead to contradictions. We will actually deal with a slight generalization of fault lines, which we call *excluded lines*. An excluded line is defined to be any line of the form y = − x + b y=-x+b with b b even, that does not contain a point in the graph of ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}}, except possibly the point with second coordinate 9 9. Since ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} is an odd-even sequence, for any point ( i, a i) (i,a_{i}) in the graph of the sequence, the integer 18 + i − a i 18+i-a_{i} is even. Hence every fault line of the sequence is also an excluded line.

In the following discussion lines of slope − 1 -1 whose y y -intercepts differ by exactly 2 2 are called *consecutive*. We start with a trivial observation.

###### Lemma 3.4.

There cannot be four consecutive excluded lines for ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}}.

###### Proof.

If there were four excluded lines y = − x + b y=-x+b, y = − x + b + 2 y=-x+b+2, y = − x + b + 4 y=-x+b+4, and y = − x + b + 6 y=-x+b+6, where b b is even, then all of the points with even y y -coordinate at most 8 8 on the line x = b − 2 x=b-2 are on one of these lines. Hence ( b − 2, a b − 2) (b-2,a_{b-2}) would be on an excluded line, a contradiction.

1 2 3 4 5 6 7 8 9 b b

Figure 5: Four consecutive excluded lines and the contradiction they give.

∎

This easily leads to the next lemma.

###### Lemma 3.5.

There cannot be three consecutive excluded lines for ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}}.

###### Proof.

If there were three consecutive excluded lines y = − x + b y=-x+b, y = − x + b + 2 y=-x+b+2, and y = − x + b + 4 y=-x+b+4, where b b is even, then a b − 4 a_{b-4} must be equal to 2 2 as all the other even values at most 8 8 would put ( b − 4, a b − 4) (b-4,a_{b-4}) on one of the three lines. Similarly, we must have a b − 2 = 8 a_{b-2}=8, and hence we have fault lines y = − x + b + 8 y=-x+b+8 and y = − x + b + 12 y=-x+b+12. This forces a b − 1 = 7 a_{b-1}=7, giving also the fault line y = − x + b + 10 y=-x+b+10. Now a b − 3 a_{b-3} can only be 1 1 or 9 9 to avoid the original three fault lines, but it clearly cannot be 9 9, since that would put ( b − 2, 8) (b-2,8) on its fault line. But if a b − 3 = 1 a_{b-3}=1, then its fault line is y = − x + b + 14 y=-x+b+14, and there would be 4 4 consecutive fault lines y = − x + b + { 8, 10, 12, 14 } y=-x+b+\left\{8,10,12,14\right\}, contradicting Lemma 3.4.

1 2 3 4 5 6 7 8 9 b b

Figure 6: Three consecutive excluded lines and the contradiction they give.

∎

A few more lemmas of this sort will be useful for the proof.

###### Lemma 3.6.

There cannot be three excluded lines of the form y = − x + b y=-x+b, y = − x + b + 2 y=-x+b+2, and y = − x + b + 6 y=-x+b+6 (with b b even).

###### Proof.

If this were the case, then this would force a b − 2 = 6 a_{b-2}=6, which results in the fault line y = − x + b + 10 y=-x+b+10. If a b − 1 = 9 a_{b-1}=9, then there would be three consecutive excluded lines y = − x + b + { 6, 8, 10 } y=-x+b+\left\{6,8,10\right\}, which would contradict Lemma 3.5. This forces a b − 1 = 5 a_{b-1}=5, which results in the fault line y = − x + b + 12 y=-x+b+12. Similarly, in order to avoid a third consecutive fault line y = − x + b + 14 y=-x+b+14, we must have a b + 2 = 2 a_{b+2}=2 and a b + 5 = 3 a_{b+5}=3, resulting in the fault lines y = − x + b + 18 y=-x+b+18 and y = − x + b + 20 y=-x+b+20, respectively. This leaves us with no valid choices for a b + 6 a_{b+6}, since a value of 2 2 would create a third consecutive fault line y = − x + b + 22 y=-x+b+22, a value of 8 8 would create a third consecutive fault line y = − x + b + 16 y=-x+b+16, and a value of 4 4 or 6 6 would put ( b + 6, a b + 6) (b+6,a_{b+6}) on the fault line of a previous point. Therefore, this configuration cannot occur.

1 2 3 4 5 6 7 8 9 b b

Figure 7: A configuration of three excluded lines and the contradiction they give.

∎

###### Lemma 3.7.

There cannot be three excluded lines of the form y = − x + b y=-x+b, y = − x + b + 4 y=-x+b+4, and y = − x + b + 6 y=-x+b+6 (with b b even).

###### Proof.

If this were the case, then this would force a b − 2 = 4 a_{b-2}=4, which results in the fault line y = − x + b + 12 y=-x+b+12. If a b − 1 = 9 a_{b-1}=9, there would be three consecutive excluded lines y = − x + b + { 4, 6, 8 } y=-x+b+\{4,6,8\}, contradicting Lemma 3.5. So we must have a b − 1 = 3 a_{b-1}=3, resulting in the fault line y = − x + b + 14 y=-x+b+14 (the other values of a b − 1 a_{b-1} would put ( b − 1, a b − 1) (b-1,a_{b-1}) on an excluded line). If a b = 8 a_{b}=8, then we would have the configuration of fault lines y = − x + b + { 4, 6, 10 } y=-x+b+\left\{4,6,10\right\} forbidden by Lemma 3.6, so we must have a b = 2 a_{b}=2, resulting in the fault line y = − x + b + 16 y=-x+b+16. But then we have the three consecutive fault lines y = − x + b + { 12, 14, 16 } y=-x+b+\left\{12,14,16\right\}, also a contradiction.

1 2 3 4 5 6 7 8 9 b b

Figure 8: A configuration of three excluded lines and the contradiction they give.

∎

All previous lemmas pave way for our final technical lemma:

###### Lemma 3.8.

There cannot be 2 2 consecutive excluded lines for ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}}.

###### Proof.

Suppose there were two consecutive excluded lines y = − x + b y=-x+b and y = − x + b + 2 y=-x+b+2 for some even b b. Consider the possible values for a b − 8 a_{b-8}. It cannot be 8 8, since this is on the excluded line y = − x + b y=-x+b. It cannot be 6 6, as this this would create a third consecutive excluded line y = − x + b + 4 y=-x+b+4. It also cannot be 4 4, because this would create the fault line y = − x + b + 6 y=-x+b+6, contradicting Lemma 3.6. Thus, we must have a b − 8 = 2 a_{b-8}=2, which means we have the fault line y = − x + b + 8 y=-x+b+8. We also must have a b − 4 = 2 a_{b-4}=2, since values 4 4 or 6 6 would put a point of the graph on one of the excluded lines, and value 8 8 would yield the fault line y = − x + b + 6 y=-x+b+6, contradicting Lemma 3.6. Thus, we also have the fault line y = − x + b + 12 y=-x+b+12.

1 2 3 4 5 6 7 8 9 b b

Figure 9: What two consecutive excluded lines can be reasoned to imply.

Now consider a b + 1 a_{b+1}. It cannot be 1 1 or 7 7, since these would put a point of the graph on an excluded line. It cannot be 9 9, otherwise it would create the fault line y = − x + b + 10 y=-x+b+10, and we would have three consecutive fault lines y = − x + b + { 8, 10, 12 } y=-x+b+\left\{8,10,12\right\} contradicting Lemma 3.5. It cannot be 5 5, for if it were, there would be the three fault lines y = − x + b + { 8, 12, 14 } y=-x+b+\left\{8,12,14\right\} in contradiction with Lemma 3.7. Hence we have a b + 1 = 3 a_{b+1}=3 and the fault line y = − x + b + 16 y=-x+b+16. Similarly, we must have a b + 3 = 1 a_{b+3}=1, since 5 5 or 9 9 put it on a fault line, 7 7 would create three consecutive fault lines y = − x + b + { 12, 14, 16 } y=-x+b+\left\{12,14,16\right\}, and 3 3 would create the configuration of fault lines y = − x + b + { 12, 16, 18 } y=-x+b+\left\{12,16,18\right\} forbidden by Lemma 3.7. Therefore, there is also the fault line y = − x + b + 20 y=-x+b+20. But now every possible value for a b + 7 a_{b+7} leads to a contradiction. If it is 1 1, 5 5, or 9 9, then it is on a fault line. If it is 3 3 or 7 7, it creates a fault line resulting in a configuration forbidden by Lemmas 3.7 and 3.5, respectively. Therefore, we cannot have two consecutive excluded lines.

1 2 3 4 5 6 7 8 9 b b

Figure 10: The contradiction reached from two consecutive fault or excluded lines.

∎

Excluded lines by definition have slope − 1 -1. To finish the proof pf Theorem 3.3 we extend the notion of excluded line to those lines y = x + b y=x+b with even b b, which do not contain any point of the graph except possibly the point ( 9 − b, 9) (9-b,9). We call these the orthogonal excluded line s of the sequence ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}}. The conclusion of Lemma 3.8 also holds for orthogonal extended lines: there cannot be two consecutive ones. Indeed, y = x + b y=x+b is an orthogonal extended line of the 18 18 -avoiding odd-even sequence ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} if and only if y = − x − b y=-x-b is an extended line of the 18 18 -avoiding odd-even sequence ( a − i) i ∈ ℤ ({a}_{-i})_{i\in\mathbb{Z}}, so we can apply Lemma 3.8 for ( a − i) i ∈ ℤ ({a}_{-i})_{i\in\mathbb{Z}}.

Another useful observation is that the line y = − x + b y=-x+b is the fault line of exactly those points that are on the line y = x + 18 − b y=x+18-b. Hence if y = − x + b y=-x+b contains a point of the graph (say, it is not excluded), then y = x + 18 − b y=x+18-b must be an orthogonal excluded line. Using this observation for ( a − i) i ∈ ℤ ({a}_{-i})_{i\in\mathbb{Z}} one can also obtain that if the orthogonal line y = x + b y=x+b contains a point of the graph of ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} (say, it is not excluded), then y = − x − 18 − b y=-x-18-b must be an excluded line for ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}}.

Let us now assume that there exists an 18 18 -avoiding sequence ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} and let y = − x + b y=-x+b be a fault line of it for some even b b. By the above we can make a sequence of conclusions. The lines y = − x + b ± 2 y=-x+b\pm 2 are not excluded by Lemma 3.8. Then y = x + 18 − b ± 2 y=x+18-b\pm 2 must be orthogonal excluded lines. Then y = x + 18 − b ± 4 y=x+18-b\pm 4 are not excluded by the adaptation of Lemma 3.8 for orthogonal lines. Then y = − x + b ± 4 y=-x+b\pm 4 must be excluded lines. Again by Lemma 3.8 the lines y = − x + b ± 6 y=-x+b\pm 6 are not excluded and hence the orthogonal lines y = x + 18 − b ± 6 y=x+18-b\pm 6 must be excluded. This implies that y = x + 18 − b ± 8 y=x+18-b\pm 8 are not orthogonal excluded lines by the adaptation of Lemma 3.8 and y = − x + b ± 8 y=-x+b\pm 8 are excluded lines.

What can now be the value of a b − 9 a_{b-9}? It must be odd as b b is even and ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} is an odd-even sequence. The line y = x + 18 − b − 2 y=x+18-b-2 being excluded shows it cannot be 7 7, y = − x + b − 4 y=-x+b-4 being excluded shows that it cannot 5 5, y = x + 18 − b − 6 y=x+18-b-6 being excluded shows it cannot be 3 3, y = x + b − 8 y=x+b-8 being excluded shows it cannot be 1 1. The line y = − x + b y=-x+b is a fault line of ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} so in principle ( a b − 9, 9) (a_{b-9},9) could be on it. However then, the orthogonal line x + 18 − b x+18-b should also be excluded, meaning that together with y = x + 18 − b ± 2 y=x+18-b\pm 2 they would represent three consecutive orthogonal excluded lines, a contradiction.

∎

To complete the proof of Theorem 1.3 we need the following little proposition.

###### Proposition 3.9.

Let k k be a positive even integer. If there is a k k -avoiding odd-even sequence, then there is a ( k + 2 ​ ℓ) (k+2\ell) -avoiding odd-even sequence for every ℓ ∈ ℤ ≥ 0 \ell\in\mathbb{Z}_{\geq 0}.

###### Proof.

If ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} is a k k -avoiding odd-even sequence, then define the sequence ( b i) i ∈ ℤ ({b}_{i})_{i\in\mathbb{Z}} by

 | b i = a i + ℓ + ℓ b_{i}=a_{i+\ell}+\ell |  |

for all i ∈ ℤ i\in\mathbb{Z}. We claim that ( b i) i ∈ ℤ ({b}_{i})_{i\in\mathbb{Z}} is a ( k + 2 ​ ℓ) (k+2\ell) -avoiding odd-even sequence.

It is clearly an odd-even sequence as b i = a i + ℓ + ℓ ≡ i + 2 ​ ℓ ≡ i ( mod 2) b_{i}=a_{i+\ell}+\ell\equiv i+2\ell\equiv i\pmod{2} for all i ∈ ℤ i\in\mathbb{Z}. Also, b i = a i + ℓ + ℓ ≤ k / 2 + ℓ = ( k + 2 ​ ℓ) / 2 b_{i}=a_{i+\ell}+\ell\leq k/2+\ell=(k+2\ell)/2 for all i ∈ ℤ i\in\mathbb{Z}. Suppose there were i, j ∈ ℤ i,j\in\mathbb{Z} with i < j i<j such that b i + b j − i + j = k + 2 ​ ℓ b_{i}+b_{j}-i+j=k+2\ell. Then we would have a i + ℓ + ℓ + a j + ℓ + ℓ − i + j = k + 2 ​ ℓ a_{i+\ell}+\ell+a_{j+\ell}+\ell-i+j=k+2\ell. But this implies a i + ℓ + a j + ℓ − ( i + ℓ) + ( j + ℓ) = k a_{i+\ell}+a_{j+\ell}-(i+\ell)+(j+\ell)=k, which contradicts the fact that ( a i) i ∈ ℤ ({a}_{i})_{i\in\mathbb{Z}} is k k -avoiding. ∎

###### Proof of Theorem 1.3 (i).

Let m ≤ 9 m\leq 9 be a positive integer. We claim that there is no 2 ​ m 2m -avoiding odd-even sequence. Indeed, otherwise our previous proposition implied that there is also an 18 18 -avoiding odd-even sequence, which contradicts Theorem 3.3. Now by Proposition 3.2, there is an integer N 0 ​ ( m) N_{0}(m) such that every even 1 1 - 3 3 tree of order at least N 0 ​ ( m) N_{0}(m) contains a leaf-leaf path of length 2 ​ m 2m, which is exactly the statement of part (i) of Theorem 1.3. ∎

## 4 Characterization of graphs with no subgraphs of minimum degree 3

Let 𝒢 {\cal G} denote the family of graphs G G with 2 ​ | G | − 2 2|G|-2 edges and no proper (not necessarily induced) subgraphs with minimum degree 3 3. In this section we characterize the members of 𝒢 {\cal G} and deduce Theorem 1.4 as a corollary.

A wheel W n W_{n} is an n n -vertex graph with vertices c c, and w 1, …, w n − 1 w_{1},\dots,w_{n-1} with edges c ​ w i cw_{i} and w i ​ w i + 1 ( mod n − 1) w_{i}w_{i+1\pmod{n-1}} for i = 1, …, n − 1 i=1,\dots,n-1. The vertex c c will be called the *centre*of the wheel and the vertices w 1, …, w n − 1 w_{1},\dots,w_{n-1} will be called the *outside vertices*of W n W_{n}. For n ≥ 4 n\geq 4, Let H n H_{n} be the graph on n n vertices called x x, y y, and v 1, …, v n − 2 v_{1},\dots,v_{n-2} formed by the edges v i ​ v i + 1 v_{i}v_{i+1} for i ∈ { 1, …, n − 3 } i\in\{1,\dots,n-3\}, x ​ v i xv_{i} for i ∈ { 1, …, n − 2 } i\in\{1,\dots,n-2\}, y ​ v 1 yv_{1}, and y ​ v n − 2 yv_{n-2}. We call x x and y y the *connectors*of H n H_{n} and v 1, …, v n − 2 v_{1},\dots,v_{n-2} the *internal vertices*of H n H_{n}. Note that the roles of the connectors are not symmetric; the letter y y will always denote one with degree two. See Figure 11 for a picture of the graph H 7 H_{7}.

y y v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} x x Figure 11: The graph H 7 H_{7}.

The next theorem shows that the graphs in 𝒢 {\cal G} must have a very specific structure. See Figure 12 for examples of its members on 11 11 vertices.

Figure 12: Graphs on 11 11 vertices with 20 20 edges and no proper (not necessarily induced) subgraphs with minimum degree 3 3.

###### Theorem 4.1.

The family 𝒢 {\cal G} consists of all wheels and those graphs that are formed, for some i i and j j, from a copy of H i H_{i} with connectors x x and y y and a copy of H j H_{j} with connectors x ′ x^{\prime} and y ′ y^{\prime} by letting x = x ′ x=x^{\prime} and y = y ′ y=y^{\prime} or by letting x = y ′ x=y^{\prime} and y = x ′ y=x^{\prime}.

For the proof we first recall some basic properties of graphs with no induced subgraphs of minimum degree 3 3.

Recall from the introduction that the following lemma is easy to prove by induction.

###### Lemma 4.2.

Every graph on n ≥ 2 n\geq 2 vertices with at least 2 ​ n − 2 2n-2 edges contains an induced subgraph with minimum degree 3 3.

For degree 3 3 -critical graphs, the induced subgraph of minimum degree 3 3 (guaranteed by the previous lemma) must be the whole G G. For these graphs, Erdős et al. [3] presented a special ordering to the vertices. Given an ordering x 1, …, x n x_{1},\dots,x_{n} of V ⁡ ( G) V(G) we let the *forward neighbourhood*of x i x_{i}, denoted N + ​ ( x i) N^{+}(x_{i}), be N + ​ ( x i) = N ⁡ ( x i) ∩ { x i + 1, …, x n } N^{+}(x_{i})=N(x_{i})\cap\{x_{i+1},\dots,x_{n}\}. The *forward degree*of x i x_{i} is d + ​ ( x i) = | N + ​ ( x i) | d^{+}(x_{i})=|N^{+}(x_{i})|. The following lemma is essentially from [3]. We prove it here in a slightly stronger formulation. Notice that the lemma considers not just graphs from 𝒢 \mathcal{G}, but degree 3 3 -critical graphs in general. We will make use of this in the next section.

###### Lemma 4.3.

For every degree 3 3 -critical graph G G on n n vertices there is an ordering x 1, …, x n x_{1},\dots,x_{n} of the vertices, such that the following hold.

1. (i)

d + ​ ( x 1) = 3 d^{+}(x_{1})=3.

2. (ii)

For 2 ≤ i ≤ n − 2 2\leq i\leq n-2, d + ​ ( x i) = 2 d^{+}(x_{i})=2.

3. (iii)

d + ​ ( x n − 1) = 1 d^{+}(x_{n-1})=1.

4. (iv)

If furthermore n ≥ 7 n\geq 7, then d ⁡ ( x n) ≥ 4 d(x_{n})\geq 4.

###### Proof.

We define x i x_{i} recursively. Let x 1 x_{1} be a vertex of minimum degree in G G. Suppose that we have already defined x 1, x 2, …, x i x_{1},x_{2},\dots,x_{i}. Then we let x i + 1 x_{i+1} be a vertex of minimal degree in G − { x 1, ⋯ −, x i } G-\{x_{1},\dots-,x_{i}\}.

For (i), notice that the average degree of G G is less than 4 4, so d ⁡ ( x 1) ≤ 3 d(x_{1})\leq 3. To see that d ⁡ ( x 1) ≥ 3 d(x_{1})\geq 3, notice that otherwise the graph G − x 1 G-x_{1} would have at least e ⁡ ( G) − 2 = 2 ​ ( n − 1) − 2 e(G)-2=2(n-1)-2 edges and Lemma 4.2 would imply the existence of an induced subgraph of G − x 1 G-x_{1} of minimum degree 3 3, a contradiction to G G being degree 3 3 -critical. Hence d ⁡ ( x 1) = 3 d(x_{1})=3.

For (ii), we proceed by induction to show that for all i i, 1 ≤ i ≤ n − 2 1\leq i\leq n-2, we have e ⁡ ( G − { x 1, …, x i }) = 2 ​ ( n − i) − 3 e(G-\{x_{1},\dots,x_{i}\})=2(n-i)-3. The case i = 1 i=1 follows from (i). Let i > 1 i>1 and assume e ⁡ ( G − { x 1, …, x i − 1 }) = 2 ​ ( n − ( i − 1)) − 3 e(G-\{x_{1},\dots,x_{i-1}\})=2(n-(i-1))-3. First notice that degree 3 3 -criticality of G G implies both d + ​ ( x i) ≤ 2 d^{+}(x_{i})\leq 2 and e ⁡ ( G − { x 1, …, x i }) ≤ 2 ​ ( n − i) − 3 e(G-\{x_{1},\dots,x_{i}\})\leq 2(n-i)-3. Indeed, otherwise the minimum degree of the induced subgraph G − { x 1, …, x i − 1 } G-\{x_{1},\dots,x_{i-1}\} would be exactly 3 3 or G − { x 1, …, x i } G-\{x_{1},\dots,x_{i}\} would contain an induced subgraph of minimum degree 3 3 by Lemma 4.2. On the other hand, e ⁡ ( G − { x 1, …, x i }) = e ⁡ ( G − { x 1, …, x i − 1 }) − d + ​ ( x i) ≥ 2 ​ ( n − ( i − 1)) − 3 − 2 e(G-\{x_{1},\dots,x_{i}\})=e(G-\{x_{1},\dots,x_{i-1}\})-d^{+}(x_{i})\geq 2(n-(i-1))-3-2 by induction, implying both e ⁡ ( G − { x 1, …, x i }) = 2 ​ ( n − i) − 3 e(G-\{x_{1},\dots,x_{i}\})=2(n-i)-3 and d + ​ ( x i) = 2 d^{+}(x_{i})=2.

Part (iii) now follows from e ⁡ ( G − { x 1, …, x n − 2 }) = 1 e(G-\{x_{1},\dots,x_{n-2}\})=1.

For (iv), assume that n ≥ 7 n\geq 7. Let x 1, …, x n x_{1},\dots,x_{n} be the ordering of the vertices of G G produced by the above procedure. Notice that the graph G ⁡ [{ x n − 5, x n − 4, …, x n }] G[\{x_{n-5},x_{n-4},\dots,x_{n}\}] must contain a vertex v v of degree at least 4 4 in G ⁡ [{ x n − 5, x n − 4, …, x n }] G[\{x_{n-5},x_{n-4},\dots,x_{n}\}] (since it has 6 6 vertices and 9 9 edges and contains a vertex of degree 2 2 (here we use that x n − 5 ≠ x 1 x_{n-5}\neq x_{1}). Since d ⁡ ( v) ≥ 4 d(v)\geq 4, v v must be one of x n − 3 x_{n-3}, x n − 2 x_{n-2}, x n − 1 x_{n-1}, or x n x_{n}. The graph G ⁡ [{ x n − 3, …, x n }] G[\{x_{n-3},\dots,x_{n}\}] has 4 4 vertices and 5 5 edges, and so contains a vertex x n − 3 ′ ≠ v x^{\prime}_{n-3}\neq v of degree 2 2 in G ⁡ [{ x n − 3, …, x n }] G[\{x_{n-3},\dots,x_{n}\}]. Let x n − 2 ′ x^{\prime}_{n-2}, x n − 1 ′ x^{\prime}_{n-1} be the two vertices in { x n − 3, x n − 2, x n − 1, x n } ∖ { v, x n − 3 ′ } \{x_{n-3},x_{n-2},x_{n-1},x_{n}\}\setminus\{v,x^{\prime}_{n-3}\} in an arbitrary order. Since G ⁡ [{ x n − 2 ′, x n − 1 ′, v }] G[\{x^{\prime}_{n-2},x^{\prime}_{n-1},v\}] spans a triangle, the ordering of G G given by x 1, x 2, … ​ x n − 5, x n − 4, x n − 3 ′, x n − 2 ′, x n − 1 ′, v x_{1},x_{2},\dots x_{n-5},x_{n-4},x^{\prime}_{n-3},x^{\prime}_{n-2},x^{\prime}_{n-1},v satisfies (i) – (iv). ∎

###### Proof of Theorem 4.1.

First we show that if G G is a wheel or a graph formed from gluing H i H_{i} and H j H_{j} together, then G G is in 𝒢 \mathcal{G}. If G G has a subgraph H H of minimum degree 3 3 and vertex v ∈ V ⁡ ( H) v\in V(H) with d G ​ ( v) = 3 d_{G}(v)=3, then the three neighbours of v v must all be in H H. Hence the connected components of the induced subgraph of G G on its vertices of degree 3 3 must either be fully contained in H H or fully missing. Wheels have only one such component, and graphs formed from gluing H i H_{i} and H j H_{j} together as in the theorem have two such components. Using this, it is easy to check that these graphs have no proper subgraphs of minimum degree 3 3.

For the reverse direction let G G be an n n -vertex graph with 2 ​ n − 2 2n-2 edges and no proper (not necessarily induced) subgraphs with minimum degree 3 3. From Lemma 4.3, we have that δ ⁡ ( G) ≥ 3 \delta(G)\geq 3. We formulate the property of G G that will be most important for us.

###### Observation 4.4.

The graph G G does not have two adjacent vertices of degree ≥ 4 \geq 4.

Indeed, the removal of the edge between two vertices of degree 4 4 would create a proper subgraph of G G minimum degree 3 3, a contradiction.

If | G | ≤ 6 |G|\leq 6, then it is easy to check (say by considering the ordering given in Lemma 4.3) that G G must be a wheel or the graph obtained by the gluing of two copies of H 4 H_{4}. Therefore, let us assume that we have | G | ≥ 7 |G|\geq 7.

First we show that if G G is not a wheel, then it contains a copy of H m H_{m} for some m ≥ 4 m\geq 4 with a certain structure to its internal vertices.

###### Claim 4.5.

Either G G is a wheel or G G has an induced subgraph H m ⊆ G H_{m}\subseteq G for some m ≥ 4 m\geq 4, such that none of the internal vertices of H m H_{m} have neighbours in G − V ⁡ ( H m) G-V(H_{m}).

###### Proof.

Consider the ordering x 1, …, x n x_{1},\dots,x_{n} of the vertices of G G as given by Lemma 4.3. Let k k be the smallest integer such that x n x_{n} is adjacent to every vertex in { x k + 1, …, x n − 1 } \{x_{k+1},\ldots,x_{n-1}\}. Note that k ∈ { 0, 1, … ​ n − 3 } k\in\{0,1,\ldots n-3\}, since by part (ii) and (iii) of Lemma 4.3, x n − 2 x_{n-2} and x n − 1 x_{n-1} are adjacent to x n x_{n}. We will show that if k = 0 k=0 then G G is a wheel and otherwise the subgraph G ⁡ [{ x k, …, x n }] G[\{x_{k},\dots,x_{n}\}] is the sort of copy of H n − k + 1 H_{n-k+1} that we need, with connectors x = x n x=x_{n} and y = x k y=x_{k}.

We plan to reconstruct G ⁡ [{ x ℓ, …, x n }] G[\{x_{\ell},\ldots,x_{n}\}] from the trivial graph on { x n } \{x_{n}\} by adding back one-by-one the vertices x i x_{i} for each i = n − 1, n − 2 ​ …, ℓ i=n-1,n-2\ldots,\ell (in reverse order), together with their incident edges to { x i + 1, …, x n } \{x_{i+1},\ldots,x_{n}\}.

First we show by backward induction that the induced subgraph G ⁡ [{ x i, …, x n − 1 }] G[\{x_{i},\ldots,x_{n-1}\}] is a path R i R_{i} for every i = max ⁡ { k + 1, 2 }, …, n − 2 i=\max\{k+1,2\},\ldots,n-2. Indeed, for every i = max ⁡ { k + 1, 2 }, …, n − 2 i=\max\{k+1,2\},\ldots,n-2 the vertex x i x_{i} is adjacent to x n x_{n} and by part (ii) of Lemma 4.3 to exactly one other vertex x j x_{j} in { x i + 1, …, x n − 1 } \{x_{i+1},\ldots,x_{n-1}\}. By part (iv) of Lemma 4.3 the degree of x n x_{n} in G G is at least 4 4 and since x j ​ x n ∈ E ⁡ ( G) x_{j}x_{n}\in E(G), Observation 4.4 implies that the degree of x j x_{j} in G ⁡ [{ x i + 1, …, x n − 1 }] G[\{x_{i+1},\ldots,x_{n-1}\}] must be at most one. So x j x_{j} is one of the endpoints of R i R_{i}, thus giving rise to a path R i − 1 R_{i-1} that is induced on { x i, …, x n − 1 } \{x_{i},\ldots,x_{n-1}\}.

Now we separate into two cases.

If k > 0 k>0, then we have that G ⁡ [{ x k + 1, …, x n − 1 }] G[\{x_{k+1},\ldots,x_{n-1}\}] is a path R k R_{k} with all its vertices adjacent to x n x_{n}. Since x k x_{k} is not adjacent to x n x_{n}, both of its forward neighbours must be in { x k + 1, …, x n − 1 } \{x_{k+1},\ldots,x_{n-1}\}. If any of these neighbours would be a vertex x j x_{j}, k < j < n k<j<n, with degree at least 2 2 in G ⁡ [{ x k + 1, …, x n − 1 }] G[\{x_{k+1},\ldots,x_{n-1}\}], then we get a contradiction from Observation 4.4 as x j ​ x n ∈ E ⁡ ( G) x_{j}x_{n}\in E(G). Hence x k x_{k} must be adjacent exactly to the two endpoints of the path R k R_{k} and then G ⁡ [{ x k, …, x n }] G[\{x_{k},\dots,x_{n}\}] is a copy of H n − k + 1 H_{n-k+1} with connectors x = x n x=x_{n} and y = x k y=x_{k} as we promised. Observe furthermore that there cannot be any additional edges between any x i ∈ { x k + 1, …, x n − 1 } x_{i}\in\{x_{k+1},\dots,x_{n-1}\} and V ⁡ ( G) ∖ { x k, …, x n } V(G)\setminus\{x_{k},\ldots,x_{n}\}, since otherwise the degree of x i x_{i} in G G would be at least 4 4 providing a contradiction from Observation 4.4 as x i ​ x n ∈ E ⁡ ( G) x_{i}x_{n}\in E(G).

If k = 0 k=0, then G ⁡ [{ x 2, …, x n − 1 }] G[\{x_{2},\ldots,x_{n-1}\}] is a path R 2 R_{2} with all its vertices adjacent to x n x_{n}. Again, none of the neighbours x j x_{j} of x 1 x_{1} can be an internal vertex of R 2 R_{2}, otherwise we obtained a contradiction from Observation 4.4 since x 1 ​ x n x_{1}x_{n} and x j ​ x n x_{j}x_{n} are both edges of G G. Recall that x 1 x_{1} has three neighbours (part (i) of Lemma 4.3). These then must be the two endpoints of R 2 R_{2} and x n x_{n}, giving rise to a wheel with center x n x_{n}. ∎

Given a copy of H m H_{m} contained in G G, we define G / H m G/H_{m} to be the graph formed out of G G by removing the internal vertices of H m H_{m}, and joining the connectors of H m H_{m} by an edge. It turns out that if H m H_{m} has the structure produced by Claim 4.5, then the graph G / H m ∈ 𝒢 G/H_{m}\in{\cal G}, so we will be able to apply induction.

###### Claim 4.6.

Suppose that graph G ∈ 𝒢 G\in{\cal G} has an induced subgraph H m ⊆ G H_{m}\subseteq G for some m m, such that none of the internal vertices of H m H_{m} have neighbours in G ∖ V ⁡ ( H m) G\setminus V(H_{m}). Then G / H m ∈ 𝒢 G/H_{m}\in{\cal G}.

###### Proof.

Let x x and y y be the connectors of H m H_{m}. By the assumptions of the lemma and the definition of G / H m G/H_{m}, the only edges which were present in G G and are not present in G / H m G/H_{m} are the 2 ​ m − 3 2m-3 edges of H m H_{m}. The only new edge in G / H m G/H_{m} is the edge x ​ y xy. From the definition of G / H m G/H_{m}, we have | G / H m | = | G | − m + 2 |G/H_{m}|=|G|-m+2. Combining this with e ⁡ ( G) = 2 ​ | G | − 2 e(G)=2|G|-2, we obtain e ⁡ ( G / H m) = e ⁡ ( G) − 2 ​ m + 4 = 2 ​ | G | − 2 ​ m + 2 = 2 | G / H m | − 2 e(G/H_{m})=e(G)-2m+4=2|G|-2m+2=2|G/H_{m}|-2.

We will show that for every proper subgraph K ⊊ G / H m K\subsetneq G/H_{m}, we have δ ⁡ ( K) ≤ 2 \delta(K)\leq 2. If K K does not contain the edge x ​ y xy, then K K is also a proper subgraph of G G, and then, since G ∈ 𝒢 G\in{\cal G}, K K must satisfy δ ⁡ ( K) ≤ 2 \delta(K)\leq 2. Suppose now that K K does contain the edge x ​ y xy. Let K ′ K^{\prime} be the graph formed from K K by removing the edge x ​ y xy, and adding the vertices and edges of H m H_{m}. Since G ∈ 𝒢 G\in{\cal G}, the proper subgraph K ′ ⊊ G K^{\prime}\subsetneq G must contain a vertex v v of degree at most 2 2. The vertex v v cannot be one of the internal vertices of H m H_{m}, since by the definition of H m H_{m}, all internal vertices have degree 3 3. So v v is also a vertex of K K. But the degree of any vertex of V ⁡ ( K) V(K) in K ′ K^{\prime} is at least as large as its degree in K K (in fact, unless u = x u=x or u = y u=y, the degree of u u in K K is equal to its degree in K ′ K^{\prime}). Hence the vertex v ∈ V ⁡ ( K) v\in V(K) has degree at most 2 2 in K K as well. ∎

Now we are ready to complete the proof of the theorem using induction on | G | |G|. The initial cases are when | G | ≤ 6 |G|\leq 6, and are easy to check by hand. Let G ∈ 𝒢 G\in{\cal G} be a graph on n ≥ 7 n\geq 7 vertices. We will show that G G possesses one of the two structures given in the theorem.

If G G is not a wheel, then by Claim 4.5 G G contains an induced copy of H ∗ H^{*} of H m H_{m} such that the internal vertices of H ∗ H^{*} have no neighbours outside of H ∗ H^{*}. By Claim 4.6, G / H ∗ ∈ 𝒢 G/H^{*}\in{\cal G}. Hence, by induction, G / H ∗ G/H^{*} is either a wheel or is a graph formed by gluing together a copy of H i H_{i} with connectors x x and y y and a copy of H j H_{j} with connectors x ′ x^{\prime} and y ′ y^{\prime}, for some i, j ≥ 4 i,j\geq 4.

First consider the case when G / H ∗ G/H^{*} is a wheel with center c c and outside vertices w 1, …, w k w_{1},\dots,w_{k}. Recall that there is an edge in G / H ∗ G/H^{*} between the two connectors of H ∗ H^{*}.

Suppose first that the connectors of H ∗ H^{*} are c c and w i w_{i} for some i i. In this case, G G is a graph formed from H k + 1 H_{k+1} and H m H_{m} by identifying the connectors of the two graphs. Indeed, this follows from the fact that removing the edge c ​ w i cw_{i} from the wheel gives a copy of H k + 1 H_{k+1} and from the fact that the internal vertices of H ∗ H^{*} have no neighbours outside of H ∗ H^{*}.

Suppose now that the connectors of H m H_{m} are two adjacent outside vertices of the wheel, say w 1 w_{1} and w 2 w_{2}. If k = 3 k=3 then the graph G / H ∗ G/H^{*} is just the complete graph on 4 4 vertices, so, as before, G G is a graph formed from H 4 H_{4} and H m H_{m} with connectors w 1 w_{1} and w 2 w_{2}. So suppose that k ≥ 4 k\geq 4. This ensures that d ⁡ ( c) ≥ 4 d(c)\geq 4 in G G. We also have d ⁡ ( w 2) ≥ 4 d(w_{2})\geq 4 in G G since w 2 w_{2} must be connected to c c, w 3 w_{3}, as well as all the internal vertices of H ∗ H^{*} (of which there are at least 2 2). But this gives a contradiction by Observation 4.4, since c ​ w 2 cw_{2} is an edge of G G.

Now, consider the case when G / H ∗ G/H^{*} is a graph formed by gluing together an H i H_{i} and an H j H_{j} at their connectors. Recall that there is an edge in G / H ∗ G/H^{*} between the two connectors of H ∗ H^{*}. Suppose, without loss of generality, that this edge is in H i H_{i}. Let x x and y y be the connectors of H i H_{i} and let v 1, …, v i − 2 v_{1},\dots,v_{i-2} be its internal vertices. Since x ​ y ∉ E ⁡ ( H i) xy\not\in E(H_{i}), one of the connectors of H ∗ H^{*} must be an internal vertex of H i H_{i}. If any internal vertex of H i H_{i} which is a connector of H ∗ H^{*} is adjacent in G G to any vertex of { x, y } \{x,y\} which is not a connector of H ∗ H^{*}, then we immediately get a contradiction by Observation 4.4 since both of these vertices have degree at least 4 4. Otherwise, for the internal vertex v t v_{t} of H i H_{i} which is a connector of H ∗ H^{*} we must have 1 < t < i − 2 1<t<i-2, and the other connector vertex must be x x. Then the proper subgraph G − { v 1, v 2, …, v t − 1 } G-\{v_{1},v_{2},\dots,v_{t-1}\} has minimum degree 3 3, contradicting our assumption of G G having no such subgraphs. This completes the proof of the inductive step and the theorem. ∎

It is an easy exercise to check that the graphs given in Theorem 4.1 are pancyclic and hence Theorem 1.4 follows.

## 5 Finding a 6 6 -cycle

###### Proposition 5.1.

Every degree 3 3 -critical graph G G with n ≥ 6 n\geq 6 contains a C 6 C_{6}.

###### Proof.

By Lemma 4.2 we have δ ⁡ ( G) ≥ 3 \delta(G)\geq 3.

Let us use Lemma 4.3 to obtain an ordering x 1, …, x n x_{1},\dots,x_{n} of the vertices of G G. By part (ii) and (iii) and using | G | ≥ 5 |G|\geq 5, the graph induced by the last four vertices is a K 4 K_{4} minus an edge. Let us assume without loss of generality that the missing edge is x n − 3 ​ x n − 2 x_{n-3}x_{n-2}, that is, both x n − 1 x_{n-1} and x n x_{n} have degree 3 3 in G ⁡ [{ x n − 3, x n − 2, x n − 1, x n }] G[\{x_{n-3},x_{n-2},x_{n-1},x_{n}\}].

Now let t ≤ n − 4 t\leq n-4 be the largest index for which the forward neighbourhood of the vertex x t x_{t} is not { x n − 1, x n } \{x_{n-1},x_{n}\} ( t t exists because, for example “ 1 1 ” is such an index).

First let us suppose that x t x_{t} has two forward neighbours x i x_{i} and x j x_{j} outside of { x n − 1, x n } \{x_{n-1},x_{n}\}. By the definition of x t x_{t} we have that x i x_{i} and x j x_{j} are both adjacent to x n − 1 x_{n-1} and x n x_{n}. Let m ∈ [n] ∖ { n, n − 1, i, j, t } m\in[n]\setminus\{n,n-1,i,j,t\} be the largest index such that the forward neighbourhood of x m x_{m} is not equal to { x i, x j } \{x_{i},x_{j}\} ( m m exists since | G | ≥ 6 |G|\geq 6). Note that if { i, j, t } ≠ { n − 2, n − 3, n − 4 } \{i,j,t\}\neq\{n-2,n-3,n-4\}, then we have m ≥ n − 4 m\geq n-4 and the forward neighbourhood of x m x_{m} is { x n, x n − 1 } \{x_{n},x_{n-1}\}. Thus x n − 1 ​ x m ​ x n ​ x j ​ x t ​ x i x_{n-1}x_{m}x_{n}x_{j}x_{t}x_{i} is a six-cycle (see Figure 13). If { i, j, t } = { n − 2, n − 3, n − 4 } \{i,j,t\}=\{n-2,n-3,n-4\}, then the graph G ⁡ [{ x n, …, x m + 1 }] G[\{x_{n},\ldots,x_{m+1}\}] (see Figure 13) has the property that any pair of vertices, but { x n − 2, x n − 3 } \{x_{n-2},x_{n-3}\} have a path of length four between them. Thus the addition of x m x_{m} will create a six-cycle.

x i x_{i} x n x_{n} x n − 1 x_{n-1} x j x_{j} x t x_{t} x m x_{m} x n − 2 x_{n-2} x n x_{n} x n − 1 x_{n-1} x n − 3 x_{n-3} x n − 4 x_{n-4} Figure 13: The two possible configurations which can occur in the case when x t x_{t} has two forward neighbours x i x_{i} and x j x_{j}, outside of { x n − 1, x n } \{x_{n-1},x_{n}\}. The grey vertices represent ones which may or may not be present.

Suppose now that x t x_{t} has exactly one forward neighbour x i x_{i}, with t + 1 ≤ i ≤ n − 2 t+1\leq i\leq n-2, outside of { x n − 1, x n } \{x_{n-1},x_{n}\}. Without loss of generality let x n x_{n} be a neighbour of x t x_{t} in { x n, x n − 1 } \{x_{n},x_{n-1}\}. By the definition of x t x_{t} we have that x i x_{i} is adjacent to both x n − 1 x_{n-1} and x n x_{n}. If i = n − 2 i=n-2, let us define s:= n − 3 s:=n-3, and otherwise let s:= n − 2 s:=n-2. Let m m be the smallest index such that the forward neighbourhood of x m x_{m} is neither { x i, x n } \{x_{i},x_{n}\} nor { x n − 1, x n } \{x_{n-1},x_{n}\} ( m m exists since the index “ 1 1 ” is certainly of that kind). Then the structure of the graph G ⁡ [{ x m + 1, …, x n }] G[\{x_{m+1},\ldots,x_{n}\}] looks like the one in Figure 14. Observe that for any pair of vertices in such a graph, but the pairs { x n − 1, x n } \{x_{n-1},x_{n}\} and { x n, x i } \{x_{n},x_{i}\}, there is a path of length four between them. Hence no matter where the two forward neighbours x j x_{j} and x l x_{l} of x m x_{m}, with { j, l } ≠ { n − 1, n }, { n, i } \{j,l\}\neq\{n-1,n\},\{n,i\}, are, they close a six-cycle.

x n − 1 x_{n-1} x i x_{i} x s x_{s} x n x_{n} x t x_{t} Figure 14: The possible induced subgraphs G [x m + 1, …, x n }] G[x_{m+1},\ldots,x_{n}\}] in the case when x t x_{t} has exactly one forward neighbour x i x_{i} outside of { x n − 1, x n } \{x_{n-1},x_{n}\}. The unlabeled vertices may or may not be there.

∎

## 6 Concluding remarks

In Theorem 1.2 we constructed degree 3 3 -critical graphs with no 23 23 -cycles. One could ask whether longer cycles could be forbidden as well. It is easy to use our method to construct sequences of degree 3 3 -critical graphs with no m m -cycles for any odd m ≥ 23 m\geq 23. Indeed, combining Proposition 3.9 with Theorem 2.5 shows that there are 2 ​ k 2k -avoiding sequences for all k ≥ 10 k\geq 10. Then Lemmas 2.1 and 2.2 give us degree 3-critical graphs with no cycles of length 2 ​ k + 3 2k+3 for all k ≥ 10 k\geq 10. It would be interesting to determine the shortest cycle length ℓ \ell for which there exist an infinite sequence of degree 3 3 -critical graphs with no cycle of length ℓ \ell. From the results in this paper we see that ℓ \ell must be between 7 7 and 23 23.

In this paper we were only able to find infinite sequences of degree 3 3 -critical graphs which do not contain *odd*cycles. It is not clear whether even cycles can be forbidden in the same way. We pose the following problem.

###### Problem 6.1.

Is there a function C ⁡ ( n) C(n) tending to infinity such that every degree 3 3 -critical graph on n n vertices contains cycles of all lengths 4, 6, 8, …, 2 ​ C ​ ( n) 4,6,8,\dots,2C(n).

Another natural extremal question concerns the number of different cycle length. A construction due to Bollobás and Brightwell [2] gives degree 3 3 -critical graphs with no cycles of length greater than 4 ​ log 2 ​ n + O ⁡ ( 1) 4\log_{2}n+O(1). Their construction is just the graph G ⁡ ( T d) G(T_{d}) where T d T_{d} is the 1 1 - 3 3 -tree having a root with each of his three subtrees being a perfect binary tree of depth d d. We conjecture that these graphs give the smallest number of cycle lengths amongst all degree 3 3 -critical graphs on n n vertices.

###### Conjecture 6.2.

Every degree 3 3 -critical graph on n n vertices contains cycles of at least 3 ​ log 2 ​ n + O ⁡ ( 1) 3\log_{2}n+O(1) distinct lengths.

A similar conjecture could be made about leaf-leaf paths in trees.

###### Conjecture 6.3.

Every 1 1 - 3 3 tree has leaf-leaf paths of at least log 2 ⁡ n \log_{2}n distinct lengths.

In this paper we have shown that for d ≥ 20 d\geq 20, it is impossible to guarantee that a sufficiently large 1 1 - 3 3 tree T T contains a leaf-leaf path of length d d. However, perhaps it is the case that in a sufficiently large 1 1 - 3 3 tree, there are leaf-leaf paths of “many” short lengths.

###### Conjecture 6.4.

There is a constant α > 0 \alpha>0 and a function C ⁡ ( n) C(n) tending to infinity such that every 1 1 - 3 3 tree of order n n contains at least α ​ C ​ ( n) \alpha C(n) of distinct leaf-leaf path lengths between 0 0 and C ⁡ ( n) C(n).

## References

- [1] B. Bollobás. Modern Graph Theory. Springer, 1998.
- [2] B. Bollobás and G. Brightwell. Long cycles in graphs with no subgraphs of minimal degree 3. Discrete Math., 75:47–53, 1989.
- [3] P. Erdős, R. J. Faudree, A. Gyárfás, and R. H. Schelp. Cycles in graphs without proper subgraphs of minimum degree 3. Ars Combin., 25(B):159–201, 1988.
- [4] P. Erdős, R. J. Faudree, C. Rousseau, and R. H. Schelp. Subgraphs of minimal degree k. Discrete Math., 85(1):53–58, 1990.
- [5] A. Gyárfás. Problems and memories. arXiv:1307.1768, 2013.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1408.5288
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1408.5289
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1408.5289
[7]: https://arxiv.org/abs/1408.5289
[8]: /html/1408.5290
