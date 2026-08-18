> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/li-wu-fibonacci-n-factor-complexity-2022.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://arxiv.org/pdf/2212.10069 | converted from PDF -->

## What it claims

Abstract. In this paper, we introduce a variation of the factor complexity, called the N -
factor complexity, which allows us to characterize the complexity of sequences on an inﬁnite
alphabet. We evaluate precisely the N -factor complexity for the inﬁnite Fibonacci sequence f
given by Zhang, Wen and Wu [Electron. J. Comb., 24 (2017)]. The N -factor complexity of a
class of digit sequences, whose nth term is deﬁned to be the number of occurrences of a given
block in the base-k representation of n, is also discussed.

1. Introduction

The factor complexity of inﬁnite sequences on a ﬁnite alphabet was well studied in recent
decades. For an inﬁnite sequence a = a(0)a(1)a(2)a(3) . . . , its factor complexity Pa(n) counts
the number of distinct subwords a(i)a(i + 1) . . . a(i + n − 1) (i ≥ 0) where n ≥ 1 is an integer.
It measures the complexity or randomness of an inﬁnite sequence. It is well known that an
ultimately periodic sequence has a bounded factor complexity (see Morse and Hedlund [9]).
Among the non-periodic sequences, the Sturmian sequences have the smallest factor complexity…

## Statements it makes

Theorem 1.4. For all N ≥ 0 and n ≥ 1,

Theorem 1.8. Let n ≥ 1 and M = ⌈logk(n)⌉ + 2. For all N ≥ M ,

Lemma 3.1. Suppose p, q ≥ 0 and q is even. Let u = τ p(q). Then |u| = Fp+1. Further, u0 = q,
uFp+1−1 = p + q, and q + 1 ≤ ui ≤ p + q − 1 for 1 ≤ i ≤ Fp+1 − 2.

Lemma 3.2. If N ≥ 1 and n ≥ 1, then Ff (n, N ) = Fτ N +1(0)(n, N ).

Proposition 3.3. If n = 1, then Pf (1, N ) = N + 1 for all N ≥ 0. If n ≥ 2, we have

Proposition 3.4. For all n ≥ 2,

Corollary 3.5. If n ≥ 3 and N ≥ φ(n) + 1, then the following holds:

Theorem 4.1. Let n ≥ 1 be an integer and w ∈ Σ∗
k\{ε}. For all N ≥ ⌈logk(n)⌉ + 2,

Proposition 4.2. Let k = 2, w = 1 and n ≥ 1. Suppose that u ∈ Nn
≥1. For all N ≥ ⌈logk(n)⌉+2,

Proposition 4.3. Let k = 2, w = 1 and n ≥ 1. For all N ≥ ⌈logk(n)⌉ + 2, we have

Proposition 4.4. Suppose (k, w) ̸= (2, 1). Let n ≥ 1 and u ∈ Nn. Then for all N ≥ ⌈logk n⌉+1,
u ∈ F (1)
s (n, N ) if and only if u + 1 ∈ F (1)
s (n, N + 1).

Lemma 4.5. Suppose that (k, w) ̸= (2, 1). Let n ≥ 1 and u ∈ Nn. Then for all N ≥ ⌈logk n⌉+ 1,
we have u + 1 ∈ F (1)
s (n, N + 1) if u ∈ F (1)
s (n, N ).

Lemma 4.6. Suppose that (k, w) ̸= (2, 1). Let m and n be positive integers. Let x be the longest
common preﬁx of (m)k, (m + 1)k, . . . , (m + n − 1)k. If w ≺ x, then there exists m′ such that

Lemma 4.7. Suppose that (k, w) ̸= (2, 1). Let n ≥ 1 and u ∈ Nn. Then for all N ≥ ⌈logk n⌉+ 1,
we have u ∈ F (1)
s (n, N ) if u + 1 ∈ F (1)
s (n, N + 1).

Lemma 4.8. Let w = 0q, N ≥ 0 and n ≤ kN −2. For all m > 0 satisfying s(m + 1) ≥ N , we
have s(m + i) > 0 for all 1 ≤ i ≤ n.

Lemma 4.9. If w = 0q, then for all mi + 2 ≤ m ≤ mi+1, we have s(mi + 1) > s(m).

Proposition 4.10. Let n ≥ 2 and w = 0q (q ≥ 1). Then for all N ≥ ⌈logk(n)⌉ + 2, we have
P (2)
s (n, N ) = n − 1.

Lemma 4.11. Let w = (k − 1)
q, N ≥ 0 and n ≤ kN −2. For all m > 0 satisfying s(m) ≥ N , we
have s(m − i) > 0 for 0 ≤ i ≤ n − 1.

Lemma 4.12. If w = (k − 1)
q, then for all mi−1 + 1 ≤ m ≤ mi − 1, we have s(mi) > s(m).

Proposition 4.13. Let n ≥ 2, w = (k − 1)
q (q ≥ 1) and (k, w) ̸= (2, 1). Then for all N ≥
⌈logk(n)⌉ + 2, we have P (2)
s (n, N ) = n − 1.

Proposition 4.14. Let n ≥ 1 and w ∈ Σ∗
k\{ε}. If w ∈ {0}∗ ∪ {k − 1}∗ and (k, w) ̸= (2, 1), then
for all N ≥ ⌈logk(n)⌉ + 2, we have P (2)
s (n, N ) = n − 1.

Lemma 4.15. Let w ∈ Σ∗
k\{ε}. If w /∈ {0}∗ ∪{k −1}∗, then for all m ≥ 0, |s(m)−s(m+1)| ≤ 1.

Lemma 4.17. Let α ∈ Σ∗
k\{ε}, w ∈ Σ∗
k\{ε} and w /∈ {0}∗ ∪{k −1}∗. Suppose that |α|w = r > 0.
Write α = x w z with |x w|w = 1. Then |z|0 ≤ |z| − r + 1 and |z|k−1 ≤ |z| − r + 1.

Proposition 4.18. Fix n ≥ 1 and w ∈ Σ∗
k\{ε}. If w /∈ {0}∗ ∪ {k − 1}∗, then for all N ≥
⌈logk(n)⌉ + 2, we have P (1)
s (n, N ) = P (1)
s (n, ⌈logk(n)⌉ + 1) ≥ 1.

Lemma 4.19. Let u, v ∈ Σl
k, a ∈ Σ∗
k. Then [u]k − [v]k = [a conj(v)]k − [a conj(u)]k.

Proposition 4.20. Suppose n ≥ 1 and N ≥ ⌈logk(n)⌉ + 2. Let u ∈ Σn
N +1, w ∈ Σq
k and

*[digest of a 52641 character source; every section, statement, and proof in full at `research/sources/li-wu-fibonacci-n-factor-complexity-2022.full.md`]*
