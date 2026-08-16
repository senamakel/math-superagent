# Index — code/order_k

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `_run_refute_kstar.sh` | _(undescribed)_ |
| `input_strictness.py` | Settles the documented open lemma G-input-strictness by exhibition: for the single-1 string h=e_{n-2} (one from the end), the fold reads position n-2 only at odd depths d in [2,n-1] (since o=d-1⊆d iff d odd), so nu2(n)=#{odd d in [2,n-1]}=ceil((n-2)/2) and S(n)=(n-2)-2*nu2(n)∈{0,1}→ |
| `kstar_exact.py` | Decisive exact computation of the correlation-order budget K*(n) of the SUPPLY fold under the authoritative cumulative definition (C_1..C_K = histograms of word-lengths 2..K+1 over overlapping windows, exact integer grouping, NOT a hash and NOT single C_K). Exhaustive over all 2^n strings n=2..15, S^2 via canonical lib.supply_fold.s_sos (floored fold d in [2,n-1]). Gates: reproduces the n=8 witness h=00000010(64)/h'=00000100(32), C_1=(5,1,1,0), S^2=0 vs 4 (so K*(8)>=2); negative control Witness(n,n-1)=False at every n. Verdict: K*(n)=floor(n/2) for n=2..15, contradicting the reopened GOAL premise ceil(n/2) at every odd n. Cross-checked by code/sat_solver/orderk_oracle.py. Output code/out/kstar_exact.captured.txt. |
| `kstar_settle.py` | Independent exact computation of the SUPPLY fold's correlation-order budget K*(n) on the cumulative C_1..C_K definition, n=2..16, with s_sos cross-checked against an independent direct submask-XOR brute. Establishes K*(n)=floor(n/2) and extends the prior n=15 ceiling. |
| `kstar_settle_minmax.py` | Memory-light independent confirmation of the SUPPLY fold's K*(n)=floor(n/2), computing n=17 and n=19 (the divergence points where ceil and floor differ inside the prior imported table) via per-fibre (min,max) of S2 so only the fibre dictionary is materialised. |
| `kstar_settle_ml.py` | _(undescribed)_ |
| `order_budget.py` | _(undescribed)_ |
| `readcone_survey.py` | Surveys single-1 and fixed sparse read-cones of the SUPPLY fold to test whether a FIXED density-0 string can keep S(n)=O(sqrt n). (1) Computes read-cone size |
| `refute_kstar.py` | Independent refutation check of the correlation-order budget claim K*(n)=ceil(n/2): recomputes K* with the authoritative cumulative C_1..C_K definition and canonical s_sos oracle, exhaustively over 2^n strings (n<=15). Used to settle whether R-budget-n32's ceil formula or kstar_exact.py's floor conclusion is correct at odd n. |
