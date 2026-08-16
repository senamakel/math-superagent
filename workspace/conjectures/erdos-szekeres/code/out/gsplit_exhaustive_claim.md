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
stale summary and has been corrected in the script (steer 7); the enumerated
counters and the explicit split lists are the authoritative output. The n=7
zero is provisional until the enumeration-completeness recheck (steer 7):
the pair-line scheme must cover all four assignments of the two on-line points
and the single-point-line rotation cases, or it may undercount.

Scoping: subject to the enumeration recheck, this would rule out the
G-split-consistent pattern only for THIS `es_construct` template at n=7. It does
not rule out other extremal sets, nor does it decide the general G-split lemma;
at n=5 and n=6 the template IS line-splittable, so the pattern holds there.

```claim
id: gsplit-exhaustive-esconstruct
statement: RETIRED (steer 11) in favour of the validated rotating-line enumerator. The all-line bipartition test on the es_construct ES construction was re-derived by `gsplit_enum_definitive.py` (validated zero-missing/zero-extra against the 2^N oracle at N=8..16) and re-captured with provenance into code/out/gsplit_phase2.captured.txt: VALID splits (both halves size exactly 2^{n-3}, both (n-1)-avoiding) in counts 4 (n=5), 2 (n=6), 0 (n=7). The n=4 count (6) is not re-derived here; this claim's n=5,6,7 verdicts are superseded by gsplit-enum-completeness-and-n7-zero, anchored at the new capture. The old pair-line scheme (2·C(N,2)+1) and the gsplit_exhaustive.captured.txt shell-error run are dead; do not cite 57/241/993 or 6/4/2/0 from them.
hypotheses: es_construct ES template at n in {5,6,7}; rotating-line enumerator validated against exact 2^N oracle.
holds-here: true — this is exactly about the es_construct ES template at n in {5,6,7}.
status: retired — superseded by gsplit-enum-completeness-and-n7-zero
formalisation:
bearing: None independently; the n=5,6,7 verdicts live in gsplit-enum-completeness-and-n7-zero (checked).
anchor: code/out/gsplit_phase2.captured.txt (new authoritative capture)
```
