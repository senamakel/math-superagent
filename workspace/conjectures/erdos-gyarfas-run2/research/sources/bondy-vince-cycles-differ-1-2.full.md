<!-- source: https://people.clas.ufl.edu/avince/files/Cycles.pdf | converted from PDF -->

Cycles in a Graph Whose
Lengths Differ by One
or Two
 J. A. Bondy
1

and A. Vince
2

1LABORATOIRE DE MATH´EMATIQUES DISCR ´ETES
UNIVERSIT ´E CLAUDE-BERNARD LYON 1
69622 VILLEURBANNE, FRANCE
2DEPARTMENT OF MATHEMATICS
UNIVERSITY OF FLORIDA
GAINESVILLE, FL U.S.A. 32611

This note is dedicated to the memory of our friend and colleague Paul Erd ˝os.

Received July 5, 1996

Abstract: Several problems concerning the distribution of cycle lengths in a graph have
been proposed by P. Erd¨os and colleagues. In this note two variations of the following
such question are answered. In a simple graph where every vertex has degree at least
three, must there exist two cycles whose lengths differ by one or two? c⃝ 1998 John Wiley
& Sons, Inc. J Graph Theory 27: 11–15, 1998

1. INTRODUCTION

Several questions concerning the distribution of cycle lengths in a graph have been posed by P.
Erd˝os and colleagues. One of these questions is the following.

Question. In a simple graph where every vertex has degree at least three, must there exist two
cycles whose lengths differ by one or two?

Other open problems concerning the existence of cycles of specified length are mentioned by
Erd˝os in [2]. For example, Erd˝os and A. Gy´arf´as asked: If G is a graph with minimum degree
three, must G have a cycle of length 2
r for some integer r? More generally, Erd˝os asked (and

c⃝ 1998 John Wiley & Sons, Inc. CCC 0364-9024/98/010011-05

12 JOURNAL OF GRAPH THEORY

offered $100) for a proof of the existence or nonexistence of a sequence a1 <a2 < ··· of density
0 and an absolute constant c for which every graph on n vertices and cn edges contains a cycle
of length ai for some i.
In this note, the above Question is answered in the affirmative. The conclusion cannot be
strengthened to ‘two cycles whose lengths differ by one’ because, in a bipartite graph, two
such cycles do not exist. However, the assertion can be pushed in two directions, given in the
following two theorems. Let Kn,Cn,Pn denote the complete graph, cycle and path, respectively,
on n vertices, and let Km,n denote the complete bipartite graph with parts of sizes m and n.

Theorem 1. With the exception of K1 and K2, every simple graph having at most two vertices
of degree less than three contains two cycles whose lengths differ by one or two.

Theorem 2. Every nonbipartite 3-connected graph has two cycles whose lengths differ by one.

Theorem 1 is best possible in the sense that each of the graphs C3,P3 and K2,3 have three
vertices of degree less than three but contain no two cycles whose lengths differ by one or two.
However, if one allows additional exceptions, then Theorem 1 can be extended. With exactly
twelve exceptions, every simple graph having at most three vertices of degree less than three
contains two cycles whose lengths differ by one or two. In addition to K1 and K2, the exceptions
are C3,P3 and K2,3, and the seven graphs obtained from C3,P3 and K2,3 by attaching a single
pendant edge to one or more vertices of degree two. The proof of this result proceeds exactly
as in the proof in Section 2 of Theorem 1, but requires a tedious case by case analysis of the
exceptional graphs in the induction step. Similar results can likely be obtained for four or five
vertices of degree less than three, if one can determine the exceptions and has the perseverance
to carry out the case by case analysis. The following question, however, is open.

Conjecture. Let k be any nonnegative integer. With finitely many exceptions, every simple
graph having at most k vertices of degree less than three has two cycles whose lengths differ by
one or two.

Concerning Theorem 2, the 3-connectedness requirement is necessary. If it is assumed instead
that G is 2-connected and, in addition, that every vertex has degree at least d, the corresponding
statement is false. The counterexample (for d =3) in Figure 1 has only cycles of lengths 4, 6, 9,
11, 13 and 15. This example can easily be generalized to an infinite family of counterexamples
by attaching a sufficiently large odd number of copies of Kd,d − e in a ring, as in the figure.

FIGURE 1. A counterexample.
 CYCLES IN A GRAPH 13

A natural extension of Theorem 2 would be a condition guaranteeing the existence of cycles
of three more more consecutive lengths. The only nonbipartite 3-connected graphs that we know
of without cycles of three consecutive lengths are K4 and the Petersen graph.

Problem. Does there exist a function f (k) such that every nonbipartite 3-connected graph
with minimum degree at least f (k) contains cycles of k consecutive lengths?

2. THE PROOFS

The proofs of Theorems 1 and 2 rely on the two lemmas which are based on an approach of
Thomassen and Toft [4] to nonseparating cycles in graphs. The terminology of ‘‘bridges’’ is
originally due to Tutte [5] (also see Bondy and Murty [1], Voss [6] or West [7]). Let C be a
cycle in a graph. A C-bridge is either (1) an edge not in C whose endpoints are in C or (2) a
component of G − V (C) together with the edges (and vertices of attachment) that connect it to
C. The vertices of the bridge that are not vertices of attachment are called internal vertices.Two
C-bridges A and B are said to conf lict if either (1) they have three common vertices of attachment
or (2) there are four vertices v1,v2,v3,v4 in cyclic order on C such that v1,v3 are vertices of
attachment of A and v2,v4 are vertices of attachment of B.Two C-bridges that do not conflict
are said to avoid each other.

Lemma 1. Let G be a 2-connected graph, not a cycle, and let C be an induced cycle in G
some bridge B of which has as many internal vertices are possible. Then either

(1) B is the only C-bridge, or else
(2) B is a C-bridge with exactly two vertices of attachment, and every other C-bridge is a
path having the same two vertices of attachment to C as B.

Proof. Let B′ be any C-bridge different from B. Denote by S and S′ the sets of vertices of
attachment of B and B′, respectively, to C. Because G is 2-connected, |S|≥ 2 and |S′|≥ 2.
Let x, y ∈ S′ and let P ′ be an xy-path in B′. We claim that S = {x, y}, and hence that
S′ = {x, y} too. Suppose, to the contrary, that S ̸= {x, y}, and consider z ∈ S \{x, y}. Denote
by P the xy-segment of C not including z. Since P ∪ P ′ is a cycle, there is an induced cycle
C ′ with V (C ′) ⊆ V (P ∪ P ′). One of the bridges of C ′ has as internal vertices all the internal
vertices of B and, in addition, the vertex z, contradicting the maximality hypothesis on C.We
conclude that S = {x, y}.
Similar reasoning shows that neither B′ − x nor B′ − y contains an induced cycle. Therefore
B′ −{x, y} is a tree having at most one vertex adjacent to each of x and y. It readily follows
from the 2-connectedness of G that B′ = P ′.

Lemma 2. Let G be a nonbipartite 2-connected graph, not a cycle, and let C be an induced
odd cycle in G some bridge B of which has as many internal vertices as possible. Then every
other bridge of C is bipartite and avoids B.

Proof. Let B′ be a C-bridge different from B. Denote by S and S′ the sets of vertices of
attachment of B and B′, respectively, to C. Because G is 2-connected, |S|≥ 2 and |S′|≥ 2.
Let x, y ∈ S′. Neither B′ − x nor B′ − y contains an induced odd cycle because one of the
bridges of such a cycle would have as internal vertices all the internal vertices of B as well as x or
y, respectively, contradicting the maximality hypothesis on C. The connectedness of B′ −{x, y}
now implies that B′ itself is bipartite.

14 JOURNAL OF GRAPH THEORY

Let P ′ be any xy-path in B′, and let P be the xy-path in C for which the cycle P ∪ P ′ is odd.
Let C ′ be an induced odd cycle with V (C ′) ⊆ V (P ∪ P ′). The cycle C ′ has a bridge whose
internal vertices include all the internal vertices of B. By the maximality hypothesis on C, one
deduces that S ⊆ V (P ).
If x and y are the only vertices of attachment of B′ to C, then it is clear that B and B′ avoid
one another, as claimed. Therefore, suppose that |S′|≥ 3, and let the vertices of S′, in cyclic
order on C,be v1,v2,...,vm.For 1 ≤ i ≤ m, denote by Pi the vivi+1-segment of C, and
let P ′
i be a vivi+1-path in B′ (indices modulo m). Because C is odd, ∑m
i=1 |E(Pi)| is odd,
and because B′ is bipartite, ∑m
i=1 |E(P ′
i )| is even. It follows that the cycle Pi ∪ P ′
i is odd for
some i, 1 ≤ i ≤ m. As noted above, this implies that S ⊆ V (Pi). Thus B and B′ avoid one
another.

Proof of Theorem 1. The proof is by induction on the number n of vertices in the graph
G. Theorem 1 is vacuously true for n ≤ 3. Let G be a graph on n> 3 vertices and assume the
theorem is true for graphs with fewer than n vertices.
By considering an appropriate block of G, we may suppose that G is 2-connected. Let C and
B be as described in Lemma 1. By this lemma, if there is a C-bridge other than B, each such
bridge is necessarily a path; moreover, all C-bridges, including B, have the same two vertices of
attachment x, y. Every other vertex of C is thus of degree two. Because G is assumed to have at
most two vertices of degree less than three, the length of C is three or four. In the former case,
there is exactly one path bridge, of length two; in the latter case, x and y are nonconsecutive
vertices of C and there is exactly one path bridge, of length one. In both cases, G has cycles of
lengths three and four. Therefore, it may be assumed that B is the only C-bridge.
There can be at most two vertices on C that are not vertices of B. Hence, unless C is a 4-cycle
with alternate vertices in B, there exist two vertices of attachment of B to C, say x and y, for
which the two xy-paths in C differ in length by one or two. Denote these two xy-paths of C by
P1 and P2, and let P be an xy-path in B. The cycles P ∪ P1 and P ∪ P2 differ in length by one
or two, which proves the theorem.
In the case that C is a 4-cycle to which B has two vertices of attachment, the bridge B itself
is a simple graph in which every vertex, except possibly its two vertices of attachment to C, has
degree at least three. By induction, either the theorem is proved or B is K1, clearly impossible,
or K2, impossible because C is induced.

Proof of Theorem 2. Let C and B be as described in Lemma 2. We claim that B is the only
bridge of C. By way of contradiction, suppose that C has a second bridge B′. By Lemma 2, the
bridges B and B′ avoid one another. There is thus a segment of C, connecting two consecutive
vertices of attachment x, y of B to C, which contains every vertex of attachment of B′ to C (and
no other vertex of attachment of B to C). But then {x, y} is a 2-vertex cut of G, contradicting
the hypothesis of 3-connectedness. Thus B is indeed the only bridge of C.
Since C is odd, there exist two vertices of C, say x and y, for which the two xy-segments of
C, P1 and P2, differ in length by one. Moreover, because B is the only bridge of C, x and y are
vertices of attachment of B to C. Let P be an xy-path in B. The cycles P ∪ P1 and P ∪ P2 differ
in length by one.

Remarks. The fact used in the proof of Theorem 2, that G contains an odd cycle C with only
one bridge B, is also an immediate corollary of a theorem of Tutte stating that the induced
nonseparating cycles in a 3-connected graph generate its cycle space [4].

CYCLES IN A GRAPH 15

Since this paper was accepted for publication, A. K. Kelmans has drawn the authors' attention
to an article of his [3] in which nonseparating cycles are treated and in which results of a similar
nature to our Lemma 1 may be found.

References

[1] J. A. Bondy and U. S. R. Murty, Graph theory with applications, MacMillan, London (1976).

[2] P. Erd˝os, Some old and new problems in various branches of combinatorics, Discrete Math. 165/166
(1997), 227–231.

[3] A. K. Kelmans, Algebraic methods in graph theory (Szeged 1978) Vol. I, Colloq. Math. Soc. J´anos
Bolyai, vol. 25, North-Holland, Amsterdam/New York (1981).

[4] C. Thomassen and B. Toft, Non-separating induced cycles in graphs, J. Combinatorial Theory B 31
(1981), 199–224.

[5] W. T. Tutte, How to draw a graph, Proc. London Math. Soc. 3 (1963), 743–768.

[6] H. J. Voss, Cycles and bridges in graphs, VEB Deutscher Verlag der Wissenschaften/Kluwer Academic
Publishers, Berlin/Dordrecht, 1991.

[7] D. B. West, Introduction to graph theory, Prentice-Hall, Upper Saddle River, NJ (1996).
