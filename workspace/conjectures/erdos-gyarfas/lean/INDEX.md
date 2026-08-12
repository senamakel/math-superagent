# Index — lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `STATUS.md` | Inspection report for lean/erdos_gyarfas.lean: the formal statement as written, the fact that the single theorem erdos_gyarfas is an intentional sorry with no lemmas, the #print axioms output [propext, sorryAx, Classical.choice, Quot.sound], that the k>=2 convention is stated both in the statement and in prose, and that the file elaborates cleanly under lean (exit 0, only the expected sorry warning). Includes a suggestion to add #print axioms erdos_gyarfas to the file. |
| `erdos_gyarfas.lean` | Formal statement of the Erdős–Gyárfás conjecture against Mathlib's SimpleGraph API: every finite simple graph with minDegree >= 3 contains a cycle of length 2^k with k>=2. The statement elaborates; the body is an intentional `sorry` since the conjecture is open. |
