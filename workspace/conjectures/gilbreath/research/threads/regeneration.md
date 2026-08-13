```thread
question: What makes the giant jumps recur? If b grows geometrically at giants, the conjecture reduces to "giants arrive infinitely often" — no rate bound needed.
status: open — bigjump characterisation DONE (12 genuine, 1 capped); Directive 24: test geometric vs linear growth of b at giants, find k* where width caps measurements
rests-on: |
  - Step law (PROVED): b_{k+1} ≥ b_k ⟺ (x,y) = (2,4), else b_{k+1} = b_k − 1. Theorems of the absolute-difference operator for ANY array (no parity, no primes), proof in research/notes/step_law_proved.md; verified on real primes depth 1000 (0 failures) and 400 random arrays (3,521 rows, 610 events, 0 failures).
  - Recharge identity (PROVED): b_k = b_1 + Σ_{events i<k} (j_i + 1) − (k−1). research/notes/step_law_proved.md. The conjecture holds iff Σ (j_i + 1) ≥ k−1−b_1 for all k.
  - Drain law (PROVED): during erosion, y_{k+1} = y_k − 2·[x_k = 2]. Corollary of the step law; verified 101/101. code/out/regeneration_analysis.captured.txt.
  - Block lemma (proved): constant = 1, n+1 rows per length-n block. research/notes/block_lemma.md.
  - Rule 90 interior (proved): halved entries evolve under XOR. research/notes/rule90-interior.md. The depth-d=2^j timing corollary is REFUTED (see rule90-regeneration thread); the interior identification stands as the edge-flip mechanism for Route A.
  - CHT 2026 Theorem 1.6: only obstructions to decay are long zero-blocks or long shallow {0,d}-blocks. hypotheses checked, R_0=4.2e8 ≫ 1000, does not bite at reachable depths.
  - Eppstein 2011: gap bounds alone do not suffice; must add non-concentration or restrict to primes.
  - **Event-rate sweep (Directive 12, this run, 1154 sequences):** the step law and recharge identity hold on ALL sequences (zero failures, 46,528 rows, 20,013 events) — the mechanism IS combinatorial. 852/1154 (73.8%) reach b_k = 0, but ALL deaths within first 10 rows (764/852 by k≤3, 852/852 by k≤10). **Directive 16 correction:** these deaths are g_0 startup, NOT the asymptotic event rate. Route A is RESTORED as live.
  - **Conditional-rate experiment (Directive 19, DONE):** D=400, W=200000, seeds 10000..10019, 26 workers, commit ae69d093 (sign fix). Pooled λ̂ = 0.585 (1098/1876), Pearson X² p = 0.68 over 8 families. 3 corner-class families (consecutive, f2-rand24, rand24) immortal with zero eligible rows — contribute nothing. **Post-startup event rate is family-independent → Route A supported.** λ̂ is measured, not bounded below for all k. Do NOT cite D=40 smoke (predates sign fix, discarded). Anchors: code/out/conditional_rate_experiment.captured.txt, code/out/conditional_rate_records.jsonl, code/out/conditional_rate_experiment.notes.md.
  - Directive 13 stands independently: bounded finite support is vacuous for the primes (gaps 8,10,12,14,34 below 2000; unbounded).
blocked-by: nothing — the mechanism is proved combinatorial; the conditional-rate experiment is done and supports Route A; the remaining step is width-degradation + geometric growth test
next: |
  1. **Width-degradation caveat (Directive 24).** Compute k* = the first row k where W − k − b_k < J_min (reasonable J_min = 1000, the threshold from the bigjump table). The floor column runs 1,268,392 (i=34) → 0 (i=161), cols shrinks 1,270,572 → 1,270,445 — data degrades continuously, not only at i=161. Mark every measurement past k* as a lower bound. Every claim on the bigjump table must carry this caveat.
  2. **Geometric growth test (Directive 24).** b at giant events: 865→2179, 4203→5942, 5939→23265, 141706→271629, 325096→515906, 515907→733564, 733575→1094273. Fit log(b) vs event index (linear = exponential growth) and b vs event index (linear growth). Report residuals. If geometric: the target is NOT a lower bound on the event rate but a proof that the inter-giant gap is finite — geometric growth makes Σ(j+1) ≫ k trivially, so giants need only arrive at ALL, at any rate. If linear: the event-rate lower-bound route remains live.
  3. **Restate the target** based on the outcome. The mean-rate-bound route (λ̂ ≈ 0.585) is already superseded per Directive 23; the geometric-growth finding determines whether even a gap-bound is the right object.

# Regeneration thread — from event rate to geometric growth

**Directive 23 reframing (DONE):** the event-rate route targets a MEAN (λ̂ ≈ 0.585), and a mean is the wrong summary for a heavy-tailed jump distribution. At depth 1000 the recharge identity holds with enormous slack — S_1000 = 1,270,603 vs required 998, b_1000 = 1.27M ≫ 1 — and that surplus is carried by a handful of giant jumps.

**Bigjump characterisation (DONE, Directive 23 item 1).** Of 13 (2,4)-events with j > 1000, 12 are GENUINE (landing block ends strictly inside the finite row; floor distances 176186..1268392) and only i=161 is CAPPED-ARTIFACT (b_162 = 1,270,444 = W − 162 − 1; j ≥ 176,181 is a lower bound). Genuine giants carry 86.1% of S_1000. The heavy tail is genuine prime renewal structure, not a finite-width effect. Claim `bigjump-cap-characterization-1000`. Anchors: `code/out/bigjump_characterization.captured.txt`, `code/out/bigjump_characterization.notes.md`.

**Directive 24 reframing:** two immediate steps.

### 1. Width-degradation caveat

The bigjump table's floor column runs 1,268,392 (i=34) → 0 (i=161), cols shrinks 1,270,572 → 1,270,445. The data degrades continuously, not only at i=161. Compute k* = the first row where W − k − b_k < J_min (J_min = 1000, matching the threshold used in bigjump_characterization). Every measurement past k* must be marked as a lower bound. Every claim resting on the bigjump table needs this caveat.

### 2. Geometric growth test

b at consecutive giant events: 865→2179, 4203→5942, 5939→23265, 141706→271629, 325096→515906, 515907→733564, 733575→1094273. This looks roughly geometric (each giant roughly doubles or triples b). Fit log(b) vs event index (geometric = exponential) and b vs event index (linear). Report residuals.

**If geometric:** the conjecture reduces to a much weaker statement. Geometric growth in b means that at each giant event, the block length multiplies by a factor > 1 — so Σ(j+1) outpaces k by an exponentially growing margin, and the recharge inequality Σ(j+1) ≥ k−2 is trivially satisfied past some finite k. The only way the conjecture could fail is if giants STOP ARRIVING — i.e., if there is a last giant and after that b erodes to 0 linearly. So the target becomes: **prove the inter-giant gap is finite** — that giants keep arriving, at any rate. No lower bound on the mean event rate is needed.

**If linear:** the event-rate lower-bound route remains live, and the heavy-tail structure alone does not relax the target.

### 3. Restate the target

Based on the outcome of item 2, restate the conjecture's condition in `research/threads/regeneration.md`. The mean-rate-bound route (λ̂ ≈ 0.585) is already superseded per Directive 23. The geometric-growth finding determines whether even a gap-bound is the right object.

## The state of the problem

Erosion is settled. The step law and recharge identity are exact:
- **Step law:** `b_{k+1} ≥ b_k ⟺ (x,y) = (2,4)`, else `b_{k+1} = b_k − 1`
- **Recharge:** `b_k = b_1 + Σ_{events i<k} (j_i + 1) − (k−1)`

Both verified independently to depth 800 with zero failures (`code/out/step_law_and_recharge_verified.md`). The drain law (`y_{k+1} = y_k − 2·[x_k = 2]`) is also verified 101/101. These are combinatorial facts about the absolute-difference operator, not facts about primes.

The conjecture is now exactly: **do (2,4)-events keep arriving fast enough that `Σ (j_i + 1)` never falls `k−1` behind?** Since `b_1 = 2` and `j_i ≥ 0`, the recharge identity gives `b_k = 2 + Σ (j_i+1) − (k−1)`. The conjecture `b_k ≥ 1` for all k is equivalent to `Σ_{i<k} (j_i + 1) ≥ k − 2`.

**The mechanism is combinatorial; the rate is family-independent post-startup (Directive 19).**
The conditional-rate experiment (D=400, W=200000, 26 workers, commit ae69d093) confirms:
pooled λ̂ = 0.585 (1098/1876), Pearson X² p = 0.68 over 8 families. Post-startup, every
live family generates events at the same rate — this is what a combinatorial mechanism
looks like. 3 corner-class families (consecutive, f2-rand24, rand24) are immortal with
zero eligible rows and contribute nothing to the pooled figure. **The gap:** λ̂ is
measured, not bounded below for all k. The conjecture needs Σ(j_i+1) ≥ k−2 holding
everywhere, which requires a rate lower bound, not a point estimate. Do NOT cite the
discarded D=40 smoke numbers (predate sign fix).

The event-rate sweep deaths (852/1154, all within first 10 rows) are g_0 startup —
Directive 16's correction stands. The conditional-rate experiment isolates the rate
from the startup and supports Route A.

## What we know

- **Consumption is exact, not just bounded.** The step law says `b_{k+1} = b_k − 1` at every non-event row. No "at most" — it is exactly one per row. The Odlyzko block lemma (constant 1) is the same fact from a different angle.

- **Regeneration is a single-row local property.** With `e_k = A_k[b_k]` (correct edge index), `b_{k+1} ≥ b_k ⟺ (e_k==2, c_k==4)`. Zero failures over 998 transitions, 60 events. The old off-by-one "refutation" is withdrawn.

- **The drain law governs the intruder between events.** During erosion, `y_{k+1} = y_k` when `x_k=0`, and `y_{k+1} = y_k − 2` when `x_k=2`. The intruder is monotone non-increasing, reaches 4 and sticks. This plus the Rule 90 edge-flip dynamics is the combinatorial engine for Route A.

- **The recharge identity is exact accounting.** `b_k = 2 + Σ (j_i+1) − (k−1)`. Empirically the surplus is enormous (272× at depth 800), but that is a fact about 800 rows, not a theorem. The recharge total is close to row width because a single event can refill most of the block — which is why the surplus looks large and must not be read as a trend.

## Two routes to the event-rate bound

### Route A — Combinatorial: bound max erosion between events (now supported by conditional-rate experiment)

The conditional-rate experiment (Directive 19, DONE) confirms: post-startup (k>10), the (2,4)-event rate is family-independent (pooled λ̂ = 0.585, Pearson X² p = 0.68 over 8 families). The mechanism is combinatorial. **The gap:** λ̂ is measured, not bounded below for all k.

Between two (2,4)-events, the block erodes by exactly 1 per row. The intruder starts at some value ≥ 4 and drains to 4 (drop rate: 2 per row with edge=2, 0 per row with edge=0). The edge flips between 0 and 2 under the Rule 90 interior dynamics.

A lemma bounding the longest possible run of (edge=0, intruder=4) before the edge flips to 2 would give a worst-case inter-event gap. This is a combinatorial claim: within a {0,2} block of length b, evolving under XOR, with an intruder y draining by the drain law, what is the maximum number of consecutive rows with edge=0?

The conditional-rate experiment (Directive 19) confirms the rate is family-independent post-startup — the mechanism is combinatorial. The gap is that λ̂=0.585 is measured, not bounded. The lemma must produce a LOWER BOUND on the rate, not an estimate. If the worst-case inter-event gap is G(b), then the rate is at least 1/(G(b)+1), and the recharge inequality can be checked.

**Directive 13 stands:** bounded finite support is vacuous for the primes. The lemma must work without assuming finite gap support.

### Route B — Analytic: bound event density from prime gaps

Assume a hypothesis on prime gaps and derive a lower bound on (2,4)-event frequency. The intruder at row k is ultimately derived from a prime gap at the block boundary. Under even a weak gap bound, can one show the intruder reaches 4 at a rate that keeps the recharge sum ahead?

This is the "general class with gap bound + non-concentration" route. Must state explicitly how it beats Eppstein's anti-Gilbreath construction (which has small gaps but fails the conjecture). The CHT 2-separation hypothesis is the natural candidate.

## First step: measure

Before attempting either proof, extract from `blocks_depth1000.json`:
- Inter-event gap distribution
- Jump-size distribution
- Cumulative recharge vs consumption at each event
- Worst-case inter-event gap and block length at gap start
- Whether the recharge surplus trend is growing or shrinking

The data already exists. One program, run it, report the numbers.

## Data available
- `code/out/blocks_depth1000.json`; `code/out/regeneration_analysis.captured.txt`; `code/out/check_regenerate_lemma.captured.txt`; `code/out/step_law_and_recharge_verified.md`; `code/out/step_law_captured.txt`; `code/out/step_law_independent.captured.txt`
- Sources: Odlyzko 1993, Killgrove–Ralston 1959, Chase 2024, CHT 2026, Eppstein 2011