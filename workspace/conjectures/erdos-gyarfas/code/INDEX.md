# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for the Erdős–Gyárfás problem: returns a graph's minimum degree and exact set of cycle lengths by brute-force enumeration (networkx.simple_cycles, length ≥ 3). Verified by hand against K4, K3,3, cube, Petersen — all MATCH. The first run exposed and fixed a bug: simple_cycles on the bidirected graph yielded spurious length-2 cycles, now filtered. This is the reference checker every later claim on small graphs is checked against; not for use at full size. |
| `c4free_check.py` | _(undescribed)_ |
| `librarian_verify_markstrom.py` | Independent verification of the HoG graph6 for the Markström graph: decode, compare with HoG API adjacency list and tool_builder's reconstruction, run the cycle oracle (expect no C4/C8, yes C16), plus planarity and spanning-tree invariants. |
| `verify_connectivity_claims.py` | UNRUN check (librarian has no executor): refutes δ≥3⟹2-connected via two K4s+bridge, refutes dichotomy⟹2-connected, and checks Markström graph girth 3. Hand off to coder/tool_builder to execute; see research/summaries/connectivity-girth-minimal-ce.md. |
| `verify_level24.py` | Independent second-route re-scan of the level-24 census (level_24_classes.txt, 58713 graph6): recounts cubic / avoids-C4 / avoids-C4&C8 classes using lib.cycle_oracle, and confirms the single C4,C8-free member is the Markström graph with cycle set {3,5,6,7,9..24} including C16. Reproduces the census's classes=58713, avoidsC4=807, avoidsC4C8=1. |
