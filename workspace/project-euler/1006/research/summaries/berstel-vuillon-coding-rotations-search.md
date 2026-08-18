> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/berstel-vuillon-coding-rotations-search.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://export.arxiv.org/pdf/2308.13657v1.pdf | converted from PDF -->

## What it claims

Florian Luca
School of Mathematics, University of the Witwatersrand
Private Bag 3, Wits 2050, South Africa
Research Group in Algebraic Structures and Applications
King Abdulaziz University, Jeddah, Saudi Arabia
ﬂorian.luca@wits.ac.za

Jo¨el Ouaknine
Max Planck Institute for Software Systems
Saarland Informatics Campus, Saarbr¨ucken, Germany
joel@mpi-sws.org

James Worrell
Department of Computer Science
University of Oxford, Oxford OX1 3QD, UK
jbw@cs.ox.ac.uk

Abstract
We consider numbers of the form Sβ(u) := ∑∞
n=0 un
βn for u = ⟨un⟩∞
n=0 a Sturmian sequence
over a binary alphabet and β an algebraic number with |β| > 1. We show that every such
number is transcendental. More generally, for a given base β and given irrational number θ we
characterise the Q-linear independence of sets of the form {
1, Sβ(u(1)), . . . , Sβ(u(k))}, where

u(1), . . . , u(k) are Sturmian sequences having slope θ.
We give an application of our main result to the theory of dynamical systems, showing
that for a contracted rotation on the unit circle with algebraic slope, its limit set is either
ﬁnite or…

1…

## Statements it makes

Theorem 1 (Subspace Theorem). Let S ⊆ M (K) be a ﬁnite set of places, containing all inﬁnite
places and let m ≥ 2. For every v ∈ S let L1,v, . . . , Lm,v be linearly independent linear forms in m
variables with algebraic coeﬃcients. Then for any ε > 0 the solutions x ∈ Om
S of the inequality

Proposition 2. [6, Proposition 2.3] Let f ∈ K[X] be a polynomial with at most k + 1 terms.
Assume that f can be written as the sum of two polynomials g and h, where every monomial of g
has degree at most d0 and every monomial of h has degree at least d1. Let β be a root of f that is
not a root of unity. If d1 − d0 > log(k H(f ))
log H(β) then β is a common root of g and h.

Theorem 4. Let θ ∈ (0, 1) be irrational. Given a positive integer k, let c0, . . . , ck ∈ C and
x1, . . . , xk ∈ I. Suppose that xi − xj ̸∈ Zθ + Z for all i ̸= j. Writing ⟨u(i)
n ⟩
∞
n=0 for the θ-coding of
xi, for i = 1, . . . , k, deﬁne un := c0 + ∑k
i=1 ciu(i)
n for all n ∈ N. Then u = ⟨un⟩
∞
n=0 is stuttering.

Theorem 5. Let A be a ﬁnite set of algebraic numbers and suppose that u ∈ A
ω is a stuttering
sequence. Then for any algebraic number β with |β| > 1, the sum α := ∑∞
n=0 un
βn is transcendental.

Theorem 6. Let β be an algebraic number with |β| > 1. Let 0 < θ < 1 be irrational and let

Theorem 7. Let 0 < λ, θ < 1 be such that λ is algebraic and θ is irrational. Let δ be the unique
oﬀset such that the contracted rotation fλ,δ has rotation number θ. Then every element of the limit
set Cλ,δ other than 0 and 1 is transcendental.

*[digest of a 26938 character source; every section, statement, and proof in full at `research/sources/berstel-vuillon-coding-rotations-search.full.md`]*
