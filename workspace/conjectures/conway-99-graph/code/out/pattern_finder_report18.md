# Pattern-finder report — round 18: the n3-seed survivor-growth sequence, run through the tools for the first time

## The one sequence earlier rounds missed

Rounds 1-17 mined the parameter-determined family counts exhaustively and
declared the catalogue closed. One on-disk integer sequence had **not** been
run through the exact tools: the survivor counts of the n3-seed local-extension
search (`code/out/n3_grow_radius.captured.txt`). The seed (two disjoint
triangles joined by exactly 2 edges) is grown under the sound rule (3)
(lambda-witness materialisation) and the number of locally-consistent
extensions counted at each radius:

- survivor counts, radii 0..6: `[1, 2, 5, 11, 19, 19, 19]`
- max materialised vertices per radius: `[6, 8, 9, 11, 12]`

## Exact tools, this round

`analyze_sequence([1,2,5,11,19,19,19])`: differences never become constant at
any level (level-1 diffs `[1,3,6,8,0,0]`), so **not a low-degree polynomial**.
`find_linear_recurrence(max_order=6, [1,2,5,11,19,19,19])`: **no**
constant-coefficient linear recurrence of order <= 6 fits all 7 terms.

`oeis_lookup([1,2,5,11,19])` matches several entries (A208970, A327265, A097008,
A319859); `oeis_lookup([6,8,9,11,12])` matches A000201, A003106, A007494,
A328594. All are **spurious coincidences**: A208970 is a 2-D necklace table
read by row, A000201 is the lower Wythoff/Beatty sequence whose early terms
happen to contain 6,8,9,11,12, and the other matches are short-prefix
coincidences. None carries a closed form or a combinatorial meaning for this
problem, and none is an exact fit to the *whole* survivor sample.

## Why this is not exploitable structure

The survivor counts are a **search-state artifact**, not a graph invariant or a
parameter-determined family count. They track the specific growth rule's
enumeration geometry (how many rule-(3) witnesses the seed forces and how the
7K2/deficit checks prune each radius's product of free bits), not any property
of a putative srg(99,14,1,2) that separates it from the controls rook(3) and
BvLS. The plateau at 19 from radius 5 to 6, and the radius-6 stable fixpoint
(0 free bits, no witness materialised, none died), is exactly the already-checked
claim `n3-seed-locally-consistent-radius1` — the seed extends locally to every
radius, so there is no local obstruction. That is a *local* statement; the
global obstruction, if any, lives in the ~91 outside vertices and no sequence
tool touches it.

## Verdict

- **Checked (this round):** the survivor sequence is not polynomial and not a
  low-order linear recurrence; its OEIS matches are spurious.
- **First-falsifying term:** none — this is a fixed finite search trace (6-7
  terms), not a fitted pattern with an extrapolating term to break. The plateau
  is a stable fixpoint already characterised by the radius-1-and-beyond claim.
- The parameter-determined catalogue of rounds 1-17 remains unchanged, and
  every item in it separates 99 from the controls **only** via the coclique
  bound 22 and the forced n3>=3 (Makhnev conditional) — neither a sequence.

## Recommendation

The sequence line is fully closed (rounds 1-18). Genuinely new exploitable
structure, if any, is construction/search: the full 99-vertex lift of the
super-simple 2-(22,4,2) design, and the k=14 local triangle geometry. NOTHING
FURTHER is available from the sequence tools.
