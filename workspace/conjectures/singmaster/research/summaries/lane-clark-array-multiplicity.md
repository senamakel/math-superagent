> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/lane-clark-array-multiplicity.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://emis.muni.cz/journals/INTEGERS/papers/k14/k14.pdf | converted from PDF -->

## What is in it

- A14 INTEGERS 10 (2010), 187-199


## What it claims

Abstract
We prove a general theorem about the multiplicity of the entries in certain integer
arrays which is best possible in general. As an application we give non-trivial
bounds for the multiplicities of several well-known combinatorial arrays including
the binomial coeﬃcients, Narayana numbers and the Eulerian numbers. For the
binomial coeﬃcients we obtain the result of Singmaster.

1. Introduction

An integer array or array is a function a : N
2 → N where a(n, 0) = 1 (n ∈
N). For a function b : P
2 → N where b(n, 1) = 1 (n ∈ P), consider the array
a(n, k) = b(n, k + 1) (n ∈ P, k ∈ N) where a(0, 0) = 1 and a(0, k) = 0 (k ∈ P).
We write a = shift b and say a results from shifting b. Here N denotes the non-
negative integers, P denotes the positive integers and [n] = {1, . . . , n} (n ∈ P). The
cardinality of a set S is denoted # S or |S|.
Suppose a is an array. Then

(D1) a is semi-triangular if and only if there exists a strictly increasing function d :
N ↦→ N such that a(n, k) ̸= 0 ⇔ 0 ≤ k ≤ d(n) (n ∈ N).

Suppose a = (a, d) is a semi-triangular array. Then

(D2) a is increasing…

## Statements it makes

Theorem 2. Suppose that a = (a, d, f, r, ∆, g) is a normal array. For all integers
t ≥ 2, Na(t) < r(
g−1(t) + ∆
)
.

Corollary 3. Suppose a = (a, d, f, r, ∆, g) is a normal array. If g(x) = τ x−c where
τ ∈ (1, ∞) and c ∈ R, then
 Na(t) < r(
logτ t + c + ∆
) .

Corollary 4. Suppose a = (a, d, f, r, ∆, g) is a normal array. If g(x) = Ω (τ x)
where τ ∈ (1, ∞), then Na(t) = O( logτ t ) .

*[digest of a 21537 character source; every section, statement, and proof in full at `research/sources/lane-clark-array-multiplicity.full.md`]*
