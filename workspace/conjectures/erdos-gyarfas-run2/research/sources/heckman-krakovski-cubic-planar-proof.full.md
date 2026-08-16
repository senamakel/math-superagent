<!-- source: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i2p7/pdf | converted from PDF -->

Erd˝os-Gy´arf´as Conjecture for Cubic Planar Graphs

Christopher Carl Heckman

School of Mathematical and Statistical Sciences
Arizona State University
Tempe, AZ 85287 - 1804

checkman@math.asu.edu
 Roi Krakovski

Department of Computer Science
Ben-Gurion University
Beer-Sheva, 84105, Israel

roikr@math.bgu.ac.il

Submitted: May 23, 2011; Accepted: Mar 30, 2013; Published: Apr 9, 2013

Abstract

In 1995, Paul Erd˝os and Andr´as Gy´arf´as conjectured that for every graph of
minimum degree at least 3, there exists a non-negative integer m such that G
contains a simple cycle of length 2m. In this paper, we prove that the conjecture
holds for 3-connected cubic planar graphs. The proof is long, computer-based in
parts, and employs the Discharging Method in a novel way.

Keywords: Erd˝os-Gy´arf´as Conjecture, Cycles of prescribed lengths, Cubic graphs.

1 Introduction

In this paper all graphs are ﬁnite and simple. Paths and cycles are simple, that is, have
no “repeated” vertices. A k-cycle is a cycle of length k. The well-known Erd˝os-Gy´arf´as
conjecture [1] states that every graph of minimum degree at least 3 contains a 2m-cycle,
for some m ⩾ 2.
A graph is planar if it can be embedded in the plane without crossing edges. A plane
graph is an embedded planar graph. A graph G is 3-connected if |V (G)| ⩾ 4 and there is
no S ⊆ V (G) such that |S| < 3 and G \ S is disconnected (\ denotes deletion). A graph
G is cubic if every vertex of G is of degree three.
By computer searches, Markstr¨om [2] veriﬁed the conjecture for cubic graphs of order
at most 29, and found that the smallest cubic planar graph with no 4- or 8-cycles has 24
vertices (see Figure 1). Note that this graph contains a 16-cycle. Shauger [3] proved the
conjecture for K1,m-free graphs of minimum degree at least m + 1 or maximum degree at
least 2m − 1. Daniel and Shauger [4] proved the conjecture for planar claw-free graphs.
The following is the main result of this paper.

1.1. Every 3-connected cubic planar graph contains a 2
m-cycle, for some 2 ⩽ m ⩽ 7.

It is not clear whether 1.1 is tight. It is possible that 2 ⩽ m ⩽ 7 in 1.1 can be replaced
with 2 ⩽ m ⩽ 4. The proof of 1.1 implies the following corollary (which implies a linear
time algorithm for detecting a 2m-cycle):

the electronic journal of combinatorics 20(2) (2013), #P7 1

Figure 1: A 3-connected cubic planar graph, with no 4- or 8-cycles.

1.2. There exists an absolute constant, c, such that every 3-connected cubic plane graph
G has a face f ∈ F (G) with |f | ⩽ 71 and a subgraph H ⊆ G with |V (H)| ⩽ c such that
the following holds:

1. f ⊆ H and for every v ∈ V (H) there exists u ∈ V (f ) and a path of length at most
six between v and u in H.

2. H contains a 2
m-cycle, for some 2 ⩽ m ⩽ 7.

We say that two cycles in a graph intersect if they have at least one vertex in common.
Thus, if two cycles in a cubic graph intersect, then they have at least one edge in common.
It is well-known that two distinct faces in a 3-connected plane graph have at most one
edge in common (or equivalently, the dual graph of a 3-connected plane graph is simple).
As this fact is used frequently, it is stated in the following lemma.

1.3. Let G be a 3-connected cubic plane graph, and let f1, f2 ∈ F (G) be distinct. Then
either f1 and f2 are disjoint, or V (f1) ∩ V (f2) = {u, v} and uv ∈ E(G).

For a graph G, we denote by G \ X the graph obtained by deleting X, where X can
be a vertex or an edge, or a set of vertices or edges. For a set X ⊆ V (G), we denote by
G[X] the subgraph of G induced by the vertices of X. Similarly, for a set X ⊆ E(G),
G[X] is the subgraph of G induced by the edges of X.
For subgraphs A1, A2 ⊆ G, disjoint means vertex-disjoint. By A1 ∪ A2 we mean the
subgraph of H with vertex-set V (A1) ∪ V (A2) and edge-set E(A1) ∪ E(A2).
Let P be a path (we consider paths as subgraphs). It is said to be an (s, t)-path if its
ends are s and t. The length of P , denoted |P |, is its number of vertices (note the unusual
notation). If P = ∅, then |P | = 0; otherwise s ̸= t or |P | = 1. Let S ⊆ G. We say that P
is internally-disjoint from S, if P and S are disjoint except possibly for the endpoints of
P . Let H be a 2-connected plane graph. The set of vertices, edges and faces of H are
denoted by V (H), E(H) and F (H), respectively. A vertex v ∈ V (H) is a k-vertex if its
degree is k. Similarly, a face f ∈ F (H) is a k-face if |V (f )| = k, and then cardinality k is
denoted as |f |. We write ⩽ k (⩾ k) for integers smaller or equal (greater or equal) to k.
For a k-vertex v ∈ V (H) we denote by ΓH(v) the set of faces incident with v. A
vertex v is a (a1, . . . , ak)-vertex, if it is a k-vertex and the faces incident with v have size
(in either a clockwise or an anti-clockwise order around v) a1, . . . , ak.
For a face f ∈ F (H), we denote by ΓH(f ) the set of faces adjacent to f . A face f
is a (a1, . . . , ak)-face, if it is a k-face and the faces adjacent to f have size (in either a
clockwise or an anti-clockwise order around v) a1, . . . , ak.

the electronic journal of combinatorics 20(2) (2013), #P7 2

If C is a cycle in a plane graph then int(C) (ext(C)) is the set of vertices and edges
inside (outside) C but not on C.

Sketch of proof. We prove 1.1 by a way of contradiction. Suppose that the theorem
is false and let G be a counterexample. We start by deﬁning a set ℑall of graphs having
some special properties. Then for every f ∈ F (G) we deﬁne a set of subgraphs of G, Πf ,
as follows:

1. Every member of Πf is isomorphic to some member of ℑall.

2. The members of Πf are “almost” pairwise disjoint.

3. Every member of Πf has at least one edge in common with f .

4. Subject to (1), (2) and (3), |Πf | is maximal.

For each X ∈ ℑall, let SX be the number of graphs in Πf isomorphic to X. Then, by the
assumption that G contains no 2m-cycles (m = 2, . . . , 7), we show that for every X ∈ ℑall
there is a constant cX such that ∑

X∈ℑall SX · cX ⩽ ϕ(|f |). (Where ϕ : N → N is a predeﬁned

function and N is the set of positive integers.) Then, using the Discharging Method, we
show that there is a face f ∈ F (G) for which ∑

X∈ℑall SX · cX > ϕ(|f |), thus obtaining a

contradiction to the existence of G.

Organization. In Section 2 we study the intersection between sets of faces of relatively
small lengths in a counterexample, G. In Section 3 the set ℑall is deﬁned, and for every
f ∈ F (G), the set Πf is constructed. In Section 4, we show how the members of Πf are
used to construct cycles of prescribed lengths. Finally, in Section 5, the main theorem is
proved using the discharging method. This is done by formulating and solving a set of
integer linear programs.

2 Basic Properties of a Counterexample

Throughout G denotes a counterexample to 1.1, that is,

(*) G is a 3-connected plane graph with no 2
m-cycles (m = 2, . . . , 7).

The following topological lemma will be useful.

2.1. Let C be a cycle of G and let v1, u1, v2 and u2 be four vertices of C appearing in order
in a clockwise (or anti-clockwise) traversal of C starting from v1. Then there do not exist
two disjoint paths P and Q, internally disjoint from C, such that P is a (v1, v2)-path, Q
is a (u1, u2)-path, and V (P ), V (Q) ⊆ V (f ) for some f ∈ F (G).

The following lemma is straightforward.

2.2. For m = 2, . . . , 7, the following holds in G:

1. Let f1, . . . , fk ∈ F (G) be distinct such that the subgraph of the dual graph of G,
induced by the vertices corresponding to f1, . . . , fk is a tree (i.e, a connected acyclic

graph). Then
 k∑

i=1 |fi| ̸= 2(k − 1) + 2m.

the electronic journal of combinatorics 20(2) (2013), #P7 3

2. If v ∈ V (G) be a (p, q, r)-vertex (p, q, r ∈ N), then p + q + r ̸= 6 + 2m.

3. Let f1, f2 ∈ F (G) be adjacent. Let g1, g2, g3 ∈ F (G) \ {f1, f2} be distinct 3-faces,
and suppose that for i = 1, 2, gi is adjacent to f1 and f2. Then g3 is disjoint from
at least one of f1 and f2.

The following corollary will be used frequently.

2.3. The following holds for G:

(0) there are no 4-, 8- or 16-cycles.

(1) no two 3-faces are adjacent.

(2) no two 5-faces are adjacent.

(3) a 6-face is adjacent to at most one 3-face.

(4) G contains no (3, 5, 6)-vertex.

(5) no two 9-faces are adjacent.

(6) G contains no (9, 3, 10)-vertex.

2.1 Properties of a 3-face not adjacent to 5-faces

Let f ∈ F (G) be a 3-face in G. Let x1, x2, x3 be the vertices of f in a cyclic clockwise
ordering. Let yi (i = 1, 2, 3) be the neighbor of xi other than xi−1 and xi+1. Set x4 := x1,
x0 := x3, y4 := y1 and y0 := y3. As G is simple, yi ̸∈ V (f ). By 2.3(0), for distinct
1 ⩽ i, j ⩽ 3, yi ̸= yj. Let fi ∈ F (G) \ {f } (i = 1, 2, 3) such that fi is incident to xixi+1.
Suppose fi = xiyipi
1pi
2 . . . pi
|fi|−4yi+1xi+1 and let P i = pi
1pi
2 . . . pi
|fi|−4.
By 1.3, V (fi) ∩ V (fi+1) = {xi+1, yi+1}, and hence for distinct 1 ⩽ i, j ⩽ 3, P i and
P i+1 are disjoint. Also by 2.3(0,1), |P i| ⩾ 1, for i = 1, 2, 3. Let

S = f1 ∪ f2 ∪ f3

Two disjoint faces f ′, f ′′ ∈ F (G) are called semi-adjacent if there exist v ∈ V (f ′) and
u ∈ V (f ′′) such that uv ∈ E(G). Note that cubicity of G implies that a k-face has at
most k semi-adjacent faces. For i = 1, 2, 3, let gi be the face incident with yi, other than
fi−1 and fi. Then g1, g2, g3 are the three semi-adjacent faces of f .

2.1.1 Properties of a 3-face adjacent to three 6-faces

Assume that |fi| = 6, for i = 1, 2, 3. The following claim follows merely from 2.3(0).

2.4. Let 1 ⩽ i ⩽ 3, 1 ⩽ j ⩽ 2 and let Q be a (pi
j, p
i+1
j )-path internally disjoint from S
(where p4
j := p1
j ). Then |Q| = 5 or |Q| ⩾ 13.

2.5. Let f ∗ ∈ F (G) \ {f, f1, f2, f3} and suppose V (f ∗) ∩ V (S) ̸= ∅.

1. If f ∗ = gi (for some i ⩽ i ⩽ 3) and |f ∗| ⩽ 18, then |V (S) ∩ V (gi)| = 3.

2. If |f ∗| ⩽ 9 and f ∗ ̸= gi (for some i = 1, 2, 3), then |V (S) ∩ V (f ∗)| = 2.

the electronic journal of combinatorics 20(2) (2013), #P7 4

Proof. (1) Without loss of generality assume that f ∗ = g1. Let k = |V (g1)| − 3. Put
q0 := p3
2, qk+1 := p1
1 and qk+2 = y1. Let Q := q1 . . . qk be a path on g1 such that for
0 ⩽ i ⩽ k, qiqi+1 ∈ E(f ). As q0, qk+1, qk+2 ∈ V (g1) ∩ S, we have to show that Q and S
are disjoint.
Suppose to the contrary that Q and S are not disjoint. By 1.3, y2, y3, p
1
2, p
3
1 /∈ V (Q) ∩
V (S). As G is cubic, |V (g1) ∩ S| = 5 and V (Q) ∩ V (S) = {p2
1, p
2
2}. Let 1 ⩽ j ⩽ k such
that qj ∈ V (S), and if k ⩾ 2, then q1, . . . , qj−1 /∈ V (S). Let Q1 = q0q1 . . . qj−1qj and
Q2 = qj+1 . . . qk+1. By deﬁnition, Q1 and Q2 are disjoint and each is internally-disjoint
from S. By 2.1, Q1 is a (q0, p
2
2)-path, and Q2 is a (qk+1, p
2
1)-path. As |g1| ⩽ 18 and
|V (g1) ∩ S| = 5, we see that |Q1| + |Q2| = |g1| − 1 ⩽ 17. By 2.4, it must be that
|Q1| = |Q2| = 5. But then S ∪ Q1 ∪ Q2 ⊆ G contains a 16-cycle; a contradiction.

(2) For i = 1, 2, 3, let hi denote the face adjacent to fi so that E(fi) ∩ E(hi) = {pi
1pi
2} and

suppose that hi ̸= {g1, g2, g3}. Then |E(S) ∩ E(hi)| ⩾ 1 and E(hi) ∩ E(S) ⊆
 3⋃

i=1
{pi
1pi
2}.

Now suppose to the contrary that for some 1 ⩽ i ⩽ 3 there exist 1 ⩽ j ̸= i ⩽ 3 so that
pj
1pj
2 ∈ E(hi). By symmetry we may assume that i = 1 and j = 2. By 2.1, there is a
(p1
2, p
2
1)-path Q ⊆ h1 internally disjoint from S. If |Q| = 2 (then g2 is a 3-face) and we get
a contradiction to 2.3. If |Q| ⩾ 3 then {p1
2, p
2
1} is a 2-cut in G contradicting 3-connectivity
of G.

2.6. Let 1 ⩽ i, j ⩽ 3 be distinct. If 5 ⩽ |gi|, |gj| ⩽ 7, then gi and gj are disjoint.

Proof. Suppose not. By symmetry, assume that i = 1, j = 2. By 1.3, |V (g1) ∩ V (g2)| = 2.
Let k := |V (g1)| − 3 and k′ := |V (g2)| − 3. Let Q
1 := q1 . . . qk ⊆ g1 (Q
2 = u1 . . . uk′ ⊆
g2), such that y1 ̸∈ V (Q1) (y2 ̸∈ V (Q2)), {q1p3
2, qkp1
1} ⊆ E(g1) ({u1p1
2, uk′p2
1} ⊆ E(g2)),
and for 1 ⩽ i ⩽ k − 1 (1 ⩽ i ⩽ k′ − 1), qiqi+1 ∈ E(g1) (uiui+1 ∈ E(g2)). By 2.5, Q1 and
Q2 are disjoint from S and since |V (g1) ∩ V (g2)| = 2 then |V (Q1) ∩ V (Q2)| = 2.
There exist 1 ⩽ ℓ ⩽ k − 1 and 1 ⩽ ℓ
′ ⩽ k′ − 1 such that qℓ = uℓ′+1 and qℓ+1 = uℓ′.
Then the length of the path P1 = p3
2, q1, . . . , qℓ = uℓ′+1, uℓ′+2, . . . , p2
1 is at least 6 (for
otherwise there is an 8-cycle in G). Similarly, the length of the path P2 = p1
2, u1, . . . , uℓ′ =
qℓ+1, qℓ+2, . . . , p1
1 is at least ﬁve. Then |g1|+|g2| = |P1|+|P2|+4 ⩾ 15 (where the +4 comes
from the fact that y1, y2 ̸∈ V (P1 ∪ P2) and that each of qℓ and qℓ′ is contained in exactly
one of V (P1) and V (P2) and in both of V (g1) and V (g2)), but this is a contradiction since
|g1|, |g2| ⩽ 7.

The following is an easy consequence of 2.3(0) and 2.6.

2.7. If 5 ⩽ |gi| ⩽ 7 (1 ⩽ i ⩽ 3), then |gi−1|, |gi+1| ⩾ 10.

2.8. Let f ∗ ∈ F (G) \ {f, f1, f2, f3} and suppose |f ∗| ∈ {3, 9}. Then f ∗ and S are disjoint.

Proof. Suppose not. By 2.3(3) and the assumption that f ∗ ̸= f , we may assume that
|f ∗| = 9. We may also assume that f ∗ ̸= gi, for i = 1, 2, 3. For if f ∗ = g1, say, then by 2.5,
|V (g1) ∩ V (S)| = 3. Hence, V (g1) ∩ V (S) = {p3
2, y1, p
1
1}, and C := (S ∪ f ∗) \ {p1
2, x2} is a
16-cycle, a contradiction.
By 2.5, |V (f ∗) ∩ V (S)| = 2, and by symmetry we may assume that E(f ∗) ∩ E(S) =
{p1
1p1
2}. But then f ∗ ∪ f1 ∪ f2 ⊆ G contains a 16-cycle; a contradiction.

2.9. Let f ∗
1 , f ∗
2 ∈ F (G) \ {f, f1, f2, f3} be distinct. Suppose that |f ∗
1 |, |f ∗
2 | ∈ {5, 6} and
S ∩ (f ∗
1 ∪ f ∗
2 ) ̸= ∅. Then

the electronic journal of combinatorics 20(2) (2013), #P7 5

1. If 5 ∈ {|f ∗
1 |, |f ∗
2 |}, then (i) S is disjoint from f ∗
1 or f ∗
2 , and (ii) f ∗
1 and f ∗
2 are not
adjacent.

2. If |f ∗
1 |, |f ∗
2 | = 6 and f ∗
1 and f ∗
2 are adjacent, then S is disjoint from f ∗
1 or f ∗
2 .

Proof. (1) First observe that (ii) follows from (i) and the assumption that G contains
no 16-cycles. For the proof of (i), we assume for a contradiction that S ∩ f ∗
1 ̸= ∅ and
S ∩ f ∗
2 ̸= ∅. Without loss of generality, assume that |f ∗
1 | = 5.
We may assume that |f ∗
2 | = 6. For if |f ∗
2 | = 5, then by 2.3(2) and by 2.2(1), the union
of f ∗
1 and f ∗
2 and two (appropriate) faces from {f1, f2, f3} form a 16-cycle, a contradiction.

Case 1. Suppose f ∗
1 = gi, for some 1 ⩽ i ⩽ 3. By symmetry assume that f ∗
1 = g1.
By 2.7, f ∗
2 ̸∈ {g2, g3}. Since S ∩ f ∗
2 ̸= ∅, E(S) ∩ E(f ∗
2 ) ⊆ {p1
1p1
2, p
2
1p2
2, p
3
1p3
2}. By 2.5,
|V (S) ∩ V (f ∗
2 )| = 2. Hence, there is a unique 1 ⩽ j ⩽ 3 such that E(S) ∩ E(f ∗
2 ) = {pj
1pj
2}.
If j ∈ {1, 3}, say j = 1, then f ∗
1 and f ∗
2 are adjacent. But then (S ∪ f ∗
1 ∪ f ∗
2 ) \ {x3} ⊆ G
contains a 16-cycle, a contradiction. Assume j = 2. Let f ∗
2 := p2
1u1u2u3u4p2
2 and let
Q := f ∗
2 \ {p2
1, p
2
2}. By 2.5, Q and S are disjoint. We may assume that f ∗
1 and f ∗
2 are not
disjoint (and hence |V (f ∗
1 ) ∩ V (f ∗
2 )| = 2), for otherwise (S ∪ f ∗
1 ∪ f ∗
2 ) \ {p3
1, x2} ⊆ G is a 16-
cycle. By 2.1 and since |f ∗
1 | = 5, we have that p2
3u4 ∈ E(G), p2
3u3 ∈ E(G) or p2
3u2 ∈ E(G).
But then we easily see that S ∪ f ∗
1 ∪ f ∗
2 ⊆ G contains an 8-cycle; a contradiction.

Case 2. Suppose that f ∗
1 ̸= gi, for i = 1, 2, 3. By the same arguments as in Case (1),
we conclude that f ∗
2 ̸= gi, for i = 1, 2, 3. By symmetry, we may assume that E(f ∗
1 ) ∩
E(S) = {p1
1p1
2} and E(f ∗
2 ) ∩ E(S) = {p2
1p2
2}. Let f ∗
1 := p1
1u1u2u3p1
2p1
1, Q1 := f ∗
1 \ {p1
1, p
1
2},
f ∗
2 := p2
1v1v2v3v4p2
2p2
1 and Q2 := f ∗
2 \ {p2
1, p
2
2}. As in Case (1), we see that f ∗
1 and f ∗
2 must
be adjacent. By 2.1, we have that u1 ∈ {v2, v3, v4} or u3 ∈ {v1, v2, v3}. But then, in all
cases, we can easily ﬁnd an 8-cycle in S ∪ f ∗
2 ⊆ G; a contradiction.
(2) The proof follows by the similar argument as the proof of (1).

2.10. Suppose |gi| ∈ {17, 18} (for some 1 ⩽ i ⩽ 3). Suppose also that there exist f ′, f ′′ ∈
F (G) \ {f, f1, f2, f3} such that |f ′| ∈ {5, 6}, |f ′′| = 3, f ′, f ′′ and gi are pairwise adjacent.
If (S ∩ gi) ∩ (f ′ ∪ f ′′) = ∅, then S ∩ (f ′ ∪ f ′′) = ∅.

Proof. For suppose not. By symmetry assume that gi = g1. By 2.5(1), V (g1) ∩ V (S) =
{p1
1, y1, p
3
2}. Let k := |V (g1)| − 3. Let Q := q1 . . . qk ⊆ g1 such that y1 ̸∈ V (Q1),
{q1p3
2, qkp1
1} ⊆ E(g1), and for 1 ⩽ i ⩽ k − 1, qiqi+1 ∈ E(g1). Let 1 ⩽ r < ℓ ⩽ k such that
V (g1) ∩ V (f ′′) = {qr, qℓ}. Let v ∈ V (f ′′) \ {qr, qℓ}. Clearly, S ∩ f ′′ = ∅. As f ′ is adjacent
to g1 and f ′′, then by symmetry, we may assume that V (g1) ∩ V (f ′) = {qℓ, qℓ+1}.
Hence (as S ∩ f ′′ = ∅ but S ∩ (f ′ ∪ f ′′) ̸= ∅), S ∩ f ′ ̸= ∅. Let Q
∗
1 := p3
2q1 . . . qr ⊆ g1
and Q
∗
2 := qℓ+1 . . . qkp1
1 ⊆ g1.
Next we show that f ′ /∈ {g2, g3}. If f ′ = g2, then by 2.5, V (S) ∩ V (f ′) = {p2
1, y2, p
1
2}.
Hence, it can only be that |f ′| = 6. By 2.1, p1
2qℓ+1 ∈ E(G). Also ℓ + 1 ̸= k (for otherwise
G[f ∪ f1 ∪ qk] contains an 8-cycle). Hence, |Q
∗
2| ⩾ 3; but then {p1
1, pℓ+1} is a 2-cut in G; a
contradiction. Similarly, if f ′ = g3, then as above V (S) ∩ V (f ′) = {p2
2, y3, p
3
1} and |f ′| = 6.
By 2.1, vp
3
1 ∈ E(G). By 2.3(0), r ̸= 1; but then {p3
2, qr} is a 2-cut in G; a contradiction.
So assume that f ′ ̸∈ {g2, g3}. As (S ∩ g1) ∩ (f ′ ∪ f ′′) = ∅, then V (f ′′) ∩ V (S) =
{p2
1, p
2
2}. By 2.1, there are disjoint paths Q1, Q2, internally-disjoint from S, such that
V (Q1), V (Q2) ⊆ V (f ′), Q1 is a (v, p2
2)-path, and Q2 is a (qℓ+1, p
2
1)-path. As 5 ⩽ |f ′| ⩽ 6
and ℓ /∈ V (Q1 ∪ Q2), |Q1| + |Q2| ⩽ 5. Hence, |Q1| = 2 or |Q2| = 2.
We shall assume that |Q1| = 2 (as the case that |Q2| = 2 and thus p2
1qℓ+1 ∈ E(G)
follows through similar arguments). Hence we have that p2
2v ∈ E(G) and 2 ⩽ |Q2| ⩽ 3.

the electronic journal of combinatorics 20(2) (2013), #P7 6

Now, using 2.3(0), it is easily veriﬁed (even regardless of the exact value of |Q2|), that
|Q
∗
2| ̸∈ {2, . . . , 10}. As |g1| ∈ {17, 18}, and y1, qℓ ̸∈ V (Q
∗
1) ∪ V (Q∗
2), then |Q
∗
1| + |Q∗
2| ⩽ 16.
Hence, we conclude that 2 ⩽ V |Q
∗
1| ⩽ 6. But then (for each possible value of |Q
∗
1|) it is
easy to ﬁnd an 8− or 16-cycle; a contradiction.

2.1.2 Properties of a 3-face adjacent to two 6-faces and a 9-face

Next we assume that f is adjacent to two 6-faces and a 9-face.

2.11. Let f ∗ ∈ F (G)\{f, f1, f2, f3} such that |f ∗| ∈ {5, 6, 9}. Then, S and f ∗ are disjoint,
unless |f ∗| = 9 and f ∗ and f are semi-adjacent so that the edge with one end in V (f ) and
one end in V (f ∗) is common to the two 6-faces.

Proof. Suppose not. By symmetry assume that |f1| = |f2| = 6 and |f3| = 9.

Case 1. Suppose f ∗ = gi, for some i, 1 ⩽ i ⩽ 3. Then either f ∗ = g2 or f ∗ ∈ {g1, g3}.
We shall consider the former case as the latter follows by similar arguments.
Suppose then that f ∗ = g2. Let k := |V (g2)| − 3. Put q0 = p1
2, qk+1 := p2
1 and
qk+2 := y2. Let Q := q1q2 . . . qk ⊆ g2 such that qiqi+1 ∈ E(g2), for i = 0, . . . , k. We
may assume that |V (S) ∩ V (f ∗)| > 3. For otherwise, if |f ∗| = 9 the claim follows, and if
|f ∗| = {5, 6}, then S ∪ f ∗ contains a 16-cycle, a contradiction.
By 1.3, we see that y1, y3, p
1
1, p
2
2 /∈ V (Q) ∩ V (S) and conclude that |V (Q) ∩ V (S)| = 2.
By 2.3(5), we may assume that |g2| ∈ {5, 6}. By 2.3(0), neither p1
2 nor p2
1 is adjacent to
any of p3
1, . . . , p3
5. Hence, |V (Q) ∩ S| = |V (Q) ∩ V (f3)| ⩽ 1; a contradiction.

Case 2. Suppose f ∗ ̸= gi, for i = 1, 2, 3.

Case 2.1 Suppose V (f ∗) ∩ V (f3) ̸= ∅. As by Case (1), f ∗ ̸= gi, for i = 1, 2, 3,
then E(f ∗) ∩ E(f3) = {p3
rp3
ℓ }, for some 1 ⩽ r < ℓ ⩽ 5. By 2.3(5), we may assume
that |f ∗| ∈ {5, 6}. We see that f ∗ is disjoint from f1 or f2. For otherwise, by Case (1),
{p1
1, p
1
2, p
2
1, p
2
2, p
3
r, p
3
ℓ } ⊆ V (f ∗). By 2.2, |f ∗| ̸= 5, and if |f ∗| = 6, then by 2.1, p1
2p2
1 ∈ E(G),
contradicting 2.3(3).
Next we show that f ∗ is disjoint from f1 and f2. For suppose not. By symmetry,
assume that V (f ∗) ∩ V (f1) ̸= ∅ and V (f ∗) ∩ V (f2) = ∅. Now, if |f ∗| = 5, then by 2.2(1),
G[f2 ∪ f3 ∪ f ∗] contains a 16-cycle. If |f ∗| = 6, then G[f ∪ f3 ∪ f2 ∪ f ∗] \ {x3} is a 16-cycle.
Both cases lead to a contradiction. Hence we may assume that f ∗ is disjoint from f1 and
f2. But then as |f ∗| ∈ {5, 6}, S ∪ f ∗ ⊆ G contains a 16-cycle, a contradiction.

Case 2.2 Suppose V (f ∗) ∩ V (f3) = ∅. By Case (1) and 2.2(1), we may assume that
V (f ∗) ∩ V (f1) ̸= ∅ and V (f ∗) ∩ V (f2) ̸= ∅. Let k := V (f ∗) − 4. By Case (1), and 2.1,
there are disjoint paths Q1, Q2 ⊆ V (F ∗), internally-disjoint from S, such that Q1 is a
(p1
2, p
2
1)-path, and Q2 is a (p1
1, p
2
2)-path. As |f ∗| ⩽ 9, |Q1| + |Q2| ⩽ 9. By 2.3(0), |Q1| ⩾ 4.
Hence, |Q2| ⩽ 5. But then we easily ﬁnd an 8-cycle in S ∪ f ∗ ⊆ G; a contradiction.

2.2 Properties of a 5-face not adjacent to a 3-face

Let f ∈ F (G) be a 5-face, which is not adjacent to a 3-face. Let x1, x2, x3, x4, x5 be the
vertices of f in a cyclic ordering. Let yi, 1 ⩽ i ⩽ 5, be the neighbor of xi other than xi−1
and xi+1 (throughout x0 := x5, x6 := x1, y0 := y5, and y6 := y1).

2.12. For distinct 1 ⩽ i, j ⩽ 5, yi ̸= yj.

the electronic journal of combinatorics 20(2) (2013), #P7 7

Proof. For suppose not. Without loss of generality assume that i < j. If j ̸= i + 1,
then G contains a 4-cycle. If j = i + 1, then as f is not adjacent to a 3-face, it must
be that intC = {xi, xi+1, yi} ̸= ∅; but then yi is a cut-vertex. In both cases we obtain a
contradiction to the deﬁnition of G.

Let fi ∈ F (G) \ {f } (i = 1, . . . , 5) such that fi is incident to xixi+1. Suppose fi =
xiyipi
1pi
2 . . . pi
|fi|−4yi+1xi+1 and let P i = pi
1pi
2 . . . p
i
|fi|−4. By 2.3(0,2), |P i| ⩾ 2 (i = 1, . . . , 5).

2.13. Let i and j be distinct, 1 ⩽ i, j ⩽ 5, and assume that j ̸= i + 1 and j ̸= i − 1. If
|fi| = |fj| = 6, then fi and fj are disjoint.

Proof. By symmetry assume that i = 1 and j = 3. Let S = V (f ) ∪ {y1, . . . , y5} ∪ V (P 1).
By 2.12, |S| ⩾ 10. Next we show that |S| = 12. As f1 is adjacent to f, f2 and f5, then
V (P 1) ∩ (V (f ) ∪ {y3, y5}) = ∅. Now, if |S| < 12, then V (P 1) ∩ {y4} ̸= ∅ and p1
1 = y4 or
p1
2 = y4, and by symmetry we may assume that p1
2 = y4
Let C := x2y2y4x4x3. By symmetry we may assume that y3 ∈ int(C). If (Γ(y2) ∪
Γ(y4)) ∩ ext(C) = ∅, then {x1, x5} is a 2-cut in G, separating y3 and y1. If (Γ(y2) ∪
Γ(y4)) ∩ int(C) = ∅, then x3 is a cut-vertex in G, separating y3 and y1. Hence we have
that Γ(y2)∩int(C) = ∅ and Γ(y4)∩int(C) ̸= ∅ or Γ(y4)∩int(C) = ∅ and Γ(y2)∩int(C) ̸= ∅.
In the former case, {x3, y4} is a 2-cut in G separating y3 and y1, and in the latter case,
{x3, y2} is a 2-cut in G separating y3 and y1. Hence |S| = 12.
Now, let v ∈ S \ {y4, x4}. We see that y4v /∈ E(G). For if y4v ∈ E(G), then by 2.12,
v /∈ V (f ) \ {x4}, and by 2.3(0), v ∩ {y3, y5} = ∅. Hence, it must be that v ∈ {y1, p
1
1, p
1
2, y2};
but then it is easily seen that G contains an 8-cycle.
Hence we have shown that V (f1) ∩ {p3
2} = ∅, and together with the fact that |S| = 12,
we conclude that V (f1) ∩ {y4, y3, p
3
2} = ∅. Hence |V (f1) ∩ V (f3)| ⩽ 1, and by 1.3, f1 and
f3 are disjoint.

2.14. Suppose that |fi| ⩾ 6 (for some 1 ⩽ i ⩽ 5). If f is a (6, 6, 6, 6, |fi|)-face, then
|fi| = 6 or |fi| ⩾ 10.

Proof. By symmetry assume that fi = f1 (and then |fj| = 6, for j = 2, . . . , 5). Now,

assume for a contradiction that 7 ⩽ |fi| ⩽ 9. Clearly, |fi| ̸= 8. Let S = f ∪
 5⋃

i=2 fi. By 2.13,

|V (S)| = 18.
It must be that f1 is adjacent both to f3 and f4, for otherwise one of f1 ∪ f ∪ f3 or
f1 ∪ f ∪ f4 (if |f1| = 9) or one of f ∪ f1 ∪ f2 ∪ f4 or f ∪ f1 ∪ f3 ∪ f5 (if |f | = 7) contains a
16-cycle. Hence, f1 is semi-adjacent to f via the edge x4y4. Let Q1 ⊆ f1 (resp., Q2 ⊆ f2)
be the p4
1y1-path (resp., p3
2y2-path) on f1. Since |f1| ⩽ 9, there exist 1 ⩽ i ⩽ 2 so that
|Qi| ⩽ 4. But then it is easily seen that Qi ∪ S contains an 8-cycle; a contradiction.

To conclude this section, we need the following lemma, proof of which is similar to the
proof of 2.14.

2.15. Suppose |fi| = 6 (for i = 1, . . . , 5). Let gi be the face incident to yi, other than fi−1
and fi+1 (that is {g1, . . . , g5} is the set of semi-adjacent faces of f ). Then, |gj| ⩾ 10, for
1 ⩽ j ⩽ 5.

the electronic journal of combinatorics 20(2) (2013), #P7 8

3 Chains and Clusters

Let f ∈ F (G) be a k-face. Let x1, . . . , xk ∈ V (f ) be the vertices of f in a cyclic clockwise
ordering. Let 1 ⩽ ℓ < k, and let {f1, . . . , fℓ} ⊆ ΓG(f ). By 1.3, |E(f ) ∩ E(fi)| = 1, for
i = 1, . . . , ℓ. Let

A = {e ∈ E(f ) : there exists 1 ⩽ i ⩽ ℓ with E(f ) ∩ E(fi) = e}

We say that the faces f1, . . . , fℓ are consecutive on f , if G[A] is a connected path (note
that since ℓ < k, G[A] cannot be a cycle).
If f1, . . . , fℓ are consecutive on f , we write f1 ≺f f2 ≺f , . . . , ≺f fℓ, if when traversing
the edges of f in a clockwise order starting from E(f1) ∩ E(f ), E(fi) ∩ E(f ) is met before
E(fi+1) ∩ E(f ), for i = 1, . . . , ℓ − 1.
Now, suppose c := {f1, . . . , fℓ} is a set of consecutive faces on f . We say that c is a
chain of f , if for every 1 ⩽ i < j ⩽ ℓ with j ̸= i + 1, we have that fi and fj are disjoint
unless j = i + 2 and fi+1 is a 3-face (and then fi and fj share an edge in common).

3.1. Let c := {f1, . . . , fℓ}, 1 ⩽ ℓ ⩽ k − 2, f1 ≺f , . . . , ≺f fℓ, be a chain of f . Let
g ∈ F (G) \ ({f } ∪ c) be a 3-face, and suppose that g and fi are consecutive on f , for some
i ∈ {1, ℓ}. Then, c′ = f1 ∪ · · · ∪ fℓ ∪ g is a chain of f .

Proof. By symmetry me may assume that i = ℓ. Without loss of generality, we may
assume that E(fj) ∩ E(f ) = {xjxj+1}, 1 ⩽ j ⩽ ℓ, and then E(g) ∩ E(f ) = {xℓxℓ+1}. It
suﬃces to show that for j = 1, . . . , ℓ − 1, fj and g are disjoint. Indeed, if V (fj) ∩ V (g) ̸= ∅
(1 ⩽ j ⩽ ℓ − 1) then fj is adjacent to g, and hence, as g is a 3-face, also adjacent to f on
the edge xℓ+1xℓ+2. But then {xjxj+1, xℓ+1xℓ+2} ⊆ E(fj) ∩ E(f ), contradicting 1.3.

3.2. Let c := {f1, . . . , fℓ} ⊆ ΓG(f ), 1 ⩽ ℓ ⩽ k −1, f1 ≺f , . . . , ≺f fℓ, be a set of consecutive
faces on f . Then c is a chain of f , if one of the following conditions holds:

1. ℓ ⩽ 2.

2. ℓ = 3 and (|f1|, |f2|, |f3|) ↔
∈ {(6, 6, 5), (6, 5, 6)}.

3. ℓ = 4 and (|f1|, |f2|, |f3|, |f4|) ↔
∈ {(6, 3, 6, 5), (6, 3, 6, 6)}.

4. ℓ = 5 and

(|f1|, |f2|, |f3|, |f4|, |f5|) ↔
∈ {(5, 6, 3, 6, 5), (5, 6, 3, 6, 6), (6, 3, 6, 5, 6), (6, 6, 3, 6, 6)}

5. ℓ = 6 and (|f1|, |f2|, |f3|, |f4|, |f5|, |f6|) ∈ {(6, 3, 6, 6, 3, 6)}.

(The notation A ↔
∈ B means that either A is in B, or the reversal of A is in B, so that
(1, 2) ↔
∈ {(2, 1)}.)

Proof. We shall prove (1)-(2). Correctness of (3)-(5) follows by similar arguments. As in
the proof of 3.1, we may assume, without loss of generality, that E(fi) ∩ E(f ) = {xixi+1},
for 1 ⩽ i ⩽ ℓ. Item (1) follows immediately from 1.3.
For the proof of (2), assume that (|f1|, |f2|, |f3|) = (6, 6, 5) (if (|f1|, |f2|, |f3|) = (6, 5, 6)
then the proof follows similar arguments). Let x1, u1, u2, u3, u4, x2 ∈ V (f1) be the vertices
of f1 in a cyclic clockwise order. Similarly, let x2, u4, u5, u6, u7, x3 be the vertices of f2 in a
cyclic clockwise order. We need to show that f1 and f3 are disjoint. Suppose not. By 1.3,

the electronic journal of combinatorics 20(2) (2013), #P7 9

either E(f1) ∩ E(f3) = u1u2 or E(f1) ∩ E(f3) = u2u3. If f1 and f3 are both incident to
u2u3, then u2x4 ∈ E(G); but then x4x3u7u6u5u4u3u2x4 is an 8-cycle. If f1 and f3 are both
incident to u1u2, then u2u7 ∈ E(G); but then u7u6u5u4x2x1u1u2u7 is an 8-cycle. Both
cases lead to a contradiction. Hence, f1 and f3 are disjoint as required.

3.2 and the assumption that G contains no 16-cycles imply the following immediate
corollary.

3.3. Let f1, . . . , fℓ, 1 ⩽ ℓ ⩽ k − 1, f1 ≺f , . . . , ≺f fℓ, be a set of consecutive faces on f .
Then, (|f1|, . . . , |fℓ|) ̸∈ {(5, 6, 3, 6, 6), (5, 6, 3, 6, 5), (6, 3, 6, 5, 6), (6, 3, 6, 6, 3, 6)}.

3.1 Partition into clusters

We start by deﬁning two sets, ℑS and ℑC, of plane graphs which are depicted in Figures 2
and 3. (The speciﬁc embeddings as in the ﬁgures are important.) We identify the names
of the graphs by the lengths of their (internal) faces. Set ℑall := ℑS ∪ ℑC.

ℑS = {(3), (3, 5), (5), (3, 5, 3), (6, 3, 6), (6, 3, 6, 5), (3, 6, 6, 3),

(3, 5, 6, 3), (6, 3, 6, 6, 3), (6, 3, 6, 5, 3), (3, 6), (3, 6, 5), (9, 3, 5, 3), (3, 9, 3, 5, 3),

(3, 9, 3, 5), (5, 3, 9, 3, 5), (3, 6, 6, 3, 6, 6, 3), (3, 6, 5, 6, 3), (9, 3, 6), (3, 9, 3, 6)}

35 63 3 33 5 5 5

5 5

5
 6 6 6

6 6 6 63 3 3 3 3 33

3 3
 6 66

3
 6
 6 3

6
 9 63 3

5
 9 5 33 93 5 33 9 53 3

6 66 63 3
9 53 3 3

9 63
 5 6 363

Figure 2: The set ℑS.

ℑC = {(3, 5
3), (6
6
36), (6
6
36, 5), (6
6
36, 5, 3), (6
66
566), (665
66), (6
6
36, 6, 3),

(9, 3, 5
3), (3, 9, 3, 5
3), (5, 9, 3, 5
3), (5, 3, 9, 3, 5
3), (5
3, 3, 9, 3, 5
3), (9, 5
3, 3),

(3, 9, 5
3, 3), (5
3, 3, 9, 5, 9, 3, 5
3), (6
9
36)}

It will be convenient to partition ℑC into the following sets (see Figure 3).

ℑ
3
C = {(3, 5
3)}

the electronic journal of combinatorics 20(2) (2013), #P7 10

3 5
 3
 6 6

5 66

6 6

3
6
 6
 3
 6 5

6
 6 6

3
6
 5 3

6

6
 5
 6

6

6
 6 6

3
9

9 3 5

3
 3 9 3 5

3
 5 9 3 5
3

5 3 9 3 5
3
 5
 3
3 9 3 5

3
 9
 3
 5 3

3 9
 3
 5 3
 3
 5 3 9 5 9 3 5
3

ℑ3

ℑ5

ℑ6

ℑ6∗
C

ℑ9
 6 6

3
6
 6 3

Figure 3: The set ℑC.

ℑ
5
C = {(6
66
566), (665
66)}

ℑ
6
C = {(6
6
36), (6
6
36, 5), (6
6
36, 5, 3), (6
6
36, 6, 3)}

ℑ
6∗
C = {(6
9
36)}

ℑ9
C = {(9, 3, 5
3), (3, 9, 3, 5
3), (5, 9, 3, 5
3), (5, 3, 9, 3, 5
3), (53, 3, 9, 3, 5
3),

(9, 5
3, 3), (3, 9, 5
3, 3), (5
3, 3, 9, 5, 9, 3, 5
3)}

Next three additional subsets of ℑall are deﬁned.

ℑ
9 = ℑ9
C ∪ {(9, 3, 5, 3), (3, 9, 3, 5, 3), (3, 9, 3, 5), (5, 3, 9, 3, 5), (9, 3, 6), (3, 9, 3, 6)}

ℑF = ℑall \ {(5), (6
6
36), (6
6
36, 5), (6
9
36), (6
66
566), (6
65
66)}

the electronic journal of combinatorics 20(2) (2013), #P7 11

ℑP = ℑall \ {(5), (6
6
36), (6
6
36, 5), (6
9
36), (666
566), (6
65
66), (3, 6), (3, 6, 5)}

Note that
 ℑP ⊆ ℑF

and ℑF \ ℑP = {(3, 6), (3, 6, 5)}

For each X ∈ ℑall we deﬁne a unique path P (X) ⊆ X. The paths are depicted in
bold in Figures 2 and 3.

Let H ⊆ G (together with its induced embedding in G) and let f ∈ F (G). We say
that H is a cluster of f of type X, if the following holds:

1. H ∼= X, for some X ∈ ℑall.

2. H is a union of faces of G, each distinct from f .

3. P (H) ⊆ f .

Let H ⊆ G, f ∈ F (G), and suppose that H satisﬁes (1)-(3) with respect to f . The
type of H is denoted by t(H) (then t(H) ∈ ℑall). We denote by F (H) the set of all faces
of H excluding the unique face of H which contains P (H) entirely (note that this face is
not a face of G as it has vertices of degree two on its boundary). We denote by Chain(H),
the set of faces of H that have at least one edge in common with P (H), excluding the
unique face of H which contains P (H). The reader may verify by inspection of ℑall that
Chain(H) is a chain of f .

For f ∈ F (G), deﬁne Υf to be the set of all clusters of f . Note that distinct clusters
in Υf may not be disjoint.
Next we eliminate redundancies in Υf . This is done by constructing a set Πf ⊆ Υf
that captures the structure of Υf , but in which the clusters are pairwise disjoint as much
as possible. Let Z ⊆ ΓG(f ) be such that g ∈ Z if and only if there exist c ∈ Υf with
g ∈ F (c). Deﬁne Πf ⊆ Υf so that the following conditions holds:

• For every g ∈ Z, there exists c ∈ Πf with g ∈ F (c).

• If c ∈ Πf , then F (c) ̸⊆ F (c′) for every c′ ∈ Υf distinct from c.

Clearly, Πf is well-deﬁned.
To avoid repetition, let us extract the following short hypothesis, common to many
statements that follow.

Hypothesis A. Let f be a k-face, k ⩾ 9. Let x1, . . . , xk ∈ V (f ) be the vertices of f in a
cyclic order. Let Υf and Πf be as deﬁned above.

The following is the main lemma of this section. It asserts that under certain conditions
the clusters in Πf are “almost” pairwise disjoint.

3.4. Under Hypothesis A, let c1, c2 ∈ Πf be distinct. Then,

1. P (c1) and P (c2) are disjoint.

the electronic journal of combinatorics 20(2) (2013), #P7 12

2. If t(c1), t(c2) ∈ ℑF and k ∈ {9, 10, 17, 18}, then c1 and c2 are disjoint unless t(ci) =
(5, 9, 3, 5
3), for some 1 ⩽ i ⩽ 2, and then c3−i is disjoint from c′
i, where c′
i ⊆ ci is a
sub-cluster of ci of type (9, 3, 5
3).

3. If t(c1), t(c2) ∈ ℑP , then c1 and c2 are disjoint, unless t(c1), t(c2) = (6, 3, 6) or
t(ci) = (5, 9, 3, 5
3), for some 1 ⩽ i ⩽ 2. In the latter cases c3−i is disjoint from c′
i,
where c′
i ⊆ ci is the sub-cluster of ci of type (9, 3, 5
3).

4. If t(c1) ∈ {(6
6
36), (6
6
36, 5), (6
9
36)}, then Chain(c1) and c2 are disjoint.

5. Suppose c1, c2, . . . , cm ∈ Πf and t(ci) = (6, 3, 6) (i = 1, . . . , m). Then each ci (i =
1, . . . , m) contains a sub-cluster ˆci of type (3, 6) such that for distinct 1 ⩽ j, r ⩽ m,
ˆcj and ˆcr are disjoint.

3.4 is proved via a series of claims. We start with the following claim which greatly
facilitates the proof of 3.4.

3.5. Under Hypothesis A, let c1, c2 ∈ Πf be distinct and suppose P (c1) and P (c2) are
disjoint. Then, c1 and c2 are disjoint provided that one of the following holds:

1. t(c1) = (3, 6) and t(c2) = (3, 5), or k ∈ {9, 10, 17, 18} and t(c1), t(c2) = (3, 6)

2. k ∈ {9, 10, 17, 18}, t(c1) = (3, 6), and t(c2) = (3, 6, 5).

Proof. Let F (c1) = {g1, g2} such that |g1| = 3 and |g2| = 6. Assume, without loss of
generality, that V (g1) ∩ V (f ) = {x1, x2} and V (g2) ∩ V (f ) = {x2, x3}. Let {u1, . . . , u4} ⊆
V (g2) such that u1x2, u4x3 ∈ E(g2) and uiui+1 ∈ E(g2), for 1 ⩽ i ⩽ 3. Note that
V (g1) = {x1, u1, x2}.

(1). Assume for a contradiction that the claim is false. Let F (c2) = {f1, f2} such that
|f1| = 3 and |f2| ∈ {5, 6}. Since P (c1) and P (c2) are disjoint, E(f ) ∩ (E(f1) ∪ E(f2)) =
{xjxj+1, xj+1xj+2}, for some 4 ⩽ j ⩽ k − 1.
Two cases are possible. Either E(f )∩E(f1) = {xjxj+1} or E(f )∩E(f1) = {xj+1xj+2}.
We prove the former case. The latter case is resolved using the exact same argument.
Let v ∈ V (f1), other than xj and xj+1. Since P (c1) and P (c2) are disjoint, f1 ∩
(g1 ∪ g2) = ∅. Hence V (c1) ∩ V (c2) ⊆ V (f2), and together with 1.3, it follows that
|E(c1) ∩ E(c2)| = 1. Since P (c1) and P (c2) are disjoint and g1 is a 3-face, f2 is adjacent
to g2 on the edge u2u3 or u3u4.
We show that |f2| ̸= 5. For suppose |f2| = 5. If f2 and g2 are adjacent on u2u3, then
by 2.1, vu3, xj+2u2 ∈ E(G). Let C := xj+2xj+3 . . . xkx1u1u2xj+2. If xj+2 = xk, then C is a
4-cycle, otherwise {xj+2, x1} is a 2-cut; a contradiction. If f2 and g2 are adjacent on u3u4,
then by 2.1, vu4, xj+2u4 ∈ E(G). Let C := u4x3x4 . . . xjvu4. If j = 4, then C is a 4-cycle,
otherwise, {x3, xj} is a 2-cut; all cases lead to a contradiction, and hence |f2| ̸= 5.
Suppose then that |f2| = 6 and k ∈ {9, 10, 17, 18}. Let S = f ∪ g1 ∪ g2 ∪ f1. Let Q1 and
Q2 be two paths such that V (Q1), V (Q2) ⊆ V (f ), Q1 = xj+3 . . . xk, and Q2 = x4 . . . xj−1
(possibly Q1 or Q2 are empty).

Case 1. Suppose that E(f2) ∩ E(g2) = {u2u3}. First we see that xj+2u2 /∈ E(G).
Indeed, if xj+2u2 ∈ E(G), let C := xj+2xj+3 . . . xkx1u1u2xj+2. If Q1 is empty, then xj+2 =
xk, and C is a 4-cycle. If |Q1| ⩾ 1, then {xj+2x1} is a 2-cut. Hence, xj+2u2 /∈ E(G). By 1.3
and as |f2| = 6, it follows that u3v ∈ E(G) and there is z ∈ V (f2), such that z ̸∈ V (S)

the electronic journal of combinatorics 20(2) (2013), #P7 13

and zu2, zxj+2 ∈ E(G). As k ∈ {9, 10, 17, 18}, then |Q1| + |Q2| ∈ {3, 4, 11, 12}. By 2.3(0),
it is easily seen that that |Q1| ∈ {1, 4, 5, 12}. Hence, as |Q1| + |Q2| ∈ {3, 4, 11, 12},
|Q2| ∈ {0, 1, 2, 3, 6, 7, 8, 10, 11}. But then it can be easily veriﬁed that for each possible
value of V (Q2), G contains an 8− or 16-cycle; a contradiction.

Case 2. Assume that E(f2) ∩ E(g2) = {u3u4}. As in Case (1), we ﬁrst show that
vu4 /∈ E(G). Indeed, if vu4 ∈ E(G), then let C = u4x3x4 . . . xjv. If Q1 is empty, then
xj = x4 and C is a 4-cycle. If |Q1| ⩾ 1 then {x3xj+1} is a 2-cut. Hence, vu4 /∈ E(G).
By 1.3 and as |f2| = 6, it follows that u3xj+2 ∈ E(G), and there is z ∈ V (f2) such that z ̸∈
V (S), and zu4, zv ∈ E(G). As k ∈ {9, 10, 17, 18} |Q1| + |Q2| ∈ {3, 4, 11, 12}. By 2.3(0),
it is easily seen that that |Q1| ∈ {4, 12}. Hence, as |Q1| ∈ {4, 12}, |Q2| ∈ {0, 7, 8}, and
again it is easy to ﬁnd an 8− or a 16-cycle in G; a contradiction.
(2) This part follows similar arguments as the proof of (1).

3.6. Under Hypothesis A, let c1, c2 ∈ Πf be distinct, and suppose that P (c1) and P (c2) are
disjoint. Then c1 and c2 are disjoint provided that one of the following conditions holds:

1. t(c1) = (6, 3, 6, 5) and t(c2) ∈ {(3, 6), (3, 6, 5)}.

2. t(c1) = (3, 6, 6, 3) and t(c2) ∈ {(6, 3, 6), (3, 6, 6, 3), (3, 6, 6, 3, 6, 6, 3)}.

3. t(c1) ∈ {(3, 6, 5, 3), (3, 6, 5, 6, 3)} and t(c2) ∈ {(3, 5), (3, 6)}.

4. t(c1) = (6, 3, 6, 6, 3) and t(c2) ∈ {(6, 3, 6), (3, 6, 6, 3)}.

Proof. Let F (c1) = {f1, . . . , fℓ} such that ℓ = |F (c1)|. Assume, without loss of generality,
that E(f ) ∩ E(fi) = {xixi+1}, for 1 ⩽ i ⩽ ℓ. By symmetry, we may assume that if c1 is
of type (a1, . . . , aℓ), then |fi| = ai, for 1 ⩽ i ⩽ ℓ. We prove Item (1). Items (2)-(4) are
proved in a similar way.
Assume for a contradiction that (1) holds, but V (c1) ∩ V (c2) ̸= ∅. Let g ∈ F (c2) such
that V (g)∩V (c1) ̸= ∅. Clearly, disjointness of P (c1) and P (c2) imply that F (c1)∩F (c2) =
∅. We may also assume that |g| ̸= 3. For if |g| = 3, then it must be that V (g) ∩ V (f4) ̸= ∅.
But then we get a contradiction to 1.3, unless f4 and g are consecutive of f . But this is
impossible as P (c1) and P (c2) are disjoint.
First we describe the settings. Let u1, . . . , u4 ⊆ V (f1) such that u1x1, u4x2 ∈ E(f ) and
uiui+1 ∈ E(f1), 1 ⩽ i ⩽ 3. Let u4, u3, u5, u6 ⊆ V (f3) such that u6x4, u3u5, u5u6 ∈ E(f3).
Let u7, u8 ⊆ V (f4) such that u6u7, u7u8, u8x5 ∈ E(f4). Let g1, g2 ∈ F (G) and if t(c2) =
(3, 6, 5) let also g3 ∈ F (G) so that: g1, g2 or g1, g2, g3 (if g3 is deﬁned) are consecutive on
f , F (c2) ⊆ {g1, g2, g3}, |g1| = 3, |g2| = 6, and if t(c2) = (3, 6, 5), then |g3| = 5.
We may assume that |V (g)∩V (c1)| ̸= 2. For if |V (g)∩V (c1)| = 2, then E(g)∩E(c1) ∈
{u1u2, u7u8}, and |g| ∈ {5, 6}, c1 ∪ g ⊆ G contains a 16-cycle. Hence, |V (g) ∩ V (c1)| ⩾ 3.
Since g ̸= g1 and P (c1) and P (c2) are disjoint, we see that |V (g) ∩ V (c1)| = 3. By 1.3 and
as u3 and u6 are 3-vertices in G[E(c1)], then V (g) ∩ V (c) = {u2, u3, u5} or V (g) ∩ V (c) =
{u5, u6, u7}. We see that g2 and c1 are disjoint (for otherwise c1 ∪ g1 ∪ g2 contains a
16-cycle). Hence, if t(c2) = (3, 6) the claim follows. If t(c2) = (3, 6, 5) then by 2.3 (2),
V (g3) ∩ V (c1) = {u2, u3, u4}. But then, by 2.2(1), g3 ∪ g2 ∪ f3 ∪ f4 contains a 16-cycle; a
contradiction. This contradiction concludes the proof.

By the deﬁnition of ℑall and Πf we have the following:

3.7. Let c1, c2 ∈ Πf be distinct and suppose V (c1) ∩ V (c2) ̸= ∅. Then, F (c2) ̸⊆ F (c1) and
there exists g ∈ F (c2) \ F (c1), |g| ∈ {3, 5, 6, 9}, so that V (c1) ∩ V (g) ̸= ∅.

the electronic journal of combinatorics 20(2) (2013), #P7 14

The rest of this section is devoted to studying intersections of clusters in Πf .

3.8. Under Hypothesis A, let c1, c2 ∈ Πf be distinct, and suppose t(c1) ∈ ℑ5
C. Then c1
and c2 are disjoint.

Proof. We shall assume that t(c1) = (665
66), as the proof when t(c1) = (666
566) is resolved
using similar arguments.
Assume for a contradiction that t(c1) = (665
66) but V (c1) ∩ V (c2) ̸= ∅. Let F (c1) =
{f1, . . . , f5} such that Chain(c1) = {f1, f2, f3}, |f1| = |f3| = |f4| = |f5| = 6 and |f2| = 5.
Let g ∈ F (c2) as exists by 3.7. We may assume that |g| ∈ {5, 6}, for by 1.3 and 2.2(1),
|g| ̸= 9 and |g| ̸= 3. Let f ′ ∈ {f1, f3, f4, f5} so that g and f ′ are adjacent.
Suppose |g| = 5. Observe that g must be disjoint from at least one 6-face f ′′ ∈
{f1, f3, f4, f5} \ f ′. But then g ∪ f ′ ∪ f2 ∪ f ′′ contains a 16-cycle; a contradiction.
Suppose |g| = 6. Since t(c2) ∈ ℑall, by inspection of ℑall, there exists g1 ∈ F (c2), so
that |g1| ∈ {3, 5}, and g and g1 are adjacent. Clearly g1 ̸= f2, and we may further assume
that g1 is disjoint from c2, for otherwise, a contradiction is obtained as in the previous
case above with g1 playing the rule of g. If |g1| = 5 then g ∪ g1 ∪ f ′ ∪ f2 contains a 16-cycle.
If |g1| = 3, then it is straightforward to verify that c2 ∪ g ∪ g1 contains a 16-cycle. Hence,
both cases lead to a contradiction.

3.9. Under Hypothesis A, let c1, c2 ∈ Πf be distinct and suppose t(c1) = (6
9
36). Then c1
and c2 are disjoint, unless t(c2) = (3) and then P (c1) and P (c2) are disjoint.

Proof. Let F (c2) = {f1, . . . , f4} such that |f1| = |f2| = 6, |f3| = 3 and |f4| = 9. If
t(c2) = (3), then the claim follows by 2.3(3), and the fact that by the deﬁnition of Πf ,
F (c2) ̸⊆ F (c1).
Hence, we may assume that t(c2) ̸= (3). Now assume for a contradiction V (c1) ∩
V (c2) ̸= ∅. Let g ∈ F (c2) as exists by 3.7. By 2.11, |g| = 3. By 2.3(3), V (g) ∩ V (c1) =
V (g) ∩ V (f4). As t(c2) ̸= (3), there exists g1 ∈ F (c2), |g1| ∈ {5, 6}, such that g1 and g are
adjacent. As g ̸∈ F (c1), then by 2.3(3), g1 ̸∈ F (c1). As g is a 3-face, then g1 and f4 are
adjacent. But then V (c1) ∩ V (g1) ̸= ∅; contradicting 2.11.

3.10. Under Hypothesis A, let c1, c2 ∈ Πf be distinct, and suppose that t(c1) = (3, 5
3).
Then, c1 and c2 are disjoint.

Proof. Suppose not. Let g ∈ F (c2) as exists by 3.7. By 2.3(1,5,6), |g| = 9. By 1.3, there
is a cluster of f , c′ := g ∪ c1 ∈ {(9, 3, 5
3), (3, 5
3, 9)}, so that t(c1) ∈ ℑall and F (c1) ⊆ F (c′);
contradicting the deﬁnition of Πf .

3.11. Under Hypothesis A, let c1, c2 ∈ Πf be distinct and suppose t(c1) ∈ ℑ
9. Then c1
and c2 are disjoint, unless one of the following holds:

• t(c1) = (5, 9, 3, 5
3); and then P (c1) and P (c2) are disjoint, and if c′ is the sub-cluster
of c of type (9, 3, 5
3), then c1 and c2 are disjoint.

• t(c2) = (5); and then P (c1) and P (c2) are disjoint.

Proof. Assume for a contradiction V (c1) ∩ V (c2) ̸= ∅. By 3.8, 3.9, and 3.10, t(c2) ̸∈
ℑ3
C ∪ ℑ5
C ∪ ℑ6∗
C .

Case 1. Suppose

t(c1) ∈ T1 := {(9, 3, 5, 3), (3, 9, 3, 5, 3), (3, 9, 5
3, 3), (9, 3, 5
3), (3, 9, 3, 5
3),

the electronic journal of combinatorics 20(2) (2013), #P7 15

(5
3, 3, 9, 3, 5
3), (5
3, 3, 9, 5, 9, 3, 5
3)}

By 2.2(1), 2.3 and the deﬁnition of Πf , it can be easily veriﬁed that

(1.i) c1 is disjoint from f ′, for any f ′ ∈ F (G) \ F (c1), with |f ′| ∈ {5, 6, 9}.

By (1.i), t(c2) ̸= (5). Let g ∈ F (c2) as exists by 3.7. By (1.i), |g| = 3. If t(c2) = (3),
then F (c2) = {g} and g is adjacent to f . Hence, by 1.3, g and F (c) are consecutive on
f . By 2.3(1), we deduce that t(c1) ∈ {(9, 3, 5, 3), (9, 3, 5
3)}. But then by 3.1 and 2.3(1),
c′ := g ∪ c1 is a cluster of f , F (c1) ⊆ F (c′), and t(c′) ∈ {(3, 9, 3, 5, 3), (3, 9, 3, 5
3)} ⊆ ℑall;
contradicting the deﬁnition of Πf . If t(c2) ̸= (3), then |F (c2)| ⩾ 2. By inspection of ℑall,
there is g1 ∈ F (c2) such that g1 ∈ {5, 6}, g and g1 are adjacent and g1 and f are adjacent.
We see that g1 ̸∈ F (c1); for otherwise |g1| = 5 and by 2.3(1), it must be that g ∈ F (c1),
contradicting the deﬁnition of g. Hence, g1 ̸∈ F (c1). But g being a 3-face intersecting
both c1 and g1 implies that V (g1) ∩ V (c1) ̸= ∅; contradicting (1.i).

Case 2. Suppose that: t(c1) ∈ T2 := {(5, 3, 9, 3, 5), (5, 3, 9, 3, 5
3)}.
As in Case (1), we ﬁrst see that

(2.i) c1 is disjoint from f ′, for any f ′ ∈ F (G) \ F (c1), with |f ′| ∈ {5, 6}.

By (2.i), t(c2) ̸= (5). We may assume that t(c2) ̸∈ T1 (for otherwise the proof proceeds
as in Case (1), with c2 playing the rule of c1).
Let g ∈ F (c2) as exists by 3.7. By (2.i), |g| = 3 or |g| = 9. If |g| = 3, the proof follows
by the same arguments as in Case (1). Hence, assume that |g| = 9. By 2.3(5), we see
that g and F (c) must be consecutive on f . Hence, there is f1 ∈ F (c1), with |f1| = 5,
so that g and f1 are consecutive on f . By the deﬁnition of Πf , and 2.3(0), we deduce
that f1 is adjacent to exactly one 3-face of G (which is in F (c1)). g ∈ F (c2) being a
9-face consecutive on f with the 5-face f1 and the assumption that t(c2) ̸∈ T1, imply that
t(c2) ∈ {(5, 9, 3, 5
3), (9, 3, 5
3), (9, 3, 6)}. Let f2 ∈ F (c1) such that |f2| = 3 and f1 and f2
are consecutive on f . Note that it is possible that f1 ∈ F (c2). Still we easily see that
c1 ∪ f1 ∪ f2 ⊆ G contains a 16-cycle, a contradiction.

Case 3. Suppose t(c1) = (9, 3, 5
3). As in Case (1), we ﬁrst see that

(3.i) c1 is disjoint from f ′, for any f ′ ∈ F (G) \ F (c1) with |f ′| ∈ {6, 9}.

Let F (c1) = {f1, . . . , f4} such that |f1| = 9, |f2| = |f4| = 3 and |f3| = 5, and
Chain(c1) = {f1, f2, f3}. Let g ∈ F (c2) as exists by 3.7. By (i), |g| = 5 or |g| = 3.

Case 3.1 Suppose |g| = 5. If t(c2) = (5) but V (P (c1)) ∩ V (P (c2)) ̸= ∅, then by 2.3(2),
c′ := g ∪ c1 is a cluster of f , F (c1) ⊆ F (c′) and t(c′) = (5, 9, 3, 5
3) ∈ ℑall, contradicting the
deﬁnition of Πf . Suppose then that t(c2) ̸= (5). We may assume that t(c2) ̸= (5, 9, 3, 5
3),
for otherwise it can be veriﬁed that c′ := c1 ∪ c2 a cluster of f , F (c1) ⊆ F (c′) and t(c′) ∈
{(5, 9, 3, 5
3), (5
3, 3, 9, 5, 9, 3, 5
3)} ⊆ ℑall, contradicting the deﬁnition of Πf . Hence, by
inspection of ℑall, there is g1 ∈ F (c2) so that g and g1 are adjacent, g1 and f are adjacent,
and g1 ∈ {3, 6}. If |g1| = 6, then by (3.i), g1 and c1 are disjoint; but since g is a 5-face,
then by 2.3(4), V (g) ∩ V (c1) = V (g) ∩ V (f1), and the faces g, f1 and f3 contradict 2.2(1).
If |g1| = 3, then by 2.3 and 2.2(1), g1 and f1 are adjacent, and then also consecutive. But
then c′ := c1 ∪ g1 a cluster of f , F (c1) ⊆ F (c′) and t(c′) = (3, 9, 3, 5
3) ∈ ℑall, contradicting
the deﬁnition of Πf .

the electronic journal of combinatorics 20(2) (2013), #P7 16

Case 3.2 Suppose |g| = 3. By the same arguments as in previous cases, we may
assume that g is not adjacent to f , and that g is not adjacent to a 6-face.
We conclude that t(c2) ∈ ℑ
9
C. By Cases (1,2) and the deﬁnition of ℑ
9
C, it follows that
t(c2) = (9, 3, 5
3). Then, it is easily seen that c′ := c1 ∪ c2 is a cluster of f , F (c1) ⊆ F (c′)
and t(c′) = (5
3, 3, 9, 3, 5
3) ∈ ℑall contradicting the deﬁnition of Πf .

Case 4. Suppose t(c1) ∈ {(3, 9, 3, 5), (9, 3, 6), (3, 9, 3, 6)}. The proof in this case
follows by similar arguments as in Cases (1,3).

Case 5. Suppose t(c1) = (5, 9, 3, 5
3) and that V (c2) ∩ V (c′) ̸= ∅, or that V (P (c1)) ∩
V (P (c2)) ̸= ∅. Let F (c1) = {f1, . . . , f5} such that |f1| = |f4| = 5, |f2| = 9 and |f3| =
|f5| = 3 and Chain(c1) = {f1, f2, f3, f4}.
If V (c2) ∩ V (c′) ̸= ∅, then let g ∈ F (c2) \ F (c1), so that V (g) ∩ V (c1) ̸= ∅. But
then it is easily seen that c1 ∪ g contains a 16-cycle. Hence, V (c2) ∩ V (c′) = ∅. If
V (P (c1)) ∩ V (P (c2)) ̸= ∅, then there is (as in Case (2)) g ∈ F (c2) \ F (c1), so that g and
f1 are consecutive on f . But then it is only possible that |g| = 9, for otherwise we can
ﬁnd a 16-cycle in c1 ∪ g ⊆ G. Now since c2 contains a 9-face, by 3.9 and Cases (1,4),
t(c2) = (5, 9, 3, 5
3). But then we deduce that c := c1 ∪ c2 is a cluster of f of type
(5
3, 3, 9, 5, 9, 3, 5
3) containing c1, contradicting the deﬁnition of Πf .

The following is veriﬁed by inspection.

3.12. If c1, c2 ∈ Πf are distinct and t(c1), t(c2) ∈ ℑS ∪ ℑ6
C, then Chain(c1) ̸= Chain(c2).

3.13. Under Hypothesis A, let c1, c2 ∈ Πf be distinct and suppose that t(c1) ∈ ℑ
6
C.

(i) Suppose that t(c1) = (6
6
36). Then, Chain(c1) and c2 are disjoint.

(ii) If t(c1) ∈ ℑ
6
C \ {(6
6
36)}, then c1 and c2 are disjoint.

Proof. (i) It suﬃces to show that P (c1) and P (c2) are disjoint (the proof then follows by
the same arguments as presented in the proofs of 2.10 and 2.9).
We may assume that t(c2) ̸∈ (ℑ3
C ∪ ℑ9 ∪ ℑ5
C ∪ ℑ6∗
C ), for otherwise the claim follows
by 3.11, 3.8, 3.9, and 3.10.
Now, assume for a contradiction that V (P (c1)) ∩ V (P (c2)) ̸= ∅. By 3.12, Chain(c1) ̸=
Chain(c2). Hence that there is g ∈ Chain(c2) such that g ̸∈ F (c1) and V (g)∩V (P (c1)) ̸= ∅.
By inspection of t(c2), we see that |g| ∈ {3, 5, 6}. By 2.3(0), we may also assume that g
and Chain(c1) are consecutive of f .
By symmetry we may assume that E(g) ∩ E(f ) = {xkx1} (the case in which E(g) ∩
E(f ) = {xℓ+1xℓ+2} is symmetric due to the symmetry of c1). Let F (c1) = {f1, . . . , f4}
such that Chain(c1) = {f1, f2}, and |f3| = 3. By 2.3 (3), |g| ̸= 3.
We may assume that |g| ̸= 5, for otherwise by 2.5, c′ = g ∪ c1 is a cluster of f of type

(5, 6
6
36) such that F (c1) ⊆ F (c′), contradicting the deﬁnition of Πf .
Hence |g| = 6. As t(c2) ∈ ℑall \ (ℑ
3
C ∪ ℑ9 ∪ ℑ5
C ∪ ℑ6∗
C ), by inspection of ℑall, there is a
3-face, g1 ∈ F (c2), such that g and g1 are adjacent.
If g1 is adjacent to f , then E(f )∩E(g1) = {xk−1xk}. By 2.5 and 2.3(3), c′ = g ∪g1 ∪c1,

is a cluster of f of type (3, 6, 6
6
36) with F (c1) ⊆ F (c′), contradicting the deﬁnition of Πf .
If g1 is not adjacent to f , then as g ̸∈ F (c1), g1 ̸= f3. By inspection of t(c2), we see
that t(c2) ∈ ℑ
6
C, and thus there is a 6-face, g2 ∈ F (c2), such that g, g1 and g2 are pairwise

the electronic journal of combinatorics 20(2) (2013), #P7 17

adjacent and g2 is adjacent to f . As g1 ̸= f3, then by 2.3 (3), g2 ̸= f1. But then, using 2.5
and 1.3, we can easily verify that f1 ∪ f2 ∪ f3 ∪ g ∪ g1 ∪ g2 ⊆ contains a 4-, 8- or 16-cycle;
a contradiction.

(ii) Suppose that t(c1) ∈ ℑ
6
C \{(6
6
36)}, and assume for a contradiction that V (c1)∩V (c2) ̸=

∅. We assume that t(c1) = {(6
6
36, 5)}, for if t(c1) ∈ {(6
6
36, 5, 3), (6
6
36, 6, 3)} then proof
follows by similar arguments. Let {f1, . . . , f5} = F (c1) such that Chain(c1) = {f1, f2, f3},
|f1| = |f2| = |f5| = 6, |f3| = 5 and |f4| = 3. Let g be as exists by 3.7. By 2.9(i) and 2.8,
|g| ̸∈ {5, 6, 9}. Hence |g| = 3. By 2.3(4), V (g) ∩ V (c1) ⊆ V (f3) \ V (f2). Now, if g is

adjacent to f , then c′ = g ∪ c1 is a cluster of f of type (6
6
36, 5, 3), and F (c1) ⊆ F (c′),
contradicting the deﬁnition of Πf . If g is not adjacent to f , we see that t(c2) ∈ ℑ
9
C ∪ ℑ3
C,
contradicting the deﬁnition of c2.

We can now turn to the proof of 3.4.

Proof of 3.4. (1) For suppose not. By 3.8, 3.9, 3.10, 3.11 and 3.13, t(c1), t(c2) ̸∈ ℑ
3
C ∪
ℑ9
C ∪ ℑ6
C ∪ ℑ5
C ∪ ℑ6∗
C . Hence,

t(c1), t(c2) ∈ ℑS \ {(3, 9, 3, 5), (5, 3, 9, 3, 5), (9, 3, 5, 3), (3, 9, 3, 5, 3), (9, 3, 6), (3, 9, 6, 3)}.

Let F (c1) = {f1, . . . , fℓ}, and assume, without loss of generality, that E(f ) ∩ E(fi) =
{xixi+1}, for 1 ⩽ i ⩽ ℓ. By symmetry, assume that if c1 is of type (a1, a2, . . . , aℓ), then
|fi| = ai, 1 ⩽ i ⩽ ℓ.
As c1 and c2 are distinct, then by 3.12, Chain(c1) ̸= Chain(c2). Hence, there is g ∈
Chain(c2) such that g ̸∈ F (c1) and V (g) ∩ V (P (c1)) ̸= ∅. In particular, g and the faces of
F (c1) are consecutive of f (and then E(g) ∩ E(f ) = {xℓ+1xℓ+2} or E(g) ∩ E(f ) = {xkx1}).
By inspection of t(c2), |g| ∈ {3, 5, 6}.

Case 1. Suppose that t(c1) ∈ {(3, 6, 6, 3, 6, 6, 3), (3, 6, 5, 6, 3), (3, 6, 6, 3)}. By the
symmetry of c1 we may assume that E(g) ∩ E(f ) = {xkx1}. By 2.3 (1) and (2), |g| /∈
{3, 5}. Hence, |g| = 6. If t(c1) = (3, 6, 6, 3, 6, 6, 3), then g, f1, . . . , f5 are consecutive
on f , of lengths, 6, 3, 6, 6, 3, 6, respectively. If t(c1) = (3, 6, 5, 6, 3), then g, f1, . . . , f4 are
consecutive on f , of lengths, 6, 3, 6, 5, 6, respectively. Both cases contradict 3.3.
If t(c1) = (3, 6, 6, 3), then by 3.2(2) and 3.1, c′ = g ∪ f1∪, . . . , ∪f4, is a cluster of f of
type (6, 3, 6, 6, 3),with F (c1) ⊆ F (c′); contradicting the deﬁnition of Πf .

Case 2. Suppose that t(c1) = (6, 3, 6, 6, 3). If E(g) ∩ E(f ) = {xℓ+1xℓ+2}, then by 2.3
(1) and (2), |f | ̸∈ {3, 5}, and by 3.3, |g| ̸= 6. Hence E(g) ∩ E(f ) = {xkx1}. By 2.3 (3),
|g| ̸= 3, and by 3.3, |g| ̸= 5. Hence, |g| = 6. By the deﬁnition of c2, there is g1 ∈ F (c2) such
that g, g1 and f are pairwise adjacent. Clearly, g1 ̸= f2. Thus E(f ) ∩ E(g1) = {xk−1xk},
and g1, g, f1, . . . , fℓ are consecutive on f , of lengths 3, 6, 6, 3, 6, 6, 3, respectively. By 3.2,
the union of this faces is a cluster, c′, of f of type (3, 6, 6, 3, 6, 6, 3), with F (c1) ⊆ F (c′);
contradicting the deﬁnition of Πf .

Case 3. Suppose t(c1) = (6, 3, 6, 5, 3). By 2.3 (1), (2), (4), and as |g| ∈ {3, 5, 6}, we
see that E(g) ∩ E(f ) ̸= {xℓ+1xℓ+2}. Hence, E(g) ∩ E(f ) = {xkx1}. By 2.3 (3), |g| ̸= 3. If
|g| = 5 (|g| = 6), then g, f1, . . . , f4 are consecutive on f of lengths 5, 6, 3, 6, 5 (6, 6, 3, 6, 5),
respectively; contradicting 3.3.

the electronic journal of combinatorics 20(2) (2013), #P7 18

Case 4. If t(c1) ∈ {(3), (5), (3, 5), (3, 5, 3), (3, 6), (3, 6, 5), (6, 3, 6), (3, 5, 6, 3),
(6, 3, 6, 5)}, the proof follows by the same arguments as in Cases (1)–(3). This proves (1).

(2,3) First note that by deﬁnition (5) , (6
6
36), (6
9
36) ̸∈ ℑP , ℑF . Hence, if V (c1) ∩ V (c2) ̸= ∅,
then by 3.8, 3.10, 3.11 and 3.13, we see that:

t(c1), t(c2) ∈ ℑ := ℑS \ {(5), (3, 9, 3, 5), (5, 3, 9, 3, 5), (9, 3, 5, 3),

(3, 9, 3, 5, 3), (9, 3, 6), (3, 9, 6, 3)}

(2) Suppose not. Let g1 ∈ F (c1) and g2 ∈ F (c2) such that V (g1) ∩ V (g2) ̸= ∅. By
inspection of t(c1) and t(c2), there are sub-clusters c′
2 of c2 and c′
1 of c1 (possibly c′
1 = c1
or c′
2 = c2) such that g1 ∈ F (c′
1), g2 ∈ F (c′
2), and t(c′
1), t(c′
2) ∈ {(3, 5), (3, 6), (3, 6, 5)}. By
deﬁnition of g1 and g2, V (c′
1) ∩ V (c′
2) ̸= ∅; a contradiction to 3.5.

(3) Suppose not. Then (by the remark above) t(c1), t(c2) ∈ ℑ ∩ ℑP . Let g ∈ F (c2) such
that g ̸∈ F (c1) and V (g) ∩ V (c1) ̸= ∅ (g exists by deﬁnition of Πf ). As t(c1), t(c2) ∈ ℑS,
|g| ∈ {3, 5, 6}. By the deﬁnition of ℑS, every face in F (c1) or F (c2) is adjacent to f .
Recall that by 3.4(1), P (c1) ∩ P (c2) = ∅. This implies that F (c1) ∩ F (c2) = ∅ and that
|g| ̸= 3 (and then t(c2) ̸= (3)). We may also assume that c1 ̸= (3).

Case 1. Suppose t(c1) ∈ {(3, 5), (3, 5, 3)}. By 2.3(2), |g| ̸= 5, hence |g| = 6. By
inspection of t(c2), there is a sub-cluster c′
2 of c2 such that g ∈ F (c′
2) and t(c′
2) = (3, 6). As
V (g)∩V (c1) ̸= ∅, there is a sub-cluster c′
1 of c1 such that t(c′
1) = (3, 5) and V (g)∩V (c′
1) ̸=
∅. But then V (c′
1) ∩ V (c′
2) ̸= ∅ and P (c′
1) and P (c′
2) are disjoint (as P (c1) and P (c2) are
disjoint); contradicting 3.5(1).

Case 2. Suppose t(c1) ∈ {(3, 6, 5, 6, 3), (3, 6, 5, 3)}. By inspection of t(c2), there is a
sub-cluster c′
2 of c2 such that g ∈ F (c′
2) and t(c′
2) ∈ {(3, 5), (3, 6)}. Hence, V (c1) ∩ V (c′
2) ̸=
∅ and V (P (c1)) ∩ V (P (c′
2)) = ∅; contradicting 3.6(3).

Case 3. Suppose t(c1) ∈ {(6, 3, 6, 5), (6, 3, 6, 5, 3)}. By Cases (1,2):

t(c2) ∈ {(6, 3, 6), (6, 3, 6, 5), (3, 6, 6, 3), (6, 3, 6, 5, 3), (6, 3, 6, 6, 3) , (3, 6, 6, 3, 6, 6, 3)}

By inspection of t(c2), there is a sub-cluster of c′
2 of c2 such that g ∈ F (c′
2) and if
|g| = 6 (|g| = 5), then t(c′
2) = (3, 6) (t(c′
2) = (3, 6, 5)). As V (g) ∩ V (c1) ̸= ∅, there
is a sub-cluster of c1, c′
1 such that t(c′
1) = (6, 3, 6, 5), and V (g) ∩ V (c′
1) ̸= ∅. Hence,
V (c′
1) ∩ V (c′
2) ̸= ∅ and V (P (c′
1)) ∩ V (P (c′
2)) = ∅, contradicting 3.6(1).

Case 4. Suppose t(c1) ∈ {(3, 6, 6, 3), (3, 6, 6, 3, 6, 6, 3)}. By Cases (1-3):

t(c2) = {(6, 3, 6), (3, 6, 6, 3) (6, 3, 6, 6, 3) , (3, 6, 6, 3, 6, 6, 3)}

By inspection of t(c2), there is a sub-cluster c′
2 of c2 such that g ∈ F (c′
2) and t(c′
2) ∈
{(6, 3, 6), (3, 6, 6, 3)}. As V (c1) ∩ V (g) ̸= ∅, then V (c1) ∩ V (c′
2) ̸= ∅, and V (P (c1)) ∩
V (P (c′
2)) = ∅; contradicting 3.6(2).

Case 5. Suppose t(c1) = (6, 3, 6, 6, 3). By Cases (1-4), t(c2) ∈ {(6, 3, 6), (6, 3, 6, 6, 3)}.
By inspection of t(c2), there is a sub-cluster of c′
2 of c2 such that g ∈ F (c′
2), and t(c′
2) ∈

the electronic journal of combinatorics 20(2) (2013), #P7 19

{(6, 3, 6), (3, 6, 6, 3)}. As V (g) ∩ V (c1) ̸= ∅, then V (c1) ∩ V (c′
2) ̸= ∅ and V (P (c1) ∩
V (P (c′
2) = ∅; contradicting 3.6(4).

(4) The proof follows from 3.13 and 3.9.

(5) The proof follows from 1.3 and 2.2(1).

We conclude this section with following lemma, which can be veriﬁed using 1.3 and 2.3(0).
The “pseudoclusters” (3,9) and (3,10) that appear in the lemma are deﬁned in a natural
way. (However, they do not belong to ℑall.)

3.14. Let c1, c2 be distinct clusters of f such that c2 ∈ Πf and F (c1) ̸⊆ F (c2)

1. Suppose t(c1) = (3, 9) and t(c2) ∈ {(3, 5
3), (3, 5, 6, 3), (6, 3, 6), (3, 9, 3, 5
3)}. Then c1
and c2 are disjoint.

2. Suppose t(c1) = (3, 10) and t(c2) = (6, 3, 6). Then c1 and c2 are disjoint.

4 Extending a Cycle

We start with some deﬁnitions. For a subgraph H ⊆ G, let ∆H ⊆ N∗ be the set of all
lengths of cycles of H, that is x ∈ ∆H if and only if H contains a cycle of length x.
(N
∗ is the set of non-negative integers.) For integers x and y, with x ⩽ y, let [x, y] =
{x, x + 1, . . . , y}.
Let c ∈ Πf , for some f ∈ F (G) and let S = c ∪ f . Using c, the face f can be extended
(inside S) into cycles of greater length than |f |. The fact that G contains no 2
m-cycles
(2 ⩽ m ⩽ 7) will allow us to characterize the set Πf . Intuitively, Πf will be “small”, for
otherwise as the clusters in Πf are essentially pairwise disjoint, we will be able to extend
f into a cycle of length 2m. Below a set ΩS ∈ N∗ is deﬁned so that |f | + ΩS ⊆ ∆S (that
is, for every ω ∈ ΩS, |f | + ω ∈ ∆S).

4.1. Under Hypothesis A, let c ∈ Πf and S = f ∪ c. Then,

1. If t(c) = (3), set ΩS := {0, 1}.

2. If t(c) = (5), set ΩS := {0, 3}.

3. If t(c) ∈ {(3, 5), (3, 5, 3)}, set ΩS := [0, 3].

4. If t(c) ∈ {(3, 6), (6, 3, 6)}, set ΩS := [0, 4] \ {2}.

5. If t(c) = {(3, 5
3)}, set ΩS := [0, 4].

6. If t(c) ∈ {(3, 5, 6, 3), (3, 6, 5)}, set ΩS := [0, 5] \ {2}.

7. If t(c) = (6, 3, 6, 5), set ΩS := [0, 6] \ {2}.

8. If t(c) = (3, 6, 6, 3), set ΩS := [0, 6].

9. If t(c) ∈ {(6
6
36), (6
6
36, 5), (6
9
36)}, set ΩS := {0, 6}.

10. If t(c) ∈ {(6, 3, 6, 5, 3), (3, 9, 3, 5), (5, 3, 9, 3, 5), (9, 3, 6), (3, 9, 3, 6), (5, 9, 3, 5
3)},

the electronic journal of combinatorics 20(2) (2013), #P7 20

11. set ΩS := [0, 7] \ {2, 5}.

12. If t(c) ∈ {(9, 3, 5, 3), (3, 9, 3, 5, 3), (9, 3, 5
3), (3, 9, 3, 5
3), (5, 3, 9, 3, 5
3), (3, 6, 5, 6, 3),

(6
6
36, 5, 3), (6, 3, 6, 6, 3), (9, 5
3, 3)}

set ΩS := [0, 8] \ {5}.

13. If t(c) ∈ {(3, 9, 5
3, 3), (53, 3, 9, 3, 5
3), (6
6
36, 6, 3)}, set ΩS := [0, 9] \ {2}.

14. If t(c) = (3, 6, 6, 3, 6, 6, 3), set ΩS := [0, 10].

15. If t(c) = (53, 3, 9, 5, 9, 3, 5
3), set ΩS := [0, 14].

16. If t(c) ∈ {(6
66
566), (6
65
66)}, set ΩS := {0}.

The reader may verify by inspection using Figures 2 and 3, that in 4.1, ΩS is indeed
always a subset of ∆S.
Let f , c, and S be as in 4.1. We say that c extends f by at most max(ΩS). The value
max(ΩS) is called the maximal extension value of c with respect to f . As this value is
determined in 4.1 solely by the type of c, then for X ∈ ℑall, let

MX be the maximal extension value of a cluster of type X (1)

The following lemma is straightforward, and can be proved by a simple inductive
argument.

4.2. Let x1, . . . , xn ∈ N
∗ such that 1 ⩽ xi ⩽ 14 and xi ̸= 2 (i = 1, . . . , n). Let y1, . . . , ym ∈
N
∗ such that 4 ⩽ yi ⩽ 14 (i = 1, . . . , m). For i = 1, . . . , n, let Xi = {0, 1, 2, . . . , xi}. For
i = 1, . . . , m, deﬁne Yi as follows:

• If 4 ⩽ yi ⩽ 5, set Yi = {0, 1, 2, . . . , yi} \ {2}.

• If 6 ⩽ yi ⩽ 14, set Yi = {0, 1, 2, . . . , yi} \ {2, 5}.

Let A = {a1, . . . , an} ⊆ N
∗ and B = {b1, . . . , bm} ⊆ N
∗. Let P (A) =
 n∑

i=1 ai and P (B) =

m∑

i=1 bi. Let r =
 n∑

i=1 (ai · xi) +
 m∑

j=1 (bj · yj) and R = {0, 1, 2, . . . , r}. If P (A) + P (B) ⩾ 2,

then each d ∈ R can be expressed as follows,

d =
 n∑

i=1
 ai∑

j=1 ˆxi,j +
 m∑

i=1
 bi∑

j=1 ˆyi,j, where ˆxi,j ∈ Xi, ˆyi,j ∈ Yj.

4.3. Under Hypothesis A, let ℑ ⊆ ℑF , and let C be a set of clusters of f such that the
following conditions holds:

1. |C| ⩾ 2.

2. for every c ∈ C, t(c) ∈ ℑ.

the electronic journal of combinatorics 20(2) (2013), #P7 21

3. If c1, c2 ∈ C are distinct, then c1 and c2 are disjoint, unless t(c1), t(c2) = (6, 3, 6)
or t(ci) = (5, 9, 3, 5
3) (1 ⩽ i ⩽ 2). In the latter case c3−i is disjoint from c′
i, where
c′
i ⊆ ci is the sub-cluster of ci of type (9, 3, 5
3).

For every X ∈ ℑ, let SX = {c ∈ C : t(c) = X}. Let L = ∑

X∈ℑ |SX| · MX, and

G
∗ = f ∪ ( ⋃

c∈C c). Then {|f |, |f | + 1, . . . , |f | + L} ⊆ ∆G∗.

Proof. Let S(6,3,6) = {c1, . . . , cm} ⊆ C and S(5,9,3,53) = {d1, . . . , dℓ} ⊆ C (where m, ℓ ⩾ 0).
By 3.4, ci (i = 1, . . . , m) contains a sub-cluster ˆci of type (3, 6) such that for distinct
1 ⩽ j, r ⩽ m, ˆcj and ˆcr are disjoint. By assumption, ˆci is disjoint from c, for every
c ∈ C \ S(6,3,6). By assumption again, di (i = 1, . . . , ℓ) contains a sub-cluster ˆdi of type
(9, 3, 5
3) such that ˆdi is disjoint from c, for every c ∈ C \ di. We conclude that the clusters
in the set C ′ = (C \ (S6,3,6 ∪ S(5,9,3,53))) ∪ ⋃m
i=1 ˆci ∪ ⋃ℓ
i=1 ˆdi are pairwise disjoint, and for
each c ∈ C ′, t(c) ∈ ℑF \ (6, 3, 6).
Let S′
X = {c ∈ C ′ : t(c) = X} and let L
′ = ∑

X∈ℑ |S′
X| · MX. By 4.1, M(3,6) = M(6,3,6)

and M(5,9,3,53) = M(9,3,53). Hence L′ = L.
For c ∈ C ′, set xc = t(c) ∈ ℑF and Hc := f ∪ c. As ℑ ⊆ ℑF , by 4.1, 1 ⩽ MX ⩽ 14,
and the following holds:

1. If 4 ⩽ MX ⩽ 5, then {0, 1, . . . , MX} \ {2} ⊆ ΩHc.

2. If 6 ⩽ MX ⩽ 14, then {0, 1, . . . , MX} \ {2, 5} ⊆ ΩHc.

The proof follows from 4.2 and the disjointness of the clusters in C ′.

Deﬁne a function α : N → N as follows:

α(x) = 2
⌊log2 x⌋+1 (2)

We then have the following straightforward observation.

4.4. In the settings of 4.3, G
∗ contains no 2
m-cycles if and only if L < α(|f |) − |f |.

If c ∈ Πf and t(c) ∈ {(6
6
36), (6
6
36, 5), (6
9
36)}, then t(c) ̸∈ ℑF . Observe that c has a
maximal extension value of 6, however c does not extend f by 1, 2 or 3. This is why these
types of clusters are not excluded from the sets ℑF or ℑP . Using 3.4(3), the extension
values of these clusters are exploited in a diﬀerent way. The idea is to extend f in steps of
6 as much as possible, thus obtaining (instead of f ) a new cycle which is closer in length
to α(|f |) but not exceeding α(|f |).

For n ⩾ 1, and a set {a0, . . . , an} ⊆ N
∗, deﬁne a function β : (a0, . . . , an) → N as
follows. β(a0, . . . , an) = m, where

1. m ⩽
 n∑

i=1 ai

2. 6 · m ⩽ α(a0) − a0

3. subject to (1) and (2), m is maximum.

the electronic journal of combinatorics 20(2) (2013), #P7 22

The following corollary is obtained by applying 4.3, 4.4, and 3.4 to the sets Πf , ℑP and
ℑF .

4.5. Under Hypothesis A, let SX = {c ∈ Πf : t(c) = X} for every X ∈ ℑF , and let

G
∗ = f ∪
 

 ⋃

c∈Πf c


.

1. If |ℑP | ⩾ 2, then
∑

X∈ℑP |SX| · MX < α(|f |) − |f | − β(|f |, |S
(6
6
36)|, |S
(66
36,5)|, |S
(69
36)|)

2. If |ℑF | ⩾ 2 and k ∈ {17, 18}, then
∑

X∈ℑF |SX| · MX < α(|f |) − |f | − β(|f |, |S
(6
6
36)|, |S
(66
36,5)|, |S
(69
36)|)

5 Discharging and Integer Programs

In this section the main theorem is proved using the Discharging Method. The ﬁrst step in
the Discharging Method is to assign numerical values (known as charges) to the elements
of G. For v ∈ V (G), let ch(v) = 4 − deg(v) and for f ∈ F (G), let ch(f ) = 4 − |f |.
The following lemma is a simple consequence of Euler’s formula.

5.1. ∑

v∈V (G)
(4 − deg(v)) + ∑

f ∈F (G)(4 − |f |) = 8.

Our goal is prove that G does not exist. To this end, the charges will be locally
redistributed according to Rules(1-15) listed below. This is called discharging, as the
rules are designed to send charge away from those elements of positive initial charge. If x
is either a vertex or a face of a plane graph, let ch∗(x) (denoted as the modiﬁed charge) be
the resultant charge after modiﬁcation of the initial charges of the elements of the graph
according to Rules(1-15).

Rule(1). If f is an (⩾ 11, ⩾ 11, ⩾ 11)-face or (10, 10, ⩾ 10)-face, then f sends 1
3 to
each of the faces adjacent to it.

Rule(2). If f is a (10, ⩾ 11, ⩾ 11)-face, then f sends 1
5 to the 10-face adjacent to
it, and 2
5 to each ⩾ 11 face adjacent to it.

Rule(3).If f is a (9, ⩾ 11, ⩾ 11)-face, then f sends 1
2 to each ⩾ 11 face adjacent to
it.

Rule(4). Let f be a (5, ⩾ 10, ⩾ 10)-face. Let Γ(f ) = {f1, f2, f3} such that |f1| = 5.

(a) If f is the only 3-face adjacent to f1, then f sends 1
2 to each ⩾ 10 face adjacent
to it; otherwise

(b) f1 is adjacent to a 3-face g such that g ̸= f . If f2 and g are disjoint then f
sends 5
6 to f2, and 1
6 to f3. If f3 and g are disjoint then f sends 5
6 to f3, and 1
6
to f2.

the electronic journal of combinatorics 20(2) (2013), #P7 23

Rule(5). Let f be a (5, 9, ⩾ 11)-face. Let Γ(f ) = {f1, f2, f3} such that |f1| = 5 and
|f2| = 9. Then,

(a) f sends 1
6 to f2 and 5
6 to f3, unless

(b) there exists a 3-face g ̸= f such that g is adjacent to f1 and f2, and then f
sends 1 to f3.

Rule(6). Let f be (6, ⩾ 9, ⩾ 9)-face.

(a) If f is a (6, 9, ⩾ 11)-face, then f sends 1
6 to the adjacent 9-face, and 5
6 to the
adjacent ⩾ 11-face

(b) If f is a (6, ⩾ 10, ⩾ 10)-face, then f sends 1
2 to each adjacent ⩾ 10-face.

Rule(7). Let f be (6, 6, k)-face such that k ⩾ 9. Let Γ(f ) = {f1, f2, f3} such that
|f1| = k.

(a) If k ⩾ 10, then f sends 4
3 to f1.

(b) If k = 9, then let g be the face which is semi-adjacent to f such that v ∈ V (f ),
u ∈ V (g), and v is a (3, 6, 6)-vertex. Then, (i) f sends 2
3 to f1, and (ii) if
|g| ⩾ 7, then f sends 2
3 to g.

Rule(8). A (6, 6, 6)-face sends 1 to each ⩾ 9 semi-adjacent face.

Rule(9). A 5-face not adjacent to 3-faces but adjacent to at least two ⩾ 7-face,
sends 1
3 to each ⩾ 7-face face adjacent to it.

Rule(10). A (⩾ 10, 6, 6, 6, 6)-face sends 2
3 to the ⩾ 10 face adjacent to it.

Rule(11). A (6, 6, 6, 6, 6)-face sends 1
6 to each ⩾ 10 semi-adjacent face.

Rule(12) A (3, ⩾ 9, ⩾ 9)-vertex sends 1
2 to each incident ⩾ 9 face.

Rule(13) A (3, ⩾ 9, 6)-vertex sends 1
3 to the incident 6-face, and 2
3 to the incident
⩾ 9-face.

Rule(14). Let v be a (3, 5, ⩾ 9)-vertex. Then,

(a) v sends 1 to the incident ⩾ 9-face, unless

(b) the 5-face incident to v is adjacent to two 3-faces, and every neighbour of v is
incident to a 3-face. In this case v sends 2
3 to the incident 9-face and 1
3 to the
incident 5-face.

Rule(15). A vertex v not sending charge by Rules (12-14), sends 1
3 to each incident
face.

Remark 1. One note for clariﬁcation. Suppose f1, f2 ∈ F (G) are two semi-adjacent
faces, and let v ∈ V (f1) and u ∈ V (f2) such that vu ∈ E(G). If f1 sends charge to f2,
then the charge is sent via v and u, i.e., f1 sends the charge to v, v sends the charge to
u, and u sends the charge to f2. This enables us to assume that charge enters a face only
from the elements V (f ) ∪ E(f ).

the electronic journal of combinatorics 20(2) (2013), #P7 24

Now the proof of the main theorem may be given. For the graph G, it will be shown
that every vertex and every face has a non-positive modiﬁed charge. The sum of all the
modiﬁed charges is then non-positive, contradicting 5.1.

Consider a vertex v ∈ V (G). Then ch(v) = 1. By Rules(12-15), it is easily seen that
v sends a total charge of 1 to the faces incident to it. By our rules, if v receives charge,
then this is because v is a link between two semi-adjacent faces, and every charge that
enters v is sent out of v. Hence, ch∗(v) = 0.

5.2. If |f | ⩽ 7, then ch
∗(f ) ⩽ 0.

Proof. Suppose |f | = 3. Then ch(f ) = 1.
Let Γ(f ) = {f1, f2, f3}. We may assume that f is adjacent to a ⩽ 9-face, for otherwise
by Rules(1,2,12), it is easily seen that ch
∗(f ) = 0.

Case 1. Assume that f is adjacent to a 9-face, say f1. If |f2|, |f3| ⩾ 9, then by 2.2(1,2),
|f2|, |f3| ⩾ 11, and ch∗(f ) = 0 by Rule(3,12). Hence, by symmetry, assume that |f2| ⩽ 7.
By 2.2(1) and 2.3(0), 5 ⩽ |f2| ⩽ 6. If |f2| = 5, then by 2.2(1,2) and 2.3(0), |f3| ⩾ 11.
Thus f is a (5, 9, ⩾ 11)-face, and ch∗(f ) = 0 by Rule(5a,5b,14). If |f2| = 6, then as above,
|f3| ⩾ 11 or |f3| = 6. If |f3| ⩾ 11, then ch∗(f ) = 0 by Rule(6a,12,13). If |f3| = 6, then
by 2.11, |g| ⩾ 7 (where g is as in Rule(7b)). By Rule(15), f receives a charge of 1
3 from
the single (3, 6, 6)-vertex incident to it, and by Rule(7b), f sends 2
3 to each of f1 and g.
Hence, ch∗(f ) = 0.

Case 2. Suppose f is not adjacent to a 9-face, but adjacent to a ⩽ 7-face, say f1.
By 2.2(1), 5 ⩽ |f1| ⩽ 6. If |f1| = 5, then, by 2.2(1) and as f is not adjacent to a 9-face,
|f2|, |f3| ⩾ 10, and by Rule(4,12,14), ch∗(f ) = 0. Hence, |f1| = 6, and thus for i = 2, 3,
|fi| = 6 or |fi| ⩾ 10. If |f2| ̸= 6 or |f3| ̸= 6, then ch∗(f ) = 0 by Rules(6b,7a,12,13).
Otherwise, f is a (6, 6, 6)-face. By 2.7, f has at least two semi-adjacent, say g1 and g2
such that |g1|, |g2| ⩾ 9. We then see that ch∗(f ) = 0, as by Rule(15), f receives a charge
of 1
3 from each vertex incident to it, and by Rule(8), f sends 1 to each of g1 and g2.

Suppose |f | = 5. Then ch(f ) = −1. Let x1, . . . , x5 be the vertices of f in a cyclic
order. Let Γ(f ) = {f1, . . . , f5} and assume that E(f ) ∩ E(fi) = xixi+1 (where x0 := x5
and x6 := x1). By our rules, f receives no charge from semi-adjacent faces.

Case 1. Suppose that f is not adjacent to a 3-face. Then |fi| ⩾ 6, for i = 1, . . . , 5.
Let δ be the number of ⩾ 7 faces adjacent to f . If δ ⩾ 2, then then by Rules(9,15),
ch
∗(f ) ⩽ −1 + 5 · 1
3 − δ · 1
3 ⩽ 0. If δ = 1, say |f1| ⩾ 7, then by 2.14, |f1| ⩾ 10, and then
by Rules(10,15), ch
∗(f ) ⩽ −1 + 5 · 1
3 − 2
3 = 0. If δ = 0 (i.e., f is a (6, 6, 6, 6, 6)-face),
then by 2.15 each semi-adjacent face of f is of length ⩾ 10. Hence, by Rules(11,15),
ch
∗(f ) ⩽ −1 + 5 · 1
3 − 5 · 1
6 < 0.

Case 2. Suppose f is adjacent to exactly one 3-face. By symmetry, assume that
|f1| = 3. By 2.3, |f5|, |f2| ⩾ 9. Then ch
∗(f ) = 0, as by Rule(14a) vertices in V (f ) ∩ V (f1)
send no charge to f , and by Rule(15) every other vertex of V (f ) sends 1
3 to f .

Case 3. Suppose f is adjacent to two 3-face. By symmetry and 2.3(1), assume that
|f1| = |f3| = 3. By Rule(14a), x4 and x1 sends no charge to f . By Rule(14b) each of x2
and x3 sends 1
3 to f . By Rule(15), x5 sends 1
3 to f . Hence, ch∗(f ) = 0.

the electronic journal of combinatorics 20(2) (2013), #P7 25

Suppose |f | = 6. Then ch(f ) = −2. By our Rules, f only receives charge according to
Rules(13,15), and then ch
∗(f ) = −2 + 6 · 1
3 = 0.

Suppose |f | = 7. ch(f ) = −3. Let δ be the number of 5-faces adjacent to f . By 2.2(1)
and 2.3(2), δ ⩽ 2.

Case 1. Suppose f receives charge from a semi-adjacent face, say f ′. If this is the

case, then Rule(7b) was applied. By this rule, there is a cluster c of f of type (6
9
36) such
that |f ′| = 3 and f ′ ∈ F (c). By this rule, f ′ sends 2
3 to f . By 2.11 and 2.3(0), we see that
δ = 0 and f ′ is the sole semi-adjacent face sending charge to f . Hence, by Rules(7b,15),
ch
∗(f ) = −3 + 7 · 1
3 + 2
3 = 0.

Case 2. Suppose f receives no charge from a semi-adjacent face. If δ = 0, then f
only receives charge by Rule(15), and ch
∗(f ) = −3 + 7 · 1
3 < 0. If δ ⩾ 1, then let g be
a 5-face adjacent to f . We see that g sends to f a charge of at most 1
3. Indeed, if g is
adjacent to a 3-face, then by our rules g sends no charge to f . If g is not adjacent to a
3-face, then by 2.14, we conclude that g is adjacent to at least two ⩾ 7-faces, and then by
Rule(9), g sends 1
3 to f . As δ ⩽ 2, then by Rules(9,15), ch∗(f ) ⩽ −3 + 7 · 1
3 + 2 · 1
3 = 0.

Next we have to show that ch
∗(f ) ⩽ 0, for every f ∈ F (G) with |f | ⩾ 9. The proof in
this case requires some more elaborate arguments.

5.3. Under Hypothesis A,

1. Let g ∈ Γ(f ). If g sends charge to f , then there is c ∈ Πf with g ∈ F (c).

2. Let v ∈ V (f ). If v sends charge to f which is strictly larger than 1
3, then there is
c ∈ Πf with v ∈ V (P (c)).

3. Suppose c ∈ Πf and let v be an endpoint of P (c). Let g ∈ F (c) so that v ∈ V (g). If
|g| ⩾ 6, then v sends 1
3 to f .

Proof. (1) By Remark 1 and Rules(1-15), if g sends charge to f , then |g| ∈ {3, 5} and g
is adjacent to f . Thus, c := g is a cluster of f of type (|g|). By deﬁnition of Πf , there is
a cluster c′ of f so that c ⊆ c′ (possibly c = c′) and g ∈ Chain(c′), as required.
(2) By Rules(1-15), if v sends to f a charge which is strictly larger than 1
3, then there
is a face g ∈ F (G) so that that either |g| = 3, g and f are adjacent and v ∈ V (g) ∩ V (f )
or |g| ∈ {3, 5}, g and f are semi-adjacent, and the charge of g is sent to f via v. We
may assume that latter case holds, as the former follows as in (1). By Rules(7,8,11), g

is contained in a cluster of f of type (6
9
36), (6
6
36) or (6
66
566)) and the proof follows by
deﬁnition of Πf .
(3) Let g1 be the face incident to v, other than f and g. By 3.4 (1), g1 ̸∈ F (c′) for
every c′ ∈ Πf distinct from c. In particular, as {(3), (5)} ∈ ℑall, |g1| ⩾ 6. If there exists
g2 ∈ F (c) so that g2 is semi-adjacent to f and g2 sends charge to f via v, then v is not
an endpoint of P (c). Hence, v is a (⩾ 6, ⩾ 9, ⩾ 6)-vertex which is not a link between f
and a semi-adjacent of f which sends charge to f . Hence, Rule(15) is applied to v.

Let
 Vs = V (f ) \ ⋃

c∈Πf V (P (c)) (3)

the electronic journal of combinatorics 20(2) (2013), #P7 26

and
 Fs = Γ(f ) \ ⋃

c∈Πf F (c) (4)

For x ∈ V (f ) ∪ Γ(f ) denote by chf (x) the amount of charge that x sends to f by Rules
(1)-(15). Note that by Remark (1), f only receives charge from elements in V (f ) ∪ Γ(f ).
By Rule(15) and 5.3 we have
 chf (v) = 1
3, for v ∈ Vs (5)

and
 chf (g) = 0, for g ∈ Fs (6)

The amount of charge received by f from a cluster c ∈ Πf is then deﬁned as follows:

chf (c) := ∑

v∈V (P (c)) chf (v) + ∑

g∈Chain(c) chf (g) (7)

Let total(f ) denote the total amount of charge received by f from all elements V (f ) ∪
Γ(f ). By 3.4 (1) we have
 total(f ) = ∑

c∈Πf chf (c) + 1
3 · |Vs| (8)

and we conclude that

ch
∗(f ) = 4 − |f | + total(f ) = 4 − |f | + ∑

c∈Πf chf (c) + 1
3 · |Vs| (9)

Observe that for any c ∈ Πf , chf (c) is determined solely by the type of c. Now, if
we equally spread the total amount of charge that c sends to f among the vertices of
V (P (c)), then if v ∈ V (P (c)) we may assume that v sends f a charge of

frf (c) := chf (c)
|P (c)| . (10)

Next we provide upper and lower bounds for chf (c), where |f | ⩾ 9. The following is a
direct consequence of Rule(1,15), 5.3 and the structural properties obtained in Section (2).

5.4. Under Hypothesis A, let c ∈ Πf .

1. Suppose t(c) = (3). Let F (c) = {f1}.

(a) If |f | = 9 then chf (c) = 1 and frf (c) = 1
2.

(b) Suppose |f | ⩾ 11.

i. If f1 is adjacent to a 9-face, then chf (c) = 3
2 and frf (c) = 3
4.
ii. If f1 is adjacent to exactly one 10-face, then chf (c) = 7
5 and frf (c) = 7
10.
iii. If f1 is adjacent to two 10-faces, then chf (c) = 4
3 and frf (c) = 2
3.

(c) If |f | = 10, then chf (c) = 6
5 and frf (c) = 3
5, unless f1 is adjacent to at least
two 10-faces, and then chf (c) = 4
3 and frf (c) = 2
3.

the electronic journal of combinatorics 20(2) (2013), #P7 27

2. If t(c) = (5), then chf (c) = 1 and frf (c) = 1
2.

3. Suppose t(c) = (3, 5). Let Fc = {f1, f2} such that |f1| = 3 and |f2| = 5.

(a) If |f | = 9, then chf (c) = 2 and frf (c) = 2
3.

(b) If |f | ⩾ 10, then chf (c) = 7
3 and frf (c) = 7
9, unless f1 is adjacent to a 9-face,
and then chf (c) = 8
3 and frf (c) = 8
9.

4. Suppose t(c) = (3, 5, 3).

(a) If |f | = 9, then chf (c) = 7
3 and frf (c) = 7
12.

(b) If |f | ⩾ 10, then chf (c) = 8
3 and frf (c) = 2
3.

5. Suppose t(c) = (3, 5
3).

(a) If |f | = 9, then chf (c) = 2 and frf (c) = 2
3.

(b) If |f | ⩾ 10, then chf (c) = 8
3 and frf (c) = 8
9.

6. Suppose t(c) = (3, 6).

(a) If |f | = 9 then chf (c) = 5
3 and frf (c) = 5
9.

(b) If |f | ⩾ 10, then chf (c) = 2 and frf (c) = 2
3.

7. Suppose t(c) = (3, 6, 5).

(a) If |f | = 9, then chf (c) = 7
3 and frf (c) = 7
12.

(b) If |f | ⩾ 10, then chf (c) = 8
3 and frf (c) = 2
3.

8. Suppose t(c) = (6, 3, 6).

(a) If |f | = 9, then chf (c) = 8
3 and frf (c) = 2
3.

(b) If |f | ⩾ 10, then chf (c) = 10
3 and frf (c) = 5
6.

9. If t(c) = (6, 3, 6, 5), then chf (c) = 4 and frf (c) = 4
5.

10. Suppose t(c) = (3, 5, 6, 3).

(a) If |f | = 9, then chf (c) = 10
3 and frf (c) = 2
3.

(b) If |f | ⩾ 10, then chf (c) = 4 and frf (c) = 4
5.

11. If t(c) = (6, 3, 6, 6, 3), then chf (c) = 5 and frf (c) = 5
6.

12. If t(c) = (3, 6, 6, 3, 6, 6, 3), then chf (c) = 20
3 and frf (c) = 5
6.

13. Suppose t(c) = (3, 6, 6, 3).

(a) If |f | = 9, then chf (c) = 3 and frf (c) = 3
5.

(b) If |f | ⩾ 10, then chf (c) = 11
3 and frf (c) = 11
15.

14. If t(c) = (6, 3, 6, 5, 3), then chf (c) = 16
3 and frf (c) = 8
9.

15. If c = (6
6
36), then chf (c) = 2 and frf (c) = 2
3.

the electronic journal of combinatorics 20(2) (2013), #P7 28

16. If t(c) = (6
9
36), then chf (c) = 5
3 and frf (c) = 5
9.

17. If t(c) = (6
6
36, 5), then chf (c) = 8
3 and frf (c) = 2
3.

18. If t(c) = (6
6
36, 5, 3), then chf (c) = 4 and frf (c) = 4
5.

19. If t(c) = (6
6
36, 6, 3), then chf (c) = 11
3 and frf (c) = 11
15.

20. If t(c) = (666
566), then chf (c) = 7
6 and frf (c) = 7
18.

21. If t(c) = (665
66), then chf (c) = 2 and frf (c) = 1
2.

22. If t(c) = (9, 3, 5, 3), then chf (c) = 11
3 and frf (c) = 11
15.

23. If t(c) = (3, 9, 3, 5, 3), then chf (c) = 29
6 and frf (c) = 29
36.

24. If t(c) = (3, 9, 3, 5), then chf (c) = 25
6 and frf (c) = 5
6.

25. If t(c) = (5, 3, 9, 3, 5), then chf (c) = 16
3 and frf (c) = 8
9.

26. If t(c) = (9, 3, 5
3), then chf (c) = 19
6 and frf (c) = 19
24.

27. If t(c) = (3, 9, 3, 5
3), then chf (c) = 13
3 and frf (c) = 13
15.

28. If t(c) = (5, 9, 3, 5
3), then chf (c) = 23
6 and frf (c) = 23
30.

29. If t(c) = (5, 3, 9, 3, 5
3), then chf (c) = 11
2 and frf (c) = 11
12.

30. If t(c) = (53, 3, 9, 3, 5
3), then chf (c) = 17
3 and frf (c) = 17
18.

31. If t(c) = (9, 5
3, 3), then chf (c) = 3 and frf (c) = 3
4.

32. If t(c) = (3, 9, 5
3, 3), then chf (c) = 25
6 and frf (c) = 5
6.

33. If t(c) = (9, 3, 6), then chf (c) = 8
3 and frf (c) = 2
3.

34. If t(c) = (3, 9, 3, 6), then chf (c) = 23
6 and frf (c) = 23
30.

35. If t(c) = (3, 6, 5, 6, 3), then chf (c) = 13
3 and frf (c) = 13
18.

36. If t(c) = (53, 3, 9, 5, 9, 3, 5
3), then chf (c) = 20
3 and frf (c) = 5
6.

Proof. As the proof is merely a routine checking, we only prove item (1). Items (2)-(36)
are proved in a similar way.
(1) is proved as follows. First note that by the deﬁnition of Πf , every face adjacent
to f1 is of length at least 9. If |f | = 9, then by 2.2, any face adjacent to f1, other than
f , is of length ⩾ 11, and (a) follows by Rules(3,12). Suppose |f | ⩾ 11 (the proof when
|f | = 10 follows by the same arguments). If f1 is adjacent to a 9-face, then by 2.2, the
third face adjacent to f1 is of size ⩾ 11, and the claim follows by Rules(3,12). If f1 is
adjacent to exactly one 10-face, then by 2.2, f1 is not adjacent to a 9-face. Thus the third
face adjacent to f1 is of length ⩾ 11 and the claim follows by Rules(2,12). If f1 is adjacent
to two 10-faces, then the claim follows by Rules(2,12).

The following shows that ch
∗(f ) ⩽ 0 for all “large” faces.

the electronic journal of combinatorics 20(2) (2013), #P7 29

5.5. If |f | ⩾ 72, then ch
∗(f ) ⩽ 0.

Proof. Let v ∈ V (f ). If v ∈ V (P (c)) for some c ∈ Πf , then by (10), v sends a charge of
frf (c) to f . Otherwise, by (5), v sends 1
3 to f . Hence v sends a charge of at most µ to f ,
where µ = max{ 1
3, max
c∈Πf {frf (c)}}. By 5.4, µ ⩽ 17
18. Hence, ch
∗(f ) ⩽ (4 − k) + 17
18k, and for

k ⩾ 72, ch∗(f ) ⩽ 0.

Next we show that ch
∗(f ) ⩽ 0 when 9 ⩽ |f | ⩽ 15.

5.6. If 9 ⩽ |f | ⩽ 15, then ch
∗(f ) ⩽ 0.

Proof. Suppose |f | = 15. By 2.2(1), if c ∈ Πf and |St(c)| > 0, then F (c) contains no
3-face adjacent to f . Hence by inspection of ℑall,

t(c) ∈ {(5), (6
6
36), (6
6
36, 5), (6
66
566), (665
66), (6
9
36)}

By 5.4, frf (c) ⩽ 2
3. By (9), ch
∗(f ) ⩽ 4 − |f | + 2
3 · |f | = 4 − 15 + 2
3 · 15 < 0.

Suppose |f | = 14. If c ∈ Πf , then c does not extend f by two. By 4.1

t(c) ∈ T := {(3), (5), (3, 6), (6, 3, 6), (3, 6, 5), (6, 3, 6, 5), (6
6
36, 6, 3), (6
6
36), (6
6
36, 5),

(6
66
566), (6
65
66), (6
9
36), (9, 3, 6)}

Let T ′ := {(3), (6, 3, 6), (6
6
36, 6, 3), (6, 3, 6, 5)} ⊆ T

By 5.4, frf (c) ⩽ 2
3 for every c ∈ T \ T ′. We may assume that ∑

X∈T ′ |SX| ⩾ 1; for

otherwise ch
∗(f ) ⩽ 4 − |f | + |f | · 2
3 ⩽ 4 − 14 + 14 · 2
3 < 0. By 2.3(1), 3.4 (1), and 2.2(1),
we deduce that ∑

X∈T ′ |SX| = 1. Let X ∈ T ′ so that |SX| = 1 and let c ∈ SX. Then, by

(9), ch
∗(f ) ⩽ 4 − |f | + |P (c)| · frf (c) + (|f | − |P (c)|) · 2
3. If X = (6, 3, 6), then by 5.4(8),
frf (c) ⩽ 5
6 and |P (c)| = 4; hence ch
∗(f ) ⩽ 4 − 14 + 4 · 5
6 + 10 · 2
3 = 0. If X ∈ T ′ \ {(6, 3, 6)},
then |P (c)| ⩽ 5 and by 5.4(1,9,19), frf (c) ⩽ 4
5; hence, ch
∗(f ) ⩽ 4 − 14 + 5 · 4
5 + 9 · 2
3 = 0.

Suppose |f | = 13. By 2.3 (0), f is not adjacent to a 5-face, and c does not extend f by

three, for every c ∈ Πf . Hence using 4.1 we see that t(c) ∈ {(3), (6
9
36), (6
66
566), 6
9
36)}.

By 5.4, we see that if t(c) ∈ {(6
6
36), (6
66
566), 6
9
36)}, then |P (c)| = 3 and frf (c) ⩽ 2
3; and
if t(c) = (3), then |P (c)| = 2 and frf (c) ⩽ 3
4. By 4.5(2), |S(3)| ⩽ 2. Hence, ch∗(f ) ⩽
4 − |f | + 4 · 3
4 + (|f | − 4) · 2
3 = 4 − 13 + 4 · 3
4 + (13 − 4) · 2
3 = 0.

Suppose |f | = 12. By 2.3(0), f is not adjacent to a six face, and c does not extend
f by four, for every c ∈ Πf . By 4.1, t(c) ∈ T := {(3), (5), (3, 5), (3, 5, 3)}. By 3.4(1)
and 2.3(1,2) we see that

(i) for distinct c1, c2 ∈ Πf , c1 and c2 are disjoint.

By 4.5(1),

the electronic journal of combinatorics 20(2) (2013), #P7 30

(ii) 3 · |S(3,5,3)| + |S(3)| + 3 · |S(3,5)| < 4.

By (i) and 2.2(1),

(iii) if |S(3,5,3)| + |S(3)| + |S(3,5)| ⩾ 1, then |S(5)| = 0.

We may assume that the following holds:

(a) |S(3,5,3)| = 0. For otherwise, let c ∈ S(3,5,3). Note that |P (c)| = 4. By 5.4(4b),
frf (c) = 2
3. Hence, by (i) and (ii), ch∗(f ) ⩽ 4 − 12 + 4 · 2
3 + (12 − 4) · 1
3 < 0.

(b) |S(3,5)| = 0. For otherwise let c ∈ S(3,5). Note that |P (c)| = 3. By (i)-(iii) and (a),
|S(3,5)| + |S(3)| + |S(5)| = 1. By 5.4(3b), frf (c) = 8
9. Hence, ch
∗(f ) ⩽ 4 − 12 + 3 · 8
9 +
(12 − 3) · 1
3 < 0.

Now, if |S(5)| ⩾ 1, then by (iii), |S(3)| = 0. By 5.4(4b), if c ∈ S(5) then frf (c) = 1
2.
Hence, ch∗(f ) ⩽ 4 − 12 + 12 · 1
2 < 0. If |S(5)| = 0, then by 4.5, |S(3)| ⩽ 3. By 5.4(1b), if
c ∈ S(3) then frf (c) ⩽ 3
4. Hence, ch∗(f ) ⩽ 4 − 12 + 6 · 3
4 + (12 − 6) · 1
3 < 0.

|f | = 11. By 2.3(0), c does not extend f by ﬁve, for every c ∈ Πf . By 4.1,

t(c) ∈ T := {(3), (5), (3, 5), (3, 5, 3), (3, 5
3), (6, 3, 6), (3, 6), (6
66
566), (9, 5
3, 3), (9, 3, 6)}

Let T ′′ := {(5), (6
66
566)}. By 5.4, if c ∈ Πf and c ∈ T ′′, then fr(c′, f ) ⩽ 1
2. Also, by
deﬁnition of ℑF , T \ T ′′ ⊆ ℑF . We may assume that

(a) |S(6,3,6)| + |S(9,53,3)| + |S(9,3,6)| = 0. For otherwise let

T ′ := {(3), (3, 5), (3, 5, 3), (3, 5
3), (6, 3, 6), (3, 6)}

By 4.5, |S(6,3,6)| + |S(9,53,3)| + |S(9,3,6)| = 1. Using 2.3(1), we conclude that |SX| = 0,
for every X ∈ T ′. Let c ∈ S(6,3,6) ∪ S(9,53,3) ∪ S(9,53,3) (|P (c)| = 4). By 5.4(8a,31,33),
frf (c) ⩽ 5
6. Hence, ch∗(f ) ⩽ 4 − 11 + 1 · 10
3 + (11 − 4) · 1
2 < 0.

(b) |S(3,6)| + |S(3,53)| = 0. For otherwise let T ′ := {(3), (3, 5), (3, 5, 3)}. By 2.3(0,1), we
see that |S(3,6)| + |S(3,53)| = 1, and |SX| = 0, for every X ∈ T ′. Let c ∈ S(3,6) ∪ S(3,53)
(|P (c)| = 3). By 5.4(6b,5b), frf (c) ⩽ 8
9. Hence, ch
∗(f ) ⩽ 4−11+3· 8
9 +(11−3)· 1
2 < 0.

(c) |S(3,5,3)| = 0. For otherwise let T ′ := {(3, 5), (3, 5, 3)}. By 4.5(1), |S(3,53)| = 1,
|S(3)| ⩽ 1 and |SX| = 0, for every for X ∈ T ′. In addition, by 2.3(0,2), |S(5)| = 0.
Let c ∈ S(3,5,3) (|P (c)| = 4). By 5.4 we see that frf (c) = 2
3, and if c′ ∈ Πf and
c′ = (3), then frf (c) ⩽ 3
4 to f . Hence, ch
∗(f ) ⩽ 4 − 11 + 4 · 2
3 + 2 · 3
4 + (11 − 6) · 1
2 < 0.

(d) |S(3,5)| = 0. For otherwise by 4.5(1), |S(3,5)| = 1, and |S(3)| ⩽ 1. Let c ∈ S(3,5)
(|P (c)| = 3), and let F (c) = {f1, f2} such that |f1| = 3 and |f5| = 5. By 2.3(0),
f1 is not adjacent to a 9-face, and thus by 5.4(3b), frf (c) = 7
9. Hence, ch
∗(f ) ⩽
4 − 11 + 3 · 7
9 + 2 · 3
4 + (11 − 5) · 1
2 < 0.

the electronic journal of combinatorics 20(2) (2013), #P7 31

Now, if |S(5)|+|S(666
566)| ⩾ 1, then |S(3)| ⩽ 1, and ch
∗(f ) ⩽ 4−11+2· 3
4 +(11−2)· 1
2 ⩽ 0.

If |S(5)| + |S
(666
566)| = 0, then, by 4.5 |S(3)| ⩽ 4, and ch∗(f ) ⩽ 4 − 11 + 8 · 3
4 + (11 − 8) · 1
3 = 0.

Suppose |f | = 10. By 2.3(2) and 2.2(1), f is adjacent to at most one 5-face. Also, c
does not extend f by six, for every c ∈ Πf . By 4.1,

t(c) ∈ T := {(3), (5), (3, 5), (3, 5
3), (3, 5, 3), (6, 3, 6), (3, 5, 6, 3), (3, 6), (6
65
66), (3, 6, 5)}

We may assume that

(a) |S(3,6,5)| + |S(3,5,6,3)| + |S(66566)| = 0. For otherwise, by 3.4(1), |S(3,6,5)| + |S(3,5,6,3)| +
|S(66566)| = 1, and |SX| = 0, for every X ∈ T \ {(3, 6, 5), (3, 5, 6, 3), (6
65
66)}. Let
c ∈ S(3,6,5) ∪ S(3,5,6,3) ∪ S(66566) (|P (c)| ⩽ 5). By 5.4(7,10a, 21), frf (c) ⩽ 4
5. Hence,
ch
∗(f ) ⩽ 4 − 10 + 5 · 4
5 + (10 − 5) · 1
3 < 0.

(b) |S(3,6)| + |S(6,3,6)| = 0. For otherwise, by 3.4(1), |S(3,6)| + |S(6,3,6)| = 1, |S(3)| ⩽ 1,
and |SX| = 0 for every X ∈ ℑ \ {(3), (3, 6), (6, 3, 6)}. Let {c} = S(3,6) ∪ S(6,3,6)
(|P (c)| ⩽ 4). By 5.4(1c,6,8), frf (c) ⩽ 5
6 and if c′ ∈ Πf with t(c′) = (3), then
fr(c′, f ) ⩽ 2
3. Hence, ch∗(f ) ⩽ 4 − 10 + 4 · 5
6 + 2 · 2
3 + (10 − 6) · 1
3 = 0.

(c) |S(3,53)| = 0. For otherwise, by 3.4(1), |S(3,53)| = 1, |S(3)| ⩽ 1, and |SX| = 0 for
every X ∈ ℑ \ {(3), S(3,53)}. Let c = S(3,53) (|P (c)| = 3). By 5.4, frf (c) = 8
9. Hence,
ch
∗(f ) ⩽ 4 − 10 + 3 · 8
9 + 2 · 2
3 + (10 − 5) · 1
3 < 0.

(d) |S(3,5,3)| = 0. For otherwise, by 3.4(1), |S(3,5,3)| = 1, |S(3)| ⩽ 2, and |SX| = 0 for
every X ∈ ℑ \ {(3), (3, 5, 3)}. Let {c} = S(3,5,3) (|P (c)| = 4). By 5.4(4), frf (c) = 2
3.
Hence, ch∗(f ) ⩽ 4 − 10 + 4 · 2
3 + 4 · 2
3 + (10 − 8) · 1
3 = 0.

(e) |S(3,5)| = 0. For otherwise, by 3.4(1), |S(3,5)| = 1, |S(3)| ⩽ 2, |SX| = 0 for every
X ∈ ℑ \ {(3), (3, 5)}. Let {c} = S(3,5), and let F (c) = {f1, f2} where |f1| = 3 and
|f2| = 5. By 2.3(0), f1 is not adjacent to a 9-face, and hence by 5.4(3b), frf (c) = 7
9.
As |P (c)| = 3, then ch∗(f ) ⩽ 4 − 10 + 3 · 7
9 + 4 · 2
3 + (10 − 7) · 1
3 = 0.

(f) |S(5)| = 0. For otherwise, by 4.5(2), |S(5)| = 1, |S(3)| ⩽ 2 and |S(66566)| = 0. Let
{c} = S(5) ( |P (c)| = 2). By 5.4(2), frf (c) = 1
2. Hence, ch∗(f ) ⩽ 4 − 10 + 2 · 1
2 + 4 ·
2
3 + (10 − 6) · 1
3 < 0.

It follows, that if c ∈ Πf , then t(c) = (3). By 4.5, |S(3)| ⩽ 5. Note that by 5.4(1c),
if v ∈ V (f ) then v sends to f a charge of at least 3
5 at most 2
3. If |S(3)| ⩽ 4, then
ch
∗(f ) ⩽ 4 − 10 + 8 · 2
3 + (10 − 8) · 1
3 ⩽ 0. If |S(3)| = 5, then by 2.3(0), f is not adjacent
to a 10-face. By 5.4(1c), chf (c) = 6
5. Hence, ch∗(f ) ⩽ 4 − 10 + 5 · 6
5 = 0.

Suppose |f | = 9. c does not extend f by seven, for every c ∈ Πf . By 4.1, together
with 2.8, 2.15 and 2.2(1), we conclude that

t(c) ∈ T := {(3), (5), (3, 5), (3, 5
3), (3, 5, 3), (6, 3, 6), (3, 5, 6, 3), (3, 6), (3, 6, 6, 3),

(3, 6, 5), (6
9
36)}

We may assume that

the electronic journal of combinatorics 20(2) (2013), #P7 32

(a) |S(6
9
36)| = 0. For otherwise, by 3.4(4) and 2.3(0), it follows that |SX| = 0, for every

X ∈ T \ {(3), (6
9
36)}. By 5.4, if c ∈ Πf and t(c) ∈ {(3), (6
9
36)}, then frf (c) ⩽ 5/9.
Hence, ch∗(f ) ⩽ 4 − 9 + 9 · 5
9 ⩽ 0.

(b) |S(3,6,6,3)| = 0. For otherwise, by 4.5(2), |S(3,6,6,3)| = 1, and |SX| = 0, for every
X ∈ T \ {(3, 6, 6, 3)}. Let c ∈ S(3,6,6,3) (|P (c)| = 5). By 5.4(13), frf (c) = 3
5. Hence,
ch
∗(f ) ⩽ 4 − 9 + 5 · 3
5 + (9 − 5) · 1
3 < 0.

(c) |S(3,6,5)| + |S(3,5,6,3)| = 0. For otherwise, by 4.5, |S(3,6,5)| + |S(3,5,6,3)| = 1, |SX| = 0,
for every X ∈ T \ {(3, 6, 5), (3, 5, 6, 3), (3)}, and S(3) ⩽ 1. Let c ∈ S(3,6,5) ∪ S(3,5,6,3)
(|P (c)| ⩽ 5). By 5.4(7,10), frf (c) ⩽ 2
3. Hence, ch∗(f ) ⩽ 4−9+5· 2
3 +2· 1
2 +(9−7)· 1
3 =
0.

(d) |S(3,53)|+|S(3,6)|+|S(6,3,6)| = 0. For otherwise, by 4.5(2), |S(3,53)|+|S(3,6)|+|S(6,3,6)| =
1, S(3) ⩽ 2, and |SX| = 0, for every X ∈ T \ {(3, 5
3), (3, 6), (6, 3, 6), (3)}. Let
c ∈ S(3,53) ∪ S(3,6) ∪ S(6,3,6) (|P (c)| ⩽ 4). By 5.4, frf (c) ⩽ 2
3, and if c′ ∈ Πf with
t(c′) = (3) then fr(c′, f ) = 1
2. Hence, ch∗(f ) ⩽ 4 − 9 + 4 · 2
3 + 4 · 1
2 + (9 − 8) · 1
3 = 0.

(e) |S(3,5,3)| = 0. For otherwise, we have that 1 ⩽ |S(3,5,3)| ⩽ 2. If |S(3,5,3)| = 2, then
by 4.5(2), |SX| = 0, for every X ∈ T \{(3, 5, 3)}. Hence, ch(f ) ⩽ 4−9+2·4· 7
12 +1· 1
3 ⩽
0. If |S(3,5,3)| = 1, then if |S(3,5)| = 1, ch
∗(f ) ⩽ 4 − 9 + 4 · 7
12 + 3 · 2
3 + (9 − 7) · 1
3 ⩽ 0,
and if |S(3,5)| = 0, then ch∗(f ) ⩽ 4 − 9 + 7
3 + (5) · 1
2 < 0.

(f) |S(3,5)| = 0. For otherwise, we have that 1 ⩽ |S(3,5)| ⩽ 2. If |S(3,5)| = 2, then
|SX| = 0, for every X ∈ T \ {(3, 5)}, and ch(f ) ⩽ 4 − 9 + 2 · 3 · 2
3 + 3 · 1
3 ⩽ 0. Suppose
then that |S(3,5)| = 1. If |S(5)| = 1, then |SX| = 0, for every X ∈ T \ {(3, 5), (5)}
and ch
∗(f ) ⩽ 4 − 9 + 3 · 2
3 + 2 · 1
2 + (9 − 5) · 1
3 ⩽ 0. If |S(5)| = 0, then |S(3)| ⩽ 3, and
ch
∗(f ) ⩽ 4 − 9 + 2 + 1 · 3 = 0.

It follows that if |SX| ⩾ 1, for some X ∈ T , then X ∈ {(3), (5)}. By 5.4(1a,2),
ch(f ) ⩽ 4 − 9 + 4 · 1 + 1 · 1
3 < 0.

It remains to show that ch
∗(f ) ⩽ 0, when 17 ⩽ |f | ⩽ 71. We start with the following
observation.

5.7. If |ΠℑP | ⩽ 1, then ch
∗(f ) ⩽ 0.

Proof. By the deﬁnition of ℑP and 5.4 we may assume the following:

(i) If there exists a cluster c ∈ Πf such that t(c) ∈ ℑP , then every v ∈ V (P (c)) sends
to f a charge of at most 17
18;

(ii) In the particular case that c ∈ Πf and t(c) ∈ {(3, 6, 6, 3, 6, 6, 3), (5
3, 3, 9, 5, 9, 5
3, 3)}
then every v ∈ V (P (c)) sends to f a charge of at most 5
6; and

(iii) If there exists a cluster c ∈ Πf such that t(c) ∈ ℑall \ ℑP , then every v ∈ V (P (c))
sends to f a charge of at most 2
3.

If |Πf (ℑP )| = 0, then by (iii) and (5), if v ∈ V (f ), then v sends to f a charge of
at most 2
3. Hence, ch
∗(f ) ⩽ 4 − |f | + 2
3(|f |), and for |f | ⩾ 17, ch∗(f ) ⩽ 0. Suppose
that |Πf (ℑP )| = 1. If t(c) ∈ {(3, 6, 6, 3, 6, 6, 3), (5
3, 3, 9, 5, 9, 5
3, 3}, then |P (c)| = 8. By

the electronic journal of combinatorics 20(2) (2013), #P7 33

(i), (ii) and (5), ch
∗(f ) ⩽ 4 − |f | + 8 · 5
6 + 2
3(|f | − 8), and for f ⩾ 17, ch
∗(f ) ⩽ 0.
If t(c) ̸∈ {(3, 6, 6, 3, 6, 6, 3), (5
3, 3, 9, 5, 9, 5
3, 3}, then |P (c)| ⩽ 6. By (i), (ii) and (5),
ch
∗(f ) ⩽ 4 − |f | + 6 · 17
18 + 2
3(|f | − 6), and for f ⩾ 17, ch∗(f ) ⩽ 0.

As Πf (ℑP ) ⊆ Πf (ℑF ), by 5.7, |ΠℑP |, |ΠℑF | ⩾ 2, which we may assume henceforth.

For every X ∈ ℑall let
 SX = {c ∈ Πf : t(c) = X}. (11)

By 3.4 (1),
 |f | = |Vs| + ∑

c∈Πf |P (c)| = |Vs| + ∑

X∈ℑall |SX| · |P (X)|. (12)

Using (11) and the deﬁnition of ℑall, (12) can be written as follows.
 (13)

|f | = |Vs| + ∑

X∈ℑall(|SX| · |P (X)|) = |Vs| + 2 · |S(3)| + 3 · |S(3,5)| + 2 · |S(5)| +

3 · |S(3,53)| + 4 · |S(3,5,3)| + 4 · |S(6,3,6)| + 5 · |S(6,3,6,5)| +
5 · |S(3,6,6,3)| + 5 · |S(3,5,6,3)| + 6 · |S(6,3,6,6,3)| + 6 · |S(6,3,6,5,3)| +
3 · |S(3,6)| + 3 · |S
(66
36)| + 4 · |S(6
6
36,5)| + 5 · |S
(66
36,5,3)| +

3 · |S(666
566)| + 4 · |S(66566)| + 4 · |S(3,6,5)| + 5 · |S
(66
36,6,3)| +

5 · |S(9,3,5,3)| + 6 · |S(3,9,3,5,3)| + 5 · |S(3,9,3,5)| + 5 · |S(3,9,3,5)| +
4 · |S(9,3,53)| + 5 · |S(3,9,3,53)| + 5 · |S(5,9,3,53)| + 6 · |S(5,3,9,3,53)| +
6 · |S(53,3,9,3,53)| + 4 · |S(9,53,3)| + 5 · |S(3,9,53,3)| + 8 · |S(3,6,6,3,6,6,3)| +
3 · |S(6
9
36)| + 6 · |S(3,6,5,6,3)| + 4 · |S(9,3,6)| + 5 · |S(3,9,3,6)| +

8 · |S(53,3,9,5,9,3,53)|

For ℑ ∈ {ℑP , ℑF } let
 Πf (ℑ) = {c ∈ Πf : t(c) ∈ ℑ}. (14)

By 4.5(1), if |f | ⩾ 9 and |Πf (ℑP )| ⩾ 2, then
∑

X∈ℑP |SX| · MX < α(|f |) − |f | − β(|f |, |S
(6
6
36)|, |S
(66
36,5)|, |S
(69
36)|) (15)

By 4.5(2), if k ∈ {17, 18} and |Πf (ℑF )| ⩾ 2, then
∑

X∈ℑF |SX| · MX < α(|f |) − |f | − β(|f |, |S
(6
6
36)|, |S
(66
36,5)|, |S
(69
36)|) (16)

We wish to write (15) and (16) in terms of the variables, {SX}X∈ℑall. By the deﬁnition
of ℑP , (15) can be written as follows.

the electronic journal of combinatorics 20(2) (2013), #P7 34

(17)
1 · |S(3)| + 3 · |S(3,5)| + 4 · |S(3,53)| + 3 · |S(3,5,3)| + 4 · |S(6,3,6)| +
7 · |S(6,3,6,5)| + 6 · |S(3,6,6,3)| + 5 · |S(3,5,6,3)| + 8 · |S(6,3,6,6,3)| +
7 · |S(6,3,6,5,3)| + 8 · |S
(66
36,5,3)| + 9 · |S
(6
6
36,6,3)| + 8 · |S(9,3,5,3)| +

8 · |S(3,9,3,5,3)| + 7 · |S(3,9,3,5)| + 7 · |S(5,3,9,3,5)| + 8 · |S(9,3,53)| + 8 · |S(3,9,3,53)| +
7 · |S(5,9,3,53)| + 8 · |S(5,3,9,3,53)| + 9 · |S(53,3,9,3,53)| + 8 · |S(9,53,3)| + 9 · |S(3,9,53,3)| +
10 · |S(3,6,6,3,6,6,3)| + 8 · |S(3,6,5,6,3)| + 7 · |S(9,3,6)| + 7 · |S(3,9,3,6)| +
14 · |S(53,3,9,5,9,3,53)| < α(|f |) − |f | − β(|f |, |S
(66
36)|, |S(6
6
36,5)|, |S(6
9
36)|)

By the deﬁnition of ℑF , (16) can be written as follows:
 (18)
3 · |S(3,6)| + 4 · |S(3,6,5)| +
1 · |S(3)| + 3 · |S(3,5)| + 4 · |S(3,53)| + 3 · |S(3,5,3)| + 4 · |S(6,3,6)| +
7 · |S(6,3,6,5)| + 6 · |S(3,6,6,3)| + 5 · |S(3,5,6,3)| + 8 · |S(6,3,6,6,3)| + 7 · |S(6,3,6,5,3)| +
8 · |S(6
6
36,5,3)| + 9 · |S
(66
36,6,3)| + 8 · |S(9,3,5,3)| + 8 · |S(3,9,3,5,3)| + 7 · |S(3,9,3,5)| +

7 · |S(5,3,9,3,5)| + 8 · |S(9,3,53)| + 8 · |S(3,9,3,53)| + 7 · |S(5,9,3,53)| + 8 · |S(5,3,9,3,53)| +
9 · |S(53,3,9,3,53)| + 8 · |S(9,53,3)| + 9 · |S(3,9,53,3)| + 10 · |S(3,6,6,3,6,6,3)| +
7 · |S(9,3,6)| + 7 · |S(3,9,3,6)| + 8 · |S(3,6,5,6,3)| +
14 · |S(53,3,9,5,9,3,53)| < α(f ) − |f | − β(|f |, |S
(66
36)|, |S
(66
36,5)|, |S
(69
36)|)

Next the proof continues according to the following sketch. For each value of |f |, 17 ⩽
|f | ⩽ 71, an integer program (IP henceforth) of the following form is constructed.

maximize(total(f )) (19)

subject to:

1. (13), and

2. (18) if |f | ∈ {17, 18}, or (17) if 19 ⩽ |f | ⩽ 71, and

3. Additional constraints based on the exact value of |f |.

For each value of |f | from 17 to 71, it will be shown that the maximum value of the
expression in (19) is at most |f | − 4. Hence by (9), ch
∗(f ) ⩽ 0.

The ﬁrst step is to derive an upper bound for total(f ) in term of the variables {SX}X∈ℑall.
Let c ∈ Πf . If t(c) ∈ ℑall \ {(3), (3, 5)}, then by 5.4, chf (c) attains a unique value
when 17 ⩽ |f | ⩽ 71. If t(c) ∈ {(3), (3, 5)}, then chf (c) attains several values, depending
on the faces adjacent to the faces of F (c). Using 5.4(1,2), S(3) and S(3,5) are partitioned
as follows:
Let S3/2
(3) , S7/5
(3) , S4/3
(3) ⊆ S(3) be a partition of S(3) into three subsets, sending a charge

of 3
2, 7
5 and 4
3 to f , respectively. Let S8/3
(3,5), S7/3
(3,5) ⊆ S(3,5) be a partition of S(3,5), into two
subsets, sending a charge of 8
3 and 7
3 to f , respectively. By deﬁnition

the electronic journal of combinatorics 20(2) (2013), #P7 35

|S(3)| = |S3/2
(3) | + |S7/5
(3) | + |S4/3
(3) |. (20)

|S(3,5)| = |S8/3
(3,5)| + |S7/3
(3,5)|. (21)

The following easily follows from the deﬁnition of Πf , 5.4(1, 2) and 2.2(1).

5.8. 1. Suppose c ∈ S3/2
(3) ∪ S8/3
(3,5). Then, there exists a 9-face g such that g is adjacent
to f and g /∈ F (c′) for every c′ ∈ Πf .

2. Suppose |S8/3
(3,5)| ⩾ 2 and let c1, c2 ∈ S8/3
(3,5) be distinct. Let g1, g2 ∈ F (G) such that
for i = 1, 2, |V (gi)| = 9, V (gi) ∩ V (ci) ̸= ∅, and c′
i = gi ∪ ci is a cluster of f of type
(9, 3, 5). Then, c1 and c2 are disjoint.

Using 5.4, (20), (21), we obtain the following upper bound for total(f ).
 (22)

total(f ) = ∑

c∈Πf chf (c) + 1
3 · |Vs| ⩽ 1
3|Vs| + 3
2 · |S3/2
(3) | + 7
5 · |S7/5
(3) | +

4
3 · |S4/3
(3) | + 8
3 · |S8/3
(3,5)| + 7
3 · |S7/3
(3,5)| + 1 · |S(5)| + 8
3 · |S(3,53)| + 8
3 · |S(3,5,3)| +

10
3 · |S(6,3,6)| + 4 · |S(6,3,6,5)| + 11
3 · |S(3,6,6,3)| + 4 · |S(3,5,6,3)| + 5 · |S(6,3,6,6,3)| +

16
3 · |S(6,3,6,5,3)| + 2 · |S(3,6)| + 2 · |S
(66
36)| + 8
3 · |S(6
6
36,5)| + 4 · |S(6
6
36,5,3)| +

7
6 · |S(666
566)| + 2 · |S(66566)| + 8
3 · |S(3,6,5)| + 11
3 · |S
(66
36,6,3)| + 3 2
3 · |S(9,3,5,3)| +

29
6 · |S(3,9,3,5,3)| + 25
6 · |S(3,9,3,5)| + 16
3 · |S(5,3,9,3,5)| + 19
6 · |S(9,3,53)| +

13
3 · |S(3,9,3,53)| + 23
6 · |S(5,9,3,53)| + 11
2 · |S(5,3,9,3,53)| + 17
3 · |S(53,3,9,3,53)| +

3 · |S(9,53,3)| + 25
6 · |S(3,9,53,3)| + 20
3 · |S(3,6,6,3,6,6,3)| + 5
3 · |S(6
9
36)| +

13
3 · |S(3,6,5,6,3)| + 8
3 · |S(9,3,6)| + 23
6 · |S(3,9,3,6)| + 20
3 · |S(53,3,9,5,9,3,53)|

In some parts of the proof that follows, a computer was used for solving certain IPs.
All IPs were solved by the second author by a simple C program that maximizes the
objective function through a simple brute-force search over all possible values of the set
of variables, and checked by the ﬁrst author by using Maple’s LPSolve function.

Suppose |f | ∈ {20, . . . , 71}. The following IP is constructed.

maximize(total(f ))
subject to: (13), (17), (20) and (21).

the electronic journal of combinatorics 20(2) (2013), #P7 36

By solving it, we obtain that total(f ) ⩽ |f | − 4 for each |f | ∈ {20, . . . , 71}.

Suppose |f | = 19. The proof follows by solving an IP which is identical to the one
constructed above but with the following additional constraint:

|S8/3
(3,5)| ⩽ 1 (23)

For the correctness of (23), suppose to the contrary that |S8/3
(3,5)| ⩾ 2, and let c1, c2 ∈ S8/3
(3,5)
be distinct. By 5.8(2), c1 and c2 are disjoint; but then f ∪ c1 ∪ c2 ⊆ G contains a 32-cycle;
a contradiction.

Suppose |f | ∈ {17, 18}. For these two values, maximizing total(f ) is done by solving
a sequence of IPs based on the value of |S3/2
(3) | + |S8/3
(3,5)|.

Case 1 Suppose |S3/2
(3) | + |S8/3
(3,5)| = 0 (24)

We split this into two cases.

Case 1.1 Suppose
 |S(6,3,6)| ⩽ 1 (25)

The proof follows by solving the following IP.

maximize(total(f )).
subject to: (13), (18), (20), (21), (24) and (25).

Case 1.2 Suppose |S(6,3,6)| ⩾ 2 (26)

It will be shown below that |S7/5
(3) | = 0 (27)

Then, the proof follows by solving the following IP.

maximize(total(f )).
subject to: (13), (18), (20), (21), (24), (26), (27).

Correctness of (27) is veriﬁed as follows. Let c1, c2 ∈ S(6,3,6) be distinct. Suppose for a
contradiction that |S7/5
(3) | ⩾ 1 and let c3 ∈ S7/5
(3) . By 3.4(2), c1 and c2 are disjoint. By

deﬁnition of S7/5
(3) , there exists a 10-face, f1, such that c′
3 = f1 ∪ c3, is a cluster of f of type
(3, 10). By 3.14(2), ci and c′
3 are disjoint, for i = 1, 2. But then c1 ∪ c2 ∪ c′
3 ⊆ G contains
a 32-cycle; a contradiction.

Case 2 Suppose |S3/2
(3) | + |S8/3
(3,5)| ⩾ 1 (28)

Case 2.1 Suppose ﬁrst that |S8/3
(3,5)| = 0 (29)

the electronic journal of combinatorics 20(2) (2013), #P7 37

Consider S3/2
(3) . By deﬁnition, if c ∈ S3/2
(3) , then there exists a 9-face adjacent to f and to
the 3-face of F (c). Deﬁne A to be the set of all such 9-faces, i.e.,

A = {g ∈ Γ(f ) : |g| = 9 and there exists c ∈ S3/2
(3) such that V (g) ∩ V (c) ̸= ∅}

By 2.2(3), 2.3(1,5), and as |f | ∈ {17, 18} and G contains no 32-cycles, it follows that
|A| ⩽ 2. Hence, |S3/2
(3) | ⩽ 4 (30)

The rest is a case analysis on |S3/2
(3) |.

Case 2.1.1 Suppose 3 ⩽ |S3/2
(3) | ⩽ 4 (31)

In this case |A| = 2. Hence, there exist distinct clusters c1 and c2 such that t(c1) = (3, 9, 3)
and t(c2) ∈ {(3, 9), (3, 9, 3)}. By 2.3(1,5), c1 and c2 are disjoint. Observe that if g is a
3-face adjacent to f , then g ∈ F (c1) or g ∈ F (c2), for otherwise G contains a 32-cycle.
By 3.14(1) and 2.3(0), it follows that

|S(3,53)|, |S(6,3,6)|, |S(6,3,6,5)| = 0 (32)

Next it is seen that |S7/5
(3) | = 0 (33)

For suppose that |S7/5
(3) | ⩾ 1. Let c ∈ S7/5
(3) , F (c) = {g} and g1 be the 10-face adjacent to
f and g. By 2.3(6), g ̸∈ F (c1) ∪ F (c2), and g is not adjacent to any of the faces of A.
It follows that G[E(g) ∪ E(c1) ∪ E(c2)] contains a 32-cycle, a contradiction. Hence (33)
holds.
By 5.8(1) and the same considerations as above, it follows that

|S(3,9,3,53)|, |S(5,3,9,3,53)|, |S(53,3,9,3,53)| = 0 (34)

The proof follows by solving the following IP.

maximize(total(f )).
subject to: (13), (18), (20), (21), (29), (31), (32), (33) and (34).

Case 2.1.2 Suppose that 1 ⩽ |S3/2
(3) | ⩽ 2 (35)

Let c ∈ S3/2
(3) . Let F (c) = {g}, and let g1 be the 9-face adjacent to f and g. Let
ˆc = g ∪ f be a cluster of type (3, 9). It is seen that

|S(3,9,3,53)|, |S(5,3,9,3,53)|, |S(53,3,9,3,53)| = 0 (36)

For suppose that at least one of the sets S(3,9,3,53), S(5,3,9,3,53) and S(53,3,9,3,53) is of size at
least one. Let c ∈ S(3,9,3,53) ∪ S(5,3,9,3,53) ∪ S(53,3,9,3,53). Then c contains a sub-cluster, c′, of
type (3, 9, 3, 5
3) (possibly c = c′). By 3.14(1), c and c
′
1 are disjoint. But then f ∪ ˆc ∪ c
contains a 32-cycle, a contradiction. Hence (36) holds.
Next the proof of this case continues by considering the value |S(3,53)| + |S(3,5,6,3)| +
|S(6,3,6)|.

the electronic journal of combinatorics 20(2) (2013), #P7 38

Case 2.1.2.1 Suppose |S(3,53)| + |S(3,5,6,3)| + |S(6,3,6)| = 0 (37)

The proof follows by solving the following IP.

maximize(total(f )).
subject to: (13), (18), (20), (21), (28), (29), (35), (36), and (37).

Case 2.1.2.2 Suppose |S(3,53)| + |S(3,5,6,3)| + |S(6,3,6)| ⩾ 1 (38)

By (35), 3.14(1) and as G contains no 32-cycles, it follows that

|S(3,53)| + |S(3,5,6,3)| + |S(6,3,6)| = 1 (39)

Three cases are possible.

1. Suppose |S(6,3,6)| = 1 (40)

The proof follows by solving the following IP.

maximize(total(f )).

subject to: (13), (18), (20), (21), (28), (29), (35), (39), and (40).

2. Suppose |S(3,5,6,3)| = 1 (41)

Let c ∈ S(3,5,6,3). By 3.14(1), ˆc and c are disjoint.

It is shown that |S7/5
(3) | + |S(3,5)| ⩽ 2 (42)

Let c1 ∈ S7/5
(3) ∪ S(3,5). For the correctness of (42) it suﬃces to show that if g ∈ F (c1)
and |g| = 3, then V (g) ∩ V (ˆc), V (g) ∩ V (c) = ∅.

(a) Suppose c1 ∈ S(3,5). By 3.4(2), c and c1 are disjoint. Also, ˆc and c1 are
disjoint for otherwise ˆc ∪ c1 is a cluster of f of type (3, 9, 3, 5) containing c1; a
contradiction to the deﬁnition of Πf .

(b) If c1 ∈ S7/5
(3) ,then by 3.4(2), c and c1 are disjoint, and by 2.3(6), ˆc and c1 are
disjoint.

The proof follows by solving the following IP.

maximize(total(f )).

subject to: (13), (18), (20), (21), (28), (29), (35), (39), (41), and (42).

3. Suppose |S(3,53)| = 1 (43)

By the same arguments as in the proof of (42), it follows that

|S7/5
(3) | + |S(3,5)| ⩽ 3 (44)

The proof follows by solving the following IP.

the electronic journal of combinatorics 20(2) (2013), #P7 39

maximize(total(f )).

subject to: (13), (18), (20), (21), (28), (29), (35), (39), (43), and (44).

Case 2.2 Suppose |S8/3
(3,5)| ⩾ 1 (45)

By 5.8(2), and as G contains no 32-cycles we have

|S8/3
(3,5)| ⩽ 2 (46)

Two cases are considered. Either |S8/3
(3,5)| = 2 or |S8/3
(3,5)| = 1.

Case 2.2.1 Suppose |S8/3
(3,5)| = 2 (47)

Let c1, c2 ∈ S8/3
(3,5). By 5.8(2) and the deﬁnition of S8/3
(3,5), there exist disjoint clusters,
c′
1 and c′
2, of type (9, 3, 5) such that F (c1) ⊆ F (c′
1) and F (c2) ⊆ F (c′
2). Suppose that g is
a 3-face adjacent to f . By 1.3 and the deﬁnition of Πf , g and ci are disjoint, for i = 1, 2.
As |S8/3
(3,5)| = 2, and G contains no 32-cycles, it follows that g ∈ F (c1) ∪ F (c2). As by the
deﬁnition of Πf a face belongs to at most one cluster, then the two 3-faces in F (c1)∪F (c2)
are the sole 3-faces adjacent to f . In particular we have

|S3/2
(3) |, |S7/5
(3) |, |S4/3
(3) |, |S(6,3,6)|, |S(3,9,3,53)|, |S(5,3,9,3,53)|, (48)

|S(53,3,9,3,53)|, |S(3,5,6,3)|, |S(3,53)| = 0

The proof follows by solving the following IP.

maximize(total(f )).
subject to: (13), (17), (20), (21), (28), (47), and (48).

Case 2.2.2 Suppose |S8/3
(3,5)| = 1 (49)

Either |S3/2
(3) | ⩾ 1 or |S3/2
(3) | = 0.

Case 2.2.2.1 Suppose |S3/2
(3) | ⩾ 1 (50)

By 2.3 and as G contains no 32-cycles, it is seen that

1 ⩽ |S3/2
(3) | ⩽ 2 (51)

By similar arguments as in Case (2.2.1), it follows that

|S(6,3,6,5,3)|, |S7/5
(3) |, |S4/3
(3) |, |S(6,3,6)|, |S(3,9,3,53)|, |S(5,3,9,3,53)|, (52)

|S(53,3,9,3,53)|, |S(3,5,6,3)|, |S(3,53)| = 0

The proof follows by solving the following IP.

maximize(total(f )).
subject to: (13), (17), (20), (21), (28), (49), (51), and (52).

the electronic journal of combinatorics 20(2) (2013), #P7 40

Case 2.2.2.2 Suppose |S3/2
(3) | = 0 (53)

By similar arguments as in the cases above, it follows that

|S(53,3,9,3,53)| = 0, |S(5,3,9,3,53)| = 0, |S(6,3,6,5,3)| + |S(3,5,6,3)| + |S(6,3,6)| + |S(3,53)| ⩽ 1 (54)

|S(6,3,6,5)| + |S(3,5)| ⩽ 1, |S(6,3,6,5,3)| + |S(3,5)| ⩽ 1 (55)

If |S(3,53)| = 0 (56)

the proof follows by solving the following IP.

maximize(total(f )).
subject to: (13), (17), (20), (21), (28), (49), (53), (54), (55).

If, |S(3,53)| ⩾ 1 (57)

It is seen that,
 |S(3,53)| ⩽ 1, |S(3)| ⩽ 3 (58)

The proof follows by solving the following IP.

maximize(total(f )).
subject to: (13), (17), (20), (21), (28), (49), (53), (57), (58).

6 Further Research

This paper is hopefully another step towards resolving the Erd˝os-Gy´arf´as Conjecture; it
might also be seen as an indication of what properties a counterexample would have to
have. The next step could involve weakening one of the conditions of 1.1 (and most likely
raising the upper bound on m); here, the authors consider how diﬃcult it would be in
each case.
Planarity could conceivably be replaced with projective-planarity, because the dis-
charging process would still be feasible. (The projective plane has a positive Euler char-
acteristic. The torus and Klein bottle both have Euler characteristic zero; using discharg-
ing on either of the latter surfaces also would require ﬁnding a face whose ﬁnal charge is
negative. Using a discharging argument on a surface with a negative Euler characteristic
is possible — it has even been done — but it requires much more accounting than even
the torus and Klein bottle cases.) However, many of the arguments in Section 2 would
become more complex, because a few pairs of edges would be allowed to cross. Planarity
thus seems to be the least likely of the hypotheses to weaken.
Replacing 3-connectivity with 2-connectivity looks more promising; the 3-connectivity
of an alleged minimal counterexample was used only in a few places in Section 2. Once
again, some further analysis would be required to obtain the contradictions needed to
prove the lemmas in that section.

the electronic journal of combinatorics 20(2) (2013), #P7 41

Allowing vertices of degree four will ruin the proof of several lemma as well, since the
fact that “two faces with a common vertex also have a common edge” was used early
on as well. Vertices of higher degree should not be much more of a problem because
(1) it can be assumed that no two vertices of degree greater than three are adjacent, and
(2) vertices with larger degrees have negative charges, and these negative charges can be
sent to a conﬁguration that complicates the proof. It seems likely that, instead of proving
that certain conﬁgurations are impossible, that it can be proven that they are possible,
but there must be one or more vertices of large degree nearby.

References

[1] Paul Erd˝os, Some old and new problems in various branches of combinatorics, Dis-
crete Math., 165 (1997), 227-231.

[2] Klas Markstr¨om, Extremal graphs for some problems on cycles in graphs, Cong.
Numer., 171 (2004), 2179-2192.

[3] Stephen E. Shauger, Results on the Erd˝os-Gy´arf´as conjecture in K1,m-free graphs,
Proc. 29th Southeastern Int. Conf. Combinatorics, Graph Theory, and Computing
(2004), 61-65.

[4] Dale Daniel and Stephen E. Shauger, A result on the Erd˝os-Gy´arf´as conjecture in
planar graphs, Proc. 29th Southeastern Int. Conf. Combinatorics, Graph Theory, and
Computing (2001), 129-139.

the electronic journal of combinatorics 20(2) (2013), #P7 42

7 Appendix: Properties of Clusters

The following page summarizes most of the important information related to the clusters
present in this paper. (Mc = max Ωc.)
 (chf (c), frf (c))
t(c) |P (c)| c ∈ Ωc |f | = 9 |f | > 9
(3) 2 ℑS, ℑF , ℑP {0,1} (1, 1
2) See 5.4
(3, 5) 3 ℑS, ℑF , ℑP [0, 3] (2, 2
3) See 5.4
(5) 2 ℑS {0,3} (1, 1
2) (1, 1
2)
(3, 5, 3) 4 ℑS, ℑF , ℑP [0, 3] ( 7
3, 7
12) ( 8
3, 2
3)
(6, 3, 6) 5 ℑS, ℑF , ℑP [0, 4] \ 2 ( 8
3, 2
3) ( 10
3 , 5
6)
(6, 3, 6, 5) 5 ℑS, ℑF , ℑP [0, 7] \ 2 — (4, 4
5)
(3, 6, 6, 3) 5 ℑS, ℑF , ℑP [0, 6] \ 2 (3, 3
5) ( 11
3 , 11
5 )
(3, 5, 6, 3) 5 ℑS, ℑF , ℑP [0, 5] \ 2 ( 10
3 , 2
3) (4, 4
5)
(6, 3, 6, 6, 3) 6 ℑS, ℑF , ℑP [0, 8] \ 5 — (5, 5
6)
(6, 3, 6, 5, 3) 6 ℑS, ℑF , ℑP [0, 7] \ {2, 5} — ( 16
3 , 8
9)
(3, 6) 3 ℑS, ℑF [0, 4] \ 2 ( 5
3, 5
9) (2, 2
3)
(3, 6, 5) 4 ℑS, ℑF [0, 5] \ 2 ( 7
3, 7
12) ( 8
3, 2
3)
(9, 3, 5, 3) 5 ℑS, ℑ9, ℑF , ℑP [0, 8] \ 5 — ( 11
3 , 11
15)
(3, 9, 3, 5, 3) 6 ℑS, ℑ9, ℑF , ℑP [0, 8] \ 5 — ( 29
6 , 29
36)
(3, 9, 3, 5) 5 ℑS, ℑ9, ℑF , ℑP [0, 7] \ {2, 5} — ( 25
6 , 5
6)
(5, 3, 9, 3, 5) 6 ℑS, ℑ9, ℑF , ℑP [0, 7] \ {2, 5} — ( 16
3 , 8
9)
(3, 6, 6, 3, 6, 6, 3) 8 ℑS, ℑF , ℑP [0, 10] — ( 20
3 , 5
6)
(3, 6, 5, 6, 3) 6 ℑS, ℑF , ℑP [0, 8] \ 5 — ( 13
3 , 13
18)
(9, 3, 6) 4 ℑS, ℑ9, ℑF , ℑP [0, 7] \ {2, 5} — ( 8
3, 2
3)
(3, 9, 3, 6) 5 ℑS, ℑ9, ℑF , ℑP [0, 7] \ {2, 5} — ( 23
6 , 23
30)
(3, 5
3) 3 ℑC, ℑ3
C, ℑF , ℑP [0, 4] (2, 2
3) ( 8
3, 8
9)

(6
66
566) 3 ℑC, ℑ5
C {0} — ( 7
6, 7
18)
(6
65
66) 4 ℑC, ℑ5
C {0} — (2, 1
2)

(6
6
36) 3 ℑC, ℑ6
C {0, 6} (2, 2
3) (2, 2
3)

(6
6
36, 5) 4 ℑC, ℑ6
C {0, 6} ( 8
3, 2
3) ( 8
3, 2
3)

(6
6
36, 5, 3) 5 ℑC, ℑ6
C, ℑF , ℑP [0, 8] \ 5 — (4, 4
5)

(6
6
36, 6, 3) 5 ℑC, ℑ6
C, ℑF , ℑP [0, 9] \ 5 — ( 11
3 , 11
15)

(6
9
36) 3 ℑC, ℑ6∗
C {0, 6} ( 5
3, 5
9) ( 5
3, 5
9)
(9, 3, 5
3) 4 ℑC, ℑ9
C, ℑ
9, ℑF , ℑP [0, 8] \ 5 — ( 19
6 , 19
24)
(3, 9, 3, 5
3) 5 ℑC, ℑ9
C, ℑ
9, ℑF , ℑP [0, 8] \ 5 — ( 13
3 , 13
15)
(5, 9, 3, 5
3) 5 ℑC, ℑ9
C, ℑ
9, ℑF , ℑP [0, 7] \ {2, 5} — ( 23
6 , 23
30)
(5, 3, 9, 3, 5
3) 6 ℑC, ℑ9
C, ℑ
9, ℑF , ℑP [0, 8] \ 5 — ( 11
2 , 11
12)
(5
3, 3, 9, 3, 5
3) 6 ℑC, ℑ9
C, ℑ
9, ℑF , ℑP [0, 9] \ 2 — ( 17
3 , 17
18)
(9, 5
3, 3) 4 ℑC, ℑ9
C, ℑ
9, ℑF , ℑP [0, 8] \ 5 — (3, 3
4)
(3, 9, 5
3, 3) 5 ℑC, ℑ9
C, ℑ
9, ℑF , ℑP [0, 9] \ 2 — ( 25
6 , 5
6)
(5
3, 3, 9, 5, 9, 3, 5
3) 4 ℑC, ℑ9
C, ℑ
9, ℑF , ℑP [0, 14] — ( 20
3 , 5
6)

the electronic journal of combinatorics 20(2) (2013), #P7 43
