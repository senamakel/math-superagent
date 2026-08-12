<!-- source: https://arxiv.org/pdf/2410.22842 | converted from PDF -->

arXiv:2410.22842v2  [math.CO]  11 Feb 2025
Erdős-Gyárfás conjecture on graphs without long
induced paths⋆

Anand Shripad Hegde1,2, R. B. Sandeep1, and P. Shashank1,2

1 Department of Computer Science and Engineering, Indian Institute of Technology
Dharwad, Dharwad, India
{cs20bt058.alum24, sandeeprb, cs20bt048.alum24}@iitdh.ac.in
2 Arista Networks, Bengaluru, India

Abstract. Erdős and Gyárfás conjectured in 1994 that every graph with
minimum degree at least 3 has a cycle of length a power of 2. In 2022,
Gao and Shan (Graphs and Combinatorics) proved that the conjecture is
true for P8-free graphs, i.e., graphs without any induced copies of a path
on 8 vertices. In 2024, Hu and Shen (Discrete Mathematics) improved
this result by proving that the conjecture is true for P10-free graphs.
With the aid of a computer search, we improve this further by proving
that the conjecture is true for P13-free graphs.

Keywords: Erdős-Gyárfás conjecture · Pk-free graphs · Computer-aided
proof.

In 1994, Erdős and Gyárfás [3]
3 conjectured that every graph with minimum
degree at least 3 has a cycle of length a power of 2. The conjecture has been
veriﬁed for the following classes of graphs - 3-connected cubic planar graphs [6],
claw-free planar graphs [2], K1,m-free graphs with some additional degree con-
straints [12], and some families of Cayley graphs [5]. Liu and Montgomery [9]
proved that there exists a large constant such that every graph with average
degree at least the constant has a cycle with length a power of 2. This dis-
proved Erdős’ later conviction that the conjecture is false for every minimum
degree at least 3 [3]. Extensive computer searches have been done to show that
a counterexample has at least 17 vertices, a cubic counterexample has at least
30 vertices [10], and a bipartite counterexample has at least 30 vertices [11].
In 2022, Gao and Shan [4] proved that the conjecture is true for P8-free
graphs, i.e., graphs without any induced copies of a path on 8 vertices. Very

⋆ A major part of this work was done when the ﬁrst and the last authors were
at IIT Dharwad. This project is supported by ANRF (SERB) MATRICS grant
MTR/2022/000692.
3 In a paper published in 1997 [3], Erdős wrote: “About three years ago, Gyárfás and
I thought at ﬁrst that if G is any graph every vertex of which has degree ≥ 3 then
our G has a cycle of length 2
k for some k. We are convinced now that this is false
and no doubt there are graphs for every r every vertex of which has degree ≥ r and
which contains no cycle of length 2
k, but we never found a counterexample even for
r = 3.”

2 A. Hegde et al.

recently, Hu and Shen [8] proved that the conjecture is true for P10-free graphs.
Inspired by a case analysis in [4], we prove with the aid of a computer search
that the conjecture is true for P13-free graphs. We prove a stronger statement
for P12-free graphs that every P12-free graphs with minimum degree at least 3
has a 4-cycle or an 8-cycle. This improves upon the similar result obtained for
P10-free graphs [8].
The key backtracking algorithm that we implemented is shown in Figure 1.
The implementation is available at [7]. The algorithm explore takes two in-
puts: a graph G and an integer k ≥ 3. The vertices of G are assumed to be
v0, v1, . . . , vn−1. It outputs False, if G can be extended to a Pk-free counterex-
ample, i.e., if there exists a Pk-free counterexample G
∗ to Erdős-Gyárfás conjec-
ture with a vertex labeling v0, v1, . . . , vn∗−1 (where n∗ ≥ n) such that {vi, vj},
for 0 ≤ i < j ≤ n − 2, is an edge in G if and only if it is an edge in G
∗, and the
set of neighbors of vn−1 in G is a subset of its neighbors in G
∗. The algorithm
returns True otherwise. We say that a subset S of {v0, v1, . . . , vn−2} is a set of
potential safe neighbors of vn−1 if {vi, vn−1} is not an edge (for vi ∈ S) in G and
making all vertices in S neighbors of vn−1 does not create any forbidden cycles
(a cycle is forbidden if it is of length a power of 2). For each such set S of safe
potential neighbors of vn−1, we add the corresponding edges, and then check
whether the new graph is a counterexample or not. If a Pk-free counterexample
is found, we return False. If the updated graph G is not a counterexample and
it is Pk-free, then we ﬁnd a vertex, anchor_node with degree less than 3, and
make it adjacent to a new vertex vn. We call explore with this updated graph
G and k and return the result if it is False. If the recursive calls return True
for each set of potential safe neighbors, then return True at the end. We run
explore with Pk, k for k ≥ 3. If we obtain that the function returns True for
every 3 ≤ k ≤ t, then we claim that the conjecture is true for Pt-free graphs.
The function get_largest_low_degree_vertex returns the vertex
with largest index having a degree less than 3. It returns −1 if the minimum
degree is at least 3. By G[A], where A is a subset of vertices of G, we denote
the graph induced by A in G. If A = {u1, u2, . . . , up}, then G[u1, u2, . . . , up]
denotes the graph G[A]. A graph is a minimal counterexample, if none of its
proper induced subgraphs are counterexamples.

Lemma 1. Let G
∗ be a minimal counterexample to Erdős-Gyárfás conjecture,
such that G
∗ is Pk-free for an integer k ≥ 3. Let {v0, v1, . . . , vn∗−1} be the set
of vertices of G
∗. Let G be a graph with the vertex set {v0, v1, . . . , vn−1}, where
3 ≤ n ≤ n∗, such that the following conditions are satisﬁed.

i. The pair {vi, vj}, for 0 ≤ i < j ≤ n − 2, is an edge in G
∗ if and only if it
an edge in G.
ii. If vi, for 0 ≤ i ≤ n − 2, is a neighbor of vn−1 in G, then so is in G
∗.

Then explore(G, k) returns False.

Proof. We prove by induction on n∗ − n. For the base case, assume that n∗ − n =
0. Let S be the set of neighbors in G
∗ which are not neighbors of vn−1 in G.

Erdős-Gyárfás conjecture on graphs without long induced paths 3

Fig. 1. The algorithm
1: function explore(G, k) ⊲ V (G) = {v0, v1, . . . , vn−1}
2: for each set S of potential safe neighbors of vn−1 do
3: Add edge {vi, vn−1} to G, for each vi ∈ S.
4: if there is an induced Pk in G then
5: continue
6: end if
7: anchor_node ← get_largest_low_degree_vertex(G)
8: if anchor_node == -1 then
9: return False ⊲ G is a counterexample.
10: end if
11: Add a node vn and the edge {vn, anchor_node} to G
12: if not explore(G, k) then
13: return False
14: end if
15: Remove node vn from G.
16: Remove edge {vi, vn−1} from G, for each vi ∈ S.
17: end for
18: return True
19: end function

This set S is discovered in one iteration of the for loop (line 2). Then G is
updated (line 3) with the corresponding edges and the updated graph becomes
isomorphic to G
∗. Since G
∗ has no induced Pk and has minimum degree at least
3, the if condition in line 4 fails and that in line 8 succeeds and the algorithm
returns False.
Now, assume that n∗ − n > 0. As before, let S be the set of neighbors among
{v0, v1, . . . , vn−2} of vn−1 in G
∗ which are not neighbors of vn−1 in G. This set S
is discovered in one iteration of the for loop and the graph G is updated with the
corresponding edges. Therefore, {vi, vj}, for 0 ≤ i < j ≤ n − 1, is an edge in G
∗

if and only if it an edge in G. Since G
∗ is Pk-free and G is an induced subgraph
of G
∗, the if condition in line 4 fails. Since G
∗ is a minimal counterexample, G
must have a vertex with degree less than 3. Let i be the largest index such that
vi is a vertex of degree at most 2 in G
∗[v0, v1, . . . , vn−1]. Then vi is returned as
the anchor_node in line 7. Clearly, vi must have a neighbor vj in G
∗ such that
vj ∈ {vn, vn+1, . . . , vn∗−1}. Without loss of generality, assume that j = n. Now,
the vertex vn and the edge {vn, anchor_node} are added to G (line 11). Hence
the number of vertices in G got incremented by one. Further, G trivially satisﬁes
both the conditions in the statement of the lemma. Now the proof follows from
the induction hypothesis.

Corollary 1 follows from Lemma 1.

Corollary 1. Let G
∗ be a minimal counterexample to Erdős-Gyárfás conjecture
and let k be the smallest integer such that G
∗ is Pk-free but has an induced Pk−1.
Let G be the path v0v1 . . . vk−1. Then explore(G, k) returns False.

4 A. Hegde et al.

Theorem 1. Every P13-free graph with minimum degree at least 3 has a cycle
of length a power of 2.

Proof. We implemented explore and ran it with G, k, where G is the path
v0v1 . . . vk−1, for k from 3 to 13. In all the executions, the program returned
True. Now, the statement follows from Corollary 1 and the fact that P2-free
graphs have no edges.

We have a diﬀerent implementation of the algorithm in which only cycles of
lengths 4 and 8 are forbidden (see the branch ‘4-8-cycles’ in the repository [7]).
Using this, we obtain a stronger result for P12-free graphs.

Theorem 2. Every P12-free graph with minium degree at least 3 has a 4-cycle
or an 8-cycle.

This improves upon the result by Hu and Shen [8] that every P10-free graph
with minimum degree at least 3 has a 4-cycle or an 8-cycle.
We implemented [7] the algorithm
4 in C++. We also have a faster but
memory-intensive parallel implementation using Cilk [1] (see ‘cilk’ branch of
the repository). The time taken by these implementations when ran on a server
(2.6 GHz CPU, 72 cores) is shown in Table 1. The parallel execution was ter-
minated due to out of memory error when ran for k = 14. A serial execution
of the modiﬁed implementation used for Theorem 2 took 1 minute 39 seconds
for k = 11, and 3 hours 9 minutes for k = 12. We conducted extensive tests to
obtain evidences for the correctness of the implementation. The details are given
in the appendix.
 k ≤ 9 10 11 12 13
Time taken (C++) <0.2s 2s 32s 31m 32s 11h 56m
Time taken (Cilk) <0.05s 0.1s 1.4s 29s 17m 17s

Table 1. Time taken by an implementation of Algorithm 1 for various values of k.
Seconds, minutes, and hours are represented by ‘s’, ‘m’, and ‘h’ respectively.

The technique that we used is not helpful for proving the conjecture for H-
free graphs when H is not a path. Assume that H has a cycle. Since an inﬁnite
tree with minimum degree at least 3 neither has H as an induced subgraph nor

4 There are slight diﬀerences between the algorithm in Figure 1 and the implemented
algorithm. The diﬀerences are trivial and have no implications on the correctness. For
example, the implemented algorithm prints a counterexample, if exists, and exits,
instead of returning False. In the implemented algorithm, the arguments passed
to explore are G and an anchor_node, instead of G and k. This is because, k
is available as part of the graph object and passing anchor_node helps in eﬃcient
execution.
 Erdős-Gyárfás conjecture on graphs without long induced paths 5

has a cycle of length a power of 2 as a subgraph, the algorithm will run for ever.
If H is a tree but not a path, then we can come up with an H-free inﬁnite graph
by replacing each vertex of an inﬁnite tree (where every vertex has degree 3)
with a clique of 3 vertices and making each such vertex adjacent to exactly one
vertex in the clique formed for a neighbor. Since this graph is claw-free, every
induced tree in it is a path. We end with the following question: Is Algorithm 1
capable of resolving the conjecture for Pk-free graphs for every integer k ≥ 14?
In other words, is there an inﬁnite graph with minimum degree at least 3 neither
having an induced Pk nor having a cycle of length a power of 2?

Acknowledgement. We thank Nikhil Hegde for suggesting ways to boost the
performance of our code. We thank Paweł Rzążewski for helpful comments on
an initial draft of this paper.

References

1. Robert D Blumofe, Christopher F Joerg, Bradley C Kuszmaul, Charles E Leiserson,
Keith H Randall, and Yuli Zhou. Cilk: An eﬃcient multithreaded runtime system.
ACM SigPlan Notices, 30(8):207–216, 1995.
2. Dale Daniel and Stephen E Shauger. A result on the Erdős-Gyárfás conjecture in
planar graphs. Congressus Numerantium, pages 129–140, 2001.
3. Paul Erdös. Some old and new problems in various branches of combinatorics.
Discret. Math., 165-166:227–231, 1997.
4. Yuping Gao and Songling Shan. Erdős-Gyárfás conjecture for P8-free graphs.
Graphs Comb., 38(6):168, 2022.
5. Mohammad Hossein Ghaﬀari and Zohreh Mostaghim. Erdős–Gyárfás conjecture
for some families of cayley graphs. Aequationes mathematicae, 92:1–6, 2018.
6. Christopher Carl Heckman and Roi Krakovski. Erdös-Gyárfás conjecture for cubic
planar graphs. Electron. J. Comb., 20(2):7, 2013.
7. Anand Shripad Hegde, R. B. Sandeep, and P. Shashank. Veriﬁer for Erdős–Gyárfás
conjecture on Pk-free graphs, October 2024. https://github.com/rbsandeep/Erdos-
Gyarfas.
8. Zhiquan Hu and Changlong Shen. The Erdős-Gyárfás conjecture holds for P10-free
graphs. Discret. Math., 347(12):114175, 2024.
9. Hong Liu and Richard Montgomery. A solution to Erdős and Hajnal’s odd cycle
problem. Journal of the American Mathematical Society, 36(4):1191–1234, 2023.
10. Klas Markström. Extremal graphs for some problems on cycles in graphs. Univer-
sity of Umeå, Department of Mathematics, 2002.
11. P Salehi Nowbandegani and H Esfandiari. An experimental result on the Erdős-
Gyárfás conjecture in bipartite graphs. In 14th Workshop on Graph Theory CID,
pages 18–23, 2011.
12. Stephen E Shauger. Results on the Erdős-Gyárfás conjecture in K1,m-free graphs.
Congressus Numerantium, pages 61–66, 1998.

6 A. Hegde et al.

Appendix: Correctness testing

The C++ program implementing the algorithm can be found at [7]. We con-
ducted various tests to verify the correctness of the implementation. They are
listed below. The outcome of the tests were as expected and we believe that it
provides strong evidences for the correctness of the implementation.

1. The output of our program is in accordance with the result obtained in [8]
for P10-free graphs.
2. By introducing logs and visualization of intermediate graphs, we manually
veriﬁed the execution of the program for 3 ≤ k ≤ 5. The output was as
expected. More details can be found in the ‘logs’ branch of the repository.
3. We conducted unit tests for major functions in the program. For each such
functions, we tested with inputs where the corresponding outputs are known
to us. More details can be found in the ‘tests’ branch of the repository.
4. We obtained all the four cubic graphs with minimum number (24) of vertices
(found by Markström [10]) having no 4-cycle and no 8-cycle but having a 16-
cycle by guiding the execution with proper values of k and by restricting the
degree to be 3. Only one of them, known as Markström graph (see Figure 2),
is planar. It is P18-free but has an induced P17. More details can be found
in the ‘special-graphs’ branch of the repository.

Fig. 2. Markström graph: the unique smallest cubic planar graph having no 4-cycle
and no 8-cycle, but having a 16-cycle. The bold (purple) edges show a 16-cycle.
