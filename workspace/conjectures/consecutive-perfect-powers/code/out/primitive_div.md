# Primitive-divisor machinery — verification

Exact integer / exact sympy arithmetic; no floats.

## 1. Lucas identities (symbolic)

- `Phi_p(x) = (x^p-1)/(x-1) == U_p(x+1,x)` and `Phi_q(-y) = (y^q+1)/(y+1) == U_q(y-1,-y)` hold symbolically for p,q in {3,5,7,11,13} where U is the Lucas sequence U_0=0,U_1=1,U_{k+1}=P U_k - Q U_{k-1}. RESULT: PASS.

## 2. GCD lemma

- `gcd(x-1, Phi_p(x)) == gcd(x-1, p)` over p in {3,5,7,11,13,17}, x in [2,500]: checked 2994 pairs, 0 failures -> **PASS**.
- Known solution (3,2,2,3): q | x (3|3) yes; p | y (2|2) yes; elementary Cassels p | x-1 (2|2) yes, q | y+1 (3|3) yes. p=2 is EVEN, so the odd-prime Cassels theorem is excluded-by-hypothesis, not applied.

## 3. Primitive divisor existence (Zsigmondy)

- For odd prime p and x >= 2, `Phi_p(x)` has a primitive divisor r (r | Phi_p, r ∤ x-1, order of x mod r = p, r ≡ 1 mod p). Table (per p: xmax reached, values with a primitive divisor, largest primitive r):

| p | Xmax | primitive-divisor values | largest primitive r |
|---|------|--------------------------|--------------------|
| 3 | 200 | 199/199 | 37831 |
| 5 | 100 | 99/99 | 97039801 |
| 7 | 60 | 59/59 | 47446779661 |
| 11 | 40 | 39/39 | 610851724137931 |
| 13 | 30 | 29/29 | 16148168401 |
| 17 | 20 | 19/19 | 689852631578947368421 |
| 19 | 15 | 14/14 | 459715689149916492091 |
| 23 | 12 | 11/11 | 11111111111111111111111 |

- (p,x) with NO primitive divisor: 0 (none) -> **PASS** (Zsigmondy confirmed).
- Largest primitive r found overall: (11111111111111111111111, 23, 10).

## 4. Zsigmondy exception at p=2

- `Phi_2(3) = 4 = 3+1`, factors {2}; 2 ≢ 1 (mod 2), so no r ≡ 1 (mod 2) exists. The known solution (p=2) sits in the Zsigmondy exceptional index — oddness of p is essential.

## 5. Condition check (scope)

- A primitive r | Phi_p(x) divides y (y^q = (x-1) Phi_p(x), r ∤ x-1) and r ≡ 1 (mod p). This is the elementary (class-group-free) side of the Wieferich machinery — it gives a congruence on a divisor r | y, not Cassels' stronger p | y itself.
- Whether the primitive-divisor engine constrains beyond the double-Wieferich conditions is **not settled** here; that needs control of r^q against x^p-1 for all x, which these finite checks cannot establish.

```claim
id: prim-div-lucas-verified
statement: >
  Two Lucas identities hold symbolically for p,q in {3,5,7,11,13}: Phi_p(x)=(x^p-1)/(x-1)=U_p(x+1,x) and Phi_q(-y)=(y^q+1)/(y+1)=U_q(y-1,-y). gcd(x-1,Phi_p(x))=gcd(x-1,p) holds for p in {3,5,7,11,13,17}, x in [2,500]. For odd prime p in {3,...,23} and every x in [2,Xmax_p] the factor Phi_p(x) has a primitive divisor r ≡ 1 (mod p). At p=2 (known solution) no such r exists; oddness is essential.
hypotheses: >
  p,q odd primes for the identities/gcd/primitive-divisor claims; x >= 2. Known solution (3,2,2,3) has p=2 (even) and is excluded by the odd-prime hypothesis.
holds-here: yes (the primitive-divisor evidence covers an odd-prime range; the p=2 exception is confirmed separately)
status: checked (exact code verification, ranges stated)
bearing: elementary, class-group-free route to r ≡ 1 (mod p) with r | y; scope: not shown to go beyond double-Wieferich
anchor: code/out/primitive_div.md
```
