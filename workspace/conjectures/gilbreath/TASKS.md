# Tasks

## Phase: REGENERATION — the open problem

The reduction is checked (depth 599, full rows). Consumption (Odlyzko's lemma: a {0,2} block of length n protects ~n/2 rows) is understood. The open problem is **regeneration**: before the current {0,2} block is exhausted by erosion, a fresh long {0,2} block must appear from below. Every approach that proves consumption and stops there has proved nothing about the conjecture.

### Immediate next steps

- [ ] **Analyze regeneration events in `blocks_deep.py` output** (already captured to depth 1000 in `code/out/blocks_deep.captured.txt` and `code/out/blocks_depth1000.json`). The key data: 60 regeneration events in 999 row transitions, longest erosion run = 838 consecutive rows, max jump +360698 at k=146. Focus on the *mechanism*: what in the row below a shrinking block causes a fresh {0,2} stretch to emerge? The intruder values (first non-{0,2} entry past the block) are the key — they're mostly 4 (59.6%), always 0 mod 4 or 2 mod 4. What must happen to the intruder for a block to regrow?

- [ ] **Stress-case analysis**: short blocks (min b=2) are where regeneration must succeed with almost no buffer. Characterize what the row looks like when b=2 and what happens in the next few rows. The `extract_witness.py` data is captured for k=1..40; extend to the full depth-1000 data and isolate every k where b drops to 2..10.

- [ ] **State a precise claim about regeneration, naming which of consumption/regeneration it proves**, before attempting to prove it. Every claim must be checked against `witnesses.json` (min leading block=2) and the depth-1000 data. A claim not checked against the actual rows is `asserted`, never `checked`.

- [ ] **Formalize the difference operator in Lean 4** (as planned): define the operator, prove the (odd, even, even, ...) shape is preserved, reduce the conjecture to the {0,2} second-entry claim. Start the Lean file even while the regeneration analysis runs — they're independent.

- [ ] **Re-derive Odlyzko's block lemma with explicit constant** — how many rows does a block of length n protect, exactly? The lemma is cited but not re-derived here. Having the exact bound (not just "~n/2") determines how much regeneration is needed and how often.

### Background (already established)

- Reduction: `A_k(1) ∈ {0,2}` ⇔ conjecture. Checked to depth 599 on full rows (`code/out/check_reduction.captured.txt`).
- Block profiles: depth 1000 computed (`code/out/blocks_depth1000.json`), agrees with witnesses.json on k=1..40.
- Witnesses: `code/out/witnesses.json`, depth 600, sieve to 400000 (33860 primes), min leading block=2.
- Erosion bound: b(k+1) ≥ b(k) - 1 (proved by {0,2} closure — cannot drop by more than 1 per row).
- All tasks that don't explicitly engage regeneration are lower priority until the regeneration claim is explicit.
