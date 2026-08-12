# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive strong-repunit oracle (PE346): literal per-n per-base repunit counting for bounds <= 1000 (reproduces worked examples: list below 50 = [1,7,13,15,21,31,40,43], sum below 1000 = 15864), plus a direct R_k(b) generator for large bounds. Both agree on every bound checked up to 1000; independent by-length route also confirms sum below 1e6 = 372810163. |
