# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Working guidance for the code/ tree: package-tree conventions — one job per file, programs live here with their outputs in code/out/, shared imports in code/lib/, the naive program stays as oracle, exact arithmetic, no exponential time/space, never delete a program carrying a result. |
| `brute.py` | Naive brute-force oracle for Project Euler 185. Enumerates all 10^L digit strings and keeps those matching every (guess, c_i) constraint exactly. Verified: on the L=5 example it reports the unique string 39542 (checked against 100000 candidates). Deliberately does not run the 10^16-candidate L=16 instance. |
| `dbg.py` | _(undescribed)_ |
| `dbg2.py` | _(undescribed)_ |
| `dbg3.py` | Debug scratch: checks milp runs with and without time_limit on the L=5 model, printing success/status and reconstructed secret per option. Kept as a record that solver options did not change the L=5 result. |
| `dbg4.py` | _(undescribed)_ |
| `dbg5.py` | _(undescribed)_ |
| `solution.py` | _(undescribed)_ |
| `solution2.py` | _(undescribed)_ |
