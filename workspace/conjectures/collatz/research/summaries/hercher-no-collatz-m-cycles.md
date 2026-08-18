> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/hercher-no-collatz-m-cycles.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

```claim
id: hercher-m92
answers: current-best-exclusion-82b1
statement: There is no Collatz m-cycle with m ≤ 91 local minima; any non-trivial cycle has at least m = 92 local minima (Main Theorem 23).
hypotheses: m counts local minima in a non-trivial cycle of the accelerated map C (n/2 if even, (3n+1)/2 if odd).
holds-here: true — the current best bound on m for non-trivial cycles.
evidence: proved in source (Hercher 2022, arXiv 2201.00406), building on Simons–de Weger's m ≥ 76 and the m ≥ 83 from newer verification bounds.
status: conditional
formalisation: code/lean/hercher_m92-97b13fb9.lean
formalisation-notes: lean_check compiled true, no sorrys, outcome conditional. Kernel checks hercher_m92 (every non-trivial cycle has at least 92 local minima) from the cited axiom Cited.no_m_cycle_le_91, which is Main Theorem 23 itself (multi-page Diophantine and computer-assisted argument, not re-derived here).
falsifies: a published non-trivial cycle with ≤ 91 local minima, or an error in the proof (none known).
```

```claim
id: hercher-m92-cited-axiom
statement: Cited.no_m_cycle_le_91 — for every non-trivial accelerated Collatz cycle Ω and every m with localMinimaCount Ω = m, ¬ m ≤ 91.
hypotheses: Ω is a non-trivial cycle of T (IsCycle ∧ all elements > 2); m is its local-minima count.
holds-here: true — this is exactly Main Theorem 23 of the paper, carried as a cited axiom under namespace Cited with source docstring arXiv:2201.00406v3.
evidence: proved in source (Hercher 2022); not re-derived, so the formalisation is conditional on it.
status: conditional
formalisation: code/lean/hercher_m92-97b13fb9.lean
formalisation-notes: declared as axiom no_m_cycle_le_91 in namespace Cited; #print axioms names it as the only non-standard axiom of hercher_m92.
falsifies: an error in Hercher's proof (none known).
```

```claim
id: hercher-K-1p375e11
statement: If all Collatz sequences of integers ≤ 3×2^69 = 1536×2^60 enter the trivial cycle, then every non-trivial cycle contains at least K > 1.375×10^11 odd numbers (Corollary 29).
hypotheses: verification bound X0 ≥ 1536×2^60; K = number of odd members of the cycle.
holds-here: true — reduction from verification range to cycle-length bound.
evidence: proved in source (Hercher 2022, Corollary 29); the range 3×2^69 is within Barina's verified 2075×2^60, so the hypothesis holds and the bound is live.
status: proved
falsifies: a non-trivial cycle with ≤ 1.375×10^11 odd members, or an error in the proof.
```

```claim
id: hercher-K-7p76e19
statement: Corollary 24 (Table 1): if there is an m-cycle with m ≤ 98, it consists of at least K ≥ 7.76×10^19 odd members.
hypotheses: m ≤ 98.
holds-here: true — strengthens the odd-member bound for small m.
evidence: proved in source (Hercher 2022, Corollary 24/Table 1).
status: proved
falsifies: a non-trivial cycle with ≤ 98 local minima and < 7.76×10^19 odd members.
```

<!-- source: https://arxiv.org/pdf/2201.00406 | converted from PDF -->

## What it claims

The Collatz conjecture (or “Syracuse problem”) considers recursively-deﬁned se-
quences of positive integers where n is succeeded by n
2 , if n is even, or 3n+1
2 , if n is odd.
The conjecture states that for all starting values n the sequence eventually reaches the
trivial cycle 1, 2, 1, 2, . . . . We are interested in the existence of nontrivial cycles.
Let m be the number of local minima in such a nontrivial cycle. Simons and de
Weger proved that m ≥ 76. With newer bounds on the range of starting values for
which the Collatz conjecture has been checked, one gets m ≥ 83. In this paper, we
prove m ≥ 92.
The last part of this paper considers what must be proven in order to raise the
number of odd members a nontrivial cycle has to have to the next bound—that is, to
at least K ≥ 1.375 · 1011. We prove that it suﬃces to show that, for every integer
smaller than or equal to 1536 · 260 = 3 · 269, the respective Collatz sequence enters the
trivial cycle. This reduces the range of numbers to be checked by nearly 60%.

1 Introduction

The Collatz conjecture
1 (or Syracuse problem) considers…

## Statements it makes

Conjecture 2 (Collatz). For all n ∈ Z>0, the sequence n, C(n), C 2(n) := C(C(n)), C 3(n), . . .
eventually reaches the trivial cycle 1, 2, 1, 2, . . . .

Lemma 8. Let n and k be positive integers, where n, C(n), . . . , C k−1(n) are all odd. Then
n ≡ −1 (mod 2k). In particular, n ≥ 2k − 1.
 4

Lemma 9. Let ni be an odd positive integer. Let ki be the exact number of o-steps directly
following ni in its Collatz sequence and ℓi the exact number of e-steps following them.
If ℓi ≥ 2, then the Collatz sequences of ni and n
′
i := ni−1
2 merge since C ki+2(ni) =
C ki+1(n
′
i).

Lemma 11. For all 1 ≤ i, we have
 T (ni) < 35
18 · 1
X0 or

Lemma 12. Let 0 ≤ m1 be an integer. Then

Corollary 13. For all 1 ≤ i ≤ m we have
 T (ni) < 97
54 · 1
X0 ,

Theorem 14. Let 0 ≤ m1 be an integer. Then

Theorem 16. Let K be the number of odd numbers in a given m-cycle and L be the number
of even numbers in it. Further let ki, ni and T (ni) be as in Deﬁnition 6. Then,

Corollary 17. With K, L as in Theorem 16, we have

Corollary 19. Provided that X0 ≥ 704 · 260, we have

Lemma 20. Let ni, ni+1 be two successive local minima in an m-cycle. Then we have
ni+1 < n
δ
i .

Theorem 21. Let K be the number of odd numbers in a given m-cycle, and let L be the
number of even numbers in it. Further, assume there exists a positive integer m2 with

Lemma 22. Let 0 < α < β be two real numbers with continued fraction expansions α =
[a0; a1, . . . , ak−1, ak, . . .] and β = [a0; a1, . . . , ak−1, bk, . . .]. Then every fraction in the open in-
terval (α, β) has a denominator which is not smaller than the one of γ = [a0; a1, . . . , ak−1, ck]
with ck = min(ak, bk) + 1.

Theorem 23 (Main Theorem). There is no m-cycle with m ≤ 91.

Corollary 24. In Table 1 diﬀerent pairs of values m und K are listed. If there is a m-cycle
with m equal or smaller than the given value, this cycle consists of at least the corresponding
number of K odd members.
 m K
98 7.76 · 1019

Lemma 26. For all 1 ≤ i, we have
 T (ni) < ki · 3
4 · 1
X0 ,

Theorem 27. Let K be the number of odd numbers in a given m-cycle, and let L be the
number of even numbers in it. Then

Corollary 29. If X0 ≥ 1536 · 260 = 3 · 269 then every nontrivial cycle contains at least
K > 1.375 · 1011 odd numbers.
 20

*[digest of a 41164 character source; every section, statement, and proof in full at `research/sources/hercher-no-collatz-m-cycles.full.md`]*
