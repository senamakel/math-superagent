> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/minimal-linear-representations-regular.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2201.13446 | converted from PDF -->

## What it claims

In this note, we precisely elaborate the connection between recognisable series
(in the sense of Berstel and Reutenauer) and q-regular sequences (in the sense of
Allouche and Shallit) via their linear representations. In particular, we show that
the minimisation algorithm for recognisable series can also be used to minimise
linear representations of q-regular sequences.

1 Introduction

1.1 Overview

Every regular sequence can also be seen as a recognisable series—deﬁnitions of both
notions are recalled below—and both can be described by a linear representation using
a collection of square matrices and two vectors. So when the authors of this note imple-
mented both concepts in SageMath [7], this relation and property played fundamental
roles. For recognisable series, there exists an algorithm to minimise the dimension of

Clemens Heuberger clemens.heuberger@aau.at, https://wwwu.aau.at/cheuberg, Alpen-
Adria-Universität Klagenfurt, Austria

Daniel Krenn math@danielkrenn.at, http://www.danielkrenn.at, Paris Lodron University of
Salzburg, Austria

Gabriel F. Lipnik…

Support Clemens…

## Statements it makes

Lemma 2.2 (Berstel–Reutenauer [3, Proposition 2.1]). Let A be a ﬁnite set, x ∈ K A⋆

Proposition 2.3. Let A be a ﬁnite set, x ∈ K A⋆ be a recognisable series and (u, M, w)
be a minimal linear representation of x. Let z ∈ A be such that x(bz) = x(b) holds for
all b ∈ A⋆. Then we have M(z)w = w.

Lemma 3.2. Let y ∈ K N0 be a q-regular sequence with linear representation (u, M, w)
and let n ∈ N0. Then we have
 y(n) = uM(digitsq(n))w. (5)

Lemma 3.3. Let y ∈ K N0 be a q-regular sequence and (u, M, w) a linear representation
of y. Then y(value(b)) = uM(b)w

Theorem 3.6. Let y be a q-regular sequence and (u, M, w) be a minimal linear represen-
tation of the recognisable series associated to y. Then (u, M, w) is a linear representation
of y, and it is also minimal.

*[digest of a 24369 character source; every section, statement, and proof in full at `research/sources/minimal-linear-representations-regular.full.md`]*
