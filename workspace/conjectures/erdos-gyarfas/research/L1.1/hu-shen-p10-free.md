> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/L0.1/hu-shen-p10-free.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2308.05675 | converted from PDF -->

## What it claims

Abstract: Let P10 be a path on 10 vertices. A graph is said to be P10-free if
it does not contain P10 as an induced subgraph. The well-known Erd˝os-Gy´arf´as
Conjecture states that every graph with minimum degree at least three has a cycle
whose length is a power of 2. In this paper, we show that every P10-free graph with
minimum degree at least three contains a cycle of length 4 or 8. This implies that
the conjecture is true for P10-free graphs.

Keywords: Erd˝os-Gy´arf´as Conjecture; P10-free graph; cycle

1 Introduction

All graphs considered here are ﬁnite and simple. Let G be a graph. The vertex
set, the edge set and the minimum degree of G are denoted by V (G), E(G) and
δ(G), respectively. For a vertex v ∈ V (G), we denote by NG(v) the neighbors of v
in G. For S ⊆ V (G), let NG(S) = ∪x∈SNG(x) − S. For convenience, we write N(v)
and N(S) for NG(v) and NG(S), respectively. Denote by G[S] the subgraph of G
induced by S. For X, Y ⊆ V (G), EG(X, Y ) represents the set consisting of all edges
in G with one end in X and the other in Y . Let H be a graph. We say that G is
H-free if it…

## Statements it makes

Theorem 1.1 Every P10-free graph with minimum degree at least three contains a
C4 or C8.

Lemma 2.1 Let G be a graph with δ(G) ≥ 3 and C a cycle of length at least 4 in
G. If G does not contain C4, then G[V (C)] has an m-hole for some integer m with
5 ≤ m ≤ ℓ(C).

Lemma 2.2 [9] Let G be a graph with δ(G) ≥ 3. If G does not contain C4 as a
subgraph, then G has an m-hole for some m ≥ 5.

Lemma 2.3 Let G be a graph and u, v, v′ three vertices of G such that v, v′ ∈ N(u).
Let A be a subset of V (G) − {u, v, v′} such that

Lemma 2.4 Let G be a graph and let C := x1x2 . . . xmx1 be a cycle in G with
5 ≤ m ≤ 7. If G contains neither C4 nor C8 as a subgraph, then |IC| ≤ 7 − m.

Lemma 2.5 Let G be a graph with δ(G) ≥ 3 and let C := x1x2 . . . xmx1 be a good
hole in G. If G contains neither C4 nor C8 as a subgraph, then for each i ∈ [1, m],
there exists a good path for (C, Xi) with order min {⌊m/2⌋ − 1, 2}, where

Lemma 2.6 Let G be a P10-free graph with minimum degree at least 3 and let H be
a subgraph of G isomorphic to θ(2, 3, 3). If t5(G) = 0, then G admits a C4 or C8.

Claim 2.1 For i = 2, 5, G contains a good (H, xi)-path of length 3.

Claim 3.1 Let D be a cycle of G. If 4 ≤ ℓ(D) ≤ ℓ(C), then D is an m-hole and
|ID| ≤ |IC|. As a consequence, there exists no cycle of length k in G with 4 ≤ k < m.

Claim 3.2 ℓ(C) ≤ 6.

Claim 3.3 ℓ(C) ̸= 6.

Claim 3.4 Let i, j be two distinct integers in [1, 5] and let P be a (u, v)-path in
G − V (C) with u ∈ Ai and v ∈ Aj. Then

Claim 3.5 Let xi ∈ IC and let P := u1 . . . us, Q := v1 . . . vt be two paths in G − C
such that u1 ∈ Ai ∩ Ai+1 and v1 ∈ Ai+2 ∪ Ai+4.

Claim 3.6 Let i ∈ [1, 5] and let P := xiuvw be a pendent xi-path for C. Then
xi−1, xi, xi+1 /∈ N(w).

Claim 3.7 For each xi ∈ IC, there exists a near-good (C, xi)-path.

Claim 3.8 Let i be an integer in [1, 5] such that xi /∈ IC ∪ I +
C , then there exists a
good (C, xi)-path of length three in G.

Claim 3.9 For each xi ∈ IC, there exists a near-good (C, xi)-path xiyiziuivi such
that EG({yi, zi, ui, vi}, V (C)) = {yixi, yixi+1, zixi+3}.

Claim 3.10 IC = ∅.

*[digest of a 44645 character source; every section, statement, and proof in full at `research/L0.1/hu-shen-p10-free.full.md`]*
