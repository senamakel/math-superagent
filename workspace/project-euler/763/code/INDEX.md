# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | House rules for working inside code/: programs live here, outputs in code/out/, code is a package tree with lib/, and every program's index row must say what established it correct (brute oracle keeps its agreed examples). Read before writing a program. |
| `brute.py` | Naive BFS oracle for D(N): enumerates every distinct set of occupied cubes reachable after exactly N divisions. Returns len of reachable sets. Verified: D(2)=3, D(10)=44499 match the statement. Exponential state space; only for N<=~10. |
| `brute_extended.py` | Level-by-level BFS oracle for D(N): same definition as brute.py but drives one BFS step per level from N=0 up, recording D(N) for every level, and stops when a level exceeds a time budget. Verified reproducing D(2)=3 and D(10)=44499 first. Same exponential state space as brute.py; only used to push the oracle a little beyond what brute.py reaches. |
