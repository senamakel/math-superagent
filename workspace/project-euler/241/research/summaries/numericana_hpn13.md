# Numericana — Hemiperfect numbers of abundancy 13/2 (Michon & Marcus)

Source: http://www.numericana.com/data/hpn13.htm — `[[numericana_hpn13.full]]`
(G. P. Michon & M. Marcus; cited by OEIS A160678 and by Wikipedia hemiperfect.)

## What it is

A growing table (304 entries as of Dec 2010) of hemiperfect numbers with abundancy
sigma(n)/n = 13/2 (OEIS A160678), each with prime factorization. "Known to be complete
only up to the 45th term" — beyond that, entries are provisional (marked with ?).

## The load-bearing fact for THIS problem

**Term 1** = 170974031122008628879954060917200710847692800
= 2^23 3^9 5^2 7^5 11^5 13^2 17 19^3 31 37 43 61^2 97 181 241 ~ 1.71e44.

This is the globally smallest number with abundancy 13/2 — i.e. a(6) of A088912, the
k=6 case. Since 1.71e44 >> 10^18, **no n <= 10^18 has abundancy 13/2**, and the DFS
target k=6 contributes zero values below the bound. Third independent corroboration of
the reachability cutoff (with A088912 and A160678), now from the primary table with
explicit factorization. Also confirms the A160678 a(1) factorization.

The first term's 2-power is 2^23 (a=23), consistent with the 2-adic reduction.

## What it lets this run do

Gives primary-source closure on the k=6 target: the DFS may include 13/2 in its
target set harmlessly (it returns nothing below 1e18), and any claimed 13/2 result
below 1e18 would be a bug. No enumeration value below the bound.

## Does not settle

Table is explicitly incomplete beyond term 45 and all known terms are ≫ 1e18, so it
adds nothing to the enumeration; the run's sum across k=1..5 is still the computation.

```claim
id: hpn13-first-term-1e44
statement: The smallest number of abundancy 13/2 is 2^23 3^9 5^2 7^5 11^5 13^2 17 19^3 31 37 43 61^2 97 181 241 = 170974031122008628879954060917200710847692800 ~ 1.71e44 (term 1 of the Michon-Marcus hpn13 table = a(6) of A088912), confirming no n <= 10^18 has abundancy 13/2.
hypotheses: hpn13 table term 1 is globally least (matches A088912 a(6) and A160678 a(1), three independent catalogues)
holds-here: yes
status: sourced (Numericana hpn13 + A088912 + A160678)
bearing: closes the k=6 target: zero solutions below 1e18; harmlessly included in DFS
anchor: research/sources/numericana_hpn13.full.md
answers: theory-numbers-with-88d5
```