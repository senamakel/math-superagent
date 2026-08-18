<!-- source: https://arxiv.org/pdf/0705.1609 | converted from PDF -->

arXiv:0705.1609v2  [math.DS]  24 Nov 2007
Perturbations of quadratic centers of genus one

S´ebastien Gautier, Lubomir Gavrilov

Institut de Math´ematiques, Universit´e de Toulouse

31062 Toulouse cedex 9, France

Iliya D. Iliev

Institute of Mathematics, Bulgarian Academy of Sciences

Bl. 8, 1113 Soﬁa, Bulgaria

October 31, 2018

Abstract

We propose a program for ﬁnding the cyclicity of period annuli of quadratic
systems with centers of genus one. As a ﬁrst step, we classify all such systems
and determine the essential one-parameter quadratic perturbations which pro-
duce the maximal number of limit cycles. We compute the associated Poincar´e-
Pontryagin-Melnikov functions whose zeros control the number of limit cycles.
To illustrate our approach, we determine the cyclicity of the annuli of two
particular reversible systems.

0. Introduction

As well known, there are four types of planar quadratic systems with a center: 1)
Hamiltonian, 2) reversible, 3) generalized Lotka-Volterra, and 4) of codimension four.
The ﬁrst integral in the Hamiltonian case is a cubic polynomial in (x, y) whose generic
level sets are elliptic curves. It is easy to observe that the generic level sets of the
ﬁrst integral of the codimension four case are elliptic curves too (see the end of Sec-
tion 4). Our main eﬀorts will be devoted to the remaining two cases. It has been
recently proved by one of the authors (S.G.) that there are 18 classes of reversible
centers, 6 classes of reversible Lotka-Volterra centers and 5 classes of generic (non-
reversible) Lotka-Volterra centers whose phase portraits contain only elliptic curves
(possibly, a ﬁnite number of them reducible) [5]. They are given by codimension-one
or codimension-two algebraic sets in the space of all centers from the corresponding
type, see Theorems 1 and 2 below. Throughout the paper, by ”genus” we mean the
genus of the compactiﬁed and normalized generic phase curves. An algebraic phase
curve is generic if it does not contain a singular point of the vector ﬁeld in its closure.

1

The centers whose (generic complexiﬁed) periodic orbits are elliptic curves will be
called centers of genus one. We note that even a quadratic system can have a center
of arbitrarily big genus.
Once we know that the ﬁrst integral of a given planar system with a center de-
ﬁnes elliptic curves, we could raise the next question: how many limit cycles could be
produced in the phase portrait under small quadratic (or even polynomial) pertur-
bations? The purpose of the paper is to present a program for solving this problem.
In what follows we restrict our attention to the limit cycles which bifurcate from
open period annuli (we do not consider graphics). It turns out that, instead of
multi-parameter perturbations, it is enough to consider suitable one-parameter small
quadratic perturbations, see [9]. The one-parameter perturbations which produce
the maximal number of limit cycles in the quadratic case, called essential perturba-
tions, together with the corresponding generating functions of limit cycles (or also
Poincar´e-Pontryagin-Melnikov functions) were determined in [14].
The ﬁrst part of our program is to adapt the results of [14] to our case. The result
is a complete list of such essential perturbations of quadratic systems with centers of
genus one, together with the corresponding generating functions. The list is presented
in Section 3 (in the reversible case) and in Section 4 (in the Lotka-Volterra case).
The second part of the program is to study the zeros of the generating functions
I(t) found in Sections 3 and 4. The fact that each I(t) = ∫

{H=t} ω is a complete
elliptic integral from a rational one-form ω, over the level sets {H = t} ⊂ C2 which are
elliptic curves, allows one to apply all related facts from algebraic geometry in order to
estimate the number of zeros of I(t) and thus to set up some upper (or lower) bounds
on the number of bifurcating limit cycles in the system, see e.g. [20, 19, 11, 7, 8].
This part of our program is illustrated in Section 5, where we study the cyclicity of
the period annuli for two types of quadratic reversible systems with centers of genus
one.
The paper is organized as follows. In Section 1 we determine all reversible centers
with phase portrait formed by elliptic curves. In Section 2 we discuss the same ques-
tion for the Lotka-Volterra centers (reversible or not). These results were previously
proved in [5]. For convenience of the reader we present here almost self-contained
proofs adapted for the purposes of the present paper. In Sections 3 and 4 we de-
termine for each of the cases the corresponding generating function, the complete
elliptic integral I(t) which is the leading term in the expansion of the ﬁrst return
mapping, respectively for the reversible and Lotka-Volterra cases. We also present
there (as Conjectures 1 and 2) the expected exact upper bounds for the number of
zeros of all generating functions. In Section 5 we use the geometric properties of the
elliptic ﬁbration determined by the ﬁrst integral of the quadratic system, in order to
determine, for two of the cases, the number of the zeros of I(t). From this we deduce
an exact result: the cyclicity of the annuli under consideration is two (Theorem 3).

2

1. The reversible case

The general ﬁrst integral of a reversible system with a center at the origin

˙z = −iz + az2 + 2|z|2 + b¯z2, a, b ∈ R, z = x + iy (1.1)

is given by H(x, y) = X λ( 1
2 y2 + AX 2 + BX + C) (1.2)

where X = 1+2(a−b)x and λ, A, B, C are explicit rational functions of the parameters
a, b (see formula (1.7) below). Moreover, one has λ ̸= 0, −1, −2. Along with the elliptic
Hamiltonian H = 1
2y2 + 1
2 x
2 − 4
3x
3 (corresponding to a = b = −1 in (1.1)), formula
(1.2) contains all the cases for which {H = t} is (possibly) an algebraic curve of genus
1. Below, we are going to determine all these cases.
We begin with the observation that it is enough to consider only the case when
λ < −1. Indeed, if λ > −1, by the bi-rational change (X, y) = (1/X1, Y1/X1) the
function (1) reduces to H1 = X −2−λ
1 ( 1
2Y 2
1 + CX 2
1 + BX1 + A) with −2 − λ < −1. For
this reason below we will consider the case when

λ = −p
q with p, q ∈ N, p > q, p ̸= 2q, gcd(p, q) = 1

where gcd(p, q) denotes the greatest common divisor of p and q.

1. Assume ﬁrst that A ̸= 0, C ̸= 0. Then {H = t} after taking X = x
q (this is an
isomorphic map [5], Lemma 1) reads

1
2y2 = −Ax
2q − Bx
q − C + tx
p. (1.3)

For arbitrary t, the curve (1.3) has a genus 1 if and only if the polynomial on the
right hand side has a degree 3 or 4. That is, either p = 3 and q = 1, 2 or p = 4 and
q = 1.
Consider now the degenerate cases when either A = 0 or C = 0 (let us note that
neither two of the coeﬃcients A, B, C can vanish simultaneously).

2. Assume that A = 0. Then (1.3) is of genus 1 if and only if either p = 3, q = 1, 2 or
p = 4, q = 1, 3. Thus the unique new case compared to the case A ̸= 0 is (p, q) = (4, 3).

3. Let C = 0. If 2q > p > q, by a bi-rational transformation (x, y) = (1/x1, y1/x
q
1)
one can transform (1.3) into
 1
2 y2 = −A − Bx
q + tx
2q−p (1.4)

(here and below, we shall omit the subscript 1). As q > 2q − p, the genus is 1 if and
only if either q = 3, p = 4, 5 or q = 4, p = 5, 7. If p > 2q and q is even, then the
rational change y = y1x
q/2 in (1.3) yields

1
2 y2 = −Ax
q − B + tx
p−q. (1.5)

3

As p − q > q, (1.5) is of genus 1 if and only if (p, q) = (5, 2). Finally, if p > 2q and q
is odd, the rational change y = y1x
(q−1)/2 in (1.3) yields

1
2 y2 = −Ax
q+1 − Bx + tx
p−q+1. (1.6)

As above, (1.6) is of genus one if and only if p − q + 1 equals 3 or 4, which is possible
when either (p, q) = (3, 1) or (p, q) = (4, 1), cases that already have been obtained
when we assumed that A ̸= 0.

Thus we have obtained the complete list of cases for which {H = t}, H given by (1.2)
and t arbitrary, is a curve of genus one (the right column contains the cases with
λ > −1):

(0) H = 1
2y2 + Ax
2 + Bx
3 (the standard elliptic case)

(i) H = X −3( 1
2y2 + AX 2 + BX + C) (ii) H = X( 1
2y2 + CX 2 + BX + A)

(iii) H = X −3/2( 1
2y2 + AX 2 + BX + C) (iv) H = X −1/2( 1
2y2 + CX 2 + BX + A)

(v) H = X −4( 1
2y2 + AX 2 + BX + C) (vi) H = X 2( 1
2y2 + CX 2 + BX + A)

(vii) H = X −4/3( 1
2 y2 + BX + C) (viii) H = X −2/3( 1
2y2 + CX 2 + BX)

(ix) H = X −4/3( 1
2 y2 + AX 2 + BX) (x) H = X −2/3( 1
2y2 + BX + A)

(xi) H = X −5/3( 1
2 y2 + AX 2 + BX) (xii) H = X −1/3( 1
2y2 + BX + A)

(xiii) H = X −5/4( 1
2y2 + AX 2 + BX) (xiv) H = X −3/4( 1
2 y2 + BX + A)

(xv) H = X −7/4( 1
2y2 + AX 2 + BX) (xvi) H = X −1/4( 1
2 y2 + BX + A)

(xvii) H = X −5/2( 1
2y2 + AX 2 + BX) (xviii) H = X 1/2( 1
2y2 + BX + A).

We should mention that in cases (iii) and (iv) above it was assumed that C ̸= 0. If
C = 0, the curve has a genus zero, see below.

Let us now recall the exact formula of (1.2) from [14]:

H(X, y) = X − a+b+2
a−b (y2

2 + 1
8(a − b)2
 ( a + b − 2
a − 3b − 2 X 2 + 2 b − 1
b + 1 X + a − 3b + 2
a + b + 2
 )) .

(1.7)
This formula holds outside the lines a = b, a + b + 2 = 0, b = −1, a − 3b − 2 = 0 (note
the last three cases correspond to λ = 0, −1, −2 in (1.2)). Except for the three points
(a, b) = (−1, −1), (±2, 0), on these lines the ﬁrst integrals contain exponents [14] and
hence their level sets are not algebraic curves. For (a, b) = (±2, 0) the level sets are
conic ovals. The lines a + b + 2 = −λ(a − b) in the (a, b)-plane, λ ∈ R, together with
a = b, form the bundle of straight lines through the point (−1, −1) which corresponds
to the standard elliptic case. Therefore using the above results, we obtain:

Theorem 1. The phase curves of (1.1) are algebraic curves of genus one if and only

4

if one of the conditions holds:

(r1) a = 2b + 1 (r2) a = −1 (the reversible Hamiltonian case)

(r3) a = 5b + 4 (b ̸= −3) (r4) a = −3b − 4 (b ̸= −3)

(r5) a = 5
3b + 2
3 (r6) a = 1
3b − 2
3
(r7) (a, b) = ( 5
2, − 1
2 ) (r8) (a, b) = (− 7
2 , − 1
2)

(r9) (a, b) = (−8, −2) (r10) (a, b) = (4, −2)

(r11) (a, b) = (−17, −5) (r12) (a, b) = (7, −5)

(r13) (a, b) = (−7, − 5
3) (r14) (a, b) = ( 11
3 , − 5
3 )

(r15) (a, b) = (−23, −7) (r16) (a, b) = (9, −7)

(r17) (a, b) = (13, 5) (r18) (a, b) = (−3, 5).

For completeness, below we add the list of all cases in (1.1) for which the ovals {H = t}
are conic curves (ellipses). These are

(r19) H = X −3/2( 1
2y2 + AX 2 + BX) when (a, b) = (−11, −3)

(r20) H = X −1/2( 1
2y2 + BX + A) when (a, b) = (5, −3)

(r21) H = X −2( 1
2y2 + BX + C) when (a, b) = (2, 0)

(r22) H = 1
2y2 + CX 2 + BX when (a, b) = (−2, 0).

Cases (r21) and (r22) (not included in (1.2) and (1.7)) are taken from the full list of
ﬁrst integrals of (1.1), see e.g. [14]. The cases (r19) and (r20) are obtained from (1.2)
in the same way as above. Note that (r20) and (r21) are the isochronous centers S3
and S2, respectively. By the way, the isochronous center S4 corresponds to b = 1 in
(r5). Perturbations of the quadratic isochronous centers have been studied in [3].

2. The Lotka-Volterra case

A (generalized) Lotka-Volterra system with a center at the origin has in complex
coordinates the form
 ˙z = −iz + Az2 + B ¯z2, z, A, B ∈ C. (2.1)

Apart of the classical Lotka-Volterra system, the generalized one splits into real and
complex cases. In appropriate coordinates, the general ﬁrst integral of the Lotka-
Volterra system in the classical real case is

H(x, y) = x
λyµ(1 − x − y), λ, µ ∈ R, λµ(λ + µ + 1) ̸= 0. (2.2)

The general ﬁrst integral in the complex case is

H(x, y) = (x
2 + y2)λ(1 − 2x)e
−2µArctan(y/x), λ, µ ∈ R, λ < −1
2 . (2.3)

When µ = 0 in the complex case and when (λ − µ)(λ − 1)(µ − 1) = 0 in the real
case, the corresponding system becomes reversible. That is, after a suitable aﬃne

5

change of the variables, the initial system with a ﬁrst integral (2.2) or (2.3) will take
in complex coordinates one of the normal forms

˙z = −iz + z2 + b¯z2, b ∈ R; ˙z = −iz + ¯z2. (2.4)

This is possible provided that the coeﬃcients in (2.1) satisfy A
3B ∈ R. Our main
result in this section is the following.

Theorem 2. The phase curves of (2.1) are algebraic curves of genus one if and only
if one of the conditions holds:

(rlv1) A = 0 (the Hamiltonian triangle)

(rlv2) 2AB − ¯A
2 = 0 (lv1) AB + (1 ± 2i) ¯A
2 = 0

(rlv3) AB − 3 ¯A
2 = 0 (lv2) 169AB − (101 ± 28i) ¯A
2 = 0

(rlv4) 5AB − 3 ¯A
2 = 0 (lv3) 289AB − (151 ± 42i) ¯A
2 = 0

(rlv5) 5AB − ¯A
2 = 0 (lv4) 1681AB − (783 ± 60√
2i) ¯A
2 = 0

(rlv6) 3AB + ¯A
2 = 0 (lv5) 841AB − (349 ± 12i) ¯A
2 = 0

The above statement is a consequence of the following two propositions which will be
proved together:

Proposition 1. The phase curves of the reversible Lotka-Volterra system (2.1),
A
3B ∈ R, are algebraic curves of genus one if and only if its ﬁrst integral is aﬃne
equivalent to one of the normal forms

(rlv1) H = xy(1 − x − y) (the Hamiltonian triangle)

(rlv2) H = x
−3y(1 − x − y)

(rlv3) H = x
2y(1 − x − y)

(rlv4) H = x
−4y(1 − x − y)

(rlv5) H = (x
2 + y2)− 2
3 (1 − 2x)

(rlv6) H = (x
2 + y2)−2(1 − 2x).

Proposition 2. The phase curves of the generic Lotka-Volterra system (2.1), A
3B ̸∈
R, are algebraic curves of genus one if and only if the ﬁrst integral is aﬃne equivalent
to one of the normal forms
 (lv1) H = x
2y3(1 − x − y)

(lv2) H = x
−6y2(1 − x − y)

(lv3) H = x
−6y3(1 − x − y)

(lv4) H = x
−4y2(1 − x − y)

(lv5) H = x
−3y 3
2 (1 − x − y).

6

Proof of Propositions 1 and 2. Under the conditions in (2.3), the critical point( λ
2λ+1 , µ
2λ+1 ) is a center. The origin is a focus for µ ̸= 0 and a center elsewhere.
Clearly, the phase curves deﬁned by (2.3) could be elliptic only if µ = 0. Note that if
µ = 0, the origin is a center for all λ ̸= 0, but this center is reversible and the system
can be transformed into the normal form (1.1). Here we study the Lotka-Volterra
center outside the origin, existing for λ < − 1
2.
Under the conditions in (2.2) (frankly, one should take H = xy(1−x−y)|x|λ−1|y|µ−1

there, but modules will be omitted thoroughly), there is a unique critical point( λ
λ+µ+1 , µ
λ+µ+1 ) outside the invariant straight lines x = 0, y = 0, x + y = 1, which is
a center if and only if λµ(λ + µ + 1) > 0. In fact, there are two topologically diﬀerent
conﬁgurations having a center, the ﬁrst one is obtained for λ > 0, µ > 0 and the
second one corresponds to the parameters outside the ﬁrst quadrant. In this latter
case, one can take without loss of generality λ < 0, µ < 0. Indeed, if e.g. λ < 0 < µ,
then applying an aﬃne change x = 1 − X − Y , y = Y , we reduce the ﬁrst integral
H(x, y) = t in (2.2) to H1(X, Y ) = t1 where

H1(X, Y ) = X 1/λY µ/λ(1 − X − Y ), t1 = t
1/λ (2.5)

One can proceed similarly with the other case µ < 0 < λ. In the same way, when λ
and µ are positive, we can reduce their values to λ, µ ∈ (0, 1]. Indeed, if e.g. λ > 1
and λ ≥ µ, the same change as above transforms (2.2) into (2.5), with both degrees
in (2.5) within (0, 1]. We proceed similarly if µ > 1 and µ ≥ λ.
When λµ(λ + µ + 1) = 0, the ﬁrst integral in (2.2) should be replaced by another
one containing logarithmic or exponential terms [14, 21, 23] and therefore its level
sets are not algebraic curves. In this way we have reduced our consideration to the
following two cases

(I) 0 < λ ≤ 1, 0 < µ ≤ 1,

(II) λ < 0, µ < 0, λ + µ + 1 > 0.

In the reversible Lotka-Volterra cases, one can ﬁnd all curves with a genus one by
simply using the results from the previous section. Take the real reversible case and
assume for deﬁniteness that λ = µ. The remaining possibilities are reduced to this one
by the same change which we used to obtain (2.5) from (2.2). Let λ = µ ∈ (−1/2, 1].
A further substitution in (2.2) x = 1
2(1 − X) + Y , y = 1
2(1 − X) − Y transforms the
curve H(x, y) = t to H1(X, Y ) = t1 where

H1(X, Y ) = X 1/λ[− 1
2Y 2 + 1
8 (X − 1)2], t1 = 1
2 t
1/λ. (2.6)

As 1/λ ∈ (−∞, −2) ∪ [1, ∞) and (2.6) takes the form already studied in Section 1
above, we conclude immediately that H1, and hence H, is of genus one if and only
if 1/λ ∈ {−4, −3, 1, 2}. Namely, for λ = µ ∈ {1, 1
2, − 1
4 , − 1
3} in (2.2). In the same
way, taking in the complex case (2.3) µ = 0 and using the substitution x = 1
2 (1 − X),
y = Y , we reduce (2.3) to (2.6) (with a sign + in front of 1
2 ). As 1/λ ∈ (−2, 0)
now, one obtains a curve of genus one if and only if 1/λ ∈ {− 3
2 , − 1
2}. That is, for
λ ∈ {− 2
3 , −2} and µ = 0 in (2.3). Thus we have obtained the complete list of cases

7

with genus one in the reversible Lotka-Volterra system (the ﬁrst three entries in the
right column contain the cases with µ = 1; the cases with λ = 1 are obtained by a
rotation of the variables (x, y) → (y, x))

H = xy(1 − x − y)

H = x 1
2 y 1
2 (1 − x − y) H = x
2y(1 − x − y)

H = x
− 1
4 y− 1
4 (1 − x − y) H = x
−4y(1 − x − y)

H = x
− 1
3 y− 1
3 (1 − x − y) H = x
−3y(1 − x − y)

H = (x
2 + y2)− 2
3 (1 − 2x) H = (x
2 + y2)−2(1 − 2x).

For a completeness, let us add to the above list the unique reversible Lotka-Volterra
case having conic orbits, namely

(rlv0) H = (x
2 + y2)−1(1 − 2x).

This is the quadratic isochronous center known as S1 and it corresponds to b = 0 in
(2.4). This ﬁnishes the proof of Proposition 1.
Now we come to the generic (non-reversible) real cases (I), (II) above, where
(λ − µ)(λ − 1)(µ − 1) ̸= 0. Consider ﬁrst (I). Let

λ = p
q , µ = r
s , p, q, r, s ∈ N, p < q, r < s, gcd(p, q) = 1, gcd(r, s) = 1.

We replace our ﬁrst integral H(x, y) = t with H1(x, y) = t1 where:

H1(x, y) = x
p1yq1(1 − x − y)r1, p1 = λr1, q1 = µr1, t1 = t
r1, r1 = qs/gcd(q, s).
(2.7)
The irreducible algebraic curve

Γt = {(x, y) ∈ C2 : x
pyq(1 − x − y)r = t}, p, q, r ∈ N, p < q < r, gcd(p, q, r) = 1
(2.8)

is smooth if and only if t ̸∈ ∆ = {0, ( r
p+q+r ) p2+q2+r2

r }. Let ¯Γt be the associated compact
Riemann surface. Its (geometric) genus is one and the same for all t ̸∈ ∆. We have
(cf. [5, 6]):

Proposition 3. The compact Riemann surface ¯Γt, t ̸∈ ∆, is of genus one if and only
if p = 1, q = 2, r = 3.

Proof. For reader’s convenience, we repeat the proof from [5]. It is based on the
Poincar´e-Hopf formula, namely deg(ω) = 2g − 2, which we apply to the meromorphic
one-form related to the ﬁrst integral (2.8)

ω = − dx
x[q − qx − (q + r)y] = dy
y[p − py − (p + r)x] .

We recall that, in our context, deg(ω) = ∑

k nk where the summation is taken over
all zeros or poles of ω, and nk are their orders. The above one-form has neither zeroes

8

nor poles in the aﬃne chart outside the critical locus. Hence it suﬃces to consider it
at inﬁnity. There are 3 points at inﬁnity: S1 = [1 : 0 : 0], S2 = [0 : 1 : 0], S3 = [1 :
−1 : 0]. The local coordinates near S1 can be chosen as follows. Write x = 1/u with
u → 0. After this change of coordinates, equation (2.8) becomes yq(1−u+yu)r = up+r

(we take t = (−1)r for simplicity). Since u → 0, we have y → 0 (if y → ∞, we would
have yu → −1 which corresponds to S3). Consequently, up to bi-analyticity, there
are local coordinates (u, y) verifying yq = up+r. Let m = gcd(q, p + r). There are m
diﬀerent parameterizations, namely:

u = ξ q
m , y = e 2ikπ
m ξ p+r
m , k = 0, . . . , m − 1,

which correspond to the m diﬀerent local coordinates near the m smooth points given
after blowing-up S1. In these local coordinates,

ω = −ud(1/u)
q − q/u − (q + r)y = qdξ

mξ[q − qξ− q
m − (q + r)e 2ikπ
m ξ p+r
m ] .

We conclude that near the m points, ω has a zero of order q
m − 1.
We perform the same study near the two other points at inﬁnity. Near S2, by
symmetry, we obtain n = gcd(p, q + r) points where the one-form ω has a zero of
order p
n − 1. Similarly, near S3, there are l = gcd(r, p + q) points where ω has a zero
of order r
l − 1.
As a result, we obtain the formula deg(ω) = p + q + r − n − m − l and therefore
the curve (2.8) is elliptic if and only if

p + q + r = n + m + l. (2.9)

Now we have to resolve this Diophantine equation. Obviously, we have m ≤ q, n ≤ p
and l ≤ r, hence (2.9) is true if and only if

gcd(q, p + r) = q, gcd(p, q + r) = p, gcd(r, p + q) = r.

Take natural numbers α, β, γ such that q + r = pα, p + r = qβ, p + q = rγ. The
latter system has a nonzero solution

p
r = γ + 1
α + 1 , q
r = γ + 1
β + 1

if and only if αβγ = 2 + α + β + γ.

By (2.8) we have α > β > γ and the unique solution satisfying this condition is α = 5,
β = 2, γ = 1 which leads to p/r = 1/3, q/r = 2/3. □

To consider the second case (II), we note that a bi-rational change of the variables

x = −X
1 − X − Y , y = −Y
1 − X − Y

9

transforms (II) to a case already considered: H1 = X ΛY M (1 − X − Y ) = t1 with
Λ > 0, M > 0, where

Λ = −λ
λ + µ + 1 , M = −µ
λ + µ + 1 , t1 = t
−1/(λ+µ+1). (2.10)

Hence one can use the values of Λ, M already obtained above to calculate λ and µ
for case (II) through the formula

λ = −Λ
Λ + M + 1, µ = −M
Λ + M + 1 .

Thus we have completed the list of all cases with genus one in the generic Lotka-
Volterra system (another 15 cases are obtained by a rotation of the variables):

H = x 2
3 y 1
3 (1 − x − y) H = x 3
2 y 1
2 (1 − x − y) H = x
2y3(1 − x − y)

H = x
− 1
6 y− 1
3 (1 − x − y) H = x
−6y2(1 − x − y) H = x 1
2 y−3(1 − x − y)

H = x
− 1
6 y− 1
2 (1 − x − y) H = x
−6y3(1 − x − y) H = x 1
3 y−2(1 − x − y)

H = x
− 1
4 y− 1
2 (1 − x − y) H = x
−4y2(1 − x − y) H = x 1
2 y−2(1 − x − y)

H = x
− 1
3 y− 1
2 (1 − x − y) H = x
−3y 3
2 (1 − x − y) H = x 2
3 y−2(1 − x − y).

Proposition 2 is completely proved. □

Proof of Theorem 2. The proof is a direct consequence of Propositions 1 and 2.
More precisely, it follows by a straightforward calculation using the formulas from
[14], case (iv) on page 157 there. □

3. The generating function in the reversible case

We are going to study small perturbations of the reversible system (1.1) in the cases
when the ﬁrst integral H deﬁnes a curve of genus one. Consider ﬁrst the quadratic
perturbations of system (1.1) rewritten in real coordinates:

˙x = Hy/M + εf (x, y, ε),

˙y = −Hx/M + εg(x, y, ε) (3.1)

where M = X λ−1 and f, g are quadratic polynomials with coeﬃcients depending an-
alytically on the small parameter ε. Given a perturbation (f, g), the limit cycles in
(3.1) are determined by the zeroes of the leading term I(t) in the expansion with
respect to ε of the displacement map. For this reason the integral I(t) is called some-
times the generating function. As well known [14], one can always choose a particular
quadratic perturbation so that the corresponding I(t) would have the possible maxi-
mum of zeroes within the whole class of quadratic perturbations. In the generic case
I(t) is given by the complete elliptic integral [14], Theorems 2 and 3

I(t) = ∫

δ(t) x
λ−1(µ1 + µ2x + µ3x
−1)ydx (3.2)

10

where δ(t) is the oval contained in the level set H = t and µi ∈ R. In the exceptional
cases (r10) and (r5) with b = 2 when system (1.1) belongs to the intersection with the
codimension-four stratum Q4 of the center manifold (see [23] for details), I(t) takes
another form and is not an Abelian integral [14]. In the standard elliptic case when
a = b = −1 in (1.1) (we will denote it by (r0)), the integral has a speciﬁc form, too.
Using (3.2) and the list of ﬁrst integrals of genus one (0)-(xviii) above, we obtain the
concrete form of I(t) for all the cases (after appropriate re-scaling of x, y, t, H, I) as
follows:

(r0) I(t) = ∫

H=0(µ1 + µ2t + µ3x)ydx,

H = 1
2 y2 − 1
2x
2 + 1
3x
3 − t, t ∈ (− 1
6 , 0)

(r1) I(t) = ∫

H=0 x
−4(µ1 + µ2x + µ3x
−1)ydx,

(r2) I(t) = ∫

H=0 x
−3(µ1 + µ2x
−1 + µ3x)ydx,

H = 1
2 y2 + 3−b
6(b+1) + b−1
b+1x + 1−3b
2(b+1) x
2 − tx
3

(r3) I(t) = ∫

H=0 x
−4(µ1 + µ2x
2 + µ3x
−2)ydx,

(r4) I(t) = ∫

H=0 x
−2(µ1 + µ2x
−2 + µ3x
2)ydx,

H = 1
2 y2 + b+3
24(b+1) + b−1
4(b+1) x
2 + 3b+1
8(b+1) x
4 − tx
3

(r5) I(t) = ∫

H=0 x
−5(µ1 + µ2x + µ3x
−1)ydx, (b ̸= 2)

(r5) I(t) = ∫

H=0 x
−5[µ1 + µ2x + µ3x
−2 + µ4(1 − x
−1) ln x]ydx, (b = 2)

(r6) I(t) = ∫

H=0 x
−4(µ1 + µ2x
−1 + µ3x)ydx,

H = 1
2 y2 + 2−b
4(b+1) + b−1
b+1x + 1−2b
2(b+1) x
2 − tx
4

(r7) I(t) = ∫

H=0 x
−5(µ1 + µ2x
3 + µ3x
−3)ydx,

(r8) I(t) = ∫

H=0 x
−2(µ1 + µ2x
−3 + µ3x
3)ydx,

H = 1
2 y2 + 1
12 − 1
3x
3 − tx
4, t ∈ (− 1
4, 0)

(r9) I(t) = ∫

H=0(µ1 + µ2x
−3 + µ3x
3)ydx,

(r10) I(t) = ∫

H=0 x
−3[µ1 + µ2x
3 + µ3x
6 + µ4(2x
3 − 1 − x
−3) ln x]ydx,

H = 1
2 y2 + 1
6 + 1
3x
3 − tx
2, t ∈ ( 1
2, ∞)

(r11) I(t) = ∫

H=0 x(µ1 + µ2x
−3 + µ3x
3)ydx,

(r12) I(t) = ∫

H=0 x
−2(µ1 + µ2x
3 + µ3x
−3)ydx,

H = 1
2 y2 + 1
3 + 1
6x
3 − tx, t ∈ ( 1
2, ∞)

(r13) I(t) = ∫

H=0(µ1 + µ2x
−4 + µ3x
4)ydx,

(r14) I(t) = ∫

H=0 x
−4(µ1 + µ2x
4 + µ3x
−4)ydx,

H = 1
2 y2 + 1
12 + 1
4x
4 − tx
3, t ∈ ( 1
3, ∞)

11

(r15) I(t) = ∫

H=0 x
2(µ1 + µ2x
−4 + µ3x
4)ydx,

(r16) I(t) = ∫

H=0 x
−2(µ1 + µ2x
4 + µ3x
−4)ydx,

H = 1
2y2 + 1
4 + 1
12 x
4 − tx, t ∈ ( 1
3 , ∞)

(r17) I(t) = ∫

H=0 x
−5(µ1 + µ2x
2 + µ3x
−2)ydx,

(r18) I(t) = ∫

H=0 x
−3(µ1 + µ2x
−2 + µ3x
2)ydx,

H = 1
2y2 + 1
6 − 1
2x
2 − tx
3, t ∈ (− 1
3, 0).

One can formulate the following conjecture concerning the maximal number of zeroes
of the generating function I(t) and the corresponding maximal number of limit cycles
produced by the period annulus (called its cyclicity).

Conjecture 1. (cf. [14]) The period annulus around the center at the origin in (r0)-
(r22) has the following cyclicity under small quadratic perturbations: three for cases
(r1) with a
∗ < a < 4, (r3) with 7
3 < a < 4, (r4) with 4 < a < 5, (r5) with a = 4, (r6)
with a > 4 and (r10), and two otherwise.

We note that a
∗ ∈ ( 5
3 , 3) is determined from a transcendental equation [15] and can
be calculated numerically, a
∗ = 2.0655...
Let us mention that for some of the cases Conjecture 1 has already been veriﬁed.
The standard elliptic case (r0) is studied entirely in [19]. The reversible Hamiltonian
case (r2) has been investigated in a series of papers, see [4] and the references therein.
Cases (r5) with b = 2 and (r10) were considered in [14] and [13], respectively. Cases
(r5) for b ̸= 2, 1
2 and (r6) with b ∈ ( 1
2, 2) are studied in [2]. Case (r1) with b ∈ (−1, 1
3 )
and b ∈ ( 1
3, 3) are considered in [22] and [15], respectively. Below we will concentrate
our eﬀorts mainly on the cases where Conjecture 1 remains open and will include in
our lists that follow only these unsolved cases.

In order to reduce the number of Hamiltonians, we replace
(x, y) → (1/x, y/x
2) in cases (r5) and (r6),
(x, y) → (x/(−4t), y/(−4t)3/2) in cases (r7) and (r8),
(x, y) → (2tx, (2t)3/2y) in case (r9),
(x, y, t) → ((−6s)1/3x, y, (−48s)−1/3) in cases (r11) and (r12),
(x, y) → (3tx, 9t
2y) in cases (r13) and (r14),
(x, y) → (1/(3tx), y/x
2) in cases (r15) and (r16),
(x, y) → (−x/3t, −y/3t) in cases (r17) and (r18).

12

In this way we obtain a reduced list of cases to study as follows:

(r1) I(t) = ∫

H=0 x
−4(µ1 + µ2x + µ3x
−1)ydx, (b ̸∈ (−1, 1
3) ∪ ( 1
3 , 3))

(r11) I(t) = ∫

H=0 x(µ1 + µ2t
−1x
−3 + µ3tx
3)ydx, (b = 1
3)

(r12) I(t) = ∫

H=0 x
−2(µ1 + µ2tx
3 + µ3t
−1x
−3)ydx, (b = 1
3 )

H = 1
2y2 + 3−b
6(b+1) + b−1
b+1x + 1−3b
2(b+1) x
2 − tx
3

(r3) I(t) = ∫

H=0 x
−4(µ1 + µ2x
2 + µ3x
−2)ydx,

(r4) I(t) = ∫

H=0 x
−2(µ1 + µ2x
−2 + µ3x
2)ydx,

H = 1
2y2 + b+3
24(b+1) + b−1
4(b+1) x
2 + 3b+1
8(b+1) x
4 − tx
3

(r5) I(t) = ∫

H=0 x(µ1 + µ2x
−1 + µ3x)ydx, (b = 1
2)

(r6) I(t) = ∫

H=0(µ1 + µ2x + µ3x
−1)ydx, (b ̸∈ ( 1
2 , 2))

H = 1
2y2 + 1−2b
2(b+1) x
2 + b−1
b+1x
3 + 2−b
4(b+1) x
4 − t

(r7) I(t) = ∫

H=0 x
−5(µ1 + µ2t
−1x
3 + µ3tx
−3)ydx,

(r8) I(t) = ∫

H=0 x
−2(µ1 + µ2tx
−3 + µ3t
−1x
3)ydx,

(r13) I(t) = ∫

H=0(µ1 + µ2tx
−4 + µ3t
−1x
4)ydx,

(r14) I(t) = ∫

H=0 x
−4(µ1 + µ2t
−1x
4 + µ3tx
−4)ydx,

(r15) I(t) = ∫

H=0 x
−6(µ1 + µ2t
−1x
4 + µ3tx
−4)ydx,

(r16) I(t) = ∫

H=0 x
−2(µ1 + µ2tx
−4 + µ3t
−1x
4)ydx,

H = 1
2y2 − 1
3x
3 + 1
4x
4 − t, t ∈ (− 1
12 , 0)

(r9) I(t) = ∫

H=0(µ1 + µ2tx
−3 + µ3t
−1x
3)ydx,

(r17) I(t) = ∫

H=0 x
−5(µ1 + µ2t
−1x
2 + µ3tx
−2)ydx,

(r18) I(t) = ∫

H=0 x
−3(µ1 + µ2tx
−2 + µ3t
−1x
2)ydx,

H = 1
2y2 − 1
2x
2 + 1
3x
3 − t, t ∈ (− 1
6 , 0).

It is useful to know the dimension of the Picard-Fuchs system satisﬁed by the ba-
sic integrals Ik(t) = ∫

δ(t) x
kydx involved in the formulas above. Let us rewrite the
equation H = 0 into the form 1
2y2 = D(x, t). Then for any k ∈ Z one obtains
∫

δ(t) x
kD′ydx = ∫

δ(t) x
kyd( 1
2y2) = 1
3 ∫

δ(t) x
kdy3 = − k
3 ∫

δ(t) x
k−1y3dx.

Therefore ∫

δ(t) x
k−1 (
xD′ + 2k
3 D) ydx = 0.

Taking D = A0 + A1x + A2x
2 + A3x
3 + A4x
4, in terms of the basic integrals Ik(t) the
last identity is equivalent to

(2k+12)A4Ik+3+(2k+9)A3Ik+2+(2k+6)A2Ik+1+(2k+3)A1Ik +2kA0Ik−1 = 0. (3.3)

13

Using (3.3) with k = 0, 1, 2, . . . and with k = −1, −2, . . . we obtain that

Ik = span(I0, I1, I2), k ≥ 3; Ik = span(I−1, I0, I1, I2), k ≤ −2 (A4 ̸= 0).

Similarly, if A4 = 0, one obtains

Ik = span(I0, I1), k ≥ 2; Ik = span(I−1, I0, I1), k ≤ −2 (A4 = 0, A3 ̸= 0),

and ﬁnally,

Ik = span(I0), k ≥ 1; Ik = span(I−1, I0), k ≤ −2 (A4 = A3 = 0, A2 ̸= 0).

Here ”span” means in general a polynomial R[t, t
−1] span. As a consequence, we can
formulate a result about the dimension of the Picard-Fuchs system satisﬁed by the
basic integrals in (r1), (r3)-(r9) and (r11)-(r18).

Proposition 4. In cases (r1), (r3)-(r4) with b = − 1
3 , (r6) with b = 2, (r9), (r11)-
(r12), (r17)-(r18) the Picard-Fuchs system is of dimension 3 while in the remaining
cases it is of dimension 4.

To derive the Picard-Fuchs equations, we use (3.3) together with the relations

I ′
k(t) = ∫

δ(t)
 x
k∂tD
y dx, ∫
δ(t)
 x
kD′

y dx = −kIk−1(t), ∫

δ(t)
 x
kD
y dx = 1
2 Ik(t). (3.4)

We can use (3.4) to further simplify some of the integrals above. Thus we get the
ﬁnal list of reversible cases of genus one yet to study:

(r1), (r12) I(t) = ∫

H=0 x
−4(µ1 + µ2x
−1 + µ3x)ydx, (b ̸∈ (−1, 1
3 ) ∪ ( 1
3, 3))

(r11) I(t) = ∫

H=0 x
−1(µ1 + µ2x
−1 + µ3x)ydx, (b = 1
3)

H = 1
2y2 + 3−b
6(b+1) + b−1
b+1 x + 1−3b
2(b+1) x
2 − tx
3,

t ∈ (− 2b
3(b+1) , 2(1−3b)2

3(b+1)(3−b)2 ) , b < −1; t ∈ (
− 2b
3(b+1) , 0) , b ≥ 1
3

(r3) I(t) = ∫

H=0 x
−4(µ1 + µ2x
2 + µ3x
−2)ydx,

(r4) I(t) = ∫

H=0 x
−2(µ1 + µ2x
−2 + µ3x
2)ydx,

H = 1
2y2 + b+3
24(b+1) + b−1
4(b+1) x
2 + 3b+1
8(b+1) x
4 − tx
3,

t ∈ ( 2b
3(b+1) , − 2
3(b+1) √
− 3b+1
b+3 ) , b ∈ (−3, − 1
3);

t ∈ ( 2b
3(b+1) , ∞) otherwise.

(r6) I(t) = ∫

H=0(µ1 + µ2x
−1 + µ3x)ydx, (b ̸∈ ( 1
2, 2))

H = 1
2y2 + 1−2b
2(b+1) x
2 + b−1
b+1 x
3 + 2−b
4(b+1) x
4 − t,

t ∈ (− b
4(b+1) , 0) , b ≥ 2; t ∈ (
− b
4(b+1) , (1−2b)3

4(b+1)(2−b)3 ) , b ≤ 1
2

14

(r7), (r14) I(t) = ∫

H=0 x
−1(µ1 + µ2x
−1 + µ3x)ydx,

(r8) I(t) = ∫

H=0 x
−1(µ1 + µ2x
−1 + µ3t
−1x
2)ydx,

(r13) I(t) = ∫

H=0(µ1 + µ2x
−1 + µ3t
−1x
2)ydx,

(r15) I(t) = ∫

H=0 x
−3(µ1 + µ2x
−1 + µ3x)ydx,

(r5), (r16) I(t) = ∫

H=0 x(µ1 + µ2x
−1 + µ3x)ydx,

H = 1
2y2 − 1
3x
3 + 1
4x
4 − t, t ∈ (− 1
12 , 0)

(r9) I(t) = ∫

H=0(µ1 + µ2x
−1 + µ3t
−1x)ydx,

(r17) I(t) = ∫

H=0 x
−2(µ1 + µ2x
−1 + µ3x)ydx,

(r18) I(t) = ∫

H=0(µ1 + µ2x
−1 + µ3x)ydx,

H = 1
2y2 − 1
2x
2 + 1
3x
3 − t, t ∈ (− 1
6 , 0).

We point out that the above formulas are related in each case to the period annulus
around the center at (1, 0) obtained for t ∈ (tc, ts) where tc is the level corresponding
to the center and ts is the level of the contour at which the annulus terminates.

4. The generating function in the Lotka-Volterra case

As in the previous section, we will obtain the complete list of generating functions
I(t) for the generalized Lotka-Volterra systems (2.1) in the cases when all their orbits
are elliptic curves. Apart of the reversible case, the equivalence classes for the Lotka-
Volterra case listed in Propositions 1 and 2 are a result of aﬃne transformations.
Therefore we can choose by one representative from each such a class and then use
the generating function corresponding to it. We will always choose the cases whose
parameters satisfy conditions (I) and (II) above. Take real coordinates z = x + iy
and consider a small quadratic perturbation as in (3.1). In the reversible case (2.4),
the ﬁrst integral and integrating factor are respectively [14]

H(X, y) = X λ ( y2

2 − λ(λ − 1)2

32(λ + 2)
 (
X − λ + 2
λ
 )2)
 , M = X λ−1 (4.1)

where λ = b + 1
b − 1 , b ̸= 0, ±1, 1
3 , X = 1 − 4x
λ − 1 .

The generating function for small quadratic perturbations reads [14], Theorem 3:

I(t) = ∫
H=t x
λ−1[µ1y + µ2yx
−1 + µ3(x − 1)y−1]dx. (4.2)

In the Hamiltonian triangle case (rlv1), the integral I(t) takes another form and this
case has already been studied in [12]. For this reason (rlv1) is not included in our
list below. By (4.1), (4.2), (2.6) and the formulas of ﬁrst integrals of genus one
(rlv2)–(rlv6), we get the list of explicit expressions of I(t) for all other reversible

15

Lotka-Volterra cases as follows:

(rlv2) I(t) = ∫

H=t x
−4(µ1y + µ2yx
−1 + µ3(x − 1)y−1)dx,

H = x
−3( 1
2y2 − (x − 1
3)2), t ∈ (− 4
9 , 0)

(rlv3) I(t) = ∫

H=t x(µ1y + µ2yx
−1 + µ3(x − 1)y−1)dx,

H = x
2( 1
2y2 − (x − 2)2), t ∈ (−1, 0)

(rlv4) I(t) = ∫

H=t x
−5(µ1y + µ2yx
−1 + µ3(x − 1)y−1)dx,

H = x
−4( 1
2y2 − (x − 1
2)2), t ∈ (− 1
4 , 0)

(rlv5) I(t) = ∫

H=t x
− 5
2 (µ1y + µ2yx
−1 + µ3(x − 1)y−1)dx,

H = x
− 3
2 ( 1
2y2 + (x + 1
3 )2), t ∈ ( 16
9 , ∞)

(rlv6) I(t) = ∫

H=t x
− 3
2 (µ1y + µ2yx
−1 + µ3(x − 1)y−1)dx,

H = x
− 1
2 ( 1
2y2 + (x + 3)2), t ∈ (16, ∞).

Clearly the elliptic curves in cases (rlv5) and (rlv6) are obtained by introducing a new
variable x → x
2 so that they are given by the level sets of H(x
2, y). Let us also recall
that the functions I(t) in (rlv2)-(rlv6) are the coeﬃcients at ε2 in the expansion of
the displacement map obtained for the special perturbations in (3.1) which keep the
coeﬃcient at ε zero.

What concerns the small quadratic perturbations of the generic (nonreversible) Lotka-
Volterra system, in (3.1) we have M = x
λ−1yµ−1 (modules needed outside the ﬁrst
quadrant but we will omit them) where H is determined by (2.2). In the generic case
I(t) is given by the complete elliptic integral [14], Theorem 2

I(t) = ∫ ∫

Int δ(t) x
λ−1yµ−1(µ1 + µ2x
−1 + µ3y−1)dxdy. (4.3)

Using (4.3) and the list of ﬁrst integrals of genus one (lv1)–(lv5), we easily obtain the
concrete form of I(t) for all the cases as follows:

(lv1) I(t) = ∫
H=t x
− 1
3 y 1
3 (µ1 + µ2x
−1 + µ3y−1)dx,

H = x 2
3 y 1
3 (1 − x − y), t ∈ (0, 432−1/3),

(lv2) I(t) = ∫
H=t x
− 7
6 y− 1
3 (µ1 + µ2x
−1 + µ3y−1)dx,

H = x
− 1
6 y− 1
3 (1 − x − y), t ∈ (4321/6, ∞),

(lv3) I(t) = ∫
H=t x
− 7
6 y− 1
2 (µ1 + µ2x
−1 + µ3y−1)dx,

H = x
− 1
6 y− 1
2 (1 − x − y), t ∈ (4321/6, ∞),

(lv4) I(t) = ∫
H=t x
− 5
4 y− 1
2 (µ1 + µ2x
−1 + µ3y−1)dx,

H = x
− 1
4 y− 1
2 (1 − x − y), t ∈ (2√2, ∞),

(lv5) I(t) = ∫
H=t x
− 4
3 y− 1
2 (µ1 + µ2x
−1 + µ3y−1)dx,

H = x
− 1
3 y− 1
2 (1 − x − y), t ∈ (4321/6, ∞).

16

As in Section 3, we formulate a general conjecture about the cyclicity of the period
annulus in the Lotka-Volterra systems having all their orbits elliptic or conic curves.

Conjecture 2. The cyclicity under small quadratic perturbations of the period an-
nulus surrounding the center at the origin in the Lotka-Volterra system (2.1) is as
follows: three in case (rlv1) (the Hamiltonian triangle) and two in all other cases
(rlv2)-(rlv6), (lv1)-(lv5).

Except for the isochronous center S1 and the Hamiltonian triangle, it is very likely
that Conjecture 2 is still open. We recall that quadratic perturbations of the general
Lotka-Volterra system have been considered in [23]. However, in the recent book [1],
page 379, V.I. Arnold declared that the problem with the Lotka-Volterra system still
remains open.

Remark about the codimension four case. In this remark we discuss in brief
the generic (non-reversible) codimension 4 center. In complex coordinate z = x + iy,
the related system becomes

˙z = −iz + 4z2 + 2|z|2 + α¯z2, α ∈ C \ R, |α| = 2.

In (¯x, ¯y) = (X 2, Y ) coordinates, where

Y = (2 + b)x + cy, X = 1 + 8x + 4
2 + b Y 2, α = b + ic,

the system has a ﬁrst integral of the form [14] (below the bars are omitted)

H(x, y) = x
−3

8(2 − b)
 ( 4y3

3(2 + b) + 4y2

2 + b + (1 − x
2)y − x
2 + 1
3
 ) .

It is seen that the level sets of this ﬁrst integral are (generically) elliptic curves.
Therefore the generating function I(t) whose zeroes correspond to limit cycles in
the perturbed system are given by the following complete elliptic integral (cf. [14],
Theorem 2 (iii))

I(t) = ∫ ∫

H(x,y)<t x
−6[µ1 + µ2y + µ3y3 + µ4(κ
2y4 − x
4)]dxdy, κ = 4
2 + b .

The conjecture that the integral I(t) has at most three zeroes in the interval (tc, ts) =
(− 1
12(2−b) , 0) corresponding to the period annulus around the center at (xc, yc) = (1, 0)
is still open.

5. Zeros of Abelian integrals for some of the reversible cases

In this section we study the generating functions I(t) related to the reversible quadratic
systems (r18) and (r11). These systems contain no parameter, have a unique period
annulus around the center at (1, 0) and the Picard-Fuchs system satisﬁed by the com-
ponents of J(t) = I ′(t) is of dimension three and two (respectively). Our main result
is the following.
 17

Theorem 3. The exact upper bound of the number of the limit cycles produced by the
period annulus under quadratic perturbations of the reversible system (r18) or (r11)
is two.

To prove Theorem 3 we study ﬁrst one-parameter analytic quadratic perturbations
of (r18) and (r11). According to the formulas derived in Section 3, the number of
the limit cycles of such perturbations is bounded by the number of the zeros of the
following generating functions

I(t) = ∫

δ(t)(µ1 + µ2x
−1 + µ3x)ydx, t ∈ (
−1
6 , 0) , Ht = 1
2 y2 − 1
2 x
2 + 1
3x
3 − t, (5.1)

for system (r18) and

I(t) = ∫

δ(t) x
−1(µ1+µ2x
−1+µ3x)ydx, t ∈ (−1
6 , 0) , Ht = 1
2 y2+ 1
3 − 1
2 x−tx
3, (5.2)

for system (r11). In the above integrals δ(t) denotes the unique oval of the real
algebraic curve {(x, y) ∈ R2 : Ht(x, y) = 0} for a given t ∈ (− 1
6 , 0) and µi are arbitrary
real constants. The ovals δ(t) in (5.1) form a period annulus which is bounded by the
homoclinic loop {H0 = 0} going through the saddle at the origin, while in the case
(5.2) they form a period annulus bounded by the parabola {H0 = 0}. In both cases,
the ovals δ(t) exist for t ∈ (− 1
6 , 0), I(t) is analytic in a neighborhood of t = −1/6,
and I(−1/6) = 0. Consider the derivative J(t) = I ′(t), see formulae (5.12), (5.13)
bellow. The key ingredient of the proof of Theorem 3 is the following result.

Theorem 4. The three-dimensional vector space of Abelian integrals J(t) = I ′(t),
t ∈ [− 1
6, 0), deﬁned by (5.1) or (5.2) is Chebyshev. This means that each integral J(t)
has at most two zeros (counted with multiplicity) in the interval [− 1
6 , 0).

Before proving Theorem 4 we need some preparation.

5.1. Monodromy of the level curves. Let us denote

Γt = {(x, y) ∈ C2, Ht(x, y) = 0}, Γt = {[x : y : z] ∈ CP
2, Ht ( x
z , y
z
 ) = 0}.

If t ̸= − 1
6, 0, then both Γt and Γt are smooth curves and Γt is a compact Riemann
surface of genus one which is also the compactiﬁcation of the aﬃne elliptic curve Γt.
We have Γt = Γt ∪ ∞ where ∞ = [0 : 1 : 0] and therefore

rank H1(Γt, Z) = 2, rank H1(Γt, Z) = 2.

For (5.2), all compact complex level curves Γt have two complex conjugate common

points, namely: P + = (0, i
√ 2
3) and P − = (0, −i
√ 2
3) in aﬃne coordinates, as well
as one common point at inﬁnity. For (5.1) there is one common point, the point
at inﬁnity. For both cases, when blowing-up these points on the complex projective

18

plane P2, one obtains a compact smooth rational surface S and an analytic map
S π
→ P where the projection π is induced by one of the rational maps

C2 → C : (x, y) ↦→ t = 1
2 y2 − 1
2 x
2 + 1
3x
3, (5.3)

C2 99K C : (x, y) ↦→ t =
 1
2 y2 + 1
3 − 1
2x
x3 . (5.4)

In both cases S is an elliptic surface in the sense of Kodaira [16] with three singular
ﬁbers π−1(0), π−1(−1/6), π−1(∞). In particular, this allows one to compute the global
monodromy of the related homology bundle as described below.

5.1.1. The monodromy of the ﬁbration (5.3). Denote by 0± the two points
on Γt with coordinates (x = 0, y = ±
√2t) and let ̂Γt = Γt \ {0+, 0−}. We shall
determine the monodromy of the homology bundle associated to (5.3) with ﬁbers
H1(̂Γt, Z) = Z
3. Let δ(t), γ(t) be a continuous family of cycles, vanishing at t = −1/6
and t = 0 respectively, and let α(t) be a cycle represented by a small loop around 0+

on ̂Γt. We need to describe the monodromy of these cycles on the plane C\{0, −1/6}.
The precise deﬁnition of the families δ(t), γ(t) is as follows. For t ∈ (−1/6, 0) the
polynomial 1
3 x
3 − 1
2 x
2 − t has three real roots x1(t) < 0 < x2(t) < x3(t). Let l be a
simple loop on C \ {x1(t), 0, x2(t), x3(t)} which makes one turn about x1(t), 0, x2(t)
in a positive direction and does not contain in its interior x3(t).
We deﬁne γ(t) to be the cycle represented by l on ̂Γt (that is to say by one of the
two pre-images of l under the projection (x, y) ↦→ x). The cycle γ(t) is deﬁned up to a
sign. The cycle ±δ(t) is deﬁned in a similar way, but the simple loop l is supposed to
make one turn about x2(t), x3(t) in a positive direction, and does not contain x1(t), 0
in its interior.
We note that x1(0) = x2(0) = 0, x3(0) > 0 and hence γ(t) is a cycle vanishing at
t = 0. Similarly, δ(t) is a vanishing cycle at t = −1/6, as x1(−1/6) < 0, x2(−1/6) =
x3(−1/6) > 0.
Let
 Π : π1(CP1 \ ∆, t0) → Aut (H1(̂Γt, Z)), ∆ = {− 1
6, 0, ∞}, t0 ∈ (− 1
6, 0)

be the monodromy representation related to the elliptic ﬁbration associated to (5.3).
The image Π(π1(CP1 \ ∆, t0))

is a group generated by l∗
0, l∗
1, l∗
∞ = l∗
1 ◦ l∗
0, the monodromy operators corresponding
respectively to the oriented loops l0, l1, l∞ = l1 ◦ l0. Here l0 is a simple loop which
makes one turn about 0 in a positive direction and does not contain −1/6 in its
interior. Similarly l1 is a simple loop which makes one turn about −1/6 in a positive
direction and does not contain 0 in its interior.

Lemma 1. In the global basis (α(t), δ(t), γ(t)) (with appropriate orientation of the

19

cycles), the monodromy operators associated to the ﬁbration deﬁned by (5.3) are:

l∗
0 : M0 =
 




 −1 1 0

0 1 0

0 −1 1
 



 , l∗
1 : M1 =
 




 1 0 0

0 1 1

0 0 1
 



 ,

l∗
∞ : M∞ = M1M0 =
 




 −1 1 1

0 0 1

0 −1 1
 



 .

Proof. The identity
 2πi ∫

α(t)
 dx
xy = 1
√t

shows that l∗
0(α(t)) = −α(t). The remaining claims follow from the usual Picard-
Lefschetz formula (it is enough to describe the monodromy of the roots xi(t)) and
therefore the details are omitted. □

5.1.2. The monodromy of the ﬁbration (5.4). Here we determine the mon-
odromy representation

Π : π1(CP1 \ ∆, t0) → Aut (H1(Γt, Z)), ∆ = {− 1
6, 0, ∞}, t0 ∈ (− 1
6 , 0)

associated to the elliptic ﬁbration deﬁned by (5.4). The automorphisms l∗
0, l∗
1, l∗
∞
associated to the oriented loops l0, l1, l∞ are deﬁned as in the preceding subsection.
For (5.4) the global monodromy does not follow from the Picard-Lefschetz formula.
The local monodromy (around the singular ﬁbers), however, depends only on the
topological type of these ﬁbers and is computed in [16]. The topological type of the
ﬁbers π−1(0), π−1(−1/6), π−1(∞) on its turn is computed in [5] and it is respectively
(III), (I1), (IV∗) (using the Kodaira notations, see e.g. [17, Table 6.1]). We conclude
that, up to a conjugation, the monodromy operators are given by (e.g. [10, Table 1])

l∗
∞ : M∞ =
 ( −1 −1

1 0
 )
 (IV∗),

l∗
1 : M1 =
 ( 1 1

0 1
 )
 (I1),

l∗
0 : M0 =
 ( 0 1

−1 0
 )
 (III).

By abuse of notation, we denote by δ(t) ∈ H1(Γt, Z), t ∈ (−1/6, 0), the continuous
family of cycles, vanishing when t → − 1
6 along a path connecting t to − 1
6 in (− 1
6 , 0).
Let γ(t) = l∗
0(δ(t)). The continuous families of cycles δ(t), γ(t) are deﬁned in C \
{− 1
6, 0}. According to [18], (δ(t), γ(t)) is a basis of H1(Γt, Z).

20

Lemma 2. In the global basis (δ(t), γ(t)) (with appropriate orientations of the cycles),
the monodromy operators associated to the ﬁbration deﬁned by (5.4) are:

l∗
0 : M0 =
 ( 0 −1

1 0
 )
 , l∗
1 : M1 =
 ( 1 −1

0 1
 )
 , l∗
∞ : M∞ = l∗
1 ◦ l∗
0 =
 ( −1 −1

1 0
 )
 .

Proof. For the global sections δ, γ of the homology bundle we have l∗
0δ = γ, l∗
1δ = δ
and hence
 M0 =
 ( 0 ∗

1 ∗
 )
 , M1 =
 ( 1 ∗

0 ∗
 )
 .

The relations T r(M1) = 2, T r(M0) = 0, det(M0) = 1, T r(M1M0) = T r(M∞) = −1
imply the result. □

5.2. Wronskians. Let
 ωk = x
kdx
y , k ∈ Z

be polynomial one-forms on C2. They induce meromorphic diﬀerential one-forms on
the compact Riemann surface Γt which are denoted in the same way.
Let us introduce the Wronskian

Wδ(t),γ(t)(ωk, ω0) = ∫

δ(t) ωk
 ∫
γ(t) ω0 − ∫

δ(t) ω0
 ∫

γ(t) ωk

where, by abuse of notation, δ(t), γ(t) are continuous families of closed loops, with
the properties :

• they intersect transversally at a single point

• Γt \ {δ(t), γ(t)} is homeomorphic to a rectangle whose opposite sides are iden-
tiﬁed to δ(t) and γ(t)

• The poles of ωk are contained in the interior of this rectangle

As ω0 is holomorphic in both cases, the above Wronskian can be computed by making
use of the reciprocity law for abelian diﬀerentials of the second and third kind [7, p.
647] as shown next. Below, we denote by C a certain nonzero constant. In the case
(5.2) the Wronskian is a rational function and

Wδ,γ(ωk, ω0) = Res∞ωk ∫ P
∞ ω0
2πi =
 



 C
t , k = 1,

0, k = 2,

C
t2 , k = 3.
 (5.5)

21

In a similar way, in the case (5.1) we have

Wδ,γ(ω−1, ω0) = Res0−ω−1
2πi
 ∫ 0−

P0 ω0 + Res0+ω−1
2πi
 ∫ 0+

P0 ω0 = 1
√2t
 ∫ 0+

0− ω0 (5.6)

and
 Wδ,γ(ω1, ω0) = Res∞ω1 ∫ P
∞ ω0
2πi = C ̸= 0. (5.7)

5.3. Asymptotics of the Abelian integrals. Here we study, for suitable k, the
asymptotical behavior of Jk(t) = ∫

δ(t) ωk, where δ(t) is the continuous family of cycles
vanishing at the center (associated to t = −1/6), near t = ∞ and t = 0. Below,
we shall write J(t) ≲ (t − t0)s log(t − t0)r, r, s ∈ R provided that for every sector S
centered at the critical value t0 ∈ ∆ there exists a nonzero constant CS such that
|J(t)| ≤ CS|t − t0|s| log(t − t0)r|.

5.3.1. The case (5.1). Here we have

Jk(t) = ∫
δ(t)
 x
kdx
y = ∫

δ(t)
 x
kdx
√− 2
3x3 + x2 + 2t, k = 0, ±1.

(a) Near t = ∞, the change of variables x = t 1
3 u leads to

Jk(t) = t k
3 − 1
6 ∫
˜δ(t)
 ukdu
√− 2
3 u3 + t
− 1
3 u2 + 2 = t k
3 − 1
6 ˜Jk(t).

When |t| → ∞ (with bounded argument) the integral ˜Jk(t) tends to a ﬁnite
constant. Consequently Jk(t) ≲ t k
3 − 1
6 , k ∈ Z. (5.8)

(b) Near t = 0, the Abelian integral Jk(t) can be expanded as follows

Jk(t) = −ln(t)
2πi
 ∫

γ(t) ωk − 1
2
 ∫

α(t) ωk + Q(t)

where Q is a meromorphic function in a neighborhood of t = 0 (this follows
from Lemma 1). Therefore

Jk(t) = C
√t + P (t) log(t) + Q(t)

where P, Q are meromorphic in a neighborhood of t = 0. We claim that

Jk(t) ≲
 



 log(t) if k = 0,

1 if k = 1,

1√
t if k = −1.
 (5.9)

22

Indeed, for k ≥ 1
 lim
t→0− Jk(t) = 2 ∫ x3(0)

0
 x
k−1dx
√
− 2
3 x + 1

where x3(0) = 3/2. For k = 0 the integral J0(t) is of the ﬁrst kind and its
behavior is well known. For k = −1 the leading term of the expansion of J−1(t)
is given by ∫ ∞

√t
 dx
x
√x2 − t = 1
√t
 ∫ ∞

1
 dx
x
√x2 − 1 .

(c) Near t = −1/6 the functions Jk(t) are holomorphic and Jk(t) ≲ 1.

5.3.2. The case (5.2). We have

Jk(t) = ∫

δ(t)
 x
kdx
y = ∫

δ(t)
 x
kdx
√
2tx3 + x − 2
3 , k = 1, 2, 3.

(a) Near t = ∞, the change of variables x = t
− 1
3 u leads to

Jk(t) = t
− k+1
3 ∫
˜δ(t)
 ukdu
√2u3 + t
− 1
3 u − 2
3
 = t
− k+1
3 ˜Jk(t).

When |t| → ∞ (with a bounded argument) the integral ˜Jk(t) tends to a ﬁnite
constant (possibly zero) and hence

Jk(t) ≲ t
− k+1
3 , k ∈ Z. (5.10)

(b) Near t = 0 any Abelian integral of the ﬁrst or second kind is a power series in
t
1/4 (because the eigenvalues of l∗
0 are fourth roots of the unity). As t tends to
0 two roots of tx
3 + x/2 − 1/3 tend to ∞ which suggests us to make the change
of variables x = t
− 1
2 u. Then we have

Jk(t) = t
−( k
2 + 1
4 ) ∫
˜δ(t)
 ukdu
√2u3 + u − 2
3t 1
2 = t
−( k
2 + 1
4 ) ˜Jk(t)

and hence Jk(t) ≲ t
−( k
2 + 1
4 ), k ∈ Z. (5.11)

(c) Near t = −1/6 the integrals Jk(t) are holomorphic and Jk(t) ≲ 1.

5.4. Proof of Theorem 4. We have to prove that the derivative

J(t) = I ′(t) = µ1
 ∫

δ(t)
 x
2dx
y + µ2
 ∫

δ(t)
 xdx
y + µ3
 ∫

δ(t)
 x
3dx
y (5.12)

23

(in the case (r11)), or

J(t) = I ′(t) = µ1
 ∫

δ(t)
 dx
y + µ2
 ∫

δ(t)
 dx
xy + µ3
 ∫
δ(t)
 xdx
y (5.13)

(in the case (r18)) has at most two zeros. For this, we use the method of Petrov, see
e.g. [20], based on the argument principle.
Introduce the function
 F (t) = J(t)
J0(t) , J0(t) = ∫

δ(t)
 dx
y .

It is real analytic on (−1/6, 0) and has an analytic continuation in the complex domain
D = C \ [0, ∞), because the period J0(t) of the elliptic curve ¯Γt does not vanish there,
including at the point t = −1/6. To bound the number of the zeros of F in D it is
enough to ﬁnd this number in the smaller domain DRr = D ∩ {t : r < |t| < R} for
r suﬃciently small and R suﬃciently big. We are going to evaluate the increment of
the argument of F along the boundary of DRr, oriented in a positive direction.

5.4.1. Zeros of F in the case (r18) and (5.1). Along the boundary of the
small circle {|t| = r}, according to (5.9), the increase of the argument of F is at
worst close to π, and along the boundary of the big circle {|t| = R} this increase
is at worst close to 2π/3, see (5.8). Denote by F ± the restriction on (0, ∞) of the
analytic function obtained as an analytic continuation of F along an arc contained in
the upper (lower) complex half-plane Im ± t > 0 respectively. The function F is real
analytic on (−∞, 0) which implies that along the interval (0, ∞) the imaginary part
Im (F +(t)) of F + satisﬁes

2i Im (F +(t)) = F +(t) − F +(t) = F +(t) − F −(t).

Assume for a moment that F +(t) − F −(t) has at most one simple zero on the interval
(0, ∞). Then summing up the above information we conclude that F (t) has at most
two zeros in the complex domain DRr, and hence in D. This result is obviously exact.
It remains to prove that F +(t) − F −(t) has at most one zero on (0, ∞). Clearly
F − is an analytic continuation of F + along an arc making one turn about t = 0
in a positive direction. This shows that F +(t) − F −(t) is obtained as an analytic
continuation of the function

F (t) − l∗
0(F (t)) =
 ∫
δ(t) ω
∫

δ(t) ω0 −
 ∫

l∗
0δ(t) ω
∫

l∗
0δ(t) ω0 = Wδ(t),l∗
0 δ(t)(ω, ω0)
∫

δ(t) ω0 ∫

l∗
0δ(t) ω0 , t ∈ (−1/6, 0)

along an arc contained in the upper complex half-plane. Here ω = µ1ω0+µ2ω−1+µ3ω1,
l∗
0δ(t), δ(t) are cycles on the elliptic curve deﬁned by Ht = 0, with two removed points
0±, and l∗
0δ(t) = δ(t) − γ(t) + α(t). Let

iW (t), t ∈ (0, ∞)

24

be the real analytic function obtained as an analytic continuation of

iWδ(t),l∗
0 δ(t)(ω, ω0), t ∈ (−1/6, 0)

along an arc contained in the upper complex half-plane. As

F +(t) − F −(t) = W (t)
| ∫

δ(t) ω0|2

then we shall show that iW (t) has at most one zero on (0, ∞). We use once again
the argument principle. We shall show that the analytic continuation of W (t) in
˜D = C \ (−∞, 0) has at most one zero counted with multiplicity. For this purpose we
consider the complex domain

˜DRr = ˜D ∩ {t : |t| > r, |t| < R}.

As before, denote by W ±(t) the restriction on (−∞, 0) of the analytic function ob-
tained as an analytic continuation of W (t), t ∈ (0, ∞) along an arc contained in the
upper (lower) complex half-plane Im ±t > 0 respectively. Along the interval (−1/6, 0)
we have

W +(t) − W −(t) = Wδ(t),l∗
0 δ(t)(ω, ω0) − (l∗
0)−1Wδ(t),l∗
0 δ(t)(ω, ω0)
= Wδ(t),l∗
0 δ(t)(ω, ω0) − W(l∗
0)−1δ(t),δ(t)(ω, ω0)
= Wδ(t),δ(t)+α(t)−γ(t)(ω, ω0) − Wδ(t)+α(t)+γ(t),δ(t)(ω, ω0)
= 2Wδ(t),α(t)(ω, ω0)

= − 2
√2t
 ∫

δ(t) ω0.

Note that, according to section 5.1.1., the functions W ±(t) are single-valued in a
neighborhood of t = −1/6. Therefore

W +(t) − W −(t) = − 2
√2t
 ∫
δ(t) ω0

along the interval (−∞, 0). We conclude that the imaginary part i(W +(t)−W −(t)), t ∈
(−∞, 0) of the analytic continuation of iW (t), t ∈ (0, ∞) does not vanish.
It follows from the asymptotic expansion of Jk near t = 0 obtained in 5.3.1.(b)
that W (t) ≲ 1
√t, t ∼ 0.

Therefore along the small circle {|t| = r}, the increase of the argument of W (t) is
at worst close to π. Along the border of the big circle the decrease of the argument
is close to 2π/6, see (5.8). Summing up the above information we conclude that the
total increase of the argument of W (t) along the border of ˜DRr is close to (or smaller
than) 4π −2π/6 and hence W (t) has at most one zero. Therefore the maximal number
of the zeros of F (t) in D is two (and this result is exact).

25

5.4.2. Zeros of F in the case (r11) and (5.2). In the same way as above we may
study F (t) in the case (r11). This leads, however, to a bound of the number of the
zeros in [−1/6, 0) equal to three. To improve the bound we consider ﬁrst the function
˜F (t) = F (t) + µ4, where µ4 is a real constant. We shall show that ˜F (t) has at most
three zeros in the complex domain D = C \ [0, ∞). For this we consider once again
the domain DRr = D ∩ {t : r < |t| < R} and evaluate the increase of the argument
of ˜F along its border. Along the boundary of the small circle {|t| = r}, according to
(5.11), the increase of the argument of ˜F (t) is close to 3π, and along the boundary
of the big circle {|t| = R} this increase is close to 0, see (5.10). Along the interval
(0, ∞) the imaginary part of F is equal to

W (t)
| ∫

δ(t) ω0|2

where, according to (5.5), for suitable constants c1, c2,

W (t) = c1t + c2
t2 .

It follows that the imaginary part of F (t) has at most one zero along (0, ∞). The
argument principle implies that ˜F (t) has at most three zeros in the complex domain
D. Suppose now that for some µ1, µ2, µ3 the function F (t) has exactly three zeros in
D, and hence in the domain DRr for r suﬃciently small and R big enough. According
to (5.10) for |t| suﬃciently big we have

F (t) = ct
−k/3 + o(|t
−k/3|).

It follows that for suﬃciently small µ4 a real zero of ˜F (t) bifurcates from ∞ on the
interval (−∞, 0) and this zero is not contained in the domain DRr. Therefore ˜F (t)
will have at least four zeros in the domain D, in contradiction with the result proved
above. Therefore the maximal number of the zeros of F (t) in D is two (and this result
is exact).
Theorem 4 is proved. □

5.5. Proof of Theorem 3. Denote the open period annulus of the ﬁxed reversible
system (r18) or (r11) by Π. Let Xλ, λ ∈ Λ be the set of all quadratic plane vector
ﬁelds, analytic with respect to λ and such that X0 coincides with (r18) (respectively,
with (r11)). Theorem 3 can be reformulated as follows:

The cyclicity Cycl(Π, Xλ) of the open period annulus Π is equal to two

which means that Xλ has at most two limit cycles which tend to Π as λ tends to zero.
It is shown in [9, Theorem 1] that if the cyclicity Cycl(Π, Xλ) is ﬁnite, then there
exists a germ of an analytic curve λ(ε), such that

Cycl(Π, Xλ) = Cycl(Π, Xλ(ε)).

26

In other words, it is enough to study one-parameter deformations. Let I(t) be the
ﬁrst non-zero Poincar´e-Pontryagin (or generating) function associated to such a per-
turbation. The derivative J(t) = I ′(t) is of the form (5.12) or (5.13) and we proved
that this function has at most two zeros (Theorem 4), and hence I(t) has at most
three zeros on [−1/6, 0), one of them being t = −1/6 . Therefore, by a standard
argument, the cyclicity of the open period annulus of the perturbed one-parameter
quadratic system is at most two.
It remains to show that the cyclicity Cycl(Π, Xλ) is ﬁnite. It is shown in [9] that if
Cycl(Π, Xλ) = ∞, then there exists a Poincar´e-Pontryagin function I(t) (associated
to some one-parameter deformation) with inﬁnite number of zeros. As I(t) is an
Abelian integral, then this is clearly impossible. This completes the proof of Theorem
3. □

Acknowledgment. This research has been partially supported by PAI Rila program
through Grants 14749SM (France) and Rila 3/6-2006 (Bulgaria).

References

[1] V.I. Arnold (Ed.), Arnold’s problems, Springer Verlag, Berlin (2005).

[2] Guoting Chen, Chengzhi Li, Changjian Liu, J. Llibre, The cyclicity of period
annuli of some classes of reversible quadratic systems, Discr. Cont. Dynam. Syst.
A 16 (2006), no. 1, 157–177.

[3] C. Chicone, M. Jacobs, Bifurcations of limit cycles from quadratic isochrones, J.
Diﬀerential Equations 91 (1991), 268–326.

[4] Shui-Nee Chow, Chengzhi Li, Yingfei Yi, The cyclicity of period annuli of degen-
erate quadratic Hamiltonian systems with elliptic segment loops, Ergodic Theory
Dynam. Systems 22 (2002), no. 2, 349–374.

[5] S. Gautier, Quadratic centers deﬁning elliptic surfaces, Preprint
arXiv:0704.1948v1 (16 April 2007), 23 pp.

[6] S. Gautier, Feuilletages quadratiques plans et leurs perturbations, Ph.D. Thesis,
University of Toulouse (November 2007), 121 pp.

[7] L. Gavrilov, Abelian integrals related to Morse polynomials and perturbations of
plane Hamiltonian vector ﬁelds, Ann. Inst. Fourier (Grenoble) 49 (1999), 611–652.

[8] L. Gavrilov, The inﬁnitesimal 16th Hilbert problem in the quadratic case, Invent.
Math. 143 (2001), 449–497.

[9] L. Gavrilov, Cyclicity of period annuli and principalization of Bautin ideals,
Preprint arXiv:0705.1112, 14 pp, to appear in Ergodic Theory Dynam. Systems.

[10] S. Herfurtner, Elliptic surfaces with four singular ﬁbres, Math. Ann. 291 (1991),
319–342.
 27

[11] E. Horozov, I.D. Iliev, On the number of limit cycles in perturbations of quadratic
Hamiltonian systems, Proc. London Math. Soc. 69 (1994), 198–224.

[12] Iliya D. Iliev, The cyclicity of the period annulus of the quadratic Hamiltonian
triangle, J. Diﬀerential Equations 128 (1996), no. 1, 309–326.

[13] Iliya D. Iliev, Inhomogeneous Fuchs equations and the limit cycles in a class of
near-integrable quadratic systems, Proc. Roy. Soc. Edinburgh A 127 (1997), no.
6, 1207–1217.

[14] Iliya D. Iliev, Perturbations of quadratic centers, Bull. Sci. Math. 122 (1998),
no. 2, 107–161.

[15] Iliya D. Iliev, Chengzhi Li, Jiang Yu, Bifurcations of limit cycles from quadratic
non-Hamiltonian systems with two centres and two unbounded heteroclinic loops,
Nonlinearity 18 (2005), no. 1, 305–330.

[16] K. Kodaira, On compact analytic surfaces II, Ann. Math. 77 (1963), 563–626.

[17] R. Miranda, The moduli of Weirstrass Fibrations Over P1, Math. Ann. 255
(1981), 379-394.

[18] H. Movasati, On the topology of foliations with a ﬁrst integral, Bol. Soc. Bras.
Mat. 31 (2000), no. 3, 305–336.

[19] G.S. Petrov, Elliptic integrals and their non-oscillation, Funct. Anal. Appl. 20
(1986), no 1, 46–49. [in Russian]

[20] G.S. Petrov, Nonoscillation of elliptic integrals, Funct. Anal. Appl. 24 (1990), no
3, 45–50. [in Russian]

[21] Dana Schlomiuk, Algebraic particular integrals, integrability and the problem of
the center, Trans. Amer. Math. Soc. 338 (1993), no. 2, 799–841.

[22] Jiang Yu, Chengzhi Li, Bifurcation of a class of planar non-Hamiltonian inte-
grable systems with one center and one homoclinic loop, J. Math. Anal. Appl.
269 (2002), no. 1, 227–243.

[23] H. ˙Zo l¸adek, Quadratic systems with center and their perturbations, J. Diﬀeren-
tial Equations 109 (1994), no 2, 223–273.

E-mail addresses:

sebagaut@wanadoo.fr
lubomir.gavrilov@math.univ-tlse.fr
iliya@math.bas.bg
 28
