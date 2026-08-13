# Rule 90 regeneration — structural prediction from the interior dynamics

```thread
question: Does the Rule 90 (Sierpinski / Pascal mod 2) structure of the {0,2}
          interior force block-length regeneration at specific depths, and do
          those depths match the computed minima record?
status: REFUTED (pattern_finder, depth-1000 record) — the Rule 90 interior
        identification is proved (block-lemma apex) and stands; the
        regeneration-timing corollary (large jumps at depth 2^j) is refuted in
        every concrete form below. See "Refutation of the depth prediction"
        at the foot of this thread.
rests-on: |
  - Block lemma (proved): the {0,2} interior evolves under the halved operator
    as XOR = Rule 90 = Pascal mod 2. The apex A_{k+n-1}(1) = 2 · XOR_j
    binom(n-1, j) mod 2 · (b_{j+1}/2). Anchor: research/notes/block_lemma.md.
  - Sierpinski fact (classical): Rule 90 from a single 1 at position 0
    produces all-1 rows (mod 2) exactly at depths d = 2^j - 1 (j ≥ 0), i.e.
    rows 0, 1, 3, 7, 15, 31, ... Within the Gilbreath block, a depth-d
    descent reaches row k+d; the halved entries at that depth are the d-step
    XOR evolution of the initial bit pattern.
  - The initial bit pattern is (A_1(2)/2, A_1(3)/2, ...), i.e. the halved
    gaps between consecutive primes: not a single 1, but an arbitrary
    binary string. At depths d = 2^j - 1 where the Sierpinski kernel is all-1,
    the halved entries become the XOR-sum of the whole width-2^j initial
    window — if that sum is 1, the halved value is 1 (= original 2), giving a
    stretch of all-2 entries which regenerates the block.
  - Minima record (depth 1000): block lengths at local minima =
    [13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263].
    These are the *values* of b_k at minima, not the row indices k.
blocked-by: nothing yet — the prediction is cheap to test
next: |
  1. ~~**Split the claim.**~~ DONE — `rule90-interior-xor` is its own proved
     claim in `research/notes/rule90-interior.md` (Directive 4). The absorption
     wrapper stays dead in `research/approaches/rule90-absorbing-boundary.md`.

  2. **Derive the depth prediction.** From the XOR structure:
     - In a {0,2} block of length n starting at row K, the halved entries
       evolve under Rule 90. At depth d (row K+d), entry at position p is
       XOR_{j=0}^{d} binom(d, j) mod 2 · (A_K(p+j)/2).
     - At d = 2^j, binom(2^j, m) ≡ 1 (mod 2) for all 0 ≤ m ≤ 2^j, so the
       halved value at position p (for p+d ≤ n) is the XOR of the width-(d+1)
       initial window starting at p. If that XOR is 1 for a long stretch, the
       halved row is all-1 (= original all-2) across that stretch — a clean
       {0,2} block that has regenerated.
     - The prediction: block-length regeneration (large jumps) should occur
       at or near depths that are powers of 2 relative to the start of a
       block, or whose block-length differences are powers of 2.

  3. **Test against the record.** Compute the row indices k where block-length
     minima occur, and the row indices where regeneration events (b_{k+1} > b_k)
     happen. Check whether:
     - The *differences* between consecutive minima row indices are powers of 2.
     - Regeneration jumps happen at depths that are 2^j from the start of the
       preceding block.
     - The block-length *values* at minima bear a power-of-2 relationship to
       each other or to the row index.
     This is cheap — the data is already in code/out/blocks_depth1000.json.

  4. **State the result exactly.** If the prediction holds, it is a structural
     mechanism for regeneration (not merely empirical) and becomes a proved
     partial result. If it fails, say at which k and by how much — a refuted
     prediction is also a result.

  5. **Promote the Rule 90 claim** into CONTEXT.md's Established section as
     proved, with the block-lemma anchor. The identification is independent of
     the regeneration question and stands on its own.
```

# Rule 90 regeneration thread

## The proved core: Rule 90 governs the {0,2} interior

From the block lemma (`research/notes/block_lemma.md`): within any leading
{0,2} block, entries are in {0,2}. Halving them gives {0,1}. The absolute
difference |a-b| for a,b ∈ {0,2} satisfies |a-b|/2 = (a/2) XOR (b/2). So the
halved block interior evolves under XOR — Wolfram Rule 90, the linear
elementary cellular automaton whose evolution is Pascal's triangle modulo 2.

After d descent steps inside a block of length n starting at row K, the halved
entry at position p (0 ≤ p ≤ n-d-1) is:

```
(A_{K+d}(p+1) / 2) = XOR_{j=0}^{d} [ binom(d, j) mod 2 ] · (A_K(p+1+j) / 2)
```

This is proved by the diagonal-subtriangle argument and verified exhaustively
over all 2^n block patterns for n ≤ 13.

## Why it matters for regeneration

At depth d = 2^j, binom(2^j, m) ≡ 1 (mod 2) for all 0 ≤ m ≤ 2^j (Lucas's
theorem). So the halved value at position p is the XOR of the width-(2^j+1)
initial window. If that XOR is 1 for a stretch of positions, the halved row
has a stretch of 1s — i.e. the original row has a stretch of 2s — which is a
clean {0,2} block that has regenerated.

In the classical Sierpinski triangle from a single 1, rows d = 2^j - 1 are
all-1 across the light cone. In the Gilbreath block the initial bit pattern is
arbitrary (the halved prime gaps), but at these depths the kernel is all-1, so
every position is the XOR of the whole window. Long runs of 1 in the halved
row mean long runs of 2 in the original — regeneration of the block.

## The prediction to test

Regeneration events (large jumps in block length) should occur at depths that
are powers of 2 relative to the start of the current block regime. Specifically:

1. The row-index *differences* between consecutive block-length minima should
   be, or be close to, powers of 2.
2. Large regeneration jumps should happen at depths d = 2^j - 1 (or 2^j)
   measured from the row where the block regime began.
3. If the block-length *values* at minima are examined, their relationships
   should reflect the power-of-2 structure of the underlying Sierpinski kernel.

## Data available

- `code/out/blocks_depth1000.json` — full block profile, intruder values,
  erosion/regen flags for k=1..1000
- `code/out/regeneration_analysis.captured.txt` — summary stats including the
  minima record
- `research/notes/regeneration_data.md` — detailed regeneration statistics and
  structural facts

## What counts as a result

- **If the prediction holds:** a structural (not empirical) mechanism for
  regeneration, formable as a proved partial result: "the Rule 90 interior
  dynamics force block-length regeneration at depths that are powers of 2."
- **If it fails:** state the exact k and depth where it fails and by how much.
  A sharp, falsifiable prediction that is refuted by the data is a result.

## Refutation of the depth prediction (pattern_finder, this record)

Tested every concrete form of "regeneration at powers of 2" against
`code/out/blocks_depth1000.json` (programs `code/pattern/rule90_depth_test.py`
and `rule90_depth_test2.py`). All forms are **refuted**:

- **(A) Gaps between consecutive regen rows:** 13 of 42 are non-powers of 2
  (non-powers: 3,3,12,5,7,6,5,3,14,13,5,3,13).
- **(B2) Next-regen offset after each big-jump row (jump ≥ 1000):** rows
  [34,56,64,68,94,96,110,112,126,130,134,146,161]; only 9/13 have the next
  regen row at a power-of-2-ish offset (offset ∈ 2^j or 2^j−1) — against a
  null rate 34/42 = 0.81 for **all** regen rows. No separation.
- **(C) Big-jump rows at absolute k:** none is a power of 2
  (34→32, 56→64, 94→64, 110→128, ...), i.e. big regeneration does not happen
  *at* a power-of-2 row.
- **(D) Strict local-minima row indices:** [7,11,13,21,25,33,37,55,67,71,85,90,
  93,95,109,124,127,133,137,145,158] — **none** is a power of 2.
- **(E) Next-regen offset histogram:** {1:10,2:11,3:4,4:7,5:3,6:1,7:1,8:1,
  12:1,13:2,14:1} — offsets 12,13,14 break the power-of-2 story and there are
  more 3s and 5s than 8s.

So the **regeneration-timing corollary** of the Rule 90 interior structure is
refuted by the depth-1000 record. This does **not** touch the interior-XOR
identification itself (proved, `rule90-interior-xor`), which concerns the
*values* inside the block, not *when* the boundary regenerates. The depth
prediction should not be re-asserted. The open regeneration content is
unchanged: why the boundary pair (x,y) = (2,4) recurs — see
`research/threads/regeneration.md`.
