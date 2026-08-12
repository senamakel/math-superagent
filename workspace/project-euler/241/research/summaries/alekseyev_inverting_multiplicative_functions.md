> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/alekseyev_inverting_multiplicative_functions.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://cs.uwaterloo.ca/journals/JIS/VOL19/Alekseyev/alek5.pdf | converted from PDF -->

## What it claims

We propose a generic algorithm for computing the inverses of a multiplicative func-
tion under the assumption that the set of inverses is ﬁnite. More generally, our algo-
rithm can compute certain functions of the inverses, such as their power sums (e.g.,
cardinality) or extrema, without direct enumeration of the inverses. We illustrate
our algorithm with Euler’s totient function ϕ(⋅) and the k-th power sum of divisors
σk(⋅). For example, we can establish that the number of solutions to σ1(x) = 10
1000 is
15, 512, 215, 160, 488, 452, 125, 793, 724, 066, 873, 737, 608, 071, 476, while it is intractable
to iterate over the actual solutions.

1 Introduction

A value of a multiplicative function f on a positive integer n equals the product of its values
on the prime powers in the prime factorization of n. That is, if n = pe1
1 ⋅ pe2
2 ⋯pem
m , where
p1 < p2 < ⋅ ⋅ ⋅ < pm are primes and e1, e2, . . . , em are positive integers, then

f (n) =
 m
M
i=1 f (pei
i ).

1

In particular, f (1) = 1. Famous examples of multiplicative functions include τ (n), the
number of divisors of n (with τ…

Tσ…

## Statements it makes

Theorem 1. We have the following identity for formal Dirichlet series of variable s over
the semiring (Pﬁn(Z>0), +, ×):

Theorem 2. Let (X, ⊕, ⊗) be a commutative semiring and C ∶ (Pﬁn(Z>0), +, ×) → (X, ⊕, ⊗)
be a weak homomorphism, then

Theorem 3. Let n be an integer and D be the set of divisors of n. Given ℓ atomic series
for C(f −1(n)), their ⊗D-product can be computed with O(ℓ ⋅ τ (n)2) operations in (X, ⊕, ⊗).

Theorem 4. Given an integer n and the set of its divisors D, the atomic series for C(ϕ−1(n))
can be computed in time O(τ (n) ⋅ log n ⋅ (log5+ǫ n + TC(2 log n))) for any ǫ > 0.

Theorem 5. Given an integer n and the set of its divisors D, the atomic series for C(σ−1
k (n))
can be computed in time O(τ (n) ⋅ log n ⋅ (log6+ǫ n + TC(log n))) for any ǫ > 0.

*[digest of a 20889 character source; every section, statement, and proof in full at `research/sources/alekseyev_inverting_multiplicative_functions.full.md`]*
