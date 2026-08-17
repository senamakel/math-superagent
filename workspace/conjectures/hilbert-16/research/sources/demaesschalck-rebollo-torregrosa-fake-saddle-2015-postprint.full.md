<!-- source: https://ddd.uab.cat/pub/artpub/2015/gsduab_3787/joudifequ_a2015v258n2p588preprint.pdf | converted from PDF -->

Cyclicity of a fake saddle inside the quadratic vector
ﬁelds

P. De Maesschalck
a, S. Rebollo-Perdomo
b, J. Torregrosac,∗

aHasselt University, Martelarenlaan 42, B-3500 Hasselt, Belgium
bCentre de Recerca Matem`atica, 08193 Bellaterra, Barcelona, Spain
cDepartament de Matem`atiques, Universitat Aut`onoma de Barcelona, Ediﬁci C, 08193
Bellaterra, Barcelona, Spain

Abstract

This paper concerns the study of small-amplitude limit cycles that appear in
the phase portrait near an unfolded fake saddle singularity. This degenerate
singularity is also known as a impassable grain. The normal form of the unper-
turbed vector ﬁeld is like a degenerate ﬂow box. Near the singularity,the phase
portrait consists of parallel ﬁbers, all of which but one have no singular points,
and at the singular ﬁber, there is one node. We study diﬀerent techniques in
order to show that the cyclicity is bigger or equal than two when the normal
form is quadratic.

Keywords: Cyclicity, Fake saddle, Impassable grain, Degenerate critical
point, Limit cycle, Bifurcation, Singularity unfolding.
2010 MSC: 34C07, 37G10, 37G15, 34D15.

1. Introduction

This paper concerns the study of small-amplitude limit cycles that appear
in the phase portrait near an unfolded degenerate singularity. More speciﬁcally,
we assume that the unperturbed vector ﬁeld can be put in a normal form that
is like a degenerate ﬂow box: near the singularity, the phase portrait consists
of parallel ﬁbers, all of which but one have no singular points, and the singular
ﬁber has a semi-stable equilibrium point. This singularity is known as a fake
saddle or a impassable grain, see [23]. In fact, it is a singularity with exactly
two saddle sectors.
Though the paper deals with more general vector ﬁelds in local normal form,
to present the ideas, think of the following typical model:

X0 : { ˙x = 0, ˙y = x2 + y2}.

This is a preprint of: “Cyclicity of a fake saddle inside the quadratic vector ﬁelds”, Peter de
Maesschalck, Salom´on Rebollo-Perdomo, Joan Torregrosa, J. Diﬀerential Equations, vol. 258(2),
588–620, 2015.
DOI: [10.1016/j.jde.2014.09.024]

whose local phase portrait is shown in Figure 1.

Figure 1: Phase portrait of X0.

In any unfolding, the ﬁbers {x = const} away from the origin will smoothly
perturb to ﬁbers without singular points. Close to the origin, more complicated
phenomena may occur: we show the presence of Hopf bifurcations, Bogdanov–
Takens bifurcations, slow-fast (canard) behavior, homoclinic and heteroclinic
orbits. All the above phenomena are well-known mechanisms near which limit
cycles can be born, and in fact the study of periodic orbits near the degenerate
point is the principle goal of this paper. We use the aforementioned mechanisms
to show the presence of up to two small amplitude limit cycles, and give evidence
that by using these mechanisms this is the best one can get.
Determining an upper bound for the number of limit cycles turned out to
be too dicult, as it revealed that a multi-parameter global study of phase
portraits was needed, going far beyond the traditional perturbative methods to
create limit cycles.
In a study of unfoldings of a vector ﬁeld like X0, it is best to make a ho-
mogeneous (family) blow-up of the perturbed family of vector ﬁelds, thereby
focusing on the behavior at the blow-up locus. The behavior at the blow-up lo-
cus is shown to be mostly determined by perturbation terms of degree two and
lower. We will therefore focus our attention to perturbations of at most degree
two. Though this restriction immediately shows a relation between the Hilbert
16th problem in degree 2, the study of the singularity at X0 has in fact no
contribution in the degree-2 programme outlined by Dumortier, Roussarie and
Rousseau [13]: in that programme, homogeneous vector ﬁelds could be avoided
using rescalings. Setting this remark aside, the study of the cyclicity of X0 at
the origin has a relevance on its own.
In Section 2 we consider forms for the unperturbed system under some ad-
ditional generic and geometric constraints, and show that the normal form de-
pends on two parameters (A, B). Next, we consider normal forms for unfoldings.
It is shown that, up to the quadratic part, any such unfolding can be written
as a 6-parameter family of vector ﬁelds: two parameters altering (A, B), and 4
additional parameters (µ1, µ2, µ3, µ4). We infer that the study of any smooth
normal form for the singularity and its unfolding will most dominantly be af-
fected by its quadratic part. More precisely, we prove that the normal form for

2

unfoldings is
{ _x = ax2 + bxy + µ1 + µ2x + µ3y + O(∥(x, y)∥
3),
_y = x2 + y2 − µ4 + O(∥(x, y)∥3), (1)

where a = A + o(1) and b = B + o(1).
Next, we restrict to quadratic vector ﬁelds and present several results on the
existence of limit cycles using perturbative arguments. In fact the maximum
number of limit cycles obtained in this way is two, with conﬁgurations (2 : 0)
and (1 : 1). In Section 3 we study the cyclicity and simultaneity properties near
isolated singularities. First perturbing weak foci by computing Lyapunov coef-
ﬁcients, secondly studying the presence of cusp points and their unfolding in a
Bogdanov–Takens bifurcation diagram (in fact we prove the simultaneous exis-
tence of two BT-diagrams). A characterization of the centers of (1) restricted to
quadratic case can be found in Section 4. The quadratic perturbations of some
centers included in these families is studied by many authors. The Hamiltonian
case is studied in [19] but the reversible non-Hamiltonian case only have been
considered in few particular cases, see [3, 5, 16, 20], and in all cases the cyclicity
is two. A short review of them is also given in this section. In Section 5, we
study slow-fast families of vector ﬁelds appearing in the model.
In a ﬁnal step, inspired by [5], we consider in Section 6 a class of sym-
metric unfoldings of the singular point, allowing us to reduce the dimension of
the parameter space. As the unperturbed vector ﬁeld is invariant under the
transformation (x, y, t) ↦→ (−x, −y, −t), we take the perturbations which are in-
variant under this transformation as well. Thus µ2 = µ3 = 0, and the restricted
quadratic family (1) can be written as
{ _x = ax2 + bxy + µ,
_y = x2 + y2 − 1. (2)

We prove that this family has at most two limit cycles in conﬁguration (1 : 1).
We show the limitations of the perturbative techniques as they fail to provide
a global bifurcation diagram for the number of limit cycles even for this simple
family of vector ﬁelds.

2. Local normal forms

2.1. Normal form of the unperturbed fake saddle

We consider a smooth vector ﬁeld X0 having a smooth invariant curve x =
φ(y) (with φ(0) = 0), and for which the reduction of X0 to this curve is given
by the equation _y = cy2 + O(y3), c > 0.

The conditions in the following lemma determine precisely the kind of sin-
gularity we examine in this paper.
 3

Lemma 1. Assume, under the above condition, that the origin is a degenerate
singular point having exactly two separatrices, both of which are the boundary of
two hyperbolic sectors. Then there exists a smooth local change of coordinates
bringing the vector ﬁeld in the form
{ _x = Ax2 + Bxy + O(∥(x, y)∥3),
_y = x2 + y2 + O(∥(x, y)∥
3), (3)

where A ≥ 0, B < 1 and A2 < 4(1 − B). (When the invariant ﬁber is a straight
line, the change of coordinates is linear.)

Proof. We assume that X0 = (P, Q) has a degenerate singular point at the
origin, implying that P (0, 0) = Q(0, 0) = 0. We also assume that the degenerate
point has no other separatrices beside the ones on the ﬁber y = 0, and that
{y = 0} separates two hyperbolic sectors. Since the origin is a degenerate
singularity, a blow-up analysis reveals the nature of singular points. We write

(x, y) = (r cos θ, r sin θ).

Imposing that {y = 0} is the border of a hyperbolic sector implies that
Py(0, 0) < 1. (This is done by requiring the Jacobian matrix of the blow-
up vector ﬁeld at (r, θ) = (0, ±π/2) to have a saddle structure.) Under this
condition, we can apply a linear transformation (x, y) ↦→ (x, ρx + y) to make
Qy(0, 0) = 0. Furthermore, we can then exclude the case Qx(0, 0) = 0 from the
study (since there are always extra separatrices then), after which we can scale
the coecient to 1. In short, we can assume

P (x, y) = Ax2 + Bxy, Q(x, y) = x2 + y2.

Additional search for separatrices leads to the property that A2 < 4(1 − B).
Symmetry allows us to assume A ≥ 0.

As a special case, we will sometimes consider those vector ﬁelds (3) that are
invariant under the symmetry (x, y, t) ↦→ (−x, −y, −t). The quadratic part is
of course always invariant under the symmetry, but for some vector ﬁelds the
higher order terms can break symmetry.

The vector ﬁeld (3) has the so-called degenerate ﬂow-box property: there
exists two boxes Bi ⊂ Be (interior and exterior) with the following properties.
Each of the boxes are dieomorphic to a square, and its four boundaries con-
sist of two orbits, an inset and an outset. Along the inset, the vector ﬁeld is
transverse and points inwards the box, and alon the outside, the vector ﬁeld is
transverse and points outwards. The orbit-edges of Bi reach the outset of Be
in positive time and the inset of Be in negative time. Furthermore, Be \ Bi has
no singular points, and Bi can be chosen arbitrarily small around the origin.

Lemma 2. Any smooth perturbation of vector ﬁeld (3) retains the degenerate
ﬂow-box property.
 4

Proof. The boxes consist of regular orbits, which perturb to regular orbits, and
insets and outsets. The transversality along the inset and outset also persists
for small perturbations.

Of course, the most interesting thing to study is what happens inside the
interior box Bi for perturbations of (3). In the next section, we study unfoldings.

2.2. Normal forms for unfoldings of the fake saddle
We consider now a perturbation
{ _x = Ax2 + Bxy + εP (x, y),
_y = x2 + y2 + εQ(x, y).

We let x = X + pY + q, y = Y + rX + s,

where p, q, r, s are to be determined implicitly below and keeping in mind all 4
ought to be O(ε). For the new equations in (X, Y ), we will require that

∂ _Y
∂X (0, 0) = ∂ _Y
∂Y (0, 0) = ∂2 _Y
∂X∂Y (0, 0) = ∂2 _X
∂Y 2 (0, 0) = 0.

Considering the mapping 	 : ( p, q, r, s, ε) ↦→ ( ∂ ˙Y
∂X (0, 0), . . . , ∂2 ˙X
∂Y 2 (0, 0)), then
it is clear that 	(0 , 0, 0, 0, 0) = (0, 0, 0, 0). On the other hand, it is a tedious
but easy exercise to show that

∂
∂(p, q, r, s) (0) =
 ∣
∣
∣
∣
∣
∣
∣
∣
 2(B − 1) 0 0 0
0 2 0 0
0 0 0 2
2 0 2 − B 0
 ∣
∣
∣
∣
∣
∣
∣
∣
 = 8(B − 1)(B − 2),

so we can apply the Implicit Function Theorem to prepare the perturbation in
the required form. This implies that we may consider
{ _x = ax2 + bxy + µ1 + µ2x + µ3y + O(∥(x, y)∥
3),
_y = x2 + y2 − µ4 + O(∥(x, y)∥3),

where a = A + o(1), b = B + o(1), and a
2 < 4(1 − b).
We now write

(µ1, µ2, µ3, µ4) = (v2M1, vM2, vM3, v2M4), v ≥ 0.

In a perturbation scheme where µ ≈ 0, we can keep ∥(M1, M2, M3, M4)∥ = 1
and let v ≈ 0.

Lemma 3. The ((v, M1, M2, M3, M4)-families of ) boxes Bi ⊂ Bo in (x, y)-
space can be chosen so that Bi lies in a O(v)-neighbourhood of the origin. (In
the language of blow-up: in a family blow-up procedure, the interior box can be
chosen as a compact K in the family chart.)

5

Proof. Use phase directional blow-up and the fact that the equator only contains
singularities at the poles.

We now blow up the origin using a homogeneous family blow-up and consider
the phase directional chart:
 (x, y, v) = (vX, vY ).

We ﬁnd { _X = aX 2 + bXY + M1 + M2X + M3Y + O(v),
_Y = X 2 + Y 2 − M4 + O(v). (4)

Remark 4. It is clear that the behaviour for v = 0 is the important piece of
information needed to determine the behaviour of (4). Furthermore, the vector
ﬁeld for v = 0 is a normal form in the space of quadratic perturbations. In
addition, the system (4) with v = 0 has no singular points for M4 < 0, and
for M4 = 0, it has a unique singular point at the origin, whose index is zero.
Therefore in both cases the restricted system has no limit cycles.

2.3. Parameter charts of the quadratic normal form
The normal form obtained from (4), after reducing to v = 0, that can have
limit cycles is { _X = aX 2 + bXY + M1 + M2X + M3Y,
_Y = X 2 + Y 2 − M4, (5)

with M4 ≥ 0.
Recall also that (M1, M2, M3, M4) lies on a sphere and cannot be zero simul-
taneously. It is important to realize that the local problem that was initially
posed in this paper, i.e. study the degenerate singular point, now has become
a global problem, both in phase space and parameter space. The control on the
number of limit cycles is typically not easy in this situation.
Removing the capitals in the notation, we have reduced to the global study
of the following family of vector ﬁelds:
{ _x = ax2 + bxy + µ1 + µ2x + µ3y,
_y = x
2 + y2 − µ4, (6)

where (x, y) is to be considered in a large compact set in the plane, and where
the parameters (µ1, µ2, µ3, µ4) lie on a sphere and cannot be zero simultaneously,
and (a, b) ∈
 := {(a, b) ∈ R2 | a ≥ 0, a2 + 4b − 4 < 0}, see Figure 2.
In some cases instead of working on a sphere, we prefer to work in one of
the charts of the sphere: µ4 = 1 and (µ1, µ2, µ3) ⊂ K ⊂ R3, that is, we can
consider the system
{ _x = ax2 + bxy + µ1 + µ2x + µ3y,
_y = x2 + y2 − 1, (7)

6

Figure 2: Region of the parameters a and b.

Figure 3: Phase portrait of system (6) for the unperturbed one (left) and near the inﬁnity
(right).

where (x, y) lies in a large compact set in the plane, (a, b) ∈
, and ( µ1, µ2, µ3) ⊂
K ⊂ R3 with K a large compact set as well. By choosing to work in this chart,
we avoid the situation where µ4 ≈ 0 and (µ1, µ2, µ3) lies on a unit sphere. This
choice is made for the sake of convenience and because it is to be expected
that no additional phenomena are present there. With techniques similar to
the ones proposed here, and by using extra desingularizations (blow-ups), a
comprehensive study of the parameter chart µ4 ≈ 0 is equally possible.

Following the techniques described in [11] the phase portraits near the in-
ﬁnity of the unperturbed and perturbed system (6) is drawn in Figure 3. In
particular the limit cycles will appear in a compact region K in the phase space,
in correspondence with the ﬁndings in Lemma 3. Moreover the total index of
ﬁnite singularities is zero because the index of the fake saddle singularity of the
unperturbed system (6) is also zero.

3. Limit cycles bifurcating from singularities

This section is devoted to the research of limit cycles that bifurcate from
singularities. From previous section we know that the total index of the ﬁnite

7

singularities is 0. This research is divided in two subsections. In the former
we will study the maximum order of a weak focus (index +1). The latter deals
with the study of Bogdanov–Takens bifurcation (index 0). In both cases we ﬁrst
study each point separately and afterwards the simultaneous bifurcation.

3.1. Bifurcation from weak foci
Let X be the vector ﬁeld associated to system (6). Then its linearization
matrix at a point (x, y) is

DX(x, y) =
 ( 2ax + by + µ2 bx + µ3

2x 2y
 )
 .

Thus, the trace and the determinant of DX(x, y) are denoted by

tr DX(x, y) = 2(ax + by) + (2 − b)y + µ2, (8)

det DX(x, y) = 4y(ax + by) − 2b(x2 + y2) − 2µ3x + 2µ2y. (9)

Lemma 5. For a weak focus (x0, y0) of system (6) we have:

(i) The value x0 is nonzero.

(ii) The ﬁrst Lyapunov quantities are given by

V3 = − v30 − v31 a − v32 a
2

8 x0 α5
0 , (10)

V5 = − 2x0y0v50 + v51 a + x0y0v52 a
2 − v53 a
3

16 x3
0 α7
0 , (11)

where α0 is the positive square root of det DX(x0, y0), and

v30 = 2x0y0(b + 2) (4(1 − b)x2
0 + α2
0 + 4y2
0) ,

v31 = (α2
0 + 4y2
0)2 − 2b (12y2
0 + α2
0) x2
0,

v32 = 4x0y0(α2
0 + 4y2
0),

v50 = (2x2
0 + 4y2
0 + α2
0)(4x2
0 + 4y2
0 + α2
0)(b + 2),

v51 = 8(b − 2)(b − 3)x6
0 + (112(2 − b)y2
0 + 2α2
0(b
2 + 10 − 9b)) x4
0
− 2(4y2
0 + α2
0) (α2
0(1 + b) − (13b + 14)y2
0) x2
0 − (4y2
0 + α2
0)
3,

v52 = 48bx
4
0 − ((32 − 152b)y2
0 + 2α2
0(4 − b)
) x2
0 − 13(4y2
0 + α2
0)2,

v53 = 12x2
0(x2
0 + 3y2
0)(4y2
0 + α2
0).

Proof. When x0 = 0 we have

tr DX(0, y0) = µ2 + by0 + 2y0 = 0,

det DX(0, y0) = 2y0(by0 + µ2) = −4y2
0 ≤ 0.

8

Consequently (0, y0) is not a weak focus (see [24]). This proves (i).
For proving statement (ii), we will ﬁrst use a suitable linear transformation
to bringing system (6) in its Poincar´e normal form.

By hypothesis tr DX(x0, y0) = 0 and det DX(x0, y0) = α2
0 for a value α0 > 0.
Hence, from (8) and (9) it follows that

µ2 = −2(ax0 + by0) − y0(2 − b) and µ3 = − 2bx
2
0 + α2
0 + 4y2
0
2x0 .

On the other hand, since (x0, y0) is a singular point, from (6) we can easily see
that
 µ1 = 2x2
0 (ax0 + 2y0) + 2bx
2
0 + α2
0 + 4y2
0
2x0 and µ4 = (x2
0 + y2
0).

By using the linear transformation

u = x0(x − x0) + y0(y − y0)
x0 , v = α0(y − y0)
2x0

and the time reparametrization dτ = α0 dt, the system (6) becomes
{ u
′ = −v + a20 u
2 + a11 uv + a02 v2,
v′ = u + b20 u
2 + b11 uv + b02 v2, (12)

where the prime denotes the derivative with respect to τ , and

a20 = ax0 + y0
x0 α0 , a11 = 2bx2
0 − 4y0(y0 + ax0)
x0 α2
0 ,

b20 = 1
2x0 , a02 = 4y0 (y0(y0 + ax0) + x2
0(1 − b)
)

x0 α3
0 ,

b11 = 2y0
x0 α0 , b02 = 2 (x2
0 + y2
0)

x0 α2
0 .

The origin of this system corresponds to the point (x0, y0) of (6).
Finally, the expressions of the Lyapunov quantities V3 and V5 given in (10)
and (11) follows after rewriting system (12) as

z′ = iz + Az2 + Bz z + C z2,

(with z := u + iv), applying [25, Proposition 1.2] and simplifying V5|V3≡0.

Theorem 6. Let (x0, y0) be a weak focus of the perturbed system (6).

(i) if a ̸= 0, then (x0, y0) is of order at most 2.

(ii) if a = 0, then (x0, y0) is of order at most 1 if y0 ̸= 0 and b ̸= −2; otherwise
(x0, y0) is a center.
 9

Proof. (i) It sucient to show that if V3 = 0, then V5 ̸= 0. This follows if
the resultant of the numerators of V3 and V5 respect to y0 is a non-vanishing
function. This resultant factors as

Res(V3, V5, y0) = a10α16
0 x20
0 (b − 2)
2R1R2
2R3,

where
 R1 = 4(a
2 + b2)x2
0 + b2α2
0, R2 = 2a
2b + (b − 1)(b + 2)2

and
 R3 = 5(3 − b)(3(b + 1)a
2 + 4(2b − 1)2)x2
0 + α2
0(10b − 5 + 3a
2)2.

By the assumption a > 0, and the fact x0 ̸= 0 (Lemma 5), it is clear that
R1 > 0. To complete the proof we will prove that R2 and R3 do not vanish in

. If (a, b) ∈
, then a
2 < −4(b − 1). Thus, R2 < (b − 1)(b − 2)2 < 0 in

because b − 1 < 0 and b − 2 < −1 in
.
Showing that 3(b + 1)a
2 + 4(2b − 1)
2 and 3 − b are positive in
 , is sucient
to show that R3 > 0 in
 because x0 ̸= 0. If (a, b) ∈
, then it is clear
that 3 − b > 0. Moreover, if b ≥ −1, then b + 1 ≥ 0, which implies that
3(b + 1)a2 + 4(2b − 1)2 > 0; and if b < −1, then −4ba
2 < −16b(b − 1), whereby

3(b + 1)a
2 + 4(2b − 1)2 = 3(b + 1)a
2 − 16b(1 − b) + 4 > 3a
2 − ba
2 > 0.

(ii) We consider the equivalent system (12). For a = 0, the Lyapunov
quantity V3 simpliﬁes to

V3 = y0 (2 + b) (4(1 − b)x2
0 + α2
0 + 4y2
0)

4α5
0 .

Since in
 we have 1 − b > 0, the polynomial 4(1 − b)x2
0 + α2
0 + 4y2
0 is positive
because α0 > 0. Hence, as we are assuming that y0 ̸= 0 and b ̸= −2 we can
conclude that V3 ̸= 0. Therefore, the origin of (12) or equivalently the weak
focus (x0, y0) of (6) is of order at most 1.
To complete the proof we will prove that if y0 = 0 or b = −2, then (x0, y0)
is a center. We will consider two cases.

Case 1. Suppose y0 = 0. From the expression of (6) we get that µ1+µ2x0 = 0
because a = 0. On the other hand, from (8) we obtain tr DX(x0, 0) = µ2, which
is zero because (x0, 0) is a weak focus. Thus, we obtain µ1 = µ2 = 0. Hence the
system (6) becomes { _x = y(bx + µ3),
_y = x2 + y2 − µ4. (13)

Thus, from (9) it follows that det DX(x0, 0) = −2(bx2
0 + µ3x0) which must be
positive because (x0, 0) is a weak focus. Hence b2 + µ
2
3 ̸= 0. We will prove that
this system has a ﬁrst integral.
 10

When b = 0 we can assume that µ3 ̸= 0 and e−2x/µ3 is an integrating factor
that provides µ3 (2µ4 − 2y2 − µ
2
3 − 2xµ3 − 2x2)

4 e2x/µ3
as a ﬁrst integral, which has either a minimum or a maximum at (x0, 0). There-
fore (x0, 0) is a center of the system.
If b ̸= 0, then (bx + µ3)
−(b+2)/b is an integrating factor and, consequently,

(b − 2)(x2 + (y2 − µ4)(1 − b)) − µ
2
3 − 2xµ3

2(b − 1)(b − 2) (bx + µ3)
 2
b

is a ﬁrst integral. Hence, if (x0, 0) is a weak focus for the system, then the
ﬁrst integral has either a minimum or a maximum at (x0, 0) which implies that
(x0, 0) is a center.

Case 2. Suppose b = −2. From (8) we get tr DX(x0, y0) = µ2, which must
be zero by the assumption on (x0, y0). Thus (6) becomes
{ _x = −2xy + µ1 + µ3y,
_y = x2 + y2 − µ4, (14)

which is a Hamiltonian system with Hamiltonian function

H(x, y) = x3

3 + xy2 − µ3
2 y2 − µ4x − µ1y.

Therefore, if (x0, y0) is a weak focus of the system, it is a center.

Corollary 7. If a ̸= 0 then the perturbed system (6) has no centers bifurcating
from the origin of the unperturbed system.

Theorem 8. If system (6) has two simultaneous weak foci, then each one of
them has order at most one.

Proof. If a = 0, then the assumption follows from statement (ii) of Theorem 6.
Hence, for the rest of the proof we assume that a ̸= 0.
Let (x0, y0) and (x1, y1) be two dierent weak foci of system (6). As they
are singular points, and from (8), (9) we have

ax2
i + bxiyi + µ2xi + µ3yi = 0,

x2
i + y2
i − µ4 = 0,

µ2 − (2axi + (b + 2)yi) = 0,

α2
i − 2xiµ3 + 2bx
2
i + 4y2
i = 0,

where αi = det DX(xi, yi) > 0 for i = 0, 1. From these expressions we can write
µ1, µ2, µ3, µ4, x1, y1, α0, and α1 as functions of (x0, y0, a, b). In particular we get

x1 = (4a
2 − (b + 2)2)x0 + 4a(b + 2)y0
4a2 + (b + 2)2 ,

y1 = 4a(b + 2)x0 − (4a
2 − (b + 2)2) y0
4a2 + (b + 2)2 .

11

We denote by Vj0 and Vj1 the Lyapunov quantities of the weak focus (x0, y0)
and (x1, y1), respectively. We note that the expression of Vj1 for j = 3, 5 comes
from (10) and (11) in Lemma 5 if we replace x0, y0, and α0 by x1, y1, and α1,
respectively. In particular,

V30 = ̃V x0((b + 2)x0 − 2ay0)
2

α5
0(4a2 + (b + 2)2)2

and
 V31 = ̃V ((4a
2 − (b + 2)2)x0 + 4a(b + 2)y0)((b + 2)x0 − 2ay0)2

α5
1(4a2 + (b + 2)2)3

where ̃V = −a(b − 2)(2ba
2 + 3b
2 + b3 − 4).
We note that if (b + 2)x0 − 2ay0 = 0, then that implies that y1 = y0 and
x1 = x0, which contradicts our assumption (x0, y0) ̸= (x1, y1). Hence we have
(b + 2)x0 − 2ay0 ̸= 0.
On the other hand, it is easy to see that the zero locus of ̃V is outside of

 \ {a = 0}, and we know that x0 ̸= 0 and x1 ̸= 0, that is, (4a
2 − (b + 2)2)x0 +
4a(b + 2)y0 ̸= 0. Moreover, this implies that V30 ̸= 0 and V31 ̸= 0. Therefore,
(x0, y0) and (x1, y1) are weak foci of order at most one.

3.2. Bifurcation from nilpotent cusps

We consider cusp singularities in (7), i.e. singularities (x0, y0) where the
determinant and the trace of the linearization is zero, but the linearization itself
is not. It is an elementary computation to show that nilpotent singularities are
located at (x0, y0) = (cos θ, sin θ) when

µ1 = a cos2 θ + (2 + b cos2 θ) tan θ, (15)

µ2 = −(b + 2) sin θ − 2a cos θ, (16)

µ3 = (2 − b) cos θ − 2 cos
−1 θ. (17)

Proposition 9. Around a nilpotent singularity and for any N ≥ 2, there exists
a local set of coordinates bringing (7) locally in the normal form




 _x = y,

_y = N∑

k=2
 (rkxk + skxk−1y) + O(∥(x, y)∥
N +1),

where in particular

r2 = 4 tan θ(1 + a sin θ cos θ − b cos2 θ), s2 = 2b cos θ − 4a sin θ + 4 cos θ.

The two coeﬃcients r2 and s2 vanish only simultaneously when both b = −2 and
θ = 0 (mod π).
 12

Proof. This proposition is even valid up to N = ∞ (this is a reduction to
Li´enard form, see for example [22]), and is well-known. Here we restrict to
giving the procedure to normalize up to cubic terms, the general case being a
direct generalization. We ﬁrst write (x, y) = (~y+x0, ~x+y0) to put the singularity
at the origin. Notice the exchange of the roles of x and y to go towards normal
form. After this, a linear change of coordinates (~x, ~y) = (2 cos θ x, −2 sin θ x + y)
changes the linear part to ( 0 1
0 0 ). Finally, we write

x = X + a2X 2, y = Y + b0X 2 + b1XY + b2Y 2

and for suitable choices of (a2, b0, b1, b2) (easily found with the help of a symbolic
math program) one can eliminate the quadratic terms in _X and the term with
y2 in the _Y -equation. Let us ﬁnally mention that the system of equations
{r2 = 0, s2 = 0} is solved when either sin θ = 0 (in which case b = −2 follows) or
b = 2+2 cos−2 θ > 2, which is out of the parameter regime that we consider.

When both r2 and s2 are nonzero, the nilpotent singularity is of codimension
2, and upon varying the parameters it unfolds in a complete Bogdanov–Takens
diagram. This is easy to see: the trace at the singular point is given by 2ax+(b+
2)y + µ2, and a similar expression is found for the determinant at the nilpotent
point. Computing the Jacobian determinant of the mapping (x0, y0, µ1, µ2) ↦→
( _x, _y, tr, det)|x=x0,y=y0, evaluated at a point (x0, y0) = (cos θ, sin θ), and given
the conditions (15), (16), and (17), gives −4 tan θ((b − 2) cos
2 θ − 2) ̸= 0 in the
parameter domain under study and when θ ̸= 0. In other words when θ ̸= 0, the
two parameters (µ1, µ2) can be used as versal parameters completely unfolding
the nilpotent point. We conclude that (7) contains all elements appearing in
Bogdanov–Takens diagrams.

Remark 10. Similarly, the mapping (x0, y0, µ1, µ2) ↦→ ( _x, _y, tr, det)|x=x0,y=y0
is easily veriﬁed to be regular at nilpotent singularities, especially when µ2 =
µ3 = 0, i.e. the case that appears in the reversible system (2). This shows that
not only cusp singularities appearing in (2) unfold in full Bogdanov–Takens
diagrams, but they even do so inside the family (2).

Moreover, we can show that simultaneous BT-bifurcations occur:

Proposition 11. A nilpotent singularity (x0, y0) = (cos θ, sin θ) occurs simulta-
neously with another nilpotent singularity at (x1, y1) = (cos φ, sin φ) only when
θ = φ + π (mod 2π) and

a = (2 sin
2 θ − 1) sin θ
cos3 θ , b = −2 tan
2 θ, µ1 = tan θ, µ2 = µ3 = 0.

The quadratic normal forms of Proposition 9 at both points are then the same,
and r2 = 4 sin θ cos−3 θ and s2 = 4(1 − 2 sin
2 θ) cos
−3 θ. In the parameter do-
main {a ̸= 0}, simultaneously occurring nilpotent singularities are always of
codimension 2 and they unfold completely and independently upon varying the
four parameters (a, b, µ2, µ3). In particular this implies the presence of two
small-amplitude limit cycles or saddle-homoclinics near the two cusp singular
points.
 13

Proof. We express ( _x, _y, tr, det) at (x0, y0) and at (x1, y1) and get a system of 8
polynomial equations, which we consider in variables (y0, x1, y1, a, b, µ1, µ2, µ3),
and treating for example x0 = cos θ as a parameter. A cumbersome compu-
tation shows that (x0, y0) necessarily equals (cos θ, sin θ) and (x1, y1) equals
(cos φ, sin φ) with φ = θ or φ = θ + π. From the same computation, we de-
rive expressions for a and b, and using those expressions, we can simplify the
known expressions for the quadratic coecients r2 and s2. It is clear that
r2 · s2 = 0 only when a = 0. Finally, assume φ = θ + π and both points are
nilpotent. Computing ( _x, _y, tr, det) at both points (x, y) = (cos θ, sin θ) and
(x, y) = (− cos θ, − sin θ) leads to a map from (x0, y0, x1, y1, a, b, µ2, µ3) into R8.
The Jacobian determinant of this map can be easily veriﬁed to be nonzero which
implies that (a, b, µ2, µ3) independently control the two bifurcation parameters
of the Bogdanov–Takens bifurcation plane for both points.

Two simultaneously appearing nilpotent singular points of codimension > 2
hence could occur only along a = 0. Let us ﬁnally state a result concerning
the maximal codimension of any appearing nilpotent singularity in our system
through the next two propositions:

Proposition 12. A nilpotent singularity for which r2 = 0 and s2 ̸= 0 is of at
most codimension three and around this point, (7) can be locally brought into
the normal form
{ _x = y,
_y = s2xy + r3x3 + ~s3x2y + O(∥(x, y)∥
5),

with s2 as before and nonzero r3 = 4(b − 2) and with ~s3 = s3 − 3s2r4/(5r3). The
singularity is of nilpotent saddle, focus or elliptic type (see [15]), depending on
parameters (s2, ~s3, r3).

Proof. Starting from the Li´enard form up to some degree N ≥ 5, one can
consider yet another transformation

x = X + c2X 2 + c3X 3.

A time change allows to keep _X = y. Tracking down the eect on the _ y equation,
we can choose c2 and c3 to annihilate the terms of order 4. With this change, a
term of order 3 however changes from s3x2y to ~s3x
2y. The explicit expression for
r3 is obtained exactly like r2 and s2 are obtained in the proof of Proposition 9.
(In fact, one ﬁnds that r3 = 8a sin θ cos θ + 4b(2 sin
2 θ − 1) which simpliﬁes to
4(b − 2) along r2 = 0.)

Proposition 13. At a nilpotent singularity for which s2 = 0 and r2 ̸= 0 (7)
can be locally brought into the normal form
{ _x = y,
_y = r2x2 + ~s4x
3y + O(∥(x, y)∥5),

with ~s4 = s4 − s3r3/r2. Except when (a, b) = (0, −2), ~s4 is never zero together
with s2 in the relevant parameter domain.

14

Proof. Just like in the previous proposition, we start with the Li´enard form up
to some degree N ≥ 5, and we consider x = X +c2X 2+c3X 3, this time combined
with y = Y + d2Y 2 + d3Y 3. A time rescaling again allows to keep _X = Y , and
the coecients c2, c3, d2, d3 are determined in order get _Y in the required form.
The exact expression for ~s4 is quite long and we have chosen not to include it,
as there are precise instructions on how to compute it. Algebraically, there are
two disjoint curves where ~s4 = s2 = 0, both of them lie outside the domain
{b < 1, a
2 + 4(b − 1) < 0}.

We leave it to the interested reader to check whether or not a versal unfolding
of the two above treated codimension 3 situations are found in (7). Versal
unfoldings of the situations described in Propositions 12 and 13 are found in
[15] and [14], respectively. For (a, b) = (0, −2), and for

(µ1, µ2, µ3) = ( 2 sin
3 θ
cos θ , 0, 2 cos 2θ
cos θ
 ) ,

the normal form in the above proposition around the singular point (x0, y0) =
(cos θ, sin θ) degenerates further as ~s4 = 0, and the study remains inconclusive.
It is easy to conclude that topologically, the singularities are cusps, but the
unfolding is less clear. From the previous section, we know however that since
also µ2 = 0, the system is Hamiltonian in that case.

4. Conﬁguration of centers and their perturbations

This section deals with the centers of the family (7) and a review of known
results about their quadratic perturbations.

Proposition 14. System (7) can have a center only if it has the form
{ _x = y(bx + µ3),
_y = x2 + y2 − 1, with b < 1 and µ3 ∈ R; (18)

or { _x = −2xy + µ1 + µ3y,
_y = x2 + y2 − 1, with µ1, µ3 ∈ R. (19)

The bifurcation diagrams of systems (18) and (19), as well as their diﬀerent
topological phase portraits on the Poincar´e disc, are shown in Figures 4 and 5,
respectively. In particular,

(i) system (18) has a center if and only if

(µ3, b) ∈ {b < 1} ∩ ({µ3 − b > 0} ∪ {µ3 + b < 0}) ⊂ R2, and

(ii) system (19) has a center if and only if

(µ1, µ3) ∈ {µ
2
1 < 1} ∪ ({D < 0} ∩ {µ1 ≥ 1}) ⊂ R2,

where D = 64µ
4
1 + µ
2
1 (µ
4
3 − 80µ
2
3 − 128) − (µ3 − 2)3(µ3 + 2)3.

15

µ3

b

I0 I1 I2 I3 I4

I0

I1I2 I2

I3
 I3 I3
 I3

I4
 b = 1

µ3 = −bµ3 = b
 Figure 4: Bifurcation diagram of system (18) and its diﬀerent topological phase portraits.

µ1

µ3

H 0

H 1

H 2

H 3 H 4 H 5 H 6

H 0
 H 0

H 1

H 1 H 1

H 1

H 2
 H 2

H 3

H 3
 H 3

H 3

H 4

H 4 H 4

H 4

H 5
 H 5

H 6
Figure 5: Bifurcation diagram of system (19) and its diﬀerent topological phase portraits.
The curve D = 0 is drawn as a continuous line.

16

From this result we can classify the centers in three families: The non-
reversible Hamiltonian ((19) with µ1 ̸= 0), the reversible Hamiltonian ((18)
with b = −2 or (19) with µ1 = 0), and the reversible non-Hamiltonian ((18)
with b ̸= −2). As we show in the proof below, if the Hamiltonian associated
with (19) has four or two dierent real singular points, then it has four singular
values (in the complex plane) for µ1 ̸= 0, then from [17] we have that at most
two limit cycles can born from H3 and H5 under quadratic perturbations; in
particular the cyclicity of the period annuli is at most 2. Moreover, in [21] is
proved that the cyclicity of the period annulus of H4 is at most 2. The reversible
Hamiltonian is studied in [4] proving that again the cyclicity of the period annuli
of H6 is two, when both are considered separately or simultaneously. However,
the global cyclicity of H4 and H6 cannot be determined since simultaneously
limit cycles could bifurcate from the cusp or from the heteroclinic connections,
respectively. This problem remains open. The cyclicity of the period annuli in
the reversible non-Hamiltonian case only have been considered in few particular
cases and in all the cases again the cyclicity is two. See [3, 5, 16, 20].

Proof of Proposition 14. From the proof of Theorem 6 we obtain that system
(6) can have a center only if it writes as (13) or (14) which, after the rescaling
introduced in Section 2.3, become (18) and (19), respectively. Moreover, by
applying the map (x, y, t) → (−x, −y, −t) we can assume, if necessary, µ3 ≥ 0
in systems (18) and (19). Finally, as the singularities at inﬁnity are hyperbolic
we restrict our analysis to the ﬁnite singularities that globally have total index
zero, see Section 3.
We ﬁrst study the bifurcation diagram and the phase portraits for system
(18) considering the division of the parameter space according to the number
and type of its singularities.
If b = µ3 = 0, then the circle x2 + y2 = 1 is a curve of singularities of the
system, and every vertical straight line is invariant. Thus, the phase portrait is
topologically conjugated to I0 in Figure 4.
For the remaining cases the points (−1, 0) and (1, 0), the intersection points
of y = 0 with the circle x2 + y2 = 1, are ﬁnite singularities of the system.
Moreover, the system can have two additional singularities (−µ3/b, yi) for i =
1, 2 with y1 > 0 and y2 < 0, which are the intersection points of the invariant
straight line x = −µ3/b with the circle x2 + y2 = 1.
The next table shows the classiﬁcation of the singularities of the system.

(−1, 0) (1, 0) (− µ3
b , y1) (− µ3
b , y2)
I1 saddle saddle unstable node stable node
I2 h−e saddle – –
I3 center saddle – –
I4 center center saddle saddle

where h−e means one hyperbolic sector and one elliptic sector,

I1 = {(µ3, b) | b < 1, b > µ3}, I3 = {(µ3, b) | b < 1, |b| < µ3, −b = µ3},

I2 = {(µ3, b) | b < 1, b = µ3}, I4 = {(µ3, b) | b < 1, µ3 < −b}.

17

See Figure 4.
The proof of the above classiﬁcation follows from the Hartman–Grobmann
Theorem for hyperbolic singularities and from Theorem 6 for centers. This
ﬁnishes the local study of the phase portraits in regions I1, I3 for µ3 ̸= −b, and
I4. The same can be applied for (1, 0) in I2 and (−1, 0) in I3 when µ3 = −b.
The remaining cases, i.e. (1, 0) in I3 with µ3 = −b and (−1, 0) in I2, are
nilpotent singularities. For determining the local behavior we must apply the
results about the characterization of nilpotent singularities. See Section 3.4 and
Theorem 3.5 in [11]. Alternatively, see [1, Ch. IX, Theorem 66].
The local phase portraits of the singularities determine the global ones for
regions I2 and I3. The global phase portraits for regions I1 and I4 are deter-
mined by using the local phase portraits of the singularities and the existence
of the invariant straight line x = −µ3/b. See Figure 4.

Secondly, we will study the bifurcation diagram and the phase portraits for
system (19), which is a Hamiltonian system with Hamiltonian function

H(x, y) = x3

3 + xy2 − µ3
2 y2 − x − µ1y. (20)

As in previous case, we ﬁrst divide the parameter space into regions according
to the number of singularities. This can be done studying the intersection points
of the two components of the vector ﬁeld. That is a hyperbola or the product
of two straight lines with the unit circle. Consequently the number of ﬁnite
singularities is 0, 1, 2, 3, 4. Alternatively, such a division is given by the zero-
locus of the discriminant of the resultant between the components of the vector
ﬁeld:
 (Res( −2xy + µ1 + µ3y, x
2 + y2 − 1, x), y) =

(4 y4 + (µ
2
3 − 4)y2 + 2µ1µ3y + µ
2
1, y) =

256µ
2
1(64µ
4
1 +µ
2
1 (µ
4
3 −80µ
2
3 −128)−(µ
2
3 − 4)3) = 256µ
2
1D(µ1, µ3).
 (21)

See Figure 5.
We will describe the phase portraits and the bifurcation diagram in terms
of the number of singularities. For simplicity each region and the corresponding
phase portrait are denoted by the same symbol.
In H0 = {D > 0, |µ1| > 1} the conics do not intersect. Consequently, there
are no ﬁnite singularities and the phase portrait is topologically equivalent to
H0 in Figure 5.
The conics are tangent in only one point in H1 = {D = 0, |µ1| > 1}. The
unique singularity is nilpotent and it is a cusp point, because the vector ﬁeld
is Hamiltonian. The global phase portrait is topologically equivalent to H1 in
Figure 5.
When there are at least two singularities we prove that the value of the
Hamiltonian on two of them coincide only when µ1 = 0. Hence, only in this case,
two singularities can be connect by an invariant curve. Writing the singularities

18

as
 (xi, yi) = ( 1 − t2
i
1 + t2
i , 2ti
1 + t2
i
 ) , i = 1, 2,

with t1 ̸= t2, the values of µ1 and µ3 are uniquely determined in terms of t1, t2.
Thus, the dierence of the Hamiltonian at these points is

4(t1 + t2)
(((3t
2
1 + 1)t2 − 2t1)
2 + 3(t2
1 + 1)2)(t1 − t2)
3

3(t2
1 + 1)3(t2
2 + 1)3(3t2
1 + 1) ,

which vanishes only when t1 = −t2, that is x1 = x2 and y1 = −y2, or equiva-
lently µ1 = 0.
There are two dierent situations with two singular points. The ﬁrst, in
H2 = {µ1 = ±1, µ3 = 0}, when the conics are tangent in two dierent points
and the second, in H3 = {D < 0}∪{µ3 = ±2, µ1 = 0}, when the conics intersect
transversally. In H2 the singularities are of cusp type, using the same argument
as in region H1, and the global phase portrait is topologically equivalent to
H2 in Figure 5 because the cusps are not connected. In H3 as the system
is Hamiltonian both singularities are simple, because the transversality, and of
index +1 and −1, respectively. Consequently, they are of saddle and center type,
the global phase portrait is totally determined and it is topologically equivalent
to H3 in Figure 5.
In H4 = {D = 0, 0 < |µ1| < 1} the conics intersect in two transversal points
and one tangent. The local behavior of these points is the same as the equivalent
points in the previously studied cases. Then there are a cusp, a saddle and a
center point. As the Hamiltonian at the cusp and the saddle does not coincide,
the global phase portrait is topologically equivalent to H4 in Figure 5.
The remaining cases are the ones with four singularities. As the conics inter-
sect transversally, the system is Hamiltonian and the total index is 0, we have
two points with index +1 (centers) and two with index −1 (saddles). The global
phase portrait depends on the value of the Hamiltonian at the saddle points.
These value do not coincide in region H5 = {D > 0, 0 < |µ1| < 1} and hence
the saddles are disconnected. They coincide in region H6 = {µ1 = 0, |µ3| < 2}.
Additionally, in the last region, the system has a vertical invariant straight line
that connect the saddles. The global phase are topologically equivalent to H5
and H6 in Figure 5, respectively.

5. Singular perturbations

We consider { _x = ε(ax2 + bxy + µ1 + µ2x + µ3y),
_y = x2 + y2 − 1, (22)

where ε is a small perturbation parameter. This system is obtained from (7)
after rescaling the parameters by ε (and using the same symbols for the rescaled
variants). Note that (εa, εb) ∈
 when ε ≥ 0 is small enough.

19

This kind of systems will be studied using techniques from geometric singular
perturbation theory. This consists of studying two limiting systems
{ _x = 0,
_y = x2 + y2 − 1, and { _x = ax2 + bxy + µ1 + µ2x + µ3y,
0 = x2 + y2 − 1,

These two systems are called the fast reduced system and the slow reduced
system. We deﬁne C = {(x, y) : x2 +y2 = 1} as the critical curve, a circle. Away
from the singular points of the fast system, i.e. away from C, the dynamics of
(22) is a perturbation of the dynamics of the fast system, whereas close to C,
the dynamics of the slow system plays a role. Of interest in C are two so-called
contact points, located at (x, y) = (±1, 0). There, C is tangent to the vertical
ﬁbers of the fast subsystem, and the fast vector ﬁeld has a nilpotent singular
point (at other points of C, we have a partially hyperbolic singular point).
The presence of contact points allows the possibility of existence of slow-fast
cycles of canard type. Before checking the conditions on the presence of canard
cycles in detail, we prepare the computations by presenting expressions in polar
coordinates. In polar coordinates (x, y) = (r cos θ, r sin θ), we have




 _r = (r2 − 1) sin θ + ε R(r, θ) cos θ,

_θ = r2 − 1
r cos θ − ε
r R(r, θ) sin θ,

with R(r, θ) = ar2 cos2 θ + br2 cos θ sin θ + µ1 + µ2r cos θ + µ3r sin θ. Around
partially hyperbolic points of C, the critical curve C perturbs to an ε-dependent
invariant manifold. Using formal methods, it is easy to see that such invariant
manifolds have the expression

r = 1 − ε cos θ
2 sin θ (a cos2 θ + b cos θ sin θ + µ1 + µ2 cos θ + µ3 sin θ) + O(ε2).

Note that the invariant manifolds potentially break down when sin θ = 0, e.g. at
the contact points. For canard solutions to exist around the point (x, y) =
(+1, 0), it is clear that a + µ1 + µ2 = o(1) as ε → 0. We will prove in the next
lemma that this is indeed a necessary condition. The fast subsystem is simply
the reduction to ε = 0, while the slow subsystem can now be expressed in terms
of θ: _θ = − a cos2 θ + b cos θ sin θ + µ1 + µ2 cos θ + µ3 sin θ
sin θ .

(We have plugged in the expression for the invariant manifold into the vector
ﬁeld to obtain this formula.) Checking near θ = 0, this yields

_θ = − a + µ1 + µ2
θ − (b + µ3) + O(θ). (23)

We have already obtained heuristically that the ﬁrst term should be zero, in
that case it is clear that the second term should be positive: for a periodic orbit
of slow-fast type to appear, the orbit has to go up along the circle slowly, and
then go along a fast vertical ﬁber downwards to close the loop. These heuristical
remarks can be made exact:
 20

Lemma 15. There exists a smooth function λ+(ε, a, b, µ1, µ2, µ3) that evaluates
to 0 at ε = 0 and such that system (22) has canard cycles around (x, y) = (+1, 0)
when a + µ1 + µ2 = λ+, b + µ3 < 0. (24)

There exists a smooth function λ−(ε, a, b, µ1, µ2, µ3) that evaluates to 0 at ε = 0
and such that system (22) has canard cycles around (x, y) = (−1, 0) when

a + µ1 − µ2 = λ−, b − µ3 < 0. (25)

Proof. We write (x, y) = (1 + ~y, ~x) and consider
{ _~x = 2~y + ~x2 + ~y2,
_~y = ε
((a + µ1 + µ2) + (b + µ3)~x + (µ2 + 2a + b~x)~y + a~y2).

A well-known trick is to simply replace a + µ1 + µ2 by a new parameter which
we call λ: { _~x = 2~y + ~x2 + ~y2,
_~y = ε(λ + (b + µ3)~x + (µ2 + 2a + b~x)~y + a~y2).

The dynamics in the new system will be found back in the original system when
we restrict to λ = a + µ1 + µ2. In this form we can readily apply Theorem 4 of
[7]. It is easy to verify that under the conditions of Lemma 15, all conditions
of this theorem are veriﬁed. It implies the existence of canard cycles. Similarly
near (x, y) = (−1, 0).

Using the implicit function theorem, we can for example explicitly write µ1
in terms of the other parameters so that (24) is satisﬁed, thereby showing the
presence of canard cycles around (x, y) = (+1, 0). Similarly for the left contact
point. Also, considering (24 − −25) as a system of equations, the same implicit
function theorem allows to ﬁnd an implicit solution writing (µ1, µ2) in terms of
the remaining parameters (a, b, µ3, ε).
Lemma 15 shows the presence of small-amplitude canard cycle near the
contact point. They consist of (a perturbation of) a fast vertical path connecting
(x, y) = (cos θ0, sin θ0) and (x, y) = (cos θ0, − sin θ0), (for θ0 ≈ 0 or θ0 ≈ π)
together with a small arc on the circle. The stability of the obtained periodic
orbits can be computed using a slow divergence integral, see [6]. This integral
is the divergence of the fast vector ﬁeld, integrated along the slow arcs, and it is
well-known that it can be computed in arbitrary coordinate systems. In polar
coordinates the divergence is given by 2y + O(ε) = 2 sin θ + O(ε), so we deﬁne

I+(θ0) = − ∫ θ0

−θ0
 2 sin
2 θ
a cos2 θ + b cos θ sin θ + µ1 + µ2 cos θ + µ3 sin θ dθ.

as the slow divergence integrals of slow-fast cycles around the contact point
(x, y) = (+1, 0), and

I−(θ0) = − ∫ θ0

2π−θ0
 2 sin
2 θ
a cos2 θ + b cos θ sin θ + µ1 + µ2 cos θ + µ3 sin θ dθ.

21

for slow divergence integrals of slow-fast cycles around (−1, 0). It is clear that
these expressions only make sense when the integrand is well-deﬁned for θ in
the integration interval. We can now prove:

Proposition 16. Coexistence of canard cycles around slow-fast Hopf points in
a (1 : 1) conﬁguration in (22) occurs for any choice of (a, b, µ3) with b < 0
and |µ3| < |b|, conveniently choosing (µ1, µ2) in terms of (ε, a, b, µ3) and of the
size of the cycles. In case of coexisting canard cycles, one always has a (1 : 1)
conﬁguration when a ̸= 0.

Proof. From Lemma 15, we know that b < 0 and |µ3| < −b for coexisting canard
cycles to appear. Letting θ+ ∈ (0, π) be an angle uniquely deﬁning a canard
cycle passing near the contact point (x, y) = (+1, 0), and letting θ− ∈ (0, π) be
an angle uniquely deﬁning a canard cycle passing near (x, y) = (−1, 0). Then
Lemma 15 states that µ1 and µ2 are determined in terms of θ+ and θ− (and
the other parameters), and that (µ1, µ2) = (−a, 0) + o(1). The slow divergence
is given by
 I+(θ+) = − ∫ θ+

−θ+
 2 sin θ
µ3 + b cos θ − a sin θ dθ,

(with a similar expression for I−(θ−)). Observe that ∂
∂a I+(θ+) is strictly positive
and that I+(θ+) = 0 at a = 0, which implies that the slow divergence integral
has a ﬁxed sign along θ+. It follows, for a ̸= 0, from results in [8] and [10] that
the number of canard cycles around the contact point (x, y) = (+1, 0) is one,
i.e. we cannot have more than one canard cycle in each nest. Similarly for the
contact point at (x, y) = (−1, 0).

In case a = 0 the coexisting canard cycles appear along µ1 = µ2 = 0; in that
case we have a symmetric vector ﬁeld, corresponding to the singularly perturbed
center case. While the slow-fast center case has been studied before and the tools
from slow divergence integral can be used, the degenerate situation that appears
in this context also needs to be studied when there are extra singularities in the
slow dynamics (i.e. µ3 + b cos θ+ − a sin θ+ = 0). Though known results could be
extended to such situations, there is no direct result to fall back on. We have
therefore decided to exclude the case a = 0 from the slow-fast study, while it is
clear that there is not to be expected any phenomenon dierent from the case
a ̸= 0.

In the remainder we check the presence of a nest of N ≥ 2 canard cycles
around one of the contact points. In short we show that N = 2 appears and
that it is the most logical upper bound to expect, though a full proof stays out
of reach. Clearly, it suces to check the cycles around (x, y) = (+1, 0), so we
assume that a + µ1 + µ2 ≈ 0 and b + µ3 < 0. The slow divergence integral is
expressed by

I(θ0) = ∫ θ0

−θ0
 2 sin
2 θ
a sin
2 θ − b cos θ sin θ + µ2(1 − cos θ) − µ3 sin θ dθ.

22

Proposition 17. Around a slow-fast Hopf point at (x, y) = (+1, 0), there are
at most two canard cycles.

Proof. Clearly I(0) = 0, so any solution of I = 0 leads by Rolle to the existence
of an intermediary solution of I ′(θ0) = 0. If furthermore, for any solution of
I ′ = 0, we ﬁnd I ′′(θ0) has a ﬁxed sign not depending on θ0, then clearly there is
only one such point and hence also at most only one solution of I = 0 (besides
θ = 0). By the results of [10], we know that this translates to the presence
of at most two canard cycles. Let N (θ) be the denominator appearing in the
integrand of I, i.e. I(θ) = ∫ θ0
−θ0 2 sin
2 θ/N (θ) dθ. We ﬁnd

I ′(θ) = 2 sin
2 θ0
N (θ0) + 2 sin
2 θ0
N (−θ0) = 2 sin
2 θ0
N (θ0)N (−θ0) (N (θ0) + N (−θ0))

= 4 sin
2 θ0
N (θ0)N (−θ0) (1 − cos θ)(µ2 + a + a cos θ).

A zero is found at θ = θ∗ := arccos µ2+a
−a , only when −2a < µ2 < 0 or 0 < µ2 <
−2a. A lengthy computation shows that

I ′′(θ∗) = sin θ∗ 4a2(µ2 + 2a)
(bµ2 + ba − µ3a)2 ,

which has a ﬁxed sign. This proves the proposition.

Besides the canard cycles involved in this study, there can be also canard
cycles at more degenerate contact points (not slow-fast Hopf): we distinguish
slow-fast Bogdanov–Takens points of codimension 2, or more in general slow-fast
codimension n contact points.

Lemma 18. At (x, y) = (+1, 0), a slow-fast Bogdanov–Takens contact point
appears when (µ1, µ3) = (−a−µ2, −b)+o(1) and µ2 ̸= −2a. A slow-fast contact
point of codimension 3 appears when (µ1, µ2, µ3) = (a, −2a, −b) + o(1) and
b ̸= 0. A slow-fast contact point of codimension 4 appears when (µ1, µ2, µ3, b) =
(a, −2a, 0, 0)+o(1). There are no slow-fast contact points of codimension higher
than 4.

Proof. Recall expression (23). Expanding it further in θ, a contact point of
codimension n is found (for a deﬁnition, see [9]) when the ﬁrst n coecients of
this expansion are zero. The lemma hence follows after an easy computation.

The cyclicity near slow-fast contact points of codimension n is known up to
n = 3. For n = 1, it is elaborated in [12], for n = 2 in [9], for n = 3 in the
PhD thesis of R. Huzak (ﬁrst part of the proof published in [18]). Using these
results, it is possible to prove that the cyclicity near slow-fast contact points is
at most 2. For slow-fast contact points of codimension 4, there are no results
that can be applied though.
 23

6. The cyclicity of the reversible families

The quadratic family introduced in this paper has, basically, two symmetric
subfamilies: (2) or (18). The objective of this section is to study the existence,
nonexistence, uniqueness, and maximum number of limit cycles of the ﬁrst sub-
family respect to the plane (a, b), because the cyclicity of the second one is zero
since it has no limit cycles (see Proposition 14). First, see Lemma 19, we show
this duality, after we ﬁnd the maximum number of limit cycles of (2), see The-
orem 20. Then we restrict our analysis to (a, b) ∈
 , where we prove that there
are several regions in the parameter space (a, b, µ) such that (2) has no limit
cycles, and ﬁnally, we prove that there is a region in the (a, b)-plane such that
(2) has two limit cycles for suitable values of µ, always in conﬁguration (1 : 1).
These values correspond with Hopf and Bogdanov–Takens bifurcations.

Lemma 19. System (6) which is invariant with respect to a point or a straight
line can be transformed to (2) or (18), respectively.

Proof. After a translation and a rotation of (6), the proof follows imposing the
invariance of the transformed vector ﬁeld with respect to (x, y, t) → (−x, −y, −t)
or (x, y, t) → (x, −y, −t).

Theorem 20. System (2) has at most two limit cycles, and if it has limit cycles,
then the unique possible conﬁguration is (1 : 1).

Proof. By using the change of variables u = x, v = ax2 + bxy + µ system (2)
becomes { u
′ = buv,
v′ = f (u, v) u
2 + g(u, v), (26)

where f (u, v) = (a
2 + b
2) u
2 + a (b − 2) v + 2µa − b2

and g(u, v) = (bv + v − µ)(v − µ).

Now, by applying the transformation {x = u2, y = v}, the previous system
reduces to
{ x′ = 2bxy,
y′ = ((a
2 + b2) x + a (b − 2) y + 2µa − b2) x + (by + y − µ)(y − µ),

which is a quadratic system with an invariant straight line. Therefore, last
system has at most one limit cycle. This implies that system (26) has at most 2
limit cycles, and if it has limit cycles the unique possible conﬁguration is (1 : 1).
This ends the proof of the ﬁrst part of the statement because systems (26) and
(2) are equivalent.

As announced in the beginning of this section, we will study in detail system
{ _x = ax2 + bxy + µ,
_y = x2 + y2 − 1. (27)

24

Figure 6: Decomposition of Ω in the disjoint regions.

when (a, b) ∈
 . We remark that some of the conclusions about non existence
can also be extended to the full space (a, b, µ), but we are only interested in
system (27) inside the class of system (6) as a perturbation of a fake saddle
singularity, i.e. (a, b) ∈
 .
The zero locus of
 G(a, b) = 8a
2 + b3 + 4b2 + 4b (28)

deﬁne the points, in the (a, b)-plane, for which system (27) can exhibit cusp
points, see the proof of Proposition 21. Hence, for analyzing the limit cycles of
this system, we will split
 in disjoint regions:

R
0
0 := {(a, b) ∈
 | a = 0},

R
+
0 := {(a, b) ∈
 | a ̸= 0, 0 < b < 1, G(a, b) > 0},

R−
0 := {(a, b) ∈
 | a ̸= 0, b ≤ 0, G(a, b) > 0},

R±
11 := {(a, b) ∈
 | a ̸= 0, ±(2 + b) > 0, G(a, b) < 0},

  ± := {(a, b) ∈
 | a ̸= 0, ±(2 + b) > 0, G(a, b) = 0},
 (29)

see Figure 6.
After the results and simulations of this section we can state that system
(27) can only have limit cycles, always in conﬁguration (1 : 1), when the values
of (a, b, µ) are in R+
11 and µ < 0 or R
−
11 and µ > 0. In fact when (a, b) ∈ R
±
11
the two limit cycles bifurcate simultaneously from two weak foci.

6.1. Local behavior of the singularities

This subsection deals with the number and local phase portrait of the sin-
gularities of system (27).
 25

Proposition 21. Consider (a, b) ∈
 . If (a, b) = (0, 0) then system (27) has
no ﬁnite singularities when µ ̸= 0 or the unit circle is ﬁlled with singularities
otherwise. On the other hand, when (a, b) ̸= (0, 0), consider µ
± = (−a ±√a2 + b2)/2, then the next properties hold.

(i) If µ ̸∈ [µ
−, µ
+], then system (27) has no ﬁnite singularities.

(ii) If µ = µ
±, then system (27) has exactly two singularities. Moreover,

• When (a, b) ∈   + and µ = µ
−, or (a, b) ∈   − and µ = µ
+, both
singularities are regular cusps;

• when (a, b) = (0, −2), they are degenerate nilpotent singularities;

• in the remaining cases, they are saddle-nodes.

(iii) If µ ∈ (µ
−, µ
+), then system (27) has exactly four ﬁnite singularities: a
pair of saddles and a pair of anti-saddles, located in the unit circle, and
the points of each pair are antipodals.

Proof. The statement for (a, b) = (0, 0) can be deduced directly from the struc-
ture of (27). From now on we assume that (a, b) ̸= (0, 0).
The number of singularities follows directly studying the intersection points
of the zero-locus of the components of the vector ﬁeld: ax2 + bxy + µ and the
circle x2 +y2 −1, and using the symmetry of system (27). A simple computation
shows that they only intersect when µ ∈ [µ
−, µ
+]. Moreover, when µ = µ
± both
curves are tangent in two antipodal symmetric points and when µ ∈ (µ
−, µ
+)
there are two pairs of two antipodal points.
Since all the singularities lie on the unit circle, we can write each of them as

(x0, y0) = ( 1 − t2

1 + t2 , 2t
1 + t2
 ) ,

with t a solution of S = (a + µ)t
4 − 2bt
3 + (−2a + 2µ)t
2 + 2bt + a + µ = 0. Then
we have
 tr DX(x0, y0) = −2 at2 − (b + 2)t − a
t2 + 1 ,

det DX(x0, y0) = −2 bt
4 + 4at
3 − 6bt
2 − 4at + b
(t2 + 1)2 .

The resultant, with respect to the variable t, of the numerators of the above
trace and determinant with S are 16T 2
ab and 4096(a
2 + b
2)
2D2
ab, respectively,
where Tab = (4a
2 + (b + 2)2)µ − ab
2 + 4a and Dab = 4µ
2 + 4aµ − b2. Finally,
the resultant, with respect to µ, of Tab and Dab, is −G(a, b)
2, see (28).
From the above resultants, we see that when µ ∈ (µ
−, µ
+), the determinant
det DX(x0, y0) never vanishes. Consequently, the local behavior of all singular-
ities is given by Hartman–Grobmann Theorem because its hyperbolicity except
in the weak focus case. But all the singularities are saddles or anti-saddles. The

26

location on the circle follows from the work of Berlinskii, see [2]. This concludes
statements (i) and (iii).
When µ = µ
±, using the previous resultants, the determinant det DX(x0, y0)
vanishes and the trace tr DX(x0, y0) only vanishes when G(a, b) = 0. Hence,
when G(a, b) ̸= 0 the points are semi-hyperbolic, in fact they are of saddle-node
type, see [11].
The remaining cases are µ = µ
± and G(a, b) = 0. We focus on µ = µ
+,
the other case being completely similar. The set {G(a, b) = 0} ∩
 =   + ∪
  − ∪ {(0, −2)} is parameterized by (a, b) = (±s(1 − s
2), −2s
2), taking the +
sign and s ∈ (0, 1) for   +, taking the − sign and s > 1 along   −, and s = 1
for (a, b) = (0, −2). Solving { _x = 0, _y = 0, tr DX = 0} along   + with respect
to (x, y, s) shows that solutions are only present when µ = −s (and along the
solution also det DX = 0). Evaluating the expression µ
+ = (−a + √a2 + b2)/2
in this parameterized form along   + yields µ
+ = s
3 ̸= −s = µ. On the other
hand, solving { _x = 0, _y = 0, tr DX = 0} along   − shows solutions along µ = s,
which corresponds to µ
+ when s > 1.
When µ = µ
± and the trace is nonzero, the singularities are clearly semi-
hyperbolic of saddle-node type. On the other hand, in the nilpotent case, one
can apply Proposition 9, compute r2 and s2 along   ± and one ﬁnds that r2.s2
is always nonzero, except when (a, b, µ) = (0, −2, ±1) (in that case, s2 = 0 but
r2 ̸= 0 since θ = ±π/4). Proposition 13 can be applied to see that it is a
degenerate nilpotent singularity.

6.2. Nonexistence of limit cycles
Next result provides conditions on the parameter space where system (27)
does not have limit cycles.

Theorem 22. System (27) has no limit cycles in the cases:

(i) 0 < b < 1.

(ii) a = 0 or b = 0.

(iii) µ ̸∈ (µ
−, µ
+).

(iv) −2 ≤ b < 0 and µ ∈ [0, µ
+), or b ≤ −2 and µ ∈ (µ
−, 0].

(v) (a, b) ∈ R
−
0 ∩ {−2 ≤ b < 0} and µ ∈ (µ
−, ^µ], or (a, b) ∈ R
−
0 ∩ {b ≤ −2}
and µ ∈ [^µ, µ
+), where
 ^µ = a(b
2 − 4)
4a2 + (b + 2)2 .

Proof. (i) First, it is well-known that any limit cycle of a quadratic system
has only one singularity of index one inside of it, and such singularity is a
focus. Hence, for proving this statement, it is enough to demonstrate that each
singularity of (27), with 0 < b < 1, is a saddle, or a node, or a saddle-node. We
will split the proof of this case in two parts: µ = 0 and µ ̸= 0.

27

Suppose now µ = 0. Then, see Proposition 21, system (27) has four sin-
gularities, two of them on the line {x = 0}, which are (0, 1) and (0, −1), and
the other two singularities are the intersections of the line {ax + by = 0} and
the circle {x2 + y2 = 1}, which we denote by p1 and p2. A straightforward
computation of the trace and the determinant at these singularities, by using
(8) and (9), and the Hartman–Grobmann Theorem imply that (0, 1) and (0, −1)
are nodes, and that p1 and p2 are saddles.
Next suppose that µ ̸= 0. Let (x0, y0) be a singularity of (27). Since µ ̸= 0,
x0 ̸= 0. Hence we have y0 = −(ax2
0 + µ)/bx0, and a simple computation shows
that
 (tr
2 DX − 4 det DX)(x0, y0) =
 (a (b + 2) x02 − µ (b − 2))2 + 8b3x4
0
b2x2
0 .

Thus, (tr2 DX − 4 det DX)(x0, y0) > 0 for 0 < b < 1, which implies that (x0, y0)
is a node if det DX(x0, y0) > 0, and it is a saddle if det DX(x0, y0) < 0. The
case det DX(x0, y0) = 0 follows from Proposition 21 and the point (x0, y0) is a
saddle-node singularity. Thus, we have proved statement (i).
(ii) First, suppose b = 0. If a = 0, then (27) has no singularities; and if a > 0,
then (27) has two invariant straight lines which contain all the singularities of
the system. These properties implies that (27) has no limit cycles.
Suppose that a = 0. From previous cases we can assume b < 0. If µ = 0,
then the resulting system is a particular case of (18), which does not have limit
cycles. If µ ̸= 0 and f (x) = x− b+2
b , then we obtain

div(f X) = − µ(b + 2)x− 2(b+1)
b
b ,

where X = (P, Q) be the vector ﬁeld associated with (27). Thus, div(f X)
does not change sign for x > 0. Hence, the classical Bendixson–Dulac Theorem
implies the assertion.
(iii) It follows from (i) and (ii) of Proposition 21 because in the ﬁrst case
system (27) has no singularities, and in the second one the type of singularities
implies the nonexistence of limit cycles.
(iv) We can assume b < 0 and a > 0. By using the function f (x) = x− b+2
b
we obtain
 div(f X) = − x− 2(b+1)
b
b (a(2 − b)x2 + µ(b + 2)) .

Hence, if −2 ≤ b < 0 and µ ≥ 0, then div(f X) ≥ 0 for x > 0; and if b ≤ −2
and µ ≤ 0, then div(f X) ≥ 0 for x > 0. Thus, the Bendixson–Dulac Theorem
implies that system (27) has no limit cycles.
(v) As µ ̸= 0 the y-axis is without contact with respect to the vector ﬁeld.
By symmetry we can restrict our analysis to the half plane x > 0. In this
region, system (27) has one saddle and one anti-saddle, see Proposition 21. The
straight line, L0S, joining the origin and the saddle point also passes trough the
other saddle. Consequently, as the vector ﬁeld is quadratic, L0S has no tangent

28

points except the saddle point and the limit cycle can not cross it. Hence the
limit cycle remains, if it exists, in the angular region deﬁned by L0S and the
y-axis that contains the anti-saddle point. The proof follows because, for the
values of the parameters, the line where the trace vanishes does not intersect
this angular region.

6.3. Hopf and Bogdanov–Takens bifurcations
From Theorem 22 it follows that system (27) can only exhibit limit cycles
when µ ∈ (µ
−, µ
+). Next we prove the existence of a Bogdanov–Takens bifur-
cation curve and a Hopf bifurcation surface.

Theorem 23. For each (a0, b0) ̸= (0, −2) in   +(  −) there exists µ0 < 0
(µ0 > 0) such that system (27) undergoes two simultaneous Bogdanov–Takens
bifurcations on R
+
11 (R
−
11).

Theorem 24. System (27) undergoes two simultaneous non-degenerate Hopf
bifurcations on the surface
 µ = a(b
2 − 4)
4a2 + (b + 2)2 (30)

if and only if (a, b) ∈ R
±
11.

A direct consequence of the above two theorems is the next result.

Corollary 25. For each (a, b) in R+
11 (R
−
11), there are values of µ < 0 (µ > 0)
such that system (27) has two limit cycles in conﬁguration (1 : 1).

Proof of Theorem 23. We focus on   +, where we write

(a, b) = (s(1 − s
2), −2s
2), 0 < s < 1

(see the proof of Proposition 21), and ﬁnd singularities of nilpotent type when
µ = −s at (x, y) = (cos θ, sin θ) when tan θ = −s. A lengthy computation of
r2 and s2 from Proposition 9 shows that r2s2 ̸= 0 whenever (a, b) ̸= (0, −2)
(i.e. whenever s ̸= 1). Using Remark 10, we know that regular cusps appearing
in the family (27) unfold completely according to a Bogdanov–Takens diagram
inside the family (27). This proves the theorem.

Proof of Theorem 24. Let X = (P, Q) be the vector ﬁeld associated with sys-
tem (27). This system has critical points with vanishing trace when {(x, y) ∈
R2 | P (x, y) = Q(x, y) = tr DX(x, y) = 0}. A necessary condition so that the
previous set is not empty is

Res(Res(P, tr DX, y), Res(Res(Q, tr DX, y), x) = 0.

The surface (30) follows from the above equation when b ̸= −2. We choose µ
∗

such that (a, b, µ∗) is in this surface, then the change

(a, b) = ( r(1 − t2)
2(t2 + 1) , 2rt
t2 + 1 − 2
)

29

with r > 0 and −1 < t < 1, writes the singularities of (27) as

p
±
t = ± ( 2t
t2 + 1 , t2 − 1
t2 + 1
 ) ,

q±
t = ± ( 2 (−2 t2 + r t − 2)(t
2 − 1)
(t2 + 1)√F , r t4 − 8 t
3 + 6r t2 − 8 t + r
(t2 + 1)√F
 ) ,

with F = r2t4 + 14r2t2 − 32rt
3 + 16t4 + r2 − 32rt + 32t
2 + 16. Straightforward
computations shows that, when a ̸= 0, F > 0. Moreover, the function G(a, b),
deﬁned in (28), moves to

G(r, t) = 2 r2(t
6 + 4 r t3 − 5 t4 − 5 t2 + 1)
(t2 + 1)3 .

The trace and the determinant at the singularities, see (8) and (9), are

tr(p
+
t ) = 0, det(p
+
t ) = − 2G(r, t)
r2 ,

tr(q+
t ) = ± 2(t2 + 1)2G(r, t)

r√F (r, t) , det(q+
t ) = 2G(r, t)
r2 .

Their sign is given in the next table:

If G(r, t) < 0 If G(r, t) > 0
tr det tr det
p
+
t 0 > 0 0 < 0
p−
t 0 > 0 0 < 0
q+
t < 0 < 0 > 0 > 0
q−
t > 0 < 0 < 0 > 0

If G(r, t) < 0 and a ̸= 0 then Theorem 6(i) asserts that p
+
t is not a center. Con-
sequently, its stability is determined and p±
t are weak foci. If G(r, t) > 0 there
are no weak foci because p±
t are saddles. Thus, there is no Hopf bifurcations if
(a, b) ∈ R
±
0 .
Finally, we show that two Hopf bifurcations exist when G(r, t) < 0, that
is, when (a, b) ∈ R±
11. Let ε be a small parameter. Thus, system (27) with
µ = µ
∗ + ε has a critical point, (xε, yε), close to p
+
t , and a straightforward
computation shows that

xε = 2t
t2 + 1 + ε (t2 − 1)(t
4 + 2t
2 + 1)
2(t6 + 4rt3 − 5t4 − 5t2 + 1) + O(ε
2),

yε = t2 − 1
t2 + 1 − ε t(t
4 + 2t
2 + 1)
t6 + 4rt3 − 5t4 − 5t2 + 1 + O(ε2).

This implies that tr(DX)(xε, yε) = −(r3/G(r, t))ε + O(ε2). Therefore, when we
cross the surface (30), a critical point of focus type of system (27) changes the
stability and, as it is not a center on the surface, a limit cycle bifurcates from
p+
t . At the same time, and with opposite stability, another one bifurcates from
p−
t .
 30

µ < µ   µ = µ  µ  < µ  µH µH < µ < µ L

µ = µL µL < µ < µ SS− µ = µSS− µSS− < µ < µ SS+

µ = µSS+ µSS+ < µ < 0 µ = 0

Figure 7: Phase portraits evolution, for µ ≤ 0 when (a, b) ∈ R+
11.

6.4. Phase portraits

From the previous sections, system (27) exhibits limit cycles when (a, b) ∈
R+
11 and µ < 0 or when (a, b) ∈ R
−
11 and µ > 0. Figures 7 and 8 shows the phase
portraits on these parameter regions. We have only shown these transitions
because they are the only ones that, with our results and simulations, exhibit
limit cycles. We think that there are no other bifurcations nor phase portraits
in these parameter regions.
We explain these transitions following the results of the previous sections
and some simulations using the software P4, see [11].
Assume that (a, b) ∈ R
+
11. When µ < µ
− there are no critical points, see
Proposition 21. For µ < µ
− two symmetric saddle-nodes appear that bifurcate
in a pair of symmetric saddle and an anti-saddle points. For µ = µH , see
Theorem 24, the system has two symmetric weak foci and two symmetric small
limit cycle bifurcate from them that remains for µH < µ < µL. The limit cycles
grow in amplitude and disappear in two ﬁnite symmetric homoclinic connections
for µ = µL. Then two types of ﬁnite saddle connections appear for µ = µSS−
and µ = µSS+. When µ = 0, see Theorem 22, x = 0 is an invariant straight
line, the points over this line are saddles and there are no limit cycles.
Assume that (a, b) ∈ R−
11. As in the previous evolution, when µ = 0, see

31
µ = 0 0 < µ < µ L µ = µL µL < µ  µH

µH < µ < µ + µ = µ+ µ > µ +

Figure 8: Phase portraits evolution, for µ ≥ 0 when (a, b) ∈ R−
11.

Theorem 22, x = 0 is an invariant straight line, the points over this line are
saddles and there are no limit cycles. Then for µ = µ
L the system has two
symmetric ﬁnite homoclinic connections. When they break, two symmetric limit
cycles appear and shrink, to disappear in two simultaneous Hopf bifurcations
for µ = µ
H , see Theorem 24. Then the symmetric pair of saddle and anti-
saddle points collide in two symmetric saddle points when µ = µ
+. Afterwards,
µ > µ
+, the system has no ﬁnite singular points.
Theorem 24 provides existence of µH < 0 (µ
H > 0) for any (a, b) in R+
11
(R
−
11). Consequently the Hopf surface projects the full region R±
11. Theorem 23
provides existence of µL < 0 (µ
L > 0) for values (a, b), close to   + (  −) in R+
11
(R
−
11). We have continued numerically these homoclinic connection values to
obtain a homoclinic connection surface that also projects in the full region R
±
11.
Theorem 22 proves the nonexistence of limit cycles in R+
0 and all our simulations
never provide them in R
−
0 . All the results and numerical simulations given in
this paper give us to think that system (27) never exhibit limit cycles in R0 =
R+
0 ∪ R−
0 . They only exist, always in conﬁguration (1 : 1), in R11 = R
+
11 ∪ R−
11.

Acknowledgements

The ﬁrst author acknowledges support from FWO Vlaanderen. The third au-
thor is supported by the MINECO/FEDER MTM2008-03437 and UNAB10-4E-
378 grants, by the AGAUR 2014SGR568 grant, and by the European Commu-
nity FP7-PEOPLE-2012-IRSES-316338 and FP7-PEOPLE-2012-IRSES-318999
grants. We thank Jorge Galan for numerical simulations conﬁrming the exis-
tence of a homoclinic connection.
 32

References

[1] A. A. Andronov, E. A. Leontovich, I. I. Gordon, and A. G. Maer. Qual-
itative theory of second-order dynamic systems. Halsted Press (A division
of John Wiley & Sons), New York-Toronto, Ont., 1973. Translated from
the Russian by D. Louvish.

[2] A. N. Berlinski. On the behavior of the integral curves of a dierential
equation. Izv. Vysˇs. Uˇcebn. Zaved. Matematika, 1960(2 (15)):3–18, 1960.

[3] G. Chen, C. Li, C. Liu, and J. Llibre. The cyclicity of period annuli of
some classes of reversible quadratic systems. Discrete Contin. Dyn. Syst.,
16(1):157–177, 2006.

[4] S.-N. Chow, C. Li, and Y. Yi. The cyclicity of period annuli of degenerate
quadratic Hamiltonian systems with elliptic segment loops. Ergodic Theory
Dynam. Systems, 22(2):349–374, 2002.

[5] B. Coll, C. Li, and R. Prohens. Quadratic perturbations of a class of
quadratic reversible systems with two centers. Discrete Contin. Dyn. Syst.,
24(3):699–729, 2009.

[6] P. De Maesschalck and F. Dumortier. Time analysis and entry-exit relation
near planar turning points. J. Diﬀerential Equations, 215(2):225–267, 2005.

[7] P. De Maesschalck and F. Dumortier. Canard solutions at non-generic
turning points. Trans. Amer. Math. Soc., 358(5):2291–2334 (electronic),
2006.

[8] P. De Maesschalck and F. Dumortier. Canard cycles in the presence of slow
dynamics with singularities. Proc. Roy. Soc. Edinburgh Sect. A, 138(2):265–
299, 2008.

[9] P. De Maesschalck and F. Dumortier. Slow-fast Bogdanov-Takens bifurca-
tions. J. Diﬀerential Equations, 250(2):1000–1025, 2011.

[10] F. Dumortier. Slow divergence integral and balanced canard solutions.
Qual. Theory Dyn. Syst., 10(1):65–85, 2011.

[11] F. Dumortier, J. Llibre, and J. C. Art´es. Qualitative theory of planar
diﬀerential systems. Universitext. Springer-Verlag, Berlin, 2006.

[12] F. Dumortier and R. Roussarie. Birth of canard cycles. Discrete Contin.
Dyn. Syst. Ser. S, 2(4):723–781, 2009.

[13] F. Dumortier, R. Roussarie, and C. Rousseau. Hilbert's 16th problem for
quadratic vector ﬁelds. J. Diﬀerential Equations, 110(1):86–133, 1994.

[14] F. Dumortier, R. Roussarie, and J. Sotomayor. Generic 3-parameter fam-
ilies of vector ﬁelds on the plane, unfolding a singularity with nilpotent
linear part. The cusp case of codimension 3. Ergodic Theory Dynam. Sys-
tems, 7(3):375–413, 1987.
 33

[15] F. Dumortier, R. Roussarie, J. Sotomayor, and H. _Zo lpolhk adek. Bifurca-
tions of planar vector ﬁelds, volume 1480 of Lecture Notes in Mathematics.
Springer-Verlag, Berlin, 1991. Nilpotent singularities and Abelian integrals.

[16] S. Gautier, L. Gavrilov, and I. D. Iliev. Perturbations of quadratic centers
of genus one. Discrete Contin. Dyn. Syst., 25(2):511–535, 2009.

[17] L. Gavrilov. The inﬁnitesimal 16th Hilbert problem in the quadratic case.
Invent. Math., 143(3):449–497, 2001.

[18] R. Huzak, P. De Maesschalck, and F. Dumortier. Limit cycles in slow-fast
codimension 3 saddle and elliptic bifurcations. J. Diﬀerential Equations,
255(11):4012–4051, 2013.

[19] I. D. Iliev. Perturbations of quadratic centers. Bull. Sci. Math., 122(2):107–
161, 1998.

[20] I. D. Iliev, C. Li, and J. Yu. Bifurcations of limit cycles from quadratic
non-Hamiltonian systems with two centres and two unbounded heteroclinic
loops. Nonlinearity, 18(1):305–330, 2005.

[21] C. Li and Z. Zhang. Remarks on 16th weak Hilbert problem for n = 2.
Nonlinearity, 15(6):1975–1992, 2002.

[22] F. Loray. A preparation theorem for codimension-one foliations. Ann. of
Math. (2), 163(2):709–722, 2006.

[23] I. Nikolaev and E. Zhuzhoma. Flows on 2-dimensional manifolds, volume
1705 of Lecture Notes in Mathematics. Springer-Verlag, Berlin, 1999. An
overview.

[24] L. Perko. Diﬀerential equations and dynamical systems, volume 7 of Texts
in Applied Mathematics. Springer-Verlag, New York, third edition, 2001.

[25] H. _Zo l˘adek. Quadratic systems with center and their perturbations. J.
Diﬀerential Equations, 109(2):223–273, 1994.

34
