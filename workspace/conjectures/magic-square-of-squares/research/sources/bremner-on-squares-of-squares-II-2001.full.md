<!-- source: http://www.multimagie.com/Bremner2.pdf | converted from PDF -->

ACTA ARITHMETICA
XCIX.3 (2001)
 On squares of squares II

by

Andrew Bremner (Tempe, AZ)

0. The problem of determining whether there can exist a 3 × 3 magic
square whose entries are perfect squares is an intriguing one, and has been
discussed by several authors, including Bremner [3], Gardner [6], Guy &
Nowakowski [7], LaBar [9], Robertson [10], Sallows [11]. There are two un-
derlying problems. First, to ﬁnd 3×3 squares all of whose entries are square,
and with as many row, column, and diagonal sums as possible being equal.
Second, to ﬁnd 3 × 3 magic squares with as many entries as possible being
perfect squares. The ﬁrst problem was discussed in some detail in Brem-
ner [3], and it is the intention of this current writing to address the second
problem. A 3 × 3 square is said to be trivial if it contains repeated entries;
there apparently is known just one non-trivial magic square (together with
its symmetries) with seven square entries:

 3732 2892 5652

360721 4252 232

2052 5272 222121
 (1) no examples known of non-trivial squares with eight square entries,
unless one extends the ground ﬁeld when there are examples such as:

 (22 + 4√

3 )2 (17 − 9√
3 )2 (5 + 13√
3 )2

(23 − √3 )2 22 · 7 · 19 (23 + √3 )2

(5 − 13√
3 )2 (17 + 9√
3 )2 (22 − 4√
3 )2
 (2)ver the ﬁeld Q(√

3 ).
Demanding that six given entries be square turns out to be equivalent
to studying the intersection of three quadrics in ﬁve-dimensional projective
space. By studying this surface in each of the sixteen ways (up to symme-
try) of selecting six entries from a 3 × 3 square, we show that for each of
these sixteen conﬁgurations there are inﬁnitely many magic squares with the

2000 Mathematics Subject Classiﬁcation: 11G05, 11D25, 14G25, 11A99.

[289]

290 A. Bremner

six entries being perfect squares. This is done by parametrizations in one
variable, so that asking for a seventh entry to be square in these examples
involves ﬁnding rational points on hyperelliptic curves (in general of high
genus) of type f (t) = ✷. But we have been unable to ﬁnd any magic squares
with seven square entries, other than the example at (1).
We further investigate in detail the geometry underlying one of the six-
teen conﬁgurations; and this allows construction of an inﬁnite family of
eight-square magic squares over Q(√3 ), such as (2).

1. Any three-by-three magic square of rational numbers has the form

 a + c −a − b + c b + c

−a + b + c c a − b + c

−b + c a + b + c −a + c
 (3) a, b, c ∈ Q. (In all that follows, a “magic square” will refer to a square
with rational entries, unless speciﬁcally otherwise indicated.) The square (3)
is trivial (has repeated entries) precisely when

ab(a2 − b2)(a2 − 4b2)(4a2 − b2) = 0.

Up to symmetry (rotation and reﬂection), there are precisely sixteen
ways of selecting six entries from a 3 × 3 square. These are as follows:

I II III IV V VI VII VIII

IX X XI XII XIII XIV XV XVI

For each of these sixteen conﬁgurations, it is possible to ﬁnd magic
squares with the six selected entries perfect squares: see Figure 1 (where
we list examples which are believed in each case to have minimum “magic”
sum). We shall show that it is possible to ﬁnd inﬁnitely many parametrized
examples of such squares in each of the sixteen cases I, . . . , XVI. Originally,
it was hoped that squares with seven square entries might be found by ex-
tending a square with six square entries; but of all the examples considered,
and after considerable computing, only the square at (1) arose. (It is worth
noting that Martin Gardner [6] has oﬀered $100 for an example of a non-
trivial nine square entry magic square, or a proof of non-existence of such.)
Duncan Buell [5] has shown by careful search that there is no seven-square

Squares of squares 291

magic square corresponding to the “hour-glass” conﬁguration

in which the central element of the square is less than 25 · 1024.
The demand that each entry at (3) be a perfect square results in nine
equations, which, on eliminating a, b, c, is equivalent to the intersection of six
quadrics in eight-dimensional projective space, a surface. It seems diﬃcult to
deduce properties of this surface of high degree. Recall the notorious problem
of ﬁnding a cubical box with all edges, face diagonals and box diagonal
rational: the corresponding equations are four quadrics in six-dimensional
projective space. Here, we restrict to considering just six entries from (3)
being squares. On eliminating a, b, c there now results the intersection of
three quadrics in P5, and there is some hope of applying to this surface
elementary ideas from geometry. In particular, if the surface is non-singular,
then it is K3 and the methods of Swinnerton-Dyer [16] may be of aid.

2. The arithmetic techniques used to analyze each of the sixteen con-
ﬁgurations are similar, and so detailed attention will be restricted to just a
few cases.
Consider the conﬁguration II, in which

±b + c = ✷, ±a ± b + c = ✷.

Put

a ± b + c = (g ± h)2, −a ± b + c = (r ± s)2, ±b + c = (m ± n)2,

so that a = 1
2 (g2 + h2 − r2 − s2), b/2 = gh = mn = rs,

c = m2 + n2 = 1
2 (g2 + h2 + r2 + s2).

From g/m = n/h = β/γ, say, follows g = αβ, m = αγ, n = βδ, h = γδ with

a = (α2 − δ2)(β2 − γ2), b = 2αβγδ, c = α2γ2 + β2δ2

and α2(−β2 + 2γ2) + 2αβγδ + δ2(2β2 − γ2) = (r + s)2,

α2(−β2 + 2γ2) − 2αβγδ + δ2(2β2 − γ2) = (r − s)2,
(4) is,
 E :
 { α2(2 − λ2) + 2λαδ − δ2(1 − 2λ2) = (ϱ + σ)2,

α2(2 − λ2) − 2λαδ − δ2(1 − 2λ2) = (ϱ − σ)2,
(5) we have put λ = β/γ, ϱ = r/γ, σ = s/γ. Regarded as the intersection
of two quadrics in α, δ, ϱ, σ-space over Q(λ), E represents an elliptic curve

292 A. Bremner

I
 492 1432 1552

1932 1252 −10999

852 10801 28849
 V
 1153 1057 313

12 292 412

372 252 232

II
 1945 12 372

232 1105 412

292 472 265
 VI
 3385 472 7081

892 652 232

372 792 5065

III
 5412 4212 492

−132839 157441 447721

5592 3712 1492
 VII
 889 697 172

52 252 352

312 553 192

IV
 93961 1912 43801

892 2412 3292

2692 79681 1492
 VIII
 1561 312 12

−719 292 492

412 721 112

Fig. 1. The sixteen conﬁgurations of six square entries in a magic square

Squares of squares 293

IX
 2713 673 352

72 1537 552

432 492 192
 XIII
 313 232 412

472 292 −527

12 1153 372

X
 3001 −1679 612

492 412 312

−359 712 192
 XIV
 52 1561 172

889 252 192

312 −311 352

XI
 10585 −1679 1132

972 852 712

412 1272 3865
 XV
 265 12 132

72 145 241

112 172 52

XII
 22009 1192 9265

492 15145 1672

1452 1272 912
 XVI
 372 5089 672

6769 3649 232

532 472 772

Fig. 1 [cont.]

294 A. Bremner

with distinguished point (α, δ, ϱ, σ) = (1, 1, λ, 1). A cubic equation for the
curve is given by

E : T 2 = S(S2 − 4(1 − 3λ2 + λ4)S + 4(1 − λ2)4),

and it is straightforward to verify that (2(1−λ2)2, 4λ(1−λ2)2) is of order 4 in
G = E(Q(λ)), with the torsion subgroup isomorphic to Z/4Z; and the rank
of E over Q(λ) is equal to 1. The point (2(1 + λ)4, 12λ(1 + λ)4) is of inﬁnite
order in G, and likely a generator of the inﬁnite component of G, though this
has not been conﬁrmed. On (5) this point corresponds to P = (1, 1, 1, λ).
The multiples of P on (5) give rise to points (α, δ, ϱ, σ) which in turn give
rise to a, b, c and corresponding magic squares for the conﬁguration II. For
example, −P is equal to

((−5 + λ2)(1 + 7λ2), (1 − 5λ2)(7 + λ2), (1 − 5λ2)(1 + 7λ2), λ(−5 + λ2)(7 + λ2))

with
 a = 24(1 − λ2)2(1 + λ2)(1 − 6λ + λ2)(1 + 6λ + λ2),

b = −2λ(5 − λ2)(1 − 5λ2)(1 + 7λ2)(7 + λ2),

c = (1 + λ2)(5 − 6λ + 5λ2)(5 + 6λ + 5λ2)(1 + 14λ2 + λ4);

and the corresponding square (mij) is
(6)

 ∗ (1+35λ+2λ2 −2λ3 −35λ4 −λ5)2 (5−7λ+34λ2 +34λ3 −7λ4 +5λ5)2

(1−35λ+2λ2 +2λ3 −35λ4 +λ5)2 ∗ (7+5λ−34λ2 +34λ3 −5λ4 −7λ5)2

(5+7λ+34λ2 −34λ3 −7λ4 −5λ5)2 (7−5λ−34λ2 −34λ3 −5λ4 +7λ5)2 ∗
 

where the diagonal entries are

m11 = 49 − 451λ2 + 1426λ4 + 1426λ6 − 451λ8 + 49λ10,
m22 = 25 + 389λ2 + 610λ4 + 610λ6 + 389λ8 + 25λ10,(7) m33 = 1 + 1229λ2 − 206λ4 − 206λ6 + 1229λ8 + λ10.

The magic squares that arise in this way from points Q and Q+T in G for T
torsion, are symmetries of each other; to compute all magic squares arising
from E it is only necessary therefore to consider points Q = mP . One can
even restrict to m > 0; P produces a trivial square, 2P produces (up to
symmetry) the square at (6) with entries of degree 10, and 3P produces a
square with entries of degree 26.
It is possible to achieve a square with entries of degree 8 by means of
the following specialization. Put

(β, γ) = (1 + 2µ + 3µ2, 2µ).

Squares of squares 295

Then (4) takes the form

α2(−1 − 4µ − 2µ2 − 12µ3 − 9µ4) + 4µ(1 + 2µ + 3µ2)αδ
+ 2δ2(1 + 4µ + 8µ2 + 12µ3 + 9µ4) = (r + s)2,
(8) α2(−1 − 4µ − 2µ2 − 12µ3 − 9µ4) − 4µ(1 + 2µ + 3µ2)αδ
+ 2δ2(1 + 4µ + 8µ2 + 12µ3 + 9µ4) = (r − s)2

with point at (α, δ) = (−1 + 3µ2, 1 − 2µ+3µ2). This leads to the magic square
[ ∗ (1 + 4µ2 + 12µ3 − 9µ4)2 (1 − 2µ + 2µ2 + 6µ3 + 9µ4)2

(1 − 4µ − 4µ2 − 9µ4)2 ∗ (1 + 4µ − 4µ2 − 9µ4)2

(1 + 2µ + 2µ2 − 6µ3 + 9µ4)2 (1 + 4µ2 − 12µ3 − 9µ4)2 ∗
 ]

(9) the diagonal entries are

m11 = 1 + 4µ + 8µ2 − 28µ3 − 2µ4 − 84µ5 + 72µ6 + 108µ7 + 81µ8,

m22 = (1 + µ2)(1 + 9µ2)(1 − 2µ2 + 9µ4),

m33 = 1 − 4µ + 8µ2 + 28µ3 − 2µ4 + 84µ5 + 72µ6 − 108µ7 + 81µ8.

(10) curve at (8) has rank 2 over Q(µ) with independent points of inﬁnite
order given by

(1, 1, 1 + 4µ + 3µ2, −1 − 3µ2),
(−1 + 3µ2, 1 − 2µ + 3µ2, 1 − 4µ − 4µ2 − 9µ4, 1 + 4µ2 + 12µ3 + 9µ4)

(where we have chosen (1, 1, 1 + 4µ + 3µ2, 1 + 3µ2) as the zero of the group
of points over Q(µ)). Correspondingly, there arises a two-dimensional fam-
ily of magic squares, with those of smaller degree having entries of degree
8, 10, 12, 16, 20, . . .

Remark. From (10), the square at (9) has m22 a perfect square pro-
vided the curve (1 + X)(1 + 9X)(1 − 2X + 9X 2) = ✷ has rational points
with X = µ2. But this elliptic curve of conductor 48 has rank 0, forcing
µ = 0 and a consequent trivial square. For m11 or m33 to be square, the
condition is that the curve of genus 3 given by 1 + 4x + 8x2 − 28x3 − 2x4 −
84x5 + 72x6 + 108x7 + 81x8 = ✷ have rational points. The curve does of
course have only ﬁnitely many rational points; it seems likely that x = 0, ∞
are the only such, though we are unable to show this. The curve contains
in its Jacobian the elliptic curve U 4 + 4U 3 − 4U 2 − 64U − 32 = ✷ (observe
the transformation U = 3x + 1/x), of conductor 1104 and rank 1, with
(−2, 8) a generator for the rational points. But computing the “small” ra-
tional points on this curve led to no non-trivial rational points on the curve
of genus 3.
Each of the sixteen conﬁgurations I–XVI may be treated as in the above
example for Category II. In each case it is straightforward to determine an
elliptic ﬁbration of the associated surface intersection of the three quadratic

296 A. Bremner

forms. To shorten the labour, observe that there is a correspondence between
squares of type II and squares of type XIII, namely

m11 B C

D m22 F

G H m33
 ←→
 n11 D F

H G n23

B n32 C

with m11 = (F + H)/2, n11 = B − D + G,

m22 = (C + G)/2, n23 = B + F − H,

m33 = (B + D)/2, n32 = F + G − C.

Similarly, there is a correspondence between squares of type VII and XIV:

m11 m12 C

D E F

G m32 I
 ←→
 D n12 C

n21 E I

G n32 F

with m11 = E + F − G, n12 = −D + F + I,

m12 = −C + D + G, n21 = C − E + F,

m32 = C + F − G, n32 = C − G + I.

It can also be noted that squares in Category VII occur in pairs:

· · C

D E F

G · I
 ←→
 · · F

G E C

D · I

as do squares in Category XIII:

· B C

D E ·

G · I
 ←→
 · G D

C I ·

B · E
 .

We ﬁnd in this manner parametrizations for the squares in Categories
I–XVI of respective degrees 12, 8, 12, 20, 12, 12, 12, 20, 20, 12, 20, 20, 8,
12, 20, 12 (but do not claim in any particular Category to have found the
parametrization of smallest degree). For reasons of space, these parametriza-
tions are not listed here, but are available to interested parties from the
author.
 Squares of squares 297

Finally we consider one further example, squares of type VII. Here

±b + c = ✷, ±(a − b) + c = ✷, −a + c = ✷, c = ✷

and putting

c = m2 + n2 = r2 + s2 = u2, b = 2mn, a − b = 2rs, a = u2 − v2,

we have m
2 + n2 = r2 + s2 = u2, u2 − v2 = 2mn + 2rs.

With
 m = αβ + γδ, n = αγ − βδ, r = αγ + βδ, s = αβ − γδ

we obtain (α2 + δ2)(β2 + γ2) = u2,

α2(β2 − 4βγ + γ2) + δ2(β2 + 4βγ + γ2) = v2,

that is,
 F :
 { (α2 + δ2)(1 + λ2) = ϱ2,

α2(1 − 4λ + λ2) + δ2(1 + 4λ + λ2) = σ2,
(11) we have put λ = β/γ, ϱ = u/γ, σ = v/γ. As a curve in α, δ, ϱ, σ-space
over Q(λ), (11) is an elliptic curve with distinguished point (α, δ, ϱ, σ) =
(λ, 1, 1 + λ2, 1 + 2λ − λ2). The Q(λ)-rank turns out to equal 2, with in-
dependent points of inﬁnite order R = (1, λ, 1 + λ2, 1 − 2λ − λ2), S =
(1, −λ, 1 + λ2, 1 − 2λ − λ2). Then −S has

(α, δ) = (1 + 4λ + 2λ2 + 4λ3 − 3λ4, λ(3 + 4λ − 2λ2 + 4λ3 − λ4))

leading to the square

 ∗ ∗ (1+λ2)2(1+8λ+6λ2 −8λ3 +λ4)2

(1+6λ+5λ2 +4λ3 −5λ4 +6λ5 −λ6)2 (1+λ2)2(1+4λ+6λ2 −4λ3 +λ4)2 (1+2λ−λ2)2(1+6λ2 +λ4)2

(1+λ2)2(1−10λ2 +λ4)2 ∗ (1+2λ−3λ2 +12λ3 +3λ4 +2λ5 −λ6)2


where the non-square entries are

m11 = (1 + 2λ − λ2)(1 + 10λ + 43λ2 + 24λ3 + 58λ4 + 60λ5 − 58λ6

+ 24λ7 − 43λ8 + 10λ9 − λ10),
m12 = (1 − 10λ + 5λ2 − 12λ3 − 5λ4 + 6λ5 − λ6)
× (1 + 6λ + 5λ2 − 12λ3 − 5λ4 − 10λ5 − λ6),
m32 = (1 + 2λ − λ2)(1 + 18λ + 75λ2 + 24λ3 + 90λ4 + 44λ5 − 90λ6

+ 24λ7 − 75λ8 + 18λ9 − λ10).

Computing “small” combinations of R, S on F leads to squares with entries
of degree 12, 20, 28, . . .

298 A. Bremner

The ﬁrst equation at (11) may be parametrized by

α : δ : ϱ = λ(p2 − q2) + 2pq : (p2 − q2) − 2λpq : (λ2 + 1)(p2 + q2)

and then the second equation at (11) demands

(12) (1+2λ−λ2)2p4 −32λ2p3q +2(1−12λ+2λ2 +12λ3 +λ4)p2q2 +32λ2pq3

+ (1 + 2λ − λ2)2q4 = ✷.

The conditions that the remaining three entries in this Category VII square
be perfect squares have become:

(1 − 2λ − λ2)2p4 + 32λ2p3q + 2(1 + 12λ + 2λ2 − 12λ3 + λ4)p2q2

− 32λ2pq3 + (1 − 2λ − λ2)2q4 = ✷,
(1+2λ−λ2)2p4 −4(1+10λ2+λ4)p3q+2(1−12λ+2λ2 +12λ3 +λ4)p2q2
(13) + 4(1 + 10λ2 + λ4)pq3 + (1 + 2λ − λ2)2q4 = ✷,
(1−2λ−λ2)2p4 +4(1+10λ2+λ4)p3q+2(1+12λ+2λ2 −12λ3 +λ4)p2q2

− 4(1 + 10λ2 + λ4)pq3 + (1 − 2λ − λ2)2q4 = ✷.

In order to try and ﬁnd a seven-square magic square, (12) was searched for
solutions also satisfying at least one of the equations (13). The only solution
(up to symmetry) occurred at λ = 13 with (p, q) = (9, 2), giving rise to the
square at (1). (By symmetry considerations, it is suﬃcient to search over a
region in which p, q, and n(λ) = numerator(λ), d(λ) = denominator(λ) are
positive; the search covered the region p + q + n(λ) + d(λ) ≤ 1000.)

3. We use geometric techniques to analyze squares in Category III. Here,

±a + c = ✷, ±b + c = ✷, ±(a + b) + c = ✷,

and putting

a = 2T U, b = 2V W, a+b = −2XY, c = T 2+U 2 = V 2+W 2 = X 2+Y 2

there results

S : T 2 + U 2 = V 2 + W 2 = X 2 + Y 2, T U + V W + XY = 0.

This intersection of three quadrics in P5 is the equation of a surface. It is
readily determined to be non-singular, and so S is K3. There is a large
symmetry group on S, with the obvious symmetries (T U ) ↔ (U T ), etc.,
(T U V W ) ↔ (V W T U ), etc., (T U V W XY ) ↔ (V W XY T U ), etc., and sign-
changes (T V X) ↔ (−T − V − X), etc., generating a group of order 384.
There are 24 conics on S, four lying in each of the six hyperplanes T = 0,
U = 0, . . . , Y = 0, and typiﬁed by {T = X, U = −Y, V = 0, W 2 = X 2 +Y 2},
which will be denoted by CT XV , where Crst denotes the conic with r = s,
t = 0. S also contains the 8 complex conics {T = ε1U, V = ε2W, X =
ε3Y, ε1U 2 + ε2W 2 + ε3Y 2 = 0} where εi are square roots of −1. We denote
these conics by Cj1j2j3 with jk = +, − according as εk = i, −i.

Squares of squares 299

There are also 32 straight lines on S, typiﬁed up to symmetry by the
following equations:

L1 : {T + X = V, T − X = −√
3 W, U + Y = W, U − Y = √
3 V }

with parametrization

(14) (T, U, V, W, X, Y ) = (√
3 α, α+2β, √
3 (α+β), −α+β, √
3 β, −2α−β).

Consider now the intersection of S with the hyperplane

U − Y = λ(X + T ).(15)

This cuts out on S the quadrics CU Y V and CU Y W , together with a residual
intersection of degree 4, on which

U + Y = 1
λ (X − T ),

and

Eλ : { (1 + 2λ − λ2)2T 2 − 2(1 − λ4)T X + (1 − 2λ − λ2)2X 2 = 4λ2(V + W )2,

(1 − 2λ − λ2)2T 2 − 2(1 − λ4)T X + (1 + 2λ − λ2)2X 2 = 4λ2(V − W )2.

As the intersection of two quadrics in P3 with distinguished point

Oλ(T, X, V, W ) = (2λ, 0, 1 − λ2, 2λ),

Eλ represents the equation of an elliptic curve over C(λ). The curve is sin-
gular precisely at λ = ±1, ±i, ±√
3, ±1/√
3.
At λ = 1, Eλ decomposes as the sum

E1 : CU XV + CU XW .(16)

Similarly, E−1 : CT Y V + CT Y W .(17)

When λ = i, then Eλ splits as the two conics:

Ei : C−−+ + C−++(18) conjugate decomposition at λ = −i,

E−i : C++− + C+−−.(19)

When λ = √

3, then Eλ splits as the four lines:

(20) E√3 : {T + X = V, T − X = −√
3 W, U + Y = W, U − Y = √
3 V }

+ {T + X = W, T − X = −√3 V, U + Y = V, U − Y = √3 W }

+ {T + X = −W, T − X = √
3 V, U + Y = −V, U − Y = −√3 W }

+ {T + X = −V, T − X = √
3 W, U + Y = −W, U − Y = −√3 V }

with conjugate decomposition at λ = −√3; and at λ = 1/√
3, the decom-
position is again four lines corresponding to the symmetry of S obtained by
changing the signs of U, W, X.

300 A. Bremner

A cubic model for Eλ is given by

τ 2 = σ(σ + (3 − λ2)2)(σ + (1 − 3λ2)2).(21)

The torsion group of Eλ over C(λ) is isomorphic to Z/4Z × Z/2Z generated
by T4(σ, τ ) = (−(3 − λ2)(1 − 3λ2), −2(1 + λ2)(3 − λ2)(1 − 3λ2)) of order 4,
and T2(σ, τ ) = (−(3 − λ2)2, 0) of order 2. These correspond to

T4(T, X, V, W ) = (1 − λ2, 1 + λ2, 1 − λ2, −2λ),

T2(T, X, V, W ) = (1 + λ2, 1 − λ2, 2λ, 1 − λ2).
(22) four singular ﬁbres of Eλ at λ = ±1, ±i are each of Kodaira Type I2,
and of Type I4 at λ = ±√
3, ±1/√
3. Denote the N´eron–Severi group of
the surface S over C by NS(S, C). Then NS(S, C) is a ﬁnitely generated
Z-module, and it follows from Shioda [13] that

rank NS(S, C) = rank Eλ(C(λ)) + 2 + 4 · (2 − 1) + 4 · (4 − 1).

Since the rank of the N´eron–Severi group of a K3-surface cannot exceed 20
(see for example Barth et al. [1]), we have rank Eλ(C(λ)) ≤ 2. Two indepen-
dent points of inﬁnite order are readily found on Eλ, namely

P1(T, X, V, W ) = (1 − λ2, 1 + λ2, 2λ, −1 + λ2),

P2(T, X, V, W ) = (2 − √
3 + λ, 2 − √
3 − λ, (1−√3 )(1+λ), (1−√
3 )(1−λ))

and thus rank Eλ(C(λ)) = 2.

Lemma. Eλ(C(λ)) ≃ Z × Z × Z/4Z × Z/2Z, with respective generators
P1, P2, T4, T2.

Proof. P1, P2 correspond respectively to the points

P1(σ, τ ) = (−(1 + λ2)2, −8λ(1 − λ4)),

P2(σ, τ ) = ((2 + √
3 )(1 − √
3 λ)(√
3 + λ)(2 − √3 − λ)2,

− 2(1 + √
3 )(1 − λ)(1 − √
3 λ)(√
3 + λ)(2 − √
3 − λ)(1 + λ2))

on (21), and it is now straightforward to compute canonical heights by
the formulae of Silverman [14]. There results ̂h(P1) = 1 and ̂h(P2) = 1/2,
̂h(P1 + P2) = 1/2. The canonical height pairing is deﬁned by

⟨P, Q⟩ = 1
2 (̂h(P + Q) − ̂h(P ) − ̂h(Q))

and so the height pairing matrix (⟨Pi, Pj⟩){1≤i≤2, 1≤j≤2} is equal to

H =
 ( 1 −1/2

−1/2 1/2
 )

with det(H) = 1/4. Thus P1, P2 are independent, and by a theorem of
Kuwata [8], P1, P2 generate a subgroup of index at most a power of 2 in
Eλ(C(λ)) modulo torsion. It is not diﬃcult to show directly that P1 + T ,

Squares of squares 301

P2 + T , P1 + P2 + T cannot lie in 2Eλ(C(λ)) for any torsion element T , and
thus P1, P2 generate Eλ(C(λ)) modulo torsion, as required.

To ﬁnd a set of generators for NS(S, C) over Z, we use ideas of Swinner-
ton-Dyer [16], to which article the reader is referred for full details (see
also Bremner [2], [4]) for further applications of these methods). The group
NS(S, C) is spanned over Z by

1. the locus of the point Oλ,
2. the components of the singular ﬁbres in the pencil Eλ,
3. the loci of the generators P1, P2, T4, T2 of the group Eλ(C(λ)).

Now the locus of Oλ as λ varies is the conic CT W X ; the locus of P1 is
the conic CU V Y ; and the locus of P2 is the straight line

L2 : {V − X = U, V + X = −√3 T, W − Y = T, W + Y = √
3 U }.

From (22), the loci of T4, T2 are the conics CT V Y and CW XU respectively.
Together with the components of the singular ﬁbres of Eλ, from (16)–(20),
the following divisors therefore generate NS(S, C) over Z:

CT V Y , CT W X, CT Y V , CT Y W , CU V Y , CU XV , CU XW , CW XU ,(23) C++−, C+−−, C−++, C−−+; L2; the 4 lines at (20) (with symmetries).

The intersection matrix of these 29 divisors is straightforward to write down,
and as expected, has rank 20. By repeatedly discarding a divisor that is a
Z-linear combination of remaining divisors, the following result is obtained.

Theorem. The following 20 divisors generate NS(S, C) over Z: CT V X ,
CU W X , CT W X, CU V X , CT V Y , CV XT , CW Y T , CW XT , CV XU , CU XV , CT Y V ,
CT XV , C+++, L2 (which we denote by Γ1, . . . , Γ14, respectively), and the 6
lines:

(24)
 Γ15 : {T + X = V, T − X = √3 W, U + Y = W, U − Y = √3 V },

Γ16 : {T + X = −V, T − X = √
3 W, U + Y = −W, U − Y = −√3 V },

Γ17 : {T + X = W, T − X = −√
3 V, U + Y = V, U − Y = √3 W },

Γ18 : {T + X = √3 W, T − X = V, U + Y = −√3 V, U − Y = W },

Γ19 : {T + X = −√3 W, T − X = −V, U + Y = √3 V, U − Y = −W },

Γ20 : {T + X = √
3 V, T − X = W, U + Y = −√3 W, U − Y = V }.

Corollary. Denote by NS(S, Q) that subgroup of NS(S, C) which is
deﬁned over Q. Then NS(S, Q) is generated over Z by the twelve divisors
Γ1, . . . , Γ12.

Corollary. Any rational curve on S has even degree.

Remark. This corollary is mildly inconvenient for the following reason.
We are interested in obtaining one-parameter solutions of the equations for
S, which geometrically represent irreducible curves of genus 0 lying on S.

302 A. Bremner

But an irreducible curve of genus 0 of even degree may not in fact actually
be rationally parametrizable.

To any curve Γ deﬁned over Q on S there thus correspond uniquely
determined integers m1, . . . , m12 such that Γ ∼ m1Γ1 + . . . + m12Γ12. The
genus of Γ is a quadratic form in the mi, given by

pa(Γ ) = 1
2 (Γ.Γ ) + 1

where (Γ.Γ ) is the self-intersection number (see Shafarevich [12], p. 5). Fol-
lowing simple algebra, there results

(25) 1
2 deg(Γ )2 − 4(Γ.Γ )

= (m1 + m2 − m3 − m4 − m5 − m6 + m8 + m9 + 2m10)2

+ (m1 + m2 − m3 − m4 − m5 − m6 + m8 + m9 + 2m11 − 2m12)2

+ 2(m1 − m4 − m5 + m6 − m8 − m9 + m10 + m11 − m12)2

+ 2(m1 − m4 − m5 − m6 − m7 + m8 + m9 − m10 − m11 + m12)2

+ 4(m1 − m3)2 + 3(m2 − m3)2 + (m2 − m3 − 2m7)2

+ 4(m2 − m4 + m5)2 + 4m2 + 4(m7 − m8 + m9)2 + 2(m10 − m11 − m12)2.

This is now in a form suitable for machine computation. Given the degree
and self-intersection number of Γ , it is possible to tabulate the ﬁnitely many
sets of integers m1, . . . , m12 that are solutions of (25). In addition, since we
are only interested in irreducible curves Γ , further restrictions are imposed
on the mi by insisting that Γ have non-negative intersection number with
every known curve lying on the surface. In this manner, it is computed ﬁrst
that the only irreducible rational curves on S of degree 2 are the known
conics (which correspond to trivial squares), and second that there are no
irreducible rational curves of degree 4. Of degree 6, there is the curve repre-
sented by the divisor Γ4 + Γ5 + Γ8 + Γ9 − Γ12, together with 96 symmetries.
This sextic is parametrized as follows:

(26) T : U : V : W : X : Y = 2λ(7 + 4λ − λ2)(1 + 2λ − 3λ2 + 2λ3) :

(1 − λ)(5 + 8λ + λ2)(1 + λ + 5λ2 − 3λ3) :

−4(1 + 2λ − λ2)(1 − 2λ − λ2)2 :

3(1 + λ2)(1 + 8λ + 2λ2 − 8λ3 + λ4) :

2(1 + 4λ − 7λ2)(2 + 3λ + 2λ2 − λ3) :

(1 + λ)(1 − 8λ + 5λ2)(3 + 5λ − λ2 + λ3),

and leads to the square with entries

m11 = (5 + 22λ + 57λ2 − 36λ3 − 45λ4 + 38λ5 − λ6)2,

Squares of squares 303

m12 = (1 − 2λ − λ2)2(7 + 20λ + 2λ2 + 4λ3 − 5λ4)2,
m13 = (1 − 32λ − 37λ2 + 48λ3 + 19λ4 + 16λ5 − 7λ6)2,
m31 = (7 + 16λ − 19λ2 + 48λ3 + 37λ4 − 32λ5 − λ6)2,
m32 = (1 + 38λ + 45λ2 − 36λ3 − 57λ4 + 22λ5 − 5λ6)2,
m33 = (1 − 2λ − λ2)2(5 + 4λ − 2λ2 + 20λ3 − 7λ4)2

and middle row elements

m21 = (1 − 2λ − λ2)2

× (1−200λ − 436λ2 + 232λ3 + 94λ4− 88λ5+ 860λ6− 520λ7+ 73λ8),

m22 = (5 − 4λ + λ2)(1 + 4λ + 5λ2)(1 + 18λ2 + λ4)(5 − 6λ2 + 5λ4),

m23 = (7 + 38λ − 9λ2 − 36λ3 + 57λ4 + 22λ5 − 23λ6)

× (7 + 14λ + 15λ2 + 108λ3 − 87λ4 − 2λ5 + λ6).

A search for values of λ making one of these latter three entries square
disclosed only λ = ±1, giving trivial cases.
There are no irreducible rational curves of degree 8 on S, and up to
symmetry just one curve of degree 10, given by the divisor 2Γ1 + 2Γ3 + Γ4 +
Γ6 − 2Γ7 − Γ8 + 2Γ9 + Γ11 − Γ12 with parametrization

(27) T : U : V : W : X : Y =
2(−1+λ)(−2−6λ+λ2)(−2+10λ−11λ2+4λ3)(100−216λ+128λ2−36λ3+λ4) :
(22−6λ+λ2)(−8+18λ−14λ2 +3λ3)(72−220λ+264λ2−152λ3+30λ4+5λ5) :
(14−30λ+17λ2)(−4+10λ−4λ2 +λ3)(112−188λ+104λ2 −16λ3 −8λ4 +λ5) :
2(10 − 18λ + 7λ2)(−6 + 4λ − 3λ2 + λ3)(92 − 264λ + 304λ2 − 156λ3 + 23λ4) :
3(2 − 2λ + λ2)(20 − 40λ + 24λ2 − 4λ3 + λ4)(68 − 264λ + 280λ2 − 84λ3 + 5λ4) :
−8(−2 + λ2)(4 − 6λ + λ2)(−152 + 480λ − 636λ2 + 432λ3 − 150λ4 + 24λ5 + λ6).

There are no irreducible rational curves of degree 12, and, up to symmetry,
6 of degree 14 corresponding to the divisors:

Γ3 − Γ4 + 2Γ5 + Γ6 − Γ7 + 2Γ8 + 2Γ11 + Γ12,

Γ3 − Γ4 − Γ5 + Γ7 + Γ8 + 3Γ10 + 3Γ12,

Γ1 + 3Γ2 + Γ3 + Γ4 − 2Γ5 + 2Γ6 + Γ7 − Γ8 + Γ9,

Γ2 − Γ5 + 3Γ6 + 3Γ9 + Γ11,

−2Γ7 + 2Γ9 + Γ10 + 3Γ11 + 3Γ12,

Γ5 + Γ7 − Γ9 + 3Γ11 + 3Γ12.

It becomes impracticable to compute the zeros of the form (25) for de-
grees greater than 14; and in any event, deciding whether the divisors found
in this way represent irreducible curves becomes increasingly diﬃcult. The
manner in which we have resolved this for the divisors above is as follows.

304 A. Bremner

As in Swinnerton-Dyer [16] it is most useful to introduce non-linear auto-
morphisms of the surface.

Let E denote a pencil of curves on S of genus 1, the general member of
which is irreducible; and let C1, C2 be two curves on S each having precisely
one point of intersection with any member of E. For P a generic point of S,
let EP be that member of E which passes through P , and let P1, P2 be the
points of EP in which C1, C2 intersect EP . Then

P ↦→ P1 + P2 − P,

where the addition is that of the group law on EP , deﬁnes a birational
map of S to itself. Such a map is necessarily biregular (Shafarevich [12],
Chapter VII, Corollary to Theorem 1), and hence gives an automorphism
of S. Moreover, it is clear from the deﬁnition that this automorphism is
actually an involution. The involution certainly interchanges the curves C1,
C2, and preserves each non-singular ﬁbre of E, so by biregularity, actually
preserves every ﬁbre of E. So if the ﬁbre is singular, then the involution
permutes the components of the decomposition, in particular interchanging
the component containing P1 with the component containing P2. Further
information about the action on the N´eron–Severi group is obtained from the
fact that the involution has ﬁxed points on each non-singular ﬁbre (for there
are just four points P satisfying 2P = P1 +P2), and hence, by specialization,
at least one ﬁxed point on every ﬁbre. In general, the components of E
together with C1 and C2 span only a subgroup G of the N´eron–Severi group,
so there is not yet suﬃcient information to determine fully the action of
the involution. However, Bremner [2] shows that the involution actually
must reverse every element of the orthogonal complement (with respect to
intersection) of G in the N´eron–Severi group; and this in general now allows
computation of the action of the involution. Indeed, the parametrizations of
the curves of degrees 6 and 10 above were computed in exactly this way, as
the image of a conic under an involution chosen with appropriate C1, C2.

As an example, we observe that up to symmetry there is on S just one
other elliptic pencil Fλ besides Eλ of degree 4 (put deg(Γ ) = 4 and (Γ.Γ ) = 0
in (25)), with the divisor Γ1 + Γ3. It is the residual intersection of S with
the hyperplane
 T − U + V + W = λX,

after removing the conics CU V X , CU W X . Fλ is singular at λ = ±2√
2, ±1/√
2
(nodal quartics), together with the following decompositions:

F0 : CU V Y + CU W Y , F∞ : CT V X + CT W X,

Squares of squares 305

F1+√
3 : {U − X = −√3 W, U + X = V, T − Y = √
3 V, T + Y = W }

+ {U − X = −√3 V, U + X = W, T − Y = √
3 W, T + Y = V }

+ {T − X = V, T + X = √
3 W, U − Y = −W, U + Y = −√3 V }

+ {T − X = −W, T + X = √3 V, U − Y = −V, U + Y = −√3 W }

with conjugate decomposition at λ = 1−√
3, and symmetric decompositions
at λ = −1 ± √3. Choosing C1, C2 as the conics CW XT , CW Y T respectively,
results in the following involution, where we represent the action by means
of a 12 × 12 matrix on Γ1, . . . , Γ12 as basis:

φ :
 
 0 0 1 0 0 0 0 0 0 0 0 0

0 −1 0 −1 1 0 1 1 0 1 0 1

1 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 −1 0 1 1 0 1 0 1

0 0 0 −1 0 0 1 1 0 1 0 1

0 −1 0 −1 0 1 0 1 1 1 0 1

0 0 0 0 0 0 0 1 0 0 0 0

0 0 0 0 0 0 1 0 0 0 0 0

0 0 0 0 0 0 1 1 −1 0 0 0

0 −1 0 0 1 0 −1 0 1 1 0 0

1 0 1 0 0 0 1 1 0 0 −1 0

0 1 0 0 −1 0 1 0 −1 0 0 1
 

(so φ(Γ1) = Γ3, etc.)
The image of the conic CT W Y (with divisor Γ2 + Γ4 − Γ5) is the sextic
curve with divisor −Γ2 + Γ7 + Γ8 + Γ10 + Γ12, whence the parametrization
(26). Similarly, the sextic Γ1 + Γ4 + Γ6 + Γ8 − Γ11 maps under the involution
to the divisor −Γ1 − Γ2 − Γ4 − Γ5 + Γ6 + Γ7 + Γ8 + Γ9 + 2Γ10 + Γ11 + 2Γ12 of
degree 10, producing the parametrization at (27). The involution may also
be useful in spotting reducibility of a divisor. For example, up to symmetry,
just one divisor arises from (25) of degree 12 and self-intersection −2, namely
−Γ2 + Γ3 − Γ4 + Γ7 + Γ8 + Γ9 + 2Γ10 + 2Γ12. However, under φ, this divisor
maps to the sum of Γ10 and the line pair {U − X = −V , U + X = ∓√
3 W ,
T − Y = −W , T + Y = ±√
3 V }, and accordingly is reducible.
A theorem whose proof was sketched by E. Looijenga (see Sterk [15])
proves that all curves of genus 0 on S are obtainable by possibly repeated
application of a ﬁnite set of automorphisms of the surface to one of a ﬁnite
number of curves of genus 0 on the surface. Swinnerton-Dyer [16] proved
such a theorem for the quartic K3 surface A4 + B4 = C4 + D4 with explicit
determination of the automorphisms (two in number, together with the sym-

306 A. Bremner

metries) and set of base curves comprising the straight line A = C, B = D.
For an explicit such calculation on another quartic surface (contained in the
four-fold x5 + y5 + z5 = u5 + v5 + w5), see Bremner [4]. In similar manner
it should be possible, in principle at least, to construct the relevant sets
of automorphisms and base curves for the surface S. In practice however,
the computation is suﬃciently daunting that it has not been pursued. (We
remark that at least two further automorphisms of S seem to be needed in
order to generate the six curves of degree 14.)

4. We turn ﬁnally to a brief investigation over the ground ﬁeld Q(√
3 ).
The line at (14) corresponds to the square

(28)
  ((1 + √

3 )α + 2β)2 (2α + (1 − √3 )β)2 ((1 − √
3 )α − (1 + √3 )β)2

∗ ∗ ∗

((1 + √
3 )α − (1 − √
3 )β)2 (2α + (1 + √
3 )β)2 ((1 − √3 )α + 2β)2
 

where the middle row elements are

m21 = 4(1 − √

3 )α2 + 4(1 − √
3 )αβ + (1 + √
3 )2β2,

m22 = 4α2 + 4αβ + 4β2,

m23 = 4(1 + √
3 )α2 + 4(1 + √
3 )αβ + (1 − √
3 )2β2.

(29)o achieve two of {m21, m22, m23} being perfect squares in Q(√
3 ) is equiv-
alent to ﬁnding points on an elliptic curve over Q(√
3 ). For example, m21 =
✷, m23 = ✷ demands
{ 4(1 − √
3 )α2 + 4(1 − √
3 )αβ + (1 + √
3 )2β2 = ✷,

4(1 + √
3 )α2 + 4(1 + √
3 )αβ + (1 − √
3 )2β2 = ✷

which is the equation of an elliptic curve having cubic model

Y 2 = X(X 2 + 8X + 4).

This curve is of rank 1 over Q(√
3 ) and has generator of inﬁnite order equal
to P = (−1, √
3 ).
The multiples of P lead to an inﬁnite sequence of squares such as (2).
Points Q and Q′ that diﬀer only by a torsion element lead to symmetries of
the same magic square, and so magic squares that arise in this way come from
the sequence mP , m ∈ Z. For example, P corresponds to (α, β) = (2, −1),
giving a trivial square; 2P corresponds to (α, β) = (4, 9), leading to the
square (2); and 3P corresponds to (α, β) = (2926, −3041), giving the square

 (3156 − 2926√

3 )2 (2811 + 3041√
3 )2 (5967 + 115√
3 )2

(4749 + 2089√
3 )2 22 · 3 · 37 · 43 · 1867 (4749 − 2089√
3 )2

(5967 − 115√
3 )2 (2811 − 3041√
3 )2 (3156 + 2926√
3 )2
  .

Squares of squares 307

The other possibility, that m21 = ✷, m22 = ✷, demands
{ 4(1 − √
3 )α2 + 4(1 − √
3 )αβ + (1 + √
3 )2β2 = ✷,

α2 + αβ + β2 = ✷.

This is the equation of an elliptic curve over Q(√
3 ), with cubic model

Y 2 = X(X 2 + 2X − 2).(30)

This curve is of rank 2 over Q(√
3 ) and has generators of inﬁnite order
equal to P1 = (1, 1), P2 = (−1, √
3 ). A two-dimensional family of magic
squares arises from the pullbacks of combinations of the two generators. For
example, P1 gives rise to

 (23 − 7√

3 )2 (1 − 4√
3 )2 (22 − 3√
3 )2

(2 + 9√3 )2 (7 − 11√
3 )2 577 − 344√
3

(11 − 8√
3 )2 52(2 − 3√3 )2 (1 + 7√3 )2
  ,

P2 to 
 (5 + 3√
3 )2 (5 − 4√
3 )2 (10 − √
3 )2

(10 − 3√
3 )2 (1 − 5√
3 )2 5(5 + 8√
3 )

72 (2 + 5√
3 )2 52(1 − √
3 )2
  ,

P1 + P2 to

 (95 − 17√
3 )2 (205 − 68√
3 )2 (110 − 51√
3 )2

52(26 − 17√
3 )2 (83 − 85√
3 )2 18553 − 6120√
3

52(17 − 20√
3 )2 (34 − 5√
3 )2 72(17 − 15√
3 )2
  ,

and 2P2 to

 (187 − 243√

3 )2 (166 + 203√
3 )2 (353 − 40√
3 )2

(227 + 100√
3 )2 (37 − 233√
3 )2 317(779 − 252√
3 )

(446 − 7√
3 )2 (283 − 180√
3 )2 (163 + 173√
3 )2
  .

None of the squares we computed had the ninth element m23 a perfect
square in Q(√
3 ).

5. As a ﬁnal remark, we observe that non-trivial 4 × 4 magic squares of
squares are not diﬃcult to construct. One such example is the following:

 372 232 212 222

12 182 472 172

382 112 132 332

32 432 22 312
  .

308 A. Bremner

References

[1] W. Barth, C. Peters and A. Van de Ven, Compact Complex Surfaces, Springer, 1984.
[2] A. Bremner, A geometric approach to equal sums of sixth powers, Proc. London
Math. Soc. (3) 43 (1981), 544–581.
[3] —, On squares of squares, Acta Arith. 88 (1999), 289–297.
[4] —, A geometric approach to equal sums of ﬁfth powers, J. Number Theory 13 (1981),
337–354.
[5] D. A. Buell, A search for a magic hourglass, preprint.
[6] M. Gardner, The magic of 3 × 3, Quantum, Jan.-Feb. 1996, 24–26.
[7] R. K. Guy and R. J. Nowakowski, “Monthly” unsolved problems, 1969–1997 , Amer.
Math. Monthly 104 (1997), 967–973.
[8] M. Kuwata, The canonical height and elliptic surfaces, J. Number Theory 36 (1990),
201–211.
[9] M. LaBar, Problem 270 , College Math. J. 15 (1984), 69.
[10] J. P. Robertson, Magic squares of squares, Math. Mag. 69 (1996), 289–293.
[11] L. Sallows, The lost theorem, Math. Intelligencer 19 (1997), 51–54.
[12] I. R. Shafarevich, Algebraic surfaces, Trudy Mat. Inst. Steklov. 75 (1965).
[13] T. Shioda, On elliptic modular surfaces, J. Math. Soc. Japan 24 (1972), 20–59.
[14] J. H. Silverman, Computing heights on elliptic curves, Math. Comp. 51 (1988),
339–358.
[15] H. Sterk, Finiteness results for algebraic K3 surfaces, Math. Z. 189 (1985), 507–513.
[16] H. P. F. Swinnerton-Dyer, Applications of algebraic geometry to number theory, in:
Proc. Sympos. Pure Math. 20, 1969 Number Theory Institute, Amer. Math. Soc.,
Providence, 1971, 1–52.

Department of Mathematics
Arizona State University
Tempe, AZ 85287-1804, U.S.A.
E-mail: bremner@asu.edu
 Received on 1.6.2000
and in revised form on 18.8.2000 (3831)
