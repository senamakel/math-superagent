# Rabern 2003 — Properties of Magic Squares of Squares

Source: Landon W. Rabern, "Properties of Magic Squares of Squares," Rose-Hulman
Undergraduate Mathematics Journal 4(1), Article 3 (2003), Washington University.
Index page (abstract + citation) downloaded:
`research/sources/rabern-properties-magic-squares-of-squares-2003.full.md`
(source URL https://scholar.rose-hulman.edu/rhumj/vol4/iss1/3).

**Full-text availability: the 4-page proof is NOT on disk.** The index page
(abstract, author bio, citation) was downloaded, but the full PDF at
https://scholar.rose-hulman.edu/cgi/viewcontent.cgi?article=1299&context=rhumj
returns HTTP 403 Forbidden (blocked download, recorded here so nobody repeats
the attempt). The claims below are therefore sourced via the abstract plus a
**secondary** account (the search-exposed body text and Morgenstern's
re-derivation), not proof-checked from the primary text.

## What the paper establishes (sourced via abstract + secondary echoes)

Assuming a 3×3 MSS of distinct squares exists, its entries have constrained
prime structure. Key results (corroborated independently by the library's
`morgenstern-properties-3x3-square-of-squares-2007.md` and CLAIMS.md
`rabern-entry-prime-restrictions`, `primitive-mss-entry-congruences`):

- **All nine entries are odd** (parity constraint derived from the magic
  constant and square residues).
- **No p ≡ 3 (mod 4) divides the centre e.** Proof via unique factorization
  in Z[i] (Gaussian integers): factorising `a²+s² = 2e²` in Z[i] as
  `(a+si)(a−si) = 2e²`; p ≡ 3 mod 4 is prime in Z[i]; then p|e forces p|a, p|s
  and (with the full structure) a descent/contradiction. Hence all prime
  factors of the centre are ≡ 1 mod 4 (or 2).
- **No p ≡ 3 or 5 (mod 8) prime divides a middle-side entry.** Proof via UFD in
  Z[√2]: for p ≡ 3,5 mod 8, p is prime in Z[√2]; from `d²+h²=2c²` derive
  divisibility of the middle-side entries. Classification: the primes that are
  prime in Z[√2] are exactly p ≡ 3,5 (mod 8) (Appendix lemma), giving these
  entry restrictions.

Thus central entry e is `1 mod 4`-only; middle-side entries have no
`5 mod 8` prime factors; no entry has a `3 mod 8` factor. These match the
run's `primitive-mss-entry-congruences` (all entries odd and ≡1 mod 3, etc.)
and `primitive-mss-modular-124-72` (all ≡1 mod 24, sum ≡3 mod 72), and Rabern's
`rabern-entry-prime-restrictions`.

## Caveat

These are **necessary conditions** on a hypothetical MSS — they sieve the
search; they do **not** establish or refute existence. The extension-field MSS
(`extension-field-mss-exist`) satisfy the same modular/prime restrictions where
defined, so no purely modular argument built on these (or the related
congruences) can prove non-existence over Q. Status of the claim blocks drawn
from this secondary sourcing: `rabern-entry-prime-restrictions` — **asserted**
(full primary text not on disk); the underlying congruences that this run has
independently verified are the stronger **proved/checked** claims
`primitive-mss-entry-congruences` and `primitive-mss-modular-124-72`.

## Claim block

```claim
id: rabern-fulltext-not-on-disk
statement: The full text of Rabern's 2003 RHUMJ paper is not in the library;
  the index/abstract page and secondary accounts are. Its entry-prime
  restrictions (all odd; centre 1-mod-4-only; no 3-mod-8 anywhere; no 5-mod-8
  on middle-side) are asserted via those secondary sources.
hypotheses: assumes a 3x3 MSS of distinct squares exists
holds-here: yes
status: asserted (primary full text not retrievable; 403 blocked)
bearing: the restrictions are superseded/confirmed by this run's checked
  congruences; do not cite Rabern's specific prime-distribution claims as
  proof-checked.
anchor: research/summaries/rabern-properties-magic-squares-of-squares-2003.md
```
