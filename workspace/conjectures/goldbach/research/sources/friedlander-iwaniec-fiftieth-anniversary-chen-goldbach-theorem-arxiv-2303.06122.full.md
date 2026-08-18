<!-- source: https://arxiv.org/pdf/2303.06122 | converted from PDF -->

arXiv:2303.06122v1  [math.NT]  10 Mar 2023
SIFTING FOR SMALL PRIMES
FROM AN ARITHMETIC PROGRESSION

J.B. FRIEDLANDER
∗ AND H. IWANIEC

On the ﬁftieth anniversary of Chen’s Goldbach theorem

Abstract: In this work and its sister paper [FI3] we give a new
proof of the famous Linnik theorem bounding the least prime in an
arithmetic progression. Using sieve machinery in both papers, we are
able to dispense with the log-free zero density bounds and the repulsion
property of exceptional zeros, two deep innovations begun by Linnik
and relied on in earlier proofs. 1 2

1. Introduction: A bit of history

The theorem of Yu.V. Linnik [L] asserts that, for integers q ⩾ 2,
(a, q) = 1, the least prime p ≡ a(mod q) satisﬁes

(1.1) pmin(q, a) ≪ qL,

where L and the implied constant are absolute.
The Riemann Hypothesis for Dirichlet L-functions L(s, χ), χ(mod q)
yields

(1.2) pmin(q, a) ≪ (q log q)2.

Linnik’s unconditional arguments make use of the Deuring-Heilbronn
phenomenon which describes a repulsion eﬀect of the exceptional zero
on all of the other zeros. Even if the exceptional zero does not exist,
the standard arguments, then and now, do not produce (1.1) with an
absolute constant L. To this end, Linnik established the so-called log-
free density bound
(1.3)∑

χ(mod q) #{ρ = β + iγ; L(ρ, χ) = 0, α ⩽ β < 1, |γ| ⩽ q} ≪ qc(1−α),

where c is an absolute constant. Moreover, in the presence of the
exceptional zero, say β1, with η1 = (1 − β1) log q being suﬃciently

∗ Supported in part by NSERC grant A5123.
1MSC 2020 classiﬁcation: 11M20, 11N05, 11N35, 11P32
2key words: sieve, small primes, Linnik theorem
1

2 Friedlander and Iwaniec

small, Linnik was able to expand the classical zero-free region, with
the result that all the other zeros ρ = β + iγ with |γ| ⩽ q satisfy

(1.4) (1 − β) log q ≫ log 1/η1

with an absolute implied constant. This is a quantitative form of the
Deuring-Heilbronn phenomenon. Later, Bombieri [B] combined these
two crucial estimations of Linnik into a single statement, namely that
the number of all zeros ρ = β + iγ with α ⩽ β < 1, |γ| ⩽ q of all L(s, χ)
other than β1 satisﬁes

(1.5) ∑

χ(mod q) N ∗(α, χ, q) ⩽ c1(1 − β1)(log q)qc(1−α),

where the constants c1, c are absolute. See Th´eor`eme 14 of [B] for
somewhat stronger statements. Bombieri employs the Turan power
sum method, essentially in place of the sieve.
Sieve ideas in conjunction with the molliﬁcation of L-functions con-
stitute the driving force of Linnik’s work. His arguments have been
reﬁned substantially over time with new innovative elements (partic-
ularly those of Heath-Brown), giving concrete values of L. Here are
some remarkable records:

L = 105 (Pan, 1957)
L = 80 (Jutila, 1977)
L = 20 (Graham, 1981)
L = 13.5 (Chen and Liu, 1989)
L = 5.5 (Heath − Brown, 1992)
L = 5.18 (Xylouris, 2009)

It is interesting that, if permitted the assistance of the exceptional
character χ1(mod q), one can accomplish a lot more for this problem
than with the Riemann Hypothesis. For example, we obtained (1.1)
with L = 2 − 1/55 under suitable conditions, see [FI1]. If one tries to
count primes p ≡ a(mod q) directly using the Riemann Hypothesis, by
means of the explicit formula

ψf (x; q, a) = ∑

n≡a(mod q) f (n/x)Λ(n)

= ˆf (1) x
ϕ(q) − 1
ϕ(q)
 ∑

χ̸=χ0 ¯χ(a) ∑

ρ ˆf (ρ)x
ρ

= ˆf (1) x
ϕ(q) + O(√
x log x)

SIFTING FOR SMALL PRIMES 3

with f smooth and compactly supported on (0, ∞), then one may
get (1.1) with L < 2 provided that there is a considerable cancella-
tion in the terms x
ρ as ρ runs over low-lying zeros ρ = β + iγ. One
actually expects that (1.1) holds with any L > 1. The distribution of
primes p ≡ a(mod q) in the vicinity of q is tricky; cf. [FG].
In these notes we do not attempt to obtain a reasonably small Linnik
constant L. In fact, at the end of the day we arrive at (1.1) with
the huge value L = 75, 744, 000. So, what motivates us to produce
this long proof of Linnik’s bound? Our ﬁrst reason is to demonstrate
how the sieve machinery can succeed in this problem when fueled by
neither the log-free density estimation nor the repulsion property of
the exceptional zero. However, we do appeal to the classical zero-free
region, speciﬁcally Lemma A1 with η = 1/657.
Moreover, these notes provide more details to our arguments in
Chapter 24 of [FI2]. To diversify a bit we treat the case of the ex-
ceptional zero by Selberg’s lower-bound sieve rather than by a combi-
natorial sieve. Of course, the results are essentially the same, but we
get nicer expressions. We have put the treatment of that case into a
separate note [FI3].
Our second incentive to produce these notes is the desire to ﬁx a
defect in the technical arrangements of the partial sums ψX(x; q, a) in
[FI2], a correction of which we have no other opportunity to publish due
to an AMS copyright issue. The required correction is embarrassing
but not diﬃcult. The subdivision there of n = pp1p2p3p4 ≡ a(mod q)
should have been made over the segments

(1.6) D 1
6 < p1, p2 < D 1
5 , x3 < p3 ⩽ 2x3, x4 < p4 ⩽ 2x4

rather than over xj < pj ⩽ 2xj for all j = 1, 2, 3, 4. That is, we should
not have put p1, p2 into dyadic segments as we did for p3, p4. However,
adjusting the existing arguments to the larger segments (1.6) is simple
with obvious modiﬁcations. The key diﬀerence appears in the factor
h(p/x) of (24.47) in [FI2] which needs to be changed to h(log p/ log x).
In other words, the ﬁrst primes p1, p2 should have been logarithmically
scaled. See how we proceed in Subsection 2.1 of these notes.

2. The linear beta-sieve

Let A = (an) be a ﬁnite sequence of real numbers an ⩾ 0, supported
on x < n ⩽ 2x, x large. Our goal is to estimate

4 Friedlander and Iwaniec

(2.1) S(A) = ∑

p ap.

It is well understood that, due to the parity barrier, one cannot obtain
a positive lower bound for S(A) within the basic sieve methods. In
this section we reduce the problem for primes to that for products of
ﬁve primes, that is to the estimation of

(2.2) S5(A) = ∑

p
 ∑

p1
 ∑

p2
 ∑

p3
 ∑

p4 app1p2p3p4,

where the pj run over speciﬁc segments, short in the logarithmic scale.
We do not lose the correct order of magnitude. Note that n = pp1p2p3p4,
which we call a prime quintet, consists of integers with an odd number
of prime factors.
Let P (z) denote the product of primes p < z in some set P. Sieve
methods are capable of producing upper and lower bounds for the sift-
ing function

(2.3) S(A, z) = ∑

(n,P (z))=1 an,

but only in a limited range. The basic assumption needed for sifting is
that the congruence sums

(2.4) Ad = ∑

n≡0(mod d) an

can, on average over d, be well-approximated by a simple model g(d)X,
where g(d) is multiplicative with 0 ⩽ g(p) < 1 and X is ﬁxed. This
requirement means that the error terms in

(2.5) Ad = g(d)X + rd

are relatively small. In particular, we must choose X ∼ A1. The
probability of seeing an with (n, P (z)) = 1 is given by the product

(2.6) V (z) = ∏

p|P (z)

(1 − g(p))

and sieve methods produce bounds of the true order of magnitude

(2.7) S(A, z) ≍ XV (z)

SIFTING FOR SMALL PRIMES 5

provided that we can control the error terms rd. In practice, we can do
so only for moduli up to some level y ⩽ x. We need, say,

(2.8) R(y) = ∑

d<y
d|P (z)
 |rd| ⩽ XV (z)(log y)−1.

Let Ad be the subsequence of A of elements an with n ≡ 0(mod d).
We start from the combinatorial identity

(2.9) S(A, z) = S−(A, z) + S2(A, z) + S4(A, z) + . . .

which is derived by a process of inclusion-exclusion; see (12.10) and
(12.11) for the linear beta-sieve in [FI2]. This holds for z = √y with

(2.10) S−(A, z) = ∑

d|P (z) λ−
d Ad

where λ−
d are the sieve weights. We have

(2.11) S4(A, z) = ∑∑∑∑

p4<p3<p2<p1 S(Ap1p2p3p4, p4)

where the prime variables of summation are restricted by two inequal-
ities

(2.12) p1p3
2 < y, p1p2p3p3
4 ⩾ y.

The other Sn(A, z) are deﬁned similarly but we are going to drop them
due to positivity. Actually, we also discard some parts of (2.12). Specif-
ically we take

(2.13) x 1
6 < pj < x 1
5 , j = 1, 2, 3, 4

and an with n = pp1p2p3p4, p prime only. We assume x 4
5 < y < x,
so that the restrictions (2.12) hold automatically because x ⩽ n ⩽ 2x.
Observe that p is the largest prime in the prime quintet n = pp1p2p3p4;
speciﬁcally we have

(2.14) x 1
5 < p < 2x 1
3 .

Let Q(A) be the following speciﬁc choice for (2.2)

(2.15) Q(A) = ∑

p
 ∑

p1
 ∑

p2
 ∑

p3
 ∑

p4 app1p2p3p4

where all prime variables are distinct and pj run freely over the seg-
ment (2.13) without ordering. The variable p is restricted only by

6 Friedlander and Iwaniec

the support of A = (an) because (2.14) is redundant. We obtain the
following combinatorial inequality:

(2.16) S(A, z) ⩾ S−(A, z) + 1
24Q(A), if y1/4 ⩽ z ⩽ y1/2.

The linear beta-sieve in Chapter 12 of [FI2] requires the density
function g(d) to satisfy the upper bound

(2.17) ∏

w⩽p<z
(1 − g(p))−1 ⩽ log z
log w (1 + ℓ
log w )

for every 2 ⩽ w < z with some constant ℓ. In our case, we shall
verify (2.17) with an absolute constant ℓ. Then we have

(2.18) S−(A, z) ⩾ (
f1(s) + O(
(log y)−1/6))
XV (z) − R(y)

where s = (log y)/ log z and f1(s) = 2e
γs−1 log(s − 1), if 2 ⩽ s ⩽ 4.
We take z = √y, so s = 2, f1(2) = 0 and (2.18) gives nothing positive.
Therefore, we are left with the following lower bound

(2.19) S(A, √
y) ⩾ 1
24Q(A) + O(
XV (√y)(log y)−1/6))
.

On the other hand, S(A) = S(A, √
2x) is close to S(A, √
y) if the
admissible level of distribution y is close to x in the logarithmic scale.
Put

(2.20) y = x
θ, 4
5 < θ < 1.

The diﬀerence

(2.21) S(A, √
y) − S(A, √
2x) = ∑

√y⩽p<√
2x S(Ap, p),

counting an over prime duos pp′ can be estimated successfully by any
upper-bound sieve method. Our sieve conditions (2.8) and (2.17) allow
us to apply (12.12) of [FI2] for every subsequence Ap. We replace X
in (2.5) by g(p)X, rd by rpd and choose the level of distribution for Ap
to be y/p. We obtain S(Ap, p) ⩽ S(Ap, y/p) and

S(Ap, y/p) ⩽ g(p)V (y/p)X{
F1(1) + O(
(log y)−1/6)} + ∑ |rpd|,

where F1(1) = 2e
γ and the sum of the error terms rpd runs over d|P (p),
d ⩽ y/p. By (2.17) we have

V (y/p) ⩽ V (y) log y
log(y/p)(1 + O( 1
log y )).

SIFTING FOR SMALL PRIMES 7

Next, we apply (5.47) of [FI2] as follows:

∑

√y<p<√
2x g(p)(log y/p)−1 < ∫ √2x

√y (log y/w)−1 d log w
log w + O(
(log y)−2)

= (log 1
2θ − 1 + O(1/ log y))
(log y)−1.

Moreover, we write by Mertens’ formula,

V (y) log y = e
−γH(
1 + O(1/ log y))

where

(2.22) H = H(y) = ∏

p<y
(
1 − g(p))(1 − 1
p )−1.

Inputting the above estimates into (2.21) and (2.19), we obtain the
following result.
Theorem 2.1: Suppose (2.17) holds for every 2 ⩽ w < z ⩽ √2x
with an absolute constant ℓ and the remainder R(y) of level (2.20)
satisﬁes (2.8). Then we have the following inequality.

(2.23) S(A) ⩾ 1
24Q(A) − 2HX
log y log 1
2θ − 1 + O(
X(log y)−7/6)
,

where Q(A) is given by (2.15) and the implied constant is absolute.
Remarks: We shall succeed to show that Q(A) ⩾ cHX(log y)−1

with an absolute constant c > 0, but it will be a small constant because
we took account of only a small portion of the combinatorial decom-
position (2.9). Nevertheless, we still obtain a positive lower bound for
S(A) because θ will be very close to 1.
From now on we are interested in an arithmetic progression. Let q
be large, (a, q) = 1 and x ⩾ q6. We take A = (an) with

(2.24) an = f (n/x), if n ≡ a(mod q)

and an = 0 otherwise. Here, f (u) ⩾ 0 is a smooth function supported
on 1 ⩽ u ⩽ 2 with

(2.25) ˆf (0) = ∫ f (u)du > 0.

Our sequence A = (an) satisﬁes the sieve conditions with

(2.26) X = ˆf (0)x/q

and density function

(2.27) g(d) = d−1 if (d, q) = 1, g(d) = 0 if (d, q) ̸= 1.

8 Friedlander and Iwaniec

Hence, the product (2.22) is constant, namely H = q/ϕ(q) because
y ⩾ q. Now, S(A) becomes

(2.28) πf (x; q, a) = ∑

p≡a(mod q) f (p/x)

and (2.23) yields
(2.29)

πf (x; q, a) ⩾ 1
24 Q(A) − ˆf (0)(
log 1
2θ − 1) 2x
ϕ(q) log y + O(x
q (log x)−7/6).

The error terms are absolutely bounded and R(y) ≪ y so we choose

(2.30) y = x/q(log x)3 = x
θ

and check that the remainder satisﬁes (2.8).
Now Q(A) in (2.23) for our sequence (2.24) reads as

(2.31) Q(A) = ∑

p
 ∑∑∑∑

pp1p2p3p4≡a(mod q)
x1/6<pj<x1/5, j=1,2,3,4
 f (pp1p2p3p4/x).

At this point we can predict the limit of our output. Deﬁnitely, we
cannot do better than the asymptotic formula for ϕ(q)Q(A):
∑∑∑∑ ∫ f (vp1p2p3p4/x)(log v)−1dv

∼ ˆf (0)x ∑∑∑∑(p1p2p3p4)−1(log(x/p1p2p3p4))−1

∼ ˆf (0) x
log x
 ∫ ∫ ∫ ∫ (1 − u1 − u2 − u3 − u4)−1 du1
u1
 du2
u2
 du3
u3
 du4
u4

< ˆf (0) 5x
log x(log 6
5 )4,

where θ
6 < uj < θ
5 , Hence, if the lower bound in (2.29) is positive, then

5
24 (
log 6
5 )4 > 2 log 1
2θ − 1, so 1 − θ < 6 · 10−5.

This shows that we cannot produce p ≡ a(mod q) smaller than q105/6.

2.1 Technical preparations:
Before detecting the congruence n = pp1p2p3p4 ≡ a(mod q) by char-
acters, we take advantage of positivity to separate the variables p3, p4
from the crop function f (n/x). To this end we subdivide p3, p4 into
short segments

(2.32) C < p3 ⩽ λC, D < p4 ⩽ λD

SIFTING FOR SMALL PRIMES 9

with

(2.33) P ⩽ C, D ⩽ λ−1P 6/5, P = x
1/6.

The constant λ is just slightly larger than 1. The complete inter-
val (2.13) is covered by the union of the segments (2.32) with

C = λmP, D = λnP, 0 ⩽ m, n ⩽ (log P )/5 log λ.

We want to replace f (pp1p2p3p4/x) by f (pp1p2CD/x). To this end
we introduce the function g(u) = uf ′(u) and apply the following:
(2.34)

f (pp1p2p3p4/x) = f (pp1p2CD/x) + ∫ p3p4/CD

1 g(pp1p2CDt/x)t
−1dt

⩾ f (pp1p2CD/x) − ∫ λ2

1 |g(pp1p2CDt/x)|t
−1dt

= f (pp1p2CD/x) − h(pp1p2CD/x),

where

(2.35) h(u) = ∫ λ2

1 |g(ut)|t
−1dt = u ∫ λ2

1 |f ′(ut)|dt ≪ log λ.

Note that h(u) is supported on λ−2 ⩽ u ⩽ 2 and is small if λ is very
close to 1.
We put

(2.36) Qf (C, D) = ∑

p
 ∑∑∑∑

pp1p2p3p4≡a(mod q)
P <p1,p2<P 6/5
C<p3⩽λC, D<p4⩽λD
 f (pp1p2CD/x).

Similarly, we deﬁne Qh(C, D) as in (2.36) with f (u) replaced by h(u).
Summing over C = λmP , D = λnP , in the segment (2.33), we get

(2.37) Q(A) ⩾ ∑

C
 ∑

D
 (Qf (c, D) − Qh(C, D))
.

The case of Qh(C, D) can be treated as Qf (C, D), but we can also
estimate Qh(C, D) directly by applying the Brun-Titchmarsh theorem
in the variable p. Let τ be a quantity O(1/ log P ), not always the same
one. We ﬁnd

∑

p≡α(mod q) h(pp1p2CD/x) < ˆh(0) (2 + τ )x
ϕ(q) (log x/qp1p2CD)−1

10 Friedlander and Iwaniec

where qpp1p2CD < qP 24/5 = qx
4/5 ⩽ x
29/30. Hence

(2.38) Qh(C, D) < ˆh(0) (2 + τ )
ϕ(q) (log 6
5)2( log λ
log P )2 30x
log x

and the contribution of Qh(C, D) to (2.37) is ≪ ˆh(0)x/ϕ(q) log x, which
is insigniﬁcant because ˆh(0) = ∫ h(u)du = (1 − λ−2) ∫ u|f ′(u)|du is
small for λ close to 1. Actually, this contribution will be discarded
entirely after rounding up (or down) the constants in the other contri-
butions.
 3. Dual sums: primes versus zeros

Let ρ = β + iγ run over complex numbers with 0 ⩽ β ⩽ 1 and
|γ| ⩽ T . For T ⩾ 1 and P ⩾ 3 we put

(3.1) V = max
|γ|⩽T
 ∑

ρ
 (
1 + (1 − β) log P )−1(1 + (γ − t)2(log P )2)−1.

Lemma 3.1: For arbitrary complex numbers ap supported on primes
in the segment P ⩽ p ⩽ P 6/5 we have
(3.2)∑

ρ P 5
2 (β−1)∣
∣ ∑

p app−ρ∣
∣
2 ⩽ (1387V + O(NT (log P )−4)) ∑

p |ap|2p−1

where N = N(T ) denotes the number of ρ’s counted with multiplicity
and the implied constant is absolute.
Proof: The assertion (3.2) is, by duality, equivalent to the statement
that the inequality
(3.3)∑

P ⩽p⩽P 6/5
 ∣
∣ ∑

ρ zρp 1
2 −ρP 5
4 (β−1)∣
∣2 ⩽ (1387V + O(NT (log P )−4)) ∑

ρ |zρ|2

holds true for all complex numbers zρ.
For the proof of the dual inequality (3.3) we majorize the summa-
tion over p by attaching the weights k(log n/ log P )Λ(n)/ log P where
k(u) ⩾ 0 is a twice diﬀerentiable function supported on 1
4 ⩽ u ⩽ 5
4
with k(u) ⩾ 1, if 1 ⩽ u ⩽ 6
5. Then, the left side of (3.3) is bounded by

(3.4) ∑

ρ
 ∑

ρ′ |zρzρ′||K(s)|P 5
4 (σ−2)

where s = ¯ρ + ρ
′ = σ + it with σ = β + β′ ⩽ 2, t = γ′ − γ, |t| ⩽ 2T and

K(s) = ∑

n k( log n
log P ) Λ(n)
log P n
1−s.

SIFTING FOR SMALL PRIMES 11

We evaluate K(s) using the Prime Number Theorem in the form

ψ(x) = ∑

n⩽x Λ(n) = x + ∆(x) with ∆(x) ≪ x(log x)−4.

We write

K(s) = (log P )−1 ∫ k( log x
log P )x
1−sd(x + ∆(x)) = K1(s) + K0(s),

say, where K1(s) is the contribution of the main term x and K0(x) is
the contribution of the error term ∆(x).
We have two expressions for K1(s):

K1(s) = ∫ k(u)P (2−s)udu = Z −2 ∫ k′′(u)P (2−s)udu,

where Z = (2 − s) log P . By the inequality

min(A, B/C) ⩽ (A + B)(1 + C)−1

we obtain

|K1(s)| ⩽ (1 + |Z|2)−1 ∫ (|k(u)| + |k′′(u)|)
P (2−σ)udu.

After multiplying this by P 5
4 (σ−2) as in (3.4) we ﬁnd that P has expo-
nent ( 5
4 − u)(σ − 2) so we can replace σ = β + β′ by its upper bound
1 + min(β′, β) = 1 + β♭, say. We get

|K1(s)|P 5
4 (σ−2) ⩽ (1 + |Z|2)−1 ∫ 1

0
 (k( 5
4 − u) + |k′′( 5
4 − u)|)
P −(1−β♭)udu.

Now we choose the particular crop function

k( 5
4 − u) = 41(sin πu)2 = 41
2 (1 − cos 2πu)

getting ∫ 1

0 = 41 ∫ 1

0
 (
(sin πu)2 + 2π2| cos 2πu|)
P −(1−β♭)udu.

For the last integral we have two easy estimations:

(1 + 2π2)/(1 − β♭) log P

and ∫ 1

0
 ((sin πu)2 + 2π2| cos 2πu|)
du = 1
2 + 4π.

12 Friedlander and Iwaniec

The minimum of these two bounds is less than 1 + 2π2 + 1
2 + 4π =
2(π + 1
2 )(π + 3
2 ) divided by 1 + (1 − β♭) log P . Hence we see that the
main term contributes to (3.4) at most

1387 ∑

ρ
 ∑

ρ′ |zρzρ′|(
1 + (1 − β♭) log P )−1(1 + (γ − γ′)2(log P )2)−1.

Finally, applying the inequality 2|zρzρ′| ⩽ |zρ|2 +|zρ′|2 we get the bound
that agrees with the leading term in (3.3).
To estimate K0(s) we integrate by parts and proceed as follows:

K0(s) = −(log P )−1 ∫ ∆(P u)dk(u)P (1−s)u

= − ∫ (k(u)(1 − s) + k′(u)/ log P )∆(P u)P (1−s)udu

≪ T (log P )−4 ∫ 5/4

1/4 P (2−σ)udu ≪ T (log P )−4P 5
4 (2−σ).

Hence the contribution to (3.4) of the error term ∆(x) is of order
bounded by T (log P )−4 times the quantity

(∑

ρ |zρ|)2 ⩽ N ∑

ρ |zρ|2.

The result obtained agrees with the ﬁnal term of (3.3). Our proof of
of (3.3) is thus complete and hence so, by duality, is that of (3.2).

Corollary 3.2: Let ρ run over the zeros of L(s, χ) with |γ| ⩽ log q
and β∗ denote the maximum of all the β’s. Let P ⩾ q6, X ⩾ P 5/2.
Then, for any complex numbers ap supported on P ⩽ p ⩽ P 6/5 we
have

(3.5) ∑

ρ X β−1∣
∣ ∑

p app−ρ∣
∣2 ⩽ 2082(
XP −5/2)(β∗−1) ∑

p |ap|2p−1.

Proof: Apply the inequality X β−1 ⩽ P 5
2 (β−1)(
XP −5/2)(β∗−1). Then
use (3.2) and Corollary A3. Moreover, NT ⩽ T 2 log qT ≪ (log q)3 so
the error term in (3.2) is absorbed by rounding up 1387 · 3001/2000 <
2082 .
 SIFTING FOR SMALL PRIMES 13

4. Prime trios with a character

Throughout (ap), (bp) are sequences of numbers 0 ⩽ ap, bp ⩽ 1
supported on P ⩽ p ⩽ P 6/5. Our goal is to estimate the character sum

(4.1) T (X, χ) = ∑

p
 ∑

p1
 ∑

p2 χ(pp1p2)ap1bp2f (pp1p2/X) log p.

Here, X is at our disposal; it is not related to that in (2.5). We assume

(4.2) P 5/2 ⩽ X ⩽ P 4.

The crop function f (y) ⩾ 0 is supported on 1 ⩽ y ⩽ 2 with |f (j)(y)| ⩽ 1
for 0 ⩽ j ⩽ 4. These conditions imply that the Mellin transform
satisﬁes the bound

˜f (s) = ∫ f (y)ys−1dy ≪ (1 + |s|)−4

and that
 | ˜f (s)| ⩽ | ˜f (1)| = ∫ f (y)dy = ˆf (0)

when 0 ⩽ Re s ⩽ 1.
For the principal character χ = χ0 we have

(4.3) T (X; 1) = ( ˆf (0) + τ )XAB

where

(4.4) A = ∑

p app−1, B = ∑

p bpp−1.

Note that A, B ⩽ log 6
5 + τ and that equality holds if ap = bp = 1. In
several places we shall use the estimates 1
31 < (log 6
5)2 < 1
30 , so that we
can drop the term with τ = O(1/ log P ).

Lemma 4.1: For χ ̸= χ0 we have

(4.5) |T (X; χ)| ⩽ 380 ˆf (0)X β∗P 5
2 (1−β∗)

where

(4.6) β∗ = max{β; ρ = β + iγ, L(ρ, χ) = 0, |γ| ⩽ log q}.

Proof: We use the approximate explicit formula
∑

p χ(p)f (p/Y ) log p = − ∑

|γ|⩽T ˜f (ρ)Y ρ + O(
Y β∗(log q)−2)

14 Friedlander and Iwaniec

with T = log q and Y = X/p1p2, getting

T (X; χ) = − ∑

|γ|⩽T ˜f (ρ)X ρ(∑

p χ(p)app−ρ)(∑

p χ(p)bpp−ρ)

+ O(
X β∗P 12
5 (1−β∗)(log q)−2).

Hence (4.5) follows from (3.5) by Cauchy’s inequality and rounding up
2082 · log 6
5 < 380.

Next, for a real character χ ̸= χ0 we are going to approximate
T (X; χ) by −T (X; χ0). Put

(4.7) λ(p) = (1 ∗ χ)(p).

This is unrelated to our constant λ > 1 introduced earlier. Note that
1 + χ(pp1p2) ⩽ λ(p) + λ(p1) + λ(p2). Hence, T (X; χ) + T (X; χ0) is
bounded by

(4.8) ∑

p
 ∑

p1
 ∑

p2
 (λ(p) + λ(p1) + λ(p2))ap1bp2f (pp1p2/X) log p.

The terms with λ(p1) contribute to (4.8) exactly (4.3), but with the
coeﬃcient ap1 replaced by λ(p1)ap1, similarly with λ(p2).
To estimate the contribution of the terms with λ(p), we ﬁrst execute
the summation over p2 in (4.8). Note that log p < (2 + τ ) log p2 because
p2 ⩾ P and p ⩽ 2XP −2 ⩽ 2P 2. Moreover, if P > q20 we have
p ⩾ XP −12/5 ⩾ P 1/10 > q2. Hence, the contribution of λ(p) in (4.8) is
bounded by

(2+τ ) ∑

q2<p⩽2P 2 λ(p) ∑

p1
 ∑

p2 ap1f (pp1p2/X) log p2 ⩽ (2+τ ) ˆf (0)XAδ(2P 2)

where

(4.9) δ(z) = ∑

q2<p⩽z λ(p)p−1.

Interchanging ap with bp we can replace A above by (AB) 1
2 . Adding up
the three contributions we see that T (X; 1) + T (X; χ) is bounded by

( ˆf (0) + τ )X{AλB + ABλ + 2(AB) 1
2 δ(2P 2)}

where Aλ = ∑

p λ(p)app−1 ⩽ δ(P 6/5) ⩽ 12
5 (1 − β) log P

and similarly Bλ ⩽ 12
5 (1 − β) log P , see (A5). Hence, we conclude:

SIFTING FOR SMALL PRIMES 15

Lemma 4.2: For χ real, χ ̸= χ0, P ⩾ q20 and P 5/2 ⩽ X ⩽ P 4 we
have

(4.10) 0 ⩽ T (X; 1) + T (X; χ) ⩽ 12
5 ˆf (0)X(1 − β) log P

where β is any real zero of L(s, χ).
Remarks: For example, β < 0 could be a trivial zero, but then (4.10)
would not be interesting. The constant 12/5 in (4.10) comes by a
rounding up of 2 · 2 · ( 6
5 + 2) log 6
5 = 2.3337 . . .. Combining (4.10)
with (4.3), one obtains another bound for T (X; χ) for χ real, in addi-
tion to (4.5). This bound is better than that given in (4.5) if L(s, χ)
has a real zero β very close to 1.

5. Prime quintets in arithmetic progressions

Throughout, we shall assume the conditions of Section 4. In addition
to (ap), (bp) supported on P ⩽ p ⩽ P 6/5 we consider two sequences (cp),
(dp) of numbers 0 ⩽ cp, dp ⩽ 1 which are supported on short segments
C < p ⩽ λC, D < p ⩽ λD respectively; see (2.32). Note that the
choice

(5.1) X = x/CD

satisﬁes X ⩽ xP −2 = P 4 = x
2/3 and X > xP −12/5 = P 18/5 = x
3/5.
Our goal is to estimate the sums

(5.2) Q(x; q, a) = ∑

p
 ∑∑∑∑

pp1p2p3p4≡a(mod q) ap1bp2cp3dp4f (pp1p2/X) log p

with the same crop function f (y) as in Section 4. We have

(5.3) Q(x; q, a) = 1
ϕ(q)
 ∑

χ(mod q) ¯χ(a)T (X; χ)C(χ)D(χ)

where T (X; χ) was deﬁned in (4.1) and

(5.4) C(χ) = ∑

p χ(p)cp, D(χ) = ∑

p χ(p)dp.

Similarly, we deﬁne C(1), C(λ), D(1), D(λ) which will appear later.
We also introduce

(5.5) ω(C) = ∑

C<p⩽λC p−1, S(C) = ∑

C<p⩽λC λ(p)p−1.

Similarly, we deﬁne ω(D), S(D).
Note that C(1) ⩽ λCω(C), D(1) ⩽ λDω(D). Moreover, if cp = dp =
1, then we have lower bounds C(1) ⩾ Cω(C), D(1) ⩾ Dω(D).

16 Friedlander and Iwaniec

We have treated T (X; χ) in Section 4; see (4.3), (4.5) and (4.10).
The last estimate (4.10) applies to the real character χ ̸= χ0. We
compared T (X; χ) to −T (X; 1) apart from a small quantity of order
X(1 − β) log P . Here, we make a similar comparison of C(χ)D(χ) to
C(1)D(1). For every p, p′ we have 0 ⩽ 1 − χ(pp′) ⩽ λ(p) + λ(p′), so

(5.6) 0 ⩽ C(1)D(1) − C(χ)D(χ) ⩽ C(λ)D(1) + C(1)D(λ)

⩽ λ2CD(
S(C)ω(D) + ω(C)S(D))
.

Now, we return to the formula (5.3). The principal character χ0(mod q)
yields the main contribution (see (4.3))

(5.7) Q0(X) = 1
ϕ(q) T (X; 1)C(1)D(1) = ( ˆf (0) + τ ) X
ϕ(q) ABC(1)D(1).

There may be a real character χ1 ̸= χ0 for which its contribution

(5.8) Q1(X) = χ1(a)
ϕ(q) T (X; χ1)C(χ1)D(χ1)

requires special attention. The other characters contribute to (5.3) in
total at most

(5.9) Q
∗(X) = 1
ϕ(q) Tmax(X)(∑

χ | ∑

p χ(p)cp|2) 1
2 (∑

χ | ∑

p χ(p)dp|2) 1
2

where Tmax(X) denotes the maximum of |T (X, χ)| over all χ other than
χ0 or χ1 (if the latter exists). For these non-exceptional characters we
have

(5.10) β∗ ⩽ 1 − η/ log q

by Lemma A1, where η is an absolute constant to be speciﬁed later.
Hence, Lemma 4.1, together with the bounds P 5/2X −1 < x
5/12−3/5 <
x
−1/6 yield

(5.11) |Tmax(X)| ⩽ 380 ˆf (0)Xx
−η/6 log q.

Next, we apply Lemma A5 with C ⩾ P , so C/q ⩾ P/q ⩾ P 19/20

and (5.9) yields

(5.12) ϕ(q)Q
∗(X) ⩽ 801 ˆf (0)( log λ
log P )2x
1−η/6 log q.

Here, 801 is obtained after increasing the number 380 · 2 · 20/19 = 800,
which allows us to replace λ − 1 by log λ. If the exceptional character
χ1 exists, which means that L(s, χ1) has a real zero

(5.13) β1 > 1 − η/ log q,

SIFTING FOR SMALL PRIMES 17

we evaluate its contribution by comparing ϕ(q)Q1(X) to

(5.14) ϕ(q)Q11(X) = −χ1(a)T (X; 1)C(1)D(1).

We get
(5.15)
ϕ(q)|Q1(X) − Q11(X)| ⩽ (T (X; 1) + T (X; χ1))
C(1)D(1)

+ T (X; 1)(
C(1)D(1) − C(χ1)D(χ1))

⩽ 2
5 ˆf (0)xω(C)ω(D)(1 − β1) log x

+ 1
30 ˆf (0)x
(ω(C)S(D) + ω(D)S(C))

⩽ 1
30 ˆf (0)xΩ(C, D)

by (4.10), (5.6) and (4.3), in which AB < 1
30. Here

(5.16) Ω(C, D) = 12ω(C)ω(D)(1−β1) log x+ω(C)S(D)+ω(D)S(C).

At some point (see (6.6)) we shall have to sum over C, D in the
segment (2.33). Note that

∑

C ω(C) = ∑

P <p⩽P 6/5 p−1 = log 6
5 + τ,

∑

C S(C) = ∑

P <p⩽P 6/5 λ(p)p−1 ⩽ δ(x
1/5)

with δ(x
1/5) ⩽ 2
5(1 − β1) log x by Lemma A4. The same estimates hold
for the sums over D. Hence,

(5.17) ∑

C
 ∑

D Ω(C, D) ⩽ 11
20(1 − β1) log x,

where 11/20 comes from rounding up 12(log 6
5)2 + 4
5 log 6
5 .
If χ1 is exceptional we can still use Lemma 4.1 which gives

|T (X; χ1)| ⩽ 380 ˆf (0)Xx
−(1−β1)/6

in place of (5.11) . Hence (5.8) gives the bound

(5.18) ϕ(q)Q1(X) ⩽ 380 ˆf (0)( log λ
log P )2x
1−(1−β1)/6

in place of (5.12), which is still useful if the exceptional zero β1 is not
very close to 1.

18 Friedlander and Iwaniec

6. Three estimations of Q(A)

Recall that Q(A) is the sum over prime quintets n = pp1p2p3p4
in the aritmetic progression n ≡ a(mod q) counted with the smooth
weight f (n/x); see (2.31), (2.37), (2.38). Now we use the results of the
previous two sections to estimate Q(A) in terms of the zeros of L(s, χ).
We start from (5.2) and (5.3) which we have estimated by:

(6.1) Q(x; q, a) ⩾ Q0(X) − Q
∗(X) − Q1(X);

see (5.7), (5.9), (5.8), with X = x/CD. The ﬁrst part Q0(X) comes
from the principal character. The second part, which comes from
those non-principal characters other than the exceptional one, satis-
ﬁes the bound (5.12) which is suﬃciently strong because η is an ab-
solute constant, which can be taken to be not very small. The last
part Q1(X) comes from the exceptional character χ1 and it satisﬁes
the bound (5.18), which is good enough only if the exceptional zero β1
is extremely close to 1. In case it is extremely close, then Q1(X) is
comparable to Q11(X); see (5.15). Therefore, we need a second option,
in addition to the direct one (5.18) for the estimatiom of ϕ(q)Q1(X).
This one is provided by

(6.2) ϕ(q)Q1(X) ⩽ −χ1(a)T (X; 1)C(1)D(1) + 1
30 ˆf (0)xΩ(C, D);

see (5.14), (5.15). Hence, if χ1 exists then, using (5.7) for Q0(X),

(6.3) ϕ(q)Q(x; q, a)) ⩾ ˆf (0)xW(C, D)

where we have two choices:
(6.4)

W(C, D) = 1
31 ω(C)ω(D)−801( log λ
log P )2x
−η/6 log q−380( log λ
log P )2x
(1−β1)/6

and
(6.5)

W(C, D) = 1
31 (1−χ1(a))ω(C)ω(D)−801( log λ
log P )2x
−η/6 log q− 1
30 Ω(C, D).

In these, we obtained the fraction 1/31 on rounding down (log 6/5)2 >
1/31. If χ1 does not exist then W(C, D) is given by (6.4) without the
last term. Recall that the number of pairs C, D is (log P )2(5 log λ)−2.
Introducing the factor log p ⩽ log(2x
1/3) into (2.36) we get

(6.6) ϕ(q)Qf (C, D) log(2x
1/3) ⩾ ϕ(q)Q(x; q, a) ⩾ ˆf (0)xW(C, D).

Note we have omitted the negative contribution of Qh(C, D) in (2.37)
because it is very small for λ close to 1 and so is absorbed by the
margin we obtained in rounding up the constants in (6.4), (6.5). Next,

SIFTING FOR SMALL PRIMES 19

summing over C and D in (6.4), (6.5) and using (5.17), we obtain
respectively two lower bounds
1
961 − 801
25 x
−η/6 log q − 380
25 x
−(1−β1)/6

and 1
961 (1 − χ1(a)) − 801
25 x
−η/ log q − 11
600(1 − β1) log x.

We simplify these bounds by assuming

(6.7) x ⩾ q80/η

which makes the middle term smaller than one twentieth of the ﬁrst
term 1/961 (check that 801/25e
80/6 < 1/19270 < 1/961 · 20). Hence,
we are left with two lower bounds

(6.8) 321ϕ(q)Q(A) log x ⩾ ˆf (0)x{ 19
20 − 14608x
(1−β1)/6}

and

(6.9) 321ϕ(q)Q(A) log x ⩾ ˆf (0)x{ 19
20 − χ1(a) − 18(1 − β1) log x}.

If the exceptional character χ1 does not exist, then (6.8) holds without
the negative exceptional term. We have proved the following result.
Lemma 6.1: Suppose that all the zeros ρ = β + iγ of every L(s, χ)
satisfy

(6.10) β ⩽ 1 − η/ log q(|γ| + 1),

except possibly for one simple real zero β1 of L(s, χ1) with a real char-
acter χ1. Let x ⩾ q80/η. Then we have

(6.11) ϕ(q)Q(A) ⩾ ˆf (0)x/350 log x,

subject to any one of the following conditions:

(6.12) χ1 does not exist,

(6.13) χ1 exists and x ⩾ e
80/(1−β1)

(6.14) χ1 exists, χ1(a) = −1 and x ⩽ e
1/18(1−β1).

Proof: The exceptional term in (6.8), subject to (6.13), is smaller
than 14608e
−80/6 < 1/42. Check that 19/20 − 1/42 > 321/350. This
shows that (6.11) holds subject to (6.13). The other two cases are clear.

Remark. The true expected value of ϕ(q)Q(A) was computed just
after (2.31) so our lower bound (6.11) is about one third that size.

20 Friedlander and Iwaniec

7. Primes in an arithmetic progression

Finally, we proceed to the estimation of the sum over primes (2.28).
To this end, we appeal to the sieve inequality (2.29) which transfers
the task to that for prime quintets apart from a small piece

(7.1) ˆf (0)(
log 1
2θ − 1 ) 2x
θϕ(q) log x

accounting for prime duos, which needs to be subtracted. Recall that
y = x/q(log x)3 = x
θ. We make the contribution in (7.1) smaller than
1
25Q(A) by choosing x ⩾ qM with a suﬃciently large number M. In
view of the lower bound (6.11), any M satisfying

2M
M − 1 log M
M − 3 < 1
25 · 350
will suﬃce. We check that M = 52600 is good enough. Applying (2.29)
and (6.11) and checking that 1/24 - 1/25 = 350/210000, we ﬁnd:

Lemma 7.1: If x ⩾ q52600 and one of the conditions (6.12), (6.13), (6.14)
holds, then

(7.2) ϕ(q)πf (x; q, a) ⩾ ˆf (0)x/210000 log x.

In addition to (7.2), we have the lower bound

(7.3) ϕ(q)πf (x; q, a) ⩾ L(1, χ1)V (χ1)x/168

if χ1(a) = 1 and q43 ⩽ x ⩽ e
1/4(1−β1). This bound is derived in [FI3] by
quite diﬀerent arguments using Selberg’s lower bound sieve. Combin-
ing (7.2) and (7.3) we establish:
Theorem 7.2: Let q be suﬃciently large and (a, q) = 1. We have

(7.4) pmin(q, a) ⩽ qL with L = 75744000.

Proof: If the exceptional zero does not exist then (7.2) produces (7.4)
with L = M = 52600. If the exceptional zero β1 exists and satisﬁes
(1 − β1) log q ⩾ 1/18 · 52600, then (7.2) subject to (6.13) together
with (7.3) subject to x ⩽ e
1/4(1−β1) yield (7.4) with L = M = 52600.
In the opposite case (1 − β1) log q < 1/18 · 52600, we use (7.2) subject
to (6.13), yielding (7.4) with L = 80 · 18 · 52600 = 75744000.

Remarks: We assumed that q is suﬃciently large and q80/η ⩽
q52600,that is the non-exceptional zeros satisfy (6.10) with η ⩾ 1/675.5
On the other hand, the old result of R.J. Miech [Mi] provides the much

SIFTING FOR SMALL PRIMES 21

larger constant η = 1/20. The current record, given speciﬁcally for
|t| ⩽ 1, is due to Xylouris [Xy] and stands at η = .440.

Appendix

In this section we select some classical results about the zeros of
Dirichlet L-functions and character sums over prime numbers.

Lemma A1: For every χ(mod q), all zeros ρ = β + iγ of L(s, χ)
satisfy β ⩽ 1 − η/ log q(1 + |γ|),
except possibly for one real simple zero β1 of L(s, χ1) with one real
character χ1(mod q). Here, η is an absolute positive constant.

We need the above inequality with η = 1/657. We do not need the
log-free zero density estimation nor the Deuring-Heilbronn repulsion
property. In place of these, we quickly prove the following inequality.

Lemma A2: For s = σ + it with σ > 1 we let

V (s, χ) = ∑

ρ
 (1 + 1 − β
σ − 1 )−1(1 + ( γ − t
σ − 1 )2)−1,

where ρ = β + iγ runs over the zeros of L(s, χ) with β > 0. If χ ̸= χ0
we have V (s, χ) ⩽ 1 + σ − 1
2 log cq|s|

where c > 1 is an absolute constant.

Proof: We can assume χ is primitive. Then (see e.g. (5.24) of [IK])

L
′

L (s, χ) = −1
2 log q
π − 1
2 Γ′

Γ ( sχ
2 ) + B(χ) + ∑

ρ
 ( 1
s − ρ + 1
ρ)

where sχ = s + (1 + χ(−1))/2, Γ′(s)/Γ(s) = log s + O(1) and

Re B(χ) = − ∑

ρ Re 1
ρ.

Hence, ∑

ρ Re 1
s − ρ = 1
2 log q|s| + Re L
′

L (s, χ) + O(1),

∣
∣ L
′

L (s, χ)∣
∣ ⩽ −ζ ′

ζ (σ) = 1
σ − 1 + O(1).

Now Lemma A2 follows easily from the inequality

Re 1
s − ρ = σ − β
(σ − β)2 + (γ − t)2 ⩾ 1/(σ − 1)(1 + 1 − β
σ − 1 )(1 + ( γ − t
σ − 1 )2)
.

22 Friedlander and Iwaniec

Corollary A3: For q suﬃciently large and |t| ⩽ log q we have
∑

ρ
 (1 + (1 − β) log q)−1(1 + (γ − t)2(log q)2)−1 ⩽ 3
2 + 1
2000.

Lemma A4: Let χ(mod q) be a real character and β a real zero of
L(s, χ). Then, for x ⩾ q2, q suﬃciently large, we have
∑

q2⩽p⩽x

(
1 + χ(p))p−1 ⩽ 2(1 − β) log x.

Proof: See the text between Proposition 24.1 and Corollary 24.2 of
[FI2].

Lemma A5: If C ⩾ q2 and |cp| ⩽ 1 for C < p ⩽ λC, then
∑

χ(mod q)

∣
∣ ∑

C<p⩽λC χ(p)cp∣
∣2 ⩽ (2 + τ )(λ − 1)2C 2(log C)−1(log C/q)−1

where λ > 1 is a ﬁxed number and τ ≪ (log C)−1 .
Proof: The left side is estimated by the Brun-Titchmarsh theorem
as follows:

ϕ(q) ∑∑

p′≡p(mod q) cp′¯cp ⩽ ϕ(q) ∑

C<p⩽λC
(π(λC; q, a) − π(C; q, a))

⩽ (2 + τ )(λ − 1)C(log C/q)−1(π(λC) − π(C))

⩽ (2 + τ )(λ − 1)2C 2(log C/q)−1(log C)−1.

Remark: Our treatment of character sums over prime quintets re-
sembles a multiplicative version of the circle method for the ternary
Goldbach problem. The prime trios alone would perform this part, but
the extra two prime factors are needed to avoid the log-free zero den-
sity bound (1.3) and the repulsion property of the possible exceptional
zero. There is a possibility to arrange a combinatorial identity of sieve
type by means of which we could work with two primes and one almost
prime rather than with prime quintets.

References

[B] Bombieri E. Le Grand Crible dans la Th´eorie Analytique des Nombres.
Ast´erisque 18, 2`eme ed., Paris: Soc. Math. France, 1987/1974
[FG] Friedlander J.B. Granville. Limitations to the equi-distribution of primes I.
Ann. of Math., 1989, 129: 363–382
[FI1] Friedlander J.B. Iwaniec H. Exceptional characters and prime numbers in
arithmetic progressions. Inter. Math. Res. Notices, 2003, 37: 2033–2050
[FI2] Friedlander J.B. Iwaniec H. Opera de Cribro. Colloquium Publications 57,
Providence: Amer. Math. Soc., 2010

SIFTING FOR SMALL PRIMES 23

[FI3] Friedlander J.B. Iwaniec H. Selberg’s sieve of irregular density. Acta Arith.,
to appear
[IK] Iwaniec H. Kowalski E. Analytic Number Theory, Colloquium Publications
53, Providence: Amer. Math. Soc., 2004
[L] Linnik Yu.V. On the least prime in an arithmetic progression I. The basic
theorem. Mat. Sbornik, 1944, 15/57: 39–178
[Mi] Miech R.J. A number theoretic constant. Acta Arith., 1969, 15: 119–137
[Xy] Xylouris T. On the least prime in an arithmetic progression and estimates
for the zeros of Dirichlet L-functions. Acta Arith., 2011, 150: 65–91

Department of Mathematics, University of Toronto
Toronto, Ontario M5S 2E4, Canada (frdlndr@math.toronto.edu)

Department of Mathematics, Rutgers University
Piscataway, NJ 08903, USA (iwaniec@comcast.net)
