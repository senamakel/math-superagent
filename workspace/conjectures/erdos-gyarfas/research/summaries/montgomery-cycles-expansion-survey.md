> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/montgomery-cycles-expansion-survey.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://ems.press/content/serial-article-files/52107 | converted from PDF -->

## What it claims

Cycles are fundamental objects in graph theory, where their inher-
ent simplicity belies the depth of even some simply stated questions.
In this article, I will discuss three problems on cycles in graphs
and recent progress on them. In each case, the progress has been
made by new and different tools involving graph expansion, itself
an important topic in extremal graph theory.

1 Eulerian graphs and the Erdős–Gallai problem

The advent of graph theory is often pinned to the Königsberg
bridge problem from the 18th century. At the time, Königsberg
had seven bridges connecting either side of the Pregel River and
the two islands within it (see Figure 1). Was it possible to walk
through the city while crossing each bridge exactly once? In 1735,
this problem reached Euler, who comprehensively solved it in full
generality. Representing each connected land mass by a vertex and
each bridge by an edge between the two vertices it connects, we
get a graph. Euler showed that there is a walk in a graph passing
through every edge exactly once if and only if it is connected1 and
at most two…

A B

C

## Statements it makes

Conjecture 1.1 (Erdős and Gallai). Every n-vertex graph has a de-
composition into O(n) cycles and edges.

Theorem 1.2. Any n-vertex graph decomposes into O(n log∗ n)
cycles and edges.

Theorem 2.1. There is some d > 0 such that every graph with
average degree at least d has a cycle whose length is a power
of 2.

Conjecture 2.2. Any graph with minimum degree at least 3 has
a cycle whose length is a power of 2.

Theorem 2.3. Every graph G with average degree d satisfies

Theorem 2.4. Every graph G with chromatic number at least k
satisfies ∑ℓ ∈ 𝒞odd(G) 1
ℓ ≥ ( 1
2 − o(1)) log k.

Conjecture 3.1 (Chvátal). There is some t such that any t-tough
graph is Hamiltonian.

Conjecture 3.2 (Thomassen). All but finitely many connected
vertex-transitive graphs have a Hamilton cycle.

Conjecture 3.3. There exists C > 0 such that any n-vertex graph
satisfying the following two conditions is Hamiltonian.
1. |N(A)| ≥ C|A| for any vertex set A of at most n/2C vertices.
2. For any disjoint vertex sets A, B of at least n/C vertices each,
there is an edge between A and B in G.

*[digest of a 40335 character source; every section, statement, and proof in full at `research/sources/montgomery-cycles-expansion-survey.full.md`]*
