<!-- source: https://arxiv.org/pdf/2301.01340 | converted from PDF -->

INSCRIBED SQUARES AND RELATION AVOIDING PATHS.

COLE HUGELMEYER

Abstract. We develop a connection between the inscribed square problem and the question of
understanding relation avoiding paths in a complex vector space. Our main theorem is that a
Jordan curve with no inscribed squares would have a seemingly impossible structure which we call
a square envelope. We will make some conjectures about the nature of relation avoiding paths in
vector spaces, and show that these conjectures would imply the existence of inscribed squares in
Jordan curves with ﬁnitely many arbitrarily complicated singularities.

1. Introduction

A Jordan curve is a continuous injective function γ : S1 Ñ R2 which wraps counterclockwise
around the region it encloses. An inscribed square of γ is a quadruple of distinct points on impγq
which form a square in R2.

Figure 1. An inscribed square of a Jordan curve.

Conjecture 1 (Toeplitz 1911). Every Jordan curve has an inscribed square.

Towards this end, we deﬁne a bad Jordan curve to be a Jordan curve with no inscribed squares.
Our main result is that a bad Jordan curve must have a structure which we call a square envelope.
A square envelope is, loosely speaking, a square moving with time, so that its ﬁrst two corners are
always outside the Jordan curve, its second two corners are always inside the Jordan curve, and
the outside corners wrap completely around the Jordan curve as time progresses.
To rigorously deﬁne a square envelope, we let T : R2 Ñ R2 be the linear map corresponding
to 90 degree counterclockwise rotation. For a pair of points a and b in the plane, we deﬁne
S1pa, bq “ a`T pb´aq and S2pa, bq “ b`T pb´aq. If a ‰ b, then the four points a, b, S2pa, bq, S1pa, bq
form the vertices of a square, labeled counterclockwise.
1arXiv:2301.01340v1  [math.MG]  3 Jan 2023
2 COLE HUGELMEYER

Deﬁnition 1. Let γ : S1 Ñ R2 be a Jordan curve. A square envelope of γ is a pair of continuous
functions mapping from R to the plane, e1, e2 : R Ñ R2, such that all of the following are true.
1) For all x P R, e1pxq and e2pxq are in the open exterior of γ.
2) For all x P R, S1pe1pxq, e2pxqq and S2pe1pxq, e2pxqq are in the open interior of γ.
3) limxÑ8 }e2pxq ´ e1pxq} “ limxÑ´8 }e2pxq ´ e1pxq} “ 0.
4) Let ℓλ be the closed curve obtained by ﬁrst following e1 from e1p´λq to e1pλq, then a
straight line from e1pλq to e2pλq, then e2 from e2pλq to e2p´λq, and ﬁnally a straight line
from e2p´λq back to e1p´λq. If p is any point inside γ, then there exists a real number
λ0 ą 0 such for all λ ą λ0, we have that the winding number of ℓλ around p is equal to one.

Figure 2. As square envelopes conjecturally do not exist, they are somewhat dif-
ﬁcult to draw. This is a rough approximation of what one might look like. The
square must somehow have its ﬁrst two corners move around the outside of the
Jordan curve while the other two corners remain inside.

Theorem 1. Every bad Jordan curve has a square envelope.

This theorem allows us to make a connection between the inscribed square problem and the
problem of understanding relation avoiding paths in a vector space. The set of squares is the vector
space, and the linear relation we avoid is the ﬁrst two corners of one square touching the second
two corners of another.
Let V be a vector space over C, and suppose R1, R2, ..., Rn are linear relations, subspaces of the
vector space V ˆ V . We then let R be the relation given by the union of sets Yn
i“1Ri. We will
assume that R is symmetric, namely aRb ðñ bRa.
A relation-avoiding path is a continuous function p : r0, 1s Ñ V such that there does not exist
any pair of times t1, t2 in r0, 1s with ppt1qRppt2q. We deﬁne a relation-avoiding origin path to be a
continuous function p : r0, 8q Ñ V with limtÑ8 pptq “ 0, such that there does not exist any pair
of times t1, t2 in r0, 8q, for which ppt1qRppt2q. The origin is not included as the endpoint of this
path because we always have 0R0.

Deﬁnition 2. We say two relation avoiding origin paths p and q are weakly homotopic if there
exists a continuous function h : r0, 1s ˆ r0, 8q Ñ V such that
1) limtÑ8 hps, tq “ 0 for all s.
2) hp0, tq “ pptq for all t.
3) hp1, tq “ qptq for all t.
4) There does not exist any ps, tq P r0, 1s ˆ r0, 8q with hps, tq R hps, 0q.

INSCRIBED SQUARES AND RELATION AVOIDING PATHS. 3

We say p and q are strongly homotopic if h can be chosen so that hps, ´q is a relation avoiding
origin path for all s.

We propose the following conjecture about relation avoiding origin paths.

Conjecture 2 (SC, Spiral Conjecture). Every relation avoiding origin path p is weakly homotopic
to a relation avoiding origin path q for which there exist linearly independent vectors x1, ..., xn in
V and complex numbers a1, ..., an such that

qptq “
 nÿ

i“1 xi ¨ e
ait

for all t.

The following fact provides some evidence for this conjecture.

Theorem 2. The spiral conjecture is true when V is one dimensional.

Finally, we will prove the following implication of Conjecture 2.

Theorem 3. Assume the spiral conjecture. Then any Jordan curve γ which is smooth except
at ﬁnitely many points has an inscribed square. The Jordan curve is permitted to be arbitrarily
complicated near these ﬁnitely many singularities.

We propose that delving into the study of relation avoiding origin paths could be a potential
approach towards solving the inscribed square problem. At the end of the paper, we will make
more conjectures about relation avoiding origin paths, which we hope might guide future research.

2. Square Envelopes

If γ is a bad Jordan curve, we will deﬁne an integer bγ which we call the bad wrapping number
of γ. This integer is only well-deﬁned for bad Jordan curves. By counting inscribed squares in a
generic approximation of γ, we will prove that bγ is odd. Then, we will use this fact to construct
a square envelope of the Jordan curve.
Let γ be a Jordan curve. We may choose a continuous function f : R2 Ñ R with the property
that if a is in the interior of γ, then f paq ă 0, if a is on the image of γ, then f paq “ 0, and if a is
outside of γ, then f paq ą 0. Using this function, we can deﬁne a function gf,γ : S1 ˆ S1 Ñ R2, by
the formula gf,γpx, yq “ pf pS1pγpxq, γpyqqq, f pS2pγpxq, γpyqqqq.
If γ is a bad Jordan curve, then gf,γpx, yq “ p0, 0q if and only if x “ y, because if we have
x ‰ y and gf,γpx, yq “ p0, 0q, then γpxq, γpyq, S2pγpxq, γpyqq, S1pγpxq, γpyqqq form the vertices of an
inscribed square.
Let C “ tpx, yq P S1 ˆ S1 : x ‰ yu. Topologically, C is an open cylinder. By the above
proposition, we see that if γ is a bad Jordan curve, then we can restrict the domain of gf,γ to C to
get a map gf,γ|C : C Ñ R2ztp0, 0qu.
We now ﬁx homotopy equivalences between C, R2ztp0, 0qu, and S1. Our homotopy equivalence
C Ñ S1 is to simply take the ﬁrst coordinate of the ordered pair. Our homotopy equivalence
R2ztp0, 0qu Ñ S1 is radial projection onto the unit circle, which we orient counterclockwise.
Using these homotopy equivalences, we see that, gf,γ|C induces a map S1 Ñ S1 up to homotopy,
and therefore gives us an element of π1pS1q » Z. This integer is deﬁned to be bγ.
bγ does not depend on the choice of f , because given two choices of f , one can be continuously
transformed into the other while always remaining a valid choice of f . This induces a homotopy
between the resulting maps S1 Ñ S1, which implies that the value of bγ is constant.

Lemma 1. For any bad Jordan curve, bγ is odd.

4 COLE HUGELMEYER

The proof of this lemma will be given later in this section. The main idea behind the proof is
that each inscribed square of a generic smooth approximation of γ contributes parity to bγ in a way
that depends on the cyclic order of the vertices of the square on the Jordan curve. The parity of
inscribed squares with a given cyclic ordering is independent of the Jordan curve, so we can simply
calculate the parity of bγ by summing the contributions from each square type. The result is odd
parity.
Lemma 1 can be used to prove Theorem 1, which we will do at the end of this section. The main
idea is that because bγ ‰ 0, the map gf,γ : C Ñ R2ztp0, 0qu wraps nontrivially around the origin.
This implies that there must be a path between the two ends of the cylinder C that maps into the
lower left quadrant of the plane under gf,γ. This path is almost a square envelope, except that e1
and e2 are on the Jordan curve rather than being inside its open exterior. This can be remedied
by simply pushing the paths oﬀ of the curve slightly.

For a manifold M , let ˜C4pM q denote the manifold of cyclically ordered quadruples of distinct
points in M . In other words, if C4 distpM q is the subset of M 4 consisting of ordered quadruples of
distinct points, then ˜C4pM q “ C4 distpM q{pZ{4Zq, where Z{4Z acts by cyclic permutation of the
entries of the 4-tuple. Let Sq denote the the submanifold of ˜C4pR2q consisting of quadruples of
points which form squares labeled counterclockwise.
We call a Jordan curve γ : S1 Ñ R2 generic if, within ˜C4pR2q, the subspace ˜C4pimpγqq intersects
transversely with Sq.
Let h : S1 ˆ r0, 1s Ñ R2 be a smooth homotopy between two generic Jordan curves for which
hp¨, tq is a smooth embedding for all t P r0, 1s. We say that h is a generic homotopy if, within
˜C4pR2q ˆ r0, 1s, the subspace tpq, tq : q P ˜C4pimphp¨, tqqu intersects transversely with the subspace
Sq ˆ r0, 1s.
By the transversality theory found in [3], we have the following facts about generic Jordan curves.
1) Any Jordan curve can be approximated arbitrarily well in the C0 topology by generic Jordan
curves.
2) Any two generic Jordan curves have a generic homotopy between them.
3) For a generic homotopy h, the intersection tpq, tq : q P ˜C4pimphp¨, tqqu X Sq ˆ r0, 1s is a
compact 1-manifold with boundary. The boundary of this manifold consists of the inscribed
squares of the two generic Jordan curves at the beginning and end of the homotopy.
Note that the manifold ˜C4pS1q has three connected components. This corresponds to three types
of inscribed square.

Deﬁnition 3. Let γ be a Jordan curve. An inscribed square of γ is called type I if the counter-
clockwise order of points on the square is the same as that of the Jordan curve. Such squares are
also called gracing squares. A square is called type II if when we label the vertices of the square as
1, 2, 3, 4 in counterclockwise order, these vertices appear in the order 1, 3, 2, 4 when we go counter-
clockwise along the Jordan curve. Finally, a square is called type III if the counterclockwise order
of the vertices is opposite to the counterclockwise order of the Jordan curve.

Figure 3. Inscribed squares of type I, II, and III respectively.

INSCRIBED SQUARES AND RELATION AVOIDING PATHS. 5

Proposition 1. If γ is a generic Jordan curve, then of the inscribed squares of γ, an odd number
of them are type I, an even number are type II, and an even number are type III.

Proof. There are three connected components of ˜C4pimpγqq corresponding to the three types of
inscribed squares when we intersect with Sq. This means that if h is a generic homotopy between
generic Jordan curves, then the 1-manifold tpq, tq : q P ˜C4pimphp¨, tqqu X Sqˆr0, 1s can be separated
into three distinct clopen pieces, one for each type of inscribed square. This proves that the parity
of each type of inscribed square is invariant of which generic Jordan curve we choose. Finally
we can compute the parities by ﬁnding the inscribed squares of any generic Jordan curve. The
quintessential generic Jordan curve is a non-circular ellipse. This curve has one gracing square, but
no inscribed square of type II or III. □

Let γ be a generic Jordan curve, and let f be a smooth function R2 Ñ R which has γ as its zero
set, is negative inside of γ, positive outside of γ, and has non-vanishing gradient on γ. Since γ is
a smooth embedding, such an f always exists. Now, we will consider gf,γ : pS1q2 Ñ R2, as deﬁned
in the previous section.
We see that the zeros of gf,γ consist of the diagonal ∆ “ tpa, aq : a P S1u, as well as four points
for each inscribed square in ˜C4pimpγqq X Sq, one point for each side of the square. Furthermore, at
these zeros corresponding to inscribed squares, gf,γ has nonsingular derivative because γ is generic
and f has non-vanishing gradient on impγq. Let X “ tp P pS1q2 : gf,γppq ‰ p0, 0qu. Let ωγ be the
cohomology class in H 1pX; Z{2Zq given by pulling back the nontrivial class of H 1pR2ztp0, 0qu; Z{2Zq
under gf,γ|X . A small loop around any of the zeroes corresponding to sides of inscribed squares will
evaluate nontrivially under ω because gf,γ has nonsingular derivative at these zeroes. Furthermore,
a loop obtained by pushing the diagonal oﬀ to one side or the other will evaluate trivially under
ωγ because it will correspond to a small square sliding around the Jordan curve with two corners
on γ and the other two corners oﬀ to one side of γ, so the corresponding loop in R2ztp0, 0qu will
remain in just one quadrant of the plane and therefore cannot wrap around the origin.
Putting this all together, we see that if ℓ is a simple closed curve in X which has the homotopy
class of the diagonal in S1 ˆ S1, then ωγpℓq is equal to the parity of the number of zeroes of gf,γ in
either connected component of pS1q2zp∆ Y ℓq.
Let ∆1 be the anti-diagonal of pS1q2, the loop consisting of pairs pa, bq where a and b are antipodes.
Then pS1q2zp∆ Y ∆1q has two connected components, which we call A and B. The component A is
the set of pairs pa, bq for which the angle from a to b is less than π and the component B is the set
of pairs for which the angle from a to b is greater than π.
If γ is a bad Jordan curve, and γ1 is a suﬃciently C0-close generic approximation, then the parity
of bγ is equal to ωγ1p∆1q. We can therefore compute bγ by counting the zeroes of gf,γ1 in A.

Proposition 2. If γ is a bad Jordan curve, and γ1 is a suﬃciently C0-close generic approximation,
then each type I inscribed square of γ1 has exactly three of its corresponding zeroes of gf,γ1 in A,
each type II inscribed square has exactly two of its corresponding zeroes in A, and each type III
inscribed square has exactly one of its corresponding zeroes in A.

Proof. Let γ1, γ2, γ3, ... be a sequence of generic Jordan curves that limit to our bad Jordan curve
γ in the C0 topology. Let sn be the side length of the largest inscribed square of γn. We know
that limnÑ8 sn “ 0 because otherwise there would be a convergent subsequence of squares that
limit to an inscribed square of our bad Jordan curve. We can give S1 a metric by identifying it
with the unit circle in R2 and using euclidean distance. Using this identiﬁcation, we let M be the
set of all pairs pa, bq P pS1q2 which have }a ´ b} ě 1. Let N P Z be suﬃciently large that both
supxPS1 }γN pxq ´ γpxq} and sN are smaller than the quantity ε “ 1
4 ¨ minpa,bqPM }γpaq ´ γpbq}. We
claim that γ1 “ γN is an approximation for which the proposition holds.
Let a, b, c, d be the vertices of an inscribed square of γN , labeled counterclockwise. Let Q be the
set of four points in S1 which map onto ta, b, c, du under γN . We claim that the diameter of Q is

6 COLE HUGELMEYER

less than one. To prove this, suppose there were elements x and y in Q with }x ´ y} ě 1. Then
px, yq P M , so }γpxq ´ γpyq} ě 4ε, so }γN pxq ´ γN pyq} ě 2ε. However, 2ε ą ?
2 ¨ sN and γN pxq and
γN pyq are vertices of a square with side length at most sN , so this is impossible.
Since the diameter of Q is less than 1, all four points of Q must lie within some interval I of
angular length π{3 radians. Orient I counterclockwise, and let w, x, y, z be the four elements of Q
in the order they appear along I. We know that pw, xq, pw, yq, pw, zq, px, yq, px, zq, and py, zq are in
A, and all the other ordered pairs are in B.
We know that γN maps tw, x, y, zu onto ta, b, c, du, but it might not preserve the ordering.
Without loss of generality, we can assume γN pwq “ a because we can permute the labels a, b, c, d
cyclically. Then, we have six possibilities to check for the six permutations of the remaining three
letters. We will now check all of the possibilities.
1) If pw, x, y, zq ÞÑ pa, b, c, dq, the square is type I and the corresponding zeroes in A are
pw, xq, px, yq, py, zq.
2) If pw, x, y, zq ÞÑ pa, c, b, dq, the square is type II and the corresponding zeroes in A are
pw, yq, px, zq.
3) If pw, x, y, zq ÞÑ pa, b, d, cq, the square is type II and the corresponding zeroes in A are
pw, xq, px, zq.
4) If pw, x, y, zq ÞÑ pa, d, c, bq, the square is type III and the only corresponding zero in A is
pw, zq.
5) If pw, x, y, zq ÞÑ pa, d, b, cq, the square is type II and the corresponding zeroes in A are
pw, yq, py, zq.
6) If pw, x, y, zq ÞÑ pa, c, d, bq, the square is type II and the corresponding zeroes in A are
pw, zq, px, yq.
This conﬁrms the proposition. The type I squares have three corresponding zeroes in A, the type
II squares have two corresponding zeroes in A, and the type III squares have only one corresponding
zero in A. □

We can now prove Lemma 1 and Theorem 1.

Proof of Lemma 1. Let γ be a bad Jordan curve, let γ1 be a suﬃciently C0-close generic approxi-
mation, and let f be a function with γ1 as its zero set as above. We now count zeroes of gf,γ1 in A,
the parity of which is the parity of bγ. We count the zeroes by those corresponding to the squares
of each type. We have an odd number of threes, an even number of twos, and an even number of
ones. This totals to an odd number.

Proof of Theorem 1. We wish to prove that every bad Jordan curve has a square envelope. We
have the function gf,γ|C : C Ñ R2ztp0, 0qu, which we know to be homotopically nontrivial. Let
π : R2ztp0, 0qu Ñ S1 be radial projection onto the unit circle, and let r “ π ˝ gf,γ|C. We now take r1

to be a smooth approximation of r with }rpxq ´ r1pxq} ă 1{4 for all x P C. Let u P S1 be a regular
value for r1 within distance 1{4 of the point p´1{
?2, ´1{?
2q. Then r´1puq is a 1-dimensional
manifold, L, which is mapped under r into a circle of radius 1{2 around p´1{?
2, ´1{
?2q, which
is entirely in the lower left quadrant of the plane. Therefore, gf,γ|C maps L into the lower left
quadrant of the plane. This implies that the square corresponding to a point of L has its ﬁrst two
corners on γ, and the other two in the open interior of γ. Furthermore, since bγ is odd, we see that
L must have an odd number of connected components which are homeomorphic to R with the two
ends limiting to the two boundaries of C. Parameterizing such a connected component, we have
functions e1, e2 : R Ñ R2 with impe1q Y impe2q Ď impγq, and limxÑ˘8 }e1pxq ´ e2pxq} “ 0, and with
the property that S1pe1pxq, e2pxqq and S2pe1pxq, e2pxqq are always in the open interior of γ. Since
the interior of gamma is open, we may choose a continuous function ε : R Ñ Rą0 with the property
that, for all x, if }a ´ e1pxq} and }b ´ e2pxq} are less than εpxq, then S1pa, bq and S2pa, bq are in the

INSCRIBED SQUARES AND RELATION AVOIDING PATHS. 7

open interior of γ as well. Thus, if we choose a continuous deformation of pe1, e2q in which we push
e1pxq and e2pxq oﬀ of the Jordan curve without exceeding a distance of εpxq, we obtain a square
envelope for γ.
 3. Relation avoiding paths

In this section, we will prove that if the spiral conjecture is true, then the inscribed square conjec-
ture holds for Jordan curves which are smooth except at a ﬁnite number of arbitrarily complicated
singularities.
However, we will ﬁrst present a proof of Theorem 2, that the spiral conjecture is indeed true in
the one-dimensional case.

Proof of Theorem 2. Identifying V with C, our relation avoiding origin paths are paths to the origin
in the complex plane p : r0, 8q Ñ C. Furthermore, we know that pptq is never zero, because p0, 0q is
in every linear relation. Thus, without loss of generality, we can ignore any of the Ri corresponding
to t0u ˆ C or C ˆ t0u. We can therefore rewrite the relation R as

xRy ðñ Di P t1, ..., nu x “ αiy or y “ αix

where α1, ..., αn are nonzero complex numbers with norm at most one. In particular, our path p
is relation avoiding if and only if it is disjoint from the paths α1p, α2p, ..., αnp. Without loss of
generality, we can assume that pp0q “ 1, and that |pptq| ď 1 for all t. The reason we can do this
is that we can always homotope p to such a path by ﬁrst contracting it within its image so that
the starting point is at the point with maximal norm, and then rescaling within C so that the
starting point becomes 1. We can also assume without loss of generality that p follows the path of
a logarithmic spiral inside some small neighborhood around 1, because making this happen only
requires a small perturbation. Working with these assumptions, we ﬁx a branch of the logarithm,
and let ℓ1, ..., ℓn be paths in upper-half plane such that e2πiℓiptq “ αipptq with ℓip0q “ 1
2πi lnpαiq,
and similarly let ℓ be a lift of p with ℓp0q “ 0. The path ℓ divides the upper-half plane, and we
deﬁne U to be the set of all points of Hzimpℓq from which a path to ´8 has even intersection parity
with ℓ. We then deﬁne integers k1, ..., kn, where ki is the largest integer such that ℓip0q ` ki P U .
We see that ℓ is disjoint from ℓi ` k for any index i and integer k, and this gives us paths disjoint
from ℓ, going up to i8, from every point of the form ℓp0q ` k. Therefore, the homotopy type of ℓ
can be completely determined by knowing which points of the form ℓip0q ` k are in U . Thus, to
prove the one-dimensional spiral conjecture, it suﬃces to prove that there exists a θ P p0, πq so that
for all i P t1, ..., nu, we have the inequalities argpℓip0q ` kiq ě θ ě argpℓip0q ` ki ` 1q. This θ would
then denote the angle of a straight line in the upper half plane that exponentiates to the desired
logarithmic spiral. To prove that such a θ exists, it suﬃces to prove that for all i and j we have
argpℓjp0q ` kj ` 1q ď argpℓip0q ` kiq.
We deﬁne a split pair to be a pair of points in the upper half-plane pp, qq, such that p ` ℓ and
q ` ℓ are both disjoint from ℓ, with p P U and q R U . For instance, pℓip0q ` ki, ℓjp0q ` kj ` 1q is
always a split pair.

8 COLE HUGELMEYER

Figure 4. A depiction of a split pair, disjoint translates of ℓ, one on each side.

Given a split pair pp, qq, we can construct a new split pair as follows. If imppq ě impqq, then
pp ´ q, qq is the new split pair. If impqq ą imppq, then pp, q ´ pq is the new split pair. The split
pair obtained by applying this transformation is called the derived split pair. We claim that the
derived split pair is always another split pair.

Figure 5. One way to understand derived split pairs is that one draws a parallel-
ogram spanning the origin and the two points, then moves the uppermost point to
the new corner.

To prove this claim, we consider the case that imppq ě impqq. We have that ℓ ` q is entirely on
the right side of ℓ, and ℓ`p is entirely on the left side of ℓ. Furthermore, since all of ℓ`p has greater
imaginary coordinate than impqq, we therefore have that p P ta P U : impaq ě impqqu Ď U ` q.
This tells us that p ´ q is in U , so pp ´ q, qq is a valid split pair. The argument for the other case
is similar.
We say a split pair is good if argppq ą argpqq. We say a split pair is bad otherwise. We see that
the derived split pair of a bad split pair is bad, and the derived split pair of a good split pair is

INSCRIBED SQUARES AND RELATION AVOIDING PATHS. 9

good. To complete the proof of the theorem, it suﬃces to prove that all split pairs are good, so we
will consider what occurs under repeated derivation of a bad split pair. First of all, note that if
imppq{impqq is a rational number, then we will eventually have a split pair with a real number as
one of the terms, and we can see that any split pair containing a real number is good. Thus, we have
shown that imppq{impqq is irrational for any bad split pair. Now, we will proceed by contradiction
to prove that there are no bad split pairs. Suppose that pp, qq is a bad split pair. We will treat the
cases of argppq ă argpqq and argppq “ argpqq separately.
Suppose that pp, qq is a bad split pair with argppq ă argpqq. Then, the i-th derived split pair is
of the form paip ´ biq, ciq ´ dipq, for nonnegative integers ai, bi, ci, di such that

lim
iÑ8 ai{bi “ lim
iÑ8 di{ci “ impqq{imppq

This tells us that while the imaginary parts of the terms of the derived split pairs approach zero,
the real parts approach `8 and ´8 respectively. However, this would force the second term to
eventually be in U , which gives us a contradiction.
Now, suppose argppq “ argpqq. In this case, the terms of the derived split pairs stay on a ﬁxed
straight line, and they approach zero. However, earlier in the proof, we assumed without loss of
generality that p followed the path of a logarithmic spiral in some small neighborhood around 1,
which means ℓ is a straight line in some small neighborhood around zero. This means that there
are no bad split pairs in this neighborhood, so we have a contradiction. This completes the proof.
□

Before we prove Theorem 3, we need to develop some notation surrounding square envelopes,
and prove a couple lemmas.

Deﬁnition 4. Let γ : S1 Ñ R2 be a Jordan curve, and let pe1, e2q be a square envelope. We
write σ˚
p pe1, e2, γq, where p P t1, 2u and ˚ P t`, ´u, to denote a sign in t`1, ´1u determined as
follows. For λ P R, let Pλ be the path that starts at e1pλq, then goes along e1 to e1p0q, then goes
in a straight line from e1p0q to e2p0q, then follows e2 to e2pλq, then goes in a straight line back to
the starting point e1pλq. We then let npλq be the wrapping number of Pλ around Sppe1p0q, e2p0qq.
Finally, we set σ˚
p pe1, e2, γq “ limλÑ˚8p´1qnpλq.

It is worth observing that these parities are determined by how the Jordan curve winds between
the vertices of a small square near t “ ˘8. For curves with ﬁnitely many singularities, they are
related to each other by the following lemma.

Lemma 2. If γ is a Jordan curve which is smooth except at ﬁnitely many points, then the following
facts are true for any square envelope pe1, e2q of γ.
1) σ`
1 pe1, e2, γq “ σ`
2 pe1, e2, γq and σ´
1 pe1, e2, γq “ σ´
2 pe1, e2, γq
2) σ`
1 pe1, e2, γq “ ´σ´
1 pe1, e2, γq
3) If ˚ P t`, ´u is such that σ˚
1 pe1, e2, γq “ ´1, then the limits limtÑ˚8 e1ptq and limtÑ˚8 e2ptq
exist, and are equal to each other.

Proof. First of all, by property (4) in the deﬁnition of a square envelope, we immediately have that
σ`
1 pe1, e2, γq “ ´σ´
1 pe1, e2, γq and σ`
2 pe1, e2, γq “ ´σ´
2 pe1, e2, γq because the deﬁning loops for the
parities in question compose to give us a loop that wraps around the Jordan curve exactly once.
Next, we claim that if ˚ P t`, ´u, and the limit limtÑ˚8 e1ptq does not exist, then we have
σ˚
1 pe1, e2, γq “ σ˚
2 pe1, e2, γq “ 1. To prove this claim, note that for the limit to fail to exist, there
must be a limit point of e1ptq, t Ñ ˚8 at one of the points where γ is smooth. Taking a suﬃciently
small square of the envelope, in the ˚8 direction, near such a point, we see that the Jordan curve
must separate the vertices of the square in a way locally equivalent to how a straight line could
separate the vertices, and there is only one such way that separates the e1, e2 vertices from the
other two vertices. Since all squares suﬃciently near t “ ˘8 will have side length smaller than the

10 COLE HUGELMEYER

diameter of some disk inside of the Jordan curve, the paths that deﬁne σ˚
1 pe1, e2, γq and σ˚
2 pe1, e2, γq
cannot wrap around either of the two interior vertices of the square at t “ 0. Therefore, we have
σ˚
1 pe1, e2, γq “ σ˚
2 pe1, e2, γq “ 1.
To prove all three parts of the lemma, all that remains is to eliminate the possibility that the limits
limtÑ˚8 e1ptq and limtÑ˚8 e2ptq exist, but σ˚
1 pe1, e2, γq and σ˚
2 pe1, e2, γq are not equal to one an-
other. The reason this is impossible is that for this to be the case, the paths e1ptq, e2ptq, S1pe1ptq, e2ptqq,
and S2pe1ptq, e2ptqq would need to all approach some point in the plane, none of them intersect-
ing each other, in such a way that as one encircles the point counterclockwise, the paths appear
in a cyclic order that alternates between the sets te1ptq, e2ptqu and tS1pe1ptq, e2ptqq, S2pe1ptq, e2ptqqu.
This would then contradict the fact that the simple closed curve γ separates the paths in te1ptq, e2ptqu
from those in tS1pe1ptq, e2ptqq, S2pe1ptq, e2ptqqu. □

If γ is a Jordan curve which is smooth except at ﬁnitely many points, and pe1, e2q is a square
envelope, we say pe1, e2q is positively oriented if σ`
1 pe1, e2, γq “ ´1 and negatively oriented if
σ`
1 pe1, e2, γq “ `1. Note that if pe1ptq, e2ptqq is a negatively oriented square envelope, we can
obtain a positively oriented one by taking pe1p´tq, e2p´tqq.
We need one more lemma before we can prove Theorem 3.

Lemma 3. Let α1, α2, β1, β2 be complex numbers such that the ratio β1{β2 is a positive real
number. Let t0 and p be arbitrary real numbers with p ‰ 0, and let λ, r1, r2 be real numbers in
r0, 1q. If there exist real numbers t1 and t2 in r0, 8q such that

eα1`β1ppt1´t0q ´
1 ` λr1e
ippt1´t0q¯ “ e
α2`β2ppt2´t0q ´
1 ` λr2e
ippt2´t0q¯

then there also exist t1
1 and t1
2 in r0, 8q such that

eα1`β1ppt1
1´t0q ´1 ` r1e
ippt1
1´t0q¯ “ e
α2`β2ppt1
2´t0q ´
1 ` r2eippt1
2´t0q¯

Proof. Making the substitutions α1 ´ α2 “ α, ppt1 ´ t0q “ t, and ppt2 ´ t0q “ pβ1{β2qt ` s, the
equation e
α1`β1ppt1´t0q ´
1 ` λr1e
ippt1´t0q¯ “ e
α2`β2ppt2´t0q ´
1 ` λr2e
ippt2´t0q¯

rearranges to
 e
α´β2s “ 1 ` λr1eit

1 ` λr2e
ip β1
β2 t`sq

Rearranging, and setting a “ r1, bpsq “ ´r2eα`pi´β2qs, and cpsq “ eα`β2s ´ 1, we have

cpsq “ λ ¨ ˆ
a ¨ e
it ` bpsq ¨ e
i´ β1
β2 t
¯˙

Also, let
 T psq “ tt : Dt1 ě 0, Dt2 ě 0, ppt2 ´ t0q “ pβ1{β2qt ` s, ppt1 ´ t0q “ tu

be the allowable values of t for ﬁxed s, when t1 and t2 are nonnegative. This will always be an
interval of the form p´8, zs or rz, 8q for some real number z. Now, let Hpsq denote the unique
minimal simply connected set containing the set

ta ¨ e
it ` bpsq ¨ e
ipβ1{β2qt : t P T psqu

Then, we see that there exists a pair of nonnegative real numbers t1 and t2 such that

e
α1`β1ppt1´t0q ´
1 ` λr1e
ippt1´t0q¯ “ e
α2`β2ppt2´t0q ´
1 ` λr2e
ippt2´t0q¯

if and only if there exists a real number s such that cpsq P λHpsq. Since β1{β2 is positive, when
β1{β2 is rational, Hpsq is the region enclosed by the outer boundary of an epitrochoid curve. When
β1{β2 is irrational, Hpsq it is a disk missing some subset of its boundary. In particular, Hpsq is

INSCRIBED SQUARES AND RELATION AVOIDING PATHS. 11

always a radial set, meaning that for any x P Hpsq, we have λx P Hpsq for all λ P r0, 1s. Therefore,
increasing the parameter λ preserves the existence of solutions to our original equation. Setting
λ “ 1 gives us the desired result.

Figure 6. The region enclosed by an epitrochoid curve is always a radial set.
 □

Now, we can prove Theorem 3.

Proof of Theorem 3. We begin by considering the system of linear relations on C2 given by letting
px1, y1qRpx2, y2q when

tx1, y1, x2, y2u X tx1 ` ipy1 ´ x1q, y1 ` ipy1 ´ x1q, x2 ` ipy2 ´ x2q, y2 ` ipy2 ´ x2qu ‰ ∅

Now, take a positively oriented square envelope pe1, e2q. Due to Lemma 2, restricting the domain
to r0, 8q immediately gives us a relation avoiding origin path pe1ptq, e2ptqq ´ limtÑ8pe1ptq, e2ptqq
for R. We are assuming the spiral conjecture, so we may mow take h : r0, 1s ˆ r0, 8q satisfying the
conditions of the spiral conjecture. This gives us complex numbers a1, a2, and vectors x1, x2 P C2,
such that pf1ptq, f2ptqq “ f ptq “ x1ea1t ` x2ea2t is a relation avoiding origin path for R which has
the property that the path in C starting at 0, following f2 to f2p0q, going in a straight line from
f2p0q to f1p0q, then following f1 back to 0 has nontrivial wrapping number parity around the points
f1p0q ` ipf2p0q ´ f1p0qq and f2p0q ` ipf2p0q ´ f1p0qq. Without loss of generality, we can assume that
a1 and a2 have the same real part, because otherwise one term will dominate at large t, reducing
us to the case of a pure logarithmic spiral, which we will cover later. Similarly, we may assume
a1 ‰ a2. Now, to prove that no such a1, a2, x1, x2 exist, we see that for the path to be relation
avoiding, we must be able to ﬁnd some ﬁxed complex number β, and nonzero real number p, such
that all four paths f1ptq, f2ptq, f1ptq ` ipf2ptq ´ f1ptqq, and f2ptq ` ipf2ptq ´ f1ptqq are of the form

eα`qβppt´t0q ´1 ` re
ippt´t0q¯

with α P C, t0 P R, q P p0, 8q, and r P r0, 1q. Therefore, Lemma 3 allows us to continuously scale
down all of the r parameters to zero while staying a relation avoiding origin path.
All that remains is to show that no pure logarithmic spiral f ptq “ xeat can be a relation avoiding
origin path with the stated wrapping number parity condition. To prove this, note that the region
swept out by a line segment between f1 and f2 would have the same area as the region swept out
by the line segment between f1 ` ipf2 ´ f1q and f2 ` ipf2 ´ f1q. However, our wrapping number

12 COLE HUGELMEYER

condition implies that the former region would need to strictly contain the latter, which would
contradict them having equal areas. □

To wrap things up, we make a couple more conjectures about relation avoiding origin paths.

Conjecture 3 (SSC, Strong Spiral Conjecture). Every relation avoiding origin path p is strongly
homotopic to a relation avoiding origin path q for which there exist linearly independent vectors
x1, ..., xn in V and complex numbers a1, ..., an such that

qptq “
 nÿ

i“1 xi ¨ e
ait

for all t.

Conjecture 4 (MSC, Monotonic Spiral Conjecture). For any continuous function p : r0, 8q Ñ
V zt0u with limtÑ8 pptq “ 0, there exists a continuous function h : r0, 1s ˆ r0, 8q Ñ V with the
following properties.
1) limtÑ8 hps, tq “ 0 for all s.
2) hp0, tq “ pptq for all t.
3) There exist linearly independent vectors x1, ..., xn in V and complex numbers a1, ..., an such
that
 hp1, tq “
 nÿ

i“1 xi ¨ eait

for all t.
4) If 0 ď s1 ď s2 ď 1, then Bps2q Ď Bps1q, where

Bpsq :“ ď

pt1,t2qPr0,8q2tf P pV ˆ V q1 : f phps, t1q, hps, t2qq “ 0u

It is not too diﬃcult to prove the implications M SC ùñ SSC ùñ SC. The strong spiral
conjecture clearly implies the spiral conjecture, but it might not be so easy to see why the monotonic
spiral conjecture implies the strong spiral conjecture. The reason is that a small perturbation of
the homotopy can be made to avoid any relations with codimension greater than one in V ˆ V ,
and the homotopy for the monotonic spiral conjecture will always increase the set of codimension
one relations that it avoids.
Morally speaking, the monotonic spiral conjecture should be true in the one-dimensional case
because curve shortening ﬂow in a logarithmic metric should have the desired property. This
argument should at least cover the case of smooth paths which are periodic deviations from a
logarithmic spiral, but the analysis is more complicated for arbitrary continuous paths. It would be
useful if there was a way to generalize such an argument to higher dimensions, though it is not at
all obvious how to achieve this. Regardless, we hope that a deep enough understanding of relation
avoiding paths will lead to new progress on the inscribed square problem.

INSCRIBED SQUARES AND RELATION AVOIDING PATHS. 13

References

[1] Arseniy Akopyan and Sergey Avvakumov. Any cyclic quadrilateral can be inscribed in any closed convex smooth
curve. Forum of Mathematics, Sigma, 2018.
[2] H.B. Griﬃths. The topology of square pegs in round holes. Proceedings of the London Mathematical Society,
s3-62(3):647–672, 1991.
[3] John McCleary Jason Cantarella, Elizabeth Denne. Transversality for conﬁguration spaces and the “square-peg”
theorem. arXiv:1402.6174 [math.GT], 2014.
[4] Benjamin Matschke. Equivariant topology methods in discrete geometry. PhD thesis, Freie University at Berlin,
2011.
[5] Benjamin Matschke. A survey on the square peg problem. Notices Amer. Math. Soc., 61(4):346–352, 2014.
[6] Benjamin Matschke. Quadrilaterals inscribed in convex curves. arXiv:1801.01945 [math.MG], 2018.
[7] M. J. Nielsen and S. E. Wright. Rectangles inscribed in symmetric continua. Geometriae Dedicata, 56(3):285–297,
1995.
[8] L. G. Schnirelman. On some geometric properties of closed curves. Usp. Mat. Nauk, 10:34–44, 1944.
[9] R.E. Schwartz. A trichotomy for rectangles inscribed in jordan loops. arXiv:1804.00740 [math.MG], 2018.
[10] Terence Tao. An integration approach to the toeplitz square peg problem. Forum of Mathematics, Sigma, (5),
2017.
