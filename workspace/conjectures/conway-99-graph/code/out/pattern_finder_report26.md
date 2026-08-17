# Pattern-finder report — round 26: fresh re-tooling; sequence line still closed

## What I did

Prior rounds (1–25) declared the sequence line closed. Before inheriting that
verdict I re-confirmed (a) that no capture artifact newer than report25 exists
on disk (only derived-ledger re-renders and lean caches postdate it — no new
sequence-bearing artifact), and (b) re-ran the exact sequence tools on the two
signature catalogue sequences.

## Fresh exact tooling (this round)

Sequence A — n3-cap `[0, 4158, 26730, 19320840, 121781611728]`:
- `analyze_sequence`: differences never constant → not a low-degree polynomial.
- `find_linear_recurrence(max_order=4)`: no constant-coefficient recurrence of
  order ≤ 4 fits all 5 terms.
- `oeis_lookup`: **no match** (new miss, distinct from the recorded vertex-count
  miss).

Sequence B — triangle counts `[6, 231, 891, 117096, 81842481]`:
- `analyze_sequence`: not linear/exponential/polynomial (differences non-constant).
- `find_linear_recurrence(max_order=4)`: no order ≤ 4 constant-coefficient fit.
- `oeis_lookup`: **no match** (new miss).

## Why this is the anticipated structure, not a finding

Both are the `u ∈ {1,3,4,10,31}` (u³/u⁴-degree) quartics over the
a = 2u+1 | 63 index set — the closed forms already established (n3-cap closed
form in `code/out/n3_cap_closed_form.captured.txt`; triangle count in the
family catalogue). A quartic-in-u evaluated at 5 index points is not a
low-order recurrence or a low-degree polynomial **in the index n**, which is
exactly what the tools report. The 5-term lists have no 6th extrapolating term
to falsify beyond validating the closed form, which is already done to k=994.

## The genuinely new (minor) negatives

The **n3-cap sequence** and the **triangle-count sequence** are themselves
uncatalogued in OEIS (they had not been looked up before; only the vertex-count
`[9,99,243,6273,494019]` miss was on record). This confirms no closed form for
either will come from OEIS. Not catalogued = no external structure to lean on;
the structure is exactly the problem's own divisor-63 quartic.

## Attack on the verdict (what would break it)

A regularity would exist if any family count *separated* 99 from its two
controls (9, 243). Every parameter-determined count verified across rounds
1–25 is a|63-governed and does not; the p-rank lists are 4 independent
measurements at distinct parameter points (2 outside the (1,2)-family), not an
indexed sequence (round 21 proved the order-2 "fit" is generic overfit). The
only 99-specific structural values remain the coclique bound 22 and the forced
n3 ≥ 3 (Makhnev conditional) — both single values with no definable
extrapolation, so no falsifying term exists.

## Verdict

NOTHING FURTHER from the sequence tools. Confirmed across 26 rounds with no gap
found. A 6th family term (k=place beyond 994) does not exist to compute; no
untooled sequence-bearing artifact is on disk. Genuinely new exploitable
structure, if any, lives in construction/search — the 99-vertex lift of the
super-simple 2-(22,4,2) design, and the k=14 local triangle geometry — not in
the sequence line.

## Files
- `research/notes/oeis-miss-n3cap-and-triangle-counts.md` — the two new OEIS misses.
- This report (`pattern_finder_report26.md`).
