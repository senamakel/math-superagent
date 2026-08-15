# Index — code/primitive_div

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `crosscheck_order.py` | Independent second route: computes multiplicative order of x mod the candidate primitive divisor directly for 102 (p,x) samples (all = p, PASS) plus a check of the mirror primitive divisor on small (q,y). Output code/out/primitive_div_crosscheck.captured.txt. |
| `mirror_primitive_div.py` | Verifies the mirror (q-side) primitive divisor of Phi_q(-y)=(y^q+1)/(y+1) and the scope of the elementary/Cassels necessary conditions for x^p-y^q=1. Task A: per-q table (q in {3,5,7,11,13,17}, Ymax scaled 120..20) counting (q,y) with a primitive divisor s (s |
| `verify_primitive_div.py` | Driver verifying Lucas identities, gcd lemma, Zsigmondy primitive-divisor existence, the p=2 exception, and the Cassels/Wieferich condition scope; writes code/out/primitive_div.md and .captured.txt. All sections PASS (exact sympy/int, no floats). |
