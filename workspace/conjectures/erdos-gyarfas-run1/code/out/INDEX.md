# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute_run.txt` | Verbatim output of `cd /workspace/code && python brute.py` (the naive-oracle worked-example harness), captured this cycle with `tee`. Each line: minimum degree, exact simple-cycle-length set, and power-of-two cycle lengths for K4, K3,3, Petersen, cube Q3, and a graph6 round-trip of K4. All four worked examples match the hand-stated values in code/verify_cycles.py, and lib/cycles agrees with the independent hand DFS in code/eg/hand_dfs_check.py. The number a report citing the oracle's worked examples should point to. |
| `Z` | Zero-byte stray capture at the code/out root (empty on read). Carries no run result and should be ignored; not part of any cycle-length or verification output. Its twin at the workspace root was already deleted. Pending removal by a deletion-capable step — this role has no delete tool. |
