> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/L0.1/liu-montgomery-odd-cycle.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2010.15802 | converted from PDF -->

## What it claims

In 1981, Erd˝os and Hajnal asked whether the sum of the reciprocals of the odd cycle lengths
in a graph with inﬁnite chromatic number is necessarily inﬁnite. Let C(G) be the set of cycle
lengths in a graph G and let Codd(G) be the set of odd numbers in C(G). We prove that, if
G has chromatic number k, then ∑ℓ∈Codd(G) 1/ℓ ≥ (1/2 − ok(1)) log k. This solves Erd˝os and
Hajnal’s odd cycle problem, and, furthermore, this bound is asymptotically optimal.
In 1984, Erd˝os asked whether there is some d such that each graph with chromatic number
at least d (or perhaps even only average degree at least d) has a cycle whose length is a power
of 2. We show that an average degree condition is suﬃcient for this problem, solving it with
methods that apply to a wide range of sequences in addition to the powers of 2.
Finally, we use our methods to show that, for every k, there is some d so that every graph
with average degree at least d has a subdivision of the complete graph Kk in which each edge
is subdivided the same number of times. This conﬁrms a conjecture of Thomassen from 1984.

1 Introduction

## Statements it makes

Theorem 1.1. There is d0 > 0 such that the following holds. If G is a graph with average degree
d ≥ d0, then, there is some ℓ ≥ d/(10 log12 d) such that C(G) contains every even integer in
[log8 ℓ, ℓ].

Corollary 1.2. If a graph G has average degree d, then

Corollary 1.3. There is some d0 > 0 such that the following holds. Given any inﬁnite sequence
σi, i ∈ N, of increasing even integers with σi+1 ≤ exp(σ1/10
i ) for each i ∈ N, any graph G with
average degree at least max{d0, σ2
1} has some i ∈ N with σi ∈ C(G).

Theorem 1.4. For each ε > 0, there is some k0 ∈ N such that the following holds for each k ≥ k0.
If G is a graph with chromatic number k, then, for some ℓ ∈ N, C(G) contains every odd integer in
[ℓ, ℓ · k1−ε].

Corollary 1.5. Let a, b ∈ N, and let Ca,b(G) = {ℓ ∈ C(G) : ℓ ≡ a mod b}. If G has chromatic
number k, then ∑

Corollary 1.6. Given C ∈ N, there exists k0 ∈ N such that the following holds. Let σ1, σ2, . . . be
an inﬁnite increasing sequence of odd integers such that σi+1 ≤ Cσi for each i ∈ N. Then, every
graph G with chromatic number at least max{k0, σ2
1} has some i ∈ N with σi ∈ C(G).

Theorem 1.7. For each k ∈ N, there exists d such that every graph with average degree at least d
contains a TK
(ℓ)
k for some ℓ ∈ N.

Theorem 2.2 ([13]). There exists some ε1 > 0 such that the following holds for every k > 0. Every
graph G has an (ε1, k)-expander subgraph H with d(H) ≥ d(G)/2 and δ(H) ≥ d(H)/2.

Lemma 2.3 ([13]). Let ε1, k > 0. If G is an n-vertex (ε1, k)-expander, then any two vertex sets,
each of size at least x ≥ k, are of distance at most 2
ε1 log3(15n/k) apart. This remains true even
after deleting x · ε(x)/4 arbitrary vertices from G.

Proposition 2.4. Within any graph G there is a bipartite subgraph H with d(H) ≥ d(G)/2.

Corollary 2.5. There exists some ε1 > 0 such that the following holds for every ε2 > 0 and d ∈ N.
Every graph G with d(G) ≥ 8d has a bipartite (ε1, ε2d)-expander subgraph H with δ(H) ≥ d.

Theorem 2.7. There exists ε1 > 0, such that, for each 0 < ε2 < 1/5, there exists d0 = d0(ε1, ε2)
such that the following holds for each n ≥ d ≥ d0. Suppose that H is a TK
(2)
d/2-free bipartite n-vertex
(ε1, ε2d)-expander with δ(H) ≥ d. Let x, y ∈ V (H) be distinct, and let

Theorem 1.1 follows from Theorem 2.7 and Corollary 2.5, as follows.

Lemma 3.2. Let 0 < ε1, ε2 < 1 and k ∈ N. There is some d0 = d0(ε1, ε2, k) for which the following
holds for each n ≥ d ≥ d0.
Suppose H is an n-vertex (ε1, ε2d)-expander. Let m = 16
ε1 log3 n and ℓ0 = (log log n)5. Let
A ⊆ V (H) with |A| ≥ ε2d/2 and let X, Y, Z ⊆ V (H) \ A be such that the following hold.

Claim 3.3. For each 0 ≤ r ≤ ℓ0 − 1,

Lemma 3.2 allows us to ﬁnd paths between sets A and B in an expander, as follows.

Lemma 3.4. For each 0 < ε1, ε2 < 1, there exists d0 = d0(ε1, ε2) such that the following holds for
each n ≥ d ≥ d0 and x ≥ 1. Let G be an n-vertex (ε1,…

Lemma…


*[further statements in the full text]*

*[digest of a 124351 character source; every section, statement, and proof in full at `research/L0.1/liu-montgomery-odd-cycle.full.md`]*
