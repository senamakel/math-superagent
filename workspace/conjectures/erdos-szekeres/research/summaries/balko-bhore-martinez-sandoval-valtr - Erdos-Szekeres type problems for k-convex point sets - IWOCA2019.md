# Balko, Bhore, Martinez-Sandoval & Valtr, "On Erdős–Szekeres-Type Problems for k-convex Point Sets"

<!-- source: https://repositum.tuwien.at/handle/20.500.12708/57987 | metadata landing page held at research/sources/balko-bhore-martinez-sandoval-valtr - ... IWOCA2019.full.md -->

**Publication.** M. Balko, S. Bhore, L. Martinez-Sandoval, P. Valtr, *Combinatorial Algorithms (IWOCA 2019)*, LNCS 11638, Springer, pp. 35–47; DOI 10.1007/978-3-030-25005-8_4. Journal version: *European J. Combin.* 89 (2020) 103157 (ScienceDirect, paywalled). **Only the metadata landing page is held here** (reposiTUm), not the full text — this is a context/abstract record, not a primary source.

## What is held

- Full abstract (below).
- Publishing metadata: authors, venue, DOI, peer review.

## What the abstract establishes (asserted-by-source abstract)

- A finite set S of n points in general position is **k-convex** if there is a spanning simple polygonization of S whose interior meets any straight line in at most k connected components. (k=1 is ordinary convex position.)
- **Main result:** for every fixed k, every n-point set in general position contains a k-convex subset of size at least Ω(log_k n). This extends the classical Erdős–Szekeres theorem (the k=1, convex-position case).
- There exist arbitrarily large 3-convex n-point sets whose largest 1-convex (convex) subset has size only O(log n) — answering a problem of Aichholzer et al.
- There is c>0 such that for every n there is an n-point set where every 2-convex polygon spanned by ≥ c·log n points of S contains an interior point of S — matching an upper bound of Aichholzer et al. up to a constant.

## Why this is **not** progress here (drift guard)

This is an **adjacent problem**, not a restricted class of the ES conjecture. k-convexity with k>1 is a *relaxation* of convex position (the polygon need only be k-convex), so a k-convex subset is *not* n points in convex position. The Ω(log_k n) results are about the size of guaranteed k-convex subsets, entirely different from ES(n)=2^{n-2}+1. It does NOT give a restricted class on which the ES conjecture holds. Held as encyclopedic context only; do not mistake its log-type statements for progress toward the exact conjecture.

## claim block

```claim
id: balko-bhore-kconvex-abstract
statement: (abstract) Every fixed k and every general-position n-point set contains a k-convex subset of size Ω(log_k n); 3-convex n-point sets exist whose largest convex subset is O(log n).
hypotheses: k-convexity as a relaxation of convex position (spanning simple polygonization meeting any line in ≤ k components).
holds-here: true as an adjacent-problem context result; does NOT bear on ES(n)=2^{n-2}+1.
status: asserted-by-source (abstract only; full text not held).
bearing: encyclopedic context only — k-convexity is a relaxation of convex position, not a restricted class where the ES conjecture is known. Do not use its log-type bounds as ES progress.
anchor: research/sources/balko-bhore-martinez-sandoval-valtr - Erdos-Szekeres type problems for k-convex point sets - IWOCA2019.full.md
```
