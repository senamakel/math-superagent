# Siegel's theorem on integral points — summary

Source: https://en.wikipedia.org/wiki/Siegel's_theorem_on_integral_points
Full text: `research/sources/siegel-theorem-integral-points.full.md`

## What it establishes

**Statement.** For a smooth algebraic curve C of genus g > 0 defined over a
number field K, presented in affine space in a given coordinate system, there
are only finitely many points on C with coordinates in the ring of integers O
of K.

- Proved by C.L. Siegel, 1929 — the first major Diophantine result depending
  only on the genus, not on the special algebraic form of the equation.
- For g > 1 it was superseded by Faltings' theorem (1983).
- History: 1926 Siegel proved it *effectively* in the special case g = 1,
  conditionally on Mordell's conjecture. 1929 he proved it unconditionally by
  combining Thue–Siegel–Roth with Mordell–Weil. 2002 Zannier–Corvaja gave a
  new proof via the subspace theorem.

## Effectiveness (the point that matters for this run)

- Siegel's result was **ineffective for g ≥ 2** (as is Thue's method in
  Diophantine approximation generally).
- Siegel proved it *effectively only in the special case g = 1* (1926).
- Effective results in some cases derive from **Baker's method**.

## Why it is in this run's library

This is MRSTT's ref [26] — the theorem underlying the claim that for bounded
`(m,m')` the binomial-equalities equation has finitely many integral solutions
[Beukers–Shorey–Tijdeman], and the mathematical anchor of the whole
"finiteness is not a bound" obstruction. For each fixed `(k1,k2)` with
genus ≥ 1, C(x,k1)=C(y,k2) has finitely many integral points by Siegel; but the
bound is not computable in `(k1,k2)` (ineffective for genus ≥ 2; only genus-1
effective special case, and even there via Baker with constants that grow with
the pair). So it delivers per-pair finiteness — already known — and no uniform
bound. This is exactly the effective-versus-uniform gap the run must name on
every claim.

## Claim

```claim
id: siegel-integral-points-ineffective
statement: A smooth algebraic curve of genus g>0 over a number field K has only
  finitely many O_K-integral points. For g>=2 this is ineffective (no computable
  bound in the coefficients); only the g=1 case has an effective form (Siegel 1926,
  conditional, via Baker's method with constants growing with the pair).
hypotheses: genus>0, smooth curve over a number field
holds-here: yes — C(x,k1)=C(y,k2) for each fixed distinct pair has genus>=1,
  so Siegel gives per-pair finiteness; but the bound is not uniform/effective in (k1,k2).
status: asserted by source (encyclopedic entry)
bearing: per-pair finiteness of C(x,k1)=C(y,k2) is already known and ineffective;
  it cannot give Singmaster's uniform bound. This is the wall every approach must beat.
anchor: research/sources/siegel-theorem-integral-points.full.md
```
