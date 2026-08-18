> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/ostrowski-numeration-addition-finite-automata.pdf.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1407.7000 | converted from PDF -->

## What it claims

ABSTRACT. We present an elementary three pass algorithm for computing addition in
Ostrowski numerations systems. When a is quadratic, addition in the Ostrowski numera-
tion system based on a is recognizable by a ﬁnite automaton. We deduce that a subset of
X ⊆ Nn is deﬁnable in (N,+,Va), where Va is the function that maps a natural number x to
the smallest denominator of a convergent of a that appears in the Ostrowski representation
based on a of x with a non-zero coefﬁcient, if and only if the set of Ostrowski representa-
tions of elements of X is recognizable by a ﬁnite automaton. The decidability of the theory
of (N,+,Va) follows.
 1. INTRODUCTION

A continued fraction expansion [a0; a1, . . . , ak, . . . ] is an expression of the form

a0 + 1
a1 + 1
a2+ 1
a3+ 1
...

For a real number a, we say [a0; a1, . . . , ak, . . . ] is the continued fraction expansion of a if
a = [a0; a1, . . . , ak, · · · ] and a0 ∈ Z, ai ∈ N>0 for i > 0. Let a be a real number with continued
fraction expansion [a0; a1, . . . , ak, . . . ]. In this note we study a numeration system due to
Ostrowski [13]…

(…

## Statements it makes

Algorithm 1. Let k = m + 1. Then set

Proposition 2.1. Algorithm 1 leaves the value represented unchanged. That is, for every
k ∈ N with 3 ≤ k ≤ m + 1 m
∑
i=0zk,i+1qi = m
∑
i=0 si+1qi.

Proposition 2.2. For k > 1, z3,k ≤ ak and z3,1 ≤ a1 − 1.

Lemma 2.3. Let k ∈ N and k ≥ 3. Then
(i) If zk+1,k−1 = 2ak−1 + 1, then zk+1,k−2 = 0.
(ii) If zk+1,k−1 = 2ak−1, then zk+1,k−2 ≤ ak−2.

Lemma 2.4. Let k ∈ N and 3 ≤ k ≤ m.
(i)k If zk+1,k−1 > ak−1, then zk+1,k < ak.
(ii)k If zk+1,k−1 = ak−1 and zk+1,k−2 > 0, then zk+1,k < ak.

Algorithm 2. Let k = 2. Then set

Lemma 2.5. There is no k ∈ N such that
• wm+1,k = ak
• wm+1,k−1 < ak−1,
• wm+1,k−2 = ak−2, and
• wm+1,k−3 > 0.

Algorithm 3. Let k = m + 3. Then set

Proposition 2.6. Let l ≥ 3. Then there is no k ≥ l − 1 such that vl,k = ak and vl,k−1 > 0.

Lemma 2.7. Let l ∈ {3, . . . , m + 3}. Then there is no k ∈ N such that
• vl,k = ak
• vl,k−1 < ak−1,
 9

Corollary 2.8. The word v3,m+2 . . . v3,1 is the Ostrowski representation of M + N.

Lemma 3.5. Let l, n ∈ N and let ∑k bk+1qk be the Ostrowski representation of n. Then
bl+1 = j iff εj(ql, n).

Lemma 3.8. Let n ∈ N and let ∑k bk+1qk be the Ostrowski representation of n. Then
(i) n ∈ Ue if and only if for all even k bk+1 ≤ 1, and for all odd k bk+1 = 0,
(ii) n ∈ Uo if and only if for all odd k bk+1 ≤ 1, and for all even k bk+1 = 0.

Theorem 3.10. Let X ⊆ Nn be a-recognizable. Then X is deﬁnable in (N, +,Va).

*[digest of a 45205 character source; every section, statement, and proof in full at `research/sources/ostrowski-numeration-addition-finite-automata.pdf.full.md`]*
