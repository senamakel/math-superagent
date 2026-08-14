# Hensley, "The number of relatively prime pairs within a contour" (1994)

Source: https://msp.org/pjm/1994/166-2/pjm-v166-n2-p04-s.pdf — full text at
`research/sources/hensley-visible-lattice-points-contour.full.md`.

## What this source establishes

Estimates P(r), the number of relatively prime pairs (a,b) of positive
integers with a²+b² < r (or more generally within a convex contour), with
error terms that improve on the trivial O(r^{1/2+ε}):

    P(r) = (6/π)r + O_ε(r^{1/2} exp(−c√(log r)))

and, assuming RH, a better exponent; also a comparable estimate for the
divisor/lattice-point-under-hyperbola problem. The key parameter is the
maximum radius of curvature of the bounding contour (Theorem 1: uniform over
convex contours enclosing the origin with large enough perimeter).

## Hypotheses

Convex contours in R²; pairs (a,b) with gcd(a,b)=1. The contour here is the
hexagon, which is convex but the bound's applicability to the exact counting
problem is not established by the paper.

## What it lets this run do

- Nothing computational: the run's method is exact integer arithmetic, not an
  asymptotic estimate. This source confirms the general shape (visible-point
  counts in regions ~ 6/π²·area) but does not bear on the exact H(10⁸).

## What it does not settle

- No exact formula; no bound for the hexagonal contour; not load-bearing.

## Claims

```claim
id: primitive-pairs-contour-asymptotic
statement: P(r) = (6/π)r + O_ε(r^{1/2} exp(−c√log r)) for relatively prime
pairs in a circle of radius r; error depends on the contour's curvature.
hypotheses: convex contours, RH not needed for the first bound.
holds-here: yes (context only).
status: sourced (Hensley, Pacific J. Math. 166:2, 1994).
bearing: none for the exact answer — magnitude context only.
anchor: research/summaries/hensley-visible-lattice-points-contour.md
```
