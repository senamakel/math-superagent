# Index — code/lean/Lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `MinimalCounterexample.lean` | Spence 2026 Thm 6.3+6.4 structural statement for a minimum-cardinality union-closed counterexample, rendered as a Lean theorem type ending in := by sorry. Hypotheses: IsUnionClosed/nonempty/nontrivial/normalized (∅∈F)/minimum-cardinality (every smaller UC family has an abundant element). Conclusions: F.card=2k+1 with all frequencies ≤ k, and every admissibly-removable A∈F is omitted by some x with count F x = k. UC.IsUnionClosed/present/count are duplicated inline because sibling imports (import Lib.Statement) do not resolve in this read-only no-lake container. |
| `Statement.lean` | The Lean statement of Frankl's union-closed sets conjecture: defines IsUnionClosed/present/count over Finset families and states union_closed_conjecture (∃ abundant element with 2·count ≥ |
