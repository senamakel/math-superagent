# Index — code/fmax_verify

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `S.md` | = 2^{n-1}+1 for n = 8..11 (re-confirming n = 1..7), with the n=10,11 d=4 |
| `solve_both.py` | Two independent exact solvers (HiGHS ILP + CP-SAT) for the decision "is there S of size 2^{n-1}+1 with D(S)<=d?", each (n,d) run by both; the n=10,11 d=4 infeasibility claim is the thing under test. Threads pinned to 1 first. |
