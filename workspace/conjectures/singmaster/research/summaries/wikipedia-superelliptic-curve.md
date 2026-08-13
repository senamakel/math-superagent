# Wikipedia — Superelliptic curve (background)

Source: https://en.wikipedia.org/wiki/Superelliptic_curve (converted HTML in
`research/sources/wikipedia-superelliptic-curve.full.md`).

## What it defines (background only, secondary source)

A **superelliptic curve** is `y^m = f(x)`, `m ≥ 2`, `f` degree `d ≥ 3`; the smooth
projective curve with that function field. Kummer theory gives the affine model
when a k-rational point exists and roots of f have order < m. Special cases:
`m=2, d=3,4` elliptic; `m=2, d≥5` hyperelliptic; `m=3, d≥4` trigonal.

- **Ramification**: branch points are the roots of f (and ∞ if m ∤ deg f);
  ramification index over α is `m/(m, r_α)` where `r_α` = root order; the curve
  is connected iff gcd of all `m, r_α` is 1.
- **Genus (Riemann–Hurwitz)**: `g = (1/2)(m(|B|−2) − Σ_α (m, r_α)) + 1`.
  This is the formula the run's `{3,n}` cyclic-trigonal and `{2,n}` hyperelliptic
  closed forms rest on (`Y³−Y = 6C(x,n)` is `m=3` superelliptic; the run's
  derive_files in code/genus/verify_superelliptic_formula.py implement it).
- **Diophantine problem**: via a Siegel identity to a Thue equation; Shorey–
  Tijdeman (Exponential Diophantine Equations, 1986) give effective bounds:
  for f with ≥ 2 distinct roots, all integer solutions with variable exponent
  `m ≥ 3, |y| ≥ 2` are bounded by an effectively computable constant of f;
  and the general `wz^m = F(x,y)` S-unit version (their Thms 10.6/10.7).

## Bearing for this run

- **Background only, secondary source.** The genus formula corroborates the run's
  small-column genus computations at the definitional level (the run already has
  the primary BST 1999 Prop 4.1 genus formula, which is more general). The
  Shorey–Tijdeman effective bound reference is a pointer to the standard
  "effective but per-equation" result for superelliptic equations — the same
  effective-per-pair/no-uniformity shape as Matveev/BMSST.
- No new claim needed beyond the definitional one; the run's own
  `bugeaud-hyperelliptic-2008` note is the substantive effective-method source.

```claim
id: superelliptic-genus-riemann-hurwitz
statement: A superelliptic curve y^m=f(x) (f squarefree degree d>=3) has genus
  g = 1/2 (m(|B|-2) - sum_alpha (m,r_alpha)) + 1, B = roots of f (plus infinity
  if m does not divide d), r_alpha = root orders; ramification index over alpha
  is m/(m,r_alpha). (Wikipedia; Riemann-Hurwitz.)
hypotheses: m coprime to characteristic; f squarefree; connectedness (gcd of m
  and the r_alpha = 1).
holds-here: yes — underlies the run's k2=3 cyclic-trigonal closed forms
  (Y^3-Y = 6C(x,n) is m=3 superelliptic); consistent with the primary
  BST 1999 Prop 4.1 genus formula and the computed grid.
status: checked
bearing: The run's own Riemann-Hurwitz derivation (genus-closed-form-derived-by-riemann-hurwitz, proved) now independently reproduces this formula as the m=2 special case of the general binomial-curve genus g(m,n) = ((m-1)(n-1)+1-gcd(m,n))/2 — the superelliptic formula for m=2, d=n gives g = floor((n-1)/2) which matches the closed form's {2,n} row.  No longer a catalogue-only entry.
anchor: research/sources/wikipedia-superelliptic-curve.full.md
```