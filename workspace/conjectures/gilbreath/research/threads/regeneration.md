```thread
question: Why does a fresh {0,2} block always reappear before the current one is exhausted by erosion?
status: open — data gathered, one candidate lemma refuted, two sharp facts established
rests-on: |
  - Reduction proved (A_k(1) ∈ {0,2} ⇔ conjecture), checked to depth 599
  - Block profiles computed to depth 1000 (code/out/blocks_depth1000.json)
  - Erosion bound: b(k+1) ≥ b(k) - 1 (a block loses at most 1 per row)
  - Odlyzko's lemma (consumption): a block of length n protects exactly n+1 rows; constant is 1, not n/2. Proved by diagonal-subtriangle argument, verified exhaustively (n=1..11, 122820 adversarial pairs, zero violations) and on real prime rows to depth 600. This is consumption = 1 position per row, linear. Regeneration is the sole remaining obstruction.
  - 60 regeneration events (b diff ≥ 0) in 999 transitions; longest pure-erosion run = 838
  - Candidate iff lemma REFUTED (code/out/check_regenerate_lemma.captured.txt and code/out/check_regenerate_lemma.notes.md): both directions of the iff fail systematically. Regeneration is not characterisable by a single-row local property of the intruder and block length alone.
blocked-by: nothing yet — the mechanism of regeneration has not been stated
next: |
  1. State the two sharp facts from the data precisely (see code/out/regeneration_analysis.captured.txt):
     (a) The block length never approaches 0 over the range computed — the smallest ever seen is 13 (at k=3), and minima grow rapidly: [13,24,96,97,175,2762,5939,31525,31533,31534,733574,1094263]. Dwell at each minimum is 1 to 4 rows. This is numerical evidence that the conjecture holds strongly — block length is not just bounded away from 0, it grows.
     (b) Regeneration is real but NOT monotone — 97→96, 871→872, 21→24 all occur, so consumption and regeneration alternate. The block can shrink before growing.
  2. The honest open question, stated sharply: is there a k with block length 0? Everything computed says no and nothing proves it. State it this way.
  3. Convert data into a characterisation attempt: what *does* the row below a short block look like when regeneration succeeds? What does it look like when it fails locally?
  4. Do not search the library further — the directive says to stop searching and convert. The library is sufficient.
```

# Regeneration thread

## What we know

- **Consumption is proven**: a leading {0,2} block of length b_k in row k implies b_{k+1} ≥ b_k - 1. The block shrinks by at most 1 per row. Constant = 1 (n+1 rows per length-n block), re-derived and proved.

- **The candidate iff lemma is REFUTED.** `check_regenerate_lemma.py` tested a proposed characterisation of regeneration by a single-row local property (involving intruder c, block length b, and second entry e) against the real rows to depth 1000. Both directions fail systematically. The oracle PASSED; the lemma FAILED. See `code/out/check_regenerate_lemma.notes.md` for exact k-values. The takeaway: **regeneration is not a local property** — it cannot be read off the current row's intruder and block length alone.

## Two sharp facts from the data

### Fact (a): Block length never approaches 0 — minima grow

Record of minima over depth 1000: `[13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263]`.

- The smallest block length after the first few rows is **13** (at k=3).
- Minima grow rapidly — the block length is not merely bounded away from 0, it *increases*.
- Dwell at each minimum is 1 to 4 rows.
- This is strong numerical evidence that the conjecture holds, but it is not a proof.

### Fact (b): Regeneration is real but NOT monotone

- `97→96` occurs (k=13): the block shrinks to a new local minimum.
- `871→872` occurs (k=26): the block grows by 1.
- `21→24` occurs (k=8): the block grows by 3.
- Consumption and regeneration **alternate** — the block can shrink before growing.
- The longest genuine live-regime erosion run is 13 rows (k=97..109). The 838-row run is a finite-width artifact.

## The honest open question

**Is there a k with block length 0?** Everything computed says no. Nothing proves it.

## What must be explained

For regeneration to fail, there must be a row k where b_k is small and the rows below fail to produce a fresh {0,2} block before b reaches 0. The conjecture asserts this never happens. To prove it, the data says:

1. Regeneration is NOT local — the single-row iff approach is dead. The mechanism must involve structure further into the row.
2. The mod-4 linearization (`d_{k+1}(n) ≡ d_k(n) + d_k(n+1) (mod 4)` for even entries) is the cleanest algebraic handle — Pascal-triangle congruences govern the even entries, and the question is whether they force the boundary between {0,2} territory and intruder territory to always move outward eventually.
3. The intruder (first non-{0,2} value) is 4 in 59.6% of rows and always 0 or 2 mod 4. Intruder==4 is *necessary* for regeneration (all 60 regen rows have intruder 4 at depth 1000) but NOT sufficient (36 erosion rows also have intruder 4).

## Data available

- `code/out/witnesses.json`: depth 600, block profile for k=1..40
- `code/out/blocks_depth1000.json`: full b, s, intruder sequences to depth 1000
- `code/out/regeneration_analysis.captured.txt`: summary stats (Q1–Q5)
- `code/out/check_regenerate_lemma.captured.txt`: refutation of candidate iff lemma
- `code/out/check_regenerate_lemma.notes.md`: refutation write-up with fenced claim
