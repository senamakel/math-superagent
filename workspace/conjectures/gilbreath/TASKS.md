# Tasks

## Directive 19 (steer): Route A supported by conditional-rate experiment — record results and move forward

Directive 18 ("build-check probe") was an operator probe testing whether the steer
binary compiled and is discarded.

### Done this cycle

- [x] **Conditional-rate experiment — COMPLETE. Route A is supported, not merely un-refuted.**
  D=400, W=200000, seeds 10000..10019, 26 workers, commit ae69d093 (sign fix).
  Pooled lambda_hat = 0.585288 (1098/1876). Pearson X² p = 0.683 over 8 families
  (consecutive, f2-rand24, rand24 are immortal corner-class with zero eligible rows
  — they contribute nothing to the pooled figure). p = 0.68 is no evidence of
  family dependence. Conditioned on survival past row 10, every live family
  generates events at the same rate. That is what a combinatorial mechanism looks
  like.

  **Three cautions, as directed:**
  1. **8 families agreed, not 11.** consecutive, f2-rand24 and rand24 show
     ev_post=0, elig_post=0 — the block fills the finite row and the corner state
     is provably immortal. They contribute nothing to the pooled figure.
  2. **lambda_hat = 0.5853 is MEASURED, not bounded.** The conjecture needs
     Σ (j_i + 1) ≥ k − 2 for all k, which requires a LOWER bound on the rate
     holding for all k. An estimate at D=400 is not that. State the gap plainly.
  3. **Do not cite the D=40 smoke numbers** (lambda 0.5577, p 0.894) anywhere —
     they predate the sign fix.

  Anchors: `code/out/conditional_rate_experiment.captured.txt`,
  `code/out/conditional_rate_records.jsonl`,
  `code/out/conditional_rate_experiment.notes.md`.

- [x] ~~Conditional-rate smoke (D=40) — DISCARDED, predates sign fix. Do not cite.~~
- [x] **Lean 4 formalisation — COMPLETE.** Nine theorems, zero sorry, axiom footprint
  [propext, Classical.choice, Quot.sound]; IFF reformulation. Directive 17.
- [x] **Operator grounding — DONE.** `code/grounding/check_absdiff_vs_forwarddiff.py`
  verifies the absolute-difference operator is the one the conjecture is about.
- [x] CHT Theorem 1.6 hypothesis check — holds-here: no (R_0 = 4.2e8 ≫ 1000).
- [x] Rule 90 depth prediction — CLOSED (null computed).
- [x] Gap-hypothesis separation check — DONE (no first-moment/tail statistic separates).

### Immediate (in order)

- [ ] **1. Bound the (2,4)-event rate from below, not estimate it.**
  The conditional-rate experiment shows the rate IS family-independent post-startup —
  this is evidence for Route A (combinatorial mechanism), not a rate bound.
  The conjecture needs: for all k, Σ_{i<k} (j_i + 1) ≥ k − 2. The pooled λ̂ = 0.585
  at D=400 says events arrive at ~0.59 per eligible row — above the needed 1/(mean
  jump + 1) ≈ 0.18 (since mean jump ~4.5 on primes) — but this is an estimate, not a
  theorem.

  **The next step is a lower bound.** Two candidates:
  - Route A: bound the worst-case erosion between events from the drain law
    (y drops 2 per edge=2 row, 0 per edge=0 row; edge flips under Rule 90 interior).
    If the longest possible run of (edge=0, intruder=4) before edge flips to 2
    is bounded by a function of block length b, events cannot be arbitrarily far apart.
  - Route B: derive a lower bound from a prime-gap concentration hypothesis.
    Must state how it beats Eppstein and the Colonna g=4 deletion counterexample.

  Write the lemma that would close the gap, state its hypotheses, and test it on the
  surviving sweep families before attempting a proof.

- [ ] **2. State the honest gap.** The conjecture requires a rate lower bound that holds
  for all k. lambda_hat = 0.585 at D=400 is a point estimate; it does not rule out a
  regime where events become arbitrarily sparse. Say under what hypothesis the rate
  cannot decay, and what would falsify it.

- [ ] **3. Write up the conditional-rate result as a claim.**
  Already in `code/out/conditional_rate_experiment.notes.md` as
  `conditional-rate-experiment-family-independent` — promote to library-state.md
  and record in CONTEXT.md. Done below; verify it appears in CLAIMS.md on next
  regeneration.

### Directive 17 (steer): Lean formalisation verified complete. Recorded.

### Directive 16 (steer): Route A is NOT refuted. Sweep deaths are g_0 startup. Resolved by conditional-rate experiment — Route A is now supported, not merely un-refuted.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal:** `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`; `b_k = 2 + Σ(j_i+1) − (k−1)`. Zero failures on all 1,154 sweep sequences AND primes. `code/out/step_law_and_recharge_verified.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified 101/101; combinatorial.
- **Conditional-rate experiment — DONE.** p = 0.68 over 8 families, no family dependence post-startup. Route A supported. Anchors above.
- **Event-rate sweep (this run, 1,154 sequences):** step law + recharge identity universal (0 failures); 852/1,154 (73.8%) reach b_k=0, ALL within first 10 rows (764/852 by k≤3). Deaths are g_0 startup. Sweep does NOT bear on the asymptotic event rate.
- **Event-rate smoke (D=40) — DISCARDED, predates sign fix, do not cite.**
- **CHT Theorem 1.6 hypothesis check — DONE.** M=7, L=2, R_0=419,430,400 ≫ 1000; `holds-here: no`.
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000).
- **Library:** 92 sources on disk, downloads halted.

### Threads

- `research/threads/regeneration.md` — LIVE. Route A SUPPORTED (Directive 19): the conditional-rate experiment confirms family-independent post-startup event rate. The gap is: λ̂ = 0.585 is measured, not bounded below for all k. Next step is a lower bound on the rate, not another estimate.
- `research/threads/rule90-regeneration.md` — CLOSED.

### Refuted this cycle (do not re-assert)

- **"Route A refuted by sweep" — WITHDRAWN (Directive 16).** The sweep deaths are g_0 startup.
- **Bounded-support re-scope — REFUTED as vacuous (Directive 13).**
- **D=40 smoke numbers — DISCARDED (Directive 19), predate sign fix.**