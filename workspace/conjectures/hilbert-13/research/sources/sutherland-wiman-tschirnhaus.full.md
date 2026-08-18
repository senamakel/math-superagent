<!-- source: https://arxiv.org/pdf/2106.09247 | converted from PDF -->

arXiv:2106.09247v1  [math.HO]  17 Jun 2021
On the Application of Tschirnhaus Transformations to the
Reduction of Algebraic Equations

A Translation by Alexander J. Sutherland

June 18, 2021

1 Original Bibliographic Information

1.1 German

• Author: Anders Wiman

• Title: ¨Uber die Anwendung der Tschirnhausen-Transformation auf die Reduktion algebraischer Gle-
ichungen

• Year: 1927

• Language: German

• Publisher: Nova Acta Regiae Societatis Scientiarum Upsaliensis (Nova Acta R. Soc. scient. Uppsala)

• Note: Der K¨onigi. Societ¨at der Wissenschaften Zu Uppsala Mitgeteilt

1.2 English

• Author: Anders Wiman

• Title: On the Application of Tschirnhaus Transformations to the Reduction of Algebraic Equations

• Year: 1927

• Language: German

• Publisher: New Proceedings of the Royal Society of Scientists of Uppsala

• Note: Notice to the Royal Society of Scientists of Uppsala on 06 May 1927

This work was supported by the National Science Foundation under Grant No. DMS-1944862.

1

2 The Translation

Part 1

1We consider a general equation of nth degree:

x
n + c1x
n−1 + · · · + cn = 0 (1)

with roots x1, . . . , xn. We then apply a Tschirnhaus transformation, which has the general form

y = a0 + a1x + · · · + an−1x
n−1. (2)

This will transform (1) into an equation

yn + C1yn−1 + · · · + Cn = 0, (3)

where the coeﬃcients Ci are all homogeneous functions of degree i in the variables aν and include all such
functions of weight up to i in the coeﬃcents ci. Tschirnhaus hoped to use this type of transformation to
convert equation (1) to the binomial form in such a way that the determination of parameters aν should
require the solution of equations of degree at most n − 1. As is well known, this is not the case, even though
there have many attempts for the degree 5; this will never be the case, just like for [the problem of] trisecting
an angle. However, the situation is completely diﬀerent if the problem is formulated in the following way: Is
it possible to satisfy the conditions

Ci(a0, a1, . . . , an−1) = 0, i = 1, . . . , m (4)

in such a way that determining the parameters aν only requires equations of degree up to m, when n is
suﬃciently large? As a result of the following treatment for the case m = 4, it should not appear doubtful
that question should also be decided in the aﬃrmative for larger m. However, the general problem of
determining the lower bound on n associated to each m appears to be very complex.

Section 2

Observe that
 C1(a0, . . . , an−1) = na0 + · · · .

If C1 = 0, then a0 is expressed linearly in the other parameters. The coeﬃcients Ci, (i = 2, . . . , n − 1) are
then homogeneous functions of degree i in the parameters a1, . . . , an−1. In order to [ﬁnd a point that will]
satisfy a single condition Cx = 0, (x > 1)

it is evident that it is only necessary to ﬁnd an intersection of the hypersurface Cx = 0 with an arbitrary
straight line to solve an equation of degree x. If all the roots of (1) are real, then you cannot get a real
solution for x = 2 because the hypersurface
 n∑

i=1 y2
i = C2 = 0 (5)

has only the trivial 0. In contrast, there are always real points on the surface C3 = 0. Indeed, as you can
easily see, the same is the case for all surfaces Cx = 0 (x > 2) if x is an even number.

1Translator’s Note: This is a translation of the original mathematics. In particular, errors in the text have not been ﬁxed.
The errors in question come from considering intersections in aﬃne spaces instead of in projective spaces. Throughout this
translation, there are additional footnotes with the identiﬁer “Translator’s Footnote:.” These footnotes refer to remarks in
Section 3 in which the translator provides additional mathematical commentary.

2

If one has n ≥ 5, then one obtains the solution of (4) for m = 3 by the well-known Bring-Jerrard
transformation, which is illustrated geometrically by F. Klein 2 in the following way.3 First, a point P is
obtained on the surface C2 = 0, which, as noted above, can be done using a square root. If n > 5, we
then consider a three-dimensional space R3 which is tangent [to C2 = 0] at P , which then has a hypersuface
of degree 2 in common with C2 = 0. A second square root is now required in order to select one of the
two generators of this surface going through P . Determining an intersection of one of these generators with
F3 = 0 requires the solution of a degree 3 equation. Although only one pair of imaginary roots need to occur
in the real equations C1 = C2 = C3 = 0, at least two pairs of imaginary roots must exist to actually execute
this transformation. Otherwise, there is no real line at C2 = 0. This is due to the fact that if one converts

C2(a1, . . . , an−1) =
 n∑

i=1 y2
i

to a sum of n − 1 real squares, one gets the λ with the sign −, where 2λ denotes the number of imaginary
roots.

Section 3

Now, let n > 5. We assume that a point P that lies on both C2 = 0 and C3 = 0 has been determined by the
procedure given above. The associated coordinates are a(0)
1 , . . . , a(0)
n−1. We write

αi − α
(0)
i = βi, i = 1, . . . , n − 2

and reconstruct C2 and C3 in terms of β1, . . . , βn−2. 4 In this manner, by summing the terms with same
total degree in the βi, we get:
 C2 = φ1 + φ2 (6)

C3 = ψ1 + ψ2 + ψ3

We want to solve the present problem in such a way that we determine a straight line going through P
that lies on both the surfaces C2 = 0 and C3 = 0. If this is successful, then the further condition C4 = 0 only
requires the solution of an equation of the fourth degree. We denote the space with homogeneous coordinates
a1, . . . , an−1 as a Rn−2, in accordance with the number that is its dimension.

The ﬁrst conditions to be introduced are
 φ1 = ψ1 = 0. (7)

The space Rn−2 is then reduced to a Rn−4.5 If we consider the straight lines through P as elements of the
space, the point space Rn−4 has only n − 5 dimensions. From this perspective, we refer to it as Ln−5 and
consider the subvarieties φ2 = 0, ψ2 = 0, and ψ3 = 0 inside it. If one takes any plane in this line space Ln−5,
then φ2 = 0 and ψ2 = 0 have four elements in common - that is, four straight line generators. If n > 7, then
a common straight line of φ2 = 0 and ψ2 = 0 can be determined by solving a fourth degree equation. We
denote such a straight line by ℓ1.

If we can complete the task in such a way that we get a plane tangent to φ2 = 0 and ψ2 = 0, then this
result will be solved, as this plane intersects ψ3 = 0 in three straight lines, so that everything else comes down
to the solution of a degree three equation. The equations of the hyperplanes, which meet the subvarieties
φ2 = 0 and ψ2 = 0 along the straight line ℓ1 are given by

φ
(1)
1 = 0, ψ(1)
1 = 0. (8)

2We refer to the in-depth treatment of F. Klein, Lectures on the Icosahedron and the Solution of the Equation of Fifth Degree,
Leipzig, 1884.
3Translator’s footnote: See Remark 1 for the translator’s summary of this argument.
4One can assume that a
(0)
n−1 ̸= 0, after possibly changing the indices, and then write an−1 = 1
5Translator’s footnote: See Remark 2 for the translator’s summary of this argument.

3

We assume the relations (8) are satisﬁed. The Rn−4 discussed above then reduces to an Rn−6. If we restrict
to this Pn−6, then elements of φ2 = 0 and ψ2 = 0 appear as planes through ℓ1. However, there are exceptions
for when n = 7, as Rn−6 coincides with ℓ1, and for when n = 8, as φ2 = 0 and ψ2 = 0 are reduced to the
double-counted straight line ℓ1. We now replace the point space Rn−6 with a space whose elements are the
planes that contain the line ℓ1. This plane space obviously has dimension n − 8 and is denoted by En−8. We
now have the intersection of the quadratic [algebraic] manifolds φ2 = 0 and ψ2 = 0 in Rn−6 in the plane
space En−8. If n ≥ 10, one concludes that only a fourth degree equation has to be solved to determine a
common plane of φ2 = 0 and ψ2 = 0 in En−8. Therefore, we have the theorem:

If n ≥ 10, the general equation (1) can be reduced to the form

yn + C5yn−5 + · · · + Cn = 0 (9)

by a transformation (2) in such a way that determining the parameters ai requires only the solution of a
ﬁnitely many quartic, cubic, and quadratic irrationalities.

Although an equation of the form (9) can be achieved with only two pairs of imaginary roots, at least three
pairs of imaginary roots of (1) must exist for this transformation to be completed using only real numbers.
It is only under this condition that the hypersurface C2 = 0 contains real planes. However, if one wishes for
not only necessary, but also suﬃcient conditions here, this does seem to be possible without fairly in-depth
discussions.

Section 4

The case n = 9 was examined by D. Hilbert in a recently published work.6 It is ﬁrst demonstrated how one
can determine a three-dimensional space R3 which is completely contained in the hypersurface C2 = 0 and
then one considers the degree three surface F3 in this R3 which is cut out by the hypersurface C3 = 0. As is
known, this surface F3 only depends on four fundamental parameters. This is also particularly evident when
one transforms only the left term of the equation to a sum of ﬁve cubes, for which it is necessary to solve a
ﬁfth degree equation. Hilbert now puts the general equation of ninth degree in the form

y9 + C5y4 + C6y3 + C7y2 + C8y + C9 = 0 (10)

by ﬁrst determining one of the 27 straight lines on the surface F3 and then intersecting one of these straight
lines with the hypersurface C4 = 0. Both the equation (10), where one can easily set C9 = 1, as well as the
equation of degree 27 are functions of only four parameters. The result of this is that the solution of the
general equation of ninth degree only requires algebraic functions of four arguments in such a way that “one
can get by with functions of one argument, sums, and two special functions of four arguments”.

It can be shown that, if the general equation of ninth degree is reduced to the form (10), then there is no
need to solve an equation of degree higher than ﬁve, so that one of the special functions of four arguments
above is unnecessary. At the end, we generalize our task set at (4) by using auxiliary equations larger than
m, but with the restriction that each degree will still always be < n.

As in the previous case, we determine a point P on both C2 = 0 and C3 = 0 and still suppose the
conditions (8) hold. Since n = 9 here, the left terms of the subcone φ2 = 0 and ψ2 = 0 can be written in ﬁve
homogeneous coordinates, such as z1, z2, z3, z4, z5. We now look for the self-conjugate pentahedron common
to both φ2 and ψ2, which corresponds to solving a ﬁfth degree equation.7 If this pentahedron is assumed to
be a coordinate pentahedron, we have expressions for φ2 and ψ2 of the form:

φ2 = a1z2
1 + a2z2
2 + a3z2
3 + a4z2
4 + a5z2
5 (11)

ψ2 = b1z2
1 + b2z2
2 + b3z2
3 + b4z2
4 + b5z2
5.

6 ¨Uber die Gleichungen neuten Grades, Math. Ann. 97, S. 243 (1926)
7Translator’s footnote: See Remark 3 for more exposition.
 4

One can now eliminate any of the ﬁve variables from φ2 = 0 and ψ2 = 0 and thus obtain ﬁve relations,
one of which we write in the form c1z2
1 + c2z2
2 + c3z2
3 + c4z2
4 = 0. (12)

We take (12) as the equation of a degree two hypersurface and try to determine the corresponding straight
line generators, which only requires taking square roots. The straight lines in this generating set are assigned
to the values of a a parameter λ and, likewise, the points of a speciﬁed generator are assigned to the values
of another parameter t1 and the their coordinates z1, z2, z3, z4 can be expressed linearly in both λ and t.
According to (11), we get the relation for z5:

z2
5 = a2(λ)t2 + b2(λ)t + c2(λ). (13)

Since the elements of (11) are straight lines through P , it can be seen that a generator of (12) corresponds
to a two-dimensional cone whose apex is P . Since this cone must have six generators in common with the
hypersurface ψ3 = 0, it follows that one need not use auxiliary equations of degree more than six when
reducing the general equation of ninth degree to the form (10).

Section 5

This matter can be simpliﬁed by looking for a value of λ such that the two-dimensional cone splits into two
planes. We need only solve the degree four equation

[b2(λ)]2 − 4a2(λ)c2(λ) = 0. (14)

The generating system of (12) has four other conjugate pairs of planes, so that the total number of planes
common to the subcones φ2 = 0 and ψ2 = 0 is 16. According to the ﬁve diﬀerent relations in four variables
of the form (12), each of these planes can be paired with ﬁve others. Two planes that can be paired together
intersect each other in a straight line. If not, they only intersect at P .

The theory of the intersection of the two cones φ2 = 0 and ψ2 = 0 is indeed well known.8 They system
of equations (11) is often used to study properties of a degree four surface with a double conic section. The
16 common planes of the two subcones correspond to the 16 straight lines lying on such a surface.

We have now demonstrated that the general equation of ninth degree can also be converted to the form
(9) without having to presuppose the solution of auxiliary equations which each depend on more than one
parameter. Among the auxiliary equations, however, there is one of ﬁfth-degree, so we cannot get by with
square roots and cube roots, as we can for n > 9. However, it seems to be diﬃcult to prove strictly that the
latter is not possible at all for n = 9.

8Translator’s footnote: See Remark 4 for the translator’s summary of this argument.

5

3 Translator’s Notes

Remark 1. (Main Argument of Section 2)
Let An be the aﬃne space of Tschirnhaus transformations and Pn−1 its projectivization. V(C1) is a hyperplane
and thus V(C1) ∼= Pn−2. A rational point P of V(C1) ∩ V(C2) can be determined over a quadratic extension
of the base ﬁeld. Then, the tangent hyperplane T at P can be computed rationally and will have dimension
at least 4 in V(C1) = Pn−2 if n > 6. Hence V(C1) ∩ V(C2) ∩ T is a quadric that is singular at P in
V(C1) ∩ T ∼= Pn−3. Consequently, a line in this cone can be determined by solving a quadratic polynomial
and it suﬃces to intersect this line with F3 = 0.

Remark 2. (Main Argument of Section 3)
To re-state Wiman’s approach, this Pn−4 is obtained by projectivizing and then considering V(C1) ∩ V(φ1) ∩
V(ψ1) inside Pn−1. By shifting P to the origin (e.g. [0 : · · · : 0 : 1]), Wiman then uses a classical corre-
spondence to consider the pencil of lines through P and identiﬁes it as Ln−5 ∼= Pn−5. Note that φ2, ψ2, and
ψ3 induce hypersurfaces of the same degree in Ln−5. If n ≥ 7, a point Q of V(φ2) ∩ V(ψ2) ⊆ Ln−5 can be
determined by solving a quartic equation. Moreover, by construction, the line ℓ1 determined by P and Q lies
in V(C1) ∩ V(C2) in the ambient space.

Now, consider the tangent hyperplanes of V(φ2), V(ψ2) ⊆ Pn−4 deﬁned by the polynomials φ
(1)
1 and
ψ(1)
1 . Consider the Pn−6 given by V(C1) ∩ V(φ1) ∩ V(ψ1) ∩ V(φ
(1)
1 ) ∩ V(ψ(1)
1 ). Every point not on ℓ1 in
En−8 = V(φ2)∩V(ψ2) ⊆ Pn−6 determines a plane on V(φ2)∩V(ψ2) in the ambient space; this is possible when
n ≥ 9. Determining such a point Q′ in En−8 determines a line ℓ2 ⊆ V(φ2)∩V(ψ2) ⊆ Ln−5 and thus a point Q′

of ℓ2 ∩ V(ψ3) ⊆ Ln−5 can be determined by solving a cubic equation. However, the line determined by P and
Q′ lies inside V(C1) ∩ V(C2) ∩ V(C3) in the ambient space and thus a point of V(C1) ∩ V(C2) ∩ V(C3) ∩ V(C4)
can be determined by solving a quartic equation.

Remark 3. (Pencils of Quadrics)
The forms φ2 and ψ2 deﬁne a pencil of quadratic forms in the ﬁve variables z1, . . . , z5. The singular ﬁbers of
the pencil are given by the roots of the discriminant, which is a polynomial of degree 5. Hence, determining
a singular quadric in the pencil corresponds to solving a degree 5 polynomial. Wiman then again uses the
observation that a singular quadric is a cone.

Remark 4. (Degree 4 del Pezzo Surfaces)
Here Wiman is observing the fact that the intersection of two quadrics in P4 is a degree 4 del Pezzo surface.

6
