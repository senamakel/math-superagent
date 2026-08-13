<!-- source: https://homes.cerias.purdue.edu/~ssw/cun/pmain126.txt | converted from plain text -->

# Cunningham Project Main Tables (Jan 2026)

The Main Tables as of January 5, 2026 (factorizations of `2^n ± 1`,
`3^n ± 1`, `5^n ± 1`, `6^n ± 1`, `7^n ± 1`, `10^n ± 1`, `11^n ± 1`, `12^n ± 1`
b^n ± 1 with b = 2,...,12 and selected higher bases), with all factors through
#6871 on Page 148. Portion held: `[[cunningham-main-tables-jan2026.full]]` is
the **Table 2 excerpt** — factorizations of `2^n − 1`, `n` odd, `n < 1500`
(the file's visible content), a 1.02 MB plain-text table.

## What it establishes and what it does not

- Exact prime factorizations of `2^n − 1` for odd `n < 1500` (e.g.
  `2^149 − 1 = 86656268566282183151 · 8235109336690846723986161`). Useful for
  Mersenne-side checks; **the table covers `2^n − 1`, NOT `2^n + 1`** — the
  `+1` side (Fermat/Aurifeuillean `L_p, M_p`, the site of the `H_even` prime
  branch `2^{2p}+1`) is not in the held excerpt.
- **None of the H_even open candidates appear**: the open branch is `m = 2p`
  with `p ∈ [1213, 17467]`, hence exponents `n = 2p` up to ~35000, and the
  numbers are `2^n + 1` — outside both the held range (`n < 1500`) and the
  held side (`−1`). The known ten `H_even` members (`m ≤ 122` ⇒ `2^m + 1`,
  m even, m ≤ 122) would need the even-exponent `+1` tables, which are the
  **Appendix C** tables (not held).

## Bearing on this run

**No direct bearing.** This source cannot verify any `H_even` element (needs
`2^m+1`, m even) nor factor any open candidate (`2^{2p}+1`, p ≥ 1213). It is a
lookup for `2^n−1` side data only. The A002827 OEIS internal-format file
remains the correct catalogue check for the five UPNs. Do not re-fetch the full
file expecting `+1` data; the `+1` tables live in a separate Appendix C file.

```claim
id: cunningham-2n-minus-1-lookup
statement: Cunningham Main Tables (Jan 2026) hold factorizations of 2^n - 1,
  n odd, n < 1500 in the held excerpt; the 2^n + 1 tables and Appendix C are
  not in the library, and no H_even candidate (2^m + 1, m even) or open
  H_even prime case (2^(2p) + 1, p >= 1213) appears in it.
hypotheses: the held file is the pmain126.txt Table 2 excerpt
holds-here: n/a -- the object needed (2^m + 1 for H_even) is not in the source
status: catalogued
bearing: prevents a wasteful re-read; the H_even verification must use its own
  factorization pipeline, not this table
anchor: research/sources/cunningham-main-tables-jan2026.full.md
answers: whether-cunningham-tables-cover-heven
```