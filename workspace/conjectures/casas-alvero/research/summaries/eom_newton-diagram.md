# Encyclopedia of Mathematics — "Newton diagram" (Newton polygon / Puiseux diagram)

Source URL: https://encyclopediaofmath.org/wiki/Newton_diagram
Full text: `research/sources/eom_newton-diagram.full.md`.

(The page is titled "Newton diagram"; this is the EoM's name for the Newton
polygon method. The URL `.../Newton_polygon` returns 404 — this is the correct
page.)

## What it establishes

Newton's 1669 graphical method for determining the principal terms of an
algebraic function's expansion (Puiseux series). For an equation
`F(x,y) = 0`, plot the exponent pairs of the terms, take the lower convex
hull — the Newton diagram — and read off the possible leading exponents
(slopes of the hull's edges); each edge length counts the number of roots
with that leading exponent. Worked out by Puiseux; algebraic version by
Lagrange.

## Bearing on the run

- The problem directive names "Newton polygons of the one-variable eliminant"
  as an instrument: after eliminating the `r_i` from the CA scheme, or
  specialising the resultants `R_i` to one variable, the Newton polygon of
  the resulting polynomial-in-`t` records the leading exponents — which the
  run computes as `ord_0(R_i) = n(n−i)` under `a_j ↦ t^j a_j`. This entry is
  the canonical reference for that instrument.
- The singularity-theory origin (Casas-Alvero's higher-order polar germs and
  the García Barroso et al. 2025 held paper) uses Newton diagrams as the
  primary tool — this entry anchors that vocabulary.

Claim status: reference-level classical method (textbook facts).