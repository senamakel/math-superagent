<!-- source: http://www.cs.bme.hu/~geza/es-1.pdf | converted from PDF -->

The Erd˝os-Szekeres theorem: upper bounds and related results

G´eza T´oth
∗

R´enyi Institute, Hungarian Academy of Sciences
e-mail: geza@renyi.hu

Pavel Valtr
†

Charles University, Prague
e-mail: valtr@kam.mff.cuni.cz

Abstract

Let ES(n) denote the least integer such that among any ES(n) points in general position in
the plane there are always n in convex position. In 1935, P. Erd˝os and G. Szekeres showed that
ES(n) exists and ES(n) ≤ (
2n−4
n−2 ) + 1. About 62 years later, the upper bound has been slightly
improved by Chung and Graham, a few months later it was further improved by Kleitman and
Pachter, and another few months later it was further improved by the present authors. Here we
review the original proof of Erd˝os and Szekeres, the improvements, and ﬁnally we combine the
methods of the ﬁrst and third improvements to obtain yet another tiny improvement.
We also brieﬂy review some of the numerous results and problems related to the Erd˝os–Szekeres
theorem.

1 Introduction

In 1933, Esther Klein raised the following question. Is it true that for every n there is a least number
ES(n) such that among any ES(n) points in general position in the plane there are always n in convex
position?
This question was answered in the aﬃrmative in a classical paper of Erd˝os and Szekeres [ES35].
In fact, they showed [ES35, ES60] that

2
n−2 + 1 ≤ ES(n) ≤
 (2n − 4
n − 2
 )
 + 1.

∗Supported by OTKA-T-038397
†Supported by project LN00A056 of The Ministry of Education of the Czech Republic.

1

The lower bound, 2n−2 + 1, is sharp for n = 2, 3, 4, 5 and has been conjectured to be sharp for
all n. However, the upper bound, (2n−4
n−2 ) + 1 ≈ c 4n
√n , was not improved for 60 years. Recently,
Chung and Graham [CG98] managed to improve it by 1. Shortly after, Kleitman and Pachter [KP978]
showed that ES(n) ≤ (2n−4
n−2 ) + 7 − 2n. A few months later the present authors [TV98] proved that
ES(n) ≤ (2n−5
n−2 ) + 2, which is a further improvement, roughly by a factor of 2.
In this note we review the original proof of Erd˝os and Szekeres, all three improvements, and then
we combine the ideas of the ﬁrst and third improvements to obtain the following result, which is a
further improvement by 1.

Theorem 1 For n ≥ 5, any set of (2n−5
n−2 ) + 1 points in general position in the plane contains n points
in convex position. That is, ES(n) ≤ (2n−5
n−2 ) + 1.

Next section contains a brief review of some of the numerous results and problems related to the
Erd˝os–Szekeres theorem.

2 Some related results

Many researchers have been motivated by the Erd˝os–Szekeres theorem. Here we mention only a small
part of the research related to the Erd˝os–Szekeres theorem. See [MS00], [BK01], and [BMP04] for the
latest survey.

2.1 Empty polygons

A famous open problem related to the Erd˝os–Szekeres theorem is the empty–hexagon problem. Let P
be a ﬁnite set of points in general position in the plane. A subset Q ⊂ P, |Q| = n, is called an n-hole
(or an empty convex n-gon) in P , if it is in convex position and its convex hull contains no further
points of P . Let g(n) be the smallest positive integer such that any P , |P | ≥ g(n), in general position
contains an n-hole. It is easy to see that g(3) = 3, g(4) = 5. Harborth [H78] proved g(5) = 10.
Horton [H83] gave a construction showing that no ﬁnite g(7) exists.

The empty–hexagon problem: Is there a ﬁnite g(6)?

Using a computer search, Overmars [O03] found a set of 29 points in general position having no
empty hexagon. Thus, if g(6) exists then g(6) ≥ 30.
Let Xk(P ) be the number of empty k-gons in an n-element point set P in general position, for k ≥ 0
(every subset of P of size at most 2 is considered as an empty polygon; thus X0(P ) = 1, X1(P ) = n,
X2(P ) = (n
2)). There are several equalities and inequalities involving these parameters. Ahrens et al.
[AGM99] proved general results giving the following interesting equalities on the numbers Xk(P ):
∑

k≥0
(−1)
kXk(P ) = 0,

2

∑

k≥1
(−1)
kkXk(P ) = −|P ∩ Int(P )|,

where |P ∩ Int(P )| is the number of interior points of P . Pinchasi et al. [PRS04] proved the above two
equalities by a simple argument (“continuous motion” method) and gave also some other equalities
and inequalities, e.g.
 X4(P ) ≥ X3(P ) − n2

2 − O(n),

X5(P ) ≥ X3(P ) − n2 − O(n).

Let Yk(n) = min|P |=n Xk(P ), that is, the minimum number of empty convex k-gons in a set of n
points. By the construction of Horton, Yk(n) = 0 for k ≥ 7. For k ≤ 6, the best known bounds are
the following.
 n2 − 5n + 10 ≤ Y3(n) ≤ 1.6195...n2 + o(n2),

(n−3
2 ) + 6 ≤ Y4(n) ≤ 1.9396...n2 + o(n2),

3 ⌊ n
12 ⌋ ≤ Y5(n) ≤ 1.0206...n2 + o(n2),

0 ≤ Y6(n) ≤ 0.2005...n2 + o(n2).

The lower bounds are given in [D87], the upper bounds in [BV04].

2.2 Convex bodies

Bisztriczky, Fejes T´oth, Pach, and T´oth [BF89], [BF90], [PT98], [T00] extended the Erd˝os-Szekeres
theorem to families of pairwise disjoint convex sets, instead of points.
A family of pairwise disjoint convex sets is said to be in convex position if none of its members is
contained in the convex hull of the union of the others.
It is easy to construct an arbitrarily large family of pairwise disjoint convex sets such that no three
or more of them are in convex position. So, without any additional condition on the family, we cannot
generalize the Erd˝os-Szekeres theorem.
For points we had the condition “no three points are on a line”, that is, “any three points are in
convex position”. Therefore, the most natural condition to try for families of convex sets is “any three
convex sets are in convex position”.
Bisztriczky and Fejes T´oth [BF89] proved that there exists a function P3(n) such that if a family
F of pairwise disjoint convex sets has more than P3(n) members, and any three members of F are in
convex position, then F has n members in convex position. In [BF90] they showed that this statement
is true with a function P3(n), triply exponential in n. Pach and T´oth [PT98] further improved the

3

upper bound on P3(n) to a simply exponential function. The best known lower bound for P3(n) is the
classical lower bound for the original Erd˝os-Szekeres theorem, 2n−2 ≤ P3(n).
In the case of points, if we have a stronger condition that every four points are in convex position,
then the problem becomes uninteresting; in this case all points are in convex position.
In case of convex sets, the condition “every four are in convex position” does not make the problem
uninteresting, but it still turns out to be a rather strong condition. Let F be a family of pairwise
disjoint convex sets. If any k members of F are in convex position, then we say that F satisﬁes
property Pk. If no n members of F are in convex position, then we say that F satisﬁes property P n.
Property P n
k means that both Pk and P n are satisﬁed. Using these notions, the above cited result of
Pach and T´oth states that if a family F satisﬁes property P n
3 , then |F| ≤ (2n−4
n−2 )2.
Bisztriczky and Fejes T´oth [BF90] raised the following more general question. What is the maxi-
mum size Pk(n) of a family F satisfying property P n
k ? Some of their bounds were later improved in
[PT98] and [T00]. The best known bounds are the following:

2n−2 ≤ P3(n) ≤ (2n−4
n−2 )2 [ES60], [PT98]

2 ⌊ n+1
4
 ⌋2 ≤ P4(n) ≤ n3 [PT98]

n − 1 + ⌊ n−1
k−2
 ⌋ ≤ P5(n) ≤ 6n − 12 [BF90], [T00]

n − 1 + ⌊ n−1
k−2
 ⌋ ≤ Pk(n) ≤ n + 1
k−5n for k ≥ 6 [BF90], [T00]

Pach and T´oth [PT00] investigated the case when the sets are not necessarily disjoint.

2.3 The partitioned version

It follows from the exponential upper bound on the number ES(n) by a simple counting argument
that for a given n every “huge” set of points in general position in the plane contains “many” n-point
subsets in convex position. However, geometric arguments yield much stronger results.
A convex n-clustering is deﬁned as a ﬁnite planar point set in general position which can be
partitioned into n ﬁnite sets X1, X2, . . . , Xn of equal size such that x1x2 . . . xn is a convex n-gon for
each choice x1 ∈ X1, x2 ∈ X2, . . . , xn ∈ Xn.
The positive fraction Erd˝os-Szekeres theorem [BV98] states that for any n any suﬃciently large
ﬁnite set X of points in general position contains a convex n-clustering of size ≥ εn · |X|, where
εn > 0 is independent of X. Answering a question of B´ar´any, P´or and Valtr [P03], [PV02] proved a
partitioned version of the Erd˝os-Szekeres theorem: any ﬁnite X in general position can be partitioned
into at most cn convex clusterings and a remaining set of at most c′
n points. The optimal constants

4

1/εn, c′
n are exponential in n, while cn is known to be at least exponential in n and at most of order
nO(n2) (see [PV02] for details).
The positive fraction Erd˝os–Szekeres theorem for collections of convex sets can be found in [PS98],
and the partitioned Erd˝os–Szekeres theorem for collections of convex sets can be found in [PV04].

3 The upper bound of Erd˝os and Szekeres

Deﬁnition. The points (x1, y1), (x2, y2), . . . , (xn, yn), x1 < x2 < . . . < xn, form an n-cap if

y2 − y1
x2 − x1 > y3 − y2
x3 − x2 > . . . > yn − yn−1
xn − xn−1 .

Similarly, they form an n-cup if
y2 − y1
x2 − x1 < y3 − y2
x3 − x2 < . . . < yn − yn−1
xn − xn−1 .

Theorem 2 (Erd˝os and Szekeres [ES35]) Let f (n, m) be the least integer such that any set of
f (n, m) points in general position in the plane contains either an n-cap or an m-cup. Then

f (n, m) =
 (n + m − 4
n − 2
 )
 + 1.

The following observation has a key role in the proof of the Erd˝os–Szekeres theorem.

Observation 1 If a point v is the rightmost point of a cap and also the leftmost point of a cup then
the cap or the cup can be extended to a larger cap or cup, respectively.

Proof. Let u be the second point of the cap from the right, and let w be the second point of the cup
from the left. Now, depending on the angle uvw, either the cap can be extended by w, or the cup can
be extended by u. See Fig. 1. ✷

Proof of f (n, m) ≤ (n+m−4
n−2 ) + 1. We use double induction on n and m. The statement trivially
holds for n = 2 and any m, and for m = 2 and any n. Let n, m ≥ 3 and suppose that the statement
holds for (n, m − 1) and for (n − 1, m). Take (n+m−4
n−2 ) + 1 points in general position. By induction
we know that any subset of at least (n+m−5
n−3 ) + 1 points contains either an n − 1-cap or an m-cup. In
the latter case we are done, so we can assume that any subset of at least (n+m−5
n−3 ) + 1 points contains
an n − 1-cap. Take an n − 1-cap and remove its right endpoint from the point set. Since we still
have at least (n+m−5
n−3 ) + 1 points, we have another n − 1-cap, remove its right endpoint again, and
continue until we have (n+m−5
n−3 ) points left. We have removed (n+m−4
n−2 ) + 1 − (n+m−5
n−3 ) = (n+m−5
m−3 ) + 1

5

v

u
 w
 u
 w

v

Figure 1: Either the cap can or the cup can be extended.

points, each of them a right endpoint of some n − 1-cap. But the set of these points, by induction,
contains either an n-cap or an m − 1-cup. In the ﬁrst case we are done. In the second case we have an
m − 1-cup whose left endpoint v is the right endpoint of some n − 1-cap. Observation 1 then ﬁnishes
the induction step. ✷

Proof of the Erd˝os-Szekeres theorem. Since ES(n) ≤ f (n, n), we have ES(n) ≤ (2n−4
n−2 ) + 1. ✷

Erd˝os and Szekeres [ES35] also proved that the bound f (n, m) ≤ (n+m−4
n−2 ) + 1 is tight for any n, m.
But it does not imply that the bound for ES(n) is tight as well. The best known lower bound is
2n−2 + 1 ≤ ES(n) [ES60] and in fact it is conjectured to be tight.

4 Three improvements

Theorem 3 (Chung and Graham [CG98]) For n ≥ 4,

ES(n) ≤
 (2n − 4
n − 2
 )

.

Proof. Take (2n−4
n−2 ) points in general position. Let A be the set of those points which are right
endpoints of some n − 1-cap. Just as above, we can argue that |A| ≥ (2n−4
n−2 ) − (2n−5
n−3 ) = (2n−5
n−3 )
. If
|A| > (2n−5
n−3 )
, then A contains either an n-cap or an n−1-cup. In the ﬁrst case we are done immediately,
in the second we have an n − 1-cup whose left endpoint is also a right endpoint of some n − 1-cap
and we are done as in the previous proof. So we can assume that |A| = (2n−5
n−3 )
. Let B be the set of
the other points, clearly |B| = (2n−5
n−3 )
. Let b ∈ B. The set {b} ∪ A has size (2n−5
n−3 ) + 1 so again it
contains either an n-cap or an n − 1-cup. In the case of n-cap we are done, so we can assume that it
an n − 1-cup for any choice of b. If the left endpoint of this n − 1-cup is an element of A, we are done
by Observation 1, since we have an n − 1-cup whose left endpoint is also a right endpoint of some
n − 1-cap. So, the left endpoint of this n − 1-cup is b. Therefore, any b ∈ B is the left endpoint of
an n − 1-cup whose right endpoint is in A. We can argue analogously, that any a ∈ A is the right

6

endpoint of an n − 1-cap whose left endpoint is in B. Let S be the set of all segments ab, where a ∈ A,
b ∈ B, and there is an n − 1-cup or n − 1-cap whose right endpoint is a and left endpoint is b. Let ab
be the element of S with the largest slope. Suppose that ab represents an n − 1-cup, the other case is
analogous. We know that there is an n − 1-cap whose right endpoint is a and left endpoint is b′. Now
it is easy to see that either the n − 1-cup and b′, or the n − 1-cap and b determine a convex n-gon.
This concludes the proof, see Fig. 2. ✷
 b a

b

Figure 2: Either b can be added to the cup, or b′ to the cap.

Theorem 4 (Kleitman and Pachter [KP98]) For n ≥ 4,

ES(n) ≤
 (2n − 4
n − 2
 )
 − 2n + 7.

Proof. We say that a point set is vertical if its two leftmost points have the same x-coordinate.
Observe, that any point set can be made vertical by an appropriate rotation. We deﬁne caps and
cups for vertical sets just like for any set of points, the only diﬀerence is that now the vertical edge
determined by the two leftmost points is allowed to be the leftmost edge of a cup or a cap, see Fig. 3.
Let fv(n, m) be the least integer such that any vertical set of fv(n, m) points in general position
contains either an n-cap or an m-cup. Take fv(n, m) − 1 points in a vertical point set with no n-caps
and m-cups. Let a and b be the two leftmost points such that a is above b. Let A be the set of those
points which are right endpoints of some n − 1-cap, and B be the set of the other points. Since the
two leftmost points do not belong to A, B is a vertical point set. If |B| ≥ fv(n − 1, m) then B has
an n − 1-cap or an m-cup. The ﬁrst case contradicts the deﬁnition of A, the second case contradicts
the assumption that we do not have an m-cup. So, |B| ≤ fv(n − 1, m) − 1. Now consider the set
A′ = A ∪ {b} and suppose that |A′| ≥ f (n, m − 1). Then A′ has an n-cap or an m − 1-cup. The ﬁrst

7

case is a contradiction immediately, in the second case consider the left endpoint of that m − 1-cup.
If it is b, then it can be extended to an m-cup by a, a contradiction. If it is in A, then the usual
argument works, we have an n − 1-cup whose left endpoint is also a right endpoint of some n − 1-cap
and one of them can be extended by Observation 1. So |A| = |A′| − 1 ≤ f (n, m − 1) − 2. Combining
the two inequalities we get that

fv(n, m) ≤ fv(n − 1, m) + f (n, m − 1) − 2,

and an analogous argument shows that

fv(n, m) ≤ fv(n, m − 1) + f (n − 1, m) − 2.

Using the known values of f (n, m), and that fv(n, 3) = fv(3, n) = n, we get that fv(n, m) ≤ (n+m−4
n−2 )+
7 − n − m, and the result follows. In fact, the inequality obtained for fv(n, m) is sharp [KP98]. ✷

a

b

Figure 3: A vertical point set with a 5-cap.

Theorem 5 (T´oth and Valtr [TV98]) For n ≥ 3,

ES(n) ≤
 (2n − 5
n − 2
 )
 + 2.

Proof. Take (2n−5
n−3 ) points in general position. Suppose that the set P does not contain n points in
convex position. Let x be a vertex of the convex hull of P . Let y be a point outside the convex hull of
P such that none of the lines determined by the points of P \ {x} intersects the segment xy. Finally,
let ℓ be a line through y which avoids the convex hull of P .
Consider a projective transformation T which maps the line ℓ to the line at inﬁnity, and maps
the segment xy to the vertical half-line v−(x′), emanating downwards from x′ = T (x). We get a
point set P ′ = T (P ) from P . Since ℓ avoided the convex hull of P , the transformation T does not

8

change convexity on the points of P , that is, any subset of P is in convex position if and only if the
corresponding points of P ′ are in convex position. So the assumption holds also for P ′, no n points of
P ′ are in convex position. By the choice of the point y, none of the lines determined by the points of
P ′ \ {x′} intersects v−(x′). Therefore, any m-cap in the set Q′ = P ′ \ {x′} can be extended by x′ to a
convex (m + 1)-gon.
Since no n points of P ′ are in convex position, Q′ cannot contain any n-cup or (n − 1)-cap.
Therefore, by the Lemma,

|Q′| ≤ f (n − 1, n) − 1 =
 (2n − 5
n − 2
 )
, |P | ≤
 (2n − 5
n − 2
 )
 + 1,

and the theorem follows. ✷
 x

Figure 4: Any n − 1-cap can be extended by x′ to a convex n-gon.

5 A combination of two methods

We now prove Theorem 1.

Proof of Theorem 1. Suppose that the set P does not contain n points in convex position and
|P | = (2n−5
n−2 ) + 1. Let x be a vertex of the convex hull of P and y be a point outside the convex hull
of P so close to x that none of the lines determined by the points of P \ {x} intersects the segment
xy. Finally, let ℓ be a line through y which avoids the convex hull of P .
Consider a projective transformation T which maps the line ℓ to the line at inﬁnity, and maps the
segment xy to the vertical half-line v−(x′), emanating downwards from x′ = T (x). We get a point

9

set P ′ from P . Just like in the previous proof, T does not change convexity on the points of P . Let
P ′′ = P ′ \ {x′}. By the assumption, P ′′ does not contain any n − 1-cap or n-cup.
Let A be the set of those points of P ′′ which are right endpoints of some n − 2-cap, and let
B = P ′′ \ A. If |A| > (2n−6
n−3 ) then A contains either an n − 1-cap or an n − 1-cup. The ﬁrst case
contradicts the assumption, in the second case we have an n − 1-cup whose left endpoint is also a
right endpoint of some n − 2-cap, so, either the n − 1-cup or the n − 2-cap can be extended by one
point and we get a contradiction. So, |A| ≤ (2n−6
n−3 )
. If |B| > (2n−6
n−2 )
, then B contains either an
n − 2-cap or an n-cup. The ﬁrst case contradicts the deﬁnition of A, since we ﬁnd a right endpoint
of some n − 2-cap in B, the second case contradicts the assumption. So |B| ≤ (2n−6
n−2 )
. But then
|P ′′| = |A| + |B| ≤ (2n−6
n−3 ) + (2n−6
n−2 ) = (2n−5
n−2 ) = |P ′′|, therefore, |A| = (2n−6
n−3 ) and |B| = (2n−6
n−2 )
.

a=v

b=v
 v v
 v

u u

u
 1
 2
 3
 4
 5=u4

3

2

1
 x

Figure 5: x′, u1, u2, u3, v1, v2 determine a convex hexagon.

Let b ∈ B. The set {b} ∪ A has size (2n−6
n−3 ) + 1 so again it contains either an n − 1-cap or an
n − 1-cup. In the case of n − 1-cap we are done, so we can assume that it is an n − 1-cup for any
choice of b. If the left endpoint of this n − 1-cup is an element of A, we have an n − 1-cup whose left
endpoint is also a right endpoint of some n − 2-cap, so, either the n − 1-cup or the n − 2-cap can be
extended by one point and we get a contradiction again. Hence the left endpoint of the n − 1-cup is b.
Therefore, any b ∈ B is the left endpoint of an n − 1-cup whose right endpoint is in A. We can argue
analogously, considering the sets {a} ∪ B, that any a ∈ A is the right endpoint of an n − 2-cap whose
left endpoint is in B.
Let S be the set of all segments ab, where a ∈ A, b ∈ B, and there is either an n − 1-cup or
n − 2-cap whose right endpoint is a and left endpoint is b. Let ab be the element of S with the largest

10

slope. Suppose that ab represents an n − 1-cup. The argument in the other case is analogous. Let
b = v1, v2, . . . , vn−1 = a be the points of the n − 1-cup from left to right. We know that there is also
an n − 2-cap whose right endpoint is a and left endpoint in B. Let u1, u2, . . . , un−2 = a be its points
from left to right. If un−3 lies above the line v1v2, then uj, v1, v2, . . . , vn−1 determine a convex n-gon
and we are done. Otherwise x′, u1, u2, . . . , un−3, v1, v2 determine a convex n-gon, see Fig. 5. This
concludes the proof. ✷

References

[AGM99] C. Ahrens, G. Gordon, and E. W. McMahon, Convexity and the beta invariant, Discrete
Comput. Geom. 22 (1999), 411-424.

[BK01] I. B´ar´any and Gy. K´arolyi, Problems and results around the Erd˝os–Szekeres theorem, Japanese
Conference on Discrete and Computational Geometry (2001), 91-105.

[BV98] I. B´ar´any and P. Valtr, A positive fraction Erd˝os–Szekeres theorem, Discrete and Computa-
tional Geometry 19 (1998), 335-342.

[BV04] I. B´ar´any and P. Valtr, Planar point sets with a small number of empty convex polygons, to
appear.

[BF89] T. Bisztriczky and G. Fejes T´oth, A generalization of the Erd˝os-Szekeres convex n-gon theorem,
Journal f¨ur die reine und angewandte Mathematik 395 (1989), 167–170.

[BF90] T. Bisztriczky and G. Fejes T´oth, Convexly independent sets, Combinatorica 10 (1990), 195–
202.

[BMP04] P. Brass, W. Moser, and J. Pach, Convex polygons and the Erd˝os-Szekeres problem, Chapter
8.2 in the book Research problems in discrete geometry, to appear.

[CG98] F. R. K. Chung and R. L. Graham, Forced convex n-gons in the plane, Discrete and Compu-
tational Geometry 19 (1998), 367–371.

[D87] K. Dehnhardt, Leere konvexe Vielecke in ebenen Punktmengen, dissertation, TU Braunschweig
1987.

[ES35] P. Erd˝os and G. Szekeres, A combinatorial problem in geometry, Compositio Mathematica 2
(1935), 463–470.

[ES60] P. Erd˝os and G. Szekeres, On some extremum problems in elementary geometry, Ann. Uni-
versitatis Scientiarum Budapestinensis, E¨otv¨os, Sectio Mathematica 3/4 (1960–61), 53–62.

11

[GRS90] R.L. Graham, B.L. Rothschild, and J.H. Spencer, Ramsey Theory, 2nd ed., John Wiley, New
York, 1990.

[H78] H. Harborth, Konvexe F¨unfecke in ebenen Punktmengen, Elem. Math. 33 (1978), 116–118.

[H83] J. D. Horton, Sets with no empty convex 7-gons, Canadian Math. Bull. 26 (1983), 482-484.

[KP98] D. J. Kleitman and L. Pachter, Finding convex sets among points in the plane, Discrete and
Computational Geometry 19 (1998), 405–410.

[MS00] W. Morris and V. Soltan, The Erd˝os-Szekeres problem on points in convex position – a survey.
Bull. Amer. Math. Soc. 37 (2000), 437-458.

[O03] M. H. Overmars, Finding sets of points without empty convex 6-gons, Discrete and Computa-
tional Geometry 29 (2003), 153–158.

[PS98] J. Pach and J. Solymosi, Canonical theorems for convex sets, Discrete and Computational
Geometry 19 (1998), 427–435.

[PT98] J. Pach and G. T´oth, A generalization of the Erd˝os-Szekeres theorem to disjoint convex sets,
Discrete and Computational Geometry, 19 (1998), 437-445.

[PT00] J. Pach and G. T´oth, Erd˝os-Szekeres-type theorems for segments and non-crossing convex
sets, Geometriae Dedicata 81 (2000) 1-12.

[P03] A. P´or, A partitioned version of the Erd˝os–Szekeres theorem for quadrilaterals, Discrete and
Computational Geometry 30 (2003), 321–336.

[PRS04] R. Pinchasi, R. Radoiˇci´c, and M. Sharir, On empty convex polygons in a planar point set,
(manuscript)

[PV02] A. P´or and P. Valtr, The partitioned version of the Erd˝os–Szekeres theorem, Discrete and
Computational Geometry 28 (2002), 625–637.

[PV04] A. P´or and P. Valtr, The partitioned Erd˝os–Szekeres theorem for convex sets, in preparation.

[T00] G. T´oth, Finding convex sets in convex position, Combinatorica 20 (2000) 589-596.

[TV98] G. T´oth and P. Valtr, Note on the Erd˝os-Szekeres theorem, Discrete and Computational
Geometry 19 (1998), 457–459.
 12
