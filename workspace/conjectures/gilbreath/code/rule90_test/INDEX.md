# Index — code/rule90_test

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `analyze_rule90_depth.py` | Tests the Rule 90 / powers-of-2 depth prediction against the real block-length record `code/out/blocks_depth1000.json`: finds local minima of the leading-{0,2} block length, computes regime depths, checks nearness to powers of two, and fans out 48 hypothesis variants with `code/lib/parallel.py`. Output: `code/out/rule90_depth_test.captured.txt`, `code/out/rule90_depth_results.json`. **Unverified correctness quality: comments claim the depth-prediction tests are refuted — do not re-assert the prediction.** |
| `null_rule90_depth.py` | Null distribution for the rule90 relative-depth hit rate. Loads the 27 genuine regime depths from code/out/rule90_depth_results.json; shows the permutation null is degenerate (the hit predicate tests depth values, not positions, so every shuffle has the same count); the honest null is the exact binomial Binomial(27, 9/16) giving P(X ≥ 21) = 0.017299 (exact Fraction tail, cross-checked by scipy.stats.binom.sf and a direct float sum, agreeing to 8 digits). Also tests tol=0 (10/27, p = 0.113) and the post-hoc [2,9] conditioning (p = 0.68). Establishes claim rule90-relative-depth-null and closes TASKS item 1 / thread rule90-regeneration. Correctness established by agreement of three independent p-value routes and reproduction of the observed hit count. |
