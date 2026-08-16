> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/dimitrov-howe-2021-powers-of-3-few-nonzero-bits.pdf.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2105.06440 | converted from PDF -->

## What is in it

- A j = O2(Mi)/O2(Mi−1). If mi is coprime to Mi−1, which is the case for all of the values…


## What it claims

ABSTRACT. Using completely elementary methods, we find all powers of 3 that can be written as the
sum of at most twenty-two distinct powers of 2, as well as all powers of 2 that can be written as the sum
of at most twenty-five distinct powers of 3. The latter result is connected to a conjecture of Erd˝os, namely,
that 1, 4, and 256 are the only powers of 2 that can be written as a sum of distinct powers of 3.
We present this work partly as a reminder that for certain exponential Diophantine equations, elemen-
tary techniques based on congruences can yield results that would be difficult or impossible to obtain
with more advanced techniques involving, for example, linear forms in logarithms.

1. Introduction

To introduce our topic, we begin with some numerical observations. For an integer x ≥ 0, consider
the binary representation of 3x. In Table 1 we give this representation for x ≤ 25, and we tabulate the
number of bits in the binary representation together with the number of those bits that are equal to 1.
Based on this limited data, it looks like about half of the bits of the…

20…

## Statements it makes

Theorem 1.1. The only powers of 3 that can be written as the sum of twenty-two or fewer distinct
powers of 2 are 3x, where 0 ≤ x ≤ 25.

Theorem 1.2. The only powers of 2 that can be written as the sum of twenty-five or fewer distinct
powers of 3 are:
 20 = 30

Definition 2.2. Let M > 0 be an integer and p a prime. We say that a power of p, say pi, is determinate
modulo M if the only integer b ≥ 0 with pb ≡ pi mod M is b = i; otherwise, we say that pi is an
indeterminate power of p modulo M.

Lemma 3.1. Let M be a positive integer. Suppose x > 2, y > 0, and c are integers such that 3y ≡
c + 2x mod M. If O′
3(M) is not divisible by 2x−1 and O′
2(M) is not divisible by 3y, then there are
integers x′ ≥ 0 and y′ ≥ 0 such that

Lemma 3.1 shows that in the example we presented in the introduction, it was necessary for us to
use a modulus divisible by a prime (in our case, 257) for which either the order of 3 is divisible by 25

Lemma 3.2.

*[digest of a 52036 character source; every section, statement, and proof in full at `research/sources/dimitrov-howe-2021-powers-of-3-few-nonzero-bits.pdf.full.md`]*
