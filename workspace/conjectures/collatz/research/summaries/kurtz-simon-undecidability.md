> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/kurtz-simon-undecidability.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

```claim
id: kurtz-simon-pi02
statement: The generalized Collatz problem is Π^0_2-complete (recursively undecidable): given a generalized Collatz function g, it is undecidable whether g^i(x) = 1 for all positive integers x. The specific Collatz function itself is NOT shown undecidable.
hypotheses: g ranges over generalized Collatz functions (piecewise affine on residue classes mod m with rational coefficients, admissible).
holds-here: true for the generalization; does NOT apply to the specific 3x+1 function.
evidence: proved in source (Kurtz–Simon 2006/2007), building on Conway 1972; full proof via register-machine double simulation.
status: proved
falsifies: a proof that the specific 3x+1 function's iteration problem is decidable (would be a result, not a falsification), or a counterexample to the Π^0_2-completeness proof.
```

```claim
id: conway-1972-unsolvable
statement: Conway (1972) exhibited an unsolvable iteration problem for a particular generalized 3x+1 function: deciding whether some iterate of the map applied to a positive integer is a power of 2.
hypotheses: the specific generalized function Conway constructed.
holds-here: true — establishes that generalized Collatz-type iteration problems can be undecidable.
evidence: asserted in Kurtz–Simon (citing Conway 1972) and in Lagarias overview Section 5(4)/Section 7.
status: asserted-by-source
falsifies: an error in Conway's construction (none known).
```

<!-- source: http://people.cs.uchicago.edu/~simon/RES/collatz.pdf | converted from PDF -->

## What it claims

The Collatz problem, widely known as the 3x + 1 problem, asks
whether or not a certain simple iterative process halts on all inputs.
We build on earlier work by J. H. Conway, and show that a natural
generalization of the Collatz problem is recursively undecidable.

1 Introduction

Deﬁne the function g : ω → ω as follows:

g(x) = { x/2, if n is even;
3x + 1, if n is odd.

Let g(i) denote the i-th iterate of g, i.e.,

g(i)(x) =
 i
︷ ︸︸ ︷
g(g(. . . g(x) . . .))

The Collatz problem asks

Problem 1.1 For all integers x > 0, is there is an i such that g(i)(x) = 1.

1

Because of its tantalizingly elementary form, and our inability to settle
it the Collatz problem has received substantial attention. Collatz started
working on the problem in 1928, but, since he felt he made little progress,
only published a history of its origin in 1986 [?]. There is a very extensive
literature on the many attempts to settle the conjecture, as well as related
questions, using an arsenal of technologies from Number Theory, to Dynam-
ical Systems, and Markov Chains: there is a 47-page annotated bibliography…

## Statements it makes

Theorem 1.4 Given a Collatz function g, it is undecidable whether or not
for all integers x there exists an i such that g(i)(x) = 1.

Theorem 1.5 The problem is range − g() = ω} is Π2complete.

Theorem 1.6 Given a Collatz function g, it is undecidable whether or not
for all integers x of the form 2k, there exists an i such that g(i)(x) = 1.

Theorem 2.1 A function ϕ is partial recursive if and only if there is a
register machine M such that ϕ = ψM .

Theorem 2.2 It suﬃces to consider register machines having only two reg-
isters, i.e., every register machine can be eﬀectively converted into a register
machine computing the same function which has only two registers.

Theorem 2.3 A register machine M can be eﬀectively converted into a
register machine M ′ such that M is total if and only if M ′ reaches a halting
conﬁguration from every conﬁguration.

*[digest of a 8656 character source; every section, statement, and proof in full at `research/sources/kurtz-simon-undecidability.full.md`]*
