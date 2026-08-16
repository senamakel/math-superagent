<!-- source: https://arxiv.org/pdf/1109.5398v3 | converted from PDF -->

arXiv:1109.5398v3  [math.CO]  7 Feb 2013
Discussiones Mathematicae1 Graph Theory xx (xxxx) 1–72
 ON THE ERD ˝OS-GY ´ARF ´AS CONJECTURE IN CLAW-FREE3 GRAPHS4
 Pouria Salehi Nowbandegani5
 Department of Mathematics,6 Shiraz University,7 Shiraz 71454, Iran8
 e-mail: pouria.salehi@gmail.com9
 Hossein Esfandiari10
 Department of Computer Science,11 University of Maryland College Park,12 College Park, MD 20742,13
 e-mail: hossein@cs.umd.edu14
 Mohammad Hassan Shirdareh Haghighi15
 Department of Mathematics,16 Shiraz University,17 Shiraz 71454, Iran18
 e-mail: shirdareh@susc.ac.ir19
 and20
 Khodakhast Bibak21
 Department of Combinatorics and Optimization,22 University of Waterloo,23 Waterloo, Ontario, Canada N2L 3G124
 e-mail: kbibak@uwaterloo.ca25
 Abstract26 The Erd˝os-Gy´arf´as conjecture states that every graph with minimum27 degree at least three has a cycle whose length is a power of 2. Since this28 conjecture has proven to be far from reach, Hobbs asked if the Erd˝os-Gy´arf´as29 conjecture holds in claw-free graphs. In this paper, we obtain some results30 on this question, in particular for cubic claw-free graphs.31 Keywords: Erd˝os-Gy´arf´as Conjecture, Claw-Free Graphs, Cycles.32 2010 Mathematics Subject Classiﬁcation: C5038, C5038.33
 2 P. Salehi, H. Esfandiari, M. H. Shirdareh and Kh. Bibak

1. Introduction34
 All graphs in this paper are assumed to be simple, that is, without any loops and35 multiple edges. Let us ﬁrst recall here brieﬂy some notation and terminology we36 will need in this paper. We denote by δ = δ(G) the minimum degree of the the37 vertices in the graph G = (V, E). A uv-path is a path having the vertices u and38 v as its ends. The length of a path P (or a cycle C) is denoted by l(P ) (resp.39 l(C)). Also, we denote the distance between the vertices u and v by d(u, v), that40 is the length of a shortest uv-path. A graph that does not contain a particular41 graph H as an induced subgraph is called H-free. The complete bipartite graph42 K1,3 is referred to as a claw ; so a graph is called claw-free if it does not have K1,343 as an induced subgraph. A triangle is a cycle of length three. A chord of a cycle44 C is an edge between two vertices of C which are not adjacent in C. By a hole45 we mean a chordless cycle of length at least four. A hole of length n is called an46 n-hole.47
 Several questions on cycles in graphs have been posed by Erd˝os and his48 colleagues (see, e.g., [1]). In particular, in 1995 Erd˝os and Gy´arf´as [4] asked:49
 If G is a graph with minimum degree at least three, does G have a cycle whose50 length is a power of 2?51
 This is known as the Erd˝os-Gy´arf´as conjecture. In fact, Erd˝os and Gy´arf´as52 [4] said that “we are convinced now that this is false and no doubt there are53 graphs for every r every vertex of which has degree ≥ r and which contain no54 cycle of length 2k, but we never found a counterexample even for r = 3”.55 There seems to be very little published on the Erd˝os-Gy´arf´as conjecture.56 Markstr¨om [5] (via computer searches) asserted that any cubic counterexample57 must have at least 30 vertices. Salehi Nowbandegani and Esfandiari [6] prove58 that any bipartite counterexample must have at least 32 vertices.59 More generally, Erd˝os asked does there exist an integer sequence a1, a2, a3, · · ·60 with zero density, and a constant c such that every graph with average degree61 at least c contains a cycle of length ai for some i. This question is answered62 aﬃrmatively by Verstra¨ete [8].63 Hobbs asked if the Erd˝os-Gy´arf´as conjecture holds in claw-free graphs [3].64 Shauger [7] proved the conjecture for K1,m-free graphs having minimum degree65 at least m + 1 or maximum degree at least 2m − 1. Also, Daniel and Shauger66 [3] proved it for planar claw-free graphs. In this paper, we investigate claw-free67 graphs with δ ≥4 and cubic claw-free graphs.68
 2. Two-power Cycle Lengths in Claw-free Graphs69
 Our ﬁrst theorem concerns claw-free graphs with δ ≥ 3.70
 On the Erd˝os-Gy´arf´as Conjecture in Claw-free Graphs 3

Theorem 1. Suppose that G is a claw-free graph with δ ≥ 3. Then G has a cycle71 whose length is 2k, or 3 · 2k, for some positive integer k.72
 To prove Theorem 1 we need the following lemma.73
 Lemma 2. Let G be a graph with δ ≥ 3. If G does not have C4 as a subgraph,74 then for some n ≥ 5, it has an n-hole.75
 Proof. It is known that every graph with δ ≥ 2 contains a cycle of length at76 least δ + 1 (see, e.g., [2, Exercise 2.1.5]). Thus G has a cycle D1 of length n1 ≥ 5.77 If n = 5, D1 must clearly be chordless. If n > 5, and D1 has no chord, we are78 ﬁnished, so suppose D1 has a chord. The chord separates D1 into two shorter79 cycles, non of which have length 4, by assumption. Thus at least one of these80 two cycles, say D2, must have length 5≤ n2 < n1. Since G is ﬁnite, we must by81 repeating this argument eventually ﬁnd a chordless cycle Dk of length nk ≥5.82
 Deﬁnition. We call an edge of a graph triangulated if it is contained in a triangle.83 Also if such a triangle is unique, we call the edge uniquely triangulated.84
 Now we are ready to prove Theorem 1.85
 Proof of Theorem 1. If G has a cycle of length four, the theorem holds, with86 k =2. We may therefore assume that G does not contain any C4. Thus, by87 Lemma 2, for some n ≥ 5, G has an n-hole. Let C : a1a2 . . . asa1, s ≥ 5, be a88 smallest hole in G. Since δ ≥ 3 and C is a hole, each vertex of C has a neighbour89 in G − V (C). For i, (1 ≤ i ≤ s), suppose that aibi ∈ E(G), where ai ∈ C and90 bi ∈ V (G) \ V (C). Then either ai−1bi ∈ E(G), or ai+1bi ∈ E(G), because G is91 claw-free. Now we show that bi ̸= bj if |j − i| ≥ 2. To get a contradiction, ﬁx i92 and let aj be the ﬁrst vertex of C after ai such that bi = bj = b, |j − i| ≥ 2. If93 j − i = 2, then we get the C4 : aiai+1ai+2bai, which is absurd. If |j − i| > 2, then94 we get the hole ai+1 . . . ajbai+1 which is certainly smaller than C (note that we95 don’t reject the case that this hole may be a C4).96 Therefore, it follows that every other edge of C is uniquely triangulated;97 we mark them. Moreover, the third vertices of the corresponding triangles are98 disjoint. Note also that s is even. Consequently, we ﬁnd cycles of lengths s, s +99 1, . . . , 3
2 s by traversing C such that as we reach a marked edge, we pass it directly100 or through the third vertex of its corresponding triangle. Since either there exists101 a 2k or a 3 · 2k−1 between s and 3
2 s, the proof is complete.102
 As mentioned above, Shauger [7] proved the Erd˝os-Gy´arf´as conjecture for103 K1,m-free graphs having minimum degree at least m + 1 or maximum degree at104 least 2m − 1. Theorem 5 improves on the result of Shauger in claw-free graphs.105 First we state the following proposition. We omit the easy proof.106
 4 P. Salehi, H. Esfandiari, M. H. Shirdareh and Kh. Bibak

Proposition 3. In a 4-regular claw-free graph which does not contain C4, every107 edge is uniquely triangulated.108
 Lemma 4. Let G be a 4-regular claw-free graph which does not contain C4 and v109 be a vertex of G. Let C be a smallest n-hole in G containing v, n ≥ 5. Then for110 every edge xy of C, the third vertex z = z(xy) of the corresponding triangle of xy111 is out of C. Furthermore, if uw ̸= xy are two edges of C, then z(uw) ̸= z(xy).112
 Proof. First note that since C is a hole, for every edge xy in C, z = z(xy) /∈ C.113 Let uw and wx be two consecutive edges in C. If z = z(uw) = z(wx), then we get114 the C4 : uwxzu. Hence z(uw) ̸= z(wx). Suppose that uw and xy are two non-115 consecutive edges in C and suppose C traverses the vertices in order u, w, x, y,116 and then v. Let Q be the yvu segment of C. Now if z = z(uw) = z(xy), then117 the cycle uQyzu is a smaller hole containing v; unless u and y are adjacent in C118 (and hence v is one of them). But in this case, we see that uzxyu is a C4 in G.119 This contradiction shows that z(uw) = z(xy) for uw ̸= xy is impossible.120
 Theorem 5. Let G be a claw-free graph with δ ≥ 4, which does not contain C4.121 Then every non-cut vertex of G lies on a cycle whose length is a power of 2.122
 Proof. Since δ ≥ 4 and G is claw-free, if G has a vertex with degree at least123 5, then this vertex lies on a C4; so we can assume that G is 4-regular. Suppose124 that v is a non-cut vertex of G and let w, x, y, and u be its neighbours. Hence,125 G − v is connected. In view of G is claw-free, we can assume that wu, xy ∈ E(G).126 Let P1, P2, P3, and P4 be the shortest wy-path, wx-path, xu-path, and yu-path127 in G − v, respectively. Also, without loss of generality assume that l(P1) =128 min{l(P1), l(P2), l(P3), l(P4)}. The path P1 together with the edges vw and vy129 make a cycle C. Clearly, l(P1) > 1, otherwise ywuvy will be a C4. Therefore,130 l(C) = s ≥ 5. Since P1 was the shortest path among P1, P2, P3, and P4, we see131 that neither x nor u are in P1 and, in fact, C is the shortest non-triangle hole132 containing the vertex v; for if v lies on another non-triangle shorter hole, then two133 of its neighbours would have distance less than l(P1) in G − v. By Lemma 4, each134 edge of C is uniquely triangulated such that the third vertex of its corresponding135 triangle is not on C and this correspondence is one to one. Since l(C) = s, then136 G contains cycles of lengths s, s + 1, . . . , 2s. For, as in the proof of theorem 1,137 when we traverse the vertices of C, we can either pass the two ends of every edge138 directly or through the third vertex of its corresponding triangle.139 This implies that G has a cycle containing v whose length is 2k, for some140 k ≥ 3.141

142
 On the Erd˝os-Gy´arf´as Conjecture in Claw-free Graphs 5

3. The Erd˝os-Gy´arf´as Conjecture in Cubic Claw-free Graphs143
 In this section, we investigate the Erd˝os-Gy´arf´as conjecture in cubic claw-free144 graphs. Indeed, we discuss on the cubic claw-free graphs for which the Erd˝os-145 Gy´arf´as conjecture possibly does not hold.146 Suppose that G is a cubic claw-free graph that does not contain C4. Let v be147 an arbitrary vertex of G, and let its neighbours be x, y, and z. Since G is claw-free,148 so we can assume that xy ∈ E(G). Thus, xz, yz /∈ E(G); otherwise a C4 appears.149 Let x1 and y1 be respectively the other neighbours of x and y. Easily we see that150 x1 ̸= y1. Therefore, for every vertex there exists a unique triangle containing151 it, such that the other neighbours of its vertices are distinct. Hence G consists152 of some vertex-disjoint triangles which are connected by a perfect matching of153 G. Furthermore, if two vertices from two triangles are matched, then there is154 no more link between these two triangles, again because we have no C4 in G.155 This means if we look locally at the graph, we see a triangle together with three156 appended edges, such that these edges connect to three disjoint triangles. Now157 deﬁne ˆ(G) to be the graph whose vertices are triangles of G and two vertices158 are adjacent in ˆG whenever their corresponding triangles in G are linked by an159 edge. The graph ˆG is then a simple cubic graph. We can imagine ˆG as a graph160 obtained from G by shrinking each triangle to a vertex.161 Conversely, we can start from a simple cubic graph ˆG and replacing each162 vertex v with a triangle T ; linking the three vertices of T to the three triangles163 corresponding to the three neighbours of v. This procedure results in a cubic164 claw-free graph G without C4. To sum up, we have the following proposition.165
 Proposition 6. The mapping G ↔ ˆG is a one to one correspondence between166 simple cubic graphs and simple cubic claw-free graphs without C4.167
 Corollary 7. If ˆG contains a cycle of length k, then this cycle provides cycles of168 lengths 2k, 2k + 1, . . . , 3k in G.169
 Proof. Consider a cycle ˆC of length k in ˆG. The subgraph S of G corresponding170 to ˆC consists of a cycle of length 2k such that every other edge of it is triangulated.171 Hence we can ﬁnd cycles of lengths 2k, 2k + 1, . . . , 3k in S.172
 Based on proposition 6 and Corollary 7, we think the following conjecture is173 true.174
 Conjecture 8. Every cubic graph contains a cycle of length l such that 2l ≤175 2k < 3l, for some positive integer k.176
 If this conjecture holds, it will lead to a proof of the Erd˝os-Gy´arf´as conjecture177 in cubic claw-free graphs. Also note that this conjecture can be easily deduced178
 6 P. Salehi, H. Esfandiari, M. H. Shirdareh and Kh. Bibak

from the Erd˝os-Gy´arf´as conjecture. But for simplicity, we restrict ourselves to179 cubic graphs, and the length of the desired cycle has a very wide range.180 At the end, we investigate minimal cubic claw-free graphs which possibly181 have no cycle with length a power of 2.182
 Theorem 9. Any counterexample to the Erd˝os-Gy´arf´as conjecture in cubic claw-183 free graphs must have at least 114 vertices.184
 Proof. Let G be a claw-free cubic graph of order 3n. Then ˆG (deﬁned in propo-
sition 6) is a cubic graph of order n. By corollary 7, if ˆG contains a cycle of
length l, where l ∈ {2, 3, 4, 6, 7, 8}, then the Erd˝os-Gy´arf´as conjecture holds for
G. So let us assume that ˆG does not contain such cycles. Let v0 be a vertex of
ˆG. We consider {v0} as level 0, and deﬁne level i, i ≥ 1, as the set

Li = {v ∈ V ( ˆG) : d(v, v0) = i}.

Clearly, L1 is an independent set. It is easy to see that the subgraph induced by185 L2 has at most one edge. One can check that if the subgraph induced by L2 has186 no edge, then the subgraph induced by L3 has at most three edges, and if the187 subgraph induced by L2 has one edge, then the subgraph induced by L3 has at188 most one edge. No two elements of L3 have common neighbours in L4, because189 otherwise, ˆG contains the cycles of lengths 2, 4, 6, or 8. An easy calculation190 shows that ˆG has at least 38 vertices. Consequently, any counterexample for the191 Erd˝os-Gy´arf´as conjecture must have at least 3 × 38 = 114 vertices.192
 Acknowledgments193
 The authors would like to thank anonymous referees for helpful mathematical194 and grammatical comments.195
 References196
 [1] J. A. Bondy, Extremal problems of Paul Erd˝os on circuits in graphs, In Paul197 Erd˝os and his Mathematics, II , Bolyai Soc. Math. Stud., 11, Jnos Bolyai198 Math. Soc., Budapest (2002), 135–156.199
 [2] J. A. Bondy and U.S.R. Murty, Graph Theory, Springer-Verlag, New York200 (2008).201
 [3] D. Daniel and S. E. Shauger, A result on the Erd˝os-Gy´arf´as conjecture in202 planar graphs, Congr. Numer. 153 (2001), 129–140.203
 [4] P. Erd˝os, Some old and new problems in various branches of combinatorics,204 Discrete Math., 165/166 (1997), 227–231.205
 On the Erd˝os-Gy´arf´as Conjecture in Claw-free Graphs 7

[5] K. Markstr¨om, Extremal graphs for some problems on cycles in graphs,206 Congr. Numer., 171 (2004), 179-192.207
 [6] P. Salehi Nowbandegani and H. Esfandiari, An experimental result on the208 Erd˝os-Gy´arf´as conjecture in bipartire graphs. 14th Workshop on graph the-209 ory (CID), September 18-23, 2011, Szklarska Poreba, Poland.210
 [7] S. E. Shauger, Results on the Erd˝os-Gy´arf´as conjecture in K1,m-free graphs,211 Congr. Numer. 134 (1998), 61–65.212
 [8] J. Verstra¨ete, Unavoidable cycle lengths in graphs, J. Graph Theory, 49(2)213 (2005), 151–167.214

215
