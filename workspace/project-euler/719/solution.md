# PE 719 — Number Splitting: derivation

## Result the method rests on (definitional reduction)

An S-number is `n = m^2` whose decimal digit string splits into `k >= 2`
contiguous blocks summing to `m = sqrt(n)`. Therefore every S-number is
determined by its **root m**, and testing whether `m` is a valid root depends
only on the digit string of `m^2`.

**Reduction:** instead of scanning all `n <= N` (here `N = 10^12`, i.e. 10^12
candidates), scan only the roots `m` with `2 <= m <= isqrt(N)`. This cuts the
work from N to `sqrt(N) = 10^6`, a factor of a million.

## Why the single-block case is excluded cleanly

The statement requires splitting into **2 or more** parts. For `m >= 2`,
`m^2 = m` holds only for `m in {0, 1}`, so for every root we test the trivial
one-block partition can never accidentally be the only success — any valid
partition is automatically 2+ blocks. `n = 1` (root `m = 1`) is the only S-shape
whose only partition is single-block, so starting the loop at `m = 2` correctly
excludes it. This is confirmed by the oracle `T(10^4) = 41333`: if 1 were
included the sum would be 41334.

## The digit-partition test

Given root m and its square's digit string `s = str(m^2)` (length L <= 13 for
N = 10^12; actually m <= 10^6 => m^2 <= 10^12 has <= 13 digits), decide whether
a left-to-right split of the digits into blocks sums to m.

Recurrence (exact integer, memoised):
`expr(target, i)` = "can the suffix s[i:] be split into one or more blocks
summing to target?" with
- `expr(target, i) = True` if `target == int(s[i:])` (whole suffix as one block), and
- `expr(target, i) = any(expr(target - int(s[i:j]), j) for j in i+1..L)`.

The top-level call forces the first block to be a proper prefix (`j` from 1 to
L-1) so the total partition has >= 2 blocks:
`partition_matches(m) = any(expr(m - int(s[:j]), j) for j in 1..L)`.

This is exactly the `expr` recursion used in the OEIS A038206/A104113 program
(Michael S. Branicky, 2021).

## Complexity

- O(sqrt(N)) roots tested. For each, the digit string has at most 13 digits,
  so the partition search explores at most 2^12 = 4096 cut patterns; memoised
  recursion makes each test cheap. Total is comfortably sub-second for
  N = 10^12. Space O(1) beyond the memo per test (memo discarded each m).
- No floating point anywhere; `m*m` and block integers are exact.

## Why the brute-force alternative is the wrong method at full size

Scanning all n <= 10^12 and factoring/checking each is 10^12 trials — the
stated bound defeats it. The structural fact that makes it unnecessary is that
an S-number is *determined by its root*, so the answer space collapses from
`[0, 10^12]` to `[2, 10^6]`.

## Verification strategy

1. **Oracle:** brute.py scans every n (via roots) and tests all partitions two
   independent ways (set-of-cuts enumeration and the recursion). It must
   reproduce T(10^4) = 41333 and agree with solution.py on every N it can reach
   (e.g. 10^4, 10^5, 10^6).
2. **Full size:** solution.py computes T(10^12).
3. **Second independent route:** the OEIS A104113 b-file lists S-numbers
   directly; verify that the sum of b-file terms <= some bound matches
   solution.py's cumulative sums up to that bound, and that no S-number
   <= 10^12 is missing from the b-file's stated range. (b-file here runs to
   408+ terms; the full A038206 b-file runs to 3200 roots, far beyond
   sqrt(10^12) = 10^6.)
