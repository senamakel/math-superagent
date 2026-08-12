# A159271 b-file — the abundancy-11/2 members

**Source:** https://oeis.org/A159271/b159271.txt — `[[oeis_A159271_bfile.full]]`
(Michel Marcus, 87 terms).

## Terms ≤ 10^18

Only the first two terms are below the bound: **17116004505600** and **75462255348480000**
(matching the Numericana hpn11 table, claim `hpn11-two-below-1e18`, and A159271's own page
whose first two terms are these). a(3) = 6219051710415667200 ≈ 6.2e18 exceeds 10^18.

These are exactly the two 11/2-branch outputs the DFS must return below 1e18, and
A159271∩A159907[1..22] confirms they are hemiperfect terms 17 and 20 of A159907.

## Cross-check with the oracle

The two terms appear as A159907 terms 17 (17116004505600) and 20 (75462255348480000),
consistent with `hemiperfect-22-below-1e18`. No A159271 term ≤ 1e18 is missing from the
union; the class-union equality in the oracle note holds for 11/2 too.

No separate claim — covered by `hpn11-two-below-1e18` and `hemiperfect-22-below-1e18`.
Do not re-read.
