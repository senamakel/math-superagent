```thread
question: Why does a fresh {0,2} block always reappear before the current one is exhausted by erosion?
status: open — consumption proved and sourced, regeneration empirically non-local and now sourced non-local; obstruction pinned by CHT inverse theorem
rests-on: |
  - Reduction proved (A_k(1) ∈ {0,2} ⇔ conjecture), checked to depth 599
  - Consumption proven & sourced: Odlyzko 1993 block lemma (length-N {0,2} block → N+1 rows start 1, constant 1); Killgrove–Ralston 1959 same; Chase 2024 Lemma 3.2 ({0,d}-block length L ⇒ max drops by 1 after L rows). Block l length → l−1 per row.
  - Block profiles to depth 1000 (code/out/blocks_depth1000.json); minima [13,24,96,97,175,2762,...] grow, never reach 0
  - Regeneration is NON-LOCAL — empirically refuted (check_regenerate_lemma: no single-row iff from intruder+length), and NOW SOURCED: Muney 2026 (arXiv:2606.23721) proves K_S and K_S=C_S are governed by the WHOLE ordered right anti-diagonal via the folding map F_S, k∈K_S ⟺ F_S(|k−s_n|)=1, and K_S=C_S ⟺ e_i≤1+Σ_{j>i}e_j (order-sensitive Brown criterion). Confirms empirically-regeneration is not a single-row property.
  - CHT 2026 Theorem 1.6 (deterministic inverse): the ONLY obstructions to decay are long zero-blocks or long shallow {0,d}-blocks (d≥2); Theorem 1.3 random-analogue needs only 2-separated non-concentration.
blocked-by: the mechanism of regeneration has not been stated; Muney gives the correct global object (folding composition F_S and its fiber over 1) but not an a priori bound ruling out the two CHT obstructions for the primes.
next: |
  1. Convert the empirical minima data into the honest claim (no k with block length 0 computed; nothing proves it).
  2. Link the two obstructions (CHT 1.6) to block length: a regeneration failure requires a long zero-block or long shallow {0,d}-block; measure how close real prime rows come to these on the depth-1000 data (0-block lengths, {0,d}-block lengths vs the R_m thresholds).
  3. The {0,2}-regeneration is NOT a single-row local property (Muney sourced + run refutation): frame regeneration as a statement about the right anti-diagonal folding composition F_S and its fiber over 1 — the correct global object.
  4. Treat Muney's e_i≤1+Σ_{j>i}e_j (interval-completeness) as a candidate structural invariant for the anti-diagonal of a row entering the {0,2} regime; check it on the real rows and see whether prime rows near the depth-1000 minima satisfy it.
```

# Regeneration thread

## What we know

- **Consumption is proven & source-backed.** Odlyzko 1993 (block lemma, constant 1); Killgrove–Ralston 1959 (same, off-by-one index); Chase 2024 Lemma 3.2 ({0,d} version). A leading {0,2} block of length b_k implies b_{k+1} ≥ b_k − 1 — the block shrinks by at most one per row. Regeneration is the sole remaining obstruction.

- **Regeneration is NOT local — now sourced.** The run's `check_regenerate_lemma` empirically refuted any single-row iff for regeneration. Muney 2026 (arXiv:2606.23721) gives this a proof-level foundation: the valid-extension set K_S of a Gilbreath prefix S is determined by its **entire ordered right anti-diagonal** through the folding composition `F_S(d) = ||…||d−e_1|−e_2|…−e_{n−1}|`, with `k∈K_S ⟺ F_S(|k−s_n|)=1`, and `K_S = C_S` iff `e_i ≤ 1 + Σ_{j>i} e_j` for all i (Theorem 20). A single-row/leading-block quantity cannot determine this — confirming the empirical refutation and supplying the correct global object.

- **The only obstructions are now pinned.** CHT 2026 Theorem 1.6 (deterministic inverse): if initial data a_n ≤ 2^M, no length-L zero-block, and no long shallow {0,d}-block, then the left diagonal is {0,1}-valued. So for the input to the primes, a regeneration/GC failure must be mediated by a long zero-block or a long shallow {0,d}-block. Both are heuristically rare but unproved absent (even under Hardy–Littlewood).

## Two sharp facts from the data

### Fact (a): Block length never approaches 0 — minima grow
Minima over depth 1000: `[13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263]`. Smallest block length after row 3 is **13**; minima grow rapidly. Strong numerical evidence the conjecture holds; not a proof.

### Fact (b): Regeneration is real but NOT monotone
`97→96`, `871→872`, `21→24` occur; consumption and regeneration alternate; longest genuine live-regime erosion run 13 rows (the 838-row run is a finite-width artifact).

## The honest open question

**Is there a k with block length 0?** Everything computed says no (min block ever seen = 13). Nothing proves it.

## What must be explained

For regeneration to fail, a row k must reach small block length with the rows below failing to regenerate a fresh {0,2} block before b hits 0. The data + sources say:
1. Regeneration is NOT local — single-row iff dead (empirical refutation + Muney's sourced global criterion).
2. The CHT inverse theorem reduces failure to two concrete structures (long zero-blocks, long shallow {0,d}-blocks) — measure these on the real rows.
3. Muney's `e_i ≤ 1 + Σ_{j>i} e_j` interval-completeness criterion is the natural structural invariant to try on the anti-diagonals of rows that successfully regenerate.

## Data available
- `code/out/witnesses.json` (depth 600); `code/out/blocks_depth1000.json`; `code/out/regeneration_analysis.captured.txt`; `code/out/check_regenerate_lemma.captured.txt` + `.notes.md`.
- Sources: Odlyzko 1993, Killgrove–Ralston 1959, Chase 2024, CHT 2026, Muney 2026, Eppstein 2011 anti-Gilbreath.
