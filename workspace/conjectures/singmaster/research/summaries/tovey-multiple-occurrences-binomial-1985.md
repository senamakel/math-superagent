# Tovey 1985 — Multiple occurrences of binomial coefficients

Source: C. A. Tovey, "Multiple Occurrences of Binomial Coefficients", The
Fibonacci Quarterly 23(4) (1985) 356–358. Primary; scanned PDF held at
`research/sources/tovey-multiple-occurrences-binomial-1985.full.md`.

## Statement (from the primary text, read this run)

- **Table 1** lists the seven small multiple occurrences:
  120, 210, 1540, 3003, 7140, 11628, 24310, with 3003 the only one expressible
  in **three proper ways** (k ≤ n/2): C(15,5)=C(14,6)=C(78,2). Matches
  `code/out/witnesses.json` and the run's convention minus mirrors.
- **Conjecture (stated, not proved)**: for every t there are infinitely many
  integers expressible in t different proper ways as binomial coefficients.
  The t=2 case is proved.
- **The construction**: Tovey solves a family equation, reducing it via a
  change of variables `x = n−k−1` to the quadratic `n² − xn − (x²+x) = 0`, so a
  perfect-square condition on `5x²+4x` must hold. Lemma 1 gives the Lucas
  identity `5F_j² + 4 = L_j²` (L_j = F_{j-1}+F_{j+1}); Theorem 1 produces a
  solution from x equal to a square of a Fibonacci number (j even); Theorem 2
  (**completeness**) proves all solutions arise this way.
- **Reproducibility caveat**: the family equation itself and the displayed
  formulas are images in the scan; the OCR text is unreliable at those points.
  The paper's published equation is the Lind/Singmaster repeated-coefficient
  family (Kiss 1988, held, independently restates the same family's iff
  classification), but **this run has NOT re-derived the exact variable
  dictionary between Tovey's parametrization and the run's
  n = F_{2i+2}F_{2i+3}−1, k = F_{2i}F_{2i+3}−1 form** — do not cite a
  dictionary from this scan. The run's own family parametrization stands on
  its own verification (claim `fibonacci-n6-family`, exact arithmetic,
  j=1..6) and on the Lind/Singmaster primary (Singmaster 1975 FQ, held).

## Bearing for this run

- **Completeness** (Theorem 2) is the structural claim that the repeated-
  coefficient family equation has no infinite solutions beyond the Fibonacci
  family — anchoring the B≥6 constraint and consistent with Kiss 1988's "iff"
  restatement.
- The six small values 120, 210, 1540, 7140, 11628, 24310 and 3003's three-way
  occurrence are directly corroborated by the run's computed witnesses.json.
- Tovey's general conjecture (every t occurs in t proper ways infinitely
  often) is open and stronger than Singmaster's; do not attach it to any
  bound claim.

```claim
id: tovey-1985-family-completeness
statement: Tovey 1985 (Fibonacci Quart. 23(4) 356-358, primary, full text
  held): independently rediscovers the Lind/Singmaster infinite repeated-
  binomial-coefficient family, proves (Theorems 1 and 2) that a Fibonacci
  parametrization gives solutions and is COMPLETE for the family equation,
  records the seven small multiple occurrences (120, 210, 1540, 3003, 7140,
  11628, 24310) with 3003 the only three-way proper occurrence, and conjectures
  (open, stronger than Singmaster) that every t occurs in t proper ways
  infinitely often. The exact variable dictionary with the run's n,k formulas
  was NOT re-derived from this scan (displayed equations are images; OCR
  unreliable) - the family identity itself is independently verified in this
  run (claim fibonacci-n6-family) and via Lind/Singmaster primaries.
hypotheses: none.
holds-here: yes - same infinite N(a)>=6 family (the reason B>=6) and the same
  witness values as code/out/witnesses.json.
status: sourced (primary, full text read this run); witness arithmetic matches
  computed witnesses; dictionary-level claims marked not-re-derived.
bearing: completeness of the infinite family; corroborates witnesses.json and
  the B>=6 lower bound; Tovey's general conjecture is not load-bearing.
anchor: research/summaries/tovey-multiple-occurrences-binomial-1985.md
```