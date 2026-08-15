# Index — code/lean_reduction

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `CatalanReduction.lean` | Lean 4 formalisation of the Catalan prime-exponent reduction identity ((x^a)^P - (y^b)^Q = 1 iff x^(a*P) - y^(b*Q) = 1, over ℕ and ℤ), the known solution 3^2 - 2^3 = 1, and that 2,3 are not nontrivial perfect powers. Kernel-checked with Lean 4.34 + Mathlib; #print axioms shows only propext/choice/Quot.sound, no sorry. |
| `REPORT.md` | Prose report of the formalisation: axioms printed, no-sorry confirmation, scope (does NOT do exponent-2 cases or odd-prime reduction in the strong sense), and position of each lemma relative to the known solution. |
