# CHT Theorem 1.6(iii): right-half {0,d}-block scan on the real primes

**Date:** this run. **Program:** `code/cht/scan_right_half_0d.py`.
**Sieve:** primes <= 6e8, W = 31,324,703 primes, N = 31,324,701 normalized
gaps. **Depth:** 401 rows (i = 0..400). **Wall:** 196 s, one row live at a
time, exact int64.

## Theorem 1.6(iii), verbatim (column restriction)

CHT 2026 (arXiv:2607.08712) Theorem 1.6, axiom (iii):

> There does NOT exist `1 <= m <= M`, `2^{M-m} < d <= 2^{M-m+1}`,
> `0 <= i <= 2 R_{m-1}`, `k >= R_m - 3 R_{m-1}`, `N' <= j <= N-i-k`, with
> `a(i,j), ..., a(i,j+k-1) in {0,d}`.

So the `{0,d}`-block obstruction (d >= 2) is confined to **columns j >= N'** —
the RIGHT HALF — and the run's own leading `{0,2}` block at j = 1 never
violates (iii). This scan measures the longest `{0,d}`-blocks (d >= 2) that
actually occur in the right half of the real prime array and compares them
against the CHT length thresholds `R_m - 3 R_{m-1}`.

## Coordinates

CHT row 0 = normalized gaps `a_n = (p_{n+2}-p_{n+1})/2 - 1`, n = 1..N.
The run's triangle satisfies `A_{i+1}[j] = 2*a(i,j)` for j >= 1 (verified on
the first 1e5 primes: oracle_halving = True), so a `{0,d}`-block in CHT row i
is a `{0,2d}`-block in run row i+1; d = 1 (run `{0,2}`) is OUTSIDE (iii) and
reported as category C for contrast. Category A = d in [2, 2^M] (the values
(iii) controls), B = d >= 2 (all), C = d == 1.

## Thresholds at this sieve

- max a_n = 140 -> M = 8 (2^8 = 256), L = longest 0-run = 2
  (provably exact: p, p+2, p+4 cannot all be prime).
- R_0 = 100*L*8^M = 3,355,443,200 ~= 3.36e9.
- T_m = R_m - 3 R_{m-1}: smallest is T_1 = R_1 - 3 R_0
  = 5.63e16. Every CHT length threshold exceeds the width of the whole
  finite array (W = 3.13e7) by more than nine orders of magnitude.

## Result

**Longest right-half {0,d}-block with d >= 2 at any depth <= 400: length 25**
(row i = 14, d = 2, columns 21,306,115..21,306,139, 0-based in CHT). The
top-15 list is lengths 25,24,24,23,23,... all at d in {2,4,8,9,13,14}. The
longest d >= 4 block is length 24 (row 37, d = 14). Blocks with d >= 2 occur
in 247 of the 401 rows, but every one is microscopic against T_1 = 5.6e16.

Category C (d = 1, run {0,2}, outside (iii)) reaches length 15,662,105 at
row 247 — the run's own leading block, sitting at the far LEFT, which is
exactly why it does not trigger the theorem.

## Verdict: holds-here = no, now with the column restriction resolved

- (iii) is restricted to the right half; the leading {0,2} block at j=1 is
  not a violation — CONFIRMED (it is category C).
- In the right half itself, the longest {0,d}-block (d >= 2) observed is 25,
  vs the smallest CHT threshold T_1 = R_1 - 3 R_0 = 5.63e16. **The gap is
  ~2.25e15x.** The {0,d}-block family of obstructions is not present at any
  length the theorem controls, in the half of the array where it would
  matter.
- (iii)'s depth scope i <= 2 R_{m-1} >= 6.7e9 rows is also far beyond reach
  (this run: 400), so the depth part of the axiom cannot even begin to be
  violated at reachable depths.

The theorem does not bite at reachable depths, and the right-half scan
confirms the obstruction family it names is absent at any threatening scale.

```claim
id: cht-right-half-0d-scan-6e8
statement: On the real prime array at sieve 6e8 (W = 31,324,703 primes,
  N = 31,324,701 normalized gaps, max a_n = 140 -> M = 8, L = 2,
  R_0 = 100*L*8^M = 3,355,443,200), scanning all 401 rows (depth i = 0..400)
  of the CHT array restricted to the right half (columns j >= N' =
  floor(N/2)), the longest {0,d}-block with d >= 2 has length 25 (row 14,
  d = 2, columns 21306115..21306139); the longest with d >= 4 has length 24
  (row 37, d = 14); d >= 2 blocks occur in 247 of 401 rows; the smallest CHT
  length threshold T_1 = R_1 - 3 R_0 = 5.63e16 exceeds every observed block
  by a factor >= 2.25e15. The d = 1 blocks (the run's leading {0,2} block,
  category C, outside (iii)) reach length 15,662,105 at row 247 but sit at
  columns j < N'.
hypotheses: CHT Theorem 1.6(iii) restricts {0,d}-blocks (d >= 2) to columns
  j >= N', depth i <= 2 R_{m-1}, length k >= R_m - 3 R_{m-1}; the scan covers
  all depths reachable in this run (i <= 400) and the full right half of
  every row (column coordinate ranges exactly as in the source).
holds-here: no — the right-half {0,d}-block obstruction is absent at any
  length the theorem controls (observed max 25 vs threshold 5.63e16, a
  2.25e15x gap), so axiom (iii) is not violated and cannot be the reason the
  inverse theorem fails to bite; it simply never comes into play at
  reachable depths.
status: checked — exact integer arithmetic, one row live at a time; three
  oracle checks passed: (1) naive expand-around-d scan agrees with the
  compressed-scan method on 200 random small rows; (2) A_{i+1}[j] = 2*a(i,j)
  halving correspondence verified on the first 1e5 primes; (3) b-profile
  (leading {0,1}-prefix length of each CHT row) matches the stored records
  from the 2e7 depth-1000 and 6e8 giant runs with ZERO mismatches over all
  400 rows.
bearing: closes TASKS Directive 35 item 1. CHT Theorem 1.6 does not apply to
  the prime rows at any reachable depth, and the right-half {0,d}-block
  obstruction — the only part of (iii) the leading-block position does not
  already trivially satisfy — is empirically absent at every threatening
  scale. The CHT deterministic route (Route C) is calibrated: the theorem's
  bite is out of range, matching the authors' own difficulty assessment; the
  run stays on Route B (Granville nu_2) as primary.
anchor: code/out/cht_right_half_0d_scan.captured.txt,
  code/out/cht_right_half_0d_scan_6e8.json,
  research/sources/chase-hunter-tao-2026-full-html.full.md (Theorem 1.6)
```

## What a bigger run would settle

- Extending to depth ~10^4-10^5 at a wider sieve would test whether any
  deeper row produces a right-half {0,d}-block with d >= 2 longer than ~25
  (i.e. whether the observed lengths drift upward with depth). The CHT
  thresholds are so far above any finite array width that this is a
  statistical question about the run's rows, not a route to the theorem's
  hypotheses.
