<!-- source: http://multimagie.com/Bremner1.pdf | converted from PDF -->

ACTA ARITHMETICA
LXXXVIII.3 (1999)
 On squares of squares

by

Andrew Bremner (Tempe, Ariz.)

0. There is a long and intriguing history of the subject of magic squares,
squares whose row, column, and diagonal sums are all equal. There has
recently been some interest in whether there can exist a three-by-three magic
square whose nine elements are all perfect squares; the problem seems ﬁrst
to have been raised by LaBar [5]. The answer is of course yes, for example
 52 12 72

72 52 12

12 72 52
 

which is a particular case of the parametrized square
 (m2 + n2)2 (m2 − 2mn − n2)2 (m2 + 2mn − n2)2

(m2 + 2mn − n2)2 (m2 + n2)2 (m2 − 2mn − n2)2

(m2 − 2mn − n2)2 (m2 + 2mn − n2)2 (m2 + n2)2
  .

Martin Gardner [3] has oﬀered $100 for an example of a three-by-three magic
square of squares in which the nine entries are distinct, or for a proof of the
non-existence of such a square. See Sallows [7] for a recent discussion of this
topic, in which is presented (a reﬂection of) the example

(1)
  582 462 1272

942 1132 22

972 822 742
 

which fails to be magic only in that the non-principal diagonal does not have
the common sum (of 1472).
There are two diﬀerent problems that can be posed. The ﬁrst, to ﬁnd
magic squares with as many as possible of the entries being perfect squares;
and the second, to ﬁnd squares with perfect square entries (“squared
squares”) in which as many as possible of the eight row, column, and diag-
onal sums are equal. In this note, we do not treat the ﬁrst problem, other

1991 Mathematics Subject Classiﬁcation: 11G05, 11D25, 11A99.

[289]

290 A. B r e m n e r

than to exhibit the magic square
 3732 2892 5652

360721 4252 232

2052 5272 222121
 

which has seven square entries; it seems that an example with eight distinct
square entries is unknown. See Guy and Nowakowski [4]. For the second
problem, the above example (1) of Sallows gives a squared square with seven
of the eight sums equal. We here extend this example by showing how to
construct parametrized families of squared squares with a similar property,
namely, having all sums equal excepting that of the non-principal diagonal.
(Henceforth, we are only interested in squares having distinct entries, and
will refer to squares with repeated entries as trivial .)
The three smallest squared squares that are found have entries of degree
8, 16, 20 in the parameter, of which we give the ﬁrst two. We ﬁnd just one
example of a magic square in which the entries are from an algebraic number
ﬁeld of odd degree.

1. Any three-by-three magic square of rational numbers has the form

(2)
  a − b a + b + c a − c
a + b − c a a − b + c
a + c a − b − c a + b
 

with a, b, c ∈ Q. The square is trivial (has repeated entries) precisely when

bc(b2 − c2)(b2 − 4c2)(4b2 − c2) = 0.

Suppose that all the entries are perfect squares; then in particular the
three triples {a, a ± c}, {a + b, a + b ± c}, {a − b, a − b ± c} are each triples
of squares. Associate to the above square the elliptic curve

(3) E : y2 = x(x2 − c2).

A point (X, Y ) in E(Q) lies in 2E(Q) if and only if the triple {X, X ± c}
is a triple of rational squares. Accordingly, a − b, a, a + b must all be x-
coordinates of points in 2E(Q). Thus the existence of a magic square of
squares is equivalent to the existence of three points in 2E(Q) with x-
coordinates in arithmetic progression. This observation appears ﬁrst to have
been noticed by Robertson [6], and seems to be a very restrictive condition,
certainly when the rank of E(Q) is small. A small computer search found
very few examples of three points in E(Q) (not 2E(Q)) with x-coordinates
in arithmetic progression. Indeed, the only example found where none of the
three points is a torsion point on E, is the triple

(−528, 26136), (−363, 22869), (−198, 17424)

Squares of squares 291

on the curve
 y2 = x(x2 − 12542)

which has rank 3 over Q.
For a magic square of squares it is necessary and suﬃcient that

a − b = x2P0, a = x2P1, a + b = x2P2

where xP denotes the x-coordinate of P , and P0, P1, P2 ∈ E(Q). Then the
square (2) becomes

(4)
  x2P0 x2P2 + c x2P1 − c
x2P2 − c x2P1 x2P0 + c
x2P1 + c x2P0 − c x2P2
 

with “magic” condition
 x2P2 − x2P1 = x2P1 − x2P0.

The curve E is known to have rational torsion group comprising just the
points of order dividing 2 (see for example Silverman [9]); and observe that
on replacing Pi by Pi + T , where T is a torsion point, the resulting square
is not altered. Put Pi = (xi, yi), so that x2Pi = (x2 + c2)2/(4y2
i ), and (4)
becomes

 (x2 + c2)2

4y2
0
 (x2 + 2cx2 − c2)2

4y2
2
 (x2 − 2cx1 − c2)2

4y2
1
(x2 − 2cx2 − c2)2

4y2
2
 (x2 + c2)2

4y2
1
 (x2 + 2cx0 − c2)2

4y2
0
(x2 + 2cx1 − c2)2

4y2
1
 (x2 − 2cx0 − c2)2

4y2
0
 (x2 + c2)2

4y2
2
 
 .

Equivalently, put (x, y) = (cx, c2y) so that the equation of E takes the
form
 E : cy
2 = x(x
2 − 1);

then the square is

 (x
2 + 1)2

4y2
 (x
2 + 2x2 − 1)2

4y2
 (x
2 − 2x1 − 1)2

4y2
(x
2 − 2x2 − 1)2

4y2
 (x
2 + 1)2

4y2
 (x
2 + 2x0 − 1)2

4y2
(x
2 + 2x1 − 1)2

4y2
 (x
2 − 2x0 − 1)2

4y2
 (x
2 + 1)2

4y2
 
 .

292 A. B r e m n e r

Finally, replace c by x2(x
2 − 1)/y
2, and put x2 = λ, with (x, y) = (X, y2Y ).
The resulting square, on multiplying by 4y2, is

(5)
 
 (X 2
0 + 1)2

Y 2
0 (λ2 + 2λ − 1)2 (X 2
1 − 2X1 − 1)2

Y 2
1

(λ2 − 2λ − 1)2 (X 2
1 + 1)2

Y 2
1
 (X 2
0 + 2X0 − 1)2

Y 2
0
(X 2
1 + 2X1 − 1)2

Y 2
1
 (X 2
0 − 2X0 − 1)2

Y 2
0 (λ2 + 1)2
 

where (Xi, Yi), i = 0, 1, are points on

(6) E : λ(λ2 − 1)Y 2 = X(X 2 − 1).

This square fails to be magic only at the non-principal diagonal; the condi-
tion that it is magic has become

(7) 2 (X 2
1 + 1)2

Y 2
1 − (X 2
0 + 1)2

Y 2
0 = (λ2 + 1)2.

2. We can regard the equation (6) for E as deﬁning an elliptic curve over
Q(λ), obviously possessing at least one point rational over Q(λ), namely
P = (λ, 1). In fact, it is easy to verify that P is of inﬁnite order, and conse-
quently the multiples of P in E(Q(λ)) can be used to furnish X-coordinates
X0, X1 for substitution into the square at (5), and in this way inﬁnitely
many parametrized squared squares result. As remarked previously, it is
only necessary to compute the multiples of P modulo torsion. Further, it is
clear from (5) that X0, X1, λ must be distinct for non-repeated entries. The
ﬁrst non-trivial square arises from replacing X0 and X1 by

X2P = (1 + λ2)2

4(λ3 − λ) and X3P = λ(3 − 6λ2 − λ4)2

(1 + 6λ2 − 3λ4)2 ,

respectively, and gives rise to a squared square in which the entries are of
degree 48.
The curve E at (6), when viewed as an elliptic ﬁbration, has four singular
ﬁbres above λ = 0, ∞, ±1, each of type I ∗
0 with ﬁve components. It follows
from a formula of Shioda [8] that

rank(E(C(λ))) + 2 + 4 · (5 − 1) ≤ 20

so that rank(E(C(λ))) ≤ 2. But (λ, 1) and (−λ, i) are two independent
points of E, and thus rank(E(C(λ))) = 2. Quite possibly, these two points
generate E(C(λ)), although we have not checked this. In any event, ra-
tional squared squares that arise from multiples of P will seemingly have
parametrizations of degree at least 48.

Squares of squares 293

If we make the replacement

(8) λ = 3s2 + s
s − 1 ,

then the curve E at (6) over Q(s) now has rank 2, with independent points
given by

(9) P0 = ( 3s2 + s
s − 1 , 1)
, P1 = ( 3s2 − s
s + 1 , (s − 1)2

(s + 1)2
 )
.

In order to ﬁnd specializations of λ such that the resulting curve will in
general possess rank at least 2, it is necessary to determine a value of X
other than λ such that the ratio of X 3 −X to λ3 −λ is a perfect square. This
is equivalent to demanding that the ratio of the area of the two Pythagorean
triangles formed from generators {X, 1} and {λ, 1} be a perfect square. It
is apparent that if the Pythagorean triangles formed from generators {p, q}
and {r, s} have areas whose ratio is a square, then (X, λ) = (p/q, r/s) have
the desired property. Bremner [1] investigates the surface

(10) xy(x2 − y2) = zt(z2 − t2)

representing of course the condition that the two primitive Pythagorean
triangles formed from generators {x, y} and {z, t} have equal area. The
table in [1] giving parametrizations of (10) can therefore be used to furnish
several cases where specialization of λ results in a curve E of rank 2. The
example given above at (8), λ = (3s2 + s)/(s − 1), corresponds to the ﬁrst
entry in the table,

(11) (x, y, z, t) = (3s2 + s, s − 1, 3s2 − s, s + 1).

With P0, P1 as at (9), then using the X-coordinates of P0 and of P0 + P1 in
(5), we deduce the following square with entries of degree 8:

(12)
  4(1+2s+2s2−6s3+9s4)2 4(1+4s2−12s3−9s4)2 (1−8s−10s2−24s3+9s4)2

4(1−4s−4s2−9s4)2 (1+22s2+9s4)2 4(1+4s−4s2−9s4)2

(1+8s−10s2+24s3+9s4)2 4(1+4s2+12s3−9s4)2 4(1−2s+2s2+6s3+9s4)2
  .

The condition that the square be magic is that

(13) 1 − 4s2 − 170s4 − 36s6 + 81s8 = 0,

where the polynomial is irreducible over Q.

I am grateful to John Robertson for pointing out the relevant section
(“Right triangles of equal area”) of Dickson [2], where a quadratic parametri-
zation of (10) is ascribed to Hillyer. An equivalent parametrization had in
fact been discovered much earlier by Euler. This parametrization is equiva-
lent to that at (11), so in fact the case can be made that Euler was essentially
aware of this family (12) of squared squares.

294 A. B r e m n e r

Other squares arising from the substitution (8) have degrees 24, 32, 40,
48, . . .
The second entry in the table of [1] corresponds to

(14) λ = −t3 + 4t2 + t
t3 + t + 2
with the curve E possessing the two independent points

(15) P0 = ( −t3 + 4t2 + t
t3 + t + 2 , 1)
,

P1 = ( −t2 + 4t + 1
2t3 − t2 − 1 , (t + 1)2(t2 − t + 2)2

(t − 1)2(2t2 + t + 1)2
 )
.

The square at (5) using the X-coordinates of P0 and of P0 − P1 results in a
square [sij] of degree 16 with the following entries:

s11 = 9(1 − 2t − t2)2(1 + 4t + 8t2 − 6t3 + t4 − 2t5 + 2t6)2,

s12 = 9(1 − 2t − t2)4(2 + 4t + t2 + 2t3 − t4)2,

s13 = (2 + 20t − 23t2 + 20t3 + 74t4 − 20t5 − 23t6 − 20t7 + 2t8)2,
s21 = 9(1 − 2t − t2)2(2 + 4t + 9t2 − 6t4 + 8t5 − t6)2,

s22 = (2 + 2t + 49t2 + 2t3 − 70t4 − 2t5 + 49t6 − 2t7 + 2t8)2,

s23 = 9(1 − 2t − t2)4(1 + 2t − t2 + 4t3 − 2t4)2,

s31 = (2 + 4t + t2 − 10t3 − t4)2(1 − 10t − t2 + 4t3 − 2t4)2,
s32 = 9(1 − 2t − t2)2(1 + 8t + 6t2 − 9t4 + 4t5 − 2t6)2,

s33 = 9(1 − 2t − t2)2(2 + 2t + t2 + 6t3 + 8t4 − 4t5 + t6)2.

Further squares arising from the substitution (14) have degrees 32, 44, 48, . . .
For each parametrization of (10) given in [1], two independent points P0
and P1 on the corresponding curve E are automatically known, and in each
instance we computed the squared squares arising from substituting into (5)
the X-coordinates of two of the points from the set

{c0P0 + c1P1 : 0 ≤ c0 + |c1| ≤ 4}.

(In two instances, an upper bound of 3 rather than 4 was taken, because
the degrees of the points being computed became too large for comfortable
manipulation.) Squares of the following degrees up to 300 were found:

8, 16, 20, 24, 28, 32, 34, 36, 40, 42, 44, 48, 52, 56, 58, 60, 64, 66, 68, 72,
74, 76, 80, 82, 84, 88, 90, 92, 96, 98, 100, 104, 106, 108, 112, 116, 120,
124, 128, 130, 132, 136, 138, 140, 144, 146, 148, 152, 154, 156, 160, 162,
164, 168, 172, 176, 180, 184, 186, 188, 192, 194, 196, 200, 202, 204, 208,
212, 216, 224, 228, 232, 240, 244, 248, 250, 256, 260, 264, 272, 276, 280,
288, 300.
 Squares of squares 295

It seems likely that squared squares exist of every degree d ≥ 16 satisfying
d ≡ 0 mod 4, and that no squared squares exist for degrees d with d ≡
6 mod 8. Further, the list gives examples of squares of degrees d ≡ 2 mod 8
in the range 34 ≤ d ≤ 202 with the exceptions of d = 50, 114, 122, 170, 178;
these latter higher degree examples may be missing simply through not
searching suﬃciently far.

3. For a given squared square constructed in the above manner by substi-
tuting X-coordinates of points on (6) into the square at (5), the property of
being magic implies from (7), under the same substitutions, the vanish-
ing of a polynomial of degree equal to that of the square. Substituting
a root θ of this polynomial into the squared square results in a magic
square with entries lying in the ﬁeld Q(θ). Accordingly, a linear factor re-
sults in a rational magic square. However, it turns out that ﬁnding magic
squares this way in any odd degree extension of the rationals is far from
easy. For each of the squared squares computed above, its associated poly-
nomial determining that the square be magic was factored. The factors
were almost always of even degree, and provided no example of a magic
square in a ﬁeld of degree less than 8, of which we already have an ex-
ample at (12) and (13). In some cases, there do exist factors of odd de-
gree, but in all but one case these lead to trivial squares with repeated
entries. The only example found of a non-trivial magic square with en-
tries in an odd-degree extension of Q arises from the parametrization λ =
(u2 − 1)/(u2 + 2),

P0 = ( u
2 − 1
u2 + 2 , 1), P1 = ( u
2 − 1
2u2 + 1 , u(u2 + 2)2

(2u2 + 1)2
 )

and where the X-coordinates of P0 + P1 and P0 − P1 are substituted into
(5). The resulting square [mij] has entries:

m11 = (1 − u3)2(2 + u)2(1 + 2u)2(10 − 32u + 94u2

− 148u3 + 161u4 − 148u5 + 94u6 − 32u7 + 10u8)2,
m12 = (2 − u)2(1 − u)2(1 + u)2(2 + u)2(1 − 2u)2

× (1 + 2u)2(1 − u + u2)2(1 + u + u2)2(−7 − 4u2 + 2u4)2,

m13 = (2 − u)2(1 + u3)2(1 − 2u)2(2 + 40u + 92u2

+ 152u3 + 181u4 + 128u5 + 80u6 + 40u7 + 14u8)2,
m21 = (2 − u)2(1 − u)2(1 + u)2(2 + u)2(1 − 2u)2

× (1 + 2u)2(1 − u + u2)2(1 + u + u2)2(−1 + 8u2 + 2u4)2,

m22 = (2 − u)2(1 + u3)2(1 − 2u)2(10 + 32u + 94u2

+ 148u3 + 161u4 + 148u5 + 94u6 + 32u7 + 10u8)2,

296 A. B r e m n e r

m23 = (1 − u3)2(2 + u)2(1 + 2u)2(14 − 40u + 80u2

− 128u3 + 181u4 − 152u5 + 92u6 − 40u7 + 2u8)2,

m31 = (2 − u)2(1 + u3)2(1 − 2u)2(14 + 40u + 80u2

+ 128u3 + 181u4 + 152u5 + 92u6 + 40u7 + 2u8)2,
m32 = (1 − u3)2(2 + u)2(1 + 2u)2(2 − 40u + 92u2

− 152u3 + 181u4 − 128u5 + 80u6 − 40u7 + 14u8)2,

m33 = (2 − u)2(1 − u3)2(1 + u3)2

× (2 + u)2(1 − 2u)2(1 + 2u)2(5 + 2u2 + 2u4)2

and is magic in the ﬁeld Q(u) of degree 27 over Q, where

−1680 − 5196u + 6768u2 + 14545u3 + 63864u4 + 29940u5 + 240u6 − 17076u7

− 259740u8 − 222115u9 − 802332u10 − 330012u11 − 1202886u12

− 343440u13 − 802332u14 − 202224u15 − 259740u16 − 28872u17

+ 240u18 + 36048u19 + 63864u20 + 7808u21 + 6768u22 − 1536u23

− 1680u24 − 816u25 + 64u27 = 0.

The smallest degree extension of Q in which we know an example of a
magic square of squares has degree 4:
 (5 − 13√
3)2 (17 + 9√
3)2 (22 − 4√
3)2

(23 − √
3)2 133 · 22 (23 + √
3)2

(22 + 4√
3)2 (17 − 9√
3)2 (5 + 13√
3)2
 

over the ﬁeld Q(√

3, √
133); or indeed, the family
 (µ2 + 1)2 −(µ2 + 2µ − 1)2 4(µ3 − µ)
−(µ2 − 2µ − 1)2 0 (µ2 − 2µ − 1)2

−4(µ3 − µ) (µ2 + 2µ − 1)2 −(µ2 + 1)2
 

over the ﬁeld Q(i, √

µ3 − µ).
 References

[1] A. B r e m n e r, Pythagorean triangles and a quartic surface, J. Reine Angew. Math.
318 (1980), 120–125.
[2] L. E. D i c k s o n, History of the Theory of Numbers, Vol. II, Carnegie Institute, Wash-
ington, 1920.
[3] M. G a r d n e r, The magic of 3 × 3, Quantum, Jan.-Feb. 1996, 24–26.
[4] R. K. G u y and R. J. N o w a k o w s k i, “Monthly” unsolved problems, 1969–1997 ,
Amer. Math. Monthly 104 (1997), 967–973.
[5] M. L a B a r, Problem 270 , College Math. J. 15 (1984), 69.

Squares of squares 297

[6] J. P. R o b e r t s o n, Magic squares of squares, Math. Mag. 69 (1996), 289–293.
[7] L. S a l l o w s, The lost theorem, Math. Intelligencer 19 (1997), no. 4, 51–54.
[8] T. S h i o d a, On elliptic modular surfaces, J. Math. Soc. Japan 24 (1972), 20–59.
[9] J. H. S i l v e r m a n, The Arithmetic of Elliptic Curves, Grad. Texts in Math. 151,
Springer, Berlin, 1994.

Department of Mathematics
Arizona State University
Tempe, Arizona 85287-1804
U.S.A. bremner@asu.edu
 Received on 3.8.1998
and in revised form on 16.11.1998 (3432)
