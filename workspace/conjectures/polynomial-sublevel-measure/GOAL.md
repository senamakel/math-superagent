# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on `inf mu(f)` and
`sup mu(f)`, where `mu(f)` is the Lebesgue measure of `{x : |f(x)| < 1}` and `f`
ranges over non-constant monic real-rooted polynomials with all roots in
`[-1,1]`.

## First task, before any mathematics

Establish, from primary sources, **which half of this problem is still open.**
The problem page reports `sup mu = 2*sqrt(2)` as known and the infimum bracketed
by `2^{4/3} - 1 <= inf <= 1.835...`. Verify this. Record the finding in
`CONTEXT.md` under Established with its evidence class and its source. If the
supremum is settled, this run is the infimum problem and everything else is
calibration.

## What a result looks like, in descending order of value

1. **The exact value of `inf mu`**, with a matching construction and proof.
2. **An improved construction** — any `f` with `mu(f) < 1.835...`, certified by
   exact arithmetic. This is checkable, immediate, and entirely within reach.
3. **An improved lower bound** above `2^{4/3} - 1`, proved.
4. **The per-degree extremal problem solved exactly** for a range of degrees,
   with the structure of the optimiser identified (interior critical point,
   repeated roots, endpoint clustering) and a conjecture for its limit.
5. **A refutation of a natural approach**, with the obstruction named exactly.

## What must exist before any claim is believed

- `code/lean/Lib/Statement.lean` typing the two extremal quantities, with
  monic-ness, real-rootedness and the root interval as binders, ending in
  `sorry`.
- A certified exact `mu(f)` evaluator, verified by hand on `f(x) = x`
  (`mu = 2`) and on `f(x) = (x+1)(x-1)^3`.
- Every number the run reports carrying its arithmetic: exact algebraic,
  interval-certified, or floating-point-heuristic. **Three decimal places
  decide this problem, so an uncertified decimal is not evidence.**

## The falsification oracle

Every claimed lower bound on `inf` is run against the optimiser's best witness
and against the standard family `(x+1)(x-1)^m`; a bound that exceeds a certified
computed `mu` is **refuted**, not weakened. Every claimed upper bound on `sup`
is run against root configurations at the endpoints `{-1,+1}`, which is where
`2*sqrt(2)` comes from.

Note the asymmetry that makes this problem safe to work on: both extrema are
*witnessed* by explicit polynomials, so a false claim in either direction dies to
a finite exact computation. Use that. There is no excuse here for an unrefuted
false bound.

## Stop conditions

A proved value or improved bound with its evidence class, or an exactly stated
gap. Not: the literature being exhausted, or the optimiser reaching a higher
degree.
