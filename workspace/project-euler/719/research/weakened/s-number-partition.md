# Weakened ladder — S-numbers (PE 719)

The full problem: an S-number is a perfect square n whose square root is
obtainable by splitting n's decimal string into 2+ contiguous parts and summing
them; T(N) is the sum of S-numbers ≤ N; find T(10^12).

This ladder climbs by re-enabling one difficulty at a time. The structural fact
under the top rung is already in the statement: n ≤ 10^12 and n = m² forces
m = √n ≤ 10^6, so enumerating *roots* replaces a 10^12-scan over n with a
10^6-scan over m. That bijection is what `n-enumeration` (below) stands for.

```ladder
goal: T(10^12), the sum of all S-numbers n ≤ 10^12 (PE 719)
difficulties: N-scale, n-enumeration, split-search, part-rule, sum-dedup
status: exhausted
```

Difficulty glossary (each `off` field refers to these exact tokens):

- `N-scale` — the magnitude of the bound. Full problem: N = 10^12, so n has up
  to 13 digits and there are up to 10^6 square roots. *Off* means N ≤ 10^4 or a
  handful of fixed cases.
- `n-enumeration` — the problem is posed as a sum over n ≤ N, so the naive
  method costs O(N); at N = 10^12 that is 10^12 candidates and infeasible. The
  escape is the bijection n ↦ m = √n (n = m² is a perfect square), covering
  exactly the squares with 10^6 roots. *Off* means N is small enough that
  scanning n directly is cheap.
- `split-search` — for fixed n = m² with d digits, deciding whether *some*
  partition of the d-digit string into contiguous parts sums to m; naive cost
  is 2^(d−1) cut sets, so it needs pruning/DP. *Off* means the split is fixed
  and handed to us.
- `part-rule` — the exact validity of a split: at least 2 parts, each a
  contiguous block; and whether a zero-padded part like "01" counts. The
  examples force a single "0" part (98+0+1) but not a zero-padded multi-digit
  part. *Off* means no ambiguity: exactly 2 parts, no zero-padded parts.
- `sum-dedup` — each S-number counts once in T(N) even with several witnesses
  (8281 has two), and the sum is over n, not over splits. *Off* means a single
  number, no summation.

```rung
id: R-1
statement: Verify that n = 81 is an S-number, with the split 8|1 fixed a priori (no search over cut positions, no leading-zero question, no summation).
off: N-scale, n-enumeration, split-search, part-rule, sum-dedup
stance: settled
merge: turning split-search back on: allow every cut set of the digit string rather than one fixed split. First move: the same decision over the four named examples, R-2.
```

```rung
id: R-2
statement: Verify each of n = 81, 6724, 8281, 9801 is an S-number, searching all splits of the digit string into ≥2 contiguous parts; note 8281 has two witnesses (8+2+81 and 82+8+1).
off: N-scale, n-enumeration, sum-dedup
stance: settled
merge: turning sum-dedup back on: scan every n ≤ 10^4 and keep each S-number once in a sum even when several splits witness it. First move: direct enumeration + exhaustive split test, check T(10^4) = 41333, R-3.
```

```rung
id: R-3
statement: T(10^4) = 41333, computed by direct enumeration over all n ≤ 10^4 with an exhaustive split test on each perfect square, each S-number summed once.
off: N-scale, n-enumeration
stance: settled
merge: turning N-scale back on to 10^6: the identical enumeration and split test at 100× the candidates, still no root parametrization needed. First move: run the R-3 brute at N = 10^6, R-4.
```

```rung
id: R-4
statement: T(10^6), computed by direct enumeration over all n ≤ 10^6 with the same exhaustive split test (10^6 candidates, digit strings ≤ 13 digits), each S-number summed once.
off: n-enumeration
stance: settled
merge: turning n-enumeration back on: at N = 10^12 an O(N) scan over n is infeasible, so switch to the bijection n = m² with m = √n ≤ 10^6 and test each m². First move: implement the root loop m → m² → split test, and confirm it agrees with R-4's value at N = 10^6, R-5.
```

```rung
id: R-5
statement: T(10^12): sum every S-number n ≤ 10^12 by enumerating square roots m ≤ 10^6, testing each n = m² for a partition of its decimal digits into ≥2 contiguous parts summing to m, and summing each n once.
off:
stance: settled
merge: none — this is the full-strength goal and it is settled; the ladder is exhausted. The result T(10^12) = 128088830547982 is two-verified (recursion route vs. OEIS A038206 b-file route, both reproducing T(10^4) = 41333).
```

Notes to the forward loop:

- R-1 and R-2 are `settled` by this run's own code, not merely by the
  statement's examples: `code/brute.py` prints `81 True`, `6724 True`,
  `8281 True [('8','2','81'),('82','8','1')]`, `9801 True` (code/out/commands.log).
- R-3 is `settled` by two independent routes in `code/out/commands.log`:
  `brute.py` prints `T(10000) = 41333 (9 S-numbers)`, and the recursive route
  `T_rec` also gives 41333. The S-number set ≤ 10^4 matches the claim
  `snumber-sum-oracle` exactly: {81,100,1296,2025,3025,6724,8281,9801,10000}.
- R-4 is `settled`: `brute.py T(10^6)` prints `10804656`, and `T_rec(10^6)`
  agrees (`N 1000000 enum 10804656 rec 10804656 agree True`).
- R-5 is `settled` (this is what closed the ladder). Two independent routes
  agree on T(10^12) = 128088830547982: (a) `code/solution.py`'s root-scan
  digit-partition recursion, and (b) `code/verify_bfile.py` summing m² over the
  OEIS A038206 b-file roots with 2 ≤ m ≤ 10^6. Both reproduce T(10^4) = 41333,
  confirming the earlier off-by-one (the b-file sentinels m = 0,1) was fixed.
  This is recorded as claim `t-final-answer` with evidence `checked`
  (anchor code/out/final_answer.md).
- The difficulty that actually bit was `part-rule`, specifically its boundary
  clause: the "at least 2 parts" rule is what excludes n = 1, and the first
  b-file route tripped over it by summing the sentinels m = 0,1 (giving 41334
  instead of 41333 at N = 10^4, and a 1-too-high T(10^12)). Filtering to
  m ≥ 2 fixed it. `split-search` was the performance trap over 10^6 roots,
  handled by the recursive prune / digit-partition, not by any novel theory.
