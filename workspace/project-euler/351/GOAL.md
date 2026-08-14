# Goal

Solve Project Euler 351: hexagonal orchards.

## Restatement (pinned down by the oracle)

A **hexagonal orchard of order n** is the set of triangular-lattice points
inside a regular hexagon of side n centred on a lattice point (the "center"),
boundary included. In 60° axial coordinates:

    Orchard(n) = { (q, r) ∈ ℤ² : |q| ≤ n, |r| ≤ n, |q+r| ≤ n }   (3n²+3n+1 points)

A point **P is hidden from the center** iff there is an orchard point
strictly between the center and P, i.e. on the same ray and strictly closer.
Closeness is exact integer squared norm q²+qr+r²; same-ray ⇔ cross product
q1·r2 == r1·q2 in the 60° basis.

## Worked examples (test oracle)

| n | H(n) stated | oracle output |
|---|-------------|---------------|
| 5 | 30  | 30 (literal and gcd methods agree) |
| 10 | 138 | 138 (literal and gcd methods agree) |
| 1000 | 1177848 | 1177848 |
| 1..8 | — | matches OEIS A216453 (0,6,12,24,30,54,60,84) |

## Completion criteria

- code/brute.py reproduces every worked example. ✅ (this run)
- code/solution.py computes H(10⁸) by an exact, polynomial method, agreeing
  with brute.py wherever brute can reach, and verified by an independent route.
- Final answer reported with the verification command.