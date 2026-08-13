# Cunningham pmain901 main tables (Table 2− only) — acquired, but does NOT close the 2^n+1 gap

Full text: [[cunningham-pmain901-2n-plus-minus.full]]
Source: https://homes.cerias.purdue.edu/~ssw/cun/third/pmain901

## What it is

The modern Cunningham main-tables file (version pmain901, ~500 KB). The held
excerpt is **Table 2−: factorizations of `2^n − 1`, `n` odd** — the same side
as the earlier-acquired `pmain126.txt` (`research/sources/cunningham-main-tables-jan2026.full.md`),
but a newer and more complete version.

## What it establishes and what it does NOT

- Exact prime factorizations of `2^n − 1` for odd `n` (up to the file's range),
  with the `(…)` notation giving algebraic/cyclotomic divisor groupings (e.g.
  `2^105−1 = (3,5,7,15,21,35)·29191·106681·152041`).
- **It does NOT contain `2^n + 1` (Table 2+, the Fermat / Aurifeuillean `L_p, M_p`
  side), nor any even-exponent `+1` data.** The `2^n+1` factorization tables live
  in **Appendix C** of the Cunningham book/third-edition files and are still not
  in this library.
- Therefore **still no table source for the `H_even` branch**: the open
  candidates are `m = 2p` with `p ≥ 1213`, i.e. exponents `n = 2p` up to ~35000
  and numbers `2^n + 1`, which is not here and is in any case not fully factored
  even by the Cunningham project (those cofactors are the paper's stated
  blocking point — 355–6000 digit unfactored composites).

## Bearing on this run — HONEST verdict

**Marginal.** `pmain901` upgrades the already-held `2^n − 1` lookup (newer,
deeper) but adds nothing to the `H_even` branch, which needs the `+1` side.
It is retained as a catalogue lookup for `2^n − 1` side checks (Mersenne-side
verification, cyclotomic divisor groupings), not as a branch-progress source.

```claim
id: cunningham-pmain901-2n-minus-1-newer
statement: pmain901 is a newer, fuller table of 2^n - 1 (n odd) factorizations
  than the held pmain126 excerpt; it contains NO 2^n + 1 data. The 2^n + 1
  Table (Appendix C of the Cunningham book) remains unobtained, so no H_even
  branch number 2^(2p)+1 is covered by any held Cunningham table.
hypotheses: the file pmain901 holds Table 2- only
holds-here: n/a -- needed object (2^(2p)+1 for H_even) not in source
status: catalogued
bearing: prevents re-attempting pmain* files for +1 data; the +1 / Appendix C
  tables are a separate file and even they do not resolve the open cofactors
anchor: research/sources/cunningham-pmain901-2n-plus-minus.full.md
```
