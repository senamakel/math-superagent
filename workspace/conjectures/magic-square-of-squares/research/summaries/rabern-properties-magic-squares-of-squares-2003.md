# Rabern, "Properties of Magic Squares of Squares", Rose-Hulman Undergrad. Math. J. 4 (2003) Iss. 1, Art. 3

[[rabern-properties-magic-squares-of-squares-2003]]
Source: https://scholar.rose-hulman.edu/rhumj/vol4/iss1/3/ (landing page captured; full PDF at https://scholar.rose-hulman.edu/cgi/viewcontent.cgi?article=1299&context=rhumj returned 403 to the download tool).

**Status: abstract + bibliographic page captured; full text NOT on disk (403).** The mathematics is, however, fully recovered independently: Morgenstern's `morgenstern-properties-3x3-square-of-squares-2007` ("3x3 Magic Square of Squares Properties", July 2015) was explicitly written to re-derive *all* of Rabern's properties from elementary AP theory (it opens by saying exactly that), and that source is on disk. So the claims below are known from the abstract plus the Morgenstern re-derivation, and are recorded as the established (asserted/proved) content.

## What it establishes (from the abstract; congruences re-derived in morgenstern-2007)

Assuming a 3×3 MSS of distinct squares exists, using **unique factorization in two finite extensions of Z** (Gaussian integers `Z[i]` and `Z[√2]`):
- **Theorem 1.1:** all nine entries are **odd**.
- **Theorem 1.2:** every prime divisor of the central parameter `e` is `p ≡ 1 (mod 4)` (Gaussian-integer proof: no `p≡3 mod 4` divides `e`).
- **Theorem 1.3/1.5:** primes in certain classes (e.g. `p ≡ 3 or 5 mod 8`) dividing non-center or corner entries impose strong divisibility forcing the prime across multiple entries; some classes are excluded outright.
- **Theorem 1.4:** no prime `p ≡ 5 (mod 8)` divides a **middle-side** entry (proof via `Z[√2]`).

These are exactly the congruences the run already holds as `primitive-mss-entry-congruences` (proved in `morgenstern-properties-3x3-square-of-squares-2007`), so nothing new is added beyond a second, independent algebraic-number-theory route to the same conclusions.

## Implications for this run
- Independent confirmation (different proof technique) that the entry-level sieve `primitive-mss-entry-congruences` is correct in the near-miss range: any MSS that fails "all odd / all `1 mod 3` / no `3 mod 8` factor / no `5 mod 8` on middle side / centre `1 mod 4`-only" is impossible. The witness grids must (and do) satisfy these, so they are safe as lemmas, not refuted by near-misses.
- The method (UFD in `Z[i]`, `Z[√2]`) is the same ring-theoretic tool the run's `gaussian-integer-factorisations` approach uses — corroborating that line.
- **What could not be obtained:** the full text. The exact statement of the "force across multiple entries" theorems and any result not covered by Morgenstern's elementary re-derivation are not locally verifiable.

```claim
id: rabern-entry-prime-restrictions
statement: Assuming a 3×3 MSS of distinct squares exists, all entries are odd; the only primes dividing the central parameter e are p≡1 mod 4; no p≡5 mod 8 divides a middle-side entry; and primes in further classes (3 or 5 mod 8) dividing non-center or corner entries force divisibility across multiple entries or are excluded. Proven via unique factorization in Z[i] and Z[√2].
hypotheses: a 3×3 MSS of distinct squares exists (proving necessary conditions conditionally)
holds-here: yes, as necessary conditions; they match the primitive-mss-entry-congruences the run already holds by elementary AP theory
status: asserted (full text not on disk; congruences independently re-derived in morgenstern-2007 which is on disk)
bearing: independent algebraic-number-theory confirmation of the entry sieve; corroborates the Gaussian-integer approach
anchor: research/sources/rabern-properties-magic-squares-of-squares-2003.full.md
```
