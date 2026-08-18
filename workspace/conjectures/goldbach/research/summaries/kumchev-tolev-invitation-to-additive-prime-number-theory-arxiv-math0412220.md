> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/kumchev-tolev-invitation-to-additive-prime-number-theory-arxiv-math0412220.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/math/0412220 | converted from PDF -->

## What it claims

The main purpose of this survey is to introduce the inexperienced reader to additive
prime number theory and some related branches of analytic number theory. We state
the main problems in the ﬁeld, sketch their history and the basic machinery used to
study them, and try to give a representative sample of the directions of current research.
2000 MSC: 11D75, 11D85, 11L20, 11N05, 11N35, 11N36, 11P05, 11P32, 11P55.

1 Introduction

Additive number theory is the branch of number theory that studies the representations of
natural numbers as sums of integers subject to various arithmetic restrictions. For example,
given a sequence of integers
 A = {a1 < a2 < a3 < · · · }

one often asks what natural numbers can be represented as sums of a ﬁxed number of
elements of A; that is, for any ﬁxed s ∈ N, one wants to ﬁnd the natural numbers n such
that the diophantine equation
 x1 + · · · + xs = n(1.1)

has a solution in x1, . . . , xs ∈ A. The sequence A may be described in some generality (say,
one may assume that A contains “many” integers), or it may be a particular sequence of
some arithmetic…

## Statements it makes

Theorem 1 (Vinogradov, 1937). For a positive integer n, let R(n) denote the number of
representations of n as the sum of three primes. Then

Theorem 2 (Chen, 1973). For an even integer n, let r(n) denote the number of represen-
tations of n in the form n = p + P2, where p is a prime and P2 is an almost prime of order
2. There exists an absolute constant n0 such that if n ≥ n0, then

Theorem 3. Let k, s and n be positive integers, and let R∗
k,s(n) denote the number of solu-
tions of the diophantine equation
 pk
1 + pk
2 + · · · + pk
s = n(1.14)

Corollary 3.1. Every suﬃciently large integer n ≡ 5 (mod 24) can be represented as the
sum of ﬁve squares of primes.

Corollary 3.2. Every suﬃciently large odd integer can be represented as the sum of nine
cubes of primes.

Theorem 4. Let k ≥ 4 be an integer, and let H(k) be as above. Then

Theorem 5 (de la Vall´ee Poussin, 1899). Let ∆(x) be deﬁned by (2.2). There exists an
absolute constant c > 0 such that

Theorem 6 (Vinogradov, Korobov, 1958). Let ∆(x) be deﬁned by (2.2). There exists
an absolute constant c > 0 such that

Theorem 7 (Siegel, 1935). For any ﬁxed A > 0, there exists a constant c = c(A) > 0
such that
 π(x; q, a) = li x
φ(q) + O(
x exp ( − c√log x))

Theorem 8 (Bombieri, Vinogradov, 1965). For any ﬁxed A > 0, there exists a B =
B(A) > 0 such that
 E(x, Q) ≪ x(log x)−A,(2.9)

Lemma 3.1. Let α be real and let a and q be integers satisfying

Lemma 3.2 (Dirichlet). Let α and Q be real and Q ≥ 1. There exist integers a and q
such that
 1 ≤ q ≤ Q, (a, q) = 1, |qα − a| < Q
−1.

Lemma 3.3. Let k ≥ 2, let α ∈ R, and suppose that a and q are integers satisfying

Lemma 3.4 (Hua’s lemma). Suppose that k ≥ 1, and let g(α) be deﬁned by (3.36). There
exists a constant c = c(k) ≥ 0 such that
∫ 1

Lemma 3.5. Suppose that k ≥ 11 and g(α) is deﬁned by (3.36). There exists a constant
c = c(k) > 0 such that for r > 1
2 k2(log k + log log k + c),

Theorem 9 (Szemer´edi’s theorem for pseudorandom measures). Let δ ∈ (0, 1] be a
ﬁxed real number, let k ≥ 3 be a ﬁxed integer, and let N be a large prime. Suppose that ν is a
“k-pseudorandom measure8” on ZN = (Z/NZ) and f : ZN → [0, ∞) is a function satisfying

Theorem 10 (Green and Tao, 2004). Let k ≥ 3 and let A be a set of prime numbers
such that
 lim sup
N →∞ #{n ∈ A : n ≤ N}
π(N) > 0.

*[digest of a 130811 character source; every section, statement, and proof in full at `research/sources/kumchev-tolev-invitation-to-additive-prime-number-theory-arxiv-math0412220.full.md`]*
