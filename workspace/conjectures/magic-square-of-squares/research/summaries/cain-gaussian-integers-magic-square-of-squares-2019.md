# Cain, "Gaussian Integers, Rings, Finite Fields, and the Magic Square of Squares", arXiv:1908.03236 (2019)

[[cain-gaussian-integers-magic-square-of-squares-2019]]

A 15-page arXiv paper (math.RA / math.NT) whose abstract-less full text (only the HTML
abstract page was downloaded, no body was converted) gives its claims at abstract level.

## What it claims (abstract-level)
- The 3×3 MSS problem is equivalent to solving quartic polynomials with certain factorization
  constraints over an abelian extension of Q.
- Analyzing a particular case where that extension is assumed to be the Gaussian integers
  yields a **new search method**.
- MSS over finite fields and rings Z/nZ is analyzed, producing **conjectures** enumerating the
  rings and finite fields in which a MSS can be constructed. Code is made available.

## Implications for this run
- The "quartic over an abelian extension" and the Gaussian-integer search method are an
  alternative reformulation to Bremner's elliptic/K3 one. It is a **new search method**, not a
  proof — and the over-finite-fields part is explicitly stated as **conjectures**, so no
  theorem is available here.
- The finite-field/ring enumeration could corroborate the run's "locally solvable mod every
  prime power" belief, but the paper treats conjecural enumerations, so it cannot confirm it.

## Assessment
- The full text (body) was not downloaded, only the abstract page. The digest/note can carry
  only the abstract-level claims: equivalence-to-quartic-over-abelian-extension, a Gaussian
  integer search method, and *conjectured* finite-field/ring enumerations. None is a proved
  result usable as a load-bearing claim. If the run wants to use the quartic reformulation it
  must fetch the body, which is not on disk.

## Contradictions / cautions
- Does not contradict recalled memory, but the "equivalent to quartic over abelian extension"
  is a different framing from Bremner's elliptic 2E(Q)-in-AP; the two should be reconciled if
  this line is pursued, and neither is established as *the* canonical reduction.

```claim
id: cain-quartic-gaussian-reformulation
statement: The 3x3 MSS problem is equivalent (per the authors) to solving quartic polynomials
  with factorization constraints over an abelian extension of Q; a Gaussian-integer case gives a
  new search method.
hypotheses: as stated at abstract level only; body not on disk
holds-here: unchecked
status: asserted
bearing: alternative reformulation to Bremner's elliptic one; not yet usable without the full text
anchor: research/sources/cain-gaussian-integers-magic-square-of-squares-2019.full.md
```
