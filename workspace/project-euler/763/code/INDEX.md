# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | House rules for working inside code/: programs live here, outputs in code/out/, code is a package tree with lib/, and every program's index row must say what established it correct (brute oracle keeps its agreed examples). Read before writing a program. |
| `amoeba_extend.py` | Extended BFS oracle for PE763 that also dumps per-config structural features (level histogram, bbox dims, max level M) for levels in a range to /workspace/data/level_N.txt. Uses lib/amoeba.py for verified BFS + feature code. Reproduces D(2)=3, D(10)=44499, D(12)=514419, D(13)=1749267; cap is 5,000,000 states. |
| `amoeba_verify.py` | Structurally independent BFS oracle for PE763 D(N): rebuilds the occupied cube set per config and tests forward-neighbour emptiness directly (different successor generation from lib/amoeba). Validated on D(0..13) and used as the second route to confirm D(14)=5949063. |
| `brute.py` | Naive BFS oracle for D(N): enumerates every distinct set of occupied cubes reachable after exactly N divisions. Returns len of reachable sets. Verified: D(2)=3, D(10)=44499 match the statement. Exponential state space; only for N<=~10. |
| `brute_bits.py` | Memory-compact BFS oracle for D(N) using fixed-width W bitmask per config, so the encoding is level-independent. Cross-checked against brute_extended.py (the frozenset oracle, validated on D(2)=3, D(10)=44499) for N=0..12. The one-step successor next_level_bits is IMPORTED from lib/amoeba.py (the single shelved definition), not duplicated here. Same exponential state space; pushes the oracle a little further than the frozenset version. |
| `brute_capped.py` | Capped BFS oracle for D(N): drives levels up to a max-depth arg, stops when the frontier exceeds 600k states, prints the full D(N) sequence and the checks D(2)=3, D(10)=44499. This is the live-at-root brute.py, moved under code/ so the root holds only Markdown; verified reproducing D(2)=3 and D(10)=44499. |
| `brute_extended.py` | Level-by-level BFS oracle for D(N): same definition as brute.py but drives one BFS step per level from N=0 up, recording D(N) for every level, and stops when a level exceeds a time budget. Verified reproducing D(2)=3 and D(10)=44499 first. Same exponential state space as brute.py; only used to push the oracle a little beyond what brute.py reaches. |
| `research_structure.py` | Structural analysis of PE763 growth rule: BFS computation of D(N) in d=2 and d=3, and verification of the reverse-merge (children→parent) reducibility characterization |
