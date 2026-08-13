# All 554 identity families verify exactly, and they cover 94.72% of `n ≡ 1 (mod 840)`

`code/out/subprogression.captured.txt` reports 554 parametric families for the
hardest open class. The run had not yet verified them as identities, nor
computed what they cover. The operator did both.

## Every family is an exact polynomial identity

Each block gives `n = a·k + b` and polynomials `x(k), y(k), z(k)`. The test
applied was the cleared-denominator identity in `Z[k]`

```
4·x·y·z  −  n·(y·z + x·z + x·y)  ≡  0
```

carried out in exact integer polynomial arithmetic (no floats, no sympy — a
small `Poly` class over `Z`). Result:

```
parsed blocks: 554
exact polynomial identities: 554/554     failures: 0
```

This is the distinction the workspace has been asked to keep: these are **not**
"tested on small `k`". The identity holds in `Z[k]`, hence for every integer
`k`. Positivity and integrality were checked separately — all coefficients are
integers, and `x(k), y(k), z(k) > 0` was confirmed at `k = 0, 1, 5, 10⁴`, with
`1/x + 1/y + 1/z = 4/n` re-verified in exact `Fraction` arithmetic at those `k`.

A family with `n = a·k + b` settles every `n ≡ b (mod a)` with `n ≥ b`. The
finitely many members of the progression below `b` are not covered by the
family and must be checked directly.

## What they cover, exactly

Every one of the 554 has `b ≡ 1 (mod 840)`, and every modulus is `a = 840·m`
with

```
m ∈ {11, 13, 17, 19, 22, 23, 26, 29, 31, 33, 34, 37}
```

Writing `n = 840t + 1`, the condition `n ≡ b (mod 840m)` reduces exactly to
`t ≡ s (mod m)`. So the families are 83 distinct residue classes of `t`, and
the covered fraction of the class is a finite computation. The moduli are not
coprime, so the union was computed by CRT after splitting the primes into
independent groups:

| prime group | modulus | classes | `t` avoiding all |
| --- | --- | --- | --- |
| `{2,3,11,13,17}` | 14586 | 53 | `3696/14586 = 56/221` |
| `{19}` | 19 | 5 | `14/19` |
| `{23}` | 23 | 9 | `14/23` |
| `{29}` | 29 | 6 | `23/29` |
| `{31}` | 31 | 7 | `24/31` |
| `{37}` | 37 | 9 | `28/37` |

The groups are independent, so the uncovered density multiplies:

```
uncovered within n ≡ 1 (mod 840):  7375872/139671337  =  5.280877%
covered   within n ≡ 1 (mod 840):  132295465/139671337 = 94.719123%
```

## What this is not

Three limits, stated so the result is not overread.

1. **It addresses one of the six open classes.** `n ≡ 121, 169, 289, 361, 529
   (mod 840)` are untouched by these families. As a fraction of all `n`, what
   is settled here is `132295465/(840·139671337) ≈ 0.1128%`.
2. **The residue `t` classes leave a positive density uncovered.** `5.28%` of
   the class remains, and a positive density is not a finite set — no amount of
   further families of these same moduli closes it. Closing it needs either new
   moduli or a different mechanism.
3. **Novelty is unestablished.** Identity families for `4/n` have been searched
   extensively; Elsholtz–Tao is the reference for which classes fall to which
   shape. Whether any of these 554 is new, or whether all are rediscoveries in
   different coordinates, has not been checked and must not be assumed. That
   check is the next step, and `research/sources/elsholtz-sums-of-k-unit-fractions.full.md`
   (40 KB, a genuine source) is where to do it.

```claim
id: subprogression-families-verified-and-coverage
statement: The 554 parametric families in code/out/subprogression.captured.txt
  are each an exact polynomial identity in Z[k]: 4xyz - n(yz+xz+xy) = 0
  identically, where n = a*k + b, verified in exact integer polynomial
  arithmetic with zero failures over all 554. Coefficients are integers and
  x,y,z > 0 was confirmed at k = 0,1,5,10^4 with 1/x+1/y+1/z = 4/n re-checked
  in exact Fraction arithmetic. Every family has b congruent to 1 mod 840 and
  modulus a = 840m for m in {11,13,17,19,22,23,26,29,31,33,34,37}, which under
  n = 840t+1 reduces to 83 residue classes of t. Their union covers exactly
  132295465/139671337 = 94.719123% of the class n congruent to 1 mod 840,
  leaving 7375872/139671337 = 5.280877% uncovered.
hypotheses: k a non-negative integer; a family covers n congruent to b mod a
  only for n >= b, the finitely many smaller members needing direct check
holds-here: yes. The identities are unconditional in Z[k]. The coverage figure
  is exact rational arithmetic, not an estimate
status: checked
bearing: converts 554 families from asserted to identities proved in Z[k], and
  quantifies for the first time what they buy: 94.72% of one of the six open
  classes, about 0.1128% of all n. The uncovered 5.28% has positive density, so
  no further family of these moduli can close it. Does not touch the other five
  open classes. Novelty against Elsholtz-Tao is unchecked and must not be
  assumed
anchor: code/out/subprogression.captured.txt; code/out/subprogression_coverage.md
source: operator-computation
```
