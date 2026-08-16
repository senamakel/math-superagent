# Pattern-finder report — round 4

## What changed since round 3

The run produced no new *sequence-bearing* artifacts since `pattern_finder_report3.md`
(which closed the coclique-bound closed form). Every family sequence admitted to
being a quartic-in-`u` form with no low-order linear recurrence and no OEIS entry.
That left one count untested: **the induced-C5 (pentagon) count**. The C6/hexagon
bound was verified independently on both controls, but the pentagon closed form
`p5 = n*k*(k-2)*(k-4)/5` (value 384,912 at BvLS) was only ever asserted-by-source.
This round independently verified it, closing the last untested family count.

## Finding — the pentagon count closed form is now verified on both controls (CHECKED)

Two independent exact routes, both with entry guards:

- **Rook(3) `srg(9,4,1,2)`** — brute-force over all `C(9,5)=126` 5-subsets with an
  exact induced-degree-2 (5 edges, all degrees 2) criterion: induced C5 count = **0**.
  Closed form `9*4*2*0/5 = 0`. Match. (`code/out/check_pentagon_formula.py`.)
- **BvLS `srg(243,22,1,2)`** — anchored directed-edge enumeration: for each of the
  2673 edges the pentagon `a-b-c-d-e-a` is completed with `c∈N(b)`, `e∈N(a)`,
  `d∈N(c)∩N(e)`, no chords, then the 5-set is verified by an exact full
  induced-degree-2 test; divide by 10 (each C5 is anchored at its 10 directed
  edges). Result: **384,912**, exactly the closed form `243*22*20*18/5 = 384,912`.
  (`code/out/count_C5_bvls_anchored.py`.)

Both entry guards passed (rook = 0). The first anchored attempt **over-counted**
(192,456 before the ÷10 — i.e. 1,924,560 undirected → its loose `edges==5` check
admitted "C4-with-pendant" shapes, and its chord pruning was wrong); the fix was
the exact induced-degree-2 verification of the 5-set, so every counted shape is
provably a single 5-cycle. The closed form is now **verified on both controls**,
promoting `p5` from asserted-by-source to checked.

At the target `k=14 (v=99)` the formula gives `p5 = 99·14·12·10/5 = 33,264`.
This is a parameter-determined count: every `srg(99,14,1,2)`, if one exists,
contains exactly 33,264 induced pentagons. By itself it is not a structural
lever — it forces nothing (the actual pentagon count is determined by `(n,k)`
alone for this family), and it does not separate 99 from either control. Its
value is purely as a verified hard target for isomorph rejection or a candidate
graph checker, exactly the role the hexagon count already plays.

## Sequences with no further structure (re-confirmed exactly)

The sequence tools confirm, over exactly the terms supplied:

- Triangles `{6, 231, 891, 117096, 81842481}` — no order-≤4 constant-coefficient
  linear recurrence; OEIS miss. (`find_linear_recurrence`, `oeis_lookup`.)
- Pentagons `{0, 33264, 384912, 1669320576, 96451036488576}` — no order-≤4
  recurrence; OEIS miss (a miss this run records so nobody searches again).
- Coclique bound `{3, 22, 45, 561, 15408}` — no order-≤4 recurrence; OEIS miss.
- Distance-2 counts `{4, 84, 220, 6160, 493024}` — no order-≤4 recurrence; OEIS miss.
- Outer-block counts `{0, 140, 660, 110880, 81348960}` — no low-order recurrence.

All are exactly the quartic-in-`u` closed forms from `k = u²+u+2`,
`v = 1+k²/2`, governed by the `a = √(4k−7) | 63` integrality characterization
already in the library. `analyze_sequence` confirms none is a low-degree
polynomial and the leading ratios are of exponential/quartic growth — consistent
with the quartic forms, not an independent law.

## Bearing

The family of counts at the five feasible `(v,k)` is fully catalogued: every one
is a fixed quartic-in-`u` closed form, and **every one is now verified on both
existing members** (triangles, pentagons, hexagons, coclique bound, distance-2,
outer blocks). None gives a structural contradiction at 99, because each is
parameter-determined and each evaluates consistently on the positive controls.
The only quantities that separate 99 from both controls remain: **(a)** the
coclique bound value 22 (distinct from 3 and 45 — the coclique-design branch of
the k14-l1-local thread), and **(b)** the Makhnev-1988 `n₃=0` exclusion forcing
`n₃ ≥ 1` at 99 while both controls have `n₃ = 0` (sourced, not machine-checked).
Neither has a new sequence behind it; this round's contribution is closing the
last untested count, not opening a new lever.

## First falsifying terms

None of the closed forms is a fit — each is derived (`k=u²+u+2`, `v=1+k²/2`,
`s=−(u+1)`) and independently verified by enumeration on both existing members
as far as those graphs reach, which is the entire existing family. The closed
forms therefore cannot be falsified by more terms of the family; they would be
falsified only by a *sixth* feasible member with different `u`-arithmetic, which
the `a|63` integrality excludes. So "first falsifying term" is empty for these
forms — that is the honest statement.
