# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for the Erdős–Straus equation 4/n=1/x+1/y+1/z. solves(n,x,y,z) is exact-int cross-multiplication ground truth; naive_solve(n,cap) is a bounded brute-force ordered search (only for small n). main() reproduces every worked example in the statement: the even identity, the n≡3 (mod 4) family, n=1 having no solution, and all 12 witnesses in code/out/witnesses.json. It caught that the brief's typed n≡3 (mod 4) identity is wrong (it solves 3/n, not 4/n) and verified the corrected family x=(n+1)/4, y=n(n+1)/4+1, z=y(y-1) symbolically as 0 for n=4k+3. All PASS. |
| `oracle.py` | _(undescribed)_ |
| `verify_library_claims.py` | _(undescribed)_ |
