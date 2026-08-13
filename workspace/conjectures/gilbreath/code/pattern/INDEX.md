# Index — code/pattern

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `analyze_genuine.py` | Analysis of the genuine (infinite-row) block-length sequence from genuine_sequences.json: local minima, strict regen jumps, s-runs, invariant checks, growth between minima. Agrees with the regeneration_* set on the same 161 live rows. |
| `bigjump_characterization.py` | Characterises the 13 giant regeneration jumps (j>1000) of the depth-1000 prime record: verifies each jump from blocks_depth1000.json plus the (edge,intruder)=(2,4) pair against an independent fresh recompute of rows A_0..A_165 (sieve 2e7, lib.gilbreath), then classifies each as GENUINE (landing block ends strictly inside the finite row; floor_distance = (W-i-2) - b_{i+1} >= 1 with a non-{0,2} intruder past the block) or CAPPED-ARTIFACT (floor_distance = 0; recorded j is a lower bound). Verdict: 12 of 13 genuine, only i=161 capped at width-exhaustion row 162. Writes code/out/bigjump_characterization.captured.txt; claim bigjump-cap-characterization-1000. |
| `blocks_deep.py` | Exact sieve-to-20M row generator for the primes to depth 1000 (O(D×W) time, O(W) memory), independent of the witness generator; saves blocks_depth1000.json with b, s, intruder and summary stats. Oracle-agrees on k=1..40; refuses to extend past a mismatch. Its captured summary is out/blocks_deep.captured.txt. |
| `boundary_check.py` | Boundary lemma verifier (block-protection constant). |
| `dump_sequences.py` | Dumps the sequence data from blocks_depth1000.json for the sequence tools (b, s, regen events, erosion runs, s runs, s changes). |
| `erosion_dynamics.py` | Verifies the erosion-track dynamics (x,y) exactly over every erosion row; confirms the regeneration trigger (x==2 && y==4) on every row (101/101 predictions, 60/60 triggers). |
| `erosion_run_ends.py` | Checks that every maximal pure-erosion run of the leading {0,2} block in the live regime (k=1..161, depth-1000 record) is directly followed by a regeneration: 26/26 confirmed; lengths listed. Pure record-arithmetic check over blocks_depth1000.json. |
| `erosion_run_predictor.py` | Closed-form predictor of the next regeneration row after an erosion-run start K, using the proved Rule-90 interior edge-bit evolution (XOR over bitwise submasks of d), the drain law y_{K+d} = max(4, y_K - 2·#{t<d: edgebit_t=1}) and the step law event iff (x,y)=(2,4): d* = min{d>=1 : edgebit_d=1 and y_{K+d}=4}. Compared against actual next event rows from the regenerated b record. Captured in out/erosion_run_predictor.captured.txt. |
| `extract_genuine.py` | Extracts the genuine (161 live rows, k=1..161) b, s, bits, intruder, diffs, runs into genuine_sequences.json, excluding the width-exhaustion tail. |
| `extract_witness.py` | Prints b(1..40), s(1..40), b(k+1)-b(k) from witnesses.json; the diffs are the consumption (-1) vs regeneration (>=0) measure. Verified: diffs match blocks_depth1000.json exactly. |
| `fresh_window.py` | Earlier probe of fresh-window regeneration (superseded). |
| `intruder_runs.py` | Intruder-run structure: the 17 maximal y=4 runs of the live regime (all end in regeneration), the erosion-step y-drain table, after-regen intruder counts by jump size. |
| `pinning_check.py` | Earlier check of block pinning (superseded). |
| `regen_from_json.py` | Re-derives regeneration/erosion/intruder summary from blocks_depth1000.json without rerunning the 20M sieve; lists every regeneration onset (k, b_k, b_{k+1}, diff, c_k) and erosion runs. Verified to reproduce blocks_deep.py's summary from the on-disk JSON. |
| `regeneration_analysis.py` | Regeneration-event analysis from blocks_depth1000.json: full 60-event table, regen rate by b-bucket, jump/gap histograms, runs test, Q1–Q5 of the regeneration questions. Captured in out/regeneration_analysis.captured.txt. |
| `regeneration_detail.py` | Follow-up detail for the regeneration note: s at events, gap histogram, big-jump ratios, intruder traces across the three longest genuine erosion runs. Captured in out/regeneration_detail.captured.txt. |
| `regeneration_lastfacts.py` | Last facts for the note: every 4-run's last row is a regeneration row; erosion-run start intruders; tall-intruder rows; y monotonicity check; min-b by row window. |
| `regeneration_successors.py` | Verification of successor patterns: every jump-0 stall followed by regeneration; after-regen successor counts; the y-drain staircases to 4; ASCII histograms. |
| `rule90_depth_test.py` | _(undescribed)_ |
| `rule90_depth_test2.py` | _(undescribed)_ |
| `sequence_extract.py` | _(undescribed)_ |
| `surplus_structure.py` | Structural probes on blocks_depth1000.json: (1) recharge surplus S_k = b_k - b_1 + (k-1) and its delta law S_{k+1}-S_k = (b_{k+1}-b_k)+1, monotonicity, and event-set (fixed this run: 1-based/0-based index bug and > vs >= event detection dropped the 17 jump-0 stalls — identity now exact over all k=1..1000, 60 events, monotone nondecreasing); (2) OLS slope log(jump) vs log(b) = 0.388 over 43 positive-jump events; (3) gap before large vs small jumps (no separation: 3.54 vs 2.48); (4) b-ratio across consecutive regen rows. Verified by independent one-line recomputation. Captured in out/surplus_structure.captured.txt, out/surplus_renewal_table.captured.txt; writeup out/surplus_renewal_structure.md. |
| `verify_intruder_law.py` | _(undescribed)_ |
