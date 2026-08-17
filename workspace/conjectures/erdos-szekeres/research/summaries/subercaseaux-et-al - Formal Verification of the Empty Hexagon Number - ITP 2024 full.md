> **Note — this source is digested in the consolidated SAT note.**

This file is the arXiv landing digest of **Subercaseaux, Nawrocki, Gallicchio,
Codel, Carneiro, Heule, "Formal Verification of the Empty Hexagon Number"**
(ITP 2024, arXiv:2403.17370). Its role in the library is discussed in:

→ [[sat-machinery-es-type-problems]] (the §Subercaseaux et al. section) and
[[LIBRARIAN-REPORT]].

**Bottom line.** A Lean 4 formalization (with `#print axioms` / DRAT proofs) of
the empty-hexagon-30 SAT result, plus tools connecting planar geometry to
propositional assignments and covering the ES encoding. This is the model for
GOAL criterion 5 (the run's Lean file stating ES(n) and the conjecture) and
evidence that the orientation-variable formalism is Lean-friendly. The
empty-hexagon number itself is **adjacent** (see the Horton/empty-hexagon
boundary); the *formalization infrastructure* is the reusable part.
