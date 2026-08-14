# Shared context

This run knows nothing yet. The workspace holds scaffolding only — no sources,
no computations, no claims, no memory. An agent that assumes earlier work exists
will build on nothing.

## Ground truth (this run's only unmarked input)

The problem is `problem.md`: for `Q_n` the `n`-cube, define
`f(n) = min{ D(S) : |S| = 2^{n-1}+1 }` where `D(S)` is the maximum internal
degree of `Q_n[S]`. Known bounds (both to be **re-derived here, not cited**):
`c·log n <= f(n) <= sqrt(n)`. The gap is the target; the deliverable is a proved
partial result, and GOAL.md's first-order target is any lower bound
`omega(log n)` — a thirty-year result.

## Established

Nothing. Proved: none. Computed and checked: none. Sourced: none.
`research/CLAIMS.md` is a header with *No claims recorded yet*.
`recall_memory`/`recall_scratch` both return empty. No `README`s that read as
findings are anything but seed templates.

## Ruled out

Nothing tried yet. The one thing to never re-attempt naively: enumerating
subsets of `{0,1}^n` — doubly exponential; the oracle must be posed as a SAT/ILP
decision question.

## Numbers

None computed. There are no captured outputs (`code/out/` holds only README),
no library modules (`code/lib/` empty), no oracle, no `f_exact` values.

## Recalled

Nothing. Durable memory is empty for this problem.

## Contradictions

None — there is nothing to contradict.

## Gaps

- **The oracle does not exist yet.** `f_exact(n)` / the `(n,d)` decision problem
  and the direct `degree_profile` checker must be built first (GOAL phase 3);
  nothing downstream is worth believing until its small-`n` values are hand
  verified and the known `sqrt(n)` upper construction is reproduced on disk.
- **Both known bounds are unverified here.** The `sqrt(n)` construction and the
  `Omega(log n)` induction bound must be re-derived and checked against exact
  small-`n` values before any new claim they calibrate means anything.
- Agreed structural ruling (from problem.md, to confirm against sources): any
  lower-bound technique that bounds an average cannot reach `sqrt(n)`; the
  bound must come from a quantity that is a maximum by construction. Verify this
  against the isoperimetric literature before building on it.

Pointer for detail: `problem.md` restates the whole obstruction; `GOAL.md` sets
the deliverable and compute policy.
