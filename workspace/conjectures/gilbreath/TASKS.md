# Tasks

## Directive 18 (steer): build-check probe

Build a focused probe program that measures one specific structural quantity
on the prime rows (depth 1000, `blocks_depth1000.json`). A probe is small,
fast, and answers one question definitively — it is not a sweep and not a
search.

### Immediate (in order)

- [ ] **1. Build and check a probe on the prime rows.** The step law makes
  regeneration a local event at `(edge, intruder) = (2,4)`, so the open
  question is: how often is `edge = 2`? The block's last entry (column b_k)
  is the necessary half of the regeneration trigger. Measure:
  - The sequence of edge values e_k = A_k[b_k] for k = 1..161 (live regime
    where the intruder exists). Count how many are 0 vs 2.
  - The distribution of run-lengths of consecutive edge=2 and edge=0.
  - Whether edge=2 has a detectable period or pattern (autocorrelation,
    spacing distribution).
  - The fraction of rows with edge=2 (this is the upper bound on the
    event rate, since every (2,4)-event requires edge=2).

  Write a small program that reads `blocks_depth1000.json`, extracts the
  edge sequence for live rows, computes the statistics above, and captures
  to `code/out/probe_edge_sequence.captured.txt`. This is independent of the
  conditional-rate experiment and can run in parallel with it.

  **Why this probe:** the recharge identity `b_k = 2 + Σ(j_i+1) − (k−1)`
  reduces the conjecture to the (2,4)-event rate. If edge=2 occurs with a
  structural frequency (not random), that frequency bounds the event rate
  from below — because intruder=4 is absorbing (drain law) and edge=2 is the
  only missing piece. If edge=2 appears to be random/unpatterned, that is
  also a finding: it tells us the rate question is genuinely probabilistic
  rather than structural.

- [ ] **2. Conditional-rate experiment: isolate the asymptotic event rate from the g_0 startup.** Use the existing sweep data (26 families × seeds, 1154 sequences, 302 survivors). Restrict to sequences that survived past row 10 (b_k ≥ 1 at k=11). On those only, measure:
  - events per row (event density) by family
  - whether the per-family densities are distinguishable (family-dependent → real evidence about the rate; family-independent → combinatorial mechanism, Route A is right)
  - inter-event gap distribution conditional on k>10
  - comparison to the prime rows' event density (60 events / 161 live rows = 0.373)

  The sweep data already has per-sequence event counts and row counts. Write a
  small program that reads the sweep JSON, filters to k>10 survivors, computes
  conditional densities per family, and reports whether the densities cluster
  (same across families) or separate. Capture to
  `code/out/conditional_rate_experiment.captured.txt`.

  **This is the blocking task for the Route A/B question.** It answers whether the event rate is
  combinatorial (Route A) or input-dependent (Route B). Either answer is
  progress — a third approach is not.

### Directive 17 (steer): Lean formalisation verified complete. Record as gilbreath-second-entry-equivalence, an IFF reformulation not a reduction. Axiom footprint [propext, Classical.choice, Quot.sound].

### Directive 16 (steer): Route A is NOT refuted. Sweep deaths are g_0 startup, not rate. Run conditional-rate experiment (now item 2 above).

Directive 12 said the sweep refutes Route A as a purely combinatorial lemma
because a combinatorial rate bound would contradict families dying 100%. That
inference is wrong. The sweep data itself shows:

- Death is determined by INITIALISATION: 764/852 deaths by k≤3, 852/852 by k≤10. Nothing dies late.
- rand24 deaths at k=1 (theorem: iff g_0=4): 30/48. rand24 survivors trunc_k=2 (theorem: iff g_0=2): 18/18.
- Wide-support families die more because they more often draw g_0≠2 and die at row 1.

So the sweep measures the STARTUP TRANSIENT, not the asymptotic event rate. The
phase-boundary table is a g_0 artifact. Route A's claim — that the event rate
is combinatorial — is UNTESTED by the sweep, not refuted. **Route A is restored
as live.** The Directive 13 correction stands independently: bounded gap support
is vacuous for the primes (gaps 8,10,12,14,34 below 2000; unbounded).

The separation verdict (gap_hypothesis_separation.captured.txt — DONE this
cycle) is still correct and still useful: no first-moment or tail statistic
separates primes from {2..20}, and the random model is TAMER (max gap 20 vs 86,
freq>50 = 0 vs 0.00345) yet dies. Given the g_0 explanation, that death happens
at k≤1 from first-gap≠2, not from the event rate.

### Immediate (in order — item 1 blocks everything else)

- [ ] **1. Conditional-rate experiment: isolate the asymptotic event rate from the g_0 startup.** Use the existing sweep data (26 families × seeds, 1154 sequences, 302 survivors). Restrict to sequences that survived past row 10 (b_k ≥ 1 at k=11). On those only, measure:
  - events per row (event density) by family
  - whether the per-family densities are distinguishable (family-dependent → real evidence about the rate; family-independent → combinatorial mechanism, Route A is right)
  - inter-event gap distribution conditional on k>10
  - comparison to the prime rows' event density (60 events / 161 live rows = 0.373)

  The sweep data already has per-sequence event counts and row counts. Write a
  small program that reads the sweep JSON, filters to k>10 survivors, computes
  conditional densities per family, and reports whether the densities cluster
  (same across families) or separate. Capture to
  `code/out/conditional_rate_experiment.captured.txt`.

  **This is the single blocking task.** It answers whether the event rate is
  combinatorial (Route A) or input-dependent (Route B). Either answer is
  progress — a third approach is not.

### Deferred until item 1 is answered

- [ ] **2. Housekeeping: move bare .txt output files from `code/pattern_finder/` to `code/out/` or delete them.** Requires a shell (`mv`/`rm`); this role has no move/delete tool.
- [x] **3. Lean 4 formalisation — COMPLETE (Directive 17 verified).**
  Nine theorems kernel-checked across `gilbreath_reduction.lean`, `reduction.lean`,
  `shape.lean`: `dist_odd_even`, `dist_dist_even`, `dist_one_eq_one`,
  `shape_theorem`, `shape_rows`, `reduction`, `reduction_lemma`,
  `gilbreath_reduction`. Every declaration depends on exactly
  `[propext, Classical.choice, Quot.sound]` (the three standard Mathlib axioms),
  **zero sorry / zero sorryAx** (grep-verified on three capture files).
  `gilbreath_reduction : GilbreathConjecture X ↔ SecondEntryIn02 X` is an
  **IFF-machine-checked equivalence, not a reduction**: the {0,2} statement is
  exactly as hard as the conjecture — it reformulates rather than reduces.
  The prime instantiation (row 1 = (1, even, even, ...)) remains
  computation-checked (witnesses.json), not Lean-proved. Claim:
  `gilbreath-second-entry-equivalence`. Anchors:
  `code/lean/gilbreath_reduction.lean`, `code/out/lean_gilbreath_reduction.captured.txt`.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal:** `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`; `b_k = 2 + Σ(j_i+1) − (k−1)`. Zero failures on all 1,154 sweep sequences AND primes. `code/out/step_law_and_recharge_verified.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified 101/101; combinatorial.
- **Event-rate sweep (this run, 1,154 sequences):** step law + recharge identity universal (0 failures); 852/1,154 (73.8%) reach b_k=0, ALL within first 10 rows (764/852 by k≤3). Deaths are g_0 startup: rand24 deaths at k=1 from g_0=4; survivors at trunc_k=2 from g_0=2. Sweep does NOT bear on the asymptotic event rate. `code/out/event_rate_sweep_analysis.captured.txt`, `code/out/event_rate_sweep.notes.md`.
- **Gap-hypothesis separation check — DONE (Directive 15).** None of the three candidates (bounded mean gap per window, frequency of gaps > G, Cramér g_n = O(log² p_n)) separates primes from {2..20}; all three are satisfied by both columns. `code/out/gap_hypothesis_separation.captured.txt`. The separation verdict is correct — but the sweep deaths are explained by g_0≠2 at k≤1, not by gap statistics.
- **CHT Theorem 1.6 hypothesis check — DONE.** M=7, L=2, R_0=419,430,400 ≫ 1000; `holds-here: no`. `code/out/cht_hyp_check.captured.txt`.
- **Rule 90 depth prediction — CLOSED** (null computed; tol=1 p=0.017, tol=0 dead). Thread `research/threads/rule90-regeneration.md`.
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000).
- **Library:** 92 sources on disk, downloads halted; no downloads until a specific gap is stated.

### Threads

- `research/threads/regeneration.md` — LIVE. Route A RESTORED (Directive 16): the sweep refutes startup, not rate. The open question is the conditional event rate (item 1). Route B (analytic, prime-gap hypothesis) unchanged but secondary.
- `research/threads/rule90-regeneration.md` — CLOSED (Directive 9). Depth-timing corollary refuted; the proved Rule 90 interior identification stands.

### Refuted this cycle (do not re-assert)

- **"Route A refuted by sweep" — WITHDRAWN (Directive 16).** The sweep deaths are g_0 startup (all within k≤10, 90% by k≤3); they do not bear on the asymptotic event rate. Route A is live.
- **Bounded-support re-scope "gaps ⊆ {2,4,6}, first gap = 2" — REFUTED as vacuous (Directive 13).** The primes violate every finite gap-support condition (gaps 8,10,12,14,34 below 2000; unbounded in general). A theorem conditional on finite support says nothing about Gilbreath.
- **"The primes satisfy this" (re the bounded-support claim) — REFUTED and removed (Directive 14).** Was still present at line 16 in the `next:` block of `research/threads/regeneration.md` after Directive 13 corrected other lines.
