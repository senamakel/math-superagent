> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/hong-2022-stewart-revisited.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2204.01858 | converted from PDF -->

## What is in it

- P ′ ≤ ( P
n + 1) exp (
80 log n log log log n
(log log n)2
 ) . (3.20)


## What it claims

Abstract
Let γ be an algebraic number of degree 2 and not a root of unity.
In this note we show that there exists a prime ideal p of Q(γ) satisfying
νp(γn − 1) ≥ 1, such that the rational prime p underlying p grows quicker
than n.

Contents

1 Introduction 1
2 Preliminary results 2
2.1 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.2 Uniform explicit version of Stewart’s theorem . . . . . . . . . . . . . . . . . . . 3
2.3 Cyclotomic polynomials and primitive divisors . . . . . . . . . . . . . . . . . . 3
2.4 Estimates for the arimetical functions . . . . . . . . . . . . . . . . . . . . . . . 4
3 Proof of Theorem 1.2 4
3.1 Case (3.9) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.2 Case (3.10) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

1 Introduction

Let P (m) denote the largest prime factor of integer m, with the convention
P (0) = P (±1) = 1. For any integer n, we denote the n-th cyclotomic polynomial
in x by Φn(x) as usual.
Schinzel [8] asked if there exists any…

T…

## Statements it makes

Theorem 1.1. Let γ be a non-zero algebraic number, not a root of unity. De-
note ω(γ) the number of primes p of the ﬁeld K = Q(γ) with the property
νp(γ) ̸= 0. Let P be the biggest element of the set

Theorem 1.2. Suppose γ is an algebraic number of degree 2 and not a root
of unity. Set n0 = exp exp(max{1010, 3|DK|}). Let n be a positive integer
satisfying n ≥ n0. There exists a prime ideal p of K = Q(γ) such that νp(γn −
1) ≥ 1 and the underlying rational prime p of p satisﬁes

Theorem 2.1. Let γ be a non-zero algebraic number of degree d, not a root
of unity. Set p0 = exp(80000d(log∗d)
2). Then for every prime p of the ﬁeld
K = Q(γ) whose absolute norm N p satisﬁes N p ≥ p0, and every positive inte-
ger n we have

Theorem 2.2. Let γ be a non-zero algebraic number of degree 2, not a root of
unity. Assume that N γ = ±1. Set p0 = exp exp(max{108, 2|DK|}), where DK
is the discriminant of the quadratic ﬁeld K = Q(γ). Then for every prime p
of K with underlying rational prime p ≥ p0, and every positive integer n we
have
 νp(γn − 1) ≤ p exp (
−0.001 log p
log log p
 ) h(γ) log∗n. (2.3)

Proposition 2.3. 1. Let γ be an algebraic number. Then

Proposition 2.4. 1. Let p be a primitive divisor of un. Then νp(Φn(γ)) ≥ 1
and N p ≡ 1 mod n; in particular, N p ≥ n + 1.

*[digest of a 14143 character source; every section, statement, and proof in full at `research/sources/hong-2022-stewart-revisited.full.md`]*
