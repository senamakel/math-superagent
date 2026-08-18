> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/daans-2023-universal-Z-10-quantifiers.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2301.02107 | converted from PDF -->

## What it claims

Abstract. We show that for a global ﬁeld K, every ring of S-integers has a
universal ﬁrst-order deﬁnition in K with 10 quantiﬁers. We also give a proof
that every ﬁnite intersection of valuation rings of K has an existential ﬁrst-
order deﬁnition in K with 3 quantiﬁers.

1. Introduction

It is a longstanding open problem whether the ring of integers Z has an exis-
tential ﬁrst-order deﬁnition in the ﬁeld of rational numbers Q in the signature
of rings. In more algebraic terms, the question is whether there exist a natural
number m and a polynomial F ∈ Q[X, Y1, . . . , Ym] such that

Z = {x ∈ Q | ∃y1, . . . , ym ∈ Q : F (x, y1, . . . , ym) = 0}.

While the answer to this question still eludes us, Koenigsmann was able to show
that the complement Q \ Z is existentially deﬁnable in Q [Koe16]. In other
words, he showed that there exist a natural number m and a polynomial F ∈
Q[X, Y1, . . . , Ym] such that

(1) Z = {x ∈ Q | ∀y1, . . . , ym ∈ Q : F (x, y1, . . . , ym) ̸= 0}.

One also says that Z has a universal ﬁrst-order deﬁnition in Q, and the number
m is called the number of…

Date:…

2…

## Statements it makes

Theorem (see Theorem 5.6). Let K be a global ﬁeld, S a ﬁnite set of valuations
on K. There exists a polynomial F ∈ K[X, Y1, . . . , Y10] such that, for the ring of
S-integers OS, we have

Corollary (see Corollary 6.2). There exists F ∈ Z[X, Y1, . . . , Y9, Z1, . . . , Z10] with
the following property. There is no algorithm which decides, for a given x ∈ Q,
whether or not

Proposition (see Proposition 4.2). Let K be a global ﬁeld, R a ﬁnite intersection
of valuation rings of K. Then there exists a polynomial F ∈ K[X, Y1, Y2, Y3] such
that R = {x ∈ K | ∃y1, y2, y3 ∈ K : F (x, y1, y2, y3) = 0}.

*[digest of a 47518 character source; every section, statement, and proof in full at `research/sources/daans-2023-universal-Z-10-quantifiers.full.md`]*
