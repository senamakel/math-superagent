# Index — code/out/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | placeholder |
| `REJECTED_uc_with_three_set.md` | Documents the deletion of the bogus code_refute_uc_with_three_set.p.json artifact: explains the TPTP slot-collapse encoding bug, the exact-oracle verification (all UC families with a 3-set on n<=4 have an abundant element), and the future gate requiring oracle re-check of any model-finder refutation. |
| `_run_check.py` | Shell wrapper that runs check_three_set_model.py from /workspace. Companion to that checker; kept for provenance of the rejection of the bogus refuted artifact. |
| `check_three_set_model.py` | Machine decode of the counter-model from code_refute_uc_with_three_set.p.json run through the canonical oracle code/lib/uc.py; confirms it is union-closed with an abundant element, so not a counterexample. |
| `code_refute_uc_with_three_set.p.json` | Replaced verdict: records the original 'refuted' as an encoding bug not a refutation; now carries corrected_assessment and oracle check conclusion. Not evidence. |
| `three_set_model_verdict.md` | Records that the TPTP 'refuted' verdict on the with-three-set rung was a first-order encoding bug (missing pairwise-distinct slots), not a refutation; rung stays open. |
