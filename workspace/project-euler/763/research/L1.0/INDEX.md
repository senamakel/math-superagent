# Index — research/L1.0

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `oeis_a001006.md` | Motzkin numbers A001006 (g.f., D-finite recurrence, closed form). Establishes D(N) is NOT Motzkin — diverges at n=2 (2 vs 3). Kills the Motzkin closed-form candidate for D(N). |
| `oeis_a005207.md` | Fibonacci family (F(2n-1)+F(n+1))/2 = 1,1,2,4,9,21,... . Diverges from D(N) at n=2. Rules out a Fibonacci closed form for D(N). |
| `oeis_a007902.md` | OEIS A007902 (number of pebbling configurations with n pebbles): terms 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668,... are identical to the run's computed 2D amoeba sequence D_2D(N) — a live match worth pursuing, not yet read for its formula. |
| `oeis_a086246.md` | Motzkin variant (1+x-sqrt(1-2x-3x^2))/2 = 0,1,1,1,2,4,9,... . Not D(N). |
| `oeis_a168049.md` | Motzkin variant (3-x-sqrt(1-2x-3x^2))/2 = 1,0,1,1,2,4,9,... . Not D(N); "essentially A086246". |
| `oeis_direct.md` | Direct OEIS search of full 15-term D(N): "No results". Authoritative negative — D(N) not catalogued, no closed form to look up. |
| `oeis_partial.md` | Direct OEIS search of offset-1 11 terms: "No results". Confirms absence regardless of offset. |
