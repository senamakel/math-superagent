<!-- source: https://arxiv.org/pdf/2508.19302 | converted from PDF -->

Cycles of Length 4 or 8 in Graphs with Diameter 2 and
Minimum Degree at Least 3

Avery Carr
Independent Researcher
avery.carr@ymail.com

Updated: January 29, 2026

Abstract

In this short note it is shown that every graph of diameter 2 and minimum degree
at least 3 contains a cycle of length 4 or 8. This result contributes to the study of the
Erd˝os–Gy´arf´as Conjecture [1] by confirming it for the class of diameter-2 graphs.

Notation and Preliminaries

All graphs considered in this note are finite, simple, and undirected.
Let G = (V (G), E(G)) be a graph where V (G) and E(G) denote the set of vertices and
edges in G respectively. For a vertex v ∈ V (G), the neighborhood of v is

N (v) = {u ∈ V (G) : uv ∈ E(G)},

and the degree of v is d(v) = |N (v)|. The minimum degree of G is denoted by

δ(G) = min{d(v) : v ∈ V (G)}.

For vertices u, v ∈ V (G), the distance d(u, v) is the length of a shortest path joining u
and v in G. The diameter of G is

diam(G) = max{d(u, v) : u, v ∈ V (G)}.

A path of length k is a sequence of distinct vertices

v0, v1, . . . , vk

such that vivi+1 ∈ E(G) for all 0 ≤ i < k. A cycle of length k is a sequence

v0, v1, . . . , vk−1, v0

in which v0, . . . , vk−1 are distinct and vivi+1 ∈ E(G) for all indices taken modulo k.

1arXiv:2508.19302v4  [math.CO]  30 Jan 2026
A k-cycle is a cycle of length k. A cycle is called simple if it contains no repeated vertices
except for the initial and terminal vertex.
Given a cycle C, an edge joining two nonconsecutive vertices of C is called a chord of C.
Throughout the paper, vertex labels v1, v2, . . . are introduced as needed and are proved
to be distinct. When a sequence is written as

v1 − v2 − · · · − vk,

it means that vivi+1 ∈ E(G) for all 1 ≤ i < k.
All set-theoretic notation is used in its standard meaning.

Introduction

A well-known open problem of Erd˝os and Gy´arf´as asks for unavoidable cycle lengths in
graphs with minimum degree at least three. In particular, they conjectured that every graph
G with δ(G) ≥ 3 contains a simple cycle whose length is a power of two. This is now
commonly referred to as the Erd˝os–Gy´arf´as Conjecture. Folklore has the conjecture first
appearing at a conference in (1995) (later in literature in (1997) [1]), and is listed in several
open-problem compilations (e.g. West [2] and Erd˝os problems forums such as [3]).
Despite its simple statement, the conjecture remains open in full generality and has been
verified only for restricted classes of graphs. Early progress includes results for planar and
cubic claw-free graphs [4,5]. More recently, Heckman and Krakovski proved the conjecture for
3-connected cubic planar graphs [6], and a number of papers have established the conjecture
for other hereditary or structured graph classes such as P8-free graphs [7].
Computational searches have also shaped the current understanding. In particular, ex-
haustive and heuristic searches (notably by Royle and Markstr¨om) indicate that any coun-
terexample must be relatively large, and Markstr¨om produced extremal examples illustrating
how power-of-two cycles can be forced to occur only at larger lengths (e.g. 16) in certain
cubic graphs [8]. These computations suggest that minimal counterexamples, if they exist,
are highly constrained.
In this note the Erd˝os–Gy´arf´as conjecture is verified for graphs of diameter 2. The main
result shows that every graph G with diam(G) = 2 and δ(G) ≥ 3 contains a cycle of length
4 or 8 (see Theorem 1.1.). Thus, within the diameter–2 regime, the conjecture holds in
its strongest possible form, guaranteeing one of the two smallest nontrivial powers of two.
From the perspective of the broader conjecture, diameter 2 graphs form a natural and widely
studied class: the global constraint diam(G) = 2 forces any two nonadjacent vertices to have
a common neighbor, creating a dense web of short connections. The proof exploits this
interaction between a local degree lower bound and the global diameter constraint to force
short power-of-two cycles.
 2

Main Result

Theorem 1.1.: Let G be a graph with diameter 2 and minimum degree at least 3. Then G
contains a cycle of length 4 or 8.

Proof

Assume G has diameter 2, minimum degree at least 3, and no 4-cycle. For a vertex v in G,
let N (v) denote its neighborhood; the set of vertices adjacent to v.
Let v1v2 ∈ E(G). By the degree condition, v1 has two neighbors other than v2, call them
v3, v4; similarly, v2 has two neighbors v5, v6. Denote this subgraph of G as G′ (see Figure 1).

v1 v2

v3 v4 v5 v6

Figure 1: G′ - Initial edge with neighbors satisfying the degree constraint.

If v3 = v5 while v4 = v6, or v3 = v6 while v4 = v5, then a cycle of length 4 forms
immediately, namely

v1 − v3 − v2 − v4 − v1 or v1 − v4 − v2 − v3 − v1.

Both cases contradict the assumption that G contains no 4-cycle.
Thus, without loss of generality, it suffices to prove the theorem by considering separately
the cases v3 = v5 and v3 ̸= v5.

Case 1: v3 = v5

Assume v3 = v5. Let v4 be the neighbor of v1 distinct from v2, v3, and let v6 be the neighbor
of v2 distinct from v1, v3. Set V (G′) = {v1, v2, v3, v4, v6}.

Claim 1.1. v4v6 /∈ E(G).
Proof. If v4v6 ∈ E(G), then
 v4 − v1 − v2 − v6 − v4

is a 4-cycle, contradicting the assumption that G contains no 4-cycle. ⋄

3

Since v4 and v6 are nonadjacent and diam(G) = 2, we have

N (v4) ∩ N (v6) ̸= ∅.

Choose v7 ∈ N (v4) ∩ N (v6).

Claim 1.2. v7 /∈ {v1, v2, v3}.
Proof. If v7 = x such that x ∈ {v1, v2, v3}, then at least one of the following 4–cycles
would form: v1 − v3 − v2 − v6 − v1,
v2 − v3 − v1 − v6 − v2,
v4 − v3 − v2 − v1 − v4. ⋄

Thus, assume v7 /∈ V (G′). Then the closed walk

v7 − v4 − v1 − v3 − v2 − v6 − v7

forms a 6-cycle with a chord v1v2 (see Figure 2).

v7

v4
 v1 v2
 v6v3

Figure 2: 6-Cycle with a v1v2 Chord

Notice v3 and v7 are not adjacent, and if the edge v3v7 ∈ E(G), then a 4-cycle forms by

v7 − v3 − v1 − v4 − v7,

a contradiction. Also, the diameter–2 condition implies

N (v3) ∩ N (v7) ̸= ∅.

Let v8 ∈ N (v3) ∩ N (v7).

Claim 1.3 v8 /∈ V (G′).
Proof. Indeed, if v8 ∈ V (G′), then v8 ∈ {v1, v2, v4, v6} and a 4–cycle arises in each case:

4

v8 = v1 =⇒ v1 − v2 − v6 − v7 − v1,
v8 = v2 =⇒ v2 − v1 − v4 − v7 − v2,
v8 = v4 =⇒ v4 − v3 − v2 − v1 − v4,
v8 = v6 =⇒ v6 − v3 − v1 − v2 − v6.

This contradicts the assumption that G contains no 4–cycle. Hence v8 /∈ V (G′)
(see Figure 3). ⋄

v7

v4
 v1 v2
 v6v3
 v8

Figure 3: v8 ∈ N (v7) ∩ N (v3)

Since δ(G) ≥ 3, the vertex v8 has a neighbor v9 /∈ {v3, v7}.

Claim 1.4. v9 /∈ V (G′).
Proof. Otherwise v9 ∈ {v1, v2, v4, v6}, and each possibility yields a 4–cycle:

v9 = v1 =⇒ v1 − v4 − v7 − v8 − v1,
v9 = v2 =⇒ v2 − v1 − v3 − v8 − v2,
v9 = v4 =⇒ v4 − v8 − v3 − v1 − v4,
v9 = v6 =⇒ v6 − v2 − v3 − v8 − v6.
 ⋄
Thus v9 /∈ V (G′) (see Figure 4).
 5

v7

v4
 v1 v2
 v6v3
 v8 v9

Figure 4: v8v9 ∈ E(G)

Claim 1.5. If v9 is adjacent to x ∈ {v1, v2, v4, v6}, then there exists a 4–cycle.
Proof. Assume v9 is adjacent to x ∈ {v1, v2, v4, v6}. Thus, a 4–cycle is formed in each of the
following cases: x = v1 =⇒ v1 − v3 − v8 − v9 − v1,
x = v2 =⇒ v2 − v3 − v8 − v9 − v2,
x = v4 =⇒ v4 − v7 − v8 − v9 − v4,
x = v6 =⇒ v6 − v7 − v8 − v9 − v6. ⋄
Also, since v9 is nonadjacent with both v4 and v2, by diam(G) = 2 both N (v9) ∩ N (v4)
and N (v9) ∩ N (v2) are non-empty.

Claim 1.6. There is a vertex v10 ∈ (N (v9) ∩ N (v4)) ∪ (N (v9) ∩ N (v2)) such that
v10 /∈ ({v7, v8} ∪ V (G
′)).
Proof. If v8 ∈ (N (v9) ∩ N (v4)) ∪ (N (v9) ∩ N (v2)) then v8 is adjacent to one of v2 or v4 and,
by Claim 1.4, a 4–cycle is present. Thus, v10 ̸= v8. Now, suppose v10 ∈ (N (v9) ∩ N (v4)) ∪
(N (v9) ∩ N (v2)) such that (N (v9) ∩ N (v4)) ∪ (N (v9) ∩ N (v2)) ⊆ ({v7} ∪ V (G
′)). Then, by
the diameter 2 condition and Claim 1.5, v9 is adjacent to both v3 and v7 (else v9 would be
adjacent to another pair of vertices in {v7}∪V (G′) violating Claim 1.5). However, this forms
a 4–cycle by v3 − v8 − v7 − v9 − v3, providing a contradiction on the claim of no 4–cycles. ⋄
Thus, by Claim 1.6, there is a distinct vertex v10 that is in at least one of N (v9) ∩ N (v2)
or N (v9) ∩ N (v4) such that v10 /∈ ({v7, v8} ∪ V (G
′)). In either case, an 8–cycle is formed (see
Figure 5 and 6) by:

v10 ∈ N (v9) ∩ N (v2) =⇒ v10 − v2 − v3 − v1 − v4 − v7 − v8 − v9 − v10,
v10 ∈ N (v9) ∩ N (v4) =⇒ v10 − v4 − v1 − v2 − v6 − v7 − v8 − v9 − v10.

6

v7

v4
 v1 v2
 v6v3
 v8 v9

v10

Figure 5: v10 ∈ N (v2) ∩ N (v9) forming an 8-Cycle

v7

v4
 v1 v2
 v6v3 v8 v9

v10

Figure 6: v10 ∈ N (v4) ∩ N (v9) forming an 8-Cycle

Case 2: v3 ̸= v5

Assume v3 ̸= v5.

Claim 2.1. If xy ∈ E(G) for some x ∈ {v3, v4} and y ∈ {v5, v6}, then G contains a 4-cycle.
Proof. Since v1x ∈ E(G) and v2y ∈ E(G), the cycle v1 − x − y − v2 − v1 has length 4. ⋄

Hence we may assume that no edge joins the sets {v3, v4} and {v5, v6}.

Claim 2.2. There exist a ∈ {v3, v4} and b ∈ {v5, v6} such that

N (a) ∩ N (b) ̸⊆ {v1, v2}.

Proof. Because diam(G) = 2 and ab /∈ E(G) (by Claim 2.1), every such pair (a, b) has a
common neighbor, so N (a) ∩ N (b) ̸= ∅.
Suppose for contradiction that for every a ∈ {v3, v4} and b ∈ {v5, v6} we have

N (a) ∩ N (b) ⊆ {v1, v2}.

7

Since v1 is adjacent to both v3 and v4, the vertex v1 is a common neighbor of (a, b) exactly
when v1b ∈ E(G). Similarly, since v2 is adjacent to both v5 and v6, the vertex v2 is a common
neighbor of (a, b) exactly when v2a ∈ E(G). Thus, for each pair (a, b), at least one of the
edges v1b or v2a must exist.
If v1 is adjacent to both v5 and v6, then v1 − v5 − v2 − v6 − v1 is a 4-cycle. If v2 is adjacent
to both v3 and v4, then v1 − v3 − v2 − v4 − v1 is a 4-cycle. Hence v1 is adjacent to at most one
of {v5, v6} and v2 is adjacent to at most one of {v3, v4}. But then there is some pair (a, b)
with v1b /∈ E(G) and v2a /∈ E(G), contradicting the requirement that each pair (a, b) has a
common neighbor in {v1, v2}. Therefore the claim holds. ⋄

By Claim 2.2, choose a ∈ {v3, v4} and b ∈ {v5, v6} and a vertex

v7 ∈ N (a) ∩ N (b) \ {v1, v2}.

If v7 ∈ {v3, v4, v5, v6}, then a 4-cycle occurs:

v7 = v3 ⇒ v1 − v3 − b − v2 − v1,
v7 = v4 ⇒ v1 − v4 − b − v2 − v1,
v7 = v5 ⇒ v1 − a − v5 − v2 − v1,
v7 = v6 ⇒ v1 − a − v6 − v2 − v1.

Thus, v7 /∈ V (G′) = {v1, v2, v3, v4, v5, v6}.

Without loss of generality, let a = v3 and b = v5; hence

v7 ∈ N (v3) ∩ N (v5), v7 /∈ V (G′)

(see Figure 7).
 v1 v2

v3 v4 v5 v6

v7

Figure 7: A new common neighbor v7 ∈ N (v3) ∩ N (v5) with v7 /∈ V (G′).

Claim 2.3. v7v4 /∈ E(G).
Proof. If v7v4 ∈ E(G), then v4 − v7 − v3 − v1 − v4 is a 4-cycle. ⋄

8

Consider the nonadjacent pair (v4, v6). If v4v6 ∈ E(G), then Claim 2.1 is violated and
there is a 4-cycle. Hence v4v6 /∈ E(G) and

N (v4) ∩ N (v6) ̸= ∅.

Choose v8 ∈ N (v4) ∩ N (v6).

Claim 2.4. v8 /∈ {v3, v5, v7}.
Proof. If v8 = v3 or v8 = v5, then Claim 2.1 is violated. If v8 = v7, then Claim 2.3 is
violated. ⋄

Subcase 2A: v8 = v1. Then v1v6 ∈ E(G). Since diam(G) = 2 and v6 and v7 are nonadja-
cent, we have N (v6) ∩ N (v7) ̸= ∅.

Choose x ∈ N (v6) ∩ N (v7). If x ∈ V (G
′) \ {v6} then a 4–cycle appears by at least one of
the following:
 x = v1 ⇒ v1 − v7 − v5 − v2 − v1,
x = v2 ⇒ v2 − v1 − v3 − v7 − v2,
x = v3 ⇒ v3 − v1 − v2 − v6 − v3,
x = v4 ⇒ v4 − v1 − v2 − v6 − v4,
x = v5 ⇒ v5 − v2 − v1 − v6 − v5.

Thus, x /∈ V (G
′) \ {v6} (see Figure 8).

v1 v2

v3 v4 v5 v6

v7 x

Figure 8: Common neighbor x ∈ N (v6) ∩ N (v7) with x /∈ V (G′) \ {v6}.

Since v4 and v5 are nonadjacent (by Claim 2.1),

N (v4) ∩ N (v5) ̸= ∅,

by the diam(G) = 2 condition.
Suppose y ∈ N (v4) ∩ N (v5). By Claim 2.1, y /∈ {v3, v6}.

9

Suppose y ∈ {v1, v2, v7, x}.

Thus, a 4–cycle occurs by the following:

y = v1 ⇒ v1 − v6 − v2 − v5 − v1,
y = v2 ⇒ v2 − v6 − v1 − v4 − v2,
y = v7 ⇒ v7 − v3 − v1 − v4 − v7,
y = x ⇒ x − v5 − v2 − v6 − x.

Therefore, y ∈ N (v4) ∩ N (v5) such that y /∈ {v1, v2, v7, x} (see Figure 9) .

v1 v2

v3 v4 v5 v6

v7 x

y

Figure 9: Common neighbor y ∈ N (v4) ∩ N (v5) with y /∈ {v1, v2, v5}.

But x − v7 − v5 − y − v4 − v1 − v2 − v6 − x

forms a cycle of length 8. ⋄

Subcase 2B: v8 = v2. This case is handled analogously to v8 = v1; using diameter and
degree constraints, start with v2v4 ∈ E(G), force a x ∈ N (v4)∩N (v7) and y ∈ N (v3)∩N (v6),
obtaining an 8–cycle.
Subcase 2C: v8 /∈ {v1, v2}. Then the edges

v7v3, v3v1, v1v4, v4v8, v8v6, v6v2, v2v5, v5v7

form the simple cycle
 v7 − v3 − v1 − v4 − v8 − v6 − v2 − v5 − v7,

which has length 8 (see Figure 10).
 10

Thus, in all cases, G contains a cycle of length 4 or 8.

v1 v2

v3 v4 v5 v6

v7 v8

Figure 10: Case 2: if v3 ̸= v5, an 8-cycle appears.
 □

Acknowledgments

The author thanks Dr. Michael Albert, Editor-in-Chief of the Australasian Journal of Com-
binatorics, and one anonymous external expert for their careful reading of an earlier draft,
advice, and for comments on the originality and merit of this work. Also, thank you to Dr.
Tao Wang of Henan University for reading the first draft and presenting a counterexample
to case 1 in personal communication that was accounted for in the author’s original notes
but not in the first draft.

References

[1] P. Erd˝os, Some old and new problems in various branches of combinatorics, Discrete
Math. 165/166 (1997), 227–231.

[2] D. B. West, Erd˝os–Gy´arf´as conjecture on 2-power cycle lengths, Open Problems page
(UIUC), https://dwest.web.illinois.edu/openp/2powcyc.htm (accessed Jan. 2026).

[3] P. Erd˝os, Problem 64, Erd˝os Problems, https://www.erdosproblems.com/64
(accessed Jan. 2026).

[4] D. Daniel and S. E. Shauger, A result on the Erd˝os–Gy´arf´as conjecture in planar graphs,
Congressus Numerantium 153 (2001), 129–139.

[5] P. Salehi Nowbandegani, H. Esfandiari, M. H. Shirdareh Haghighi, and K. Bibak, On the
Erd˝os–Gy´arf´as conjecture in claw-free graphs, Discuss. Math. Graph Theory 34 (2014),
635–640.
 11

[6] C. C. Heckman and R. Krakovski, Erd˝os–Gy´arf´as conjecture for cubic planar graphs,
Electronic J. Combin. 20(2) (2013), #P7.

[7] Y. Gao and S. Shan, Erd˝os–Gy´arf´as conjecture for P8-free graphs, Graphs and Combina-
torics 38 (2022), Article 168.

[8] K. Markstr¨om, Extremal graphs for some problems on cycles in graphs, Congressus Nu-
merantium 171 (2004), 177–188.
 12
