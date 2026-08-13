# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**. The conjecture has
been open since 1948 and is believed true, so the working assumption is that
you will not prove it. Claiming it on an argument that has not survived attack
is the one outright failure available here.

A partial result that would count:

- a **new parametric identity family** `x(k), y(k), z(k)` covering some subset
  of an open class `n = 840k + r`, verified as an identity in `k` and with the
  positivity and integrality conditions stated exactly;
- a proof that a stated ansatz **cannot** cover `n ≡ 1 (mod 840)`, with the
  obstruction named — a clean impossibility for a family of shapes is worth as
  much as a new family;
- the six open classes re-derived from scratch, with the exact reason each of
  the other 834 classes falls, and each identity verified symbolically here;
- a reproduction of the Elsholtz–Tao counting bound with its constant made
  explicit, or a located error in it;
- a precise statement of what blocks the symbolic search, naming the degree
  and shape reached, not reporting that the search did not finish.

A result stated without the bound it was established under is not a result. A
family verified for `k <= 10^4` is a fact about `k <= 10^4` unless it is proved
as an identity.

## The oracle here is a verifier and an identity checker, not a search

There is no value to recompute — the answer is a construction. So the oracle
is three things:

1. **`solves(n, x, y, z)`** — exact rational arithmetic (`fractions.Fraction`
   or integer cross-multiplication), returning whether `4/n = 1/x + 1/y + 1/z`
   with `x, y, z` **positive integers**. No floats anywhere. This is ground
   truth and every other program is measured against it.

2. **`is_identity(expr_x, expr_y, expr_z, n_of_k)`** — symbolic verification
   that a proposed family satisfies `4/n(k) - 1/x(k) - 1/y(k) - 1/z(k)`
   simplifies to **exactly zero** as a rational function of `k`. A family that
   works for the first twenty `k` and is not an identity is the failure mode
   this check exists to catch.

3. **The falsification oracle, which is the one that matters.**

> **Every claimed family must be run against the witness set**, and every
> claimed *impossibility* must be checked against known solutions.
> `code/out/witnesses.json` holds verified `(n, x, y, z)` solutions across the
> residue classes, including members of the open classes found by search. A
> lemma proving no solution exists for some `n` that the witness set solves is
> **false**. Full stop — record it refuted, not weakened.

Positivity and integrality are where these constructions die. A "family" whose
`z(k)` is negative for small `k`, or non-integral unless `k` satisfies a
further congruence, is not a covering family; it is a family plus a condition,
and the condition must be stated and its own coverage computed.

## Compute policy — light, symbolic, parallel

The instrument here is symbolic algebra over small ansätze, not a sweep over
`n`.

- **Verify identities symbolically**, in `k`, once. That settles infinitely
  many `n` and costs nothing per `n`.
- **Search ansatz space, not integer space.** Enumerate shapes — degrees,
  denominators, factorisation patterns — and test each as an identity.
- **Parallelise across the ansatz grid.** `code/lib/parallel.py` with
  `code/lib/PARALLEL.md` is in this workspace. The box has 28 CPUs and the
  container has no CPU quota. One ansatz per work item is exactly the shape
  `parallel_map` and `parallel_any` are for. State the worker count and the
  grid covered in every capture.
- **Bound every run.** Launch as
  `timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`.
  Output that only reaches the model is destroyed when the attempt ends.
- **A search that cannot finish is a finding.** Bound it, capture the partial
  result with the bound stated, and say what was not covered.

Numerical search over `n` has one legitimate use: producing witnesses for the
falsification oracle, and testing whether a proposed family actually fires on
the `n` it claims. Keep it small and bounded.

## The traps specific to this problem

**Rediscovering known families.** The residual six classes are exactly the ones
that resist the standard type I / type II shapes, and those have been searched
hard. If your ansatz produces a family, check whether it covers anything not
already covered before recording it as new. A rediscovered identity is a
correctness check, not a result.

**Reducing to primes without saying so.** The reduction to prime `n` and the
even case are standard and easy, but they must be *verified here* and recorded
as claims, because everything downstream leans on them.

**Confusing "verified for many `n`" with "identity".** State the evidence class
on every claim: proved, verified-numerically, conjectured, or
asserted-by-source.

## Ending

Stop and report when you have a partial result of the kind listed above, or
when you can state precisely what blocks the construction and why. Report the
ansatz space searched, the classes covered, the witnesses reproduced, and the
evidence class of every claim.
