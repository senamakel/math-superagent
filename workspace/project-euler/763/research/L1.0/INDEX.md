# Index — research/L1.0

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `oeis_a001006.md` | Motzkin numbers A001006 (g.f., D-finite recurrence, closed form). Establishes D(N) is NOT Motzkin — diverges at n=2 (2 vs 3). Kills the Motzkin closed-form candidate for D(N). |
| `oeis_a005207.md` | Fibonacci family (F(2n-1)+F(n+1))/2 = 1,1,2,4,9,21,... . Diverges from D(N) at n=2. Rules out a Fibonacci closed form for D(N). |
| `oeis_a007902.md` | A007902 (pebbling configurations) = the run's 2D amoeba sequence D_2D(N), matched on every published term (D_2D(N)=A007902(N+1)). Names the 2D analogue; has no closed form, only asymptotic (~2.32^n) and a memoized G(k,m) recurrence. Not the 3D D(N). Claim d2d-equals-a007902. |
| `oeis_a055999.md` | _(undescribed)_ |
| `oeis_a074171.md` | _(undescribed)_ |
| `oeis_a086246.md` | Motzkin variant (1+x-sqrt(1-2x-3x^2))/2 = 0,1,1,1,2,4,9,... . Not D(N). |
| `oeis_a134227.md` | OEIS A134227 ((n-1)(n+6)/2 + [n=1], "essentially A055999", row sums of triangle A134226) lookup note. Sibling of A055999/A074171, all giving the same n(n+7)/2 family; the run's Q_2(N)=(N-5)(N+2)/2 max-level-column identification uses A055999. Source https://oeis.org/A134227. |
| `oeis_a168049.md` | Motzkin variant (3-x-sqrt(1-2x-3x^2))/2 = 1,0,1,1,2,4,9,... . Not D(N); "essentially A086246". |
| `oeis_direct.md` | Direct OEIS search of full 15-term D(N): "No results". Authoritative negative — D(N) not catalogued, no closed form to look up. |
| `oeis_partial.md` | Direct OEIS search of offset-1 11 terms: "No results". Confirms absence regardless of offset. |
