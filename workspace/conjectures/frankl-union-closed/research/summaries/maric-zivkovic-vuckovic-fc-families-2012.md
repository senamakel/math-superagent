# Marić, Živković, Vučković, "Formalizing Frankl's conjecture: Fc-families" — DEFECTIVE BODY

**Intended citation:** F. Marić, M. Živković, B. Vučković, *Formalizing Frankl's
conjecture: Fc-families*, Lecture Notes in Computer Science 7362 (2012), 248–263
(CICM / Intelligent Computer Mathematics). Survey statement:
`research/sources/bruhn-schaudt-journey-survey-2013-body.full.md` §5.1:

> "Marić, Živković and Vučković [44] verified some known FC-families and found a
> new one using the automatic proof assistant Isabelle/HOL. For this, they
> formalised the condition of FC-families to enable a computer search. As a
> result, we know now that **all families containing four 3-subsets of a 7-set
> are FC-families.**"

## DEFECT (scholar, this run)

The local file `research/sources/maric-zivkovic-vuckovic-fc-families-2012.full.md`
(downloaded as arXiv:1209.5628) **does NOT contain this paper**. It contains
Georg Oberdieck's *"A Serre derivative for even weight Jacobi forms"* — a
modular-forms/number-theory paper (arXiv:1209.5628v3, 2014). The FC-families
paper is a LNCS book chapter; it is **not on arXiv** under this or a nearby ID,
and its body is paywalled (Springer LNCS 7362).

**Impact assessment:** This file and its auto-generated digest carry the *wrong
content*, but **no load-bearing claim in CLAIMS.md anchors to this file or to
arXiv:1209.5628.** The run's FC-machinery claims (`vuckovic-zivkovic-fc-lemma`,
`pulaj-algorithm`, `verified-n12-comp-primary`) anchor to the genuine Vučković–
Živković 2017 paper and to Pulaj 2017, both of which are real full bodies. So the
defect is a *mislabeled paper on disk*, not a corrupted established claim.

**What the FC family content actually rests on (all genuine, on disk):**
- Morris (math/0702348), FC-families characterisation on ≤ 5 elements;
- Vučković–Živković 2017 (`vuckovic-zivkovic-12-element-2017.full.md`),
  Poonen-weight characterisation and the 33 FC families for n=12;
- Pulaj 2017 (`pulaj-cutting-planes-2017.full.md`), exact algorithm via
  Poonen's weight polyhedron.
The "four 3-subsets of a 7-set are FC" fact is best sourced from the survey and
from Vučković–Živković's list, not from this mislabeled file.

```claim
id: maric-4-3subsets-7set-fc
statement: All families containing four 3-subsets of a 7-set are FC-families
  (force Frankl's conjecture in every union-closed superfamily), verified by the
  automatic proof assistant Isabelle/HOL (Marić–Živković–Vučković).
hypotheses: A is a family of four 3-subsets of [7]; F ⊇ A union-closed.
holds-here: yes (FC-machinery fact, survey-sourced; local full body of the
  original paper is NOT available — mislabeled on disk).
status: asserted-by-source (standard Isabelle proof, per survey).
bearing: an FC-families data point for the LP/weight computational route
  (GOAL item 3-set question); confirms the FC machinery's reach, not an
  established class beyond the survey's word.
anchor: research/sources/bruhn-schaudt-journey-survey-2013-body.full.md §5.1
  (original paper paywalled; do NOT cite arXiv:1209.5628 — wrong body).
```
