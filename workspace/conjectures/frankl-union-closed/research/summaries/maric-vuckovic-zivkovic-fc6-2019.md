# Fully Automatic, Verified Classification of all Frankl-Complete (FC(6)) Set Families

Filip Marić, Bojan Vučković, Miodrag Živković. arXiv:1902.08765 (cs.LO), v1 23 Feb 2019.

**Full text:** `research/sources/maric-vuckovic-zivkovic-fc6-2019.full.md`
<!-- source: https://arxiv.org/pdf/1902.08765 -->

## What it establishes (primary source)

A **total characterization of all Frankl-complete (FC) families over a 6-element
universe**, obtained by fully automated, computer-assisted enumeration that is
**formally verified inside the Isabelle/HOL proof assistant** — both that the
enumerated families are FC and that the enumeration is complete (thenon-FC side
is also proved, via Poonen's theorem, formalized for the first time).

The paper defines and enumerates all **minimal FC-families** and all **maximal
non-FC (NFC) families** on six elements. Its role in the attack on Frankl's
conjecture is search-space pruning: an FC-family forces the conjecture in any
union-closed family containing it; knowing all (minimal) FC(6) families tells
which 6-element local structures cannot appear inside a counterexample.

This complements (does not extend) the ground-set verification bound in the
library: the n≤12/n=13 line of Bošnjak–Marković and Vučković–Živković verifies
UC for ground sets up to size 12; a classification of FC(6) families is a
mechanized, formally-checked statement about the local-configuration/weight
machinery (Poonen) that underpins that line, at universe size 6.

```claim
id: maric-zivkovic-fc6-classification
statement: All Frankl-complete (FC) families on a 6-element universe are characterized: the minimal FC-families and maximal non-FC families are enumerated, and both the FC-status and the completeness of the enumeration are formally verified in Isabelle/HOL (non-FC via Poonen's theorem, first formalized there).
hypotheses: universe [6]; FC = every union-closed F ⊇ Fc has a Frankl-abundant element in ∪Fc.
holds-here: true
status: sourced (formally-verified computational classification; abstract + bibliographic record downloaded)
bearing: a mechanized, proof-assistant-checked piece of the Poonen local-configuration/weight machinery that underlies the small-universe verification line; complements the n≤12 ground-set bound without extending it; useful as a trusted-software cross-check for the library's own oracle work on small universes.
anchor: arXiv:1902.08765, abstract.
```

## Notes
- The abstract-page/body coverage is bibliographic + abstract (the formalization
  details and the full FC/NFC lists live in the paper's appendix). It is held
  because the Pulaj–Wood paper (on disk) cites it and it is the state of the art
  in *verified* FC-classification, distinct from the algorithmic FC-solvers
  (Pulaj) also on disk.
- Does NOT change the verified ground-set range (still n ≤ 12, so any
  counterexample has ≥ 13 elements) nor the |F| ≥ 4m−1 ≥ 51 bound.
