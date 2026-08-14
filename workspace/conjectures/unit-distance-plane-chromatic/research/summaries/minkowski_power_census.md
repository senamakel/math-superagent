# Minkowski-power census of the calibrated spindle — chi(A^k) = 4, k = 1..6

Computed by `code/spindle_minkowski_census.py` (exact arithmetic) with
captures in `code/out/spindle_minkowski_census*.captured.txt`; extended by
`code/extend_spindle_census.py` (counts only, no colouring) in
`code/out/extend_spindle_census.captured.txt`; the polynomial structure of the
counts was computed by `code/minkowski_growth_fit.py` (exact Fraction
Lagrange interpolation) in `code/out/minkowski_growth_fit.captured.txt`.

## The construction

A = the 7-point calibrated spindle of `problem.md` (chi = 4, not 3; 11 exact
unit edges). A^k = the k-fold Minkowski sum. Because A is a unit-distance
graph, every A^k is; the edge set is re-certified from the coordinates at each
level rather than inherited.

## The measured table (exact)

| level | distinct points n | unit edges e | e/n | colour |
| --- | --- | --- | --- | --- |
| k=1 | 7 | 11 | 1.571 | chi=4 (calibration) |
| k=2 | 26 | 69 | 2.654 | chi=4, not 3 (two-way) |
| k=3 | 70 | 240 | 3.429 | chi=4, not 3 (two-way) |
| k=4 | 155 | 628 | 4.052 | chi=4, not 3 (two-way) |
| k=5 | 301 | 1375 | 4.568 | chi=4, not 3 (two-way) |
| k=6 | 532 | 2659 | 4.998 | chi=4, not 3 (two-way) |
| k=7 | 876 | 4694 | 5.358 | **not coloured** (counts only) |

Two-way = edges re-certified independently (brute exact field arithmetic AND
sympy), and colouring decided by a complete DSATUR test cross-checked by an
independently written plain backtracking colour test with a different witness
family; the two agree at every level through k=6. The k=6 graph (532 vertices,
2659 edges ≈ 5n) is the largest graph this run has colour-tested with two
agreeing complete methods; k=7's colouring was not attempted.

## The structural regularity in the counts (catalogued, not proved)

Exact Fraction interpolation through k=1..6 (`minkowski_growth_fit.py`):

- **n(k) is a quartic through k=1..6**: n(k) = 1 + (5/2)k + (7/3)k² + k³ +
  (1/6)k⁴ = (k⁴ + 6k³ + 14k² + 15k + 6)/6, with the degree-5 coefficient
  exactly 0. The fit through k=1..5 **predicted n(6) = 532 exactly** (an
  out-of-sample match), and the same quartic gives n(7) = 876, matching the
  later measured k=7 count — so the quartic is exact on the whole computed
  range k=1..7 with a genuine out-of-sample verification.
- **e(k) is not low-degree**: the degree-5 interpolation through k=1..6 has
  nonzero k⁵ coefficient −1/60 (fourth finite differences are 38, 36 — not
  constant), so e(k) is not a polynomial of degree ≤ 4 on the measured range.
- **e/n → ~5 observed**: e/n rises 1.57 → 5.36 across k=1..7. This is an
  observed trend on the computed range with NO proof for larger k; it shows
  the Minkowski-power construction produces very dense unit-distance graphs
  (≈5n edges, far above the 5-critical floor e ≥ 2n) that remain
  4-colourable — density alone does not force chromatic number in this
  family.

These are **catalogued regularities on the computed range**, not theorems
about the infinite family A^∞; the first falsifier of the quartic is the
smallest k > 7 with n(k) ≠ (k⁴+6k³+14k²+15k+6)/6 (unmeasured), and the
colour claims stop at k=6.

## What this establishes

- Compound Minkowski powers of a 4-chromatic seed remain **4-colourable**
  through k=6 (checked, two-way) — consistent with the El-Zahar–Sauer blocker
  (`product-chromatic-4chromatic`): chromatic number does not compound under
  product-like operations even at ≈5n edge density.
- The oracle pair is exercised at increasing size (up to 532 vertices / 2659
  edges colour-tested two ways; up to 876 vertices / 4694 edges counted) with
  two-way independent agreement throughout — the explicit largest-colour-tested
  size for the run's report.
- This is a census result about the construction class actually reached
  (A^k, k=1..7 for counts; k=1..6 for colouring). It bounds nothing beyond
  the measured levels and is not evidence about other construction families.

## Status

Colour verdicts k=1..6 `checked`; counts k=1..7 `checked`; polynomial
regularities `catalogued` (exact on computed range with out-of-sample
confirmation, not proved for all k); e/n trend `observed`, not proved.

```claim
id: minkowski-power-census
statement: For the calibrated 7-vertex spindle A (chi=4, not 3; problem.md construction), the Minkowski powers A^k have exact counts n=7,26,70,155,301,532,876 and e=11,69,240,628,1375,2659,4694 for k=1..7; chi(A^k)=4 (not 3-colourable, two independent complete colour tests agreeing) for k=1..6. n(k) = (k^4+6k^3+14k^2+15k+6)/6 exactly for k=1..7 (fit through k=1..5 predicted k=6 out-of-sample; quartic also matches k=7); e(k) is not a polynomial of degree <= 4 on the measured range. k=6 (532 vertices, 2659 edges ~5n) is the largest graph colour-tested two ways; k=7 counts-only.
hypotheses: A the exact calibrated spindle; A^k the k-fold Minkowski sum; all arithmetic exact (Q(sqrt3,sqrt11); sympy independent re-certification).
holds-here: yes — the run's own exact computation; the census deliverable in miniature; the explicit largest-colour-tested size; the quartic is a catalogued regularity on the computed range, not a theorem about A^infinity.
status: checked for counts k=1..7 and colours k=1..6; catalogued for the polynomial regularities (exact on the computed range, unproved beyond k=7).
bearing: reports the maximum chi attained by the run's own constructions (4); shows density ~5n does not force 5 colours in this family; gives the exact n(k) closed form on the swept range as a structural handle for the construction engine; marks the boundary (k=6 coloured, k=7 not) so claims do not outrun computation.
anchor: code/out/spindle_minkowski_census_k2..k6.captured.txt, code/out/extend_spindle_census.captured.txt, code/out/minkowski_growth_fit.captured.txt, code/spindle_minkowski_census.py, code/extend_spindle_census.py, code/minkowski_growth_fit.py
```

## Falsifier

The first computed level k with chi(A^k) > 4, or an independent exact re-run
disagreeing with any row above, or the first k > 7 where n(k) ≠
(k⁴+6k³+14k²+15k+6)/6.