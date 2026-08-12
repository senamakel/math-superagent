> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/arjunbalaji-zenodo-pdf.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://zenodo.org/records/21190438/files/erdos-gyarfas-ieee.pdf?download=1 | converted from PDF -->

SUBMITTED TO IEEE ACCESS 1

Verifying the Erdős–Gyárfás Conjecture up to 31
Vertices with SAT Modulo Symmetries

Arjun Balaji

Abstract—Boolean satisfiability (SAT) solvers have resolved
a series of longstanding combinatorial problems, yet many
well-known conjectures have never been attacked with modern
automated-reasoning tools. We present the first SAT-based
attack on the Erdős–Gyárfás conjecture (1995), which asserts
that every graph of minimum degree at least 3 contains a
cycle whose length is a power of two. The conjecture is open;
prior computer search established that any general minimum-
degree-3 counterexample has at least 17 vertices (Royle and
Markström), and any cubic (3-regular) counterexample at least
30 (Markström, 2004). Using SAT Modulo Symmetries (SMS),
which performs complete isomorph-free graph generation inside
a CDCL solver, with the Glasgow subgraph solver as a complete
forbidden-subgraph propagator, we verify that every minimum-
degree-3 graph on at most 31 vertices contains a cycle of
length 4, 8, or 16, settling the entire range in which these are
the only admissible power-of-two cycle lengths. Consequently
any general minimum-degree-3 counterexample has at least 32
vertices, improving the two-decade-old general bound from 17
to 32 and the cubic bound from 30 to 32. Each order up to 31
is decided in at most about two hours on a single CPU core,
whereas a conventional CEGAR baseline stalls near order 20.
We corroborate the result with an exact ground-truth check
against nauty at n = 10, reproduction of the n ≤ 16 baseline,
agreement with the independent CEGAR solver for n ≤ 19,
and robustness across cardinality encodings and symmetry-
breaking methods, and we release the complete reproducible
pipeline.

Index Terms—Automated reasoning, Boolean satisfiability,
combinatorics, constraint propagation, Erdős–Gyárfás conjec-
ture, graph generation, symmetry breaking.

I. Introduction
S AT solvers have become a standard instrument for set-
tling hard combinatorial questions: celebrated exam-
ples include the Boolean Pythagorean triples problem [1],
Schur number five [2], and Keller’s conjecture [3], each
resolved by encoding the question into propositional logic
and letting a conflict-driven solver exhaust the search
space. A newer line of work, SAT Modulo Symmetries
(SMS) [15], [16], extends this instrument to graph exis-
tence questions: it augments a CDCL solver with an in-
search canonicity propagator so that the solver enumerates
exactly one representative per isomorphism class, making
exhaustive isomorph-free search feasible at orders far
beyond explicit enumeration. In this paper we apply SMS
to a well-known open conjecture of Erdős and Gyárfás that,
to our knowledge, has never been attacked with SAT-based
or constraint-programming methods.

A. Balaji is with Columbia University, New York, NY, USA (e-mail:
ab6136@columbia.edu). ORCID: 0009-0005-1790-0034.
 In 1995 Erdős and Gyárfás posed the following conjec-
ture (see Erdős [4]); Erdős offered $100 for a proof and
$50 for a counterexample [5].
Conjecture 1 (Erdős–Gyárfás): Every graph with mini-
mum degree at least 3 contains a simple cycle whose length
is a power of two.
The conjecture is open. It has been confirmed for
restricted classes, including K1,m-free graphs [9], planar
claw-free graphs [10], 3-connected cubic planar graphs [8],
and the Pt-free families P8 [11], P10 [12], and (with the aid
of a computer search assisting a structural proof) P13 [13].
These are theorems for infinite hereditary classes and do
not bound the order of a general counterexample. Carr [14]
recently showed that at least 4/7 of the vertices of any
minimal counterexample have degree exactly 3.
Computationally, two frontiers were known, and the
distinction is central to this paper. Write δ(G) for the
minimum degree of G.


*[excerpt ends; 16906 characters not shown — see `research/sources/arjunbalaji-zenodo-pdf.full.md`]*
