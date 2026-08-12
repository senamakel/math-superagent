<!-- source: https://discovery.ucl.ac.uk/id/eprint/10112658/1/CyclesPaper.pdf | converted from PDF -->

Graphs without proper subgraphs of minimum
degree 3 and short cycles

Lothar Narins∗, Alexey Pokrovskiy†, Tibor Szab´o ‡

Department of Mathematics,

Freie Universit¨at,

Berlin, Germany.

February 5, 2015

Abstract

We study graphs on n vertices which have 2n − 2 edges and no proper induced
subgraphs of minimum degree 3. Erd˝os, Faudree, Gy´arf´as, and Schelp conjectured
that such graphs always have cycles of lengths 3, 4, 5, . . . , C(n) for some function
C(n) tending to inﬁnity. We disprove this conjecture, resolve a related problem
about leaf-to-leaf path lengths in trees, and characterize graphs with n vertices and
2n − 2 edges, containing no proper subgraph of minimum degree 3.

1 Introduction

A simple exercise in graph theory is to show that every graph G with n vertices and at
least 2n − 2 edges must have an induced subgraph with minimum degree 3. Moreover,
this statement is best possible: there are several constructions with 2n − 3 edges which
do not have this property. So every graph with n vertices and 2n − 2 edges must contain
an induced subgraph with minimum degree 3, however this subgraph might be the whole
graph. A subgraph H of G is called proper if H ̸= G. See Figure 1 for two examples of
graphs with 2|G| − 2 edges but no proper induced subgraphs of minimum degree 3. The
ﬁrst of these, has an even stronger property—it has no proper induced or non-induced
subgraphs with minimum degree 3. On the other hand, the second example has a proper

∗Research supported by the Research Training Group Methods for Discrete Structures and the Berlin
Mathematical School.
†Research supported by the Research Training Group Methods for Discrete Structures.
‡Research partially supported by DFG within the Research Training Group Methods for Discrete Struc-
tures.
 1

non-induced subgraph with minimum degree 3 formed by removing the edge between the
two vertices of degree 4.

Figure 1: Two examples of graphs on 6 vertices with 10 edges and no proper induced
subgraphs with minimum degree 3.

In this paper we will study graphs with n vertices and 2n − 2 edges which have no
proper induced subgraphs with minimum degree 3. Following Bollob´as and Brightwell [2]
we call such graphs degree 3-critical. It is easy to see that graphs with n vertices and at
least 2n − 1 edges contain a proper degree 3-critical subgraph. Erd˝os (cf [4]) conjectured
that they should contain a degree 3-critical subgraph not only on at most n − 1, but on at
most (1 − ϵ)n vertices, for some constant ϵ > 0. Degree 3-critical graphs are closely related
to several other interesting classes of graphs. For example, they are trivially equivalent
to graphs of minimum degree 3 all of whose subgraphs are 2-degenerate (where a graph
is deﬁned to be 2-degenerate if it has no subgraph of minimum degree 3). Also notice
that degree 3-critical graphs certainly have no proper subgraphs H with 2|H| − 2 edges.
Graphs with 2n − 2 edges and no proper subgraphs H with 2|H| − 2 edges have a number
of interesting properties. They are rigidity circuits: by a theorem of Laman [5], removing
any edge from such a graph produces a graph H which is minimally rigid in the plane, i.e.,
any embedding of it into the plane where the vertices are substituted by joints and the
edges by rods produces a rigid structure, but no proper subgraph of H has this property.
Furthermore, by a special case of a theorem of Nash-Williams [7] these graphs are exactly
the ones that are the union of two disjoint spanning trees and Lehman’s Theorem [6]
characterizes them as the minimal graphs to win the so-called connectivity game on. That
is, with two players alternately occupying the edges of G, the player playing second is able
to occupy a spanning tree.
The study of degree 3-critical graphs was initiated by Erd˝os, Faudree, Gy´arf´as, and
Schelp [3], where they investigated the possible cycle lengths. They showed that degree
3-critical graphs on n ≥ 5 vertices always contain a cycle of length 3, 4, and 5, as well as a
cycle of length at least ⌊log2 n⌋, but not necessarily of length more than √
n. Bollob´as and
Brightwell [2] resolved asymptotically the question of how short the longest cycle length in
degree 3-critical graphs can be. They showed that every degree 3-critical graph contains a
cycle of length at least 4 log2 n − o(log n) and constructed degree 3-critical graphs with no
cycles of length more than 4 log2 n + O(1). Erd˝os, et al. [3] made the following conjecture
about possible cycle lengths in degree 3-graphs.

2

Conjecture 1.1 (Erd˝os, Faudree, Gy´arf´as, and Schelp, [3]). There is an increasing func-
tion C(n) such that the following holds such that every degree 3-critical graph on n vertices
contains all cycles of lengths 3, 4, 5, 6, . . . , C(n).

A historical remark must be made here. The exact phrasing of Conjecture 1.1 in [3] is
not quite what is stated above. In [3] ﬁrst a class of graphs, G
∗(n, m), is deﬁned as “the
set of graphs with n vertices, m edges, and with the property that no proper subgraph
has minimum degree 3.” Then Conjecture 1.1 is stated as “If G ∈ G
∗(n, 2n − 2), then G
contains all cycles of length at most k where k tends to inﬁnity.” Notice that the word
“induced” is not present in the original formulation. However a careful reading of [3] shows
that in that paper “proper subgraph” implicitly must mean “proper induced subgraph”.
Indeed many of the constructions given in [3] (such as Examples 1, 2, 3, 5, and 6 on pages
197-201) of graphs which have “no proper subgraphs of minimum degree 3” actually do
have proper non-induced subgraphs with minimum degree 3. In addition, one can check
that all the results and proofs given in [3] concerning graphs with “no proper subgraphs of
minimum degree 3” hold also for graphs with “no proper induced subgraphs of minimum
degree 3”. Therefore, it is plausible to assume that the word “induced” should be present in
the statement of Conjecture 1.1. This also coincides with the interpretation of the concept
in the paper of Bollob´as and Brightwell [2].
Consequently throughout most of this paper we will study Conjecture 1.1 as it is stated
above. However, for the sake of completeness, in Section 4 we will diverge and consider the
special case of Conjecture 1.1 when G contains neither induced nor non-induced subgraphs
with minimum degree 3.
The main result of this paper is a disproof of Conjecture 1.1. We prove the following.

Theorem 1.2. There is an inﬁnite sequence of degree 3-critical graphs (Gn)
∞
n=1 which do
not contain a cycle of length 23.

In the process of proving this theorem, we will naturally arrive to a question of indepen-
dent interest, concerning the various leaf-leaf path lengths (i.e., the lengths of paths going
between two leaves) that must occur in a tree. Obviously, if T is just a path, then T only
has a single leaf-leaf path. However if T has no degree 2 vertices, then one would expect
T to have many diﬀerent leaf-leaf path lengths. Of particular relevance to Conjecture 1.1
will be even 1-3 trees. A tree is called even if all of its leaves are in the same class of the
tree’s unique bipartition and a tree is called a 1-3-tree if every vertex has degree 1 or 3. On
our way towards the proof of Theorem 1.2 we determine the smallest even number which
does not occur as a leaf-leaf path in every even 1-3-tree.

Theorem 1.3. (i) There is an integer N0 such that every even 1-3 tree T with |T | ≥ N0
contains leaf-leaf paths of lengths 0, 2, 4, . . . , 18.

(ii) There is an inﬁnite family of even 1-3 trees (Tn)
∞
n=1, such that Tn contains no leaf-leaf
path of length 20.
 3

Part (ii) of Theorem 1.3 will be used to construct our counterexample to Conjecture 1.1,
while part (i) shows that our method, as is, can not deliver a stronger counterexample.
Hence it would be interesting to determine the shortest cycle length which is not present
in every suﬃciently large degree 3-critical graph. Theorem 1.2 shows that this number is
at most 23, while Erd˝os et al. [3] showed that it is at least 6. They also mention that their
methods could be extended to work for 7. In Section 5 we verify their statement, by giving
a short proof that every degree 3-critical graph must contain C6.
Finally, we revisit Conjecture 1.1 with the word “induced” removed from the deﬁnition
of degree 3-critical. We characterize all n-vertex graph with 2n − 2 edges and no proper
(not necessarily induced) subgraph with minimum degree 3 and show that the conjecture
is true for them in a much stronger form.

Theorem 1.4. Let G be a graph with n vertices, 2n − 2 edges and no proper subgraph with
minimum degree 3. Then G is pancyclic, that is, it contains cycles of length i for every
i = 3, 4, 5, . . . , and n.

Theorem 1.4 will follow from a structure theorem which we shall prove about graphs
with n vertices, 2n − 2 edges and no proper (not necessarily induced) subgraphs with
minimum degree 3. It will turn out that there are only two particular families of graphs
satisfying these conditions. One of them is the family of wheels and the other is a family
of graphs obtained from a wheel by replacing one of its edges with a certain other graph.
The structure of this paper is as follows. In Section 2 we construct our counterexamples
to Conjecture 1.1 via proving part (ii) of Theorem 1.3 and Theorem 1.2. In Section 3 we
study necessary leaf-leaf path lengths in even 1-3 trees and prove part (i) Theorem 1.3. In
Section 4 we prove the weakening of Conjecture 1.1 when the word “induced” is removed
from the deﬁnition. In Section 5 we show that degree 3-critical graphs on at least 6 vertices
always contain a six-cycle. In Section 6 we make some concluding remarks and pose several
interesting open problems raised naturally by our results. Our notation follows mostly that
of [1].

2 Counterexample to Conjecture 1.1

The goal of this section is to prove Theorem 1.2. First we need some preliminary results
about 1-3 trees.
Given a tree T , deﬁne G(T ) to be the graph formed from T by adding two new vertices
x and y, the edge xy as well as every edge between {x, y} and the leaves of T . See Figure 2
for an example of a graph G(T ).
Notice that if T is a 1-3 tree then G(T ) is degree 3-critical. In the case when T is an
even 1-3 tree, the cycles of G(T ) have nice properties.

Lemma 2.1. Let T be an even 1-3-tree. Then the following hold:

(i) The graph G(T ) contains a cycle of length 2k + 1 ⇐⇒ T contains a leaf-leaf path
of length 2k − 2.
 4

x y
 T

Figure 2: The graph G(T ) for an even 1-3 tree T .

(ii) The graph G(T ) contains a cycle of length 2k ⇐⇒ T contains two vertex-disjoint
leaf-leaf paths P1 and P2 such that e(P1) + e(P2) = 2k − 4 or T contains a leaf-leaf
path of length 2k − 2.

Proof. For (i), let C be a (2k + 1)-cycle in G(T ). Notice that since T is an even tree,
G(T ) − xy is bipartite. So C must contain the edge xy and hence C − x − y must be a
leaf-leaf path of length 2k − 2 as required. For the converse, notice that any path P ⊆ T
of length ℓ between leaves u1 and u2 can be turned into a cycle of length ℓ + 3 by adding
the vertices x and y as well as the edges u1x, xy, yu2 of G(T ).
For (ii), let C now be a 2k-cycle in G(T ). If |C ∩ {x, y}| = 1 then C − x − y is a leaf-leaf
path in T of length 2k − 2. Now suppose that both x, y ∈ V (C). Notice that since T is
even, all leaf-leaf paths in T have even length. Therefore, all cycles containing the edge xy
in G(T ) must have odd length, and hence C does not contain xy. Thus C − x − y consists
of two vertex-disjoint leaf-leaf paths P1, P2 ⊆ T such that their lengths sum to 2k − 4, as
required. For the converse, ﬁrst notice that any leaf-leaf path P ⊆ T of length ℓ can be
turned into a cycle of length ℓ + 2 in G(T ) by adding the vertex x and the edges between
the endpoints of P and x. Also, any two vertex-disjoint leaf-leaf paths P1 ⊆ T of length
ℓ1 with endpoints u1, w1 and P2 ⊆ T of length ℓ2 with endpoints u2 and w2 can be turned
into a cycle of length ℓ1 + ℓ2 + 4 in G(T ) by adding the vertices x and y, and the edges
u1x, xu2, w2y, and yw1 of G(T ). ■

We say that a rooted binary tree T is perfect if all non-leaf vertices have two children
and all root-leaf paths have the same length d (or, alternatively if |V (T )| = 2
d+1 − 1 where
d is the depth of T ). Given a sequence of positive integers x1, . . . , xn, we deﬁne a tree
T (x1 . . . xn) as follows. First consider a path on n vertices with vertex sequence v1, . . . , vn.
For each i satisfying 2 ≤ i ≤ n − 1, add a perfect rooted binary tree Ti of depth xi − 1 with
root vertex ui. For i = 1 and n add two perfect rooted binary trees each: trees T (1)
1 and
T (1)
1 of depths x1 − 1 with root vertices u
(1)
1 and u
(2)
1 , respectively and trees T (1)
n and T (1)
n of
depths xn −1 with root vertices u(1)
n and u(2)
n , respectively. Finally, for each i, 2 ≤ i ≤ n−1,

5

v1 v2 v3 v4 v5

Figure 3: The 1-3 tree T (2, 3, 2, 3, 2).

we add the edges viui, as well as the edges v1u
(1)
1 , v1u(2)
1 , vnu
(1)
n , and vnu
(2)
n . See Figure 3
for an example of a tree T (x1, . . . , xn).
Notice that for any sequence x1, . . . , xn of positive integers, the tree T (x1 . . . xn) is a 1-3
tree. We will mainly be concerned with odd-even sequences, that is, sequences for which
xi ≡ i (mod 2) for all i (that is, xi is even ⇐⇒ i is even). It turns out that for odd-even
sequences the leaf-leaf path length of the tree T (x1 . . . xn) are easy to characterize.

Lemma 2.2. Let x1, . . . , xn be an odd-even sequence. Then we have the following:

(i) The tree T (x1 . . . xn) contains no leaf-leaf path of odd length. In particular, T (x1, . . . , xn)
is an even tree.

(ii) For every integer m, 0 ≤ m < max
n
i=1 xi, the tree T (x1 . . . xn) contains a leaf-leaf
path of length 2m.

(iii) For m = max
n
i=1 xi, the tree T (x1 . . . xn) contains a leaf-leaf path of length 2m if and
only if either max{x1, xn} = max
n
i=1 xi or there are two distinct integers i and j such
that xi + xj + |i − j| = 2m.

(iv) For every m > max
n
i=1 xi, the tree T (x1 . . . xn) contains a leaf-leaf path of length 2m
if and only if there are two distinct integers i and j such that xi + xj + |i − j| = 2m.

Proof. Leaf-leaf paths of T (x1, . . . , xn) can be classiﬁed based on their intersection with
the path v1, . . . , vn. Note that this intersection is always a (potentially empty) path.
If the intersection is empty then the path is a leaf-leaf path of a perfect binary tree of
depth xi − 1 for some i, and hence its length is 2m for some m, 0 ≤ m < max
n
i=1 xi.
If the intersection is a single vertex, then this vertex must be either v1 or vn. Then
the path is a leaf-leaf path going through the root in one of the perfect binary trees on
V (T (1)
1 ) ∪ V (T (2)
1 ) ∪ {v1} and V (T (1)
n ) ∪ V (T (2)
n ) ∪ {vn} of depths x1 and xn, respectively,
and hence its length is 2x1 or 2xn, respectively.
If the intersection is a segment vi, . . . , vj for some 1 ≤ i < j ≤ n, then the path has
length xi + j − i + xj. This implies the “only if ” part of (iii) and (iv). Note also that all
these paths have even length (xi + j − i + xj is even because (x1, . . . , xn) is an odd-even
sequence), and so (i) holds.
For (ii) and the “if” part of (iii) and (iv) one must only note that a perfect tree of
depth d contains a leaf-leaf path of every even length 0, 2, . . . , 2d and hence all leaf-leaf
path-lengths given by the classiﬁcation can actually be realized. ■

6

We now produce a sequence of integers (xn)
∞
n=1 such that for every n, the tree T (x1 . . . xn)
will not have leaf-leaf paths of length 20.

2.1 k-avoiding sequences

We will be concerned with two-sided sequences (ai)i∈Z of positive integers. Again, we say
that such a sequence is an odd-even sequence if ai ≡ i (mod 2) for all i ∈ Z.

Deﬁnition 2.3. Let k be a positive even integer. A two-sided sequence (xi)i∈Z of positive
integers is called k-avoiding if ai ≤ k/2 for all i ∈ Z and if for every i, j ∈ Z, i ̸= j, we
have ai + aj + |i − j| ̸= k.

In order to check if an odd-even sequence (ai)i∈Z with ai ≤ k/2 for all i ∈ Z is k-avoiding,
consider the graph {(i, ai) : i ∈ Z} of the sequence. Call a point (x, y) ∈ Z × [1, k/2] in
conﬂict with another point (z, w) ∈ Z × [1, k/2], (z, w) ̸= (x, y), if y + w + |x − z| = k.
Notice that the points (x, y) in conﬂict with a ﬁxed point (c, d) lie on the two diagonal
lines y = −x + (k + c − d) and y = x + (k − c − d). Since being in conﬂict is a symmetric
relation we can say that we blame a conﬂict on the point with lower ﬁrst coordinate (the
ﬁrst coordinates of points in conﬂict cannot be equal). Then the points (x, y) ∈ Z×[1, k/2],
whose conﬂicts with (c, d) are blamed on (c, d) lie on the single line y = −x + (k + c − d).
Indeed, the ﬁrst coordinates of a point (x, y) on the other diagonal line is x = y −k +c+d ≤
k/2 − k + c + k/2 at most c, hence these conﬂicts are not blamed on (c, d). We deﬁne the
fault line of the point (c, d) to be the line y = −x + (k + c − d). From the above discussion
we obtain the following proposition.

Proposition 2.4. A sequence (ai)i∈Z is k-avoiding if, and only if, for any two distinct
indices i and j the point (i, ai) is not on the fault line of (j, aj).

It is useful to note that all the points on the line y = x + b have the same fault line
y = −x + b + k.

Theorem 2.5. There is a 20-avoiding odd-even sequence.

Proof. Let (ai)i∈Z be the periodic sequence of period 24 consisting of repetitions of

. . . , 1, 2, 1, 4, 3, 2, 7, 6, 5, 6, 7, 2, 3, 4, 1, 2, 1, 8, 9, 6, 5, 6, 9, 8, . . . .

We claim (ai)i∈Z is a 20-avoiding odd-even sequence. It is clearly an odd-even sequence,
and ai ≤ 10 = 20/2 for all i ∈ Z. We prove that it is 20-avoiding by showing that in the
graph of this sequence, no point lies on the fault line of another point. Then Proposition 2.4
implies the theorem.
Figure 4 is a snapshot of two periods of the graph. The points on the graph are black
circles, and the fault lines are drawn in red. Note that points on a line ℓ parallel to the
line “x = y” have the same fault line, and that this fault line crosses ℓ when the second
coordinate is 10.
From the picture we see that no point of the sequence lies on a fault line of another
point, implying that (ai)i∈Z is indeed 20-avoiding. ■

7

1

2

3

4

5

6

7

8

9

10
 5 10 15 20 25 30 35 40 45

Figure 4: A snapshot of the graph of a periodic 20-avoiding odd-even sequence.

We are now ready to prove part (ii) of Theorem 1.3 and Theorem 1.2.

Proof of part (ii) of Theorem 1.3. Let x1, . . . , xn be the ﬁrst n terms (starting at 1) of the
20-avoiding sequence produced by Theorem 2.5. The tree Tn = T (x1 . . . xn) is a 1-3-tree
for any sequence (x1, . . . , xn) by construction. Since (x1, . . . , xn) is an odd-even sequence,
Tn is also an even tree by part (i) of Lemma 2.2. The tree Tn contains no leaf-leaf paths
of length 20, since 20 > 2 · max xi = 18 and part (iv) of Lemma 2.2 tells us that a leaf-leaf
path of length 20 exists only if there are distinct i and j such that xi + xj + |i − j| = 20,
which is not case since x1, . . . , xn is 20-avoiding. ■

Proof of Theorem 1.2. We let Gn = G(Tn) be the graph constructed from the tree Tn given
by part (ii) of Theorem 1.3. Since Tn is a 1-3-tree, the graph Gn is degree 3-critical, as
required. Since Tn is an even 1-3-tree, we can use part (i) of Lemma 2.1 and the fact that
Tn does not contain a leaf-leaf path of length 20 to conclude that Gn contains no cycle of
length 23. ■

3 Possible leaf-leaf path lengths in even 1-3 trees

In this section we prove part (i) of Theorem 1.3. We ﬁrst need a lemma about possible
lengths of leaf-leaf paths in binary trees which have no short root-leaf paths.

Lemma 3.1. Let T be an even rooted binary tree and let m be the length of its shortest
root-leaf path. Then T contains leaf-leaf paths of lengths 0, 2, 4, . . . , 2m.

Proof. The proof is by induction on |V (T )|. The statement is certainly true for |V (T )| = 1.
Let now |V (T )| > 1 and let x and y be the children of the root r.
Suppose ﬁrst that in one of the subtrees Tx and Ty ⊆ T , rooted at x and y, respectively,
the shortest root-leaf path is of length m as well. In this case we can apply induction to
this subtree and ﬁnd in it leaf-leaf paths of all length 0, 2, . . . , 2m. The leaf-leaf path of
the subtree are of course leaf-leaf paths of T , so we are done in this case.
Otherwise, the length of the shortest root-leaf path of both subtrees Tx and Ty is m − 1
(the subtrees cannot contain a shorter root-leaf path, because T itself does not contain a
root-leaf path shorter than m). Then by induction there are leaf-leaf paths of all lengths

8

0, 2, . . . , 2m − 2 in both of these subtrees and hence also in T . To construct a leaf-leaf path
of length 2m in T let Px be a path between x and a leaf of T of length m − 1, and Py be
a path between y and a leaf of T of length m − 1. Then the path Px + r + Py formed by
joining Px and Py to r using the edges rx and ry is a leaf-leaf path in T of length 2m. ■

The following proposition shows that ﬁnding which leaf-leaf path lengths always occur
in suﬃciently large trees is equivalent to ﬁnding the k for which k-avoiding sequences exist.

Proposition 3.2. Let m be a positive integer. The following are equivalent.

(i) There is an integer N0(m) such that every even 1-3-tree of order at least N0(m)
contains a leaf-leaf path of length 2m.

(ii) There exists no 2m-avoiding odd-even sequence (xn)n∈Z.

Proof. Let us assume ﬁrst that (i) holds with integer N0(m) = N0. Let (xn)
∞
n=1 be an
arbitrary odd-even sequence such that max
n
i=1 xi ≤ m. Notice that since xi is even if and
only if i is even, there are inﬁnitely many indices a for which xa < max
n
i=1 xi. Therefore
we can choose two indices a and b such that a − b ≥ N0 and xa, xb < m. Then by parts
(iii) and (iv) of Lemma 2.2, the tree T (xa . . . xb) has a leaf-leaf path of length 2m if and
only if there are two distinct indices i and j such that xi + xj + |i − j| = 2m holds. On
the other hand notice that by part (i) of Lemma 2.2, T (xa . . . xb) is an even 1-3 tree and
hence, since its order is at least N0, does have a leaf-leaf path of length 2m. That is, there
do exist indices i ̸= j such that xi + xj + |i − j| = 2m holds, implying that (xn)
∞
n=1 is not
2m-avoiding.
Now assume that (ii) holds. Let us deﬁne N0(m) = N0 = 3
2 · 2
N1/2 − 1, where N1 =
m
2m + 2m. Let T be an arbitrary even 1-3 tree of order at least N0. We will show that T
contains a leaf-leaf path of length 2m. Since T is a tree of maximum degree at most 3 on
N0 vertices it must contain a path v1, v2, . . . , vN1 with N1 vertices. Let Ti be the subtree
of T consisting of the connected component of T − vi+1 − vi−1 containing vi and let xi be
the length of the shortest path from vi to a leaf of Ti. Note that (xi)
N1
i=1 is an odd-even
sequence, because T is an even tree.
Suppose ﬁrst that we have m < max
N1
i=1 xi. Choose an index i such that xi > m holds
and let T ′ = Ti − vi. Then T ′ is a binary tree rooted at the neighbour of vi, with no
root-leaf paths shorter than m, so Lemma 3.1 gives us a leaf-leaf path of length 2m.
Suppose now that we have m ≥ max
N1
i=1 xi. Since N1 > m
2m + 2m − 1, the Pi-
geonhole Principle implies that there must be indices a < b such that xa = xb, xa+1 =
xb+1, . . . , xa+2m−1 = xb+2m−1 all hold. Consider now the inﬁnite periodic sequence

. . . , xa, xa+1, . . . , xb−1, xa, xa+1, . . . , xb−1, xa, . . . ,

denoted by (yi)i∈Z. This is an odd-even sequence as the sequence (xi)
N1
i=1 was odd-even. By
our assumption (yi)i∈Z is not 2m-avoiding. But m ≥ max
n
i=1 xi = max
n
i=1 yi, so there must
be indices i ̸= j such that yi + yj + |i − j| = 2m. Since the sequence is positive we must
have |i − j| < 2m and by periodicity we can assume that a ≤ i < j ≤ b + 2m − 1. The way

9

we chose a and b ensures that xi = yi for every i between a and b + 2m − 1, so we also have
xi + xj + |i − j| = 2m. We can now ﬁnd a leaf-leaf path in T of length 2m = xi + xj + |i − j|
by concatenating a shortest path from vi to a leaf of Ti, the path between vi and vj and a
shortest path from vj to a leaf of Tj. ■

We now proceed to prove part (i) of Theorem 1.3. We do this by showing that part (ii)
of Proposition 3.2 holds for m ≤ 9.

Theorem 3.3. There is no 18-avoiding odd-even sequence.

Proof. Consider an odd-even sequence (ai)i∈Z with ai ≤ 9 for all i ∈ Z. Assume that it
is 18-avoiding. As in the proof of Theorem 2.5, we will consider the graph of (ai)i∈Z and
consider fault lines. In this case, the fault line of a point (c, d) is the line y = −x+(18+c−d).
Since (ai)i∈Z is 18-avoiding, Proposition 2.4 implies that no point of the graph lies on the
fault line of another point of the graph. Notice however, that a point of the form (x, 9),
which by deﬁnition lies on its own fault line, is not itself a barrier to a sequence being
18-avoiding.
We start with some lemmas about conﬁgurations of fault lines that lead to contradic-
tions. We will actually deal with a slight generalization of fault lines, which we call excluded
lines. An excluded line is deﬁned to be any line of the form y = −x + b with b even, that
does not contain a point in the graph of (ai)i∈Z, except possibly the point with second
coordinate 9. Since (ai)i∈Z is an odd-even sequence, for any point (i, ai) in the graph of
the sequence, the integer 18 + i − ai is even. Hence every fault line of the sequence is also
an excluded line.
In the following discussion lines of slope −1 whose y-intercepts diﬀer by exactly 2 are
called consecutive. We start with a trivial observation.

Lemma 3.4. There cannot be four consecutive excluded lines for (ai)i∈Z.

Proof. If there were four excluded lines y = −x + b, y = −x + b + 2, y = −x + b + 4, and
y = −x + b + 6, where b is even, then all of the points with even y-coordinate at most 8 on
the line x = b − 2 are on one of these lines. Hence (b − 2, ab−2) would be on an excluded
line, a contradiction.
 1

2

3

4

5

6

7

8

9
 b

Figure 5: Four consecutive excluded lines and the contradiction they give.
 ■

This easily leads to the next lemma.
 10

Lemma 3.5. There cannot be three consecutive excluded lines for (ai)i∈Z.

Proof. If there were three consecutive excluded lines y = −x + b, y = −x + b + 2, and
y = −x + b + 4, where b is even, then ab−4 must be equal to 2 as all the other even values at
most 8 would put (b − 4, ab−4) on one of the three lines. Similarly, we must have ab−2 = 8,
and hence we have fault lines y = −x + b + 8 and y = −x + b + 12. This forces ab−1 = 7,
giving also the fault line y = −x + b + 10. Now ab−3 can only be 1 or 9 to avoid the original
three fault lines, but it clearly cannot be 9, since that would put (b − 2, 8) on its fault line.
But if ab−3 = 1, then its fault line is y = −x + b + 14, and there would be 4 consecutive
fault lines y = −x + b + {8, 10, 12, 14}, contradicting Lemma 3.4.

1

2

3

4

5

6

7

8

9
 b

Figure 6: Three consecutive excluded lines and the contradiction they give.
 ■

A few more lemmas of this sort will be useful for the proof.

Lemma 3.6. There cannot be three excluded lines of the form y = −x + b, y = −x + b + 2,
and y = −x + b + 6 (with b even).

Proof. If this were the case, then this would force ab−2 = 6, which results in the fault
line y = −x + b + 10. If ab−1 = 9, then there would be three consecutive excluded lines
y = −x + b + {6, 8, 10}, which would contradict Lemma 3.5. This forces ab−1 = 5, which
results in the fault line y = −x + b + 12. Similarly, in order to avoid a third consecutive
fault line y = −x + b + 14, we must have ab+2 = 2 and ab+5 = 3, resulting in the fault lines
y = −x + b + 18 and y = −x + b + 20, respectively. This leaves us with no valid choices
for ab+6, since a value of 2 would create a third consecutive fault line y = −x + b + 22, a
value of 8 would create a third consecutive fault line y = −x + b + 16, and a value of 4 or 6
would put (b + 6, ab+6) on the fault line of a previous point. Therefore, this conﬁguration
cannot occur.
 1

2

3

4

5

6

7

8

9
 b
 11

Figure 7: A conﬁguration of three excluded lines and the contradiction they give.
 ■

Lemma 3.7. There cannot be three excluded lines of the form y = −x + b, y = −x + b + 4,
and y = −x + b + 6 (with b even).

Proof. If this were the case, then this would force ab−2 = 4, which results in the fault
line y = −x + b + 12. If ab−1 = 9, there would be three consecutive excluded lines
y = −x + b + {4, 6, 8}, contradicting Lemma 3.5. So we must have ab−1 = 3, resulting in
the fault line y = −x+b+14 (the other values of ab−1 would put (b−1, ab−1) on an excluded
line). If ab = 8, then we would have the conﬁguration of fault lines y = −x + b + {4, 6, 10}
forbidden by Lemma 3.6, so we must have ab = 2, resulting in the fault line y = −x+b+16.
But then we have the three consecutive fault lines y = −x + b + {12, 14, 16}, also a
contradiction.
 1

2

3

4

5

6

7

8

9
 b

Figure 8: A conﬁguration of three excluded lines and the contradiction they give.
 ■

All previous lemmas pave way for our ﬁnal technical lemma:

Lemma 3.8. There cannot be 2 consecutive excluded lines for (ai)i∈Z.

Proof. Suppose there were two consecutive excluded lines y = −x + b and y = −x + b + 2
for some even b. Consider the possible values for ab−8. It cannot be 8, since this is on the
excluded line y = −x + b. It cannot be 6, as this this would create a third consecutive
excluded line y = −x + b + 4. It also cannot be 4, because this would create the fault line
y = −x + b + 6, contradicting Lemma 3.6. Thus, we must have ab−8 = 2, which means we
have the fault line y = −x + b + 8. We also must have ab−4 = 2, since values 4 or 6 would
put a point of the graph on one of the excluded lines, and value 8 would yield the fault line
y = −x+b+6, contradicting Lemma 3.6. Thus, we also have the fault line y = −x+b+12.

1

2

3

4

5

6

7

8

9
 b

12

Figure 9: What two consecutive excluded lines can be reasoned to imply.

Now consider ab+1. It cannot be 1 or 7, since these would put a point of the graph on an
excluded line. It cannot be 9, otherwise it would create the fault line y = −x+b+10, and we
would have three consecutive fault lines y = −x + b + {8, 10, 12} contradicting Lemma 3.5.
It cannot be 5, for if it were, there would be the three fault lines y = −x + b + {8, 12, 14} in
contradiction with Lemma 3.7. Hence we have ab+1 = 3 and the fault line y = −x + b + 16.
Similarly, we must have ab+3 = 1, since 5 or 9 put it on a fault line, 7 would create three
consecutive fault lines y = −x + b + {12, 14, 16}, and 3 would create the conﬁguration of
fault lines y = −x + b + {12, 16, 18} forbidden by Lemma 3.7. Therefore, there is also the
fault line y = −x + b + 20. But now every possible value for ab+7 leads to a contradiction.
If it is 1, 5, or 9, then it is on a fault line. If it is 3 or 7, it creates a fault line resulting in
a conﬁguration forbidden by Lemmas 3.7 and 3.5, respectively. Therefore, we cannot have
two consecutive excluded lines.

1

2

3

4

5

6

7

8

9
 b

Figure 10: The contradiction reached from two consecutive fault or excluded lines.
 ■

Excluded lines by deﬁnition have slope −1. To ﬁnish the proof pf Theorem 3.3 we
extend the notion of excluded line to those lines y = x + b with even b, which do not
contain any point of the graph except possibly the point (9 − b, 9). We call these the
orthogonal excluded lines of the sequence (ai)i∈Z. The conclusion of Lemma 3.8 also holds
for orthogonal extended lines: there cannot be two consecutive ones. Indeed, y = x + b
is an orthogonal extended line of the 18-avoiding odd-even sequence (ai)i∈Z if and only if
y = −x − b is an extended line of the 18-avoiding odd-even sequence (a−i)i∈Z, so we can
apply Lemma 3.8 for (a−i)i∈Z.
Another useful observation is that the line y = −x + b is the fault line of exactly those
points that are on the line y = x + 18 − b. Hence if y = −x + b contains a point of the
graph (say, it is not excluded), then y = x + 18 − b must be an orthogonal excluded line.
Using this observation for (a−i)i∈Z one can also obtain that if the orthogonal line y = x + b
contains a point of the graph of (ai)i∈Z (say, it is not excluded), then y = −x − 18 − b must
be an excluded line for (ai)i∈Z.
Let us now assume that there exists an 18-avoiding sequence (ai)i∈Z and let y = −x + b
be a fault line of it for some even b. By the above we can make a sequence of conclusions.
The lines y = −x + b ± 2 are not excluded by Lemma 3.8. Then y = x + 18 − b ± 2 must
be orthogonal excluded lines. Then y = x + 18 − b ± 4 are not excluded by the adaptation

13

of Lemma 3.8 for orthogonal lines. Then y = −x + b ± 4 must be excluded lines. Again
by Lemma 3.8 the lines y = −x + b ± 6 are not excluded and hence the orthogonal lines
y = x + 18 − b ± 6 must be excluded. This implies that y = x + 18 − b ± 8 are not orthogonal
excluded lines by the adaptation of Lemma 3.8 and y = −x + b ± 8 are excluded lines.
What can now be the value of ab−9? It must be odd as b is even and (ai)i∈Z is an
odd-even sequence. The line y = x + 18 − b − 2 being excluded shows it cannot be 7,
y = −x + b − 4 being excluded shows that it cannot 5, y = x + 18 − b − 6 being excluded
shows it cannot be 3, y = x+b−8 being excluded shows it cannot be 1. The line y = −x+b
is a fault line of (ai)i∈Z so in principle (ab−9, 9) could be on it. However then, the orthogonal
line x + 18 − b should also be excluded, meaning that together with y = x + 18 − b ± 2
they would represent three consecutive orthogonal excluded lines, a contradiction. ■

To complete the proof of Theorem 1.3 we need the following little proposition.

Proposition 3.9. Let k be a positive even integer. If there is a k-avoiding odd-even
sequence, then there is a (k + 2ℓ)-avoiding odd-even sequence for every ℓ ∈ Z≥0.

Proof. If (ai)i∈Z is a k-avoiding odd-even sequence, then deﬁne the sequence (bi)i∈Z by

bi = ai+ℓ + ℓ

for all i ∈ Z. We claim that (bi)i∈Z is a (k + 2ℓ)-avoiding odd-even sequence.
It is clearly an odd-even sequence as bi = ai+ℓ + ℓ ≡ i + 2ℓ ≡ i (mod 2) for all i ∈ Z.
Also, bi = ai+ℓ + ℓ ≤ k/2 + ℓ = (k + 2ℓ)/2 for all i ∈ Z. Suppose there were i, j ∈ Z with
i < j such that bi +bj −i+j = k +2ℓ. Then we would have ai+ℓ +ℓ+aj+ℓ +ℓ−i+j = k +2ℓ.
But this implies ai+ℓ + aj+ℓ − (i + ℓ) + (j + ℓ) = k, which contradicts the fact that (ai)i∈Z
is k-avoiding. ■

Proof of Theorem 1.3 (i). Let m ≤ 9 be a positive integer. We claim that there is no
2m-avoiding odd-even sequence. Indeed, otherwise our previous proposition implied that
there is also an 18-avoiding odd-even sequence, which contradicts Theorem 3.3. Now by
Proposition 3.2, there is an integer N0(m) such that every even 1-3 tree of order at least
N0(m) contains a leaf-leaf path of length 2m, which is exactly the statement of part (i) of
Theorem 1.3. ■

4 Characterization of graphs with no subgraphs of
minimum degree 3

Let G denote the family of graphs G with 2|G| − 2 edges and no proper (not necessarily
induced) subgraphs with minimum degree 3. In this section we characterize the members
of G and deduce Theorem 1.4 as a corollary.
A wheel Wn is an n-vertex graph with vertices c, and w1, . . . , wn−1 with edges cwi and
wiwi+1 (mod n−1) for i = 1, . . . , n − 1. The vertex c will be called the centre of the wheel

14

y
 v1

v2

v3

v4

v5
 x

Figure 11: The graph H7.

Figure 12: Graphs on 11 vertices with 20 edges and no proper (not necessarily induced)
subgraphs with minimum degree 3.

and the vertices w1, . . . , wn−1 will be called the outside vertices of Wn. For n ≥ 4, Let
Hn be the graph on n vertices called x, y, and v1, . . . , vn−2 formed by the edges vivi+1 for
i ∈ {1, . . . , n−3}, xvi for i ∈ {1, . . . , n−2}, yv1, and yvn−2. We call x and y the connectors
of Hn and v1, . . . , vn−2 the internal vertices of Hn. Note that the roles of the connectors
are not symmetric; the letter y will always denote one with degree two. See Figure 11 for
a picture of the graph H7.
The next theorem shows that the graphs in G must have a very speciﬁc structure. See
Figure 12 for examples of its members on 11 vertices.

Theorem 4.1. The family G consists of all wheels and those graphs that are formed, for
some i and j, from a copy of Hi with connectors x and y and a copy of Hj with connectors
x′ and y′ by letting x = x′ and y = y′ or by letting x = y′ and y = x′.

For the proof we ﬁrst recall some basic properties of graphs with no induced subgraphs
of minimum degree 3.
Recall from the introduction that the following lemma is easy to prove by induction.

Lemma 4.2. Every graph on n ≥ 2 vertices with at least 2n − 2 edges contains an induced
subgraph with minimum degree 3.

For degree 3-critical graphs, the induced subgraph of minimum degree 3 (guaranteed
by the previous lemma) must be the whole G. For these graphs, Erd˝os et al. [3] presented
a special ordering to the vertices. Given an ordering x1, . . . , xn of V (G) we let the forward
neighbourhood of xi, denoted N +(xi), be N +(xi) = N (xi) ∩ {xi+1, . . . , xn}. The forward

15

degree of xi is d+(xi) = |N +(xi)|. The following lemma is essentially from [3]. We prove
it here in a slightly stronger formulation. Notice that the lemma considers not just graphs
from G, but degree 3-critical graphs in general. We will make use of this in the next section.

Lemma 4.3. For every degree 3-critical graph G on n vertices there is an ordering x1, . . . , xn
of the vertices, such that the following hold.

(i) d+(x1) = 3.

(ii) For 2 ≤ i ≤ n − 2, d
+(xi) = 2.

(iii) d+(xn−1) = 1.

(iv) If furthermore n ≥ 7, then d(xn) ≥ 4.

Proof. We deﬁne xi recursively. Let x1 be a vertex of minimum degree in G. Suppose that
we have already deﬁned x1, x2, . . . , xi. Then we let xi+1 be a vertex of minimal degree in
G − {x1, · · · −, xi}.
For (i), notice that the average degree of G is less than 4, so d(x1) ≤ 3. To see that
d(x1) ≥ 3, notice that otherwise the graph G−x1 would have at least e(G)−2 = 2(n−1)−2
edges and Lemma 4.2 would imply the existence of an induced subgraph of G − x1 of
minimum degree 3, a contradiction to G being degree 3-critical. Hence d(x1) = 3.
For (ii), we proceed by induction to show that for all i, 1 ≤ i ≤ n − 2, we have
e(G − {x1, . . . , xi}) = 2(n − i) − 3. The case i = 1 follows from (i). Let i > 1 and assume
e(G − {x1, . . . , xi−1}) = 2(n − (i − 1)) − 3. First notice that degree 3-criticality of G implies
both d
+(xi) ≤ 2 and e(G − {x1, . . . , xi}) ≤ 2(n − i) − 3. Indeed, otherwise the minimum
degree of the induced subgraph G − {x1, . . . , xi−1} would be exactly 3 or G − {x1, . . . , xi}
would contain an induced subgraph of minimum degree 3 by Lemma 4.2. On the other
hand, e(G − {x1, . . . , xi}) = e(G − {x1, . . . , xi−1}) − d+(xi) ≥ 2(n − (i − 1)) − 3 − 2 by
induction, implying both e(G − {x1, . . . , xi}) = 2(n − i) − 3 and d
+(xi) = 2.
Part (iii) now follows from e(G − {x1, . . . , xn−2}) = 1.
For (iv), assume that n ≥ 7. Let x1, . . . , xn be the ordering of the vertices of G produced
by the above procedure. Notice that the graph G[{xn−5, xn−4, . . . , xn}] must contain a
vertex v of degree at least 4 in G[{xn−5, xn−4, . . . , xn}] (since it has 6 vertices and 9 edges
and contains a vertex of degree 2 (here we use that xn−5 ̸= x1). Since d(v) ≥ 4, v must be
one of xn−3, xn−2, xn−1, or xn. The graph G[{xn−3, . . . , xn}] has 4 vertices and 5 edges, and
so contains a vertex x′
n−3 ̸= v of degree 2 in G[{xn−3, . . . , xn}]. Let x′
n−2, x′
n−1 be the two
vertices in {xn−3, xn−2, xn−1, xn} \ {v, x′
n−3} in an arbitrary order. Since G[{x′
n−2, x
′
n−1, v}]
spans a triangle, the ordering of G given by x1, x2, . . . xn−5, xn−4, x
′
n−3, x
′
n−2, x
′
n−1, v satisﬁes
(i) – (iv). ■

Proof of Theorem 4.1. First we show that if G is a wheel or a graph formed from gluing Hi
and Hj together, then G is in G. If G has a subgraph H of minimum degree 3 and vertex
v ∈ V (H) with dG(v) = 3, then the three neighbours of v must all be in H. Hence the
connected components of the induced subgraph of G on its vertices of degree 3 must either

16

be fully contained in H or fully missing. Wheels have only one such component, and graphs
formed from gluing Hi and Hj together as in the theorem have two such components. Using
this, it is easy to check that these graphs have no proper subgraphs of minimum degree 3.
For the reverse direction let G be an n-vertex graph with 2n − 2 edges and no proper
(not necessarily induced) subgraphs with minimum degree 3. From Lemma 4.3, we have
that δ(G) ≥ 3. We formulate the property of G that will be most important for us.

Observation 4.4. The graph G does not have two adjacent vertices of degree ≥ 4.

Indeed, the removal of the edge between two vertices of degree 4 would create a proper
subgraph of G minimum degree 3, a contradiction.
If |G| ≤ 6, then it is easy to check (say by considering the ordering given in Lemma 4.3)
that G must be a wheel or the graph obtained by the gluing of two copies of H4. Therefore,
let us assume that we have |G| ≥ 7.
First we show that if G is not a wheel, then it contains a copy of Hm for some m ≥ 4
with a certain structure to its internal vertices.

Claim 4.5. Either G is a wheel or G has an induced subgraph Hm ⊆ G for some m ≥ 4,
such that none of the internal vertices of Hm have neighbours in G − V (Hm).

Proof. Consider the ordering x1, . . . , xn of the vertices of G as given by Lemma 4.3. Let k
be the smallest integer such that xn is adjacent to every vertex in {xk+1, . . . , xn−1}. Note
that k ∈ {0, 1, . . . n − 3}, since by part (ii) and (iii) of Lemma 4.3, xn−2 and xn−1 are
adjacent to xn. We will show that if k = 0 then G is a wheel and otherwise the subgraph
G[{xk, . . . , xn}] is the sort of copy of Hn−k+1 that we need, with connectors x = xn and
y = xk.
We plan to reconstruct G[{xℓ, . . . , xn}] from the trivial graph on {xn} by adding back
one-by-one the vertices xi for each i = n − 1, n − 2 . . . , ℓ (in reverse order), together with
their incident edges to {xi+1, . . . , xn}.
First we show by backward induction that the induced subgraph G[{xi, . . . , xn−1}] is a
path Ri for every i = max{k+1, 2}, . . . , n−2. Indeed, for every i = max{k+1, 2}, . . . , n−2
the vertex xi is adjacent to xn and by part (ii) of Lemma 4.3 to exactly one other vertex
xj in {xi+1, . . . , xn−1}. By part (iv) of Lemma 4.3 the degree of xn in G is at least 4 and
since xjxn ∈ E(G), Observation 4.4 implies that the degree of xj in G[{xi+1, . . . , xn−1}]
must be at most one. So xj is one of the endpoints of Ri, thus giving rise to a path Ri−1
that is induced on {xi, . . . , xn−1}.
Now we separate into two cases.
If k > 0, then we have that G[{xk+1, . . . , xn−1}] is a path Rk with all its vertices
adjacent to xn. Since xk is not adjacent to xn, both of its forward neighbours must be
in {xk+1, . . . , xn−1}. If any of these neighbours would be a vertex xj, k < j < n, with
degree at least 2 in G[{xk+1, . . . , xn−1}], then we get a contradiction from Observation 4.4
as xjxn ∈ E(G). Hence xk must be adjacent exactly to the two endpoints of the path Rk
and then G[{xk, . . . , xn}] is a copy of Hn−k+1 with connectors x = xn and y = xk as we
promised. Observe furthermore that there cannot be any additional edges between any

17

xi ∈ {xk+1, . . . , xn−1} and V (G) \ {xk, . . . , xn}, since otherwise the degree of xi in G would
be at least 4 providing a contradiction from Observation 4.4 as xixn ∈ E(G).
If k = 0, then G[{x2, . . . , xn−1}] is a path R2 with all its vertices adjacent to xn. Again,
none of the neighbours xj of x1 can be an internal vertex of R2, otherwise we obtained a
contradiction from Observation 4.4 since x1xn and xjxn are both edges of G. Recall that
x1 has three neighbours (part (i) of Lemma 4.3). These then must be the two endpoints
of R2 and xn, giving rise to a wheel with center xn. ■

Given a copy of Hm contained in G, we deﬁne G/Hm to be the graph formed out of G
by removing the internal vertices of Hm, and joining the connectors of Hm by an edge. It
turns out that if Hm has the structure produced by Claim 4.5, then the graph G/Hm ∈ G,
so we will be able to apply induction.

Claim 4.6. Suppose that graph G ∈ G has an induced subgraph Hm ⊆ G for some m, such
that none of the internal vertices of Hm have neighbours in G \ V (Hm). Then G/Hm ∈ G.

Proof. Let x and y be the connectors of Hm. By the assumptions of the lemma and the
deﬁnition of G/Hm, the only edges which were present in G and are not present in G/Hm
are the 2m − 3 edges of Hm. The only new edge in G/Hm is the edge xy. From the
deﬁnition of G/Hm, we have |G/Hm| = |G| − m + 2. Combining this with e(G) = 2|G| − 2,
we obtain e(G/Hm) = e(G) − 2m + 4 = 2|G| − 2m + 2 = 2|G/Hm| − 2.
We will show that for every proper subgraph K ⊊ G/Hm, we have δ(K) ≤ 2. If K does
not contain the edge xy, then K is also a proper subgraph of G, and then, since G ∈ G,
K must satisfy δ(K) ≤ 2. Suppose now that K does contain the edge xy. Let K ′ be the
graph formed from K by removing the edge xy, and adding the vertices and edges of Hm.
Since G ∈ G, the proper subgraph K ′ ⊊ G must contain a vertex v of degree at most 2.
The vertex v cannot be one of the internal vertices of Hm, since by the deﬁnition of Hm,
all internal vertices have degree 3. So v is also a vertex of K. But the degree of any vertex
of V (K) in K ′ is at least as large as its degree in K (in fact, unless u = x or u = y, the
degree of u in K is equal to its degree in K ′). Hence the vertex v ∈ V (K) has degree at
most 2 in K as well. ■

Now we are ready to complete the proof of the theorem using induction on |G|. The
initial cases are when |G| ≤ 6, and are easy to check by hand. Let G ∈ G be a graph
on n ≥ 7 vertices. We will show that G possesses one of the two structures given in the
theorem.
If G is not a wheel, then by Claim 4.5 G contains an induced copy of H ∗ of Hm such that
the internal vertices of H ∗ have no neighbours outside of H ∗. By Claim 4.6, G/H ∗ ∈ G.
Hence, by induction, G/H ∗ is either a wheel or is a graph formed by gluing together a
copy of Hi with connectors x and y and a copy of Hj with connectors x′ and y′, for some
i, j ≥ 4.
First consider the case when G/H ∗ is a wheel with center c and outside vertices
w1, . . . , wk. Recall that there is an edge in G/H ∗ between the two connectors of H ∗.

18

Suppose ﬁrst that the connectors of H ∗ are c and wi for some i. In this case, G is a
graph formed from Hk+1 and Hm by identifying the connectors of the two graphs. Indeed,
this follows from the fact that removing the edge cwi from the wheel gives a copy of Hk+1
and from the fact that the internal vertices of H ∗ have no neighbours outside of H ∗.
Suppose now that the connectors of Hm are two adjacent outside vertices of the wheel,
say w1 and w2. If k = 3 then the graph G/H ∗ is just the complete graph on 4 vertices, so,
as before, G is a graph formed from H4 and Hm with connectors w1 and w2. So suppose
that k ≥ 4. This ensures that d(c) ≥ 4 in G. We also have d(w2) ≥ 4 in G since w2 must
be connected to c, w3, as well as all the internal vertices of H ∗ (of which there are at least
2). But this gives a contradiction by Observation 4.4, since cw2 is an edge of G.
Now, consider the case when G/H ∗ is a graph formed by gluing together an Hi and an
Hj at their connectors. Recall that there is an edge in G/H ∗ between the two connectors
of H ∗. Suppose, without loss of generality, that this edge is in Hi. Let x and y be the
connectors of Hi and let v1, . . . , vi−2 be its internal vertices. Since xy ̸∈ E(Hi), one of the
connectors of H ∗ must be an internal vertex of Hi. If any internal vertex of Hi which is a
connector of H ∗ is adjacent in G to any vertex of {x, y} which is not a connector of H ∗,
then we immediately get a contradiction by Observation 4.4 since both of these vertices
have degree at least 4. Otherwise, for the internal vertex vt of Hi which is a connector
of H ∗ we must have 1 < t < i − 2, and the other connector vertex must be x. Then the
proper subgraph G−{v1, v2, . . . , vt−1} has minimum degree 3, contradicting our assumption
of G having no such subgraphs. This completes the proof of the inductive step and the
theorem. ■

It is an easy exercise to check that the graphs given in Theorem 4.1 are pancyclic and
hence Theorem 1.4 follows.

5 Finding a 6-cycle

Proposition 5.1. Every degree 3-critical graph G with n ≥ 6 contains a C6.

Proof. By Lemma 4.2 we have δ(G) ≥ 3.
Let us use Lemma 4.3 to obtain an ordering x1, . . . , xn of the vertices of G. By part
(ii) and (iii) and using |G| ≥ 5, the graph induced by the last four vertices is a K4 minus
an edge. Let us assume without loss of generality that the missing edge is xn−3xn−2, that
is, both xn−1 and xn have degree 3 in G[{xn−3, xn−2, xn−1, xn}].
Now let t ≤ n − 4 be the largest index for which the forward neighbourhood of the
vertex xt is not {xn−1, xn} (t exists because, for example “1” is such an index).
First let us suppose that xt has two forward neighbours xi and xj outside of {xn−1, xn}.
By the deﬁnition of xt we have that xi and xj are both adjacent to xn−1 and xn. Let
m ∈ [n] \ {n, n − 1, i, j, t} be the largest index such that the forward neighbourhood of xm
is not equal to {xi, xj} (m exists since |G| ≥ 6). Note that if {i, j, t} ̸= {n − 2, n − 3, n − 4},
then we have m ≥ n − 4 and the forward neighbourhood of xm is {xn, xn−1}. Thus
xn−1xmxnxjxtxi is a six-cycle (see Figure 13). If {i, j, t} = {n − 2, n − 3, n − 4}, then the

19

xi

xn xn−1

xj
 xt

xm
 xn−2

xn xn−1

xn−3
 xn−4

Figure 13: The two possible conﬁgurations which can occur in the case when xt has
two forward neighbours xi and xj, outside of {xn−1, xn}. The grey vertices represent
ones which may or may not be present.

xn−1 xi

xs xn xt

Figure 14: The possible induced subgraphs G[xm+1, . . . , xn}] in the case when xt has
exactly one forward neighbour xi outside of {xn−1, xn}. The unlabeled vertices may or
may not be there.

graph G[{xn, . . . , xm+1}] (see Figure 13) has the property that any pair of vertices, but
{xn−2, xn−3} have a path of length four between them. Thus the addition of xm will create
a six-cycle.
Suppose now that xt has exactly one forward neighbour xi, with t + 1 ≤ i ≤ n − 2,
outside of {xn−1, xn}. Without loss of generality let xn be a neighbour of xt in {xn, xn−1}.
By the deﬁnition of xt we have that xi is adjacent to both xn−1 and xn. If i = n − 2, let us
deﬁne s := n − 3, and otherwise let s := n − 2. Let m be the smallest index such that the
forward neighbourhood of xm is neither {xi, xn} nor {xn−1, xn} (m exists since the index
“1” is certainly of that kind). Then the structure of the graph G[{xm+1, . . . , xn}] looks
like the one in Figure 14. Observe that for any pair of vertices in such a graph, except for
the pairs {xn−1, xn} and {xn, xi}, there is a path of length four between them. Hence no
matter where the two forward neighbours xj and xl of xm, with {j, l} ̸= {n − 1, n}, {n, i},
are, they close a six-cycle. ■

20

6 Concluding remarks

In Theorem 1.2 we constructed degree 3-critical graphs with no 23-cycles. One could ask
whether longer cycles could be forbidden as well. It is easy to use our method to construct
sequences of degree 3-critical graphs with no m-cycles for any odd m ≥ 23. Indeed,
combining Proposition 3.9 with Theorem 2.5 shows that there are 2k-avoiding sequences
for all k ≥ 10. Then Lemmas 2.1 and 2.2 give us degree 3-critical graphs with no cycles
of length 2k + 3 for all k ≥ 10. It would be interesting to determine the shortest cycle
length ℓ for which there exist an inﬁnite sequence of degree 3-critical graphs with no cycle
of length ℓ. From the results in this paper we see that ℓ must be between 7 and 23.
In this paper we were only able to ﬁnd inﬁnite sequences of degree 3-critical graphs
which do not contain odd cycles. It is not clear whether even cycles can be forbidden in
the same way. We pose the following problem.

Problem 6.1. Is there a function C(n) tending to inﬁnity such that every degree 3-critical
graph on n vertices contains cycles of all lengths 4, 6, 8, . . . , 2C(n).

Another natural extremal question concerns the number of diﬀerent cycle length. A
construction due to Bollob´as and Brightwell [2] gives degree 3-critical graphs with no
cycles of length greater than 4 log2 n + O(1). Their construction is just the graph G(Td)
where Td is the 1-3-tree having a root with each of his three subtrees being a perfect binary
tree of depth d. We conjecture that these graphs give the smallest number of cycle lengths
amongst all degree 3-critical graphs on n vertices.

Conjecture 6.2. Every degree 3-critical graph on n vertices contains cycles of at least
3 log2 n + O(1) distinct lengths.

A similar conjecture could be made about leaf-leaf paths in trees.

Conjecture 6.3. Every 1-3 tree has leaf-leaf paths of at least log2 n distinct lengths.

In this paper we have shown that for d ≥ 20, it is impossible to guarantee that a
suﬃciently large 1-3 tree T contains a leaf-leaf path of length d. However, perhaps it is the
case that in a suﬃciently large 1-3 tree, there are leaf-leaf paths of “many” short lengths.

Conjecture 6.4. There is a constant α > 0 and a function C(n) tending to inﬁnity such
that every 1-3 tree of order n contains at least αC(n) of distinct leaf-leaf path lengths
between 0 and C(n).

References

[1] B. Bollob´as. Modern Graph Theory. Springer, 1998.

[2] B. Bollob´as and G. Brightwell. Long cycles in graphs with no subgraphs of minimal
degree 3. Discrete Math., 75:47–53, 1989.

21

[3] P. Erd˝os, R. J. Faudree, A. Gy´arf´as, and R. H. Schelp. Cycles in graphs without proper
subgraphs of minimum degree 3. Ars Combin., 25(B):159–201, 1988.

[4] P. Erd˝os, R. J. Faudree, C. Rousseau, and R. H. Schelp. Subgraphs of minimal degree
k. Discrete Math., 85(1):53–58, 1990.

[5] G. Laman. On graphs and the rigidity of plane skeletal structures. J. Engrg. Math.,
4(4):331–340, 1970.

[6] A. Lehman. A solution of the Shannon switching game. J. Soc. Indust. Appl., 12:687–
725, 1964.

[7] C. Nash-Williams. Edge disjoint spanning trees of ﬁnite graphs. J. London Math. Soc.,
36:445–450, 1961.
 22
