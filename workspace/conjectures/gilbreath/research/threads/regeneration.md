```thread
question: Can we bound the (2,4)-event rate from below, and does that bound suffice to keep b_k ≥ 1 for all k?
status: open — step law and recharge identity are exact (verified depth 800, zero failures); the conjecture is now the event-rate inequality
rests-on: |
  - Step law: b_{k+1} ≥ b_k ⟺ (x,y) = (2,4), else b_{k+1} = b_k − 1. Verified independently to depth 800 (0 failures). code/out/step_law_and_recharge_verified.md.
  - Recharge identity: b_k = b_1 + Σ_{events i<k} (j_i + 1) − (k−1). Verified independently to depth 800 (0 failures). The conjecture holds iff Σ (j_i + 1) ≥ k−1−b_1 for all k.
  - Drain law: during erosion, y_{k+1} = y_k − 2·[x_k = 2]. Verified 101/101. code/out/regeneration_analysis.captured.txt.
  - Block lemma (proved): constant = 1, n+1 rows per length-n block. research/notes/block_lemma.md.
  - Rule 90 interior (proved): halved entries evolve under XOR. research/notes/rule90-interior.md.
  - CHT 2026 Theorem 1.6: only obstructions to decay are long zero-blocks or long shallow {0,d}-blocks.
  - Eppstein 2011: gap bounds alone do not suffice; must add non-concentration or restrict to primes.
blocked-by: nothing — the step law and recharge identity are exact; what remains is bounding the event rate
next: |
  1. Extract inter-event gap distribution and jump-size distribution from blocks_depth1000.json. Measure cumulative recharge vs consumption at each event, worst-case inter-event gap, and whether the surplus trend is growing or shrinking.
  2. Route A (combinatorial): prove a worst-case bound on erosion between events from the Rule 90 edge-flip dynamics + drain law. If the edge must flip to 2 within at most F(b) rows, then the max inter-event gap is bounded.
  3. Route B (analytic): assume a prime-gap hypothesis, derive a lower bound on event density. Must state how it beats Eppstein.
  4. Deliverable: a theorem of the form "under hypothesis H, the event rate ≥ r, and r suffices."
```

# Regeneration thread — event-rate lower bound

## The state of the problem

Erosion is settled. The step law and recharge identity are exact:
- **Step law:** `b_{k+1} ≥ b_k ⟺ (x,y) = (2,4)`, else `b_{k+1} = b_k − 1`
- **Recharge:** `b_k = b_1 + Σ_{events i<k} (j_i + 1) − (k−1)`

Both verified independently to depth 800 with zero failures (`code/out/step_law_and_recharge_verified.md`). The drain law (`y_{k+1} = y_k − 2·[x_k = 2]`) is also verified 101/101. These are combinatorial facts about the absolute-difference operator, not facts about primes.

The conjecture is now exactly: **do (2,4)-events keep arriving fast enough that `Σ (j_i + 1)` never falls `k−1` behind?** Since `b_1 = 2` and `j_i ≥ 0`, the recharge identity gives `b_k = 2 + Σ (j_i+1) − (k−1)`. The conjecture `b_k ≥ 1` for all k is equivalent to `Σ_{i<k} (j_i + 1) ≥ k − 2`.

## What we know

- **Consumption is exact, not just bounded.** The step law says `b_{k+1} = b_k − 1` at every non-event row. No "at most" — it is exactly one per row. The Odlyzko block lemma (constant 1) is the same fact from a different angle.

- **Regeneration is a single-row local property.** With `e_k = A_k[b_k]` (correct edge index), `b_{k+1} ≥ b_k ⟺ (e_k==2, c_k==4)`. Zero failures over 998 transitions, 60 events. The old off-by-one "refutation" is withdrawn.

- **The drain law governs the intruder between events.** During erosion, `y_{k+1} = y_k` when `x_k=0`, and `y_{k+1} = y_k − 2` when `x_k=2`. The intruder is monotone non-increasing, reaches 4 and sticks. This plus the Rule 90 edge-flip dynamics is the combinatorial engine for Route A.

- **The recharge identity is exact accounting.** `b_k = 2 + Σ (j_i+1) − (k−1)`. Empirically the surplus is enormous (272× at depth 800), but that is a fact about 800 rows, not a theorem. The recharge total is close to row width because a single event can refill most of the block — which is why the surplus looks large and must not be read as a trend.

## Two routes to the event-rate bound

### Route A — Combinatorial: bound max erosion between events

Between two (2,4)-events, the block erodes by exactly 1 per row. The intruder starts at some value ≥ 4 and drains to 4 (drop rate: 2 per row with edge=2, 0 per row with edge=0). The edge flips between 0 and 2 under the Rule 90 interior dynamics.

A lemma bounding the longest possible run of (edge=0, intruder=4) before the edge flips to 2 would give a worst-case inter-event gap. This is a combinatorial claim: within a {0,2} block of length b, evolving under XOR, with an intruder y draining by the drain law, what is the maximum number of consecutive rows with edge=0?

If this maximum is G(b), then events are at most G(b) rows apart, and the recharge inequality can be checked. The Rule 90 depth-d=2^j prediction (`research/threads/rule90-regeneration.md`) is a candidate mechanism: if the edge flips to 2 at depths that are powers of 2, then G(b) ≤ 2^⌈log₂(b)⌉.

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