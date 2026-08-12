<!-- source: https://arxiv.org/html/2605.22844v1 | converted from HTML -->

Every Minimal Counterexample to the Erdős–Gyárfás Conjecture is Predominantly Cubic

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2605.22844v1 [math.CO] 13 May 2026

# Every Minimal Counterexample to the Erdős–Gyárfás Conjecture is Predominantly Cubic

Avery Carr Affiliation: Independent Researcher Email: [avery.carr@ymail.com][3]

Updated: May 13, 2026

###### Abstract

A minimal counterexample to the Erdős–Gyárfás conjecture is a graph of minimum possible order and size with minimum degree at least 3 3 that contains no cycle whose length is a power of 2 2. Markström observed that any such graph must contain an independent set of vertices of degree at least 4 4 together with a nonempty set of vertices of degree exactly 3 3. As an immediate consequence, every regular minimal counterexample must be cubic. Building on this structure, two additional consequences are derived. First, every vertex of a minimal counterexample is adjacent to a vertex of degree exactly 3 3. Second, at least 4 / 7 4/7 of the vertices of any minimal counterexample must have degree exactly 3 3.

Keywords: Erdős–Gyárfás conjecture, cycles of power-of-two length, cubic graphs, minimal counterexamples, graph structure, extremal graph theory

Mathematics Subject Classification: 05C38, 05C35, 05C75

## Notation

All graphs considered in this note are finite, simple, and undirected. Let G = ( V ⁡ ( G), E ⁡ ( G)) G=(V(G),E(G)) be a graph with vertex set V ⁡ ( G) V(G) and edge set E ⁡ ( G) E(G). For a vertex v ∈ V ⁡ ( G) v\in V(G), the neighborhood of v v is

 | N ⁡ ( v) = { u ∈ V ⁡ ( G): u ​ v ∈ E ⁡ ( G) }, N(v)=\{u\in V(G):uv\in E(G)\}, |  |

and the degree of v v is

 | d ⁡ ( v) = | N ⁡ ( v) |. d(v)=|N(v)|. |  |

The minimum degree of G G is denoted by

 | δ ⁡ ( G) = min ⁡ { d ⁡ ( v): v ∈ V ⁡ ( G) }. \delta(G)=\min\{d(v):v\in V(G)\}. |  |

A graph H H is a proper subgraph of G G if H ⊊ G H\subsetneq G. A graph G G is called k k -regular if every vertex of G G has degree k k. A cubic graph is a 3 3 -regular graph.

In this note, a minimal counterexample to the Erdős–Gyárfás conjecture means a graph G G with δ ⁡ ( G) ≥ 3 \delta(G)\geq 3 that contains no cycle whose length is a power of 2 2, chosen with minimum possible order and, subject to that, minimum possible size.

## Introduction

The Erdős–Gyárfás conjecture asks whether every graph G G with minimum degree δ ⁡ ( G) ≥ 3 \delta(G)\geq 3 contains a cycle whose length is a power of two [1]. Despite its simple formulation, the conjecture remains open in general and has only been verified for restricted graph classes, including planar graphs, cubic claw-free graphs, 3 3 -connected cubic planar graphs, P 8 P_{8} -free graphs, and P 10 P_{10} -free graphs [2, 3, 4, 5, 6].

Computational work of Royle and Markström further suggests that any counterexample must be highly constrained. In particular, their investigations imply that any cubic counterexample must contain at least 30 30 vertices, while extremal constructions show that the smallest power-of-two cycle lengths can first occur at comparatively large values such as 16 16 [7].

Recent work of the author establishes the conjecture for graphs of diameter 2 2, proving that every graph G G with diam ⁡ ( G) = 2 \operatorname{diam}(G)=2 and δ ⁡ ( G) ≥ 3 \delta(G)\geq 3 contains a cycle of length 4 4 or 8 8 [8]. Motivated by the increasingly rigid structure expected of minimal counterexamples, this note studies structural restrictions on such graphs.

## Main Result

###### Lemma 0.1.

Let G G be a minimal counterexample to the Erdős–Gyárfás conjecture. Then δ ⁡ ( H) ≤ 2 \delta(H)\leq 2 for every proper subgraph H ⊊ G H\subsetneq G.

###### Proof.

Let G G be a minimal counterexample with respect to order and size, and suppose H ⊊ G H\subsetneq G is a proper subgraph with δ ⁡ ( H) ≥ 3 \delta(H)\geq 3. By minimality of G G, the graph H H cannot be a counterexample. Hence, H H contains a cycle whose length is a power of 2 2. Since H H is a subgraph of G G, the same cycle occurs in G G, contradicting that G G is a counterexample. Therefore, δ ⁡ ( H) ≤ 2 \delta(H)\leq 2 for every proper subgraph H ⊊ G H\subsetneq G. ∎

The following corollaries and theorem strengthen the structural picture first described by Markström [7]. In particular, Corollary 0.1(1) shows that the cubic vertices form a dominating set in every minimal counterexample. Corollary 0.1(2), originally observed by Markström [7], states that the vertices of degree at least 4 4 form an independent set. Theorem 0.1 then uses this structural restriction to establish an explicit lower bound on the proportion of cubic vertices.

###### Corollary 0.1.

Let G G be a minimal counterexample to the Erdős–Gyárfás conjecture.

1. 1.

Every vertex of G G is adjacent to a vertex of degree exactly 3 3.

2. 2.

The set of vertices of degree at least 4 4 forms an independent set.

###### Proof.

(1) Let v ∈ V ⁡ ( G) v\in V(G). Since G − v G-v is a proper subgraph of G G, Lemma 0.1 0.1 gives δ ⁡ ( G − v) ≤ 2 \delta(G-v)\leq 2. Since every vertex of G G has degree at least 3 3, the only way a vertex in G − v G-v can have degree at most 2 2 after deleting v v is if it was adjacent to v v and had degree exactly 3 3 in G G. Therefore, v v is adjacent to a vertex of degree exactly 3 3.

(2) Suppose u, v ∈ V ⁡ ( G) u,v\in V(G) are adjacent vertices with d ⁡ ( u) ≥ 4 d(u)\geq 4 and d ⁡ ( v) ≥ 4 d(v)\geq 4. Deleting the edge u ​ v uv decreases both degrees by exactly 1 1, so both vertices retain degree at least 3 3, while all other vertex degrees remain unchanged. Hence δ ⁡ ( G − u ​ v) ≥ 3 \delta(G-uv)\geq 3, contradicting Lemma 0.1 0.1. Therefore, no two vertices of degree at least 4 4 can be adjacent.

∎

v v w w v 1 v_{1} v 2 v_{2} v k − 1 v_{k-1} w 1 w_{1} w 2 w_{2} w k − 1 w_{k-1} ⋯ \cdots ⋯ \cdots Figure 1: An edge v ​ w vw in a k k -regular graph, where k ≥ 4 k\geq 4. Each endpoint has k − 1 ≥ 3 k-1\geq 3 other incident edges. v v w w v 1 v_{1} v 2 v_{2} v k − 1 v_{k-1} w 1 w_{1} w 2 w_{2} w k − 1 w_{k-1} ⋯ \cdots ⋯ \cdots d G − v ​ w ​ ( v) = d G − v ​ w ​ ( w) = k − 1 ≥ 3 d_{G-vw}(v)=d_{G-vw}(w)=k-1\geq 3 Figure 2: After deleting the edge v ​ w vw, the vertices v v and w w still have degree at least 3 3, while all other vertices retain their original degrees. Hence δ ⁡ ( G − v ​ w) ≥ 3 \delta(G-vw)\geq 3.

###### Corollary 0.2.

If G G is a regular minimal counterexample to the Erdős–Gyárfás conjecture, then G G is cubic.

###### Proof.

Suppose G G is k k -regular. Since δ ⁡ ( G) ≥ 3 \delta(G)\geq 3, one has k ≥ 3 k\geq 3. If k ≥ 4 k\geq 4, then every vertex has degree at least 4 4, contradicting Corollary 0.1 ​ ( 2) 0.1(2). Therefore k = 3 k=3, and hence G G is cubic. ∎

###### Theorem 0.1.

Let G G be a minimal counterexample to the Erdős–Gyárfás conjecture. Then at least 4 / 7 4/7 of the vertices of G G have degree exactly 3 3.

###### Proof.

Let

 | V 3 = { v ∈ V ⁡ ( G): d ⁡ ( v) = 3 } V_{3}=\{v\in V(G):d(v)=3\} |  |

and

 | V ≥ 4 = { v ∈ V ⁡ ( G): d ⁡ ( v) ≥ 4 }. V_{\geq 4}=\{v\in V(G):d(v)\geq 4\}. |  |

By Corollary 0.1 ​ ( 2) 0.1(2), the set V ≥ 4 V_{\geq 4} is independent. Hence every edge incident to a vertex of V ≥ 4 V_{\geq 4} joins it to a vertex of V 3 V_{3}.

Let e ⁡ ( V 3, V ≥ 4) e(V_{3},V_{\geq 4}) denote the number of edges between the two sets. Since every vertex in V ≥ 4 V_{\geq 4} has degree at least 4 4, one has

 | e ⁡ ( V 3, V ≥ 4) ≥ 4 ​ | V ≥ 4 |. e(V_{3},V_{\geq 4})\geq 4|V_{\geq 4}|. |  |

On the other hand, every vertex in V 3 V_{3} has degree exactly 3 3, so

 | e ⁡ ( V 3, V ≥ 4) ≤ 3 ​ | V 3 |. e(V_{3},V_{\geq 4})\leq 3|V_{3}|. |  |

Therefore,

 | 4 ​ | V ≥ 4 | ≤ 3 ​ | V 3 |. 4|V_{\geq 4}|\leq 3|V_{3}|. |  |

Since V ⁡ ( G) = V 3 ∪ V ≥ 4 V(G)=V_{3}\cup V_{\geq 4}, it follows that

 | | V ⁡ ( G) | = | V 3 | + | V ≥ 4 | ≤ | V 3 | + 3 4 | V 3 | = 7 4 ​ | V 3 |. |V(G)|=|V_{3}|+|V_{\geq 4}|\leq|V_{3}|+\frac{3}{4}|V_{3}|=\frac{7}{4}|V_{3}|. |  |

Hence,

 | | V 3 | ≥ 4 7 ​ | V ⁡ ( G) |. |V_{3}|\geq\frac{4}{7}|V(G)|. |  |

Thus at least 4 / 7 4/7 of the vertices of G G have degree exactly 3 3. ∎

## Acknowledgments

The author would like to thank Klas Markström for prior structural observations related to minimal counterexamples to the Erdős–Gyárfás conjecture, as well as the editors for their time and consideration.

## References

- [1] P. Erdős, *Some old and new problems in various branches of combinatorics*, Discrete Math. 165/166 (1997), 227–231.
- [2] D. Daniel and S. E. Shauger, *A result on the Erdős–Gyárfás conjecture in planar graphs*, Congressus Numerantium 153 (2001), 129–139.
- [3] P. Salehi Nowbandegani, H. Esfandiari, M. H. Shirdareh Haghighi, and K. Bibak, *On the Erdős–Gyárfás conjecture in claw-free graphs*, Discuss. Math. Graph Theory 34 (2014), 635–640.
- [4] C. C. Heckman and R. Krakovski, *Erdős–Gyárfás conjecture for cubic planar graphs*, Electronic J. Combin. 20 (2) (2013), #P7.
- [5] Y. Gao and S. Shan, *Erdős–Gyárfás conjecture for P 8 P_{8} -free graphs*, Graphs and Combinatorics 38 (2022), Article 168.
- [6] Z. Hu and C. Shen, *The Erdős–Gyárfás conjecture holds for P 10 P_{10} -free graphs*, Discrete Mathematics 347 (2024), 114175.
- [7] K. Markström, *Extremal graphs for some problems on cycles in graphs*, Congressus Numerantium 171 (2004), 177–188.
- [8] A. Carr, *Cycles of Length 4 or 8 in Graphs with Diameter 2 and Minimum Degree at Least 3*, Bull. Inst. Combin. Appl. 109 (February 2027), to appear. Available at: https://arxiv.org/abs/2508.19302.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:
