> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/lagarias-3x1-overview.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

```claim
id: lagarias-W1
statement: (W1) The 3x+1 conjecture has been verified for all n < 20 × 2^58 ≈ 5.7646 × 10^18 (Oliveira e Silva).
hypotheses: n positive integer < 20×2^58.
holds-here: true at the time of writing (2010 overview); superseded by Barina's 2^71 (2025).
evidence: asserted by Lagarias overview, Section 6.1 (W1), citing Oliveira e Silva's chapter in The Ultimate Challenge.
status: asserted-by-source
falsifies: a counterexample below 20×2^58, or a primary source giving a different record.
```

```claim
id: lagarias-W2
statement: (W2) The trivial cycle {1,2} is the only cycle of the 3x+1 function on the positive integers having period length less than 10,439,860,591; it is also the only cycle containing less than 6,586,818,670 odd integers (Eliahou 1993, Theorem 3.2).
hypotheses: cycle on positive integers under the accelerated map T (n/2 if even, (3n+1)/2 if odd).
holds-here: true — the cycle-exclusion bound from Eliahou's continued-fraction method; the value (21,0) in Eliahou's Table 2, smaller values ruled out by later verification (W1).
evidence: asserted by Lagarias overview Section 6.1 (W2) with footnote, citing Eliahou [24, Theorem 3.2]; full method in Eliahou 1993.
status: asserted-by-source
falsifies: a published non-trivial cycle of period < 10,439,860,591.
```

```claim
id: lagarias-W3
statement: (W3) Infinitely many positive integers n take at least 6.143 log n steps to reach 1 under the 3x+1 function T (Applegate–Lagarias).
hypotheses: none.
holds-here: true — lower bound on total stopping time for infinitely many n.
evidence: asserted by Lagarias overview Section 6.1 (W3), citing Applegate and Lagarias, Math. Comp. 72 (2003), 1035-1049.
status: asserted-by-source
falsifies: a published proof that the constant can be raised (which would replace it, not falsify).
```

```claim
id: lagarias-W5
statement: (W5) The number of integers 1 ≤ n ≤ X that iterate to 1 is at least X^0.84, for all sufficiently large X (Krasikov–Lagarias).
hypotheses: X sufficiently large.
holds-here: true — unconditional lower bound on the count of n reaching 1.
evidence: asserted by Lagarias overview Section 6.1 (W5) and Section 8, citing Krasikov and Lagarias.
status: asserted-by-source
falsifies: a published proof raising the exponent (replaces it) or a counterexample.
```

```claim
id: lagarias-counterexample-structure
statement: Structure of a counterexample: either (a) an orbit diverges to infinity (unbounded trajectory), or (b) an orbit enters a non-trivial cycle other than {1,2}. Both are open; no known method approaches either.
hypotheses: none — this is the exact two-part structure of the open case.
holds-here: true — the fundamental dichotomy of the problem.
evidence: Lagarias overview, Section 6.1 and Section 7 (two fundamental difficulties: proving pseudo-randomness rules out divergent trajectories; ruling out enormously long non-trivial cycles).
status: asserted-by-source
falsifies: a proof of the conjecture (would close both) or a counterexample.
```

```claim
id: lagarias-2adic-ergodic
statement: The 3x+1 map extends to the 2-adic integers Z_2 where it is ergodic (topologically and metrically conjugate to the shift), so the parity of iterates is a 'coin flip' random variable; the difficulty is the restriction to Z ⊂ Z_2, a dense measure-zero subset where no non-random regularity is known.
hypotheses: the 2-adic extension; ergodic theory of the shift.
holds-here: true — explains why average-case control does not touch the conjecture.
evidence: Lagarias overview, Section 6.3; Terras 1976 and Everett 1977 for the invariant measure.
status: asserted-by-source
falsifies: a proof that Z retains the mixing property in a quantitative form that implies convergence.
```

<!-- source: https://arxiv.org/pdf/2111.02635 | converted from PDF -->

Reference. The Ultimate Challenge: The 3x + 1 Problem. Edited by Jeﬀrey C.
Lagarias. American Mathematical Society, Providence, RI, 2010, pp. 3–29.

THE 3x + 1 PROBLEM: AN OVERVIEW

JEFFREY C. LAGARIAS

1. Introduction

The 3x+1 problem concerns the following innocent seeming arithmetic procedure
applied to integers: If an integer x is odd then “multiply by three and add one”,
while if it is even then “divide by two”. This operation is described by the Collatz
function
 C(x) =
 



 3x + 1 if x ≡ 1 (mod 2),

x
2 if x ≡ 0 (mod 2).

The 3x + 1 problem, which is often called the Collatz problem, concerns the behavior
of this function under iteration, starting with a given positive integer n.
3x+1 Conjecture. Starting from any positive integer n, iterations of the function
C(x) will eventually reach the number 1. Thereafter iterations will cycle, taking
successive values 1, 4, 2, 1, ....
This problem goes under many other names, including the Syracuse problem,
Hasse’s algorithm, Kakutani’s problem and Ulam’s problem.
A commonly used reformulation of the 3x+1 problem iterates a diﬀerent function,
the 3x + 1 function, given by

T (x) =
 



 3x + 1
2 if x ≡ 1 (mod 2),

x
2 if x ≡ 0 (mod 2).

From the viewpoint of iteration the two functions are simply related; iteration of
T (x) simply omits some steps in the iteration of the Collatz function C(x). The
relation of the 3x + 1 function T (x) to the Collatz function C(x) is that:

T (x) =
 



 C(C(x)) if x ≡ 1 (mod 2) ,

C(x) if x ≡ 0 (mod 2) .

As it turns out, the function T (x) proves more convenient for analysis of the problem
in a number of signiﬁcant ways, as ﬁrst observed independently by Riho Terras ([88],
[89]) and by C. J. Everett [27].
The 3x+1 problem has fascinated mathematicians and non-mathematicians alike.
It has been studied by mathematicians, physicists, and computer scientists. It
remains an unsolved problem, which appears to be extremely diﬃcult.
1arXiv:2111.02635v1  [math.NT]  4 Nov 2021
2 JEFFREY C. LAGARIAS

This paper aims to address two questions:

(1) What can mathematics currently say about this problem?

(2) How can this problem be hard, when it is so easy to state?

To address the ﬁrst question, this overview discusses the history of work on the
problem. Then it describes generalizations of the problem, and lists the diﬀerent
ﬁelds of mathematics on which the problem impinges. It gives a brief summary of
the current strongest results on the problem.

Besides the results summarized here, this volume contains more detailed surveys
of mathematicians’ understanding of the 3x + 1 problem and its generalizations.
These cover both rigorously proved results and heuristic predictions made using
probabilistic models. The book includes several survey articles, it reprints several
early papers on the problem, with commentary, and it presents an annotated bibli-
ography of work on the problem and its generalizations.

To address the second question, let us remark ﬁrst that the true level of diﬃculty
of any problem can only be determined when (and if) it is solved. Thus there can be
no deﬁnitive answer regarding its diﬃculty. The track record on the 3x+1 problem so
far suggests that this is an extraordinarily diﬃcult problem, completely out of reach
of present day mathematics. Here we will only say that part of the diﬃculty appears
to reside in an inability to analyze the pseudorandom nature of successive iterates
of T (x), which could conceivably encode very diﬃcult computational problems. We
elaborate on this answer in §7.

Is the 3x + 1 problem an important problem? Perhaps not for its individual sake,
where it merely stands as a challenge. It seems to be a prototypical example of
an extremely simple to state, extremely hard to solve, problem. A middle of the
road viewpoint is that this problem is representative of a large class of problems,

*[excerpt ends; 81157 characters not shown — see `research/sources/lagarias-3x1-overview.full.md`]*
