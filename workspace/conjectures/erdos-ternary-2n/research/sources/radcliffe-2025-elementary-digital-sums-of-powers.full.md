<!-- source: https://arxiv.org/pdf/2511.15850 | converted from PDF -->

ELEMENTARY BOUNDS ON DIGITAL SUMS OF POWERS,
FACTORIALS, AND LCMS

DAVID G. RADCLIFFE

Abstract. We prove logarithmic lower bounds on digital sums of powers, multi-
ples of powers, factorials, and the least common multiple of {1, . . . , n}, using only
elementary number theory. We conclude with an expository proof of Stewart’s
theorem on digital sums of powers, which uses Baker’s theorem on linear forms in
logarithms.
 1. Introduction

In this expository article, we prove lower bounds on digital sums of powers, multi-
ples of powers, factorials, and the least common multiple of {1, . . . , n}, using only
elementary number theory.

We were inspired by the following problem, which was posed and solved by Wac law
Sierpi´nski [9, Problem 209]:

Prove that the sum of digits of the number 2
n (in decimal system)
increases to infinity with n.

The reader is urged to attempt this problem independently before proceeding. Note
that it is not enough to prove that the sum of digits of 2
n is unbounded, since the
sequence is not monotonic.

Consider the sequence of powers of 2 (sequence A000079 in the On-Line Encyclopedia
of Integer Sequences):

1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, . . .

This sequence grows very rapidly. Now define another sequence by summing the
decimal digits of each term. For example, 16 becomes 1 + 6 = 7, and 32 becomes
3 + 2 = 5. The first few terms of this new sequence (A001370) are listed below:

Date: January 9, 2026. 1arXiv:2511.15850v2  [math.NT]  7 Jan 2026
2 DAVID G. RADCLIFFE

Figure 1. Scatter plot of the digital sum of 2
n for n ≤ 100 together
with the heuristic linear approximation.

1, 2, 4, 8, 7, 5, 10, 11, 13, 8, 7, . . .

This sequence of digital sums grows much more slowly and is not monotonic. Nev-
ertheless, it is reasonable to conjecture that it tends to infinity. Indeed, one might
guess that the sum of the decimal digits of 2
n is approximately 4.5 n log10 2, since 2n

has ⌊n log10 2⌋ + 1 decimal digits, and the digits seem to be approximately uniformly
distributed among 0, 1, 2, . . . , 9. However, this stronger conjecture remains unproved.
See Figure 1.

In Section 3, we prove that the digital sum of 2
n is greater than log4 n for all n ≥ 1.
Before doing so, we review the relevant notation and terminology.

2. Notation and terminology

For integers N ≥ 0 and b ≥ 2, the base-b expansion of N is the unique representation
of the form
 N =
 ∞∑

i=0 dibi, di ∈ {0, 1, . . . , b − 1}.

The integers di are the base-b digits of N ; all but finitely many of these digits are
zero. When b = 10, this is called the decimal expansion.

ELEMENTARY BOUNDS ON DIGITAL SUMS OF POWERS, FACTORIALS, AND LCMS 3

For an integer b ≥ 2, we write sb(N ) for the sum of the base-b digits of N , and cb(N )
for the number of nonzero digits in that expansion. These functions are equivalent
up to a constant factor, since cb(N ) ≤ sb(N ) ≤ (b − 1)cb(N ) for all N and b; so we
focus on cb(N ).

The function sb is subadditive: sb(M + N ) ≤ sb(M ) + sb(N ) for all nonnegative
integers M and N . Equality holds if no carries occur in the digitwise addition of M
and N . Otherwise, each carry reduces the digital sum by b − 1. The function cb is
likewise subadditive.

For a prime p, the p-adic valuation of N , denoted νp(N ), is the exponent of p in the
prime factorization of N . If p does not divide N then νp(N ) = 0. The function νp is
completely additive: νp(M N ) = νp(M ) + νp(N ) for all positive integers M and N .

We use asymptotic notation to describe the approximate size of functions [3]. Let f
and g be real-valued functions defined on a domain D. One writes f (n) = O(g(n))
if there exists a positive real number C such that

|f (n)| ≤ Cg(n) for all n ∈ D.

In particular, O(1) denotes a bounded function.

The notation f (n) ≍ g(n) means that there exist positive real numbers C and C ′

such that Cg(n) ≤ |f (n)| ≤ C ′g(n) for all n ∈ D.

3. Digital sums of powers of two

We present an informal proof that c10(2n), the number of nonzero digits in the decimal
expansion of 2
n, tends to infinity as n → ∞. See [6] for an alternative approach.

Let n be a positive integer, and write the decimal expansion of 2
n as

2
n =
 ∞∑

i=0 di10
i,

where each di ∈ {0, . . . , 9} and all but finitely many di are zero. Since 2
n is not
divisible by 10, its final digit d0 is nonzero.

Assume first that n ≥ 4. Then 2
n is divisible by 24 = 16. Consider the last four
digits of 2
n, that is, 2
n mod 10
4.
This number is divisible by 16. If the digits d1, d2, d3 were all zero, then this remainder
would be less than 10, and hence could not be divisible by 16. Therefore, at least
one of the digits d1, d2, d3 is nonzero.

4 DAVID G. RADCLIFFE

2
0 = 1
2
4 = 1 6
2
14 = 1 638 4
2
47 = 1 4073748835 532 8
2
157 = 1 826877046663628647754606040895353 7745699156 787 2

Figure 2. Decimal digits of 2
n, separated into blocks. Each block
contributes at least one nonzero digit.

Now assume n ≥ 14. Then 2n is divisible by 2
14. Since 2
14 > 104, any positive
number divisible by 214 must be at least 104. Thus, the last 14 digits of 2
n,

2
n mod 10
14,

cannot be less than 104. If the digits d4, d5, . . . , d13 were all zero, this remainder
would be less than 104, which is impossible. Hence, at least one digit in this block is
nonzero.

Continuing in this way, as n increases, we obtain more blocks of decimal digits, each
containing at least one nonzero digit. These blocks are disjoint, and the number of
such blocks grows without bound as n → ∞.

Therefore, the number of nonzero decimal digits of 2
n tends to infinity as n → ∞.
See Figure 2.

Let us formalize this argument.

Theorem 1. Let (ek) be a sequence of integers such that e1 ≥ 1 and 2ek > 10ek−1
for all k ≥ 2. Suppose that N is divisible by 2
ek but not by 10. Then c10(N ) ≥ k.

Proof. We argue by induction on k. The case k = 1 is immediate, since any positive
integer has at least one nonzero digit.

Assume now that k ≥ 2, and that the statement holds for k − 1. Apply the division
algorithm to write N = 10
ek−1q + r, 0 ≤ r < 10
ek−1,
for integers q, r.

Because N ≥ 2ek > 10
ek−1 by hypothesis, the quotient satisfies q ≥ 1.

Next, both N and 10
ek−1q are divisible by 2ek−1, hence their difference

r = N − 10ek−1q

is also divisible by 2ek−1.

ELEMENTARY BOUNDS ON DIGITAL SUMS OF POWERS, FACTORIALS, AND LCMS 5

Moreover, r is not divisible by 10, since 10ek−1q is divisible by 10 and N is not.

Therefore, c10(r) ≥ k − 1 by the induction hypothesis.

Finally, the decimal expansion of N is obtained by concatenating the decimal expan-
sion of q with the (possibly zero-padded) expansion of r. Thus,

c10(N ) = c10(q) + c10(r) ≥ 1 + (k − 1) = k.

This completes the proof. □

We now apply Theorem 1 to obtain our desired lower bound.

Corollary 1. Let a be a positive integer that is divisible by 2 but not divisible by 10.
Then c10(a
n) ≥ log4 n for all n > 1.

Proof. Let ek = 4k−1 for k ≥ 1. This sequence satisfies e1 ≥ 1 and 2
ek > 10ek−1 for
all k ≥ 2.

Let n > 1 and k = ⌈log4 n⌉, so that 4
k−1 < n ≤ 4k. Then an is divisible by 2
n, so a
n

is also divisible by 2ek. Moreover, a
n is not divisible by 10.

Therefore, c10(a
n) ≥ k ≥ log4 n by Theorem 1. □

A similar argument applies if a is divisible by 5 but not divisible by 10, or more
generally, if the prime factorization of a contains unequal numbers of twos and fives.
In the next section, we generalize this insight to non-decimal base expansions.

4. Digital sums of powers in other bases

In this section, we prove a logarithmic lower bound for cb(an). The first step (The-
orem 2 below) generalizes the corresponding base-10 argument from the previous
section.

Theorem 2. Let 2 ≤ a < b be integers with a | b. Let (ek) be a sequence of integers
such that e1 ≥ 1 and a
ek > b
ek−1 for all k ≥ 2. Suppose that N is divisible by aek but
not by b. Then cb(N ) ≥ k.

Proof. In the proof of Theorem 1, replace 2 with a and 10 with b throughout. □

The conclusion of Theorem 2 can be converted into an explicit logarithmic lower
bound, as described below. A similar result was independently proved by Shreyansh
Jaiswal (private communication).

6 DAVID G. RADCLIFFE

Theorem 3. Let 2 ≤ a < b be integers with a | b. Suppose that N is divisible by an

but not b. Then there exists C > 0, depending only on a and b, such that

cb(N ) > C log n

for n sufficiently large. Moreover, any constant 0 < C < (log(log(b)/ log(a)))
−1 is
admissible.

Proof. Let r = log(b)/ log(a), and define (ek) by e1 = 1 and ek = ⌈rek−1⌉ for k ≥ 2.
It is routine to verify that (ek) satisfies the conditions of Theorem 2.

By the definition of (ek), we have
 e2 < r + 1,

e3 < r2 + r + 1,

and in general,

(1) ek <
 k−1∑

i=0 ri < rk

r − 1.

Fix an integer n ≥ r/(r − 1), and let

k = ⌊ log((r − 1)n)
log r
 ⌋ .

Then
 1 ≤ k ≤ log((r − 1)n)
log r ,

which implies that
 n ≥ rk

r − 1.

Therefore n > ek by (1), hence cb(N ) ≥ k by Theorem 2.

Since ⌊ log((r − 1)n)
log r
 ⌋ = log n
log r + O(1),

choosing any C < (log r)−1 gives
⌊ log((r − 1)n)
log r
 ⌋ > C log n

for n sufficiently large, which implies that cb(N ) > C log n. □

ELEMENTARY BOUNDS ON DIGITAL SUMS OF POWERS, FACTORIALS, AND LCMS 7

To handle the case where b | a
n, we require a lower bound on the p-adic valuation of
the remaining factor after removing powers of b. The following lemma provides such
a bound under an irrationality assumption.

Lemma 1. Let a, b ≥ 2 be integers such that log(a)/ log(b) is irrational. Suppose
that a
n = bmt, where t ≥ 1 is an integer. Then there exists a prime factor p of a,
and C > 0 depending only on a and b, such that νp(t) ≥ Cn.

Proof. Since log(a)/ log(b) is irrational, there are no integers u, v with av = b
u, except
u = v = 0. Equivalently, the vectors (νp(a))p and (νp(b))p are linearly independent,
so we can choose primes p and q such that

(2) νp(a)νq(b) − νq(a)νp(b) > 0.

By comparing the p- and q-adic valuations of a
n, we obtain

(3) nνp(a) = mνp(b) + νp(t)

and

(4) nνq(a) ≥ mνq(b).

Combining (3) and (4) yields

(5) νp(t) ≥ nνp(a) − n νq(a)
νq(b) νp(b) = Cn,

where
 C = νp(a)νq(b) − νq(a)νp(b)
νq(b) .

Finally, C > 0 by (2). □

We now come to the main result of this section.

Theorem 4. Let a, b ≥ 2 be integers. Let d be the smallest factor of a such that
gcd(a/d, b) = 1, and suppose that log(d)/ log(b) is irrational. Then cb(a
n) > C log n
for all sufficiently large n, where C > 0 depends only on a and b.

Proof. Write an = b
ms with b ∤ s, and set g = a/d. By the minimality of d, the prime
divisors of d are exactly those prime divisors of a that also divide b; in particular
gcd(d, g) = 1 and any prime p | d satisfies p | b.

Since gn | a
n and gcd(g, b) = 1, it follows that gn | s. Define t = s/gn; then dn = b
mt.

By Lemma 1, applied with a ← d, there exists a prime divisor p of d such that

νp(t) ≥ C ′n

8 DAVID G. RADCLIFFE

for some C ′ > 0 depending only on a and b.

Because gcd(d, g) = 1, the prime p does not divide g, and hence νp(s) = νp(t).
Therefore, by Theorem 3, applied with a ← p and N ← s,

cb(s) > C log n

for n sufficiently large.

Finally, cb(a
n) = cb(s) since s and an differ only by a power of b and thus have the
same base-b expansion up to trailing zeros.

Consequently, cb(a
n) > C log n for n sufficiently large. □

In 1973, Senge and Straus [8, Theorem 3] showed that for integers a ≥ 1 and b ≥ 2,

lim
n→∞ cb(a
n) = ∞ if and only if log a
log b is irrational.

However, their result does not yield any explicit lower bound.

Subsequently, Stewart [10, Theorem 2] proved that if log(a)/ log(b) is irrational then

cb(a
n) > log n
log log n + C − 1

for all n > 4, where C depends only on a and b. This bound is quite general
but grows slower than logarithmically. This result was extended to certain linear
recurrence sequences by Luca [4].

Remark. The arguments in this section apply equally to an and to any multiple of
an. But it can be shown that every 3n has a multiple of the form 10k + 8, which
has only two nonzero decimal digits. Thus, any approach that does not distinguish
an from its multiples cannot prove that c10(3
n) tends to infinity. We overcome this
limitation in Section 6.

5. Digital sums of factorials and LCMs

In this section, we prove logarithmic lower bounds for the base-b digital sums of n!
and Λn = lcm(1, . . . , n). In contrast with the situation for a
n, where prime-power
divisibility played a central role, the key feature for factorials and LCMs is that both
n! and Λn are divisible by large integers of the form br − 1.

The key insight is provided by the following lemma, which was originally proved by
Stolarsky [11] for base 2, and later extended to general bases by Balog and Dar-
tyge [1].

ELEMENTARY BOUNDS ON DIGITAL SUMS OF POWERS, FACTORIALS, AND LCMS 9

Lemma 2. Let m, r ≥ 1 and b ≥ 2 be integers. If m is divisible by b
r − 1 then
sb(m) ≥ (b − 1)r.

Proof. Write the base-b expansion of m as a concatenation of r-digit blocks, so that

m =
 k−1∑

i=0 Bibri, 0 ≤ Bi < b
r, Bk−1 ≥ 1.

Define the block sum operator G by

G(m) =
 k−1∑

i=0 Bi.

Observe that G(m) ≡ m (mod br − 1), since b
r ≡ 1 (mod b
r − 1). Also, G(m) < m
for m ≥ b
r, and G(m) = m for 0 ≤ m < b
r.

Iterate G on m: define m0 = m and mt+1 = G(mt). By the observations above, (mt)
is a sequence of positive multiples of br − 1 that is strictly decreasing while its terms
exceed b
r − 1. Therefore, the sequence must eventually reach br − 1, which is the
unique positive multiple of b
r − 1 that is less than b
r.

Since sb is subadditive,
 sb(G(m)) ≤
 k−1∑

i=0 sb(Bi) = sb(m).

Therefore, sb(m) ≥ sb(b
r − 1) = (b − 1)r. □

This lemma has an immediate consequence for factorials and least common multiples.
If n ≥ b
r − 1, then both n! and Λn are divisible by b
r − 1, and hence

sb(n!) ≥ (b − 1)r, sb(Λn) ≥ (b − 1)r.

Since one may choose r = ⌊logb(n + 1)⌋, this yields lower bounds of the form

sb(n!) > C log n, sb(Λn) > C log n

for some C > 0 depending only on b.

Luca [5] proved the same results using similar methods. In 2015, Sanna [7] used the
lemma above, together with more advanced methods, to prove that

sb(n!) > C log n log log log n

10 DAVID G. RADCLIFFE

Figure 3. Scatter plot of the digital sums of n! and Λn for n ≤ 100,
together with their heuristic approximations.

for all integers n > ee and all b ≥ 2, where C depends only on b. The same
estimate holds for sb(Λn). Our interest here is not to compete with the sharpest
known results, but rather to show that simple divisibility arguments already imply
logarithmic growth.

We conjecture that sb(n!) ≍ n log n and sb(Λn) ≍ n, based on the assumption that,
apart from trailing zeros, their digits are approximately uniformly distributed among
{0, 1, . . . , b − 1}. However, these conjectures remain unproved. See Figure 3.

6. Stewart’s Theorem

In this final section, we prove that the number of nonzero digits in the base-b ex-
pansion of a
n tends to infinity as n → ∞, provided that log(a)/ log(b) is irrational.
This result appears in earlier work of Senge and Straus [8] and Stewart [10], but we
present an argument that we hope is more accessible.

The irrationality condition is necessary. Indeed, if log(a)/ log(b) = r/s ∈ Q, then

ans = b
nr

for every integer n, so ans has only one nonzero digit in base b.

The following lemma permits us to disregard trailing zeros in the base-b expansion
of an.

ELEMENTARY BOUNDS ON DIGITAL SUMS OF POWERS, FACTORIALS, AND LCMS 11

Lemma 3. Let a, b ≥ 2 be integers with log(a)/ log(b) irrational. Then there exist
positive constants C and C ′, depending only on a and b, such that whenever

an = b
rt,

we have Cn ≤ log t ≤ C ′n.

In other words, log t ≍ n.

Proof. By Lemma 1, there exists a prime divisor p of a such that

νp(t) > C1n

holds for all n, where C1 > 0 depends only on a and b.

Therefore, t > p
C1n and hence
 log t > C1n log p.

On the other hand, t ≤ a
n hence log t ≤ n log a.

Therefore, Cn ≤ log t ≤ C ′n

holds for all n, where C = C1 log p and C ′ = log a. □

We require the following theorem, due to Baker and W¨ustholz [2], which we state
without proof.

Theorem 5. Let Λ = b1 log α1 + · · · + bn log αn,

where b1, . . . , bn are integers. Assume that α1, . . . , αn are algebraic numbers with
heights at most A1, . . . , An (all ≥ e) respectively and that their logarithms have their
principal values. Further assume that b1, . . . , bn have absolute values at most B (≥ e).
If Λ ̸= 0 then log |Λ| > −(16nd)
2(n+2) log A1 · · · log An log B,

where d denotes the degree of Q(α1, . . . , αn).

Recall that a nonzero algebraic number α ∈ C is a root of a unique irreducible integer
polynomial P with positive leading coefficient and coprime coefficients. The height
of α is the maximum of the absolute values of the coefficients of P ; the height of a
rational integer is equal to its absolute value. Finally, the degree of Q(α1, . . . , αn) is
its dimension as a vector space over Q.

12 DAVID G. RADCLIFFE

In our application of Theorem 5, we assume that n = 3, and that α1, α2, α3 are
rational integers. So in this context, d = 1 and (16nd)2(n+2) = 48
10.

We now prove the main theorem of the section.

Theorem 6. Let a, b ≥ 2 be integers, and suppose that log(a)/ log(b) is irrational.
Then there exists C > 0, depending only on a and b, such that

cb(a
n) > log n
log log n + C
holds for all sufficiently large n.

In the following, C and C1, C2, C3, . . . denote effectively computable positive real
constants, depending on a and b, but independent of n. Inequalities involving these
constants are assumed to hold for all sufficiently large n.

Proof. Let an = b
m (
d1b−m1 + · · · + dkb−mk) ,
where m = ⌈logb an⌉, k = cb(a
n), di ∈ {1, . . . , b − 1}, and

1 = m1 < · · · < mk ≤ m.

That is, d1, . . . , dk are the nonzero digits of a
n in base b, and m1, . . . , mk are their
positions when the digits are numbered from left (most-significant) to right (least-
significant). We may assume that k ≥ 2.

Fix i ∈ {1, . . . , k − 1}. Our goal is to show that large gaps between digit positions
cannot occur; in particular, we prove that
mi+1
mi < C log n.

This implies that the number of gaps, and hence the number of nonzero digits, cannot
be too small.

Define
 q = bmi(d1b−m1 + · · · + dib−mi),

r = b
m(di+1b−mi+1 + · · · + dkb−mk),

so that an = b
m−miq + r.
In other words, if we split the base-b expansion of an at the i-th nonzero digit,
the digits up to and including that digit combine to form the integer q, while the
remaining digits combine to form the integer r.

ELEMENTARY BOUNDS ON DIGITAL SUMS OF POWERS, FACTORIALS, AND LCMS 13

From the base-b expansion, we obtain the bounds

bm−1 < a
n < b
m,

bmi−1 < q < bmi,

bm−mi+1 ≤ r < bm−mi+1+1.

Consequently,

(6) b−mi+1 < a
−nr < b
−mi+1+2,

which implies that mi+1 − 2
mi < − log(a−nr)
log q < mi+1
mi − 1
provided that q ≥ 2 and mi ≥ 2.

If mi ≥ 3 (and mi+1 ≥ 4) then
mi+1 − 2
mi ≥ 1
2 mi+1
mi , mi+1
mi − 1 ≤ 3
2 mi+1
mi ,

hence

(7) 1
2 mi+1
mi < − log(a−nr)
log q < 3
2 mi+1
mi .

Now set

(8) Λ = log(a−nbm−miq) = −n log a + (m − mi) log b + log q.

Since a−nbm−miq = 1 − a
−nr and a
−nr < 1/2,

(9) |Λ| = − log(1 − a−nr) < 2a
−nr.

Applying Baker’s theorem to (8) yields a lower bound on |Λ|. This implies an upper
bound on the gap mi+1/mi, as shown in (11) below. There are two cases, depending
on the size of q.

Case 1. q < b
2, or equivalently mi ≤ 2.

Here, the log αi are uniformly bounded, so Baker’s theorem yields

log |Λ| > −C1 log n.

Thus, log(2a−nr) > −C1 log n,
and hence, log(2b−mi+1+2) > −C1 log n,

14 DAVID G. RADCLIFFE

which implies that mi+1 < C2 log n, C2 > C1/ log b.

Since mi ≥ 1, we also have mi+1
mi < C2 log n.

Case 2. q > b
2, or equivalently mi ≥ 3.

Here, log q is unbounded, so Baker’s theorem yields

log |Λ| > −C3 log q log n

Thus, log(2a−nr) > −C3 log q log n,
and hence,

(10) − log(a−nr)
log(q) < C4 log n, C4 > C3.

Combining (7) and (10) gives
mi+1
mi < C5 log n, C5 = 2 C4.

In either case, we have

(11) mi+1
mi < C6 log n, C6 = max(C2, C5),

and thus

(12) log ( mi+1
mi
 ) < log log n + C7, C7 = log C6.

Summing the logarithms of these ratios,

log mk =
 k−1∑

i=1 log ( mi+1
mi
 )

which yields

(13) log mk < (k − 1)(log log n + C7).

Write a
n as bm−mkt, where bmk−1 < t < bmk.

Thus mk ≍ log t, and log t ≍ n by Lemma 3, so mk ≍ n and

(14) log mk = log n + O(1).

ELEMENTARY BOUNDS ON DIGITAL SUMS OF POWERS, FACTORIALS, AND LCMS 15

Therefore, (13) and (14) imply that

k > log n
log log n + C
as required. □

Since this is a long proof, let us review the main steps.

(1) Approximate a
n by truncating to the i-th nonzero digit.

(2) Estimate the digit gap mi+1/mi in terms of the truncation error a
−nr.

(3) Use Baker’s theorem to obtain a lower bound on the truncation error.

(4) Deduce thereby an upper bound on the digit gap.

(5) Compute a lower bound on the number of gaps, and hence the number of
nonzero digits.
 References

[1] Balog, A. and Dartyge, C., “On the sum of the digits of multiples.” Moscow Journal of Com-
binatorics and Number Theory, 2 (2012), pp. 3–15.
[2] Baker, A. and W¨ustholz, G., “Logarithmic forms and group varieties.” Journal f¨ur die reine
und angewandte Mathematik, 442 (1993), pp. 19–62. https://doi.org/10.1515/crll.199
3.442.19
[3] Graham, R., Knuth, D., and Patashnik, O., Concrete Mathematics, 2nd ed., Addison–Wesley,
Reading, Massachusetts, 1994.
[4] Luca, F., “Distinct digits in base b expansions of linear recurrence sequences,” Quaestiones
Mathematicae 23 (2000), pp. 389–404.
[5] Luca, F., “The number of non-zero digits of n!” Canadian Mathematical Bulletin 45.1, (2002),
pp. 115–118.
[6] Radcliffe, D., “The growth of digital sums of powers of 2,” arXiv preprint arXiv:1605.02839
(2016). https://arxiv.org/abs/1605.02839
[7] Sanna, C., “On the sum of digits of the factorial,” J. Number Theory 147 (2015), pp. 836–841.
[8] Senge, H. G. and Straus, E. G., “PV-numbers and sets of multiplicity,” Period. Math. Hungar.
3 (1973), no. 1, pp. 93–100.
[9] Sierpi´nski, W., 250 Problems in Elementary Number Theory, American Elsevier Publishing
Company, New York, 1970.
[10] Stewart, C. L., “On the representation of an integer in two different bases,” J. Reine Angew.
Math. 319 (1980), pp. 63–72.
[11] Stolarsky, K. B., “Integers whose multiples have anomalous digital frequencies,” Acta Arith
38.2 (1980), pp. 117–128.
