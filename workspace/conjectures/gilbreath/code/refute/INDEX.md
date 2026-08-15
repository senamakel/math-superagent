# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `RUNME.txt` | _(undescribed)_ |
| `RUN_exhaust.md` | _(undescribed)_ |
| `WHERE.md` | _(undescribed)_ |
| `break_carved_gap24.py` | _(undescribed)_ |
| `calibrate.p` | Calibration of the find_counterexample tool: a trivially-refutable relational problem (element b has ~p, conjecture every element has p). Returned 'undecided', confirming the tool gives no counterexample channel in this environment (consistent with the run's cb_dying_pair_statement.md observation). |
| `carved_gap24_corner.p` | TPTP encoding of the carved-{2,4} corner claim for find_counterexample (gaps in {2,4} make A_2 the {0,2} corner). Returned undecided like every encoding in this environment. |
| `cb_dying_pair.p` | _(undescribed)_ |
| `cb_dying_pair_clean.p` | _(undescribed)_ |
| `cb_dying_pair_confirmed.p` | _(undescribed)_ |
| `cb_dying_pair_rel.p` | _(undescribed)_ |
| `cb_dying_pair_relational.p` | _(undescribed)_ |
| `cb_dying_pair_statement.md` | Records the located internal contradiction in the open gap CB-dying-pair: the dying row's b=1 claim contradicts the dying condition (b must be 0). |
| `cb_dying_pair_tff.p` | _(undescribed)_ |
| `check_cb_dying_pair.py` | Reference script reproducing the CB-dying-pair reasoning on delete-7/delete-5/delete-11 failing triangles. |
| `doit.sh` | _(undescribed)_ |
| `exec_search.py` | _(undescribed)_ |
| `exhaust_carved_gap24.py` | _(undescribed)_ |
| `g_balance.p` | TPTP numeric fragment of the per-event G-balance claim (two events separated by two erosions), used with find_counterexample. Note: the naive encoding collapses to a trivial domain, so find_counterexample's answer is not a meaningful second route. |
| `g_balance_check.py` | Verifies the strong per-event form of G-balance (j >= d at every (2,4)-event) against blocks_depth1000.json; documents the refutation by counting every j<d event. |
| `g_balance_numeric.p` | _(undescribed)_ |
| `g_supply_transfer.p` | TPTP encoding of the G-supply-transfer claim (find_counterexample returned undecided; the environment cannot interpret arithmetic). The refutation itself rests on the exact hand arithmetic in g_supply_transfer_refuted.md. |
| `g_supply_transfer_refuted.md` | Records the refutation of G-supply-transfer: consecutive-odds prefix (2,3,5,7,9) is successful with w=2 but nu2<=1, violating nu2>=(2/3)w; decides the S1 fork to prime-specific. Exact hand arithmetic, model finder unavailable for arithmetic. |
| `import_check.py` | _(undescribed)_ |
| `kernel_characterize.py` | Characterises the F2 transfer matrix Phi_n of the G-supply linearisation. Part A: builds Phi_n (rows k=2..n-2 tail cells, cols j=2..n-1 halved gap bits, entry [C(k-1, j-(n-k)) mod 2], ancestor window [n-k,n-1]) for n=2..20; rank=n-3, nullity=1, kernel spanned by the all-ones vector (each row XORs a full Pascal row sum 2^(k-1) even), so nu2=wt(Phi_n·1)=0 and no positive universal covering constant c (nu2>=w/c for all h) exists. Part B: sieve 1e6, measures nu2/w on the real primes for n up to 3000 (min 0.5152 at n=53) — the real bit string avoids the kernel. Correctness: Part B matches nu2_vs_gap_parity.py exactly on shared samples; Part A rank/nullity matches phi_nullspace.py. Exact integers. Output: code/out/kernel_characterize.captured.txt, .notes.md. |
| `nu2_transfer.p` | _(undescribed)_ |
| `phi_nullspace.py` | _(undescribed)_ |
| `placeholder.py` | _(undescribed)_ |
| `run_carved_gap24.py` | _(undescribed)_ |
| `run_exhaust_carved.sh.py` | _(undescribed)_ |
| `run_search.py` | _(undescribed)_ |
| `search_allzero_subclaim.py` | _(undescribed)_ |
| `search_carved_gap24.py` | Brute-force exhaustive generator for the {2,4}-gap class; computes the Gilbreath triangle for every binary gap string over a window and reports any leading-1 death. Written as the verification oracle for R-carved-gap24 (no counterexample found; the class is settled by the corner argument instead). |
| `search_intruder4_rung.py` | _(undescribed)_ |
| `tooltest.p` | _(undescribed)_ |
| `tooltest2.p` | _(undescribed)_ |
| `tooltest3.p` | _(undescribed)_ |
| `universal_transfer_matrix.py` | _(undescribed)_ |
| `universal_transfer_matrix_run.py` | Full exhaustive run of the S1-nu2-transfer-weight claim. (A) checks wt(Phi_n h) >= wt(h)/2 for ALL h in {0,1}^{n-2} at n=4..20 (refuted: first counterexample n=4, h=[1,1], nu2=0<w/2=1; 19,947 violators total). (B) exact worst-case ratio min_{h!=0} wt(Phi_n h)/wt(h) per n — uniformly 0 for every n=4..20, achieved by the all-ones h (nu2=0). (C) direct triangle construction of consecutive-odds q=(2,3,5,7,9,...): bottom entry 1 (SUCCESS) for every n=1..18 while nu2=0 and w=n-2, confirming the recorded claim g-supply-transfer-refuted. Phi_n entry (k,j) = C(k-1, j-(n-k)) mod 2 for j in [n-k,n-1]. Correctness: exact integer arithmetic; (C) cross-checked independently via lib.gilbreath.rows_generator and lib.rightdiag.incremental_diagonals (identical diagonals). Output: code/out/universal_transfer_matrix_RUN.captured.txt. |
| `verify_cb_dying_pair.py` | _(undescribed)_ |
| `verify_hand_findings.py` | _(undescribed)_ |
| `verify_transfer_refutation.py` | Independent exact reproduction of the G-supply-transfer refutation on consecutive odds using lib.gilbreath oracle on the run's settled class. |
