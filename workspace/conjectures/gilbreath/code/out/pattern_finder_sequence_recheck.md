# Pattern-finder sequence recheck (this pass)

Everything below is exact over the terms supplied (nu2_dense.txt, 30000 terms;
blocks_depth1000.json, 1000 block lengths; pattern_finder_outputs/ run-length
files; the ballot captures to 2.4e9 primes). Each regularity is a conjecture
(verified-numerically), not a proof; each is already filed in durable memory
except the one marked NEW.

## nu2(q_n) — the supply-side open content

- `find_linear_recurrence` (order ≤ 8): no constant-coefficient recurrence fits.
- `analyze_sequence`: not a low-degree polynomial (differences never constant).
- OEIS: no entry. (Miss already recorded in CONTEXT.)
- Flu. walk dev(n) = 2·nu2(n) − n, n=1..30000: max +558 at n=26840,
  min −639 at n=27625, min dev/sqrt(n) = −3.84, longest deficit run 15,
  final dev(30000) = +58. Matches stored record exactly (0 mismatch).

## NEW: increment process is heavy-tailed, not local

inc(n) = nu2(n+1) − nu2(n), n=1..29999:
- |inc| ≤ 1 on only 574/29999 = 1.91% of steps
- |inc| ≥ 50 on 15019/29999 ≈ half the steps
- range −468..+459; mean +0.501 (consistent with nu2 ~ n/2)
- most common increments {0,±1,±2,±3, 12,−13,−15} each ~200, but the walk is
  dominated by ~500-step jumps.

This is the structural reason no low-order recurrence/polynomial fits nu2: the
walk is a giant-step process, one value carries almost no information about the
next. It is a consequence of nu2 being the Hamming weight of XOR-folds of the
whole [2, n−1] gap window, which changes by O(n−window) at each n. Consequence:
no exact algorithmic handle on nu2; the surviving Route-B open content remains
the mod-4 switch-majority ballot e(n) ≥ 0 (below).

## Ballot e(n) ≥ 0 (mod-4 switch majority)

Verified in stored captures (fresh sieves):
- to 1e9 primes: min e = 1, zero dips = 0, final e = 5,193,722, min e/n = 0.10214
- to 2.4e9 primes: min e = 1, zero dips = 0, final e = 11,515,823, min e/n = 0.09858
The domain boundary term e(1) = −1 in W_switch_prefix_file is a boundary-index
artifact; the meaningful statement (n ≥ 3, where e = 3−4+... ) has min 0 there.
Conjectural; named-open at ABGS-2011-s9 (two-point mod-4 switch limit).

## Second-entry run-length sequences

s_runs0 (zero runs) and s_runs2 (two runs): no low-degree polynomial, no
constant-coefficient linear recurrence (order ≤ 8). Structurally random run
lengths.

## Block profile

b_k = A000232(k) − 1, already established (catalogued, verified k=1..16 and
corroborated to k≥265 via A000232 b-file). Local minima and record-maxima
sequences are thin (21 minima, 37 record maxima in 1000 rows) and match the
recorded minima era; not separately catalogued.

## Ledger state

Every regularity confirmed here is already in durable memory / CONTEXT.md. The
only genuinely new observation is the heavy-tailed increment structure above,
now stored. Nothing found here is not already held by the run; no sequence
showed structure the run had not already established.
