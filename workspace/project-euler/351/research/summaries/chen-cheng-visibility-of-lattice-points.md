# Chen–Cheng, "Visibility of lattice points" (Acta Arith. 107(3), 2003)

<!-- source: https://www.impan.pl/shop/en/publication/transaction/download/product/81923?download.pdf= (open-access IMPAN PDF) -->

## Bibliographic anchor

- Yong-Gao Chen (Nanjing) and Lin-Feng Cheng (Xuzhou), *Visibility of lattice points*,
  Acta Arithmetica **107** (2003), no. 3, 203–207. DOI 10.4064/aa107-3-1.
- Open-access PDF at impan.pl (this library: `research/sources/chen-cheng-visibility-of-lattice-points.full.md`).

## What it establishes

The canonical modern definition used across the visibility literature:

- Two integer points P(a₁,…,aₖ) and Q(b₁,…,bₖ) are **visible to each other** iff
  P = Q or the segment PQ contains no other integer point; for P ≠ Q this holds iff
  **gcd(a₁−b₁, …, aₖ−bₖ) = 1**.
- A set A is visible from a set B if every point of A is visible from some point of B.
- Main results (extremal, for the Erdős–Gruber–Hammer question): with
  ∆ₖₙ = {(x₁,…,xₖ) ∈ ℤᵏ : 1 ≤ xᵢ ≤ n} and fₖ(n), Fₖ(n) the minimum size of a set
  from which ∆ₖₙ is visible (S ⊂ ℤᵏ resp. S ⊆ ∆ₖₙ):
  - fₖ(n) ≥ ζ(k)·log n·log log n·(1+o(1))  (Theorem 1, k ≥ 2)
  - Fₖ(n) ≤ ζ(k−1)·log n·log log n·(1+o(1))  (Theorem 2, k ≥ 3)

## Why it is in this library

Fixes, from a peer-reviewed Acta Arithmetica source, the **visibility criterion in
lattice coordinates**: P visible from the origin iff gcd of the coordinate
differences is 1. This is the same criterion this run's governing lemma uses for the
hexagonal orchard (axial coordinates (a,b): hidden iff gcd(|a|,|b|) > 1), now with
the general-k statement and the Erdős–Gruber–Hammer context. The extremal theorems
are context only — PE 351 is an exact count, not an extremal question.

## Not established here

Nothing in this paper computes H(n) or Φ(n); it is a reference for the visibility
definition and the surrounding literature, not for the answer.
