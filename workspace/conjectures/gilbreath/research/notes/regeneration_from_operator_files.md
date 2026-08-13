# Regeneration of the leading {0,2} block, from the operator files

**Sources.** `/workspace/code/out/blocks_depth1000.json` (exact rows of the primes
to depth 1000, sieve to 20M, oracle-agrees with `witnesses.json` on k=1..40),
`/workspace/code/out/witnesses.json` (the run's witness oracle). Analyzed live by
`/workspace/code/pattern/extract_witness.py` and
`/workspace/code/pattern/regen_from_json.py`; outputs captured in
`out/extract_witness.captured.txt` and `out/blocks_deep_regen.captured.txt`.

**Notation.** Row `A_k` starts `(1, a_1, a_2, ..., a_b, c, ...)`, where `a_1..a_b`
is the maximal leading `{0,2}` block of length `b = b_k`, and `c = c_k` is the
*intruder* — the first entry past the block. The difference operator is
`A_{k+1}[j] = |A_k[j] − A_k[j+1]|`. The conjecture is `A_k(1) ∈ {0,2}` for all k
(equivalently `b_k ≥ 1` always). Regeneration means `b_{k+1} ≥ b_k` (diff `≥ 0`);
pure erosion means `b_{k+1} = b_k − 1`.

## The dichotomy is a theorem, not an observation

Positions inside the block: `|x−y|` with `x,y ∈ {0,2}` is `0` or `2`, so the first
`b−1` positions of the next row are always in `{0,2}`. Hence **`b_{k+1} ≥ b_k − 1`
always** (`{0,2}`-closure; diff is never below −1 — confirmed, min over 999
transitions is −1).

The next-row position `b` equals `|a_b − c|`. Since `a_b ∈ {0,2}`:

| intruder `c_k` | `A_{k+1}[b]` | effect on block |
|---|---|---|
| `4` | `{2,4}` | `2` if `a_b=2` (block holds/extends), `4` if `a_b=0` (shrinks) |
| `6` | `{4,6}` | `∉{0,2}` → block shrinks to `b−1` |
| `8` | `{6,8}` | same |
| `10,12,14,…` | `{c−2,c}` | all `≥4` → same |

So:

- **`c_k ≥ 6` (even, ≠4) forces `b_{k+1} = b_k − 1`** — exactly one row of
  erosion, unconditionally. **Proved.**
- **Regeneration onset (`b_{k+1} ≥ b_k`) requires `c_k = 4` and `a_b = 2`.**
  **Proved** (`c≥6` excluded by the table; `c=4` with `a_b=2` gives a value `2` at
  position `b`, so the block is at least as long).

## Verified against depth 1000 (all 999 transitions)

- Regeneration events (`diff ≥ 0`): **60 of 999**.
- **All 60 have `c_k = 4`.** (`c_k` value at regen onset is uniquely `4`.)
- Rows with `c_k = 4`: 96, of which **60 regenerate** (62.5%); the other 36 erode.
- Rows with `c_k ∉ {4}` and defined: 65, of which **0 regenerate** (all erode).
- Rows with `c_k = None` (block reaches end of row — whole row is `{0,2}`): 838,
  all erode by 1 per row (from k=163 to the end of the recorded depth).
- Intruder distribution (defined rows): `4`×96, `6`×29, `8`×16, `10`×6,
  `12`×8, `14`×6 — i.e. the only `c ≡ 0 (mod 4)` value seen is exactly `4`, and
  every value is `≡ 0 (mod 2)`. The `mod 4` distribution over 161 defined rows is
  `0 mod 4` ×120 (all of them `4`... but see below) and `2 mod 4` ×41.

  (Correction to the block_deep print: it reported `mod4 = {0:120, 2:41}`; broken
  down by value these are exactly `{4:96, 8:16, 12:8}` = 120 in `0 mod 4` and
  `{6:29, 10:6, 14:6}` = 41 in `2 mod 4`. There is no `c ≡ 0 (mod 4)` value other
  than `4` in the depth-1000 data.)

- Regeneration **does not cluster where `b` is small**: `b_k` at regen onset ranges
  over `{2,7,13,21,24,58,96,173,175,288,739,865,871,2176,2762,…,1094263}`; only 9 of
  60 regenerations start with `b_k < 100`. The smallest event is `k=1→2: b 2→7`
  (`diff +5`), the simplest regeneration.
- Big jumps are the typical regeneration: e.g. `k=143→144: +3`, `k=146→147:
  +360698`. Regenerations with `c_k=4` and `a_b=2` can extend the block arbitrarily
  far.

## The regeneration cycle, and the consumption trap (the finding that matters)

The dangerous failure named in GOAL.md is **consumption without regeneration**: an
argument that a `{0,2}` block protects `≈n/2` rows and quietly treats that as
persistence forever. The depth-1000 data shows exactly why that is the real risk:

- Regeneration is **rare** (60/999 ≈ 6%) and is **entirely mediated by the
  intruder being exactly `4`** — the single value for which the block can
  regrow. No `c ≥ 6` row ever regenerates; no `c = None` (fully-degenerate) row
  ever regenerates.
- Long erosion is genuinely long and final: starting at `k=163` the block has
  covered the whole row (`c = None`), and for the remaining **838 rows** the block
  shrinks by exactly 1 each row with no intru-decide to regenerate. That run is cut
  off at depth 1000 only by our depth, not by the mechanism.

So **regeneration in the prime rows is a `c_k = 4` phenomenon**, and the theorem
above proves the `c ≥ 6` direction unconditionally. What is *not* established is a
lower bound on the rate at which `c_k = 4` recurs — the prime rows give it 96/1000
here, but nothing proves recurrence, and a single `c = None` event is a terminal
pure-erosion descent.

## What this settles

- **Proved (exact arithmetic):** `c_k ≥ 6 ⇒ b_{k+1} = b_k − 1` unconditionally.
- **Proved:** regeneration requires `c_k = 4 ∧ a_b = 2`.
- **Verified numerically (999 transitions):** every regeneration has `c_k = 4`;
  no `c ≠ 4` row regenerates.
- **Unresolved:** a lower bound on the recurrence rate of `c_k = 4` (or of
  `c = None` being staved off), which is what regeneration-rate sufficiency would
  need.
