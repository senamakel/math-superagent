# Tasks

## Directive 6 (steer): Erosion settled. Step law exact. Focus everything on the event-rate lower bound.

The step law and recharge identity are verified independently (operator, `code/out/step_law_and_recharge_verified.md`):
- **Step law:** `b_{k+1} ≥ b_k ⟺ (x,y) = (2,4)`, else `b_{k+1} = b_k − 1`
- **Recharge:** `b_k = b_1 + Σ_{events i<k} (j_i + 1) − (k−1)`
- Verified to depth 800 on 216,816 primes, zero failures. Do not re-derive.

The conjecture is now exactly: **do (2,4)-events keep arriving fast enough that `Σ (j_i + 1)` never falls `k−1` behind?** A lower bound on the event rate, even under a stated hypothesis on prime gaps, is a real result. Another verification of erosion is not.

### Primary

- [ ] **1. Bound the (2,4)-event rate from below.** This is the run's whole job now.

  The step law and recharge identity reduce the conjecture to a single inequality: for all k, `Σ_{i<k} (j_i + 1) ≥ k − 1 − b_1`. Since `b_1 = 2` and `j_i ≥ 0`, sufficient condition: at least one event every `J+1` rows where `J` is the typical jump. But jumps vary enormously (median 4.5, max 360,698), so the real question is the *distribution* of inter-event gaps and jump sizes.

  Two routes, pursue both in parallel:

  **Route A — Structural / combinatorial.** Prove that between any two (2,4)-events the block cannot erode by more than some function of the block length. The intruder drains at rate 2 per row when `x=2` and 0 when `x=0`; the edge flips 0↔2 under the Rule 90 interior dynamics. A lemma bounding the longest possible (edge=0, intruder=4) run before the edge flips to 2 would give a worst-case inter-event gap. This is a combinatorial claim about the {0,2} interior under XOR evolution plus the drain law — primes enter only through the initial bit pattern.

  **Route B — Analytic / prime-gap.** Assume a hypothesis on prime gaps (e.g. gaps ≤ f(n), or Cramér, or something weaker) and derive a lower bound on the density of (2,4)-events. The intruder starts as the gap between the prime at the block boundary and the next prime. Under even a weak gap bound, can one show the intruder reaches 4 often enough? This is the "general class with gap bound + 2-separation" route — must state how it beats Eppstein.

  **Deliverable for either route:** a theorem of the form "under hypothesis H, the (2,4)-event rate is at least r, and r suffices to keep b_k ≥ 1 for all k." Or: "under H, the maximum inter-event gap is at most G, and with minimum jump J_min the recharge never falls behind."

  **Measure first.** Before attempting either proof, extract from `blocks_depth1000.json`:
  - Inter-event gap distribution (rows between consecutive (2,4)-events)
  - Jump-size distribution
  - Cumulative recharge vs cumulative consumption at each event
  - Worst-case inter-event gap and the block length at the start of that gap
  - Whether the recharge surplus is growing or shrinking with k

  The data is in `code/out/blocks_depth1000.json`. Write one program to extract these, run it, report the numbers. Then pick the route the numbers support.

- [ ] **2. Rule 90 depth prediction — test as a candidate explanation for event timing.** If (2,4)-events cluster at depths that are powers of 2, the XOR-window mechanism is *why* the edge flips to 2 at the right moments. This feeds Route A directly: it would turn "the edge eventually flips to 2" into "the edge flips to 2 at depth 2^j." Test against the real data, report match/mismatch with exact numbers. This is a sub-task of item 1, not a separate investigation.

### Supporting (do not let these consume the run)

- [x] **3. CHT Theorem 1.6 hypothesis check — DONE, holds-here = no.** Sieve 2e7, 1,270,607 primes, 1,270,605 normalized gaps a_n=(p_{n+2}−p_{n+1})/2−1. **max a_n = 89** (prime gap 180, consecutive primes 17051707, 17051887) → **M = ceil(log2 89) = 7** (2^7=128 ≥ 89). **L = 2** (longest 0-run; only a_1=a_2=0). **R_0 = 100·L·8^M = 100·2·8^7 = 419,430,400** (~4.2e8, log2≈28.6). R_0 ≫ 1000, so the no-{0,d}-block hypothesis is **not satisfiable at any depth ≤ 1000** — the CHT protection window is of order ~4.2e8 rows, so the theorem does not bite at reachable depths. First nine a_n = 0,0,1,0,1,0,1,2,0 match the claim. Claim block `cht-inverse-theorem-hyp-check` (status checked) in `code/out/cht_hyp_check.notes.md`; program `code/cht_hyp/check_cht_hyp.py`, captured `code/out/cht_hyp_check.captured.txt`; independently recomputed by a second program.

- [ ] **4. Lean 4 formalisation.** Define the difference operator, prove shape preservation, reduce to {0,2} second-entry claim. Machine-checked lemma. Report `#print axioms` and every `sorry`. Independent of items 1–3, run in parallel.

### Background (established — do not re-derive or re-verify)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved and checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Step law and recharge identity:** verified independently by operator to depth 800, zero failures. `code/out/step_law_and_recharge_verified.md`. This is the accounting framework the whole run now uses.
- **Regeneration criterion:** b_{k+1} ≥ b_k ⟺ (A_k[b_k]==2 AND A_k[b_k+1]==4). Established to depth 1000, zero failures, 60/60 events. `code/out/check_regenerate_lemma.captured.txt`.
- **Drain law:** during erosion, y_{k+1} = y_k − 2·[x_k = 2]. Verified 101/101. `code/out/regeneration_analysis.captured.txt`.
- **Rule 90 interior (PROVED):** `research/notes/rule90-interior.md`. Within any {0,2} block, halved entries evolve under XOR = Rule 90 = Pascal mod 2.
- **Minima record (depth 1000):** [13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263].
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000), `step_law_captured.txt` / `step_law_independent.captured.txt` (depth 800, independent).
- **Library:** downloads halted. 92 sources, 3 checked. No more downloads without a stated gap.

### Threads

- `research/threads/regeneration.md` — updated: the question is now "can we bound the (2,4)-event rate from below?" rather than the open-ended "is there a k with block length 0?"
- `research/threads/rule90-regeneration.md` — Rule 90 depth prediction, now subordinated to the event-rate question (item 2 above).