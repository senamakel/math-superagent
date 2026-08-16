# Girth-5 danger-region scan extended to n=12, 13

Extends the closed n=10,11 crosscheck (`edge_transfer_girth5.py`) to the **first
open danger above the single-cage regime**.

## Why n=13 is the named boundary

For min-degree-3 graphs, girth 6 needs ≥ 14 vertices and girth 7 needs ≥ 22
(Moore bound), so girth ≥ 5 on n ≤ 13 is exactly the whole girth-5 window.
Extending to 13 settles whether **every** 2-connected min-degree ≥ 3 graph up to
n=13 has a 4- or 8-cycle:

- n ≤ 8 : girth ≤ 4, hence a 4-cycle (closure already established).
- n = 10..13 : girth-5, the 8-cycle question — and the rung where the class
  first leaves the single-cage regime (n=10 was the sole Petersen, n=11 empty).

This is the named thing n=13 settles that n=11 did not.

## Method

- **Generation** — `lib.girth5_gen.generate_2connected_girth_atleast5(13)` (the
  committed C5-seeded open-ear generator, girth-pruned, WL-hash + VF2 dedup),
  filtered to min-degree ≥ 3. Generator untouched. The generator's enumeration
  alone takes ~280–310 s, so its output is cached in `girth5_class_n13.json` and
  re-regenerated to the identical 7 graphs as an independent reproduction.
- **Verification** (asserted per graph): girth ≥ 5, min-degree ≥ 3, and an
  8-cycle via the **independent** `nx.simple_cycles` route (route 2) — no use of
  `lib.erdos_gyarfas`.
- **Good-chord test** — same definition as `edge_transfer_girth5.py` (imported
  from it, so the two cannot drift): a deletable chord e=ab (G−e 2-connected,
  δ(G−e) ≥ 2) is GOOD iff C(G−e) has a power of two (4/8/16) OR G−e has an a–b
  path of length 2^k−1 in {3,7,15,…}.

Structural reduction, established & cross-checked: for girth ≥ 5, a bad graph
(no good deletable chord) ⇔ no power-of-two cycle; on n ≤ 13 that means no
8-cycle.

## Results

| n | graphs in class | worst cases |
|---|---|---|
| 10 | 1 (Petersen) | 0 |
| 11 | 0 | 0 |
| 12 | 2 | 0 |
| 13 | 4 | 0 |
| **TOT** | **7** | **0** |

Good-chord scan: **132 deletable chords total across the 7 graphs, 132 GOOD,
0 BAD.** Every 2-connected min-degree ≥ 3 girth-5 graph on n=10..13 has an
8-cycle, so every deletable chord of every such graph is GOOD.

## Verdict

**No worst case.** The chord-deletion induction step closes over the entire
girth-5 danger region through n=13: every 2-connected min-degree ≥ 3 graph up
to n=13 (4-cycles at n≤8, 8-cycles at n=10..13) has a power-of-two cycle. The
n=12,13 class (6 graphs) is genuinely non-cubic and multi-graph, confirming the
claim leaves the single-cage regime cleanly.

Analysis wall time (cache loaded): **0.4 s** well under the 120 s budget
(generation is the ~280–310 s part, cached).

## Files

- `code/out/check_girth5_upto13.py` — the scan: generation-cache load, per-n
  verification + chord scan.
- `code/out/girth5_class_n13.json` — cached generator output (7 graphs),
  regenerated twice to the identical class.
- `code/out/check_girth5_upto13.out` — captured stdout.

```claim
statement: Every 2-connected graph with min-degree >= 3 on at most 13 vertices
  contains a cycle of length 4 or 8.
holds-here: Every 2-connected min-degree>=3 graph up to n=13.
basis: Exact enumeration via lib.girth5_gen over the girth-5 class on n=10..13
  (counts 1,0,2,4 = 7 graphs), each 8-cycle verified via independent
  nx.simple_cycles route; n<=8 has girth<=4 hence a 4-cycle (already closed).
  Good-chord scan: 132/132 deletable chords GOOD, 0 BAD -> no worst case for the
  chord-deletion induction through n=13.
status: verified-numerically
falsifies: a 2-connected min-degree>=3 graph on <=13 vertices with no 4- or 8-cycle.
```

