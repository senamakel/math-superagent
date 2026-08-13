# Tasks

## Directive 7 (steer): Erosion settled. Step law exact. Spend this run on the event rate and nothing else.

The step law and recharge identity are exact (verified depth 800, zero failures). The conjecture is now: do (2,4)-events keep arriving fast enough that `Σ (j_i + 1)` never falls `k−1` behind?

The step law also holds on **random non-prime arrays** (3,521 rows, 610 events, zero failures — `code/out/step_law_and_recharge_verified.md`). This means the event mechanism is **combinatorial, not arithmetic** — the drain law, the edge-flip, and the local criterion `(2,4)` are facts about the absolute-difference operator itself. Primes enter only through event density. Therefore a lower bound on the event rate may be provable for the **general Gilbreath-like class** without any prime input at all. This is the route the directive identifies as most promising.

### Primary

- [ ] **1. Bound the (2,4)-event rate from below — combinatorial Route A first.**

  The random-array observation (step law holds on non-prime starts) means Route A is not a heuristic about primes — it targets a structural fact about the operator `|a−b|` on `{0,2}`-valued sequences with an even intruder. The question: **what is the density of k at which the intruder pair is exactly (2,4)? Is that rate bounded below, and by what?**

  **Route A — combinatorial.** Between two (2,4)-events, the block erodes at exactly 1 per row. The intruder drains at rate 2 when `x=2`, 0 when `x=0`. The edge flips 0↔2 under Rule 90 XOR dynamics. Prove a worst-case bound on consecutive rows with `(edge=0, intruder=4)` before the edge flips to 2. This is a combinatorial lemma about XOR evolution + drain law — no primes needed. If the maximum inter-event gap is G(b), then event rate ≥ 1/G, and the recharge inequality can be checked.

  **Route B — analytic (secondary).** Assume a prime-gap hypothesis and derive event density. Must state how it beats Eppstein.

  **Measure first.** Extract from `blocks_depth1000.json`:
  - Inter-event gap distribution
  - Jump-size distribution
  - Cumulative recharge vs consumption at each event
  - Worst-case inter-event gap and block length at gap start
  - Whether recharge surplus is growing or shrinking with k

  **Deliverable:** a theorem "under hypothesis H, the (2,4)-event rate is at least r, and r suffices to keep b_k ≥ 1 for all k." For the combinatorial route, hypothesis H is about the {0,2} interior + an even intruder — no prime input.

### Supporting (do not let these consume the run)

- [x] **2. Rule 90 depth prediction — REFUTED.** The regeneration-timing corollary (large jumps at depth 2^j) is refuted in every concrete form against the depth-1000 record. See `research/threads/rule90-regeneration.md` for the full refutation. The Rule 90 interior identification itself is proved and stands; the timing prediction is dead. Do not re-test.

- [x] **3. CHT Theorem 1.6 hypothesis check — DONE, holds-here = no.** R_0 = 4.2e8 ≫ 1000; the theorem does not bite at reachable depths. `code/out/cht_hyp_check.captured.txt`.

- [ ] **4. Lean 4 formalisation.** Define the difference operator, prove shape preservation, reduce to {0,2} second-entry claim. Machine-checked lemma. Report `#print axioms` and every `sorry`. Independent of items 1–3, run in parallel.

- [ ] **5. Ledger hygiene (directive asks explicitly).** The ledger counts moved asserted 36→38, checked 3→5, proved 17→15 — this reads as two deliberate demotions (proved→asserted). Librarian: name which claims were demoted and say in the notes whether it was deliberate, or correct the statuses. Do not let a silent demotion stand.

- [ ] **6. Record the random-array step law as its own claim.** The step law holding on random non-prime arrays (3,521 rows, 610 events, zero failures) is load-bearing for Route A. It is currently only a sentence inside `step-law-and-recharge-identity`'s bearing. Librarian: split it into a distinct claim (e.g. `step-law-combinatorial-general-class`) with its own hypotheses (non-prime 2-then-odds starts) and evidence (checked). This is what the "general Gilbreath-like class, no prime input" theorem will rest on.

### Background (established — do not re-derive or re-verify)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved.
- **Block lemma:** constant = 1. Proved. `research/notes/block_lemma.md`.
- **Step law + recharge identity:** exact, verified independently depth 800, zero failures. `code/out/step_law_and_recharge_verified.md`. Also holds on random non-prime arrays (3,521 rows, 610 events, zero failures) — these are combinatorial facts about the operator.
- **Regeneration criterion:** b_{k+1} ≥ b_k ⟺ (A_k[b_k]==2 AND A_k[b_k+1]==4). Depth 1000, zero failures, 60/60.
- **Drain law:** y_{k+1} = y_k − 2·[x_k = 2]. Verified 101/101.
- **Rule 90 interior (PROVED):** `research/notes/rule90-interior.md`.
- **Minima record (depth 1000):** [13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263].
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000).
- **Library:** downloads halted. 92 sources, 3 checked. No more downloads.

### Threads

- `research/threads/regeneration.md` — the live question: bound the (2,4)-event rate from below. Combinatorial Route A is the priority (random-array evidence). Route B (analytic) is secondary.
- `research/threads/rule90-regeneration.md` — **REFUTED.** The depth-d=2^j timing prediction is dead. The Rule 90 interior identification is proved and unaffected; it feeds Route A as the edge-flip mechanism.
