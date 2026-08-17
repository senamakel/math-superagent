# Wikipedia — "Newton polytope"

Source URL: https://en.wikipedia.org/wiki/Newton_polytope
Full text: `research/sources/wikipedia_newton-polytope.full.md`.

## What it establishes

The Newton polytope of a multivariate polynomial `Σ c_α x^α`: the convex hull
of the exponent vectors `α` with `c_α ≠ 0`. For one variable this is an
interval; for the two-variable case it is the Newton polygon (Newton diagram).
Properties: the Minkowski sum of Newton polytopes corresponds to polynomial
multiplication (`Newt(f·g) = Newt(f) + Newt(g)`); the face structure records
which monomials dominate after a toric term order; links to toric varieties,
the Bernstein–Kushnirenko theorem (mixed volume counts common roots).

## Bearing on the run

- The weighted-order / initial-form analysis of the CA resultants: under
  `a_j ↦ t^j a_j` the Newton polytope of `R_i` degenerates to a point at
  weight `n(n−i)` (weighted homogeneity) — the run's Theorem A. The
  polytope/face vocabulary is what connects that to toric initial ideals
  (the `generic-initial-ideal` proposed approach) and to the tropical
  examples in Chávez Martínez 2018 (where CA holds classically but fails
  under a tropical definition).

Claim status: reference-level definitions; the Bernstein–Kushnirenko
statement is a theorem (cited to GKZ within the page).