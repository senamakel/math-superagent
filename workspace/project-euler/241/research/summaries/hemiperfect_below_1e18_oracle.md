# Oracle: the 22 hemiperfect numbers ≤ 10^18, from OEIS b-files

Sources: A159907 b-file (`research/sources/A159907_bterm.full.md`), A141643 b-file
(`research/summaries/oeis_A141643_bfile.md`), A055153 b-file
(`research/summaries/A055153_bterm.md`), A141645 b-file
(`research/summaries/oeis_A141645_bfile.md`), A159271 b-file
(`research/sources/oeis_A159271_bfile.full.md`). All OEIS. This note classifies,
by abundancy, every A159907 term ≤ 10^18 and checks the four class sequences agree.

## The classification (exact integer comparison, done at write time)

A159907 terms 1..22 are all ≤ 10^18 and term 23 = 6219051710415667200 ≈ 6.22e18 > 1e18:
exactly 22 hemiperfects below the bound. Partition by abundancy:

- **3/2** (1): 2
- **5/2** (3): 24, 91963648, 10200236032
- **7/2** (9): 4320, 4680, 26208, 20427264, 197064960, 21857648640, 57575890944,
  88898072401645056, 301183421949935616
- **9/2** (7): 8910720, 17428320, 8583644160, 57629644800, 206166804480,
  1416963251404800, 15338300494970880  (A141645 a(8) = 6275163455171297280 ≈ 6.28e18 exceeds)
- **11/2** (2): 17116004505600, 75462255348480000  (A159271 a(3), a(4) exceed)

The union of the four class b-files restricted to ≤ 10^18 equals A159907[1..22]
exactly, so the two independent OEIS listings agree: **the answer set is these 22
values, and their sum is the PE241 answer** (sum to be computed and verified by the
solver, not asserted here).

## Completeness caveat (what this oracle does and does not prove)

OEIS listings are *known* members, not a proof that no others exist below 10^18.
Completeness comes from the other side of the library: the tree-search method —
Flammenkamp's exhaustive construction of all multiply-perfects < e^350
(`research/summaries/flammenkamp_multiply_perfect.md`) and Alekseyev's Theorem 3.3 /
Section 3.4 machinery for `aσ(n)=bn+c` (`research/sources/alekseyev_diophantine_sigma_html.full.md`)
— which is exactly what `code/hemiperfect_dfs.py` implements for (a,b,c)=(2,2k+1,0).
The solver must (a) reproduce these 22 values by the DFS at 10^18, and (b) sum them.

```claim
id: hemiperfect-22-below-1e18
statement: There are exactly 22 hemiperfect numbers n <= 10^18, namely A159907 terms 1..22, partitioned by abundancy as 3/2:{2}; 5/2:{24,91963648,10200236032}; 7/2:{4320,4680,26208,20427264,197064960,21857648640,57575890944,88898072401645056,301183421949935616}; 9/2:{8910720,17428320,8583644160,57629644800,206166804480,1416963251404800,15338300494970880}; 11/2:{17116004505600,75462255348480000}. The answer to PE241 is their sum.
hypotheses: A159907 and the four class b-files correctly list all known hemiperfects; completeness below 1e18 is established by the DFS (the solver's job), not by these listings alone
holds-here: yes (the two independent OEIS listings agree on all 22 values)
status: sourced from OEIS b-files; set-to-set agreement between A159907 and the class-sequence union; counting/membership done at write time by direct comparison
bearing: fixes the exact answer set the solver must reproduce; replaces the recalled-but-unverified "22 values" with a sourced list
anchor: research/summaries/hemiperfect_below_1e18_oracle.md
answers: theory-numbers-with-88d5
```