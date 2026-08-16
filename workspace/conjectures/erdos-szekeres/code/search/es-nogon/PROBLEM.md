# Scoreboard problem: es-nogon — search for a no-convex-n-gon point set

## Objective

Score a **candidate module** that exposes a single callable

```python
points(k) -> list of (x, y) integer pairs
```

The scorer's job is to measure, and independently certify, the largest candidate
set the module can produce on a given rung `k` **without** containing `k` points
in convex position. A higher certified count is a better score.

The Erdős–Szekeres conjecture says a set of size `2^{k-2}` with no convex `k`-gon
(an "es-k-nogon set") should exist for every `k`. The rungs are:

| k  | target size | status of ES(k)          |
|----|-------------|--------------------------|
| 6  | 16          | ES(6) = 17 is known; max no-6-gon size 16 (known rung) |
| 7  | 32          | record is 32; ES(7) is **open** |

So the first milestone is `k = 6` at count 16 (a known rung that lets the scorer
and the search harness be validated against a ground-truth answer), and the real
target is `k = 7` at count 32 — the current record as a no-7-gon construction.

## The scorer (this folder's `score.py`)

`python score.py <module_path> [k]`

Import `<module_path>` (a `.py` file or a dotted module name on `PYTHONPATH`),
calling `points(k)`. The scorer then prints **exactly one** verdict line:

- `SCORE: n`   — where `n = len(points)`, and **all** of the following held:
  1. points are distinct, with integer coordinates;
  2. the set is in general position (no three collinear) — exact integer
     determinant / orientation, never floating point;
  3. no `k` points lie in convex position.

- `INVALID: <check> — with a witness` — at the first failed check.
  The witness is a concrete subset or triple (a collinear triple, or the
  specific `k` points found in convex position).

### How the "no k points in convex position" check is made exact but fast

The naive scan is `C(N,k)` convexity tests (`C(32,7) = 3,365,856`). To stay far
under the 10-second budget at `k = 7` we use two layers:

1. **Onion-layer precheck (sufficient, never necessary).** Peel convex hull
   layers. If any single hull layer has `>= k` points, those points are
   themselves a convex `k`-gon (every hull layer is a convex polygon), so the
   candidate is INVALID immediately with that layer as the witness. This catches
   most invalid candidates in `O(N^2)`.
2. **Exact parallel enumeration (the authority).** Because a hull layer of size
   `< k` does **not** imply the absence of a convex `k`-gon (that implication is
   false — verified against brute force on thousands of random sets), every
   candidate that survives the layer precheck must still be checked exactly.
   `score.py` enumerates the `C(N,k)` subsets in parallel across all available
   cores, testing each with `lib.es_geom.in_convex_position` (exact integer
   hull). Any convex `k`-subset found is reported INVALID with its witness; if
   none is found the set is certified SCORE `n`.

The enumeration is the ground truth; the layer peel is only an accelerator that
never overrides it.

### Exact arithmetic only

All geometry goes through `lib.es_geom` (`orient`, `in_convex_position`) and is
exact integer-determinant arithmetic. No floats anywhere. The self-test in
`scorer_selftest.captured.txt` proves the scorer:
- SCOREs 16 for `es_construct(6)` (no 6-gon at k=6),
- SCOREs 32 for `es_construct(7)` (no 7-gon at k=7),
- prints INVALID for a collinear set and for a 17-point set (which must contain
  a convex 6-gon, as ES(6) = 17).

### Boundary of this problem

This is *not* the monotone-subsequence Erdős–Szekeres theorem, not an
asymptotics estimate, and not the empty-hexagon problem. It is exactly: find, or
fail to find, an explicit integer-point set of a given size with no convex `k`-gon.
A candidate that certifies a no-`k`-gon set of size `> 2^{k-2}` would refute the
conjecture; the scorer is built to report exactly such a finding rather than
silently cap it.
