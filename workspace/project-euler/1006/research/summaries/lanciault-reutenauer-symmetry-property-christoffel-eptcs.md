# Lanciault & Reutenauer, "A Symmetry Property of Christoffel Words"

**Primary (recent, short).** Yan Lanciault, Christophe Reutenauer, *A Symmetry
Property of Christoffel Words*, EPTCS 403 (2024) 123–127, in Proceedings
GASCom 2024, doi:10.4204/eptcs.403.26. Full text via arXiv:2406.16408:
`research/sources/lanciault-reutenauer-symmetry-property-christoffel-eptcs.full.md`
(URL recorded in-file). CC BY 4.0.

## What it establishes

**Strong factor-symmetry.** For a word w over {a,b} with Parikh image (p,q),
δ_w(i,j) = the number of distinct factors of w with Parikh image (i,j). w is
*strongly factor-symmetric* if δ_w(i,j) = δ_w(p−i, q−j) for all i,j.

- **Thm 3.1**: every Christoffel word is strongly factor-symmetric.
- **Thm 3.2**: a primitive Sturmian word whose support of δ_w is symmetric (in
  particular, strongly factor-symmetric) is a Christoffel word. (aabb is
  strongly factor-symmetric but not Sturmian, so "Sturmian" is essential.)
- **Thm 3.3**: for w = u^k, u primitive, k ≥ 2, w is strongly factor-symmetric
  iff u is a Christoffel word.
- **Thm 4.1**: explicit bijection between length-k factors of a Christoffel
  word intersecting the palindromic-factorization cut and length-(n−k) factors
  of the same cut, complementing Parikh images: γ(f_i) + γ(g_i) = γ(w).
- **Thm 4.2**: the support of δ_w for a lower Christoffel word w is exactly the
  set of integer points on the paths of w and its upper Christoffel reversal w̃.
- **Thm 4.3**: w = u^k, u primitive, k ≥ 2 is factor-symmetric iff u is the
  conjugate of a Christoffel word.
- Recalls the classical characterisation: a Sturmian word is a Christoffel word
  iff it is Lyndon iff it is unbordered (after Berstel–de Luca 1997, ref [3]/[6]).

## Bearing on PE1006

- This is the *conjugacy/Christoffel-class axis*, the same axis as the held
  Borel–Reutenauer 2006 "On Christoffel classes" and the run's refuted
  approach `pe1006-christoffel-conjugacy-rotation-sum` (the k+1 factors of the
  Fibonacci word are k rotations of one Christoffel word plus one singular
  factor). It adds a new, bivariate characterisation of Christoffel words by
  factor-array symmetry.
- **It does NOT bear on Ψ(k)**: δ_w counts distinct factors by Parikh image
  (number of 0s and 1s), not by decimal value; Ψ sums squares of decimal values
  over the length-k factor set. The Parikh-image symmetry is a different
  observable (it is the balance/structure axis, already anchored by the
  Sturmian balance claims). No decimal-weight statement appears.
- Modern companion confirming the Christoffel-Lyndon-unbordered
  characterisation the run already holds via Borel–Reutenauer.

## Relationship to the held library

- Complements `borel-reutenauer-christoffel-classes-2006.full.md` (the
  Christoffel-class reference) and the BWT/Christoffel material in the held
  Fici–Mantaci–Restivo–Romana–Rosone–Sciortino survey.
- Its 18-23 citations added to the frontier are the standard Christoffel/
  trapezoidal-word literature (Bucci–de Luca–Fici trapezoidal, de Luca's
  trapezoidal words, Levé–Séébold, d'Alessandro) — new leads for the
  trapezoidal/factor-symmetric axis, none of which is a PE1006 moment source.

## Bibliographic note (mis-fetch trail)

The arXiv id 2406.16408 was reached only via the verified DOI
doi:10.4204/eptcs.403.26 (which redirected to the arXiv abstract page); the
earlier guessed id 2406.10263 fetched a machine-learning paper and was
overwritten with a MIS-FETCH note (see
`research/notes/library-cycle-2026-08-20-palindromic-richness.md`).
