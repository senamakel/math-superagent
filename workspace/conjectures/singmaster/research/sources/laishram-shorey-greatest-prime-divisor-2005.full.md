<!-- source: https://www.isid.ac.in/~shanta/PAPERS/ActaPCons.pdf | converted from PDF -->

THE GREATEST PRIME DIVISOR OF A PRODUCT
OF CONSECUTIVE INTEGERS

SHANTA LAISHRAM AND T. N. SHOREY

1. Introduction

Let k ≥ 2 and n ≥ 1 be integers. We denote by

∆(n, k) = n(n + 1) · · · (n + k − 1).

For an integer ν > 1, we denote by ω(ν) and P (ν) the number
of distinct prime divisors of ν and the greatest prime factor of ν,
respectively, and we put ω(1) = 0, P (1) = 1.
A well known theorem of Sylvester [7] states that

P (∆(n, k)) > k if n > k.(1)

We observe that P (∆(1, k)) ≤ k and therefore, the assumption
n > k in (1) cannot be removed. For n > k, Moser [5] sharpened
(1) to P (∆(n, k)) > 11
10k and Hanson [3] to P (∆(n, k)) > 1.5k
unless (n, k) = (3, 2), (8, 2), (6, 5). Further Faulkner [2] proved that
P (∆(n, k)) > 2k if n is greater than or equal to the least prime
exceeding 2k and (n, k) ̸= (8, 2), (8, 3). In this paper, we sharpen
the results of Hanson and Faulkner. We shall not use these results
in the proofs of our improvements. We prove

Theorem 1. We have
(a)
 P (∆(n, k)) > 2k for n > max(k + 13, 279
262k).(2)

(b)
 P (∆(n, k)) > 1.97k for n > k + 13.(3)

We observe that 1.97 in (3) cannot be replaced by 2 since there
are arbitrary long chains of consecutive composite positive integers.
The same reason implies that Theorem 1 (a) is not valid under
the assumption n > k + 13. Further the assumption n > 279
262k in
Theorem 1 (a) is necessary since P (∆(279, 262)) ≤ 2 × 262.

2000 Mathematics Subject Classiﬁcation: Primary 11A41, 11N05, 11N13.
Keywords: Arithmetic Progressions, Primes.
1

2 SHANTA LAISHRAM AND T. N. SHOREY

Now we give a lower bound for P (∆(n, k)) > 2k which is valid
for n > k > 2 except for an explicitly given ﬁnite set. For this, we
need some notation. For a pair (n, k) and a positive integer h, we
write [n, k, h] for the set of all pairs (n, k), · · · (n + h − 1, k) and we
set [n, k] = [n, k, 1] = {(n, k)}. Let

A10 = {58}; A8 = A10 ∪ {59}; A6 = A8 ∪ {60};

A4 = A6 ∪ {12, 16, 46, 61, 72, 93, 103, 109, 151, 163};

A2 = A4 ∪ {4, 7, 10, 13, 17, 19, 25, 28, 32, 38, 43, 47, 62, 73, 94, 104, 110, 124, 152, 164, 269}

and A2i+1 = A2i for 1 ≤ i ≤ 5. Further let
A1 = A2 ∪ {3, 5, 6, 8, 9, 11, 14, 15, 18, 20, 23, 26, 29, 33, 35, 39, 41, 44, 48, 50, 53,

56, 63, 68, 74, 78, 81, 86, 89, 95, 105, 111, 125, 146, 153, 165, 173, 270}.

Finally we denote B as the union of the sets [8, 3], [5, 4, 3], [14, 13, 3]
and {(k + 1, k)|k = 3, 5, 8, 11, 14, 18, 63}. Then

Theorem 2. We have

P (∆(n, k)) > 1.95k for n > k > 2(4)

unless and only unless (n, k) ∈ [k + 1, k, h] for k ∈ Ah with 1 ≤ h ≤
11 or (n, k) = (8, 3).

If k = 2, we observe (see Lemma 7) that P (∆(n, k)) > 2k unless
n = 3, 8 and that P (∆(3, 2)) = P (∆(8, 2)) = 3. Thus the estimate
(4) is valid for k = 2 whenever n ̸= 3, 8. We observe that P (∆(k +
1, k)) ≤ 2k and therefore, 1.95 in (4) cannot be replaced by 2.
There are few exceptions if 1.95 is replaced by 1.8 in Theorem 2.
We derive from Theorem 2 the following result.

Corollary 1. We have

P (∆(n, k)) > 1.8k for n > k > 2(5)

unless and only unless (n, k) ∈ B.

2. Lemmas

We begin with a well known result due to Levi ben Gerson on a
particular case of Catalan equation.

Lemma 1. The solutions of

2
a − 3
b = ±1 in integers a > 0, b > 0

are given by (a, b) = (1, 1), (2, 1), (3, 2).

Next we state a result of Saradha and Shorey [6] on a lower bound
for ω(∆(n, k)).

THE GREATEST PRIME DIVISOR OF CONSECUTIVE INTEGERS 3

Lemma 2. For n > k > 2, we have

ω(∆(n, k)) ≥ π(k) + [1
3 π(k)
] + 2

unless and only unless (n, k) belongs to the union of sets




[4, 3], [6, 3, 3], [16, 3], [6, 4], [6, 5, 4], [12, 5], [14, 5, 3], [23, 5, 2],
[7, 6, 2], [15, 6], [8, 7, 3], [12, 7], [14, 7, 2], [24, 7], [9, 8], [14, 8],
[14, 13, 3], [18, 13], [20, 13, 2], [24, 13], [15, 14], [20, 14], [20, 17].

We shall use Lemma 2 only when k = 3 or 5 ≤ k ≤ 8. Let pi
denote the i−th prime number. Then

Lemma 3. We have

pi+1 − pi <
 



35 for pi ≤ 5591
15 for pi ≤ 1123, pi ̸= 523, 887, 1069
21 for pi = 523, 887, 1069
9 for pi ≤ 361, pi ̸= 113, 139, 181, 199, 211, 241, 283, 293, 317, 337.

(6)

Lemma 4. Let N be a positive real number and k0 a positive inte-
ger. Let I(N, k0) = {i|pi+1 − pi ≥ k0, pi ≤ N}. Then

P (n(n + 1) · · · (n + k − 1)) > 2k

for 2k ≤ n < N and k ≥ k0 except possibly when pi < n < n + k −
1 < pi+1 for i ∈ I(N, k0).

Proof. Let 2k ≤ n < N and k > k0. We may suppose that none of
n, n + 1, · · · , n + k − 1 is a prime, otherwise the result follows. Let
pi < n < n + k − 1 < pi+1. Then i = π(n) and pπ(n) < n < N. For
π(n) /∈ I(N, k0), we have

k − 1 = n + k − 1 − n < pπ(n)+1 − pπ(n) < k0

which implies k − 1 < k0 − 1, a contradiction. Hence the assertion.
□

The following result is on the estimates for primes due to Dusart
[1, p.14].

Lemma 5. For ν > 1, we have

(i) π(ν) ≤ ν
log ν
 (
1 + 1.2762
log ν
 )

(ii) π(ν) ≥ ν
log ν − 1 for ν ≥ 5393.

4 SHANTA LAISHRAM AND T. N. SHOREY

Lemma 6. Let X > 0 and 0 < θ < e − 1 be real numbers. For
l ≥ 0, let

X0 = max ( 5393
1 + θ , exp(log(1 + θ) + 0.2762
θ )
) ,

Xl+1 = max
 ( 5393
1 + θ , exp(log(1 + θ) + 0.2762)

θ + 1.2762(1−log(1+θ))
log2 Xl )

)
 .

Then we have
 π((1 + θ)X) − π(X) > 0

for X > Xl.

Proof. Let l ≥ 0 and X > Xl. Then (1 + θ)X ≥ 5393. By Lemma
5, we have

δ := π((1 + θ)X) − π(X) ≥ (1 + θ)X
log(1 + θ)X − 1 − X
log X
 (
1 + 1.2762
log X
 )

≥ X
log(1 + θ)X − 1
 {
1 + θ − log(1 + θ)X − 1
log X
 (
1 + 1.2762
log X
 )}

≥ X
log(1 + θ)X − 1
 {
1 + θ − (1 − 1 − log(1 + θ)
log X
 ) (
1 + 1.2762
log X
 )}

≥ X
log(1 + θ)X − 1 {F (X) + G(X)}

where F (X) = θ − log(1+θ)+0.2762
log X and G(X) = 1.2762(1−log(1+θ))
log2 X . We
see that G(X) > 0 and decreasing since 0 < θ < e − 1. Further
we observe that {Xi} is a non-increasing sequence. We notice that
δ > 0 if F (X) + G(X) > 0. But F (X) + G(X) > F (X) > 0 for
X > X0 by the deﬁnition of X0. Thus δ > 0 for X > X0. Let X ≤
X0. Then F (X) + G(X) ≥ F (X) + G(X0) and F (X) + G(X0) > 0
if X > X1 by the deﬁnition of X1. Hence δ > 0 for X > X1. Now
we proceed inductively as above to see that δ > 0 for X > Xl with
l ≥ 2. □

Lemma 7. Let n > k and k ≤ 16. Then

P (∆(n, k)) ≤ 2k(7)

implies that (n, k) ∈ {(8, 2), (8, 3)} or (n, k) ∈ [k + 1, k] for k ∈
{2, 3, 5, 6, 8, 9, 11, 14, 15} or (n, k) ∈ [k+1, k, 3] for k ∈ {4, 7, 10, 13}
or (n, k) ∈ [k + 1, k, 5] for k ∈ {12, 16}.

THE GREATEST PRIME DIVISOR OF CONSECUTIVE INTEGERS 5

Proof. We apply Lemma 1 to derive that (7) is possible only if
n = 3, 8 when k = 2 and n = 5, 6, 7 when k = 4. For the latter
assertion, we apply Lemma 1 after securing P ((n + i)(n + j)) ≤ 3
with 0 ≤ i < j ≤ 3 by deleting the terms divisible by 5 and 7 in
n, n + 1, n + 2 and n + 3. For k = 3 and 5 ≤ k ≤ 8, the assertion
follows from Lemma 2.
Thus we may assume that k ≥ 9. Assume that (7) holds. Then
there are at most 1 + [ k−1
p ] terms divisible by the prime p. After
removing all the terms divisible by p ≥ 7, we are left with at least
4 terms only divisible by 2, 3 and 5. Further out of these terms,
for each prime 2, 3 and 5, we remove a term in which the prime
divides to a maximal power. Then we are left with a term n + i
such that n ≤ n + i ≤ 8 × 9 × 5 = 360. Let n ≥ 2k. We now apply
Lemma 4 with N = 361, k0 = 9 and (6) to get P (∆(n, k)) > 2k
for k ≥ 9 except possibly when pi < n < n + k − 1 < pi+1, pi =
113, 139, 181, 199, 211, 241, 283, 293, 317, 337. For these values of n,
we check that P (∆(n, k)) > 2k is valid for 9 ≤ k ≤ 16. Thus it
suﬃces to consider k < n < 2k. We calculate P (∆(n, k)) for (n, k)
with 9 ≤ k ≤ 16 and k < n < 2k. We ﬁnd that (7) holds only if
(n, k) is given in the statement of the Lemma 7. □

3. Proof of Theorem 1 (a)

Let n > max(k + 13, 279
262k). In view of Lemma 7, we may take
k ≥ 17 since n ≤ k + 5 for the exceptions (n, k) given in Lemma 7.
It suﬃces to prove (2) for k such that 2k − 1 is prime. Let k1 < k2
be such that 2k1 − 1 and 2k2 − 1 are consecutive primes. Suppose
(2) holds at k1. Then for k1 < k < k2, we have

P (n(n + 1) · · · (n + k − 1)) ≥ P (n · · · (n + k1 − 1)) > 2k1

implying P (∆(n, k)) ≥ 2k2 − 1 > 2k. Therefore we may suppose
that k ≥ 19 since 2k −1 with k = 17, 18 are composites. We assume
from now onward in the proof of Theorem 1 (a) that 2k−1 is prime.
We put x = n + k − 1. Then ∆(n, k) = x(x − 1) · · · (x − k + 1). Let
f1 < f2 < · · · < fµ be all the integers in [0, k) such that

P ((x − f1) · · · (x − fµ)) ≤ k.(8)

We derive as in the proof of [4, Lemma 4] to get

k! > x
µ−π(k) (1 − k
x
 )µ .(9)

6 SHANTA LAISHRAM AND T. N. SHOREY

We may suppose ω(∆(n, k)) ≤ π(2k) otherwise (2) follows. Then

µ ≥ k − π(2k) + π(k)(10)

which we use as in [4, Lemma 4] to derive from (9) that

x < k 3
2 for k ≥ 87; x < k 7
4 for k ≥ 40; x < k2 for k ≥ 19.(11)

If x ≥ 7k and k > 57, then we derive as in [4, Lemma 7] from
(10) that x ≥ k 3
2 . Thus we get from (11) that x < 7k for k ≥ 87.
Putting back n = x − k + 1, we may assume that n < 6k + 1 for
k ≥ 87, n < k 7
4 − k + 1 for 40 ≤ k < 87 and n < k2 − k + 1 for
19 ≤ k < 40.
Let k < 87. Suppose n ≥ 2k. Then 2k ≤ n < k 7
4 − k + 1 for
40 ≤ k < 87 and 2k ≤ n < k2 −k +1 for 19 ≤ k < 40. Thus Lemma
4 with N = 87 7
4 − 87 + 1, k0 = 35 and (6) implies that P (∆(n, k)) >
2k for k ≥ 35. We note here that 2k ≤ n < N for 35 ≤ k < 40.
Let k < 35. Taking N = 34
2 − 34 + 1, k0 = 21 for 21 ≤ k ≤ 34 and
N = 19
2 − 19 + 1, k0 = 19 for k = 19, we see from Lemma 4 and (6)
that P (∆(n, k)) > 2k for k ≥ 19. Here the case k = 20 is excluded
since 2k − 1 is composite. Therefore we may assume that n < 2k.
Further we observe that π(n + k − 1) − π(2k) ≥ π(2k + 13) − π(2k)
since n > k + 13. Next we check that π(2k + 13) − π(2k) > 0. This
implies that [2k, n + k − 1] contains a prime.
Thus we may assume that k ≥ 87. Then we write n = αk + 1
with 279
262 − 1
k < α ≤ 6 if k ≥ 201 and 1 + 12
k < α ≤ 6 if k < 201.
Further we consider π(n + k − 1) − π(max(n − 1, 2k)) which is

= π((α + 1)k) − π(αk) for α ≥ 2

≥ π([541
262k]) − π(2k) for α < 2 and k ≥ 201

≥ π(2k + 13) − π(2k) for α < 2 and k < 201.

We check by using exact values of π function that π(2k + 13) −
π(2k) > 0 for k < 201 and π([ 541
262k])−π(2k) > 0 for 201 ≤ k ≤ 2616.
Thus we may suppose that k > 2616 if α < 2. Also [ 541
262k] ≥ 540
262k
for k > 2616. Now we apply Lemma 6 with X = αk, θ = 1
α, l = 0
if α ≥ 2 and X = 2k, θ = 4
131, l = 1 if α < 2 to get π(n + k −
1) − π(max(n − 1, 2k)) > 0 for X > X0 = 5393
1+ 1
α if α ≥ 2 and

X > X1 = 5393
1+ 4
131 if α < 2. Further when α < 2, we observe that
X = 2k > X1 since k > 2616. Thus the assertion follows for n < 2k.
It remains to consider the case α ≥ 2 and X ≤ 5393(1+ 1
α )
−1. Then
2k ≤ n < n+k−1 = X(1+ 1
α ) ≤ 5393. Now we apply Lemma 4 with
N = 5393, k0 = 35 and (6) to conclude that P (∆(n, k)) > 2k. □

THE GREATEST PRIME DIVISOR OF CONSECUTIVE INTEGERS 7

4. Proof of Theorem 1 (b)

In view of Lemma 7 and Theorem 1 (a), we may assume that
k ≥ 17 and k < n ≤ 279
262k. Let X = 279
262k, θ = 245
279, l = 0. Then for
k < n ≤ X, we see from Lemma 6 that

π(2k) − π(n − 1) ≥ π((1 + θ)X) − π(X) > 0

for X > X0 = 5393(1 + θ)
−1 which is satisﬁed for k > 2696 since
(1 + θ)X = 2k. Thus we may suppose that k ≤ 2696. Now we
check with exact values of π function that π(2k) − π( 279
262k) > 0.
Therefore P (∆(n, k)) ≥ P (n(n + 1) · · · 2k) ≥ pπ(2k). Further we
apply Lemma 6 with X = 1.97k, θ = 3
197 and l = 25. We calculate
that Xl ≤ 284000. We conclude by Lemma 6 that

π(2k) − π(1.97k) = π((1 + θ)X) − π(X) > 0

for k > 145000. Let k ≤ 145000. Then we check that π(2k) −
π(1.97k) > 0 is valid for k ≥ 680 by using the exact values of π
function. Thus
 pπ(2k) > 1.97k for k ≥ 680.(12)

Therefore we may suppose that k < 680. Now we observe that for
n > k +13, π(n + k − 1) − π(1.97k) ≥ π(2k +13) − π(1.97k) > 0, the
latter inequality can be checked by using exact values of π function.
Hence the assertion follows since n < 1.97k. □

5. Proof of Theorem 2

By Theorem 1 (b), we may assume that n ≤ k + 13. Also we may
suppose that k < 680 by (12). For k ≤ 16, we calculate P (∆(n, k))
for all the pairs (n, k) given in the statement of Lemma 7. We ﬁnd
that either P (∆(n, k)) > 1.95k or (n, k) is an exception stated in
Theorem 1 (a). Thus we may suppose that k ≥ 17. Now we check
that π(n + k − 1) − π(1.95k) > 0 except for (n, k) ∈ [k + 1, k, h] for
k ∈ Ah with 1 ≤ h ≤ 11 and the assertion follows. □

6. Proof of Corollary 1

We calculate P (∆(n, k)) for all (n, k) with k ≤ 270 and k + 1 ≤
n ≤ k + 11. This contains the set of exceptions given in Theorem
2. We ﬁnd that P (∆(n, k)) > 1.8k unless (n, k) ∈ B. Hence the
assertion (5) follows from Theorem 2. □

8 SHANTA LAISHRAM AND T. N. SHOREY

References

[1] Pierre Dusart, Autour de la fonction qui compte le nombre de nombres
premiers, Ph.D thesis, Universit´e de Limoges, 1998.
[2] M. Faulkner, On a theorem of Sylvester and Schur, J. Lond. Math. Soc.,
41 (1966), 107-110.
[3] D. Hanson, On a theorem of Sylvester and Schur, Canad. Math. Bull.,
16 (1973), 195-199.
[4] S. Laishram and T. N. Shorey, Number of prime divisors in a product of
consecutive integers, Acta Arith. 113 (2004), 327-341.
[5] L. Moser, Insolvability of (2n
n ) = (2a
a )(2b
b ), Canad. Math. Bull.(2), 6
(1963), 167-169.
[6] N. Saradha and T. N. Shorey, Almost squares and factorisations in con-
secutive integers, Compositio Math. 138 (2003), 113-124.
[7] J. J. Sylvester, On arithmetical series, Messenger of Mathematics, XXI
(1892), 1-19, 87-120, and Mathematical Papers, 4(1912), 687-731.

School of Mathematics, Tata Institute of Fundamental Research,
Homi Bhabha Road, Mumbai 400005, India
E-mail address: shanta@math.tifr.res.in
E-mail address: shorey@math.tifr.res.in
