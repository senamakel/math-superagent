# Spencer–Szemerédi–Trotter (1984) — upper bound on unit distances in the plane

**Source URL:** J. Spencer, E. Szemerédi, W. T. Trotter, *Unit distances in the
Euclidean plane*, in *Graph Theory and Combinatorics* (B. Bollobás, ed.),
Academic Press, New York, 1984, pp. 293–303. (Some citations give 294–304 / 293–308.)
Full text: `research/sources/spencer-szemeredi-trotter-1984.full.md`
(bibliographic record; original text not fetched — see gap note).

## Exact result statement

Let `P` be a set of `n` points in the Euclidean plane `R²`. Let `u(P)` be the
number of (unordered) pairs of points of `P` at distance exactly `1`, and let
`u(n) = max { u(P) : |P| = n }`. Then

```
u(n) = O(n^{4/3}).
```

## Hypotheses

- `P` finite, in the **plane** `R²`, with the ordinary Euclidean distance.
- The unit is a normalisation (any fixed distance; the bound is scale-invariant).
- The bound is the **upper** bound on the number of unit distances. It is tight
  up to constants under current methods. The matching lower bound is Erdős's:
  `u(n) = Ω(n^{1 + c/log log n})` for some `c > 0` (Erdős 1946), which is still
  conjectured to be optimal.

## Why this run cares (density cannot be bought)

A unit-distance graph on `n` points has `O(n^{4/3})` edges, so average degree is
`O(n^{1/3})` and a random/greedy point set has far too few edges to force a high
chromatic number. Any graph with chromatic number `≥ 5` must be **rigid**: its
unit distances must be highly coincidental, which happens only for point sets
with algebraic structure. This is exactly the guidance in `problem.md`: search
over structured constructions (Minkowski sums, rotations, algebraic point sets),
never over random points.

## What it does NOT forbid

The bound says nothing about what chromatic numbers are achievable — it only
limits edge density. It does not rule out `5`-chromatic unit-distance graphs; it
tells the search where rigidity has to come from. (Chromatically dense graphs
force high degree, and high degree is only reachable through algebraic
coincidence, not random placement.)

## Status

- **Sourced, standard theorem.** Statement and hypotheses corroborated by the
  original-record entry (NYU Scholars), the Ágoston–Pálvölgyi survey (arXiv
  2006.06285), the Pach–Raz–Solymosi SoCG 2026 paper (DOI 10.4230/lipics.socg.2026.83),
  and the 2023 Discrete & Comput. Geom. survey (DOI 10.1007/s00454-023-00503-2).
- All those sources attribute `u(n) = O(n^{4/3})` to Spencer–Szemerédi–Trotter
  (1984); the Pach–Raz–Solymosi paper calls it "the classical result" and notes
  it "remains the best-known upper bound".
- **Unverified locally:** no verbatim 1984 text was fetched (reported in
  FRONTIER.md). The proof mechanism (reduction to an incidence bound for unit
  circles, later recast via the crossing-number lemma) is described in the
  cited sources but not reproduced here.
