> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/bordignon-johnston-starichkova-explicit-chen-linear-sieve-arxiv-2207.09452.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2207.09452 | converted from PDF -->

## What it claims

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

Conjec…

## Statements it makes

Conjecture 1 (Goldbach). For any even integer N ⩾ 4 there exist two primes p1 and
p2, such that N = p1 + p2.

Theorem 1 (Vinogradov–Helfgott). For any odd number N ⩾ 7 there exist three
primes p1, p2 and p3, such that
 N = p1 + p2 + p3.

Theorem 2 (Chen). All sufficiently large even numbers can be written as the sum of
a prime and another number that is the product of at most two primes (a semi-prime).

Theorem 3. Let π2(N ) denote the number of representations of a given even integer
N as the sum of a prime and a semi-prime. If N > exp(exp(32.7)), then

Corollary 4. Every even integer N > exp(exp(32.7)) can be represented as the sum
of a prime and a square-free number with at most two prime factors.

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
versions of…

Theorem 6 (The linear-sieve, explicit version). Let A = {a(n)}
∞
n=1 be an arithmetic
function such that
a(n) ⩾ 0 for all n and |A| =
 ∞∑

Lemma 7. The bound (18) holds with cn as in Table 2 below.

Lemma 8 ([40, Lemma 9.7]). For all n ⩾ 2 we have that (18) holds with

Lemma 9. Let γ3 = 4e/3 and for any 2 ⩽ s0 ⩽ 2.8, let γs0 = e
s0−2. Then

Lemma 10. Let κ2 = 0.9607, κ2.2 = 0.9557, κ2.4 = 0.9457, κ2.6 = 0.9261, κ2.8 = 0.8914
and κ3 = 0.8349. Then for s0 ∈ {2, 2.2, 2.4, 2.6, 2.8, 3}, we have

Lemma 11. Let z ⩾ 2, and D > 0 be real such that

Lemma 12. Keep the notation of Lemma 11. Let τ ′
n be such that τ ′
1 = 3 and for n ⩾ 2

Proposition 13. Let z, D, s, P, g(d) and ε satisfy the hypotheses of Lemma 11. Let

Lemma 14. Let τn and τ ′
n be as defined in (31) and (40) respectively. For some choice
of ε ∈ (0, 1/74] and any ke, ko ⩾ 1, we have

Lemma 15. For all x ⩾ exp(20), there exists a prime in the interval [0.999x, x).

Lemma 16. For all 2 ⩽ x ⩽ 10
12, we have

Lemma 17. For all x ⩾ 2, with M defined in (47), we have

Lemma 18. Let z > exp(4000) and u0 = 10
9. Then for all u0 < u < z, we have

Lemma 19 ([12, Lemma 2]). Let f and F be as defined in (8). Then,

Lemma 20 ([24, Lemma 1 (ii)]). Let f (t) be a positive, monotone function defined for
w ⩽ t ⩽ z with f ′(t) piecewise continuous on [w, z], and c(n) be an arithmetic function
satisfying ∑

Lem…


*[further statements in the full text]*

*[digest of a 114259 character source; every section, statement, and proof in full at `research/sources/bordignon-johnston-starichkova-explicit-chen-linear-sieve-arxiv-2207.09452.full.md`]*
