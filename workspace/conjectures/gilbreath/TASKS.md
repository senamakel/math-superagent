# Tasks

## Directive 28 (steer): Width-capping correction + extend sieve for more genuine giants

**Directive 28 stated row 238's giant (j=5,596,824, land=16,252,084) is genuine
because landing 16.2M against "width 3e8." This is a unit error.** 3e8 is the
sieve bound, not the row width. Row width at row 239 is π(3e8) − 239 ≈
16,252,086, and b₂₃₉ = 16,252,084 fills the row — flooring = 1, intruder None,
k* = 239. Both capture files already record it as capped. The 14 genuine gaps
remain [22,8,4,26,2,14,2,14,4,4,12,15,13], max=26, and the gap-trend OLS
(slope −0.818, R² 0.109) is already on disk from Directive 25. Step 6 of the
chain is NOT in doubt from this data; the claimed "gaps roughly doubling"
(12, 28, 64) came from including a capped artifact as though genuine.

The parity result (14 of 15 giant pre-jump rows even, 14 of 14 with row 161
excluded; p ≈ 0.0008 vs plain 1/2 null) is recorded in
`research/notes/pattern_finder_wider_giants.md` as
`giant-parity-even-pre-jump-rows` — status: checked numerically, suggestive,
not established (post-hoc-with-two-confirmations), falsifier = a second
odd-pre-jump-row giant.

### Immediate (in order)

- [ ] **1. Extend the sieve to capture genuinely new giants past row 238.**
  The 3e8 sieve covers the live regime only to row 238; the 15th "giant" at
  row 238→239 is the finite-width artifact of that sieve. To test the
  bounded-gap claim on new data, extend the sieve past 3e8 so the live regime
  (rows with intruder defined) reaches at least row 300. Use the same generator
  and width-degradation test as `wider_width_extend`. Report: k*, genuine giant
  rows, inter-giant gaps, max gap, and whether any new gap exceeds 26.
  Anchor pattern: `code/out/wider_width_extend.captured.txt`.
  **Budget:** single-threaded, O(W) memory, < 8 GiB. Say the sieve bound and
  expected runtime before launching.

- [ ] **2. Update thread and CONTEXT.md with width-capping correction.**
  `research/threads/regeneration.md`'s thread-header status currently says
  "max gap now 64 (175→239 drought)" — that is WRONG; row 239 is a
  width-capped artifact, not a genuine giant. Restore the 14-genuine-giant
  record (max=26) and remove the superseded claim. DONE — this edit.

- [ ] **3. Provability question (Directive 26 core, still open).** Before attempting
  a proof: does "the gap between consecutive (2,4)-events is bounded" follow from
  anything known about prime gaps, or is it equivalent to something hard? Three branches:
  - **Corollary of known results:** prime gaps are O(p^θ) with θ≈0.525, but does
    that feed through the Rule 90 interior + drain law to bound the inter-event gap?
  - **Equivalent to a named conjecture:** Cramér? GPY? Elliott–Halberstam? If so,
    the equivalence IS a partial result — a reduction of Gilbreath to a standard
    conjecture.
  - **Neither:** a new isolated statement, not known hard. Name the obstruction.
  `request_research` if the answer depends on a source the library does not have.

- [ ] **4. Hygiene: remove bare .txt duplicates in `code/pattern_finder/`.**
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
- **Bigjump characterisation (DONE, Directive 23):** 12 of 13 giants genuine, 1 capped-artifact (i=161). Genuine giants carry 86.1% of S_1000. Claim `bigjump-cap-characterization-1000`. **Directive 27: cap resolved — wider sieve (3e8, 16.25M primes, depth 240) adds two genuine giants at rows 162 (j=4,323,712), 175 (j=5,237,310).**
- **Width-degradation caveat (DONE, Directive 24):** k* = 162 (original sieve), k* = 239 (wider sieve). All 14 genuine giants have flooring well above threshold.
- **Geometric growth description (Directive 24):** ×1.68/event, R²=0.94 vs linear 0.78 over 12 genuine giants. **Directive 27: improved to ×1.751/event, R²=0.9607 over 14 giants.**
- **Sublinear jump exponent (depth 1000):** log(jump) vs log(b) OLS slope 0.388 over 43 positive-jump events. `code/out/surplus_renewal_structure.md`.
- **Growth law — UNSETTLED (Directive 27).** The 13th ratio 4.95 reverses the declining-ratio trend Directive 25 used to argue sublinear asymptotics. Geometric fit improved with new data. The honest position: the growth law is not determined by this data. What IS settled: j → ∞, inter-giant max gap unchanged at 26.
- **Inter-giant gap (Directive 25 + 27):** 14 genuine gaps = 22,8,4,26,2,14,2,14,4,4,12,15,13; max 26 unchanged, new gaps inside existing range. Gap half of claim `directive25-gap-trend-and-reconciliation` strengthened; reconciliation half downgraded. Anchors: `code/out/directive25_gap_trend.md`, `code/out/wider_width_extend.captured.txt`.
- **Lean 4 formalisation — COMPLETE** (Directive 17). Nine theorems, zero sorry, axiom footprint [propext, Classical.choice, Quot.sound]; IFF reformulation. Live claim `gilbreath-second-entry-equivalence`.
- **Conditional-rate experiment — DONE** (Directive 19). Pooled λ̂ ≈ 0.585, family-independent post-startup (p=0.68 over 8 families). **Mean rate superseded (heavy tail).**
- **CHT Theorem 1.6 hypothesis check — DONE:** M=7, L=2, R_0≈4.2e8 ≫ 1000; `holds-here: no`.
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000, sieve 2e7, 1,270,607 primes), `wider_width_b.json` (depth 240, sieve 3e8, 16,252,325 primes).
- **Library:** downloads halted; FRONTIER.md restored from commit db36fc23.

### Threads

- `research/threads/regeneration.md` — LIVE (Directive 27): gap bounded (max 26, unchanged with 15× width increase, corroborated). Growth law unsettled. Next: provability question (Directive 26).
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).
