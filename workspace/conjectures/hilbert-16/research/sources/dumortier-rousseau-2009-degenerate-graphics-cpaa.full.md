<!-- source: http://www.dms.umontreal.ca/~rousseac/Dumortier_Rousseau.pdf | converted from PDF -->

Study of the cyclicity of some degenerate graphics
inside quadratic systems ∗†

F. Dumortier, Hasselt University
C. Rousseau, DMS and CRM, Universit´e de Montr´eal

November 30, 2007

Abstract

In this paper we make essential steps in proving the ﬁnite cyclicity of degenerate
graphics in quadratic systems, having a line of singular points in the ﬁnite plane. In
particular we consider the graphics (DF1a), (DF2a) of the program of [DRR] to prove the
ﬁniteness part of Hilbert’s 16th problem for quadratic vector ﬁelds. We make a complete
treatment except for one very speciﬁc problem that we clearly identify.

1 Introduction

Together with Robert Roussarie, we initiated the DRR program in 1994 (see [DRR]) to prove
the ﬁniteness part of Hilbert’s 16th problem for quadratic vector ﬁelds. The program reduces
the global problem of showing the existence of a uniform upper bound for the number of
limit cycles of a quadratic vector ﬁeld to 121 local ﬁniteness problems. Each of these local
problems consists in showing the ﬁnite cyclicity of a graphic surrounding the origin inside
the family ˙x = λx − µy + a1x2 + a2xy + a3y2

˙y = µx + λy + b1x2 + b2xy + b3y2, (1.1)

with Λ = (λ, µ) ∈ S1 and A = (a1, a2, a3, b1, b2, b3) ∈ S5. A graphic Γ surrounding the origin
for a given system (1.1) corresponding to parameter values (Λ, A) has ﬁnite cyclicity inside the
family (1.1) if there exists an integer n, a tubular neighborhood U of Γ and a neighborhood
V of (Λ, A) in parameter space, such that for any (Λ′, A′) ∈ V the corresponding vector ﬁeld
of (1.1) has at most n limit cycles in U . The paper [R] lists the graphics whose ﬁnite cyclicity
is proved.
The original list of 121 graphics of the DRR program contains 13 degenerate graphics
with a line of singular points. These graphics are considered the most diﬃcult and the
most interesting ones. Indeed it was recently shown in [DR2] and [DPR] that bifurcations of
degenerate graphics can create more limit cycles than usually expected. Also Artes, Llibre
and Schlomiuk identify in [ALS] an interesting quadratic system with a line of singular point,
which they conjecture to be an organizing center of the bifurcation diagram of quadratic

∗This work is supported by NSERC in Canada.
†AMS classiﬁcation numbers: 34C07, 34C26, 37G99

1

2 F. Dumortier & C. Rousseau

systems. Partial results on the cyclicity of the graphic (DI2a) are ready to be presented as a
preprint ([ADL]).
In this paper we wish to start a systematic study of the cyclicity of the degenerate graphics
appearing in the DRR program, attempting at least to prove ﬁnite cyclicity or giving a rather
rough upper bound. In this attempt we can rely on recent results and methods in treating
the cyclicity of degenerate graphics. The graphics of the DRR program all have the following
features: they have one line of singular points, all of which are normally hyperbolic, except for
one, called a contact point. In treating such contact points, a technique has been particularly
powerful. It consists in desingularizing the family near the contact point by the method of the
blow-up of the family. This allows to identify the regions in parameter space where limit cycles
are likely to appear. In these regions the displacement map is studied. Under the condition
that the slow dynamics is non- zero, its derivative is shown to be C ∞ contact equivalent
to a development having the slow divergence integral as leading term. The properties of
the development are suﬃciently regular to permit a nice control by the leading term. As a
consequence, among other results, ﬁnite cyclicity is obtained as soon as the slow divergence
integral does not vanish identically and in that case the cyclicity is determined by the slow
divergence integral. Reﬁnements have been studied in [DD3] for the case when singularities
like saddle points or saddle-nodes appear in the slow dynamics. These are used in the generic
case. In the center case, we need to make an ad hoc adaptation. We also have to deal with a
slow divergence integral that is identically zero when the center conditions are met, requiring
extensions of the existing theoretical results. In the presence of a desingularized contact point
we are able to deal with this problem by blowing up the parameters in the neighborhood of
the center conditions.
It is known for a long time that the space of quadratic systems modulo aﬃne conjugacy
and scaling of time is essentially of dimension 5 (see for instance [RS]). It is hence natural
to reduce the family (1.1) to a 5-parameter family which is well suited to study the ﬁnite
cyclicity of a given degenerate graphic. Such a 5-parameter “normal form” is not unique. The
surprise is that there is no adequate normal form allowing to perform the program described
above for all parameter values. Indeed the blow-up of the family requires at the contact point
a weighted blow-up. Depending on the monomials we choose to keep in the normal form they
may play an important role in the slow divergence integral or in the family rescaling of the
blow-up family. There does not seem to exist a normal form in which one can desingularize
the contact point when the slow dynamics has a zero at the contact point. This seems to be
a hard problem that we can not yet treat for the moment. Due to this diﬃculty our study
is incomplete. The lack of knowlegde is however limited to a small and precise region in
parameter space.
In this paper we study the graphics (DF1a), (DF2a) of the DRR program (see Figure 1
below). The graphic (DF2a) is the center version of the generic graphic (DF1a). We expect
that our method can be used for the other degenerate graphics of the DRR program although
we do not expect that this will be a trivial exercise, especially for (DH5). In all these graphics
the main diﬃculty will not be to treat the center graphics, but to overcome the fact that
the family cannot be desingularized. For this reason we have given normal forms adequate
to study the ﬁnite cyclicity of all the degenerate graphics of the DRR program. We had a
second surprise when looking for a normal form for the unfolding of a quadratic system with
a graphic of type (DH5): there exists no analytic 5-parameter normal form and a natural
analytic normal form needs 7 parameters! The explanation is the following: usually one

Singular perturbations 3

reduces the quadratic family by means of the action of the aﬃne group and time scaling.
This works when the orbits are transversal to the stratum being studied. Here the stratum
is invariant under a 2-dimensional subgroup of the aﬃne group.

2 Normal forms for families unfolding degenerate graphics

In this section and in view of treating all degenerate quadratic graphics, we derive good
normal forms for quadratic families unfolding the degenerate graphics of [DRR]. There are
13 such graphics but only three normal forms are necessary to treat them all; we give all three.
Diﬀerent normal forms for the families are possible: we choose some where each parameter
has its deﬁnite role in the perturbed system.

2.1 Quadratic families unfolding the graphics with a line of singular points
in the ﬁnite plane

These are the graphics (DF1a), (DF1b), (DF2a), (DF2b), (DH1), (DH2).

Proposition 2.1 A quadratic system with a line of singular points in the ﬁnite plane, all of
which except one are normally hyperbolic, and a focus (strong or weak) or center can always
be brought to the form ˙x = y + b0xy − y2

˙y = xy, (2.1)

with b0 ∈ (−2, 2). The general quadratic perturbation of (2.1) can be brought by an aﬃne
change of coordinates and time scaling, depending analytically on the parameters, to the form

˙x = y + bxy − y2 + µ1 + µ2x + µ3x2

˙y = xy + µ4, (2.2)

where b = b0 + µ0 is a variable parameter inside (−2, 2). Hence the ﬁve-parameter quadratic
unfolding of (2.1) is parameterized by (µ0, . . . , µ4). When b0 ̸= 0,using a scaling (x, t) ↦→
(−x, −t) we can consider b > 0.

Proof If a quadratic system has a line of singular points we can always suppose that it
is the line y = 0. All points of the line are normally hyperbolic except one which we can
suppose to be the origin. We can suppose that the focus or center is located at (0, 1). So we
can always suppose that the system has the form (2.1) with b0 ∈ (−2, 2), the later condition
guaranteeing that (0, 1) is a focus or center. The general quadratic perturbation is of the
form ˙x = y + b0xy − y2 + ∑0≤i+j≤2 aijxiyj

˙y = xy + ∑
0≤i+j≤2 bijxiyj. (2.3)

We consider a change of coordinates

(x, y) = (X + δ1Y + δ3, δ2X + Y + δ4) (2.4)

for the family, which reduces to the identity for (2.1). Such a change of coordinates brings
(2.3) to the form ˙X = Y + b0XY − Y 2 + ∑
0≤i+j≤2 AijX iY j
˙Y = XY + ∑0≤i+j≤2 BijX iY j. (2.5)

4 F. Dumortier & C. Rousseau

We consider the map (δ1, δ2, δ3, δ4, aij, bij) ↦→ (B10, B01, B20, B02). The diﬀerential w.r.t.
(δ1, δ2, δ3, δ4) at aij = bij = 0, namely





 0 0 0 1
0 −1 1 0
0 1 0 0
1 1 0 0
 



 , (2.6)

is invertible, yielding that we can solve the equations B10 = B01 = B20 = B02 = 0 by the
implicit function theorem.
Using scalings in (X, Y, t) allows to take A01 = A02 = B11 = 0, while we can write
b0 + A11 = b. ✷

2.2 Quadratic families unfolding the graphics with a line of singular points
at inﬁnity

These are the graphics (DI1a), (DI1b), (DI2a), (DI2b), (DH3), (DH4).

Proposition 2.2 A quadratic system with a line of singular points at inﬁnity, all of which
except one are normally hyperbolic, a ﬁnite invariant line and a focus (strong or weak) or
center can always be brought to the form

˙x = c0x − y + 1 + x2

˙y = xy, (2.7)

with c0 ∈ (−2, 2). The general quadratic perturbation of (2.7) can be brought by an aﬃne
change of coordinates and time scaling, depending analytically on the parameters, to the form

˙x = cx − y + 1 + (1 + µ2)x2 + µ1xy + µ0y2

˙y = xy − µ3x2, (2.8)

where c = c0 + µ4 is a variable parameter inside (−2, 2), yielding the ﬁve-parameter unfolding
of (2.7) being parameterized by (µ0, . . . , µ4). When c0 ̸= 0, using a scaling (x, t) ↦→ (−x, −t)
we can consider c > 0.

Proof We can always suppose that the invariant line is the line y = 0. The line at inﬁnity
is a line of singular points, so is the equator of the Poincar´e-sphere, compactifying the ﬁnite
plane. All points of the equator are normally hyperbolic except for two. By a change of
coordinate X = x + ay we can always suppose that the non normally hyperbolic points are
located on the y-axis. We can suppose that the focus or center is located at (0, 1). So we
can always suppose that the system has the form (2.7) with c0 ∈ (−2, 2), the last condition
guaranteeing that (0, 1) is a focus or center. The general quadratic perturbation is of the
form ˙x = c0x − y + 1 + x2 + ∑0≤i+j≤2 aijxiyj

˙y = xy + ∑
0≤i+j≤2 bijxiyj. (2.9)

We consider a change of coordinates

(x, y) = (X + δ1Y + δ3, δ2X + Y + δ4) (2.10)

Singular perturbations 5

for the family, which reduces to the identity for (2.7). Such a change of coordinates brings
(2.9) to the form
 ˙X = c0X − Y + 1 + X 2 + ∑
0≤i+j≤2 AijX iY j
˙Y = XY + ∑
0≤i+j≤2 BijX iY j. (2.11)

We consider the map (δ1, δ2, δ3, δ4, aij, bij) ↦→ (B00, B10, B01, B02). The diﬀerential w.r.t.
(δ1, δ2, δ3, δ4) at aij = bij = 0, given by





 0 −1 0 0
0 −c 0 1
0 1 1 0
1 0 0 0
 



 (2.12)

is invertible, yielding that we can solve the equations B00 = B10 = B01 = B02 = 0 by the
implicit function theorem.
Using scalings in (X, Y, t) allows to take A01 = A00 = B11 = 0, while we can write
c0 + A10 = c. ✷

2.3 Quadratic family unfolding the graphic with two lines of singular
points

This is the graphic (DH5) which occurs in the system

˙x = xy
˙y = −y + y2. (2.13)

In the two previous cases the quadratic family could be reduced to a 5-parameter family of
vector ﬁelds through the action of the aﬃne group and scaling of time. In this case it is not
possible through a change of coordinates, depending analytically on the parameter, to reduce
the full quadratic unfolding of (2.13) to a 5-parameter family. Indeed (2.13) is invariant
under any change of coordinate (X, Y ) = (αx + β(y − 1), y). Using a change of coordinate
(x, y) = (X + δ3, δ2X + Y + δ4) and scalings in Y and t we can reduce the full quadratic
unfolding to the 7-parameter family

˙x = xy(1 + µ4) + µ0 + µ1x + µ2x2 + µ3y2

˙y = −y + y2 − µ6x2 + (µ2 − µ5)xy. (2.14)

Although we have more parameters than really necessary, the unfolding (2.14) has the
advantage that the slow motion on the line y = 0 is given by ˙x = µ0 + µ1x + µ2x2, while the
slow motion on the equator, using coordinates (v, w) = (x/y, 1/y) is given by ˙v = µ3 + µ4v +
µ5v2 + µ6v3, both being simple polynomial expressions.

3 Statement of results on the cyclicity of DF1a and DF2a

We will study the degenerate graphic DF1a and DF2a as they occur in system (2.1) for
respectively b0 ∈ (0, 2) and b0 = 0 (see Figure 1). Such a graphic consists of a fast orbit,
that we denote by γb0
x0, and a critical curve, included in the x-axis, that we denote by C b0
x0 =

6 F. Dumortier & C. Rousseau

DF1a DF2a

ba

Figure 1: Degenerate graphics under consideration.

[fb0(x0), x0]; x0 > 0 is the x-coordinate of the point p0 = (x0, 0) representing the α-limit of
the fast orbit and p1 = (fb0(x0), 0) represents the ω-limit of the fast orbit. Let Γb0
x0 = γb0
x0 ∪C b0
x0
denote the degenerate graphic.
We will study the cyclicity of Γb0
x0, with x0 ∈ (0, ∞), We therefore consider system (2.2),
with (ε1, ε2, ε3, ε4) ∼ (0, 0, 0, 0), for some b ∈ [0, 2).
From the subsequent calculations it will reveal to be interesting to write (2.2) as
{ ˙x = y + bxy − y2 + ε2(E0 + E1x + E2x2)
˙y = xy + ε3D (3.1)

with ε ≥ 0 small, b − b0 small and keeping (E0, E1, E2, D) in the boundary C1 of a cylinder,
more precisely inside C1 = B0 ∪ B1 ∪ B−1

with
 B0 = {E2
0 + E2
1 + E2
2 = 1, D ∈ [−1, 1]} and
Bi = {E2
0 + E2
1 + E2
2 ≤ 1, D = i} (3.2)

for i = ±1.
Studying the systems (3.1), for ε > 0, subject to (D, E0, E1, E2) ∈ C1, requires using
a number of recent results on singular perturbations, as well as extensions of these results.
Unfortunately, for the moment, we are not able to deal with systems (3.1) that are close to
P∗ ∈ B0 ⊂ C1 with P∗ = (D, E0, E1, E2) = (0, 0, 0, 1).

In making precise statements of the results that we have obtained till now, we introduce the
balls Bδ(P∗) = {(D, E0, E1, E2) ∈ C1 | d((D, E0, E1, E2), P∗) < δ},

with δ > 0.
We can write the unknown systems with (D, E0, E1, E2) ∈ Bδ(P∗), for δ > 0 suﬃciently
small, as: { ˙x = y + bxy − y2 + ε2(e0 + e1x + x2)
˙y = xy + ε3D, (3.3)

with (e0, e1, D) ∼ (0, 0, 0).
As we will see in the further elaboration, it does not seem possible to “desingularize” at

Singular perturbations 7

(e0, e1, D) = (0, 0, 0), creating theoretical problems that we can not overcome for the moment.
A similar problem has also been encountered for the equations (5) in [ADL].
Except for that problem we are able to make a fairly complete study for the degenerate
graphics (DF1a) and (DF2a). The results that we obtain are presented in Theorem 3.1.

Theorem 3.1 Consider a system ( 3.1) and a set of degenerate graphics Γb0
x0, with b0 ∈ [0, 2)
and x0 ∈ K, with K ⊂ (0, ∞) compact. Then the following statements hold, for arbitrary
δ > 0:

(i) If b0 ∈ (0, 2), there exists ε0 > 0, η0 > 0 and ρ > 0 such that system ( 3.1) with
ε ∈ [0, ε0], b ∈ (b0 − η0, b0 + η0) and (D, E0, E1, E2) ∈ C1\Bδ(P∗) has at most three
limit cycles (multiplicity taken into account), lying each within Hausdorﬀ distance ρ of
a corresponding graphic Γb0
x0, with x0 ∈ K. If moreover we keep E1 ≥ 0, then, under
the same conditions on ε, b, (D, E0, E1, E2), system ( 3.1) has at most one limit cycle,
which is hyperbolic and attracting when it exists.

(ii) If b0 = 0 there exists ε > 0, η0 > 0 and ρ > 0 such that system ( 3.1) with ε ∈ [0, ε0], b ∈
[−η0, η0] and (D, E0, E1, E2) ∈ C1\Bδ(P∗) has at most 5 limit cycles (multiplicity taken
into account) each within Hausdorﬀ distance ρ of a corresponding graphic Γ0
x0 with
x0 ∈ K. If moreover we keep bE1 ≥ 0, then, under the same conditions on ε, b,
(D, E0, E1, E2), system ( 3.1) has at most one limit cycle. When it exists it is hyperbolic.
It is attracting (resp. repelling) for E1 > 0 or E1 = 0, b > 0 (resp. E1 < 0 or E1 = 0,
b < 0)

(iii) Let Bδ1((0, E0, 0, E2)) be a δ1-neighbourhood of the circle {D = E1 = 0} inside C1. If
b0 = 0 and δ1 > 0 is arbitrary, then there exists ε0 > 0 and η0 > 0 such that system ( 3.1)
with ε ∈ [0, ε0], b ∈ [−η0, η0] and (D, E0, E1, E2) ∈ C1\(Bδ(P∗) ∪ Bδ1((0, E0, 0, E2))) has
at most 1 limit cycle and this limit cycle is hyperbolic; it is repelling for E1 < 0 and
attracting for E1 > 0.

Remark 3.2 We can state rather precise cyclicity results in (i) and (iii); (i) treats the case
b0 ∈ (0, 2) and (D, E0, E1, E2) ̸= (0, 0, 0, 1) while (iii) treats the case b0 = 0 and E1 ̸= 0. In
(ii) we only obtain a rather rough cyclicity result when b0 = 0 and E1 = 0, with (D, E0, E2) ̸=
(0, 0, 1). Using (iii), this statement has hence only to be proven for b ∼ 0 and (D, E0, E1, E2)
with (D, E1) ∼ (0, 0). As already mentioned we do not yet see how to treat the cyclicity of
systems (3.1) with (D, E0, E1, E2) = (0, 0, 0, 1).

4 Proof of Theorem 3.1

4.1 Blow up at the origin

To prove Theorem 3.1 we will blow up the origin by means of the family blow up

(x, y, ε) = (r¯x, r2 ¯y, r¯ε), (4.1)

with r ≥ 0 small and keeping (¯x, ¯y, ¯ε) inside S+
2 with S+
2 = {¯x2 + ¯y2 + ¯ε2 = 1, ¯ε ≥ 0}.

8 F. Dumortier & C. Rousseau

Of course the calculations near the blow-up locus S+
2 × {0} will be performed, as usual, in
charts. We start by the traditional rescaling chart {¯ε = 1} in which the expression of (3.1),
after division by r, becomes:
{ ˙¯x = ¯y + br¯x¯y − r2 ¯y2 + E0 + rE1 ¯x + r2E2 ¯x2
˙¯y = ¯x¯y + D; (4.2)

on {r = 0} this gives: { ˙¯x = ¯y + E0
˙¯y = ¯x¯y + D. (4.3)

Hence we see that we have desingularized if either E0 or D is nonzero. When E0 = D = 0
the case E1 ̸= 0 causes no problem as it prevents the existence of limit cycles. But near
E0 = E1 = D = 0 we expect several limit cycles and we cannot desingularize: this new
problem is a real challenge.
For the phase-directional rescaling in the {¯x = 1}-direction we get, after division by r:




 ˙r = r(¯y + ¯ε2E0 + r(b¯y + ¯ε2E1) + r2(−¯y2 + ¯ε2E2))
˙¯ε = −¯ε(¯y + ¯ε2E0 + r(b¯y + ¯ε2E1) + r2(−¯y2 + ¯ε2E2))
˙¯y = ¯ε3D + (1 − 2¯ε2E0)¯y − 2¯y2 − 2r¯y(b¯y + ¯ε2E1) + 2r2 ¯y(¯y2 − ¯ε2E2). (4.4)

On {r = ¯ε = 0} we ﬁnd two singularities, at respectively ¯y = 0 and ¯y = 1/2. At the ﬁrst one
the vector ﬁeld (4.4) is normally repelling, having two-dimensional center bevaviour transverse
to the ¯y-axis; each center manifold contains a line of singularities, deﬁned by {¯y = ¯ε = 0}.
The center manifold on the blow up locus {r = 0} is situated at

¯y = −D¯ε
3(1 + O(¯ε)) (4.5)

and the dynamics on this center manifold is given by

˙¯ε = −¯ε
3E0 + D¯ε
4(1 + O(¯ε)). (4.6)

At the other singularity, the vector ﬁeld (4.4) has a resonant saddle; but this singularity is
unimportant for the study of limit cycles near the graphics under consideration.
The phase-directional rescaling in the {¯x = −1}-direction leads to a similar situation,
given by the expression:




 ˙¯r = −r(¯y + ¯ε2E0 − r(b¯y + ¯ε2E1) + r2(−¯y2 + ¯ε2E2))
˙¯ε = ¯ε(¯y + ¯ε2E0 − r(b¯y + ¯ε2E1) + r2(−¯y2 + ¯ε2E2))
˙¯y = ¯ε3D − (1 − 2¯ε2E0)¯y + 2¯y2 − 2r¯y(b¯y + ¯ε2E1) − 2r2 ¯y(¯y2 − ¯ε2E2). (4.7)

At the origin, system (4.7) is now normally attracting, also having two-dimensional center
manifolds, transverse to the ¯y-axis and containing the line of zeroes given by {¯y = ¯ε = 0}.
The center manifolds on the blow up locus {r = 0} is situated at

¯y = D¯ε
3(1 + O(¯ε)) (4.8)

and the dynamics on this center manifold is given by

¯¯ε = E0 ¯ε
3 + D¯ε
4(1 + O(¯ε)). (4.9)

There is no need to use a phase-directional rescaling in the ¯y-direction.

Singular perturbations 9

4.2 Proof of statement (i) of Theorem 3.1, i.e. for b0 ∈ (0, 2)

From now on we will simply write b0 = b, unless it is explicitly needed to underline the
diﬀerence. Let us start by considering a graphic DF1a, as represented in Figure 1(a). We
recall that it consists of a fast orbit, that we denote by γb
x0, and a critical curve, included
in the x-axis, that we denote by C b
x0 = [fb(x0), x0]; x0 > 0 is the x-coordinate of the point
p0 = (x0, 0) representing the α-limit of the fast orbit; p1 = (fb(x0), 0) represents the ω-limit
of the fast orbit. The relation, expressed by f , i.e. f (x0, b) = fb(x0), is deﬁned by the layer
equation (2.1). It can hence also be deﬁned by following an orbit of the linear vector ﬁeld
{ ˙x = 1 + bx − y
˙y = x, (4.10)

starting at the initial value p0, until it hits again, for the ﬁrst time, the x-axis (at p1 =
fb(x0, 0)).

Important features in order to study the cyclicity of the graphic Γb
x0 = γb
x0 ∪ C b
x0 are the
slow dynamics along C b
x0, and the slow divergence integral, along C b
x0. The slow dynamics,
deﬁned on {y = 0}, is given by
 ˙x = P (x, E); (4.11)

the slow divergence integral is deﬁned as

Ib(x0, E) =
 x0∫

fb(x0)
 x dx
P (x, E) , (4.12)

with E = (E0, E1, E2) and
 P (x, E) = E0 + E1x + E2x
2. (4.13)

Indeed the divergence on y = 0 is given by x when ε = 0 and dt = dx
P (x,E).
The dynamics on the blow up locus S+
2 can be obtained by combining (4.3), together with
the information on {r = 0} given by the phase-directional rescaling. The whole combines to
a compactiﬁcation of (4.3) on a (1, 2)-Poincar´e-Lyapunov disk (PL-disk). To permit the cre-
ation of limit cycles near Γx0, we at least need the existence of an invariant curve, connecting
the points P1 and P0 (see Figure 2), that are situated at (¯ε, r, ¯y) = (0, 0, 0) in respectively
the (¯x = −1) and (¯x = 1)-charts. It is clear from (4.3), (4.5) and (4.8) that such an invariant
curve is only possible for D = 0; it can only be part of a limit periodic set (after blow up) if
E0 ≥ 0.

i) D = 0, E0 > 0

In this case (4.3) contains a regular orbit having, in the (1, 2)-PL disk, P1 as α-limit and
P0 as ω-limit. Both near P1 and P0, the respective systems (4.7) and (4.4) have a center
behaviour which is a hyperbolic saddle, after division by ¯ε2. The parameter D is a “breaking
parameter” (see [DD1] and [DD2]) in the sense that the derivative w.r.t. D of the distance

10 F. Dumortier & C. Rousseau

P1 P0

Figure 2: Blow up of (3.1) at (x, y) = (0, 0).

between the respective center manifolds of P1 and P0 is nonzero. We can measure this dis-
tance using any regular parameter along a section, e.g. {¯x = 0}, transversally cutting both
center manifolds.
Depending on the quadratic function P (x0, E) we are in a perfect position to use the results
given in [DD1] or [DD3].

In case P (x, E) has no zeroes on [fb(x0), x0] and hence is strictly positive there, then we
know from [DD1] that the cyclicity of Γb
x0 can be at most one unit higher than the order of
the zero of Ib(x, E) at x0.
If we do not consider a single x0, but let x0 vary in a compact interval [x1, x2] ⊂]0, ∞[,
then also in this case the total number of limit cycles, close to degenerate graphics Γb
x0, with
x0 ∈ [x1, x2], is at most one unit higher than the total number of zeroes of Ib(x, E) on [x1, x2],
multiplicities taken into account.

It is hence clear that the function f (x0, b) will play an important role in the calculations. In
the Appendix we will prove the following proposition:

Proposition 4.1 The function f (x, b) has the following properties:

(i)
 f (x, b) < −x ≤ 0 for all 0 < b < 2 and x ≥ 0, (4.14)

while f (x, 0) = −x.

(ii) For 0 < b < 2 and x ≥ 0
 f (x, b) < −x − b (4.15)

and
 f ′′(x, b) = ∂2f
∂x2 (x, b) < 0. (4.16)

Singular perturbations 11

(iii) For 0 ≤ b < 2 and x ≥ 0

f ′(x, b) = ∂f
∂x (x, b) = S(x, b)
S(f (x, b), b) , (4.17)

with S(x, b) = x
x2 + bx + 1 .

(iv) For x ≥ 0
 ϕ(x) = ∂f
∂b (x, 0) = −1 + x2 + 1
x arctan x − π x2 + 1
x . (4.18)

From now on we will rely on these properties.

Essential information is given by the function I(x0, b, E) as deﬁned in (4.12); we can write:

I(x0, b, E) =
 x0∫

f (x0,b)
 R(x, E)dx (4.19)

with R(x, E) = x
P (x, E) = x
E2x2 + E1x + E0

Proposition 4.2 Under the condition 0 < b < 2, E0 > 0, and restricting to values (x0, E),
with x0 ≥ 0 and such that P (x, E) is strictly positive on [f (x0, b), x0], we get the following
results:

1) If E1 ≥ 0, then I(x0, b, E) < 0.

2) If E1 < 0, then we have the following cases:

(i) E1 = bE2, implying that I(x0, b, E) is strictly monotone decreasing w.r.t. x0, with
I ′(x0, b, E) < 0 for x0 > 0.

(ii) E1 ̸= bE2
Either I(x0, b, E) is strictly monotone w.r.t. x0, with I ′ non-zero for x0 > 0,
or it has a unique critical point for x0 > 0, which is non-degenerate. Moreover
I ′(x0, b, E) < 0 for x0 → ∞, when bE2 < E1.

3) I(0, b, E) < 0 and I ′(0, b, E) = 0.

Proof
We have
 R(x, E) + R(−x, E) = −2E1x2

P (x, E)P (−x, E) < 0,

when E1 > 0, implying that |R(x, E)| < |R(−x, E)|,

when E1 > 0 and x > 0.

12 F. Dumortier & C. Rousseau

From (4.14) we know that |f (x, b)| > x, for b > 0, while R(x, E) has the same sign as
x. Hence I(x0, b, E) < 0 when E1 > 0. We clearly also have I(x0, b, E) < 0 when E1 = 0.
Moreover, for all E, we have I(0, b, E) < 0.

Let us now restrict to the case E0 > 0 and E1 < 0:

I ′(x, b, E) = ∂I
∂x (x, b, E) = R(x, E) − R(f (x, b), E)f ′(x, b)

= R(x, E) − R(f (x, b), E) S(x,b)
S(f (x,b),b)

= S(f (x,b),b)R(x,E)−R(f (x,b),E)S(x,b)
S(f (x,b),b)

= xf (x,b)(f (x,b)−x)
S(f (x,b),b) · K(x,f (x,b))
L(x,f (x,b)) ,
 (4.20)

where
 K(x, α) = (bE2 − E1)xα + (α + x)(E2 − E0) + E1 − bE0 (4.21)

and
 L(x, α) = (1 + bα + α
2)(1 + bx + x
2)(E0 + E1x + E2x
2)(E0 + E1α + E2α
2).

We clearly see, under the conditions of Proposition 4.2, that L(x, f (x, b)) > 0, so that
I ′(0, b, E) = 0 and, for x > 0, I ′ has the same zeroes as K; I ′(x, b, E) has exactly the
opposite sign of K(x, f (x, b)), when K is nonzero. Remark that K(0, 0) < 0.
A thorough study of the set K(x, a) = 0 is hence needed and especially its position with
respect to the graph of α = f (x, b).
We essentially distinguish two cases:

i) E1 = bE2
In that case
 K(x, α) = (E2 − E0)(α + x + b).

If we restrict to α = f (x, b), then we see that K(x, f (x, b)) is strictly positive by (4.15).

ii) E1 ̸= bE2
In that case K(x, α) = 0 represents a hyperbola whose axes are parallel to the coordinate-
axes. The asymptotes of the hyperbola intersect at
( E0 − E2
bE2 − E1 , E0 − E2
bE2 − E1
 ) .

The hyperbola cuts the coordinate-axes at
( bE0 − E1
E2 − E0 , 0
) and (0, bE0 − E1
E2 − E0
 ) ,

and we remark that bE0 − E1 > 0, since E0 > 0 and E1 < 0. The hyperbola is symmetric
with respect to the diagonal.

Singular perturbations 13

In Lemma 4.3 below we will show that a branch of the hyperbola K(x, α) = 0 can have
at most one point of intersection with the graph of α = f (x, b), and in forthcoming case
the two curves cut transversally. This will follow from the non existence of contact points
between K(x, α) = 0 and a vector ﬁeld having α = f (x, b) as a trajectory.

We can now give an overview of the diﬀerent cases concerning the relative position of the
hyperbola and the curve α = f (x, b), and check the consequences for I ′(x, b, E), and hence
also for I(x, b, E). In each case we will see that there is at most one intersection point of
the hyperbola with α = f (x, b), leading to at most one zero of I ′(x, b, E), which moreover is
simple.

The diﬀerent cases are represented in Figure 3. We also represent the sign of K. Seen

x

-+

-
 a

(a) D > 0, A, C < 0
 x
-

+
 a
 +

(b) D, A, C > 0
 x

+

-

+
 a

(c) D, A > 0, C = 0
 x
-

+
 +

a

(d) D, A > 0, C < 0

x
-+

-
 a

(e) D, C > 0, A < 0 (f) D, A, C < 0
 x

+
 -
 +

a

(g) D, A < 0, C=0
 x
-
 +

+
 a

(h) D, A < 0, C > 0

Figure 3: Diﬀerent positions of the hyperbola K(x, α) = 0 (see (4.22) for the notation).

in the (x, α)-plane, the graph of α = f (x, b) is approximately as in Figure 4. Taking into
account the information, pictorially represented in the Figures 3 and 4, together with the
result proved in Lemma 4.3, the claim is clear. In Figure 3 the following notation is used





A = bE2 − E1
C = E0 − E2
D = (E2 − E0)2 − (E1 − bE0)(bE2 − E1)
 (4.22)

An intersection point can appear in all cases except for the cases (c) and (d). It will necessarily
appear in cases (a), (f) and g. In the remaining cases this depends on the value of the
parameters. The sign of K in the diﬀerent regions is determined from the fact that K(0, 0) <

14 F. Dumortier & C. Rousseau

a
 x

Figure 4: Graph of α = f (x, b).

a b

Figure 5: Graph of I(x, b, E) when it is not monotone.

0. Hence I ′(x, b, E) > 0 for x ∼ 0, except possibly in cases (b), (e) and (h). In cases (b)
(resp. (e) and (h)) it is possible to have I(x, b, E) monotone increasing (resp. decreasing)
with I ′(x, b, E) > 0 (resp. I ′(x, b, E) < 0) for x > 0, while it is also possible to encounter a
function I(x, b, E) having a single critical point which is a non-degenerate minimum (resp.
maximum). In cases (a), (f) and (g), I(x, b, E) necessarily has a non-degenerate maximum.
In cases (c) and (d), I(x, b, E) is monotonically increasing.
This ends the proof of Proposition 4.2. ✷
In Figure 5 we represent the two possibilities for I(x, b, E) to have a critical point, not paying
attention to the relative position w.r.t. the x-axis, nor to the exact behaviour for x → +∞.
The case of a non-degenerate minimum (case (b) of Figures 4 and 5) can only occur for
E1 < bE2 (A > 0).

Lemma 4.3 In case E2 ̸= bE1, a branch of the hyperbola K(x, α) = 0 has at most one point
of intersection with the graph of α = f (x, b). At such point both curves intersect transversally.

Proof From (4.17) we see that the graph of α = f (x, b) is an orbit of the system
{ ˙x = α(x2 + bx + 1)
˙α = x(α2 + bα + 1). (4.23)

If we would have two intersection points of a branch of the hyperbola with the graph of
α = f (x, b), then in between these two intersection points, there would be a point of contact
of (4.21) with K(x, α) = 0.
The same would happen at a point where the intersection of the two curves is not transverse.
We will now show that the hyperbola is never tangent to an orbit of (4.23). At such a contact

Singular perturbations 15

point (x0, α0) the vector (α0(x2
0 + bx0 + 1), x0(α2
0 + bα0 + 1)) has to be perpendicular to

∇K(x0, α0) = ((bE2 − E1)α0 + (E2 − E0), (bE2 − E1)x0 + (E2 − E0))

and moreover K(x0, α0) = 0.

The former condition implies that

((bE2 − E1)x2
0 + (E2 − E0)x0)(α2
0 + bα0 + 1)
= (x2
0 + bx0 + 1)((bE2 − E1)α2
0 + (E2 − E0)α0). (4.24)

Remark that we may suppose that (bE2 − E1)z + (E2 − E0) is diﬀerent from zero for both
z = x0 and α0, since otherwise they both would have to be zero, which is impossible since
x0 · α0 < 0.
It is a straightforward calculation to see that condition (4.24) can be written as:

(α0 − x0)[(b
2 − 1)E2 − bE1 + E0)α0x0 + (bE2 − E1)(α0 + x0) + (E2 − E0)] = 0.

It hence suﬃces to show that there does not exist a common solution of:
{ (bE2 − E1)xα + (E2 − E0)(α + x) + E1 − bE0 = 0
(b(bE2 − E1) − (E2 − E0))xα + (bE2 − E1)(α + x) + E2 − E0 = 0. (4.25)

From the former equation we get an expression for xα, and plugging it into the latter one, it
implies that a solution of (4.25) necessarily satisﬁes:

(x + α)[−b(E2 − E0)(bE2 − E1) + (E2 − E0)2 + (bE2 − E1)2]
+[(E2 − E0)(bE2 − E1) − b(bE2 − E1)(E1 − bE0) + (E2 − E0)(E1 − bE0)] = 0. (4.26)

A straightforward calculation, using E2
0 + E2
1 + E2
2 = 1 reduces equation (4.26) to:

(x + α + b)(1 − bE0E1 − bE1E2 + (b
2 − 2)E0E2) = 0,

implying the existence of a solution to
{ bE0E1 + bE1E2 + (2 − b2)E0E2 = 1
E2
0 + E2
1 + E2
2 = 1.

This is equivalent to proving a non-zero solution to

E2
0 + E2
1 + E2
2 − bE0E1 − bE1E2 + (b
2 − 2)E0E2 = 0. (4.27)

We only need to restrict to the range of E-values that we consider, namely E0 > 0, E1 < 0
and E2 ̸= bE1.

Since the left hand side of (4.26) is a quadratic form we merely have to calculate the eigen-
values of its matrix; they are respectively 1
2 (2 + b2), 1
2 (4 − b2) and 0. A straightforward
calculation shows that the eigenspace for the eigenvalue 0 is given by

(E0, E1, E2) = E0(1, b, 1),

16 F. Dumortier & C. Rousseau

which is not in the range of E-values that we consider. ✷

This ﬁnishes the study for E0 > 0, under the condition that P (x, E) > 0 on C b
x0 =
[fb(x0), x0], with x0 ∈ K ⊂ (0, ∞).
Of course, the slow dynamics, given by

P (x, E) = E2x
2 + E1x + E0,

with E2
2 + E2
1 + E2
0 = 1, can have zeroes on the segments [fb(x0), x0] under consideration. P
has at most 2 zeroes, multiplicity taken into account. It can have a unique double zero in
case E2 ≥ 0. This double zero will be situated at the origin in case E1 = 0 = E0, a case that
we discarded from the statements in Theorem 3.1. For (E0, E1) ̸= (0, 0) a possible double
zero will be situated at a non-zero value x0, inducing (see [DD3]) that nearby systems (3.1)
can have at most one limit cycle lying near the graphics Γb
x0, with x0 ∈ K. Such a limit cycle
is hyperbolic; it is attracting if x0 < 0 and repelling if x0 > 0.
Another possibility under which a slow dynamics with zeroes on [fb(x0), x0] can never-
theless permit limit cycles near Γb
x0 is when a simple zero occur at x0, at fb(x0) or at both x0
and fb(x0). All these cases have been studied in [DD3]. The ﬁrst two have cyclicity one; the
third one has cyclicity two if the product of the hyperbolicity ratios at the two saddle points
is diﬀerent from one. Recall that the hyperbolicity ratio of a saddle point is the quotient of
minus the negative eigenvalue to the positive eigenvalue. The hyperbolicity ratio at (x0, 0) is
∣
∣
∣
∣ P ′(x0, E)
x0
 ∣
∣
∣
∣ (4.28)

and that at (fb(x0), 0) is ∣
∣
∣
∣ fb(x0)
P ′(fb(x0), E)
 ∣
∣
∣
∣ . (4.29)

Since P ′ is the derivative of the slow movement, then P ′(x0, E) and P ′(fb(x0), E) are the
“slow” eigenvalues at (x0, 0) and (fb(x0), 0) respectively.
Since we suppose that P (x, E0), for the chosen value E = E0, has zeroes at respectively
x0 and fb(x0), we have P (x, E0) = E0
2 (x − x0)(x − fb(x0)),

with E0
2 > 0. As such
 P ′(x0, E0) = E0
2 (x0 − fb(x0))
P ′(fb(x0), E0) = E0
2(fb(x0) − x0)

Since fb(x0) < −x0 it is clear that the product of the hyperbolicity ratios (4.28) and (4.29)
is diﬀerent from one, thus ﬁnishing the proof of statement (i) for E0 > 0.

(ii) D = 0, E0 = 0.

The slow dynamics is given by

P (x, (0, E1, E2)) = E1x + E2x
2,

Singular perturbations 17

showing that no passage at x = 0 is possible when E1 ̸= 0. Since the condition E2 ≥ 0 is
necessary to admit limit cycles near the Γb
x0, for x0 > 0, we end up with the case

(E0, E1, E2) = (0, 0, 1)

that we discarded from the statements in Theorem 3.1.
The unicity of the limit cycle for E1 ≥ 0 follows from Proposition 4.2(1), stating that
I < 0 in that case.
This ends the proof of statement (i) in Theorem 3.1.

4.3 Proof of statement (iii) of Theorem 3.1: the case b0 = 0 and (D, E1) ̸= (0, 0)

Like in the proof of statement (i) it is clear that limit cycles are only possible near systems
(3.1) for which D = 0. In the subsequent calculations we will hence suppose that D = 0. In
the same way as before we can also suppose that E0 > 0.
In case b = 0 we can use that f (x0, 0) = −x0

and
 I(x0, 0, E) =
 x0∫

−x0
 x
E2x2 + E1x + E0 dx. (4.30)

This integral can easily be calculated, depending on the speciﬁc value of E; recall that we
take E1 ̸= 0, so that no passage near 0 is possible unless E2 ̸= 0. There is however no need
to calculate this integral. For E1 = 0 it is clearly identically zero. Moreover we see that

∂I
∂E1 (x0, 0, E) = −
 x0∫

−x0
 x2

(E2x2 + E1x + E0)2 dx < 0, (4.31)

implying that I(x0, 0, E), for x0 > 0, is everywhere strictly negative for E1 > 0 and every-
where strictly positive for E1 < 0. The same property also holds if we take x0 ∈ K, K
compact, and b ∼ 0.
As in the proof of statement (i) this induces the occurrence of at most one limit cycle near
graphics Γ0
x0 with x0 ∈ K ⊂ (0, ∞), for systems (3.1) with ε > 0 suﬃciently small, D ∼ 0
and (E0, E1, E2), with E0 > 0, near values for which P (x, E) = E2x2 + E1x + E0 has no
zeroes on [−x0, x0].
Since E1 ̸= 0 it is not possible for P to have neither a zero at both −x0 and x0 nor a double
zero at the origin, so that statement (iii) follows from [DD3], in case P (x, E) has zeroes on
[−x0, x0].

4.4 Proof of statement (ii) of Theorem 3.1: the case b0 = 0 and (D, E1) =
(0, 0)

Recall that we can keep E0 > 0, so that from [DD2] follows that there exists a smooth
function D0(ε, b, E, x0)

18 F. Dumortier & C. Rousseau

with the property that periodic orbits of system (3.1), lying near graphics Γb
x0, with x0 ∈
K ⊂ (0, 0), can only occur for D = D0(ε, b, E, x0).
For precise understanding of this statement, we consider {x = 0, y > 1}. Each point on
this half-line belongs to a unique graphic Γb
x0, and we can hence parametrize the points on
{x = 0, y > 1} by means of this unique x0. System (3.1), for ε ∼ 0, will exhibit a closed orbit
passing through (0, y), characterized in this way by x0, if and only if D = D0(ε, b, E, x0).
From this point on we can no longer rely on the existing literature to get results on limit
cycles of system (3.1), for ε ∼ 0, by merely studying the zeroes of the slow divergence integral.
We will have to recall and extend some steps in the proofs given in [DD1], [DD2] and [DD3].
To that end we consider a ﬁrst section

T1 = {x = 0, y > 1}

that we parameterize by (ε, b, D, E, x0) in the way explained above.
We consider a second section T2 that we deﬁne along the blown-up locus of the origin.
More precisely, in the blow-up coodinates (x, y, 1) as deﬁned in (4.1), we consider

T2 = {x = 0}.

T2 is hence deﬁned in the traditional rescaling chart {ε = 1}. We know from [DD2] that,
by following the orbits of systems (3.1) both in forward time and in backward time, we can
deﬁne smooth transition maps from T1 to T2, denoted by respectively ∆1 and ∆2. Closed
orbits of system (3.1) for ε > 0, ε ∼ 0, are given by zeroes of the displacement map

∆ = ∆1 − ∆2.

∆ is smooth in the variables (ε, b, D, E, x0), also at ε = 0. We can take b ∈ (−2, 2), (D, E) ∈
C1, and x0 ∈ K ⊂ (0, ∞).
In this part of the proof we will of course take b ∼ 0, ε ∼ 0, and (D, E1) ∼ (0, 0).
Since ∆(0, b, 0, E, x0) = 0 and ∂∆
∂D (0, b, 0, E, x0) ̸= 0 (as discussed in Section 4.2), it is a
consequence of the Implicit Function Theorem that solution of ∆ = 0, for ε ∼ 0 and D ∼ 0,
can only occur for D = D0(ε, b, E, x0),

with D0 some smooth function.
Moreover we know that the systems (3.1) with b = D = E1 = 0 represent centers since
they are invariant under (x, t) ↦→ (−x, −t). As such

∆(ε, 0, 0, (E0, 0, E1), x0) = 0, (4.32)

as well as
 D0(ε, 0, (E0, 0, E1), x0) = 0. (4.33)

Instead of continuing working with ∆, we prefer to work with

̃∆(ε, b, E, x0) = ∆(ε, b, D0(ε, b, E, x0), E, x0), (4.34)

which is a smooth function. The closed orbits correspond to the solutions of

̃∆(ε, 0, (E0, 0, E2), x0) = 0. (4.35)

Singular perturbations 19

From [DD1] improving the results of [DR1], we know that ∂ e∆
∂x0 is, on {ε > 0}, C ∞-contact
equivalent to
 I(x0, b, E) + ϕ1(x0, ε, b, E) + ϕ2(ε, b, E)ε ln ε, (4.36)

for some C ∞ functions ϕ1 and ϕ2, with I(x0, b, E) = Ib(x0, E) the slow divergence integral
as deﬁned in (4.12) and ϕ1 is O(ε).
We recall that “C ∞-contact equivalent” means that ∂ e∆
∂x0 is the product of a strictly positive
C ∞ function with the expression in (4.36). The C ∞-contact equivalence only holds for ε > 0
but the functions ϕ1 and ϕ2 are C ∞ also at ε = 0.
The function I is analytic and it is identically zero for b = E1 = 0. From (4.35) we even
know that ∂ e∆
∂x0 is identically zero for b = E1 = 0, so that we can write (4.36) as

b(I b(x0, b, E) + Φb(x0, ε, b, E)) + E1(I 1(x0, b, E) + Φ1(x0, ε, b, E)), (4.37)

where both Φb and Φ1 are O(ε) and ε-regularly smooth in (x0, b, E), as deﬁned in [DR2]. It
means that Φb and Φ1 and all their partial derivatives w.r.t. (x0, b, E) are continuous in ε,
including at ε = 0.
We will now start by keeping E0 = 1, thus writing E2 instead of E2, with E2 belonging
to an arbitrarily large compact and

(b, E1) = u(b, E1) (4.38)

with u ≥ 0 and b
2 + E2
1 = 1. (This means that we made an abuse of notation and kept the
same E1 when we took the chart E0 = 1.) As already mentioned we can limit our study to
b ≥ 0. Expression (4.37) can be written as

u [I(x0, b, E1, E2) + O(u) + O(ε)
] , (4.39)

where O(u) represents an analytic function and O(ε) an ε-regularly smooth function and

I(x0, b, E1, E2) = b ∂I
∂b (x0, 0, (1, 0, E 2)) + E1 ∂I
∂E1 (x0, 0, (1, 0, E 2))
= limu→0 1
u I(x0, ub, (1, uE 1, E2)). (4.40)

We see that (see Appendix)

∂I
∂b (x0, 0, (1, 0, E 2)) = x0
E2x2
0+1
 (−1 + 1+x2
0
x0 arctan x0 − π 1+x2
0
x0
 )

∂I
∂E1 (x0, 0, (1, 0, E 2)) = − ∫ x0
−x0 x2dx
(E2x2+1)2 . (4.41)

Both functions in (4.41) are strictly negative.
Therefore the expression inside brackets in (4.39) is strictly negative when we take E1 ≥ 0
and b ≥ 0 and strictly positive when E1 ≤ 0 and b ≤ 0. The same is hence true for expression
(4.39) itself if we take u > 0. This yields the conclusion on the existence of at most one limit
cycle, which is hyperbolic if it exists and attracting.
It remains to look what happens with (4.39) when we take E1 · b < 0. We already know
that it suﬃces to take b ≥ 0 and, to have uniformity in the results, we will take E1 ≤ 0.
Instead of working directly with (4.39) we will consider its derivative with respect to x0 that
can be written as

20 F. Dumortier & C. Rousseau

u [ ∂I
∂x0 (x0, b, E1, E2) + O(u) + O(ε)
] , (4.42)

where O(u) represents an analytic function, O(ε) is an ε-regularly smooth function and

∂I
∂x0 = lim
u→0 1
u ∂I
∂x0 (x0, ub, (1, uE 1, E2)), (4.43)

because of (4.40). We will now prove that ∂I
∂x0 can have at most three zeroes, multiplicity
taken into account, for the conditions on x0, E2 and (b, E1) under consideration. This will
of course imply a similar statement for the expression in (4.42) for u > 0, u ∼ 0.
By (4.43) it suﬃces to study ∂I
∂x0 . Hence, because of (4.20) we only need to consider
K(x0, fb(x0)), where K is given in (4.21). Noting that f0(x0) = −x0 we write

fb(x0) = −x0 + bψ(x0, b), (4.44)

where ψ(x0, b) is analytic for nonzero x0 and ψ(x0, 0) = ϕ(x) is the transcendental function
deﬁned in (4.18).
From (4.20) and (4.21) we see that ∂I
∂x0 is C ∞-contact equivalent (even C ω-contact equiv-
alent) to
 K1(x0, b, E1, E2) = (b E2 − E1)x
2
0 − b(E2 − 1)ϕ(x0) + b − E1. (4.45)

The function K1 in (4.45) is a linear combination of the three linearly independent func-
tions {1, x2
0, ϕ(x0)}. Hence it can only be identically zero for b = E1 and E2 = 1, a case
in which we already proved the cyclicity to be less than or equal to 1. For the values of
(b, E1, E2) we are considering now, (4.45) never vanishes identically and hence ∂I
∂x0 will have
a uniformly bounded number of zeroes. In the next proposition we show that this number is
three.

Proposition 4.4 Any linear combination of {1, x2, ϕ(x)} has at most three zeroes in ]0, ∞[,
multiplicity taken into account.

Proof Let us consider F (x) = A + Bx2 + Cϕ(x), with (A, B, C) ̸= (0, 0, 0). If B = C = 0
then F does not vanish. Otherwise we consider

F ′(x) = 2Bx + C ( x2 − 1
x arctan x + 1
x − π x2 − 1
x
 ) . (4.46)

When C = 0 then F ′(x) does not vanish, yielding at most one zero for F (x). If C ̸= 0, let
G(x) = F ′(x)
x . Then G′(x) = 0 if and only if

π + arctan x = x(3 + x2)
(x2 + 1)(3 − x2) . (4.47)

Since the left hand side is positive, the only solutions of (4.47) lie in ]0, √3[. Moeover the
derivative of x(3+x2)
(x2+1)(3−x2) − π − arctan x is 16x4
(x2+1)2(3−x2)2 > 0, yielding that (4.47) has at most
one positive solution and hence that F has at most three positive zeroes. ✷

Singular perturbations 21

As such we see that for ε > 0, ε ∼ 0, expression (4.36) has at most four zeroes, multiplicity
taken into account. This result holds in a uniform way on ε (see [DD1]) as long as the slow
dynamics is diﬀerent from zero on [−x0, x0], with x0 ∈ K ⊂ (0, ∞). The slow dynamics is
given by ˙x = E0 + E2x
2,

and since we avoid working at E0 = 0, it can also be expressed as

˙x = 1 + E2x
2.

So the only situation where the results from [DD1] do not apply is when we consider E2 < 0
and x0 = x0 = 1/e2 with e2 = (−E2)1/2.
This situation has not been studied in [DD3], since it is too degenerate. We can however
develop a similar elaboration as in [DD3] to treat the speciﬁc case under consideration. More
precisely we will ﬁrst show that I(x0, b, E1, E2) as deﬁned in (4.40), with E2 = −e2
2, has at
most a simple zero for x0 ∼ x0 = 1/e2 and b
2 + E2
1 = 1 and then we will show that the
result extends to (4.39) itself, when we add the perturbation O(u) + O(ε), implying that the
cyclicity of Γ0
x0 is at most two.
Let us start with the ﬁrst claim. For x0 ∼ 1/e2, but x0 < 1/e2 we can calculate ∂I
∂E1 (see
(4.41)) and write expression (4.40) as:

b ∂I
∂b (x0, 0, (1, 0, −e2
2)) + E1 ∂I
∂E1 (x0, 0, (1, 0, −e2
2))

= 1
1−e2
2x2
0
 [b(−x0 + (1 + x2
0)(arctan x0 − π)) − E1
2e3
2
 (
2e2x0 − (1 − e2
2x2
0) ln ( 1+e2x0
1−e2x0
 ))] . (4.48)

Expression (4.48) has only to be considered for x0 ∈ (0, 1
e2 ). We will now show that the
expression in between brackets in (4.48) has at most one simple zero for x0 ∼ x0, and this
for any choice of (b, E1) ∈ S1. We therefore write this expression as

bf (x0) − E1
2e3
2 g(x0), (4.49)

with
 f (x0) = −x0 + (1 + x2
0)(arctan x0 − π), (4.50)

g(x0) = 2e2x0 − (1 − e
2
2x
2
0) ln ( 1 + e2x0
1 − e2x0
 ) . (4.51)

We also see that
 f ′(x0) = 2x0(arctan x0 − π), (4.52)

g′(x0) = 2e
2
2x0 ln (1 + e2x0
1 − e2x0
 ) . (4.53)

For x0 → 1/e2 the function f (x0) · g′(x0) − g(x0)f ′(x0) tends to +∞, inducing that (4.49),
and hence also (4.48) can never be identically zero, unless (b, E1) = (0, 0). This also implies
that (4.48) has at most one simple zero for x0 ∼ x0, as claimed.

22 F. Dumortier & C. Rousseau

We will now show that this implies that the cyclicity of Γ0
x0 is at most two. We recall that

we observed that ∂ e∆
∂x0 is, on {ε = 0}, C ∞ contact equivalent to (4.36), an expression that we
can also write as (4.37). This however has only been proved for a regular slow dynamics. We
now want to get, in the case under consideration, a similar result for x0 ∼ x0 = 1/e2, to be
able to conclude on the number of zeroes of ̃∆ for x0 ∼ x0. To study I(x0, b, E) for x0 ∼ x0
we multiply it by the positive quantity

1 − e
2
2x
2
0 = 1 − ( x0
x0
 )2 , (4.54)

where ±x0 = ±1/e2 represent the (simple) zeroes of the slow dynamics along the critical
curve {y = 0} for ε = 0. The expression in between brackets in (4.48) is in fact I multiplied
by (1 − e2
2x2
0), expressed in (b, E1) = u(b, E1), divided by u and evaluated at u = 0. We will
now deﬁne in (4.59) below a smooth extension ψ of (4.54) and will then continue studying
ψ · ∂ e∆
∂x0 instead of ∂ e∆
∂x0 itself. Let us ﬁrst show how to deﬁne ψ.
We are looking at system (3.1) or more precisely at
{ ˙x = y + bxy − y2 + ε2(1 + E1x − e2
2x2)
˙y = xy + ε3D, (4.55)

with (b, D, E1) ∼ (0, 0, 0). (As before we make an abuse of notation by not changing the
name of the parameter E1 when passing to the chart E0 = 1.)
These systems have a hyperbolic saddle near (x, y) = (x0, 0) and (x, y) = (−x0, 0) for ε ∼
0, ε > 0.
To prove this we use the center manifold theorem near these points providing C ∞ center
manifolds given as graphs of functions yc(x) with

yc(x) = D
x ε
3 (−1 + 1
x2 (1 + E1x − e
2
2x
2)ε
2 + O(ε
3)
) . (4.56)

(These are calculated as series in ε with coeﬃcients given by functions of x.) On such a
center manifold, always near (±x0, 0) system (4.55) is described by

˙x0 = ε
2 [
(1 + E1x0 − e
2
2x
2
0) − (1 + bx0)
x0 Dε + O(ε
2)
] , (4.57)

and zeroes are given by
 z± = ± 1
e2 + O(E1, ε). (4.58)

The expression of z+ and z− depends on D, but as before we will restrict D to D0(ε, b, E, x0),
as used in (4.34).
Seen in the x0-coordinate, as used from the start in Section 4.4, it is easy to see that closed
orbits are only possible for x0 ∈]z−, z+[. We now consider

ψ(ε, b, E, x0) = (1 − x0
z−
 ) (
1 − x0
z+
 ) (4.59)

as a natural extension of (4.54). As announced, instead of studying directly ∂ e∆
∂x0 , with ̃∆ as

introduced in (4.34), we multiply ∂ e∆
∂x0 by the function ψ given (4.59).

Singular perturbations 23

We will now show that ψ · ∂ e∆
∂x0 is, for any r ∈ N, C r contact equivalent to an ε-regular

C r extension of the slow divergence integral, mutiplied by ψ. This will imply that ψ · ∂ e∆
∂x0
is for any r ∈ N, C r contact equivalent to an ε-regular C r extension of ψ · I, which near
(b, E1) = (0, 0) and because of the fact that ∂ e∆
∂x0 ≡ 0 at (b, E1) = (0, 0) can be written as

u[(1 − e
2
2x
2
0)I(x0, b, E1, −e
2
2) + O(u) + O(ε)], (4.60)

thus inducing that ψ · ∂ e∆
∂x0 , and hence also ∂ e∆
∂x0 , can have at most one simple zero for
x0 ∼ x0. The use of ψ only serves to be able to rely on the known results about (1 −
e2
2x2
0)I(x0, b, E1, −e2
2). In fact it is possible to prove that, for any r ≥ 1, ∂ e∆
∂x0 is C r-contact

equivalent to an ε-regular C r extension of I. Seen that ∂ e∆
∂x0 is, for ε > 0, C ∞ contact equiv-
alent to the (full) divergence integral multiplied by ε2 and taking into account the known
results in case of a regular dynamics, the full divergence integral only needs to be studied
near the endpoints x0 = ±x0. Near each of these points we will prove that the full divergence
integral multiplied by ε2 is, for any r ≥ 1, a C r extension of the slow divergence integral.
The proof of this fact is based on the use of the normal linearization theorem of Takens
[T], permitting to write (4.55) near the points (z+, yc(z+)) and (z−, yc(z−)) as
{ ˙v = ε2µ±(ε, b, E)v
˙w = λ±(ε, b, E, u)w, (4.61)

for which {w = 0} represent a center manifold, {v = 0, w = 0} is the singularity and λ±, µ±

are, for given r ∈ N, C r functions with the following properties:

λ
+(0, 0, (1, 0, −e
2
2), 0) = x0

represents the unstable eigenvalue of (3.1) for x0 ∼ x0, and similarly

λ−(0, 0, (1, 0, −e
2
2), 0) = −x0

represents the stable eigenvalue of (3.1) for x0 ∼ −x0:

µ+(0, 0, (1, 0, −e
2
2), 0) = −2/x0

represents the stable eigenvalue at x0 for the slow dynamics and

µ−(0, 0, 0(1, 0, −e
2
2), 0) = 2/x0

represents the unstable eigenvalue −x0 for the slow dynamics.
The product of the hyperbolicity ratios at both saddles is equal to 1, so we cannot use the
results from [DD3].
The calculations that we intend to make near (x0, 0) are similar to those near (−x0, 0), so
we will consider expression (4.61) with λ− and µ− and suppose that the side under consid-
eration is v > 0. We write λ and µ instead of respectively λ− and µ−. In these coordinates
(v, w), used in (4.61) we can now compare ε2 times the divergence integral along orbits from
(v, 1) to (1, w) to the slow divergence integral for b = 0 and E1 = 0. The divergence integral
multiplied by ε2 is given by
1
µ(ε, b, E)
 1∫

v
 λ(ε, b, E, s) + ε2µ(ε, b, E)
s ds; (4.62)

24 F. Dumortier & C. Rousseau

the related slow divergence integral for b = 0 and E1 = 0 integral is given by

1
µ(0, 0, (1, 0, −e2
2))
 1∫

v
 λ(0, 0, (1, 0, −e2
2), s)
s ds. (4.63)

For simplicity in notation, let us introduce µ0 = µ(0, 0, (1, 0, −e2
2)),

λ0(s) = λ(0, 0, (1, 0, −e
2
2), s) and δ = (ε, b, E 1).

The slow divergence integral can then be written as:

1
µ0
 1∫

v
 λ0(s)
s ds (4.64)

and the full divergence integral, multiplied by ε2, as:

1
µ0 + 0(∥δ∥)
 1∫

v
 λ0(s)(1 + φ(ε, b, E, s))
s ds, (4.65)

with φ(ε, b, E, s) = O(∥δ∥). We now write φ as:

φ(ε, b, E, s) = φ0(ε, b, E) + sφ1(ε, b, E, s),

so that (4.65) can be written as:

1
µ0+O(∥δ∥)
 1∫

v
 λ0(s)
s (1 + φ0(ε, b, E) + sφ1(ε, b, E, s))ds

= ( 1+O(∥δ∥)
µ0+O(∥δ∥) ) 1∫

v
 λ0(s)
s ds + O(∥δ∥). (4.66)

This shows that the (full) divergence integral multiplied by ε2 is a C r extension of the
slow divergence integral, thus proving the claim that we made on ψ · ∂ e∆
∂x0 . ✷

A Appendix: Proof of Proposition 4.1

In paragraph 3 the function f (x0, b) has been deﬁned and we know that it plays an important
role in the study of the cyclicity of the graphic Γb
x0. It can be calculated, or at least its essential
properties can be studied by merely considering the linear system, given by (2.12), that we
repeat here: { ˙x = 1 + bx − y
˙y = x. (A.1)

It is deﬁned by considering an orbit of (A.1) starting at some point (x0, 0), with x0 ≥ 0, and
following it until it hits again, for the ﬁrst time, the x-axis at a point whose x-coordinate we
deﬁne to be f (x0, b). Recall that −2 < b < 2, and that we can limit to b ≥ 0.

Singular perturbations 25

We ﬁrst introduce a ﬁrst integral for (A.1), obtained by considering invariant straight lines
F (x, y) = 0, with
 F (x, y) = 1 − Ax − y. (A.2)

Clearly ˙F = −AF , if A satisﬁes A2 + Ab + 1 = 0, hence

A, ¯A = 1
2
 (
−b ± i(4 − b
2)
1/2) . (A.3)

This gives the ﬁrst integral:

Hb(x, y) = (1 − Ax − y)
i ¯A(1 − ¯Ax − y)
−iA, (A.4)

which on {y = 0} gives:

Hb(x, 0) = H 0
b (x) = (1 − Ax)
i ¯A(1 − ¯Ax)
−iA. (A.5)

We also see that
 (H 0
b )′(x) = H 0
b (x) iA ¯A( ¯A−A)x
|A|2x2−2ReAx+1

= H 0
b (x) (4−b2)1/2x
x2+bx+1 ,
 (A.6)

since ReA = − b
2 , A ¯A = 1 and ImA = 1
2 (4 − b2)1/2.

Writing x instead of x0, we know that f (x, b) is given by

H 0
b (f (x, b)) = H 0
b (x),
f (x, b) < 0, (A.7)

and hence:
 f ′(x, b) = ∂f
∂x (x, b) = S(x, b)
S(f (x, b), b) , (A.8)

with
 S(x, b) = x
x2 + bx + 1 . (A.9)

Indeed:
 (H 0
b (f (x, b)))
′ = (H 0
b )
′(f (x, b)) · f ′(x, b)

= (4 − b
2)
1/2S(f (x, b))H0(f (x, b)) · f ′(x, b)

= (4 − b2)
1/2H 0
b (x)S(x).

We can also calculate ∂f
∂b (x, b) by deriving

H 0(f (x, b), b) = H 0(x, b), (A.10)

26 F. Dumortier & C. Rousseau

introducing H 0(x, b) = H 0
b (x). We get:

∂f
∂b (x, b) =
 ∂H 0
∂b (x, b) − ∂H 0
∂b (f (x, b), b)

∂H 0
∂x (f (x, b), b) . (A.11)

We would like to evaluate ∂f
∂b at b = 0, where we already know that f (x, b) = −x. From (A.5)
we get

∂H 0

∂b (x, b) = H 0(x, b) [ −i ¯Ax
1 − Ax dA
db + iAx
1 − ¯Ax d ¯A
db + i d ¯A
db ln(1 − Ax) − i dA
db ln(1 − ¯Ax)
] .(A.12)

From A2 + Ab + 1 = 0 we get
 dA
db = − A
2A + b ,

and since A = i and ¯A = −i for b = 0, this gives

dA
db |b=0= d ¯A
db |b=0= − 1
2 . (A.13)

We need to use (A.12) to evaluate ∂H 0
∂b (f (x, 0), 0). Of course H 0(x, 0) = H 0(f (x), 0). The
bracket part of (A.12) is odd in x but we must pay attention to the logarithmic terms
whose imaginary part depends on the argument of 1 − if (x, 0) and 1 + if (x, 0). The quantity
1−if (x, 0) (resp. 1+if (x, 0) is the analytic continuation of 1−ix−y (resp 1+ix−y) along the
trajectory joining (x, 0) to (f (x), 0). This trajectory surrounds the point (0,1) in the positive
direction. Let Y = y − 1. We work in the (x, Y ) coordinates. Let ±θ = arg(±ix − Y )|y=0.
When we move along the trajectory of the vector ﬁeld, ix − Y turns in the positive direction
and arg(ix − Y ) increases from θ to 2π − θ. Similarly −ix − Y turns in the negative direction
and arg(−ix − Y ) decreases from −θ to −2π + θ. Hence the contribution to the real part in
the bracket expression of (A.12) is −θ. When we evaluate the same expression at f (x, 0) the
contribution to the real part is θ − 2π. It follows that

∂H 0
∂b (x, 0) = H 0(x, 0) [ x
1+x2 + i
2 ln ∣
∣
∣ 1+ix
1−ix ∣
∣
∣ − θ]

= H 0(x, 0) [ x
1+x2 − arctan x
] (A.14)

and
 ∂H 0
∂b (f (x, 0), 0) = H 0(f (x, 0), 0) [− x
1+x2 − i
2 ln ∣
∣
∣ 1+ix
1−ix ∣
∣
∣ + θ − 2π]

= H 0(f (x, 0), 0) [− x
1+x2 + arctan x − π] . (A.15)

Using (A.6) with b = 0 this implies

ϕ(x) = ∂f
∂b (x, 0) =
 x
x2+1 −arctan x+π

− x
x2+1
= −1 + x2+1
x arctan x − π x2+1
x . (A.16)

Lemma A.1 When b > 0, then f (x, b) < −x − b for all x ≥ 0.

Singular perturbations 27

Proof Consider F (x, y) = x2 + y2 − bxy + bx − 2y.

F is a Lyapunov function for (A.1), having a minimum at (0, 1) with F (0, 1) = −1.
Indeed:
 ˙F (x, y) = bx2 + by2 − b2xy − 2by + b
2x + b

= G(x, y).

To obtain that G(x, y) ≥ 0, it suﬃces to check that G attains its minimum at (0, 1).

Now F (x, 0) = x2 + bx is zero iﬀ x = 0 or x = −b, implying already that

f (0, b) < −b.

We also see that f (x, b) has to be inferior to x1 < 0, where x1 satisﬁes

F (x1, 0) = F (x, 0).

This induces (x1 − x)(x1 + x + b) = 0,

implying that f (x, b) + x + b < 0 as claimed. ✷

We can also observe that

f ′′(x, b) = ∂2f
∂x2 (x, b) = ((f (x, b))2 + bf (x, b) + 1)
(x2 + bx + 1)2 · (x2 − (f (x, b))2)
(f (x, b))3 < 0, (A.17)

implying that the graph of f (x, b), for each b > 0 separately, is a concave curve. It intersects
{x = 0} at f (0, b) < −b < 0, and stays below the straight line with equation

f = −x − b

in a (x, f )-plane.
One can show that
 lim
x→∞ f (x, b)
x = −1.

References

[ADL] J.C. Art´es, F. Dumortier, J. Llibre, Limit cycles near hyperbolas in quadratic sys-
tems, preprint.

[ALS] J.C. Art´es, J. Llibre, D. Schlomiuk, Quadratic diﬀerential systems with a weak focus
of second order, Internat. J. Bifur. Chaos Appl. Sci. Engrg. 16 (2006), 3127–3194.

[DD1] P. De Maesschalck, F. Dumortier, Time analysis and entry-exit relation near planar
turning points, Journal of Diﬀerential Equations, 215 (2005), 225–267.

28 F. Dumortier & C. Rousseau

[DD2] P. De Maesschalck, F. Dumortier, Canard solutions at non-generic turning points,
Transactions of the American Mathematical Society, 358 (2006), 2291–2334.

[DD3] P. De Maesschalck, F. Dumortier, Canard cycles in the presence of slow dynamics
with singularities, Proc. Royal Society of Edinburgh-A, to appear.

[DPR] F. Dumortier, D. Panazzolo and R. Roussarie, More limit cycles than expected in
Li´enard equations, Proc. Amer. Math. Soc. 135 (2007), 1895–1904.

[DR1] F. Dumortier, R. Roussarie, Multiple canard cycles in generalized Li´enard equations,
Journal of Diﬀerential Equations, 174 (2001), 1–29.

[DR2] F. Dumortier, R. Roussarie, Canard cycles with two breaking parameters, Discrete
and Continuous Dynamical Systems, Series A 17, nr4 (2007), 787–806.

[DRR] F. Dumortier, R. Roussarie, and C. Rousseau, Hilbert’s 16-th problem for quadratic
vector ﬁelds, J. Diﬀerential Equations 110 (1994), 86–133.

[R] C. Rousseau, Normal forms, bifurcations and ﬁniteness properties of vector ﬁelds,
in Normal forms, bifurcations and ﬁniteness properties of vector ﬁelds, NATO Sci.
Ser. II Math. Phys. Chem., 137, Kluwer Acad. Publ., Dordrecht, 2004, 431–470.

[RS] R. Roussarie and D. Schlomiuk, On the geometric structure of the class of quadratic
systems, in Qual. Theory Dyn. Syst. 3 (2002), 93–121.

[T] F. Takens, Partially hyperbolic ﬁxed points, Topology 10 (1974), 133–147.
