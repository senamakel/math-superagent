# Numericana — Hemiperfect numbers of abundancy 17/2 (Michon & Marcus)

Source: http://www.numericana.com/data/hpn17.htm — `[[numericana_hpn17.full]]`
(G. P. Michon & M. Marcus; cited by OEIS A160678 and Wikipedia hemiperfect.)

## What it is

A table of hemiperfect numbers with abundancy sigma(n)/n = 17/2 (the k=8 case of the
problem), each with prime factorization. "Some Integers n of Abundancy 17/2" — an
incomplete list of known members.

## Relevance to THIS problem: boundary only

Abundancy 17/2 = k+1/2 with k=8. The smallest known 17/2 hemiperfect is ~2.72e190
(Marcus, per A088912 / Numericana main page), far above 10^18. Combined with the
13/2 cutoff (~1.71e44), **no n <= 10^18 has abundancy >= 13/2**: k >= 6 contributes
zero values. This table again confirms the cutoff direction from beyond the bound.

## Does not settle

No terms below 1e18; nothing for the enumeration. Coverage completes the Numericana
hemiperfect data tier (hpn11, hpn13, hpn15, hpn17 all on disk now), matching what the
frontier's top rows cited. Bearing is confirmatory only; no new claim.

## Complete state of the hemiperfect data tier (all downloaded this run)

- hpn11 (11/2): the two ≤1e18 members (17116004505600, 75462255348480000) — the
  load-bearing oracle for the DFS 11/2 branch (`hpn11-two-below-1e18`).
- hpn13 (13/2): term 1 ~1.71e44 = a(6), closes k=6 (`hpn13-first-term-1e44`).
- hpn15 (15/2), hpn17 (17/2): k=7,8; all ≫ 1e18, confirmatory only.