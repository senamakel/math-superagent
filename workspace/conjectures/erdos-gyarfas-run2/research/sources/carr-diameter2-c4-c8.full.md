<!-- source: https://arxiv.org/html/2508.19302v4 | converted from HTML -->

Cycles of Length 4 or 8 in Graphs with Diameter 2 and Minimum Degree at Least 3

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2508.19302v4 [math.CO] 30 Jan 2026

# Cycles of Length 4 or 8 in Graphs with Diameter 2 and Minimum Degree at Least 3

Avery Carr Affiliation: Independent Researcher Email: [avery.carr@ymail.com][3]

Updated: January 29, 2026

###### Abstract

In this short note it is shown that every graph of diameter 2 2 and minimum degree at least 3 3 contains a cycle of length 4 4 or 8 8. This result contributes to the study of the Erdős–Gyárfás Conjecture [1] by confirming it for the class of diameter- 2 2 graphs.

## Notation and Preliminaries

All graphs considered in this note are finite, simple, and undirected.

Let G = ( V ⁡ ( G), E ⁡ ( G)) G=(V(G),E(G)) be a graph where V ⁡ ( G) V(G) and E ⁡ ( G) E(G) denote the set of vertices and edges in G respectively. For a vertex v ∈ V ⁡ ( G) v\in V(G), the *neighborhood*of v v is

 | N ⁡ ( v) = { u ∈ V ⁡ ( G): u ​ v ∈ E ⁡ ( G) }, N(v)=\{u\in V(G):uv\in E(G)\}, |  |

and the *degree*of v v is d ⁡ ( v) = | N ⁡ ( v) | d(v)=|N(v)|. The minimum degree of G G is denoted by

 | δ ⁡ ( G) = min ⁡ { d ⁡ ( v): v ∈ V ⁡ ( G) }. \delta(G)=\min\{d(v):v\in V(G)\}. |  |

For vertices u, v ∈ V ⁡ ( G) u,v\in V(G), the *distance*d ⁡ ( u, v) d(u,v) is the length of a shortest path joining u u and v v in G G. The *diameter*of G G is

 | diam ( G) = max { d ( u, v): u, v ∈ V ( G) }. \operatorname{diam}(G)=\max\{d(u,v):u,v\in V(G)\}. |  |

A *path*of length k k is a sequence of distinct vertices

 | v 0, v 1, …, v k v_{0},v_{1},\dots,v_{k} |  |

such that v i ​ v i + 1 ∈ E ⁡ ( G) v_{i}v_{i+1}\in E(G) for all 0 ≤ i < k 0\leq i<k. A *cycle*of length k k is a sequence

 | v 0, v 1, …, v k − 1, v 0 v_{0},v_{1},\dots,v_{k-1},v_{0} |  |

in which v 0, …, v k − 1 v_{0},\dots,v_{k-1} are distinct and v i ​ v i + 1 ∈ E ⁡ ( G) v_{i}v_{i+1}\in E(G) for all indices taken modulo k k.

A *k k -cycle*is a cycle of length k k. A cycle is called *simple*if it contains no repeated vertices except for the initial and terminal vertex.

Given a cycle C C, an edge joining two nonconsecutive vertices of C C is called a *chord*of C C.

Throughout the paper, vertex labels v 1, v 2, … v_{1},v_{2},\dots are introduced as needed and are proved to be distinct. When a sequence is written as

 | v 1 − v 2 − ⋯ − v k, v_{1}-v_{2}-\cdots-v_{k}, |  |

it means that v i ​ v i + 1 ∈ E ⁡ ( G) v_{i}v_{i+1}\in E(G) for all 1 ≤ i < k 1\leq i<k.

All set-theoretic notation is used in its standard meaning.

## Introduction

A well-known open problem of Erdős and Gyárfás asks for unavoidable cycle lengths in graphs with minimum degree at least three. In particular, they conjectured that every graph G G with δ ⁡ ( G) ≥ 3 \delta(G)\geq 3 contains a simple cycle whose length is a power of two. This is now commonly referred to as the *Erdős–Gyárfás Conjecture*. Folklore has the conjecture first appearing at a conference in (1995) (later in literature in (1997) [1]), and is listed in several open-problem compilations (e.g. West [2] and Erdős problems forums such as [3]).

Despite its simple statement, the conjecture remains open in full generality and has been verified only for restricted classes of graphs. Early progress includes results for planar and cubic claw-free graphs [4, 5]. More recently, Heckman and Krakovski proved the conjecture for 3 3 -connected cubic planar graphs [6], and a number of papers have established the conjecture for other hereditary or structured graph classes such as P 8 P_{8} -free graphs [7].

Computational searches have also shaped the current understanding. In particular, exhaustive and heuristic searches (notably by Royle and Markström) indicate that any counterexample must be relatively large, and Markström produced extremal examples illustrating how power-of-two cycles can be forced to occur only at larger lengths (e.g. 16 16) in certain cubic graphs [8]. These computations suggest that minimal counterexamples, if they exist, are highly constrained.

In this note the Erdős–Gyárfás conjecture is verified for graphs of diameter 2 2. The main result shows that every graph G G with diam ⁡ ( G) = 2 \operatorname{diam}(G)=2 and δ ⁡ ( G) ≥ 3 \delta(G)\geq 3 contains a cycle of length 4 4 or 8 8 (see Theorem 1.1.). Thus, within the diameter– 2 2 regime, the conjecture holds in its strongest possible form, guaranteeing one of the two smallest nontrivial powers of two. From the perspective of the broader conjecture, diameter 2 2 graphs form a natural and widely studied class: the global constraint diam ⁡ ( G) = 2 \operatorname{diam}(G)=2 forces any two nonadjacent vertices to have a common neighbor, creating a dense web of short connections. The proof exploits this interaction between a local degree lower bound and the global diameter constraint to force short power-of-two cycles.

## Main Result

Theorem 1.1.: Let G G be a graph with diameter 2 2 and minimum degree at least 3 3. Then G G contains a cycle of length 4 4 or 8 8.

## Proof

Assume G G has diameter 2 2, minimum degree at least 3 3, and no 4 4 -cycle. For a vertex v v in G G, let N ⁡ ( v) N(v) denote its neighborhood; the set of vertices adjacent to v v.

Let v 1 ​ v 2 ∈ E ⁡ ( G) v_{1}v_{2}\in E(G). By the degree condition, v 1 v_{1} has two neighbors other than v 2 v_{2}, call them v 3, v 4 v_{3},v_{4}; similarly, v 2 v_{2} has two neighbors v 5, v 6 v_{5},v_{6}. Denote this subgraph of G G as G ′ G^{\prime} (see Figure 1).

v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} Figure 1: G ′ G^{\prime} - Initial edge with neighbors satisfying the degree constraint.

If v 3 = v 5 v_{3}=v_{5} while v 4 = v 6 v_{4}=v_{6}, or v 3 = v 6 v_{3}=v_{6} while v 4 = v 5 v_{4}=v_{5}, then a cycle of length 4 4 forms immediately, namely

 | v 1 − v 3 − v 2 − v 4 − v 1 or v 1 − v 4 − v 2 − v 3 − v 1. v_{1}-v_{3}-v_{2}-v_{4}-v_{1}\quad\text{or}\quad v_{1}-v_{4}-v_{2}-v_{3}-v_{1}. |  |

Both cases contradict the assumption that G G contains no 4 4 -cycle.

Thus, without loss of generality, it suffices to prove the theorem by considering separately the cases v 3 = v 5 v_{3}=v_{5} and v 3 ≠ v 5 v_{3}\neq v_{5}.

### Case 1: v 3 = v 5 v_{3}=v_{5}

Assume v 3 = v 5 v_{3}=v_{5}. Let v 4 v_{4} be the neighbor of v 1 v_{1} distinct from v 2, v 3 v_{2},v_{3}, and let v 6 v_{6} be the neighbor of v 2 v_{2} distinct from v 1, v 3 v_{1},v_{3}. Set V ⁡ ( G ′) = { v 1, v 2, v 3, v 4, v 6 } V(G^{\prime})=\{v_{1},v_{2},v_{3},v_{4},v_{6}\}.

Claim 1.1. v 4 ​ v 6 ∉ E ⁡ ( G) v_{4}v_{6}\notin E(G).

*Proof.*If v 4 ​ v 6 ∈ E ⁡ ( G) v_{4}v_{6}\in E(G), then

 | v 4 − v 1 − v 2 − v 6 − v 4 v_{4}-v_{1}-v_{2}-v_{6}-v_{4} |  |

is a 4 4 -cycle, contradicting the assumption that G G contains no 4 4 -cycle. ⋄ \diamond

Since v 4 v_{4} and v 6 v_{6} are nonadjacent and diam ⁡ ( G) = 2 \operatorname{diam}(G)=2, we have

 | N ⁡ ( v 4) ∩ N ⁡ ( v 6) ≠ ∅. N(v_{4})\cap N(v_{6})\neq\varnothing. |  |

Choose

 | v 7 ∈ N ⁡ ( v 4) ∩ N ⁡ ( v 6). v_{7}\in N(v_{4})\cap N(v_{6}). |  |

Claim 1.2. v 7 ∉ { v 1, v 2, v 3 } v_{7}\notin\{v_{1},v_{2},v_{3}\}.

*Proof.*If v 7 = x v_{7}=x such that x ∈ { v 1, v 2, v 3 } x\in\{v_{1},v_{2},v_{3}\}, then at least one of the following 4 4 –cycles would form:

 | v 1 − v 3 − v 2 − v 6 − v 1, \displaystyle v_{1}-v_{3}-v_{2}-v_{6}-v_{1}, |  |

 | v 2 − v 3 − v 1 − v 6 − v 2, \displaystyle v_{2}-v_{3}-v_{1}-v_{6}-v_{2}, |  |

 | v 4 − v 3 − v 2 − v 1 − v 4. \displaystyle v_{4}-v_{3}-v_{2}-v_{1}-v_{4}. |  |

⋄ \diamond

Thus, assume v 7 ∉ V ⁡ ( G ′) v_{7}\notin V(G^{\prime}). Then the closed walk

 | v 7 − v 4 − v 1 − v 3 − v 2 − v 6 − v 7 v_{7}-v_{4}-v_{1}-v_{3}-v_{2}-v_{6}-v_{7} |  |

forms a 6 6 -cycle with a chord v 1 ​ v 2 v_{1}v_{2} (see Figure 2).

v 7 v_{7} v 4 v_{4} v 1 v_{1} v 2 v_{2} v 6 v_{6} v 3 v_{3} Figure 2: 6 6 -Cycle with a v 1 ​ v 2 v_{1}v_{2} Chord

Notice v 3 v_{3} and v 7 v_{7} are not adjacent, and if the edge v 3 ​ v 7 ∈ E ⁡ ( G) v_{3}v_{7}\in E(G), then a 4 4 -cycle forms by

 | v 7 − v 3 − v 1 − v 4 − v 7, v_{7}-v_{3}-v_{1}-v_{4}-v_{7}, |  |

a contradiction. Also, the diameter– 2 2 condition implies

 | N ⁡ ( v 3) ∩ N ⁡ ( v 7) ≠ ∅. N(v_{3})\cap N(v_{7})\neq\varnothing. |  |

Let v 8 ∈ N ⁡ ( v 3) ∩ N ⁡ ( v 7) v_{8}\in N(v_{3})\cap N(v_{7}).

Claim 1.3 v 8 ∉ V ⁡ ( G ′) v_{8}\notin V(G^{\prime}).
*Proof.*

Indeed, if v 8 ∈ V ⁡ ( G ′) v_{8}\in V(G^{\prime}), then v 8 ∈ { v 1, v 2, v 4, v 6 } v_{8}\in\{v_{1},v_{2},v_{4},v_{6}\} and a 4 4 –cycle arises in each case:

 | v 8 = v 1 \displaystyle v_{8}=v_{1} | ⟹ v 1 − v 2 − v 6 − v 7 − v 1, \displaystyle\implies v_{1}-v_{2}-v_{6}-v_{7}-v_{1}, |  |

 | v 8 = v 2 \displaystyle v_{8}=v_{2} | ⟹ v 2 − v 1 − v 4 − v 7 − v 2, \displaystyle\implies v_{2}-v_{1}-v_{4}-v_{7}-v_{2}, |  |

 | v 8 = v 4 \displaystyle v_{8}=v_{4} | ⟹ v 4 − v 3 − v 2 − v 1 − v 4, \displaystyle\implies v_{4}-v_{3}-v_{2}-v_{1}-v_{4}, |  |

 | v 8 = v 6 \displaystyle v_{8}=v_{6} | ⟹ v 6 − v 3 − v 1 − v 2 − v 6. \displaystyle\implies v_{6}-v_{3}-v_{1}-v_{2}-v_{6}. |  |

This contradicts the assumption that G G contains no 4 4 –cycle. Hence v 8 ∉ V ⁡ ( G ′) v_{8}\notin V(G^{\prime})
(see Figure 3). ⋄ \diamond

v 7 v_{7} v 4 v_{4} v 1 v_{1} v 2 v_{2} v 6 v_{6} v 3 v_{3} v 8 v_{8} Figure 3: v 8 ∈ N ⁡ ( v 7) ∩ N ⁡ ( v 3) v_{8}\in N(v_{7})\cap N(v_{3})

Since δ ⁡ ( G) ≥ 3 \delta(G)\geq 3, the vertex v 8 v_{8} has a neighbor v 9 ∉ { v 3, v 7 } v_{9}\notin\{v_{3},v_{7}\}.

Claim 1.4. v 9 ∉ V ⁡ ( G ′) v_{9}\notin V(G^{\prime}).
*Proof.*Otherwise v 9 ∈ { v 1, v 2, v 4, v 6 } v_{9}\in\{v_{1},v_{2},v_{4},v_{6}\}, and each possibility yields a 4 4 –cycle:

 | v 9 = v 1 \displaystyle v_{9}=v_{1} | ⟹ v 1 − v 4 − v 7 − v 8 − v 1, \displaystyle\implies v_{1}-v_{4}-v_{7}-v_{8}-v_{1}, |  |

 | v 9 = v 2 \displaystyle v_{9}=v_{2} | ⟹ v 2 − v 1 − v 3 − v 8 − v 2, \displaystyle\implies v_{2}-v_{1}-v_{3}-v_{8}-v_{2}, |  |

 | v 9 = v 4 \displaystyle v_{9}=v_{4} | ⟹ v 4 − v 8 − v 3 − v 1 − v 4, \displaystyle\implies v_{4}-v_{8}-v_{3}-v_{1}-v_{4}, |  |

 | v 9 = v 6 \displaystyle v_{9}=v_{6} | ⟹ v 6 − v 2 − v 3 − v 8 − v 6. \displaystyle\implies v_{6}-v_{2}-v_{3}-v_{8}-v_{6}. |  |

⋄ \diamond

Thus v 9 ∉ V ⁡ ( G ′) v_{9}\notin V(G^{\prime}) (see Figure 4).

v 7 v_{7} v 4 v_{4} v 1 v_{1} v 2 v_{2} v 6 v_{6} v 3 v_{3} v 8 v_{8} v 9 v_{9} Figure 4: v 8 ​ v 9 ∈ E ⁡ ( G) v_{8}v_{9}\in E(G)

Claim 1.5. If v 9 v_{9} is adjacent to x ∈ { v 1, v 2, v 4, v 6 } x\in\{v_{1},v_{2},v_{4},v_{6}\}, then there exists a 4 4 –cycle.
*Proof.*

Assume v 9 v_{9} is adjacent to x ∈ { v 1, v 2, v 4, v 6 } x\in\{v_{1},v_{2},v_{4},v_{6}\}. Thus, a 4 4 –cycle is formed in each of the following cases:

 | x = v 1 \displaystyle x=v_{1} | ⟹ v 1 − v 3 − v 8 − v 9 − v 1, \displaystyle\implies v_{1}-v_{3}-v_{8}-v_{9}-v_{1}, |  |

 | x = v 2 \displaystyle x=v_{2} | ⟹ v 2 − v 3 − v 8 − v 9 − v 2, \displaystyle\implies v_{2}-v_{3}-v_{8}-v_{9}-v_{2}, |  |

 | x = v 4 \displaystyle x=v_{4} | ⟹ v 4 − v 7 − v 8 − v 9 − v 4, \displaystyle\implies v_{4}-v_{7}-v_{8}-v_{9}-v_{4}, |  |

 | x = v 6 \displaystyle x=v_{6} | ⟹ v 6 − v 7 − v 8 − v 9 − v 6. \displaystyle\implies v_{6}-v_{7}-v_{8}-v_{9}-v_{6}. |  |

⋄ \diamond

Also, since v 9 v_{9} is nonadjacent with both v 4 v_{4} and v 2 v_{2}, by diam ⁡ ( G) = 2 \operatorname{diam}(G)=2 both N ⁡ ( v 9) ∩ N ⁡ ( v 4) N(v_{9})\cap N(v_{4}) and N ⁡ ( v 9) ∩ N ⁡ ( v 2) N(v_{9})\cap N(v_{2}) are non-empty.

Claim 1.6. There is a vertex v 10 ∈ ( N ⁡ ( v 9) ∩ N ⁡ ( v 4)) ∪ ( N ⁡ ( v 9) ∩ N ⁡ ( v 2)) v_{10}\in(N(v_{9})\cap N(v_{4}))\cup(N(v_{9})\cap N(v_{2})) such that
v 10 ∉ ( { v 7, v 8 } ∪ V ⁡ ( G ′)) v_{10}\notin(\{v_{7},v_{8}\}\cup V(G^{\prime})).
*Proof.*If v 8 ∈ ( N ⁡ ( v 9) ∩ N ⁡ ( v 4)) ∪ ( N ⁡ ( v 9) ∩ N ⁡ ( v 2)) v_{8}\in(N(v_{9})\cap N(v_{4}))\cup(N(v_{9})\cap N(v_{2})) then v 8 v_{8} is adjacent to one of v 2 v_{2} or v 4 v_{4} and, by Claim 1.4, a 4 4 –cycle is present. Thus, v 10 ≠ v 8 v_{10}\neq v_{8}. Now, suppose v 10 ∈ ( N ⁡ ( v 9) ∩ N ⁡ ( v 4)) ∪ ( N ⁡ ( v 9) ∩ N ⁡ ( v 2)) v_{10}\in(N(v_{9})\cap N(v_{4}))\cup(N(v_{9})\cap N(v_{2})) such that ( N ⁡ ( v 9) ∩ N ⁡ ( v 4)) ∪ ( N ⁡ ( v 9) ∩ N ⁡ ( v 2)) ⊆ ( { v 7 } ∪ V ⁡ ( G ′)) (N(v_{9})\cap N(v_{4}))\cup(N(v_{9})\cap N(v_{2}))\subseteq(\{v_{7}\}\cup V(G^{\prime})). Then, by the diameter 2 condition and Claim 1.5, v 9 v_{9} is adjacent to both v 3 v_{3} and v 7 v_{7} (else v 9 v_{9} would be adjacent to another pair of vertices in { v 7 } ∪ V ⁡ ( G ′) \{v_{7}\}\cup V(G^{\prime}) violating Claim 1.5). However, this forms a 4 4 –cycle by v 3 − v 8 − v 7 − v 9 − v 3 v_{3}-v_{8}-v_{7}-v_{9}-v_{3}, providing a contradiction on the claim of no 4 4 –cycles. ⋄ \diamond

Thus, by Claim 1.6, there is a distinct vertex v 10 v_{10} that is in at least one of N ⁡ ( v 9) ∩ N ⁡ ( v 2) N(v_{9})\cap N(v_{2}) or N ⁡ ( v 9) ∩ N ⁡ ( v 4) N(v_{9})\cap N(v_{4}) such that v 10 ∉ ( { v 7, v 8 } ∪ V ⁡ ( G ′)) v_{10}\notin(\{v_{7},v_{8}\}\cup V(G^{\prime})). In either case, an 8 8 –cycle is formed (see Figure 5 and 6) by:

 | v 10 ∈ N ⁡ ( v 9) ∩ N ⁡ ( v 2) \displaystyle v_{10}\in N(v_{9})\cap N(v_{2}) | ⟹ v 10 − v 2 − v 3 − v 1 − v 4 − v 7 − v 8 − v 9 − v 10, \displaystyle\implies v_{10}-v_{2}-v_{3}-v_{1}-v_{4}-v_{7}-v_{8}-v_{9}-v_{10}, |  |

 | v 10 ∈ N ⁡ ( v 9) ∩ N ⁡ ( v 4) \displaystyle v_{10}\in N(v_{9})\cap N(v_{4}) | ⟹ v 10 − v 4 − v 1 − v 2 − v 6 − v 7 − v 8 − v 9 − v 10. \displaystyle\implies v_{10}-v_{4}-v_{1}-v_{2}-v_{6}-v_{7}-v_{8}-v_{9}-v_{10}. |  |

v 7 v_{7} v 4 v_{4} v 1 v_{1} v 2 v_{2} v 6 v_{6} v 3 v_{3} v 8 v_{8} v 9 v_{9} v 10 v_{10} Figure 5: v 10 ∈ N ⁡ ( v 2) ∩ N ⁡ ( v 9) v_{10}\in N(v_{2})\cap N(v_{9}) forming an 8 8 -Cycle v 7 v_{7} v 4 v_{4} v 1 v_{1} v 2 v_{2} v 6 v_{6} v 3 v_{3} v 8 v_{8} v 9 v_{9} v 10 v_{10} Figure 6: v 10 ∈ N ⁡ ( v 4) ∩ N ⁡ ( v 9) v_{10}\in N(v_{4})\cap N(v_{9}) forming an 8 8 -Cycle

### Case 2: v 3 ≠ v 5 v_{3}\neq v_{5}

Assume v 3 ≠ v 5 v_{3}\neq v_{5}.

Claim 2.1. If x ​ y ∈ E ⁡ ( G) xy\in E(G) for some x ∈ { v 3, v 4 } x\in\{v_{3},v_{4}\} and y ∈ { v 5, v 6 } y\in\{v_{5},v_{6}\}, then G G contains a 4 4 -cycle.

*Proof.*Since v 1 ​ x ∈ E ⁡ ( G) v_{1}x\in E(G) and v 2 ​ y ∈ E ⁡ ( G) v_{2}y\in E(G), the cycle v 1 − x − y − v 2 − v 1 v_{1}-x-y-v_{2}-v_{1} has length 4 4. ⋄ \diamond

Hence we may assume that no edge joins the sets { v 3, v 4 } \{v_{3},v_{4}\} and { v 5, v 6 } \{v_{5},v_{6}\}.

Claim 2.2. There exist a ∈ { v 3, v 4 } a\in\{v_{3},v_{4}\} and b ∈ { v 5, v 6 } b\in\{v_{5},v_{6}\} such that

 | N ⁡ ( a) ∩ N ⁡ ( b) ⊈ { v 1, v 2 }. N(a)\cap N(b)\not\subseteq\{v_{1},v_{2}\}. |  |

*Proof.*Because diam ⁡ ( G) = 2 \operatorname{diam}(G)=2 and a ​ b ∉ E ⁡ ( G) ab\notin E(G) (by Claim 2.1), every such pair ( a, b) (a,b) has a common neighbor, so N ⁡ ( a) ∩ N ⁡ ( b) ≠ ∅ N(a)\cap N(b)\neq\varnothing.

Suppose for contradiction that for every a ∈ { v 3, v 4 } a\in\{v_{3},v_{4}\} and b ∈ { v 5, v 6 } b\in\{v_{5},v_{6}\} we have

 | N ⁡ ( a) ∩ N ⁡ ( b) ⊆ { v 1, v 2 }. N(a)\cap N(b)\subseteq\{v_{1},v_{2}\}. |  |

Since v 1 v_{1} is adjacent to both v 3 v_{3} and v 4 v_{4}, the vertex v 1 v_{1} is a common neighbor of ( a, b) (a,b) exactly when v 1 ​ b ∈ E ⁡ ( G) v_{1}b\in E(G). Similarly, since v 2 v_{2} is adjacent to both v 5 v_{5} and v 6 v_{6}, the vertex v 2 v_{2} is a common neighbor of ( a, b) (a,b) exactly when v 2 ​ a ∈ E ⁡ ( G) v_{2}a\in E(G). Thus, for each pair ( a, b) (a,b), at least one of the edges v 1 ​ b v_{1}b or v 2 ​ a v_{2}a must exist.

If v 1 v_{1} is adjacent to both v 5 v_{5} and v 6 v_{6}, then v 1 − v 5 − v 2 − v 6 − v 1 v_{1}-v_{5}-v_{2}-v_{6}-v_{1} is a 4 4 -cycle. If v 2 v_{2} is adjacent to both v 3 v_{3} and v 4 v_{4}, then v 1 − v 3 − v 2 − v 4 − v 1 v_{1}-v_{3}-v_{2}-v_{4}-v_{1} is a 4 4 -cycle. Hence v 1 v_{1} is adjacent to at most one of { v 5, v 6 } \{v_{5},v_{6}\} and v 2 v_{2} is adjacent to at most one of { v 3, v 4 } \{v_{3},v_{4}\}. But then there is some pair ( a, b) (a,b) with v 1 ​ b ∉ E ⁡ ( G) v_{1}b\notin E(G) and v 2 ​ a ∉ E ⁡ ( G) v_{2}a\notin E(G), contradicting the requirement that each pair ( a, b) (a,b) has a common neighbor in { v 1, v 2 } \{v_{1},v_{2}\}. Therefore the claim holds. ⋄ \diamond

By Claim 2.2, choose a ∈ { v 3, v 4 } a\in\{v_{3},v_{4}\} and b ∈ { v 5, v 6 } b\in\{v_{5},v_{6}\} and a vertex

 | v 7 ∈ N ⁡ ( a) ∩ N ⁡ ( b) ∖ { v 1, v 2 }. v_{7}\in N(a)\cap N(b)\setminus\{v_{1},v_{2}\}. |  |

If v 7 ∈ { v 3, v 4, v 5, v 6 } v_{7}\in\{v_{3},v_{4},v_{5},v_{6}\}, then a 4 4 -cycle occurs:

 | v 7 = v 3 \displaystyle v_{7}=v_{3} | ⇒ v 1 − v 3 − b − v 2 − v 1, \displaystyle\Rightarrow v_{1}-v_{3}-b-v_{2}-v_{1}, |  |

 | v 7 = v 4 \displaystyle v_{7}=v_{4} | ⇒ v 1 − v 4 − b − v 2 − v 1, \displaystyle\Rightarrow v_{1}-v_{4}-b-v_{2}-v_{1}, |  |

 | v 7 = v 5 \displaystyle v_{7}=v_{5} | ⇒ v 1 − a − v 5 − v 2 − v 1, \displaystyle\Rightarrow v_{1}-a-v_{5}-v_{2}-v_{1}, |  |

 | v 7 = v 6 \displaystyle v_{7}=v_{6} | ⇒ v 1 − a − v 6 − v 2 − v 1. \displaystyle\Rightarrow v_{1}-a-v_{6}-v_{2}-v_{1}. |  |

Thus,

 | v 7 ∉ V ⁡ ( G ′) = { v 1, v 2, v 3, v 4, v 5, v 6 }. v_{7}\notin V(G^{\prime})=\{v_{1},v_{2},v_{3},v_{4},v_{5},v_{6}\}. |  |

Without loss of generality, let a = v 3 a=v_{3} and b = v 5 b=v_{5}; hence

 | v 7 ∈ N ⁡ ( v 3) ∩ N ⁡ ( v 5), v 7 ∉ V ⁡ ( G ′) v_{7}\in N(v_{3})\cap N(v_{5}),\quad v_{7}\notin V(G^{\prime}) |  |

(see Figure 7).

v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} Figure 7: A new common neighbor v 7 ∈ N ⁡ ( v 3) ∩ N ⁡ ( v 5) v_{7}\in N(v_{3})\cap N(v_{5}) with v 7 ∉ V ⁡ ( G ′) v_{7}\notin V(G^{\prime}).

Claim 2.3. v 7 ​ v 4 ∉ E ⁡ ( G) v_{7}v_{4}\notin E(G).

*Proof.*If v 7 ​ v 4 ∈ E ⁡ ( G) v_{7}v_{4}\in E(G), then v 4 − v 7 − v 3 − v 1 − v 4 v_{4}-v_{7}-v_{3}-v_{1}-v_{4} is a 4 4 -cycle. ⋄ \diamond

Consider the nonadjacent pair ( v 4, v 6) (v_{4},v_{6}). If v 4 ​ v 6 ∈ E ⁡ ( G) v_{4}v_{6}\in E(G), then Claim 2.1 is violated and there is a 4 4 -cycle. Hence v 4 ​ v 6 ∉ E ⁡ ( G) v_{4}v_{6}\notin E(G) and

 | N ⁡ ( v 4) ∩ N ⁡ ( v 6) ≠ ∅. N(v_{4})\cap N(v_{6})\neq\varnothing. |  |

Choose

 | v 8 ∈ N ⁡ ( v 4) ∩ N ⁡ ( v 6). v_{8}\in N(v_{4})\cap N(v_{6}). |  |

Claim 2.4. v 8 ∉ { v 3, v 5, v 7 } v_{8}\notin\{v_{3},v_{5},v_{7}\}.

*Proof.*If v 8 = v 3 v_{8}=v_{3} or v 8 = v 5 v_{8}=v_{5}, then Claim 2.1 is violated. If v 8 = v 7 v_{8}=v_{7}, then Claim 2.3 is violated. ⋄ \diamond

Subcase 2A: v 8 = v 1 v_{8}=v_{1}. Then v 1 ​ v 6 ∈ E ⁡ ( G) v_{1}v_{6}\in E(G). Since diam ⁡ ( G) = 2 \operatorname{diam}(G)=2 and v 6 v_{6} and v 7 v_{7} are nonadjacent, we have

 | N ⁡ ( v 6) ∩ N ⁡ ( v 7) ≠ ∅. N(v_{6})\cap N(v_{7})\neq\varnothing. |  |

Choose x ∈ N ⁡ ( v 6) ∩ N ⁡ ( v 7) x\in N(v_{6})\cap N(v_{7}). If x ∈ V ⁡ ( G ′) ∖ { v 6 } x\in V(G^{\prime})\setminus\{v_{6}\} then a 4 4 –cycle appears by at least one of the following:

 | x = v 1 \displaystyle x=v_{1} | ⇒ v 1 − v 7 − v 5 − v 2 − v 1, \displaystyle\Rightarrow v_{1}-v_{7}-v_{5}-v_{2}-v_{1}, |  |

 | x = v 2 \displaystyle x=v_{2} | ⇒ v 2 − v 1 − v 3 − v 7 − v 2, \displaystyle\Rightarrow v_{2}-v_{1}-v_{3}-v_{7}-v_{2}, |  |

 | x = v 3 \displaystyle x=v_{3} | ⇒ v 3 − v 1 − v 2 − v 6 − v 3, \displaystyle\Rightarrow v_{3}-v_{1}-v_{2}-v_{6}-v_{3}, |  |

 | x = v 4 \displaystyle x=v_{4} | ⇒ v 4 − v 1 − v 2 − v 6 − v 4, \displaystyle\Rightarrow v_{4}-v_{1}-v_{2}-v_{6}-v_{4}, |  |

 | x = v 5 \displaystyle x=v_{5} | ⇒ v 5 − v 2 − v 1 − v 6 − v 5. \displaystyle\Rightarrow v_{5}-v_{2}-v_{1}-v_{6}-v_{5}. |  |

Thus, x ∉ V ⁡ ( G ′) ∖ { v 6 } x\notin V(G^{\prime})\setminus\{v_{6}\} (see Figure 8).

v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} x x Figure 8: Common neighbor x ∈ N ⁡ ( v 6) ∩ N ⁡ ( v 7) x\in N(v_{6})\cap N(v_{7}) with x ∉ V ⁡ ( G ′) ∖ { v 6 } x\notin V(G^{\prime})\setminus\{v_{6}\}.

Since v 4 v_{4} and v 5 v_{5} are nonadjacent (by Claim 2.1),

 | N ⁡ ( v 4) ∩ N ⁡ ( v 5) ≠ ∅, N(v_{4})\cap N(v_{5})\neq\varnothing, |  |

by the diam ⁡ ( G) = 2 \operatorname{diam}(G)=2 condition.
Suppose y ∈ N ⁡ ( v 4) ∩ N ⁡ ( v 5) y\in N(v_{4})\cap N(v_{5}). By Claim 2.1, y ∉ { v 3, v 6 } y\notin\{v_{3},v_{6}\}.
Suppose y ∈ { v 1, v 2, v 7, x } y\in\{v_{1},v_{2},v_{7},x\}.

Thus, a 4 4 –cycle occurs by the following:

 | y = v 1 \displaystyle y=v_{1} | ⇒ v 1 − v 6 − v 2 − v 5 − v 1, \displaystyle\Rightarrow v_{1}-v_{6}-v_{2}-v_{5}-v_{1}, |  |

 | y = v 2 \displaystyle y=v_{2} | ⇒ v 2 − v 6 − v 1 − v 4 − v 2, \displaystyle\Rightarrow v_{2}-v_{6}-v_{1}-v_{4}-v_{2}, |  |

 | y = v 7 \displaystyle y=v_{7} | ⇒ v 7 − v 3 − v 1 − v 4 − v 7, \displaystyle\Rightarrow v_{7}-v_{3}-v_{1}-v_{4}-v_{7}, |  |

 | y = x \displaystyle y=x | ⇒ x − v 5 − v 2 − v 6 − x. \displaystyle\Rightarrow x-v_{5}-v_{2}-v_{6}-x. |  |

Therefore, y ∈ N ⁡ ( v 4) ∩ N ⁡ ( v 5) y\in N(v_{4})\cap N(v_{5}) such that y ∉ { v 1, v 2, v 7, x } y\notin\{v_{1},v_{2},v_{7},x\} (see Figure 9) .

v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} x x y y Figure 9: Common neighbor y ∈ N ⁡ ( v 4) ∩ N ⁡ ( v 5) y\in N(v_{4})\cap N(v_{5}) with y ∉ { v 1, v 2, v 5 } y\notin\{v_{1},v_{2},v_{5}\}.

But

 | x − v 7 − v 5 − y − v 4 − v 1 − v 2 − v 6 − x x-v_{7}-v_{5}-y-v_{4}-v_{1}-v_{2}-v_{6}-x |  |

forms a cycle of length 8 8. ⋄ \diamond

Subcase 2B: v 8 = v 2 v_{8}=v_{2}. This case is handled analogously to v 8 = v 1 v_{8}=v_{1}; using diameter and degree constraints, start with v 2 ​ v 4 ∈ E ⁡ ( G) v_{2}v_{4}\in E(G), force a x ∈ N ⁡ ( v 4) ∩ N ⁡ ( v 7) x\in N(v_{4})\cap N(v_{7}) and y ∈ N ⁡ ( v 3) ∩ N ⁡ ( v 6) y\in N(v_{3})\cap N(v_{6}), obtaining an 8 8 –cycle.

Subcase 2C: v 8 ∉ { v 1, v 2 } v_{8}\notin\{v_{1},v_{2}\}. Then the edges

 | v 7 ​ v 3, v 3 ​ v 1, v 1 ​ v 4, v 4 ​ v 8, v 8 ​ v 6, v 6 ​ v 2, v 2 ​ v 5, v 5 ​ v 7 v_{7}v_{3},\ v_{3}v_{1},\ v_{1}v_{4},\ v_{4}v_{8},\ v_{8}v_{6},\ v_{6}v_{2},\ v_{2}v_{5},\ v_{5}v_{7} |  |

form the simple cycle

 | v 7 − v 3 − v 1 − v 4 − v 8 − v 6 − v 2 − v 5 − v 7, v_{7}-v_{3}-v_{1}-v_{4}-v_{8}-v_{6}-v_{2}-v_{5}-v_{7}, |  |

which has length 8 8 (see Figure 10).

Thus, in all cases, G G contains a cycle of length 4 4 or 8 8.

v 1 v_{1} v 2 v_{2} v 3 v_{3} v 4 v_{4} v 5 v_{5} v 6 v_{6} v 7 v_{7} v 8 v_{8} Figure 10: Case 2: if v 3 ≠ v 5 v_{3}\neq v_{5}, an 8-cycle appears.

□ \square

## Acknowledgments

The author thanks Dr. Michael Albert, Editor-in-Chief of the Australasian Journal of Combinatorics, and one anonymous external expert for their careful reading of an earlier draft, advice, and for comments on the originality and merit of this work. Also, thank you to Dr. Tao Wang of Henan University for reading the first draft and presenting a counterexample to case 1 in personal communication that was accounted for in the author’s original notes but not in the first draft.

## References

- [1] P. Erdős, Some old and new problems in various branches of combinatorics, Discrete Math. 165/166 (1997), 227–231.
- [2] D. B. West, Erdős–Gyárfás conjecture on 2 2 -power cycle lengths, Open Problems page (UIUC), [https://dwest.web.illinois.edu/openp/2powcyc.htm][4] (accessed Jan. 2026).
- [3] P. Erdős, Problem 64, Erdős Problems, [https://www.erdosproblems.com/64][5]
(accessed Jan. 2026).
- [4] D. Daniel and S. E. Shauger, A result on the Erdős–Gyárfás conjecture in planar graphs, *Congressus Numerantium*153 (2001), 129–139.
- [5] P. Salehi Nowbandegani, H. Esfandiari, M. H. Shirdareh Haghighi, and K. Bibak, On the Erdős–Gyárfás conjecture in claw-free graphs, Discuss. Math. Graph Theory 34 (2014), 635–640.
- [6] C. C. Heckman and R. Krakovski, Erdős–Gyárfás conjecture for cubic planar graphs, *Electronic J. Combin.*20 (2) (2013), #P7.
- [7] Y. Gao and S. Shan, Erdős–Gyárfás conjecture for P 8 P_{8} -free graphs, *Graphs and Combinatorics*38 (2022), Article 168.
- [8] K. Markström, Extremal graphs for some problems on cycles in graphs, Congressus Numerantium 171 (2004), 177–188.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:
[4]: https://dwest.web.illinois.edu/openp/2powcyc.htm
[5]: https://www.erdosproblems.com/64
