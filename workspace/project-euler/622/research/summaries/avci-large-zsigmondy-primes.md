# Avci — "Large Zsigmondy Primes" (arXiv:2011.06136)

Source: https://arxiv.org/pdf/2011.06136 · full text: [[avci-large-zsigmondy-primes.full]]

## What it establishes

A survey-style paper giving the clean modern statement of Zsigmondy's theorem and a finer *large* Zsigmondy classification.

- **Zsigmondy's Theorem (stated, Sec 1):** for relatively prime integers a > b and n > 1, a^n − b^n has a *Zsigmondy prime* p (p | a^n − b^n but p ∤ a^m − b^m for 1 ≤ m < n) except when (a,b,n) = (2,1,6), or n = 2 and a + b = 2^k. Mentions Birkhoff–Vandiver's independent rediscovery.
- **Theorem 1.1 (large Zsigmondy primes):** a *large* Zsigmondy prime additionally has p² | a^n − b^n or p > n+1. Such a prime exists for all (a,b,n) except: (i) n=2 and a+b = 2^s or 3·2^s; (ii) n=4 and (a,b)∈{(2,1),(3,1)}; (iii) n=6 and (a,b)∈{(2,1),(3,1),(3,2),(5,4)}; (iv) n∈{10,12,18} and (a,b)=(2,1).
- **Lemma 2.2 (LTE):** for p ≥ 3 and x ≡ y ≢ 0 (mod p), v_p(x^n − y^n) = v_p(x−y) + v_p(n). Separate p=2 branch.
- **Cyclotomic structure (Lemmas 2.5–2.11):** x^n − 1 = ∏_{d|n} Φ_d(x); a^n − b^n = ∏_{d|n} Φ_d(a,b); and the p-adic valuation of Φ_n(a,b) is 1 on p^β·k, β≥1, where k is the order of a/b mod p.

## Consequences for this problem

For a=2, b=1 (the Mersenne case PE622 needs): Zsigmondy's single exception is n=6 (2^6−1 = 63 = 3²·7 has no primitive/order-6 prime). This is exactly the record in claim `zsigmondy-primitive-prime-divisor`: for every d | 60, d ≥ 2, d ≠ 6, Φ_d(2) has a prime p with ord_p(2) = d, so each order class among the primes of 2^60−1 is nonempty (the empty order-6 class is Zsigmondy's exception and is harmless). It is supporting, not load-bearing — the ord_m(2)=60 enumeration runs off the order data + Wieferich/lcm machinery, and only needs Zsigmondy to certify the full range of orders exists. LTE (Lemma 2.2) is a second anchor for the Wieferich lift `wieferich-lift-order`: it gives v_p(2^b − 1) = v_p(2−1) + v_p(b) for the correct intermediate exponents.

## Does not settle

No numerical enumeration for PE622; nothing about which specific primes divide 2^60−1 (that is arithmetic, already machine-checked).

## Status

Zsigmondy's theorem is cited (proved elsewhere, Zsigmondy 1892 / Birkhoff–Vandiver), its *statement* is asserted here; the large-Zsigmondy Theorem 1.1 and the LTE/p-adic lemmas are proved in the paper. Matches the existing `zsigmondy-primitive-prime-divisor` claim.

```claim
id: zsigmondy-large-zsigmondy-sourceable
statement: Zsigmondy's theorem (stated): for coprime a > b and n > 1, a^n - b^n
  has a primitive prime divisor p (p | a^n-b^n, p ∤ a^m-b^m for 1 <= m < n)
  except (a,b,n) = (2,1,6) and n=2 with a+b a power of 2. Large-Zsigmondy
  exceptions are listed in Theorem 1.1. In the a=2,b=1 Mersenne case the sole
  Zsigmondy exception is n=6: 2^6-1 = 63 = 3^2*7 has no order-6 prime.
hypotheses: gcd(a,b) = 1; a > b; n > 1.
holds-here: yes (n = 60, d | 60, none equals 6 except the harmless d=6;
  all moduli odd, gcd(2,·)=1).
status: sourced (Zsigmondy's theorem cited; exceptions verified here: the 11
  primes of 2^60-1 have exactly the recorded orders {2,4,3,10,12,5,20,60,15,30,60}).
bearing: certifies every order class {p : ord_p(2)=d}, d | 60, is nonempty and
  that the order-6 class is empty (Zsigmondy's (2,1,6) exception) — the
  completeness justification for the prime-power lcm classification.
anchor: research/sources/avci-large-zsigmondy-primes.full.md Theorem 1.1 + Sec 1
follows-from: zsigmondy-primitive-prime-divisor
```
