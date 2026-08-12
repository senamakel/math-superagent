# Frachebourg, Martin & Piasecki, "Ballistic aggregation: a solvable model of irreversible many-particle dynamics" — summary

<!-- source: https://arxiv.org/pdf/cond-mat/9911346 | L. Frachebourg, Ph. A. Martin, J. Piasecki, Physica A 279 (2000) 69–99; arXiv:cond-mat/9911346 -->

Full text at `research/sources/frachebourg_martin_piasecki_ballistic_aggregation.full.md` (62k chars).

## What the source establishes

Rigorous, exactly solvable treatment of 1D ballistic aggregation (perfectly
inelastic / sticky gas of point particles; mass and momentum conserved on
collision, kinetic energy dissipated).

- Derives the infinite hierarchy of kinetic equations for nearest-neighbour
  cluster distributions and shows it is **exactly equivalent to a system of
  two coupled equations** for a wide class of initial conditions (exact
  closure: the many-body distributions factorize into products of two-particle
  conditional distributions with the one-particle density).
- For Gaussian/white-noise initial velocities the model maps to a **Brownian
  motion with parabolic constraints**, giving closed analytical results for
  cluster masses, velocities, and shock statistics.
- These limiting distributions are **identical to the statistics of shocks in
  the (decaying) Burgers turbulence**.

Provides the rigorous "why the 1D ballistic aggregation / sticky gas is
classical and exactly solvable" backbone behind the pure (no-finish) bumper
race — the mathematical machinery (Brownian-parabolic-constraint map, exact
closure of the hierarchy) that MJMS later used to reach the convex-minorant /
random-permutation-cycles description.

## Why it is in the library

The survey report cited this paper ("Frachebourg–Martin–Piasecki 1999–2000
exact solutions") as part of the classical treatment of the pure problem, but
it was only a search hit, not a library file. Now the full text is on disk so
the "exactly solvable model" claim is citable from the primary source.

## Bearing on PE597

Like all no-boundary ballistic-aggregation work, this describes the **pure**
(finish-line-free) race — the warm-up, not the answer. The finite finish line
of PE597 (boats finishing/removed at x=L, not just by bumping) breaks the
mass-conserving sticky-gas and the no-boundary fan state; the finish event is
inverse-exponential, not an exponential clock (run-verified, see
`research/torpids_exact_combinatorics_report.md` §2). Nothing here transfers a
closed recursion for p(13,1800).

## Consistency with the run's record

Consistent with the run's own findings: the pure race = classical 1D ballistic
aggregation (convex minorant, random-permutation cycles); the finite finish
line is the unmodeled obstruction. No contradiction.