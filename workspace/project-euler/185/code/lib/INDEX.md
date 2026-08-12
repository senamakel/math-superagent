# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `pe185.py` | Shared single source of truth for PE185 instance data: L5/CONSTRAINTS5 and L16/CONSTRAINTS16, transcribed exactly from the problem statement, plus N16. Imported by both solution.py and solution2.py so the two solvers cannot drift on inputs. Callable without reading source: `from lib.pe185 import L16, CONSTRAINTS16`. |
| `pe185data.py` | Extracts the sequences derivable from the PE 185 constraint data (c_i counts, per-column digit sequences, row/column digit sums) and prints them for the exact sequence tools. Result: no exploitable integer-sequence structure exists in this constraint data; used by the pattern finder. |
| `pe185secret.py` | Derives integer sequences from the L=16 secret 4640261571849533 (hard-coded here; produced and verified by code/solution2.py): per-position hitcounts, digit distribution, and per-guess match positions, printed for the exact sequence tools. Re-verifies all 22 (guess, c_i) counts as it goes. For the pattern finder — establishes whether the secret digits themselves carry structure. |
