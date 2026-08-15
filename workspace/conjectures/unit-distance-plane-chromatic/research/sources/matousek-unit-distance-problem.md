# Matoušek lecture chapter — the unit distance problem in the plane

**Subject:** A canonical university-course treatment of the unit distance
problem that the run's O(n^{4/3}) density constraint derives from. University
course notes are a preferred source type for the library.

## Source
- J. Matoušek, *The unit distance problem*, lecture chapter (Charles University,
  Prague), https://kam.mff.cuni.cz/~matousek/u.pdf. Retrieved via
  `read_sources` (server-side).

## What it establishes

- In the Euclidean plane, the maximum `u(n)` of unit-distance pairs among `n`
  points satisfies `u(n) = Omega(n^{1+c/log log n})` (Erdős, from the
  `sqrt{n} x sqrt{n}` grid) and `u(n) = O(n^{4/3})` — the upper bound due to
  **Spencer–Szemerédi–Trotter 1984**, based on the incidence method of
  Szemerédi–Trotter 1983.
- Erdős conjectured `u(n) = O(n^{1+epsilon})` for every fixed epsilon; the
  `O(n^{4/3})` upper bound is still the best known and is the foundation for
  the density-cannot-be-bought reading in `problem.md`.
- Alternative proofs of the SST bound are recorded: Clarkson et al. 1990,
  Aronov–Sharir 2002, and the simplest by Székely 1997 (crossing-number
  method). Székely's crossing-number proof is the structural route the run can
  hold in mind as the two-line justification.
- The chapter also treats the problem for general norms: `u(n) = Omega(n log n)`
  for all norms, and the Euclidean upper bound carries to most norms up to an
  `O(log log n)` factor.

## Why it matters here

- Fixes the *tightness* of the O(n^{4/3}) unit-distance bound and its
  incidence-geometric proof route, so the run does not have to re-derive it and
  knows the bound cannot be dodged (a high-chromatic UDG must be rigid, not
  dense-random).
- Records the alternative proof methods so the researcher can cite a route
  (Székely crossing-number) if the unit-distance constraint needs to be
  reapplied in a strict form.
- This is the exact context that says a random point set has almost no unit
  edges — the "search over constructions, not points" rule of `problem.md`.

## Basis and status
- Statements = sourced (retrieved verbatim; standard textbook/course content).
- Not re-verified computationally here (asymptotic theorem).

## Claim block
```claim
id: unit-distance-dense-upper-bound-tight
statement: u(n), the max unit-distance pairs among n plane points, satisfies
  Omega(n^{1+c/log log n}) <= u(n) <= O(n^{4/3}); the upper bound is the
  classical Spencer-Szemeredi-Trotter 1984 result proved via point-circle
  incidences / the Szemeredi-Trotter incidence theorem, with simpler proofs by
  Szekely (crossing number), Clarkson et al., and Aronov-Sharir.
hypotheses: finite point sets in the Euclidean plane, pair at distance exactly 1.
holds-here: YES — same setting as the run's unit-distance graphs; the O(n^{4/3})
  edge budget is what rules out random-dense graphs and pushes the search to
  rigid algebraic constructions.
status: asserted-by-source (course notes + the primary SST 1984 attribution and
  alternative proofs).
bearing: restates and confirms research/sources/spencer-szemeredi-trotter-unit-distance-bound.md
  from an independent, teaching-grade source; fixes the density constraint
  exactly.
anchor: research/sources/matousek-unit-distance-problem.md
falsifies: a construction of n plane points with > C n^{4/3} unit distances for
  all C — would contradict a classical theorem; none known.
```
