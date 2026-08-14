# Haase, Nill & Paffenholz, "Lecture Notes on Lattice Polytopes" (TU Darmstadt, 2012)

Source: https://math.ovgu.de/Institute/IAG/Lehrveranstaltungen/wise15/GP/_/ln_lattice_polytopes-version-by-paffenholz.pdf — full text at
`research/sources/haase-nill-paffenholz-lattice-polytopes.full.md`
[[haase-nill-paffenholz-lattice-polytopes.full]]

## What this source establishes

Fall-school lecture notes (Haase, Nill, Paffenholz; preliminary version 7 Dec
2012) covering lattice polytopes, Ehrhart theory, geometry of numbers,
reflexive/Gorenstein polytopes, and unimodular triangulations. Theorems
relevant to this run:

- **Ehrhart's Theorem (Thm 3.3.13).** For a lattice d-polytope P ⊂ R^d,
  ehr_P(k) = |kP ∩ Z^d| is a polynomial in k of degree d; its leading
  coefficient is vol(P) (Prop 3.3.16); the constant term is 1 (Cor 3.3.19);
  d!·c_j ∈ Z for all coefficients (Cor 3.3.21). The Ehrhart series is
  h*(t)/(1−t)^{d+1} with h* a degree-≤d integer polynomial, h*(1) = Vol(P)
  (Thm 3.3.13, Cor 3.3.18), h*_0 = 1 and h*_i ≥ 0 (Stanley, Thm 3.3.23).
- **Pick's Formula (Thm 2.2.1).** For a lattice polygon with i interior and b
  boundary lattice points, area = i + b/2 − 1.
- **Ehrhart–Macdonald reciprocity (Thm 3.3.27).** ehr_P(−k) = (−1)^d
  |int(kP) ∩ Z^d|.
- **Brion's Theorem (Thm 3.4.4),** Barvinok's algorithm (Thm 3.5.6, LattE
  implements it), Minkowski's theorems, the Flatness theorem.
- Lattice definition (Def 1.3.1), primitive vector = not a positive multiple
  of another lattice vector (Def 1.3.15); unimodular equivalence preserves
  lattice-point count and volume (Cor 2.1.4).

## Why it is in this library

The hexagon {(a,b) ∈ Z² : |a|,|b|,|a+b| ≤ n} is a lattice polygon, so
Ehrhart's theorem explains why |Orchard(n)| = 3n²+3n+1 is a quadratic
polynomial in n (the Ehrhart polynomial, leading coefficient = area 6·(√3/4)
in the lattice's own normalization — the count 3n²+3n+1 is the one this run
uses, from OEIS A003215). The primitive-vector definition (Def 1.3.15:
conv(0,v) ∩ Λ = {0,v}) is exactly the geometric meaning of gcd = 1 that the
orchard's visibility criterion uses. This is background that fixes the
geometry; it contributes no counting formula beyond the point count.

## What it does not settle

No hidden-point count, no totient identity, no hexagonal-orchard formula.
Not load-bearing for H(10^8) — the point count was already fixed by
A003215/brute.py; the notes confirm the structural reason (Ehrhart theory)
why it is a polynomial.

## Claims

```claim
id: ehrhart-lattice-polygon-count
statement: For a lattice d-polytope P, ehr_P(k) = |kP ∩ Z^d| is a polynomial
of degree d with constant term 1 and leading coefficient vol(P); for a lattice
polygon, Pick's formula area = i + b/2 − 1 holds.
hypotheses: P a lattice polytope in Z^d.
holds-here: yes — the orchard hexagon {|a|,|b|,|a+b| <= n} is a lattice
polygon, so |Orchard(n)| = 3n^2+3n+1 is its Ehrhart polynomial (matches
A003215 and brute.py).
status: sourced (Haase–Nill–Paffenholz, Ehrhart's Theorem 3.3.13, Pick
2.2.1, Ehrhart–Macdonald reciprocity 3.3.27)
bearing: fixes why the orchard's point count is a quadratic polynomial;
structural background only, not load-bearing for the hidden-point count.
anchor: research/summaries/haase-nill-paffenholz-lattice-polytopes.md
```
