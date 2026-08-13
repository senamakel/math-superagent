# Index — code/boundary

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `boundary_cut_table.py` | Tabulates every known nontrivial left-half occurrence (witness set from code/out/witnesses.json + infinite Fibonacci family j=1..6) against the MRSTT boundary cut exp((log n)^(7/6)) with eps=1/2. No search — each rep verified math.comb(n,k)==a in exact arithmetic. Result: all 27 reps BOUNDARY, 0 interior. Capture code/out/boundary_cut_tabulation.captured.txt (EXIT_CODE=0). Supersedes the hanging code/boundary_cut.py. |
