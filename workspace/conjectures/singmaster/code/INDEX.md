# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for Singmaster's conjecture. `occurrences(a, n_max)` enumerates all (n,k) with 0<=k<=n<=n_max and C(n,k)==a by direct exact integer comb evaluation; `multiplicity(a,n_max)` counts them. Convention: counts both mirrored occurrences and the trivial pair C(a,1)=C(a,a-1). Exact arithmetic (math.comb), O(n_max^2). Verified: reproduces N(3003)=8 and N(120)=N(210)=N(1540)=N(7140)=N(11628)=N(24310)=6, matching code/out/witnesses.json, and confirms 3003=C(3003,1)=C(78,2)=C(15,5)=C(14,6) with its four mirrors. |
| `count_multiplicity.py` | _(undescribed)_ |
| `librarian_check_families.py` | Independent exact recomputation of the infinite Fibonacci binomial family (C(n+1,m+1)=C(n,m+2)) and the six one-off binomial collisions listed in MRSTT Remark 1.4, to verify the catalogue the librarian recorded before trusting it. |
| `verify_family.py` | Finds equal binomial pairs: buckets C(n,k), 2<=k<=n/2, n<=1000, value<=1e18; prints every colliding value (all 7 witnesses reproduced); writes code/out/family_pairs.json; also enumerates the Pell family C(n+1,k+1)=C(n,k+2) (Singmaster 1975) with j=1..4, the infinite N>=6 family. |
| `verify_fibonacci_identity.py` | Exact-integer software check of Singmaster's infinite family C(n+1,m+1)=C(n,m+2) (Fibonacci Pell solutions) and that the common value occurs >=6 times, plus reproduction of N(3003)=8 and the seven Singmaster witnesses. (Source-check companion; numbers cross-checked against witnesses.json.) |
inst witnesses.json.) |
