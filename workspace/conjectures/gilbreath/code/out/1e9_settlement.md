# 1e9 settlement — empirical route at ceiling

Directive 36 pivot. The 1e9 run (W = 50,847,534 primes, π(1e9), depth 400, 185s, 1.37 GiB)
doubled the width from 6e8 and **row-248 is STILL capped**.

## Four settled findings

1. **Row-248 is still capped.** b_land = 50,847,285 = W − 248 − 1, floor = 0,
   genuine = False. Its jump is now a lower bound of 27,684,003 (up from 8,161,172 at 6e8).
   The bound moved, the measurement did not. This is NOT a genuine giant — the block reaches
   the right edge of the finite row.

2. **Max gap is still 64.** The 239→248 gap of 9 is noise, so the 64 at 175→239 stands as
   the maximum over everything measured (depth 1000 at 2e7, 6e8, and 1e9).

3. **Ratio bound gap_i/(j_i+1) holds everywhere.** Max 1.2644e-02 at gap 22 vs j=1,314
   (giant 1, row 34→56); none above 0.1. This is the strongest empirical statement the run
   has — it survived two width doublings (6e8 → 1e9).

4. **Oracle passed.** Rows 1..247 reproduce the 6e8 record; rows 1..161 reproduce the 2e7
   depth-1000 record; mismatches = [].

## Why this is the ceiling

Geometric fit: log2(b_land) slope 0.070645, doubling every 14.16 rows, R² = 0.946 over
15 genuine giants. Gaps are 9 to 64 rows. So each giant costs 1.5× to 8× the width of the
last.

At 1e9 (50.8M primes, 1.37 GiB, 185s), the next genuine giant (row ~300) needs b ~55M,
requiring W ~55M + 300 ≈ 55.3M primes → sieve ~1.1e9 (fitting at ~1.5 GiB). But the one
after that (row ~364) needs b ~100M → W ~100M + 364 → sieve ~2.1e9 (~2.8 GiB). And the
one after that (row ~428) needs b ~180M → W ~180M + 428 → sieve ~3.8e9 (~5.1 GiB).
The 4th giant from now would need ~8+ GiB — the container cap.

And none of this settles the conjecture. Each run pushes a bound outward; the ratio bound
survives with 2+ orders of slack; the geometric growth is what it is. The empirical route
cannot reach the asymptotic regime, let alone prove anything.

## Parity correction (Directive 36)

The 1e9 capture's parity p-value counted all 16 giants including row 247 (genuine=False).
Recomputed on 15 genuine giants only:

- 1 odd 0-based row (161) of 15.
- Fair-coin p = (C(15,1) + C(15,0)) / 2^15 = 16/32768 = 4.883e-04.
- Base-rate p (against measured event rate 0.600): = 0.0052.
- Quote the base-rate figure, not the fair-coin one — the events are not fair coins.

## What remains

The theoretical work: Granville's ν_2 lower bound (Lemma 5.4, Theorem 5.5) and CHT
Theorem 1.6. Both full texts are in `research/sources/` as `*-FULLPDF.full.md` and have
not yet been read. A 2e9 or 4e9 sieve run should NOT be queued.