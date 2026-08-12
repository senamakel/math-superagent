<!-- source: https://arxiv.org/html/2410.22842v2 | converted from HTML -->

Erdős-Gyárfás conjecture on graphs without long induced paths

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2410.22842v2 [math.CO] 11 Feb 2025

# Erdős-Gyárfás conjecture on graphs without long induced paths Thanks: A major part of this work was done when the first and the last authors were at IIT Dharwad. This project is supported by ANRF (SERB) MATRICS grant MTR/2022/000692.

Anand Shripad Hegde Affiliation: Department of Computer Science and Engineering, Indian Institute of Technology Dharwad, Dharwad, India E-mail [{cs20bt058.alum24, sandeeprb, cs20bt048.alum24}@iitdh.ac.in][3] Affiliation: Arista Networks, Bengaluru, India R. B. Sandeep Affiliation: Department of Computer Science and Engineering, Indian Institute of Technology Dharwad, Dharwad, India E-mail [{cs20bt058.alum24, sandeeprb, cs20bt048.alum24}@iitdh.ac.in][3] P. Shashank Affiliation: Department of Computer Science and Engineering, Indian Institute of Technology Dharwad, Dharwad, India E-mail [{cs20bt058.alum24, sandeeprb, cs20bt048.alum24}@iitdh.ac.in][3] Affiliation: Arista Networks, Bengaluru, India

###### Abstract

Erdős and Gyárfás conjectured in 1994 that every graph with minimum degree at least 3 3 has a cycle of length a power of 2 2. In 2022, Gao and Shan (Graphs and Combinatorics) proved that the conjecture is true for P 8 P_{8} -free graphs, i.e., graphs without any induced copies of a path on 8 8 vertices. In 2024, Hu and Shen (Discrete Mathematics) improved this result by proving that the conjecture is true for P 10 P_{10} -free graphs. With the aid of a computer search, we improve this further by proving that the conjecture is true for P 13 P_{13} -free graphs.

###### Keywords:

Erdős-Gyárfás conjecture P k P_{k} -free graphs Computer-aided proof.

In 1994, Erdős and Gyárfás [3] 1 1 1 In a paper published in 1997 [3], Erdős wrote: “About three years ago, Gyárfás and I thought at first that if G G is any graph every vertex of which has degree ≥ 3 \geq 3 then our G G has a cycle of length 2 k 2^{k} for some k k. We are convinced now that this is false and no doubt there are graphs for every r r every vertex of which has degree ≥ r \geq r and which contains no cycle of length 2 k 2^{k}, but we never found a counterexample even for r = 3 r=3.” conjectured that every graph with minimum degree at least 3 3 has a cycle of length a power of 2 2. The conjecture has been verified for the following classes of graphs - 3 3 -connected cubic planar graphs [6], claw-free planar graphs [2], K 1, m K_{1,m} -free graphs with some additional degree constraints [12], and some families of Cayley graphs [5]. Liu and Montgomery [9] proved that there exists a large constant such that every graph with average degree at least the constant has a cycle with length a power of 2. This disproved Erdős’ later conviction that the conjecture is false for every minimum degree at least 3 [3]. Extensive computer searches have been done to show that a counterexample has at least 17 17 vertices, a cubic counterexample has at least 30 30 vertices [10], and a bipartite counterexample has at least 30 30 vertices [11].

In 2022, Gao and Shan [4] proved that the conjecture is true for P 8 P_{8} -free graphs, i.e., graphs without any induced copies of a path on 8 8 vertices. Very recently, Hu and Shen [8] proved that the conjecture is true for P 10 P_{10} -free graphs. Inspired by a case analysis in [4], we prove with the aid of a computer search that the conjecture is true for P 13 P_{13} -free graphs. We prove a stronger statement for P 12 P_{12} -free graphs that every P 12 P_{12} -free graphs with minimum degree at least 3 has a 4-cycle or an 8-cycle. This improves upon the similar result obtained for P 10 P_{10} -free graphs [8].

The key backtracking algorithm that we implemented is shown in Figure 1. The implementation is available at [7]. The algorithm explore takes two inputs: a graph G G and an integer k ≥ 3 k\geq 3. The vertices of G G are assumed to be v 0, v 1, …, v n − 1 v_{0},v_{1},\ldots,v_{n-1}. It outputs False, if G G can be extended to a P k P_{k} -free counterexample, i.e., if there exists a P k P_{k} -free counterexample G ∗ G^{*} to Erdős-Gyárfás conjecture with a vertex labeling v 0, v 1, …, v n ∗ − 1 v_{0},v_{1},\ldots,v_{n^{*}-1} (where n ∗ ≥ n n^{*}\geq n) such that { v i, v j } \{v_{i},v_{j}\}, for 0 ≤ i < j ≤ n − 2 0\leq i<j\leq n-2, is an edge in G G if and only if it is an edge in G ∗ G^{*}, and the set of neighbors of v n − 1 v_{n-1} in G G is a subset of its neighbors in G ∗ G^{*}. The algorithm returns True otherwise. We say that a subset S S of { v 0, v 1, …, v n − 2 } \{v_{0},v_{1},\ldots,v_{n-2}\} is a set of potential safe neighbors of v n − 1 v_{n-1} if { v i, v n − 1 } \{v_{i},v_{n-1}\} is not an edge (for v i ∈ S v_{i}\in S) in G G and making all vertices in S S neighbors of v n − 1 v_{n-1} does not create any forbidden cycles (a cycle is forbidden if it is of length a power of 2 2). For each such set S S of safe potential neighbors of v n − 1 v_{n-1}, we add the corresponding edges, and then check whether the new graph is a counterexample or not. If a P k P_{k} -free counterexample is found, we return False. If the updated graph G G is not a counterexample and it is P k P_{k} -free, then we find a vertex, anchor_node with degree less than 3 3, and make it adjacent to a new vertex v n v_{n}. We call explore with this updated graph G G and k k and return the result if it is False. If the recursive calls return True for each set of potential safe neighbors, then return True at the end. We run explore with P k, k P_{k},k for k ≥ 3 k\geq 3. If we obtain that the function returns True for every 3 ≤ k ≤ t 3\leq k\leq t, then we claim that the conjecture is true for P t P_{t} -free graphs.

The function get_largest_low_degree_vertex returns the vertex with largest index having a degree less than 3 3. It returns − 1 -1 if the minimum degree is at least 3 3. By G ⁡ [A] G[A], where A A is a subset of vertices of G G, we denote the graph induced by A A in G G. If A = { u 1, u 2, …, u p } A=\{u_{1},u_{2},\ldots,u_{p}\}, then G ⁡ [u 1, u 2, …, u p] G[u_{1},u_{2},\ldots,u_{p}] denotes the graph G ⁡ [A] G[A]. A graph is a minimal counterexample, if none of its proper induced subgraphs are counterexamples.

Figure 1: The algorithm

1: function explore ( G, k G,k) ⊳ \triangleright V ⁡ ( G) = { v 0, v 1, …, v n − 1 } V(G)=\{v_{0},v_{1},\ldots,v_{n-1}\}

2: for each set S S of potential safe neighbors of v n − 1 v_{n-1} do

3: Add edge { v i, v n − 1 } \{v_{i},v_{n-1}\} to G G, for each v i ∈ S v_{i}\in S.

4: if there is an induced P k P_{k} in G G then

5: continue

6: end if

7: anchor_node ← \leftarrow get_largest_low_degree_vertex ( G G)

8: if anchor_node = ⁣ = == -1 then

9: return False ⊳ \triangleright G is a counterexample.

10: end if

11: Add a node v n v_{n} and the edge { v n, a ​ n ​ c ​ h ​ o ​ r ​ _ ​ n ​ o ​ d ​ e } \{v_{n},anchor\_node\} to G G

12: if not explore ( G, k G,k) then

13: return False

14: end if

15: Remove node v n v_{n} from G G.

16: Remove edge { v i, v n − 1 } \{v_{i},v_{n-1}\} from G G, for each v i ∈ S v_{i}\in S.

17: end for

18: return True

19: end function

###### Lemma 1

Let G ∗ G^{*} be a minimal counterexample to Erdős-Gyárfás conjecture, such that G ∗ G^{*} is P k P_{k} -free for an integer k ≥ 3 k\geq 3. Let { v 0, v 1, …, v n ∗ − 1 } \{v_{0},v_{1},\ldots,v_{n^{*}-1}\} be the set of vertices of G ∗ G^{*}. Let G G be a graph with the vertex set { v 0, v 1, …, v n − 1 } \{v_{0},v_{1},\ldots,v_{n-1}\}, where 3 ≤ n ≤ n ∗ 3\leq n\leq n^{*}, such that the following conditions are satisfied.

1. i.

The pair { v i, v j } \{v_{i},v_{j}\}, for 0 ≤ i < j ≤ n − 2 0\leq i<j\leq n-2, is an edge in G ∗ G^{*} if and only if it an edge in G G.

2. ii.

If v i v_{i}, for 0 ≤ i ≤ n − 2 0\leq i\leq n-2, is a neighbor of v n − 1 v_{n-1} in G G, then so is in G ∗ G^{*}.

Then explore( G, k G,k) returns False.

###### Proof

We prove by induction on n ∗ − n n^{*}-n. For the base case, assume that n ∗ − n = 0 n^{*}-n=0. Let S S be the set of neighbors in G ∗ G^{*} which are not neighbors of v n − 1 v_{n-1} in G G. This set S S is discovered in one iteration of the for loop (line 2). Then G G is updated (line 3) with the corresponding edges and the updated graph becomes isomorphic to G ∗ G^{*}. Since G ∗ G^{*} has no induced P k P_{k} and has minimum degree at least 3, the if condition in line 4 fails and that in line 8 succeeds and the algorithm returns False.

Now, assume that n ∗ − n > 0 n^{*}-n>0. As before, let S S be the set of neighbors among { v 0, v 1, …, v n − 2 } \{v_{0},v_{1},\ldots,v_{n-2}\} of v n − 1 v_{n-1} in G ∗ G^{*} which are not neighbors of v n − 1 v_{n-1} in G G. This set S S is discovered in one iteration of the for loop and the graph G G is updated with the corresponding edges. Therefore, { v i, v j } \{v_{i},v_{j}\}, for 0 ≤ i < j ≤ n − 1 0\leq i<j\leq n-1, is an edge in G ∗ G^{*} if and only if it an edge in G G. Since G ∗ G^{*} is P k P_{k} -free and G G is an induced subgraph of G ∗ G^{*}, the if condition in line 4 fails. Since G ∗ G^{*} is a minimal counterexample, G G must have a vertex with degree less than 3. Let i i be the largest index such that v i v_{i} is a vertex of degree at most 2 in G ∗ ​ [v 0, v 1, …, v n − 1] G^{*}[v_{0},v_{1},\ldots,v_{n-1}]. Then v i v_{i} is returned as the anchor_node in line 7. Clearly, v i v_{i} must have a neighbor v j v_{j} in G ∗ G^{*} such that v j ∈ { v n, v n + 1, …, v n ∗ − 1 } v_{j}\in\{v_{n},v_{n+1},\ldots,v_{n^{*}-1}\}. Without loss of generality, assume that j = n j=n. Now, the vertex v n v_{n} and the edge { v n, anchor_node } \{v_{n},\text{anchor\_node}\} are added to G G (line 11). Hence the number of vertices in G G got incremented by one. Further, G G trivially satisfies both the conditions in the statement of the lemma. Now the proof follows from the induction hypothesis.

Corollary 1 follows from Lemma 1.

###### Corollary 1

Let G ∗ G^{*} be a minimal counterexample to Erdős-Gyárfás conjecture and let k k be the smallest integer such that G ∗ G^{*} is P k P_{k} -free but has an induced P k − 1 P_{k-1}. Let G G be the path v 0 ​ v 1 ​ … ​ v k − 1 v_{0}v_{1}\ldots v_{k-1}. Then explore ( G, k G,k) returns False.

###### Theorem 0.1

Every P 13 P_{13} -free graph with minimum degree at least 3 3 has a cycle of length a power of 2 2.

###### Proof

We implemented explore and ran it with G, k G,k, where G G is the path v 0 ​ v 1 ​ … ​ v k − 1 v_{0}v_{1}\ldots v_{k-1}, for k k from 3 3 to 13 13. In all the executions, the program returned True. Now, the statement follows from Corollary 1 and the fact that P 2 P_{2} -free graphs have no edges.

We have a different implementation of the algorithm in which only cycles of lengths 4 and 8 are forbidden (see the branch ‘4-8-cycles’ in the repository [7]). Using this, we obtain a stronger result for P 12 P_{12} -free graphs.

###### Theorem 0.2

Every P 12 P_{12} -free graph with minium degree at least 3 3 has a 4-cycle or an 8-cycle.

This improves upon the result by Hu and Shen [8] that every P 10 P_{10} -free graph with minimum degree at least 3 has a 4-cycle or an 8-cycle.

We implemented [7] the algorithm 2 2 2 There are slight differences between the algorithm in Figure 1 and the implemented algorithm. The differences are trivial and have no implications on the correctness. For example, the implemented algorithm prints a counterexample, if exists, and exits, instead of returning False. In the implemented algorithm, the arguments passed to explore are G G and an anchor_node, instead of G G and k k. This is because, k k is available as part of the graph object and passing anchor_node helps in efficient execution. in C++. We also have a faster but memory-intensive parallel implementation using Cilk [1] (see ‘cilk’ branch of the repository). The time taken by these implementations when ran on a server ( 2.6 2.6 GHz CPU, 72 cores) is shown in Table 1. The parallel execution was terminated due to out of memory error when ran for k = 14 k=14. A serial execution of the modified implementation used for Theorem 0.2 took 1 minute 39 seconds for k = 11 k=11, and 3 hours 9 minutes for k = 12 k=12. We conducted extensive tests to obtain evidences for the correctness of the implementation. The details are given in the appendix.

k k | ≤ 9 \leq 9 | 10 | 11 | 12 | 13 |

Time taken (C++) | < < 0.2s | 2s | 32s | 31m 32s | 11h 56m |

Time taken (Cilk) | < < 0.05s | 0.1s | 1.4s | 29s | 17m 17s |

Table 1: Time taken by an implementation of Algorithm 1 for various values of k k. Seconds, minutes, and hours are represented by ‘s’, ‘m’, and ‘h’ respectively.

The technique that we used is not helpful for proving the conjecture for H H -free graphs when H H is not a path. Assume that H H has a cycle. Since an infinite tree with minimum degree at least 3 neither has H H as an induced subgraph nor has a cycle of length a power of 2 as a subgraph, the algorithm will run for ever. If H H is a tree but not a path, then we can come up with an H H -free infinite graph by replacing each vertex of an infinite tree (where every vertex has degree 3) with a clique of 3 vertices and making each such vertex adjacent to exactly one vertex in the clique formed for a neighbor. Since this graph is claw-free, every induced tree in it is a path. We end with the following question: Is Algorithm 1 capable of resolving the conjecture for P k P_{k} -free graphs for every integer k ≥ 14 k\geq 14? In other words, is there an infinite graph with minimum degree at least 3 neither having an induced P k P_{k} nor having a cycle of length a power of 2?

Acknowledgement. We thank Nikhil Hegde for suggesting ways to boost the performance of our code. We thank Paweł Rzążewski for helpful comments on an initial draft of this paper.

## References

- [1] Robert D Blumofe, Christopher F Joerg, Bradley C Kuszmaul, Charles E Leiserson, Keith H Randall, and Yuli Zhou. Cilk: An efficient multithreaded runtime system. ACM SigPlan Notices, 30(8):207–216, 1995.
- [2] Dale Daniel and Stephen E Shauger. A result on the Erdős-Gyárfás conjecture in planar graphs. Congressus Numerantium, pages 129–140, 2001.
- [3] Paul Erdös. Some old and new problems in various branches of combinatorics. Discret. Math., 165-166:227–231, 1997.
- [4] Yuping Gao and Songling Shan. Erdős-Gyárfás conjecture for P 8 {P}_{8} -free graphs. Graphs Comb., 38(6):168, 2022.
- [5] Mohammad Hossein Ghaffari and Zohreh Mostaghim. Erdős–Gyárfás conjecture for some families of cayley graphs. Aequationes mathematicae, 92:1–6, 2018.
- [6] Christopher Carl Heckman and Roi Krakovski. Erdös-Gyárfás conjecture for cubic planar graphs. Electron. J. Comb., 20(2):7, 2013.
- [7] Anand Shripad Hegde, R. B. Sandeep, and P. Shashank. Verifier for Erdős–Gyárfás conjecture on P k P_{k} -free graphs, October 2024. https://github.com/rbsandeep/Erdos-Gyarfas.
- [8] Zhiquan Hu and Changlong Shen. The Erdős-Gyárfás conjecture holds for P 10 {P}_{10} -free graphs. Discret. Math., 347(12):114175, 2024.
- [9] Hong Liu and Richard Montgomery. A solution to Erdős and Hajnal’s odd cycle problem. Journal of the American Mathematical Society, 36(4):1191–1234, 2023.
- [10] Klas Markström. Extremal graphs for some problems on cycles in graphs. University of Umeå, Department of Mathematics, 2002.
- [11] P Salehi Nowbandegani and H Esfandiari. An experimental result on the Erdős-Gyárfás conjecture in bipartite graphs. In 14th Workshop on Graph Theory CID, pages 18–23, 2011.
- [12] Stephen E Shauger. Results on the Erdős-Gyárfás conjecture in K 1, m {K}_{1,m} -free graphs. Congressus Numerantium, pages 61–66, 1998.

## Appendix: Correctness testing

The C++ program implementing the algorithm can be found at [7]. We conducted various tests to verify the correctness of the implementation. They are listed below. The outcome of the tests were as expected and we believe that it provides strong evidences for the correctness of the implementation.

1. 1.

The output of our program is in accordance with the result obtained in [8] for P 10 P_{10} -free graphs.

2. 2.

By introducing logs and visualization of intermediate graphs, we manually verified the execution of the program for 3 ≤ k ≤ 5 3\leq k\leq 5. The output was as expected. More details can be found in the ‘logs’ branch of the repository.

3. 3.

We conducted unit tests for major functions in the program. For each such functions, we tested with inputs where the corresponding outputs are known to us. More details can be found in the ‘tests’ branch of the repository.

4. 4.

We obtained all the four cubic graphs with minimum number (24) of vertices (found by Markström [10]) having no 4-cycle and no 8-cycle but having a 16-cycle by guiding the execution with proper values of k k and by restricting the degree to be 3. Only one of them, known as Markström graph (see Figure 2), is planar. It is P 18 P_{18} -free but has an induced P 17 P_{17}. More details can be found in the ‘special-graphs’ branch of the repository.

Figure 2: Markström graph: the unique smallest cubic planar graph having no 4-cycle and no 8-cycle, but having a 16-cycle. The bold (purple) edges show a 16-cycle.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:%7Bcs20bt058.alum24,%20sandeeprb,%20cs20bt048.alum24%7D@iitdh.ac.in
