# Pattern-finder report — round 8: the n3-seed radius-growth trajectory (new), closes the sequence catalogue

## What changed since round 7

Round 7 catalogued the C3 triangle-graph spectra. The run's single newest, most
incomplete artifact is the **local-extension radius growth** of the n3 seed —
the 2-edge-joined disjoint triangle pair forced at 99 by Makhnev's n3≥1
(`code/out/n3_grow_radius.captured.txt`). No prior pattern round had tabulated
this per-radius survivor/vertex trajectory. It is also the only non-parametric
quantity in the whole investigation, so it is the one place a structural
regularity *should* live. I reproduce it freshly, run the sequence tools, and
close it.

## The data (freshly re-run this round, exact complete enumeration)

Sound engine (`n3_grow_radius.py`, complete enumeration of free interior bits,
no floats), self-checked to reproduce radius-1 = 2 survivors before trusting
larger radii:

| radius | survivors | max vertices | max free bits |
|---|---|---|---|
| 0 | 1 | 6 | 0 |
| 1 | 2 | 8 | 9 |
| 2 | 5 | 9 | 6 |
| 3 | 11 | 11 | 15 |
| 4 | 19 | 11 | 8 |
| 5 | 19 | 12 | 9 |
| 6 | 19 | 12 | 0 (fixpoint) |

The re-run reproduces every row exactly (wall clock ~1.1s). Radius 6 is a
**stable fixpoint**: no survivor materialises a new witness and none dies, so
the seed extends *locally to every radius* under the sound criterion. Radius 6
is also a genuine "hard target": every survivor has free bits 0, i.e. all
interior adjacencies are fully decided and consistent.

## Sequence-tool results (exact over the terms supplied)

Survivor counts `[1, 2, 5, 11, 19, 19, 19]` and max-vertices `[6, 8, 9, 11, 11, 12, 12]`:

- `analyze_sequence`: neither is a low-degree polynomial; differences never
  stabilise (the flattening 11→19→19→19 is a *plateau* at the fixpoint, not a
  polynomial limit).
- `find_linear_recurrence(order ≤ 5)`: **no constant-coefficient linear
  recurrence fits either** — expected, since the growth is not governed by a
  `u`-parameter formula but by the discrete rule-(3) witness closure.
- `oeis_lookup([1,2,5,11,19])`: 4 matches, all **spurious** — necklace counts
  and partition expansions (A208970, A327265, A097008, A319859) that agree on
  the early terms and have nothing to do with a bounded local-extension
  enumeration that reaches a stable fixpoint. Recorded as a miss: none is the
  law here.

So the radius trajectory shows **no algebraic hidden law** — and that is the
honest, load-bearing point. The growth is an *enumeration count*, not a
parameter-determined count, and it is governed by the local rule set, not by the
`srg(v,k,1,2)` arithmetic. There is no recurrence to extract.

## The one structural fact the trajectory establishes (conjecture-grade)

The salient *non-sequence* fact is the **stable fixpoint at radius 6** with all
19 survivors fully decided (free bits 0). Two readings:

1. **Strongest honest claim.** Under the sound local criterion (adjacent ≤1
   common neighbour, non-adjacent ≤2, degree ≤14, 7K₂ preserved), the
   Makhnev-forced n3 seed extends locally *indefinitely* — radius 6 already
   reaches the fixpoint where nothing further can change. There is **no local
   obstruction** at any radius, so the n3-seed killing line, as a purely local
   argument, is a dead end *for these rules*. This matches report-2's sound
   result (2 satisfying assignments, not the superseded engine's
   CONTRADICTION) and extends it from radius 1 to the fixpoint.
2. **What it does not show.** Local extendability says nothing about global
   existence of srg(99,14,1,2): the ~90 un-materialised vertices absorb all
   deficits, so the seed's consistency here is a lower bound, not a graph.

## Why this is a conjecture, and the first falsifying term

- The fixpoint claim holds **exactly over the enumeration actually run** (radii
  0–6, complete products of free bits, `≤ 2^9` per survivor). It is a
  **checked computation**, and re-running it reproduces every row.
- Its *generalisation* — "the seed extends locally to every radius" — is **not**
  a proof. It is a conjecture whose supporting computation reached radius 6 and
  found a fixpoint with free bits 0. The first term that would break it: a
  radius-7+ enumeration producing **0 survivors** (a genuine local obstruction
  the radius-6 fixpoint does not see). Because radius 6 has all-free-bits-0, a
  future radius cannot change anything — the fixpoint is structural — so within
  *this rule set* the conjecture is closed; it would be refuted only by an
  additional sound local rule (e.g. a deeper mu-witness argument) that radius 6
  did not apply. Named precisely, that is the honest bound on the claim.

## Bearing on the open problem

This closes the last quantity the sequence tools can be run on. The full
catalogue now stands:

**Parameter-determined family counts** (all quartic-in-`u` closed forms from
`k=u²+u+2`, `v=1+k²/2`, `s=−(u+1)`, `a=2u+1|63`; all verified on both existing
members; none a low-order recurrence; OEIS misses recorded): triangles,
pentagons, hexagons, outer blocks, distance-2, coclique bounds ({3,22,45,561,
15408}), eigenvalue multiplicities, C3 spectra (round 7), n3 cap
(`v·k(k−2)/4`, round 6). **None separates 99** — each is fixed by parameters
and holds on the controls.

**The only 99-specific quantities** that separate 99 from rook(3) and BvLS begin
and end with the coclique bound **22** (round 3) and the forced **n3≥1** hence
**n3≥3** (rounds 2/6, Makhnev conditional). The n3 seed's *local* consistency is
now settled to the fixpoint (this round): the n3≥1 case cannot be killed by a
local obstruction of this rule set, and the remaining question is global.

**Recommendation.** The sequence line is exhausted — every family count is an
`a|63` quartic, and the only non-parametric count (the n3 radius trajectory) is
an enumeration, not an algebraic sequence. The lever the numbers point at is
unchanged and now isolated: the **22-coclique / 2-(22,K,2) design branch** and
the **Wilbrink–Brouwer counting inequality (Lemma 1)** applied at 99, where 22
is the one exactly-derivable 99-only value the controls (3 and 45) cannot reach.
That is the structural thread, not a sequence.

## Files

- `code/out/n3_grow_radius.py` / `code/out/n3_grow_radius.captured.txt` — source data, re-run this round.
- This report (`code/out/pattern_finder_report8.md`).
