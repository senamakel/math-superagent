<!-- source: https://arxiv.org/pdf/2107.01006 | converted from PDF -->

arXiv:2107.01006v2  [math.HO]  6 Jul 2021
On the Problem of Resolvents

A Translation by Alexander J. Sutherland

July 8, 2021

1 Original Bibliographic Information

I thank Ignat Soroko for helpful comments on the bibliographic information.

1.1 Russian

• Author: Г. Н. Чеботарев

• Title: К Пpoблeмe Рeзoльвeнт

• Year: 1954

• Language: русский

• Publisher: Учeныe Записки Казанского Государствeнного Унивeрситeта им. В. И. Ульянова-
Лeнина

1.2 English

• Author: G.N. Chebotarev

• Title: On the Problem of Resolvents

• Year: 1954

• Language: Russian

• Publisher: Scientiﬁc Proceedings of the V.I. Ulyanov-Lenin Kazan State University

This work was supported by the National Science Foundation under Grant No. DMS-1944862.

1

2 The Translation

On the Problem of Resolvents

1 Consider an equation of nth degree

f (x) = x
n + a1x
n−1 + · · · + an = 0 (1)

whose coeﬃcients a1, . . . , an are indeterminates. Substituting

y = t0 + t1x + · · · + tn−2x
n−2 + x
n−1

into f (x) = 0 yields an nth degree equation

yn + C1yn−1 + C2yn−2 + · · · + Cn = 0 (2)

where the coeﬃcients C1, . . . , Cn depend rationally on a1, . . . , an and are polynomials in t0, . . . , tn−2 of re-
spective degrees 1, . . . , n.

Equation (2) is called an s-parameter resolvent of equation (1) if its coeﬃcients C1, . . . , Cn are rational
functions of s parameters v1, . . . , vs and the coeﬃcients t0, . . . , tn−2 of the Tschirnhaus transformation depend
rationally on a1, . . . , an and the roots of some auxiliary equations (secondary resolvents), which themselves
admit s-parameter resolvents.

It is easy to show that if one does not limit the degree of the secondary resolvents, the s-parameter
resolvent of equation (1) can be put in the particular form

yn + Cn−sys + Cn−s+1ys−1 + · · · + Cn−1y + 1 = 0. (3)

In fact, let
 g(z) = zn + B1zn−1 + · · · + Bn = 0

be an s-parameter resolvent of equation (1), i.e. B1, . . . , Bn are rational functions s of parameters v1, . . . , vs.

Take the new Tschirnhaus transformation

y = τ0 + τ1z + · · · + τn−2zn−2 + zn−1.

The coeﬃcients C1, . . . , Cn of the equation that y satisﬁes are polynomials of the corresponding degree in
the τ0, . . . , τn−2 and, moreover, depend rationally on the coeﬃcients B1, . . . , Bn and therefore on the param-
eters v1, . . . , vs. Setting C1, . . . , Cn−s−1 equal to zero and Cn equal to 1 and composing the results of these
equations (in which τ0, . . . , τn−2 are unknown), we obtain a chain of auxiliary equations whose coeﬃcients
depend on s parameters.

D. Hilbert (1) showed in his article ”On Equations of the Ninth Degree” that an equation of the ninth
degree admits a resolvent that depends on 4 parameters. His method of obtaining this resolvent is as follows.

The coeﬃcients t0, . . . , tn−2 of the Tschirnhaus transformation are considered as the coordinates of a point
in the space T taking values from the ﬁeld of rational functions in a1, . . . , an and its algebraic extensions.
The equations C1 = 0, C2 = 0, C3 = 0 and C4 = 0 determine hypersurfaces in the space T of degrees 1,
2, 3, and 4, respectively. Finding a 4-parameter resolvent of an equation of 9th degree reduces to ﬁnding
a common point of these hypersurfaces by solving a chain of algebraic equations that admit ≤ 4-parameter
resolvents. Substituting y = n√
Cnz makes the ﬁnal term a unit.

1Translator’s Note: This is a translation of the original mathematics. In particular, errors in the text have not been ﬁxed.
The errors in question come from considering intersections in aﬃne spaces instead of in projective spaces.

2

This problem is solved by Hilbert as follows. A three-dimensional hyperplane is found that entirely be-
longs to the hypersurfaces C1 = 0, C2 = 0. On it, the surface C3 = 0 cuts out a cubic surface, which, as you
know, always contains lines that lie entirely on it; to ﬁnd these lines, one has to solve an equation of the 27th
degree which depends only on four parameters, since the equation of the cubic surface allows a special tech-
nique based on the subtle properties of cubic quarternary forms (by summing up ﬁve cubes that are the roots
of one equation of ﬁfth-degree) which leads to a form that depends on 4 parameters. The intersection of the
line just found with the hypersurface C4 = 0 determines the desired point. Thus, to construct a 4-parameter
resolvent of an equation of the 9th degree, in addition to a series of equations of degree between 2 and 5,
it is necessary to solve an equation of the 27th degree, which is greater than the degree of the original equation.

In the work ”On the Application of Tschirnhaus Transformations to the Reduction of Algebraic Equations”
(2), A. Wiman show that to obtain an (n − 5)-parameter resolvent of an equation of degree n ≥ 10, it is
suﬃcient to solve several auxiliary one-parameter equations of degree no higher than 4. To do this, he moves
the origin to an intersection point of the hypersurfaces C1 = 0, C2 = 0, C3 = 0 and reduces the last two
equations to the form
 0 = C2 = φ2
0 = C3 = ψ2 + ψ3

where φ2 and ψ2 are quadratic homogeneous forms and ψ3 is a cubic homogeneous form, and using elegant
geometric considerations, searches for a two-dimensional plane that lies entirely in both the hypercones φ2 = 0
and ψ2 = 0. The intersection of this plane with the cubic cone ψ3 = 0 gives a straight line belonging to the
surfaces C1 = 0, C2 = 0, C3 = 0.

For the case n = 9, Wiman proves that in order to obtain a 4-parameter resolvent, it is suﬃcient to
only solve one auxiliary equation of 5th degree (which has a one-parameter resolvent) in addition to the the
equations of degrees 1-4. To do this, he performs a linear transformation (which is determined by solving
an equation of ﬁfth degree) which simultaneously diagonalizes the forms φ2 = 0 and ψ2 = 0 and deﬁnes a
one-parameter family of two-dimensional cones, all points of which belong to both cones φ2 = 0 and ψ2 = 0.
By solving an equation of fourth degree, we ﬁnd the value of the parameter at which the cone of the family
splits into a pair of planes.

Applying the method of Wiman, we can ﬁnd an (n − 6)-parameter resolvent of an equation of degree
n ≥ 77. In this article, an attempt is made to slightly modify this method, as a result of which, the (n − 6)-
parameter resolvent can be constructed for equations of degree n ≥ 21.

Following Wiman, we consider the space Tn−1 of the parameters t0, . . . , tn−2 and the hypersurfaces C1 =
0, C2 = 0, C3 = 0, C4 = 0, C5 = 0 in this space. We move the origin to a point common to the hypersurfaces
C1 = 0, C2 = 0, C3 = 0, which can be determined by solving auxiliary equations of the second and third
degree. Now, in the equations of the ﬁrst three surfaces, the free terms disappear and these equations can
be written as follows:
 0 = C1
0 = C2 = φ1 + φ2
0 = C3 = ψ1 + ψ2 + ψ3

where C1, φ1, ψ1 are linear forms of the parameters ti, ψ2, φ2 are quadratic [forms], and ψ3 is a cubic. The
equations φ1 = 0 and ψ1 = 0 determine the hyperplanes tangent to the hypersurfaces C2 = 0 and C3 = 0 at
the origin. The intersection of these hyperplanes with the hyperplane C1 = 0 determines the space Tn−4, in
which the equations of the hypersurfaces cut out by C2 = 0 and C3 = 0 will have the form

0 = C′
2 = φ
′
2
0 = C′
3 = ψ′
2 + ψ′
3.

We show that for n ≥ 19, there exists a two-dimensional plane belonging entirely to the hypersurfaces
C′
2 = 0 and C′
3 = 0 in the space Tn−4.
 3

Lemma 2.1. Two (3k − 1)-dimensional quadratic cones with a common vertex in 3k-dimensional space share
a whole k-dimensional plane passing through the vertex of the cones.

Proof. We proceed by induction. Find straight-line generators common to both cones (for this, it is enough
to intersect both cones with any two-dimensional plane that does not pass through their vertex, ﬁnd the
intersection point of the two quadrics cut by the cones on the plane - which requires solving an equation of
fourth degree - and connect the found point to the vertex of the cones). Take a plane of dimension 3k − 1
that does not pass through vertex of the cones. On this hyperplane, our cones will cut out two hypersurfaces
of degree 2, the common point of which is rationally deﬁned as the intersection of the hyperplane and the
previously found common [straight-line] generator of the cones.

The intersection of the [original] hyperplane and the two [tangent] hyperplanes touching these hypersur-
faces at their common point deﬁnes a space of 3k − 3 dimensions, in which out cones cut out a pair of cones
of 3k − 4 dimensions with a common vertex, which contains a generic k − 1 dimensional linear space by the
inductive hypothesis. The desired k-dimensional subspace common to both cones is deﬁned as the space
passing through the (k − 1)-dimensional space and the vertex of the cones.

Lemma 2.2. A cubic four-dimensional cone in ﬁve-dimensional space contains a two-dimensional plane
passing through the top of the cone which lies entirely in the cone.

Proof. Intersect our cone with a four-dimensional plane that does not pass through its top. The cone will
cut out a three-dimensional cubic hypersurface on it. We ﬁnd a point on this surface (for which it is enough
to solve one equation of the third degree) and construct a three-dimensional hyperplane that is tangent to
the surface at this point. If, after moving the point to the origin, the equation of the hypersurface has the
form
 φ1 + φ2 + φ3 = 0,

then the equation of the tangent hyperplane will be

φ1 = 0.

Consider the intersection of our surface with the given tangent hyperplane. Obviously, the equation of this
intersection will have the form
 φ
′
2 + φ
′
3 = 0

where φ
′
2 and φ
′
3 are forms of second and third degree, respectively, in three variables. We consider the
quadratic and cubic cones
 φ
′
2 = 0 and φ
′
3 = 0

with a common vertex in three-dimensional space. These cones have a common straight line generator and it
suﬃces to solve an equation of the sixth degree to ﬁnd it (determine the intersection point of the quadric and
cubic cut out by the cones on any two-dimensional plane not passing through their vertex and connect it to
the vertex of the cones). The two-dimensional plane which passes through the [original] vertex and through
the straight line just found lies entirely in the original cubic cone.

Theorem 2.3. The general algebraic equation of degree n ≥ 21 admits an (n − 6)-parameter resolvent.

Proof. As above, consider the hypersurfaces

C1 = 0, C2 = 0, C3 = 0, C4 = 0, C5 = 0

in the space Tn−1. We move the origin to a common point of the hypersurfaces C1 = 0, C2 = 0, C3 = 0.
We construct tangent hyperplanes to the hypersurfaces C2 = 0 and C3 = 0 at the origin and consider the

4

space Tn−4, which is the intersection of these hyperplanes with the hyperplane C1 = 0. In Tn−4, our surfaces
C′
2 = 0 and C′
3 = 0 are deﬁned by equations of the form

0 = C′
2 = φ2,
0 = C′
3 = ψ2 + ψ3.

By virtue of Lemma 1 and as n − 4 ≥ 15, the two cones

φ2 = 0, ψ2 = 0

have a common 5-dimensional linear subspace. According to Lemma 2, the cubic cone ψ′
3 = 0 in this subspace
contains a two-dimensional plane and according to the above, we do not need to solve any equations above
the sixth degree to ﬁnd one.

The hypersurfaces
 C4 = 0 and C5 = 0

cut out curves of the 4th and 5th degree are cut out on this plane, the intersection point of which can be
found by solving an equation of the 20th degree, which, according to Wiman, has a resolvent that depends
on no more than 15 parameters. However, n − 6 ≥ 15, which proves the theorem.

This technique allows us to state the existence of (n − 7)-parameter resolvents of a general equation of
degree n ≥ 121.

Literature

(1) D. Hilbert. ¨Uber die Gleichung neunten Grades. Ges. Abh., Bd. II, S. 393.
(2) A. Wiman. ¨Uber die Anwendung der Tschirnhausentransformationen auf die Reduktion algebraischer
Gleichungen. Nova Acta Regiae Societatis Scientiarum Upsaliensis, volumen extra ordinem 1927.

Department of Algebra Received January 19, 1953.

5
