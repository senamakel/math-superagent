# Goins–Harris–Kubik–Mbirika, "Lattice point visibility on generalized lines of sight"

<!-- source: https://arxiv.org/abs/1710.04554 (also https://arxiv.org/html/1710.04554v1) -->

## Bibliographic anchor

- Authors: Edray Herber Goins, Pamela E. Harris, Bethany Kubik, Aba Mbirika.
- arXiv:1710.04554 [math.NT], submitted 2017-10-12; **published** American Mathematical
  Monthly **125 (2018), No. 7, 593–601**, DOI 10.1080/00029890.2018.1465760.
- Full text also at https://arxiv.org/html/1710.04554v1 (this library: `research/sources/arxiv-1710.04554-goins-html.full.md`).

## What it establishes

For fixed b ∈ ℕ, a point (r,s) ∈ ℤ×ℤ is **b-visible** from the origin if it lies on the
graph of a power function f(x) = a·x^b with a ∈ ℚ and no other integer lattice point lies
on that curve between (0,0) and (r,s).

- Main theorem: the proportion of b-visible integer lattice points is **1/ζ(b+1)**.
- For b = 1 (straight lines of rational slope through the origin) this recovers the
  classical result: the proportion of lattice points visible from the origin is
  **1/ζ(2) = 6/π² ≈ 0.607927**.
- Although the visible proportion tends to 1 as b → ∞, there exist arbitrarily large
  rectangular arrays of b-invisible points for every fixed b (a folklore fact in the
  b = 1 case: arbitrarily large gcd>1 square blocks).

## Why it is in this library

Fixes, from the modern literature, the classical visibility fact this run uses as its
governing lemma: a point (a,b) ∈ ℤ² is visible from the origin iff gcd(a,b) = 1
(b = 1 case), and the density of visible points is 6/π². The hexagonal orchard's
triangular lattice is a rank-2 lattice, so the criterion transfers (a point is hidden
iff gcd of its axial coordinates exceeds 1). The density 6/π² is the magnitude anchor
for Φ(N) ~ (3/π²)N², which the computed Φ(10⁸)/10¹⁶ = 0.303964 matches.

## Not established here

The paper's b > 1 results (curved lines of sight) are not needed for PE 351; recorded
as context. The b = 1 recovery is the part this run relies on, and it is independently
established by MathWorld VisiblePoint and the brute-force oracle (gcd test) in this run.
