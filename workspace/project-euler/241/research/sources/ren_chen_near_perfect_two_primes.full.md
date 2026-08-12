<!-- source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/07195AD6B597AFD416F0AE1935286E3F/S0004972713000178a.pdf/div-class-title-on-near-perfect-numbers-with-two-distinct-prime-factors-div.pdf | converted from PDF -->

Bull. Aust. Math. Soc. 88 (2013), 520–524
doi:10.1017/S0004972713000178

ON NEAR-PERFECT NUMBERS WITH TWO DISTINCT
PRIME FACTORS

XIAO-ZHI REN and YONG-GAO CHEN ˛

(Received 29 December 2012; accepted 12 January 2013; ﬁrst published online 11 March 2013)

Abstract

Recently, Pollack and Shevelev [‘On perfect and near-perfect numbers’, J. Number Theory 132 (2012),
3037–3046] introduced the concept of near-perfect numbers. A positive integer n is called near-perfect
if it is the sum of all but one of its proper divisors. In this paper, we determine all near-perfect numbers
with two distinct prime factors.

2010 Mathematics subject classiﬁcation: primary 11A25; secondary 11B83.
Keywords and phrases: perfect number, sum-of-divisors function, near-perfect number.

1. Introduction

A positive integer is called a perfect number if it is the sum of all of its proper divisors.
It is well known that Euler proved that an even perfect number can be written as
2p−1(2p − 1), where both p and 2p − 1 are primes. Primes of the form 2p − 1 are called
Mersenne primes. Lenstra, Pomerance, and Wagstaﬀ have conjectured that there are
inﬁnitely many Mersenne primes (see the discussion in [1]).
Following Pollack and Shevelev [2], a positive integer n is called a near-perfect
number if it is the sum of all but one of its proper divisors. The missing divisor d is
called redundant. That is, n is near-perfect with redundant divisor d if and only if d
is a proper divisor of n and σ(n) = 2n + d. Pollack and Shevelev [2] constructed the
following three types of near-perfect numbers.

Type 1. n = 2
t−1(2t − 2
k − 1), where 2
t − 2
k − 1 is prime, and 2
k is the redundant
divisor.
Type 2. n = 2
2p−1(2p − 1), where both p and 2p − 1 are prime numbers, and 2p(2p − 1)
is the redundant divisor.
Type 3. n = 2p−1(2p − 1)2, where both p and 2p − 1 are prime numbers, and 2p − 1 is
the redundant divisor.

This work was supported by the National Natural Science Foundation of China, Grant No. 11071121.
c⃝ 2013 Australian Mathematical Publishing Association Inc. 0004-9727/2013 $16.00

520

https://doi.org/10.1017/S0004972713000178 Published online by Cambridge University Press

[2] On near-perfect numbers with two distinct prime factors 521

R 1.1. If p and 2p − 1 are prime numbers, then

n = 2p(2p − 1) = 2p(2p+1 − 2p − 1)

is a near-perfect number with redundant divisor 2p. In this case, n = 2m, where
m = 2p−1(2p − 1) is an even perfect number. Pollack and Shevelev [2, Proposition 3]
proved that if n = 2 jm is a near-perfect number, where m is an even perfect number,
then either n = 2p(2p − 1) or n = 22p−1(2p − 1), where both p and 2p − 1 are prime
numbers. It is clear that if the Lenstra–Pomerance–Wagstaﬀ conjecture is true, then
there are inﬁnitely many near-perfect numbers.

We observe that near-perfect numbers of types 1, 2 and 3 have two distinct prime
factors. It is easy to see that 40 is a near-perfect number with redundant divisor 10,
and 40 is not of type 1, 2 or 3.
In this paper, we determine all near-perfect numbers with two distinct prime factors.

T 1.2. All near-perfect numbers with two distinct prime factors are of types 1,
2 and 3, together with 40.

Among the ﬁrst 39 near-perfect numbers which are listed in A181595 in [3], except
for the number 40, 21 (12, 20, 56, 88, 104, 368, 464, 992, 1504, 1888, 1952, 16256,
24448, 28544, 30592, 32128, 98048, 122624, 128768, 130304, 507392) are of type 1;
three (24, 224, 15872) are of type 2; three (18, 196, 15376) are of type 3, and 11 (234,
650, 3724, 5624, 9112, 11096, 13736, 17816, 77744, 174592, 396896) have three
distinct prime factors. D. Johnson has found that 173369889 = 34 × 72 × 112 × 19
2

the smallest odd near-perfect number and P. Moses has veriﬁed that this is the only
odd near-perfect number up to 1.4 × 1019 (see A181595 in [3]). (From the deﬁnition
of near-perfect numbers, one may see that all odd near-perfect numbers are squares.)
We pose the following conjecture.

C 1.3. For any integer k ≥ 3, there are only ﬁnitely many near-perfect
numbers with k distinct prime factors.

2. Preliminary lemmas

To prove Theorem 1.2, we ﬁrst give the following two lemmas.

L 2.1. If n = 2
αq is a near-perfect number with redundant divisor d = 2sq, where
q is an odd prime, then either n = 40 or n is of type 2.

P. Since n = 2αq is a near-perfect number with redundant divisor d = 2sq, it
follows that (2
α+1 − 1)(q + 1) = 2
α+1q + 2sq. That is, (2s + 1)q = 2
α+1 − 1. This
implies that s ≥ 1.
Let k and r be two integers with 0 ≤ r ≤ s − 1 such that α + 1 = ks + r. Then

2α+1 − 1 ≡ 2ks+r − 1 ≡ (−1)k2
r − 1 (mod 2s + 1).

https://doi.org/10.1017/S0004972713000178 Published online by Cambridge University Press

522 X.-Z. Ren and Y.-G. Chen [3]

Since (2s + 1)q = 2α+1 − 1, it follows that 2s + 1 | (−1)
k2r − 1. Thus, by

|(−1)k2
r − 1| ≤ 2r + 1 < 2s + 1,

we have (−1)k2
r − 1 = 0. This implies that k is even and r = 0. Let k = 2m. Thus, by
(2s + 1)q = 2α+1 − 1 = 22sm − 1,
 q = (2s − 1) 2
2sm − 1
22s − 1 .

Since q is an odd prime, it follows that either 2s − 1 = 1 or 2
2sm − 1 = 22s − 1. Thus,
either s = 1 or m = 1.
If s = 1, then α + 1 = 2m. Thus (2s + 1)q = 2
α+1 − 1 becomes 3q = (2
m − 1) ×
(2m + 1). Since (2m − 1, 2
m + 1) = 1 and q ≥ 3, it follows that m = 2, q = 5 and α = 3.
Thus n = 40.
If m = 1, then q = 2s − 1 is an odd prime and α = 2s − 1. Hence n = 22s−1(2s − 1) is
of type 2.
This completes the proof of Lemma 2.1. □

L 2.2. Let q be an odd prime, α and β positive integers with β ≥ 2. If n = 2
αq
β is
a near-perfect number with redundant divisor d, then q
β ∤ d.

P. Suppose that d = 2sqβ with 0 ≤ s ≤ α − 1. We will derive a contradiction.
Since σ(n) = 2n + d, it follows that

(2α+1 − 1)(1 + q + · · · + qβ) = (2α+1 + 2s)q
β. (2.1)

If β is even, then 1 + q + · · · + q
β is odd. Thus s = 0. Since

(2α+1 − 1, 2α+1 + 1) = 1, (1 + q + · · · + qβ, qβ) = 1,

it follows from (2.1) that

2α+1 − 1 = qβ, 1 + q + · · · + q
β = 2α+1 + 1.

Thus 2
α+1 + 1 = 2
α+1 − 1 + 2 = q
β + 2 < 1 + q + · · · + q
β = 2
α+1 + 1,

a contradiction.
Now we assume that β is odd. Then the left-hand side of (2.1) is even. Thus s ≥ 1.
From (2.1), 2s | 1 + q + · · · + q
β (2.2)

and (2α+1 − 1)(1 + q + · · · + q
β−1) = (2s + 1)q
β. (2.3)

By (2.3) and (q
β, 1 + q + · · · + qβ−1) = 1,

1 + q + · · · + qβ−1 | 2s + 1. (2.4)

We distinguish two cases according to the value of β.

https://doi.org/10.1017/S0004972713000178 Published online by Cambridge University Press

[4] On near-perfect numbers with two distinct prime factors 523

Case 1: β ≡ 1 (mod 4). Since

1 + q + · · · + qβ = (1 + q)(1 + q
2 + q
4 + · · · + q
β−1)

and
 1 + q
2 + q
4 + · · · + q
β−1 ≡ β + 1
2 . 0 (mod 2),

it follows from (2.2) that 2s | 1 + q. Thus, by β ≥ 3, we have 2s + 1 ≤ q + 2 < 1 + q +
· · · + q
β−1, a contradiction with (2.4).

Case 2: β ≡ 3 (mod 4). Since

1 + q + · · · + q
β = (1 + q
2)(1 + q + q
4 + q
5 + · · · + q
β−3 + q
β−2)

and 4 ∤ 1 + q
2, it follows from (2.2) that 2s−1 | 1 + q + q
4 + q
5 + · · · + q
β−3 + q
β−2.
Thus, by (2.4) and β ≥ 3,

q2s−1 ≤ q(1 + q + q4 + q5 + · · · + qβ−3 + qβ−2) ≤ 2s + 1 − 1 = 2s,

a contradiction with q being an odd prime. This completes the proof of Lemma 2.2. □

3. Proof of Theorem 1.2

Let n = p
αq
β be a near-perfect number with redundant divisor d, where p and q
are two primes with p < q, and α, β are two positive integers. Then σ(n) = 2n + d. If
p ≥ 3, then

σ(n) = pα+1 − 1
p − 1 q
β+1 − 1
q − 1 < p
α+1

p − 1 qβ+1

q − 1 = n p
p − 1 q
q − 1 ≤ 3 × 5
2 × 4 n < 2n.

Hence p = 2. Let d = 2sq
t with 0 ≤ s ≤ α and 0 ≤ t ≤ β. Thus, σ(n) = 2n + d becomes

(2α+1 − 1)(1 + q + · · · + qβ) = 2α+1qβ + 2sq
t. (3.1)

We distinguish three cases according to the value of β.

Case 1: β = 1. Then t ∈ {0, 1}. If t = 0, then, by (3.1), q = 2
α+1 − 2s − 1 is an odd
prime and d = 2s. Thus n = 2
α(2α+1 − 2s − 1) is of type 1. If t = 1, then n = 2αq is a
near-perfect number with redundant divisor d = 2sq. By Lemma 2.1, either n = 40 or
n is of type 2.

Case 2: β = 2. By Lemma 2.2, q2 ∤ d. Thus t ∈ {0, 1}. By (3.1), s = 0. If
t = 0, then, by (3.1), (2α+1 − q)(1 + q) = 2, a contradiction. Hence t = 1. By (3.1),
q = 2α+1 − 1 is an odd prime. Therefore, n = 2
α(2α+1 − 1)2 is of type 3.

https://doi.org/10.1017/S0004972713000178 Published online by Cambridge University Press

524 X.-Z. Ren and Y.-G. Chen [5]

Case 3: β ≥ 3. By Lemma 2.2, 0 ≤ t ≤ β − 1. The equality (3.1) can be rewritten
as (2α+1 − q)(1 + q + · · · + qβ−1) = 1 + 2sqt. (3.2)

If q < 2
α, then the left-hand side of (3.2) is more than 2α(1 + q + · · · + q
β−1). Noting
that β ≥ 3, the right-hand side of (3.2) does not exceed 1 + 2
αqβ−1 < 2α(1 + q + · · · +
qβ−1), a contradiction. Hence q ≥ 2
α. Since the left-hand side of (3.2) is at least

1 + q + · · · + qβ−1 > 1 + q
2 ≥ 1 + 2
αq ≥ 1 + 2sq,

we have t ≥ 2. By (3.1), q | 2
α+1 − 1, a contradiction with q ≥ 2α.

This completes the proof of Theorem 1.2.

Acknowledgements

We are grateful to the referee for helpful comments and the editor for suggesting
that we give a list of some known near-perfect numbers.

References

[1] R. Crandall and C. Pomerance, Prime Numbers: A Computational Perspective, 2nd edn (Springer,
New York, 2005).
[2] P. Pollack and V. Shevelev, ‘On perfect and near-perfect numbers’, J. Number Theory 132 (2012),
3037–3046.
[3] N. J. Sloane, ‘The online encyclopedia of integer sequences’, available at http://oeis.org/.

XIAO-ZHI REN, School of Mathematical Sciences and Institute of Mathematics,
Nanjing Normal University, Nanjing 210023, PR China

YONG-GAO CHEN, School of Mathematical Sciences and Institute of Mathematics,
Nanjing Normal University, Nanjing 210023, PR China
e-mail: ygchen@njnu.edu.cn

https://doi.org/10.1017/S0004972713000178 Published online by Cambridge University Press
