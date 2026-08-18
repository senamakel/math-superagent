> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/poonen-2009-ae-formula.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://math.mit.edu/~poonen/papers/ae.pdf | converted from PDF -->

## What is in it

- X(Fq) ≥ (q + 1 − 2
√q) − 12 > 0,


## What it claims

Abstract. We prove that Z in deﬁnable in Q by a formula with 2 universal quantiﬁers
followed by 7 existential quantiﬁers. It follows that there is no algorithm for deciding, given
an algebraic family of Q-morphisms, whether there exists one that is surjective on rational
points. We also give a formula, again with universal quantiﬁers followed by existential
quantiﬁers, that in any number ﬁeld deﬁnes the ring of integers.

1. Introduction

1.1. Background. D. Hilbert, in the 10th of his famous list of 23 problems, asked for
an algorithm for deciding the solvability of any multivariable polynomial equation in inte-
gers. Thanks to the work of M. Davis, H. Putnam, J. Robinson [DPR61], and Y. Matija-
seviˇc [Mat70], we know that no such algorithm exists. In other words, the positive existential
theory of the integer ring Z is undecidable.
It is not known whether there exists an algorithm for the analogous problem with Z
replaced by the ﬁeld Q of rational numbers. But Robinson showed that the full ﬁrst-order
theory of Q is undecidable: she reduced the problem to the corresponding known…

## Statements it makes

Lemma 2.1.
(i) If p /∈ ∆a,b, then Sa,b(Qp) = Qp.
(ii) If p ∈ ∆a,b, then red
−1
p (Up) ⊆ Sa,b(Qp) ⊆ Zp.

Lemma 2.2. If a, b ∈ Q
× and either a > 0 or b > 0, then Sa,b = Q ∩ ⋂
p Sa,b(Qp).

Lemma 2.3. For any prime power q, the set Uq is nonempty. If q > 11 then Uq + Uq = Fq.

Lemma 2.5. If a, b ∈ Q
× and either a > 0 or b > 0, then Ta,b = ⋂
p∈∆a,b Z(p).

Lemma 2.7. We have ⋂

Theorem 3.1. The set Z equals the set of t ∈ Q for which the following Π+
2 -formula is true
over Q:
 (∀a, b)(∃a1, a2, a3, a4, b1, b2, b3, b4, x1, x2, x3, x4, y1, y2, y3, y4, n)

Theorem 4.1. It is possible to deﬁne Z in Q with a Π+
2 -formula with 2 universal quantiﬁers
followed by 7 existential quantiﬁers.

Theorem 4.3 (Cornelissen and Shlapentokh). For every ϵ > 0, there is a set R of primes
of natural density at least 1 − ϵ such that Z is deﬁnable in Z[R−1] using a Π
+
2 -formula with
just one universal quantiﬁer (instead of two).

Theorem 5.1. There is a Π+
2 -formula that in any number ﬁeld k deﬁnes its ring of integers.

*[digest of a 17008 character source; every section, statement, and proof in full at `research/sources/poonen-2009-ae-formula.full.md`]*
