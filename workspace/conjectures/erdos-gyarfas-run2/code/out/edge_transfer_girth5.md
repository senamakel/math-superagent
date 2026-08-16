# Edge-transfer good-chord search on the girth-5 danger region (n = 10, 11)

The earlier chord-deletion scan (`edge_transfer_worstcase.py`) found **no worst
case for n ≤ 8** — every δ≥3 graph there has girth ≤ 4 and hence a 4-cycle, which
makes every chord good. The genuine danger region is girth ≥ 5, which the Moore
bound places at n ≥ 10. This scan attacks exactly that region.

## The good-chord definition (from `research/approaches/edge-deletion-2adic-transfer.md`)

A **deletable chord** e = ab of a 2-connected δ≥3 graph G is an edge such that
H := G−e is 2-connected and δ(H) ≥ 2 (Lemma A guarantees one exists). Such a
chord is **GOOD** when the single induction step closes:

> C(H) contains a power of two (4, 8, 16, …)  **OR**  H has a simple a–b path of
> length 2^k − 1 (3, 7, 15, …).

A graph is a **worst case** when it has *no* good deletable chord — exactly where
the induction stops (`edge-deletion-2adic-transfer.md`'s open content).

## The reduction used, and why it is exact here

Structural fact, cross-checked (see below): if G has a 2^k-cycle, then **every**
deletable chord is good (a 2^k-cycle either avoids e and lies in H, or passes
through e and its complement in H is an a–b path of length 2^k − 1); conversely
a good chord certifies a 2^k-cycle in G. So

> bad graph ⇔ G has no power-of-two cycle.

For girth ≥ 5 on n ≤ 11 the only possible power-of-two cycle length is **8**
(C4 is forbidden by girth; C16 needs ≥ 16 vertices). So the whole scan reduces
to: *does every 2-connected δ≥3 girth-5 graph on n = 10, 11 have an 8-cycle?*
That is exactly the n ≤ 12 rung of `research/WEAKENED.md`.

**The Moore bound already sharpens this to a single graph.** For min-degree-3,
girth ≥ 6 needs n ≥ 14 and girth ≥ 7 needs n ≥ 22, so on n ≤ 11 any min-degree≥3
girth≥5 graph has girth exactly 5, and at n = 10 the min degree is exactly 3
(Moore-bound equality). The (3,5)-cage is the Petersen graph.

## Results

### Petersen (n = 10, the only δ≥3 girth-5 graph on ≤ 10 vertices)

| Quantity | Value |
|---|---|
| girth | 5 |
| min degree | 3 |
| n | 10 |
| Petersen's own power-of-two cycle | 8-cycle present |
| deletable chords (2-connected & δ≥2 after deletion) | 15 |
| GOOD deletable chords | **15 / 15** |
| NOT GOOD (bad) chords | **0** |

**Every deletable chord of Petersen is good.** (Confirmed by the full per-chord
definition: each of the 15 edges e with G−e 2-connected and δ(G−e)≥2 either
leaves an 8-cycle in G−e or yields an a–b path of length 7 in G−e.)

### Enumeration: 2-connected min-degree≥3 girth-5 graphs, n = 10 and 11

| n | graphs in class | with an 8-cycle | worst cases |
|---|---|---|---|
| 10 | **1** (Petersen) | 1 | **0** |
| 11 | **0** | – | **0** |

Generation via `lib.girth5_gen` (C5-seeded open-ear decomposition, girth-pruned,
WL-hash + VF2 dedup), validated complete for the min-degree≥3 class by matching
the full 2-connected generator filtered by girth≥5 and δ≥3 (all n ≤ 7 agree; the
only discrepancies at larger girth are min-degree-2 graphs, correctly excluded).

## Verdict

**No worst case exists.** Every 2-connected min-degree≥3 girth-5 graph on
n = 10, 11 — the genuine danger region below the Moore-bound floor — has a
power-of-two cycle (specifically an 8-cycle), so every deletable chord is good
and the single chord-deletion induction step closes. Combined with the n ≤ 8
scan (all girth ≤ 4, hence a 4-cycle), **the chord-deletion step closes on every
2-connected δ≥3 graph through n = 11.**

The class is so small because the Moore bound confines it: at n = 10 to a single
graph, Petersen, and at n = 11 to nothing. The first genuine open danger begins
at n ≥ 12 (still girth 5), where the class first has room for non-cubic and
multiple graphs — consistent with the standing obstruction (ROOT §1) and Balaji's
verification bound.

*(Context note, outside the requested bound: at n = 12 the same scan already finds
2 such graphs, both with 8-cycles, so the pattern continues as the Moore floor is
crossed — but the requested decision for n = 10, 11 is complete and clean.)*

## Files

- `code/lib/girth5_gen.py` — C5-seeded girth-5 2-connected generator (pruned,
  hash+VF2 dedup), with the open-ear theorem and girth measure.
- `code/out/edge_transfer_girth5.py` — Petersen test + full enumeration + per-chord
  good-chord scan.
- `code/out/edge_transfer_girth5.out` — captured stdout.
- `code/out/check_girth5_gen.py` — validation of the generator's completeness for
  the δ≥3 class against the full 2-connected generator.
