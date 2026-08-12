> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/brandenburg_de_loera_meroni_best_ways_slice_polytope.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2304.14239 | converted from PDF -->

## What it claims

We study the structure of the set of all possible aﬃne hyperplane sections of a convex
polytope. We present two diﬀerent cell decompositions of this set, induced by hyperplane
arrangements. Using our decomposition, we bound the number of possible combinatorial
types of sections and craft algorithms that compute optimal sections of the polytope
according to various combinatorial and metric criteria, including sections that maximize
the number of k-dimensional faces, maximize the volume, and maximize the integral of a
polynomial. Our optimization algorithms run in polynomial time in ﬁxed dimension, but
the same problems show hardness otherwise. Our tools can be extended to intersection
with halfspaces and projections onto hyperplanes. Finally, we present several experiments
illustrating our theorems and algorithms on famous polytopes.

1 Introduction

What is the best way to slice a 3-dimensional permutahedron? Figure 1 shows three of many
possible “best slices”. In this article we give a ﬁnite description of all aﬃne hyperplane
sections of an arbitrary polytope, called slices, and…

(…

## Statements it makes

Theorem 1.1. Given a polytope P ⊂ Rd, there exist two diﬀerent parametric decompositions
of the space of all aﬃne hyperplanes in Rd into ﬁnitely many cells, called slicing chambers.
Each decomposition is organized by a pair (R, C) of arrangements (cf. Table 1), where each
region of R deﬁnes a parametric hyperplane arrangement C. The following holds for slicing
chambers in both decompositions:

Theorem 1.2. For d-dimensional polytopes with n vertices, an upper bound on the number
of combinatorial types of hyperplane sections is O(n2d+12d).

Theorem 1.3. Let P ⊂ Rd be a polytope and f (x) a polynomial in Q[x1, . . . , xd]. Denote by
fk(P ) the number of k-dimensional faces of P and let wk+1 be a weight function deﬁned on
all (k + 1)-dimensional faces F of P . Let H be an aﬃne hyperplane, H +
0 denote a halfspace
deﬁned by a central hyperplane, and πH denote the projection of P in the direction orthogonal
to H. We give algorithms to ﬁnd an optimal solution for the following problems:

Lemma 2.1 ([BBMS22, Lemma 2.4]). Let P be a full-dimensional polytope in Rd and consider
the central hyperplane arrangement

Lemma 2.3 ([LA01, Theorem 2.1],[BBDL+11, Remark 9]). Let ∆ = conv(s1, . . . , sn) ⊂ Rd

Lemma 2.4 ([BBDL+11, Equation 13]). Any monomial can be written as a sum of powers
of linear forms of the same degree as follows:

Theorem 2.5. Let P ⊂ Rd be a full-dimensional polytope, let f (x) = ∑
α cαxα be a polyno-
mial, and let C ⊂ Rd be a maximal open slicing chamber of the central hyperplane arrangement
C⟲(P ) from Lemma 2.1. Restricted to directions u ∈ C ∩ Sd−1, the integral ∫

Lemma 2.8. Let P ⊂ Rd be a polytope and ﬁx a direction u ∈ Sd−1. Consider the aﬃne
hyperplane arrangement, made of parallel hyperplanes

Theorem 2.12. Let P ⊂ Rd be a full-polytope, let f (x) = ∑
α cαxα be a polynomial, ﬁx
a normal direction u ∈ Sd−1 and let C ⊂ Rd be a maximal open chamber of the hyperplane
arrangement Cu
↑ (P ) from Lemma 2.8. Restricted to values β ∈ C, the integral ∫
P ∩H(β) f (x) dx
is a polynomial in the variable β.

Theorem 2.14. The Ehrhart function Ehr(P ∩H(β)) that counts lattice points of dilations of
polytopes is a piecewise rational function in β. In ﬁxed dimension and for a rational polytope
P , these formulas can be computed in polynomial time.

Lemma 2.17. Let P ⊂ Rd be a polytope containing the origin in its interior and let P ◦

Theorem 2.18. Let P ⊂ Rd be a full-dimensional polytope, let f (x) = ∑
α cαxα be a poly-
nomial, and let C ⊂ Rd be a maximal open chamber of the hyperplane arrangement C⟲(P ◦) in
Lemma 2.17. Restricted to directions u ∈ C ∩Sd−1, the integral ∫

Lemma 3.1 ([BM23, Lemma 3.2, Proposition 3.4]). Let P ⊂ Rd be a full-dimensional polytope
and let R be a maximal region of the aﬃne hyperplane arrangement

Proposition 3.3. Let P ⊂ Rd be a polytope with n vertices. In the cocircuit arrangement
R⟲(P ) there are at most (n
d)…

T…


*[further statements in the full text]*

*[digest of a 100968 character source; every section, statement, and proof in full at `research/sources/brandenburg_de_loera_meroni_best_ways_slice_polytope.full.md`]*
