# Tasks

## Directive 31 (steer): make the keystone auditable, and clear the unrun pile

### Immediate (in order)

- [ ] **1. Re-emit `lean_reduction.captured.txt` so it proves something on its own.**
  `code/out/lean_reduction.captured.txt` is **zero bytes** — identical to a command
  that never ran, yet INDEX.md calls it "lean compile of the repaired reduction
  lemma file (EXIT=0, clean)." After compiling `code/lean/reduction.lean`, add
  `#print axioms <theorem name>` for every theorem in that file, capture stdout,
  and also echo `lean --version` and `sha256sum` of the source file so the
  artifact identifies what was compiled. If `lean` is unavailable in the
  container, say so and downgrade any claim that rests on this file to
  `asserted`.

  **Note:** the main claim `gilbreath-second-entry-equivalence` correctly anchors
  to `lean_gilbreath_reduction.captured.txt` (1028 bytes, full `#print axioms`
  ledger with all 9 theorems, non-empty). The empty `lean_reduction.captured.txt`
  is the separate compilation of just `code/lean/reduction.lean` — it is a broken
  artifact regardless, and INDEX.md must not call it evidence of anything.

- [ ] **2. `lean_shape.captured.txt` check.**
  It is 147 bytes (non-empty, shows `shape_theorem` and `shape_iter` axioms).
  The directive says "Same for `lean_shape.captured.txt` if it is empty too" —
  it is not empty, so skip. Confirm in the task note.

- [ ] **3. Clear the unrun `.py` pile in `code/out/`.**
  The directive lists 12 `.py` files with no matching `.captured.txt`.
  Cross-check against the actual directory (some now have captures:
  `runner1.py` → `runner1.captured.txt` 176B, `verify_c1.py` →
  `verify_c1.captured.txt` 54B, `check_window_range_empirical.py` →
  `check_window_range_empirical.captured.txt` 116B). The genuinely uncaptured
  set is: `check_three_candidates.py`, `check_three_candidates2.py`,
  `check_window_range_allcells.py`, `check_window_range_empirical2.py`,
  `final_run.py`, `final_run2.py`, `_run_edge.py`, `runner2.py`, `runner3.py`
  — 9 files. `exec.sh` covers only `final_run.py` and `final_run2.py`.
  
  **Do:** extend `exec.sh` with `timeout 540 python3 ... 2>&1 | tee` for all 9,
  run it, capture every output in `code/out/`. Then delete any file that is
  superseded rather than leaving it looking like pending work.
  `refresh_index code/out/` after.

- [ ] **4. `edge_map_invertibility` already in CLAIMS.md — confirm and close.**
  Claim `edge-interior-invertibility-sharpened` is already in the ledger at
  `proved` with the unitriangular F₂ argument, three-route machine check to
  n=18, and Rule-90 anchor. The directive's item 3 ("carry the sharpened
  edge-zero-run statement into CLAIMS.md") is already satisfied. Confirm the
  claim block in `code/out/edge_map_invertibility.notes.md` matches the ledger
  entry and mark this item done.

### Directive 30 tasks (mathematical direction — keep, do after hygiene)

- [ ] **5. Produce the ratio table (Directive 30 item 4).**
  Columns: 0-based giant pre-jump row, 1-based landing row, b_land, j_i,
  gap_i (to next giant), ratio gap_i/(j_i+1), flooring. 15 genuine giants
  from the 6e8 run (exclude row 248). Source:
  `code/out/pattern_finder_6e8_giants.captured.txt`. If every ratio < 1 with
  room, restate step 6 as the ratio bound and mark the old bounded-gap form
  superseded. Anchor: `code/out/directive30_ratio_table.md`.

- [ ] **6. Rephrase step 6 in `research/threads/regeneration.md`.**
  The conjecture needs Σ(j_i+1) ≥ k−2. This holds if each giant covers
  the distance to the next: gap_i ≤ j_i + 1. The 6e8 data shows max ratio
  0.0167 — two orders of slack.

- [ ] **7. Compute the width needed for the next genuine giant.**
  k*=248 at 6e8 (W=31,324,703 primes). Geometric growth factor ~1.75×
  puts next landing block at ~55M. Width needed ≈ landing + row + headroom
  → sieve roughly 9e8–1e9. Report in `research/threads/regeneration.md`.

- [ ] **8. Update CONTEXT.md Run state and Established.**
  Replace Directive 28 run-state block with 6e8 record: 15 genuine giants,
  max gap 64, row 238 genuine, k*=248, parity 14/15, step 6 rephrased as
  ratio bound.

- [ ] **9. Downgrade superseded claims.**
  `wider-width-giant-record-3e8` → superseded. `directive25-gap-trend-and-reconciliation`
  gap max → 64, not 26. `giant-parity-even-pre-jump-rows` count unchanged
  (14/15) but row 238 now proven genuine.

- [ ] **10. Hygiene: remove bare .txt duplicates in `code/pattern_finder/`.**
  `b.txt, bits.txt, diffs.txt, intruder.txt, jumps.txt, minima_b.txt,
  minima_rows.txt, regen_rows.txt, s.txt, s_runs0.txt, s_runs2.txt,
  b_genuine.txt` — 12 files. Canonical copies in
  `code/out/pattern_finder_outputs/`. `rm` the duplicates. `refresh_index`
  both folders.

- [ ] **11. Provability question (Directive 26 core, still open).**
  Ratio bound gap_i/(j_i+1) ≤ 0.017 changes the question: proving the gap
  grows slower than the jump. Is geometric growth of b a consequence of
  anything known about primes, or new?

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal.** `research/notes/step_law_proved.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified; combinatorial.
- **Recharge surplus (depth 1000):** S_1000 = 1,270,603 vs required 998. `code/out/surplus_renewal_structure.md`.
- **6e8 giant record (DONE, Directive 30):** 15 genuine giants, max gap 64, row 238 genuine, k*=248, parity 14/15, geometric growth ×1.765/event. `code/out/pattern_finder_6e8_giants.captured.txt`.
- **Width-degradation caveat (DONE):** k*=162 (2e7), k*=239 (3e8), k*=248 (6e8).
- **Lean 4 formalisation — COMPLETE** (Directive 17). Nine theorems, zero sorry, axiom footprint [propext, Classical.choice, Quot.sound]; IFF reformulation. Claim `gilbreath-second-entry-equivalence`. Anchored to `code/out/lean_gilbreath_reduction.captured.txt` (1028B, non-empty, full `#print axioms`).
- **Edge-map invertibility — PROVED.** Claim `edge-interior-invertibility-sharpened`: every nonzero {0,2} block shows edge 2 at least once during its n erosion reads; worst zero-run ≤ n−1 (sharp). F₂-unitriangular argument + three-route machine check. `code/out/edge_map_invertibility.notes.md`.
- **Conditional-rate experiment — DONE** (Directive 19). Mean rate superseded (heavy tail).
- **CHT Theorem 1.6 hypothesis check — DONE:** `holds-here: no`.
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000, sieve 2e7), `wider_width_b.json` (depth 240, sieve 3e8), `giants_6e8.json` (depth 400, sieve 6e8).
- **Library:** downloads halted; FRONTIER.md restored from commit db36fc23.

### Threads

- `research/threads/regeneration.md` — LIVE (Directive 30): 15 genuine giants, max gap 64, step 6 rephrased as ratio bound gap_i ≤ j_i+1 (holds with 2+ orders margin). Next: ratio table + provability question refocused on jump growth rate.
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).