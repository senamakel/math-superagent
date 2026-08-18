<!-- source: https://arxiv.org/pdf/2106.01914 | converted from PDF -->

A quantitative version of Tao’s result on the Toeplitz
Square Peg Problem

Ludovic Riﬀord

October 28, 2021

Abstract

Building on a result by Tao, we show that a certain type of simple closed curve
in the plane given by the union of the graphs of two 1-Lipschitz functions inscribes
a square whose sidelength is bounded from below by a universal constant times the
maximum of the diﬀerence of the two functions.

1 Introduction

A subset Γ of the plane R2 is said to inscribe a square if it contains the four vertices
of a square with positive sidelength. The Square Peg Problem raised by Toeplitz [7]
in 1911 can be stated as follows (we recall that a (continuous) curve γ : [0, 1] → R2 is
called closed if γ(0) = γ(1) and simple if the function t ∈ [0, 1) ↦→ γ(t) is injective):

Square Peg Problem. Let γ : [0, 1] → R2 be a simple closed continuous curve. Does
γ([0, 1]) necessarily inscribe a square?

Figure 1: A square in red inscribed in the blue curve

The answer to the Square Peg Problem is known to be ”Yes” for curves with enough
regularity (e.g. convex, piecewise analytic or locally monotone curves) but remains open
in its full generality (in the case of merely continuous simple closed curves). For further
details, we refer for example the interested reader to the survey by Matschke [4]. The
absence of positive result in the continuous case is due, in particular, to the lack of

1arXiv:2106.01914v2  [math.CA]  12 Jun 2021
positive lower bound for the sidelengths of squares inscribed in smooth simple closed
curves (or any curve in a set which is dense, in some sense, in the set of continuous
simple closed curves). As a matter of fact, if we could show for instance that smooth
simple closed curves always inscribe a square whose sidelength is bounded from below
by some quantity depending continuously on the curve (such as for example the area
enclosed by the curve or its diameter) then it would allow us to prove, by a simple ar-
gument of approximation, that any (continuous) simple closed curve inscribes a square.
The aim of the present paper is precisely to show that we can bound from below the
sidelength of squares inscribed in the type of sets investigated by Tao in [6].

Another way to state the Square Peg Problem is to see it as a problem of intersection
of a set with its set of opposite square corners. We say that a triple (O, P, R) in (R2)3

is a square corner if the three points O, P, R are distinct and if

R = Rot
π/2
O (P ),

where Rotπ/2
O : R2 → R2 denotes the rotation of angle π/2 about the point O.
Then, denoting by SC ⊂ (R2)3 the set of square corners, we call opposite corner of
a triple (O, P, R) ∈ SC the unique point Q = Q(O, P, R) which makes the quadrilateral
(OP QR) a square (see Figure 2), that is

Q(O, P, R) := P + −−→
OR.

O

P

R

Q

Figure 2: The point R is the image of P by the rotation of angle π/2 about O and Q
is the opposite corner to O in the square (OP QR)

Now, given a subset Γ of the plane, we deﬁne its set of opposite square corners,
denoted by SOSC(Γ), as the set of opposite corners of all square corners in Γ, that is

SOSC(Γ) := {
Q(O, P, R) | (O, P, Q) ∈ SC ∩ Γ
3}
.

If Γ = γ([0, 1]) with γ : [0, 1] → R2 a simple closed curve, then this set can also be
written as (see Figure 3)

SOSC(Γ) := ⋃

t,u,v∈[0,1)

{
Q(γ(t), γ(u), γ(v)) ∈ R2 | u ̸= t and γ(v) = Rot
π/2
γ(t)(γ(u))
}
.

2
 γ(t)

γ(u)

γ(v)

Q(γ(t), γ(u), γ(v))
 Rot
π/2
γ(t)(Γ)

Figure 3: The set SOSC(Γ) is the union over t ∈ [0, 1) of opposite corners of the form
Q(γ(t), γ(u), γ(v)) where γ(u), γ(v) are such that (γ(t), γ(u), γ(v)) is a square corner

By construction of the set of opposite square corners, the Square Peg Problem is
equivalent to asking whether the set Γ ∩ SOSC(Γ) is empty or not: A set Γ = γ([0, 1]),
with γ : [0, 1] → R2 a simple closed curve, does inscribe a square if and only if the set
Γ ∩ SOSC(Γ) is not empty.

Figure 4: In red a discretization of SOSC(Γ) with Γ the ellipse of equation 4x2 + y2 = 4

Classical transversality arguments can be used to demonstrate1 that the set of op-
posite square corners of a generic smooth simple closed curve is a (non necessarily
connected2) compact smooth manifold of dimension 1 immersed in the plane (see Fig-
ures 4 and 5). Moreover, according to well-known results on the Square Peg Problem in
the generic smooth case asserting that generic smooth (simple closed) curves inscribe

1As a matter if fact, an appropriate Multijet Transversality Theorem (see e.g. [2, Theorem 4.13 p.
57]) allows to show that for a generic smooth simple closed curve, the set of (t, u, v) ∈ S
1 such that
(γ(t), γ(u), γ(v)) ∈ SC is a compact smooth submanifold of dimension 1 of (S
1)3 and that the set of
opposite square corners of the curve is the image of that set by a smooth immersion.
2For example, we can show that if we consider the ellipse Γ of Figure 4 and replace for ϵ > 0
small the (short) piece of Γ joining Aϵ := (1 − ϵ, 2√2ϵ − ϵ2) to Bϵ := (1 − ϵ, 2
√2ϵ + ϵ2) by a (simple
non-closed) curve from Aϵ to Bϵ contained in the ball centered at (1, 0) with radius 10
√ϵ and with
a non-empty set of opposite square corners, then this small deformation generates a new connected
component of SOSC(Γ) for ϵ small enough.
 3

an odd number of squares, one is inclined to think that the intersection of a set with
its set of opposite square corners generically contains exactly a ﬁnite number of points
which is an odd multiple of 4. This conclusion follows from existing results which are
based on purely topological methods that do not rely on the set of opposite square
corners, and as we said before, this type of approach does not allow, a priori, any
estimation on the sidelength of the squares in terms of the “geometry” of the curve.
This is not the case of the method proposed in [6], where Tao proves a conservation
lemma (see Lemma 2.1) that allows to resolve the Square Peg Problem whenever the
set of opposite square corners has a peculiar form.

Figure 5: In red a discretization of SOSC(Γ) where Γ is the blue set

Before proceeding further, we mention that similar constructions of sets of opposite
vertices have been used by Matschke in [5] to deal with the problem of quadrilaterals
inscribed in convex curves. As in our paper, his results are based on a conservation
lemma (see Lemma 2.1) by Karasev [3] and Tao [6] and considerations in terms of area
of some sets related to the set of opposite vertices. We refer the reader to [5] for further
details.

In [6], Tao considers simple closed curves given by the union of the graphs of two
functions with “small” Lipschitz constants. Given an interval I = [T0, T1], two functions
f, g : I → R such that

f (T0) = g(T0), f (T1) = g(T1) and f (t) < g(t) ∀t ∈ (T0, T1)

and setting
 Γ := Γ
f ∪ Γ
g with Γ
f := Graphf (I), Γ
g := Graphg(I),

he shows, roughly speaking3, that, if f and g are (1 − ϵ)-Lipschitz for some ϵ > 0, then
the set SOSC(Γ) is the union of the four sets (see Figure 6)

S1 = {
Q(O, P, R) | (O, P, Q) ∈ SC ∩ (Γf × Γ
f × Γ
g)} ,

S2 = {
Q(O, P, R) | (O, P, Q) ∈ SC ∩ (Γf × Γ
g × Γ
f )} ,

3The result on SOSC(Γ) that we are stating here is not rigorously correct, we refer the reader to
Tao’s paper [6] or to Lemma 3.1 and Remarks 3.2, 3.3 for a better understanding of the situation.

4

S3 = {
Q(O, P, R) | (O, P, Q) ∈ SC ∩ (Γ
g × Γ
g × Γ
f )} ,

S4 = {
Q(O, P, R) | (O, P, Q) ∈ SC ∩ (Γ
g × Γ
f × Γ
g)} ,

Figure 6: The set SOSC(Γ), with Γ the set in blue, is the union of the four non-blue
simple curves

and moreover each of those sets is a Lipschitz simple curve joining the point P0 :=
(T0, f (T0)) = (T0, g(T0)) to the point P1 := (T1, f (T1)) = (T1, g(T1)). Then, Tao applies
a conservation lemma (see Lemma 2.1) to show that the (signed) area enclosed by Γg

and S1 has to be zero. Which implies that the two curves Γg \ {P0, P1} and S1 must
intersect and so proves4 the existence of a square inscribed in Γ. The idea of this present
paper is simply to show that a “quantiﬁcation” of Tao’s approach allows to obtain the
following result:

Theorem 1.1. There is a universal constant C > 0 such that the following property
holds: Let I = [T0, T1] be interval and f, g : I → R be 1-Lipschitz functions such that
f (T0) = g(T0), f (T1) = g(T1) and f (t) < g(t) for all t ∈ (T0, T1), then the set

Graphf (I) ∪ Graphg(I)

inscribes a square of sidelength at least

C · max
t∈I
 {
g(t) − f (t)
}
.

The proof of Theorem 1.1 is sketched in the next section and given with full detail
in Section 3. It provides a constant C equal to 0.018 which seems very far from being
sharp since computer simulations5 suggest that the optimal constant of Theorem 1.1 is
probably 0.5. Although moderately interesting, Theorem 1.1 shows at least that Tao’s
approach might provide an eﬃcient method to quantify the size of squares inscribed in
simple closed curves in term of the geometry of the curve and thus might be certainly

4As we said, we sketch here a simpliﬁed version of Tao’s proof, we refer the reader to [6] for the
complete proof.
5We wrote a computer program in Python to generate at random pairs (f, g) of piecewise aﬃne
functions (over a dyadic partition of [0, 1]) as in Theorem 1.1 and compute the corresponding inscribed
squares. We have not found any inscribed square with sidelength < 0.5 · maxt∈I {g(t) − f (t)}. By the
way, we leave the reader to check the optimal constant has to be ≤ 0.5.

5

useful to settle the Square Peg Problem in the general case. But the road is long, there
are a number of issues. As an example, the second part of the proof of Theorem 1.1
relies heavily on the 1-Lipschitzness assumption on the functions (see next section),
can we weaken this assumption? More precisely, does a variant of Theorem 1.1 (where
max{g − f } can be replaced by another quantity depending on f and g) holds true if
we assume that f ang g are smooth (or by approximation only continuous), but not
necessarily 1-Lipschitz, and that the set SOSC(Γ) contains a simple Lipschitz curve
connecting (T0, f (T0)) = (T0, g(T0)) to (T1, f (T1)) = (T1, g(T1))?

The paper is organized as follows: The main idea of the proof of Theorem 1.1 is
explained in Section 2, its complete proof is given in Section 3, and technical lemmas
are stated and proved in Section 4.

Acknowledgements. The author is indebted to B. Matschke and T. Tao for
bringing several references to his attention.

2 A rough idea of the proof of Theorem 1.1

The proof of Theorem 1.1 is based on two observations. The ﬁrst one, due to Karasev
[3] and Tao [6], is a result showing that some quantity is conserved along a quadruple
of curves which traverse squares (see Figure 7). We refer the reader to [6] for its proof
and more details on the meaning of the integrals involved.
 γ1

γ2

γ3
γ4

Figure 7: For every t, (γ1(t)γ2(t)γ3(t)γ4(t)) is a square

Lemma 2.1. Let γ1, γ2, γ3, γ4 : [t0, t1] → R2 be rectiﬁables curves and x, y, a, b :
[t0, t1] → R be continuous functions such that

γ1(t) = (x(t), y(t))
γ2(t) = (x(t) + a(t), y(t) + b(t))
γ3(t) = (x(t) + a(t) − b(t), y(t) + a(t) + b(t))
γ4(t) = (x(t) − b(t), y(t) + a(t))
 ∀t ∈ [t0, t1]. (2.1)

Then we have the identity
∫

γ1 y dx − ∫

γ2 y dx + ∫

γ3 y dx − ∫

γ4 y dx = a(t1)2 − b(t1)2

2 − a(t0)2 − b(t0)2

2 . (2.2)

The above result will be used to show that if our simple closed curve (made of the
union of the graphs of two 1-Lipschitz functions) does inscribe only squares with small

6

sidelength then some area enclosed by a piece of graph of g together with a piece of the
set of opposite square corners has to be small. The second observation is the following
type of result which gives a lower bound for some integral if the union of the graphs of
two 1-Lipschitz functions inscribes a certain type of square, its proof is given in Figure
8.

Lemma 2.2. Let f, g : [T0, T1] → R be 1-Lipschitz functions such that f (T0) = g(T0),
f (T1) = g(T1) and f (t) < g(t) for all t ∈ (T0, T1) and t, a, b ∈ R be such that

T0 ≤ t, t + a, t − b, t + a − b ≤ T1, a > 0 (2.3)

and
 f (t + a) = f (t) + b
g(t + a − b) = f (t) + a + b
g(t − b) = f (t) + a. (2.4)

Then we have ∫ t+a−b

t−b g(s) ds − ∫ t+a

t f (s) ds ≥ a2 + b2

2 . (2.5)

t t + a

f (t)
f (t) + b

f (t) + a
f (t) + a + b graph of g(· − b)

graph of f

Figure 8: ∫ t+a−b
t−b g(s) ds − ∫ t+a
t f (s) ds = ∫ t+a
t g(s − b) − f (s) ds is larger or equal to
the sum of the blue area and the red area given respectively by a2/2 and b2/2

Then the proof of Theorem 1.1 is divided in two parts:

First part: We note that it is suﬃcient to prove the result for fonctions which are
(1 − ϵ)-Lipschitz for some ϵ > 0 small. Then, we ﬁx ϵ > 0 and two (1 − ϵ)-Lipschitz
functions f and g as in the assumption of Theorem 1.1, we extend them to the whole
real line and consider the set of (possibly degenerate) opposite square corners of the
form Qt = P f
t + Rg
t − Of
t ,

7

where t ∈ R, Of
t = (t, f (t)), P f
t ∈ Γf , Rg
t ∈ Γg and Rg
t is the image of P f
t by the rotation
of angle π/2 with center Of
t . As shown by Tao [6], the function t ∈ R ↦→ Qt is Lipschitz
and injective, so its image is a simple rectiﬁable curve joining (T0, f (T0)) to (T1, f (T1)),
and by construction, the curve t ∈ R ↦→ Qt comes along with three Lipschitz curves
t ∈ R ↦→ Of
t ∈ Γf , t ∈ R ↦→ P f
t ∈ Γf and t ∈ R ↦→ Rg
t ∈ Γg such that (Of
t P f
t QtRg
t )
is always a square (see Lemma 3.1). Therefore, any intersection of (Qt)t∈R with Γg

gives rise to a (possibly degenerate) inscribed square. Furthermore, if we consider two
consecutive intersections of (Qt)t∈R with Γg, say at times t0 < t1 in [T0, T1] then Tao’s
conservation lemma can be used to bound from above the (non-signed) area enclosed
by the simple closed curve made of the concatenation of Q[t0,t1] and the piece Γg joining
Qt0 to Qt1 in terms of the sizelengths of the corresponding squares at t0 and t1 (see
Lemma 3.7). This result allows to show that the smaller are the squares at t0 and t1 the
smaller is the area and the closer to Γg has to be the curve t ∈ R ↦→ Qt (see Lemma 3.9).

Second part: From the ﬁrst part, we need to ﬁgure out what happens when the curve
t ∈ R ↦→ Qt is close to Γg in some sense and to see how to get a contradiction if the
squares at times t0 and t1 are too small. To do this let us imagine, for sake of simplicity,
that Qt is so close to Γg that it belongs indeed to Γg for all t ∈ [t0, t1] and that the
sidelength of the squares at t0, t1 is equal to 0. Then in this case, Tao’s Lemma 2.1
allows to show that we have (compare Lemma 3.8)

∫ t+at−bt

t−bt g(s) ds − ∫ t+at

t f (s) ds = a2
t − b2
t
2 t ∈ [t0, t1],

where we suppose that Of
t , P f
t , Qt and Rg
t satisfy

Of
t = (t, f (t))
P f
t = (t + at, f (t + at)) = (t + at, f (t) + bt)
Qt = (t + at − bt, f (t + at − bt)) = (t + at − bt, f (t) + at + bt)
Rg
t = (t − bt, g(t − bt)) = (t − bt, f (t) + at)
 ∀t ∈ [t0, t1].

Furthermore, Lemma 2.2 implies that we also have

∫ t+at−bt

t−bt g(s) ds − ∫ t+at

t f (s) ds ≥ a2
t + b2
t
2 t ∈ [t0, t1].

Then, we conclude that bt = 0 for all t ∈ [t0, t1] and as a consequence that

g(t) = f (t) + at, g(t + at) = f (t) + at and ∫ t+at

t g(s) − f (s) ds = a2
t
2 ,

for all t ∈ [t0, t1]. This type of property prevents the function g − f to admit a max-
imum at some T ∈ (t0, t1) such that T ∈ (t, t + at) ∈ [t0, t1] for some t ∈ [t0, t1], and
yields a contradiction.

The proof of Theorem 1.1 consists in quantifying all the above arguments to make
the sketch of proof correct.
 8

3 Proof of Theorem 1.1

It is suﬃcient to prove the result for functions f and g which are (1 − ϵ)-Lipschitz for
some ϵ > 0. As a matter of fact, if Theorem 1.1 holds true in this case, then given
f, g : I → R we can deﬁne for every ϵ > 0 small fϵ, gϵ : I → R by fϵ := (1 − ϵ)f and
gϵ := (1 − ϵ)g, apply the result and pass to the limit as ϵ ↓ 0 to obtain the required
inscribed square as the limit of a sequence of squares whose sidelengths are bounded
from below by C · maxt∈I {gϵ(t) − fϵ(t)} which tends to C · maxt∈I {g(t) − f (t)}. So
from now on, we assume that we are given two functions f, g : I → R which are
(1 − ϵ)-Lipschitz for some ϵ > 0 and set

M := max
t∈I
 {
g(t) − f (t)} > 0.

Moreover, as in [6], we extend f and g to the whole real line R by setting

f (t) = g(t) = f (T0) = g(T0) ∀t ≤ T0 and f (t) = g(t) = f (T1) = g(T1) ∀t ≥ T1,

and denote respectively the graphs of f and g over R by Γf and Γg. Then, for every
t ∈ R, we set Of
t = (t, f (t)) and denote by Rotf
t : R2 → R2 the rotation of angle π/2
with center Of
t .

Lemma 3.1. The following properties hold:

(i) For every t ∈ R, the set Rot
f
t (Γf ) ∩ Γg is a singleton equal to {Rg
t } with Rg
t =
Rot
f
t (P f
t ) ∈ Γg and P f
t = (ut, f (ut)) ∈ Γf , where ut ∈ [t + (g(t) − f (t))/2, +∞)
is the unique solution u ∈ R of the equation

g(t + f (t) − f (u)) − f (t) − u + t = 0.

(ii) If t /∈ (T0, T1), then Rotf
t (Γf ) ∩ Γg = {Of
t } = {(t, g(t)}.

(iii) The functions t ∈ R ↦→ P f
t , t ∈ R ↦→ Rf
t and Q : R → R2 deﬁned by

Q(t) = Qt := P f
t + Rg
t − Of
t ∀t ∈ R

are Lipschitz.

(iv) The Lipschitz functions a, b : R → R deﬁned by at := ut − t and bt := f (ut) − f (t)
for all t ∈ R satisfy

P f
t = (t + at, f (t) + bt) = (t + at, f (t + at))
Qt = (t + at − bt, f (t) + at + bt)
Rg
t = (t − bt, f (t) + at) = (t − bt, g(t − bt)) ,

and
 at ≥ g(t) − f (t)
2 , |bt| ≤ at

for all t ∈ R.
 9

(v) The function t ∈ R ↦→ Qt is injective.

Remark 3.2. The triple (Of
t , P f
t , Rg
t ) is not always in SC (the set of square corners),
it is the case if and only if Of
t ̸= P f
t ⇔ ut ̸= 0 ⇔ t ∈ (T0, T1). Moreover, we do not
have necessarily Qt ∈ SOSC(Graphf (I) ∪ Graphg(I)) for all t ∈ (T0, T1) because we
might have that P f
t ∈ Γf \ Graphf (I) (remember that Γf denotes the graph of f over
R) for some t in (T0, T1).

Remark 3.3. If we denote for every t ∈ R, by Rotf,−
t : R2 → R2 the rotation of angle
−π/2 with center Of
t , by Rot
g
t : R2 → R2 the rotation of angle π/2 with center Og
t
and by Rotg,−
t : R2 → R2 the rotation of angle −π/2 with center Og
t , then Lemma 3.1
implies by symmetry (we can exchange the roles of f anf g and/or reverse time) that
for every t ∈ R, the sets Rotf,−
t (Γf ) ∩ Γg, Rotg
t (Γg) ∩ Γf and Rotg,−
t (Γg) ∩ Γf are
singletons and the corresponding mappings t ∈ R ↦→ Q2
t , t ∈ R ↦→ Q3
t and t ∈ R ↦→ Q4
t
are Lipschitz and injective. Moreover, we can check easily that

SOSC(Graphf (I) ∪ Graphg(I)) ⊂ ⋃

t∈[T0,T1]
 {Qt, Q
2
t , Q
3
t , Q
4
t } .

Remark 3.4. Lemma 3.1 requires f and g to be (1 − ϵ)-Lipschitz for some ϵ > 0. If f
and g are only 1-Lipschitz then one can show that for every t ∈ R, the set Rot
f
t (Γf )∩Γg

is either a singleton or a segment of slope ±1.

Proof of Lemma 3.1. Let t ∈ R be ﬁxed. The continuous function ϕt : [t, +∞) → R
deﬁned by ϕt(u) := g(t + f (t) − f (u)) − f (t) − u + t ∀u ∈ R,

satisﬁes lim
u→+∞ ϕt(u) = −∞

and, by 1-lipschitzness of f and g (they are indeed (1 − ϵ)-Lipschitz) and the non-
negativity of g − f , we have

ϕt
 (
t + g(t) − f (t)
2
 ) = g (
t + f (t) − f (
t + g(t) − f (t)
2
 )) − f (t)
2 − g(t)
2

≥ g(t) − ∣
∣
∣
∣f (t) − f (
t + g(t) − f (t)
2
 )∣
∣
∣
∣ − f (t)
2 − g(t)
2

≥ g(t) − ∣
∣
∣
∣ g(t) − f (t)
2
 ∣
∣
∣
∣ − f (t)
2 − g(t)
2 = 0.

Hence there is u ≥ t + g(t)−f (t)
2 such that ϕt(u) = 0, that is, such that

Rot
f
t (u, f (u)) = (t, f (t)) + (f (t) − f (u), u − t) = (t + f (t) − f (u), f (t) + u − t) ∈ Γ
g.

This u is unique because if there is another u′ ∈ R verifying ϕt(u′) = 0, then we have
( by (1 − ϵ)-lipschitzness of f and g)

|u
′ − u| = ∣
∣g(t + f (t) − f (u
′)) − g(t + f (t) − f (u))
∣
∣

≤ (1 − ϵ) ∣
∣f (u
′) − f (u)
∣
∣ ≤ (1 − ϵ)
2|u
′ − u|,

10

which shows that u′ = u. Thus the proof of (i) is complete. We notice that if t /∈
(T0, T1), then ϕt(t) = g(t) − f (t) = 0, which shows that u = t, that is Rg
t = P f
t = Of
t ,
corresponds to the unique point in Rot
f
t (Γf ) ∩ Γg and proves (ii). For every t, t′ in R,
we have
 |ut − ut′|

= ∣
∣g (t + f (t) − f (ut)) − f (t) + t − g (t
′ + f (t′) − f (ut′)
) + f (t
′) − t′∣
∣

≤ ∣
∣g (t + f (t) − f (ut)) − g (t
′ + f (t
′) − f (ut′))∣
∣ + ∣
∣f (t′) − f (t)∣
∣ + ∣
∣t
′ − t
∣
∣

≤ (1 − ϵ) ∣
∣(t + f (t) − f (ut)) − (t
′ + f (t
′) − f (ut′))∣
∣ + (1 − ϵ) ∣
∣t
′ − t∣
∣ + ∣
∣t
′ − t∣
∣

≤ ∣
∣(t + f (t) − f (ut)) − (t
′ + f (t
′) − f (ut′))∣
∣ + 2 ∣
∣t′ − t∣
∣

≤ |f (ut) − f (ut′)| + ∣
∣f (t′) − f (t)∣
∣ + 3 ∣
∣t
′ − t∣
∣

≤ (1 − ϵ) |ut′ − ut| + (1 − ϵ) ∣
∣t′ − t
∣
∣ + 3 ∣
∣t
′ − t
∣
∣ ≤ (1 − ϵ) |ut′ − ut| + 4 ∣
∣t
′ − t∣
∣ ,

which implies that |ut′ − ut| ≤ (4/ϵ)|t′ − t|. This shows that the function t ∈ R ↦→ ut is
Lipschitz and as a consequence that the functions deﬁned in (iii) are Lipschitz. The ﬁrst
part of (iv) is a straightforward consequence of the deﬁnitions of P f
t , Rg
t , Qt and at, bt.
Concerning the second part, at ≥ (g(t) − f (t))/2 follows from ut ≥ t + (g(t) − f (t))/2
and |bt| ≤ at follows from the 1-lipschitzness of f (because f (t + at) = f (t) + bt). To
prove (v) we suppose for contradiction that there are t ̸= t′ ∈ R such that Qt = Qt′.
Then, the point Q = Qt = Qt′ belongs to the two squares

(Of
t P f
t QRg
t ) and (Of
t′P f
t′ QRg
t′),

which shows that P f
t ̸= P f
t′ , Rg
t ̸= Rg
t′ (otherwise Of
t = Of
t′ which is impossible because
t ̸= t′) and that Rg
t (resp. Rg
t′) is the image of P f
t (resp. of P f
t′ ) by the rotation of
angle −π/2 about Q. Therefore, the lines D = (P f
t P f
t′ ) and D′ = (Rg
t Rg
t′) are well-
deﬁned (they pass through diﬀerent points) and D′ is the image of D by the rotation
of angle −π/2 about Q. But since P f
t and P f
t′ belong to Γf and f is (1 − ϵ)-Lipschitz
the angle between D and the horizontal is strictly less than π/4 and consequently the
angle of D′, its image by the rotation of angle −π/2 about Q, with the vertical is
strictly less than π/4. This is a contradiction because Rg
t and Rg
t′ belong to Γg and g
is (1 − ϵ)-Lipschitz.

By construction, for every t ∈ R, the points Of
t , P f
t , Qt and Rg
t form a square, and
in addition the points Of
t and P f
t always belong to Γf and Rg
t always belongs to Γg.
So, we can apply Lemma 2.1 and write some integrals in terms of integrals of f and g.

Lemma 3.5. For every t < t′ ∈ R,
∫ t+at

t f (s) ds−∫ t′+at′

t′ f (s) ds+∫

Q([t,t′]) y dx−∫ t′−bt′

t−bt g(s) ds = a2
t′ − b2
t′
2 − a2
t − b2
t
2 .

Proof of Lemma 3.5. Applying Tao’s Lemma 2.1 with γ1, γ2, γ3, γ4 : [t, t′] → R2 deﬁned
by (see Lemma 3.1)

γ1(s) = Of
s = (s, f (s))
γ2(s) = P f
s = (s + as, f (s) + bs) = (s + as, f (s + as))
γ3(s) = Qs = (s + as − bs, f (s) + as + bs)
γ4(s) = Rg
s = (s − bs, f (s) + as) = (s − bs, g(s − bs)) ,
 ∀s ∈ [t, t
′],

11

we obtain ∫

γ1 y dx − ∫

γ2 y dx + ∫

γ3 y dx − ∫

γ4 y dx = a2
t′ − b2
t′
2 − a2
t − b2
t
2 . (3.1)

Since γ1, γ2 and γ4 are graphs, we have (see [6, Example 3.3])
∫

γ1 y dx = ∫ t′

t f (s) ds, ∫

γ2 y dx = ∫ t′+at′

t+at f (s) ds, ∫

γ4 y dx = ∫ t′−bt′

t−bt g(s) ds.

Then (3.1) gives
∫ t′

t f (s) ds − ∫ t′+at′

t+at f (s) ds + ∫

Q([t,t′]) y dx − ∫ t′−bt′

t−bt g(s) ds = a2
t′ − b2
t′
2 − a2
t − b2
t
2

and we conclude by the equality
∫ t′

t f (s) ds = ∫ t+at

t f (s) ds + ∫ t′+at′

t+at f (s) ds + ∫ t′

t′+at′ f (s) ds.

Let T ∈ (T0, T1) such that (g − f )(T ) = M be ﬁxed and ρ ∈ (0, 1/8) a constant to
be chosen later. We deﬁne t0, t1 ∈ [T0, T1] by

t0 = max
{
t ∈ [T0, T ] | Qt ∈ Γg and at ≤ ρM }

and t1 = min
{
t ∈ [T, T1] | Qt ∈ Γ
g and at ≤ ρM }
,

which are well-deﬁned because aT0 = 0 and aT1 = 0 by Lemma 3.1 (iv). Then we set

τ0 := t0 + at0 − bt0 and τ1 := t1 + at1 − bt1

and note that by construction, the following result holds:

Lemma 3.6. We have
 t0 ≤ τ0 < T < T + 3M
8 < t1 ≤ τ1 (3.2)

and
 Qt0 = (τ0, g(τ0)) , Qt1 = (τ1, g(τ1)) and Qt /∈ Γ
g ∀t ∈ (t0, t1). (3.3)

Furthermore, if we denote by Ω ⊂ R2 the bounded open set enclosed by the curve

γ : [0, t1 − t0 + τ1 − τ0] −→ R2

given by the concatenation of C := Q([t0, t1]) with the reversal of Graphg ([τ0, τ1]) (which
is a simple closed curve thanks to the previous property), then there is σ ∈ {−1, 1}
such that the following property holds: For every τ ∈ (τ0, τ1), there are λτ > 0 and
tτ ∈ (t0, t1) such that

(τ, g(τ ) + σ λ) = Qtτ ∈ C and (τ, g(τ ) + σ s) ∈ Ω ∀s ∈ (0, λτ ). (3.4)

Moreover, if σ = 1 then the curve γ is clockwise oriented and if σ = −1 it is anticlock-
wise oriented.
 12

Proof. By construction and the fact that both at0 − bt0, at1 − bt1 are nonnegative (see
Lemma 3.1 (iv)), we already know that t0 ≤ T ≤ t1, t0 ≤ τ0 and t1 ≤ τ1. Since
Qt0 ∈ Γg, we have, by Lemma 3.1 (iv),

g(τ0) = g (t0 + at0 − bt0) = f (t0) + at0 + bt0 = f (t0 + at0) + at0,

which gives (by 1-lipschitzness of f )

|g(τ0) − f (τ0)| ≤ |g(τ0) − f (t0 + at0)| + |f (t0 + at0) − f (τ0)| ≤ 2at0 ≤ 2ρM. (3.5)

Consequently, if τ0 ≥ T , then we have (remember that |bt0| ≤ at0)

0 ≤ τ0 − T ≤ τ0 − t0 = at0 − bt0 ≤ 2at0 ≤ 2ρM,

which implies (by 2-lipschitzness of g − f )

(g(τ0) − f (τ0)) ≥ (g(T ) − f (T )) − 2 |τ0 − T | ≥ M − 4ρM = (1 − 4ρ) M,

which contradicts (3.5) since ρ < 1/8. Furthermore, since g(t1 − b1) = f (t1) + at1 and
|bt1| ≤ at1, we have (by 1-lipschitzness of f and g)

M − 2(t1 − T ) = g(T ) − f (T ) − 2(t1 − T ) ≤

g(t1) − f (t1)

≤ |g(t1) − g(t1 − bt1)| + |g(t1 − bt1) − f (t1)| ≤ 2at1 ≤ 2ρM

which implies that t1 − T ≥ M (1 − 2ρ)/2 > 3M/8 since ρ ∈ (0, 1/8). So, the proof
of (3.2) is complete. The property (3.3) is a direct consequence of the construction of
t0 and t1. Let us now prove the second part of the statement. The concatenation of
C := Q([t0, t1]) with the reversal of Graphg ([τ0, τ1]) is the curve

γ : [0, t1 − t0 + τ1 − τ0] −→ R2

deﬁned by

γ(s) := { Qt0+s if s ∈ [0, t1 − t0]
(τ1 − (s − t1 + t0), g (τ1 − (s − t1 + t0))) if s ∈ [t1 − t0, t1 − t0 + τ1 − τ0],

for all s ∈ [0, t1 − t0 + τ1 − τ0]. We check easily that γ is Lipschitz and closed as
the concatenation of two Lipschitz curves with the same endpoints (we have, by (3.3),
γ(0) = Qt0 = (τ0, g(τ0)) and γ(t1 −t0) = Qt1 = (τ1, g(τ1))) and that it is simple because
t ∈ R ↦→ Qt is injective and Qt /∈ Γg for all t ∈ [t0, t1] (by (3.3)). Then, by the Jordan
curve Theorem, the image of γ, I := γ([0, t1 − t0 + τ1 − τ0]), divides the plane R2 into
two connected components Ω and O where Ω is the bounded open set enclosed by γ
and O is the complement of Ω. For every τ ∈ (τ0, τ1), the point (τ, g(τ )) belongs to
the image of γ but not to γ([0, t1 − t0]). So, since g is 1-Lipschitz there is hτ > 0
such that the vertical segment centered at (τ, g(τ )) of length 2hτ intersects I only at
(τ, g(τ )) (note that the vertical line through (τ, g(τ )) intersects I at (τ, g(τ )) and at
at least another point of C either at h . By connectedness of Ω and O (and the fact
that they are separated by I), we can show that there is σ ∈ {−1, +1} such that for

13

every τ ∈ (τ0, τ1), (τ, g(τ )) + σ(0, hτ ) belongs to Ω and we can check that γ is clockwise
oriented if σ = 1 and anticlockwise oriented if σ = −1. If for every τ ∈ (τ0, τ1), we
deﬁne λτ > 0 by λτ := min
{
h > 0 | (τ, g(τ )) + σ(0, h) /∈ Ω}
,

then, since Ω is bounded λτ is well-deﬁned, since λτ ≥ hτ λτ is positive, and by
construction (τ, g(τ )) + σ(0, s) ∈ Ω for s ∈ (0, λτ ) and (τ, g(τ )) + σ(0, λτ ) ∈ Ω \ Γg = C
so that there is a unique tτ ∈ [t0, t1] (by Lemma 3.1 (v)) such that (τ, g(τ )) + σ(0, λτ ) =
Qtτ . This completes the proof of the Lemma.

By Lemma 3.6, we know that for every τ ∈ (τ0, τ1) the concatenation of the curve
Cτ := Q([t0, tτ ]) with the vertical segment joining Qtτ to (τ, g(τ )) and the reversal of
Graphg ([τ0, τ ]) is a simple closed curve, we denote by Ωτ the open set enclosed by that
curve and we set Aτ = ∫

Q([t0,tτ ]) y dx − ∫ τ

τ0 g(s) ds.

graph of g

curve C

τ0 τ τ1

Qtτ
Ωτ

Figure 9: The set Ωτ is contained in Ω, the set enclosed by the concatenation of C with
Graphg([τ0, τ1])

The following result follows from Stoke’s formula, Lemma 3.5 and Lemma 4.1 whose
proof can be found in Section 4.

Lemma 3.7. We have

L2(Ωτ ) = |Aτ | ≤ L
2(Ω) ≤ ρ2M 2 ∀τ ∈ (τ0, τ1). (3.6)

Furthermore, if σ = 1, then we have 0 ≤ Aτ ≤ Aτ1 for all τ ∈ [τ0, τ1] and if σ = −1,
then we have Aτ1 ≤ Aτ ≤ 0 for all τ ∈ [τ0, τ1].

Proof of Lemma 3.7. By Lemma 3.6 and Stoke’s formula, we have (see [6, Lemma 3.4])

L
2(Ω) = σ
 (∫

Q([t0,t1]) y dx − ∫ τ1

τ0 g(s) ds
)
 = σAτ1 (3.7)

14

and since for every τ ∈ (τ0, τ1) the concatenation of Cτ with the vertical segment joining
Qtτ to (τ, g(τ )) and the reversal of Graphg ([τ0, τ ]) is a simple closed curve with the
same orientation of γ, we also have

L
2(Ωτ ) = σAτ ∀τ ∈ (τ0, τ1). (3.8)

By construction, Ωτ is contained in Ω for all τ ∈ (τ0, τ1), so we have L2(Ωτ ) = |Aτ | ≤
L2(Ω) for every τ ∈ (τ0, τ1) and the second part of the lemma follows easily from
(3.7)-(3.8). It remains to show that L2(Ω) ≤ ρ2M 2. We note that by Lemma 3.5, we
have ∫

Q([t0,t1]) y dx − ∫ t1+at1 −bt1

t0+at0 −bt0 g(s) ds

= ∫

Q([t0,t1]) y dx − ∫ t1−bt1

t0−bt0 g(s) ds − ∫ t0−bt0

t0+at0 −bt0 g(s) ds − ∫ t1+at1 −bt1

t1−bt1 g(s) ds

= a2
t1 − b2
t1
2 − a2
t0 − b2
t0
2 − ∫ t0+at0

t0 f (s) ds + ∫ t1+at1

t1 f (s) ds

− ∫ t0−bt0

t0+at0 −bt0 g(s) ds − ∫ t1+at1 −bt1

t1−bt1 g(s) ds

= a2
t1 − b2
t1
2 − a2
t0 − b2
t0
2 +
 [∫ t0+at0 −bt0

t0−bt0 g(s) ds − ∫ t0+at0

t0 f (s) ds
]

−
 [∫ t1+at1 −bt1

t1−bt1 g(s) ds − ∫ t1+at1

t1 f (s) ds
]
 .

But Lemma 4.1 gives

a2
ti + b2
ti
2 ≤ ∫ ti+ati −bti

ti−bti g(s) ds − ∫ ti+ati

ti f (s) ds ≤ 3a2
ti − b2
ti
2 ∀i = 0, 1.

Then, we conclude that

−ρ
2M 2 ≤ −a
2
t1 ≤ −a
2
t1 + b
2
t0 ≤ ∫

Q([t0,t1]) y dx − ∫ τ1

τ0 g(s) ds ≤ a2
t0 − b
2
t1 ≤ a2
t0 ≤ ρ2M 2,

which completes the proof of the lemma.

Lemma 3.8. We have for every τ ∈ [τ0, τ1]

∫ τ

tτ −btτ g(s) ds − ∫ tτ +atτ

tτ f (s) ds ≤ a2
tτ − b2
tτ
2 + ρ
2M 2.

Proof of Lemma 3.8. Let τ ∈ [τ0, τ1] be ﬁxed. If σ = 1, then Lemma 3.5 with t = t0

15

and t′ = tτ , the deﬁnition of Aτ and Aτ ≥ 0 (by Lemma 3.7) give

∫ τ

tτ −btτ g(s) ds − ∫ tτ +atτ

tτ f (s) ds

= ∫ τ

tτ −btτ g(s) ds + a2
tτ − b2
tτ
2 − a2
t0 − b2
t0
2 − ∫ t0+at0

t0 f (s) ds

− ∫

Q([t0,tτ ]) y dx + ∫ tτ −btτ

t0−bt0 g(s) ds

= a2
tτ − b2
tτ
2 − a2
t0 − b2
t0
2 + ∫ τ0

t0−bt0 g(s) ds − ∫ t0+at0

t0 f (s) ds − Aτ

≤ a2
tτ − b2
tτ
2 − a2
t0 − b2
t0
2 + ∫ τ0

t0−bt0 g(s) ds − ∫ t0+at0

t0 f (s) ds,

which can be bounded from above, by (4.4) of Lemma 4.1 with δ = 0, by

a2
tτ − b2
tτ
2 − a2
t0 − b2
t0
2 + 3a2
t0 − b2
t0
2 = a2
tτ − b2
tτ
2 + a
2
t0 ≤ a2
tτ − b2
tτ
2 + ρ2M 2.

If σ = −1, then Lemma 3.5 with t = tτ and t′ = t1 gives

∫ τ

tτ −btτ g(s) ds − ∫ tτ +atτ

tτ f (s) ds =

a2
tτ − b2
tτ
2 − a2
t1 − b2
t1
2 − ∫ t1+at1

t1 f (s) ds + ∫

Q([tτ ,t1]) y dx − ∫ t1−bt1

τ g(s) ds

where we have

∫

Q([tτ ,t1]) y dx − ∫ t1−bt1

τ g(s) ds = ∫

Q([t0,t1]) y dx − ∫

Q([t0,tτ ]) y dx

− ∫ τ0

τ g(s) ds − ∫ τ1

τ0 g(s) ds − ∫ t1−bt1

τ1 g(s) ds = Aτ1 − Aτ + ∫ τ1

t1−bt1 g(s) ds.

Therefore, since Aτ1 ≤ Aτ ≤ 0 (by Lemma 3.7), we infer that

∫ τ

tτ −btτ g(s) ds − ∫ tτ +atτ

tτ f (s) ds

≤ a2
tτ − b2
tτ
2 − a2
t1 − b2
t1
2 − ∫ t1+at1

t1 f (s) ds + ∫ τ1

t1−bt1 g(s) ds,

which can be bounded from above, by (4.4) of Lemma 4.1 with δ = 0, by

a2
tτ − b2
tτ
2 − a2
t1 − b2
t1
2 + 3a2
t1 − b2
t1
2 = a2
tτ − b2
tτ
2 + a
2
t1 ≤ a2
tτ − b2
tτ
2 + ρ2M 2.

16

For every µ > 0, we set
 Λµ := {
τ ∈ [τ0, τ1] | λτ ≥ µ}
.

The Lebesgue measure of this set is controlled by the area of Ω, we have:

Lemma 3.9. For every µ > 0, L1(Λµ) ≤ L2(Ω)/µ.

Proof of Lemma 3.9. By Fubini’s Theorem, we have

L
2(Ω) = ∫

R H1(Ω ∩ Vτ ) dτ,

where Vτ denotes the vertical line of abscissa τ . If τ ∈ [τ0, τ1] is such that λτ ≥ µ, then
by (3.4) of Lemma 3.6, the 1-dimensional set Ω ∩ Vτ contains at least a vertical segment
of length µ, so that H1(Ω ∩ Vτ ) ≥ µ. As a consequence, we have that

L
2(Ω) ≥ ∫

Λµ µ dτ = µ L
1 (Λµ) ,

which proves the result.

We are now ready to conclude the proof of Theorem 1.1. We consider a constant
B ≥ 2 to be ﬁxed later and set

ν := ρM and µ := 2Bρ2M.

Since [T + M
4 − M
4B , T + M
4 + M
4B
 ] ⊂ [τ0, τ1] (by (3.2))

and
 L
1 ([
T + M
4 − M
4B , T + M
4 + M
4B
 ]) = M
2B = ν2

µ ,

there exists by Lemma 3.7 (L2(Ω) ≤ ν2) and Lemma 3.9

τ ∈ [T + M
4 − M
4B , T + M
4 + M
4B
 ] (3.9)

such that
 λτ ∈ [0, µ]. (3.10)

We set λ := λτ , t := tτ , a := atτ , b := btτ and

E := ∫ τ

t−b g(s) ds − ∫ t+a

t f (s) ds.

The contradiction will come from two inconsistent bounds for E, one from above given
by Lemma 3.8 and one from below that will follow from Lemma 4.2. On the one hand,
Lemma 3.8 gives
 E ≤ a2 − b2

2 + ν2. (3.11)

17

Now, in order to apply Lemma 4.2, we need to show that τ − a < T . Let us do it. By
Lemma 3.1 (iv), we have
 τ = t + a − b
f (t + a) = f (t) + b
g(t + a − b) = f (t) + a + b − σλ
g(t − b) = f (t) + a,
 (3.12)

which can be used to show that (by using the 1-lipschitzness of f )

0 < a = g(t + a − b) − f (t + a) + σλ

≤ g(τ ) − f (τ ) + |f (t + a − b) − f (t + a)| + σλ

≤ M + |b| + λ. (3.13)

Then, by (3.11) and (4.3) of Lemma 4.1 with δ = −σλ, we have

a2 + b2

2 − σλ(a + b)
2 + λ2

4 ≤ E ≤ a2 − b2

2 + ν2,

which gives by (3.10) and (3.13)

b
2 ≤ ν2 − λ2

4 + σλ(a + b)
2

≤ ν2 − λ2

4 + λ(a + |b|)
2

≤ ν2 − λ2

4 + λM
2 + λ2

2 + λ|b|

≤ ν2 + µ2

4 + µM
2 + µ|b|. (3.14)

The roots of the quadratic polynomial b2 − µb − ν2 − µ2/4 − µM/2 (in the b variable)
are given by
 µ − √
2µ2 + 2µM + 4ν2

2 and µ + √
2µ2 + 2µM + 4ν2

2

so the inequality (3.14) implies that

|b| ≤ µ + √
2µ2 + 2µM + 4ν2

2 = ρM D

with D = D(ρ, B) := Bρ + √
2B2ρ2 + B + 1. (3.15)

By 1-lipschitzness of f and g together with (3.12), we infer that

a = g(t + a − b) − f (t + a) + σλ

= g(τ ) − f (τ ) + f (t + a − b) − f (t + a) + σλ

≥ M − 2(τ − T ) − |b| − µ, (3.16)

18

which yields (by (3.9))

τ − a ≤ τ − M + 2(τ − T ) + |b| + µ

≤ T + M
4 + M
4B − M + 2 ( M
4 + M
4B
 ) + ρM D + 2Bρ2M

= T − M
4
 (
1 − 3
B − 4ρD − 8Bρ2) .

In conclusion, we have proved that if

1 − 3
B − 4ρD − 8Bρ2 > 0, (3.17)

then we have τ − a < T < τ and Lemma 4.2 can be applied to the 2-Lipschitz function
h := g − f . Assuming that (3.17) holds, we obtain
∫ τ

τ −a h(t) dt ≥

h(T )2

4 − a2

2 + h(τ − a)2 + h(τ )2

8 − h(T )(h(τ − a) + h(τ ))
4

+ a (h(T ) − 2T + 2τ )
2 + (T − τ + a)h(τ − a)
2 + (τ − T )h(τ )
2 − (τ − T )2,

where (remember (3.12))

h(T ) = M
h(τ ) = a + δ1 with δ1 := −σλ + f (t + a) − f (t + a − b)
h(τ − a) = a + δ2 with δ2 := f (t) − f (t − b).

So, by setting u := τ − T , we have

∫ τ

τ −a h(s) ds ≥ M 2

4 − a2

2 + (a + δ2)2 + (a + δ1)2

8 − M (2a + δ1 + δ2)
4

+ a (M + 2u)
2 + (a − u)(a + δ2)
2 + u(a + δ1)
2 − u
2

= a2

2 + M 2 − a2

4 + au − u
2

+ (a − M )(δ1 + 3δ2)
4 + δ2
1 + δ2
2
8 + u(δ1 − δ2)
2 + M δ2
2 . (3.18)

By construction, we have u ∈ [M/4(1 − 1/B), M/4(1 + 1/B)] (see (3.9)) and, by (3.13)
and (3.16), M (1 − F ) − 2u ≤ a ≤ M (1 + F )

with F = F (ρ, B) := ρD + 2Bρ2 > 0.

So Lemma 4.3 gives

M 2 − a2

4 + au − u
2 ≥ M 2

16
 (3 − 2
B − 1
B2
 ) − M 2F
4
 (1 + F + 1
B
 ) . (3.19)

19

We need now to bound from below the remaining terms of the right-hand side of (3.18).
We have by 1-lipschitzness of f and g and the above inequalities

|δ1| ≤ λ + |f (t + a) − f (t + a − b)| ≤ µ + |b| ≤ M (2Bρ2 + ρD) ,

|δ2| ≤ |f (t) − f (t − b)| ≤ |b| ≤ M ρD,

0 ≤ u ≤ M
4
 (1 + 1
B
 ) ,

and
 |a − M | = |g(t + a − b) − f (t + a) + σλ − g(T ) + f (T )|

≤ |g(t + a − b) − g(T )| + |f (T ) − f (t + a)| + λ

≤ |τ − T | + |T − τ − b| + µ

≤ 2|τ − T | + |b| + µ

≤ M
2
 (
1 + 1
B
 ) + ρM D + 2Bρ2M.

So we infer that
 (a − M )(δ1 + 3δ2)
4 + δ2
1 + δ2
2
8 + u(δ1 − δ2)
2 + M δ2
2

≥ − |a − M | (δ1| + 3|δ2|)
4 − u (|δ1| + |δ2|)
2 − M |δ2|
2

≥ − M 2

4
 ( 1
2
 (
1 + 1
B
 ) + ρD + 2Bρ2) (2Bρ2 + 4ρD)

− M 2

8
 (1 + 1
B
 ) (2Bρ2 + 2ρD) − M 2

2 ρD. (3.20)

Finally, we note that E can be written as

E = ∫ t+a−b

t−b g(s) − f (s) ds + ∫ t

t−b f (s) ds − ∫ t+a

t+a−b f (s) ds

= ∫ τ

τ −a h(s) ds + ∫ t

t−b f (s) ds − ∫ t+a

t+a−b f (s) ds,

where by 1-lipschitness of f we have
∫ t

t−b f (s) ds − ∫ t+a

t+a−b f (s) ds = ∫ t

t−b f (s) − f (s + a) ds ≥ −|b|a,

and we infer that E satisﬁes
 E ≥ ∫ τ

τ −a h(t) dt − |b|a, (3.21)

where the term ∫ τ
τ −a h(t) dt can be bounded from below thanks to (3.18), (3.19) and
(3.20).
 20

In conclusion, we have proved that if (3.17) is satisﬁed, then, by (3.11), (3.21) and
the related inequalities, we have

a2

2 ≥ a2 − b2

2 ≥ E − ρ
2M 2

≥ ∫ τ

τ −a h(t) dt − |b|a − ρ2M 2

≥ ∫ τ

τ −a h(t) dt − |b||a − M | − |b|M − ρ2M 2

≥ a2

2 + M 2

16
 (3 − 2
B − 1
B2
 ) − M 2

4 G,

where (remembering that F (ρ, B) = ρD + 2Bρ2)

G = G(ρ, B) := F (
1 + F + 1
B
 )

+ (
1 + 1
B + 2ρD + 4Bρ2) (Bρ2 + 2ρD)

+ (1 + 1
B
 ) (Bρ2 + ρD) + 2ρD

+ 2ρD ((
1 + 1
B
 ) + 2ρD + 4Bρ2) + 4ρD + 4ρ2

= 6 (
2 + 1
B
 ) ρD + 4(2 + B)ρ
2 + 9ρ
2D2 + 22Bρ3D + 8B2ρ
4.

and D = Bρ + √2B2ρ2 + B + 1. We obtain a contradiction if the pair ρ, B ∈ (0, 1/8) ×
[2, ∞) satisﬁes

1 − 3
B − 4ρD − 8Bρ2 > 0 and M 2

16
 (
3 − 2
B − 1
B2
 ) − M 2

4 G(ρ, B) > 0. (3.22)

Since we have for every B > 3,

1 − 3
B > 0, 3 − 2
B − 1
B2 > 0 and lim
ρ↓0 4ρD + 8Bρ2 = lim
ρ↓0 G(ρ, B) = 0,

such pairs exist for any choice of B in (3, ∞). For example, if we take B = 4, then
(3.22) is equivalent to requiring that ρ ∈ (0, 1/8) satisﬁes

1
4 > 4ρD + 32ρ2

and

39
16 > 4G(ρ, 4) = 54ρD + 96ρ
2 + 36ρ
2D2 + 352ρ
3D + 512ρ
4

with D = 4ρ + √32ρ2 + 5.

Those properties are satisﬁed for ρ = 0.018.

21

4 Estimates

We gather here the technical lemmas used in the proof of Theorem 1.1.

Lemma 4.1. Let f, g : R → R be 1-Lipschitz functions and t, a, b, δ ∈ R such that

a > 0, |b| ≤ a, (4.1)

and
 f (t + a) = f (t) + b, g(t − b) = f (t) + a, g(t + a − b) = f (t) + a + b + δ. (4.2)

Then ∫ t+a−b

t−b g(s) ds − ∫ t+a

t f (s) ds ≥ a2 + b2

2 + δ(a + b)
2 + δ2

4 (4.3)

and ∫ t+a−b

t−b g(s) ds − ∫ t+a

t f (s) ds ≤ 3a2 − b2

2 + δ(a − b)
2 − δ2

4 . (4.4)

Proof of Lemma 4.1. We ﬁrst note that if h : R → R is a 1-Lipschitz function then we
have for every c, d ∈ R with c ≤ d,

∫ d

c h(s) ds ≥ 1
4 (h(d) − h(c))
2 + 1
2 (d − c) (h(d) + h(c)) − 1
4 (d − c)2. (4.5)

As a matter of fact, given c, d ∈ R with c ≤ d, we can deﬁne the functions φ1, φ2 :
[c, d] → R by
 φ1(s) = h(c) − (s − c) and φ2(s) = h(d) + (s − d),

for all s ∈ R and notice that since h is 1-Lipschitz and h(c) = φ1(c), h(d) = φ2(d), we
have

h(s) ≥ h(c) − |s − c| = φ1(s) and h(s) ≥ g(d) − |s − d| = φ2(s) ∀s ∈ [c, d].

Since φ1 and φ2 are aﬃne with diﬀerent slopes, there is a unique ¯s ∈ R such that
φ1(¯s) = φ2(¯s), it is given by
 ¯s = 1
2
 (h(c) − h(d) + c + d
).

Since ¯s − c = (h(c) − h(d) − c + d)/2 and d − ¯s = (h(d) − h(c) − c + d)/2 ≥ 0 by
1-Lipschitzness of h, we have φ1 ≥ φ2 on [c, ¯s] and φ2 ≥ φ1 on [¯s, d]. Then, we have

∫ d

c h(s) ds ≥ ∫ ¯s

c φ1(s) ds + ∫ d

¯s φ2(s) ds,

22

where ∫ ¯s

c φ1(s) ds = (¯s − c) (h(c) + c) − 1
2
 (¯s2 − c
2)

= (¯s − c) h(c) − 1
2 (¯s − c)
2

= 1
2 (h(c) − h(d) − c + d)h(c) − 1
8 (h(c) − h(d) − c + d)
2

and ∫ d

¯s φ2(s) ds = (d − ¯s)(h(d) − d) + 1
2 (d
2 − ¯s2)

= (d − ¯s) h(d) − 1
2 (d − ¯s)
2

= 1
2 (h(d) − h(c) − c + d)h(d) − 1
8 (h(d) − h(c) − c + d)
2,

which gives (4.5). We can apply (4.5) to h = g on the interval [t − b, t + a − b] and
h = −f on [t, t + a]. We obtain
∫ t+a−b

t−b g(s) ds − ∫ t+a

t f (s) ds ≥

1
4 (g(t + a − b) − g(t − b))
2 + a
2 (g(t + a − b) + g(t − b)) − a2

4

+ 1
4 (−f (t + a) + f (t))
2 + a
2 (−f (t + a) − f (t)) − a2

4 ,

which, by (4.2), gives
∫ t+a−b

t−b g(s) ds − ∫ t+a

t f (s) ds ≥

1
4 (b + δ)
2 + a
2 (2f (t) + 2a + b + δ) − a2

4 + b2

4 + a
2 (−2f (t) − b) − a2

4
and implies (4.3). We can also apply (4.5) to h = −g on the interval [t − b, t + a − b]
and h = f on [t, t + a] to get
∫ t+a−b

t−b −g(s) ds + ∫ t+a

t f (s) ds ≥

1
4 (−g(t + a − b) + g(t − b))
2 + a
2 (−g(t + a − b) − g(t − b)) − a2

4

+ 1
4 (f (t + a) − f (t))
2 + a
2 (f (t + a) + f (t)) − a2

4 .

By (4.2), we obtain
∫ t+a−b

t−b g(s) ds − ∫ t+a

t f (s) ds ≤

− 1
4 (b + δ)2 + a
2 (2f (t) + 2a + b + δ) + a2

4 − b2

4 + a
2 (−2f (t) − b) + a2

4 ,

which gives (4.4).
 23

Lemma 4.2. Let h : R → R be a 2-Lipschitz function and T, τ, a ∈ R such that

τ − a < T < τ. (4.6)

Then we have
∫ τ

τ −a h(t) dt ≥

h(T )2

4 − a2

2 + h(τ − a)2 + h(τ )2

8 − h(T )(h(τ − a) + h(τ ))
4

+ a (h(T ) − 2T + 2τ )
2 + (T − τ + a)h(τ − a)
2 + (τ − T )h(τ )
2 − (τ − T )
2. (4.7)

Proof of Lemma 4.2. Since the function h/2 is 1-Lipschitz, we can apply the lower
bound (4.5) obtained at the beginning of the proof of Lemma 4.1. We obtain that for
every c, d ∈ R, with c ≤ d, we have
∫ d

c h(s) ds ≥ 1
8 (h(d) − h(c))
2 + 1
2 (d − c) (h(d) + h(c)) − 1
2 (d − c)2. (4.8)

We infer that
∫ τ

τ −a h(t) dt

= ∫ T

τ −a h(t) dt + ∫ τ

T h(t) dt

≥ 1
8 (h(T ) − h(τ − a))
2 + 1
2 (T − τ + a) (h(T ) + h(τ − a)) − 1
2 (T − τ + a)
2

+ 1
8 (h(τ ) − h(T ))
2 + 1
2 (τ − T ) (h(τ ) + h(T )) − 1
2 (τ − T )
2

which gives (4.7).

Lemma 4.3. Let M, δ > 0 and B > 1 be ﬁxed. Then for any a, u ∈ R such that

M (1 − δ) − 2u ≤ a ≤ M (1 + δ) and M
4
 (1 − 1
B
 ) ≤ u ≤ M
4
 (
1 + 1
B
 )

we have
 M 2 − a2

4 + au − u
2 ≥ M 2

16
 (3 − 2
B − 1
B2
 ) − M 2δ
4
 (1 + δ + 1
B
 ) . (4.9)

Proof of Lemma 4.3. Let Φ : R2 → R be the function deﬁned by

Φ(a, u) := M 2 − a2

4 + u(a − u) = M 2

4 − (a − 2u)2

4 ∀(a, u) ∈ R
2.

The gradient of Φ is given by

∇Φ(a, u) = − (a − 2u)
2
 ( 1
−2
)

24

So, if it vanishes at (a, u), we have Φ(a, u) = M 2/4 and (a, u) is necessarily a local
maximum of φ. As a consequence, the minimum of Φ on the closed set

F = {(a, u) ∈ R2 | M (1 − δ) − 2u ≤ a ≤ M (1 + δ), M
4
 (
1 − 1
B
 ) ≤ u ≤ M
4
 (
1 + 1
B
 )}

is attained on the boundary. We check easily that the vector (1, −2) is never orthogonal
to the fours faces of the boundary. This shows that the minimum of Φ on F has to be
attained at one of the four corners of F whose images by Φ are given by

Φ (M (1 + δ), M
4
 (1 + ϵ
B
 ))

= M 2

4 (−2δ − δ2) + M
4
 (1 + ϵ
B
 ) (
M (1 + δ) − M
4
 (1 + ϵ
B
 ))

= M 2

16
 (
3 + 2ϵ
B − 1
B2
 ) + M 2

4
 (
−δ − δ2 + ϵδ
B
 )

and
 Φ (
M (1 − δ) − M
2
 (1 + ϵ
B
 ) , M
4
 (1 + ϵ
B
 ))

= M 2

4 − 1
4
 (M (1 − δ) − M (1 + ϵ
B
 ))2

= M 2

4
 (1 − 1
B2
 ) − M 2

4
 ( ϵδ
B + δ2)

for ϵ = ±1. We note that since B > 1, we have 4(1 − 1/B2) > 3 − 2/B − 1/B2, so the
minimum of the four values above is attained for (a, u) = (M (1 + δ), M (1 − 1/B)/4),
so we obtain that

Φ(a, u) ≥ M 2

16
 (
3 + 2ϵ
B − 1
B2
 ) − M 2δ
4
 (
δ + δ2 + δ
B
 ) ,

which proves the result.

References

[1] A. Akopyan and S. Avvakumov. Any cyclic quadrilateral can be inscribed in any
closed convex smooth curve. Forum Math. Sigma, 6, 2018.

[2] M. Golubitsky and V. Guillemin. Stable mapping and their singularities. Graduate
Texts in Mathematics, Vol. 14. Springer-Verlag, New-York-Heidelberg, 1973.

[3] R.N. Karasev. On two conjectures of Makeev. Translated from Zap. Nauchn.
Sem. S.-Peterburg. Otdel. Mat. Inst. Steklov. (POMI) 415 (2013), Geometriya i
Topologiya. 12, 5–14 J. Math. Sci. (N.Y.) 212(5): 521—526, 2016.

[4] B. Matschke. A survey on the square peg problem. Notices Amer. Math. Soc.,
61(4):346–352, 2014.
 25

[5] B. Matschke. Quadrilaterals inscribed in convex curves. Preprint,
https://arxiv.org/abs/1801.01945, 2020.

[6] T. Tao. An integration approach to the Toeplitz square peg problem. Forum Math.
Sigma, 5, 2017.

[7] O. Toeplitz. ¨Uber einige aufgaben der Analysis situs. Verhandlungen der Schweiz-
erischen Naturforschenden Gesellschaft in Solothurn, 4:197, 1911.

Laboratoire J.A. Dieudonn´e, Universit´e Cˆote d’Azur, Parc Valrose, 06108 Nice Cedex
2, France

E-mail address: ludovic.rifford@math.cnrs.fr

26
