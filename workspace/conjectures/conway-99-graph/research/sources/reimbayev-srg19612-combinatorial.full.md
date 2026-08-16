<!-- source: https://arxiv.org/html/2511.06569v1 | converted from HTML -->

Nonexistence of ⁢ s r g ( 19 , 6 , 1 , 2 ) : Combinatorial Proof

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2511.06569v1 [math.CO] 09 Nov 2025

# Nonexistence of s ​ r ​ g ​ ( 19, 6, 1, 2) srg(19,6,1,2): Combinatorial Proof

Reimbay Reimbayev

###### Abstract

An s ​ r ​ g ​ ( 19, 6, 1, 2) srg(19,6,1,2) is the graph with the smallest parameter set in the family of strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2 for which the respective graph doesn’t exist. The proof of that fact is based on algebraic arguments, particularly, on the Integrality Test, the very usefull tool for studying strongly regular graphs. To our best knowledge, there have not been proofs of pure combinatorial nature. In this short paper, we have decided to fill in this gap.

In the family of strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2, the graph s ​ r ​ g ​ ( 19, 6, 1, 2) srg(19,6,1,2) is not a ‘superstar’ like an s ​ r ​ g ​ ( 99, 14, 1, 2) srg(99,14,1,2), which is under the search for at least half a century to the moment [1]. Moreover, it doesn’t even exist - a well established fact. But this is the first graph that doesn’t exist in the line of possible ones. For the first two possible values for the parameters n n and k k, respectively the order of the graph and valency of its vertices, the graphs exist: K 3 K_{3} (for k = 2 k=2) - a complete graph on three vertices , P 9 P_{9} (for k = 4 k=4) - Paley graph on nine vertices.

For the parameter k = 6 k=6, which is the next possible, i.e. our case, the graph doesn’t exist due to the Integrality Test, an incredibly useful tool in studying strongly regular graphs. The tool that uses multiplicities of eigenvalues of an adjacency matrix of a graph to determine its nonexistence. But Integrality Test is only a necessary condition for existance of a strongly regular graph and thus there are still some cases that slips through it, namely for the parameters of k = 14, 22, 112, 994. k=14,22,112,994.

Out of these four graphs that pass the Integrality Test, only for k = 22 k=22 the graph has been shown to exist [2]. For the other ones, the question of existence has not been resolved. For that reason, we think, any attempt to prove the existance of such graphs without referral to Integrality Test might be useful.

By definition, the graph is strongly regular if a pair of its vertices has exactly λ \lambda common neighbors given they are adjacent, or μ \mu common neighbors otherwise [3, 4]. Another way of defining strongly regular graphs, perhaps more precise as it cuts away some trivial cases like complete graphs, is by using spectral graph theory, by which the finite graph is strongly regular if its spectrum consists of exactly three eigenvalues, one of which is k k with multiplicity one [5].

For simplicity, let us call an s ​ r ​ g ​ ( 19, 6, 1, 2) srg(19,6,1,2) further on just G G. Below is the formal statement we are going to prove.

###### Theorem 1.

srg(19,6,1,2) doesn’t exist.

###### Proof.

Choose any triangle, K 3 K_{3}, with vertices a, b, c a,b,c from G = s ​ r ​ g ​ ( 19, 6, 1, 2) G=srg(19,6,1,2). We will denote A = { v ∈ G | v a ∈ E ( G), v ≠ b, c }, B = { v ∈ G | v b ∈ E ( G), v ≠ a, c }, C = { v ∈ G | v c ∈ E ( G), v ≠ a, b } A=\{v\in G|va\in E(G),v\neq b,c\},B=\{v\in G|vb\in E(G),v\neq a,c\},C=\{v\in G|vc\in E(G),v\neq a,b\}, the sets of vertices adjacent to a given vertex of the original triangle except the vertices of the triangle.

One more set is needed W = V ⁡ ( G) ∖ ( A ∪ B ∪ C ∪ { a, b, c }) W=V(G)\setminus(A\cup B\cup C\cup\{a,b,c\}), the set of vertices at distance 2 from triangle { a, b, c } \{a,b,c\}. Notice that { a, b, c } \{a,b,c\}, A, B, C A,B,C, and W W - is a partition of V ⁡ ( G) V(G), and | A | = | B | = | C | = | W | = 4 |A|=|B|=|C|=|W|=4. Now, here is the goal we want to achieve: to show that an induced subgraph on vertices A ∪ B ∪ C, ( G ⁡ [A ∪ B ∪ C]) A\cup B\cup C,(G[A\cup B\cup C]) cannot satisfy both λ = 1 \lambda=1 (Condition I) and μ = 2 \mu=2 (Condition II). First, we show that it doesn’t contain triangles. Vertex w w from W W is adjacent to exactly 2 2 vertices from A A, as w ​ a ∉ E ⁡ ( G) wa\notin E(G). The same hold true regarding B B and C C (Figure 1). But d ​ e ​ g ​ ( w) = 6 deg(w)=6, and an induced subgraph on W is an empty graph. That means there are exactly 12 ​ ( 3 ⋅ 4) 12(3\cdot 4) triangles with one vertex on W W and two on A ∪ B ∪ C A\cup B\cup C. In total there 19 triangles in G ( n ​ k 6 \frac{nk}{6}, Proposition 3 [6]), out of which 7 have at least one vertex from { a,b,c}. Thus, 19 − 7 − 12 = 0 19-7-12=0, and A ∪ B ∪ C A\cup B\cup C has no triangles.

[image: Refer to caption] Figure 1: The structure of s ​ r ​ g ​ ( 19, 6, 1, 2) srg(19,6,1,2)

For any a ~ ∈ A \tilde{a}\in A there exists unique b ~ ∈ B \tilde{b}\in B such that a ​ b ~ ∈ E ⁡ ( G) \tilde{ab}\in E(G). This is due to Condition II because a ~ ​ b ∉ E ⁡ ( G) \tilde{a}b\notin E(G). The function given by this adjacency relationship, say f: A → B f:A\rightarrow B is bijective. Suppose not. Then there exist b ~ 1 \tilde{b}_{1} and b ~ 2 \tilde{b}_{2} both adjacent to a ~ ∈ A \tilde{a}\in A. But then a ~ \tilde{a} and b b, two non-adjacent vertices, have three common neighbors, - a a, b ~ 1, b ~ 2 \tilde{b}_{1},\tilde{b}_{2}, which is impossible. Similarly, there cannot be a ~ 1, a ~ 2 ∈ A \tilde{a}_{1},\tilde{a}_{2}\in A and b ~ ∈ B \tilde{b}\in B, such that a ~ 1 ​ b ~ ∈ E ⁡ ( G) \tilde{a}_{1}\tilde{b}\in E(G) and a ~ 2 ​ b ~ ∈ E ⁡ ( G) \tilde{a}_{2}\tilde{b}\in E(G). We can continue in this way and set a bijection B → C B\rightarrow C, then another one C → A C\rightarrow A. Bijectivity of the relationship A → B → C → A A\rightarrow B\rightarrow C\rightarrow A, or simply permutation of vertices of A A, makes the induced subgraph on A ∪ B ∪ C A\cup B\cup C regular of degree three. Not two because we have to take into account pairwise connectedness of vertices in A A, as well as in B B and C C. Thus, without these edges, G ⁡ [A ∪ B ∪ C] G[A\cup B\cup C] consists of cycles of length 3, 6, 9, or 12. The cycles of lenght 3, triangles, are not possible as we already agreed before. By the same reason C 9 C_{9} is also impossible, otherwise G ⁡ [A ∪ B ∪ C] = C 9 + C 3 G[A\cup B\cup C]=C_{9}+C_{3} plus additional inner chords, which gives us a union of two cycles (and additional chords or bridges), one of which is a triangle. There has left two cases, which we consider separately.

Case 1: G ⁡ [A ∪ B ∪ C] = C 6 + C 6 G[A\cup B\cup C]=C_{6}+C_{6} plus chords and/or connectors. Consider a 6-cycle, with possible chords that we will ignore altogether, a 1 ​ b 1 ​ c 1 ​ a 2 ​ b 2 ​ c 2 a_{1}b_{1}c_{1}a_{2}b_{2}c_{2}, where a i ∈ A, b i ∈ B, c i ∈ C, i = 1, 2 a_{i}\in A,b_{i}\in B,c_{i}\in C,i=1,2. Each edge is a base of a triangle with the third vertex on W = { w 1, w 2, w 3, w 4 } W=\{w_{1},w_{2},w_{3},w_{4}\}. The goal is to show that the proper distribution of the vertices of the given six triangles among four elements of W W is impossible. Denote w 1 w_{1} the vertex of the first triangle based on the edge a 1 ​ b 1 a_{1}b_{1} and move anti-clockwise as depicted on the Figure 2 (case 1). We cannot chose w 1 w_{1} for the next triangle with basis on b 1 ​ c 1 b_{1}c_{1} or else the edge b 1 ​ w 1 b_{1}w_{1} belongs to two trianlges. Chose w 2 w_{2}. Next triangle based on c 1 ​ a 2 c_{1}a_{2} necesseraly should have a vertex distinct from both previous ones: w 1 w_{1} and w 2 w_{2}. Otherwise b 1 ​ c 1 b_{1}c_{1} belongs to two triangles b 1 ​ c 1 ​ w 1 b_{1}c_{1}w_{1} and b 1 ​ c 1 ​ w 1 b_{1}c_{1}w_{1}. So w 3 ≠ w 1, w 2 w_{3}\neq w_{1},w_{2}.

[image: Refer to caption] Figure 2: Illustration for the Theorem 1: left - for case 1, right - for case 2.

Last step. Consider triangle a 2 ​ b 2 ​ w 4 a_{2}b_{2}w_{4}, where w 4 ≠ w 2, w 3 w_{4}\neq w_{2},w_{3} due to the same reasoning as before. But w 4 ≠ w 1 w_{4}\neq w_{1} as well! Assume not, and w 4 = w 1 w_{4}=w_{1}. We know that every vertex belongs to exactly three triangles ( k = 6 k=6). For w 1 w_{1} those are w 1 ​ a 1 ​ b 1 w_{1}a_{1}b_{1}, w 1 ​ a 2 ​ b 2 w_{1}a_{2}b_{2}, and w 1 ​ x ​ y w_{1}xy, where x x and y y are both belong to C C. But that is not possible, otherwise the edge x ​ y xy belongs to w 1 ​ x ​ y w_{1}xy and c ​ x ​ y cxy, two distinct triangles at the same time. We run out of vertices from W W to assign for the next triangle in the line.

Case 2: G ⁡ [A ∪ B ∪ C] = C 12 G[A\cup B\cup C]=C_{12} plus chords. The only possible way of distributing the vertices of W W is shown in the figure. Again, this is due to the same reasons as in Case 1. We have also established earlier that G ⁡ [W] = K 4 ¯ G[W]=\overline{K_{4}} is an empty graph. Thus w 1 ​ w 4 ∉ E ⁡ ( G) w_{1}w_{4}\notin E(G). But this two vertices now have three common neighbors, namely a 1, b 2, c 3 a_{1},b_{2},c_{3}, which is not possible. That completes the proof.

∎

Similarly, it can be proved, with a bit more work, for the next parameter of k k. Instead, using the Integrality Test [7, 8] eliminates decisively all the graphs up to k = 14 k=14, which is also called Conway-99 graph and is among five problems Conway has offered to solve [1]. Three more values of k k, k = 22,112,994 k=22,112,994, also pass the Integrality Test, out of which one for k = 22 k=22, to ones amusement, has been already constructed [2].

In conclusion, in this short paper we have proved nonexistance of the lowest possible graph from the family of strongly regular graphs with parameters λ = 1 \lambda=1 and μ = 2 \mu=2 using strictly combinatorial arguments. Although, the more important graph from the same family is an s ​ r ​ g ​ ( 99, 14, 1, 2) srg(99,14,1,2), existance of which is still undefined, we do not think that our work is a futile exercise but rather an attempt to look from another perspective on the problem. The search for an s ​ r ​ g ​ ( 99, 14, 1, 2) srg(99,14,1,2) is still an on-going process.

## References

- [1] Conway, John (Update 2017), *Five $ 1,000 Problems*, On-Line Encyclopedia of Integer Sequences, OEIS sequance A248380.
- [2] Berlekamp, E.R.; Van Lint, J.H.; Seidel, J.J.(1973), *A strongly regular graph derived from the perfect ternary Golay code*, A survey of combinatorial theory, Amsterdam, 25-30.
- [3] Royle, Gordon, *List of Large Graphs and Families*, http://people.csse.uwa.edu.au/gordon/remote/srgs/
- [4] Brouwer, Andries E., *Parameters of Strongly Regular Graphs*, https://www.win.tue.nl/~aeb/graphs/srg/srgtab.html
- [5] Brouwer, Andries; van Maldeghem, Hendrik (2022), *Strongly Regular Graphs*, Cambridge University Press.
- [6] Reimbayev, R (2024), *The Lower Bound for Number of Hexagons in Strongly Regular Graphs with Parameters λ = 1 \lambda=1 and μ = 2 \mu=2*, ArXiv
- [7] West, Douglas B. (2000) *Introduction to Graph Theory*, Pearson Education Limited, 2-nd ed.
- [8] Cvetcovic, Dragos; Rowlinson, Peter; Simic, Slobodan (2010), *An Introduction to the Theory of Graph Spectra*, Cambridge University Press


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
