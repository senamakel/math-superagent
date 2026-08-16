# Pór & Valtr, "The Partitioned Version of the Erdős–Szekeres Theorem"

<!-- source: https://link.springer.com/article/10.1007/s00454-002-2894-1 | full text at
     research/sources/por-valtr - The Partitioned Version of the Erdos-Szekeres Theorem - DCG 2002.full.md -->

**Publication.** A. Pór and P. Valtr, *Discrete & Computational Geometry* 28 (2002) 625–637,
DOI 10.1007/s00454-002-2894-1.

## The main theorem — point sets partition into bounded convex clusterings

A planar finite set $X$ is a **convex $k$-clustering** if it is a disjoint union of $k$ sets
$X_1,\dots,X_k$ of equal sizes such that $x_1\cdots x_k$ is a convex $k$-gon for every choice of
$x_i\in X_i$.

**Theorem (Pór–Valtr, answering Kalai's question).** For every $k\ge 4$ there are constants
$c=c(k)$ and $c'=c'(k)$ such that: if $X$ is a finite set of planar points in general position,
then it has a subset $X'$ of size at most $c'$ such that $X\setminus X'$ can be partitioned
into at most $c$ convex $k$-clusterings. (The case $k=4$ was proved earlier by Pór.)

## Why it matters for this problem

This is the **partition/recursion structural instrument** the problem description's phase-4
route points at ("Ramsey-type counting, cups-and-caps, *the positive-fraction and same-type
lemmas*, transversal/Tverberg machinery"). Its key content:

1. It **strengthens the positive-fraction ES theorem** (Bárány–Valtr, already in the library):
   beyond "there exist $k$ subsets $Y_i$ of linear size whose every transversal is convex,"
   the *whole* point set (minus a bounded exception) splits into a *bounded number* of such
   clusterings, improving Pach–Solymosi's constants.
2. **Local structure of large point sets:** any $n$-point set is almost entirely a bounded
   union of convex clusterings — so a hypothetical extremal set of $2^{n-2}$ points with no
   convex $n$-gon cannot be "generic"; it must concentrate its $n$-gon avoidance in the
   bounded remainder $X'$ and in how the clusterings interact. This is the structural handle
   for "what a minimal counterexample must look like."
3. Answers Kalai's question, and generalizes to higher dimensions.

## claim block

```claim
id: por-valtr-partitioned
statement: For every k ≥ 4 there are constants c=c(k), c'=c'(k) such that every finite planar general-position set X has a subset X' of size ≤ c' with X\X' a disjoint union of ≤ c convex k-clusterings (each a union of k equal-size sets whose every transversal is a convex k-gon). Strengthens the positive-fraction ES theorem (Bárány–Valtr) and answers a question of Kalai.
hypotheses: finite planar point sets in general position; k ≥ 4; equal-size transversal-convex blocks.
holds-here: true — this is the structural/partition instrument for understanding what an extremal (n-gon-free) set must look like.
status: proved (Pór–Valtr, DCG 28 (2002) 625–637).
bearing: a minimal counterexample of 2^{n-2} points must be almost a bounded union of convex k-clusterings; its n-gon-avoidance is concentrated in the bounded exception and inter-clustering interaction — a concrete structural constraint on extremal sets (GOAL/MEMORY structural work).
anchor: research/sources/por-valtr - The Partitioned Version of the Erdos-Szekeres Theorem - DCG 2002.full.md
```
