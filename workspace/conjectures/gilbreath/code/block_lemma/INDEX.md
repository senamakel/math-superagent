# Index — code/block_lemma

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_real.py` | Checks the block-lemma guarantee and the regeneration margin against the real prime rows (depth 600) rebuilt from the generator. |
| `explore_shape.py` | Computes the exact apex (Sierpinski/binomial-XOR) of the {0,2} block subtriangle and the self-preservation distribution over all 2^n block patterns; shows the worst-case minimum is exactly n+1 rows while the extra rows past k+n come from the boundary, not the block pattern. |
| `verify_constant.py` | Exhaustive/adversarial brute-force verification of Odlyzko's block lemma constant (n+1 rows) over all 2^n block patterns with adversarial even completions, n=1..8. Confirms exactly n+1 leading-1 rows and first-escape offset n. |
| `verify_diagonal.py` | Independent brute-force check that the diagonal-subtriangle positions 1..n-d in row k+d stay in {0,2} for all 2^n block patterns with adversarial tails, n=1..11 (122820 pairs, zero violations); confirms the exact n+1 guarantee and sharpness. |
| `worstcase_pattern.py` | Identifies exactly which block patterns achieve the minimum self-preservation depth n+1 (the all-constant block, exactly one of 2^n) under an adversarial tail. |
