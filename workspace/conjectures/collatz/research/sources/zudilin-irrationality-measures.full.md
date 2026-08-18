<!-- source: https://arxiv.org/pdf/math/0404523 | converted from PDF -->

arXiv:math/0404523v2  [math.NT]  27 May 2004An essay on irrationality measures
of π and other logarithms

Wadim Zudilin∗ (Moscow)

E-print math.NT/0404523
14 May 2004

To my teacher and friend A. I. Galochkin
on the occasion of his 60th birthday

Let a ∈ Q ∩ (0, 2], a ̸= 1. Then the sequence of quantities
∫ 1

0
 x
n(1 − x)n

(1 − (1 − a)x)n+1 dx ∈ Q log a + Q, n = 0, 1, 2, . . . , (1)

produces ‘good’ rational approximations to log a. There are several ways of perform-
ing integration in (1) in order to show that the integral lies in Q log a + Q; we give
an exposition of diﬀerent methods below. The aim of this essay is to demonstrate
how suitable generalizations of the integrals in (1) allow to prove the best known
results on irrationality measures of the numbers log 2, π and log 3. Although meth-
ods presented below work in general situations (e.g., for certain Q-linear forms in
logarithms) as well, the three numbers seem to be very nice and important models
for our exposition.
Bounds for irrationality measures are presented by means of upper estimates for
irrationality exponents. Recall that the irrationality exponent of a real irrational
number γ is deﬁned by the relation

µ = µ(γ) = inf{c ∈ R : the inequality |γ − a/b| ⩽ |b|−c has
only ﬁnitely many solutions in a, b ∈ Z}.

The estimates for µ(γ) are deduced by constructing sequences of linear forms in-
volving γ and using standard tools of the following shapes.

∗The work is supported by an Alexander von Humboldt research fellowship and partially sup-
ported by grant no. 03-01-00359 of the Russian Foundation for Basic Research.

Irrationality measures of logarithms 2

Proposition 1 ([10], Lemma 3.1). Let γ ∈ R be irrational. Suppose that a sequence
of linear forms bnx − an, with integer coeﬃcients from the ﬁeld of rationals or an
imaginary quadratic ﬁeld, satisﬁes

lim sup
n→∞ log |bn|
n ⩽ C1, lim
n→∞ log |bnγ − an|
n = −C0

for some positive real C0 and C1. Then µ(γ) ⩽ 1 + C1/C0.

Proposition 2 ([11], Lemma 2.1). Let ω, ω′ ∈ R be two irrational numbers. Suppose
that sequences of linear forms bnx − an and bnx − a
′
n, with integer coeﬃcients from
the ﬁeld of rationals or an imaginary quadratic ﬁeld, satisﬁes

lim sup
n→∞ log |bn|
n ⩽ C1, lim
n→∞ log |bnω − an|
n = −C0, lim
n→∞ log |bnω′ − a
′
n|
n = −C ′
0

for some positive real constants C0 < C ′
0 and C1. Then any nonzero element γ ∈
Qω+Qω′ is irrational with the bound µ(γ) ⩽ 1+C1/C0 for the irrationality exponent.

Remark. In fact, the statement of Lemma 2.1 in [11] slightly diﬀers from our last
claim, but one can easily verify that the proof given there proves our ‘modiﬁcation’
as well.

1 Irrationality measure for log 2 (after E. Rukhadze)

1.1 Gauss hypergeometric function

It is worth performing a slightly general integral than (1), namely

I(m, n0, n1; a) = ∫ 1

0
 x
n0(1 − x)n1

(1 − (1 − a)x)m+1 dx (2)

for non-negative integers m, n0, n1, provided the condition max{m, n0} ⩽ n1 holds
for further convenience. The integral in (2) is exactly Euler’s integral for the Gauss
hypergeometric series:

I(m, n0, n1; a) = Γ(n0 + 1) Γ(n1 + 1)
Γ(n0 + n1 + 2) 2F1
(
m + 1, n0 + 1
n0 + n1 + 2
 ∣
∣
∣
∣ 1 − a
)

= Γ(n1 + 1)
Γ(m + 1)
 ∞∑

ν=0
 Γ(m + 1 + ν) Γ(n0 + 1 + ν)
Γ(1 + ν) Γ(n0 + n1 + 2 + ν) (1 − a)ν (3)

(see, e.g., [3], Section 2.2). The latter sum may be written as

I(m, n0, n1; a) =
 ∞∑

ν=0 R(ν)(1 − a)ν, (4)

Irrationality measures of logarithms 3

where

R(t) = (t + 1)(t + 2) · · · (t + m)
m! · n1!
(t + n0 + 1)(t + n0 + 2) · · · (t + n0 + n1 + 1) (5)

and R(t) = O(t
−1) as t → ∞ by m ⩽ n1. Denote m
∗ = min{m, n0} and n
∗
0 =
max{m, n0} and decompose the rational function (5) in a sum of partial fractions:

R(t) =
 n0+n1∑

k=n∗
0
 Ak
t + k + 1 =
 n0+n1∑

k=n∗
0
 (−1)m+n0−k( k
m)( n1
k−n0)

t + k + 1 . (6)

Then by (4) we obtain

I(m, n0, n1; a) =
 ∞∑

ν=−m∗ R(ν)(1 − a)ν =
 n0+n1∑

k=n∗
0 Ak(1 − a)−(k+1) ∞∑

ν=−m∗
 (1 − a)ν+k+1

ν + k + 1

=
 n0+n1∑

k=n∗
0 Ak(1 − a)−(k+1)( ∞∑

l=1 −
 k−m∗
∑

l=1
 ) (1 − a)l

l

= − log a ·
 n0+n1∑

k=n∗
0 Ak(1 − a)−(k+1) −
 n0+n1∑

k=n∗
0
 k−m∗
∑

l=1
 Ak(1 − a)l−(k+1)

l , (7)

hence
 I(m, n0, n1; a)(1 − a)n0+n1+1 · dn0+n1−m∗Dn0+n1−m∗ ∈ Z log a + Z, (8)

where d denotes the denominator of a and Dn stands for the least common multiple
of the numbers 1, 2, . . . , n. By the prime number theorem, we have the following
asymptotic formula:
 lim
n→∞ log Dn
n = 1.

1.2 Arithmetic valuation

The inclusion (8) may be essentially improved in several cases, and it is the obser-
vation that allowed Rukhadze to prove the record irrationality measure for log 2.
The symmetry of the 2F1-series in (3) with respect to its upper parameters m + 1
and n0 + 1 gives us a way to write the identity

I(m, n0, n1; a)
Γ(n0 + 1) Γ(n1 + 1) = I(n0, m, n0 + n1 − m; a)
Γ(m + 1) Γ(n0 + n1 − m + 1) (9)

(which is not so evident if one looks on deﬁnition (2)). The inclusion (8) written for
the I-quantity on the right of (9),

I(n0, m, n0 + n1 − m; a)(1 − a)n0+n1+1 · dn0+n1−m∗Dn0+n1−m∗ ∈ Z log a + Z,

Irrationality measures of logarithms 4

and the equality

I(m, n0, n1; a)(1 − a)n0+n1+1 · dn0+n1−m∗Dn0+n1−m∗ · m! (n0 + n1 − m)!
n0! n1!
= I(n0, m, n0 + n1 − m; a)(1 − a)n0+n1+1 · dn0+n1−m∗Dn0+n1−m∗

imply that if Φ(m, n0, n1) is the denominator of the quotient

m! (n0 + n1 − m)!
n0! n1! ,

then

I(m, n0, n1; a)(1−a)n0+n1+1·dn0+n1−m∗Dn0+n1−m∗ ·Φ(m, n0, n1)−1 ∈ Z log a+Z. (10)

By the well-known formula, for each prime p we have ordp N! = ⌊N/p⌋+⌊N/p2⌋+
⌊N/p3⌋ + · · · , where ⌊ · ⌋ denotes the integral part of a number. Therefore

Φ(m, n0, n1) = ∏

p pφ(p)+φ(p2)+φ(p3)+···, (11)

where
 φ(t) = max{
0, ⌊n0
t
 ⌋ + ⌊n1
t
 ⌋ − ⌊m
t
 ⌋ − ⌊n0 + n1 − m
t
 ⌋}.

The ﬁnal remark (made by G. Chudnovsky in [7] together with introducing the
method of asymptotic evaluation of the factors like (11)) consists in the fact that
the divisor ̃Φ(m, n0, n1) = ∏

p>√n1 pφ(p) (12)

of Φ(m, n0, n1) gives the main contribution in the asymptotic of (11) and may be
easily controlled.

1.3 Irrationality result

The choice a = 2 and n0 = 6n, m = 7n, n1 = 8n, where n is the positive integer
parameter increasing to ∞, allowed E. Rukhadze in [18] to prove the following result
(see also [10], [19] and [6]).

Theorem 1. The irrationality exponent of log 2 satisﬁes the inequality

µ(log 2) ⩽ 3.89139977 . . . .

We will brieﬂy indicate required ingredients of the proof. For the above choice
of the parameters we set

In = I(7n, 6n, 8n; 2) = ∫ 1

0
 (x
6(1 − x)8

(1 + x)7
 )n dx
1 + x = ¯An log 2 − ¯Bn,

Irrationality measures of logarithms 5

where, by (6) and (7),
 ¯An = (−1)n 14n∑

k=7n
 ( k
7n

)( 8n
k − 6n

).

Then

lim
n→∞ log In
n = log max
0<x<1 x
6(1 − x)8

(1 + x)7

= log 2533(7734633√
393 − 153333125)
77 = −11.84497806 . . . (13)

and, thanks to Stirling’s asymptotic formula for the factorial,

lim
n→∞ log | ¯An|
n = lim
n→∞ 1
n log max
7n⩽k⩽14n
 ( k
7n

)( 8n
k − 6n

)

= log max
7<y<14
( yy

77(y − 7)y−7 · 88

(y − 6)y−6(14 − y)14−y
 )

= log 2533(7734633√
393 + 153333125)
77 = 12.68147230 . . . . (14)

Concerning the asymptotic behaviour of the value Φn = ̃Φ(7n, 6n, 8n) in (12), we
use the fact φ(t) = ̟0(n/t), where

̟0(x) = max
{
0, ⌊6x⌋ + ⌊8x⌋ − 2⌊7x⌋
}

=
 {
1 if x ∈ [ 1
8, 1
7) ∪ [ 1
4, 2
7) ∪ [ 3
8, 3
7) ∪ [ 1
2, 4
7) ∪ [ 2
3, 5
7) ∪ [ 5
6, 6
7),
0 otherwise.

Therefore,

lim
n→∞ log Φn
n = ∫ 1

0 ̟0(x)dψ(x) = log 21533

77 + π(3 + 6√2 − 4√3)
6 = 2.45775406 . . . ,

(15)
where ψ(x) denotes the logarithmic derivative of the gamma function. Using inclu-
sions (10) and the asymptotics (13)–(15), we obtain

C0 = − log(7734633√
393 − 153333125) + 10 log 2 − 8 + π(3 + 6√
2 − 4√3)
6
= 6.30273213 . . . ,

C1 = log(7734633√
393 + 153333125) − 10 log 2 + 8 − π(3 + 6√
2 − 4√3)
6
= 18.22371823 . . . ,

Irrationality measures of logarithms 6

in the notation of Proposition 1 and, ﬁnally, conclude with the estimate

µ(log 2) ⩽ 1 + C1
C0 = 3.89139977 . . . .

The result for the measure of log 2 may be compared with that obtained in
simpler settings n0 = n1 = m = n (as in (1)):

C0 = −2 log(√
2 − 1) − 1 = 2 log(√2 + 1) − 1, C1 = 2 log(√2 + 1) + 1,

hence
 µ(log 2) ⩽ 1 + C1
C0 ⩽ 1 + 2 log(√2 + 1) + 1
2 log(√2 + 1) − 1 = 4.62210083 . . . .

2 Irrationality measure for π (after M. Hata)

2.1 Simultaneous approximations to logarithms

The change of variable z = 1 − (1 − a)x in (1) transforms the integral (1) into

(−1)n+1

(1 − a)2n+1
 ∫ a

1
 (z − 1)n(z − a)n

zn+1 dz. (16)

Instead of decomposing the latter integral we will perform a more general complex
integral
 Ik(a, m, n; a) = ∫
Γ1,a
 (z − 1)n0(z − a1)n1 · · · (z − ak)nk

zm+1 dz,

where Γ1,a denotes a smooth oriented path from 1 to a contained in C \ {0};
the parameters a, a1, . . . , ak are complex numbers distinct from 0, 1; the exponents
n0, n1, . . . , nk, m are positive integers. The integral in (16) corresponds to k = 1,
a1 = a and n0 = n1 = m = n. Setting additionally a0 = 1, we may compute, as
in [11], Section 3,

Ik(a, m, n; a) =
 n0∑

l0=0
 n1∑

l1=0
· · ·
 nk∑

lk=0 Al
(
n0
l0
 )(n1
l1
 ) · · · (
nk
lk
 ) ∫
Γ1,a zl0+l1+···+lk−m−1 dz

= ∑· · · ∑

l0+···+lk̸=m
 Al
l0 + · · · + lk − m
(
n0
l0
 ) · · · (
nk
lk
 )
(a
l0+···+lk−m − 1)

+ ∑· · · ∑

l0+···+lk=m Al
(n0
l0
 ) · · · (
nk
lk
 ) · log a, (17)

where Al = Al0,l1,...,lk = (−1)l0+l1+···+lka
n1−l1
1 · · · a
nk−lk
k

Irrationality measures of logarithms 7

and we use the formula
∫

Γ1,a zl−1 dz = ∫ a

1 zl−1 dz =
 {
a
l/l if l ̸= 0,
log a if l = 0.

The main idea is that the coeﬃcient of log a in the linear form (17) does not
depend on the choice of a (but of course the analytic behaviour of the integral
does!). The suitable and natural choice of a is from the set {a1, . . . , ak}. Then the
above quantities Ik produce simultaneous approximations to log a1, . . . , log ak.

2.2 Analytic and arithmetic ingredients

Our basic consideration will be devoted to the case k = 2, which is used in [11]
to give the linear independence measure of π and log 2 over Q (in particular, the
irrationality measure of π) and the new irrationality measure of π/√3.
Thus, Hata [11] takes k = 2 (that really gives an extension of (16), and hence
of (1)) and substitute a = a1 and a = a2 to get nice simultaneous approximations
to log a1 and log a2. Hata ‘restricts’ himself from the beginning to considering the
particular case n0 = n1 = n2 = 2n and m = 3n, where n is an increasing parameter.
However, this simple choice produces the best possible number-theoretic results, and
our consideration of the general case

n0 = α0n, n1 = α1n, n2 = α2n, m = αn,

where α0, α1, α2, α are positive integers, is mostly due to methodological reasons.
Write the integrals in the form

Jj,n = I2(aj) = ∫

γj
 e
nf (z)

z dz, j = 1, 2, (18)

where
 f (z) = α0 log(z − a0) + α1 log(z − a1) + α2 log(z − a2) − α log z

and the path γj joints the points 1 and aj and goes through the corresponding saddle
point. The saddle points ξ0, ξ1, ξ2 are solutions of the equation f ′(z) = 0 becoming
the cubic polynomial equation: two of these saddles correspond to the growth of the
integrals in (18),

lim
n→∞ log |J1,n|
n = Re f (ξ1), lim
n→∞ log |J2,n|
n = Re f (ξ2),

while the third saddle ξ0 determines the asymptotic behaviour of the coeﬃcients of
the linear forms.

Irrationality measures of logarithms 8

To compute the arithmetic of the coeﬃcients we should evaluate the true de-
nominators of the products

1
l0 + l1 + l2 − αn
(
α0n
l0
 )(
α1n
l1
 )(α2n
l2
 )
, l0 + l1 + l2 ̸= αn.

Clearly the least common multiple Dβn, where β = max{α, α0 + α1 + α2 − α},
is required but some primes p > √Cn may be then excluded from this Dβn by
considering the following problem: determine primes p dividing all the integers
(α0n
l0
 )(
α1n
l1
 )(α2n
l2
 )

under the additional condition l0 + l1 + l2 ≡ αn (mod p). Writing x = {n/p} and
yj = {lj/p}, j = 0, 1, 2, for the fractional parts, we reduce the problem to minimizing
the 1-periodic integer-valued function

̟(x, y0, y1, y2) =
 2∑

j=0
 (
⌊αjx⌋ − ⌊yj⌋ − ⌊αjx − yj⌋
)

on the cube (y0, y1, y2) ∈ [0, 1)3 under the additional hypothesis y0 + y1 + y2 ≡
αx (mod 1). (The last condition means that knowledge of x, y0, y1 determines the
remaining value y2 uniquely.) Denote by ̟0(x) the required minimum. For example,
Hata’s choice α0 = α1 = α2 = 2, α = 3 gives

̟0(x) =
 {
1 if x ∈ [ 1
2, 2
3),
0 otherwise.

There is also a ‘problem’ of ﬁnding the true denominators of Al and Ala
l0+l1+l2−m.
For example, in the case a1 = 2, a2 = 1 + i (of simultaneous approximations to log 2
and π) we have

(−1)l0+l1+l2Ala
l0+l1+l2−m
0 = 2n1−l1(1 + i)n2−l2 ∈ Z[i],

(−1)l0+l1+l2Ala
l0+l1+l2−m
1 = 2n1+l0+l2−m(1 + i)n2−l2

= 2n1+l0−m(1 + i)l2(1 − i)l2 · (1 + i)2⌊n2/2⌋(1 + i)2{n2/2}−l2

= 2n1+⌊n2/2⌋−m+l0i
⌊n2/2⌋(1 + i)2{n2/2}(1 − i)l2 ∈ Z[i],

(−1)l0+l1+l2Ala
l0+l1+l2−m
2 = 2n1−l1(1 + i)n2+l0+l1−m

= (1 + i)n1−l1(1 − i)n1−l1(1 + i)n2+l0+l1−m

= (1 + i)n1+n2−m+l0(1 − i)n1−l1 ∈ Z[i],

provided that n1 + ⌊n2/2⌋ − m ⩾ 0 and n1 + n2 − m ⩾ 0 (i.e., that α1 + α2/2 ⩾ α).

Irrationality measures of logarithms 9

2.3 Measure for π

Thus, Hata’s choice a1 = 2, a2 = 1 + i and n0 = n1 = n2 = 2n, m = 3n with the
help of Proposition 2 gives the following result.

Theorem 2. The irrationality exponent of any nonzero γ ∈ Q log 2 + Qπ satisﬁes
the inequality µ(γ) ⩽ 8.01604539 . . . .

We would like to refer the interested reader to the notes [5] that could give some
feelings of how diﬃcult is evaluating the irrationality measure of π.

2.4 Double hypergeometric series

Here we present a connection of Hata’s construction with hypergeometric series (that
were a major tool in Section 1).
For simplicity, we will set a = a1, b = a2 and deal with the integrals

J = ∫ a

1
 (z − 1)n0(z − a)n1(z − b)n2

zm+1 dz

and
 J ∗ = ∫ b

1
 (z − 1)n0(z − a)n1(z − b)n2

zm+1 dz

giving the simultaneous approximations to log a and log b. Applying the starting
change of variable z = 1 − (1 − a)x to the ﬁrst integral we obtain the single integral

J = (−1)n0+1(1 − a)n0+n1+1(1 − b)n2 ∫ 1

0
 x
n0(1 − x)n1(1 − 1 − a
1 − b x
)n2

(1 − (1 − a)x)m+1 dx (19)

that may be identiﬁed with the Appell hypergeometric function

J = (−1)n0+1(1 − a)n0+n1+1(1 − b)n2 Γ(n0 + 1) Γ(n1 + 1)
Γ(n0 + n1 + 1)

× F1
(
n0 + 1; m + 1, −n2; n0 + m + 2; 1 − a, 1 − a
1 − b
 )

(see [4], Section 9.3, formula (4)), where the series

F1(A; B, B′; C; X, Y ) =
 ∞∑

ν=0
 ∞∑

µ=0
 (A)ν+µ(B)ν(B′)µ
ν! µ!(C)ν+µ X νY µ

is absolutely convergent in the domain |X| < 1, |Y | < 1.
The next change of variable

x = (1 − y)∕(
1 − 1 − a
1 − b y)

Irrationality measures of logarithms 10

in (19) gives the integral representation

J = (−1)n0+m(1 − a)n0+n1+1(1 − b)n0+n2+1(a − b)n1+n2+1

× ∫ 1

0
 yn1(1 − y)n0 dy
(
a(1 − b) − b(1 − a)y)m+1(
(1 − b) − (1 − a)y)n0+n1+n2−m+1 (20)

= (−1)n0+m (1 − a)n0+n1+1(a − b)n1+n2+1

am+1(1 − b)n1+1 Γ(n0 + 1) Γ(n1 + 1)
Γ(n0 + n1 + 1)

× F1
(
n1 + 1; m + 1, n0 + n1 + n2 − m + 1; n0 + n1 + 2; b(1 − a)
a(1 − b) , 1 − a
1 − b
 )
.

The case a = 2, b = 1 + i gives us the following arguments of the last F1-series:

1 − a
1 − b = −i = e
−πi/2, b(1 − a)
a(1 − b) = 1
√2e
−πi/4.

Finally, the above changes of variable applied to the integral J ∗ produce the
same integrals as in (19) and (20) but with integrations over smooth paths from 0
to (1 − b)/(1 − a) and from ∞ to 1, respectively.

3 Irrationality measure for log 3 (after G. Rhin)

3.1 Preliminary remark

As mentioned, the method of Section 2 have several other applications. For instance,
the choice a = 4/3, b = 3/2 and n0 = n1 = n2 = 2n, m = 3n (cf. Section 2.3) with
the help of Proposition 2 implies that the irrationality exponent of γ ∈ Q log 2 +
Q log 3 satisﬁes the inequality µ(γ) ⩽ 11.1017577 . . . (see [12], Corollary 3.1).

3.2 Back to rational approximations to log 2

As we already know from Section 1.1, for our starting integral (1) in the case a = 2
we have
 Dn
 ∫ 1

0
 ( x(1 − x)
1 + x
 )n dx
1 + x ∈ Z log 2 + Z,

hence
 Dn
 ∫ 1

0
 (x(1 − x)
1 + x
 )k dx
1 + x ∈ Z log 2 + Z

for any non-negative integer k ⩽ n. Considering linear combinations of the latter
integrals we arrive at general inclusions

Dn
 ∫ 1

0 Gn
(x(1 − x)
1 + x
 ) dx
1 + x ∈ Z log 2 + Z (21)

Irrationality measures of logarithms 11

valid for all polynomials Gn(y) ∈ Z[y] of degree deg Gn ⩽ n. To guess a ‘nice’ choice
for the polynomial Gn, we start with notifying that
∫ 1

0
 ( x(1 − x)
1 + x
 )n dx
1 + x = C ∫ b

0
 ( x(1 − x)
1 + x
 )n dx
1 + x,

where C is a constant (in our case C = 2) and b is the saddle point for the integrand:
b = √2 − 1; therefore,
∫ 1

0
 (x(1 − x)
1 + x
 )n dx
1 + x = C ∫ (
√2−1)2

0 ynx(y) dy,

where y = x(1 − x)/(1 + x) and x(y) (0, (√
2 − 1)2) → (0, b) is the inverse function.
Finally, ∫ 1

0 Gn
(x(1 − x)
1 + x
 ) dx
1 + x = C ∫ (
√2−1)2

0 Gn(y)x(y) dy;

thus, evaluating the required asymptotic, using inclusions (21) and applying Propo-
sition 1 result in the estimate µ(log 2) ⩽ 1 + C1/C0, where

C0 = −1 − lim
n→∞ log max
0⩽y⩽(
√2−1)2{
|Gn(y)|1/n}
,

C1 = 1 + lim
n→∞ log max
0⩽y⩽(
√2+1)2{
|Gn(y)|1/n}
.

One might now think to look for a polynomial Gn ∈ Z[y] of degree ⩽ n admitting
the minimum for the quantity C1/C0. Unfortunately, the (non-linear!) problem
seems to be very hard for being solved.
The idea of Rhin [15], [16], who introduced the above construction, was to ‘lin-
earize’ the optimization. He suggested to look for a polynomial G∗ ∈ Z[y] of degree
⩽ n
∗, say, which is close enough to the optimal polynomial choice in the problem

min
G∈Z[y]
1⩽deg G⩽n∗ max
0⩽y⩽(
√2−1)2{
|G(y)|1/n∗}
, (22)

and then take Gn(x) to be (G∗(x))⌊n/n∗⌋ for n suﬃciently greater than n
∗. For
instance, the fact (√2 − 1)2 ≈ 1/6 gives one the ﬁrst non-trivial approximation
G∗(y) = y6(6y − 1) in the problem.
The problem of minimizing the quantity (22) is deeply related to evaluating the
Z-transﬁnite diameter of the segment [0, (√2 − 1)2]. (The Z-transﬁnite diameter of
the set Y ⊂ R is deﬁned by the formula

tZ(Y ) = inf
G∈Z[x]
deg G⩾1 max
y∈Y {
|G(y)|1/ deg G}
,

see [1] for problems of computing the quantity.) This relationship is described in
[2]; there one can also ﬁnd the result µ(log 2) < 3.991, which may be achieved by

Irrationality measures of logarithms 12

the method. The latter estimate looks rather close to the inequality in Theorem 1;
however, it seems to be very ‘computer dependent’.
The above method may be used in situations `a la Section 2 as well. For example,
we may go back to simultaneous Z[i]-approximations to log a1 and log a2 and write
∫ a1

1 Gn
( (z − 1)2(z − a1)2(z − a2)2

z3
 ) dz
z = Bn log a1 − B′
n,
∫ a2

1 Gn
( (z − 1)2(z − a1)2(z − a2)2

z3
 ) dz
z = Bn log a2 − B′′
n

for any polynomial Gn(y) ∈ Z[y] of degree ⩽ n, where

dnBn, dnD3nB′
n, dnD3nB′′
n ∈ Z[i],

the integer d > 0 emanates from denominators to the numbers a1, a2, a
−1
1 , a
−1
2 . (Us-
ing the better inclusions achieved by Hata in [11] is in this case rather problematic.)
Unfortunately, this way does not look perspective, again due to the fact that we are
required to ‘linearize’ the appeared optimization problem.

3.3 Another generalization of the integral in (1)

On the other hand, we may perform integration in (1) by putting a general polyno-
mial of degree ⩽ 2n in the numerator of the integrand (in place of x
n(1 − x)n). Of
course, in this case the polynomial is required to satisfy some additional conditions.
Let a = c/d ∈ Q with pairwise coprime c and d > 0, and let ∆ be a common
multiple of the numbers c and d. Suppose that a polynomial Hn(z) ∈ Z[z] of degree
⩽ 2n may be represented in the form

Hn(z) =
 n∑

ν=0 Bν∆
n−νzν +
 2n∑

ν=n+1 Bνzν, where Bν ∈ Z, ν = 0, 1, . . . , 2n. (23)

(Clearly, for a = 2 the polynomial Hn(z) = (z − 1)n(z − 2)n has the desired form.)
Then for the integral

I(n) = (1 − a) ∫ 1

0
 Hn(d − d(1 − a)x)
dn(1 − (1 − a)x)n+1 dx

we deduce

I(n) =
 n∑

ν=0 Bν∆
n−νdν−n(1 − a) ∫ 1

0 (1 − (1 − a)x)ν−n−1 dx

+
 2n∑

ν=n+1 Bνdν−n(1 − a) ∫ 1

0 (1 − (1 − a)x)ν−n−1 dx

=
 n−1∑

ν=0 Bν∆
n−νdν−n a
ν−n − 1
n − ν − Bn log a −
 2n∑

ν=n+1 Bνdν−n 1 − a
ν−n

ν − n ,

Irrationality measures of logarithms 13

hence I(n) · Dn ∈ Z log a + Z.

In general, having a set of k rational numbers aj = cj/d for j = 1, . . . , k, we
suppose that the polynomial Hn(z) ∈ Z[z] of degree ⩽ 2n has representation (23)
with ∆ being a multiple of the numbers c1, . . . , ck, d. Then setting

I(n; aj) = (1 − aj) ∫ 1

0
 Hn(d − d(1 − aj)x)
dn(1 − (1 − aj)x)n+1 dx, j = 1, . . . , k, (24)

we obtain

I(n; aj) · Dn = −Bn log aj + Anj ∈ Z log aj + Z, j = 1, . . . , k,

again simultaneous approximations to log a1, . . . , log ak. (In fact, the choice

Hn(z) = ∆
2n(z − 1)⌊β0n⌋(z − a1)⌊β1n⌋ · · · (z − ak)⌊βkn⌋

where βj = αj/α for j = 0, 1, . . . , k, gives us exactly the same approximations as in
Section 2. The case β1 = · · · = βk was previously treated in [15] and [17].)
Finding a suitable polynomial Hn(z) for a given set of the numbers a1, . . . , ak
is very similar to that of Section 3.2. The change of variable zj = d − d(1 − aj)x
in the integrals (24) (hence, integrating then a simpler expression over the segment
[d, daj]) leads to the problem of ﬁnding a polynomial Hn(z) ∈ Z[z] of degree ⩽ 2n
with expansion (23) such that the quantity

max
z∈Z
 {∣
∣
∣
∣Hn(z)
z
 ∣
∣
∣
∣
1/n}, Z =
 k⋃

j=1
[d, daj],

is as small as possible. The algorithmic solution to this optimization problem by
means of the LLL-algorithm was recently proposed by Q. Wu [20]. This gives one
a machinery to produce fairly good estimates for linear forms in the logarithms of
rational numbers.

3.4 Measure for log 3

To derive a nice irrationality measure for log 3, Rhin constructs in [16] simultaneous
approximations to the logarithms of a1 = 2/3, a2 = 4/3 and use the following (very
complicated) choice of the polynomial (23):

Hn(z) = 214 · 32n+7 · (z − 1)⌊0.704324n⌋(
z − 2
3
 )⌊0.552418n⌋(z − 4
3
 )⌊0.447582n⌋

× (5z − 4)⌊0.109072n⌋(17z2 − 34z + 16)⌊0.038934n⌋(19z2 − 36z + 16)⌊0.054368n⌋

(a ‘justiﬁcation’ of the choice is done in [20]). By these means he proves

Irrationality measures of logarithms 14

Theorem 3. The irrationality exponent of any nonzero γ ∈ Q log 2+Q log 3 satisﬁes
the inequality µ(γ) < 8.616.

Further results in this direction (e.g., irrationality measures for log 5, log 7 etc.)
may be found in [20].

4 Concluding improvisations

Connections with the hypergeometric subject (indicated in Sections 1.1 and 2.4
above) could play a role in further improvements of the irrationality measures of
logarithms and related constants. For instance, Euler’s transform (see, e.g., [4],
Section 2.4, formula (1))

2F1
(
A, B
C
 ∣
∣
∣
∣ z) = 1
(1 − z)A · 2F1
(
A, C − B
C
 ∣
∣
∣
∣ −z
1 − z
 )

translates the value z = 1 − a = −1 of Section 1 into −z/(1 − z) = 1/2. This leads
to a 2F1-series with positive terms and makes possible the analytic evaluation of the
quantity (3) without using the integral representation (2)—we may get rid of the
integral (the idea belongs to K. Ball, cf. [21], the proof of Lemma 4). However,
other hypergeometric ingredients are required for real improvements.
We ﬁnd quite curious that Ramanujan’s formulae for π, in particular

∞∑

ν=0
 (1/4)ν(1/2)ν(3/4)ν
ν!3 (21460ν + 1123) · (−1)ν

8822ν+1 = 4
π ,

∞∑

ν=0
 (1/4)ν(1/2)ν(3/4)ν
ν!3 (26390ν + 1103) · 1
994ν+2 = 1
2π√2
 (25)

(see [14], equations (39) and (44)) and several others, might be used for constructing
good rational approximations to π and π√d, where d is a positive integer. Namely,
one can expect reasonable estimates for the corresponding irrationality measures
by constructing explicit Pad´e approximations (of either ﬁrst or second type) to the
functional system 1, f (z), f ′(z), f ′′(z), where

f (z) =
 ∞∑

ν=0
 (1/4)ν(1/2)ν(3/4)ν
ν!3 zν = 3F2
( 1
4 , 1
2, 3
4
1, 1
 ∣
∣
∣
∣ z).

The paper [13] provides Pad´e approximations to the homogeneous system f (z),
f ′(z), f ′′(z) (without 1) that are not enough for our purposes. Finally, we should
mention that a general result of A. Galochkin in [8] (proved by a proper variation of
Siegel’s method) yields the qualitative linear independence of the numbers 1, f (1/b),
f ′(1/b), and f ′′(1/b) for integers b satisfying |b| > b0, where the value of b0 is so huge
that b = −8822 and b = 994 in (25) do not suit.

Irrationality measures of logarithms 15

Acknowledgements. I thank G. Rhin kindly for introducing me to the subject of
transﬁnite diameters and their number-theoretic applications, in particular those
presented in Section 3. Special gratitude is due to P. Bundschuh, the fruitful dis-
cussions with whom during my long-term stay at Cologne University were crucial
for this writing. I thank J. Guillera for attracting my attention to Ramanujan-type
formulae and making me familiar with the manuscript [9], and J. Sondow for several
suggestions.

References

[1] F. Amoroso, “Sur le diam`etre transﬁni entier d’un intervalle r´eel,” Ann. Inst.
Fourier (Grenoble) 40, no. 4, 885–911 (1990)

[2] F. Amoroso, “f -transﬁnite diameter and number theoretic applications,” Ann.
Inst. Fourier (Grenoble) 43, no. 4, 1179–1198 (1993)

[3] G. E. Andrews, R. Askey and R. Roy, Special functions, Encyclopedia of Math-
ematics and its Applications 71 (Cambridge University Press, Cambridge 1999)

[4] W. N. Bailey, Generalized hypergeometric series, Cambridge Math. Tracts
32 (Cambridge University Press, Cambridge 1935); 2nd reprinted edition
(Stechert-Hafner, New York 1964)

[5] F. Beukers, “A rational approach to π,” Notes of a lecture held on the occasion
of Pi-day, on July 5, 2000 in Leiden, Nieuw Archief voor Wiskunde, no. 4,
17 pages (2000)

[6] N. Brisebarre, “Irrationality measures of log 2 and π/√
3,” Experiment. Math.
10, no. 1, 35–52 (2001)

[7] G. V. Chudnovsky, “On the method of Thue–Siegel,” Ann. of Math. (2) 117,
no. 2, 325–382 (1983)

[8] A. I. Galochkin, “Lower bounds for linear forms of values of G-functions,” Vest-
nik Moskov. Univ. Ser. I Mat. Mekh. [Moscow Univ. Math. Bull.] 51, no. 3,
23–29 (1996)

[9] J. Guillera, “Some closely related to Ramanujan formulas for π,” Unpublished
manuscript, 8 pages (December 2003)

[10] M. Hata, “Legendre type polynomials and irrationality measures,” J. Reine
Angew. Math. 407, no. 1, 99–125 (1990)

[11] M. Hata, “Rational approximations to π and some other numbers,” Acta Arith.
63, no. 4, 335–349 (1993)

Irrationality measures of logarithms 16

[12] M. Huttner, “On linear independence measures of some abelian integrals,”
Kyushu J. Math. 57, no. 1, 129–157 (2003)

[13] Yu. V. Nesterenko, “Pad´e–Hermite approximants of generalized hypergeometric
functions,” Mat. Sb. [Russian Acad. Sci. Sb. Math.] 185, no. 10, 39–72 (1994)

[14] S. Ramanujan, “Modular equations and approximations to π,” Quart. J. Math.
Oxford Ser. 2 45, 350–372 (1914); Collected Papers of Srinivasa Ramanujan,
eds. G. H. Hardy, P. V. Sechu Aiyar and B. M. Wilson, 23–39 (Cambridge Uni-
versity Press, Cambridge 1927); 2nd reprinted edition (Chelsea Publ., New York
1962)

[15] G. Rhin, “Sur l’approximation diophantienne simultan´ee de deux logarithmes
de nombres rationnels,” Diophantine approximations and transcendental num-
bers (Luminy 1982), Progress in Math. 31, 247–258 (Birkh¨auser, Boston 1983)

[16] G. Rhin, “Approximants de Pad´e et mesures eﬀectives d’irrationalit´e,”
S´eminaire de Th´eorie des Nombres (Paris 1985–86), ed. C. Goldstein, Progress
in Math. 71, 155–164 (Birkh¨auser, Boston 1987)

[17] G. Rhin and P. Toﬃn, “Approximants de Pad´e simultan´es de logarithmes,” J.
Number Theory 24, no. 3, 284–297 (1986)

[18] E. A. Rukhadze, “A lower bound for the approximation of ln 2 by rational num-
bers,” Vestnik Moskov. Univ. Ser. I Mat. Mekh. [Moscow Univ. Math. Bull.]
42, no. 6, 25–29 (1987)

[19] C. Viola, “Hypergeometric functions and irrationality measures,” Analytic
Number Theory ed. Y. Motohashi, London Math. Soc. Lecture Note Ser. 247,
353–360 (Cambridge University Press, Cambridge 1997)

[20] Q. Wu, “On the linear independence measure of logarithms of rational num-
bers,” Math. Comput. 72, no. 242, 901–911 (2002)

[21] W. Zudilin, “An elementary proof of Ap´ery’s theorem,” E-print
math.NT/0202159, 8 pages (2002)

Moscow Lomonosov State University
Department of Mechanics and Mathematics
Vorobiovy Gory, GSP-2
119992 Moscow, RUSSIA
E-mail : wadim@ips.ras.ru
URL: http://wain.mi.ras.ru/
