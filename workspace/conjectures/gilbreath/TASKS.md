# Tasks

## Directive 35 (steer): CHT column restriction + three-route comparison

### Immediate (in order)

- [ ] **1. Measure right-half {0,d} blocks (Directive 35 item 1).**
  CHT Theorem 1.6(iii) restricts the {0,d}-block obstruction to columns j ≥ N′
  (= ⌊N/2⌋) — the RIGHT HALF only. The run's leading {0,2} block sits at j=1
  (far left), so it does NOT violate (iii). The question is whether long {0,d}
  blocks with d ≥ 2 exist in the RIGHT HALF of the prime array. Scan the 6e8
  data (or the depth-1000 data) for {0,d} blocks with d ≥ 2 in the right half,
  record the longest at each depth, and compare against CHT's threshold
  R_m − 3R_{m−1}. If long right-half shallow blocks exist, Theorem 1.6 does not
  apply to primes and we've located precisely why. If not, (iii) is empirically
  supported and the obstruction is elsewhere. Both answers are worth having.
  Produce: `code/out/cht_right_half_0d_scan.captured.txt`,
  `research/notes/cht-right-half-scan.md`.

- [ ] **2. Three-route comparison in regeneration.md (Directive 35 item 2).**
  The three routes to GC and their demand sides:
  - **Route A (run's ratio bound):** needs bounded inter-giant gaps (6e8 data:
    gap ≤ 64 and holding, max gap across 15 giants is 64). Demand: geometric
    growth of b, or at minimum gap_i ≤ j_i+1 for all i.
  - **Route B (Granville ν_2):** needs ν_2 > n^0.525 with BHP unconditional
    alongside. Demand side α=0.525 is unconditional (Baker-Harman-Pintz);
    supply side ν_2/n ≈ 0.49–0.52 measured, exceeds threshold. Lemma 5.4 must
    be re-derived here (published proof broken).
  - **Route C (CHT deterministic):** needs Cramér (a_n ≪ log^10 N), open and
    strictly stronger than BHP; plus no zero-blocks of length ~log^10 N; plus
    no right-half {0,d} blocks above threshold. CHT state (ii) and (iii) "look
    difficult to establish rigorously, even if one assumes strong conjectures
    on the primes such as the Hardy–Littlewood prime tuples conjecture."
  **Granville's (Route B) has the weakest demand side** — BHP is unconditional,
  ν_2 is measured above threshold, and the only outstanding piece is Lemma 5.4
  re-derivation. The CHT authors' own difficulty assessment ("look difficult
  to establish rigorously") calibrates Route C. Add the three-route comparison
  to `research/threads/regeneration.md`; state the run is on **Route B**
  (Granville ν_2) as primary, with Route A (ratio bound) as the fallback
  empirical target. Record Tao's assessment as calibration, not discouragement:
  it is the best evidence available on how hard Route C is.

- [ ] **3. Update CONTEXT.md Run state to Directive 35.**
  Add: CHT column-restriction clarification (right half only; leading block at
  j=1 does not violate (iii)); three-route comparison summary; Tao difficulty
  assessment. Keep within budget — compress older material if needed.

## Directive 34 (steer): read the six papers you never read

### (continue — Directive 35 items take priority, then return here)

- [ ] **4. Read CHT 2026 first.**
  `research/sources/chase-hunter-tao-2026-cramer-random-model-gilbreath-FULLPDF.full.md`
  (98 KB, 137 theorem/lemma/proof hits). Produce a summary: main theorem
  verbatim, hypotheses, effective and uniform or not. Anchor:
  `research/notes/cht-2026-summary.md`. **The full text is now read by
  Directive 35 — the summary should note the column restriction j ≥ N′ in
  Theorem 1.6(iii), noted by Directive 35.**

- [ ] **5. Read Arias de Reyna.**
  Anchor: `research/notes/arias-de-reyna-summary.md`.

- [ ] **6. Read Muney 2026.**
  Anchor: `research/notes/muney-2026-summary.md`.

- [ ] **7. Read the remaining three.**
  BCZ 2023 filtered-rays, BCZ quasi-periodicity, Granville 2026 — in that
  order.

- [ ] **8. Re-judge `granville-2026-piercing-gilbreath-not-load-bearing`.**
  Re-grade based on full PDF. Lemma 5.4 and Theorem 5.5 are real; the paper
  contains a genuinely useful reduction. Status depends on Lemma 5.4
  re-derivation.

- [ ] **9. Revisit all nine claims anchored to `/abs/` landing pages.**

## Directive 32/33 (steer): Granville's Lemma 5.4

- [ ] **10. Reproduce the operator's nu_2 numbers in-container.**
  `code/nu2_granville_check.py` → `code/out/nu2_granville_check.captured.txt`.

- [ ] **11. Re-derive Lemma 5.4 from scratch.**
  Handle the `delta_{k-1}(q_n)=0` case explicitly — it occurs in 100% of
  columns. Prove it and Lemma 5.4 becomes `proved` here.

- [ ] **12. Test Lemma 5.4 from the FAILING side.**
  Find sequences with v_n straddling 2·nu_2+2 and check success flips exactly
  at the threshold.

- [ ] **13. Adopt nothing else from Granville.**
  Theorem 2.5's proof is not a proof. Theorem 5.5's β = 0.99 comes from the
  author's own Conjecture 5.1.

## Directive 31 (steer): keystone auditable + unrun pile

### (lower priority)

- [ ] **14. Re-emit `lean_reduction.captured.txt`.**
- [ ] **15. `lean_shape.captured.txt` check — skip (non-empty).**
- [ ] **16. Clear the unrun `.py` pile in `code/out/`.**
- [ ] **17. `edge_map_invertibility` already in CLAIMS.md — confirm and close.**

## Directive 30 tasks (keep, lower priority)

- [ ] **18. Ratio table (Directive 30 item 4).**
- [ ] **19. Rephrase step 6 in `research/threads/regeneration.md`.**
- [ ] **20. Width estimate for next genuine giant.**
- [ ] **21. Update CONTEXT.md Run state and Established.**
- [ ] **22. Downgrade superseded claims.**
- [ ] **23. Hygiene: remove bare .txt duplicates in `code/pattern_finder/`.**

## Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked, Lean 4 IFF
  sorry-free.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved.
- **Rule 90 interior (PROVED).**
- **Step law + recharge identity — PROVED, universal.**
- **6e8 giant record:** 15 genuine giants, max gap 64.
- **Edge-map invertibility — PROVED.**
- **CHT Theorem 1.6 hypothesis check — DONE:** `holds-here: no`. **Directive 35
  adds:** the column restriction j ≥ N′ means the leading {0,2} block at j=1
  does NOT violate (iii); the right half is unscanned.
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json`, `blocks_depth1000.json`, `wider_width_b.json`,
  `giants_6e8.json`.
- **Library:** downloads halted. FRONTIER.md restored.

### Threads

- `research/threads/regeneration.md` — LIVE (Directive 35): **three-route
  comparison added.** Primary route = Route B (Granville ν_2, weakest demand
  side: BHP unconditional, ν_2 measured above threshold, Lemma 5.4 to
  re-derive). Route A (ratio bound) kept as fallback empirical target. Route C
  (CHT deterministic) calibrated by CHT authors' own difficulty assessment.
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).