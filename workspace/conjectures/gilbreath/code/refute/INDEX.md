# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `RUNME.txt` | _(undescribed)_ |
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
| `exec_search.py` | _(undescribed)_ |
| `g_balance.p` | TPTP numeric fragment of the per-event G-balance claim (two events separated by two erosions), used with find_counterexample. Note: the naive encoding collapses to a trivial domain, so find_counterexample's answer is not a meaningful second route. |
| `g_balance_check.py` | Verifies the strong per-event form of G-balance (j >= d at every (2,4)-event) against blocks_depth1000.json; documents the refutation by counting every j<d event. |
| `g_balance_numeric.p` | _(undescribed)_ |
| `g_supply_transfer.p` | TPTP encoding of the G-supply-transfer claim (find_counterexample returned undecided; the environment cannot interpret arithmetic). The refutation itself rests on the exact hand arithmetic in g_supply_transfer_refuted.md. |
| `g_supply_transfer_refuted.md` | Records the refutation of G-supply-transfer: consecutive-odds prefix (2,3,5,7,9) is successful with w=2 but nu2<=1, violating nu2>=(2/3)w; decides the S1 fork to prime-specific. Exact hand arithmetic, model finder unavailable for arithmetic. |
| `import_check.py` | _(undescribed)_ |
| `nu2_transfer.p` | _(undescribed)_ |
| `phi_nullspace.py` | _(undescribed)_ |
| `placeholder.py` | _(undescribed)_ |
| `run_carved_gap24.py` | _(undescribed)_ |
| `run_search.py` | _(undescribed)_ |
| `search_allzero_subclaim.py` | _(undescribed)_ |
| `search_carved_gap24.py` | Brute-force exhaustive generator for the {2,4}-gap class; computes the Gilbreath triangle for every binary gap string over a window and reports any leading-1 death. Written as the verification oracle for R-carved-gap24 (no counterexample found; the class is settled by the corner argument instead). |
| `search_intruder4_rung.py` | _(undescribed)_ |
| `tooltest.p` | _(undescribed)_ |
| `tooltest2.p` | _(undescribed)_ |
| `tooltest3.p` | _(undescribed)_ |
| `universal_transfer_matrix.py` | _(undescribed)_ |
| `verify_cb_dying_pair.py` | _(undescribed)_ |
| `verify_transfer_refutation.py` | Independent exact reproduction of the G-supply-transfer refutation on consecutive odds using lib.gilbreath oracle on the run's settled class. |
