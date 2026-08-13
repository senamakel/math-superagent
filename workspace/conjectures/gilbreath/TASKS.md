# Tasks

## Directive 23 (steer): The surplus is heavy-tailed — characterise the giant jumps and reframe the target

### Immediate (in order)

- [ ] **1. Characterise the big jumps (the directive's first demand).**
  `code/out/surplus_renewal_table.captured.txt` shows the recharge identity
  holds exactly at depth 1000 (`b_1000 = 2 + S_1000 − 999` = `1,269,606 =
  2 + 1,270,603 − 999`), but the jump column is heavy-tailed: most j are tiny
  (0,1,2,3,4,9,…) and the surplus is carried by a handful of giant recharges —
  the three largest are i=134 (j=217,657), i=146 (j=360,698), i=161
  (j=176,181). Print every event i with j > 1000 alongside its block structure:
  j, b_i (block length at that row), the (edge, intruder) pair, and whether the
  row sits at a block boundary or a row-length/width reset (finite sieve width
  = 1,270,607 primes; the k=162 row where the block fills width−1 is the known
  finite-width artifact). Say explicitly, per big jump, whether it is genuine
  dynamics or a boundary artifact — i=161 lands at b≈1.27M = width−1, so if the
  giants cluster at width resets the heavy tail may be a finite-width effect,
  not the primes' asymptotic renewal structure. This determination decides
  whether the reframing in item 2 bites.
  Anchors: `code/out/surplus_renewal_table.captured.txt`,
  `code/out/blocks_depth1000.json`, `code/out/surplus_renewal_structure.md`.

- [ ] **2. Reframe the regeneration thread (directive item 2) — carried out in
  this directive; verify it reads correctly.** `research/threads/regeneration.md`
  now states: the event-rate route targets a MEAN (λ̂ ≈ 0.585), a mean is the
  wrong summary for a heavy-tailed jump distribution, and what a bound must
  control is the GAP between consecutive large jumps, not the average event
  rate. Confirm no stale "bound the mean rate" task survives in TASKS/CONTEXT.

- [ ] **3. Hygiene: remove the 12 bare duplicate outputs in `code/pattern_finder/`**
  (`b.txt, bits.txt, diffs.txt, intruder.txt, jumps.txt, minima_b.txt,
  minima_rows.txt, regen_rows.txt, s.txt, s_runs0.txt, s_runs2.txt,
  b_genuine.txt`). Their canonical copies already exist with identical sizes in
  `code/out/pattern_finder_outputs/` — so this is a `rm` of the duplicates, not
  a move (the director has no delete tool; the coder role runs it). Keep the
  `.py` scripts in `code/pattern_finder/`. Then `refresh_index` both folders.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal:** `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`; `b_k = b_1 + Σ_{i<k}(j_i+1) − (k−1)`. Zero failures on all 1,154 sweep sequences AND primes. `research/notes/step_law_proved.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified; combinatorial.
- **Recharge surplus (depth 1000):** S_k = b_k − b_1 + (k−1) = Σ(j_i+1), monotone, strictly increases exactly at (2,4)-events; S_1000 = 1,270,603 vs required 998. `code/out/surplus_renewal_structure.md`, `code/out/surplus_renewal_table.captured.txt`.
- **Lean 4 formalisation — COMPLETE** (Directive 17). Nine theorems, zero sorry, axiom footprint [propext, Classical.choice, Quot.sound]; IFF reformulation. Live claim `gilbreath-second-entry-equivalence` (verbatim `Nat.dist`, proved).
- **Conditional-rate experiment — DONE** (Directive 19). Pooled λ̂ ≈ 0.585, family-independent post-startup (p=0.68 over 8 families). **Directive 23: λ̂ is a MEAN, wrong summary for the heavy-tailed jump distribution — do not build a mean-rate bound.**
- **CHT Theorem 1.6 hypothesis check — DONE:** M=7, L=2, R_0≈4.2e8 ≫ 1000; `holds-here: no`.
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000, sieve 2e7, 1,270,607 primes).
- **Library:** downloads halted; FRONTIER.md restored from commit db36fc23.

### Threads

- `research/threads/regeneration.md` — LIVE, REFRAMED (Directive 23): the object is the gap between consecutive large jumps, not the mean event rate. Next step: characterise the big jumps (j > 1000) and say whether they are genuine dynamics or width-reset artifacts.
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).
