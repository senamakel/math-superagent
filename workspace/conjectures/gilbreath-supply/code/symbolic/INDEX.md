# Index — code/symbolic

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `sphere_mean_sympy.py` | Independent sympy (non-enumeration) evaluation of the sphere-mean closed form E_Sw[nu2] = sum_d (1/2)(1 - K_w(2^popcount(d))/C(n,w)), plus the full n=8 w-sweep. Reproduces the exact integers from sphere_mean_verify.py (n=4,w=1 -> 3/2; n=8,w=3 -> 25/7), and shows the task-stated '6.846' is impossible (nu2 <= 6 at n=8). |
| `sphere_mean_verify.py` | Brute-force oracle for the sphere-mean Krawtchouk formula: enumerates S_w, computes nu2 via the literal submask-XOR fold, and checks E_Sw[nu2] = sum_d (1/2)(1 - K_w(2^popcount(d))/C(n,w)) exactly for every (n,w), n=3..16. Establishes the closed form in research/notes/linear_supply_threshold_krawtchouk.md (claim sphere-mean-krawtchouk-exact). |
| `sphere_mean_verify2.py` | Second verification route for the sphere-mean Krawtchouk lemma: (a) the Krawtchouk evaluation sum_{h in S_w}(-1)^{h.1_A} = K_w(m;n) by brute force (n<=10, all w, m); (b) the per-cell parity count #{h: xor over A = 1} = (C(n,w)-K_w(m;n))/2 (random subsets); (c) the finite-n asymptotics K_w(m;n)/C(n,w) -> (1-2alpha)^m. All PASS. |
