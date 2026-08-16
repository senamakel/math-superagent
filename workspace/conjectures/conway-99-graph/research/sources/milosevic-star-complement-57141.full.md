<!-- source: https://www1.pmf.ni.ac.rs/pmf/publikacije/filomat/2008/22-2-2008/f22-2-5.pdf | converted from PDF -->

Faculty of Sciences and Mathematics, University of Niˇs, Serbia
Available at: http://www.pmf.ni.ac.yu/filomat

Filomat 22:2 (2008), 53–57

AN EXAMPLE OF USING STAR COMPLEMENTS
IN CLASSIFYING STRONGLY REGULAR GRAPHS∗

Marko Miloˇsevi´c

Abstract

In this paper we show how the star complement technique can be used to
reprove the result of Wilbrink and Brouwer that the strongly regular graph
with parameters (57, 14, 1, 4) does not exist.

1 Introduction

Let G = (V, E) be a ﬁnite, undirected, simple graph. For two vertices u, v, we write
u ∼ v if they are adjacent in G. The neighborhood N (u) of u is the set of neighbors
of u. The closed neighborhood N [u] is the set N (u) ∪ u.
The graph G is a strongly regular with parameters (n, k, λ, µ) if G is k-regular
on n vertices, such that any two adjacent vertices have λ common neighbors, and
any two nonadjacent vertices have µ common neighbors. Obviously, in such a graph
the neighborhood of each vertex induces a λ–regular graph on k vertices.
In 1983, Wilbrink and Brouwer proved that the strongly regular graph with
parameters (57, 14, 1, 4) does not exist. Here, a self-contained proof of the nonex-
istence of this graph is given, using linear algebra and spectral graph theory, more
precisely the technique of star complements. This technique was developed by
Cvetkovi´c, Rowlinson and Simi´c in a series of papers (see, e.g., [1], [2], [3], [5], [6]).
Let ξ be an eigenvalue of G with multiplicity m. A star set for ξ in G is a set
X ⊂ V (G) of m vertices such that ξ is not an eigenvalue of G − X, the subgraph
of G induced by X = V (G) \ X. The graph G − X is called a star complement
for ξ in G. If X is a star set for an eigenvalue ξ /∈ {−1, 0} of G, then X is a
location-dominating set in G, meaning that the X–neighborhoods of vertices in X
are distinct and nonempty [1].
The following theorem is known as the Reconstruction Theorem.

∗This work was supported by the research grant 144026 of the Serbian Ministry of Science and
Environmental Protection.
2000 Mathematics Subject Classiﬁcations. 05E30, 05C50.
Key words and Phrases. Strongly regular graph; Star complement; Graph eigenvalues; Graph.
Received: July 27, 2008
Communicated by Dragan Stevanovi´c

54 Marko Miloˇsevi´c

Theorem 1 ([1]) Let X be a set of vertices in graph G and suppose that G has
adjacency matrix ( AX BT

B C
 )

where AX is adjacency matrix of the subgraph induced by X. Then X is a star set
for ξ in G if and only if ξ is not an eigenvalue of C and

ξI − AX = BT (ξI − C)
−1B. (1)

Thus, if we know ξ, B and C, we can reconstruct the whole graph G. If we
denote the columns of B by bu (u ∈ X) and equate corresponding matrix entries
in (1), we obtain the following result

Corollary 2 ([5]) If X is a star set for ξ then ⟨bu, bu⟩ = ξ, for all u ∈ X, and
⟨bu, bv⟩ ∈ {−1, 0} where ⟨bu, bv⟩ = bT
u (ξI − C)−1 bv. If ⟨bu, bu⟩ = −1, then
u ∼ v, and if ⟨bu, bu⟩ = 0, then u ̸∼ v.

One can now deﬁne the compatibility graph Comp(C, ξ) having as vertices all
(0, 1)–vectors b which satisfy ⟨b, b⟩ = ξ, with two vertices b
′ and b
′′ adjacent if
and only if ⟨b′, b
′′⟩ ∈ {−1, 0}. Then, for each graph G that has G − X as a star
complement for ξ, there is a clique in Comp(C, ξ) that completely determines G.
As for the strongly regular graph with parameters (57, 14, 1, 4), these param-
eters determine the spectrum [14, 238, −518], where exponents denote multiplicity.
Therefore, to apply the star complements technique, one has to ﬁnd an induced
subgraph on 19 vertices that does not have 2 as an eigenvalue.
Let G be the strongly regular graph with parameters (57, 14, 1, 4), and let u be
an arbitrary vertex of G. The closed neighborhood N [u] induces the windmill W14.
Each vertex v ̸∈ N [u] has exactly four neighbors in common with the vertex u. Any
two connected vertices from N (u) have u as their unique common neighbor, so they
do not have any more common neighbors. Therefore we may assume, without loss
of generality, that the graph H induced by N [u] ∪ {v}, where v is some arbitrary,
but a ﬁxed vertex from V (G) \ N [u], is like the one on the Figure 1.

Figure 1: Induced subgraph of G.

Graph H is a 16–vertex graph that does not have 2 as an eigenvalue. Lemma
3 from the next section enables expanding of the graph H with three additional

Example of using star complements in classifying strongly regular graphs 55

vertices to get all of the possible star complements (which contain H as an induced
subgraph) in G for the eigenvalue 2. In Section 3, it is shown that none of the
possible star complements gives a rise to a desired strongly regular graph, thus
proving that the graph G does not exist. These results were obtained using a
computer.

2 Extending to a star complement

It this section we show that any induced subgraph that does not have the eigenvalue
ξ can be extended to a star complement for the eigenvalue ξ. The lemma was proved
by D. Stevanovi´c and M. Miloˇsevi´c.

Lemma 3 Let ξ be an eigenvalue of G and let H be an induced subgraph of G such
that ξ is not an eigenvalue of H. Then there exists a star complement H ′ for ξ in
G such that H ⊆ H ′.

Proof: Let E(ξ) be the eigenspace of ξ in G, and let P be the orthogonal projection
of R
n onto E(ξ) with respect to the standard orthonormal basis {e1, . . . , en} of R
n.
Further, let X = G − H.
Following the proof of Theorem 7.2.3 in [1], we can show that ⟨P ej : j ∈ X⟩ =
E(ξ). Suppose, on the contrary, that ⟨P ej : j ∈ X⟩ ⊂ E(ξ). Then, there is a
non-zero vector x ∈ E(ξ) ∩ ⟨P ej : j ∈ X⟩
⊥. Thus, x
T P ej = 0 for all j ∈ X. Hence
(P x)T ej = (x
T P )ej = 0 for all j ∈ X. Consequently, P x ∈ ⟨ej : j ∈ X⟩
⊥ = ⟨es :
s ̸∈ X⟩. Since x = P x, we have non-zero x ∈ E(ξ) ∩ ⟨es : s ̸∈ X⟩.

From x = ( 0
x
′
 )
, with x
′ ̸= 0, it follows that x
′ is an eigenvector of G−X = H,

a contradiction.
Thus, there exists a subset X ′ ⊆ X such that the vectors {P ej : ej ∈ X ′} form a
basis for E(ξ). In such case, from Theorem 7.2.9 in [1] it follows that |X ′| = dim E(ξ)
and ξ is not an eigenvalue of G − X ′ = H ′. Thus, H ′ is a star complement for ξ
which contains H as an induced subgraph.

3 The nonexistence

According to Lemma 3, to classify strongly regular graphs with parameters (57, 14, 1, 4),
it is suﬃcient to extend graph H (Figure 1) with three additional vertices in all
possible ways so that the second largest eigenvalue of the resulting graph is strictly
lower than 2, and then examine the compatibility graphs that arise from these star
complements.
So, in each of the three steps we add a new vertex that has four neighbors in
common with vertex u, and we do this in all possible ways, preserving the conditions
that any two adjacent vertices do not have more than one common neighbor, and
that any two non-adjacent vertices do not have more than four common neighbors.

56 Marko Miloˇsevi´c

After that we get one representative of each isomorphism class, and discard those
graphs that have the second largest eigenvalue greater or equal to 2.
This way, the graph H can be extended with three vertices as described to get
3720 non-isomorphic graphs. These graphs represent potential star complements in
G for the eigenvalue 2. To each of them we apply the Reconstruction theorem. We
do not actually need to create the whole compatibility graph since the conditions on
common neighbors count must be satisﬁed. Therefore we only consider those (0, 1)–
vectors that do not violate the conditions for strong regularity, i.e. we work with
an induced subgraph of each compatibility graph, but we still call these subgraphs
the compatibility graphs, for the ease of notation.
Sizes of the compatibility graphs vary from 4 to 265 vertices. We have used
Cliquer [4] to determine the largest cliques in these compatibility graphs. Summary
of the results is given in the following table.

The largest clique size Number of compatibility graphs
2 6
3 2
4 13
5 32
6 18
7 173
8 358
9 403
10 131
11 220
12 502
13 400
14 58
15 123
16 303
29 19
30 49
31 910

Table 1: The largest cliques in compatibility graphs.

As we can see from Table 1, none of these compatibility graphs contains the
clique of size 38 which is needed to reconstruct the graph on 57 vertices.
Thus, we conclude that

Theorem 4 The strongly regular graph with parameters (57, 14, 1, 4) does not exist.

Example of using star complements in classifying strongly regular graphs 57

References

[1] D. Cvetkovi´c, P. Rowlinson, S. Simi´c, Eigenspaces of graphs, Cambridge Uni-
versity Press, Cambridge, 1997.

[2] D. Cvetkovi´c, P. Rowlinson, S. Simi´c, Some characterizations of graphs by star
complements, Linear Algebra Appl. 301 (1999), 81–97.

[3] D. Cvetkovi´c, P. Rowlinson, S. Simi´c, Spectral generalizations of line graphs,
Cambridge University Press, Cambridge, 2004.

[4] P. ¨Osterg˚ard, Cliquer, http://users.tkk.ﬁ/∼pat/cliquer.html

[5] P. Rowlinson, Co-cliques and star complements in extremal strongly regular
graphs, Linear Algebra and its Appl. 421 (2007), 157–162.

[6] P. Rowlinson, Star sets in regular graphs, J. Comb. Math. Comb. Comput. 34
(2000), 3–22.

[7] D. Stevanovi´c, M. Miloˇsevi´c, A spectral proof of the uniqueness of a strongly
regular graph with parameters (81, 20, 1, 6), Eur. J. Comb., to appear

[8] H.A. Wilbrink, A.E. Brouwer, A (57, 14, 1, 4) strongly regular graph does not
exist, Indag. Math. 45 (1983), 117–121

Faculty of Science and Mathematics, Viˇsegradska 33, 18000 Niˇs, Serbia
E-mail: ninja643@gmail.com
