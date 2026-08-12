# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Working rules for the code/ tree: how programs are laid out (one job per file, lib/ for shared helpers, out/ for produced output), the PYTHONPATH import convention, the oracle rule, and the exact-arithmetic and no-exponential requirements. Guidance, not mathematics. |
| `brute.py` | Naive oracle for PE345: computes Matrix Sum (max-weight perfect matching) by enumerating all n! column permutations. Verified: reproduces the statement's 5x5 example, returning 3315 = 863+383+343+959+767 with column permutation (4,1,2,3,0). Factorial method, oracle only (n=5). |
| `seq_extract.py` | Pattern-extraction aid: computes the Matrix Sum (Hungarian) of each leading principal kxk submatrix of PE345's 15x15 matrix, k=1..15, yielding the sequence [7,680,...,13938] that analyze_sequence/find_linear_recurrence were run on. Confirmed dead thread (no recurrence, no polynomial, uncatalogued); reproduced full 15x15 = 13938. |
| `solution.py` | Solves PE345 15x15 Matrix Sum via Hungarian (scipy linear_sum_assignment on negated costs); answers 13938; verifies 5x5 oracle and random agreement vs brute. |
