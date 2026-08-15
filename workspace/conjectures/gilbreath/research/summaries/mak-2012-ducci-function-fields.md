> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/mak-2012-ducci-function-fields.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://www.fq.math.ca/Papers1/50-4/Kit-HoMak.pdf | converted from PDF -->

## What it claims

Abstract. A classical Ducci sequence of integers is a sequence of n-tuples of integers obtained
by iterating the map (a1, . . . , an) ↦→ (|a1 − a2|, |a2 − a3|, . . . , |an − a1|). In this paper, we study
a natural analogue of the Ducci sequences deﬁned over function ﬁelds that are motivated by
the number ﬁeld-function ﬁeld analogy. Results that are analogous to the classical case have
been found, and diﬀerences between the two cases are also explored.

1. Introduction

Let d ≥ 3 be an integer. A classical Ducci sequence of integers is a sequence of d-tuples
u, ˜D(u), ˜D2(u) = ˜D( ˜D(u)), . . ., obtained by iterating the map ˜D : Zd → Zd, where
˜D(u0, u1, . . . , ud−1) = (|u0 − u1| , |u1 − u2| , . . . , |ud−1 − u0|). (1.1)

The origin of this sequence dates back to E. Ducci, who is credited in [12] for discovering the
fact that every Ducci sequence will eventually stabilize at the zero vector when d = 4. In fact,
the same property holds if and only if d is a power of 2. For any positive integer d, the dynamic
system induced by D always forms a cycle. Having relations to the…

In the…

## Statements it makes

Lemma 2.5. The set L(D) is a ﬁnite dimensional vector space over Fq. In particular, it is a
ﬁnite set. In addition, the set L(D) is nonempty if deg D is suﬃciently large.

Proposition 3.5. Every Ducci sequence over K eventually forms a cycle. For example, for
any u ∈ K d, there exists positive integers n0, k such that Dn(u) = Dn+k(u) for all n ≥ n0.

Theorem 4.1. Let D be the Ducci map as in Deﬁnition 3.1. The following are equivalent:
(1) d is a power of 2,
(2) For all x ∈ K d, Dn(x) = (0, 0, . . . , 0) for all suﬃciently large n.

Lemma 4.2. Let d = 2st with t odd. Let u = (u0, . . . , ud−1) ∈ Fd
2, then u vanishes if and only
if ui = ui+2s for all i (here the index is taken modulo d).

Proposition 4.3. Let d = 2st with t odd, and u = (u0, . . . , ud−1) ∈ K d.
(1) Let φ be as in (4.1). If φ(u) is non-vanishing (in F2), then u is non-vanishing.
(2) If ui = ui+2s for all i, then it is vanishing.

Proposition 4.6. Let d = 2st and u = (u0, . . . , ud−1) ∈ K d be a positive, vanishing d-tuple
such that all ui only have poles at P∞. Let m = maxi(−v∞(ui)), then the length of d is at
most 2s(m + 1).

Theorem 5.2. Let u ∈ K d
∞. Then exactly one of the following happens:
(1) The sequence Dn(u) tends to zero as n → ∞,
(2) The sequence Dn(u) is eventually periodic.

Corollary 5.3. If d is a power of 2, then the sequence Dn(u) either tends to zero as n → ∞,
or is zero for all suﬃciently large n.

Conjecture. Every Ducci sequence over K∞ is eventually periodic.

Proposition 6.2. Let K be a function ﬁeld whose constant ﬁeld has q elements. If u ∈ K d

*[digest of a 31497 character source; every section, statement, and proof in full at `research/sources/mak-2012-ducci-function-fields.full.md`]*
