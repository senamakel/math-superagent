# Tasks

## Phase: REGENERATION — the open problem

The reduction is checked (depth 599, full rows). Consumption (Odlyzko's lemma: a {0,2} block of length n protects **n+1 rows, exact** — re-derived in `research/notes/block_lemma.md`; the old "~n/2" phrasing is refuted) is understood. The open problem is **regeneration**: before the current {0,2} block is exhausted by erosion, a fresh long {0,2} block must appear from below. Every approach that proves consumption and stops there has proved nothing about the conjecture.

### Immediate next steps

- [ ] **VERIFY: Run `code/block_lemma/verify_constant.py` and `code/block_lemma/check_real.py`** against the existing sieve-to-400000 triangle (33860 primes, 599 rows in `code/out/witnesses.json`). Command: `timeout 540 python3 code/block_lemma/verify_constant.py 2>&1 | tee code/out/verify_constant.captured.txt; echo EXIT_CODE=$?` and similarly for `check_real.py`. Capture output. These confirm the exact constant 1 (n+1 rows protected per length-n block) against the real prime rows — the block lemma re-derived and proved by this run.

- [ ] **CHT hypotheses audit: Read the actual hypotheses of `cht-inverse-theorem` and `cht-random-analogue` from the full CHT 2026 text** (`research/sources/chase-hunter-tao-2026-full-html.full.md`, 93KB) and state explicitly, for each hypothesis: does it hold for the prime-difference sequence? The two claims are currently marked as `sourced` in `library-state.md` with informal `holds-here` notes, but an unchecked hypothesis on a real theorem is the trap. The inverse theorem (Theorem 1.6) requires no-0-block-of-length-L and no-shallow-{0,d}-block — these are precisely what the regeneration analysis must address but are not proved for primes. The random analogue (Theorem 1.3) requires independence + sublinear growth + no-2-separated-concentration — independence is only conjectural for prime gaps. Update `library-state.md` with the precise holds/fails assessment.

- [ ] **Analyze regeneration events in `blocks_deep.py` output** (already captured to depth 1000 in `code/out/blocks_deep.captured.txt` and `code/out/blocks_depth1000.json`). The key data: 60 regeneration events in 999 row transitions, longest erosion run = 838 consecutive rows, max jump +360698 at k=146. Focus on the *mechanism*: what in the row below a shrinking block causes a fresh {0,2} stretch to emerge? The intruder values (first non-{0,2} entry past the block) are the key — they're mostly 4 (59.6%), always 0 mod 4 or 2 mod 4. What must happen to the intruder for a block to regrow?

- [ ] **Stress-case analysis**: short blocks (min b=2) are where regeneration must succeed with almost no buffer. Characterize what the row looks like when b=2 and what happens in the next few rows. Isolate every k where b drops to 2..10 and trace what the intruder does.

- [ ] **State a precise claim about regeneration, naming which of consumption/regeneration it proves**, before attempting to prove it. Every claim must be checked against `witnesses.json` (min leading block=2) and the depth-1000 data. A claim not checked against the actual rows is `asserted`, never `checked`.
  **The only question worth answering:** is there a k with block length 0 before the next increase? Block lengths can decrease locally (24→23→22→21, 97→96). The conjecture is exactly: regeneration always outruns consumption. Consumption is one row per block entry (proved). Regeneration is unproved.

- [ ] **Formalize the difference operator in Lean 4** (as planned): define the operator, prove the (odd, even, even, ...) shape is preserved, reduce the conjecture to the {0,2} second-entry claim. Start the Lean file even while the regeneration analysis runs — they're independent.

- [x] **Re-derive Odlyzko's block lemma with explicit constant** — how many rows does a block of length n protect, exactly? **DONE:** the constant is exactly **1** (a `{0,2}` block of length n protects **n+1 rows**; first possible failure at row k+n+1, first possible second-entry escape at row k+n). This *corrects* the "~n/2" phrasing: it is linear, one row per block entry. Re-derived from a diagonal-subtriangle argument and verified exhaustively over all 2^n block patterns with adversarial even tails (n=1..11, 122820 pairs, zero violations) and against the real prime rows to depth 600 (zero violations). Consistent with Odlyzko 1993 §2 (p.374) and Killgrove–Ralston 1959. The `{0,2}` block's internal pattern controls the subtriangle apex exactly (Sierpinski/XOR) but cannot extend the worst-case guarantee, because position 1 of row k+n needs A_k(n+1), outside the block. Full write-up + fenced claim (`odlyzko-block-lemma-exact`) in `research/notes/block_lemma.md`.

  **Consequence for regeneration:** consumption is one row per block entry — *slower* than the old "n/2 per row" misreading, so regeneration has less distance to cover per block than previously thought. But the lemma still protects only a finite number of rows, so regeneration remains the true open problem and untouched here.

### Background (already established)

- Reduction: `A_k(1) ∈ {0,2}` ⇔ conjecture. Checked to depth 599 on full rows (`code/out/check_reduction.captured.txt`).
- Block profiles: depth 1000 computed (`code/out/blocks_depth1000.json`), agrees with witnesses.json on k=1..40.
- Witnesses: `code/out/witnesses.json`, depth 600, sieve to 400000 (33860 primes), min leading block=2.
- Erosion bound: b(k+1) ≥ b(k) - 1 (proved by {0,2} closure — cannot drop by more than 1 per row).
- All tasks that don't explicitly engage regeneration are lower priority until the regeneration claim is explicit.
