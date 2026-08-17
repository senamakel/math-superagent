# srg(33,12,1,6) infeasible by integrality — Lean formalisation

This note carries the claim block for the Lean rendering of the
eigenvalue-multiplicity infeasibility of the subobject srg(33,12,1,6) that
Makhnev 1988 Thm 2 forces at (99,14,1,2) under condition (*) [n3=0].

The arithmetic is fully kernel-checked in
`code/lean/makhnev1988_condstar_theorems.lean`:
- the discriminant δ = (1−6)² + 4(12−6) = 49 = 7² (`condstar_discriminant`),
- the multiplicity numerator 2k + (v−1)(λ−μ) = 2·12 + 32·(−5) = −136
  (`condstar_mult_num`),
- 7 ∤ 136 (`not_seven_dvd_neg_136`, `not_seven_dvd_pos_136`,
  `not_seven_dvd_mult_num`).

These depend only on the kernel's own three axioms (propext / Classical.choice /
Quot.sound) — no Cited axioms.

The theorem `srg33_12_1_6_infeasible_by_integrality` (no srg(33,12,1,6)
exists) additionally rests on the Cited axiom
`Cited.srg_multiplicity_integrality` (the integrality of SRG eigenvalue
multiplicities, Bose–Mesner algebra), so that theorem is **conditional**, not
formalised.

```claim
id: srg33-12-1-6-infeasible-by-integrality-lean
statement: No strongly regular graph with parameters srg(33,12,1,6) exists:
  its multiplicity numerator -136 is not divisible by sqrt(delta) = 7, where
  delta = (1-6)^2 + 4(12-6) = 49 = 7^2.
hypotheses: the eigenvalue-multiplicity integrality of SRGs (Bose-Mesner
  algebra), taken as Cited.srg_multiplicity_integrality; the divisibility
  arithmetic is kernel-checked.
holds-here: yes — the theorem srg33_12_1_6_infeasible_by_integrality compiles
  (lean_check, no sorry); it rests on Cited.srg_multiplicity_integrality plus
  kernel arithmetic. This is a literature result, so the claim is conditional.
status: conditional
formalisation: code/lean/makhnev1988_condstar_theorems.lean
bearing: Makhnev Thm 2's forced subobject cannot exist at all, by multiplicity
  integrality alone (the run's shorter self-contained proof).
anchor: research/notes/makhnev-99-shorter-proof.md
```
