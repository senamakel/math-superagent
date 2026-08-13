# Saturation of modulus 23

Operator directive 4: the uncovered density factors over independent prime
groups as a product of (p − c_p)/p, every factor strictly positive. It reaches
zero only if for some single modulus m the generator realises all m residues.
23 is the smallest with room: currently 9/23 residues realised, 14 avoided.
Either exhibit families for the 14 missing residues, or prove an obstruction.

```thread
question: Can the Salez seven-equation generator produce polynomial identity
  families for all 23 residue classes t mod 23 (where t = (n−1)/840,
  n = 840·23·k + (840s+1) with s = t)?
status: deferred
rests-on: subprogression-families-verified-and-coverage,
  subprogression-coverage-positive-limit,
  seven-equations-complete
blocked-by: none — the search_subprogression.py engine is on disk and running
next: (1) Run search_subprogression.py focused on modulus a = 840×23 = 19320,
  enumerating b ≡ 1 (mod 840) that are QNR mod 840×23 (Schinzel requirement).
  Record which t-residues appear. (2) For any missing residues after a bounded
  search, attempt to prove an obstruction: the equations (14a)–(15d) with
  p = a·k + b constrain b modulo the constants B,C,D,E,F; show that some
  residues s = (b−1)/840 mod 23 cannot satisfy any of the seven congruences
  for any choice of the constant parameters within bounded ranges. (3) State
  the result: either families for all 23 residues, or a precise statement of
  which residues are unreachable and why.
```

## Current state

From the operator's coverage recomputation (1451 families, 123 distinct (m,s)
across all three capture files):

- Modulus 23: 9/23 residues covered: [5, 9, 12, 13, 15, 17, 18, 19, 20]
- Missing 14 residues: [0, 1, 2, 3, 4, 6, 7, 8, 10, 11, 14, 16, 21, 22]

## Method

`code/search_subprogression.py` runs the Salez seven converse equations
(Proposition 3 / Corollary 1) over A,B,C,D,E,F parameter grids for
n = a·k + b with a = 840m. For m = 23, this is a = 19320. The b values
must satisfy:
- b ≡ 1 (mod 840) (so n is in class 1 mod 840)
- gcd(b, 19320) = 1 (primitive)
- b is a quadratic non-residue mod 19320 (Schinzel: polynomial families
  require b a QNR mod a)

## The obstruction approach

If some residue s mod 23 is unreachable, the proof would be: for that s,
b = 840s + 1, and for every choice of the constant parameters (A,B,C,D,E,F)
in the seven equations with a = 19320, either the congruence condition fails
or the resulting x,y,z are not all positive-integer-valued polynomials in k.
This is a finite check for fixed parameter bounds — a complete proof if the
bounds are large enough to exhaust all possibilities.

## Reference

- Salez seven-equation converse: Proposition 3, Corollary 1 in
  `research/sources/salez-seven-modular-equations.full.md`
- Coverage summary: `code/out/coverage_update_extended.md`