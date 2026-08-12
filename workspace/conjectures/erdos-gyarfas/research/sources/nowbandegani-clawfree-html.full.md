<!-- source: https://arxiv.org/html/1109.5398v3 | converted from HTML -->

On the Erdős-Gyárfás Conjecture in Claw-free Graphs

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1109.5398v3 [math.CO] 07 Feb 2013

# On the Erdős-Gyárfás Conjecture in Claw-free Graphs

###### Abstract

The Erdős-Gyárfás conjecture states that every graph with minimum degree at least three has a cycle whose length is a power of 2. Since this conjecture has proven to be far from reach, Hobbs asked if the Erdős-Gyárfás conjecture holds in claw-free graphs. In this paper, we obtain some results on this question, in particular for cubic claw-free graphs.

###### keywords

Erdős-Gyárfás Conjecture, Claw-Free Graphs, Cycles

\newauthor

Pouria Salehi NowbandeganiP. SalehiDepartment of Mathematics,
Shiraz University,
Shiraz 71454, Iran[pouria.salehi@gmail.com] \newauthor Hossein EsfandiariH. EsfandiariDepartment of Computer Science,
University of Maryland College Park,
College Park, MD 20742,[hossein@cs.umd.edu] \newauthor Mohammad Hassan Shirdareh HaghighiM. H. ShirdarehDepartment of Mathematics,
Shiraz University,
Shiraz 71454, Iran[shirdareh@susc.ac.ir] \newauthor Khodakhast BibakKh. BibakDepartment of Combinatorics and Optimization,
University of Waterloo,
Waterloo, Ontario, Canada N2L 3G1[kbibak@uwaterloo.ca] \classnbr C5038, C5038

## 1 Introduction

All graphs in this paper are assumed to be simple, that is, without any loops and multiple edges. Let us first recall here briefly some notation and terminology we will need in this paper. We denote by δ = δ ⁡ ( G) \delta=\delta(G) the minimum degree of the the vertices in the graph G = ( V, E) G=(V,E). A u ​ v uv -path is a path having the vertices u u and v v as its ends. The length of a path P P (or a cycle C C) is denoted by l ⁡ ( P) l(P) (resp. l ⁡ ( C) l(C)). Also, we denote the distance between the vertices u u and v v by d ⁡ ( u, v) d(u,v), that is the length of a shortest u ​ v uv -path. A graph that does not contain a particular graph H H as an induced subgraph is called H H -free. The complete bipartite graph K 1, 3 K_{1,3} is referred to as a claw; so a graph is called claw-free if it does not have K 1, 3 K_{1,3} as an induced subgraph. A triangle is a cycle of length three. A chord of a cycle C C is an edge between two vertices of C C which are not adjacent in C C. By a hole we mean a chordless cycle of length at least four. A hole of length n n is called an n n -hole.

Several questions on cycles in graphs have been posed by Erdős and his colleagues (see, e.g., [1]). In particular, in 1995 Erdős and Gyárfás [4] asked:

If G G is a graph with minimum degree at least three, does G G have a cycle whose length is a power of 2?

This is known as the Erdős-Gyárfás conjecture. In fact, Erdős and Gyárfás [4] said that “we are convinced now that this is false and no doubt there are graphs for every r r every vertex of which has degree ≥ r \geq r and which contain no cycle of length 2 k 2^{k}, but we never found a counterexample even for r = 3 r=3 ”.

There seems to be very little published on the Erdős-Gyárfás conjecture. Markström [5] (via computer searches) asserted that any cubic counterexample must have at least 30 vertices. Salehi Nowbandegani and Esfandiari [6] prove that any bipartite counterexample must have at least 32 vertices.

More generally, Erdős asked does there exist an integer sequence a 1, a 2, a 3, ⋯ a_{1},a_{2},a_{3},\cdots with zero density, and a constant c c such that every graph with average degree at least c c contains a cycle of length a i a_{i} for some i i. This question is answered affirmatively by Verstraëte [8].

Hobbs asked if the Erdős-Gyárfás conjecture holds in claw-free graphs [3]. Shauger [7] proved the conjecture for K 1, m K_{1,m} -free graphs having minimum degree at least m + 1 m+1 or maximum degree at least 2 ​ m − 1 2m-1. Also, Daniel and Shauger [3] proved it for planar claw-free graphs. In this paper, we investigate claw-free graphs with δ ≥ \delta\geq 4 and cubic claw-free graphs.

## 2 Two-power Cycle Lengths in Claw-free Graphs

Our first theorem concerns claw-free graphs with δ ≥ 3 \delta\geq 3.

###### Theorem 2.1.

Suppose that G G is a claw-free graph with δ ≥ 3 \delta\geq 3. Then G G has a cycle whose length is 2 k 2^{k}, or 3 ⋅ 2 k 3\cdot 2^{k}, for some positive integer k k.

To prove Theorem 1 we need the following lemma.

###### Lemma 2.2.

Let G G be a graph with δ ≥ 3 \delta\geq 3. If G G does not have C 4 C_{4} as a subgraph, then for some n ≥ 5 n\geq 5, it has an n n -hole.

###### Proof 2.3.

It is known that every graph with δ ≥ 2 \delta\geq 2 contains a cycle of length at least δ + 1 \delta+1 (see, e.g., [2, Exercise 2.1.5]). Thus G G has a cycle D 1 D_{1} of length n 1 ≥ 5 n_{1}\geq 5. If n = 5 n=5, D 1 D_{1} must clearly be chordless. If n > 5 n>5, and D 1 D_{1} has no chord, we are finished, so suppose D 1 D_{1} has a chord. The chord separates D 1 D_{1} into two shorter cycles, non of which have length 4, by assumption. Thus at least one of these two cycles, say D 2 D_{2}, must have length 5 ≤ n 2 < n 1 \leq n_{2}<n_{1}. Since G G is finite, we must by repeating this argument eventually find a chordless cycle D k D_{k} of length n k ≥ n_{k}\geq 5.

{dnt}

We call an edge of a graph triangulated if it is contained in a triangle. Also if such a triangle is unique, we call the edge uniquely triangulated.

Now we are ready to prove Theorem 1.

###### Proof 2.4 (Proof of Theorem 1).

If G G has a cycle of length four, the theorem holds, with k = k= 2. We may therefore assume that G G does not contain any C 4 C_{4}. Thus, by Lemma 2, for some n ≥ 5 n\geq 5, G G has an n n -hole. Let C: a 1 ​ a 2 ​ … ​ a s ​ a 1 C:\;a_{1}a_{2}\ldots a_{s}a_{1}, s ≥ 5 s\geq 5, be a smallest hole in G G. Since δ ≥ 3 \delta\geq 3 and C C is a hole, each vertex of C C has a neighbour in G − V ⁡ ( C) G-V(C). For i i, ( 1 ≤ i ≤ s 1\leq i\leq s), suppose that a i ​ b i ∈ E ⁡ ( G) a_{i}b_{i}\in E(G), where a i ∈ C a_{i}\in C and b i ∈ V ⁡ ( G) ∖ V ⁡ ( C) b_{i}\in V(G)\setminus V(C). Then either a i − 1 ​ b i ∈ E ⁡ ( G) a_{i-1}b_{i}\in E(G), or a i + 1 ​ b i ∈ E ⁡ ( G) a_{i+1}b_{i}\in E(G), because G G is claw-free. Now we show that b i ≠ b j b_{i}\not=b_{j} if | j − i | ≥ 2 |j-i|\geq 2. To get a contradiction, fix i i and let a j a_{j} be the first vertex of C C after a i a_{i} such that b i = b j = b b_{i}=b_{j}=b, | j − i | ≥ 2 |j-i|\geq 2. If j − i = 2 j-i=2, then we get the C 4: a i ​ a i + 1 ​ a i + 2 ​ b ​ a i C_{4}:\;a_{i}a_{i+1}a_{i+2}ba_{i}, which is absurd. If | j − i | > 2 |j-i|>2, then we get the hole a i + 1 ​ … ​ a j ​ b ​ a i + 1 a_{i+1}\ldots a_{j}ba_{i+1} which is certainly smaller than C C (note that we don’t reject the case that this hole may be a C 4 C_{4}).

Therefore, it follows that every other edge of C C is uniquely triangulated; we mark them. Moreover, the third vertices of the corresponding triangles are disjoint. Note also that s s is even. Consequently, we find cycles of lengths s, s + 1, …, 3 2 ​ s s,s+1,\ldots,\frac{3}{2}s by traversing C C such that as we reach a marked edge, we pass it directly or through the third vertex of its corresponding triangle. Since either there exists a 2 k 2^{k} or a 3 ⋅ 2 k − 1 3\cdot 2^{k-1} between s s and 3 2 ​ s \frac{3}{2}s, the proof is complete.

As mentioned above, Shauger [7] proved the Erdős-Gyárfás conjecture for K 1, m K_{1,m} -free graphs having minimum degree at least m + 1 m+1 or maximum degree at least 2 ​ m − 1 2m-1. Theorem 5 improves on the result of Shauger in claw-free graphs. First we state the following proposition. We omit the easy proof.

###### Proposition 1.

In a 4 -regular claw-free graph which does not contain C 4 C_{4}, every edge is uniquely triangulated.

###### Lemma 2.5.

Let G G be a 4 -regular claw-free graph which does not contain C 4 C_{4} and v v be a vertex of G G. Let C C be a smallest n-hole in G G containing v v, n ≥ 5 n\geq 5. Then for every edge x ​ y xy of C C, the third vertex z = z ⁡ ( x ​ y) z=z(xy) of the corresponding triangle of x ​ y xy is out of C C. Furthermore, if u ​ w ≠ x ​ y uw\not=xy are two edges of C C, then z ⁡ ( u ​ w) ≠ z ⁡ ( x ​ y) z(uw)\not=z(xy).

###### Proof 2.6.

First note that since C C is a hole, for every edge x ​ y xy in C C, z = z ⁡ ( x ​ y) ∉ C z=z(xy)\notin C. Let u ​ w uw and w ​ x wx be two consecutive edges in C C. If z = z ⁡ ( u ​ w) = z ⁡ ( w ​ x) z=z(uw)=z(wx), then we get the C 4: u ​ w ​ x ​ z ​ u C_{4}:\;uwxzu. Hence z ⁡ ( u ​ w) ≠ z ⁡ ( w ​ x) z(uw)\not=z(wx). Suppose that u ​ w uw and x ​ y xy are two non-consecutive edges in C C and suppose C C traverses the vertices in order u, w, x, y u,w,x,y, and then v v. Let Q Q be the y ​ v ​ u yvu segment of C C. Now if z = z ⁡ ( u ​ w) = z ⁡ ( x ​ y) z=z(uw)=z(xy), then the cycle u ​ Q ​ y ​ z ​ u uQyzu is a smaller hole containing v v; unless u u and y y are adjacent in C C (and hence v v is one of them). But in this case, we see that u ​ z ​ x ​ y ​ u uzxyu is a C 4 C_{4} in G G. This contradiction shows that z ⁡ ( u ​ w) = z ⁡ ( x ​ y) z(uw)=z(xy) for u ​ w ≠ x ​ y uw\not=xy is impossible.

###### Theorem 2.7.

Let G G be a claw-free graph with δ ≥ 4 \delta\geq 4, which does not contain C 4 C_{4}. Then every non-cut vertex of G G lies on a cycle whose length is a power of 2.

###### Proof 2.8.

Since δ ≥ 4 \delta\geq 4 and G G is claw-free, if G G has a vertex with degree at least 5, then this vertex lies on a C 4 C_{4}; so we can assume that G G is 4-regular. Suppose that v v is a non-cut vertex of G G and let w w, x x, y y, and u u be its neighbours. Hence, G − v G-v is connected. In view of G G is claw-free, we can assume that w ​ u, x ​ y ∈ E ⁡ ( G) wu,xy\in E(G). Let P 1 P_{1}, P 2 P_{2}, P 3 P_{3}, and P 4 P_{4} be the shortest w ​ y wy -path, w ​ x wx -path, x ​ u xu -path, and y ​ u yu -path in G − v G-v, respectively. Also, without loss of generality assume that l ⁡ ( P 1) = min ⁡ { l ⁡ ( P 1), l ⁡ ( P 2), l ⁡ ( P 3), l ⁡ ( P 4) } l(P_{1})=\min\{l(P_{1}),l(P_{2}),l(P_{3}),l(P_{4})\}. The path P 1 P_{1} together with the edges v ​ w vw and v ​ y vy make a cycle C C. Clearly, l ⁡ ( P 1) > 1 l(P_{1})>1, otherwise y ​ w ​ u ​ v ​ y ywuvy will be a C 4 C_{4}. Therefore, l ⁡ ( C) = s ≥ 5 l(C)=s\geq 5. Since P 1 P_{1} was the shortest path among P 1 P_{1}, P 2 P_{2}, P 3 P_{3}, and P 4 P_{4}, we see that neither x x nor u u are in P 1 P_{1} and, in fact, C C is the shortest non-triangle hole containing the vertex v v; for if v v lies on another non-triangle shorter hole, then two of its neighbours would have distance less than l ⁡ ( P 1) l(P_{1}) in G − v G-v. By Lemma 4, each edge of C C is uniquely triangulated such that the third vertex of its corresponding triangle is not on C C and this correspondence is one to one. Since l ⁡ ( C) = s l(C)=s, then G G contains cycles of lengths s, s + 1, …, 2 ​ s s,s+1,\ldots,2s. For, as in the proof of theorem 1, when we traverse the vertices of C C, we can either pass the two ends of every edge directly or through the third vertex of its corresponding triangle.

This implies that G G has a cycle containing v v whose length is 2 k 2^{k}, for some k ≥ 3 k\geq 3.

## 3 The Erdős-Gyárfás Conjecture in Cubic Claw-free Graphs

In this section, we investigate the Erdős-Gyárfás conjecture in cubic claw-free graphs. Indeed, we discuss on the cubic claw-free graphs for which the Erdős-Gyárfás conjecture possibly does not hold.

Suppose that G G is a cubic claw-free graph that does not contain C 4 C_{4}. Let v v be an arbitrary vertex of G G, and let its neighbours be x x, y y, and z z. Since G G is claw-free, so we can assume that x ​ y ∈ E ⁡ ( G) xy\in E(G). Thus, x ​ z, y ​ z ∉ E ⁡ ( G) xz,yz\notin E(G); otherwise a C 4 C_{4} appears. Let x 1 x_{1} and y 1 y_{1} be respectively the other neighbours of x x and y y. Easily we see that x 1 ≠ y 1 x_{1}\not=y_{1}. Therefore, for every vertex there exists a unique triangle containing it, such that the other neighbours of its vertices are distinct. Hence G G consists of some vertex-disjoint triangles which are connected by a perfect matching of G G. Furthermore, if two vertices from two triangles are matched, then there is no more link between these two triangles, again because we have no C 4 C_{4} in G G. This means if we look locally at the graph, we see a triangle together with three appended edges, such that these edges connect to three disjoint triangles. Now define OPEN ( ^ ​ G) \hat{(}G) to be the graph whose vertices are triangles of G G and two vertices are adjacent in G ^ \hat{G} whenever their corresponding triangles in G G are linked by an edge. The graph G ^ \hat{G} is then a simple cubic graph. We can imagine G ^ \hat{G} as a graph obtained from G G by shrinking each triangle to a vertex.

Conversely, we can start from a simple cubic graph G ^ \hat{G} and replacing each vertex v v with a triangle T T; linking the three vertices of T T to the three triangles corresponding to the three neighbours of v v. This procedure results in a cubic claw-free graph G G without C 4 C_{4}. To sum up, we have the following proposition.

###### Proposition 2.

The mapping G ↔ G ^ G\leftrightarrow\hat{G} is a one to one correspondence between simple cubic graphs and simple cubic claw-free graphs without C 4 C_{4}.

###### Corollary 3.

If G ^ \hat{G} contains a cycle of length k k, then this cycle provides cycles of lengths 2 ​ k, 2 ​ k + 1, …, 3 ​ k 2k,2k+1,\ldots,3k in G G.

###### Proof 3.1.

Consider a cycle C ^ \hat{C} of length k k in G ^ \hat{G}. The subgraph S S of G G corresponding to C ^ \hat{C} consists of a cycle of length 2 ​ k 2k such that every other edge of it is triangulated. Hence we can find cycles of lengths 2 ​ k, 2 ​ k + 1, …, 3 ​ k 2k,2k+1,\ldots,3k in S S.

Based on proposition 6 and Corollary 7, we think the following conjecture is true.

{con}

Every cubic graph contains a cycle of length l l such that 2 ​ l ≤ 2 k < 3 ​ l 2l\leq 2^{k}<3l, for some positive integer k k.

If this conjecture holds, it will lead to a proof of the Erdős-Gyárfás conjecture in cubic claw-free graphs. Also note that this conjecture can be easily deduced from the Erdős-Gyárfás conjecture. But for simplicity, we restrict ourselves to cubic graphs, and the length of the desired cycle has a very wide range.

At the end, we investigate minimal cubic claw-free graphs which possibly have no cycle with length a power of 2.

###### Theorem 3.2.

Any counterexample to the Erdős-Gyárfás conjecture in cubic claw-free graphs must have at least 114 vertices.

###### Proof 3.3.

Let G G be a claw-free cubic graph of order 3 ​ n 3n. Then G ^ {\hat{G}} (defined in proposition 6) is a cubic graph of order n n. By corollary 7, if G ^ {\hat{G}} contains a cycle of length l l, where l ∈ { 2, 3, 4, 6, 7, 8 } l\in\{2,3,4,6,7,8\}, then the Erdős-Gyárfás conjecture holds for G G. So let us assume that G ^ {\hat{G}} does not contain such cycles. Let v 0 v_{0} be a vertex of G ^ {\hat{G}}. We consider { v 0 } \{v_{0}\} as level 0, and define level i i, i ≥ 1 i\geq 1, as the set

 | L i = { v ∈ V ⁡ ( G ^): d ⁡ ( v, v 0) = i }. L_{i}=\{v\in V({\hat{G}})\;:\;\;d(v,v_{0})=i\}. |  |

Clearly, L 1 L_{1} is an independent set. It is easy to see that the subgraph induced by L 2 L_{2} has at most one edge. One can check that if the subgraph induced by L 2 L_{2} has no edge, then the subgraph induced by L 3 L_{3} has at most three edges, and if the subgraph induced by L 2 L_{2} has one edge, then the subgraph induced by L 3 L_{3} has at most one edge. No two elements of L 3 L_{3} have common neighbours in L 4 L_{4}, because otherwise, G ^ {\hat{G}} contains the cycles of lengths 2, 4, 6, or 8. An easy calculation shows that G ^ {\hat{G}} has at least 38 vertices. Consequently, any counterexample for the Erdős-Gyárfás conjecture must have at least 3 × 38 = 114 3\times 38=114 vertices.

Acknowledgments

The authors would like to thank anonymous referees for helpful mathematical and grammatical comments.

## References

- [1] J. A. Bondy, Extremal problems of Paul Erdős on circuits in graphs, In Paul Erdős and his Mathematics, II, Bolyai Soc. Math. Stud., 11, Jnos Bolyai Math. Soc., Budapest (2002), 135–156.
- [2] J. A. Bondy and U.S.R. Murty, Graph Theory, Springer-Verlag, New York (2008).
- [3] D. Daniel and S. E. Shauger, A result on the Erdős-Gyárfás conjecture in planar graphs, Congr. Numer. 153 (2001), 129–140.
- [4] P. Erdős, Some old and new problems in various branches of combinatorics, Discrete Math., 165/166 (1997), 227–231.
- [5] K. Markström, Extremal graphs for some problems on cycles in graphs, Congr. Numer., 171 (2004), 179-192.
- [6] P. Salehi Nowbandegani and H. Esfandiari, An experimental result on the Erdős-Gyárfás conjecture in bipartire graphs. 14th Workshop on graph theory (CID), September 18-23, 2011, Szklarska Poreba, Poland.
- [7] S. E. Shauger, Results on the Erdős-Gyárfás conjecture in K 1, m K_{1,m} -free graphs, Congr. Numer. 134 (1998), 61–65.
- [8] J. Verstraëte, Unavoidable cycle lengths in graphs, J. Graph Theory, 49 (2) (2005), 151–167.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
