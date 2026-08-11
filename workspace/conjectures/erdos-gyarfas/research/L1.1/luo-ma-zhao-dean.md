> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/L0.0/luo-ma-zhao-dean.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2601.13552 | converted from PDF -->

## What it claims

Dean conjectured three decades ago that every graph with minimum degree at least k ≥ 3
contains a cycle whose length is divisible by k. While the conjecture has been verified for
k ∈ {3, 4}, it remains open for k ≥ 5. A weaker version, also proposed by Dean, asserting
that every k-connected graph contains a cycle of length divisible by k, was resolved by Gao,
Huo, Liu, and Ma [16] using the notion of admissible cycles.
In this paper, we resolve Dean’s conjecture for all k ≥ 6. In fact, we prove a stronger
result by showing that every graph with minimum degree at least k contains cycles of length
r (mod k) for every even integer r, unless every end-block belongs to a specific family of
exceptional graphs, which fail only to contain cycles of length 2 (mod k). We also estab-
lish a strengthened result on the existence of admissible cycles. Our proof introduces two
sparse graph families, called trigonal graphs and tetragonal graphs, which provide a flexible
framework for studying path and cycle lengths and may be of independent interest.

1 Introduction

The study of cycle lengths in…

## Statements it makes

Conjecture 1.1 (Dean’s conjecture). For every integer k ≥ 3, every graph with minimum degree
at least k contains a cycle of length divisible by k.

Theorem 1.2 (Main Theorem). For every integer k ≥ 6, let G be a graph with minimum degree
at least k. Then exactly one of the following holds:

Corollary 1.3. Let k ≥ 6 be an integer. Then for every even integer r ̸≡ 2 (mod k), every
graph with minimum degree at least k contains a cycle of length r (mod k).

Theorem 1.4. Let k ≥ 7 and let G be a graph with minimum degree at least k. Then G contains
k admissible cycles, unless every end-block of G is isomorphic to a graph in {Kk+1, Kk,k} ∪ Hk.

Definition 2.1. A set of integers is called consecutive (resp. admissible) if its elements form
a 1-AP (resp. 1-AP or 2-AP). A family of paths or cycles in a graph G is called consecutive
(resp. admissible) if the set of their lengths is consecutive (resp. admissible).

Lemma 2.3. ([8]) Let k be a positive integer. If (G, x, y) is a 2-connected rooted graph with
|G| ≥ 4 and δ2(G, x, y) ≥ k + 1, then there exist k admissible (x, y)-paths in G.

Theorem 2.4. ([8]) For any integer k ≥ 2, every graph G on at least three vertices, having at
most two vertices of degree less than k + 1, contains k admissible cycles.

Lemma 2.5. Let C be a cycle of length s ≥ 3 in graph G, and let u1, u2 ∈ V (G − C) be two
distinct vertices such that degC(u1) > 0 and degC(u2) > 0. If neither NC(u1) nor NC(u2)
contains two consecutive vertices of C, then the following statements hold.

Definition 3.1 (Trigonal graph). A trigonal graph T is a non-bipartite outer-planar graph
equipped with a Hamiltonian cycle ∂T , defined as the final graph Tn (with ∂T = ∂Tn) of a finite
sequence of trigonal graphs T3, T4, . . . , Tn that satisfies the following properties:

Proposition 3.2. Let T be a trigonal graph with |T | = t, and let u, v be two distinct vertices
of V (T ) with dist∂T (u, v) = d, then [d, t − d] ⊆ LT
u,v. In particular, if uv ∈ E(∂T ), then
[1, t − 1] ⊆ LT
u,v.

Definition 3.4 (Tetragonal graph). A tetragonal graph T is a bipartite outer-planar graph
equipped with a Hamiltonian cycle ∂T , defined as the final graph Tn (with ∂T = ∂Tn) of a finite
sequence of tetragonal graphs T2, T3, · · · , Tn satisfying the following properties:

Proposition 3.5. Let T be a tetragonal graph with |T | = 2m, and let u, v be two distinct vertices
of T with dist∂T (u, v) = d. Then {d, d + 2, . . . , 2m − d} ⊆ LT
u,v.

Definition 3.6. We say that T is an optimal tetragonal subgraph of a bipartite graph G if the
following conditions hold.

Lemma 3.7. Let T be an optimal tetragonal subgraph of a bipartite graph G. If |T | = 2m ≥ 6,
then the following hold:

Definition 4.1. Let k ≥ 3 be an integer. A graph G is k-weak if one of the following holds:

Theorem 4.2. Let k ≥ 6 be an integer. If G is a k-weak graph not isomorphic to any graph in
{Kk+1, Kk,k} ∪ Hk,…


*[further statements in the full text]*

*[digest of a 109086 character source; every section, statement, and proof in full at `research/L0.0/luo-ma-zhao-dean.full.md`]*
