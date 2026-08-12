> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/holdener_stanton_outlaws.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://cs.uwaterloo.ca/journals/JIS/VOL10/Holdener/holdener7.pdf | converted from PDF -->

## What it claims

The abundancy index of a positive integer n is deﬁned to be the rational number
I(n) = σ(n)/n, where σ is the sum of divisors function σ(n) = ∑d|n d. An abundancy
outlaw is a rational number greater than 1 that fails to be in the image of of the map
I. In this paper, we consider rational numbers of the form (σ(N ) + t)/N and prove
that under certain conditions such rationals are abundancy outlaws.

1 Introduction

The abundancy index of a positive integer n is deﬁned to be the rational number I(n) =
σ(n)/n, where σ is the sum of divisors function, σ(n) = ∑
d|n d. Positive integers having
integer-valued abundancy indices are said to be multiperfect numbers, and if I(n) = 2 in
particular, then n is perfect. More generally, the abundancy index of a number n can be
thought of as a measure of its perfection; if I(n) < 2 then n is said to be deﬁcient, and if
I(n) > 2 then n is abundant. In this way, the abundancy index is a useful tool in gaining a
better understanding of perfect numbers. In fact, the following theorem provides conditions
equivalent to the existence of an odd perfect…

The…

## Statements it makes

Theorem 1.1. There exists an odd perfect number if and only if there exist positive integers
p, n, and α such that p ≡ α ≡ 1 mod 4, where p is a prime not dividing n, and

Lemma 3.1. Let N = ∏n
i=1 pki
i for primes p1, p2, ..., pn. Then

Theorem 3.2. Let r/s > 1 be a fraction in lowest terms such that there exists a divisor
N = ∏n
i=1 pki
i of s satisfying the following two conditions:

Lemma 4.1. Let N = ∏n
i=1 pki
i , where pi is a prime for all 1 ≤ i ≤ n. Then, for a given
1 ≤ j ≤ n and a positive integer t,
 pj < 1
t σ
 ( N

Theorem 4.2. For a positive integer t, let σ(N )+t
N be a fraction in lowest terms, and let
N = ∏n
i=1 pki
i for primes p1, p2, ..., pn. If there exists a positive integer j ≤ n such that
pj < 1
t σ(N/pkj
j ) and σ(pkj
j ) has a divisor D > 1 such that at least one of the following is
true:

Corollary 4.3. Let σ(N )+1
N be a fraction in lowest terms, and let N = ∏n
i=1 pki
i for primes
p1, p2, ..., pn. If there exists a natural number j ≤ n such that pj < σ(N/pkj
j ) and σ(pkj
j ) has
a divisor D such that at least one of the following is true:

Lemma 5.1. Let N = ∏n
i=1 pki
i for primes p1, p2, ..., pn. Then N is relatively prime to
σ(N ) + 1 if and only if pi is relatively prime to σ(N/pki
i ) + 1 for all 1 ≤ i ≤ n.

Corollary 5.2. For all natural numbers m and nonnegative integers n, and for all odd
primes p such that gcd(p, σ(2m)) = 1, the rational number

Corollary 5.3. For all primes p > 3,
 σ(2p) + 1
2p

Corollary 5.3 also captures another (potentially inﬁnite) set of outlaws having even de-
nominators...

Corollary 5.5. If N is an even perfect number,

Corollary 5.6. Let M be an odd natural number, and let p, α, and t be odd natural numbers
such that p ∤ M and p < 1
t σ(M ). Then, if (σ(pαM ) + t)/pαM is in lowest terms,

Corollary 5.7. For primes p and q, with 3 < q, p < q, and gcd(p, q + 2) = gcd(q, p + 2) = 1,

Corollary 5.7 produces outlaws with ease. To illustrate, let p and q be odd primes with
3 < p < q, and assume q ≡ 1 (mod p). Then p ∤ q + 2 and q ∤ p + 2. Since Dirichlet’s theorem
on arithmetic progressions of primes ensures the existence of an inﬁnite sequence of primes
q satisfying q ≡ 1 (mod p), Corollary 5.7 reveals an inﬁnite class of outlaws corresponding
to each odd prime p > 3. The sequences corresponding to the primes 5, 7, and 11 follow.

*[digest of a 45326 character source; every section, statement, and proof in full at `research/sources/holdener_stanton_outlaws.full.md`]*
