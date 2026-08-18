# Chen-prime Goldbach check: no exception through 10^8

Every even n ≡ 4 (mod 6) with 4 ≤ n ≤ 10^8 is a sum of two Chen primes
(primes p with p+2 prime or semiprime). The checker found no first failure at
any bound; the largest verified n is 10^8 itself.

- 10^6: 0.39 s, last witness (41, 999959)
- 10^7: 4.60 s, last witness (29, 9999971)
- 10^8: 63.12 s, last witness (29, 99999971)
- 10^8 module-form rerun: 63.38 s, identical output

The method is exact (bytearray flags, integer arithmetic): sieve of
Eratosthenes to B+2, semiprime marks from all prime pairs f ≤ g with
f·g ≤ B+2, Chen flag = prime and (p+2 prime or semiprime), then for each
n ≡ 4 mod 6 scan p ≤ n/2 for p and n−p both Chen. Correctness was checked by
an independent trial-division oracle (factor-count definition of semiprime)
for every p ≤ 200, by the three hand classifications (p=2: 4=2·2; p=3: 5
prime; p=7: 9=3·3), and by reproducing the ordinary Goldbach partition
oracle for every even n in [4, 1000].

This is finite evidence for candidate (d) of G-structural-closure in
`research/backward/full-goldbach-via-exceptional-set.md`: the
Grimmelt–Teräväinen exceptional set for n ≡ 4 mod 6 contains no element
below 10^8. It does not prove the structural lemma; the exceptional set could
be nonempty above 10^8.

```claim
id: chen-prime-goldbach-check-1e8
statement: Every even n with 4 <= n <= 10^8 and n == 4 (mod 6) is a sum of
  two Chen primes (p prime and p+2 prime or semiprime).
status: checked
evidence: exact program code/chen_goldbach/check.py, run to bound 10^8
  (63.12 s, no first failure); rerun in module form reproduced identical
  output (witness (29, 99999971) at n = 10^8). Oracle cross-check vs
  trial-division definition for p <= 200; hand checks p=2,3,7; ordinary
  Goldbach oracle reproduced for all even n in [4, 1000].
search-frame: all n == 4 (mod 6) in [4, 10^8]; outside the published
  exhaustive verification regime 4e18 is irrelevant here — this is a
  Chen-pair statement, not ordinary Goldbach.
bears-on: research/backward/full-goldbach-via-exceptional-set.md
  G-structural-closure, candidate (d)
```
