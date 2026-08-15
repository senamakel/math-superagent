# Cobham's theorem — grounded (named-tool fill for the dyadic thread)

**Fill of a named gap.** The two *adopted* approaches
`christol-cobham-fold-inverse-automaticity` and `dyadic-linear-complexity-supply`
name **Cobham's theorem** as the load-bearing rigidity tool for their
automatic-subclass lemma, but no readable statement of it was on disk or in
memory. This note grounds it. Full text:
`research/sources/cobham-theorem-krebs-proof-statement.full.md`
(summary: `research/summaries/cobham-theorem-krebs-proof-statement.md`).

Source: Krebs, "A more reasonable proof of Cobham's theorem", arXiv:1801.06704
[cs.FL], 2018, 3 pp., a short proof of the classical theorem (original: Cobham
1969, Math. Systems Theory 3:186–192).

```claim
id: cobham-theorem-grounded
statement: If a sequence (f_x) over a finite set is both a-automatic and b-automatic for multiplicatively independent bases a,b >= 2 (a^m != b^n for all m,n > 0, equivalently log a/log b irrational), then it is ultimately periodic. Equivalently, a set X ⊆ ℕ that is both a-recognizable and b-recognizable with a,b multiplicatively independent is ultimately periodic (a finite union of arithmetic progressions). (Cobham 1969; statement + proof verbatim in Krebs arXiv:1801.06704 Theorem 1.)
hypotheses: two bases a,b >= 2, multiplicatively independent; automaticity is the finite-state base-expansion-output notion (DFAO / k-kernel finite by Christol's theorem for the F_q-coefficient case).
holds-here: yes — this is the finite-state rigidity tool the adopted dyadic-periodicity-collapse approaches cite for their automatic-subclass lemma; the approach applies it only to the 2-automatic subclass, and explicitly notes (correctly) that Cobham alone does NOT force rigidity on a single-base 2-automatic string.
status: sourced-statement (verbatim theorem + proof held); the USE of it in the automatic-subclass lemma remains the adopted approach's, not proved here.
bearing: closes the named-tool gap behind the automatic-subclass lemma. Scope discipline the approach itself records: Thue-Morse is 2-automatic and aperiodic (Cobham does not apply — single base), period-3 is 2-automatic yet non-rigid with positive density nu2 ~ 0.647n — so the dyadic dichotomy rests on the σ = I+S spectral structure, NOT on Cobham. This source does not overclaim toward closing G-supply.
anchor: research/sources/cobham-theorem-krebs-proof-statement.full.md
answers: is-cobhams-theorem-grounded
```

## Note for the thread

The automatic-subclass step reads: "a 2-automatic h has a finite 2-kernel, so
its σ-action is finite-state, and Cobham rigidity then yields that an automatic
h is rigid iff its σ-action is nilpotent." Cobham's role there is to turn
*extra* base-independence automaticity into ultimate periodicity (the collapse
direction). It is not, by itself, a rigidity/non-rigidity dichotomy generator on
one base — the two witnesses force the invariant to be the 2-adic σ-spectrum.
This is consistent with what the approach file already records; the source now
makes the citation checkable.
