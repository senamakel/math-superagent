# Erdős Problems entry — powers of 2 with digits 0,1 in base 3

**Source:** https://www.erdosproblems.com/latex/406 — the standard problem-collection entry, cross-referenced in Guy's Unsolved Problems in Number Theory (Problem B33).

## What it records

- **Statement:** Is it true that only finitely many powers of 2 have only digits 0 and 1 in base 3? Known examples: 1 = 1, 4 = 1+3, 256 = 1+3+3^2+3^5.
- **Kummer's theorem link:** if we only allow digits 1 and 2, then 2^15 seems the largest such power; this would imply 3 | binomial(2^(k+1), 2^k) for all large k (the original motivation for Erdős's question, later proved by Sárközy/Granville–Ramaré/Velammal by other means).
- **Counting function:** N(x) = #{n ≤ x : 2^n has only digits 0,1 in base 3}, and Narkiewicz proved N(x) ≤ 1.62 x^(log_3 2).
- **Generalizations** and literature pointers: Abram–Lagarias (J. Fractal Geom. 2014) on intersections of multiplicative translates of 3-adic Cantor sets; Lagarias (2009); Guy B33.

## Claims
```claim
id: EP-406
statement: The Erdős problem (only finitely many 2^n with base-3 digits only 0,1) is open; known solutions exactly {2^0, 2^2, 2^8}; N(x) ≤ 1.62 x^(log_3 2) (Narkiewicz).
hypotheses: none.
holds-here: yes — problem statement and counting-function bound as recorded in the standard collection.
status: asserted-by-source (standard reference)
bearing: fixes the statement and the count-bound citation for every note.
anchor: research/sources/erdos-problems-b33.md
```