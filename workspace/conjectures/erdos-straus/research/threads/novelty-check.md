# Subprogression novelty check

Operator directive 3: the 554 subprogression families are real (554/554 exact
ℤ[k] polynomial identities), but their novelty against Elsholtz–Tao is
UNCHECKED. Identity families for 4/n have been searched for decades, and
rediscoveries announced as new are the failure mode the operator named.

```thread
question: Are the 554 subprogression families new, or are they rediscoveries
  of known Elsholtz–Tao Prop 1.9 / Salez seven-equation families in different
  coordinates? For each of the 12 moduli m ∈ {11,13,17,19,22,23,26,29,31,33,
  34,37}, which E-T family (if any) produces that modulus, and are the 83
  residue classes of t a subset of what E-T already classifies?
status: open
rests-on: subprogression-families-verified-and-coverage,
  elsholtz-k-unit-fractions-bound,
  elt-prop16-vanishing-odd-squares,
  seven-equations-complete
blocked-by: none — the Elsholtz–Tao source and the subprogression data are
  both on disk
next: (1) Parse the 554 families from code/out/subprogression.captured.txt
  into a structured form (m, t-residue, x(k), y(k), z(k)). (2) For each
  family, classify whether it is Type I or Type II (which denominator(s) carry
  the factor n). (3) Cross-reference against E-T Prop 1.9's four Type-I and
  three Type-II forms — match the modulus a = 840m and offset b to the E-T
  parametrisation and determine whether the family is a specialisation of an
  E-T form or genuinely new. (4) Report: per-modulus counts (how many of the
  83 classes are E-T-covered vs new), and whether any family shape (degree,
  coefficient pattern) is absent from the E-T classification. A rediscovery
  honestly labelled is fine.
```

## What the operator established

- 554/554 families verified as exact polynomial identities in ℤ[k]
- Moduli: a = 840m, m ∈ {11,13,17,19,22,23,26,29,31,33,34,37}
- All b ≡ 1 (mod 840)
- 83 distinct residue classes of t under n = 840t+1
- Coverage: 94.72% of n ≡ 1 (mod 840); uncovered 5.28% has positive density

## Reference: Elsholtz–Tao Prop 1.9 forms

From `research/sources/elsholtz-tao-counting.full.md` lines 2390–2470:

**Type I** (p divides exactly one denominator):
1. n ≡ −f (mod 4ad) with f | 4a²d + 1
2. n ≡ −f (mod 4ac) and n ≡ −c/a (mod f)
3. n ≡ −f (mod 4cd) and n² ≡ −4c²d (mod f)
4. n ≡ −1/e (mod 4ab) with e | a + b

**Type II** (p divides exactly two denominators):
5. n ≡ −e (mod 4ab)
6. n ≡ −4a²d (mod f) with 4ad | f + 1
7. n ≡ −4a²d − e (mod 4ade)

Salez's seven equations are the degree-1 linear special case.

## What to match

For each subprogression family with n = 840m·k + b:
- Identify which of x(k), y(k), z(k) carry the factor (840m·k + b) — this
  determines Type I vs Type II.
- Extract the parameters (a, c, d, e, f) that produce the modulus 840m and
  offset b ≡ 1 mod 840 in the E-T classification.
- If no (a,c,d,e,f) tuple in the E-T classification produces this family,
  it is new.

## Density context

The operator noted that 94.72% coverage with 12 moduli, leaving 5.28%
positive-density gap, means these 12 moduli cannot close the class. The
novelty question is orthogonal: even if all 554 are rediscoveries, the
coverage quantification is new and valuable. If any are genuinely new shapes,
that changes what the next search should target.