# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive brute-force oracle for PE 591 BQA_d(pi,n): for each b in [-n,n] best a=round(x-b*sqrt(d)) with |
| `verify_big.py` | High-precision (mpmath, 60 digits) check of the d=2 n=10^13 candidate and the statement's upper bound candidate: |
| `verify_ostrowski.py` | Verification harness for the Ostrowski alpha-numeration best left/right approximation algorithm (Cabanillas-Lopez & Labbe Props 9/10) against a brute-force oracle on small inputs. Not run in this environment (no exec tool); kept for the solver agent to execute. |
