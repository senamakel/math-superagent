# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `digits.py` | Exact O(log10 n) place-value digit-count f(n,d) for Project Euler 156 — `f_place_value(n, d)`. Verified against the brute-force oracle: agrees with f_naive on the statement's f(n,1) table for n=0..12 (0,1,...,4,5), on f(22,2)=6, on every solution the oracle's 0..300000 scan reported, and with the brute-force running total for all n in 0..20000. This is the efficient counter the real solver will be checked against. |
