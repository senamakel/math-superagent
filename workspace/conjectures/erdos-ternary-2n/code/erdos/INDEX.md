# Index — code/erdos

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `__init__.py` | Package init for code/erdos, re-exporting digit_free, sieve_count, finite_check, direct_count, lift_count, to_base3 from oracle.py. |
| `dh_classifier.py` | _(undescribed)_ |
| `dr_surjectivity.py` | Settles the adopted cross-modulus route: proves Dr(q)=F_q (digit-{0,1} ternary integers are surjective mod every q coprime to 3, via S_t = sum_{j<t} 3^{j*ord_q(3)} == t), verifies it by construction for all 197 q in [5,300] coprime to 3 plus 257/641/1021 for every residue, and shows the corrected mod-q consistency (b') is vacuous so mixed_count == pure == 2^(k-1) on the (q,k) grid (q in {5,7,11,13,17,19,29,41,193,257}, k in 1..9, cap lcm <= 3e5) — hypothesis H1 of CROSS-MODULUS-BEATS-SIEVE-HYPOTHESES REFUTED. Correctness: reproduces digit_free witnesses (0,2,8 True; 5 False, 1012_3), matches brute-force oracle for k=1,2,3, verified every residue of every q. |
| `oracle.py` | Exact float-free Erdős oracle: digit_free(n) (base-3 of 2**n avoids 2, exact arithmetic), sieve_count(k)= |
