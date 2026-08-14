# Index — code

What each file in this folder is for. Keep it current: describe a file when you
create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Code-folder conventions and oracle/method/verification rules for this run. |
| `brute.py` | Naive oracle: enumerates all 3n²+3n+1 points of the order-n hexagon in axial coords {(a,b): |a|,|b|,|a+b| ≤ n}, counts hidden iff gcd(|a|,|b|) > 1 (origin excluded). O(n²); prints H(5)=30, H(10)=138, H(1000)=1177848 — the statement's oracles. |
| `solution.py` | PE351 exact solution: parity table for n=5,10,1000 (identity H=3n²+3n−6·Φ(n) vs embedded brute-force check), then computes Φ(10⁸) via lib.totient.sum_phi (int32 sieve, ~400 MB) and prints Φ(10⁸)=3039635516365908 and H(10⁸)=11762187201804552. |
| `verify_mobius.py` | Independent verification of Φ(10⁸): Möbius inversion Φ(N)=Σ μ(k)·T(⌊N/k⌋) with a separate int8 μ sieve (step p² for squarefree zeroing). Agrees exactly with lib.totient.sum_phi; shares only the prime list. |
| `lib/` | Reusable helpers. `lib/totient.py` = exact `sum_phi(N)` (incremental totient sieve, int32) and `H_hexagon(n, Φ_n)`; INDEX.md inside. |
| `out/` | Outputs and check programs: exact values (`pe351_values.md`), oracle-vs-catalogue (`check_library_values.py`), A063985 recursion route (`patterns.py`), mod-4 law checks, sequence dumps. See `out/INDEX.md`. |
