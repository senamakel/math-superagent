# Kruskal–Katona theorem (primary statement)

Source: J. B. Kruskal, "The number of simplices in a complex" (1963); G. O. H.
Katona, "A theorem of finite sets" (1968). For the statement used here see also
the Springer article "f-Vectors Implying Vertex Decomposability", Discrete
Comput. Geom. (2012). URL: https://link.springer.com/article/10.1007/s00454-012-9477-6

## Statement

For a family U of k-element subsets of [n], the **lower shadow** ΔU is the set of
all (k−1)-subsets contained in some member of U. The Kruskal–Katona theorem gives
the minimum possible size of ΔU in terms of |U| = m. Order k-subsets in the
**squashed order** (A < B iff max(A∖B) < max(B∖A)); let S_k(m) be the first m
sets. Then for every family U of k-sets with |U| = m,

    |ΔU| >= |ΔS_k(m)|.

There is an explicit formula: if m = C(a_k, k) + C(a_{k-1}, k-1) + ... with
a_k > a_{k-1} > ... (the k-binomial decomposition of m), then
|ΔS_k(m)| = C(a_k, k-1) + C(a_{k-1}, k-2) + ...

## Relevance to problem.md

This is the exact extremal tool used by the "Induced subgraphs of hypercubes"
paper to count how many vertices of an induced subgraph Q_k[S] can be **full**
(degree k). A vertex x ∈ S is full iff all k of its neighbours are in S — a
condition expressible as a shadow of the set system determined by S's layers,
so Kruskal–Katona controls it. K–K is a machinery source for a
maximum-producing count on the cube, one direction candidates for D(S) come
from; it is here as the technique, not as the answer to problem.md.
