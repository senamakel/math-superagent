> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/radcliffe-2025-elementary-digital-sums-of-powers.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2511.15850 | converted from PDF -->

## What it claims

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

1, 2, 4, 8, 16, 32, 64, 128, 256,…

## Statements it makes

Theorem 1. Let (ek) be a sequence of integers such that e1 ≥ 1 and 2ek > 10ek−1
for all k ≥ 2. Suppose that N is divisible by 2
ek but not by 10. Then c10(N ) ≥ k.

Corollary 1. Let a be a positive integer that is divisible by 2 but not divisible by 10.
Then c10(a
n) ≥ log4 n for all n > 1.

Theorem 2. Let 2 ≤ a < b be integers with a | b. Let (ek) be a sequence of integers
such that e1 ≥ 1 and a
ek > b
ek−1 for all k ≥ 2. Suppose that N is divisible by aek but
not by b. Then cb(N ) ≥ k.

Theorem 3. Let 2 ≤ a < b be integers with a | b. Suppose that N is divisible by an

Lemma 1. Let a, b ≥ 2 be integers such that log(a)/ log(b) is irrational. Suppose
that a
n = bmt, where t ≥ 1 is an integer. Then there exists a prime factor p of a,
and C > 0 depending only on a and b, such that νp(t) ≥ Cn.

Theorem 4. Let a, b ≥ 2 be integers. Let d be the smallest factor of a such that
gcd(a/d, b) = 1, and suppose that log(d)/ log(b) is irrational. Then cb(a
n) > C log n
for all sufficiently large n, where C > 0 depends only on a and b.

Lemma 2. Let m, r ≥ 1 and b ≥ 2 be integers. If m is divisible by b
r − 1 then
sb(m) ≥ (b − 1)r.

Lemma 3. Let a, b ≥ 2 be integers with log(a)/ log(b) irrational. Then there exist
positive constants C and C ′, depending only on a and b, such that whenever

Theorem 5. Let Λ = b1 log α1 + · · · + bn log αn,

Theorem 6. Let a, b ≥ 2 be integers, and suppose that log(a)/ log(b) is irrational.
Then there exists C > 0, depending only on a and b, such that

*[digest of a 22396 character source; every section, statement, and proof in full at `research/sources/radcliffe-2025-elementary-digital-sums-of-powers.full.md`]*
