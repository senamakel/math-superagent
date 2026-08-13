# Tasks

## Directive 24 (steer): Width degradation caveat + geometric growth test

### Immediate (in order)

- [ ] **1. Width-degradation caveat (directive item 1).**
  The bigjump table (`code/out/bigjump_characterization.captured.txt`) shows
  the floor column runs from 1,268,392 at i=34 down to 0 at i=161, cols
  shrinks 1,270,572 → 1,270,445 — so the data degrades continuously and i=161
  is only where it degrades to nothing. Compute the depth k* beyond which the
  remaining floor is small enough that a giant jump of size ≥ J would be
  truncated (i.e., where `W − k − b_k < J_min` for a reasonable J_min like
  1000). Mark every measurement past k* as a lower bound in
  `research/threads/regeneration.md`. Every claim resting on the bigjump table
  needs this caveat or it overstates.

- [ ] **2. Geometric growth test (directive item 2).**
  Giants exhibit b roughly doubling: 865→2179, 4203→5942, 5939→23265,
  141706→271629, 325096→515906, 515907→733564, 733575→1094273. Fit b at the
  giant-event rows against BOTH a linear model and a geometric (exponential)
  model. Report residuals and which fits. If geometric: restate
  the target in `research/threads/regeneration.md` — not a lower bound on the
  event rate, but a proof that the inter-giant gap is finite (giants need only
  keep arriving AT ALL, at any rate, because geometric growth makes the
  recharge inequality trivial). If linear: the event-rate lower-bound route
  remains live.

- [ ] **3. Restate the target in `research/threads/regeneration.md`**
  based on the outcome of item 2. If geometric: the conjecture reduces to
  "giants arrive infinitely often" rather than "event rate ≥ threshold".
  State the new target explicitly and close the mean-rate-bound route as
  superseded.

- [ ] **4. Hygiene: remove bare .txt duplicates in `code/pattern_finder/`.**
  `b.txt, bits.txt, diffs.txt, intruder.txt, jumps.txt, minima_b.txt,
  minima_rows.txt, regen_rows.txt, s.txt, s_runs0.txt, s_runs2.txt,
  b_genuine.txt` — 12 files. Canonical copies in
  `code/out/pattern_finder_outputs/`. `rm` the duplicates (coder role).
  Keep the `.py` scripts. `refresh_index` both folders.

- [ ] **5. Update CONTEXT.md** with width-degradation caveat and geometric-growth
  finding once computed; record depth k* and the model fit.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal:** `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`; `b_k = b_1 + Σ_{i<k}(j_i+1) − (k−1)`. Zero failures on all 1,154 sweep sequences AND primes. `research/notes/step_law_proved.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified; combinatorial.
- **Recharge surplus (depth 1000):** S_k = b_k − b_1 + (k−1) = Σ(j_i+1), monotone, strictly increases exactly at (2,4)-events; S_1000 = 1,270,603 vs required 998. `code/out/surplus_renewal_structure.md`, `code/out/surplus_renewal_table.captured.txt`.
- **Bigjump characterisation (DONE, Directive 23 item 1):** 12 of 13 giants genuine, 1 capped-artifact (i=161). Genuine giants carry 86.1% of S_1000. Claim `bigjump-cap-characterization-1000`. Anchors: `code/out/bigjump_characterization.captured.txt`, `code/out/bigjump_characterization.notes.md`.
- **Lean 4 formalisation — COMPLETE** (Directive 17). Nine theorems, zero sorry, axiom footprint [propext, Classical.choice, Quot.sound]; IFF reformulation. Live claim `gilbreath-second-entry-equivalence`.
- **Conditional-rate experiment — DONE** (Directive 19). Pooled λ̂ ≈ 0.585, family-independent post-startup (p=0.68 over 8 families). **Directive 23: λ̂ is a MEAN, wrong summary for the heavy-tailed jump distribution — do not build a mean-rate bound.**
- **CHT Theorem 1.6 hypothesis check — DONE:** M=7, L=2, R_0≈4.2e8 ≫ 1000; `holds-here: no`.
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000, sieve 2e7, 1,270,607 primes).
- **Library:** downloads halted; FRONTIER.md restored from commit db36fc23.

### Threads

- `research/threads/regeneration.md` — LIVE, REFRAMED (Directive 24): the object is the gap between consecutive giant jumps. Next step: width-degradation caveat (find k* and mark capped measurements) + geometric growth test on b at giant events. If geometric growth holds, the target relaxes to "giants arrive infinitely often" rather than "event rate bounded below".
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).
