# Index — code/block_lemma

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_real.py` | Checks the block-lemma guarantee and the regeneration margin against the real prime rows (depth 600) rebuilt from the generator. |
| `explore_shape.py` | _(undescribed)_ |
| `verify_constant.py` | Exhaustive/adversarial brute-force verification of Odlyzko's block lemma constant (n+1 rows) over all 2^n block patterns with adversarial even completions, n=1..8. Confirms exactly n+1 leading-1 rows and first-escape offset n. |
| `verify_diagonal.py` | _(undescribed)_ |
| `worstcase_pattern.py` | Identifies exactly which block patterns achieve the minimum self-preservation depth n+1 (the all-constant block, exactly one of 2^n) under an adversarial tail. |
