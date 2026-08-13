# Coverage update: 1451 families now, and the returns are collapsing

Supersedes the coverage figure in `code/out/subprogression_coverage.md`, which
was computed on `subprogression.captured.txt` alone. The run has since produced
`extended_subprogression.full.txt`, adding moduli `m = 38, 39, 41, 43` — genuine
new primes 41 and 43, which is what was asked for.

All blocks across all three capture files were re-parsed and the union
recomputed by the same CRT method.

```
subprogression.captured.txt        838 FOUND blocks
extended_subprogression.full.txt   597 FOUND blocks
extended_subprogression.captured.txt 16 FOUND blocks
total 1451 blocks  ->  123 distinct residue classes (m, s)
moduli m: 11,13,17,19,22,23,26,29,31,33,34,37,38,39,41,43
```

| prime group | modulus | classes | `t` avoiding all |
| --- | --- | --- | --- |
| `{2,3,11,13,17,19}` | 277134 | 82 | `7/39` |
| `{23}` | 23 | 9 | `14/23` |
| `{29}` | 29 | 6 | `23/29` |
| `{31}` | 31 | 7 | `24/31` |
| `{37}` | 37 | 10 | `27/37` |
| `{41}` | 41 | 6 | `35/41` |
| `{43}` | 43 | 3 | `40/43` |

```
covered   within n ≡ 1 (mod 840):  732719497/762354697 = 96.112676%
uncovered within n ≡ 1 (mod 840):   29635200/762354697 =  3.887324%
```

## The trend is the result

| | families | covered |
| --- | --- | --- |
| previous | 554 | 94.719123% |
| now | 1451 | 96.112676% |

**Nearly tripling the family count bought 1.39 percentage points.** The per-prime
avoidance fractions show why: the newest primes are the weakest contributors —
`41` removes only `6/41` of its residues and `43` only `3/43`, against `14/23`
and `23/29` avoided at the older primes. Each new prime `p` enters the product
as a factor `(p − c_p)/p`, and `c_p` is not growing with `p`.

## Why this method cannot close the class

The uncovered density is a **product of strictly positive rational factors**,
one per independent prime group. It is therefore strictly positive for any
finite set of families, and remains so no matter how many are added — unless
for some single modulus `m` the generator produces **all** `m` residues, which
would send that factor to zero and the whole product with it.

That is the sharp question, and it is finite and checkable: for which `m`, if
any, can the generator realise every residue class `s mod m`? At present the
best is the `{2,3,11,13,17,19}` group at `7/39` avoided, so no modulus is
close to full. Absent such an `m`, generating further families is guaranteed to
approach a positive limit and never reach 1, and the run should stop generating
and either prove that some modulus can be saturated or change mechanism.

This is the same shape as the negative result in the ternary workspace: a proof
about what the *method* can reach, which is worth more than another increment.

```claim
id: subprogression-coverage-positive-limit
statement: Across all three capture files the run has produced 1451 identity
  family blocks, giving 123 distinct residue classes (m, s) with moduli m in
  {11,13,17,19,22,23,26,29,31,33,34,37,38,39,41,43}. Their union covers
  732719497/762354697 = 96.112676% of the class n congruent to 1 mod 840,
  leaving 29635200/762354697 = 3.887324% uncovered, up from 94.719123% at 554
  families. Since the uncovered density factors over independent prime groups
  as a product of terms (p - c_p)/p, it is strictly positive for any finite
  family set, and can reach zero only if for some modulus m every one of the m
  residues is realised. No modulus is currently close to saturation, the best
  group avoiding 7/39.
hypotheses: the families are exact identities in Z[k], established separately
  in subprogression-families-verified-and-coverage; a family for n = a*k + b
  covers n congruent to b mod a only for n >= b
holds-here: yes. Exact rational arithmetic over the parsed family set; the
  positivity of the product is immediate from each factor being positive
status: checked
bearing: shows the identity-family method is in sharp diminishing returns -
  tripling the family count bought 1.39 percentage points - and that it
  converges to a positive uncovered density rather than closing the class.
  Reduces the open question to a finite one: is there a modulus m all of whose
  residues the generator can realise. If not, further families cannot settle
  n congruent to 1 mod 840 and the mechanism must change
anchor: code/out/subprogression.captured.txt;
  code/out/extended_subprogression.full.txt; code/out/coverage_update_extended.md
source: operator-computation
```
