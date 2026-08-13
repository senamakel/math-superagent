# Tasks

## Directive 34 (steer): read the six papers you never read

The nine arXiv `/abs/` landing pages have been replaced by full PDFs. Six are
directly on the problem. Read them before any further mathematics.

### Immediate (in order)

- [ ] **1. Read CHT 2026 first.**
  `research/sources/chase-hunter-tao-2026-cramer-random-model-gilbreath-FULLPDF.full.md`
  (98 KB, 137 theorem/lemma/proof hits). Chase proved the random-integer
  analogue of Gilbreath — the closest thing to a theorem anyone has. Read what
  hypothesis on the gap distribution his argument needs, and whether prime gaps
  satisfy or fail it. That settles whether the regeneration route and his are
  the same argument. Produce a summary: main theorem verbatim, hypotheses,
  effective and uniform or not. Anchor: `research/notes/cht-2026-summary.md`.

- [ ] **2. Read Arias de Reyna.**
  `research/sources/arias-de-reyna-list-manipulation-conjecture-FULLPDF.full.md`
  (52 KB, 91 hits). The list-manipulation framing is the standard one.
  Summary: main theorem verbatim, hypotheses. Anchor:
  `research/notes/arias-de-reyna-summary.md`.

- [ ] **3. Read Muney 2026.**
  `research/sources/muney-2026-holes-valid-extension-sets-FULLPDF.full.md`
  (95 KB, 110 hits). Bears directly on the
  `valid-extension-backward-nonlocal-refuted` claim. Summary: main theorem
  verbatim, hypotheses. Anchor: `research/notes/muney-2026-summary.md`.

- [ ] **4. Read the remaining three.**
  BCZ 2023 filtered-rays, BCZ quasi-periodicity, Granville 2026 — in that
  order. One summary per paper. Anchors:
  `research/notes/bcz-2023-filtered-rays-summary.md`,
  `research/notes/bcz-quasi-periodicity-summary.md`,
  `research/notes/granville-2026-summary.md`.

- [ ] **5. Re-judge `granville-2026-piercing-gilbreath-not-load-bearing`.**
  The claim was made off the 6.8 KB `/abs/` landing page. The FULL PDF
  (175 KB, 70 theorem/lemma/proof hits) and the operator's notes
  (`research/notes/granville-2607-04166-actually-read.md`,
  `research/notes/lemma54-discarded-case-is-universal.md`) show Lemma 5.4
  and Theorem 5.5 are real — Lemma 5.4 is a supply-vs-demand budget
  inequality equivalent to the run's own recharge identity in different
  coordinates; Theorem 5.5 reduces GC to a lower bound on nu_2 alone (demand
  side α=0.525 unconditional by Baker-Harman-Pintz). The paper is cs.CR,
  not peer reviewed, proofs are uneven (Theorem 2.5: "Take κ₀=0 and the
  theorem is proved!"; Lemma 5.4 discards delta=0 case occurring in 100% of
  columns). **Re-grade**: not "not-load-bearing" — it contains a genuinely
  useful reduction. Status depends on Lemma 5.4 re-derivation (Directive 32/33):
  if it survives re-derivation here, upgrade to `checked` with the caveat
  that the proof is this run's, not the author's.

- [ ] **6. Revisit all nine claims anchored to `/abs/` landing pages.**
  For each claim whose `check it at` field points at a <7 KB source, verify
  that the matching `-FULLPDF.full.md` file supports or contradicts it.
  Update the claim's evidence, bearing, and status. The nine are the six
  above plus: bhat-cobeli-zaharescu-filtered-rays (identical to the 2023
  version), colonna-proth-gilbreath-record (already had full content), and
  plouffe-2025-verification-10e14 (already had its own full PDF).

## Directive 32/33 (steer): Granville's Lemma 5.4

### (start after item 1 — CHT must be read first)

- [ ] **7. Reproduce the operator's nu_2 numbers in-container.**
  `code/nu2_granville_check.py` already written; run it, capture to
  `code/out/nu2_granville_check.captured.txt`. Verify: nu_2/n ∈ [0.42, 0.52]
  for n ∈ {50,100,200,400,800,1600,3200,3999}, Lemma 5.4 hypothesis
  g*_n ≤ 2·nu_2(q_{n-1})+2 holds at every sampled n. Mark the operator claim
  `granville-nu2-density-measured` as run-reproduced.

- [ ] **8. Re-derive Lemma 5.4 from scratch.**
  Handle the `delta_{k-1}(q_n)=0` case explicitly — it occurs in 100% of
  columns (operator-computation, `lemma54-discarded-case-is-universal`).
  The published proof sets it aside as an exception; the repair is showing
  a zero inside the block guarantees success in general. **Prove it and
  Lemma 5.4 becomes `proved` here.** If it survives, it is the strongest item
  in the ledger.

- [ ] **9. Test Lemma 5.4 from the FAILING side.**
  Use Granville's "closest failing sister" construction (his section 5.1)
  or synthetic Poisson-gap sequences (his section 4). Find sequences with v_n
  straddling 2·nu_2+2 and check success flips exactly at the threshold.
  If it flips elsewhere, the constant is wrong and Theorem 5.5 needs
  restating. **The prime-only test is vacuous** (every column succeeds, both
  sides always true — Directive 33 warning).

- [ ] **10. Compare routes in `research/threads/regeneration.md`.**
  Current route (step 6): ratio bound gap_i ≤ j_i+1, needs geometric growth
  of b. Granville's route: Lemma 5.4 → Theorem 5.5 → nu_2 > n^β with β >
  0.525. His demand is nu_2 > n^0.525, met by 26× and rising (operator
  measurement: nu_2 = 2048 at n = 3999 vs threshold 78). If Granville's
  route is provably weaker, **SWITCH** the thread target: mark the ratio-bound
  route superseded, make "lower-bound nu_2" the live target. If the routes
  are equivalent (both reduce to proving the block never dies), record that.

- [ ] **11. Adopt nothing else from Granville.**
  Theorem 2.5's proof is not a proof. Theorem 5.5's β = 0.99 comes from the
  author's own Conjecture 5.1. The only pieces worth having are Lemma 5.4
  and the Baker-Harman-Pintz α = 0.525 on the demand side.

## Directive 31 (steer): keystone auditable + unrun pile

### (lower priority; do these when blocked on thinking)

- [ ] **12. Re-emit `lean_reduction.captured.txt`.**
  Currently zero bytes. Re-compile `code/lean/reduction.lean`, add
  `#print axioms <theorem name>` for every theorem, capture stdout,
  echo `lean --version` and `sha256sum`. If `lean` unavailable, say so
  and downgrade claims resting on this file. The main claim
  `gilbreath-second-entry-equivalence` correctly anchors to the non-empty
  `lean_gilbreath_reduction.captured.txt` — this is about the separate
  `reduction.lean` compilation artifact. INDEX.md must not call a zero-byte
  file evidence of anything.

- [ ] **13. `lean_shape.captured.txt` check.**
  It is 147 bytes, non-empty — skip.

- [ ] **14. Clear the unrun `.py` pile in `code/out/`.**
  9 files genuinely uncaptured: `check_three_candidates.py`,
  `check_three_candidates2.py`, `check_window_range_allcells.py`,
  `check_window_range_empirical2.py`, `final_run.py`, `final_run2.py`,
  `_run_edge.py`, `runner2.py`, `runner3.py`. Extend `exec.sh` with
  `timeout 540 python3 ... 2>&1 | tee` for all 9, run, capture. Delete
  superseded files. `refresh_index code/out/`.

- [ ] **15. `edge_map_invertibility` already in CLAIMS.md — confirm and close.**
  Claim `edge-interior-invertibility-sharpened` already at `proved`. Confirm
  the claim block in `code/out/edge_map_invertibility.notes.md` matches the
  ledger entry and mark this item done.

## Directive 30 tasks (mathematical — keep, lower priority)

- [ ] **16. Ratio table (Directive 30 item 4).**
  15 genuine giants, 6e8 run. Columns: 0-based pre-jump row, 1-based
  landing row, b_land, j_i, gap_i, ratio gap_i/(j_i+1), flooring.
  Exclude row 248 (cap). Anchor: `code/out/directive30_ratio_table.md`.

- [ ] **17. Rephrase step 6 in `research/threads/regeneration.md`.**
  Ratio bound gap_i ≤ j_i+1 holds with 2+ orders margin (max ratio 0.0000122).
  **But hold: the Granville comparison (item 10) may supersede this.**

- [ ] **18. Width estimate for next genuine giant.**
  k*=248 at 6e8 (W=31.3M primes). Geometric projection ~55M block →
  sieve ~1e9. Report in `research/threads/regeneration.md`.

- [ ] **19. Update CONTEXT.md Run state and Established.**
  Replace Directive 30 run-state block with 6e8 record. **Do after
  Directive 34 completion — the run state is now under Directive 34.**

- [ ] **20. Downgrade superseded claims.**
  `wider-width-giant-record-3e8` → superseded. `directive25-gap-trend-and-reconciliation`
  gap max → 64, not 26. `giant-parity-even-pre-jump-rows` count unchanged
  (14/15) but row 238 now proven genuine.

- [ ] **21. Hygiene: remove bare .txt duplicates in `code/pattern_finder/`.**
  `b.txt, bits.txt, diffs.txt, intruder.txt, jumps.txt, minima_b.txt,
  minima_rows.txt, regen_rows.txt, s.txt, s_runs0.txt, s_runs2.txt,
  b_genuine.txt` — 12 files. Canonical copies in
  `code/out/pattern_finder_outputs/`. `rm` the duplicates. `refresh_index`
  both folders.

## Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
  Lean 4 IFF, sorry-free. Claim `gilbreath-second-entry-equivalence`.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved.
  `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 =
  Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal.**
  `research/notes/step_law_proved.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified; combinatorial.
- **Recharge surplus (depth 1000):** S_1000 = 1,270,603 vs required 998.
  `code/out/surplus_renewal_structure.md`.
- **6e8 giant record (DONE, Directive 30):** 15 genuine giants, max gap 64,
  row 238 genuine, k*=248, parity 14/15, geometric growth ×1.765/event.
  `code/out/pattern_finder_6e8_giants.captured.txt`.
- **Width-degradation caveat (DONE):** k*=162 (2e7), k*=239 (3e8), k*=248 (6e8).
- **Edge-map invertibility — PROVED.** Claim `edge-interior-invertibility-sharpened`.
  `code/out/edge_map_invertibility.notes.md`.
- **Conditional-rate experiment — DONE** (Directive 19). Mean rate superseded
  (heavy tail). `code/out/conditional_rate_experiment.notes.md`.
- **CHT Theorem 1.6 hypothesis check — DONE:** `holds-here: no`.
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000,
  sieve 2e7), `wider_width_b.json` (depth 240, sieve 3e8), `giants_6e8.json`
  (depth 400, sieve 6e8).
- **Library:** downloads halted; FRONTIER.md restored from commit db36fc23.
  Six FULL-PDF papers now in `research/sources/` awaiting reading (Directive 34).
- **Granville notes (operator-computation, not yet run-reproduced):**
  `research/notes/granville-2607-04166-actually-read.md` — Lemma 5.4/Theorem 5.5
  reduction, nu_2 ~ n/2 measurement. `research/notes/lemma54-discarded-case-is-universal.md` —
  delta=0 case occurs in 100% of columns; published proof does not establish the lemma.

### Threads

- `research/threads/regeneration.md` — LIVE (Directive 30/34): 15 genuine giants,
  max gap 64, step 6 rephrased as ratio bound. **Directive 34 adds a new fork:**
  Granville's Lemma 5.4/Theorem 5.5 route (lower-bound nu_2) vs current
  ratio-bound route (geometric growth of b). Comparison queued (item 10).
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).