# Index — code/pattern_finder

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `boundary_state.py` | Extracts the exact boundary-automaton state per row (halved w,i,e last three {0,2} entries; s,t bits; intruder c) from the real rows for k=1..161, and verifies the Rule-90 left-boundary law e_bits[k] = i_bits[k-1] ^ e_bits[k-1]. |
| `corrected_giant_analysis.py` | _(undescribed)_ |
| `cycle_floor_analysis.py` | Extracts exact structural sequences (b-series-derived quantities) from the genuine regime k=1..161 of blocks_depth1000.json. |
| `edge_sliding_independent.py` | _(undescribed)_ |
| `edge_sliding_timing.py` | _(undescribed)_ |
| `event_gap_analysis.py` | Event-gap analysis for the edge-sliding (rightmost-2 depth) prediction; consumes blocks_depth1000.json and conditional_rate_records.jsonl. |
| `extract_sequences.py` | Extracts the sequences of record (b, s, intruder, diffs, minima, regen rows, jumps, s-runs) from code/out/blocks_depth1000.json into the plain-text files now canonicalized in code/out/pattern_finder_outputs/. |
| `giant_parity_falsify.py` | _(undescribed)_ |
| `giant_parity_falsify2.py` | _(undescribed)_ |
| `giant_parity_significance.py` | _(undescribed)_ |
| `giants_6e8.py` | Giant-jump parity test at sieve 6e8: streams absolute-difference rows to depth 400 recording b_k (leading {0,2} block length) one row at a time (exact int64), extracts regen events and giants (jump>1000), reports k* = first no-intruder row, and prints giant pre-jump rows with 0-based parity, inter-giant gaps, landing blocks/jumps/floors. Answers whether any odd 0-based pre-jump giant row arises beyond the former cap artifact 161. Writes code/out/pattern_finder_outputs/giants_6e8.json. Correctness: cross-checked rows 1..161 exactly vs blocks_depth1000.json and independently re-derived events/giants/k*/gaps in pure Python from the saved b array, all matching; b up to row 300 matches the 3e8 record except the width-degraded tail (rows 239+ where the 3e8 block hits its finite edge). |
| `jump_closure_law.py` | Verifies the jump-closure law exactly over real prime rows: at a (2,4)-regeneration event, the jump j_k = b_{k+1} − b_k equals the closure-run length of the next row past the block. |
| `jump_smooth_run_law.py` | Exact verification of the Jump = Smooth-Run law: at a (2,4)-event, b_{k+1} = b_k + L_k where L_k is the length of the initial 1-Lipschitz run of the halved row past the block, minus one (jump is a one-row local fact). |
| `threshold_gap_table.py` | _(undescribed)_ |
| `verify_step_law_transition.py` | Recomputes rows 235..240 at sieve 300M one row at a time, verifying the step law at the 238->239 transition (where a wide jump follows intrusion c=4); the OOM-fixed trustworthy version. |
| `wider_giant_sequences.py` | _(undescribed)_ |
| `wider_giants_update.py` | _(undescribed)_ |
| `wider_width_clean.py` | _(undescribed)_ |
| `wider_width_extend.py` | _(undescribed)_ |
