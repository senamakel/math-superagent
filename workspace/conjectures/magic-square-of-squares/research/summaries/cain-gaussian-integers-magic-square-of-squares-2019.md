# Cain, "Gaussian Integers, Rings, Finite Fields, and the Magic Square of Squares", arXiv:1908.03236 (2019) — [[cain-gaussian-integers-magic-square-of-squares-2019.full]]

Modern reformulation (19pp, math.RA). Abstract statement:
- The 3×3 magic square of squares problem is shown **equivalent to solving quartic polynomials with certain factorisation constraints over an abelian extension of Q**.
- A special case (extension = Gaussian integers) yields a **new search method**.
- The problem is also analysed over finite fields and Z/nZ, producing **conjectures** enumerating the rings and finite fields in which a magic square of squares can be constructed. Code released.

**Status/provenance caveat:** only the abstract is in this local copy; the full content (the exact quartic reduction, the Gaussian search algorithm, the conjectures) is not present in `research/sources/`. What is asserted here is the *claim of equivalence* and the existence of a new search method, not the derivation.

## Bearing on this run
Confirms the direction that the obstruction is number-theoretic/integral (message consistent with Bremner's extension-field result: solving requires picking the right ring). The finite-field enumeration conjecture could serve as a check: whatever it claims about which Z/nZ and F_q admit a square, a sieve-based impossibility proof must not contradict it. But because the derivation is absent locally, treat the specific content as `asserted-by-source`, not verified.

```claim
id: cain-quartic-abelian
statement: The 3×3 magic square of squares problem is equivalent to solving quartic
  polynomials with certain factorisation constraints over an abelian extension of Q; the
  Gaussian-integer case gives a new search method and the finite-field/ring cases yield
  conjectures.
hypotheses: —
holds-here: unchecked (full derivation not in local copy)
status: asserted (per the paper's abstract only)
bearing: supports the integral/number-theoretic character of the obstruction; a candidate
  new search family (Gaussian integers)
anchor: research/sources/cain-gaussian-integers-magic-square-of-squares-2019.full.md
```
