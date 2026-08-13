# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for Singmaster's conjecture. `occurrences(a, n_max)` enumerates all (n,k) with 0<=k<=n<=n_max and C(n,k)==a by direct exact integer comb evaluation; `multiplicity(a,n_max)` counts them. Convention: counts both mirrored occurrences and the trivial pair C(a,1)=C(a,a-1). Exact arithmetic (math.comb), O(n_max^2). Verified: reproduces N(3003)=8 and N(120)=N(210)=N(1540)=N(7140)=N(11628)=N(24310)=6, matching code/out/witnesses.json, and confirms 3003=C(3003,1)=C(78,2)=C(15,5)=C(14,6) with its four mirrors. |
