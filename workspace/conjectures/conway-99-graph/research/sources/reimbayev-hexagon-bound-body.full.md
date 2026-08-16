<!-- source: https://arxiv.org/html/2409.10620v1 | converted from HTML -->

The Lower Bound for Number of Hexagons in Strongly Regular Graphs with Parameters = λ 1 and = μ 2

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2409.10620v1 [math.CO] 16 Sep 2024

# The Lower Bound for Number of Hexagons in Strongly Regular Graphs with Parameters λ = 1 \lambda=1 and μ = 2 \mu=2

Reimbay Reimbayev

###### Abstract

The existence of s ​ r ​ g ​ ( 99, 14, 1, 2) srg(99,14,1,2) has been a question of interest for several decades to the moment. In this paper we consider the structural properties in general for the family of strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2. In particular, we establish the lower bound for the number of hexagons and, by doing that, we show the connection between the existence of the aforementioned graph and the number of its hexagons.

## 1 Introduction

The existence of some graphs, most notably of those that have a very fine structure called strong regularity, is still not known [1, 2]. In his renowned set of five problems, John Conway [3] stated a problem regarding the search for one of such graphs. It states the following.

Problem: Is there 99-vertex graph such that the following conditions are satisfied: I. Any edge belongs to a unique triangle ( C 3 C_{3}); II. Any non-edge belongs to a unique quadrilateral ( C 4 C_{4})?

The problem is a rephrase of the search for a strongly-regular graph with parameters n = 99, k = 14, λ = 1, μ = 2, n=99,k=14,\lambda=1,\mu=2, in short, s ​ r ​ g ​ ( 99, 14, 1, 2) srg(99,14,1,2). Makhnev [4] has answered this question partially. In this paper, we study the structure of such graphs in general and find the lower bound for number of hexagons; in doing so, we show that if the lower bound for hexagons achieved then the graph doesn’t exist. Supporting this hypothesis is the fact that both of the known graphs of the same class, namely s ​ r ​ g ​ ( 9, 4, 1, 2) srg(9,4,1,2) (i.e. Paley 9) and s ​ r ​ g ​ ( 243, 22, 1, 2) srg(243,22,1,2), obey to it and take the lowest possible value for the number of hexagons.

Moreover, it does look like if the other two graphs in the same class with parameters k = 112 k=112 and k = 994 k=994 should exist have to be built of Paley 9, i.e. s ​ r ​ g ​ ( 9, 4, 1, 2) srg(9,4,1,2), as building blocks. But without strict proves we can only speculate about it.

## 2 Preliminary Study

For simplicity, a graph, satisfying conditions I and II without regard to its order n n, henceforth be denoted G G. First of all, let us show that the graph G G is indeed an srg. Obviously, G G is simple due to Condition I and with at least two vertices is connected due to Condition II. Also conditions guaranty that if G G is regular than it is strongly regular. Thus, we just need to prove the regularity.

###### Proposition 1.

Graph G G is regular, thus - strongly regular.

###### Proof.

We can safely assume that G G has at least two vertices or else, it does not have any edges or non-edges. Choose vertex a ∈ V ⁡ ( G) a\in V(G), G G is connected so there exists b ∈ G b\in G s.t. a ​ b ∈ E ⁡ ( G) ab\in E(G). Condition I guarantees the existence of the unique c c - the third vertex of the triangle with vertices a, b, c a,b,c. Denote N ⁡ ( v) N(v) - the set of vertices adjacent to a given vertex v v, its neighborhood excluding the vertex itself. If N ⁡ ( a) ∖ { a, c } = N ⁡ ( b) ∖ { b, c } = ∅ N(a)\setminus\{a,c\}=N(b)\setminus\{b,c\}=\varnothing then G = K 3 G=K_{3} thus 2-regular and by default is an s ​ r ​ g ​ ( 3, 2, 1, 2) srg(3,2,1,2). Otherwise choose v ∈ N ⁡ ( a) ∖ { b, c } v\in N(a)\setminus\{b,c\}. v ​ b ∉ E ⁡ ( G) vb\notin E(G) and v ​ c ∉ E ⁡ ( G) vc\notin E(G) due to Condition I. As v ​ b vb is a non-edge, Condition II identifies w ∈ N ⁡ ( b) w\in N(b) s.t. v ​ w ∈ E ⁡ ( G) vw\in E(G). v v is not adjacent to any other vertices from N ⁡ ( b) ∖ { a, c } N(b)\setminus\{a,c\}. Similarly w w cannot be adjacent to any other vertices from N ⁡ ( a) ∖ { b, c } N(a)\setminus\{b,c\}. Bijection has been established, which means the vertex degrees are equal, d a = d b d_{a}=d_{b}, i.e. a a and b b are vertices of equal valencies. G G is connected, thus for any x ∈ V ⁡ ( G) x\in V(G) there is a path a, y, …, x a,y,...,x, with d a = d y = … = d x d_{a}=d_{y}=...=d_{x}, so d a = d x d_{a}=d_{x}. G G is regular. ∎

[image: Refer to caption] Figure 1: Drawings of Paley 9 graph P 9 ≡ s ​ r ​ g ​ ( 9, 4, 1, 2) P_{9}\equiv srg(9,4,1,2).

As a result of the proposition, G G is strongly regular, s ​ r ​ g ​ ( n, k, λ, μ) srg(n,k,\lambda,\mu), where n n -number of vertices, k k - valency, that is necessarily even due to Condition I, λ = 1 \lambda=1 (also Condition I), μ = 2 \mu=2 (Condition II). Thus Conditions I and II define the class of strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2. The order of the graph n n and its valency k k are also related with a simple formula.

###### Proposition 2.

For a k k -regular graph G G satisfying Conditions I and II,

 | n = | V ⁡ ( G) | = k 2 + 2 2 n=|V(G)|=\frac{k^{2}+2}{2} |  |

.

###### Proof.

We will use the standard technique in Graph Theory called Double Counting. Let a ∈ V ⁡ ( G) a\in V(G), N ⁡ ( a) N(a) - neighborhood of a a, and W ⁡ ( a) = V ⁡ ( G) ∖ N ⁡ ( a) ∖ { a } W(a)=V(G)\setminus N(a)\setminus\{a\}, the set of vertices of G G different from a a and N ⁡ ( a) N(a). So we have: n = | V ⁡ ( G) | n=|V(G)|, | N ⁡ ( a) | = k |N(a)|=k, | W ⁡ ( a) | = n − k − 1 |W(a)|=n-k-1. Consider all the edges between N ⁡ ( a) N(a) and W ⁡ ( a) W(a). Then,

 | k ⁡ ( k − 2) = 2 ​ ( n − k − 1). k(k-2)=2(n-k-1). |  |

Left-hand side is due to regularity and Condition I; the right-hand side- due to Condition II. Solving the equation, we get n = k 2 + 2 2 n=\frac{k^{2}+2}{2}. ∎

Denote p 3, p 4, p 5 p_{3},p_{4},p_{5} and p 6 p_{6} the number of, respectively, triangles (induced subgraphs isomorphic to cycle C 3 C_{3}), quadrilaterals ( C 4 C_{4}), pentagons ( C 5 C_{5}) and hexagons ( C 6 C_{6}). The next few proposition are about the number of such polygons (cycles) in G G. The quantities p 3 p_{3}, and p 4 p_{4} can be found directly.

###### Proposition 3.

Graph G G has exactly 1 6 ​ n ​ k \frac{1}{6}nk triangles and 1 8 ​ n ​ k ​ ( k − 2) \frac{1}{8}nk(k-2) quadrilaterals.

###### Proof.

Straight-forward counting using Condition I and Handshaking Lemma gives:

 | p 3 = n ​ k 2 3 = n ​ k 6. p_{3}=\frac{\frac{nk}{2}}{3}=\frac{nk}{6}. |  |

To count the number of quadrilateral we will use the fact that each node of G G has n − k − 1 n-k-1 nodes (vertices) non-adjacent with it. Condition II guarantees exactly one quadrilateral for each of them. Counting over all the vertices and dividing to four, because we count each quadrilateral exactly four times, we obtain:

 | p 4 = n ⁡ ( n − k − 1) 4 = 1 4 ​ n ​ ( k 2 + 2 2 − k − 1) = 1 8 ​ n ​ k ​ ( k − 2). p_{4}=\frac{n(n-k-1)}{4}=\frac{1}{4}n(\frac{k^{2}+2}{2}-k-1)=\frac{1}{8}nk(k-2). |  |

Notice that we have used Proposition 2 here. ∎

To find p 5 p_{5} we need to work a bit harder.

###### Theorem 1.

Graph G has exactly 1 5 ​ n ​ k ​ ( k − 2) ​ ( k − 4) \frac{1}{5}nk(k-2)(k-4) pentagons.

###### Proof.

Any closed walk of length 5 in the graph can be coded into a string of six numbers d 1 ​ d 2 ​ d 3 ​ d 4 ​ d 5 ​ d 1 d_{1}d_{2}d_{3}d_{4}d_{5}d_{1}, which we denote here the distance between a vertex in a walk to its starting, and thus finishing, vertex. Pentagons will be coded by the string 012210 012210. Using the geometry of the graph, the first vertex can be chosen n n ways, the second - k k ways, the next three respectively k − 2, k − 2, 2 k-2,k-2,2 ways and the last vertex, being already predetermined, - one way. In total, there are exactly n ⋅ k ⋅ ( k − 2) ⋅ ( k − 2) ⋅ 2 ⋅ 1 = 2 ​ n ​ k ​ ( k − 2) 2 n\cdot k\cdot(k-2)\cdot(k-2)\cdot 2\cdot 1=2nk(k-2)^{2} of such walks. Except of pentagons, two more possible configurations, T 1 T_{1} and T 2 T_{2}, satisfy the same code (Figure 2).

[image: Refer to caption] Figure 2: Walks coded by string 012210 012210 and their induced subgraphs.

Thus, denoting t 1 t_{1} the number of subgraphs of type T 1 T_{1}, and t 2 t_{2} - of type T 2 T_{2}, we have

 | 2 ​ n ​ k ​ ( k − 2) 2 = 10 ⋅ p 5 + 6 ​ t 1 + 2 ​ t 2, 2nk(k-2)^{2}=10\cdot p_{5}+6t_{1}+2t_{2}, |  |

where t 1 = 4 ⋅ p 4 t_{1}=4\cdot p_{4}; and t 2 = 3 ​ ( k − 2) ⋅ p 3 t_{2}=3(k-2)\cdot p_{3}. The coefficients in front of t 1 t_{1} and t 2 t_{2} are coming from the symmetries of the walks.

So,

 | 10 ⋅ p 5 \displaystyle 10\cdot p_{5} | = 2 ​ n ​ k ​ ( k − 2) 2 − 6 ​ t 1 − 2 ​ t 2 \displaystyle=2nk(k-2)^{2}-6t_{1}-2t_{2} |  |

 |  | = 2 ​ n ​ k ​ ( k − 2) 2 − 6 ⋅ 4 ⋅ 1 4 ​ n ​ ( n − k − 1) − 2 ⋅ 3 ​ ( k − 2) ​ n ​ k 6 \displaystyle=2nk(k-2)^{2}-6\cdot 4\cdot\frac{1}{4}n(n-k-1)-2\cdot 3(k-2)\frac{nk}{6} |  |

 |  | = 2 ​ n ​ k ​ ( k − 2) 2 − 6 ​ n ​ ( k 2 + 2 2 − k − 1) − n ​ k ​ ( k − 2) \displaystyle=2nk(k-2)^{2}-6n(\frac{k^{2}+2}{2}-k-1)-nk(k-2) |  |

 |  | = 2 ​ n ​ k ​ ( k − 2) 2 − 3 ​ n ​ k ​ ( k − 2) − n ​ k ​ ( k − 2) \displaystyle=2nk(k-2)^{2}-3nk(k-2)-nk(k-2) |  |

 |  | = 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4). \displaystyle=2nk(k-2)(k-4). |  |

Notice that we have used Proposition 2 in calculations. The statement follows.

∎

The next statement follows immediately.

###### Corollary 1.

An edge of G G belongs to exactly 2 ​ ( k − 2) ​ ( k − 4) 2(k-2)(k-4) pentagons.

###### Proof.

On average, each edge belongs to p 5 / | E ⁡ ( G) | = 2 ​ ( k − 2) ​ ( k − 4) p_{5}/|E(G)|=2(k-2)(k-4) pentagons, where | E ⁡ ( G) | |E(G)| - number of edges in G G. So we just need to prove that this is the maximum number of pentagons possible for a given edge.

Given a ​ b ∈ E ⁡ ( G) ab\in E(G), each of k − 2 k-2 vertices of a a, out of triangle based on a ​ b ab, is adjacent to exactly one vertex from neighborhood of b b and is not adjacent to exactly k − 3 k-3. Remember Condition II. Now it gives us at most 2 ​ ( k − 2) ​ ( k − 3) − 2 ​ ( k − 2) = 2 ​ ( k − 2) ​ ( k − 4) 2(k-2)(k-3)-2(k-2)=2(k-2)(k-4) pentagons, where subtraction needed due to the two existing routs to each choice of k − 2 k-2 vertices. The statement follows. ∎

## 3 Main result

To find the number of hexagons we will compare two quantities: the coefficient c 6 c_{6} of the characteristic polynomial of the adjacency matrix of G G against the number of all possible triples of edges in G G, which is obviously ( | E ⁡ ( G) | 3) \binom{|E(G)|}{3}.

To begin with, we have to remind ourselves some known fact from algebraic graph theory. Given a graph G G, with its adjacency matrix A = A ⁡ ( G) A=A(G) and characteristic polynomial P G ​ ( x) P_{G}(x), the coefficients of its characteristic polynomial are connected with the structure of the graph in the following manner:

 | c i = ( − 1) i ​ ∑ | S | = i d ​ e ​ t ​ A ​ ( G ⁡ [S]), c_{i}=(-1)^{i}\sum_{|S|=i}detA(G[S]), |  | (1) |

where

 | P G ​ ( x) = d ​ e ​ t ​ ( λ ​ I − A) = ∑ i = 1 n ( x − λ i) = c 0 ​ x n + c 1 ​ x n − 1 + c 2 ​ x n − 2 ​ …, P_{G}(x)=det(\lambda I-A)=\sum_{i=1}^{n}(x-\lambda_{i})=c_{0}x^{n}+c_{1}x^{n-1}+c_{2}x^{n-2}..., |  |

and A ⁡ ( G ⁡ [S]) A(G[S]) is an adjacency matrix of an induced subgraph on the set of vertices S S (West, 2-nd ed., p.454 [5]). Here λ i \lambda_{i} -s are the eigenvalues of A ⁡ [G] A[G].

Instead of vertices, we can induce the subgraphs on the set of three edges, which might not always give a subgraph of order six. The next proposition asserts those cases.

###### Proposition 4.

Denote e 4 e_{4} - number of edge triples that are based on at most four vertices of G G, e 5 e_{5} - number of edge triples that are based on exactly five vertices of G G. The following equalities hold:

 | e 4 \displaystyle e_{4} | = 1 6 ​ n ​ k ​ ( 4 ​ k 2 − 9 ​ k + 3); \displaystyle=\frac{1}{6}nk(4k^{2}-9k+3); |  |

 | e 5 \displaystyle e_{5} | = 1 8 ​ n ​ k ​ ( k − 2) ​ ( k 3 + k 2 − 8 ​ k + 2). \displaystyle=\frac{1}{8}nk(k-2)(k^{3}+k^{2}-8k+2). |  |

###### Proof.

Three edges can be contained by three vertices if they are mutually incident and form a triangle in p 3 p_{3} ways. Three edges can all be incident to exactly one vertex, and thus being contained by four vertices, - in n ​ ( k 3) n\binom{k}{3} ways. And finally, three edges can be incident consequentially as in a path P 4 P_{4}: choose the middle edge arbitrarily from all possible edges; two adjacent ones - such that they do not form a triangle, - altogether, in n ​ k 2 ​ ( ( k − 1) 2 − 1) \frac{nk}{2}((k-1)^{2}-1) ways. Collecting,

 | e 4 = n ​ k 6 + n ​ ( k 3) + n ​ k 2 ​ ( ( k − 1) 2 − 1) = 1 6 ​ n ​ k ​ ( 4 ​ k 2 − 9 ​ k + 3). e_{4}=\frac{nk}{6}+n\binom{k}{3}+\frac{nk}{2}((k-1)^{2}-1)=\frac{1}{6}nk(4k^{2}-9k+3). |  |

Notice that different triples of edges can give the same induced subgraph, but it should not bother us at the moment as we are counting only distinct triples of edges, not subgraphs.

To find e 5 e_{5}, we have to realize that three edges can be incident to exactly five vertices only if two edges are incident while the third edge is not incident to the previous two. This fact means that among five vertices we always have one unique vertex with two edges incident to it. Choose that vertex, n n ways; next choose two incident to it edges out of k k possible. Here we have to consider two possibilities: when the pair of edges belong to a triangle, k 2 \frac{k}{2} pairs, and when they do not, ( k 2) − k 2 \binom{k}{2}-\frac{k}{2} cases. For each possibility, we will choose the third edge out of all possible edges not incident to the ones already chosen.

Thus,

 | e 5 \displaystyle e_{5} | = n ⁡ [k 2 ​ ( n ​ k 2 − 3 ​ ( k − 2) − 3) + ( ( k 2) − k 2) ​ ( n ​ k 2 − ( k − 2) − 2 ​ ( k − 1) − 2)] \displaystyle=n[\frac{k}{2}(\frac{nk}{2}-3(k-2)-3)+(\binom{k}{2}-\frac{k}{2})(\frac{nk}{2}-(k-2)-2(k-1)-2)] |  |

 |  | = 1 2 ​ n ​ k ​ ( k − 1) ​ ( n ​ k 2 − 3 ​ k + 2) + n ​ k 2 = 1 8 ​ n ​ k ​ ( k − 2) ​ ( k 3 + k 2 − 8 ​ k + 2). \displaystyle=\frac{1}{2}nk(k-1)(\frac{nk}{2}-3k+2)+\frac{nk}{2}=\frac{1}{8}nk(k-2)(k^{3}+k^{2}-8k+2). |  |

∎

Now we turn our attention to the case when three edges incident to six vertices. It is the case when we have a perfect matching, or three-edge covers of the six vertex subgraphs. We have to consider all possible subgraphs on six vertices of G G. They are given in the following two tables. Table 1 considers connected subgraphs and Table 2 - disconnected ones.

Table 1: Connected subgraphs |

num. | 1. | 2. | 3. | 4. |  |  | 5. |  | 6. |  | 7. |

Cvet. | 51 | 68 | 70 | 72 | 79 | 83 | 84 | 85 | 86 | 87 | 88 |

det. | 0 | -4 | 0 | -1 | -1 | -1 | 3 | -1 | 0 | -1 | 0 |

cov. | 4 | 2 | 2 | 3 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

 |

num. | 8. | 9. | 10. |  |  |  |  |  |  |  |  |

Cvet. | 89 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100 | 101 |

det. | -4 | -1 | 0 | 0 | 0 | -1 | -1 | -1 | 0 | -1 | 0 |

cov. | 2 | 3 | 2 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |

 |

num. |  |  | 11. |  | 12. |  |  |  |  |  |  |

Cvet. | 102 | 103 | 104 | 105 | 106 | 107 | 108 | 109 | 110 | 111 | 112 |

det. | -1 | 0 | 0 | -1 | -4 | 0 | 0 | 0 | -1 | 0 | -1 |

cov. | 1 | 0 | 2 | 1 | 2 | 0 | 0 | 0 | 1 | 0 | 1 |

Here, *num.*- is the special numeration of the graphs that do not vanish when we add the bottom rows: d ​ e ​ t. + c ​ o ​ v. det.+cov.; *Cvet.*- the numeration of six-vertex graphs due to Cvetcovic [10]; *det.*- is the determinant of the adjacency matrix of the given graph; *cov.*- number of edge covers of the graph by exactly three edges. Here we have to use [10] in order to make sure that we do not miss any graph. The paper gives a complete list of connected six-vertex graphs and allows us to refer to the graphs without necessarily drawing them. The values for the determinants have been found using online Matrix Calculator [11]. We will use them in summation for c 6 c_{6} from formula ( 1). Five more disconnected graphs on six vertices, that are not available from the list of Cvetcovic [10], are given in Table 2.

Table 2: Disconnected subgraphs |

num. | graph | det. | cov. |

 | [image: [Uncaptioned image]] | -1 | 1 |

 | [image: [Uncaptioned image]] | -1 | 1 |

13. | [image: [Uncaptioned image]] | 0 | 2 |

 | [image: [Uncaptioned image]] | -1 | 1 |

14. | [image: [Uncaptioned image]] | 4 | 0 |

In short, adding two quantities, c 6 c_{6} and ( | E ⁡ ( G) | 3) \binom{|E(G)|}{3} would allow us to eliminate, as it can be seen from the tables, most of the graphs and leave only twelve of them. They are given in Figure 3 with the same numeration as in tables. Denote n i n_{i} - number of graphs isomorphic to the graph enumerated by i, 1 ≤ i ≤ 12 i,1\leq i\leq 12, from the Figure 3. Then,

 |  | c 6 + ( | E ⁡ ( G) | 3) = 4 ​ n 1 − 2 ​ n 2 + 2 ​ n 3 + 2 ​ n 4 + 4 ​ n 5 + 2 ​ n 6 + 2 ​ n 7 − 2 ​ n 8 + 2 ​ n 9 + \displaystyle c_{6}+\binom{|E(G)|}{3}=4n_{1}-2n_{2}+2n_{3}+2n_{4}+4n_{5}+2n_{6}+2n_{7}-2n_{8}+2n_{9}+ |  |

 |  | 2 ​ n 10 + 2 ​ n 11 − 2 ​ n 12 + 2 ​ n 13 + 4 ​ n 14 + e 4 + e 5. \displaystyle 2n_{10}+2n_{11}-2n_{12}+2n_{13}+4n_{14}+e_{4}+e_{5}. |  | (2) |

[image: Refer to caption] Figure 3: The only induced subgraphs that have not been eliminated by summation c 6 + ( | E ⁡ ( G) | 3) c_{6}+\binom{|E(G)|}{3}. The enumeration is the same as in Table 1 and 2.

To proceed further, we need the next rather lengthy proposition. It will allow us to tie up all the quantities on the right hand side of ( 2).

###### Proposition 5.

The following equalities hold:

 | n 2 \displaystyle n_{2} | = 1 2 ​ n ​ k ​ ( k − 2); \displaystyle=\frac{1}{2}nk(k-2); |  | (3) |

 | n 4 + n 8 \displaystyle n_{4}+n_{8} | = n ​ k ​ ( k − 2) ​ ( k − 4); \displaystyle=nk(k-2)(k-4); |  | (4) |

 | 6 ​ n 1 + n 4 \displaystyle 6n_{1}+n_{4} | = 1 2 ​ n ​ k ​ ( k − 2); \displaystyle=\frac{1}{2}nk(k-2); |  | (5) |

 | 3 ​ n 1 + n 3 \displaystyle 3n_{1}+n_{3} | = 1 4 ​ n ​ k ​ ( k − 2); \displaystyle=\frac{1}{4}nk(k-2); |  | (6) |

 | 3 ​ n 1 + n 4 + n 9 \displaystyle 3n_{1}+n_{4}+n_{9} | = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 3); \displaystyle=\frac{1}{4}nk(k-2)(k-3); |  | (7) |

 | n 1 + n 3 + n 5 + n 14 \displaystyle n_{1}+n_{3}+n_{5}+n_{14} | = 1 12 ​ n ​ k ​ ( n ​ k 6 − 1) − 1 8 ​ n ​ k ​ ( k − 2); \displaystyle=\frac{1}{12}nk(\frac{nk}{6}-1)-\frac{1}{8}nk(k-2); |  | (8) |

 | 3 ​ n 1 + 2 ​ n 4 + n 6 + n 7 + 2 ​ n 9 + n 10 + n 11 + n 13 \displaystyle 3n_{1}+2n_{4}+n_{6}+n_{7}+2n_{9}+n_{10}+n_{11}+n_{13} | = 1 8 ​ n ​ k ​ ( k − 2) ​ ( n ​ k 2 − 4 ​ k + 4). \displaystyle=\frac{1}{8}nk(k-2)(\frac{nk}{2}-4k+4). |  | (9) |

###### Proof.

Take a quadrilateral from G G. Complete on its two adjacent sides triangles. We will get the unique graph of type 2 (Figure 3). So using Proposition 3:

 | n 2 = 4 ​ p 4 = 1 2 ​ n ​ k ​ ( k − 2). n_{2}=4p_{4}=\frac{1}{2}nk(k-2). |  |

Take a pentagon from G G. Complete a triangle on one of its sides. We can get the graph of type 4 or type 8 and no other one. Thus,

 | n 4 + n 8 = 5 ​ p 5 = n ​ k ​ ( k − 2) ​ ( k − 4). n_{4}+n_{8}=5p_{5}=nk(k-2)(k-4). |  |

Take a triangle in G G. Choose a vertex adjacent to one of the three vertices of the triangle, out of 3 ​ ( k − 2) 3(k-2) possible ones. Complete it uniquely the way we did it in Figure 5a. We have two possible configurations: 4 and 1. If we get graph 1, it should be counted six times as it can be obtained in six different ways.

 | 6 ​ n 1 + n 4 = p 3 ⋅ 3 ​ ( k − 2) = 1 2 ​ n ​ k ​ ( k − 2). 6n_{1}+n_{4}=p_{3}\cdot 3(k-2)=\frac{1}{2}nk(k-2). |  |

Take again a quadrilateral from G G. Similarly, complete two triangles but this time on its opposite sides. We can get either graph 3 or 1. If we get graph 1, we have to count it three times as it has three distinct quadrilaterals, we could start with.

 | 3 ​ n 1 + n 3 = 2 ​ p 4 = 1 4 ​ n ​ k ​ ( k − 2). 3n_{1}+n_{3}=2p_{4}=\frac{1}{4}nk(k-2). |  |

All three graphs:1, 4 and 9, consist of two quadrilaterals sharing an edge. Any edge belongs to exactly k − 2 k-2 quadrilaterals, from which we can choose pairs of quadrilaterals. Graph 1 again is counted three times as it has three pairs of such quadrilaterals. So,

 | 3 ​ n 1 + n 4 + n 9 = | E ⁡ ( G) | ​ ( k − 2 2) = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 3). 3n_{1}+n_{4}+n_{9}=|E(G)|\binom{k-2}{2}=\frac{1}{4}nk(k-2)(k-3). |  |

The four graphs: 1, 3, 5, and 14 are all consist of exactly two triangles that do not share a vertex. In order to find all such configurations we simply need to subtract from all possible pairs of triangles those that DO share a vertex. Remember, they can share at most one vertex due to condition 1. Thus,

 | n 1 + n 3 + n 5 + n 14 = ( p 3 2) − n ​ ( k / 2 2) = 1 12 ​ n ​ k ​ ( n ​ k 6 − 1) − 1 8 ​ n ​ k ​ ( k − 2). n_{1}+n_{3}+n_{5}+n_{14}=\binom{p_{3}}{2}-n\binom{k/2}{2}=\frac{1}{12}nk(\frac{nk}{6}-1)-\frac{1}{8}nk(k-2). |  |

Finally, the last relation bonds the graphs that can be obtained by choosing a quadrilateral and an edge that is not incident to any of the vertices of the quadrilateral. Notice, once a quadrilateral is chosen, the choice of an edge uniquely defines the six-vertex graph. Thus, the coefficients in front of the quantities depend only on number of quadrilaterals the graph has.

 | 3 ​ n 1 + 2 ​ n 4 + n 6 + n 7 + 2 ​ n 9 + n 10 + n 11 + n 13 \displaystyle 3n_{1}+2n_{4}+n_{6}+n_{7}+2n_{9}+n_{10}+n_{11}+n_{13} | = p 4 ​ ( | E ⁡ ( G) | − 4 ​ ( k − 2) − 4) \displaystyle=p_{4}(|E(G)|-4(k-2)-4) |  |

 |  | = 1 8 ​ n ​ k ​ ( k − 2) ​ ( n ​ k 2 − 4 ​ k + 4). \displaystyle=\frac{1}{8}nk(k-2)(\frac{nk}{2}-4k+4). |  |

∎

Now, when we are equipped with all the relations from Proposition 5, we can proceed with (2). But first, let us remind ourselves what we are trying to achieve with all these cumbersome calculations. We want to find n 12 n_{12} - the number of subgraphs of type 12 in G G, namely hexagons (Figure 3).

Rewrite (2),

 |  | 2 ​ n 1 − n 2 + n 3 + n 4 + 2 ​ n 5 + n 6 + n 7 − n 8 + n 9 + n 10 + n 11 − n 12 + n 13 + 2 ​ n 14 \displaystyle 2n_{1}-n_{2}+n_{3}+n_{4}+2n_{5}+n_{6}+n_{7}-n_{8}+n_{9}+n_{10}+n_{11}-n_{12}+n_{13}+2n_{14} |  |

 |  | = 1 2 ​ ( c 6 + ( | E ⁡ ( G) | 3) − e 4 − e 5). \displaystyle=\frac{1}{2}(c_{6}+\binom{|E(G)|}{3}-e_{4}-e_{5}). |  |

Subtracting (9) from this expression, we obtain,

 |  | − n 1 − n 2 + n 3 − n 4 + 2 ​ n 5 − n 8 − n 9 − n 12 + 2 ​ n 14 \displaystyle-n_{1}-n_{2}+n_{3}-n_{4}+2n_{5}-n_{8}-n_{9}-n_{12}+2n_{14} |  |

 |  | = 1 2 ​ ( c 6 + ( | E ⁡ ( G) | 3) − e 4 − e 5) − 1 8 ​ n ​ k ​ ( k − 2) ​ ( n ​ k 2 − 4 ​ k + 4). \displaystyle=\frac{1}{2}(c_{6}+\binom{|E(G)|}{3}-e_{4}-e_{5})-\frac{1}{8}nk(k-2)(\frac{nk}{2}-4k+4). |  |

Further subtracting double of (8), we get rid of n 5 n_{5} and n 14 n_{14},

 |  | − 3 ​ n 1 − n 2 − n 3 − n 4 − n 8 − n 9 − n 12 = 1 2 ​ ( c 6 + ( | E ⁡ ( G) | 3) − e 4 − e 5) \displaystyle-3n_{1}-n_{2}-n_{3}-n_{4}-n_{8}-n_{9}-n_{12}=\frac{1}{2}(c_{6}+\binom{|E(G)|}{3}-e_{4}-e_{5}) |  |

 |  | − 1 8 ​ n ​ k ​ ( k − 2) ​ ( n ​ k 2 − 4 ​ k + 4) − 1 6 ​ n ​ k ​ ( n ​ k 6 − 1) + 1 4 ​ n ​ k ​ ( k − 2). \displaystyle-\frac{1}{8}nk(k-2)(\frac{nk}{2}-4k+4)-\frac{1}{6}nk(\frac{nk}{6}-1)+\frac{1}{4}nk(k-2). |  |

The right hand side of the expression is getting horrible and Wolfram Alfa [12] here is of no help (or we just didn’t find the way to use it properly), but we should not worry about it at the moment and rather concentrate on the left-hand side solely. Using (3), (4) and (6), we get

 |  | − n 9 − n 12 = 1 2 ​ ( c 6 + ( | E ⁡ ( G) | 3) − e 4 − e 5) − 1 8 ​ n ​ k ​ ( k − 2) ​ ( n ​ k 2 − 4 ​ k + 4) \displaystyle-n_{9}-n_{12}=\frac{1}{2}(c_{6}+\binom{|E(G)|}{3}-e_{4}-e_{5})-\frac{1}{8}nk(k-2)(\frac{nk}{2}-4k+4) |  |

 |  | − 1 6 ​ n ​ k ​ ( n ​ k 6 − 1) + 1 4 ​ n ​ k ​ ( k − 2) + 3 4 ​ n ​ k ​ ( k − 2) + n ​ k ​ ( k − 2) ​ ( k − 4). \displaystyle-\frac{1}{6}nk(\frac{nk}{6}-1)+\frac{1}{4}nk(k-2)+\frac{3}{4}nk(k-2)+nk(k-2)(k-4). |  |

Next, we express n 9 n_{9} through needed n 4 n_{4}, using (7) and (5).

 | n 9 = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 3) − 1 4 ​ n ​ k ​ ( k − 2) − n 4 2. n_{9}=\frac{1}{4}nk(k-2)(k-3)-\frac{1}{4}nk(k-2)-\frac{n_{4}}{2}. |  |

Substituting,

 |  | n 4 2 − n 12 = 1 2 ​ ( c 6 + ( | E ⁡ ( G) | 3) − e 4 − e 5) − 1 8 ​ n ​ k ​ ( k − 2) ​ ( n ​ k 2 − 4 ​ k + 4) \displaystyle\frac{n_{4}}{2}-n_{12}=\frac{1}{2}(c_{6}+\binom{|E(G)|}{3}-e_{4}-e_{5})-\frac{1}{8}nk(k-2)(\frac{nk}{2}-4k+4) |  |

 |  | − 1 6 ​ n ​ k ​ ( n ​ k 6 − 1) + 3 4 ​ n ​ k ​ ( k − 2) + n ​ k ​ ( k − 2) ​ ( k − 4) + 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 3). \displaystyle-\frac{1}{6}nk(\frac{nk}{6}-1)+\frac{3}{4}nk(k-2)+nk(k-2)(k-4)+\frac{1}{4}nk(k-2)(k-3). |  |

Denoting right hand side by − F ⁡ ( n, k) -F(n,k), we have:

 | n 4 2 − n 12 = − F ⁡ ( n, k). \frac{n_{4}}{2}-n_{12}=-F(n,k). |  |

Notice also that from (5) and (6) n 4 = 2 ​ n 3 n_{4}=2n_{3}. Thus,

 | n 12 = F ⁡ ( n, k) + n 3. n_{12}=F(n,k)+n_{3}. |  |

Tedious calculations are required in order to proceed further with the expression on the right hand side. The challenge is the coefficient c 6 c_{6} that is inside F ⁡ ( n, k) F(n,k). It can be easily calculated numerically for a particular value of n n and k k, using the relation

 | c 6 = k ​ ∑ i = 0 5 ( r 1 5 − i) ​ ( r 2 i) ​ λ 1 5 − i ​ λ 2 i + ∑ i = 0 6 ( r 1 6 − i) ​ ( r 2 i) ​ λ 1 6 − i ​ λ 2 i. c_{6}=k\sum_{i=0}^{5}\binom{r_{1}}{5-i}\binom{r_{2}}{i}\lambda_{1}^{5-i}\lambda_{2}^{i}+\sum_{i=0}^{6}\binom{r_{1}}{6-i}\binom{r_{2}}{i}\lambda_{1}^{6-i}\lambda_{2}^{i}. |  |

Here λ 1, λ 2 \lambda_{1},\lambda_{2} = eigenvalues of an adjacency matrix A ⁡ ( G) A(G), and r 1, r 2 r_{1},r_{2} their respective multiplicities. In particular, the characteristic polynomial P G ​ ( x) = ( x − k) ​ ( x − λ 1) r 1 ​ ( x − λ 2) r 2. P_{G}(x)=(x-k)(x-\lambda_{1})^{r_{1}}(x-\lambda_{2})^{r_{2}}.

Table 3: The values of c 6 c_{6} for several orders of G G |

n | k | c 6 c_{6} |

9 | 4 | -168 |

99 | 14 | -47,288,703 |

243 | 22 | -2,975,686,065 |

6,273 | 112 | -7,204,770,339,625,320 |

494,019 | 994 | -2,466,795,174,682,153,663,896,408 |

The numerical values of c 6 c_{6} for several orders of G G are given in the above table. The calculations are done using Julia programming language [8]. Further heavily relying on computation machinery of Wolfram Alpha [12] with the use of the additional relations for eigenvalues and their multiplicities (see West, 2-nd ed., p.466 [5]) such as:

 | λ 1 + λ 2 \displaystyle\lambda_{1}+\lambda_{2} | = − 1; \displaystyle=-1; |  |

 | λ 1 ​ λ 2 \displaystyle\lambda_{1}\lambda_{2} | = − ( k − 2); \displaystyle=-(k-2); |  |

 | r 1 + r 2 \displaystyle r_{1}+r_{2} | = n − 1; \displaystyle=n-1; |  |

we will obtain a formula

 | c 6 = − 1 576 ​ n ​ k ​ ( k − 2) ​ ( 3 ​ k 5 + 6 ​ k 4 − 84 ​ k 3 + 116 ​ k 2 + 124 ​ k − 240). c_{6}=-\frac{1}{576}nk(k-2)(3k^{5}+6k^{4}-84k^{3}+116k^{2}+124k-240). |  |

Finally, plugging everything back into F ⁡ ( n, k) F(n,k), the expression for n 12 n_{12} simplifies to

 | n 12 = 1 12 ​ n ​ k ​ ( k − 2) ​ ( 2 ​ k 2 − 21 ​ k + 53) + n 3. n_{12}=\frac{1}{12}nk(k-2)(2k^{2}-21k+53)+n_{3}. |  |

By this and n 3 ≥ 0 n_{3}\geq 0, we have proven the following statement:

###### Theorem 2.

The number of hexagons in G G is at least 1 12 ​ n ​ k ​ ( k − 2) ​ ( 2 ​ k 2 − 21 ​ k + 53) \frac{1}{12}nk(k-2)(2k^{2}-21k+53).

## 4 Conclusion

In this paper we have studied the structure of a class of strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2. We have shown that the lower bound for the number of hexagons in such graphs is 1 12 ​ n ​ k ​ ( k − 2) ​ ( 2 ​ k 2 − 21 ​ k + 53) \frac{1}{12}nk(k-2)(2k^{2}-21k+53). We conjecture that the lower bound is indeed the true value for p 6 p_{6} due to many symmetries broken otherwise. This bound is achieved when n 3 = 0 n_{3}=0, which in turn meaning that two triangles in G G connected through two edges are necessarily connected through the third one. Given such condition, Makhnev [4] has proved that s ​ r ​ g ​ ( 99, 14, 1, 2) srg(99,14,1,2) doesn’t exist.

###### Conjecture.

The number of hexagons in strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2 is equal to 1 12 ​ n ​ k ​ ( k − 2) ​ ( 2 ​ k 2 − 21 ​ k + 53) \frac{1}{12}nk(k-2)(2k^{2}-21k+53).

Several things worth noticing. First, given the conjecture is true, Makhnev’s condition holds not only for a graph with n = 99 n=99 and k = 14 k=14 but for the entire family of strongly regular graphs with λ = 1 \lambda=1 and μ = 2 \mu=2. This can be observed for the case when k = 4 k=4 or Paley 9. Some preliminary checks show that it holds for another known graph from the family - the Berlekamp–Van Lint–Seidel graph, for k = 22 k=22 [7]. Second, all the graphs, except of trivial case K 3 K_{3}, must be built of Paley 9 graphs as building blocks if the conjecture is true. In particular, both of the yet unknown graphs for k = 112 k=112 and k = 994 k=994 in that case have more coarse structure. Their P 9 P_{9} -built structure might give us an insight on their existence as well.

## References

- [1] Royle, Gordon, *List of Large Graphs and Families*, http://people.csse.uwa.edu.au/gordon/remote/srgs/
- [2] Brouwer, Andries E., *Parameters of Strongly Regular Graphs*, https://www.win.tue.nl/~aeb/graphs/srg/srgtab.html
- [3] Conway, John (Update 2017), *Five $ 1,000 Problems*, On-Line Encyclopedia of Integer Sequences, OEIS sequance A248380.
- [4] Makhnev, A. (1988), *Strongly Regular Graphs with λ = 1 \lambda=1*, Matemticheskie Zametki, Vol.44, No.5, pp.667-672, Academy of Sciences of the USSR.
- [5] West, Douglas B. (2000) *Introduction to Graph Theory*, Pearson Education Limited, 2-nd ed.
- [6] Cvetcovic, Dragos; Rowlinson, Peter; Simic, Slobodan (2010), *An Introduction to the Theory of Graph Spectra*, Cambridge University Press
- [7] Berlekamp, E.R.; Van Lint, J.H.; Seidel, J.J.(1973), *A strongly regular graph derived from the perfect ternary Golay code*, A survey of combinatorial theory, Amsterdam, 25-30.
- [8] The Julia Programming Language, https://julialang.org/
- [9] Information System on Graph Classes and their Inclusions, https://www.graphclasses.org/smallgraphs.html#nodes4
- [10] Cvetcovic, Dragos; Petric, Milenko (1984), *A Table of Connected Graphs on Six Vertices*, Discrete Mathematics 50, 37-49, Elsevier, North-Holland
- [11]*Online Matrix Calculator App*, https://matrixcalc.org/en/
- [12] Wolfram Research, Inc. (2021), *Mathematica Online*, Champaign, IL www.wolfram.com


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
