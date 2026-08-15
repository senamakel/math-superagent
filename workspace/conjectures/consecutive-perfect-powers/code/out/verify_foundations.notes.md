# Verified foundation — exact-integer oracle and checks

`status: checked`

Program: `code/verify_foundations.py` — exact integer arithmetic only (no floats,
no logs, no `math.pow`). Output: `code/out/verify_foundations.captured.txt`.

## `.Oracle` — `solutions(N)`

All `(x,p,y,q)` with `x^p, y^q <= N` and `x^p - y^q = 1`.

| N | result | runtime |
| --- | --- | --- |
| 9 | `[(3,2,2,3)]` | 0.000s |
| 100 | `[(3,2,2,3)]` | 0.000s |
| 1000 | `[(3,2,2,3)]` | 0.000s |
| 10^4 | `[(3,2,2,3)]` | 0.000s |
| 10^5 | `[(3,2,2,3)]` | 0.000s |
| 10^6 | `[(3,2,2,3)]` | 0.000s |
| 10^7 | `[(3,2,2,3)]` | 0.001s |
| 10^8 | `[(3,2,2,3)]` | 0.002s |

**Largest N reached: 10^8; oracle returns exactly `(3,2,2,3)` for every N>=9.**

## `.Exp2-xq` — `x^2 - y^q = 1`, q prime

Unique solution `(3,2,2,3)` = `3^2 - 2^3 = 1` over the whole ladder to 10^8.

## `.Exp2-yp` — `x^p - y^2 = 1`, p prime

No solutions over the ladder to 10^8.

## `.PrimeReduction` — composite exponents descend to prime exponents

`(x^a)^P - (y^b)^Q = x^p - y^q` checked exactly on 40 composite cases; identity
held everywhere.

## `.DoubleWieferich` — distinct odd primes p,q <= 200

- ordered pairs: 1980; satisfying BOTH congruences `p^(q-1)≡1 (q^2)`,
  `q^(p-1)≡1 (p^2)`: **0**.
- unordered pairs satisfying at least one: 53.
- Duality check against the literature pair `(83,4871)`: both congruences hold
  there — the checker finds a real double-Wieferich pair when given one, so the
  0-within-200 result is a genuine finding, not a broken predicate.

## Claims (all `status: checked`, verified-numerically over the stated ranges only)

```claim
id: oracle-single-solution
statement: For every N in {9, 100, 1000, 10^4, 10^5, 10^6, 10^7, 10^8}, the set of solutions of x^p - y^q = 1 with x^p, y^q <= N is exactly {(3,2,2,3)}.
hypotheses: x,y>0, p,q>1, exact integer arithmetic.
holds-here: yes
status: checked
bearing: calibration target for every lemma; the known solution 3^2-2^3=1 must never be eliminated by a lemma.
anchor: code/out/verify_foundations.captured.txt
```

```claim
id: exp2-cases-numerically
statement: For x^2 - y^q = 1 (q prime) the only solution below 10^8 is (3,2,3); for x^p - y^2 = 1 (p prime) there is no solution below 10^8.
hypotheses: x,y>0, p,q prime.
holds-here: yes
status: checked
bearing: confirms the two exponent-2 cases numerically (not proved).
anchor: code/out/verify_foundations.captured.txt
```

```claim
id: prime-reduction-identity
statement: If p=a*P and q=b*Q with P,Q prime, then (x^a)^P - (y^b)^Q = x^p - y^q as integers, on 40 checked cases.
hypotheses: exact integer arithmetic.
holds-here: yes
status: checked
bearing: the reduction to prime exponents is algebraically sound (numerically confirmed).
anchor: code/out/verify_foundations.captured.txt
```

```claim
id: no-double-wieferich-below-200
statement: Among distinct odd primes p,q <= 200 there are no ordered pairs with both p^(q-1)≡1 (mod q^2) and q^(p-1)≡1 (mod p^2).
hypotheses: exact integer arithmetic.
holds-here: yes
status: checked
bearing: double-Wieferich pairs are rare and start above 200; e.g. (83,4871) is one.
anchor: code/out/verify_foundations.captured.txt
```
