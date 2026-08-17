# Refutation: CA in degree 6 over F_7 is false — NON-VACUOUS char-p counterexample

**Refuter finding.** Answer to the live question `rdc-charp-break` /
`redirect-refuter-to-rootdiff`: *"Is there a char-p input where the named break
does NOT occur (which would mean the break is mis-located)?"* — **YES**, and
here it is.

## Statement attacked

CA for degree 6 over F_7, Hasse-derivative formulation (the formulation of the
published bad-prime lists): a monic degree-6 f over F_7 sharing a root with
each Hasse derivative H_1..H_5 is a pure power (x−a)^6.

## Witness (derived by hand, confirmed entry-for-entry by find_counterexample)

```
f(x) = x^6 - x^2  over F_7
```

- Roots over F_7: x^2 (x^4 − 1) = x^2 (x−1)(x+1)(x^2+1).  6 is a non-square
  mod 7, so x^2+1 is irreducible over F_7: roots are {0 (mult 2), 1, 6} in
  F_7, + two roots in F_49.  THREE distinct F_7-roots ⇒ **not a pure power**.
- Hasse derivatives (H_i = Σ_j C(j,i) c_j x^{j−i}; c_6 = 1, c_2 = −1; all mod 7):

| i | H_i | mod 7 | zeros on F_7 | common root with f |
|---|---|---|---|---|
| 1 | 6x^5 − 2x | 6x^5 + 5x | {0} only | 0 |
| 2 | 15x^4 − 1 | x^4 − 1 | {1, 6} | 1 (and 6) |
| 3 | 20x^3 | 6x^3 | {0} only | 0 |
| 4 | 15x^2 | x^2 | {0} only | 0 |
| 5 | 6x | 6x | {0} only | 0 |

  H_1's only F_7-zero is 0: 6x^4+5 = 0 ⇒ x^4 = −5·6^{−1} = −5·6 = −30 ≡ 5, and
  the 4th powers of nonzero residues mod 7 are {1,2,4}, never 5.
  H_2's zeros solve x^4 = 1 ⇒ x ∈ {±1} = {1,6}, both roots of f.
  Numerics: f = (0,0,4,6,6,4,0); H_1 = (0,4,6,3,4,1,3); H_2 = (6,0,1,3,3,1,0);
  H_3 = (0,6,6,1,6,1,1); H_4 = (0,1,4,2,2,4,1); H_5 = (0,6,5,4,3,2,1) — all
  recomputed by hand (Fermat: x^6 = 1 for x ≠ 0, so f(x) = 1 − x^2; x^5 = 1/x).

## Engine result

`find_counterexample` on `code/refute/ca_deg6_char7.p` returned **refuted**
(CounterSatisfiable).  The 7-element model's f, h1..h5 tables match the hand
computation over F_7 entry-for-entry; all 21 pairwise-distinct axioms keep the
domain the genuine field F_7.  Hypothesis (a shared root with each H_i)
satisfied; conclusion (exactly one zero ⇒ pure power) falsified (three zeros).

## Why this is NOT just another char-p refutation

1. **No derivative degenerates: the named vacuity break does NOT occur here.**
   p = 7 > n = 6, so **no** binomial coefficient C(6,i) vanishes mod 7 and every
   H_i is a genuine nonzero polynomial.  The run's `rdc-charp-break` naming
   locates the char-p break in "per-color vacuity H_i ≡ 0 for middle i (Lucas)"
   of the witness x^{p+1}−x^p.  This witness shows vacuity is **not necessary**
   for the char-p falsehood: all five colors are real constraints, none
   vacuous, and the coloring {0: i ∈ {1,3,4,5}; {1,6}: i = 2} still does not
   collapse 0 and 1.  The collapse step must fail here for a reason other than
   derivative degeneracy — the missing char-0-only ingredient (Gauss-Lucas /
   convex-hull propagation, in the approach's own account) is exposed alone.
   The named break as "the" break is **mis-located if stated as per-color
   vacuity**; correct statement: char-p falsehood persists with no degeneracy,
   so the char-0-only collapse step is the whole obstruction, and it must
   survive a test against THIS witness (all H_i ≠ 0), not just against the
   x^{p+1}−x^p family.
2. **The centroid-descent break p | n−1 also does NOT occur**: p = 7 ∤ 5 = n−1,
   and the pinned centroid is 0 (a_1 = 0), which IS a root of f — the pinned
   centroid condition holds, and still no collapse.
3. **Published bad prime, corroborated, not new:** 7 is the third entry of the
   held degree-6 bad-prime list (castryck2012 Table 1: 2 | 5 | 7 | 11 | 13 | 19
   | 23 | 29 | 37 | …).  This is the first engine refutation at n=6 with all
   Hasse derivatives nonzero (n=6 p=2 and p=5 refutations both rely on H_i ≡ 0),
   and the explicit polynomial realizing the sufficient binomial criterion:
   **7 | C(6,2) − 1 = 14**, and x^6 − x^2 is the concrete witness.
4. It does NOT touch any char-0 claim (R-ca-deg4, R-ca-deg6-over-Q etc. remain
   untouched; CA over Q in degree 6 is settled true by the literature and is a
   separate statement).

## Honest verdict

`refuted` for "CA holds in degree 6 over F_7" — a published known-bad prime
corroborated by a non-vacuous witness.  The substantive finding: the char-p
break is NOT (only) Lucas vacuity; a fully non-degenerate char-p failure
exists, pinning the entire obstruction onto the char-0-only collapse step and
requiring that step to be tested against this witness (every H_i ≠ 0) as well
as against x^{p+1}−x^p.

```claim
id: deg6-char7-nonvacuous-refuted
statement: CA in degree 6 over F_7 is false in the Hasse-derivative
  formulation: f = x^6 − x^2 has three F_7-roots {0 (mult 2), 1, 6} (not a
  pure power), and shares a root with each Hasse derivative H_1=6x^5+5x,
  H_2=x^4−1, H_3=6x^3, H_4=x^2, H_5=6x, ALL NONZERO (p = 7 > n = 6, so no
  binomial coefficient vanishes: no Lucas per-color vacuity).  Hence p=7 is a
  bad prime for n=6, matching the published degree-6 bad-prime list (Castryck
  et al. 2012 Table 1: 2,5,7,11,...), and realizing the sufficient binomial
  criterion 7 | C(6,2)−1 = 14.  The char-p break is therefore NOT (only)
  per-color Hasse vacuity: a fully non-degenerate char-p failure exists, so
  the obstruction is the missing char-0-only collapse step (Gauss-Lucas /
  convex-hull propagation) above and beyond derivative degeneracy.
hypotheses: characteristic 7, degree 6, Hasse-derivative formulation of the
  char-p CA hypothesis (the formulation of the published bad-prime lists);
  f monic degree 6
holds-here: yes — answers the live rdc-charp-break question ("is there a char-p
  input where the named break does not occur?") affirmatively; constrains any
  char-0 collapse-step argument to survive a test where no derivative
  vanishes; does NOT bear on char-0 rungs, which remain open/separate
status: checked — engine-refuted on code/refute/ca_deg6_char7.p (7-element
  model's f,h1..h5 tables match x^6−x^2 and its five Hasse derivatives over
  F_7 entry-for-entry, recomputed by hand); 7 confirmed in the published
  degree-6 bad-prime list (castryck2012 Table 1, lines 164-165 of the held
  full text)
anchor: code/refute/ca_deg6_char7.p; research/sources/castryck2012_degree12_html.full.md Table 1
falsifies: a claim that the char-p failure of any CA collapse step is
  explained BY per-color Hasse vacuity (Lucas) alone — this witness has zero
  vacuity and still fails; or a version of the collapse step that holds over
  F_7 at n=6 (i.e. proves a false char-p statement)
```