# OEIS A260683 — Number of 2's in the ternary expansion of 2^n

Source: https://oeis.org/A260683. Full text: `research/sources/oeis-A260683-number-of-2s-in-2n-base3.full.md`.

## What it establishes (catalogue)

`a(n) = # of digit 2 in (2^n)_3`. First values:
`0, 1, 0, 2, 1, 1, 1, 2, 0, 4, ...` — the value 0 occurs exactly at n = 0, 2, 8 in the listed range (and per the associated literature / verification bounds, only there up to far beyond). Erdős's conjecture is exactly `a(n) > 0` for n > 8.

Related OEIS numbers: A004642 (2^n in base 3), A020915 (number of ternary digits), A036461 (number of 1s), A104320 (number of 0s), A005836 (integers with no digit 2 in base 3).

## What it does for this problem

Confirms the witness set `{0, 2, 8}` as the only places `a(n) = 0` in the empirical table; useful as a quick reference for the digit-2 count. **Catalogue evidence, not proof** — OEIS b-files are computed terms; they establish the first N values, not the general statement. For a claim about witnesses, attribute the verification to the bound sources (Saye, Dimitrov–Howe), not to the OEIS row.

## Status

Catalogue. No theorem; do not cite for anything beyond the initial terms / witness confirmation.

```claim
id: OEIS-A260683-WITNESSES
statement: In the base-3 expansion of 2^n, the count of digit-2s is 0 exactly at
  n = 0, 2, 8 (first term values: 0,1,0,2,1,1,1,2,0,4,...). Erdős's conjecture
  is a(n) > 0 for n > 8.
hypotheses: n a nonnegative integer.
holds-here: yes — confirms the three witnesses are the only digit-2-free powers
  in the computed range.
status: catalogued (OEIS A260683; terms to n=10000) — a term list, not an
  argument; reproduction by a program is required to rely on it as established.
bearing: quick empirical confirmation of the witness set; not a proof.
anchor: research/sources/oeis-A260683-number-of-2s-in-2n-base3.full.md
```
