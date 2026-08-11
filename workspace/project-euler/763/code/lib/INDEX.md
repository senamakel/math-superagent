# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `amoeba.py` | Reusable PE763 routines shared by every oracle and data dump: fixed-width int-bitmask encode/decode, structural feature extraction (level histogram, bbox, max level M), and the one-step BFS successor function next_level_bits. Correctness established by the brute oracles reproducing D(2)=3 and D(10)=44499. |
| `amoeba2d.py` | Reusable routines for the 2D amoeba (PE763 in d=2): int-bitmask encode/decode and the one-step BFS successor next_level_bits2_compact using compact per-level grid width. The 2D companion to code/lib/amoeba.py; its correctness is established by cross-check against the frozenset oracle in code/amoeba/d2_check.py. |
