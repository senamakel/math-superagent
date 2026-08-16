# Index — code/supply_endpoint

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `endpoint_density.py` | Driver for the SUPPLY endpoint-comparison density study. Computes S(n), #(T=1), density of T=1 for real prime h (h_string) up to a ceiling (default 4000, each n), and for the negative controls h all-ones and all-zeroes at step sizes. Cross-checks the O(n log n) SOS path against the literal oracle for n<=200 and against nu2(n) (brute.py) up to 79 (agrees ±1). Writes code/out/supply_endpoint_density.txt. Established correct by oracle agreement and control separation. |
