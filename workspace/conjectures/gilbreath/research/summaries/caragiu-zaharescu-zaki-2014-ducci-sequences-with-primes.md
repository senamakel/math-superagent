> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/caragiu-zaharescu-zaki-2014-ducci-sequences-with-primes.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.fq.math.ca/Papers1/52-1/CaragiuZaharescuZaki.pdf | converted from PDF -->

## What it claims

Abstract. We introduce an analogue of the Ducci game that involves d-tuples of prime
numbers subjected to the iteration G sending such a d-tuple (p1, p2, . . . , pd) into (gpf(p1 +
p2), gpf(p2 + p3), . . . , gpf(pd + p1)), where for any x ≥ 1, gpf(x) represents the greatest prime
factor of the integer x. We show that the iteration of G always leads into a limit cycle C.
Moreover, if C has length greater than 1, then not only every vector in C has all components
in P0 := {2, 3, 5, 7}, but every element of P0 appears as a component of some vector in C. An
analysis of the lengths of the nontrivial cycles for small values of d is provided.

1. Introduction

An interesting elementary result going back to at least the 1930’s [15, 19] shows that iterating
the map φ(x1, x2, x3, x4) = (|x1 − x2|, |x2 − x3|, |x3 − x4|, |x4 − x1|) over the integers eventually
leads to the null vector. This generated extensive research and inspired numerous results on
the dynamics induced by the Ducci maps φ : Zd → Zd given by

φ(x0, x1, . . . , xd−1) = (|x0 − x1|, |x1 − x2|, . . . , |xd−1 − x0|).

For example,…

## Statements it makes

Proposition 1. Every ‘GPF-Ducci’ iteration is ultimately periodic.

Theorem 2. Let X ∈ P d with LX > 1. Then for all n ≥ nX the components of Gn(X) belong
to P0. Moreover, each element of P0 appears in Gn(X) for some n ≥ nX.

Lemma 1. Let q be the largest entry in the matrix A. Then q is odd, and if the primes
a and b are consecutive entries in a row of A producing q = gpf(a + b) in the immediately
following row, one of the following holds true: (i) a = b = q, or (ii) q − 2 is a prime and either
(a, b) = (2, q − 2) or (a, b) = (q − 2, 2).

Lemma 2. Let p := q − 2. Then p must occur in A.

Lemma 3. The largest entry q of the limit cycle matrix A satisﬁes q ≤ 7.

Lemma 4. Each one of the primes 2, 3, 5, and 7 is an entry of the matrix A.

*[digest of a 22494 character source; every section, statement, and proof in full at `research/sources/caragiu-zaharescu-zaki-2014-ducci-sequences-with-primes.full.md`]*
