# Index — code/verify

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `linear_supply_independent.py` | Independent ground-truth verification of the linear-supply-by-weight characterisation: computes nu2(n)=wt(Phi_n h) by raw literal submask-XOR enumeration (no SOS transform), verifying e_{n-2} mechanism, n=8 witness, min-weight thresholds for n=10/14/16 (exhaustive), and the all-ones negative control. Captures to code/out/linear_supply_independent.txt. |
