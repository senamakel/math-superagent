# Abundant number / abundancy index (Wikipedia; encyclopedic entry)

**Source:** https://en.wikipedia.org/wiki/Abundancy_index — this URL **redirects to
"Abundant number"** (the fetched article is "Abundant number", oldid 1363371058,
retrieved 2026). Full text: `research/sources/wikipedia_abundancy_index.full.md`.

## What it fixes (terminology)

- **Abundance** of n = σ(n) − 2n; n is **abundant** iff σ(n) > 2n, perfect iff
  σ(n) = 2n, deficient iff σ(n) < 2n.
- **Abundancy index** of n is the ratio σ(n)/n ("Related concepts" section). This
  is exactly the perfection quotient of PE 241. A number with higher abundancy
  index than all smaller numbers is **superabundant**; distinct n with the same
  abundancy index are **friendly numbers**.
- Article's own focus is abundant numbers (12 first abundant, abundance 4;
  smallest odd abundant 945), so most of the body is background, not the
  half-integer case.

## Facts in it that bear on the solve

- **Every multiple of an abundant number is abundant**, and every multiple of a
  perfect number (other than itself) is abundant: if 6 | n then
  σ(n) ≥ n/2 + n/3 + n/6 + 1 = n + 1. This is the same
  "multiplication raises or preserves abundance" monotonicity used by the
  solver's pruning (adding a prime power to n can only raise σ(n)/n).
- Density of abundant numbers is a nonzero constant in (0.2476171, 0.2476475)
  (Hall–Tenenbaum; Deléglise 1998) — context showing the abundancy-index
  > 2 threshold is common, while the half-integer values targeted by PE 241 are
  sparse (only 22 below 10^18).
- Convergent chain: every integer > 20161 is a sum of two abundant numbers.

## Relation to the rest of the library

The half-integer case (hemiperfect numbers, A159907) is covered in depth by
`research/summaries/hemiperfect_wikipedia.md` (source
`research/sources/hemiperfect_wikipedia.full.md`, the *Hemiperfect number*
article, which is the one that defines σ(n)/n = k/2 with k odd and lists the
sequence 2, 24, 4320, 4680, 26208, ...). This entry adds the abundancy-index
terminology and the multiple-of-abundant monotonicity; it does not change the
method. The Laatsch citation (Mathematics Magazine 59(2) 84–92, 1986) inside it
is already in the library (`research/summaries/laatsch_measuring_abundancy.md`).

```claim
id: abundancy-index-multiples-monotone
statement: The abundancy index I(n)=sigma(n)/n is the perfection quotient of PE241; every multiple of an abundant number is abundant (if 6|n then sigma(n) >= n+1), and the set of abundant numbers has natural density ~0.2476. Half-integer abundancy values are the hemiperfect numbers (A159907), the sparse objects the problem targets.
hypotheses: n a positive integer; abundancy index defined as sigma(n)/n
holds-here: yes — monotonicity under multiplication is part of why the residual quotient Q=T*n/sigma(n) only decreases as prime powers are added, the core pruning invariant of the DFS
status: encyclopedic (Wikipedia, "Abundant number"); density bound sourced to Hall–Tenenbaum and Deléglise 1998 within the article
bearing: fixes terminology and supports the Q<1 pruning rationale; background, not load-bearing for the final sum
anchor: research/summaries/wikipedia_abundancy_index.md
```