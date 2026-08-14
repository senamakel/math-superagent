# Induced subgraphs of hypercubes: full vertices via Kruskal-Katona

Source: "Induced subgraphs of hypercubes", European J. Combinatorics (2012).
URL: https://www.sciencedirect.com/science/article/pii/S0195669812001680

## What it establishes

For the k-dimensional hypercube Q_k, a vertex of an induced subgraph
G = Q_k[S] is **full** if its degree inside G is k (the maximum possible).
Define φ_k(n) = max over S with |S| = n of the number of full vertices in
Q_k[S]. The paper determines φ_k(n) exactly for all n ≤ 2^k (Theorem 3.2),
describes the extremal subgraphs, and uses it to solve a min-max problem about
covering all edges of Q_k by two induced subgraphs (Theorem 4.1).

Method: Kruskal–Katona theory applied to the f-vector of the simplicial complex
of subsets of S (a vertex is full iff all its k neighbours are in S, which is a
downward-closed condition expressible via the shadow of the set system).

## Relevance to problem.md

This is a legitimate technique source (not the answer to problem.md) that
develops the Kruskal–Katona method on the hypercube. It directly concerns how
many vertices can have degree close to k inside S. For problem.md the relevant
quantitative object is the maximum internal degree D(S); the "full vertex" count
is the D = k end of the spectrum, whereas problem.md's S of size 2^{n-1}+1 is at
the other end. Still, the Kruskal–Katona / shadow technique is one candidate for
a maximum-producing bound and is worth holding. The extremal structure
(Hamming-ball-like / initial-segment families) also connects to the isoperimetric
theory.
