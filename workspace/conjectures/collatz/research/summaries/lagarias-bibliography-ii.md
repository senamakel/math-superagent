> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/lagarias-bibliography-ii.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/math/0608208 | converted from PDF -->

arXiv:math/0608208v6  [math.NT]  12 Feb 2012
The 3x + 1 Problem: An Annotated Bibliography, II
(2000-2009)

J. C. Lagarias
Department of Mathematics
University of Michigan
Ann Arbor, MI 48109–1109
lagarias@umich.edu

(Jan. 10, 2012)

ABSTRACT. The 3x + 1 problem concerns iteration of the map T : Z → Z given by

T (x) =
 



 3x + 1
2 if x ≡ 1 (mod 2) .

x
2 if x ≡ 0 (mod 2) .

The 3x + 1 Conjecture asserts that each m ≥ 1 has some iterate T (k)(m) = 1. This is the
second installment of an annotated bibliography of work done on the 3x+1 problem and related
problems, mainly covering the period 2000 through 2009, with some related later papers (which
were preprints by 2009). At present the 3x + 1 Conjecture remains unsolved.

1. Introduction

The 3x + 1 problem is most simply stated in terms of the Collatz function C(x) deﬁned
on integers as “multiply by three and add one” for odd integers and “divide by two” for even
integers. That is,
 C(x) =
 



 3x + 1 if x ≡ 1 (mod 2) ,

x
2 if x ≡ 0 (mod 2) ,

The 3x + 1 problem (or Collatz problem) is to prove that starting from any positive integer,
some iterate of this function takes the value 1. The problem other names: it has also been
called Kakutani’s problem, the Syracuse problem, and Ulam’s problem.
Much work on the problem is stated in terms of the 3x + 1 function

T (x) =
 



 3x + 1
2 if x ≡ 1 (mod 2)

x
2 if x ≡ 0 (mod 2) .

The 3x + 1 Conjecture states that every m ≥ 1 has some iterate T (k)(m) = 1.
The 3x + 1 Conjecture has now been veriﬁed up to 17 × 258 > 4.899 × 1018 (as of Feb.
21, 2008) by an ongoing computation run by T. Oliveira e Silva (2004+). An independent
computation of Roosendaal(2004+) veriﬁes it to 612 × 250 > 6.89 × 1017.

1

At present the 3x + 1 conjecture remains unsolved. The proofs claimed in Yamada (1981),
Cadogan (2006) and Bruckman (2008) are incomplete.
Surveys on results on the 3x + 1 problem can be found in Lagarias (1985), M¨uller (1991),
and the ﬁrst chapter of Wirsching (1998a), described in the ﬁrst installment of the annotated
bibliography, Lagarias (2003+). A more recent survey appears in Chamberland (2003).

2. Terminology

We use the following deﬁnitions. The trajectory or foward orbit of an integer m is the set

O+(m) := {m, T (m) , T (2)(m), . . .} .

The stopping time σ(m) of m is the least k such that T (k)(m) < m, and is ∞ if no such k exists.
The total stopping time σ∞(m) is the least k such that m iterates to 1 under k applications
of the function T i.e. σ∞(m) := inf {k : T (k)(m) = 1}.

The scaled total stopping time or gamma value γ(m) is given by

γ(m) := σ∞(m)
log m .

The height h(m) is the least k for which the Collatz function C(x) has C (k)(m) = 1. It is also
given by h(m) := σ∞(m) + d(m),

where d(m) counts the number of iterates T (k)(m) ≡ 1 (mod 2) for 0 ≤ k < σ∞(m). Finally,
the function πa(x) counts the number of n with |n| ≤ x that contain a in their forward orbit
under T .

3. Bibliography

This bibliography covers research articles, survey articles and PhD theses on the 3x + 1
problem and related problems from 2000 to the present. The ﬁrst installment of the annotated
bibliography is Lagarias(2003+), which covers the period 1963–1999. Articles in Chinese have
the authors surname listed ﬁrst.

1. Ethan Akin (2004), Why is the 3x + 1 Problem Hard?, In: Chapel Hill Ergodic Theory
Workshops (I. Assani, Ed.), Contemp. Math. vol 356, Amer. Math. Soc. 2004, pp.
1–20. (MR 2005f:37031).

This paper analyzes the 3x + 1 problem by viewing the map T as acting on the
domain Z2 of 2-adic integers. The map T is topologically conjugate over Z2 to the 2-adic
shift map
 S(x) =
 



 x − 1
2 if x ≡ 1 (mod 2) ,

x
2 if x ≡ 0 (mod 2) ,

2

by a conjugacy map Q3 : Z2 → Z2, i.e. Q3 ◦ T = S ◦ Q3. (The map Q3 equals the map
denoted Q∞ in Lagarias (1985), and is the inverse of the map Φ in Bernstein (1994).)

*[excerpt ends; 117387 characters not shown — see `research/sources/lagarias-bibliography-ii.full.md`]*
