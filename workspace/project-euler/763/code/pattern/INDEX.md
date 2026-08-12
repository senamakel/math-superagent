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
| `pn_poly.py` | Computes P_N(x)=sum_k Q_k(N)x^k and checks D(N)=3^(N-1)P_N(1/9); detects the even-N discrepancy in the Q-decomposition. |
| `poly_test.py` | _(undescribed)_ |
| `q45.py` | _(undescribed)_ |
| `q_array.py` | Extracts the full triangular array Q_k(N) = N(N,N-k)/3^(N-2k-1) from the data/level_N.txt feature dumps and prints each offset column k as a sequence of exact rationals, for OEIS-style closed-form hunting on the N(N,M) table. |
| `q_bivariate.py` | _(undescribed)_ |
| `q_coeff_pattern.py` | _(undescribed)_ |
| `q_columns_fresh.py` | Rebuilds the full Q_k(N)=R(N,N-k)/3^(N-2k-1) table from data/level_N.txt + code/out/mhist_13_14.txt and does exact finite-difference tests proving each Q_k (k=0..4) is a degree-k polynomial, with fresh N=13,14 as out-of-sample. Backs the re-confirmed max-level decomposition. |
| `q_decomp_verify.py` | _(undescribed)_ |
| `q_fresh_test.py` | _(undescribed)_ |
| `q_fresh_verify.py` | Sympy-exact verification of the Q_k closed forms (Q_0..Q_4) and leading coefficients (==1/k!) at every measured point incl the fresh OOS N=13,14; also confirms the Q_2 column == OEIS A055999. |
| `q_verify.py` | _(undescribed)_ |
| `qdecomp_falsify.py` | _(undescribed)_ |
| `recur.py` | Recurrence search over D(0..14): constant-coefficient orders 1..7, holonomic forms, and asymptotic ratio fit. Found the order-7 constant-coeff recurrence that is later shown (recur_deadend.py) to be an overfit. |
| `recur2.py` | _(undescribed)_ |
| `recur3.py` | _(undescribed)_ |
| `recur_deadend.py` | Characterizes the order-7 constant-coefficient recurrence (3D[n]=9D[n-1]+12D[n-2]-17D[n-3]-30D[n-4]-31D[n-5]+63D[n-6]) fitted over D(0..14): shows its first extrapolated term is non-integer (fails at n=18), so the recurrence can never reproduce D(20)/D(100). Records this as a dead end. |
| `recur_integral.py` | _(undescribed)_ |
| `recur_test.py` | _(undescribed)_ |
| `transfer_hunt.py` | Hunt for a row-to-row transfer recurrence in R(N,M) (configs by max level M) like R(N,M)=c0 R(N-1,M)+c1 R(N-1,M-1)+c2 R(N-1,M-2) or a fixed transfer matrix — the 3D analog of the 2D A007902 G(k,m) recurrence that would compute D(10000) without BFS. Uses exact least-squares on data/level_N.txt + mhist_13_14.txt and inspects neighbor ratios; companion to transfer_search.py/transfer_search2.py in the dead transfer-recurrence hunt. |
| `transfer_search.py` | _(undescribed)_ |
| `transfer_search2.py` | _(undescribed)_ |
| `triangle_build.py` | Builds the max-level triangle R(N,M)=#distinct reachable configs after N divisions with max level M (from data/level_N.txt N=2..12 and mhist_13_14.txt N=13,14), prints the raw triangle, the M=N diagonal, and each offset column R(N,N-k) raw and normalized to Q_k(N)=R(N,N-k)/3^(N-2k-1) as exact Fractions. Backs the Q_k/column closed-form and diagonal study. |
| `verify_a186085.py` | _(undescribed)_ |
| `verify_columns.py` | _(undescribed)_ |
| `verify_forms.py` | sympy-exact check of Q_0..Q_3 closed forms on every measured point including fresh N=13,14; fits Q_4 (degree 4) on N=9..13 and predicts N=14=979 (OOS pass). |
| `verify_mhist.py` | _(undescribed)_ |
| `verify_reconstruct.py` | Reconstructs D(N) from the max-level column model: verifies the M=N diagonal count equals 3^(N-1) for all N=2..14, then sums the modeled columns N(N,M)=Q_k(N)*3^(N-2k-1) for k=0..4 (closed forms Q_0..Q_4) and checks the sum reproduces the true D(N) where those columns cover every M row (N=8,9 exactly; reports which rows exceed k=4 for larger N). Independent confirmation that the Q_k closed forms re-assemble into D(N). Companion to q_verify.py/verify_forms.py. |
