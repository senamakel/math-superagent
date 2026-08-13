# Viada (2003), "The intersection of a curve with algebraic subgroups in a product of elliptic curves" — CM case primary

[[viada-intersection-curve-algebraic-subgroups-product-elliptic-2003]]

Source: Evelina Viada, "The intersection of a curve with algebraic subgroups in
a product of elliptic curves", Annali della Scuola Normale Superiore di Pisa,
Classe di Scienze (4) 2 (2003), 47–75. Full text:
`research/sources/viada-intersection-curve-algebraic-subgroups-product-elliptic-2003.full.md`
(59.5 KB from http://archive.numdam.org/article/ASNSP_2003_5_2_1_47_0.pdf).

## What it establishes

C an irreducible curve defined over Q, transversally embedded in E^n (E an
elliptic curve over Q). The points of C(Q) lying in the union of proper
algebraic subgroups of E^n form a set of **bounded canonical height**. Two
sharper finiteness statements differ by whether E has CM:

- **CM case**: ⋃ C∩A(Q) over algebraic subgroups **A of codimension ≥ 2** of
  E^n is **finite**.
- **non-CM case**: ⋃ C∩A(Q) over algebraic subgroups of codimension ≥ n/2 + 2
  is finite.

**Subgroup Lemma (structural difference that matters)**:
- E non-CM: an algebraic subgroup of codim r of E^n is characterized by r
  Q-linearly independent equations ∑ n_i π_i = 0, n_i ∈ Z, π_i a Z-basis of
  Hom(E^n,E).
- E CM (O = End(E) ⊗ Q): it is characterized by r **k-linearly independent**
  equations ∑ α_i π_i = 0, α_i ∈ O, π_i a free **O**-module basis of
  Hom(E^n,E). The ambient Hom-module has rank 1 over Z in the non-CM case and
  rank 1 over O (i.e. a larger rank-2-over-Z lattice) in the CM case.

## Bearing on this problem

The run's curve is E: y² = x³ − c²x, j = 1728, **CM by the Gaussian integers**
(well-established: it is the congruent-number curve; its endomorphism ring
contains Z[i]). The explicit-height-constant program for points on transverse
curves in E^n — the lane the open request `dp07-explicit-constant-for-e3-ap`
needs to compute C^(1+r) — is worked out for **non-CM** E (Veneziano–Viada,
Pacific J. Math. 2021; Checcoli–Veneziano–Viada, Forum Math. Sigma 2019; the
MDPI 2017 "Lattices and rational points"). Viada's own comments there describe
the CM-case bounds as much too big to be used, and the CM subgroup/module
structure above explains why: the richer O-module structure makes the explicit
estimates blow up.

**Consequence for the run**: even if the DP07 Théorème 1.13 explicit constant
were obtained, it would be specialised to a **CM** curve (our E), and the entire
documented explicit-constant technology delivers only non-CM bounds. This
corroborates the already-recorded blocking of the uniform-height-AP approach by
constant size: for the CM Robertson/Bremner curve there is no usable explicit
constant, and the external-blockset record (`hms-constant-bound`,
`dp07-explicit-constant-for-e3-ap`) stands. The request stays open for the
*value* of DP07's constant but is now grounded as far as its usefulness: C^(1+r)
< 3 is not in reach through this lane for a CM curve.

```claim
id: viada-2003-cm-subgroup-structure-richer
statement: For E^n (n≥1) with E CM by O, an algebraic subgroup of codim r is
  cut out by r k-linearly independent equations with coefficients in O over a
  free O-basis of Hom(E^n,E), whereas for non-CM E it needs r Z-linearly
  independent equations over a Z-basis. Consequence (Viada 2003 Thm 2): the
  points of a transverse curve lying in codim ≥ 2 algebraic subgroups are
  finite in the CM case, with the explicit estimates being far larger than in
  the non-CM case. Our curve E: y²=x³−c²x (j=1728) is CM by Z[i], so the
  explicit-constant lane (Veneziano-Viada/DP07) yields no usable C for it.
hypotheses: E elliptic over Q; C irreducible transverse in E^n; CM means
  End(E) ⊗ Q = O a rank-2 Z-order (here Z[i]).
holds-here: yes — our curve is CM, so the non-CM explicit constant technology
  does not apply to it.
status: checked (primary on disk, research/sources/viada-...2003.full.md;
  abstract + Subgroup Lemma read directly)
bearing: grounds dp07-explicit-constant-for-e3-ap: even a fetched DP07 constant
  would be non-CM oriented and unusable for the run's CM curve; corroborates
  the constant-size blocking of uniform-height-bound-elliptic-ap.
anchor: research/summaries/viada-intersection-curve-algebraic-subgroups-product-elliptic-2003.md
```

## Notes

- This is a finiteness/bounded-height paper, not an explicit-constant paper; it
  does not itself deliver a numeric C. It is in the library because it is the
  **CM-case primary** the explicit-constant lane implicitly excludes, fixing
  why that lane cannot serve this problem.
- MDPI "Lattices and Rational Points" (2227-7390/5/3/36, 2017) and the
  Veneziano–Viada Pacific J. Math. 2021 paper are **paywalled** (403 on every
  route tried this cycle); their abstracts' explicit-formula summaries are the
  basis for the non-CM-vs-CM contrast above, cross-confirmed by Viada's own
  survey-level comments inside Checcoli–Veneziano–Viada (Forum Math. Sigma 2019,
  available). No download of the paywalled pair was stored.
