<!-- source: https://arxiv.org/pdf/1511.03409 | converted from PDF -->

arXiv:1511.03409v2  [math.NT]  17 Dec 2015Explicit Chen’s theorem∗†

Tomohiro Yamada

Abstract

We show that every even number > exp exp 36 can be represented
as the sum of a prime and a product of at most two primes.

1 Introduction

In a letter of 1742 to Euler, Goldbach conjectured that every integer greater
then 2 is the sum of three primes including 1, which is equivalent that every
even integer N ≥ 4 is the sum of two primes (not including 1) or of the
form p + 3 with p prime.

Euler replied that this is equivalent to the statement that every even
integer N ≥ 4 is the sum of two primes.

An weaker conjecture is that every odd integer N ≥ 7 can be represented
as the sum of three primes. Vinogradov[19][20][14, Chapter 8] showed that
every suﬃciently large odd integer can be represented as the sum of three
primes. His student K. Borozdin[1] proved that 3315 is large enough. Chen
and Wang[4] reduced the constant to exp exp 11.503, Chen and Wang[5]
to exp exp 9.715 and Liu and Wang[12] to exp 3100. Deshouillers, Eﬃnger,
te Riele and Zinoviev[6] showed that the Generalized Riemann Hypothesis
gives the weaker conjecture. Recently, Harald Helfgott claimed to have
proved three prime conjecture unconditionally.

Contrastly, the ordinary Goldbach’s conjecture is still unsolved. A well-
known partial result is the theorem of Chen[2][3], who proved that every
suﬃciently large even number can be represented as the sum of a prime
and the product of at most two primes. Ross[16] gave a simpler proof.

∗2010 Mathematics Subject Classiﬁcation: 11N35.
†Key words and phrases: Linear sieve, Rosser-Iwaniec sieve.

1

1 INTRODUCTION 2

Nathanson[14, Chapter 10] gave another proof based on Iwaniec’s unpub-
lished lecture note. However, they did not give an explicit constant above
which every even number can be represented as p + P2. The purpose of this
paper is to give an explicit constant for Chen’s theorem; every even number
> exp exp 36 can be represented as the sum of a prime and a product of at
most two primes. Indeed, we shall prove the following result:

Theorem 1.1. Let π2(N) denote the number of representations of a given
integer N as the sum of a prime and a product of at most two primes. If
N is an even integer > exp exp 36, then we have

π2(N) > 0.007UN N
log2 N , (1)

where
 UN = 2e
−γ ∏

p>2
 (
1 − 1
(p − 1)2
 ) ∏

p>2,p|N
 p − 1
p − 2 . (2)

Our argument is based on Nathanson’s one, which used Rosser-Iwaniec
linear sieve to give upper and lower bounds for numbers of sifted primes,
combining explicit error terms for the disribution of primes in arithmetic
progressions and explicit Rosser-Iwaniec linear sieve, which are given in
other papers by the author [21][22].

However, possible existence of a Siegel zero prevents from making the
size of error term in Rosser-Iwaniec linear sieve explicit. There are two
cases — the exceptional modulus is large or small. If the exceptional mod-
ulus is small, then we can see that the contribution of the Siegel zero can be
absorbed into error estimates concerning the distribution of primes in arith-
metic progression (see Lemma 2.5). In the other case, when the exceptional
modulus is large, it is easy to avoid a possible Siegel zero in the argument
to estimate upper bounds since we can exclude a prime dividing the excep-
tional modulus from sifting primes. However, we cannot directly avoid a
possible Siegel zero in the argument to estimate lower bounds. In order to
overcome this obstacle, we use a variant of inclusion-exclusion principle and
both upper bound and lower bound sieves, as performed in Section 5. Thus
we can obtain explicit bounds.

So that, our argument can be divided into four parts: error estimates
involving the number of primes in arithmetic progressions based on esti-
mates in [21], explicit error terms in Rosser-Iwaniec linear sieve shown in
[22], upper bounds and lower bounds for various sets of sifted primes, and
the ﬁnal conclusion.

For calculations of constants, we used PARI-GP. Our script is available
from http://tyamada1093.web.fc2.com/math/files/prim0009pari.txt

2 PRELIMINARY RESULTS 3

2 Preliminary results

In this section, we shall introduce some preliminary results, involving ex-
plicit estimates for various quantities involving the number of primes in
arithmetic progressions.

We begin by noting that, in this paper, θ denotes a quantity with |θ| ≤ 1
taking diﬀerent values at each occurence. It can easily be distinguished from
Chebyshev functions.

We shall introduce a partial-sum type inequality.

Lemma 2.1. Let f (x) be a monotone function deﬁned in w ≤ x ≤ z, c(n)
be an arithmetic function satisfying
∑

x≤n<y c(n) ≤ g(y) − g(x) + E (3)

for some constant E whenever w ≤ x ≤ y < z. Then we have

∑

w≤n<z c(n)f (n) ≤ ∫ z

w f (t)g′(t)dt + E max{f (w), f (z)}. (4)

Proof. This is Lemma 1, (ii) in [8, p.p. 30–31].

We shall often use the following explicit estimates.

Lemma 2.2. For n ≥ 3,
 ω(n) < 1.3841 log n
log log n . (5)

For x ≥ 2973, ∏

p≤x
 (
1 − 1
p
 ) = e
−γ

log x
 (
1 + θ
5 log2 x
 ) . (6)

Moreover, we have, for any real numbers a > 1 and b > 10372,

∑

a≤p<b
 1
p < log log b − log log a + 1
5 log2 a + 8
15 log3 a (7)

Proof. (5) is Theorem 11 of [15]. (6) and (7) follow from Theorem 6.12 and
Theorem 6.10 in [7] respectively.

2 PRELIMINARY RESULTS 4

Henthforth we shall give explicit estimates for various quantities involv-
ing the error terms concerning to the number of primes in arithmetic pro-
gressions. Let Ef (x; k, l) denote the error function f (x; k, l) − f (x)
ϕ(k) for f = π
(i.e. f (x) = π(x) and f (x; k, l) = π(x; k, l)), θ or ψ.

Lemma 2.3. Let x > X1 = exp exp 11.7 and k < log10 x be an integer.
Let E0 = 1 and β0 denote the Siegel zero modulo k if it exists and E0 = 0
otherwise. Then we have
ϕ(q)
x |Eψ(x; k, l)| < 0.000012
log8 x + E0 x
β0−1

β0 . (8)

Proof. This is Theorem 1.1 of [21] with (α1, α, Y0) = (10, 8, 11.7).

Deﬁne Π(s, q) = ∏

χ (mod q) L(s, χ) and let R0 = 6.397 and R1 = 2.0452 · · · .
Theorem 1.1 of Kadiri[11] states that the function Π(s, q) has at most one
zero ρ = β + it in the region 0 ≤ β < 1 − 1/R0 log max{q, q |t|}, which
must be real and simple and induced by some nonprincipal real primitive
character ̃χ (mod ̃q) with 987 ≤ ̃q ≤ x. Moreover, Theorem 1.3 of [11] im-
plies that, for any given Q1, such zero satisﬁes β < 1 − 1/2R1 log Q1 except
possibly one modulus below Q1. Henceforth let k0 be a such a modulus if it
exists and call this modulus and the corresponding character to be excep-
tional. Furthermore, we set δ = 7/5 and deﬁne k1 = k0 if k0 ≥ logδ x and
k1 = 0 otherwise, so that k1 | k is equivalent to both k0 | k and k0 ≥ logδ x
hold.

Corollary 2.4. Assume that x is a real number > X2 = exp exp 32, x2 =
e−100x
log4 x , K0 = logδ x2 and let Q1 = log10 x2. Moreover, let k1 = k0 if k0 ≥ K0
and k1 = 0 otherwise, If k is a modulus ≤ Q1 not divisible by k1, then we
have ϕ(k)
x |Eπ(x; k, l)| < e
−14

log4 x. (9)

Proof. We begin by observing that β0 ≤ 1−π/0.4923K 1/2
0 log2 K0. It is clear
that either k0 ∤ k or k0 < logδ x2 holds if there exists the Siegel zero. In the
case k0 ∤ k, it is clear that β0 < 1 − 1/2R1 log Q1 = 1 − 1/20R1 log log x2 <
1 − π/0.4923K 1/2
0 log2 K0. In the other case k0 < K0, Theorem 3 of [12]
gives β0 ≤ 1 − π/0.4923k1/2
0 log2 k0 ≤ 1 − π/0.4923K 1/2
0 log2 K0.

Let y be an arbitrary real number with x2 < y ≤ x. Since 1/2 < β0 ≤
1 − π/0.4923K 1/2
0 log2 K0, we can see that yβ0−1

β0 < e−15

log3 y from x > X2 if the
Siegel zero exists. Thus, by Lemma 2.3,

ϕ(q)
y
 ∣
∣
∣
∣ψ(y; k, l) − y
ϕ(k)
 ∣
∣
∣
∣ < 1.1e
−15

log3 y . (10)

2 PRELIMINARY RESULTS 5

The rough estimate |ψ(y; k, l) − θ(y; k, l)| < y 1
2 log2 y/ log 2 is enough to
give ϕ(k)
y
 ∣
∣
∣
∣θ(y; k, l) − y
ϕ(k)
∣
∣
∣
∣ < 1.2e
−15

log3 y . (11)

Since
 ϕ(k) ∣
∣
∣
∣θ(y)
y − 1∣
∣
∣
∣ < 0.1e
−15

log3 y (12)

for y > X2 by Theorem 2 of [18], we have

ϕ(k)
y |Eθ(y; k, l)| < 1.3e
−15

log3 y . (13)

Now, partial summation yields

Eπ(x; k, l) = Eπ(x2; k, l) + Eθ(x; k, l)
log x − Eθ(x2; k, l)
log x2 + ∫ x

x2
 Eθ(t; k, l)
t log2 t dt, (14)

and
 ϕ(k) ∫ x

x2
 Eθ(t; k, l)
t log2 t dt < 1.3e
−15

1 − 5
log x2
 ∫ x

x2
 1
log5 t
 (
1 − 5
log t
) dt

= 1.3e
−15

1 − 5
log x2
 ( x
log5 x − x2
log5 x2
 ) . (15)

Hence we obtain

|Eπ(x; k, l)| < 1.3e
−15x
log4 x + 2.6e
−15x2
log4 x2 + 1.4e
−15 ( x
log5 x − x2
log5 x2
 ) . (16)

The right-hand side does not exceed e−14

log4 x if x > X2, which proves the
corollary.

Lemma 2.5. Assume that x is a any real number > X2. Let x2, Q1, k1 be
as in Corollary 2.4 and Q = √x2
log10 x2 . Then we have

∑

k≤Q,k1∤k µ2(k) max
l (mod k) |Eπ(x; k, l)| < e
−8x
log3 x. (17)

Proof. Let y be an arbitrary real number with x2 < y ≤ x. We begin by
showing that
 ∑

k≤Q,k1∤k µ2(k) max
l (mod k) |Eψ(y; k, l)| < 1.9e
−9y
log2 y . (18)

2 PRELIMINARY RESULTS 6

As in the proof of Corollary 2.4, either k0 | k or k0 ≥ K0 holds if the
Siegel zero exists. Moreover, in the case k0 ≥ K0, we have k1 = k0.

If k1 = k0 or there exists no Siegel zero, we can apply Theorem 1.4 of
[21] with A = 10 but Q1 in this theorem replaced by Q1 in Corollary 2.4.
Let c0, c1, C be the constants deﬁned by

c0 = 2 13
2
9π log 2
 ( 1
3 + 3
2 log 2
 ) (2 + log(log 2/ log(4/3))
log 2
 ) √ ψ(113)
113 , (19)

c1 = ∏

p
 (1 + 1
p(p − 1)
 ) = ζ(2)ζ(3)
ζ(6) (20)

and C = 0.0000128, as in Theorem 1.4 of [21]. We note that c0 < 48.83215
and c1 < 1.9436. Now, since Q1 = log10 x2 ≤ log10 y, Theorem 1.4 of [21]
gives ∑

k≤Q,k1∤k µ2(k) max
l (mod k) |Eψ(y; k, l)|

< c0c1(2 + e
−800)y

log 11
2 y + 2c0c1y log 9
2 y
Q1 + c2
1(C + e
−17)y(1 + 10 log log y)
4 log6 y . (21)

Since we can see that Q1 > (1 − e
−20) log10 x, we have
∑

k≤Q,k1∤k µ2(k) max
l (mod k) |Eψ(y; k, l)|

< c0c1(4 + e
−19)y

log 11
2 y + c2
1(C + e
−17)y(1 + 10 log log y)
4 log6 y

< 379.64067y

log 11
2 y < 1.9e
−9y
log2 y
 (22)

and therefore (18) holds.

Next, consider the case k0 < K0. Now we see that
∑

k≤Q µ2(k) max
l (mod k) |Eψ(y; k, l)|

<
 ( ∑

1≤m≤Q
 1
ϕ(m)
 ) ∑

1<q≤Q
 ∣
∣
∣
∣
∣
∣
 ∑∗

χ (mod q) ψ(y, χ)
∣
∣
∣
∣
∣
∣ . (23)

Similarly to the proof of Theorem 1.4 of [21], we have

∑∗

χ (mod k0) |ψ(y, χ)| < (C + e
−17)y
log6 y + yβ0−1

β0 , (24)

2 PRELIMINARY RESULTS 7

where β0 denotes the Siegel zero modulo k0. Theorem 3 of [12] gives β0 ≤
1 − π/0.4923k1/2
0 log2 k0 ≤ 1 − π/0.4923K 1/2
0 log2 K0 and we see that

y
1− π

0.4923K 1
2
0 log2 K0

1 − π

0.4923K 1
2
0 log2 K0
 < e
−11.5y
log3 y log log y . (25)

A similar argument to the proof of Theorem 1.4 of [21] using this inequality
instead of (52) in [21] gives (18). Similarly to (53), for each k ≤ Q1, we
have
∑∗

χ (mod k) |ψ(y, χ)| < (C0 + e
−18)y
log7 y + e
−11.5y
log3 y log log y < 2e
−12y
log3 y log log y (26)

and, similarly to (54) in [21], we obtain

∑

q≤Q1,q0∤q
 1
ϕ(q)
 ∑∗

χ (mod q) |ψ(x, χ)| ≤ 2.01c1e
−12y(1 + 10 log log y)
log3 y log log y < 1.95e
−9y
log3 y .

(27)
This gives

∑

k≤Q,k1∤k µ2(k) max
l (mod k) |Eψ(y; k, l)| < 1.95c1e
−9y
2 log2 y < 1.9e
−9y
log2 y . (28)

Now we estimate Eπ(x; k, l). We begin by observing that partial sum-
mation gives

Eπ(x; k, l) = Eπ(x2; k, l) + Eθ(x; k, l)
log x − Eθ(x2; k, l)
log x2 + ∫ x

x2
 Eθ(t; k, l)
t log2 t dt. (29)

We would like to majorize the four terms in the right-hand side.

From the argument in the proof of Theorem A. 17 of [14], we see that∑

k≤Q 1
ϕ(k) < c1(1 + log Q) < c1
2 log x and therefore (18) yields

∑

k≤Q,k1∤k µ2(k) max
l (mod k) |Eθ(y; k, l)|

< ∑

k≤Q,k1∤k µ2(k) max
l (mod k) |Eψ(y; k, l)|

+ 2y 1
2 log2 y
log 2
 ∑

k≤Q,k1∤k
 µ2(k)
ϕ(k)

< 1.9e
−9y
log2 y + c1y 1
2 log2 y log x
log 2
 (30)

2 PRELIMINARY RESULTS 8

for x2 ≤ y ≤ x. Hence we obtain
∑

k≤Q µ2(k) max
l (mod k) |Eθ(x; k, l)| < 2e
−9x
log2 x , (31)

∑

k≤Q µ2(k) max
l (mod k) |Eθ(x2; k, l)| < 1.9e
−9x2
log2 x2 + c1x 1
2 log3 x
log 2 (32)

and
∫ x

x2
 maxl (mod k) |Eθ(t; k, l)|
t log2 t dt < ∫ x

x2
 1.9e
−9

log4 t + c1 log x

t 1
2 log 2 dt

< 1
1 − 1
5 log x2
 ∫ x

x2
 1.9e
−9

log4 t
 (
1 − 4
log t
) dt + 2c1x 1
2 log x

= 1.9e
−9

1 − 1
5 log x2
 ( x
log4 x − x2
log4 x2
 ) + 2c1x 1
2 log x

< 2e
−9x
log4 x .
 (33)

Moreover, we use a trivial estimate Eπ(x2; k, l) ≤ x2 to obtain

∑

k≤Q µ2(k) max
l (mod k) Eπ(x2; k, l) < x2 ∑

k≤Q
 µ2(k)
ϕ(k) < c1x2 log x. (34)

Combining (31)-(34), we have

∑

k≤Q,k1∤k µ2(k) max
l (mod k) |Eπ(x; k, l)| < e
−8x
log3 x. (35)

This proves the lemma.

Now we introduce a extention of the previous lemma, which plays an
important role in our argument to avoid the exceptional modulus.

Lemma 2.6. Let x > X2 = exp exp 36 and Q, k1 as in the previous lemma.
If k divides k1, then we have
∑#

d≤Q/k µ2(k) max
l (mod k)
 ∣
∣
∣
∣π(x; kd, l) − π(x; k, l)
ϕ(d)
 ∣
∣
∣
∣

< e
−8x
log3 x,
 (36)

where d runs over integers such that k1 ∤ kd if k ̸= k1.

3 AN EXPLICIT ROSSER-IWANIEC LINEAR SIEVE 9

Proof. We have

ψ(x; kd, l) − ψ(x; k, l)
ϕ(d) = ∑

χ1,χ2
 1
ϕ(kd)
 ∑

χ1 (mod k),
χ2̸=χ0,d (mod d)
 ¯χ1(l) ¯χ2(l)ψ(x; χ1χ2),

(37)
where χ0,d denotes the trivial character modulo d, and observe that there
exists no character χ1χ2 appearing in this sum induced from the exceptional
one (mod k1) since χ2 is nontrivial and either k1 ∤ kd or k = k1 holds. Now,
similarly to (18), we have

∑#

d≤Q/k µ2(q) max
l (mod kd)
 ∣
∣
∣
∣ψ(y; kd, l) − ψ(y; k, l)
ϕ(d)
 ∣
∣
∣
∣

< 1.9e
−9y
log3 y
 (38)

for x2 < y ≤ x. The remaining argument essentially repeats the proof of
the previous lemma.

3 An explicit Rosser-Iwaniec linear sieve

In this section, we introduce an explicit version of Rosser-Iwaniec linear
sieve. We use the following notation: A is a ﬁnite set of integers, Ωp a set of
congruent classes modulo p and ρ(p) be a multiplicative arithmetic function
which takes zero if Ωp is empty,

Ap =A ∩ Ωp, Ad = ⋂

p|d Ap, r(d) = |Ad| − ρ(d)
d |A| ,

S(A, P ) =
 ∣
∣
∣
∣
∣
∣
A − ⋃

p|P Ap
∣
∣
∣
∣
∣
∣ , V (P ) = ∏

p|P
 (
1 − ρ(p)
p
 )

and

P (z) = ∏

p<z p.

Now we can state that the sieve problem is to estimate S(A, P ) under the
condition that r(d) is small. A special case is the case ∏

p≤x(1 − ρ(p)/p) ∼
C log x for some constant C, which is called linear.

4 FRAMEWORK OF OUR SIEVE ARGUMENT 10

Using Selberg’s sieve, Jurkat and Richert[10] gave upper and lower bounds
for the linear sieve. Using Rosser’s combinatorial argument in his un-
published manuscript, Iwaniec[9] improved their upper and lower bounds.
Moreover, an explicit version of Rosser-Iwaniec linear sieve is given in Chap-
ter 9 in [14] although it requires an additional condition. In [22], the author
gave another explicit version of Rosser-Iwaniec linear sieve which can be
applied in more general cases. Here we shall introduce Theorem 1.2 in [22].
The assumption in this theorem is satisﬁed, for instance, when A is the set
of odd integers of the form aq + b with a, b ﬁxed coprime integers and q odd
prime and Ωp consists at most one congruent class modulo p for each prime
p. In particular, A can be taken to be sets of integers the form N − q with
N even and q odd prime, which we shall consider in the following sections.

Theorem 3.1. Assume that ρ(p) ≤ p/(p − 1) and ρ(2) = 0. Then, for
every D, s > 0, we have

S(A, P (D 1
s )) > X
 (
V (P (D 1
s )) − 2
 ( f1(s)
log D + 255.84406

log 3
2 D
 ))
 − |R(D, P (z))|

(39)
and

S(A, P (D 1
s )) < X
 (
V (P (D 1
s )) + 2
 ( F1(s)
log D + 298.87013

log 3
2 D
 ))
+|R(D, P (z))| .

(40)
where f1(s), F1(s) are functions such that F1(s) = 2e
γ − s for 0 ≤ s ≤ 3 and

F ′
1(s) = − f (s − 1)
s − 1 for s ≥ 3,

f ′
1(s) = − F1(s − 1)
s − 1 for s ≥ 2, (41)

and R(D, P ) = ∑

d|P,d≤D |µ2(d)r(d)|.

4 Framework of our sieve argument

We use the following notation. As we assumed in Theorem 1.1, let N be
an even integer ≥ X2 = exp exp 36. Let z = N 1
8 and y = N 1
3 . Then
z > exp exp 33 and y > exp exp 34.

We shall consider the set A = {N − p : p ≤ N, p ∤ N}. If A contains
at least one prime, then N could be represented by the sum of two primes.
We set Ωp to be the congruent class 0 (mod p), so that Aq = {m : q | m}.

4 FRAMEWORK OF OUR SIEVE ARGUMENT 11

Moreover, let r(d) = |Ad| − |A|
ϕ(d) and rk(d) = |Akd| − |Ak|
ϕ(d) denote error terms.
Clearly we have |A| = π(N) − ω(N) and |Ak| = π(N; k, N) − ω(N; k, N),
where ω(n; q, a) denotes the number of prime factors of n which is equivalent
to a (mod q).

As Chen and other authors did, we introduce the other set B = {N −
p1p2p3 : z ≤ p1 < y ≤ p2 ≤ p3, p1p2p3 < N, (p1p2p3, N) = 1} and obtain the
following lower bound, which is Theorem 10.2 in [14].

Lemma 4.1.

π2(N) > S(A, P (z)) − 1
2
 ∑

z≤q<y S(Aq, P (z)) − 1
2S(B, P (y)) − 2N 7
8 − 2N 1
3 .

(42)

So that, it suﬃces to give an lower bound for S(A, P (z)) and upper
bounds for S(B, P (y)) and S(Aq, P (z)) for each primes q with z ≤ q < y.

We set x2 = e−100N
log4 N , which coincides x2 in Section 2 with x = N, K0 =
logδ x2 and let Q1 = log10 x2. Moreover, we set k0 to be the exceptional
modulus deﬁned as in Section 2 and k1 = k0 if k0 ≥ K0 and k1 = 0
otherwise,

Let q1 > q2 > · · · > ql be all prime factors of k1 and mj = q1q2 · · · qj, A
(j) =
Amj and P (j)(x) = ∏

p<x,p∤N,p̸=q1,q2,...,qj p for j = 0, 1, 2, . . . , l. We note
that m0 = 1, A
(0) = A, P (0)(x) = P (x). Moreover, we write for brevity
V (x) = V (P (x)) amd V (j)(x) = V (P (j)(x)).

As in the proof of Theorem 10.3 in [14], we deduce from (6) that

V (j)(x) = U (j)
N
log x
 (
1 + θ
5 log2 x
 ) (
1 + 8θ log x
x
 ) (43)

for j = 0, 1, . . . , l and x ≥ z, where

U (j)
N = 2e
−γ ∏

p>2
 (
1 − 1
(p − 1)2
 ) ∏

p>2,p|N mj
 p − 1
p − 2 , (44)

so that U (0)
N = UN . Moreover, we have

l < 1.3841 log(10 log N)
log log(10 log N) < e log log N
log log log N (45)

by (6). Moreover, since k1 ≥ logδ x2 > 3 × 5 × 7 × 11 × · · · × 53, we have

q1 ≥ max{59, 2 + log log N} (46)

4 FRAMEWORK OF OUR SIEVE ARGUMENT 12

and therefore U (1)
N ≤ UN q − 1
q − 2 ≤ UN (1 + ǫ0(N)), (47)

where ǫ0(N) = 1
max{57,log log N }.

We can easily see that, for any d | P (j)(x), rmj (d) = ∣
∣
∣A
(j)
d ∣
∣
∣ − |A(j)|
ϕ(d) . We
have the following estimates.

Lemma 4.2. We have |A| > N
log N . (48)

For j = 0, 1, . . . , l − 1, we have

|r(mj)| < e
−8N
log3 N (49)

and |r(ml)| < 0.19N
log2.3 N . (50)

Moreover, for any integer k dividing k1, we have

∑#

d<Q/k µ2(kd) |rk(d)| < 1.1e
−8N
log3 N , (51)

where Q = x2
log10 x2 and d runs over integers such that k1 ∤ kd if k ̸= k1.

Proof. We recall that |A| = π(N) − ω(N) and (48) easily follows from (5)
and Theorem 1, (3.1) of [17] or Theorem 6.9, (6.5) of [7].

We observe that Corollary 2.4 gives (49) for j = 0, 1, . . . , l−1. Moreover,
Brun-Titchmarsh’s inequality in the form [13, Theorem 2] gives

|r(ml)| < ( 2 log N
log(N/ml) − 1) N
ϕ(ml) log N + ω(N)

<(1 + e
−20) N(e
γ log(log log N + log δ) + 0.5)
log1+δ N

< 0.19N
log2.3 N
 (52)

since ml = k1 > K0 = logδ N ≥ logδ X2 and ϕ(ml) > ml/(e
γ log log ml +0.5)
by Theorem 15, (3.41-42) of [17]. This proves (50).

5 LOWER BOUNDS FOR SOME SUMS OVER PRIMES 13

Recalling that |Ak| = π(N; k, N)−ω(N; k, N) and |Akd| = π(N; kd, N)−
ω(N; kd, N), we see that

rk(d) = π(N; kd, N) − π(N; k, N)
ϕ(d) + 1.3841θ log N
log log N (53)

and therefore
∑#

d<Q/k µ2(kd) |rk(d)| < 1.3841Q log N
log log N + ∑#

d<Q/k
 ∣
∣
∣
∣π(N; kd, N) − π(N; k, N)
ϕ(d)
 ∣
∣
∣
∣ .

(54)
Now we apply Lemma 2.6 with x = N and obtain
∑#

d<Q/k µ2(kd) |rk(d)| < 1.3841D log N
log log N + e
−8x
log3 x < 1.1e
−8x
log3 x . (55)

5 Lower bounds for some sums over primes

The purpose of this section is to obtain an lower bound for S(A, P (z)):

Theorem 5.1.

S(A, P (z)) >UN |A|
log N

×
 (
4e
γ log 3 − 0.5198ǫ0(N) − 767.7471

log 1
2 N
 )
 . (56)

As mentioned in the introduction, we cannot directly estimate S(A, P (z))
due to possible existence of the exceptional zero k1. However, the following
inclusion-exclusion identity allows us to overcome this obstacle.

Lemma 5.2.

S(A, P (z)) =
 l−1∑

i=0 (−1)iS(A
(i), P (i+1)(z)) + (−1)lS(A
(l), P (l)(z)). (57)

Proof. S(A, P 1(z))−S(A, P (z)) counts the number of integers in A divisible
by q1 but not divisible by any other primes below z. S(A
(1), P (2)(z)) −
S(A, P 1(z)) + S(A, P (z)) counts the number of integers in A divisible by
q1, q2 but not divisible by any other primes below z. Iterating this argument,
we see that ∑l−1
i=0(−1)l−1−iS(A
(i), P (i+1)(z)) + (−1)lS(A, P (z)) counts the
number of integers in A divisible by q1, q2, . . . , ql but not divisible by any
other primes below z, which is equal to S(A
(l), P (l)(z)).

5 LOWER BOUNDS FOR SOME SUMS OVER PRIMES 14

As we will see below, each quantity can be estimated by sieve argument
without encountering the exceptional character.

Theorem 3.1 immediately gives the following estimates:

Lemma 5.3. Let

Ej =
 {∑

d|P (j+1)(z),d<D rmj (d) if j = 0, 1, . . . , l − 1
∑

d|P (l)(z),d<D rml(d) if j = l. (58)

Then we have

S(A
(j), P (j+1)(z))

> ∣
∣A
(j)∣
∣ [
V (j+1)(z) − U (j+1)
N
 ( f (sj)
log D + 255.84406

log 3
2 D
 )]
 − |Ej| (59)

and
 S(A
(j), P (j+1)(z))

< ∣
∣A
(j)∣
∣ [

V (j+1)(z) + U (j+1)
N
 (F (sj)
log D + 298.87013

log 3
2 D
 )]
 + |Ej| (60)

for j = 0, 1, . . . , l − 1. Moreover, we have

S(A
(l), P (l)(z))

> ∣
∣A
(l)∣
∣ [

V (l)(z) − U (l)
N
 ( f (sl)
log D + 255.84406

log 3
2 D
 )]
 − |El| (61)

and
 S(A
(l), P (l)(z))

< ∣
∣A
(l)∣
∣ [

V (l)(z) + U (l)
N
 ( F (sl)
log D + 298.87013

log 3
2 D
 )]
 + |El| (62)

Let D = √x2
k1 log10 x2 and sj = log D/mj
log z . Since mj < k1 < log10 N, we have

log D > log N
2 − 22 log log N − 50 (63)

and
 4 − 8(32 log log N + 50)
log N < s1 < 4. (64)

5 LOWER BOUNDS FOR SOME SUMS OVER PRIMES 15

We majorize |Ej| for each j = 0, 1, . . . , l − 1 as well as for j = l. It is
almost trivial that D < Q and therefore (51) immediately gives

|Ej| < 1.3841D log N
log log N + 1.1e
−8N
log3 N < 1.2e
−8N
log3 N (65)

for each j = 0, 1, . . . , l − 1 as well as j = l.

Substituting this estimate into the inequalities in Lemma 5.3 gives

S(A
(j), P (j+1)(z))

> ∣
∣A
(j)∣
∣ [

V (j+1)(z) − U (j+1)
N
 ( f (sj)
log D + 255.84406

log 3
2 D
 )]

− 1.2e
−8N
log3 N .
 (66)

and
 S(A
(j), P (j+1)(z))

< ∣
∣A
(j)∣
∣ [

V (j+1)(z) + U (j+1)
N
 (F (sj)
log D + 298.87013

log 3
2 D
 )]

+ 1.2e
−8N
log3 N .
 (67)

Similar estimates also holds for S(A
(l), P (l)(z)).

We see that f (sj), F (sj) < 0.0866 for our values sj since sj > 4 −
11 log log N
log N > 3.9999. Hence, substituting (66) and (67) (and similar estimates
for S(A
(l), P (l)(z))) into Lemma 5.2, using (45) and observing that the error
terms are 1.2e
−8N log log N
log3 N log log log N < e
−23N
log2.5 N , (68)

5 LOWER BOUNDS FOR SOME SUMS OVER PRIMES 16

we obtain

S(A, P (z)) >
 l−1∑

j=0(−1)j ∣
∣A
(j)∣
∣ V (j+1)(z) + (−1)l ∣
∣A
(l)∣
∣ V (l)(z)

− |A| U (1)
N
 ( f (s1)
log D + 255.84406

log 3
2 D
 )

−
 ( l−1∑

j=1
 ∣
∣A
(j)∣
∣ U (j+1)
N + ∣
∣A
(l)∣
∣ U (l)
N
 )

×
 ( 0.0866
log D + 298.87013

log 3
2 D
 )

− e
−23N
log2.5 N .
 (69)

Now we shall evaluate each line in (69). We shall begin by showing that

l−1∑

j=0(−1)j ∣
∣A
(j)∣
∣ V (j+1)(z) + (−1)l ∣
∣A
(l)∣
∣ V (l)(z) = |A| V (z)
 (
1 + e
−27θ

log 1
2 N
 )
 .

(70)

We divide each term in the left-hand side of (70) and obtain

l−1∑

j=0(−1)j ∣
∣A
(j)∣
∣ V (j+1)(z) + (−1)l ∣
∣A
(l)∣
∣ V (l)(z)

=
 l−1∑

j=0(−1)j |A|
ϕ(mj) V (j+1)(z) + (−1)l |A|
ϕ(ml)V (l)(z)

+
 l−1∑

j=0 (−1)jr(mj)V (j+1)(z) + (−1)lr(ml)V (l)(z).
 (71)

We write ϕ∗(N) = N ∏

p|N p−2
p . Since

|A|
ϕ(mj) V (j+1)(z) = |A| V (z)
ϕ∗(mj)
 (
1 + 1
qj+1 − 2
) , (72)

we have
 l−1∑

j=0 (−1)j |A|
ϕ(mj) V (j+1)(z) = |A| V (z) (1 + (−1)j

ϕ∗(mj+1)
 ) (73)

5 LOWER BOUNDS FOR SOME SUMS OVER PRIMES 17

and therefore

l−1∑

j=0 (−1)j |A|
ϕ(mj) V (j+1)(z) + (−1)l |A|
ϕ(ml) V (l)(z) = |A| V (z). (74)

Substituting (74), (49), (50) into (71), we obtain

l−1∑

j=0 (−1)j ∣
∣A
(j)∣
∣ V (j+1)(z) + (−1)l ∣
∣A
(l)∣
∣ V (l)(z)

= |A| V (z) + 0.193θN
log2.3 N V (l)(z)
 (75)

Using Theorem 15, (3.41-42) of [17] again, we have

V (l)(z)
V (z) ≤
 l∏

j=1
 qj − 1
qj − 2 <
 l∏

j=1
 qj
qj − 1
 ∏

p
 (qj − 1)2

qj(qj − 2)

<1.51479 (
e
γ log log k1 + 5
2 log log k1
 )

<4 log log log N.
 (76)

Hence, (48) and (75) gives

l−1∑

j=0 (−1)j ∣
∣A
(j)∣
∣ V (j+1)(z) + (−1)l ∣
∣A
(l)∣
∣ V (l)(z)

= |A| V (z) + 0.772θN log log log N
log2.3 N V (z)

= |A| V (z) + e
−27θN
log1.5 N V (z)

= |A| V (z)
 (
1 + e
−27θ

log 1
2 N
 )
 ,
 (77)

which is (70).

Next we shall estimate the second line of (69). Since Lemma 2.2 gives

V (z) − UN f (s)
log D > UN
 (2e
γ log(s − 1)
log D − 1
4 log3 z
 ) , (78)

We see that log D > (0.5 − e
−16) log N and log(s1 − 1) > log 3 − 1

e9 log 1
2 N by

5 LOWER BOUNDS FOR SOME SUMS OVER PRIMES 18

(63) and (64). Thus we have

U (1)
N
 ( f (s1)
log D + 255.84406

log 3
2 D
 )

<V (z) + UN
 (
−2e
γ log(s1 − 1)
log D + 1
4 log3 z + ǫ0(N)f (s1)
log D + 255.84406(1 + ǫ0(N))

log 3
2 D
 )

<V (z) + UN
 (
−2e
γ log(s1 − 1)
log D + 128
log3 N + 0.1733ǫ0(N)
log N + 736.33191

log 3
2 N
 )

<V (z) + UN
 (
−4e
γ log 3 − 0.1733ǫ0(N)
log N + 736.33192

log 3
2 N
 )
 .
 (79)

Finally we shall evaluate the term in the third and the fourth line of
(69). With the aid of (48) we have

l−1∑

j=1
 ∣
∣A
(j)∣
∣ U (j+1)
N + ∣
∣A
(l)∣
∣ U (l)
N

< 2UN ǫ0(N) |A| + ( e
−8N
log3 N + 0.19N
log2.3 N
 ) U (l)
N

< UN
 

2ǫ0(N) |A| + 0.191N
log2.3 N
 ∏

p|k1
 p − 1
p − 2




< UN
 (
2ǫ0(N) |A| + N log log log N
log2.3 N
 )

< UN |A| (
2ǫ0(N) + e
−9

log N
 )
 (80)

observing that

UN
 ( l∑

j=1
 qj − 1
ϕ∗(mj−1)(qj − 2) + 1
ϕ∗(k1)
)

= 1
q1 − 2
 (1 + 1
q2 − 2 + 1
(q2 − 2)(q3 − 2) + · · · )

≤ 2UN
q1 − 2
< 2UN ǫ0(N).
 (81)

Since it follows from (63) that

0.0866
log D + 298.87013

log 3
2 D < 0.17321
log N + 845.33239

log 3
2 N , (82)

6 UPPER BOUNDS FOR SOME SUMS OVER PRIMES 19

we conclude that
( l−1∑

j=1
 ∣
∣A
(j)∣
∣ U (j+1)
N + ∣
∣A
(l)∣
∣ U (l)
N
 ) ( 0.0866
log D + 298.87013

log 3
2 D
 )

< UN |A| ǫ0(N)
 ( 0.3465
log N + 1790.6648

log 3
2 N
 )
 .
 (83)

Substituting (70), (79) and (83) into (69), we obtain Theorem 5.1.

6 Upper bounds for some sums over primes

In this section, we shall obtain an upper bound for ∑
z≤q<y S(Aq, P, z):

Theorem 6.1.
∑

z≤q<y S(Aq, P (z)) < UN |A|
log N

×
 (
4e
γ log 6(1 + ǫ0(N)) + 993.2507

log 1
2 N
 )
 .
 (84)

In this mission, it is much easier to break the obstacle due to possi-
ble existence of exceptional modulus; it suﬃces to give an upper bound for∑

z≤q<y S(Aq, P (1)(z)) since it is clear that ∑

z≤q<y S(Aq, P (z)) ≤ ∑

z≤q<y S(Aq, P (1)(z)).

In this section, we set D = x 1
2
2
log10 x2 and sq = log(D/q)
log z . Theorem 3.1
immediately gives

S(Aq, P (1)(z)) < |Aq|
 [

V (1)(z) + U (1)
N
 ( F (sq)
log D
q + 298.87013

log 3
2 D
q
 )]

+ ∑

d<D/q,d|P (1)(z) |rq(d)| , (85)

where rq(d) = |Aqd| − |Aq| /ϕ(d), and therefore the sum ∑

z≤q<y S(Aq, P, z)
can be bounded from above by

∑

z≤q<y |Aq|
 [

V (1)(z) + U (1)
N
 ( F (sq)
log D
q + 298.87013

log 3
2 D
q
 )]

+ ∑

z≤q<y
 ∑

d<D/q,d|P (1)(z) |rq(d)| (86)

6 UPPER BOUNDS FOR SOME SUMS OVER PRIMES 20

Using Lemma 2.5, we obtain that the sum over the error terms is
∑

z≤q<y
 ∑

d<D/q,d|P (1)(z) |rq(d)|

≤ ∑

z≤q<y
 ∑

d<D/q,d|P (1)(z)
 (∣
∣
∣
∣π(N; qd, N) − π(N; q, N)
ϕ(d)
 ∣
∣
∣
∣ + ω(N))

≤ ∑

z≤q<y
 ∑

d<D/q,d|P (1)(z)
 (
|Eπ(N; qd, N)| + ∣
∣
∣
∣Eπ(N; q, N)
ϕ(d)
 ∣
∣
∣
∣ + ω(N))

< 1.2e
−8N
log3 N .
 (87)

Since N 1
8 < D
y < D
q < D
z < N 3
8 , we have 1 < sq < 3 and therefore
F (sq) = 2e
γ − sq. Thus we have

V (1)(z) + U (1)
N F (sq)
log D
q =U (1)
N 2e
γ

log D
q + V (1)(z) − U (1)
N
log z

<U (1)
N
 ( 2e
γ

log D
q + 1
5 log2 z
 )
 .
 (88)

This gives
 ∑

z≤q<y |Aq|
 [

V (1)(z) + U (1)
N
 ( F (sq)
log D
q + 298.87013

log 3
2 D
q
 )]

≤ U (1)
N ∑

z≤q<y |Aq|
 ( 2e
γ

log D
q + 298.87013

log 3
2 D
q + 1
5 log2 z
 )
 .
 (89)

Since |Aq| ≤ |A|+ω(N )
q−1 + Eπ(N; q, N), we have

∑

z≤q<y |Aq|
 ( 2e
γ

log D
q + 298.87013

log 3
2 D
q + 1
5 log2 z
 )

≤ z(|A| + ω(N))
z − 1
 ∑

z≤q<y
 2e
γ

q log D
q + 298.87013

q log 3
2 D
q + 1
5q log2 z

+
 ( 2e
γ

log D
y + 298.87013

log 3
2 D
y + 1
5 log2 z
 ) ∑

z≤q<y Eπ(N; q, N).
 (90)

Using Lemma 2.5, we have ∑

z≤q<y Eπ(N; q, N) < e−8N
log3 N and therefore

6 UPPER BOUNDS FOR SOME SUMS OVER PRIMES 21

(86) is at most

∑

z≤q<y
 (|A| + ω(N)
ϕ(q) + Eπ(N; q, N)) [

V (1)(z) + U (1)
N
 ( F (sq)
log D
q + 298.87013

log 3
2 D
q
 )]

< U (1)
N ∑

z≤q<y
 (|A| + ω(N)
ϕ(q) + Eπ(N; q, N)) ( 2e
γ

log D
q + 298.87013

log 3
2 D
q + 1
5 log2 z
 )

< U (1)
N |A| ∑

z≤q<y
 1
q − 1
 ( 2e
γ

log D
q + 298.87013

log 3
2 D
q + 1
5 log2 z
 )

+ 1.2e
−8U (1)
N N
log3 N
 ( 2e
γ

log D
y + 298.87013

log 3
2 D
y + 1
5 log2 z
 )

< U (1)
N |A|
 (
2e
γ ∑

z≤q<y
 1
(q − 1) log D
q + 298.87013 ∑

z≤q<y
 1

(q − 1) log 3
2 D
q + 1
5 log2 z
 ∑

z≤q<y
 1
q − 1
 )

+ e
−4U (1)
N N
log4 N .
 (91)

We use Lemma 2.1, with the aid of (7), to obtain

∑

z≤q<y
 1

q log N 1
2
q < ∫ y

z
 dt

t log t log N 1
2
t + 6
log N × 1.001
5 log2 z

< 2 log 6
log N + 76.9
log3 N
 (92)

and
 ∑

z≤q<y
 1

q log 3
2 N 1
2
q < ∫ y

z
 dt

t log t log 3
2 N 1
2
t + 6 3
2

log 3
2 N × 1.00001
5 log2 z

<4√2 (√3 − √ 4
3 )

log 3
2 N + 188.2

log 7
2 N .
 (93)

These inequalities, combined with log D > 1
2 log N − 12 log log N − 50 >
1
2 log N − 14 log log N, give the upper bounds

∑

z≤q<y
 1
(q − 1) log D
q < 1
1 − 29 log log N
log N
 (2 log 6
log N + 76.9
log3 N
 )

< 2 log 6
log N + 215.02 log log N
log2 N + 76.91
log3 N
 (94)

7 AN UPPER BOUND FOR A BILINEAR FORM 22

and
 ∑

z≤q<y
 1

q log 3
2 D
q < 1
1 − 29 log log N
log N
 


4√2 (√3 − √ 4
3)

log 3
2 N + 188.2

log 7
2 N
 




< 3.26599

log 3
2 N + 188.21

log 7
2 N .
 (95)

Moreover, (7) immediately gives

∑

z≤q<y
 1
q − 1 < ∑

q≥z
 1
q(q − 1) + ∑

z≤q<y
 1
q < log 8
3 + 1
3 log2 N . (96)

Combining (94)-(96) with (91), we obtain

∑

z≤q<y S(Aq, P (1)(z)) < U (1)
N |A|
log N

×
 (

4e
γ log 6 + 976.1256

log 1
2 N
 ) (97)

Thus, with the aid of (47), we prove Theorem 6.1.

7 An upper bound for a bilinear form

We shall ﬁnish our sieve argument by obtaining an upper bound for S(B, P (y)):

Theorem 7.1. Let ǫ be a positive real number < 0.01. Then

S(B, P (y))

≤ c2(1 + ǫ)NUN
log2 N
 (
4e
γ(1 + ǫ0(N)) + 860.16295

log 3
2 N
 )
 + e
−138N
ǫ log3 N . (98)

In order to obtain this upper bound for S(B, P (y)), we use the following
upper bound for a bilinear form:

Lemma 7.2. Let a(n) be an arithmetic function with |a(n)| ≤ 1 for all n.
Let X, Y, Z > 0 be real numbers with log10 Y < X ≤ N
z , XY < 2N and

7 AN UPPER BOUND FOR A BILINEAR FORM 23

Y, Z > z. Moreover, let D∗ = (XY ) 1
2
log10 Y . Then we have

∑

d<D∗,q1∤d max
(a,d)=1
 ∣
∣
∣
∣
∣
∣
∣
∣
∑

n<X
 ∑

Z≤p<Y,
np≡a (mod d)
 a(n) − 1
ϕ(d)
 ∑

n<X
 ∑

Z≤p<Y,
(np,d)=1
 a(n)
∣
∣
∣
∣
∣
∣
∣
∣

≤ e
−144XY
log4 Y .
 (99)

Proof. Factoring χ = χ0,sχ1 with d = rs, the bilinear form is

∑

rs<D∗,
q1∤rs
 ∑∗

χ (mod r)
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

n<X,
(n,s)=1
 a(n)χ(n)
∣
∣
∣
∣
∣
∣
∣
∣
 ∣
∣
∣
∣
∣
∣
 ∑

Z≤p<Y,p∤s χ(p)
∣
∣
∣
∣
∣
∣

≤ ∑

s<D∗,
q1∤s
 ∑

r<D∗,
q1∤r
 ∑∗

χ (mod r)
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

n<X,
(n,s)=1
 a(n)χ(n)
∣
∣
∣
∣
∣
∣
∣
∣
 ∣
∣
∣
∣
∣
∣
 ∑

Z≤p<Y,p∤s χ(p)
∣
∣
∣
∣
∣
∣ .
 (100)

We begin by estimating the inner sum restricted to r < D0, where
D0 = log10 Y . Since r is nonexceptional, as we derived Corollary 2.4 from
Lemma 2.3, we derive from Theorem 1.1 of [21] that ∑∗
χ (mod r) |π(x; χ)| <

10−4x
log10 x < e−212x
log4 x for x ≥ z ≥ x
1/8
0 . Thus we have

∑∗

χ (mod r)
 ∣
∣
∣
∣
∣
∣
 ∑

Z≤p<Y,p∤s χ(p)
∣
∣
∣
∣
∣
∣

≤ ∑∗

χ (mod r) |π(Y ; χ) − π(Z; χ)| + ω(s)

< e
−212Y
log4 Y + e
−212Z
log4 Z + 1.3841ϕ(r) log D∗

2 log log D∗

< 2e
−212Y
log4 Y + 1.3841ϕ(r) log D∗

2 log log D∗ .
 (101)

Now we can see that the inner sum restricted to r < D0 is

<2e
−212Y
log4 Y
 ∑

r<D0
 1
ϕ(r) + 1.3841D0 log D∗

2 log log D∗

<4e
−212Y log D0
log4 Y + 1.3841D0 log D∗

2 log log D∗ .

<e
−210Y log D0
log4 Y ,
 (102)

7 AN UPPER BOUND FOR A BILINEAR FORM 24

where the last inequality follows from fact that D0 < log10 Y and log D∗ <
log X < log N = 8 log z < 8 log Y .

In order to estimate the inner sum restricted to D0 ≤ r < D∗, we divide
the interval into intervals of the form D1 ≤ r < 2D1, where D1 = 2kD0(0 ≤
k ≤ log(D∗/D0)
log 2 ) and use Cauchy’s inequality and the large-sieve inequality.
We have, for each D1,

∑

D0≤r<D∗,
D1≤r<2D1,
q1∤r
 ∑∗

χ (mod r)
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

n<X,
(n,s)=1
 a(n)χ(n)
∣
∣
∣
∣
∣
∣
∣
∣
 ∣
∣
∣
∣
∣
∣
 ∑

Z≤p<Y,p∤s χ(p)
∣
∣
∣
∣
∣
∣

≤ 1
D2
 




∑

r
 ∑∗

χ (mod r)
 r
ϕ(r)
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

n<X,
(n,s)=1
 a(n)χ(n)
∣
∣
∣
∣
∣
∣
∣
∣
2




 1
2

×
 


∑

r
 ∑∗

χ (mod r)
 r
ϕ(r)
 ∣
∣
∣
∣
∣
∣
 ∑

Z≤p<Y,p∤s χ(p)
∣
∣
∣
∣
∣
∣

2


 1
2

≤ 1
D2
 (
(D2
2 + X)(D2
2 + Y )XY ) 1
2

≤√XY (D2 + 2√X + Y ) + XY
D2

≤D2√XY + 4XY
log10 Y + XY
D2 ,
 (103)

where D2 is the number of integers r with max{D0, D1} ≤ r < min{2D1, D∗},
and summming these quantities over 0 ≤ k ≤ log(D∗/D0)
log 2 , we obtain

∑

D0≤r<D∗,
q1∤r
 ∑∗

χ (mod r)
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

n<X,
(n,s)=1
 a(n)χ(n)
∣
∣
∣
∣
∣
∣
∣
∣
 ∣
∣
∣
∣
∣
∣
 ∑

Z≤p<Y,p∤s χ(p)
∣
∣
∣
∣
∣
∣

<2D∗√XY + (4 log D∗

log 2 + 2) XY
D0

< 4XY
log10 Y + 2XY log N
(log 2) log10 Y < 2.9XY log N
log10 Y .
 (104)

Summing over s is only to multiply by ∑

s 1
ϕ(s) < 2 log D∗ < log N =

8 log z < 8 log Y , so that the contribution is at most 2e−145XY
log4 Y . Combin-
ing this estimate with (102), we obtain the result.

7 AN UPPER BOUND FOR A BILINEAR FORM 25

The rest of this section is devoted to the proof of Theorem 7.1. Let

B(j) = {N−p1p2p3 : z ≤ p1 < y ≤ p2 ≤ p3, up2p3 < N, (p2p3, N) = 1, wj ≤ p1 < (1+ǫ)wj},
(105)
where
 wj = z(1 + ǫ)j for j = 0, 1, · · · , j0 = ⌈ log(y/z)
log(1 + ǫ)
 ⌉ − 1, (106)

and B# = ∪jB(j).

We can easily see that ∣
∣B(j)∣
∣ = (π(Y ) − π(Z))#{(p2, p3) : y ≤ p2 ≤
p3, wjp2p3 < N, (p2p3, N) = 1}, where Z = max{z, wj} and Y = min{(1 +
ǫ)wj, y}, and

S(B, P (1)(y)) ≤ S(B#, P (1)(y)) ≤
 j0∑

j=0 S(B(j), P (1)(y)). (107)

Lemma 7.3. ∣
∣B#∣
∣ < c2(1 + ǫ)N
log N + 2.207(1 + ǫ)N
log2 N , (108)

where c2 = ∫ 1/3
1/8 log(2−3β)
β(1−β) + 10−8 < 0.36309.

Proof. We begin by

∣
∣B#∣
∣ ≤ ∑

z≤p1<y≤p2,
p1p2
2<(1+ǫ)N
 π ((1 + ǫ)N
p1p2
 )

≤ (1 + ǫ + 10−8)N ∑

z≤p1<y
 1
p1
 ∑

y≤p2<w
 1
p2 log N
p1p2 ,
 (109)

where w = w(p1) = √ (1+ǫ)N
p1 .

As in p. 289 in [14], we introduce two functions hp(t) = 1
log N
pt and

H(u) = ∫ (N/u) 1
2

y hu(t)d log log t = ∫ (N/u) 1
2

y
 d log log t
log N
ut . (110)

We see that

H(N α) = ∫ N 1−α
2

N 1
3
 d log log t
log N 1−α
t = 1
log N
 ∫ 1−α
2

1
3
 dβ
β(1 − α − β). (111)

In particular, we have hp1(w) = 2
log N
(1+ǫ)p1 , H(y) = 0 and H(z) = log 26
21
log N .

7 AN UPPER BOUND FOR A BILINEAR FORM 26

Now Lemma 2.1 and (7) give that the inner sum in (109) is

∑

y≤p2<x
 ∑ hp1(p2)
p2 ≤ H(p1) + hp1(w)
4 log2 y . (112)

Since
 hp1(w)
4 log2 y = 1
2 log N
(1+ǫ)p1 log y

≤ 1
2 log N
(1+ǫ)y log y

= 1

2 log N 2
3
1+ǫ log N 1
3

≤ 9
4 log2 N ×
 2
3 log N

2
3 log N − log(1 + ǫ)

≤9(1 + e
−50)
4 log2 N ,
 (113)

we have ∑

y≤p2<x
 ∑ hp1(p2)
p2 ≤ H(p1) + 9(1 + e
−50)
4 log2 N . (114)

Hence the outer sum in (109) is at most

∑

z≤p1<y
 H(p1)
p1 + 9(1 + e
−50)
4 log2 N
 ∑

z≤p1<y
 1
p1 < ∑

z≤p1<y
 H(p1)
p1 + 2.2069
log2 N (115)

since it immediately follows from (7) that ∑
z≤p<y(1/p) < log(8/3) + 1
4 log2 z .

Using Lemma 2.1 and (7) again and exploiting the fact ∫ y
z H(u)d log log u =
c2
log N in p. 291 of [14], we have

∑

z≤p1<y
 H(p1)
p1 < ∫ y

z H(u)d log log u + log 26
21
4 log2 z log N

= c2
log N + 16 log 26
21
log3 N .
 (116)

This proves the lemma.

7 AN UPPER BOUND FOR A BILINEAR FORM 27

We set D = N 1
2
log10 N and let s = log D
log y . Then Theorem 3.1 gives

S(B(j), P (1)(y))

≤ ∣
∣B(j)∣
∣ (
V (1)(y) + U (1)
N
 ( F (s)
log D + 298.87013

log 3
2 D
 ))
 + ∑

d<D,d|P (1)(y)
 ∣
∣
∣r(j)
d ∣
∣
∣ ,

(117)

where r(j)
d = ∣
∣
∣B(j)
d ∣
∣
∣−|B(j)|
ϕ(d) . By Lemma 2.2, we have V (1)(y) < U (1)
N
log y (1 + 1
5 log2 y )
.
We can see that 1 < sw < 3 and therefore F (sl) = 2e
γ − sw. Thus, similarly
to (89), we have, for each j,

S(B(j), P (1)(y))

≤ ∣
∣B(j)∣
∣ U (1)
N
 ( 2e
γ

log D + 298.87013

log 3
2 D + 1
5 log2 y
 )
 + R(j) (118)

and therefore, by (107),

S(B, P (1)(y))

≤ ∣
∣B#∣
∣ U (1)
N
 ( 2e
γ

log D + 298.87013

log 3
2 D + 1
5 log2 y
 )
 + R, (119)

where R(j) = ∑

d<D,d|P (1)(y) ∣
∣
∣r(j)
d ∣
∣
∣ and R = ∑j0
j=0 R(j).

We put a(n) = aN (n) to be the characteristic function of the set of
integers of the form n = p2p3 with y ≤ p2 < p3 and (N, p2p3) = 1. Then,
noting that (d, p2p3) = 1 since d | P (y), we see that

r(j)
d = ∑

n<N/wj
 ∑

Z≤p<Y,
np≡N (mod d)
 a(n) − 1
ϕ(d)
 ∑

n<N/wj
 ∑

Z≤p<Y a(n)

=r(j,1)
d + r(j,2)
d ,
 (120)

where
 r(j,1)
d = ∑

n<N/wj
 ∑

Z≤p<Y,
np≡N (mod d)
 a(n) − 1
ϕ(d)
 ∑

n<N/wj
 ∑

Z≤p<Y,
(np,d)=1
 a(n) (121)

and r(j,2)
d = 1
ϕ(d)
 ∑

n<N/wj
 ∑

Z≤p<Y,
p|d
 a(n). (122)

7 AN UPPER BOUND FOR A BILINEAR FORM 28

Now we can divide R ≤ R1 + R2, where Ri = ∑j0
j=0 ∑

d<D,d|P (1)(y) ∣
∣
∣r(j,i)
d ∣
∣
∣ for
i = 1, 2.

In order to estimate R1, we shall apply Lemma 7.2 with X = N/wj, Y =
min{y, (1 + ǫ)j}, Z = max{wj, z} and a = N. We see that D < D∗ =

(XY ) 1
2
log10 Y < (XY ) 1
2 < N and therefore

∑

d<D,d|P (y)
 ∣
∣
∣r(j,1)
d ∣
∣
∣

≤ ∑

d<D∗,d|P (y)
 ∣
∣
∣r(j,1)
d ∣
∣
∣

= ∑

d<D∗,d|P (y)
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

n<N/wj
 ∑

Z≤p<Y,
np≡N (mod d)
 a(n) − 1
ϕ(d)
 ∑

n<N/wj
 ∑

Z≤p<Y,
(np,d)=1
 a(n)
∣
∣
∣
∣
∣
∣
∣
∣

< e
−144(1 + ǫ)N
log4 y
 (123)

for each j = 0, 1, . . . , j0. Hence, noting that ǫ < 1/100, we see that R1 is at
most
 j0∑

j=0
 ∑

d<D,d|P (y)
 ∣
∣
∣r(j,1)
d ∣
∣
∣ < (1 + ǫ)e
−144N log y
z
log(1 + ǫ) log4 y

< e
−139N
ǫ log3 N .
 (124)

Next, R2 is at most

j0∑

j=0
 ∑

d<D,d|P (y) r(j,2)
d = 1
ϕ(d)
 ∑

n<N/l
 ∑

Z≤p<Y,
p|d
 a(n)

≤8N 7
8 ∑

d<D,d|P (y)
 1
ϕ(d)

<8N 7
8 log N

< e
−139N
log3 N
 (125)

8 PROOF OF THE MAIN THEOREM 29

since we can see that
 j0∑

j=0 r(j,2)
d = 1
ϕ(d)
 ∑

n<N/wj
 ∑

Z≤p<Y,
p|d
 a(n)

= 1
ϕ(d)
 ∑

n<N/wj
 ∑

p>z,p|d a(n)

≤ N log d
ϕ(d)l log z ≤ 8N 7
8
ϕ(d).
 (126)

Using (124) and (125), we have

S(B, P (1)(y))

≤ ∣
∣B#∣
∣ U (1)
N
 ( 2e
γ

log D + 298.87013

log 3
2 D + 1
5 log2 y
 )
 + 2e
−139N
ǫ log3 N . (127)

Now Lemma 7.3 gives ∣
∣B#∣
∣ < c2(1+ǫ)N
log N + 2.207(1+ǫ)N
log2 N . Since log D =

1
2 log N − 10 log log N, we have 1/ log D − 2/ log N < 20 log log N/(log N −
20 log log N) < e
−10/ log 3
2 N and therefore the right-hand side in (127) is at
most c2(1 + ǫ)NU (1)
N
log N
 ( 4e
γ

log N + 845.33255

log 3
2 N
 )
 + 2e
−139N
ǫ log3 N . (128)

We recall the inequality (47) and obtain

S(B, P (1)(y))

≤ c2(1 + ǫ)NUN
log2 N
 (
4e
γ(1 + ǫ0(N)) + 860.16295

log 3
2 N
 )
 + 2e
−139N
ǫ log3 N . (129)

Since trivially S(B, P (1)(y)) ≤ S(B, P (y)), we obtain Theorem 7.1.

8 Proof of the main theorem

We recall that
V (j)(x) = U (j)
N
log x
 (
1 + θ
5 log2 x
 ) (
1 + 8θ log x
x
 ) (130)

REFERENCES 30

for j = 0, 1, . . . , l and x ≥ z, where

U (j)
N = 2e
−γ ∏

p
 (
1 − 1
(p − 1)2
 ) ∏

p>2,p|N mj
 p − 1
p − 2 . (131)

Now we shall take e
−100 < ǫ < e
−20 and apply Lemma 4.1 combined
with Theorems 5.1, 6.1 and 7.1, which gives

π2(N) log N
UN |A| >e
γ(4 log 3 − 2 log 6 − 2c2(1 + ǫ))

− ǫ0(N)(2e
γ(c2(1 + ǫ) + log 6) + 0.5198)

− 767.7471 + 496.6254 + 430.0815c2(1 + ǫ)

log 1
2 N − 1
log N .

(132)

Since ǫ0(N) ≤ 1/57 and ǫ < e
−20, we have

π2(N) log N
UN |A| > 0.007. (133)

As mentioned in (48), we have |A| > N
log N . This completes the proof of the
main theorem.

References

[1] K. G. Borodzkin, On I. M. Vinogradovfs constant, Proc. Third All-Union
Math. Conf., Izdat. Akad. Nauk SSSR, Moscow 1 (1956), p. 3.

[2] J.-R. Chen, On the representation of a large even integer as the sum
of a prime and the product of at most two primes, Kexue Tongbao, 17
(1966), 385–386.

[3] J.-R. Chen, On the representation of a large even integer as the sum
of a prime and the product of at most two primes, Sci. China Ser. A 16
(1973), 157–176, II, ibid. 21 (1978), 421–430.

[4] J.-R. Chen and T.-Z. Wang, On the Goldbach problem, Acta Math.
Sinica 32 (1989), 702–718. (in Chinese)

[5] J.-R. Chen and T.-Z. Wang, The Goldbach problem for odd numbers,
Acta Math. Sinica 39 (1989), 169–174. (in Chinese)

REFERENCES 31

[6] J.-M. Deshouillers, G. Eﬃnger, H. te Riele and D. Zinoviev, . ”A com-
plete Vinogradov 3-primes theorem under the Riemann hypothesis, Elect.
Res. Ann. Amer. Math. Soc. 3 (1997), 99–104.

[7] Pierre Dusart, Estimates of some functions over primes without R.H.,
preprint, arXiv: 1002.0442.

[8] G. Greaves, Sieves in Number Theory, Springer-Verlag, Berlin, 2001.

[9] H. Iwaniec, On the error term in the linear sieve, Acta Arith. 19, 1–30.

[10] W. B. Jurkat and H.-E. Richert, An improvement of Selberg’s sieve
method I, Acta Arith. 11, 217–240.

[11] Habiba Kadiri, An explicit zero-free region for the Dirichlet L-
functions, http://arxiv.org/abs/0510570.

[12] M.-C. Liu and T.-Z. Wang, On the Vinogradov bound in the three
primes Goldbach conjecture, Acta Arith. 105 (2002) 133–175.

[13] H. L. Montgomery and R. C. Vaughan, The large sieve, Mathematika
20, 119–134.

[14] Melvyn B. Nathanson, Additive Number Theory: The Classical Bases,
GTM 164, Springer-Verlag, New York, 1996.

[15] Guy Robin, Estimation de la fonction de Tchebychef θ sur le k-i`eme
nombre premier et grandes valuers de la fonction ω(n) nombre de di-
viseurs premiers de n, Acta Arith 42 (1983), 367–389.

[16] P. M. Ross, On Chen’s theorem that every large even number has the
form p1 + p2 or p1 + p2p3, J. London Math. Soc. (2) 10 (1975), 500–506.

[17] J. Barkley Rosser and Lowell Schoenfeld, Approximate formulas for
some functions of prime numbers, Illinois J. Math. 6 (1962), 64–94.

[18] J. Barkley Rosser and Lowell Schoenfeld, Sharper Bounds for the
Chebyshev Functions θ(x) and ψ(x), Math. Comp 29 (1975), 243–269.

[19] I. M. Vinogradov, Representation of an odd number as a sum of three
primes, C.R. Acad. Sci. USSR 15 (1937), 291–294.

[20] I. M. Vinogradov, Some theorems concerning the theory of primes, Rec.
Math. N.S. (Mat. Sb.) 2(44) (1937), 179–195.

[21] Tomohiro Yamada, Explicit formulae for primes in arithmetic progres-
sions I, http://arxiv.org/abs/1306.5322.

REFERENCES 32

[22] Tomohiro Yamada, An explicit formula for the linear sieve, (in prepa-
ration).

Tomohiro Yamada
Center for Japanese language and culture
Osaka University
562-8558
8-1-1, Aomatanihigashi, Minoo, Osaka
Japan
e-mail: tyamada1093@gmail.com
