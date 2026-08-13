```thread
question: Why does a fresh {0,2} block always reappear before the current one is exhausted by erosion? (Is there a k with block length 0?)
status: open — consumption proved and sourced; regeneration is a LOCAL criterion (edge-2/intruder-4, checked exactly to depth 1000) but its availability is not proved; CHT inverse theorem pins the only obstructions
rests-on: |
  - Reduction proved (A_k(1) ∈ {0,2} ⇔ conjecture), checked to depth 599
  - Consumption proven & sourced: Odlyzko 1993 block lemma (length-N {0,2} block → N+1 rows start 1, constant 1); Killgrove–Ralston 1959 same; Chase 2024 Lemma 3.2 ({0,d}-block length L ⇒ max drops by 1 after L rows). Block length b_k → b_{k+1} ≥ b_k − 1.
  - REGENERATION IS LOCAL (run's own corrected computation): b_{k+1} ≥ b_k ⟺ (A_k[b_k]==2 and A_k[b_k+1]==4), zero failures over all 998 transitions k=1..999 (sieve 20M, depth 1000); exactly 60 regeneration events (matching the independent long-standing count). The earlier "refutation" was an off-by-one edge-index bug (e_k=A_k[b_k−1] instead of A_k[b_k]) and has been withdrawn (code/out/check_regenerate_lemma.notes.md).
  - Block profiles to depth 1000; minima [13,24,96,97,175,2762,5939,31525,31533,31534,733574,1094263] never reach 0
  - Muney 2026 (arXiv:2606.23721): the FULL valid-extension set K_S is governed by the whole ordered right anti-diagonal (folding map F_S; K_S=C_S ⟺ e_i≤1+Σ_{j>i}e_j). This is a DIFFERENT, global question — orthogonal to the local block-regeneration criterion; no contradiction.
  - CHT 2026 Theorem 1.6 (deterministic inverse): the ONLY obstructions to decay are long zero-blocks or long shallow {0,d}-blocks (d≥2); Theorem 1.3 random-analogue needs only 2-separated non-concentration.
blocked-by: the local criterion (edge 2 + intruder 4) is checked to depth 1000 but not PROVED for all k; and even as a proven law it only says when regeneration CAN happen, not that it happens before b_k reaches 0 (its availability/frequency is unproved).
next: |
  1. State the honest open question as: is there a k with block length 0? Nothing computed says yes (min block ever seen = 13); nothing proves no.
  2. The local criterion being exact makes regeneration a well-defined event with computable rate at each row; turn the depth-1000 statistics (how often (e,c)=(2,4) occurs at regenerations, 60 events) into a lower-bound argument if possible.
  3. Measure the CHT-1.6 obstructions on the real rows (longest zero-blocks, longest shallow {0,d}-blocks vs the R_m thresholds) to see how far the prime rows are from the failure regime.
  4. Muney's folding-map/fiber formalism is the correct global object for the extension-set question; keep it separate from the local regeneration criterion.
```

# Regeneration thread

```claim
id: regeneration-criterion-local-exact
statement: In the prime Gilbreath triangle, let the leading {0,2} block of row A_k occupy 0-based columns 1..b_k, and define the edge e_k = A_k[b_k] (the last {0,2} entry of the block) and the intruder c_k = A_k[b_k+1]. Then b_{k+1} >= b_k  iff  (e_k == 2 and c_k == 4). Equivalently the first non-{0,2} value q_k = A_{k+1}[b_k] = |e_k - c_k| is in {0,2} iff (e_k,c_k)=(2,4).
hypotheses: A_0 = primes (or any 2-then-odds sequence with even gaps >= ... ); c_k >= 4 by definition of intruder (first value past the {0,2} block, which has only even values and is not 0 or 2). b_k = length of the leading {0,2} block, positions 1..b_k.
holds-here: yes - zero failures over all 998 transitions k=1..999 (sieve to 20,000,000, depth 1000); exactly 60 regeneration events, matching the independent long-standing count; both directions.
status: proved (finite identity: q_k = |e_k-c_k| in {0,2} iff (e_k,c_k) = (2,4), since c_k >= 4 even; and b_{k+1} >= b_k iff q_k in {0,2} by definition of block length)
bearing: regeneration is a single-row local property (edge==2 AND intruder==4) - the earlier CONTEXT.md "Ruled out" row claiming regeneration is not local was an off-by-one (e_k = A_k[b_k-1]) and is WITHDRAWN. The honest open question is purely frequency: how often (e==2,c==4) recurs before erosion (b shrinks by exactly 1 per non-regen row) drives b to 0. Minima record to depth 1000: 13,24,96,97,175,2762,5939,31525,31533,31534,733574,1094263 - never 0.
answers: is-regeneration-local
anchor: code/out/check_regenerate_lemma.captured.txt (Variant B), code/regeneration/check_regenerate_lemma.py, research/threads/regeneration.md
```

## What we know

- **Consumption is proven & source-backed.** Odlyzko 1993 (block lemma, constant 1); Killgrove–Ralston 1959 (same, off-by-one index); Chase 2024 Lemma 3.2 ({0,d} version). A leading {0,2} block of length b_k implies b_{k+1} ≥ b_k − 1 — the block shrinks by at most one per row. Regeneration is the sole remaining obstruction.

- **Regeneration IS a single-row local property — established by the run's own corrected computation.** With the correct edge index e_k = A_k[b_k], the criterion
  `b_{k+1} ≥ b_k  ⟺  (A_k[b_k] == 2 and A_k[b_k+1] == 4)`
  holds with **zero failures over all 998 transitions** (k=1..999, sieve 20M / 1.27e6 primes, depth 1000), and exactly 60 regeneration events (matching the independent count). The old claim that regeneration is "not local" came from an off-by-one edge-index bug and has been **withdrawn** (`code/out/check_regenerate_lemma.notes.md`; claim `regeneration-lemma-edge-2-intruder-4-established`, status checked).

- **Muney 2026 (arXiv:2606.23721) governs the full valid-extension set — a different, global question.** K_S (which integers can be appended while every row's leading entry stays 1) is governed by the whole ordered right anti-diagonal via the folding composition F_S: k∈K_S ⟺ F_S(|k−s_n|)=1, and K_S=C_S iff e_i≤1+Σ_{j>i} e_j (Theorem 20). This does NOT contradict the local regeneration criterion: the set of admissible next values is global, but whether the block *grows* when a particular next value is chosen is local. Both facts stand; neither subsumes the other.

- **The only obstructions are now pinned.** CHT 2026 Theorem 1.6 (deterministic inverse): if initial data a_n ≤ 2^M, no length-L zero-block, and no long shallow {0,d}-block, then the left diagonal is {0,1}-valued. A GC failure must be mediated by a long zero-block or a long shallow {0,d}-block; both are heuristically rare but unproved.

## Two sharp facts from the data

### Fact (a): Block length never approaches 0 — minima grow
Minima over depth 1000: `[13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263]`. Smallest block length after row 3 is **13**; minima grow rapidly. Strong numerical evidence the conjecture holds; not a proof.

### Fact (b): Regeneration is real but NOT monotone
`97→96`, `871→872`, `21→24` occur; consumption and regeneration alternate; longest genuine live-regime erosion run 13 rows (the 838-row run is a finite-width artifact).

## The honest open question

**Is there a k with block length 0?** Everything computed says no (min block ever seen = 13). Nothing proves it.

## What must be explained

For regeneration to fail, a row k must reach small block length with the rows below failing to hit the (edge-2, intruder-4) regeneration configuration before b hits 0. The data + sources say:
1. Regeneration has an exact local criterion (edge 2, intruder 4) — checked to depth 1000, not proved for all k, and its availability at small block lengths is unmeasured as a theorem.
2. The CHT inverse theorem reduces failure to two concrete structures (long zero-blocks, long shallow {0,d}-blocks) — measure these on the real rows.
3. Muney's `e_i ≤ 1 + Σ_{j>i} e_j` interval-completeness criterion is the natural structural invariant for the full extension-set question; keep it separate from the local regeneration law.

## Data available
- `code/out/witnesses.json` (depth 600); `code/out/blocks_depth1000.json`; `code/out/regeneration_analysis.captured.txt`; `code/out/check_regenerate_lemma.captured.txt` + `.notes.md` (criterion ESTABLISHED, refutation withdrawn).
- Sources: Odlyzko 1993, Killgrove–Ralston 1959, Chase 2024, CHT 2026, Muney 2026, Eppstein 2011 anti-Gilbreath.