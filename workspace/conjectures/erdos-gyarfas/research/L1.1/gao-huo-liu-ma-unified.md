> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/L0.0/gao-huo-liu-ma-unified.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1904.08126 | converted from PDF -->

## What it claims

In this paper, we prove a tight minimum degree condition in general graphs for the existence of
paths between two given endpoints, whose lengths form a long arithmetic progression with common
diﬀerence one or two. This allows us to obtain a number of exact and optimal results on cycle lengths
in graphs of given minimum degree, connectivity or chromatic number.
More precisely, we prove the following statements by a uniﬁed approach.

1. Every graph G with minimum degree at least k + 1 contains cycles of all even lengths modulo k;
in addition, if G is 2-connected and non-bipartite, then it contains cycles of all lengths modulo
k.

2. For all k ≥ 3, every k-connected graph contains a cycle of length zero modulo k.

3. Every 3-connected non-bipartite graph with minimum degree at least k + 1 contains k cycles
of consecutive lengths.

4. Every graph with chromatic number at least k + 2 contains k cycles of consecutive lengths.

The ﬁrst statement is a conjecture of Thomassen, the second is a conjecture of Dean, the third is
a tight answer to a question of Bondy and Vince, and the fourth is…

## Statements it makes

Conjecture 1.1 (Liu and Ma [15]). Every graph with minimum degree at least k + 1 contains k
admissible cycles.

Theorem 1.2. Let G be a 2-connected graph and let x, y be distinct vertices of G. If every vertex of G
other than x and y has degree at least k + 1, then there exist k admissible paths from x to y in G.

Theorem 1.3. Every graph G with minimum degree at least k + 1 contains k admissible cycles.

Theorem 1.3 improves many previous results such as the results in [10, 12, 15, 25]. As the writeup of
a version of this paper was close to complete, we noticed that very recently, Chiba and Yamashita [4]
independently proved Theorem 1.3 under an extra condition that G is 2-connected, by using a diﬀerent
approach from this paper.
One can ask another natural question: what are necessary or suﬃcient conditions for the existence
of k cycles of consecutive lengths? It is clear that such conditions should include non-bipartiteness.
This was addressed by Bondy and Vince in [2], where they proved that any non-bipartite 3-connected
graph contains two cycles of consecutive lengths. On the other hand,…

Theorem 1.4. Every non-bipartite 3-connected graph with minimum degree at least k + 1 contains k
cycles of consecutive lengths.

Conjecture 1.5 (Thomassen [21]). Every graph with minimum degree at least k + 1 contains cycles of
all even lengths modulo k.

Conjecture 1.6 (Thomassen [21]). Every 2-connected non-bipartite graph with minimum degree at
least k + 1 contains cycles of all lengths modulo k.

Theorem 1.7. Conjectures 1.5 and 1.6 hold for any positive integer k.

Conjecture 1.8 (Dean [5]). For any positive integer k ≥ 3, every k-connected graph contains a cycle
of length zero modulo k.

Theorem 1.9. Conjecture 1.8 holds for any positive integer k ≥ 3.

Conjecture 1.10 (Sudakov and Verstra¨ete [20]). For every integer k ≥ 2, χk = k + 1.

Theorem 1.11. Conjecture 1.10 holds for every integer k ≥ 2.

Theorem 2.1. Let G be a 2-connected graph and let x, y be distinct vertices of G. If every vertex in
G other than x and y has degree at least 3, then there are two admissible paths from x to y in G.

Theorem 3.1. Let k be a positive integer. If (G, x, y) is a 2-connected rooted graph with minimum
degree at least k + 1, then there exist k admissible paths from x to y in G.

Lemma 3.2. Let (H, u, v) be a rooted graph and W be a subset of V (H). Let s be a positive integer.
Assume that there exist s admissible paths P1, ..., Ps, where Pi is from u to some wi ∈ W for each
i ∈ [s]. Assume that for each i ∈ [s], H − V (Pi − wi) contains t paths Ri
1, ..., Ri
t from wi to v such that
their lengths form an arithmetic progression with common diﬀerence one or two2. If |R1
j | = · · · = |Rs
j |
for every j ∈ [t], then there exist s + t − 1 admissible paths in H from u to v.

Lemma 3.3. G is 2-connected, x and y are not adjacent in G, and k ≥ 3.

Lemma 3.4. There is no…


*[further statements in the full text]*

*[digest of a 100520 character source; every section, statement, and proof in full at `research/L0.0/gao-huo-liu-ma-unified.full.md`]*
