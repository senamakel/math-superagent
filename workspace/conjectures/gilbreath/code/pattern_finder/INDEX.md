# Index — code/pattern_finder

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `boundary_state.py` | Extracts the exact boundary-automaton state per row (halved w,i,e last three {0,2} entries; s,t bits; intruder c) from the real rows for k=1..161, and verifies the Rule-90 left-boundary law e_bits[k] = i_bits[k-1] ^ e_bits[k-1]. |
| `chain_stats_all.py` | _(undescribed)_ |
| `chain_value_stats.py` | _(undescribed)_ |
| `corrected_giant_analysis.py` | _(undescribed)_ |
| `cycle_floor_analysis.py` | Extracts exact structural sequences (b-series-derived quantities) from the genuine regime k=1..161 of blocks_depth1000.json. |
| `edge_sliding_independent.py` | _(undescribed)_ |
| `edge_sliding_timing.py` | _(undescribed)_ |
| `event_gap_analysis.py` | Event-gap analysis for the edge-sliding (rightmost-2 depth) prediction; consumes blocks_depth1000.json and conditional_rate_records.jsonl. |
| `extract_sequences.py` | Extracts the sequences of record (b, s, intruder, diffs, minima, regen rows, jumps, s-runs) from code/out/blocks_depth1000.json into the plain-text files now canonicalized in code/out/pattern_finder_outputs/. |
| `giant_parity_falsify.py` | _(undescribed)_ |
| `giant_parity_falsify2.py` | _(undescribed)_ |
| `giant_parity_significance.py` | _(undescribed)_ |
| `giants_1e9.py` | Larger-run settlement at sieve 1e9, depth 400: exact int64 streaming row generator (one row live, ~2.2 GiB peak, O(D·W) time) computing b_k = leading {0,2} block length each row, extracting (2,4)-regen events and giants (jump>1000), flooring per giant = W−row1−1−b_land, gap between consecutive giants (settling whether the 16th giant exists with floor>0, whether its gap exceeds the 64-row max, and whether gap_i/(j_i+1) and the geometric b-growth fit survive at landing b~40M+). Cross-checks rows 1..247 vs giants_6e8.json (must be []) and rows 1..161 vs blocks_depth1000.json; parity tail p=(C(n,1)+C(n,0))/2^n over 0-based rows; geometric (log2 OLS, numpy + exact Fraction closed form, must agree) and linear fits on landing blocks of genuine giants. Writes giants_1e9.json to code/out/pattern_finder_outputs/. Correctness: 30M/60-row smoke reproduced 6e8 giants 1-2 exactly (rows 35,57; jumps 1314,1739; landings 2179,5942), fit slopes agree to 4e-17. |
| `giants_6e8.py` | Giant-jump parity test at sieve 6e8: streams absolute-difference rows to depth 400 recording b_k (leading {0,2} block length) one row at a time (exact int64), extracts regen events and giants (jump>1000), reports k* = first no-intruder row, and prints giant pre-jump rows with 0-based parity, inter-giant gaps, landing blocks/jumps/floors. Answers whether any odd 0-based pre-jump giant row arises beyond the former cap artifact 161. Writes code/out/pattern_finder_outputs/giants_6e8.json. Correctness: cross-checked rows 1..161 exactly vs blocks_depth1000.json and independently re-derived events/giants/k*/gaps in pure Python from the saved b array, all matching; b up to row 300 matches the 3e8 record except the width-degraded tail (rows 239+ where the 3e8 block hits its finite edge). |
| `jump_closure_law.py` | Verifies the jump-closure law exactly over real prime rows: at a (2,4)-regeneration event, the jump j_k = b_{k+1} − b_k equals the closure-run length of the next row past the block. |
| `jump_smooth_run_law.py` | Exact verification of the Jump = Smooth-Run law: at a (2,4)-event, b_{k+1} = b_k + L_k where L_k is the length of the initial 1-Lipschitz run of the halved row past the block, minus one (jump is a one-row local fact). |
| `jump_smooth_run_wider.py` | _(undescribed)_ |
| `nu2_convention_resolve.py` | Resolves the two nu2 conventions (gap_parity floor0 on d[2:-1] vs incremental cyc floor2 on d[:-1]) on the same diagonal, showing both give identical nu2 and the real difference is which diagonal is traversed. |
| `nu2_dense_transfer.py` | Dense (30k consecutive n) measurement of the supply side of Route B: nu2(n)=#2s in maximal {0,2} suffix of the prime right-diagonal vs w(n)=mod-4 gap-bit weight; checks nu2>n^0.525 and the transfer nu2>=c*w on every n; writes code/out/nu2_dense.txt. |
| `nu2_linear_bound.py` | Sharpen the Route-B supply statement to the linear bound nu2>=c*n (dominates n^0.525): shows nu2>=0.45*n holds for every n>=823, giving a clean falsifier bound. |
| `nu2_postprocess.py` | Clean post-process of the dense nu2 run: min nu2/w by threshold, transfer-bound violation counts, fluctuation F_n=nu2-n//2, weak implied exponent, min nu2/n. |
| `nu2_shift_check.py` | Tests and REFUTES the run's claimed off-by-one reconciliation gap_parity(n)==incremental(n+1) (holds only 4/8 samples); the two implementations compute genuinely different diagonals. |
| `nu2_transfer_thresholds.py` | Exact last-hit thresholds for the transfer bound nu2<c*w for c in 0.5..0.85 over n=2..30000, giving clean falsifier bounds for "nu2>=c*w for all n>N_c". |
| `step6_ratio_table.py` | Directive 30: step-6 ratio-bound table for Gilbreath giants from the existing 6e8 extraction (code/out/pattern_finder_outputs/giants_6e8.json). No new sieve, 1 worker. Excludes the k*=248 floating==0 width artifact, asserts the 15 survivor rows and 14 gaps match the operator's examples, prints the per-giant table (b_land, j_i, gap, ratio gap/(j+1), margin b_land-1, flooring), fits the gap trend two ways (numpy polyfit vs exact-arithmetic closed-form slope 594/455, R^2=0.1163), computes fair and p=0.6 parity p-values (14/15 even: p_fair=1/2048, p_0.6=0.005172), fits geometric growth of log(b_land) (factor e^0.5769 = 1.7805, next b ~ 41.24M at row 302, requiring W ~ 41,244,539 = pi ~ N/ln N with N = 847,917,348), and checks the ratio/cumulative-margin sufficiency over all 14 gaps (0 failures, min margin 2156). Writes code/out/step6_ratio_table.captured.txt and .json. Correctness: flooring formula W-(row+1)-1-b_land recomputed independently in the script and asserted equal to the stored JSON column; survivor/gap lists PASS the operator's worked examples; OLS slopes PASS independent closed-form exact-arithmetic checks; EXIT_CODE=0. |
| `threshold_gap_table.py` | _(undescribed)_ |
| `verify_1e9_independent.py` | Independent verification of giants_1e9.json by a second route: re-derives the giant table (rows/jumps/landings/floors/gaps) from the saved raw b array in pure Python, re-checks rows 1..247 vs the 6e8 record, recomputes the parity tail (C(n,1)+C(n,0))/2^n in exact Fractions, refits log2 b_land vs row0 with numpy independently of the program's inline fit, compares geometric vs linear r2, and states the block-lemma protection bound (n+1 rows) implied by the full-width {0,2} row 248. Correctness: asserts every re-derived quantity against the JSON and prints the settlement numbers; any mismatch aborts nonzero. |
| `verify_giants_6e8.py` | Independent pure-Python (exact int/Fraction, no numpy) verification of giants_6e8.json: 15 genuine giants after excluding the flooring==0 artifact, 14 gaps, exact OLS of gaps and of log(landing blocks), exact p-values, recharge-identity consistency 14/14. Output: code/out/verify_giants_6e8.captured.txt. |
| `verify_step_law_transition.py` | Recomputes rows 235..240 at sieve 300M one row at a time, verifying the step law at the 238->239 transition (where a wide jump follows intrusion c=4); the OOM-fixed trustworthy version. |
| `wider_facts_verify.py` | _(undescribed)_ |
| `wider_giant_sequences.py` | _(undescribed)_ |
| `wider_giants_update.py` | _(undescribed)_ |
| `wider_width_clean.py` | _(undescribed)_ |
| `wider_width_extend.py` | _(undescribed)_ |
