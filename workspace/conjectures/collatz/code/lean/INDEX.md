# Index — code/lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `crandall_finite_cycles-47c20f34.lean` | Cited Lean formalisation of Crandall 1978 Corollary 7.2: a finite-set encoding of finitely many cyclic trajectories for each fixed period. |
| `hercher_K_1p375e11-553d60ec.lean` | Conditional Lean rendering of Hercher Corollary 29, with explicit cycle and odd-count definitions, cited source axiom, theorem proof, and axioms printout. |
| `hercher_m92-97b13fb9.lean` | Node hercher-m92: Hercher's Main Theorem 23 stated in Lean. Defines the accelerated map T, IsCycle, IsNontrivialCycle, local minima as odd elements not reached from odd elements, localMinimaCount; carries Cited.no_m_cycle_le_91 (the paper's Main Theorem 23, source arXiv:2201.00406v3) as a cited axiom; proves hercher_m92 — every non-trivial cycle has ≥ 92 local minima — by the contrapositive with omega. lean_check: compiled true, outcome conditional (only non-standard axiom: Cited.no_m_cycle_le_91), no sorrys. |
| `lagarias_W2-eb4a08bf.lean` | Conditional Lean formalisation of Lagarias W2: under the cited Eliahou 1993 numerical cycle-exclusion theorem, a cycle with period or odd-count below the stated bounds is the trivial (period 2, one odd entry) cycle. |
| `no_nontrivial_cycle_G_cycle_diophantine_bridge-33fd98af.lean` | Kernel-checked abstract two-sided numerical bridge for the cycle Diophantine statement; cycle combinatorics are parameterised rather than defined. |
| `no_nontrivial_cycle_G_irrationality_measure-81d9ad7b.lean` | Formalizes the requested conditional application of an effective irrationality-measure hypothesis for log 3/log 2 to p=K+L and q=K. |
| `no_nontrivial_cycle_G_min_element_lower-e06ff9dc.lean` | Formalizes the requested abstract power-law lower-bound shape; documents that cycle, Hercher sum, and explicit constants were not defined in the supplied node. |
| `zudilin_mu_8616-b4bd408b.lean` | Formal definition of irrationality exponent and conditional Lean rendering of Zudilin Theorem 3 instantiated at log 3/log 2; currently exposes the span-membership proof gap. |
