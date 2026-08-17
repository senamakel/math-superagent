# Index — code/lean/Lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `Statement.lean` | Statement node for the whole run: Conway's 99-graph conjecture formalised as an existential over Mathlib's SimpleGraph.IsSRGWith 99 14 1 2 (the strong-regular restatement), plus the Conway original wording (ConwayFamily def), the counting identity k(k-2)=2(v-k-1) forcing v=1+k+k(k-2)/2, and v99 forcing k=14. All end in := by sorry — the statements elaborate (lean_check: compiled true, outcome failed only on the three sorries, which is correct for an open statement node). Names: Conway99.conway_99_srg_exists, Conway99.ConwayFamily, Conway99.counting_identity, Conway99.v99_forces_k14. No proof is claimed: the conjecture is open. |
