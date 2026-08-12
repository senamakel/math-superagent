# Ellipse — Wolfram MathWorld

[[research/sources/ellipse-mathworld.full.md]] · source:
https://mathworld.wolfram.com/Ellipse.html

## What it establishes

The encyclopedic reference for the ellipse, with the exact forms the solver
needs:

- **Definition**: locus of points with r₁ + r₂ = 2a, foci F₁, F₂ distance 2c
  apart; a = semimajor, b = semiminor, b² = a² − c².
- **Polar equation with the pole at a FOCUS** (eq. 50):
      r(θ) = a(1−e²) / (1 + e·cos θ),   e = c/a = eccentricity.
  (r, θ measured from focus F; θ from the major-axis direction toward the other
  focus).
- Apoapsis/periapsis from the focus: r± = a(1±e).
- Focal parameter p = b²/c = a(1−e²)/e.
- General quadratic criterion (eq. 15–23), center/axes/rotation formulas.
- Area πab; perimeter via elliptic integrals.
- Explicitly notes: **the locus of centers of a Pappus chain of circles is an
  ellipse** (ties this entry to the Pappus-chain summary).

## Implication for PE620

The solver's discrete counting model needs, for each candidate planet center,
its distance r from a focus (the sun's center) as a function of the angle θ
from the C–S major axis. That is exactly eq. 50:
   with 2a = (c+s)/2π (sum of focal distances, planet size cancels), 2c = d
   (C–S center distance), e = d·2π/(c+s),
   r(θ) = a(1−e²)/(1+e·cos θ).
Each planet's center must be at distance (s+m)/2π from the sun center (m = p or
q) AND at a lattice angle (multiple of 2π/(c+s)); equating r(θ) with these
constants is the algebraic heart of the finite count.

## Cross-references

- Pappus chain / Steiner chain summaries: why the locus is this ellipse.
- Cut-the-Knot arbelos summary: AMM 1947 statement with rational
  parametrization.