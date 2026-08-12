# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Working instructions for the code/ package tree: imports via PYTHONPATH, one subject per lib module, exact arithmetic, brute-force policy, evidence standards. |
| `brute.py` | Naive exact-integer oracle for Project Euler 185 (Number Mind). Parses (guess_string, count) pairs, enumerates all 10^L candidate secrets, returns every string matching every constraint position-wise. Establishes correctness: reproduces the statement's inline 1234/2036->1 example and the N=5 example uniquely as 39542. Intentionally O(10^L) — must NOT be run on the 16-digit case. Also embeds the 22-guess 16-digit instance as data (parse-only confirms 22 guesses of length 16). |
| `diag.py` | Diagnostic for the pruning solver: counts backtracking nodes on the 16-digit/22-guess instance under a node budget (so it measures growth without hanging), and tests whether an alternative column order (by per-column digit diversity) visits fewer nodes than the natural order. A measurement/tuning script, not a solver — it does not produce the answer. Imports nothing; embeds its own copy of the 22-guess 16-digit data and its own parse, duplicating what brute.py and solution.py embed. |
| `solution.py` | Efficient Project Euler 185 solver: backtracking over positions with two-sided arc-consistent pruning (matches_so_far[i] <= count[i] and matches_so_far[i]+remaining >= count[i] for every guess). Not enumeration — pruning makes most of 10^N unreachable. Prints the N=5 example solutions as a self-check and the full 16-digit/22-guess solutions. Exact integer arithmetic; intended to be checked against code/brute.py on N=5. (Execution status unconfirmed from the run log.) |
