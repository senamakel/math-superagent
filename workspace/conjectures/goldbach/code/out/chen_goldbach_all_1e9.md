# All-even Chen-pair Goldbach check: first failure 302

The earlier 4-mod-6-only run found **no failure through 10^8**. The all-even
sweep — every even n, 4 ≤ n ≤ B, is a sum of two Chen primes p ≤ n/2 — finds
its **first failure at n = 302**. So the 4 mod 6 restriction in the
Grimmelt–Teräväinen theorem is not where the phenomenon "lives"; it is the
only residue class that stays clean, and the failure lives in the 2 mod 6
class.

## Result

- All-even check, 4 ≤ n ≤ B, first n with no Chen pair: **302**, for every
  bound B = 10^7, 10^8, 10^9 (the sweep stops at the first failure, so the
  result is bound-independent once B ≥ 302).
- Original 4-mod-6 class: **no failure** through 10^9 (extending the 10^8
  claim to 10^9).
- All failures ≤ 10^6 (27 of them) are **≡ 2 (mod 6)**; none in 0 or 4 mod 6.

Failures ≤ 10^6:
`[302, 332, 458, 542, 632, 692, 872, 902, 1544, 1964, 2522, 2642, 2834,
4544, 4952, 6932, 7442, 9170, 11114, 11672, 12224, 13562, 17072, 22922,
34082, 34892, 35912]` (27 values).

## Why 302 fails (independent factorisation)

For n ≡ 2 (mod 6), every Goldbach pair p + q = n has both primes ≡ 1 (mod 3)
(proved in `research/threads/mod6-structure-minimal-goldbach.md`), so the
complement q always has q + 2 ≡ 0 (mod 3); q is Chen iff (q+2)/3 is prime.
For 302 the Goldbach pairs are
(19,283), (31,271), (61,241), (73,229), (79,223), (103,199), (109,193),
(139,163), (151,151). In every pair where p is Chen, (q+2)/3 is composite
(285/3=95, 273/3=91, 195/3=65, 165/3=55); in the pair where q is Chen
(q=199, 201=3·67), p=103 is not Chen (105=3·5·7). So no pair has both sides
Chen — a genuine both-or-neither obstruction. Verified by sympy direct
factorisation, not the sieve.

## Why the 4 mod 6 class is special

The theorem's n ≡ 4 (mod 6) class is exactly the one with no failures in the
entire verified range; failures concentrate in n ≡ 2 (mod 6). This is
consistent with the structural story in
`research/backward/full-goldbach-via-exceptional-set.md` — the exceptional
set for Chen-pair sums is real and lives off the 4 mod 6 class.

## Verification (second route)

- Sieve method (`check.py`, bytearray exact): first failure 302 at every
  bound; 4-mod-6 clean to 10^9.
- Independent trial-division oracle (`oracle_check.py`): Chen flags match the
  sieve for every p ≤ 200, and the oracle's own all-even scan finds first
  failure 302 and no other failures ≤ 302.
- Independent sympy factorisation route: same 27 failures ≤ 10^5, same first
  failure 302, exact agreement.

## Runs (exact commands and outputs in `code/out/`)

| Command | Bound | All-even first failure | 4-mod-6 first failure | Tested n≡4 mod 6 | Wall |
| --- | --- | --- | --- | --- | --- |
| `python -m chen_goldbach.check 10000000` | 10^7 | 302 | none | 1666667 | 4.29 s |
| `python -m chen_goldbach.check 100000000` | 10^8 | 302 | none | 16666667 | 63.98 s |
| `python -m chen_goldbach.check 1000000000` | 10^9 | 302 | none | 166666667 | 800.59 s |

Outputs: `code/out/chen_goldbach_all_1e7.txt`, `chen_goldbach_all_1e8.txt`,
`chen_goldbach_all_1e9.txt`, `chen_goldbach_all_oracle_check.txt`,
`chen_goldbach_all_census_1e6.txt`, `chen_goldbach_all_sympy_crosscheck.txt`.

```claim
id: chen-prime-goldbach-all-even-1e9
statement: The least even n >= 4 that is NOT a sum of two Chen primes
  (p and n-p both Chen) is 302, and 302 == 2 (mod 6).  Every even n == 4
  (mod 6) with 4 <= n <= 10^9 IS a sum of two Chen primes.  The complete
  all-even failure census is known to 10^6: 27 failures, all == 2 (mod 6),
  none in 0 or 4 mod 6.
status: checked
evidence: exact bytearray sieve program code/chen_goldbach/check.py, runs to
  10^7 (4.29 s), 10^8 (63.98 s), 10^9 (800.59 s), all finding first failure
  302 and no 4-mod-6 failure; the all-even failure census to 10^6
  (27 values, all == 2 mod 6) and the hardest-n diagnostics come from
  census_all_even. Independent trial-division oracle (oracle_check.py)
  confirms flags for p <= 200 and first failure 302 by its own scan <= 302.
  Independent sympy factorisation cross-route reproduces the exact 27-failure
  list <= 10^5. All arithmetic exact.
search-frame: the first-failure statement is bound-independent (the sweep
  stops at the first failure, so every run with B >= 302 finds 302). The
  4-mod-6 class is verified to 10^9. The all-even failure census is complete
  to 10^6 only: above 10^6 more 2-mod-6 failures may exist and were not
  swept (the all-even scan stops at 302, so n in (302, 10^9] other than the
  4-mod-6 class were never individually checked).
bears-on: research/backward/full-goldbach-via-exceptional-set.md
  G-structural-closure, candidate (d): the Chen-pair exceptional set is real,
  nonempty, and its first element is 302 == 2 (mod 6) — exactly the residue
  class candidate (d) predicted would need the repeated argument, while the
  Grimmelt–Teräväinen 4-mod-6 class stays clean to 10^9.
```

