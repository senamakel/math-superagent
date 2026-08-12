# Apollonius' Problem — Wolfram MathWorld

[[research/sources/apollonius-problem-mathworld.full.md]] · source:
https://mathworld.wolfram.com/ApolloniusProblem.html

## What it establishes

Apollonius' problem: given three objects (points, lines, circles), construct all
circles tangent to each. Ten cases; the hardest is three given circles, with up
to eight solution circles (the "Apollonius circles"), obtained by solving three
simultaneous quadratics in the unknown center (x,y) and radius r for the eight
sign choices of internal/external tangency:

    (x−x_i)² + (y−y_i)² − (r ± r_i)² = 0,  i = 1,2,3.

For the two-circle sub-case, the tangency equations reduce to a locus: a
quadratic equation in x, y (with r eliminated), which is the ellipse/hyperbola
locus of centers (see MathWorld's equation 4: expanding and subtracting pairs
gives linear relations; the centers lie on the conic with the two given centers
as foci).

## Implication for PE620

The problem of a single planet tangent to C and S is exactly the *two-given-
circles* Apollonius case (one circle inside the other): the tangency equations
give the ellipse locus of planet centers. This is the encyclopedic entry fixing
the statement and names ("Apollonius circles", "Problem of Apollonius",
Gergonne construction, Van Roomen hyperbola approach) and its standard
algebraic form is the one used to write the discrete count.

Also relevant: the *three*-circle Apollonius construction is what would decide
whether a circle tangent to a given planet AND C AND S exists — but PE620 does
not require planets to touch each other (overlap allowed), so the single-planet
(two-circle) case is the one that counts.

## Cross-references

- Eppstein Geometry Junkyard "Apollonian circles" (same library): the 8
  Apollonius solutions, compass-straightedge construction, inversion argument.
- Cut-the-Knot / Pappus / Steiner: ellipse locus of the two-circle case.