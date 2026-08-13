# Tasks

## Directive 30 (steer): 6e8 run settles it — row 238 genuine, 15 giants, max gap 64, step 6 rephrased

**The 6e8 run (`code/out/pattern_finder_6e8_giants.captured.txt`) overturns
Directive 28/29.** Row 238 (0-based; 1-based row 239) lands at b=23,163,290
with flooring 8,161,173 — genuine, not capped. The 3e8 record capped it via
insufficient width; 6e8 resolves it. Row 248 (0-based 247; 1-based 248) is the
cap (flooring exactly 0). So the genuine set is **15 giants**, 0-based pre-jump
rows `[34,56,64,68,94,96,110,112,126,130,134,146,161,174,238]`, gaps
`[22,8,4,26,2,14,2,14,4,4,12,15,13,64]`, **max=64** (the 175→238 drought).
Parity: 14/15 even (only 161 odd), one-sided p = 16/2^15 = 4.9×10⁻⁴ —
stronger than the 13/14 figure. k*=248 at 6e8 (31.3M primes) — only 247 usable
rows. The reduction step 6 is rephrased: the condition needed is
**gap_i ≤ j_i + 1**, which holds with 2+ orders of margin (max ratio 0.0167,
at the largest gap 64 vs j=5,237,310). "Gap is bounded" is superseded by this
stronger and manifestly satisfied inequality.

### Immediate (in order)

- [ ] **1. Produce the ratio table (Directive 30 item 4).**
  Columns: 0-based giant pre-jump row, 1-based landing row, b_land, j_i,
  gap_i (to next giant), ratio gap_i/(j_i+1), flooring. 15 genuine giants
  from the 6e8 run (exclude row 248). Source:
  `code/out/pattern_finder_6e8_giants.captured.txt` (landing blocks, jumps,
  gaps, floorings all in the output). If every ratio < 1 with room, restate
  step 6 as the ratio bound and mark the old bounded-gap form superseded.
  Anchor: `code/out/directive30_ratio_table.md`.

- [ ] **2. Rephrase step 6 in `research/threads/regeneration.md`.**
  The conjecture needs Σ(j_i+1) ≥ k−2. This holds if each giant covers
  the distance to the next: gap_i ≤ j_i + 1. The 6e8 data shows max ratio
  0.0167 — two orders of slack, and j ~ b^0.388 grows while gaps grow far
  slower. Restate the step and mark "inter-giant gap is bounded" superseded
  by the ratio bound (which is both sufficient and verified to 15 giants).

- [ ] **3. Compute the width needed for the next genuine giant.**
  k*=248 at 6e8 (W=31,324,703 primes). At row 247 the block is ~31.3M;
  geometric growth factor ~1.75× puts the next landing block at ~55M.
  Width needed ≈ landing + row + headroom (~1000) → sieve roughly 9e8–1e9.
  Report the estimate in `research/threads/regeneration.md`.

- [ ] **4. Update CONTEXT.md Run state and Established sections.**
  Replace the Directive 28 run-state block with the 6e8 record: 15 genuine
  giants, max gap 64, row 238 genuine, k*=248, parity 14/15, step 6
  rephrased as ratio bound. Update the wider-width record in Established.

- [ ] **5. Downgrade claims asserting max=26 or "no trend."**
  `wider-width-giant-record-3e8` reports max=26 over the 14 live-at-3e8
  giants — it is now superseded by the 6e8 record (15 genuine, max=64).
  `directive25-gap-trend-and-reconciliation` claim: gap half now reads
  max=64, not 26. Update both. The parity claim
  `giant-parity-even-pre-jump-rows` updates from 14/15 to 14/15 (same count
  but row 238 is now proven genuine rather than capped — the 15th was always
  even, so the count is unchanged).

- [ ] **6. Hygiene: remove bare .txt duplicates in `code/pattern_finder/`.**
  `b.txt, bits.txt, diffs.txt, intruder.txt, jumps.txt, minima_b.txt,
  minima_rows.txt, regen_rows.txt, s.txt, s_runs0.txt, s_runs2.txt,
  b_genuine.txt` — 12 files. Canonical copies in
  `code/out/pattern_finder_outputs/`. `rm` the duplicates (coder role).
  Keep the `.py` scripts. `refresh_index` both folders.

- [ ] **7. Provability question (Directive 26 core, still open).**
  The ratio bound gap_i/(j_i+1) ≤ 0.017 being manifestly satisfied changes
  the question: proving the gap grows slower than the jump is what matters,
  and the geometric description (j ~ 1.75× per event, gaps ≤ 64 and at most
  slowly growing) makes this a comparison of growth rates. Is the geometric
  growth of b (and hence j) a consequence of anything known about primes, or
  is it a new statement? Three branches as before but now focused on the jump
  growth rate rather than gap boundedness.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal:** `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`; `b_k = b_1 + Σ_{i<k}(j_i+1) − (k−1)`. Zero failures on all 1,154 sweep sequences AND primes. `research/notes/step_law_proved.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified; combinatorial.
- **Recharge surplus (depth 1000):** S_k = b_k − b_1 + (k−1) = Σ(j_i+1), monotone, strictly increases exactly at (2,4)-events; S_1000 = 1,270,603 vs required 998. `code/out/surplus_renewal_structure.md`, `code/out/surplus_renewal_table.captured.txt`.
- **Bigjump characterisation (DONE, Directive 23):** 12/13 genuine, 1 capped (i=161 at 2e7). Claim `bigjump-cap-characterization-1000`. All caps resolved at wider widths.
- **6e8 giant record (DONE, Directive 30):** `code/out/pattern_finder_6e8_giants.captured.txt` — sieve 6e8, 31,324,703 primes, depth 400, 96.2 s. 15 genuine giants (0-based pre-jump rows [34,56,64,68,94,96,110,112,126,130,134,146,161,174,238]), gaps [22,8,4,26,2,14,2,14,4,4,12,15,13,64], max=64. Row 248 capped (flooring 0). k*=248. Parity 14/15 even (only 161 odd), p=4.9×10⁻⁴. Record max jump 12,508,030 (row 238). Geometric fit 15 giants: R²=0.968, factor 1.765/event.
- **Width-degradation caveat (DONE, Directive 24):** k*=162 (2e7), k*=239 (3e8), k*=248 (6e8). All genuine giants have flooring ≥ 8,161,173.
- **Geometric growth:** ×1.68 → ×1.75 → ×1.765 per event as width increased 2e7→3e8→6e8.
- **Lean 4 formalisation — COMPLETE** (Directive 17). Nine theorems, zero sorry, axiom footprint [propext, Classical.choice, Quot.sound]; IFF reformulation. Live claim `gilbreath-second-entry-equivalence`.
- **Conditional-rate experiment — DONE** (Directive 19). Pooled λ̂ ≈ 0.585, family-independent post-startup (p=0.68 over 8 families). **Mean rate superseded (heavy tail).**
- **CHT Theorem 1.6 hypothesis check — DONE:** M=7, L=2, R_0≈4.2e8 ≫ 1000; `holds-here: no`.
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000, sieve 2e7), `wider_width_b.json` (depth 240, sieve 3e8), `giants_6e8.json` (depth 400, sieve 6e8).
- **Library:** downloads halted; FRONTIER.md restored from commit db36fc23.

### Threads

- `research/threads/regeneration.md` — LIVE (Directive 30): 15 genuine giants, max gap 64, step 6 rephrased as ratio bound gap_i ≤ j_i+1 (holds with 2+ orders margin). Next: ratio table + provability question refocused on jump growth rate.
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).
