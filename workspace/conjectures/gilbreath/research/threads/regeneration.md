```thread
question: Why does a fresh {0,2} block always reappear before the current one is exhausted by erosion?
status: open — but a precise single-row regeneration criterion is now ESTABLISHED to depth 1000
rests-on: |
  - Reduction proved (A_k(1) ∈ {0,2} ⇔ conjecture), checked to depth 599
  - Block profiles computed to depth 1000 (code/out/blocks_depth1000.json)
  - Erosion bound: b(k+1) ≥ b(k) - 1 (a block loses at most 1 per row)
  - Odlyzko's lemma (consumption): a block of length n protects exactly n+1 rows; constant is 1, not n/2. Proved by diagonal-subtriangle argument, verified exhaustively (n=1..11, 122820 adversarial pairs, zero violations) and on real prime rows to depth 600. Consumption = 1 position per row, linear. Regeneration is the sole remaining obstruction.
  - REGENERATION CRITERION (ESTABLISHED, exact, checked to depth 1000): with the block in 0-based cols 1..b_k, let c_k=A_k[b_k+1] (intruder) and e_k=A_k[b_k] (the true last {0,2} value of the block — NOT b_k-1, that is the earlier off-by-one error). Then q_k=A_{k+1}[b_k]=|e_k-c_k| lies in {0,2} IFF (e_k==2 and c_k==4), and b_{k+1}>=b_k IFF (e_k==2 and c_k==4). Zero failures over all 998 transitions; exactly 60 regeneration events (matching the long-standing count). The earlier note "regeneration is not a local property / lemma refuted" is WITHDRAWN: it was an off-by-one in the edge index. See code/regeneration/check_regenerate_lemma.py and code/out/check_regenerate_lemma.captured.txt.
blocked-by: nothing yet — criterion established, but why the criterion forces b never to hit 0 (globally) is not yet proved
next: |
  1. Promote the criterion: regeneration = (edge==2 AND intruder==4), i.e. block must end in 2 with a 4 just past it. This is a real single-row local fact, not an artifact.
  2. Link it to the mod-4 linearization d_{k+1}(n) ≡ d_k(n)+d_k(n+1) (mod 4): edge 2 + intruder 4 means columns b_k, b_k+1 sum to 2 (mod 4) giving q=2 at column b_k in the next row.
  3. Stress cases: at every k where b_k is small (local minima [13,24,96,97,...]), check whether the row below has (edge==2,intruder==4) available *before* erosion would drive b to 0. b never hits 0 in the computed range; explain via regeneration being cheap (needs only edge 2 and intruder 4 at the current boundary).
  4. The honest open question remains: is there a k with block length 0? No proof yet.
```

# Regeneration thread

## What we know

- **Consumption is proven**: a leading {0,2} block of length b_k in row k implies b_{k+1} ≥ b_k - 1. The block shrinks by at most 1 per row. Constant = 1 (n+1 rows per length-n block), re-derived and proved.

- **The regeneration criterion is ESTABLISHED (depth 1000, exact).** The block occupies 0-based columns `1..b_k`. Let the intruder be `c_k = A_k[b_k+1]` (the first value past the block) and the edge be `e_k = A_k[b_k]` (the **last** `{0,2}` value of the block — 0-based index `b_k`, not `b_k-1`). Then the value `q_k = A_{k+1}[b_k] = |e_k - c_k|` satisfies:
  - `q_k ∈ {0,2}`  ⟺  `(e_k == 2 and c_k == 4)`
  - `b_{k+1} ≥ b_k`  ⟺  `(e_k == 2 and c_k == 4)`
  - With **zero failures** over all 998 transitions; exactly **60** regeneration events, matching the long-standing count.
  - For rows whose whole leading length is `{0,2}` (no intruder, 838 of them), `b_{k+1} ≥ b_k` is always false, so the iff still holds.
  - Distributions: (e,c) pairs — (2,4):60, (0,4):36, (2,6):16, (0,6):13, (0,8):8, (2,8):8, (0,12):5, (0,14):4, (2,10):4, (2,12):3, (0,10):2, (2,14):2.

### Correction to prior record

The earlier thread entry "**candidate iff lemma REFUTED — regeneration is not a local property**" was based on an **off-by-one**: it used `e_k = A_k[b_k-1]` (and `q_k = A_{k+1}[b_k-1]`). Under that wrong index, `q_k == |e_k-c_k|` fails on 141/161 rows and the iff on 109. The correct definition `e_k = A_k[b_k]` follows from `A_{k+1}[j]=|A_k[j]-A_k[j+1]|`: the diff partner of the intruder `A_k[b_k+1]` is `A_k[b_k]`, not `A_k[b_k-1]`. With the correction, the iff holds exactly. **Withdrawn.**

This resolves the thread's open item "intruder==4 necessary but not sufficient (36 erosion rows also have intruder 4)": the missing condition is `e==2`. Among the 96 rows with intruder 4, the 60 with edge 2 regenerate and the 36 with edge 0 erode.

### Fact (a): Block length never approaches 0 — minima grow

Record of minima over depth 1000: `[13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263]`.

- The smallest block length after the first few rows is **13** (at k=3).
- Minima grow rapidly — the block length is not merely bounded away from 0, it *increases*.
- This is strong numerical evidence, not a proof.

### Fact (b): Regeneration is real but NOT monotone

`97→96` (k=13), `871→872` (k=26), `21→24` (k=8) all occur. Consumption and regeneration alternate.

## The honest open question

**Is there a k with block length 0?** Everything computed says no. Nothing proves it.

## What must be explained

To prove the conjecture one must show the regeneration criterion — the block ends in 2 with a 4 immediately past it — is available often enough that erosion never drives `b` to 0. The criterion is now known precisely; why it is always eventually available is not.

## Data available

- `code/out/witnesses.json`: depth 600, block profile for k=1..40
- `code/out/blocks_depth1000.json`: full b, s, intruder sequences to depth 1000
- `code/regeneration/check_regenerate_lemma.py` and `code/out/check_regenerate_lemma.captured.txt`: the established criterion, oracle-verified
- `code/out/regeneration_analysis.captured.txt`: earlier summary stats
- `code/out/check_regenerate_lemma.notes.md`: (superseded refutation note from the off-by-one run)
