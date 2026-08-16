# Aichholzer, Aurenhammer & Krasser 2002, "Enumerating Order Types for Small Point Sets with Applications", Order 19, 265–281

Source: https://link.springer.com/article/10.1023/A:1021231927255
Full text: [[aichholzer-aurenhammer-krasser - Enumerating order types for small point sets with applications 2002 full.full]]

## What it establishes

A complete and reliable database of all *order types* (rank-3 chirotopes / abstract oriented
matroids) of size $n \le 10$, each with a realizing point set in a small integer grid. Order type
= combinatorial orientation information; convex position is an order-type invariant.

```claim
id: aichholzer-order-db
statement: The order types of n <= 10 (size in standard small integer grids) are enumerated and held as a database with realizing point sets.
hypotheses: n <= 10
holds-here: yes (for small-n verification; not for n>=7 full ES which is far beyond any Order enumeration)
status: proved / catalogued (enumeration)
bearing: enumeration source for small n; lets the run verify convex-position checks and near-extremal structure up to n<=10 by order type rather than raw coordinates.
anchor: research/sources/aichholzer-aurenhammer-krasser - Enumerating order types for small point sets with applications 2002 full.full.md
```

## Caveat that governs its use

Not every abstract chirotope is realizable (realizability is $\exists\mathbb{R}$-complete). So:
an upper bound proved over ALL abstract order types is stronger than the conjecture and may be
false — look for the unrealizable witness before believing such a proof; and any lower-bound
construction found in order-type space must be realized with explicit rational/integer coordinates
before it counts as a planar ES witness. The ES(7)=33 claims live far outside this database's size
range.

## Not-helpful bounds

The applications in this paper (triangulations, polygonalizations, k-sets) are examples of the
database's use, not contributions to ES structure. Not used beyond the database itself.
