<!-- source: http://www.dms.umontreal.ca/~rousseac/DGR.pdf | converted from PDF -->

Journal Name ???, 1–30 (???)

ARTICLE NO. HA-00000

Finite cyclicity of elementary graphics surrounding a focus or
center in quadratic systems*

F. Dumortier

Limburgs Universitair Centrum, Universitaire Campus, B-3590, Diepenbeek,
Belgium.

A. Guzm´an

Departamento de Matem´aticas, Facultad de Ciencias, Universidad Nacional
Aut´onoma de M´exico, Ciudad Universitaria, M´exico, D.F. 04510, M´exico.

C. Rousseau

D´epartement de Math´ematiques et de statistique and CRM, Universit´e de
Montr´eal, C.P. 6128, Succursale Centre-Ville, Montr´eal, Qc, H3C 3J7, Canada.

In this paper we prove that several elementary graphics surrounding a focus
or center in quadratic systems have ﬁnite cyclicity. This paper represents an
additional step in the large program to prove the existence of a uniform bound
for the number of limit cycles of a quadratic vector ﬁeld which we can call the
ﬁniteness part of Hilbert’s 16th problem for quadratic vector ﬁelds. It nearly
ﬁnishes the part of the program concerned with elementary graphics. In [3]
this problem was reduced to the proof that 121 graphics have ﬁnite cyclicity.
The graphics considered here are the hemicycles (H 3
4 ), (H 3
5 ) and (H 3
6 ) together
with (I 2
14a), (I 2
15a), (I 2
15b) and (I 2
27) in the notation of [3] (Figure 1).

1. INTRODUCTION

This paper is part of a large program namely the proof of the ﬁniteness
part of Hilbert’s 16th problem [5] for quadratic systems:

Finiteness part of Hilbert’s 16-th problem for quadratic sys-
tems. There exists a natural number N such that any quadratic vector
ﬁeld in the plane has at most N limit cycles.

* This work was supported by NSERC and FCAR in Canada.

1

2 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

In studying this problem it is natural to compactify the phase space to the
Poincar´e disc. The parameter space can be compactiﬁed as well. We obtain
a family {Xλ}λ∈Λ, of analytic vector ﬁelds deﬁned on a compact phase
space and depending on parameters λ varying in a compact set Λ. Using
a compacity argument Roussarie [12] showed that to prove the ﬁniteness
part of Hilbert’s 16-th problem for quadratic vector ﬁelds it is suﬃcient
to prove that any limit periodic set in the family Xλ has ﬁnite cyclicity,
i.e. can give rise to a uniformly bounded number of limit cycles in any
perturbation inside the family Xλ.
The following theorem was proved in [3].

Theorem 1.1 [3]. The ﬁniteness part of Hilbert’s 16-th problem for
quadratic vector ﬁelds will be proved as soon as the following conjecture is
proved.

Conjecture 1.2. Any limit periodic set surrounding the origin in the
family
 ˙x = λx − µy + a1x
2 + a2xy + a3y2

˙y = µx + λy + b1x
2 + b2xy + b3y2, (1)

with (λ, µ) ∈ S1 and (a1, a2, a3, b1, b2, b3) ∈ S5 has ﬁnite cyclicity inside
(1).

The paper [3] then showed that the proof of the Conjecture 1.2 could
be reduced to the proof of the ﬁnite cyclicity of 121 graphics, (54 of them
appearing in families of graphics, yielding a total of 85 pictures). Since
1991, where the conjecture was ﬁrst stated, there has been an intensive
attack to prove the ﬁnite cyclicity of the 121 graphics listed in [3], the most
diﬃcult ones being of course the graphics surrounding a center. We are
now approaching 3/4 of the program with the recent progress on graphics
through a nilpotent point ([13] and [14]) and nearly all elementary graphics
inside the family are proved to have ﬁnite cyclicity.

In this paper we prove the ﬁnite cyclicity of three hemicycles (H 3
4 ), (H 3
5 )
and (H 3
6 ) (Figure 1) with four singular points: two hyperbolic saddles
with opposite hyperbolicity ratio and two saddle nodes. The proof uses
a direct calculation of a displacement map. The ﬁrst two graphics, (H 3
4 ),
(H 3
5 ), satisfy genericity conditions while the third one can be perturbed
to a hemicycle with only two singular points and surrounding a center.

CYCLICITY OF ELEMENTARY GRAPHICS 3

When the hyperbolicity ratios of the saddles are diﬀerent from one, the
generic graphics have cyclicity 2 as soon as some regular transition has a
non vanishing second derivative. Because the transition occurs along an
invariant line or along the equator we are able to calculate explicitly the
required derivative. When the hyperbolicity ratios are equal to one the
genericity condition is the non-vanishing of the ﬁrst saddle quantities. The
ﬁnite cyclicity of (H 3
6 ) follows from a reduction to the previous generic
cases via a Bautin type argument.

We also prove the ﬁnite cyclicity of the graphics (I 2
14a), (I 2
15a), (I 2
15b) and
(I 2
27) (Figure 1). The ﬁnite cyclicity of these graphics was announced in
[1]. However the given elaboration cannot be considered to be a proof since
a connection was incorrectly kept ﬁxed. Here again the proof requires a
condition on the higher derivatives of a regular transition.

Together with the recent proof of the ﬁnite cyclicity of (I 2
2 ) by Mourtada
[11] this nearly completes the proof of the ﬁnite cyclicity of the 58 ele-
mentary graphics listed in [3]. The ﬁnite cyclicity of the graphic (I16a) is
still open and a systematic checking of all proofs remain to be done before
anouncing that the part of the program dealing with elementary graphics
is ﬁnished. For the remaining graphics, 50 of them have a nilpotent point
(many of which are treated in [13] and [14]) while the remaining 13 have a
line of singular points.

2. FINITE CYCLICITY OF GRAPHICS WITH A PAIR OF
HYPERBOLIC POINTS ON THE EQUATOR AND TWO
SEMI-HYPERBOLIC POINTS OF OPPOSITE NATURE

Theorem 2.1. We consider a graphic Γ of a polynomial vector ﬁeld
which is a hemicycle. The pair of opposite singular points are two hy-
perbolic saddles P1 and P2 with irrational hyperbolicity ratios satisfying
r1(λ)r2(λ) ≡ 1. There is one attracting saddle-node P3 on the equator
and one repelling saddle-node P4 on the other connection. Both connec-
tions near P3 and P4 are central (Figure 2). In the neighborhood of each
singular point we use C k-coordinates bringing the family to C k integrable
normal forms. We deﬁne sections to the graphic as in Figure 2. These
sections are parallel to the coordinates axes in the C k normal coordinates
and parametrized by these. Then, under one of the following conditions:

(1) the regular transition S0 : τ2 → σ3 has a non-vanishing higher order
derivative;
(2) the regular transition R0 : τ4 → σ2 has a non-vanishing higher order
derivative;

4 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

the graphic Γ has ﬁnite cyclicity inside Xλ. The cyclicity of Γ is ≤ 2 in the
two following cases: 
 S′′
0 (0) ̸= 0 and r < 1

R′′
0 (0) ̸= 0 and r > 1.

Proof. We take sections σi and τi as in Figure 2. Let us denote

r1(λ) = 1

r(λ) = s(λ) and r2 = r(λ). The connections on the equator are

unbroken.
The technique is standard: we use C k-coordinates in the neighborhood of
the singular points so that the vector ﬁeld is in normal form (see for instance
[8] or [1]). This allows to calculate the return map and to conclude to ﬁnite
cyclicity by a standard derivation-division algorithm.
In the neighborhood of the saddle points the vector ﬁeld can be linearized
so that the Dulac maps have the form

Di,λ(xi) = x
ri(λ)
i . (2)

Also, the normal form of the vector ﬁeld in the neighborhood of P3,4 is

˙xi = x
2
i (1 + Ai(λ)x) + ϵi

˙yi = ±yi, (3)

yielding that the Dulac maps near P3 and P4 are linear of the form

 D3,λ(x3) = m(λ)x3 with limλ→0 m(λ) = 0

D4,λ(x4) = M (λ)x4 with limλ→0 M (λ) = +∞. (4)

Moreover, by the results of [4], the family of C k-coordinates in which we
have the normal form (3) is not unique. Using the freedom in the choice
of coordinates it is possible to ﬁnd normalizing coordinates depending onso that the transition map from τ3 to σ1 is the identity and so that the
transition map from τ1 to σ4 is a mere translation y1 ↦→ y1 + ϵ. Let Sλ
(resp. Rλ) be the regular transition from τ2 to σ3 (resp. from τ4 to σ2)
and let fλ (resp. gλ) be its inverse. We have that fλ(x3) = x3f1,λ(x3) =
∑k
i=1 ai(λ)xi
3 + o(x
k
3) with f1,λ(0) > 0. Let us suppose that gλ(x2) =
∑k
i=0 bi(λ)xi
2 + o(x
k
2), with b0(0) = 0 and b1(0) ̸= 0.
Limit cycles are given by isolated ﬁxed points of the return map or,
equivalently, by isolated solutions of the displacement map Vλ(x3) from σ3

CYCLICITY OF ELEMENTARY GRAPHICS 5

to τ4. Then, renaming x3 by x

Vλ(x) = M (λ)[D1,λ(m(λ)x) + ϵ] − gλ ◦ D−1
2,λ ◦ fλ(x). (5)

Then

Vλ(x) = M (λ)ϵ + M (λ)(m(λ))
s(λ)x
s(λ) − gλ (x
s(λ)(f1,λ(x))
s(λ)) (6)

Note that the map Vλ(x) has a nice expansion in monomials of the form
x
is(λ)+j, allowing to perform the usual derivation-division algorithm. A
ﬁrst derivation kills the constant term. We then divide by x
s(λ)−1. A second
derivative removes completely the term with coeﬃcient M (λ)(m(λ))
s(λ)

and yields Wλ(x) = ( V ′
λ(x)
xs(λ)−1
 )′. The remaining part is an expansion in

monomials of the form x
is(λ)+j, none of which has an unbounded coeﬃcient
(i.e. containing M (λ)). Here we need to distinguish the two cases:

(1) Let us suppose f (n)
0 (0) ̸= 0. In Vλ(x) appears a monomial x
n−1+s(λ)

with nonzero coeﬃcient. After the two derivations and the division it has
produced a monomial x
n−2 with nonzero coeﬃcient. We choose the class of
diﬀerentiability k suﬃciently large so as to be able to continue the classical
derivation division algorithm on Wλ(x) until we kill all monomials of order
of ﬂatness less than n − 2.
(2) Let us suppose g(n)
0 (0) ̸= 0. Similarly in Vλ(x) appears a monomial
x
ns(λ) with nonzero coeﬃcient. After the two derivations and the division
it has produced a monomial x
(n−1)s(λ)−1 with nonzero coeﬃcient. We
choose the class of diﬀerentiability k suﬃciently high so as to be able to
perform the classical derivation division algorithm on Wλ(x) until we kill
all monomials of order of ﬂatness less than (n − 1)s(λ) − 1.

In the particular case n = 2 with the adequate restriction on r(0) the
monomial we are exhibiting in Wλ(x) is precisely the lower order monomial
so Wλ(x) divided by this monomial does not vanish.

Theorem 2.2. We consider a graphic Γ of a polynomial vector ﬁeld
which is a hemicycle. The pair of opposite singular points are two hy-
perbolic saddles P1 and P2 with rational hyperbolicity ratios satisfying
r1(λ)r2(λ) ≡ 1. Moreover there is one attracting saddle-node P3 on the
equator and one repelling saddle-node P4 on the other connection. Both
connections near P3 and P4 are central (Figure 2). Then, under one of the
following conditions:

6 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

(1) the regular transition from τ2 to σ3 has a non-vanishing second order
derivative when r1(0) > 1 ;
(2) the regular transition from τ4 to σ2 has a non-vanishing second order
derivative when r1(0) < 1;
(3) the saddle point P2 has a non-vanishing ﬁrst saddle quantity when
r(0) = 1;

then the graphic Γ has ﬁnite cyclicity ≤ 2 inside Xλ.

Proof. The situation is very similar to the study of hemicycles done
by El Morsalani in [6], the only diﬀerence lying in the presence of the small
(resp. large) coeﬃcient m(λ) (resp. M (λ)). We consider the same displace-
ment map (5) as in Theorem 2.1. The diﬀerence with Theorem 2.1 is that
the Dulac maps Di,λ near Pi, i = 1, 2 have a more complicated expression.
To give it we let r1(0) = p/q = and r2(0) = q/p and α1(λ) = p/q − r1(λ).
Moreover we introduce the Ecalle-Leontovich-Roussarie compensator

ω(x, λ) =
 
 x
−α1 − 1

α1 if α1 ̸= 0

− ln x if α1 = 0.
 (7)

Then it is shown in [6] (see also [1]) that the maps D1,λ and D−1
2,λ have the
form

D1,λ(x1) = x
s(λ)
1 [1 + ∑

1≤j≤i≤K(k) βij(λ)xip
1 ωj(x1, λ)) + Ψ1(x1, λ)], (8)

where Ψ1(x1, λ) = xk
1ψ(x1, λ) is a C k-function, k-ﬂat with respect to
x1 = 0 and ψ(x1, λ) satisﬁes the property I ∞
0 of Mourtada, namely:

∀n ∈ IN lim
x→0 x
n ∂nψ
∂xn (x, λ) = 0 (9)

uniformly for λ in a small neighborhood of the origin in parameter space.
Similarly

D−1
2,λ(x2) = x
s(λ)
2 [1 + ∑

1≤j≤i≤K(k) γij(λ)xip
2 ωj(x2, λ)) + Ψ2(x2, λ)], (10)

with the same compensator ω. Let also fλ(x3) = a1(λ)x3 +a2(λ)x2
3 +o(x
2
3)
with a1(0) ̸= 0 and gλ(x2) = ϵ2 + x2g1,λ(x2) = ϵ2 + ∑k
i=1 bi(λ)xi
2 + o(x
k
2),
with g1,λ(0) ̸= 0.

CYCLICITY OF ELEMENTARY GRAPHICS 7

Alltogether this yields for Vλ(x) an expansion in monomials of the form
x
is(λ)+j ωℓ(x, λ). Expressions of this type have been studied by El Mor-
salani in [6] and the general derivation-division algorithm described, once
a genericity condition is given. We need only make the connection with
his case by identifying the respective coeﬃcients and making sure that the
quantities m(λ) and M (λ) cause no problem.
The ﬁrst terms of the expansion have the form:

Vλ(x) = α000(λ) + α100(λ)xs(λ)

+
 
 a200x
2s(λ) + o(x
2s(λ)) if s(0) < 1
a110x
s(λ)+1 + o(x
1+s(λ)) if s(0) > 1
a111x
s(λ)+1ω(x, λ) + O(xs(λ)+1) if s(0) = 1,
 (11)

where
 α000(λ) = M (λ)ϵ − b0(λ)

α100(λ) = M (λ)(m(λ))s(λ) − (a1(λ))
s(λ)b1(λ). (12)

The ﬁrst part of the algorithm is common to all cases and goes as follows:
We start with a ﬁrst derivation of Vλ(x) to kill the constant term. The
number of zeros of Vλ(x) is at most one plus the number of zeros of Uλ(x) =
x
1−s(λ)V ′
λ(x). A small neighborhood of the origin in parameter space can
be divided into three cones:

(i) the cone M (λ)m(λ)
s(λ)

a1(λ)p/qb1(λ) < 1/2. In that region Uλ(x) < 0 for suﬃ-

ciently small λ yielding at most one root of Vλ(x), i.e. at most one limit
cycle;

(ii) the cone M (λ)m(λ)
s(λ)

a1(λ)p/qb1(λ) > 2. In that region Uλ(x) > 0 for suﬃ-

ciently small λ yielding at most one root of Vλ(x), i.e. at most one limit
cycle;

(iii) the cone 1/3 < M (λ)m(λ)
s(λ)

a1(λ)p/qb1(λ) < 3. In that case it is clear

that M (λ)m(λ)
s(λ) just behaves as a regular nonzero quantity. We con-

sider as before Wλ(x) = ( Uλ(x)
xs(λ)−1
 )′. In the monomials of the expan-

sion of Wλ(x) appear some factors x
is(λ). We transform them by the rule
x
s(λ) = x
p/q(1 + α1ω(x, λ)). Then the function Wλ(x) has an expansion
in monomials of the form x
ip/qωj(x, λ) with j ≤ ip, which is an expansion
exactly of the type studied in [6] (all monomials are well-ordered). We

8 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

analyse the leading term(s) coming from (11) (in the sequel * always de-
notes a nonzero constant, possibly depending on λ but bounded away from
zero):

Wλ(x) =


 [O(m(λ) − ∗b2(λ)(a1(λ))
s(λ)]x
s(λ)−1 + o(x
s(λ)−1) if s(0) < 1
[O(m(λ) − ∗b1(λ)(a1(λ))
s(λ)a2(λ)]x + o(x) if s(0) > 1
[O(m(λ) − ∗β11(λ)(a1(λ))
s(λ)]ω(x, λ) + O(1) if s(0) = 1.
 (13)

In each case we have that Wλ(x) ̸= 0 for small x > 0 and λ, yielding that
the cyclicity is ≤ 2.

3. FINITE CYCLICITY OF HEMICYCLES AMONG
QUADRATIC SYSTEMS

Theorem 3.1. The graphics (H 3
4 ) and (H 3
5 ) have ﬁnite cyclicity (less
than or equal to 2) when the hyperbolic saddles at inﬁnity have irrational
hyperbolicity ratios.

Proof. The proof is a direct application of Theorem 2.1 if we show
that either the regular transition from τ2 to σ3, or the regular transition
from τ4 to σ2 has a non-vanishing second derivative. In fact we will prove
that both transitions simulaneously have non-vanishing second derivative.
Let us hence consider a quadratic system having a graphic of type (H 3
4 )
or (H 3
5 ). For simplicity in calculation it is better to work in regions where
the coordinates are positive. All graphics (possibly modulo some change
of sign in y or t) occur inside the family of quadratic systems:

˙x = x(1 + x + Ay)

˙y = xy + y2 + Bx, (14)

with A > 1 and B ∈ IR (see Figure 1) and the center case (H 3
6 ) corresponds
to B = 0.
The point P2 is studied in the chart (v, w) = (x/y, 1/y) in which the
system has the form (after multiplication by w)

˙v = (A − 1)v + vw − Bv2w

˙w = −w − vw − Bvw2. (15)

CYCLICITY OF ELEMENTARY GRAPHICS 9

The point P3 is studied in the chart (u, z) = (y/x, 1/x) in which the system
has the form (after multiplication by z)

˙u = (1 − A)u2 + Bz − uz

˙z = −z − Auz − z2. (16)

We will show that the second derivatives of the map R : τ4 → σ2 and of
the map S : τ2 → σ3 do not vanish for B(A − 2) ̸= 0 (the condition A ̸= 2
corresponds to the hyperbolicity ratios of the saddle points being diﬀerent
from 1).

Calculation of the second derivative of the map R : τ4 → σ2:
The sections τ4 and σ2 need to be taken parallel to the coordinate axes
in the normalizing coordinates. Let us call (X, Y ) (resp. (V, W )) the
normalizing coordinates around P4 (resp. P2). To calculate the second
derivative of R we write R as a composition six maps. The derivatives and
second derivatives of each of them are calculated using the propositions in
the appendix.

(1) the map R1 from {Y = Y1} to the image of {y = y0} in the (X, Y )-
coordinates, where (X, Y ) = (0, Y1) and (x, y) = (0, y0) represent the same
point and where both sections are parametrized by X. Then R′
1(0) = 1

and R′′
1 (0) = −2 h′
1(0)
Y 2
1 (1 − AY1) , where the section y = y0 has equation

Y = h1(X) = Y1 + O(X);

(2) the map R2 which is the change of coordinate from X to x on {y =
y0}. Let R2(X) = a1X + a2X 2 + o(X 2), with a1 > 0;

(3) the map R3(x) which is the transition from {y = y0} (y0 small) to
{y = Y0} (Y0 large) in the (x, y)-coordinates;

(4) the map R4 which is the transition from the coordinate x to the
coordinate v = x/Y0 on {y = Y0}. Then R4 is linear R4(x) = x/Y0 = xW0,
where W0 = 1/Y0. (Note that the section {y = Y0} becomes the section
{w = W0} in the (v, w)-coordinates;

(5) the change of coordinate R5 from v to V on {w = W0}. Let R5(v) =
b1v + b2v2 + o(v2) with b1 > 0;

(6) the map R6 from the image of {w = W0} in (V, W )-coordinates
to {W = W1}, where (v, w) = (0, W0) and (V, W ) = (0, W1) represent
the same point and both sections are parametrized by V in the (V, W )-

coordinates. Then R′
6(0) = 1 and R′′
6 (0) = h′
2(0)(A − 1)
W1 , where the section

{w = W0} has equation W = h2(V ) = W1 + O(V ).

10 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

Hence
 R′(0) =
 6∏

i=1 R′
i(0) = a1b1R′
3(0)
Y0 > 0 (17)

and

R′′(0) = R′(0) [ −2h′
1(0)
Y 2
1 (1 − AY1) + 2 a2
a1 + a1 R′′
3 (0)
R′
3(0)

+2 a1b2
b1 W0R′
3(0) + a1b1(A − 1)R′
3(0)h′
2(0) W0
W1
 ] .
 (18)

We need calculate the diﬀerent quantities appearing in (18).

Normal form near P4:
To bring the system to normal form we ﬁrst need to diagonalize (14) by
means of (x1, y1) = (x, −Bx + y), yielding

˙x1 = x1 + (1 + AB)x
2
1 + Ax1y1

˙y1 = y2
1 + (1 − AB + 2B)x1y1 − B2(A − 1)x
2
1. (19)

We then divide the system by 1 + (1 + AB)x1 + Ay1. The normal form
coordinates can be taken of the form (X, Y ) = (x, −Bx + y + o(|(x, y)|))
(see Theorem A.3 of the Appendix). This is suﬃcient to show that a1 = 1
and a2 = 0. For B ̸= 0, h′
1(0) has the sign of −B while for B = 0 we have
h′
1(0) = −y0 + o(y0) < 0.

Normal form near P2:
To bring the system to normal form we ﬁrst divide the system (15) by
1 + v + Bvw, yielding

˙v = (A − 1)v + vw − (A − 1)v2 + o(|(v, w)|
2)
˙w = −w. (20)

The normalizing change of coordinates has the form W = w + o(|(v, w)|
3)

and

V = v + v2 + vw + v3

2 + (1 + AB
A − 2
 ) v2w + vw2

2 + o(|(v, w)|
3), (21)

yielding h′
2(0) = 0 and b2
b1 = 1 + AB
A − 2 W0 + o(W0). (Remember that

A = 2 corresponds to hyperbolicity ratios of the saddle points being equal
to 1, a case not considered here.)

CYCLICITY OF ELEMENTARY GRAPHICS 11

Calculation of R′
3(0) and R′′
3 (0):
The formulae (A.6) and (A.7) of the Appendix yield

R′
3(0) = exp (∫ Y0
y0 1 + Ay
y2 dy)

= ( Y0
y0
 )A exp ( 1
y0 − 1
Y0
 ) (22)

and
 R′′
3 (0)
R′
3(0) = 2y−A
0 exp A
y0

∫ Y0
y0 (1 − A)y2 − (1 + AB)y − B
y4 yA exp (− 1
y
 ) dy.
 (23)

The non-vanishing of R′′(0) for B(A − 2) ̸= 0:
We now come back to formula (18): in the bracket the second and ﬁfth
term vanish. Hence

R′′(0)
R′(0) = −2 h′
1(0)
Y 2
1 (1 − AY1) + a1 R′′
3 (0)
R′
3(0) + 2a1 b2
b1 W0R′
3(0). (24)

Using that

Y A−1
0 e
−1/Y0 = yA−1
0 e
−1/y0 + ∫ Y0

y0 [(A − 1)yA−2 + yA−3]e
−1/ydy (25)

we obtain

yA
0 e
−1/y0 R′′(0)
R′(0) = (− 2h′
1(0)
Y 2
1 (1 − AY1) y0 + 2a1 b2
b1
 ) yA−1
0 e
−1/y0

+2a1 ∫ Y0
y0 [(A − 1)βyA−2 + (β − AB)yA−3 − ByA−4]e
−1/ydy
 (26)

where β = b2
b1 − 1. The ﬁrst term is small for y0 small because of the

ﬂatness of e
−1/y0 and Y1 = y0 + o(y0). Moreover the integrand is ﬂat at
y=0 and the integral diverges to sgn(β)∞ as Y0 → +∞. So for small y0
and large Y0
 sgn(R′′(0)) = sgn(β) = sgn B
A − 2 . (27)

12 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

The case B = 0:
In that case the system has a center and the authors made the complete
calculations to verify that, as expected, R′′(0) = 0. Indeed in that case the
ﬁrst integral
 H(x, y) = xy−A exp ( x + 1
y
 ) (28)

allows to explicitly calculate a normalizing change of coordinates

Y = y
x + 1

X = x(1 + x − Ay)
−A (29)

(which does not glue continuously with the one used in the previous case).
With the notations introduced before this yields

a1 = (1 − Ay0)
A

a2 = A(1 − Ay0)
2A−1

h′
1(0) = −y0(1 − Ay0)
A
 (30)

Similarly the linearizing coordinates near P2 are given by

V = v exp(v)

W = w exp ( w
A − 1
 ) (31)

yielding b1 = b2 = 1 and h′
2(0) = 0. Moreover using (25) we obtain the
explicit expression

R′′
3 (0)
R′
3(0) = −2y−A
0 Y A−1
0 exp ( 1
y0 − 1
Y0
 ) + 2
y0 . (32)

Altogether this yields R′′(0) = 0.

Calculation of the second derivative of the map S : τ2 → σ3:
The calculations are exactly the same as for R′′(0). Hence we give less
details. The sections τ2 and σ2 are taken parallel to the coordinate axes
in the normalizing coordinates. Let us call (U, Z) the normalizing coordi-
nates around P3. To calculate the second derivative of S we write S as a
composition six maps whose ﬁrst derivatives and second derivatives will be
calculated as before.

CYCLICITY OF ELEMENTARY GRAPHICS 13

(1) the map S1 from {V = V0} to the image of {v = v0} in the (V, W )-
coordinates where (V, W ) = (V0, 0) and (v, w) = (v0, 0) represent the same
point. As normalizing coordinates (V, W ) near P2 we can choose

(V, W ) = (v + o(|(v, w)|
3), w + 1
A − 1 vw + 1
A − 1 w2 + 1
2(A − 1)2 v2w

+ ( 1
(A − 1)2 + AB
(A − 1)(A − 2)
 ) vw2 + 1
2(A − 1)2 w3 + o(|(v, w)|
3)
) ,

(33)

yielding that S′
1(0) = 1 and S′′
1 (0) = 0;
(2) the map S2 which is the change of coordinate from W to w on {v =
v0}. If S−1
2 (w) = C1w +C2w2 +o(w2) then S2(W ) = c1W +c2W 2 +o(W 2),

with c1 = 1/C1 and c2 = −C2/C 3
1 . Then c1 = 1 − 1
A − 1 v0 + o(v0) and

c2
c2
1 = − C2
C1 = − 1
A − 1 − AB
A − 2 v0 + o(v0); (34)

(3) the map S3 which is the transition from the coordinate w to the
coordinate z = w/v0 = U0z on {v = v0}. Then S3 is linear S3(w) =
w/v0 = U0w, where U0 = 1/v0. (Note that the section {v = v0} becomes
the section {u = U0} in the (u, z)-coordinates;
(4) the map S4(x) which is the transition from {u = U0} (U0 large) to
{u = u0} (u0 small) in the (u, z)-coordinates;
(5) the change of coordinate S5 from z to Z on {u = u0}. Let S5(z) =
d1z + d2z2 + o(z2) with d1 > 0;
(6) the map S6 from the image of {u = u0} to {U = U1}, in the (U, Z)-
coordinates, where (u, z) = (u0, 0) and (U, Z) = (U1, 0) represent the same

point. Then S′
6(0) = 1 and S′′
6 (0) = k′(0)
(A − 1)u2
0(1 − Au0) , where the section

{u = u0} has equation U = k(Z) = U1 + o(Z).

Normal form near P3:
To bring the system to normal form we ﬁrst need to diagonalize (16) by
means of (u1, z1) = (u + Bz, z), yielding

˙u1 = (1 − A)u2
1 + (AB − 1 − 2B)u1z1 + B2z2
1

˙z1 = −z1 − Au1z1 + (AB − 1)z2
1. (35)

We then divide the system by 1 + Au1 − (AB − 1)z1. The normal form
coordinates hence have the form (U, Z) = (u + Bz + o(|(u, z)|), z). This is
suﬃcient to show that d1 = 1, d2 = 0 and that k′(0) has the sign of B.

14 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

Calculation of S′
4(0) and S′′
4 (0):
The formulae (A.6) and (A.7) of the Appendix yield

S′
4(0) = exp (∫ u0
U0 1 + Au
(A − 1)u2 du)

= ( u0
U0
 ) A
A−1 exp ( 1
(A − 1)U0 − 1
(A − 1)u0
 ) (36)

and
 S′′
4 (0)
S′
4(0) = 2U − A
A−1
0 exp 1
(A − 1)U0

∫ u0
U0 −u2 + (AB − 1)u + B
(A − 1)2u4 u A
A−1 exp (− 1
(A − 1)u
 ) du.
 (37)

The non-vanishing of S′′(0) for B ̸= 0:

S′(0) =
 6∏

i=1 S′
i(0) = c1d1S′
4(0)U0 > 0 (38)

and
 S′′(0)
S′(0) = c1
 (2 c2
c2
1 + U0 S′′
4 (0)
S′
4(0) + d1U0S′
4(0)S′′
6 (0)
) . (39)

We use an equivalent of (25) given by

∫ u0
U0 u + 1
(A − 1)u3 u
 A
A − 1 exp (
− 1
(A − 1)u
 ) du

= u
 1
A − 1 exp (− 1
(A − 1)u
 )∣
u0

U0
 .
 (40)

As before we work on

u
 A

A−1
0 e
− 1
(A−1)u0
c1
 S′′(0)
S′(0) = u
 1
A−1
0 e
− 1
(A−1)u0 U0
 ( d1k′(0)
(A − 1)u0(1 − Au0) + 2 c2
c2
1
 ) .

+2U0 ∫ u0
U0
 [
γu2 + (γ + B
A − 1
 ) u + B
A − 1
 ] u A
A−1 −4e
− 1
(A−1)u du,
 (41)

CYCLICITY OF ELEMENTARY GRAPHICS 15

where γ = − 1
A − 1 − c2
c2
1 = ABv0
A − 2 + o(v0). The ﬁrst term is small for small

u0 while the second term is large for large U0 because of the divergence of
the integral as U0 → +∞. Hence S′′(0) has the sign of −B(A − 2).

Theorem 3.2. The graphics (H 3
4 ) and (H 3
5 ) have cyclicity ≤ 2 when
the singular points P1 and P2 have rational hyperbolicity ratios.

Proof. We have shown in Theorem 3.1 that both the second derivatives
of f and g do not vanish when B(A − 2) ̸= 0. This is suﬃcient to conclude
in the case r(0) ̸= 1. In the case r(0) = 1, i.e. A = 2 we calculate the ﬁrst
saddle quantity for system (15). It is equal to 2B ̸= 0.

Theorem 3.3. The graphic (H 3
6 ) has cyclicity ≤ 2 if r(0) ̸= 1 and ≤ 3
if r(0) = 1.

Proof. The proof is more subtle in this case and we need consider the
whole quadratic 5-parameter unfolding (14) where B = 0. This family is
given by
 ˙x = x(1 + x + Ay) + δ1

˙y = xy + y2 + δ2 + δ3x + δ4x
2, (42)

where A is a variable parameter. In the particular case of r = 1, i.e. an
initial value A0 = 2 we will let A = 2 + δ5. The center conditions for
this family correspond to the existence of three invariant lines (possibly
multiple). They are given by

 p1(δ) = δ1 = 0
p2(δ) = δ4 + (A − 1)δ2 = 0
p3(δ) = δ3 + (A − 2)δ2 = 0. (43)

Moreover the ideal I generated by the three polynomials pi(ϵ) is radical.
In the particular case A0 = 2 it coincides for δ5 = 0, i.e. r = 1, with the
ideal of the ﬁrst three saddle quantities at the point P2. (The fact that the
ideal is radical is most probably explained by the fact that the system for= 0 is not located at the intersection of strata of centers.)
The idea is to perform a derivation-division algorithm together with a
Bautin type argument on the displacement map Vδ(x) from σ3 to τ4 deﬁned
in (5). This map has the form

Vδ(x) = M (δ)[D1(m(δ)x) + ϵ(δ)] − gδ ◦ D−1
2,δ ◦ fδ(x). (44)

16 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

We have to distinguish diﬀerent cases. In all of them Vδ(x) vanishes
identically under the center conditions.

(1) r(0) /∈ Q. Let s(δ) = 1
r(δ) . In that case the Dulac maps are simply

of the form y ↦→ ys(δ). Since fδ(0) = 0 the displacement map has the
development

Vδ(x) = a00(δ) + ∑

i + js(δ) ≤ k
j > 0
 aij(δ)x
i+js(δ) + Ψδ(x), (45)

where Ψδ(x) = o(x
k).

The whole argument is to show that we can write (45) as

Vδ(x) =

{ a00(δ)h1(x, δ) + a01(δ)x
s(δ)h2(x, δ) + a11(δ)x
1+s(δ)h3(x, δ) s(0) > 1
a00(δ)h1(x, δ) + a01(δ)x
s(δ)h2(x, δ) + a02(δ)x
2s(δ)h3(x, δ) s(0) < 1,
 (46)

with hi(0, 0) ̸= 0. This is achieved in several steps. We write the rest
of the proof in the case s(0) > 1, the case s(0) < 1 being similar. In the
sequel ∗ denotes a nonzero function of δ.

It is clear that fδ(x) and gδ(x) are linear under the center conditions. Since
fδ and gδ are smooth their non-aﬃne part can be divided in the ideal I.
Hence:
 Wδ(x) = Vδ(x) − a00(δ) − a01x
s(δ)

= p1(δ)k1(x, δ) + p2(δ)k2(x, δ) + p3(δ)k3(x, δ). (47)

The rest of the proof consists in three steps:

• show that p1(δ) = ∗a00(δ)
M (δ) : this is done in Lemma 3.4;

• show that p2(δ) = a01(δ)γ(δ) with γ(δ) = O(δ): this is done in Lemma
3.5;show that a11(δ) = ξ1p1(δ) + ξ2p2(δ) + ξ3p3(δ), with ξ3 ̸= 0: this is done
in Lemma 3.6.

The discussion is then divided in three cones covering a neighborhood K
of the origin. We write it in the case s(0) > 1. In the cone K1 = {δ ∈
K|a00(δ) = max(a00(δ), a01(δ), a11(δ))} we can divide (45) by a00 without
introducing small denominators. The resulting function does not vanish in

CYCLICITY OF ELEMENTARY GRAPHICS 17

K1 if K is suﬃciently small. In K2 = {δ ∈ K|a01(δ) = max(a00(δ), a01(δ),
a11(δ))} we consider V ′
λ(x) which does not vanish in K2 if K is suﬃciently
small. In K3 = {δ ∈ K|a11(δ) = max(a00(δ), a01(δ), a11(δ))} we consider
( V ′
λ(x)
xs(δ)−1
 )′ which does not vanish for x ̸= 0 in K3 if K is suﬃciently small.

(2) r(0) ∈ Q \ {1}. We perform a completely similar argument. Under
the center conditions the system is Darboux integrable (see for instance
[15]) and the ﬁrst integral yields a ﬁrst integral near P2. Hence D1,δ(x1)
in (8) can be written

D1,δ(x1) = x
s(δ)
1 [1 +
 3∑

i=1 pi(λ)hi(x1, λ)] (48)

and a similar form for D−1
2,λ. If s(0) > 1 (resp. s(0) < 1) the ﬁrst term
x
p
1ω(x1, δ) in (8) has order greater than the term with coeﬃcient a11(δ) (as
p > 1) (resp. a02)). Hence all terms with factors of the form ω(x, δ) appear
as o(1) in the functions hi(x, δ) of expression (46), which is still valid in
that case. Substituting (48) in (45) yields an expansion in monomials of
the form x
i+js(δ)ωl(x, δ) plus a C k ﬂat rest, where all monomials of higher
order and the rest can be divided in the ideal of the pi(δ). We conclude as
in the ﬁrst case.
(3) r(0) = 1. The system, localized at P2 by means of (v, w) = (x/y, 1/w)
is given by
 ˙v = v(1 + δ5) + vz + δ1z2 − δ4v3 − δ3v2z − δ2vz2

˙w = −w − vw − δ4v2w − δ3vw2 − δ2w3. (49)

The hyperbolicity ratio is precisely one when δ5 = 0. Under this condition
the three ﬁrst saddle quantities are given by (each Li is simpliﬁed modulo
the Lj, j < i):
 L1 = −δ3

L2 = −3(δ2 + δ4) + δ1 − 4δ1δ4

L3 = δ1(1 − 16δ4)(9 − 4δ4).
 (50)

Again we perform a derivation-division on the map Vλ(x) given in (45),
together with the Bautin argument. Instead of the form (46) we use a form

Vδ(x) = a0(δ)h1(x, δ) + b(δ)xω(x, δ) + a1(δ)xh2(x, δ)

+a2(δ)x
2ω(x, δ)h3(x, δ). (51)

18 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

As before p1(δ) = ∗a0
M (δ) and p2(δ) = γ(δ)a01(δ). Also for the same reason

as before a2(δ) = ξ1p1(δ) + ξ2p2(δ) + ξ3p3(δ) with ξ3 ̸= 0. The proof is
completely standard and can be done as before in the three cones where
each ai, i = 0, 1, 2, is of maximum absolute value. In the ﬁrst cone we
conclude as before. In the last cone an additional derivation division is
necessary to kill the term with coeﬃcient b(δ) before we can divide by the
corresponding ai(δ). This yields that the cyclicity is ≤ 3.

Lemma 3.4. p1(δ) = ∗a00(δ)
M (δ) .

Proof. We need to calculate a00(δ) = M (δ)ϵ(δ) − c0(δ). Clearly both
the functions ϵ(δ) and c0(δ) have to be divisible by δ1. Here c0(δ) represents
the translation term in gδ, so −c0(δ) represents the translation term in Rλ.
We ﬁrst calculate the translation term for the transition map Rλ deﬁned
in the usual coordinates. A scaling is then necessary to transform it in
the normalizing coordinates. We use Proposition A.2 from the Appendix

to show ∂Rλ
∂δ1 (0) > 0, since all factors in (A.10) are positive. A similar

calculation yields ∂ϵ
∂δ1 > 0.

Lemma 3.5. p2(δ) = a01(δ)γ(δ) with γ(δ) = O(δ).

Proof. Let us consider

a01(δ) = (m(δ))
s(δ)M (δ) − (f ′
δ(0))
s(δ)g′
δ(0)

= (f ′
δ(0))
s(δ)g′
δ(0)[(m(δ))
s(δ)M (δ)((f −1
δ )
′(0))
s(δ)(g−1
δ )
′(0) − 1].
(52)

In Figure 2 let us call Gδ : τ1 → σ2 and Fδ : τ2 → σ1. The part in brackets
in (52) represents the diﬀerence N (δ) = (F ′
δ(0))
s(δ)G
′ (0) − 1, where the
sections σ1 and τ2 (resp. τ1 and σ2) are chosen symmetric with respect to
the x-axis.
For δ2 > 0, δ4 < 0 a direct calculation yields

G
′ (0) = limY0→+∞ exp (∫ Y0
−Y0 1 + Ay

y2 + δ2 dy)

= exp ( π
√δ2
 ) .
 (53)

CYCLICITY OF ELEMENTARY GRAPHICS 19

Similarly
 F ′
δ(0) = exp
 (

−π
√ 1
−δ4(A − 1)
 )
 . (54)

Hence, since s(λ) = A − 1:

N (δ) = exp π
 ( 1
√
δ2 −
 √ A − 1
−δ4
 )
 − 1

= π
 ( 1
√δ2 −
 √ A − 1
−δ4
 )
 (1 + o(1))

= π √
−δ4 − √(A − 1)δ2
√
−δ2δ4 (1 + o(1)).
 (55)

It easily follows that p2(δ) = N (δ)γ(δ) with γ(δ) small. As f ′
δ(0), g′
δ(0) ̸= 0
it follows that p2(δ) = γ(δ)a01(δ), with γ small.

Lemma 3.6. a11(δ) = ξ1p1(δ) + ξ2p2(δ) + ξ3p3(δ), with ξ3 ̸= 0.

Proof. The proof follows directly from the calculations of Theorem 3.1.
There we calculated the second derivatives of f0 and g0 for δ1 = δ2 = δ4
and got that they were of the form ∗δ3, where ∗ could be chosen bounded
away from 0 as δ3 is small.

4. FINITE CYCLICITY OF (I 2
27)

This graphic was discussed in [1] (Theorem 4.1) and appears in Figures 1
and 3. When speaking about an “unbroken connection”, as seems to occur
along the equator in (I 2
27) one has to pay attention to what is really meant.
Whenever singularities show up in the unfolding of P3 they have to lie on
the equator and the one closest to P1 will be connected to P1 since the
equator stays invariant. We can say that the connection between P1 and
P3 remains “unbroken”. Whenever the singularities near P3 disappear this
by no means implies that it should be possible to encounter a connection
from P1 to P2 passing near P3 on the contrary. Clearly the graphic (I 2
27)
cannot be approched by graphics with two hyperbolic saddles as in Figure
4. Therefore we necessarily need to consider that the connection between

20 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

P1 and P3 can be broken. The more degenerate (and simpler) case of an
unbroken connection has been studied in ([1], Theorem 4.1). The proof for
(I 2
27) is even simpler as we will show now. We follow the reasoning made
in [1].

Theorem 4.1. The graphic (I 2
27) has cyclicity less than or equal to 2.

Proof. the case r1r2 ̸= 1 was done in [3] and we only need to consider
the case r1(0)r2(0) = 1. The value of r1(0) will not matter in our proof and
we will give diﬀerent proofs depending on whether r2(0) ̸= 1 or r2(0) = 1.
Using the theory of normal forms, we can deﬁne three normalized charts
around each singularity Pi, 1 ≤ i ≤ 3. Near P3 the vector ﬁeld Xλ has
one of the expressions (3) and the Dulac map is as in the ﬁrst line of (4).
The Dulac maps near P1 and P2 have one of the forms (2) or (8). When
r2(0) = 1 we will assume that the vector ﬁeld is in a C k normal form near
P2 allowing to calculate the Dulac map as in (8). This occurs for λ in some
neighbourhood W and for some ﬁnite class of diﬀerentiability which is ﬁxed
by the problem. Let σi and τi with 1 ≤ i ≤ 3 be transverse segments to the
vector ﬁeld Xλ (Figure 3). The essential change with the proof in [1] is to
extend the section σ3 with equation x = −x0 and whose endpoint is chosen
to be on the unstable manifold of P2 to some section σ′
3 ending on the
equator. We choose a coordinate y on σ′
3 so that the equator corresponds
to y = 0 and the unstable manifold of P2 to y = 1 (this is possible modulo
an adequate dilation y ↦→ B(λ)y not changing the normal form expression).
For the proof we simply calculate the displacement map. The Dulac maps
Di,λ : σi → τi near the hyperbolic saddles P1 and P2 have the following
expressions:
 yi = Di,λ(xi) = x
ri(λ)
i (1 + φi(xi, λ)) (56)

where xi and yi are respectively the parameters on σi and τi. The func-
tions φi(xi, λ) verify the property I ∞
0 deﬁned in (9). The Dulac maps are
invertible and their inverses di,λ have similar expansions:

xi = di,λ(yi) = ysi(λ)
i (1 + ψi(yi, λ)) (57)

where si(λ) = 1/ri(λ) and the function ψi(yi, λ) also has the property I ∞
0
deﬁned in (9).
Near the semi-hyperbolic singularity P3, the Dulac map D3,λ : σ3 → τ3
is linear as in (4):
 y3 = D3,λ(x3) = m(λ)x3, (58)

CYCLICITY OF ELEMENTARY GRAPHICS 21

with
 lim
λ→0 m(λ) = 0
+. (59)

The regular maps Ri,λ : τi → σi+1, 1 ≤ i ≤ 3 (note that σ4 = σ1) are
C k–diﬀeomorphisms with respective inverses Si,λ.
A displacement map whose isolated zeros yield the limit cycles close to
Γ is deﬁned as the diﬀerence of the two transition maps from σ3 to σ2.

δλ(x3) = R1,λ ◦ D1,λ ◦ R3,λ ◦ D3,λ(1 + x3) − d2,λ ◦ S2,λ(x3)

with x3 small and x3 = 0 corresponding to the unstable manifold of P2.
The following change of coordinates on σ3

x3 = Rλ(x) = c1(λ)x + o(x), c1(λ) ̸= 0 (60)

transforms the regular map S2,λ into a genuine translation:

S2,λ(Rλ(x)) = x + b(λ) = y (61)

with b(λ) = S2,λ(0). Let us now call x3 = x. Then

δλ(x) = δλ(Rλ(x)) = b1(λ) + M (λ)(∗(1 + x) + φ(x, λ))

−ys2(λ)(1 + ψ(y, λ)). (62)

where M (λ) = m(λ)
r1(λ), ∗ is a nonzero function of the parameter λ, the
function ψ(y, λ) has the property I ∞
0 and φ(x, λ) is of class C k.

(1) r2(0) ̸= 1. A derivation of δ with respect to x yields:

δ′ (x) = M (λ)(∗ + φ1(x, λ)) − s2ys2−1(1 + ψ1(y, λ)) (63)

where the function ψ1(y, λ) has the property I ∞
0 and φ1(x, λ) is of class
C k−1.

The equation δ′ (x) = 0 is equivalent to

N (λ)(∗ + φ2(x, λ)) = y(1 + ψ2(y, λ)) = Y, (64)

where N (λ) = ( M (λ)

s2(λ)
 ) 1
s2(λ)−1 . Using the results of Mourtada in [10], the

function
 Y = y(1 + ψ2(y, λ)). (65)

22 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

is invertible, with inverse:

y = Y (1 + ψ3(Y, λ)), (66)

where ψ3 has property I k−1
0 . The equation (64) is equivalent to:

y = x + b(λ) = N (λ)(∗ + φ2(x, λ))(1 + ψ3(Y (x, λ), λ)). (67)

If s2(0) > 1, then N (λ) → 0 as λ → 0. And (67) has the form

x + b(λ) − N (λ)(∗ + φ3(x, λ)) = 0 (68)

with φ3 having property I k−1
0 . The derivative with respect to x is strictly
positive, yielding at most one solution of (68).

If s2(0) < 1, then N (λ) → +∞ for λ → 0. Going back to (64), keeping
in mind that Y may be taken bounded, and dividing by N (λ), we see that
(64) has no solution.
(2) r2(0) = 1. In that case we go back to (62) and we let

s2(λ) = 1 − α1(λ) (69)

with α1(0) = 0. We introduce the compensator ω(x, λ) as in (7). Equation
(62) can be rewritten as

δλ(y) = b1(λ) + M (λ)(∗(1 + x) + φ(x, λ))

−α1(λ)yω(1 + ξ1(y, λ)) − y(1 + ξ2(y, λ) (70)

where we can write x = y − b(λ), keeping both y and x close to zero.
Knowing that M (λ) → 0 for λ → 0 this equation clearly has at most two
solutions by a classical derivation-division algorithm.

5. FINITE CYCLICITY OF (I 2
14A), (I 2
15A) AND (I15B)

Theorem 5.1. Graphics (I 2
14a) and (I 2
15a) have ﬁnite cyclicity

Proof. The two graphics have the same conﬁguration of singular points
as in Figure 5. We choose the variable x ∈ τ2 (instead of y2) so that
{x = 0} corresponds to the connection for λ = 0. We choose the normal

CYCLICITY OF ELEMENTARY GRAPHICS 23

form coordinates near P3 so that the invariant line at inﬁnity corresponds
to {y3 = 0}. Moreover by a λ-dependent scaling in y3 we take care to have
R2,λ(0) ≡ 1, for suﬃciently small λ. The displacement mapping from τ2 to
σ2 is given by

V (x, λ) = R1,λ ◦ D1,λ ◦ R3,λ ◦ D3,λ ◦ R2,λ(x) − D−1
2,λ(x) (71)

and its isolated zeros give the limit cycles and graphics. Using adequate
normalizing change of coordinates as in [4] it is possible to assume that
R1,λ is an aﬃne map:

x2 = R1,λ(y1) = b0(λ) + b1(λ)y1,

with b0(0) = 0, b1(0) > 0, and R3,λ a linear map:

x1 = R3,λ(y3) = a(λ)y3 (72)

with a(0) > 0. Moreover we let

x3 = R2,λ(x) = 1 + Sλ(x) (73)

where a good choice of x allows to have S′
λ(0) = 1 and Sλ(0) = 0. We
also have y3 = D3,λ(x3) = m(λ)x3 and x2 = D−1
2,λ(x) = M (λ)x where
m(λ), M (λ) → 0 as λ → 0. Finally

Y1 = D1,λ(x1) = x
r(λ)
1 (1 + φ(x1, λ)) (74)

where φ has the property I k
0 .
Hence

V (x, λ) = b0(λ) + N (λ)(1 + Sλ(x))
r(λ)(1 + O(m(λ))) − M (λ)x, (75)

with N (λ) = b1(λ)[a(λ)m(λ)]
r(λ) and where the asymptotic property not
only holds for the function but also for all its derivatives in x up to an a
priori chosen order. Then

V ′(x, λ) = N (λ)r(λ)(1 + Sλ(x))
r(λ)−1S′
λ(x)(1 + O(m(λ))) − M (λ). (76)

This function has a ﬁnite number of small zeros if we can prove that the
function W (x) = (1 + Sλ(x))
r(λ)−1S′
λ(x) has a nonzero derivative at x = 0
for λ = 0. Formally this is the case if we do not have

R(x) = R2,0(x) = 1 + S(x) = (1 + rx)
1/r (77)

24 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

where r = r(0). This will be veriﬁed if we prove that (R(x))
r is not
an aﬃne map, i.e. has a nonvanishing higher derivative. This is done in
Lemma 5.2.

Lemma 5.2. For graphics (I 2
14a), (I 2
15a) inside quadratic systems the
function (R(x))
r is not an aﬃne map and has a nonvanishing higher deriva-
tive.

Proof. The proof is simple and relies on the results of [2], namely
on the choice of adequate normalizing change of coordinates near the two
saddle-nodes. Indeed, using the sectorial normalizing theorem it is possible
to choose normalizing coordinates (xi, yi), i = 2, 3 which are analytic in
the parabolic sectors and then to include these in a normalizing change
of coordinates for the whole family (see results in Appendix). In these
coordinates the map R(x) is analytic. It is always possible to choose the
section on which R(x) is deﬁned with end point on the invariant line which
we suppose to be at x = x0, and the image section having end point on the
equator. To show that (R(x))
r is not an aﬃne map and has a nonvanishing
higher derivative it suﬃces to prove it at one point. We prove it at a point
x near x0. Indeed near x0 the map R(x) is the composition of the regular
transitions considered in Theorem 3.1 (we called them R and S and the r
used here is the s of Theorem 3.1) with the Dulac map for a point with
hyperbolicity ratio r. Since these transitions have a non-vanishing second
derivative for r ̸= 1 and since the saddle is non integrable for r = 1, then
(R(x))
r is not an aﬃne map in the neighborhood of x = x0. (The r here
is the s in Theorem 5.1.)

Theorem 5.3. The graphic (I 2
15b) (Figure 6) has cyclicity ≤ 2.

Proof. We take sections as in Figure 6. We start exactly as in the
proof of Theorem 5.1, the only diﬀerence being that the passage near P2
is now center-unstable. We use the same displacement map V (x, λ) from
τ2 to σ2 given in (71) which we write V (x, λ) = H(x, λ) − D−1
2 (x, λ). The
map D−1
2 (x, λ) is a solution of a Pfaﬀ form ω(x, λ) = F (x, λ)dy − ydx, with
F (x, λ) of the form F (x, λ) = x2(1 + A(λ)x) + ϵ(λ). This allows to use the
method of fewnomials of Khovanskii: solutions of V (x, λ) = 0 are solutions
of the system
 
 H(x, λ) = y

F (x, λ)dy − ydx. (78)

CYCLICITY OF ELEMENTARY GRAPHICS 25

The number of solutions of (78) is bounded by one plus the number of
contact points of ω(x, λ) on y = H(x, λ). These are given by

 y = b0(λ) + N (λ)(1 + Sλ(x))
r(λ)(1 + O(m(λ)))

y = N (λ)r(λ)F (x, λ)(1 + Sλ(x))
r(λ)−1S′
λ(x)(1 + O(m(λ))) (79)

and elimination of y yields

0 = b0(λ) + N (λ) [(1 + Sλ)
r(λ)(1 + O(m(λ)))

−r(λ)F (x, λ)S′
λ(x)(1 + Sλ(x))
r(λ)−1 + O(m(λ))
] , (80)

which has at most one small zero since the ﬁrst derivative does not vanish
for small x and for λ such that N (λ) ̸= 0.

APPENDIX
A.1. Derivatives of regular transition maps

Proposition A.1. Let

X = P (x, y) ∂
∂x + Q(x, y) ∂
∂y (A.1)

be a vector ﬁeld. We consider the transition map R(x) of (A.1) between
two arcs without contact: Σ = {(x, y) = (x, f1(x))} and ̃Σ = {(x, y) =
(x, f2(x))}, in a region where Q(x, y) ̸= 0. Let x = x(x0, y0, y) be the
solution with initial condition x(x0, y0, y0) = x0. Then

dR
dx0 (x0) = exp
 (∫ f2(R(x0))
f1(x0)
 ( P ′
xQ − P Q
′

Q2
 )∣x=x(x0,f1(x0),y) dy
)

1 − ( P

Q
 ) (x0, f1(x0))f ′
1(x0)

1 − ( P
Q
 ) (x0, f2(R(x0)))f ′
2(R(x0)) .
 (A.2)

Formulas for the ﬁrst and second derivatives are given in the particular
case where x0 = 0 and P (0, y) ≡ 0. Let yi = fi(0).

R′(0) = exp (∫ y2

y1
 P ′
x
Q (0, y)dy) . (A.3)

26 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

R′′(0) = R′(0) [2 (f ′
2(0)R′(0) ( Px
Q
 ) (0, y2) − f ′
1(0) ( Px
Q
 ) (0, y1)
)

+ ∫ y2
y1
 ( P ′′
x
Q (0, y) − 2 P ′
xQ
′

Q2 (0, y)
) exp (∫ y
y1 P ′
x
Q (0, z) dz) dy] .

(A.4)

Proof. We transform (A.1) into the equivalent diﬀerential equation

dx
dy = P
Q . (A.5)

The solution is x = x(x0, f1(x0), y) with initial condition x(x0, f1(x0), f1(x0)) =
x0. We have that R(x0) = x(x0, f1(x0), f2(R(x0))). Moreover

∂
∂y ∂x
∂x0 = ∂
∂x0
 ∂x
∂y = ∂
∂x0
 P (x(x0, f1(x0), y), y)
Q(x(x0, f1(x0), y), y)

= P ′
xQ − P Q
′

Q2 ∂x
∂x0 ,
 (A.6)

from which
 ∂x
∂x0 = exp
 (∫ y

f1(x0)
 P ′
xQ − P Q
′

Q2 dy
)
 (A.7)

follows. Hence we can rewrite

dR
dx0 (x0) = exp
 (∫ f2(R(x0))
f1(x0)
 ( P ′
xQ − P Q
′

Q2
 )∣x=x(x0,f1(x0),y) dy
)

1 − ( P

Q
 ) (x0, f1(x0))f ′
1(x0)

1 − ( P
Q
 ) (x0, f2(R(x0)))f ′
2(R(x0)) .
 (A.8)

The second derivative of R is most easily calculated from this formula.
However the general formula is very long. In the particular case x0 = 0 we
get (A.3) and (A.4) for R′(0) and R′′(0).

Proposition A.2. Let

Xδ = P (x, y, δ) ∂
∂x + Q(x, y, δ) ∂
∂y (A.1)

CYCLICITY OF ELEMENTARY GRAPHICS 27

be a vector ﬁeld depending on a small parameter δ. We consider the
transition map R(x, δ) of (A.1) between two arcs without contact: Σ =
{(x, y) = (x, f1(x))} and ̃Σ = {(x, y) = (x, f2(x))}, in a region where
Q(x, y, δ) ̸= 0. Let x = x(x0, y0, y, δ) be the solution with initial condition
x(x0, y0, y0, δ) = x0. Let

F (x0, y, δ) = exp
 (∫ y

f1(x0)
 ( P ′
xQ − P Q
′

Q2
 )∣x=x(x0,f1(x0),z,δ) dz
)
 . (A.9)

Then

∂R

∂δ = F (x0, f2(R(x0, δ)), δ)

[1 − ( P
Q
 ) (x0, f1(x0), f2(R(x0, δ)), δ).f ′
2(R(x0, δ))
]−1

∫ f2(R(x0,δ))
f1(x0)
 ( P ′
δQ − P Q
′

Q2
 )∣x=x(x0,f1(x0),y,δ) F −1(x0, y, δ) dy.

(A.10)

Proof. The proof is very similar to that of the previous proposition.
We start by deriving R(x0, δ) = x(x0, f1(x0), f2(R(x0, δ)), δ) with respect
to δ and get

∂R

∂δ (x0, δ) [1 − ( P
Q
 ) (x0, f1(x0), f2(R(x0, δ)), δ).f ′
2(R(x0, δ))
]

= ∂x
∂δ (x0, f1(x0), f2(R(x0, δ)), δ).
 (A.11)

We let x = x(x0, f1(x0), y, δ) with initial condition x(x0, f1(x0), f1(x0), δ) =
x0 be the solution of (A.5) (which now depends on δ). Then

∂
∂y
 ( ∂x
∂δ
 ) = ∂
∂δ P (x(x0, f1(x0), y, δ), y, δ)
Q(x(x0, f1(x0), y, δ), y, δ)

= ( P
Q
 )
x
 ∂x
∂δ + ( P
Q
 )
δ .
 (A.12)

The result follows by integration and evaluation at y = f2(R(x0, δ)).

A.2. Normalizing coordinates near a saddle-node
We recall the results of [2].

28 F. DUMORTIER, A. GUZM ´AN AND C. ROUSSEAU

An analytic planar saddle-node germ v of multiplicity 2 is formally or-
bitally equivalent by means of a transformation (x, y) ↦→ (z, w) to a poly-
nomial normal form
 v0 = z2(1 + az)
−1 ∂
∂z − w ∂
∂w ; (A.13)

the time orientation may be reversed. An unfolding of a germ v, depending
on the multi-parameter λ is ﬁnitely smoothly orbitally equivalent to the
local family
 vλ = ϵ(λ) ∂
∂z + z2(1 + a(λ)z)
−1 ∂
∂z − w ∂
∂w , (A.14)

where ϵ(0) = 0, [8].
Any complex saddle-node of multiplicity 2 is orbitally analytically equiv-
alent to a germ
 v = v0 + z2R(z, w) ∂
∂w . (A.15)

To state the theorems of [2] we suppose that v has the form (A.15)

Theorem A.3. Consider a real analytic germ of a saddle-node vector
ﬁeld on (IR2, 0) with one zero and one negative eigenvalue and with mul-
tiplicity 2. Then it is C ∞ orbitally equivalent to its normal form (A.13)
by means of a change of coordinate (Z, W ) = (z, w) + o(|(z, w)|). The
equivalence may be taken analytic outside the stable manifold.

Theorem A.4. For any C ∞ unfolding of a germ from Theorem A.3
there exists a ﬁnitely smooth orbital equivalence with the polynomial nor-
mal form (A.14). For the critical parameter value this equivalence is ana-
lytic outside the stable manifold of the saddle-node germ.

ACKNOWLEDGEMENTS

The authors are grateful to Mohamed El Morsalani, Yulij Ilyashenko,
Robert Roussarie and Sergey Yakovenko for helpful discussions.

CYCLICITY OF ELEMENTARY GRAPHICS 29

REFERENCES

1. F. Dumortier, M. El Morsalani and C. Rousseau Hilberts 16th problem for quadratic
systems and cyclicity of elementary graphics, Nonlinearity, Vol. 9, 1996, 1209-1261.

2. F. Dumortier, Y. Ilyashenko and C. Rousseau Normal forms near a saddle-node
and applications to ﬁnite cyclicity of graphics, preprint, Centre de Recherches
Math´ematiques, 2000.

3. F. Dumortier, R. Roussarie and C. Rousseau Hilbert’s 16th problem for quadratic
vector ﬁelds, J. Diﬀerential Equations, Vol. 110, 1994, 86-133.

4. A. Guzm´an and C. Rousseau Genericity conditions for ﬁnite cyclicity of elementary
graphics, J. Diﬀerential Equations, 1999, Vol. 155, 44-72

5. D. Hilbert Mathematische Probleme (lecture), The second International Congress
of Mathematicians Paris 1900, Nachr. Ges. Wiss. Gottingen Math.-Phys. Kl.1900,
253-297, Mathematical developments arising from Hilbert’s problems Proceedings of
Symposium in Pure Mathematics, Vol. 28, 1976 it AMS, F. Browder editor, 50-51.

6. M. El Morsalani Bifurcations de polycycles inﬁnis pour les champs de vecteurs poly-
nomiaux, Annales de la Facult´e des Sciences de Toulouse, Vol. 3, 1994, 387-410.

7. Yu Ilyashenko Nonlinear Stokes phenomena, Advances in Soviet Mathematics, Vol.
14, American Mathematical Society, 1993, 1-55.

8. Yu Ilyashenko and S. Yakovenko Finitely-smooth normal forms of local families of
diﬀeomorphisms and vector ﬁelds, Russian Math. Surveys, Vol. 46, 1991, 1-43.

9. Khovanskii Real analytic varieties with the property of ﬁniteness and complex
Abelian integrals, Func. Anal. Appl., Vol. 18, 1984, 40-50.

10. A. Mourtada Cyclicit´e ﬁnie des polycycles hyperboliques des champs de vecteurs du
plan: mise sous forme normale, Springer Lecture Notes in Mathematics, Vol. 1455,
1990, 272-314.

11. A. Mourtada Projections de sous-ensembles quasi r´eguliers d’Hilbert II, preprint,
Universit´e de Bourgogne # 207, 1999.

12. R. Roussarie A note on ﬁnite cyclicity and Hilbert’s 16th problem, Springer Lecture
Notes in Mathematics, Vol. 1331, 161–168, 1988.

13. H. Zhu and C. Rousseau Finite cyclicity of graphics through a nilpotent singularity
of elliptic or saddle type, to appear in J. Diﬀerential Equations.

14. H. Zhu and C. Rousseau Graphics with a nilpotent singularity in quadratic systems
and Hilbert’s 16th problem, in preparation, 2000.

15. D. Schlomiuk Algebraic particular integrals, integrability and the problem of the
center, Trans. Amer. Math. Soc., Vol. 338, 1993, 799–841.
