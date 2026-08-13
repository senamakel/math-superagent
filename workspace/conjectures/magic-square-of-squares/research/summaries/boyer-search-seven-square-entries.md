# Boyer 2004 — A search for 3×3 magic squares having more than six square integers

Source: Christian Boyer, "A search for 3x3 magic squares having more than six
square integers among their nine distinct integers," Draft v2, 16 September
2004, http://www.multimagie.com/Search.pdf. Full text:
`research/sources/boyer-search-seven-square-entries.full.md`.

Primary source that fixes the **seven-square configuration taxonomy**, the
**Buell 25×10²⁴ bound** and its exact scope, and Boyer's own (negative) searches.
This is the paper the run kept citing through secondary sources; it is now the
authority on disk.

## What it establishes

**Statement of the problem (B).** Nine distinct positive integers, squares in a
3×3 grid, all three rows, columns and both diagonals sum to M. Martin Gardner's
$100 challenge (LaBar 1984; Gardner 1996: "if it exists, its numbers are sure to
be monstrously large"). Open in 2004 (and remains open).

**Sallows/Schweitzer near-miss (problem A — squared square, 7 of 8 sums):**
```
127² 46² 58²
 2² 113² 94²
74² 82² 97²
```
all rows/columns and one diagonal = 147² = 21609, the other diagonal fails
(38307). First found independently by Lee Sallows and Michael Schweitzer.

**Six-square configurations (Bremner 2001).** All sixteen configurations up to
symmetry of a magic square containing six square integers are possible. The
"smallest" (least magic sum) six-square example (Bremner's configuration 6.XV,
central cell 145 = 5·29):
```
265 1² 13²
 7² 145 241
11² 17²  5²
```
Two smallest with a *square* central cell (configurations 6.VII and 6.XIV),
which correspond under Bremner's correspondence (same square integers, one
identical diagonal):
```
889  697 17²      5² 1561 17²
 5²  25² 35²     889  25² 19²
31²  553 19²     31² -311 35²
```
Magic sum of a 3×3 magic square always = 3 × central cell.

**Seven-square configurations (fig. 5):** eight up to symmetry — 7.I…7.VIII.
**The only known seven-square example (fig. 6) is configuration 7.IV**, found
separately by Sallows and Bremner, central cell 425² = (5²·17)² = 180,625:
```
373²  289²  565²
360721 425² 23²
205²  527²  222121
```
central cell 425², the two non-square entries 360721 and 222121.

**Seven-square results already known (Boyer states two):**
- **Duncan Buell (1998), config 7.I ("magic hourglass"):** computed no solution
  with central cell < **25·10²⁴**. Boyer's direct consequence: *if a magic
  square of squares exists, its central cell is bigger than 25·10²⁴.* (Note:
  Buell's paper is a 1999 preprint, not on disk; this is the authoritative
  secondary statement of the bound and its scope — it concerns configuration
  7.I, the hourglass, *square* centre.)
- Sallows & Bremner: the only 7-square example (7.IV) with central cell 425².

**Eight-square configuration taxonomy (fig. 7):** three up to symmetry — 8.I,
8.II, 8.III. No 8-square or 9-square example known.

## What it establishes about the structure (the counting lemmas D1, D2)

A line through the centre C with two square entries around it solves x²+y²=2C.
Since 4k+3 primes cannot be sums of two squares, only central cells that are
products of 4k+1 primes are studied. A 4k+1 prime has one representation as a sum
of two squares; (a²+b²)(c²+d²) gives two; 2(a²+b²)=(a+b)²+(a−b)². Then:
- **D1.** Configs 7.I–7.VI and 8.I–8.II with C a square, C=c²: if c has n
  distinct 4k+1 prime factors then there are **(3ⁿ−1)/2** solutions of
  x²+y²=2c² with x<y.
- **D2.** Configs 7.VII, 7.VIII, 8.III with C not a square: if C has n distinct
  4k+1 prime factors then there are **2ⁿ⁻¹** solutions x²+y²=2C with x<y.

This matches the library's `phi-universal-set` formula (3ⁿ−1)/2 for the number
of AP-differences when the centre is a square with n distinct 1-mod-4 prime
factors — an independent confirmation of the |S(e)| formula from a different
route (D1 counts lines x²+y²=2c² = the same thing).

## Boyer's own searches (negative results)

**Square central cell** — only fig. 6 has ≥7 square entries, for central cell
types (5^i·p1·…·pk)² with various prime bounds (types a–m), covering central
cells up to ~10²³–10³⁰ in the largest families. Because a magic square with x
square entries keeps them when all cells are multiplied by a square, negative
results for (5²·p1·…)² cover all submultiples (5·p1…, p1…, etc.) in the studied
intervals.

**Non-square central cell** — no magic square with ≥6 square entries for types
n–x (5^i·p1·…) with prime bounds up to central cells ~10¹⁷.

## Conclusion / caveats

Boyer concludes it is "very strange (and really disappointing…)" to find no
second 7-square example, and states his *feeling* that a complete 9-square MSS
cannot exist — explicitly **not** a proof.

**Caveats for this run:** (1) The 25×10²⁴ Buell bound is Boyer's authoritative
secondary statement, specifically for the hourglass (7.I) with square centre;
the ROOT.md caveat that this is not a general full-MSS centre bound stands — but
note Boyer *does* state the direct consequence "if a MSS exists, central cell >
25×10²⁴" (because any MSS contains an hourglass as a sub-configuration). (2) The
(3ⁿ−1)/2 and 2ⁿ⁻¹ formulas are a different, complementary derivation of the
sum-of-two-squares counting behind `phi-universal-set`. (3) Boyer's own searches,
not a proof of impossibility — his own conclusion is a "feeling".

## Claim blocks

```claim
id: buell-hourglass-25e24-authoritative
statement: Duncan Buell (1998, preprint 1999) computed that configuration 7.I
  ("magic hourglass", square central cell) has no solution with central cell <
  25·10²⁴; Boyer draws the direct consequence that any 3x3 MSS of squares must
  have central cell > 25·10²⁴.
hypotheses: configuration 7.I; square central cell; Buell's search method and
  any coprimality assumption as in his preprint (not on disk).
holds-here: yes (target problem includes the hourglass via its centre lines)
status: asserted (primary secondary statement; Buell's own paper not on disk)
bearing: bounds where any proof must look; the run already treats 25e24 as a
  centre bound only with the caveat.
anchor: research/summaries/boyer-search-seven-square-entries.md
```

```claim
id: boyer-counting-lines-3n-1-over-2
statement: For a square central cell C=c² whose root c has n distinct 4k+1 prime
  factors, the number of lines x²+y²=2c² with two square entries (x<y) is
  (3ⁿ−1)/2; for non-square C with n distinct 4k+1 prime factors it is 2ⁿ⁻¹.
hypotheses: C product of distinct 4k+1 primes (with multiplicity in c for D1).
holds-here: yes; equals this run's |S(e)|=(∏(2a+1)−1)/2 for the square-centre
  case (independent confirmation).
status: asserted (Boyer states the method; this run's own formula matches)
bearing: independently confirms phi-universal-set / |S(e)| from a different
  derivation; tells how many AP-differences a centre of given prime type admits.
anchor: research/summaries/boyer-search-seven-square-entries.md
```
