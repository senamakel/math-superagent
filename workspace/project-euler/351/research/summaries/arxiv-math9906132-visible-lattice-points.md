# Baake, Moody & Pleasants, "Diffraction of visible lattice points" (arXiv:math/9906132)

Source: https://arxiv.org/pdf/math/9906132 — full text at
`research/sources/arxiv-math9906132-visible-lattice-points.full.md`.

## What this source establishes

Proves that the set of visible points of any lattice of dimension n ≥ 2 has
pure point diffraction spectrum, and determines it explicitly (Theorem 3),
settling earlier speculation. Related results: visible points of a lattice Γ
have natural density dens(V) = dens(Γ)/ζ(n) (Proposition 6, so 6/π² in 2D);
V is uniformly discrete with arbitrarily large holes; V − V = Γ (n ≥ 2); the
1-dimensional analogue for kth-power-free integers (Theorems 4–5).

**Relevant facts for this run:** the 2D density 6/π² of visible points (the
same constant as the probability two integers are coprime) — a magnitude
anchor for Φ(10⁸)/10¹⁶ ≈ 3/π² and H(10⁸)/10¹⁶ ≈ 3(1−6/π²). The diffraction
results themselves are not needed.

## Hypotheses

Lattice Γ ⊂ Rⁿ, n ≥ 2. Holds here for the rank-2 orchard lattice.

## What it lets this run do

- Independent academic confirmation of the 6/π² visible-point density used as
  the run's sanity anchor.

## What it does not settle

- No finite-region counting formula; no totient connection. Not load-bearing
  for the final answer.

## Claims

```claim
id: visible-point-density-zeta
statement: The visible points of a lattice Γ ⊂ R^n have density dens(Γ)/ζ(n)
(6/π² in 2D).
hypotheses: lattice Γ, n ≥ 2.
holds-here: yes — matches the run's Φ(10^8)/10^16 = 0.303964 ≈ 3/π² and
H(10^8)/10^16 = 1.17622 ≈ 3(1 − 6/π²).
status: sourced (Baake–Moody–Pleasants, arXiv:math/9906132, Prop. 6).
bearing: magnitude anchor only.
anchor: research/summaries/arxiv-math9906132-visible-lattice-points.md
```
