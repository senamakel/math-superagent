> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/alekseyev2601_pdf.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2601.17832 | converted from PDF -->

## What it claims

Abstract. We propose an efficient computational method for finding all so-
lutions n ≤ U to the Diophantine equation aσ(n) = bn + c, where integer
coefficient a, b, c and an upper bound U are given. Our method is implemented
in SageMath computer algebra system within the framework of recursively
enumerated sets and natively benefits from MapReduce parallelization. We
used it to discover new solutions to many published equations and close gaps in
between the known large solutions, including but not limited to hyperperfect
and f -perfect numbers, as well as to significantly lift the existence bounds in
open questions about quasiperfect and almost-perfect numbers.

1. Introduction

The sum of divisors function, commonly denoted by σ, has fascinated people for
centuries. In particular, it provides elegant characterizations for several important
classes of integers, such as the prime numbers, which are precisely the solutions to
σ(n) = n + 1, and the perfect numbers, defined by the equation σ(n) = 2n, among
others discussed later in the present paper. While the solutions to the former…

(…

## Statements it makes

Theorem 3.1 (OEIS [14]). For integers d and ℓ > 0, the number n = 2ℓ−1(2ℓ −
d − 1) is a solution to σ(n) = 2n + d whenever 2
ℓ − d − 1 is prime.

Theorem 3.2. Let n, U , and S be positive integers such that n ≤ U , σ(n) ≥ S,
and spf(n) = pk for some index k. Then for a positive integer ℓ:

Theorem 3.3. Let a
′, b
′, c
′, U ′ be defined as above. Suppose n′ ≤ U ′ is a solution
to a′σ(n
′) = b
′n′ + c′ with ω(n′) ≥ 2 and spf(n
′) = pt > lpf(m) for some index
t. Then at a certain point the prime wheel reaches the state with |W | ≤ ω(n′) and
W1 = pt.

*[digest of a 34593 character source; every section, statement, and proof in full at `research/sources/alekseyev2601_pdf.full.md`]*
