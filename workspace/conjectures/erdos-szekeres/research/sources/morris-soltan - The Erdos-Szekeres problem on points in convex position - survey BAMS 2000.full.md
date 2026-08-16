<!-- source: https://www.ams.org/journals/bull/2000-37-04/S0273-0979-00-00877-6/S0273-0979-00-00877-6.pdf | converted from PDF -->

BULLETIN (New Series) OF THE
AMERICAN MATHEMATICAL SOCIETY
Volume 37, Number 4, Pages 437–458
S 0273-0979(00)00877-6
Article electronically published on June 26, 2000

THE ERD ˝OS-SZEKERES PROBLEM ON POINTS IN CONVEX
POSITION – A SURVEY

W. MORRIS AND V. SOLTAN

Abstract. In 1935 Erd˝os and Szekeres proved that for any integer n ≥ 3
there exists a smallest positive integer N (n) such that any set of at least N (n)
points in general position in the plane contains n points that are the vertices
of a convex n-gon. They also posed the problem to determine the value of
N (n) and conjectured that N (n)= 2n−2 +1 for all n ≥ 3.
Despite the eﬀorts of many mathematicians, the Erd˝os-Szekeres problem is
still far from being solved. This paper surveys the known results and questions
related to the Erd˝os-Szekeres problem in the plane and higher dimensions, as
well as its generalizations for the cases of families of convex bodies and the
abstract convexity setting.
 1. Introduction

The following problem attracts the attention of many mathematicians by its
beauty and elementary character.

The Erd˝os-Szekeres Problem 1.1. ([32], [33]) For any integer n ≥ 3, determine
the smallest positive integer N (n) such that any set of at least N (n) points in general
position in the plane (i.e., no three of the points are on a line) contains n points
that are the vertices of a convex n-gon.

The interest of Erd˝os and Szekeres in this problem was initiated by Esther Klein
(later Mrs. Szekeres), who observed that any set of ﬁve points in general position
in the plane contains four points that are the vertices of a convex quadrilateral.
Indeed, there are three distinct types of placement of ﬁve points in the plane, no
three on a line, as shown on Figure 1.1. In any of these cases, one can pick out at
least one convex quadrilateral determined by the points.
Klein suggested the following more general problem, namely the problem on the
existence of a ﬁnite number N (n)such thatfromany setcontainingat least N (n)
points in general position in the plane, it is possible to select n points forming a
convex polygon.
As observed by Erd˝os and Szekeres, there are two particular questions related
to this problem:
(1) Does the number N (n) exist?
(2) If so, how is N (n) determined as a function of n?
In their paper [32], Erd˝os and Szekeres proved the existence of the number

Received by the editors December 20, 1999, and in revised form April 4, 2000.
2000 Mathematics Subject Classiﬁcation. Primary 52C10.
Key words and phrases. Erd˝os-Szekeres problem, Ramsey theory, convex polygons and poly-
hedra, generalized convexity.
 c⃝2000 American Mathematical Society

437

438 W. MORRIS AND V. SOLTAN

s

s
 s
 s
 s
❆
❆❆
❆ ✁✁
✁
✁
✚
✚
✚✚❩
❩
❩❩
 s

s
 s

s
s
❳❳❳❳
❏❏
❏
❏❏❏ ss

s

ss

✑
✑✑ ◗
◗◗✡
✡
✡✡
✡✡❏
❏
❏❏
❏❏

Figure 1.1. Any ﬁve points in general position determine a con-
vex quadrilateral.

N (n) by two diﬀerent methods. The ﬁrst of them uses Ramsey’s theorem and,
as a result, gives the inequality N (n) ≤ R4(5,n), where R4(5,n)is a Ramsey
number (see Section 2 for details). The second method is based on some geometric
considerations, resulting in a better upper bound N (n) ≤ (
2n−4
n−2 ) +1. In the same
paper Erd˝os and Szekeres formulated the following conjecture.

Conjecture 1.2 ([32]). N (n)= 2n−2 +1 for all n ≥ 3.

Many years later (see [25], [26], and [29]) Erd˝os stated that “Szekeres conjectured
N (n)=2n−2+1.” He amended this in [28] to “Probably N (n)= 2n−2+1.” Szekeres
was more forceful in [78], saying “Of course we ﬁrmly believe that N (n)= 2n−2 +1
is the correct value.” Another statement of faith in the conjectured value for N (n)
may be found in [16]. Shortly before he died, Erd˝os [30] wrote: “I would certainly
pay $500 for a proof of Szekeres’ conjecture.”
Klein and Szekeres married shortly after the publication of [32], prompting Erd˝os
to call Problem 1.1 the “Happy End Problem”. The books [45] and [73] contain
picturesque descriptions of the Erd˝os-Szekeres problem origins.
Their second paper [33] contains an example of a set of 2n−2,n ≥ 3, points in
general position in the plane, no n of which determine a convex polygon. In other
words, Erd˝os and Szekeres have shown that N (n) ≥ 2n−2 +1 for all n ≥ 3.
Despite its elementary character and the eﬀort of many mathematicians, the
Erd˝os-Szekeres problem is solved for the values n =3, 4, and 5 only. The case
n = 3 is trivial, and n = 4 is due to Klein. The original paper by Erd˝os and
Szekeres [32] notes that E. Makai proved the equality N (5) = 9, while the ﬁrst
published proof of this result is due to Kalbﬂeisch et al. [50].
The next step in solving Problem 1.1 is to answer the following question.

Question 1.3. Does any set of at least 17 points in general position in the plane
contain 6 points that are the vertices of a convex hexagon?

For larger values of n, the best known upper bound N (n) ≤ (
2n−5
n−3 ) +2 was
recently proved by T´oth and Valtr [80].
Later Erd˝os posed a similar problem on empty convex polygons.

Problem 1.4 ([27]). For any positive integer n ≥ 3, determine the smallest posi-
tive integer H(n), if it exists, such that any set X of at least H(n) points in general
position in the plane contains n points which are the vertices of an empty convex
polygon, i.e., a polygon whose interior does not contain any point of X.

Trivially, H(3) = 3 and H(4) = 5, as easily follows from Figure 1.1. In 1978
Harborth [43] proved that H(5) = 10, while Horton [46] showed in 1983 that H(n)

THE ERD ˝OS-SZEKERES PROBLEM ON POINTS IN CONVEX POSITION 439

does not exist for all n ≥ 7. The only open case in Problem 1.4 is given by the
following question of Erd˝os.

Question 1.5 ([29]). Does the number H(6) exist?

There were many attempts to prove or disprove the existence of H(6) (see Section
3 for details). The best known result in this direction belongs to Overmars et al.
[67], who showed in 1989 that H(6) ≥ 27, if it exists.
To give positive or negative answers to Questions 1.3 and 1.5, several algorithms
for detecting a largest convex polygon or a largest empty convex polygon determined
by a given set of points were elaborated. Detailed descriptions of these algorithms
can be found in [3], [18], [22], [67].
Due to a wide interest in Problem 1.1, the original papers by Erd˝os and Szekeres
were reprinted (see [32], [33], and [78]), and a long list of reviews and books discussed
the problem in broad strokes (see [17], [20], [21], [31], [35], [39], [40], [41], [42], [45],
[56], [59], [61], [73], [74], [85]). Nevertheless, none of them covers the whole variety
of existing results and open problems. The purpose of this survey is to reﬂect the
recent stage of the Erd˝os-Szekeres problem, as well as its various generalizations
and related questions. The content of the survey is indicated by section headings
as follows.
1. Introduction.
2. Bounds on N (n).
3. The Erd˝os problem on empty convex polygons.
4. Higher dimensional extensions.
5. Other generalizations and related results.
In particular, we formulate a new conjecture for the higher dimensional version
of the Erd˝os-Szekeres problem (see Conjecture 4.2).
In what follows, we use standard notation: Ed denotes Euclidean d-space; |X|
and convX are the cardinality and the convex hull of a set X ⊂ Ed, respectively;
extP is the set of vertices (extreme points) of a convex polytope P ⊂ Ed.
We say that a set X ⊂ Ed is in convex position if x ̸∈ conv(X \ x) for any
point x ∈ X.In other words, X ⊂ Ed is in convex position provided X is a set of
vertices of a convex polytope in Ed. A convex polytope whose vertices belong to a
set Y ⊂ Ed is called empty provided the interior of the polytope does not contain
any point of Y . Recall that a set Z ⊂ Ed is in general position if no d +1 of its
points lie in a hyperplane.
 2. Bounds on N (n)

2.1. Upper Bounds from Ramsey Theory. As was mentioned above, the ﬁrst
proof on the existence of N (n) belongs to Erd˝os and Szekeres [32] and is based on
the following fundamental result of Ramsey [72].

Theorem 2.1 ([72]). For any positive integers k, l1,l2,... ,lr there exists a small-
est positive integer m0 satisfying the following condition. For any integer m ≥ m0,
if the k-element subsets of {1, 2,... ,m} are colored with colors 1, 2,... ,r,then
there exists an i, 1 ≤ i ≤ r, and an li-element subset T ⊂{1, 2,... ,m} so that each
of the k-element subsets of T is i-colored.

The smallest number m0 for which the conclusion of Ramsey’s theorem holds
is usually denoted by Rk(l1,l2,... ,lr). A proof of Ramsey’s theorem, for the case

440 W. MORRIS AND V. SOLTAN

r = 2, was independently discovered by Szekeres (see [32]) for the purpose of
showing the ﬁniteness of N (n).
The paper [38] discusses the importance of [32] in the development of Ramsey
theory. In the following theorem we give three diﬀerent methods for getting upper
bounds on N (n) based on Ramsey’s theorem. In each case, an easy argument shows
that N (n) ≤ Rk(l1,l2) for an appropriate choice of k, l1,l2.

Theorem 2.2. For any positive integer n ≥ 3 the number N (n) exists and

N (n) ≤ min{R4(n, 5),R3(n, n)}.

Proof. 1) Let X be any set of at least R4(n, 5) points in general position in the
plane. The original proof of [32] colors the 4-element subsets of X with color 1 if
the points are in convex position and colors them with color 2 otherwise. Klein’s
argument shows that it is impossible for all of the 4-element subsets of a 5-element
subset of X to be of color 2. Hence it must be true that X contains an n-element
subset for which all 4-element subsets are of color 1; i.e. all of them are in convex
position. It easily follows that all the n points are in convex position. Hence
N (n) ≤ R4(n, 5).
2) Lewin [60] reported that Tarsy, an undergraduate student, had come up with
the following independent proof while taking an exam in a combinatorics course.
Let X = {x1,x2,... ,xm} be a set of points in general position in the plane, with
m ≥ R3(n, n). Color a 3-element subset {xi,xj,xk}⊂ X, i< j < k, with color 1
if one encounters the points in the order (xi,xj,xk) by passing clockwise around
their convex hull. Color the subset with color 2 otherwise. It is easy to see that a
4-element subset of X is in convex position if and only if all of its 3-element subsets
are colored with the same color. This implies that an n-element subset of X is in
convex position if and only if all of its 3-element subsets are colored with the same
color. Hence N (n) ≤ R3(n, n).
3) The most recent proof involving a Ramsey-theoretic upper bound on N (n)
was discovered by Johnson [49]. Color a 3-element subset S of a planar set X in
general position with color 1 if there is an even number of points of X in the interior
of convS,and color S with color 2 otherwise. A one-line proof then shows that a
4-element subset of X is in convex position if and only if all of its 3-element subsets
have the same color. This once again implies that an n-element subset of X is
in convex position if and only if all of its 3-element subsets have the same color.
Therefore, N (n) ≤ R3(n, n).

Lewin [60] points out that R3(n, n) seems to be lower than R4(n, 5). The best
known bounds on the Ramsey numbers R3(n, n)are 2bn
2 ≤ R3(n, n) ≤ 2cn,for
some constants b and c (see [39]). The next section shows that these bounds are
far from the true value of N (n).

2.2. Caps and Cups - Better Upper Bounds. We will assume in this section
that a coordinate system (x, y) is introduced in the plane. Let X = {(x1,y1),
(x2,y2),... , (xm,ym)} be a set of points in general position in the plane, with
xi ̸= xj for all i ̸= j. A subset of points {(xi1 ,yi1 ), (xi2 ,yi2),... , (xir ,yir )} is
called in [16] an r-cup if xi1 <xi2 < ... < xir and

yi1 − yi2
xi1 − xi2 < yi2 − yi3
xi2 − xi3 < ... < yir−1 − yir
xir−1 − xir .

THE ERD ˝OS-SZEKERES PROBLEM ON POINTS IN CONVEX POSITION 441

t
 t
 t
❩
❩
❩
❩✚
✚
✚
✚
 t
 tt
 t✚
✚
✚
✚ ❩
❩
❩
❩

Figure 2.1. Examples of a 3-cup and a 4-cap.

Similarly, the subset is called an r-cap if xi1 <xi2 < ... < xir and

yi1 − yi2
xi1 − xi2 > yi2 − yi3
xi2 − xi3 > ... > yir−1 − yir
xir−1 − xir .

In other words, the set of r points forms an r-cup (respectively, an r-cap) pro-
vided the sequence of slopes of the segments

[(xi1 ,yi1 ), (xi2 ,yi2)], [(xi2 ,yi2), (xi3 ,yi3 )],... , [(xir−1 ,yir−1 ), (xir ,yir )]

is monotonically increasing (respectively, decreasing). See, e.g., Figure 2.1.
Deﬁne f (k, l) to be the smallest positive integer for which X contains a k-cup
or an l-cap whenever X has at least f (k, l)points.

Theorem 2.3 ([32]). f (k, l) ≤ (k+l−4
k−2 ) +1.

Proof. The inequality follows from the boundary conditions f (k, 3) = f (3,k)= k
and the recurrence f (k, l) ≤ f (k − 1,l)+ f (k, l − 1) − 1. We sketch a proof of the
recurrence.
Suppose that X contains f (k − 1,l)+ f (k, l − 1) − 1points. Let Y be the set
of left endpoints of (k − 1)-cups of X.If X \ Y contains f (k − 1,l)points, then it
contains an l-cap. Otherwise, Y contains f (k, l−1) points. Suppose that Y contains
an (l − 1)-cap {(xi1 ,yi1 ), (xi2 ,yi2),... , (xil−1 ,yil−1)}.Let {(xj1 ,yj1 ), (xj2 ,yj2 ),... ,
(xjk−1 ,yjk−1 )} be a (k − 1)-cup with il−1 = j1. A quick sketch then shows that
either (xil−2 ,yil−2) can be added to the (k − 1)-cup to create a k-cup or (xj2 ,yj2 )
can be added to the (l − 1)-cap to create an l-cap.

Because N (n) ≤ f (n, n), we get from Theorem 2.3 that N (n) ≤ (
2n−4
n−2 ) +1.
This upper bound was not improved upon until 63 years later, when Chung and
Graham [16] managed to modify the above argument to show that N (n) ≤ (
2n−4
n−2 )
.
A further modiﬁcation by Kleitman and Pachter [57] implied N (n) ≤ (
2n−4
n−2 ) +7 −
2n. Shortly thereafter, T´oth and Valtr [80] gave the following simple argument to
roughly cut the Erd˝os-Szekeres bound in half.

Theorem 2.4 ([80]). N (n) ≤ (2n−5
n−3 ) +2.

Proof. Let a be an extreme point of a planar set X.Denote by b a point outside of
convX so that no line determined by the points of X \{a} intersects the segment
[a, b]. Let l be a line through b that does not intersect convX. It is easily seen that
the projective transformation T that maps l to the line at inﬁnity and maps the
segment [a, b] to the vertical ray emanating downward from T (a) has the following
properties:
(i) a subset Y of X is in convex position if and only if T (Y )is,

442 W. MORRIS AND V. SOLTAN

(ii) a subset Z of X containing a is in convex position if and only if T (Z \ a)is
acap.
Suppose now that X contains (
2n−5
n−3 )+2 points. Then T (X \a) determines either
a(n − 1)-cap or a n-cup (see Theorem 2.3). This implies that X contains n points
in convex position.

Stirling’s formula shows that (
2n−5
n−3 ) is smaller than 4n and is, asymptotically,
larger than (4 − c)
n for any constant c> 0. Chung and Graham [16] have oﬀered
$100 for the ﬁrst proof that N (n)= O((4 − c)
n)for some constant c> 0. (They
oﬀer no money for showing that no such c exists.) The simplicity of the argument
of T´oth and Valtr [80] seems to indicate that further reductions in the upper bound
are within reach. On the other hand, substantially diﬀerent techniques might be
needed to claim the $100 prize.

2.3. Construction for the Lower Bound. We begin with a theorem that states
that the inequality for f (k, l) in Theorem 2.3 is actually an equality.

Theorem 2.5 ([32]). f (k, l)= (
k+l−4
k−2 ) +1.

Proof. Note that we have already observed this to be the case when k or l is 3.
We proceed by induction. Suppose that we have a set A of (
k+l−5
k−3 ) points with
no (k − 1)-cup and no l-cap, and a set B of (k+l−5
k−2 ) points with no k-cup and no
(l − 1)-cap. Translate these sets so that the following conditions are satisﬁed:
(i) every point of B has greater ﬁrst coordinate than the ﬁrst coordinates of
points of A,
(ii) the slope of any line connecting a point of A to a point of B is greater than
the slope of any line connecting two points of A or two points of B.
Let X = A ∪ B be the resulting conﬁguration. Any cup in X that contains
elements of both A and B may have only one element of B. It follows that X
contains no k-cup. We similarly see that X contains no l-cap. Thus

f (k, l) ≥ (k + l − 5
k − 3
 ) + (
k + l − 5
k − 2
 ) +1 = (k + l − 4
k − 2
 ) +1. ✷

Now we are ready to prove the inequality N (n) ≥ 2n−2 + 1. This lower bound
on N (n) was essentially proved in [33]. Some inaccuracies in the proof were later
corrected by Kalbﬂeisch and Stanton [51]. (Erd˝os refers to their corrections in [26].)
We sketch the main ideas of the construction as it is presented in [61].

Theorem 2.6 ([33],[51])). N (n) ≥ 2n−2 +1.

Proof. To prove the inequality, we construct a set X of 2n−2 points with no subset
of n points in convex position. For i =0, 1,... ,n − 2, let Ti be a set of (
n−2
i ) points
containing no (i + 2)-cap and no (n − i)-cup and having the property that no two
points in the set are connected by a line having slope of absolute value greater than
1. For i =0, 1,... ,n − 2, place a small copy of Ti in a neighborhood of the point
on the unit circle making an angle of π
4 − iπ
2(n−2) with the positive x-axis. Let X
be the union of the Ti, i =1, 2,... ,n − 2. Then

|X| =
 n−2∑

i=0
 (
n − 2
i
 ) =2n−2.

THE ERD ˝OS-SZEKERES PROBLEM ON POINTS IN CONVEX POSITION 443

Suppose that Y is a subset of X in convex position. Let k and l be the smallest
and the largest values of i so that Y ∩Ti ̸= ∅.If k = l,then Y contains no (k+2)-cap
and no (n − k)-cup. The construction guarantees that:
(a) Y ∩ Tk is a cap of at most k +1 points,
(b) Y ∩ Tl is a cup of at most n − l − 1points,
(c) |Y ∩ Ti|≤ 1 for all i = k +1,k +2,... ,l − 1.
Thus
 |Y |≤ k +1+ l − k − 1+ n − l − 1= n − 1.

Hence no subset of X in convex position contains n points.

An interesting conjecture was formulated by Erd˝os et al. [34] that connects the
proof of the upper bound on N (n) given in [32] to the conjectured lower bound on
N (n). Let m(n, k, l) be the smallest number such that any set of m(n, k, l)points in
general position in the plane contains either a set of n points in convex position, or a
k-cup, or an l-cap. It is proved in [34] that m(n, k, l) ≤ ∑k−2
i=n−l (
k−2
i )
. The authors
of [34] conjecture that equality holds and prove its equivalence to the conjecture
N (n)=2n−2 +1.

2.4. The case n =5. Erd˝os and Szekeres note already in [32] that Makai had
proved the equality N (5) = 9. Credit for this result is given in [33] to Makai and
Tur´an. A proof did not appear in the literature until Kalbﬂeisch et al. [50]. Since
their proof was rather long, Bonnice [12] and Lov´asz ([61], pp. 88–89, 501–506)
independently published much simpler proofs. In what follows we outline the proof
of Bonnice [12].

Theorem 2.7. N (5) = 9.

The proof of Theorem 2.7 is based on Lemma 2.8 below. Given a ﬁnite set
X of points in the plane, the statement that X is (k1,k2,... ,kj) will mean that
|X| = k1+k2+...+kj and the convex hull of X is a k1-gon; that, when the vertex set
of convX is taken away from X, the convex hull of the remaining points is a k2-gon;
etc. Also, if abcd is a convex quadrilateral with vertices ordered counterclockwise,
beam ab:cd denotes the section of the plane obtained by deleting conv{a, b, c, d}
from the convex section of the plane bounded by segment [a, b]and rays [a, d),
[b, c). Similarly, if x, y,and z are not collinear, beam x:yz will denote the inﬁnite
section of the plane obtained by deleting conv{x, y, z} from the convex cone which
has vertex x and is bounded by rays [x, y)and [x, z).

Lemma 2.8. If a planar set Y is (3, 3, 2),or (4, 3, 1),or (3, 4, 2),then Y deter-
mines a convex pentagon.

Proof. First, assume that Y is (3, 3, 2). Let y1,y2,y3 be the vertices of convY ;let
triangle v1v2v3 be the second triangle, conv(Y \{y1,y2,y3}); and let z1,z2 be the
two points of Y interior to v1v2v3. We may assume that line (z1,z2) intersects sides
[v1,v2]and [v1v3]of v1v2v3 such that [z1,z2) intersects [v1,v2).
The vertices y1,y2,and y3 of the outside triangle are in the union of beams
z1z2:v2v3, z1:v1v3,and z2:v1v2. If one of these vertices, say y1,isin beam z1z2:v2v3,
then z1z2v2y1v3 is a convex pentagon. Thus we may assume that two of the
points y1,y2,y3,say y1 and y2,are in beam z1:v1v3. Since conv{y1,y2,y3} con-
tains all of v1,v2,v3, triangle v1v2v3 lies in one of the open half-planes determined

444 W. MORRIS AND V. SOLTAN

t
 tt
 t

t tt t

Figure 2.2. A set of eight points determining no convex pentagon.

by line (y1,y2). Thus line (y1,y2) does not intersect conv{v1,v2,v3}, and therefore
z1v1v3y1y2 is a convex pentagon.
Now assume that Y is (4, 3, 1). Let y1,y2,y3,and y4 be the vertices of convY ;let
v1v2v3 be theinsidetriangle, conv(Y \{y1,y2,y3,y4}); and let z denote the point
of Y inside it. Partitioning the plane outside v1v2v3 into beams z:v1v3, z:v1v2,and
z:v2v3, we may assume that two of the four points y1,y2,y3,y4,say y1 and y2,are
in beam z:v1v3. Then, as above, zv1v3y1y2 is a convex pentagon.
Finally, assume that Y is (3, 4, 2). The technique is the same: let y1y2y3,
v1v2v3v4,and z1z2 be the triangle, quadrilateral, and line segment given by the
fact that Y is (3, 4, 2). If line (z1,z2)cuts a vertex, say v1,of v1v2v3v4,then
z1z2v2v3v4 is a convex pentagon. So assume that line (z1,z2)cuts sides [v1,v4]and
[v2,v3] such that rays [z1,z2)and [v2,v3) intersect. As above, if there is a point of
{y1,y2,y3} in one of the beams z1z2:v3v4, z2z1:v1v2, a convex pentagon is formed.
Thus we may assume that {y1,y2,y3} lies in the union of beams z1:v1v4 and z2:v2v3.
In particular, we may assume that both y1 and y2 are in z1:v1v4; whence, as before,
z1v1v4y1y2 is a convex pentagon.

Proof of Theorem 2.7. If a set of nine points in general position in the plane deter-
mines no convex pentagon, it is one of the following: (4, 4, 1), (4, 3, 2), (3, 4, 2), or
(3, 3, 3). Each of the ﬁrst two cases has a subset of 8 points which is (4, 3, 1), and
each of the last two cases has a subset which is (3, 3, 2). Thus Lemma 2.8 applies to
all cases to show that N (5) ≤ 9. The opposite inequality easily follows from Figure
2.2.

As mentioned by Bonnice [12], the same approach can hardly be applied to the
case n = 6. Indeed, assuming that N (6) = 17, one can see that a set X of 17
points in the plane can determine 70 distinct tuples (k1,k2,... ,kj)representing
the diﬀerent ways the successive convex hulls of X might nest if it determines no
convex hexagon.
 3. The Erd˝os problem on empty polygons

In 1978 Erd˝os [27], [28], [29] posed a new problem on convex polygons.

Problem 3.1 ([27]). For any positive integer n ≥ 3, determine the smallest posi-
tive integer H(n), if it exists, such that any set X of at least H(n) points in general
position in the plane contains n points which are the vertices of an empty convex
polygon, i.e., a polygon whose interior does not contain any point of X.

THE ERD ˝OS-SZEKERES PROBLEM ON POINTS IN CONVEX POSITION 445

t
 t
 t
 t

t

t

t
 t t

Figure 3.1. A set of nine points with no empty convex pentagon.

Trivially, H(3) = 3, and from Figure 1.1 we easily conclude that H(4) = 5.
Using a direct geometric approach, Harborth [43] showed in 1978 that H(5) = 10.
The inequality H(5) ≥ 10 immediately follows from Figure 3.1, where a set of nine
points in general position determines no empty convex pentagon (there are still two
convex pentagons, neither being empty).
In 1983 Horton [46] showed that H(n) does not exist for all n ≥ 7. This statement
is due to the following analytic construction of a planar set Sk of 2k (k ≥ 1) points in
general position determining no empty convex 7-gon. Let a1a2 ··· ak be the binary
representation of the integer i,0 ≤ i< 2k, where leading 0’s are omitted. Put c =
2k + 1 and deﬁne d(i)= ∑k
j=0 ajcj−1. Now a simple analytical consideration shows
that any convex polygon determined by the set Sk = {(i, d(i)) : i =0, 1,... , 2k − 1}
has at most six vertices.
Valtr [82] deﬁnes a Horton set inductively as follows. The empty set and any
one-point set are Horton sets. The points of a Horton set H are in general position
in the plane, with distinct x-coordinates. Furthermore, H can be partitioned into
two sets A and B such that:
1. Each of A and B is a Horton set.
2. The set A is below any line connecting two points of B,and the set B lies
above any line connecting two points of A.
3. The x-coordinates of the points of A and B alternate.
One can easily prove by induction on n = |H| that if {(x1,y1), (x2,y2), (x3,y3),
(x4,y4)} is a 4-cup (respectively, 4-cap) in H, then there is a point (x, y)of H lying
above (respectively, below) one of the segments [(xi,yi), (xi+1,yi+1)],i =1, 2, 3. It
immediately follows that H contains no empty 7-gon, because otherwise A would
contain a 4-cup or B would contain a 4-cap.
Note that the above sets Sk ﬁt the deﬁnition of Horton sets. Valtr [82], [83] uses
Horton sets in several generalizations of the empty polygon problem, as we will see
in Sections 4 and 5.
In this connection the following question of Erd˝os [29] (and later of Horton [46])
still remains open.

Question 3.2. Does the number H(6) exist?

446 W. MORRIS AND V. SOLTAN

Horton [46] expresses the belief that H(6) exists. B´ar´any and Valtr [86] present
a conjecture which would imply the existence of H(6). Trying to determine the
lower bound on H(6), Avis and Rappaport [3] elaborated a method to determine
whether a given set of points in the plane contains an empty convex 6-gon, and by
using this approach they found a set of 20 points in general position containing no
empty convex 6-gon.
Overmars et al. [67], modifying considerations of Dobkin et al. [22], constructed
an algorithm of time complexity O(n2) that solves the following problem: for a
given set V in the plane, containing no empty convex 6-gon, and for a point z ̸∈ V ,
determine whether the set {z}∪ V contains an empty convex 6-gon. Using this
algorithm, they found a set of 26 points containing no empty convex 6-gon. Hence,
H(6) ≥ 27, if it exists.
As with the original Erd˝os-Szekeres problem, the theory for the empty polygon
problem is limited to that which can be proved using cups and caps. There remains
once again a large gap that probably will require some new paradigms to be bridged.

4. Higher dimensional extensions

4.1. The Erd˝os-Szekeres Problem in Higher Dimensions. An observation
that the Erd˝os-Szekeres problem can be generalized for higher dimensions was al-
ready mentioned by its authors (see [32]) and later rediscovered by Danzer et al.
[21]. Recall that a set X of points in Euclidean space Ed is in general position if
no d +1 points of X lie in a hyperplane. (Clearly, a set X is in general position
if and only if for any positive integer k,1 ≤ k ≤ d,no k +1 points of X lie in a
k-dimensional plane.) Furthermore, X is said to be in convex position if no point
of X lies in the convex hull of the remaining points. In other words, a set X in
general position is in convex position if and only if it is the vertex set of a convex
d-polytope in Ed.
Following [21], we deﬁne Nd(n),d ≥ 2,n ≥ 1 to be the smallest positive integer
such that any set of Nd(n) points in general position in Ed contains n points
in convex position. Similarly to the planar case, one can pose the following two
problems:
1) Do the numbers Nd(n) exist for all d ≥ 2 and n ≥ 1?
2) If yes, what are the values of Nd(n)?
The existence of Nd(n) can be established analogously to the planar case (see
Section 1) by implementing the following steps:
(a) A set X of at least d + 2 points in general position in Ed is in convex position
if and only if any d + 2 of them are in convex position. (This fact is a direct
consequence of Carath´eodory’s theorem [14]: a point z belongs to the convex hull
of a set A ⊂ Ed if and only if z belongs to the convex hull of at most d +1 points
of A.)
(b) Any set of d + 3 points in general position in Ed contains d + 2 points in
convex position. (A stronger version of this statement was proved by Motzkin [63];
see also [64], who showed that the number of nonconvex (d + 2)-subsets of a general
(d +3)-set in Ed equals either 0, or 2, or 4 for all d ≥ 2.)
(c) If Rd+2(n, d + 3) is a Ramsey number, then any set of Rd+2(n, d +3) points
in general position in Ed contains n points in convex position. (This statement is
a direct generalization of the original proof by Erd˝os and Szekeres for the planar
case.)
 THE ERD ˝OS-SZEKERES PROBLEM ON POINTS IN CONVEX POSITION 447

As a result, we conclude that the numbers Nd(n) exist for all positive integers
d ≥ 2and n ≥ 1, and Nd(n) ≤ Rd+2(n, d +3).
Valtr [85] gave another idea for proving the existence of numbers Nd(n). He
considers any set X of at least N2(n) points in general position in Ed and its
projection Y onto a two-dimensional subspace L ⊂ Ed such that Y is in general
position in L.Since |Y |≥ N2(n), one can select in Y a subset of n points in convex
position. It is easily seen that the prototypes of these points in X are in convex
position. This consideration implies the inequality Nd(n) ≤ N2(n),d ≥ 2. A similar
consideration is true for the case of an m-dimensional plane in Ed,2 <m <d.
Hence we obtain

Nd(n) ≤ Nd−1(n) ≤ ... ≤ N2(n) ≤ (
2n − 5
n − 3
 ) +2.

K´arolyi [52] has recently proved that Nd(n) ≤ Nd−1(n − 1) + 1, and this implies

Nd(n) ≤ (
2n − 2d − 1
n − d
 ) + d.

The paper [52] also contains the intriguing result that for any n ≥ 1and d ≥ 3
there is a smallest integer Md(n)so thatif P is any set of Md(n) points in general
position in Ed and if p ∈ P , then there is a subset of P consisting of n points in
convex position and containing p.
Johnson [49] showed that his proof of the existence of N (n) can be modiﬁed to
get Nd(n) ≤ Rd+1(n, n,... ,n), where the last term has d − 1copiesof n.We note
here that no one has yet succeeded in generalizing the “caps and cups” arguments
of Erd˝os and Szekeres [32] for the case d ≥ 3.
The only known general lower bound for Nd(n) is due to K´arolyi and Valtr [54].
They prove that for each d ≥ 2 there exists a constant c = c(d)so that

Nd(n)= Ω(c d−1√n).

Table 4.1 shows the known values of Nd(n), where the respective value is placed
at the intersection of column d and row n.
Indeed, the equalities Nd(n)= n if n ≤ d + 1 are trivial, and Nd(d +2) = d +3,
mentioned by Danzer et al. [21] (see also Gr¨unbaum [40]), was proved by Motzkin
[63]. We note here that the equality N2(4) = 5, which is due to Klein, is a particular
case of Nd(d+2) = d+3. The next range of values of Nd(n) is given by the following
new theorem.

Theorem 4.1. Nd(n)=2n − d − 1 for d +2 ≤ n ≤⌊3d/2⌋ +1.

Proof. As a consequence of a stronger assertion by Bisztriczky and Soltan [11] (see
Section 4.2 below) one has Nd(n) ≤ 2n − d − 1for d ≥ 2and d +2 ≤ n ≤
⌊3d/2⌋ +1. For any n ≥ d + 2, Bisztriczky and Harborth [10] constructed a set
X = {x1,x2,... ,x2n−d−3} in Ed so that X ∪{o} is in general position and every
set of n − 1pointsof X contains the origin o of Ed in the interior of its convex hull.
They showed that no set of n points of X ∪{o} could be the set of vertices of an
empty convex polytope.
If we now scale the points of X by positive scalars λi so that for each i ≥ n, λixi
is in the interior of the convex hull of every set of n − 1points of {λ1x1,λ2x2,... ,
λi−1xi−1}, one can similarly see that no set of n points of {λ1x1,λ2x2,... ,
λ2n−d−3x2n−d−3,o} is in convex position. Thus Nd(n) ≥ 2n−d−1for n ≥ d+2.

448 W. MORRIS AND V. SOLTAN

n

14 18
13 17 16
12 15 14
11 14 13 12
10 13 12 11 10
9 11 10 9 9
8 109888
7 987777
6 9 766666
5 9 6 555555
4 5 4 444444
3 3 3 333333
2 2 2 222222
1 1 1 111111
2 3 456789 ... d

Table 4.1. Known values of Nd(n)when d< 10.

For n> ⌊3d/2⌋ + 1, there are known only two values of Nd(n): N2(5) = 9; see
Section 2 and N3(6) = 9, due to Bisztriczky and Soltan [11]. Their proof is similar
to that of Bonnice and is based on selecting three subsets, P, Q, R, of a set X ⊂ E3

of 9 points in general position such that

P =ext convX, Q =ext conv(X \ P ),R =ext conv(X \ (P ∪ Q)).

Considering separately the cases
(i) |P |≥ 6,
(ii) |P | =5 and |Q| =4,
(iii) |P | =4 and |Q| =5,
(iv) |P | =4, |Q| =4, and |R| =1,
they show each time the existence of a subset of 6 points in X in convex position.
It is interesting to mention that all the known values of Nd(n), with d ≥ 2and
n> ⌊(3d +1)/2⌋, satisfy the equality Nd(n)= 4Nd(n − d) − 3. This also agrees
with the conjecture N2(n)= 2n−2 +1 of Erd˝os and Szekeres. We therefore oﬀer
the following conjecture.

Conjecture 4.2. Nd(n)= 4Nd(n − d) − 3 for all d ≥ 2 and n> ⌊(3d +1)/2⌋.

Gr¨unbaum ([40], pp. 22-23) discovered a variant of the Erd˝os-Szekeres problem
in higher dimensions. Namely, he established the existence of the minimum number
Bd(n),d ≥ 2and n ≥ 1, such that any set X ⊂ Ed consisting of at least Bd(n)
points in general position contains a subset of n points lying on the boundary of
aconvex body in Ed. His proof is based on Ramsey’s theorem and the following
assertion: a ﬁnite set Y ⊂ Ed lies on the boundary of a convex body in Ed if and
only if each of its subsets of at most 2d + 1 points lies on the boundary of a convex
body in Ed. The last statement is a direct consequence of the Steinitz theorem
[77]: a point z ∈ Ed belongs to the interior of the convex hull of a set S ⊂ Ed if
and only if z belongs to the interior of the convex hull of at most 2d points of S.

THE ERD ˝OS-SZEKERES PROBLEM ON POINTS IN CONVEX POSITION 449

Later Bisztriczky and Soltan [11] showed that in the deﬁnition of Bd(n)the set
X ⊂ Ed can be arbitrary (not necessarily in general position), and they also proved
the equality Bd(n)= Nd(n) for all d ≥ 2and n ≥ 1. Their proof is based on
a simple idea that any ﬁnite set in Ed can be approximated by a set in general
position.

4.2. Empty Convex Polytopes. Generalizing the Erd˝os problem on empty con-
vex polygons (see Section 2), Bisztriczky and Soltan [11] deﬁned Hd(n)to be the
smallest positive integer, if it exists, such that any set X of Hd(n) points in general
position in Ed contains a subset of n points that are the vertices of an empty convex
polytope, i.e., a polytope whose interior does not contain any point of X.
Valtr [83] proved the following deep results on the existence of Hd(n), generaliz-
ing considerations of Horton [46].
1) Hd(n) exists for all n ≤ 2d +1, d ≥ 2, and Hd(2d +1) ≤ Nd(4d +1);
2) H3(n) does not exist for all n ≥ 22;
3) Hd(n)does not exist if n ≥ 2d−1(P (d − 1) + 1) and d ≥ 4, where P (d − 1) is
the product of the ﬁrst d − 1prime numbers.
By using simple geometric arguments, Bisztriczky and Soltan [11] showed that
Hd(n) ≤ 2n − d − 1for d +2 ≤ n ≤⌊3d/2⌋ + 1. Later Bisztriczky and Harborth
[10] proved the opposite inequality Hd(n) ≥ 2n − d − 1if Hd(n) exists. Their proof
is based on the construction of a set X ⊂ Ed of cardinality 2n − d − 3 such that
the intersection of all convex hulls of subsets Y ⊂ X, |Y | = n − 1, is nonempty.
Combining the results of [10], [11] and Theorem 4.1, one gets

Hd(n)= Nd(n)= 2n − d − 1for d ≥ 2and d +2 ≤ n ≤⌊3d/2⌋ +1.(1)

For n> ⌊3d/2⌋ + 1, there are known only two values of Hd(n): H2(5) = 10, proved
by Harborth [43], and H3(6) = 9, proved by Bisztriczky and Soltan [11].
Since H3(6) can be considered as a particular case of Hd(⌊(3d +1)/2⌋ +1), we
pose the following problem.

Problem 4.3. Determine the value of Hd(⌊(3d +1)/2⌋ +1).

Due to equality (1), it is suﬃcient to consider in the problem above the case
when d is odd: e.g. the numbers H5(9), H7(12), H9(15), etc.
Some problems on the existence of empty convex polytopes in a two-colored set
of points in Ed are considered by Borwein [13].

5. Other generalizations and related results

5.1. Many Convex n-gons. After the existence of convex n-gons has been proved,
it is natural to ask how many there are. For a planar point set of r points in general
position there are, of course, (
r
3
) triangles determined by the set. The number of
convex quadrilaterals formed by such a set is positive, for r ≥ 5, as noted by Klein
[32]. To show that the number of such convex quadrilaterals is at least (
r−2
3 ) was
a problem in the Eleventh International Mathematical Olympiad, Bucharest, 1969
(see [88], [89], and [12]).
More generally, we can pose the following problem.

Problem 5.1. Determine the minimum number of convex n-gons in a planar set
of r points in general position.

450 W. MORRIS AND V. SOLTAN

Clearly, a similar problem can be posed for higher dimensions.
B´ar´any and Valtr [5] proved that suﬃciently large planar point sets have many
collections of subsets in convex position of a given size n.

Theorem 5.2 ([5]). For every integer n ≥ 4 there is a constant cn > 0 with the
property that every suﬃciently large ﬁnite planar set X in general position contains
n subsets Y1,... ,Yn with |Yi|≥ cn|X|,i =1,... ,n, such that any set {y1,... ,yn}
satisfying yi ∈ Yi for all i =1,... ,n is in convex position.

Special cases of this theorem were previously proved by Solymosi [76] and Nielsen
[66]. The inﬁmum of the constants cn for which Theorem 5.2 is true is shown in [5]
to be at least (N (n)2(
N (n)−1
2 ))−1 .

A note at the end of [5] states that Solymosi has proved the inequality cn ≥ 2−16n
2.
Also proved in [5] is c4 ≥ 1
22 .
Erd˝os notes in [27] that a discussion with P. Hammer prompted him to study
the function s(r), the minimum number of convex subsets (of any number n ≥ 3
of points) contained in a set of r points in general position in the plane. Erd˝os
proves [27] that there exist constants a and b so that ralogr <s(r) <rblogr. He
also speculates that limn→∞ logs(r)/(logn)
2 exists.
The problem of counting the number of empty n-gons has received considerable
interest. Let fn(r) denote the minimum number of empty n-gons in a set of r points
in general position in the plane. Note that Horton [46] proved fn(r)=0 for n ≥ 7.
Purdy [71] announced the equality f3(r)= O(r2), while Harborth [43] showed that
f3(r)= r2 − 5r +7 for 3 ≤ r ≤ 9and f3(10) = 58.
Katchalski and Meir [55] continued the investigation of fn(r) for smaller n by
proving that (n
2) ≤ f3(r) ≤ Kr2 for some constant K< 200. B´ar´any and F¨uredi
[4] followed up on the work of Katchalski and Meir by proving some new bounds:

r2 − O(rlogr) ≤ f3(r) ≤ 2r2, 1
4 r2 − O(r) ≤ f4(r) ≤ 3r2,

⌊ r
10 ⌋≤ f5(r) ≤ 2r2,f6(r) ≤ 1
2 r2.

The upper bounds were improved by Valtr [84], and later by Dumitrescu [23], to

f3(r) < 1.68r2,f4(r) < 2.132r2,f5(r) < 1.229r2,f6 < 0.298r2.

Valtr [84] mentioned personal correspondence from B´ar´any in which a lower bound
of f4(r) ≥ 1
2 r2 − O(r)is given.
We close this section by mentioning the papers by Ambarcumjan [2], Karolyi
[52], Hosono and Urabe [47], and Urabe [81], which deal with some combinatorial
problems on clustering of ﬁnite planar sets, i.e. partitioning a set into subsets in
convex position.

5.2. Replacing Points with Convex Bodies. Bisztriczky and Fejes T´oth (see
[7], [8], [9]) showed that the Erd˝os-Szekeres problem has a generalization for the
case of convex bodies in the plane. We say that a family of pairwise disjoint convex
bodies is in convex position if none of its members is contained in the convex hull
of the union of the others.

THE ERD ˝OS-SZEKERES PROBLEM ON POINTS IN CONVEX POSITION 451

Theorem 5.3 ([7]). For any integer n ≥ 4, there is a smallest positive integer g(n)
such that if F is a family of pairwise disjoint convex bodies in the plane, any three
of which are in convex position and |F | >g(n), then some n convex bodies of F
are in convex position.

The authors prove the existence of g(n) using Ramsey’s theorem. They also
made the bold conjecture that g(n)= N (n) − 1. This conjecture is supported in
[8], where it is shown that g(5) = 8.
A family F of convex bodies in the plane is said to have property H n
k ,for
3 ≤ k< n,ifevery setof k elements of F is in convex position and no n of them
are in convex position. The third paper [9] of these authors is devoted to studying
h(k, n), which is the maximum cardinality of a family of mutually disjoint convex
bodies satisfying property H n
k . Clearly, h(k, n) ≤ h(3,n)= g(n), so h(k, n)exists
for all 3 ≤ k< n. An upper bound h(4,n) ≤ (n − 4)
(
2n−4
n−2 ) − n + 7, similar to the
bound of [32] on N (n), is proved. This is shown to imply the (very large) upper
bound
 g(n) ≤ R4((n − 4)
(
2n − 4
n − 2
 ) − n +8, 5).

Smaller upper bounds are derived in [9] for h(k, n)if k ≥ 5.
The bounds on h(k, n) from [9] are considerably improved by Pach and T´oth
[69], [79]. The best known bounds are

2n−2 ≤ h(3,n) ≤ (
2n − 4
n − 2
 )2, 2⌊ n +1
4 ⌋2 ≤ h(4,n) ≤ n3,

n − 1+ ⌊ n − 1
3 ⌋≤ h(5,n) ≤ 6n − 12,

n − 1+ ⌊ n − 1
k − 2 ⌋≤ h(k, n) ≤ k − 4
k − 5 n, k > 5.

Pach and Solymosi [68] extend the results of B´ar´any and Valtr (see Section 5.1),
replacing points by compact convex sets. Speciﬁcally, they prove that for every
n ≥ 4 there is a positive constant cn =2O(n
2), so that the following is true: every
family F of r pairwise disjoint compact convex sets in general position in the plane
has n disjoint ⌊cnr⌋-membered subfamilies Fi, 1 ≤ i ≤ n, such that no matter how
we pick one set from each Fi, they are always in convex position. Note that the
exponent for cn here is better than that of [5].
Recent research by Pach and T´oth [70] investigates Erd˝os-Szekeres type problems
in which the points are replaced by convex sets that are not necessarily disjoint.

5.3. Restricted Planar Point Sets. The size of the coordinates of the points in
the conﬁgurations given by Kalbﬂeisch and Stanton [51] that meet the conjectured
upper bound on N (n) grows very quickly. A step toward showing that this is
unavoidable was taken by Alon et al. [1].
Suppose that X is a set of points in the plane, with no three on a line. Let
q(A) be the ratio of the largest distance between two points of X to the smallest
distance between two points of X. The authors of [1] prove that if |X| = k and
q(X) ≤ α
√
k, then there is a constant β, depending on α,so that X contains a
subset of size at least βk 1
4 in convex position. In other words, the restriction of

452 W. MORRIS AND V. SOLTAN

the Erd˝os-Szekeres problem to point sets with relatively uniform distances between
points yields a function N (n)thatis atmost a fourth-degree polynomial.
The results of [1] were improved by Valtr [82]. Under the same conditions,
|X| = k and q(X) ≤ α
√k, Valtr shows that there is a constant β = β(α)so
that X contains a subset of size at least βk 1
3 in convex position. Furthermore, he
constructs, for any c> 5.96 and k large enough, a set Ak of k points with no subset
in convex position larger than ck 1
3 . The sets Ak have the property that they contain
no empty convex 7-gons.

5.4. Polygons That Are Empty Modulo q. Recall that Horton [46] proved the
existence of arbitrarily large sets of points in general position in the plane that
contain no empty convex 7-gons. In view of this, the following conjecture of [6] is
surprising.

Conjecture 5.4. For any two positive integers q and n, n ≥ 3,there is a smallest
positive integer C(n, q) so that any set X of C(n, q) points in general position in the
plane contains a subset n points in convex position for which the number of points
of X in its interior is divisible by q.

Bialostocki et al. prove in[6] that theconjectureis trueinthe cases n ≡ 2(mod q)
and n ≥ q + 3. Extremely large upper bounds on C(n, q) in both cases are obtained
by the Ramsey theoretic argument.
Caro [15] found a better upper bound that also holds for a more general function.
Let X be a set of points in general position in the plane, and let G be an abelian
group. If w is a function from X to G and K is a subset of X in convex position,
then K is said to have zero-sum interior modulo G if
∑

x∈interiorK w(x)=0 (in G).

Theorem 5.5 ([15]). For any two integers n and q, n ≥ q +2, there is an integer
E(n, q) satisfying the following conditions:
(1) Let X be a set of points in general position in the plane, and let G be an
abelian group of order q. Assume w : X → G.Then |X|≥ E(n, q) implies that X
contains a set of n points in convex position that has zero-sum interior.
(2) For a given q, one has E(n, q) ≤ 2c(q)n,where c(q) depends only on q but
not on n or the structure of G.

Caro [15] speculates that the bound for E(n, q) can be considerably improved
when n ≥ q + 2. A recent result of K´arolyi et al. [53] is that Conjecture 5.4 is true
for n ≥ 5
6 q + O(1).

5.5. Duality. The Erd˝os-Szekeres problem has a dual one in terms of arrangements
of lines in the plane. Attention to this equivalent problem was ﬁrst drawn by
Goodman and Pollack [37]. An arrangement of lines is called simple if no two of
the lines are parallel and no three of them meet in a point. The dual problem is
then to determine the smallest integer N (n) so that every simple arrangement of
N (n) lines together with a point q not on any line contains a sub-arrangement of
n lines for which the cell containing q is a convex n-gon.
One generalization is to consider the smallest integer p(n)so thatevery simple
arrangement of p(n) lines contains a sub-arrangement of n lines determining a
convex n-gon. Harborth and M¨oller [44] show that this problem is only interesting

THE ERD ˝OS-SZEKERES PROBLEM ON POINTS IN CONVEX POSITION 453

if the arrangements are considered to be in the projective plane. To do this, one
identiﬁes opposite unbounded cells of the arrangements. It is trivially true that
p(n) ≤ N (n). It is shown in [44] that p(6) = 9 and p(n) ≥ 1+2 k+1
2 .
A second generalization is to replace the lines by pseudolines. Goodman and
Pollack [36] conjectured that the inequality N (n) ≤ 2n−2 + 1 holds even if “lines”
in the dual Erd˝os-Szekeres problem are replaced by “pseudolines”. If we denote by
Nps(n) the analogous function for pseudolines, one can see that the arguments of
[32] and [80] remain valid and show that Nps(n) ≤ (
2n−5
n−2 ) + 2. A non-stretchable
arrangement of 16 lines for which no subarrangement of 6 lines forms a polygon
containing a speciﬁed point is given by Morris [62]. Harborth and M¨oller also ask
if the function p(n) of their problem is altered by substituting pseudolines for lines.

5.6. Generalized Convexity. Many of the known results on the Erd˝os-Szekeres
problem have been proved using only some very simple combinatorial properties of
the plane. It is natural to ask what the most general framework is for studying this
problem. One such framework is that of generalized convexity (see the books by
Soltan [75] and Van de Vel [87] for an overview of this topic).
We start with a ﬁnite set X and a collection F of subsets of X. The pair (X, F )
is called a convexity on X if the following hold:
1) ∅ and X are in F ,
2) F is closed under intersection.
For any subset A of X, deﬁne co(A) to be the smallest member of F containing
A. A subset A of X is called convexly independent if a/∈ co(A \ a) for all a ∈ A.
Aset X of points in Ed is said to realize aconvexity (X, F )if A ∈F precisely
when A = K ∩ X for some convex subset K of Ed.If (X, F ) is realizable and
satisﬁes a nondegeneracy assumption, then we have seen that there is a function
N (n)sothat X contains a convexly independent set of size n whenever |X|≥ N (n).
For nondegeneracy, one simply stipulates that, for some k, all subsets of X of size
at most k are convexly independent. One would like to replace the condition of
realizability by a simpler combinatorial condition.
Aconvexity (X, F )is said to have the anti-exchange property if for any subset
A of X and x, y /∈ co(A), x ∈ co(A ∪ y) implies y/∈ co(A ∪ x). Several names have
been given to convexities with the anti-exchange property, most notably convex
geometry (see [24]) and antimatroid (see [59]). Note that Coppel [19] uses the term
convex geometry to refer to a diﬀerent set of axioms.
A basis of a set A ⊆ X is a minimal set B ⊆ A such that co(B)= co(A). The
anti-exchange property is equivalent to the property that every set A ⊆ X has a
unique basis. The anti-exchange property by itself is not a strong enough property
to provide a structure in which one can carry through Szekeres’ Ramsey-theoretic
proof of the Erd˝os-Szekeres theorem. We will see that the addition of one more
property is suﬃcient for this purpose.
The Carath´eodory number of a convexity F is the least positive integer c such
that co(Y )= ∪{co(Z): Z ⊆ Y, |Z|≤ c} for any Y ⊆ X. Aset Y ⊆ X is said to be
in nice position if any c points of Y are convexly independent.
Let c be the Carath´eodory number of a convexity (X, F ). We say that (X, F )
satisﬁes the simplex partition property if for any set {z1,z2,... ,zc+2} of c +2
points in nice position, with {zc+1,zc+2}⊆ co(z1,... ,zc), the point zc+2 belongs
to exactly one of the sets co(z1,... ,zi−1,zc+1,zi+1,... ,zc),i =1,... ,c.

454 W. MORRIS AND V. SOLTAN

Lemma 5.6. Let convexity (X, F ) satisfy the anti-exchange property and the sim-
plex partition property. Any set of c +2 points of X in nice position contains c +1
convexly independent points.

Proof. Let {z1,... ,zc+2} be a set of points of X in nice position. We may as-
sume that zc+2 ∈ co(z2,z3,... ,zc+1)and zc+1 ∈ co(z1,z3,z4,... ,zc,zc+2). We
then claim that A = {z1,z2,z4,... ,zc+2} is convexly independent. The simplex
partition property implies that zi /∈ co(A\zi)for i = c +1,c +2. The anti-exchange
property implies that zi /∈ co(A\zi)for i =1, 2, 4,... ,c.

Theorem 5.7. Let (X, F ) be a convexity with the anti-exchange property and the
simplex partition property, and with Caratheodory number c ≥ 3. Then for any
positive integer n there exists a positive integer N (n) such that any set Y ⊆ X of
N (n) points in nice position contains n convexly independent points.

Proof. Put N (n)= Rc+1(n, c +2).

Another variant of the Erd˝os-Szekeres theorem for convexities satisfying almost
the same properties as the above theorem is given by Korte and Lov´asz [58].
If (X, F ) is a convexity, then a set A ⊆ X is called free if it is both convexly
independent and a member of F . For realizable (X, F ), a freeset is theset of
vertices of an empty convex polytope. The Helly number of (X, F ) is the smallest
integer h such that for any subfamily B of F ,ifeach h or fewer members of B have
nonempty intersection, then the intersection of all members of B is nonempty. It
is proved in [48] that the Helly number of a convexity is always at least as large
as the cardinality of its largest free set. If the convexity satisﬁes the anti-exchange
property, however, these two numbers are equal.
An interesting problem seems to be to ﬁnd an inﬁnite sequence of convexities
{(Xi, Fi)} so that |Xi| = i,each (Xi, Fi) satisﬁes combinatorial conditions that “al-
most” imply realizability in general position in the plane, and no (Xi, Fi)contains
a free set of cardinality 6.
 6. Acknowledgement

The authors would like to thank the referees for their insightful comments and
for information on some as yet unpublished research.

References

[1] Alon N., Katchalski M., Pulleyblank W.R., The maximum size of a convex polygon
in a restricted set of points in the plane, Discrete Comput. Geom. 4 (1989), 245–251.
MR 91a:52006
[2] Ambarcumjan R.V., Convex subclusters of point clusters in the plane, (Russian) Dokl. Acad.
Nauk Armjan. SSR 43 (1966), 12–14. MR 34:8277
[3] Avis D., Rappaport D., Computing the largest empty convex subsets of a set of points,
Proc. First ACM Symp. Comput. Geom. Baltimore, 1985, pp. 161–167.
[4] B´ar´any I., F¨uredi Z., Empty simplices in Euclidean space, Canad. Math. Bull. 30 (1987),
436–445. MR 89g:52004
[5] B´ar´any I., Valtr P., A positive fraction Erd˝os–Szekeres theorem, Discrete Comput. Geom.
19 (1998), 335–342. MR 99a:52024
[6] Bialostocki A., Dierker P., Voxman B., Some notes on the Erd˝os–Szekeres theorem,
Discrete Math. 91 (1991), 231–238. MR 92k:52034
[7] Bisztriczky T., Fejes T´oth G., A generalization of the Erd˝os–Szekeres convex n-gon the-
orem, J. Reine Angew. Math. 395 (1989), 167–170. MR 90b:52005

THE ERD ˝OS-SZEKERES PROBLEM ON POINTS IN CONVEX POSITION 455

[8] Bisztriczky T., Fejes T´oth G., Nine convex sets determine a pentagon with convex sets
as vertices, Geom. Dedicata 31 (1989), 89–104. MR 90h:52003
[9] Bisztriczky T., Fejes T´oth G., Convexly independent sets, Combinatorica 10 (1990), 195–
202. MR 92c:52005
[10] Bisztriczky T., Harborth H., On empty convex polytopes, J. Geom. 52 (1995), 25–29.
MR 95m:52038
[11] Bisztriczky T., Soltan V.,Some Erd˝os-Szekeres type results about points in space,
Monatsh. Math. 118 (1994), 33–40. MR 95e:52026
[12] Bonnice W.E., On convex polygons determined by a ﬁnite planar set, Amer. Math. Monthly
81 (1974), 749–752. MR 50:8301
[13] Borwein P.B., On monochromatic triangles, J. Combin. Theory Ser. A 37 (1984), 200–204.
MR 85h:52013
[14] Carath´eodory C., ¨Uber den Variabilit¨atsbereich der Fourierschen Konstanten von positiven
harmonischen Funktionen, Rend. Circ. Mat. Palermo 32 (1911), 193–217.
[15] Caro Y., On the generalized Erd˝os-Szekeres conjecture – a new upper bound, Discrete Math.
160 (1996), 229–233. MR 97h:52023
[16] Chung F.R.L., Graham R.L., Forced convex n-gons in the plane, Discrete Comput. Geom.
19 (1998), 367–371. MR 99e:52020
[17] Chung F.R.L., Graham R.L., Erd˝os on Graphs. His Legacy of Unsolved Problems. A. K.
Peters, Ltd., Wellesley, MA, 1998. MR 99b:05031
[18] Chv´atal V., Klincsek G., Finding largest convex subsets, Congr. Numer. 29 (1980), 453–
460. MR 82i:52001
[19] Coppel W. A., Foundations of Convex Geometry, Cambridge University Press, Cambridge,
1998, 222 pp. MR 99f:52001
[20] Croft H.T., Falconer K.J., Guy R.K., Unsolved Problems in Geometry, Springer-Verlag,
New York, 1991. (Corrected reprint: Springer-Verlag, New York, 1994) MR 92c:52001;
MR 95k:52001
[21] Danzer L., Gr¨unbaum B., Klee V., Helly’s theorem and its relatives, pp. 101–179. Convexity
(Seattle, 1961), Proc. Symp. Pure Math. Vol. VII. Amer. Math. Soc., Providence, R.I., 1963.
MR 28:524
[22] Dobkin D.P., Edelsbrunner H., Overmars M., Searching for empty convex polygons,
Algorithmica 5 (1990), 561–571. MR 91g:68160
[23] Dumitrescu A., Planar point sets with few empty convex polygons, Studia Sci. Math. Hun-
gar. 36 (2000), to appear.
[24] Edelman P.H., Jamison R.E., The theory of convex geometries, Geom. Dedicata 19 (1985),
247–270. MR 87f:52002
[25] Erd˝os P., Some unsolved problems, Magyar Tud. Akad. Mat. Kut. Int. Kozl. 6 (1961), 221–
254. Partially reprinted in: Paul Erd˝os: The Art of Counting. Selected Writings (J. Spencer,
ed.), pp. 15–22, MIT Press, Cambridge, MA, 1973. MR 31:2106; MR 58:27144
[26] Erd˝os P., On some problems of elementary and combinatorial geometry, Ann. Mat. Pura
Appl. 103 (1975), 99–18. MR 54:113
[27] Erd˝os P., Some more problems on elementary geometry, Austral. Math.Soc.Gaz. 5 (1978),
52–54. MR 80b:52005
[28] Erd˝os P., Combinatorial problems in geometry and number theory, Relations Between Com-
binatorics and Other Parts of Mathematics. Proc. Conf. Ohio State Univ. Columbus, 1978.
Proc. Symp. Pure Math. Vol. 34, 1979, pp. 149–162. MR 80i:05001
[29] Erd˝os P., Some combinatorial problems in geometry, Geometry and Diﬀerential Geometry.
Proc. Conf. Univ. Haifa, 1979. Lecture Notes Math. 792 (1980), 46–53. MR 82d:51002
[30] Erd˝os P., Someofmy favoriteproblems and results, The Mathematics of Paul Erd˝os, Vol.
I (R. L. Graham and J. Nesetril, eds.), Springer-Verlag, Berlin, 1997, 47–67. MR 98e:11002
[31] Erd˝os P., Purdy G., Extremal problems in combinatorial geometry, pp. 809–874. Hand-
book of Combinatorics (R. L. Graham, M. Gr¨otschel, and L. Lov´asz, eds.), Elsevier Science,
Amsterdam, 1995. MR 96m:52025
[32] Erd˝os P., Szekeres G., A combinatorial problem in geometry, Compositio Math. 2 (1935),
463–470. Reprinted in: Paul Erd˝os: The Art of Counting. Selected Writings (J. Spencer,
ed.), pp. 3–12, MIT Press, Cambridge, MA, 1973. Reprinted in: Classic Papers in Combi-
natorics (I. Gessel and G.-C. Rota, eds.), pp. 49–56, Birkh¨auser, Basel, 1987. MR 58:27144;
MR 88c:01055

456 W. MORRIS AND V. SOLTAN

[33] Erd˝os P., Szekeres G., On some extremum problems in elementary geometry, Ann. Univ.
Sci. Budapest. E¨otv¨os Sect. Math. 3-4 (1961), 53–62. Reprinted in: Paul Erd˝os: The Art
of Counting. Selected Writings (J. Spencer, ed.), pp. 680–689, MIT Press, Cambridge, MA,
1973. MR 24:A3560; MR 58:27144
[34] Erd˝os P., Tuza Z., Valtr P., Ramsey remainder, European J. Combin. 17 (1996), 519–532.
MR 98d:05146
[35] Fejes T´oth G., Recent progress on packing and covering, Advances in Discrete and Com-
putational Geometry, (South Hadley, MA, 1996), pp. 145–162. Contemp. Math. 223 (1999),
AMS, Providence, RI, 1999. MR 99g:52036
[36] Goodman J.E., Pollack R., A combinatorial perspective on some problems in geometry,
Congr. Numer. 32 (1981), 383–394. MR 84b:05003
[37] Goodman J.E., Pollack R., A theorem of ordered duality, Geom. Dedicata 12 (1982),
63–74. MR 83f:51009
[38] Graham R.L., Neˇsetˇril J., Ramsey theory in the work of Paul Erd˝os, The Mathematics
of Paul Erd˝os, Vol. II, (R. L. Graham and J. Neˇsetˇril, eds.), Springer-Verlag, Berlin, 1997,
193–209. MR 97j:01031
[39] Graham R.L., Rothschild B.L., Spencer J.H., Ramsey Theory, 2nd edition, Wiley-
Interscience, New York, 1990. MR 90m:05003
[40] Gr¨unbaum B., Convex Polytopes, Interscience Publishers, New York, 1967. MR 37:2085
[41] Hadwiger H., Debrunner H.,Ausgew¨ahlte Einzelprobleme der kombinatorischen Geometrie
in der Ebene, Enseign. Math. 1 (1955), 56–89. MR 17:887c
[42] Hadwiger H., Debrunner M., Kombinatorische Geometrie in der Ebene, Inst. Math. Univ.,
Gen`eve, 1960. (English translation: Hadwiger H., Debrunner M., and Klee V., Combinato-
rial Geometry in the Plane, Holt, Rinehart and Winston, New York, 1964.) MR 22:11310;
MR 29:1577
[43] Harborth H.,Konvexe F¨unfecke in ebenen Punktmengen, Elem. Math. 33 (1978), 116–118.
MR 80a:52003
[44] Harborth H., M¨oller M., The Esther Klein problem in the projective plane, J. Combin.
Math. Combin. Comput. 15 (1994), 171–179. MR 95d:52013
[45] Hoffman P., The Man Who Loved Only Numbers, Hyperion, New York, 1998. CMP 99:07
[46] Horton J.D., Sets with no empty convex 7-gons, Canad. Math. Bull. 26 (1983), 482–484.
MR 85f:52007
[47] Hosono K., Urabe M., On the number of disjoint convex quadrilaterals for a given point
set in the plane, Comput. Geom. Theory and Applications, submitted.
[48] Jamison-Waldner R.E., Partition numbers for trees and ordered sets, Paciﬁc J. Math. 96
(1981), 115–140. MR 83a:52003
[49] Johnson S., A new proof of the Erd˝os-Szekeres convex k-gon result, J. Combin. Theory Ser.
A 42 (1986), 318–319. MR 87j:52004
[50] Kalbfleisch J.D., Kalbfleisch J.G., Stanton R.G., A combinatorial problem on convex
regions, Proc. Louisiana Conf. Combinatorics, Graph Theory and Computing, Louisiana
State Univ., Baton Rouge, La, 1970. Congr. Numer. 1 (1970), 180-188. MR 42:8394
[51] Kalbfleisch J.G., Stanton R.G., On the maximum number of coplanar points containing
no convex n-gons, Utilitas Math. 47 (1995), 235–245. MR 96b:52016
[52] K´arolyi G., Ramsey-remainder for convex sets and the Erd˝os-Szekeres Theorem, Discr.
Appl. Math., to appear.
[53] K´arolyi G., Pach J., T´oth G., A modular version of the Erd˝os-Szekeres Theorem, in
preparation.
[54] K´arolyi G., Valtr P.,Sets in Rd without large convex subsets, in preparation.
[55] Katchalski M., Meir A., On empty triangles determined by points in the plane, Acta.
Math. Hungar. 51 (1988), 323–328. MR 89f:52021
[56] Klee V., Wagon S., Old and New Unsolved Problems in Plane Geometry and Number
Theory, Mathematical Association of America, Dolciani Mathematical Expositions–No. 11,
1991. MR 92k:00014
[57] Kleitman D., Pachter L., Finding convex sets among points in the plane, Discrete Comput.
Geom. 19 (1998), 405–410. MR 99e:52021
[58] Korte B., Lov´asz L., Shelling structures, convexity and a happy end, pp. 219–232. Graph
Theory and Combinatorics (B. Bollob´as, ed.), Academic Press, London, 1984. MR 86e:90091

THE ERD ˝OS-SZEKERES PROBLEM ON POINTS IN CONVEX POSITION 457

[59] Korte B., Lov´asz L., Schrader R., Greedoids, Springer-Verlag, Berlin, 1991.
MR 93f:90003
[60] Lewin M., A new proof of a theorem of Erd˝os and Szekeres, Math. Gaz. 60 (1976), 136–138.
MR 58:10486
[61] Lov´asz L., Combinatorial Problems and Exercises, North-Holland, Amsterdam, 1979.
MR 80m:05001
[62] Morris W.D., Convex dimension of locally planar convex geometries, Discrete Comput.
Geom., to appear.
[63] Motzkin T.S., Cooperative classes of ﬁnite sets in one and more dimensions, J. Combin.
Theory 3 (1967), 244–251. MR 35:5328
[64] Motzkin T.S., O’Neil P.E., Bounds assuring subsets in convex position, J. Combin. Theory
3 (1967), 252–255. MR 35:5329
[65] Neˇsetˇril J., Valtr P., A Ramsey-type theorem in the plane, Combin. Probab. Comput. 3
(1994), 127–135. Also in: Combinatorics, Geometry and Probability, pp. 525–533 (Cambridge,
1993), Cambridge University Press, Cambridge, 1997. MR 95e:05119
[66] Nielsen M.J., Transverse matchings on a ﬁnite planar set (Manuscript), University of Idaho,
Moscow, 1995.
[67] Overmars M., Scholten B., Vincent I., Sets without empty convex 6-gons, Bull. European
Assoc. Theor. Comput. Sci. No. 37 (1989), 160–168.
[68] Pach J., Solymosi J., Canonical theorems for convex sets, Discrete Comput. Geom. 19
(1998), 427–435. MR 99a:52025
[69] Pach J., T´oth G., A generalization of the Erd˝os-Szekeres theorem for disjoint convex sets,
Discrete Comput. Geom. 19 (1998), 437–445. MR 99b:52038
[70] Pach J., T´oth G.,Erd˝os-Szekeres type theorems for segments and non-crossing convex sets,
Geometriae Dedicata,to appear.
[71] Purdy G.B., The minimum number of empty triangles, AMS Abstracts 3 (1982), 318.
[72] Ramsey F.P., On a problem of formal logic, Proc. London Math. Soc. 30 (1930), 264–286.
Reprinted in: Classic Papers in Combinatorics (I. Gessel and G.-C. Rota, eds.), pp. 2–24.
Birkh¨auser, Basel, 1987. MR 88c:01055
[73] Schechter B., My Brain Is Open, Simon & Schuster, New York, 1998. MR 99h:01038
[74] Schmitt P., Problems in discrete and combinatorial geometry, pp. 449–483. Handbook
of Convex Geometry, (P.M. Gruber and J.M. Wills, eds.), Elsevier Sci. Publ., 1993.
MR 94h:52002
[75] Soltan V., Introduction to the Axiomatic Theory of Convexity, (Russian) S¸tiint¸a, Chi¸sin˘au,
1984. MR 87h:52004
[76] Solymosi J., Combinatorial Problems in Finite Ramsey Theory, Master’s Thesis, E¨otv¨os
University, Budapest, 1988.
[77] Steinitz E., Bedingt konvergente Reihen und konvexe Systeme, J. Reine Angew. Math. 143
(1913), 128–175; 144 (1914), 1–40; 146 (1916), 1–52.
[78] Szekeres G., A combinatorial problem in geometry, Reminiscences, pp. xix–xxii. Paul Erd˝os:
The Art of Counting. Selected Writings (J. Spencer, ed.), MIT Press, Camgridge, MA, 1973.
MR 58:27144
[79] T´oth G., Finding convex sets in convex position, Combinatorica,to appear.
[80] T´oth G., Valtr P., Note on the Erd˝os-Szekeres theorem, Discrete Comput. Geom. 19 (1998),
457–459. MR 99e:52022
[81] Urabe M., On a partition into convex polygons, Discrete Appl. Math. 64 (1996), 179–191.
MR 96m:52027
[82] Valtr P., Convex independent sets and 7-holes in restricted planar point sets, Discrete
Comput. Geom. 7 (1992), 135–152. MR 93e:52037
[83] Valtr P.,Sets in IRd with no large empty convex subsets, Discrete Math. 108 (1992), 115–
124. MR 93i:52007
[84] Valtr P., On the minimum number of empty polygons in planar point sets, Studia Sci.
Math. Hungar. 30 (1995), 155–163. MR 96e:52019
[85] Valtr P., Several Results Related to the Erd˝os–Szekeres Theorem, Doctoral Dissertation,
Charles University, Prague, 1996.
[86] Valtr P., On mutually avoiding sets, The Mathematics of Paul Erd˝os, Vol. II, (R. L. Graham
and J. Neˇsetˇril, eds.), Springer-Verlag, Berlin, 1997, 324–328. MR 98d:52025

458 W. MORRIS AND V. SOLTAN

[87] van de Vel M.L.J., Theory of Convex Structures, North-Holland, Amsterdam, 1993.
MR 95a:52002
[88] Watson F.R., XIth International Mathematical Olympiad. Bucharest, July 1969, Math. Gaz.
53 (1969), 395–396.
[89] Watson F.R., A problem on convex quadrilaterals, Math. Spectrum 2 (1969/70), 54–57.

Department of Mathematical Sciences, George Mason University, 4400 University
Drive, Fairfax, VA 22030

Department of Mathematical Sciences, George Mason University, 4400 University
Drive, Fairfax, VA 22030
