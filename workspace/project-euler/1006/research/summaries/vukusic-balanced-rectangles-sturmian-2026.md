> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/vukusic-balanced-rectangles-sturmian-2026.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2602.12801 | converted from PDF -->

## What is in it

- ([ξ, ξ + δ) ∩ B) ∈ {c, c + 1}.


## What it claims

Abstract. We consider m × n rectangular matrices formed from Sturmian words with
slope α, and we fully characterise their balance properties in terms of the Ostrowski
representations of m and n with respect to α. This generalises recent results by Anselmo
et al., as well as those by Shallit and the author, where only quadratic irrational slopes
were considered. In contrast to the two mentioned papers, the approach in this paper is
based on the distribution of nα mod 1.

1. Introduction

Let α ∈ (0, 1) be irrational and θ ∈ [0, 1). Then the Sturmian word a = a1a2a3 · · · with
slope α and intercept θ can be defined via

(1.1) an := ⌊(n + 1)α + θ⌋ − ⌊nα + θ⌋ ∈ {0, 1}.

For example, setting α = (3 − √5)/2 and θ = 0 we get the famous infinite Fibonacci word

f = 010010100100101 · · · .

Recall that a factor is simply a contiguous block of symbols within a word, and the weight
of a factor of a binary word is the number of 1’s contained in it. One of the basic properties
of Sturmian words is that they are balanced, that is, the weights of any two factors of the
same length differ by at…

A(…

## Statements it makes

Definition 1.1. Let a = a1a2a3 · · · be an infinite word over {0, 1}. We say that the m × n
rectangles of a are balanced if there exists an integer c = c(a, m, n) such that

Definition 1.2. Let α, δ ∈ (0, 1) and let N ≥ 1 be an integer. We say the intervals of length
δ are balanced with respect to (α, N ) if there exists an integer c = c(α, δ, N ) such that for all
half open intervals I = [ξ, ξ + δ), 0 ≤ ξ < 1, we have

Theorem 2.1. Let α ∈ (0, 1) be irrational and 2 ≤ m ≤ n. Then the m × n rectangles of
the Sturmian words with slope α are balanced if and only if the Ostrowski representations of
m, n with respect to α are of at least one of the following four shapes.
They have “split representations” in the following sense:

Lemma 2.4. Let α < 1/2 be irrational and n a positive integer. Then the Ostrowski repre-
sentation of n with respect to α is n = ∑N
k=0 bkqk if and only if the Ostrowski representation
of n with respect to 1 − α is n = ∑N +1
k=1 bk−1qk.

Theorem 3.1. Let a be a Sturmian word with slope α. Then the m × n rectangles are
balanced if and only if the intervals of length {nα} are balanced with respect to (α, m).

Definition 4.1. Let B = {ξ0, ξ1, . . . , ξm−1} be a set of m distinct points on the torus T and
let δ ∈ (0, 1). We say that the intervals of length δ are balanced with respect to B if there

Definition 4.2. Let B = {ξ0, ξ1, . . . , ξm−1} ⊆ T be a set of m distinct points and let
δ ∈ (0, 1). Then we define the following two maps on the set {0, 1, . . . , m − 1}: fleft maps ℓ
to the index of the closest point in B that lies to the left of ξℓ + δ, and fright maps ℓ to the
index of the closest point in B that lies to the right of ξℓ + δ. In other words,

Lemma 4.3. Let B = {ξ0, ξ1, . . . , ξm−1} ⊆ T be a set of m distinct points. Moreover, let
δ ∈ (0, 1) be such that δ ̸= ξi − ξj for all i, j. Then the following statements are equivalent:

Lemma 4.6. Let B = {ξ0, ξ1, . . . , ξm−1} ⊆ T be a set of m distinct points and let δ ∈ (0, 1).
Then the intervals of length δ are balanced with respect to B if and only if the intervals of
length 1−δ are balanced. Moreover, if δ ̸= ξi −ξj for all i, j, then for all ε with |ε| sufficiently
small, the intervals of length δ are balanced if and only if the intervals of length 1 − δ + ε are
balanced.

Lemma 5.1. Let α ∈ (0, 1/2) and n ≥ 1 with k0(n) = L. Then

Lemma 5.2. Let α ∈ (0, 1/2) and n ≥ 1 and assume that k0(n) ≥ 1. Then we have

Lemma 5.2 cannot be extended to k0(n) ≥ 0, so when the smallest allowed digit in the
representation of n shows up, then {nα} might lie on “the wrong side of 1/2”. Indeed, if
k0(n) = 0, we might have {nα} > 1/2 if b0(n) is large, even though from the parity of
k0(n) we would expect {nα} < 1/2. The next lemma will be useful when dealing with such
exceptional cases.

Lemma 5.3. Assume α < 1/2 and k0(n) = 0. Then

Lemma 5.4. Let ⟨·⟩∗…


*[further statements in the full text]*

*[digest of a 70227 character source; every section, statement, and proof in full at `research/sources/vukusic-balanced-rectangles-sturmian-2026.full.md`]*
