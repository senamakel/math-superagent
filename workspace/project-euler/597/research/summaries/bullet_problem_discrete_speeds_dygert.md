# Dygert, Kinzel, Junge, Raymond, Slivken & Zhu, "The bullet problem with discrete speeds" — summary

<!-- source: https://doi.org/10.1214/19-ecp238 | Electron. Commun. Probab. 24 (2019), paper no. 42 -->

Full text at `research/sources/bullet_problem_discrete_speeds_dygert.full.md`.

## What the source establishes

Bullets fired at one-second intervals from a fixed origin, speeds iid sampled
uniformly from a finite discrete set S = {s_n < ... < s_2 < s_1}. When a faster
bullet catches a slower one they **mutually annihilate**.

Results:
- A bullet with the **second largest** speed survives with positive
  probability.
- A bullet with the **smallest** speed almost surely does not survive.
- Both extend to exponential spacings between firing times and to certain
  non-uniform speed measures that down-weight the second-fastest speed.

This is the discrete-speed ballistic-annihilation ("bullet problem") line, the
two-sided version called ballistic annihilation by physicists.

## Why it is in the library

The PE597 survey report explicitly flagged this as the **adjacent** process and
excluded it: "its collision rule is annihilation, so it is not the right model
for this rear-removal rule." The full text is now on disk so that exclusion is
checkable against the primary source, not the run's memory.

## Bearing on PE597 — contrast, not a solver

PE597's rule is the opposite removal: on a bump the REAR (bumping) boat is
removed and the FRONT continues; bumped boats that are OUT are passed freely.
Bullet-annihilation (both removed) is structurally different, and — as the run
verified — PE597's parity depends on speed **magnitudes**, not merely their
order (w-order hypothesis refuted), whereas bullet-process survival depends
only on the speed order. No result here transfers a closed recursion for
p(13,1800).

## Consistency with the run's record

Consistent with `research/torpids_exact_combinatorics_report.md`'s rejection
of the bullet/ballistic-annihilation family as the wrong collision rule. No
contradiction.