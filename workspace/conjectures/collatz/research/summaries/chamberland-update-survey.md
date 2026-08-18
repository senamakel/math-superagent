> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/chamberland-update-survey.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.math.grinnell.edu/~chamberl/papers/3x_survey_eng.pdf | converted from PDF -->

An Update on the 3x+1 Problem

Marc Chamberland

Department of Mathematics and Computer Science

Grinnell College, Grinnell, IA, 50112, U.S.A.

E-mail: chamberl@math.grinnell.edu

Contents

1 Introduction 2

2 Numerical Investigations and Stopping Time 3

2.1 Stopping Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.2 Total Stopping Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.3 The Collatz Graph and Predecessor Sets . . . . . . . . . . . . . . . . . . . . . . 9

3 Representations of Iterates of a 3x + 1 Map 12

4 Reduction to Residue Classes and Other Sets 13

5 Cycles 15

6 Extending T to Larger Spaces 17

6.1 The Integers ZZ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

6.2 Rational Numbers with Odd Denominators . . . . . . . . . . . . . . . . . . . . 18

6.3 The Ring of 2-adic Integers ZZ2 . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

6.4 The Gaussian Integers and ZZ2[i] . . . . . . . . . . . . . . . . . . . . . . . . . . 20

6.5 The Real Line lR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

6.6 The Complex Plane lC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

7 Generalizations of 3x + 1 Dynamics 23

8 Miscellaneous 25

AMS subject classiﬁcation : 11B83.

Key Words. 3x + 1 problem, Collatz conjecture.

Running title: 3x + 1 survey.
 1
 2

1 Introduction

The 3x+1 Problem is perhaps today’s most enigmatic unsolved mathematical

problem: it can be explained to child who has learned how to divide by 2

and multiply by 3, yet there are relatively few strong results toward solving it.

Paul Erd¨os was correct when he stated, “Mathematics is not ready for such

problems.”

The problem is also referred to as the 3n + 1 problem and is associated with

the names of Collatz, Hasse, Kakutani, Ulam, Syracuse, and Thwaites. It may

be stated in a variety of ways. Deﬁning the Collatz function as

C(x) =
  3x + 1 x ≡ 1 (mod 2)

x

2 x ≡ 0 (mod 2),

the conjecture states that for each m ∈ ZZ+, there is a k ∈ ZZ+ such that

C (k)(m) = 1, that is, any positive integer will eventually iterate to 1. Note that

an odd number m iterates to 3m + 1 which then iterates to (3m + 1)/2. One

may therefore “compress” the dynamics by considering the map

T (x) =
 
 3x+1

2 x ≡ 1 (mod 2)

x
2 x ≡ 0 (mod 2).

The map T is usually favored in the literature.

To a much lesser extent some authors work with the most dynamically

streamlined 3x + 1 function, F : ZZ+dd → ZZ+dd, deﬁned by

F (x) = 3x + 1

2m(3x+1)

where m(x) equals the number of factors of 2 contained in 3x+1. While working

with F allows one to work only on the odd positive integers, the variability of

m seems to prohibit any substantial analysis.

This survey reﬂects the author’s view of how work on this problem can

be structured. I owe a huge debt to Jeﬀ Lagarias and G¨unther Wirsching for

the important work they have done in bringing this problem forward. The

paper of Lagarias[45](1985) thoroughly catalogued earlier results, made copious
 3

connections, and developed many new lines of attack; it has justly become the

classical reference for this problem. Wirsching’s book [87](1998) begins with

a strong survey, followed by several chapters of his own noteworthy analysis.

Lagarias has also maintained an annotated bibliography [48](1998) of work on

this problem, another valuable resource. This current survey would have been

much more diﬃcult to write in the absence of these signiﬁcant contributions.

This survey is not meant to be exhaustive, but rather is complementary to

the work of Lagarias and Wirsching. Where I believed there was signiﬁcant new

work in a given area, I included earlier contributions for the sake of completeness.

Some areas which have not seen recent development, such as the interesting


*[excerpt ends; 46641 characters not shown — see `research/sources/chamberland-update-survey.full.md`]*

```claim
id: chamberland-cycle-sum
statement: For any cycle Ω of the accelerated map T, Σ_{x∈Ω_even} x = Σ_{x∈Ω_odd} x + |Ω_odd| (rearranging Σ_{x∈Ω} x = Σ_{x∈Ω} T(x)). (Chamberland 1999, Monks 2002)
hypotheses: Ω a cycle of T; Ω_odd, Ω_even the odd/even terms.
holds-here: true — an exact structural identity for cycles.
evidence: asserted in source (Chamberland update survey, Section 5, citing Chamberland 1999 and Monks 2002).
status: asserted-by-source
falsifies: a cycle violating the identity (impossible if the algebra is right — a checkable identity).
```

```claim
id: davison-circuit-equation
statement: A circuit (cycle of k odd elements followed by l even elements) of the 3x+1 map corresponds one-to-one with solutions (k, l, h) in positive integers of (2^{k+l} − 3^k) h = 2^l − 1 (Davison 1976). The only solution is (1,1,1), so {1,2} is the only circuit (Steiner 1977, Rozier 1990).
hypotheses: circuit = cycle writable as k odd then l even elements.
holds-here: true — the fundamental circuit equation and its only solution.
evidence: asserted in source (Chamberland update survey, Section 5, citing Davison 1976, Steiner 1977, Rozier 1990).
status: asserted-by-source
falsifies: a non-trivial circuit (a cycle of the prescribed form), which would contradict the only-solution claim.
```

```claim
id: eliahou-cycle-formula
statement: For any non-trivial cycle Ω of the accelerated map with odd terms Ω_0 and m, M the smallest and largest terms, log_2(3 + 1/M) ≤ |Ω|/|Ω_0| ≤ log_2(3 + 1/m). Combined with Diophantine approximation of log_2 3 and the bound m > 2^40, Eliahou (1993) derives |Ω| = 301994a + 17087915b + 85137581c with a,b,c nonnegative integers, b ≥ 1, ac = 0.
hypotheses: Ω a non-trivial cycle of T; m = min, M = max element; verification m > 2^40 at the time.
holds-here: true — the exact structural formula and the ratio bound behind the 17,087,915 cycle-length bound.
evidence: asserted in source (Chamberland update survey, Section 5, citing Eliahou 1993).
status: asserted-by-source
falsifies: a non-trivial cycle whose length is not of that form, or an error in the derivation (the formula is checkable).
```

```claim
id: tempkin-arteaga-cycle-formula
statement: Tightening Eliahou's relations with a better lower bound on m, Tempkin and Arteaga (1997) derived |Ω| = 187363077a + 272500658b + 357638239c with a,b,c ≥ 0, b ≥ 1, ac = 0 — giving cycle length ≥ 272,500,658.
hypotheses: same as Eliahou's but with stronger verification bound on m.
holds-here: true — the sharpened cycle-length lower bound.
evidence: asserted in source (Chamberland update survey, Section 5, citing Tempkin and Arteaga 1997).
status: asserted-by-source
falsifies: a non-trivial cycle of length < 272,500,658.
```

```claim
id: brox-finitely-many-cycles
statement: Brox (2000) proved there are finitely many cycles with σ_1 < 2 log(σ_1 + σ_3), where σ_i = number of terms in a cycle congruent to i mod 4.
hypotheses: σ_i counts terms congruent to i mod 4 in a cycle.
holds-here: true — a finiteness result for cycles with few descents.
evidence: asserted in source (Chamberland update survey, Section 5, citing Brox 2000).
status: asserted-by-source
falsifies: an infinite family of cycles satisfying the inequality.
```

```claim
id: bohmsontacchi-cycle-formula
statement: x ∈ Z^+ is in an n-cycle of T if and only if there are integers 0 ≤ v_0 ≤ v_1 ≤ ⋯ ≤ v_m = n such that x = (1/(2^n − 3^m)) Σ_{k=0}^{m−1} 3^{m−k} 2^{v_k} (Böhm and Sontacchi 1978).
hypotheses: T the accelerated 3x+1 map; n-cycle = cycle with n total steps.
holds-here: true — the exact parametric characterization of cycle elements.
evidence: asserted in source (Chamberland update survey, Section 5, citing Böhm and Sontacchi 1978).
status: asserted-by-source
falsifies: an element of a cycle failing the representation, or an x of that form not lying on a cycle (a checkable identity).
```
