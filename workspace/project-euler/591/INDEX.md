# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive brute-force oracle for PE 591 BQA_d(pi,n): for each b in [-n,n] best a=round(x-b*sqrt(d)) with |a|<=n; tracks min error, tie-break by smaller |a|. Reproduces all three statement examples; records d=2 n=1e7/1e8 and d=3 n=1e6 results. |
| `verify_big.py` | High-precision (mpmath, 60 digits) check of the d=2 n=10^13 candidate and the statement's upper bound candidate: |a+b*sqrt(2)-pi|; confirms both < 1e-13 where double precision was insufficient to resolve the gap. |
