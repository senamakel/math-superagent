# Pattern-finder report — round 24: the last untooled on-disk sequence, closed

## What I did

Rounds 1–23 (00:02–00:51) declared the sequence line fully closed twice. Before
inheriting that verdict, I re-confirmed the exclusivity of the mined surface and
found one on-disk integer sequence earlier rounds never explicitly ran through
the exact tools: the **n3-seed survivor-count-per-radius** list from
`n3_grow_radius.captured.txt` (radius 0 → 6 all present there; wall clock 1.1s).

## The sequence

Extracted from the radius-growth capture, at each radius the number of distinct
survivors under the sound upper-bound growth rule (free-interior-bit complete
enumeration):

    radius:     0  1  2  3  4  5  6
    survivors:  1  2  5 11 19 19 19

This is the search-trace of the growth loop, not a parameter-determined family
count. (Radius 1 = 2 is the verified self-check anchor; radius 6 is the stable
fixpoint with 0 free bits, at which the seed extends locally to every radius.)

## Exact sequence tools (first tooling of this list)

`analyze_sequence([1,2,5,11,19,19,19])`:
- differences never become constant within 6 levels → **not a low-degree polynomial**.
- leading ratios 2.0, 2.5, 2.2, 1.73, 1.0, 1.0 → not exponential.

`find_linear_recurrence(max_order=4, [1,2,5,11,19,19,19])`:
- **No constant-coefficient linear recurrence of order ≤ 4 fits all 7 terms.**

`oeis_lookup([1,2,5,11,19,19,19])`:
- **No match.** (Also worth noting: the even columns of the catalogue —
  e.g. C3 spectra — already exhausted in rounds 19/22/23.)

## Why this is bookkeeping, not structure (so a reported pattern would be noise)

The survivor counts are an artefact of the **enumeration mechanism**, not an
invariant of any object:

1. They measure how many free-interior-bit assignments survive the sound
   upper-bound checks at a patch that is being materialised witness-by-witness
   by rule (3). Diffrent witness-materialisation order / choice among witnesses
   would give different intermediate counts.
2. There is no index `n` whose growth carries meaning independent of the
   mechanics: the plateau 4→5→6 (19, 19, 19) is the patch reaching its stable
   fixpoint (0 free bits, no new witnesses), i.e. a property of the growth rule
   stopping, not of a sequence converging.
3. It carries no lower bound that over-subscribes the 231-line / 693-incidence
   budget — the same conclusion the ledger already drew (residuals 223–227
   lines, 669–681 incidences always absorbable).
4. This is the same failure mode round 18/20/21 flagged for search-traces: a
   fitting target only in the sense that any finite list of integers admits a
   polynomial/recurrence fit, and none of those fits means anything here.

There is therefore **no first term that would falsify a conjectured pattern**:
the "sequence" has no definable extrapolation, so no break term exists. The
absence of OEIS match is a real (if minor) negative: it confirms the terms are
not a catalogued growth pattern by some independent meaning.

## Consequence

The one candidate sequence the earlier rounds had not tooled is now tooled and
shows no structure — consistent with, not contradicting, the standing verdict
that every parameter-determined count on disk is `a=2u+1 | 63`-governed and none
separates 99 from its controls rook(3)/BvLS.

The only 99-specific structural values remain the **coclique bound 22** and the
**forced n3 ≥ 3** (Makhnev conditional) — neither a sequence.

## Verdict

NOTHING FURTHER is available from the sequence tools. The sequence line is
closed across rounds 1–24 with no gap found. Genuinely new exploitable
structure, if any, is in construction/search: the 99-vertex lift of the
super-simple 2-(22,4,2) design, and the k=14 local triangle geometry.

## Files
- `code/out/n3_grow_radius.captured.txt` — the source (survivor counts per radius).
- This report (`pattern_finder_report24.md`).
