# Pattern-recognition scan — structural findings on the extracted sequences

Status of every claim below: **verified exactly over the real computed rows**
(`code/out/blocks_depth1000.json`, sieve 2e7 / 1,270,607 primes, depth 1000;
genuine regime k=1..161; giant table from the 1e9 run). None of the *sequence
structure* claims is a proof; each is labelled. Sequences were run through
`analyze_sequence`, `find_linear_recurrence`, GF(2)-recurrence testing, and
OEIS lookup.

## 1. Negative results — no catalogue / low-order structure to be had

The following sequences were both (a) run through the exact sequence tools and
(b) sent to OEIS. Result: **no constant-coefficient linear recurrence up to
order 8, no low-degree polynomial, no GF(2) linear recurrence up to order 12,
no eventual period up to length 500** — and, except for the two known
catalogue identities already established, **no OEIS entry**:

- `s_k` second entries (the conjecture object, {0,2}-valued). OEIS-lookup of
  `2,0,2,2,2,2,2,2` matches A080378/A036476/A340456/A341191 only by a
  coincidental 8-term prefix (all four are unrelated partition/prime-residue
  sequences); the run's own 105-term crosscheck against OEIS **A089582**
  (the genuine second-entry catalogue) confirms `s_k = A089582` exactly
  (`check_A089582_crosscheck.captured.txt`: 105/105, zero mismatches).
- `b_k` block profile (2,7,13,13,24,...). Catalogue identity
  `b_k = A000232(k) − 1` already established and confirmed term-by-term from
  the OEIS A000232 table. No further structure.
- regen-row gaps, jump sizes, giant rows, giant landing blocks, inter-giant
  gaps: all uncatalogued and no recurrence/polynomial/period.

**Recording decision**: none of these should be re-searched. The growth is
irregular at every order the tools can test, which is the honest pattern:
there is no low-order *arithmetic* lever in these sequences. The regularity is
elsewhere (below).

## 2. Confirmed exact regularities (checks of the real rows)

Reproduced and verified exactly over the genuine regime of `blocks_depth1000.json`:

- **Delta law / recharge surplus monotonicity.** With
  `S_k = b_k − b_1 + (k−1)`:
  `S_{k+1} − S_k = (b_{k+1} − b_k) + 1` at every transition (0 failures over
  k=1..160); `S_k` is nondecreasing; it increases at exactly 59 rows, which are
  precisely the (2,4)-events **including the jump-0 stalls** (b_{k+1}=b_k with
  intruder 4 and edge 2). `S_1 = 0`, `S_161 = 1,094,421`, `min S = 0`.
  → the recharge identity, already a proved theorem of the step law, holds
  with zero slack failure; the whole conjecture is `S_k ≥ k−2` = never
  returning the surplus to zero, and empirically the surplus only grows.
- **Edge/intruder step law at the 4-runs.** Every maximal run of intruder-4
  rows, in the genuine regime, regenerates (edge=2 at some interior row), or
  is cut off by the finite-width regime at k≥162. Matches the proved step law.
- **Giant intruder return.** After every genuine giant, the intruder returns
  to 4 within ≤12 rows (all 14 giants in the 1e9 table; the largest intruder
  54 at row 175 drains 6,4,4,...,→4 through the 48-row erosion run ending at
  row 223's regen).
- **Ratio bound.** `gap_i ≤ j_i + 1` and `gap_i/(j_i+1) ≤ 0.10` for all 15
  genuine giants; observed max ratio 0.0167 (row 34). Verified exactly.

## 3. Weak post-hoc effects (reported, not load-bearing)

- **Regen rows cluster at powers of 2**: 6 of the 8 powers of 2 in 1..161 are
  regen rows (1,2,4,8,64,128), hypergeometric p≈0.005; regen rows are
  even-skewed 30/43 (two-sided fair-coin p≈0.007). These are the same
  parity/power-of-2 effects already recorded (giant parity p=0.0052; Rule-90
  depth corollary closed as tolerance-dependent in CONTEXT.md). Post-hoc and
  not a mechanism; do not build on them.

## 4. Which regularity is most likely to yield a derivation

The single structural fact with hope is **not** an arithmetic sequence law but
the **monotone recharge surplus** of §2: `S_k = b_k − b_1 + (k−1)` is a proved,
exact, additive quantity that never decreases and increments only at
(2,4)-events. The conjecture is exactly "S_k − (k−1) never returns below 0".
Its growth to 1.09M by row 161, with min literally 0, means the block never
approaches its starting length again — the surest attack on regeneration is a
**lower bound on the (2,4)-event arrival rate** driving S, not any closed
form for the block/gap/jump sequences, which demonstrably have none at low
order.

## Fenced claim block

```claim
id: pattern-finder-no-loworder-plus-surplus
statement: (negatives) the second-entry, block-profile, regen-gap, jump, giant-row, giant-landing and inter-giant-gap sequences have no constant-coefficient linear recurrence of order <= 8, no low-degree polynomial, no GF(2) linear recurrence of order <= 12, and no eventual period up to length 500; OEIS confirms only the two known identities s_k = A089582 and b_k = A000232 - 1 (the block-profile OEIS miss already recorded). (positives, all exact over k=1..161) S_k = b_k - b_1 + (k-1) satisfies S_{k+1} - S_k = (b_{k+1}-b_k) + 1, is nondecreasing, increases at exactly the (2,4)-events including jump-0 stalls (59 in the genuine regime), S_1=0, S_161=1094421; every maximal intruder-4 run regenerates (or is cut off by finite width); after every genuine giant the intruder returns to 4 within <=12 rows; gap_i <= j_i+1 and gap_i/(j_i+1) <= 0.10 over all 15 giants (max 0.0167). Hypothesis-free over the stated rows.
hypotheses: rows are iterated absolute differences of the primes below sieve bound; genuine regime k=1..161; giant table from 1e9 run.
holds-here: yes (exact, depth 1000 genuine regime; giants to 1e9)
status: checked (exact over supplied rows) — the negatives and regularities are verified numerically, not proved for all k; the S monotonicity/equivalent-conjecture form is a proved theorem of the step law.
bearing: the one exploitable structure is the monotone surplus S (proved form of the recharge identity => GC iff S_k >= k-2 for all k); the low-order arithmetic levers are all empty and should not be re-searched.
anchor: code/out/pattern_finder_gf2_recurrence.py; code/out/check_A089582_crosscheck.py; this note.
```
