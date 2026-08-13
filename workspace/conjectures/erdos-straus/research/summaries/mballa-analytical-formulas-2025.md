# Mballa, "Partial Resolution of the Erdős–Straus, Sierpiński, and Generalized Erdős–Straus Conjectures Using New Analytical Formulas" (2025)

Source: https://arxiv.org/abs/2502.20935 (arXiv:2502.20935, 28 Feb 2025),
Philemon Urbain Mballa.
Full text: `research/sources/mballa-analytical-formulas-2025.full.md`

## What it establishes (sourced, preprint)

An equivalent reformulation of the ESC as a **perfect-square condition**:

The equation `4/n = 1/x + 1/y + 1/z` is equivalent (with `t` parametrising
the two-denominator part) to the existence of `(x, t)` such that

```
q² = t²(4x − n)² − 2nxt         (a perfect square)
```

with `q ∈ N`. When such a square exists, the formulas give explicit y, z
(roots of the quadratic `V² − (4x−n)(2t)V + 2nxt = 0`).

**Theorems 1–3** give the reduction in three forms (divisibility condition →
square condition → Vieta-roots), and **Theorem 4** generalises to any
`a ≥ 4` (the generalised Erdős–Straus/Sierpiński/Schinzel setting):
the conjecture holds for all n ≥ N₀ iff such (x, t) and square exist.

**Conjectures 1–4** (strong: integer t; weak: rational t; generalised):
Conjecture 1 is *equivalent* to the classical ESC. So the whole problem is
reduced to: *for every n ≥ 2, find x, t with t²(4x−n)² − 2nxt a perfect
square.*

## Relation to the library

- The same author's later work (`mballa-unified-parametric.full.md`, in
  library) is the stronger/parametric version: introduces the function
  F⁽ᵏ⁾_{x,t}(n) = t²(kx−n)² − 2nxt, whose perfect-square values are exactly
  the solutions; Zero Lemma: a zero of F in the admissible domain occurs at
  the domain's upper bound and gives symmetric solutions (y = z).
  That paper proves symmetric solutions for all n ≡ 0,2,3 (mod 4) and, for
  n ≡ 1 (mod 4), for all n having a divisor b ≡ 3 (mod 4) — a density-1
  subset of n ≡ 1 (mod 4).
- So both Mballa papers share the "reduce ESC to a square search" shape.

## Consequences for this run

Reformulating the target as a perfect-square condition `q² = t²(4x−n)²−2nxt`
is one of the *equivalent* settings the run could adopt as its fixed
parametrisation (GOAL.md asks to fix one). The evaluation is elementary: for
n = 840k+1, a candidate polynomial family `x(k), t(k)` makes the RHS a
polynomial in k; asking it to be a square for all k is a strong Diophantine
constraint that can be checked symbolically (a polynomial that is a square
for infinitely many integers must be a perfect square of a polynomial).
Status: preprint; Theorem 1–4 are exact algebraic equivalences (verifiable
directly), the conjectures are open.

```claim
id: mballa-square-reformulation
statement: 4/n = 1/x+1/y+1/z has a solution iff there exist x, t ∈ N with t²(4x−n)² − 2nxt a perfect square; the y, z are then the roots of V² − (4x−n)(2t)V + 2nxt = 0. (Equivalent to ESC by Conjecture 1 of the paper.)
hypotheses: n ≥ 2.
holds-here: true — an exact algebraic reformulation; generalises to a ≥ 4.
status: asserted (preprint Theorems 1–4 with proofs in full text; algebra verifiable).
bearing: a second fixed-parametrisation candidate; the square condition for n = 840k+1 is a polynomial-square constraint when x,t are polynomials.
anchor: research/sources/mballa-analytical-formulas-2025.full.md
```