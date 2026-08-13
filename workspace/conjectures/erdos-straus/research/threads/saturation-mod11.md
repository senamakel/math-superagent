# Saturation of modulus 11

Directive 5: M=11 is the smallest modulus and the cheapest test of whether the
Salez seven-equation generator can saturate any modulus at all. Currently only
3 of 11 residues are covered. Either exhibit families for the 8 missing
residues, or prove an obstruction forbidding some of them. Either answer is a
result.

```thread
question: Can the Salez seven-equation generator produce polynomial identity
  families for all 11 residue classes t mod 11 (where t = (n−1)/840,
  n = 840·11·k + (840s+1) with s = t)?
status: open
rests-on: subprogression-families-verified-and-coverage,
  subprogression-coverage-positive-limit,
  seven-equations-complete,
  coverage-figure-triangulated
blocked-by: none — the search_subprogression.py engine is on disk
next: (1) Run search_subprogression.py focused on modulus a = 840×11 = 9240,
  enumerating b ≡ 1 (mod 840) that are QNR mod 9240 (Schinzel requirement).
  Record which t-residues mod 11 appear. (2) Apply Schinzel Thm 1 to determine
  which residues, if any, are ineligible for ANY ℤ[k]-polynomial family — the
  theorem forbids polynomial identities when b is a QR mod a, and with a=9240
  and b≡1 mod 840, b is a QR mod {2,3,5,7} automatically, so the QR/QNR
  condition reduces to b mod 11. Compute exactly which s-residues give b a QR
  vs QNR mod 11. (3) State the result: either families for all eligible missing
  residues, or a precise obstruction statement naming which residues are
  unreachable and why.
```

## Current state

From `code/out/aggregate_subprogression.captured.txt` (603 families across
moduli 11–37):

- Modulus 11: 3/11 residues covered: [5, 7, 10]
- Missing 8 residues: [0, 1, 2, 3, 4, 6, 8, 9]

## Why M=11 first

M=11 is the smallest modulus. With only 11 residue classes to cover and a
search space over b values that is proportionally smaller, this is the cheapest
possible saturation test. If the generator cannot saturate M=11, it cannot
saturate any prime modulus — and the uncovered density is bounded away from
zero by a product whose first factor stays at least the avoided fraction for
M=11.

## Method

`code/search_subprogression.py` runs the Salez seven converse equations
(Proposition 3 / Corollary 1) over A,B,C,D,E,F parameter grids for
n = a·k + b with a = 840m. For m = 11, this is a = 9240. The b values
must satisfy:
- b ≡ 1 (mod 840) (so n is in class 1 mod 840)
- gcd(b, 9240) = 1 (primitive)
- b is a quadratic non-residue mod 9240 (Schinzel: polynomial families
  require b a QNR mod a)

## The obstruction approach

Two independent lines:

1. **Search**: run the generator and see which missing residues it can reach
   with expanded parameter bounds.

2. **Schinzel analysis**: compute exactly which s-residues mod 11 produce b
   that are QRs vs QNRs mod 9240. Since b ≡ 1 mod 840 makes b a QR mod
   {2,3,5,7} automatically, the QR/QNR condition on b reduces to b mod 11.
   Residues that force b to be a QR mod 11 are Schinzel-forbidden: no
   ℤ[k]-polynomial identity can exist for them. This is an obstruction about
   the method, not about the conjecture — it says the polynomial-family
   approach cannot cover those residues regardless of parameter choices.

## Reference

- Schinzel Thm 1: `research/summaries/schinzel-three-unit-fractions.md`
- Salez seven equations: Proposition 3, Corollary 1 in
  `research/sources/salez-seven-modular-equations.full.md`
- Coverage triangulation: `code/out/coverage_triangulated.md`
- Aggregate data: `code/out/aggregate_subprogression.captured.txt`