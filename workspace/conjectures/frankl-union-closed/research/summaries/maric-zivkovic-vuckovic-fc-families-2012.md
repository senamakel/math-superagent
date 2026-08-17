# Marić, Živković, Vučković — "Formalizing Frankl's Conjecture: FC-families"

**Source**: https://arxiv.org/abs/1207.3604 (arXiv:1207.3604v2, 2012); journal
version: F. Marić, M. Živković, B. Vučković, *Formalizing Frankl's conjecture:
FC-families*, Intelligent Computer Mathematics (CICM), LNCS 7362 (2012),
248–263, Springer.
**Full body on disk**: `research/sources/maric-zivkovic-vuckovic-fc-families-2012.full.md`
(retrieved from the ar5iv rendering of arXiv:1207.3604; URL embedded in line 1).

> **Repair record (librarian, this cycle).** The previous body under this name
> was the wrong paper — arXiv:1209.5628 (Oberdieck, "A Serre derivative for
> even weight Jacobi forms", number theory) — downloaded under a mistyped ID
> and flagged DEFECTIVE. The genuine body is now on disk; **never cite
> arXiv:1209.5628 for FC-families.**

## What this paper is

The first proof-assistant formalisation of the FC-family machinery used to
attack Frankl's conjecture. FC-families (`Fc`): families for which it is proved
that **every** union-closed superfamily satisfies Frankl's condition (has an
element in ≥ half the sets). If FC status were known for every small family,
search-space pruning would settle small universes; conversely, if the
conjecture were true, every family would be FC. The paper formalises, in
Isabelle/HOL, the weight-function/share characterisation (Poonen's theorem,
restated as their Theorem 2.1): `Fc` is FC iff there is a weight function `w`
on `∪ Fc` such that every union-closed extension has non-negative `w`-share
for every element. It implements and *verifies* (proof-by-computation) a
combinatorial search procedure `ssn` that decides the FC property.

## What it establishes

**Theorem 5.1** — the following are FC-families (all confirmed as previously
known in the literature, except item 5):

1. all families containing one 1-element set `{{a}}`;
2. all families containing one 2-element set `{{a,b}}`;
3. all families containing three 3-element sets whose union is contained in a
   5-element set (uniform `53_3`-families);
4. all families containing four 3-element sets whose union is contained in a
   6-element set (uniform `63_4`-families);
5. **all families containing four 3-element sets whose union is contained in a
   7-element set (uniform `73_4`-families) — the new FC-family discovered
   here.**

Proof method: for each isomorphism class (Lemma 8 reduces to the rows of
Table 1), a weight function `w` is exhibited and Lemma 9 (`ssn Fc w = ⊥`,
meaning no union-closed extension has a negative share) is discharged **by
computation inside Isabelle/HOL**. The formalisation is ~6500 lines of
Isabelle/Isar; the proof check takes ~28 min on a 2.1 GHz notebook, of which
22.8 min is the final uniform-`73_4` case. This is a mechanised, independently
checkable certificate — stronger than the original Java search by
Živković–Vučković, which it re-implements and verifies.

## Why it matters for this run

- The **three-set question** of `problem.md` (which 3-set families force UC) is
  answered in part here: any 3-element-set-containing family that contains
  three 3-sets in a 5-universe, or four 3-sets in a 6- or 7-universe, is FC —
  so every union-closed family containing such a configuration satisfies the
  conjecture. This is the FC/data point behind the n ≤ 12 verification and
  behind the Pulaj/Morris algorithmic line already on disk.
- It is the primary citation for the claim previously sourced only via the
  Bruhn–Schaudt survey: **all families containing four 3-subsets of a 7-set
  are FC-families** (survey §5.1 restates this exactly; the primary proof is
  this paper's Theorem 5.1(5)).

```claim
id: maric-4-3subsets-7set-fc
statement: All families containing four 3-element sets whose union is contained
  in a 7-element set are FC-families (every union-closed superfamily satisfies
  Frankl's condition), proved in Isabelle/HOL by the verified ssn computation
  (Theorem 5.1(5) and Lemma 9, Marić–Živković–Vučković). The paper further
  confirms as FC: any family containing a 1-set, a 2-set, three 3-sets in a
  5-universe, or four 3-sets in a 6-universe (Thm 5.1(1)–(4)).
hypotheses: Fc is a family of four 3-subsets of [7] (uniform 73_4); F ⊇ Fc
  union-closed and finite.
holds-here: yes (FC-machinery fact, primary source, machine-verified in
  Isabelle/HOL — not merely asserted by the survey).
status: proved (by computation, formally verified in the proof assistant, per
  the paper's own statement — an Isabelle-checked certificate).
bearing: answers part of the 3-set question (GOAL.md result class 6 territory:
  which small configurations force UC); underlies the FC-based n≤12
  verification; the local library now holds the primary body, not just the
  survey's restatement.
anchor: research/sources/maric-zivkovic-vuckovic-fc-families-2012.full.md,
  Theorem 5.1, Lemma 9, Table 1 (arXiv:1207.3604).
ceiling: the FC-family classification for larger configurations (e.g. five
  3-sets in [7]) is NOT settled by this paper; extend only via the
  Marić–Vučković–Živković FC(6) classification (arXiv:1902.08765, on disk) or
  the Pulaj–Wood local-configurations work.
answers: (none — this closes no standing request; the FC-families request was
  never posted because the fact was already survey-sourced, which is why the
  mislabeled body went unnoticed until this repair).
```

## Cross-references on disk

- Survey restatement: `research/sources/bruhn-schaudt-journey-survey-2013-body.full.md` §5.1.
- Sequence of the FC line: Morris (math/0702348) → Marić–Živković–Vučković
  (this paper) → Marić–Vučković–Živković FC(6) classification (arXiv:1902.08765)
  → Pulaj cutting planes (arXiv:1702.01426) → Vučković–Živković n=12
  (2017). All on disk except the paywalled Springer LNCS original, now
  superseded by the arXiv body.