> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/huang-wen-fibonacci-gap-sequence.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1404.4269 | converted from PDF -->

## What it claims

Let ω be a factor of Fibonacci sequence F∞ = x1x2 · · · , then it appears in the sequence inﬁnitely
many times. Let ωp be the p-th appearance of ω and νω,p be the gap between ωp and ωp+1.
In this paper, we discuss the structure of the gap sequence {νω,p}p≥1, we ﬁrst introduce the
singular kernel word sk(ω) for any factor ω of F∞ and give a decomposition of ω with respect to
sk(ω). Using the singular kernel and the decomposition, we prove the gap sequence {νω,p}p≥1
has exactly two diﬀerent elements {νω,1, νω,2} and determine the expressions of gaps completely,
then we prove that the gap sequence over the alphabet {νω,1, νω,2} is still a Fibonacci sequence.
Finally, we introduce the spectrum for studying some typical combinatorial, using the results
above, we determine completely the spectrums.

1. Introduction

Let A = {a, b} be a binary alphabet. Let A∗ be the set of ﬁnite words on A and AN be the
set of one-sided inﬁnite words. The elements of A∗ are called words or factors, which will be
denoted by ω. The neutral element of A∗ is called the empty word, which we denote by ε. For
a…

## Statements it makes

Proposition 1.5 (Uniqueness of Singular Kernel and Singular Decomposition).
Assume that ω ≺ F∞ and ω ̸∈ {ε, ab, ba, aba}. Then
(1) ω has a unique singular kernel sk(ω), i.e., as a factor, sk(ω) appears in ω only once;
(2) ω has a unique singular decomposition by its singular as ω = µ1(ω) ∗ sk(ω) ∗ µ2(ω).

Proposition 1.7 (Wen and Wen[19]).

Proposition 1.5 (Uniqueness of Singular Kernel and Singular Decomposition).
Assume that ω ≺ F∞ and ω ̸∈ {ε, ab, ba, aba}. Then
(1) ω has a unique singular kernel sk(ω), i.e., as a factor, sk(ω) appears in ω only once;
(2) ω has a unique singular decomposition by its singular as ω = µ1(ω) ∗ sk(ω) ∗ µ2(ω).

Proposition 1.5 states a factor ω can be decomposed by its singular kernel, and two questions
arise naturally: (1) for any factor ω, determine explicitly its decomposition by singular kernel;
(2) the sequences {ωp}p≥0 and {sk,p}p≥0 describes the locations of these factors, what is the
relation between the singular kernel of sk(ωp) and the singular word sk,p? Theorem 2.3 answers
completely the ﬁrst question, and Theorem 2.1 answers the second question positively, it shows
that sk(ωp) = sk,p.

Theorem 2.1 (Decomposition of ωp and νω,p by sk(ω)).
Let ωp ≺ F∞ and sk(ωp) = sk. Both decompositions below are unique:
(1) ωp = µ1(ω) ∗ sk,p ∗ µ2(ω);
(2) νω,p = µ−1
2 (ω) ∗ νsk,p ∗ µ−1
1 (ω).

Theorem 2.2 (Gap and gap sequence).
(1) Any factor ω ≺ F∞ has exactly two distinct gaps νω,1 and νω,2;
(2) The gap sequence {νω,p}p≥1 is the Fibonacci sequence.

Theorem 2.3 (Decomposition of ω by sk(ω), more explicitly).

Theorem 2.4 (Expressions of νω,1 and νω,2).

Lemma 3.1. Let sk be the k-th singular word. Then:
(1) sk = βα−1sk−1sk−2 = sk−2sk−1α−1β;
(2) sk = sk−2sk−3sk−2.

Lemma 3.2. ∏k−1
j=−1 sj = α−1sk+1.

Lemma 3.3. For any ω ﬁxed, let sk(ω) = sk, then sk(ωp) = sk,p, i.e., the singular kernel of
ωp is equal to sk,p by location.

Corollary 3.4. Let sk be the singular word of order k, θk := α−1sk+1sksk+1α−1.
(1) sk(θk) = sk;
(2) If τ ≺ θk with sk(τ ) = sk, then τ appears in θk only once;
(3) Let ω be a factor with singular kernel sk, then ω ≺ θk, i.e.,

Theorem 2.1(Decomposition of ωp and νω,p by sk(ω)).
Let ωp ≺ F∞ and sk(ω) = sk. Both decompositions below are unique:
(1) ωp = µ1(ω) ∗ sk,p ∗ µ2(ω);
(2) νω,p = µ−1
2 (ω) ∗ νsk,p ∗ µ−1
1 (ω).

Theorem 2.2(Gap and gap sequence).
(1) Any factor ω ≺ F∞ has exactly two distinct gaps νω,1 and νω,2;
(2) The gap sequence {νω,p}p≥1 is the Fibonacci sequence.

Lemma 4.1. The six types are pairwise disjoint and their union is all factors of F∞, i.e.,
(1) {ω ∈ F∞| ∃ k, s.t. |ω| = fk} = T1.1 ⊔ T1.2 ⊔ T1.3;
(2) {ω ∈ F∞| ∃ k, s.t. fk < |ω| < fk+1} = T2.1 ⊔ T2.2 ⊔ T2.3.

Theorem 2.3 (Decomposition of ω by sk(ω)).

Corollary 4.2.
(1) ω ∈T1.2⇔ ω = Ci(Fk), where fk−1 − 1 ≤ i ≤ fk − 1.
(2) ω ∈T1.3⇔ ω = Ci(Fk), where 0 ≤ i ≤ fk−1 − 2.

Theorem 2.4(1)

Theorem 2.4(2)

Theorem 2.4(3)

Theorem 2.4(4)

T…


*[further statements in the full text]*

*[digest of a 49676 character source; every section, statement, and proof in full at `research/sources/huang-wen-fibonacci-gap-sequence.full.md`]*
