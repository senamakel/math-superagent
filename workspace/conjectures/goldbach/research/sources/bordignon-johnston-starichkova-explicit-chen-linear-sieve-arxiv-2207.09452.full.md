<!-- source: https://arxiv.org/pdf/2207.09452 | converted from PDF -->

arXiv:2207.09452v6  [math.NT]  25 Jun 2025
An explicit version of Chen’s theorem and the linear sieve

MATTEO BORDIGNON, DANIEL R. JOHNSTON AND VALERIIA STARICHKOVA

Abstract. Drawing inspiration from the work of Nathanson and Yamada we prove
an effective and explicit version of Chen’s theorem. By contrast, existing proofs of
Chen’s theorem are ineffective due to their use of the Siegel-Walfisz theorem. Our
main result is that every even integer larger than exp(exp(32.7)) can be written as
the sum of a prime and the product of at most two primes. We also prove that all
even integers N ⩾ 4 can be written as the sum of a prime and the product of at
most e29.3 primes. The main idea will be to follow a proof of Chen’s theorem due to
Nathanson, being more careful with the treatment of potential Siegel zeros in order
to obtain an effective and explicit result. In following this framework we also prove
an explicit version of the linear sieve, which substantially improves upon the previous
best one by Nathanson.

Keywords: Chen’s theorem, sieves, linear sieve, exceptional zero, explicit results.

MSC classes: 11N36, 11P32 (Primary) 11M20, 11N13 (Secondary)

1 Introduction

One of the most famous problems in number theory is Goldbach’s conjecture.

Conjecture 1 (Goldbach). For any even integer N ⩾ 4 there exist two primes p1 and
p2, such that N = p1 + p2.

This conjecture was verified for all even N ⩽ 4·10
18 by Oliveira e Silva [41]. However,
a complete proof appears to be out of reach for the present state of mathematics. There
are two results that are arguably the nearest approximations to Goldbach’s conjecture:
Goldbach’s weak conjecture and Chen’s theorem. Goldbach’s weak conjecture, also
known as the ternary Goldbach problem, is a proved result.

Theorem 1 (Vinogradov–Helfgott). For any odd number N ⩾ 7 there exist three
primes p1, p2 and p3, such that
 N = p1 + p2 + p3.

Date: June 26, 2025.
The basis for this work was done as part of the thesis the first author wrote during the length of their
PhD at the University of New South Wales Canberra. It was also partially supported by an Australian
Mathematical Society Lift-off Fellowships of the first and the third author, by OP RDE project No.
CZ.02.2.69/0.0/0.0/18 053/0016976 International mobility of research, technical and administrative
staff at the Charles University, and by Australian RC Discovery Project DP240100186.
1

In particular, Vinogradov proved in [47] that all odd numbers larger than some
constant C can be written as a sum of three prime numbers. According to [19, p. 201],
the first explicit value of C was established by Borodzkin in his unpublished doctoral
dissertation and he later, in [5], improved the result to C = exp(exp(16.038)). After
a series of further improvements, the final push to prove Goldbach’s weak conjecture
was done by Helfgott in [27].
In this paper we instead focus on obtaining an explicit version of Chen’s theorem,
first proved in 1966 by Chen [15, 16].

Theorem 2 (Chen). All sufficiently large even numbers can be written as the sum of
a prime and another number that is the product of at most two primes (a semi-prime).

A lot of work has been done to improve Chen’s result. Simpler proofs were given
in [25], [45] and [40]. Further, Chen’s theorem was quantitatively improved, in the
counting of the number of ways in which large enough even numbers can be written
as the sum of a prime and a semi-prime, by Chen himself in [17] and [18], and further
in [11], [48], [12] and [49]. Many generalizations of Chen’s theorem have also been
obtained. Generalizations with bounds on the prime and/or semi-prime were given
in [36], [9], [10], [34] and [13]. Lu and Cai [37], proved a version in which the prime
and semi-prime are in certain arithmetic progressions. Hinz [28] proved a version for
totally real algebraic number fields. Car [14] proved a version for Fq[X], the ring of
polynomials with one variable over a finite field of q elements.
It is interesting to note that while a lot of effort was put into making Vinogradov’s
proof of Goldbach’s weak conjecture completely explicit, not much effort was put into
making Chen’s theorem explicit. The only attempt was made by Yamada in [50], but
several mistakes can be found in the proof; see [50, (87) & (104)], where a log term
appears to be missing, and, notably, that no proof is given of the explicit version of
the linear sieve that is used and that this version is inconsistent with the versions in
[31], [29] and [40]. The aim of this paper is thus to obtain the first complete explicit
version of Chen’s theorem. Our main result is as follows.

Theorem 3. Let π2(N ) denote the number of representations of a given even integer
N as the sum of a prime and a semi-prime. If N > exp(exp(32.7)), then

(1) π2(N ) > 2 · 10
−4 · UN N
log2 N ,

where, with γ the Euler–Mclaurin constant,

(2) UN := 2e
−γ ∏

p>2
 (
1 − 1
(p − 1)2
 ) ∏

p>2
p|N
 p − 1
p − 2.

Here we note that directly correcting the mistakes in [50] would lead to a much
worse lower bound than the exp(exp(36)) claimed in the paper. While the lower bound
exp(exp(32.7)) that we prove appears only to be a modest improvement on the one in
the incomplete work of Yamada [50], this is mainly due to this constant being around
the optimal that is possible to obtain with the present method, for more details see §9.
2

Using (1), we will prove the following corollary, which is essentially a stronger form of
Chen’s theorem.

Corollary 4. Every even integer N > exp(exp(32.7)) can be represented as the sum
of a prime and a square-free number with at most two prime factors.

In particular, Corollary 4 implies that we can take the prime factors in Chen’s
theorem to be distinct.
We also prove the following, which is a simple consequence of Theorem 3 and a result
of Dudek [21], where he proves that all integers larger than two can be written as the
sum of a prime and a square-free number.

Theorem 5. All even integers N ⩾ 4 can be written as the sum of a prime and the
product of at most e
29.3 primes.

Theorem 5 makes explicit a result of R´enyi [44]. We also remark that the proof of
Theorem 5 is quite wasteful, meaning the number e
29.3 can certainly be lowered with
more work. The second and third authors are currently writing a follow up article in
this direction.
For the proof of Theorem 3 we will draw inspiration from the works of Nathanson in
[40] and Yamada in [50]. In particular, Nathanson [40, Theorem 10.1] gives a proof of
Chen’s theorem, of which Yamada [50, Theorem 1.1] made a partial attempt to make
explicit. The technique uses an explicit version of the linear sieve to obtain upper
and lower bounds for the number of certain sifted integers, combined with explicit
versions of the prime number theorem for primes in arithmetic progression and an
upper bound for an exceptional zero of a Dirichlet L-function. Note that previous
proofs of Chen’s theorem, including Nathanson’s [40], are ineffective. Hence, to obtain
an explicit version a modified approach is required. That is, one cannot simply repeat
each step of these past proofs whilst keeping track of the error terms. The main problem
is making the error term in the linear sieve explicit, accounting for the possible existence
of an exceptional zero. We address this problem by splitting the argument into two
cases: one when the exceptional modulus is ‘small’ and one when it is ‘large’. In the
case when the modulus is ‘small’ it is possible to absorb the Siegel zero into the error
term concerning primes in arithmetic progression. In the second case, a variant of
the inclusion-exclusion principle is used, avoiding the Siegel zero but introducing more
complicated error terms.
For reference, all of the notation used at the paper is given at the end, in Section 11.
Otherwise, an outline of the paper is as follows. In Section 2 we prove a new explicit
version of the linear sieve and introduce other preliminary results and definitions.
In Section 3 we state several lemmas from existing literature that will be frequently
used in the later sections. For our application of the linear sieve, the remainder term
essentially corresponds with the error term in the prime number theorem for arithmetic
progressions. Thus, in Section 4 we prove a collection of explicit results regarding
primes in arithmetic progressions. Here, we use a recent result for the prime number
theorem for primes in arithmetic progressions given by the first author in [4] and an
improved upper bound for the exceptional zero given by the first author in [2, 3]. In
Section 5, we then use the preceding results to set up all the required preliminaries
3

for sieving. In Sections 6, 7 and 8 we obtain upper and lower bounds for the sifted
integer sets. In Section 9 we prove Theorem 3 and in Section 10 we conclude by proving
Corollary 4 and Theorem 5.
 Acknowledgements

We would like to thank our supervisor Tim Trudgian for his help in developing this
paper and his insightful comments. We would also like to thank Leo Goldmakher,
Bryce Kerr and Kevin O’Bryant for their helpful comments and suggestions.

2 An explicit version of the linear sieve

Nathanson’s proof of Chen’s theorem [40, §10], which we roughly follow, requires
multiple applications of lower and upper bounds of the linear sieve. Therefore, in
order to obtain the best explicit result, we prove the following theorem, which is an
improved and more general version of Nathanson’s linear sieve bounds in [40, Theorem
9.7]. Notably, our result is written in a general form, and can thus be used in other
applications beyond Chen’s Theorem.

Theorem 6 (The linear-sieve, explicit version). Let A = {a(n)}
∞
n=1 be an arithmetic
function such that
a(n) ⩾ 0 for all n and |A| =
 ∞∑

n=1 a(n) < ∞.

Let P be a set of prime numbers and for z ⩾ 2, let

P (z) := ∏

p∈P
p<z
 p.

Let
 S(A, P, z) :=
 ∞∑

n=1
(n,P (z))=1
 a(n).

For every n ⩾ 1, let gn(d) be a multiplicative function such that

0 ⩽ gn(p) < 1 for all p ∈ P.

Define |Ad| and r(d) by

(3) |Ad| :=
 ∞∑

n=1
d|n
 a(n) =
 ∞∑

n=1 a(n)gn(d) + r(d).

Let Q ⊆ P, and Q be the product of its primes. Suppose that, for some ε satisfying
0 < ε ⩽ 1/74, the inequality

(4) ∏

p∈P/Q
u⩽p<z
(1 − gn(p))
−1 < (1 + ε) log z
log u,

4

ε−1 C1(ε) C2(ε)
74 631 630
76 559 559
78 504 504
80 461 461
85 386 386
90 336 337
 ε−1 C1(ε) C2(ε)
95 302 302
100 276 277
120 218 219
140 189 190
160 172 173
180 161 162
 ε−1 C1(ε) C2(ε)
200 153 154
300 133 134
400 125 126
500 121 122
600 118 119
700 116 117
 ε−1 C1(ε) C2(ε)
800 115 116
900 114 115
1000 113 114
2000 109 110
10000 106 108
100000 106 107

Table 1: Values for C1(ε) and C2(ε).

holds for all n and 1 < u < z. Then, for any D ⩾ z we have the upper bound

(5) S(A, P, z) < (F (s) + εC1(ε)e
2h(s))XA + R,

and for any D ⩾ z2 we have the lower bound

(6) S(A, P, z) > (f (s) − εC2(ε)e2h(s))XA − R,

where s := log D
log z ,

(7) h(s) :=
 



e
−2 1 ⩽ s ⩽ 2,
e
−s 2 ⩽ s ⩽ 3,
3s−1e
−s s ⩾ 3,

F (s) and f (s) are the two functions defined by the following delay differential equations
(see [12]):

(8)
 {
F (s) = 2eγ
s , f (s) = 0 for 0 < s ⩽ 2,
(sF (s))
′ = f (s − 1), (sf (s))
′ = F (s − 1) for s ⩾ 2,

C1(ε) and C2(ε) come from Table 1,

(9) XA :=
 ∞∑

n=1 a(n) ∏

p|P (z)
(1 − gn(p)) = |A| ∏

p|P (z)
(1 − gn(p)),

and the remainder term is

(10) R := ∑

d|P (z)
d<QD
 |r(d)|.

If there is a multiplicative function g(d) such that gn(d) = g(d) for all n, then

(11) XA = V (z)|A|, where V (z) := ∏

p|P (z)
(1 − g(p)).

To read Table 1 it is useful to remember that C1(ε) and C2(ε) are decreasing in
ε−1. This will be made evident from the proof. We also note that we chose to stop
at ε−1 = 100000 as any larger value would give the same upper bound (to the nearest
integer) for C1(ε) and C2(ε). 5

We observe that for ε = 1/200 and all s ⩾ 1

(12) 154εe2h(s) ⩽ 0.77 and 153εe2h(s) ⩽ 0.765.

This gives a uniform upper bound for the ‘constants’ appearing in Theorem 6. In [40]
the equivalent upper bounds for εCi(ε)e2h(s) are ≈ 2210, and thus ours in (12) are
around 3000 times smaller.

2.1 Introduction

To begin with, we note that the functions f and F from Theorem 6 may be equiva-
lently defined as follows [40, Theorem 9.4]:

F (s) := 1 + ∑

n=1
n odd
 fn(s), for s ⩾ 1,(13)
 f (s) := 1 − ∑

n=1
n odd
 fn(s), for s ⩾ 2.(14)

Here,

(15) sf1(s) :=
 {
3 − s, 1 ⩽ s ⩽ 3,
0 s > 3.

Then, if n ⩾ 2 is even and s ⩾ 2, or if n ⩾ 3 is odd and s ⩾ 3,

(16) sfn(s) := ∫ ∞

s fn−1(t − 1)dt.

Finally, if n is odd and 1 ⩽ s ⩽ 3, then

(17) sfn(s) := 3fn(3) = ∫ ∞

3 fn−1(t − 1)dt.

A key part of the proof of Theorem 6 is based on finding accurate upper bounds
for the functions fn(s). We will focus on improving Nathanson’s bound on fn(s) in
[40, Chapter 9], combining his analytic approach with a more computational one. To
this aim we introduce an elementary method, namely, approximating an integral by
Riemann sums, to obtain an upper bound for the function fn(s) for ‘small’ n. The
chosen upper bound function is h(s) from (7) which was also used by Nathanson and
indeed appears to be a numerically good approximation for fn(s). Our aim will be to
find a value cn such that

(18) fn(s) ⩽ 2e
2(cn)n−1h(s)

when n is odd and s ⩾ 1, or if n is even and s ⩾ 2. Note that by the definitions (15)
and (7), we can take c1 = 1. Thus, it suffices to find values for cn for n ⩾ 2.
Our computational approach, which we detail in Section 2.2, yields the following
values for cn when 2 ⩽ n ⩽ 500. 6

Lemma 7. The bound (18) holds with cn as in Table 2 below.

n cn
2 0.33
3 0.39
4 0.45
5 0.51
6 0.54
 n cn
7 0.57
8 0.58
9 − 10 0.61
11 − 12 0.63
13 0.64
 n cn
14 0.65
15 − 18 0.66
19 − 20 0.67
21 − 26 0.68
27 − 34 0.69
 n cn
35 − 46 0.7
47 − 82 0.71
83 − 345 0.72
346 − 500 0.73

Table 2: Valid values of cn for 2 ⩽ n ⩽ 500

Certainly, it is possible to compute these values of cn to more decimal places and
larger n if required. We then extend Lemma 7 to all n by using the following analytic
result of Nathanson.

Lemma 8 ([40, Lemma 9.7]). For all n ⩾ 2 we have that (18) holds with

cn = 0.9607.

The rest of the proof of Theorem 6 is laid out as follows. In Section 2.2 we prove
Lemma 7. Then, in Section 2.3 we provide some useful bounds relating to the function
h(s). Finally, in Section 2.4 we finish the proof of Theorem 6. Explicit versions of the
inequality (4) are then included in a supplementary section 2.5.

2.2 Numerical approximation of fn(s)

Using the definition (15)–(17) of fn(s) we obtain

(19) sf2(s) =
 {
s − 3 log(s − 1) + 3 log 3 − 4, 2 ⩽ s ⩽ 4,
0, s ⩾ 4,

but for larger n the solution is more complicated. From (19) and the definition (7) of
h(s) we find c2 = 0.33 works in (18). For n ⩾ 3, we introduce a simple computational
framework to bound fn(s) above by h(s). We start by observing from (16) and (17),
that for n ⩾ 4 even and 2 ⩽ s ⩽ 4,

(20) sfn(s) = 3fn−1(3) log ( 3
s − 1
) + ∫ ∞

4 fn−1(t − 1)dt.

Therefore, by (17) and (20), we need to approximate
∫ ∞

max(3,s) fn−1(t − 1)dt

when s ⩾ 1 and n ⩾ 3 is odd, and
∫ ∞

max(4,s) fn−1(t − 1)dt

7

when s ⩾ 2 and n ⩾ 4 is even. Now, since fn(s) is decreasing in s, and fn(t) = 0 for
t ⩾ n + 2, we can use the Riemann sum approximation (with interval length 1/1000):
∫ ∞

σ fn−1(t − 1)dt ⩽
 1000(n−1)∑

i=0
 fn−1 ((σ − 1) + i
1000)

1000 ,(21)

with σ = max(3, s) or σ = max(4, s). Here, we chose an interval length of 1/1000 so
that the bound (21) was sharp enough for our purposes whilst still easy to calculate
on a modern computer. In particular, we ran some longer computations with smaller
intervals and only found a marginal improvement in our results.
After bounding the relevant integral in (21) one then obtains an upper bound for
fn(s) by (16), (17) or (20). For our purposes, we used (21) recursively to approximate
fn(1 + i/1000) for 3 ⩽ n ⩽ 499 odd and 0 ⩽ i ⩽ 1000(n + 1), and fn(2 + i/1000) for
4 ⩽ n ⩽ 500 even and 0 ⩽ i ⩽ 1000n.
Finally, we can use our bounds for fn(s) to compute cn for 3 ⩽ n ⩽ 500. More
precisely, we let xi = 1 + i/1000 if n is odd, and xi = 2 + i/1000 if n is even. Since
fn(s) and h(s) are decreasing, fn (xi) /h (xi+1) is an upper bound for fn(s)/h(s) for all
s ∈ [xi, xi+1]. Computing the maximum such bound over all intervals [xi, xi+1] to 2
decimal places (rounded up) then gives the values for cn in Table 2 and thereby proves
Lemma 7.

2.3 Bounds relating to h(s)

In this section we prove some useful bounds relating to h(s). Compared to Nathanson,
we split our results into more regions for s. This piecewise approach ultimately yields
better values for C1(ε) and C2(ε) in Table 1.
To begin with, we give the following lemma, which readily follows from the definition
(7) of h(s).

Lemma 9. Let γ3 = 4e/3 and for any 2 ⩽ s0 ⩽ 2.8, let γs0 = e
s0−2. Then

h(s − 1) ⩽
 {
γs0 · h(s), if 2 ⩽ s ⩽ s0 + 0.2,
γ3 · h(s), if s ⩾ 3.
(22)

Moreover, for 1 ⩽ s ⩽ 3

(23) 3
s h(2) ⩽ 3h(s).

Next, for s ⩾ 2, we define

(24) H(s) := ∫ ∞

s h(t − 1)dt and α := H(2)
2h(2) = e2H(2)
2 = 0.96068 . . . .

The following lemma is then an improved version of [40, Lemma 9.6] which bounds
H(s) in different ranges.

Lemma 10. Let κ2 = 0.9607, κ2.2 = 0.9557, κ2.4 = 0.9457, κ2.6 = 0.9261, κ2.8 = 0.8914
and κ3 = 0.8349. Then for s0 ∈ {2, 2.2, 2.4, 2.6, 2.8, 3}, we have

H(s) ⩽ κs0 · s · h(s), if s ⩾ s0.(25)
 8

In addition, for ˜κ = 0.9214,

H(3) ⩽ ˜κ · s · h(s), if 1 ⩽ s ⩽ 3.(26)

Proof. We start by proving (25). Firstly, for s ⩾ 4, we show the stronger bound

H(s) ⩽ 0.81 · s · h(s).

This follows from a repeated application of integration by parts:

1
3H(s) = ∫ ∞

s−1
 e−t

t dt

= e
1−s ( 1
s − 1 − 1
(s − 1)2 + 2
(s − 1)3
 ) − ∫ ∞

s−1
 6e
−t

t4 dt

⩽ e (1
3 − 1
32 + 2
33
 ) e−s

⩽ 0.81e−s.

That is, H(s) ⩽ 0.81 · 3e−s = 0.81 · s · h(s)
as claimed. Next we consider 3 ⩽ s ⩽ 4. In this case

1
3esH(s) = es ( 1
3
 ∫ 3

s−1 e−tdt + ∫ ∞

3
 e−t

t dt
)

⩽ 1
3 (
e − es−3) + 0.01305 · e
s,

which is maximised at s = 3. Thus,
1
3 e
−sH(s) ⩽ 1
3 (e − 1) + e3 · 0.01305 ⩽ 0.8349,

so that H(s) ⩽ κ3 · s · h(s) as required.
In the case 2 ⩽ s ⩽ 3, we have h(s) = e−s and

H(s) = ∫ 2

s−1 e
−2dt + ∫ 3

2 e−tdt + 3 ∫ ∞

3 e
−tt
−1dt = (4 − s)e
−2 − e
−3 + 3 ∫ ∞

3 e
−tt
−1dt,

hence e
s

s H(s) = e
s

s
 (
(4 − s)e
−2 − e
−3 + 3 ∫ ∞

3 e
−tt
−1dt) .(27)

Standard calculus arguments reveal that the right-hand side of (27) is decreasing.
Hence, for every s0 ∈ {2, 2.2, 2.4, 2.6, 2.8} we can substitute s0 into (27) to obtain that
H(s) ⩽ κs0 · s · h(s) for s ⩾ s0.
Finally, let us prove (26). If 2 ⩽ s ⩽ 3,

H(3) = H(2) − e
−2 = (2α − 1)e
−2 ⩽ e(2α − 1)
3 s · h(s),

since se−s is decreasing for s ⩾ 1. Then, if 1 ⩽ s ⩽ 2,

H(3) = (2α − 1)e
−2 ⩽ (2α − 1)sh(s).
9

The desired result then follows upon noting that

max { e(2α − 1)
3 , 2α − 1
} = 2α − 1 ⩽ 0.9214 = ˜κ. □

Remarks.
1. In [40, Lemma 9.7], the bound H(s) ⩽ α·s·h(s) is used to give cn = α ⩽ 0.9607.
That is, Lemma 8.
2. One could further split the regions of s for which we bound h(s − 1) and H(s).
This would slightly improve our final numerics, but further complicate our
ensuing arguments. We have chosen not to pursue such an optimisation as it is
unlikely to have any impact on our final application to Chen’s theorem.

2.4 Explicit version of the linear sieve

We now list some more definitions related to the linear sieve. Let P be a set of primes
and g(d) : N → C a multiplicative function. For 2 ⩽ z ⩽ D, with D ∈ R+, we define
V (z) as in (11) and let
 yn = yn(D, p1, . . . , pn) := ( D
p1 . . . pn
 ) 1
2 .

We wish to obtain an upper bound for

(28) Tn(D, z) := ∑

p1...pn∈P
yn⩽pn<...<p1<z
pm<ym∀m<n, m≡n (mod 2)
 g(p1 . . . pn)V (pn).

In particular, an upper bound on Tn(D, z) is the core ingredient used to obtain the
lower and upper bounds on S(A, P, z) in Theorem 6. To estimate Tn(D, z) we will
utilise our bounds on fn(s), h(s) and H(s) obtained in the previous sections.
Our main lemma is as follows, which improves on [40, Theorem 9.5]. Compared to
the work of Nathanson, we obtain a significant improvement by reducing the uniformity
in the parameters, which improves the overall accuracy in the induction step.

Lemma 11. Let z ⩾ 2, and D > 0 be real such that

s := log D
log z ⩾
 {
1 if n is odd,
2 if n is even.

Let P be a set of primes and g(d) be a multiplicative function such that

0 ⩽ g(p) < 1 for all p ∈ P

and

(29) V (u)
V (z) := ∏

p∈P
u⩽p<z
(1 − g(p))
−1 ⩽ K log z
log u,

for all u such that 1 < u < z and K such that

(30) 1 < K < 1 + ε
10

for some choice of ε > 0. Then

Tn(D, z) < V (z) (
fn(s) + ετne2h(s)
) ,

where τ1 = 3 and for n ⩾ 2

(31) τn :=
 {
τn−1 · max{ξ2, ξ2.2, ξ2.4, ξ2.6, ξ2.8, ξ3} if n even,
τn−1 · max{ξ3, ˜ξ} if n odd,

and
 ξs0 := κs0 + (γs0 + κs0) ε + 2γs0 (cn−1)
n−2

τn−1 + 2 (cn)
n−1

τn−1

˜ξ := ˜κ + (5 + 4ε)ε + 6(1 + ε)(cn−1)
n−2

τn−1 + 2(2 + ε)(cn)
n−1

τn−1
with γs0, κs0 and ˜κ as defined in Lemmas 9 and 10, and cn as defined in Section 2.1.

Proof. We start by defining

(32) hn(s) := ετne
2h(s).

We thus want to prove

(33) Tn(D, z) < V (z) (fn(s) + hn(s)) .

We proceed by induction on n. Let n = 1. By [40, Lemma 9.3] with β = 2, we have
T1(D, z) = 0 for s > 3. Since the right-hand side of (33) is positive, it follows that the
inequality holds for s > 3. If 1 ⩽ s ⩽ 3 then sf1(s) = 3 − s and

T1(D, z) = V (D1/3) − V (z),

by [40, (9.13)]. Hence, using (29),

T1(D, z)
V (z) ⩽ ( 3
s − 1
) + 3
s (K − 1) < f1(s) + h1(s).

This proves the lemma for n = 1. Now, let n ⩾ 2 and assume that the lemma holds for
n − 1. We begin with the case where s ⩾ 3. Using [40, Lemma 9.8] and the induction
hypothesis for n − 1 as done in [40, Theorem 9.5]

Tn(D, z)
V (z) <(K − 1)(fn−1(s − 1) + hn−1(s − 1))(34)
 + K
s
 ∫ ∞

s (fn−1(t − 1) + hn−1(t − 1))dt.

We now bound each term in (34) in terms of hn−1(s). Firstly, by (22) and (18),

(K − 1)fn−1(s − 1) < ε · 2e2(cn−1)
n−2h(s − 1)

⩽ ε · 2γ3 · e2(cn−1)n−2h(s) = 2γ3 (cn−1)n−2

τn−1 hn−1(s).
(35)

Then, again by (22)

(36) (K − 1)hn−1(s − 1) < ε · γ3 · hn−1(s).
11

Next, by (16) we have K
s
 ∫ ∞

s fn−1(t − 1)dt = Kfn(s).

To express this in terms of hn(s), we note that by (18)

(K − 1)fn(s) < ε · 2e2(cn)n−1h(s) = 2 (cn)
n−1

τn−1 hn−1(s)

so

(37) Kfn(s) < fn(s) + 2 (cn)n−1

τn−1 hn−1(s).

Finally, by the definition of H(s) and Lemma 10,
∫ ∞

s h(t − 1)dt = H(s) ⩽ κ3 · s · h(s),

and thus

(38) K
s
 ∫ ∞

s hn−1(t − 1)dt ⩽ κ3Khn−1(s) < κ3hn−1(s) + ε · κ3hn−1(s).

Combining (35), (36), (37) and (38)

Tn(D, z)
V (z) < fn(s) + ξ3 · hn−1(s) ⩽ fn(s) + hn(s),

as required. The case for n ⩾ 2 even and 2 ⩽ s ⩽ 3 is similar. In particular, for any
s0 ∈ {2, 2.2, 2.4, 2.6, 2.8} repeating the above argument gives

Tn(D, z)
V (z) < fn(s) + ξs0 · hn−1(s)

if s0 ⩽ s ⩽ s0 + 0.2. Now, let n ⩾ 3 be odd and 1 ⩽ s ⩽ 3. In this case, the recursion
formula (cf. Equation 34) is different and, following the proof of
1 [40, Theorem 9.5],
one obtains

Tn(D, z) < (K − 1)V (D1/3)(fn−1(2) + hn−1(2))

+ KV (D1/3)
3
 ∫ ∞

3 (fn−1(t − 1) + hn−1(t − 1))dt

⩽ 3K
s (K − 1)V (z)(fn−1(2) + hn−1(2))

+ K 2V (z)
s
 ∫ ∞

3 (fn−1(t − 1) + hn−1(t − 1))dt,(39)

where we have used that
 V (D1/3) ⩽ 3K
s V (z)

1Note that here we fix an error of Nathanson’s as he incorrectly claimed Tn(D, z) < V (z)(fn(3) +
hn(3)), which would contradict the optimality of the linear sieve (see e.g. [23, Section 12.3]).
12

by (29). One now argues similarly as before, using (23) and (26) to deduce that

3K
s (K − 1)fn−1(2) < 6(1 + ε)(cn)
n−2

τn−1 hn−1(s),

3K
s (K − 1)hn−1(2) < 3ε(1 + ε)hn−1(s),

K 2

s
 ∫ ∞

3 fn−1(t − 1)dt < fn(s) + 2(2 + ε)(cn)
n−1

τn−1 hn−1(s),

K 2

s
 ∫ ∞

3 hn−1(t − 1)dt < ˜κhn−1(s) + ε(2 + ε)˜κhn−1(s)

and thus Tn(D, z)
V (z) < fn(s) + ˜ξhn−1(s).

This completes the proof. □

As an example, in Table 3 we report upper bounds for τn for ε = 1/200 and n ⩽ 500,
obtained by Lemma 7. In particular, the upper bound for τn is computed recursively
using (31) with c1 = 1 and cn as in Table 2 for 2 ≤ n ≤ 500.

n τn
1 3
2 8
3 − 10 10
11 − 13 9
14 − 16 8
 n τn
17 − 20 7
21 − 24 6
25 − 30 5
31 − 37 4
38 − 46 3
 n τn
47 − 63 2
64 − 118 1
119 − 173 10
−1

174 − 228 10
−2

229 − 283 10
−3
 n τn
284 − 338 10
−4

339 − 393 10
−5

394 − 448 10
−6

449 − 500 10
−7

Table 3: Upper bound for τn for ε = 1/200.

Before continuing, we also provide an upper bound for τn that will be easier to work
with when n is large.

Lemma 12. Keep the notation of Lemma 11. Let τ ′
n be such that τ ′
1 = 3 and for n ⩾ 2

(40) τ ′
n := τ ′
n−1
 (κ2 + (γ2 + κ2)ε + 8e
3 (cn−1)
n−2

τ ′
n−1 + 2(2 + ε)(cn)n−1

τ ′
n−1
 )

Then, we have τn ⩽ τ ′
n whenever 0 < ε ⩽ 1/74.

Proof. We proceed by induction. First note that τ1 = τ ′
1 = 3 so that the result holds
for n = 1. Now suppose that n ⩾ 2 and τn−1 ⩽ τ ′
n−1. To begin with, we note that

κs0 + (γs0 + κs0)ε

is a linear function of ε. Thus, through elementary analysis one finds

max
s0∈{2, 2.2, 2.4, 2.6, 2.8, 3} {κs0 + (γs0 + κs0)ε} ⩽ κ2 + (γ2 + κ2)ε

13

provided ε ⩽ 1/54. Also, since γs0 ⩽ γ3 = 4e/3 and 2 ⩽ 2(2 + ε), one then has

τn−1ξs0 = τn−1
 (
κs0 + (γs0 + κs0) ε + 2γs0 (cn−1)n−2

τn−1 + 2 (cn)n−1

τn−1
 )

⩽ τ ′
n−1
 (κ2 + (γ2 + κ2) ε + 8e
3 (cn−1)n−2

τ ′
n−1 + 2(2 + ε)(cn)
n−1

τ ′
n−1
 ) = τ ′
n(41)

for all s0 ∈ {2, 2.2, 2.4, 2.6, 2.8, 3}. Similarly,

˜κ + (5 + 4ε)ε ⩽ κ2 + (γ2 + κ2)ε

provided ε ⩽ 1/74 so that

τn−1 ˜ξ = τn−1
 (˜κ + (5 + 4ε)ε + 6(1 + ε)(cn−1)n−2

τn−1 + 2(2 + ε)(cn)
n−1

τn−1
 )

⩽ τ ′
n−1
 (κ2 + (γ2 + κ2)ε + 8e
3 (cn−1)n−2

τ ′
n−1 + 2(2 + ε)(cn)
n−1

τ ′
n−1
 ) = τ ′
n.(42)

From (41) and (42), it follows that τn ⩽ τ ′
n as required. □

We can now effectively bound the upper and lower bound sieves constructed in [40,
Theorem 9.3] for S(A, P, z) and improve on [40, Theorem 9.6].

Proposition 13. Let z, D, s, P, g(d) and ε satisfy the hypotheses of Lemma 11. Let

G(z, λ±) := ∑

d|P (z) λ
±(d)g(d),

with λ±(d) the upper and lower bound sieves for S(A, P, z) constructed in [40, Theorem
9.3]. Then
 G(z, λ+) < V (z)
 (

F (s) + εe2h(s)
 ∞∑

n=1 τ2n−1
)

and
 G(z, λ−) > V (z)
 (

f (s) − εe2h(s)
 ∞∑

n=1 τ2n
)
 ,

where F (s) and f (s) are defined in (8), h(s) is defined in (7) and τn is defined in (31).

Proof. By [40, Lemma 9.3], we have

G(z, λ+) = V (z) +
 ∞∑

n=1
n≡1 (mod 2)
 Tn(D, z)

and
 G(z, λ−) = V (z) −
 ∞∑

n=1
n≡0 (mod 2)
 Tn(D, z).

The proof then follows upon applying our upper bound for Tn(D, z) in Lemma 11, and
the definitions (13) and (14) of F (s) and f (s) in terms of fn(s). □
14

We now obtain a bridging result which allows us to make Proposition 13 explicit.

Lemma 14. Let τn and τ ′
n be as defined in (31) and (40) respectively. For some choice
of ε ∈ (0, 1/74] and any ke, ko ⩾ 1, we have

(43) C1(ε) :=
 ∞∑

n=1 τ2n−1 ⩽
 ko∑

n=1 τ2n−1 + τ ′
2ko
 ∞∑

n=1 J(2ko + 1)2n−1

and

(44) C2(ε) :=
 ∞∑

n=1 τ2n ⩽
 ke∑

n=1 τ2n + τ ′
2ke+1
 ∞∑

n=1 J(2ke + 2)2n−1,

where

J(k) := κ2 + (γ2 + κ2) ε + 8e
6
 ( κ2
κ2 + (γ2 + κ2) ε
 )k−2 + 2(2 + ε)
3 κ
k−1
2
(κ2 + (γ2 + κ2) ε)k−2 .

Proof. First we note that since κ2 + (γ2 + κ2)ε < 1 for ε < 1/74, and
κ2
κ2 + (γ2 + κ2)ε < 1,

it follows that |J(k)| < 1 for sufficiently large k and the infinite sums in (43) and (44)
converge.
Now, we will only prove the inequality in (43) since (44) follows in an identical
fashion. So, to begin with, we use Lemma 12 to obtain

(45)
 ∞∑

n=1 τ2n−1 =
 ko∑

n=1 τ2n−1 +
 ∞∑

n=ko+1 τ2n−1 ⩽
 ko∑

n=1 τ2n−1 +
 ∞∑

n=ko+1 τ ′
2n−1.

Next we note that cn ⩽ κ2 = 0.9607 (Lemma 8) and by the definition (40) of τ ′
n, we
have τ ′
n ⩾ 3 · (κ2 + (γ2 + κ2)ε)
n−1.

Hence, again by (40), τ ′
n
τ ′
n−1 ⩽ J(n)

for all n ⩾ 2. This means that

τ ′
2ko+1 = τ ′
2ko
 ( τ ′
2ko+1
τ ′
2ko
 ) ⩽ τ ′
2koJ(2ko + 1),

and, since J(k) is decreasing in k, we have by induction

τ ′
2ko+2n−1 ⩽ τ ′
2koJ(2ko + 1)2n−1.

Substituting this into (45) then gives (43) as required. □

We can now conclude the proof of Theorem 6 using the above machinery.
15

Proof of Theorem 6. The proof of Theorem 6 is the same as [40, Theorem 9.7] but with
our bounds for C1(ε) and C2(ε) from Lemma 14. To obtain the values in Table 1 we
first choose ke = 250 and ko = 249 and then use Lemmas 7, 8, 11 and 12 to iteratively
compute τn for n ⩽ 500 and τ ′
n for n ⩽ 501. Finally, to bound the infinite series in
(43) and (44), we first compute J(2ke + 2) and J(2ko + 1) and then evaluate the sum
as a geometric series. □

Remark. The restriction ε ≤ 1/74 in Theorem 6 is required to prove the intermediary
result Lemma 12. It appears difficult to significantly weaken this restriction, especially
since we also require

(46) κ2 + (γ2 + κ2)ε < 1

in the proof of Lemma 14. In particular, with γ2 = e0.2 (Lemma 9) and κ2 = 0.9607
(Lemma 10), the inequality (46) necessitates that ε < 1/55.

2.5 Explicit bounds for ε in (4)

For our applications of Theorem 6 we will choose gn such that gn(p) = 1
p−1. With
this choice, we now prove a series of lemmas that will be used to give a value of ε in
(4).

Lemma 15. For all x ⩾ exp(20), there exists a prime in the interval [0.999x, x).

Proof. For exp(20) ⩽ x ⩽ 4 · 10
18 we use the results on gaps between primes in [42,
Table 8]. For x > 4 · 10
18, we use [33, Table 2]. □

Lemma 16. For all 2 ⩽ x ⩽ 10
12, we have

log log x + M < ∑

p⩽x
 1
p < log log x + M + 2
√x log x ,

with

(47) M := lim
x→∞
 (
∑

p⩽x
 1
p − log log x
)
 = 0.261497212847643 . . . .

Proof. The proof of the lemma is by direct computation. The computation took just
over 15 hours on an Intel Core i7 3.00GHz processor. To begin with, we used the
primesieve package in Python to compute all the primes up to 10
8, and used these
primes to directly verify the lemma up to x = 10
8. This process was then repeated for
all primes p satisfying 10
8 < p ⩽ 2 · 10
8, and then similarly for intervals of length 10
8

until we covered all primes up to 10
12. Note that were unable to store all primes up to
10
12 in one go due to the limited memory on our computer. □

Remark. Lemma 16 extends a computation due to Rosser and Schoenfeld [46, Theorem
20] by a factor of 104.

Lemma 17. For all x ⩾ 2, with M defined in (47), we have

(48) ∑

p⩽x
 1
p ⩾ log log x + M − 2.964 · 10
−6

log x ,

16

and for all x > exp(4000), we have

(49) ∑

p⩽x
 1
p ⩽ log log x + M + 1.436 · 10
−16

log x .

Proof. By [46, (4.20)] we have

(50) ∑

p⩽x
 1
p = log log x + M + θ(x) − x
x log x + ∫ ∞

x
 (y − θ(y))(1 + log y)
y2 log2 y dy,

where

(51) θ(x) = ∑

p⩽x log p,

is Chebyshev’s theta function. To obtain (49), we simply substitute into (50) the bound
for M1 in [6, Table 15], such that
 θ(x) − x ⩽ M1x
log x ,

corresponding to x > exp(4000), namely M1 = 5.7410 · 10
−13. To prove (48) for
2 ⩽ x ⩽ 10
12 we use Lemma 16. To prove (48) for x > 10
12 we take much more care.
Firstly, by [6, Table 15], the first error term in (50) can be bounded by
∣
∣
∣
∣θ(x) − x
x log x
 ∣
∣
∣
∣ ⩽ 6.9322 · 10
−5

log2 x .

We now split into the cases 10
12 < x ⩽ 10
19 and x > 10
19. In the first case, we have
∫ ∞

x
 (y − θ(y))(1 + log y)
y2 log2 y dy = ∫ 1019

x
 (y − θ(y))(1 + log y)
y2 log2 y dy

+ ∫ ∞

1019 (y − θ(y))(1 + log y)
y2 log2 y dy.

For the first integral, we use [8, Theorem 2] to obtain
∫ 1019

x
 (y − θ(y))(1 + log y)
y2 log2 y dy ⩾ ∫ 1019

x
 0.05(1 + log y)
y3/2 log2 y dy

= 0.05 [1
2 li ( 1
√
y
 ) − 1
√y log y
 ]1019

x

⩾ 0.05
√x log x − 0.025 li ( 1
√x
) − 7.077 · 10
−13,

where

(52) li(x) = ∫ x

0
 dt
log t ,

17

is the logarithmic integral function. For the second integral we again use [6, Table 15]
to obtain
∣
∣
∣
∣
∫ ∞

1019 (y − θ(y))(1 + log y)
y2 log2 y dy∣
∣
∣
∣ ⩽ 8.6315 · 10
−7 ( 1
2 log2(1019) + 1
log(1019)
) .

Thus, for 1012 < x ⩽ 10
19, we have an error term bounded below by

− 6.9322 · 10
−5

log2 x + 0.05
√x log x − 0.025 li ( 1
√
x
 ) − 7.077 · 10
−13

− 8.6315 · 10
−7 ( 1
2 log2(1019) + 1
log(1019)
)

⩾ −2.964 · 10
−6

log x .

For x > 10
19 an even sharper bound is obtained by simply substituting into (50) the
entry for M1 in [6, Table 15] corresponding to 1019. □

We are now able to obtain explicit bounds for ε in (4).

Lemma 18. Let z > exp(4000) and u0 = 10
9. Then for all u0 < u < z, we have

(53) ∏

u⩽p<z
 (1 − 1
p − 1
 )−1 < (1 + 1.452 · 10
−7) log z
log u.

Proof. We first note that
∏

u⩽p<z
 (
1 − 1
p − 1
)−1 = ∏

u⩽p<z
 ( (p − 1)
2

p(p − 2)
) ∏

u⩽p<z
 (
1 − 1
p
 )−1 .

By Lemma 15, noting that exp(20) < 10
9, we then have
∏

u⩽p<z
 ( (p − 1)2

p(p − 2)
) = ∏

u⩽p<z
 (
1 + 1
p(p − 2)
)

⩽ ∏

0.999u⩽p<z
 (
1 + 1
p2
 )

⩽ 1 + ∑

n⩾0.999u
 1
n2 ⩽ 1 + 1
0.999u − 1.

Thus,

(54) ∏

u⩽p<z
 (
1 − 1
p − 1
 )−1 < (1 + 1
0.999u − 1
 ) ∏

u⩽p<z
 (
1 − 1
p
)−1 .

Next, we note that

(55) ∏

u⩽p<z
 (
1 − 1
p
)−1 = exp
 (
− ∑

u⩽p<z log (
1 − 1
p
))
 .

18

Now, by Lemma 17
∑

u⩽p<z
 1
p = ∑

p<z
 1
p − ∑

p<u
 1
p ⩽ log log z − log log u + 1.436 · 10
−16

log z + 2.964 · 10
−6

log u
(56)
 = ∑

p<z
 1
p − ∑

p<u
 1
p ⩽ log log z − log log u + 1.431 · 10
−7(57)

since z > exp(4000) and u > u0 = 10
9. Hence, using (55), (56) and that for x ∈ (0, 1/2],

log(1 − x) ⩾ −x − x2, e
x ⩽ 1 + x + x2,

we have,
 ∏

u⩽p<z
 (
1 − 1
p
)−1 ⩽ log z
log u exp (
1.431 · 10
−7) exp
 (
∑

p⩾u
 1
p2
 )

⩽ log z
log u exp (
1.431 · 10
−7) exp
 (
∑

n⩾u
 1
n2
 )

⩽ log z
log u exp (
1.431 · 10
−7) (
1 + 1
u − 1 + 1
(u − 1)2
 ) .(58)

Using (54), (58), u > u0 = 109, and merging to the term log z
log u, gives the desired
result. □

Note that the range u was chosen to be near optimal for the final computations in
§9. It is also worth noting that the above result is one of the key numerical ingredients
in the proof of Theorem 3. In particular, sharpening the bound (53) is necessary if one
wishes to obtain a substantial improvement to the range of N in Theorem 3.

3 Some useful lemmas

In this section, we introduce some general explicit results from the literature that
will be highly useful. Here and throughout the rest of the paper, π(x), θ(x) and ψ(x)
(and their generalisations) denote the standard prime counting functions, µ(n) denotes
the M¨obius function and φ(n) denotes the Euler totient function.
We begin by giving some explicit expressions for the sieving functions f (s) and F (s)
defined in (8). For a particular range of s, one can do this inductively using the
definition of these functions. For our purposes, we will only need 0 < s ⩽ 4 so the
following lemma is restricted to this case only.

Lemma 19 ([12, Lemma 2]). Let f and F be as defined in (8). Then,

F (s) = 2e
γ

s , 0 < s ⩽ 3,(59)
 F (s) = 2e
γ

s
 (1 + ∫ s−1

2
 log(t − 1)
t dt) , 3 ⩽ s ⩽ 4,(60)
 f (s) = 0, 0 < s ⩽ 2,(61) 19

f (s) = 2e
γ log(s − 1)
s , 2 ⩽ s ⩽ 4.(62)

Next we give a general result which one can use to bound sums over arithmetic
functions.

Lemma 20 ([24, Lemma 1 (ii)]). Let f (t) be a positive, monotone function defined for
w ⩽ t ⩽ z with f ′(t) piecewise continuous on [w, z], and c(n) be an arithmetic function
satisfying ∑

x⩽n<y c(n) ⩽ g(y) − g(x) + E,

for some constant E whenever w ⩽ x < y ≤ z. Then,
∑

w⩽n<z c(n)f (n) ⩽ ∫ z

w f (t)g′(t)dt + E max (f (w), f (z)) .

Finally, we give some explicit bounds on functions relating to primes and prime
factors.

Lemma 21 (See [46, Theorem 5]). For any a > 1 and b ⩾ 286,

(63) ∑

a⩽p⩽b
 1
p < log log b − log log a + 1
log2 a.

Lemma 22. Let ω(n) count the number of unique prime divisors of n ⩾ 3. We have

(64) ω(n) ⩽ log n
log 2
and

(65) ω(n) < 1.3841 log n
log log n .

Proof. The first bound (64) follows by noting that each prime factor of n is greater
than or equal to 2. The second bound (65) is [43, Theorem 11]. □

Certainly, the bound (65) is stronger asymptotically than (64) and in fact stronger
explicitly when n ⩾ 14. However, in some cases where the error terms we are working
with are insignificant, we will use the simpler bound (64) to improve readability.

Lemma 23. For all x ⩾ 45, we have

(66) ∑

n⩽x µ
2(n) ⩽ 0.65x.

Proof. For x ⩾ 10
5, the result follows by [7, (4.6)]. For smaller values of x, the result
can be verified via a simple computation. □

Lemma 24 ([7, Lemma 4.5]). For all x ⩾ 10
9, we have
∑

n⩽x
 µ2(n)
φ(n) ⩽ log x + Bµ,φ + 58
√
x ⩽ 1.1 log x,

where Bµ,φ = 1.332 . . . is a constant. 20

Lemma 25. For all x ⩾ 2 and θ defined in (51), we have

θ(x) < x (
1 + 9 · 10
−7

log x
 ) .

Proof. For 2 ⩽ x < 10
19, the result follows by [8, Theorem 2]. For x > 10
19 the result
follows by [6, Table 15]. □

While most of the results above are not optimal, they are sufficient for our purposes.

4 Results on primes in arithmetic progressions

As is commonplace in applications of the linear sieve, the remainder terms r(d)
(defined in (3)) essentially correspond to the error term for the prime number theorem
in arithmetic progressions. Thus in this section, we will obtain estimates for

(67) Ef (x; k, l) := f (x; k, l) − f (x)
φ(k),

for f = π, θ, ψ, the standard prime counting functions, where f (x; k, l) means that the
counting function f (x) is restricted to n ≡ l (mod k) for n ⩽ x. In particular, for
our application we are interested in averaged estimates for Eπ(N, d, N ) with N a large
integer and d square-free. Such estimates will allow us to bound the total remainder
R (see (10)) in the linear sieve.
We start with a result on the zeroes of Dirichlet L-functions, namely [32, Theorem
1.1 & 1.3].

Theorem 26 (Kadiri). Define ∏(s, q) = ∏
χ (mod q) L(s, χ), where the product is over
Dirichlet characters χ (mod q), R0 = 6.3970 and R1 = 2.0452. Then the function∏(s, q) has at most one zero ρ = β + iγ, in the region β ⩾ 1 − 1/ (R0 log max (q, q |γ|)).
Such a zero is called a Siegel zero and if it exists, then it must be real, simple and
correspond to a non-principal real character χ (mod q). Moreover, for any given Q1,
among all the zeroes of primitive characters with modulus q ⩽ Q1 there is at most
one zero with β ⩾ 1 − 1/2R1 log Q1, we will call this zero and the related modulus
exceptional.

We now introduce a bound on Eψ(x; k, l) that is a specific case of [4, Theorem 1.2,
Table 6]. Namely, using the notation of [4], we set Y0 = 10.4, α1 = 10 and α2 = 8. We
will also use the following notation:

(68) π(x, χ) := ∑

p⩽x χ(p), ψ(x, χ) := ∑

n⩽x Λ(n)χ(n), θ(x, χ) := ∑

p⩽x χ(n) log p,

where χ denotes a Dirichlet character.

Lemma 27. Let Eψ(x; k, l) and ψ(x, χ) be as in (67) and (68) respectively. Let
x ⩾ exp(exp(10.4)) and k < log10 x be an integer. Let Indk = 1 if βk, the Siegel
zero modulo k, exists and Indk = 0 otherwise. Then,

φ(k)
x |Eψ(x; k, l)| < 3.2 · 10
−8

log8 x + Indk xβk−1

βk
21

and

(69) −1 + x−1 ∑

χ (mod k) |ψ(x, χ)| < 3.2 · 10
−8

log8 x + Indk xβk−1

βk .

Importantly, the -1 appearing in (69) appears when bounding the contribution from
the principal character in the proof of [4, Theorem 1.2]. Thus, we also have the following
variant of Lemma 27.

Lemma 28. Keep the notation and conditions of Lemma 27 and let χ0 denote the
trivial character modulo k. We have

x−1 ∑

χ (mod k)
χ̸=χ0
 |ψ(x, χ)| < 3.2 · 10
−8

log8 x + Indk xβk−1

βk .

We now introduce a function x2(x) = x/ log15 x < x. In doing so, we can apply a
partial summation argument and obtain a sufficiently strong analogue of Lemma 28
for the sum over |π(x, χ)|.

Lemma 29. Let π(x, χ) be as in (68). Let x2(x) = x/ log15 x. Also assume x > X1,
with X1 such that log log x2(X1) ⩾ 10.4. We then have, for k < log10(x2(x))

(70) ∑

χ (mod k)
χ̸=χ0
 |π(x, χ)| < vk(X1)x
log5 x ,

where
(71)

vk(X1) := v′
k(X1)
 

1 + 1
log10(X1) log5 x2(X1) + 1
(1 − 6
log x2(X1) ) log X1
 

 + 3
log(X1),

and
 v′
k(X1) := max
y⩾x2(X1)
 [3.2 · 10
−8

log4 y + log4 y (
Indk yβk−1

βk + 1.02 log10 y
√y + 3 log10 y
y2/3
 )] .(72)

with Indk and βk as in Lemma 27.

Proof. Let y ∈ [x2(x), x]. By Lemma 28, we have
∑

χ (mod k)
χ̸=χ0
 |ψ(y, χ)| < 3.2 · 10
−8y
log8 y + Indk yβk

βk .

We then use the estimate |ψ(y, χ) − θ(y, χ)| ⩽ ψ(y) − θ(y) < 1.02y1/2 + 3y1/3 ([46,
(3.39)]) to obtain ∑

χ (mod k)
χ̸=χ0
 |θ(y, χ)| < v′
k(X1)y
log4 y .

22

Finally, by partial summation,

π(x, χ) = π(x2(x), χ) + θ(x, χ)
log x − θ(x2(x), χ)
log x2(x) + ∫ x

x2(x)
 θ(y, χ)
y log2 y dy,

where, using that x2(x) is increasing within the concerned range of x,

∫ x

x2(x)
 ∑
χ (mod k)
χ̸=χ0 |θ(y, χ)|

y log2 y dy ⩽ v1(X1)
1 − 6
log x2(X1)
 ∫ x

x2(x)
 1
log6 y
 (
1 − 6
log y
 ) dy

⩽ v1(X1)
1 − 6
log x2(X1) · x
log6 x

and
 ∑

χ (mod k)
χ̸=χ0
 |π(x2(x), χ)| = ∑

χ (mod k)
χ̸=χ0
 ∣
∣
∣
∣
∣
∣
 ∑

p⩽x2(x) χ(p)
∣
∣
∣
∣
∣
∣ = ∑

χ (mod k)
χ̸=χ0
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

a (mod k)
(a,k)=1
 χ(a) ∑

p⩽x2(x)
p≡a (mod k)
 1

∣
∣
∣
∣
∣
∣
∣
∣

⩽ (φ(k))
2 max
a
(a,k)=1 π(x2(x); k, a)

which, by an explicit form of the Brun–Titchmarsh theorem [38, Theorem 2], is bounded
above by
 φ(k) 2x2(x)
log(x2(x)/k) ⩽ φ(k) 3x2(x)
log x2(x) ⩽ k · 3x2(x)
log x2(x) ⩽ 3x
log6 x.

This proves (70) as required. □

4.1 Notation and conditions

We now introduce some further notation and conditions that will be used throughout.
First, we let 0 < δ < 2 be a parameter, X2 and X3 be fixed positive real numbers,
and N be a positive even integer which we will set to be greater than either X2 or X3.
Then, we set X, Y, Z > 0 to be real numbers such that

(73) N
y < X ⩽ N
z , XY < 2N, Y > Z, Y > z,

where

(74) z = N 1/8, and y = N 1/3.

In the final part of our sieving process (§8), precise expressions will be given for X, Y
and Z. We also define

x1 = x1(N ) := N
log5 N , x2 = x2(Y ) := Y
log15 Y ,(75)
 Kδ(x) := logδ x, Q1(x) := log10 x, P (z) := ∏

p<z
p∤N
 p.(76)
 23

As in Lemma 29, the functions x1 and x2 will be used to control the error term
resulting from partial summation arguments. Now, let i ∈ {1, 2}. With regard to
Theorem 26, we let k0(xi) be the exceptional modulus up to Q1(xi) (if it exists) and

(77) ki :=
 {
k0(xi), if k0(xi) exists and (k0(xi), N ) = 1,
0, otherwise.

By [39, pp. 296–297], k0(xi) is square-free or 4 times a square-free number. Thus, since
N is even, ki is a square-free odd number whenever ki ̸= 0.
In what follows, we will separately consider the cases ki < Kδ(xi) and Kδ(xi) ⩽ ki ⩽
Q1(xi). This is because if ki < Kδ(xi) then we can directly bound the contribution of
the Siegel zero in Lemma 27 using the results of [2] and [3]. On the other hand, if ki
is too large this is not possible so a more complicated argument is required as to avoid
the contribution from the exceptional zero.

4.2 The case when the exceptional modulus is small

We first consider the case

(78) ki < Kδ(xi) = logδ xi,

where the value of i ∈ {1, 2} will be specified for each result. We begin with the
following lemma, which is very similar
2 to [4, Theorem 1.4].

Lemma 30. Let Eψ(x; k, l) be as in (67) and N be a positive even integer. Suppose
x1 = x1(N ), Kδ(x1), and Q1(x1) are defined by (75) and (76), k1 < Kδ(x1), and
log log x1 ⩾ 10.4. Let H = H(N ) := √x1
log10 x1 and y ∈ [x1, N ]. We have

∑

d⩽H
(d,N )=1
 µ
2(d) |Eψ(y; d, N )| < 1.1 log(Q1(x1)) ( 3.2 · 10
−8y
log8 y + yβ0(x1)

β0(x1)
)

+ 27 · E(y) + √
y
2(log 2) log8 y + 0.4 log3 y,(79)

where

(80) E(y) := 4y log 9
2 y
log10 x1(y) + 4y
log5.5 y + 18y 11
12

log 1
2 y + 5
2y 5
6 log 11
2 y

and

(81) β0(x1) := 1 − ν(x1), ν(x1) := min
 { 100
√
Kδ(x1) log2 Kδ(x1), 1
2R1 log(Q1(x1))
}
 ,

with R1 = 2.0452 as in Theorem 26.

2In the proof of Lemma 30 we also fix a couple of errors in the proof of [4, Theorem 1.4]. For
example, the bound (12) in [4] is missing a factor of log x. This error also appears in the proof of [4,
Theorem 1.2] but contributes so little that none of the final computational results are affected.
24

Proof. By [39, (11.22)] we have for (a, q) = 1

ψ(x; q, a) = 1
φ(q)
 ∑

χ χ(a)ψ(N, χ),

with ψ(x; q, a) defined as in (4), and thus,

ψ(y; d, N ) − ψ(y)
φ(d) = 1
φ(d)
 ∑

χ (mod d)
χ̸=χ0
 χ(N )ψ(y, χ) − 1
φ(d)(ψ(y) − ψ(y, χ0)),

where χ0 denotes the trivial character modulo d. We note that if χ∗ induces χ modulo
d, recalling the definition for ψ(y, χ) in (68), then by Lemma 22

(82) |ψ(y, χ) − ψ(y, χ
∗)| ⩽ ∑

pm⩽y
m|d
 log p ⩽ log y ∑

p|d 1 ⩽ log y log d
log 2 ⩽ log2 y
2 log 2.

Thus,
 |ψ(y) − ψ(y, χ0)| ⩽ log2 y
2 log 2,

so that by Lemma 24

(83) ∑

d⩽H
(d,N )=1
 µ2(d)
φ(d) |ψ(y) − ψ(y, χ0)| ⩽ log2 y
2 log 2
 ∑

d⩽H
(d,N )=1
 µ2(d)
φ(d) ⩽ 0.4 log3 y.

It remains to bound ∑

d⩽H
(d,N )=1
 µ2(d)
φ(d)
 ∑

χ (mod d)
χ̸=χ0
 |ψ(y, χ)|.

For this we consider two cases 1 ⩽ d ⩽ Q1(x1) and Q1(x1) < d ⩽ H. In the first case,
we have by Lemmas 24 and 28

(84) ∑

d⩽Q1(x1)
(d,N )=1
 µ2(d)
φ(d)
 ∑

χ (mod d)
χ̸=χ0
 |ψ(y, χ)| ⩽ 1.1 log Q1(x1) ( 3.2 · 10
−8y
log8 y + yβ0(x1)

β0(x1)
) ,

where β0(x1) is as defined in (81). To see why each potential Siegel zero βd modulo d
satisfies βd ⩽ β0(x1) we consider two cases:
(a) Suppose k1 | d. Then k1 = k0(x1) is non-zero and bounded above by Kδ(x1) by
the assumption in (78). The Siegel zero βd is the exceptional zero modulo k1,
and thus bounded by [2, Theorem 1.3] and [3, Theorem 1.3] as follows

βd ⩽ 1 − 100
√
Kδ(x1) log2 Kδ(x1).

(b) Suppose k1 ∤ d and recall the definition of k1 in (77). If k1 = 0, then either
k0(x1) does not exist or (k0(x1), N ) ̸= 1 and d is not divisible by the exceptional
25

modulus k0 because (d, N ) = 1. If k1 ̸= 0, then k1 = k0(x1) ∤ d and again βd is
not exceptional. In both cases βd can be bounded by Theorem 26, that is

βd ⩽ 1 − 1
2R1 log(Q1(x1)).

Combining cases (a) and (b) gives (81) as desired. Now we consider Q1(x1) < d ⩽ H.
For this range of d, we roughly follow the proof of [1, Theorem 1.3]. First, by (82),

(85) 1
φ(d)
 ∑

χ (mod d)
χ̸=χ0
 |ψ(y, χ)| ⩽ 1
φ(d)
 ∑

χ (mod d) |ψ(y, χ
∗)| + log2 y
2 log 2.

Letting ∑∗ denote the sum over all primitive characters, we then have

∑

Q1(x1)<d⩽H
(d,N )=1
 µ2(d)
φ(d)
 ∑

χ (mod d)
χ̸=χ0
 |ψ(y, χ)|

⩽ ∑

Q1(x1)<d⩽H
(d,N )=1
 µ2(d)
φ(d)
 ∑

χ (mod d) |ψ(y, χ
∗)| + H log2 y
2 log 2

⩽
 ( ∑

1⩽m⩽H
 µ2(m)
φ(m)
 ) ∑

Q1(x1)<d⩽H
(d,N )=1
 µ2(d)
φ(d)
 ∑∗

χ (mod d) |ψ(y, χ)| + √y
2(log 2) log8 y

⩽ 1.1 log y ∑

Q1(x1)<d⩽H
(d,N )=1
 µ2(d)
φ(d)
 ∑∗

χ (mod d) |ψ(y, χ)| + √y
2(log 2) log8 y ,(86)

where in the second inequality we used that φ(ab) ⩾ φ(a)φ(b) and in the third inequal-
ity we used Lemma 24 and that H is an increasing function in the range of interest.
To finish off, one repeats the argument from [1, pp. 1929–1930], whereby [1, Theorem
1.2] and partial summation give

log y ∑

Q1(x1)<d⩽H
(d,N )=1
 µ2(d)
φ(d)
 ∑∗

χ (mod d) |ψ(y, χ)|

⩽ 1.1
2 log y · 48.84 (
4 y
Q1(x1) + 4y 1
2 H + 18y 2
3 H 1
2 + 5y 5
6 log ( eH
Q1(x1)
)) (log y) 7
2

⩽ 27 · E(y).

This proves the lemma. □

We now convert the above result into a statement involving π(x).

26

Lemma 31. Keep the notation and conditions of Lemma 30, and assume N ⩾ X2
with log log x1(X2) ⩾ 10.4. Then
∑

d⩽H
(d,N )=1
 µ2(d)|Eπ(N ; d, N )| < p(X2)N
log3 N

with

p(X2) := p1(X2)
 

1 + 1
log2 X2 log3 x1(X2) + 1
(1 − 4
log x1(X2) ) log X2
 

 + 2.2
log2 X2 ,

p1(X2) := p2(X2) + 1
log8 x1(X2)
 (

0.67 + 2

x1(X2) 1
6
 )
 ,

p2(X2) := max
y⩾x1(X2)
 [log2 y
y
 (
1.1 log(Q1(y)) ( 3.2 · 10
−8y
log8 y + yβ0(x1)

β0(x1)
)
(87)
 +27 · E(y) + √y
2(log 2) log8 y + 0.4 log3 y)] .

Proof. Let y ∈ [x1(N ), N ]. By Lemma 30
∑

d⩽H
(d,N )=1
 µ2(d)|Eψ(y; d, N )| ⩽ p2(X2)y
log2 y .

Next, since |ψ(y; d, N ) − θ(y; d, N )| ⩽ ψ(y) − θ(y) ⩽ 1.02y1/2 + 3y1/3 ([46, (3.39)])
we have

|Eψ(y; d, N ) − Eθ(y; d, N )| = ∣
∣
∣
∣ψ(y; d, N ) − θ(y; d, N ) − ψ(y) − θ(y)
φ(d)
 ∣
∣
∣
∣

< max {
1.02y1/2 + 3y1/3, 1.02y1/2 + 3y1/3

φ(d)
 }

= 1.02y1/2 + 3y1/3,

noting that ψ(y; d, N ) − θ(y; d, N ) and ψ(y)−θ(y)
φ(d) are both positive.
Thus, using Lemma 23
∑

d⩽H
(d,N )=1
 µ2(d)|Eθ(y; d, N )| ⩽ ∑

d⩽H
(d,N )=1
 µ2(d)|Eψ(y; d, N )| + 0.65H(1.02y1/2 + 3y1/3)

⩽ p1(X2)y
log2 y .(88)

Next, by partial summation

Eπ(N ; d, N ) = Eπ(x1; d, N ) + Eθ(N ; d, N )
log N − Eθ(x1; d, N )
log x1 + ∫ N

x1
 Eθ(y; d, N )
y log2 y dy.(89)
 27

Now, by the Brun-Titchmarsh theorem [38, Theorem 2],

π(x1, d; N ) < 2x1
log(x1/d)φ(d)

and π(x1)
φ(d) < 2x1
log(x1)φ(d) ⩽ 2x1
log(x1/d)φ(d),

for any integer d ⩾ 1. By combining this with Lemma 24, we get
∑

d⩽H
(d,N )=1
 µ2(d)|Eπ(x1; d, N )| ⩽ 2 x1
log(x1/H)
 ∑

d⩽H
(d,N )=1
 µ2(d)
φ(d) ⩽ 2.2x1.

Then, ∑

d⩽H
(d,N )=1
 µ2(d) ∣
∣
∣
∣
∫ N

x1
 Eθ(y; d, N )
y log2 y dy∣
∣
∣
∣ ⩽ p1(X2)
1 − 4
log x1(X2)
 ∫ N

x1
 1
log4 y
 (1 − 4
log y
 ) dy

< p1(X2)
1 − 4
log x1(X2) · N
log4 N .

The remaining terms of (89) can be bounded using (88) to give
∑

d⩽H
(d,N )=1
 µ2(d)|Eπ(N ; d, N )| < p(X2)N
log3 N

as required. □

Finally, we prove an upper bound related to a bilinear form, to be used in Section 8.

Lemma 32. Suppose N is a positive even integer, y = N 1
3 , z = N 1
8 and X, Y, Z > 0
be real numbers such that
N
y < X ⩽ N
z , XY < 2N, Y > Z, Y > z.

Let a(n) be an arithmetic function with |a(n)| ⩽ 1 for all n. Suppose x2 = x2(Y ) and
Kδ(x2) are defined by (75) and (76) respectively, k2 < Kδ(x2), and N > (X3)
8, with
X3 such that log log x2(X3) ⩾ 10.4. With D∗ = √XY
log10 Y , we have

(90) ∑

d<D∗
d|P (y)
 max
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

Z⩽p<Y
np≡N (mod d)
 a(n) − 1
φ(d)
 ∑

n<X
 ∑

Z⩽p<Y
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
 ⩽ m(X3)XY
log3 Y ,

Here,

m(X3) := 39v0(X3) + 108 log16 X3
X3 log log X3 + 26 log5 X3
log10(x2(X3)) + 88 log5 X3
 ( 1

X
 8
3
3 + 1

X
 1
2
3
 )
 + 106
log6 X3
28

and v0(X3) is equal to vk(X3) from Lemma 29 but with βk (appearing in (72)) replaced
with

(91) β0(x2) := 1 − ν(x2), ν(x2) := min
 { 100
√
Kδ(x2) log2 Kδ(x2), 1
2R1 log(Q1(x2))
}
 .

Note that R1 = 2.0452 as in Theorem 26.

Proof. Following [40, §10.7], we write χ = χ0,sχ1 with d = sr and χ1 primitive, and
rewrite the left-hand side of (90) as

∑

rs<D∗
rs|P (y)
 1
φ(sr)
 ∑∗

χ (mod r)
χ̸=χ0,r
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
∣
∣
 ∑

Z⩽p<Y
p∤s
 χ(p)

∣
∣
∣
∣
∣
∣
∣
∣
 ,(92)

where ∗ means that the sum is restricted to primitive characters. We begin estimating
the sum restricted to r < D0, with

(93) D0 := log10(x2(Y )).

Since Y > Z, Y > z = N 1
8 and N > (X3)
8, we obtain, by Lemma 29,

∑∗

χ (mod r)
χ̸=χ0,r
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

Z⩽p<Y
p∤s
 χ(p)

∣
∣
∣
∣
∣
∣
∣
∣
 ⩽ ∑

χ (mod r)
χ̸=χ0,r
 (|π(⌈Y − 1⌉, χ) − π(⌊Z + 1⌋, χ)| + ω(s))

⩽ 2vr(X3)Y
log5 Y + 1.3841φ(r) log D∗

log log D∗ ,

(94)

where we used Lemma 22 to bound ω(n). The Siegel zero βr (appearing in the function
vr(X3)) satisfies βr ⩽ β0(x2) by the same argument as in the proof of Lemma 30. Hence
vr(X3) can be bounded by v0(X3) in (94). Then, using Lemma 24 and |a(n)| ⩽ 1 we
obtain
 ∑

rs<D∗
r<D0
rs|P (y)
 1
φ(rs)
 ∑∗

χ (mod r)
χ̸=χ0,r
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
∣
∣
 ∑

Z⩽p<Y
p∤s
 χ(p)

∣
∣
∣
∣
∣
∣
∣
∣

⩽ ( 2v0(X3)XY
log5 Y + 1.3841D0X log D∗

log log D∗
 ) ( ∑

l⩽D∗
 µ2(l)
φ(l)
 )2

⩽ 2.42v0(X3)XY log2 D∗

log5 Y + 1.21 · 1.3841D0X log3 D∗

log log D∗

⩽ 39v0(X3)XY
log3 Y + 108X log13 Y
log log Y ,(95)
 29

where in the last line we used that log3 D∗

log log D∗ increases for 5 ⩽ D∗ and D∗ ⩽ Y 4, which
follow readily from the restrictions on X and Y and the definition of D∗. We are
now left with estimating the sum in (92) restricted to r ⩾ D0, which upon using
φ(rs) ⩾ φ(r)φ(s) is bounded by

∑

s<D∗
s|P (y)
 1
φ(s)
 ∑

D0⩽r⩽D∗
r|P (y)
 1
φ(r)
 ∑∗

χ (mod r)
χ̸=χ0,r
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
∣
∣
 ∑

Z⩽p<Y
p∤s
 χ(p)

∣
∣
∣
∣
∣
∣
∣
∣
 .

To do so, we divide the interval D0 ⩽ r ⩽ D∗ into subintervals of the form

Dk ⩽ r ⩽ 2Dk, where Dk := 2
kD0, 0 ⩽ k ⩽ log(D∗/D0)
log 2 .

Using the Cauchy–Schwarz inequality and the large sieve inequality [20, p. 160] as in
the proof of [40, Theorem 10.7], we obtain, for each Dk,

∑

Dk⩽r<2Dk
r|P (y)
 1
φ(r)
 ∑∗

χ (mod r)
χ̸=χ0,r
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
∣
∣
 ∑

Z⩽p<Y
p∤s
 χ(p)

∣
∣
∣
∣
∣
∣
∣
∣

⩽ 1
Dk
 



 ∑

Dk⩽r<2Dk
 ∑∗

χ (mod r)
χ̸=χ0,r
 r
φ(r)
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

·
 



 ∑

Dk⩽r<2Dk
 ∑∗

χ (mod r)
χ̸=χ0,r
 r
φ(r)
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

Z⩽p<Y
p∤s
 χ(p)

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

⩽ 1
Dk
 (
(X + 12D2
k)(Y + 12D2
k)XY ) 1
2

= ((XY )
2

D2
k + 12XY 2 + 12Y X 2 + 144D2
kXY ) 1
2

⩽XY
D0 + √12XY + √12Y X + 12Dk√XY .

Thus, summing over 0 ⩽ k ⩽ log(D∗/D0)
log 2 and using Lemma 24,

∑

s<D∗
s|P (y)
 1
φ(s)
 ∑

D0<r<D∗
r|P (y)
 1
φ(r)
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

n<X
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
∣
∣
 ∑

Z⩽p<Y
p∤s
 χ(p)

∣
∣
∣
∣
∣
∣
∣
∣

30

⩽ 1.1 log D∗ [log D∗

log 2
 ( XY
log10(x2(Y )) + √
12XY ( 1
√X + 1
√
Y
 )) + 24D∗√XY ]

⩽ 26XY log2(Y )
log10(x2(Y )) + 88XY log2 Y ( 1
√X + 1
√Y
 ) + 106XY
log9 Y ,(96)

where we have again used D∗ ⩽ Y 4 and also ∑

k Dk ⩽ 2D∗. We now obtain the desired
result from (92), (95) and (96). □

4.3 The case when the exceptional modulus is large

We recall that for i ∈ {1, 2}, k0(xi) denotes the modulus of the exceptional zero
up to Q1(xi) (Equations (75) and (76)) if it exists and ki is defined by (77). In this
section, we suppose that ki ⩾ Kδ(xi) = logδ xi. This means that (k0(xi), N ) = 1 and
thus ki = k0(xi). Several of the following lemmas will be slight variations on those in
Section 4.2.

Lemma 33. Suppose N is a positive even integer. Let Ef (x; k, l) be as in (67). Suppose
k1 ⩾ Kδ(x1), N ⩾ X2, and log log x1(X2) ⩾ 10.4. Then, for any k strictly dividing k1,

φ(k)
N |Eπ(N ; k, N )| < c(X2)
log3 N ,

with

c(X2) := c1(X2)
 

1 + 1
log2(X2) log3 x1(X2) + 1
(1 − 4
log x1(X2)) log X2
 

 + 1
log2 X2 ,

c1(X2) := max
y⩾x1(X2)
 [ 3.2 · 10
−8

log6 y + log2 y
( (1 − 1
2R1 log Q1(y)
)−1 y− 1
2R1 log Q1(y)

+ Q1(y) ( 1.02
√y + 3
y2/3
 ) + 9.4(log y)
1.515 exp(−0.8274
√
log y)

)]

.(97)

Proof. Let y ∈ [x1(N ), N ]. Let βk be the Siegel zero modulo k if it exists. Since
k strictly divides k1, it is not the exceptional modulus k0 up to Q1(x1) and thus by
Theorem 26,

(98) βk ⩽ 1 − 1
2R1 log Q1(x1) ⩽ 1 − 1
2R1 log Q1(y).

Then, since yβk −1

βk increases as a function of βk,

yβk−1

βk ⩽ (1 − ν(y))
−1y−ν(y),

with ν(y) = 1
2R1 log Q1(y) . Thus by Lemma 27,

φ(k)
y
 ∣
∣
∣
∣ψ(y; k, N ) − y
φ(k)
∣
∣
∣
∣ < 3.2 · 10
−8

log8 y + (1 − ν(y))
−1y−ν(y).

31

By definition, k1 is the exceptional modulus up to Q1(x1(N )) hence φ(k) < k1 ⩽
Q1(x1(N )) ⩽ Q1(y). Thus, using |ψ(y; k, N ) − θ(y; k, N )| ⩽ ψ(y) − θ(y) ⩽ 1.02y1/2 +
3y1/3 ([46, (3.39)]), we obtain

φ(k)
y
 ∣
∣
∣
∣θ(y; k, N ) − y
φ(k)
∣
∣
∣
∣ < 3.2 · 10
−8

log8 y + (1 − ν(y))
−1y−ν(y) + Q1(y) ( 1.02
√y + 3
y2/3
 ) .

Then, by [30, Corollary 1.2 & Table 1, l.1] and the triangle inequality

φ(k)
y |Eθ(y; k, N )| < 3.2 · 10
−8

log8 y + (1 − ν(y))
−1y−ν(y) + Q1(y) ( 1.02
√
y + 3
y2/3
 )

+ 9.4(log y)
1.515 exp(−0.8274
√
log y).

Therefore, φ(k)
y |Eθ(y; k, l)| < c1(X2)
log2 y ,

with c1(X2) defined in (97).
It remains to express Eπ(x; k, N ) by partial summation

Eπ(N ; k, N ) = Eπ(x1; k, N ) + Eθ(N ; k, N )
log N − Eθ(x1; k, N )
log x1 + ∫ N

x1
 Eθ(y; k, N )
y log2 y dy,

where
 φ(k) ∣
∣
∣
∣
∫ N

x1
 Eθ(y; k, N )
y log2 y dy∣
∣
∣
∣ ⩽ c1(X2)
1 − 4
log x1(X2)
 ∫ N

x1
 1
log4 y
 (
1 − 4
log y
 ) dy

< c1(X2)
1 − 4
log x1(X2)
 N
log4 N

and, by [38, Theorem 2]

φ(k)
N |Eπ(x1; k, N )| ⩽ max { φ(k)
N π(x1; k, N ), π(x1)
N
 }

⩽ max { 2x1
N log(x1/k), x1
N
 }

= x1
N

= 1
log5 N .

Therefore,
 φ(k)
N |Eπ(N ; k, N )| < c(X2)
log3 N

as required. □

Next we introduce some variants of Lemma 31.
32

Lemma 34. Suppose N is a positive even integer. Let Ef (x; k, l) be as in (67). Suppose
k1 ⩾ Kδ(x1), N ⩾ X2, and log log x1(X2) ⩾ 10.4. Then
∑

d⩽H
(d,N )=1
k1∤d
 µ2(d)|Eπ(N ; d, N )| < p∗(X2)N
log3 N ,

where p∗(X2) = p(X2) as in Lemma 31 with the ∗ indicating that β0(x1) (appearing in
(87)) is replaced by

(99) β∗
0(x1) := 1 − 1
2R1 log(Q1(x1))

which is sharper than (81).

Proof. Identical to the proof of Lemmas 30 and 31 however the condition k1 ∤ d means
that d is never exceptional so that any Siegel zero βd modulo d can always be bounded
as in (99) using Theorem 26. □

Lemma 35. Suppose N is a positive even integer, k1 ⩾ Kδ(x1), N ⩾ X2, and
log log x1(X2) ⩾ 10.4. Then, for each k | k1 with k ̸= 1, we have
∑

d⩽H/k
(d,N )=(d,k)=1
 µ2(d) ∣
∣
∣
∣π(N ; kd, N ) − π(N ; k, N )
φ(d)
 ∣
∣
∣
∣ < p∗(X2)N
log3 N ,

where p∗(X2) is as in Lemma 34, and π(N ; k, l) denotes the number of primes up to N
congruent to l modulo k.

Proof. Much of this proof is identical to those of Lemmas 30 and 31, so we will be
terse in some algebraic manipulations, only highlighting the differences to the previous
proofs. For convenience, for an arithmetic function f ∈ {π, θ, ψ} we will denote

(100) Df (x; q1, q2, l) := f (x; q1q2, l) − f (x; q1, l)
φ(q2)
so that we are trying to prove
∑

d⩽H/k
(d,N )=(d,k)=1
 µ
2(d) |Dπ(N ; k, d, N )| < p∗(X2)N
log3 N .

Let y ∈ [x1(N ), N ]. We have,

Dψ(y; k, d, N )

= 1
φ(kd)
 ∑

χ (mod kd) χ(N )ψ(y; χ) − 1
φ(d)φ(k)
 ∑

χ1 (mod k) χ1(N )ψ(y; χ1)

= 1
φ(kd)
 



 ∑

χ1 (mod k)
χ2 (mod d)
 χ1(N )χ2(N )ψ(y; χ1χ2) − ∑

χ1 (mod k) χ1(N )χ0,d(N )ψ(y; χ1)






33

= 1
φ(kd)
 



 ∑

χ1 (mod k)
χ2 (mod d)
 χ1(N )χ2(N )ψ(y; χ1χ2) − ∑

χ1 (mod k) χ1(N )χ0,d(N )ψ(y; χ1χ0,d)







− 1
φ(kd)
 ∑

χ1 (mod k) χ1(N )χ0,d(N ) (ψ(y; χ1) − ψ(y; χ1χ0,d))

= 1
φ(kd)
 ∑

χ1 (mod k)
χ2̸=χ0,d (mod d)
 χ1(N )χ2(N )ψ(y; χ1χ2)

− 1
φ(kd)
 ∑

χ1 (mod k) χ1(N )χ0,d(N ) (ψ(y; χ1) − ψ(y; χ1χ0,d)) ,

where χ0,d is the principal character modulo d.
We use above that χ0,d(l) = 1 for (l, d) = 1, and that for (k, d) = 1 the character
modulo kd is represented in a unique way as the product of two characters modulo k
and modulo d.
Summing over d and noting that µ2(kd) = µ2(d), the above last term is bounded by

∑

d⩽H/k
(d,N )=(d,k)=1
 µ2(d)
φ(kd)
 ∣
∣
∣
∣
∣
∣
 ∑

χ1 (mod k) χ1(N )χ0,d(N ) (ψ(y; χ1) − ψ(y; χ1χ0,d))

∣
∣
∣
∣
∣
∣ ⩽ 0.4 log3 y(101)

similar to inequality (83) from the proof of Lemma 30. Then, for the case kd ⩽ Q1(x1),
we get analogously to (84)

∑

dk⩽Q1(x1)
(d,N )=(d,k)=1
 µ2(d)
φ(kd)
∣
∣
∣
∣
∣
 ∑

χ1 (mod k)
χ2̸=χ0,d (mod d)

χ1(N )χ2(N )ψ(y; χ1χ2)

∣
∣
∣
∣
∣
(102)
 ⩽ 1.1 log Q1(y)

(3.2 · 10
−8y
log8 y + yβ∗
0 (x1)

β∗
0(x1)
)

.

Here we note that since χ2 ̸= χ0,d and k | k1, the exceptional character never
appears in the inner sum of (102). Thus, using Theorem 26 we can bound each Siegel
zero modulo d by β∗
0(x1) (Equation (99)).
The case Q1(x1)/k < d ⩽ H/k is also dealt with analogously to the inequalities (85)
and (86) from the proof of Lemma 30. Then finally, the conversion from Dψ(y; k, d, N )
to Dπ(N ; k, d, N ) is done using the same reasoning as in Lemma 31. □

34

Lemma 36. Keep the notation and conditions of Lemma 32 except assuming k2 ⩾
Kδ(x2). We then have

∑

d<D∗
d|P (y)
k2∤d
 max
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

Z⩽p<Y
np≡N (mod d)
 a(n) − 1
φ(d)
 ∑

n<X
 ∑

Z⩽p<Y
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
 ⩽ m
∗(X3)XY
log3 Y

where m
∗(X2) = m(X2) as in Lemma 32 with the ∗ indicates that β0(x2) is replaced
with

(103) β∗
0(x2) = 1 − 1
2R1 log(Q1(x2))

which is sharper than (91).

Proof. As with Lemma 34, the proof is the same as the case k2 < Kδ(x2), with the
added condition k2 ∤ d meaning that d is not exceptional, giving (103). □

5 Preliminaries to sieving

We now set up the main sieving argument that will be used to prove an explicit
version of Chen’s theorem. Some of the definitions that will be presented in this section
were previously introduced. We decided to include them here to ease readability and
make this section somewhat self-contained.
Fix

(104) N ⩾ X2, z = N 1
8 , y = N 1
3 .

We shall consider the sets

(105) A := {N − p : p ⩽ N, p ∤ N } , Ap := {a ∈ A : p|a} Ad := ⋂

p|d Ap.

with p prime and d square-free. Note that

(106) |A| = π(N ) − ω(N ) and |Ad| = π(N ; d, N ) − ω(N ; d, N )

where ω(n; q, a) denotes the number of prime factors of n which are congruent to a
modulo q. We also set

(107) S(A, n) :=
 ∣
∣
∣
∣
∣
∣A − ⋃

p|n Ap
∣
∣
∣
∣
∣
∣

and

(108) B := {N − p1p2p3 : z ⩽ p1 < y ⩽ p2 ⩽ p3, p1p2p3 < N, (p1p2p3, N ) = 1}

where p1, p2 and p3 are primes. Then, defining

(109) P (x) := ∏

p<x
p∤N
 p,

one obtains the following bound. 35

Lemma 37 ([40, Theorem 10.2]). Let π2(N ) denote the number of representations of
a given even integer N as the sum of a prime and a semi-prime. We have3

π2(N ) > S(A, P (z)) − 1
2
 ∑

z⩽q<y
q∤N
 S(Aq, P (z)) − 1
2S(B, P (y)) − 2N 7
8 − N 1
3 .

To prove Theorem 3 it thus suffices to give a good lower bound for S(A, P (z)) and
good upper bounds for S(B, P (y)) and S(Aq, P (z)) for each prime q with z ⩽ q < y.
We now let xi, Kδ, ki and Q1 be as in Section 4.1. For fixed i ∈ {1, 2}, if ki ⩾ Kδ(xi)
we let q1 > . . . > qℓ be all prime factors of ki and set m0 = 1, P 0(x) := P (x) and for
1 ⩽ j ⩽ ℓ,

(110) mj := q1 · · · qj, A
(j) := Amj , P (j)(x) := ∏

p<x, p∤N,
p̸=q1,...,qj
 p.

In relation to the function V (z) from the explicit linear sieve (see (11)), we then define

(111) V (x) := ∏

p|P (x)
 (1 − 1
p − 1
) , V (j)(x) := ∏

p|P (j)(x)
 (1 − 1
p − 1
 ) ,

for 1 ⩽ j ⩽ ℓ and set V 0(x) = V (x). To bound V (j)(x) we use the following result.

Lemma 38. For x ⩾ 285 and j = 0, . . . , ℓ, we have

V (j)(x) = U (j)
N
log x
 [1 + 1.45 θ1(x)log N
x − 1
 (
1 + 10 log log N
log N
 )]

· (
1 + 1.002 θ2(x)
x − 3
 ) (
1 + θ3(x)
2 log2 x
) ,(112)

where |θi| ⩽ 1, i = 1, 2, 3, and
4

(113) U (j)
N := 2e
−γ ∏

p>2
 (
1 − 1
(p − 1)2
 ) ∏

p>2
p|N mj
 p − 1
p − 2,

so that U (0)
N = UN as defined by (2). In particular, when x = z = N 1/8 ⩾ exp(20),

(114) U (j)
N
log z
 (
1 − 32.02
log2 N
 ) < V (j)(z) < U (j)
N
log z
 (
1 + 32.02
log2 N
 )

and when x = y = N 1/3 ⩾ exp(20), we have

(115) U (j)
N
log y
 (1 − 4.51
log2 N
 ) < V (j)(y) < U (j)
N
log y
 (
1 + 4.51
log2 N
 ) .

3For ease of argument, we have added the condition q ∤ N to the second term which was not present
in [40]. This condition is vacuous since if q | N − p ∈ A and q | N then q = p. However, this is not
possible since p ∤ N .
4In the analogous (non-explicit) theorem by Nathanson [40, Theorem 10.3], there is a small typo.
Namely, a factor of 2 is missing from UN (G(N ) in Nathanson’s notation).
36

Proof. We follow the argument in the proof of [40, Theorem 10.3]. Let

W (x) = ∏

2<p<x
 (
1 − 1
p − 1
 ) ,

then V (j)(x)
W (x) = ∏

2<p<x
p|N mj
 (1 − 1
p − 1
)−1

= ∏

p>2
p|N mj
 (
1 − 1
p − 1
)−1 ∏

p⩾x
p|N mj
 (
1 − 1
p − 1
)

= ∏

p>2
p|N mj
 p − 1
p − 2
 ∏

p⩾x
p|N mj
 (
1 − 1
p − 1
 ) .(116)

Let us estimate the second product in (116). To do so, we note that

p − 1 ⩾ x − 1 ⩾ 284,

1 − t > exp(−1.002t), for 0 < t ≤ 1/284,(117)
 1 − t ⩽ exp(−t), for all t ∈ R.

Hence,
 ∏

p⩾x
p|N mj
 (
1 − 1
p − 1
 ) > exp
 



−1.002 ∑

p⩾x
p|N mj
 1
p − 1
 





⩾ exp (
−1.002 ω(N mj)
x − 1
 ) .

By the definition (110) of mj and conditions (75) and (76) on ki, we have mj ⩽ ki ⩽ log10 N .
Thus by Lemma 22, we have

ω(N mj) ⩽ log N + 10 log log N
log 2 ,

and we can continue the chain of inequalities as follows:

exp (
−1.002 ω(N mj)
x − 1
 ) ⩾ exp (−1.002 log N + 10 log log N
(log 2)(x − 1)
 )

⩾ 1 − 1.45log N + 10 log log N
x − 1 .

To summarise,

(118) V (j)(x)
W (x) = [1 + 1.45 θ1(x)log N
x − 1
 (
1 + 10 log log N
log N
 )] ∏

p>2
p|N mj
 p − 1
p − 2,

37

where |θ1(x)| ⩽ 1.
Now,
 W (x) ∏

p<x
 (1 − 1
p
 )−1 = 2 ∏

2<p<x
 (
1 − 1
(p − 1)2
 )

= 2 ∏

p>2
 (1 − 1
(p − 1)2
 ) ∏

p⩾x
 (
1 + 1
p(p − 2)
)

⩽ 2 ∏

p>2
 (
1 − 1
(p − 1)2
 ) exp
 (
∑

p⩾x
 1
p(p − 2)
)
 ,

where we have used that 1 + x ≤ exp(x) for all x ∈ R. Next we note that

0 ⩽ ∑

p⩾x
 1
p(p − 2) ⩽ ∑

n⩾x−2
 1
n2 ⩽ 1
(x − 3),

whence, by (117),

W (x) ∏

p<x
 (
1 − 1
p
 )−1 = 2 ∏

p>2
 (
1 − 1
(p − 1)2
 ) (
1 + 1.002 θ2(x)
x − 3
 ) ,

with |θ2(x)| ⩽ 1. Using an explicit form of Mertens’ third theorem [46, Theorem 7]
then yields

(119) W (x) = 2e
−γ

log x
 ∏

p>2
 (1 − 1
(p − 1)2
 ) (
1 + θ3(x)
2 log2 x
) (
1 + 1.002 θ2(x)
x − 3
 ) ,

for all x ≥ 285, with |θ3(x)| ≤ 1. The expressions (119) and (118) imply (112). □

We also have the following bounds relating to ℓ, qj and U (j)
N .

Lemma 39. If ℓ primes divide ki then

(120) ℓ ⩽ 1.3841 log(log10 xi)
log log(log10 xi) .

Proof. The result follows from (65) using that ki ⩽ Q1(xi) = log10 xi. □

Lemma 40. If ℓ ⩾ 2,
1
q2 − 2 + 1
(q2 − 2)(q3 − 2) + · · · + 1
(q2 − 2)(q3 − 2) · · · (qℓ − 2) ⩽ 1.

Proof. Since N is even, and (ki, N ) = 1, ki and all its prime factors are odd. Thus
q2 > q3 > · · · > qℓ is a decreasing set of odd numbers, so we have q2 ⩾ 2ℓ − 1. Thus,
1
q2 − 2 + 1
(q2 − 2)(q3 − 2) + · · · + 1
(q2 − 2)(q3 − 2) · · · (qℓ − 2) ⩽ (ℓ − 1) 1
q2 − 2

⩽ ℓ − 1
2ℓ − 3
38
 = 1
2 + 1
4ℓ − 6
⩽ 1
 □

Lemma 41. We recall that 0 < δ < 2 and Kδ(x) = logδ x. Suppose N is a positive
even integer with N ⩾ X2, and ki ⩾ Kδ(xi(X2)) ⩾ 3 and

(121) εi(X2, δ) := 1
p − 2 ,

with p the largest prime such that

logδ xi(X2) ⩾ ∏

2<p⩽p p.

We then have U (1)
N ⩽ UN (1 + εi(X2, δ))

where U (1)
N is defined in (113).

Proof. Since ki ⩾ logδ xi(X2), ki ⩾ ∏

2<p⩽p p.

Then, since ki is odd and square-free, this means that q1 ⩾ p. Thus

U (1)
N = UN q1 − 1
q1 − 2 ⩽ UN (1 + εi(X2, δ)),

as required. □

In relation to the remainder term (10) appearing in the linear sieve, we now define

(122) r(d) := |Ad| − |A|
φ(d) and rk(d) := |Akd| − |Ak|
φ(d),

with A and Ad defined in (105). By (106), r(d) and rk(d) can be expressed as

r(d) = π(N ; d, N ) − ω(N ; d, N ) − π(N ) − ω(N )
φ(d)
(123)
 rk(d) = π(N ; kd, N ) − ω(N ; kd, N ) − π(N ; k, N ) − ω(N ; k, N )
φ(d) .(124)

This leads us to the following estimates.

Lemma 42. Let N be a positive even integer with N ⩾ X2 and log log(x1(X2)) ⩾ 10.4.
We have

(125) N
log N < |A| < 1.00005 N
log N .

If k1 ⩾ Kδ(x1) then for j = 0, 1, . . . , l − 1 we have

(126) |r(mj)| < c2(X2)N
log3 N ,

39

with

(127) c2(X2) := c(X2) + 1.3841 log4 X2
X2 log log X2 ,

where c(X2) defined in Lemma 33. We also have

(128) |r(ml)| ⩽ c3(X2)N log log log N
log1+δ N ,

with
 c3(X2) := max
N ⩾X2
 [ 1
log log log N · ( 3
2 log N + log(N log10 x1)
log(N/ log10 x1)
) logδ N
logδ x1
(129)
 · (
eγ log log logδ x1 + 5
2 log log logδ x1
 )

+ 1.3841 log2+δ N
N log log N log log log N
 ]
.

Proof. By (106) and Lemma 22, we have

π(N ) − 1.3841 log N
log log N ⩽ |A| ⩽ π(N ),

where we used that log N
log log N increases for log log N ⩾ 1. Hence, by [46, Theorem 2],

(130) N
log N − 1
2 − 1.3841 log N
log log N < |A| < N
log N − 3
2 ,

which implies (125) for log log x1(N ) ⩾ 10.4.
Now let us prove (126). By (123), and Lemmas 22 and 33, we get

r(mj) = ∣
∣
∣
∣|Amj | − |A|
φ(mj)
∣
∣
∣
∣

⩽ ∣
∣
∣
∣π(N ; mj, N ) − π(N )
φ(mj)
∣
∣
∣
∣ + ∣
∣
∣
∣ω(N ; mj, N ) − ω(N )
φ(mj)
∣
∣
∣
∣

⩽ |Eπ(N ; mj, N )| + max {
ω(N ; mj, N ), ω(N )
φ(mj)
}

⩽ |Eπ(N ; mj, N )| + ω(N )

⩽ |Eπ(N ; mj, N )| + 1.3841 log N
log log N
(131)
 ⩽ N
log3 N
 (
c(X2) + 1.3841 log4 N
N log log N
 ) ,

and we conclude (126) since the function log4 N
N log log N decreases for N ⩾ exp(exp(10.4)).
To prove (128), we use (131) with j = ℓ and bound |Eπ(N ; mℓ, N )| with a bit more
40

care. First, by an explicit form of the Brun–Titchmarsh theorem [38, Theorem 2] we
have
π(N ; mℓ, N ) < 2N
φ(mℓ) log(N/mℓ) = N
φ(mℓ) log N + log(N mℓ)
log(N/mℓ) · N
φ(mℓ) log N .

Thus, noting π(N ; mℓ, N ) ⩾ 0,

π(N ; mℓ, N ) = N
φ(mℓ) log N + ε log(N mℓ)
log(N/mℓ) · N
φ(mℓ) log N

for some |ε| ⩽ 1. Similarly, by [46, Theorem 1]

π(N )
φ(mℓ) = N
φ(mℓ) log N + ε′ 3N
2φ(mℓ) log2 N

for some |ε′| ⩽ 1. Therefore,

|Eπ(N ; mℓ, N )| = ∣
∣
∣
∣π(N ; mℓ, N ) − π(N )
φ(mℓ)
∣
∣
∣
∣ ⩽ N
φ(mℓ) log N
 ( 3
2 log N + log(N mℓ)
log(N/mℓ)
) .

Finally, since k1 is square-free and by (110), we get that mℓ = ki is odd, hence by [46,
Theorem 15] 1
φ(mℓ) < e
γ log log mℓ
mℓ + 5
2mℓ log log mℓ .

Combining all the above estimates with (131) for j = ℓ and using mℓ = ki ∈ [logδ x1, log10 x1]
gives the desired result. □

Lemma 43. Let N be a positive even integer with N ⩾ X2 and log log x1(X2) ⩾ 10.4,
H = H(N ) = √x1
log10 x1 , and suppose p(X2), p∗(X2) are as in Lemmas 31 and 34. We
have

(132) ∑

d<H
d|P (z)
 |r(d)| < c4(X2)N
log3 N

and if k1 ⩾ Kδ(x1)

(133) ∑♯

d<H/mj |rmj (d)| < c∗
4(X2)N
log3 N ,

for all 1 ⩽ j ⩽ ℓ, where

c4(X2) := p(X2) + 0.9
√
x1(X2) log4 X2
X2 log10(x1(X2)) log log X2 ,(134)
 c∗
4(X2) := p∗(X2) + 0.9
√x1(X2) log4 X2
X2 log10(x1(X2)) log log X2
(135)

and the ♯ means that the sum is over d | P (j+1)(z) if j < ℓ and d | P (ℓ)(z) if j = ℓ, with
P (j) defined in (110). 41

Proof. First, we prove (132). As in (131),

|r(d)| ⩽ |Eπ(N ; d, N )| + 1.3841 log N
log log N .

Thus by Lemmas 31 and 23,
∑

d<H
d|P (z)
 |r(d)| < p(X2)N
log3 N + 0.65H · 1.3841 log N
log log N ,

which gives the required result. The proof of (133) is essentially the same, using Lemma
35 in place of Lemma 31. □

6 A lower bound for S(A, P (z))

In this section, we obtain a lower bound for S(A, P (z)). This is the first term
appearing in the bound for π2(N ) in Lemma 37. We recall that functions f (x) and
F (x) are defined in (8), x1(N ) defined in (75), and c2(X2), c3(X2) defined in (127) and
(129). We introduce the following notations: for α1 > 0, set

cα1,X2 := 4 − 8α1 − 160 log log X2
log X2 ,(136)
 mα1,X2 := max{(1 − f (cα1,X2), F (cα1,X2) − 1)},(137)
 a(X2) := a1(X2) max
N ⩾X2
 [ log log log N
logδ N · ∏

p>2
 (p − 1)2

p(p − 2)
(138)
 · (
eγ log log(log10 x1(N )) + 2.5
log log(log10 x1(N ))
 )] ,

a1(X2) := max
N ⩾X2
 [ c2(X2)
log2−δ N log log log N · 1.3841 log(log10 x1(N ))
log log(log10 x1(N ))
 ] + c3(X2).(139)

Theorem 44. Let u0 = 109 and ε = 1.452 · 10
−7 be the corresponding values in
Lemma 18. Recall that Kδ(x) = logδ(x) for 0 < δ < 2. Let X2 be such that
log log x1(X2) ⩾ 10.4, assume that α1 > 0, N ⩾ X2 is an even integer, and z = N 1/8

such that
 N α1

log10 x1(N ) log2.5 N ⩾ exp (
u0
 (1 + 9 · 10
−7

log u0
 )) , N 1
2 −α1

log20 N ⩾ z2

8α1 + 160 log log N
log N < 1, Kδ(x1(X2)) ⩾ 3022.(140)

Let A, S(A, n), and P (z) be defined by (105), (107), and (109) respectively. Assume
UN = U (0)
N is defined in (113), h(x) in (7), ε1(X2, δ) in (121), c4(X2) and c∗
4(X2) in
Lemma 43, and let C1(ε) = 106 and C2(ε) = 107 be the values from Table 1. Let
C(ε) = max{C1(ε), C2(ε)}. For k1 as defined in (77), we consider two cases.
42

(a) If k1 < Kδ(x1(N )), we have

S(A, P (z)) > 8|A|UN
log N
 (
1 − 32.02
log2 N
 ) {2e
−γ log(3 − 8α1)
4 − 8α1 − C2(ε)εe
2h(4 − 8α1)

− 1
8
 (
1 − 32.02
log2 N
 )−1 (
2e
−γ ∏

p>2
 (1 − 1
(p − 1)2
 ))−1 c4(X2)
log N
 }

.

(b) If k1 ⩾ Kδ(x1(N )), we have

S(A, P (z)) >

8 |A|UN
log N
 (
1 + 32.02
log2 N
 ) { 2e
γ log(3 − 8α1 − 160 log log X2
log X2 )

4 − 8α1 − 160 log log X2
log X2 − ε1(X2, δ)(1 − f (cα1,X2))

− (1 + ε1(X2, δ))εC2(ε)e2h(cα1,X2)

− (3ε1(X2, δ) + a(X2)) · (mα1,X2 + εC(ε)e
2h(cα1,X2)) − a(X2) − 64.04
log2 N

− 1
8
 (
1 + 32.02
log2 N
 )−1 (
2e
−γ ∏

p>2
 (
1 − 1
(p − 1)2
 ))−1 c∗
4(X2)
log N 1.3841 log(log10 x1(N ))
log log(log10 x1(N ))
 }

,

with c2(X2) and c3(X2) as in Lemma 42.

Remark. The constant
∏

p>2
 (1 − 1
(p − 1)2
 ) = ∏

p>2
 p(p − 2)
(p − 1)2 = 0.66016 . . . ,

is called the twin prime constant.

Proof of Theorem 44 in case (a). Assume k1 < Kδ(x1). In this case, we set

(141) D(1) := N 1
2 −α1, s(1) := log D(1)

log z = 4 − 8α1 and Q(u) := ∏

p<u
p∤N
 p.

We note that 3 ⩽ s(1) ⩽ 4 since α1 > 0 by definition and α1 < 1
8 by (140).
We will apply Theorem 6 to the set A with P the set of primes coprime to N ,
gn(p) = 1/(p − 1), Q = Q(u0), D = D(1), and s = s(1). Setting parameters in this way
implies that S(A, P (z)) = S(A, P, z) from Theorem 6. Then D ⩾ z2 follows from the

condition N 1
2 −α1
log20 N ⩾ z2 assumed in the first line of (140), and thus

S(A, P (z)) > (f (s(1)) − εC2(ε)e
2h(s(1)))|A|V (z) − ∑

d|P (z)
d<QD(1)
 |r(d)|

> 8|A|UN
log N
 (
1 − 32.02
log2 N
 ) (f (s(1)) − C2(ε)εe
2h(s(1))) − ∑

d|P (z)
d<QD(1)
 |r(d)|,(142)
 43

where we used Theorem 6 in the first line and (114) in the second line. By the definition
(62) of f (s(1)) for 2 ⩽ s(1) ⩽ 4, the second line of (142) coincides with

(143) 8|A|UN
log N
 (1 − 32.02
log2 N
 ) (2e
γ log(3 − 8α1)
4 − 8α1 −C2(ε)εe2h(4−8α1)

)
− ∑

d|P (z)
d<QD(1)
 |r(d)|.

We remark that the condition
N α1

log10 x1(N ) log2.5 N ⩾ exp (u0
 (
1 + 9 · 10
−7

log u0
 ))

implies that

(144) Q ⩽ N α1

log10 x1(N ) log2.5 N

by Lemma 25. As a result, QD(1) ⩽ H = √x1
log10 x1 so that we may apply Lemma 43 (in
particular the bound (132)) to the error term in (143):
∑

d|P (z)
d<QD(1)
 |r(d)| < c4(X2)N
log3 N = UN N
log3 N · U −1
N · c4(X2)

< |A|UN
log2 N
 (
2e
γ ∏

p>2
 (1 − 1
(p − 1)2
 ))−1 c4(X2),(145)

where in the last line we used the definition (113) of UN and the condition |A| >
N/ log N , see (125).
Combining (142), (143), and (145) proves the theorem in case (a). □

In case (b), when k1 ⩾ Kδ(x1), we need to apply an inclusion-exclusion argument
which in essence allows us to avoid the large exceptional zero.

Lemma 45. Keep the notations from Theorem 44. We have

S(A, P (z)) =
 ℓ−1∑

j=0 (−1)
jS(A
(j), P (j+1)(z)) + (−1)
ℓS(A
(ℓ), P (ℓ)(z)),

with A
(j) and P (j)(z) defined in (110).

Proof. First note that S(A, P (1)(z)) − S(A, P (z)) counts the number of integers in A
that are divisible by q1 but not by any other primes below z. Then, S(A
(1), P (2)(z)) −
S(A, P (1)(z)) + S(A, P (z)) counts the number of integers in A that are divisible by q1
and q2 but not any other primes less than z. By generalising this argument, we have
that ∑ℓ−1
j=0(−1)ℓ−1−jS(A
(j), P (j+1)(z)) + (−1)ℓS(A, P (z)) counts the number of integers
in A divisible by q1, . . . , qℓ but no other primes less than z. That is,

S(A
(ℓ), P (ℓ)(z)) =
 ℓ−1∑

j=0 (−1)ℓ−1−jS(A
(j), P (j+1)(z)) + (−1)
ℓS(A, P (z)),

44

which rearranges to give the desired result. □

We now bound S(A
(j), P (j+1)(z)) and S(A
(ℓ), P (ℓ)(z)).

Lemma 46. Keep the notation from the beginning of Section 6 and Theorem 44. Let

D(1)
j := N 1
2 −α1

k1mj and s(1)
j := log D(1)
j
log z .

for j = 0, . . . , ℓ. Let Q(u) be as in (141), rk(d) be as in (122), and

Ej :=
 {∑
d|P (j+1)(z), d<D(1)
j Q(u0) |rmj (d)|, if j = 0, . . . , ℓ − 1,
∑
d|P (ℓ)(z), d<D(1)
ℓ Q(u0) |rmℓ(d)|, if j = ℓ.

Provided that each D(1)
j ⩾ z2,

∣
∣A(j)∣
∣ [
V (j+1)(z) − 8U (j+1)
N
 (
1 + 32.02
log2 N
 ) (1 − f (s(1)
j )) + εC2(ε)e
2h(s(1)
j )
log N
 ]
 − Ej

< S(A
(j), P (j+1)(z))

< ∣
∣A
(j)∣
∣ [

V (j+1)(z) + 8U (j+1)
N
 (
1 + 32.02
log2 N
 ) (F (s(1)
j ) − 1) + εC1(ε)e
2h(s(1)
j )
log N
 ]
 + Ej

for j = 0, . . . , ℓ − 1, and

∣
∣A
(ℓ)∣
∣ [
V (ℓ)(z) − 8U (ℓ)
N
 (1 + 32.02
log2 N
 ) (1 − f (s(1)
ℓ )) + εC2(ε)e2h(s(1)
ℓ )
log N
 ]
 − Eℓ

< S(A
(ℓ), P (ℓ)(z))

< ∣
∣A(ℓ)∣
∣ [
V (ℓ)(z) + 8U (ℓ)
N
 (1 + 32.02
log2 N
 ) (F (s(1)
ℓ ) − 1) + εC1(ε)e2h(s(1)
ℓ )
log N
 ]
 + Eℓ,

where A(j), V (j)(z), and U (j)
N (z) are defined in (110), (111), and (113) respectively.

Proof. We only prove the lower bound for j = 0, . . . , ℓ − 1 as the proof for the other
cases will follow by almost identical reasoning. We apply Theorem 6 to the set A
(j),
with P the set of primes coprime to N , gn(p) = 1/(p − 1), Q = Q(u0), and D = D(1)
j .
With P (j)(z) as in (110), we thus have

S(A
(j), P (j+1)(z)) > |A
(j)|V (j+1)(z) (
f (s(1)
j ) − εC2(ε)e2h(s)
) − Ej

= ∣
∣A
(j)∣
∣ (V (j+1)(z) − V (j+1)(z) · (1 − f (s(1)
j ) + εC2(ε)e
2h(s))) − Ej.

Next, we note that

s(1)
j = log(D(1)
j )
log z = 4 − 8α1 − 8 log(k1) + 8 log(mj)
log N
45

so by (136),
 cα1,N = 4 − 8α1 − 160 log log N
log N ⩽ s(1)
j < 4 − 8α1

since mj ⩽ k1 ⩽ log10 N by the definition (77) of k1 and the definition (110) of mj.
From the condition 0 < α1 < 1
8, which follows from (140), we have 3 ⩽ s(1)
j ⩽ 4 and
hence by (62)
 1 − f (s(1)
j ) = 1 − 2e
γ log(s(1)
j − 1)

s(1)
j > 0.

The result then follows by applying the upper bound in (114) in Lemma 38. □

By the definition of D(1)
j from Lemma 46 and (144), we have QD(1)
j ⩽ H/mj, and
thus we can apply Lemma 43 to get the following bound for Ej (with Ej defined in
Lemma 46).

Lemma 47. With the notations from Lemma 46, we have for j = 0, . . . , ℓ,

Ej < c∗
4(X2)N
log3 N .

Proof of Theorem 44 in case (b). We assume that k1 ⩾ Kδ(x1). Combining Lemmas
39, 45, 46 and 47 gives

S(A,P (z)) >
 ℓ−1∑

j=0 (−1)
j|A
(j)|V (j+1)(z) + (−1)
ℓ|A
(ℓ)|V (ℓ)(z)

− 8U (1)
N |A| (1 + 32.02
log2 N
 ) ((1 − f (cα1,X2)) + εC2(ε)e2h(cα1,X2)
log N
 )

− 8
 ( ℓ−1∑

j=1 |A
(j)|U (j+1)
N + |A(ℓ)|U (ℓ)
N
 ) (1 + 32.02
log2 N
 ) (mα1,X2 + εC(ε)e2h(cα1,X2)
log N
 )

− c∗
4(X2)N
log3 N 1.3841 log(log10 x1(N ))
log log(log10 x1(N )) ,

(146)

where we recall that mα1,X2 is defined in (137). Above, we used that cα1,X2 ⩽ s(1)
j for
all j and that h(s) and F (s) are decreasing whereas f (s) is increasing for 3 ⩽ s ⩽ 4 —
this follows from the definitions of these functions (7), (60) and (62).
We note that the term corresponding to j = 0 is written separately in line 2 of (146)
since it will be estimated differently from the cases 0 < j < ℓ from line 3.
We now bound each line in (146).

Lemma 48. Keep the notations from the beginning of Section 6 and Theorem 44, and
assume k1 ⩾ Kδ(x1). Let A
(j) (with A = A
(0)) and V (j)(z) be as in (110) and (111)
46

respectively. Then

(147)
 ℓ−1∑

j=0 (−1)
j|A(j)|V (j+1)(z) + (−1)ℓ|A
(ℓ)|V (ℓ)(z) = |A|V (z) (1 + θa(X2))

where |θ| ⩽ 1 and a(X2) is defined in (138).

Proof. By the definition of r(mj), given in (122), we have

ℓ−1∑

j=0 (−1)
j|A(j)|V (j+1)(z) + (−1)ℓ|A
(ℓ)|V (ℓ)(z) =

ℓ−1∑

j=0 (−1)j |A|
φ(mj)V (j+1)(z) + (−1)
ℓ |A|
φ(mℓ)V (ℓ)(z)

+
 ℓ−1∑

j=0 (−1)
jr(mj)V (j+1)(z) + (−1)
ℓr(mℓ)V (ℓ)(z),

where V (j)(z) is defined in (111). Writing φ∗(n) = n ∏
p|n p−2
p (so that φ
∗(mj) =
∏j
i=1(qi − 2) for j ⩾ 1), we have

|A|
φ(mj)V (j+1)(z) = |A|V (z)
φ∗(mj)
 (1 + 1
qj+1 − 2
 )

so that

(148)
 ℓ−1∑

j=0 (−1)
j |A|
φ(mj)V (j+1)(z) = |A|V (z) (1 + (−1)
ℓ−1

φ∗(mℓ)
 )

and thus ℓ−1∑

j=0 (−1)j |A|
φ(mj)V (j+1)(z) + (−1)ℓ |A|
φ∗(mℓ)V (ℓ)(z) = |A|V (z).

Next, by Lemmas 39 and 42
∣
∣
∣
∣
∣
 ℓ−1∑

j=0 (−1)
jr(mj)V (j+1)(z) + (−1)
ℓr(mℓ)V (ℓ)(z)

∣
∣
∣
∣
∣ ⩽ a1(X2)N V (ℓ)(z) log log log N
log1+δ N

⩽ a1(X2)|A|V (ℓ)(z) log log log N
logδ N ,(149)

with a1(X2) defined in (139). We have

1 ⩽ V (ℓ)(z)
V (z) =
 ℓ∏

j=1
 qj − 1
qj − 2

⩽ ∏

p>2
 (p − 1)
2

p(p − 2) k1
φ(k1)
 47

⩽ ∏

p>2
 (p − 1)
2

p(p − 2)
 (
eγ log log k1 + 2.5
log log k1
 )
(150)
 ⩽ ∏

p>2
 (p − 1)
2

p(p − 2)
 (
eγ log log log10(x1(N )) + 2.5
log log log10(x1(N ))
) ,(151)

where in (150) we used [46, Theorem 15] noting that k1 is odd, and in (151) we used
that k1 ⩾ Kδ(x1) ⩾ 3022 so that the expression is increasing.
Substituting (151) into (149) and using the definition (138) of a(X2) then completes
the proof of (147). □

We now move onto the second line of (146). By (114) in Lemma 38 we have

8UN
log N < V (z) + 8 · 32.02UN
log3 N .

Thus, by the formula (62) of f , for any 3 ⩽ s′ ⩽ 4,

8UN
log N − 8UN f (s′)
log N < V (z) + 8 ( 32.02UN
log3 N − 2UN e
γ log(s′ − 1)
s′ log N
 ) .

Using this result, along with Lemma 41 and the definition (136) of cα1,X2 ∈ [3, 4],
gives
 8|A|U (1)
N
 ( 1 − f (cα1,X2) + εC2(ε)e
2h(cα1,X2)
log N
 )

< |A|V (z) + 8|A|UN
 {
 − 2e
γ log (3 − 8α1 − 160 log log X2
log X2
 )

(4 − 8α1 − 160 log log X2
log X2 ) log N + 32.02
log3 N

+ ε1(X2, δ)(1 − f (cα1,X2))
log N + (1 + ε1(X2, δ))εC2(ε)e2h(cα1,X2)
log N
 }

.(152)

Finally, we deal with the third line of (146).

Lemma 49. Keep the notations from the beginning of Section 6 and Theorem 44, and
assume k1 ⩾ Kδ(x1). Let A
(j) (with A = A
(0)) and V (j)(z) be as in (110) and (111)
respectively. Then

ℓ−1∑

j=1 |A
(j)|U (j+1)
N + |A
(ℓ)|U (ℓ)
N ⩽ |A|UN (3ε1(X2, δ) + a(X2)) ,

where a(X2) is defined in (138).

Proof. The argument is analogous to the proof of Lemma 48. Namely, by the definition
of r(mj), given in (122), we have

ℓ−1∑

j=1 |A
(j)|U (j+1)
N + |A
(ℓ)|U (ℓ)
N

48

=
 ℓ−1∑

j=1
 |A|
φ(mj)U (j+1)
N + |A|
φ(mℓ)U (ℓ)
N +
 ℓ−1∑

j=1 r(mj)U (j+1)
N + r(mℓ)U (ℓ)
N .(153)

Similarly to (148), |A|
φ(mj)U (j+1)
N = |A|UN
φ∗(mj)
 (
1 + 1
qj+1 − 2
)

and |A|
φ(mℓ)U (ℓ)
N = |A|UN
φ∗(mℓ)
so that
 ℓ−1∑

j=1
 |A|
φ(mj)U (j+1)
N + |A|
φ(mℓ)U (ℓ)
N =

= |A|UN
q1 − 2
 (
1 + 2
q2 − 2 + 2
(q2 − 2)(q3 − 2) + · · · + 2
(q2 − 2) · · · (qℓ − 2)
)

⩽ 3|A|UN ε1(X2, δ).

In the last line, we used Lemma 40 and the inequality 1
q1−2 ⩽ ε1(X2, δ), which follows
from definition (121) of ε1(X2, δ).
Therefore, we have bounded the first two terms of (153). We use Lemma 42 and
that U (j)
N ⩽ U (ℓ)
N for 0 ⩽ j ⩽ ℓ following from the definition (113), to bound the last
two terms:
∣
∣
∣
∣
∣
 ℓ−1∑

j=1 r(mj)U (j+1)
N + r(mℓ)U (ℓ)
N
 ∣
∣
∣
∣
∣ < (ℓ − 1)c2(X2) N
log3 N U (ℓ)
N + c3(X2)N log log N
log1+δ N U (ℓ)
N

⩽ ( a1(X2) log log log N
log1+δ N
 ) U (ℓ)
N ,

by the definition (139) of a1(X2) and the bound for ℓ from Lemma 39.
Thus we get an upper bound for (153):

ℓ−1∑

j=1 |A
(j)|U (j+1)
N + |A
(ℓ)|U (ℓ)
N ⩽ 3|A|UN ε1(X2, δ) + ( a1(X2)|A| log log log N
logδ N
 ) U (ℓ)
N .

Similarly to (151), we derive

U (ℓ)
N
UN ⩽ ∏

p>2
 (p − 1)2

p(p − 2)
 (e
γ log log log10(x1(N )) + 2.5
log log log10(x1(N ))
) ,

whence
 ℓ−1∑

j=1 |A
(j)|U (j+1)
N + |A
(ℓ)|U (ℓ)
N ⩽ 3|A|UN ε1(X2, δ) + a(X2)UN

⩽ |A|UN (3ε1(X2, δ) + a(X2)) ⩽ |A|UN (3ε1(X2, δ) + a(X2)) ,

where in the last inequality we used that |A| > N
log N > X2
log X2 by (125). □

49

We combine (146) with Lemmas 48 and 49 and the bound (152) to obtain:

S(A,P (z)) > |A|V (z) − a(X2)|A|V (z)

(154)
− (1 + 32.02
log2 N
 ) {

|A|V (z) + 8|A|UN
 [
 − 2e
γ log (3 − 8α1 − 160 log log X2
log X2
 )

(4 − 8α1 − 160 log log X2
log X2 ) log N + 32.02
log3 N

+ ε1(X2, δ)(1 − f (cα1,X2))
log N + (1 + ε1(X2, δ))εC2(ε)e
2h(cα1,X2)
log N
 ]}

− 8|A|UN (3ε1(X2, δ) + a(X2)) (1 + 32.02
log2 N
 ) (mα1,X2 + εC(ε)e2h(cα1,X2)
log N
 )

− c∗
4(X2)N
log3 N 1.3841 log(log10 x1(N ))
log log(log10 x1(N )) .

The terms involving V (z) from the first and the second lines cancel out as follows:

|A|V (z) − a(X2)|A|V (z) − (
1 + 32.02
log2 N
 ) |A|V (z) = −|A|V (z) (a(X2) + 32.02
log2 N
 )

> −8|A|UN
log N
 (
a(X2) + 32.02
log2 N
 ) ,

where we used the bound (114) in the last inequality. The lower bound (154) therefore
simplifies to

8|A|UN
log N
 (
1 + 32.02
log2 N
 ) {2eγ log (3 − 8α1 − 160 log log X2
log X2
 )

(4 − 8α1 − 160 log log X2
log X2 ) − 32.02
log2 N − a(X2) − 32.02
log2 N

− ε1(X2, δ)(1 − f (cα1,X2)) − (1 + ε1(X2, δ))εC2(ε)e2h(cα1,X2)

− (3ε1(X2, δ) + a(X2)) (mα1,X2 + εC(ε)e
2h(cα1,X2)
) }

,

− c∗
4(X2)N
log3 N 1.3841 log(log10 x1(N ))
log log(log10 x1(N )) .

which completes the proof of case (b) in Theorem 44 upon noting that |A| > N
log N

by (125) and U −1
N ⩽ (2e
γ ∏
p>2 (1 − 1
(p−1)2 ))−1 which follows from the definition of

UN = U (0)
N in (113). □

7 An upper bound for ∑z⩽q<y S(Aq, P (z))

In this section, we shall obtain an upper bound for the sum over primes ∑

z⩽q<y S(Aq, P (z))
with z = N 1/8, y = N 1/3 and each q not dividing N . This is the second term appearing
in the bound for π2(N ) in Lemma 37. Compared to the lower bound for S(A, P (z)) in
50

§6, this is obtained in a quite straightforward way, using Theorem 6 and Lemmas 31
and 34. We start by defining

(155) kx := 8 ( 1
2 − 1
3 − x) = 8 ( 1
6 − x) .

Theorem 50. Let u0 = 109 and ε = 1.452 · 10
−7 be the corresponding values in
Lemma 18. Let x1 be as in (75) and X2 be such that log log x1(X2) ⩾ 10.4. Assume
that 0 < α2 < 1/24 and N ⩾ X2 is an even integer such that

N α2

log10 x1(N ) log2.5 N ⩾ exp (u0
 (
1 + 9 · 10
−7

log u0
 )) .

Let UN = U (0)
N and Kδ(x1) be as in (113) and (76) respectively. Consider the cases (a)
k1 < Kδ(x1) and (b) k1 ⩾ Kδ(x1). In case (a) we have

∑

z⩽q<y
q∤N
 S(Aq, P (z)) < UN N
log2 N
 (

8.0004 (1 + 32.02
log2 N
 ) (l1(X2) + l2(X2))

+ l(X2)

2eγ ∏
p>2 (1 − 1
(p−1)2 ) log N
 )

.

On the other hand, in case (b)

∑

z⩽q<y
q∤N
 S(Aq, P (z)) < UN N
log2 N
 (
8.0004 (
1 + 32.02
log2 N
 ) (1 + ε1(X2, δ)) (l∗
1(X2) + l2(X2))

+ l∗(X2)

2eγ ∏
p>2 (1 − 1
(p−1)2 ) log N
 )

,

where
 l(X2) :=p(X2) ( 1
log X2 + 0.55
)

+ 1.3841 (
log 8
3 + 64
log2 X2
 ) √
x1(X2) log3 X2
X2 (log log X2) (
log10 x1(X2)
) ,(156)
 l∗(X2) :=p∗(X2) ( 1
log X2 + 0.55
)

+ 1.3841 (
log 8
3 + 64
log2 X2
 ) √
x1(X2) log3 X2
X2 (log log X2) (
log10 x1(X2)
) ,(157)
 l1(X2) :=log2 X2
X2
 ( 2e
γ

kα2 + εC1(ε)e
2h(kα2)
)

·
 ( X 1/8
2
X 1/8
2 − 1
 (log 8
3 + 64
log2 X2
 ) 1.3841
log log X2 + p(X2)X2
log4 X2
 )
 ,(158)
 51

l∗
1(X2) :=log2 X2
X2
 ( 2e
γ

kα2 + εC1(ε)e
2h(kα2)
)

·
 ( X 1/8
2
X 1/8
2 − 1
 (log 8
3 + 64
log2 X2
 ) 1.3841
log log X2 + p∗(X2)X2
log4 X2
 )
 ,(159)
 l2(X2) := X 1/8
2
X 1/8
2 − 1
[ e
γ

4
 

 log(6) + log ( 3−8α2
3−18α2
 )

( 1
2 − α2) + 512
kα2 log2 X2
 



+ (
log 8
3 + 64
log2 X2
 ) εC1(ε)e2h(kα2)

]
,(160)

with p(X2) and p∗(X2) defined in Lemmas 31 and 34, ε1(X2, δ) in (121), and C1(ε) =
106 is as in Table 1.

Proof. We again begin with case (a) k1 < Kδ(x1). Let N 1
8 = z ⩽ q < y = N 1
3 . Similar
to the proof of Theorem 44 we set

(161) Q(u) := ∏

p<u
p∤N
 p, D(2) := N 1
2 −α2, D(2)
q := D(2)

q , and s(2)
q := log D(2)
q
log z .

The condition N α2

log10 x1(N ) log2.5 N ⩾ exp (u0
 (
1 + 9 · 10
−7

log u0
 ))

then guarantees that

(162) N α2

log10 x1(N ) log2.5 N ⩾ Q(u0)

by Lemma 25 and we also have qD(2)
q Q(u0) ⩽ H = √x1
log10 x1 . Moreover, the condition
α2 < 1/24 gives

(163) N 1
2 −α2

q ⩾ z,

for all z ⩽ q < y. Namely, this means that we can apply the upper bound (5) in
Theorem 6. In particular, setting gn(p) = 1/(p − 1), A = Aq, Q = Q(u0) and D = D(2)
q
in (5) gives

(164) ∑

z⩽q<y
q∤N
 S(Aq, P (z)) ⩽ 8UN
 (1 + 32.02
log2 N
 ) ∑

z⩽q<y
q∤N
 |Aq|
 (F (s(2)
q ) + εC1(ε)e
2h(s(2)
q )
log N
 )

+ ∑

z⩽q<y
q∤N
 ∑

d|P (z)
d<D(2)
q Q(u0)
 |rq(d)| .

52

where we have used (9), namely,

XA := |A| ∏

p|P (z)
(1 − gn(p)) ⩽ 8UN
log N
 (
1 + 32.02
log2 N
 ) .

by (114) in Lemma 38.
We start by bounding the sum over |rq(d)| in (164). By the definition of rq(d) given
in (124),

∑

z⩽q<y
q∤N
 ∑

d|P (z)
d<D(2)
q Q(u0)
 |rq(d)| ⩽ ∑

z⩽q<y
q∤N
 ∑

d|P (z)
d<D(2)
q Q(u0)
 (
|Eπ(N ; qd, N )| + |Eπ(N ; q, N )|
φ(d) + ω(N )
) ,

(165)

noting that (q, d) = 1 since q is a prime greater than or equal to z = N 1
8 . We thus
have to bound three sums. Since qD(2)
q Q(u0) ⩽ H, we have by Lemma 31 that the first
sum in (165) can be bounded as

(166) ∑

z⩽q<y
q∤N
 ∑

d|P (z)
d<D(2)
q Q(u0)
 |Eπ(N ; qd, N )| < p(X2)N
log3 N .

We can now bound the second sum in (165) using Lemmas 24 and 31. That is,

∑

z⩽q<y
q∤N
 ∑

d|P (z)
d<D(2)
q Q(u0)
 |Eπ(N ; q, N )|
φ(d) ⩽
 ( ∑

z⩽q<y |Eπ(N ; q, N )|

) 



 ∑

d⩽H
d|P (z)
 1
φ(d)




 ⩽ 0.55p(X2)N
log2 N .

(167)

Finally, for the third sum in (165), Lemmas 21 and 22 give

(168) ∑

z⩽q<y
q∤N
 ∑

d|P (z)
d<D(2)
q Q(u0)
 ω(N ) ⩽ 1.3841 log N
log log N
 (log 8
3 + 64
log2 N
 ) √x1(N )
log10 x1(N ),

noting that log log(y/z) = log log(N 1/3/N 1/8) = log 8
3. Hence, with l(X2) defined as in
(156), the three bounds (166), (167) and (168) give

(169) ∑

z⩽q<y
q∤N
 ∑

d|P (z)
d<D(2)
q Q(u0)
 |rq(d)| ⩽ l(X2)N
log2 N .

We now bound the sum on the right-hand side of (164). By (163) and the definition
of s(2)
q , we have 1 < s
(2)
q < 3 and thus F (s(2)
q ) = 2eγ

s(2)
q by (59). Moreover, we note that

s(2)
q ⩾ kα2 and by (106)
 |Aq| ⩽ |A| + ω(N )
q − 1 + Eπ(N ; q, N ).

53

Therefore,
∑

z⩽q<y
q∤N
 |Aq|
 (F (s(2)
q ) + εC1(ε)e2h(s(2)
q )
log N
 )

⩽ ∑

z⩽q<y
q∤N
 |A|
q − 1
 ( e
γ

4 log D(2)/q + εC1(ε)e2h(kα2)
log N
 )
(170)
 + ( eγ

4 log D(2)/y + εC1(ε)e
2h(kα2)
log N
 ) ∑

z⩽q<y
q∤N
 (ω(N )
q − 1 + Eπ(N ; q, N )
) .(171)

where we have used that h(s) is decreasing. We start bounding (171). Using Lemma 31
we obtain ∑
z⩽q<y Eπ(N ; q, N ) < p(X2)N
log3 N . Then, by Lemmas 21 and 22,

∑

z⩽q<y
q∤N
 ω(N )
q − 1 ⩽ N 1/8

N 1/8 − 1
 (log 8
3 + 64
log2 N
 ) 1.3841 log N
log log N .

This allows us to bound (171) with

(172) ( 2e
γ

kα2 + εC1(ε)e2h(kα2)
) ( N 1/8

N 1/8 − 1
 (log 8
3 + 64
log2 N
 ) 1.3841
log log N + p(X2)N
log4 N
 ) .

Dividing (172) by N/ log2 N gives rise to a monotonically decreasing function for N ⩾
X2 which is thus bounded by l1(X2) (Equation (158)). We now bound (170). Applying
Lemma 20 with f (t) = 1/ log(D/t), g(t) = log log t,

c(n) =
 {
1/n, if n is prime,
0, otherwise

and E = 64/ log2 N (as a consequence of Lemma 21), we have
∑

z⩽q<y
q∤N
 1
q log D(2)/q ⩽ ∑

z⩽q<y
 1
q log D(2)/q ⩽ ∫ y

z
 1
t log t log D(2)/tdt + 64
log2 N 1
log D(2)/y

= log(6) + log ( 3−8α2
3−18α2
 )

( 1
2 − α2) log N + 512
kα2 log3 N ,(173)

where we substituted z = N 1/8, y = N 1/3 and D(2) = N 1/2−α2 to obtain the final
equality. Using (173) and Lemma 21, we have that (170) is at most

|A|
log N N 1/8

N 1/8 − 1
 [ eγ

4
 

log(6) + log ( 3−8α2
3−18α2
 )

1
2 − α2 + 512
kα2 log2 N
 



+ (log 8
3 + 64
log2 N
 ) εC1(ε)e
2h(kα2)

]

(174)
 54

⩽ |A|
log N l2(X2),(175)

noting that each term in (174) (upon taking out the factor of |A|/ log N ) is either
constant or decreasing in N . Combining (125), (169), (172) and (174) we obtain the
desired result and thereby finish the proof of case (a).
Now we consider the case (b) k1 ⩾ Kδ(x1). This case requires a slightly different argu-
ment to case (a). In particular, we can no longer apply Lemma 31 for such large values
of k1. To circumvent this, we note that ∑

z⩽q<y S(Aq, P (z)) ⩽ ∑

z⩽q<y S(Aq, P (1)(z))
so that it suffices to bound the latter. Working with P (1)(z) as opposed to just P (z)
then allows us to guarantee d ̸= k1 in the sieve remainder term. In particular, defining

(176) Q
(1)(u) := ∏

p<u, p∤N
p̸=q1
 p

we then, similar to case (a), use Lemma 38 and Theorem 6 with gn(p) = 1/(p − 1),
A = Aq, Q = Q
(1)(u0) and D = D(2)
q in (5) to obtain

S(Aq, P (1)(z)) < |Aq|
 (
8U (1)
N
 (1 + 32.02
log2 N
 ) F (s(2)
q ) + εC1(ε)e
2h(s(2)
q )
log N
 )

+ ∑

d|P (1)(z)
d<D(2)
q Q(1)(u0)
 |rq(d)| .

Here, U (1)
N ⩽ UN (1 + ε1(X2, δ))
by Lemma 41. The proof then follows as in case (a). The only difference is that we
have ∑

z⩽q<y
q∤N
 ∑

d|P (1)(z)
d<D(2)
q Q(1)(u0)
 |Eπ(N ; qd, N )| < p∗(X2)N
log3 N , and(177)
 ∑

z⩽q<y
q∤N
 |Eπ(N ; q, N )| < p∗(X2)N
log3 N
(178)

by Lemma 34. In particular, to apply Lemma 34 we require in (177) that k1 ∤ qd and
in (178) that k1 ∤ q. However, this is true since q ⩾ z > k1 is prime and d ̸= k1 as
d | P (1)(z). □

8 An upper bound for S(B, P (y))

We will now prove an upper bound for S(B, P (y)). This is the third term appearing
in the bound for π2(N ) in Lemma 37. The bound will be obtained using Theorem 6
together with Lemmas 32 and 36. Unlike the proofs of Theorems 44 and 50 we will
only provide a single bound for S(B, P (y)) rather than giving two bounds depending
55

on the value of ki. This is in part because we define a sequence of different values for
Y = Yj appearing in Lemma 32 and then take a overall bound which is independent
of the value of the exceptional modulus.

Theorem 51. Let u0 = 109 and ε = 1.452 · 10
−7 be the corresponding values in
Lemma 18. Let 0 < δ < 2 and 0 < ε0 < 1. Set X3 to be such that log log x2(X3) ⩾ 10.4
with x2 defined in (75). Also let N > (X3)
8 be an even integer and 0 < α3 < 1/6
satisfying 3
10N α3

log10 N ⩾ exp (
u0
 (1 + 9 · 10
−7

log u0
 ))
.

We have

S(B,P (y)) < UN N
log2 N
 {

1.00005(1 + ε2((X3)
8, δ)) (
1 + 4.51
log2 N
 )

· [ 2
1
2 − α3 eγ + 3εC1(ε)e
2h ( 3
2 − 3α3
)] (
1 + ε0 + 9
log N
 )

· [
c + 36
log2 N + (
log 8
3 + 64
log2 N
 ) (10 log(1 + ε0)
log N + 27
log2 N
 )]

+
 (
2e
γ ∏

p>2
 (
1 − 1
(p − 1)2
 ))−1 (320 · m(X3)(1 + ε0)
3 log(1 + ε0) + 0.13(1 + ε0) log5 N

N 1
8 log(1 + ε0)
 ) }

,

with UN defined in (2), c defined in Lemma 52 below, m(X3) in Lemma 32, ε2 in
Lemma 41, and C1(ε) = 106 from Table 1.

Before we prove Theorem 51 we start by recalling that

B = {N − p1p2p3 : z ⩽ p1 < y ⩽ p2 ⩽ p3, p1p2p3 < N, (p1p2p3, N ) = 1}

where z = N 1/8 and y = N 1/3 (Equations (104) and (108)). With a view to apply
Lemma 32, we now drop the restriction (p1, N ) = 1 and relax the condition p1p2p3 < N ,
so that p1 and p2p3 will range over independent intervals giving a bilinear form. In
doing this we define

B(j) := {N − p1p2p3 : z ⩽ p1 < y ⩽ p2 ⩽ p3,

ωjp2p3 < N, (p2p3, N ) = 1, ωj ⩽ p1 < ωj(1 + ε0)},(179)

where

(180) ωj := z(1 + ε0)
j for 0 ⩽ j ⩽ j0 := log y/z
log(1 + ε0),

with 0 < ε0 < 1. We see that
∣
∣B(j)∣
∣ = (π(Yj) − π(Zj))♯{(p2, p3) : y ⩽ p2 ⩽ p3, ωjp2p3 < N, (p2p3, N ) = 1},

where

(181) Zj := ωj and Yj := min (ωj(1 + ε0), y) .
56

Defining B := ∪jB(j), we have

(182) B ⊆ B ⊆ {N − p1p2p3 : z ⩽ p1 < y ⩽ p2 ⩽ p3, p1p2p3 < (1 + ε0)N }

and

(183) S(B, P (y)) ⩽ S(B, P (y)) = ∑

j⩽j0 S(B(j), P (y)).

We now prove an explicit upper bound for the cardinality of B in a similar way as done
by Nathanson in [40, pp. 289–291].

Lemma 52. Keeping the notation and conditions of Theorem 51, we have

∣
∣B∣
∣ ⩽ (1 + ε0 + 9
log N
 ) N
log N

· [c + 36
log2 N + (log 8
3 + 64
log2 N
 ) (10 log(1 + ε0)
log N + 27
log2 N
 )] ,

with c = ∫ 1/3
1/8 log(2−3β)
β(1−β) dβ < 0.363084.

Proof. First note that since p1 < p2 ⩽ p3 and p1p2p3 < (1 + ε0)N , we have

p3 < (1 + ε0)N
p1p2 and(184)
 p1p2
2 < (1 + ε0)N(185)

Using (184) and 0 < ε0 < 1, we then obtain via [46, Theorem 1]

π ( (1 + ε0)N
p1p2
 ) ⩽ (
1 + ε0 + 9
log N
 ) N
p1p2 log(N/p1p2).

Thus, from the definition (182) of B and (184),

∣
∣B∣
∣ ⩽ ∑

z⩽p1<y⩽p2⩽p3
p1p2p3<(1+ε0)N
 1 ⩽ ∑

z⩽p1<y⩽p2
p1p2
2<(1+ε0)N
 π ( (1 + ε0)N
p1p2
 )

⩽ (1 + ε0 + 9
log N
 ) N ∑

z⩽p1<y
 1
p1
 ∑

y⩽p2<w
 1
p2 log(N/p1p2),(186)

with w = √ (1+ε0)N
p1 .

We now introduce the functions hp(t) = (log N/pt)−1 and

I(u) = ∫ √N/u

y hu(t)d log log t.

Noting that
 y = N 1/3 ⩾ X 8/3
2 > 286,
57

we apply Lemma 20 with f (t) = hp1(t), g(t) = log log t,

c(n) =
 {
1/n, if n is prime,
0, otherwise

and E = 1/ log2 y (as a consequence of Lemma 21) to obtain
∑

y⩽p2<w
 1
p2 log(N/p1p2) ⩽ ∫ w

y hp1(t)d log log t + hp1(w)
log2 y

= I(p1) + ∫ w

√ N
p1 hp1(t)d log log t + hp1(w)
log2 y

⩽ I(p1) + 10 log(1 + ε0)
log2 N + 27
log3 N .

Where, in the last step, we substituted y = N 1/3 and applied the bounds
∫ w

√ N
p1 hp1(t)d log log t ⩽ 10 log(1 + ε0)
log2 N
(187)
 hp1(w) = 2

log ( N
(1+ε0)p1
 ) ⩽ 3
log N .

Here, (187) is obtained by the change of variables t = √
N/p1s as in [40, p. 290].
Therefore, also using Lemma 21,
∑

z⩽p1<y
 1
p1
 ∑

y⩽p2<w
 1
p2 log(N/p1p2)

⩽ ∑

z⩽p1<y
 I(p1)
p1 + (
log 8
3 + 64
log2 N
 ) (10 log(1 + ε0)
log2 N + 27
log3 N
 ) .(188)

Next we note that [40, p. 291]
∫ y

z I(u)d log log u = c
log N
and upon using the substitution t = N τ ,

0 = I(y) ⩽ I(z) = 1
log N
 ∫ 7/16

1/3
 1
( 7
8 − τ )τ dτ ⩽ 0.56
log N .

We can thereby apply Lemma 20 with f (t) = I(t), g(t) = log log t,

c(n) =
 {
1/n, if n is prime,
0, otherwise

and E = 1/ log2 z (as a consequence of Lemma 21) to obtain
∑

z⩽p1<y
 I(p1)
p1 < ∫ y

z I(t)d log log t + I(z)
log2 z

58

⩽ c
log N + 36
log3 N .(189)

Using (189) to bound (188) we can then bound |B| in (186), which concludes the proof
of the lemma. □

Equipped with Lemma 52, we now prove Theorem 51.

Proof of Theorem 51. From (183) we see that to bound S(B, P (y)) it suffices to bound
each S(B(j), P (y)) for 0 ⩽ j ⩽ j0, with B(j) defined in (179) and j0 defined in (180).
So, we begin by fixing a value of j and consider the two cases k2 < Kδ(x2(Yj)) and
k2 ⩾ Kδ(x2(Yj)). Here, Yj is as in (181) and k2, Kδ, x2 are as defined in Section 4.1
with Y = Yj.

Case 1: k2 < Kδ(x2(Yj)).
Let
 Q(u) := ∏

p<u
p∤N
 p, D(3) := N 1
2 −α3, sb := log D(3)/ log y(190)

and
 R(j) := ∑

d<D(3)Q(u0)
d|P (y)
 ∣
∣
∣r(j)
d ∣
∣
∣

where r(j)
d = ∣
∣
∣B(j)
d ∣
∣
∣ − |B(j)|
φ(d) , and

B(j)
d = ∑

p1p2p3≡N (mod d)
z⩽p1<y⩽p2⩽p3, ωj ⩽p1<ωj (1+ε0)
ωj p2p3<N, (p2p3,N )=1
 1.

Now, since α3 < 1/6, we have D(3) ⩾ y = N 1/3.

Therefore, we can apply Theorem 6 to the set B(j) with gn(p) = 1/(p − 1), Q = Q(u0)
and D = D(3) in (5) to give

S(B(j), P (y)) < ∣
∣B(j)∣
∣ V (y)(F (s) + εC1(ε)e2h(s)) + R(j).

By (115) in Lemma 38 we have V (y) < 3 UN
log N (1 + 4.51
log2 N ). We also see by (190) that

sb = 3
2 − 3α3 < 3 and therefore F (sb) = 2eγ
sb by (59). Hence

S(B(j),P (y)) <

(191)
 ∣
∣B(j)∣
∣ UN
log N
 (
1 + 4.51
log2 N
 ) [ 2
1
2 − α3 e
γ + 3εC1(ε)e
2h (3
2 − 3α3
)] + R(j).

59

Now, from the definition of the sets B(j), we obtain

r(j)
d = ∑

p1p2p3≡N (mod d)
z⩽p1<y⩽p2⩽p3, ωj ⩽p1<ωj (1+ε0)
ωj p2p3<N, (p2p3,N )=1
 1 − 1
φ(d)
 ∑

z⩽p1<y⩽p2⩽p3
ωj ⩽p1<ωj (1+ε0)
ωj p2p3<N, (p2p3,N )=1
 1.

We now add the condition (p1p2p3, d) = 1 to the second sum above. This is equivalent
to (p1, d) = 1, since the condition (p2p3, d) = 1 already follows from the fact that d
divides P (y) and p2, p3 ⩾ y. This condition decreases the second term above by at
most
1
φ(d)
 ∑

p1p2p3<(1+ε0)N
p1|d,p1⩾z
 1 ⩽ (1 + ε0)N
φ(d)
 ∑

p1|d,p1⩾z
 1
p1 ⩽ (1 + ε0)N ω(d)
zφ(d) ⩽ (1 + ε0)N log d
zφ(d) log 2 ,

where the last inequality uses Lemma 22. We now put a(n) = aN (n) to be the char-
acteristic function of the set of integers of the form n = p2p3 with y ⩽ p2 ⩽ p3 and
(N, p2p3) = 1. Then, for |θ| ⩽ 1 we see that

r(j)
d = ∑

n<Xj
 ∑

Zj ⩽p<Yj
np≡N (mod d)
 a(n) − 1
φ(d)
 ∑

n<Xj
 ∑

Zj ⩽p<Yj
(np,d)=1
 a(n) + (1 + ε0)θN log d
zφ(d) log 2 ,

with

(192) Xj = N
wj , Yj = min (y, (1 + ε0)wj) and Zj = wj.

With X = Xj, Y = Yj and Z = Zj the conditions in Lemma 32 hold. Moreover, we
also see that, from the condition
3
10N α3

log10 N ⩾ exp (
u (
1 + 9 · 10
−7

log u
 ))

and Lemma 25, D∗ := √Xj Yj
log10 Yj ⩾ √N
log10 y ⩾ D(3) · Q(u0). Therefore, using Lemmas 24 and

32, and the bound Yj ⩾ z = N 1/8, we obtain

R(j) ⩽ ∑

d<D∗
d|P (y)
 ∣
∣
∣r(j)
d ∣
∣
∣

⩽ ∑

d<D∗
d|P (y)
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

n<Xj
 ∑

Zj ⩽p<Xj
np≡N (mod d)
 a(n) − 1
φ(d)
 ∑

n<Xj
 ∑

Zj ⩽p<Xj
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
 + ∑

d<D∗
d|P (y)
 ( (1 + ε0)N log d
zφ(d) log 2
 )

⩽m(X3)(1 + ε0)8
3N
log3 N + 1.1
log 2 (1 + ε0)N 7
8 log2 D∗

⩽m(X3)(1 + ε0)8
3N
log3 N + 0.58(1 + ε0)N 7
8 log2 N

(193)
 60

where in the last inequality we have used the bound D∗ ⩽ √XjXj ⩽ √
N y/z = N 29/48.
Substituting this into (191) gives us an upper bound for S(B(j), P (y)) in terms of B(j).
We now move onto the second case k2 ⩾ Kδ(x2(Yj)).

Case 2: k2 ⩾ Kδ(x2(Yj)).
As in the proof of part (b) of Theorem 50, we avoid complications with the ex-
ceptional zero by working with P (1)(y) as opposed to P (y). In particular, since
S(B(j), P (y)) ⩽ S(B(j), P (1)(y)) it suffices to bound the latter. We also let Q
(1)(u)
be as in (176) with q1 now denoting the largest prime factor of k2. Now, similar to the
first case, we apply Theorem 6 to the set B(j), with gn(p) = 1/(p − 1), Q = Q
(1)(u0)
and D = D(3) in (5) to give (cf. (191))

S(B(j), P (1)(y)) < ∣
∣B(j)∣
∣UN (1 + ε2((X3)
8, δ))
log N
 (
1 + 4.51
log2 N
 )
(194)
 · [ 2
1
2 − α3 e
γ + 3εC1(ε)e2h ( 3
2 − 3α3
)] + R(1,j),

where

(195) R(1,j) := ∑

d<D(3)Q(1)(u0)
d|P (1)(y)
 |r(j)
d |.

and we have used that U (1)
N ⩽ UN (1 + ε2((X3)
8, δ))
by Lemma 41. We can then bound for R(1,j) in the same way as R(j) in the case
k2 < Kδ(x2(Yj)). However, since in the definition (195) of R(1,j) we have d | P (1)(y)
and thus k2 ∤ d, we apply Lemma 36 (as opposed to 32) to obtain

(196) R(1,j) ⩽ ∑

d<D∗
d|P (1)(y)
 ∣
∣
∣r(j)
d ∣
∣
∣ ⩽ m
∗(X3)(1 + ε0)8
3N
log3 N + 0.58(1 + ε0)N 7
8 log2 N.

Substituting this into (194) gives us an upper bound for S(B(j), P (1)(y)) and thus
S(B(j), P (y)) in terms of |B(j)| when k2 ⩾ Kδ(x2(Yj)).

We now combine our bounds for the two cases k2 < Kδ(x2(Yj)) and k2 ⩾ Kδ(x2(Yj)).
In particular, by taking the maximum of our expressions for S(B(j), P (y)) and S(B(j), P (1)(y))
in (191) and (194) with our bounds for R(j) and R(1,j) in (193) and (196), we find that,
for all values of k2

S(B(j), P (y)) < ∣
∣B(j)∣
∣UN (1 + ε2((X3)
8, δ))
log N
 (
1 + 4.51
log2 N
 )
(197)
 · [ 2
1
2 − α3 e
γ + 3εC1(ε)e2h ( 3
2 − 3α3
)]
(198)
 + m(X3)(1 + ε0)83N
log3 N + 0.58(1 + ε0)N 7
8 log2 N,

61

noting that m
∗(X3) ⩽ m(X3) by their respective definitions in Lemmas 32 and 36. To
finish off, we sum (197) over 0 ⩽ j ⩽ j0. Namely, using (183) along with the fact that
B = ⋃
j Bj is a disjoint union and j0 = log(y/z)
log(1+ε0) = 5 log N
24 log(1+ε0) ,

S(B, P (y)) ⩽ ∑

j⩽j0 S(B(j), P (y))

⩽ ∣
∣B∣
∣ UN (1 + ε2((X3)8, δ))
log N
 (
1 + 4.51
log2 N
 )

· [ 2
1
2 − α3 eγ + 3εC1(ε)e
2h ( 3
2 − 3α3
)]

+ 320 · m(X3)(1 + ε0)N
3 log(1 + ε0) log2 N + 0.13(1 + ε0)N 7
8 log3 N
log(1 + ε0) .

Applying our bound for |B| in Lemma 52 then completes the proof of the theorem. □

9 Proof of Theorem 3

Being now equipped with a lower bound on S(A, P (z)) (Theorem 44) and upper
bounds on ∑

z⩽q<y S(Aq, P (z)) (Theorem 50) and S(B, P (y)) (Theorem 51) we can
prove our main result, Theorem 3, by using the estimate on π2(N ) given in Lemma 37.
Specifically we need to select suitable values for X2, X3, δ, α1, α2, α3 and ε0 such that
the conditions in Theorems 44, 50 and 51 hold, and (1) is true for each possible range
of k1. This is obtained with X2 = exp(exp(32.7)), X3 = exp(exp(30.62)), δ = 1.478,
α1 = α2 = α3 = 10
−5 and ε0 = 10
−4. Note that when computing the lower bound from
Theorem 44, we can use (125) and replace |A| by N
log N once we have ensured that the
lower bound is positive. In particular, with these choices of parameters, we find that
for N ⩾ X2 ⩾ X 8
3 π2(N ) > 1
10 · UN N
log2 N
for k1 < Kδ(x1(N )) and
 π2(N ) > 2 · 10
−4 · UN N
log2 N
for k1 ⩾ Kδ(x1(N )).
In obtaining these parameters, we found that the most sensitive variable was δ. So,
we only roughly optimised over α1, α2, α3 and ε0 before focusing on finding the value
of δ which allowed us to take the lowest value of X2. Note that increasing δ causes
the bound β0 on the Siegel zero to get very large (see (81)), whereas taking δ smaller
causes εi(X2, δ) to become too large (see Lemma (41)). It therefore seems that the
clearest way to improve our result would be to improve on the Siegel zero bounds we
used from [2] and [3].
It is however interesting to note that using the technique developed here it would
be impossible5 to prove Theorem 3 for N ⩾ exp(exp(22)). This is because our lower

5That is, unless some far-reaching result is proven, such as the non-existence of Siegel zeros.
62

bound for π2(N ) (accounting for the possibility of a large exceptional zero) is at best

F(X2, δ) = 2 log 3 − (1 + ε1(X2, δ)) log(6) − (1 + ε2(X 1/8
2 , δ))c

and F(exp(exp(22)), 2) < 0. Since taking δ close to 2 is very difficult without better
bounds on the exceptional zero, it would be tough to even reach N ⩾ exp(exp(30))
with the current framework. As a result, a different approach would be required to
obtain a substantial improvement to Theorem 3. In this regard, Cai [12], Wu [49]
and very recently Li [35] give an alternate (albeit more complicated) proof of Chen’s
theorem which is asymptotically superior to the method we adapted from Nathanson
[40]. Therefore, it is likely that an explicit version of these methods (or similar) would
give a better result than the one obtained here.

10 Proof of Corollary 4 and Theorem 5

In this section we prove Corollary 4 and Theorem 5 which follow readily from our
main result (Theorem 3). For Corollary 4 we let π2(N ) be as in Theorem 3, and π∗
2(N )
denote the number of representations of an even integer N as the sum of a prime and a
square-free number η > 1 with at most two prime factors. So, let N > exp(exp(32.7))
be an even integer and consider representations of the form

(199) N = p + η,

where p is prime and η has at most two prime factors. If η is not square-free there are
two possible cases: either η = 1, or η has two identical prime factors.
For a fixed value of N , the case η = 1 corresponds to at most one representation of
the form (199). That is, either N − 1 is prime and we set p = N − 1, or η = 1 does
not give any valid representation.
On the hand if η has two identical prime factors, q1 and q2, then q1 = q2 < √
N . As
a result, such values of η correspond to at most √N representations of the form (199).
Combining these two cases, we have, by Theorem 3,

π∗
2(N ) ⩾ π2(N ) − 1 − √N > 2 · 10
−4 · UN N
log2 N − 1 − √N > 0,

which proves Corollary 4.
We now prove Theorem 5. For this, we require the following result proved in [21].

Theorem 53 (Dudek). All integers greater than two can be written as the sum of a
prime and a square-free number.

Theorem 5 now follows from Theorem 3 and, by Theorem 53, computing the largest
k such that ∏

i⩽k pi ⩽ e
e32.7.

By [46, Theorems 3 & 4] we have e
29.2 < k < e29.3. It should be possible to exactly
compute k, but we will not do so here. We also note that Theorem 53 was improved by
Lee and Francis in [22], and Hathi and Johnston in [26]. However, such improvements
have a negligible impact on Theorem 5 unless Theorem 3 is substantially improved.
63

11 Notation index

As this paper contains a lot of different notation, below we have added page and
equation numbers for the definitions of different pieces of notation used. If there is
no equation number we will instead state the theorem, lemma, proof etc. where the
notation first appears. Note that some notations are defined twice: in general (gen.)
and then in a particular way to be applied to the proof of the main result (appl.). Note
also that throughout the paper, letters p, q and any subscripts thereof (e.g. pi and qi)
will always denote prime numbers.

α, p8, eq.(24) α1, p42, Thm.44
α2, p51, Thm.50 α3, p56, Thm.51

βk, p21, Lem.27 β0(x), p24, eq.(81)

β∗
0(x), p33, eq.(99) γ3, p8, Lem.9
γs0, p8, Lem.9 δ, p23, Sec.4.1

ε, p4, eq.(4) εi(X2, δ), p39, eq.(121)

θ(x), p17, eq.(51) κs0, p8, Lem.10

˜κ, p8, Lem.10 ν(x), p24, eq.(81)

ξs0, p11, aft.eq.(31) ˜ξ, p11, aft.eq.(31)

π2(N ), p2, Thm.3 π∗
2(N ), p63, Sec.10

τn, p11, eq.(31) τ ′
n, p13, eq.(40)

φ
∗(n), p47, pf Lem.48 χ∗, p25, pf Lem.30

χ0, p22, Lem.28 ω(n), p20, Lem.22

ω(n; q, a), p35, Sec.5 ωj, p56, eq.(180)

A, p4, Thm.6(gen.) A, p35, eq.(105)(appl.)

A(j), p36, eq.(110) Ad, p4, Thm.6(gen.)

Ad, p35, eq.(105)(appl.) a(n) = aN (n), p60, pf Thm.51

a(x), p42, eq.(138) a1(x), p42, eq.(139)

B, p35, eq.(108) B, p57, bef.eq.(182)

Bµ,φ, p20, Lem.24 B(j), p56, eq.(179)

B(j)
d , p59, aft.eq.(190) C1(ε), p5, Table 1

C2(ε), p5, Table 1 C(ε), p42, pf Thm.44

c, p57, Lem.52 c(x), p31, eq.(97)

c1(x), p31, eq.(97) c2(x), p40, eq.(127)

c3(x), p40, eq.(129) c4(x), p41, eq.(134)

c
∗
4(x), p41, eq.(135) cα,x, p42, eq.(136)
cn, p7, Table 2 D, p4, Thm.6

D∗, p28, Lem.32(gen.) D∗, p60, pf Thm.51(appl.)
64

D0, p29, pf Lem.32 D(1), p43, eq.(141)

D(1)
j , p45, Lem.46 D(2), p52, eq.(161)

D(2)
q , p52, eq.(161) D(3), p59, eq.(190)

Df (x; q1, q2, l), p33, eq.(100) Ej, p45, Lem.46

E(x), p24, eq.(80) Ef (x; k, l), p21, eq.(67)

F (s), p5, eq.(8), (59), (60) F(x, δ), p63, Sec.9

f (s), p5, eq.(8), (61), (62) f (x, χ), p21, eq.(68)

fn(s), p6, eq.(15) − (17) G(z, λ
±), p14, Prop.13

gn(d), p4, Thm.6(gen.) gn(d), p16, Sec.2.5(appl.)

H := H(N ), p24, Lem.30 H(s), p8, eq.(24)

h(s), p5, eq.(7) hn(s)(Sec.2), p11, eq.(32)

hp(t)(Sec.8), p57, pf Lem.52 I(u), p57, pf Lem.52

Indk, p21, Lem.27 J(k), p15, Lem.14

j0, p56, eq.(180) K, p10, eq.(30)

Kδ(x), p23, eq.(76) ki, p24, eq.(77)

kx, p51, eq.(155) k0(xi), p24, bef.(77)

ℓ, p36, bef.(110) l(x), p51, eq.(156)

l∗(x), p51, eq.(157) l1(x), p51, eq.(158)

l∗
1(x), p52, eq.(159) l2(x), p52, eq.(160)

li(x), p17, eq.(52) M, p16, eq.(47)

mα1,x, p42, eq.(137) mj, p36, eq.(110)

m(x), p28, Lem.32 m
∗(x), p35, Lem.36

P, p4, Thm.6(gen.) P, p43, pf Thm.44(appl.)

P (x), p4, Thm.6(gen.) P (x), p23, eq.(76)(appl.)

P (j)(x), p36, eq.(110) p(x), p27, eq.(87)

p∗(x), p33, Lem.34 pi(x), p27, eq.(87)

Q(u), p43, eq.(141) Q
(1)(u), p55, eq.(176)

Q1(x), p23, eq.(76) qj, p36, bef.(110)

R, p5, eq.(10) Ri, p21, Thm.26

R(j), p59, aft.eq.(190) R(1,j), p61, eq.(195)

r(d), p4, Thm.6(gen.) r(d), p39, eq.(122)(appl.)

rk(d), p39, eq.(122) r(j)
d , p59, aft.eq.(190)

S(A, n), p35, eq.(107) S(A, P, z), p4, Thm.6

s, p5, Thm.6 s
(1), p43, eq.(141)

sb, p59, eq.(190) s
(1)
j , p45, Lem.46

65

s
(2)
q , p52, eq.(161) TN (D, z), p10, eq.(28)

UN , p2, eq.(2) U (j)
N , p36, eq.(113)

u0, p18, Lem.18 V (x), p5, eq.(11)(gen.)

V (x), p36, eq.(111)(appl.) V (j)(x), p36, eq.(111)

v0, p28, Lem.32 vk(x), p22, eq.(71)

v′
k(x), p22, eq.(72) w, p57, aft.eq.(186)

X, p23, eq.(73)(gen.) X, p60, eq.(192)(appl.)
X1, p22, Lem.29 X2, p23, Sec.4.1

X3, p23, Sec.4.1 XA, p5, eq.(9)

Xj, p60, eq.(192) x1(N ), p23, eq.(75)

x2(Y ), p23, eq.(75) x(n)
k , p7, aft.eq.(20)

Y, p23, eq.(73)(gen.) Y, p60, aft.eq.(192)(appl.)

Yj, p56, eq.(181) y, p23, eq.(74)

yn, p10, Sec.2.4 Z, p23, eq.(73)(gen.)

Z, p60, aft.eq.(192)(appl.) Zj, p56, eq.(181)

z, p4, Thm.6(gen.) z, p23, eq.(74)(appl.)

66

References

[1] A. Akbary and K. Hambrook, A variant of the Bombieri-Vinogradov theorem with explicit con-
stants and applications Math. Comp.: 84(294): 1901–1934, 2015.
[2] M. Bordignon, Explicit bounds on exceptional zeroes of Dirichlet L-functions, J. Number Theory,
201:68–76, 2019.
[3] M. Bordignon, Explicit bounds on exceptional zeroes of Dirichlet L-functions II, J. Number The-
ory, 210: 481–487, 2020.
[4] M. Bordignon, Medium-sized values for the prime number theorem for primes in arithmetic pro-
gressions New York J. Math., 27:1415–1438, 2021.
[5] K. G. Borodzkin, On the problem of I. M. Vinogradov’s constant, Proc. Third All-Union Math.
Conf., 1956.
[6] S. Broadbent, H. Kadiri, A. Lumley, N. Ng and K. Wilk, Sharper bounds for the Chebyshev
function θ(x), Math. Comp.: 90(331):2281–2315, 2021.
[7] J. B¨uthe A Brun-Titchmarsh inequality for weighted sums over prime numbers Acta Arith. 166.3
289–299, 2014.
[8] J. B¨uthe An analytic method for bounding ψ(x). Math. Comp. 87.312: 1991–2009, 2018.
[9] Y. Cai and M. Lu, Chen’s theorem in short intervals, Acta Arith., 91(4):311–323, 1999.
[10] Y. Cai, Chen’s theorem with small primes, Acta Math. Sin., 18(3):597–604, 2002.
[11] Y. Cai and M. Lu, On Chen’s theorem, In: Jia C., Matsumoto K. (eds) Analytic Number Theory.
Developments in Mathematics, vol 6. Springer, Boston, MA, 2002.
[12] Y. Cai, On Chen’s theorem. II. J. Number Theory, 128(5):1336–1357, 2008.
[13] Y. Cai, A remark on Chen’s theorem with small primes, Taiwanese J. Math., 19(4):1183–1202,
2015.
[14] M. Car, Le th´eor`eme de Chen pour Fq[X], Dissertationes Math. (Rozprawy Mat.) 223, 54 pp.,
1984.
[15] J. R. Chen, On the representation of a large even integer as the sum of a prime and the product
of at most two primes, Kexue Tongbao, 17:385–386, 1966.
[16] J. R. Chen, On the representation of a large even integer as the sum of a prime and the product
of at most two primes, Sci. Sinica, 16:157–176, 1973.
[17] J. R. Chen, On the representation of a large even integer as the sum of a prime and the product
of at most two primes. II, Sci. Sinica, 21(4):421–430, 1978.
[18] J. R. Chen, Further improvement on the constant in the proposition ‘1+2’: On the represen-tation
of a large even integer as the sum of a prime and the product of at most two primes (II), Sci.
Sinica, 21(4):477–49, 1978.
[19] N. G. Chudakov, Introduction to the Theory of Dirichlet L-Functions, OGIZ, Moscow-Leningrad,
1947.
[20] H. Davenport, Multiplicative Number Theory, Third Edition, Graduate Texts in Mathematics,
74. Springer-Verlag, New York, 2000.
[21] A. W. Dudek, On the sum of a prime and a square-free number, Ramanujan J., 42:233–240, 2017.
[22] F. J. Francis and E. S. Lee, Additive Representations of Natural Numbers, Integers, 22 (#A14),
2022.
[23] J.B. Friedlander and H. Iwaniec, Opera de Cribro, American Mathematical Society, Providence
RI, 2010.
[24] G. Greaves, Sieves in Number Theory, Springer-Verlag, Berlin, 2001.
[25] H. Halberstam, A proof of Chen’s theorem, Journ´ees Arithm´etiques de Bordeaux, Ast´erisque,
(24-25):281–293, 1975.
[26] S. Hathi and D. R. Johnston, On the sum of a prime and a square-free number with divisibility
conditions, J. Number Theory, 256:354–372, 2024.
[27] H. Helfgott, The ternary Goldbach problem, to appear in Ann. of Math. Studies.
[28] J. G. Hinz, Chen’s theorem in totally real algebraic number fields, Acta Arith., 58(4):335–361,
1991. 67

[29] H. Iwaniec, Sieve Methods, Graduate Course, Rutgers university, New Brunswick, NJ, unpub-
lished notes, 1996.
[30] D. R. Johnston and A. Yang, Some explicit estimates for the error term in the prime number
theorem J. Math. Anal. Appl., 527(2): Paper No. 127460, 23 pp., 2023.
[31] W. B. Jurkat and H.-E. Richert, An improvement on Selberg’s sieve method I, Acta Arith.,
11:207–216, 1965.
[32] H. Kadiri, An explicit zero-free region for the Dirichlet L-functions, arXiv:math/0510570v1, 2005.
[33] H. Kadiri and A. Lumley Short effective intervals containing primes Integers, 14 (#A61), 2014.
[34] Y. Li and Y. Cai, Chen’s theorem with small primes, Chin. Ann. Math. Ser. B, 32(3):387–396,
2011.
[35] R. Li, On Chen’s theorem, Goldbach’s conjecture and almost prime twins,
https://arxiv.org/abs/2405.05727, 2024.
[36] M. Lu and Y. Cai, Chen’s theorem in short intervals, Chinese Sci. Bull., 43(16):1401–1403, 1998.
[37] M. Lu and Y. Cai, Chen’s theorem in arithmetical progressions, Sci. China Ser. A, 42(6):561–569,
1999.
[38] H. L. Montgomery and R. C. Vaughan, The large sieve, Matematika, 20(40):119–134, 1973.
[39] H. L. Montgomery and R. C. Vaughan, Multiplicative number theory. I. Classical theory Cam-
bridge University Press, Cambridge, 2007.
[40] B. M. Nathanson, Additive Number Theory, The classical bases, Graduate Texts in Mathematics,
164, Springer-Verlag, New York, 1996.
[41] T. Oliveira e Silva, Goldbach Conjecture verification , http://sweet.ua.pt/tos/goldbach.html.
[42] T. Oliveria e Silva, S. Herzog and S. Pardi Empirical verification of the even Goldbach conjecture
and computation of prime gaps up to 4 · 1018 Math. Comp., 83 (288): 2033–2060, 2014.
[43] G. Robin, Estimation de la fonction de Tchebychef θ sur le k-i`eme nombre premier et grandes
valeurs de la fonction ω(n) nombre de diviseurs premiers de n, Acta Arith., 42(4):367–389, 1983.
[44] A. A. R´enyi, On the representation of an even number as the sum of a prime and an almost
prime, Izv. Akad. Nauk. SSSR 12:57–78 (in Russian), 1948.
[45] P. M. Ross, On Chen’s theorem that each large even number has the form p1+p2 or p1+p2p3, J.
London Math. Soc. (2), 10(4):500–506, 1975.
[46] J. B. Rosser and L. Schoenfeld, Approximate formulas for some functions of prime numbers,
Illinois J. Math., 6:64–94, 1962.
[47] I. M. Vinogradov, Representation of an odd number as a sum of three primes, Dokl.Akad. Nauk.
SSR, 15:291–294, 1937.
[48] J. Wu, Chen’s double sieve, Goldbach’s conjecture and the twin prime problem, Acta Arith.,
114(3):215–273, 2004.
[49] J. Wu, Chen’s double sieve, Goldbach’s conjecture and the twin prime problem. II. Acta Arith.,
131(4):367–387, 2008.
[50] T. Yamada, Explicit Chen’s theorem, https://arxiv.org/abs/1511.03409, 2015.

KTH Royal Institute of Technology, Stockholm
and
Charles University, Faculty of Mathematics and Physics, Department of Algebra,
Sokolovsk´a 83, 186 00 Praha 8, Czech Republic Department of Mathematics
Email address: matteobordignon91@gmail.com

The University of New South Wales Canberra, School of Science
Email address: daniel.johnston@unsw.edu.au

The University of New South Wales Canberra, School of Science
Email address: v.starichkova@unsw.edu.au
 68
