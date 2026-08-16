# Index — code/nu2_extended

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `compute_nu2_sos.py` | Streamed exact nu2(n) for prime h via per-n O(n log n) submask-product SOS (s_sos) up to n=20000 — reports dips<0.42, [50,N] means, and last-half-window variance. Cross-checked s_sos vs s_direct on n=4..200 and against the independent character-sum s_char_runs at n=274,53,1000,5000,10000,20000 (all match). Output: code/out/nu2_extended.txt. |
| `track_smax.py` | Streams exact nu2(n) for prime h via per-n O(n log n) s_sos (no triangle) for n=50..N and reports the trajectory of |
