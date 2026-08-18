# Index — code/lean/Lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `CitedGoldbach.lean` | Lean declarations of source-labelled Chen p+P2 and exceptional-set facts; these are cited axioms, not theorems formalised by this run. |
| `GoldbachOracle.lean` | Kernel-checked witness certificate for every even `n` in [4, 50]: `witness n` is a prime-sum pair for `n`, and `all_even_4_to_50_goldbach` bundles it. Mirrors `HAND_COUNTS_4_50` in `code/lib/goldbach.py` |
| `Statement.lean` | Formal Lean statement of the binary Goldbach conjecture; intentionally ends with sorry because the conjecture is open. |
