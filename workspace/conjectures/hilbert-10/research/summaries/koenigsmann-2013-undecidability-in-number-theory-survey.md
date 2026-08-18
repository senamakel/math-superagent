> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/koenigsmann-2013-undecidability-in-number-theory-survey.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1309.0441 | converted from PDF -->

## What it claims

1 Decidability, Turing machines and Gödel’s 1st Incomplete-
ness Theorem 6
1.1 Turing machines . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.2 Coding 1st-order Lring-formulas and Turing machines . . . . . 7
1.3 Proof of Gödel’s 1st Incompleteness Theorem (sketch) . . . . . 8

2 Undecidability of number rings and ﬁelds 9
2.1 The ﬁeld Qp of p-adic numbers . . . . . . . . . . . . . . . . . . 9
2.2 The Local-Global-Principle (LGP) for quadratic forms over Q 14
2.3 Julia Robinson’s deﬁnition for Z in Q and in other number ﬁelds 14
2.4 Totally real numbers . . . . . . . . . . . . . . . . . . . . . . . 16
2.5 Large algebraic extensions of Q and geometric LGP’s . . . . . 19

3 Hilbert’s 10th Problem and the DPRM-Theorem 20
3.1 The original problem and ﬁrst generalisations . . . . . . . . . 20
3.2 Listable, recursive and diophantine sets . . . . . . . . . . . . . 23
3.3 The Davis-Putnam-Robinson-Matiyasevich
(= DPRM)–Theorem . . . . . . . . . . . . . . . . . . . . . . . 24
3.4 Consequences of the DPRM-Theorem . . . . . . . . . . . . . . 26

4 Deﬁning Z in Q 27
4.1 Key steps in the…

## Statements it makes

Theorem 1.1 ([Göd31]). Th(N ) is undecidable.

Corollary 1.2. The Peano axioms don’t axiomatise all of Th(N ).

Corollary 1.3. Th(⟨Z; +, ·; 0, 1⟩) is undecidable.

Lemma 2.3 (Hensel’s Lemma). Simple zeros lift: Let f ∈ Zp[X] be a
monic polynomial and assume α ∈ Zp is such that α is a simple zero of f
(i.e., f (α) = 0 ̸= f ′(α)). Then there is some β ∈ Zp with f (β) = 0 and
β = α.

Theorem 2.7 (Ax-Kochen/Ershov). Th(Qp) is decidable. It is eﬀectively
axiomatized by the following axioms:

Theorem 2.10 (Hasse-Minkowski-Theorem). A rational a is represented by
q in Q if and only if a is represented by q in all Qp and in R.

Theorem 2.11 ([Rob49]). For any n ∈ Q,

Corollary 2.12. Th(Q) is undecidable.

Theorem 2.13 ([Rob59]). For any number ﬁeld K, OK is deﬁnable in K
and Z is deﬁnable in OK. In particular, Th(OK ) and Th(K) are undecidable.

fact, most of them are: there are only countably many decision algorithms,
but uncountably many non-isomorphic, and hence, in this case, non-elementarily
equivalent algebraic extensions of Q. To give an explicit example, let A be an
undecidable (= non-recursive, cf. section 3.2) subset of the set of all primes
and let K := Q({√p | p ∈ A}).

Theorem 2.14 ([Rob62]). Th(OT ) is undecidable.

Lemma 2.15. Let R be an integral domain with N ⊆ R. Let F ⊆ ℘(R)
be a family of subsets of R which is arithmetically deﬁned (or uniformly
parametrised), say, by an Lring-formula φ(x; y1, . . . , yk), i.e., for any F ⊆ R,

Lemma 2.16.

Theorem 2.17. T is pseudo-real-closed (‘PRC’), i.e. T satisﬁes the follow-
ing geometric LGP: for each (aﬃne) algebraic variety V /T ,

Theorem 2.18. Th(T ) is decidable.

Corollary 2.19. OT is not deﬁnable in T .

Theorem 2.22. Let V be an aﬃne variety deﬁned over ̃Z. Then

Theorem 2.23. Th(̃Z) is decidable.

Corollary 3.2. Let K be a ﬁeld not containing the algebraic closure of the
prime ﬁeld. Then

Proposition 3.5 (The Halting Problem of Computer Science is un-
decidable). There is no algorithm to decide whether a program (with code)
p halts on INPUT x.

Theorem 3.6 ([Mat70], conjectured by Davis 1953, building on work of
Davis, Putnam and Robinson). Every listable subset of Z is diophantine.

Corollary 3.7. Hilbert’s 10th problem is unsolvable.

Theorem 3.8 ([Dav53]). If A ⊆ N is listable then A is almost diophantine,
i.e., there is a polynomial g ∈ Z[T ; X; Y, Z] such that for all a ∈ N

Theorem 3.10 ([Rob52]). There is a polynomial q ∈ Z[A, B, C; X] such that
for all a, b, c ∈ N a = b
c ⇔ ∃x q(a, b, c; x) = 0,

Theorem 3.11 ([DPR61]). If A ⊆ N is listable then there are exponential
polynomials EL and ER such that, for all a ∈ N,

Theorem 3.12 ([Mat70]). There is a diophantine relation J(u, v) of expo-
nential growth.

Corollary 3.13. There is some n ∈ N and a polynomial f ∈ Z[X1, . . . , Xn]
such that P = f (Z
n) ∩ N>0.

Corollary 3.14. There is a polynomial U ∈ Z[T ; X] and an algorithm pro-…


*[further statements in the full text]*

*[digest of a 82420 character source; every section, statement, and proof in full at `research/sources/koenigsmann-2013-undecidability-in-number-theory-survey.full.md`]*
