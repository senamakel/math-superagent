# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for PE620 written by a concurrent agent; same continuous-d model as lib/gears.py but with the corrected phase sign F = R*beta - r*gamma + T (T_sign=+1) and an independent direct phase-solve verify_solution. As of this run it has not been executed to completion here; its companion note oracle-model-broken.md reports the same g(16,5,5,6)=0 verdict on the lib.gears path. Kept as the corroborating oracle candidate; unverified until run. |
| `oracle_test.py` | Driver testing the lib/gears.py meshing model against the PE620 oracle values: g_count(16,5,5,6), G(16), G(20). Prints per-pair g distribution, wall-clock times, and AGREE/DISAGREE verdicts; saves full output to code/out/oracle_test.txt. Result: model FAILED all three (0 vs 9, 0 vs 9, 0 vs 205). Runs from /workspace/code so `from lib.gears import ...` works. G(20) pass uses grid_points=50000 because the default 400000 grid would exceed the 600s tool cap (~11 min); g(16,5,5,6) is run at the full 400000 grid. |
