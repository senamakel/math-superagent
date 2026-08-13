# Tasks

## Directive 8 (steer): CHT holds-here done. Rule 90 needs null. Back to event rate.

### Immediate (in order — do not parallelise these away from each other)

- [x] **1. Compute the null distribution for the rule90 relative-depth result — DONE.** Program `code/rule90_test/null_rule90_depth.py`, capture `code/out/null_rule90_depth.captured.txt`, JSON `code/out/rule90_depth_null.json` (26 workers, 10,000 permutations). **The permutation null is degenerate**: the hit predicate tests depth *values* only, so all 10,000 shuffles of the 27 regime lengths gave the same count — a permutation test has zero power for a value-only predicate. **The honest null is the exact binomial** X ~ Binomial(27, 9/16) (uniform over the observed [0,15], hit values {1,2,3,4,5,7,8,9,15}, program's depth>0 guard): mean 15.19, sd 2.58, z = 2.25, **P(X ≥ 21) = 0.017299** — significant at 5%, not at 1%. Three independent routes agree to 8 digits (exact Fraction tail, scipy.stats.binom.sf, direct float sum). **The signal lives entirely in the tol=1 tolerance**: at tol=0 (exact powers {1,2,4,8,16}) only 10/27 hit, p = 0.113 (not significant); conditioning on the observed concentrated range [2,9] post hoc gives p = 0.68. Verdict: the 21/27 relative-depth result is a mild, tolerance-dependent concentration, not a structural regeneration mechanism.

- [ ] **2. Bound the (2,4)-event rate from below — combinatorial Route A.**

  The step law holds on random non-prime arrays (3,521 rows, 610 events, zero failures), so the event mechanism (drain law, edge-flip, local criterion) is combinatorial — facts about the operator itself. The conjecture is: do (2,4)-events keep arriving fast enough that `Σ (j_i + 1)` never falls `k−1` behind?

  **Route A — combinatorial.** Between two (2,4)-events, the block erodes at exactly 1 per row. The intruder drains at rate 2 when x=2, 0 when x=0. The edge flips 0↔2 under Rule 90 XOR dynamics. Prove a worst-case bound on consecutive rows with `(edge=0, intruder=4)` before the edge flips to 2. If the maximum inter-event gap is G, then event rate ≥ 1/G, and the recharge inequality is checkable.

  **Route B — analytic (secondary).** Assume a prime-gap hypothesis and derive event density. Must state how it beats Eppstein.

  **Deliverable:** a theorem "under hypothesis H, the (2,4)-event rate is at least r, and r suffices to keep b_k ≥ 1 for all k." For Route A, H is about the {0,2} interior + an even intruder — no prime input.

### Supporting (do not let these consume the run)

- [x] **3. CHT Theorem 1.6 hypothesis check — DONE, holds-here = no.** M=7, L=2, R_0=419,430,400 ≫ 1000. Set on BOTH copies (`research/notes/library-state.md`, `research/summaries/chase-hunter-tao-2026-full-html.md`). `code/out/cht_hyp_check.captured.txt`.

- [x] **4. Rule 90 depth prediction — CLOSED (null computed, item 1).** The absolute-depth and jump-timing forms are refuted. The relative-depth measure (depth from regime start) gives 21/27 within tol=1 of a power of 2, which against the exact binomial Binomial(27, 9/16) is p = 0.0173 (significant at 5%, not 1%) but is dead at tol=0 (p = 0.113) and erased by conditioning on the observed [2,9] range (p = 0.68). Verdict: mild, tolerance-dependent concentration, not a structural mechanism. Claim `rule90-relative-depth-null` recorded; thread `research/threads/rule90-regeneration.md` status CLOSED. Do not re-assert the timing prediction.

- [ ] **5. Lean 4 formalisation.** Define the difference operator, prove shape preservation, reduce to {0,2} second-entry claim. Report `#print axioms` and every `sorry`. Independent of items 1–2.

- [ ] **6. Ledger hygiene.** The ledger counts moved asserted 36→38, checked 3→5, proved 17→15. Name which claims were demoted and say whether deliberate. Do not let a silent demotion stand.

- [ ] **7. Record the random-array step law as its own claim.** Split the general-class finding (3,521 rows, 610 events, zero failures) into a distinct claim `step-law-combinatorial-general-class` with its own hypotheses and the checked evidence. This is what Route A's theorem will rest on.

### Background (established — do not re-derive or re-verify)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved.
- **Block lemma:** constant = 1. Proved. `research/notes/block_lemma.md`.
- **Step law + recharge identity:** exact, verified independently depth 800, zero failures. `code/out/step_law_and_recharge_verified.md`. Also holds on random non-prime arrays (3,521 rows, 610 events, zero failures) — combinatorial facts about the operator.
- **Regeneration criterion:** b_{k+1} ≥ b_k ⟺ (A_k[b_k]==2 AND A_k[b_k+1]==4). Depth 1000, zero failures, 60/60.
- **Drain law:** y_{k+1} = y_k − 2·[x_k = 2]. Verified.
- **Rule 90 interior (PROVED):** `research/notes/rule90-interior.md`.
- **Minima record (depth 1000):** [13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263].
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000).
- **Library:** downloads halted. 92 sources, 3 checked. No more downloads.
- **CHT Theorem 1.6:** holds-here = no. R_0 = 419,430,400 ≫ 1000. The theorem does not bite at reachable depths. Both claim copies updated.

### Threads

- `research/threads/regeneration.md` — bound the (2,4)-event rate from below. Combinatorial Route A first.
- `research/threads/rule90-regeneration.md` — **OPEN (pending null test).** Relative-depth measure 21/27 near power of 2 at tol=1; null to be computed (item 1). The absolute and jump-timing forms are refuted; the Rule 90 interior identification is proved and unaffected.