<!-- source: http://www.dms.umontreal.ca/~rousseac/epp3_18.pdf | converted from PDF -->

PP-graphics with a nilpotent elliptic singularity in
quadratic systems and Hilbert’s 16th problem

Christiane Rousseau∗

Department of Mathematics and Statistics
University of Montreal, Montreal, Quebec, Canada, H3C 3J7
Huaiping Zhu†

Department of Mathematics and Statistics
York University, Toronto, Ontario, Canada, M3J 1P3

Abstract

This paper is part of the program launched in [4] to prove the ﬁniteness part of
Hilbert’s 16th problem for quadratic system, which consists in proving that 121 graphics
have ﬁnite cyclicity among quadratic systems. We show that any pp-graphic through
a multiplicity 3 nilpotent singularity of elliptic type which does not surround a center
has ﬁnite cyclicity. Such graphics may have additional saddles and/or saddle-nodes.
Altogether we show the ﬁnite cyclicity of 15 graphics of [4]. In particular we prove the
ﬁnite cyclicity of a pp-graphic with an elliptic nilpotent singular point together with a
hyperbolic saddle with hyperbolicity ̸= 1 which appears in generic 3-parameter families
of vector ﬁelds and hence belongs to the zoo of Kotova-Stanzo [11].

1 Introduction

This paper is part of a large attack on the ﬁniteness part of Hilbert’s 16th problem
for quadratic ﬁelds which consists in proving the existence of a uniform bound for the

∗Supported by NSERC and FCAR in Canada, E-mail: rousseac@dms.umontreal.ca
†Partially supported by an NSERC postdoctoral fellowship and Startup fund of York University, E-mail:
huaiping@mathstat.yorku.ca
 1

number of limit cycles of a quadratic vector ﬁeld

P (x, y) ∂
∂x + Q(x, y) ∂
∂x . (1.1)

In [4], the following theorem is proved:

Theorem 1.1. There exists a uniform bound for the number of limit cycles of a quadratic
vector ﬁeld if and only if all limit periodic sets surrounding the origin inside the family
{ ˙x = λx − µy + a1x
2 + a2xy + a3y2

˙y = µx + λy + b1x
2 + b2xy + b3y2 (1.2)

have ﬁnite cyclicity inside (1.2).

The complete list of 121 graphics was also given. The program is progressing well
and several papers have permitted to prove the ﬁnite cyclicity of nearly all elementary
graphics ([1], [2], and [5]). The paper of Dumortier, Roussarie and Sotomayor [7] is the
ﬁrst study of a graphic with a nilpotent point. The ideas have been reﬁned in Zhu and
Rousseau [15] and extended and have permitted to prove the ﬁnite cyclicity of several
graphics of codimension 3 or 4 passing through a nilpotent point of saddle or elliptic
type. The ﬁnite cyclicity theorems usually have genericity conditions on the regular
transition map along the graphic.
In this paper we apply the theorems and/or methods of [15] to all the pp-graphics
through a nilpotent singularity of elliptic type appearing in the list of [4]. In some cases
the ﬁnite cyclicity follows from a veriﬁcation of the genericity conditions inside quadratic
systems while in others the proofs of [15] must be adapted to graphics which may have up
to three additional elementary singular points (one or two hyperbolic saddles and/or one
saddle-node). The proofs given in [15] are very complete. The applications to quadratic
systems require long calculations and checking of details. In the present paper we have
tried to keep the proofs to a minimum as long as they require no new ideas and are
copied on “classical” proofs of ﬁnite cyclicity for elementary graphics.

(a) A pp-graphic

R
 (b) Blow-up

Figure 1: pp-graphics with a nilpotent elliptic point having ﬁnite cyclicity

From the results of [15], we will also be able to prove the ﬁnite cyclicity of several
graphics in [4]: hp-graphics and hh-graphics with a nilpotent elliptic point and graphics
through a nilpotent saddle. As the calculations are quite long and some are subtle, these
will be treated in a forthcoming publication.

2

(a) (H1
6)(F
1
6a) (F 1
6b) (b) (H3
7)(I
2
17a) (I 2
17b)

(c) (H3
9)(I1
5a) (I 1
5b) (d) (H3
10)(I
2
18a) (I 2
18b)

(e) (I2
23)(I
1
7a) (I 1
7b) (f) (I
2
24)(I
1
8a) (I 1
8b)

(g) (I2
25)(I
1
9a) (I 1
9b) (h) (I2
39)(I
1
10a) (I 1
10b)

Figure 2: The 15 pp-graphics for which we prove ﬁnite cyclicity (the ﬁnite cyclicity of (I 1
10a)
is proved in [3])
 3

2 Preliminaries

2.1 General ﬁnite cyclicity theorems

The following theorem is proved in [15]:

Theorem 2.1. A pp-graphic with a triple nilpotent elliptic point (Epp) of any codimen-
sion with 2 parabolic and 2 hyperbolic sectors (Fig. 1) has cyclicity ≤ n (Cycl(Epp) ≤ n)
if the regular transition map R calculated using normalizing coordinates has its n−th
derivative non-vanishing.

To check the hypothesis, we do not need to unfold the family. A simple blow-up
(x, y) = (r¯x, r2 ¯y) will be suﬃcient. As shown in Fig. 1b, we will take normalizing
coordinates near the two nodes on the blow-up circle. The map R is deﬁned on sections
parallel to the coordinate axes deﬁned in these charts.

2.2 Statement of the result

Theorem 2.2. All the 16 pp-graphics listed in Fig. 2 have ﬁnite cyclicity.

Remark 2.3. For the none pp-graphics graphics listed in Fig.2:

1. Graphics (F 1
6b), (I 1
5b), (I 1
7b) and (I 1
8b) have ﬁnite cyclicity by [15].

2. Graphics (I 1
17b) and (I 1
18b) are still open.

3. Graphics (I 1
9b) and (I 1
10b) have ﬁnite cyclicity but the proof is not yet published.

4. The proof of the ﬁnite cyclicity of (I 1
10a) appears in [3].

2.3 Dulac map near a hyperbolic saddle in the plane

To prove the ﬁnite cyclicity results, we need the following statements about the Dulac
maps near a hyperbolic saddle.

Deﬁnition 2.4.

1. A singular point is elementary if it has at least one nonzero eigenvalue. It is
hyperbolic (resp. semi-hyperbolic) if the two eigenvalues are not on the imaginary
axis (resp. exactly one eigenvalue is zero).

2. The hyperbolicity ratio at a hyperbolic saddle is the ratio σ = − λ1
λ2 , where λ1 <
0 < λ2 are the two eigenvalues.

Let (Xλ)λ∈Λ, be a C∞ family of vector ﬁelds deﬁned in the neighborhood of a hy-
perbolic saddle at the origin. We also assume that the coordinate axes are the invariant
manifolds near the saddle point. By normal form theory, we can for any ﬁxed k ∈ N, up
to Ck-equivalence write the family of vector ﬁelds Xλ into some explicit normal form
(cf. [13], [10]). Let σ(λ) be the hyperbolicity ratio of Xλ at the origin.

• If σ(0) is irrational, then, ∀k ∈ N, the family of vector ﬁelds Xλ is Ck-equivalent
to { ˙x = x
˙y = −σ(λ)y (2.1)

for λ in some neighborhood W of the origin in parameter space.

4

1

y
 xO
 Dl
S
 S2

Figure 3: Dulac map near a hyperbolic saddle in the plane

• If σ(0) = p
q ∈ Q, (p, q) = 1. Then ∀k ∈ N, the family Xλ is Ck-equivalent to





 ˙x = x

˙y = y[ − p
q +
 N (k)∑

i=0 αi+1(λ)(xpyq)
i]
. (2.2)

for λ in some neighborhood W of the origin in parameter space. In particular,
α1 = σ(0) − σ(λ).

Let ̃Σ1 = {y = y0} and ̃Σ2 = {x = x0} be two sections transverse to the vector ﬁeld
Xλ (Fig. 3), where x0, y0 > 0 constants. The ﬂow of Xλ induces a Dulac map Dλ(., λ):

Dλ : ̃Σ1 −→ ̃Σ2

for all λ ∈ W .
The Dulac map is C∞ for x > 0. The following theorem of Mourtada ([12]) describes
its behavior near x = 0.

Proposition 2.5. (Mourtada) The Dulac map Dλ can be written as

Dλ(x) = x
σ(λ)[c(λ) + ψ(x, λ)] (2.3)

where c(λ) = y0
xσ(λ)
0 , ψ(x, λ) is C∞ for (x, λ) ∈ (0, x0] × W . Furthermore, ψ satisﬁes the

following property (I ∞
0 ):

(I ∞
0 ) : ∀n ∈ N, lim
x→0 x
n ∂nψ
∂xn (x, λ) = 0 uniformly for λ ∈ W (2.4)

where

1. if σ(0) /∈ Q, then ψ ≡ 0;

2. if σ(0) = p
q , then we have the more precise expression (see [1]).
Let
 ω(x, α1) =
 { x−α1 −1
α1 if α1 ̸= 0
− ln x if α1 = 0. (2.5)

5

be the Ecalle-Roussarie compensator of the vector ﬁeld Xλ where α1(λ) = σ(0) −
σ(λ). Then
 Dλ(x) = xσ(λ)
 

1 + ∑

1≤j≤i≤K(k) βijxipωj + ¯ψk(x, λ)



 (2.6)

where ¯ψk(x, λ) is k−ﬂat.

Consequently the map ψ(x, λ) in (2.3) has the form ψ(x, λ) = o(xη) for all η < 1.

Proposition 2.6. The Ck−normal form for a family unfolding a saddle-node is
{ ˙x = x2 − ε
˙y = ±y(1 + ax). (2.7)

The transition Dulac map from x = −x0 to x = x0 has the form

y ↦→ m(ε)y (2.8)

where lim
ε→0 m(ε) = +∞ (resp. lim
ε→0 m(ε) = 0) for a repelling (resp attracting) saddle-node.

The next proposition developed in [2] and [15] will be used to calculate the ﬁrst and
second order derivatives of a regular transition map of a vector ﬁeld.

Proposition 2.7. Consider the regular transition map R for a vector ﬁeld

˙x = P (x, y)
˙y = Q(x, y) (2.9)

between two arcs without contact Σ1 = {y = y1} and Σ2 = {y = y2}. The formulas are
simpler if we add the following hypotheses

• P (0, y) ≡ 0, so the transition is along the axis x = 0;

• Q(0, y) ̸= 0 for y ∈ (y1, y2).

Then
 R′(0) = exp (∫ y2

y1
 P ′
x
Q (0, y) dy) , (2.10)

R′′(0) = R′(0) ∫ y2

y1
 ( P ′′
x
Q (0, y) − 2 P ′
xQ′
x
Q2 (0, y)
) exp (∫ y

y1
 P ′
x
Q (0, z) dz) dy. (2.11)

2.4 Normal forms near nilpotent singularities of multiplic-
ity 3

We present two normal forms: the classical one of Dumortier and Roussarie [6] which
allows the reader to understand our results with no translation needed and a second one
which has been proved to be particularly convenient in [15] and which is well adapted to
applications to quadratic systems since its principal part is quadratic instead of cubic.
A family containing a triple nilpotent singularity of elliptic type with two parabolic
sectors can be written as ([6])
{ ˙x = y
˙y = −x3 + λ2x + λ1 + y(λ3 + bx + ε2x2 + x3h(x, λ)) + y2Q(x, y, λ) (2.12)

6

Figure 4: An elliptic nilpotent point

where b > 2
√
2 (Fig. 4), λ = (λ1, λ2, λ3, ˆλ) are the parameters, Q(x, y, λ) is C∞ in
(x, y, λ) and of arbitrarily high order in (x, y, λ).
For the purpose of studying the passages in the neighborhood of the nilpotent sin-
gularity, in [15] we developed a new normal form for the unfolding of the nilpotent
singularity of the saddle and elliptic type. For the elliptic case, we have

Theorem 2.8. The family (2.12) is C∞-equivalent to
{ ˙X = Y + µ2 + aX 2
˙Y = µ1 + Y (µ3 + X + ¯ε2X 2 + X 3h1(X, µ)) + X 4h2(X, µ) + Y 2Q(X, Y, µ)
(2.13)
where a ∈ (0, 1
2 ), ¯ε2 = aε2, and µ = (µ1, µ2, µ3, ˆµ) is the parameter, h1(X, µ), h2(X, µ) =
ε2a + O(µ) + O(X) and Q(X, Y, µ) are C∞ and Q(X, Y, µ) is of arbitrary high order in
(X, Y, µ).
If a = 1
2 , the unfolding is of codimension 4, type 1, which corresponds to the case
b = 2√
2 (the two characteristic trajectories coalesce into one).

Remark 2.9. If ε2 = 0, the 3-parameter unfolding (2.13) is not universal. In this case,
the codimension of the nilpotent singularity is at least 4.

2.5 Quadratic systems with a nilpotent singular point in
the ﬁnite plane

Theorem 2.10. A quadratic system with a nilpotent singular point of multiplicity 3 at
the origin and an anti-saddle in the upper half-plane is linearly equivalent to
{ ˙x = y + ax2 + cxy − y2

˙y = xy. (2.14)

where a ̸= 0 and c ∈ R.

Proof. By Jordan normal form theorem, we can write the quadratic system with a triple
nilpotent singular point of saddle or elliptic type at the origin in the form
{ ˙x1 = y1 + a1x2
1 + b1x1y1 + c1y2
1
˙y1 = e1x1y1 + f1y2
1 (2.15)

7

where a1e1 ̸= 0.
By a linear transformation { x1 = 1
e1 x2 − f1
e2
1 y2
y1 = 1
e1 y2

system (2.15) is equivalent to
{ ˙x2 = y2 + a2x2
2 + b2x2y2 + c2y2
2
˙y2 = x2y2. (2.16)

Adding an additional singular point on the y-axis, we should have c2 ̸= 0. This
singular point is an anti-saddle if c2 < 0. By rescaling we get (2.14). It follows from
Theorem 2.10 that for a ∈ (0, 1
2 ), the nilpotent point at the origin is elliptic.

One can verify that for (2.14) with a ∈ (0, 1
2 ), if 0 < c < 2
√
1 − a, we have (H 1
6 ), if
c = 2√
1 − a, we have (H 3
7 ). We will use (2.14) to prove the ﬁnite cyclicity for (H 1
6 ).

2.6 Quadratic systems with a nilpotent singular point at
inﬁnity

Theorem 2.11. A quadratic system with a triple singularity point of elliptic type at
inﬁnity and a ﬁnite singular point of focus or center type can be brought to the form
{ ˙x = δx − y + Ax2

˙y = x + γy + xy (2.17)

with A < 1. For the graphics of Fig.2(c)-(h) we will have 1
2 < A < 1. Moreover,

1. The system has an invariant line y = −1 if γ = 0.

2. The value of “a” in the corresponding normal form (2.13) is a = 1 − A. For the
graphics of Fig.2(c)-(h), 0 < a < 1
2 .

Proof. We can suppose that the nilpotent singular point at inﬁnity is located on the
y-axis and the other singular point at inﬁnity on the x-axis. Then the system can be
brought to the form { ˙x = δ10x + δ01y + δ20x2 + δ11xy
˙y = γ10x + γ01y + γ11xy + γ02y2. (2.18)

For the ﬁnite singular point to be an anti-saddle, we should have δ10γ01 − δ01γ10 > 0.
Localizing the system (2.18) at the singular point at inﬁnity on y-axis by v = x
y , z =
1
y , we then have

{ ˙v = (δ11 − γ02)v + δ01z + (δ20 − γ11)v2 + (δ10 − γ01)vz − γ10v2z
˙z = z(−γ02 − γ01z − γ11v − γ10vz) (2.19)

The singular point (0, 0) of system (2.19) is nilpotent, we should have δ11 = γ02 = 0.
The point is triple if γ11(δ20 − γ11) ̸= 0. By a rescaling and still using the original
coordinates (x, y), we obtain the system (2.17)
Note that to bring (2.19) to the form (2.14), we take X = −v, Y = z.

8

For system (2.17) with A ∈ ( 1
2 , 1) and γ = 0, if 0 < δ < 2√
A, we have (H 3
9 ), if
δ = 2
√
A, we have (H 3
10). To make the calculation easier, we will use an equivalent for
of (2.17) to prove the ﬁnite cyclicity of (H 3
10).
In the following discussions, we will use P to denote the intervals of the parameters
a and A in each case. P is deﬁned in Tab.1.

in the ﬁnite plane at inﬁnity
Elliptic type a ∈ (0, 1
2 ) A ∈ ( 1
2 , 1)

Table 1: The deﬁnition of the interval P in each case

2.7 Blow-up of the family (normal form)

We are interested in the family for a ∈ P where a can depend on parameters and
(x, y, µ) in a neighborhood U × Λ of (0, 0, 0). Taking Λ as a sphere, we make the change
of parameters 



 µ1 = ν3 ¯µ1
µ2 = ν2 ¯µ2
µ3 = ν ¯µ3 (2.20)

where ¯µ = (¯µ1, ¯µ2, ¯µ3) ∈ S2 and ν ∈ (0, ν0). Adding to the system (2.13) the equation
˙ν = 0, we have 



 ˙x = y + ν2 ¯µ2 + ax2

˙y = ν3 ¯µ1 + y[
ν ¯µ3 + x + ε2x2 + x
3h1(x, ν ¯µ)
]

+x
4h2(x, ν ¯µ) + y2Q(x, y, ν ¯µ)
˙ν = 0.
 (2.21)

We then make the weighted blow-up




 x = r¯x
y = r2 ¯y
ν = rρ (2.22)

where r > 0 and (¯x, ¯y, ρ) ∈ S2.
Note that for each ¯µ, the foliation given by {ν = rρ = const} is preserved by X (a,¯µ):

• For {rρ = ν} with ν > 0, the leaf is a regular manifold of dimension 2.

• For {rρ = 0}, we get a stratiﬁed set in the critical locus. As shown in Fig. 5, there
are two strata of 2-dimensional manifolds:

– ˆF¯µ ∼= S1 × R+ the blow-up of the ﬁbre µ = 0,
– Dµ = {¯x2 + ¯y2 + ρ2 = 1, ρ ≥ 0}.

On ˆF¯µ = {ρ = 0}, (2.22) is just the common blow-up of the nilpotent point:
{ x = r¯x
y = r2 ¯y (2.23)

9

P
 PP 1
 P 3
 2

F
 D

4

Figure 5: The stratiﬁed set {rρ = 0} in the blow-up

P P34

P1 P2

Figure 6: Common blow-up of the nilpotent singularity

and by the blow-up (2.23), we get a vector ﬁeld with four singular points Pi (i =
1, 2, 3, 4). P1 and P2 are nodes, P3 and P4 are hyperbolic saddles (Fig. 6).
The four points Pi on the circle x2 + y2 = 1, r = ρ = 0 are studied in the charts
x = ±1, while the upper part of the sphere r = 0, ρ > 0 is studied in the chart ρ = 1.
In [15] we ﬁnd the list of the phase portraits of (2.21) on this half sphere for the
diﬀerent values of µi. Together with the regular part of the graphics this gives us the list
of limit periodic sets for which ﬁnite cyclicity must be proved. These appear in Table. 2.

graphic Epp1 graphic Epp2 graphic Epp3

Table 2: Limit periodic sets of pp-type for the graphic with an elliptic point

10

2.8 Dulac maps near P1 and P2

To prove the ﬁnite cyclicity results in [15] we have proved results about the two diﬀerent
types of Dulac maps near the points P1 (resp. P2) and P3 (resp. P4). For the purpose
of proving the ﬁnite cyclicity of pp-graphics, we only need the ﬁrst type of Dulac maps
near P1 and P2.
Although after blow-up we deal with a 3-dimensional vector ﬁeld, because of the
invariant foliation, we can consider the Dulac maps to be 1-dimensional maps. The
ﬁrst type is similar to the passage near a saddle-node while the second is similar to the
passage near a hyperbolic saddle.
The eigenvalues at P1 and P2 appear in Tab. 2.8. Due to the special form of the
family, the vector ﬁelds at each point P1 and P2 are linear in r and ρ after dividing by
a C∞ positive function. We study P1. The study near P2 is similar. Let

σ1(a) = 1 − 2a
a .

r ρ y
P1 −a a −(1 − 2a)
P2 a −a (1 − 2a)

Table 3: The eigenvalues at P1 and P2

Near P1, the system is of the form

X(a,¯µ)
 



 ˙r = −r
˙ρ = ρ
˙¯y = −σ1(a)¯y + f(a,¯µ)(r, ρ, ¯y) (2.24)

where

f(a,¯µ)(r, ρ, ¯y)

= σ1(a)¯y + −(1−2a)¯y+2¯y2+¯y[ε2r+¯µ3ρ+2¯µ2ρ2−r2h1(r,rρ,¯µ)]+¯µ1ρ3+r¯h2(r,rρ,¯µ)+¯y2Q2(r,ρ,¯y,¯µ)
a+¯y+¯µ2ρ2 (2.25)
and the parameters (a, µ) ∈ P × S2.

Proposition 2.12. Consider the family X(a,¯µ) in the form of (2.24) with parameters
(a, ¯µ) ∈ P × S2. Then ∀(a0, ¯µ) ∈ P × S2 and ∀k ∈ N, there exists P0 ⊂ P, a neighborhood
of a0, N (k) ∈ N and a Ck−transformation

Ψ(a,¯µ) : (r, ρ, ¯y) −→ (r, ρ, ψ(a,¯µ)(r, ρ, ¯y))

where ψ(a,¯µ)(r, ρ, ¯y) = ¯y + o(|(r, ρ, ¯y)|) (2.26)

such that ∀(a, ¯µ) ∈ P0 × S2, the map ψ(a,¯µ) transforms X(a,¯µ) into one of the following
normal forms:

• If σ1(a0) /∈ Q
 ̃X(a,¯µ)
 



 ˙r = −r
˙ρ = +ρ
˙y = −¯σ1(a, ¯µ, ν)y. (2.27)

11

• If σ1(a0) = p
q ∈ Q

̃X(a,¯µ)
 



 ˙r = −r
˙ρ = ρ

˙y = 1
q
 [ − p +
 N (k)∑

i=0 αi+1(a, ¯µ, ν)(ρ
pyq)i]
y (2.28)

where ν = rρ > 0 and
 ¯σ1(a, ¯µ, ν) = σ1(a) − α0(a, ¯µ, ν)

α0(a, ¯µ, ν) =
 N (k)∑

i=1 γiνi

α1(a, ¯µ, ν) = p − ¯σ1(a, ¯µ, ν)q
 (2.29)

where γi(a, ¯µ), αi and κ are smooth functions deﬁned for (a, ¯µ) ∈ P0 × S2.

Proof. The proof [15] is a straightforward application of normal form theory.

D
 r

O

y

r
 y)
 (d, D) P

S
(n,
 Figure 7: The ﬁrst type Dulac map

We consider the ﬁrst type Dulac map (Fig. 2.8):

∆(a,¯µ) = (d, D) : Σ −→ Π

where Σ = {r = r0} and Π = {ρ = ρ0} are sections in the normal form coordinates, r0
and ρ0 are positive constants.
To simplify the notation, for all the maps and vector ﬁelds, we will drop the index
(a, ¯µ). For example, the Dulac map ∆(ν, ˜y1) means ∆(a,¯µ)(ν, ˜y1).
If we parameterize the sections Σ and Π by (ν, y) with the obvious relation ρ = ν
r0
on Σ and r = ν
ρ0 on Π, then we have

Theorem 2.13. For any a0 ∈ P and ¯µ ∈ S2, consider the family ̃X = ̃X(a,¯µ) with
eigenvalues −1, 1, σ1(a0) in normal form (2.27) or (2.28). Then ∀Y0 ∈ R, there exist

12

P0 ⊂ P, a neighborhood of a0, and ν1 > 0 such that ∀ν ∈ (0, ν1) and (a, ¯µ, y) ∈ P0 ×
S2 × [0, Y0], the Dulac map ∆(ν, y) = (d(ν, y), D(ν, y)) has the form




 d(ν, y) = ν

D(ν, y) = ( ν
ν0
 )¯σ1[
y + φ(ν, ω( ν
ν0 , −α1), y)
] (2.30)

where ν0 = r0ρ0 > 0 a constant and

If σ1(a0) /∈ Q, φ = 0;
If σ1(a0) = p
q ∈ Q, p, q ∈ N and (p, q) = 1, then φ(ν, ω( ν
ν0 , −α1), y) is C∞ and
φ = O(ν ¯pωq+1( ν
ν0 , −α1) ln ν
ν0 )
∂φ
∂y = O(ν ¯pωq( ν
ν0 , −α1) ln ν
ν0 )

∂j φ
∂yj = O(
ν ¯p(1+[ j−2
q ])ωq−j+1+q[ j−2
q ]( ν
ν0 , −α1) ln ν
ν0
 ) , j ≥ 2
 (2.31)
where
 ¯p = { q¯σ1(a, ν) α1 ≥ 0
p α1 < 0. (2.32)

Also all the partial derivatives with respect to the parameters (a, ¯µ) are of order

O(ν ¯pωq( ν
ν0 , −α1) ln ν
ν0
 )
.

Remark 2.14.

1. As the ﬁrst component of ∆ is the identity we only write the second component.
We will do the same with the other transition maps.

2. Theorem 2.13 gives the inverse of the Dulac map Π2 −→ Σ2 near P2.

3. Essentially Theorem 2.13 ensures that the Dulac map behaves under derivation
and composition with Ck maps as in the simple case where a(0) /∈ Q. Whenever
there is no additional diﬃculty in the case a(0) ∈ Q compared to the case a(0) /∈ Q
and the ideas are very similar to [15] we will present the proof in the simple case
a(0) /∈ Q, so as to enlighten the ideas.

Remark 2.15. In this paper, all the graphics through a nilpotent point are studied inside
the global blown-up families with several parameters:

• case of a nilpotent point in the ﬁnite plane a ∈ P, ¯µ = (¯µ1, ¯µ2, ¯µ3) ∈ V ⊂ S2, ν > 0;

• case of a nilpotent point at inﬁnity A ∈ P, ¯µ = (¯µ1, ¯µ2) ∈ V ⊂ S1, ν > 0.

We will simply denote all the parameters described above which relate to a graphic by
λ. When we study the cyclicity of a graphic, we take a section Σ (sections Σ1 and
Σ2) in the normal form coordinates in a neighborhood of a singular point, and we study
the number of small zeros of the displacement map for the parameter λ in some subset
(cone) of P × S2 × [0, ν) for ν > 0 suﬃciently small.

Consider the transition map Tλ along the passage from P1 to P2 (in fact its second
component). Let Vi be the subset of parameters in which the pp-graphics Eppi exists
(i = 1, 2, 3). By Prop. 6.2 in [15], there exists ν0 > 0 such that for any k ∈ N, if λ ∈ V3
(resp. λ ∈ V2) all the derivatives of Tλ (resp. T −1
λ ) are suﬃciently small. For λ ∈ V1,
Tλ(˜y1) is Ck, and the transition has a “funnelling eﬀect”, i.e. Tλ is almost aﬃne.

13

P  P
S 1 S 2
T

1 2
l

Figure 8: The transition map along the pp-passage:“funnelling eﬀect”.

Theorem 2.16. [15] There exists ε0 > 0 such that for any k ∈ N, a0 ∈ (0, 1
2 ), there
exist A0 ⊂ (0, 1
2 ), a neighborhood of a0 such that for ∀(a, ¯µ) ∈ A0 × V3, T ′
λ is suﬃciently
small; while for (a, ¯µ) ∈ A × V2, (Tλ−1)′ is suﬃciently small. For any (a, ¯µ) ∈ A0 × V1
and ν > 0 suﬃciently small, Tλ is Ck, and

Tλ(˜y1) =
 k∑

i=0 γ12i(λ)˜yi
1 + O(yk+1) (2.33)

where

γ120 = m120(ν)( ν
ν0 )−¯σ1 + κ1rp
0(1 − m121(ν))ω( ν
ν0 , α1) + O(
( ν
ν0 )¯σ1ω2( ν
ν0 , −α0)
)

γ121 = m121(ν) + O(
( ν
ν0 )¯pωq( ν
ν0 , −α0) ln ν
ν0
 )

γ12i = O(ν ¯p(1+[ i−2
q ])ωq+1−i−q[ i−2
q ])( ν
ν0 , −α0) ln ν
ν0
 )
, i ≥ 2

where m120(0) = 0 and m121(0) = exp( π ¯µ3√a¯µ2 ).

3 The ﬁnite cyclicity of the pp-graphics

In the proof of the ﬁnite cyclicity, we will always use * to denote a positive constant.

3.1 Finite cyclicity of the codimension 3 graphic with an
elliptic nilpotent point with pp-transition together with a
hyperbolic saddle

Note that this graphic should ﬁgure in the zoo of Kotova-Stanzo in the generic case
where the singular point has hyperbolicity ratio ̸= 1 [11].

Theorem 3.1. Consider a graphic with pp-transition through a nilpotent elliptic point
of multiplicity 3 for which a ̸= 1
2 in (2.13) and a hyperbolic saddle. If the hyperbolic
saddle has hyperbolicity ratio σ ̸= 1, then the graphic has ﬁnite cyclicity at most 2.

Proof. As shown in Tab. 2, to prove the graphic has ﬁnite cyclicity, we have to prove
that all the limit periodic sets Epp1, Epp2 and Epp3 have ﬁnite cyclicity. We limit
ourself to the case σ > 1.
 14

D

T
 S S

SS 1 2
 3

4

1 T2

l

Figure 9: Graphic through a nilpotent elliptic point and a hyperbolic saddle

Let Tλ : Σ1 −→ Σ2 be the transition map in the neighborhood of the nilpotent point
as deﬁned in Theorem 2.16. Let Vi be the subset of parameters in which the pp-graphics
Eppi exists (i = 1, 2, 3).
In the neighborhood of the hyperbolic saddle, take sections Σ3 and Σ4 using the
normal form coordinates. By Prop. 2.5, the Dulac map D : Σ3 −→ Σ4 has the form

D(x, λ) = x
σ(λ)(1 + φ(x, λ)) (3.1)

where φ(x, λ) ∈ (I ∞
0 ).
For the graphics Epp1 and Epp3, consider the displacement map deﬁned from Σ3 to
Σ2: L : Σ3 −→ Σ2
L = Tλ ◦ T1 ◦ D − T −1
2 (3.2)

where T1 : Σ4 −→ Σ1 and T2 : Σ2 −→ Σ3 are the regular transition maps using normal
form coordinates on each section. By the chain rule,

L′ = σT ′
λT ′
1x
σ−1(1 + φ(x, λ)) − (T −1
2 )
′.

The second term is bounded away from 0 while the ﬁrst term is small which gives the
ﬁnite cyclicity of the graphic is at most 1.
For the graphic Epp2, we consider the displacement map deﬁned from Σ3 to Σ1:

L : Σ3 −→ Σ1
L = T1 ◦ D − T −1
λ ◦ T −1
2 . (3.3)

Then a straightforward calculation gives that

L(x, λ) = ˜m10(λ) + ˜m1(λ)xσ(λ)[1 + ˜φ(x, λ)] − [ ˜m20(λ) + ˜m2(λ)x(1 + O(x))] (3.4)

where ˜m1(λ0) ˜m2(λ0) ̸= 0, φ ∈ (I ∞
0 ) and ˜m2(λ0) is very small.

15

The ﬁrst derivative of L(x, λ) gives

L′(x, λ) = σ(λ) ˜m1(λ)x
σ(λ)−1 (
1 + ˜φ1(x, λ)
) − ˜m2(λ)[1 + O(x)] (3.5)

where ˜φ1(x, λ) ∈ (I ∞
0 ). Let L1(x, λ) = L′(x,λ)
1+O(x) . Then by (3.5), L′(x, λ) = 0 is equivalent
to L1(x, λ) = 0. Since

L
′
1(x, λ) = ˜m1(λ)σ(λ)(σ(λ) − 1)x
σ(λ)−2(
1 + ˜φ2(x, λ)
) ̸= 0

where ˜φ2(x, λ) ∈ (I ∞
0 ), so L(x, λ) = 0 has at most 2 small positive roots which gives
that the graphic has cyclicity at most 2. (A standard checking ensures that the case
σ(λ) = 2 causes no problem.)

Corollary 3.2. The graphics (I 2
23), (I 2
24) and (I 2
25) have cyclicity ≤ 2.

Proof. This follows immediately from Theorem 3.1 since the graphics occur in family
(2.17) with A ̸= 1
2 and the additional hyperbolic saddle at inﬁnity has hyperbolicity
ratio σ = A
1−A ̸= 1 or 1
σ .

3.2 Finite cyclicity of the hemicycles (H 1
6 ) and (H 3
9 )

In order to prove the ﬁnite cyclicity of the hemicycles (H 1
6 ) and (H 3
9 ), we will need to
prove that some regular transition in these hemicycles has a nonzero second derivative.
This is the purpose of the following lemma.
 PS
 P r

r rlP
 R

Dl

P l
 lS
 D rR R

3
 21 .

Figure 10: Transition maps related to the quadratic system (2.14)

Lemma 3.3. Consider the quadratic system (2.14) with a ∈ (0, 1
2 ), Fig. 10. The graphic
(H 1
6 ) occurs for c2 − 4(1 − a) < 0. We work under this hypothesis.

1. Take sections Σl = {x = −X0}, Σ1 = {x = −x0}, Σ2 = {x = x0} and Σr =
{x = X0}, where 0 < x0 < X0 constants. Let R1 : Σl −→ Σ1 = {x = −x0} and
R2 : Σ2 −→ Σr be the two regular transformations along the invariant line y = 0.
Then R1(y) = ( x0
X0 )1/a,
R2(y) = ( X0
x0 )1/a. (3.6)

16

2. Let (v, w) = ( x
y , 1
y ). Then system (2.14) at inﬁnity becomes

{ ˙v = (a − 1)v2 + cv − 1 + w
˙w = −vw. (3.7)

Let u0 > 0 small, Πl = {v = − 1
u0 } and Πr = {v = 1
u0 }. Then the transformation
map R3 : Πr −→ Πl

is C∞ and if we write

R3(w) = β001(u0)w + β002(u0)w2 + O(w3). (3.8)

then

β001(u0) = exp(−c2π) + O(u0),

β002(u0) = − exp(−3c2π)[exp(c2π) − 1]
(2k1 − 2)(1 − a)2 u
2(k2−k1+1)
0 [1 + O(u0)] (3.9)

where k1 = 3 − 4a
2(1 − a) ∈ (1, 3
2 )

k2 = 1
2(1 − a) ∈ ( 1
2 , 1)

2(k2 − k1 + 1) = 2a
1 − a ∈ (0, 2)

c1 = √
4(1 − a) − c2

c2 = c

(1 − a)
√4(1 − a) − c2 .
 (3.10)

Proof. The proof for the ﬁrst part is straightforward. We now prove the second part.
Note that for system (3.7), the w−axis is invariant, also with 0 < c < 2√
1 − a, there
holds ˙v |w=0= (a − 1)v2 + cv − 1 < 0. Hence R3 is a C∞ map which can be written as
(3.8). By Prop. 2.7, a straightforward calculation gives

β001 = exp (∫ − 1
u0

1
u0
 vdv
(1 − a)v2 − cv + 1
 )

= exp (
−c2[ arctan 2(1−a)−cu0
c1u0 − arctan −2(1−a)−cu0
c1u0
 ]) [ (1−a)+cu0+u2
0
(1−a)−cu0+u2
0
 ]k2

= exp(−c2π) + O(u0)
 (3.11)

and

β002(u0) = −β001(u0)∫ 1
u0

− 1
u0
 2v exp (∫ v

1
u0
 vdv
(1 − a)v2 − cv + 1
 )

((1 − a)v2 − cv + 1)2 dv

= − 2u
2k2
0 [1+O(u0)] exp(− 3c2π
2 )
(1−a)k2
 ∫ 1
u0

− 1
u0
 2v exp (
c2 arctan( 2(1−a)v−c
c1
 )

((1 − a)v2 − cv + 1)k1 dv
 (3.12)

where k1, k2, c1 and c2 are given by (3.10).

17

Note that

lim
u0→0
 ∫ 1
u0

− 1
u0
 2v exp (c2 arctan( 2(1−a)v−c
c1 )
)

((1 − a)v2 − cv + 1)k1 dv

1
u2k1−2
0
 = exp( 1
2 c2π) − exp(− 1
2 c2π)
(2k1 − 2)(1 − a)k1 .

Therefore by (3.12), we have (3.9).

Theorem 3.4. The hemicycle (H 1
6 ) has ﬁnite cyclicity.

Proof. The hemicycle (H 1
6 ) occurs in (2.14) with 0 < c < 2
√
1 − a. After the blow-up
of the family, take sections Σ1 and Σ2 in the normal form coordinates at the entrance
and exit parabolic sectors in the neighborhood of P1 and P2 respectively (Fig. 11). To
prove that (H 1
6 ) has ﬁnite cyclicity, we ﬁrst study the transition map

R : Σ2 −→ Σ1 (3.13)

along the equator. We are going to prove in detail that the second component R2(λ0, ˜y2)
is nonlinear in ˜y2.

S S S S
 P

l

P l
 r
 r

2
Pl Pr

R

1
 Figure 11: The hemicycle (H 1
6 )

(1). Normal forms and Dulac maps at inﬁnity
As shown in Fig. 11, let Pr be the saddle point at inﬁnity in the direction of the
positive x−axis. Using coordinates (zr, ur) = ( 1
x , y
x ), we have

{ ˙ur = ur(1 − a − cur + u
2
r − urzr)
˙zr = −zr(a + cur − u
2
r + urzr) (3.14)

Hence Pr is a hyperbolic saddle of hyperbolicity ratio σr = a
1−a . For a ∈ (0, 1
2 ), we
have 0 < σr < 1. Dividing system (3.14) by 1 − a − cur + u2
r − urzr (positive in the
neighborhood of Pr), a normalizing change of coordinates can be taken of the form
(ur, zr) = (ur, Ψr(ur, Zr) where

Ψr(ur, Zr) = dr1(ur)Zr + dr2(ur)Z2
r + urO(Z3
r )
= [1 + O(ur)]Zr + O(ur)O(Z2
r ). (3.15)

18

Take two sections Σr = {Zr = Z0} and Πr = {ur = u0} in the normal form
coordinates. By [12], for the Dulac map Dr : Σr −→ Πr, we have

Dr(ur) = u
σr
r (Ar + ψr(ur)) (3.16)

where Ar > 0 constant, also ψr ∈ (I ∞
0 ).
To study Pl, the singular point at inﬁnity in the direction of the negative x-axis,
we use coordinates (zl, ul) = (− 1
x , − y
x ). The study is obtained from that of Pr by
(ur, zr) ↦→ (−ul, −zl), yielding a normalizing change of coordinates of the form

(ul, Zl) = (ul, Ψl(ul, zl)) = dl1(ul)zl + dl2(ul)z2
l + ulO(z3
l ).

Taking two sections Πl = {ul = u0}, Σl = {Zl = Z0} in the normal form coordinates,
the Dulac map Dl : Πl −→ Σl can be written as

Dl(Zl) = Zσl
l (Al + ψl(Zl)) (3.17)

where σl = 1
σr > 1, Al > 0 constant, also ψl ∈ (I ∞
0 ).

(2). Decomposition of the map R
The transition map R deﬁned in (3.13) can be calculated by the decomposition

R = R1 ◦ Dl ◦ R0 ◦ Dr ◦ R2 (3.18)

where R1 and R2 are the regular transition maps in the ﬁrst part of Lemma 3.3 and R0
is the map R3 in the second part of Lemma 3.3 seen in diﬀerent coordinates allowing the
compositions. Then a straightforward calculation from (3.16), (3.17) and (3.18) gives

R(˜y) = β1 ˜y + β2 ˜y1+σr + o(˜y1+σr ) (3.19)

where β1 = R′
1(0)R′
2(0)(ArR′
o(0)) 1
σr Al > 0

β2 = 1
2σr R′
1(0)(R′
2(0))
σr+1(R′
0(0)) 1
σr −1R′′
0(0)AlA
1+ 1
σr
r . (3.20)

(3). Calculation of R′′
0(0) to show R(˜y) is nonlinear
It follows from (3.19) and (3.20) that to show R(˜y) is nonlinear, it suﬃce to prove
R′′
0(0) ̸= 0.
To do this, we introduce the coordinates (v, w) = ( x
y , 1
y ) and make the following
decomposition R0 := ¯Ψl ◦ Φ2 ◦ R3 ◦ Φr ◦ ¯Ψr (3.21)

where we denote ¯Ψr(Zr) = Ψr(u0, Zr) and similarly ¯Ψl(zl) = Ψl(u0, zl), and

Φr : { v = 1
ur
w = zr
ur , Φl : { ul = − 1
v
zl = − w
v (3.22)

are the coordinate changes between the charts.
It follows from (3.21),(3.22) and (3.8) that

R0(Zr) = β01Zr + β02Z2
r + O(Z3
r )

19

where

β01(u0) = dr1(u0)dl1(u0)β001
= e−c2π + O(u0),

β02(u0) = β001dl1(u0)dr2(u0) + dl2(u0)d
2
r1(u0)β2
001 + 1
u0 d
2
r1(u0)dl1(u0)β002

= O(u0) + O(u0) − 1
u0
 exp(−3c2π)[exp(c2π) − 1]
(2k1 − 2)(1 − a)2 u
2(k2−k1+1)
0 [1 + O(u0)]

= − exp(−3c2π)[exp(c2π) − 1]
(2k1 − 2)(1 − a)2 u
2(k2−k1)+1
0 [1 + O(u0)] + O(u0).

Since 2(k2 − k1) + 1 = 3a − 1
1 − a ∈ (−1, 1),

so β02 ̸= 0. i.e., R has the form in (3.19) with β2 ̸= 0.

(4). Cyclicity of (H 1
6 )
Note that all steps of the proof of Theorem 2.1 work with this form of the transition
in (3.19), yielding Cycl(H 1
6 ) ≤ 2.

Theorem 3.5. The hemicycle (H 3
9 ) has ﬁnite cyclicity.

Proof. For the hemicycle (H 3
9 ), we have to prove that all the three limit periodic sets
have ﬁnite cyclicity. The proof is similar to that of the (H 1
6 ) in the above theorem.

T D

S S

S S

S S
4 3

2

2

1
 1

1 2

Tl T3T4

1D
 Figure 12: The hemicycle (H 3
9 )

As shown in Fig. 12, take sections in the normal form coordinates in the neighborhood
of the two hyperbolic saddles at inﬁnity respectively.
We consider the transition map

L : Σ1 −→ Σ1
L = D1 ◦ T4 ◦ Tλ − T −1
1 ◦ D−1
2 ◦ T −1
3

where Tλ is the pp-transition through the nilpotent elliptic point, and as show in Fig. 12,
the connections in Tλ, T3 and T4 are ﬁxed while the connection T1 can be broken. Note
that σ(0) = 1−A
A < 1 where σ(0) is the hyperbolicity ratio of the left hyperbolic saddle
point at inﬁnity. A straightforward calculation gives that

L(˜y, λ) = ˜yσ(λ) [ ¯m1(λ) + ¯m2(λ)˜y + O(˜y2)
]

− [
m0(λ) + m1(λ)˜yσ(λ) + m2(λ)˜y2σ(λ) + o(˜y2σ(λ))
] (3.23)

20

where m2(λ) = ∗ ∂2T −1
1
∂y2 and m1(λ) is bounded and bounded away from zero.
Diﬀerentiating of L(˜y, λ) with respect to ˜y yields

L′(˜y, λ) = ˜yσ(λ)−1 [σ(λ) ¯m1(λ) + (1 + σ(λ)) ¯m2(λ)˜y + O(˜y2)
]

−˜yσ(λ)−1 [
σ(λ)m1(λ) + 2σ(λ)m2(λ)˜yσ(λ) + o(˜yσ(λ))
] (3.24)

For Epp2, ¯m1(λ) is very large, hence L′(˜y, λ) > 0 for ˜y > 0 small and λ small. For
Epp3, ¯m1(λ) is very small, hence L′(˜y, λ) < 0 for ˜y > 0 small and λ small. Therefore
Epp2 and Epp3 have cyclicity at most 1.
We now consider the case of Epp1. Let

L1(˜y, λ) = ˜y1−σ(λ)L
′(˜y, λ).

Then the number of small roots of L(˜y, λ) = 0 is at most 1 plus the number of roots of
L1(˜y, λ) = 0. Since 0 < σ(λ) < 1, so

L′
1(˜y, λ) = −2σ(λ)m2(λ)˜yσ(λ)−1 (
1 + o(˜yσ(λ))
) + (1 + σ(λ)) ¯m2(λ) + O(˜y) ̸= 0

which gives that the number of small positive roots of L(˜y, λ) = 0 is at most 2, i.e.
Cycl(H 3
9 ) ≤ 2, if we show that m2(λ0) ̸= 0.
Let us now show that m2(0) ̸= 0. The graphic occurs inside the family (2.17) with
γ = 0. By Theorem 2.11, the invariant line y = −1 is part of the hemicycle. The
transition map T1 : Σ2 −→ Σ1 along the invariant line then can be decomposed as

T1 = Φ1 ◦ T0 ◦ Φ
−1
2 (U, λ) (3.25)

where Φ1 and Φ2 are the normalizing coordinates changes on the sections Σ1 and Σ2
respectively and U is the normalizing coordinate (see below). Let the sections Σi (i =
1, 2) be given by z = z0 with z0 > 0 small, then

T0 : {x = − 1
z0 } −→ {x = 1
z0 }

is the regular transition map along the invariant line y = −1 for the system (2.17) with
δ2 − 4A < 0.
Note that for system (2.17), if we move the invariant line ˆy = −1 to y = 0 by making
the transformation x = −ˆx, y = ˆy − 1,

then system (2.17) becomes { ˙ˆx = −δ ˆx + ˆy − 1 − Aˆx2
˙ˆy = −ˆxˆy. (3.26)

System (3.26) is exactly the system (3.7) if we take A = 1 − a and δ = −c. Hence the
calculation of the transition map along the invariant line ˆy = 0 can be done as before.
We need also consider the normalizing changes of coordinates. For that purpose we
transform (3.26) by means of (u, z) = ( y
x , 1
x ). This yields the system

{ ˙u = (A − 1)u + δuz − u2z − uz2

˙z = Az + δz2 + z3 − uz2. (3.27)

21

In order to bring to normalizing coordinates we divide the system by A + δz + z2 − uz2.
Hence normalizing coordinates can be taken as

(U, Z) = (
1 + O(z)u + O(z)O(u
2), z)
.

As in part (3) in Theorem 3.4, we can conclude that m = m2(λ0) ̸= 0.

3.3 Finite cyclicity of a graphic with a nilpotent elliptic
point, a saddle and a saddle-node

Theorem 3.6. A graphic with a pp-transition through a nilpotent elliptic point together
with an attracting saddle node and a repelling hyperbolic saddle (with hyperbolicity ratio
σ < 1) has ﬁnite cyclicity ≤ 2 provided that the saddle is located on the side of the
parabolic sector of the saddle-node (Fig. 13).

S1
 P
 S
 P

2

1
 2

P 3 3S

Figure 13: Graphic with a pp-transition, hyperbolic saddle and a saddle node

Proof. We take two sections Σ1 and Π1 located at the entrance and the exit of the
saddle and other sections as in Fig. 13. Let

R1 : Π1 −→ Σ2
R2 : Π2 −→ Σ3
R5 : Π3 −→ Σ1

be the regular transition maps. The map from Σ3 −→ Π3 has the form (for a
irrational) ν−σ1R4,λ(M (λ)R3,λ(νσ1 ˆy))

where M (λ) is 1 (resp. large, small) for Epp1 (resp. Epp2, Epp3) and R3,λ, R4,λ are
regular transitions, hence diﬀeomorphisms such that R′
3,λ and R′
4,λ are bounded and
bounded away from 0.
We consider the displacement map

Vλ : Π1 → Σ1.

22

Here again we write the proof for a irrational which implies σ(0) irrational but we
explain what is the non trivial adaptation for the case σ(0) = 1
2 . The displacement map
has the form

Vλ(y) = R5,λ
(
ν−σ1R4,λ
(
M (λ)R3,λ(
νσ1R2,λ(m(λ)R1,λ(y))
)
)) − y
 1
σ(λ) (3.28)

where the Ri,λ are regular transitions satisfying R′
i,λ(y) ̸= 0 and m(λ) → 0 as λ → 0.
Then V ′
λ(y) = m(λ)M (λ)R′
1,λR′
2,λR′
3,λR′
4,λR′
5,λ − 1
σ(λ) y
 1
σ(λ) −1. (3.29)

We divide a neighborhood of 0 in parameter space in two cones. In the ﬁrst cone
where M (λ)m(λ) > 1
2 , then V ′
λ(y) > 0 for small y yielding cyclicity ≤ 1. Note that this
cone contains the values of parameter λ corresponding to Epp1 and Epp3.
In the second cone where M (λ)m(λ) < 1 then zeros of V ′
λ(y) are zeros of

Wλ(y) = σ(λ)M (λ)m(λ) − y
 1
σ(λ) −1

R′
1,λR′
2,λR′
3,λR′
4,λR′
5,λ . (3.30)

Then for σ(0) ̸= 1
2

W ′
λ(x) = −
[ 1
σ(λ) − 1]
x
 1
σ(λ) −2 [ ˆM (λ) + O(M (λ)m(λ))O(x) + O(m(λ))O(x)
] (3.31)

where ˆM (λ) ̸= 0. Then W ′
λ(x) is nonzero for small nonzero y.
In the particular case σ(0) = 1
2 , we apply the same argument but we replace the
function Wλ(y) by the function

¯Wλ(y) = [σ(λ)M (λ)m(λ)] 1
2 −
 [ x
 1
σ(λ) −1

R′
1,λR′
2,λR′
3,λR′
4,λR′
5,λ
 ] 1
2 . (3.32)

Corollary 3.7. The graphic (I 2
39) has ﬁnite cyclicity.

Proof. The graphic (I 2
39) occurs inside the family (2.17) with 1
2 < A < 1 and the
hyperbolicity ratio is 1−A
A < 1. The ﬁnite cyclicity of (I 2
39) follows from Theorem 3.6.

3.4 Finite cyclicity of a graphic with a nilpotent elliptic
point and a saddle-node

Theorem 3.8. A graphic with a nilpotent elliptic point of multiplicity 3, a pp-transition,
and a saddle-node with central transition has ﬁnite cyclicity if the regular transition from
the nilpotent point to the node sector of the saddle-node is nonlinear.

Proof. The graphics Epp1 and Epp3 have cyclicity 1 as the ﬁrst return map P satisﬁes
P ′(0) < 1. We now consider the case of Epp2. As shown in Fig. 14, we take sections Σi

23

P 2
 1P

2S
 1R
R2
 S1

Figure 14: Graphic through a nilpotent elliptic point and a saddle-node

and Πi (i = 1, 2) in normal form coordinates in the neighborhood of the elliptic point
and the saddle-node respectively. Let

R1 : Π1 −→ Σ2
R2 : Π2 −→ Σ1

be the regular transition maps. By assumption there exists N such that the transition
map R1 can be written as

R1(y, λ) =
 N∑

i=0 mi(ν, λ)yi + O(yN +1) (3.33)

where mN (0, λ) ̸= 0.
We will consider the displacement map V : Π1 −→ Σ2. As in the proof of Theo-
rem 3.6, the transition map through the blown-up sphere has the form

R0(ˆy, λ) = ν−σ1R4,λ(
M (λ)R3,λ(νσ1 ˆy)
)
. (3.34)

where M (λ) is large. It follows from Proposition 2.6 that the central transition map
through the saddle-node has the form (2.8) with the constant m(λ) small.
The displacement map V now reads

V (y, λ) = R1(y, λ) − m−1(λ)R−1
2 ◦ R−1
0 (y, λ)

= R1(y, λ) − m−1(λ)R−1
2
 (
ν−σ1R−1
3,λ(
M (λ)−1R−1
4,λ(νσ1y)
)
)
. (3.35)

Then

V ′(y, λ) = R′
1(y, λ) − m−1(λ)R−1
2 ′(
R−1
0 (y, λ)
)
R−1
0 ′(y, λ)

= R′
1(y, λ) − m−1(λ)M (λ)−1R−1
2 ′(
R−1
0 (y, λ)
)
(R−1
4,λ)′(R−1
3,λ)′. (3.36)

Let
 W (y, λ) = R′
1(y, λ)

R−1
2 ′(
R−1
0 (y, λ)
)
(R−1
4,λ)′(R−1
3,λ)′ − m−1(λ)M −1(λ). (3.37)

24

It follows from Theorem 2.16, (3.33) and (3.34) that W (N −1)(y, λ) ̸= 0 as all the higher
order derivatives of R0 and R2 are small for small y because of the funnelling eﬀect.
This gives that the cyclicity of the graphic is at most N .

Since we will have to deal with family of graphics of the same type, we state the
following important principle which will be used to deal with all the families of graphics.

Theorem 3.9. Analytic extension principle to prove a regular transition map
is nonlinear:
The transition map must be calculated in normalizing coordinates on sections parallel to
the axes.

1. For the points Pi we deal with 3-dimensional hyperbolic saddles with two eigen-
values of the same sign and for which the planes r = 0 and ρ = 0 are invariant.
Using Poincar´e theorem stating that it is possible to bring a node to normal form
via an analytic change of coordinates it is possible to choose normalizing coordi-
nates which are analytic in the coordinate plane where the singular point has a node
behavior. Our section is then analytic and parameterized by an analytic coordinate
inside that plane (details in [15]).

2. Using the sectorial normalizing theorem for a saddle-node it is possible to show that
there exist a normalizing change of coordinates which is analytic in the node sector
for the zero value of the parameters. Then the section parallel to the stable (un-
stable) manifold in the node sector is analytic for the zero value of the parameters
and parameterized by an analytic coordinate (details in [3]).

Then the principle says: if a regular transition appears for a graphic in a family of
graphics and if the two sections on which it is deﬁned are analytic and parameterized
by analytic coordinates, then, if the transition is nonlinear in one point, it is nonlinear
everywhere.
It is usually easy to prove the nonlinearity of the transition near one of the boundary
graphics of the family.

By the above Analytic extension principle and the ﬁnite cyclicity results obtained
above, we immediately have

Corollary 3.10. The graphics (F 1
6a), (I 1
5a), (I 1
7a), (I 1
8a), (I 1
9a) and (I 1
10a) have ﬁnite
cyclicity.

Proof. Since the pp-transition through the nilpotent elliptic point is almost aﬃne, to
prove the ﬁnite cyclicity of these graphics we only need to verify that the corresponding
“external” map is nonlinear.

1. (F 1
6a) and (I 1
5a)
In the proof of Theorem 3.4 we show that the map R along the hemicycle (H 1
6 )
is nonlinear of order 2, therefore by Theorem 3.9, the corresponding transition for
each of the graphic in the family (F 1
6a) is nonlinear too.
The nonlinearity of the corresponding map for (I 1
5a) comes from the proof of The-
orem 3.5 for the hemicycle (H 3
9 ) and the fact that the regular transition map along
the invariant line is nonlinear of order 2.

25

2. (I 1
7a), (I 1
8a), (I 1
9a) and (I 1
10a)
These graphics occur in family (2.17) with A ̸= 1
2 and the additional hyperbolic
saddle at inﬁnity has hyperbolicity ratio σ = A
1−A ̸= 1. Thus the corresponding
maps for the boundary graphics (I 2
23), (I 2
24), (I 2
25) and (I 2
39) are nonlinear respec-
tively.

Remark 3.11. In [3], Dumortier, Ilyashenko and Rousseau proved that the graphic
(I 1
10a) has ﬁnite cyclicity.

3.5 Finite cyclicity of the hemicycles (H 3
7 ) and (H 3
10)

Consider the hemicycle (H 3
7 ). As shown in Fig. 15, take the transversal sections Π2 and
Π0 in the neighborhood of the saddle point at inﬁnity and the attracting saddle-node
on the equator. Let R3,0 : Π2 −→ Π0

be the regular transition map in the normalizing coordinates.

Theorem 3.12. If R′′
3,0(0) ̸= 0, then the hemicycle (H 3
7 ) has ﬁnite cyclicity ≤ 2.

Proof. We write the proof in the case a ∈ P irrational. Then the hyperbolicity ratios of
the two saddle points at inﬁnity on the right (resp. left) are σr = a
1−a (resp σl = 1
σr )
with σr(0) < 1 irrational.
 2

0P

RD
 R
 R D
1 1 2 2

3

D4 0

Sl
S 1 S 2

R
 P

Figure 15: The transition maps of hemicycle (H 3
7 ) in proving its ﬁnite cyclicity

As shown in Fig. 15, let R1,λ (resp. R2,λ) be the regular transitions along the x-axis
on the left (resp. right). We can suppose that the transition R4,λ along the equator
to the left of the saddle-node is the identity (see [9]). Let R3,λ be the transition along
the equator on the right side of the saddle-node. In particular R3,λ(0) = 0. The Dulac
maps D1 and D2 have the form of (2.3) in Proposition 2.5 with ψi = 0. If we denote
the central transition map of the saddle-node by D0 and write it as in (2.8) with the
coeﬃcient m1(λ) → 0, then, the transition Σ2 −→ Σ1 along the equator can be written
as Rλ(y) = D1 ◦ R4,λ ◦ D0 ◦ R3,λ ◦ D2
= [m1(λ)R3,λ((R2,λ(y))σr )
]σl.

26

Let Sλ be the inverse of the transition map Tλ deﬁned in (2.33). Consider the
displacement map Vλ : Σ2 −→ Σ1 given by

Vλ(y) = Rλ(y) − R−1
1 ◦ Sλ ◦ R−1
2,λ(y).

The ﬁrst derivative of Rλ is small for small y and the ﬁrst derivative of Sλ is nonzero
(resp. small, large) for Epp1 (resp. Epp2, Epp3). Hence for limit periodic sets of type
Epp1 or Epp3, the displacement map has a nonzero derivative, yielding cyclicity ≤ 1.
For Epp2, it follows from (2.33) that we can rewrite the map Sλ(y1) (we will apply
this with y1 = R−1
2,λ(y)) as

Sλ(y1) = ν−σ1(
ε0 + m2(λ)νσ1y1
(
1 + O(
|(νσ1, m2(λ))|
)
O(y1)
))
,

with m2(λ) → 0 as λ → 0. Hence

S′
λ(y1) = m2(λ)(
1 + O(|(νσ1, m2(λ))|)O(y1)
) = m2(λ)
(
1 + ψ(y1, λ)
)

where ψ(y1, λ) = O(νσ1m2(λ)). Moreover for y1 = R−1
2,λ(y) we will have

1 + ψ(y1, λ) = 1 + ψ1(y, λ),

where again ψ1(y, λ) = O(νσ1m2(λ)).
Let
 Wλ(y) = V ′
λ(y)

m1(λ)
(
1 + ψ1(y, λ)
)(
R−1
1,λ)′(
R−1
2,λ)′

= R′
λ(y)

m1(λ)(1 + ψ1(y, λ))
(
R−1
1,λ)′(
R−1
2,λ)′ − m2(λ)
m1(λ)

= a0(λ) + a1(λ)yσr(λ) + O(y)
 (3.38)

where a1(λ) = ∗R′′
3,λ(0) is bounded and bounded away from 0 for small z and λ as R′′
3,0
is nonzero (see Lemmas 3.14 and 3.15 below). Hence W ′
λ(y) is large for small y and λ,
yielding that (H 3
7 ) has cyclicity at most 2.

We will postpone the proof that R3,0 after the proof of the ﬁnite cyclicity of (H 3
10).
The diﬀerence between (H 3
7 ) and (H 3
10) is that the transition map along the invariant
line is not ﬁxed in (H 3
10) while the transition along the equator was ﬁxed in (H 3
7 ). As
shown in Fig. 16, let R1,0 : Σ1 −→ ˆΣ1

be the regular transition map from the saddle point to the attracting saddle-node in the
normalizing coordinates. Similar to the case of (H 3
7 ), we will show that it is suﬃcient
to prove that R′′
1,0(0) ̸= 0. This will be proved in Lemma 3.15.

Theorem 3.13. The hemicycle (H 3
10) has ﬁnite cyclicity ≤ 2 if R′′
1,0(0) ̸= 0.

27

1
 lS

S SS1 2
Rl
R1
 Figure 16: The transition maps for the hemicycle (H 3
10)

Proof. Again, we write the proof in the case A ∈ P irrational. As shown in Fig. 16, we
take two sections Σ1 and Σ2 near the hyperbolic saddles at inﬁnity using the normalizing
coordinates. Then we consider the displacement map

Vλ(y) = Rλ(y) − Gλ(y) : Σ1 −→ Σ2 (3.39)

where Rλ is the transition from Σ1 to Σ2 along the invariant line, Gλ is the transition
map along the equator (which is the composition of two regular transitions along the
equator and the transition map Sλ through the nilpotent elliptic point) composed with
the two Dulac maps near the hyperbolic saddles at inﬁnity.
A straightforward calculation gives

Rλ(y) = ϵ0 + m1(λ)[y + M2y2 + O(y3)] (3.40)

where m1(λ) → 0 and M2(0) = ∗R′′
1λ(0).
For the transition map G, note that the transition map Tλ through the nilpotent
elliptic point is almost linear since it also satisﬁes Tλ(0) = 0. So, we can write the
inverse of the transition map T as

Sλ(y1) = m2(λ)y1(
1 + O(|(νσ, m2(λ))|)O(y1)
) = m2(λ)y1(
1 + ψ(y1, λ)
)
,

with m2(λ) nonzero (resp. small, large) for Epp1 (resp. Epp2, Epp3). Therefore, we
can write the transition map Gλ as

Gλ(y) = ˆm2(λ)y(
1 + ˆM2yσr + O(
y1+σr )) (3.41)

where σr = A
1−A > 1 and ˆm2(λ) = ∗m2(λ).
Using the expression of (3.40) and (3.41) in (3.39), we have

V ′
λ(y) = m1(λ)
[1 + 2M2y + O(y2)] − ˆm2(λ)[
1 + σr ˆM2yσr + O(
y1+σr )]
. (3.42)

Hence for the limit periodic sets of type Epp1 and Epp3, V ′
λ(y) ̸= 0 for y and λ small,
yielding cyclicity ≤ 1.
 28

For the limit periodic set of type Epp2, ˆm2(λ) = ∗m2(λ) is small. Let

Wλ(y) = V ′
λ(y)
ˆm2(λ)[1 + 2M2y + O(y2)] = m1(λ)
ˆm2(λ) − 1 + σr ˆM2yσr + O(
y1+σr )

1 + 2M2y + O(y2) .

Then
 Wλ(y) = m1(λ)
ˆm2(λ) − 1 + 2M2y + O(y2) + O(yσr ) (3.43)

where M2 = ∗R′′
1λ(0). Therefore for y and λ suﬃciently small

W ′
λ(y) = 2M2 + O(y) + O(yσr−1).

Hence (H 3
10) has cyclicity at most 2 if M2 = R′′
1λ(0) ̸= 0.

Next we show the the nonlinearity of the two transition maps in the above two
theorems.
It follows from the results in Section 2.6 that the hemicycle (H 3
10) occurs in the
family { ˙x = −y + Ax2 + 2√
A x + 1,
˙y = xy (3.44)

with 1
2 < A < 1, while (H 3
7 ) occurs in the family
{ ˙x = y + ax2 + 2√
1 − a xy − y2,
˙y = xy, (3.45)

with a ∈ (0, 1
2 . If we calculate the regular transition map R3λ for (H 3
7 ) using system
(3.45) by relocating system through x = v
w , y = 1
w , we have system
{ ˙v = w + (a − 1)v2 + √
1 − av − 1,
˙w = vw. (3.46)

A further change v ↦→ −v can bring (3.46) to exactly system (3.44). Hence the calcula-
tion of R3,0 is the same as the calculating for R1,0 using system (3.44), yielding

Lemma 3.14. The condition R′′
3,0(0) ̸= 0 is satisﬁed for (H 3
7 ) if and only if R′′
1,0(0) ̸= 0
for (H 3
10).

Note that system (3.44) has a saddle-node at (− 1√A , 0). To make the calculations
easier, we ﬁrst translate the saddle-node to the origin. Then a rescaling

x ↦→ −A
√
A x, y ↦→ −A
2 y, t ↦→ − 1
√
A t

yields { ˙x = y + x2,
˙y = y(1 + Bx) (3.47)

where B = 1
A ∈ (1, 2).
For system (3.47), we have a hemicycle (Fig. 17). As shown in the ﬁgure, let Σ1 and
Σ2 be two sections parameterized by the normalized coordinates in the neighborhood
of the repelling saddle-node and hyperbolic saddle at inﬁnity respectively. One can see

29 2
1 1S T S2Q Q

Figure 17: The transition map T for system (3.47) in Lemma 3.15

that to show R′′
1,0(0) ̸= 0 for (H 3
10) using system (3.44), it is equivalent to show that the
transition map T : Σ1 −→ Σ2

in the normalizing coordinates satisﬁes T ′′(0) ̸= 0.

Lemma 3.15. The transition map T has a nonzero second derivative, i.e., T ′′(0) ̸= 0.

Proof. Let us call (X, Y ) (resp. (U, Z)) the normalizing coordinates at Q1, the origin
(resp. Q2, the point at inﬁnity). The regular transition map R can be written as a
composition of the following 6 maps:

1) The map T1 from {X = X1} to {x = x0} in the (X, Y ) coordinates, where
(X1, 0) and (x0, 0) represent the same point with (X, Y ) and (x, y) coordinates
respectively. Both sections are parameterized by Y . Hence T ′
1(0) = 1.

2) The map T2 which is the change of coordinates from Y to y on {x = x0}. Then

T2(Y ) = a1Y + a2Y 2 + O(Y 3) (3.48)

where a1 > 0.

3) The map T3(y) which is the transition from {x = x0} (x0 small ) to {x = X0}
(X0 large) in (x, y) coordinates.

4) The map T4 which is the transition from the coordinate y to the coordinate
u = y
X0 on {x = X0}. Then T4 is linear: T4(y) = y
X0 = Z0y with Z0 = 1
X0 (the
section {x = X0} becomes {z = Z0} in the (u, z) = ( y
x , 1
x ) coordinates.

5) The change of coordinate T5 from u to U on {z = Z0}. Then

T5(u) = b1u + b2u
2 + O(u3) (3.49)

where b1 > 0.

6) The map T6 from the image of {z = Z0} in (U, Z) coordinates to {Z = Z1}
where (0, Z0) and (0, Z1) represent the same point written respectively in (u, z)
and (U, Z) coordinates. Then T ′
6(0) = 1.

30

Hence T = T6 ◦ T5 ◦ T4 ◦ T3 ◦ T2 ◦ T1. (3.50)

A straightforward calculation from (3.48), (3.49) and (3.50) gives

T ′(0) =
 6∏

i=1 T ′
i (0) = a1b1
X0 T ′
3(0) (3.51)

and

T ′′(0) = T ′(0) [
T ′′
1 (0) + 2a2
a1 + T ′′
3 (0)
T ′
3(0) a1 + 2a1b2
b1 Z0T ′
3(0) + a1b1Z0T ′
3(0)T ′′
6 (0)
] . (3.52)

Now we calculate all the terms appearing in T ′′(0) in (3.52).

i). Calculation of T ′
3(0) and T ′′
3 (0).
Applying Proposition 2.7 to system (3.47), we have

T ′
3(0) = exp (∫ X0

x0
 1 + Bx
x2 dx
) = ( X0
x0
 )B exp ( 1
x0 − 1
X0
 ) (3.53)

and
 T ′′
3 (0)
T ′
3(0) = 2 ∫ X0

x0
 ( x
x0
 )B exp ( 1
x0 − 1
x
 ) −(1 + Bx)
x4 dx

= −2x
−B
0 e
 1
x0 ∫ X0

x0
 (
Bx
B−3 + x
B−4) e− 1
x dx. (3.54)

ii). Calculations at Q2
The system located at Q2 in (u, z) = ( y
x , 1
x ) coordinates has the form
{ ˙u = (B − 1)u + uz − u2z,
˙z = −z(1 + uz). (3.55)

To bring system (3.55) to normal form, we ﬁrst divided the system by 1 + uz, then
{ ˙u = (B − 1)u + uz − (B − 1)u2z + O(|(u, z)|4)
˙z = −z. (3.56)

So the normalizing change of coordinates have the form

u = U − U Z − B
B − 2 U 2Z + 1
2 U Z2 + O(|(U, Z)|
4), z = Z

yielding
 U = u + uz + B
B − 2 u2z − 1
2 uz2 + O(|(u, z)|
4), Z = z.

So on Z = Z0, the change of coordinate T5 can be written as

T5(u) = [1 + Z0 + O(Z2
0 )]u + [ B
B − 2 Z0 + O(Z2
0 )]u2 + O(u
3).

Then we have
 b1 = 1 + Z0 + O(Z2
0 ), b2 = B
B − 2 Z0 + O(Z2
0 ). (3.57)

31

Hence b2
b1 = B
B − 2 Z0 + O(Z2
0 ). (3.58)

Also T6 = identity.

iii) Normal form at the origin Q1
We diagonalize the normal form by means of x1 = x + y. Then
{ ˙x1 = x2
1 + (2 − B)x1y + (1 − B)y2,
˙y = y + By2 + Bx1y. (3.59)

We divide system (3.59) by 1 + Bx1 + By. One can verify that the normalizing
change of coordinate of the form

X = x1 − (2 − B)x1y − 1 − B
2 y2 + O(|(x1, y)|
3), Y = y (3.60)

transforms system (3.59) into a normal form
{ ˙X = X 2,
˙Y = Y (1 + BX). (3.61)

Hence in the new coordinates, the section x = x0 has the equation

X = h1(Y ) = x0 + Y (−1 + O(x0) + O(Y 2). (3.62)

In particular, h(0) = x0, h′
1(0) = −1.
It follows from (3.61) that we have
∫ h1(Y )

x0
 1 + Bx
x2 dx = ∫ T1(Y )

Y dY.

A straightforward calculation yields

T1(y) = Y − ( B
x0 + 1
x2
0
 )Y 2 + O(Y 3). (3.63)

Hence T ′
1(0) = 1, T ′′
1 (0) = −2( B
x0 + 1
x2
0
 )
. (3.64)

As Y = y we have a1 = 1, a2 = 0. (3.65)

Let us take Z0 = x0 and X0 = 1
x0 and let x0 > 0 suﬃciently small. Note that
1 < B < 2, it follows from substitution of (3.51), (3.53), (3.54), (3.58), (3.64) and (3.65)
into (3.52) and a straightforward calculation gives

T ′′(0) = x
1−2B
0 e
 1
x0 (1 + O(x0)) [−2
( B
x0 + 1
x2
0
 )

−2x−B
0 e
 1
x0 ∫ 1
x0

x0 (BxB−3 + xB−4)e− 1
x dx + 2x
2−2B
0 e
 1
x0 ( B
B − 2 + O(x0)
)]

= x
1−3B
0 e
 2
x0
 [

−2 ∫ 1
x0

x0 (BxB−3 + xB−4)e− 1
x dx + O(x
2−B
0 )
]

< 0. (3.66)
where since 1 < B < 2, we have 0 < 2 − B < 1 and −2 < B − 3 < −1.

32

3.6 Finite cyclicity of (I 2
17a) and (I 2
18a)

Theorem 3.16. The graphics (I 2
17a) and (I 2
18a) have ﬁnite cyclicity.

Proof. Let us consider (I 2
17a) and the sections as deﬁned in Fig. 15.

1 1 R

P
3

RD
 R
 2

D0
 2Sl

1S S

Figure 18: The transition maps for (I 2
17a)

We consider the displacement map V : Σ2 −→ Σ1 given by Vλ(y) = Rλ(y) − Sλ(y)
as in Theorem. 3.12. As before we write the proof in the case a(0) irrational. For the
passage near the saddle-node at inﬁnity we can suppose that the normal form is taken so
that the equator coincides with one coordinate axis. Then we can scale the normalizing
coordinates so that the graphic cuts a section Π transversal to the equator at a height
1 (Fig.18). The transition R2,λ(y) : Σ2 −→ Π can be taken as

R2,λ(y) = 1 + T1,λ(y)

where T1,0(0) = 0 and T ′
1,λ(0) > 0.
We can choose the normalizing coordinates so that R3 is a linear map. Then the
displacement map has the form

Vλ(y) = R1,λ((m1(λ)(1 + T1,λ(y)))
 1
σ(λ) ) − Sλ(y). (3.67)

Let
 ˜y = m1(λ)
(1 + T1,λ(y)
) 1
σ(λ) .

Then
 V ′
λ(y) = R′
1,λ(˜y)m1(λ))
 1
σ(λ) (
1 + T1,λ(y)
) 1
σ(λ) −1T ′
1,λ(y) − S′
λ(y). (3.68)

For limit periodic sets of type Epp1 (resp. Epp3) V ′
λ(y) is nonzero (resp. large) yielding
cyclicity ≤ 1 as σ(λ) < 1.
For limit periodic set of type Epp2 we have S′
λ(y) = ∗m2(λ)(1 + O(νσ1)O(y)), where
* is a nonzero constant. Let

Wλ(y) = V ′
λ(y)

(m1(λ))
 1
σ(λ) (
1 + O(νσ1)O(y)
) . (3.69)

33

Then W ′(y) = R′′
1,λ(˜y)m1(λ)
 1
σ(λ) (
1 + T1,λ(y)
)2( 1
σ(λ) −1)T ′
1,λ2(y)

+ 1−σ(λ)
σ(λ) R′
1,λ(˜y)(1 + T1,λ(y))
 1
σ(λ) −2T ′
1,λ2(y)

+R′
1,λ(˜y)(1 + T1,λ(y))
 1
σ(λ) −1T ′′
1,λ(y)
+O(νσ1).

The ﬁrst and fourth terms are small as well as all their derivatives. Let us look at
the sum of the second and third terms. It is given by a nonzero function multiplied by:

Kλ(y) = 1 − σ(λ)
σ(λ) (T ′
1,λ)
2(y) + (1 + T1,λ(y))T ′′
1,λ(y). (3.70)

For λ = 0 the equation K0(y) ≡ 0 can be integrated by quadratures. It is equivalent

to say that (1 + T1,0(y))
 1
σ(λ) is an aﬃne map. Hence the proposition follows by ﬁnding a
nonzero derivative of W ′(y) as soon as we show that K0(y) has a nonlinear term, which

is equivalent to say that, at a ﬁnite order (1 + T1,0(y))
 1
σ(λ) diﬀers from an aﬃne map.
We can choose analytic coordinates on Σ2 and Π. By the analytic extension principle
it suﬃces to verify the condition for graphics very close to the hemicycle. There the
transition map is the composition of a regular map together with a Dulac map for which
σ < 1 and a regular map with non-vanishing second derivative. This last property is
exactly the needed obstruction which guarantees that (1 + T1,0(0))
 1
σ(0) diﬀers from an
aﬃne map.
Proving that the graphic (I 2
18a) has ﬁnite cyclicity is completely similar.

References

[1] F. Dumortier, M. El. Morsalani and C. Rousseau, Hilbert’s 16th problem
for quadratic systems and cyclicity of elementary graphics. Nonlinearity 9
(1996), no. 5, 1209–1261.

[2] F. Dumortier, A. Guzm´an and C. Rousseau Finite cyclicity of elementary
graphics surrounding a focus or center in quadratic systems, to appear in
Qualitative Theory of Dynamical Systems.

[3] F. Dumortier, Y. Ilyashenko and C. Rousseau, Normal forms near a saddle-
node and applications to ﬁnite cyclicity of graphics, Erg. Th. Dynam. Syst.
22 (2002), 783–818.

[4] F. Dumortier, R. Roussarie and C. Rousseau, Hilbert’s 16th problem for
quadratic vector ﬁelds. J. Diﬀerential Equations 110 (1994), no. 1, 86–133.

[5] F. Dumortier, R. Roussarie and C. Rousseau, Elementary graphics of cyclic-
ity 1 and 2. Nonlinearity 7 (1994), no. 3, 1001–1043.

[6] F. Dumortier, R. Roussarie and S. Sotomayor, Generic 3-parameter fam-
ilies of vector ﬁelds in the plane, unfoldings of saddle, focus and elliptic
singularities with nilpotent linear parts. Springer Lecture Notes in Mathe-
matics 1480 1-164 (1991).

[7] F. Dumortier, R. Roussarie and S. Sotomayor, Bifurcations of Cuspidal
Loops. Nonlinearity 10 (1997), no. 6, 1369–1408.

34

[8] M. El Morsalani, Perturbations of graphics with semi-hyperbolic singulari-
ties, Bull. Sciences Math´ematiques, Vol. 120, (1996), 337–366.

[9] A. Guzm´an and C. Rousseau, Genericity conditions for ﬁnite cyclicity of
elementary graphics. J. Diﬀerential Equations 155 (1999), no. 1, 44–72.

[10] Y. Ilyashenko and S. Yakovenko, Finite-smooth normal forms of local fami-
lies of diﬀeomorphisms and vector ﬁelds. Russian Math. Surveys 46, (1991),
1–43.

[11] A. Kotova and V. Stanzo, On few-parameter generic families of vector ﬁelds
on the two-dimensional sphere. Concerning the Hilbert 16th problem. 155–
201, Amer. Math. Soc. Transl. Ser. 2, 165, Amer. Math. Soc., Providence,
RI, 1995.

[12] A. Mourtada, Cyclicit´e ﬁnie des polycycles hyperboliques de champs de
vecteurs du plan: mise sous forme normale. Bifurcations of planar vec-
tor ﬁelds (Luminy, 1989), 272–314, Lecture Notes in Math., 1455, Springer,
Berlin, 1990.

[13] S. Sternberg, On the structure of local homeomorphisms of euclidean n-
space. II. Amer. J. Math. 80, (1958), 623–631.

[14] F. Takens, Singularities of vector ﬁelds. Publ. Math. de l’IHES 43, 47-100,
1974.

[15] H. Zhu and C. Rousseau Finite cyclicity of graphics with a nilpotent sin-
gularity of saddle or elliptic type, J. Diﬀerential Equations, Vol. 178, No.2,
325-436. (2002)
 35
