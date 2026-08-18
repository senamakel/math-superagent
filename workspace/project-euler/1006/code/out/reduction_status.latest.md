# Reduction status (2026-08-18)

Commands run:

```sh
python code/lib/ueuclid.py > code/out/ueuclid_main.latest.txt
python code/verify_z_index.py
python code/solution.py
python code/directive9_transfer.py
```

Results:

- `ueuclid.py`: 30/30 random S0/S1/S2, 30/30 floor-sum checks, deterministic cases 6/6, and ue0 30/30 passed. The O(log) primitive is sound under its 1-indexed convention.
- `verify_z_index.py`: k=1,2,3 all ue0 floor moments agree with direct moments. Mechanical totals are 1, 101, 20302 and factor values at k=3 are `[1,10,100,101]`.
- `solution.py`: contiguous-window evaluator agrees with `mech_psi` for k=1..150 and gives Psi(10) = 10699667, but explicitly remains O(k), not a full-size solver.
- `directive9_transfer.py`: finite transfer checks k=1..150 pass; k=3 and k=10 reproduce 20302 and 10699667.

No valid O(log) reduction of the full Psi sum through a single `ueuclid` call was found. The obstruction is the k+1 distinct intercepts in formulation B; replacing them by one intercept is false already at k=1. Consequently the corrected anchors and Psi(10^18) were not run by an honest ueuclid reduction. No answer is claimed.
