# Index — code/elementary

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `elementary_rungs.py` | Settles the two weakest provable Catalan-ladder rungs (R-trivial-bases: x=1 or y=1 impossible — proved via two-line case split; R-p-eq-q: x^p-y^p=1 has no solution — proved via (x-y)(sum)=1 factorisation) and re-verifies R-fixed-23 (x^2-y^3=1: only (3,2) with y>0) numerically to x=10^7. Exact integer only. Correctness established by: (a) the proofs are one-line and independent of the machine; (b) each is cross-checked against the exact oracle solutions(10^8)=[(3,2,2,3)] and fresh brute-force searches (0 hits over primes<=19,x<3000 for p-eq-q; integer cube-root search to 1e7 for fixed-23). Output: code/out/elementary_rungs.captured.txt; note+claims: code/out/elementary_rungs.note.md. |
