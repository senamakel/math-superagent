# Index — code/modular

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `modA.py` | Initial (slow) attempt at factorization + Pisano period; timed out because it used direct iteration over a prime ~10^8. Superseded by modA_fast.py. |
| `modA_fast.py` | TASK A: computes modular structure of M=101001001 (prime; ord_10=50500500, Pisano period=101001000) via fast divisor-reduction, verified two ways. Writes code/out/mod_A.txt. |
| `modB.py` | TASK B: r(k)=Psi(k) mod M for k=1..150 and search for small eventual period; none <=75 found (negative result). Writes code/out/mod_B.txt. |
| `modC.py` | TASK C: factor table k=1..12 and N(i;k) k=1..40; falsifies N=floor((k-i)a+c). Writes code/out/mod_C.txt. |
| `modC_ones.py` | Exact ones-total T(k)=(k+1)*floor(ka)+r_k over k<=40, r_k table. Writes code/out/mod_C_ones.txt. |
| `modC_struct.py` | Verifies N(i;k) balanced in i and constant F_{m-2} at k=F_m-1; falsifies the position-Beatty candidate. Writes code/out/mod_C_struct.txt. |
