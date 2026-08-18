# Index — code/lean/Lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AcceleratedCycleIdentity.lean` | Blueprint Lean statement for the accelerated-map finite parity-word affine reduction; currently has an explicit sorry and is not a proved identity. |
| `CitedCycleBounds.lean` | Conditional Lean placeholder carrying Hercher's cited no-m-cycle theorem; intentionally abstract until the accelerated cycle structure is formalised. |
| `CitedRestrictedClasses.lean` | Lean placeholders for cited restricted-class results from Monks, Hercher, and Knight; axioms are explicitly source-backed and not formalised proofs. |
| `Statement.lean` | Formal Lean statement of the accelerated Collatz map and conjecture; theorem intentionally remains sorry as the open target. |
| `accelerated_collatz_conjecture.lean` | Cited formal statement of the accelerated (Syracuse) Collatz conjecture, with the required trailing #print axioms. lean_check: compiled true, outcome conditional, verified false; depends on Cited.accelerated_collatz_conjecture and no sorry. |
| `collatz_conjecture.lean` | Cited formal statement of the ordinary Collatz conjecture, with the required trailing #print axioms. lean_check: compiled true, outcome conditional, verified false; depends on Cited.collatz_conjecture and no sorry. |
| `cycle_collision.lean` | Pinned-down statement of the collision lemma behind gap G-min-element-lower: Cited axioms for the Hercher bridge upper bound, the Zudilin Diophantine lower bound (mu = 8.616), and the reciprocal-sum bound S <= m/x_min, plus the theorem that a non-trivial m-cycle forces x_min > (3 log 2 / c_0) * m^mu with body := by sorry. Status: compiles, theorem open (sorry), three cited axioms. |
| `cycle_sum_identity.lean` | Defines the accelerated map T and IsCycle, and states the cycle-sum identity as a cited axiom, with the required trailing #print axioms. lean_check: compiled true, outcome conditional, verified false; depends on Cited.cycle_sum_identity (plus the three standard axioms) and no sorry. |
| `finitely_many_cycles_fixed_period.lean` | Crandall 1978 Corollary 7.2 as a cited axiom: for each period k, the set of k-element T-cycles is finite. With the required trailing #print axioms. lean_check: compiled true, outcome verified, verified true — the binder k is data (period), the finiteness content is in the Set.Finite statement; the cited axiom itself is trivially closed by the kernel, so the verdict is formalised, with the caveat that the mathematical content is the axiom (see prose in the report). |
