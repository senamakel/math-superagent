# Tasks

## Directive 26 (steer): Complete the chain — the conjecture reduces to one statement

Directive 25 items are DONE. The chain is now:

1. Gilbreath ⇔ second entry in {0,2} (Lean, sorry-free, axioms clean)
2. ⇔ Σ(j_i+1) ≥ k−2 (recharge identity, proved, universal)
3. 13 giants carry 99.76% of S_1000 (bigjump_characterization)
4. giants ARE the (2,4)-events (every one has edge=2, intr=4)
5. j grows like b^0.388, sublinear but → ∞ (43-event OLS)
6. inter-giant gap: no trend, mean 10.18, max 26 over b 2e3..1.1e6
7. bounded gap + j → ∞ ⇒ b_k ≥ 1 forever

**The conjecture now reduces to ONE statement: the inter-giant gap is bounded.**
The chain is written into `research/threads/regeneration.md` as the run's whole
position.

Two cautions recorded: 12 gaps is a small sample (R² 0.109 does not exclude a slow
trend); every number comes from one finite triangle, not a property of the primes.

### Immediate (in order)

- [ ] **1. Provability question (Directive 26 core).** Before attempting a proof:
  does "the gap between consecutive (2,4)-events is bounded" follow from anything
  known about prime gaps, or is it equivalent to something hard? Three branches:
  - **Corollary of known results:** prime gaps are O(p^θ) with θ≈0.525, but does
    that feed through the Rule 90 interior + drain law to bound the inter-event gap?
  - **Equivalent to a named conjecture:** Cramér? GPY? Elliott–Halberstam? If so,
    the equivalence IS a partial result — a reduction of Gilbreath to a standard
    conjecture. That meets the GOAL.md bar.
  - **Neither:** a new isolated statement, not known hard. Name the obstruction.
  Answer this before launching a proof attempt. `request_research` if the answer
  depends on a source the library does not have.

- [ ] **2. Hygiene: remove bare .txt duplicates in `code/pattern_finder/`.**
  `b.txt, bits.txt, diffs.txt, intruder.txt, jumps.txt, minima_b.txt,
  minima_rows.txt, regen_rows.txt, s.txt, s_runs0.txt, s_runs2.txt,
  b_genuine.txt` — 12 files. Canonical copies in
  `code/out/pattern_finder_outputs/`. `rm` the duplicates (coder role).
  Keep the `.py` scripts. `refresh_index` both folders.

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
- **Inter-giant gap trend (DONE, Directive 25 item 3):** genuine-12 gaps = 22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12 rows (mean 10.18, median 8, max 26); no trend vs event index or prior b (Spearman rho = −0.141, all R² ≤ 0.11). Compatible with "giants arrive at bounded spacing while j ~ b^0.388 → ∞". `code/out/directive25_gap_trend.md`.
- **Geometric-vs-sublinear reconciliation (DONE, Directive 25 item 4):** observed rho across the 11 genuine pairs declines 3.9 → 1.49 toward 1 with b; sublinear rho = 1 + C·b^(α−1) (α=0.388, C_pool=802.6) has log-residual MSE 0.140 vs geometric 1.6816's 0.154 — neither decisive, but the ratio's *decline* tracks the sublinear law, so ×1.68/event is a description of 12 points, not an asymptotic law. Operative target: G_k < j_k ≈ C·b_k^0.388 (gap grows slower than b^0.388). `code/out/directive25_gap_trend.md`; claim `directive25-gap-trend-and-reconciliation`.
- **Lean 4 formalisation — COMPLETE** (Directive 17). Nine theorems, zero sorry, axiom footprint [propext, Classical.choice, Quot.sound]; IFF reformulation. Live claim `gilbreath-second-entry-equivalence`.
- **Conditional-rate experiment — DONE** (Directive 19). Pooled λ̂ ≈ 0.585, family-independent post-startup (p=0.68 over 8 families). **Directive 23: λ̂ is a MEAN, wrong summary for the heavy-tailed jump distribution — do not build a mean-rate bound.**
- **CHT Theorem 1.6 hypothesis check — DONE:** M=7, L=2, R_0≈4.2e8 ≫ 1000; `holds-here: no`.
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000, sieve 2e7, 1,270,607 primes).
- **Library:** downloads halted; FRONTIER.md restored from commit db36fc23.

### Threads

- `research/threads/regeneration.md` — LIVE, REFRAMED (Directive 25): the geometric-growth framing from Directive 24 is inconsistent with the sublinear exponent 0.388 in the limit (b_next/b → 1). The target is now: prove the inter-giant gap grows strictly slower than b^0.388 (e.g., bounded, or logarithmic). Next step: measure inter-giant gap trend (fit against i and b) and reconcile geometric growth with the sublinear law.
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).
