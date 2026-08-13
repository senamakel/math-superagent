# Fuchs–Heintze 2021 — Diophantine equations in separated variables and polynomial power sums (PRIMARY, readable)

Source: Clemens Fuchs, Sebastian Heintze, Monatshefte für Mathematik 196:1
(2021) 59–65, DOI 10.1007/s00605-021-01560-6 (open access, PMC8550583).
Full text: `research/sources/separated-variables-survey-pmc.full.md` (this is
the complete paper, not a survey — the file name is a leftover).

## What it establishes

**Theorem 1.** Let `G_n(x) = a₁α₁(x)ⁿ + … + a_d α_d(x)ⁿ` and
`H_m(y) = b₁β₁(y)ᵐ + … + b_t β_t(y)ᵐ` be the n-th and m-th polynomials of
linear recurrence sequences of the "required shape" (dominant root condition
`deg α₁ > deg αᵢ`, at most one constant characteristic root, and the excluded
shape where the nonconstant part is a perfect power of a linear polynomial).
Assume `n, m > 2` and `G_n` indecomposable. Then

> `G_n(x) = H_m(y)` has infinitely many rational solutions with a bounded
> denominator **iff** there is a polynomial `P ∈ Q[y]` with
> `H_m(y) = G_n(P(y))` identically.

If `H_m` is also indecomposable, `P` may be taken linear.

The proof uses the **Bilu–Tichy criterion** (Theorem 2, restated verbatim: the
five standard pairs), ruling out each standard-pair kind in turn (first kind →
contradicts the recurrence shape; second kind → degrees > 2; third kind →
Dickson decomposition forces `deg α₁ = 1`; fourth kind → indecomposability;
fifth kind → n=4 or m=4 forcing `deg α₁ = 1`), then handling `deg φ = 1` and
`deg φ > 1` cases.

Remark 1 (arithmetic version): using Bilu–Tichy Theorem 10.5 rather than
1.1, the same result holds over any number field K with a finite set S of
places, for rational solutions with bounded O_S-denominator.

## Bearing for this run

- **Does NOT apply to the binomial family `C(x,k1)=C(y,k2)` directly**: those
  are fixed polynomials `x(x-1)…(x-k1+1)/k1!`, not polynomial power sums, so
  the recurrence-shape hypotheses (dominant root, at most one constant root,
  excluded perfect-power-of-linear shape) fail. The Binomial polynomials are
  not "of the required shape" as power sums.
- **Confirms the Bilu–Tichy structure** the run already relies on
  (`bilu-tichy-classification-primary`): the five standard pairs, and the
  mechanism that infinite-family cases are exactly the standard-pair /
  composition cases. This is an independent modern restatement of the BT
  criterion in a different (power-sum) setting.
- **Remark 1** is useful methodologically: the S-arithmetic version over
  number fields with O_S-denominator is exactly the shape the run's
  `sunit-subspace-inapplicable` note discusses (why the S-unit/Subspace route
  does not give a uniform bound). No new binomial content.

```claim
id: fuchs-heintze-power-sums-bt-criterion
statement: Fuchs-Heintze 2021 (Monatsh. Math. 196, 59-65, Thm 1): for
  polynomial power sums G_n, H_m of the required shape (dominant root, at most
  one constant root, nonconstant part not a perfect power of a linear
  polynomial) with n,m>2 and G_n indecomposable, the equation G_n(x)=H_m(y)
  has infinitely many rational solutions with bounded denominator iff
  H_m = G_n o P for some P in Q[y] (linear if H_m indecomposable). Proved via
  the Bilu-Tichy standard-pair classification (restated as Thm 2: the five
  kinds) and Dickson-composition/degree arguments.
hypotheses: polynomial power sums of the required shape; n,m > 2; G_n
  indecomposable; rational solutions with bounded denominator (or O_S-
  denominator over number fields, Remark 1).
holds-here: no — the binomial polynomials C(x,k1) are fixed-degree polynomials,
  not power sums; the recurrence-shape hypotheses fail. The Bilu-Tichy
  structure it restates is the run's already-held classification.
status: asserted (open-access full text read; statements quoted)
bearing: negative for Singmaster directly; positive as an independent modern
  restatement of the BT standard-pair criterion the run relies on for the
  ineffective-uniformity wall. No new binomial bound.
anchor: research/sources/separated-variables-survey-pmc.full.md
```