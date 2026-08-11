> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/L0.1/carr-diameter2.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2508.19302 | converted from PDF -->

## What it claims

In this short note it is shown that every graph of diameter 2 and minimum degree
at least 3 contains a cycle of length 4 or 8. This result contributes to the study of the
Erd˝os–Gy´arf´as Conjecture [1] by confirming it for the class of diameter-2 graphs.

Notation and Preliminaries

All graphs considered in this note are finite, simple, and undirected.
Let G = (V (G), E(G)) be a graph where V (G) and E(G) denote the set of vertices and
edges in G respectively. For a vertex v ∈ V (G), the neighborhood of v is

N (v) = {u ∈ V (G) : uv ∈ E(G)},

and the degree of v is d(v) = |N (v)|. The minimum degree of G is denoted by

δ(G) = min{d(v) : v ∈ V (G)}.

For vertices u, v ∈ V (G), the distance d(u, v) is the length of a shortest path joining u
and v in G. The diameter of G is

diam(G) = max{d(u, v) : u, v ∈ V (G)}.

A path of length k is a sequence of distinct vertices

v0, v1, . . . , vk

such that vivi+1 ∈ E(G) for all 0 ≤ i < k. A cycle of length k is a sequence

v0, v1, . . . , vk−1, v0

in which v0, . . . , vk−1 are distinct and vivi+1 ∈ E(G) for all indices taken modulo k.

1arXiv:…

## Statements it makes

Theorem 1.1.: Let G be a graph with diameter 2 and minimum degree at least 3. Then G
contains a cycle of length 4 or 8.

Claim 1.1. v4v6 /∈ E(G).
Proof. If v4v6 ∈ E(G), then
 v4 − v1 − v2 − v6 − v4

Claim 1.2. v7 /∈ {v1, v2, v3}.
Proof. If v7 = x such that x ∈ {v1, v2, v3}, then at least one of the following 4–cycles
would form: v1 − v3 − v2 − v6 − v1,
v2 − v3 − v1 − v6 − v2,
v4 − v3 − v2 − v1 − v4. ⋄

Claim 1.3 v8 /∈ V (G′).
Proof. Indeed, if v8 ∈ V (G′), then v8 ∈ {v1, v2, v4, v6} and a 4–cycle arises in each case:

Claim 1.4. v9 /∈ V (G′).
Proof. Otherwise v9 ∈ {v1, v2, v4, v6}, and each possibility yields a 4–cycle:

Claim 1.5. If v9 is adjacent to x ∈ {v1, v2, v4, v6}, then there exists a 4–cycle.
Proof. Assume v9 is adjacent to x ∈ {v1, v2, v4, v6}. Thus, a 4–cycle is formed in each of the
following cases: x = v1 =⇒ v1 − v3 − v8 − v9 − v1,
x = v2 =⇒ v2 − v3 − v8 − v9 − v2,
x = v4 =⇒ v4 − v7 − v8 − v9 − v4,
x = v6 =⇒ v6 − v7 − v8 − v9 − v6. ⋄
Also, since v9 is nonadjacent with both v4 and v2, by diam(G) = 2 both N (v9) ∩ N (v4)
and N (v9) ∩ N (v2) are non-empty.

Claim 1.6. There is a vertex v10 ∈ (N (v9) ∩ N (v4)) ∪ (N (v9) ∩ N (v2)) such that
v10 /∈ ({v7, v8} ∪ V (G
′)).
Proof. If v8 ∈ (N (v9) ∩ N (v4)) ∪ (N (v9) ∩ N (v2)) then v8 is adjacent to one of v2 or v4 and,
by Claim 1.4, a 4–cycle is present. Thus, v10 ̸= v8. Now, suppose v10 ∈ (N (v9) ∩ N (v4)) ∪
(N (v9) ∩ N (v2)) such that (N (v9) ∩ N (v4)) ∪ (N (v9) ∩ N (v2)) ⊆ ({v7} ∪ V (G
′)). Then, by
the diameter 2 condition and Claim 1.5, v9 is adjacent to both v3 and v7 (else v9 would be
adjacent to another pair of vertices in {v7}∪V (G′) violating Claim 1.5). However, this forms
a 4–cycle by v3 − v8 − v7 − v9 − v3, providing a contradiction on the claim of no 4–cycles. ⋄
Thus, by Claim 1.6,…

Claim 2.1. If xy ∈ E(G) for some x ∈ {v3, v4} and y ∈ {v5, v6}, then G contains a 4-cycle.
Proof. Since v1x ∈ E(G) and v2y ∈ E(G), the cycle v1 − x − y − v2 − v1 has length 4. ⋄

Claim 2.2. There exist a ∈ {v3, v4} and b ∈ {v5, v6} such that

Claim 2.3. v7v4 /∈ E(G).
Proof. If v7v4 ∈ E(G), then v4 − v7 − v3 − v1 − v4 is a 4-cycle. ⋄

Claim 2.4. v8 /∈ {v3, v5, v7}.
Proof. If v8 = v3 or v8 = v5, then Claim 2.1 is violated. If v8 = v7, then Claim 2.3 is
violated. ⋄

*[digest of a 14190 character source; every section, statement, and proof in full at `research/L0.1/carr-diameter2.full.md`]*
