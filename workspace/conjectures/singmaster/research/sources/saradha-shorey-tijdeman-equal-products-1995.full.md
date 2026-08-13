<!-- source: https://bibliotekanauki.pl/articles/1391588.pdf | converted from PDF -->

ACTA ARITHMETICA
LXVIII.1 (1994)

On arithmetic progressions with equal products

by

N. Saradha (Bombay), T. N. Shorey (Bombay)
and R. Tijdeman (Leiden)

To Wolfgang M. Schmidt
at the occasion of his sixtieth birthday

1. Introduction. In this paper we consider the diophantine equation

(1) x(x + d1) . . . (x + (L − 1)d1) = y(y + d2) . . . (y + (M − 1)d2)

in positive integers d1, d2, L > 1, M > 1, x, y. We assume throughout
the paper that d1 and d2 are ﬁxed and that L/M has a given ratio. Put
k = gcd(L, M ), l = L/k and m = M/k. Hence l and m are ﬁxed and
gcd(l, m) = 1.
There are several results in the literature in case d1 = d2 = 1. In 1963
Mordell [6] proved that (1) with (L, M ) = (2, 3) implies that (x, y) = (2, 1) or
(14, 5). MacLeod and Barrodale [5] showed in 1970 that (1) has no solutions
if (L, M ) = (2, 4), (2, 6), (2, 8), (2, 12), (4, 8) or (5, 10) and admits only
the solution (x, y) = (8, 1) if (L, M ) = (3, 6). Two years later Boyd and
Kisilevsky [1] proved that (x, y) = (2, 1), (4, 2), (55, 19) are the only solutions
of (1) if (L, M ) = (3, 4). For ﬁxed L and M = 2L, MacLeod and Barrodale
further showed that (1) admits only ﬁnitely many solutions. In 1990 Saradha
and Shorey [8] proved that there exists only one solution with M = 2L,
namely (L, M, x, y) = (3, 6, 8, 1). In 1991 they showed in [9] that (1) has
no solutions with M = 3L or M = 4L. Recently, Mignotte and Shorey
showed that this is also the case when M = 5L or M = 6L. In general, for
m > 1 and M = mL, Saradha and Shorey [10] proved that equation (1)
implies that max(L, x, y) is bounded by an eﬀectively computable number
depending only on m.
In 1992 Saradha and Shorey [11] started the study of equation (1) for
more general pairs (d1, d2). They showed that if d1 = d2 = d and l = 1, m >
1 then there exists an eﬀectively computable upper bound for k = L, x and
y which depends only on d and m. Later, Saradha and Shorey [12] showed

[89]

90 N. Saradha et al.

that equation (1) implies that k is bounded by an eﬀectively computable
number depending only on d1, d2 and m. They further showed that x and
y are bounded by such a number unless

(i) m = k = 2, d1 = 2d2
2, x = y2 + 3d2y, or
(ii) d1/d
m
2 is a product of m > 2 distinct positive integers composed of
primes not exceeding m and m ≥ α(k) where α(k) = 14 for 2 ≤ k ≤ 7,
α(8) = 50 and α(k) = exp(k log k − 1.25475k − log k + 1.56577) for k ≥ 9.
Condition (i) is necessary. In the present paper we shall show that con-
dition (ii) is superﬂuous.
The authors [13] studied equation (1) with L = M . Observe that in
this case d1 = d2 implies x = y. Therefore there is no loss of generality in
assuming that d1 < d2 and gcd(d1, d2, x, y) = 1. We proved that under
these assumptions L, M , x and y are bounded by an eﬀectively computable
number depending only on d2 unless d1 = 1, d2 = 4, x = L + 1, y = 2.
Observe that

(L + 1)(L + 2) . . . (2L) = 2 · 6 · . . . · (4L − 2) for L = 2, 3, . . . ,

since both sides equal (2L)!/L!. Hence, in case L = M there is an inﬁnite
class of exceptions.
The following two theorems cover all pairs (L, M ) with L ̸= M dealt
with in the literature up to now.

Theorem 1. Let d1, d2, L, M , x and y be as in the ﬁrst paragraph of
this section. If

(2) L ∈ {2, 4} and M is odd

then max(x, y) ≤ C1 where C1 is some eﬀectively computable number de-
pending only on d1, d2 and M .

Theorem 2. Let d1, d2, L, M , x and y be as in the ﬁrst paragraph of
this section. Suppose that gcd(L, M ) > 1 and L ̸= M . Then

(3) max(L, M, x, y) ≤ C2
where C2 is some eﬀectively computable number depending only on d1, d2
and L/M , unless

(d1, d2, L, M, x, y) or (d2, d1, M, L, y, x) equals (d, 2d
2, 4, 2, z, z2 + 3dz)

for some positive integers d and z.

2. The proof of Theorem 1. We shall use the following lemma.

Lemma 1. Let P (X) be an odd monic polynomial with real coeﬃcients
of degree M > 1 such that for some positive number v there are (M − 1)/2
distinct real numbers β with P (β) = v, P ′(β) = 0. Then

P (X) = a1TM (a2X)

Arithmetic progressions with equal products 91

where TM (X) is the M-th Chebyshev polynomial cos(M arccos X) and a1
and a2 are non-zero real constants.

P r o o f. As P is odd, there are also (M − 1)/2 distinct real numbers
β with P (β) = −v, P ′(β) = 0. Since P ′ has degree M − 1, the union of
the numbers β is the set of roots of P ′ and all the roots of P ′ are simple.
It follows that every root of P ′ is a point where P has a local extremum.
Since P is monic and odd, the extremum attained for the lowest value of β
is a maximum v, then follows a minimum −v, a maximum v and so forth,
alternating and ending with a minimum −v. Observe that there is a unique
point β0, greater than the largest value where P attains a maximum, such
that P (β0) = v, P ′(β0) > 0. Of course, P (−β0) = −v, P ′(−β0) > 0. Deﬁne
̃PM (X) = β−M
0 P (β0X). Then ̃PM (X) is a monic polynomial of degree M
with | ̃PM (X)| ≤ β−M
0 v for |X| ≤ 1 and it assumes the values β−M
0 v and
−β−M
0 v each (M + 1)/2 times in the interval [−1, 1] in alternating way.
Put ̃TM (X) = 2−M +1TM (X). Then ̃TM has the smallest maximum ab-
solute value on [−1, 1] among all monic polynomials of degree M and every
monic polynomial ̸= ± ̃TM has a higher maximum absolute value. (See e.g.
[7], pp. 56–57.) Suppose ̃PM ̸= ̃TM . Then β−M
0 v > max−1≤X≤1 | ̃TM (X)|, so
that ̃PM (X) − ̃TM (X) is positive at each point β with ̃PM (β) = β−M
0 v and
negative at each point β with ̃PM (β) = −β−M
0 v. Since both ̃PM and ̃TM
are monic, it follows that ̃PM − ̃TM is a polynomial of degree at most M − 1
which has M sign changes in the interval [−1, 1], which is a contradiction.
Thus ̃PM = ̃TM , which implies that

P (X) = 2(β0/2)M TM (X/β0).

The second lemma is due to Brindza. It is proved by the method of
estimating linear forms of logarithms.

Lemma 2. Let f (X) ∈ Z[X], f (X) = a0(X − α1)
r1 . . . (X − αn)
rn, be
a polynomial with distinct roots α1, . . . , αn. Then there exists an eﬀectively
computable number C3 depending only on f such that the equation z2 =
f (y) in rational integers y, z implies max(|y|, |z|) ≤ C3 unless at most two
exponents rj are odd.

P r o o f. See [2] or [15], Theorem 8.3.

P r o o f o f T h e o r e m 1. Consider equation (1) with L = 2. Since
x(x + d1) = (x + 1
2 d1)
2 − 1
4 d2
1, this implies

(4) z2 = 4y(y + d2) . . . (y + (M − 1)d2) + d2
1
where z = 2x + d1. Now consider equation (1) with L = 4. Then

(x
2 + 3d1x + d2
1)
2 − d
4
1 = y(y + d2) . . . (y + (M − 1)d2)

92 N. Saradha et al.

whence

(5) z2 = y(y + d2) . . . (y + (M − 1)d2) + d4
1
where z = x
2 + 3d1x + d
2
1. We conclude that all cases of Theorem 1 can be
reduced to an equation

z2 = δy(y + d2) . . . (y + (M − 1)d2) + c
2

where c is some positive rational integer and δ = 1 or 4.
We deal ﬁrst with the cases with M = 3. In these cases equation (1) is
reduced to the elliptic equation

(6) z2 = δy(y + d2)(y + 2d2) + c
2.

Put f (Y ) = δY (Y + d2)(Y + 2d2) + c
2. According to Lemma 2 we have
max(|y|, |z|) ≤ C3 where C3 depends only on d2 and c unless f has a double
root α. In the latter case we have

0 = δ−1f ′(α) = 3α2 + 6d2α + 2d
2
2,

which implies α = −d2 ± d2
3 √3. Hence

0 = f (α) = δ(α3 + 3d2α2 + 2d
2
2α) + c
2 = ∓ 2
9 δd3
2√3 + c
2.

Since δ, c and d2 are rational, this implies d2 = 0, which is a contradiction. So
we obtain max(x, y) ≤ C4 where C4 is some computable number depending
only on d1 and d2.
We are left with the cases L ∈ {2, 4} and M is odd, M ≥ 5. Here we
consider the hyperelliptic equation z2 = f (y) where

(7) f (Y ) := δY (Y + d2) . . . (Y + (M − 1)d2) + c
2

and c is some positive rational integer. According to Lemma 2 we have
max(y, z) ≤ C3 where C3 depends only on c, d2 and M , unless f has exactly
one root of odd order. In the latter case we may assume without loss of
generality that
f (Y ) = δ(Y − α1)r1 (Y − α2)
r2 . . . (Y − αn)rn

with α1, . . . , αn distinct roots, r1 odd and r2, . . . , rn even. Since f (Y ) − c
2

has M distinct real roots, the roots of f ′ are real and simple by Rolle’s
theorem. Thus r1 = 1, r2 = . . . = rn = 2. Therefore M = 2n − 1 and f has
(M − 1)/2 double roots α2, . . . , αn.
Consider the polynomial

g(Y ) := (Y − M − 1
2
 )(
Y − M − 3
2
 ) . . . (
Y + M − 3
2
 )(Y + M − 1
2
 )
.

Observe that g is an odd function and that

f (Y ) = δdM
2 g( Y
d2 + M − 1
2
 ) + c
2.

Arithmetic progressions with equal products 93

Since f has (M − 1)/2 double roots, the polynomial g has (M −1)/2 distinct
real values β with g(β) = −δc2d−M
2 , g′(β) = 0. Since g is odd, Lemma 1
gives that the function g is of the form g(Y ) = a1TM (a2Y ) where TM is the
M th Chebyshev polynomial and a1 and a2 are non-zero real constants. This
implies that
 f (Y ) = δa1d
M
2 TM
 ( a2
d2 Y + a2(M − 1)
2
 ) + c
2.

We infer from (7) that

Y (Y + d2) . . . (Y + (M − 1)d2) = a1dM
2 TM
 ( a2
d2 Y + a2(M − 1)
2
 ).

However, it follows from the deﬁnition of Chebyshev polynomials that for
M > 3 the roots of TM are not equidistant, which yields a contradiction.
We conclude that max(x, y) ≤ C5 where C5 is some number depending only
on d1, d2 and M .

3. Lemmas for the proof of Theorem 2. Using the notation of the
ﬁrst paragraph of the introduction we rewrite (1) as follows:

(8) x(x + d1) . . . (x + (lk − 1)d1) = y(y + d2) . . . (y + (mk − 1)d2).

Without loss of generality we shall assume that l < m. We shall frequently
use the Vinogradov symbol ≪ and then tacitly assume that the implied
constants are eﬀectively computable positive numbers depending only on
d1, d2, l and m. Note that l and m are completely determined by L/M .

Lemma 3. k ≪ log(x + 1).

P r o o f. We assume that k is larger than some suitable number depending
only on d1, d2, l and m. We express this by saying that k is taken suﬃciently
large. Let p be the smallest prime number which does not divide d1d2. Then

ordp(y(y + d2) . . . (y + (mk − 1)d2)) ≥ [ mk
p
 ] + [ mk
p2
 ] + . . .

On the other hand,

ordp(x(x + d1) . . . (x + (lk − 1)d1))

≤ max
i=0,...,lk−1 ordp(x + id1) + [ lk
p
 ] + [ lk
p2
 ] + . . .

It now follows from (8) and l < m that, for k suﬃciently large,

k ≪ [ mk
p
 ] − [ lk
p
 ] ≤ max
i=0,...,lk−1 ordp(x + id1) ≪ log(x + kd1).

Hence k ≪ log(x + 1).

Lemma 4. x
l − ym ≪ ym−1 log(y + 1), ym − x
l ≪ x
l−1 log(x + 1).

94 N. Saradha et al.

P r o o f. We have, by (8), ykm ≤ (x + kld1)
kl. Hence, by Lemma 3,
ym/l − x ≤ kld1 ≪ log(x + 1). This implies ym − x
l ≪ x
l−1 log(x + 1). For
the proof of the ﬁrst inequality we derive from (8) and Lemma 3 as above
that xl/m − y ≪ log(x + 1), which implies that log(x + 1) ≪ log(y + 1) and
the ﬁrst inequality follows.

The following inequalities follow immediately from Lemmas 3 and 4:

(9) k ≪ log(y + 1),

(10) x
l ≪ ym, ym ≪ x
l, |x
l − ym| ≪ min(x
l, ym) log y
y .

Because of Lemma 3, (9) and (10) we may assume that x and y are larger
than some suitable number depending only on d1, d2, l and m. We express
this by saying that x (or y) is taken suﬃciently large. From now onwards,
we shall assume without reference that x and y are suﬃciently large.
We adopt the notation of [10] in slightly modiﬁed form. We deﬁne posi-
tive integers Aj(ν, k) for ν ∈ {l, m} by

z(z + 1) . . . (z + νk − 1) =
 νk−1∑

j=0 Aj(ν, k)zνk−j.

Further we determine rational numbers Bj(ν, k) and Hj(ν, k) such that

(zν + B1(ν, k)zν−1 + . . . + Bν(ν, k))k =
 νk∑

j=0 Hj(ν, k)zνk−j

satisﬁes
 Hj(ν, k) = Aj(ν, k) for 0 ≤ j ≤ ν.

We introduce the notation

Gj(ν, k) = Aj(ν, k) − Hj(ν, k) for 0 < j ≤ νk.

Lemma 5. There exist eﬀectively computable absolute constants c1 and
c2 such that
 Aj(ν, k) ≤ (νk)2j for 0 ≤ j < νk,(a)
 Bj(ν, k) ≤ c
j3/2
1 (νk)
2j for 1 ≤ j ≤ ν,(b)
 |Gj(ν, k)| ≤ c
j√
ν
2 (νk)
2j for 0 < j ≤ νk,(c) k2j−1Bj(ν, k) ∈ Z for 1 ≤ j ≤ ν,(d) k2j−1Gj(ν, k) ∈ Z for 0 < j ≤ νk.(e)
 Arithmetic progressions with equal products 95

P r o o f. (a) Aj(ν, k) ≤ (
νk−1
j )
(νk)
j < (νk)2j.
(b) As the proof of [10], Lemma 1.
(c) As the proof of [10], Lemma 2.
(d), (e) As the proof of [10], Lemma 3.

Put

(11) Lj = Bj(l, k)d
j
1 for 1 ≤ j ≤ l,

Mj = Bj(m, k)dj
2 for 1 ≤ j ≤ m,

(12) L∗
j = Gj(l, k)d
j
1 for 1 ≤ j ≤ lk,

M ∗
j = Gj(m, k)d
j
2 for 1 ≤ j ≤ mk.

Then

(13) x(x + d1) . . . (x + (lk − 1)d1)
= (xl + L1xl−1 + . . . + Ll)
k + L
∗
l+1x
kl−l−1 + L∗
l+2x
kl−l−2 + . . .

and

(14) y(y + d2) . . . (y + (mk − 1)d2)

= (ym + M1ym−1 + . . . + Mm)k

+ M ∗
m+1ykm−m−1 + M ∗
m+2ykm−m−2 + . . .

Lemma 6.

(15) xl + L1xl−1 + . . . + Ll = ym + M1ym−1 + . . . + Mm.

P r o o f. By (13), (14), (8), (12) and Lemma 5(c),

D : = |(xl + L1xl−1 + . . . + Ll)
k − (ym + M1ym−1 + . . . + Mm)k|

= ∣
∣
∣
 lk∑

i=l+1 L∗
i x
lk−i −
 mk∑

j=m+1 M ∗
j ymk−j∣
∣
∣

≤
 lk∑

i=l+1 c
i√
l
2 (lkd1)
2ix
lk−i +
 mk∑

j=m+1 c
j√
m
2 (mkd2)
2jymk−j.

By Lemma 3 and (9), we obtain

D ≤ (lkd1)
2l+2c
(l+1)√
l
2 x
lk−l−1

1 − c
√
l
2 (lkd1)2/x + (mkd2)
2m+2c
(m+1)√
m
2 ymk−m−1

1 − c
√
m
2 (mkd2)2/y

≪ ( k2

x
 )l+1x
lk + ( k2

y
 )m+1ymk.

96 N. Saradha et al.

On the other hand, we have L1 > 0, M1 > 0 and

D = |(x
l + L1x
l−1 + . . . + Ll)k − (ym + M1ym−1 + . . . + Mm)
k|

≥ |(x
l + L1x
l−1 + . . . + Ll) − (ym + M1ym−1 + . . . + Mm)|

× min(xl(k−1), ym(k−1)).

Suppose (15) does not hold. Then, by (11), Lemma 5(d) and l < m, it fol-
lows that D ≥ wk−1/k2m−1 with w = min(x
l, ym). On combining the lower
and upper bound for D we obtain, using the fact that l < m and x ≫ y by
Lemma 4,
 wk−1 ≤ k2m−1D ≪ k4m+1

y max(xlk−l, ymk−m).

Hence, by (9) and (10),

wk−1 ≪ k4m+1

y (w + |x
l − ym|)k−1 ≪ (log y)
4m+1

y wk−1(
1 + log y
y
 )k−1.

This implies, by (9),

log y ≪ log log y + k log (
1 + log y
y
 ) ≪ log log y + (log y)
2

y .

This proves that y ≪ 1, which is a contradiction.

Lemma 7. We have
 L∗
i = 0 for l < i < 2l

and

(16) M ∗
j = 0 for m < j < 2m.

P r o o f. Deﬁne I and J by

L
∗
l+1 = . . . = L∗
I−1 = 0, L∗
I ̸= 0, M ∗
m+1 = . . . = M ∗
J−1 = 0, M ∗
J ̸= 0.

By (15), (8), (13) and (14), we obtain ∑lk
i=I L∗
i x
lk−i = ∑mk
j=J M ∗
j ymk−j.
Therefore, by (10), it suﬃces to show that either Al+1 = . . . = A2l−1 = 0 or
Bm+1 = . . . = B2m−1 = 0. Suppose that this assertion is false. Then we can
take l < I < 2l and m < J < 2m. Observe that mI = lJ and gcd(l, m) = 1
imply l | I, a contradiction. We prove the lemma when mI < lJ and the
proof for the case mI > lJ is similar. We have

(17) mI ≤ lJ − 1.

Arithmetic progressions with equal products 97

Hence, by (12), Lemma 5(c), Lemma 3 and (9),

|L∗
I x
lk−I | ≤
 lk∑

i=I+1 |L
∗
i |x
lk−i +
 mk∑

j=J |M ∗
j |ymk−j

≤
 lk∑

i=I+1 c
i√
l
2 (lkd1)
2ix
lk−i +
 mk∑

j=J c
j√m
2 (mkd2)
2jymk−j

≤ 2c
(I+1)√
l
2 (lkd1)
2I+2

xI+1 x
lk + 2c
J√
m
2 (mkd2)2J

yJ ymk.

By (12), Lemma 5(e) and L∗
I ̸= 0, we have |L∗
I | ≥ k−2I . Hence, by I < 2l,
Lemma 3 and (10),

1 ≤ 2c
(I+1)
√l
2 k2I (lkd1)
2I+2

x + 2c
J√
m
2 k2I (mkd2)2J

yJ−mI/l
 ( ym

xl
 )k−I/l
(18)
 ≤ 2 (c
√l
2 lkd1)
8l

x + 2 cJ√
m
2 k4l(mkd2)2J

yJ−mI/l
 (1 + |ym − x
l|
xl
 )k

≤ 1
2 + 2 c
J√
m
2 k4l(mkd2)
2J

yJ−mI/l
 (
1 + c3 log y
y
 )k

for some number c3 depending only on d1, d2, l and m. Since J < 2m, (18)
implies, by (17),

(19) y1/l ≤ c
J√
m
2 (mkd2)
10m(
1 + c3 log y
y
 )k.

By (19) and (9)

(20) log y ≪ log k + k log (1 + c3 log y
y
 ) ≪ log log y + (log y)2

y .

It is clear from (20) that y ≪ 1, a contradiction.

The next lemma is due to R. Balasubramanian.

Lemma 8. Let m > 2. There exists an eﬀectively computable number C6
depending only on m and an integer q with m < q < 2m such that

(21) Gq(m, k) ̸= 0 for k ≥ C6.

P r o o f. See [10], Lemma 7.

Lemma 9. Suppose that f (X) and g(Y ) are polynomials of positive degree
with rational numbers as coeﬃcients. Assume that the degrees of f and g
are relatively prime. Then f (X) − g(Y ) is irreducible over the rationals.

P r o o f. This is due to Ehrenfeucht [4]. Cf. [14], p. 94 and [3].

98 N. Saradha et al.

4. Proof of Theorem 2. It suﬃces to show that equation (8) with
k > 1 and l < m implies that max(k, x, y) ≤ C2. By the result of Saradha
and Shorey [10] mentioned in the introduction we may assume m > 2. By
Lemma 3 and (10) we may take x and y suﬃciently large so that (16) holds.
Then, by (12), Lemma 8 and m > 2, we have k ≪ 1. We may therefore
assume that k is ﬁxed. Hence L1, . . . , Ll and M1, . . . , Mm are ﬁxed. If

(22) X(X + d1) . . . (X + (lk − 1)d1) − Y (Y + d2) . . . (Y + (mk − 1)d2)

and

(23) (X l + L1X l−1 + . . . + Ll) − (Y m + M1Y m−1 + . . . + Mm)

have no non-constant common factor, then the resultant of both polynomials
with respect to X is a non-zero polynomial in Y which is a linear combination
of the polynomials (22) and (23). Since every suﬃciently large solution (x, y)
of (8) is also a solution of (15), it follows that y is a zero of the resultant.
This implies that y is bounded. This contradicts our assumption that y is
suﬃciently large. If (22) and (23) have a non-constant common factor, then
we see from Lemma 9 that (22) has to be divisible by (23).
Put g(Y ) = Y m +M1Y m−1 +. . .+Mm. By taking Y = 0, −d2, −2d2, . . . ,
−(mk − 1)d2 we ﬁnd that each polynomial

fj(X) := X l + L1X l−1 + . . . + Ll − g(−jd2) (j = 0, 1, . . . , mk − 1)

is a divisor of
 X(X + d1) . . . (X + (lk − 1)d1).

However, g can assume each value at most m times. So in 0, −d2, . . . ,
−(mk − 1)d2 the polynomial g attains at least k distinct values. To each
value corresponds a polynomial fj(X) of degree l. Since X(X + d1) . . .
. . . (X + (lk − 1)d1) is a polynomial of degree lk and any two distinct poly-
nomials fj are coprime (their diﬀerence is constant), there are at most k
distinct polynomials fj. Thus the polynomials {fj}mk−1
j=0 split into k classes
of size m such that within a class the polynomials are identical and any two
polynomials from diﬀerent classes are distinct.
First we consider the case where m is odd. We have shown that at the
points {−jd2 | 0 ≤ j < mk} the monic polynomial g of odd degree m > 2
attains exactly k distinct values and each value precisely m times. Denote
these values by v1 < v2 < . . . < vk and the points where g attains the value
vi by −ji,1d2 < −ji,2d2 < . . . < −ji,md2 (i = 1, . . . , k). By Rolle’s theorem
each interval (−ji,hd2, −ji,h+1d2) contains a zero of g′. Since g′ has only
m − 1 zeros, z1, z2, . . . , zm−1 say, these zeros are distinct and simple and

−ji,1d2 < z1 < −ji,2d2 < z2 < . . . < −ji,m−1d2 < zm−1 < −ji,md2
(i = 1, . . . , k).

Arithmetic progressions with equal products 99

The polynomial g is increasing on (−∞, z1), decreasing on (z1, z2), increasing
on (z2, z3), . . . , increasing on (zm−1, ∞). It follows that the set {−ji,1d2 | 1 ≤
i ≤ k} consists of the k extreme negative points {−jd2 | (m − 1)k ≤ j ≤
mk −1} and, more precisely, j1,1 = mk −1, j2,1 = mk −2, . . . , jk,1 = mk −k.
Further, we have the following scheme in case m is odd (↓ indicates g is
increasing, ↑ indicates g is decreasing):

v1 = g(−(mk − 1)d2) = . . . →
= g(−(3k − 1)d2) = g(−kd2) →
= g(−(k − 1)d2)
↓ ↓ ↑ ↓
v2 = g(−(mk − 2)d2) = . . . = g(−(3k − 2)d2) = g(−(k + 1)d2) = g(−(k − 2)d2)
↓ ↓ ↑ ↓
... ... ... ...
↓ ↓ ↑ ↓
vk−1 = g(−(mk − k + 1)d2) = . . . = g(−(2k + 1)d2) = g(−(2k − 2)d2) = g(−d2)
↓ ↓ ↑ ↓
vk = g(−(mk − k)d2) →
= . . . = g(−2kd2) →
= g(−(2k − 1)d2) = g(0)
Hence we have

g(Y ) = Y (Y + (2k − 1)d2)(Y + 2kd2)(Y + (4k − 1)d2) . . .

. . . (Y + (mk − k)d2) + vk
= (Y + d2)(Y + (2k − 2)d2)(Y + (2k + 1)d2)(Y + (4k − 2)d2) . . .

. . . (Y + (mk − k + 1)d2) + vk−1.

By putting Y = 0 and Y = −(2k − 1)d2 in the above equality we have

vk − vk−1 = d
m
2 · 1 · (2k − 2)(2k + 1)(4k − 2) . . . (mk − k + 1)
= d
m
2 · (−2k + 2)(−1)(2)(2k − 1) . . . (mk − 3k + 2),

which is impossible since m ≥ 3.
If m is even, a similar reasoning yields the following scheme:

v1 = g(−(mk − k)d2) →
= . . . →
= g(−(3k − 1)d2) = g(−kd2) →
= g(−(k − 1)d2)
↑ ↓ ↑ ↓
v2 = g(−(mk − k + 1)d2) = . . . = g(−(3k − 2)d2) = g(−(k + 1)d2) = g(−(k − 2)d2)
↑ ↓ ↑ ↓
... ... ... ...
↑ ↓ ↑ ↓
vk−1 = g(−(mk − 2)d2) = . . . = g(−(2k + 1)d2) = g(−(2k − 2)d2) = g(−d2)
↑ ↓ ↑ ↓
vk = g(−(mk − 1)d2) = . . . = g(−2kd2) →
= g(−(2k − 1)d2) = g(0)
Hence we have

g(Y ) = Y (Y + (2k − 1)d2)(Y + 2kd2)(Y + (4k − 1)d2) . . .

. . . (Y + (mk − 1)d2) + vk
= (Y + d2)(Y + (2k − 2)d2)(Y + (2k + 1)d2)(Y + (4k − 2)d2) . . .

. . . (Y + (mk − 2)d2) + vk−1.

100 N. Saradha et al.

By putting Y = 0 and Y = −(2k − 1)d2 in the above equality we have

vk − vk−1 = d
m
2 · 1 · (2k − 2)(2k + 1)(4k − 2) . . . (mk − 2)
= d
m
2 · (−2k + 2)(−1)(2)(2k − 1) . . . (mk − 2k − 1),

which is impossible since m ≥ 4. In fact, the above argument is also valid
when m = 2 and k ≥ 3.
 References

[1] D. W. B o y d and H. H. K i s i l e v s k y, The diophantine equation u(u + 1)(u + 2)(u +
3) = v(v + 1)(v + 2), Paciﬁc J. Math. 40 (1972), 23–32.
[2] B. B r i n d z a, On S-integral solutions of the equation ym = f (x), Acta Math. Hun-
gar. 44 (1984), 133–139.
[3] J. W. S. C a s s e l s, Factorization of polynomials in several variables, in: Proc. 15th
Scandinavian Congress, Oslo 1968, Lecture Notes in Math. 118, Springer, 1970,
1–17.
[4] A. E h r e n f e u c h t, A criterion for absolute irreducibility of polynomials, Prace Mat.
2 (1958), 167–169 (in Polish).
[5] R. A. M a c L e o d and I. B a r r o d a l e, On equal products of consecutive integers,
Canad. Math. Bull. 13 (1970), 255–259.
[6] L. J. M o r d e l l, On the integer solutions of y(y + 1) = x(x + 1)(x + 2), Paciﬁc J.
Math. 13 (1963), 1347–1351.
[7] T. J. R i v l i n, The Chebyshev Polynomials, Wiley, New York, 1974.
[8] N. S a r a d h a and T. N. S h o r e y, On the ratio of two blocks of consecutive integers,
Proc. Indian Acad. Sci. (Math. Sci.) 100 (1990), 107–132.
[9] —, —, On the equation (x + 1) . . . (x + k) = (y + 1) . . . (y + mk) with m = 3, 4,
Indag. Math. 2 (1991), 489–510.
[10] —, —, On the equation (x + 1) . . . (x + k) = (y + 1) . . . (y + mk), ibid. 3 (1992),
79–90.
[11] —, —, On the equation x(x + d) . . . (x + (k − 1)d) = y(y + d) . . . (y + (mk − 1)d),
ibid. 3 (1992), 237–242.
[12] —, —-, On the equation x(x + d1) . . . (x + (k − 1)d1) = y(y + d2) . . . (y + (mk − 1)d2),
Proc. Indian Acad. Sci. (Math. Sci.) 104 (1994).
[13] N. S a r a d h a, T. N. S h o r e y and R. T i j d e m a n, On arithmetic progressions of
equal lengths with equal products, Math. Proc. Cambridge Philos. Soc., to appear.
[14] A. S c h i n z e l, Selected Topics on Polynomials, University of Michigan Press, Ann
Arbor, 1982.
[15] T. N. S h o r e y and R. T i j d e m a n, Exponential Diophantine Equations, Cambridge
University Press, 1986.

SCHOOL OF MATHEMATICS MATHEMATICAL INSTITUTE

TATA INSTITUTE OF FUNDAMENTAL RESEARCH LEIDEN UNIVERSITY

HOMI BHABHA ROAD P.O. BOX 9512

BOMBAY 400005 2300 RA LEIDEN

INDIA THE NETHERLANDS

Received on 23.3.1994 (2583)
