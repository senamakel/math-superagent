# Index — code/phi_triple_variety

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `side_census_par.py` | Parallel, checkpointed COMPLETE side census: for all pairs q1>q2 in Phi(M) with q1+q2<1, counts how often 1-(q1+q2) and 1+(q1+q2) are rational squares and whether both ever hold. Same exact predicate as side_census.py (gcd-reduced fraction square test) but exact-sorted (cross-multiplication) and spread over a 28-core Pool in chunks, resumable via JSONL checkpoint. Correctness: exact agreement with serial side_census.py at M=100 (614165 pairs, 46/5/0) and M=200 (9856010 pairs, 132/24/0). Full run: M=800 complete, 2,509,516,913 pairs, minus=718 plus=150 both=0; checkpoint totals match printed RESULT; example witnesses independently re-verified via lib.phi.in_phi and exact side re-check. |
