# Falik–Samorodnitsky, "Edge-Isoperimetric Inequalities and Influences" (CPC 16, 2007)

Source URL: https://doi.org/10.1017/s0963548306008340
Full text URL: https://www.semanticscholar.org/reader/fd95cf9a50eb528b975ed1bf7f5b779ca7c11098
Authors: Dvir Falik, Alex Samorodnitsky. Combinatorics, Probability and Computing 16 (2007), 693–712.

## What this source establishes

1. The **edge-isoperimetric inequality** on the Boolean cube: for A ⊆ {0,1}^n
   with |A| ≤ 2^{n-1}, i.e. µ = |A|/2^n ≤ 1/2,

       Σ_{i=1}^n I_i(A) ≥ 2 log2(1/µ) · µ

   (equivalently total influence ≥ 2 log2(e)·n·µ·log(1/µ) up to constants),
   where I_i(A) is the influence of the i-th coordinate on the indicator of A.
   This is an **average/total** quantity (sum of per-coordinate influences).

2. A combinatorial proof of the Kahn–Kalai–Linial result: every balanced
   Boolean function on the cube has a variable with influence ≥ Ω(log n / n).

3. Improved constants in related isoperimetric statements, plus conjectures
   about optimal constants whose near-optimal functions resemble subcubes.

## Why it is here

This is the link between isoperimetry on the cube and the influence/Fourier
machinery. The bound it gives is on Σ I_i(A), the total influence / average
boundary. For a set S with |S| = 2^{n-1}+1 it does **not** bound the maximum
internal degree D(S). The average internal degree of S is
(2·e_internal(S))/|S| = (internal edges · 2)/|S|, a different quantity from total
influence (which counts edges leaving S). KBELOW the half-cube size the
influence bound is the natural max-lower-bound engine: I_i(A) = fraction of
vertices whose flip leaves A. The max degree inside S is at most max_i of
(vertices in S flipping coordinate i into S) = a per-coordinate *internal*
influence, not a total one.

## Claim blocks

```claim
id: falik-samorodnitsky-edge-isoperimetric
statement: For A ⊆ {0,1}^n with µ = |A|/2^n ≤ 1/2, the total influence
  Σ_i I_i(A) ≥ 2 log2(1/µ)·µ (edge-isoperimetric inequality, with the KKL bound
  as a corollary: some variable has influence ≥ Ω(log n / n) for balanced f).
hypotheses: A ⊆ {0,1}^n, µ ≤ 1/2; I_i(A) = influence (edge-boundary fraction
  in direction i).
holds-here: partially — the set size in problem.md is 2^{n-1}+1 (µ slightly over
  1/2), just above the regime where this is stated. The quantity bounded is
  total/average, not the max internal degree D(S).
status: asserted-by-source (proved in the paper; not re-derived here).
bearing: fingerprints the obstruction in problem.md — influence/total-boundary
  methods bound average quantities; a max bound on D(S) needs a per-coordinate
  internal influence, which is not what these give directly.
anchor: falik-samorodnitsky-2007
```

```claim
id: kkl-balance-influence
statement: Every balanced Boolean function on {0,1}^n (µ = 1/2) has a variable
  with influence ≥ c·(log n)/n for an absolute constant c > 0 (Kahn–Kalai–Linial
  1988; combinatorial proof in Falik–Samorodnitsky 2007).
hypotheses: f: {0,1}^n → {0,1} with E f = 1/2.
holds-here: this bounds max over coordinates of the *leaving* boundary fraction,
  not the max internal degree of a +1 vertex set. D(S) concerns edges both
  endpoints in S; a derivative w.r.t. coordinate i is some vertex whose flip
  changes membership, i.e. an S→complement edge. The KKL bound gives one
  coordinate where many S→comp edges exist; it does not give one vertex in S
  with many internal neighbours.
status: asserted-by-source.
bearing: a key adjacent technique; if it directly gave D(S) ≥ c log n /something
  the gap would be different. Confirms the max-internal-degree quantity is a
  per-vertex max, orthogonal to per-coordinate influence sums.
anchor: falik-samorodnitsky-2007
```
