# Index — code/pattern

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `analyze_genuine.py` | _(undescribed)_ |
| `blocks_deep.py` | Exact sieve-to-20M row generator for the primes to depth 1000 (O(D*W) time, O(W) memory), independent of the witness generator; saves blocks_depth1000.json with b, s, intruder and summary stats. Oracle-agrees on k=1..40; refuses to extend past a mismatch. Its captured summary is out/blocks_deep.captured.txt. |
| `boundary_check.py` | _(undescribed)_ |
| `dump_sequences.py` | _(undescribed)_ |
| `erosion_dynamics.py` | _(undescribed)_ |
| `extract_genuine.py` | _(undescribed)_ |
| `extract_witness.py` | Prints b(1..40), s(1..40), b(k+1)-b(k) from witnesses.json; the b(k+1)-b(k) diffs are the consumption (-1) vs regeneration (>=0) measure. Verified: diffs match blocks_depth1000.json exactly. |
| `fresh_window.py` | _(undescribed)_ |
| `intruder_runs.py` | _(undescribed)_ |
| `pinning_check.py` | _(undescribed)_ |
| `regen_from_json.py` | Re-derives regeneration/erosion/intruder summary from blocks_depth1000.json without rerunning the 20M sieve; lists every regeneration onset (k, b_k, b_{k+1}, diff, c_k) and erosion runs. Verified to reproduce blocks_deep.py's summary from the on-disk JSON, and to agree with the c>=6 erosion theorem exactly on all 999 transitions. |
| `regeneration_analysis.py` | _(undescribed)_ |
| `regeneration_detail.py` | _(undescribed)_ |
| `regeneration_lastfacts.py` | Last facts for the note: every 4-run's last row is a regeneration row; erosion-run start intruders; tall-intruder rows; y monotonicity check; min-b by row window. |
| `regeneration_successors.py` | _(undescribed)_ |
)_ |
