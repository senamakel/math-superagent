<!-- source: http://www.dms.umontreal.ca/~rousseac/Roussarie_Rousseau.pdf | converted from PDF -->

Finite cyclicity of nilpotent graphics of pp-type
surrounding a center ∗

R. Roussarie, Universit´e de Bourgogne
C. Rousseau, DMS and CRM, Universit´e de Montr´eal

August 2007

Abstract

This paper is part of the DRR-program of [4] to prove the ﬁniteness part of Hilbert’s
16th problem for quadratic vector ﬁelds by showing the ﬁnite cyclicity of 121 graphics.
In this paper we prove the ﬁnite cyclicity of 4 graphics passing through a triple nilpotent
point of elliptic type surrounding a center, namely the graphics (H 1
7 ), (F 1
7a), (H 3
11) and
(I 1
6a). These four graphics are of pp-type, in the sense that they join two parabolic sectors
of the nilpotent point. The exact cyclicity is 2 for (H 1
7 ) and (H 3
11). The graphics (F 1
7a) and
I 1
6a) occur in continuous families. Their exact cyclicity is 2 except for a discrete subset of
such graphics. The method can be applied to most other graphics of the DRR-program
[4] through a triple nilpotent point and surrounding a center.

This paper is dedicated to Freddy Dumortier, our estimated collaborator and dear friend,
with whom we started the DRR-program in 1990.

1 Introduction

In the paper [4], together with Freddy Dumortier we presented a program (called the DRR-
program to prove the ﬁniteness part of Hilbert’s 16th problem. The DRR-program consisted
in the proof of the ﬁnite cyclicity of 121 graphics among the family of quadratic systems.
This paper is a contribution to this program. Indeed we show the ﬁnite cyclicity of the
graphics (H 1
7 ), (F 1
7a), (H 3
11) and (I 1
6a) on the Poincar´e sphere (see Figure 1 and Figure 2 for
the common blow-up of the singularity). These graphics surround a center and for this reason
we call them center graphics.

Deﬁnition 1.1 A graphic of an analytic vector ﬁeld X is called a center graphic if for any
tubular neighborhood W of the graphic, there exists an analytic deformation Xε depending
on a ﬁnite number of parameters such that X0 = X and for each η > 0 there exists ε with
|ε| < η such that Xε has an annulus of periodic solutions inside W .

The corresponding generic graphics (when the system has a focus) have been shown to
have ﬁnite cyclicity in [6]. These graphics are called pp-graphics in [6] and [7], to mean that
they join two parabolic sectors of the nilpotent point of multiplicity three and elliptic type.

∗This work is supported by NSERC in Canada.
 1

2 R. Roussarie & C. Rousseau

(a) The family of graphics (F 1
7a)
ending in the hemicycle (H 1
7 ) (b) The family of graphics (I 1
6a)
ending in the hemicycle (H 3
11)

Figure 1: The families of graphics we study here do not include the inner graphic which is the
only one having a return map. The surrounding circle is the equator of the Poincar´e sphere.

prpl

Figure 2: Common blow-up of the nilpotent singularity

In the paper [7] it is shown that such a graphic has cyclicity ≤ n if it satisﬁes the following
genericity condition: the n-th derivative of the regular transition map along the graphic (see
Figure 3) is nonzero.

Genericity conditions involving higher order derivatives are typical for graphics occurring
in continuous families of graphics, as is the case with the pp-graphics considered here and in
[7] and [6]. The ingredient of the proof was the blow-up of the family unfolding the nilpotent
point. In the paper [6] it was shown that this genericity condition held for the pp-graphics of
the DRR-program for quadratic systems ([4]) when the system was not integrable. We now
show that the Bautin trick can be used to transform the proof of ﬁnite cyclicity in the generic
case into a proof of ﬁnite cyclicity for the similar center pp-graphics. The proof works easily
because the Bautin ideal is radical in the cases considered here. Indeed we can decompose a

Finite cyclicity of nilpotent graphics surrounding a center 3

Σl Σr

(a) A pp-graphic
 Σ
l Σr

(b) The graphic in the blow-up

Figure 3: The regular transition for a pp-graphic

displacement map δε(z) in some center ideal obtaining some form

δε(z) =
 n∑

j=1 ˜εjhj(z, ε) (1.1)

with n ≥ 3, where {˜ε1, ˜ε2, ˜εn} generate the center ideal and the function hj(z, ε) have strictly
increasing order in z at z = z0. For all but a discrete subset of graphics, and also for the
hemicycle graphics (H 1
7 ) and H 3
11), n is equal to 2 yielding an exact cyclicity of 2.
In principle it could be diﬃcult to verify genericity conditions involving higher order
derivatives of regular transitions: indeed the calculations of such higher order derivatives is
quite involved. Moreover the regular transitions are deﬁned on sections parallel to the axes
in normalizing coordinates. The change of coordinates to normalizing coordinates should be
taken into account when calculating these derivatives. In [6] a trick proved in [1] was used
to minimize the calculations, which consisted in remarking that the sections in normalizing
coordinates could be taken analytic and parameterized by analytic coordinates. Thus, as
soon as the regular transition was nonlinear at one point on the section (corresponding to one
graphic), it was nonlinear at all points of the section. It hence suﬃced to verify the genericity
condition near the limit graphic given by the hemicycle, where it followed from the fact that
the hyperbolicity ratios were diﬀerent from 1 and the regular transition along an invariant
line of the limiting graphic formed by the hemicycle had a nonzero second derivative. The
same kind of trick is used in this paper to make the division (1.1), thus allowing to reduce the
calculations to a minimum. More involved calculations with Abelian integrals could permit
to transform the ﬁnite cyclicity argument into an exact cyclicity argument for the center
graphics.
We believe that the same kind of argument should allow to treat the other center graphics
in the DRR-program of [4], once the ﬁnite cyclicity of the corresponding generic graphics is
done (see discussion in Section 8).

2 Normal forms for quadratic families unfolding a graphic
with a triple nilpotent point and surrounding a center

Such a triple nilpotent singular point can be of saddle or elliptic type.

4 R. Roussarie & C. Rousseau

2.1 The case of a nilpotent point in the ﬁnite plane

Proposition 2.1 A quadratic system with a nilpotent point of saddle or elliptic type in the
ﬁnite plane and a point of center type can always be brought to the form

˙x = y + a0x2 − y2

˙y = xy, (2.1)

with a0 ∈ R (see Figure 1(a)). The point is of saddle type if a0 < 0 and of elliptic type if
a0 > 0. The system is part of the stratum of reversible centers.
The case a0 = − 1
2 corresponds to the particular case of a system both Hamiltonian and
reversible.
The case a0 = 1 corresponds to the particular case of a reversible system with a triple
invariant line. Hence it is at the intersection of two strata.
The hemicycle surrounding the center has a return map if a0 ≥ 1
2 . So the graphics (H 1
7 )
and (F 1
7a) correspond to 0 < a0 < 1
2 .

Proof. If a quadratic system has a triple nilpotent point at the origin of saddle or elliptic
type then it has an invariant line which we can always suppose to be the line y = 0. Then
necessarily the linear part has the form y ∂
∂x . Modulo a scaling in x we can suppose that
the second equation has the form ˙y = xy + by2. A change of coordinate X = x + by allows
to bring it to the form ˙y = Xy. Then the singular point is on the line X = 0. A scaling
in y allows to bring the singular point at (0, 1). The system then has the form (calling the
coordinates (x, y)): ˙x = y + a0x2 + cxy − y2

˙y = xy. (2.2)

The divergence vanishes at (0, 1) if and only if c = 0. ✷

Proposition 2.2 In the case a0 ̸= 1 the general (5-parameter) quadratic perturbation of
(2.1) can be brought by an aﬃne change of coordinate and time scaling depending analytically
on the parameters to the form
 ˙x = y + ax2 − y2 + ε4xy + ε1
˙y = xy + ε2 + ε3y, (2.3)

where ε0 = a − a0

is a small parameter.
In the neighborhood of a0 = − 1
2 the system is Hamiltonian under the conditions:





a + 1
2 = 0
ε3 = 0
ε4 = 0,
 (2.4)

and reversible under the conditions: 



ε2 = 0
ε3 = 0
ε4 = 0.
 (2.5)

Finite cyclicity of nilpotent graphics surrounding a center 5

Except in the case a ∈ {0, 1
2 } the ﬁrst integral is given by

H = x−2a (y2 + 2(1 − a)
2a − 1 y + (1 − a)x2 + ε1(1 − a)
a
 ) . (2.6)

Proof. The general quadratic perturbation is of the form

˙x = y + a0x2 − y2 + ∑
0≤i+j≤2 aijxiyj

˙y = xy + ∑
0≤i+j≤2 bijxiyj. (2.7)

We consider a change of coordinate

(x, y) = (X + δ1Y + δ3, δ2X + Y + δ4) (2.8)

for the family, which reduces to the identity for δ1 = δ2 = δ3 = δ4 = 0. Such a change of
coordinates brings (2.7) to the form

˙X = Y + bX 2 − Y 2 + ∑
0≤i+j≤2 AijX iY j
˙Y = XY + ∑
0≤i+j≤2 BijX iY j. (2.9)

We consider the function (δ1, δ2, δ3, δ4, aij, bij) ↦→ (A00, A10, A11, B00, B10, B01, B20, B02). The
Jacobian at aij = bij = 0, namely













 0 0 0 1
0 1 2a0 0
2a0 − 1 −2 0 0
0 0 0 0
0 0 0 1
0 −1 1 0
0 1 − a0 0 0
1 1 0 0
 












 , (2.10)

has rank 4. Hence we can solve any set of 4 equations of the form Aij = 0 or Bij = 0 by the
implicit function theorem, as long as they correspond to 4 linearly independent lines of the
matrix. In particular we can never get rid of the constant term in ˙Y . The X 2 term in ˙Y can
only be removed when a0 ̸= 1, i.e. we have a simple singular point at inﬁnity in the direction
of the X-axis. When a = 1 we have a triple point at inﬁnity in that direction, thus explaining
the obstruction to remove this term. We choose to solve A10 = B10 = B20 = B02 = 0. Using
scalings in (X, Y, t) allows to take A01 = A02 = B11 = 0. ✷

2.2 The case of a nilpotent point at inﬁnity

The diﬀerence with the previous case is that the condition of having a triple nilpotent point
at inﬁnity is of codimension 2, since the equator is invariant.

Proposition 2.3 A quadratic system with a nilpotent point of saddle or elliptic type at in-
ﬁnity, an invariant line and a point of center type can always be brought to the form

˙x = 1 − y + A0x2

˙y = xy, (2.11)

6 R. Roussarie & C. Rousseau

with A0 ∈ R (see Figure 1(b)). The point is of saddle type if A0 > 1 and of elliptic type if
A0 < 1. The system is part of the stratum of reversible centers. When the point is of elliptic
type, the hemicycle surrounding the center has a return map if A0 ≤ 1
2 . So the graphics (H 3
11)
and (I 1
6a) correspond to 1
2 < A0 < 1.

Proof. If a quadratic system has a triple nilpotent point at inﬁnity of saddle or elliptic
type we can always suppose that it is located along the y-axis. We can also suppose that the
other inﬁnite point is along the x-axis, that the invariant line is the line y = 0 and that the
center is above this line. Then necessarily the quadratic part has the form (Ax2 + Bxy) ∂
∂x +
(Cxy + Dy2) ∂
∂y . In order that the singular point at inﬁnity has two zero eigenvalues we get
B = D = 0. It is triple if C ̸= 0. A scaling in x allows to take C = 1 and the system has the
form ˙x = Ax2 + α + βx + γy
˙y = xy + δy. (2.12)

A translation in x allows to bring the center on the y-axis and a scaling in y allows to suppose
it is located at (0, 1). Hence δ = 0 and α = −γ. The divergence vanishes at (0, 1) if β = 0.
As necessarily α ̸= 0 (since otherwise x = 0 is a line of singular points) a simultaneous scaling
in (x, t) allows to take α = 1. ✷

Proposition 2.4 In the case A0 ̸= 1
2 , 1, the general (5-parameter) quadratic perturbation of
(2.11) can be brought by an aﬃne change of coordinate and time scaling depending analytically
on the parameters to the form

˙x = 1 − y + Ax2 + ε1y2 + ε3xy
˙y = xy + ε2 + ε3y2 + ε4y, (2.13)

where A − A0 is a small parameter.
The system is integrable under the condition ε2 = ε3 = ε4 = 0. It has an invariant line
under the condition ε2 = 0. The ﬁrst integral is given by

H(x, y) = y−2A (y + 1 − 2A
2 x
2 + 1 − 2A
2A + ε1 1 − 2A
2(A − 1) y2) . (2.14)

The two parameters (ε1, ε3) unfold the nilpotent point at inﬁnity.

Proof. The general quadratic perturbation is of the form

˙x = 1 − y + Ax2 + ∑
0≤i+j≤2 aijxiyj

˙y = xy + ∑0≤i+j≤2 bijxiyj. (2.15)

We consider a change of coordinate

(x, y) = (X + δ1Y + δ3, δ2X + Y + δ4) (2.16)

for the family, which reduces to the identity for δ1 = δ2 = δ3 = δ4 = 0. Such a change of
coordinates brings (2.15) to the form

˙X = 1 − y + A0x2 + ∑
0≤i+j≤2 AijX iY j
˙Y = XY + ∑0≤i+j≤2 BijX iY j. (2.17)

Finite cyclicity of nilpotent graphics surrounding a center 7

We consider the function (δ1, δ2, δ3, δ4, aij, bij) ↦→ (A10, A11, A02, B00, B10, B01, B20, B02). The
Jacobian at aij = bij = 0, namely













 0 2A0 −1 0
2A0 − 1 0 0 0
0 0 0 0
0 0 −1 0
0 0 0 1
0 1 1 0
0 0 1 − A0 0
1 0 0 0
 












 , (2.18)

has rank 4. We choose to solve A10 = B10 = B20 = A11 − B02 = 0. Using scalings in (X, Y, t)
allows to take A00 = A01 = B11 = 0. ✷

The following calculation will be needed to derive the result.

Lemma 2.5 The family (2.13) localized in the neighborhood of the singular point at inﬁnity
in the direction of the y-axis by means of (v, w) = ( x
y , 1
y ) is given by

˙v = −w + (A − 1)v2 + w2 + ε1 − ε4vw − ε2vw2

˙w = −vw − ε3w − ε4w2 − ε2w3. (2.19)

3 Blowing up

In this section, we want to explain how to blow up the nilpotent singularity p = (0, 0) ∈ R2

for the vector ﬁeld unfolding Xε deﬁned by the diﬀerential equation (2.3).
The parameter set ε = (ε1, ε2, ε3, ε4, ε0), (3.1)

includes the local parameter ε0 = a − a0

where a0 is ﬁxed in ]0, 1
2 [; we will use a as well as ε0 chosen small enough so that a ∈]0, 1
2 [.
We refer to [3] and [9] for the details about this technique. We will discuss in great detail
the case of (2.3) and then give brieﬂy the adjustments for (2.13). For instance we replace
ε0 = a − a0 by ε0 = A − A0 in (3.1).

3.1 The blow-up of the family (2.3)

Taking into account the quasi-homogeneity properties of (2.3), it is natural to choose the
following formula for the blowing up :

ε1 = ν2 ¯ε1, ε2 = ν3 ¯ε2, ε3 = ν ¯ε3 (3.2)

and also: x = r¯x, y = r2 ¯y, ν = rρ. (3.3)

Here, ¯ε = (¯ε1, ¯ε2, ¯ε3) ∈ S2
P A ≈ S2, (3.4)

8 R. Roussarie & C. Rousseau

where S2
P A ≈ S2 is a parameter-sphere (i.e. {¯ε2
1 + ¯ε2
2 + ¯ε2
3 = 1}), (¯x, ¯y, ρ) ∈ S2
P H ≈ S2, a phase-
sphere (i.e. {¯x2+y2+ρ2 = 1}) and ν is a small positive parameter (we will write: ν ∈ (R+, 0)).
Let us notice that we do not blow up the parameters ε4, ε0 ∈ (R, 0). As a consequence, the
blown-up space E is a neighborhood of the 4-dimensional manifold S2
P H × S2
P A × {(0, 0)}
in S2
P H × S2
P A × R+ × R2. We will denote by π : E → R7, the blowing-up map deﬁned
by the formulas (3.2), (3.3) and {ε4 = ε4, ε0 = ε0}. This map π has a phase-component
πP H : (¯x, ¯y, r) → (x, y) and a parameter-component πP : (¯ε1, ¯ε2, ¯ε3, ε4, ε0, r, ρ) → ε. We
deﬁne the blown-up vector ﬁeld ¯X = 1
ν ˆX , where ˆX is the lift of the family Xε (considered as
a vector ﬁeld in R7), in the blown-up space E.

Let us consider one limit periodic set Γ of X0, of type (F 1
7a), that we want to study. Γ
is union of the singular point p with a regular orbit which has p as ω and α limits. This
type of limit periodic set is called a graphic. In the case of a limit periodic set of type (H 1
7 ),
the regular orbit is replaced by the union of three regular orbits and two opposite saddle
points on the equator. One regular orbit is given by the upper half of the equator, while
the two others are given by the positive and negative x-axis. Let Σl = {−X} × [−Y, Y ] and
Σr = {X} × [−Y, Y ]. We choose X > 0, Y > 0 such that Σl, Σr are sections transverse to Γ
and contained in π(E). Let y0 ∈] − Y, Y [ be the point which corresponds to the intersection of
Γ with Σl (or Σr by symmetry). We will denote by y → Rε(y) the transition map of Xε from
Σl to Σr following the ﬂow backwards. This map is deﬁned on [−Y0, Y0] where 0 < Y0 < Y
and ε is near 0. We will denote by y → Tε(y) the transition map of Xε from Σl to Σr following
the ﬂow forwards. This map is not always deﬁned. For instance some singular points can be
in the way and forbid the transition. Also, due to a strong deviation, all orbits from points
in Σl may arrive below or above Σr.
 p
rpl

Figure 4: The critical locus {rρ = 0} in the blow-up

Recall that for each ¯ε ∈ S2 the critical locus C¯ε (Figure 4) is the union of a half-sphere
HS¯ε ⊂ S2
P H × {¯ε}, corresponding to ρ ≥ 0, and of the 2-dimensional blown-up space P H of
the phase space, which is parameterized by ((¯x, ¯y), ρ) ∈ S1 × R+. These two parts are glued
along their boundaries, deﬁned in each of them by {ρ = 0}. To obtain the cyclicity of Γ we
have to consider all the graphics of the blown-up ﬁeld ¯X which exist in E and are blown
down in Γ (this means that they are sent onto Γ by the map π). Such a graphic exists in
C¯ε if a regular orbit γ¯ε connects in HS¯ε the point pl = ((−1, 0), 0) ∈ S1 × R+ with the point
pr = ((1, 0), 0) ∈ S1 × R+. We see below that this is the case for ¯ε2 = 0. We also have the
limit cases where there is an additional saddle-node on γ¯ε.
To study this connection γ¯ε we work in the parameter directional chart deﬁned by {ρ = 1}.
In this chart r ≡ ν, and we will use this parameter ν. Also in this chart one chooses (¯x, ¯y) ∈ ¯D,
with ¯D an arbitrarily large disk, (¯ε1, ¯ε3) ∈ S1 and ε2, ε4, ε0, ν near 0. As a consequence, the

Finite cyclicity of nilpotent graphics surrounding a center 9

blown-up ﬁeld is given in this chart by a vector ﬁeld family ¯X¯λ in the phase space ¯D and
parameter: ¯λ = ((¯ε1, ¯ε3), ¯ε2, ε4, ε0, ν) ∈ S1 × (R, 0)
3 × (R+, 0). (3.5)

This vector ﬁeld family ¯X¯λ is given by:

˙¯x = ¯y + (a0 + ε0)¯x2 + ¯ε1 −ν2 ¯y2 + νε4 ¯x¯y
˙¯y = ¯x¯y + ¯ε3 ¯y +¯ε2, (3.6)

where we have pushed on the right the perturbative terms.
If ¯ε2 = 0, the axis {¯y = 0} is invariant. Moreover, for ¯ε1 = 0, the vector ﬁeld ¯X(¯ε,0,0)
has a saddle-node singular point at (¯x, ¯y) = (0, 0) which bifurcates into two singular points
for ¯ε1 < 0. On the contrary, one has a connection from pl and pr when ¯ε2 = 0 and ¯ε1 > 0
(the points pl, pr are located on the circle at inﬁnity in the phase plane (¯x, ¯y)). Inversely, if
¯ε2 ̸= 0, the ﬁeld is transverse to the axis {¯y = 0}. This prevents the possibility of a connection
between pl, pr for ¯ε1 < 0 or ¯ε2 ̸= 0. Finally, a connection exists if and only if ¯ε2 = 0 and
¯ε1 > 0. But we need also study the limiting case ¯ε1 = 0 which can (and does) create limit
cycles by perturbation.
As we are interested to the bifurcation of limit cycles, we will restrict (¯ε1, ¯ε3) to the interval
E = {(¯ε1, ¯ε3) ∈ S1 | ¯ε1 ≥ 0} ⊂ S1 and we will call its interior E = {(¯ε1, ¯ε3) ∈ S1 | ¯ε1 > 0} ⊂ S1.
E (resp. E) is parameterized by ¯ε3 ∈ [−1, +1] (resp. ¯ε3 ∈] − 1, +1[), which we will identify
with E (resp. E). Along E and E, ¯ε1 is function of ¯ε3: ¯ε1(¯ε3) = √
1 − ¯ε2
3. We will also write

¯µ = (¯ε3, ¯ε2, ε4) ∈ E × (R, 0) × (R, 0) (3.7)

and we will identify ¯λ with (¯µ, ε0, ν) in E × (R, 0)3 × (R+, 0). For convenience we will also
introduce the parameter
 µ = (¯µ, ε0) = (¯ε3, ¯ε2, ε4, ε0) ∈ E × (R, 0)
3. (3.8)

We will note γ(¯ε1(¯ε3),0,¯ε3) by γ¯ε3. For each ¯ε3 ∈ E, a unique limit periodic set Γ¯ε3 is then
deﬁned in C(¯ε1(¯ε3),0,¯ε3) : Γ¯ε3 = ˜Γ ∪ γ¯ε3, where ˜Γ which connects pl and pr in P H, is the strict
lift of Γ by the blowing-up.

To study the transition above γ¯ε3, one chooses two sections Σ′
l = {− ¯X} × [− ¯Y , ¯Y ] and
Σ′
r = { ¯X} × [− ¯Y , ¯Y ], transverse to ¯X¯λ for ¯ε2 = 0 with a constant ¯X taken large enough.
Now, for ¯ε1 > 0 and ¯ε2, ε4, ε0, ν small enough, a regular transition map ¯T¯λ(¯y) along the ﬂow
of ¯X¯λ, is deﬁned from a subsection Σ′′
l ⊂ Σ′
l into Σ′
r (one can choose Σ′′
l = {− ¯X} × [− ˜Y , ˜Y ]
for some ˜Y < ¯Y ).
Now, taking ˜Y , ¯Y large enough, one can deﬁne a transition map Dl
¯λ(y) : Σl → Σ′
l along
the ﬂow of ¯X¯λ near pl and a transition map Dr
¯λ(y) : Σr → Σ′
r along the ﬂow of − ¯X¯λ near pr.
The transition map Tε = TπP (¯λ) is then given as the composition: Tε = (Dr
¯λ)−1 ◦ ¯T¯λ ◦ Dl
¯λ. We
will see that the natural parameter for studying the ﬁnite cyclicity is ¯λ rather than ε. So we
want to consider Tε as a function of ¯λ and by abuse of notation we will use the same notation
Tε = T¯λ. In the next section we will use this composition to obtain a good presentation of
T¯λ.

Remark 3.1 There exist three limit periodic sets in the blown-up vector ﬁeld corresponding
to

10 R. Roussarie & C. Rousseau

(i) ¯ε2 = 0, ε1 > 0;

(ii) ¯ε1 = ¯ε2 = 0, ¯ε3 = +1;

(iii) ¯ε1 = ¯ε2 = 0, ¯ε3 = −1.

The graphics in π−1(Γ) ⊂ E are the graphics Γ¯ε3 for ¯ε3 ∈ [−1, +1]. As a consequence, one
has that: Cycl(Xε, Γ) = Sup{Cycl( ¯X , Γ¯ε3) | ¯ε3 ∈ [−1, +1]} (3.9)

Then, to prove the ﬁnite cyclicity of our graphic we need to prove the ﬁnite cyclicity of
each of these limit periodic sets. The limit periodic sets (ii) and (iii) have been shown in [7]
to have cyclicity 1. The proof of [7] made no use of the genericity condition and is still valid
here. So we only need to study the ﬁnite cyclicity of a graphic of type (i).

3.2 The blow-up of (2.13).

We consider here the blow-up of the family unfolding the nilpotent singular point. The family
(2.13) localized at this point appears in (2.19). Here, only the parameters ε1 and ε3 unfold
the nilpotent singularity. So they are the only parameters we blow-up. We replace (3.2) by

ε1 = ν2 ¯ε1, ε3 = ν ¯ε3. (3.10)

As the nilpotent point appears at inﬁnity the phase variables are now (v, z) in (2.19) we let

v = r¯v, w = r2 ¯w, ν = rρ. (3.11)

4 Presentation of the transition maps for the graphics (F 1
7a)
and (H 1
7 )

In this section, we will restrict to (¯ε1, ¯ε3) ∈ S1 with ¯ε1 > 0, which, because of Remark 3.1, is
the only case to discuss. We can parameterize this arc of circle E by ¯ε3 ∈] − 1, +1[ and we
will consider ¯ε1 as a function of ¯ε3 : ¯ε1(¯ε3) = √1 − ¯ε2
3.

4.1 Presentation of ¯T¯λ for the graphic (F 1
7a)

This maps goes from a section Σl = {¯x = − ¯X} to the symmetric section Σr = {¯x = ¯X} over
the blow-up sphere in the family chart ρ = 1.

Proposition 4.1 For ¯ε3 ∈ E the transition map ¯T¯λ is analytic in (¯y, ¯λ) and has the following
presentation:

¯T¯λ(¯y) = ¯y + α(¯λ) + β(¯λ)¯y + ¯y2(¯ε2Φ2(¯y, ¯λ) + ¯ε3Φ3(¯y, ¯λ) + νε4Φ4(¯y, ¯λ)) (4.1)

with α(¯λ) = c2(¯λ)¯ε2, β(¯λ) = c3(¯λ) ¯ε3√¯ε1 +O(¯ε2). The function c2 is analytic and strictly positive

in E × (R, 0)3 × (R+, 0) and the function c3 is analytic and strictly positive in ¯E × (R, 0)3 ×
(R+, 0) (in particular it is strictly positive and analytic at ¯ε3 = ±1).

Finite cyclicity of nilpotent graphics surrounding a center 11

Proof. Let us ﬁx (¯ε1, ¯ε3) ∈ E as above. We observe that the term νε4 enters as a parameter
in the equation (3.6). Moreover the phase portrait of (3.6) is invariant by the symmetry
(¯x, ¯y) → (−¯x, ¯y) when ¯ε2 = ¯ε3 = νε4 = 0. As the sections Σ′
l and Σ′
r are exchanged by this
symmetry, one has that ¯T¯λ(¯y) ≡ ¯y when ¯ε2 = ¯ε3 = νε4 = 0. It follows that ¯T¯λ(¯y) has the
form (4.1) with α, β in the ideal generated by: ¯ε2, ¯ε3, νε4.
We now proceed to obtain more information about α and β. Recall {¯y} = 0 is an orbit of
¯X¯λ when ¯ε2 = 0. Along this orbit the diﬀerential equation reduces to

˙¯x = a¯x
2 + ¯ε1. (4.2)

It follows that the time to go from − ¯X to some value ¯x ∈ [− ¯X, ¯X] is equal to:

t(¯x) = 1
√a¯ε1
 (
arctan (√ a
¯ε1 ¯x
) + arctan (√ a
¯ε1 ¯X))

and if ¯x(t) is the inverse function of t(¯x), g(t) = (¯x(t), 0) is the trajectory with initial condition
¯x(0) = − ¯X, ¯y(0) = 0, when ¯ε2 = 0. Let us notice that g(t) is in fact a trajectory of ¯X¯λ as soon
as ¯ε2 = 0 (for any value of ¯ε3, ν, ε4). It follows that α is divisible by ¯ε2 : α(¯λ) = c2(¯λ)¯ε2, for
an analytic function c2. We must show that c2(¯λ) > 0. Now, for ν = 0, the ¯ε2-derivative ∇(t)
of the ¯y-component of the ﬂow of (3.6) at the time t, in the neighborhood of the trajectory
g(t), veriﬁes the diﬀerential equation d
dt ∇ = (¯x(t) + ¯ε3)∇(t) + 1 with ∇(0) = 0. It follows
easily by integration of the diﬀerential equation that ∇(t) > 0 for any t > 0 and then that
c2|{¯ε2=0} = ∇(t( ¯X)) > 0. Then c2(¯λ) > 0.

The coeﬃcient β(¯λ) is equal to the derivative d ¯T¯λ
d¯y (0) − 1. For ¯ε2 = 0, one has:

d ¯T¯λ
d¯y (0) = exp ∫ + ¯X

− ¯X div( ¯X¯λ)dt = exp ∫ + ¯X

− ¯X
 2a¯x + ¯x + ¯ε3
a¯x2 + ¯ε1 d¯x.

The integral reduces to

∫ + ¯X

− ¯X
 ¯ε3
a¯x2 + ¯ε1 d¯x = ¯ε3√¯ε1
 ∫ ¯X√¯ε1

− ¯X√¯ε1
 dξ
aξ2 + 1 = c ¯ε3√¯ε1 (1 + O(
√¯ε1)),

for some constant c > 0. Finally we have that d ¯T¯λ
d¯y (0) = exp c ¯ε3√¯ε1 (1 + O(
√¯ε1)). This implies

that β(¯λ) is divisible by ¯ε3 when ¯ε2 = 0. As a consequence one has that β(¯λ) = c3(¯λ) ¯ε3√¯ε1 +
O(¯ε2) with a function c3 as in the statement. It is possible to show that c3 is bounded and
bounded away from 0 in the neighborhood of ¯ε3 = ±1. We do not write the details since the
study of the ﬁnite cyclicity in the neighborhood of ¯ε3 = ±1 is covered by Remark 3.1. ✷

4.2 Presentation of the Dulac transitions near the points pl and pr

These transitions are commonly called Dulac maps in the literature: see Figure 5 for a Dulac
map near pl.
For i = l, r, the singular point pi is located in a phase-directional chart deﬁned by ¯x = ±1
(−1 for i = l and +1 for i = r). In these charts the blown-up ﬁeld ¯X is a family of vector ﬁelds
¯Xµ deﬁned in a neighborhood of 0 ∈ R3 with coordinates (¯y, ρ, r) and parameter deﬁned in
(3.8). (The diﬀerence with ¯λ is that now ν is a variable instead of a parameter. Recall that

12 R. Roussarie & C. Rousseau

(ν,y)
 (ν,D(y))D(y))D(y))

r
 ρ

y
 Σ
 Σ'

Figure 5: A Dulac map

E =] − 1, +1[ and that ¯ε1 = √
1 − ¯ε2
3.) We have integrability through symmetry precisely
when ¯µ = 0 with ¯µ given in (3.7). In this subsection we will rely heavily on the paper [7],
some results of which we recall. First, we recall that the point pi is a saddle point with
eigenvalues {−1, +1, −σ(a)}, where
 σ(a) = 1 − 2a
a (4.3)

and we recall that the graphic occurs for σ(a) > 0.
In the chart, we consider sections ¯Σi given by ρ = ρ0 and sections ¯Σ′
i given by r = r0,
where ρ0, r0 are multiples of the above constants X, ¯X (this will be discussed in more details
below). Also in the chart, ν appears as a ﬁrst integral: ν = rρ. In the neighborhood of pi the
natural coordinates are (r, ρ, ¯y). When ¯x = ±1, modulo a time scaling the system is given by

˙r = ±r
˙ρ = ∓ρ
˙¯y = ± (1−2a)¯y−2¯y2±¯ε3ρ¯y−2ε1ρ2 ¯y∓2ε4r ¯y2+2r2 ¯y3±¯ε2ρ3

a+¯y−r2 ¯y2±ε4r ¯y+ρ2 ¯ε1 . (4.4)

Each section is naturally parameterized by (ν, ¯y). With these coordinates the transition from
¯Σi to ¯Σ′
i takes the special form (ν, ¯y) ↦→ (ν, Di
µ(¯y, ν)). By abuse of notation, we will forget
the ﬁrst coordinate, so ν becomes a parameter for the second coordinate and for each value
ν, we will denote by Di
¯λ(¯y) the transition from ¯Σi to ¯Σ′
i (when i = r the transition follows
the ﬂow backwards.) The graphic of ¯Xµ we want to consider cuts Σi at the value ¯y = ¯yi
0. It
depends only on ε4 and ε0 (since the graphic is located in the plane r = 0).
The point pi corresponds to (r, ρ, ¯y) = (0, 0, 0) in (4.4). It is possible to bring (4.4) to
normal form in the neighborhood of this point. Because of the form of the system, the
normalizing change of coordinates to normal form has the simple form

ˆyi = ¯y + o(|r, ρ, θ|).

Finite cyclicity of nilpotent graphics surrounding a center 13

Hence it is remarkable that the sections ¯Σi and ¯Σ′
i above are parallel to the coordinate planes
in the normalizing coordinate system. In the normalizing coordinate system the transition
map is given by ˆD¯λ(ˆyi). Its special form is well described in [7]. In particular it is linear in
the case σ(a0) /∈ Q:
 ˆDi
¯λ(ˆyi) = ( ν
ν0
 )¯σi ˆyi, (4.5)

and all the intuition can be built on this case. This form comes from the fact that a C N (K)

normal form is given by ˙r = ±r
˙ρ = ∓ρ
˙ˆy = ±ˆy( 1−2a
a + ∑K
j=1 γi
jνi)
, (4.6)

since all resonances involve powers of ν = rρ. We have that N (K) → +∞ when K → ∞ and
then N (K) can be chosen arbitrarily large, but the neighborhood on which we can use (4.6)
shrinks with K. Then
 ¯σi = 1 − 2a
a +
 K∑

j=1 γi
jνi.

Additional resonant terms have to be added in the case σ(a0) = p
q . The computation of the
Dulac map involves a compensator with parameter of the form

α
i
1 = p − ¯σiq

which is a smooth function of (µ, ν) (details in [7]). Also in the particular case a0 ∈ N there is
in general an additional constant term coming from the existence of a resonant term between
r and ˆy. However this term does not exist in our family (4.4). This comes from the fact that
we have been able to remove all pure terms in x in the ˙y term of (2.3).

Notation 4.2 1. The symbol OP (¯µ) where ¯µ has been deﬁned in (3.7) refers to a function
in the parameter ¯λ, belonging to the ideal generated by ¯ε2, ¯ε3, ε4. Such a function is
expressed as a combination: ¯ε2Φ2(µ, ν) + ¯ε3Φ3(µ, ν) + ε4Φ4(µ, ν).

2. The symbol OG(¯µ) will denote a function of (z, ¯λ) also in the ideal generated by ¯ε2, ¯ε3, ε4,
but in the space of functions of (z, ¯λ). Such a function is expressed as a combination:
¯ε2Φ2(z, µ, ν) + ¯ε3Φ3(z, µ, ν) + ε4Φ4(z, µ, ν).

3. ω is the compensator deﬁned for z > 0 by:

ω(z, α) =
 { zα−1
α α ̸= 0
ln z α = 0.

Summing all the results for D, introducing the variable z = ˆyi − ˆyi
0 and keeping the same
letter ˆDµ,ν for the transition written in the z-coordinate we get:

Proposition 4.3 For any a0 ∈ (0, 1
2 ) (rational or not) the map ˆDi
¯λ has the form

ˆDi
¯λ(z) = ˆηi(¯λ
) + ( ν
ν0
 )¯σi [z + ˆφ
i(z, µ, ν, ω( ν
ν0 , −α
i
1))]. (4.7)

14 R. Roussarie & C. Rousseau

In (4.7) ¯σi is a function of the parameter ¯λ = (µ, ν) of the form

¯σi(¯λ
) = σ(a) + OP (¯µ). (4.8)

The function ˆφ is C ∞. Letting ν0 = r0ρ0, one has that

ˆηi(¯λ
) = ˆyi
0( ν
ν0
 )¯σi (4.9)

When σ(a0) ̸∈ Q, we have ˆφi ≡ 0 yielding the particular case (4.5).

Proof. The formula (4.7) comes from [7]. (4.8) comes from the integrability of pi when
¯µ = 0.
The simple form of ˆη in (4.9) comes from the special form of (4.6). In general, when
σ(a0) = p ∈ N, then we could have one resonant term of the form rp, which yields to the
more complicated form of ˆη described in [7]. This term does not appear in (4.6) which comes
from the blow-up of a family of quadratic systems. ✷

Let us deﬁne the function

ˆϕ
i(z, µ, ν) = ˆφ
i(
z, µ, ν, ω( ν
ν0 , −α
i
1))
. (4.10)

There exists τ > 0 such that each partial derivative of ˆϕi in the variables z, ¯ε3, ¯ε2, ε4, ε0 is
O(ντ ). The function ˆϕi is ν-regularly smooth in (z, µ) in the following sense:

Deﬁnition 4.4 A function f (u, ν) deﬁned for (u, ν) ∈ Rk × R+ is ν-regularly smooth in u
if all the partial derivatives of f in u exist and are continuous in ν (including at the value
ν = 0).

Remark 4.5 (i) Let f (u, ν) be a function, ν-regularly smooth in u. If there exists some
τ > 0 such that each partial derivative of f in u is divisible by ντ , it is clear that we
can write f (u, ν) = ντ ˜f (u, ν) with a function ˜f which is also ν-regularly smooth in u.

(ii) If the function f (u, ν) is ν-regularly smooth in u and f (u, ν) = 0 when u1 = · · · = uj = 0,
for some j: 1 ≤ j ≤ k, then we can write f (u, ν) = ∑j
i=1 uifi(u, ν), with factor functions
fi which are ν-regularly smooth in u. This can be proved by using a Taylor formula
with an integral remainder.

Lemma 4.6 In the family (2.3) there exists τ > 0 such that ˆϕi(z, µ, ν) deﬁned in (4.10)
always has the form ˆϕ
i(z, µ, ν) = ντ OG(¯µ), (4.11)

and the factors in the ideal decomposition are ν-regularly smooth in (z, µ).

Proof. The singular point pi is integrable for ¯µ = 0: this is a direct consequence of the form
of (2.6). So ϕ|¯µ=0 ≡ 0. It is proved in Theorem 4.10 of [7] that all partial derivatives of the
functions ˆϕi, in terms of z and the parameter µ are O(ντ ) for some τ > 0. Then, using the
Remark 4.5 for the division by ντ and next for the ideal decomposition in the ¯µ-coordinates,
we obtain (4.11). ✷

Finite cyclicity of nilpotent graphics surrounding a center 15

Now, an important remark is the symmetry that we have already noticed in the parameter-
directional chart and which extends at the boundary to give the following symmetry property
between the two phase-directional charts: for ¯µ = 0, one has that ( ¯X0, pr) = −( ¯X0, pl). In
fact, it was already established in [6], equation (4.10), page 349 that:

¯σr(¯λ
) = ¯σl(¯λ
) + νOP (¯µ), α
r
1(¯λ
) = α
l
1(¯λ
) + νOP (¯µ). (4.12)

We use these equations (4.12) to obtain further division properties by a power of ν:

Proposition 4.7 There exists τ > 0 such that:

ˆηr(¯λ
) − ˆηl(¯λ
) = ντ ˆΞ
(¯λ
) = ντ OP (¯µ), (4.13)

and ˆΞ
(¯λ
) is ν-regularly smooth in µ and belongs to the ideal generated by ¯ε2, ¯ε3, ε4.

Proof. The divisibility by a power of ντ with τ any positive real number strictly less than
σ(a) is obvious yielding (ˆηr − ˆηl)(¯λ) = ντ ˆΞ(¯λ). We can decompose

ˆηr(¯λ
) − ˆηl(¯λ
) = ˆyl
0(( ν
ν0
 )¯σr − ( ν
ν0
 )¯σl) + (ˆyr
0 − ˆyl
0)
( ν
ν0
 )¯σr .

Now, we have:

( ν
ν0
 )¯σr − ( ν
ν0
 )¯σl = ( ν
ν0
 )¯σr (( ν
ν0
 )νOP (¯µ) − 1
) = ( ν
ν0
 )¯σr (
1 + ν log( ν
ν0
 )OP (¯µ)
)
. (4.14)

The fact that ˆΞ is ν-regularly smooth in µ follows directly from (4.14). Now, as a consequence
of ˆyr
0 − ˆyl
0 = OP (¯µ), we have that ˆΞ(µ, ν) = OP (¯µ). ✷

Passing form ˆDi
¯λ to Di
¯λ.
The ﬁrst remark we can make is that we work in the charts: ¯x = ±1. Hence we can always
take r0 = ±X, i.e. Σi = ¯Σi. Similarly we can take ρ0 = ± ¯X0, i.e. Σ′
i = ¯Σ′
i. So the only
change is the parametrization of the sections. The sections Σi and Σ′
i are parameterized by
¯y, while the sections ¯Σ1 and ¯Σ′
i are parameterized by ˆyi, and the changes ¯y ↦→ ˆyi = hi
µ(¯y, r, ρ)
are C N (K) diﬀeomorphisms for some N (K) larger than the order of the graphic to be deﬁned
below in Deﬁnition 4.11.
Because of the symmetry we also have that

h
r
µ(¯y, r, ρ) − h
l
µ(¯y, r, ρ) = OG(¯µ).

This gives us for the maps Di
¯λ(z)

Proposition 4.8 The maps Di
¯λ(z) have the form

Di
¯λ(z) = ξi(¯λ
) + ( ν
ν0
 )¯σi[z + ψi(
z, ¯λ)
))], (4.15)

where {
ξl − ξr = ντ OP (¯µ)
ψi = ντ OG(¯µ),

and the functions ξi (resp. ψi) is ν-regularly smooth in µ (resp. (z, µ)).

16 R. Roussarie & C. Rousseau

We will go further and expand ψi as

ψi(z, ¯λ) = b
i
0(¯λ) + b
i
1(¯λ)z + z2gi(z, ¯λ).

Then necessarily bi
0(¯λ) = ντ OP (¯µ), bi
1(¯λ) = ντ OP (¯µ) and gi(z, ¯λ) = ντ OG(¯µ).
This gives us the ﬁnal form for the maps Di
¯λ(z)

Proposition 4.9 The maps Di
¯λ(z) have the form

Di
¯λ(z) = ηi(¯λ
) + ( ν
ν0
 )¯σi[c
i(¯λ)z + ϕ
i(
z, ¯λ)
))], (4.16)

where 




ηl − ηr = ντ OP (¯µ)
ϕi = ντ OG(¯µ)O(z2)
ci(¯λ) = 1 + OP (¯µ),

and the functions ηi, ci (resp. ϕi) are ν-regularly smooth in µ (resp. (z, µ)).

4.3 Presentation of the regular transition Rε

Let us recall that the regular transition goes from Σl to Σr following the ﬂow backwards. As
the vector ﬁeld Xε has a symmetric phase diagram for ε2 = ε3 = ε4 = 0 one has that:

Rε(y) = R(y, ε) = y + ε2R2(y, ε) + ε3R3(y, ε) + ε4R4(y, ε)

where the Ri are analytic functions of (y, ε). Moreover we can prove:

Proposition 4.10 The function y → R4(y, 0) is not aﬃne, or in other words ∂2R4
∂y2 (y, 0) ̸≡ 0.
As a consequence, for each y0, there exists a minimum integer k = k(y0), 2 ≤ k < +∞ such
that ∂kR4
∂yk (y0, 0) ̸= 0. Moreover for all y0 except a discrete subset we have k(y0) = 2.

Proof. From the deﬁnition of Σi, i ∈ {r, l} it is clear that R is analytic in (y, ε). It is shown
in [6] (which studies the generic case) that ∂2R
∂y2 (y0, ε) ̸= 0 for ε2 = ε3 = 0 and ε4 ̸= 0 and y0
small. Indeed y0 = 0 corresponds to the hemicycle. So it is possible to consider the expansion
of R along the hemicycle. The calculation of this expansion makes use of the fact that the
hyperbolicity ratio of the right (resp. left) saddle at inﬁnity on the hemicycle is sr ∈ (0, 1)
(resp. sl = 1
sr > 1) and that the regular transition along the upper half of the equator has
a nonzero second derivative (see also the discussion of the hemicycle in Section 4.5 below).
Consequently R4(y, 0) = ∂R
∂ε4 (y, 0) is a nonlinear analytic map in y. In particular for each y0
there exists k ≥ 2 such that ∂kR4
∂yk (y0, 0) ̸= 0. Moreover, except on a discrete subset we have
k(y0) = 2. ✷

Deﬁnition 4.11 If Γ is the graphic passing through y0 ∈ Σl, we call order of Γ and denote
by ord(Γ) the integer k(y0) given by Proposition 4.10.

Finite cyclicity of nilpotent graphics surrounding a center 17

Now, when we consider the displacement map from Σl to Σr we will consider it as a
function of y = y
r2
0 . As this change is linear it preserves the nonlinearity properties of R. We
introduce the local coordinate z = ¯y − ¯y0.

Notation. Using the blowing up formulas (3.2) we can use the parameter ¯λ = (µ, ν) as the
parameter of R, as well as the variable z. By abuse of notation we will use the same letters
R (or R¯λ) and the Ri for the expression of R in the z coordinate and parameter ¯λ.

We have:

Corollary 4.12 The expression of the regular transition from Σl to Σr following the ﬂow
backwards is given by

R¯λ(z) = R(z, ¯λ) = z + ν3 ¯ε2R2(z, ¯λ) + ν ¯ε3R3(z, ¯λ) + ε4R4(z, ¯λ). (4.17)

The functions Ri are analytic and the functions Ri(z, (µ, 0)) are independent of ¯µ. Moreover
∂kR4
∂yk (0, 0) ̸= 0, with k = ord(Γ), is the ﬁrst non zero derivative of R4 of order k ≥ 2.

4.4 Change of parametrization on Σ
′
i

We used the same letter ¯y for the ¯y-coordinate when we calculated Di
¯λ and ¯T¯λ. This is an
abuse of notation as we calculate Di
¯λ in the chart ¯x = ±1 and we compute ¯T¯λ in the chart
ρ = 1. The change from one to the other is a positive constant bounded and bounded away
from zero. Moreover the constant depends only on ¯X, so it is the same on the left and on
the right. This justiﬁes a posteriori the abuse of notation.

4.5 Presentation of the transition R¯λ for the graphic (H 1
7 )

In the case of the graphic (H 1
7 ) there are two additional saddles Pl and Pr on the graphic,
so the map R¯λ is no longer regular at ¯y0 = 0. Fortunately the connection between the two
saddles is ﬁxed allowing a nice expansion for R¯λ. All necessary calculations on the form of
R¯λ have been done in [6] in the generic case ε4 ̸= 0. They are still valid here with ε4 replacing
the nonzero coeﬃcient of the xy-term in the ﬁrst equation of (2.3). Let us discuss them.
As in the previous case the center case corresponds precisely to the case where there is
symmetry with respect to the y-axis.
To calculate R¯λ let us look at Figure 6.
It is necessary to take two additional sections Πi and Π′
i in the neighborhood of each
singular point at inﬁnity Pi, i = l, r. These sections should be taken parallel to the coordinate
axes in the normalizing coordinates near Pl and Pr. The hyperbolicity ratios at Pr and Pl are
given by sr and sl = 1
sr with sr < 1. The transition map R¯λ (following the ﬂow backwards)
is given by (to simplify, we do not write the dependence of all intermediate maps on ¯λ)

R¯λ = (Sr)
−1 ◦ (∆r)
−1 ◦ (Sinf )
−1 ◦ (∆l)
−1 ◦ (Sl)
−1.

The functions Sl, Sr and Sinf are C N (K) regular transitions. The Dulac maps ∆i are given
by {
(∆l)−1(u) = u
 1
sl (1 + Ψl(ε, u))

(∆r)−1(u) = u 1
sr (1 + Ψr(ε, u)) (4.18)

18 R. Roussarie & C. Rousseau

Sr

Σl ΠrΠl
 Πr'Πl'
 Σr

Sl
 S
inf
 ∆r∆l

Figure 6: The sections for the graphic (H 1
7 )

where the functions Ψi have the property (I) of Mourtada deﬁned below in Deﬁnition 4.14,
which implies ∂j(∆l)−1

∂uj = ∗u
 1
si −j(1 + ˆΨi(¯λ, u)) (4.19)

for ∗ a nonzero constant and ˆΨi(ε, u) = O(u), all this holding uniformly in ε for ε in a
neighborhood of the origin. We also have

∆r(u) = u
 1
sl (1 + Φr(ε, u))

with Φr of class (I) and moreover Ψl(ε, u) − Φr(ε, u) = OG(¯µ).
We will need the expression of R¯λ in the variable ¯y = y
r2
0 , By abuse of notation we keep

the same letter R¯λ and we switch to the parameter ¯λ.
We have Sl(y) = ε2ξ1(¯λ) + S(y) with S(y) = O(y) a C N (K)-diﬀeomorphism, so that

(Sl)−1(y) = S−1(y − ε2ξ1(¯λ))

= S−1(r2
0(¯y − ε2 ξ1(¯λ)
r2
0 ))

= S−1(r2
0(¯y − ε2ξ(¯λ)
)),

with ξ(¯λ) = ξ1(¯λ)
r2
0 .

The form of the transition map R¯λ is best given in the variable ˇy = ¯y − ε2ξ(¯λ) = (ζ¯λ)−1(¯y)
with image in the variable ¯y. It is given by

ˇR(ˇy) = ˇy + νC1(¯λ)ˇy + ˇy1+sr (
ν3 ¯ε2ψ2(¯λ, ˇy) + ν ¯ε3ψ3(¯λ, ˇy) + ε4ψ4(¯λ, ˇy)
) (4.20)

where ˇR(˜y) − ˇy = OG(¯µ) has the property (I) of Mourtada, (implying C1(¯λ) = OP (¯µ)) and
moreover ψ4(0, 0) ̸= 0. This last property comes from the fact that Sinf − id = OG(µ) and

the direct calculation ∂3Sinf
∂u2∂ε4 ̸= 0 following from [6].
We have proved

Proposition 4.13 There exists τ > 0 such that the transition map R¯λ in ¯y-coordinate,
composed with the translation

¯y = ζ¯λ(ˇy) = ˇy + ε2ξ(¯λ) = ˇy + ντ OP (¯µ) (4.21)

Finite cyclicity of nilpotent graphics surrounding a center 19

has the form ˇR¯λ(ˇy) = ˇy + ντ OG(¯µ) + ε4Ψ4(¯λ, ˇy) (4.22)

where Ψ4(ˇy) = c1(¯λ)ˇy + c2(¯λ)ˇy1+sr (1 + ψ(¯λ, ˇy)),

c2(0) ̸= 0 and ψ has the property (I) deﬁned in Deﬁnition 4.14, for some N . (N can be
chosen arbitrarily large provided the sections Πi and Π′
i are chosen suﬃciently close to the
singular points Pi.)

Deﬁnition 4.14 A function Ψ(ε, u) has the property (I) of Mourtada if Ψ is C N for some
N on W ×]0, u0[, where W is some neighborhood of the origin in ε-space and if there exists
some neighborhood W ′ of the origin in ε-space such that, for all 0 ≤ j ≤ N ,

lim
u→0 u
j ∂jΨ
∂uj = 0

uniformly for ε ∈ W ′.

5 Equation for the limit cycles for the graphic (F 1
7a)

Let us recall that ¯µ = (¯ε2, ¯ε3, ε4) and that O(¯µ) denotes a function divisible in the ideal
generated by ¯ε2, ¯ε3, ε4. Recall that we have also introduced more precise notations in Nota-
tion 4.2: OP (¯µ) and OG(¯µ). For a local positive numerical function g we will also use the
usual Landau notation O(g).

5.1 The displacement map

It is convenient to interpret the formula (4.16) for Di
¯λ as a composition of three maps:
Di
¯λ = T i
¯λ ◦ H i
¯λ ◦ ˜Di
¯λ where

T i
¯λ (u) = u + ηi(¯λ), H i
¯λ(u) = ( ν
ν0
 )¯σi(¯λ)u, ˜Di
¯λ(u) = c
i(¯λ)u + ϕ
i(u, ¯λ) (5.1)

and ϕ = O(u2). Indeed as ¯T¯λ(0) is usually nonzero, it could become large after composition
by (H r
¯λ)−1 and then cause problems in the composition with the nonlinear map ( ˜Dr
¯λ)−1. So
we must avoid performing composition with ( ˜Dr
¯λ)−1 when ¯T¯λ(0) ̸= 0.
The trick to avoid this diﬃculty is to use the diﬀeomorphisms ˜Di
¯λ to reparameterize the
sections Σi. In these new parameterizations of Σi (that we continue to call z), the transition
T¯λ becomes: ˜T¯λ = (H r
¯λ)
−1 ◦ (T r
¯λ )
−1 ◦ ¯T¯λ ◦ T l
¯λ ◦ H l
¯λ
and the regular transition R becomes:

˜R¯λ = ˜Dr
¯λ ◦ R¯λ ◦ ( ˜Dl
¯λ)
−1

Then in this new coordinate on the sections Σi, the displacement map is equal to δ¯λ = ˜R¯λ− ˜T¯λ
and the equation for limit cycles is given by

δ¯λ(z) = ˜R¯λ(z) − ˜T¯λ(z) = 0.

We now want to make precise ˜R¯λ, ˜T¯λ.

20 R. Roussarie & C. Rousseau

5.2 The transition ˜T¯λ

We begin by looking to the composition (T r
¯λ )−1 ◦ ¯T¯λ ◦ T l
¯λ.

Proposition 5.1

(T r
¯λ )
−1 ◦ ¯T¯λ ◦ T l
¯λ(u) = u + ˜α + ˜βu + u2(¯ε2 ˜Φ2 + ¯ε3 ˜Φ3 + νε4 ˜Φ4) (5.2)

where there exists a τ > 0 such that

˜α = ˜α(¯λ) = α(¯λ) + ντ OP (¯µ),

˜β = ˜β(¯λ) = β(¯λ) + ντ OP (¯µ)

and α and β are the functions deﬁned in Proposition 4.1. The functions ˜α and ˜β are ν-
regularly smooth in µ. The ˜Φi = ˜Φi(u, ¯λ) are functions of (u, µ, ν) which are ν-regularly
smooth in (u, µ). Moreover ˜α = OP (¯µ) and ˜β = OP (¯µ).

Proof. Introducing Ψj(¯y, ¯λ) = ¯y2Φj(¯y, ¯λ), j = 2, 3, 4, the formula (4.1) can be written:

¯T¯λ(¯y) = ¯y + α(¯λ) + β(¯λ)¯y + ¯ε2Ψ2(¯y, ¯λ) + ¯ε3Ψ3(¯y, ¯λ) + νε4Ψ4(¯y, ¯λ).

Let us consider (T r
¯λ )−1 ◦ ¯T¯λ ◦ T l
¯λ(u) = ¯T¯λ(u + ηl) − ηr. It is equal to

u + ηl − ηr + βηl + α + βu + ¯ε2Ψ2(u + ηl, ¯λ) + ¯ε3Ψ3(u + ηl, ¯λ) + νε4Ψ4(u + ηl, ¯λ)

with α = α(¯λ), β = β(¯λ), ηi = ηi(¯λ).

We can expand:
 Ψi(u + ηl, ¯λ) = Ψi(ηl, ¯λ) + u ∂Ψi
∂u (ηl, ¯λ) + u
2 ˜Φi(u, ¯λ)

where ˜Φi(u, ¯λ) is ν-regularly smooth in (u, µ). One has that

Ψi(ηl, ¯λ) = O((ηl)
2) and ∂Ψi
∂u (ηl, ¯λ) = O(ηl).

Taking any strictly positive τ < σ(a) we have that ηl = O(ντ ) and then:

˜Φi(u + ηl, ¯λ) = O(ν2τ ) + uO(ντ ) + u
2Ψi(u, ¯λ) (5.3)

It suﬃces now to bring these expansions to obtain the expansion (5.2) with:

˜α(¯λ) = α(¯λ) + ηl(¯λ) − ηr(¯λ) + β(¯λ)ηl(¯λ) + ν2τ OP (¯µ) = α(¯λ) + ντ OP (¯µ)

as ηl(¯λ) − ηr(¯λ) = ντ OP (¯µ) by Proposition 4.7. We have also that ˜β(¯λ) = β(¯λ) + ντ OP (¯µ).
✷
 We can now compute ˜T¯λ = (H r
¯λ)−1 ◦ (
(T r
¯λ )−1 ◦ ¯T¯λ ◦ T l
¯λ
) ◦ H l
¯λ, using the formula (5.2):

˜T¯λ(z) = ˜α(¯λ)
( ν
ν0
 )−¯σr + (1 + ˜β(¯λ))z( ν
ν0
 )¯σl−¯σr + z2( ν
ν0
 )2¯σl−¯σr (¯ε2 ˆΦ2 + ¯ε3 ˆΦ3 + νε4 ˆΦ4)

Finite cyclicity of nilpotent graphics surrounding a center 21

where ¯σi = ¯σi(¯λ) and ˆΦi = ˆΦi(z, ¯λ) = ˜Φi(
z( ν
ν0
 )¯σl, ¯λ) is ν-regularly smooth in (z, µ). We
have that ( ν
ν0
 )¯σl−¯σr = ( ν
ν0
 )νOP (¯µ) = 1 + ν log( ν
ν0
 )OP (¯µ)

and then:
 (1 + ˜β(¯λ))
( ν
ν0
 )¯σl−¯σr = 1 + β(¯λ) + ντ OP (¯µ) (5.4)

for some new value of τ > 0. Finally, we have obtained the following representation of ˜T¯λ :

Proposition 5.2 There exists some τ > 0 such that:

˜T¯λ(z) = z + (α(¯λ) + ντ OP (¯µ)
)( ν
ν0
 )−¯σr + (β(¯λ) + ντ OP (¯µ)
)z + ντ OG(¯µ)z2 (5.5)

where α(¯λ) and β(¯λ) are the parameter functions deﬁned in Proposition 4.1 and the functions
represented by OP (¯µ) (resp. OG(¯µ)) are ν-regularly smooth in µ (resp. (z, µ)).

Remark 5.3 In order to apply the formula (5.5) we have to assume that the coeﬃcient
(α + ντ OP (¯µ)
)( ν
ν0
 )−¯σr remains bounded. This implies that the parameter ε2 must be chosen

in an interval of order ( ν
ν0
 )¯σr ≈ νσ(a). In fact, outside this interval, the possible limit cycles
have already escaped the neighborhood of Γ that is chosen for the study.

5.3 The regular transition ˜R¯λ

Below, τ > 0 is an arbitrarily small constant which may be adapted at each step. The map
R¯λ can be written: R¯λ(z) = z + νOG(¯µ) + ε4R4(z, ¯λ)

using (4.17). We ﬁrst compute:

R¯λ ◦ ( ˜Dl
¯λ)
−1(z) = ( ˜Dl
¯λ)
−1(z) + νOG(¯µ) + ε4R4(( ˜Dl
¯λ)
−1(z), ¯λ)

As ( ˜Dl
¯λ)−1(z) = z + O(ντ ) by inversion of a similar formula for ˜Dl
¯λ(z), we have that

R4(( ˜Dl
¯λ)
−1(z), ¯λ) = R4(z, ¯λ) + O(ντ )

and then, writting O(ντ )ε4 + νOG(¯µ) as ντ OG(¯µ) (for a suﬃciently small new τ ), one has

R¯λ ◦ ( ˜Dl
¯λ)
−1(z) = ( ˜Dl
¯λ)
−1(z) + ντ OG(¯µ) + ε4R4(z, ¯λ)

We can now compute
 ˜R¯λ(z) = ˜Dr
¯λ(
( ˜Dl
¯λ)
−1(z) + ντ OG(¯µ) + ε4R4(z, ¯λ)
)

Expanding this expression at order k = ord(Γ) we obtain

˜R¯λ(z) = ˜Dr
¯λ ◦ ( ˜Dl
¯λ)
−1(z) +
 k−1∑

j=1
 1
j! ∂j ˜Dr
¯λ
∂zj (( ˜Dl
¯λ)
−1(z))
(ντ OG(¯µ) + ε4R4(z, ¯λ)
)j

22 R. Roussarie & C. Rousseau

+ 1
k!
 ∫ 1

0 (1 − s)
k ∂k ˜Dr
¯λ
∂zk
 (
( ˜Dl
¯λ)
−1(z) + s(
ντ OG(¯µ) + ε4R4(z, ¯λ)
))(ντ OG(¯µ) + ε4R4(z, ¯λ)
)kds

Now, as ˜Dr
¯λ = ˜Dl
¯λ + ντ OG(¯µ), we have that

˜Dr
¯λ ◦ ( ˜Dl
¯λ)
−1(z) = z + ντ OG(¯µ).

From ˜Di
¯λ(z) = z + O(ντ ) we deduce that

∂ ˜Dr
¯λ
∂z (
( ˜Dl
¯λ)
−1(z)
) = 1 + O(ντ )

and also that
 ∂j ˜Dr
¯λ
∂zj
 (( ˜Dl
¯λ)
−1(z) + s(O(ντ )O(¯µ) + ε4R4(z, ¯λ)
)) = O(ντ )

Bringing these estimates in the above expression of ˜R¯λ we obtain

˜R¯λ(z) = z + ντ OG(¯µ) + (1 + O(ντ ))
(ντ OG(¯µ) + ε4R4(z, ¯λ)
) + ντ OG(¯µ)

Expanding this expression, one obtains the following result:

Proposition 5.4 ˜R¯λ(z) = z + ντ OG(¯µ) + ε4R4(z, ¯λ), (5.6)

for some τ > 0. The term OG(¯µ) and the function R4 are functions of (z, µ, ν) and are ν-
regularly smooth in (z, µ). In agreement with Proposition 4.10, one has that ∂kR4
∂zk (0, 0, 0) ̸= 0,
where k = ord(Γ) < ∞ is the order of the graphic Γ deﬁned in Deﬁnition 4.11.

Then, we have proved that ˜R¯λ has an expression similar to the one for R¯λ.

5.4 Presentation of the displacement map

We now use the expressions (5.5) and (5.6) to obtain a good presentation of δ¯λ = ˜R¯λ − ˜T¯λ.
We have, using the expressions of α, β, that

δ¯λ(z) = ντ OG(¯µ) + ε4R4(z, ¯λ)

−((
c2 ¯ε2 + ντ OP (¯µ)
)( ν
ν0
 )−¯σr + (c3 ¯ε3√¯ε1 + O(¯ε2) + ντ OP (¯µ)
)z + ντ OG(¯µ)z2).

where c2 = c2(¯λ) and c3 = c3(¯λ) are the strictly positive analytic functions deﬁned in Propo-
sition 4.1 (in particular, c2(¯λ), c3(¯λ) ≥ C for some constant C > 0).
We expand the ﬁrst term ντ OG(¯µ) of ˜R¯λ at order 2 in z :

ντ OG(¯µ) = ντ OP (¯µ) + ντ OP (¯µ)z + ντ OG(¯µ)z2

All the terms in this sum are ν-regularly smooth (in their other variables). We now regroup
these terms in δ with the corresponding terms in ˜T¯λ. (Let us remark for instance that the

Finite cyclicity of nilpotent graphics surrounding a center 23

term ντ OP (¯µ) of ˜R¯λ is of course absorbed by the term ντ OP (¯µ)
( ν
ν0
 )−¯σr of ˜T¯λ). We obtain
the following expansion:

δ¯λ(z) = ε4R4(z, ¯λ) − (
c2 ¯ε2 + ντ OP (¯µ)
)( ν
ν0
 )−¯σr

−(
c3 ¯ε3√¯ε1 + O(¯ε2) + ντ OP (¯µ)
)z + ντ OG(¯µ)z2, (5.7)

for some new terms OP (¯µ), OG(¯µ).
We introduce now the coeﬃcients of order 0 and 1 in (5.7) as new parameters, namely:
{
−˜ε2(¯λ) = c2(¯λ)¯ε2 + ντ OP (¯µ) = δ¯λ(0)
−˜ε3(¯λ) = c3(¯λ) ¯ε3√¯ε1 + O(¯ε2) + ντ OP (¯µ) = δ′
¯λ(0). (5.8)

(This change of parameters is invertible). In fact, writing

˜µ = (˜ε2, ˜ε3, ε4),

the map Pν : (¯µ, ε0) → (˜µ, ε0) is a ν-family of smooth diﬀeomorphisms which are ν-regularly
smooth in (¯µ, ε0). Of course, a function in the parameter ¯λ = (¯µ, ε0, ν) is OP (¯µ) if and
only it is OP (˜µ) and it is ν-regularly smooth in µ = (¯µ, ε0) if it is ν-regularly smooth in
(˜µ, ε0). Similar remarks can be made about the symbols OG(¯µ), OG(˜µ) and the ν-regularly
smoothness.
We can now expand the term ντ OG(¯µ)z2 of (5.7) in the ideal generated by ˜ε2, ˜ε3, ε4:

ντ OG(¯µ)z2 = ντ (˜ε2z2Ω2(z, ˜µ, ε0, ν) + ˜ε3z2Ω3(z, ˜µ, ε0, ν) + ε4z2Ω4(z, ˜µ, ε0, ν)
)

where the functions Ωi are ν-regularly smooth in (z, ˜µ, ε0). Putting this expression in (5.7),
we obtain:

Theorem 5.5

δ(z, ˜µ, ε0, ν) = ˜ε2( ν
ν0
 )−¯σr (
1 + ντ ( ν
ν0
 )¯σr z2Ω2) + ˜ε3z(
1 + ντ zΩ3) + ε4 ˜R4 (5.9)

where ˜R4 = R4 + ντ z2Ω4. The parameters ˜ε2, ˜ε3 are deﬁned by (5.8) and the functions ˜R4 =
˜R4(z, ˜µ, ε0, ν), Ωi = Ωi(z, ˜µ, ε0, ν) are ν-regularly smooth in (z, ˜µ, ε0). Moreover

∂k ˜R4
∂zk (0, ˜µ, ε0, ν) ̸= 0,

where k = ord(Γ) < ∞.

6 Finite cyclicity of (F 1
7a) and (H 1
7 )

6.1 The ﬁnite cyclicity of (
F 1
7a)

We will write ˜λ = (˜µ, ε0, ν)

24 R. Roussarie & C. Rousseau

and we recall that ε4 = ˜ε4. The parameter ˜λ is a parameter locally diﬀeomorphic to the
parameter ¯λ and it is of course equivalent to work with it to study the cyclicity.
Let Γ be any graphic of type (
F 1
7a) for the unfolding Xε, and δ(z, ˜λ, ν) its local dis-

placement map. We will use the equation (5.9) for δ(z, ˜λ, ν) to compute the cyclicity of the
graphics Γ¯ε3. These graphics of the blown-up unfolding ¯X˜λ, are the graphics associated to the
graphic Γ of Xε, and we will prove that Γ has a ﬁnite cyclicity using the formula (3.9).

6.1.1 The cyclicity of Γ¯ε3, for ¯ε3 ̸= 0

If ¯ε3 ̸= ±1, 0 (i.e. if ¯ε1 ̸= 0, 1), the derivative ∂δ
∂z (0, 0, ¯ε3, 0, 0) = c3 ¯ε3√¯ε1 ̸= 0 and the unfolding
is generic in the direction of the parameter ¯ε2. Then Cycl( ¯X˜λ, Γ¯ε3) = 1, for ¯ε3 ̸= ±1, 0.
It was proved in [6] that Cycl( ¯X˜λ, Γ±1) = 1. It is also possible to deduce this from (5.9).
In fact, as the function c3(¯λ) > C > 0, we have that |˜ε3| → +∞ when ¯ε3 → ±1 in (5.8)
(recall that ¯ε1 = √1 − ¯ε2
3). Then, we also have Cycl( ¯X˜λ, Γ±1) = 1.

6.1.2 The cyclicity of Γ0

Theorem 6.1 Let the order of the graphic Γ, ord(Γ), be deﬁned through the regular transition
R¯λ in Deﬁnition 4.11. Then
 Cycl( ¯X˜λ, Γ0) ≤ ord(Γ) < ∞.

Proof. The proof uses a procedure of derivation-division applied to (5.9), very similar to
the one ﬁrst introduced in [8]. To make the text more readable, we will give a short sketch
of the proof. To simplify, we do not write everywhere the variables.
Let W = U \ {0}, where U is some compact neighborhood of ˜λ = 0 in the parameter
space, in which the formula (5.9) makes sense (for z small enough). We can write

W = W2 ∪ W3 ∪ W4

where Wi = {˜λ | |˜εi| ≥ |˜εj|, for j ∈ {2, 3, 4} \ {i} },

where we have written ε4 = ˜ε4 for convenience. Let us notice that ˜εi ̸= 0 when ˜λ ∈ Wi.

1. On W2 one can consider:

δ(z, ˜µ, ε0, ν)
˜ε2 = ( ν
ν0
 )−¯σr (
1 + ντ ( ν
ν0
 )¯σr z2Ω2) + ˜ε3
˜ε2 z(1 + ντ zΩ3) + ˜ε4
˜ε2 ˜R4

= ( ν
ν0
 )−¯σr (1 + ντ ( ν
ν0
 )¯σr z2Ω2) + O(z).

As U is compact, this function is everywhere non-zero for ˜λ ∈ W2, and z small enough.
Then, the displacement function does not vanish for ˜λ ∈ W2, and z suﬃciently small.

2. If z is small enough, one can consider on W3 the function

˜δ = δ(z, ˜µ, ε0, ν)

1 + ντ ( ν
ν0
 )¯σr z2Ω2 = ˜ε2( ν
ν0
 )−¯σr + ˜ε3z 1 + ντ zΩ3

1 + ντ ( ν
ν0
 )¯σr z2Ω2 + ε4R4.

Finite cyclicity of nilpotent graphics surrounding a center 25

where R4 = ˜R4/
(1 + ντ ( ν
ν0
 )¯σr z2Ω2) is nonlinear of order k ≥ 2 in z at z = 0, ˜λ = 0, as

˜R4. Let us consider δ1 = ∂ ˜δ
∂z . One has

δ1 = ˜ε3(1 + ντ z ˆΩ3) + ˜ε4 ˆR4,

for functions ˆΩ3, ˆR4, which are ν-regularly smooth in (z, ˜µ, ε0). The function ˆR4 is of
order k − 1 in z at z = 0, ˜λ = 0 and then ˆR4 = O(|z| + ||˜λ||). Then the function
δ1
˜ε3 = 1 + O(|z| + ||˜λ||), does not vanish on W3 as soon as we choose the size of U small
enough. Using Rolle’s Theorem, one obtains that the displacement function has at most
one zero for ˜λ ∈ W2, and z suﬃciently small.

3. If z is small enough, one can consider on W4 the function

˜δ1 = δ1
1 + ντ z ˆΩ3 = ˜ε3 + ˜ε4 ˆR4
1 + ντ z ˆΩ3 ,

where the function ˆR4/(1 + ντ z ˆΩ3) is of order k − 1 in z at z = 0, ˜λ = 0. Then, if
δk = ∂k−1
∂zk−1 ˜δ1, one has
 δk(z, ˜λ) = ˜ε4U (z, ˜µ, ε0, ν)

where U is a function ν-regularly smooth in (z, ˜µ, ε0) such that U (0, 0, 0) ̸= 0. Applying
again k times Rolle’s Theorem, one obtains that the displacement function has at most
k zeros for ˜λ ∈ W2, with z and the size of U suﬃcently small.

The result follows now from the three above points. ✷

6.1.3 The cyclicity of Γ

By deﬁnition, ord(Γ) ≥ 2. Then it follows from the above results and the formula (3.9) that

Theorem 6.2 Cycl(Xε, Γ) ≤ ord(Γ) < ∞.

Moreover for all graphics (F 1
7 ) except a discrete set we have Cycl(Xε, (F 1
7 )) ≤ 2.

6.2 The ﬁnite cyclicity of (H 1
7 )

The transition R¯λ (which is no more regular in that case) has been calculated in Proposi-
tion 4.13 in the variable ˇy = (ζ¯λ)−1(¯y). This allows to get the exact cyclicity theorem:

Theorem 6.3 Cycl(Xε, H 1
7 ) ≤ 2.

Proof. We consider the displacement map

ˇδ¯λ(ˇy) = R¯λ ◦ ζ¯λ − T¯λ ◦ ζ¯λ.

26 R. Roussarie & C. Rousseau

We have that T¯λ = (Dr
¯λ)−1 ◦ ¯T¯λ ◦ Dl
¯λ. We consider the composition Dl
¯λ ◦ ζ¯λ = ¯Dl
¯λ. It is a
map which has the same form as Dl
¯λ as in (4.16). So it an also be written as a composition
of three maps: ¯Dl
¯λ = ˇT l
¯λ ◦ ˇH l
¯λ ◦ ˇDl
¯λ where

ˇT l
¯λ(u) = u + ˇηl(µ, ν), ˇH l
¯λ(u) = ( ν
ν0
 )¯σlu, ˇDl
¯λ(u) = u + ˇϕ
i(u, µ, ν) (6.1)

and {ˇηl(µ, ν) = ηl + ντ OP (¯µ)
ˇϕ(u, µ, ν) = u2OG(¯µ).

The function ˇηl (resp. ˇD¯λ) is ν-regularly smooth in µ (resp. (u, µ)).
Rather than working with ˇδ¯λ we will work with

δ¯λ = ˜Dr
¯λ ◦ ˇδ¯λ ◦ ˇDl
¯λ
= ˜Dr
¯λ ◦ R¯λ ◦ ˇDl
¯λ − (H r
¯λ)−1 ◦ (T r
¯λ )−1 ◦ ¯T¯λ ◦ ˇT l
¯λ ◦ ˇH l
¯λ
= ˜R¯λ − ˜T¯λ,

where { ˜R¯λ = ˜Dr
¯λ ◦ R¯λ ◦ ˇDl
¯λ
˜T¯λ = (H r
¯λ)−1 ◦ (T r
¯λ )−1 ◦ ¯T¯λ ◦ ˇT l
¯λ ◦ ˇH l
¯λ.

The form of ˜T¯λ is exactly the one given by Proposition 5.2. Also the composition ˜R¯λ has the
same form as ˇR¯λ given in Proposition 4.13.
This allows to give a nice decomposition for δ which has exactly the form of (5.7), the
only diﬀerence being the form of R4. Finally we can reparameterize as in the case of (F 1
7a)
and get

δ(z, ˜µ, ν) = ˜ε2( ν
ν0
 )−¯σr (
1 + ντ zΩ2) + ˜ε3z(1 + ντ zΩ3) + ˜ε4z1+sr (1 + Ω4) (6.2)

where Ω4(z, ˜µ, ε0, ν) = O(z) and the functions Ωi = Ωi(z, ˜µ, ε0, ν) have the property (I) of
Mourtada (see Deﬁnition 4.14).
As {1, z, z1+sr } is a Tchebychev system, a standard division of the parameter space in
cones and derivation-division yields that δ has at most two positive zeroes in z in a neigh-
borhood of (z, ˜µ, ε0, ν) = 0. ✷

7 The graphics (I 1
6a) and (H 3
11)

Here most of the development is identical to the case of the graphics (F 1
7a) and (H 1
7 ), so we
will only insist on the diﬀerences. We drop the dependence on ¯λ in all expressions.
The main diﬀerence comes from the fact that the connection on the blow-up sphere is
ﬁxed (see Figure 7). So the map ¯T has the property that ¯T (0) = 0. One consequence is that
the reparametrization from R, T to ˜R, ˜T is no more necessary.
The formulas for the blow-up of (2.19) have been given in Section 3.2. The sections used
for deﬁning the displacement map are now given by {v = ±V0} and they are parameterized
by ¯w. Consider the cyclicity of a graphic Γ cutting the sections at w0 in w-variable ( ¯w0 in
¯w-variable). We will let z = ¯w − ¯w0, so the graphic occurs at z = 0. Moreover w0 = 0 for the
graphic (H 3
11).

Finite cyclicity of nilpotent graphics surrounding a center 27

ΣrΣl
 pr
pl

Figure 7: The sections Σr and Σl for a graphic (I6a)

7.1 Finite cyclicity of (I 1
6a)

In the previous section, when we were considering the equation for limit cycles we were
having terms of diﬀerent orders controlled by independent parameters. Let us review this
and compare with what we now have:

• The dominant nonlinear term was coming from R, since the nonlinear terms of ¯T were
multiplied by a factor ντ . It was controlled by the parameter ε4. This property will
remain the same for the displacement maps associated to (I6a) and (H 3
11).

• The dominant linear term was coming from ¯T : this property will remain the same. In
the previous section the analysis has allowed us to reparameterize by ˜ε3 which was the
coeﬃcient of the linear term minus 1. Moreover the form of ˜ε3 was a nonzero multiple
of ¯ε3 plus a term of the form O(¯ε2). Here is is even simpler as ¯T ′(0) is exactly a nonzero
multiple of ¯ε3.

• The dominant constant term was coming from ¯T . It was dominant over the constant
term coming from R because of the factor ντ in the constant term of R. It was controlled
by a parameter ˜ε2 which was “essentially” a large multiple of ε2.

This is no more valid as ¯T and Di, i = l, r, have no constant terms. So the constant
term is exactly that of R. Fortunately there is an easy way to handle this. Indeed only
the parameters ε1 and ε3 have been blown-up in Section 3.2. Moreover the ε2-term is
without contact in (2.13). This yields (keeping z for the name of the variable in R so
that the graphic occurs at z = 0):
 ∂R(0)
∂ε2 = c2 ̸= 0. (7.1)

Since R is analytic in ε and R ≡ id when ε2 = ε3 = ε4 = 0 we have moreover

∂R(0)
∂ ¯ε3 = O(ν). (7.2)

In the previous section it was obvious without calculations that (ε2, ¯ε3, ε4) ↦→ (˜ε2, ˜ε3, ε4)
was an invertible change of parameters because of the presence of the factors ντ . In the
context of (I16a) and (H 3
11) we need to be more careful. A natural reparametrization is given
by (ε2, ¯ε3, ε4) ↦→ (˜ε2, ˜ε3, ˜ε4) = (R(0), R′(0) − T ′(0), ε4). (7.3)

28 R. Roussarie & C. Rousseau

Lemma 7.1 The change of parameters (7.3) is invertible.

The ﬁrst thing to remark is that R′(0) − T ′(0) = c3 ¯ε3 + O(ν) with c3 ̸= 0. So it suﬃces
to show that for ε3 = 0 the change of parametrization (ε2, ε4) ↦→ (˜ε2, ˜ε4) = (R(0), ε4) is
invertible. This follows from (7.1). ✷

The transition map R from Σr = {v = V0} to Σl = {v = −V0} following the ﬂow
backwards is analytic. Moreover we have that R ≡ id for ˜ε2 = ˜ε3 = ˜ε4 = 0. We will stress
that the map δ smoothly depends on ¯w0 and we will make this dependence explicit. This
yields a decomposition

R(z, w0) − z = ˜ε2h2(z, w0) + ˜ε3zh3(z, w0) + ˜ε4z2h4(z, w0), (7.4)

where h2(0, w0) ̸= 0.

Proposition 7.2 For each ¯w0 there exists k = k( ¯w0) ≥ 0 such that ∂kh4
∂zk ̸= 0.

Proof. We want to use an analyticity argument as in the proof of Proposition 4.10. Indeed
for w0 ̸= 0 the maps hj(z, w0) depend analytically on z, w0 and the parameters. Moreover
we can show that h4 ̸= 0 for w0 small (see Lemma 7.4 below). This follows by analyzing R
in the neighborhood of the hemicycle. The conclusion follows from the analyticity of h4. ✷

Deﬁnition 7.3 Let k(w0) be the minimum k with this property, then the order of Γ is
deﬁned as ord(Γ) = k(w0) + 2.

Lemma 7.4 The function h4 deﬁned in Proposition 7.2 does not vanish in a neighborhood
of 0 for w0 small.

Proof. An asymptotic expansion of the transition R along the hemicycle can only be
explicitly calculated when ε2 = 0, i.e. the invariant line remains unbroken (more details in [6]
and in Section 7.2 below). Let us look at Figure 8. Then we have R = (Sr◦∆r◦Sf in◦∆l◦Sl)−1.
It has the form R(z) = c1z + c2z1+sl + o(z1+sl)

where sl ∈ (0, 1) is the hyperbolicity ratio of Pl. (This is the case since 1/sr = sl.) The
coeﬃcient c2 is a nonzero multiple of S′′
f in(0) which was calculated in [6] for ε2 = 0. The
calculation yielded S′′
f in(0) = Cε4 for some nonzero constant C. Remark that the function
O(z1+sl) has property (I). ✷

Theorem 7.5 Let Γ be a graphic of type (I 1
6a). Then

Cycl(Xε, Γ) ≤ ord(Γ).

Proof. Let k + 2 = ord(Γ). As before we consider the displacement function δ(z) =
R(z) − T (z). It can be decomposed as

δ(z, w0) = ˜ε2Ψ2(z, w0) + ˜ε3zΨ3(z, w0) + z2 ˜ε4Ψ4(z, w0), (7.5)

where Ψ2, Ψ3 ̸= 0 and ∂kΨ4
∂zk ̸= 0. A separation of the discussion in three cones and an
algorithm of derivation-division allows to conclude as in Section 6.1. ✷

Finite cyclicity of nilpotent graphics surrounding a center 29

7.2 Finite cyclicity of (H 3
11)

Theorem 7.6 Cycl(Xε, H 3
11) ≤ 2.

Proof. We introduce sections as in Figure 8. All connections along the equator are ﬁxed,

Σl Σr

Πl Π
r

Π
l' Πr
'

Sl Sr

Sfin
∆l ∆r PrPl

Figure 8: The sections for the graphic (H 3
11)

so it is natural to consider a displacement map δ : Σr → Π′
r given by

δ = ∆l ◦ Sl ◦ T − S−1
f in ◦ ∆−1
r ◦ (Sr)
−1.

We have that Sr − Sl = OG(¯µ). Also the ∆i are given by
{∆l(u) = usl(1 + Ψl(u, ε))
(∆r)−1(u) = usl(1 + Ψr(u, ε))

where the Ψi(u, ε) are of class (I) and Ψl(u, ε) − Ψr(u, ε) = OG(¯µ). Finally

Sf in(u) − u = OG(u) = ε2S2(u) + ¯ε3S3(u) + ε4S4(u)

with S2(0) ̸= 0, S3(0) = 0, S′
3(0) ̸= 0, S4(0) = 0 and ∂2S4
∂u2 ̸= 0 and sl ∈ (0, 1). This gives for
δ a decomposition

δ(z) = ε2h2(z, µ, ν) + (¯ε3 + ντ OP (µ))zh3(z, µ, ν) + (ε4 + ντ OP (¯µ))z1+slh4(z, µ, ν)

with h2, h3, h4 ̸= 0 from which cyclicity 2 follows. ✷

8 Perspectives for proving the ﬁnite cyclicity of center graph-
ics

The present paper presents a strategy to study the ﬁnite cyclicity of several center graph-
ics occurring in ﬁnite-parameter families of analytic vector ﬁelds Xε. With the following
ingredients we can hope proving the ﬁnite cyclicity of a center graphic Γ0:

(i) The Bautin ideal is radical. We recall that the set of zeros of this ideal is the set of
parameter values for which there exists an annulus of periodic solutions.

30 R. Roussarie & C. Rousseau

(ii) There exists a regular submanifold M in parameter space such that for ε ∈ M then Xε
has a graphic Γε. The family {Γε}ε∈M is a continuous family of graphics. All graphics
Γε have the “same type” (same kind of singular points and orbits connecting them).

(iii) Any graphic Γε is either a center graphic for ε in the set of zeros of the Bautin ideal or
satisﬁes a genericity condition.

(iv) The ﬁnite cyclicity of a generic graphic Γε0 is obtained by means of a generalized
derivation-division algorithm on a “well-behaved” system of equations whose solutions
yield the periodic solutions of Xε for ε close to ε0.

(v) The ﬁnite cyclicity of the generic Γε’s in the neighborhood of a center graphic is uniformly
bounded in the neighborhood of a center graphic.

These conditions are very general. Conditions (i) and (ii) are satisﬁed for all center
graphics from the DRR program. In [2] and [5], it was pointed that there remains a unique
elementary graphic (i.e. with only hyperbolic and semi-hyperbolic singular points), namely
(I16a), whose ﬁnite cyclicity is not yet proved. This graphic satisﬁes (i)-(v).
Let us discuss in more detail why the method presented here is powerful for studying the
center graphics of the DRR program. The usual problem with studying the exact cyclicity
of center graphics is the computation of complicated Abelian integrals. Indeed we need to
show that a change of parameters as in Lemma 7.1 is invertible. A direct calculation could
be extremely tricky. Our argument is indirect and makes an essential use of analyticity: it
applies for graphics occurring in families of graphics. The genericity condition for the generic
graphics is deﬁned on analytic transitions between analytic sections and has the property
that, once it is satisﬁed for one graphic, it is satisﬁed for all graphics in the family. The
genericity condition is easy to check (by direct calculation) for a graphic near the boundary
of the family of graphics. Indeed the boundary graphic usually involves invariant lines.
Passing to the proof that the change of parameters is invertible, we use the analyticity in the
parameters: it is easy to show that the change of parameters is invertible near the boundary
graphic. Analyticity in the parameters allows to push this property for all graphics. This
last property has not yet been noticed at the time of [2], explaining why the ﬁnite cyclicity
of (I16a) was not proved at the time.

Acknowledgments

The ﬁrst author would like to thank the Centre de Recherches Math´ematiques (Montreal),
for its hospitality during the preparation of this paper.

Finite cyclicity of nilpotent graphics surrounding a center 31

References

[1] F. Dumortier, Y. Ilyashenko and C. Rousseau, Normal forms near a saddle-node
and applications to ﬁnite cyclicity of graphics, Ergod. Th. Dynam. Syst. 22 (2002),
783–818.

[2] F. Dumortier, A. Guzm´an, and C. Rousseau, Finite cyclicity of elementary graphics
surrounding a focus or center in quadratic systems, Qual. Theory Dynam. Syst., 3
(2002), 123–154.

[3] F. Dumortier and R. Roussarie, Duck cycles and centre manifolds, Memoirs of A.M.S.
121, n◦1 (1996), 1–100.

[4] F. Dumortier, R. Roussarie, and C. Rousseau, Hilbert’s 16-th problem for quadratic
vector ﬁelds, J. Diﬀerential Equations 110 (1994), 86–133.

[5] C. Rousseau, Normal forms, bifurcations and ﬁniteness properties of vector ﬁelds, in
Normal forms, bifurcations and ﬁniteness properties of vector ﬁelds, NATO Sci. Ser.
II Math. Phys. Chem., 137, Kluwer Acad. Publ., Dordrecht, 2004, 431–470.

[6] C. Rousseau and H. Zhu, PP-graphics with a nilpotent elliptic singularity in quadratic
systems and Hilbert’s 16th problem, J. Diﬀerential Equations, 196 (2004), 169–208.

[7] H. Zhu, and C. Rousseau, Finite cyclicity of graphics through a nilpotent singularity
of elliptic or saddle type, J. Diﬀerential Equations 178 (2002), 325-436.

[8] R. Roussarie, On the number of limit cycles which appear by perturbation of separatrix
loop of planar vector ﬁelds, Bol. Soc. Bras. Mat., 17, (1986), no. 2, 67-101.

[9] R. Roussarie, Bifurcations of Planar Vector Fields and Hilbert’s Sixteenth Problem,
Progress in Mathematics, vol. 164, Birkhauser-Verlag, Basel (1998).
