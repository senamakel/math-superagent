<!-- source: https://arxiv.org/html/2511.06572v1 | converted from HTML -->

Hamiltonian Subgraphs of Order Seven in ⁢ s r g ( n , k , 1 , 2 )

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2511.06572v1 [math.CO] 09 Nov 2025

# Hamiltonian Subgraphs of Order Seven in s ​ r ​ g ​ ( n, k, 1, 2) srg(n,k,1,2)

Reimbay Reimbayev

###### Abstract

Strongly regular graphs are highly symmetrical and can be described fully with just a few parameters, yet the existence of many of them is still under the question. In this paper, we continue the study of the famuly of strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2 and establish all of their possible Hamiltonian subgraphs of order seven. By doing so we establish the lower and upper bounds for number of 7-gons, or 7-cycles, in such graphs.

We will skip a long and lengthy introduction into the problem [1] and motivation of this work as this is merely a continuation of the previous work that we have posted on ArXiv. But instead, we will briefly summarize what we have done so far. In our previous papers, we have extensively studied the structure of the strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2 [2, 3]. In particular, we have looked at the possible subgraphs of order six and their numbers in such graphs, should they exist. Here, we continue our previous work and move on subgraphs of order seven but only the ones that contain Hamiltonian cycles, or in short, the Hamiltonian subgraphs of order seven. By doing so, we will also establish bounds for heptagons, C 7 C_{7}, in addition to other polygons (cycles) of lower order that we have found previously.

Strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2, for simplicity henceforth call it a graph G G, can have 19 possible Hamiltonian subgraphs of order seven (Figure 1). The cycle of order seven is not depicted in the figure. Obviously, for the graphs of smaller order (smaller n n) not all the subgraphs would exist. The subgraphs are obtained by straight-forward exhaustive search of all such graphs that do not brake strong-regularity conditions for G G.

Let us denote H i H_{i} the graphs of type i i from the figure 1 and by h i h_{i} the number of such graphs in G G. Separately, we denote H 0 H_{0} the cycles of order seven, C 7 C_{7}, and h 0 h_{0} - the number of such cycles in G G. We will also extensively use the notation from the previous study regarding six-vertex subgraphs N i N_{i} and their number n i n_{i} given in the paper [3]. We assume they are already known. Here we derive only the values for h i h_{i}.

[image: Refer to caption] Figure 1: All possible Hamiltonian subgraphs, except one for a 7-cycle, in s ​ r ​ g ​ ( n, k, 1, 2) srg(n,k,1,2).

Some of the values for h i h_{i} -s can be found directly. For example, h 10 h_{10}. For that consider N 3 N_{3}. On one of the two sides of its quadrilateral with no triangles attached , we can recover a triangle in a unique way. Thus,

 | h 10 = 2 ​ n 3. h_{10}=2n_{3}. |  |

Similarly, H 17 H_{17} can be obtained from N 1 N_{1} in a unique way, by recovering a triangle on one of its three (free of triangles) sides. Thus,

 | h 17 = 3 ​ n 1 = 1 4 ​ n ​ k ​ ( k − 2) − n 3. h_{17}=3n_{1}=\frac{1}{4}nk(k-2)-n_{3}. |  |

Now H 14 H_{14} can be obtained from N 4 N_{4} uniquely in two ways:

 | h 14 = 2 ​ n 4 = 4 ​ n 3. h_{14}=2n_{4}=4n_{3}. |  |

Next, consider N 5 N_{5}. The subgraph has two triangles. Each vertex of degree two on one triangle has exactly two common neighbors with any two vertices of degree two of the other triangle. Thus,

 | h 6 = 8 ​ n 5 = n ​ k ​ ( k − 2) ​ ( k − 4) − 8 ​ n 3. h_{6}=8n_{5}=nk(k-2)(k-4)-8n_{3}. |  |

From N 9 N_{9}, we can recover H 4 H_{4}. Thus,

 | h 4 = n ​ k ​ ( k − 2) ​ ( k − 4) − 4 ​ n 3. h_{4}=nk(k-2)(k-4)-4n_{3}. |  |

Consider N 8 N_{8}. Recover a triangle at one of its edges that are not incident with its existing triangle (or belong to it). As there are only two such edges, there are two ways of doing that. We obtain:

 | 2 ​ n 8 = 2 ​ h 6 + 4 ​ h 15 + h 14. 2n_{8}=2h_{6}+4h_{15}+h_{14}. |  |

Thus,

 | 4 ​ h 15 = 2 ​ n 8 − 2 ​ h 6 − h 14 = 8 ​ n 3. 4h_{15}=2n_{8}-2h_{6}-h_{14}=8n_{3}. |  |

Or,

 | h 15 = 2 ​ n 3. h_{15}=2n_{3}. |  |

To move further, we have to assign one of the h i h_{i} -s as a free variable. The choice is fairly arbitrary. Here we have chosen h 11 h_{11}.

Consider N 4 N_{4}. Recover a triangle on its edge that is incident to the existing triangle of N 4 N_{4}, but only on the ones that are on its sides (leaving the one in the middle). Notice, that the middle edge is topologically different from the two on the sides, as it is incident to vertices of degrees both equal three. Thus,

 | 2 ​ n 4 = h 11 + 4 ​ h 18. 2n_{4}=h_{11}+4h_{18}. |  |

Or,

 | h 18 = n 3 − h 11 4. h_{18}=n_{3}-\frac{h_{11}}{4}. |  |

In the same way we recover triangles on N 8 N_{8} and obtain:

 | 2 ​ n 8 = 2 ​ h 3 + h 11. 2n_{8}=2h_{3}+h_{11}. |  |

Or,

 | h 3 = n ​ k ​ ( k − 2) ​ ( k − 4) − 2 ​ n 3 − h 11 2. h_{3}=nk(k-2)(k-4)-2n_{3}-\frac{h_{11}}{2}. |  |

Consider again N 4 N_{4}. It has a pair of vertices of degree two which must have exactly one more neighbor out of N 4 N_{4}. Recover it. We have,

 | n 4 = h 16 + 4 ​ h 18. n_{4}=h_{16}+4h_{18}. |  |

Or,

 | h 16 = − 2 ​ n 3 + h 11. h_{16}=-2n_{3}+h_{11}. |  |

As a side note, from the values of h 16 h_{16} and h 18 h_{18}, both nonnegative integers, we can give an estimates for h 11 h_{11}:

 | 4 ​ n 3 ≥ h 11 ≥ 2 ​ n 3. 4n_{3}\geq h_{11}\geq 2n_{3}. |  |

Once more, consider N 4 N_{4}. This time we are looking for the second common neighbor between a vertex of degree two (there are two of them but we take one) and the vertex of the triangle that doesn’t belong to the same equilateral as the first vertex. We have,

 | 2 ​ n 4 = 2 ​ h 13 + 4 ​ h 18. 2n_{4}=2h_{13}+4h_{18}. |  |

Or,

 | h 13 = h 11 2. h_{13}=\frac{h_{11}}{2}. |  |

Consider, M 19 M_{19}, or basically two triangles of G G that share a common vertex. The value of m 19 m_{19} is also taken from [3]. We can build it up to h 12 h_{12} and by doing that we can also obtain H 18 H_{18}. Thus,

 | 2 ​ m 19 = h 12 + h 18. 2m_{19}=h_{12}+h_{18}. |  |

Or,

 | h 12 = 1 4 ​ n ​ k ​ ( k − 2) − n 3 + h 11 4. h_{12}=\frac{1}{4}nk(k-2)-n_{3}+\frac{h_{11}}{4}. |  |

Consider N 9 N_{9}. The subgraph has exactly two pairs of vertices that are neither adjacent nor have a common neighbor in N 9 N_{9}. To a chosen pair we add one of their common neighbor from G G. We obtain:

 | 4 ​ n 9 = h 9 + 2 ​ h 16 + 2 ​ h 18. 4n_{9}=h_{9}+2h_{16}+2h_{18}. |  |

Or,

 | h 9 = n ​ k ​ ( k − 2) ​ ( k − 4) − 2 ​ n 3 − 3 2 ​ h 11. h_{9}=nk(k-2)(k-4)-2n_{3}-\frac{3}{2}h_{11}. |  |

Consider N 8 N_{8}. For the vertex of degree two of the triangle, there are exactly two vertices of N 8 N_{8} that are not adjacent to it but have a common neighbor (one of the vertices of the triangle). Recover the second common neighbor from G G. We get:

 | 2 ​ n 8 = h 8 + 2 ​ h 16 + 4 ​ h 15. 2n_{8}=h_{8}+2h_{16}+4h_{15}. |  |

Or,

 | h 8 = 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − 8 ​ n 3 − 2 ​ h 11. h_{8}=2nk(k-2)(k-4)-8n_{3}-2h_{11}. |  |

Consider N 9 N_{9}. Recover a triangle on one of the two edges that are incident to vertices of degree of two from both sides. We have:

 | 2 ​ n 9 = h 7 + 2 ​ h 16 + 2 ​ h 18. 2n_{9}=h_{7}+2h_{16}+2h_{18}. |  |

Or,

 | h 7 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − 3 2 ​ h 11. h_{7}=\frac{1}{2}nk(k-2)(k-4)-\frac{3}{2}h_{11}. |  |

Consider N 17 N_{17}. The vertex of degree two of the triangle of N 17 N_{17} (the ‘rooftop’) and its leaf has exactly one common neighbor outside of N 17 N_{17}. Recover it. We have:

 | n 17 = 2 ​ h 5 + 2 ​ h 13. n_{17}=2h_{5}+2h_{13}. |  |

Or,

 | h 5 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − h 11 2. h_{5}=\frac{1}{2}nk(k-2)(k-4)-\frac{h_{11}}{2}. |  |

Consider N 11 N_{11}. From the set of vertices G \ N 11 G\backslash N_{11} recover a common neighbor for the leaf and one of the vertices of degree two of the quadrilateral that is adjacent to the vertex of degree three in N 11 N_{11}. We have,

 | 4 ​ n 11 = 2 ​ h 2 + 2 ​ h 7 + 2 ​ h 5 + h 8 + h 11. 4n_{11}=2h_{2}+2h_{7}+2h_{5}+h_{8}+h_{11}. |  |

Or,

 | h 2 = n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 8) + 12 ​ n 3 + 5 2 ​ h 11. h_{2}=nk(k-2)(k-4)(k-8)+12n_{3}+\frac{5}{2}h_{11}. |  |

Consider a hexagon, N 12 N_{12}. Recover a triangle on one of its sides. We have:

 | 6 ​ n 12 = h 1 + h 8 + 2 ​ h 12. 6n_{12}=h_{1}+h_{8}+2h_{12}. |  |

Or,

 | h 1 = 1 2 ​ n ​ k ​ ( k − 2) ​ ( 2 ​ k 2 − 25 ​ k + 68) + 16 ​ n 3 + 3 2 ​ h 11. h_{1}=\frac{1}{2}nk(k-2)(2k^{2}-25k+68)+16n_{3}+\frac{3}{2}h_{11}. |  |

Finally, for h 0 h_{0}, the number of seven-cycles in G G, or heptagons, which are not depicted in the figure, we have a relation:

 | 2 ​ n 35 = 7 ​ h 0 + 2 ​ h 1 + 2 ​ h 2 + h 3 + h 4 + h 5. 2n_{35}=7h_{0}+2h_{1}+2h_{2}+h_{3}+h_{4}+h_{5}. |  |

Thus,

 | h 0 = 1 14 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( 2 ​ k 2 − 30 ​ k + 133) − 10 ​ n 3 − h 11. h_{0}=\frac{1}{14}nk(k-2)(k-4)(2k^{2}-30k+133)-10n_{3}-h_{11}. |  |

Notice, that given the values for n 3 n_{3} and h 11 h_{11} cannot be negative, we can see what should be the upper bound for number of heptagons in G G. It is not hard to derive the lower bound as well but we would rather leave it as it is as we strongly believe that the upper bound is indeed its exact value. To prove that still requires some meticulous work so for now we leave it as a conjecture.

Let us summarize what we have so far. Below are all the values for number of Hamiltonian subgraphs in s ​ r ​ g ​ ( n, k, 1, 2) srg(n,k,1,2). They are given in terms of ‘free variables’ n 3 n_{3} and h 11 h_{11}. Of course, it is possible using the relation between n n and k k to get rid of n n altogether but then the formulas become very cumbersome.

 | h 0 = \displaystyle h_{0}= | 1 14 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( 2 ​ k 2 − 30 ​ k + 133) − 10 ​ n 3 − h 11; \displaystyle\frac{1}{14}nk(k-2)(k-4)(2k^{2}-30k+133)-10n_{3}-h_{11}; |  |

 | h 1 = \displaystyle h_{1}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( 2 ​ k 2 − 25 ​ k + 68) + 16 ​ n 3 + 3 2 ​ h 11; \displaystyle\frac{1}{2}nk(k-2)(2k^{2}-25k+68)+16n_{3}+\frac{3}{2}h_{11}; |  |

 | h 2 = \displaystyle h_{2}= | n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( k − 8) + 12 ​ n 3 + 5 2 ​ h 11; \displaystyle nk(k-2)(k-4)(k-8)+12n_{3}+\frac{5}{2}h_{11}; |  |

 | h 3 = \displaystyle h_{3}= | n ​ k ​ ( k − 2) ​ ( k − 4) − 2 ​ n 3 − h 11 2; \displaystyle nk(k-2)(k-4)-2n_{3}-\frac{h_{11}}{2}; |  |

 | h 4 = \displaystyle h_{4}= | n ​ k ​ ( k − 2) ​ ( k − 4) − 4 ​ n 3; \displaystyle nk(k-2)(k-4)-4n_{3}; |  |

 | h 5 = \displaystyle h_{5}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − h 11 2; \displaystyle\frac{1}{2}nk(k-2)(k-4)-\frac{h_{11}}{2}; |  |

 | h 6 = \displaystyle h_{6}= | n ​ k ​ ( k − 2) ​ ( k − 4) − 8 ​ n 3; \displaystyle nk(k-2)(k-4)-8n_{3}; |  |

 | h 7 = \displaystyle h_{7}= | 1 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − 3 2 ​ h 11; \displaystyle\frac{1}{2}nk(k-2)(k-4)-\frac{3}{2}h_{11}; |  |

 | h 8 = \displaystyle h_{8}= | 2 ​ n ​ k ​ ( k − 2) ​ ( k − 4) − 8 ​ n 3 − 2 ​ h 11; \displaystyle 2nk(k-2)(k-4)-8n_{3}-2h_{11}; |  |

 | h 9 = \displaystyle h_{9}= | n ​ k ​ ( k − 2) ​ ( k − 4) − 2 ​ n 3 − 3 2 ​ h 11; \displaystyle nk(k-2)(k-4)-2n_{3}-\frac{3}{2}h_{11}; |  |

 | h 10 = \displaystyle h_{10}= | 2 ​ n 3; \displaystyle 2n_{3}; |  |

 | h 11 = \displaystyle h_{11}= | h 11; \displaystyle h_{11}; |  |

 | h 12 = \displaystyle h_{12}= | 1 4 ​ n ​ k ​ ( k − 2) − n 3 + h 11 4; \displaystyle\frac{1}{4}nk(k-2)-n_{3}+\frac{h_{11}}{4}; |  |

 | h 13 = \displaystyle h_{13}= | h 11 2; \displaystyle\frac{h_{11}}{2}; |  |

 | h 14 = \displaystyle h_{14}= | 4 ​ n 3; \displaystyle 4n_{3}; |  |

 | h 15 = \displaystyle h_{15}= | 2 ​ n 3; \displaystyle 2n_{3}; |  |

 | h 16 = \displaystyle h_{16}= | h 11 − 2 ​ n 3; \displaystyle h_{11}-2n_{3}; |  |

 | h 17 = \displaystyle h_{17}= | 1 4 ​ n ​ k ​ ( k − 2) − n 3; \displaystyle\frac{1}{4}nk(k-2)-n_{3}; |  |

 | h 18 = \displaystyle h_{18}= | n 3 − h 11 4. \displaystyle n_{3}-\frac{h_{11}}{4}. |  |

Finally, denote p i p_{i} the number of i-gons in G G. By i-gon here we mean cycle C i C_{i} in G G. Then, using the previously obtained results [2, 3] for p i p_{i} -s up to six and adding one more for p 7 p_{7}, we have the following relations:

 | p 3 = \displaystyle p_{3}= | 1 6 ​ n ​ k; \displaystyle\frac{1}{6}nk; |  |

 | p 4 = \displaystyle p_{4}= | 1 8 ​ n ​ k ​ ( k − 2); \displaystyle\frac{1}{8}nk(k-2); |  |

 | p 5 = \displaystyle p_{5}= | 1 5 ​ n ​ k ​ ( k − 2) ​ ( k − 4); \displaystyle\frac{1}{5}nk(k-2)(k-4); |  |

 | p 6 ≥ \displaystyle p_{6}\geq | 1 12 ​ n ​ k ​ ( k − 2) ​ ( 2 ​ k 2 − 21 ​ k + 53); \displaystyle\frac{1}{12}nk(k-2)(2k^{2}-21k+53); |  |

 | p 7 ≤ \displaystyle p_{7}\leq | 1 14 ​ n ​ k ​ ( k − 2) ​ ( k − 4) ​ ( 2 ​ k 2 − 30 ​ k + 133). \displaystyle\frac{1}{14}nk(k-2)(k-4)(2k^{2}-30k+133). |  |

We conjecture that the bounds for p 6 p_{6} and p 7 p_{7} are in fact their exact values.

## References

- [1] Conway, John (Update 2017), *Five $ 1,000 Problems*, On-Line Encyclopedia of Integer Sequences, OEIS sequence A248380.
- [2] Reimbayev, R (2024), *The Lower Bound for Number of Hexagons in Strongly Regular Graphs with Parameters λ = 1 \lambda=1 and μ = 2 \mu=2*, ArXiv
- [3] Reimbayev, R (2025), *The Subgraphs of Order Six of the Family of Strongly Regular Graphs with Parameters λ = 1 \lambda=1 and μ = 2 \mu=2*, ArXiv


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
