# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `commands.log` | _(undescribed)_ |
| `dump_factors_k40.txt` | Captured stdout of code/dump_factors.py: full printed table for k=1..40 (counts, Psi(k), Psi(k) mod 101001001, ones-count multiset, per-position one-counts), plus the N(i;k) rows k=8..15. Includes count==k+1 confirmation. |
| `factors_k40.json` | Data file: dict k (key as string "1".."40") -> sorted list of the k+1 distinct Fibonacci subwords of length k, produced by code/dump_factors.py. Source of the Psi(k), ones-counts, and per-position one-counts printed by that program. |
| `psi_brute_k1_30.txt` | _(undescribed)_ |
