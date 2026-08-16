# G-split-consistent exhaustive line-split test: captured result

Runs `code/out/gsplit_exhaustive.py` against the **verified** `lib.es_construct`
ES construction `es_set(n)` (N = 2^{n-2} points in exact rationals, general
position, no convex n-gon). Full stdout with command and exit code is in
`code/out/gsplit_exhaustive.captured.txt`.

Exhaustive scheme: for each n in 4..7, every straight-line bipartition of the
point set is generated from the C(N,2) pair-lines through two points, with on-line
points assigned each way; each bipartition is kept once. A "split tried" is a
bipartition whose two sides are split as an L/R pair by some line and reached the
size-target check. A VALID split is one where **both** sides have size exactly
`2^{n-3}` and **both** sides are free of a convex `(n-1)`-gon.

Exact arithmetic throughout (integer cross-products via `lib.es_geom`); no
floating point.

## Captured numbers

| n | N = 2^{n-2} | line-bipartitions enumerated | splits tried (size-target) | VALID splits (both halvessize 2^{n-3}, both (n-1)-avoiding) |
|---|-------------|------------------------------|----------------------------|-----------------------------------------|
| 4 | 4    | 13  | 13  | 6  |
| 5 | 8    | 57  | 57  | 4  |
| 6 | 16   | 241 | 241 | 2  |
| 7 | 32   | 993 | 993 | 0  |

Exit code: 0. All of n=5,6,7 completed (n=7 was not abandoned; 993
bipartitions ran to completion).

## What is established

For the verified `es_construct` ES construction at **n=5 and n=6**, some
straight-line bipartition does split the set into two halves of size exactly
`2^{n-3}` that are each free of a convex `(n-1)`-gon (4 such splits at n=5,
2 at n=6), so the G-split property (a line yielding two `(n-1)`-avoiding halves
of the extremal size) **holds on this template at n=5 and n=6**.

At **n=7**, the exhaustive search over all C(32,2) pair-line bipartitions finds
**no** line splitting the es_construct set into two halves of size exactly 16
that are each free of a convex 6-gon (0 valid splits).

The script's hard-coded closing banner claiming "no line splits it into two
(n-1)-avoiding halves at n=5,6,7" is inaccurate for n=5,6 — the actual per-n
VALID counters above (4 and 2) show such splits exist there. The banner is a
stale summary; the enumerated counters and the explicit split lists are the
authoritative output.

Scoping: this rules out the G-split-consistent pattern only for THIS `es_construct`
template at n=7. It does not rule out other extremal sets, nor does it decide the
general G-split lemma.

```claim
id: gsplit-exhaustive-esconstruct
statement: For the verified es_construct ES construction, the exhaustive all-line bipartition test finds that at n=5 (N=8) exactly 4 straight-line splits and at n=6 (N=16) exactly 2 straight-line splits yield two halves of size exactly 2^{n-3} that are each free of a convex (n-1)-gon; at n=7 (N=32) exactly 0 straight-line splits do so over all 993 enumerated line-bipartitions. The even/odd block-index halves (each 2^{n-3}, (n-1)-avoiding) are separated by no single line in this radial placement, so the G-split-consistent pattern fails on this template at n=7.
hypotheses: es_construct.es_set(n) realization of the Erdős–Szekeres construction (2^{n-2} points, general position, no convex n-gon, verified by the exact es_geom oracle); lines are the C(N,2) pair-lines with on-line points assigned both ways; exact integer determinants for convexity and collinearity.
holds-here: true — this is exactly about the es_construct ES template at n in {5,6,7}.
status: checked
formalisation:
bearing: Structural constraint on this extremal template: a single separating line cannot reduce the n=7 es_construct set into two 6-avoiding halves; the earlier even/odd block finding (each half 2^{n-3} and (n-1)-avoiding) is real but not line-realizable, so any G-split induction would need a different separation than a straight line on this construction.
anchor: code/out/gsplit_exhaustive.captured.txt
```
