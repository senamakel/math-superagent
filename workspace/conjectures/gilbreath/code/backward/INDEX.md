# Index — code/backward

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `erosion_runs.py` | Extract every erosion run (maximal stretch of rows with b_{k+1}=b_k-1) from a prime Gilbreath triangle re-generated in numpy int64, and verify the REG-intruder-drains claim. For each run computes y0, yf, edge-2 flip count, run length d, initial block b0, and block-nonzero. Checks (i) drain-law flips==(y0-yf)/2 and (ii) yf=4 with b>=1 and nonzero block, both with zero violations on the 2e7/6e8/1e9 records (rows 1..247). Oracle: reproduces blocks_depth1000.json b and intruder arrays exactly. Output: code/out/erosion_run_draining.captured.txt. |
