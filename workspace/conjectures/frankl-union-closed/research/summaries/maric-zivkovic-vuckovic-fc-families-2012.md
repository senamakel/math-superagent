# Marić, Živković, Vučković, "Formalizing Frankl's conjecture: FC-families" (CICM 2012; arXiv:1207.3604)

**Full text:** [[maric-zivkovic-vuckovic-fc-families-2012.full]]

Formalizes the FC-family search in Isabelle/HOL (proof-by-computation), confirms known FC-families, discovers a new one. This is the verification route the later Pulaj–Wood SMT work builds on.

```claim
id: maric-fc-formalization
statement: FC-family membership is formalized and machine-checked in Isabelle/HOL; known FC-families confirmed and one new FC-family found. Also proves FC(3,7)=4 (per Pulaj's reading: all families containing four 3-subsets of a 7-set are FC).
hypotheses: finite union-closed, Poonen's Theorem
holds-here: yes
status: proved (machine-checked in Isabelle/HOL)
bearing: the canonical machine-verification route for FC claims — the "formalize and verify the oracle" precedent this run's phase 3 can follow (this is the `status: formalised` model).
anchor: research/sources/maric-zivkovic-vuckovic-fc-families-2012.full.md
```

**Bearing:** precedent that the Poonen-weight FC decision is verifiable in a theorem prover; a reproduction target for phase 3 and a note against re-deriving what Isabelle already checks.
