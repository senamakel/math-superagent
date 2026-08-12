# Numericana — Hemiperfect numbers of abundancy 11/2 (Michon & Marcus)

Source: http://www.numericana.com/data/hpn11.htm — `[[numericana_hpn11.full]]`
(G. P. Michon & M. Marcus; cited by OEIS A159271 and by Wikipedia hemiperfect.)

## What it is

A table of 117 hemiperfect numbers with abundancy sigma(n)/n = 11/2 (OEIS A159271),
each with its prime factorization (2^a 3^b 5^c ...). Dated June 2010; "the authors do not
(yet) claim that all integers of abundancy 11/2 are listed."

## The two members below 10^18 (directly load-bearing for THIS problem)

- **1:** 17116004505600 = 2^11 3^4 5^2 7^2 11 13 19 31  (~1.71e13)
- **2:** 75462255348480000 = 2^11 3^4 5^4 7^3 11^2 13 19 71  (~7.55e16)

Both are < 10^18. The third member, 6219051710415667200 (~6.2e18), already exceeds 10^18.
So the abundancy-11/2 branch of the DFS **must return exactly these two values** below
10^18 — an independent, primary-source cross-check of the 11/2 branch, consistent with
A159271's term list (17116004505600, 75462255348480000, 6219051710415667200, ...).

The 2-adic structure is visible: both have 2^11 (a=11) and, per the run's
v2(sigma(u)) = a−1 identity, the odd part u must satisfy v2(sigma(u)) = 10.

## What it lets this run do

- Independent verification oracle for the 11/2 target branch of `hemiperfect_dfs.py`
  (two expected values ≤ 1e18: 17116004505600, 75462255348480000).
- Corroborates the A088912/A141643 record that the least 11/2 number is
  17116004505600 = a(5) from A088912.

## Does not settle

Table is explicitly not claimed complete for 11/2, and it covers only abundancy 11/2 —
the other targets (3/2..9/2) still need their own sources (A088912/A141643/A055153/
A141645 already held) and the full ≤10^18 qualifying union + sum is the run's
computation. The 117-term table (mostly ≫ 1e18) is background; the two small terms are
the operative ones.

```claim
id: hpn11-two-below-1e18
statement: The abundancy-11/2 hemiperfects below 1e18 are exactly 17116004505600 and 75462255348480000 (the first two members of A159271 / Michon-Marcus's hpn11 table; the third member ~6.2e18 exceeds the bound).
hypotheses: Michon-Marcus hpn11 table has no missing member below 1e18 (term 3 is the first exceeding 1e18 in the table; table is large and A159271 matches)
holds-here: yes
status: sourced (Numericana hpn11 + OEIS A159271)
bearing: independent oracle for the DFS 11/2 branch: it must output exactly these two values
anchor: research/sources/numericana_hpn11.full.md
```
