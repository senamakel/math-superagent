# Tasks

## Directive: STOP SEARCHING AND CONVERT

The library is sufficient. No more downloads until a specific gap is stated that a source could close. The current search (`exa_search 25→37`, frontier `309→345`) is to be halted — the checked count stayed at 3 while both indices moved, which means searching is consuming the run without producing new results.

## The data says two things, precisely and separately

### Fact (a): The block length never approaches 0 — and minima grow

Over the depth-1000 record (1.27M primes, `code/out/regeneration_analysis.captured.txt`), the record of **minimum block lengths** is:

`[13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263]`

- The **smallest block length ever seen after the first few rows is 13**, at k=3.
- Minima **grow rapidly**: 13 → 24 → 96 → 97 → 175 → 2762 → 5939 → ...
- **Dwell** at each minimum is 1 to 4 rows, then the block jumps up.
- The block length is not merely bounded away from 0 — it *increases* across the computed range.

This is strong numerical evidence that the conjecture holds, but it is not a proof.

### Fact (b): Regeneration is real but NOT monotone

- `97→96` occurs (k=13): the block *shrinks* to a new local minimum, then jumps to 97→173.
- `871→872` occurs (k=26): the block grows by 1.
- `21→24` occurs (k=8): the block grows by 3.
- Consumption and regeneration **alternate**. The block can shrink before growing.
- The longest pure-erosion run is 838 consecutive rows (k=162..999), but this is after the live regime (intruder becomes null, the block has consumed the entire row width).

### The honest open question, stated sharply

**Is there a k with block length 0?** Everything computed says no. Nothing proves it.

## Immediate next steps (in order)

- [ ] **1. Convert the regeneration analysis into a precise structural question.** Given the data above: what is happening in the rows where the block length hits a minimum and then jumps? The intruder is the first non-{0,2} value past the block. When b=13 (k=3), what is the row above it and what makes the next row's block length 13 again instead of 12? Characterise the rows at each minimum in the record.

- [ ] **2. State a new precise claim about regeneration.** The `iff` approach (single-row local property) is refuted. The data says regeneration is NOT local — it depends on structure further into the row. What *is* the right characterisation? The mod-4 linearization (entries are even, so `d_{k+1}(n) ≡ d_k(n) + d_k(n+1) (mod 4)`) is the cleanest algebraic handle — does it force intruder values to eventually become 0 or 2?

- [ ] **3. Attack the new claim before trusting it.** Run it against the real rows in `witnesses.json` and `blocks_depth1000.json`, especially the rows where the block is short (k=3, b=13; k=8, b=21; any k where b decreases). A claim that fails there is false.

- [ ] **4. Formalise the difference operator in Lean 4.** This is independent of the regeneration analysis. Define the operator, prove the (odd, even, even, ...) shape is preserved, reduce the conjecture to the {0,2} second-entry claim. Start the `.lean` file.

- [ ] **5. Refutation filed.** `code/out/check_regenerate_lemma.notes.md` records the refuted candidate lemma with exact k-values for both failure modes (IFF FAIL and REGEN FAIL). The oracle PASSED; the lemma FAILED. This is a dead end recorded — do not re-open.

## Background (already established, do not redo)

- Reduction: `A_k(1) ∈ {0,2}` ⇔ conjecture. Proved and checked to depth 599.
- Block lemma: constant = 1 (n+1 rows per length-n block). Proved, verified exhaustively, checked against real rows. `research/notes/block_lemma.md`.
- Oracle: `witnesses.json` (depth 600, 33860 primes) and `blocks_depth1000.json` (depth 1000, 1.27M primes).
- Mod-4 linearization: `d_{k+1}(n) ≡ d_k(n) + d_k(n+1) (mod 4)` for k≥1, n≥2.
- Library: sufficient. FRONTIER.md is at 309→345 with checked at 3 — searching has stopped producing new results. Stop.