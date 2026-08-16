# Summary — Allouche & Shallit, "The ring of k-regular sequences II" (TCS 307 (2003) 3–29)

Companion / continuation of the foundational k-regular paper I. Defines the
k-kernel generalization cleanly and collects closure properties and new
examples.

<!-- source: http://plouffe.fr/simon/articles/kreg2.pdf (preprint submitted to Elsevier Science) -->

## What the paper establishes

Recalls the Eilenberg theorem: a sequence `(a_n)` over a finite alphabet is
**k-automatic** iff its k-kernel (subsequences `(a_{k^i n + r})`, `i ≥ 0`,
`0 ≤ r < k^i`) is finite — Thue–Morse being the canonical example. It then
generalises: rather than the k-kernel being finite, one asks that the
`R`-module it generates be **finitely generated**; such sequences are
**R-k-regular** (usually `R = Z`, then "k-regular"). Key example: the sum-of-
digits function `s₂(n)` is 2-regular (its 2-kernel lies in the Z-span of
`s₂(n)` and the constant sequence). The paper proves new closure/structure
results, gives ~20 new examples, and states open problems.

## Why it matters for SUPPLY

This is the cleanest statement of the definition the diagonal-automaton approach
uses: `T(n,d) = ⊕_{o⊆d} h[·]` is a submask-XOR whose 2-regularity as a function
of `(n,d)` (via Lucas) would make `ν₂(n)` an automaton-counting function. The
`Σ_d` over the diagonal is exactly the kind of finite sum that the ring *closure
under addition* keeps inside the 2-regular family, so the algebraic route's
well-formedness is grounded here. Thue–Morse being 2-regular is also the precise
reason closed door 3 (aperiodicity is insufficient) holds — the pathological
input is 2-regular, so the fold's submask-XOR reading cannot grow linearly on it.

## Caveat

Full text is stored but the PDF→Markdown conversion is garbled (ligatures, no
word spaces). The definition and examples above are confirmed from the readable
portion; exact theorem numbers are not transcribed.

## Wikilinks / claims

```claim
id: as-kregular-II-definition
statement: A sequence over a Noetherian ring R is R-k-regular iff the R-module generated
  by its k-kernel is finitely generated; k-automatic (finite alphabet) is the special
  case where the k-kernel is finite. The 2-kernel of the sum-of-digits function is
  finitely generated, so s₂ is 2-regular; Thue–Morse is 2-automatic (finite 2-kernel).
hypotheses: R Noetherian (R=Z usual).
holds-here: yes — over F₂ the fold's submask-XOR diagonal is a binomial-sum mod 2 object
  in the 2-regular family, and Thue–Morse's 2-regularity explains door 3.
status: proved (Allouche–Shallit, 2003 continuation).
bearing: fixes the definition and examples grounding approach
  diagonal-2regular-automaton; confirms the pathological inputs (Thue–Morse) lie in the
  2-regular family the automaton route would have to exclude.
anchor: allouche_shallit_kregular_II.full
```
