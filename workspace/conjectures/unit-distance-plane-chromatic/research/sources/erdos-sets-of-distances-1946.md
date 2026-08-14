# On Sets of Distances of n Points — Erdős 1946

**Source:** doi:10.2307/2305092, Paul Erdős, American Mathematical Monthly 53 (1946)
**Full text:** not on disk; read via read_sources.

## What this establishes

The founding paper of the two classical extremal distance problems in the
plane. Both are the density side of the unit-distance story and both fix what a
unit-distance graph on n points can look like.

- **Unit-distance lower bound (Problem A):** there exist configurations of n
  points in the plane with Ω(n log n) pairs at unit distance. The construction
  is structured (lattice/grid-like), not random — the first instance of the
  "algebraic structure produces coincidental unit distances" principle that
  problem.md names as the productive framing for the chromatic search.
- **Distinct-distances lower bound (Problem B):** any n points in the plane
  determine at least roughly n / log n distinct distances (a lower bound of the
  form c·n/log n). This is the companion extremal statement.
- Together with Spencer–Szemerédi–Trotter's later O(n^{4/3}) upper bound
  (1984), these pin the unit-distance problem between n^{1+Ω(1/log log n)} and
  n^{4/3}: density of unit-distance graphs is sharply bounded, so high
  chromatic number must come from rigidity, not density.

## Why it matters here

problem.md's claim "a unit-distance graph on n points has O(n^{4/3}) edges, so
density cannot be bought" rests on this line of work. This source is the
starting point of that line and the first construction of many coincidental
unit distances (the grid), which is also the natural seed family for the run's
own constructions.

```claim
id: erdos-1946-unit-distance-grid-lower
statement: There exist n-point subsets of the plane determining Ω(n log n) unit distances (structured grid/lattice construction); and any n-point set determines at least c·n/log n distinct distances.
hypotheses: Points in R^2; Euclidean distance; n finite.
holds-here: true — establishes that algebraic/grid structure creates many coincidental unit distances (the density that rigidity-based chromatic attacks exploit); also fixes the lower side of the unit-distance counting problem.
status: sourced (Erdős 1946; statement via read_sources summary and survey restatements)
bearing: Supplies the seed construction family (integer/triangular grids) for the run's construction search; bounds how much density a unit-distance graph can have.
anchor: research/sources/erdos-sets-of-distances-1946.md
```

## Note on download

Full text blocked at network layer. Content from read_sources summary plus the
Pach–Raz–Solymosi restatement of the 1946 problems. Status: **sourced via
read_sources; full text not on disk.**