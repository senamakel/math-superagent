# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `pe185.py` | PE 185 shared instance data (L5, CONSTRAINTS5, L16, CONSTRAINTS16, N16) meant as the single source of truth for the solver and MILP route so they cannot drift. Currently NOT imported anywhere — solution.py and solution2.py hardcode the same constraints inline; pe185data.py overlaps too. Correct data (matches the official statement). Dedup/import wiring left as a code decision. |
| `pe185data.py` | Extracts the sequences derivable from the PE 185 constraint data (c_i counts, per-column digit sequences, row/column digit sums) and prints them for the exact sequence tools. Result: no exploitable integer-sequence structure exists in this constraint data; used by the pattern finder. |
