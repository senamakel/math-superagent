# Numericana — Hemiperfect numbers of abundancy 15/2 (Michon & Marcus)

Source: http://www.numericana.com/data/hpn15.htm — `[[numericana_hpn15.full]]`
(G. P. Michon & M. Marcus; cited by OEIS A160678 and Wikipedia hemiperfect.)

## What it is

A large table (hundreds of entries; 172k chars) of hemiperfect numbers with abundancy
sigma(n)/n = 15/2, each with prime factorization. This is the k=7 case of the problem
(k+1/2 = 15/2).

## Relevance to THIS problem: boundary only

Abundancy 15/2 = k+1/2 with k=7. The smallest known 15/2 hemiperfect is ~1.27e88
(Marcus's bound, per A088912 / Numericana main page), enormously above 10^18. Since
even the least 13/2 number is ~1.71e44 >> 1e18, and 15/2 ≫ 13/2, **no n <= 10^18 has
abundancy 15/2** — the k=7 target contributes zero values. This table adds no
load-bearing term for the sum; it confirms the cutoff direction from yet another
abundancy.

## Does not settle

No terms below 1e18; nothing for the enumeration. Kept in the library for coverage of
the full hemiperfect data tier and as the source that the Numericana main page and
A088912 cite for the 15/2 smallest-value claim. The Marcus bound of ~1.27e88 is stated
in A088912's comments; this table holds the factorizations behind it.

## Bearing

Corroborates (weakly, from beyond the cutoff) that only k ≤ 5 half-integer abundancies
occur below 1e18. Purely confirmatory; no new claim needed beyond
`a088912-abundancy-threshold` / `a160678-reachability-13over2`.