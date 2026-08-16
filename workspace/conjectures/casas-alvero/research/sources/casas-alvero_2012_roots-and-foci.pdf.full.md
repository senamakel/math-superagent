<!-- source: https://ems.press/content/serial-article-files/44231 | converted from PDF -->

L’Enseignement Math´ematique (2) 58 (2012), 223–248

ROOTS OF COMPLEX POLYNOMIALS
AND FOCI OF REAL ALGEBRAIC CURVES

by Eduardo CASAS-ALVERO ∗ )

ABSTRACT. We give a new proof of results of B. Z. Linﬁeld presenting the roots
of the derivative of a complex polynomial as the foci of a certain real algebraic curve
in the complex plane C.
 1. INTRODUCTION

A nice and old theorem due to J. Siebeck ([12]), also ascribed to F. J. van
den Berg ([13]), asserts that if f ∈ C[z] is a polynomial of the third degree
whose roots z1, z2, z3 , viewed as points in the complex plane, are not aligned,
then the roots of its derivative df /dz are the foci of the unique conic C (an
ellipse in fact) which is tangent to the sides of the triangle z1z2z3 at their
midpoints. For a nice geometric proof based on the focal properties of conics,
see [1]. Other proofs may be found in [10], 1.2.2.
Many generalizations and other proofs of Siebeck’s theorem appeared in
the ﬁrst quarter of the 20th century, the reader may see M. Marden’s paper [8]
and references therein 1 ). Among them, Linﬁeld’s paper [7] is worth noting,
not only because it deals with polynomials of arbitrary degree (and even
rational functions), but especially because it obtains the real algebraic curve
playing the role of the conic C in Siebeck’s result (Siebeck curve)as the
curve enveloped by part of a certain polar curve in the dual plane. This gives
a far clearer insight into the problem and allows one to cover the cases of
particular positions of the roots.

∗ ) Partially supported by MTM-2009-14163-C02-01.
1 ) The original result of Siebeck has recently been named after Marden, which, in view of
the careful historic quotations by Marden himself, makes no sense.

224 E. CASAS-ALVERO

The present paper gives a precise statement and a new proof of Siebeck’s
theorem for polynomials of arbitrary degree following Linﬁeld’s approach
in [7], written according to modern standards. We have in particular addressed a
number of points, such as the zero-dimensional components and the uniqueness
of the Siebeck curve, which received no mention in Linﬁeld’s paper. For the
convenience of the reader, the easier case of non-aligned roots is presented
ﬁrst, in Section 6, while the somewhat more technical general case is dealt
with in Section 7. Further properties of the Siebeck curve and its application
to the location of the roots of the derivative, reﬁning the Gauss-Lucas theorem,
will appear in [2].

ACKNOWLEDGEMENTS. I am indebted to S. del Ba˜no for calling my
attention on the present subject. I also wish to thank J. C. Naranjo and J. Ro´e
for their encouragements and useful discussions.

2. PRELIMINARIES

We will deal with abstract, real or complex, projective planes with an
already ﬁxed system of homogeneous coordinates, and with algebraic curves
C (in the sequel simply called curves) in them, deﬁned by equations F = 0,
F an homogeneous polynomial in the projective coordinates. The point with
homogeneous coordinates (x0, x1, x2) will be denoted [x0, x1, x2] and we will
usually write C : F = 0 to indicate that the curve C has equation F = 0.
A line t is said to be tangent to the curve C at a point p ∈ C if and only if
the intersection multiplicity of t and C at p is higher than the multiplicity
of p on C . The point p is then called a contact point of t and C ,many
contact points being possible for the same tangent. The curve composed of
(possibly repeated) curves Cj : Fj = 0, j = 1,... , r , which by deﬁnition has
equation ∏r=1 Fj = 0 , will be denoted by C1 + ··· + Cr .
Any real projective plane P2 will be viewed as embedded in its complex
extension CP2 , which is obtained by just allowing the homogeneous coor-
dinates to take arbitrary complex values, not all zero. In this situation, the
points of P2 are those which have real coordinates and will be called real
points, while, as usual, the points in CP2 − P2 are called imaginary points.
The (complex) conjugate of [x0, x1, x2] ∈ CP2 is [¯x0, ¯x1, ¯x2] , the bar mean-
ing complex conjugation. The fact that complex conjugation is an involutive
automorphism of C over R, and therefore preserves any type of algebraic
relation, will be used without further mention in what follows.

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 225

Groups of points will be taken to be ﬁnite unordered lists of possibly
repeated points G = {pj}j=1,...,n , the number of times that a point is repeated
being the multiplicity of the point in the group. Groups of points will be
represented as formal sums G = ∑n=0 pj or, showing the multiplicities, after
a suitable renumbering, G = ∑r=0 µjpj , pj ̸= ps if j ̸= s, ∑r=1 µj = n .
The integer n is called the degree,and also the number of points (counted
according to multiplicities) of G .If C and C′ are curves of a projective
plane with no common component, then

C · C′ = ∑

p∈C∩C′[C · C′]p p ,

[ · ]p meaning the intersection multiplicity at p , will be called the inter-
section group of C and C′ . If the points of a group G belong to a
projective line and have there homogeneous coordinates pj = [aj, bj], then
G = ∏n=1(bjx0 − ajx1) = 0 will be taken as an equation for G .Conversely,
any homogeneous polynomial G ∈ R[x0, x1] , of degree n , is a product of n
linear factors in C[x0, x1] , and hence any equation G = 0 is the equation of
a group of n , possibly imaginary, points.
We will consider objects composed of a curve C and a group of points
G in the same plane, represented as G + C : they will be called augmented
curves. A useful convention is to consider both curves and groups of points
as augmented curves (with empty zero-dimensional or one-dimensional part,
respectively).
We will think of the ﬁeld of complex numbers C as a (real) Euclidean
plane, its metric structure being the one deﬁned by the usual absolute value
|z| = √

z ¯z of complex numbers. To avoid confusions, this Euclidean plane
will be denoted by E. Thus, as sets, C = E.If f ∈ C[z] is a polynomial,
its roots, repeated according to their multiplicities, compose a group of points
in E that will be denoted by Z( f ).
Taking, as usual, (x, y) as the coordinates of the complex number x + yi
deﬁnes orthonormal coordinates on E. We will denote by P(E) the projective
closure of E, namely the result of adding to E a line of improper points,
each corresponding to a direction on E. Thus P(E) is a real projective
plane and we take on it the homogeneous coordinates associated to the
above orthonormal coordinates x, y, so that the complex number x + yi has
homogeneous coordinates (1, x, y)in P(E) ; equivalently, x + yi = [1, x, y].
We will also consider the complex extension of P(E) , a further enlargement
of the complex plane according to the sequence

C = E ⊂ P(E) ⊂ CP(E) .

226 E. CASAS-ALVERO

In particular we will deal with the cyclic (or circular) points of the Euclidean
plane E : they are the (improper, imaginary and mutually conjugate) points
I = [0, 1, i]and J = [0, 1, −i] , which determine the metric structure of the
Euclidean plane up to the choice of the unit of length.
We will not distinguish between an algebraic curve C in E, deﬁnedbya
non-homogeneous equation g(x, y) = 0, g ∈ R[x, y] , and its projective closure
in P(E) , deﬁned by the homogeneous equation G = xd g(x1/x0, x2/x0) = 0,
d = deg g . Augmented curves of E will be those composed of a curve in E
and a group of points all belonging to E.
In the sequel we will write simply P for P(E) ; this will cause no confusion.
As for any projective plane, the lines of P are the points of another projective
plane P∨ ,the dual plane of P ; coordinates in P∨ may be taken so that the
line of equation wx0 + ux1 + vx2 = 0in P has coordinates (w, u,v)in P∨ .
Since the condition for the line of coordinates (w, u,v) to belong to the pencil
p∗ , of the lines through a ﬁxed point p = [c, a, b], is

wc + ua + vb = 0 ,

we see that in turn the lines of P∨ are the pencils of lines of P. Any inclusion
p ∈ ℓ , between a point and a line of P, appears reversed, ℓ ∈ p∗ ,in P∨ .
Mapping p∗ ↦→ p is a projectivity through which the bidual space (P∨)∨ is
usually identiﬁed with P.
The same is done with the lines of CP, which are the points of the dual
plane CP∨ of CP. Each line of P being identiﬁed to the line of CP with the
same equation, we see that P∨ ⊂ CP∨ , and the latter appears as the complex
extension of the former. In particular the improper line of P, L∞ : x0 = 0,
appears as the point of P∨ with coordinates (1, 0, 0) , the pencils of lines
through the cyclic points, I∗ , J∗ , are the lines of CP∨ that have equations
u + iv = 0and u − iv = 0 , and their intersection is L∞ , their only real point.
There is a one-to-one correspondence between curves of CP containing
no lines and curves of CP∨ containing no lines, so that the points of the
curve C∗ corresponding to a curve C of CP are the lines tangent to C and,
conversely, the tangent lines to C∗ are the pencils p∗ , p ∈ C .The curve C∗

is called the envelope of C ,and C the curve enveloped by C∗ .Also, C and
C∗ are said to be dual to each other. The degree of C∗ is called the class
of C : it may be viewed as the number of tangent lines to C going through
any already ﬁxed point p , counted with the multiplicities they have in the
group C∗ · p∗ . The latter is a group of lines in p∗ , usually called the group
of tangents to C from p . The reader may see [14], V.8.1 or [5], 5.1. In our
case it is easy to see that if C has a real equation, then also C∗ has a real

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 227

equation, and conversely. Thus the bijection C ↔ C∗ restricts to a bijection
between curves of P and curves of P∨ containing no (real or imaginary)
lines.
We deﬁne the envelope of a group of points G = p1 + ··· + pm ,of CP,to
be the curve G∗ of CP∨ composed of the pencils of lines through the points
of G taken with the same multiplicities, G∗ = p∗ + ··· + p∗ . Then we extend
the above bijection between curve and envelope to a bijection between the set
of augmented curves of CP containing no line and the set of all curves of
CP∨ ,by taking as the envelope of an augmented curve C = G + C the curve
C∗ = G∗ + C∗ , composed of the envelopes of G and C . The augmented curve
C will be referred to as the augmented curve enveloped by C∨ . Obviously
the degree of C∗ equals the class of C plus the number of points of G :we
will callitthe class of the augmented curve C .
An augmented curve as above, C = G + C , is called real if and only if the
curve C is real and for each point p belonging to G , its complex conjugate
also belongs to G and has the same multiplicity as p . The second condition
is obviously satisﬁed if p is real. It is easy to check that real augmented
curves have real envelopes and, conversely, each real curve of P∨ envelops a
real augmented curve of P.
As deﬁned above, a line ℓ is tangent to an augmented curve C = G + C
if and only if either ℓ is tangent to the curve C at a point q or ℓ contains
a point q of G . In both cases q will be called a contact point of ℓ and we
will say that ℓ is tangent to C at q . Assume that p ∈ P does not belong
to G ; then the group of tangents to C from p is deﬁned to be C∗ · p∗ .Itis
well deﬁned because in no case is p∗ ⊂ C∗ , and its elements are the tangents
to C going through p .

3. FOCI OF ALGEBRAIC CURVES

The aim of this section is to recall and reformulate the deﬁnition and some
properties of the foci of algebraic curves, which belong to the today almost
forgotten metric theory of algebraic curves; for more details, the reader may
see Chapter X of [4], as well as the historical notes and references in [6].
We will continue to deal with the Euclidean plane E, but of course, since
any two Euclidean planes are isometric, the content of this section applies
without changes to any Euclidean plane. Let C be a curve of E containing
no real or imaginary line. For simplicity we will assume from now on that
C is not tangent to the improper line, this being enough for our purposes.

228 E. CASAS-ALVERO

The classical deﬁnition (due to Pl¨ucker) extends the usual one for central conics
(see [11], V.9, for instance) by taking the foci of C to be the intersection
points of the pairs of conjugate tangents to C from I and J . Equivalently,
a point q ∈ P is a focus of C if and only if, in the dual plane, the line q∗

joins two conjugate intersections of C∗ with I∗ and J∗ . We will complete
this deﬁnition by assigning multiplicities to the foci. Assume that the class
of C is m, place ourselves in CP∨ and write C∗ · I∗ = ℓ1 + ··· + ℓm .The
lines ℓ1,...,ℓm are thus the tangent lines to C from I , repeated according
to their multiplicities in C∗ · I∗ . Since the equation of C∗ may be taken real
and those of the lines I∗ , J∗ mutually conjugate, the conjugates ¯ℓ1,..., ¯ℓm
of the above ℓj are the intersections of C∗ and J∗ , that is, the tangents to
C from J (repeated according to their multiplicities in C∗ · J∗ ). Since C is
assumed to be not tangent to L∞ ,we have L∞ = I∗ ∩ J∗ /∈ C∗ and therefore
ℓj ̸= ¯ℓj , j = 1,..., m. Thus each pair ℓj, ¯ℓj spans a real line of CP∨ that
does not contain L∞ , that is, a pencil of lines q∗ , qj ∈ E. Each qj is a focus
according to the deﬁnition recalled above and we deﬁne Φ(C) = q1 + ··· + qm
to be the focal group of C .
The above deﬁnition applies without changes to any real augmented curve
C = G + C for which C is a curve of P containing no real or imaginary line
and not tangent to L∞ , these augmented curves being called non-parabolic
in the sequel. As the reader may easily check, the real points of G belong
to the focal group of C with the same multiplicity they have in G . In case
all points of G are real, we have Φ(G + C) = G + Φ(C) . In particular the
focal group of a group of real points is the group itself.
Most of the properties of foci follow from the next proposition, which is
well known and widely used in the case of conics.

PROPOSITION 3.1. Assume that C = G + C is a non-parabolic augmented
curve of class m and let F = 0 be a real homogeneous equation of the
envelope of C . Assume that H is a group of m points of E and that H = 0
is a real equation of the envelope of H .Then H is the focal group of C if and
only if there exist λ ∈ R−{0} and a homogeneous polynomial P ∈ R[w, u,v] ,
of degree m − 2 ,for which

F = λH + (u2 + v2)P .

Proof. We place ourselves in CP∨ . Assume that H = Φ(C) . Then neither
H∗ nor G∗ contains I∗ , because both H and G are composed of proper
points. By the deﬁnition of Φ(C), we have

H∗ · I∗ = C∗ · I∗ .

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 229

Take λ = F(1, 0, 0)/H(1, 0, 0) , which is ﬁnite and non-zero because
[1, 0, 0] = L∞ does not belong to C∗ or H∗ , and is obviously real. Then the
curve D : F − λH = 0of CP∨ has degree m, intersects I∗ at the points of
C∗ · I∗ = H∗ · I∗ with at least the multiplicities they have in the group and
furthermore contains L∞ .ByB´ezout’s theorem, D contains I∗ . Therefore,
since D is a real curve (or just repeating the above argument for J∗ ), D also
contains J∗ and hence contains the pair of lines I∗ + J∗ .Since I∗ + J∗ has
equation u2 + v2 = 0, we have

F − λH = (u2 + v2)P ,

P ∈ C[w, u,v] , homogeneous and of degree m − 2 . By taking conjugates
in the former equality, one sees that P must be real, which proves that the
condition is necessary.
Conversely, since u2 + v2 vanishes identically on I∗ ,

(3.1) H∗ · I∗ = C∗ · I∗ ,

and so, in particular,

(3.2) H∗ ∩ I∗ = C∗ ∩ I∗ .

Take q ∈ H and ℓ = q∗ ∩ I∗ . By Equation (3.2), ℓ ∈C∗ and so ℓ is a tangent
to C from I .Since q is a proper point, ℓ ̸= L∞ . The latter being the only
real line in I∗ , ℓ is imaginary and therefore different from its conjugate ¯ℓ ,
which in turn obviously belongs to both q∗ , C∗ and J∗ . Thus ¯ℓ is a tangent
to C from J and q = ℓ ∩ ¯ℓ is a focus of C .
Call ν the multiplicity of q in H , which by deﬁnition is the multiplicity
of q∗ as an irreducible component of H∗ . Note ﬁrst that no other q∗ ⊂ H∗

contains ℓ , as the same arguments used above would apply to q1 ,giving
q1 = ℓ ∩ ¯ℓ = q . Then, using Equation (3.1),

[C∗ · I∗]ℓ = [H∗ · I∗]ℓ = ν[q∗ · I∗]ℓ = ν,

and so the multiplicities of q in H and Φ(C) are the same. We have seen
thus that all the points q of H belong to Φ(C) with the same multiplicities.
Since both groups of points have the same degree, their equality follows.
 .

The reader may note that if λ and P, taken as in the above statement,
are allowed to vary, then λH + (u2 + v2)P = 0 describes the equations of the
envelopes of all non-parabolic augmented curves with focal group H .

230 E. CASAS-ALVERO

We close this section by showing a nice property of the foci of algebraic
curves, due to Laguerre, that follows easily from Proposition 3.1. Its version
for conics is better known (see [11], VII.5, for instance). We shall not use it
in the sequel.

THEOREM 3.2 (Laguerre). Assume that C is a non-parabolic algebraic
curve of class m, p a point other than the foci of C and ℓ1,...,ℓm the lines
joining p to the foci of C , repeated according to the multiplicities of the foci
in the focal group. If t1 + ··· + tm is the group of tangents to C from p and
we assume that all tangents tj are real, then

m∑

j=1 ̂ℓjtj = 0 ,

where ̂ℓjtj is the angle between the lines ℓj, tj (in whatever manner the foci
and the tangent lines are numbered).

Before proving Theorem 3.2 we introduce an auxiliary result concerning
groups of points on a line :

LEMMA 3.3. Suppose we have three different groups of m points of a
complex projective line P1 ,say A = a1 + ··· + am , B = b1 + ··· + bm and
C = c1 + ··· + cm with linearly dependent equations. Assume also that c1 ̸= c2
and that neither c1 nor c2 belongs to A or B.Then

m∏

j=1(aj, bj, c1, c2) = 1 ,

where (aj, bj, c1, c2) stands for the cross-ratio of aj, bj, c1, c2 .

Proof. Take homogeneous coordinates on P1 such that c1 = [1, 0]
and c2 = [0, 1] . Then any equation of C, H = ∑m=0 hs xm−s
0 xs = 0, has
h0 = hm = 0.
As no point aj is equal to c1 or c2 , these points may be written aj = [αj, 1] ,
αj ̸= 0 , and so we take
 P =
 m∏

j=1(x0 − αjx1) = 0

as an equation for A. Similarly, write bj = [βj, 1] , βj ̸= 0 , and take

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 231

Q =
 m∏

j=1(x0 − βjx1) = 0

as an equation for B.Then wehave

(aj, bj, c1, c2) = βj
αj .

By hypothesis, there is a relation H = λP + µQ, from which, by equating
the coefﬁcients of xm
0 and xm
1 on both sides, we get :

λ + µ = 0and λα1 ... αm + µβ1 ...βm = 0

and so β1
α1 ··· βm
αm = 1

as claimed. .

Proof of Theorem 3.2. In the pencil p∗ , of real and imaginary lines
through p ,wetake A = C∗ · p∗ , the group of tangents to C from p and
B = Φ(C)∗ · p∗ , the group of lines projecting the foci from p . In case A = B
the claim is obviously satisﬁed, as the reader can see. Otherwise, notations
being as in Proposition 3.1, take D to be the curve of P∨ which has equation
(u2 + v2)P = 0 . The inclusion p∗ ⊂ D would imply, by Proposition 3.1,
that A = B, which has been excluded. So we take C = D · p∗ and, by
Proposition 3.1 again, the groups A, B, C satisfy the hypothesis of Lemma 3.3.
In view of the deﬁnition of C we are allowed to take as c1, c2 the lines pI, pJ
joining p to the cyclic points. Since these lines are imaginary, they do not
belong to A or B, and so we may apply Lemma 3.3. Laguerre’s formula (see
[11], IV.8, for instance) gives

̂ℓjtj = 1
2i log(ℓj, tj, pI, pJ) ,

and the assertion follows. .

4. POLAR CURVES AND POLAR GROUPS

We recall the basic deﬁnitions and some easy facts relative to polar curves
and polar groups of points. In order to deal with both cases together, the
deﬁnition and ﬁrst properties will be given in the n -dimensional case; the
reader may assume that n = 1, 2.

232 E. CASAS-ALVERO

Take a real n -dimensional projective space Pn , with ﬁxed homogeneous
coordinates x0,..., xn . Assume given in Pn a point p = [a0,..., an]and a
hypersurface V , with equation F = 0, F ∈ R[x0,... , xn] , homogeneous and
of degree d > 1 . An easy computation shows that the equation

a0 ∂F
∂x0 + ··· + an ∂F
∂xn = 0

is an identity if and only if p is a d -fold point of V (i.e., V is a cone with
vertex p ). Otherwise it deﬁnes a hypersurface of degree d − 1 which is called
the polar of V relative to p (and also the polar of p with respect to V ); it
will be denoted in the sequel by Pp(V).
It is straightforward to verify that the above deﬁnition does not depend
on the coordinates and therefore the relationship between V, p and Pp(V)is
invariant under projectivities. The following results on polars will be used in
the forthcoming sections.

LEMMA 4.1. p /∈ V if and only if Pp(V) is deﬁned and p /∈Pp(V) .

Proof. Simply use Euler’s formula

dF(a0,..., an) =
 n∑

j=0 aj ∂F
∂xj (a0,..., an) .

REMARK 4.2. If p is the last vertex of the projective frame of reference,
p = [0,... , 0, 1] , then the polar has equation ∂F/∂xn = 0 . One may always
assume this to be the case after a suitable choice of projective coordinates.

LEMMA 4.3. If W : F1 = 0 is an irreducible component of multiplicity
µ> 0 of V : F = 0 (that is, F1 is an irreducible factor of multiplicity µ
of F ) and p /∈ V , then W is an irreducible component of multiplicity µ − 1
of Pp(V) .

Proof. Assume that F = Fµ
1 G, with F1 irreducible and not dividing G.
By Remark 4.2 we may assume an equation of the polar to be
∂F
∂xn = Fµ−1
1
 (
µ ∂F1
∂xn G + F1 ∂G
∂xn
 ) = 0 .

Since p /∈ V , it does not belong to W either. Then, by Lemma 4.1, Pp(W)is
deﬁned and so ∂F1/∂xn does not vanish identically. In the equality displayed
above, F1 does not divide ∂F1/∂xn or G, because of its degree and the
hypothesis. Thus F1 is an irreducible factor of multiplicity µ − 1of the
equation of Pp(V) , as claimed. .

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 233

Assume that p , ℓ and C are, respectively a point, a line and a curve of
P2 , with p ∈ ℓ , p /∈ C .Then ℓ ̸⊂ C , C · ℓ is a group of points of ℓ and
we may consider its polar Pp(C · ℓ) , which is deﬁned by Lemma 4.1. Also
Pp(C) is deﬁned, for the same reason, and we have :

LEMMA 4.4. Hypothesis and notations being as above, we have

Pp(C) · ℓ = Pp(C · ℓ) .

Proof. Take coordinates with p = [0, 0, 1] and ℓ : x1 = 0. Then x0, x2
may be taken as coordinates on ℓ and, relative to them, C · ℓ has equation
F(x0, 0, x2) = 0 . Then the assertion follows from Remark 4.2 and the obvious
equality ∂F
∂x2 (x0, 0, x2) = ∂F(x0, 0, x2)
∂x2 .

In the sequel we denote by TCq(C)the tangent cone to a plane curve
C at one of its points q . The pencil q∗ of the lines through q is a line
of the dual plane P∨ and in particular a one-dimensional projective space.
Since the tangent cone TCq(C) is composed of lines through q counted
with multiplicities, it is a group of points of the one-dimensional projective
space q∗ . It thus makes sense to consider, in q∗ , the polar group of TCq(C)
relative to any line through q .We have :

LEMMA 4.5. Let C be a curve of P2 and q an e-fold point of C , e > 1 .
Assume that p ̸= q is a point of P2 such that the line qp does not belong to
TCq(C) . Then the polar Pp(C) is deﬁned, q is a point of multiplicity e − 1
of Pp(C) and Pqp(TCq(C)) = TCq(Pp(C)) .

Proof. Take projective coordinates so that q = [1, 0, 0] and p = [0, 0, 1] .
Assume that C has degree d and equation

F = Fexd−e
0 + ··· + Fd = 0 ,

each Fj being a homogeneous polynomial in x1, x2 . Then the tangent cone
TCq(C) has equation Fe = 0. If Fe is written as a product of powers of
distinct linear factors,
 Fe(x1, x2) =
 r∏

j=1(ujx1 + vjx2)µj ,

234 E. CASAS-ALVERO

then TCq(C) is composed of the lines ℓj = [0, uj,vj], j = 1,... , r , with
multiplicities µj . Then each ℓj has coordinates uj,vj in q∗ and so

Fe(v, −u) =
 r∏

j=1(ujv − vju)µj = 0

is an equation of TCq(C) as a group of points in q∗ . The line qp has equation
x1 = 0 , hence coordinates (0, 1, 0) in P∨ and thus coordinates (1, 0) in q∗ .
The polar group Pqp(TCq(C)) , which is well deﬁned by Lemma 4.1, thus has
equation

(4.1) ∂Fe(v, −u)

∂u = − ∂Fe
∂x2 (v, −u) .

On the other hand, since we know from the above that ∂Fe/∂x2 is not
identically zero, neither is

∂F
∂x2 = ∂Fe
∂x2 xd−e
0 + ··· + ∂Fd
∂x2 = 0

identically. This expression can therefore be taken as an equation for Pp(C).
Still using that ∂Fe/∂x2 is not identically zero, since it has degree e − 1,
q has multiplicity e − 1in Pp(C) . Furthermore, an equation of TCq(Pp(C))
is ∂Fe
∂x2 = 0 .

As argued for TCq(C) , substituting (v, −u)for(x1, x2) in the above equation
yields an equation of TCq(Pp(C)) as a group of points of q∗ . The result of
the substitution is ∂Fe
∂x2 (v, −u) = 0;

comparing with Equation (4.1) concludes the proof. .

LEMMA 4.6. Suppose we have a group G = µ1p1 + µ2p2 , of two different
points of an afﬁne line A1 , and let p∞ be the improper point of A1 .Then
Pp∞ (G) = (µ1 − 1)p1 + (µ2 − 1)p2 + p where p is the point dividing the
segment p1p2 in the ratio µ2/µ1 .

Proof. Take an afﬁne coordinate x on A1 and the homogeneous coor-
dinates x0, x1 associated to it ( x = x1/x0 ). If p1, p2 have afﬁne coordinates
α1,α2 ,take (x1 − α1x0)µ1(x1 − α2x0)µ2 = 0

as an equation of G .Since p∞ = [0, 1] , Pp∞ (G) has equation

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 235

(x1 − α1x0)µ1−1(x1 − α2x0)µ2−1(
µ1(x1 − α2x0) + µ2(x1 − α1x0)) = 0 ,

which, using the afﬁne coordinate, is

(x − α1)µ1−1(x − α2)µ2−1(
µ1(x − α2) + µ2(x − α1)) = 0 .

Then there is in Pp∞(G) a single point p other than p1, p2 , and its afﬁne
coordinate α satisﬁes
 µ1(α − α2) + µ2(α − α1) = 0 ,

as stated. .
 5. LINFIELD’S THEOREM

THEOREM 5.1 (Linﬁeld). Assume that D is a non-parabolic augmented
curve whose focal group is the group of roots of a polynomial f ∈ C[z] ,
d = deg f > 1 . Then the polar relative to the improper line of the envelope
of D envelops a non-parabolic augmented curve C ,of class d − 1 , whose
focal group is the group of roots of df /dz.

In particular, if D is simply a group of points, we have :

COROLLARY 5.2. Assume that G is the group of roots of a polynomial
f ∈ C[z] ,d = deg f > 1 . Then the polar relative to the improper line of the
envelope of G envelops a non-parabolic augmented curve C ,ofclass d − 1 ,
whose focal group is the group of roots of df /dz.

Proof of Theorem 5.1. Denote, as before, by w, u,v the coordinates
on P∨ , consider the ring homomorphism

ψ : R[w, u,v] −→ C[z]

F(w, u,v) ↦−→ F(z, −1, −i)

and note the following easy facts :
(1) For any F ∈ R[w, u,v] , it clearly follows from the deﬁnition that

d
dz ψ(F) = ψ( ∂F
∂w
 ).

(2) ψ(u2 + v2) = 0 ; therefore if F = 0 is an equation of the envelope
of a non-parabolic augmented curve C ,and H = 0 an equation of the
envelope of the focal group of C , then by Proposition 3.1, ψ(F) = λψ(H),
λ ∈ R −{0} .

236 E. CASAS-ALVERO

(3) If z1,..., zd are complex numbers and F = 0 is an equation of the
envelope of the group of points of E which they compose, then ψ(F)
has roots z1,..., zd . For, in case d = 1, if z1 = a + bi, then, up to a
non-zero real factor, F = w + av + bu and so ψ(F) = z − (a + bi). The
case d > 1 follows because ψ is a ring homomorphism.

To conclude the proof, assume that F = 0 is an equation for the envelope
of D . By (2) and (3) above, ψ(F) = cf for a suitable c ∈ C −{0} .
Since D is assumed to be non-parabolic, L∞ /∈D∗ ; as seen in Lemma 4.1,
L∞ /∈PL∞ (D∗) , hence C is also non-parabolic. An equation of PL∞ (D∗)
being ∂F/∂w = 0 , on the one hand ψ(∂F/∂w) = cdf /dz, by (2), while on
the other hand, by (1), ψ(∂F/∂w) = ψ(H)where H is a suitable equation
of the envelope of the focal group of C . Since, by (3), ψ(H) has the focal
group as group of roots, the claim follows. .

REMARK 5.3. It follows from Theorem 5.1 that for 1 ≤ r ≤ d − 1, the
r -th order iterated polar, relative to the improper line, of the envelope of D
in Theorem 5.1 (or G in Corollary 5.2) envelops a non-parabolic augmented
curve, of class d − r , whose focal group is the group of roots of drf /dz
r .

6. THE NICEST CASE

The envelope of the augmented curve C of Corollary 5.2 is the polar,
relative to the improper line, of a curve composed of real lines. Due to this,
C has a number of special properties that provide an alternative presentation
of C . Since for each multiple root zj of f , say of multiplicity µj , the pencil z
∗
appears as a component of multiplicity µj − 1of C∗ (by Lemma 4.3), in the
sequel we will discard these obvious components of C∗ and focus our attention
on the remaining curve S∗ and its enveloped augmented curve S .In this
section we will deal with the case of non-aligned roots. The next theorem is
a direct generalization of Siebeck’s result quoted in the introduction :

THEOREM 6.1. Assume that f (z) ∈ C[z] has distinct roots z1,... , zm ,
m > 1 , with respective multiplicities µ1,... ,µm , no three of the zi being (as
points of the complex plane) aligned. For each pair j, s, 1 ≤ j < s ≤ m, let
pj,s be the point which divides the segment with extremities zj, zs in the ratio
µs/µj (i.e., pj,szj/pj,szs = µs/µj ). Then :

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 237

(1) In the complex plane there is a unique augmented curve S ,of class
m − 1 , tangent to each of the lines zjzs , 1 ≤ j < s ≤ m, at the point pj,s .
(2) S is non-parabolic and its foci agree, multiplicities included, with the
roots of the derivative df /dz other than z1,..., zm .Inother words,

Z(df /dz) = Φ(S) +
 m∑

j=1 (µj − 1)zj .

Proof. Take C∗ = PL∞ (µ1z
∗+···+µmz
∗ ) . By Corollary 5.2, the enveloped
augmented curve C is non-parabolic and its focal group is the group of roots
of df /dz. On the one hand, the roots zj , j = 1,... , m,of f appear with
multiplicities µj − 1 in the group of roots of df /dz. On the other hand, by
Lemma 4.3, each pencil z
∗ appears as a component of multiplicity µj − 1
of C∗ . Then we write

C∗ = (µ1 − 1)z
∗ + ··· + (µm − 1)z
∗ + S∗

and take S to be the augmented curve enveloped by S∗ .Then S is non-
parabolic too and the focal group Φ(C) is composed of the points zj , with
multiplicities µj − 1, j = 1,... , m, plus the focal group of S : the latter is
thus the group of roots of df /dz other than the zj , j = 1,... , m, and assertion
(2) is established.
Regarding assertion (1), denote by ℓj,s the line of E joining zj, zs ,
1 ≤ j < s ≤ m, and call its improper point qj,s . Since no three zj are
aligned, the ℓj,s are all different and so each ℓj,s is a singular point of
µ1z
∗ + ··· + µmz
∗ at which the latter has tangent cone

TCℓj,s (µ1z
∗ + ··· + µmz
∗ ) = µjz
∗ + µsz
∗ .

The line (of P∨ ) joining ℓj,s and L∞ is q∗,s ̸= z
∗, z
∗ . Then, by Lemmas 4.5
and 4.3, the tangent cone to the polar C∗ at ℓj,s is

(6.1) Pq∗,s(µjz
∗ + µsz
∗) = (µj − 1)z
∗ + (µs − 1)z
∗ + tj,s ,

where tj,s is a line of P∨ through ℓj,s , tj,s ̸= z
∗, z
∗ . By omitting the components
(µj − 1)z
∗ and (µs − 1)z
∗ , it follows that

TCℓj,s(S∗) = tj,s ,

and so ℓj,s is a simple point of S∗ at which the tangent line is tj,s . Dualizing,
ℓj,s is tangent to S as claimed and, its contact point being already named
pj,s ,wehave tj,s = p∗,s .

238 E. CASAS-ALVERO

Equality (6.1) may thus be rewritten

Pq∗,s(µjz
∗ + µsz
∗) = (µj − 1)z
∗ + (µs − 1)z
∗ + p∗,s ,

or, equivalently, by biduality and the projective invariance of the polarity
relationship,
 Pqj,s(µjzj + µszs) = (µj − 1)zj + (µs − 1)zs + pj,s .

The last equality and Lemma 4.6 guarantee that pj,s belongs to the segment
with endpoints zj, zs and divides it in the ratio µs/µj .
Lastly, to prove the uniqueness of an augmented curve subjected to the
conditions of assertion (1), it is enough to prove the uniqueness of its envelope,
which in turn follows directly from Lemma 6.2 below.
 .

LEMMA 6.2. Assume there are given, in a real projective plane P2 , lines
L1,... , Lm ,m ≥ 2 , no three concurrent. For each pair s, j( j < s), write
Pj,s = Lj ∩ Ls and assume we have ﬁxed a line Tj,s through Pj,s ,Tj,s ̸= Lj, Ls .
Then there is at most one curve C of P2 ,of degree m − 1 , going through
all the Pj,s and having tangent Tj,s at each Pj,s .

Proof. Let C be a curve satisfying the above conditions. We begin by
showing that C cannot contain any of the lines Lj . Indeed, up to renumbering
the lines, assume that C = rL1 + C1 ,deg C1 < m − 1and C1 ̸⊃ L1 .Then
C1 has to be tangent to each T1,s at P1,s , s = 2,... m, because L1 is not.
In particular L1 ∩ C1 contains P1,2,... , P1,m , in contradiction to the B´ezout
theorem.
Once we know that C contains no Lj , note that, for j = 1,... , m and
again by B´ezout’s theorem, there are no intersections of C and Lj other than
the m − 1 points Pk,s lying on Lj , the latter are simple intersections of C
and Lj and so, in particular, non-singular points of C .
Assume now that two different curves C : F = 0and C′ : F′ = 0 satisfy
the above conditions. Call Θ the pencil of curves spanned by C and C′ ,
namely the family of the curves with equations

λF + λ
′F′ = 0 , (λ, λ
′) ∈ R2 −{0, 0}.

It is clear from these equations that any curve in Θ goes through any point
shared by C and C′ , and so in particular through all the points Pj,s ,and
has at Pj,s intersection multiplicity higher than one with Ti, j , because both
C and C′ have. It is also clear that for any point P ∈ P2 there is at least
one curve in Θ going through P.If P is taken on Lj and different from all

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 239

the Pk,s ,weget a curve Cj ∈ Θ sharing more than m − 1 points with Lj
and hence (once again by B´ezout’s theorem) containing it. If Pk,s ∈ Lj ,then
both lines Lj and Tk,s have intersection multiplicity with Cj higher than one,
hence such a Pk,s is a singular point of Cj . Assume now that two of the
curves Cj , say, up to renumbering, C1 and C2 , are different. Then C1 and
C2 span Θ and both have P1,2 as a singular point. It follows that all curves
in Θ , in particular C ,have P1,2 as a singular point, in contradiction to what
we have already proved for C . Thus C1 = ··· = Cm , which would be a curve
of degree m − 1 containing m different lines, a contradiction which proves
the uniqueness of C . .

REMARK 6.3. If all roots of f are simple, then each pj,s is the midpoint
of zj, zs .

REMARK 6.4. The number of conditions imposed on S in Theorem 6.1 (1)
is m(m − 1) , always larger than the number m(m + 1)/2 − 1 of parameters
(the ratios between the coefﬁcients of the equation of its envelope) on which
a general curve of class m − 1 depends. Thus, the existence of S is a priori
not clear.

REMARK 6.5. The augmented curve S of Theorem 6.1 will be called the
Siebeck curve of f . It is important to retain that, besides its characterization
in Theorem 6.1, the Siebeck curve of f is the augmented curve enveloped by

PL∞ (µ1z
∗ + ··· + µmz
∗ ) − (µ1 − 1)z
∗ − ··· − (µm − 1)z
∗ .

EXAMPLE 6.6. Take f = z
4 − 1 , whose roots 1, −1, i, −i, all simple, are
the vertices of a square. The envelope of the group of roots has equation

(w + u)(w − u)(w + v)(w − v) = w4 − w2u2 − w2v2 + u2v2 = 0 .

Its polar relative to L∞ = [1, 0, 0] thus has equation

4w3 − 2wu2 − 2wv2 = 0

and so splits into w = 0 , the pencil of lines through the origin O = 0
of the complex plane, and the envelope 2w2 − u2 − v2 = 0of the circle
C : x2 + y2 − 1/2 = 0 . The Siebeck curve of f is thus S = O + C : C is
tangent to the four sides of the square at their midpoints, while O is the
midpoint of the two diagonals, according to the conditions of Theorem 6.1 (1).
Since the focal group of C is 2O, the focal group of S is 3O in accordance
with df /dz = 4z
3 .

240 E. CASAS-ALVERO

The next example was given a direct proof in [9] :

EXAMPLE 6.7. Let f be a polynomial with only simple roots z1,... , zm .
Assume that z1,..., zm are the images by an afﬁne map of the vertices of
a regular m-gon. Take i = 1,... , m and read the indices mod m. Then, for
each s ﬁxed, 1 ≤ s < m/2 , all the segments zizi+s are tangent to an ellipse
Cs at their midpoints and, furthermore, if m is even, all segments zizi+m/2
have the same midpoint, called O in the sequel. Indeed, both properties are
afﬁne-invariant and obvious in the case of a regular polygon. It follows from
Theorem 6.1 that the Siebeck curve of f is either S = C1 + ··· + C(m−1)/2 ,if
m is odd, or S = O + C1 + ··· + C(m−2)/2 if m is even. The group of roots
of df /dz is then

Z( df
dz ) = Φ(S) =
 {Φ(C1) + ··· + Φ(C(m−1)/2)if m is odd ,

O + Φ(C1) + ··· + Φ(C(m−2)/2)if m is even .

EXAMPLE 6.8. Assume that f has simple roots 0, 1, 2i, 5 + 3i. Since the
roots are simple, the polar of the envelope of the group of roots is the envelope
of the Siebeck curve S of f . A direct computation gives

S∗ :4w3 + 18w2u + 15w2v + 10wu2 + 12wv2 + 30wuv + 10u2v + 6uv2 = 0 ,

which is a non-singular cubic of P∨ .Then S is a sextic of P with 9 cusps,
three of which are real, see Figure 1.

7. THE GENERAL CASE

From now on, we will no longer assume that no three roots of f are
aligned. If three or more distinct roots of f lie on a line ℓ , there is still an
augmented curve S , determined by the roots of f , whose foci are the roots
of df /dz other than the roots of f . The main difference with the case of
Theorem 6.1 is that the lines containing three or more roots appear as multiple
tangents to S ; their contact points are still determined by the roots of f lying
on the line, but the determination is less explicit than in Theorem 6.1. The
next deﬁnition will help to locate these contact points.

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 241

1 2 3 4 5

0.5

1

1.5

2

2.5

3
 FIGURE 1
The lines joining the roots of f in Example 6.8,
the Siebeck curve S and its three foci

Assume that G = ∑r=1 µjqj , with qj ̸= qs if j ̸= s, is a group of points
of a real afﬁne line A1 .If q∞ is the improper point of A1 , we call

H(G) = Pq∞(G) −
 r∑

j=1 (µj − 1)qj

the harmonic group of G ; this makes sense by Lemma 4.3.

EXAMPLE 7.1. In Lemma 4.6, the point p is a single-point harmonic group.

LEMMA 7.2. The harmonic group of a group of points G = ∑r=1 µjqj ,
q1,..., qr distinct points of a real afﬁne line, consists of r − 1 distinct points,
all real and of multiplicity one. Furthermore, any two consecutive points of
G have just one of the points of the harmonic group between them.

Proof. If x is an afﬁne coordinate on A1 and x0, x1 its corresponding
homogeneous coordinates (x = x1/x0 ), then q∞ has homogeneous coordinates
(0, 1) . If G(x0, x1) = 0 is an homogeneous equation of G ,then g = G(1, x)is
a polynomial of degree d = µ1+···+µr whose roots are the afﬁne coordinates
αj of the qj , each root αj having multiplicity µj . Since the polar group has
equation ∂G/∂x1 = 0 , similarly the roots of (∂G/∂x1)(1, x) = dg/dx are the
αj with multiplicities µj − 1, j = 1,... , r , together with the afﬁne coordinates
of the points of the harmonic group, the multiplicity of each root equal to the

242 E. CASAS-ALVERO

multiplicity of the corresponding point in the harmonic group. Then Rolle’s
theorem ensures that there is at least one point of the harmonic group between
any two consecutive points of G . Since, by its deﬁnition, the harmonic group
contains at most d − 1 − ∑r=1(µj − 1) = r − 1 points, there is just one point
of the harmonic group between any two consecutive points of G ,there areno
further (real or imaginary) points in the harmonic group, and all multiplicities
are one, as required.
 .

THEOREM 7.3. Assume that f (z) ∈ C[z] has m > 1 distinct roots
z1,... , zm , with respective multiplicities µ1,... ,µm . For each line ℓ joining
two different roots of f , let Gℓ be the group of the roots of f lying on ℓ ,
counted with their multiplicities as roots. Then :
(1) In the complex plane there is a unique augmented curve S ,of class
m − 1 and tangent to each line ℓ joining two roots of f at each of the
points of the harmonic group of Gℓ .
(2) S is non-parabolic and Z(df /dz) = Φ(S) + ∑j=1(µj − 1)zj .

Proof. As in the proof of Theorem 6.1, take

C∗ = PL∞ (µ1z
∗ + ··· + µmz
∗ ) = (µ1 − 1)z
∗ + ··· + (µm − 1)z
∗ + S∗.

The arguments used there prove that the augmented curve S , enveloped by S∗ ,
satisﬁes assertion (2).
Assume that ℓ is a line joining two roots of f and that, after a suitable
renumbering, the roots of f on ℓ are z1,... , zr . Denote by q∞ the improper
point of ℓ . We will work in P∨ for a while. Clearly, the tangent cone to
µ1z
∗ + ··· + µmz
∗ at ℓ is G∗ = µ1z
∗ + ··· + µrz
∗ and L∞ does not belong
to it. Then, by Lemma 4.5, the tangent cone to C∗ at ℓ is the polar (in the
pencil of lines of P ∨ through ℓ )of G∗ relative to the line q∗ joining ℓ
to L∞ . By Lemma 4.3,

Pq∗ (G∗) = (µ1 − 1)z
∗ + ··· + (µr − 1)z
∗ + t1 + ··· + tr−1 ,

where t1,..., tr−1 are lines of P∨ through ℓ , tj ̸= z
∗ ,for j = 1,... , r − 1
and s = 1,... , r . Hence t1 + ··· + tr−1 is the tangent cone to S∗ at ℓ and
therefore tj = p∗ where p1,... , pr−1 are the contact points of ℓ and S .
The above equality thus reads

Pq∗ (G∗) = (µ1 − 1)z
∗ + ··· + (µr − 1)z
∗ + p∗ + ··· + p∗−1 ,

which, returning to P by identifying lines of P∨ to points of P by biduality,

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 243

gives Pq∞(Gℓ) = (µ1 − 1)z1 + ··· + (µr − 1)zr + p1 + ··· + pr .

This shows that the contact points p1,... , pr−1 are the points of the harmonic
group of Gℓ .
As in the proof of Theorem 6.1, the uniqueness of S follows from the
next lemma, which is just a more general version of Lemma 6.2. .

LEMMA 7.4. Let Λ be a set of m distinct lines of a real projective
plane P2 . Denote by Π the set of points belonging to at least two lines in Λ
and, for each P ∈ Π,by ΛP the set of lines in Λ going through P. For each
P ∈ Π, denote by νP the number of lines in ΛP and assume given νP − 1
different lines through P, TP,1,..., TP,νp−1 , none in Λ. Then there is at most
one curve C , of degree m − 1 , which, for all P ∈ Π, goes through P and
has tangents TP,1,..., TP,νp−1 at P.

Proof. For each L ∈ Λ, the lines other than L in Λ being m − 1in
number,

(7.1) m − 1 = ∑

P∈L(νP − 1) ,

which is the number of prescribed tangents at the points on L .
Assume that C satisﬁes the conditions stated in the conclusion, and ﬁx
L ∈ Λ. As in the proof of Lemma 6.2, L ̸⊂ C , since if not, C = rL + C′ ,
deg C′ < m − 1, L ̸⊂ C′ , by Equation (7.1), C′ would have at least m − 1
different tangents at points on L , contradicting B´ezout’s theorem.
The prescribed tangents at P ∈ Π are νP − 1 in number, hence the
multiplicity eP(C), of C at P,is eP(C) ≥ νP − 1 . Then for any line L ∈ Λ,
by B´ezout and Equation (7.1),

m − 1 ≥ ∑

P∈L∩Π eP(C) ≥ ∑

P∈L∩Π
(νP − 1) = m − 1 .

This ensures that eP(C) = νP − 1for all P ∈ L ∩ Π and, since L is arbitrary,
also for all P ∈ Π.
Assume that there are two curves C, C′ satisfying the stated conditions.
Arguing as in the proof of Lemma 6.2, C, C′ span a pencil Θ of curves of
degree m − 1 in which, for each L ∈ Λ, there is a curve CL containing L .For
any P ∈ L , L and TP,1,..., TP,νP−1 have with CL intersection multiplicity at
P higher than νP − 1 . This forces eP(CL) >νP − 1. If CL ̸= CL′ then they
span Θ and both have multiplicity higher than νP − 1at P = L∩L
′ . Therefore

244 E. CASAS-ALVERO

all curves in Θ , in particular C , have multiplicity higher than νP − 1at P,
contradicting what we have seen above.
Lastly, if all the CL agree, a curve of degree m − 1 would contain all of
the m distinct lines in Λ, which is absurd. .

REMARK 7.5. Theorem 7.3 is simply a more general version of Theo-
rem 6.1, just note Example 7.1 and Lemma 4.6.

REMARK 7.6. Still in the more general case of Theorem 7.3 we have

S∗ = PL∞ (µ1z
∗ + ··· + µmz
∗ ) − (µ1 − 1)z
∗ − ··· − (µm − 1)z
∗ ,

and the augmented curve S will be called the Siebeck curve of f .

COROLLARY 7.7 (of the proof of Theorem 7.3). A line ℓ containing exactly
r > 1 distinct roots of f is an ordinary singularity of multiplicity r − 1 of
S∗ (a non-singular point if r = 2 ) with real tangents.

Proof. The smooth and the ordinary singular points of a curve are those
at which the number of tangents to the curve is equal to the multiplicity of
the point. In the proof of Theorem 7.3 we have seen that, using the notation
introduced there, the tangent cone to S∗ at ℓ is p∗ + ··· + p∗−1 and also that
p1 +···+pr−1 is a harmonic group, so the claim follows from Lemma 7.2.
 .

The singularities of a curve C∗ in the dual plane are called tangential
singularities of the enveloped (possibly augmented) curve C . The ordinary
singularities of C∗ are called ordinary multiple tangents of C : the number of
contact points of an ordinary multiple tangent is equal to its multiplicity (as a
point of C∗ ). In our case, a line ℓ containing exactly r > 1 distinct roots of
f is either a non-singular tangent to S ,if r = 2 , or an ordinary (r − 1) -fold
tangent with all its contact points real, if r > 2 . Next is an example with a
three-fold tangent.

EXAMPLE 7.8. Take f = z(z+ 1)(z− 2)(z+ 3)(z− 1 − i) . Then the envelope
of the roots is
 w(u − w)(2u + w)(3u − w)(u + v + w) = 0

and so

S∗ :6u4 + 6u3v + 2u3w − 10u2vw − 21u2w2 − 6uvw2 − 4uw3 + 4vw3 + 5w4 = 0,

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 245

which is a quartic of P∨ with an ordinary triple point at [0, 0, 1] , hence
rational. The Siebeck curve S is then a rational sextic of class four. See
Figure 2.

-3 -2 -1 1 2

0.2

0.4

0.6

0.8

1

FIGURE 2
The lines joining the roots of f in Example 7.8,
the Siebeck curve of f and its four foci

8. FURTHER PROPERTIES OF THE SIEBECK CURVE

A pencil of parallel lines p∗ , p a (real) improper point of E, is a one-
dimensional projective space in which L∞ is a distinguished element : taking
L∞ as the improper element deﬁnes on p∗ a structure of an afﬁne line. In
what follows we will take all pencils of parallel lines endowed with this afﬁne
structure and use, in particular, the betweenness relation on parallel lines. The
reader may note that if ℓ is any line of E transverse to p∗ (that is, with
p /∈ ℓ ), then mapping each line of p∗ to its intersection with ℓ is a projectivity
which maps the improper line to the improper point, hence an afﬁne map. In
particular, regarding betweenness, L lies between L1 and L2 if and only if
L ∩ ℓ lies between L1 ∩ ℓ and L2 ∩ ℓ ,for any L, L1, L2 ∈ p∗ −{L∞} .

246 E. CASAS-ALVERO

Fix a pencil of parallel lines p∗ , p ∈ L∞ ,of E, and consider in it the
group of lines Lp = ∑m=1 µjzjp , composed of the lines through the roots of
f in the direction of p , each counted with multiplicity equal to the sum of
multiplicities of the roots of f lying on it. For each line L in Lp ,take rL
to be the number of different roots of f on L . Note that rL = 1for all L
except in the case in which p is the improper point of a line joining two
different roots of f . The main result in this section is :

PROPOSITION 8.1. With the above notation, the group of tangents to S
from an improper (real) point p is

H(Lp) + ∑

L∈Lp(rL − 1)L ,

where H(Lp) denotes the harmonic group of Lp .

Proof. For each line L joining p to one of the roots of f , we write
zL,1,..., zL,rL for the roots of f lying on L . By Lemma 4.4,

PL∞ (µ1z
∗ + ··· + µmz
∗ ) · p∗ = PL∞ ((µ1z
∗ + ··· + µmz
∗ ) · p∗) = PL∞ (Lp) .

On the one hand, by Remark 7.6,

PL∞(µ1z
∗ + ... + µmz
∗ ) · p∗

= S∗ · p∗ + (µ1 − 1)z
∗ · p∗ + ··· + (µm − 1)z
∗ · p∗

= S∗ · p∗ + (µ1 − 1)z1p + ··· + (µm − 1)zmp

= S∗ · p∗ + ∑

L∈Lp(µL,1 + ··· + µL,rL − rL)L .

On the other hand,

PL∞ (Lp) = H(Lp) + ∑

L∈Lp(µL,1 + ··· + µL,rL − 1)L

and the conclusion follows.
 .

COROLLARY 8.2. The Siebeck curve of f has no real tangential singularity
other than the lines joining three or more distinct roots of f and so, in
particular, no real tangential singularity at all if no three distinct roots of f
are aligned.

Proof. If a real line ℓ is a singular point of S∗ , then it appears with
multiplicity higher than one in any group S∗ · p∗ for any p ∈ ℓ . The point p
can be taken improper (and real), in which case Proposition 8.1 applies and
shows that ℓ must be a line joining at least three roots of f . .

ROOTS OF POLYNOMIALS AND FOCI OF REAL CURVES 247

REMARK 8.3. Besides the multiple tangents of Corollary 8.2, S may have
imaginary tangential singularities, for instance the tangents from O to C in
Example 6.6.

From Corollaries 8.2 and 7.7 there follows :

COROLLARY 8.4. All real tangential singularities of the Siebeck curve S
of f are ordinary multiple tangents with the property that all their contact
points are real.

The tangents at the inﬂection points of a curve are non-ordinary tangential
singularities ([14], V.8.1 or [5], 5.5), hence by Corollary 8.4 :

COROLLARY 8.5. A Siebeck curve has no real inﬂection points.

The reader used to dealing with singularities and duality for plane curves
will encounter no difﬁculty in deducing from Corollary 8.2 that all real
branches of a Siebeck curve have class one (see for instance [3], Exercise
5.2), no two different branches having the same tangent, except for those
tangent to one of the multiple tangents described in Corollary 7.7.
To conclude, the next corollary ensures that a Siebeck curve is bounded :

COROLLARY 8.6. A Siebeck curve has no real improper points.

Proof. If p is a real improper point of S ,then p∗ is a line of P∨ tangent
to S∗ , and so either p∗ ⊂ S∗ or S∗ · p∗ contains at least one point (line of P)
with multiplicity higher than its multiplicity in S∗ . Proposition 8.1 shows that
neither of these possibilities can occur. .

REFERENCES

[1] B ˆOCHER, M. Some propositions concerning the geometric representation of
imaginaries. Ann. of Math. 7 (1892/93), 70–76.
[2] CASAS-ALVERO, E. Siebeck curves and two reﬁnements of the Gauss-Lucas
theorem. Math. Scand. 111 (2012), 12–41.
[3] Singularities of Plane Curves. London Mathematical Society Lecture
Note Series 276. Cambridge University Press, Cambridge, 2000.
[4] COOLIDGE,J. L. A Treatise on Algebraic Plane Curves. Oxford University
Press, London, 1931.

248 E. CASAS-ALVERO

[5] FISCHER,G. Plane Algebraic Curves. Translated from the 1994 German original
by Leslie Kay. Student Mathematical Library 15.Amer. Math.Soc.,
Providence, RI, 2001.
[6] HILTON,H. and S. D. JERVIS. On the real foci and directrices of a class cubic
and other plane algebraic curves. Proc. London Math. Soc. (2) 27 (1928),
427–434.
[7] LINFIELD, B. Z. On certain polar curves with their application to the location
of the roots of the derivatives of a rational function. Trans. Amer. Math.
Soc. 25 (1923), 239–258.
[8] MARDEN, M. A note on the zeros of the sections of a partial fraction. Bull.
Amer. Math. Soc. 51 (1945), 935–940.
[9] PARISH, J. L. On the derivative of a vertex polynomial. Forum Geom. 6 (2006),
285–288.
[10] PRASOLOV,V. V. Polynomials. Translated from the 2001 Russian second edition
by Dimitry Leites. Algorithms and Computation in Mathematics 11.
Springer-Verlag, Berlin, 2004.
[11] SEMPLE,J. G. and G. T. KNEEBONE. Algebraic Projective Geometry. Oxford
University Press, 1963.
[12] SIEBECK, J. Ueber eine neue analytische Behandlungsweise der Brennpunkte.
J. Reine Angew. Math. 64 (1865), 175–182.
[13] VAN DEN BERG, F. J. Nogmaals over afgeleide wortelpunten. Nieuw Archief
voor Wiskunde 15 (1889), 100–164.
[14] WALKER,R. J. Algebraic Curves. Dover Publications, Inc., New York, 1962;
unabridged and corrected reprint of the work ﬁrst published as Princeton
Mathematical Series 13. Princeton University Press, Princeton, N. J.,
1950.
 (Rec¸u le 4 juillet 2010)

Eduardo Casas-Alvero
Departament d’ `Algebra i Geometria
Universitat de Barcelona
Gran Via 585
E-08007 Barcelona
Spain
e-mail : casasalvero@ub.edu
