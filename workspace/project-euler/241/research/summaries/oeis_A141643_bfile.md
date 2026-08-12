# A141643 b-file — the abundancy-5/2 members (3 of them, all ≤ 10^18)

**Source:** https://oeis.org/A141643/b141643.txt — `[[oeis_A141643_bfile.full]]`
(3 terms; the A141643 page's b-file).

## Terms

All 3 known 5/2-members: **24, 91963648, 10200236032**. All are ≤ 10^18. The page
note says a(4) > 10^100 if it exists (Alekseyev, Jun 2025) and no more terms below
10^12; the sequence is exhaustive of known 5/2 numbers.

## Relation to the oracle

These are exactly A159907 terms 2, 9, 12 (the 5/2 hemiperfects), confirming the
`hemiperfect-22-below-1e18` partition's 5/2:{24,91963648,10200236032}. The 5/2 branch
of the DFS must return exactly these three values ≤ 1e18.

```claim
id: a141643-three-5over2
statement: The 5/2-abundancy hemiperfects below 1e18 are exactly 24, 91963648, 10200236032 (A141643, class b-file); no other 5/2 number is known (a(4) > 1e100 if it exists).
hypotheses: A141643 lists all known 5/2 numbers; completeness below 1e18 is the solver's DFS proof, not this listing alone
holds-here: yes
status: sourced (OEIS A141643 b-file)
bearing: per-target oracle for the 5/2 DFS branch: must output exactly {24,91963648,10200236032}
anchor: research/summaries/oeis_A141643_bfile.md
```
