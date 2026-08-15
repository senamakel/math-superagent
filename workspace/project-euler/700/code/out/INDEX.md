# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `alpha_cf.py` | _(undescribed)_ |
| `ap_check.py` | Detects maximal runs of constant consecutive difference (AP runs) in the PE700 Eulercoin value and index sequences; both split into the same 17 runs. |
| `ap_coverage.py` | _(undescribed)_ |
| `ap_diag.py` | _(undescribed)_ |
| `ap_fix.py` | Corrects the shared-boundary double count between adjacent AP runs; confirms V=1517926517777556. |
| `ap_relation.py` | Verifies that within each AP run the index step D and value step d satisfy A*D = d (mod M), exact for all 17 runs. |
| `ap_sum_check.py` | Earlier AP-run reconstruction attempt (had integer-division truncation bug) superseded by ap_verify2.py/ap_fix.py. |
| `ap_verify.py` | _(undescribed)_ |
| `ap_verify2.py` | Recomputes the PE700 answer V by summing each AP run with the exact AP formula over the 102 coins. |
| `brute.txt` | _(undescribed)_ |
| `check_floor_sum.txt` | _(undescribed)_ |
| `commands.log` | _(undescribed)_ |
| `direct_sum.py` | Direct sum of the 102 Eulercoin values = 1517926517777556, matching the documented answer. |
| `euclid_check.py` | _(undescribed)_ |
| `euclid_ladder.md` | Pattern-finder finding: the 102 Eulercoin values are exactly reconstructed from the Euclidean remainders of (M,A) — odd-indexed remainders are run-start values, even-indexed are AP steps, quotient = run length; recomputes V=1517926517777556 independently. |
| `eulercoins.py` | _(undescribed)_ |
| `run_structure.py` | _(undescribed)_ |
| `runs.py` | _(undescribed)_ |
| `solution.note.md` | Claim note beside the computed solution output: records the final answer (sum=1517926517777556, 102 Eulercoins) with status checked, and how it was cross-verified against brute force; promotes the computed result into research/CLAIMS.md as eu700-final-answer. |
| `solution.txt` | _(undescribed)_ |
| `structure_check.py` | _(undescribed)_ |
| `sum_runs.py` | _(undescribed)_ |
| `verify_recurrence.txt` | _(undescribed)_ |
| `verify_scan.py` | _(undescribed)_ |
