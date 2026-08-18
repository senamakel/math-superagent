# Index — code/chen_goldbach

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check.py` | All-even Chen-prime Goldbach checker: exact sieve/semiprime/Chen flags, scans every even n in [4,B] for a Chen pair p<=n/2 (p and n-p Chen), stops at first failure (302), reports hardest-n and the original 4-mod-6-only scan result over the same flags. Verified vs trial-division oracle and sympy cross-route. |
| `oracle_check.py` | Independent trial-division oracle for Chen flags: cross-checks the sieve's flags for p<=200, prints Chen primes up to 50, and independently scans all even n<=302 asserting first failure 302. Bounded oracle. |
| `__init__.py` | Package marker; empty. |

## What this folder attacks

Claim **G-structural-closure** in
`research/backward/full-goldbach-via-exceptional-set.md`: whether the
Grimmelt–Teräväinen exceptional set is empty in a verified finite range, and
how the all-even version behaves. This is evidence, not a proof — the
structural closure lemma is open.

The all-even sweep (every even n, 4 ≤ n ≤ B, must be a sum of two Chen
primes) finds its **first failure at n = 302** (≡ 2 mod 6), so the 4-mod-6
class is the one that stays clean and the failures live in the 2-mod-6 class.
See `code/out/chen_goldbach_all_1e9.md` and its fenced claim block.

## Runs (exact commands and outputs in `code/out/`)

- `python -m chen_goldbach.check 10000000` — bound 10^7: all-even first
  failure 302; 4-mod-6 class none; 1666667 tested; 4.29 s.
  Output: `code/out/chen_goldbach_all_1e7.txt`.
- `python -m chen_goldbach.check 100000000` — bound 10^8: all-even first
  failure 302; 4-mod-6 class none; 16666667 tested; 63.98 s.
  Output: `code/out/chen_goldbach_all_1e8.txt`.
- `python -m chen_goldbach.check 1000000000` — bound 10^9: all-even first
  failure 302; 4-mod-6 class none; 166666667 tested; 800.59 s.
  Output: `code/out/chen_goldbach_all_1e9.txt`.
- `python -m chen_goldbach.oracle_check` — trial-division oracle: flags match
  sieve for p ≤ 200, oracle's own all-even scan finds first failure 302.
  Output: `code/out/chen_goldbach_all_oracle_check.txt`.
- census and sympy cross-route: `code/out/chen_goldbach_all_census_1e6.txt`,
  `code/out/chen_goldbach_all_sympy_crosscheck.txt`.

Earlier 4-mod-6-only runs (before the all-even modification) found no failure
through 10^8; see `code/out/chen_goldbach_1e8.md` and
`chen_goldbach_1e6.txt`–`chen_goldbach_1e8_module.txt`.

The all-even modification does not change the 4-mod-6 computation: the
4-mod-6-only scan over the same flags reproduces "none" through each bound,
matching the earlier runs. The all-even first failure is 302 at every bound
(the sweep stops at the first failure, so the answer is independent of bound
once B ≥ 302). The 10^9 run answers that the Grimmelt–Teräväinen 4-mod-6
exceptional set contains no n with 4 ≤ n ≤ 10^9 — every such n is a sum of
two Chen primes — while the all-even statement has first failure 302. So the
theorem's 4-mod-6 restriction is genuine: failures concentrate in the 2-mod-6
class. Evidence toward G-structural-closure's candidate (d); the exceptional
set could still be nonempty above 10^9 and the structural lemma remains open.
