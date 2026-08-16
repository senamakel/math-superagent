<!-- source: https://link.springer.com/article/10.1007/s00493-026-00205-2 | converted from HTML -->

Leaf-to-leaf paths and cycles in degree-critical graphs | Combinatorica | Springer Nature Link

Skip to main content

# Leaf-to-leaf paths and cycles in degree-critical graphs

- Original Paper
- [Open access][1]
- Published: 04 March 2026

- Volume 46, article number 11 ( 2026)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[Combinatorica][5] [Aims and scope][6] [Submit manuscript][7]

Leaf-to-leaf paths and cycles in degree-critical graphs

[Download PDF][2]

## Abstract

An *n*-vertex graph is *degree 3-critical*if it has \(2n - 2\) edges and no proper induced subgraph with minimum degree at least 3. In 1988, Erdős, Faudree, Gyárfás, and Schelp asked whether one can always find cycles of all short lengths in these graphs, which was disproven by Narins, Pokrovskiy, and Szabó through a construction based on leaf-to-leaf paths in trees whose vertices have degree either 1 or 3. They went on to suggest several weaker conjectures about cycle lengths in degree 3-critical graphs and leaf-to-leaf path lengths in these so-called 1-3 trees. We resolve three of their questions either fully or up to a constant factor. Our main results are the following:

-

every *n*-vertex degree 3-critical graph has \(\Omega (\log n)\) distinct cycle lengths;

-

every tree with maximum degree \(\Delta \ge 3\) and \(\ell \) leaves has at least \(\log _{\Delta -1}\, ((\Delta -2)\ell )\) distinct leaf-to-leaf path lengths;

-

for every integer \(N\ge 1\), there exist arbitrarily large 1–3 trees which have \(O(N^{0.91})\) distinct leaf-to-leaf path lengths smaller than *N*, and, conversely, every 1–3 tree on at least \(2^N\) vertices has \(\Omega (N^{2/3})\) distinct leaf-to-leaf path lengths smaller than *N*.

Several of our proofs rely on purely combinatorial means, while others exploit a connection to an additive problem that might be of independent interest.

### Similar content being viewed by others

### [Lower Bounds for Leaf Rank of Leaf Powers][8]

Chapter © 2024

### [Fully Leafed Induced Subtrees][9]

Chapter © 2018

### [Parameterized Leaf Power Recognition via Embedding into Graph Products][10]

Article 29 May 2020

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Combinatorics][11]
- [Criticality][12]
- [Discrete Mathematics][13]
- [Graph Theory][14]
- [Graph Theory in Probability][15]
- [Leaf development][16]

## 1 Introduction

There is a long line of research in combinatorics seeking to understand what conditions guarantee that a graph contains cycles of many different lengths. In 1973, Bondy [[4][17]] made the famous meta-conjecture that any non-trivial condition that guarantees Hamiltonicity is enough to ensure that the *n*-vertex graph is *pancyclic*, i.e. that it contains all cycle lengths in \(\{3, \dots , n\}\). This led to a host of interesting results in the following fifty years bringing support to Bondy’s conjecture in a variety of different settings [[1][18], [4][17], [6][19], [9][20], [17][21]]. However, most of the results in the area concern (somewhat) dense graphs, and for very sparse graphs our understanding of which graphs contain many cycle lengths is more fragmentary. Sudakov and Verstraëte [[22][22]] showed that graphs with average degree \(d\) and girth at least \(g\) contain \(\Omega (d^{\lfloor (g-1)/2 \rfloor })\) distinct cycles lengths, thus proving a conjecture of Erdős [[11][23]]. A related conjecture of Erdős and Hajnal [[11][23]] was resolved by Gyárfás, Komlós, and Szemerédi [[14][24]], who proved that in a graph with average degree *d*, the sum of the reciprocals of the distinct cycle lengths is \(\Omega (\log d)\).

The starting point of the present work is a conjecture of Erdős, Faudree, Gyárfás, and Schelp [[12][25]], who asked whether many cycle lengths can be found in a specific class of sparse graphs called *degree 3-critical graphs*. These are defined to be graphs with \(n\) vertices, \(2n-2\) edges and no proper induced subgraph with minimum degree at least 3; it is not hard to see that these graphs necessarily have minimum degree 3. Degree 3-critical graphs satisfy several interesting properties; for example, they have no proper induced subgraph *H*on \(2|V(H)|-2\) edges, and hence, by a theorem of Nash-Williams [[19][26]], they are the union of two edge-disjoint spanning trees.

Erdős, Faudree, Gyárfás, and Schelp [[12][25]] proved that any *n*-vertex degree 3-critical graph contains a cycle of length 3, 4, and 5, as well as a cycle of length at least \(\log n\). Footnote 1 This last bound was later improved by Bollobás and Brightwell [[3][27]] to \(4\log n+O(\log \log n)\), which is asymptotically best possible. In an effort to reveal a rich structure of cycle lengths in such graphs, Erdős et al. [[12][25]] (also see [[10][28]]) conjectured that it should be possible to find cycle lengths \(3,4,5 \dots , N\) for some \(N= N(n) \rightarrow \infty \) as \(n \rightarrow \infty \). Their conjecture, however, was disproven by Narins, Pokrovskiy, and Szabó [[18][29]] who showed that there are arbitrarily large degree 3-critical graphs with no cycle of length 23. The crucial ingredient of their construction is a particular class of trees called *1–3 trees*. A 1–3 tree is a tree where every vertex has degree either 1 or 3. It was shown in [[18][29]] that there exist infinitely many 1–3 trees with no two leaves at distance 20 from one another, which then yielded the desired degree 3-critical graphs by adding two vertices adjacent to all leaves and to each other.

Despite their surprising counterexamples, the authors of [[18][29]] proved that any degree 3-critical graph with at least six vertices contains a cycle of length 6, and asked whether it might still be the case that degree 3-critical graphs contain many cycle lengths. They posed the following conjecture.

### Conjecture A

( [[18][29], Conjecture 6.2]) Every degree 3-critical graph on *n*vertices contains cycles of at least \(3 \log n + O(1)\) distinct lengths.

A classical construction of Bollobás and Brightwell [[3][27]] shows that, if true, Conjecture [A][30] is best possible. Our first result proves that Conjecture [A][30] is true up to a constant factor.

### Theorem 1

Every degree 3-critical graph on *n*vertices contains cycles of at least \(\frac{\log n}{3+\log 3}+O(1)\) distinct lengths.

This provides the first bound on the number of cycle lengths as a function of *n*tending to infinity, and arguably can be viewed as confirmation of the original motivation of Erdős et al. [[12][25]] to demonstrate the abundance of cycle lengths in such graphs. In fact, we establish this result as a corollary of a more general theorem (Theorem [12][31]) which applies to *degree k-critical graphs*for any \(k \ge 3\), i.e., *n*-vertex graphs with \((k-1)n - \left( {\begin{array}{c}k\\ 2\end{array}}\right) + 1\) edges and no proper induced subgraph with minimum degree at least *k*. This family was introduced by Bollobás and Brightwell [[3][27]] as a natural generalization of degree 3-critical graphs, and a problem closely related to this family was studied more recently by Sauermann [[21][32]].

The key idea behind the proof of Theorem [1][33] is to define an appropriate partial ordering on the vertex set of the given graph. By Dilworth’s theorem, this either gives a long chain or a long antichain. The first case yields a long path *P*together with a collection of paths that intersect *P*in a special way (a structure known as a *vine*). In the second case, we find two large trees that are vertex-disjoint except for the fact that they share the same set of leaves. A careful analysis then yields many cycle lengths in either case.

Motivated by the connection between degree 3-critical graphs and 1–3 trees that they established, the authors of [[18][29]] also formulated two conjectures about leaf-to-leaf path lengths in 1–3 trees. The first of these conjectures is as follows.

### Conjecture B

( [[18][29], Conjecture 6.3], corrected version) Every 1–3 tree *T*of order *n*has leaf-to-leaf paths of at least \(\log (n+2) -1\) distinct lengths.

Here and throughout the rest of this paper, the length of a path is equal to the number of edges of the path, and we consider a single vertex to be a path of length 0.

The original form of Conjecture [B][34] in [[18][29]] asks for at least \(\log n\) distinct lengths, but as stated this is false, as the following example shows. For any \(d \ge 2\), consider the (unique) 1-3 tree *T*in which, for some root \(r \in V(T)\), every leaf is at distance precisely *d*from *r*. It is not hard to see that *T*contains \(3 \cdot 2^{d} -2\) vertices but only \(d+1 < \log (3 \cdot 2^{d} -2)\) distinct leaf-to-leaf path lengths (namely, the ones in \(\{0,2,4,\dots , 2d\}\)). This example also shows that Conjecture [B][34] is tight whenever \(n=3\cdot 2^{d}-2\) for some \(d\ge 2\).

Our second result resolves Conjecture [B][34] in a strong form. Our proof works for arbitrary trees, and gives a bound depending on the maximum degree. Consider, however, for any \(n>\Delta \ge 2\), the tree obtained from a star \(S_{\Delta }\) by subdividing an edge \(n - \Delta - 1\) times. This yields a tree with *n*vertices and maximum degree \(\Delta \) with only three distinct leaf-to-leaf path lengths, so we cannot expect to give a bound in terms of just *n*and \(\Delta \). Instead, we require control over the number of *leaves*, say \(\ell \), of the tree.

### Theorem 2

Let *T*be a tree with maximum degree \(\Delta \ge 3\) and \(\ell \) leaves. Then *T*has at least \(\log _{\Delta -1}\, ((\Delta -2)\ell )\) distinct leaf-to-leaf path lengths.

Theorem [2][35] for \(\Delta = 3\) implies Conjecture [B][34] since any 1–3 tree on \(n\) vertices has precisely \(\frac{n+2}{2}\) leaves. More generally, our result is tight whenever \(\ell = \Delta (\Delta - 1)^{d-1}\) for some \(d \ge 2\), as demonstrated by the tree *T*in which each vertex has degree 1 or \(\Delta \) and each leaf is at distance precisely *d*from some root \(r \in V(T)\) (whose leaf-to-leaf path lengths are \(0, 2, \dots , 2d\)). In fact, noticing that *T*’s leaves can be grouped into \((\Delta -1)\) -tuples of sister leaves that share a neighbour, and that deleting at most \((\Delta -2)\) leaves in each tuple does not affect the path lengths of the tree, we may construct for each \(\ell '>\Delta (\Delta -1)^{d-2}\) a tree \(T'\) with maximum degree \(\Delta \) and \(\ell '\) leaves and only \(d+1\) distinct leaf-to-leaf path lengths. This shows that Theorem [2][35] is tight for all values of \(\ell \) and \(\Delta \), up to an additive term of 1. The proof proceeds by finding a suitable choice of root vertex through Helly’s theorem for trees, deleting the leaves that are at a certain distance from the root, and then applying induction.

While Conjecture [B][34] imposes no restrictions on the lengths considered, the final conjecture of Narins, Pokrovskiy and Szabó [[18][29]] that we address asks to determine how many *short*leaf-to-leaf path lengths can be found. They conjectured that for 1–3 trees, one can find path lengths which are dense in an interval of the form [0, *N*].

### Conjecture C

( [[18][29], Conjecture 6.4]) There exist a constant \(\alpha >0\) and a function \(N = N(n)\) tending to infinity as \(n \rightarrow \infty \) such that every 1–3 tree of order *n*contains at least \(\alpha N\) distinct leaf-to-leaf path lengths between 0 and *N*.

Our next result disproves Conjecture [C][36] in the following strong form, namely, with a poly-sublinear upper bound.

### Theorem 3

There exists an absolute constant \(c\in (0,1)\) such that the following holds.

For all \(N \ge 1\) and all even \(n\ge N\), there exists an *n*-vertex 1–3 tree with \(O(N^c)\) distinct leaf-to-leaf path lengths between 0 and *N*.

The proof of Theorem [3][37] yields \(c=\left( 2-\frac{\log 10}{\log 13} \right) ^{-1}\approx 0.9073\). We complement this result by also providing a polynomial lower bound on the number of short lengths that may be found, which shows that we cannot take \(c < 2/3\) in Theorem [3][37].

### Theorem 4

For all \(N \ge 1\) and all even \(n \ge 2^{N/2}\), every *n*-vertex 1-3 tree contains leaf-to-leaf paths of \(\Omega (N^{2/3})\) distinct lengths between 0 and *N*.

In fact, Theorem [4][38] is an immediate corollary of a more general statement about trees with no vertices of degree 2. Given a tree *T*and a leaf \(v \in V(T)\), we say that *v**witnesses*the length \(\ell \) if there is a leaf-to-leaf path of length \(\ell \) containing *v*(as an endpoint).

### Theorem 5

For all \(N \ge 1\) sufficiently large, both of the following statements hold.

1. (i)

Let *T*be a tree containing no vertex of degree 2. If *T*contains a path of length at least *N*/2, then *T*contains \(\Omega (N^{2/3})\) leaf-to-leaf paths of distinct lengths between 0 and *N*, all witnessed by the same leaf \(v \in V(T)\).

2. (ii)

For all even *n*, there exists an *n*-vertex 1–3 tree in which no leaf witnesses more than \(O(N^{2/3})\) distinct lengths between 0 and *N*.

Note that the assumption that there are no vertices of degree 2 in the lower bound of Theorem [5][39] is necessary, as shown again by the example of a subdivided star. Since every *n*-vertex 1-3 tree has diameter at least \(\log n - 2\) (for instance, by Theorem [2][35]), we see that indeed the first part of Theorem [5][39] implies Theorem [4][38].

The proof of the first part of Theorem [5][39] proceeds as follows: if *T*contains many disjoint (rooted) subtrees in which some leaf is very close to the root, then we use the Erdős-Szekeres theorem to find a subfamily of such subtrees for which we can control the lengths of paths between leaves in distinct subtrees. If instead *T*contains a subtree \(T'\) in which every leaf is far from the root, then we find many distinct leaf-to-leaf path lengths inside of \(T'\).

The proofs of Theorem [3][37] and the second part of Theorem [5][39] rely on a connection to an additive combinatorics question which may be interesting in its own right. More specifically, we construct a tree *T*by appending balanced binary trees of varying depths to a long path; it then turns out that the set of leaf-to-leaf path lengths in *T*can be controlled by the additive structure of the sequence of subtree depths. For Theorem [3][37], this allows us to relate the problem to the construction of a pair of finite sets \(U, V \subseteq \mathbb {N}\) such that, for some large \(m \ge 1\), \(U - V = [m]\) and \(|U+V| = O(m^\beta )\) for some suitable \(\beta \in (0,1)\). We discuss this in more detail in the concluding remarks (Section [5][40]).

### 1.1 Notation

We use standard asymptotic notation and graph theory notation and terminology – see [[2][41]].

In particular, given a (simple, undirected) graph *G*we write \(N_G(v)\) for the neighbourhood of a vertex *v*in *G*, \(\deg _G(v)\) for the degree of *v*and \(d_G(u, v)\) for the distance between *u*and *v*in a graph, i.e. the number of edges of the shortest path connecting them. We will drop the subscript *G*from the above notations if the graph *G*is clear from context. We also write \(\Delta (G)\) for the maximum degree of *G*. For \(U\subseteq V(G)\), let *G*[*U*] be the induced subgraph of *G*with the vertex set *U*. For a path *P*and a cycle *C*in *G*, we denote the length of *P*(resp. *C*) by \(\ell (P)\) (resp. \(\ell (C)\)), meaning the number of edges in *P*(resp. *C*).

For positive integers *s*, *t*, we write \((t)_s\) for the residue of \(t \mod s\) (as an integer in \(\{0, 1, \dots , s-1\}\)) and also use the nonstandard notation \((t)_s^*\) for the same residue considered as an integer in \(\{1, 2, \dots , s\}\). When \(s\le t\), define \([s,t]=\{i\in \mathbb {Z}:s\le i\le t\}\) and let \([t]=[1,t]\).

Given a rooted tree (*T*, *r*), its *layers*are the sets \(\{v \in V(T): d(v,r)=i\}\) for \(i \ge 0\). Given \(\ell \ge 1\), we call (*T*, *r*) a *perfect binary tree on*\(\ell \)*layers*if *T*is a binary tree rooted at *r*and every leaf \(v\in T\) satisfies \(d(r, v)=\ell -1\). We denote the set of leaves of \(T\) by \(L(T)\). For \(u,v\in V(T)\), we write *T*[*u*, *v*] to denote the unique (*u*, *v*) path in *T*.

We also employ a common abuse of notation by omitting floor and ceiling symbols and ignoring the rounding errors this causes whenever it is not essential for our argument; we emphasize this will only occur in the proofs of our asymptotic results and not in the case of Theorem [2][35].

### 1.2 Organization

The remainder of the paper is organized as follows. We prove that we can find many leaf-to-leaf path lengths in trees – Theorem [2][35] and the first part of Section [5][39] – in Section [2][42]. We provide constructions of trees with a small number of distinct leaf-to-leaf path lengths – Theorem [3][37] and the second part of Theorem [5][39] – in Theorem [3][43]. We prove Theorem [1][33] – that we can find many distinct cycle lengths in degree 3-critical graphs – in Section [4][44]. We discuss several open problems in Section [5][40].

## 2 Finding many leaf-to-leaf path lengths

### 2.1 Paths of unrestricted length

In this section, we prove Theorem [2][35]. We begin with a lemma showing how to find many lengths in a rooted tree with many leaves at the same distance from the root.

### Lemma 6

Let \(\Delta \ge 3\) and let *T*be a rooted tree with root *r*and \(\Delta (T) \le \Delta \). Assume that for some \(a\ge 1\) there are *m*distinct leaves \(x_1, \dots , x_m\) such that \(d(r, x_i) =a\) for all \(1\le i\le m\). Then there exists an \(i \in [m]\) such that *T*contains leaf-to-leaf paths of at least \(\log _{\Delta - 1} (m/\Delta ) + 2\) distinct lengths between 0 and 2*a*, all witnessed by \(x_i\).

### Proof

Denote the root’s neighbours by \(r_1, \dots , r_k\) with \(k\le \Delta \). Deleting the root *r*from *T*gives *k*new rooted trees \(T_1, \dots T_k\), with the new roots being the \(r_i\) ’s.

**Case 1:**\(\deg (r)\le \Delta -1\). In this case, we will prove the slightly stronger result that we can find at least \(\log _{\Delta -1}m+1\) suitable lengths, all witnessed by the same \(x_i\). We proceed by induction on the number of vertices of *T*.

As a base case, note that if *T*has only one vertex \(x_1\), then there is precisely \(\log _{\Delta -1}(1)+1=1\) leaf-to-leaf path, namely that of length 0 (witnessed by \(x_1\)).

For the inductive step, we distinguish two further subcases. If one of the \(T_i\) ’s contains all leaves \(x_1, \dots , x_m\), then the claim follows by the induction hypothesis applied to \(T_i\), since the root of \(T_i\) has degree at most \(\Delta -1\). Otherwise, by relabelling if necessary, we may assume that \(T_1\) contains at least \(m/(\Delta -1)\) of the leaves \(x_1, \dots , x_m\), and that \(T_2\) contains at least one leaf \(x_j\).

Moreover, the root of \(T_1\) has degree at most \(\Delta -1\). By the inductive hypothesis, \(T_1\) contains at least \(\log _{\Delta -1}(m/(\Delta -1))+1 = \log _{\Delta -1}(m)\) distinct lengths of leaf-to-leaf paths between 0 and \(2(a-1)\), all witnessed by a some leaf \(x_i\). Observe that the unique path from \(x_i\) to \(x_j\) has length 2*a*. This gives \(\log _{\Delta -1}(m) + 1\) lengths of paths between 0 and 2*a*, all witnessed by \(x_i\).

**Case 2:**\(\deg (r)=\Delta \). We again induct on the number of vertices of *T*. If *T*has \(\Delta +1\) vertices, then \(m = \Delta \) and each leaf witnesses lengths 0 and 1, so the conclusion holds.

For the inductive step, again consider the two subcases outlined above. If one of the \(T_i\) ’s contains all *m*leaves \(x_1, \dots , x_m\), then the claim follows by the inductive hypothesis applied to \(T_i\). Otherwise, again like in Case 1 we may assume that \(T_1\) has at least \(m/\Delta \) leaves from the set \(\{x_1, \dots , x_m\}\) and \(T_2\) has at least one leaf \(x_j\). Now the root of \(T_1\) has degree at most \(\Delta -1\), so we may use the slightly stronger bound obtained in Case 1 to find at least \(\log _{\Delta -1}(m/\Delta )+1\) distinct lengths between 0 and \(2(a-1)\), all witnessed by some \(x_i\). Together with the path of length 2*a*connecting \(x_i\) to \(x_j\), we obtain at least \(\log _{\Delta -1}(m/\Delta )+2\) lengths of paths between 0 and 2*a*, all witnessed by \(x_i\). \(\square \)

Our proof of Theorem [2][35] proceeds by induction on the number of leaves in the tree *T*. After choosing a root appropriately, we either find many leaves at the same distance from it (and thus Lemma [6][45] applies), or instead find a subtree \(T'\) with strictly smaller diameter but still having many leaves of *T*(to which the inductive hypothesis applies). For the choice of root, we need the following well-known Helly-type lemma for trees (see, for instance, [[15][46]] or [[16][47]]).

### Lemma 7

Let \(T\) be a tree and \(T_1,\hdots , T_s\) be a collection of subtrees of \(T\) such that \(V(T_i)\cap V(T_j) \ne \emptyset \) for all \(1\le i<j\le s\). Then \(\cap _{i=1}^s V(T_i) \ne \emptyset \).

We are now ready to prove the main result of this section.

### Proof of Theorem 2

The proof is by induction on |*L*(*T*)|. Note that the statement is trivial when \(|L(T)|=1\), since there is one path length (namely zero), and when \(|L(T)|\in [2,\Delta ]\), since there are at least two path lengths in *T*and \(\log _{\Delta -1}(\Delta (\Delta -2)) \le 2\). Assume that the statement is true for all \(\ell '<\ell \) and consider a tree *T*with \(\ell \) leaves. It is not hard to see that any two longest paths in \(T\) share a vertex and thus Lemma [7][48] implies there is a vertex *v*which is contained in every longest path. Moreover, we may assume without loss of generality that *v*is not a leaf, since otherwise its neighbour also satisfies this condition. Let *m*be the length of the longest path in *T*. We consider two cases.

**Case 1:**There is some leaf *x*with \(d(x,v)>m/2\).

Firstly, take a leaf *x*that maximizes *d*(*x*, *v*). Let \(e=vu\) be the edge incident to *v*on *T*[*v*, *x*]. Note that every leaf *y*that is connected to *v*by a path not containing *e*satisfies \(d(y,v) \le m - d(x,v) < m/2\), as otherwise \(T[x,y]=T[x,v]\cup T[v,y]\) would be a path of length greater than *m*. Moreover, since every longest path in *T*passes through *v*, there must exist some leaf *y*satisfying \(e\notin T[y,v]\) and \(d(y, v)=m-d(v, x)\). It follows that every longest path in *T*is formed by concatenating a path of length *d*(*x*, *v*) from a leaf to *v*(passing through *e*) together with a path of length \(m - d(x,v)\) from *v*to another leaf (avoiding *e*).

Now, let \(X_1\) be the set of leaves whose distance from *v*is equal to *d*(*x*, *v*) and let \(X_2\) be the set of leaves whose distance from *v*is equal to \(m - d(x,v)\). \(X_1\) and \(X_2\) are clearly disjoint, and by the above, every longest path in *T*goes from a vertex in \(X_1\) to a vertex in \(X_2\).

By relabelling if necessary, we may assume that \(|X_1| \le |X_2|\). Let \(L=L(T)\) be the set of leaves in *T*, and observe that \(|L \setminus X_1| \ge \ell /2\). We define \(T'\) to be the smallest subtree of *T*such that \(L \setminus X_1 \subseteq V(T')\), and claim that \(L(T')=L \setminus X_1\). Indeed, if \(T'\) contained some other leaf \(u \notin L \setminus X_1\), then \(T' - u\) would still be connected and we would have \(L \setminus X_1 \subseteq V(T' - u)\), a contradiction. Thus, \(L(T')=L \setminus X_1\subseteq L(T)\), which implies that leaf-to-leaf paths in \(T'\) are also leaf-to-leaf paths in *T*. Crucially, \(V(T') \cap X_1 = \emptyset \) and thus the longest path in \(T'\) is of length strictly less than *m*.

By the induction hypothesis, \(T'\) contains leaf-to-leaf paths of at least

$$\begin{aligned} \log _{\Delta -1}(\ell /2)+\log _{\Delta -1}(\Delta -2)\ge \log _{\Delta -1}\ell +\log _{\Delta -1}(\Delta -2)-1 \end{aligned}$$

distinct lengths, all strictly smaller than *m*. Together with the length *m*, we conclude that *T*contains at least \(\log _{\Delta -1}\ell +\log _{\Delta -1}(\Delta -2)\) distinct leaf-to-leaf path lengths.

**Case 2:**The furthest leaf *x*from *v*satisfies \(d(x,v) = m/2\).

In this case, every longest path is obtained by concatenating two internally vertex-disjoint paths of length *m*/2 from *v*to different leaves. Let *X*be the set of leaves of *T*which are at distance precisely *m*/2 from *v*. Now we split into two further subcases.

**Case 2.1:**\(|X|<(1-(\Delta -1)^{-2})\ell \). Consider the collection of subtrees of *T*obtained by deleting the vertex *v*, and let \(\overline{T}\) be one which contains at least \(|X|/\Delta \) elements of *X*.

Define \(X' = X \setminus V(\overline{T})\), so that \(|X'| \le (1 - \Delta ^{-1})|X|\). Recalling that *L*is the set of leaves of *T*and \(|L|=\ell \), we define \(T'\) to be the smallest subtree of *T*such that \(L \setminus X' \subseteq V(T')\). Using the same argument as in Case 1, it is easy to see that \(L(T')=L \setminus X'\). Hence we have

$$ |L\setminus L(T')|=|X'|\le \frac{\Delta -1}{\Delta }|X| \le \left( 1-\frac{1}{\Delta } - \frac{1}{\Delta (\Delta -1)} \right) \ell = (1-1/(\Delta -1))\ell . $$

Thus, \(T'\) has maximum degree at most \(\Delta \), at least \(\ell /(\Delta -1)\) leaves and by construction the longest path in \(T'\) is strictly shorter than *m*in length. Indeed, given a longest path, it has leaves \(u_1\) and \(u_2\), say, as endpoints. Supposing this path has length *m*, by the assumption of Case 2 above we know that \(d(v, u_1)=d(v, u_2)=m/2\), and so \(u_1, u_2\in X\setminus X'\). But then both \(u_1\) and \(u_2\) belong to the subtree \(\overline{T}\), and hence the path connecting them doesn’t pass through *v*, contradiction.

Thus, by the induction hypothesis, the leaf-to-leaf paths in \(T'\) have at least \(\log _{\Delta -1}((\Delta -2)\ell )-1\) many distinct lengths, and all of these also occur in *T*. Together with a leaf-to-leaf path of length *m*in *T*, we get the required bound.

**Case 2.2:**\(|X|\ge (1-(\Delta -1)^{-2})\ell \). Then, it follows by applying Lemma [6][45] to *T*rooted at *v*that there are at least

$$\begin{aligned} \log _{\Delta -1}\left( \frac{(1-(\Delta -1)^{-2})\ell }{\Delta }\right) +2=\log _{\Delta -1}((\Delta -2)\ell ) \end{aligned}$$

distinct leaf-to-leaf path lengths, as required. \(\square \)

### 2.2 Paths of restricted length

The aim of this section is to prove the lower bound of Theorem [5][39], which guarantees many lengths of short leaf-to-leaf paths in trees with not-too-small diameter and no vertices of degree 2.

We will consider a path of maximum length in *T*and look at its initial segment *P*of length *N*/2. Each vertex *v*in *P*has a subtree hanging from it (which we root at *v*). We will split into two cases depending on the minimum root-to-leaf distance in each of these subtrees. If one of them is very deep, we will be able to find many short leaf-to-leaf paths inside of it; this is inspired by the approach of [[18][29]]. Otherwise, all of the subtrees have shallow leaves and we will travel along *P*to find many paths of distinct lengths connecting them.

We will require the following classical result.

### Theorem 8

(Erdős-Szekeres [[13][49]]) Any sequence of \(n\) not necessarily distinct real numbers contains a monotone subsequence of length at least \(\sqrt{n}\).

We use Theorem [8][50] to prove the following lemma, which will be useful for proving Theorem [5][39]*(i)*.

### Lemma 9

Let \((a_1, \dots , a_n)\) be a sequence of non-negative real numbers such that \(a_i \le m\) for each \(1 \le i \le n\) and some \(m>0\). Then

$$\begin{aligned} \max \bigg \{\big |\{a_i+i: 1\le i\le n\} \big |, \big |\{a_i-i: 1\le i\le n\}\big | \bigg \}\ge \frac{n}{4\sqrt{m}}. \end{aligned}$$

### Proof

First, suppose that \(m \le n/2\). For each \(1\le i\le n/(2m) \), set \(A_i:=(a_j)_{j=2(i-1)m+1}^{(2i-1)m}\). Theorem [8][50] implies that each sequence \(A_i\) contains a monotone subsequence of length at least \(\sqrt{m}\). Let \(B_i\) be the set of indices of this subsequence, so that \(|B_i|\ge \sqrt{m}\) and \(B_i \subseteq [2(i-1)m+1,(2i-1)m]\).

Let *X*be the set of indices \(1\le k\le \frac{n}{2m}\) for which \((a_i)_{i\in B_k}\) is an increasing sequence, and set \(Y:=\left[ \frac{n}{2m} \right] \setminus X\). Suppose \(|X| \ge \frac{n}{4m}\). For each \(k\in X\) and \(i, j\in B_k\) with \(i < j\), we have \(a_{i} + i< a_{j} +j\), so the set \( A_k' = \{ a_i + i: i \in B_k \} \) consists of \(|B_k| \ge \sqrt{m}\) distinct elements. Moreover, given integers \(1\le k_1<k_2\le \frac{n}{2m}\), for any \(i_1\in B_{k_1}\) and \( i_2\in B_{k_2}\) we have

$$ a_{i_1} + i_1 \le m + (2k_1-1)m = 2k_1 m, $$

and

$$ a_{i_2} + i_2 \ge 0 + 2(k_2-1)m +1 \ge 2k_1 m +1, $$

so the sets \(A_k'\) are pairwise disjoint. We conclude that

$$ |\{ a_i+i : 1\le i\le n\}| \ge \sum _{k\in X} |A_k'| \ge \frac{n}{4m} \cdot \sqrt{m}= \frac{n}{4\sqrt{m}}. $$

If instead we have \(|X|<\frac{n}{4m}\), then \(|Y| \ge \frac{n}{4m}\), and for every \(k\in Y\), \((a_i)_{i\in B_k}\) is a decreasing subsequence. An analogous argument shows that in this case \(|\{a_i - i: 1\le i\le n\}|\ge \frac{n}{4\sqrt{m}}\).

If \(m>n/2\), Theorem [8][50] guarantees that the sequence \((a_i)_{i=1}^n\) has a monotone subsequence of length at least \(\sqrt{n}\). If this sequence is increasing, then \(|\{a_i+i:1\le i\le n\}|\ge \sqrt{n}\), while if the sequence is decreasing, then \(|\{a_i-i: 1\le i\le n\}|\ge \sqrt{n} \), and note that both quantities are at least \( \frac{n}{4\sqrt{m}}\), as required. \(\square \)

### Proof of Theorem 5(i)

We can assume that *N*is an even integer. Let \(P = v_0 v_1 \dots v_M\) be a path of maximum length in *T*and let \(P'= v_0 v_1 \dots v_{N/2}\) be its initial segment of length *N*/2. For each \(1 \le i \le N/2\), let \(T_i\) be the connected component of \(T \setminus E(P)\) that contains \(v_i\).

Observe that for every \(1\le i\le N/2\) and every leaf \(x\in T_i\setminus \{v_i\}\), we must have \(d(x, v_i)\le N/2\), as otherwise we would have \(d(x, v_M)>M\), a contradiction.

**Case 1:**There exists some \(1\le i\le N/2\) such that for every leaf \(x\in T_i\setminus \{v_i\}\), we have \(d(x, v_i)>N^{2/3}/2\). Then \(v_i\) has a neighbour \(u_i \in V(T_i)\) which is not a leaf and hence has degree at least 3 in \(T_i\). Let \(T'\) be a maximal binary subtree of \(T_i - v_i\) rooted at \(u_i\), and note that every leaf of \(T'\) is also a leaf of \(T\). Every leaf of \(T'\) is at distance at least \(N^{2/3}/2 - 1\) from \(u_i\). Together with the fact that each non-leaf vertex in \(T'\) has two children, this implies that \(T'\) contains at least \(2^{N^{2/3}/2 -1}\) leaves. As established above, each of these leaves is at distance at most *N*/2 from \(v_i\). Thus, there exists some \(1\le d\le N/2\) for which at least \(2^{N^{2/3}/2}/N\ge 2^{N^{2/3}/3}\) distinct leaves in \(T_i\) are all at distance precisely *d*from \(v_i\). By Lemma [6][45] we can then find a leaf \(x\in T_i\) witnessing at least \(\log (2^{N^{2/3}/3}/3)+ 2 \ge N^{2/3}/3\) distinct leaf-to-leaf path lengths in *T*, and all of these lengths are at most equal to \(2d\le N\).

**Case 2:**For every \(1\le i\le N/2\) there exists a leaf \(x_i\in T_i\), \(x_i\ne v_i\), such that \(a_i :=d(x_i, v_i) \le N^{2/3}/2\).

Observe that the set of path lengths connecting pairs in \(\{x_1, \dots , x_{N/2}\}\) is precisely

$$\begin{aligned} X = \{a_i + a_j + j - i : 1 \le i < j \le N/2\}. \end{aligned}$$

Moreover, any \((x_i, x_j)\) -path has length at most \(N/2 + N^{2/3} \le N\). By applying Lemma [9][51] with \(m = N^{2/3}/2\), we see that

$$\max \left( \big |\{a_i + i:1\le i\le N/2\}\big |, \big |\{a_i - i: 1\le i\le N/2\}\big |\right) \ge \frac{N^{2/3}}{4\sqrt{2}}.$$

If the inequality holds for \(\{a_i + i: 1\le i\le N/2\}\), then

$$\begin{aligned} |X| \ge |\{a_1 - 1 + (a_i + i) : 2 \le i \le N/2\}| \ge N^{2/3}/6, \end{aligned}$$

with \(N^{2/3}/6\) distinct lengths being witnessed by \(x_1\). If it holds for \(\{a_i - i: 1\le i\le N/2\}\), then

$$\begin{aligned} |X| \ge |\{a_{N/2} + (N/2) + (a_i - i): 1 \le i \le (N/2)-1\}| \ge N^{2/3}/6, \end{aligned}$$

with \(x_{N/2}\) witnessing all these lengths, as desired. \(\square \)

## 3 Trees with few leaf-to-leaf path lengths

In this section we prove Theorem [3][37] and the second part of Theorem [5][39]. Each result is obtained by taking a sequence \((a_i)\) with a suitable additive structure and constructing an *n*-vertex tree \(T_n((a_i))\) from it. We first describe the general construction, and then provide a suitable choice of \((a_i)\) for each of the two results.

### 3.1 The general construction

Let \(n \ge 4\) be even. Let \(m\in \mathbb {N}\) and consider a positive integer sequence \((a_i)_{i=1}^m\). We will now describe a general construction of an \(n\) -vertex 1–3 tree \(T_n((a_i))\) based on this sequence. For the most part, our construction consists of a path together with a collection of perfect binary trees attached to the path’s internal vertices, with the sequence \((a_i)\) dictating the depths of the perfect trees.

Consider the periodic sequence \((a'_i)_{i \ge 1}\) given by

$$ a_1, \dots , a_{m}, a_1, \dots , a_{m}, a_1, \dots , $$

and take its shortest initial segment \((a'_1, \dots , a'_t)\) with the property that \(S :=2+\sum _{i=1}^{t} 2^{a'_i} \ge n\). Note that \(t \ge 1\). Based on our choice of *t*and the fact that *n*and *S*are even, it must be the case that \(S - 2^{a'_t} \le n - 2\).

We will now describe how to construct \(T_n((a_i))\). We start with a path \(P = v_0 v_1 \dots v_{t+1}\). For each \(i \in [t-1]\), we take a perfect binary tree \((T_i, r_i)\) on \(a'_i\) layers, and add an edge from \(v_i\) to \(r_i\). Thus far, every vertex in the tree other than \(v_t\) has degree either 1 or 3 and the total number of vertices is

$$\begin{aligned} t+2 + \sum _{i=1}^{t-1} (2^{a'_i} - 1) = S - 2^{a_t'} + 1 \le n -1. \end{aligned}$$

Let \(L = n - (S - 2^{a'_t} + 1) \ge 1\), which must be odd since *n*and *S*are even. Since \(S \ge n\), we have that \(L \le 2^{a'_t} - 1\). We take a perfect binary tree \((\tilde{T}, r_t)\) on \(\lceil \log (L + 1) \rceil \le a'_t\) layers. With this choice, we have \(L \le |V(\tilde{T})| < 2L\). We now proceed to iteratively delete pairs of leaves sharing a parent from the lowest layer of \(\tilde{T}\), until we obtain a tree \(T_t\) which has precisely *L*vertices (which is possible since both \(L\) and \(|V(\tilde{T})|\) are odd). By removing pairs of leaves which share a parent, and always from the lowest layer, we guarantee that the resulting \(T_t\) is still a binary tree, with its leaves spanning at most two layers. Adding an edge from \(r_t\) to \(v_t\) then completes the construction of \(T_n((a_i))\). Observe that for any two leaves \(x_i \in T_i\), \(x_j \in T_j\) with \(i \ne j\), the unique path from \(x_i\) to \(x_j\) consists of the path inside \(T_i\) from \(x_i\) to \(r_i\), the edge \(r_iv_i\), the path from \(v_i\) to \(v_j\) in \(P\), the edge \(v_jr_j\) and finally the path from \(r_j\) to \(x_j\); cf. Figure [1][52].

**Fig. 1**

[image: Fig. 1]

[Full size image][53]

The construction of the tree \(T_n((a_i))\). Each subtree \(T_{i+mj}\) for \(j\ge 1\), except \(T_t\), represents a perfect binary tree on \(a_i\) layers, whose root neighbours the corresponding vertex on the horizontal path *P*. Note that this pattern repeats cyclically every *m*steps. To the vertex \(v_t\), we instead append the specific tree \(T_t\), as described in the context

### 3.2 Upper bound on path lengths in \([N]\)

For a set \(U\subseteq \mathbb {Z}\) and \(k\in \mathbb {Z}\), let \(k\cdot U :=\{ ku: u \in U\}\) and \(k + U = U + k :=\{u+k : u \in U\}\).

### Proposition 10

Suppose that there exist a positive integer \(m\), sets \(U,V \subseteq \mathbb {Z}\) and a real \(\beta \in (0,1)\) that satisfy the following:

1. 1.

\(U+V \subseteq [m] \subseteq U-V\); and

2. 2.

\(\left| U+V\right| = m^\beta \).

Let \(M = \lfloor m^{2-\beta }\rfloor \) and \(n\ge M\) even. If \(m^{1-\beta }\ge 4\), then there exists a 1–3 tree \(T\) on \(n\) vertices such that the number of distinct leaf-to-leaf path lengths in \([M]\) is at most \(26M^{\frac{1}{2-\beta }}\).

### Proof

Since \(U-V = [m]\), we can find a sequence of pairs \((u_i,v_i)_{i=1}^m\) such that \(i = u_i - v_i\). Consider the sequence \((a_i)_{i=1}^m\), defined by \(a_i = u_i + v_i\). Let \(T\) be the tree \(T_n((a_i))\) as defined in Section [3.1][54].

We proceed to count the number of leaf-to-leaf path lengths at most *M*in *T*. We will prove that there are at most 13*m*such paths, which suffices to prove the proposition since

$$\begin{aligned} M^{\frac{1}{2-\beta }} \ge (m^{2-\beta } - 1)^{\frac{1}{2-\beta }} \ge \frac{m}{2^{\frac{1}{2-\beta }}} \ge \frac{m}{2}, \end{aligned}$$

where we used \(m^{1-\beta } \ge 4\) in the second inequality.

First note that, for two leaves *u*and *v*belonging to the same subtree \(T_i\), say, we must have \(d(u, v)\le 2m\). It therefore suffices to show that there are at most 11*m*lengths arising when we consider leaves belonging to different subtrees, say \(u\in T_i\) and \(v\in T_j\) with \(1\le i<j\le t\) and \(d(u, v)\le M\), or when \(u=v_0\) or \(v=v_{t+1}\).

Recall that we write \((i)_m^*\) for the integer in \(\{1, 2, \dots m\}\) congruent to \(i \mod m\). Write \(i = (i)_m^* + \ell _i \cdot m\), and \(j = (j)_m^* + \ell _j \cdot m\).

**Case 1.**If \(u\ne v_0, v\ne v_{t+1}\) and \(j\ne t\), then \(d(u, v)\) is precisely equal to

$$\begin{aligned} & a_{(i)_m^*} + j - i + a_{(j)_m^*} = a_{(i)_m^*} + (j)_m^* - (i)_m^*\\ & \quad + a_{(j)_m^*} + (\ell _j -\ell _i)m = 2 u_{(j)_m^*} + 2 v_{(i)_m^*} + (\ell _j - \ell _i)m, \end{aligned}$$

where we have used the fact that \(a_i+i=2u_i\) and \(a_i-i=2v_i\) for all *i*. Since \(d(u, v) \in [M]\), we must have \(0\le \ell _j-\ell _i\le \lceil M/m\rceil \) and thus

$$ d(u, v) \in 2\cdot (U+V) + m \cdot \{0, \dots , \lceil {M/m}\rceil \} {=}{:} A. $$

But note that \(|A|\le |U+V| \cdot (2M/m)\le 2m\), so there are at most 2*m*distances we can find in this case.

**Case 2.**If \(u\ne v_0\) and \(j=t\), then let \(c\in \mathbb {N}\) be such that the leaves in \(T_t\) are all at distance either \(a_{(t)_m^*}-c\) or \( a_{(t)_m^*}-c-1\) from the root.

We then have that \(d(u, v)\) is precisely either

$$ a_{(t)_m^*} -c + t-i + a_{(i)_m^*} $$

or

$$ a_{(t)_m^*} -c-1 + t-i + a_{(i)_m^*}, $$

i.e. we have \(d(u, v)\in (A-c)\cup (A-c-1)\), and so we obtain at most 4*m*distances in this case.

**Case 3.**If \(u=v_0\), then the cases of \(v=v_{t+1}\) or \(j=t\) provide at most three new distances. If we instead have \(j\ne t\), then \(j\le M\) since \(d(u, v)\le M\), and so \(0\le \ell _j\le \lceil M/m \rceil \). Thus,

$$ d(u, v)=a_{(j)_m^*}+j+1=2u_{(j)_m^*}+1+\ell _j m\in 2\cdot U + 1+ m\cdot \{0, 1, \dots , \lceil M/m\rceil \} $$

which is a set of size at most \(|U+V|\cdot 2M/m\le 2m\).

**Case 4.**If \(v=v_{t+1}\), then the case \(i=t\) provides at most two new distances. Assuming that \(u\ne v_0\) and \(i\ne t\), we have that \(i\ge (t+1)-M\) since \(d(u, v)\le M\), and by proceeding similarly to the previous case we have again at most 2*m*new distances.

Putting everything together, we see that indeed *d*(*u*, *v*) can take at most \(10m+5\le 11m\) distinct values when *u*and *v*do not lie in the same subtree, which completes the proof. \(\square \)

### Proof of Theorem 3

Given *N*in the statement of the theorem, it is clear that we may assume \(n>20N\), say, as for smaller *n*the conclusion follows by considering the almost-perfect tree on *n*vertices, which only has about \(\log n\) leaf-to-leaf path lengths in total. Let \(k\in \mathbb {N}\) be the smallest integer such that \(N \le (169/10)^k\). Set

$$ X = \{1,2,5,7\} \text { and } Y = \{-5,-4,-1,1 \} $$

and observe that

$$ X-Y = [0,12] \text { and } X+Y = \{ -4,-3,-2,0,1,2,3,4,6,8 \}. $$

We further set

$$ U = \left\{ \sum _{i=0}^{k-1} x_i 13^i : x_i \in X \right\} + \frac{13^k-1}{6} +1 $$

and

$$ V = \left\{ \sum _{i=0}^{k-1} y_i 13^i : y_i \in Y \right\} + \frac{13^k-1}{6}. $$

Observe that \(U-V = [13^k]\) and \(\left| U+V\right| = 10^k\). Thus for any even \(n\ge (169/10)^k\), applying Proposition [10][55] with \(m=13^k\) and \(\beta = \log 10 / \log 13\) (and hence \(M=\lfloor (169/10)^k\rfloor \)) gives a tree *T*on *n*vertices with at most \(26M^{\frac{1}{2-\beta }}\) leaf-to-leaf path lengths in [*M*]. In particular, as \(10M/169<N\le M\), there are at most \(500N^{\frac{1}{2-\beta }}\) lengths in [*N*], and so the conclusion of the theorem follows. \(\square \)

Similar constructions to those in the above proof can be found in the work of Ruzsa [[20][56]].

### 3.3 Upper bound on path lengths witnessed by a leaf

### Proof of Theorem 5(ii)

We will provide an explicit construction of an *n*-vertex 1–3 tree in which each individual leaf witnesses at most \(20N^{2/3}\) distinct leaf-to-leaf path lengths between 0 and *N*.

Let \(m :=\lfloor N^{1/3} \rfloor \). Recall that we write \((i)_m\) for the residue of \(i \mod m\), considered as an element of \(\{0, 1,\dots , m-1\}\), and define the sequence \((a_1, \dots , a_{m^2})\) by

$$\begin{aligned} a_i :=\Big \lceil \frac{i}{m} \Big \rceil \cdot m - (i-1)_m . \end{aligned}$$

Observe that \(1 \le a_i \le m^2 \le N^{2/3}\) for each \(i \in [m^2]\). Consider the tree \(T = T_n((a_i)_{i=1}^{m^2})\) described in Section [3.1][54].

We claim that *T*satisfies the conditions of the theorem. Suppose for the sake of contradiction that there is a leaf \(u \in V(T)\) witnessing more than \(20N^{2/3}\) distinct lengths in [0, *N*]. Then \(u\) witnesses at least \(18N^{2/3}\) distinct lengths in \([2N^{2/3}, N]\). We will show how to handle the case when \(u \in T_{j_0}\) for some \(j_0\in [t]\), since the case when \(u \in \{v_0, v_{t+1}\}\) is only easier, as it will be clear by the end of the proof. Set \(q = \lfloor 18N^{2/3}\rfloor \) and let \(s_1, \dots , s_q\) be leaves such that the distances \(d(u, s_i)\) are all distinct and in the interval \([2N^{2/3}, N]\).

Since \(T_{j_0}\) has at most \(N^{2/3}\) layers, every leaf-to-leaf path in \(T_{j_0}\) is of length at most \(2N^{2/3}-2\). But for every \(s_i\) we have \(d(s_i,u) \ge 2N^{2/3} \), and thus \(s_i \notin T_{j_0}\) for all \(i\).

For \(j\ne j_0, t\), any two leaves in \(T_j\) clearly are at the same distance from \(u\), since \(T_j\) is a perfect binary tree; and, provided \(j_0 \ne t\), leaves in \(T_t\) can have at most two distinct distances to \(u\), since leaves in \(T_t\) are spread over at most two layers. Moreover, the only leaves not in any tree \(T_i\) are \(v_0, v_{t+1}\). Therefore, after relabeling the leaves \(s_i\) if necessary, we may assume that for \(1\le i \le q-4\), there exists \(j_i \in [t]\setminus \{ j_0, t\}\) with \(s_i \in T_{j_i} \), and the indices \(j_{i}\) are pairwise distinct.

For each integer \(0 \le k \le t/m^2\), define \(I_k:=\{km^2+1,\dots , (k+1)m^2\}\). Let \(k_0\) satisfy \(I_{k_0} \ni j_0\). For each \(i \in [q-4]\), if \(j_i \in I_k\) then we must have \(|k-k_0| < 2N^{1/3}\) since \(d(s_i, u) \le N\). Then, by pigeonhole there exists *k*such that

$$\begin{aligned} |I_k \cap \{j_i : i \in [q-4]\}| \ge \frac{q-4}{4N^{1/3}} \ge 4N^{1/3} \ge 4m. \end{aligned}$$

We split \(I_k\) into \(I_L = I_k \cap [0, j_0)\) and \(I_R = I_k \cap (j_0, t-1]\), and observe that both \(I_L\) and \(I_R\) are non-empty if and only if \(k=k_0\).

Recall that \(T_{j_i}\) is a perfect binary tree on \(a_{(j_i)_{m^2}^*}\) layers. For every \(i \in [q-4]\) with \(j_i \in I_R\), we have \(j_i > j_0\) and thus

$$\begin{aligned} d(u, s_i) = a_{(j_0)_{m^2}^*} + j_i - j_0+ a_{(j_i)_{m^2}^*} = a_{(j_0)_{m^2}^*} + (j_i)_{m^2}^* + km^2 - j_0+ a_{(j_i)_{m^2}^*}, \end{aligned}$$

(1)

since the distance between \(u\) and \(v_{j_0}\) in \(T_{j_0}\) is \(a_{(j_0)_{m^2}^*}\), the distance between \(v_{j_0}\) and \(v_{j_i}\) in \(P\) is \(j_i - j_0\), and the distance between \(v_{j_i}\) and \(s_i\) in \(T_{j_i}\) is \(a_{(j_i)_{m^2}^*}\). However, from the definition of \(a_{(j_i)_{m^2}^*}\) it easily follows that \(a_{(j_i)_{m^2}^*} + (j_i)_{m^2}^* \equiv 1 \pmod m\), which implies that the RHS of ( [1][57]) can take at most *m*distinct values as \(j_i \in I_R\) varies. Hence we must have \(|I_R| \le m\), which implies \(|I_L| \ge |I_k| - m \ge 3m\).

Similarly, for \(j_i \in I_L\) we have \(j_i < j_0\) and thus

$$\begin{aligned} d(u, s_i) = a_{(j_i)_{m^2}^*} + j_0 - j_i + a_{(j_0)_{m^2}^*} = a_{(j_i)_{m^2}^*} + j_0 - (j_i)_{m^2}^* - km^2 + a_{(j_0)_{m^2}^*}. \end{aligned}$$

(2)

However, for each \(s \in [m^2]\) we see from the definition of \(a_{s}\) that

$$\begin{aligned} -m+1 \le \left( \frac{s}{m}\cdot m - (s-1)_m\right) -s \le a_s - s \le \left( \left( \frac{s}{m} + 1\right) \cdot m - (s-1)_m\right) - s \le m. \end{aligned}$$

This implies that the RHS of ( [2][58]) can take at most 2*m*distinct values as \(j_i \in I_L\) varies. Together with the fact that \(|I_L| \ge 3m\), this yields the desired contradiction.

It is not hard to see that when \(u \in \{v_0,v_{t+1}\}\) essentially the same argument again gives a contradiction. \(\square \)

## 4 Cycles in degree *k*-critical graphs

Recall that an *n*-vertex graph is *degree k-critical*for some \(k \ge 3\) if it has \((k-1)n - {k \atopwithdelims (){2}} + 1\) edges and no proper induced subgraph with minimum degree at least *k*. In this section, we prove a lower bound on the number of cycle lengths in graphs belonging to a general family that contains all degree *k*-critical graphs (i.e. Theorem [12][31] below). By taking \(k = 3\), this result implies Theorem [1][33].

Our first lemma provides a useful ordering of the vertex set of a degree *k*-critical graph; we remark that the case \(k=3\) was already proven in [[12][25], Lemma 1]. Let \(\mathcal {X}=x_1,x_2,\dots ,x_n\) be a given ordering of the vertex set *V*of a graph *G*. For \(x_i\in V\), define \(N_\mathcal {X}^+(x_i)=\{x_j\in N_G(x_i):i<j\}\) and \(N_\mathcal {X}^-(x_i)=\{x_j\in N_G(x_i):i>j\}\). We also define \(d_\mathcal {X}^+(x_i)=|N_\mathcal {X}^+(x_i)|\) and \(d_\mathcal {X}^-(x_i)=|N_\mathcal {X}^-(x_i)|\). We will generally omit the subscript \(\mathcal {X}\) if the ordering is clear from context.

### Lemma 11

Let \(k\ge 3\) and \(n \ge k+1\). Given any *n*-vertex degree *k*-critical graph *G*, there exists an ordering \(\mathcal {X}=x_1, x_2,\dots ,x_n\) of \(V=V(G)\) such that

$$\begin{aligned} d^{+}(x_i)=\left\{ \begin{array}{lcl} k & & \text {if } i=1, \\ k-1 & & \text {if } i\in [2, n-k+1],\\ n-i & & \text {if } i\in [n-k+2, n]. \end{array} \right. \end{aligned}$$

### Proof

We construct the ordering \(x_1, x_2,\dots ,x_n\) iteratively. As a first step, note that by definition there exists a vertex \(x_1\in V\) satisfying \(d_G(x_1)\le k\); otherwise, deleting any vertex in *G*would leave a proper induced subgraph with minimum degree at least *k*.

Assume we have chosen \(\{x_1,\dots ,x_\ell \}\) for some \(\ell \in [n-k]\). Since the minimum degree of the proper induced subgraph \(G[V\setminus \{x_1,\dots ,x_\ell \}]\) is less than *k*, there exists a vertex \(v\in V \setminus \{x_1,\dots ,x_\ell \}\) such that \(|N_G(v)\setminus \{x_1,\dots ,x_\ell \}|\le k-1\). Define \(x_{\ell +1}=v\).

After selecting \(\{x_1,\dots ,x_{n-k+1}\}\), we order the remaining \(k-1\) vertices arbitrarily as \(x_{n-k+2},\dots ,x_n\). Then the ordering \(x_1, x_2,\dots ,x_n\) satisfies \(d^+(x_1)\le k\), \(d^+(x_i)\le k-1\) for \(i\in [2,n-k+1]\), and \(d^+(x_i)\le n-i\) for \(i \in [n-k+2,n]\).

We can thus bound the number of edges in *G*as

$$ |E(G)|=\sum _{i=1}^nd^{+}(x_i) \le k+(k-1)(n-k)+\sum _{i=0}^{k-2}i=n(k-1) - \frac{k(k-1)}{2} + 1. $$

By definition, *G*has exactly \(n(k-1) - \frac{k(k-1)}{2} + 1\) edges, hence all inequalities in the previous expression must hold with equality, which proves the lemma. \(\square \)

Fix an integer \(k\ge 3\). Let *G*be a graph on *n*vertices and let \(\mathcal {X}=x_1, x_2,\dots ,x_n\) be an ordering of *V*(*G*). We say that \((G,\mathcal {X})\) is a *k-ordered graph*if

1. (1)

\(x_{n-1}x_n\in E(G)\),

2. (2)

\(d^+(x_i)\in [2,k]\) for \(i\in [1,n-2],\) and

3. (3)

\(d^-(x_i)\ge 1\) for \(i\in [2,n].\)

Suppose *G*is a degree *k*-critical graph on *n*vertices and let \(\mathcal {X}=x_1, x_2,\dots ,x_n\) be the ordering given by Lemma [11][59]. Then it is easy to verify that \((G,\mathcal {X})\) is a *k*-ordered graph.

Given a graph *G*, we use \(\mathcal {C}_G\) to denote the set of cycle lengths in *G*. We can now state the main result of this section.

### Theorem 12

Let \(k\ge 3\) and \(n\ge k+1\). If \((G,\mathcal {X})\) is a *k*-ordered graph on *n*vertices, then \(|\mathcal {C}_G|\ge \frac{\log n}{3+\log k}-2\).

Throughout the rest of this section, we will assume that \((G,\mathcal {X})\) is a *k*-ordered graph. Let \(u,v\in V(G)\) and \(P=w_1w_2\cdots w_t\) be a path in *G*where \(w_1=u\) and \(w_t=v\). We call *P*a *forward (u,v)-path*if \(w_{i+1}\in N_\mathcal {X}^+(w_i)\) for every \(i\in [t-1]\). In particular, we also view a path consisting of a single vertex as a forward path.

Towards the proof of Theorem [12][31], we start with a series of lemmas. The first lemma establishes a lower bound on \(|\mathcal {C}_G|\) based on the length of the longest forward path in *G*.

### Lemma 13

Let \(k \ge 3\) and let \((G,\mathcal {X})\) be a *k*-ordered graph. For any integer \(\ell \ge 2\), if *G*contains a forward path of length \(\ell \), then \(|\mathcal {C}_G|\ge \log (\ell +1) -1\).

### Proof

Fix a vertex \(v_1\in V(G)\setminus \{x_{n-1},x_n\}\). Let \(P=v_1\cdots v_t\) be a longest forward path starting at \(v_1\). Note that \(d^+(v_1) \ge 2\), and thus \(v_1\) has a forward neighbour \(v' \in V \setminus \{x_n\}\). Since each \(v \in V \setminus \{x_n\}\) satisfies \(d^+(v) \ge 1\), there exists a forward path from \(v'\) to \(x_n\). For the same reason, each longest forward path has \(x_n\) as its endpoint. Thus, \(v_t = x_n\) and \(t \ge 3\).

We claim that \(\mathcal {C}_G\cap [t,2t-2]\ne \emptyset \). We will construct a cycle of suitable length by following a strategy similar to [[3][27]]. Given two vertices \(a, b \in V(P)\), we write \(a < b\) if *a*precedes *b*in *P*, and we write \(a \le b\) if either \(a < b\) or \(a = b\). Given a path *Q*and vertices \(u, v \in Q\), recall that *Q*[*u*, *v*] denotes the unique subpath of *Q*whose endpoints are *u*and *v*. Following the idea in [[5][60]], we define a slightly stronger version of *vine*based on *P*as a collection of internally vertex-disjoint forward paths \(\mathcal {Q} = \{Q_i: i \in [m]\}\) such that the ends of \(Q_i\) are \((a_i, b_i)\) and the following are satisfied:

1. (1)

\(V(Q_i)\cap V(P)=\{a_i,b_i\}\) and \(\ell (P[a_i,b_i])\ge 2\) for every \(i\in [m]\);

2. (2)

\(v_1=a_1<a_2<b_1\le a_3<b_2\le a_4<b_3\le \cdots \le a_m<b_{m-1}<b_m=x_n\); and

3. (3)

\(a_{i+1}\) is the immediate predecessor of \(b_i\) on *P*for every \(i\in [m-1].\)

We will first show the existence of the above structure \(\mathcal {Q}\) based on *P*and then argue that this implies the existence of a cycle of the desired length. For the first of these tasks, we argue inductively that we can construct a collection of paths \(\mathcal {Q}\) satisfying (1), (2), and (3), and then show that satisfying these conditions implies that the paths are internally vertex-disjoint.

Suppose that for some \(r \ge 0\) we have constructed paths \(Q_1, \dots , Q_r\) satisfying (1), (3), as well as

( \(2'\)):

\(v_1 = a_1< a_2< b_1 \le a_3< b_2 \le a_4< b_3 \le \dots \le a_r< b_{r-1} < b_r\).

Let us show how to construct \(Q_{r+1}\). If \(r = 0\), we let \(a_{r+1} = v_1\), and observe that with this choice we have \(d^+(a_{r+1}) \ge 2\). If \(r > 0\), then we may assume that \(b_r < x_n\) as otherwise (2) is also satisfied and we are done. In this case, we let \(a_{r+1}\) be the immediate predecessor of \(b_r\) on *P*, and observe that again \(d^+(a_{r+1}) \ge 2\) since \(a_{r+1}< b_r < x_n\).

Since \(d^+(a_{r+1}) \ge 2\), \(a_{r+1}\) has a neighbour \(c_{r+1} \in N^+(a_{r+1}) \setminus \{b_r\}\). Let \(P_{r+1}\) be a forward \((c_{r+1},x_n)\) -path, and let \(b_{r+1}\) be the vertex in \(V(P_{r+1}) \cap V(P)\) which minimizes \(\ell (P_{r+1}[c_{r+1}, b_{r+1}])\). Indeed, \(x_n \in V(P_{r+1}) \cap V(P)\) and thus such a vertex must exist. Define

$$Q_{r+1} = \{a_{r+1}c_{r+1}\} \cup P_{r+1}[c_{r+1}, b_{r+1}],$$

so that \(Q_{r+1}\) is a forward path. By definition, \(V(Q_{r+1}) \cap V(P) = \{a_{r+1}, b_{r+1}\}\). Moreover, \(\ell (P[a_{r+1}, b_{r+1}]) \ge 2\), since otherwise \(a_{r+1}b_{r+1} \in E(P)\), and as \(Q_{r+1}\) is a forward path it would follow that \(b_{r+1}=b_r\ne c_{r+1}\), and thus \((P \setminus \{a_{r+1}b_{r+1}\}) \cup Q_{r+1}\) is a longer forward path starting at \(v_1\), contradiction. Finally, if \(r \ge 2\), we have \(b_{r-1} \le a_{r+1}\), since \(a_r\) is the predecessor of \(b_{r-1}\) and \(a_{r+1}\) is the predecessor of \(b_r\). This shows that \(Q_1, \dots , Q_{r+1}\) satisfy conditions (1), ( \(2'\)), and (3).

We repeat this procedure as long as possible, eventually obtaining a collection of paths \(\mathcal {Q} = \{Q_1, \dots , Q_m\}\) satisfying (1), (2), and (3). We claim that for any \(i < j\), \(Q_i\) and \(Q_j\) are internally vertex-disjoint. If \(i + 2 \le j\), then (2) implies that \(a_i< b_i \le a_j < b_j\) and thus \(Q_i\) and \(Q_j\) are internally disjoint since they are both forward paths. In the case \(j = i + 1\), suppose for a contradiction that the interiors of \(Q_i\) and \(Q_j\) intersect at \(c \in V(G)\). Then \(Q_{i+1}[a_{i+1},c]\cup Q_i[c,b_i]\) is a forward \((a_{i+1},b_i)\) -path of length at least 2. Hence \(\left( P\setminus \{a_{i+1}b_i\}\right) \cup Q_{i+1}[a_{i+1},c]\cup Q_i[c,b_i]\) is a forward \((v_1,x_n)\) -path of length at least *t*, which is strictly greater than \(\ell (P)\), contradicting the maximality of *P*.

**Fig. 2**

[image: Fig. 2]

[Full size image][61]

An example of the forward path *P*and the path collection \(\mathcal {Q}\) forming a vine. The cycle *C*is illustrated by the bold line

The vine \(\mathcal {Q}\) just constructed yields the cycle (cf. Figure [2][62])

$$\begin{aligned} C=\big (P\setminus \{a_{j+1}b_j:j\in [m-1]\}\big )\cup \left( \bigcup \limits _{i\in [m]}Q_i[a_i,b_i]\right) . \end{aligned}$$

In other words, if *m*is odd, this cycle is precisely

$$\begin{aligned} a_1 Q_1 b_1 \overline{P} a_3 Q_3 b_3 \dots a_m Q_m b_m \overline{P} b_{m-1} Q_{m-1} a_{m-1} \dots a_2 \overline{P} a_1, \end{aligned}$$

whereas if it is even, the cycle we get is

$$\begin{aligned} a_1 Q_1 b_1 \overline{P} a_3 Q_3 b_3 \dots a_{m-1} Q_{m-1} b_{m-1} \overline{P} b_m Q_m a_m \dots a_2 \overline{P} a_1, \end{aligned}$$

where we informally write \(\overline{P}\) above to refer to any subpath between two specified vertices on the path *P*.

It remains to verify that \(\ell (C)\in [t,2t-2]\). Since \(V(C)\supseteq V(P)\), we have that \(\ell (C)\ge t\). We also have \(\ell (Q_i)\le \ell (P[a_i,b_i])\), as otherwise the forward path \(\big (P\setminus P[a_i,b_i]\big )\cup Q_i[a_i,b_i]\) contradicts the maximality of *P*. Hence, we have

$$\begin{aligned} & \ell (C)= \ell (P)+\sum \limits _{i=1}^m\ell (Q_i)-(m-1)\\ & \quad \le \ell (P)+\sum \limits _{i=1}^m\ell (P[a_i,b_i])-(m-1)=2\ell (P)= 2t-2. \end{aligned}$$

Let \(Q=u_1u_2\cdots u_{\ell +1}\) be a longest forward path in *G*, so that \(u_{\ell +1}=x_n\). Then for every \(t\in [2,\ell ]\), \(Q[u_{\ell +1-t},x_n]\) is a longest forward path with \(t+1\ge 3\) vertices starting at the vertex \(u_{\ell +1-t}\) in *G*. By the argument above, each of these paths yields a cycle whose length belongs to the interval \([t+1, 2t]\). Thus, \(\mathcal {C}_G\cap [t+1,2t]\ne \emptyset \) for every \(t\in [2,\ell ]\), which implies \(\mathcal {C}_G\cap [2^s+1,2^{s+1}]\ne \emptyset \) for every \(s\in \big [\lfloor \log \ell \rfloor \big ]\). Since the intervals \([2^s+1,2^{s+1}]\) are pairwise disjoint, we obtain \(|\mathcal {C}_G|\ge \lfloor \log \ell \rfloor \ge \log (\ell +1)-1\), as desired. \(\square \)

Our next goal is to establish a lower bound on \(|\mathcal {C}_G|\) under the assumption that *G*contains no long forward path. Our proof proceeds by defining a suitable partial order on *V*(*G*) and then showing that the absence of long forward paths in *G*implies the absence of long chains in this partial order. Thanks to the following classical theorem, this will allow us to reduce the problem to the case where *G*has a long antichain.

### Theorem 14

(Dilworth [[8][63]]) In any finite partial order, the maximum size of an antichain is equal to the minimum number of chains required to cover all its elements.

Let \((G,\mathcal {X})\) be a *k*-ordered graph and let \(V=V(G)\). For \(u,v\in V\), let \(u\preceq v\) if there exists a forward (*u*, *v*)-path in *G*. It is easy to see that \((V, \preceq )\) is a partial order. We call \((V,\preceq )\) the partial order *generated by*\(\mathcal {X}\). We also write \(u\prec v\) when \(u\preceq v\) and \(u\ne v\). Observe that if \(v_1\prec v_2\prec \cdots \prec v_\ell \) is a chain under the partial order \((V,\preceq )\), then there exists a forward path *P*such that \(v_1,v_2,\cdots , v_\ell \) occur sequentially along *P*. Hence if every forward path in *G*has length at most \(\ell \), then every chain under \((V,\preceq )\) contains at most \(\ell +1\) elements. If so, by Theorem [14][64], \((V, \preceq )\) contains an antichain on at least \(n/(\ell + 1)\) elements.

The next lemma shows that, given any antichain *L*, one can find two trees whose leaf set is precisely *L*and which have no other vertices in common. A subtree *T*of *G*rooted at *u*is called *forward-directed*(resp. *backward-directed*) if

1. (1)

for any subpath \(P=u_1u_2\cdots u_t\) of *T*with \(u_1=u\) and \(u_t\in L(T)\), \(u_i\preceq u_{i+1}\) (resp. \(u_{i+1}\preceq u_i\)) for every \(i\in [t-1]\); and

2. (2)

either \(d_T(u)\ge 2\) or *T*consists of a single vertex.

Hence the root of a forward-directed (resp. backward-directed) tree *T*is its minimum (maximum) vertex under \(\preceq \).

### Lemma 15

Let \((G,\mathcal {X})\) be a *k*-ordered graph for some \(k \ge 3\) and let \((V,\preceq )\) be the partial order generated by \(\mathcal {X}\). Then for any given antichain \(L=\{v_1,v_2,\cdots ,v_m\}\) under \(\preceq \), there exist a forward-directed subtree *S*and a backward-directed subtree *T*of *G*satisfying \(L(S)=L(T)=L\).

### Proof

We will just prove the existence of a forward-directed tree *S*such that \(L(S)=L\), since, as will be clear by the end of the proof, the existence of the required backward-directed tree follows by symmetry.

*S*is constructed through the following procedure. At the start, we let \(S_1 = \{v_1\}\), which we view as a one-vertex tree rooted at \(v_1\). Now, suppose that we have already constructed a forward-directed tree \(S_i\) for some integer \(i\in [m-1]\), and that \(L(S_i)=\{v_1,\cdots , v_i\}\). Let \(u_i\) be the root of \(S_i\). Then \(v_{i+1}\preceq u_i\) cannot hold, as otherwise \(v_{i+1}\preceq u_i\preceq v_1\), contradicting the fact that *L*forms an antichain under \(\preceq \).

We will now show how to extend \(S_i\) to a larger forward-directed tree \(S_{i+1}\) with \(L(S_{i+1}) = \{v_1, \dots , v_{i+1}\}\). We split into two cases.

**Case 1:**\(u_i\prec v_{i+1}\).

Note that this cannot happen when \(i=1\), hence we may assume that \(|L(S_i)|\ge 2\) and \(d_{S_{i}}(u_i)\ge 2\). Let \(v\in V(S_{i})\) be a maximal vertex under \(\preceq \) such that \(v\preceq v_{i+1}\). Select an arbitrary forward \((v,v_{i+1})\) path *P*in *G*, which implies \(V(P)\cap V(S_{i})=\{v\}\) by maximality of *v*. Let \(S_{i+1}=S_i\cup P\), and observe that \(d_{S_{i+1}}(u_i)\ge d_{S_{i}}(u_i)\ge 2\). Thus, \(S_{i+1}\) is a forward-directed tree rooted at \(u_i\) such that \(L(S_{i+1})=\{v_1,\cdots , v_{i+1}\}\).

**Case 2:**\(u_i\nprec v_{i+1}\).

Let \(w\in V(G)\) be a maximal vertex under \(\preceq \) such that \(w\preceq v_{i+1}\) and \(w\preceq u_i\). Indeed, such a vertex *w*exists since \(x_1 \preceq u_i\) and \(x_1 \preceq v_{i+1}\) (recall that each vertex \(x \in V(G) \setminus \{x_1\}\) satisfies \(d^-(x) \ge 1\), and thus \(x_1 \preceq x\)). Select an arbitrary forward \((w,u_i)\) path *P*and an arbitrary forward \((w,v_{i+1})\) path *Q*. Then, our choice of *w*and the fact that \(u_i \nprec v_{i+1}\) imply that \(V(P)\cap V(S_i)=\{u_i\}\), \(V(Q)\cap V(S_i)=\emptyset \), and \(V(P)\cap V(Q)=\{w\}\). Letting \(S_{i+1}=S_i\cup P\cup Q\), we have \(d_{S_{i+1}}(w)\ge 2\). Thus, \(S_{i+1}\) is a forward-directed tree rooted at *w*such that \(L(S_{i+1})=\{v_1,\cdots , v_{i+1}\}\).

The algorithm terminates with a forward-directed tree \(S_m\) with \(L(S_m)=L\), as required. It can be easily checked that the same argument yields a backward-directed tree *T*such that \(L(T) = L\). The only part of the argument that does not follow directly from the symmetry of the partial order is in Case 2, where we instead use the fact that \(x \preceq x_n\) for each \(x \in V(G) \setminus \{x_n\}\) since \(d^+(x)\ge 1\). \(\square \)

We call a tree *T*rooted at *u**fair*if, for some \(q \ge 1\), each leaf \(x \in L(T)\) satisfies \(d(u,x) = q\). The following lemma shows that by reducing the size of the antichain *L*by at most a constant factor, we can essentially assume that the forward-directed and backward-directed subtrees guaranteed by Lemma [15][65] are both fair.

### Lemma 16

Let \(k \ge 3, c \ge 1\). Let \((G,\mathcal {X})\) be a *k*-ordered graph with no forward path of length *c*, and let \((V, \preceq )\) be the partial order generated by \(\mathcal {X}\). Then *G*contains an antichain \(L_0 \subseteq V\), a fair forward-directed tree \(S_0\), and a fair backward-directed tree \(T_0\), satisfying \(L(S_0) = L(T_0) = L_0\). Moreover, \(|L_0|\ge \frac{|V|}{c^3}\).

### Proof

First, observe that if \(|V| \le c^3\), then the statement can be seen to be trivially true by choosing \(L_0 = \{v\}\) where \(v \in V\) is arbitrary, and letting \(S_0\) and \(T_0\) be one-vertex trees with vertex set \(\{v\}\). With this choice, \(|L_0| = 1 \ge |V|/c^3\).

From now on, we will assume that \(|V| > c^3\). By our assumption on the length of forward paths in \((G, \mathcal {X})\), every chain under \(\preceq \) contains at most *c*elements. By Theorem [14][64], this implies that there is an antichain *L*satisfying \(|L|\ge \frac{|V|}{c}\).

By Lemma [15][65], there exist a forward-directed tree *S*rooted at *u*and a backward-directed tree *T*rooted at *v*with \(L(S)=L(T)=L\). Observe that the path in *S*connecting *u*to any given \(w \in L\) is a forward path, and thus of length at most *c*. So, there is a subset \(L_1\subseteq L\) with \(|L_1|\ge \frac{|L|}{c} \ge \frac{|V|}{c^2} \ge 2\) such that any two leaves in \(L_1\) are at the same distance from *u*in *S*. Let \(S_1\) and \(T_1\) be the unique subtrees of *S*and *T*such that \(L(S_1)=L(T_1)=L_1\). Let \(u'\in V(S_1)\) be the minimum vertex under \(\prec \). Then \(d_{S_1}(u') \ge 2\) and \(S_1\) is a forward-directed tree rooted at \(u'\). Analogously, by choosing \(v'\in V(T_1)\) to be the maximum vertex under \(\prec \), we get that \(T_1\) is a backward-directed tree rooted at \(v'\). Moreover, \(S_1\) is fair.

We now apply a similar procedure to \(T_1\). Again, there must be a subset \(L_0 \subseteq L_1\) with \(|L_0|\ge \frac{|L_1|}{c} \ge \frac{|V|}{c^3} >1\) such that any two leaves in \(L_0\) are at the same distance from \(v'\) in \(T_1\). Let \(S_0\) and \(T_0\) be the unique subtrees of \(S_1\) and \(T_1\) respectively, such that \(L(S_0)=L(T_0)=L_0\). By the same argument as before, \(S_0\) is a forward-directed tree and \(T_0\) is a backward-directed tree. Moreover, both \(S_0\) and \(T_0\) are fair, as required. \(\square \)

Next, we obtain a lower bound on \(|\mathcal {C}_G|\) using the structure from Lemma [16][66]. It will be sufficient for our purposes to consider cycles of a special kind. We call a cycle *C**good*if *C*is the union of two internally-disjoint forward (*u*, *v*)-paths for two vertices \(u,v\in V\). Denote the set of all lengths of good cycles in *G*by \(\mathcal {C}_1(G)\).

### Lemma 17

Let \(k\ge 3, \Delta \ge 2\), and let \((G,\mathcal {X})\) be a *k*-ordered graph. Suppose that *S*is a fair forward-directed tree in *G*, and that *T*is a fair backward-directed tree in *G*, such that \(L(S) = L(T) =L\) where \(|L| \ge 2\). Further assume that \(\Delta (S) \le \Delta \). Then \(|\mathcal {C}_1(S\cup T)|\ge \frac{\log |L|}{\log \Delta }\).

### Proof

Let \((V,\preceq )\) be the partial order generated by \(\mathcal {X}\). We prove the lemma by induction on |*L*|. As a base case, let \(|L|\in [2,\Delta ]\). Pick any two leaves in *L*, and note that they are connected by a path \(P_1\) in *S*and a path \(P_2\) in *T*. Then, \(P_1 \cup P_2\) is a good cycle, so that \(|\mathcal {C}_1(S\cup T)|\ge 1 \ge \frac{\log |L|}{\log \Delta }\).

Assume that the lemma holds for \(|L|\le t-1\) and consider the case \(|L|=t>\Delta \). Let *u*and *v*be the roots of *S*and *T*respectively. Let \(r_1, \dots , r_{\Delta '}\) ( \(\Delta ' \le \Delta \)) be the neighbours of *u*in *S*. Observe that for some \(i \in [\Delta ']\) the subtree \(S'\) rooted at \(r_i\) obtained by deleting *u*from *S*contains at least \(|L|/\Delta \ge 2\) leaves distinct from \(r_i\). Let \(u_0\) be maximal under \(\preceq \) such that \(u_0\) is contained in every path from \(r_i\) to \(L(S')\) in *S*. Let \(S_0\) be the unique subtree of \(S'\) whose leaf set is precisely \(L_0:= L(S')\), then \(S_0\) is a fair forward-directed tree rooted at \(u_0\) with \(|L_0|\ge |L|/\Delta \). Let \(T_0\subseteq T\) be the unique backward-directed subtree of *T*with \(L(T_0)=L_0\). Letting \(v_0\) be the minimal vertex under \(\preceq \) that is on every path from *v*to \(L_0\) in *T*, we view \(T_0\) as rooted at \(v_0\), so that \(T_0\) is also fair.

By the inductive hypothesis applied to \(L_0\), \(S_0\) and \(T_0\), we have

$$|\mathcal {C}_1(S_0\cup T_0)|\ge \frac{\log |L_0|}{\log \Delta } \ge \frac{\log |L|}{\log \Delta }-1.$$

Let \(d_S, d_T \ge 1\) satisfy \(d_S(u, w) = d_S\) and \(d_T(v, w) = d_T\) for each \(w \in L\). Any cycle contained in \(S_0 \cup T_0\) is of length at most \(2 d_{S} + 2 d_{T}- 2\). Therefore, to complete the proof it suffices to show that there exists a good cycle in \(S \cup T\) containing *u*and *v*, which must have length precisely \(2d_S + 2d_T\).

Suppose otherwise. By our choice of \(L_0\), every subpath of *S*connecting \(L_0\) and \(L \setminus L_0\) must contain *u*. So, we may assume that every subpath in *T*connecting \(L_0\) and \(L \setminus L_0\) avoids *v*. Let \(r'_1, \dots , r'_{\Delta ''}\) ( \(\Delta '' \le \Delta \)) be the neighbours of *v*in *T*, and let \(T_{i}\) ( \(i \in [\Delta '']\)) be the subtree of *T*containing \(r'_i\) after deleting *v*. If there are distinct \(i, j \in [\Delta '']\) such that \(L_0 \cap V(T_i)\) and \((L \setminus L_0) \cap V(T_j)\) are non-empty, then we obtain a path from *L*to \(L\setminus L_0\) in *T*containing *v*(passing through \(r'_i\) and \(r'_j\)), giving a contradiction. Thus, there is some \(i \in [\Delta '']\) such that \(L = L_0 \cup (L \setminus L_0) \subseteq V(T_i)\), which is only possible if \(d_T(v) = 1\), contradicting the fact that *T*is a backward-directed tree.

Hence, there exists a good cycle in \(S \cup T\) containing *u*and *v*. This cycle is necessarily of length \(2d_S + 2d_T\), and thus

$$|\mathcal {C}_1(S\cup T)|\ge |\mathcal {C}_1(S_0\cup T_0)|+1\ge \frac{\log |L|}{\log \Delta },$$

which completes the proof. \(\square \)

Finally, we are ready to complete the proof of Theorem [12][31].

### Proof of Theorem 12

Suppose the maximum length of a forward path in *G*is \(c-1\). By Lemma [13][67], \(|\mathcal {C}_G|\ge \log c-1\). Hence if \(n<2c^3\), we have \(|\mathcal {C}_G|\ge \frac{\log n-4}{3}>\frac{\log n}{3+\log k}-2\). Consider the case \(n\ge 2c^3\). Applying Lemma [16][66], we obtain \(L\subseteq V\), a fair forward-directed subtree *S*and a fair backward-directed subtree *T*of *G*, satisfying \(L(S)=L(T)=L\) and \(|L|\ge \frac{n}{c^3} \ge 2\). Since \((G,\mathcal {X})\) is *k*-ordered, *S*has maximum degree at most *k*. From Lemma [17][68], it follows that

$$|\mathcal {C}_G|\ge \big |\mathcal {C}_1(S\cup T)\big |\ge \frac{\log |L|}{\log k}\ge \frac{\log n-3\log c}{\log k}.$$

Now we complete the proof by deducing that

$$\begin{aligned} \big |\mathcal {C}_G\big |&\ge \min _{c>0}\max \left\{ \log c-1,\frac{\log n-3\log c}{\log k}\right\} =\frac{\log n-3}{3+\log k}, \end{aligned}$$

where \(\max \left\{ \log c-1,\frac{\log n-3\log c}{\log k}\right\} \) achieves its minimum when \(\log c=\frac{\log n+\log k}{3+\log k}\). \(\square \)

Theorem [1][33] promptly follows by setting \(k = 3\) and combining Lemma [11][59] with Theorem [12][31].

## 5 Conclusion and open problems

In this paper, we answered several questions of Narins, Pokrovskiy and Szabó [[18][29]] on lengths of cycles in degree-critical graphs and leaf-to-leaf paths in trees. We have proven Conjecture [B][34] and disproven Conjecture [C][36], but several questions still remain. The most obvious one would be to improve the leading coefficient of the bound we prove in Theorem [1][33] and completely settle Conjecture [A][30].

Another interesting question is to determine ‘how far’ Conjecture [C][36] is from being true, i.e. find the value of the best possible constant *c*in Theorem [3][37].

### Problem D

Determine the supremum \(c^*\) over all \(c\in [0, 1]\) for which the following holds: for all *N*and all sufficiently large even *n*(as a function of *N*and *c*), every *n*-vertex 1–3 tree contains leaf-to-leaf paths of \(\Omega (N^{c})\) distinct lengths between 0 and *N*.

We do not have a guess for what the true value of \(c^*\) should be. Theorem [4][38] shows that \(c^*\ge 2/3\). In the proof of Theorem [4][38], however, we could only obtain leaf-to-leaf paths which are all witnessed by the same leaf, and Theorem [5][39] shows that our bound in this setting is essentially best possible. It is natural to attempt and improve this lower bound on \(c^*\) by sharpening the bound in Lemma [9][51], i.e. improving on the lower bound \(c'\ge 2/3\) in the setting below.

### Problem E

Determine the supremum \(c'\) over all \(c\in [0, 1]\) for which the following holds: for all sufficiently large *n*and all sequences \((a_i)_{i=1}^n\) of non-negative integers such that \(a_i \le n^{c}\), we have

$$\begin{aligned} |\{a_i + a_j + (j - i) : 1 \le i < j \le n\}| =\Omega \left( n^{c}\right) . \end{aligned}$$

On the other hand, Theorem [3][37] shows that \(c^*\le \left( 2-\frac{\log 10}{\log 13} \right) ^{-1}\approx 0.9073\), and a straightforward application of the Ruzsa triangle inequality shows that our proof method cannot improve this beyond 0.75 (more specifically, it is proven in [[20][56]] that one has \(|U+V|\ge |U-V|^{2/3}\) for any \(U, V\subseteq \mathbb {Z}\), so we cannot take \(\beta <2/3\) in Proposition [10][55]).

As a related problem, it would be interesting to determine the optimal value of \(\beta \) that one could take in Proposition [10][55]. We remark that even the more basic question of determining how small \(A+B\) can be relative to \(A-B\) for \(A, B\subseteq \mathbb {N}\) seems to be wide open – the best bound we are aware of is the construction of Cutler, Pebody, and Sarkar [[7][69]] which gives \(|A+A|\le |A-A|^{0.868}.\)

Lastly, let us mention one more problem stated in [[18][29]].

### Problem F

( [[18][29], Problem 6.1]) Is there a function *C*(*n*) tending to infinity such that every degree 3-critical graph on *n*vertices contains cycles of all lengths 4, 6, 8, ..., 2*C*(*n*)?

The tools used in the present paper seem insufficient to be able to answer this, and we do not speculate on what the answer might be.

## Notes

1.

Unless indicated otherwise, logarithms throughout this paper are base 2.

## References

1.

Bauer, D., Schmeichel, E.: Hamiltonian degree conditions which imply a graph is pancyclic. J. Comb. Theory Ser. B **48**(1), 111–116 (1990)

[Article][70] [Google Scholar][71]

2.

Bollobás, B.: Modern Graph Theory. Graduate Texts in Mathematics, vol. 184. Springer, New York (1998)

3.

Bollobás, B., Brightwell, G.: Long cycles in graphs with no subgraphs of minimal degree 3. In Annals of Discrete Mathematics, volume 43, pages 47–53. Elsevier, J. Comb. Theory Ser. B (1989)

4.

Bondy, J.A.: Pancyclic graphs I. J. Comb. Theory Ser. B **11**(1), 80–84 (1971)

5.

Bondy, J.A., Locke, S.C.: Relative lengths of paths and cycles in 3-connected graphs. Discret. Math. **33**(2), 111–122 (1981)

[Article][72] [Google Scholar][73]

6.

Bucić, M., Gishboliner, L., Sudakov, B.: Cycles of many lengths in Hamiltonian graphs. Forum Math. Sigma **10**, e70 (2022)

[Article][74] [Google Scholar][75]

7.

Cutler, J., Pebody, L., Sarkar, A.: Sums, Differences and Dilates. arXiv preprint [arXiv:2402.18297][76], (2024)

8.

Dilworth, R.P.: A decomposition theorem for partially ordered sets. Ann. Math. **51**(1), 161–166 (1950)

[Article][77] [Google Scholar][78]

9.

Draganić, N., Correia, D. M., Sudakov, B.: Pancyclicity of Hamiltonian graphs. J. Eur. Math. Soc. (2024)

10.

Erdős, P.: Problems and results in combinatorial analysis and combinatorial number theory. Graph theory, combinatorics, and applications, Vol. 1 (Kalamazoo, MI, 1988):397–406 (1991)

11.

Erdős, P.: Some of my favorite solved and unsolved problems in graph theory. Quaest. Math. **16**(3), 333–350 (1993)

[Article][79] [Google Scholar][80]

12.

Erdős, P., Faudree, R.J., Gyárfás, A., Schelp, R.H.: Cycles in graphs without proper subgraphs of minimum degree 3. Ars Combinatorica **25**, 195–201 (1988)

[Google Scholar][81]

13.

Erdős, P., Szekeres, G.: A combinatorial problem in geometry. Compos. Math. **2**, 463–470 (1935)

[Google Scholar][82]

14.

Gyárfás, A., Komlós, J., Szemerédi, E.: On the distribution of cycle lengths in graphs. J. Graph Theory **8**(4), 441–462 (1984)

[Article][83] [Google Scholar][84]

15.

Gyárfás, A., Lehel, J.: A Helly-type problem in trees. In: Combinatorial theory and its applications. I-III (Proceedings of the Colloquium held at Balatonfüred, 1969), volume 4 of Colloquia Mathematica Societatis János Bolyai, pp. 571–584. North-Holland, Amsterdam-London (1970)

16.

Horn, W.A.: Three results for trees, using mathematical induction. J. Res. Natl. Bur. Stand. **76B**, 39–43 (1972)

[Article][85] [Google Scholar][86]

17.

Letzter, S.: Pancyclicity of highly connected graphs. arXiv preprint [arXiv:2306.12579][87], (2023)

18.

Narins, L., Pokrovskiy, A., Szabó, T.: Graphs without proper subgraphs of minimum degree 3 and short cycles. Combinatorica **37**, 495–519 (2017)

[Article][88] [Google Scholar][89]

19.

C. St. J. A. Nash-Williams.: Decomposition of finite graphs into forests. J. Lond. Math. Soc. **s1–39**(1), 12–12 (1964)

20.

Ruzsa, I.: Sums of finite sets. In D.V. Chudnovsky, G.V. Chudnovsky, and M.B. Nathanson, editors, Number Theory: New York Seminar. Springer-Verlag (1996)

21.

Sauermann, L.: A proof of a conjecture of Erdős, Faudree, Rousseau and Schelp on subgraphs of minimum degree \(k\). J. Comb. Theory Ser. B **134**, 36–75 (2019)

[Article][90] [Google Scholar][91]

22.

Sudakov, B., Verstraëte, J.: Cycle lengths in sparse graphs. Combinatorica **28**(3), 357–372 (2008)

[Article][92] [Google Scholar][93]

[Download references][94]

## Acknowledgements

We thank the anonymous referees for their careful reading of this paper and their valuable comments. We would also like to thank Jozef Skokan for a careful reading of a preliminary version of this manuscript.

## Author information

### Authors and Affiliations

1.

Department of Mathematics, London School of Economics, London, UK

Francesco Di Braccio

2.

Department of Mathematics, University College London, London, UK

Kyriakos Katsamaktsis

3.

School of Mathematical Sciences, University of Science and Technology of China, Hefei, Anhui, 230026, China

Jie Ma & Ziyuan Zhao

4.

Yau Mathematical Sciences Center, Tsinghua University, Beijing, 100084, China

Jie Ma

5.

Mathematical Institute, University of Oxford, England, UK

Alexandru Malekshahian

6.

Department of Mathematics, King’s College London, London, UK

Alexandru Malekshahian

Authors

1. Francesco Di Braccio

[View author publications][95]

Search author on: [PubMed][96] [Google Scholar][97]

2. Kyriakos Katsamaktsis

[View author publications][98]

Search author on: [PubMed][99] [Google Scholar][100]

3. Jie Ma

[View author publications][101]

Search author on: [PubMed][102] [Google Scholar][103]

4. Alexandru Malekshahian

[View author publications][104]

Search author on: [PubMed][105] [Google Scholar][106]

5. Ziyuan Zhao

[View author publications][107]

Search author on: [PubMed][108] [Google Scholar][109]

### Corresponding author

Correspondence to [Francesco Di Braccio][110].

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Kyriakos Katsamaktsis: Research supported by the Engineering and Physical Sciences Research Council [grant number EP/W523835/1]. Jie Ma: Research supported by National Key Research and Development Program of China 2023YFA1010201 and National Natural Science Foundation of China grant 12125106. Ziyuan Zhao: Research supported by Innovation Program for Quantum Science and Technology 2021ZD0302902.

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][111].

[Reprints and permissions][112]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [113]

### Cite this article

Braccio, F.D., Katsamaktsis, K., Ma, J. *et al.*Leaf-to-leaf paths and cycles in degree-critical graphs. *Combinatorica***46**, 11 (2026). https://doi.org/10.1007/s00493-026-00205-2

[Download citation][114]

-

Received: 24 April 2025

-

Revised: 28 January 2026

-

Accepted: 28 January 2026

-

Published: 04 March 2026

-

Version of record: 04 March 2026

-

DOI: https://doi.org/10.1007/s00493-026-00205-2

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s00493-026-00205-2.pdf
[3]: /article/10.1007/s00493-026-00205-2/save-research?_csrf=bqX7i6XGCiRtVtkv2jomM05KaPsLP28F
[4]: /saved-research
[5]: /journal/493
[6]: /journal/493/aims-and-scope
[7]: https://ef.msp.org/submit/combinatorica
[8]: https://link.springer.com/10.1007/978-3-031-63021-7_26?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/978-3-319-94667-2_8?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/s00453-020-00720-8?fromPaywallRec=false
[11]: /subjects/combinatorics
[12]: /subjects/criticality
[13]: /subjects/discrete-mathematics
[14]: /subjects/graph-theory
[15]: /subjects/graph-theory-in-probability
[16]: /subjects/leaf-development
[17]: /article/10.1007/s00493-026-00205-2#ref-CR4
[18]: /article/10.1007/s00493-026-00205-2#ref-CR1
[19]: /article/10.1007/s00493-026-00205-2#ref-CR6
[20]: /article/10.1007/s00493-026-00205-2#ref-CR9
[21]: /article/10.1007/s00493-026-00205-2#ref-CR17
[22]: /article/10.1007/s00493-026-00205-2#ref-CR22
[23]: /article/10.1007/s00493-026-00205-2#ref-CR11
[24]: /article/10.1007/s00493-026-00205-2#ref-CR14
[25]: /article/10.1007/s00493-026-00205-2#ref-CR12
[26]: /article/10.1007/s00493-026-00205-2#ref-CR19
[27]: /article/10.1007/s00493-026-00205-2#ref-CR3
[28]: /article/10.1007/s00493-026-00205-2#ref-CR10
[29]: /article/10.1007/s00493-026-00205-2#ref-CR18
[30]: /article/10.1007/s00493-026-00205-2#FPar1
[31]: /article/10.1007/s00493-026-00205-2#FPar23
[32]: /article/10.1007/s00493-026-00205-2#ref-CR21
[33]: /article/10.1007/s00493-026-00205-2#FPar2
[34]: /article/10.1007/s00493-026-00205-2#FPar3
[35]: /article/10.1007/s00493-026-00205-2#FPar4
[36]: /article/10.1007/s00493-026-00205-2#FPar5
[37]: /article/10.1007/s00493-026-00205-2#FPar6
[38]: /article/10.1007/s00493-026-00205-2#FPar7
[39]: /article/10.1007/s00493-026-00205-2#FPar8
[40]: /article/10.1007/s00493-026-00205-2#Sec12
[41]: /article/10.1007/s00493-026-00205-2#ref-CR2
[42]: /article/10.1007/s00493-026-00205-2#Sec4
[43]: /article/10.1007/s00493-026-00205-2#Sec7
[44]: /article/10.1007/s00493-026-00205-2#Sec11
[45]: /article/10.1007/s00493-026-00205-2#FPar9
[46]: /article/10.1007/s00493-026-00205-2#ref-CR15
[47]: /article/10.1007/s00493-026-00205-2#ref-CR16
[48]: /article/10.1007/s00493-026-00205-2#FPar11
[49]: /article/10.1007/s00493-026-00205-2#ref-CR13
[50]: /article/10.1007/s00493-026-00205-2#FPar13
[51]: /article/10.1007/s00493-026-00205-2#FPar14
[52]: /article/10.1007/s00493-026-00205-2#Fig1
[53]: /article/10.1007/s00493-026-00205-2/figures/1
[54]: /article/10.1007/s00493-026-00205-2#Sec8
[55]: /article/10.1007/s00493-026-00205-2#FPar17
[56]: /article/10.1007/s00493-026-00205-2#ref-CR20
[57]: /article/10.1007/s00493-026-00205-2#Equ1
[58]: /article/10.1007/s00493-026-00205-2#Equ2
[59]: /article/10.1007/s00493-026-00205-2#FPar21
[60]: /article/10.1007/s00493-026-00205-2#ref-CR5
[61]: /article/10.1007/s00493-026-00205-2/figures/2
[62]: /article/10.1007/s00493-026-00205-2#Fig2
[63]: /article/10.1007/s00493-026-00205-2#ref-CR8
[64]: /article/10.1007/s00493-026-00205-2#FPar26
[65]: /article/10.1007/s00493-026-00205-2#FPar27
[66]: /article/10.1007/s00493-026-00205-2#FPar29
[67]: /article/10.1007/s00493-026-00205-2#FPar24
[68]: /article/10.1007/s00493-026-00205-2#FPar31
[69]: /article/10.1007/s00493-026-00205-2#ref-CR7
[70]: https://doi.org/10.1016%2F0095-8956%2890%2990133-K
[71]: http://scholar.google.com/scholar_lookup?amp;title=Hamiltonian%20degree%20conditions%20which%20imply%20a%20graph%20is%20pancyclic&amp;journal=J.%20Comb.%20Theory%20Ser.%20B&amp;doi=10.1016%2F0095-8956%2890%2990133-K&amp;volume=48&amp;issue=1&amp;pages=111-116&amp;publication_year=1990&amp;author=Bauer%2CD&amp;author=Schmeichel%2CE
[72]: https://doi.org/10.1016%2F0012-365X%2881%2990159-X
[73]: http://scholar.google.com/scholar_lookup?amp;title=Relative%20lengths%20of%20paths%20and%20cycles%20in%203-connected%20graphs&amp;journal=Discret.%20Math.&amp;doi=10.1016%2F0012-365X%2881%2990159-X&amp;volume=33&amp;issue=2&amp;pages=111-122&amp;publication_year=1981&amp;author=Bondy%2CJA&amp;author=Locke%2CSC
[74]: https://doi.org/10.1017%2Ffms.2022.42
[75]: http://scholar.google.com/scholar_lookup?amp;title=Cycles%20of%20many%20lengths%20in%20Hamiltonian%20graphs&amp;journal=Forum%20Math.%20Sigma&amp;doi=10.1017%2Ffms.2022.42&amp;volume=10&amp;publication_year=2022&amp;author=Buci%C4%87%2CM&amp;author=Gishboliner%2CL&amp;author=Sudakov%2CB
[76]: https://arxiv.org/pdf/2402.18297
[77]: https://doi.org/10.2307%2F1969503
[78]: http://scholar.google.com/scholar_lookup?amp;title=A%20decomposition%20theorem%20for%20partially%20ordered%20sets&amp;journal=Ann.%20Math.&amp;doi=10.2307%2F1969503&amp;volume=51&amp;issue=1&amp;pages=161-166&amp;publication_year=1950&amp;author=Dilworth%2CRP
[79]: https://doi.org/10.1080%2F16073606.1993.9631741
[80]: http://scholar.google.com/scholar_lookup?amp;title=Some%20of%20my%20favorite%20solved%20and%20unsolved%20problems%20in%20graph%20theory&amp;journal=Quaest.%20Math.&amp;doi=10.1080%2F16073606.1993.9631741&amp;volume=16&amp;issue=3&amp;pages=333-350&amp;publication_year=1993&amp;author=Erd%C5%91s%2CP
[81]: http://scholar.google.com/scholar_lookup?amp;title=Cycles%20in%20graphs%20without%20proper%20subgraphs%20of%20minimum%20degree%203&amp;journal=Ars%20Combinatorica&amp;volume=25&amp;pages=195-201&amp;publication_year=1988&amp;author=Erd%C5%91s%2CP&amp;author=Faudree%2CRJ&amp;author=Gy%C3%A1rf%C3%A1s%2CA&amp;author=Schelp%2CRH
[82]: http://scholar.google.com/scholar_lookup?amp;title=A%20combinatorial%20problem%20in%20geometry&amp;journal=Compos.%20Math.&amp;volume=2&amp;pages=463-470&amp;publication_year=1935&amp;author=Erd%C5%91s%2CP&amp;author=Szekeres%2CG
[83]: https://doi.org/10.1002%2Fjgt.3190080402
[84]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20distribution%20of%20cycle%20lengths%20in%20graphs&amp;journal=J.%20Graph%20Theory&amp;doi=10.1002%2Fjgt.3190080402&amp;volume=8&amp;issue=4&amp;pages=441-462&amp;publication_year=1984&amp;author=Gy%C3%A1rf%C3%A1s%2CA&amp;author=Koml%C3%B3s%2CJ&amp;author=Szemer%C3%A9di%2CE
[85]: https://doi.org/10.6028%2Fjres.076B.002
[86]: http://scholar.google.com/scholar_lookup?amp;title=Three%20results%20for%20trees%2C%20using%20mathematical%20induction&amp;journal=J.%20Res.%20Natl.%20Bur.%20Stand.&amp;doi=10.6028%2Fjres.076B.002&amp;volume=76B&amp;pages=39-43&amp;publication_year=1972&amp;author=Horn%2CWA
[87]: https://arxiv.org/pdf/2306.12579
[88]: https://link.springer.com/doi/10.1007/s00493-015-3310-9
[89]: http://scholar.google.com/scholar_lookup?amp;title=Graphs%20without%20proper%20subgraphs%20of%20minimum%20degree%203%20and%20short%20cycles&amp;journal=Combinatorica&amp;doi=10.1007%2Fs00493-015-3310-9&amp;volume=37&amp;pages=495-519&amp;publication_year=2017&amp;author=Narins%2CL&amp;author=Pokrovskiy%2CA&amp;author=Szab%C3%B3%2CT
[90]: https://doi.org/10.1016%2Fj.jctb.2018.05.002
[91]: http://scholar.google.com/scholar_lookup?amp;title=A%20proof%20of%20a%20conjecture%20of%20Erd%C5%91s%2C%20Faudree%2C%20Rousseau%20and%20Schelp%20on%20subgraphs%20of%20minimum%20degree%20%24%24k%24%24%20k&amp;journal=J.%20Comb.%20Theory%20Ser.%20B&amp;doi=10.1016%2Fj.jctb.2018.05.002&amp;volume=134&amp;pages=36-75&amp;publication_year=2019&amp;author=Sauermann%2CL
[92]: https://link.springer.com/doi/10.1007/s00493-008-2300-6
[93]: http://scholar.google.com/scholar_lookup?amp;title=Cycle%20lengths%20in%20sparse%20graphs&amp;journal=Combinatorica&amp;doi=10.1007%2Fs00493-008-2300-6&amp;volume=28&amp;issue=3&amp;pages=357-372&amp;publication_year=2008&amp;author=Sudakov%2CB&amp;author=Verstra%C3%ABte%2CJ
[94]: https://citation-needed.springer.com/v2/references/10.1007/s00493-026-00205-2?format=refman&amp;flavour=references
[95]: /search?sortBy=newestFirst&amp;contributor=Francesco%20Di%20Braccio
[96]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Francesco%20Di%20Braccio
[97]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Francesco%20Di%20Braccio%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[98]: /search?sortBy=newestFirst&amp;contributor=Kyriakos%20Katsamaktsis
[99]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Kyriakos%20Katsamaktsis
[100]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Kyriakos%20Katsamaktsis%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[101]: /search?sortBy=newestFirst&amp;contributor=Jie%20Ma
[102]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Jie%20Ma
[103]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Jie%20Ma%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[104]: /search?sortBy=newestFirst&amp;contributor=Alexandru%20Malekshahian
[105]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Alexandru%20Malekshahian
[106]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Alexandru%20Malekshahian%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[107]: /search?sortBy=newestFirst&amp;contributor=Ziyuan%20Zhao
[108]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Ziyuan%20Zhao
[109]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Ziyuan%20Zhao%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[110]: mailto:f.di-braccio@lse.ac.uk
[111]: http://creativecommons.org/licenses/by/4.0/
[112]: https://s100.copyright.com/AppDispatchServlet?title=Leaf-to-leaf%20paths%20and%20cycles%20in%20degree-critical%20graphs&amp;author=Francesco%20Di%20Braccio%20et%20al&amp;contentID=10.1007%2Fs00493-026-00205-2&amp;copyright=The%20Author%28s%29&amp;publication=0209-9683&amp;publicationDate=2026-03-04&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[113]: https://crossmark.crossref.org/dialog/?doi=10.1007/s00493-026-00205-2
[114]: https://citation-needed.springer.com/v2/references/10.1007/s00493-026-00205-2?format=refman&amp;flavour=citation
