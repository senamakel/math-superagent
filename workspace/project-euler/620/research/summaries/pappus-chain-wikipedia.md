# Pappus chain — Wikipedia

[[research/sources/pappus-chain-wikipedia.full.md]] · source:
https://en.wikipedia.org/wiki/Pappus_chain

## What it establishes

A Pappus chain is a ring of circles between two tangent circles, each circle
externally tangent to the inner circle and internally tangent to the outer one
— again the abstraction of each PE620 planet touching ring C internally and sun
S externally.

Key facts:

1. **Centers on an ellipse.** The center P_n of each chain circle satisfies
     |P_n U| + |P_n V| = (r_U + r_n) + (r_V − r_n) = r_U + r_V = const,
   where U, V are the centers of the two given circles. Hence the locus is an
   ellipse with **foci at U and V** and major-axis constant r_U + r_V.
   — For PE620 this says each planet of radius ρ (circumference m) has its
   center on the ellipse with sum of focal distances (c/2π + s/2π) — the
   planet radius ρ cancels. Consistent with `tangent_circle_center_ellipse`.

2. **Explicit parametrization** (r = (1−r) ratio variant): centers at
     x_n = r(1+r) / (2[n²(1−r)² + r]),  y_n = n·r(1−r) / (n²(1−r)² + r),
   radius r_n = (1−r)r / (2[n²(1−r)² + r]).
   This gives a clean algebraic parametrization of the tangent-circle family:
   the center is a rational function of the (continuous) index n.

## Implication / gap

Confirms the continuous 1-parameter tangent family lives on an ellipse and
furnishes an explicit algebraic (rational) parametrization of the centers — the
algebraic object the least-mesh-angle lattice (multiples of 2π/(c+s)) must be
intersected with. The discrete half comes from the gear sources (Drivetrain
Hub / UTS / Handbook).

## Cross-references

- Steiner chain (same library): same locus theorem, porism.
- Drivetrain / UTS / Handbook: least-mesh-angle quantization.
- Cut-the-Knot arbelos summary: AMM 1947 original statement.

```claim
id: pappus_center_ellipse_params
statement: The centers of circles tangent externally to an inner circle (radius
r_U) and internally to an outer circle (radius r_V) lie on the ellipse with foci
at the two given centers and sum of focal distances r_U + r_V; the family is
rationally parametrized by x_n = r(1+r)/(2[n^2(1-r)^2+r]), y_n = n r(1-r)/(n^2(1-r)^2+r).
hypotheses: two given circles, inner one enclosed by outer one; each chain circle
tangent to both, in the annular crescent.
holds-here: true — PE620 sun S (radius s/2π) inside ring C (radius c/2π); planet
tangent internally to C and externally to S; sum of focal distances (c+s)/2π.
status: sourced (Wikipedia Pappus chain, citing Ogilvy Excursions in Geometry;
corroborates tangent_circle_center_ellipse).
bearing: fixes the continuous tangent family to a rational parametrization of an
ellipse; the discrete count intersects it with the least-mesh-angle lattice.
anchor: research/summaries/pappus-chain-wikipedia.md
```
