<!-- source: https://arxiv.org/pdf/2206.04260v2 | converted from PDF -->

arXiv:2206.04260v2  [math.CO]  9 Oct 2022
ON THE ERDŐS-TUZA-VALTR CONJECTURE

JINEON BAEK

Abstract. The Erdős-Szekeres conjecture states that any set of more than
2n−2 points in the plane with no three on a line contains the vertices of a
convex n-gon. Erdős, Tuza, and Valtr strengthened the conjecture by stating
that any set of more than ∑a−2
i=n−b (n−2
i ) points in a plane either contains
the vertices of a convex n-gon, a points lying on a concave downward curve,
or b points lying on a concave upward curve. They also showed that the
generalization is actually equivalent to the Erdős-Szekeres conjecture.
We prove the ﬁrst new case of the Erdős-Tuza-Valtr conjecture since the
original 1935 paper of Erdős and Szekeres. Namely, we show that any set of(n−1
2 ) + 2 points in the plane with no three points on a line and no two points
sharing the same x-coordinate either contains 4 points lying on a concave
downward curve or the vertices of a convex n-gon.

1. Introduction

A set of n points on a plane is in a convex position if they form the vertices of a
convex polygon. For simplicity, denote any set of n points in convex position as an
n-gon. The well-known Erdős-Szekeres conjecture is the following. Here, a ﬁnite
set of points on a plane is in general position if no three points are on a line and
no two points share the same x-coordinate1.

Deﬁnition 1.1. For any n ≥ 3, let N (n) be the maximum number of points on a
plane in a general position with no subset forming an n-gon.

Conjecture 1 (Erdős-Szekeres [4]). For any n ≥ 3, N (n) = 2n−2.

In 1935, Erdős and Szekeres showed N (n) ≤ (
2n−4
n−2 ) = O (4n/√
n) [3]. In 1960,
they provided a construction of exactly 2n−2 points with no n points in convex
position, showing the lower bound N (n) ≥ 2n−2 [4]. The upper bound of N (n)
stayed in the magnitude of O(4n/√
n) despite many improvements [2, 8, 14, 15, 9,
11] until Suk [12] proved an upper bound of N (n) ≤ 2n+o(n) in 2016. The best upper
bound so far is N (n) ≤ 2n+O(√
n log n) [7], and the precise equality N (n) = 2n−2

remains neither proven or disproven to this date.
Now we state the generalization of Conjecture 1 by Erdős, Tuza, and Valtr [5].

Deﬁnition 1.2. An a-cap (resp. a-cup) is a set of a points lying on the graph of
a downwardly (resp. upwardly) convex function (see Figure 1).

Deﬁnition 1.3. Call any tuple (n, a, b) of integers satisfying 2 ≤ a, b ≤ n ≤ a+b−2
a triplet. For any triplet (n, a, b), deﬁne N (n, a, b) as the maximum number of points
on a plane in general position with no subset forming an n-gon, a-cap, or b-cup.

1It is not usually required for the x-coordinates to be diﬀerent when stating the Erdős-Szekeres
conjecture. However, the extra assumption does not hurt generality as we can rotate the point
set slightly if there is any overlap in the x-coordinates.

1

2 JINEON BAEK

Figure 1. A 4-cap, 5-cup and 6-gon (from left to right)

Conjecture 2 (Erdős-Tuza-Valtr [5]). For any triplet (n, a, b), we have

N (n, a, b) =
 a−2∑

i=n−b
 (
n − 2
i
 )
.

Deﬁnition 1.4. For any triplet (n, a, b), let P (n, a, b) be the statement that
N (n, a, b) = ∑a−2
i=n−b (
n−2
i )
. That is, P (n, a, b) is the special case of Conjecture
1 with the triplet (n, a, b).

Then the special case P (n, n, n) of Conjecture 2 is Conjecture 1, as n-caps/cups
are n-gons and the conjectured sum equals 2n−2. Interestingly, they showed that
the strengthened Conjecture 2 is actually implied by the original Conjecture 1 as
well.

Theorem 1.5 ([5]). Conjecture 1 and Conjecture 2 are equivalent. Speciﬁcally, for
any n ≥ 3 and any triplets (n, a, b), (n, a′, b′) with a ≥ a′ and b ≥ b′, the statement
P (n, a, b) implies P (n, a′, b′).

So any counterexample of Conjecture 2 for one triplet (n, a, b) would disprove
Conjecture 1 immediately. Indeed, such a line of attack [1] succeeded in disproving
a set-theoretic generalization [13] of Conjecture 1 by disproving an analogous set-
theoretic generalization of Conjecture 2 for the triplet (n, 4, n).
It is then natural to ask whether the original Conjecture 2 will hold for the same
triplet (n, 4, n) or not. We show that it does.

Theorem 1.6 (Main Theorem). For any n ≥ 3, the statement P (n, 4, n) holds.
That is, (
n−1
2 ) + 2 points on a plane in general position determine either a 4-cap or
a n-gon.

Related, Erdős and Szekeres proved the following cups-caps theorem in 1935 [3].

Theorem 1.7 (Erdős–Szekeres). For any a, b ≥ 2, any set of more than (
a+b−4
a−2 )

points in general position contains either an a-cap or b-cup.

For any a, b ≥ 2, the cases P (a+b−3, a, b) and P (a+b−2, a, b) of Conjecture 2 are
immediate consequences of this theorem. To see this, observe that any (a+b−3)-gon
either contains an a-cap on top or a b-cap on the bottom, and that the conjectured
values N (a + b − 3, a, b) = (
a+b−5
a−3 ) + (
a+b−5
a−2 ) = (
a+b−4
a−2 ) and N (a + b − 2, a, b) =
(
a+b−4
a−2 ) match with the cups-caps theorem. Our Theorem 1.6 is not a consequence
of the cups-caps theorem as n < a + b − 3 in the triplet (n, 4, n).

ON THE ERDŐS-TUZA-VALTR CONJECTURE 3

By Theorem 1.5, for triplets (n, a, b) with a ﬁxed n, the cases P (n, a, b) of Con-
jecture 2 form a pyramid of implications from top to bottom (Figure 2). On the
top, we have the Erdős-Szekeres conjecture (Conjecture 1), and at the bottom, we
have the cups-caps theorem (Theorem 1.7). Our theorem lies strictly in the middle
of them (Theorem 1.6). To the best of our knowledge, this is the ﬁrst new instance
of Conjecture 2 proven so far since the original 1935 paper [3] of Erdős and Szekeres.

P (n, n, n)

P (n, n − 1, n) P (n, n, n − 1)

P (n, n − 2, n) P (n, n − 1, n − 1) P (n, n, n − 2)

P (n, 4, n) P (n, 5, n − 1) · · · P (n, n, 4)

P (n, 3, n) P (n, 4, n − 1) · · · · · · · · · P (n, n, 3)

Erdős-Szekeres
(Conjecture 1)
 Our theorem
(Theorem 1.6)

Cups-caps theorem
(Theorem 1.7)

· · · · · · · · · · · · · · · · · ·

· · · · · ·

Figure 2. A schematic diagram of the implications between Con-
jecture 1, Theorem 1.7 and our Theorem 1.6.

The proof of main Theorem 1.6 generalizes to a purely combinatorial model of
convexity (Theorem 2.7). Section 2 describes the combinatorial setup we mainly
work with. Section 3 describes the α-statistic, a function for understanding a-
cap, b-cup free conﬁgurations especially with nearly maximal number of points.
Section 4 introduces (α, β)-plane, an useful notion for understanding 4-cap free
conﬁgurations, and motivates the deﬁnition of interweaved laced cups (Deﬁnition
4.4 and 4.5). Finally, Section 5 proves main Theorem 1.6 by ﬁnding interweaved
laced cups with induction (Theorem 5.10).

2. A combinatorial model of convexity

We introduce a purely combinatorial model of convexity that we mainly work
with. It is a slight modiﬁcation of the one ﬁrst suggested in [13] and explored
further in [6], [10] and [1].

Deﬁnition 2.1. In this paper, a conﬁguration is a ﬁnite set S of elements called
points or vertices equipped with the following structures.
• A linear ordering < of the vertices.
• For any subset of S with size 3, an arbitrary assignment of whether they
form a cap or a cup.
In standard terms, a conﬁguration is a bi-coloring of a ﬁnite, complete 3-uniform
hypergraph with a prescribed linear ordering of vertices.

Given a ﬁnite set of points in general position, we can make a conﬁguration
by ordering the points in their increasing x-coordinates and assigning each size 3
subset to be either a cap or cup according to its position in the plane. Let’s say that

4 JINEON BAEK

a conﬁguration is realizable if it can be constructed from actual points in this way.
The notion of caps and cups in plane are generalized to arbitrary conﬁgurations
which may not be realizable.

Deﬁnition 2.2. Denote any set of vertices x1 < x2 < · · · < xa of a conﬁguration
as simply x1x2 · · · xa in the increasing order.
In a conﬁguration, a set C = x1x2 · · · xa of a vertices forms an a-cup (resp.
a-cap) if any three consecutive points xi−1xixi+1 form a cup (resp. cap) for any
1 < i < a. In particular, we allow 1-cups and 1-caps. The size of C, also denoted
|C|, is the number of vertices a in C.
We say that x1 is the starting point of C and xa is the ending point of C. The
points x1 and xa are the endpoints of C. Equivalently, we say that C starts with
x1 and ends with xa, or that C is a cap (resp. cup) from x1 to xa. Call any pair
x < y of vertices in a conﬁguration an edge. If the size a of C is at least 2, we say
that C starts with the edge x1x2 and ends with the edge xa−1xa.
For a cap (resp. cup) C from vertex s to vertex t, say that C extends to left
with the vertex x (or edge xs) if xC is also a cap (resp. cup). Likewise, say that C
extends to right with the vertex x (or edge tx) if Cx forms a cap (resp. cup).

We also introduce the mirror reﬂection of a conﬁguration. For realizable conﬁg-
urations, this corresponds to reﬂecting the points along the y-axis.

Deﬁnition 2.3. The mirror reﬂection Sop of a conﬁguration S is the conﬁguration
with the same vertex set and assignments of 3-caps and 3-cups, but the prescribed
linear ordering reversed. In this way, a cap (resp. cup) C in S naturally corresponds
to the reﬂected cap (resp. cup) Cop in Sop with the same set of vertices.

We introduce two possible generalizations of an n-gon in this combinatorial model
of convexity.

Deﬁnition 2.4. In a conﬁguration, a weak (a, b)-gon is a pair of a-cap C1 and b-
cup C2 sharing the same endpoints x and y. An weak n-gon is any weak (a, b)-gon
with a + b = n + 2.
On the other hand, a strong (a, b)-gon is a weak (a, b)-gon (C1, C2) with the
additional constraint that C1 ∩ C2 = {x, y}. An strong n-gon is any strong (a, b)-
gon with a + b = n + 2.
An (a, b)-gon or n-gon denotes the weak (a, b)-gon or n-gon by default.

The only diﬀerence is that a weak n-gon allows the cap and cup to have over-
lapping vertices in the middle, while a strong n-gon does not. Note also that there
is no diﬀerence in any realizable conﬁgurations. We use the following notion.

Deﬁnition 2.5. A conﬁguration is a-cap (resp. b-cup or weak/strong n-gon) free
if it has no a-cap (resp. b-cup or weak/strong n-gon) in the conﬁguration.

Peters and Szekeres [13] proposed to generalize Conjecture 1 by stating that for
any n ≥ 2, the maximum size of a strong n-gon free conﬁguration is 2n−2, and
supplied a computer proof for the case n = 6. Later, Balko and Valtr [1] found
counterexamples for n = 7 and 8 with SAT solvers by ﬁnding counterexamples for
analogues of Conjecture 2. We instead propose to use the deﬁnition of a weak n-gon
instead to generalize Conjecture 1.

Conjecture 3 (Set-theoretic Erdős-Szekeres). For any n ≥ 2, the maximum size
̂N (n) of a weak n-gon free conﬁguration is equal to 2n−2.

ON THE ERDŐS-TUZA-VALTR CONJECTURE 5

From now on, we omit the word weak when we mention any (a, b)-gon or n-
gon. We can also state the analogous generalization of Conjecture 2 to arbitrary
conﬁgurations.

Conjecture 4 (Set-theoretic Erdős-Tuza-Valtr). For any triplet (n, a, b), the max-
imum size ̂N (n, a, b) of a weak n-gon, a-cap and b-cup free conﬁguration is equal
to ∑a
i=n+2−b (
n−2
i−2 )
.

The generalization of cups-caps theorem (Theorem 1.7) to arbitrary conﬁgura-
tions is well-known (e.g. [10]).

Theorem 2.6 (Set-theoretic cups-caps). For any a, b ≥ 2, the maximum size of an
a-cap and b-cup free conﬁguration is (
a+b−4
a−2 )
.

Our main result is the proof of Conjecture 4 for the case (n, a, b) = (n, 4, n). It
is the generalization of Theorem 1.6 to arbitrary conﬁgurations.

Theorem 2.7. For any n ≥ 3, any conﬁguration of size (
n−1
2 ) + 2 contains either
a 4-cap, n-cup or a (3, n − 1)-gon.

3. Structure of a-cap, b-cup free configurations

In this section, we discuss some properties of a conﬁguration S that avoids a-
caps and b-cups. They will be useful especially when the size of S is close to the
maximum possible value (
a+b−4
a−2 ) shown in Theorem 2.6. We do not claim originality
of the results in this section - it is mostly a recasting of the deﬁnitions introduced
in [10].
First, we deﬁne the slope labeling of an a-cap free conﬁguration S.

Deﬁnition 3.1. A slope labeling s of an a-cap free conﬁguration S is the assignment
of an integer s(xy) ∈ {1, 2, · · · , a − 2} to all the edges xy of S so that it satisﬁes
the following.
• For any points x < y < z in S, s(xy) ≤ s(yz) implies that xyz is a 3-cup.
The value s(xy) assigned to the edge xy is the label of xy.

For the actual slope sR(xy) ∈ R of an edge in a realizable conﬁguration S, both
the following properties would hold.
• For any points x < y < z in S, sR(xy) > sR(yz) implies that xyz is a 3-cap.
• For any points x < y < z in S, sR(xy) < sR(yz) implies that xyz is a 3-cup.
A slope labeling restricts the possible values of a ‘slope’ (label) to a much smaller
set {1, 2, · · · , a − 2} at the cost of giving up the ﬁrst property. That is, edges of
strictly decreasing labels may not form a cap (see the cup ABF in Figure 3). It is
also impossible in general to assign a slope labeling that satisﬁes both the properties.
However, any a-cap free conﬁguration has a slope labeling that satisﬁes the second
property.

Theorem 3.2. For any a-cap free conﬁguration S, a slope labeling always exists.
In particular, for any edge e, let c(e) be the maximum length of a cap starting with
e; the function c(e) − 1 is a slope labeling.

Proof. For any edge e, its assigned label i is in between 1 and a − 2 inclusive by
deﬁnition. Assume by contrary that there is a 3-cap xyz in S with the label s of
xy less than or equal to the label t of yz. As the label of edge yz is t, there is a cap

6 JINEON BAEK

C of size t + 1 starting with yz. Since xyz forms a cap, the cap C extends to a cap
xC of size t + 2 that starts with xy. By the deﬁnition of s, we have s + 1 ≥ t + 2,
which contradicts the hypothesis s ≤ t. □

A
 B
 C
 D
 E
 F
2
 1
 2
 2
 1
 2 1
 1

1 1
 1

Figure 3. A 4-cap and 4-cup free realizable conﬁguration with
the slope labeling of Theorem 3.2. The labels of the edges AF, BD,
CD and CE are 1, 2, 2 and 2 respectively.

For the rest of the paper, we will ﬁx a large a-cap free conﬁguration S and a
slope labeling of S so that there is no confusion in the label of an arbitrary edge of
S. The following lemma is immediate.

Lemma 3.3. For any a-cap free conﬁguration S with slope labeling s, the restric-
tion of s to an arbitrary subset S′ of S is a slope labeling of S′.

Assume any a-cap, b-cup free conﬁguration S with a slope labeling s by integers
from 1 to a − 2. For each point p of S, we assign its α-statistic which is a tuple
α(p) = (α1(p), α2(p), · · · , αa−2(p)) of natural numbers.

Deﬁnition 3.4. Fix any a-cap, b-cup free conﬁguration S with a slope labeling.
For all p ∈ S and 1 ≤ i ≤ a−2, deﬁne the integer αi(p) as maximum length of a cup
that ends with the point p and an edge of slope ≤ i. If there is no such cup, then
let αi(p) = 1. In particular, the rightmost point p has the value α
i(p) = 1 for any
i. The α-statistic of a point p in S is the tuple α(p) = (α1(p), α2(p), · · · , αa−2(p)).

Deﬁnition 3.5. For any integers a, b ≥ 2, deﬁne the grid simplex

Ta,b := {(x1, x2, · · · , xa−2) ∈ Na−2 : 1 ≤ x1 ≤ · · · ≤ xa−2 ≤ b − 1}.

Theorem 3.6. For any a-cap, b-cup free conﬁguration S with a ﬁxed slope labeling
s, the α-statistic of S satisﬁes the following.
(1) For any point p, 1 ≤ α1(p) ≤ · · · ≤ αa−2(p) ≤ b − 1. Consequently, the
α-statistic α is a map from S to Ta,b.

ON THE ERDŐS-TUZA-VALTR CONJECTURE 7

(2) For any two points x < y connected by an edge of label i, αi(x) < αi(y)
holds. So in particular, α is injective.

Proof. We check the two conditions the α-statistic has to satisfy. The inequality
1 ≤ α1(p) ≤ · · · ≤ αa−2(p) ≤ b − 1 for any point p follows directly from the
deﬁnitions. The cup of length αi(x) that ends with the vertex x and an edge
of label ≤ i can be extended to the right with the edge xy of label i, so that
αi(x) + 1 ≤ αi(y) in any of the two given deﬁnitions of αi. □

Note that the size of Ta,b is (
a+b−4
a−2 )
. For a quick proof, note that any
(x1, x2, · · · , xa−2) ∈ Ta,b corresponds bijectively to an arbitrary subset {xi + i −
1 : 1 ≤ i ≤ a − 2} of {1, 2, · · · , a + b − 4} of size a − 2. Consequently, α being
injective immediately proves Theorem 2.6 that |S| ≤ (
a+b−4
a−2 ). Therefore, if the size
of S is nearly equal to the maximum size (
a+b−4
a−2 )
, we can expect the map α to be
almost bijective with some exceptional ‘holes’ in Ta,b.
Let us end this section with a remark on the α-statistic of the mirror conﬁgura-
tion.

Deﬁnition 3.7. For any a-cap, b-cup free conﬁguration S and its slope labeling s,
deﬁne the mirror reﬂection sop of the slope labeling s as the following.

sop(yx) = a − 1 − s(xy)

We leave it as an exercise to show that sop is a proper slope labeling of Sop.

Lemma 3.8. The mirror reﬂection sop of a slope labeling s of S is a slope labeling
of Sop.

Remark 3.9. We use the mirror reﬂection of a labeling extensively to exploit the
symmetry without loss of generality. For example, take an arbitrary 4-cap free
conﬁguration S. Its slope labeling s has values in {1, 2}. So for any edge xy, if
its label s(xy) is 1 (resp. 2) then the labeling sop(yx) of its reﬂection is 2 (resp.
1). Therefore, if the statement we want to show regarding S is invariant under
reﬂection, then we can safely assume that the edge connecting x and y is labeled 1
by reﬂecting S if necessary.
 4. The (α, β)-plane

In this section, we focus our attention on an arbitrary 4-cap, n-cup free conﬁg-
uration S with a ﬁxed slope labeling and α-statistic.

In our conﬁguration S, we only have edges of label 1 and 2, and the following is
an immediate consequence of Deﬁnition 3.1. We will use this extensively without
further mentions.

Corollary 4.1. In an arbitrary 4-cap free conﬁguration with slope labeling, any
edge of label 1 extends a cup to the left. That is, for any edge pq of label 1 and a
cup C that starts with q, the sequence pC is also a cup.
Likewise, any edge of label 2 extends a cup to the right. That is, for any edge
pq of label 2 and a cup C that ends with p, the sequence Cq is also a cup.

Also, we deﬁne aliases for the α-statistic of S.

8 JINEON BAEK
 α(p)

β(p)
 1

1
 2

2
 3

3
 A

B C

D E F

2 1

2
 2
 1

2 2 1

1
 1
 1

Figure 4. The (α, β)-plane of the 4-cap, 4-cup free conﬁguration
in Figure 3 with the slope labels of some edges.

Deﬁnition 4.2. For an arbitrary 4-cap, n-cup free conﬁguration S with a ﬁxed
slope labeling and α-statistic p ↦→ (α1(p), α2(p)), deﬁne aliases α = α1 and β = α2.
Thus, α(p) = α1(p) is the maximum length of a cup that ends with the vertex p
and an edge of label 1 (α(p) = 1 if there is no such cup). The value β(p) = α2(p)
is the maximum length of any cup that ends with the vertex p.

The α-statistic α(p) = (α(p), β(p)) maps S to the triangular grid set

T4,n := {(a, b) ∈ N2 : 1 ≤ a ≤ b ≤ n − 1}

injective by Theorem 3.6. With this, if the size of S is |T4,n| − k = (
n−1
2 ) − k
where k is small, it helps to identify S with the grid points T4,n with k missing
holes (see Figure 4). Call such a diagram an (α, β)-plane of the 4-cap, n-cup free
conﬁguration S. The following is a direct consequence of Theorem 3.6, and we will
use it extensively without mentioning.

Corollary 4.3. Assume an arbitrary 4-cap, n-cup free conﬁguration S.
For any points p, q with β(p) = β(q),
• p and q are always connected with an edge of label 1
• and p < q if and only if α(p) < α(q).
Consequently, in an (α, β)-plane any horizontal edge is labeled 1, and each column
is sorted in the increasing order of vertices from left to right.
Likewise, for any points p, q with α(p) = α(q),
(1) p and q are always connected with an edge of label 2
(2) and p < q if and only if β(p) < β(q).
Consequently, in an (α, β)-plane any vertical edges is labeled 2, and each row is
sorted in the increasing order of vertices from bottom to top.

ON THE ERDŐS-TUZA-VALTR CONJECTURE 9

We will now use the concept of the (α, β)-plane to introduce and motivate several
key notions for our proof. Take a 4-cap, n-cup free conﬁguration S. For simplicity,
assume at ﬁrst that S of size (n
2) (the maximum possible size), so that every location
in the (α, β)-plane is occupied. Then we can identify a point p in S with its location
(α(p), β(p)) in the (α, β)-plane.
Take any 1 ≤ k ≤ n − 1 and consider the path of vertices

Ck = (1, k), (2, k), . . . , (k − 1, k), (k, k), (k, k + 1), . . . , (k, n − 1)

in the (α, β)-plane. By Corollary 4.3, the ﬁrst k − 1 edges in this path are labeled 1,
and the last n − k − 1 edges are labeled 2, so these points must form an (n − 1)-cup
Ck from start pk = (1, k) to end qk = (k, n − 1). For any pair of (n − 1)-cups Ck and
Cl with k < l, the ordering of their endpoints is then pk < pl ≤ qk < ql. Motivated
by this, we introduce the following deﬁnition of interweaved cups.

Deﬁnition 4.4. Two cups C1 and C2 running from p to r and q to s respectively
are interweaved if p < q ≤ r < s holds.

So if |S| = (
n
2)
, we get n − 1 diﬀerent (n − 1)-cups C1, . . . , Cn−1 all mutually
interweaved. Moreover, for each cup Ck we have the k-cup Dk of vertices

Dk = (1, 1), (1, 2), ..., (1, k)

that ends with the left endpoint pk of Ck and the (n − k)-cup Ek of vertices

Ek = (k, n − 1), (k + 1, n − 1), ..., (n − 1, n − 1)

that starts with the right endpoint qk of Ck. Motivated by this, we introduce the
following notion of laced cups.

Deﬁnition 4.5. A (n − 1)-cup C from p to q is laced if there exists a cup Cp that
ends with p, and a cup Cq that starts with q, so that |Cp| + |Cq| = n − 1.
2

So if |S| = (
n
2) = (
n−1
2 )+(n−1), then all of our mutually interweaved (n−1)-cups
Ck are laced. The importance of this concept will be shown in Lemma 5.2 which
shows that if S contains just two interweaved laced (n − 1)-cups, then S contains
a (3, n − 1)-gon. We expect that for |S| = (
n−1
2 ) + d with any 1 ≤ d ≤ n − 1, we
can ﬁnd d mutually interweaved laced (n − 1)-cups (Conjecture 5). Roughtly, this
amounts to saying that an additional hole in the (α, β)-plane only destroys one of
the mutually interweaved laced (n − 1)-cups.
We show this for d = 2 (Theorem 5.10) and this is suﬃcient to show the main
theorem that for |S| = (
n−1
2 ) + 2 we can always ﬁnd an n-gon (Theorem 2.7). The
proof for case d = 2 requires a delicate inductive argument and several lemmas
about interweaved laced (n − 1)-cups; we now turn to stating and proving those
lemmas. Before doing so, we brieﬂy remark that the concept of interweaved cups
and of laced cups are symmetric under mirror reﬂection.

Lemma 4.6. Two cups C1, C2 are interweaved in conﬁguration S if and only if
Cop
2 and Cop
1 are interweaved in Sop. An (n − 1)-cup C is laced in conﬁguration S
if and only if Cop is laced in Sop.

2One might expect the sum to be n given the above motivation, but it turns out that n − 1 is
suﬃcient.

10 JINEON BAEK

x

1
a b c
QP

Figure 5. Figure for the proof of Lemma 5.1. The cup P ends at
a and the cup Q is from b to c.

p
 q r
 s
Cp
 Cr
1

2
 C1 C2

Figure 6. Figure for the proof of Lemma 5.2. The cup Cp ends
with p and Cr starts with r.

5. Interweaved laced cups

We ﬁrst show that in a 4-cap free conﬁguration, a pair of interweaved laced
(n − 1)-cups from p to r and q to s respectively (so that p < q ≤ r < s) is suﬃcient
to force an n-gon. The following covers the degenerate case q = r.

Lemma 5.1 (Balko and Valtr [1]). Take any n ≥ 3 and a 4-cap, n-cup free conﬁg-
uration S. If the ending point x of an (n − 1)-cup C1 is also the starting point of
another (n − 1)-cup C2, then S contains an (3, n − 1)-gon.

Proof. (See Figure 5) Say C1 = P x where P is an (n − 2)-cup that ends with
some vertex a. Likewise, say that C2 = xQ where Q is an (n − 2)-cup that starts
with b. Note that the statement to prove and the deﬁnitions introduced so far are
symmetric under reﬂection. So without loss of generality, we can assume that ab is
labeled 1. Now aQ is a (n − 1)-cup because ab has label 1. Say that Q ends with
the point c.
If axc is a cap, then we ﬁnd the (3, n − 1)-gon formed by axc and aC′
2 and we
are done. If axc is a cup, then the (n − 1)-cup C1 extends to the right with vertex
c, contradicting that S is n-cup free. □

Now we show the general case q ≤ r.

Lemma 5.2. Take any 4-cap, n-cup free conﬁguration S where n ≥ 3. If S contains
a pair of interweaved laced (n − 1)-cups, then S contains an (3, n − 1)-gon.

Proof. (See Figure 6) Let C1 and C2 be the pair of interweaved laced (n − 1)-cups
from p to r and q to s respectively, so that p < q ≤ r < s. If q = r, we are done
by Lemma 5.1, so we can assume q < r. As the setup is symmetric along reﬂection

ON THE ERDŐS-TUZA-VALTR CONJECTURE 11

x
a b
 y
 dc

Q
P R

Figure 7. Figure for the proof of Lemma 5.3. The cups P , Q and
R contains the endpoints a, b and c, and d respectively.

(e.g. Remark 3.9 and 4.6), we can assume that the edge qr is of label 1 without
loss of generality.
As C1 is laced we have a cup Cp ending with p and and a cup Cr starting with
r so that |Cp| + |Cr| = n − 1. Observe that the edge pq is of label 2, or otherwise
we can extend the (n − 1)-cup C2 to left with pq and reach contradiction.
If pqr is a cap, then the cap pqr and the cup C1 forms a (3, n − 1)-gon and
we are done. Now assume that pqr is a cup. Since pq is of label 2, the cup Cp
extends to right with q. Since qr is of label 1, the cup Cr extends to left with q
as well. Now the cups Cpq and qCr are joined along the vertex q. Since pqr is a
cup, they all connect to make a cup CpqCr of size |Cp| + |Cr| + 1 = n, leading to
contradiction. □

We prepare more lemmas and observations before starting the main proof. In
particular, we will use the following special case to ﬁnd a pair of interweaved laced
cups. Note that for this lemma we have n ≥ 4 instead of n ≥ 3.

Lemma 5.3. Take any 4-cap, n-cup free conﬁguration S with n ≥ 4. Assume an
(n − 1)-cup C from x to y in S. Also, assume an (n − 2)-cup Cx that ends with x,
and an (n − 2)-cup Cy that starts with y. Then S contains a pair of interweaved
laced (n − 1)-cups.

Proof. Using the symmetry of the statement along mirror reﬂection, we can assume
that xy is labeled 1 without loss of generality.
Let Cx = P x, C = xQy and Cy = yR so that P, Q, R are (n−3)-cups (see Figure
7). Let a be the ending point of P and d be the starting point of R. Say that Q is
from point b to c. As |P |, |Q|, |R| ≥ 1, the points a, b, c and d are all well-deﬁned
and we have a < x < b ≤ c < y < d (there is a possibility for b = c when n = 4).
The sequence xyR is an (n − 1)-cup because xy is labeled 1 and Cy = yR is
(n − 2)-cup. It is also laced because x is the endpoint of the (n − 2)-cup Cx = P x.
So we have two laced (n − 1)-cups xQy = C and xyR.
Do case analysis on the label of ab. Assume ﬁrst that ab is labeled 1. Then aQy
is an (n − 1)-cup. It is also laced because a is a 1-cup and yR is a (n − 2)-cup. aQy
interweaves with the laced (n − 1)-cup xyR because a < x < y and the endpoint of
R is strictly on the right of y.
Assume now that ab is labeled 2. We do another case analysis on the label of by.
If by is labeled 1, then byR is a laced (n − 1)-cup because it is a (n − 1)-cup and P b
is a (n − 2)-cup. Now the laced (n − 1)-cups xQy and byR are interweaved because
x < b < y and the endpoint of R is strictly on the right of y. If by is labeled 2, then
P by is an (n − 1)-cup, and it is also laced because yR is an (n − 2)-cup. Now laced

12 JINEON BAEK

(n − 1)-cups P by and xyR are interweaved, because the starting point of P comes
before x, x < y, and the endpoint of R is strictly on the right side of y. The proof
is now done. □

We introduce the following terminologies for a 4-cap, n-cup free conﬁguration S
of size at least (
n−1
2 ) + 1. Note that the following deﬁnition does not depend on a
particular choice of a slope labeling of S.

Deﬁnition 5.4. Assume an arbitrary 4-cap, n-cup free conﬁguration S of size at
least (
n−1
2 ) + 1 with n ≥ 3.
Deﬁne L(S) as the set of left endpoints of all (n − 1)-cups in S, and R(S) as
the set of right endpoints of all (n − 1)-cups in S. Let pS be the rightmost point
of L(S) and qS be the leftmost point of R(S). By Theorem 2.6, there is at least
one (n − 1)-cup in S, so that L(S), R(S) are nonempty and the points pS, qS are
well-deﬁned.

Remark 5.5. Note that under the assumption of Deﬁnition 5.4, L(Sop) = R(S),
R(Sop) = L(S), pSop = qS and qSop = pS.

Lemma 5.6. Under the assumption of Deﬁnition 5.4, we always have pS ≤ qS. In
other words, the sets L(S) and R(S) are separated in the increasing order with at
most one overlap.

Proof. Assume the contrary that pS > qS. Take any slope labeing of S. If the edge
qSpS is of label 1 we can extend an (n − 1)-cup starting with pS to the left by qS,
ﬁnding an n-cup in S. Likewise, if the edge qSpS is of label 2 we can extend an
(n − 1)-cup starting with qS to the right by pS, ﬁnding an n-cup in S. Both cases
lead to contradiction. □

We rule out the following case where we can ﬁnd a pair of interweaved laced
(n − 1)-cups immediately as well.

Lemma 5.7. Assume an arbitrary 4-cap, n-cup free conﬁguration S of size at least(
n−1
2 ) + 1. If a (n − 2)-cup in S ends with pS and a (n − 2)-cup in S starts with
qS, then S contains a pair of interweaved laced (n − 1)-cups.

Proof. An (n − 1)-cup Cl from some p′ ∈ L(S) to qS exists by the deﬁnition of
qS and L(S). Likewise, an (n − 1)-cup Cr from pS to some q′ ∈ R(S) exists by
the deﬁnition of pS and R(S). Note that Cl (or Cr) is laced by the existence of a
(n − 2)-cup that ends with pS (or that starts with qS).
We have p′ ≤ pS by the deﬁnition of pS, pS ≤ qS by Lemma 5.6 and qS ≤ q′

by the deﬁnition of qS. If p′ = pS, then we can apply lemma 5.3 to Cl to conclude
the proof. If qS = q′, then we can apply lemma 5.3 to Cr to conclude the proof. If
none of such equalities hold, then p′ < pS ≤ qS < q′ holds so Cl and Cr forms a
pair of interweaved laced (n − 1)-cups. □

We deﬁne the rows of S in the (α, β)-plane and show that each row is nonempty.

Deﬁnition 5.8. Fix an arbitrary 4-cap, n-cup free conﬁguration S of size at least(
n−1
2 )+1 with n ≥ 3 and a ﬁxed slope labeing and α-statistic. For any 1 ≤ i ≤ n−1,
deﬁne Ri(S) = {p ∈ S : β(p) = i}
which is the i’th row of the (α, β)-plane of S from the bottom. Note that Rn−1(S) =
R(S) in particular by deﬁnition.

ON THE ERDŐS-TUZA-VALTR CONJECTURE 13

Lemma 5.9. Under the assumption of Deﬁnition 5.8, each row Ri(S) is nonempty
for all 1 ≤ i ≤ n − 1.

Proof. Deﬁne the set R≥i(S) = {p ∈ S : β(p) ≥ i} for all 1 ≤ i ≤ n − 1. By
Theorem 2.6, there is at least one (n − 1)-cup C in S, so that the right endpoint of
C is contained in R≥i(S) for all i. Therefore, the minimum (leftmost) point xi of
R≥i(S) exists for all i.
We show that xi < xi+1 for all 1 ≤ i < n − 1. As xi+1 is in R≥(i+1)(S), we can
take a (i + 1)-cup Cxi+1 that ends with xi+1. Let y be the ending point of the
i-cup C. Then y ∈ R≥i(S) by deﬁnition and also y < xi+1 because Cxi+1 forms a
cup. This implies that xi = min R≥i(S) ≤ y < xi+1.
Because S is n-cup free, the equality Rn−1(S) = R≥(n−1)(S) holds and the set
is nonempty. For all 1 ≤ i < n − 1, the set Ri(S) = R≥(i+1)(S) \ R≥i(S) contains
xi because xi < xi+1. This concludes the proof. □

Now we are ready to prove the existence of a pair of interweaved laced (n − 1)-
cups by induction.

Theorem 5.10. For any n ≥ 3, any 4-cap, n-cup free conﬁguration of size (
n−1
2 )+2
contains a pair of interweaved laced (n − 1)-cups.

Proof. We proceed by induction. The base case n = 3 can be checked as the
following. For any conﬁguration of size (
2
2
) + 2 = 3, if the points are x, y, z in
the increasing order, then xy and yz forms a pair of interweaved laced 2-cups by
deﬁnition.
Now we show the inductive step. Fix an arbitrary n ≥ 4 and the following
inductive hypothesis (∗).

(∗) Any 4-cap, (n − 1)-cup free conﬁguration of size (
n−2
2 ) + 2 contains a pair
of interweaved laced (n − 2)-cups.

Fix an arbitrary 4-cap, n-cup free conﬁguration S of size (
n−1
2 ) + 2. Our goal now
is to show that S contains a pair of interweaved laced (n − 1)-cups.
By Lemma 5.7, we are already done if pS is an endpoint of a (n − 2)-cup and
qS is the starting point of an (n − 2)-cup at the same time. It remains for us to
show the case where either pS is not the endpoint of a (n − 2)-cup, or qS is not the
starting point of an (n − 2)-cup. Without loss of generality (e.g. Remark 5.5), we
can assume that qS is not the starting point of an (n − 2)-cup by reﬂecting S in the
other case. Now ﬁx a speciﬁed slope labeling and α-statistic of S to use (Theorem
3.2).

We deﬁne the set S′ on which we will apply the inductive hypothesis (∗) as the
following. For each 1 ≤ i ≤ n − 1, deﬁne xi as the leftmost point of the i’th row
Ri(S) of the (α, β)-plane (Deﬁnition 5.8). By Lemma 5.9, each xi is well-deﬁned.
Deﬁne the set ∆ = {x1, x2, · · · , xn−2} of size n − 2. Note that the point xn−1 is
excluded from ∆ by deﬁnition, and that xn−1 = qS by Deﬁnition 5.4. Deﬁne the
set S′ of size (
n−2
2 ) + 2 as S′ = S \ ∆ (see Figure 8). We will show later that S′ is
(n − 1)-cup free, so that we can apply the induction hypothesis (∗) to S′.
We assumed without loss of generality that qS is not the starting point of an
(n − 2)-cup. Using it, we show the following consequences.

14 JINEON BAEK
 α(p)

β(p)
 1

1
 2

2
 3

3
 4

4
 5

5
 6

6
 x1

x2

x3
 x4

x5
 x6

Figure 8. A hypothetical (α, β)-plane of a 4-cap, n-cup free set
S of size (
n−1
2 ) + 2 with n = 7. There are n − 3 = 4 ‘holes’ not in
S drawn as white points. The set ∆ of size n − 2 = 5 is marked
with circles.

(∗∗) Let x be the starting point of an arbitrary (n − 2)-cup C in S′ and let
i = β(x). Then the following hold.
(1) x < qS
(2) x ̸∈ Rn−1(S) and i ≤ n − 2
(3) xi < x and the edge xix is labeled 1, so xiC is an (n − 1)-cup in S
(4) α(xi) = 1 and α(x) = 2

First we show x < qS, the ﬁrst item of (∗∗). Assume otherwise that x ≥ qS. Then
the case x = qS directly contradicts our assumption, so we should have x > qS.
If the edge qSx is labeled 1, then qSC is an (n − 1)-cup so it also contradicts our
assumption. So qSx should be labeled 2. But in this case, as qS is the ending point
of some (n − 1)-cup D by deﬁnition, Dx is an n-cup which contradicts that S is
n-cup free. This concludes the proof of x < qS by contradiction.
As qS is the minimum value of R(S) = Rn−1(S), we also get x ̸∈ Rn−1(S) and
i = β(x) ≤ n − 2 (the second item of (∗∗)). Therefore, xi ∈ ∆ and as xi is minimal
in the row Ri(S) that also contains x, we have xi < x and the edge xix is labeled
1. Consequently, the (n − 1)-cup C extends to left with xi (the third item of (∗∗)).
If α(xi) > 1, then we can extend the (n−1)-cup xiC to left in S, so it contradicts
that S is n-cup free. So α(xi) = 1. Next, we show that α(x) = 2. Because the
edge xip is labeled 1, we have α(p) ≥ 2. If α(p) > 2, then we have a 3-cup D
that ends with pǫ and an edge with label 1. Now the cup D and Cǫ meets at pǫ,
and they form a cup because D ends with an edge with label 1. The cup is of size
|D| + |Cǫ| − 1 = n and we reach contradiction. So the equality α(pǫ) = 2 holds (the
fourth item of (∗∗)). This concludes the proof of (∗∗).
We now show that S′ is (n − 1)-cup free. Assume otherwise that S′ contains an
(n − 1)-cup C0 from some point x to y. Let i = β(x). Then since x is also the
starting point of some (n − 2)-cup in S′, the property (∗∗) implies that the edge xix
has label 1. Now the (n − 1)-cup C0 in S′ extends to left with xi in S, contradicting
that S is n-cup free.
 ON THE ERDŐS-TUZA-VALTR CONJECTURE 15

As S′ is (n − 1)-cup free, we can apply the inductive hypothesis (∗). Doing so,
we ﬁnd a pair (C1, C2) of interweaved laced (n − 2)-cups in S′, each from p1 to r1
and p2 to r2 so that p1 < p2 ≤ r1 < r2. Deﬁne i1 = β(p1) and i2 = β(p2). By the
property (∗∗) applied to C1 and C2 respectively, we have the following.
• p1, p2 < qS
• i1, i2 < n − 1
• xi1 p1 and xi2 p2 are edges with label 1
• xi1 C1 are xi2 C2 are (n − 1)-cups in S
• α(xi1 ) = α(xi2 ) = 1 and α(p1) = α(p2) = 2
We show that the pair (xi1 C1, xi2 C2) of (n − 1)-cups is interweaved and laced. This
completes the inductive step and the whole proof.
First, we show that the pair is interweaved. That is, whether xi1 < xi2 ≤ r1 < r2
is true. By the assumptions xi2 < p2 ≤ r1 < r2, it only remains for us to show
that xi1 < xi2 . Applying Corollary 4.3 to p1 < p2 and α(p1) = α(p2) = 2, we have
β(p1) < β(p2) which is exactly i1 < i2 by deﬁnition. Applying Corollary 4.3 again
to β(xi1 ) = i1 < i2 = β(xi2 ) and α(xi1 ) = α(xi2 ) = 1, we have xi1 < xi2 . This
completes the proof that the pair (xi1 C1, xi2 C2) is interweaved.
Now we show that each cup in the pair (xi1 C1, xi2 C2) is laced. Let ǫ ∈ {1, 2}
be any of the index 1 or 2. We extend the laced (n − 2)-cup Cǫ in S′ to show
that xiǫ Cǫ in S is also laced. Because Cǫ from pǫ to rǫ is laced in S′, there are
cups Cpǫ and Crǫ in S′ that ends with pǫ and starts with rǫ respectively, so that
|Cpǫ | + |Crǫ | = n − 2.
Say that Cpǫ starts with a point z in S′. Then z ≤ pǫ < qS so β(z) < n − 1 by
the deﬁnition of qS. Consequently, we have α(z) ≥ 2 as β(z) < n − 1 and z is not in
∆. So z is the endpoint of an edge yz of label 1 in S. We can extend Cpǫ to left to
a cup yCpǫ of size |Cpǫ | + 1 in S, and the cup yCpǫ ends with pǫ. This implies that
|Cpǫ | + 1 ≤ β(pǫ) = iǫ = β(xiǫ ). So in particular, β(xiǫ ) + |Cri| ≥ |Cpǫ | + |Cr| + 1 =
n − 1 and xiǫ Cǫ is a laced (n − 1)-cup for any of ǫ = 1 or 2. This concludes the
proof. □

We obtain the main theorem (Theorem 2.7) immediately as the following.

Proof of Theorem 2.7. Combine Theorem 5.10 with Lemma 5.2. □

We end with a conjecture that generalizes Theorem 5.10.

Conjecture 5. For any n ≥ 3 and 1 ≤ k ≤ n, any 4-cap, n-cup free conﬁguration
of size (
n−1
2 ) + k contains k mutually interweaved laced (n − 1)-cups.

Theorem 5.10 is a special case k = 2 of this conjecture. We can also prove the
case k = 1 with a similar induction argument with the same S′ = S \ ∆. The
case k = n is an immediate consequence of the discussion at the end of Section 4.
The proof of Theorem 5.10 fails to extend because it exploits the mirror symmetry
and essentially applies the inductive hypothesis twice to force the ’rightmost’ laced
(n − 1)-cup starting with pS and the ’leftmost’ laced (n − 1)-cup ending with qS.
This special case is then covered by Lemma 5.3.

Acknowledgement

The author is indebted to David Speyer for many illuminating discussions and
his help in making the presentation much more organized and clear. The author

16 JINEON BAEK

thanks to Andreas Holmsen for directing the author to the work of Moshkovitz and
Shapira [10] that inspired the notion of (α, β)-plane. The author also thanks to
Martin Balko and Pavel Valtr for their work [1] that inspired the main Theorem
1.6 and their thoughtful feedback on the early version of the draft.

References

[1] M. Balko and P. Valtr. A sat attack on the erdős–szekeres conjecture. European Journal of
Combinatorics, 66:13–23, 2017.
[2] F. R. Chung and R. L. Graham. Forced convex n-gons in the plane. Discrete & Computational
Geometry, 19(3):367–371, 1998.
[3] P. Erdös and G. Szekeres. A combinatorial problem in geometry. Compositio mathematica,
2:463–470, 1935.
[4] P. Erdös and G. Szekeres. On some extremum problems in elementary geometry. In Annales
Univ. Sci. Budapest, pages 3–4, 1960.
[5] P. Erdos, Z. Tuza, and P. Valtr. Ramsey-remainder. European Journal of Combinatorics,
17(6):519–532, 1996.
[6] J. Fox, J. Pach, B. Sudakov, and A. Suk. Erdős–szekeres-type theorems for monotone paths
and convex bodies. Proceedings of the London Mathematical Society, 105(5):953–982, 2012.
[7] A. F. Holmsen, H. N. Mojarrad, J. Pach, and G. Tardos. Two extensions of the erdős–szekeres
problem. Journal of the European Mathematical Society, 22(12):3981–3995, 2020.
[8] D. Kleitman and L. Pachter. Finding convex sets among points in the plane. Discrete &
Computational Geometry, 19(3):405–410, 1998.
[9] H. N. Mojarrad and G. Vlachos. An improved upper bound for the erdős–szekeres conjecture.
Discrete & Computational Geometry, 56(1):165–180, 2016.
[10] G. Moshkovitz and A. Shapira. Ramsey theory, integer partitions and a new proof of the
erdős–szekeres theorem. Advances in Mathematics, 262:1107–1129, 2014.
[11] S. Norin and Y. Yuditsky. Erdős–szekeres without induction. Discrete & Computational Ge-
ometry, 55(4):963–971, 2016.
[12] A. Suk. On the erdős-szekeres convex polygon problem. Journal of the American Mathemat-
ical Society, 30(4):1047–1053, 2017.
[13] G. Szekeres and L. Peters. Computer solution to the 17-point erdős-szekeres problem. The
ANZIAM Journal, 48(2):151–164, 2006.
[14] G. Tóth and P. Valtr. Note on the erdos-szekeres theorem. Discrete & Computational Geom-
etry, 19(3):457–459, 1998.
[15] G. Tóth and P. Valtr. The erdos-szekeres theorem: upper bounds and related results. Com-
binatorial and computational geometry, 19:557–568, 2005.

Jineon Baek, University of Michigan, Department of Mathematics, 2074 East
Hall, 530 Church Street, Ann Arbor, MI 48109-1043
Email address: jineon@umich.edu
