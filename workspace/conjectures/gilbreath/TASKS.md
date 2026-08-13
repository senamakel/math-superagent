# Tasks

## Directive: Split Rule 90 from the absorption wrapper, then test the depth prediction

The `rule90-identification-real-absorption-refuted` claim contains a **proved core**
and a **refuted wrapper**. The proved core is: the {0,2} interior evolves under
the halved operator as XOR = Rule 90 = Pascal mod 2 (block-lemma apex, verified
exhaustively for n ≤ 13). The refuted wrapper was the uniform boundary-absorption
mechanism. Split them now — the Rule 90 identification deserves its own claim,
separate from the dead absorption approach. Then use it.

Rule 90 from a single 1 gives the Sierpinski triangle — all-1 rows at depths
d = 2^j. If the interior really is Rule 90, the Sierpinski kernel is all-1 at
those depths, meaning the halved row is the XOR of the whole width-d window. If
that XOR is 1 for a stretch, the original row is all-2 across that stretch — a
clean regenerated block. This predicts regeneration at specific depths.

Test: the minima were [13,24,96,97,175,2762,5939,31525,...] — check whether the
jumps sit where Rule 90 says they should. Sharp, falsifiable, cheap. Thread at
`research/threads/rule90-regeneration.md`.

**No more downloads.** The library is sufficient. FRONTIER.md is not to be
consumed further until a specific gap is stated.

## Immediate next steps (in order)

- [ ] **1. Split the Rule 90 claim.** Create a clean proved claim `rule90-interior-xor` in its own note under `research/notes/`, stating: within any {0,2} block, the halved entries evolve under XOR (= Rule 90 = Pascal mod 2), giving the Sierpinski structure of the subtriangle. Proved by block-lemma diagonal argument; verified exhaustively n ≤ 13. Anchor it to `research/notes/block_lemma.md`. The absorption wrapper stays refuted in `research/approaches/rule90-absorbing-boundary.md`. Then amend CONTEXT.md Established to carry the proved Rule 90 claim.

- [ ] **2. Derive the depth prediction.** From the XOR evolution formula: at depth d = 2^j, binom(2^j, m) ≡ 1 (mod 2) for all m, so (A_{K+d}(p+1)/2) = XOR of width-(d+1) initial window. If XOR = 1 for a stretch, halved row is all-1 → original row all-2 → regenerated block. State the prediction precisely: regeneration events (large b_{k+1} > b_k) and minima should occur at depths that are powers of 2 relative to the start of the current block regime.

- [ ] **3. Test against `blocks_depth1000.json`.** Write a program that:
  - Finds every regeneration event (b_{k+1} > b_k) and every local minimum
  - Computes the depth from the start of the current block regime (the row where the block was last at a minimum or where it was "born")
  - Checks whether those depths are powers of 2 (or 2^j ± 1)
  - Reports match/mismatch with exact k values
  Parallelise over hypothesis variants (`code/lib/parallel.py`, 28 CPUs).

- [ ] **4. Report the result.** If the prediction holds: a structural mechanism for regeneration, worth promoting to a proved partial result. If it fails: state the exact k and depth where it fails, and by how much — a refuted prediction from a proved structure is also a result.

- [ ] **5. Formalise the difference operator in Lean 4.** Define the operator, prove the (odd, even, even, ...) shape is preserved, reduce to the {0,2} second-entry claim. Report `#print axioms` and every `sorry`. This is independent of the regeneration analysis and can run in parallel.

## Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved and checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved, verified exhaustively, checked against real rows. `research/notes/block_lemma.md`. The subtriangle apex is the Sierpinski/XOR of the block's bit pattern.
- **Rule 90 interior (proved core, needs splitting from refuted wrapper):** within any {0,2} block, halved entries evolve under XOR = Rule 90. Proved by block-lemma diagonal argument; currently buried inside `rule90-identification-real-absorption-refuted` in `research/approaches/rule90-absorbing-boundary.md`.
- **Regeneration criterion:** regeneration at row k ⇔ (A_k[b_k] == 2 AND A_k[b_k+1] == 4). Established to depth 1000, zero failures, 60/60 events match. `code/out/check_regenerate_lemma.captured.txt`.
- **Minima record (depth 1000):** block lengths at local minima = [13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263].
- **Oracle:** `witnesses.json` (depth 600) and `blocks_depth1000.json` (depth 1000).
- **Mod-4 linearization:** d_{k+1}(n) ≡ d_k(n) + d_k(n+1) (mod 4) for k≥1, n≥2.
- **Candidate iff lemma — refuted and withdrawn.** The off-by-one version was refuted; the corrected version (using A_k[b_k] as edge) holds exactly. See `research/threads/regeneration.md` for the withdrawn note.
- **Library:** sufficient. No more downloads.
- **Refutation handling:** `code/out/check_regenerate_lemma.notes.md` cleanly records the refuted candidate with exact k-values. Oracle PASSED, lemma FAILED. Keep it.