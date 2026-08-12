# Index — code/pushverify

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `solve_n.py` | CDCL-style driver: solve C4+degree base, extract model, run cycle oracle independently, block found C8/C16, iterate to UNSAT. Reports UNSAT (theorem) or SAT counterexample with graph6. Usage: python solve_n.py N. |
