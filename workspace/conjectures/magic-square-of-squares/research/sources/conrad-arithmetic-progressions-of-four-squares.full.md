<!-- source: https://kconrad.math.uconn.edu/blurbs/ugradnumthy/4squarearithprog.pdf | converted from PDF -->

ARITHMETIC PROGRESSIONS OF FOUR SQUARES

KEITH CONRAD

1. Introduction

Suppose a, b, c, and d are rational numbers such that a2, b2, c2, and d2 form an arithmetic
progression: the diﬀerences b2 − a2, c2 − b2, and d2 − c2 are equal. One possibility is that the
arithmetic progression is constant: a2, a2, a2, a2. Are there arithmetic progressions of four
rational squares that are not constant? This question was ﬁrst raised by Fermat in 1640.
There are no such progressions with small rational squares, but that doesn’t preclude the
possibility of a rational solution altogether. After all, the smallest positive integer solution
to x2 − 61y2 = 1 is (x, y) = (1766319049, 226153980).
We will show how to turn 4-tuples of real numbers (not all 0) whose squares form an
arithmetic progression into points on the elliptic curve

(1.1) y2 = (x − 1)(x2 − 4).

A brief check reveals 8 rational points of the homogenized projective curve: [0, 1, 0] and

(1.2) (1, 0), (2, 0), (−2, 0), (0, 2), (0, −2), (4, 6), (4, −6).

We will see that whether or not there is a nonconstant 4-term arithmetic progression of
rational squares is equivalent to the existence of an additional rational point on this curve.
To turn four squares in arithmetic progression into points on (1.1), the main idea is to let
geometry dictate the right changes of variables. This is carried out in Section 2. In Section
3 we will apply theorems about elliptic curves over Q to ﬁnd all rational points on (1.1)
and thus all arithmetic progressions of four rational squares.

2. Geometric Considerations

To say a2, b2, c2, and d2 are in an arithmetic progression means b2 − a2 = c2 − b2 and
c2 − b2 = d2 − c2. We write these conditions as

(2.1) a
2 + c
2 = 2b
2, b
2 + d
2 = 2c
2.

These equations are homogeneous, so we will consider a, b, c, and d as a point [a, b, c, d] in
P3(R).
Each equation in (2.1), considered separately, cuts out a surface in P3(R). The eight
points [±1, ±1, ±1, 1], with independent choices of sign, lie on both surfaces. (There are not
16 points if we allow an independent sign in the last coordinate, since we are working pro-
jectively, e.g., [1, −1, 1, −1] = [−1, 1, −1, 1].) Finding common solutions to both equations
in (2.1) means looking at the intersection of the two surfaces, which will be a curve. Call it
C. Rational points on C are what we are interested in, since they will tell us the 4-tuples
of rational numbers whose squares are in arithmetic progression.
To ﬁnd an equation for C itself, so we can study its rational points, we will project C
into the projective plane {[a, b, c, 0]} and work in this plane. We of course need to be sure
that our projection is one-to-one on C so no information is lost. For instance, projecting
1

2 KEITH CONRAD

C to the plane {[a, b, c, 0]} in the simple-minded way by [a, b, c, d] ↦→ [a, b, c, 0], which is
projection from the point [0, 0, 0, 1], will be 2-to-1 on C since [a, b, c, ±d] both go to the
same point. That’s no good! We will be more careful by projecting into the plane from a
point already on C; lines through the point will turn out to meet C in at most one other
point. Diﬀerent points on C will have diﬀerent projections into the plane.
Set P := [1, 1, 1, 1], Π := {[a, b, c, 0]} ⊂ P3(R).
Let f : P3(R) − P → Π by f (Q) = P Q ∩ Π. So f (Q) is the point on the line P Q that lies
in the plane Π. To ﬁnd an explicit formula for f (Q), write Q = [a, b, c, d]. The line P Q is

P Q = {[λ + µa, λ + µb, λ + µc, λ + µd] : [λ, µ] ∈ P1(R)}.

This line meets Π when λ + µd = 0, so λ = −µd. Thus

f (Q) = [µ(a − d), µ(b − d), µ(c − d), 0] = [a − d, b − d, c − d, 0].

We are interested in f not on all of P3(R) − P , but speciﬁcally on C, which includes P
too. What should f (P ) mean? There is no line P P , but we will use the tangent line to C
at P . What is this line and where does it meet Π? The tangent planes of the two surfaces
in (2.1) at P are given by a + c = 2b, b + d = 2c.
These planes overlap in {[a, b, −a + 2b, −2a + 3b] : [a, b] ∈ P1(R)}, so this is the tangent
line to C at P . This line meets Π where −2a + 3b = 0, so the intersection point is
[a, (2/3)a, (1/3)a, 0] = [3, 2, 1, 0]. Thus, we deﬁne f : C → Π by

(2.2) f ([a, b, c, d]) =
 {
[a − d, b − d, c − d, 0], if [a, b, c, d] ̸= [1, 1, 1, 1],
[3, 2, 1, 0], if [a, b, c, d] = [1, 1, 1, 1].

Table 1 gives the projection to Π of the 8 obvious rational points on C. Note the
coordinates of f (Q) are only determined up to an overall scaling. For instance, (2.2) says
f ([−1, 1, 1, 1]) = [−2, 0, 0, 0], which appears in Table 1 as [1, 0, 0, 0].

Q f (Q)
[1, 1, 1, 1] [3, 2, 1, 0]
[−1, 1, 1, 1] [1, 0, 0, 0]
[1, −1, 1, 1] [0, 1, 0, 0]
[1, 1, −1, 1] [0, 0, 1, 0]
[−1, −1, 1, 1] [1, 1, 0, 0]
[1, −1, −1, 1] [0, 1, 1, 0]
[−1, 1, −1, 1] [1, 0, 1, 0]
[−1, −1, −1, 1] [1, 1, 1, 0]
Table 1.

Remark 2.1. The formula for f is not discontinuous at P . Indeed, let’s pick a sequence
of points on C tending to P and see their f -values tend to [3, 2, 1, 0]. To keep the algebra
simple, for any ε let Pε be a point on C with coordinates d = 1 and c = 1+ε. The coordinates
a and b are determined (up to sign) by the equations in (2.1). Choosing positive square
roots, we take Pε = [
√1 + 6ε + 3ε2, √
1 + 4ε + 2ε2, 1 + ε, 1].

ARITHMETIC PROGRESSIONS OF FOUR SQUARES 3

Then P0 = P and for ε ̸= 0, (2.2) says

f (Pε) = [
√
1 + 6ε + 3ε2 − 1, √
1 + 4ε + 2ε2 − 1, ε, 0].

To understand the behavior of f (Pε) as ε → 0 (the limit is not [0, 0, 0, 0]!), scale the third
coordinate to 1:
 f (Pε) =
 [ √1 + 6ε + 3ε2 − 1
ε ,
 √1 + 4ε + 2ε2 − 1
ε , 1, 0

]
 .

Letting ε → 0, a derivative calculation shows the limit is [3, 2, 1, 0].

We want to ﬁnd an equation for f (C) in the plane Π. Considering the formula for f in
(2.2) away from P , when [a, b, c, d] ̸= [1, 1, 1, 1] set

(2.3) u = a − d, v = b − d, w = c − d,

so a = u + d, b = v + d, and c = w + d. Using this, (2.1) becomes

(u + d)
2 + (w + d)2 = 2(v + d)
2, (v + d)2 + d
2 = 2(v + d)
2.

Expanding the squares and collecting like terms,

(2.4) u
2 − 2v2 + w2 = −2d(u − 2v + w), v2 − 2w2 = −2d(v − 2w).

We can eliminate d by multiplying the ﬁrst equation by v − 2w, the second equation by
u − 2v + w, and then equating the left sides:

(v − 2w)(u
2 − 2v2 + w2) = (v2 − 2w2)(u − 2v + w).

After multiplying out both sides and moving everything to one side, this equation becomes

(2.5) uv2 − u
2v + 2u
2w − 2uw2 − 3v2w + 3vw2 = 0.

We should check that the elimination of d is reversible: is d determined by u, v, and w in
one of the equations in (2.4)? Yes, provided either u − 2v + w or v − 2w is nonzero. Could
u − 2v + w and v − 2w both vanish? If v − 2w = 0, then the second equation in (2.4) implies
4w2 − 2w2 = 0, so w = 0 and thus v = 0. In terms of b, c, and d this means b = c = d.
The ﬁrst equation in (2.4) becomes u2 = −2du, so either u = 0 or u = −2d, which implies
a = d or a = −d, respectively. Therefore a point [a, b, c, d] where v − 2w vanishes must be
[±d, d, d, d] = [±1, 1, 1, 1], and if also u − 2v + w vanishes the point is [1, 1, 1, 1] = P . So
as long as we are looking at projections of points Q = [a, b, c, d] on C other than P , d is
determined by f (Q) = [u, v, w]. If Q ̸= P then f (Q) ̸= [3, 2, 1], and [3, 2, 1] satisﬁes (2.5),
so f (C) is the set of points [u, v, w, 0] in P3(R) satisfying (2.5).
All points in f (C) have ﬁnal coordinate 0, so we may as well just ignore this last coordi-
nate: identify Π with P2(R) by [u, v, w, 0] ↔ [u, v, w]. The equation (2.5) deﬁnes a smooth
cubic curve in P2(R), and it does have rational points on it: the second column of Table 1
provides 8 of them when we drop the last coordinate 0 from those points.
In order to write (2.5) in the (aﬃne) form y2 = cubic in x, we need to ﬁnd a point on
(2.5) whose tangent line to the curve passes through no other point on the curve. Then a
linear change of variables [u, v, w] ↦→ [x, y, z] that moves that point to [0, 1, 0] and moves
its tangent line to the line z = 0 in P2(R) will give us a simpler equation for (2.5). But
watch out! Even though the point [0, 1, 0] is already on the curve (2.5), its tangent line is
u = 3w, which meets the curve in another point, [3, 2, 1]. So a linear change of variables
[u, v, w] ↦→ [x, y, z] that ﬁxes [0, 1, 0] and makes its tangent line z = 0 will move [3, 2, 1] to

4 KEITH CONRAD

this line, which means the new equation for the curve has two solutions on the line z = 0,
so the curve won’t have the (aﬃne) equation y2 = cubic in x.
In Table 2 are the tangent lines to (2.5) at all 8 points we already know.

[u, v, w] Tangent Line
[3, 2, 1] u − 3v + 3w = 0
[1, 0, 0] v − 2w = 0
[0, 1, 0] u − 3w = 0
[0, 0, 1] 2u − 3w = 0
[1, 1, 0] u − v + w = 0
[0, 1, 1] u + 3v − 3w = 0
[1, 0, 1] u + v − w = 0
[1, 1, 1] u − 2v + 3w = 0
Table 2.

An inspection shows the tangents at [3, 2, 1], [1, 1, 0], and [1, 0, 1] pass through [0, 1, 1]
and the tangents at [1, 0, 0], [0, 1, 0], [0, 0, 1], and [1, 1, 1] pass through [3, 2, 1]. Among the
8 points in Table 2, only [0, 1, 1] has a tangent line that contains no other point on (2.5).
(Indeed, if you set u = 3w − 3v in (2.5) the equation simpliﬁes to 12(v − w)3 = 0, so v = w
and thus [u, v, w] = [0, v, v] = [0, 1, 1].) A linear change of variables [u, v, w] ↦→ [X, Y, Z]
that turns [0, 1, 1] into [0, 1, 0] and the line u + 3v − 3w = 0 into the line Z = 0 is

(2.6) X = u, Y = v, Z = u + 3v − 3w.

The new coordinates of our 8 points are in Table 3. (For instance, when [u, v, w] = [0, 0, 1]
we get [X, Y, Z] = [0, 0, −3] = [0, 0, 1].)

[u, v, w] [X, Y, Z]
[3, 2, 1] [3, 2, 6]
[1, 0, 0] [1, 0, 1]
[0, 1, 0] [0, 1, 3]
[0, 0, 1] [0, 0, 1]
[1, 1, 0] [1, 1, 4]
[0, 1, 1] [0, 1, 0]
[1, 0, 1] [1, 0, −2]
[1, 1, 1] [1, 1, 1]
Table 3.

Inverting (2.6),
 u = X, v = Y, w = 1
3 (X + 3Y − Z),

and substitution of this into (2.5) turns the equation into

(2.7) 9Y 2Z − 3Y Z2 − 6XY Z − 4X 3 + 2X 2Z + 2XZ2 = 0.

Remark 2.2. The tangent line to the original curve C at P = [1, 1, 1, 1] meets C at no
point other than P itself, but after projection to the plane Π, the tangent line to f (C) at
f (P ) (in Π) meets f (C) at a second point. It is not really a surprise that projecting into

ARITHMETIC PROGRESSIONS OF FOUR SQUARES 5

a lower-dimensional space can introduce extra intersections, but in fact there is something
more going on: the projection of the tangent line to C at P under f is not the tangent
line to f (C) at f (P ). Indeed, the whole tangent line to C at P gets projected onto the
single point f (P ). (Similarly, each line through P – not just the tangent line to C –
gets projected from P to a single point in Π.) For each Q ̸= P in Table 1, the relation
between projection and tangency is better: the projection f of the tangent line to C at Q
is the tangent line to f (C) at f (Q). For example, the tangent line to C at [−1, 1, 1, 1] is
{[a, b, a + 2b, 2a + 3b] : [a, b] ∈ P1(R)} and the image of this line under f is the line v = 2w,
which is listed in Table 2 as the tangent line to (2.5) at f ([−1, 1, 1, 1]) = [1, 0, 0] (dropping
the fourth coordinate 0).

We want to massage (2.7) further so Y only occurs once in the equation. At this point
the geometry ends and grinding algebra takes over. To make the algebra easier to follow,
let’s pass to the aﬃne form of (2.7) with Z = 1:

9Y 2 − 3Y − 6XY − 4X 3 + 2X 2 + 2X = 0.

Put the Y -free terms on the right:

9Y 2 − 3Y (1 + 2X) = 4X 3 − 2X 2 − 2X.

Complete the square on the left:
(3Y − 1 + 2X
2
 )2 − ( 1 + 2X
2
 )2 = 4X 3 − 2X 2 − 2X.

Bring the second term on the left over to the other side:
(
3Y − 1 + 2X
2
 )2 = 4X 3 − X 2 − X + 1
4 .

Multiply through by 4 to clear the denominator:

(6Y − 2X − 1)
2 = 16X 3 − 4X 2 − 4X + 1.

Multiply by 4 (again) to absorb the power of 2 everywhere:

(12Y − 4X − 2)
2 = (4X)3 − (4X)2 − 4(4X) + 4.

In homogeneous form, this is

(12Y − 4X − 2Z)2Z = (4X)3 − (4X)2Z − 4(4X)Z2 + 4Z3.

This equation tells us to make a ﬁnal change of variables:

(2.8) x = 4X, y = 12Y − 4X − 2Z, z = Z.

The equation of the curve is
 y2z = x3 − x
2z − 4xz2 + 4z3,

or

(2.9) y2 = x
3 − x2 − 4x + 4

in aﬃne form. (The cubic polynomial in x factors as (x − 1)(x2 − 4), thus recovering (1.1).)
Table 4 records the ﬁnal set of coordinates of the 8 points. The 7 points in the last column
of the table other than [0, 1, 0] are precisely the points listed in (1.2).
We have proved the following theorem.

6 KEITH CONRAD

[a, b, c, d] [u, v, w] [X, Y, Z] [x, y, z]
[1, 1, 1, 1] [3, 2, 1] [3, 2, 6] [2, 0, 1]
[−1, 1, 1, 1] [1, 0, 0] [1, 0, 1] [4, −6, 1]
[1, −1, 1, 1] [0, 1, 0] [0, 1, 3] [0, 2, 1]
[1, 1, −1, 1] [0, 0, 1] [0, 0, 1] [0, −2, 1]
[−1, −1, 1, 1] [1, 1, 0] [1, 1, 4] [1, 0, 1]
[1, −1, −1, 1] [0, 1, 1] [0, 1, 0] [0, 1, 0]
[−1, 1, −1, 1] [1, 0, 1] [1, 0, −2] [−2, 0, 1]
[−1, −1, −1, 1] [1, 1, 1] [1, 1, 1] [4, 6, 1]
Table 4.

Theorem 2.3. The 4-tuples [a, b, c, d] ∈ P3(R) such that a2, b2, c2, d2 form an arithmetic
progression are parametrized by the points on the elliptic curve

E : y2 = x3 − x2 − 4x + 4.

A formula for [x, y, z] in terms of [a, b, c, d] is obtained by composing the changes of
variables (2.3), (2.6), and (2.8): for any [a, b, c, d] ̸= [1, 1, 1, 1],

(2.10) [x, y, z] = [4(a − d), −6(a − b − c + d), a + 3b − 3c − d],

while for [a, b, c, d] = [1, 1, 1, 1] we use [x, y, z] = [2, 0, 1]. For the reverse mapping from
[x, y, z] to [a, b, c, d], if [x, y, z] ̸= [2, 0, 1] then use (2.8) to deﬁne X, Y, Z, use (2.6) to deﬁne
u, v, w, use either equation in (2.4) to deﬁne d (the second equation can be used unless
v = 2w, which only happens for [x, y, z] = [2, 0, 1] or [4, −6, 1]) and ﬁnally use (2.3) to
deﬁne a, b, and c by

(2.11) a = d + u = d + x
4 , b = d + v = d + x + y + 2z
12 , c = d + w = d + 2x + y − 2z
12 .

If [x, y, z] = [2, 0, 1] then set [a, b, c, d] = [1, 1, 1, 1].
From the formulas, [x, y, z] is a rational point if and only if [a, b, c, d] is a rational point, so
rational 4-tuples besides (0, 0, 0, 0) whose squares are in arithmetic progression correspond
to rational points on E. Looking at the ﬁrst and last columns of Table 4, the eight rational
points in the last column of Table 4 correspond to 4-tuples whose squares form a constant
arithmetic progression (common diﬀerence 0), allowing for sign changes in the four numbers
before they are squared. To ﬁnd a nonconstant arithmetic progression of 4 rational squares
is equivalent to ﬁnding another rational point on E.

3. Rational Points on E

The eight rational points we identiﬁed already in E(Q) are all torsion points. More
precisely, these points form a group of size 8 generated by (0, 2) (of order 4) and (1, 0) (of
order 2). Table 5 expresses each of the seven non-identity points in terms of the chosen
generators.
 P 2P 3P Q P + Q 2P + Q 3P + Q
(0, 2) (2, 0) (0, −2) (1, 0) (4, 6) (−2, 0) (4, −6)
Table 5. Torsion on E(Q)

ARITHMETIC PROGRESSIONS OF FOUR SQUARES 7

Theorem 3.1. The eight points found already in E(Q) form its full torsion subgroup.

Proof. We give two proofs, ﬁrst using Nagell-Lutz and then using reduction mod p.
To use the Nagell-Lutz theorem, we rewrite the Weierstrass equation (2.9) for E in the
form y′2 = x′3 + Ax′ + B. Taking x = (x′ + 3)/9 and y = y′/27, we obtain from (2.9) the
new equation
 y′2 = x′3 − 351x′ + 1890
= (x′ − 6)(x′ − 15)(x′ + 21).

Here 4A3 + 27B2 = −24 · 314, so if (x′, y′) is a rational torsion point then x′ and y′ are
integers with y′ = 0 or y′ | 22 · 37. When y′ = 0 we have x′ = 6, 15, or −21. When y′ runs
through the 24 positive factors of 22 · 37, only y′ = 54 and y′ = 162 produce a corresponding
integral x′. The results, and the conversion back to x, y coordinates, are in Table 6. We
recover the known torsion points and nothing further.

(x′, y′) (x, y)
(6, 0) (1, 0)
(15, 0) (2, 0)
(−21, 0) (−2, 0)
(−3, 54) (0, 2)
(−3, −54) (0, −2)
(33, 162) (4, 6)
(33, −162) (4, −6)
Table 6. Checking Nagell-Lutz

For the second proof of the theorem, consider reduction E(Q) → E(Fp). The discrim-
inant of the cubic is divisible only by the primes 2 and 3, so reduction is injective on the
torsion subgroup of E(Q) when p > 3. A calculation shows E(F5) has size 8, and we already
have 8 torsion points, so the points we found in E(Q) are its full torsion subgroup. □

Remark 3.2. The Nagell-Lutz theorem is true for Weierstrass equations y2 = x3 + ax2 +
bx + c where the coeﬃcients are all integers (a need not be 0). A torsion point (x, y) has
integer coordinates and y = 0 or y2 | ∆, where

∆ = 4b
3 + 27c
2 − a
2b
2 + 4a3c − 18abc.

(When a = 0 this reduces to the usual formula for the cubic discriminant.) The original
Weierstrass equation (2.9) has this form: a = −1, b = −4, and c = 4, giving ∆ = 144, so
a torsion point (x, y) has y = 0 or y | 12. Running through the factors of 12 as values for
y, we get integral x when y = ±2 and y = ±6. The corresponding points on E are (0, ±2),
and (4, ±6), which are torsion. Allowing y = 0 leads to the rest of the torsion points in
E(Q).

Corollary 3.3. If there is a nonconstant 4-term arithmetic progression of rational squares
then there are inﬁnitely many that are not scalar multiples of each other.

Proof. A nonconstant 4-term arithmetic progression of rational squares leads to a point in
E(Q) besides the 8 known points, which must have inﬁnite order, and we get inﬁnitely
many progressions from those inﬁnitely many rational points. □

8 KEITH CONRAD

Theorem 3.4. A nonconstant 4-term arithmetic progression of rational squares does not
exist.

Proof. We show E(Q) is ﬁnite. This can be done by a descent argument, and that is how
Euler proceeded when he solved this problem in 1780. (He used descent on the pair of
equations (2.1), not on an elliptic curve.) We will instead use Kolyvagin’s theorem: if the
L-function of an elliptic curve over Q is nonzero at s = 1, then the elliptic curve has ﬁnitely
many rational points. For our particular elliptic curve E, PARI says L(E, 1) ≈ .53912, so if
we believe this is even approximately correct then L(E, 1) ̸= 0 and thus E(Q) is ﬁnite. □

While nonconstant 4-term arithmetic progressions of rational squares don’t exist, there
are such progressions in other ﬁelds, and we can ﬁnd them using Theorem 2.3. Indeed, the
proof of Theorem 2.3 applies not just to rational numbers, but to four elements of any ﬁeld
F (not of characteristic 2 or 3)
1 whose squares are in a nonconstant arithmetic progression,
giving a bijection between such 4-tuples as a point in P3(F ) and the points in E(F ).

Example 3.5. Consider the arithmetic progression 0, 1, 2, 3. This is not an arithmetic
progression of rational squares, but it is an arithmetic progression of squares if it is viewed
as 02, 12, √22, √3
2. Starting with [a, b, c, d] = [0, 1, √
2, √3] on C, we obtain by (2.10) the
point [x, y, z] = [−4√3, 6 + 6√2 − 6√3, 3 − 3√2 − √3]
on E. In aﬃne form, this is [x/z, y/z, 1], where
x
z = 4 + 3√2 − 2√3 − √6, y
z = 12 + 9√
2 − 8√3 − 5
√6.

Example 3.6. Let’s go the other way, from a point on E to an arithmetic progression of
4 squares. The point (x, y) = (3, √10) lies on E so it must correspond to an arithmetic
progression of squares in Q(
√10). Setting x = 3, y = √10, and z = 1, we run all the
changes of variables in reverse:

X = 3
4 , Y = 5 + √10
12 , Z = 1

and
 u = 3
4 , v = 5 + √10
12 , w = 4 + √10
12 .

From either equation in (2.4) and some algebra we get d = (−9 + √10)/24. Feeding this
into (2.11),
 a = 9 + √10
24 , b = 1 + 3√10
24 , c = −1 + 3√10
24 , d = −9 + √10
24 .

The numbers a2 > b2 > c2 > d2 are a decreasing arithmetic progression with common
diﬀerence √10/48.
The point (3, √10) has inﬁnite order on E, since its double is (89/40, 273
√10/800), which
doesn’t have coordinates in Z[
√10], so by an analogue of the Nagell-Lutz theorem for elliptic
curves over Q(√10) the double has inﬁnite order and thus the original point has inﬁnite
order as well. Since the group E(Q(
√10)) is inﬁnite, there are inﬁnitely many arithmetic
progressions of 4 squares in Q(
√10) that are not scalar multiples of each other.

1Inverting the changes of variables from [a, b, c, d] to [x, y, z] involves division by 2 and 3, so everything
works as long as 2 and 3 are not 0 in the ﬁeld.

ARITHMETIC PROGRESSIONS OF FOUR SQUARES 9

Example 3.7. The group E(F43) contains the point (3, 15). Performing the changes
of variables in reverse modulo 43 starting from [x, y, z] = [3, 15, 1] produces the point
[a, b, c, d] = [1, 27, 9, 11] in P3(F43), which squares modulo 43 to [1, 41, 38, 35]. These coor-
dinates are an arithmetic progression modulo 43.

Remark 3.8. Modulo 43, 152 = 10, so we can think of 15 mod 43 as a square root of 10. So
working with (3, 15) in E(F43) is like working with (3, √10) in E(Q(√10)). If you replace√10 by 15 everywhere in the formulas for a, b, c, and d in Example 3.6 and then reduce
the resulting fractions modulo 43, you will reproduce the result of Example 3.7.

When p ≥ 5 is prime, the 8 points we have found in E(Q) stay distinct in E(Fp), so there
is a nonconstant arithmetic progression of 4 squares in Fp provided |E(Fp)| > 8. The Hasse
bound | |E(Fp)| − (p + 1)| ≤ 2√p tells us |E(Fp)| > 8 as long as p + 1 − 2
√p > 8, which is
the same as (√p − 1)2 > 8. This holds for p ≥ 17, so in Fp there is a nonconstant arithmetic
progression of 4 squares when p ≥ 17. An explicit check reveals such a progression in F13:
10, 12, 1, 3. There are no nonconstant 4-term arithmetic progressions of squares in Fp for
p ≤ 11 by an examination of squares in Fp for small p.

Appendix A. Geometric Interpretation of Sign Changes

When [a, b, c, d] is a point on C (the common solutions to (2.1)), every [±a, ±b, ±c, ±d]
lies on C. It is interesting to ask what these sign change operations mean in terms of the
group law on C as an elliptic curve. Put more simply, if we transfer these operations over
to E with its Weierstrass equation y2 = x3 − x2 − 4x + 4, what do the operations look
like? Since the coordinates are only deﬁned up to scaling, we may focus on the sign changes
[±a, ±b, ±c, d], where d is ﬁxed.

Theorem A.1. Let [a, b, c, d] ∈ P3 satisfy (2.1) and correspond to the point [x, y, z] on E.
Then
(1) [−a, b, c, d] corresponds to −[x, y, z] + [4, 6, 1],
(2) [a, −b, c, d] corresponds to −[x, y, z] + [0, −2, 1],
(3) [a, b, −c, d] corresponds to −[x, y, z] + [0, 2, 1],
(4) [−a, −b, c, d] corresponds to [x, y, z] + [−2, 0, 1],
(5) [a, −b, −c, d] corresponds to [x, y, z] + [2, 0, 1],
(6) [−a, b, −c, d] corresponds to [x, y, z] + [1, 0, 1],
(7) [−a, −b, −c, d] corresponds to −[x, y, z] + [4, −6, 1].

Proof. We will give two proofs, one a concrete but tedious set of calculations and the other
using general theorems about elliptic curves (and no hard computations at all).
From the sign change operations in (5), (6), and (7) we can get the other sign change
operations by composition: (1) is (7) followed by (5), (2) is (7) followed by (6), (4) is (5)
followed by (6), and (3) is (7) followed by (4). A case-by-case check shows the corresponding
operations on the elliptic curve compose in the same way as the sign changes. (E.g., the sign
change in (1) is (7) followed by (5), while the elliptic curve operation in (1) is (7) followed
by (5).) So it suﬃces to verify (5), (6) and (7).
Here are the formulas on E relevant to (5), (6), and (7):
(a) [x, y, z] + [2, 0, 1] = [2x(x − 2z), −4yz, (x − 2z)2],
(b) [x, y, z] + [1, 0, 1] = [(x − 4z)(x − z), 3yz, (x − z)2],
(c) −[x, y, z] + [4, −6, 1] = [(4x2z + 4xz2 − 8z3 − 12yz2)(x − 4z), −6x3 − 60x2z + 120xz2 +
36xyz, (x − 4z)3].

10 KEITH CONRAD

We see here that formulas for translation by a 2-torsion point are simpler than formulas
for negation and translation by a point of order 4, so it’s preferable to work with more
formulas of the former kind than the latter kind. This is why it’s better to check (5), (6),
and (7) explicitly rather than (1), (2), and (3). (We need to deal with at least one operation
that is not translation since translations never compose to give a non-translation.)
Equation (2.10) gives the coordinates of [x, y, z] in terms of [a, b, c, d] away from [1, 1, 1, 1].
Apply (2.10) to [a, −b, −c, d] instead of to [a, b, c, d] and check the resulting point on E is
[x, y, z] + [2, 0, 1]. This is a tedious calculation left to the reader, and (2.1) is required for
it. This establishes (5). Parts (6) and (7) are established similarly.
For the second proof of the theorem, we replace tedious calculations with ideas. Each of
the seven sign changes is an automorphism of order 2 on P3 that preserves C. The induced
automorphisms of C have order 1 or 2; in fact the order is 2 since [1, 1, 1, 1] gets moved.
The curve C ∼= E is an elliptic curve. What are the automorphisms of order 2 of an elliptic
curve? The elliptic curve E doesn’t have endomorphism ring Z[i] or Z[ζ3] since j(E) ̸= 0 or
1728 (using the Weierstrass equation for E, j(E) = 35152/9), so the only automorphisms of
E that ﬁx the identity element are the identity automorphism and negation. Therefore all
the automorphisms of E (not necessarily ﬁxing the identity element) are translations and
negation followed by translations. A translation P ↦→ P + Q has order 2 only when Q is a
point of order 2, while P ↦→ −P + Q has order 2 for any Q.
Consider the sign change [a, b, c, d] ↦→ [−a, b, c, d] on C. To ﬁgure out what it looks like
on E, let’s see where it sends the identity element. The point [0, 1, 0] on E comes from
[1, −1, −1, 1] on C (see the ﬁrst and last columns of Table 4), which is sent by the sign
change to [−1, −1, −1, 1]. This corresponds to the point [4, 6, 1] on E, so the sign change
on C looks like either [x, y, z] ↦→ [x, y, z] + [4, 6, 1] or [x, y, z] ↦→ −[x, y, z] + [4, 6, 1] on E.
Since the automorphism has order 2 and [4, 6, 1] has order 4, the ﬁrst option is impossible.
Therefore [a, b, c, d] ↦→ [−a, b, c, d] on C corresponds to [x, y, z] ↦→ −[x, y, z] + [4, 6, 1] on E.
The sign changes [a, b, c, d] ↦→ [a, −b, c, d] and [a, b, c, d] ↦→ [a, b, −c, d] send [1, −1, −1, 1]
to [1, 1, −1, 1] and [1, −1, 1, 1], which correspond to [0, −2, 1] and [0, 2, 1]. These points on E,
like [4, 6, 1], have order 4 and therefore the same analysis as above shows the corresponding
automorphisms of E are [x, y, z] ↦→ −[x, y, z] + [0, −2, 1] and [x, y, z] ↦→ −[x, y, z] + [0, 2, 1].
We have established (1), (2), and (3). The rest follow from these by composition. □

It’s amusing to note that while we wanted to avoid as much as possible the operations
P ↦→ −P + Q when dealing with explicit formulas in the ﬁrst proof, it is precisely these
operations that we used in the conceptual second proof because P ↦→ P +Q and P ↦→ −P +Q
have diﬀerent orders when Q is not a 2-torsion point.
