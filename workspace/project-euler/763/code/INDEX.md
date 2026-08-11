# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `amoeba_2d.py` | BFS for 2D amoeba process, D_2D(N) N=0..15, to test the A007902 identity suggested by the run's index. |
| `amoeba_extend.py` | _(undescribed)_ |
| `amoeba_verify.py` | _(undescribed)_ |
| `brute.py` | _(undescribed)_ |
| `brute_bits.py` | _(undescribed)_ |
| `brute_capped.py` | _(undescribed)_ |
| `brute_extended.py` | Level-by-level BFS oracle for D(N): same definition as brute.py but drives one BFS step per level from N=0 up, recording D(N) for every level, and stops when a level exceeds a time budget. Verified reproducing D(2)=3 and D(10)=44499 first. Same exponential state space as brute.py; only used to push the oracle a little beyond what brute.py reaches. |
| `research_structure.py` | Structural analysis of PE763 growth rule: BFS computation of D(N) in d=2 and d=3, and verification of the reverse-merge (children→parent) reducibility characterization. |
