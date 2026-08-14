# Adhikari–Granville, "Visibility in the plane" (J. Number Theory 129, 2009)

<!-- source: https://dms.umontreal.ca/~andrew/PDF/VisibleLatticePts.pdf (Granville's author copy) -->

## Bibliographic anchor

- Sukumar Das Adhikari and Andrew Granville, *Visibility in the plane*, Journal of
  Number Theory **129** (2009), 2335–2345. DOI 10.1016/j.jnt.2009.02.019.
- Author copy: https://dms.umontreal.ca/~andrew/PDF/VisibleLatticePts.pdf
  (this library: `research/sources/adhikari-granville-visibility-in-the-plane.full.md`).

## What it establishes

- The **visibility criterion** (stated in the introduction, D ≥ 2): a ∈ ℤ^D is visible
  from b ∈ ℤ^D iff there is no lattice point on the open segment between them, which
  holds iff **gcd of the coordinates of a − b is 1**. In ℤ²: (a,b) visible from (c,d)
  iff gcd(c−a, d−b) = 1.
- A set A is visible from B if every point of A is visible from some point of B.
- Main results: for {1,…,N}^D, the smallest set from which it is visible has size
  **ζ(D)·log N / log log N · (1+o(1))** (Theorem 1, Corollary 2; lower bound
  Proposition 3, upper bound Proposition 4). This answers a question of Erdős et al.
  (Erdős, Gruber, Hammer) and extends the Abbott and Adhikari–Balasubramanian bounds.
- Theorems 5–9 refine the count for arbitrary compact convex sets S ⊂ ℝ² (visibility
  of S ∩ ℤ²) in terms of the slopes of S's boundary (L(N₊), L(N₋), convergents of α).

## Why it is in this library

This is the canonical modern reference for lattice-point visibility in the plane — the
subject this run's governing lemma belongs to. Its introduction states the exact
criterion used here: a hexagonal-orchard point with axial coordinates (a,b) is hidden
from the centre iff gcd(|a|,|b|) > 1 (visible iff gcd = 1), because the segment from
(0,0) to (a,b) contains a lattice point iff gcd(a,b) > 1. It also situates the
visibility problem in the Erdős–Gruber–Hammer literature, which the run's other
visibility sources (Chen–Cheng, Goins et al.) all cite.

## Not established here

The extremal results (size of smallest visible set) are not needed for PE 351 — that
is an exact count of hidden points, not an extremal covering problem. The definitional
criterion and the literature map are the parts this run relies on.

## Claim for the ledger

```claim
id: visibility-criterion-adhikari-granville
statement: In Z^D (D >= 2), a point a is visible from b (no lattice point on the open
segment between them) iff gcd of the coordinates of a - b equals 1. In the plane,
(a,b) is visible from (c,d) iff gcd(c-a, d-b) = 1; hence a lattice point is visible
from the origin iff its coordinates are coprime.
hypotheses: integer lattice Z^D, open segment contains no lattice point, D >= 2.
holds-here: yes — the hexagonal orchard is a rank-2 lattice (axial coordinates
(a,b) in Z^2), so a point is hidden from the centre iff gcd(|a|,|b|) > 1; the
brute-force oracle confirms this at n = 5, 10, 1000.
status: sourced (Adhikari–Granville, J. Number Theory 129 (2009) 2335–2345, intro;
corroborated by Chen–Cheng Acta Arith. 107 (2003) and MathWorld VisiblePoint, and
by this run's brute force).
bearing: fixes the governing lemma for the hidden-point count; reduces H(n) to the
totient identity via the count of non-coprime pairs in one sector.
anchor: research/summaries/adhikari-granville-visibility-in-the-plane.md
```
