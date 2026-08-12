# Index — code/pattern

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `a186085.py` | _(undescribed)_ |
| `aggregate_triangle.py` | _(undescribed)_ |
| `bottom_probe.py` | Probes the bottom of the (N,M) max-level triangle: reports the min-M per N (and whether it stays near N/2) from data/level_N.txt + code/out/mhist_13_14.txt, and prints the full Q_k = count/3^(N-2k-1) array including negative-exponent (large k) rows as exact Fractions, testing whether the Q_k-polynomial column model extends into large k. Structural probe of the max-level decomposition. |
| `check_a186085_recurrence.py` | _(undescribed)_ |
| `columns.py` | _(undescribed)_ |
| `d2_oeis.py` | _(undescribed)_ |
| `diagonal.py` | Checks the M=N diagonal conjecture for PE763's structural parameter M (max level): tabulates count of configs with max level M=N against 3^(N-1), plus the near-diagonal M=N-1 column, reading the /workspace/data/level_N.txt feature dumps. |
| `distinct_hist_from_data.py` | _(undescribed)_ |
| `fit_qk.py` | _(undescribed)_ |
| `fresh_recheck.py` | Fresh independent re-check of the max-level decomposition: rebuilds the (N,M) histogram from raw data/level_N.txt + mhist_13_14.txt, prints the exact-rational Q_k columns (limited to non-negative exponent), checks each column's leading coefficient via finite differences, and probes whether the level histogram alone determines a config (counts configs sharing a histogram at N=4). Companion to the Q_k closed-form study. |
| `full_triangle.py` | _(undescribed)_ |
| `full_triangle_dump.py` | Builds the full R(N,M) max-level triangle (#distinct configs after N divisions with max level M) from data/level_N.txt (N=2..12) plus code/out/mhist_13_14.txt (N=13,14); verifies R(N,N)=3^(N-1) and D(N)=sum_M R(N,M), and prints each fixed-M column R(N,M) as N varies for transfer-structure hunting. Now imports sorted_key from lib/datafiles (its former local split('level_') copy was a fourth duplicate of the canonical definition, now consolidated). |
| `holonomic2.py` | _(undescribed)_ |
| `holonomic3.py` | Clean sweep of the holonomic (P-recursive) hypothesis: fits sum_j p_j(N)D[N+j]=0, p_j degree d, over m=1..6, d=1..4 on D(0..14); extends each nullspace solution to D(100) requiring integer values, and tags any exactly reproducing both held-out values D(20)=9204559704 and D(100) mod 10^9=780166455. Companion to holonomic_fit.py/holonomic2.py; refutes the holonomic P-recursive closed form. Uses fit() from lib/holonomic (consolidated). |
| `holonomic_diag.py` | _(undescribed)_ |
| `holonomic_fit.py` | _(undescribed)_ |
| `mdist.py` | Counts reachable configs by max level M from the data/level_N.txt feature dumps, producing the (N,M) histogram rows that underlie the max-level decomposition. |
| `mdist2.py` | _(undescribed)_ |
| `offsets.py` | _(undescribed)_ |
| `oos_predict.py` | Decisive out-of-sample test of the column-polynomial model: fits Q_0..Q_5 polynomials using ONLY N=2..12 data, then predicts N(N,M)=Q_k(N)*3^(N-2k-1) at fresh N=13,14 (from code/out/mhist_13_14.txt) and reconstructs D(N). Checks the N(N,M)=Q_k(N)*3^(N-2k-1) submodel holds on points never used in the fit. |
| `pn_poly.py` | _(undescribed)_ |
| `poly_test.py` | _(undescribed)_ |
| `q45.py` | _(undescribed)_ |
| `q_array.py` | _(undescribed)_ |
| `q_bivariate.py` | _(undescribed)_ |
| `q_coeff_pattern.py` | _(undescribed)_ |
| `q_columns_fresh.py` | _(undescribed)_ |
| `q_decomp_verify.py` | _(undescribed)_ |
| `q_fresh_test.py` | _(undescribed)_ |
| `q_fresh_verify.py` | _(undescribed)_ |
| `q_verify.py` | _(undescribed)_ |
| `qdecomp_falsify.py` | _(undescribed)_ |
| `recur.py` | _(undescribed)_ |
| `recur2.py` | _(undescribed)_ |
| `recur3.py` | _(undescribed)_ |
| `recur_deadend.py` | _(undescribed)_ |
| `recur_integral.py` | _(undescribed)_ |
| `recur_test.py` | _(undescribed)_ |
| `transfer_hunt.py` | _(undescribed)_ |
| `transfer_search.py` | _(undescribed)_ |
| `transfer_search2.py` | _(undescribed)_ |
| `triangle_build.py` | _(undescribed)_ |
| `verify_a186085.py` | _(undescribed)_ |
| `verify_columns.py` | _(undescribed)_ |
| `verify_forms.py` | _(undescribed)_ |
| `verify_mhist.py` | _(undescribed)_ |
| `verify_reconstruct.py` | _(undescribed)_ |
ribed)_ |
| `verify_a186085.py` | _(undescribed)_ |
| `verify_columns.py` | _(undescribed)_ |
| `verify_forms.py` | _(undescribed)_ |
| `verify_mhist.py` | _(undescribed)_ |
| `verify_reconstruct.py` | _(undescribed)_ |
