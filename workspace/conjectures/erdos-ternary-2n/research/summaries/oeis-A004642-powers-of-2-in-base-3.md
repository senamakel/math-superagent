# OEIS A004642 — Powers of 2 written in base 3

Source: https://oeis.org/A004642. Full text: `research/sources/oeis-A004642-powers-of-2-in-base-3.full.md`.

## What it establishes (catalogue + one useful structural fact)

`a(n) = (2^n)_3` as a ternary-digit string. First values (n=0..25):
`1, 2, 11, 22, 121, 1012, 2101, 11202, 100111, 200222, ...` — the digit-{0,1}-only entries are exactly n = 0 (1), n = 2 (11), n = 8 (100111).

**Structural fact (Alonso del Arte):** `2^n ≡ 1 (mod 3)` when n is odd, `≡ 2 (mod 3)` when n is even. So the least significant ternary digit of `2^n` is 1 (n odd) or 2 (n even). **A digit-2-free `2^n` therefore requires n even** — its last digit must be 1. This is a real constraint: search / invariance arguments can restrict to even n immediately.

Also recorded: Erdős (1978) conjecture `a(n)` has a 2 for n > 8; Sloane (1973) conjecture `a(n)` has a 0 between most- and least-significant digits for n > 15; and the cross-links to the Aliyev and Lagarias sources already in this library.

## What it does for this problem

- Confirms the witness set `{0,2,8}` in the catalogue range.
- Gives the parity constraint: any candidate counterexample must have n even (this is free and exact).
- Catalogue terms are computed, not proven; attribute verification to the bound sources.

## Status

Catalogue. The parity/digit fact is elementary and exact; the witness list is computed terms.

```claim
id: OEIS-PARITY-CONSTRAINT
statement: 2^n ≡ 1 (mod 3) for odd n, 2 (mod 3) for even n, so the last ternary
  digit of 2^n is 1 (odd) or 2 (even). Hence any digit-2-free 2^n (last digit 1)
  must have n even.
hypotheses: n a nonnegative integer.
holds-here: yes — restricts possible counterexamples to even n immediately.
status: proved (elementary mod-3; 2 ≡ -1 mod 3, so 2^n ≡ (-1)^n)
bearing: a free structural restriction on counterexamples; any invariance or
  search should reduce to even n. Confirms 2^0, 2^2, 2^8 (all even) are the
  digit-free witnesses.
anchor: research/sources/oeis-A004642-powers-of-2-in-base-3.full.md
```
