> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/bilu-hong-luca-big-prime-factors-elliptic-curves.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2112.07046 | converted from PDF -->

## What is in it

- E(Fqn ) of Fqn -rational points. The numbers (#E(Fqn ))n≥1 form a linearly re-
current…
- {d | n : d < x} ≤ Θ(x, S)
- {d | n : d < x} ≤ exp (
(log n)
1/2 log log n + 20 · 3 log n
(log log n)2 log(2 log log…
- P ′ ≤ ( P
n + 1) exp (
80 log n log log log n
(log log n)2
 ) . (3.16)
- P ′ ≤ ∑
- P ′ ≤ ∑


## What it claims

Let E be an elliptic curve over the ﬁnite ﬁeld Fq. We prove that,
when n is a suﬃciently large positive integer, #E(Fqn ) has a prime factor
exceeding n exp(c log n/ log log n).

Contents

1 Introduction 1
1.1 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2 Auxiliary facts 4
2.1 The Theorems of Stewart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.2 Cyclotomic polynomials and primitive divisors . . . . . . . . . . . . . . . . . . 4
2.3 Counting S-units . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3 Proof of Theorem 1.1 7
3.1 Case (3.3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.2 Case (3.4) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

1 Introduction

A Lucas sequence (un)n≥0 is a binary recurrent sequence of integers satisfying
un+2 = run+1 + sun for all n ≥ 0, and with u0 = 0, u1 = 1. The parameters
r, s are assumed to be nonzero coprime integers such that r2 + 4s ̸= 0. In this
case,
 un = α
n − βn

α − β holds for all…

## Statements it makes

Theorem 1.1. Set n0 := exp exp(max{1010, 3q}) Let n be a positive integer sat-
isfying n ≥ n0. Then the rational integer (α
n − 1)(¯α
n − 1) has a prime divisor p
satisfying
 p ≥ n exp (0.0001 log n
log log n
 ) .

Theorem 2.1. Let γ be a non-zero algebraic number of degree d, not a root
of unity. Set p0 = exp(80000d(log∗d)
2). Then for every prime p of the ﬁeld
K = Q(γ) whose absolute norm N p satisﬁes N p ≥ p0, and every positive inte-
ger n we have

Theorem 2.2. Let γ be a non-zero algebraic number of degree 2, not a root of
unity. Assume that N γ = ±1. Set p0 = exp exp(max{108, 2|DK|}), where DK
is the discriminant of the quadratic ﬁeld K = Q(γ). Then for every prime p of K
with underlying rational prime p ≥ p0, and every positive integer n we have

Proposition 2.3. 1. Let p be a primitive divisor of un. Then νp(Φn(γ)) ≥ 1
and N p ≡ 1 mod n; in particular, N p ≥ n + 1.

Proposition 2.5. Let S be a set of k prime numbers. Then for x ≥ 3 we have

Proposition 2.6. In the set-up of Proposition 2.5 assuming x ≥ 7 we have

Proposition 2.7. In the set-up of Proposition 2.5, assume that p ≥ k1/2 for
every p ∈ S. Then

Proposition 2.3.3 implies that, for n ≥ 8,
∑

Proposition 2.3.3 bounds the sum on the right by

Theorem 1.1 is proved.
 13

*[digest of a 24176 character source; every section, statement, and proof in full at `research/sources/bilu-hong-luca-big-prime-factors-elliptic-curves.full.md`]*
