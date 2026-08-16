# Duque, Fabila-Monroy, Hidalgo-Toscano, "Point Sets with Small Integer Coordinates and with Small Convex Polygons" (arXiv:1602.03075, DCG 2017)

<!-- source: https://arxiv.org/pdf/1602.03075 | full text: research/sources/duque-fabila-monroy-hidalgo-toscano - ES construction small integer coordinates - correct full.full.md -->

**Publication.** F. Duque, R. Fabila-Monroy, C. Hidalgo-Toscano, *Discrete & Computational Geometry* (2017), DOI 10.1007/s00454-017-9931-6. (The sibling `duque-... - 2017 full.md` is a MIS-DOWNLOAD stub — this is the correct file.)

## What it establishes

**The ES 1961 lower-bound construction is realizable with small integer coordinates.** Concretely: for every positive integer t, there is a set of n = 2^{t-2} points in general position such that every convex polygon with vertices in the set has at most log₂(n)+1 vertices, and the set fits in an integer grid of size **O(n² log³ n)**.

- This is a *grid-size* result about the known construction, not a new bound on ES(n). It converts the classical (geometric/real-valued) Erdős–Szekeres 1961 construction into exact integer coordinates, which is exactly what GOAL criterion 3 needs to build and verify the lower-bound witness set at n = 5, 6, 7 (8, 16, 32 points, grid size O(n² log³ n) = O(25·27), O(36·64), O(49·125)).
- It does **not** settle realizability of the ES construction in general — that is the 1961 paper itself — but it settles the *coordinates* the run can hand the oracle.

## Hypotheses and whether they hold here

- **Holds:** the result concerns exactly the objects this run works over (planar general-position point sets, convex polygons, the ES construction).
- **Status:** proved in the paper (construction via perturbation of the classical blocks onto an integer grid); not independently re-derived in this run. Treated as asserted-by-source until the run's own `es_construct` oracle reproduces the property at n = 5, 6, 7 (which it does — see `code/out/verify_es_construct.py`).

## Bearing on this run

- Supplies the exact-coordinate realization that makes the lower-bound witness set *checkable*: `es_construct.es_set` (exact Fractions) is the run's implementation of this construction family, verified at n = 4..7 by the oracle and an independent gift-wrap hull.
- The O(n² log³ n) grid bound is a coordinate-size budget: any exact integer realization the run builds should be comparable in magnitude, and the oracle's `in_general_position` will catch grid collisions that break general position (the failure mode that killed the older `es_construction.es_lower_set`).

## What it does not settle

- It does not prove ES(n) = 2^{n-2}+1 (no upper bound); it only makes the lower-bound construction explicit and finite.
- It does not give the run a new structural constraint on hypothetical extremal sets beyond the existence of small-coordinate realizations.

```claim
id: es-construction-integer-realization
statement: The Erdős–Szekeres 1961 lower-bound construction (n = 2^{t-2} points, no convex polygon with more than log₂(n)+1 vertices) can be realized with integer coordinates in a grid of size O(n² log³ n).
hypotheses: planar point set in general position; n = 2^{t-2}; t a positive integer.
holds-here: yes — this is the coordinate budget behind the run's verified es_construct witness set.
status: asserted-by-source (proved in Duque et al. 2017; not independently re-derived here, but consistent with the run's own exact realization).
bearing: GOAL criterion 3 — the oracle's witness set needs exact integer/rational coordinates; this bounds how large those coordinates must be, and warns that floating-point radial placement (which killed the older construction) must be avoided.
anchor: research/sources/duque-fabila-monroy-hidalgo-toscano - ES construction small integer coordinates - correct full.full.md
```
