# Index — code/regeneration

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_regenerate_lemma.py` | Exact checker of the regeneration lemma against real prime rows (sieve 20M, depth 1000, one row at a time). Proves the corrected iff holds with 0 failures across all 998 transitions; the literal task indexing is shown to fail. Oracle-verified against witnesses.json first-40 rows. |
| `step_law_independent.py` | Independent second route (pure-Python rows_generator, fresh sieve 2e6, depth 300) re-verifying the step law, drain law, recharge identity, and the sharpness constructions (1,2,4)->b>=1 vs (1,0,4)/(1,2,6)->b=0. Zero failures; captured in code/out/step_law_independent.captured.txt. |
| `step_law_theorem.py` | Proves + verifies the local step law of the leading {0,2} block: b_{k+1} >= b_k iff (edge, intruder) = (2,4), else b_{k+1} = b_k - 1; drain law; recharge identity. Verified on real prime rows depth 1000 (sieve 2e7) and 400 random general-class arrays, zero failures (captured in code/out/step_law_captured.txt). |
