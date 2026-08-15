> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/cobeli-crasmaru-zaharescu-2000-cellular-automaton-torus.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://emis.muni.cz/journals/PM/57f3/pm57f305.pdf | converted from PDF -->

## What it claims

In the seventies, when more and more people had access to personal comput-
ers, John Conway’s game of life became very popular. Since then, the study of
this type of game grew up into the theory of cellular automata. In [4] (see also
[1, page 311]) Brian Thwaites proposes a conjecture which leads to such a cellular
automaton.

Thwaites’s conjecture is: Given any ﬁnite sequence of rational numbers, take
the positive diﬀerences of successive members (including diﬀerencing the last
member with the ﬁrst); iteration of this operation eventually produces a set of
zeros if and only if the size of the set is a power of 2.

Our aim in this note is to prove that Thwaites conjecture holds true.
Let a0, ..., ad−1 be the given d rational numbers, which we may think as the
heights of d poles situated around a circle. These numbers are replaced at the
next step by d rational numbers given by the diﬀerence in heights of successive
poles, and then the process is repeated.
Being an iteration of the same operation, it resembles Conway’s life game.
For now the ﬁeld of play is a 1-dimensional torus and…

## Statements it makes

Lemma 1. Let d be a positive integer, (a0, a1, ...) a sequence of nonnegative
integers satisfying (1) and suppose the function φ is deﬁned as above. Then
there is a positive integer a such that for suﬃciently large n all the components
of φ(n)(a0, a1, ...) belong to {0, a}.

Theorem 1. Let d be a positive integer and suppose the evolution function φ
is deﬁned as above. Then there is a rational number r > 0 such that the repeated
application of φ to any initial sequence of rational numbers (a0, a1, ...) satisfying
(1) will eventually produce a cycle of sequences with the property (1) with all
their components in {0, r}. Moreover, the cycle will contain only the sequence
(0, 0, ...) independently on the initial sequence if and only if d is a power of 2.

Theorem 2.

Lemma 2. For any nonnegative integers k, m, n and any x, y ∈ S we have:

Corollary 1. Suppose d = 2k. Then, for any x ∈ S and n ≥ 1 we have that
φ(d+n−1)(x) = 0 if s is even and φ(nd)(x) = x if s is odd.

Proposition 1. Let x ∈ S and

Theorem 3. For any positive integer k represented as in (6), we have

Corollary 2. Let k = 2l0 + 2l1 + · · · + 2lµ be the representation in base 2 of
the positive integer k, where l0 < · · · < lµ, and φ(x) = x ρ(x). Denote

Corollary 3. A positive integer k is a period for φ(x) = x ρ(x) if and only
if the numbers νk,d(m), 1 ≤ m ≤ d have the same parity.

Conjecture. Suppose d is a prime number, s is the order of 2 mod d, s is
even and k = d(2s/2 − 1). Then

*[digest of a 21484 character source; every section, statement, and proof in full at `research/sources/cobeli-crasmaru-zaharescu-2000-cellular-automaton-torus.full.md`]*
