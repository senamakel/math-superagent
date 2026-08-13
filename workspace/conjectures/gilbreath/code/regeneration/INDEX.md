# Index — code/regeneration

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_regenerate_lemma.py` | Exact checker of the regeneration lemma against real prime rows (sieve 20M, depth 1000, one row at a time). Proves the corrected iff holds with 0 failures across all 998 transitions; the literal task indexing is shown to fail. Oracle-verified against witnesses.json first-40 rows. |
