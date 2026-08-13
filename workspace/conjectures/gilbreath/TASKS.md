# Tasks

## Directive 25 (steer): Reconcile geometric growth with sublinear exponent — measure the inter-giant gap trend

Directive 24 items 1–2 are DONE (`directive24_width_degradation.md`: k* = 162, all 12 genuine giants far above threshold; `directive24_geometric_growth.md`: geometric R²=0.94 vs linear 0.78, ×1.68/event over 12 genuine). Directive 25 points out an internal inconsistency: under the sublinear jump exponent j ~ C·b^0.388 (log-log slope from surplus_renewal_structure, 43 positive-jump events), the ratio b_next/b = 1 + C·b^(-0.612) → 1 as b grows — so the ×1.68/event observed over 12 points cannot be the asymptotic law. Geometric growth and a sublinear exponent are inconsistent in the limit, and the run has written both without reconciling them.

This is not bad news: b still increases whenever j exceeds the inter-giant gap, and j → ∞ under the sublinear law, so divergence survives. What changes is what has to be proved — not "the ratio stays above 1" (false asymptotically if 0.388 is real), but "the inter-giant gap stays bounded (or grows slower than b^0.388)."

### Immediate (in order)

- [x] **1. Width-degradation caveat — DONE.** k* = 162; all 12 genuine giants have flooring ≥ 536,885 > 1000; rows ≥ 162 are lower bounds only. `code/out/directive24_width_degradation.md`.

- [x] **2. Geometric growth test — DONE.** Geometric R²=0.94 vs linear 0.78 over genuine 12; ×1.68/event, doubling every ~1.33 events. Robust to all-13 (0.94 vs 0.81). `code/out/directive24_geometric_growth.md`.

- [ ] **3. Inter-giant gap trend (Directive 25 core).**
  From the 13 giants at i = 34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146, 161, the inter-giant gaps in rows are: 22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12, 15. Fit these gaps against i (event index) and against b (post-jump block length at the previous giant). Report both fits alongside j. Say whether gaps trend upward, downward, or are flat. If the gap is bounded while j grows (j ~ b^0.388 → ∞), then b_k ≥ 1 follows and the mechanism is established. If the gap grows comparably, that is the real obstruction.

- [ ] **4. Reconcile geometric growth with sublinear exponent.**
  Compute the expected ratio b_next/b = 1 + j/b from the sublinear law j ~ C·b^0.388 at the b-values of the 12 genuine giants. Compare to the observed ratios (2.7, 3.9, 1.35, 2.94, …). Is the discrepancy a sample-size effect (12 points at b ~ 10³–10⁶) or a genuine tension? State what a run at larger width would settle.

- [ ] **5. Restate the target in `research/threads/regeneration.md`.**
  The "geometric growth → giants arrive infinitely often" framing from Directive 24 is too weak if the ratio decays asymptotically. The correct reduction: b_k ≥ 1 for all k follows if the inter-giant gap G_k satisfies G_k · (consumption rate 1) < j_k for all k after startup. Under the sublinear law j ~ C·b^0.388, this is: G_k < C·b_k^0.388. So the conjecture holds if the inter-giant gap grows strictly slower than b^0.388 — i.e., if the gap is bounded, or grows logarithmically, or as any sub-power law. State this explicitly, close the geometric-growth route as a description-of-12-points rather than a law, and keep the sublinear exponent as the operative constraint.

- [ ] **6. Hygiene: remove bare .txt duplicates in `code/pattern_finder/`.**
  `b.txt, bits.txt, diffs.txt, intruder.txt, jumps.txt, minima_b.txt,
  minima_rows.txt, regen_rows.txt, s.txt, s_runs0.txt, s_runs2.txt,
  b_genuine.txt` — 12 files. Canonical copies in
  `code/out/pattern_finder_outputs/`. `rm` the duplicates (coder role).
  Keep the `.py` scripts. `refresh_index` both folders.

- [ ] **7. Update CONTEXT.md** with the inter-giant gap trend and the reconciled framing once computed.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal:** `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`; `b_k = b_1 + Σ_{i<k}(j_i+1) − (k−1)`. Zero failures on all 1,154 sweep sequences AND primes. `research/notes/step_law_proved.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified; combinatorial.
- **Recharge surplus (depth 1000):** S_k = b_k − b_1 + (k−1) = Σ(j_i+1), monotone, strictly increases exactly at (2,4)-events; S_1000 = 1,270,603 vs required 998. `code/out/surplus_renewal_structure.md`, `code/out/surplus_renewal_table.captured.txt`.
- **Bigjump characterisation (DONE, Directive 23 item 1):** 12 of 13 giants genuine, 1 capped-artifact (i=161). Genuine giants carry 86.1% of S_1000. Claim `bigjump-cap-characterization-1000`. Anchors: `code/out/bigjump_characterization.captured.txt`, `code/out/bigjump_characterization.notes.md`.
- **Width-degradation caveat (DONE, Directive 24 item 1):** k* = 162, flooring(r) = 0 for all r ≥ 162, all 12 genuine giants have flooring ≥ 536,885. `code/out/directive24_width_degradation.md`.
- **Geometric growth description (DONE, Directive 24 item 2):** ×1.68/event, R²=0.94 vs linear 0.78 over 12 genuine giants. Description of the record, not a proved growth law. **Directive 25: inconsistent with sublinear exponent 0.388 in the limit — b_next/b → 1 asymptotically, so the geometric description is a finite-sample effect at b ~ 10³–10⁶.**
- **Sublinear jump exponent (depth 1000):** log(jump) vs log(b) OLS slope 0.388 over 43 positive-jump events. `code/out/surplus_renewal_structure.md`. Under this law, j ~ C·b^0.388, so the conjecture holds if the inter-giant gap grows strictly slower than b^0.388.
- **Lean 4 formalisation — COMPLETE** (Directive 17). Nine theorems, zero sorry, axiom footprint [propext, Classical.choice, Quot.sound]; IFF reformulation. Live claim `gilbreath-second-entry-equivalence`.
- **Conditional-rate experiment — DONE** (Directive 19). Pooled λ̂ ≈ 0.585, family-independent post-startup (p=0.68 over 8 families). **Directive 23: λ̂ is a MEAN, wrong summary for the heavy-tailed jump distribution — do not build a mean-rate bound.**
- **CHT Theorem 1.6 hypothesis check — DONE:** M=7, L=2, R_0≈4.2e8 ≫ 1000; `holds-here: no`.
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000, sieve 2e7, 1,270,607 primes).
- **Library:** downloads halted; FRONTIER.md restored from commit db36fc23.

### Threads

- `research/threads/regeneration.md` — LIVE, REFRAMED (Directive 25): the geometric-growth framing from Directive 24 is inconsistent with the sublinear exponent 0.388 in the limit (b_next/b → 1). The target is now: prove the inter-giant gap grows strictly slower than b^0.388 (e.g., bounded, or logarithmic). Next step: measure inter-giant gap trend (fit against i and b) and reconcile geometric growth with the sublinear law.
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).
