# Index — code/verify_literature

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `cubic_nole_to16.py` | Bounded n<=16 exhaustive corroboration via nauty-geng + oracle: no connected cubic graph on n<=16 lacks both C4 and C8 (counts 1,2,5,19,85,509,4060 = A000421, zero no-C4&C8-free). Consistent with published first-at-24; corroborates low end only. |
| `reproduce_markstrom.py` | Fresh independent verification of Markström extremal-cycle data with the oracle: re-verifies K4 {3,4}, K3,3 {4,6}, cube {4,6,8}, Petersen {5,6,8,9}, then reconstructs the Markström graph (HoG 51419) from its published adjacency list and checks it is cubic on 24, has no C4/C8, contains C16, and has MathWorld profile {3,5,6,7,9..24}. RUN: all MATCH, reproduction MATCHES published claim. |
