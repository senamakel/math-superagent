# Divisor-63 characterization of the five-member family

## Statement (CHECKED)

For a strongly regular graph `srg(v,k,1,2)` with `v = 1 + k + k(k-2)/2`, eigenvalue-
multiplicity integrality holds **iff**
```
a = sqrt(4k-7) = 2u+1  is an odd divisor of 63,
```
i.e. `a in {3, 7, 9, 21, 63}` and `u in {1, 3, 4, 10, 31}`. This is exactly the
five-member family `v in {9, 99, 243, 6273, 494019}` (Berlekamp–van Lint–Seidel /
Makhnev–Minakova classification), reproduced here from first principles.

## Why it is the right factorization

The index list `{1,3,4,10,31}` that "classifies" the family is otherwise opaque.
It is in fact nothing more than: the quantity `a = sqrt(4k-7)`, which must be an
odd integer `2u+1`, simultaneously:
- makes `4k-7` a perfect square (equivalently `k = u^2+u+2`), and
- makes the negative-eigenvalue multiplicity an integer.

The derivation shows both collapse to one condition, `a | 63`:

```
v-1       = k^2/2
2k-(v-1)  = k(4-k)/2
k         = (a^2+7)/4,   4-k = (9-a^2)/4
k(4-k)/2  = (a^2+7)(9-a^2)/16

mult of negative eigenvalue  g = ( (v-1) - (2k-(v-1))/a ) / 2
integrality requires  a | k(4-k)/2.  Since a is odd, gcd(a,16)=1, so
a | k(4-k)/2  <=>  a | (a^2+7)(9-a^2)  <=>  a | 7*9 = 63.
The remaining /2 parity is satisfied exactly when a | 63 (checked).
```

`(a^2+7)(9-a^2) mod a = 63` is verified symbolically (sympy `rem = 63`).

## Exact verification

| a (=2u+1) | u | k | v | integrality |
|---|---|---|---|---|
| 3  | 1  | 4   | 9     | PASS (rook's graph / Paley 9) |
| 5  | 2  | 8   | 33    | FAIL (2k-(v-1)=-16 not div by 5) — **srg(33,8,1,2) doesn't exist** |
| 7  | 3  | 14  | 99    | PASS (**open** — the Conway-99 problem) |
| 9  | 4  | 22  | 243   | PASS (BvLS graph, exists) |
| 11 | 5  | 32  | 513   | FAIL |
| 13 | 6  | 44  | 969   | FAIL |
| 21 | 10 | 112 | 6273  | PASS |
| 63 | 31 | 994 | 494019| PASS |

Scan over `u in [1, 300000]`: `passes(u)` iff `(2u+1) | 63`, **zero mismatches**.
This is a scan over the DESCRIPTION index of a closed-form family (verifying a
claimed classification), not a search of the answer space.

```claim
id: divisor63-multiplicity-integrality
statement: Eigenvalue-multiplicity integrality of any srg(v,k,1,2) holds iff
  a = sqrt(4k-7) = 2u+1 is an odd divisor of 63, i.e. a in {3,7,9,21,63} and
  u in {1,3,4,10,31}; this is exactly the five-member family (9,4),(99,14),
  (243,22),(6273,112),(494019,994). Mechanism: mult g = ((v-1) - (2k-(v-1))/a)/2
  requires a | k(4-k)/2; with k=(a^2+7)/4 and a odd (gcd(a,16)=1) this reduces
  mod a to a | (a^2+7)(9-a^2) = 7*9 = 63 (sympy rem = 63, verified). This also
  names the mechanism that kills srg(33,8,1,2) (a=5 not | 63) and why it cannot
  touch 99 (a=7 | 63): 99 is the a=7 member.
hypotheses: any srg(v,k,1,2); v = 1 + k + k(k-2)/2; a = sqrt(4k-7) an odd integer.
holds-here: yes — verified symbolically (sympy rem = 63) and by scan over
  u in [1,300000] with zero mismatches (passes(u) iff (2u+1) | 63).
status: checked
bearing: gives an exact structural restatement — a putative (99,14,1,2) is the
  a=7 member — and shows the 33-precedent (a=5) is a spectral dead end that
  cannot transfer to 99, matching the GOAL.md discipline.
anchor: code/out/divisor63-characterization.md, code/out/feasibility-candidates-corrected.md
```

## Bearing on the 99 problem

- The mechanism that rules out `srg(33,8,1,2)` (the "nearest precedent" in
  problem.md) is this same `a | 63` integrality test; it is spectral and **cannot
  transfer to 99** (a=7 divides 63, so 99 passes integrality). This confirms and
  sharpens claim `srg33-mechanism-answers-request`: the 33-precedent is a dead end
  for 99, and now we know exactly why (a=5 not | 63, while a=7 | 63).
- 99 has `a = 7`, the smallest odd divisor of 63 beyond 3. So 99 is the "first
  genuinely open" member after the rook's graph — consistent with it being the
  famous hard case and 243 (a=9) existing.
- This gives the run a clean, exact, structural restatement: **a putative
  (99,14,1,2) is the member with `a=7`**, and any nonexistence argument must be
  specific to `a=7` (not the integrality that 9 and 243 both survive).

## Verification status
CHECKED (exact integer arithmetic + symbolic sympy reduction + scan to 300000).
