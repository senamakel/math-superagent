# Thread: Minkowski-sum construction and the forced-pair/5-chromatic crux

```thread
question: Can accumulating rigidity from small unit-distance graphs — via
  Minkowski sums A+B and rotation/spindling — force a pair (u,v) with
  |u-v| >= 1/2 that is monochromatic in EVERY 4-colouring, in a graph that is
  itself 4-chromatic? If yes, the spindle skeleton gives chi(plane) >= 5.
status: open — dead for the spindle itself and for Moser+Moser (first sum);
  needs a strictly richer base graph.
rests-on: minkowski-sum-unit-distance-condition, minkowski-sum-dense-graphs,
  sat-k-colourability-encoding, critical-minimum-degree
blocked-by: the run's own complete forced-pair SAT test found NO forced pair
  in the Moser spindle (10 pairs, k=4) or in Moser+Moser (26v,69e,256 pairs,
  k=4); both are 4-colourable. A richer base graph is required.
next: feed denser / more rigid candidate base graphs through the SAME complete
  forced-pair SAT harness (code/forced_pair.py): other Minkowski sums
  (triangle+wheel, rotation-coincidence sums per minkowski-sum-dense-graphs),
  and graph products / spindlings that accumulate rigidity. Each candidate is a
  finite SAT query per qualifying pair. Exact field Q(sqrt3,sqrt11).
```

## Why this thread exists

`problem.md` names Minkowski sums + rotations as the construction engine and
the path to accumulated rigidity. The library's two Minkowski claims
(`minkowski-sum-unit-distance-condition` — the exact distance-1 identity the
whole method rests on — and `minkowski-sum-dense-graphs` — that many
densest-known small UDGs are such sums) are the sourced backing. But the run's
own measurement (`code/out/forced_pair.captured.txt`, recalled in CONTEXT.md)
killed the first two candidates. The measure of progress on the lower bound is
whether a new construction forces such a pair.

## What the library gives this thread

- `minkowski-sum-unit-distance-condition`: a unit distance in A+B iff
  |(a1-a2)+(b1-b2)| = 1. This is the exact finite computation governing which
  pairs of the sum are edges — verifiable symbolically, no floats. Could be
  upgraded from `asserted` to `checked` by a quick exact rational verification
  (workspace scholar wrote code/scholar_verify_library.py to do the cheap ones;
  needs a tool_builder run to produce captured output).
- `sat-k-colourability-encoding`: the complete colouring oracle already
  calibrated on the Moser spindle (chi=4 reproduced).
- `critical-minimum-degree`: any 5-critical candidate must have min degree >= 4;
  the size-bound skeleton's S-critical-degree gap is discharged by this.

## What it does NOT give

- Whether sums of 4-colourable UDGs can ever raise chi above 4 — this is OPEN
  (REQUESTS row) and is exactly the computation to run, not a source to fetch.
- The general chromatic effect of spindling — OPEN (REQUESTS row), to derive.

## Falsifiers kept in mind

A proof that sums of 4-colourable UDGs are always 4-colourable would kill this
thread's central hope (but not the size-bound rung).
