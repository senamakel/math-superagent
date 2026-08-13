# Index — code/pattern

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `analyze_genuine.py` | Analysis of the genuine (infinite-row) block-length sequence from genuine_sequences.json: local minima, strict regen jumps, s-runs, invariant checks, growth between minima. Agrees with the regeneration_* set on the same 161 live rows. |
| `blocks_deep.py` | Exact sieve-to-20M row generator for the primes to depth 1000 (O(D×W) time, O(W) memory), independent of the witness generator; saves blocks_depth1000.json with b, s, intruder and summary stats. Oracle-agrees on k=1..40; refuses to extend past a mismatch. Its captured summary is out/blocks_deep.captured.txt. |
| `boundary_check.py` | Boundary lemma verifier (block-protection constant). |
| `dump_sequences.py` | Dumps the sequence data from blocks_depth1000.json for the sequence tools (b, s, regen events, erosion runs, s runs, s changes). |
| `erosion_dynamics.py` | Verifies the erosion-track dynamics (x,y) exactly over every erosion row; confirms the regeneration trigger (x==2 && y==4) on every row (101/101 predictions, 60/60 triggers). |
| `erosion_run_ends.py` | Checks that every maximal pure-erosion run of the leading {0,2} block in the live regime (k=1..161, depth-1000 record) is directly followed by a regeneration: 26/26 confirmed; lengths listed. Pure record-arithmetic check over blocks_depth1000.json. |
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
| `sequence_extract.py` | _(undescribed)_ |
