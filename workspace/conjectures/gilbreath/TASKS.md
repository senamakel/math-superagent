# Tasks

## Directive 20 (steer): Collapse duplicate Lean claims, explain downgrade

### Done this cycle

- [x] **Duplicate Lean claims collapsed.** `code/lean/gilbreath_reduction.lean` defines
  `Step s i = Nat.dist (s i) (s (i+1))` — verbatim `Nat.dist`, not `|...|`.
  `gilbreath-second-entry-equivalence` (in `research/notes/library-state.md`) quotes
  that definition exactly and is `proved`. `lean-reduction-machine-checked` (in
  `code/out/lean_gilbreath_reduction.notes.md`) paraphrased the operator as
  `|s i - s (i+1)|`, which in ℕ is ambiguous (could be read as truncated `Nat.sub`
  rather than `Nat.dist`). That claim is now **superseded** with a retirement note
  pointing to the verbatim claim. `code/grounding/check_absdiff_vs_forwarddiff.py`
  independently confirms the absolute-difference operator is the one the conjecture
  is about: iterated abs diff ≠ |signed forward diff| (counterexample `[5,1,6]` at k=2),
  so the operator is genuinely `|a − b|` (= `Nat.dist`), not a signed-forward
  confusable.

- [x] **Proved count 14→13 explained.** `lean-reduction-machine-checked` was `proved`
  in an earlier ledger revision (the note claimed `status: checked` but a prior
  regeneration had it as `proved`). The ambiguity in the `|...|` notation —
  `Nat.dist` vs. `Nat.sub` — is what dropped it: a claim that misstates the
  definition cannot be `proved`. The verbatim `gilbreath-second-entry-equivalence`
  is the live `proved` claim. No mathematics was lost; the paraphrase was wrong.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal:** `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`; `b_k = 2 + Σ(j_i+1) − (k−1)`. Zero failures on all 1,154 sweep sequences AND primes. `code/out/step_law_and_recharge_verified.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified 101/101; combinatorial.
- **Lean 4 formalisation — COMPLETE.** Nine theorems, zero sorry, axiom footprint [propext, Classical.choice, Quot.sound]; IFF reformulation. Live claim: `gilbreath-second-entry-equivalence` (verbatim `Nat.dist`, proved). `lean-reduction-machine-checked` superseded (ambiguous `|...|` paraphrase). Directive 17.
- **Conditional-rate experiment — DONE.** p = 0.68 over 8 families (consecutive, f2-rand24, rand24 are immortal corner-class — 0 eligible rows), no family dependence post-startup. Route A supported. λ̂ = 0.585288, D=400 corrected run (commit ae69d093). Directive 19.
- **D=40 smoke numbers — DISCARDED** (Directive 19, predate sign fix). Do not cite.
- **CHT Theorem 1.6 hypothesis check — DONE.** M=7, L=2, R_0=419,430,400 ≫ 1000; `holds-here: no`.
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000).
- **Library:** 92 sources on disk, downloads halted.

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

### Threads

- `research/threads/regeneration.md` — LIVE. Route A SUPPORTED (Directive 19): the conditional-rate experiment confirms family-independent post-startup event rate. The gap is: λ̂ = 0.585 is measured, not bounded below for all k. Next step is a lower bound on the rate, not another estimate.
- `research/threads/rule90-regeneration.md` — CLOSED.