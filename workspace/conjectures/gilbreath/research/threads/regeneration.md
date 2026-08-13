```thread
question: Why does a fresh {0,2} block always reappear before the current one is exhausted by erosion?
status: open — data gathered, mechanism not yet characterized
rests-on: |
  - Reduction proved (A_k(1) ∈ {0,2} ⇔ conjecture), checked to depth 599
  - Block profiles computed to depth 1000 (code/out/blocks_depth1000.json)
  - Erosion bound: b(k+1) ≥ b(k) - 1 (a block loses at most 1 per row)
  - Odlyzko's lemma (consumption): a block of length n protects exactly n+1 rows; constant is 1, not n/2. Proved by diagonal-subtriangle argument, verified exhaustively (n=1..11, 122820 adversarial pairs, zero violations) and on real prime rows to depth 600. This is consumption = 1 position per row, linear. Regeneration is the sole remaining obstruction.
  - 60 regeneration events (b diff ≥ 0) in 999 transitions; longest pure-erosion run = 838
  - Block lengths at k=1..40: 2,7,13,13,24,23,22,21,24,58,97,96,97,96,173,175,..., with local decreases (24→23→22→21, 97→96) — these are consumption outrunning regeneration locally. The question: is there a k with block length 0 before the next increase?
blocked-by: nothing yet — the mechanism of regeneration has not been stated
next: |
  1. Characterize the intruder (first non-{0,2} value past the block) — 59.6% are 4, all are 0 or 2 mod 4
  2. What must happen in the row below for a block to regrow? Study the k where b jumps.
  3. Stress-case: rows where b ≤ 10 — does regeneration still occur? (yes, b never stays at 2, but *why*?)
  4. State a precise claim about regeneration before trying to prove it.
  5. Run verify_constant.py and check_real.py against the sieve-to-400000 triangle as a final confirmation of the constant=1 lemma.
```

# Regeneration thread

## What we know

- **Consumption is proven**: a leading {0,2} block of length b_k in row k implies b_{k+1} ≥ b_k - 1. The block shrinks by at most 1 per row. This is the erosion bound — it's a theorem, not conjecture.

- **Regeneration is observed but not explained**: in 999 row transitions (depth 1000), 60 show b_{k+1} ≥ b_k (regeneration), and the largest single erosion run is 838 consecutive rows. Despite 838 rows of pure erosion, the block never drops to 0 — regeneration always intervenes.

- **The intruder**: the first entry after the leading {0,2} block. At depth 1000: min 4, max 14; 59.6% are exactly 4; all are 0 or 2 mod 4. The intruder is what the erosion-bound argument does not control — it's the first value that can "invade" the block as rows descend.

- **Short blocks are the stress case**: min b = 2 occurs at k=1 (because the prime row starts 2,3,5,7 so A_1 starts 1,2,2,4 — the first 4 is an intruder immediately). At k=2, b jumps to 7. The mechanism that turns b=2 into b=7 in one row is the simplest case of regeneration.

## Data available

- `code/out/witnesses.json`: depth 600, block profile for k=1..40, confirms b≥2 always
- `code/out/blocks_depth1000.json`: full b, s, intruder sequences to depth 1000
- `code/out/blocks_deep.captured.txt`: summary stats including regeneration events, erosion runs, s-run lengths
- `code/pattern/extract_witness.py`: extracts b, s, diffs from witnesses (captured for k=1..40)
- `code/out/commands.log`: full dump_sequences.py output with regeneration events and s-change positions

## What must be explained

For regeneration to fail, there must be a row k where b_k is small and the rows below fail to produce a fresh {0,2} block before b reaches 0. The conjecture asserts this never happens. To prove it, we need:

1. A theorem about *when* regeneration occurs — what property of the row below the block guarantees a fresh {0,2} stretch?
2. A bound on *how long* the block takes to regenerate — if regeneration takes at most R rows and b_k ≥ 2·R, then it's guaranteed. But R is not uniformly bounded: the jump sizes vary wildly (from 1 to 360698).
3. The key structural fact: what is the invariant of the absolute-difference operator that forces intruder values to eventually become 0 or 2?
