# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `verify_independent.py` | Independent machinery check for PE 579, not the final answer. Task 1: re-runs primary-quaternion logic (primary primitive quats == all primitive quats for odd N<=30, and N==edge length) — PASS. Task 2: exhaustively proves (frame_method vector-pairing enumeration, norm cap relaxed to sqrt(3)n + box-fit filter) no primitive frame in [0,n]^3 has even edge length for n<=80 — PASS. Task 3: recomputes C(n),S(n) via frame_method enumeration + solution_power.compute_power for n=1,2,4,5,10,50, all matching oracle. Task 4: N/A (solution.py absent). Writes /workspace/verify_independent_output.txt. |
