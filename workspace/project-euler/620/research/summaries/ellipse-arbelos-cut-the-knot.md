# Ellipse in Arbelos (Cut-the-Knot) — locus of circles tangent to two circles

[[research/sources/ellipse-arbelos-cut-the-knot.full.md]] · source:
https://www.cut-the-knot.org/Curriculum/Geometry/EllipseInArbelos.shtml
(problem E 762, American Mathematical Monthly Vol. 54 No. 9, Nov 1947, Van Andel / Anning)

## Result (part a)
Let A1, A2 be two circles with radii a1 < a2, centers distance d apart, one inside the
other such that a circle C in the crescent between them is tangent to both A1 and A2.
Then the **locus of centers of C is an ellipse** with foci at the two centers: the sum
of distances from the center of C to the two circle centers is constant = a1 + a2.
- major semiaxis = (a1 + a2)/2.
- minor semiaxis = sqrt(a1·a2)  (from right triangle: h² = [(a1+a2)/2]² − [(a2−a1)/2]²
  = a1·a2 when centers are collinear at distance a2 − a1).

## Result (part b): rational parametrization
With the inner circle center at the origin and cotangent-circle center at distance d:
φ_t = a1·a2 + t²(a2 − a1)², and the tangent circle Ct has
- radius r_t = a1·a2·(a2 − a1)/φ_t,
- x_t = a1·a2·(a2 + a1)/φ_t,
- y_t = 2t·r_t,
for every real t. Ct is tangent to A1, A2.

## Implication for PE620
Mount the sun S (radius s/2π, off-centre inside C of radius c/2π) with its center at
distance d from C's center. Every planet of radius p/2π (p<q) tangent to both C and S
has its center on an **ellipse** with foci at C's center and S's center, major semiaxis
(a1+a2)/2 where a1, a2 are the planet radius sums/differences. The continuous family of
positions of each planet is cut to a finite set by the least-mesh-angle quantization
(theta_hat = 2π/(s+c)).

```claim
id: tangent_circle_center_ellipse
statement: The center of a circle tangent to two fixed circles (one contained in the
other, crescent region) traces an ellipse whose foci are the two fixed centers and
whose sum of focal distances equals the sum of the two fixed radii (a1 + a2). Equivalently,
the set of centers of circles of fixed radius r tangent internally to a circle of radius
R and externally to a circle of radius s inside it is an ellipse (when the tangency
region is the crescent).
hypotheses: the given circles are disjoint with one inside the other; the tangent
circle lies in the annular crescent and touches one internally, the other externally.
holds-here: true — in PE620 the planet (radius p/2π) is tangent internally to C
(radius c/2π) and externally to S (radius s/2π); S lies inside C; planet center is
in the crescent.
status: sourced (Cut-the-Knot / AMM 1947; corroborated by UGA tangent-circle notes).
bearing: fixes the planet-center locus to an ellipse; combined with least-mesh-angle
quantization (2π/(s+c)) it gives the finite discrete set of legal planet positions.
anchor: research/summaries/ellipse-arbelos-cut-the-knot.md
```
