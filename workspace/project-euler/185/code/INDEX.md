# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Working instructions for the code/ package tree: imports via PYTHONPATH, one subject per lib module, exact arithmetic, brute-force policy, evidence standards. |
| `brute.py` | Naive exact-integer oracle for Project Euler 185 (Number Mind). Parses (guess_string, count) pairs, enumerates all 10^L candidate secrets, returns every string matching every constraint position-wise. Establishes correctness: reproduces the statement's inline 1234/2036->1 example and the N=5 example uniquely as 39542. Intentionally O(10^L) — must NOT be run on the 16-digit case. Also embeds the 22-guess 16-digit instance as data (parse-only confirms 22 guesses of length 16). |
