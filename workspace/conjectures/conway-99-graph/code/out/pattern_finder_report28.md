# Pattern-finder report — round 28: sequence line re-confirmed closed; Paley-config count re-tooled exactly

## What I did

Swept the workspace for anything newer than the last report (`pattern_finder_report27.md`,
01:22) that could carry an untooled integer sequence, and re-ran the exact sequence
tools on the one sequence that postdates round 26.

**Newer-file audit (mechanical, not assumed):**
- `find -newer pattern_finder_report27.md` (excluding git internals and
  derived-ledger re-renders) returns exactly **two files**: the prose approach
  documents `research/approaches/star-complement-reconstruction.md` and
  `orderly-canonical-augmentation.md`. Neither contains a computed list of terms
  (grep for bracketed integer lists and "sequence" confirms: only parameter
  values like (99,14,1,2), no term sequences).
- Every `.py` newer than `pattern_finder_report26.md` has a sibling
  `.captured.txt` (the scripted check found zero un-captured programs — the
  round-27 trap of a written-but-never-run `paley9_pattern_check.py` is the only
  such case on record, and it was executed in round 27).
- Ledger `attempts` has one entry newer than round 27 (`c3-spectrum-exact-verify`),
  status `rejected`; it records no computed integer list, only the closed-form C3
  spectrum already tooled in rounds 19/22/23.

**Result: the only integer sequence on disk newer than round 26 is the Paley(9)
per-vertex configuration count from round 27's exact BvLS verification.**

## The sequence, re-tooled exactly by me this round

Per-vertex config count over the five integrality-feasible members
(k = u²+u+2, u ∈ {1,3,4,10,31}):

    k = 4  14    22     112     994
    [1, 21, 55, 1540, 123256]

- `analyze_sequence`: differences never constant (4 levels) — not a low-degree
  polynomial; leading ratios 21, 2.62, 28, 80 — not exponential.
- `find_linear_recurrence(max_order=4)`: **no constant-coefficient linear
  recurrence of order ≤ 4 fits all 5 terms** (exact rational elimination).
- `oeis_lookup([1,21,55,1540,123256])`: **no match** (as already recorded in
  `research/notes/oeis-miss-paley-pattern-config-counts.md`).
- Closed form (I re-ran it: `python3 -c` over `k(k−2)/8` and `C(k/2,2)`):
  both give exactly `[1, 21, 55, 1540, 123256]` at all five k. This is the
  parameter-determined count `C(k/2, 2)` — the number of matching-edge pairs in
  the 7K2/k-over-2 local structure — which the tools correctly fail to re-find
  as a low-order recurrence because it is a quartic in u evaluated at five
  index points, exactly the family pattern established for every other count.

**Why it carries no leverage on the 99 problem (conjecture-classified):**
all five values are determined by the parameters alone, so the value at any
hypothetical 99 graph (2079 = 14·12/8·99/… = 14·12/8 = 21 per vertex, 99×21 =
2079) is a conditional count that holds for every srg(99,14,1,2) if one exists
and, being a parameter identity, also for BvLS — it cannot separate 99 from the
two existing controls. This is the same structure as every other family count
on disk (a = 2u+1 | 63-governed quartic).

## What would falsify anything here

- The closed form would be falsified at the next feasible family member; **no
  sixth member exists** (next candidate k = 6426 has a = 129 ∤ 63, excluded by
  the integrality five-member theorem). So the 5-term list is exhaustive over
  the family and no falsifying term is computable.
- A constant-coefficient recurrence of order ≤ 4 would falsify my
  `find_linear_recurrence` output; the tool's exact rational elimination already
  answers "none" over the terms supplied, and with no 6th term there is nothing
  further to test against.
- The BvLS Paley-pattern verification itself (13365/13365 all-is_srg) is a
  complete enumeration, not a sample; a falsifier would be a single failing BvLS
  configuration, and none exists.

## Attack on the standing verdict

The prior 27 rounds claimed the sequence line closed: every parameter-determined
count is a|63-governed and none separates 99 from its controls rook(3)/BvLS;
p-rank lists are 4-point measurements with no indexed meaning (generic-overfit
exposed in round 21); the n3-grow survivor counts are mechanism traces with no
definable extrapolation (rounds 24–25). I attacked this by (a) a mechanical
newer-than sweep over every file type that can hold terms, and (b) re-running
the two signature catalogue sequences' negative results myself in round 26's
report and the Paley-config sequence this round. No gap found: there is no
on-disk sequence I have not tooled, and the one new sequence shows exactly the
anticipated structure.

## Verdict

**NOTHING FURTHER from the sequence tools.** Both sequence-specific results of
this round — the OEIS miss and the exhaustive-over-family closed form — were
already recorded (note `oeis-miss-paley-pattern-config-counts.md`). Any
genuinely new exploitable structure for the 99 problem remains in
construction/search (the 99-vertex lift of the super-simple 2-(22,4,2) design;
the k=14 local triangle geometry), not in the sequence line. Provisional record
of this round: note `6631067530713885929` (scratch).