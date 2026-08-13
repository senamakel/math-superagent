# Index — code/pattern_finder

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `extract_sequences.py` | Extracts the sequences of record (b, s, intruder, diffs, minima, regen rows, jumps, s-runs) from code/out/blocks_depth1000.json into the plain-text files now canonicalized in code/out/pattern_finder_outputs/. |
| `boundary_state.py` | Extracts the exact boundary-automaton state per row (halved w,i,e last three {0,2} entries; s,t bits; intruder c) from the real rows for k=1..161, and verifies the Rule-90 left-boundary law e_bits[k] = i_bits[k-1] ^ e_bits[k-1]. |
| `cycle_floor_analysis.py` | Extracts exact structural sequences (b-series-derived quantities) from the genuine regime k=1..161 of blocks_depth1000.json. |
| `event_gap_analysis.py` | Event-gap analysis for the edge-sliding (rightmost-2 depth) prediction; consumes blocks_depth1000.json and conditional_rate_records.jsonl. |
| `jump_closure_law.py` | Verifies the jump-closure law exactly over real prime rows: at a (2,4)-regeneration event, the jump j_k = b_{k+1} − b_k equals the closure-run length of the next row past the block. |
| `jump_smooth_run_law.py` | Exact verification of the Jump = Smooth-Run law: at a (2,4)-event, b_{k+1} = b_k + L_k where L_k is the length of the initial 1-Lipschitz run of the halved row past the block, minus one (jump is a one-row local fact). |
