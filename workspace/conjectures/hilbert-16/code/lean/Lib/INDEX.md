# Index — code/lean/Lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `Bautin.lean` | _(undescribed)_ |
| `BautinRecurrence.lean` | Hand-written Lean checker for the H14^3 finite core: reconstructs P30 from untrusted Generated/P30Data data, closes checkP30 (P30 + 12*weighted_g6 = 0) by decide; restates Darboux/bridge identities (part B) with named sorries pending the in-Lean recurrence. |
| `Statement.lean` | H16.2 stated in Lean: PlanarPolyField n carries P Q : MvPolynomial (Fin 2) ℝ with totalDegree ≤ n; IsLimitCycle = non-constant periodic integral curve isolated in the set of periodic orbits; h16_2 states ∀ n, ∃ N, ∀ f, (LimitCycleSet f.toMap).Finite ∧ ncard ≤ N, ending in by sorry. Compiles via lean_check (only axiom beyond the kernel's own three is sorryAx from the intentional sorry). |
