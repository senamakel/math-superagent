<!-- source: https://arxiv.org/html/2508.03377v2 | converted from HTML -->

The Subgraphs of Order Six of the Family of Strongly Regular Graphs with Parameters = λ 1 and = μ 2

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2508.03377v2 [math.CO] 03 Nov 2025

# The Subgraphs of Order Six of the Family of Strongly Regular Graphs with Parameters λ = 1 \lambda=1 and μ = 2 \mu=2

Reimbay Reimbayev

###### Abstract

Strongly regular graphs are highly symmetrical and can be described fully with just a few parameters yet the existence of many of them is still under the question. Due to this uncertainty, it is of immense interest to study their structure, in particular to obtain all the possible subgraphs of lower order. In this paper we study the family of strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2 and establish all their subgraphs of order six.

## 1 Introduction

The existence of s ​ r ​ g ​ ( 99, 14, 1, 2) srg(99,14,1,2), famously known as Conway’s 99-vertex graph problem [1], is an intriguing one. But this is just one graph from the family of strongly regular graphs for which only few known to exist, e.g. those with valencies k = 2, 4 k=2,4 and, surprisingly 22 [2]. For that reason it is of interest to study the structure for the entire family of such graphs rather than just for a particular one. In this paper we have studied all possible subgraphs of order up to six and gave their numbers depending on the order n n (or valency k k, which is interrelated) of such graphs given they do exist.

As a short reminder, the graph is strongly regular if a pair of its vertices has exactly λ \lambda common neighbors given they are adjacent, or μ \mu common neighbors otherwise [3, 4]. Another way of defining strongly regular graphs, perhaps more precise as it cuts away some trivial cases like complete graphs, is by using spectral graph theory by which the finite graph is strongly regular if its spectrum consists of exactly three eigenvalues, one of which is k k with multiplicity one [5].

There have been some extensive studies by Makhnev et. al. on the structure of the family of strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2 with regard to their automorphism groups [6]. Also, Makhnev was able to partially answer to the question of the existence of the graph s ​ r ​ g ​ ( 99, 14, 1, 2) srg(99,14,1,2) in his earlier work [7]. Using Wilbrink and Brouwer’s lemma [8], Lou and Murin were able to establish a forbidden subgraph of order 9 in cade when k = 14 k=14 [9]. This fact should hold true for any k k, which needs a strict proof of course.

In our previous work we have shown that the existance of this graph depends also on number of hexagons it contain [10], for which we have set a lower bound. It worth to note that the number of subgraphs of order up to five are all uniquely defined. And only starting with subgraphs of order six the problem of their quantification begins. In this paper we have resolved this problem for six vertex subgraphs setting one of the values, namely n 3 n_{3}, as a free variable.

We will divide the paper into subsections in the following matter. First we will bring all the possible six-vertex subgraphs with derivations of their possible numbers. Then the formulas will be summarized at the end of the subsection. One who wishes to skip all the derivations can fast forward to the end of the next subsection.

Also, in order to find some of the values for six-vertex subgraphs it is necessary to know the values for five-vertex subgraphs upfront, which are in our case are all exact and depend only on n n and k k. We will omit the derivations of those values, giving just formulas further, as they can be obtain in a similar but much easier way. Together with five-vertex subgraphs, we will also give values for all four-vertex subgraphs also without derivations.

Finally, we need the next proposition.

###### Proposition 1.

Consider p i p_{i} for i = 3, 4, 5 i=3,4,5 is the number of triangles, quadrilaterals and pentagons respectively in a strongly regular graph s ​ r ​ g ​ ( n, k, 1, 2) srg(n,k,1,2). Then,

 | p 3 = \displaystyle p_{3}= | 1 6 ​ n ​ k, \displaystyle\frac{1}{6}nk, |  |

 | p 4 = \displaystyle p_{4}= | 1 8 ​ n ​ k ​ ( k − 2), \displaystyle\frac{1}{8}nk(k-2), |  |

 | p 5 = \displaystyle p_{5}= | 1 5 ​ n ​ k ​ ( k − 2) ​ ( k − 4). \displaystyle\frac{1}{5}nk(k-2)(k-4). |  |

###### Proof.

The proof has given in [10]. ∎

## 2 Derivations of the Formulas

A strongly regular graphs of sufficiently high order with parameters λ = 1 \lambda=1 and μ = 2 \mu=2, for simplicity henceforth call it a graph G G, have exactly 62 possible subgraphs of order six (Figure 1). Note that for the graphs of smaller order not all the subgraphs would exist. The subgraphs were obtained through extensive search of all six-vertex graphs that do not break strong-regularity condition for the main graph. Let us denote N i N_{i} the graphs of type i i from the Figure 1 and by n i n_{i} the number of such graphs in G G.

[image: Refer to caption] Figure 1: All possible subgraphs of order six in s ​ r ​ g ​ ( n, k, 1, 2) srg(n,k,1,2).

As the exact numbers for six-vertex subgraphs are not known, compared to five-vertex ones, for which it is easy to obtain the exact formulas, we will have to use n 3 n_{3} as a free variable compared to which all other values will be calculated.

For n 1 n_{1}, given a quadrilateral, recover triangles on its opposite sides. So we get the relation

 | 2 ​ p 4 = 3 ​ n 1 + n 3. 2p_{4}=3n_{1}+n_{3}. |  |

Thus,

 | n 1 = 1 12 ​ n ​ k ​ ( k − 2) − 1 3 ​ n 3. n_{1}=\frac{1}{12}nk(k-2)-\frac{1}{3}n_{3}. |  |

Notice, that we have left n 3 n_{3} as an unknown parameter through which we will define all other values as noted above.

For n 2 n_{2}, given a quadrilateral, choose this time triangles on adjacent sides,

 | n 2 = 4 ​ p 4 = 1 2 ​ n ​ k ​ ( k − 2). n_{2}=4p_{4}=\frac{1}{2}nk(k-2). |  |

For n 3 n_{3}, n 3 = n 3 n_{3}=n_{3}.

For n 4 n_{4}, given a triangle v 0 ​ v 1 ​ v 2 v_{0}v_{1}v_{2}, there exist exactly 3 ​ ( k − 2) 3(k-2) distinct vertices of G G, each adjacent to exactly one of the vertices of the triangle v 0 ​ v 1 ​ v 2 v_{0}v_{1}v_{2}. Choose one, w 0 w_{0}, assume it is adjacent to v 0 v_{0}. The next two vertices w 1 w_{1} and w 2 w_{2} are predetermined as common neighbors of w 0 w_{0} and v 1 v_{1} and w 0 w_{0} and v 2 v_{2} respectively. Now, v 0 ​ v 1 ​ v 2 ​ w 0 ​ w 1 ​ w 2 v_{0}v_{1}v_{2}w_{0}w_{1}w_{2} can give us a subgraph isomorphic to either N 1 N_{1} or N 4 N_{4}. Thus, by this construction we will get:

 | 3 ​ ( k − 2) ​ p 3 = 6 ​ n 1 + n 4. 3(k-2)p_{3}=6n_{1}+n_{4}. |  |

From where,

 | n 4 = 1 2 ​ n ​ k ​ ( k − 2) − 6 ​ n 1 = 2 ​ n 3. n_{4}=\frac{1}{2}nk(k-2)-6n_{1}=2n_{3}. |  |

For n 5 n_{5}, choose an edge v 1 ​ v 2 v_{1}v_{2}. Excluding a triangle based on v 1 ​ v 2 v_{1}v_{2}, choose one of the k 2 − 1 \frac{k}{2}-1 incident triangles for each vertex v 1 v_{1} and v 2 v_{2}. We obtain:

 | | E ⁡ ( G) | ​ ( k 2 − 1) 2 = n 5 + 2 ​ n 3 + 3 ​ n 1. |E(G)|(\frac{k}{2}-1)^{2}=n_{5}+2n_{3}+3n_{1}. |  |

And after algebraic operations,

 | n 5 = 1 8 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − n 3. n_{5}=\frac{1}{8}nk(k-2)(k-4)-n_{3}. |  |

For n 6 n_{6}, choose a quadrilateral, recover a triangle based on one of its sides. There are exactly k − 2 k-2 vertices adjacent to the third recovered vertex of the triangle. Thus,

 | 4 ​ ( k − 2) ​ p 4 = n 6 + 2 ​ n 4 + 6 ​ n 1. 4(k-2)p_{4}=n_{6}+2n_{4}+6n_{1}. |  |

Plugging the values,

 | n 6 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 3) − 2 ​ n 3. n_{6}=\frac{1}{2}nk(k-2)(k-3)-2n_{3}. |  |

For n 7 n_{7}, choose a quadrilateral, at one of its vertices recover one of the k 2 − 2 \frac{k}{2}-2 triangles that are not based on the sides of the quadrilateral. Notice that there cannot be any new edges between the quadrilateral and the triangle. We have

 | 4 ​ p 4 ​ ( k 2 − 2) = n 7. 4p_{4}(\frac{k}{2}-2)=n_{7}. |  |

So,

 | n 7 = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4). n_{7}=\frac{1}{4}nk(k-2)(k-4). |  |

For n 8 n_{8}, choose a pentagon. Recover on one of its sides a triangle. Thus,

 | 5 ​ p 5 = n 8 + n 4. 5p_{5}=n_{8}+n_{4}. |  |

And

 | n 8 = n ​ k ​ ( k − 2) ​ ( k − 4) − 2 ​ n 3. n_{8}=nk(k-2)(k-4)-2n_{3}. |  |

For n 9 n_{9}, choose an edge. Due to topology of the graph, there exactly k − 2 k-2 quadrilaterals based on that edge. Choose two. Thus,

 | | E ⁡ ( G) | ​ ( k − 2 2) = n 9 + n 4 + 3 ​ n 1. |E(G)|{k-2\choose 2}=n_{9}+n_{4}+3n_{1}. |  |

After some algebra,

 | n 9 = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − n 3. n_{9}=\frac{1}{4}nk(k-2)(k-4)-n_{3}. |  |

For n 10 n_{10}, choose a pentagon in p 5 p_{5} ways. Now we have exactly five pairs of vertices at distance two from each other on that pentagon. To each such pair, there is a unique vertex to recover a quadrilateral on the given pair of vertices. We have

 | 5 ​ p 5 = 2 ​ n 10 + 2 ​ n 4. 5p_{5}=2n_{10}+2n_{4}. |  |

From where,

 | n 10 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − 2 ​ n 3. n_{10}=\frac{1}{2}nk(k-2)(k-4)-2n_{3}. |  |

Notice that N 10 N_{10} will be counted twice by this construction due to two distinct pentagons, while N 4 N_{4} - due to two pairs of vertices of the same pentagon.

For n 11 n_{11}, let us notice that the graph N 11 N_{11} has only one vertex of degree three. We will use that vertex as a starting point for our construction, n n ways. Three adjacent to the first vertex but mutually not connected vertices can be chosen in 1 6 ​ k ​ ( k − 2) ​ ( k − 4) \frac{1}{6}k(k-2)(k-4) ways. Out of these three choose a pair and complete a quadrilateral. By this we have obtain the fifth vertex. To choose the last vertex of degree one (a leaf) we have k − 4 k-4 choices.

 | n ​ k ​ ( k − 2) ​ ( k − 4) 6 ​ 3 ​ ( k − 4) = n 11 + 2 ​ n 10. n\frac{k(k-2)(k-4)}{6}3(k-4)=n_{11}+2n_{10}. |  |

Or

 | n 11 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) + 4 ​ n 3. n_{11}=\frac{1}{2}nk(k-2)(k-4)(k-6)+4n_{3}. |  |

For n 12 n_{12}, it has been already found in [10]. Here we find it in another much easier way in two steps. First, we find the number of paths P 5 P_{5}, which we denoted earlier m 13 m_{13}. Choose a vertex, the middle one in P 5 P_{5}; next, two vertices adjacent to it; and finally, two leaves. We have

 | n ​ k ⁡ ( k − 2) 2 ​ ( k − 3) 2 = m 13 + 5 ​ p 5. n\frac{k(k-2)}{2}(k-3)^{2}=m_{13}+5p_{5}. |  |

Or

 | m 13 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k 2 − 8 ​ k + 17). m_{13}=\frac{1}{2}nk(k-2)(k^{2}-8k+17). |  |

Next construction: choose P 5 P_{5} from G G. Two leaves of P 5 P_{5} share exactly two neighbors all distinct from other vertices of chosen P 5 P_{5}. Choosing one of these neighbors, we have

 | 2 ​ m 13 = 6 ​ n 12 + 2 ​ n 9 + n 8 + n 2. 2m_{13}=6n_{12}+2n_{9}+n_{8}+n_{2}. |  |

Plugging all known values,

 | n 12 = 1 12 ​ n ​ k ​ ( k − 2) ​ ( 2 ​ k 2 − 21 ​ k + 53) + n 3. n_{12}=\frac{1}{12}nk(k-2)(2k^{2}-21k+53)+n_{3}. |  |

For n 13 n_{13}, choose a quadrilateral. Next, choose an edge of G G that is not incident to that quadrilateral. We have:

 | p 4 ​ ( | E ⁡ ( G) | − 12 − 4 ​ ( k − 4)) = n 13 + n 11 + n 10 + 2 ​ n 9 + n 7 + n 6 + 2 ​ n 4 + 3 ​ n 1. p_{4}(|E(G)|-12-4(k-4))=n_{13}+n_{11}+n_{10}+2n_{9}+n_{7}+n_{6}+2n_{4}+3n_{1}. |  |

From where

 | n 13 = 1 32 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 12 ​ k + 42) − n 3. n_{13}=\frac{1}{32}nk(k-2)(k-4)(k^{2}-12k+42)-n_{3}. |  |

For n 14 n_{14}, consider all pairs of triangles that do not share a common vertex. Thus,

 | 1 2 ​ p 3 ​ ( p 3 − 1) − 1 2 ​ n ⋅ k 2 ​ ( k 2 − 1) = n 1 + n 3 + n 5 + n 14. \frac{1}{2}p_{3}(p_{3}-1)-\frac{1}{2}n\cdot\frac{k}{2}(\frac{k}{2}-1)=n_{1}+n_{3}+n_{5}+n_{14}. |  |

So,

 | n 14 = 1 144 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 12) + n 3 3. n_{14}=\frac{1}{144}nk(k-2)(k-4)(k-12)+\frac{n_{3}}{3}. |  |

For n 15 n_{15}, choose a vertex. Then choose two adjacent to it triangles and a leaf. We have

 | n 15 = n ​ ( k / 2 2) ​ ( k − 4) = 1 8 ​ n ​ k ​ ( k − 2) ​ ( k − 4). n_{15}=n{k/2\choose 2}(k-4)=\frac{1}{8}nk(k-2)(k-4). |  |

For n 16 n_{16}, choose a vertex, then two triangles adjacent to it. To one of the four degree-two vertices attach a leaf in k − 4 k-4 ways.

 | n 16 = n ​ ( k / 2 2) ​ 4 ​ ( k − 4) = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4). n_{16}=n{k/2\choose 2}4(k-4)=\frac{1}{2}nk(k-2)(k-4). |  |

For n 17 n_{17}, choose a quadrilateral, recover on one of its sides a triangle, at one of the vertices of degree three attach a leaf in k − 4 k-4 ways. The graph has been uniquely built.

 | n 17 = p 4 ⋅ 4 ⋅ 2 ​ ( k − 4) = n ​ k ​ ( k − 2) ​ ( k − 4). n_{17}=p_{4}\cdot 4\cdot 2(k-4)=nk(k-2)(k-4). |  |

For n 18 n_{18}, choose a quadrilateral, recover a triangle on one of its sides. To one of the remaining vertices of the quadrilateral of degree two attach a leaf in k − 4 k-4 ways. We obtain

 | p 4 ⋅ 4 ⋅ 2 ​ ( k − 4) = n 18 + 2 ​ n 4. p_{4}\cdot 4\cdot 2(k-4)=n_{18}+2n_{4}. |  |

Thus,

 | n 18 = n ​ k ​ ( k − 2) ​ ( k − 4) − 4 ​ n 3. n_{18}=nk(k-2)(k-4)-4n_{3}. |  |

For n 19 n_{19}, notice that it has only one vertex of degree five. We will start the construction from it. Choose a vertex, a triangle attached to it, and three leaves.

 | n 19 = n ⋅ k 2 ⋅ ( k − 2) ​ ( k − 4) ​ ( k − 6) 6 = 1 12 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6). n_{19}=n\cdot\frac{k}{2}\cdot\frac{(k-2)(k-4)(k-6)}{6}=\frac{1}{12}nk(k-2)(k-4)(k-6). |  |

For n 2 ​ 0 n_{2}0, choose a vertex, a triangle attached to it, and two leaves. To one of the two new vertices of the triangle, attach a leaf in k − 4 k-4 ways. Thus,

 | n 20 = n ⋅ k 2 ⋅ ( k − 2) ​ ( k − 4) 2 ⋅ 2 ​ ( k − 4) = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) 2. n_{20}=n\cdot\frac{k}{2}\cdot\frac{(k-2)(k-4)}{2}\cdot 2(k-4)=\frac{1}{2}nk(k-2)(k-4)^{2}. |  |

For n 21 n_{21}, choose a triangle , for every vertex of the triangle choose one of its other k − 2 k-2 neighbors. We get,

 | p 3 ​ ( k − 3) 3 = n 21 + n 6 + n 4 + 2 ​ n 1. p_{3}(k-3)^{3}=n_{21}+n_{6}+n_{4}+2n_{1}. |  |

So,

 | n 21 = 1 6 ​ n ​ k ​ ( k − 2) ​ ( k − 3) ​ ( k − 4) + 2 3 ​ n 3. n_{21}=\frac{1}{6}nk(k-2)(k-3)(k-4)+\frac{2}{3}n_{3}. |  |

For n 22 n_{22}, once more we look at the vertex of highest degree of the subgraph. To that vertex we attach a triangle in k / 2 k/2 ways, and add two other vertices, to one of which we need to add an extra vertex out of k − 5 k-5 possible choices. Thus,

 | n 22 = n ⋅ k 2 ⋅ ( k − 2) ​ ( k − 4) 2 ⋅ 2 ​ ( k − 5) = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 5). n_{22}=n\cdot\frac{k}{2}\cdot\frac{(k-2)(k-4)}{2}\cdot 2(k-5)=\frac{1}{2}nk(k-2)(k-4)(k-5). |  |

For n 23 n_{23}, choose a triangle. To two of its vertices add their neighbors, one to each, there will be ( k − 2) ​ ( k − 3) (k-2)(k-3) possibilities to do it. Now to one of them add a vertex that would be at distance two from all the vertices of the triangle - in k − 4 k-4 ways. We have,

 | p 3 ⋅ 3 ​ ( k − 2) ​ ( k − 3) ⋅ 2 ​ ( k − 4) = n 23 + 2 ​ n 8. p_{3}\cdot 3(k-2)(k-3)\cdot 2(k-4)=n_{23}+2n_{8}. |  |

Thus,

 | n 23 = n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 5) + 4 ​ n 3. n_{23}=nk(k-2)(k-4)(k-5)+4n_{3}. |  |

For n 24 n_{24} choose an edge. From one side attach a triangle to it in k / 2 − 1 k/2-1 ways, to the other side two leaves. Thus we have,

 | | E ⁡ ( G) | ⋅ 2 ​ ( k 2 − 1) ​ ( k − 2) ​ ( k − 4) 2 = n 24 + n 18 + n 4. |E(G)|\cdot 2(\frac{k}{2}-1)\frac{(k-2)(k-4)}{2}=n_{24}+n_{18}+n_{4}. |  |

Or

 | n 24 = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) + 2 ​ n 3. n_{24}=\frac{1}{4}nk(k-2)(k-4)(k-6)+2n_{3}. |  |

For n 25 n_{25}, we start again the construction from the vertex of highest degree of the subgraph. Attach a triangle and a leaf to it. Extend the leaf further by adding to it one of the k − 4 k-4 neighbors that are not adjacent to any other vertices. To the last vertex we will add another its neighbor such that it is still at distance two from the original vertex as well as from the first added leaf - ( k − 3) (k-3) ways. We have

 | n ⋅ k 2 ​ ( k − 2) ​ ( k − 4) ​ ( k − 3) = n 25 + 2 ​ n 8. n\cdot\frac{k}{2}(k-2)(k-4)(k-3)=n_{25}+2n_{8}. |  |

So,

 | n 25 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 7) + 4 ​ n 3. n_{25}=\frac{1}{2}nk(k-2)(k-4)(k-7)+4n_{3}. |  |

For n 26 n_{26}, choose a quadrilateral. On one of its vertices attach two leaves. We have,

 | n 26 = p 4 ⋅ 4 ⋅ ( k − 4) ​ ( k − 6) 2 = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6). n_{26}=p_{4}\cdot 4\cdot\frac{(k-4)(k-6)}{2}=\frac{1}{4}nk(k-2)(k-4)(k-6). |  |

For n 27 n_{27}, choose a quadrilateral, attach two leaves to the neighboring two vertices of it. We have

 | p 4 ⋅ 4 ​ ( k − 4) 2 = n 27 + 2 ​ n 9. p_{4}\cdot 4(k-4)^{2}=n_{27}+2n_{9}. |  |

So,

 | n 27 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 5) + 2 ​ n 3. n_{27}=\frac{1}{2}nk(k-2)(k-4)(k-5)+2n_{3}. |  |

For n 28 n_{28}, choose a quadrilateral. Attach two leaves on its opposite sides. We have

 | p 4 ⋅ 2 ​ ( k − 4) 2 = n 28 + n 10. p_{4}\cdot 2(k-4)^{2}=n_{28}+n_{10}. |  |

. Then

 | n 28 = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) + 2 ​ n 3. n_{28}=\frac{1}{4}nk(k-2)(k-4)(k-6)+2n_{3}. |  |

For n 29 n_{29}, choose a pentagon from G G. To one of its vertices attach a leaf, which might turn out to be not a leaf but just make sure to not choose a common neighbor with one of its immediate neighbors. We have

 | p 5 ⋅ 5 ​ ( k − 4) = n 29 + 4 ​ n 10 + n 4. p_{5}\cdot 5(k-4)=n_{29}+4n_{10}+n_{4}. |  |

And thus,

 | n 29 = n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) + 6 ​ n 3. n_{29}=nk(k-2)(k-4)(k-6)+6n_{3}. |  |

For n 30 n_{30}, start from the vertex of highest degree of the subgraph, to which choose five mutually non adjacent its neighbors. Thus,

 | n 30 = n ⋅ 1 5! ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ​ ( k − 8) = 1 120 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ​ ( k − 8). n_{30}=n\cdot\frac{1}{5!}k(k-2)(k-4)(k-6)(k-8)=\frac{1}{120}nk(k-2)(k-4)(k-6)(k-8). |  |

For n 31 n_{31}, start from the vertex of highest degree of the subgraph; add four leaves, to one of which add one more vertex in k − 5 k-5 ways. Thus,

 | n 31 = n ⋅ 1 4! ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ⋅ 4 ​ ( k − 5) = 1 6 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 5) ​ ( k − 6). n_{31}=n\cdot\frac{1}{4!}k(k-2)(k-4)(k-6)\cdot 4(k-5)=\frac{1}{6}nk(k-2)(k-4)(k-5)(k-6). |  |

For n 32 n_{32}, choose an edge; to each of its vertices add two non adjacent vertices. We get

 | | E ⁡ ( G) | ⋅ ( ( k − 2) ​ ( k − 4) 2) 2 = n 32 + n 27 + n 9. |E(G)|\cdot(\frac{(k-2)(k-4)}{2})^{2}=n_{32}+n_{27}+n_{9}. |  |

After some calculations,

 | n 32 = 1 8 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 10 ​ k + 26) − n 3. n_{32}=\frac{1}{8}nk(k-2)(k-4)(k^{2}-10k+26)-n_{3}. |  |

For n 33 n_{33}, choose a vertex of degree three of the subgraph; as a starting point from that vertex we can rebuild the rest of the graph. We have,

 | n ⋅ k ​ ( k − 2) ​ ( k − 4) 6 ⋅ 3 ​ ( k − 4) 2 = n 33 + n 29. n\cdot\frac{k(k-2)(k-4)}{6}\cdot 3(k-4)^{2}=n_{33}+n_{29}. |  |

So

 | n 33 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 10 ​ k + 28) − 6 ​ n 3. n_{33}=\frac{1}{2}nk(k-2)(k-4)(k^{2}-10k+28)-6n_{3}. |  |

For n 34 n_{34}, similarly to the previous case, we will start the construction from the vertex of degree three and proceed adding vertices. We have,

 | n ⋅ k ​ ( k − 2) ​ ( k − 4) 6 ⋅ 3 ​ ( k − 4) ⋅ ( k − 3) = n 34 + 2 ​ n 29 + 2 ​ n 10. n\cdot\frac{k(k-2)(k-4)}{6}\cdot 3(k-4)\cdot(k-3)=n_{34}+2n_{29}+2n_{10}. |  |

 | n 34 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 11 ​ k + 34) − 8 ​ n 3. n_{34}=\frac{1}{2}nk(k-2)(k-4)(k^{2}-11k+34)-8n_{3}. |  |

For n 35 n_{35}, choose P 5 P_{5} from G G in m 13 m_{13} ways. Add a vertex to one of its end vertices such that the new vertex will not be connected to any of the two preceding vertices in exactly k − 3 k-3 ways. Thus,

 | m 13 ⋅ 2 ​ ( k − 3) = 2 ​ n 35 + 2 ​ n 29 + 12 ​ n 12 + 2 ​ n 8. m_{13}\cdot 2(k-3)=2n_{35}+2n_{29}+12n_{12}+2n_{8}. |  |

And

 | n 35 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 11 ​ k + 36) − 10 ​ n 3. n_{35}=\frac{1}{2}nk(k-2)(k-4)(k^{2}-11k+36)-10n_{3}. |  |

Due to not the best choice of numeration of subgrpaphs, further calculations cannot be carried out in linear fashion as the calculation of n 36 n_{36} requires the knowledge of the values that come after it. Here we have to skip to n 44 n_{44}.

For n 44 n_{44}, reconstruction of the subgraph follows straight forward pattern working out from the vertex of highest degree and further. We have,

 | n 44 = n ⋅ 1 4! ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ⋅ ( n − k − 1 − 6 − 4 ​ ( k − 5)) = 1 24 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ​ ( n − 5 ​ k + 13). n_{44}=n\cdot\frac{1}{4!}k(k-2)(k-4)(k-6)\cdot(n-k-1-6-4(k-5))=\frac{1}{24}nk(k-2)(k-4)(k-6)(n-5k+13). |  |

For n 45 n_{45}, we choose a quadrilateral of G G, then choose a pair of vertices that are not adjacent to any vertices of the quadrilateral. This pair can be mutually adjacent, thus giving us

 | p 4 ⋅ ( n − 8 − 4 ​ ( k − 4) 2) = n 45 + n 13. p_{4}\cdot{n-8-4(k-4)\choose 2}=n_{45}+n_{13}. |  |

So,

 | n 45 = 1 64 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ​ ( k 2 − 8 ​ k + 26) + n 3. n_{45}=\frac{1}{64}nk(k-2)(k-4)(k-6)(k^{2}-8k+26)+n_{3}. |  |

For n 46 n_{46}, start the construction from the vertex of degree three of the subgraph. Choose three mutually non adjacent vertices, one of which continue further. Finally, we need to choose the last vertex our of the ones located at distance two from the first vertex such that it is still non adjacent to two other leaves. Then we have

 | n ⋅ k ​ ( k − 2) ​ ( k − 4) 6 ⋅ 3 ​ ( k − 4) ⋅ ( n − k − 4 − 3 ​ ( k − 4)) = n 46 + n 34. n\cdot\frac{k(k-2)(k-4)}{6}\cdot 3(k-4)\cdot(n-k-4-3(k-4))=n_{46}+n_{34}. |  |

 | n 46 = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 14 ​ k 2 + 72 ​ k − 140) + 8 ​ n 3. n_{46}=\frac{1}{4}nk(k-2)(k-4)(k^{3}-14k^{2}+72k-140)+8n_{3}. |  |

Once more we need to fast forward to n 60 n_{60} before we find n 47 n_{47}.

For n 60 n_{60}, choose a triangle K 3 K_{3} in p 3 p_{3} ways. Denote N ⁡ ( K 3) N(K_{3}) a set of vertices in G G at distance one from a vertex in K 3 K_{3}, and W ⁡ ( K 3) W(K_{3}) - at distance two from all vertices of K 3 K_{3}. In order to built a bigger component of the subgraph we can add one of the vertices from N ⁡ ( K 3) N(K_{3}) in 3 ​ ( k − 2) 3(k-2). Now choose a vertex from W ⁡ ( K 3) W(K_{3}) such that it is not adjacent to the previously chosen vertex. This vertex is adjacent to exactly six vertices from N ⁡ ( K 3) N(K_{3}). Complete the construction choosing the neighboring vertex that is not one of those six. We have

 | p 3 ⋅ 3 ​ ( k − 2) ⋅ ( | W ⁡ ( K 3) | − ( k − 4)) ⋅ ( k − 6) = 2 ​ n 60 + n 25. p_{3}\cdot 3(k-2)\cdot(|W(K_{3})|-(k-4))\cdot(k-6)=2n_{60}+n_{25}. |  |

Or,

 | n 60 = 1 8 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 12 ​ k + 38) − 2 ​ n 3. n_{60}=\frac{1}{8}nk(k-2)(k-4)(k^{2}-12k+38)-2n_{3}. |  |

For n 47 n_{47}, similar to n 60 n_{60}, we will choose the connected component first and then two non adjacent to that component vertices. We have

 | n ⋅ k / 2 ⋅ ( k − 2) ​ ( n − k − 1 − 2 ​ ( k − 2) − ( k − 4) 2) = n 47 + n 60. n\cdot k/2\cdot(k-2){n-k-1-2(k-2)-(k-4)\choose 2}=n_{47}+n_{60}. |  |

Or

 | n 47 = 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ​ ( k 2 − 8 ​ k + 22) + 2 ​ n 3. n_{47}=\frac{1}{16}nk(k-2)(k-4)(k-6)(k^{2}-8k+22)+2n_{3}. |  |

For n 48 n_{48}, first of all we will show that any P 3 P_{3} from G G can be completed to a pentagon in exactly 2 ​ ( k − 4) 2(k-4) ways.

###### Proposition 2.

A path P 3 P_{3} in G G can be completed to exactly 2 ​ ( k − 4) 2(k-4) pentagons in G G.

###### Proof.

In order to show that notice that each pentagon contains exactly 5 paths P 3 P_{3}. So the average number of pentagons that a given P 3 P_{3} belongs to is 5 ​ p 5 5p_{5} divided to the number of all P 3 P_{3} -s in G G and that is

 | 5 ⋅ 1 5 ​ n ​ k ​ ( k − 2) ​ ( k − 4) / 1 2 ​ n ​ k ​ ( k − 2) = 2 ​ ( k − 4). 5\cdot\frac{1}{5}nk(k-2)(k-4)/\frac{1}{2}nk(k-2)=2(k-4). |  |

That means we just need to prove that this is a maximal number of possible pentagons for a given P 3 P_{3}. Assume a path given v 1 ​ v 0 ​ v 2 v_{1}v_{0}v_{2}. Denote w w another common neighbor to v 1 v_{1} and v 2 v_{2} along with v 0 v_{0}, and z z a vertex that completes a triangle on edge v 0 ​ v 2 v_{0}v_{2}. Now there are exactly k − 3 k-3 neighbors of v 1 v_{1} to which we can continue our path without being connected to v 0 v_{0} or v 2 v_{2}. From those k − 3 k-3 vertices there are at most 2 ​ ( k − 3) − 2 = 2 ​ ( k − 4) 2(k-3)-2=2(k-4) paths of length two to the vertex v 2 v_{2} that can complete to a pentagon. We subtract two as we have exactly one path that goes through vertex w w and one through z z. The statement is proven. ∎

Now we proceed with a construction of subgraphs N 48 N_{48}. Choose a middle vertex of P 5 P_{5} and recover the entire paths, by doing that we will use the previous proposition. The last, possibly isolated, vertex we will choose such that it can only be adjacent to end points of the constructed path in n − 3 ​ k + 4 n-3k+4 ways. Thus,

 | n ⋅ k ⁡ ( k − 2) 2 ⋅ ( ( k − 3) 2) − 2 ​ ( k − 4) ⋅ ( n − 3 ​ k + 4) = n 48 + 2 ​ n 35 + 6 ​ n 12. n\cdot\frac{k(k-2)}{2}\cdot((k-3)^{2})-2(k-4)\cdot(n-3k+4)=n_{48}+2n_{35}+6n_{12}. |  |

And

 | n 48 = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 14 ​ k 2 + 75 ​ k − 160) + 14 ​ n 3. n_{48}=\frac{1}{4}nk(k-2)(k-4)(k^{3}-14k^{2}+75k-160)+14n_{3}. |  |

For n 62 n_{62}, choose a triangle. Similarly, denote W W the set of all vertices of G G that are at distance two from the three vertices of the triangle. Notice that G ⁡ [W] G[W] is regular of degree k − 6 k-6 and | W | = n − 3 − 3 ​ ( k − 2) |W|=n-3-3(k-2). Now choose a vertex from W W and two its neighbors also from W W. We have

 | p 3 ⋅ | W | ​ ( k − 6 2) = n 62 + 6 ​ n 14. p_{3}\cdot|W|{k-6\choose 2}=n_{62}+6n_{14}. |  |

Or

 | n 62 = 1 24 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 14 ​ k + 54) − 2 ​ n 3. n_{62}=\frac{1}{24}nk(k-2)(k-4)(k^{2}-14k+54)-2n_{3}. |  |

For n 49 n_{49}, we will make similar construction like for n 62 n_{62} starting with a triangle, but this time we choose first an edge from W W in | W | ​ ( k − 6) 2 \frac{|W|(k-6)}{2} ways, and the last vertex also from W W in | W | − 2 |W|-2 ways. We have

 | p 3 ⋅ | W | ​ ( k − 6) 2 ⋅ ( | W | − 2) = n 49 + 2 ​ n 62 + 6 ​ n 14. p_{3}\cdot\frac{|W|(k-6)}{2}\cdot(|W|-2)=n_{49}+2n_{62}+6n_{14}. |  |

So

 | n 49 = 1 48 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 16 ​ k 2 + 94 ​ k − 216) + 2 ​ n 3, n_{49}=\frac{1}{48}nk(k-2)(k-4)(k^{3}-16k^{2}+94k-216)+2n_{3}, |  |

For n 50 n_{50}, we will start the construction from the vertex of degree three of the subgraph. The last vertex, possibly isolated, we choose at distance two from the first vertex such that it is also not adjacent to three other vertices at distance one from the starting vertex. Thus, we have

 | n ⋅ 1 6 ​ k ​ ( k − 2) ​ ( k − 4) ⋅ 3 ​ ( n − k − 1 − 2 ​ ( k − 3) − 1 − ( k − 4)) = n 50 + 2 ​ n 28. n\cdot\frac{1}{6}k(k-2)(k-4)\cdot 3(n-k-1-2(k-3)-1-(k-4))=n_{50}+2n_{28}. |  |

And

 | n 50 = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 10 ​ k + 30) − 4 ​ n 3, n_{50}=\frac{1}{4}nk(k-2)(k-4)(k^{2}-10k+30)-4n_{3}, |  |

For n 51 n_{51}, choose a triangle, to two of its vertices attach two vertices such that they are not adjacent, ( k − 2) ​ ( k − 3) (k-2)(k-3) ways. The final, possibly isolated, vertex of the subgraph can be chosen from W W. We have

 | n ​ k 6 ⋅ 3 ​ ( k − 2) ​ ( k − 3) ⋅ 1 2 ​ ( k − 2) ​ ( k − 4) = n 51 + n 23 + n 8. \frac{nk}{6}\cdot 3(k-2)(k-3)\cdot\frac{1}{2}(k-2)(k-4)=n_{51}+n_{23}+n_{8}. |  |

Or

 | n 51 = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 9 ​ k + 22) − 2 ​ n 3. n_{51}=\frac{1}{4}nk(k-2)(k-4)(k^{2}-9k+22)-2n_{3}. |  |

Here, for n 52 n_{52}, we can find its exact value. Start the construction from the vertex of degree four, call it v 0 v_{0}. Choose a triangle, in k / 2 k/2 ways, and two leaves, in 1 2 ​ ( k − 2) ​ ( k − 4) \frac{1}{2}(k-2)(k-4) ways, attached to v 0 v_{0}. From the set of vertices at distance two from v 0 v_{0} we can choose the vertex that is not adjacent to any other already chosen vertices. Thus,

 | n 52 = n ⋅ k 2 ⋅ 1 2 ​ ( k − 2) ​ ( k − 4) ​ ( n − k − 1 − 2 ​ ( k − 2) − 2 ​ ( k − 5) − 1) = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( n − 5 ​ k + 12). n_{52}=n\cdot\frac{k}{2}\cdot\frac{1}{2}(k-2)(k-4)(n-k-1-2(k-2)-2(k-5)-1)=\frac{1}{4}nk(k-2)(k-4)(n-5k+12). |  |

For n 53 n_{53}, choose a pentagon. Notice that all five vertices of the triangles based on the sides of this pentagon are distinct. Then we can choose for the last vertex of the subgraph one of the n − 10 n-10 remaining vertices. We can get

 | p 5 ⋅ ( n − 10) = n 53 + 2 ​ n 10 + n 29. p_{5}\cdot(n-10)=n_{53}+2n_{10}+n_{29}. |  |

So

 | n 53 = 1 5 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( n − 5 ​ k + 15) − 2 ​ n 3. n_{53}=\frac{1}{5}nk(k-2)(k-4)(n-5k+15)-2n_{3}. |  |

For n 54 n_{54}, start from the vertex of degree four, v 0 v_{0}; choose two adjacent to it triangles. From the set of vertices at distance two from v 0 v_{0} choose the last vertex non adjacent to any other previously chosen vertices. We have

 | n 54 = n ⋅ ( k / 2 2) ⋅ ( n − k − 1 − 2 ​ ( k − 2) − 2 ​ ( k − 4)). n_{54}=n\cdot{k/2\choose 2}\cdot(n-k-1-2(k-2)-2(k-4)). |  |

Or

 | n 54 = 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6). n_{54}=\frac{1}{16}nk(k-2)(k-4)(k-6). |  |

For n 55 n_{55}, choose a quadrilateral, recover a triangle at one of its sides. The last vertex choose such that it is not adjacent to any vertices of the quadrilateral. Thus we have

 | p 4 ⋅ 4 ​ ( n − 8 − 4 ​ ( k − 4)) = n 55 + n 6. p_{4}\cdot 4(n-8-4(k-4))=n_{55}+n_{6}. |  |

And

 | n 55 = 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) + 2 ​ n 3. n_{55}=\frac{1}{4}nk(k-2)(k-4)(k-6)+2n_{3}. |  |

For n 56 n_{56}, start the construction from the vertex of degree three, call it v 0 v_{0}. Choose a triangle and a leaf attached to v 0 v_{0}. Continue the leaf further attaching another vertex to it. The sixth vertex we choose from the set of vertices at distance two from v 0 v_{0} with extra requirements of not being adjacent to any of the chosen vertices except the very last one. Then we have

 | n ⋅ k 2 ⋅ ( k − 2) ​ ( k − 4) ​ ( n − k − 2 − 2 ​ ( k − 2) − ( k − 4)) = n 56 + n 25. n\cdot\frac{k}{2}\cdot(k-2)(k-4)(n-k-2-2(k-2)-(k-4))=n_{56}+n_{25}. |  |

Or

 | n 56 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( n − 5 ​ k + 14) − 4 ​ n 3. n_{56}=\frac{1}{2}nk(k-2)(k-4)(n-5k+14)-4n_{3}. |  |

Once more, we need the value of n 58 n_{58} before looking for n 57 n_{57}. For that notice that we have a relation

 | m 6 ⋅ 2 ​ ( k − 3) = 2 ​ n 58 + 2 ​ n 35 + n 25. m_{6}\cdot 2(k-3)=2n_{58}+2n_{35}+n_{25}. |  |

This is due to the fact that in five-vertex subgraph M 6 M_{6} we can prolong its component P 3 P_{3} path to P 4 P_{4} by adding to either of its sides a vertex in k − 3 k-3 ways. Thus,

 | n 58 = 1 8 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 15 ​ k 2 + 86 ​ k − 190) + 8 ​ n 3. n_{58}=\frac{1}{8}nk(k-2)(k-4)(k^{3}-15k^{2}+86k-190)+8n_{3}. |  |

Now for n 57 n_{57}, start the construction from choosing an isolated edge, in | E ⁡ ( G) | |E(G)| ways. Next choose a pair of vertices from those what are not incident to the chosen one. There will be exactly | E ⁡ ( G) | − 3 − 7 ​ ( k − 2) − 2 ​ ( k − 2) ​ ( k − 4) |E(G)|-3-7(k-2)-2(k-2)(k-4) edges to choose the pair from. Notice that by this construction we might end up with a five-vertex subgraph. Thus

 | | E ⁡ ( G) | ​ ( | E ⁡ ( G) | − 3 − 7 ​ ( k − 2) − 2 ​ ( k − 2) ​ ( k − 4) 2) = 3 ​ m 14 + m 6 + n 60 + 2 ​ n 13 + n 58 + 3 ​ n 57. |E(G)|{|E(G)|-3-7(k-2)-2(k-2)(k-4)\choose 2}=3m_{14}+m_{6}+n_{60}+2n_{13}+n_{58}+3n_{57}. |  |

And

 | n 57 = n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 4 − 18 ​ k 3 + 140 ​ k 2 − 564 ​ k + 996) / 192 − 4 3 ​ n 3. n_{57}=nk(k-2)(k-4)(k^{4}-18k^{3}+140k^{2}-564k+996)/192-\frac{4}{3}n_{3}. |  |

For n 59 n_{59}, start the construction from the vertex of degree three, v 0 v_{0}. Choose three other vertices from its neighborhood. Lastly, choose an edge from the set of vertices at distance two from v 0 v_{0} such that it is not a base for any triangle on previously chosen vertices. We get

 | n ⋅ 1 6 ​ k ​ ( k − 2) ​ ( k − 4) ⋅ ( | E ⁡ ( G) | − 3 2 ​ k − k ⁡ ( k − 2) − 3 ​ ( k 2 − 1)) = n 59 + n 34 + n 29 + 2 ​ n 28 + 2 ​ n 10. n\cdot\frac{1}{6}k(k-2)(k-4)\cdot(|E(G)|-\frac{3}{2}k-k(k-2)-3(\frac{k}{2}-1))=n_{59}+n_{34}+n_{29}+2n_{28}+2n_{10}. |  |

Or

 | n 59 = 1 24 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ​ ( k 2 − 10 ​ k + 34) + 2 ​ n 3. n_{59}=\frac{1}{24}nk(k-2)(k-4)(k-6)(k^{2}-10k+34)+2n_{3}. |  |

For n 61 n_{61}, consider five-vertex subgraph M 3 M_{3}. Notice that two isolated vertices should have exactly two common neighbors due to the topology of the graph. Then

 | 2 ​ m 3 = 2 ​ n 61 + 2 ​ n 32 + n 34 + n 20 + n 26. 2m_{3}=2n_{61}+2n_{32}+n_{34}+n_{20}+n_{26}. |  |

From which

 | n 61 = 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 16 ​ k 2 + 96 ​ k − 220) + 5 ​ n 3. n_{61}=\frac{1}{16}nk(k-2)(k-4)(k^{3}-16k^{2}+96k-220)+5n_{3}. |  |

The rest of the values n 36 − n 43 n_{36}-n_{43} can be found from the equations directly. But we will stick to constructions wherever it is possible so we can use the equations as the way of check. It will also decrease the calculations tremendously. Again we have to go from top to bottom.

For n 43 n_{43}, choose a triangle. From the set W W of vertices at distance two from all the vertices of the triangle, choose three vertices. We have

 | p 3 ​ ( W 3) = n 43 + n 62 + n 49 + 2 ​ n 14. p_{3}{W\choose 3}=n_{43}+n_{62}+n_{49}+2n_{14}. |  |

And

 | n 43 = 1 288 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 4 − 18 ​ k 3 + 130 ​ k 2 − 460 ​ k + 720) − 2 3 ​ n 3. n_{43}=\frac{1}{288}nk(k-2)(k-4)(k^{4}-18k^{3}+130k^{2}-460k+720)-\frac{2}{3}n_{3}. |  |

For n 42 n_{42}, consider five-vertex subgrpaph M 3 M_{3}. The component P 3 P_{3} in it we can continue in k − 3 k-3 was in either direction. By that we have

 | m 3 ⋅ 2 ​ ( k − 3) = 2 ​ n 42 + 2 ​ n 48 + n 34. m_{3}\cdot 2(k-3)=2n_{42}+2n_{48}+n_{34}. |  |

Thus

 | n 42 = 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 4 − 17 ​ k 3 + 120 ​ k 2 − 430 ​ k + 684) − 10 ​ n 3. n_{42}=\frac{1}{16}nk(k-2)(k-4)(k^{4}-17k^{3}+120k^{2}-430k+684)-10n_{3}. |  |

For n 41 n_{41}, consider again M 3 M_{3}. Two isolated vertices of the subgraph has exactly two common neighbors so there exactly 2 ​ ( k − 2) 2(k-2) vertices that are neighbors to only one of them. Thus, we obtain a relationship

 | m 3 ⋅ 2 ​ ( k − 2) = 2 ​ n 41 + 2 ​ n 48 + n 46 + 2 ​ n 51 + n 50. m_{3}\cdot 2(k-2)=2n_{41}+2n_{48}+n_{46}+2n_{51}+n_{50}. |  |

Or

 | n 41 = 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 4 − 18 ​ k 3 + 136 ​ k 2 − 524 ​ k + 892) − 14 ​ n 3. n_{41}=\frac{1}{16}nk(k-2)(k-4)(k^{4}-18k^{3}+136k^{2}-524k+892)-14n_{3}. |  |

For n 40 n_{40}, we start the construction from the vertex v 0 v_{0} of degree three. Then choose three mutually non-adjacent its neighbors. Lastly, choose the pair of vertices from the set of vertices at distance two from v 0 v_{0} such that none is adjacent to any previously chosen vertices. We have

 | n ⋅ k ​ ( k − 2) ​ ( k − 4) 6 ⋅ ( n − k − 1 − 3 − 3 ​ ( k − 4) 2) = n 40 + n 54. n\cdot\frac{k(k-2)(k-4)}{6}\cdot{n-k-1-3-3(k-4)\choose 2}=n_{40}+n_{54}. |  |

Or

 | n 40 = 1 48 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 4 − 18 ​ k 3 + 130 ​ k 2 − 460 ​ k + 696) − 2 ​ n 3. n_{40}=\frac{1}{48}nk(k-2)(k-4)(k^{4}-18k^{3}+130k^{2}-460k+696)-2n_{3}. |  |

For n 39 n_{39}, consider five-vertex subgraph M 4 M_{4}. There are exactly n − k − 5 n-k-5 vertices of the graph G G excluding the ones that are already in M 4 M_{4} that are not adjacent to the only isolated vertex of the subgraph. Thus we have

 | m 4 ⋅ ( n − k − 5) = n 54 + n 56 + 3 ​ n 49 + n 48 + 2 ​ n 41 + 2 ​ n 39. m_{4}\cdot(n-k-5)=n_{54}+n_{56}+3n_{49}+n_{48}+2n_{41}+2n_{39}. |  |

Or

 | n 39 = 1 128 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 5 − 20 ​ k 4 + 176 ​ k 3 − 884 ​ k 2 + 2588 ​ k − 3624) + 6 ​ n 3. n_{39}=\frac{1}{128}nk(k-2)(k-4)(k^{5}-20k^{4}+176k^{3}-884k^{2}+2588k-3624)+6n_{3}. |  |

For n 38 n_{38}, we start the construction from the vertex v 0 v_{0} of degree two, then choose its two neighbors. We have obtained P 3 P_{3}. Lastly, we choose three vertices from the set of all vertices of G G that are not adjacent to any of the vertices of P 3 P_{3}. We have

 | n ⋅ k ⁡ ( k − 2) 2 ⋅ ( n − 3 ​ k + 4 3) = n 38 + n 41 + 2 ​ n 61 + n 62. n\cdot\frac{k(k-2)}{2}\cdot{n-3k+4\choose 3}=n_{38}+n_{41}+2n_{61}+n_{62}. |  |

Or

 | n 38 = 1 96 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 5 − 20 ​ k 4 + 172 ​ k 3 − 828 ​ k 2 + 2300 ​ k − 3048) + 6 ​ n 3. n_{38}=\frac{1}{96}nk(k-2)(k-4)(k^{5}-20k^{4}+172k^{3}-828k^{2}+2300k-3048)+6n_{3}. |  |

For n 37 n_{37}, consider five-vertex subgraph M 1 M_{1}. To one of its five isolated vertices add its neighboring vertex. We have

 | m 1 ⋅ 5 ​ k = 2 ​ n 37 + 2 ​ n 38 + 3 ​ n 40 + 4 ​ n 44 + 5 ​ n 30. m_{1}\cdot 5k=2n_{37}+2n_{38}+3n_{40}+4n_{44}+5n_{30}. |  |

And

 | n 37 = 1 768 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 6 − 22 ​ k 5 + 212 ​ k 4 − 1208 ​ k 3 + 4484 ​ k 2 − 10456 ​ k + 12288) − 3 ​ n 3. n_{37}=\frac{1}{768}nk(k-2)(k-4)(k^{6}-22k^{5}+212k^{4}-1208k^{3}+4484k^{2}-10456k+12288)-3n_{3}. |  |

And finally, for n 36 n_{36} we use the equation

 | m 1 ​ ( n − 5) = n 30 + 6 ​ n 36 + 2 ​ n 37 + n 38 + n 40 + n 44. m_{1}(n-5)=n_{30}+6n_{36}+2n_{37}+n_{38}+n_{40}+n_{44}. |  |

So

 | n 36 = 1 23040 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 7 − 24 ​ k 6 + 248 ​ k 5 − 1520 ​ k 4 + 6436 ​ k 3 − 19520 ​ k 2 + 38896 ​ k − 40704) + 1 3 ​ n 3. n_{36}=\frac{1}{23040}nk(k-2)(k-4)(k^{7}-24k^{6}+248k^{5}-1520k^{4}+6436k^{3}-19520k^{2}+38896k-40704)+\frac{1}{3}n_{3}. |  |

Thus we have obtained all the formulas for the number of subgraphs of order six in G G. Below is the summary of all our calculations of n i n_{i} -s.

 | n 1 = \displaystyle n_{1}= | 1 12 ​ n ​ k ​ ( k − 2) − n 3 3, \displaystyle\frac{1}{12}nk(k-2)-\frac{n_{3}}{3}, |  |

 | n 2 = \displaystyle n_{2}= | 1 2 ​ n ​ k ​ ( k − 2), \displaystyle\frac{1}{2}nk(k-2), |  |

 | n 3 = \displaystyle n_{3}= | n 3, \displaystyle n_{3}, |  |

 | n 4 = \displaystyle n_{4}= | 2 ​ n 3, \displaystyle 2n_{3}, |  |

 | n 5 = \displaystyle n_{5}= | 1 8 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − n 3, \displaystyle\frac{1}{8}nk(k-2)(k-4)-n_{3}, |  |

 | n 6 = \displaystyle n_{6}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 3) − 2 ​ n 3, \displaystyle\frac{1}{2}nk(k-2)(k-3)-2n_{3}, |  |

 | n 7 = \displaystyle n_{7}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4), \displaystyle\frac{1}{4}nk(k-2)(k-4), |  |

 | n 8 = \displaystyle n_{8}= | n ​ k ​ ( k − 2) ​ ( k − 4) − 2 ​ n 3, \displaystyle nk(k-2)(k-4)-2n_{3}, |  |

 | n 9 = \displaystyle n_{9}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − n 3, \displaystyle\frac{1}{4}nk(k-2)(k-4)-n_{3}, |  |

 | n 10 = \displaystyle n_{10}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − 2 ​ n 3, \displaystyle\frac{1}{2}nk(k-2)(k-4)-2n_{3}, |  |

 | n 11 = \displaystyle n_{11}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) + 4 ​ n 3, \displaystyle\frac{1}{2}nk(k-2)(k-4)(k-6)+4n_{3}, |  |

 | n 12 = \displaystyle n_{12}= | 1 12 ​ n ​ k ​ ( k − 2) ​ ( 2 ​ k 2 − 21 ​ k + 53) + n 3, \displaystyle\frac{1}{12}nk(k-2)(2k^{2}-21k+53)+n_{3}, |  |

 | n 13 = \displaystyle n_{13}= | 1 32 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 12 ​ k + 42) − n 3, \displaystyle\frac{1}{32}nk(k-2)(k-4)(k^{2}-12k+42)-n_{3}, |  |

 | n 14 = \displaystyle n_{14}= | 1 144 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 12) + n 3 3, \displaystyle\frac{1}{144}nk(k-2)(k-4)(k-12)+\frac{n_{3}}{3}, |  |

 | n 15 = \displaystyle n_{15}= | 1 8 ​ n ​ k ​ ( k − 2) ​ ( k − 4), \displaystyle\frac{1}{8}nk(k-2)(k-4), |  |

 | n 16 = \displaystyle n_{16}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4), \displaystyle\frac{1}{2}nk(k-2)(k-4), |  |

 | n 17 = \displaystyle n_{17}= | n ​ k ​ ( k − 2) ​ ( k − 4), \displaystyle nk(k-2)(k-4), |  |

 | n 18 = \displaystyle n_{18}= | n ​ k ​ ( k − 2) ​ ( k − 4) − 4 ​ n 3, \displaystyle nk(k-2)(k-4)-4n_{3}, |  |

 | n 19 = \displaystyle n_{19}= | 1 12 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6), \displaystyle\frac{1}{12}nk(k-2)(k-4)(k-6), |  |

 | n 20 = \displaystyle n_{20}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) 2, \displaystyle\frac{1}{2}nk(k-2)(k-4)^{2}, |  |

 | n 21 = \displaystyle n_{21}= | 1 6 ​ n ​ k ​ ( k − 2) ​ ( k − 3) ​ ( k − 4) + 2 ​ n 3 3, \displaystyle\frac{1}{6}nk(k-2)(k-3)(k-4)+\frac{2n_{3}}{3}, |  |

 | n 22 = \displaystyle n_{22}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 5), \displaystyle\frac{1}{2}nk(k-2)(k-4)(k-5), |  |

 | n 23 = \displaystyle n_{23}= | n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 5) + 4 ​ n 3, \displaystyle nk(k-2)(k-4)(k-5)+4n_{3}, |  |

 | n 24 = \displaystyle n_{24}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) + 2 ​ n 3, \displaystyle\frac{1}{4}nk(k-2)(k-4)(k-6)+2n_{3}, |  |

 | n 25 = \displaystyle n_{25}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 7) + 4 ​ n 3, \displaystyle\frac{1}{2}nk(k-2)(k-4)(k-7)+4n_{3}, |  |

 | n 26 = \displaystyle n_{26}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6), \displaystyle\frac{1}{4}nk(k-2)(k-4)(k-6), |  |

 | n 27 = \displaystyle n_{27}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 5) + 2 ​ n 3, \displaystyle\frac{1}{2}nk(k-2)(k-4)(k-5)+2n_{3}, |  |

 | n 28 = \displaystyle n_{28}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) + 2 ​ n 3, \displaystyle\frac{1}{4}nk(k-2)(k-4)(k-6)+2n_{3}, |  |

 | n 29 = \displaystyle n_{29}= | n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) + 6 ​ n 3, \displaystyle nk(k-2)(k-4)(k-6)+6n_{3}, |  |

 | n 30 = \displaystyle n_{30}= | 1 120 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ​ ( k − 8), \displaystyle\frac{1}{120}nk(k-2)(k-4)(k-6)(k-8), |  |

 | n 31 = \displaystyle n_{31}= | 1 6 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 5) ​ ( k − 6), \displaystyle\frac{1}{6}nk(k-2)(k-4)(k-5)(k-6), |  |

 | n 32 = \displaystyle n_{32}= | 1 8 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 10 ​ k + 26) − n 3, \displaystyle\frac{1}{8}nk(k-2)(k-4)(k^{2}-10k+26)-n_{3}, |  |

 | n 33 = \displaystyle n_{33}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 10 ​ k + 28) − 6 ​ n 3, \displaystyle\frac{1}{2}nk(k-2)(k-4)(k^{2}-10k+28)-6n_{3}, |  |

 | n 34 = \displaystyle n_{34}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 11 ​ k + 34) − 8 ​ n 3, \displaystyle\frac{1}{2}nk(k-2)(k-4)(k^{2}-11k+34)-8n_{3}, |  |

 | n 35 = \displaystyle n_{35}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 11 ​ k + 36) − 10 ​ n 3, \displaystyle\frac{1}{2}nk(k-2)(k-4)(k^{2}-11k+36)-10n_{3}, |  |

 | n 36 = \displaystyle n_{36}= | 1 23040 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 7 − 24 ​ k 6 + 248 ​ k 5 − 1520 ​ k 4 + 6436 ​ k 3 − 19520 ​ k 2 CLOSE \displaystyle\frac{1}{23040}nk(k-2)(k-4)(k^{7}-24k^{6}+248k^{5}-1520k^{4}+6436k^{3}-19520k^{2} |  |

 |  | OPEN + 38896 ​ k − 40704) + 1 3 ​ n 3, \displaystyle+38896k-40704)+\frac{1}{3}n_{3}, |  |

 | n 37 = \displaystyle n_{37}= | 1 768 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 6 − 22 ​ k 5 + 212 ​ k 4 − 1208 ​ k 3 + 4484 ​ k 2 − 10456 ​ k + 12288) − 3 ​ n 3, \displaystyle\frac{1}{768}nk(k-2)(k-4)(k^{6}-22k^{5}+212k^{4}-1208k^{3}+4484k^{2}-10456k+12288)-3n_{3}, |  |

 | n 38 = \displaystyle n_{38}= | 1 96 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 5 − 20 ​ k 4 + 172 ​ k 3 − 828 ​ k 2 + 2300 ​ k − 3048) + 6 ​ n 3, \displaystyle\frac{1}{96}nk(k-2)(k-4)(k^{5}-20k^{4}+172k^{3}-828k^{2}+2300k-3048)+6n_{3}, |  |

 | n 39 = \displaystyle n_{39}= | 1 128 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 5 − 20 ​ k 4 + 176 ​ k 3 − 884 ​ k 2 + 2588 ​ k − 3624) + 6 ​ n 3, \displaystyle\frac{1}{128}nk(k-2)(k-4)(k^{5}-20k^{4}+176k^{3}-884k^{2}+2588k-3624)+6n_{3}, |  |

 | n 40 = \displaystyle n_{40}= | 1 48 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 4 − 18 ​ k 3 + 130 ​ k 2 − 460 ​ k + 696) − 2 ​ n 3, \displaystyle\frac{1}{48}nk(k-2)(k-4)(k^{4}-18k^{3}+130k^{2}-460k+696)-2n_{3}, |  |

 | n 41 = \displaystyle n_{41}= | 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 4 − 18 ​ k 3 + 136 ​ k 2 − 524 ​ k + 892) − 14 ​ n 3, \displaystyle\frac{1}{16}nk(k-2)(k-4)(k^{4}-18k^{3}+136k^{2}-524k+892)-14n_{3}, |  |

 | n 42 = \displaystyle n_{42}= | 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 4 − 17 ​ k 3 + 120 ​ k 2 − 430 ​ k + 684) − 10 ​ n 3, \displaystyle\frac{1}{16}nk(k-2)(k-4)(k^{4}-17k^{3}+120k^{2}-430k+684)-10n_{3}, |  |

 | n 43 = \displaystyle n_{43}= | 1 288 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 4 − 18 ​ k 3 + 130 ​ k 2 − 460 ​ k + 720) − 2 3 ​ n 3, \displaystyle\frac{1}{288}nk(k-2)(k-4)(k^{4}-18k^{3}+130k^{2}-460k+720)-\frac{2}{3}n_{3}, |  |

 | n 44 = \displaystyle n_{44}= | 1 24 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ​ ( n − 5 ​ k + 13), \displaystyle\frac{1}{24}nk(k-2)(k-4)(k-6)(n-5k+13), |  |

 | n 45 = \displaystyle n_{45}= | 1 64 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ​ ( k 2 − 8 ​ k + 26) + n 3, \displaystyle\frac{1}{64}nk(k-2)(k-4)(k-6)(k^{2}-8k+26)+n_{3}, |  |

 | n 46 = \displaystyle n_{46}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 14 ​ k 2 + 72 ​ k − 140) + 8 ​ n 3, \displaystyle\frac{1}{4}nk(k-2)(k-4)(k^{3}-14k^{2}+72k-140)+8n_{3}, |  |

 | n 47 = \displaystyle n_{47}= | 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ​ ( k 2 − 8 ​ k + 22) + 2 ​ n 3, \displaystyle\frac{1}{16}nk(k-2)(k-4)(k-6)(k^{2}-8k+22)+2n_{3}, |  |

 | n 48 = \displaystyle n_{48}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 14 ​ k 2 + 75 ​ k − 160) + 14 ​ n 3, \displaystyle\frac{1}{4}nk(k-2)(k-4)(k^{3}-14k^{2}+75k-160)+14n_{3}, |  |

 | n 49 = \displaystyle n_{49}= | 1 48 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 16 ​ k 2 + 94 ​ k − 216) + 2 ​ n 3, \displaystyle\frac{1}{48}nk(k-2)(k-4)(k^{3}-16k^{2}+94k-216)+2n_{3}, |  |

 | n 50 = \displaystyle n_{50}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 10 ​ k + 30) − 4 ​ n 3, \displaystyle\frac{1}{4}nk(k-2)(k-4)(k^{2}-10k+30)-4n_{3}, |  |

 | n 51 = \displaystyle n_{51}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 9 ​ k + 22) − 2 ​ n 3, \displaystyle\frac{1}{4}nk(k-2)(k-4)(k^{2}-9k+22)-2n_{3}, |  |

 | n 52 = \displaystyle n_{52}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( n − 5 ​ k + 12), \displaystyle\frac{1}{4}nk(k-2)(k-4)(n-5k+12), |  |

 | n 53 = \displaystyle n_{53}= | 1 5 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( n − 5 ​ k + 15) − 2 ​ n 3, \displaystyle\frac{1}{5}nk(k-2)(k-4)(n-5k+15)-2n_{3}, |  |

 | n 54 = \displaystyle n_{54}= | 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6), \displaystyle\frac{1}{16}nk(k-2)(k-4)(k-6), |  |

 | n 55 = \displaystyle n_{55}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) + 2 ​ n 3, \displaystyle\frac{1}{4}nk(k-2)(k-4)(k-6)+2n_{3}, |  |

 | n 56 = \displaystyle n_{56}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 10 ​ k + 30) − 4 ​ n 3, \displaystyle\frac{1}{4}nk(k-2)(k-4)(k^{2}-10k+30)-4n_{3}, |  |

 | n 57 = \displaystyle n_{57}= | n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 4 − 18 ​ k 3 + 140 ​ k 2 − 564 ​ k + 996) / 192 − 4 3 ​ n 3, \displaystyle nk(k-2)(k-4)(k^{4}-18k^{3}+140k^{2}-564k+996)/192-\frac{4}{3}n_{3}, |  |

 | n 58 = \displaystyle n_{58}= | 1 8 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 15 ​ k 2 + 86 ​ k − 190) + 8 ​ n 3, \displaystyle\frac{1}{8}nk(k-2)(k-4)(k^{3}-15k^{2}+86k-190)+8n_{3}, |  |

 | n 59 = \displaystyle n_{59}= | 1 24 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6) ​ ( k 2 − 10 ​ k + 34) + 2 ​ n 3, \displaystyle\frac{1}{24}nk(k-2)(k-4)(k-6)(k^{2}-10k+34)+2n_{3}, |  |

 | n 60 = \displaystyle n_{60}= | 1 8 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 12 ​ k + 38) − 2 ​ n 3, \displaystyle\frac{1}{8}nk(k-2)(k-4)(k^{2}-12k+38)-2n_{3}, |  |

 | n 61 = \displaystyle n_{61}= | 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 16 ​ k 2 + 96 ​ k − 220) + 5 ​ n 3, \displaystyle\frac{1}{16}nk(k-2)(k-4)(k^{3}-16k^{2}+96k-220)+5n_{3}, |  |

 | n 62 = \displaystyle n_{62}= | 1 24 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 14 ​ k + 54) − 2 ​ n 3. \displaystyle\frac{1}{24}nk(k-2)(k-4)(k^{2}-14k+54)-2n_{3}. |  |

First of all notice that the values for n 3 n_{3} are not given. The arguments of symmetry tell us that it should be equal zero, but then it would follow immediately that s ​ r ​ g ​ ( 99, 14, 1, 2) srg(99,14,1,2), an infamous strongly regular of Conway, doesn’t exist [7]. All other values for other six-vertex subgraphs are given in terms of n, k n,k and n 3 n_{3}. Of course, it is possible using the relation between n n and k k to get rid of n n altogether but then the formulas become very cumbersome.

## 3 Four- and Five-Vertex Subgraphs

There are only nine subgraphs of order four in G G. They are given in Figure 2. Denote them L i L_{i} and their quantities l i ​ ( i = 1, 9 ¯) l_{i}(i=\overline{1,9}). It is a trivial exercise to find the number of each subgraph of order four. They are as follows:

[image: Refer to caption] Figure 2: All possible subgraphs of order four in s ​ r ​ g ​ ( n, k, 1, 2) srg(n,k,1,2).

 | l 1 = \displaystyle l_{1}= | 1 192 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 6 ​ k 2 + 10 ​ k − 12), \displaystyle\frac{1}{192}nk(k-2)(k-4)(k^{3}-6k^{2}+10k-12), |  |

 | l 2 = \displaystyle l_{2}= | 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 4 ​ k + 6), \displaystyle\frac{1}{16}nk(k-2)(k-4)(k^{2}-4k+6), |  |

 | l 3 = \displaystyle l_{3}= | 1 16 ​ n ​ k ​ ( k − 2) ​ ( k 2 − 6 ​ k + 10), \displaystyle\frac{1}{16}nk(k-2)(k^{2}-6k+10), |  |

 | l 4 = \displaystyle l_{4}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( n − 3 ​ k + 4), \displaystyle\frac{1}{2}nk(k-2)(n-3k+4), |  |

 | l 5 = \displaystyle l_{5}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 3), \displaystyle\frac{1}{2}nk(k-2)(k-3), |  |

 | l 6 = \displaystyle l_{6}= | 1 6 ​ n ​ k ​ ( k − 2) ​ ( k − 4), \displaystyle\frac{1}{6}nk(k-2)(k-4), |  |

 | l 7 = \displaystyle l_{7}= | 1 12 ​ n ​ k ​ ( k − 2) ​ ( k − 4), \displaystyle\frac{1}{12}nk(k-2)(k-4), |  |

 | l 8 = \displaystyle l_{8}= | 1 8 ​ n ​ k ​ ( k − 2), \displaystyle\frac{1}{8}nk(k-2), |  |

 | l 9 = \displaystyle l_{9}= | 1 2 ​ n ​ k ​ ( k − 2). \displaystyle\frac{1}{2}nk(k-2). |  |

Based on these values, we can find the values for the five-vertex subgraphs. For that, we can use the following equations bounding the values for four-vertex subgraphs with five-vertex ones. To obtain these equations we need to consider all the possible graphs that can be obtained by adding to a given four-vertex subgraph exactly one vertex out of n − 4 n-4 remaining in G G. On the other hand, we can obtain the same quantities by subtracting a vertex from a given five-vertex subgraph. It is a tedious but straight-forward exercise.

 | l 1 ​ ( n − 4) = \displaystyle l_{1}(n-4)= | 5 ​ m 1 + 2 ​ m 2 + m 3 + m 5 + m 9, \displaystyle 5m_{1}+2m_{2}+m_{3}+m_{5}+m_{9}, |  |

 | l 2 ​ ( n − 4) = \displaystyle l_{2}(n-4)= | 3 ​ m 2 + 2 ​ m 3 + 4 ​ m 4 + m 6 + 2 ​ m 7 + 3 ​ m 8 + m 11 + m 12 + m 17, \displaystyle 3m_{2}+2m_{3}+4m_{4}+m_{6}+2m_{7}+3m_{8}+m_{11}+m_{12}+m_{17}, |  |

 | l 3 ​ ( n − 4) = \displaystyle l_{3}(n-4)= | m 4 + 2 ​ m 6 + m 13 + 3 ​ m 14 + m 19 + m 21, \displaystyle m_{4}+2m_{6}+m_{13}+3m_{14}+m_{19}+m_{21}, |  |

 | l 4 ​ ( n − 4) = \displaystyle l_{4}(n-4)= | 2 ​ m 3 + 3 ​ m 5 + 2 ​ m 6 + 2 ​ m 7 + 4 ​ m 10 + m 11 + 2 ​ m 12 + 2 ​ m 13 + m 15 + 2 ​ m 16, \displaystyle 2m_{3}+3m_{5}+2m_{6}+2m_{7}+4m_{10}+m_{11}+2m_{12}+2m_{13}+m_{15}+2m_{16}, |  |

 | l 5 ​ ( n − 4) = \displaystyle l_{5}(n-4)= | m 7 + 2 ​ m 11 + 2 ​ m 13 + 2 ​ m 15 + m 16 + 5 ​ m 18 + 2 ​ m 20 + 2 ​ m 21, \displaystyle m_{7}+2m_{11}+2m_{13}+2m_{15}+m_{16}+5m_{18}+2m_{20}+2m_{21}, |  |

 | l 6 ​ ( n − 4) = \displaystyle l_{6}(n-4)= | m 5 + 4 ​ m 9 + m 11 + m 15 + 2 ​ m 17, \displaystyle m_{5}+4m_{9}+m_{11}+m_{15}+2m_{17}, |  |

 | l 7 ​ ( n − 4) = \displaystyle l_{7}(n-4)= | 2 ​ m 8 + m 12 + 2 ​ m 14 + m 21, \displaystyle 2m_{8}+m_{12}+2m_{14}+m_{21}, |  |

 | l 8 ​ ( n − 4) = \displaystyle l_{8}(n-4)= | m 10 + m 15 + m 20, \displaystyle m_{10}+m_{15}+m_{20}, |  |

 | l 9 ​ ( n − 4) = \displaystyle l_{9}(n-4)= | m 12 + 2 ​ m 16 + 2 ​ m 17 + 4 ​ m 19 + 2 ​ m 20 + m 21. \displaystyle m_{12}+2m_{16}+2m_{17}+4m_{19}+2m_{20}+m_{21}. |  |

By M i M_{i} here we denote the subgraph of type i i from the Figure 3 and m i m_{i} - the number of such subgraphs in G G. Notice, we can also use these equations to check the values for m i m_{i} -s. They are given below. Figure 3 depicts their configurations.

 | m 1 = \displaystyle m_{1}= | 1 960 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( n − 4 ​ k + 6) ​ ( k 3 − 6 ​ k 2 + 14 ​ k − 36), \displaystyle\frac{1}{960}nk(k-2)(k-4)(n-4k+6)(k^{3}-6k^{2}+14k-36), |  |

 | m 2 = \displaystyle m_{2}= | 1 96 ​ n ​ k ​ ( k − 2) ​ ( k − 4) 2 ​ ( k 3 − 8 ​ k 2 + 26 ​ k − 48), \displaystyle\frac{1}{96}nk(k-2)(k-4)^{2}(k^{3}-8k^{2}+26k-48), |  |

 | m 3 = \displaystyle m_{3}= | 1 16 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 10 ​ k 2 + 38 ​ k − 60), \displaystyle\frac{1}{16}nk(k-2)(k-4)(k^{3}-10k^{2}+38k-60), |  |

 | m 4 = \displaystyle m_{4}= | 1 32 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 3 − 10 ​ k 2 + 40 ​ k − 68), \displaystyle\frac{1}{32}nk(k-2)(k-4)(k^{3}-10k^{2}+40k-68), |  |

 | m 5 = \displaystyle m_{5}= | 1 6 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( n − 4 ​ k + 8), \displaystyle\frac{1}{6}nk(k-2)(k-4)(n-4k+8), |  |

 | m 6 = \displaystyle m_{6}= | 1 8 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 8 ​ k + 20), \displaystyle\frac{1}{8}nk(k-2)(k-4)(k^{2}-8k+20), |  |

 | m 7 = \displaystyle m_{7}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k 2 − 7 ​ k + 16), \displaystyle\frac{1}{4}nk(k-2)(k-4)(k^{2}-7k+16), |  |

 | m 8 = \displaystyle m_{8}= | 1 24 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( n − 4 ​ k + 8), \displaystyle\frac{1}{24}nk(k-2)(k-4)(n-4k+8), |  |

 | m 9 = \displaystyle m_{9}= | 1 24 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6), \displaystyle\frac{1}{24}nk(k-2)(k-4)(k-6), |  |

 | m 10 = \displaystyle m_{10}= | 1 8 ​ n ​ k ​ ( k − 2) ​ ( n − 4 ​ k + 8), \displaystyle\frac{1}{8}nk(k-2)(n-4k+8), |  |

 | m 11 = \displaystyle m_{11}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) 2, \displaystyle\frac{1}{2}nk(k-2)(k-4)^{2}, |  |

 | m 12 = \displaystyle m_{12}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4) 2, \displaystyle\frac{1}{4}nk(k-2)(k-4)^{2}, |  |

 | m 13 = \displaystyle m_{13}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k 2 − 8 ​ k + 17), \displaystyle\frac{1}{2}nk(k-2)(k^{2}-8k+17), |  |

 | m 14 = \displaystyle m_{14}= | 1 24 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 6), \displaystyle\frac{1}{24}nk(k-2)(k-4)(k-6), |  |

 | m 15 = \displaystyle m_{15}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4), \displaystyle\frac{1}{2}nk(k-2)(k-4), |  |

 | m 16 = \displaystyle m_{16}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 3), \displaystyle\frac{1}{2}nk(k-2)(k-3), |  |

 | m 17 = \displaystyle m_{17}= | 1 4 ​ n ​ k ​ ( k − 2) ​ ( k − 4), \displaystyle\frac{1}{4}nk(k-2)(k-4), |  |

 | m 18 = \displaystyle m_{18}= | 1 5 ​ n ​ k ​ ( k − 2) ​ ( k − 4), \displaystyle\frac{1}{5}nk(k-2)(k-4), |  |

 | m 19 = \displaystyle m_{19}= | 1 8 ​ n ​ k ​ ( k − 2), \displaystyle\frac{1}{8}nk(k-2), |  |

 | m 20 = \displaystyle m_{20}= | 1 2 ​ n ​ k ​ ( k − 2), \displaystyle\frac{1}{2}nk(k-2), |  |

 | m 21 = \displaystyle m_{21}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4). \displaystyle\frac{1}{2}nk(k-2)(k-4). |  |

[image: Refer to caption] Figure 3: All possible subgraphs of order five in s ​ r ​ g ​ ( n, k, 1, 2) srg(n,k,1,2).

Similarly, we can derive the equations bounding the values for n i n_{i} -s with the values for m i m_{i} -s. In fact we can do it for subgraphs of any orders given that we studied all the possible configurations of them.

 | m 1 ​ ( n − 5) = \displaystyle m_{1}(n-5)= | n 30 + 6 ​ n 36 + 2 ​ n 37 + n 38 + n 40 + n 44, \displaystyle n_{30}+6n_{36}+2n_{37}+n_{38}+n_{40}+n_{44}, |  |

 | m 2 ​ ( n − 5) = \displaystyle m_{2}(n-5)= | n 19 + n 31 + 4 ​ n 37 + 2 ​ n 38 + 4 ​ n 39 + n 41 + 2 ​ n 42 + 3 ​ n 43 + n 46 + n 47 + n 52 + n 59, \displaystyle n_{19}+n_{31}+4n_{37}+2n_{38}+4n_{39}+n_{41}+2n_{42}+3n_{43}+n_{46}+n_{47}+n_{52}+n_{59}, |  |

 | m 3 ​ ( n − 5) = \displaystyle m_{3}(n-5)= | n 20 + n 26 + 2 ​ n 32 + n 34 + 3 ​ n 38 + 3 ​ n 40 + 2 ​ n 41 + 2 ​ n 42 + 4 ​ n 45 + n 46 + 2 ​ n 47 + 2 ​ n 48 \displaystyle n_{20}+n_{26}+2n_{32}+n_{34}+3n_{38}+3n_{40}+2n_{41}+2n_{42}+4n_{45}+n_{46}+2n_{47}+2n_{48} |  |

 |  | + n 50 + 2 ​ n 51 + 2 ​ n 61, \displaystyle+n_{50}+2n_{51}+2n_{61}, |  |

 | m 4 ​ ( n − 5) = \displaystyle m_{4}(n-5)= | n 15 + n 22 + n 33 + 2 ​ n 39 + 2 ​ n 41 + n 48 + 3 ​ n 49 + n 54 + n 56 + 6 ​ n 57 + 2 ​ n 58 + n 60, \displaystyle n_{15}+n_{22}+n_{33}+2n_{39}+2n_{41}+n_{48}+3n_{49}+n_{54}+n_{56}+6n_{57}+2n_{58}+n_{60}, |  |

 | m 5 ​ ( n − 5) = \displaystyle m_{5}(n-5)= | n 20 + 2 ​ n 28 + n 31 + n 34 + 2 ​ n 40 + 4 ​ n 44 + n 46 + n 50 + 2 ​ n 52 + 2 ​ n 59, \displaystyle n_{20}+2n_{28}+n_{31}+n_{34}+2n_{40}+4n_{44}+n_{46}+n_{50}+2n_{52}+2n_{59}, |  |

 | m 6 ​ ( n − 5) = \displaystyle m_{6}(n-5)= | n 7 + n 11 + 4 ​ n 13 + n 16 + n 23 + n 24 + n 25 + n 34 + 2 ​ n 35 + n 41 + 2 ​ n 58 + 3 ​ n 59 \displaystyle n_{7}+n_{11}+4n_{13}+n_{16}+n_{23}+n_{24}+n_{25}+n_{34}+2n_{35}+n_{41}+2n_{58}+3n_{59} |  |

 |  | + 2 ​ n 60 + 4 ​ n 61 + 3 ​ n 62, \displaystyle+2n_{60}+4n_{61}+3n_{62}, |  |

 | m 7 ​ ( n − 5) = \displaystyle m_{7}(n-5)= | n 17 + 3 ​ n 21 + 2 ​ n 27 + n 29 + 2 ​ n 33 + 2 ​ n 35 + 2 ​ n 42 + 2 ​ n 46 + 2 ​ n 48 + 2 ​ n 50 + n 51 + 5 ​ n 53 \displaystyle n_{17}+3n_{21}+2n_{27}+n_{29}+2n_{33}+2n_{35}+2n_{42}+2n_{46}+2n_{48}+2n_{50}+n_{51}+5n_{53} |  |

 |  | + 2 ​ n 55 + 2 ​ n 56 + 2 ​ n 58, \displaystyle+2n_{55}+2n_{56}+2n_{58}, |  |

 | m 8 ​ ( n − 5) = \displaystyle m_{8}(n-5)= | n 24 + 3 ​ n 43 + n 47 + 2 ​ n 49 + n 56 + n 62, \displaystyle n_{24}+3n_{43}+n_{47}+2n_{49}+n_{56}+n_{62}, |  |

 | m 9 ​ ( n − 5) = \displaystyle m_{9}(n-5)= | 2 ​ n 19 + n 26 + 5 ​ n 30 + n 31 + n 44, \displaystyle 2n_{19}+n_{26}+5n_{30}+n_{31}+n_{44}, |  |

 | m 10 ​ ( n − 5) = \displaystyle m_{10}(n-5)= | n 6 + n 11 + 2 ​ n 13 + 2 ​ n 45 + n 50 + n 55, \displaystyle n_{6}+n_{11}+2n_{13}+2n_{45}+n_{50}+n_{55}, |  |

 | m 11 ​ ( n − 5) = \displaystyle m_{11}(n-5)= | 2 ​ n 10 + n 11 + n 17 + n 18 + n 20 + 2 ​ n 22 + 2 ​ n 24 + 2 ​ n 26 + 2 ​ n 27 + 2 ​ n 29 + 3 ​ n 31 + 4 ​ n 32 \displaystyle 2n_{10}+n_{11}+n_{17}+n_{18}+n_{20}+2n_{22}+2n_{24}+2n_{26}+2n_{27}+2n_{29}+3n_{31}+4n_{32} |  |

 |  | + 2 ​ n 33 + n 34 + n 46, \displaystyle+2n_{33}+n_{34}+n_{46}, |  |

 | m 12 ​ ( n − 5) = \displaystyle m_{12}(n-5)= | n 16 + n 18 + n 22 + n 23 + n 25 + 2 ​ n 47 + 2 ​ n 51 + 2 ​ n 52 + 4 ​ n 54 + 2 ​ n 55 + n 56 + 2 ​ n 60, \displaystyle n_{16}+n_{18}+n_{22}+n_{23}+n_{25}+2n_{47}+2n_{51}+2n_{52}+4n_{54}+2n_{55}+n_{56}+2n_{60}, |  |

 | m 13 ​ ( n − 5) = \displaystyle m_{13}(n-5)= | n 2 + 2 ​ n 6 + 2 ​ n 8 + 2 ​ n 9 + 2 ​ n 11 + 6 ​ n 12 + n 18 + n 23 + 2 ​ n 25 + 2 ​ n 28 + 2 ​ n 29 + n 33 \displaystyle n_{2}+2n_{6}+2n_{8}+2n_{9}+2n_{11}+6n_{12}+n_{18}+n_{23}+2n_{25}+2n_{28}+2n_{29}+n_{33} |  |

 |  | + 2 ​ n 34 + 2 ​ n 35 + n 48, \displaystyle+2n_{34}+2n_{35}+n_{48}, |  |

 | m 14 ​ ( n − 5) = \displaystyle m_{14}(n-5)= | 2 ​ n 5 + 6 ​ n 14 + n 25 + n 49 + n 60 + 2 ​ n 62, \displaystyle 2n_{5}+6n_{14}+n_{25}+n_{49}+n_{60}+2n_{62}, |  |

 | m 15 ​ ( n − 5) = \displaystyle m_{15}(n-5)= | 2 ​ n 4 + 2 ​ n 7 + 4 ​ n 9 + 2 ​ n 10 + n 11 + n 17 + n 18 + 2 ​ n 26 + 2 ​ n 27 + 2 ​ n 28 + n 50, \displaystyle 2n_{4}+2n_{7}+4n_{9}+2n_{10}+n_{11}+n_{17}+n_{18}+2n_{26}+2n_{27}+2n_{28}+n_{50}, |  |

 | m 16 ​ ( n − 5) = \displaystyle m_{16}(n-5)= | 2 ​ n 2 + n 4 + 2 ​ n 6 + n 8 + 2 ​ n 16 + n 17 + 2 ​ n 20 + 3 ​ n 21 + n 23 + n 51, \displaystyle 2n_{2}+n_{4}+2n_{6}+n_{8}+2n_{16}+n_{17}+2n_{20}+3n_{21}+n_{23}+n_{51}, |  |

 | m 17 ​ ( n − 5) = \displaystyle m_{17}(n-5)= | n 7 + 4 ​ n 15 + n 17 + 3 ​ n 19 + n 20 + n 22 + n 52, \displaystyle n_{7}+4n_{15}+n_{17}+3n_{19}+n_{20}+n_{22}+n_{52}, |  |

 | m 18 ​ ( n − 5) = \displaystyle m_{18}(n-5)= | n 4 + n 8 + 2 ​ n 10 + n 29 + n 53, \displaystyle n_{4}+n_{8}+2n_{10}+n_{29}+n_{53}, |  |

 | m 19 ​ ( n − 5) = \displaystyle m_{19}(n-5)= | n 2 + n 15 + n 16 + n 54, \displaystyle n_{2}+n_{15}+n_{16}+n_{54}, |  |

 | m 20 ​ ( n − 5) = \displaystyle m_{20}(n-5)= | 6 ​ n 1 + 2 ​ n 2 + 2 ​ n 3 + 2 ​ n 4 + n 6 + n 17 + n 18 + n 55, \displaystyle 6n_{1}+2n_{2}+2n_{3}+2n_{4}+n_{6}+n_{17}+n_{18}+n_{55}, |  |

 | m 21 ​ ( n − 5) = \displaystyle m_{21}(n-5)= | 4 ​ n 3 + 4 ​ n 5 + 2 ​ n 7 + 2 ​ n 8 + n 16 + n 18 + n 22 + n 23 + 2 ​ n 24 + n 25 + n 56. \displaystyle 4n_{3}+4n_{5}+2n_{7}+2n_{8}+n_{16}+n_{18}+n_{22}+n_{23}+2n_{24}+n_{25}+n_{56}. |  |

## 4 Conclusion

In this paper we have studied the structure of a class of strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2. In particular we have found the subgraphs of order up to six: all their configurations and their number if the graph with given parameters do exist. All the subgraphs of order up to five have exact values that depend only on parameters n n and k k, which are themselves interdependent. In fact, we can say that they depend only on valency of G G. While starting from subgraphs of order six it is required one additional parameter n 3 n_{3} in order to define the number of each subgraph in G G. Well, at least we were not able to avoid it. All the arguments of symmetry tell that n 3 n_{3} must be equal zero. But that would immediately mean, as shown by Makhnev [7], that an s ​ r ​ g ​ ( 99, 14, 1, 2) srg(99,14,1,2) doesn’t exist, while the rest of the graphs from the family must be of more coerce structure, namely consist of Paley-9 as building blocks.

Some preliminary research done on subgraphs of order seven tells us that their numbers depend on two parameters one of which can be chosen the same n 3 n_{3}. This is clearly a direction to work on although no conclusions might be guaranteed.

## References

- [1] Conway, John (Update 2017), *Five $ 1,000 Problems*, On-Line Encyclopedia of Integer Sequences, OEIS sequance A248380.
- [2] Berlekamp, E.R.; Van Lint, J.H.; Seidel, J.J.(1973), *A strongly regular graph derived from the perfect ternary Golay code*, A survey of combinatorial theory, Amsterdam, 25-30.
- [3] Royle, Gordon, *List of Large Graphs and Families*, http://people.csse.uwa.edu.au/gordon/remote/srgs/
- [4] Brouwer, Andries E., *Parameters of Strongly Regular Graphs*, https://www.win.tue.nl/~aeb/graphs/srg/srgtab.html
- [5] Brouwer, Andries; van Maldeghem, Hendrik (2022), *Strongly Regular Graphs*, Cambridge University Press.
- [6] Makhnev, A; Minkova, I (2004), *On automorphisms of strongly regular graphs with parameters λ = 1, μ = 2 \lambda=1,\mu=2*, Discrete Mathematics and Applications.
- [7] Makhnev, A. (1988), *Strongly Regular Graphs with λ = 1 \lambda=1*, Matemticheskie Zametki, Vol.44, No.5, pp.667-672, Academy of Sciences of the USSR.
- [8] Wilbrink, H.; A., Brouwer, A. E. (1983, January). A (57, 14, 1) strongly regular graph does not exist. In Indagationes Mathematicae (Proceedings) (Vol. 86, No. 1, pp. 117-121). North-Holland.
- [9] Lou, S.; Murin, M. On The Strongly Regular Graph of Parameters (99, 14, 1, 2).
- [10] Reimbayev, R (2024), *The Lower Bound for Number of Hexagons in Strongly Regular Graphs with Parameters λ = 1 \lambda=1 and μ = 2 \mu=2*, ArXiv


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
