```thread
question: Can we bound the (2,4)-event rate from below, and does that bound suffice to keep b_k ≥ 1 for all k?
status: open — step law + recharge identity PROVED; Route A RESTORED live (Directive 16: sweep deaths are g_0 startup, not rate); conditional-rate experiment is the blocking task
rests-on: |
  - Step law (PROVED): b_{k+1} ≥ b_k ⟺ (x,y) = (2,4), else b_{k+1} = b_k − 1. Theorems of the absolute-difference operator for ANY array (no parity, no primes), proof in research/notes/step_law_proved.md; verified on real primes depth 1000 (0 failures) and 400 random arrays (3,521 rows, 610 events, 0 failures).
  - Recharge identity (PROVED): b_k = b_1 + Σ_{events i<k} (j_i + 1) − (k−1). research/notes/step_law_proved.md. The conjecture holds iff Σ (j_i + 1) ≥ k−1−b_1 for all k.
  - Drain law (PROVED): during erosion, y_{k+1} = y_k − 2·[x_k = 2]. Corollary of the step law; verified 101/101. code/out/regeneration_analysis.captured.txt.
  - Block lemma (proved): constant = 1, n+1 rows per length-n block. research/notes/block_lemma.md.
  - Rule 90 interior (proved): halved entries evolve under XOR. research/notes/rule90-interior.md. The depth-d=2^j timing corollary is REFUTED (see rule90-regeneration thread); the interior identification stands as the edge-flip mechanism for Route A.
  - CHT 2026 Theorem 1.6: only obstructions to decay are long zero-blocks or long shallow {0,d}-blocks. hypotheses checked, R_0=4.2e8 ≫ 1000, does not bite at reachable depths.
  - Eppstein 2011: gap bounds alone do not suffice; must add non-concentration or restrict to primes.
  - **Event-rate sweep (Directive 12, this run, 1154 sequences):** the step law and recharge identity hold on ALL sequences (zero failures, 46,528 rows, 20,013 events) — the mechanism IS combinatorial. 852/1154 (73.8%) reach b_k = 0, but ALL deaths within first 10 rows (764/852 by k≤3, 852/852 by k≤10). **Directive 16 correction:** these deaths are g_0 startup, NOT the asymptotic event rate. rand24 deaths at k=1 (iff g_0=4): 30/48; survivors at trunc_k=2 (iff g_0=2): 18/18. Wide-support families die more because they more often draw g_0≠2 and die at row 1. The sweep measures INITIALISATION, so it does NOT refute Route A. Route A is RESTORED as live. **The conditional-rate experiment (restrict to k>10 survivors, measure per-family event density) is the blocking task.** code/out/event_rate_sweep_analysis.captured.txt.
  - **Gap-hypothesis separation check — DONE (Directive 15).** None of H1/H2/H3 separates primes from {2..20}; all three satisfied by both columns. This is correct — but the sweep deaths are g_0 startup, not gap statistics. code/out/gap_hypothesis_separation.captured.txt.
  - Directive 13 stands independently: bounded finite support is vacuous for the primes (gaps 8,10,12,14,34 below 2000; unbounded).
blocked-by: nothing — the step law and recharge identity are exact and universal; the conditional-rate experiment (TASKS item 1) is the next step
next: |
  1. **Run the conditional-rate experiment (TASKS item 1).** Read sweep JSON, filter to sequences surviving past k=10, compute per-family event density. Family-independent → Route A combinatorial; family-dependent → real evidence about rate. Capture to `code/out/conditional_rate_experiment.captured.txt`.
  2. Route A (combinatorial): prove a worst-case bound on erosion between events from the Rule 90 edge-flip dynamics + drain law. The mechanism is combinatorial; the g_0 startup artefact is irrelevant to the rate question. If the conditional experiment shows family-independent event density, Route A is the correct framing.
  3. Route B (analytic, secondary): assume a prime-gap hypothesis, derive a lower bound on event density. Must state how it beats Eppstein.
  4. Deliverable: a theorem of the form "under hypothesis H, the event rate ≥ r, and r suffices."

lean-formalisation: |
  COMPLETE (Directive 17 verified). Nine theorems kernel-checked. gilbreath_reduction : GilbreathConjecture X ↔ SecondEntryIn02 X is an IFF — the {0,2} second-entry statement is exactly as hard as the conjecture, not a simplification. Axiom footprint [propext, Classical.choice, Quot.sound]. Zero sorry/sorryAx. claim: gilbreath-second-entry-equivalence, anchor: code/lean/gilbreath_reduction.lean.
```

# Regeneration thread — event-rate lower bound

## The state of the problem

Erosion is settled. The step law and recharge identity are exact:
- **Step law:** `b_{k+1} ≥ b_k ⟺ (x,y) = (2,4)`, else `b_{k+1} = b_k − 1`
- **Recharge:** `b_k = b_1 + Σ_{events i<k} (j_i + 1) − (k−1)`

Both verified independently to depth 800 with zero failures (`code/out/step_law_and_recharge_verified.md`). The drain law (`y_{k+1} = y_k − 2·[x_k = 2]`) is also verified 101/101. These are combinatorial facts about the absolute-difference operator, not facts about primes.

The conjecture is now exactly: **do (2,4)-events keep arriving fast enough that `Σ (j_i + 1)` never falls `k−1` behind?** Since `b_1 = 2` and `j_i ≥ 0`, the recharge identity gives `b_k = 2 + Σ (j_i+1) − (k−1)`. The conjecture `b_k ≥ 1` for all k is equivalent to `Σ_{i<k} (j_i + 1) ≥ k − 2`.

**The mechanism is combinatorial; the rate is not (Directive 12).** The event-rate
sweep over 1,154 random 2-then-odds sequences settles this: the step law and
recharge identity hold universally (zero failures, 46,528 rows, 20,013 events
across all families), confirming the mechanism is a fact about the operator
`|a−b|`. But the event RATE — whether `Σ (j_i+1) ≥ k−2` holds — is sharply
dependent on the gap support. 852/1,154 sequences (73.8%) reach `b_k = 0`, all
deaths within the first 10 rows. The phase boundary (sweep batch, n=48 per family):

| gap support | % die | first-gap-2 helps? |
|---|---|---|
| `{2}` | 0% | N/A (primes-like) |
| `{2,4}` | 62% | yes — 0% with f2 |
| `{2,4,6}` | 94% | drops to 60% with f2 |
| `{2..20}` | 100% | still 100% with f2 |
| `{2..100}` | 100% | still 100% with f2 |
| Geom(p=.25) | 100% | still 100% with f2 |

A purely combinatorial bound on the event rate from the `{0,2}` interior + drain law
alone would have to hold for `{2..20}` and Geom(p=.25) — but those die 100% of the
time. So Route A cannot be "no prime input." It MUST include a gap-support hypothesis
that the dying families violate. Route A is re-scoped accordingly: the mechanism
(step law, drain law, edge-flip) is combinatorial; the rate hypothesis is about the
input sequence's gap profile. **Directive 13: the bounded-support form (gaps ⊆ {2,4,6}, first gap 2) is VACUOUS for Gilbreath — the primes do NOT satisfy it (gaps 8,10,12,14,34 occur below 2000; prime gaps are unbounded), so no finite-support hypothesis holds.** The separating property must be a CONCENTRATION condition that tolerates rare large gaps; pick one (bounded mean gap per window / frequency of gaps > G / Cramér g_n = O(log² p_n)) and check it against both the primes and {2..20} before writing it in.

**Directive 16 correction:** the inference that the sweep refutes Route A is WRONG. The sweep data shows deaths are g_0 startup: 764/852 by k≤3, 852/852 by k≤10, nothing dies late. rand24 deaths at k=1 (iff g_0=4): 30/48; survivors at trunc_k=2 (iff g_0=2): 18/18. Wide-support families die more because they more often draw g_0≠2 and die at row 1. The sweep measures INITIALISATION, not the asymptotic event rate. Route A is RESTORED as live: the mechanism is combinatorial, and the conditional-rate experiment (restrict to k>10 survivors) is what will test it.

## What we know

- **Consumption is exact, not just bounded.** The step law says `b_{k+1} = b_k − 1` at every non-event row. No "at most" — it is exactly one per row. The Odlyzko block lemma (constant 1) is the same fact from a different angle.

- **Regeneration is a single-row local property.** With `e_k = A_k[b_k]` (correct edge index), `b_{k+1} ≥ b_k ⟺ (e_k==2, c_k==4)`. Zero failures over 998 transitions, 60 events. The old off-by-one "refutation" is withdrawn.

- **The drain law governs the intruder between events.** During erosion, `y_{k+1} = y_k` when `x_k=0`, and `y_{k+1} = y_k − 2` when `x_k=2`. The intruder is monotone non-increasing, reaches 4 and sticks. This plus the Rule 90 edge-flip dynamics is the combinatorial engine for Route A.

- **The recharge identity is exact accounting.** `b_k = 2 + Σ (j_i+1) − (k−1)`. Empirically the surplus is enormous (272× at depth 800), but that is a fact about 800 rows, not a theorem. The recharge total is close to row width because a single event can refill most of the block — which is why the surplus looks large and must not be read as a trend.

## Two routes to the event-rate bound

### Route A — Combinatorial + concentration hypothesis: bound max erosion between events

Between two (2,4)-events, the block erodes by exactly 1 per row. The intruder starts at some value ≥ 4 and drains to 4 (drop rate: 2 per row with edge=2, 0 per row with edge=0). The edge flips between 0 and 2 under the Rule 90 interior dynamics.

A lemma bounding the longest possible run of (edge=0, intruder=4) before the edge flips to 2 would give a worst-case inter-event gap. This is a combinatorial claim: within a {0,2} block of length b, evolving under XOR, with an intruder y draining by the drain law, what is the maximum number of consecutive rows with edge=0?

**Re-scoped per Directive 12, corrected per Directive 13:** the event-rate sweep refutes a purely combinatorial bound. Any such lemma must additionally assume a hypothesis on the input sequence's gaps that the dying sweep families ({2..20}, Geom(p=.25)) violate. **The bounded-support form (gaps ⊆ {2,4,6}, first gap = 2) is VACUOUS for the primes** — gaps 8,10,12,14,34 occur below 2000 and prime gaps are unbounded, so no finite-support hypothesis holds. The hypothesis must be a CONCENTRATION condition that tolerates rare large gaps (bounded mean gap per window / frequency of gaps > G / Cramér g_n = O(log² p_n)); pick one and check it against BOTH primes and {2..20}. Without a separating hypothesis, the lemma would prove a bound false for the dying families — a contradiction.

If this maximum is G(b) under the concentration hypothesis, then events are at most G(b) rows apart, and the recharge inequality can be checked.

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