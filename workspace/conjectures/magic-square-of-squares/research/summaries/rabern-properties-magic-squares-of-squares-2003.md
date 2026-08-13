# Rabern, "Properties of Magic Squares of Squares", RHUMJ 4(1) Art. 3, 2003

[[rabern-properties-magic-squares-of-squares-2003]]

Source: Landon W. Rabern, "Properties of Magic Squares of Squares," Rose-Hulman
Undergraduate Mathematics Journal 4(1), Article 3 (2003), Washington University
(faculty sponsor N. Mohan Kumar; written while the author was studying in the
Netherlands, July 2002).

**Full-text status: ON DISK as of this cycle.** The direct Rose-Hulman PDF
(`scholar.rose-hulman.edu/cgi/viewcontent.cgi?article=1299&context=rhumj`)
returns 403, and Academia.edu also 403s. The complete 4-page paper was
retrieved via the Wayback Machine snapshot of that exact viewcontent URL:
`https://web.archive.org/web/2023id_/https://scholar.rose-hulman.edu/cgi/viewcontent.cgi?article=1299&context=rhumj`,
now at `research/sources/rabern-properties-magic-squares-of-squares-2003.full.md`
(10.7 KB, full text with all five theorems and proofs). The landing page
(`rhumj/vol4/iss1/3/`) is abstract-only. The old claim
`rabern-fulltext-not-on-disk` is now **false** and must not be re-quoted.

## What the paper establishes (all proofs on disk)

Assuming a 3×3 MSS of distinct squares exists (entries `a² b² c² / d² e² f² /
g² h² s²`, magic number `M = 3e²` after Gardner):

- **Theorem 1.1**: All nine entries are odd. (Parity analysis of the line sums.)
- **Theorem 1.2**: The only prime divisors of the centre `e` are `p ≡ 1 (mod 4)`.
  (UFD in Z[i]: from `a²+s² = 2e²`.)
- **Theorem 1.3**: If a prime `p ≡ 3, 5 (mod 8)` divides a non-centre entry
  then `p` also divides the centre and the opposite entry on that line.
  (UFD in Z[√2].)
- **Corollary 1.1**: No prime `p ≡ 3 (mod 8)` divides any entry.
- **Theorem 1.4**: No prime `p ≡ 5 (mod 8)` divides a middle-side entry.
- **Theorem 1.5**: If a prime `p ≡ 3 (mod 4)` divides a corner entry then it
  divides the two middle-side entries not adjacent to that corner.

These match this run's checked/proved claims `primitive-mss-entry-congruences`
(all nine entries odd and ≡1 mod 3, no 3 mod 8 factor anywhere, no 5 mod 8
factor on middle-side entries, centre 1-mod-4-only) and
`primitive-mss-modular-124-72` (all entries ≡1 mod 24, magic sum ≡3 mod 72),
and are independently re-proved with elementary methods by Morgenstern 2015
(`morgenstern-properties-3x3-square-of-squares-2007`). Rabern's are necessary
conditions on a hypothetical MSS: they sieve searches but neither prove nor
refute existence, and the extension-field MSS (`extension-field-mss-exist`)
satisfy the same restrictions where defined.

## Claim block

```claim
id: rabern-entry-prime-restrictions
statement: Assuming a 3×3 MSS of distinct squares exists: all nine entries are
  odd (Thm 1.1); primes dividing the centre e are all p ≡ 1 mod 4 (Thm 1.2);
  p ≡ 3,5 mod 8 dividing a non-centre entry forces p to divide the centre and
  the opposite entry on that line (Thm 1.3); no p ≡ 3 mod 8 divides any entry
  (Cor 1.1); no p ≡ 5 mod 8 divides a middle-side entry (Thm 1.4); p ≡ 3 mod 4
  dividing a corner divides the two non-adjacent middle-side entries (Thm 1.5).
hypotheses: a 3x3 MSS of distinct positive integer squares exists (conditional
  statement)
holds-here: yes (necessary conditions; superseded as search sieves by the run's
  proved congruences)
status: proved-where-stated; full primary text now on disk and read
bearing: entry-level modular sieve; cannot prove non-existence (extension-field
  MSS satisfy them); matches primitive-mss-entry-congruences /
  primitive-mss-modular-124-72
anchor: research/summaries/rabern-properties-magic-squares-of-squares-2003.md
```

```claim
id: rabern-fulltext-on-disk
statement: The full text of Rabern's 2003 RHUMJ paper (5 theorems, all proofs)
  is in the library at research/sources/rabern-properties-magic-squares-of-
  squares-2003.full.md, retrieved through the Wayback Machine after direct
  Rose-Hulman and Academia.edu fetches returned 403.
hypotheses: —
holds-here: yes
status: checked (10.7 KB full text read; theorems extracted)
bearing: upgrades rabern-entry-prime-restrictions from asserted to
  proved-where-stated
anchor: research/summaries/rabern-properties-magic-squares-of-squares-2003.md
```