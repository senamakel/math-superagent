> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/L0.0/hegde-sandeep-shashank-p13-free.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2410.22842 | converted from PDF -->

## What it claims

Abstract. Erdős and Gyárfás conjectured in 1994 that every graph with
minimum degree at least 3 has a cycle of length a power of 2. In 2022,
Gao and Shan (Graphs and Combinatorics) proved that the conjecture is
true for P8-free graphs, i.e., graphs without any induced copies of a path
on 8 vertices. In 2024, Hu and Shen (Discrete Mathematics) improved
this result by proving that the conjecture is true for P10-free graphs.
With the aid of a computer search, we improve this further by proving
that the conjecture is true for P13-free graphs.

Keywords: Erdős-Gyárfás conjecture · Pk-free graphs · Computer-aided
proof.

In 1994, Erdős and Gyárfás [3]
3 conjectured that every graph with minimum
degree at least 3 has a cycle of length a power of 2. The conjecture has been
veriﬁed for the following classes of graphs - 3-connected cubic planar graphs [6],
claw-free planar graphs [2], K1,m-free graphs with some additional degree con-
straints [12], and some families of Cayley graphs [5]. Liu and Montgomery [9]
proved that there exists a large constant such that every graph with average
degree…

## Statements it makes

Lemma 1. Let G
∗ be a minimal counterexample to Erdős-Gyárfás conjecture,
such that G
∗ is Pk-free for an integer k ≥ 3. Let {v0, v1, . . . , vn∗−1} be the set
of vertices of G
∗. Let G be a graph with the vertex set {v0, v1, . . . , vn−1}, where
3 ≤ n ≤ n∗, such that the following conditions are satisﬁed.

Corollary 1 follows from Lemma 1.

Corollary 1. Let G
∗ be a minimal counterexample to Erdős-Gyárfás conjecture
and let k be the smallest integer such that G
∗ is Pk-free but has an induced Pk−1.
Let G be the path v0v1 . . . vk−1. Then explore(G, k) returns False.

Theorem 1. Every P13-free graph with minimum degree at least 3 has a cycle
of length a power of 2.

Theorem 2. Every P12-free graph with minium degree at least 3 has a 4-cycle
or an 8-cycle.

*[digest of a 14917 character source; every section, statement, and proof in full at `research/L0.0/hegde-sandeep-shashank-p13-free.full.md`]*
