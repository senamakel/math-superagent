# Index — code/nu2_extended

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `compute_nu2_sos.py` | Streamed exact nu2(n) for prime h via per-n O(n log n) submask-product SOS (s_sos) up to n=20000 — reports dips<0.42, [50,N] means, and last-half-window variance. Cross-checked s_sos vs s_direct on n=4..200 and against the independent character-sum s_char_runs at n=274,53,1000,5000,10000,20000 (all match). Output: code/out/nu2_extended.txt. |
| `kstar_brute_table.py` | _(undescribed)_ |
| `kstar_budget_explicit.py` | Decisive budget settlement for GOAL priority 3: exhaustively re-derives B(n)=min-K-constant and A(n)=budget for n=2..18 on the canonical oracle, and prints an explicit witness pair (same C_A fiber, different S^2) at the largest-K witness for each n so every crossing is hand-checkable. Shows the imported ceil(n/2) budget table is wrong from n>=6. |
| `kstar_resolve.py` | Memory-lean exact brute oracle for the budget K*(n): streams all 2^n strings by integer (never stores the set), builds a compact canonical (K+1)-gram histogram key, and computes A(n)=largest-K-with-witness and B(n)=min-K-constant on every C_K fiber via the canonical s_sos oracle. Fixed the OOM of kstar_brute_table.py. Agrees exactly with orderk_correlation.py (n<=12) and kstar_structural.py (n<=14) on B. |
| `kstar_structural.py` | Decisive structural test of the claim K*(n)=R(n)−1, where R(n) = max over d,d'∈[2,n−1] of the maximal run length of the fold-row symmetric difference M_d△M_d'. Computes R(n) exactly n=2..200 (closed form: 2^k on (2^k,2^{k+1}), 2^j−3 at n=2^j), compares against the imported K* table and ceil(n/2), and independently verifies the characterization by exhaustive 2^n fiber enumeration n=4..14 under BOTH the single-C_K histogram definition and the cumulative C_1..C_K definition, extracting explicit counterexample pairs (n=6,K=3: 001001/010010 same 4-gram multiset, S²=4 vs 0, all runs≤4). Verdict REFUTED both ways; cumulative K*=floor(n/2). Establishes correctness: c_k cross-checked against independent construction n=4..9 all strings; s_sos vs s_direct agree n=4..9; R closed form matches exact to n=200; REOPENED n=8 K=1 witness reproduced. Output: code/out/kstar_structural_capture.txt. |
| `orderk_correlation.py` | _(undescribed)_ |
| `track_smax.py` | Streams exact nu2(n) for prime h via per-n O(n log n) s_sos (no triangle) for n=50..N and reports the trajectory of |
