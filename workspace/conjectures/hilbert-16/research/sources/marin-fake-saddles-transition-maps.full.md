<!-- source: https://ddd.uab.cat/pub/artpub/2026/327411/p11901.pdf | converted from PDF -->

Electronic Journal of Qualitative Theory of Differential Equations
2026, No. 5, 1–10; https://doi.org/10.14232/ejqtde.2026.1.5 www.math.u-szeged.hu/ejqtde/

Fake saddles and their transition maps

David Marín B

Universitat Autònoma de Barcelona, Departament de Matemàtiques, Edifici Cc,
08193 Cerdanyola del Vallès, Barcelona, Spain

Received 22 September 2025, appeared 19 March 2026

Communicated by Armengol Gasull

Abstract. We study degenerate singular points of planar vector fields inside a (degen-
erate) flow box. These kind of singularities are called fake saddles and their linear parts
are always zero. We characterize fake saddles with non-zero second-order jet and we
give the first term of a uniform asymptotic expansion of the Poincaré map between two
transverse sections to their corresponding singular fiber, determining its stability.

Keywords: singularities, Poincaré and Dulac transition maps, asymptotic expansion,
uniform flatness, stability.

2020 Mathematics Subject Classification: 34D10, 34D20; Secondary: 34C05.

1 Introduction and statements of main results

Following [3,8] we define a fake saddle as a singular point having exactly two separatrices which
are contained in a smooth invariant curve separating two hyperbolic sectors, see Figure 1.1.
This kind of singularities are also known as impassable grains. Another way to think about a
fake saddle is that the corresponding vector field can be put in a form that is like a degenerate
flow box, i.e. near the singularity the phase portrait consists of parallel fibers, all but one
of which have no singular points, and the singular fiber (the union of the singular point
with its two separatrices) has a semi-stable equilibrium point, see [2]. Taking two transverse
sections Σα and Σω to the singular fiber outside the singular point there is a transition map
Πω
α : Σα → Σω which is well-defined on both sides of the singular fiber.
The local phase portrait of a singularity with non-zero linear part (for the nilpotent case
see for instance [1, Theorem 3.5]) is well known and prevents the singular point from being a
fake saddle. Notice that the smoothness of the singular fiber is strictly necessary because the
Hamiltonian vector field y∂x + x2∂y has a nilpotent singularity at the origin with exactly two
separatrices that are contained in the cuspidal curve y2 − 2
3 x3 = 0 separating two hyperbolic
sectors.
The first non-trivial and generic case of a fake saddle arises when the second-order jet
is non-zero. Our objective is to characterize these generic fake saddles and to analyze their
transition maps in order to determine whether the behavior is attractive or repulsive on each
side of the singular fiber. The techniques we employ allow us to derive the leading term of an
asymptotic expansion that is uniform with respect to parameters.

B Email: David.Marin@uab.cat

2 D. Marín

THE EFFECT OF A SINGULARITY ON TRANSITION MAPS

B. Coll 1,A.Gasull 2 and R. Prohens ⇤1

1Departament de Ci`encies Matem`atiques i Inform`atica
Universitat de les Illes Balears, IAC3 (Palma de Mallorca) Spain

2Departament de Matem`atiques, Universitat Aut`onoma de Barcelona
08193 Bellaterra (Barcelona) Spain

Abstract. Consider a planar autonomous di↵erential equation having a de-
generated singularity inside a ﬂow box with two transversal sections in such a
way that a Poincar´e map between them is well deﬁned by the ﬂow. We are
interested in understanding which is the e↵ect of having this singularity on the
properties of this Poincar´e map. The ﬁber containing the singularity is usually
called singular ﬁber and, in particular, we want to determine its attractive or
repulsive character. We prove that there is a real value whose sign determines
the stability of the singular ﬁber. This value is given by the principal value of
asuitableintegralconstructedfromthecorrespondingdi↵erential equation.

1. Introduction and main results. We are interested in understanding what
the e↵ect of having a degenerate singularity inside a ﬂow box is on the properties
of a Poincar´e map, when this map is deﬁned between two transversal sections to
the ﬂow, say ⌃↵ and ⌃!. See Figure 1. This Poincar´e map is also called transition
map.

Figure 1. Transition map with a singular ﬁber containing a fake singularity.

Notice that usual ﬂow boxes have no singularities inside and the transition
map ⇧
!
↵ between each two transversal sections is as smooth as the vector ﬁeld
itself. Nevertheless, in our situation, we have a singularity on one of the ﬁbers and
the rest of points of this particular ﬁber are its two separatrices. Sometimes this
kind of singularities are called fake singularities,see [8] and this ﬁber is called a
singular ﬁber. Clearly, a fake singularity allows that the associated return map can
be extended continuously to the point where the singular ﬁber cuts with ⌃↵, but
the regularity of this map ⇧
!
↵ at this cut is not clear at all.

2020 Mathematics Subject Classiﬁcation. Primary: 34D10, 34D20, 34B08; Secondary: 34C05.
Key words and phrases. Degenerate singularities, transition map, stability.
⇤Corresponding author: R. Prohens.
 1

Figure 1.1: Fake saddle and the associated transition maps.

This work is mainly motivated by the paper [2], which provides a normal form for generic
fake saddles that we recall in the sequel. First we can locate the fake saddle at the origin
(0, 0). Secondly, if the vector field is at least of class C 3 there exists a local diffeomorphism
that rectifies the germ of singular fiber, so that it is contained in the line y = 0 in a certain
coordinate system (x, y), see [2, Lemma 2.1]. Thanks to the hypothesis that the second-order
jet of the fake saddle is non-zero, after a suitable rescaling of the coordinates we can assume
that the fake saddle is defined by a system of differential equations
{ ˙x = x2 + axy + y2 + O3(x, y),

˙y = y(cx + by + O2(x, y)),

where a, b, c ∈ R. This normal form motivates us to consider a smooth family of planar vector
fields {Xµ}µ∈Ω⊂Rn having the form

Xµ(x, y) = (x2 f1(x, y; µ) + a(µ)xy + y2 f2(x, y; µ))∂x + (xg1(x, y; µ) + yg2(y; µ))y∂y, (1.1)

where f1(x, y; µ), f2(x, y; µ), g1(x, y; µ) and g2(y; µ) are C K-functions fulfilling f1(0, 0; µ) =
f2(0, 0; µ) = 1. We consider the following invariants

a(µ), b(µ) := g2(0; µ), c(µ) := g1(0, 0; µ) (1.2)

of the family (1.1) and define the associated value d(µ) := 4(1 − c(µ)) − (a(µ) − b(µ))2, which
will play a key role in the sequel.
In this paper we extend the main theorems of [2] and we give simpler proofs of them using
the results stated in [5,7]. Our first result gives a characterization of generic fake saddles inside
the family (1.1), generalizing [2, Theorem A] which only treats the case a = 0.

Theorem 1.1. If the invariants (a, b, c) given in (1.2) of a vector field X in the family (1.1) do not
belong to {d = 0} ∩ {a2 − b2 = 4} then the origin is a fake saddle if and only if, either d > 0, or
c = 1 and a = b. In both situations after blowing up the origin we have a single singular point on the
exceptional divisor, which is a hyperbolic saddle of hyperbolicity ratio 1 − c > 0 in the first one and a
semi-hyperbolic saddle in the second one.

The hypothesis (a, b, c) /∈ {d = 0} ∩ {a2 − b2 = 4} in Theorem 1.1 (which is always verified
when a = 0) can not be removed as Example 3.1 will show.
Let Ω be an open subset of Rn and let W any subset of Ω. We recall (cf. [5, Defi-
nition 1.2]) that a C K-function f (s; µ) defined in the intersection of (0, +∞) × Ω with an

Fake saddles and their transition maps 3

open neighborhood of {0} × Ω ⊂ Rn+1 belongs to the flat class F K
L (W) if for each µ0 ∈ W
and ν = (ν0, . . . , νn) ∈ Nn+1 with |ν| = ν0 + · · · + νn ≤ K there exists ε > 0 such that
|∂ν0
s ∂ν1
µ1 · · · ∂νn
µn f (s; µ)| ≤ CsL−ν0 for every s ∈ (0, ε) and µ ∈ Bε(µ0) ∩ Ω.
We consider the transverse sections Σ⋆ = {x = ⋆} to y = 0, for ⋆ ∈ {α, ω}, where
α < 0 < ω. We assume that f1(x, 0) > 0 for all x ∈ [α, ω] and we consider the transition
map Πω
α : Σα → Σω. Our second result extends [2, Theorem B], which only treats the case
a = b = 0, ∂y f1 = ∂yg1 = 0, f2 = 1 and g2 = 0, when the transition map is restricted to y > 0.
In that theorem the authors characterize the stability of the transition map from the sign of
the Cauchy principal value

PV ∫ ω

α g1(x, 0; µ)
x f1(x, 0; µ) dx := lim
ε→0+
 (∫ −ε

α g1(x, 0; µ)
x f1(x, 0; µ) dx + ∫ ω

ε g1(x, 0; µ)
x f1(x, 0; µ) dx) .

Theorem 1.2. Assume that µ0 ∈ Ω and that the invariants (1.2) of the vector field Xµ0 in (1.1) belong
to {d = 4(1 − c) − (a − b)2 > 0}. If µ ≈ µ0 then the origin is a fake saddle of Xµ and its transition
map Πω
α : Σα → Σω satisfies Πω
α (y; µ) = eγ±(µ)y + F K
1+ϵ({d > 0}) on ±y ≥ 0, where ϵ > 0 and

γ±(µ) = PV ∫ ω

α g1(x, 0; µ)
x f1(x, 0; µ) dx ± π(2b(µ) − c(µ)(a(µ) + b(µ)))
√d(µ) .

Remark 1.3. Using that f1(0, 0) = 1 and g1(0, 0) = c we can explicitly compute the previous
Cauchy principal value using a convergent integral:

PV ∫ ω

α g1(x, 0)
x f1(x, 0) dx = c log ∣
∣
∣ ω
α
 ∣
∣
∣ + ∫ ω

α
 ( g1(x, 0)
f1(x, 0) − c) dx
x .

Remark 1.4. Clearly the sign of γ±(µ) determines the stability of the singular fiber y = 0 on
the side ±y > 0. In the case a = b = 0 the two values γ±(µ) coincide with the principal
value of the integral. Otherwise the stability of the two sides ±y > 0 can be different, see
Example 3.2.

It is worth to be noticed that the writing of Πω
α (y; µ) in the statement implies that it is of
the form eγ±(µ)y + o(y) but also that the remainder term o(y) is uniform with respect to the
parameter µ. This uniformity allows to address cyclicity problems and not just study stability.
For clarity in the exposition we will omit the dependence on µ when it is not essential.

2 Proofs of the main results

Proof of Theorem 1.1. A straightforward computation shows that

Y = (u, uv)∗X
u = P(u, v)u∂u + Q(u, v)v∂v

with P(0, 0) = 1 and Q(0, v) = −v2 + (b − a)v + c − 1. The point (u, v) = (0, 0) is always
a singular point of Y. If d < 0 then Y has two other singular points on the exceptional
divisor u = 0 with at least one non-zero eigenvalue. If (a, b, c) ∈ {d = 0} \ ({c = 1, a =
b} ∪ {a2 − b2 = 4}) then Y has another double singular point at (u, v) = (0, (b − a)/2) with a
non-zero eigenvalue. In these situations the transition map Πω
α : {x = α} → {x = ω} is not
well defined so that the origin is not a fake saddle of X. The remaining assertions are easy to
check.

4 D. Marín

The proof of Theorem 1.2 is based on some results of [5, 7]. For reader’s convenience we
recall here the notations that we will use in the sequel.
Consider a smooth family of planar vector fields {Xµ}µ≈µ0

Xµ = P1(x, y; µ)x∂x + P2(x, y; µ)y∂y (2.1)

having a saddle point at the origin with hyperbolicity ratio λ(µ) = − P2(0,0;µ)
P1(0,0;µ) > 0 and sep-
aratrices contained in the coordinate axes xy = 0. Let σ1(s; µ) = (σ11(s; µ), σ12(s; µ)) and
σ2(s; µ) = (σ21(s; µ), σ22(s; µ)) be parametrized smooth transverse sections to x = 0 and y = 0
respectively. Denote σijk(µ) = ∂k
s σij(0; µ) and assume that σ110 = σ220 = 0. We also assume
that for all µ ≈ µ0 we have P2(0, y; µ) ̸= 0 for all y ∈ [0, σ120(µ)] and P1(x, 0; µ) ̸= 0 for all
x ∈ [0, σ210(µ)]. Let us introduce the following auxiliary functions (see [7, p. 47])

L1(z; µ) = exp ∫ z

0
 ( P1
P2 (0, y; µ) + 1
λ(µ)
 ) dy
y ,

L2(z; µ) = exp ∫ z

0
 ( P2
P1 (x, 0; µ) + λ(µ)) dx
x .
 (2.2)

We will use the next result on the Dulac map of (2.1) which follows by applying [5, Theo-
rem A] and [7, Theorem A].

Theorem 2.1. The Dulac map D(s; µ) of the saddle at the origin of (2.1) associated to the parametrized
transverse sections σ1 and σ2 admits the following asymptotic expansion

D(s; µ) = sλ(µ)(∆00(µ) + Fϵ(µ0)),

where ϵ ∈ (0, min(λ(µ0), 1)) and
 ∆00 = σ111σλ
120(L2(σ210))λ

σλ
221σ210L1(σ120) . (2.3)

We will also use the following auxiliary result that gathers some properties of the flat class
F K
L (W) (see [5, Lemma A.2]).

Lemma 2.2. For every K ∈ Z≥0 ∪ {∞} the following assertions hold:

(a) C K(Ω) ⊂ F K
0 (Ω).

(b) If L ≥ L′ then F K
L (W) ⊂ F K
L′ (W).

(c) F K
L (W) is closed under addition.

(d) F K
L (W) · F K
L′ (W) ⊂ F K
L+L′ (W).

(e) F K
L (W) ◦ F K
L′ (W) ⊂ F K
LL′ (W).

Proof of Theorem 1.2. Let us compute first the value γ+, i.e. we assume that y ≥ 0. For simplic-
ity we omit the dependence on µ. Consider the charts (x, y) = π±(u, v) = (±u(1 − v), uv) of
the blow-up of the origin, see Figure 2.1. Notice that v = y
y±x is a coordinate on the exceptional
divisor u = 0. We assume that u, v ≥ 0, we write

π∗
±X
u = P±(u, v)u∂u + Q±(u, v)v∂v

Fake saddles and their transition maps 5

Σα Σ0 Σω

{x = y} {x = −y}

x

y

Figure 2.1: Blowup of the fake saddle at the origin.

and define
 X±(x, y) = P±
1 (x, y)x∂x + P±
2 (x, y)y∂y

with

P−
1 (x, y) = Q−(y, x), P−
2 (x, y) = P−(y, x), P+
1 (x, y) = P+(x, y), P+
2 (x, y) = Q+(x, y).

It can be checked that λ± = − P±
2 (0,0)
P±
1 (0,0) > 0, so that (0, 0) is a hyperbolic saddle of X±. More-

over λ+λ− = 1. Consider the Dulac map D± of the origin of X± between the parametrized
transverse sections

σ−
1 (s) = ( s
−α + s , −α + s), σ−
2 (s) = (1, s), σ+
1 (s) = (s, 1), σ+
2 (s) = (ω + s, s
ω + s
 ), (2.4)

which come from the parametrizations by the y coordinate of the original transverse sections
Σα, Σ0 and Σω to the invariant line {y = 0} of X.
By Theorem 2.1 it follows that D±(s; µ) = sλ±(µ)(∆±
00(µ) + Fϵ) for some ϵ± > 0, where
we write Fϵ± instead of F K
ϵ± ({λ± > 0}) for brevity. By applying Lemma 2.2 we get that
(1 + s)λ− − 1 ∈ F1 and D− ∈ Fϵ′
− for some ϵ′
− > 0. Then, using again Lemma 2.2 and the fact
λ+λ− = 1, we can write

Πω
α (y) = (D+ ◦ D−)(y) = (yλ− (∆−
00 + Fϵ− ))λ+ (∆+
00 + Fϵ+ ◦ D−) = ∆00y + F1+ϵ,

with ∆00 = (∆−
00)λ+ ∆+
00 and some ϵ > 0. According to (2.3) and (2.2), in order to compute the
coefficients ∆±
00 we must consider the following functions:

R−
12(y) = P−
1
P−
2 (0, y) = g(−y, 0)
f (−y, 0) − 1,

R−
21(x) = P−
2
P−
1 (x, 0) = 1
1 − c
 [ (−a + b + c − 2) x2 + (a − c + 2) x − 1
(a − b − c + 2) x2 + (−a + b + 2c − 2) x + 1 − c
 ] ,

R+
12(y) = P+
1
P+
2 (0, y) = 1
1 − c
 [ (−a + b − c + 2) y2 + (a + c − 2) y + 1
(a − b + c − 2) y2 + (−a + b − 2c + 2) y + c − 1
 ] ,

R+
21(x) = P+
2
P+
1 (x, 0) = g(x, 0)
f (x, 0) − 1.

Notice that λ := λ+ = 1 − c > 0 and recall that λ− = 1
λ+ . According to (2.2) we consider the

6 D. Marín

functions

log L−
1 (u) := ∫ u

0
 (R−
12(y) + 1
λ−
 ) dy
y = ∫ −u

0
 ( g(x, 0)
f (x, 0) − c) dx
x ,

log L−
2 (u) := ∫ u

0
 (R−
21(x) + λ−) dx
x = 1
1 − c
 ∫ u

0
 (c (a − b − c + 2) x − (ac − c2 − b + c) )dx

(a − b − c + 2) x2 − (a − b − 2c + 2) x − (c − 1) ,

log L+
1 (u) := ∫ u

0
 (R+
12(y) + 1
λ+
 ) dy
y = 1
1 − c
 ∫ u

0
 (c (a − b + c − 2) y − (ac + c2 − b − c) )dy

(a − b + c − 2) y2 − (a − b + 2c − 2) y + (c − 1) ,

log L+
2 (u) := ∫ u

0
 (R+
21(x) + λ+) dx
x = ∫ u

0
 ( g(x, 0)
f (x, 0) − c) dx
x .

From (2.4) we compute the partial derivatives σ±
ijk = ∂k
s σ±
ij (0) of the parametrizations σ±
i (s) =
(σ±
i1 (s), σ±
i2 (s)):

σ−
111 = −1/α, σ−
120 = −α, σ−
210 = 1, σ−
221 = 1, σ+
111 = 1, σ+
120 = 1, σ+
210 = ω, σ+
221 = 1/ω.

Then, according to (2.3) and Remark 1.3, we obtain the following expression:

∆00 = (∆−
00)λ+ ∆+
00 = σ−
111(σ−
120)λ(L−
2 (σ−
210))λ(σ+
111)λσ+
120L+
2 (σ+
210)
L−
1 (σ−
120)(σ−
221)λσ−
210(L+
1 (σ+
120))λσ+
221(σ+
210)λ = (−α)−1+λL+
2 (ω)
ω−1+λL−
1 (−α)
 ( L−
2 (1)
L+
1 (1)
 )λ

= exp (PV ∫ ω

α g1(x, 0)
x f1(x, 0) dx + γ0
) ,

where γ0 := λ log ( L−
2 (1)
L+
1 (1) ). Let us prove now that

γ0 = − π(c(a + b) − 2b)
√d .

With this aim notice that

log L+
1 (u; a, b, c) = log L−
2 (u; −a, −b, c) = α(u; a, b, c) + β(u; a, b, c)

where
 α(u; a, b, c) = c
2(1 − c) log ( 1 − c + (a − b + 2c − 2)u + (−a + b − c + 2)u2

1 − c
 )

and β(u; a, b, c) = − ((a+b)c−2b)
(1−c)√d
 [arctan ( 2(1−c)+b−a+2(a−b+c−2)u√d
 ) − arctan ( 2(1−c)+b−a√d
 )] .

Since α(1; a, b, c) = − c
2(1−c) log(1 − c) we obtain that

log ( L−
2 (1)
L+
1 (1)
 ) = β(1; −a, −b, c) − β(1; a, b, c) = ((a + b)c − 2b)
(1 − c)√d F(a, b, c),

where F(a, b, c) is the following function

arctan (
 b−a−2√d
 ) − arctan (
 b−a+2−2c√d
 ) + arctan ( −b+a−2√d
 ) − arctan ( −b+a+2−2c√d
 ) .

Notice that F(a, b, c) = G(c, e) only depends on c and e = b − a because d = 4(1 − c) − e2. It
can be checked that ∂cG = ∂eG = 0 so that G, and consequently F, is constant. Evaluating at
e = 0 we obtain that F ≡ −π.
To compute γ− it suffices to apply to X the symmetry (x, y) ↦→ (x, −y) that transforms the
invariants (a, b, c) into (−a, −b, c) and the value γ0 into −γ0.

Fake saddles and their transition maps 7

3 Examples and applications

Example 3.1. For each integer n ≥ 3 we consider the vector field

Xn = (x + y)2∂x + yn∂y

having a degenerate singularity at the origin with invariants (a, b, c) = (2, 0, 0) ∈ {d = 0} ∩
{a2 − b2 = 4}.
It can be checked that in the resolution of singularities of X3 appears a saddle-node whose
weak separatrix is not the strict transform of y = 0 and meets transversely the exceptional
divisor. Consequently the origin is not a fake saddle for the vector field X3.
On the other hand, the blowup of the vector field X4

Y0 = (v, uv)∗X4
v = (−(u + 1)2 + u3v2)u∂u + (u + 1)2v∂v

has two singular points on the exceptional divisor v = 0: (u, v) = (0, 0) which is a hyperbolic
saddle and (u, v) = (−1, 0) which is degenerated. Moreover,

Y1 = (u − 1, v)∗Y0 = (u2 + v2 − u3 − 4uv2 + 6u2v2 − 4u3v2 + u4v2)∂u + u2v∂v

has invariants (a, b, c) = (0, 0, 0), so that d = 4 and the transition map along v = 0 is well-
defined for Y1. Thus, the origin is a fake saddle of X4, see Figure 3.1. This example (for which

Figure 3.1: Numerical solutions of X4 = (x + y)2∂x + y4∂y.

a1,1 := a = 2, h0,1 := b = 0 and h1,0 := c = 0) contradicts the following claim of [2]: “it is
readily seen that a necessary condition for the origin to be a fake singularity on the singular
fiber y = 0 is that [. . . ] either (h0,1 − a1,1)2 + 4(h1,0 − 1) < 0, or that h1,0 = 1 and h0,1 = a1,1.”
Moreover, since a = b = 0, according to Theorem 1.2, the derivative at v = 0 of the transition
map Πω
α (v) of Y1 is
 exp PV ∫ ω

α u2

u2 − u3 du = ∣
∣
∣
∣ 1 − α
1 − ω
 ∣
∣
∣
∣ ,

8 D. Marín

so that it is contractive or repulsive on both sides ±v > 0. Notice that the transition map
Π+1
−1(y) of X4 is contractive on one side y > 0 and repulsive on the other side y < 0, see
Figure 3.1.

Example 3.2. Consider the quadratic homogeneous vector field X = (x2 + y2 + axy)∂x +
(cx + by)y∂y with d = 4(1 − c) − (a − b)2 > 0. Taking α = −1 and ω = 1 we have that

PV ∫ ω
α g1(x,0)
f1(x,0) dx
x = PV ∫ 1
−1 cx
x2 dx = 0. Taking also a = 1, b = −1, c = −1 (so that d = 4)

the transition map Π+1
−1 is contractive for y > 0 and expansive for y < 0 in accordance with

Π+1
−1(y) = eγ± y + F1+ϵ, where γ± = 0 ± π (−2(−1)−(1−1)(−1))
2 = ±π depending on the sign ±
of y, see Figure 3.2.

Figure 3.2: Local phase portrait of the vector field (x2 + y2 + xy)∂x − (x + y)y∂y
having first integral ln(y2(2x2 + 2xy + y2)) − 2 arctan( x+y
x ).

To finish this work we apply Theorems 1.1 and 1.2 to the study of the following family of
degenerated singularities considered in [4]:

Zµ :
 { ˙x = βx2y + αxy2 − βy3 − x4,

˙y = 4βxy2 + αy3 + 2x5, µ = (α, β) ∈ R2. (3.1)

According to [4, p. 189], the origin is monodromic for Zµ if and only if β > 1/4.
Blowing up the origin, see Figure 3.3, we have that

Yµ = (x, ux)∗Zµ
x2 = (3βu2 + βu4 + ux + 2x2)∂u + (βu + αu2 − βu3 − x)x∂x

and, assuming that β > 0

Xµ =
 ( x
3β , y
√6β
 )∗ Yµ =
 (
x2 + y2 + xy
√6β + x4

27β2
 )
 ∂x +
 ( x
3 − y
√6β + αx2

9β2 − x3

27β2
 )
 y∂y

is of the form (1.1) with f1(x, y; µ) = 1 + x2
27β2 , f2(x, y; µ) ≡ 1, a(µ) = 1√6β , g1(x, y; µ) =

1
3 + αx
9β2 − x2
27β2 , g2(y; µ) ≡ b(µ) = − 1√6β and c(µ) = 1
3 .

Notice that f1(x, 0; µ) ̸= 0 for all x ∈ R and d(µ) = 4(1 − c(µ)) − (a(µ) − b(µ))2 = 2
3 (4 − 1
β )

is positive if and only if β > 1
4 . By applying Theorem 1.1 we also deduce that the origin is

Fake saddles and their transition maps 9

x

y

x = −ηyx = ηy
 π xy uvv = η

v = −η
 u

x

u = − 1
η u = 1
η

Figure 3.3: Blowup of the origin for the family Zµ in the charts π(x, u) = (x, ux)
and π(v, y) = (vy, y).

monodromic if and only if β > 1
4 . In that case we can apply Theorem 1.2 and consider the
limit (as η → 0+) transition map Π+∞
−∞(y; µ) = eγ±(µ)y + F ∞
1+ϵ({β > 1
4 }) of Xµ, with

γ±(µ) = PV ∫ +∞

−∞
 1
3 + αx
9β2 − x2
27β2

1 + x2
27β2
 dx
x ∓ π
√4β − 1 = π
 ( α

β√3 ∓ 1
√4β − 1
 )
 .

Assuming that β > 1
4 , the Poincaré return map R(x; µ) of Zµ around (0, 0) is the composition
of two transition maps Π+∞
−∞(x; µ) = eγ±(µ)x + F ∞
1+ϵ({β > 1
4 }) of Xµ, one for x > 0 and
the other for x < 0, see Figure 3.3, so that R(x; µ) = eγ(µ)x + F ∞
1+ϵ({β > 1
4 }) with γ(µ) =
γ+(µ) + γ−(µ) = 2πα
β√3 , in agreement with [4, p. 189].

Notice that for any β > 1
4 the origin is a center of Z(0,β) because it is reversible via
(x, y, t) ↦→ (−x, y, −t). Moreover, thanks to the uniform properties of the flat remainder
class F ∞
1+ϵ we can assert that the ciclicity of the origin in the family (3.1) is zero at any
µ0 = (α0, β0) ∈ R2 with β0 > 1
4 . This last assertion can not be deduced from the results
in [4] because they are not uniform with respect to parameters. Indeed, this property is clear
for α0 ̸= 0. Assume now that α0 = 0. We can express the displacement function

R(x; µ) − x = x(e
 2πα
β√3 − 1 + f (x; µ)),

with a remainder term f (x; µ) ∈ F ∞
ϵ which vanishes identically along α = 0. By using the
division result [6, Lemma 4.1] in the flat class F K
L , we can write f (x; µ) = αg(x; µ) for some
g ∈ F ∞
ϵ . If αx ̸= 0 then
 R(x; µ) − x
αx = e
 2πα
β√3 − 1
α + g(x; µ)

tends to 2π
β0√3 ̸= 0 as (x, µ) → (0, µ0). Hence there is no limit cycle for Zµ near the origin for
any µ ≈ µ0.

10 D. Marín

Acknowledgements

This work has been partially funded by the Ministry of Science, Innovation and Universities
of Spain through the grant PID2021-125625NB-I00 and by the Agency for Management of
University and Research Grants of Catalonia through the grant 2021SGR01015.

References

[1] J. C. Artés, F. Dumortier, J. Llibre, Qualitative theory of planar differential systems, Uni-
versitext, Springer-Verlag, Berlin, 2006. https://doi.org/10.1007/978-3-540-32902-2;
MR2256001; Zbl 1110.34002

[2] B. Coll, A. Gasull, R. Prohens, The effect of a singularity on transition maps, Discrete
Contin. Dyn. Syst. Ser. S 18(2025), No. 12, 4021–4039. https://doi.org/10.3934/dcdss.
2025125; MR4974889; Zbl 08109466

[3] P. De Maesschalk, S. Rebollo-Perdomo, J. Torregrosa, Cyclicity of a fake saddle inside
the quadratic vector fields, J. Differential Equations 258(2015), No. 2, 588–620. https://
doi.org/10.1016/j.jde.2014.09.024; MR3274770; Zbl 1314.34066

[4] A. Gasull, V. Mañosa, F. Mañosas, Monodromy and stability of a class of degenerate
planar critical points, J. Differential Equations 182(2002), No. 1, 169–190. https://doi.org/
10.1006/jdeq.2001.4095; MR1912074; Zbl 1013.34028

[5] D. Marín, J. Villadelprat, Asymptotic expansion of the Dulac map and time for un-
foldings of hyperbolic saddles: general setting, J. Differential Equations 275(2021) 684–732.
https://doi.org/10.1016/j.jde.2020.11.020; MR4191338; Zbl 1467.37030

[6] D. Marín, J. Villadelprat, The criticality of reversible quadratic centers at the outer
boundary of its period annulus, J. Differential Equations 332(2022) 123–201. https://doi.
org/10.1016/j.jde.2022.05.026; MR4437712; Zbl 1501.34032

[7] D. Marín, J. Villadelprat, Asymptotic expansion of the Dulac map and time for un-
foldings of hyperbolic saddles: Coefficient properties, J. Differential Equations 404(2024)
43–107. https://doi.org/10.1016/j.jde.2024.05.037; MR4752819; Zbl 1545.34038

[8] I. Nikolaev, E. Zhuzhoma, Flows on 2-dimensional manifolds. An overview, Lecture Notes in
Math., Vol. 1705, Springer-Verlag, Berlin, 1999. https://doi.org/10.1007/BFb0093599;
MR1707298; Zbl 1022.37027
